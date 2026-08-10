#!/bin/bash
set -euo pipefail

# Shared utilities
# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

# File to update
OUTPUT_FILE="MY_PULL_REQUESTS.md"

# JSON output for structured consumption (e.g. kaovilai.pw)
JSON_OUTPUT_FILE="open-prs.json"

# Get current date
CURRENT_DATE=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
UPDATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)

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

# Function to fetch PRs authored by kaovilai
fetch_prs() {
    gh search prs --author=kaovilai --state=open --archived=false \
        --json number,title,repository,url,isDraft,updatedAt,labels,author,assignees \
        --limit 1000 2>/dev/null || echo "[]"
}

# Function to fetch PRs assigned to kaovilai (catches Copilot-authored PRs)
fetch_assigned_prs() {
    gh search prs --assignee=kaovilai --state=open --archived=false \
        --json number,title,repository,url,isDraft,updatedAt,labels,author,assignees \
        --limit 1000 2>/dev/null || echo "[]"
}

# Copilot bot logins used by GitHub Copilot coding agent
COPILOT_LOGINS=("copilot-swe-agent[bot]" "github-copilot[bot]" "copilot[bot]" "github-advanced-security[bot]")

# Function to get PR details (CI status, base branch, linked issues, review state, merge state)
get_pr_details() {
    local repo="$1"
    local number="$2"
    retry_with_backoff gh pr view "$number" --repo "$repo" \
        --json statusCheckRollup,baseRefName,closingIssuesReferences,reviews,reviewRequests,mergeStateStatus || echo "{}"
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
            milestone=$(retry_with_backoff gh issue view "$issue_num" --repo "$issue_repo" --json milestone --jq '.milestone.title // empty')
            if [ -n "$milestone" ]; then
                echo "$milestone"
                return
            fi
        fi
    done
    echo ""
}

# Fetch PR details and milestone into a temp file (used for parallel execution)
# Args: repo number index tmpdir
fetch_pr_detail_worker() {
    local repo="$1"
    local number="$2"
    local index="$3"
    local tmpdir="$4"

    echo "  [$index] Fetching details for $repo#$number..." >&2
    local pr_details
    pr_details=$(get_pr_details "$repo" "$number")

    local milestone=""
    if [[ "$repo" == *"/velero"* ]]; then
        milestone=$(get_linked_milestone "$repo" "$pr_details")
    fi

    # Write combined result to temp file
    echo "$pr_details" > "$tmpdir/${index}.details"
    echo "$milestone" > "$tmpdir/${index}.milestone"
}

MAX_PARALLEL=10

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
echo "Fetching open PRs authored by kaovilai..."
PRS_JSON=$(fetch_prs)

# Fetch PRs assigned to kaovilai (to catch Copilot-authored PRs)
echo "Fetching open PRs assigned to kaovilai (for Copilot-authored PRs)..."
ASSIGNED_PRS_JSON=$(fetch_assigned_prs)

# Merge: start from authored PRs, then add assigned PRs authored by Copilot bots not already included
# Build set of already-seen "repo#number" keys from authored PRs
SEEN_KEYS=$(echo "$PRS_JSON" | jq -r '.[] | "\(.repository.nameWithOwner)#\(.number)"')

