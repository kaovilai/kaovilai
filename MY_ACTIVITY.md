# Activity Log

> **Period:** 2026-08-26 — 2026-09-09
> **Generated:** 2026-09-09 19:37:18 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 47 |
| PRs Opened | 51 |
| PRs Reviewed | 77 |
| Issues/PRs Commented | 33 |
| Issues Closed | 5 |

---

## PRs Merged (47)

**velero-io** (9)
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero
- [#10307 Fix generic CSI changeID retrieval and honor snapshot class deletion policy for CBT retention](https://github.com/velero-io/velero/pull/10307) — velero-io/velero
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero
- [#10403 Check both daemonsets before returning non-NotFound lookup error in IsReady](https://github.com/velero-io/velero/pull/10403) — velero-io/velero
- [#10406 release-1.17: validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10406) — velero-io/velero
- [#10381 1.18: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10381) — velero-io/velero
- [#10348 1.18: Backport #10342: Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10348) — velero-io/velero
- [#10407 1.18: Cherry-pick #10390: Validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10407) — velero-io/velero
- [#10409 Update community meeting links to LFX Zoom, add calendar](https://github.com/velero-io/velero/pull/10409) — velero-io/velero

**openshift** (13)
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release
- [#2435 fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2435) — openshift/oadp-operator
- [#84490 oadp-operator: split e2e-test-kubevirt-aws into kdm/non-kdm jobs (oadp-1.6)](https://github.com/openshift/release/pull/84490) — openshift/release
- [#2404 test: unpend two kdm restore PIts, fixing bugs found via live e2e validation](https://github.com/openshift/oadp-operator/pull/2404) — openshift/oadp-operator
- [#84337 oadp: split kubevirt e2e job (5.0) and add Claude failure analysis to kdm-controller/plugin](https://github.com/openshift/release/pull/84337) — openshift/release
- [#566 1.4: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/566) — openshift/velero
- [#2423 fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2423) — openshift/oadp-operator
- [#2139 OADP-7665: Pass --log-level to NodeAgent DaemonSet container args](https://github.com/openshift/oadp-operator/pull/2139) — openshift/oadp-operator
- [#2019 Add uploader-type argument to Velero deployment configuration when configuration.args is used.](https://github.com/openshift/oadp-operator/pull/2019) — openshift/oadp-operator
- [#2368 [oadp-1.4] Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2368) — openshift/oadp-operator
- [#2205 OADP-7943: Fix DPA annotation changes not triggering reconciliation](https://github.com/openshift/oadp-operator/pull/2205) — openshift/oadp-operator
- [#2367 Make controller-gen/kustomize/golangci-lint/envtest tool-binary caching reliable](https://github.com/openshift/oadp-operator/pull/2367) — openshift/oadp-operator
- [#84048 oadp-analyze-e2e-failure: give Claude explicit source-clone instructions](https://github.com/openshift/release/pull/84048) — openshift/release

**migtools** (4)
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller

**Other** (21)
- [#11 Handle client abort gracefully in streaming chat-completions](https://github.com/kaovilai/copilot-api/pull/11) — kaovilai/copilot-api
- [#10 Fix desktop typecheck failure (missing files in tsconfig.node.json)](https://github.com/kaovilai/copilot-api/pull/10) — kaovilai/copilot-api
- [#9 Fix streaming tool_calls with a non-zero starting index (crashes n8n's AI SDK)](https://github.com/kaovilai/copilot-api/pull/9) — kaovilai/copilot-api
- [#12 Land the CodeRabbit fixes that missed PR #11's merge](https://github.com/kaovilai/n8n-playwright/pull/12) — kaovilai/n8n-playwright
- [#8 Fix non-streaming chat-completions response missing required index/object/logprobs](https://github.com/kaovilai/copilot-api/pull/8) — kaovilai/copilot-api
- [#7 Add dev-branch Docker build/push workflow](https://github.com/kaovilai/copilot-api/pull/7) — kaovilai/copilot-api
- [#11 Consume the published @kaovilai fork in the Dockerfile instead of upstream's package](https://github.com/kaovilai/n8n-playwright/pull/11) — kaovilai/n8n-playwright
- [#10 Publish this fork's package to GitHub Packages (@kaovilai scope)](https://github.com/kaovilai/n8n-playwright/pull/10) — kaovilai/n8n-playwright
- [#9 Add browser session reuse across Playwright nodes, capped by memory budget](https://github.com/kaovilai/n8n-playwright/pull/9) — kaovilai/n8n-playwright
- [#8 Fix browser-close leak, update deps, add Dependabot auto-merge](https://github.com/kaovilai/n8n-playwright/pull/8) — kaovilai/n8n-playwright
- [#7 Bump n8n 2.0.3 -> 2.37.10, chromium stage alpine 3.22 -> 3.24](https://github.com/kaovilai/n8n-playwright/pull/7) — kaovilai/n8n-playwright
- [#6 Neuter setup-browsers.js -- n8n runs it at every boot, undoing the build-time fix](https://github.com/kaovilai/n8n-playwright/pull/6) — kaovilai/n8n-playwright
- [#4 Bake browsers at build time + add CI and Dependabot](https://github.com/kaovilai/n8n-playwright/pull/4) — kaovilai/n8n-playwright
- [#179 Improve mobile touch interactions and settings persistence](https://github.com/kaovilai/github-bot-command-palette/pull/179) — kaovilai/github-bot-command-palette
- [#178 Make auto-submit/combo path touch-friendly and add a form-submit fallback](https://github.com/kaovilai/github-bot-command-palette/pull/178) — kaovilai/github-bot-command-palette
- [#177 Add hover/click popups for Claude analysis links and failed-step logs](https://github.com/kaovilai/github-bot-command-palette/pull/177) — kaovilai/github-bot-command-palette
- [#176 Add per-command cancel-x to pending combo buttons](https://github.com/kaovilai/github-bot-command-palette/pull/176) — kaovilai/github-bot-command-palette
- [#175 Skip Test/Override buttons on tide's own status context](https://github.com/kaovilai/github-bot-command-palette/pull/175) — kaovilai/github-bot-command-palette
- [#174 Extend combo window to per-check Override, add pending-button spinner](https://github.com/kaovilai/github-bot-command-palette/pull/174) — kaovilai/github-bot-command-palette
- [#173 Combo auto-submit window, override on pending checks, native Approve sync](https://github.com/kaovilai/github-bot-command-palette/pull/173) — kaovilai/github-bot-command-palette
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
## PRs Opened (51)

**velero-io** (10)
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero
- [#10428 [release-1.14] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10428) — velero-io/velero
- [#10427 [release-1.15] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10427) — velero-io/velero
- [#10426 [release-1.18] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10426) — velero-io/velero
- [#10425 [release-1.17] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10425) — velero-io/velero
- [#10424 [release-1.16] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10424) — velero-io/velero
- [#10423 [release-1.16] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/velero-io/velero/pull/10423) — velero-io/velero
- [#10416 Fix re-request-review workflow token permissions for fork-originated PRs](https://github.com/velero-io/velero/pull/10416) — velero-io/velero
- [#10409 Update community meeting links to LFX Zoom, add calendar](https://github.com/velero-io/velero/pull/10409) — velero-io/velero
- [#10407 1.18: Cherry-pick #10390: Validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10407) — velero-io/velero

**openshift** (10)
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release
- [#2435 fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2435) — openshift/oadp-operator
- [#84490 oadp-operator: split e2e-test-kubevirt-aws into kdm/non-kdm jobs (oadp-1.6)](https://github.com/openshift/release/pull/84490) — openshift/release
- [#567 1.5: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/567) — openshift/velero
- [#566 1.4: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/566) — openshift/velero
- [#84337 oadp: split kubevirt e2e job (5.0) and add Claude failure analysis to kdm-controller/plugin](https://github.com/openshift/release/pull/84337) — openshift/release
- [#2423 fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2423) — openshift/oadp-operator
- [#84229 oadp-operator: bump e2e-test-kubevirt-aws timeout to 3h](https://github.com/openshift/release/pull/84229) — openshift/release
- [#84228 Add Depends-On cross-repo image build across the OADP ecosystem (KDM, oadp-operator, velero family)](https://github.com/openshift/release/pull/84228) — openshift/release
- [#565 OADP-7061: [oadp-1.5] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/openshift/velero/pull/565) — openshift/velero

**migtools** (6)
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#213 fix: speed up Dockerfile builds with cache mounts](https://github.com/migtools/kubevirt-datamover-controller/pull/213) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller
- [#206 fix: retry expected-backup-type annotation on conflict instead of giving up](https://github.com/migtools/kubevirt-datamover-controller/pull/206) — migtools/kubevirt-datamover-controller

**Other** (25)
- [#11 Handle client abort gracefully in streaming chat-completions](https://github.com/kaovilai/copilot-api/pull/11) — kaovilai/copilot-api
- [#10 Fix desktop typecheck failure (missing files in tsconfig.node.json)](https://github.com/kaovilai/copilot-api/pull/10) — kaovilai/copilot-api
- [#9 Fix streaming tool_calls with a non-zero starting index (crashes n8n's AI SDK)](https://github.com/kaovilai/copilot-api/pull/9) — kaovilai/copilot-api
- [#8 Fix non-streaming chat-completions response missing required index/object/logprobs](https://github.com/kaovilai/copilot-api/pull/8) — kaovilai/copilot-api
- [#7 Add dev-branch Docker build/push workflow](https://github.com/kaovilai/copilot-api/pull/7) — kaovilai/copilot-api
- [#12 Land the CodeRabbit fixes that missed PR #11's merge](https://github.com/kaovilai/n8n-playwright/pull/12) — kaovilai/n8n-playwright
- [#11 Consume the published @kaovilai fork in the Dockerfile instead of upstream's package](https://github.com/kaovilai/n8n-playwright/pull/11) — kaovilai/n8n-playwright
- [#10 Publish this fork's package to GitHub Packages (@kaovilai scope)](https://github.com/kaovilai/n8n-playwright/pull/10) — kaovilai/n8n-playwright
- [#9 Add browser session reuse across Playwright nodes, capped by memory budget](https://github.com/kaovilai/n8n-playwright/pull/9) — kaovilai/n8n-playwright
- [#8 Fix browser-close leak, update deps, add Dependabot auto-merge](https://github.com/kaovilai/n8n-playwright/pull/8) — kaovilai/n8n-playwright
- [#7 Bump n8n 2.0.3 -> 2.37.10, chromium stage alpine 3.22 -> 3.24](https://github.com/kaovilai/n8n-playwright/pull/7) — kaovilai/n8n-playwright
- [#6 Neuter setup-browsers.js -- n8n runs it at every boot, undoing the build-time fix](https://github.com/kaovilai/n8n-playwright/pull/6) — kaovilai/n8n-playwright
- [#5 Add CI (lint+build) and Dependabot config](https://github.com/kaovilai/n8n-playwright/pull/5) — kaovilai/n8n-playwright
- [#4 Bake browsers at build time + add CI and Dependabot](https://github.com/kaovilai/n8n-playwright/pull/4) — kaovilai/n8n-playwright
- [#179 Improve mobile touch interactions and settings persistence](https://github.com/kaovilai/github-bot-command-palette/pull/179) — kaovilai/github-bot-command-palette
- [#178 Make auto-submit/combo path touch-friendly and add a form-submit fallback](https://github.com/kaovilai/github-bot-command-palette/pull/178) — kaovilai/github-bot-command-palette
- [#177 Add hover/click popups for Claude analysis links and failed-step logs](https://github.com/kaovilai/github-bot-command-palette/pull/177) — kaovilai/github-bot-command-palette
- [#176 Add per-command cancel-x to pending combo buttons](https://github.com/kaovilai/github-bot-command-palette/pull/176) — kaovilai/github-bot-command-palette
- [#175 Skip Test/Override buttons on tide's own status context](https://github.com/kaovilai/github-bot-command-palette/pull/175) — kaovilai/github-bot-command-palette
- [#174 Extend combo window to per-check Override, add pending-button spinner](https://github.com/kaovilai/github-bot-command-palette/pull/174) — kaovilai/github-bot-command-palette
- [#173 Combo auto-submit window, override on pending checks, native Approve sync](https://github.com/kaovilai/github-bot-command-palette/pull/173) — kaovilai/github-bot-command-palette
- [#4552 Fix conversion webhook crash on legacy featureGates empty-object shape](https://github.com/kubevirt/hyperconverged-cluster-operator/pull/4552) — kubevirt/hyperconverged-cluster-operator
- [#18957 storage/cbt: fix stale reconcile overwriting a completed VMBackup with SourceLost](https://github.com/kubevirt/kubevirt/pull/18957) — kubevirt/kubevirt
- [#18949 storage/cbt: fix VMBackup status freeze during target PVC attach](https://github.com/kubevirt/kubevirt/pull/18949) — kubevirt/kubevirt
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
## PRs Reviewed (77)

**velero-io** (9)
- [#10479 Report incremental fallback message](https://github.com/velero-io/velero/pull/10479) — velero-io/velero
- [#10436 Add block data mover support for Velero backup/restore describe CLI.](https://github.com/velero-io/velero/pull/10436) — velero-io/velero
- [#10438 Issue #10437: derive velero server's graceful shutdown timeout from terminationGracePeriodSeconds](https://github.com/velero-io/velero/pull/10438) — velero-io/velero
- [#10468 Add Community section with meeting info to README](https://github.com/velero-io/velero/pull/10468) — velero-io/velero
- [#10449 Fix snapshot-location get --selector flag to actually filter VolumeSnapshotLocations by label](https://github.com/velero-io/velero/pull/10449) — velero-io/velero
- [#10474 [release-1.18] Add operation context to user-facing error messages](https://github.com/velero-io/velero/pull/10474) — velero-io/velero
- [#10464 Add operation context to user-facing error messages](https://github.com/velero-io/velero/pull/10464) — velero-io/velero
- [#10421 Add "IncrementalBytes" field to status of DataDownload and PVR to indicate data transfered by the incremental restore](https://github.com/velero-io/velero/pull/10421) — velero-io/velero
- [#10447 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10447) — velero-io/velero

**openshift** (35)
- [#164 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (4dd1b5d) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/164) — openshift/oadp-must-gather
- [#310 Fix 4 CVEs (CVE-2026-46600, CVE-2026-56852, GHSA-hrxh-6v49-42gf, ...)](https://github.com/openshift/hypershift-oadp-plugin/pull/310) — openshift/hypershift-oadp-plugin
- [#84713 remove github action 'run ci' requirement](https://github.com/openshift/release/pull/84713) — openshift/release
- [#2415 [oadp-1.5] Add uploader-type argument to Velero deployment configuration when configuration.args is used.](https://github.com/openshift/oadp-operator/pull/2415) — openshift/oadp-operator
- [#573 Fix OADP 1.5 release branch CI checks](https://github.com/openshift/velero/pull/573) — openshift/velero
- [#572 Fix 7 CVEs (CVE-2026-56854, CVE-2026-56864, CVE-2026-56865, ...)](https://github.com/openshift/velero/pull/572) — openshift/velero
- [#2439 Fix 5 CVEs (CVE-2026-56854, CVE-2026-46600, CVE-2026-56852, ...)](https://github.com/openshift/oadp-operator/pull/2439) — openshift/oadp-operator
- [#2438 [oadp-1.6] fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2438) — openshift/oadp-operator
- [#2437 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-operator/pull/2437) — openshift/oadp-operator
- [#2436 [oadp-1.6] OADP-7895 CRD changes for the non admin describe command issue](https://github.com/openshift/oadp-operator/pull/2436) — openshift/oadp-operator
- [#571 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero/pull/571) — openshift/velero
- [#309 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/hypershift-oadp-plugin/pull/309) — openshift/hypershift-oadp-plugin
- [#167 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/167) — openshift/velero-plugin-for-microsoft-azure
- [#167 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-gcp/pull/167) — openshift/velero-plugin-for-gcp
- [#165 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-aws/pull/165) — openshift/velero-plugin-for-aws
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-must-gather/pull/166) — openshift/oadp-must-gather
- [#469 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/openshift-velero-plugin/pull/469) — openshift/openshift-velero-plugin
- [#2419 [oadp-1.6] [OADP-8704] fix: only set region in BSL config for AWS CloudStorage](https://github.com/openshift/oadp-operator/pull/2419) — openshift/oadp-operator
- [#2434 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-operator/pull/2434) — openshift/oadp-operator
- [#2431 OADP-7895 CRD changes for the non admin describe command issue](https://github.com/openshift/oadp-operator/pull/2431) — openshift/oadp-operator
- [#2418 docs(kubevirt-datamover): fix HCO featureGates patch, CR name typo, and log-capture accuracy](https://github.com/openshift/oadp-operator/pull/2418) — openshift/oadp-operator
- [#467 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (4fbd08e) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/467) — openshift/openshift-velero-plugin
- [#468 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/openshift-velero-plugin/pull/468) — openshift/openshift-velero-plugin
- [#570 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero/pull/570) — openshift/velero
- [#165 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-must-gather/pull/165) — openshift/oadp-must-gather
- [#308 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/hypershift-oadp-plugin/pull/308) — openshift/hypershift-oadp-plugin
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-gcp/pull/166) — openshift/velero-plugin-for-gcp
- [#164 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-aws/pull/164) — openshift/velero-plugin-for-aws
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/166) — openshift/velero-plugin-for-microsoft-azure
- [#2432 [oadp-1.6] Fix VMFR NetworkPolicy egress to BSL endpoints](https://github.com/openshift/oadp-operator/pull/2432) — openshift/oadp-operator
- [#2430 Fix VMFR NetworkPolicy egress to BSL endpoints](https://github.com/openshift/oadp-operator/pull/2430) — openshift/oadp-operator
- [#165 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.1 (6fb0379) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/165) — openshift/velero-plugin-for-microsoft-azure
- [#2426 [oadp-1.6] feat: Add NetworkPolicy support for OADP operands (OADP-6074)](https://github.com/openshift/oadp-operator/pull/2426) — openshift/oadp-operator
- [#2424 [oadp-1.6] fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2424) — openshift/oadp-operator
- [#2422 [oadp-1.6] e2e: add cacert tests using in-cluster minio with TLS](https://github.com/openshift/oadp-operator/pull/2422) — openshift/oadp-operator

**migtools** (31)
- [#231 [oadp-1.6] Updated annotation name for consistency with naming conventions](https://github.com/migtools/kubevirt-datamover-controller/pull/231) — migtools/kubevirt-datamover-controller
- [#229 Updated annotation name for consistency with naming conventions](https://github.com/migtools/kubevirt-datamover-controller/pull/229) — migtools/kubevirt-datamover-controller
- [#188 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/udistribution/pull/188) — migtools/udistribution
- [#384 Fix CVE-2026-46600, CVE-2026-56852](https://github.com/migtools/oadp-non-admin/pull/384) — migtools/oadp-non-admin
- [#230 [oadp-1.6] Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/230) — migtools/kubevirt-datamover-controller
- [#228 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-datamover-controller/pull/228) — migtools/kubevirt-datamover-controller
- [#37 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-vmdp/pull/37) — migtools/oadp-vmdp
- [#264 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-cli/pull/264) — migtools/oadp-cli
- [#84 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-velero-plugin/pull/84) — migtools/kubevirt-velero-plugin
- [#382 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-non-admin/pull/382) — migtools/oadp-non-admin
- [#38 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/filebrowser/pull/38) — migtools/filebrowser
- [#104 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-vm-file-restore/pull/104) — migtools/oadp-vm-file-restore
- [#50 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kopia/pull/50) — migtools/kopia
- [#59 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-datamover-plugin/pull/59) — migtools/kubevirt-datamover-plugin
- [#379 [oadp-1.6] OADP-7895 : Fix for oc oadp nonadmin backup describe shows Pod Volume…](https://github.com/migtools/oadp-non-admin/pull/379) — migtools/oadp-non-admin
- [#58 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-datamover-plugin/pull/58) — migtools/kubevirt-datamover-plugin
- [#103 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-vm-file-restore/pull/103) — migtools/oadp-vm-file-restore
- [#227 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-datamover-controller/pull/227) — migtools/kubevirt-datamover-controller
- [#83 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-velero-plugin/pull/83) — migtools/kubevirt-velero-plugin
- [#263 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-cli/pull/263) — migtools/oadp-cli
- [#37 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/filebrowser/pull/37) — migtools/filebrowser
- [#380 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-non-admin/pull/380) — migtools/oadp-non-admin
- [#49 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kopia/pull/49) — migtools/kopia
- [#36 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-vmdp/pull/36) — migtools/oadp-vmdp
- [#57 Bump google.golang.org/grpc from 1.82.1 to 1.83.1](https://github.com/migtools/kubevirt-datamover-plugin/pull/57) — migtools/kubevirt-datamover-plugin
- [#102 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (1208cdf) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/102) — migtools/oadp-vm-file-restore
- [#378 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (63a89f8) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/378) — migtools/oadp-non-admin
- [#215 [oadp-1.6] fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/215) — migtools/kubevirt-datamover-controller
- [#216 [oadp-1.6] fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/216) — migtools/kubevirt-datamover-controller
- [#214 [oadp-1.6] alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/214) — migtools/kubevirt-datamover-controller
- [#53 [oadp-1.6] Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/53) — migtools/kubevirt-datamover-plugin

**Other** (2)
- [#184 Fix CVE remediation dependency rollbacks](https://github.com/oadp-rebasebot/oadp-rebase/pull/184) — oadp-rebasebot/oadp-rebase
- [#3 fix: allow unrestricted egress for operator pod NetworkPolicy](https://github.com/shubham-pampattiwar/oadp-operator/pull/3) — shubham-pampattiwar/oadp-operator
## Issues/PRs Commented On (33)

**velero-io** (18)
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#9833 Backup/restore describe for block data mover](https://github.com/velero-io/velero/issues/9833) — velero-io/velero
- [#9835 Backup deletion for block data mover](https://github.com/velero-io/velero/issues/9835) — velero-io/velero
- [#10478 Support structured output for multi-item backup and restore describe](https://github.com/velero-io/velero/issues/10478) — velero-io/velero
- [#7564 Add support to output restore describe in multiple format like backups](https://github.com/velero-io/velero/issues/7564) — velero-io/velero
- [#8654 Velero backups failing due to blob missing from the repository](https://github.com/velero-io/velero/issues/8654) — velero-io/velero
- [#10440 Cleanup: Resolve Ginkgo V2 and Gomega anti-patterns in test suite](https://github.com/velero-io/velero/issues/10440) — velero-io/velero
- [#10437 `velero server`'s shutdown grace period is hardcoded to 30s, ignoring `terminationGracePeriodSeconds`](https://github.com/velero-io/velero/issues/10437) — velero-io/velero
- [#9556 Block level backup/restore support](https://github.com/velero-io/velero/issues/9556) — velero-io/velero
- [#8263 Fatal: unable to open config file results in PartiallyFailed Backup](https://github.com/velero-io/velero/issues/8263) — velero-io/velero
- [#9318 Behavior of skip volume policy is strange/problematic](https://github.com/velero-io/velero/issues/9318) — velero-io/velero
- [#9453 DataUpload tasks stuck in Prepared phase for extended periods](https://github.com/velero-io/velero/issues/9453) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#9656 Kopia maintenance fails with 'ciphertext too short: 0' after S3 quota-related write failures leave 0-byte blobs](https://github.com/velero-io/velero/issues/9656) — velero-io/velero
- [#9760 Allow Velero kubernetes objects to be backed up with If-None-Match bucket policies enabled.](https://github.com/velero-io/velero/issues/9760) — velero-io/velero

**openshift** (3)
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#2413 Poll: how to fix e2e-test-kubevirt-aws hitting the 2h Prow step timeout](https://github.com/openshift/oadp-operator/issues/2413) — openshift/oadp-operator

**Other** (12)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#915 branchprotector cannot manage required status check GitHub App identity](https://github.com/kubernetes-sigs/prow/issues/915) — kubernetes-sigs/prow
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
- [#1847 Include scrollback history in state restoration](https://github.com/ghostty-org/ghostty/issues/1847) — ghostty-org/ghostty
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#481 Support using a later patch release than what's in go.mod](https://github.com/actions/setup-go/issues/481) — actions/setup-go
- [#18963 VEP #25: Infer backup target StorageClass from source VM volumes](https://github.com/kubevirt/kubevirt/issues/18963) — kubevirt/kubevirt
- [#18959 VEP #25: CBT: completed VirtualMachineBackup can be overwritten with SourceLost due to a stale reconcile race](https://github.com/kubevirt/kubevirt/issues/18959) — kubevirt/kubevirt
- [#18950 VEP #25: CBT: VirtualMachineBackup status freezes indefinitely while target PVC attach is pending](https://github.com/kubevirt/kubevirt/issues/18950) — kubevirt/kubevirt
## Issues Closed (5)

**velero-io** (2)
- [#10298 Setting node-agent csiSnapshotMetadataServiceConfigs.saName breaks all CSI snapshot datamover backups (arg/flag name mismatch)](https://github.com/velero-io/velero/issues/10298) — velero-io/velero
- [#10294 Generic CSI changeID retrieval returns empty — all non-vSphere drivers silently fall back to full backups](https://github.com/velero-io/velero/issues/10294) — velero-io/velero

**migtools** (1)
- [#211 DataUpload stuck forever: "VMBT already prepared but VMB not yet visible in cache, requeuing"](https://github.com/migtools/kubevirt-datamover-controller/issues/211) — migtools/kubevirt-datamover-controller

**Other** (2)
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
- [#1623 jira_transition_issue's `comment` argument silently dropped on Jira Cloud (transition succeeds, comment never posts)](https://github.com/sooperset/mcp-atlassian/issues/1623) — sooperset/mcp-atlassian
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
