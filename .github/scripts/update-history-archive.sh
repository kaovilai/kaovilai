#!/bin/bash
# Incremental refresh of workstream-archive.json. Cheap by design: only queries
# items updated since the last run (not the whole history), and only ever writes
# an entry when something actually changed (new close, reopen, or a comment after
# close). Quiet closed items already archived are never re-fetched.
set -euo pipefail

# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

JSON_OUTPUT_FILE="workstream-archive.json"
GENERATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)

if [ ! -f "$JSON_OUTPUT_FILE" ]; then
    echo "ERROR: $JSON_OUTPUT_FILE not found — run backfill-history.sh once first." >&2
    exit 1
fi

LAST_RUN=$(jq -r '.generatedAt' "$JSON_OUTPUT_FILE")
LAST_RUN_DATE=$(date -u -d "$LAST_RUN" +%Y-%m-%d 2>/dev/null || date -u -j -f "%Y-%m-%dT%H:%M:%SZ" "$LAST_RUN" +%Y-%m-%d)
echo "Checking for PR/issue activity since $LAST_RUN_DATE..."

PRS=$(retry_with_backoff gh search prs is:public --author=kaovilai --updated=">=$LAST_RUN_DATE" \
    --json number,title,repository,url,state,createdAt,closedAt,updatedAt --limit 1000)
ISSUES=$(retry_with_backoff gh search issues is:public --author=kaovilai --updated=">=$LAST_RUN_DATE" \
    --json number,title,repository,url,state,createdAt,closedAt,updatedAt --limit 1000)

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Build updated/removed entries from the fresh query
echo "$PRS" | jq -c --arg type "pr" 'map(. + {_type:$type})[]' > "$TMPDIR/fresh.jsonl" 2>/dev/null || true
echo "$ISSUES" | jq -c --arg type "issue" 'map(. + {_type:$type})[]' >> "$TMPDIR/fresh.jsonl" 2>/dev/null || true

touch "$TMPDIR/fresh.jsonl"
REOPENED_KEYS="$TMPDIR/reopened_keys.txt"
: > "$REOPENED_KEYS"

while IFS= read -r item; do
    [ -z "$item" ] && continue
    repo=$(echo "$item" | jq -r '.repository.nameWithOwner')
    number=$(echo "$item" | jq -r '.number')
    type=$(echo "$item" | jq -r '._type')
    state=$(echo "$item" | jq -r '.state // "closed"') # gh search returns lowercase: open|closed|merged
    key="${type}:${repo}#${number}"

    if [ "$state" = "open" ]; then
        # Reopened (or still open): drop from archive, it's live-tracked elsewhere
        echo "$key" >> "$REOPENED_KEYS"
        continue
    fi

    workstream="$(classify_workstream "$repo")"
    if [ "$type" = "pr" ]; then
        echo "$item" | jq -c --arg org "${repo%%/*}" --arg repo "$repo" --arg type "pr" \
            --arg archiveState "$state" --arg workstream "$workstream" \
            '{number, repo:$repo, org:$org, title, url, type:$type, state:$archiveState, createdAt, closedAt:(.closedAt // null), updatedAt, workstream:$workstream}' \
            >> "$TMPDIR/updated.jsonl"
    else
        echo "$item" | jq -c --arg org "${repo%%/*}" --arg repo "$repo" --arg type "issue" \
            --arg workstream "$workstream" \
            '{number, repo:$repo, org:$org, title, url, type:$type, state:"closed", createdAt, closedAt:(.closedAt // null), updatedAt, workstream:$workstream}' \
            >> "$TMPDIR/updated.jsonl"
    fi
done < "$TMPDIR/fresh.jsonl"

touch "$TMPDIR/updated.jsonl"
UPDATED_COUNT=$(wc -l < "$TMPDIR/updated.jsonl" | tr -d ' ')
REOPENED_COUNT=$(wc -l < "$REOPENED_KEYS" | tr -d ' ')
echo "New/changed closed items: $UPDATED_COUNT, reopened (removed from archive): $REOPENED_COUNT"

jq -s \
    --arg generatedAt "$GENERATED_AT_ISO" \
    --slurpfile reopenedFile <(jq -R -s -c 'split("\n") | map(select(. != ""))' "$REOPENED_KEYS") \
    '
    (.[0].items // []) as $existing
    | (.[1:]) as $updated
    | ($reopenedFile[0] // []) as $reopened
    | ($updated | map({key: (.type + ":" + .repo + "#" + (.number|tostring)), value: .})) as $updatedPairs
    | ($updatedPairs | map(.key)) as $updatedKeys
    | ($existing
        | map(select(((.type + ":" + .repo + "#" + (.number|tostring)) as $k
                      | ($reopened | index($k)) or ($updatedKeys | index($k))) | not))
      ) as $kept
    | { generatedAt: $generatedAt
      , items: ($kept + ($updatedPairs | map(.value)) | sort_by(.createdAt))
      }
    ' \
    "$JSON_OUTPUT_FILE" "$TMPDIR/updated.jsonl" > "$TMPDIR/archive_new.json"

mv "$TMPDIR/archive_new.json" "$JSON_OUTPUT_FILE"

COUNT=$(jq '.items | length' "$JSON_OUTPUT_FILE")
echo "Archive refreshed: $COUNT total historical items."
