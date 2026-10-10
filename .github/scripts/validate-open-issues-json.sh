#!/bin/bash
# Validates that open-issues.json has the expected schema.
# Usage: bash .github/scripts/validate-open-issues-json.sh [path/to/open-issues.json]
set -euo pipefail

JSON_FILE="${1:-open-issues.json}"

if [ ! -f "$JSON_FILE" ]; then
    echo "ERROR: $JSON_FILE not found" >&2
    exit 1
fi

echo "Validating $JSON_FILE..."

jq -e '.updatedAt | type == "string"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing updatedAt string"; exit 1; }
jq -e '.issues | type == "array"' "$JSON_FILE" > /dev/null || { echo "ERROR: missing issues array"; exit 1; }

ISSUE_COUNT=$(jq '.issues | length' "$JSON_FILE")
echo "Checking $ISSUE_COUNT issues in .issues[]..."
for field in number repo org title url status author relation assignees labels updatedAt workstream; do
    BAD=$(jq --arg f "$field" '[.issues[] | select(has($f) | not) | .url] | length' "$JSON_FILE")
    if [ "$BAD" -gt 0 ]; then
        echo "ERROR: $BAD issues missing field '$field'" >&2
        exit 1
    fi
done

echo "Validation passed."
