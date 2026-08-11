#!/bin/bash
# Validates that open-prs.json has the expected schema including reviewQueue groups.
# Usage: bash .github/scripts/validate-open-prs-json.sh [path/to/open-prs.json]
set -euo pipefail

JSON_FILE="${1:-open-prs.json}"

if [ ! -f "$JSON_FILE" ]; then
    echo "ERROR: $JSON_FILE not found" >&2
    exit 1
fi

echo "Validating $JSON_FILE..."

# Top-level fields
jq -e '.updatedAt | type == "string"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing updatedAt string"; exit 1; }
jq -e '.prs | type == "array"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing prs array"; exit 1; }
jq -e '.reviewQueue | type == "object"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing reviewQueue object"; exit 1; }
jq -e '.reviewQueue.needsReview | type == "array"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing reviewQueue.needsReview array"; exit 1; }
jq -e '.reviewQueue.approvedWaitingToLand | type == "array"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing reviewQueue.approvedWaitingToLand array"; exit 1; }

# Each PR in the prs array has required fields
PR_COUNT=$(jq '.prs | length' "$JSON_FILE")
echo "Checking $PR_COUNT PRs in .prs[]..."
for field in number repo org title url targetBranch status author isDraft labels updatedAt; do
    BAD=$(jq --arg f "$field" '[.prs[] | select(has($f) | not) | .url] | length' "$JSON_FILE")
    if [ "$BAD" -gt 0 ]; then
        echo "ERROR: $BAD PRs missing field '$field'" >&2
        exit 1
    fi
done

# Each reviewQueue item has required fields
for group in needsReview approvedWaitingToLand; do
    COUNT=$(jq --arg g "$group" '.reviewQueue[$g] | length' "$JSON_FILE")
    echo "Checking $COUNT items in reviewQueue.$group..."
    for field in number repo org title url author group reason waitingDays updatedAt isApproved labels; do
        BAD=$(jq --arg g "$group" --arg f "$field" '[.reviewQueue[$g][] | select(has($f) | not) | .url] | length' "$JSON_FILE")
        if [ "$BAD" -gt 0 ]; then
            echo "ERROR: $BAD items in reviewQueue.$group missing field '$field'" >&2
            exit 1
        fi
    done
done

# Optional review-decision fields must have the right type when present
BAD=$(jq '[.reviewQueue.needsReview[], .reviewQueue.approvedWaitingToLand[]
           | select(has("reviewDecision") and (.reviewDecision != null) and ((.reviewDecision | type) != "string"))
           | .url] | length' "$JSON_FILE")
if [ "$BAD" -gt 0 ]; then
    echo "ERROR: $BAD reviewQueue items have a non-string reviewDecision" >&2
    exit 1
fi
for field in approvalCount requiredApprovals; do
    BAD=$(jq --arg f "$field" '[.reviewQueue.needsReview[], .reviewQueue.approvedWaitingToLand[]
               | select(has($f) and (.[$f] != null) and ((.[$f] | type) != "number"))
               | .url] | length' "$JSON_FILE")
    if [ "$BAD" -gt 0 ]; then
        echo "ERROR: $BAD reviewQueue items have a non-numeric $field" >&2
        exit 1
    fi
done

# All reviewQueue items must be from org-owned repos (no kaovilai/* personal repos)
PERSONAL=$(jq '[.reviewQueue.needsReview[], .reviewQueue.approvedWaitingToLand[] | select(.org == "kaovilai")] | length' "$JSON_FILE")
if [ "$PERSONAL" -gt 0 ]; then
    echo "ERROR: $PERSONAL personal kaovilai/* repos found in reviewQueue" >&2
    exit 1
fi

# No drafts in review queue
DRAFTS=$(jq '[.reviewQueue.needsReview[], .reviewQueue.approvedWaitingToLand[] | select(.isDraft == true)] | length' "$JSON_FILE")
if [ "$DRAFTS" -gt 0 ]; then
    echo "ERROR: $DRAFTS draft PRs found in reviewQueue" >&2
    exit 1
fi

echo "Validation passed."
