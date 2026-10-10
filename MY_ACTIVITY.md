# Activity Log

> **Period:** 2026-07-12 — 2026-10-10
> **Generated:** 2026-10-10 20:21:26 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 100 |
| PRs Opened | 100 |
| PRs Reviewed | 83 |
| Issues/PRs Commented | 100 |
| Issues Closed | 92 |

---

## PRs Merged (100)

**velero-io** (20)
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
- [#10307 Fix generic CSI changeID retrieval and honor snapshot class deletion policy for CBT retention](https://github.com/velero-io/velero/pull/10307) — velero-io/velero
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero
- [#10403 Check both daemonsets before returning non-NotFound lookup error in IsReady](https://github.com/velero-io/velero/pull/10403) — velero-io/velero
- [#10406 release-1.17: validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10406) — velero-io/velero
- [#10381 1.18: #9795: Skip DeleteSnapshot when ProviderSnapshotID is empty](https://github.com/velero-io/velero/pull/10381) — velero-io/velero
- [#10348 1.18: Backport #10342: Fix LoadAffinity mutation accumulating OS node selector terms](https://github.com/velero-io/velero/pull/10348) — velero-io/velero
- [#10407 1.18: Cherry-pick #10390: Validate kind node tags before adding to e2e test matrix](https://github.com/velero-io/velero/pull/10407) — velero-io/velero
- [#10409 Update community meeting links to LFX Zoom, add calendar](https://github.com/velero-io/velero/pull/10409) — velero-io/velero
- [#10309 Report a measured zero incremental instead of erasing it](https://github.com/velero-io/velero/pull/10309) — velero-io/velero

**openshift** (24)
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
- [#2406 [OADP-8716] Pin MCE to stable-2.8 only below OCP 4.19, matching HCP target env](https://github.com/openshift/oadp-operator/pull/2406) — openshift/oadp-operator

**migtools** (7)
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller
- [#50 Set binding-blocking spec.selector on restore-target PVCs](https://github.com/migtools/kubevirt-datamover-plugin/pull/50) — migtools/kubevirt-datamover-plugin

**Other** (49)
- [#252 Speak question speech for Claude AskUserQuestion permission requests](https://github.com/OpenPetsHQ/openpets/pull/252) — OpenPetsHQ/openpets
- [#495 ⚡ Bolt: Optimize file staleness checks with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/495) — kaovilai/dotfiles
- [#506 ⚡ Bolt: Optimize brew list performance by caching list into array](https://github.com/kaovilai/dotfiles/pull/506) — kaovilai/dotfiles
- [#497 🔒 Fix Arbitrary Code Execution in registry login](https://github.com/kaovilai/dotfiles/pull/497) — kaovilai/dotfiles
- [#500 🧹 Extract common logic in socktainer-symlink functions](https://github.com/kaovilai/dotfiles/pull/500) — kaovilai/dotfiles
- [#514 🔒 Fix insecure TLS validation in ROSA STS login](https://github.com/kaovilai/dotfiles/pull/514) — kaovilai/dotfiles
- [#502 🔒 Fix insecure curl -k usage in MinIO scripts](https://github.com/kaovilai/dotfiles/pull/502) — kaovilai/dotfiles
- [#487 ⚡ perf: optimize process formatting in kill-stuck-qemu](https://github.com/kaovilai/dotfiles/pull/487) — kaovilai/dotfiles
- [#499 ⚡ perf: optimize `dco` git commit signoff checking with single git log query](https://github.com/kaovilai/dotfiles/pull/499) — kaovilai/dotfiles
- [#498 ⚡ Optimize GitHub PR Diff Fetching Concurrency](https://github.com/kaovilai/dotfiles/pull/498) — kaovilai/dotfiles
- [#488 🔒 Fix eval() vulnerability in verify-migration](https://github.com/kaovilai/dotfiles/pull/488) — kaovilai/dotfiles
- [#516 ⚡ Bolt: [performance improvement] fix compinit startup check](https://github.com/kaovilai/dotfiles/pull/516) — kaovilai/dotfiles
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
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
- [#170 Add Velero backport button for velero-io/velero](https://github.com/kaovilai/github-bot-command-palette/pull/170) — kaovilai/github-bot-command-palette
## PRs Opened (100)

**velero-io** (11)
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero
- [#10555 Fix e2e-test-kind and changelog-check CI flakes](https://github.com/velero-io/velero/pull/10555) — velero-io/velero
- [#10534 Add changelog-bot workflow to add changelogs via /changelog comment](https://github.com/velero-io/velero/pull/10534) — velero-io/velero
- [#10458 Skip kind E2E tests on PRs that don't touch Go code or the workflow itself](https://github.com/velero-io/velero/pull/10458) — velero-io/velero
- [#10428 [release-1.14] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10428) — velero-io/velero
- [#10427 [release-1.15] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10427) — velero-io/velero
- [#10426 [release-1.18] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10426) — velero-io/velero
- [#10425 [release-1.17] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10425) — velero-io/velero
- [#10424 [release-1.16] Skip upstream-only workflows on forks (cherry-pick #10001)](https://github.com/velero-io/velero/pull/10424) — velero-io/velero
- [#10423 [release-1.16] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/velero-io/velero/pull/10423) — velero-io/velero

**openshift** (19)
- [#86664 Add release-4.21 to Prow configuration branches](https://github.com/openshift/release/pull/86664) — openshift/release
- [#2473 fix(e2e): route/proxy 503 fallback and empty checksum exec flakes](https://github.com/openshift/oadp-operator/pull/2473) — openshift/oadp-operator
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator
- [#2453 OADP-6065: auto-detect AWS region for CloudStorage-backed BSLs](https://github.com/openshift/oadp-operator/pull/2453) — openshift/oadp-operator
- [#2452 OADP-7984: fix(nodeagent): propagate PodConfig.PriorityClassName to node-agent ConfigMap](https://github.com/openshift/oadp-operator/pull/2452) — openshift/oadp-operator
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release
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
- [#565 OADP-7061: [oadp-1.5] DM controller refactor for cancel (cherry-pick #8952)](https://github.com/openshift/velero/pull/565) — openshift/velero

**migtools** (9)
- [#192 Fix CI coverage handling for no-test packages and update setup-go](https://github.com/migtools/udistribution/pull/192) — migtools/udistribution
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore
- [#218 Detect VMI guest-agent availability before quiesce, with explicit user override](https://github.com/migtools/kubevirt-datamover-controller/pull/218) — migtools/kubevirt-datamover-controller
- [#213 fix: speed up Dockerfile builds with cache mounts](https://github.com/migtools/kubevirt-datamover-controller/pull/213) — migtools/kubevirt-datamover-controller
- [#212 fix: two DataUpload livelocks in VMB handling (stuck retry guard + stale cached status)](https://github.com/migtools/kubevirt-datamover-controller/pull/212) — migtools/kubevirt-datamover-controller
- [#208 fix: recognize VirtualMachineBackup's renamed Complete condition](https://github.com/migtools/kubevirt-datamover-controller/pull/208) — migtools/kubevirt-datamover-controller
- [#207 alt: merge-patch expected-backup-type annotation instead of retrying Update](https://github.com/migtools/kubevirt-datamover-controller/pull/207) — migtools/kubevirt-datamover-controller
- [#206 fix: retry expected-backup-type annotation on conflict instead of giving up](https://github.com/migtools/kubevirt-datamover-controller/pull/206) — migtools/kubevirt-datamover-controller

**Other** (61)
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
- [#17509 fix(server): show Antigravity's real sign-in failure reason](https://github.com/pingdotgg/t3code/pull/17509) — pingdotgg/t3code
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#126897 fix(copilot): send captured backend apiVersion to unlock 1M context](https://github.com/NousResearch/hermes-agent/pull/126897) — NousResearch/hermes-agent
- [#124184 fix(desktop): recognize Copilot's dash-suffixed 1M-context model ids](https://github.com/NousResearch/hermes-agent/pull/124184) — NousResearch/hermes-agent
- [#123138 fix(tools): hard-fail message_agent on a profile's old, renamed-away name](https://github.com/NousResearch/hermes-agent/pull/123138) — NousResearch/hermes-agent
- [#122945 fix(tools): re-derive dependency env in bot_mode_dm background runner](https://github.com/NousResearch/hermes-agent/pull/122945) — NousResearch/hermes-agent
- [#121974 feat(browser): recognize Comet, BrowserOS neo, Vivaldi, Opera, Opera GX, and Yandex for real-profile browsing](https://github.com/NousResearch/hermes-agent/pull/121974) — NousResearch/hermes-agent
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
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
- [#176 Add per-command cancel-x to pending combo buttons](https://github.com/kaovilai/github-bot-command-palette/pull/176) — kaovilai/github-bot-command-palette
- [#175 Skip Test/Override buttons on tide's own status context](https://github.com/kaovilai/github-bot-command-palette/pull/175) — kaovilai/github-bot-command-palette
- [#174 Extend combo window to per-check Override, add pending-button spinner](https://github.com/kaovilai/github-bot-command-palette/pull/174) — kaovilai/github-bot-command-palette
- [#173 Combo auto-submit window, override on pending checks, native Approve sync](https://github.com/kaovilai/github-bot-command-palette/pull/173) — kaovilai/github-bot-command-palette
- [#4552 Fix conversion webhook crash on legacy featureGates empty-object shape](https://github.com/kubevirt/hyperconverged-cluster-operator/pull/4552) — kubevirt/hyperconverged-cluster-operator
- [#18957 storage/cbt: fix stale reconcile overwriting a completed VMBackup with SourceLost](https://github.com/kubevirt/kubevirt/pull/18957) — kubevirt/kubevirt
- [#18949 storage/cbt: fix VMBackup status freeze during target PVC attach](https://github.com/kubevirt/kubevirt/pull/18949) — kubevirt/kubevirt
- [#5 Add .github/pull.yml to sync dev branch from upstream via rebase](https://github.com/kaovilai/copilot-api/pull/5) — kaovilai/copilot-api
## PRs Reviewed (83)

**velero-io** (36)
- [#10570 Warn when the volume data of an existing PVC backed up by snapshot is not restored](https://github.com/velero-io/velero/pull/10570) — velero-io/velero
- [#10588 e2e: make the StorageClass definitions configurable](https://github.com/velero-io/velero/pull/10588) — velero-io/velero
- [#10598 e2e: add VolumeGroupSnapshot coverage](https://github.com/velero-io/velero/pull/10598) — velero-io/velero
- [#10612 fix: defer VGS cleanup until backup finalization](https://github.com/velero-io/velero/pull/10612) — velero-io/velero
- [#10204 Enable TLS for MinIO in the kind E2E workflow](https://github.com/velero-io/velero/pull/10204) — velero-io/velero
- [#10636 e2e: correct why the kind backup cases are skipped](https://github.com/velero-io/velero/pull/10636) — velero-io/velero
- [#10630 e2e: document running the CSI cases on kind](https://github.com/velero-io/velero/pull/10630) — velero-io/velero
- [#10609 docs: add local Kind setup for CSI e2e](https://github.com/velero-io/velero/pull/10609) — velero-io/velero
- [#10051 docs: use consistent excludedNames glob pattern in filter design examples](https://github.com/velero-io/velero/pull/10051) — velero-io/velero
- [#10463 Fix stale contributor documentation link](https://github.com/velero-io/velero/pull/10463) — velero-io/velero
- [#10631 Fix the MinIO image cache key in the kind e2e workflow](https://github.com/velero-io/velero/pull/10631) — velero-io/velero
- [#10621 fix(controller): propagate context during backup request preparation](https://github.com/velero-io/velero/pull/10621) — velero-io/velero
- [#10593 e2e: verify CSI snapshots on kind](https://github.com/velero-io/velero/pull/10593) — velero-io/velero
- [#10212 Fix Zip Slip path check accepting a sibling directory in archive extraction](https://github.com/velero-io/velero/pull/10212) — velero-io/velero
- [#10596 e2e: add a script to install CSI snapshot support on kind](https://github.com/velero-io/velero/pull/10596) — velero-io/velero
- [#10622 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10622) — velero-io/velero
- [#10617 docs: fix contributor and maintainer guidance links](https://github.com/velero-io/velero/pull/10617) — velero-io/velero
- [#10556 [Design]Owner reference and dependency relink design](https://github.com/velero-io/velero/pull/10556) — velero-io/velero
- [#2 Document maintainer lifecycle, affiliation policy, and Code of Conduct](https://github.com/velero-io/.github/pull/2) — velero-io/.github
- [#10572 Add architecture entry point and roadmap change process](https://github.com/velero-io/velero/pull/10572) — velero-io/velero
- [#335 Make the S3 uploader inherit the client's RequestChecksumCalculation](https://github.com/velero-io/velero-plugin-for-aws/pull/335) — velero-io/velero-plugin-for-aws
- [#10385 refactor: propagate context.Context in core kube secrets and namespace utilities](https://github.com/velero-io/velero/pull/10385) — velero-io/velero
- [#10131 Fix Tiltfile Developer Experience and Plugin Build Issues](https://github.com/velero-io/velero/pull/10131) — velero-io/velero
- [#10601 Detect VolumeGroupSnapshot API version at runtime (v1/v1beta2/v1beta1)](https://github.com/velero-io/velero/pull/10601) — velero-io/velero
- [#10286 Fix re-request-review workflow for fork-originated PRs (privilege separation)](https://github.com/velero-io/velero/pull/10286) — velero-io/velero
- [#10438 Issue #10437: derive velero server's graceful shutdown timeout from terminationGracePeriodSeconds](https://github.com/velero-io/velero/pull/10438) — velero-io/velero
- [#10590 docs: fix broken internal links and anchors in main docs](https://github.com/velero-io/velero/pull/10590) — velero-io/velero
- [#10578 Enable VGDP soothing by default and set queue length as 5](https://github.com/velero-io/velero/pull/10578) — velero-io/velero
- [#10493 fix: bound VolumeSnapshot and VolumeSnapshotContent error retry by CSISnapshotTimeout](https://github.com/velero-io/velero/pull/10493) — velero-io/velero
- [#10484 fix(csi): don't fail a backup on a retryable VolumeSnapshotContent error](https://github.com/velero-io/velero/pull/10484) — velero-io/velero
- [#10177 Add FailBlock hook error mode to skip the whole ItemBlock](https://github.com/velero-io/velero/pull/10177) — velero-io/velero
- [#10432 Show default volume snapshot location in snapshot-location get output](https://github.com/velero-io/velero/pull/10432) — velero-io/velero
- [#10355 Surface EnableCSI requirement for snapshot-move-data backups](https://github.com/velero-io/velero/pull/10355) — velero-io/velero
- [#10354 Re-process InProgress DeleteBackupRequests on retry](https://github.com/velero-io/velero/pull/10354) — velero-io/velero
- [#10373 Remove RemapCRDVersionAction backup item action](https://github.com/velero-io/velero/pull/10373) — velero-io/velero
- [#10579 Change hashing algorithm to HMAC-SHA256-128 for kopia repo](https://github.com/velero-io/velero/pull/10579) — velero-io/velero

**openshift** (26)
- [#322 fix(etcdbackup): treat waiting for credentials as in progress](https://github.com/openshift/hypershift-oadp-plugin/pull/322) — openshift/hypershift-oadp-plugin
- [#2478 Fix VeleroIsDeleted GC race and GetPodWithLabel rollout flake](https://github.com/openshift/oadp-operator/pull/2478) — openshift/oadp-operator
- [#321 OADP-8726: Remove committed kubeconfig with system:masters credentials](https://github.com/openshift/hypershift-oadp-plugin/pull/321) — openshift/hypershift-oadp-plugin
- [#2443 OADP-8764: handle CACertRef in DPT](https://github.com/openshift/oadp-operator/pull/2443) — openshift/oadp-operator
- [#2475 fix(e2e): add retry logic for empty sha256sum output in checksum helpers](https://github.com/openshift/oadp-operator/pull/2475) — openshift/oadp-operator
- [#2466 [oadp-1.4] OADP-8835: feat(bsl): concatenate all CA certificates from BSLs and include system defaults](https://github.com/openshift/oadp-operator/pull/2466) — openshift/oadp-operator
- [#2474 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (fcf7610) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2474) — openshift/oadp-operator
- [#118 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (33ef7bd) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/118) — openshift/velero-plugin-for-legacy-aws
- [#319 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (45480df) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/319) — openshift/hypershift-oadp-plugin
- [#178 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.4 (d173fa9) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/178) — openshift/velero-plugin-for-gcp
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/oadp-must-gather/pull/166) — openshift/oadp-must-gather
- [#318 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (636bec3) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/318) — openshift/hypershift-oadp-plugin
- [#586 Detect VolumeGroupSnapshot API version at runtime (v1/v1beta2/v1beta1) (#10601)](https://github.com/openshift/velero/pull/586) — openshift/velero
- [#2470 [oadp-1.6] test(e2e): pin MinIO to migtools Bitnami image](https://github.com/openshift/oadp-operator/pull/2470) — openshift/oadp-operator
- [#2469 test(e2e): pin MinIO to migtools Bitnami image](https://github.com/openshift/oadp-operator/pull/2469) — openshift/oadp-operator
- [#174 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-aws/pull/174) — openshift/velero-plugin-for-aws
- [#173 Remove bz-pr-action GitHub Actions workflow](https://github.com/openshift/velero-plugin-for-aws/pull/173) — openshift/velero-plugin-for-aws
- [#165 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-aws/pull/165) — openshift/velero-plugin-for-aws
- [#477 Bump go.opentelemetry.io/otel/sdk from 1.44.0 to 1.45.0](https://github.com/openshift/openshift-velero-plugin/pull/477) — openshift/openshift-velero-plugin
- [#166 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-gcp/pull/166) — openshift/velero-plugin-for-gcp
- [#164 Add PrasadJoshi12 as approver and reviewer](https://github.com/openshift/velero-plugin-for-aws/pull/164) — openshift/velero-plugin-for-aws
- [#583 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero/pull/583) — openshift/velero
- [#482 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/openshift-velero-plugin/pull/482) — openshift/openshift-velero-plugin
- [#175 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/175) — openshift/velero-plugin-for-microsoft-azure
- [#175 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-gcp/pull/175) — openshift/velero-plugin-for-gcp
- [#69 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/restic/pull/69) — openshift/restic

**migtools** (17)
- [#64 build(deps): bump go.opentelemetry.io/otel/sdk from 1.44.0 to 1.45.0](https://github.com/migtools/kubevirt-datamover-plugin/pull/64) — migtools/kubevirt-datamover-plugin
- [#238 build(deps): bump go.opentelemetry.io/otel/exporters/otlp/otlptrace from 1.40.0 to 1.45.0](https://github.com/migtools/kubevirt-datamover-controller/pull/238) — migtools/kubevirt-datamover-controller
- [#239 build(deps): bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc from 1.40.0 to 1.45.0](https://github.com/migtools/kubevirt-datamover-controller/pull/239) — migtools/kubevirt-datamover-controller
- [#60 chore(deps): bump google.golang.org/grpc from 1.83.1 to 1.83.2](https://github.com/migtools/kubevirt-datamover-plugin/pull/60) — migtools/kubevirt-datamover-plugin
- [#237 build(deps): bump go.opentelemetry.io/otel/sdk from 1.44.0 to 1.45.0](https://github.com/migtools/kubevirt-datamover-controller/pull/237) — migtools/kubevirt-datamover-controller
- [#261 Bump google.golang.org/grpc from 1.81.1 to 1.83.2](https://github.com/migtools/oadp-cli/pull/261) — migtools/oadp-cli
- [#81 Bump google.golang.org/grpc from 1.79.3 to 1.83.1](https://github.com/migtools/kubevirt-velero-plugin/pull/81) — migtools/kubevirt-velero-plugin
- [#221 build(deps): bump google.golang.org/grpc from 1.82.1 to 1.83.1](https://github.com/migtools/kubevirt-datamover-controller/pull/221) — migtools/kubevirt-datamover-controller
- [#376 ⬆ Bump hadolint/hadolint-action from 3.4.0 to 3.5.0](https://github.com/migtools/oadp-non-admin/pull/376) — migtools/oadp-non-admin
- [#39 chore(deps): bump csv-parse from 6.2.1 to 7.0.2 in /frontend](https://github.com/migtools/filebrowser/pull/39) — migtools/filebrowser
- [#40 chore(deps-dev): bump vitest from 4.1.6 to 4.1.11 in /frontend](https://github.com/migtools/filebrowser/pull/40) — migtools/filebrowser
- [#189 Bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/189) — migtools/udistribution
- [#69 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (dc932cf) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/69) — migtools/kubevirt-datamover-plugin
- [#96 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.9.1 (6d1f840) into oadp-1.6](https://github.com/migtools/kubevirt-velero-plugin/pull/96) — migtools/kubevirt-velero-plugin
- [#276 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (f5ba313) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/276) — migtools/oadp-cli
- [#36 Add PrasadJoshi12 as approver and reviewer](https://github.com/migtools/oadp-vmdp/pull/36) — migtools/oadp-vmdp
- [#30 merge upstream/master into oadp-dev](https://github.com/migtools/filebrowser/pull/30) — migtools/filebrowser

**Other** (4)
- [#849 fix: status-reconciler track own config state for dropped deltas](https://github.com/kubernetes-sigs/prow/pull/849) — kubernetes-sigs/prow
- [#7381 PROJQUAY-8767: fix(ui): load all tag history pages](https://github.com/quay/quay/pull/7381) — quay/quay
- [#458 update minio deployment after images were pulled](https://github.com/kubevirt/kubevirt-velero-plugin/pull/458) — kubevirt/kubevirt-velero-plugin
- [#394 feat(network): support internal networks](https://github.com/socktainer/socktainer/pull/394) — socktainer/socktainer
## Issues/PRs Commented On (100)

**velero-io** (52)
- [#10646 Consider enrolling Velero in Anthropic OSS Scanner](https://github.com/velero-io/velero/issues/10646) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#8454 Large PVCs are canceled](https://github.com/velero-io/velero/issues/8454) — velero-io/velero
- [#9189 Support deleting running backups](https://github.com/velero-io/velero/issues/9189) — velero-io/velero
- [#2098 Implement abort running backup job](https://github.com/velero-io/velero/issues/2098) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
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
- [#9744 Bug: Restore stuck in Finalizing phase indefinitely due to unbounded hook-tracker wait](https://github.com/velero-io/velero/issues/9744) — velero-io/velero
- [#8265 Provide S3 plugin that aims to support any S3 compatible object storage.](https://github.com/velero-io/velero/issues/8265) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#10303 Losing the data mover pod leaves the DataUpload InProgress until the 4h ItemOperationTimeout — pod informer has no DeleteFunc](https://github.com/velero-io/velero/issues/10303) — velero-io/velero
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero
- [#10302 Block data mover silently falls back to the filesystem uploader when no volume policy is supplied](https://github.com/velero-io/velero/issues/10302) — velero-io/velero
- [#9964 backup-finalizer retries forever when object-store PUT hits a non-retryable error (e.g. Azure BlobImmutableDueToPolicy 409)](https://github.com/velero-io/velero/issues/9964) — velero-io/velero
- [#10265 Technical Debt: Remove `context.TODO()` in `pkg/util/kube and pkg/util/podvolume`](https://github.com/velero-io/velero/issues/10265) — velero-io/velero
- [#10266 docs: how to run CSI e2e specs against a local Kind cluster](https://github.com/velero-io/velero/issues/10266) — velero-io/velero

**openshift** (9)
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
- [#2403 e2e: Simple backup and restore flow using MinIO w/ TLS certs](https://github.com/openshift/oadp-operator/issues/2403) — openshift/oadp-operator
- [#2413 Poll: how to fix e2e-test-kubevirt-aws hitting the 2h Prow step timeout](https://github.com/openshift/oadp-operator/issues/2413) — openshift/oadp-operator
- [#2407 Migrate Claude e2e failure analysis to shared claude-ai-helpers step-registry pattern](https://github.com/openshift/oadp-operator/issues/2407) — openshift/oadp-operator
- [#10791 Azure CAPZ IPI: bootkube deadlocks forever creating capz-manager-bootstrap-credentials Secret in a namespace that's never created during bootstrap](https://github.com/openshift/installer/issues/10791) — openshift/installer
- [#10590 GCP CAPI: bootstrap in master instance group causes worker ignition failure via ILB pinning](https://github.com/openshift/installer/issues/10590) — openshift/installer
- [#2391 Follow up: simplify and document PodResources defaulting](https://github.com/openshift/oadp-operator/issues/2391) — openshift/oadp-operator

**migtools** (9)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#14 Handle guest agent connectivity and SkipQuiesce for VirtualMachineBackup](https://github.com/migtools/kubevirt-datamover-controller/issues/14) — migtools/kubevirt-datamover-controller
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#84 Implement concurrent data mover limiter for DU and DD controllers](https://github.com/migtools/kubevirt-datamover-controller/issues/84) — migtools/kubevirt-datamover-controller
- [#175 Implement concurrency limiter for DataDownload controller](https://github.com/migtools/kubevirt-datamover-controller/issues/175) — migtools/kubevirt-datamover-controller
- [#184 DataDownload pod config doesn't propagate several BSL fields that DataUpload does](https://github.com/migtools/kubevirt-datamover-controller/issues/184) — migtools/kubevirt-datamover-controller
- [#169 VM run-state restore sibling correlation should scope by restore attempt, not just VM identity](https://github.com/migtools/kubevirt-datamover-controller/issues/169) — migtools/kubevirt-datamover-controller
- [#120 Cancellation cleanup errors are logged but not propagated, phase moves to Canceled regardless](https://github.com/migtools/kubevirt-datamover-controller/issues/120) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller

**Other** (30)
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#17655 [Bug]: Composer: can't insert a second slash-command skill on the same line (needs Shift+Return)](https://github.com/pingdotgg/t3code/issues/17655) — pingdotgg/t3code
- [#17422 [Bug]: Mobile composer stops saving typed text, so the send button stays disabled until the app restarts](https://github.com/pingdotgg/t3code/issues/17422) — pingdotgg/t3code
- [#13875 [Bug]: Claude model picker not synchronized with Claude Code model list, unlike Codex](https://github.com/pingdotgg/t3code/issues/13875) — pingdotgg/t3code
- [#15234 [Feature]: Continue a Codex or Claude Code session started in the terminal as a T3 Code thread](https://github.com/pingdotgg/t3code/issues/15234) — pingdotgg/t3code
- [#26598 Support `strategy.matrix` on the `agent` job for parallel AI execution](https://github.com/github/gh-aw/issues/26598) — github/gh-aw
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
- [#43 Chrome Web Store listing reports location permission](https://github.com/rxliuli/redirector/issues/43) — rxliuli/redirector
- [#868 Feature Request: Add support for editing issue comments](https://github.com/github/github-mcp-server/issues/868) — github/github-mcp-server
- [#201 feat: Add Podman libpod API endpoints for native podman CLI support](https://github.com/socktainer/socktainer/issues/201) — socktainer/socktainer
- [#841 `status-reconciler`: a required context that never once reported can never be retired, permanently deadlocking Tide under `github_merge_blocks_policy: block`](https://github.com/kubernetes-sigs/prow/issues/841) — kubernetes-sigs/prow
## Issues Closed (92)

**velero-io** (29)
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
- [#10050 nits for fine-grained filter docs](https://github.com/velero-io/velero/issues/10050) — velero-io/velero
- [#10023 Ginkgo CLI Version Mismatch GoMod Import](https://github.com/velero-io/velero/issues/10023) — velero-io/velero
- [#10029 Flaky test: TestKopiaObjectWriterEx_ConcurrentAsyncErrors can observe async error before all writes are queued](https://github.com/velero-io/velero/issues/10029) — velero-io/velero
- [#10048 CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/issues/10048) — velero-io/velero

**openshift** (16)
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
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero
- [#443 OADP-7384: ImageStream backup fails with `manifest unknown` when a status tag item references another namespace's repository and that reference is stale](https://github.com/openshift/openshift-velero-plugin/issues/443) — openshift/openshift-velero-plugin
- [#552 Configure required_status_checks.contexts in Prow branch protection (velero + plugin forks)](https://github.com/openshift/velero/issues/552) — openshift/velero

**migtools** (21)
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
- [#118 lint workflow is using node20](https://github.com/migtools/kubevirt-datamover-controller/issues/118) — migtools/kubevirt-datamover-controller
- [#108 evaluateVMBackupStatus misses real VMBackup failures due to exact-match on Progressing.Reason=="Failed"](https://github.com/migtools/kubevirt-datamover-controller/issues/108) — migtools/kubevirt-datamover-controller
- [#112 Temp backup PVC hardcoded to 10Gi (ensureTempPVC), causing silent backup failures for larger disks](https://github.com/migtools/kubevirt-datamover-controller/issues/112) — migtools/kubevirt-datamover-controller

**Other** (26)
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
- [#121 [FEATURE] Matrix Strategy Multi-Arch example](https://github.com/redhat-actions/buildah-build/issues/121) — redhat-actions/buildah-build
- [#330 Omit  ANTHROPIC_MODEL: sonnetModel ?? opusModel, from claude-code so selected model option sticks](https://github.com/caozhiyuan/copilot-api/issues/330) — caozhiyuan/copilot-api
- [#1807 Support Google Vertex AI with Application Default Credentials (ADC)](https://github.com/pingdotgg/t3code/issues/1807) — pingdotgg/t3code
- [#164 Transient curl failures during kind/kubectl download abort the whole job (no retry)](https://github.com/helm/kind-action/issues/164) — helm/kind-action
- [#15702 Subsequent funnel of the same name from different node breaks HTTPS](https://github.com/tailscale/tailscale/issues/15702) — tailscale/tailscale
- [#318 Should also have an environment variable for the default Opus model, allowing opus+sonnet+haiku usage.](https://github.com/caozhiyuan/copilot-api/issues/318) — caozhiyuan/copilot-api
- [#317 Command used when Vertex AI is set up for Claude Code does not override Vertex AI.](https://github.com/caozhiyuan/copilot-api/issues/317) — caozhiyuan/copilot-api
- [#18471 IncrementalBackup: backup fails with "No space left on device" shortly after creating the qcow2 metadata overlay, unrelated to any volume's real free space](https://github.com/kubevirt/kubevirt/issues/18471) — kubevirt/kubevirt
- [#81 https://www.google.com/maps/ -> https://www.google.com/maps/?authuser=1](https://github.com/URLAutoRedirector/URLAutoRedirector/issues/81) — URLAutoRedirector/URLAutoRedirector
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