# For assigned PRs: keep only those authored by Copilot bots and not already in authored list
COPILOT_PRS_JSON=$(echo "$ASSIGNED_PRS_JSON" | jq --arg logins "copilot-swe-agent[bot] github-copilot[bot] copilot[bot] github-advanced-security[bot]" '
    [.[] | select(.author.login as $a | ($logins | split(" ") | any(. == $a)))]
')

# Merge into single list; track which are Copilot-authored via a flag
# We'll add isCopilotAuthored field to each PR JSON object
PRS_MERGED=$(jq -n \
    --argjson authored "$PRS_JSON" \
    --argjson copilot "$COPILOT_PRS_JSON" \
    '
    ($authored | map(. + {isCopilotAuthored: false})) +
    ($copilot | map(. + {isCopilotAuthored: true}))
    | group_by(.repository.nameWithOwner + "#" + (.number|tostring))
    | map(.[0])
    ')

# Org order: velero-io first, openshift, migtools, then others
ORG_ORDER=("velero-io" "openshift" "migtools" "oadp-rebase")

# Arrays per org (and catch-all for others)
declare -a VELERO_IO_PRS=()
declare -a OPENSHIFT_PRS=()
declare -a MIGTOOLS_PRS=()
declare -a OADP_REBASE_PRS=()
declare -a OTHER_PRS=()

# Create temp directory for parallel fetch results
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Phase 1: Parse search results and launch parallel detail fetches
PR_COUNT=$(echo "$PRS_MERGED" | jq 'length')
echo "Found $PR_COUNT open PRs. Fetching details (max $MAX_PARALLEL parallel)..."

running=0
index=0
while IFS= read -r pr; do
    if [ -z "$pr" ] || [ "$pr" = "null" ]; then
        continue
    fi

    repo=$(echo "$pr" | jq -r '.repository.nameWithOwner')
    number=$(echo "$pr" | jq -r '.number')

    # Save search data for phase 2
    echo "$pr" > "$TMPDIR/${index}.search"

    # Launch parallel detail fetch
    fetch_pr_detail_worker "$repo" "$number" "$index" "$TMPDIR" &
    running=$((running + 1))

    # Throttle: wait when hitting max parallel limit
    if [ $running -ge $MAX_PARALLEL ]; then
        wait -n 2>/dev/null || wait
        running=$((running - 1))
    fi

    index=$((index + 1))
done < <(echo "$PRS_MERGED" | jq -c '.[]')

# Wait for all remaining background jobs
wait
echo "All detail fetches complete."

# Phase 2: Process results and build badges
# Also track review-queue items for org-owned repos
REVIEW_QUEUE_JSONL="$TMPDIR/review_queue.jsonl"
touch "$REVIEW_QUEUE_JSONL"

# Rebase-blocking labels (hidden from review queue)
REBASE_LABELS=("needs-rebase" "do-not-merge/needs-rebase" "do-not-merge/rebase-needed")

for i in $(seq 0 $((index - 1))); do
    pr=$(cat "$TMPDIR/${i}.search")
    pr_details=$(cat "$TMPDIR/${i}.details" 2>/dev/null || echo "{}")
    milestone=$(cat "$TMPDIR/${i}.milestone" 2>/dev/null || echo "")

    number=$(echo "$pr" | jq -r '.number')
    title=$(echo "$pr" | jq -r '.title')
    repo=$(echo "$pr" | jq -r '.repository.nameWithOwner')
    url=$(echo "$pr" | jq -r '.url')
    is_draft=$(echo "$pr" | jq -r '.isDraft')
    updated_at=$(echo "$pr" | jq -r '.updatedAt')
    author=$(echo "$pr" | jq -r '.author.login // "unknown"')
    is_copilot=$(echo "$pr" | jq -r '.isCopilotAuthored // false')
    assignees_json=$(echo "$pr" | jq -c '[.assignees[]?.login] // []')

    # Extract label names
    label_names=$(echo "$pr" | jq -r '[.labels[].name] | join(",")')
    labels_json=$(echo "$pr" | jq -c '[.labels[].name] // []')
    has_needs_rebase="false"
    has_hold_label="false"
    has_approved="false"
    has_lgtm="false"
    has_do_not_merge="false"

    if echo ",$label_names," | grep -qE ',(needs-rebase|do-not-merge/needs-rebase|do-not-merge/rebase-needed),'; then
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

    status_checks=$(echo "$pr_details" | jq -c '.statusCheckRollup' 2>/dev/null)
    base_branch=$(echo "$pr_details" | jq -r '.baseRefName // "unknown"' 2>/dev/null)
    merge_state=$(echo "$pr_details" | jq -r '.mergeStateStatus // "UNKNOWN"' 2>/dev/null)

    # Determine if repo is org-owned (for review queue filtering)
    # repository.owner.type from search results; if missing, derive from nameWithOwner
    repo_owner_type=$(echo "$pr" | jq -r '.repository.owner.type // "unknown"')
    # If owner type not available in search results, use gh api
    if [ "$repo_owner_type" = "unknown" ] || [ -z "$repo_owner_type" ]; then
        owner_login=$(echo "$repo" | cut -d'/' -f1)
        repo_owner_type=$(gh api "users/$owner_login" --jq '.type' 2>/dev/null || echo "unknown")
    fi
    is_org_repo="false"
    if [ "$repo_owner_type" = "Organization" ]; then
        is_org_repo="true"
    fi

    # Get badge info
    badge_info=$(get_badge_info "$is_draft" "$updated_at" "$status_checks" "$has_needs_rebase" "$has_hold_label" "$has_approved" "$has_lgtm" "$has_do_not_merge")
    color=$(echo "$badge_info" | cut -d'|' -f1)
    status=$(echo "$badge_info" | cut -d'|' -f2)

    # Create badge markdown
    badge=$(create_badge "$repo" "$number" "$title" "$url" "$color" "$status" "$base_branch" "$milestone")

    # Sort priority: PRs needing others' attention first, my own action items last
    # 1=ready, 2=waiting-merge, 3=ci-pending, 4=draft, 5=stale, 6=hold, 7=failing-ci, 8=needs-attention
    sort_key=""
    case "$status" in
        ready)            sort_key=1 ;;
        waiting--merge)   sort_key=2 ;;
        ci--pending)      sort_key=3 ;;
        draft)            sort_key=4 ;;
        stale)            sort_key=5 ;;
        hold)             sort_key=6 ;;
        failing--ci)      sort_key=7 ;;
        needs--attention) sort_key=8 ;;
        *)                sort_key=9 ;;
    esac

    # Prefix badge with sort key (stripped on output)
    sorted_badge="${sort_key}|${badge}"

    # Categorize PR by org
    org=$(echo "$repo" | cut -d'/' -f1)
    case "$org" in
        velero-io)
            VELERO_IO_PRS+=("$sorted_badge")
            org_sort=1
            ;;
        openshift)
            OPENSHIFT_PRS+=("$sorted_badge")
            org_sort=2
            ;;
        migtools)
            MIGTOOLS_PRS+=("$sorted_badge")
            org_sort=3
            ;;
        oadp-rebase)
            OADP_REBASE_PRS+=("$sorted_badge")
            org_sort=4
            ;;
        *)
            OTHER_PRS+=("$sorted_badge")
            org_sort=5
            ;;
    esac

    # Accumulate structured JSON record (status uses single-dash form)
    status_clean="${status//--/-}"
    if [ -n "$milestone" ]; then
        milestone_json=$(jq -n --arg m "$milestone" '$m')
    else
        milestone_json="null"
    fi
    jq -nc \
        --argjson number "$number" \
        --arg repo "$repo" \
        --arg org "$org" \
        --arg title "$title" \
        --arg url "$url" \
        --arg targetBranch "$base_branch" \
        --arg status "$status_clean" \
        --argjson milestone "$milestone_json" \
        --argjson orgSort "$org_sort" \
        --argjson statusSort "$sort_key" \
        --arg author "$author" \
        --argjson isCopilotAuthored "$is_copilot" \
        --argjson assignees "$assignees_json" \
        --argjson isDraft "$is_draft" \
        --argjson labels "$labels_json" \
        --arg updatedAt "$updated_at" \
        '{number:$number, repo:$repo, org:$org, title:$title, url:$url, targetBranch:$targetBranch, status:$status, milestone:$milestone, author:$author, isCopilotAuthored:$isCopilotAuthored, assignees:$assignees, isDraft:$isDraft, labels:$labels, updatedAt:$updatedAt, _orgSort:$orgSort, _statusSort:$statusSort}' \
        >> "$TMPDIR/prs.jsonl"

    # --- Review queue classification (org-owned repos, non-draft, non-rebase-blocked) ---
    if [ "$is_org_repo" = "true" ] && [ "$is_draft" = "false" ] && [ "$has_needs_rebase" = "false" ]; then
        # Compute approval state from GitHub reviews
        has_github_approval="false"
        if echo "$pr_details" | jq -e '.reviews[]? | select(.state == "APPROVED")' > /dev/null 2>&1; then
            has_github_approval="true"
        fi
        # Combine: Prow labels OR native GitHub approval
        is_approved="false"
        if [ "$has_github_approval" = "true" ] || \
           ( [ "$has_approved" = "true" ] && [ "$has_lgtm" = "true" ] ); then
            is_approved="true"
        fi
        # Merge-conflict state hides PR from review queue
        merge_conflict="false"
        if [ "$merge_state" = "DIRTY" ] || [ "$merge_state" = "BEHIND" ]; then
            merge_conflict="true"
        fi

        if [ "$merge_conflict" = "false" ]; then
            # Determine waiting age (seconds since updatedAt, formatted as days)
            updated_ts=$(date -d "$updated_at" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$updated_at" +%s)
            now_ts=$(date -u +%s)
            waiting_seconds=$(( now_ts - updated_ts ))
            waiting_days=$(( waiting_seconds / 86400 ))

            # Determine group and reason
            if [ "$is_approved" = "true" ] && [ "$has_do_not_merge" = "false" ]; then
                rq_group="approvedWaitingToLand"
                if [ "$has_hold_label" = "true" ]; then
                    rq_reason="hold"
                else
                    rq_reason="pendingMerge"
                fi
            else
                rq_group="needsReview"
                if [ "$has_hold_label" = "true" ]; then
                    rq_reason="hold"
                else
                    rq_reason="awaitingReview"
                fi
            fi

            # Build review requests list
            review_requests_json=$(echo "$pr_details" | jq -c '[.reviewRequests[]? | .login // .name // ""] | map(select(. != ""))' 2>/dev/null || echo "[]")

            jq -nc \
                --argjson number "$number" \
                --arg repo "$repo" \
                --arg org "$org" \
                --arg title "$title" \
                --arg url "$url" \
                --arg targetBranch "$base_branch" \
                --arg author "$author" \
                --argjson isCopilotAuthored "$is_copilot" \
                --argjson assignees "$assignees_json" \
                --argjson labels "$labels_json" \
                --arg mergeStateStatus "$merge_state" \
                --argjson isApproved "$is_approved" \
                --argjson hasProwApproval "$([ "$has_approved" = "true" ] && [ "$has_lgtm" = "true" ] && echo true || echo false)" \
                --argjson hasGithubApproval "$has_github_approval" \
                --argjson reviewRequests "$review_requests_json" \
                --arg group "$rq_group" \
                --arg reason "$rq_reason" \
                --argjson waitingDays "$waiting_days" \
                --arg updatedAt "$updated_at" \
                '{number:$number, repo:$repo, org:$org, title:$title, url:$url, targetBranch:$targetBranch, author:$author, isCopilotAuthored:$isCopilotAuthored, assignees:$assignees, labels:$labels, mergeStateStatus:$mergeStateStatus, isApproved:$isApproved, hasProwApproval:$hasProwApproval, hasGithubApproval:$hasGithubApproval, reviewRequests:$reviewRequests, group:$group, reason:$reason, waitingDays:$waitingDays, updatedAt:$updatedAt}' \
                >> "$REVIEW_QUEUE_JSONL"
        fi
    fi
done

# Helper to write a section for an org (sorts by priority prefix, strips it)
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
        # Sort by priority prefix and strip it
        printf '%s\n' "${prs[@]}" | sort -t'|' -k1,1n | while IFS= read -r line; do
            echo "- ${line#*|}"
        done
    fi
}

