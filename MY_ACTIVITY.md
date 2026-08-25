# Activity Log

> **Period:** 2026-08-11 — 2026-08-25
> **Generated:** 2026-08-25 13:52:27 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 58 |
| PRs Opened | 89 |
| PRs Reviewed | 77 |
| Issues/PRs Commented | 53 |
| Issues Closed | 26 |

---

## PRs Merged (58)

**velero-io** (12)
- [#10034 chore: pin helm/kind-action to commit with curl retry fix](https://github.com/velero-io/velero/pull/10034) — velero-io/velero
- [#9795 Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/9795) — velero-io/velero
- [#10305 Log the discovered parent snapshot ID, not the empty lookup parameter](https://github.com/velero-io/velero/pull/10305) — velero-io/velero
- [#10308 Detect block uploader cancellation through wrapped errors](https://github.com/velero-io/velero/pull/10308) — velero-io/velero
- [#10262 [release-1.17] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10262) — velero-io/velero
- [#10263 [release-1.18] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10263) — velero-io/velero
- [#10220 Group Dependabot GitHub Actions updates](https://github.com/velero-io/velero/pull/10220) — velero-io/velero
- [#10211 backport: add pre-merge label-on-comment support; add copilot-instructions and auto-labeler for changelog exemptions](https://github.com/velero-io/velero/pull/10211) — velero-io/velero
- [#10222 1.18 Backport: correct typos in log messages and status strings (#10192)](https://github.com/velero-io/velero/pull/10222) — velero-io/velero
- [#10223 [release-1.17] Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10223) — velero-io/velero
- [#10221 1.17 Backport #10192: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10221) — velero-io/velero
- [#10224 1.18: Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10224) — velero-io/velero

**openshift** (20)
- [#83833 Rename KDM e2e job to virt-kdm, fix operator-sdk-bundle-image step bugs](https://github.com/openshift/release/pull/83833) — openshift/release
- [#2373 fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2373) — openshift/oadp-operator
- [#2375 [oadp-1.5] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2375) — openshift/oadp-operator
- [#2374 [oadp-1.6] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2374) — openshift/oadp-operator
- [#83341 ci-tools: bump bin build memory request to 3Gi](https://github.com/openshift/release/pull/83341) — openshift/release
- [#83049 Run oadp-operator e2e against kdm-controller/kdm-plugin PRs (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83049) — openshift/release
- [#83221 gather-must-gather: retry camgi download, don't fail gather on it](https://github.com/openshift/release/pull/83221) — openshift/release
- [#2350 Add e2e coverage for kubevirt-datamover VM backup/restore: multi-PVC, incremental sequence, and CBT restore (+ max-concurrent-data-movers config)](https://github.com/openshift/oadp-operator/pull/2350) — openshift/oadp-operator
- [#83299 gather-extra: harden against oc timeouts/flakes; jq to ARTIFACT_DIR](https://github.com/openshift/release/pull/83299) — openshift/release
- [#2358 [oadp-1.4] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2358) — openshift/oadp-operator
- [#2357 [oadp-1.5] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2357) — openshift/oadp-operator
- [#2376 [oadp-1.4] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2376) — openshift/oadp-operator
- [#5334 test/e2e: unpin optional-operators fixture from EOL ocp/4.6 integrated stream](https://github.com/openshift/ci-tools/pull/5334) — openshift/ci-tools
- [#83286 Prep oadp-1.4/1.5 with bundle promotion for future cross-repo e2e](https://github.com/openshift/release/pull/83286) — openshift/release
- [#83282 Promote oadp-operator bundle directly instead of a broken index](https://github.com/openshift/release/pull/83282) — openshift/release
- [#2241 OADP-4817, OADP-1945, OADP-641: Add AWS_CA_BUNDLE support for custom CA certificates in BSLs](https://github.com/openshift/oadp-operator/pull/2241) — openshift/oadp-operator
- [#5363 pkg/steps: retry network-unreachable builds, capture failed build logs](https://github.com/openshift/ci-tools/pull/5363) — openshift/ci-tools
- [#2206 OADP-7943: Fix DPA annotation changes not triggering reconciliation](https://github.com/openshift/oadp-operator/pull/2206) — openshift/oadp-operator
- [#2346 docs: add CI plugin image sync guidance to common.go](https://github.com/openshift/oadp-operator/pull/2346) — openshift/oadp-operator
- [#404 [oadp-1.5] OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/404) — openshift/openshift-velero-plugin

**migtools** (10)
- [#197 fix: work PVC must be ReadWriteOnce, not the target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/pull/197) — migtools/kubevirt-datamover-controller
- [#199 fix: honor matchLabels selector on restore target PVC instead of failing](https://github.com/migtools/kubevirt-datamover-controller/pull/199) — migtools/kubevirt-datamover-controller
- [#200 test: pin that a same-restore-name incomplete sibling still blocks the VM flip](https://github.com/migtools/kubevirt-datamover-controller/pull/200) — migtools/kubevirt-datamover-controller
- [#182 fix: use %s format verb for cmp.Diff in t.Errorf calls](https://github.com/migtools/udistribution/pull/182) — migtools/udistribution
- [#47 Address declined CodeRabbit follow-ups from PR #41, add missing unit test coverage](https://github.com/migtools/kubevirt-datamover-plugin/pull/47) — migtools/kubevirt-datamover-plugin
- [#187 feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/187) — migtools/kubevirt-datamover-controller
- [#186 feat: DD concurrency limiter (#175), scratch PVC hardening, multi-disk isolation test (issue #73 Phase 4)](https://github.com/migtools/kubevirt-datamover-controller/pull/186) — migtools/kubevirt-datamover-controller
- [#182 fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/182) — migtools/kubevirt-datamover-controller
- [#124 feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/124) — migtools/kubevirt-datamover-controller
- [#180 fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/180) — migtools/kubevirt-datamover-controller

**Other** (16)
- [#1 feat: multi-arch builds via comma-separated --platform and automatic QEMU builder for non-native architectures](https://github.com/kaovilai/socktainer/pull/1) — kaovilai/socktainer
- [#2 feat(libpod): Add Podman /libpod/* API endpoints](https://github.com/kaovilai/socktainer/pull/2) — kaovilai/socktainer
- [#1 Make pdf2text-ocr an installable, colorful, foldable-friendly PWA with progress, print, and page navigation](https://github.com/kaovilai/pdf2text-pwa/pull/1) — kaovilai/pdf2text-pwa
- [#576 feat(openshift): preflight-check EC release signatures, offer nightly-style bypass](https://github.com/kaovilai/dotfiles/pull/576) — kaovilai/dotfiles
- [#163 Refresh screenshots to reflect current profiles and rehearsal button](https://github.com/kaovilai/github-bot-command-palette/pull/163) — kaovilai/github-bot-command-palette
- [#162 Resolve rehearsal rerun job names from presubmit config, not comment scraping](https://github.com/kaovilai/github-bot-command-palette/pull/162) — kaovilai/github-bot-command-palette
- [#160 Skip /test on non-Prow checks, add optional Actions rerun](https://github.com/kaovilai/github-bot-command-palette/pull/160) — kaovilai/github-bot-command-palette
- [#159 Add ship skill for solo-repo commit-to-merge cycle](https://github.com/kaovilai/github-bot-command-palette/pull/159) — kaovilai/github-bot-command-palette
- [#158 Fix job picker status mismatching GitHub's real check state](https://github.com/kaovilai/github-bot-command-palette/pull/158) — kaovilai/github-bot-command-palette
- [#155 Fix detectTargetBranch resolving head branch instead of base](https://github.com/kaovilai/github-bot-command-palette/pull/155) — kaovilai/github-bot-command-palette
- [#187 Implementing recent review display feature](https://github.com/kaovilai/kaovilai.pw/pull/187) — kaovilai/kaovilai.pw
- [#183 Add review queue panel consuming reviewQueue data from open-prs.json](https://github.com/kaovilai/kaovilai.pw/pull/183) — kaovilai/kaovilai.pw
- [#72 Add reviewDecision, approvalCount, and requiredApprovals to open-prs.json reviewQueue](https://github.com/kaovilai/kaovilai/pull/72) — kaovilai/kaovilai
- [#23 Recompile stale daily-upstream-parity.lock.yml](https://github.com/kaovilai/oadp-ui/pull/23) — kaovilai/oadp-ui
- [#24 Fix Dependabot security alerts in yarn.lock](https://github.com/kaovilai/oadp-ui/pull/24) — kaovilai/oadp-ui
- [#20 Add `__mocks__/**` to allowed-files for upstream-parity agent](https://github.com/kaovilai/oadp-ui/pull/20) — kaovilai/oadp-ui
## PRs Opened (89)

**velero-io** (37)
- [#10399 [Backport release-1.17] Fix e2e kind matrix misparsing pre-release node tags](https://github.com/velero-io/velero/pull/10399) — velero-io/velero
- [#10390 Skip kind e2e matrix entries for kindest/node tags with missing manifests](https://github.com/velero-io/velero/pull/10390) — velero-io/velero
- [#10389 Support `/backport 1.17` shorthand and auto-fix changelog filename in backport PRs](https://github.com/velero-io/velero/pull/10389) — velero-io/velero
- [#10382 1.17: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10382) — velero-io/velero
- [#10381 1.18: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10381) — velero-io/velero
- [#10348 1.18: Backport #10342: Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10348) — velero-io/velero
- [#10327 Detect data path pod deletion via informer DeleteFunc](https://github.com/velero-io/velero/pull/10327) — velero-io/velero
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero
- [#10309 Report a measured zero incremental instead of erasing it](https://github.com/velero-io/velero/pull/10309) — velero-io/velero
- [#10308 Detect block uploader cancellation through wrapped errors](https://github.com/velero-io/velero/pull/10308) — velero-io/velero
- [#10307 Fix generic CSI changeID retrieval and honor snapshot class deletion policy for CBT retention](https://github.com/velero-io/velero/pull/10307) — velero-io/velero
- [#10306 Degrade CBT bitmap failures to allocated blocks instead of whole-device](https://github.com/velero-io/velero/pull/10306) — velero-io/velero
- [#10305 Log the discovered parent snapshot ID, not the empty lookup parameter](https://github.com/velero-io/velero/pull/10305) — velero-io/velero
- [#10286 Fix re-request-review workflow for fork-originated PRs (privilege separation)](https://github.com/velero-io/velero/pull/10286) — velero-io/velero
- [#328 [release-1.13] Bump google.golang.org/grpc from 1.73.0 to 1.79.3 (cherry-pick #307)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/328) — velero-io/velero-plugin-for-microsoft-azure
- [#327 [release-1.14] feat: Add SAS token authentication for Azure Blob Storage object store (cherry-pick #314)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/327) — velero-io/velero-plugin-for-microsoft-azure
- [#326 [release-1.13] feat: Add SAS token authentication for Azure Blob Storage object store (cherry-pick #314)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/326) — velero-io/velero-plugin-for-microsoft-azure
- [#325 [release-1.13] Update AzureAD Microsoft Authentication Library to v1.5.0 (cherry-pick #294)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/325) — velero-io/velero-plugin-for-microsoft-azure
- [#325 [release-1.14] fix: allow valid S3 object tag values (cherry-pick #294)](https://github.com/velero-io/velero-plugin-for-aws/pull/325) — velero-io/velero-plugin-for-aws
- [#324 [release-1.13] fix: allow valid S3 object tag values (cherry-pick #294)](https://github.com/velero-io/velero-plugin-for-aws/pull/324) — velero-io/velero-plugin-for-aws
- [#323 [release-1.13] Fix SSE-C signed URLs (cherry-pick #280)](https://github.com/velero-io/velero-plugin-for-aws/pull/323) — velero-io/velero-plugin-for-aws
- [#322 [release-1.13] Add support for specifying KMS key for EBS volume restoration (cherry-pick #276)](https://github.com/velero-io/velero-plugin-for-aws/pull/322) — velero-io/velero-plugin-for-aws
- [#269 [release-1.13] Bump go.opentelemetry.io/otel/sdk to 1.40.0, CVE-2026-24051 (cherry-pick #250)](https://github.com/velero-io/velero-plugin-for-gcp/pull/269) — velero-io/velero-plugin-for-gcp
- [#268 [release-1.13] Bump golang to 1.25 to fix CVEs. (cherry-pick #245)](https://github.com/velero-io/velero-plugin-for-gcp/pull/268) — velero-io/velero-plugin-for-gcp
- [#267 [release-1.13] feat: copy labels from Disk to Snapshot (cherry-pick #178)](https://github.com/velero-io/velero-plugin-for-gcp/pull/267) — velero-io/velero-plugin-for-gcp
- [#321 [release-1.13] Add descriptive error message when SSE-C is denied on S3 buckets (cherry-pick #318)](https://github.com/velero-io/velero-plugin-for-aws/pull/321) — velero-io/velero-plugin-for-aws
- [#320 [release-1.14] Add descriptive error message when SSE-C is denied on S3 buckets (cherry-pick #318)](https://github.com/velero-io/velero-plugin-for-aws/pull/320) — velero-io/velero-plugin-for-aws
- [#324 Use velero-io/velero's shared reusable workflows instead of local copies](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/324) — velero-io/velero-plugin-for-microsoft-azure
- [#266 Use velero-io/velero's shared reusable workflows instead of local copies](https://github.com/velero-io/velero-plugin-for-gcp/pull/266) — velero-io/velero-plugin-for-gcp
- [#319 Use velero-io/velero's shared reusable workflows instead of local copies](https://github.com/velero-io/velero-plugin-for-aws/pull/319) — velero-io/velero-plugin-for-aws
- [#10281 Make backport/pr-filepath-check/auto_assign_prs reusable across velero-io repos](https://github.com/velero-io/velero/pull/10281) — velero-io/velero
- [#10276 Fail fast with clear error when data mover pod is unschedulable](https://github.com/velero-io/velero/pull/10276) — velero-io/velero
- [#10275 Implement namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10275) — velero-io/velero
- [#10263 [release-1.18] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10263) — velero-io/velero
- [#10262 [release-1.17] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10262) — velero-io/velero
- [#10224 1.18: Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10224) — velero-io/velero
- [#10223 [release-1.17] Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10223) — velero-io/velero

**openshift** (22)
- [#2411 [oadp-1.4] Add --ginkgo.junit-report flag to test-e2e target](https://github.com/openshift/oadp-operator/pull/2411) — openshift/oadp-operator
- [#2409 [oadp-1.6] Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2409) — openshift/oadp-operator
- [#2408 Migrate Claude e2e failure analysis to claude-ai-helpers step-registry](https://github.com/openshift/oadp-operator/pull/2408) — openshift/oadp-operator
- [#83957 oadp-operator: migrate e2e Claude failure analysis to claude-ai-helpers post-step](https://github.com/openshift/release/pull/83957) — openshift/release
- [#2406 [OADP-8716] Fall back to previous MCE patch version if HyperShift operator fails to start](https://github.com/openshift/oadp-operator/pull/2406) — openshift/oadp-operator
- [#2404 test: unpend two kdm restore PIts, fixing bugs found via live e2e validation](https://github.com/openshift/oadp-operator/pull/2404) — openshift/oadp-operator
- [#2402 Unpend two kdm restore e2e tests now that phase 4 landed](https://github.com/openshift/oadp-operator/pull/2402) — openshift/oadp-operator
- [#83833 Rename KDM e2e job to virt-kdm, fix operator-sdk-bundle-image step bugs](https://github.com/openshift/release/pull/83833) — openshift/release
- [#2387 Expose kubevirt-datamover --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/pull/2387) — openshift/oadp-operator
- [#83416 Add watch-ci-status skill: watch postsubmit refresh + PR status](https://github.com/openshift/release/pull/83416) — openshift/release
- [#83341 ci-tools: bump bin build memory request to 3Gi](https://github.com/openshift/release/pull/83341) — openshift/release
- [#2379 Fix ENVTESTPATH arch decided at Makefile-parse time on cold bin/](https://github.com/openshift/oadp-operator/pull/2379) — openshift/oadp-operator
- [#2378 Fix ENVTESTPATH arch decided at Makefile-parse time on cold bin/](https://github.com/openshift/oadp-operator/pull/2378) — openshift/oadp-operator
- [#2376 [oadp-1.4] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2376) — openshift/oadp-operator
- [#2375 [oadp-1.5] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2375) — openshift/oadp-operator
- [#2374 [oadp-1.6] fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2374) — openshift/oadp-operator
- [#2373 fix: check errors.IsNotFound before failing DaemonSet delete in NodeAgent reconcile](https://github.com/openshift/oadp-operator/pull/2373) — openshift/oadp-operator
- [#5363 pkg/steps: retry network-unreachable builds, capture failed build logs](https://github.com/openshift/ci-tools/pull/5363) — openshift/ci-tools
- [#83299 gather-extra: harden against oc timeouts/flakes; jq to ARTIFACT_DIR](https://github.com/openshift/release/pull/83299) — openshift/release
- [#83286 Prep oadp-1.4/1.5 with bundle promotion for future cross-repo e2e](https://github.com/openshift/release/pull/83286) — openshift/release
- [#83282 Promote oadp-operator bundle directly instead of a broken index](https://github.com/openshift/release/pull/83282) — openshift/release
- [#83221 gather-must-gather: retry camgi download, don't fail gather on it](https://github.com/openshift/release/pull/83221) — openshift/release

**migtools** (11)
- [#200 test: pin that a same-restore-name incomplete sibling still blocks the VM flip](https://github.com/migtools/kubevirt-datamover-controller/pull/200) — migtools/kubevirt-datamover-controller
- [#50 Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/50) — migtools/kubevirt-datamover-plugin
- [#199 fix: honor matchLabels selector on restore target PVC instead of failing](https://github.com/migtools/kubevirt-datamover-controller/pull/199) — migtools/kubevirt-datamover-controller
- [#197 fix: work PVC must be ReadWriteOnce, not the target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/pull/197) — migtools/kubevirt-datamover-controller
- [#195 fix: name root cause in restore PVC-conflict error messages](https://github.com/migtools/kubevirt-datamover-controller/pull/195) — migtools/kubevirt-datamover-controller
- [#182 fix: use %s format verb for cmp.Diff in t.Errorf calls](https://github.com/migtools/udistribution/pull/182) — migtools/udistribution
- [#47 Address declined CodeRabbit follow-ups from PR #41, add missing unit test coverage](https://github.com/migtools/kubevirt-datamover-plugin/pull/47) — migtools/kubevirt-datamover-plugin
- [#187 feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/187) — migtools/kubevirt-datamover-controller
- [#186 feat: DD concurrency limiter (#175), scratch PVC hardening, multi-disk isolation test (issue #73 Phase 4)](https://github.com/migtools/kubevirt-datamover-controller/pull/186) — migtools/kubevirt-datamover-controller
- [#182 fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/182) — migtools/kubevirt-datamover-controller
- [#180 fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/180) — migtools/kubevirt-datamover-controller

**Other** (19)
- [#375 feat(libpod): add Podman /libpod/* API, manifest lists, and multi-arch build support](https://github.com/socktainer/socktainer/pull/375) — socktainer/socktainer
- [#1 Make pdf2text-ocr an installable, colorful, foldable-friendly PWA with progress, print, and page navigation](https://github.com/kaovilai/pdf2text-pwa/pull/1) — kaovilai/pdf2text-pwa
- [#13882 macos: add regression test for double-click rename after dragging tab…](https://github.com/ghostty-org/ghostty/pull/13882) — ghostty-org/ghostty
- [#13881 macos: add regression test for double-click rename after dragging tab between windows](https://github.com/ghostty-org/ghostty/pull/13881) — ghostty-org/ghostty
- [#576 feat(openshift): preflight-check EC release signatures, offer nightly-style bypass](https://github.com/kaovilai/dotfiles/pull/576) — kaovilai/dotfiles
- [#163 Refresh screenshots to reflect current profiles and rehearsal button](https://github.com/kaovilai/github-bot-command-palette/pull/163) — kaovilai/github-bot-command-palette
- [#162 Resolve rehearsal rerun job names from presubmit config, not comment scraping](https://github.com/kaovilai/github-bot-command-palette/pull/162) — kaovilai/github-bot-command-palette
- [#160 Skip /test on non-Prow checks, add optional Actions rerun](https://github.com/kaovilai/github-bot-command-palette/pull/160) — kaovilai/github-bot-command-palette
- [#159 Add ship skill for solo-repo commit-to-merge cycle](https://github.com/kaovilai/github-bot-command-palette/pull/159) — kaovilai/github-bot-command-palette
- [#158 Fix job picker status mismatching GitHub's real check state](https://github.com/kaovilai/github-bot-command-palette/pull/158) — kaovilai/github-bot-command-palette
- [#188 Fix review queue card deadspace](https://github.com/kaovilai/kaovilai.pw/pull/188) — kaovilai/kaovilai.pw
- [#155 Fix detectTargetBranch resolving head branch instead of base](https://github.com/kaovilai/github-bot-command-palette/pull/155) — kaovilai/github-bot-command-palette
- [#35 Fix: stop injecting popup-only Bootstrap bundle + popup.js into every site](https://github.com/HASHCUT69/Blend-n-Run/pull/35) — HASHCUT69/Blend-n-Run
- [#187 Implementing recent review display feature](https://github.com/kaovilai/kaovilai.pw/pull/187) — kaovilai/kaovilai.pw
- [#72 Add reviewDecision, approvalCount, and requiredApprovals to open-prs.json reviewQueue](https://github.com/kaovilai/kaovilai/pull/72) — kaovilai/kaovilai
- [#185 Use PAT for Dependabot auto-merge to fix failure on workflow-file PRs](https://github.com/kaovilai/kaovilai.pw/pull/185) — kaovilai/kaovilai.pw
- [#183 Add review queue panel consuming reviewQueue data from open-prs.json](https://github.com/kaovilai/kaovilai.pw/pull/183) — kaovilai/kaovilai.pw
- [#24 Fix Dependabot security alerts in yarn.lock](https://github.com/kaovilai/oadp-ui/pull/24) — kaovilai/oadp-ui
- [#23 Recompile stale daily-upstream-parity.lock.yml](https://github.com/kaovilai/oadp-ui/pull/23) — kaovilai/oadp-ui
## PRs Reviewed (77)

**velero-io** (41)
- [#10360 [cherry-pick release-1.18] Fast-fail backup when built-in data mover has no running node-agent](https://github.com/velero-io/velero/pull/10360) — velero-io/velero
- [#10356 Add volumeName condition to VolumePolicy resource filtering](https://github.com/velero-io/velero/pull/10356) — velero-io/velero
- [#10354 Re-process InProgress DeleteBackupRequests on retry](https://github.com/velero-io/velero/pull/10354) — velero-io/velero
- [#10331 Preserve PVC selected-node annotation via carrier annotation for in-place restore](https://github.com/velero-io/velero/pull/10331) — velero-io/velero
- [#10280 fix(restore_finalizer): bound WaitRestoreExecHook poll with resourceT…](https://github.com/velero-io/velero/pull/10280) — velero-io/velero
- [#10366 Bump github/codeql-action from 4.37.6 to 4.37.7 in the github-actions group](https://github.com/velero-io/velero/pull/10366) — velero-io/velero
- [#10387 [Backport release-1.18] Avoid io.ReadAll in buildFinalTarball()](https://github.com/velero-io/velero/pull/10387) — velero-io/velero
- [#10388 [Backport release-1.17] Avoid io.ReadAll in buildFinalTarball()](https://github.com/velero-io/velero/pull/10388) — velero-io/velero
- [#10329 Embed CRD manifests via go:embed instead of codegen](https://github.com/velero-io/velero/pull/10329) — velero-io/velero
- [#10359 Fix e2e kind matrix misparsing pre-release node tags](https://github.com/velero-io/velero/pull/10359) — velero-io/velero
- [#10235 Allow configuration of page buffer size in Item Collector (#10219)](https://github.com/velero-io/velero/pull/10235) — velero-io/velero
- [#10252 Skip signing a download URL when no artifacts can exist yet](https://github.com/velero-io/velero/pull/10252) — velero-io/velero
- [#10346 Double check the label for backup when deleting VSC](https://github.com/velero-io/velero/pull/10346) — velero-io/velero
- [#10315 Testing: Implement missing unit tests for pkg/backup/snapshots.go](https://github.com/velero-io/velero/pull/10315) — velero-io/velero
- [#10342 Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10342) — velero-io/velero
- [#10337 Document secretNames/configMapNames for backup/restore PVC config](https://github.com/velero-io/velero/pull/10337) — velero-io/velero
- [#10347 1.18: Only sync finished backups from object storage](https://github.com/velero-io/velero/pull/10347) — velero-io/velero
- [#10335 [release-1.18] Support copying namespace-scoped secrets/configmaps for backup and restore PVC provisioning](https://github.com/velero-io/velero/pull/10335) — velero-io/velero
- [#10322 Issue 10321: fill the error to the corresponding CR when data mover pod is evicted](https://github.com/velero-io/velero/pull/10322) — velero-io/velero
- [#10237 Reject negative --ttl in backup create validation](https://github.com/velero-io/velero/pull/10237) — velero-io/velero
- [#10319 [cherry-pick][1.18] Remove PVC and PV inclusion check during creating PVR.](https://github.com/velero-io/velero/pull/10319) — velero-io/velero
- [#10269 Remove PVC and PV inclusion check during creating PVR.](https://github.com/velero-io/velero/pull/10269) — velero-io/velero
- [#10253 Refactor: Remove legacy resticrepositories hardcoding from restore controller](https://github.com/velero-io/velero/pull/10253) — velero-io/velero
- [#10317 Cleanup: Remove deprecated --wait flag from velero uninstall](https://github.com/velero-io/velero/pull/10317) — velero-io/velero
- [#10312 assert expected errors from the test case rather than the returned error](https://github.com/velero-io/velero/pull/10312) — velero-io/velero
- [#10264 Fix loadConcurrency slot leak on forced cancel](https://github.com/velero-io/velero/pull/10264) — velero-io/velero
- [#10229 Add printer columns for DownloadRequest and ServerStatusRequest](https://github.com/velero-io/velero/pull/10229) — velero-io/velero
- [#10255 Use thread safe map for cancel recorder](https://github.com/velero-io/velero/pull/10255) — velero-io/velero
- [#10258 Cap the unzip of metadata download to avoid OOM kill](https://github.com/velero-io/velero/pull/10258) — velero-io/velero
- [#10270 Cap the metadata decompression in object store](https://github.com/velero-io/velero/pull/10270) — velero-io/velero
- [#10254 credentialFile in Config of BSL should be used internally](https://github.com/velero-io/velero/pull/10254) — velero-io/velero
- [#10283 test: add verification for skippedPVTracker in backup tests](https://github.com/velero-io/velero/pull/10283) — velero-io/velero
- [#10279 Use k8s.io/api well-known label constants instead of hardcoded strings](https://github.com/velero-io/velero/pull/10279) — velero-io/velero
- [#10273 Fix PVR regression](https://github.com/velero-io/velero/pull/10273) — velero-io/velero
- [#10236 E2E: add kind VolumeSnapshotClass test data](https://github.com/velero-io/velero/pull/10236) — velero-io/velero
- [#10245 Document what the DownloadRequest Processed phase means](https://github.com/velero-io/velero/pull/10245) — velero-io/velero
- [#10250 Fix pvr deadlock](https://github.com/velero-io/velero/pull/10250) — velero-io/velero
- [#10251 Fix wrong node-agent check result when PVR restorer run concurrently](https://github.com/velero-io/velero/pull/10251) — velero-io/velero
- [#10234 Make restore logs testable by returning errors instead of calling cmd.Exit](https://github.com/velero-io/velero/pull/10234) — velero-io/velero
- [#10231 Site: add a troubleshooting entry for log downloads failing with "no such host"](https://github.com/velero-io/velero/pull/10231) — velero-io/velero
- [#10228 docs: fix grammar and typos in backup-restore-windows](https://github.com/velero-io/velero/pull/10228) — velero-io/velero

**openshift** (22)
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
- [#2395 e2e: add cacert tests using in-cluster minio with TLS](https://github.com/openshift/oadp-operator/pull/2395) — openshift/oadp-operator
- [#2390 Deprecate config.credentialsFile; translate to spec.credential](https://github.com/openshift/oadp-operator/pull/2390) — openshift/oadp-operator
- [#463 Merge https://github.com/openshift/openshift-velero-plugin:oadp-dev (033e6b1) into oadp-dev](https://github.com/openshift/openshift-velero-plugin/pull/463) — openshift/openshift-velero-plugin
- [#163 Merge https://github.com/velero-io/velero-plugin-for-gcp:main (1e7b956) into oadp-dev](https://github.com/openshift/velero-plugin-for-gcp/pull/163) — openshift/velero-plugin-for-gcp
- [#2393 [oadp-1.6] OADP-8548: PodResources unset fields should be output as "0" to fix parsing errors results in ignored resource settings](https://github.com/openshift/oadp-operator/pull/2393) — openshift/oadp-operator
- [#2396 [oadp-1.6] Add e2e coverage for kubevirt-datamover VM backup/restore: multi-PVC, incremental sequence, and CBT restore (+ max-concurrent-data-movers config)](https://github.com/openshift/oadp-operator/pull/2396) — openshift/oadp-operator
- [#2394 [OADP-8700] Guard NodeAgent.ExtraArgs access against nil when using restic config](https://github.com/openshift/oadp-operator/pull/2394) — openshift/oadp-operator
- [#2385 OADP-8548: PodResources unset fields should be output as "0" to fix parsing errors results in ignored resource settings](https://github.com/openshift/oadp-operator/pull/2385) — openshift/oadp-operator
- [#162 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.12.2 (82b9141) into oadp-1.5](https://github.com/openshift/velero-plugin-for-aws/pull/162) — openshift/velero-plugin-for-aws
- [#562 Rebase oadp-dev onto upstream/main (4f55fb5a6)](https://github.com/openshift/velero/pull/562) — openshift/velero
- [#160 Merge https://github.com/openshift/oadp-must-gather:oadp-1.4 (832961f) into oadp-1.4](https://github.com/openshift/oadp-must-gather/pull/160) — openshift/oadp-must-gather
- [#2382 PodResources must be complete for Velero parser](https://github.com/openshift/oadp-operator/pull/2382) — openshift/oadp-operator

**migtools** (11)
- [#375 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (b85b84a) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/375) — migtools/oadp-non-admin
- [#49 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (9531d54) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/49) — migtools/kubevirt-datamover-plugin
- [#258 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (0aeee34) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/258) — migtools/oadp-cli
- [#100 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (2f3a322) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/100) — migtools/oadp-vm-file-restore
- [#98 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-dev (2768b89) into oadp-dev](https://github.com/migtools/oadp-vm-file-restore/pull/98) — migtools/oadp-vm-file-restore
- [#190 [oadp-1.6] feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/190) — migtools/kubevirt-datamover-controller
- [#257 Merge https://github.com/migtools/oadp-cli:oadp-1.5 (f2cb269) into oadp-1.5](https://github.com/migtools/oadp-cli/pull/257) — migtools/oadp-cli
- [#188 [oadp-1.6] fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/188) — migtools/kubevirt-datamover-controller
- [#185 [oadp-1.6] feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/185) — migtools/kubevirt-datamover-controller
- [#183 [oadp-1.6] feat: add staleness check for per-VM DataUpload serialization](https://github.com/migtools/kubevirt-datamover-controller/pull/183) — migtools/kubevirt-datamover-controller
- [#181 [oadp-1.6] fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/181) — migtools/kubevirt-datamover-controller

**Other** (3)
- [#849 fix: status-reconciler track own config state for dropped deltas](https://github.com/kubernetes-sigs/prow/pull/849) — kubernetes-sigs/prow
- [#12323 Fix kubevirt-velero-plugin branch target for oadp-1.4](https://github.com/openshift-eng/ocp-build-data/pull/12323) — openshift-eng/ocp-build-data
- [#12324 Fix kubevirt-velero-plugin branch target for oadp-1.3](https://github.com/openshift-eng/ocp-build-data/pull/12324) — openshift-eng/ocp-build-data
## Issues/PRs Commented On (53)

**velero-io** (23)
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
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#9964 backup-finalizer retries forever when object-store PUT hits a non-retryable error (e.g. Azure BlobImmutableDueToPolicy 409)](https://github.com/velero-io/velero/issues/9964) — velero-io/velero
- [#10265 Technical Debt: Remove `context.TODO()` in `pkg/util/kube and pkg/util/podvolume`](https://github.com/velero-io/velero/issues/10265) — velero-io/velero
- [#10266 docs: how to run CSI e2e specs against a local Kind cluster](https://github.com/velero-io/velero/issues/10266) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero
- [#10199 Backup and Restore CRDs have no printer columns since the 2021 revert](https://github.com/velero-io/velero/issues/10199) — velero-io/velero
- [#8457 Configurable pull policy when `velero install`](https://github.com/velero-io/velero/issues/8457) — velero-io/velero

**openshift** (6)
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#10590 GCP CAPI: bootstrap in master instance group causes worker ignition failure via ILB pinning](https://github.com/openshift/installer/issues/10590) — openshift/installer
- [#2391 Follow up: simplify and document PodResources defaulting](https://github.com/openshift/oadp-operator/issues/2391) — openshift/oadp-operator
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#1832 e2e jobs for other repos](https://github.com/openshift/oadp-operator/issues/1832) — openshift/oadp-operator

**migtools** (13)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#84 Implement concurrent data mover limiter for DU and DD controllers](https://github.com/migtools/kubevirt-datamover-controller/issues/84) — migtools/kubevirt-datamover-controller
- [#175 Implement concurrency limiter for DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/175) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#120 Cancellation cleanup errors are logged but not propagated, phase moves to Canceled regardless](https://github.com/migtools/kubevirt-datamover-controller/issues/120) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller

**Other** (11)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#378 ci on real hw](https://github.com/socktainer/socktainer/issues/378) — socktainer/socktainer
- [#43 Chrome Web Store listing reports location permission](https://github.com/rxliuli/redirector/issues/43) — rxliuli/redirector
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#201 feat: Add Podman libpod API endpoints for native podman CLI support](https://github.com/socktainer/socktainer/issues/201) — socktainer/socktainer
- [#101 UDP support](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#481 Support using a later patch release than what's in go.mod](https://github.com/actions/setup-go/issues/481) — actions/setup-go
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
- [#477 branchprotector: excluded branches retain existing protection instead of being removed](https://github.com/kubernetes-sigs/prow/issues/477) — kubernetes-sigs/prow
- [#2906 EFS should have snapshot function similar to EBS](https://github.com/aws/aws-sdk-go-v2/issues/2906) — aws/aws-sdk-go-v2
- [#22368 Facilitate ConfigMap rollouts / management](https://github.com/kubernetes/kubernetes/issues/22368) — kubernetes/kubernetes
## Issues Closed (26)

**velero-io** (8)
- [#10328 Stop committing generated config/crd/*/crds/crds.go; embed CRDs via go:embed at build time](https://github.com/velero-io/velero/issues/10328) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#10296 Cancelling a block data mover backup reports it as a failure — cancel sentinel compared with == against a wrapped error](https://github.com/velero-io/velero/issues/10296) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10300 Unified repo config dir resolves to unwritable /udmrepo when HOME=/ (arbitrary-UID / OpenShift non-root server)](https://github.com/velero-io/velero/issues/10300) — velero-io/velero
- [#10301 Dead code in repository maintenance: GenOptionMaintainMode/Full/Quick and overwrite*MaintainInterval are unreachable](https://github.com/velero-io/velero/issues/10301) — velero-io/velero
- [#10304 Block data mover: retained CBT base snapshots are never reclaimed at backup deletion (design L370-371/L474 unimplemented)](https://github.com/velero-io/velero/issues/10304) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero

**openshift** (3)
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#2383 Evaluate and migrate user-provided credentialsFile handling for Velero #10254](https://github.com/openshift/oadp-operator/issues/2383) — openshift/oadp-operator
- [#5333 e2e-oo permanently failing: fixture pins EOL integrated stream ocp/4.6, configresolver returns 400](https://github.com/openshift/ci-tools/issues/5333) — openshift/ci-tools

**migtools** (12)
- [#198 Add regression test: ensureWorkPVC must force ReadWriteOnce regardless of target's AccessModes](https://github.com/migtools/kubevirt-datamover-controller/issues/198) — migtools/kubevirt-datamover-controller
- [#42 Follow-up: address CodeRabbit code-quality suggestions declined during PR #41 review](https://github.com/migtools/kubevirt-datamover-plugin/issues/42) — migtools/kubevirt-datamover-plugin
- [#130 Checkpoint chain integrity gaps not covered by #77 (corrupt-but-present objects, TOCTOU, memoization verdict-loss, index history wipe)](https://github.com/migtools/kubevirt-datamover-controller/issues/130) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#121 Spec.OperationTimeout is not honored by either DataUpload or DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/121) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller

**Other** (3)
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#625 Add pagination support for get_pull_request_diff to handle large PRs](https://github.com/github/github-mcp-server/issues/625) — github/github-mcp-server
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
