#!/bin/bash
set -euo pipefail

# File to update
OUTPUT_FILE="MY_PULL_REQUESTS.md"

# Get current date
CURRENT_DATE=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Calculate stale date (60 days ago)
STALE_DATE=$(date -u -d '60 days ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-60d +%Y-%m-%dT%H:%M:%SZ)

# Start building the markdown file
cat > "$OUTPUT_FILE" << 'EOF'
# My Open Pull Requests

> Last updated: TIMESTAMP

This file is automatically updated every hour by GitHub Actions.

EOF

# Replace TIMESTAMP with actual timestamp
sed -i "s/TIMESTAMP/$CURRENT_DATE/" "$OUTPUT_FILE"

# Function to fetch PRs
fetch_prs() {
    gh search prs --author=kaovilai --state=open --archived=false \
        --json number,title,repository,url,isDraft,updatedAt,labels \
        --limit 1000 2>/dev/null || echo "[]"
}

# Function to get PR details (CI status, base branch, linked issues)
get_pr_details() {
    local repo="$1"
    local number="$2"
    gh pr view "$number" --repo "$repo" \
        --json statusCheckRollup,baseRefName,closingIssuesReferences 2>/dev/null || echo "{}"
}

# Function to get milestone from linked issues (for velero repos)
get_linked_milestone() {
    local repo="$1"
    local pr_details="$2"
    local milestone=""

    # Only check for velero repos
    if [[ "$repo" != *"/velero"* ]]; then
        echo ""
        return
    fi

    # Get linked issue numbers
    local issue_numbers
    issue_numbers=$(echo "$pr_details" | jq -r '.closingIssuesReferences[]?.number // empty' 2>/dev/null)

    for issue_num in $issue_numbers; do
        local issue_repo
        issue_repo=$(echo "$pr_details" | jq -r --argjson num "$issue_num" '.closingIssuesReferences[] | select(.number == $num) | "\(.repository.owner.login)/\(.repository.name)"' 2>/dev/null)
        if [ -n "$issue_repo" ]; then
            milestone=$(gh issue view "$issue_num" --repo "$issue_repo" --json milestone --jq '.milestone.title // empty' 2>/dev/null)
            if [ -n "$milestone" ]; then
                echo "$milestone"
                return
            fi
        fi
    done
    echo ""
}

# Function to determine badge color and status
get_badge_info() {
    local is_draft="$1"
    local updated_at="$2"
    local status_checks="$3"
    local has_needs_rebase="$4"
    local has_hold_label="$5"
    local has_approved="$6"
    local has_lgtm="$7"
    local has_do_not_merge="$8"

    # Check if needs attention (needs-rebase = merge conflicts)
    if [ "$has_needs_rebase" = "true" ]; then
        echo "orange|needs--attention"
        return
    fi

    # Check if stale (no activity in 60 days)
    local updated_timestamp=$(date -d "$updated_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$updated_at" +%s)
    local stale_timestamp=$(date -d "$STALE_DATE" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$STALE_DATE" +%s)

    if [ "$updated_timestamp" -lt "$stale_timestamp" ]; then
        echo "yellow|stale"
        return
    fi

    # Check for hold label
    if [ "$has_hold_label" = "true" ]; then
        echo "yellow|hold"
        return
    fi

    # Check if draft
    if [ "$is_draft" = "true" ]; then
        echo "gray|draft"
        return
    fi

    # Check if waiting to merge (approved + lgtm, no do-not-merge blockers)
    if [ "$has_approved" = "true" ] && [ "$has_lgtm" = "true" ] && [ "$has_do_not_merge" = "false" ]; then
        echo "blue|waiting--merge"
        return
    fi

    # Check CI status
    if [ "$status_checks" = "null" ] || [ -z "$status_checks" ] || [ "$status_checks" = "[]" ]; then
        echo "green|ready"
        return
    fi

    # Parse status checks - look for any failed conclusions
    if echo "$status_checks" | grep -q '"conclusion":"FAILURE"'; then
        echo "red|failing--ci"
        return
    elif echo "$status_checks" | grep -q '"conclusion":"ERROR"'; then
        echo "red|failing--ci"
        return
    elif echo "$status_checks" | grep -q '"status":"IN_PROGRESS"'; then
        echo "yellow|ci--pending"
        return
    elif echo "$status_checks" | grep -q '"status":"QUEUED"'; then
        echo "yellow|ci--pending"
        return
    fi

    # Default to ready for review
    echo "green|ready"
}

# Function to create badge markdown
create_badge() {
    local repo="$1"
    local number="$2"
    local title="$3"
    local url="$4"
    local color="$5"
    local status="$6"
    local base_branch="$7"
    local milestone="$8"

    # Create badge using shields.io
    local line="[![PR #$number](https://img.shields.io/badge/PR%20%23$number-$status-$color)]($url) **$repo** → \`$base_branch\` - $title"

    # Add milestone if available
    if [ -n "$milestone" ]; then
        line="$line (milestone: **$milestone**)"
    fi

    echo "$line"
}

# Fetch all open PRs authored by the user
echo "Fetching open PRs..."
PRS_JSON=$(fetch_prs)

# Org order: vmware-tanzu first, openshift, migtools, then others
ORG_ORDER=("vmware-tanzu" "openshift" "migtools" "oadp-rebase")

# Arrays per org (and catch-all for others)
declare -a VMWARE_TANZU_PRS=()
declare -a OPENSHIFT_PRS=()
declare -a MIGTOOLS_PRS=()
declare -a OADP_REBASE_PRS=()
declare -a OTHER_PRS=()

# Process each PR
while IFS= read -r pr; do
    if [ -z "$pr" ] || [ "$pr" = "null" ]; then
        continue
    fi

    number=$(echo "$pr" | jq -r '.number')
    title=$(echo "$pr" | jq -r '.title')
    repo=$(echo "$pr" | jq -r '.repository.nameWithOwner')
    url=$(echo "$pr" | jq -r '.url')
    is_draft=$(echo "$pr" | jq -r '.isDraft')
    updated_at=$(echo "$pr" | jq -r '.updatedAt')

    # Extract label names
    label_names=$(echo "$pr" | jq -r '[.labels[].name] | join(",")')
    has_needs_rebase="false"
    has_hold_label="false"
    has_approved="false"
    has_lgtm="false"
    has_do_not_merge="false"

    if echo ",$label_names," | grep -q ',needs-rebase,'; then
        has_needs_rebase="true"
    fi
    if echo ",$label_names," | grep -q ',do-not-merge/hold,'; then
        has_hold_label="true"
    fi
    if echo ",$label_names," | grep -q ',approved,'; then
        has_approved="true"
    fi
    if echo ",$label_names," | grep -q ',lgtm,'; then
        has_lgtm="true"
    fi
    if echo ",$label_names," | grep -q ',do-not-merge/'; then
        has_do_not_merge="true"
    fi

    # Fetch PR details (CI status, base branch, linked issues)
    echo "  Fetching details for $repo#$number..."
    pr_details=$(get_pr_details "$repo" "$number")
    status_checks=$(echo "$pr_details" | jq -c '.statusCheckRollup' 2>/dev/null)
    base_branch=$(echo "$pr_details" | jq -r '.baseRefName // "unknown"' 2>/dev/null)

    # Get milestone from linked issues (velero repos only)
    milestone=$(get_linked_milestone "$repo" "$pr_details")

    # Get badge info
    badge_info=$(get_badge_info "$is_draft" "$updated_at" "$status_checks" "$has_needs_rebase" "$has_hold_label" "$has_approved" "$has_lgtm" "$has_do_not_merge")
    color=$(echo "$badge_info" | cut -d'|' -f1)
    status=$(echo "$badge_info" | cut -d'|' -f2)

    # Create badge markdown
    badge=$(create_badge "$repo" "$number" "$title" "$url" "$color" "$status" "$base_branch" "$milestone")

    # Categorize PR by org
    org=$(echo "$repo" | cut -d'/' -f1)
    case "$org" in
        vmware-tanzu)
            VMWARE_TANZU_PRS+=("$badge")
            ;;
        openshift)
            OPENSHIFT_PRS+=("$badge")
            ;;
        migtools)
            MIGTOOLS_PRS+=("$badge")
            ;;
        oadp-rebase)
            OADP_REBASE_PRS+=("$badge")
            ;;
        *)
            OTHER_PRS+=("$badge")
            ;;
    esac

