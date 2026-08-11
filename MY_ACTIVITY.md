# Activity Log

> **Period:** 2026-07-28 — 2026-08-11
> **Generated:** 2026-08-11 13:10:55 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 77 |
| PRs Opened | 98 |
| PRs Reviewed | 97 |
| Issues/PRs Commented | 41 |
| Issues Closed | 26 |

---

## PRs Merged (77)

**velero-io** (4)
- [#10221 1.17 Backport #10192: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10221) — velero-io/velero
- [#10224 1.18: Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10224) — velero-io/velero
- [#10047 Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10047) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero

**openshift** (38)
- [#404 [oadp-1.5] OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/404) — openshift/openshift-velero-plugin
- [#2366 [oadp-1.4] OADP-7829: Add additive extraArgs support for Velero server and node-agent](https://github.com/openshift/oadp-operator/pull/2366) — openshift/oadp-operator
- [#83124 ixney on 5.1ney (rebased)](https://github.com/openshift/release/pull/83124) — openshift/release
- [#83078 Add e2e-test-kubevirt-aws presubmit for oadp-dev 5.0](https://github.com/openshift/release/pull/83078) — openshift/release
- [#83110 Promote oadp-operator bundle/index/e2e-test-binary images (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83110) — openshift/release
- [#2208 OADP-7943, OADP-7829: Fix DPA annotation changes not triggering reconciliation](https://github.com/openshift/oadp-operator/pull/2208) — openshift/oadp-operator
- [#434 OADP-6536: Call WaitGroup.Done() once only when PVB changes to final status the first time to avoid panic](https://github.com/openshift/velero/pull/434) — openshift/velero
- [#2353 Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2353) — openshift/oadp-operator
- [#2352 Add datadownloads RBAC to kubevirt-datamover ClusterRole](https://github.com/openshift/oadp-operator/pull/2352) — openshift/oadp-operator
- [#82762 Add CI image substitutions for OADP plugin images (base_images + operator.substitutions)](https://github.com/openshift/release/pull/82762) — openshift/release
- [#2340 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2340) — openshift/oadp-operator
- [#460 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/460) — openshift/openshift-velero-plugin
- [#458 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/458) — openshift/openshift-velero-plugin
- [#150 Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/150) — openshift/oadp-must-gather
- [#459 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/459) — openshift/openshift-velero-plugin
- [#82764 Bump openshift-velero-plugin CI memory limit from 4Gi to 8Gi](https://github.com/openshift/release/pull/82764) — openshift/release
- [#2344 Add missing image-producing repo badges to README](https://github.com/openshift/oadp-operator/pull/2344) — openshift/oadp-operator
- [#2341 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2341) — openshift/oadp-operator
- [#2342 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2342) — openshift/oadp-operator
- [#559 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/559) — openshift/velero
- [#561 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/561) — openshift/velero
- [#557 Remove inactive users from OWNERS](https://github.com/openshift/velero/pull/557) — openshift/velero
- [#82747 Remove unused releases: blocks from OADP ci-operator configs](https://github.com/openshift/release/pull/82747) — openshift/release
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/161) — openshift/velero-plugin-for-microsoft-azure
- [#76 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/76) — openshift/velero-plugin-for-legacy-aws
- [#75 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/75) — openshift/velero-plugin-for-legacy-aws
- [#74 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/74) — openshift/velero-plugin-for-legacy-aws
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/162) — openshift/velero-plugin-for-gcp
- [#154 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/154) — openshift/oadp-must-gather
- [#153 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/153) — openshift/oadp-must-gather
- [#155 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/155) — openshift/oadp-must-gather
- [#152 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/152) — openshift/oadp-must-gather
- [#77 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/77) — openshift/velero-plugin-for-legacy-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/161) — openshift/velero-plugin-for-aws
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/162) — openshift/velero-plugin-for-microsoft-azure
- [#560 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/560) — openshift/velero
- [#5329 pkg/steps: pin bundle builds to amd64 nodes](https://github.com/openshift/ci-tools/pull/5329) — openshift/ci-tools
- [#2313 Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2313) — openshift/oadp-operator

**migtools** (11)
- [#170 fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/170) — migtools/kubevirt-datamover-controller
- [#44 Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/44) — migtools/kubevirt-datamover-plugin
- [#41 Add RestoreItemAction plugins to trigger kubevirt datamover restore](https://github.com/migtools/kubevirt-datamover-plugin/pull/41) — migtools/kubevirt-datamover-plugin
- [#371 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/371) — migtools/oadp-non-admin
- [#40 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/40) — migtools/kubevirt-datamover-plugin
- [#157 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/157) — migtools/kubevirt-datamover-controller
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#143 oadp-1.6: Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/143) — migtools/kubevirt-datamover-controller
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#142 Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/142) — migtools/kubevirt-datamover-controller
- [#115 feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/115) — migtools/kubevirt-datamover-controller

**Other** (24)
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
- [#3 Follow-up fixes for #967 subagent routing opt-out and provenance scoping](https://github.com/kaovilai/context-mode/pull/3) — kaovilai/context-mode
- [#2 Reduce permission-classifier false positives on injected subagent routing block](https://github.com/kaovilai/context-mode/pull/2) — kaovilai/context-mode
- [#148 Group Dependabot updates per ecosystem](https://github.com/kaovilai/github-bot-command-palette/pull/148) — kaovilai/github-bot-command-palette
- [#138 Add structured payload picker dialog (stacked on #137)](https://github.com/kaovilai/github-bot-command-palette/pull/138) — kaovilai/github-bot-command-palette
- [#137 Add OpenShift static command profiles (payload, verified, jira, labels, specialized)](https://github.com/kaovilai/github-bot-command-palette/pull/137) — kaovilai/github-bot-command-palette
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
- [#2 Add PAT-free gh-aw agentic workflows](https://github.com/kaovilai/redirector/pull/2) — kaovilai/redirector
- [#1 Add Dependabot config with grouped PRs](https://github.com/kaovilai/redirector/pull/1) — kaovilai/redirector
- [#2 Implement Route 127 trailer strategy calculator as a static GitHub Pages site](https://github.com/kaovilai/route-127-trailer-nc/pull/2) — kaovilai/route-127-trailer-nc
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
## PRs Opened (98)

**velero-io** (8)
- [#10224 1.18: Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10224) — velero-io/velero
- [#10223 [release-1.17] Backport #10047: Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10223) — velero-io/velero
- [#10222 1.18 Backport: correct typos in log messages and status strings (#10192)](https://github.com/velero-io/velero/pull/10222) — velero-io/velero
- [#10221 1.17 Backport #10192: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10221) — velero-io/velero
- [#10220 Group Dependabot GitHub Actions updates](https://github.com/velero-io/velero/pull/10220) — velero-io/velero
- [#10211 backport: add pre-merge label-on-comment support; add copilot-instructions and auto-labeler for changelog exemptions](https://github.com/velero-io/velero/pull/10211) — velero-io/velero
- [#10210 Fix explicitly excluded namespaces still tracked via LabelSelector/OrLabelSelector match](https://github.com/velero-io/velero/pull/10210) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero

**openshift** (45)
- [#83221 gather-must-gather: retry camgi download, don't fail gather on it](https://github.com/openshift/release/pull/83221) — openshift/release
- [#2368 [oadp-1.4] Make controller-gen/kustomize/golangci-lint version checks reliable](https://github.com/openshift/oadp-operator/pull/2368) — openshift/oadp-operator
- [#2367 Make controller-gen/kustomize/golangci-lint version checks reliable](https://github.com/openshift/oadp-operator/pull/2367) — openshift/oadp-operator
- [#2366 [oadp-1.4] OADP-7829: Add additive extraArgs support for Velero server and node-agent](https://github.com/openshift/oadp-operator/pull/2366) — openshift/oadp-operator
- [#83124 ixney on 5.1ney (rebased)](https://github.com/openshift/release/pull/83124) — openshift/release
- [#83110 Promote oadp-operator bundle/index/e2e-test-binary images (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83110) — openshift/release
- [#83078 Add e2e-test-kubevirt-aws presubmit for oadp-dev 5.0](https://github.com/openshift/release/pull/83078) — openshift/release
- [#83049 Run oadp-operator e2e against kdm-controller/kdm-plugin PRs (oadp-dev, oadp-1.6)](https://github.com/openshift/release/pull/83049) — openshift/release
- [#2360 docs: kubevirt-datamover design doc — 2026-08-06 implementation status](https://github.com/openshift/oadp-operator/pull/2360) — openshift/oadp-operator
- [#2358 [oadp-1.4] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2358) — openshift/oadp-operator
- [#2357 [oadp-1.5] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2357) — openshift/oadp-operator
- [#2353 Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2353) — openshift/oadp-operator
- [#2352 Add datadownloads RBAC to kubevirt-datamover ClusterRole](https://github.com/openshift/oadp-operator/pull/2352) — openshift/oadp-operator
- [#2350 Add e2e coverage for kubevirt-datamover VM backup/restore: multi-PVC, incremental sequence, and CBT restore](https://github.com/openshift/oadp-operator/pull/2350) — openshift/oadp-operator
- [#5354 Support github_merge_blocks_policy in per-repo supplemental prow config](https://github.com/openshift/ci-tools/pull/5354) — openshift/ci-tools
- [#2346 docs: add CI plugin image sync guidance to common.go](https://github.com/openshift/oadp-operator/pull/2346) — openshift/oadp-operator
- [#82764 Bump openshift-velero-plugin CI memory limit from 4Gi to 8Gi](https://github.com/openshift/release/pull/82764) — openshift/release
- [#2345 Add CI plugin image substitution guide and developer comments](https://github.com/openshift/oadp-operator/pull/2345) — openshift/oadp-operator
- [#82762 Add CI image substitutions for OADP plugin images (base_images + operator.substitutions)](https://github.com/openshift/release/pull/82762) — openshift/release
- [#2344 Add missing image-producing repo badges to README](https://github.com/openshift/oadp-operator/pull/2344) — openshift/oadp-operator
- [#82747 Remove unused releases: blocks from OADP ci-operator configs](https://github.com/openshift/release/pull/82747) — openshift/release
- [#77 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/77) — openshift/velero-plugin-for-legacy-aws
- [#76 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/76) — openshift/velero-plugin-for-legacy-aws
- [#75 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/75) — openshift/velero-plugin-for-legacy-aws
- [#74 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/74) — openshift/velero-plugin-for-legacy-aws
- [#155 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/155) — openshift/oadp-must-gather
- [#154 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/154) — openshift/oadp-must-gather
- [#153 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/153) — openshift/oadp-must-gather
- [#152 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/152) — openshift/oadp-must-gather
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/162) — openshift/velero-plugin-for-gcp
- [#460 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/460) — openshift/openshift-velero-plugin
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/162) — openshift/velero-plugin-for-microsoft-azure
- [#459 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/459) — openshift/openshift-velero-plugin
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/161) — openshift/velero-plugin-for-microsoft-azure
- [#458 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/458) — openshift/openshift-velero-plugin
- [#73 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/73) — openshift/velero-plugin-for-legacy-aws
- [#72 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/72) — openshift/velero-plugin-for-legacy-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/161) — openshift/velero-plugin-for-aws
- [#2342 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2342) — openshift/oadp-operator
- [#2341 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2341) — openshift/oadp-operator
- [#2340 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2340) — openshift/oadp-operator
- [#561 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/561) — openshift/velero
- [#560 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/560) — openshift/velero
- [#559 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/559) — openshift/velero
- [#557 Remove inactive users from OWNERS](https://github.com/openshift/velero/pull/557) — openshift/velero

**migtools** (13)
- [#170 fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/170) — migtools/kubevirt-datamover-controller
- [#44 Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/44) — migtools/kubevirt-datamover-plugin
- [#373 Document NADR (NonAdminDownloadRequest) usage](https://github.com/migtools/oadp-non-admin/pull/373) — migtools/oadp-non-admin
- [#41 Add RestoreItemAction plugins to trigger kubevirt datamover restore](https://github.com/migtools/kubevirt-datamover-plugin/pull/41) — migtools/kubevirt-datamover-plugin
- [#253 Fix #252: Add exact-output assertion for schedule create example normalization](https://github.com/migtools/oadp-cli/pull/253) — migtools/oadp-cli
- [#48 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/48) — migtools/kopia
- [#40 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/40) — migtools/kubevirt-datamover-plugin
- [#157 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/157) — migtools/kubevirt-datamover-controller
- [#251 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/251) — migtools/oadp-cli
- [#371 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/371) — migtools/oadp-non-admin
- [#47 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/47) — migtools/kopia
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#149 Cherry-pick #131: Azure BSL support to oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/149) — migtools/kubevirt-datamover-controller

**Other** (32)
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
- [#174 Addressing date and time display per browser timezone](https://github.com/kaovilai/kaovilai.pw/pull/174) — kaovilai/kaovilai.pw
- [#1034 fix(routing): self-identify subagent routing block, add opt-out (#967)](https://github.com/mksglu/context-mode/pull/1034) — mksglu/context-mode
- [#3 Follow-up fixes for #967 subagent routing opt-out and provenance scoping](https://github.com/kaovilai/context-mode/pull/3) — kaovilai/context-mode
- [#2 Reduce permission-classifier false positives on injected subagent routing block](https://github.com/kaovilai/context-mode/pull/2) — kaovilai/context-mode
- [#148 Group Dependabot updates per ecosystem](https://github.com/kaovilai/github-bot-command-palette/pull/148) — kaovilai/github-bot-command-palette
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
- [#1 fix: enforce Spec.OperationTimeout in DataUpload/DataDownload controllers](https://github.com/kaovilai/kubevirt-datamover-controller/pull/1) — kaovilai/kubevirt-datamover-controller
- [#3 Add design docs for one-click community rule install via marketplace deep links](https://github.com/kaovilai/redirector/pull/3) — kaovilai/redirector
- [#2 Add PAT-free gh-aw agentic workflows](https://github.com/kaovilai/redirector/pull/2) — kaovilai/redirector
- [#1 Add Dependabot config with grouped PRs](https://github.com/kaovilai/redirector/pull/1) — kaovilai/redirector
- [#2 Implement Route 127 trailer strategy calculator as a static GitHub Pages site](https://github.com/kaovilai/route-127-trailer-nc/pull/2) — kaovilai/route-127-trailer-nc
- [#138 Add structured payload picker dialog (stacked on #137)](https://github.com/kaovilai/github-bot-command-palette/pull/138) — kaovilai/github-bot-command-palette
- [#137 Add OpenShift static command profiles (payload, verified, jira, labels, specialized)](https://github.com/kaovilai/github-bot-command-palette/pull/137) — kaovilai/github-bot-command-palette
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
- [#552 ⚡ Bolt: [performance improvement] Replace find subprocesses with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/552) — kaovilai/dotfiles
- [#551 ⚡ Bolt: Remove redundant manual compinit](https://github.com/kaovilai/dotfiles/pull/551) — kaovilai/dotfiles
- [#550 ⚡ Bolt: [performance improvement] Remove redundant manual compinit execution](https://github.com/kaovilai/dotfiles/pull/550) — kaovilai/dotfiles
## PRs Reviewed (97)

**velero-io** (31)
- [#10228 docs: fix grammar and typos in backup-restore-windows](https://github.com/velero-io/velero/pull/10228) — velero-io/velero
- [#10200 Add printer columns for Backup and Restore CRDs](https://github.com/velero-io/velero/pull/10200) — velero-io/velero
- [#10189 Make backupType case insensitive in the CLI.](https://github.com/velero-io/velero/pull/10189) — velero-io/velero
- [#10190 docs: fix grammar and typos in customize-installation](https://github.com/velero-io/velero/pull/10190) — velero-io/velero
- [#10203 Bump github/codeql-action from 4.37.3 to 4.37.6](https://github.com/velero-io/velero/pull/10203) — velero-io/velero
- [#10202 Bump actions/setup-go from 6 to 7](https://github.com/velero-io/velero/pull/10202) — velero-io/velero
- [#10196 test: add unit tests for boolptr and stringptr utilities](https://github.com/velero-io/velero/pull/10196) — velero-io/velero
- [#10192 fix: correct typos in log messages and status strings](https://github.com/velero-io/velero/pull/10192) — velero-io/velero
- [#10208 Re-request maintainer review when only one CODEOWNERS approval exists](https://github.com/velero-io/velero/pull/10208) — velero-io/velero
- [#10210 Fix explicitly excluded namespaces still tracked via LabelSelector/OrLabelSelector match](https://github.com/velero-io/velero/pull/10210) — velero-io/velero
- [#10158 ci: add backport/cherry-pick GitHub Action for release branches](https://github.com/velero-io/velero/pull/10158) — velero-io/velero
- [#10159 Fix excluded namespace objects leaking into backup with cross-namespa…](https://github.com/velero-io/velero/pull/10159) — velero-io/velero
- [#10162 [release-1.16] Fix ResourceDeletionStatusTracker key Kind mismatch in terminating-namespace wait (#9987)](https://github.com/velero-io/velero/pull/10162) — velero-io/velero
- [#10102 Verify extracted item paths stay inside the backup directory](https://github.com/velero-io/velero/pull/10102) — velero-io/velero
- [#10096 feat(e2e) :- add E2E test for BSL ReadOnly mode validation](https://github.com/velero-io/velero/pull/10096) — velero-io/velero
- [#10104 Update Restore Exposer and PVC CSI to support in-place restore](https://github.com/velero-io/velero/pull/10104) — velero-io/velero
- [#10121 Enhancement: fail-fast on velero install wait](https://github.com/velero-io/velero/pull/10121) — velero-io/velero
- [#10163 [release-1.17] Fix ResourceDeletionStatusTracker key Kind mismatch in terminating-namespace wait (#9987)](https://github.com/velero-io/velero/pull/10163) — velero-io/velero
- [#10119 Fix csi pvc restore action](https://github.com/velero-io/velero/pull/10119) — velero-io/velero
- [#10132 Do not assume a port name is a string when clearing node ports](https://github.com/velero-io/velero/pull/10132) — velero-io/velero
- [#10127 feat(cli): add velero client set-context-as-velero-namespace command](https://github.com/velero-io/velero/pull/10127) — velero-io/velero
- [#10147 docs: document ownership loss on mount-constant filesystems](https://github.com/velero-io/velero/pull/10147) — velero-io/velero
- [#10157 docs: update community page backlog links away from classic projects](https://github.com/velero-io/velero/pull/10157) — velero-io/velero
- [#10103 Add regression test for additional item with invalid JSON](https://github.com/velero-io/velero/pull/10103) — velero-io/velero
- [#10106 Fix some issues for CBT features:](https://github.com/velero-io/velero/pull/10106) — velero-io/velero
- [#10098 Implement server default restore resource modifier](https://github.com/velero-io/velero/pull/10098) — velero-io/velero
- [#10135 Bump github/codeql-action from 3 to 4.37.3](https://github.com/velero-io/velero/pull/10135) — velero-io/velero
- [#10097 feat(e2e) :- add E2E test for restore hook failure policies](https://github.com/velero-io/velero/pull/10097) — velero-io/velero
- [#10123 Feature: Add support for server args to velero install Deployment](https://github.com/velero-io/velero/pull/10123) — velero-io/velero
- [#10110 refactor(serverstatus): Remove outdated Kubernetes v1.9.0 workaround](https://github.com/velero-io/velero/pull/10110) — velero-io/velero
- [#10090 fix(kopia): fix block restore write loop slice bounds](https://github.com/velero-io/velero/pull/10090) — velero-io/velero

**openshift** (29)
- [#2370 [oadp-1.6] feat: expose staleDataUploadThreshold in DPA KubevirtDatamoverConfig](https://github.com/openshift/oadp-operator/pull/2370) — openshift/oadp-operator
- [#2361 feat: expose staleDataUploadThreshold in DPA KubevirtDatamoverConfig](https://github.com/openshift/oadp-operator/pull/2361) — openshift/oadp-operator
- [#83117 ixney on 5.1ney](https://github.com/openshift/release/pull/83117) — openshift/release
- [#2356 [oadp-1.6] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2356) — openshift/oadp-operator
- [#2349 feat: use velero SA and add bound-sa-token volume for KDM controller](https://github.com/openshift/oadp-operator/pull/2349) — openshift/oadp-operator
- [#2359 [oadp-1.6] feat: use velero SA and add bound-sa-token volume for KDM controller](https://github.com/openshift/oadp-operator/pull/2359) — openshift/oadp-operator
- [#2328 [oadp-1.6] Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2328) — openshift/oadp-operator
- [#158 [oadp-1.4] Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/158) — openshift/oadp-must-gather
- [#159 [oadp-1.6] Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/159) — openshift/oadp-must-gather
- [#82902 tide: set github_merge_blocks_policy to block for OADP repos](https://github.com/openshift/release/pull/82902) — openshift/release
- [#2329 [oadp-1.5] Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2329) — openshift/oadp-operator
- [#151 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/151) — openshift/oadp-must-gather
- [#2330 Merge https://github.com/openshift/oadp-operator:oadp-1.5 (a9247ea) into oadp-1.5](https://github.com/openshift/oadp-operator/pull/2330) — openshift/oadp-operator
- [#456 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/456) — openshift/openshift-velero-plugin
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/159) — openshift/velero-plugin-for-gcp
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/160) — openshift/velero-plugin-for-microsoft-azure
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/160) — openshift/velero-plugin-for-gcp
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/159) — openshift/velero-plugin-for-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/161) — openshift/velero-plugin-for-gcp
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/159) — openshift/velero-plugin-for-microsoft-azure
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/160) — openshift/velero-plugin-for-aws
- [#558 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/558) — openshift/velero
- [#2339 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2339) — openshift/oadp-operator
- [#457 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/457) — openshift/openshift-velero-plugin
- [#70 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/70) — openshift/velero-plugin-for-legacy-aws
- [#2338 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2338) — openshift/oadp-operator
- [#158 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/158) — openshift/velero-plugin-for-aws
- [#2337 update TROUBLESHOOTING.md to use oc oadp CLI instead of velero pod -exec alias](https://github.com/openshift/oadp-operator/pull/2337) — openshift/oadp-operator
- [#2331 docs: fix links, restic refs, and typos in examples and root-level docs](https://github.com/openshift/oadp-operator/pull/2331) — openshift/oadp-operator

**migtools** (32)
- [#177 [oadp-1.6] fix: defer PVC/PV cleanup while datamover pod terminates](https://github.com/migtools/kubevirt-datamover-controller/pull/177) — migtools/kubevirt-datamover-controller
- [#178 [oadp-1.6] feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/178) — migtools/kubevirt-datamover-controller
- [#167 feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/167) — migtools/kubevirt-datamover-controller
- [#46 [oadp-1.6] Clear PVC binding state and halt kubevirt VMs at restore time](https://github.com/migtools/kubevirt-datamover-plugin/pull/46) — migtools/kubevirt-datamover-plugin
- [#172 feat: add staleness check for per-VM DataUpload serialization](https://github.com/migtools/kubevirt-datamover-controller/pull/172) — migtools/kubevirt-datamover-controller
- [#176 [oadp-1.6] issue #98: inject Azure Workload Identity env vars into datamover pods](https://github.com/migtools/kubevirt-datamover-controller/pull/176) — migtools/kubevirt-datamover-controller
- [#166 feat: add BSL config parity with Velero AWS plugin](https://github.com/migtools/kubevirt-datamover-controller/pull/166) — migtools/kubevirt-datamover-controller
- [#164 fix: handle hyphenated disk names in extractDiskName](https://github.com/migtools/kubevirt-datamover-controller/pull/164) — migtools/kubevirt-datamover-controller
- [#255 Remove dead oadp-operator replace directive](https://github.com/migtools/oadp-cli/pull/255) — migtools/oadp-cli
- [#372 ⬆ Bump hadolint/hadolint-action from 3.1.0 to 3.4.0](https://github.com/migtools/oadp-non-admin/pull/372) — migtools/oadp-non-admin
- [#161 [oadp-1.6] feat: add bound-sa-token projected volume to datamover pod for STS auth](https://github.com/migtools/kubevirt-datamover-controller/pull/161) — migtools/kubevirt-datamover-controller
- [#158 feat: add bound-sa-token projected volume to datamover pod for STS auth](https://github.com/migtools/kubevirt-datamover-controller/pull/158) — migtools/kubevirt-datamover-controller
- [#242 Merge https://github.com/migtools/oadp-cli:oadp-1.4 (2c406b4) into oadp-1.4](https://github.com/migtools/oadp-cli/pull/242) — migtools/oadp-cli
- [#156 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/156) — migtools/kubevirt-datamover-controller
- [#247 [oadp-1.4] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/247) — migtools/oadp-cli
- [#245 [oadp-1.6] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/245) — migtools/oadp-cli
- [#246 [oadp-1.5] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/246) — migtools/oadp-cli
- [#34 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vmdp/pull/34) — migtools/oadp-vmdp
- [#32 Remove inactive users from OWNERS](https://github.com/migtools/filebrowser/pull/32) — migtools/filebrowser
- [#33 Remove inactive users from OWNERS](https://github.com/migtools/filebrowser/pull/33) — migtools/filebrowser
- [#249 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/249) — migtools/oadp-cli
- [#97 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vm-file-restore/pull/97) — migtools/oadp-vm-file-restore
- [#35 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vmdp/pull/35) — migtools/oadp-vmdp
- [#370 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/370) — migtools/oadp-non-admin
- [#46 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/46) — migtools/kopia
- [#250 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/250) — migtools/oadp-cli
- [#248 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/248) — migtools/oadp-cli
- [#96 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vm-file-restore/pull/96) — migtools/oadp-vm-file-restore
- [#39 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/39) — migtools/kubevirt-datamover-plugin
- [#369 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/369) — migtools/oadp-non-admin
- [#45 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/45) — migtools/kopia
- [#180 Remove inactive users from OWNERS](https://github.com/migtools/udistribution/pull/180) — migtools/udistribution

**Other** (5)
- [#13 Exclude README.md from protected-files denylist in daily-upstream-parity workflow](https://github.com/kaovilai/oadp-ui/pull/13) — kaovilai/oadp-ui
- [#168 [ImgBot] Optimize images](https://github.com/kaovilai/kaovilai.pw/pull/168) — kaovilai/kaovilai.pw
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
- [#3 Add design docs for one-click community rule install via marketplace deep links](https://github.com/kaovilai/redirector/pull/3) — kaovilai/redirector
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
## Issues/PRs Commented On (41)

**velero-io** (16)
- [#8457 Configurable pull policy when `velero install`](https://github.com/velero-io/velero/issues/8457) — velero-io/velero
- [#10199 Backup and Restore CRDs have no printer columns since the 2021 revert](https://github.com/velero-io/velero/issues/10199) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#8807 Support per-storageclass VSClass annotation](https://github.com/velero-io/velero/issues/8807) — velero-io/velero
- [#10120 Enhancement: Fail-fast in `velero install --wait` on Deployment ReplicaFailure](https://github.com/velero-io/velero/issues/10120) — velero-io/velero
- [#10026 Restore logs endless watch errors for API groups without watch support (e.g. authorization.openshift.io)](https://github.com/velero-io/velero/issues/10026) — velero-io/velero
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#8686 Avoid overwriting during backup to support object lock enabled buckets](https://github.com/velero-io/velero/issues/8686) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#3194 Have the Velero CLI use the active namespace in the current context](https://github.com/velero-io/velero/issues/3194) — velero-io/velero
- [#9965 Add safe auto-merge workflow for high-confidence Dependabot PRs](https://github.com/velero-io/velero/issues/9965) — velero-io/velero
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#8466 Velero doesnt do well with Minio bucket versioning ](https://github.com/velero-io/velero/issues/8466) — velero-io/velero
- [#9957 `VolumeSnapshotContent` resources are forcefully restored, ignoring `includedResources` and `excludedResources` filters](https://github.com/velero-io/velero/issues/9957) — velero-io/velero
- [#10092 Deprecate the block volume backup/restore functionality through Kopia file system uploader](https://github.com/velero-io/velero/issues/10092) — velero-io/velero
- [#9600 Deprecation: Remove `BackupStorageLocation.Spec.ObjectStorage.CACert` inline field in favor of `CACertRef` secret reference](https://github.com/velero-io/velero/issues/9600) — velero-io/velero

**openshift** (2)
- [#1832 e2e jobs for other repos](https://github.com/openshift/oadp-operator/issues/1832) — openshift/oadp-operator
- [#2343 Investigate making plugin repo changes immediately available for OADP-operator e2e tests](https://github.com/openshift/oadp-operator/issues/2343) — openshift/oadp-operator

**migtools** (15)
- [#168 Configurable VMB (and VMBT) cleanup after DataUpload Failed transition](https://github.com/migtools/kubevirt-datamover-controller/issues/168) — migtools/kubevirt-datamover-controller
- [#175 Implement concurrency limiter for DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/175) — migtools/kubevirt-datamover-controller
- [#84 Implement concurrent data mover limiter for DU and DD controllers](https://github.com/migtools/kubevirt-datamover-controller/issues/84) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#45 VM restore Progress's first-DataDownload grace period is anchored to restore start, not operation registration](https://github.com/migtools/kubevirt-datamover-plugin/issues/45) — migtools/kubevirt-datamover-plugin
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller
- [#120 Cancellation cleanup errors are logged but not propagated, phase moves to Canceled regardless](https://github.com/migtools/kubevirt-datamover-controller/issues/120) — migtools/kubevirt-datamover-controller
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#160 Checkpoint index records requested PVC size, not actual PV capacity, undersizing restore scratch space](https://github.com/migtools/kubevirt-datamover-controller/issues/160) — migtools/kubevirt-datamover-controller

**Other** (8)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#1997 [CNCF LFX Proposal] Velero CSI E2E Testing](https://github.com/cncf/mentoring/issues/1997) — cncf/mentoring
- [#148413 View multiple debug consoles side by side in editor areas](https://github.com/microsoft/vscode/issues/148413) — microsoft/vscode
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#132 Dynamic Prow Plugin Detection per Repo](https://github.com/kaovilai/github-bot-command-palette/issues/132) — kaovilai/github-bot-command-palette
- [#736 Tide status controller falsely reports "In merge pool." for PRs blocked by a never-triggered required context](https://github.com/kubernetes-sigs/prow/issues/736) — kubernetes-sigs/prow
- [#110 [improve] Performance: add Vite manual chunk splitting for better browser caching](https://github.com/kaovilai/kaovilai.pw/issues/110) — kaovilai/kaovilai.pw
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
## Issues Closed (26)

**velero-io** (6)
- [#10046 fs-backup restore deadlocks at Init:0/1 on owner-restricted volumes — restore-wait init container ignores pod-level securityContext, falls back to hardcoded runAsUser 1000](https://github.com/velero-io/velero/issues/10046) — velero-io/velero
- [#9603 Backport/Cherry-pick GitHub action](https://github.com/velero-io/velero/issues/9603) — velero-io/velero
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#10099 Update velero.io community pages](https://github.com/velero-io/velero/issues/10099) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#10022 Flaky unit test:  TestBlockUploaderBackup/success_full_backup](https://github.com/velero-io/velero/issues/10022) — velero-io/velero

**openshift** (5)
- [#2209 Feature request: Additive extraArgs for Velero server and node-agent](https://github.com/openshift/oadp-operator/issues/2209) — openshift/oadp-operator
- [#2236 Flaky E2E: DPA reconciliation race condition causes NoDefaultBackupLocation test failure](https://github.com/openshift/oadp-operator/issues/2236) — openshift/oadp-operator
- [#2351 kubevirt-datamover ClusterRole missing RBAC for Phase 3 (DataDownload) support](https://github.com/openshift/oadp-operator/issues/2351) — openshift/oadp-operator
- [#149 Gather PVC/PV/Namespace(SCC) data for backed-up/restored app namespaces to diagnose restore permission/ownership bugs](https://github.com/openshift/oadp-must-gather/issues/149) — openshift/oadp-must-gather
- [#5328 src-bundle build flake: no node selector lets buildah pod land on arm64 node, fails pulling amd64-only pipeline:src manifest list](https://github.com/openshift/ci-tools/issues/5328) — openshift/ci-tools

**migtools** (5)
- [#168 Configurable VMB (and VMBT) cleanup after DataUpload Failed transition](https://github.com/migtools/kubevirt-datamover-controller/issues/168) — migtools/kubevirt-datamover-controller
- [#171 DataUpload cleanup blocks reconcile worker when pod cleanup hasn't finished before PVC/PV cleanup](https://github.com/migtools/kubevirt-datamover-controller/issues/171) — migtools/kubevirt-datamover-controller
- [#45 VM restore Progress's first-DataDownload grace period is anchored to restore start, not operation registration](https://github.com/migtools/kubevirt-datamover-plugin/issues/45) — migtools/kubevirt-datamover-plugin
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller
- [#160 Checkpoint index records requested PVC size, not actual PV capacity, undersizing restore scratch space](https://github.com/migtools/kubevirt-datamover-controller/issues/160) — migtools/kubevirt-datamover-controller

**Other** (10)
- [#148413 View multiple debug consoles side by side in editor areas](https://github.com/microsoft/vscode/issues/148413) — microsoft/vscode
- [#176 Group my contributions by organization than by repository of the repos](https://github.com/kaovilai/kaovilai.pw/issues/176) — kaovilai/kaovilai.pw
- [#147 group dependabot prs into ecosystems.. ie typescript, actions, etc.](https://github.com/kaovilai/github-bot-command-palette/issues/147) — kaovilai/github-bot-command-palette
- [#69 activity.json is not updated the same time as .md files.](https://github.com/kaovilai/kaovilai/issues/69) — kaovilai/kaovilai
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#1 Implement my gemini app into github pages static](https://github.com/kaovilai/route-127-trailer-nc/issues/1) — kaovilai/route-127-trailer-nc
- [#146 https://legacy.kaovilai.pw/pay-me this section has thai qr code payment info. add it to here](https://github.com/kaovilai/kaovilai.pw/issues/146) — kaovilai/kaovilai.pw
- [#67 Add JSON export alongside MY_ACTIVITY.md / MY_PULL_REQUESTS.md for site consumption](https://github.com/kaovilai/kaovilai/issues/67) — kaovilai/kaovilai
- [#74 gh aw compile isn't available in this environment prevent use gh aw install action](https://github.com/kaovilai/kaovilai.pw/issues/74) — kaovilai/kaovilai.pw
- [#1492 Move CRD installs out of Reconcile](https://github.com/stolostron/multiclusterhub-operator/issues/1492) — stolostron/multiclusterhub-operator
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
