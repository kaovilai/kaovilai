#!/bin/bash
set -euo pipefail

OUTPUT_FILE="MY_ACTIVITY.md"

CURRENT_DATE=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
TWO_WEEKS_AGO=$(date -u -d '14 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-14d +%Y-%m-%d)

# Retry wrapper with exponential backoff
retry_with_backoff() {
    local max_retries=3
    local delay=2
    local attempt=0
    local output=""

    while [ $attempt -lt $max_retries ]; do
        if output=$("$@" 2>/dev/null); then
            echo "$output"
            return 0
        fi
        attempt=$((attempt + 1))
        if [ $attempt -lt $max_retries ]; then
            echo "  Retry $attempt/$max_retries after ${delay}s..." >&2
            sleep $delay
            delay=$((delay * 2))
        fi
    done
    echo "[]"
    return 1
}

# Org grouping helper: takes JSON array, groups by org, outputs markdown
group_by_org() {
    local json="$1"
    local orgs=("vmware-tanzu" "openshift" "migtools" "oadp-rebase")
    local count
    count=$(echo "$json" | jq 'length')

    if [ "$count" -eq 0 ]; then
        echo "No activity."
        echo ""
        return
    fi

    for org in "${orgs[@]}"; do
        local org_items
        org_items=$(echo "$json" | jq -c --arg org "$org" '[.[] | select(.repository.nameWithOwner | startswith($org + "/"))]')
        local org_count
        org_count=$(echo "$org_items" | jq 'length')

        if [ "$org_count" -gt 0 ]; then
            echo "**$org** ($org_count)"
            echo "$org_items" | jq -r '.[] | "- [#\(.number) \(.title)](\(.url)) — \(.repository.nameWithOwner)"'
            echo ""
        fi
    done

    # Others
    local other_items
    other_items=$(echo "$json" | jq -c '[.[] | select(.repository.nameWithOwner | (startswith("vmware-tanzu/") or startswith("openshift/") or startswith("migtools/") or startswith("oadp-rebase/")) | not)]')
    local other_count
    other_count=$(echo "$other_items" | jq 'length')

    if [ "$other_count" -gt 0 ]; then
        echo "**Other** ($other_count)"
        echo "$other_items" | jq -r '.[] | "- [#\(.number) \(.title)](\(.url)) — \(.repository.nameWithOwner)"'
        echo ""
    fi
}

echo "Generating activity log for $TWO_WEEKS_AGO to $CURRENT_DATE..."

# Fetch all data
echo "Fetching merged PRs..."
MERGED_PRS=$(retry_with_backoff gh search prs --author=kaovilai --merged --merged-at=">=$TWO_WEEKS_AGO" \
    --json number,title,repository,url --sort=updated --limit 100)

echo "Fetching opened PRs..."
OPENED_PRS=$(retry_with_backoff gh search prs --author=kaovilai --created=">=$TWO_WEEKS_AGO" \
    --json number,title,repository,url,isDraft,state --sort=created --limit 100)

echo "Fetching PRs reviewed..."
REVIEWED_PRS=$(retry_with_backoff gh search prs --reviewed-by=kaovilai --sort=updated --created=">=$TWO_WEEKS_AGO" \
    --json number,title,repository,url,author --limit 100)
# Exclude own PRs from reviews
REVIEWED_PRS=$(echo "$REVIEWED_PRS" | jq -c '[.[] | select(.author.login != "kaovilai")]')

echo "Fetching PRs/issues commented on..."
COMMENTED=$(retry_with_backoff gh search issues --commenter=kaovilai --updated=">=$TWO_WEEKS_AGO" \
    --json number,title,repository,url --sort=updated --limit 100)
# Exclude own issues/PRs
COMMENTED=$(echo "$COMMENTED" | jq -c '[.[] | select(true)]')

echo "Fetching issues closed..."
CLOSED_ISSUES=$(retry_with_backoff gh search issues --author=kaovilai --state=closed --closed=">=$TWO_WEEKS_AGO" \
    --json number,title,repository,url --sort=updated --limit 100)

# Count totals
MERGED_COUNT=$(echo "$MERGED_PRS" | jq 'length')
OPENED_COUNT=$(echo "$OPENED_PRS" | jq 'length')
REVIEWED_COUNT=$(echo "$REVIEWED_PRS" | jq 'length')
COMMENTED_COUNT=$(echo "$COMMENTED" | jq 'length')
CLOSED_COUNT=$(echo "$CLOSED_ISSUES" | jq 'length')

# Generate report
cat > "$OUTPUT_FILE" << EOF
# Activity Log

> **Period:** $TWO_WEEKS_AGO — $(date -u +%Y-%m-%d)
> **Generated:** $CURRENT_DATE

| Metric | Count |
|--------|-------|
| PRs Merged | $MERGED_COUNT |
| PRs Opened | $OPENED_COUNT |
| PRs Reviewed | $REVIEWED_COUNT |
| Issues/PRs Commented | $COMMENTED_COUNT |
| Issues Closed | $CLOSED_COUNT |

---

## PRs Merged ($MERGED_COUNT)

$(group_by_org "$MERGED_PRS")
## PRs Opened ($OPENED_COUNT)

$(group_by_org "$OPENED_PRS")
## PRs Reviewed ($REVIEWED_COUNT)

$(group_by_org "$REVIEWED_PRS")
## Issues/PRs Commented On ($COMMENTED_COUNT)

$(group_by_org "$COMMENTED")
## Issues Closed ($CLOSED_COUNT)

$(group_by_org "$CLOSED_ISSUES")
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
EOF

echo "Activity log generated successfully!"
