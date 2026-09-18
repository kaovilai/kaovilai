# Activity Log

> **Period:** 2026-09-04 — 2026-09-18
> **Generated:** 2026-09-18 22:23:07 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 40 |
| PRs Opened | 39 |
| PRs Reviewed | 57 |
| Issues/PRs Commented | 31 |
| Issues Closed | 7 |

---

## PRs Merged (40)

**velero-io** (6)
- [#9221 docs: Document --write-sparse-files flag for disk space issues during restore](https://github.com/velero-io/velero/pull/9221) — velero-io/velero
- [#9772 Design: namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/9772) — velero-io/velero
- [#10027 Add set-based label selector test and docs coverage for restore](https://github.com/velero-io/velero/pull/10027) — velero-io/velero
- [#9575 Add configurable tolerations for PodVolumeBackup and data mover pods](https://github.com/velero-io/velero/pull/9575) — velero-io/velero
- [#10318 Fix datamover backup arg mismatch for CSI CBT service account name](https://github.com/velero-io/velero/pull/10318) — velero-io/velero
- [#10307 Fix generic CSI changeID retrieval and honor snapshot class deletion policy for CBT retention](https://github.com/velero-io/velero/pull/10307) — velero-io/velero

**openshift** (8)
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release
- [#449 Detect SCC UID/GID-range mismatch on namespace restore](https://github.com/openshift/openshift-velero-plugin/pull/449) — openshift/openshift-velero-plugin
- [#2446 [oadp-1.5] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts (cherry-pick #2234)](https://github.com/openshift/oadp-operator/pull/2446) — openshift/oadp-operator
- [#2445 fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2445) — openshift/oadp-operator
- [#2234 OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2234) — openshift/oadp-operator
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release
- [#2435 fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2435) — openshift/oadp-operator

**migtools** (1)
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller

**Other** (25)
- [#1 Bring vendor/amazon/maverick blobs in sync with the lineage-20 device tree manifest](https://github.com/kaovilai/android_vendor_amazon_maverick/pull/1) — kaovilai/android_vendor_amazon_maverick
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
## PRs Opened (39)

**velero-io** (1)
- [#10534 Add changelog-bot workflow to add changelogs via /changelog comment](https://github.com/velero-io/velero/pull/10534) — velero-io/velero

**openshift** (8)
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator
- [#2453 OADP-6065: auto-detect AWS region for CloudStorage-backed BSLs](https://github.com/openshift/oadp-operator/pull/2453) — openshift/oadp-operator
- [#2452 fix(nodeagent): propagate PodConfig.PriorityClassName to node-agent ConfigMap](https://github.com/openshift/oadp-operator/pull/2452) — openshift/oadp-operator
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release
- [#2446 [oadp-1.5] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts (cherry-pick #2234)](https://github.com/openshift/oadp-operator/pull/2446) — openshift/oadp-operator
- [#2445 fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2445) — openshift/oadp-operator
- [#84592 oadp-operator: split e2e-test-kubevirt-aws-periodic into kdm/non-kdm jobs](https://github.com/openshift/release/pull/84592) — openshift/release

**migtools** (1)
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore

**Other** (29)
- [#4 Throwaway: trigger fork CI](https://github.com/kaovilai/cliprelay/pull/4) — kaovilai/cliprelay
- [#116 OtpExtractor: support alphanumeric OTP codes](https://github.com/geekflyer/cliprelay/pull/116) — geekflyer/cliprelay
- [#3 WIP: OTP extractor pattern fixes (Copilot workspace — do not merge)](https://github.com/kaovilai/cliprelay/pull/3) — kaovilai/cliprelay
- [#1 Bring vendor/amazon/maverick blobs in sync with the lineage-20 device tree manifest](https://github.com/kaovilai/android_vendor_amazon_maverick/pull/1) — kaovilai/android_vendor_amazon_maverick
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
## PRs Reviewed (57)

**velero-io** (9)
- [#10537 Add doc for block data mover](https://github.com/velero-io/velero/pull/10537) — velero-io/velero
- [#10539 [Backport release-1.18] Fix backup queue permanently stuck when a dequeued backup completes during the patch](https://github.com/velero-io/velero/pull/10539) — velero-io/velero
- [#10521 Fix backup queue permanently stuck when a dequeued backup completes during the patch](https://github.com/velero-io/velero/pull/10521) — velero-io/velero
- [#10530 Identify the backed-up volume by CSI volume handle in the in-place restore pre-flight check](https://github.com/velero-io/velero/pull/10530) — velero-io/velero
- [#10507 install: clarify --wait flag behavior, default false](https://github.com/velero-io/velero/pull/10507) — velero-io/velero
- [#10526 Fix schedule create dropping backup type](https://github.com/velero-io/velero/pull/10526) — velero-io/velero
- [#10524 test: use the Kind constant instead of the string literal](https://github.com/velero-io/velero/pull/10524) — velero-io/velero
- [#10523 Let uploader to control fallback centrally](https://github.com/velero-io/velero/pull/10523) — velero-io/velero
- [#10479 Report incremental fallback message](https://github.com/velero-io/velero/pull/10479) — velero-io/velero

**openshift** (24)
- [#2456 Grant VMFR controller PVC delete permission](https://github.com/openshift/oadp-operator/pull/2456) — openshift/oadp-operator
- [#2455 [oadp-1.6] fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2455) — openshift/oadp-operator
- [#85502 Update OADP builder images to ubi9-v1.26](https://github.com/openshift/release/pull/85502) — openshift/release
- [#85499 Update migtools/oadp-cli builder to ubi9-v1.26 for oadp-dev, oadp-1.5, oadp-1.6](https://github.com/openshift/release/pull/85499) — openshift/release
- [#474 Bump google.golang.org/grpc from 1.83.1 to 1.83.2](https://github.com/openshift/openshift-velero-plugin/pull/474) — openshift/openshift-velero-plugin
- [#167 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-gcp/pull/167) — openshift/velero-plugin-for-gcp
- [#469 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/openshift-velero-plugin/pull/469) — openshift/openshift-velero-plugin
- [#167 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/167) — openshift/velero-plugin-for-microsoft-azure
- [#2449 [oadp-1.6] chore(deps): migrate MinIO image registry from Docker Hub to Quay](https://github.com/openshift/oadp-operator/pull/2449) — openshift/oadp-operator
- [#2448 chore(deps): migrate MinIO image registry from Docker Hub to Quay](https://github.com/openshift/oadp-operator/pull/2448) — openshift/oadp-operator
- [#84954 Remove OADP rebasebot periodic jobs](https://github.com/openshift/release/pull/84954) — openshift/release
- [#2447 [oadp-1.6] fix: don't check VEP-25 CRDs before the feature gate that creates them](https://github.com/openshift/oadp-operator/pull/2447) — openshift/oadp-operator
- [#2444 [oadp-1.6] OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2444) — openshift/oadp-operator
- [#310 Fix 4 CVEs (CVE-2026-46600, CVE-2026-56852, GHSA-hrxh-6v49-42gf, ...)](https://github.com/openshift/hypershift-oadp-plugin/pull/310) — openshift/hypershift-oadp-plugin
- [#84713 remove github action 'run ci' requirement](https://github.com/openshift/release/pull/84713) — openshift/release
- [#573 Fix OADP 1.5 release branch CI checks](https://github.com/openshift/velero/pull/573) — openshift/velero
- [#572 Fix 7 CVEs (CVE-2026-56854, CVE-2026-56864, CVE-2026-56865, ...)](https://github.com/openshift/velero/pull/572) — openshift/velero
- [#2439 Fix 5 CVEs (CVE-2026-56854, CVE-2026-46600, CVE-2026-56852, ...)](https://github.com/openshift/oadp-operator/pull/2439) — openshift/oadp-operator
- [#2438 [oadp-1.6] fix: vendor virtualmachineinstances RBAC from KDM PR #218](https://github.com/openshift/oadp-operator/pull/2438) — openshift/oadp-operator
- [#2437 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-operator/pull/2437) — openshift/oadp-operator
- [#571 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero/pull/571) — openshift/velero
- [#309 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/hypershift-oadp-plugin/pull/309) — openshift/hypershift-oadp-plugin
- [#165 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-aws/pull/165) — openshift/velero-plugin-for-aws
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-must-gather/pull/166) — openshift/oadp-must-gather

**migtools** (20)
- [#236 Fix default max concurrent data movers](https://github.com/migtools/kubevirt-datamover-controller/pull/236) — migtools/kubevirt-datamover-controller
- [#105 [oadp-1.6] OADP-7467: Fix VMFR restore namespace access](https://github.com/migtools/oadp-vm-file-restore/pull/105) — migtools/oadp-vm-file-restore
- [#190 Bump go.opentelemetry.io/otel/sdk from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/190) — migtools/udistribution
- [#189 Bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/189) — migtools/udistribution
- [#59 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/kubevirt-datamover-plugin/pull/59) — migtools/kubevirt-datamover-plugin
- [#235 Fix default max concurrent data movers](https://github.com/migtools/kubevirt-datamover-controller/pull/235) — migtools/kubevirt-datamover-controller
- [#62 update kubevirt-datamover-controller dependency and remove replace](https://github.com/migtools/kubevirt-datamover-plugin/pull/62) — migtools/kubevirt-datamover-plugin
- [#61 [oadp-1.6] issue #14: allow users to skip quiesce via Backup or VM](https://github.com/migtools/kubevirt-datamover-plugin/pull/61) — migtools/kubevirt-datamover-plugin
- [#231 [oadp-1.6] Updated annotation name for consistency with naming conventions](https://github.com/migtools/kubevirt-datamover-controller/pull/231) — migtools/kubevirt-datamover-controller
- [#229 Updated annotation name for consistency with naming conventions](https://github.com/migtools/kubevirt-datamover-controller/pull/229) — migtools/kubevirt-datamover-controller
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

**Other** (4)
- [#620 :sparkles: Restrict operand egress via NetworkPolicy](https://github.com/konveyor/operator/pull/620) — konveyor/operator
- [#192 update plugins to 1.14.3-rc.2](https://github.com/oadp-rebasebot/oadp-rebase/pull/192) — oadp-rebasebot/oadp-rebase
- [#394 feat(network): support internal networks](https://github.com/socktainer/socktainer/pull/394) — socktainer/socktainer
- [#184 Fix CVE remediation dependency rollbacks](https://github.com/oadp-rebasebot/oadp-rebase/pull/184) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (31)

**velero-io** (19)
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9556 Block level backup/restore support](https://github.com/velero-io/velero/issues/9556) — velero-io/velero
- [#8707 Support multiple transmission protocols](https://github.com/velero-io/velero/issues/8707) — velero-io/velero
- [#10340 Bug: EphemeralContainers are missing from ServiceAccount token filtering in PodAction](https://github.com/velero-io/velero/issues/10340) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#2812 Restore fails with error "no space left on device" if PVCs are 100% utilised during backup](https://github.com/velero-io/velero/issues/2812) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#8263 Fatal: unable to open config file results in PartiallyFailed Backup](https://github.com/velero-io/velero/issues/8263) — velero-io/velero
- [#9318 Behavior of skip volume policy is strange/problematic](https://github.com/velero-io/velero/issues/9318) — velero-io/velero
- [#9453 DataUpload tasks stuck in Prepared phase for extended periods](https://github.com/velero-io/velero/issues/9453) — velero-io/velero
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#9735 Velero should add a clear error when data mover pod is unschedulable due to affinity/topology mismatch](https://github.com/velero-io/velero/issues/9735) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#9833 Backup/restore describe for block data mover](https://github.com/velero-io/velero/issues/9833) — velero-io/velero
- [#9835 Backup deletion for block data mover](https://github.com/velero-io/velero/issues/9835) — velero-io/velero
- [#10478 Support structured output for multi-item backup and restore describe](https://github.com/velero-io/velero/issues/10478) — velero-io/velero

**openshift** (3)
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator

**migtools** (2)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#14 Handle guest agent connectivity and SkipQuiesce for VirtualMachineBackup](https://github.com/migtools/kubevirt-datamover-controller/issues/14) — migtools/kubevirt-datamover-controller

**Other** (7)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#2 OtpExtractor: support alphanumeric OTP codes](https://github.com/kaovilai/cliprelay/issues/2) — kaovilai/cliprelay
- [#2525 `pull_request_review_write` combines create/submit/delete into one tool, making fine-grained permissions by method impossible](https://github.com/github/github-mcp-server/issues/2525) — github/github-mcp-server
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
- [#915 branchprotector cannot manage required status check GitHub App identity](https://github.com/kubernetes-sigs/prow/issues/915) — kubernetes-sigs/prow
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
## Issues Closed (7)

**velero-io** (5)
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#9771 Design: ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/9771) — velero-io/velero
- [#10295 CBT delta-error fallback marks the whole device dirty instead of the design's allocated-blocks full backup](https://github.com/velero-io/velero/issues/10295) — velero-io/velero
- [#10298 Setting node-agent csiSnapshotMetadataServiceConfigs.saName breaks all CSI snapshot datamover backups (arg/flag name mismatch)](https://github.com/velero-io/velero/issues/10298) — velero-io/velero
- [#10294 Generic CSI changeID retrieval returns empty — all non-vSphere drivers silently fall back to full backups](https://github.com/velero-io/velero/issues/10294) — velero-io/velero

**openshift** (2)
- [#448 Feature request: detect/reconcile SCC UID/GID-range mismatch on Namespace restore](https://github.com/openshift/openshift-velero-plugin/issues/448) — openshift/openshift-velero-plugin
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
