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

# Function to fetch PRs and check CI status
fetch_prs() {
    local query="$1"

    gh search prs "$query" \
        --json number,title,repository,url,isDraft,updatedAt,statusCheckRollup \
        --limit 1000 2>/dev/null || echo "[]"
}

# Function to determine badge color and status
get_badge_info() {
    local is_draft="$1"
    local updated_at="$2"
    local status_checks="$3"
    local has_hold_label="$4"

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

    # Check CI status
    if [ "$status_checks" = "null" ] || [ -z "$status_checks" ]; then
        echo "green|ready"
        return
    fi

    # Parse status checks - look for any failed states
    if echo "$status_checks" | grep -q '"state":"FAILURE"'; then
        echo "red|failing-ci"
        return
    elif echo "$status_checks" | grep -q '"state":"ERROR"'; then
        echo "red|failing-ci"
        return
    elif echo "$status_checks" | grep -q '"state":"PENDING"'; then
        echo "yellow|ci-pending"
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

    # Sanitize title for URL encoding
    local encoded_title=$(echo "$title" | sed 's/ /%20/g' | sed 's/#/%23/g')

    # Create badge using shields.io
    echo "[![PR #$number](https://img.shields.io/badge/PR%20%23$number-$status-$color)]($url) **$repo** - $title"
}

# Fetch all open PRs authored by the user
echo "Fetching open PRs..."

# Search for all PRs across different organizations
PRS_JSON=$(fetch_prs "is:open is:pr author:kaovilai archived:false")

# Create associative arrays to categorize PRs
declare -a READY_PRS=()
declare -a DRAFT_PRS=()
declare -a FAILING_PRS=()
declare -a STALE_PRS=()
declare -a HOLD_PRS=()
declare -a PENDING_PRS=()

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
    status_checks=$(echo "$pr" | jq -c '.statusCheckRollup')

    # Check for hold labels (would require additional API call per PR)
    # For now, we'll skip this and rely on draft/CI/stale status
    has_hold_label="false"

    # Get badge info
    badge_info=$(get_badge_info "$is_draft" "$updated_at" "$status_checks" "$has_hold_label")
    color=$(echo "$badge_info" | cut -d'|' -f1)
    status=$(echo "$badge_info" | cut -d'|' -f2)

    # Create badge markdown
    badge=$(create_badge "$repo" "$number" "$title" "$url" "$color" "$status")

    # Categorize PR
    case "$status" in
        ready)
            READY_PRS+=("$badge")
            ;;
        draft)
            DRAFT_PRS+=("$badge")
            ;;
        failing-ci)
            FAILING_PRS+=("$badge")
            ;;
        stale)
            STALE_PRS+=("$badge")
            ;;
        hold)
            HOLD_PRS+=("$badge")
            ;;
        ci-pending)
            PENDING_PRS+=("$badge")
            ;;
    esac

done < <(echo "$PRS_JSON" | jq -c '.[]')

# Write categorized PRs to file
{
    echo ""
    echo "## 🟢 Ready for Review"
    echo ""
    if [ ${#READY_PRS[@]} -eq 0 ]; then
        echo "No PRs ready for review."
    else
        for pr in "${READY_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "## 🟡 CI Pending"
    echo ""
    if [ ${#PENDING_PRS[@]} -eq 0 ]; then
        echo "No PRs with pending CI."
    else
        for pr in "${PENDING_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "## ⚫ Draft PRs"
    echo ""
    if [ ${#DRAFT_PRS[@]} -eq 0 ]; then
        echo "No draft PRs."
    else
        for pr in "${DRAFT_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "## 🔴 Failing CI"
    echo ""
    if [ ${#FAILING_PRS[@]} -eq 0 ]; then
        echo "No PRs with failing CI."
    else
        for pr in "${FAILING_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "## 🟡 Stale PRs (No activity >60 days)"
    echo ""
    if [ ${#STALE_PRS[@]} -eq 0 ]; then
        echo "No stale PRs."
    else
        for pr in "${STALE_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "## 🟡 On Hold"
    echo ""
    if [ ${#HOLD_PRS[@]} -eq 0 ]; then
        echo "No PRs on hold."
    else
        for pr in "${HOLD_PRS[@]}"; do
            echo "- $pr"
        done
    fi

    echo ""
    echo "---"
    echo ""
    echo "**Legend:**"
    echo "- 🟢 Green: Ready for review"
    echo "- 🟡 Yellow: Stale (>60 days) or On Hold or CI Pending"
    echo "- ⚫ Gray: Draft"
    echo "- 🔴 Red: Failing CI"

} >> "$OUTPUT_FILE"

echo "PR list updated successfully!"
