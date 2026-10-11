#!/bin/bash
# Maintain repo-languages.json: {"owner/repo": "Go" | null}, the primary language of
# every public repo outside the personal namespace that I've merged a PR into.
# Cached by design: only repos missing from the file are queried, so scheduled runs
# cost ~0 API calls once seeded. Feeds the language chart in generate-profile-svgs.py.
set -euo pipefail

ARCHIVE="workstream-archive.json"
OUT="repo-languages.json"
OWNER="kaovilai"

[ -f "$ARCHIVE" ] || { echo "ERROR: $ARCHIVE not found" >&2; exit 1; }
[ -f "$OUT" ] || echo '{}' > "$OUT"

MISSING=$(jq -r --arg owner "$OWNER" --slurpfile known "$OUT" '
    [.items[] | select(.type == "pr" and .state == "merged" and .org != $owner) | .repo]
    | unique | .[] as $r | select($known[0] | has($r) | not) | $r' "$ARCHIVE")

if [ -z "$MISSING" ]; then
    echo "repo-languages.json already covers every repo"
    exit 0
fi

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
echo "$MISSING" | while read -r repo; do
    # Deleted/private/renamed repos resolve to null rather than failing the run.
    lang=$(gh api "repos/$repo" --jq '.language // ""' 2>/dev/null || true)
    jq -n --arg repo "$repo" --arg lang "$lang" '{($repo): (if $lang == "" then null else $lang end)}'
done | jq -s 'add // {}' > "$TMP"

jq -S -s '.[0] + .[1]' "$OUT" "$TMP" > "$OUT.new" && mv "$OUT.new" "$OUT"
echo "repo-languages.json now has $(jq 'length' "$OUT") repos"
