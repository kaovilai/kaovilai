# Activity Log

> **Period:** 2026-08-29 — 2026-09-12
> **Generated:** 2026-09-12 20:27:53 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 47 |
| PRs Opened | 45 |
| PRs Reviewed | 79 |
| Issues/PRs Commented | 29 |
| Issues Closed | 6 |

---

## PRs Merged (47)

**velero-io** (5)
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero
- [#10307 Fix generic CSI changeID retrieval and honor snapshot class deletion policy for CBT retention](https://github.com/velero-io/velero/pull/10307) — velero-io/velero
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero
- [#10403 Check both daemonsets before returning non-NotFound lookup error in IsReady](https://github.com/velero-io/velero/pull/10403) — velero-io/velero
- [#10406 release-1.17: validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10406) — velero-io/velero

**openshift** (10)
- [#2446 [oadp-1.5] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts (cherry-pick #2234)](https://github.com/openshift/oadp-operator/pull/2446) — openshift/oadp-operator
- [#2445 fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2445) — openshift/oadp-operator
- [#2234 OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2234) — openshift/oadp-operator
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release
- [#2435 fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2435) — openshift/oadp-operator
- [#84490 oadp-operator: split e2e-test-kubevirt-aws into kdm/non-kdm jobs (oadp-1.6)](https://github.com/openshift/release/pull/84490) — openshift/release
- [#2404 test: unpend two kdm restore PIts, fixing bugs found via live e2e validation](https://github.com/openshift/oadp-operator/pull/2404) — openshift/oadp-operator
- [#84337 oadp: split kubevirt e2e job (5.0) and add Claude failure analysis to kdm-controller/plugin](https://github.com/openshift/release/pull/84337) — openshift/release
- [#566 1.4: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/566) — openshift/velero
- [#2423 fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2423) — openshift/oadp-operator

**migtools** (4)
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller

**Other** (28)
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
- [#175 Skip Test/Override buttons on tide's own status context](https://github.com/kaovilai/github-bot-command-palette/pull/175) — kaovilai/github-bot-command-palette
- [#174 Extend combo window to per-check Override, add pending-button spinner](https://github.com/kaovilai/github-bot-command-palette/pull/174) — kaovilai/github-bot-command-palette
- [#173 Combo auto-submit window, override on pending checks, native Approve sync](https://github.com/kaovilai/github-bot-command-palette/pull/173) — kaovilai/github-bot-command-palette
## PRs Opened (45)

**velero-io** (1)
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero

**openshift** (11)
- [#2446 [oadp-1.5] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts (cherry-pick #2234)](https://github.com/openshift/oadp-operator/pull/2446) — openshift/oadp-operator
- [#2445 fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2445) — openshift/oadp-operator
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release
- [#2435 fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2435) — openshift/oadp-operator
- [#84490 oadp-operator: split e2e-test-kubevirt-aws into kdm/non-kdm jobs (oadp-1.6)](https://github.com/openshift/release/pull/84490) — openshift/release
- [#567 1.5: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/567) — openshift/velero
- [#566 1.4: Skip upstream-only workflows on this fork (cherry-pick velero-io/velero#10001)](https://github.com/openshift/velero/pull/566) — openshift/velero
- [#84337 oadp: split kubevirt e2e job (5.0) and add Claude failure analysis to kdm-controller/plugin](https://github.com/openshift/release/pull/84337) — openshift/release
- [#2423 fix(e2e): TEST_VIRT excludes kdm specs, enable split-job e2e (issue #2413 option B)](https://github.com/openshift/oadp-operator/pull/2423) — openshift/oadp-operator
- [#84229 oadp-operator: bump e2e-test-kubevirt-aws timeout to 3h](https://github.com/openshift/release/pull/84229) — openshift/release
- [#84228 Add Depends-On cross-repo image build across the OADP ecosystem (KDM, oadp-operator, velero family)](https://github.com/openshift/release/pull/84228) — openshift/release

**migtools** (3)
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#213 fix: speed up Dockerfile builds with cache mounts](https://github.com/migtools/kubevirt-datamover-controller/pull/213) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller

**Other** (30)
- [#7 Add safe Dependabot auto-merge workflow for npm patch/minor updates](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/7) — kaovilai/bandwidth-hero-proxy2
- [#14 Fix healthcheck: use 127.0.0.1 instead of localhost](https://github.com/kaovilai/copilot-api/pull/14) — kaovilai/copilot-api
- [#13 Lower ambiguous-timeout budget to 80s to beat client watchdogs](https://github.com/kaovilai/copilot-api/pull/13) — kaovilai/copilot-api
- [#182 Fall back to top-level build-log.txt for steps that die before writing artifacts](https://github.com/kaovilai/github-bot-command-palette/pull/182) — kaovilai/github-bot-command-palette
- [#6 Fix Netlify build failure: bump Node version and sync yarn.lock](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/6) — kaovilai/bandwidth-hero-proxy2
- [#3 Harden CRX recorder/transport reconnect lifecycle with bounded recovery and stale-session renewal](https://github.com/kaovilai/playwright-crx/pull/3) — kaovilai/playwright-crx
- [#1 Keep recorder sessions alive across UI reconnects and stop Resume/Step from replaying paused actions](https://github.com/kaovilai/playwright-crx/pull/1) — kaovilai/playwright-crx
- [#12 Address CodeRabbit findings on the streaming chat-completions handler](https://github.com/kaovilai/copilot-api/pull/12) — kaovilai/copilot-api
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
## PRs Reviewed (79)

**velero-io** (10)
- [#10526 Fix schedule create dropping backup type](https://github.com/velero-io/velero/pull/10526) — velero-io/velero
- [#10524 test: use the Kind constant instead of the string literal](https://github.com/velero-io/velero/pull/10524) — velero-io/velero
- [#10507 install: default --wait to true and add --no-wait flag](https://github.com/velero-io/velero/pull/10507) — velero-io/velero
- [#10523 Let uploader to control fallback centrally](https://github.com/velero-io/velero/pull/10523) — velero-io/velero
- [#10479 Report incremental fallback message](https://github.com/velero-io/velero/pull/10479) — velero-io/velero
- [#10468 Add Community section with meeting info to README](https://github.com/velero-io/velero/pull/10468) — velero-io/velero
- [#10449 Fix snapshot-location get --selector flag to actually filter VolumeSnapshotLocations by label](https://github.com/velero-io/velero/pull/10449) — velero-io/velero
- [#10474 [release-1.18] Add operation context to user-facing error messages](https://github.com/velero-io/velero/pull/10474) — velero-io/velero
- [#10464 Add operation context to user-facing error messages](https://github.com/velero-io/velero/pull/10464) — velero-io/velero
- [#10447 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10447) — velero-io/velero

**openshift** (35)
- [#84954 Remove OADP rebasebot periodic jobs](https://github.com/openshift/release/pull/84954) — openshift/release
- [#2447 [oadp-1.6] fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2447) — openshift/oadp-operator
- [#2444 [oadp-1.6] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2444) — openshift/oadp-operator
- [#164 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (4dd1b5d) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/164) — openshift/oadp-must-gather
- [#310 Fix 4 CVEs (CVE-2026-46600, CVE-2026-56852, GHSA-hrxh-6v49-42gf, ...)](https://github.com/openshift/hypershift-oadp-plugin/pull/310) — openshift/hypershift-oadp-plugin
- [#84713 remove github action 'run ci' requirement](https://github.com/openshift/release/pull/84713) — openshift/release
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
- [#2434 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-operator/pull/2434) — openshift/oadp-operator
- [#2431 OADP-7895 CRD changes for the non admin describe command issue](https://github.com/openshift/oadp-operator/pull/2431) — openshift/oadp-operator
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

**migtools** (32)
- [#221 build(deps): bump google.golang.org/grpc from 1.82.1 to 1.83.1](https://github.com/migtools/kubevirt-datamover-controller/pull/221) — migtools/kubevirt-datamover-controller
- [#61 [oadp-1.6] issue #14: allow users to skip quiesce via Backup or VM](https://github.com/migtools/kubevirt-datamover-plugin/pull/61) — migtools/kubevirt-datamover-plugin
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

**Other** (2)
- [#394 feat(network): support internal networks](https://github.com/socktainer/socktainer/pull/394) — socktainer/socktainer
- [#184 Fix CVE remediation dependency rollbacks](https://github.com/oadp-rebasebot/oadp-rebase/pull/184) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (29)

**velero-io** (16)
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#9735 Velero should add a clear error when data mover pod is unschedulable due to affinity/topology mismatch](https://github.com/velero-io/velero/issues/9735) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero
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

**openshift** (4)
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#2413 Poll: how to fix e2e-test-kubevirt-aws hitting the 2h Prow step timeout](https://github.com/openshift/oadp-operator/issues/2413) — openshift/oadp-operator

**Other** (9)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
- [#2525 `pull_request_review_write` combines create/submit/delete into one tool, making fine-grained permissions by method impossible](https://github.com/github/github-mcp-server/issues/2525) — github/github-mcp-server
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
- [#915 branchprotector cannot manage required status check GitHub App identity](https://github.com/kubernetes-sigs/prow/issues/915) — kubernetes-sigs/prow
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
- [#1847 Include scrollback history in state restoration](https://github.com/ghostty-org/ghostty/issues/1847) — ghostty-org/ghostty
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
## Issues Closed (6)

**velero-io** (3)
- [#10295 CBT delta-error fallback marks the whole device dirty instead of the design's allocated-blocks full backup](https://github.com/velero-io/velero/issues/10295) — velero-io/velero
- [#10298 Setting node-agent csiSnapshotMetadataServiceConfigs.saName breaks all CSI snapshot datamover backups (arg/flag name mismatch)](https://github.com/velero-io/velero/issues/10298) — velero-io/velero
- [#10294 Generic CSI changeID retrieval returns empty — all non-vSphere drivers silently fall back to full backups](https://github.com/velero-io/velero/issues/10294) — velero-io/velero

**openshift** (1)
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator

**migtools** (1)
- [#211 DataUpload stuck forever: "VMBT already prepared but VMB not yet visible in cache, requeuing"](https://github.com/migtools/kubevirt-datamover-controller/issues/211) — migtools/kubevirt-datamover-controller

**Other** (1)
- [#4549 v1beta1→v1 conversion webhook fails on spec.featureGates: "cannot unmarshal object into Go struct field HyperConvergedSpec.spec.featureGates"](https://github.com/kubevirt/hyperconverged-cluster-operator/issues/4549) — kubevirt/hyperconverged-cluster-operator
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
