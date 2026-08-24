#!/bin/bash
# Generates workstream-issues.json and workstream-prs.json: ALL of kaovilai's
# public open issues/PRs across every repo/org, classified into workstream
# categories (Velero, OADP, KubeVirt Data Mover, Kubernetes, CNCF Landscape,
# Uncategorized). Feeds the general workstream dashboard, separate from the
# unrelated open-prs.json/activity.json pipeline.
set -euo pipefail

# Shared utilities
# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

ISSUES_OUTPUT_FILE="workstream-issues.json"
PRS_OUTPUT_FILE="workstream-prs.json"

UPDATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
STALE_CUTOFF=$(date -u -d '60 days ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-60d +%Y-%m-%dT%H:%M:%SZ)

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Classifies a repo (owner/name) into one of the fixed workstream categories.
# Keep in sync with WORKSTREAM_NODE_ORDER in workstream/app.js.
classify_workstream() {
    local repo="$1"
    case "$repo" in
        velero-io/*) echo "Velero" ;;
        openshift/oadp-operator) echo "OADP" ;;
        migtools/*[Oo][Aa][Dd][Pp]*) echo "OADP" ;;
        kubevirt/*) echo "KubeVirt Data Mover" ;;
        migtools/*datamover*|migtools/*data-mover*|migtools/*[Dd]ata[Mm]over*) echo "KubeVirt Data Mover" ;;
        */velero-plugin-for-*) echo "Velero" ;;
        openshift/openshift-velero-plugin) echo "Velero" ;;
        cncf/*) echo "CNCF Landscape" ;;
        kubernetes/*) echo "Kubernetes" ;;
        kubernetes-sigs/*) echo "Kubernetes" ;;
        *) echo "Uncategorized" ;;
    esac
}

echo "Fetching recognized milestones from velero-io/velero..."
RECOGNIZED_MILESTONES=$(gh api repos/velero-io/velero/milestones --paginate --jq \
    '[.[] | select(.state=="open") | .title]' 2>/dev/null || echo "[]")
RECOGNIZED_MILESTONES=$(jq -c '
    map(select(test("^v?[0-9]+\\.[0-9]+")))
    | map({orig: ., parts: (sub("^v"; "") | split(".") | map(tonumber? // 0))})
    | sort_by(.parts) | reverse
    | .[0:2] | map(.orig)
' <<< "$RECOGNIZED_MILESTONES")
echo "Recognized milestones: $RECOGNIZED_MILESTONES"

### Issues ###

echo "Fetching all public issues assigned to kaovilai..."
ISSUES_RAW=$(gh search issues is:public --assignee=kaovilai --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000 2>/dev/null || echo "[]")
ISSUES_MERGED=$(jq -c '[.[] | {
    number, repo: .repository.nameWithOwner, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login]
}] | unique_by(.repo + "#" + (.number | tostring))' <<< "$ISSUES_RAW")
ISSUE_COUNT=$(jq 'length' <<< "$ISSUES_MERGED")
echo "Found $ISSUE_COUNT open issues assigned to kaovilai."

: > "$TMPDIR/issues.jsonl"
while IFS= read -r issue; do
    [ -z "$issue" ] && continue
    repo=$(jq -r '.repo' <<< "$issue")
    number=$(jq -r '.number' <<< "$issue")
    workstream=$(classify_workstream "$repo")
    echo "  Enriching issue $repo#$number ($workstream)..." >&2
    milestone=$(retry_with_backoff gh issue view "$number" --repo "$repo" --json milestone --jq '.milestone.title // empty')

    jq -n --argjson issue "$issue" --arg milestone "$milestone" --arg staleCutoff "$STALE_CUTOFF" --arg workstream "$workstream" '
        ($issue.updatedAt) as $u
        | {
            number: $issue.number,
            repo: $issue.repo,
            org: ($issue.repo | split("/")[0]),
            workstream: $workstream,
            title: $issue.title,
            url: $issue.url,
            status: (if $u < $staleCutoff then "stale" else "open" end),
            author: $issue.author,
            assignees: $issue.assignees,
            labels: $issue.labels,
            updatedAt: $u,
            milestone: (if $milestone == "" then null else $milestone end)
        }
    ' >> "$TMPDIR/issues.jsonl"
done < <(jq -c '.[]' <<< "$ISSUES_MERGED")

jq -s --arg updatedAt "$UPDATED_AT_ISO" --argjson recognizedMilestones "$RECOGNIZED_MILESTONES" \
    '{updatedAt: $updatedAt, recognizedMilestones: $recognizedMilestones, issues: .}' \
    "$TMPDIR/issues.jsonl" > "$ISSUES_OUTPUT_FILE"

### PRs ###

echo "Fetching all public PRs authored by kaovilai..."
PRS_RAW=$(gh search prs is:public --author=kaovilai --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees,isDraft --limit 1000 2>/dev/null || echo "[]")
PRS_MERGED=$(jq -c '[.[] | select(.author.login == "kaovilai") | {
    number, repo: .repository.nameWithOwner, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login], isDraft
}] | unique_by(.repo + "#" + (.number | tostring))' <<< "$PRS_RAW")
PR_COUNT=$(jq 'length' <<< "$PRS_MERGED")
echo "Found $PR_COUNT open PRs authored by kaovilai."

: > "$TMPDIR/prs.jsonl"
while IFS= read -r pr; do
    [ -z "$pr" ] && continue
    repo=$(jq -r '.repo' <<< "$pr")
    number=$(jq -r '.number' <<< "$pr")
    workstream=$(classify_workstream "$repo")
    echo "  Enriching PR $repo#$number ($workstream)..." >&2
    details=$(retry_with_backoff gh pr view "$number" --repo "$repo" \
        --json milestone,statusCheckRollup,mergeStateStatus,baseRefName,closingIssuesReferences)
    if ! jq -e 'type == "object"' <<< "$details" > /dev/null 2>&1; then
        details='{}'
    fi

    owner="${repo%%/*}"
    name="${repo##*/}"
    blocker=$(retry_with_backoff gh api graphql -f query='
        query($owner:String!, $name:String!, $number:Int!) {
          repository(owner:$owner, name:$name) {
            pullRequest(number:$number) {
              mergeable
              reviewDecision
              reviewThreads(first: 50) { nodes { isResolved } }
            }
          }
        }' -F owner="$owner" -F name="$name" -F number="$number" \
        --jq '.data.repository.pullRequest')
    if ! jq -e 'type == "object"' <<< "$blocker" > /dev/null 2>&1; then
        blocker='{}'
    fi

    jq -n --argjson pr "$pr" --argjson details "$details" --argjson blocker "$blocker" --arg staleCutoff "$STALE_CUTOFF" --arg workstream "$workstream" '
        ($details.milestone.title // null) as $milestone
        | ($details.baseRefName // "unknown") as $targetBranch
        | ($pr.updatedAt) as $u
        | ([$details.closingIssuesReferences[]? | {
                number: .number,
                repo: (.repository.nameWithOwner // (.url | capture("github.com/(?<o>[^/]+)/(?<r>[^/]+)/issues") | "\(.o)/\(.r)")),
                url: .url
            }]) as $closing
        | ([$details.statusCheckRollup[]? | {
                name: (.name // .context // ""),
                conclusion: (.conclusion // .state // "")
            } | select(.name | test("tide|auto request review"; "i") | not)]) as $ci
        | ($blocker.reviewThreads.nodes // []) as $threads
        | (
            if $pr.isDraft then "draft"
            elif ($pr.labels | index("do-not-merge/hold")) then "hold"
            elif ([$ci[] | select(.conclusion | IN("FAILURE", "ERROR", "TIMED_OUT", "CANCELLED"))] | length > 0)
                then "failing-ci"
            elif ($details.mergeStateStatus == "BEHIND") or ($u < $staleCutoff)
                then "stale"
            elif ($details.mergeStateStatus | IN("CLEAN", "HAS_HOOKS", "UNSTABLE"))
                then "ready"
            elif ($blocker.mergeable == "CONFLICTING")
                then "conflicts"
            elif ([$ci[] | select(.conclusion == "" or .conclusion == null)] | length > 0)
                then "missing-checks"
            elif ($blocker.reviewDecision | IN("REVIEW_REQUIRED", "CHANGES_REQUESTED"))
                then "missing-reviews"
            elif ([$threads[] | select(.isResolved == false)] | length > 0)
                then "unresolved-conversations"
            else "blocked"
            end
        ) as $status
        | {
            number: $pr.number,
            repo: $pr.repo,
            org: ($pr.repo | split("/")[0]),
            workstream: $workstream,
            title: $pr.title,
            url: $pr.url,
            targetBranch: $targetBranch,
            status: $status,
            milestone: $milestone,
            author: $pr.author,
            assignees: $pr.assignees,
            isDraft: $pr.isDraft,
            labels: $pr.labels,
            updatedAt: $u,
            ciChecks: $ci,
            closingIssuesReferences: $closing
        }
    ' >> "$TMPDIR/prs.jsonl"
done < <(jq -c '.[]' <<< "$PRS_MERGED")

jq -s --arg updatedAt "$UPDATED_AT_ISO" --argjson recognizedMilestones "$RECOGNIZED_MILESTONES" \
    '{updatedAt: $updatedAt, recognizedMilestones: $recognizedMilestones, prs: .}' \
    "$TMPDIR/prs.jsonl" > "$PRS_OUTPUT_FILE"

echo "Workstream data updated successfully!"
echo "  $ISSUES_OUTPUT_FILE: $ISSUE_COUNT issues"
echo "  $PRS_OUTPUT_FILE: $PR_COUNT PRs"
