# Activity Log

> **Period:** 2026-07-26 — 2026-10-24
> **Generated:** 2026-10-24 15:47:19 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 100 |
| PRs Opened | 100 |
| PRs Reviewed | 70 |
| Issues/PRs Commented | 100 |
| Issues Closed | 89 |

---

## PRs Merged (100)

**velero-io** (12)
- [#10683 docs: point README OpenSSF Best Practices badge at bestpractices.dev](https://github.com/velero-io/velero/pull/10683) — velero-io/velero
- [#10051 docs: use consistent excludedNames glob pattern in filter design examples](https://github.com/velero-io/velero/pull/10051) — velero-io/velero
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero
- [#10077 Add Dependabot auto-approve workflow](https://github.com/velero-io/velero/pull/10077) — velero-io/velero
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero
- [#9646 Fix backup-finalizer: do not set backup phase to Completed before PutBackupMetadata succeeds](https://github.com/velero-io/velero/pull/9646) — velero-io/velero
- [#10275 Implement namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10275) — velero-io/velero
- [#9221 docs: Document --write-sparse-files flag for disk space issues during restore](https://github.com/velero-io/velero/pull/9221) — velero-io/velero
- [#9772 Design: namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/9772) — velero-io/velero
- [#10027 Add set-based label selector test and docs coverage for restore](https://github.com/velero-io/velero/pull/10027) — velero-io/velero
- [#9575 Add configurable tolerations for PodVolumeBackup and data mover pods](https://github.com/velero-io/velero/pull/9575) — velero-io/velero
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero

**openshift** (34)
- [#87638 Trust OADP automation apps for presubmit triggering](https://github.com/openshift/release/pull/87638) — openshift/release
- [#600 OADP-8895: Reject restores from backups not in a completed or partially failed phase (#9792)](https://github.com/openshift/velero/pull/600) — openshift/velero
- [#130 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/130) — openshift/velero-plugin-for-legacy-aws
- [#489 OADP-8924: Treat missing openshift-apiserver config as no internal registry](https://github.com/openshift/openshift-velero-plugin/pull/489) — openshift/openshift-velero-plugin
- [#190 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-gcp/pull/190) — openshift/velero-plugin-for-gcp
- [#76 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/76) — openshift/restic
- [#77 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/77) — openshift/restic
- [#75 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/75) — openshift/restic
- [#74 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/74) — openshift/restic
- [#190 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/190) — openshift/velero-plugin-for-microsoft-azure
- [#189 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-gcp/pull/189) — openshift/velero-plugin-for-gcp
- [#188 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-gcp/pull/188) — openshift/velero-plugin-for-gcp
- [#189 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/189) — openshift/velero-plugin-for-microsoft-azure
- [#131 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/131) — openshift/velero-plugin-for-legacy-aws
- [#128 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/128) — openshift/velero-plugin-for-legacy-aws
- [#186 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-aws/pull/186) — openshift/velero-plugin-for-aws
- [#129 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/129) — openshift/velero-plugin-for-legacy-aws
- [#188 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/188) — openshift/velero-plugin-for-microsoft-azure
- [#187 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-aws/pull/187) — openshift/velero-plugin-for-aws
- [#184 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-aws/pull/184) — openshift/velero-plugin-for-aws
- [#187 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/187) — openshift/velero-plugin-for-microsoft-azure
- [#567 oadp-1.5: Pin Bitnami MinIO e2e build and cherry-pick velero-io/velero#10001 (skip upstream-only workflows on forks)](https://github.com/openshift/velero/pull/567) — openshift/velero
- [#185 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-aws/pull/185) — openshift/velero-plugin-for-aws
- [#2479 fix(e2e): wait for DPA-owned secret GC in Undeploy](https://github.com/openshift/oadp-operator/pull/2479) — openshift/oadp-operator
- [#86664 Add release-4.21 to Prow configuration branches](https://github.com/openshift/release/pull/86664) — openshift/release
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator
- [#2453 OADP-6065: auto-detect AWS region for CloudStorage-backed BSLs](https://github.com/openshift/oadp-operator/pull/2453) — openshift/oadp-operator
- [#2452 OADP-7984: fix(nodeagent): propagate PodConfig.PriorityClassName to node-agent ConfigMap](https://github.com/openshift/oadp-operator/pull/2452) — openshift/oadp-operator
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release
- [#449 Detect SCC UID/GID-range mismatch on namespace restore](https://github.com/openshift/openshift-velero-plugin/pull/449) — openshift/openshift-velero-plugin
- [#2446 [oadp-1.5] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts (cherry-pick #2234)](https://github.com/openshift/oadp-operator/pull/2446) — openshift/oadp-operator
- [#2445 fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2445) — openshift/oadp-operator
- [#2234 OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2234) — openshift/oadp-operator

**migtools** (10)
- [#192 Fix CI coverage handling for no-test packages and update setup-go](https://github.com/migtools/udistribution/pull/192) — migtools/udistribution
- [#49 ci: use go.mod Go version in CI workflow (oadp-1.6)](https://github.com/migtools/filebrowser/pull/49) — migtools/filebrowser
- [#120 [oadp-1.6] ci: build e2e MinIO image from pinned Bitnami Dockerfile](https://github.com/migtools/oadp-vm-file-restore/pull/120) — migtools/oadp-vm-file-restore
- [#44 UPSTREAM: <carry>: Bump Go to 1.26 and fix Lint workflow failures on oadp-dev](https://github.com/migtools/oadp-vmdp/pull/44) — migtools/oadp-vmdp
- [#63 chore(ci): disable upstream-only license-check and code-coverage workflows](https://github.com/migtools/kopia/pull/63) — migtools/kopia
- [#396 [oadp-1.5] ci: build golangci-lint with repo Go toolchain via make lint](https://github.com/migtools/oadp-non-admin/pull/396) — migtools/oadp-non-admin
- [#121 ci: build e2e MinIO image from pinned Bitnami Dockerfile](https://github.com/migtools/oadp-vm-file-restore/pull/121) — migtools/oadp-vm-file-restore
- [#62 ci: disable failing Quay binaries push workflow](https://github.com/migtools/kopia/pull/62) — migtools/kopia
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore

**Other** (44)
- [#1571 Add support for Chipsea-BLE GATT body fat scales](https://github.com/oliexdev/openScale/pull/1571) — oliexdev/openScale
- [#198 docs: Android update via Tasker; stable-name release zip (v1.1.2)](https://github.com/kaovilai/github-bot-command-palette/pull/198) — kaovilai/github-bot-command-palette
- [#197 fix(content): give the review-dialog command bar its own row](https://github.com/kaovilai/github-bot-command-palette/pull/197) — kaovilai/github-bot-command-palette
- [#196 feat: in-extension update check and automated GitHub releases](https://github.com/kaovilai/github-bot-command-palette/pull/196) — kaovilai/github-bot-command-palette
- [#195 fix(settings): shard config across sync keys to stay under 8 KB item quota](https://github.com/kaovilai/github-bot-command-palette/pull/195) — kaovilai/github-bot-command-palette
- [#15 Merge upstream/dev (268 commits) into dev](https://github.com/kaovilai/copilot-api/pull/15) — kaovilai/copilot-api
- [#91 docs(welcome): add hosted-model-only recipes for Claude Code and Codex](https://github.com/redhat-et/pricetag-metering/pull/91) — redhat-et/pricetag-metering
- [#5 Fix PR commit detection from deferred GitHub diff markup](https://github.com/kaovilai/github-html-diff-preview/pull/5) — kaovilai/github-html-diff-preview
- [#192 chore: prepare Chrome Web Store submission](https://github.com/kaovilai/github-bot-command-palette/pull/192) — kaovilai/github-bot-command-palette
- [#80 Group every repo under an org node in the orbit chart](https://github.com/kaovilai/kaovilai/pull/80) — kaovilai/kaovilai
- [#72 fix: parse @-prefixed and filters-nested OWNERS entries](https://github.com/dpanshug/upstream-pulse/pull/72) — dpanshug/upstream-pulse
- [#266 ci: fix gh aw compile failure by dropping web-fetch from docs-harmonize](https://github.com/kaovilai/cephcsi-cbt-e2e/pull/266) — kaovilai/cephcsi-cbt-e2e
- [#267 feat(desktop): throw the pet like a ball on drag release](https://github.com/OpenPetsHQ/openpets/pull/267) — OpenPetsHQ/openpets
- [#264 Ignore transparent sprite pixels in pet hit testing](https://github.com/OpenPetsHQ/openpets/pull/264) — OpenPetsHQ/openpets
- [#135 fix: switch MinIO image to cgr.dev/chainguard/minio:latest](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/135) — kaovilai/k8s-cbt-s3mover-demo
- [#65 [improve] ci: add concurrency groups to prevent stale demo workflow overlap](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/65) — kaovilai/k8s-cbt-s3mover-demo
- [#134 chore: update to latest upstream releases and refresh slides](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/134) — kaovilai/k8s-cbt-s3mover-demo
- [#261 Update to latest ecosystem: deps, lint v2, scripts, docs](https://github.com/kaovilai/cephcsi-cbt-e2e/pull/261) — kaovilai/cephcsi-cbt-e2e
- [#17611 fix(mobile): new thread draft names its repo and says it is a new thread](https://github.com/pingdotgg/t3code/pull/17611) — pingdotgg/t3code
- [#79 Enhance career map with animated route and accessible details](https://github.com/kaovilai/kaovilai/pull/79) — kaovilai/kaovilai
- [#78 Add Bojangles and animated backyard adventures](https://github.com/kaovilai/kaovilai/pull/78) — kaovilai/kaovilai
- [#77 Animated, linked OSS account pills in the README](https://github.com/kaovilai/kaovilai/pull/77) — kaovilai/kaovilai
- [#76 Group Other-lane repos under org nodes in the orbit chart](https://github.com/kaovilai/kaovilai/pull/76) — kaovilai/kaovilai
- [#75 Lock down the workstream local save server](https://github.com/kaovilai/kaovilai/pull/75) — kaovilai/kaovilai
- [#74 Replace github-stats images with animated language chart; animate live data](https://github.com/kaovilai/kaovilai/pull/74) — kaovilai/kaovilai
- [#73 Refresh profile README with animated SVGs generated from repo data](https://github.com/kaovilai/kaovilai/pull/73) — kaovilai/kaovilai
- [#252 Speak question speech for Claude AskUserQuestion permission requests](https://github.com/OpenPetsHQ/openpets/pull/252) — OpenPetsHQ/openpets
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#188 Fix review queue card deadspace](https://github.com/kaovilai/kaovilai.pw/pull/188) — kaovilai/kaovilai.pw
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
- [#1 Bring vendor/amazon/maverick blobs in sync with the lineage-20 device tree manifest](https://github.com/kaovilai/android_vendor_amazon_maverick/pull/1) — kaovilai/android_vendor_amazon_maverick
- [#7 Add safe Dependabot auto-merge workflow for npm patch/minor updates](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/7) — kaovilai/bandwidth-hero-proxy2
- [#14 Fix healthcheck: use 127.0.0.1 instead of localhost](https://github.com/kaovilai/copilot-api/pull/14) — kaovilai/copilot-api
- [#13 Lower ambiguous-timeout budget to 80s to beat client watchdogs](https://github.com/kaovilai/copilot-api/pull/13) — kaovilai/copilot-api
- [#182 Fall back to top-level build-log.txt for steps that die before writing artifacts](https://github.com/kaovilai/github-bot-command-palette/pull/182) — kaovilai/github-bot-command-palette
- [#176 Add per-command cancel-x to pending combo buttons](https://github.com/kaovilai/github-bot-command-palette/pull/176) — kaovilai/github-bot-command-palette
- [#6 Fix Netlify build failure: bump Node version and sync yarn.lock](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/6) — kaovilai/bandwidth-hero-proxy2
- [#3 Harden CRX recorder/transport reconnect lifecycle with bounded recovery and stale-session renewal](https://github.com/kaovilai/playwright-crx/pull/3) — kaovilai/playwright-crx
- [#1 Keep recorder sessions alive across UI reconnects and stop Resume/Step from replaying paused actions](https://github.com/kaovilai/playwright-crx/pull/1) — kaovilai/playwright-crx
- [#12 Address CodeRabbit findings on the streaming chat-completions handler](https://github.com/kaovilai/copilot-api/pull/12) — kaovilai/copilot-api
- [#11 Handle client abort gracefully in streaming chat-completions](https://github.com/kaovilai/copilot-api/pull/11) — kaovilai/copilot-api
## PRs Opened (100)

**velero-io** (8)
- [#10696 design: fix the order of the snapshot retention cases in block data mover](https://github.com/velero-io/velero/pull/10696) — velero-io/velero
- [#10695 ci: add CodeQL analysis for Go](https://github.com/velero-io/velero/pull/10695) — velero-io/velero
- [#10692 Add Dependabot updates for run-jammy-tiny on supported release branches](https://github.com/velero-io/velero/pull/10692) — velero-io/velero
- [#10691 Delete retained volume snapshots on backup deletion for data movement](https://github.com/velero-io/velero/pull/10691) — velero-io/velero
- [#10690 [release-1.18] Bump paketobuildpacks/run-jammy-tiny to 0.2.190](https://github.com/velero-io/velero/pull/10690) — velero-io/velero
- [#10689 Group Go security updates in Dependabot](https://github.com/velero-io/velero/pull/10689) — velero-io/velero
- [#10683 docs: point README OpenSSF Best Practices badge at bestpractices.dev](https://github.com/velero-io/velero/pull/10683) — velero-io/velero
- [#5 Draft Velero security self-assessment and SECURITY.md response roles for CNCF incubation](https://github.com/velero-io/.github/pull/5) — velero-io/.github

**openshift** (29)
- [#504 NO-JIRA: Group Go security updates in Dependabot](https://github.com/openshift/openshift-velero-plugin/pull/504) — openshift/openshift-velero-plugin
- [#327 NO-JIRA: Group Go security updates in Dependabot](https://github.com/openshift/hypershift-oadp-plugin/pull/327) — openshift/hypershift-oadp-plugin
- [#87638 Trust OADP automation apps for presubmit triggering](https://github.com/openshift/release/pull/87638) — openshift/release
- [#2515 fix: retry AWS bucket region discovery on transient S3 errors](https://github.com/openshift/oadp-operator/pull/2515) — openshift/oadp-operator
- [#600 OADP-8895: Reject restores from backups not in a completed or partially failed phase (#9792)](https://github.com/openshift/velero/pull/600) — openshift/velero
- [#2508 Sync NonAdmin CRDs with oadp-non-admin oadp-dev](https://github.com/openshift/oadp-operator/pull/2508) — openshift/oadp-operator
- [#77 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/77) — openshift/restic
- [#76 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/76) — openshift/restic
- [#75 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/75) — openshift/restic
- [#74 ci: disable upstream tests workflow](https://github.com/openshift/restic/pull/74) — openshift/restic
- [#190 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-gcp/pull/190) — openshift/velero-plugin-for-gcp
- [#189 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-gcp/pull/189) — openshift/velero-plugin-for-gcp
- [#188 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-gcp/pull/188) — openshift/velero-plugin-for-gcp
- [#190 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/190) — openshift/velero-plugin-for-microsoft-azure
- [#189 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/189) — openshift/velero-plugin-for-microsoft-azure
- [#188 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/188) — openshift/velero-plugin-for-microsoft-azure
- [#187 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/187) — openshift/velero-plugin-for-microsoft-azure
- [#131 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/131) — openshift/velero-plugin-for-legacy-aws
- [#130 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/130) — openshift/velero-plugin-for-legacy-aws
- [#129 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/129) — openshift/velero-plugin-for-legacy-aws
- [#128 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/128) — openshift/velero-plugin-for-legacy-aws
- [#187 Skip Auto Request Review workflow outside upstream (oadp-dev)](https://github.com/openshift/velero-plugin-for-aws/pull/187) — openshift/velero-plugin-for-aws
- [#186 Skip Auto Request Review workflow outside upstream (oadp-1.6)](https://github.com/openshift/velero-plugin-for-aws/pull/186) — openshift/velero-plugin-for-aws
- [#185 Skip Auto Request Review workflow outside upstream (oadp-1.5)](https://github.com/openshift/velero-plugin-for-aws/pull/185) — openshift/velero-plugin-for-aws
- [#184 Skip Auto Request Review workflow outside upstream (oadp-1.4)](https://github.com/openshift/velero-plugin-for-aws/pull/184) — openshift/velero-plugin-for-aws
- [#2499 fix(e2e): don't dereference nil BSL LastValidationTime in BSLsAreUpdated](https://github.com/openshift/oadp-operator/pull/2499) — openshift/oadp-operator
- [#489 OADP-8924: Treat missing openshift-apiserver config as no internal registry](https://github.com/openshift/openshift-velero-plugin/pull/489) — openshift/openshift-velero-plugin
- [#2482 fix(kubevirt-datamover): size controller for scale, make resources configurable](https://github.com/openshift/oadp-operator/pull/2482) — openshift/oadp-operator
- [#2479 fix(e2e): wait for DPA-owned secret GC in Undeploy](https://github.com/openshift/oadp-operator/pull/2479) — openshift/oadp-operator

**migtools** (16)
- [#287 Group Go security updates in Dependabot](https://github.com/migtools/oadp-cli/pull/287) — migtools/oadp-cli
- [#250 Group Go security updates in Dependabot](https://github.com/migtools/kubevirt-datamover-controller/pull/250) — migtools/kubevirt-datamover-controller
- [#197 Group Go security updates in Dependabot](https://github.com/migtools/udistribution/pull/197) — migtools/udistribution
- [#109 Add akarol to OWNERS_ALIASES](https://github.com/migtools/kubevirt-velero-plugin/pull/109) — migtools/kubevirt-velero-plugin
- [#108 Sync OWNERS_ALIASES with main](https://github.com/migtools/kubevirt-velero-plugin/pull/108) — migtools/kubevirt-velero-plugin
- [#107 Sync OWNERS_ALIASES with main](https://github.com/migtools/kubevirt-velero-plugin/pull/107) — migtools/kubevirt-velero-plugin
- [#106 Sync OWNERS_ALIASES with main](https://github.com/migtools/kubevirt-velero-plugin/pull/106) — migtools/kubevirt-velero-plugin
- [#397 Fix pre-existing CI failures on oadp-dev](https://github.com/migtools/oadp-non-admin/pull/397) — migtools/oadp-non-admin
- [#44 UPSTREAM: <carry>: Bump Go to 1.26 and fix Lint workflow failures on oadp-dev](https://github.com/migtools/oadp-vmdp/pull/44) — migtools/oadp-vmdp
- [#63 chore(ci): disable upstream-only license-check and code-coverage workflows](https://github.com/migtools/kopia/pull/63) — migtools/kopia
- [#62 ci: disable failing Quay binaries push workflow](https://github.com/migtools/kopia/pull/62) — migtools/kopia
- [#49 ci: use go.mod Go version in CI workflow (oadp-1.6)](https://github.com/migtools/filebrowser/pull/49) — migtools/filebrowser
- [#121 ci: build e2e MinIO image from pinned Bitnami Dockerfile](https://github.com/migtools/oadp-vm-file-restore/pull/121) — migtools/oadp-vm-file-restore
- [#120 [oadp-1.6] ci: build e2e MinIO image from pinned Bitnami Dockerfile](https://github.com/migtools/oadp-vm-file-restore/pull/120) — migtools/oadp-vm-file-restore
- [#396 [oadp-1.5] ci: build golangci-lint with repo Go toolchain via make lint](https://github.com/migtools/oadp-non-admin/pull/396) — migtools/oadp-non-admin
- [#245 fix: stop gate hot loop, avoid priority-queue starvation, scope cache (part of #244)](https://github.com/migtools/kubevirt-datamover-controller/pull/245) — migtools/kubevirt-datamover-controller

**Other** (47)
- [#115 docs(welcome): document EnMaaS request body limit](https://github.com/redhat-et/pricetag-metering/pull/115) — redhat-et/pricetag-metering
- [#453 feat: log per-request latency and time to first token](https://github.com/caozhiyuan/copilot-api/pull/453) — caozhiyuan/copilot-api
- [#198 docs: Android update via Tasker; stable-name release zip (v1.1.2)](https://github.com/kaovilai/github-bot-command-palette/pull/198) — kaovilai/github-bot-command-palette
- [#197 fix(content): give the review-dialog command bar its own row](https://github.com/kaovilai/github-bot-command-palette/pull/197) — kaovilai/github-bot-command-palette
- [#196 feat: in-extension update check and automated GitHub releases](https://github.com/kaovilai/github-bot-command-palette/pull/196) — kaovilai/github-bot-command-palette
- [#452 feat: publish in-flight generation requests to an optional directory](https://github.com/caozhiyuan/copilot-api/pull/452) — caozhiyuan/copilot-api
- [#195 fix(settings): shard config across sync keys to stay under 8 KB item quota](https://github.com/kaovilai/github-bot-command-palette/pull/195) — kaovilai/github-bot-command-palette
- [#15 Merge upstream/dev (268 commits) into dev](https://github.com/kaovilai/copilot-api/pull/15) — kaovilai/copilot-api
- [#1571 Add support for Chipsea-BLE GATT body fat scales](https://github.com/oliexdev/openScale/pull/1571) — oliexdev/openScale
- [#5 Fix PR commit detection from deferred GitHub diff markup](https://github.com/kaovilai/github-html-diff-preview/pull/5) — kaovilai/github-html-diff-preview
- [#192 chore: prepare Chrome Web Store submission](https://github.com/kaovilai/github-bot-command-palette/pull/192) — kaovilai/github-bot-command-palette
- [#47 Preview HTML files in pull request diffs (green additions, clickable red removals, side by side)](https://github.com/dohyeon5626/github-html-preview-extension/pull/47) — dohyeon5626/github-html-preview-extension
- [#19792 feat(claude): add a fork subagents switch to Claude instances](https://github.com/pingdotgg/t3code/pull/19792) — pingdotgg/t3code
- [#19785 fix(web): a message queued behind a running turn no longer pushes the working header below it](https://github.com/pingdotgg/t3code/pull/19785) — pingdotgg/t3code
- [#91 docs(welcome): add hosted-model-only recipes for Claude Code and Codex](https://github.com/redhat-et/pricetag-metering/pull/91) — redhat-et/pricetag-metering
- [#80 Group every repo under an org node in the orbit chart](https://github.com/kaovilai/kaovilai/pull/80) — kaovilai/kaovilai
- [#72 fix: parse @-prefixed and filters-nested OWNERS entries](https://github.com/dpanshug/upstream-pulse/pull/72) — dpanshug/upstream-pulse
- [#266 ci: fix gh aw compile failure by dropping web-fetch from docs-harmonize](https://github.com/kaovilai/cephcsi-cbt-e2e/pull/266) — kaovilai/cephcsi-cbt-e2e
- [#267 feat(desktop): throw the pet like a ball on drag release](https://github.com/OpenPetsHQ/openpets/pull/267) — OpenPetsHQ/openpets
- [#18765 feat(web): sidebar search finds a thread by its ID](https://github.com/pingdotgg/t3code/pull/18765) — pingdotgg/t3code
- [#18712 fix(web): a thread waiting on another thread shows Waiting, not Working](https://github.com/pingdotgg/t3code/pull/18712) — pingdotgg/t3code
- [#1750 feat(upstream-pulse): seed OADP upstream repositories](https://github.com/red-hat-data-services/rhai-org-pulse/pull/1750) — red-hat-data-services/rhai-org-pulse
- [#135 fix: switch MinIO image to cgr.dev/chainguard/minio:latest](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/135) — kaovilai/k8s-cbt-s3mover-demo
- [#264 Ignore transparent sprite pixels in pet hit testing](https://github.com/OpenPetsHQ/openpets/pull/264) — OpenPetsHQ/openpets
- [#261 Update to latest ecosystem: deps, lint v2, scripts, docs](https://github.com/kaovilai/cephcsi-cbt-e2e/pull/261) — kaovilai/cephcsi-cbt-e2e
- [#134 chore: update to latest upstream releases and refresh slides](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/134) — kaovilai/k8s-cbt-s3mover-demo
- [#18096 fix(server): show Antigravity's real sign-in failure reason](https://github.com/pingdotgg/t3code/pull/18096) — pingdotgg/t3code
- [#79 Enhance career map with animated route and accessible details](https://github.com/kaovilai/kaovilai/pull/79) — kaovilai/kaovilai
- [#78 Add Bojangles and animated backyard adventures](https://github.com/kaovilai/kaovilai/pull/78) — kaovilai/kaovilai
- [#77 Animated, linked OSS account pills in the README](https://github.com/kaovilai/kaovilai/pull/77) — kaovilai/kaovilai
- [#76 Group Other-lane repos under org nodes in the orbit chart](https://github.com/kaovilai/kaovilai/pull/76) — kaovilai/kaovilai
- [#75 Lock down the workstream local save server](https://github.com/kaovilai/kaovilai/pull/75) — kaovilai/kaovilai
- [#74 Replace github-stats images with animated language chart; animate live data](https://github.com/kaovilai/kaovilai/pull/74) — kaovilai/kaovilai
- [#73 Refresh profile README with animated SVGs generated from repo data](https://github.com/kaovilai/kaovilai/pull/73) — kaovilai/kaovilai
- [#129 jira-solve-agent: add OADP to tracked Jira projects](https://github.com/RedHatInsights/rhai-org-pulse/pull/129) — RedHatInsights/rhai-org-pulse
- [#17831 feat(server): PR watch reports missing required checks and behind-base](https://github.com/pingdotgg/t3code/pull/17831) — pingdotgg/t3code
- [#17722 fix(composer): a second skill can be added after the first on the same line](https://github.com/pingdotgg/t3code/pull/17722) — pingdotgg/t3code
- [#17721 fix(mobile): iPad composer accepts dragged screenshots](https://github.com/pingdotgg/t3code/pull/17721) — pingdotgg/t3code
- [#17720 fix(mobile): Android composer accepts images pasted from Gboard](https://github.com/pingdotgg/t3code/pull/17720) — pingdotgg/t3code
- [#17717 fix(mobile): header menu and Git menu reach a thread's linked pull request](https://github.com/pingdotgg/t3code/pull/17717) — pingdotgg/t3code
- [#128 jira-solve-agent: track full OADP repo set (21 repos, incl. migtools org)](https://github.com/RedHatInsights/rhai-org-pulse/pull/128) — RedHatInsights/rhai-org-pulse
- [#17611 fix(mobile): new thread draft names its repo and says it is a new thread](https://github.com/pingdotgg/t3code/pull/17611) — pingdotgg/t3code
- [#252 Speak question speech for Claude AskUserQuestion permission requests](https://github.com/OpenPetsHQ/openpets/pull/252) — OpenPetsHQ/openpets
- [#17606 fix(models): Ultracode is offered on Sonnet 5, Sonnet 5.5 and Haiku 5.5](https://github.com/pingdotgg/t3code/pull/17606) — pingdotgg/t3code
- [#17604 feat(provider): add Claude fork-subagents instance setting](https://github.com/pingdotgg/t3code/pull/17604) — pingdotgg/t3code
- [#17527 fix(web): git actions menu no longer offers Create PR when the thread has a linked PR](https://github.com/pingdotgg/t3code/pull/17527) — pingdotgg/t3code
- [#17521 feat(web): auto-assign accent color to non-default provider instances](https://github.com/pingdotgg/t3code/pull/17521) — pingdotgg/t3code
## PRs Reviewed (70)

**velero-io** (17)
- [#10678 e2e: finish converting the CSI feature checks to FeatureEnabled](https://github.com/velero-io/velero/pull/10678) — velero-io/velero
- [#10385 refactor: propagate context.Context in core kube secrets and namespace utilities](https://github.com/velero-io/velero/pull/10385) — velero-io/velero
- [#10682 [release-1.18] Bump Golang to 1.26.10 and golang.org/x/net to v0.61.0 to fix CVEs](https://github.com/velero-io/velero/pull/10682) — velero-io/velero
- [#10673 Recognize GCS object-not-found error during backup deletion](https://github.com/velero-io/velero/pull/10673) — velero-io/velero
- [#10652 e2e: add a target that runs the tests on a kind cluster it creates](https://github.com/velero-io/velero/pull/10652) — velero-io/velero
- [#10658 e2e: run the Kibishii snapshot cases on kind under CSI](https://github.com/velero-io/velero/pull/10658) — velero-io/velero
- [#10654 Add S3 SSE-C headers to download requests](https://github.com/velero-io/velero/pull/10654) — velero-io/velero
- [#10660 e2e: drop the SKIP_KIND label, which nothing reads](https://github.com/velero-io/velero/pull/10660) — velero-io/velero
- [#10649 Makefile: fix make serve-docs on buildx setups](https://github.com/velero-io/velero/pull/10649) — velero-io/velero
- [#10556 [Design]Owner reference and dependency relink design](https://github.com/velero-io/velero/pull/10556) — velero-io/velero
- [#10493 fix: bound VolumeSnapshot and VolumeSnapshotContent error retry by CSISnapshotTimeout](https://github.com/velero-io/velero/pull/10493) — velero-io/velero
- [#10666 build(deps): bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10666) — velero-io/velero
- [#10657 e2e: point Kibishii at the kind-csi overlay when CSI is enabled](https://github.com/velero-io/velero/pull/10657) — velero-io/velero
- [#10656 Reuse cached Go modules across CI jobs](https://github.com/velero-io/velero/pull/10656) — velero-io/velero
- [#10640 fix(cli): update legacy repository issue URLs in velero bug command](https://github.com/velero-io/velero/pull/10640) — velero-io/velero
- [#10438 Issue #10437: derive velero server's graceful shutdown timeout from terminationGracePeriodSeconds](https://github.com/velero-io/velero/pull/10438) — velero-io/velero
- [#10609 docs: add local Kind setup for CSI e2e](https://github.com/velero-io/velero/pull/10609) — velero-io/velero

**openshift** (34)
- [#2491 [oadp-dev] tests/e2e: retry transient QEMU 'Invalid parameter pid' in guest-exec-status poll](https://github.com/openshift/oadp-operator/pull/2491) — openshift/oadp-operator
- [#493 Bump github.com/klauspost/compress from 1.18.6 to 1.18.7](https://github.com/openshift/openshift-velero-plugin/pull/493) — openshift/openshift-velero-plugin
- [#56 OADP-7954: Add Phase 1 OADP Agent Skills](https://github.com/openshift/agentic-skills/pull/56) — openshift/agentic-skills
- [#182 Add akarol and PrasadJoshi12 to OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/182) — openshift/velero-plugin-for-aws
- [#181 Add akarol to OWNERS](https://github.com/openshift/oadp-must-gather/pull/181) — openshift/oadp-must-gather
- [#182 Update auto-request-review action to v0.13.0](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/182) — openshift/velero-plugin-for-microsoft-azure
- [#487 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/openshift/openshift-velero-plugin/pull/487) — openshift/openshift-velero-plugin
- [#501 Fix 5 CVEs (CVE-2024-41110, CVE-2026-34986, CVE-2025-66506, ...)](https://github.com/openshift/openshift-velero-plugin/pull/501) — openshift/openshift-velero-plugin
- [#502 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.4 (22c704b) into oadp-1.4](https://github.com/openshift/openshift-velero-plugin/pull/502) — openshift/openshift-velero-plugin
- [#602 UPSTREAM: <carry>: add GetLevel() to logrusAdapter to satisfy hclog.Logger interface](https://github.com/openshift/velero/pull/602) — openshift/velero
- [#2489 [OADP-8902] docs: clarify maxConcurrentDataMovers CRD default](https://github.com/openshift/oadp-operator/pull/2489) — openshift/oadp-operator
- [#490 Bump github.com/moby/sys/user from 0.4.0 to 0.4.1](https://github.com/openshift/openshift-velero-plugin/pull/490) — openshift/openshift-velero-plugin
- [#500 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.4 (a2553ae) into oadp-1.4](https://github.com/openshift/openshift-velero-plugin/pull/500) — openshift/openshift-velero-plugin
- [#498 [oadp-1.6] OADP-8924: Treat missing openshift-apiserver config as no internal registry](https://github.com/openshift/openshift-velero-plugin/pull/498) — openshift/openshift-velero-plugin
- [#189 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.10.1 (5c92b55) into oadp-1.4](https://github.com/openshift/velero-plugin-for-aws/pull/189) — openshift/velero-plugin-for-aws
- [#192 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.10.1 (c66d196) into oadp-1.4](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/192) — openshift/velero-plugin-for-microsoft-azure
- [#133 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.4 (7d87261) into oadp-1.4](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/133) — openshift/velero-plugin-for-legacy-aws
- [#591 Bump golangci-lint from v2.5.0 to v2.14.0](https://github.com/openshift/velero/pull/591) — openshift/velero
- [#593 Backport: Add ConfigMap support for keepLatestMaintenanceJobs (oadp-1.5)](https://github.com/openshift/velero/pull/593) — openshift/velero
- [#2477 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/openshift/oadp-operator/pull/2477) — openshift/oadp-operator
- [#2485 tests/e2e: increase three-BSLs default BSL availability timeout from 180s to 300s](https://github.com/openshift/oadp-operator/pull/2485) — openshift/oadp-operator
- [#2493 OADP-8924: Add HCP guest cluster pod backup test case](https://github.com/openshift/oadp-operator/pull/2493) — openshift/oadp-operator
- [#2500 fix: add nil guard for BSL LastValidationTime in BSLsAreUpdated](https://github.com/openshift/oadp-operator/pull/2500) — openshift/oadp-operator
- [#87249 Make oadp AllNamespaces e2e jobs manual-trigger-only and move them to 5.1](https://github.com/openshift/release/pull/87249) — openshift/release
- [#2498 Fix BSL count race condition in multi-BSL e2e test](https://github.com/openshift/oadp-operator/pull/2498) — openshift/oadp-operator
- [#183 Update auto-request-review action to v0.13.0](https://github.com/openshift/velero-plugin-for-gcp/pull/183) — openshift/velero-plugin-for-gcp
- [#177 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (50b3928) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/177) — openshift/oadp-must-gather
- [#2494 OADP-8926, OADP-8911: scope operand network policies and fix DNS egress](https://github.com/openshift/oadp-operator/pull/2494) — openshift/oadp-operator
- [#590 Merge https://github.com/velero-io/velero:v1.14.0 (2fc6300) into oadp-1.4](https://github.com/openshift/velero/pull/590) — openshift/velero
- [#87092 Add optional AllNamespaces e2e presubmits for oadp-operator oadp-dev 5.0](https://github.com/openshift/release/pull/87092) — openshift/release
- [#2484 tests/e2e: retry transient QEMU 'Invalid parameter pid' in guest-exec-status poll](https://github.com/openshift/oadp-operator/pull/2484) — openshift/oadp-operator
- [#2486 tests/e2e: remove redundant dpaCR.IsDeleted() in Undeploy — VeleroIsDeleted already subsumes it](https://github.com/openshift/oadp-operator/pull/2486) — openshift/oadp-operator
- [#180 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.4 (cbd0773) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/180) — openshift/velero-plugin-for-microsoft-azure
- [#122 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (7c90cde) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/122) — openshift/velero-plugin-for-legacy-aws

**migtools** (16)
- [#116 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/oadp-vm-file-restore/pull/116) — migtools/oadp-vm-file-restore
- [#55 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/kopia/pull/55) — migtools/kopia
- [#119 Add akarol to OWNERS](https://github.com/migtools/oadp-vm-file-restore/pull/119) — migtools/oadp-vm-file-restore
- [#278 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/oadp-cli/pull/278) — migtools/oadp-cli
- [#390 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/oadp-non-admin/pull/390) — migtools/oadp-non-admin
- [#97 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/kubevirt-velero-plugin/pull/97) — migtools/kubevirt-velero-plugin
- [#193 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/udistribution/pull/193) — migtools/udistribution
- [#40 Add AGENTS.md and AI tool configs for agentic development readiness](https://github.com/migtools/oadp-vmdp/pull/40) — migtools/oadp-vmdp
- [#61 Add akarol to OWNERS](https://github.com/migtools/kopia/pull/61) — migtools/kopia
- [#285 Merge https://github.com/migtools/oadp-cli:oadp-1.4 (50b9d39) into oadp-1.4](https://github.com/migtools/oadp-cli/pull/285) — migtools/oadp-cli
- [#189 Bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/189) — migtools/udistribution
- [#50 chore(deps-dev): bump vite from 8.0.16 to 8.1.6 in /frontend](https://github.com/migtools/filebrowser/pull/50) — migtools/filebrowser
- [#103 Add akarol to OWNERS](https://github.com/migtools/kubevirt-velero-plugin/pull/103) — migtools/kubevirt-velero-plugin
- [#105 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.7.1 (c30669d) into oadp-1.4](https://github.com/migtools/kubevirt-velero-plugin/pull/105) — migtools/kubevirt-velero-plugin
- [#59 Fix CVE-2026-63209](https://github.com/migtools/kopia/pull/59) — migtools/kopia
- [#280 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (1e1b143) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/280) — migtools/oadp-cli

**Other** (3)
- [#23732 fix(web): PDF previews keep their page when the agent responds](https://github.com/pingdotgg/t3code/pull/23732) — pingdotgg/t3code
- [#23510 fix(clients): later image reads show updated file contents](https://github.com/pingdotgg/t3code/pull/23510) — pingdotgg/t3code
- [#208 Refresh dashboard CVE data when a fix PR merges](https://github.com/oadp-rebasebot/oadp-rebase/pull/208) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (100)

**velero-io** (49)
- [#10694 E2E: verify retained data mover snapshots are deleted from the storage on backup deletion (kind CSI job)](https://github.com/velero-io/velero/issues/10694) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#4045 Allow customizing restore order for Kubernetes controllers and their managed resources](https://github.com/velero-io/velero/issues/4045) — velero-io/velero
- [#10627 Allow Multiple Key Properties](https://github.com/velero-io/velero/issues/10627) — velero-io/velero
- [#9109 Add comprehensive make target for E2E testing with MinIO setup and fresh builds](https://github.com/velero-io/velero/issues/9109) — velero-io/velero
- [#10266 docs: how to run CSI e2e specs against a local Kind cluster](https://github.com/velero-io/velero/issues/10266) — velero-io/velero
- [#8668 Download Links for S3 Bucket content are broken when using SSE-C encryption](https://github.com/velero-io/velero/issues/8668) — velero-io/velero
- [#10646 Consider enrolling Velero in Anthropic OSS Scanner](https://github.com/velero-io/velero/issues/10646) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#8454 Large PVCs are canceled](https://github.com/velero-io/velero/issues/8454) — velero-io/velero
- [#9189 Support deleting running backups](https://github.com/velero-io/velero/issues/9189) — velero-io/velero
- [#2098 Implement abort running backup job](https://github.com/velero-io/velero/issues/2098) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#10299 Backup with --snapshot-move-data completes with zero DataUploads when EnableCSI is off — no upfront validation, and the warning/skip-reason don't name the flag](https://github.com/velero-io/velero/issues/10299) — velero-io/velero
- [#10310 Include the errors/warnings from node-agent and data-mover pods in the velero backup/restore get/describe commands](https://github.com/velero-io/velero/issues/10310) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#9735 Velero should add a clear error when data mover pod is unschedulable due to affinity/topology mismatch](https://github.com/velero-io/velero/issues/9735) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
- [#10545 CRD schema check: make `warn` mode non-blocking and bound `strict` mode with a shared timeout](https://github.com/velero-io/velero/issues/10545) — velero-io/velero
- [#10544 CRD schema check: self-resolution for `strict` mode failures (`/readyz` instead of crash-loop)](https://github.com/velero-io/velero/issues/10544) — velero-io/velero
- [#9556 Block level backup/restore support](https://github.com/velero-io/velero/issues/9556) — velero-io/velero
- [#8707 Support multiple transmission protocols](https://github.com/velero-io/velero/issues/8707) — velero-io/velero
- [#10340 Bug: EphemeralContainers are missing from ServiceAccount token filtering in PodAction](https://github.com/velero-io/velero/issues/10340) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#2812 Restore fails with error "no space left on device" if PVCs are 100% utilised during backup](https://github.com/velero-io/velero/issues/2812) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#8263 Fatal: unable to open config file results in PartiallyFailed Backup](https://github.com/velero-io/velero/issues/8263) — velero-io/velero
- [#9318 Behavior of skip volume policy is strange/problematic](https://github.com/velero-io/velero/issues/9318) — velero-io/velero
- [#9453 DataUpload tasks stuck in Prepared phase for extended periods](https://github.com/velero-io/velero/issues/9453) — velero-io/velero
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#9833 Backup/restore describe for block data mover](https://github.com/velero-io/velero/issues/9833) — velero-io/velero
- [#9835 Backup deletion for block data mover](https://github.com/velero-io/velero/issues/9835) — velero-io/velero
- [#10478 Support structured output for multi-item backup and restore describe](https://github.com/velero-io/velero/issues/10478) — velero-io/velero
- [#7564 Add support to output restore describe in multiple format like backups](https://github.com/velero-io/velero/issues/7564) — velero-io/velero
- [#8654 Velero backups failing due to blob missing from the repository](https://github.com/velero-io/velero/issues/8654) — velero-io/velero
- [#10440 Cleanup: Resolve Ginkgo V2 and Gomega anti-patterns in test suite](https://github.com/velero-io/velero/issues/10440) — velero-io/velero
- [#10437 `velero server`'s shutdown grace period is hardcoded to 30s, ignoring `terminationGracePeriodSeconds`](https://github.com/velero-io/velero/issues/10437) — velero-io/velero
- [#9656 Kopia maintenance fails with 'ciphertext too short: 0' after S3 quota-related write failures leave 0-byte blobs](https://github.com/velero-io/velero/issues/9656) — velero-io/velero
- [#9760 Allow Velero kubernetes objects to be backed up with If-None-Match bucket policies enabled.](https://github.com/velero-io/velero/issues/9760) — velero-io/velero
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#9603 Backport/Cherry-pick GitHub action](https://github.com/velero-io/velero/issues/9603) — velero-io/velero
- [#9839 CBT availability detection per volume](https://github.com/velero-io/velero/issues/9839) — velero-io/velero
- [#9894 Transition all project meetings to CNCF Zoom](https://github.com/velero-io/velero/issues/9894) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#9429 velero doesn't correctly handle an empty ProviderSnapshotID](https://github.com/velero-io/velero/issues/9429) — velero-io/velero

**openshift** (8)
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#439 Image stream backup: Azure Workload Identity (WIF) not supported in registry env var wiring](https://github.com/openshift/openshift-velero-plugin/issues/439) — openshift/openshift-velero-plugin
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator
- [#2413 Poll: how to fix e2e-test-kubevirt-aws hitting the 2h Prow step timeout](https://github.com/openshift/oadp-operator/issues/2413) — openshift/oadp-operator
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer

**migtools** (2)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#14 Handle guest agent connectivity and SkipQuiesce for VirtualMachineBackup](https://github.com/migtools/kubevirt-datamover-controller/issues/14) — migtools/kubevirt-datamover-controller

**Other** (41)
- [#19736 [Bug]: A message queued behind a running turn pushes the "Working for…" header below it](https://github.com/pingdotgg/t3code/issues/19736) — pingdotgg/t3code
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#16000 [Bug]: Runtime-mode, instance and worktree changes detach the Claude session and kill live subagents without the background-work check](https://github.com/pingdotgg/t3code/issues/16000) — pingdotgg/t3code
- [#17875 VEP#25 Enhancement: Incremental VirtualMachineBackup delta is always relative to VirtualMachineBackupTracker.status.latestCheckpoint only (no arbitrary base checkpoint)](https://github.com/kubevirt/kubevirt/issues/17875) — kubevirt/kubevirt
- [#1419 `kubectl explain -o md`](https://github.com/kubernetes/kubectl/issues/1419) — kubernetes/kubectl
- [#26598 Support `strategy.matrix` on the `agent` job for parallel AI execution](https://github.com/github/gh-aw/issues/26598) — github/gh-aw
- [#17531 Claude provider hangs on Bash calls when a UI-dependent Claude Code mod (e.g. blast-radius) is installed](https://github.com/pingdotgg/t3code/issues/17531) — pingdotgg/t3code
- [#17422 [Bug]: Mobile composer stops saving typed text, so the send button stays disabled until the app restarts](https://github.com/pingdotgg/t3code/issues/17422) — pingdotgg/t3code
- [#956 [Feature Request] Lock Bolt BLE: read-only protocol paths (realtime status, door state, history, settings read-back)](https://github.com/SecKatie/ha-wyzeapi/issues/956) — SecKatie/ha-wyzeapi
- [#10553 [Bug]: File links in agent output always resolve against the thread's project, not the repo the file is in](https://github.com/pingdotgg/t3code/issues/10553) — pingdotgg/t3code
- [#502 Enhancement: Allow combining `run_if_changed` and `skip_if_only_changed` for more flexible job triggering](https://github.com/kubernetes-sigs/prow/issues/502) — kubernetes-sigs/prow
- [#17508 [Bug]: Antigravity Google sign-in hides the real failure reason (ineligible account, rejected redirect URL)](https://github.com/pingdotgg/t3code/issues/17508) — pingdotgg/t3code
- [#134 `tide` not honoring multiple reviewer branch protection](https://github.com/kubernetes-sigs/prow/issues/134) — kubernetes-sigs/prow
- [#16992 [Bug]: Jira MCP Apps render blank inline cards despite successful tool results](https://github.com/pingdotgg/t3code/issues/16992) — pingdotgg/t3code
- [#245 Package errors looking for new maintainers](https://github.com/pkg/errors/issues/245) — pkg/errors
- [#438 Add regex support for branch matching in Tide status controller](https://github.com/kubernetes-sigs/prow/issues/438) — kubernetes-sigs/prow
- [#3314 CSI Differential Snapshot for Block Volumes](https://github.com/kubernetes/enhancements/issues/3314) — kubernetes/enhancements
- [#17655 [Bug]: Composer: can't insert a second slash-command skill on the same line (needs Shift+Return)](https://github.com/pingdotgg/t3code/issues/17655) — pingdotgg/t3code
- [#17718 [Bug]: Android composer ignores images pasted from Gboard](https://github.com/pingdotgg/t3code/issues/17718) — pingdotgg/t3code
- [#15234 [Feature]: Continue a Codex or Claude Code session started in the terminal as a T3 Code thread](https://github.com/pingdotgg/t3code/issues/15234) — pingdotgg/t3code
- [#13875 [Bug]: Claude model picker not synchronized with Claude Code model list, unlike Codex](https://github.com/pingdotgg/t3code/issues/13875) — pingdotgg/t3code
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
- [#4300 cdi-importer image sha256:b2241514d6f3... missing amd64 manifest (only s390x)](https://github.com/kubevirt/containerized-data-importer/issues/4300) — kubevirt/containerized-data-importer
- [#101 UDP support](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#12543 Issue can land permanently blocked on a "recovery owner"/disposition state when the run that created it terminates](https://github.com/paperclipai/paperclip/issues/12543) — paperclipai/paperclip
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
- [#18963 VEP #25: Infer backup target StorageClass from source VM volumes](https://github.com/kubevirt/kubevirt/issues/18963) — kubevirt/kubevirt
- [#2 OtpExtractor: support alphanumeric OTP codes](https://github.com/kaovilai/cliprelay/issues/2) — kaovilai/cliprelay
- [#2525 `pull_request_review_write` combines create/submit/delete into one tool, making fine-grained permissions by method impossible](https://github.com/github/github-mcp-server/issues/2525) — github/github-mcp-server
- [#915 branchprotector cannot manage required status check GitHub App identity](https://github.com/kubernetes-sigs/prow/issues/915) — kubernetes-sigs/prow
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
- [#1847 Include scrollback history in state restoration](https://github.com/ghostty-org/ghostty/issues/1847) — ghostty-org/ghostty
- [#481 Support using a later patch release than what's in go.mod](https://github.com/actions/setup-go/issues/481) — actions/setup-go
- [#18959 VEP #25: CBT: completed VirtualMachineBackup can be overwritten with SourceLost due to a stale reconcile race](https://github.com/kubevirt/kubevirt/issues/18959) — kubevirt/kubevirt
- [#18950 VEP #25: CBT: VirtualMachineBackup status freezes indefinitely while target PVC attach is pending](https://github.com/kubevirt/kubevirt/issues/18950) — kubevirt/kubevirt
- [#378 ci on real hw](https://github.com/socktainer/socktainer/issues/378) — socktainer/socktainer
## Issues Closed (89)

**velero-io** (26)
- [#10653 Improve CI reliability by reusing Go module caches across test jobs](https://github.com/velero-io/velero/issues/10653) — velero-io/velero
- [#10076 Dependabot auto approve action](https://github.com/velero-io/velero/issues/10076) — velero-io/velero
- [#10564 E2E test coverage for namespace selection by label in resource policy](https://github.com/velero-io/velero/issues/10564) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
- [#10545 CRD schema check: make `warn` mode non-blocking and bound `strict` mode with a shared timeout](https://github.com/velero-io/velero/issues/10545) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#9771 Design: ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/9771) — velero-io/velero
- [#10295 CBT delta-error fallback marks the whole device dirty instead of the design's allocated-blocks full backup](https://github.com/velero-io/velero/issues/10295) — velero-io/velero
- [#10298 Setting node-agent csiSnapshotMetadataServiceConfigs.saName breaks all CSI snapshot datamover backups (arg/flag name mismatch)](https://github.com/velero-io/velero/issues/10298) — velero-io/velero
- [#10294 Generic CSI changeID retrieval returns empty — all non-vSphere drivers silently fall back to full backups](https://github.com/velero-io/velero/issues/10294) — velero-io/velero
- [#10328 Stop committing generated config/crd/*/crds/crds.go; embed CRDs via go:embed at build time](https://github.com/velero-io/velero/issues/10328) — velero-io/velero
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#10296 Cancelling a block data mover backup reports it as a failure — cancel sentinel compared with == against a wrapped error](https://github.com/velero-io/velero/issues/10296) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10300 Unified repo config dir resolves to unwritable /udmrepo when HOME=/ (arbitrary-UID / OpenShift non-root server)](https://github.com/velero-io/velero/issues/10300) — velero-io/velero
- [#10301 Dead code in repository maintenance: GenOptionMaintainMode/Full/Quick and overwrite*MaintainInterval are unreachable](https://github.com/velero-io/velero/issues/10301) — velero-io/velero
- [#10304 Block data mover: retained CBT base snapshots are never reclaimed at backup deletion (design L370-371/L474 unimplemented)](https://github.com/velero-io/velero/issues/10304) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#10046 fs-backup restore deadlocks at Init:0/1 on owner-restricted volumes — restore-wait init container ignores pod-level securityContext, falls back to hardcoded runAsUser 1000](https://github.com/velero-io/velero/issues/10046) — velero-io/velero
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#10099 Update velero.io community pages](https://github.com/velero-io/velero/issues/10099) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#10022 Flaky unit test:  TestBlockUploaderBackup/success_full_backup](https://github.com/velero-io/velero/issues/10022) — velero-io/velero
- [#10042 Add `.github` repo](https://github.com/velero-io/velero/issues/10042) — velero-io/velero

**openshift** (16)
- [#259 Cherrypicks missing for https://github.com/openshift/enhancements/pull/1945 related PRs to oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/issues/259) — openshift/hypershift-oadp-plugin
- [#258 No HostedControlPlane found: unexpected behavior during HostedControlPlane backup](https://github.com/openshift/hypershift-oadp-plugin/issues/258) — openshift/hypershift-oadp-plugin
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#448 Feature request: detect/reconcile SCC UID/GID-range mismatch on Namespace restore](https://github.com/openshift/openshift-velero-plugin/issues/448) — openshift/openshift-velero-plugin
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
- [#2384 e2e: add cacert tests](https://github.com/openshift/oadp-operator/issues/2384) — openshift/oadp-operator
- [#2410 oadp-1.4: test-e2e Makefile target doesn't generate junit_report.xml](https://github.com/openshift/oadp-operator/issues/2410) — openshift/oadp-operator
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#2383 Evaluate and migrate user-provided credentialsFile handling for Velero #10254](https://github.com/openshift/oadp-operator/issues/2383) — openshift/oadp-operator
- [#5333 e2e-oo permanently failing: fixture pins EOL integrated stream ocp/4.6, configresolver returns 400](https://github.com/openshift/ci-tools/issues/5333) — openshift/ci-tools
- [#2209 Feature request: Additive extraArgs for Velero server and node-agent](https://github.com/openshift/oadp-operator/issues/2209) — openshift/oadp-operator
- [#2236 Flaky E2E: DPA reconciliation race condition causes NoDefaultBackupLocation test failure](https://github.com/openshift/oadp-operator/issues/2236) — openshift/oadp-operator
- [#2351 kubevirt-datamover ClusterRole missing RBAC for Phase 3 (DataDownload) support](https://github.com/openshift/oadp-operator/issues/2351) — openshift/oadp-operator
- [#149 Gather PVC/PV/Namespace(SCC) data for backed-up/restored app namespaces to diagnose restore permission/ownership bugs](https://github.com/openshift/oadp-must-gather/issues/149) — openshift/oadp-must-gather
- [#5328 src-bundle build flake: no node selector lets buildah pod land on arm64 node, fails pulling amd64-only pipeline:src manifest list](https://github.com/openshift/ci-tools/issues/5328) — openshift/ci-tools

**migtools** (18)
- [#211 DataUpload stuck forever: "VMBT already prepared but VMB not yet visible in cache, requeuing"](https://github.com/migtools/kubevirt-datamover-controller/issues/211) — migtools/kubevirt-datamover-controller
- [#198 Add regression test: ensureWorkPVC must force ReadWriteOnce regardless of target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/issues/198) — migtools/kubevirt-datamover-controller
- [#42 Follow-up: address CodeRabbit code-quality suggestions declined during PR #41 review](https://github.com/migtools/kubevirt-datamover-plugin/issues/42) — migtools/kubevirt-datamover-plugin
- [#130 Checkpoint chain integrity gaps not covered by #77 (corrupt-but-present objects, TOCTOU, memoization verdict-loss, index history wipe)](https://github.com/migtools/kubevirt-datamover-controller/issues/130) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#121 Spec.OperationTimeout is not honored by either DataUpload or DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/121) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller
- [#168 Configurable VMB (and VMBT) cleanup after DataUpload Failed transition](https://github.com/migtools/kubevirt-datamover-controller/issues/168) — migtools/kubevirt-datamover-controller
- [#171 DataUpload cleanup blocks reconcile worker when pod cleanup hasn't finished before PVC/PV cleanup](https://github.com/migtools/kubevirt-datamover-controller/issues/171) — migtools/kubevirt-datamover-controller
- [#45 VM restore Progress's first-DataDownload grace period is anchored to restore start, not operation registration](https://github.com/migtools/kubevirt-datamover-plugin/issues/45) — migtools/kubevirt-datamover-plugin
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller
- [#160 Checkpoint index records requested PVC size, not actual PV capacity, undersizing restore scratch space](https://github.com/migtools/kubevirt-datamover-controller/issues/160) — migtools/kubevirt-datamover-controller

**Other** (29)
- [#601 Icon request: fusion360](https://github.com/devicons/devicon/issues/601) — devicons/devicon
- [#19736 [Bug]: A message queued behind a running turn pushes the "Working for…" header below it](https://github.com/pingdotgg/t3code/issues/19736) — pingdotgg/t3code
- [#450 Proposal: fallback list / auto-discovery for small, search and auto-mode models when a model is retired](https://github.com/caozhiyuan/copilot-api/issues/450) — caozhiyuan/copilot-api
- [#17529 [Bug]: Git actions menu offers "Create PR" when the thread already has a linked PR on another ref](https://github.com/pingdotgg/t3code/issues/17529) — pingdotgg/t3code
- [#17506 Model picker/composer: hard to tell which provider instance is active](https://github.com/pingdotgg/t3code/issues/17506) — pingdotgg/t3code
- [#19422 [Bug]: Mobile review diff stops scrolling before the end of long unwrapped lines (Android, iOS)](https://github.com/pingdotgg/t3code/issues/19422) — pingdotgg/t3code
- [#4 [bug] This page did not say which commits the pull request compares, so there is nothing to preview. Reload the Files changed tab and try again; if it keeps happenin…](https://github.com/kaovilai/github-html-diff-preview/issues/4) — kaovilai/github-html-diff-preview
- [#848 status-reconciler can permanently miss config changes when delta delivery times out](https://github.com/kubernetes-sigs/prow/issues/848) — kubernetes-sigs/prow
- [#265 Feature: throw the pet like a ball (release inertia + bounce off the current monitor's edges)](https://github.com/OpenPetsHQ/openpets/issues/265) — OpenPetsHQ/openpets
- [#17718 [Bug]: Android composer ignores images pasted from Gboard](https://github.com/pingdotgg/t3code/issues/17718) — pingdotgg/t3code
- [#17610 [Bug]: iPad new-thread draft names the project by folder and shows no "New thread" header](https://github.com/pingdotgg/t3code/issues/17610) — pingdotgg/t3code
- [#17644 [Enhancement]: Report missing required checks and behind-base in native PR watches](https://github.com/pingdotgg/t3code/issues/17644) — pingdotgg/t3code
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#251 Bug: "Approval needed" shown for AskUserQuestion (and other non-approval PermissionRequests)](https://github.com/OpenPetsHQ/openpets/issues/251) — OpenPetsHQ/openpets
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
- [#1623 jira_transition_issue's `comment` argument silently dropped on Jira Cloud (transition succeeds, comment never posts)](https://github.com/sooperset/mcp-atlassian/issues/1623) — sooperset/mcp-atlassian
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#625 Add pagination support for get_pull_request_diff to handle large PRs](https://github.com/github/github-mcp-server/issues/625) — github/github-mcp-server
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
- [#148413 View multiple debug consoles side by side in editor areas](https://github.com/microsoft/vscode/issues/148413) — microsoft/vscode
- [#176 Group my contributions by organization than by repository of the repos](https://github.com/kaovilai/kaovilai.pw/issues/176) — kaovilai/kaovilai.pw
- [#147 group dependabot prs into ecosystems.. ie typescript, actions, etc.](https://github.com/kaovilai/github-bot-command-palette/issues/147) — kaovilai/github-bot-command-palette
- [#69 activity.json is not updated the same time as .md files.](https://github.com/kaovilai/kaovilai/issues/69) — kaovilai/kaovilai
- [#1 Implement my gemini app into github pages static](https://github.com/kaovilai/route-127-trailer-nc/issues/1) — kaovilai/route-127-trailer-nc
- [#146 https://legacy.kaovilai.pw/pay-me this section has thai qr code payment info. add it to here](https://github.com/kaovilai/kaovilai.pw/issues/146) — kaovilai/kaovilai.pw
- [#67 Add JSON export alongside MY_ACTIVITY.md / MY_PULL_REQUESTS.md for site consumption](https://github.com/kaovilai/kaovilai/issues/67) — kaovilai/kaovilai
- [#74 gh aw compile isn't available in this environment prevent use gh aw install action](https://github.com/kaovilai/kaovilai.pw/issues/74) — kaovilai/kaovilai.pw
- [#1492 Move CRD installs out of Reconcile](https://github.com/stolostron/multiclusterhub-operator/issues/1492) — stolostron/multiclusterhub-operator
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
