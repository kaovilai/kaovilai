# Activity Log

> **Period:** 2026-09-24 — 2026-10-08
> **Generated:** 2026-10-08 23:40:57 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 11 |
| PRs Opened | 13 |
| PRs Reviewed | 38 |
| Issues/PRs Commented | 19 |
| Issues Closed | 2 |

---

## PRs Merged (11)

**velero-io** (4)
- [#10051 docs: use consistent excludedNames glob pattern in filter design examples](https://github.com/velero-io/velero/pull/10051) — velero-io/velero
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero
- [#10077 Add Dependabot auto-approve workflow](https://github.com/velero-io/velero/pull/10077) — velero-io/velero
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero

**openshift** (1)
- [#86664 Add release-4.21 to Prow configuration branches](https://github.com/openshift/release/pull/86664) — openshift/release

**migtools** (1)
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore

**Other** (5)
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#188 Fix review queue card deadspace](https://github.com/kaovilai/kaovilai.pw/pull/188) — kaovilai/kaovilai.pw
## PRs Opened (13)

**velero-io** (1)
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero

**openshift** (2)
- [#86664 Add release-4.21 to Prow configuration branches](https://github.com/openshift/release/pull/86664) — openshift/release
- [#2473 fix(e2e): route/proxy 503 fallback and empty checksum exec flakes](https://github.com/openshift/oadp-operator/pull/2473) — openshift/oadp-operator

**migtools** (1)
- [#192 Fix CI coverage handling for no-test packages and update setup-go](https://github.com/migtools/udistribution/pull/192) — migtools/udistribution

**Other** (9)
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#126897 fix(copilot): send captured backend apiVersion to unlock 1M context](https://github.com/NousResearch/hermes-agent/pull/126897) — NousResearch/hermes-agent
- [#124184 fix(desktop): recognize Copilot's dash-suffixed 1M-context model ids](https://github.com/NousResearch/hermes-agent/pull/124184) — NousResearch/hermes-agent
- [#123138 fix(tools): hard-fail message_agent on a profile's old, renamed-away name](https://github.com/NousResearch/hermes-agent/pull/123138) — NousResearch/hermes-agent
- [#122945 fix(tools): re-derive dependency env in bot_mode_dm background runner](https://github.com/NousResearch/hermes-agent/pull/122945) — NousResearch/hermes-agent
- [#121974 feat(browser): recognize Comet, BrowserOS neo, Vivaldi, Opera, Opera GX, and Yandex for real-profile browsing](https://github.com/NousResearch/hermes-agent/pull/121974) — NousResearch/hermes-agent
## PRs Reviewed (38)

**velero-io** (15)
- [#10630 e2e: document running the CSI cases on kind](https://github.com/velero-io/velero/pull/10630) — velero-io/velero
- [#10598 e2e: add VolumeGroupSnapshot coverage](https://github.com/velero-io/velero/pull/10598) — velero-io/velero
- [#10609 docs: add local Kind setup for CSI e2e](https://github.com/velero-io/velero/pull/10609) — velero-io/velero
- [#10588 e2e: make the StorageClass definitions configurable](https://github.com/velero-io/velero/pull/10588) — velero-io/velero
- [#10631 Fix the MinIO image cache key in the kind e2e workflow](https://github.com/velero-io/velero/pull/10631) — velero-io/velero
- [#10621 fix(controller): propagate context during backup request preparation](https://github.com/velero-io/velero/pull/10621) — velero-io/velero
- [#10593 e2e: verify CSI snapshots on kind](https://github.com/velero-io/velero/pull/10593) — velero-io/velero
- [#10596 e2e: add a script to install CSI snapshot support on kind](https://github.com/velero-io/velero/pull/10596) — velero-io/velero
- [#10622 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10622) — velero-io/velero
- [#10617 docs: fix contributor and maintainer guidance links](https://github.com/velero-io/velero/pull/10617) — velero-io/velero
- [#10612 fix: defer VGS cleanup until backup finalization](https://github.com/velero-io/velero/pull/10612) — velero-io/velero
- [#10601 Detect VolumeGroupSnapshot API version at runtime (v1/v1beta2/v1beta1)](https://github.com/velero-io/velero/pull/10601) — velero-io/velero
- [#10590 docs: fix broken internal links and anchors in main docs](https://github.com/velero-io/velero/pull/10590) — velero-io/velero
- [#10578 Enable VGDP soothing by default and set queue length as 5](https://github.com/velero-io/velero/pull/10578) — velero-io/velero
- [#10579 Change hashing algorithm to HMAC-SHA256-128 for kopia repo](https://github.com/velero-io/velero/pull/10579) — velero-io/velero

**openshift** (19)
- [#2478 Fix VeleroIsDeleted GC race and GetPodWithLabel rollout flake](https://github.com/openshift/oadp-operator/pull/2478) — openshift/oadp-operator
- [#321 OADP-8726: Remove committed kubeconfig with system:masters credentials](https://github.com/openshift/hypershift-oadp-plugin/pull/321) — openshift/hypershift-oadp-plugin
- [#2475 fix(e2e): add retry logic for empty sha256sum output in checksum helpers](https://github.com/openshift/oadp-operator/pull/2475) — openshift/oadp-operator
- [#2474 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (fcf7610) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2474) — openshift/oadp-operator
- [#118 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (33ef7bd) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/118) — openshift/velero-plugin-for-legacy-aws
- [#319 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (45480df) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/319) — openshift/hypershift-oadp-plugin
- [#178 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.4 (d173fa9) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/178) — openshift/velero-plugin-for-gcp
- [#318 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (636bec3) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/318) — openshift/hypershift-oadp-plugin
- [#586 Detect VolumeGroupSnapshot API version at runtime (v1/v1beta2/v1beta1) (#10601)](https://github.com/openshift/velero/pull/586) — openshift/velero
- [#2470 [oadp-1.6] test(e2e): pin MinIO to migtools Bitnami image](https://github.com/openshift/oadp-operator/pull/2470) — openshift/oadp-operator
- [#2469 test(e2e): pin MinIO to migtools Bitnami image](https://github.com/openshift/oadp-operator/pull/2469) — openshift/oadp-operator
- [#174 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-aws/pull/174) — openshift/velero-plugin-for-aws
- [#173 Remove bz-pr-action GitHub Actions workflow](https://github.com/openshift/velero-plugin-for-aws/pull/173) — openshift/velero-plugin-for-aws
- [#583 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero/pull/583) — openshift/velero
- [#482 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/openshift-velero-plugin/pull/482) — openshift/openshift-velero-plugin
- [#175 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/175) — openshift/velero-plugin-for-microsoft-azure
- [#175 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/velero-plugin-for-gcp/pull/175) — openshift/velero-plugin-for-gcp
- [#69 Remove obsolete bz-on-pr-merge workflow](https://github.com/openshift/restic/pull/69) — openshift/restic
- [#582 Remove bz-pr-action GitHub Actions workflow](https://github.com/openshift/velero/pull/582) — openshift/velero

**migtools** (3)
- [#69 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (dc932cf) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/69) — migtools/kubevirt-datamover-plugin
- [#96 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.9.1 (6d1f840) into oadp-1.6](https://github.com/migtools/kubevirt-velero-plugin/pull/96) — migtools/kubevirt-velero-plugin
- [#276 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (f5ba313) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/276) — migtools/oadp-cli

**Other** (1)
- [#458 update minio deployment after images were pulled](https://github.com/kubevirt/kubevirt-velero-plugin/pull/458) — kubevirt/kubevirt-velero-plugin
## Issues/PRs Commented On (19)

**velero-io** (7)
- [#9189 Support deleting running backups](https://github.com/velero-io/velero/issues/9189) — velero-io/velero
- [#2098 Implement abort running backup job](https://github.com/velero-io/velero/issues/2098) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#10299 Backup with --snapshot-move-data completes with zero DataUploads when EnableCSI is off — no upfront validation, and the warning/skip-reason don't name the flag](https://github.com/velero-io/velero/issues/10299) — velero-io/velero
- [#10310 Include the errors/warnings from node-agent and data-mover pods in the velero backup/restore get/describe commands](https://github.com/velero-io/velero/issues/10310) — velero-io/velero

**openshift** (1)
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer

**Other** (11)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#26598 Support `strategy.matrix` on the `agent` job for parallel AI execution](https://github.com/github/gh-aw/issues/26598) — github/gh-aw
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
- [#4300 cdi-importer image sha256:b2241514d6f3... missing amd64 manifest (only s390x)](https://github.com/kubevirt/containerized-data-importer/issues/4300) — kubevirt/containerized-data-importer
- [#101 UDP support](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#12543 Issue can land permanently blocked on a "recovery owner"/disposition state when the run that created it terminates](https://github.com/paperclipai/paperclip/issues/12543) — paperclipai/paperclip
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
## Issues Closed (2)

**velero-io** (2)
- [#10076 Dependabot auto approve action](https://github.com/velero-io/velero/issues/10076) — velero-io/velero
- [#10564 E2E test coverage for namespace selection by label in resource policy](https://github.com/velero-io/velero/issues/10564) — velero-io/velero
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