# Write PRs grouped by org
{
    write_org_section "velero-io" "${VELERO_IO_PRS[@]+"${VELERO_IO_PRS[@]}"}"
    write_org_section "openshift" "${OPENSHIFT_PRS[@]+"${OPENSHIFT_PRS[@]}"}"
    write_org_section "migtools" "${MIGTOOLS_PRS[@]+"${MIGTOOLS_PRS[@]}"}"
    write_org_section "oadp-rebase" "${OADP_REBASE_PRS[@]+"${OADP_REBASE_PRS[@]}"}"

    if [ ${#OTHER_PRS[@]} -gt 0 ]; then
        write_org_section "Other" "${OTHER_PRS[@]}"
    fi

    echo ""
    echo "---"
    echo ""
    echo "**Legend** (sorted by priority — needs review first, my action items last):"
    echo "- 🟢 Green: Ready for review"
    echo "- 🔵 Blue: Waiting to merge (approved + lgtm, pending CI)"
    echo "- 🟡 Yellow: CI Pending / Stale (>60 days) / On Hold"
    echo "- ⚫ Gray: Draft"
    echo "- 🔴 Red: Failing CI (my action item)"
    echo "- 🟠 Orange: Needs rebase (my action item)"

} >> "$OUTPUT_FILE"

# Write structured JSON output (sorted by org priority then status priority)
touch "$TMPDIR/prs.jsonl"
jq -s \
    --arg updatedAt "$UPDATED_AT_ISO" \
    'sort_by(._orgSort, ._statusSort)
     | map(del(._orgSort, ._statusSort))
     | {updatedAt: $updatedAt, prs: .}' \
    "$TMPDIR/prs.jsonl" > "$TMPDIR/prs_base.json"

# Build reviewQueue from review_queue.jsonl
touch "$REVIEW_QUEUE_JSONL"
jq -s \
    --arg updatedAt "$UPDATED_AT_ISO" \
    '{
        updatedAt: $updatedAt,
        needsReview: [.[] | select(.group == "needsReview")] | sort_by(-.waitingDays),
        approvedWaitingToLand: [.[] | select(.group == "approvedWaitingToLand")] | sort_by(-.waitingDays)
    }' \
    "$REVIEW_QUEUE_JSONL" > "$TMPDIR/review_queue.json"

# Merge prs and reviewQueue into final JSON output
jq -n \
    --slurpfile base "$TMPDIR/prs_base.json" \
    --slurpfile rq "$TMPDIR/review_queue.json" \
    '$base[0] + {reviewQueue: $rq[0]}' \
    > "$JSON_OUTPUT_FILE"

echo "PR list updated successfully!"
