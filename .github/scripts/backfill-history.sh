#!/bin/bash
# One-time (or re-seed-on-demand) backfill of ALL-TIME closed/merged PRs and issues
# authored by kaovilai into workstream-archive.json. Not scheduled — run manually:
#   bash .github/scripts/backfill-history.sh
# Windows by year to stay under gh search's 1000-results-per-query cap.
set -euo pipefail

# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

JSON_OUTPUT_FILE="workstream-archive.json"
GENERATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
CURRENT_YEAR=$(date -u +%Y)
START_YEAR=2015 # comfortably before any plausible first contribution; narrows itself via empty results

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT
touch "$TMPDIR/items.jsonl"

# gh search prs' `state` field is itself "open"|"closed"|"merged" (lowercase) —
# --state=closed already returns merged PRs with state:"merged", no extra query needed.
fetch_year() {
    local kind="$1" # prs|issues
    local year="$2"
    local range="${year}-01-01..${year}-12-31"

    if [ "$kind" = "prs" ]; then
        retry_with_backoff gh search prs is:public --author=kaovilai --state=closed --created="$range" \
            --json number,title,repository,url,state,createdAt,closedAt,updatedAt \
            --limit 1000
    else
        retry_with_backoff gh search issues is:public --author=kaovilai --state=closed --created="$range" \
            --json number,title,repository,url,createdAt,closedAt,updatedAt \
            --limit 1000
    fi
}

for year in $(seq "$START_YEAR" "$CURRENT_YEAR"); do
    echo "Fetching closed PRs created in $year..."
    prs_json=$(fetch_year prs "$year")
    echo "$prs_json" | jq -c '.[]' | while IFS= read -r item; do
        [ -z "$item" ] && continue
        repo=$(echo "$item" | jq -r '.repository.nameWithOwner')
        workstream="$(classify_workstream "$repo")"
        state=$(echo "$item" | jq -r '.state // "closed"')
        echo "$item" | jq -c --arg org "${repo%%/*}" --arg repo "$repo" --arg type "pr" \
            --arg state "$state" --arg workstream "$workstream" \
            '{number, repo:$repo, org:$org, title, url, type:$type, state:$state, createdAt, closedAt:(.closedAt // null), updatedAt, workstream:$workstream}' \
            >> "$TMPDIR/items.jsonl"
    done

    echo "Fetching closed issues created in $year..."
    issues_json=$(fetch_year issues "$year")
    echo "$issues_json" | jq -c '.[]' | while IFS= read -r item; do
        [ -z "$item" ] && continue
        repo=$(echo "$item" | jq -r '.repository.nameWithOwner')
        workstream="$(classify_workstream "$repo")"
        echo "$item" | jq -c --arg org "${repo%%/*}" --arg repo "$repo" --arg type "issue" \
            --arg state "closed" --arg workstream "$workstream" \
            '{number, repo:$repo, org:$org, title, url, type:$type, state:$state, createdAt, closedAt:(.closedAt // null), updatedAt, workstream:$workstream}' \
            >> "$TMPDIR/items.jsonl"
    done
done

touch "$TMPDIR/items.jsonl"
jq -s --arg generatedAt "$GENERATED_AT_ISO" \
    'group_by(.type + .repo + (.number|tostring)) | map(.[0])
     | sort_by(.createdAt)
     | {generatedAt: $generatedAt, items: .}' \
    "$TMPDIR/items.jsonl" > "$JSON_OUTPUT_FILE"

COUNT=$(jq '.items | length' "$JSON_OUTPUT_FILE")
echo "Backfill complete: $COUNT historical items archived to $JSON_OUTPUT_FILE"
