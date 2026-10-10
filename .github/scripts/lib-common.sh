#!/bin/bash
# Shared utilities for GitHub Actions scripts.
# Source this file: source "$(dirname "$0")/lib-common.sh"

# Retry wrapper with exponential backoff.
# Usage: retry_with_backoff <command> [args...]
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

# Classify a repo (org/repo) into a workstream lane for the /workstream/ dashboard.
# Used as the "default" classification source — overridable per-repo/per-item in
# workstream-classification.json (source: "manual"/"auto" always wins over this).
# Usage: classify_workstream "velero-io/velero"
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

# CI check names to hide from the workstream dashboard's CI summary (case-insensitive
# substring match) — merge-queue/bot noise, not real test signal. Velero uses Tide;
# other repos generally don't have contexts matching these, so this is safe globally.
CI_CHECK_IGNORE_REGEX="tide|auto request review"

# Normalize a PR's `statusCheckRollup` (from `gh pr view --json statusCheckRollup`)
# into a compact [{name, conclusion}] array for open-prs.json, filtering out
# $CI_CHECK_IGNORE_REGEX. Handles both CheckRun (name/conclusion/status) and
# legacy StatusContext (context/state) shapes.
# Usage: ci_checks_json "$pr_details_json"
ci_checks_json() {
    local pr_details="$1"
    echo "$pr_details" | jq -c --arg ignore "$CI_CHECK_IGNORE_REGEX" '
        [ (.statusCheckRollup // [])[]
          | {name: (.name // .context // "unknown"), conclusion: (.conclusion // .state // .status // "PENDING")}
          | select((.name | ascii_downcase | test($ignore)) | not)
        ]
    ' 2>/dev/null || echo "[]"
}

# jq equivalent of classify_workstream(), for scripts that shape records with jq
# rather than one-at-a-time in bash. Splice into a jq program string, e.g.:
#   jq "$WORKSTREAM_JQ_DEF"' map(. + {workstream: classify_workstream(.repo)})'
read -r -d '' WORKSTREAM_JQ_DEF <<'JQEOF' || true
def classify_workstream(repo):
  if (repo | test("^velero-io/")) then "Velero"
  elif (repo == "openshift/oadp-operator") then "OADP"
  elif (repo | test("^migtools/.*oadp"; "i")) then "OADP"
  elif (repo | test("^kubevirt/")) then "KubeVirt Data Mover"
  elif (repo | test("^migtools/.*(datamover|data-mover)"; "i")) then "KubeVirt Data Mover"
  elif (repo | test("velero-plugin-for-")) then "Velero"
  elif (repo == "openshift/openshift-velero-plugin") then "Velero"
  elif (repo | test("^cncf/")) then "CNCF Landscape"
  elif (repo | test("^kubernetes/")) then "Kubernetes"
  elif (repo | test("^kubernetes-sigs/")) then "Kubernetes"
  else "Uncategorized"
  end;
JQEOF
