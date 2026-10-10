---
on:
  schedule: daily
  workflow_dispatch:
engine: copilot
permissions:
  contents: read
  issues: read
  pull-requests: read
tools:
  edit:
  bash: ["jq", "cat", "ls", "grep"]
  github:
    toolsets: [repos, issues, pull_requests]
network:
  allowed:
    - defaults
    - github
safe-outputs:
  create-pull-request:
    max: 1
    title-prefix: "[workstream] "
    labels: [automation, workstream-classification]
    reviewers: [kaovilai]
    protected-files: { policy: fallback-to-issue, exclude: [README.md, workstream-layout.json] }
---

# Workstream Classifier

You classify newly-discovered PRs/issues on the `kaovilai/kaovilai` `/workstream/` dashboard into a
workstream lane, for anything the default regex rules couldn't place.

## Data

- `open-prs.json`, `open-issues.json` — live items, each already has a `workstream` field set by a
  fast default-regex rule (in `.github/scripts/lib-common.sh`'s `classify_workstream`). Items that
  didn't match any rule are set to `"Uncategorized"`.
- `workstream-archive.json` — historical closed/merged items, same `workstream` convention.
- `workstream-classification.json` — the override file, keyed by `org/repo` or `org/repo#123`:
  ```json
  { "org/repo#123": { "workstream": "...", "source": "manual"|"auto"|"default", "note": "..." } }
  ```

## Your job

1. Read `workstream-classification.json`. Build the set of existing lane names already in use
   (from both this file and the `workstream` values already appearing in the data files) —
   these are `Velero` (includes its plugin repos), `OADP`, `KubeVirt Data Mover`, `Kubernetes`, `CNCF Landscape`, plus
   any `source: manual`/`auto` custom lane a human or a prior run has already introduced.
2. Find every item (in `open-prs.json`, `open-issues.json`, `workstream-archive.json`) where
   `workstream == "Uncategorized"` AND either:
   - there is no entry for it (by `org/repo#number`, falling back to `org/repo`) in
     `workstream-classification.json`, OR
   - there is an entry but its `source` is `"auto"` and it's still sitting in Uncategorized.
3. For each such item, look at its title, labels, and repo (fetch more detail via the `github`
   tools only if genuinely ambiguous) and propose the best-fitting workstream: prefer an existing
   lane; only propose a brand-new lane name if the item is genuinely unrelated to all existing
   ones (e.g. a wholly different technology area).
4. Write your proposals into `workstream-classification.json` as entries with `"source": "auto"`.
   Keep the file valid JSON, keyed consistently, alphabetically sorted by key for a clean diff.

## Hard rule — never touch manual overrides

**Never add, edit, or remove any entry whose current `"source"` is `"manual"`.** Those are
explicit human decisions and are permanent. If you're unsure whether your proposed change would
touch one, skip that item entirely rather than risk it.

## Pre-flight

Before doing anything, check for an existing open PR labeled `workstream-classification`. If one
exists, stop — do not open a second one. Post a comment on it noting there's new Uncategorized
volume instead, only if the count has grown meaningfully since that PR was opened.

## Output

A single pull request (`safe-outputs.create-pull-request`) with the updated
`workstream-classification.json`, or nothing if there is nothing new to classify or a PR is
already open and awaiting review.
