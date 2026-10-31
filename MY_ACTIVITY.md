# Activity Log

> **Period:** 2026-08-02 — 2026-10-31
> **Generated:** 2026-10-31 05:16:19 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 100 |
| PRs Opened | 100 |
| PRs Reviewed | 77 |
| Issues/PRs Commented | 100 |
| Issues Closed | 87 |

---

## PRs Merged (100)

**velero-io** (19)
- [#10689 Group Go security updates in Dependabot](https://github.com/velero-io/velero/pull/10689) — velero-io/velero
- [#10695 ci: add CodeQL analysis for Go](https://github.com/velero-io/velero/pull/10695) — velero-io/velero
- [#10752 docs: add data mover memory and upload concurrency tuning guidance](https://github.com/velero-io/velero/pull/10752) — velero-io/velero
- [#319 Add CODEOWNERS for automatic review requests](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/319) — velero-io/velero-plugin-for-microsoft-azure
- [#10690 [release-1.18] Bump paketobuildpacks/run-jammy-tiny to 0.2.190](https://github.com/velero-io/velero/pull/10690) — velero-io/velero
- [#10700 Treat a kopia snapshot not found after a repo refresh as deleted](https://github.com/velero-io/velero/pull/10700) — velero-io/velero
- [#10696 design: fix the order of the snapshot retention cases in block data mover](https://github.com/velero-io/velero/pull/10696) — velero-io/velero
- [#10698 Fix BLKZEROOUT ioctl request number in block uploader](https://github.com/velero-io/velero/pull/10698) — velero-io/velero
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

**openshift** (32)
- [#327 NO-JIRA: Group Go security updates in Dependabot](https://github.com/openshift/hypershift-oadp-plugin/pull/327) — openshift/hypershift-oadp-plugin
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

**migtools** (11)
- [#197 Group Go security updates in Dependabot](https://github.com/migtools/udistribution/pull/197) — migtools/udistribution
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

**Other** (38)
- [#213 docs: seed OADP FAQ with curated answers](https://github.com/oadp-rebasebot/oadp-rebase/pull/213) — oadp-rebasebot/oadp-rebase
- [#17 fix: parse every stream event so first-token timing is recorded](https://github.com/kaovilai/copilot-api/pull/17) — kaovilai/copilot-api
- [#16 Merge upstream/dev (2.7.43, incl. request plugins) into dev](https://github.com/kaovilai/copilot-api/pull/16) — kaovilai/copilot-api
- [#649 docs: document enableSeLinuxHostMount for node plugins](https://github.com/ceph/ceph-csi-operator/pull/649) — ceph/ceph-csi-operator
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
## PRs Opened (100)

**velero-io** (32)
- [#10752 docs: add data mover memory and upload concurrency tuning guidance](https://github.com/velero-io/velero/pull/10752) — velero-io/velero
- [#10750 Reject malformed glob patterns in resource filters](https://github.com/velero-io/velero/pull/10750) — velero-io/velero
- [#10749 e2e: bound each Kibishii verify attempt by the poll deadline](https://github.com/velero-io/velero/pull/10749) — velero-io/velero
- [#10718 docs: correct schedule useOwnerReferencesInBackup deletion and block data mover volume mode guidance](https://github.com/velero-io/velero/pull/10718) — velero-io/velero
- [#10717 Store resourceTimeout in the backup finalizer reconciler](https://github.com/velero-io/velero/pull/10717) — velero-io/velero
- [#10716 Retain the backup snapshot only for the block data mover](https://github.com/velero-io/velero/pull/10716) — velero-io/velero
- [#10715 Fail backup when its metadata can't be written to the BSL](https://github.com/velero-io/velero/pull/10715) — velero-io/velero
- [#10714 Don't hold restore in Finalizing when results upload fails](https://github.com/velero-io/velero/pull/10714) — velero-io/velero
- [#10713 Drop deleted backups from the backup tracker; clarify useOwnerReferencesInBackup on schedule deletion](https://github.com/velero-io/velero/pull/10713) — velero-io/velero
- [#10712 Warn when resource modifiers change a PVC's volumeMode from Block on restore](https://github.com/velero-io/velero/pull/10712) — velero-io/velero
- [#10711 Back up raw block volumes with snapshots instead of skipping them when defaultVolumesToFsBackup is set](https://github.com/velero-io/velero/pull/10711) — velero-io/velero
- [#10710 Clean up CSI VolumeSnapshots of failed backups outside the Velero namespace](https://github.com/velero-io/velero/pull/10710) — velero-io/velero
- [#10709 Refuse to delete a backup while a restore from it is in progress](https://github.com/velero-io/velero/pull/10709) — velero-io/velero
- [#10708 Delete retained source VSC when cleaning up an interrupted CSI snapshot expose](https://github.com/velero-io/velero/pull/10708) — velero-io/velero
- [#10707 Add expose diagnose summary to DU/DD/PVB/PVR prepare timeout message](https://github.com/velero-io/velero/pull/10707) — velero-io/velero
- [#10706 Fill the container termination reason to DU/DD/PVB/PVR when the data mover pod is OOMKilled](https://github.com/velero-io/velero/pull/10706) — velero-io/velero
- [#10705 Don't block DataDownload controller waiting for target PVC consumer](https://github.com/velero-io/velero/pull/10705) — velero-io/velero
- [#10704 Fail data path when its data mover pod is deleted, release leaked data path slot](https://github.com/velero-io/velero/pull/10704) — velero-io/velero
- [#10703 Report the CSI snapshot error when waiting for the snapshot handle times out](https://github.com/velero-io/velero/pull/10703) — velero-io/velero
- [#10702 Back off repo maintenance retries after failures, skip maintenance on unavailable BSL](https://github.com/velero-io/velero/pull/10702) — velero-io/velero
- [#10701 Bound block data mover memory burst and set Go memory limit](https://github.com/velero-io/velero/pull/10701) — velero-io/velero
- [#10700 Treat a kopia snapshot not found after a repo refresh as deleted](https://github.com/velero-io/velero/pull/10700) — velero-io/velero
- [#10699 Delete the in-place restore baseline snapshot under a Retain class](https://github.com/velero-io/velero/pull/10699) — velero-io/velero
- [#10698 Fix BLKZEROOUT ioctl request number in block uploader](https://github.com/velero-io/velero/pull/10698) — velero-io/velero
- [#10696 design: fix the order of the snapshot retention cases in block data mover](https://github.com/velero-io/velero/pull/10696) — velero-io/velero
- [#10695 ci: add CodeQL analysis for Go](https://github.com/velero-io/velero/pull/10695) — velero-io/velero
- [#10692 Add Dependabot updates for run-jammy-tiny on supported release branches](https://github.com/velero-io/velero/pull/10692) — velero-io/velero
- [#10691 Delete retained volume snapshots on backup deletion for data movement](https://github.com/velero-io/velero/pull/10691) — velero-io/velero
- [#10690 [release-1.18] Bump paketobuildpacks/run-jammy-tiny to 0.2.190](https://github.com/velero-io/velero/pull/10690) — velero-io/velero
- [#10689 Group Go security updates in Dependabot](https://github.com/velero-io/velero/pull/10689) — velero-io/velero
- [#10683 docs: point README OpenSSF Best Practices badge at bestpractices.dev](https://github.com/velero-io/velero/pull/10683) — velero-io/velero
- [#5 Draft Velero CNCF incubation security and engineering materials](https://github.com/velero-io/.github/pull/5) — velero-io/.github

**openshift** (31)
- [#2525 docs: describe descheduler impact on virtualization backups](https://github.com/openshift/oadp-operator/pull/2525) — openshift/oadp-operator
- [#604 [oadp-1.6] Handle data mover and hook pods that go away during a backup](https://github.com/openshift/velero/pull/604) — openshift/velero
- [#2519 docs: note that nodeAgent.loadAffinity also limits File System Backup](https://github.com/openshift/oadp-operator/pull/2519) — openshift/oadp-operator
- [#2518 Keep IPv6 brackets when stripping default port from s3Url](https://github.com/openshift/oadp-operator/pull/2518) — openshift/oadp-operator
- [#2517 Delete registry secrets of BSLs removed from the DPA](https://github.com/openshift/oadp-operator/pull/2517) — openshift/oadp-operator
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

**migtools** (18)
- [#199 deps: consolidate pending dependabot bumps](https://github.com/migtools/udistribution/pull/199) — migtools/udistribution
- [#198 ci: fail on unformatted Go instead of pushing a format commit](https://github.com/migtools/udistribution/pull/198) — migtools/udistribution
- [#111 UPSTREAM: <carry>: Select the live virt-launcher pod after live migration](https://github.com/migtools/kubevirt-velero-plugin/pull/111) — migtools/kubevirt-velero-plugin
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

**Other** (19)
- [#213 docs: seed OADP FAQ with curated answers](https://github.com/oadp-rebasebot/oadp-rebase/pull/213) — oadp-rebasebot/oadp-rebase
- [#17 fix: parse every stream event so first-token timing is recorded](https://github.com/kaovilai/copilot-api/pull/17) — kaovilai/copilot-api
- [#16 Merge upstream/dev (2.7.43, incl. request plugins) into dev](https://github.com/kaovilai/copilot-api/pull/16) — kaovilai/copilot-api
- [#6479 KEP-3314: document requireBaseSnapshotForDelta on SnapshotMetadataService](https://github.com/kubernetes/enhancements/pull/6479) — kubernetes/enhancements
- [#6569 fix(autocomplete): use file name of the binary as default basename](https://github.com/scaleway/scaleway-cli/pull/6569) — scaleway/scaleway-cli
- [#18636 csi: enable selinux host mount in openshift example](https://github.com/rook/rook/pull/18636) — rook/rook
- [#1793 fix(server): stop orphaned stdio servers by honoring SIGTERM and parent exit](https://github.com/sooperset/mcp-atlassian/pull/1793) — sooperset/mcp-atlassian
- [#649 docs: document enableSeLinuxHostMount for node plugins](https://github.com/ceph/ceph-csi-operator/pull/649) — ceph/ceph-csi-operator
- [#82 Ignore assets/profile in Imgbot](https://github.com/kaovilai/kaovilai/pull/82) — kaovilai/kaovilai
- [#5748 fix(providers): return S3 PutObject error when GetModTime is requested](https://github.com/kopia/kopia/pull/5748) — kopia/kopia
- [#115 docs(welcome): document EnMaaS request body limit](https://github.com/redhat-et/pricetag-metering/pull/115) — redhat-et/pricetag-metering
- [#453 feat: log per-request latency and time to first token](https://github.com/caozhiyuan/copilot-api/pull/453) — caozhiyuan/copilot-api
- [#198 docs: Android update via Tasker; stable-name release zip (v1.1.2)](https://github.com/kaovilai/github-bot-command-palette/pull/198) — kaovilai/github-bot-command-palette
- [#197 fix(content): give the review-dialog command bar its own row](https://github.com/kaovilai/github-bot-command-palette/pull/197) — kaovilai/github-bot-command-palette
- [#196 feat: in-extension update check and automated GitHub releases](https://github.com/kaovilai/github-bot-command-palette/pull/196) — kaovilai/github-bot-command-palette
- [#452 feat: publish in-flight generation requests to an optional directory](https://github.com/caozhiyuan/copilot-api/pull/452) — caozhiyuan/copilot-api
- [#195 fix(settings): shard config across sync keys to stay under 8 KB item quota](https://github.com/kaovilai/github-bot-command-palette/pull/195) — kaovilai/github-bot-command-palette
- [#15 Merge upstream/dev (268 commits) into dev](https://github.com/kaovilai/copilot-api/pull/15) — kaovilai/copilot-api
- [#1571 Add support for Chipsea-BLE GATT body fat scales](https://github.com/oliexdev/openScale/pull/1571) — oliexdev/openScale
## PRs Reviewed (77)

**velero-io** (29)
- [#10761 Add 1.19 release notes](https://github.com/velero-io/velero/pull/10761) — velero-io/velero
- [#10764 e2e: run the FSBackup backup deletion case on kind under CSI](https://github.com/velero-io/velero/pull/10764) — velero-io/velero
- [#6 Clarify the code repositories in GOVERNANCE.md](https://github.com/velero-io/.github/pull/6) — velero-io/.github
- [#10766 build(deps): bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10766) — velero-io/velero
- [#10762 Restic deprecation: ignore invalid PVB uploader](https://github.com/velero-io/velero/pull/10762) — velero-io/velero
- [#10759 Expose resourcemodifiers package to pkg for plugin reuse](https://github.com/velero-io/velero/pull/10759) — velero-io/velero
- [#10760 Add doc for custom action in volume policy](https://github.com/velero-io/velero/pull/10760) — velero-io/velero
- [#10739 fix(tilt): make the dev setup work on a clean checkout and on arm64](https://github.com/velero-io/velero/pull/10739) — velero-io/velero
- [#336 Update auto-assignees.yml](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/336) — velero-io/velero-plugin-for-microsoft-azure
- [#10735 e2e: add fine-grained resource and restore filter test via resource policies](https://github.com/velero-io/velero/pull/10735) — velero-io/velero
- [#10753 Rollback create retain snapshot](https://github.com/velero-io/velero/pull/10753) — velero-io/velero
- [#280 Update assignees in the yaml file](https://github.com/velero-io/velero-plugin-for-gcp/pull/280) — velero-io/velero-plugin-for-gcp
- [#335 Make the S3 uploader inherit the client's RequestChecksumCalculation](https://github.com/velero-io/velero-plugin-for-aws/pull/335) — velero-io/velero-plugin-for-aws
- [#10740 Issue 10724: Add parallel upload/download control for Velero fs and block data mover](https://github.com/velero-io/velero/pull/10740) — velero-io/velero
- [#10751 build(deps): bump github.com/go-jose/go-jose/v4 from 4.1.4 to 4.1.6](https://github.com/velero-io/velero/pull/10751) — velero-io/velero
- [#10747 e2e: run the BSL deletion snapshot case on kind under CSI](https://github.com/velero-io/velero/pull/10747) — velero-io/velero
- [#10652 e2e: add a target that runs the tests on a kind cluster it creates](https://github.com/velero-io/velero/pull/10652) — velero-io/velero
- [#340 Update the auto-assignees.yml of aws plugin](https://github.com/velero-io/velero-plugin-for-aws/pull/340) — velero-io/velero-plugin-for-aws
- [#10678 e2e: finish converting the CSI feature checks to FeatureEnabled](https://github.com/velero-io/velero/pull/10678) — velero-io/velero
- [#10624 Fix backup dequeued twice from a stale cached Queued copy](https://github.com/velero-io/velero/pull/10624) — velero-io/velero
- [#91 Update assignee settings](https://github.com/velero-io/velero-plugin-example/pull/91) — velero-io/velero-plugin-example
- [#10742 Remove qiuming-best from OWNERS of PROW action](https://github.com/velero-io/velero/pull/10742) — velero-io/velero
- [#10680 e2e: run the Kibishii file system backup cases on kind under CSI](https://github.com/velero-io/velero/pull/10680) — velero-io/velero
- [#10673 Recognize GCS object-not-found error during backup deletion](https://github.com/velero-io/velero/pull/10673) — velero-io/velero
- [#10682 [release-1.18] Bump Golang to 1.26.10 and golang.org/x/net to v0.61.0 to fix CVEs](https://github.com/velero-io/velero/pull/10682) — velero-io/velero
- [#10679 e2e: give the namespace-mapping cases real volumes on kind under CSI](https://github.com/velero-io/velero/pull/10679) — velero-io/velero
- [#10685 docs: fix Kubernetes version check for volume group snapshots](https://github.com/velero-io/velero/pull/10685) — velero-io/velero
- [#10697 build(deps): bump github/codeql-action from 4.38.3 to 4.39.1 in the github-actions group](https://github.com/velero-io/velero/pull/10697) — velero-io/velero
- [#10385 refactor: propagate context.Context in core kube secrets and namespace utilities](https://github.com/velero-io/velero/pull/10385) — velero-io/velero

**openshift** (29)
- [#2527 Bug: fix CreateNamespace race when namespace is Terminating](https://github.com/openshift/oadp-operator/pull/2527) — openshift/oadp-operator
- [#163 Merge https://github.com/velero-io/velero-plugin-for-gcp:main (1e7b956) into oadp-dev](https://github.com/openshift/velero-plugin-for-gcp/pull/163) — openshift/velero-plugin-for-gcp
- [#135 Migrate konflux.Dockerfile from brew to registry.redhat.io Go 1.26 builder](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/135) — openshift/velero-plugin-for-legacy-aws
- [#126 Add akarol and PrasadJoshi12 to OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/126) — openshift/velero-plugin-for-legacy-aws
- [#183 Add akarol to OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/183) — openshift/velero-plugin-for-aws
- [#2526 docs: add progress reporting section to kubevirt-datamover backup-restore guide](https://github.com/openshift/oadp-operator/pull/2526) — openshift/oadp-operator
- [#80 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/80) — openshift/velero-plugin-for-legacy-aws
- [#2493 OADP-8924: Add HCP guest cluster pod backup test case](https://github.com/openshift/oadp-operator/pull/2493) — openshift/oadp-operator
- [#331 NO-JIRA: Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity from 1.14.0 to 1.15.0 in the azure-github-dependencies group](https://github.com/openshift/hypershift-oadp-plugin/pull/331) — openshift/hypershift-oadp-plugin
- [#2488 Enable AllNamespaces install mode with multi-tenant DPA support](https://github.com/openshift/oadp-operator/pull/2488) — openshift/oadp-operator
- [#2521 Add hotfix image creation guide for development docs](https://github.com/openshift/oadp-operator/pull/2521) — openshift/oadp-operator
- [#603 Migrate konflux.Dockerfile from brew to registry.redhat.io Go 1.26 builder](https://github.com/openshift/velero/pull/603) — openshift/velero
- [#505 [oadp-1.4] Add comprehensive test coverage for restore plugins](https://github.com/openshift/openshift-velero-plugin/pull/505) — openshift/openshift-velero-plugin
- [#329 NO-JIRA: Bump the github-dependencies group across 1 directory with 3 updates](https://github.com/openshift/hypershift-oadp-plugin/pull/329) — openshift/hypershift-oadp-plugin
- [#593 Backport: Add ConfigMap support for keepLatestMaintenanceJobs (oadp-1.5)](https://github.com/openshift/velero/pull/593) — openshift/velero
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

**migtools** (16)
- [#190 Bump go.opentelemetry.io/otel/sdk from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/190) — migtools/udistribution
- [#189 Bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/189) — migtools/udistribution
- [#288 Migrate konflux.Dockerfile from brew to registry.redhat.io Go 1.26 builder](https://github.com/migtools/oadp-cli/pull/288) — migtools/oadp-cli
- [#251 Migrate konflux.Dockerfile from brew to registry.redhat.io Go 1.26 builder](https://github.com/migtools/kubevirt-datamover-controller/pull/251) — migtools/kubevirt-datamover-controller
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
- [#50 chore(deps-dev): bump vite from 8.0.16 to 8.1.6 in /frontend](https://github.com/migtools/filebrowser/pull/50) — migtools/filebrowser
- [#103 Add akarol to OWNERS](https://github.com/migtools/kubevirt-velero-plugin/pull/103) — migtools/kubevirt-velero-plugin

**Other** (3)
- [#23732 fix(web): PDF previews keep their page when the agent responds](https://github.com/pingdotgg/t3code/pull/23732) — pingdotgg/t3code
- [#23510 fix(clients): later image reads show updated file contents](https://github.com/pingdotgg/t3code/pull/23510) — pingdotgg/t3code
- [#208 Refresh dashboard CVE data when a fix PR merges](https://github.com/oadp-rebasebot/oadp-rebase/pull/208) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (100)

**velero-io** (55)
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10018 Discussion: rely on CODEOWNERS instead of necojackarc/auto-request-review across velero-io repos](https://github.com/velero-io/velero/issues/10018) — velero-io/velero
- [#10026 Restore logs endless watch errors for API groups without watch support (e.g. authorization.openshift.io)](https://github.com/velero-io/velero/issues/10026) — velero-io/velero
- [#10078 CI to check doc compliance with code change](https://github.com/velero-io/velero/issues/10078) — velero-io/velero
- [#10675 E2E: Kibishii cases reachable on kind with CSI but never run there](https://github.com/velero-io/velero/issues/10675) — velero-io/velero
- [#9650 Restore fails when Service last-applied-configuration has "healthCheckNodePort": null](https://github.com/velero-io/velero/issues/9650) — velero-io/velero
- [#10730 DataDownload waiting for a WaitForFirstConsumer target PVC blocks the node-agent DataDownload controller (deadlock with Immediate PVCs in the same pod)](https://github.com/velero-io/velero/issues/10730) — velero-io/velero
- [#10694 E2E: verify retained data mover snapshots are deleted from the storage on backup deletion (kind CSI job)](https://github.com/velero-io/velero/issues/10694) — velero-io/velero
- [#10483 [CSI][Async Backup] Progress() treats retryable VolumeSnapshotContent errors as terminal, failing backups the snapshot controller was about to retry](https://github.com/velero-io/velero/issues/10483) — velero-io/velero
- [#7804 Enhancing Velero Schedule with RetainDays and RetainCount for Backup Retention Management.](https://github.com/velero-io/velero/issues/7804) — velero-io/velero
- [#8401 Issue with Velero Restore : Azure disk PV Created with Old SKU Despite Updated Storage Class](https://github.com/velero-io/velero/issues/8401) — velero-io/velero
- [#9866 Kopia Repository Folder Not Cleaned Up from MinIO After Backup Deletion and Full Maintenance](https://github.com/velero-io/velero/issues/9866) — velero-io/velero
- [#7760 Metrics for backup repository maintenance job](https://github.com/velero-io/velero/issues/7760) — velero-io/velero
- [#8535 Repo maintenance - don't run backup/restore if repo maintenance fails in a row](https://github.com/velero-io/velero/issues/8535) — velero-io/velero
- [#7858 Backup en AWS Outposts ](https://github.com/velero-io/velero/issues/7858) — velero-io/velero
- [#4169 velero Restic restore aws efs Error](https://github.com/velero-io/velero/issues/4169) — velero-io/velero
- [#5232 AWS EBS restore should use the KMS key specified in the storage class](https://github.com/velero-io/velero/issues/5232) — velero-io/velero
- [#9396 Velero cannot detect CSI driver ebs.csi.eks.amazonaws.com on EKS Auto Mode](https://github.com/velero-io/velero/issues/9396) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#10693 Block data mover: backup deletion does not delete retained volume snapshots (design Volume Snapshot Retention L370-371, L474 not implemented)](https://github.com/velero-io/velero/issues/10693) — velero-io/velero
- [#10092 Deprecate the block volume backup/restore functionality through Kopia file system uploader](https://github.com/velero-io/velero/issues/10092) — velero-io/velero
- [#10120 Enhancement: Fail-fast in `velero install --wait` on Deployment ReplicaFailure](https://github.com/velero-io/velero/issues/10120) — velero-io/velero
- [#10310 Include the errors/warnings from node-agent and data-mover pods in the velero backup/restore get/describe commands](https://github.com/velero-io/velero/issues/10310) — velero-io/velero
- [#8689 Report Object Lock when PutObject errors patching backup to Completed, and Fail backup](https://github.com/velero-io/velero/issues/8689) — velero-io/velero
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

**openshift** (4)
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#439 Image stream backup: Azure Workload Identity (WIF) not supported in registry env var wiring](https://github.com/openshift/openshift-velero-plugin/issues/439) — openshift/openshift-velero-plugin
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator

**migtools** (2)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#14 Handle guest agent connectivity and SkipQuiesce for VirtualMachineBackup](https://github.com/migtools/kubevirt-datamover-controller/issues/14) — migtools/kubevirt-datamover-controller

**Other** (39)
- [#5342 baseRelDir cannot be set to false in new netlify sites or change to true from older sites](https://github.com/netlify/build/issues/5342) — netlify/build
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#17531 Claude provider hangs on Bash calls when a UI-dependent Claude Code mod (e.g. blast-radius) is installed](https://github.com/pingdotgg/t3code/issues/17531) — pingdotgg/t3code
- [#2524 Clarify that pull_request_review_write create without event creates a pending review](https://github.com/github/github-mcp-server/issues/2524) — github/github-mcp-server
- [#2525 `pull_request_review_write` combines create/submit/delete into one tool, making fine-grained permissions by method impossible](https://github.com/github/github-mcp-server/issues/2525) — github/github-mcp-server
- [#10553 [Bug]: File links in agent output always resolve against the thread's project, not the repo the file is in](https://github.com/pingdotgg/t3code/issues/10553) — pingdotgg/t3code
- [#17655 [Bug]: Composer: can't insert a second slash-command skill on the same line (needs Shift+Return)](https://github.com/pingdotgg/t3code/issues/17655) — pingdotgg/t3code
- [#17422 [Bug]: Mobile composer stops saving typed text, so the send button stays disabled until the app restarts](https://github.com/pingdotgg/t3code/issues/17422) — pingdotgg/t3code
- [#6679 rbd: Filesystem volume mounted without SELinux `context=` although CSIDriver sets `seLinuxMount: true`; non-root pods get EACCES (`unlabeled_t`)](https://github.com/ceph/ceph-csi/issues/6679) — ceph/ceph-csi
- [#909 [Bug]: Orphaned Python/Docker processes after closing MCP clients/agents](https://github.com/sooperset/mcp-atlassian/issues/909) — sooperset/mcp-atlassian
- [#4673 v1beta1 HyperConverged apply fails with conversion webhook error right after the CSV reaches Succeeded](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4673) — kubevirt/hyperconverged-cluster-operator
- [#19736 [Bug]: A message queued behind a running turn pushes the "Working for…" header below it](https://github.com/pingdotgg/t3code/issues/19736) — pingdotgg/t3code
- [#16000 [Bug]: Runtime-mode, instance and worktree changes detach the Claude session and kill live subagents without the background-work check](https://github.com/pingdotgg/t3code/issues/16000) — pingdotgg/t3code
- [#17875 VEP#25 Enhancement: Incremental VirtualMachineBackup delta is always relative to VirtualMachineBackupTracker.status.latestCheckpoint only (no arbitrary base checkpoint)](https://github.com/kubevirt/kubevirt/issues/17875) — kubevirt/kubevirt
- [#1419 `kubectl explain -o md`](https://github.com/kubernetes/kubectl/issues/1419) — kubernetes/kubectl
- [#26598 Support `strategy.matrix` on the `agent` job for parallel AI execution](https://github.com/github/gh-aw/issues/26598) — github/gh-aw
- [#956 [Feature Request] Lock Bolt BLE: read-only protocol paths (realtime status, door state, history, settings read-back)](https://github.com/SecKatie/ha-wyzeapi/issues/956) — SecKatie/ha-wyzeapi
- [#502 Enhancement: Allow combining `run_if_changed` and `skip_if_only_changed` for more flexible job triggering](https://github.com/kubernetes-sigs/prow/issues/502) — kubernetes-sigs/prow
- [#17508 [Bug]: Antigravity Google sign-in hides the real failure reason (ineligible account, rejected redirect URL)](https://github.com/pingdotgg/t3code/issues/17508) — pingdotgg/t3code
- [#134 `tide` not honoring multiple reviewer branch protection](https://github.com/kubernetes-sigs/prow/issues/134) — kubernetes-sigs/prow
- [#16992 [Bug]: Jira MCP Apps render blank inline cards despite successful tool results](https://github.com/pingdotgg/t3code/issues/16992) — pingdotgg/t3code
- [#245 Package errors looking for new maintainers](https://github.com/pkg/errors/issues/245) — pkg/errors
- [#438 Add regex support for branch matching in Tide status controller](https://github.com/kubernetes-sigs/prow/issues/438) — kubernetes-sigs/prow
- [#3314 CSI Differential Snapshot for Block Volumes](https://github.com/kubernetes/enhancements/issues/3314) — kubernetes/enhancements
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
## Issues Closed (87)

**velero-io** (26)
- [#10724 Block data mover pods OOMKilled: async write burst scales with node CPUs, no Go memory limit](https://github.com/velero-io/velero/issues/10724) — velero-io/velero
- [#10721 Regression: backup deletion fails for good after an interrupted deletion (kopia snapshot not found after repo refresh)](https://github.com/velero-io/velero/issues/10721) — velero-io/velero
- [#10719 Block data mover restore skips zero ranges: BLKZEROOUT ioctl number is wrong](https://github.com/velero-io/velero/issues/10719) — velero-io/velero
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
- [#10300 Unified repo config dir resolves to unwritable /udmrepo when HOME=/ (arbitrary-UID / OpenShift non-root server)](https://github.com/velero-io/velero/issues/10300) — velero-io/velero
- [#10301 Dead code in repository maintenance: GenOptionMaintainMode/Full/Quick and overwrite*MaintainInterval are unreachable](https://github.com/velero-io/velero/issues/10301) — velero-io/velero
- [#10304 Block data mover: retained CBT base snapshots are never reclaimed at backup deletion (design L370-371/L474 unimplemented)](https://github.com/velero-io/velero/issues/10304) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#10046 fs-backup restore deadlocks at Init:0/1 on owner-restricted volumes — restore-wait init container ignores pod-level securityContext, falls back to hardcoded runAsUser 1000](https://github.com/velero-io/velero/issues/10046) — velero-io/velero
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#10099 Update velero.io community pages](https://github.com/velero-io/velero/issues/10099) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero

**openshift** (15)
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

**Other** (28)
- [#23825 [Bug]: Deferred MCP App forms never display; write tool returns awaiting_user_submission with no fallback](https://github.com/pingdotgg/t3code/issues/23825) — pingdotgg/t3code
- [#17531 Claude provider hangs on Bash calls when a UI-dependent Claude Code mod (e.g. blast-radius) is installed](https://github.com/pingdotgg/t3code/issues/17531) — pingdotgg/t3code
- [#90071 Model reimplements ad-hoc polling scripts instead of using an available, more specific installed skill](https://github.com/anthropics/claude-code/issues/90071) — anthropics/claude-code
- [#6679 rbd: Filesystem volume mounted without SELinux `context=` although CSIDriver sets `seLinuxMount: true`; non-root pods get EACCES (`unlabeled_t`)](https://github.com/ceph/ceph-csi/issues/6679) — ceph/ceph-csi
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
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
