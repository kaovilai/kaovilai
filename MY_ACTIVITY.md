# Activity Log

> **Period:** 2026-09-22 — 2026-10-06
> **Generated:** 2026-10-06 22:56:01 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 13 |
| PRs Opened | 15 |
| PRs Reviewed | 46 |
| Issues/PRs Commented | 20 |
| Issues Closed | 4 |

---

## PRs Merged (13)

**velero-io** (5)
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero
- [#10077 Add Dependabot auto-approve workflow](https://github.com/velero-io/velero/pull/10077) — velero-io/velero
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero
- [#9646 Fix backup-finalizer: do not set backup phase to Completed before PutBackupMetadata succeeds](https://github.com/velero-io/velero/pull/9646) — velero-io/velero
- [#10275 Implement namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10275) — velero-io/velero

**openshift** (1)
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator

**migtools** (1)
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore

**Other** (6)
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#188 Fix review queue card deadspace](https://github.com/kaovilai/kaovilai.pw/pull/188) — kaovilai/kaovilai.pw
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
## PRs Opened (15)

**velero-io** (2)
- [#10608 fix: regenerate CRD manifests for the status.activities field](https://github.com/velero-io/velero/pull/10608) — velero-io/velero
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero

**openshift** (1)
- [#2473 fix(e2e): route/proxy 503 fallback and empty checksum exec flakes](https://github.com/openshift/oadp-operator/pull/2473) — openshift/oadp-operator

**migtools** (1)
- [#192 Fix CI coverage handling for no-test packages and update setup-go](https://github.com/migtools/udistribution/pull/192) — migtools/udistribution

**Other** (11)
- [#189 fix(combo): don't re-submit form while GitHub's post is still in flight](https://github.com/kaovilai/github-bot-command-palette/pull/189) — kaovilai/github-bot-command-palette
- [#188 fix(rehearse): accept gcs.ci.openshift.org listing URLs for full job list](https://github.com/kaovilai/github-bot-command-palette/pull/188) — kaovilai/github-bot-command-palette
- [#2 fix: address shubham's review feedback on DPT CACertRef handling](https://github.com/msfrucht/oadp-operator/pull/2) — msfrucht/oadp-operator
- [#386 Make chain previews and panels respond to touch taps](https://github.com/kaovilai/fidelity-margin-calculator-auto/pull/386) — kaovilai/fidelity-margin-calculator-auto
- [#1 fix: remove unused bsl parameter (golangci-lint unparam)](https://github.com/msfrucht/oadp-operator/pull/1) — msfrucht/oadp-operator
- [#126897 fix(copilot): send captured backend apiVersion to unlock 1M context](https://github.com/NousResearch/hermes-agent/pull/126897) — NousResearch/hermes-agent
- [#124184 fix(desktop): recognize Copilot's dash-suffixed 1M-context model ids](https://github.com/NousResearch/hermes-agent/pull/124184) — NousResearch/hermes-agent
- [#123138 fix(tools): hard-fail message_agent on a profile's old, renamed-away name](https://github.com/NousResearch/hermes-agent/pull/123138) — NousResearch/hermes-agent
- [#122945 fix(tools): re-derive dependency env in bot_mode_dm background runner](https://github.com/NousResearch/hermes-agent/pull/122945) — NousResearch/hermes-agent
- [#121974 feat(browser): recognize Comet, BrowserOS neo, Vivaldi, Opera, Opera GX, and Yandex for real-profile browsing](https://github.com/NousResearch/hermes-agent/pull/121974) — NousResearch/hermes-agent
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
## PRs Reviewed (46)

**velero-io** (14)
- [#10588 e2e: make the StorageClass names configurable](https://github.com/velero-io/velero/pull/10588) — velero-io/velero
- [#10596 e2e: add a script to install CSI snapshot support on kind](https://github.com/velero-io/velero/pull/10596) — velero-io/velero
- [#10622 Bump the github-actions group with 2 updates](https://github.com/velero-io/velero/pull/10622) — velero-io/velero
- [#10617 docs: fix contributor and maintainer guidance links](https://github.com/velero-io/velero/pull/10617) — velero-io/velero
- [#10556 [Design]Owner reference and dependency relink design](https://github.com/velero-io/velero/pull/10556) — velero-io/velero
- [#2 Document maintainer lifecycle, affiliation policy, and Code of Conduct](https://github.com/velero-io/.github/pull/2) — velero-io/.github
- [#10572 Add architecture entry point and roadmap change process](https://github.com/velero-io/velero/pull/10572) — velero-io/velero
- [#10612 fix: defer VGS cleanup until backup finalization](https://github.com/velero-io/velero/pull/10612) — velero-io/velero
- [#10601 Detect VolumeGroupSnapshot API version at runtime (v1/v1beta2/v1beta1)](https://github.com/velero-io/velero/pull/10601) — velero-io/velero
- [#10570 [WIP] Warn when the volume data of an existing PVC backed up by snapshot is not restored](https://github.com/velero-io/velero/pull/10570) — velero-io/velero
- [#10590 docs: fix broken internal links and anchors in main docs](https://github.com/velero-io/velero/pull/10590) — velero-io/velero
- [#10578 Enable VGDP soothing by default and set queue length as 5](https://github.com/velero-io/velero/pull/10578) — velero-io/velero
- [#10579 Change hashing algorithm to HMAC-SHA256-128 for kopia repo](https://github.com/velero-io/velero/pull/10579) — velero-io/velero
- [#10568 Document maintainer contact info and shared responsibility](https://github.com/velero-io/velero/pull/10568) — velero-io/velero

**openshift** (22)
- [#2475 fix(e2e): add retry logic for empty sha256sum output in checksum helpers](https://github.com/openshift/oadp-operator/pull/2475) — openshift/oadp-operator
- [#2466 [oadp-1.4] OADP-8835: feat(bsl): concatenate all CA certificates from BSLs and include system defaults](https://github.com/openshift/oadp-operator/pull/2466) — openshift/oadp-operator
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
- [#480 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (4ae9c74) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/480) — openshift/openshift-velero-plugin
- [#99 Remove obsolete bz-on-pr-create workflow](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/99) — openshift/velero-plugin-for-legacy-aws
- [#110 Remove obsolete bz-on-pr-create workflow](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/110) — openshift/velero-plugin-for-legacy-aws
- [#578 Pin Bitnami MinIO source for kind E2E tests](https://github.com/openshift/velero/pull/578) — openshift/velero

**migtools** (8)
- [#69 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (dc932cf) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/69) — migtools/kubevirt-datamover-plugin
- [#96 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.9.1 (6d1f840) into oadp-1.6](https://github.com/migtools/kubevirt-velero-plugin/pull/96) — migtools/kubevirt-velero-plugin
- [#276 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (f5ba313) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/276) — migtools/oadp-cli
- [#110 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (a725c94) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/110) — migtools/oadp-vm-file-restore
- [#241 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-1.6 (6a1a241) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/241) — migtools/kubevirt-datamover-controller
- [#387 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (24ca6dd) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/387) — migtools/oadp-non-admin
- [#54 fix(gcs): use service-account credential options](https://github.com/migtools/kopia/pull/54) — migtools/kopia
- [#39 fix(gcs): use service-account credential options](https://github.com/migtools/oadp-vmdp/pull/39) — migtools/oadp-vmdp

**Other** (2)
- [#7381 PROJQUAY-8767: fix(ui): load all tag history pages](https://github.com/quay/quay/pull/7381) — quay/quay
- [#458 update minio deployment after images were pulled](https://github.com/kubevirt/kubevirt-velero-plugin/pull/458) — kubevirt/kubevirt-velero-plugin
## Issues/PRs Commented On (20)

**velero-io** (11)
- [#9189 Support deleting running backups](https://github.com/velero-io/velero/issues/9189) — velero-io/velero
- [#2098 Implement abort running backup job](https://github.com/velero-io/velero/issues/2098) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#10299 Backup with --snapshot-move-data completes with zero DataUploads when EnableCSI is off — no upfront validation, and the warning/skip-reason don't name the flag](https://github.com/velero-io/velero/issues/10299) — velero-io/velero
- [#10310 Include the errors/warnings from node-agent and data-mover pods in the velero backup/restore get/describe commands](https://github.com/velero-io/velero/issues/10310) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#9735 Velero should add a clear error when data mover pod is unschedulable due to affinity/topology mismatch](https://github.com/velero-io/velero/issues/9735) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero

**openshift** (1)
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer

**Other** (8)
- [#190 Web Camera is broken](https://github.com/EmixamPP/linux-enable-ir-emitter/issues/190) — EmixamPP/linux-enable-ir-emitter
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#4300 cdi-importer image sha256:b2241514d6f3... missing amd64 manifest (only s390x)](https://github.com/kubevirt/containerized-data-importer/issues/4300) — kubevirt/containerized-data-importer
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#12543 Issue can land permanently blocked on a "recovery owner"/disposition state when the run that created it terminates](https://github.com/paperclipai/paperclip/issues/12543) — paperclipai/paperclip
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
## Issues Closed (4)

**velero-io** (4)
- [#10076 Dependabot auto approve action](https://github.com/velero-io/velero/issues/10076) — velero-io/velero
- [#10564 E2E test coverage for namespace selection by label in resource policy](https://github.com/velero-io/velero/issues/10564) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
