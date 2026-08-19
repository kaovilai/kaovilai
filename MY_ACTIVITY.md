# Activity Log

> **Period:** 2026-08-05 — 2026-08-19
> **Generated:** 2026-08-19 01:37:34 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 62 |
| PRs Opened | 100 |
| PRs Reviewed | 76 |
| Issues/PRs Commented | 43 |
| Issues Closed | 25 |

---

## PRs Merged (62)

**velero-io** (10)
- [#10262 [release-1.17] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10262) — velero-io/velero
- [#10263 [release-1.18] Backport #10250: Fix pod volume restore deadlock](https://github.com/velero-io/velero/pull/10263) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero
- [#10220 Group Dependabot GitHub Actions updates](https://github.com/velero-io/velero/pull/10220) — velero-io/velero
- [#10211 backport: add pre-merge label-on-comment support; add copilot-instructions and auto-labeler for changelog exemptions](https://github.com/velero-io/velero/pull/10211) — velero-io/velero
- [#10222 1.18 Backport: correct typos in log messages and status strings (#10192)](https://github.com/velero-io/velero/pull/10222) — velero-io/velero
- [#10223 [release-1.17] Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10223) — velero-io/velero
- [#10221 1.17 Backport #10192: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10221) — velero-io/velero
- [#10224 1.18: Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10224) — velero-io/velero
- [#10047 Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10047) — velero-io/velero

**openshift** (19)
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
- [#2366 [oadp-1.4] OADP-7829: Add additive extraArgs support for Velero server and node-agent](https://github.com/openshift/oadp-operator/pull/2366) — openshift/oadp-operator
- [#83124 ixney on 5.1ney (rebased)](https://github.com/openshift/release/pull/83124) — openshift/release
- [#83078 Add e2e-test-kubevirt-aws presubmit for oadp-dev 5.0](https://github.com/openshift/release/pull/83078) — openshift/release
- [#83110 Promote oadp-operator bundle/index/e2e-test-binary images (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83110) — openshift/release
- [#2208 OADP-7943, OADP-7829: Fix DPA annotation changes not triggering reconciliation](https://github.com/openshift/oadp-operator/pull/2208) — openshift/oadp-operator
- [#434 OADP-6536: Call WaitGroup.Done() once only when PVB changes to final status the first time to avoid panic](https://github.com/openshift/velero/pull/434) — openshift/velero
- [#2353 Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2353) — openshift/oadp-operator

**migtools** (8)
- [#187 feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/187) — migtools/kubevirt-datamover-controller
- [#186 feat: DD concurrency limiter (#175), scratch PVC hardening, multi-disk isolation test (issue #73 Phase 4)](https://github.com/migtools/kubevirt-datamover-controller/pull/186) — migtools/kubevirt-datamover-controller
- [#182 fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/182) — migtools/kubevirt-datamover-controller
- [#124 feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/124) — migtools/kubevirt-datamover-controller
- [#180 fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/180) — migtools/kubevirt-datamover-controller
- [#170 fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/170) — migtools/kubevirt-datamover-controller
- [#44 Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/44) — migtools/kubevirt-datamover-plugin
- [#41 Add RestoreItemAction plugins to trigger kubevirt datamover restore](https://github.com/migtools/kubevirt-datamover-plugin/pull/41) — migtools/kubevirt-datamover-plugin

**Other** (25)
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
- [#71 Export review-queue panel data in open-prs.json for kaovilai.pw](https://github.com/kaovilai/kaovilai/pull/71) — kaovilai/kaovilai
- [#17 Recompile Daily Upstream Parity lock file and add license attribution rules](https://github.com/kaovilai/oadp-ui/pull/17) — kaovilai/oadp-ui
- [#15 Merge open Dependabot PRs; pin back major bumps that break console peer compatibility](https://github.com/kaovilai/oadp-ui/pull/15) — kaovilai/oadp-ui
- [#28 docs: note full Xcode requirement for hev-socks5-server build script](https://github.com/Nanako0129/SocksBypass/pull/28) — Nanako0129/SocksBypass
- [#13 Exclude README.md from protected-files denylist in daily-upstream-parity workflow](https://github.com/kaovilai/oadp-ui/pull/13) — kaovilai/oadp-ui
- [#8 Add grouped Dependabot updates with CI-gated auto-merge](https://github.com/kaovilai/oadp-ui/pull/8) — kaovilai/oadp-ui
- [#1 Add daily gh-aw upstream parity workflow for single-cluster OADP UI](https://github.com/kaovilai/oadp-ui/pull/1) — kaovilai/oadp-ui
- [#177 Group “Currently Working On” contributions by organization before repository](https://github.com/kaovilai/kaovilai.pw/pull/177) — kaovilai/kaovilai.pw
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
- [#149 Fix command bar overlapping review dialog comment box](https://github.com/kaovilai/github-bot-command-palette/pull/149) — kaovilai/github-bot-command-palette
- [#174 Addressing date and time display per browser timezone](https://github.com/kaovilai/kaovilai.pw/pull/174) — kaovilai/kaovilai.pw
## PRs Opened (100)

**velero-io** (37)
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
- [#10222 1.18 Backport: correct typos in log messages and status strings (#10192)](https://github.com/velero-io/velero/pull/10222) — velero-io/velero
- [#10221 1.17 Backport #10192: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10221) — velero-io/velero
- [#10220 Group Dependabot GitHub Actions updates](https://github.com/velero-io/velero/pull/10220) — velero-io/velero
- [#10211 backport: add pre-merge label-on-comment support; add copilot-instructions and auto-labeler for changelog exemptions](https://github.com/velero-io/velero/pull/10211) — velero-io/velero
- [#10210 Fix explicitly excluded namespaces still tracked via LabelSelector/OrLabelSelector match](https://github.com/velero-io/velero/pull/10210) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero

**openshift** (24)
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
- [#2368 [oadp-1.4] Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2368) — openshift/oadp-operator
- [#2367 Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2367) — openshift/oadp-operator
- [#2366 [oadp-1.4] OADP-7829: Add additive extraArgs support for Velero server and node-agent](https://github.com/openshift/oadp-operator/pull/2366) — openshift/oadp-operator
- [#83124 ixney on 5.1ney (rebased)](https://github.com/openshift/release/pull/83124) — openshift/release
- [#83110 Promote oadp-operator bundle/index/e2e-test-binary images (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83110) — openshift/release
- [#83078 Add e2e-test-kubevirt-aws presubmit for oadp-dev 5.0](https://github.com/openshift/release/pull/83078) — openshift/release
- [#83049 Run oadp-operator e2e against kdm-controller/kdm-plugin PRs (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83049) — openshift/release
- [#2360 docs: kubevirt-datamover design doc — 2026-08-06 implementation status](https://github.com/openshift/oadp-operator/pull/2360) — openshift/oadp-operator
- [#2358 [oadp-1.4] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2358) — openshift/oadp-operator
- [#2357 [oadp-1.5] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2357) — openshift/oadp-operator

**migtools** (8)
- [#47 Address declined CodeRabbit follow-ups from PR #41, add missing unit test coverage](https://github.com/migtools/kubevirt-datamover-plugin/pull/47) — migtools/kubevirt-datamover-plugin
- [#187 feat: concurrency limiter for DataUpload controller (issue #174)](https://github.com/migtools/kubevirt-datamover-controller/pull/187) — migtools/kubevirt-datamover-controller
- [#186 feat: DD concurrency limiter (#175), scratch PVC hardening, multi-disk isolation test (issue #73 Phase 4)](https://github.com/migtools/kubevirt-datamover-controller/pull/186) — migtools/kubevirt-datamover-controller
- [#182 fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/182) — migtools/kubevirt-datamover-controller
- [#180 fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/180) — migtools/kubevirt-datamover-controller
- [#170 fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/170) — migtools/kubevirt-datamover-controller
- [#44 Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/44) — migtools/kubevirt-datamover-plugin
- [#373 Document NADR (NonAdminDownloadRequest) usage](https://github.com/migtools/oadp-non-admin/pull/373) — migtools/oadp-non-admin

**Other** (31)
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
- [#20 Add `__mocks__/**` to allowed-files for upstream-parity agent](https://github.com/kaovilai/oadp-ui/pull/20) — kaovilai/oadp-ui
- [#71 Export review-queue panel data in open-prs.json for kaovilai.pw](https://github.com/kaovilai/kaovilai/pull/71) — kaovilai/kaovilai
- [#17 Recompile Daily Upstream Parity lock file and add license attribution rules](https://github.com/kaovilai/oadp-ui/pull/17) — kaovilai/oadp-ui
- [#28 docs: note full Xcode requirement for hev-socks5-server build script](https://github.com/Nanako0129/SocksBypass/pull/28) — Nanako0129/SocksBypass
- [#1 Dual-stack listening + structured startup output with per-interface shell env examples](https://github.com/kaovilai/iOS-SOCKS-Server/pull/1) — kaovilai/iOS-SOCKS-Server
- [#15 Merge open Dependabot PRs; pin back major bumps that break console peer compatibility](https://github.com/kaovilai/oadp-ui/pull/15) — kaovilai/oadp-ui
- [#13 Exclude README.md from protected-files denylist in daily-upstream-parity workflow](https://github.com/kaovilai/oadp-ui/pull/13) — kaovilai/oadp-ui
- [#8 Add grouped Dependabot updates with CI-gated auto-merge](https://github.com/kaovilai/oadp-ui/pull/8) — kaovilai/oadp-ui
- [#1 Add daily gh-aw upstream parity workflow for single-cluster OADP UI](https://github.com/kaovilai/oadp-ui/pull/1) — kaovilai/oadp-ui
- [#177 Group “Currently Working On” contributions by organization before repository](https://github.com/kaovilai/kaovilai.pw/pull/177) — kaovilai/kaovilai.pw
- [#18725 Release the VMBackup finalizer when its BackupTracker is gone](https://github.com/kubevirt/kubevirt/pull/18725) — kubevirt/kubevirt
- [#149 Fix command bar overlapping review dialog comment box](https://github.com/kaovilai/github-bot-command-palette/pull/149) — kaovilai/github-bot-command-palette
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
## PRs Reviewed (76)

**velero-io** (45)
- [#10315 Testing: Implement missing unit tests for pkg/backup/snapshots.go](https://github.com/velero-io/velero/pull/10315) — velero-io/velero
- [#10322 Issue 10321: fill the error to the corresponding CR when data mover pod is evicted](https://github.com/velero-io/velero/pull/10322) — velero-io/velero
- [#10235 Allow configuration of page buffer size in Item Collector (#10219)](https://github.com/velero-io/velero/pull/10235) — velero-io/velero
- [#10237 Reject negative --ttl in backup create validation](https://github.com/velero-io/velero/pull/10237) — velero-io/velero
- [#10252 Skip signing a download URL when no artifacts can exist yet](https://github.com/velero-io/velero/pull/10252) — velero-io/velero
- [#10319 [cherry-pick][1.18] Remove PVC and PV inclusion check during creating PVR.](https://github.com/velero-io/velero/pull/10319) — velero-io/velero
- [#10269 Remove PVC and PV inclusion check during creating PVR.](https://github.com/velero-io/velero/pull/10269) — velero-io/velero
- [#10253 Refactor: Remove legacy resticrepositories hardcoding from restore controller](https://github.com/velero-io/velero/pull/10253) — velero-io/velero
- [#10187 thread context through GetVolumeSnapshotContentForVolumeSnapshot](https://github.com/velero-io/velero/pull/10187) — velero-io/velero
- [#10185 Full backup for all data movers](https://github.com/velero-io/velero/pull/10185) — velero-io/velero
- [#10317 Cleanup: Remove deprecated --wait flag from velero uninstall](https://github.com/velero-io/velero/pull/10317) — velero-io/velero
- [#10312 assert expected errors from the test case rather than the returned error](https://github.com/velero-io/velero/pull/10312) — velero-io/velero
- [#10264 Fix loadConcurrency slot leak on forced cancel](https://github.com/velero-io/velero/pull/10264) — velero-io/velero
- [#10229 Add printer columns for DownloadRequest and ServerStatusRequest](https://github.com/velero-io/velero/pull/10229) — velero-io/velero
- [#10255 Use thread safe map for cancel recorder](https://github.com/velero-io/velero/pull/10255) — velero-io/velero
- [#10258 Cap the unzip of metadata download to avoid OOM kill](https://github.com/velero-io/velero/pull/10258) — velero-io/velero
- [#10270 Cap the metadata decompression in object store](https://github.com/velero-io/velero/pull/10270) — velero-io/velero
- [#10280 fix(restore_finalizer): bound WaitRestoreExecHook poll with resourceT…](https://github.com/velero-io/velero/pull/10280) — velero-io/velero
- [#10254 credentialFile in Config of BSL should be used internally](https://github.com/velero-io/velero/pull/10254) — velero-io/velero
- [#10283 test: add verification for skippedPVTracker in backup tests](https://github.com/velero-io/velero/pull/10283) — velero-io/velero
- [#10279 Use k8s.io/api well-known label constants instead of hardcoded strings](https://github.com/velero-io/velero/pull/10279) — velero-io/velero
- [#10167 validate backup name format before contacting the API server](https://github.com/velero-io/velero/pull/10167) — velero-io/velero
- [#10273 Fix PVR regression](https://github.com/velero-io/velero/pull/10273) — velero-io/velero
- [#318 Add descriptive error message when SSE-C is denied on S3 buckets](https://github.com/velero-io/velero-plugin-for-aws/pull/318) — velero-io/velero-plugin-for-aws
- [#10236 E2E: add kind VolumeSnapshotClass test data](https://github.com/velero-io/velero/pull/10236) — velero-io/velero
- [#10245 Document what the DownloadRequest Processed phase means](https://github.com/velero-io/velero/pull/10245) — velero-io/velero
- [#10250 Fix pvr deadlock](https://github.com/velero-io/velero/pull/10250) — velero-io/velero
- [#10251 Fix wrong node-agent check result when PVR restorer run concurrently](https://github.com/velero-io/velero/pull/10251) — velero-io/velero
- [#10210 Fix explicitly excluded namespaces still tracked via LabelSelector/OrLabelSelector match](https://github.com/velero-io/velero/pull/10210) — velero-io/velero
- [#10196 test: add unit tests for boolptr and stringptr utilities](https://github.com/velero-io/velero/pull/10196) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero
- [#10189 Make backupType case insensitive in the CLI.](https://github.com/velero-io/velero/pull/10189) — velero-io/velero
- [#10201 Bump kentaro-m/auto-assign-action from 2.0.0 to 2.0.2](https://github.com/velero-io/velero/pull/10201) — velero-io/velero
- [#10234 Make restore logs testable by returning errors instead of calling cmd.Exit](https://github.com/velero-io/velero/pull/10234) — velero-io/velero
- [#10200 Add printer columns for Backup and Restore CRDs](https://github.com/velero-io/velero/pull/10200) — velero-io/velero
- [#10180 Site: add conference talks to resources and LinkedIn to community page](https://github.com/velero-io/velero/pull/10180) — velero-io/velero
- [#10231 Site: add a troubleshooting entry for log downloads failing with "no such host"](https://github.com/velero-io/velero/pull/10231) — velero-io/velero
- [#10228 docs: fix grammar and typos in backup-restore-windows](https://github.com/velero-io/velero/pull/10228) — velero-io/velero
- [#10190 docs: fix grammar and typos in customize-installation](https://github.com/velero-io/velero/pull/10190) — velero-io/velero
- [#10203 Bump github/codeql-action from 4.37.3 to 4.37.6](https://github.com/velero-io/velero/pull/10203) — velero-io/velero
- [#10202 Bump actions/setup-go from 6 to 7](https://github.com/velero-io/velero/pull/10202) — velero-io/velero
- [#10192 fix: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10192) — velero-io/velero
- [#10159 Fix excluded namespace objects leaking into backup with cross-namespa…](https://github.com/velero-io/velero/pull/10159) — velero-io/velero
- [#10162 [release-1.16] Fix ResourceDeletionStatusTracker key Kind mismatch in terminating-namespace wait (#9987)](https://github.com/velero-io/velero/pull/10162) — velero-io/velero
- [#10163 [release-1.17] Fix ResourceDeletionStatusTracker key Kind mismatch in terminating-namespace wait (#9987)](https://github.com/velero-io/velero/pull/10163) — velero-io/velero

**openshift** (12)
- [#2390 Deprecate config.credentialsFile; translate to spec.credential](https://github.com/openshift/oadp-operator/pull/2390) — openshift/oadp-operator
- [#2393 [oadp-1.6] OADP-8548: PodResources unset fields should be output as "0" to fix parsing errors results in ignored resource settings](https://github.com/openshift/oadp-operator/pull/2393) — openshift/oadp-operator
- [#2385 OADP-8548: PodResources unset fields should be output as "0" to fix parsing errors results in ignored resource settings](https://github.com/openshift/oadp-operator/pull/2385) — openshift/oadp-operator
- [#162 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.12.2 (82b9141) into oadp-1.5](https://github.com/openshift/velero-plugin-for-aws/pull/162) — openshift/velero-plugin-for-aws
- [#562 Rebase oadp-dev onto upstream/main (4f55fb5a6)](https://github.com/openshift/velero/pull/562) — openshift/velero
- [#160 Merge https://github.com/openshift/oadp-must-gather:oadp-1.4 (832961f) into oadp-1.4](https://github.com/openshift/oadp-must-gather/pull/160) — openshift/oadp-must-gather
- [#2382 PodResources must be complete for Velero parser](https://github.com/openshift/oadp-operator/pull/2382) — openshift/oadp-operator
- [#2370 [oadp-1.6] feat: expose staleDataUploadThreshold in DPA KubevirtDatamoverConfig](https://github.com/openshift/oadp-operator/pull/2370) — openshift/oadp-operator
- [#2361 feat: expose staleDataUploadThreshold in DPA KubevirtDatamoverConfig](https://github.com/openshift/oadp-operator/pull/2361) — openshift/oadp-operator
- [#83117 ixney on 5.1ney](https://github.com/openshift/release/pull/83117) — openshift/release
- [#2356 [oadp-1.6] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2356) — openshift/oadp-operator
- [#2359 [oadp-1.6] feat: use velero SA and add bound-sa-token volume for KDM controller](https://github.com/openshift/oadp-operator/pull/2359) — openshift/oadp-operator

**migtools** (14)
- [#257 Merge https://github.com/migtools/oadp-cli:oadp-1.5 (f2cb269) into oadp-1.5](https://github.com/migtools/oadp-cli/pull/257) — migtools/oadp-cli
- [#188 [oadp-1.6] fix: correct S3 checkpoint index when backup type mismatch detected](https://github.com/migtools/kubevirt-datamover-controller/pull/188) — migtools/kubevirt-datamover-controller
- [#185 [oadp-1.6] feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/185) — migtools/kubevirt-datamover-controller
- [#183 [oadp-1.6] feat: add staleness check for per-VM DataUpload serialization](https://github.com/migtools/kubevirt-datamover-controller/pull/183) — migtools/kubevirt-datamover-controller
- [#172 feat: add staleness check for per-VM DataUpload serialization](https://github.com/migtools/kubevirt-datamover-controller/pull/172) — migtools/kubevirt-datamover-controller
- [#165 [oadp-1.6] fix: handle hyphenated disk names in extractDiskName](https://github.com/migtools/kubevirt-datamover-controller/pull/165) — migtools/kubevirt-datamover-controller
- [#181 [oadp-1.6] fix: wire BSL profile config through to S3 credential resolution](https://github.com/migtools/kubevirt-datamover-controller/pull/181) — migtools/kubevirt-datamover-controller
- [#177 [oadp-1.6] fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/177) — migtools/kubevirt-datamover-controller
- [#178 [oadp-1.6] feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/178) — migtools/kubevirt-datamover-controller
- [#167 feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/167) — migtools/kubevirt-datamover-controller
- [#46 [oadp-1.6] Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/46) — migtools/kubevirt-datamover-plugin
- [#176 [oadp-1.6] issue #98: inject Azure Workload Identity env vars into datamover pods](https://github.com/migtools/kubevirt-datamover-controller/pull/176) — migtools/kubevirt-datamover-controller
- [#166 feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/166) — migtools/kubevirt-datamover-controller
- [#164 fix: handle hyphenated disk names in extractDiskName](https://github.com/migtools/kubevirt-datamover-controller/pull/164) — migtools/kubevirt-datamover-controller

**Other** (5)
- [#12323 Fix kubevirt-velero-plugin branch target for oadp-1.4](https://github.com/openshift-eng/ocp-build-data/pull/12323) — openshift-eng/ocp-build-data
- [#849 fix: status-reconciler track own config state for dropped deltas](https://github.com/kubernetes-sigs/prow/pull/849) — kubernetes-sigs/prow
- [#12324 Fix kubevirt-velero-plugin branch target for oadp-1.3](https://github.com/openshift-eng/ocp-build-data/pull/12324) — openshift-eng/ocp-build-data
- [#13 Exclude README.md from protected-files denylist in daily-upstream-parity workflow](https://github.com/kaovilai/oadp-ui/pull/13) — kaovilai/oadp-ui
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
## Issues/PRs Commented On (43)

**velero-io** (17)
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#10297 A measured zero incremental is indistinguishable from never-measured — omitempty erases it on the API status fields](https://github.com/velero-io/velero/issues/10297) — velero-io/velero
- [#9603 Backport/Cherry-pick GitHub action](https://github.com/velero-io/velero/issues/9603) — velero-io/velero
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero
- [#9833 Backup/restore describe for block data mover](https://github.com/velero-io/velero/issues/9833) — velero-io/velero
- [#9835 Backup deletion for block data mover](https://github.com/velero-io/velero/issues/9835) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#9964 backup-finalizer retries forever when object-store PUT hits a non-retryable error (e.g. Azure BlobImmutableDueToPolicy 409)](https://github.com/velero-io/velero/issues/9964) — velero-io/velero
- [#10265 Technical Debt: Remove `context.TODO()` in `pkg/util/kube and pkg/util/podvolume`](https://github.com/velero-io/velero/issues/10265) — velero-io/velero
- [#10266 docs: how to run CSI e2e specs against a local Kind cluster](https://github.com/velero-io/velero/issues/10266) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero
- [#10199 Backup and Restore CRDs have no printer columns since the 2021 revert](https://github.com/velero-io/velero/issues/10199) — velero-io/velero
- [#8457 Configurable pull policy when `velero install`](https://github.com/velero-io/velero/issues/8457) — velero-io/velero
- [#8807 Support per-storageclass VSClass annotation](https://github.com/velero-io/velero/issues/8807) — velero-io/velero

**openshift** (3)
- [#2391 Follow up: simplify and document PodResources defaulting](https://github.com/openshift/oadp-operator/issues/2391) — openshift/oadp-operator
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#1832 e2e jobs for other repos](https://github.com/openshift/oadp-operator/issues/1832) — openshift/oadp-operator

**migtools** (14)
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
- [#168 Configurable VMB (and VMBT) cleanup after DataUpload Failed transition](https://github.com/migtools/kubevirt-datamover-controller/issues/168) — migtools/kubevirt-datamover-controller
- [#84 Implement concurrent data mover limiter for DU and DD controllers](https://github.com/migtools/kubevirt-datamover-controller/issues/84) — migtools/kubevirt-datamover-controller
- [#45 VM restore Progress's first-DataDownload grace period is anchored to restore start, not operation registration](https://github.com/migtools/kubevirt-datamover-plugin/issues/45) — migtools/kubevirt-datamover-plugin
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller

**Other** (9)
- [#481 Support using a later patch release than what's in go.mod](https://github.com/actions/setup-go/issues/481) — actions/setup-go
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#101 UDP support](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
- [#477 branchprotector: excluded branches retain existing protection instead of being removed](https://github.com/kubernetes-sigs/prow/issues/477) — kubernetes-sigs/prow
- [#2906 EFS should have snapshot function similar to EBS](https://github.com/aws/aws-sdk-go-v2/issues/2906) — aws/aws-sdk-go-v2
- [#22368 Facilitate ConfigMap rollouts / management](https://github.com/kubernetes/kubernetes/issues/22368) — kubernetes/kubernetes
- [#1997 [CNCF LFX Proposal] Velero CSI E2E Testing](https://github.com/cncf/mentoring/issues/1997) — cncf/mentoring
- [#148413 View multiple debug consoles side by side in editor areas](https://github.com/microsoft/vscode/issues/148413) — microsoft/vscode
## Issues Closed (25)

**velero-io** (6)
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#10300 Unified repo config dir resolves to unwritable /udmrepo when HOME=/ (arbitrary-UID / OpenShift non-root server)](https://github.com/velero-io/velero/issues/10300) — velero-io/velero
- [#10301 Dead code in repository maintenance: GenOptionMaintainMode/Full/Quick and overwrite*MaintainInterval are unreachable](https://github.com/velero-io/velero/issues/10301) — velero-io/velero
- [#10304 Block data mover: retained CBT base snapshots are never reclaimed at backup deletion (design L370-371/L474 unimplemented)](https://github.com/velero-io/velero/issues/10304) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#10046 fs-backup restore deadlocks at Init:0/1 on owner-restricted volumes — restore-wait init container ignores pod-level securityContext, falls back to hardcoded runAsUser 1000](https://github.com/velero-io/velero/issues/10046) — velero-io/velero

**openshift** (3)
- [#5333 e2e-oo permanently failing: fixture pins EOL integrated stream ocp/4.6, configresolver returns 400](https://github.com/openshift/ci-tools/issues/5333) — openshift/ci-tools
- [#2209 Feature request: Additive extraArgs for Velero server and node-agent](https://github.com/openshift/oadp-operator/issues/2209) — openshift/oadp-operator
- [#2236 Flaky E2E: DPA reconciliation race condition causes NoDefaultBackupLocation test failure](https://github.com/openshift/oadp-operator/issues/2236) — openshift/oadp-operator

**migtools** (13)
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#121 Spec.OperationTimeout is not honored by either DataUpload or DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/121) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller
- [#168 Configurable VMB (and VMBT) cleanup after DataUpload Failed transition](https://github.com/migtools/kubevirt-datamover-controller/issues/168) — migtools/kubevirt-datamover-controller
- [#171 DataUpload cleanup blocks reconcile worker when pod cleanup hasn't finished before PVC/PV cleanup](https://github.com/migtools/kubevirt-datamover-controller/issues/171) — migtools/kubevirt-datamover-controller
- [#45 VM restore Progress's first-DataDownload grace period is anchored to restore start, not operation registration](https://github.com/migtools/kubevirt-datamover-plugin/issues/45) — migtools/kubevirt-datamover-plugin
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller

**Other** (3)
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
- [#148413 View multiple debug consoles side by side in editor areas](https://github.com/microsoft/vscode/issues/148413) — microsoft/vscode
- [#176 Group my contributions by organization than by repository of the repos](https://github.com/kaovilai/kaovilai.pw/issues/176) — kaovilai/kaovilai.pw
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
