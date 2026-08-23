#!/bin/bash
# Generates velero-open-issues.json and velero-open-prs.json: kaovilai's open
# issues/PRs restricted to the Velero family of repos (velero-io/* plus
# openshift/openshift-velero-plugin). Feeds a Velero-only dashboard, separate
# from the general cross-project open-prs.json/open-issues.json.
set -euo pipefail

# Shared utilities
# shellcheck source=lib-common.sh
source "$(dirname "$0")/lib-common.sh"

ISSUES_OUTPUT_FILE="velero-open-issues.json"
PRS_OUTPUT_FILE="velero-open-prs.json"

OSVP_REPO="openshift/openshift-velero-plugin"

UPDATED_AT_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)
STALE_CUTOFF=$(date -u -d '60 days ago' +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-60d +%Y-%m-%dT%H:%M:%SZ)

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

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

echo "Fetching issues assigned to kaovilai (owner:velero-io)..."
VELERO_IO_ISSUES=$(gh search issues is:public --assignee=kaovilai --owner=velero-io --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees --limit 1000 2>/dev/null || echo "[]")
VELERO_IO_ISSUES_NORM=$(jq -c '[.[] | {
    number, repo: .repository.nameWithOwner, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login]
}]' <<< "$VELERO_IO_ISSUES")

echo "Fetching issues assigned to kaovilai ($OSVP_REPO)..."
OSVP_ISSUES=$(gh issue list --repo "$OSVP_REPO" --assignee=kaovilai --state=open \
    --json number,title,url,updatedAt,labels,author,assignees --limit 1000 2>/dev/null || echo "[]")
OSVP_ISSUES_NORM=$(jq -c --arg repo "$OSVP_REPO" '[.[] | {
    number, repo: $repo, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login]
}]' <<< "$OSVP_ISSUES")

ISSUES_MERGED=$(jq -c -n --argjson a "$VELERO_IO_ISSUES_NORM" --argjson b "$OSVP_ISSUES_NORM" \
    '($a + $b) | unique_by(.repo + "#" + (.number | tostring))')
ISSUE_COUNT=$(jq 'length' <<< "$ISSUES_MERGED")
echo "Found $ISSUE_COUNT open issues assigned to kaovilai in Velero family repos."

: > "$TMPDIR/issues.jsonl"
while IFS= read -r issue; do
    [ -z "$issue" ] && continue
    repo=$(jq -r '.repo' <<< "$issue")
    number=$(jq -r '.number' <<< "$issue")
    echo "  Enriching issue $repo#$number..." >&2
    milestone=$(retry_with_backoff gh issue view "$number" --repo "$repo" --json milestone --jq '.milestone.title // empty')

    jq -n --argjson issue "$issue" --arg milestone "$milestone" --arg staleCutoff "$STALE_CUTOFF" '
        ($issue.updatedAt) as $u
        | {
            number: $issue.number,
            repo: $issue.repo,
            org: ($issue.repo | split("/")[0]),
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

echo "Fetching PRs authored by kaovilai (owner:velero-io)..."
VELERO_IO_PRS=$(gh search prs is:public --author=kaovilai --owner=velero-io --state=open --archived=false \
    --json number,title,repository,url,updatedAt,labels,author,assignees,isDraft --limit 1000 2>/dev/null || echo "[]")
VELERO_IO_PRS_NORM=$(jq -c '[.[] | select(.author.login == "kaovilai") | {
    number, repo: .repository.nameWithOwner, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login], isDraft
}]' <<< "$VELERO_IO_PRS")

echo "Fetching PRs authored by kaovilai ($OSVP_REPO)..."
OSVP_PRS=$(gh pr list --repo "$OSVP_REPO" --author=kaovilai --state=open \
    --json number,title,url,updatedAt,labels,author,assignees,isDraft --limit 1000 2>/dev/null || echo "[]")
OSVP_PRS_NORM=$(jq -c --arg repo "$OSVP_REPO" '[.[] | select(.author.login == "kaovilai") | {
    number, repo: $repo, title, url, updatedAt,
    labels: [.labels[].name], author: .author.login,
    assignees: [.assignees[].login], isDraft
}]' <<< "$OSVP_PRS")

PRS_MERGED=$(jq -c -n --argjson a "$VELERO_IO_PRS_NORM" --argjson b "$OSVP_PRS_NORM" \
    '($a + $b) | unique_by(.repo + "#" + (.number | tostring))')
PR_COUNT=$(jq 'length' <<< "$PRS_MERGED")
echo "Found $PR_COUNT open PRs authored by kaovilai in Velero family repos."

: > "$TMPDIR/prs.jsonl"
while IFS= read -r pr; do
    [ -z "$pr" ] && continue
    repo=$(jq -r '.repo' <<< "$pr")
    number=$(jq -r '.number' <<< "$pr")
    echo "  Enriching PR $repo#$number..." >&2
    details=$(retry_with_backoff gh pr view "$number" --repo "$repo" \
        --json milestone,statusCheckRollup,mergeStateStatus,baseRefName,closingIssuesReferences)
    if ! jq -e 'type == "object"' <<< "$details" > /dev/null 2>&1; then
        details='{}'
    fi

    jq -n --argjson pr "$pr" --argjson details "$details" --arg staleCutoff "$STALE_CUTOFF" '
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
        | (
            if $pr.isDraft then "draft"
            elif ($pr.labels | index("do-not-merge/hold")) then "hold"
            elif ([$ci[] | select(.conclusion | IN("FAILURE", "ERROR", "TIMED_OUT", "CANCELLED"))] | length > 0)
                then "failing-ci"
            elif ($details.mergeStateStatus == "BEHIND") or ($u < $staleCutoff)
                then "stale"
            elif ($details.mergeStateStatus | IN("CLEAN", "HAS_HOOKS", "UNSTABLE"))
                then "ready"
            else "waiting-merge"
            end
        ) as $status
        | {
            number: $pr.number,
            repo: $pr.repo,
            org: ($pr.repo | split("/")[0]),
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

echo "Velero workstream data updated successfully!"
echo "  $ISSUES_OUTPUT_FILE: $ISSUE_COUNT issues"
echo "  $PRS_OUTPUT_FILE: $PR_COUNT PRs"