done < <(echo "$PRS_JSON" | jq -c '.[]')

# Helper to write a section for an org
write_org_section() {
    local org_name="$1"
    shift
    local prs=("$@")

    echo ""
    echo "## $org_name"
    echo ""
    if [ ${#prs[@]} -eq 0 ]; then
        echo "No open PRs."
    else
        for pr in "${prs[@]}"; do
            echo "- $pr"
        done
    fi
}

# Write PRs grouped by org
{
    write_org_section "vmware-tanzu" "${VMWARE_TANZU_PRS[@]+"${VMWARE_TANZU_PRS[@]}"}"
    write_org_section "openshift" "${OPENSHIFT_PRS[@]+"${OPENSHIFT_PRS[@]}"}"
    write_org_section "migtools" "${MIGTOOLS_PRS[@]+"${MIGTOOLS_PRS[@]}"}"
    write_org_section "oadp-rebase" "${OADP_REBASE_PRS[@]+"${OADP_REBASE_PRS[@]}"}"

    if [ ${#OTHER_PRS[@]} -gt 0 ]; then
        write_org_section "Other" "${OTHER_PRS[@]}"
    fi

    echo ""
    echo "---"
    echo ""
    echo "**Legend:**"
    echo "- 🟠 Orange: Needs attention (rebase required, merge conflicts)"
    echo "- 🔵 Blue: Waiting to merge (approved + lgtm, pending CI)"
    echo "- 🟢 Green: Ready for review"
    echo "- 🟡 Yellow: Stale (>60 days) or On Hold or CI Pending"
    echo "- ⚫ Gray: Draft"
    echo "- 🔴 Red: Failing CI"

} >> "$OUTPUT_FILE"

echo "PR list updated successfully!"
