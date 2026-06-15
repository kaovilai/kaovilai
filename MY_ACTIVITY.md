# Activity Log

> **Period:** 2026-06-01 — 2026-06-15
> **Generated:** 2026-06-15 11:59:21 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 4 |
| PRs Opened | 8 |
| PRs Reviewed | 40 |
| Issues/PRs Commented | 28 |
| Issues Closed | 7 |

---

## PRs Merged (4)

**openshift** (4)
- [#405 [oadp-1.4] OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/405) — openshift/openshift-velero-plugin
- [#406 fix: mock GetBucketRegion in shared_test.go](https://github.com/openshift/openshift-velero-plugin/pull/406) — openshift/openshift-velero-plugin
- [#402 OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/402) — openshift/openshift-velero-plugin
- [#268 [oadp-1.5] fix: scope go.work gitignore patterns to root only](https://github.com/openshift/hypershift-oadp-plugin/pull/268) — openshift/hypershift-oadp-plugin
## PRs Opened (8)

**velero-io** (1)
- [#9910 feat: add CRD schema validation during server startup](https://github.com/velero-io/velero/pull/9910) — velero-io/velero

**openshift** (5)
- [#2234 OADP-7541: fix non-deterministic matchExpressions ordering causing node-agent restarts](https://github.com/openshift/oadp-operator/pull/2234) — openshift/oadp-operator
- [#406 fix: mock GetBucketRegion in shared_test.go](https://github.com/openshift/openshift-velero-plugin/pull/406) — openshift/openshift-velero-plugin
- [#405 [oadp-1.4] OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/405) — openshift/openshift-velero-plugin
- [#404 [oadp-1.5] OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/404) — openshift/openshift-velero-plugin
- [#402 OADP-6540: Skip restore of k8s RBAC system rolebindings](https://github.com/openshift/openshift-velero-plugin/pull/402) — openshift/openshift-velero-plugin

**migtools** (1)
- [#83 Phase 0+1: DataDownload prerequisites and shared helper extraction](https://github.com/migtools/kubevirt-datamover-controller/pull/83) — migtools/kubevirt-datamover-controller

**Other** (1)
- [#129 feat: add CRD schema validation during server startup](https://github.com/kaovilai/velero/pull/129) — kaovilai/velero
## PRs Reviewed (40)

**velero-io** (13)
- [#9906 feat(resourcepolicies): support PVC volume mode and access mode matching](https://github.com/velero-io/velero/pull/9906) — velero-io/velero
- [#9913 Clone pv on rebind](https://github.com/velero-io/velero/pull/9913) — velero-io/velero
- [#9903 Apply ResourceModifier rules during restore finalization for dynamic PVs](https://github.com/velero-io/velero/pull/9903) — velero-io/velero
- [#9909 [release-1.18] Add external-snapshotter version requirement to VGS docs](https://github.com/velero-io/velero/pull/9909) — velero-io/velero
- [#9870 Fix backup performance regression with includedNamespaces ["*"]](https://github.com/velero-io/velero/pull/9870) — velero-io/velero
- [#9887 Incremental aware object writer - writeat](https://github.com/velero-io/velero/pull/9887) — velero-io/velero
- [#9899 Refactor object writer interface](https://github.com/velero-io/velero/pull/9899) — velero-io/velero
- [#9888 Design: propose PVC volume mode and access mode criteria](https://github.com/velero-io/velero/pull/9888) — velero-io/velero
- [#9880 implemented fine-grained backup filter policies](https://github.com/velero-io/velero/pull/9880) — velero-io/velero
- [#303 fix: skip x-amz-tagging header when tagging is empty](https://github.com/velero-io/velero-plugin-for-aws/pull/303) — velero-io/velero-plugin-for-aws
- [#9881 cli support for fine-grained filter policies](https://github.com/velero-io/velero/pull/9881) — velero-io/velero
- [#9883 [cherry-pick][1.18] Fix unknown containerd config version error in run-e2e-test action](https://github.com/velero-io/velero/pull/9883) — velero-io/velero
- [#9875 Repo snapshot operation enhance](https://github.com/velero-io/velero/pull/9875) — velero-io/velero

**openshift** (17)
- [#2235 remove hypershift from oadp-1.4](https://github.com/openshift/oadp-operator/pull/2235) — openshift/oadp-operator
- [#80303 OADP-8083: Added Prow CI for oadp-1.5 oadp-cli](https://github.com/openshift/release/pull/80303) — openshift/release
- [#80380 remove hcp from oadp 1.4 jobs](https://github.com/openshift/release/pull/80380) — openshift/release
- [#10586 no-jira: GCP Destroy: Group Load Balancer Resources & Retry on Errors](https://github.com/openshift/installer/pull/10586) — openshift/installer
- [#80356 Add OADP 1.5 image build and mirroring for hypershift-oadp-plugin](https://github.com/openshift/release/pull/80356) — openshift/release
- [#274 fix: use golang-1.25-openshift-4.22 builder image on oadp-1.5](https://github.com/openshift/hypershift-oadp-plugin/pull/274) — openshift/hypershift-oadp-plugin
- [#112544 OADP-6673: Add OADP 1.6.0 RNs](https://github.com/openshift/openshift-docs/pull/112544) — openshift/openshift-docs
- [#2229 [oadp-dev] public velero ref 1.18.1 to match openshift/velero replace](https://github.com/openshift/oadp-operator/pull/2229) — openshift/oadp-operator
- [#103 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (c6abec6) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/103) — openshift/oadp-must-gather
- [#271 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (0742331) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/271) — openshift/hypershift-oadp-plugin
- [#2231 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (f9a4a08) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2231) — openshift/oadp-operator
- [#401 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (da98cea) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/401) — openshift/openshift-velero-plugin
- [#58 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (71d3f52) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/58) — openshift/velero-plugin-for-legacy-aws
- [#131 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.1 (6902b36) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/131) — openshift/velero-plugin-for-gcp
- [#135 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.1 (6fb0379) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/135) — openshift/velero-plugin-for-microsoft-azure
- [#136 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.14.1 (96a651c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-aws/pull/136) — openshift/velero-plugin-for-aws
- [#512 UPSTREAM: 9870: Fix backup performance regression with includedNamespaces ["*"]](https://github.com/openshift/velero/pull/512) — openshift/velero

**migtools** (7)
- [#198 Prompts user to choose when more than one NABSL exists](https://github.com/migtools/oadp-cli/pull/198) — migtools/oadp-cli
- [#20 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (ef0cf55) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/20) — migtools/kubevirt-datamover-plugin
- [#81 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-1.6 (9169b8d) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/81) — migtools/kubevirt-datamover-controller
- [#195 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (a975937) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/195) — migtools/oadp-cli
- [#84 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (0a22f05) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/84) — migtools/oadp-vm-file-restore
- [#347 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (54d1934) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/347) — migtools/oadp-non-admin
- [#65 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.9.0 (d2e45cc) into oadp-1.6](https://github.com/migtools/kubevirt-velero-plugin/pull/65) — migtools/kubevirt-velero-plugin

**Other** (3)
- [#43 Add pre-rebase hook to verify upstream Velero tag SHA](https://github.com/oadp-rebasebot/oadp-rebase/pull/43) — oadp-rebasebot/oadp-rebase
- [#4863 Mark Velero as a CNCF Sandbox project (accepted 2026-03-11)](https://github.com/cncf/landscape/pull/4863) — cncf/landscape
- [#244 Delay Atlassian auth redirect checks until page load settles](https://github.com/kaovilai/tampermonkey-scripts-pub/pull/244) — kaovilai/tampermonkey-scripts-pub
## Issues/PRs Commented On (28)

**velero-io** (13)
- [#8264 Velero 1.14.1 & aws plugin 1.10.1: api error SignatureDoesNotMatch](https://github.com/velero-io/velero/issues/8264) — velero-io/velero
- [#9907 Performance improvement for the GetNamespaceFilter call](https://github.com/velero-io/velero/issues/9907) — velero-io/velero
- [#2812 Restore fails with error "no space left on device" if PVCs are 100% utilised during backup](https://github.com/velero-io/velero/issues/2812) — velero-io/velero
- [#9894 Transition all project meetings to CNCF Zoom](https://github.com/velero-io/velero/issues/9894) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9897 Nondeterministic affinity ordering in ToSystemAffinity causes spurious spec diffs and restarts](https://github.com/velero-io/velero/issues/9897) — velero-io/velero
- [#9876 Evaluate and onboard Dosu (AI maintainer assistant) for velero-io](https://github.com/velero-io/velero/issues/9876) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#9483 Remove Restic from Velero Doc](https://github.com/velero-io/velero/issues/9483) — velero-io/velero
- [#2098 Implement abort running backup job](https://github.com/velero-io/velero/issues/2098) — velero-io/velero
- [#4707 restore with object metadata.ownerreference and metadata.finalizer](https://github.com/velero-io/velero/issues/4707) — velero-io/velero
- [#7774 Volume Policy -- add more logs when a volume is skipped](https://github.com/velero-io/velero/issues/7774) — velero-io/velero

**openshift** (3)
- [#10584 GCP destroy: instance group deletion fails due to dependency ordering with backend services](https://github.com/openshift/installer/issues/10584) — openshift/installer
- [#2218 Agentic SDLC for OADP](https://github.com/openshift/oadp-operator/issues/2218) — openshift/oadp-operator
- [#10590 GCP CAPI: bootstrap in master instance group causes worker ignition failure via ILB pinning](https://github.com/openshift/installer/issues/10590) — openshift/installer

**migtools** (3)
- [#161 Unable to run crane imag](https://github.com/migtools/crane/issues/161) — migtools/crane
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#74 Force full backup when BSL checkpoint validation fails](https://github.com/migtools/kubevirt-datamover-controller/issues/74) — migtools/kubevirt-datamover-controller

**Other** (9)
- [#6786 Build cancellation leaves orphaned QEMU processes: no timeout on state polling loop](https://github.com/podman-container-tools/buildah/issues/6786) — podman-container-tools/buildah
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
- [#42 Add mechanism to detect tag drifts](https://github.com/oadp-rebasebot/oadp-rebase/issues/42) — oadp-rebasebot/oadp-rebase
- [#101 Future: UDP proxy](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#2229 feat: add `list_pull_request_review_threads` tool to expose PRRT_ node IDs for resolving threads](https://github.com/github/github-mcp-server/issues/2229) — github/github-mcp-server
- [#1209 Unable to create 100MiB PVC from snapshot created from 100MiB PVC](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/issues/1209) — kubernetes-sigs/aws-ebs-csi-driver
- [#473 [PROJECT ONBOARDING] Velero](https://github.com/cncf/sandbox/issues/473) — cncf/sandbox
- [#28439 podman machine start reports success on macOS Apple Silicon, but VM falls into emergency mode with Ignition/fsck root UUID errors](https://github.com/podman-container-tools/podman/issues/28439) — podman-container-tools/podman
## Issues Closed (7)

**velero-io** (2)
- [#9897 Nondeterministic affinity ordering in ToSystemAffinity causes spurious spec diffs and restarts](https://github.com/velero-io/velero/issues/9897) — velero-io/velero
- [#9790 Restore validation should reject restores from backups in Deleting phase](https://github.com/velero-io/velero/issues/9790) — velero-io/velero

**openshift** (1)
- [#2218 Agentic SDLC for OADP](https://github.com/openshift/oadp-operator/issues/2218) — openshift/oadp-operator

**Other** (4)
- [#10 track: exotic-arch builds (ppc64le, s390x, riscv64) — Apple QEMU support or mocker workaround](https://github.com/us/mocker/issues/10) — us/mocker
- [#246 exclude `cncfservicedesk.atlassian.net`](https://github.com/kaovilai/tampermonkey-scripts-pub/issues/246) — kaovilai/tampermonkey-scripts-pub
- [#242 "Log in to Jira to see this work item" do not get redirected](https://github.com/kaovilai/tampermonkey-scripts-pub/issues/242) — kaovilai/tampermonkey-scripts-pub
- [#239 Delay Atlassian login detection to allow site to fully load](https://github.com/kaovilai/tampermonkey-scripts-pub/issues/239) — kaovilai/tampermonkey-scripts-pub
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
