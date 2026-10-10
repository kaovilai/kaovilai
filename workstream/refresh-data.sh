#!/bin/bash
# Pull fresh data on demand, between scheduled Actions runs.
set -euo pipefail
cd "$(dirname "$0")/.."
bash .github/scripts/update-pr-list.sh
bash .github/scripts/update-issues-list.sh
bash .github/scripts/update-activity-log.sh
if [ -f workstream-archive.json ]; then
    bash .github/scripts/update-history-archive.sh
else
    echo "workstream-archive.json not found — run .github/scripts/backfill-history.sh once first."
fi
