# Activity Log

> **Period:** 2026-08-17 — 2026-08-31
> **Generated:** 2026-08-31 23:09:39 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 49 |
| PRs Opened | 54 |
| PRs Reviewed | 64 |
| Issues/PRs Commented | 51 |
| Issues Closed | 20 |

---

## PRs Merged (49)

**velero-io** (12)
- [#10406 release-1.17: validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10406) — velero-io/velero
- [#10381 1.18: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10381) — velero-io/velero
- [#10348 1.18: Backport #10342: Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10348) — velero-io/velero
- [#10407 1.18: Cherry-pick #10390: Validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10407) — velero-io/velero
- [#10409 Update community meeting links to LFX Zoom, add calendar](https://github.com/velero-io/velero/pull/10409) — velero-io/velero
- [#10309 Report a measured zero incremental instead of erasing it](https://github.com/velero-io/velero/pull/10309) — velero-io/velero
- [#10390 Skip kind e2e matrix entries for kindest/node tags with missing manifests](https://github.com/velero-io/velero/pull/10390) — velero-io/velero
- [#10389 Support `/backport 1.17` shorthand and auto-fix changelog filename in backport PRs](https://github.com/velero-io/velero/pull/10389) — velero-io/velero
- [#10034 chore: pin helm/kind-action to commit with curl retry fix](https://github.com/velero-io/velero/pull/10034) — velero-io/velero
- [#9795 Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/9795) — velero-io/velero
- [#10305 Log the discovered parent snapshot ID, not the empty lookup parameter](https://github.com/velero-io/velero/pull/10305) — velero-io/velero
- [#10308 Detect block uploader cancellation through wrapped errors](https://github.com/velero-io/velero/pull/10308) — velero-io/velero

**openshift** (21)
- [#2139 OADP-7665: Pass --log-level to NodeAgent DaemonSet container args](https://github.com/openshift/oadp-operator/pull/2139) — openshift/oadp-operator
- [#2019 Add uploader-type argument to Velero deployment configuration when configuration.args is used.](https://github.com/openshift/oadp-operator/pull/2019) — openshift/oadp-operator
- [#2368 [oadp-1.4] Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2368) — openshift/oadp-operator
- [#2205 OADP-7943: Fix DPA annotation changes not triggering reconciliation](https://github.com/openshift/oadp-operator/pull/2205) — openshift/oadp-operator
- [#2367 Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2367) — openshift/oadp-operator
- [#84048 oadp-analyze-e2e-failure: give Claude explicit source-clone instructions](https://github.com/openshift/release/pull/84048) — openshift/release
- [#2406 [OADP-8716] Pin MCE to stable-2.8 only below OCP 4.19, matching HCP target env](https://github.com/openshift/oadp-operator/pull/2406) — openshift/oadp-operator
- [#84043 Retry operator-sdk run bundle on transient opm pull failures](https://github.com/openshift/release/pull/84043) — openshift/release
- [#83957 oadp-operator: migrate e2e Claude failure analysis to claude-ai-helpers post-step](https://github.com/openshift/release/pull/83957) — openshift/release
- [#2409 [oadp-1.6] Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2409) — openshift/oadp-operator
- [#2411 [oadp-1.4] Add --ginkgo.junit-report flag to test-e2e target](https://github.com/openshift/oadp-operator/pull/2411) — openshift/oadp-operator
- [#2408 Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2408) — openshift/oadp-operator
- [#83833 Rename KDM e2e job to virt-kdm, fix operator-sdk-bundle-image step bugs](https://github.com/openshift/release/pull/83833) — openshift/release
- [#2373 fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2373) — openshift/oadp-operator
- [#2375 [oadp-1.5] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2375) — openshift/oadp-operator
- [#2374 [oadp-1.6] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2374) — openshift/oadp-operator
- [#83341 ci-tools: bump bin build memory request to 3Gi](https://github.com/openshift/release/pull/83341) — openshift/release
- [#83049 Run oadp-operator e2e against kdm-controller/kdm-plugin PRs (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83049) — openshift/release
- [#83221 gather-must-gather: retry camgi download, don't fail gather on it](https://github.com/openshift/release/pull/83221) — openshift/release
- [#2350 Add e2e coverage for kubevirt-datamover VM backup/restore: multi-PVC, incremental sequence, and CBT restore (+ max-concurrent-data-movers config)](https://github.com/openshift/oadp-operator/pull/2350) — openshift/oadp-operator
- [#83299 gather-extra: harden against oc timeouts/flakes; jq to ARTIFACT_DIR](https://github.com/openshift/release/pull/83299) — openshift/release

**migtools** (11)
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller
- [#50 Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/50) — migtools/kubevirt-datamover-plugin
- [#199 fix: honor matchLabels selector on restore target PVC instead of failing](https://github.com/migtools/kubevirt-datamover-controller/pull/199) — migtools/kubevirt-datamover-controller
- [#200 test: pin that a same-restore-name incomplete sibling still blocks the VM flip](https://github.com/migtools/kubevirt-datamover-controller/pull/200) — migtools/kubevirt-datamover-controller
- [#197 fix: work PVC must be ReadWriteOnce, not the target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/pull/197) — migtools/kubevirt-datamover-controller
- [#182 fix: use %s format verb for cmp.Diff in t.Errorf calls](https://github.com/migtools/udistribution/pull/182) — migtools/udistribution
- [#47 Address declined CodeRabbit follow-ups from PR #41, add missing unit test coverage](https://github.com/migtools/kubevirt-datamover-plugin/pull/47) — migtools/kubevirt-datamover-plugin
- [#187 feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/187) — migtools/kubevirt-datamover-controller
- [#186 feat: DD concurrency limiter (#175), scratch PVC hardening, multi-disk isolation test (issue #73 Phase 4)](https://github.com/migtools/kubevirt-datamover-controller/pull/186) — migtools/kubevirt-datamover-controller

**Other** (5)
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
- [#170 Add Velero backport button for velero-io/velero](https://github.com/kaovilai/github-bot-command-palette/pull/170) — kaovilai/github-bot-command-palette
- [#1 feat: multi-arch builds via comma-separated --platform and automatic QEMU builder for non-native architectures](https://github.com/kaovilai/socktainer/pull/1) — kaovilai/socktainer
- [#2 feat(libpod): Add Podman /libpod/* API endpoints](https://github.com/kaovilai/socktainer/pull/2) — kaovilai/socktainer
- [#1 Make pdf2text-ocr an installable, colorful, foldable-friendly PWA with progress, print, and page navigation](https://github.com/kaovilai/pdf2text-pwa/pull/1) — kaovilai/pdf2text-pwa
## PRs Opened (54)

**velero-io** (20)
- [#10428 [release-1.14] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10428) — velero-io/velero
- [#10427 [release-1.15] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10427) — velero-io/velero
- [#10426 [release-1.18] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10426) — velero-io/velero
- [#10425 [release-1.17] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10425) — velero-io/velero
- [#10424 [release-1.16] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10424) — velero-io/velero
- [#10423 [release-1.16] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/velero-io/velero/pull/10423) — velero-io/velero
- [#10416 Fix re-request-review workflow token permissions for fork-originated PRs](https://github.com/velero-io/velero/pull/10416) — velero-io/velero
- [#10409 Update community meeting links to LFX Zoom, add calendar](https://github.com/velero-io/velero/pull/10409) — velero-io/velero
- [#10407 1.18: Cherry-pick #10390: Validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10407) — velero-io/velero
- [#10406 release-1.17: validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10406) — velero-io/velero
- [#10403 Check both daemonsets before returning non-NotFound lookup error in IsReady](https://github.com/velero-io/velero/pull/10403) — velero-io/velero
- [#10401 Fix e2e build-artifact handoff race (velero.tar missing after force-push)](https://github.com/velero-io/velero/pull/10401) — velero-io/velero
- [#10399 [Backport release-1.17] Fix e2e kind matrix misparsing pre-release node tags](https://github.com/velero-io/velero/pull/10399) — velero-io/velero
- [#10390 Skip kind e2e matrix entries for kindest/node tags with missing manifests](https://github.com/velero-io/velero/pull/10390) — velero-io/velero
- [#10389 Support `/backport 1.17` shorthand and auto-fix changelog filename in backport PRs](https://github.com/velero-io/velero/pull/10389) — velero-io/velero
- [#10382 1.17: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10382) — velero-io/velero
- [#10381 1.18: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10381) — velero-io/velero
- [#10348 1.18: Backport #10342: Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10348) — velero-io/velero
- [#10327 Detect data path pod deletion via informer DeleteFunc](https://github.com/velero-io/velero/pull/10327) — velero-io/velero
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero

**openshift** (14)
- [#2423 fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2423) — openshift/oadp-operator
- [#84229 oadp-operator: bump e2e-test-kubevirt-aws timeout to 3h](https://github.com/openshift/release/pull/84229) — openshift/release
- [#84228 Add Depends-On cross-repo image build for KDM and oadp-operator e2e jobs](https://github.com/openshift/release/pull/84228) — openshift/release
- [#565 OADP-7061: [oadp-1.5] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/openshift/velero/pull/565) — openshift/velero
- [#84048 oadp-analyze-e2e-failure: give Claude explicit source-clone instructions](https://github.com/openshift/release/pull/84048) — openshift/release
- [#84043 Retry operator-sdk run bundle on transient opm pull failures](https://github.com/openshift/release/pull/84043) — openshift/release
- [#2411 [oadp-1.4] Add --ginkgo.junit-report flag to test-e2e target](https://github.com/openshift/oadp-operator/pull/2411) — openshift/oadp-operator
- [#2409 [oadp-1.6] Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2409) — openshift/oadp-operator
- [#2408 Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2408) — openshift/oadp-operator
- [#83957 oadp-operator: migrate e2e Claude failure analysis to claude-ai-helpers post-step](https://github.com/openshift/release/pull/83957) — openshift/release
- [#2406 [OADP-8716] Pin MCE to stable-2.8 only below OCP 4.19, matching HCP target env](https://github.com/openshift/oadp-operator/pull/2406) — openshift/oadp-operator
- [#2404 test: unpend two kdm restore PIts, fixing bugs found via live e2e validation](https://github.com/openshift/oadp-operator/pull/2404) — openshift/oadp-operator
- [#2402 Unpend two kdm restore e2e tests now that phase 4 landed](https://github.com/openshift/oadp-operator/pull/2402) — openshift/oadp-operator
- [#83833 Rename KDM e2e job to virt-kdm, fix operator-sdk-bundle-image step bugs](https://github.com/openshift/release/pull/83833) — openshift/release

**migtools** (11)
- [#213 fix: speed up Dockerfile builds with cache mounts](https://github.com/migtools/kubevirt-datamover-controller/pull/213) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller
- [#206 fix: retry expected-backup-type annotation on conflict instead of giving up](https://github.com/migtools/kubevirt-datamover-controller/pull/206) — migtools/kubevirt-datamover-controller
- [#200 test: pin that a same-restore-name incomplete sibling still blocks the VM flip](https://github.com/migtools/kubevirt-datamover-controller/pull/200) — migtools/kubevirt-datamover-controller
- [#50 Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/50) — migtools/kubevirt-datamover-plugin
- [#199 fix: honor matchLabels selector on restore target PVC instead of failing](https://github.com/migtools/kubevirt-datamover-controller/pull/199) — migtools/kubevirt-datamover-controller
- [#197 fix: work PVC must be ReadWriteOnce, not the target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/pull/197) — migtools/kubevirt-datamover-controller
- [#195 fix: name root cause in restore PVC-conflict error messages](https://github.com/migtools/kubevirt-datamover-controller/pull/195) — migtools/kubevirt-datamover-controller
- [#182 fix: use %s format verb for cmp.Diff in t.Errorf calls](https://github.com/migtools/udistribution/pull/182) — migtools/udistribution

**Other** (9)
- [#4552 Fix conversion webhook crash on legacy featureGates empty-object shape](https://github.com/kubevirt/hyperconverged-cluster-operator/pull/4552) — kubevirt/hyperconverged-cluster-operator
- [#18957 storage/cbt: fix stale reconcile overwriting a completed VMBackup with SourceLost](https://github.com/kubevirt/kubevirt/pull/18957) — kubevirt/kubevirt
- [#18949 storage/cbt: fix VMBackup status freeze during target PVC attach](https://github.com/kubevirt/kubevirt/pull/18949) — kubevirt/kubevirt
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
- [#170 Add Velero backport button for velero-io/velero](https://github.com/kaovilai/github-bot-command-palette/pull/170) — kaovilai/github-bot-command-palette
- [#375 feat(libpod): add Podman /libpod/* API, manifest lists, and multi-arch build support](https://github.com/socktainer/socktainer/pull/375) — socktainer/socktainer
- [#1 Make pdf2text-ocr an installable, colorful, foldable-friendly PWA with progress, print, and page navigation](https://github.com/kaovilai/pdf2text-pwa/pull/1) — kaovilai/pdf2text-pwa
- [#13882 macos: add regression test for double-click rename after dragging tab…](https://github.com/ghostty-org/ghostty/pull/13882) — ghostty-org/ghostty
- [#13881 macos: add regression test for double-click rename after dragging tab between windows](https://github.com/ghostty-org/ghostty/pull/13881) — ghostty-org/ghostty
## PRs Reviewed (64)

**velero-io** (29)
- [#10449 Fix snapshot-location get --selector flag to actually filter VolumeSnapshotLocations by label](https://github.com/velero-io/velero/pull/10449) — velero-io/velero
- [#10438 Issue #10437: derive velero server's graceful shutdown timeout from terminationGracePeriodSeconds](https://github.com/velero-io/velero/pull/10438) — velero-io/velero
- [#10436 Add block data mover support for Velero backup/restore describe CLI.](https://github.com/velero-io/velero/pull/10436) — velero-io/velero
- [#10447 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10447) — velero-io/velero
- [#10421 Add "IncrementalBytes" field to status of DataDownload and PVR to indicate data transfered by the incremental restore](https://github.com/velero-io/velero/pull/10421) — velero-io/velero
- [#10372 Show validation frequency in backup-location get output](https://github.com/velero-io/velero/pull/10372) — velero-io/velero
- [#10393 [Backport release-1.17] fix(restore_finalizer): bound WaitRestoreExecHook poll with resourceT…](https://github.com/velero-io/velero/pull/10393) — velero-io/velero
- [#10353 Reject velero backup delete when BSL is read-only](https://github.com/velero-io/velero/pull/10353) — velero-io/velero
- [#10405 [Backport release-1.18] Fix node agent readiness check issue](https://github.com/velero-io/velero/pull/10405) — velero-io/velero
- [#10360 [cherry-pick release-1.18] Fast-fail backup when built-in data mover has no running node-agent](https://github.com/velero-io/velero/pull/10360) — velero-io/velero
- [#10397 Fix node agent rediness check issue](https://github.com/velero-io/velero/pull/10397) — velero-io/velero
- [#10356 Add volumeName condition to VolumePolicy resource filtering](https://github.com/velero-io/velero/pull/10356) — velero-io/velero
- [#10354 Re-process InProgress DeleteBackupRequests on retry](https://github.com/velero-io/velero/pull/10354) — velero-io/velero
- [#10331 Preserve PVC selected-node annotation via carrier annotation for in-place restore](https://github.com/velero-io/velero/pull/10331) — velero-io/velero
- [#10366 Bump github/codeql-action from 4.37.6 to 4.37.7 in the github-actions group](https://github.com/velero-io/velero/pull/10366) — velero-io/velero
- [#10387 [Backport release-1.18] Avoid io.ReadAll in buildFinalTarball()](https://github.com/velero-io/velero/pull/10387) — velero-io/velero
- [#10388 [Backport release-1.17] Avoid io.ReadAll in buildFinalTarball()](https://github.com/velero-io/velero/pull/10388) — velero-io/velero
- [#10329 Embed CRD manifests via go:embed instead of codegen](https://github.com/velero-io/velero/pull/10329) — velero-io/velero
- [#10359 Fix e2e kind matrix misparsing pre-release node tags](https://github.com/velero-io/velero/pull/10359) — velero-io/velero
- [#10346 Double check the label for backup when deleting VSC](https://github.com/velero-io/velero/pull/10346) — velero-io/velero
- [#10315 Testing: Implement missing unit tests for pkg/backup/snapshots.go](https://github.com/velero-io/velero/pull/10315) — velero-io/velero
- [#10342 Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10342) — velero-io/velero
- [#10337 Document secretNames/configMapNames for backup/restore PVC config](https://github.com/velero-io/velero/pull/10337) — velero-io/velero
- [#10347 1.18: Only sync finished backups from object storage](https://github.com/velero-io/velero/pull/10347) — velero-io/velero
- [#10335 [release-1.18] Support copying namespace-scoped secrets/configmaps for backup and restore PVC provisioning](https://github.com/velero-io/velero/pull/10335) — velero-io/velero
- [#10322 Issue 10321: fill the error to the corresponding CR when data mover pod is evicted](https://github.com/velero-io/velero/pull/10322) — velero-io/velero
- [#10319 [cherry-pick][1.18] Remove PVC and PV inclusion check during creating PVR.](https://github.com/velero-io/velero/pull/10319) — velero-io/velero
- [#10317 Cleanup: Remove deprecated --wait flag from velero uninstall](https://github.com/velero-io/velero/pull/10317) — velero-io/velero
- [#10312 assert expected errors from the test case rather than the returned error](https://github.com/velero-io/velero/pull/10312) — velero-io/velero

**openshift** (21)
- [#2422 [oadp-1.6] e2e: add cacert tests using in-cluster minio with TLS](https://github.com/openshift/oadp-operator/pull/2422) — openshift/oadp-operator
- [#2395 e2e: add cacert tests using in-cluster minio with TLS](https://github.com/openshift/oadp-operator/pull/2395) — openshift/oadp-operator
- [#2405 feat: Add NetworkPolicy support for OADP operands (OADP-6074)](https://github.com/openshift/oadp-operator/pull/2405) — openshift/oadp-operator
- [#2397 [OADP-8704] fix: only set region in BSL config for AWS CloudStorage](https://github.com/openshift/oadp-operator/pull/2397) — openshift/oadp-operator
- [#2415 [oadp-1.5] Add uploader-type argument to Velero deployment configuration when configuration.args is used.](https://github.com/openshift/oadp-operator/pull/2415) — openshift/oadp-operator
- [#2412 [oadp-1.6] [OADP-8716] Pin MCE to stable-2.8 only below OCP 4.19, matching HCP target env](https://github.com/openshift/oadp-operator/pull/2412) — openshift/oadp-operator
- [#163 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.14.1 (96a651c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-aws/pull/163) — openshift/velero-plugin-for-aws
- [#165 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.1 (6902b36) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/165) — openshift/velero-plugin-for-gcp
- [#164 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.12.2 (c25b809) into oadp-1.5](https://github.com/openshift/velero-plugin-for-gcp/pull/164) — openshift/velero-plugin-for-gcp
- [#163 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.12.2 (bef8467) into oadp-1.5](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/163) — openshift/velero-plugin-for-microsoft-azure
- [#2398 docs: add KubeVirt DataMover user-facing documentation](https://github.com/openshift/oadp-operator/pull/2398) — openshift/oadp-operator
- [#464 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.5 (84ccff9) into oadp-1.5](https://github.com/openshift/openshift-velero-plugin/pull/464) — openshift/openshift-velero-plugin
- [#304 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (538be00) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/304) — openshift/hypershift-oadp-plugin
- [#162 Merge https://github.com/openshift/oadp-must-gather:oadp-1.5 (1b098f8) into oadp-1.5](https://github.com/openshift/oadp-must-gather/pull/162) — openshift/oadp-must-gather
- [#163 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (6cfe3b2) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/163) — openshift/oadp-must-gather
- [#164 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.1 (6fb0379) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/164) — openshift/velero-plugin-for-microsoft-azure
- [#2390 Deprecate config.credentialsFile; translate to spec.credential](https://github.com/openshift/oadp-operator/pull/2390) — openshift/oadp-operator
- [#2393 [oadp-1.6] OADP-8548: PodResources unset fields should be output as "0" to fix parsing errors results in ignored resource settings](https://github.com/openshift/oadp-operator/pull/2393) — openshift/oadp-operator
- [#2396 [oadp-1.6] Add e2e coverage for kubevirt-datamover VM backup/restore: multi-PVC, incremental sequence, and CBT restore (+ max-concurrent-data-movers config)](https://github.com/openshift/oadp-operator/pull/2396) — openshift/oadp-operator
- [#2394 [OADP-8700] Guard NodeAgent.ExtraArgs access against nil when using restic config](https://github.com/openshift/oadp-operator/pull/2394) — openshift/oadp-operator
- [#162 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.12.2 (82b9141) into oadp-1.5](https://github.com/openshift/velero-plugin-for-aws/pull/162) — openshift/velero-plugin-for-aws

**migtools** (13)
- [#205 fix(#14): default SkipQuiesce=false, opt-in application-consistent backup](https://github.com/migtools/kubevirt-datamover-controller/pull/205) — migtools/kubevirt-datamover-controller
- [#214 [oadp-1.6] alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/214) — migtools/kubevirt-datamover-controller
- [#215 [oadp-1.6] fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/215) — migtools/kubevirt-datamover-controller
- [#216 [oadp-1.6] fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/216) — migtools/kubevirt-datamover-controller
- [#53 [oadp-1.6] Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/53) — migtools/kubevirt-datamover-plugin
- [#192 docs: add architecture and testing guides, refresh README](https://github.com/migtools/kubevirt-datamover-controller/pull/192) — migtools/kubevirt-datamover-controller
- [#181 Bump the go-dependencies group across 1 directory with 7 updates](https://github.com/migtools/udistribution/pull/181) — migtools/udistribution
- [#375 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (b85b84a) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/375) — migtools/oadp-non-admin
- [#49 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (9531d54) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/49) — migtools/kubevirt-datamover-plugin
- [#258 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (0aeee34) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/258) — migtools/oadp-cli
- [#100 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (2f3a322) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/100) — migtools/oadp-vm-file-restore
- [#190 [oadp-1.6] feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/190) — migtools/kubevirt-datamover-controller
- [#257 Merge https://github.com/migtools/oadp-cli:oadp-1.5 (f2cb269) into oadp-1.5](https://github.com/migtools/oadp-cli/pull/257) — migtools/oadp-cli

**Other** (1)
- [#3 fix: allow unrestricted egress for operator pod NetworkPolicy](https://github.com/shubham-pampattiwar/oadp-operator/pull/3) — shubham-pampattiwar/oadp-operator
## Issues/PRs Commented On (51)

**velero-io** (28)
- [#10437 `velero server`'s shutdown grace period is hardcoded to 30s, ignoring `terminationGracePeriodSeconds`](https://github.com/velero-io/velero/issues/10437) — velero-io/velero
- [#8263 Fatal: unable to open config file results in PartiallyFailed Backup](https://github.com/velero-io/velero/issues/8263) — velero-io/velero
- [#9318 Behavior of skip volume policy is strange/problematic](https://github.com/velero-io/velero/issues/9318) — velero-io/velero
- [#9453 DataUpload tasks stuck in Prepared phase for extended periods](https://github.com/velero-io/velero/issues/9453) — velero-io/velero
- [#10440 Cleanup: Resolve Ginkgo V2 and Gomega anti-patterns in test suite](https://github.com/velero-io/velero/issues/10440) — velero-io/velero
- [#9556 Block level backup/restore support](https://github.com/velero-io/velero/issues/9556) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#9656 Kopia maintenance fails with 'ciphertext too short: 0' after S3 quota-related write failures leave 0-byte blobs](https://github.com/velero-io/velero/issues/9656) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#9760 Allow Velero kubernetes objects to be backed up with If-None-Match bucket policies enabled.](https://github.com/velero-io/velero/issues/9760) — velero-io/velero
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#9603 Backport/Cherry-pick GitHub action](https://github.com/velero-io/velero/issues/9603) — velero-io/velero
- [#9839 CBT availability detection per volume](https://github.com/velero-io/velero/issues/9839) — velero-io/velero
- [#9833 Backup/restore describe for block data mover](https://github.com/velero-io/velero/issues/9833) — velero-io/velero
- [#9835 Backup deletion for block data mover](https://github.com/velero-io/velero/issues/9835) — velero-io/velero
- [#9894 Transition all project meetings to CNCF Zoom](https://github.com/velero-io/velero/issues/9894) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#9429 velero doesn't correctly handle an empty ProviderSnapshotID](https://github.com/velero-io/velero/issues/9429) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9744 Bug: Restore stuck in Finalizing phase indefinitely due to unbounded hook-tracker wait](https://github.com/velero-io/velero/issues/9744) — velero-io/velero
- [#10340 Bug: EphemeralContainers are missing from ServiceAccount token filtering in PodAction](https://github.com/velero-io/velero/issues/10340) — velero-io/velero
- [#8265 Provide S3 plugin that aims to support any S3 compatible object storage.](https://github.com/velero-io/velero/issues/8265) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero

**openshift** (6)
- [#2413 Poll: how to fix e2e-test-kubevirt-aws hitting the 2h Prow step timeout](https://github.com/openshift/oadp-operator/issues/2413) — openshift/oadp-operator
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#10590 GCP CAPI: bootstrap in master instance group causes worker ignition failure via ILB pinning](https://github.com/openshift/installer/issues/10590) — openshift/installer
- [#2391 Follow up: simplify and document PodResources defaulting](https://github.com/openshift/oadp-operator/issues/2391) — openshift/oadp-operator

**migtools** (5)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#84 Implement concurrent data mover limiter for DU and DD controllers](https://github.com/migtools/kubevirt-datamover-controller/issues/84) — migtools/kubevirt-datamover-controller
- [#175 Implement concurrency limiter for DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/175) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller

**Other** (12)
- [#1847 Include scrollback history in state restoration](https://github.com/ghostty-org/ghostty/issues/1847) — ghostty-org/ghostty
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#481 Support using a later patch release than what's in go.mod](https://github.com/actions/setup-go/issues/481) — actions/setup-go
- [#18963 VEP #25: Infer backup target StorageClass from source VM volumes](https://github.com/kubevirt/kubevirt/issues/18963) — kubevirt/kubevirt
- [#18959 VEP #25: CBT: completed VirtualMachineBackup can be overwritten with SourceLost due to a stale reconcile race](https://github.com/kubevirt/kubevirt/issues/18959) — kubevirt/kubevirt
- [#18950 VEP #25: CBT: VirtualMachineBackup status freezes indefinitely while target PVC attach is pending](https://github.com/kubevirt/kubevirt/issues/18950) — kubevirt/kubevirt
- [#378 ci on real hw](https://github.com/socktainer/socktainer/issues/378) — socktainer/socktainer
- [#43 Chrome Web Store listing reports location permission](https://github.com/rxliuli/redirector/issues/43) — rxliuli/redirector
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#201 feat: Add Podman libpod API endpoints for native podman CLI support](https://github.com/socktainer/socktainer/issues/201) — socktainer/socktainer
- [#101 UDP support](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
## Issues Closed (20)

**velero-io** (7)
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#10328 Stop committing generated config/crd/*/crds/crds.go; embed CRDs via go:embed at build time](https://github.com/velero-io/velero/issues/10328) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#10296 Cancelling a block data mover backup reports it as a failure — cancel sentinel compared with == against a wrapped error](https://github.com/velero-io/velero/issues/10296) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10300 Unified repo config dir resolves to unwritable /udmrepo when HOME=/ (arbitrary-UID / OpenShift non-root server)](https://github.com/velero-io/velero/issues/10300) — velero-io/velero
- [#10301 Dead code in repository maintenance: GenOptionMaintainMode/Full/Quick and overwrite*MaintainInterval are unreachable](https://github.com/velero-io/velero/issues/10301) — velero-io/velero

**openshift** (5)
- [#2384 e2e: add cacert tests](https://github.com/openshift/oadp-operator/issues/2384) — openshift/oadp-operator
- [#2410 oadp-1.4: test-e2e Makefile target doesn't generate junit_report.xml](https://github.com/openshift/oadp-operator/issues/2410) — openshift/oadp-operator
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#2383 Evaluate and migrate user-provided credentialsFile handling for Velero #10254](https://github.com/openshift/oadp-operator/issues/2383) — openshift/oadp-operator

**migtools** (5)
- [#211 DataUpload stuck forever: "VMBT already prepared but VMB not yet visible in cache, requeuing"](https://github.com/migtools/kubevirt-datamover-controller/issues/211) — migtools/kubevirt-datamover-controller
- [#198 Add regression test: ensureWorkPVC must force ReadWriteOnce regardless of target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/issues/198) — migtools/kubevirt-datamover-controller
- [#42 Follow-up: address CodeRabbit code-quality suggestions declined during PR #41 review](https://github.com/migtools/kubevirt-datamover-plugin/issues/42) — migtools/kubevirt-datamover-plugin
- [#130 Checkpoint chain integrity gaps not covered by #77 (corrupt-but-present objects, TOCTOU, memoization verdict-loss, index history wipe)](https://github.com/migtools/kubevirt-datamover-controller/issues/130) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller

**Other** (3)
- [#1623 jira_transition_issue's `comment` argument silently dropped on Jira Cloud (transition succeeds, comment never posts)](https://github.com/sooperset/mcp-atlassian/issues/1623) — sooperset/mcp-atlassian
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#625 Add pagination support for get_pull_request_diff to handle large PRs](https://github.com/github/github-mcp-server/issues/625) — github/github-mcp-server
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
