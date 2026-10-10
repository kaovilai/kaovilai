#!/bin/bash
set -euo pipefail

# Shared utilities
# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

OUTPUT_FILE="MY_ISSUES.md"
JSON_OUTPUT_FILE="open-issues.json"

CURRENT_DATE=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
UPDATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Calculate stale date (60 days ago) - same convention as update-pr-list.sh
STALE_DATE=$(date -u -d '60 days ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-60d +%Y-%m-%dT%H:%M:%SZ)
STALE_TS=$(date -d "$STALE_DATE" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$STALE_DATE" +%s)

echo "Fetching open issues authored by kaovilai..."
AUTHORED=$(retry_with_backoff gh search issues is:public --author=kaovilai --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000)

echo "Fetching open issues assigned to kaovilai..."
ASSIGNED=$(retry_with_backoff gh search issues is:public --assignee=kaovilai --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000)

echo "Fetching still-open issues commented on by kaovilai (last 90 days)..."
COMMENTED=$(retry_with_backoff gh search issues is:public --commenter=kaovilai --state=open --archived=false \
    --updated=">=$(date -u -d '90 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-90d +%Y-%m-%d)" \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000)

echo "Fetching openshift/openshift-eng issue involvement (full org activity)..."
OPENSHIFT_INVOLVED=$(retry_with_backoff gh search issues is:public --involves=kaovilai --owner=openshift --owner=openshift-eng --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000)

# Merge all four, tagging relation, de-duplicating by repo#number (author > assignee > commenter > involved priority)
MERGED=$(jq -n \
    --argjson authored "$AUTHORED" \
    --argjson assigned "$ASSIGNED" \
    --argjson commented "$COMMENTED" \
    --argjson involved "$OPENSHIFT_INVOLVED" \
    '
    ($authored  | map(. + {relation: "author"})) +
    ($assigned  | map(. + {relation: "assignee"})) +
    ($commented | map(. + {relation: "commenter"})) +
    ($involved  | map(. + {relation: "involved"}))
    | group_by(.repository.nameWithOwner + "#" + (.number|tostring))
    | map(.[0])
    ')

ISSUE_COUNT=$(echo "$MERGED" | jq 'length')
echo "Found $ISSUE_COUNT open issues."

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT
touch "$TMPDIR/issues.jsonl"

echo "$MERGED" | jq -c '.[]' | while IFS= read -r issue; do
    [ -z "$issue" ] && continue

    number=$(echo "$issue" | jq -r '.number')
    title=$(echo "$issue" | jq -r '.title')
    repo=$(echo "$issue" | jq -r '.repository.nameWithOwner')
    org=$(echo "$repo" | cut -d'/' -f1)
    url=$(echo "$issue" | jq -r '.url')
    updated_at=$(echo "$issue" | jq -r '.updatedAt')
    author=$(echo "$issue" | jq -r '.author.login // "unknown"')
    relation=$(echo "$issue" | jq -r '.relation')
    assignees_json=$(echo "$issue" | jq -c '[.assignees[]?.login] // []')
    labels_json=$(echo "$issue" | jq -c '[.labels[].name] // []')
    workstream="$(classify_workstream "$repo")"

    updated_ts=$(date -d "$updated_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$updated_at" +%s)
    if [ "$updated_ts" -lt "$STALE_TS" ]; then
        status="stale"
    else
        status="open"
    fi

    jq -nc \
        --argjson number "$number" \
        --arg repo "$repo" \
        --arg org "$org" \
        --arg title "$title" \
        --arg url "$url" \
        --arg status "$status" \
        --arg author "$author" \
        --arg relation "$relation" \
        --argjson assignees "$assignees_json" \
        --argjson labels "$labels_json" \
        --arg updatedAt "$updated_at" \
        --arg workstream "$workstream" \
        '{number:$number, repo:$repo, org:$org, title:$title, url:$url, status:$status, author:$author, relation:$relation, assignees:$assignees, labels:$labels, updatedAt:$updatedAt, workstream:$workstream}' \
        >> "$TMPDIR/issues.jsonl"
done

jq -s --arg updatedAt "$UPDATED_AT_ISO" \
    'sort_by(.updatedAt) | reverse | {updatedAt: $updatedAt, issues: .}' \
    "$TMPDIR/issues.jsonl" > "$JSON_OUTPUT_FILE"

# Markdown summary, grouped by workstream
{
    echo "# My Open Issues"
    echo ""
    echo "> Last updated: $CURRENT_DATE"
    echo ""
    echo "This file is automatically updated by GitHub Actions."
    echo ""
    jq -r '.issues | group_by(.workstream) | .[] | "## \(.[0].workstream) (\(length))\n" + (map("- [#\(.number) \(.title)](\(.url)) — \(.repo) (\(.relation), \(.status))") | join("\n")) + "\n"' "$JSON_OUTPUT_FILE"
} > "$OUTPUT_FILE"

echo "Issue list updated successfully!"
