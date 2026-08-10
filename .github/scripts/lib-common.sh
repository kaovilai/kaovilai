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
