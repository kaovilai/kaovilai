# Activity Log

> **Period:** 2026-04-20 — 2026-05-04
> **Generated:** 2026-05-04 10:36:00 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 8 |
| PRs Opened | 9 |
| PRs Reviewed | 31 |
| Issues/PRs Commented | 23 |
| Issues Closed | 4 |

---

## PRs Merged (8)

**openshift** (8)
- [#500 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/500) — openshift/velero
- [#498 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest, migrate config](https://github.com/openshift/velero/pull/498) — openshift/velero
- [#501 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/501) — openshift/velero
- [#2109 OADP-5777: Require region in BSL validation when s3Url is set, fix nil config skipping region auto-detection](https://github.com/openshift/oadp-operator/pull/2109) — openshift/oadp-operator
- [#78204 feat: update hypershift-oadp-plugin CI configuration and image mapping](https://github.com/openshift/release/pull/78204) — openshift/release
- [#129 oadp-1.3: OADP-7568,OADP-7571: Fix CVEs: bump Go to 1.25.8, update dependencies](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/129) — openshift/velero-plugin-for-microsoft-azure
- [#125 oadp-1.3: OADP-7568,OADP-7571: Fix CVEs: bump Go to 1.25.8, update dependencies](https://github.com/openshift/velero-plugin-for-gcp/pull/125) — openshift/velero-plugin-for-gcp
- [#393 Bump Go dependencies to fix CVEs (Trivy scan)](https://github.com/openshift/openshift-velero-plugin/pull/393) — openshift/openshift-velero-plugin
## PRs Opened (9)

**openshift** (4)
- [#501 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/501) — openshift/velero
- [#500 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/500) — openshift/velero
- [#2184 Increase Fedora VM startup timeout to 20 minutes](https://github.com/openshift/oadp-operator/pull/2184) — openshift/oadp-operator
- [#78204 feat: update hypershift-oadp-plugin CI configuration and image mapping](https://github.com/openshift/release/pull/78204) — openshift/release

**Other** (5)
- [#8 feat: implement Docker/Podman socket compatibility via launchd activation](https://github.com/us/mocker/pull/8) — us/mocker
- [#9772 Design: namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/9772) — velero-io/velero
- [#9770 design: Kubernetes name length enforcement for Velero-created objects (#8815)](https://github.com/velero-io/velero/pull/9770) — velero-io/velero
- [#1381 Update project-maintainers.csv for velero.io](https://github.com/cncf/foundation/pull/1381) — cncf/foundation
- [#1 Fix arucogen SVG support, detection robustness, and memory leaks](https://github.com/kbralten/aruco_online/pull/1) — kbralten/aruco_online
## PRs Reviewed (31)

**openshift** (16)
- [#2187 OADP-7882: add dpa config to disable early csi polling interval](https://github.com/openshift/oadp-operator/pull/2187) — openshift/oadp-operator
- [#2179 feat: add KubevirtDatamoverConfig to DPA for max incremental backups](https://github.com/openshift/oadp-operator/pull/2179) — openshift/oadp-operator
- [#499 Optimize VSC handle readiness polling for VSS backups (cp from upstream 1.18)](https://github.com/openshift/velero/pull/499) — openshift/velero
- [#2182 [oadp-1.6] OADP-5777: Require region in BSL validation when s3Url is set, fix nil config skipping region auto-detection](https://github.com/openshift/oadp-operator/pull/2182) — openshift/oadp-operator
- [#2174 Kubevirt datamover e2e](https://github.com/openshift/oadp-operator/pull/2174) — openshift/oadp-operator
- [#2181 OADP-7882: add dpa config to disable early csi polling interval](https://github.com/openshift/oadp-operator/pull/2181) — openshift/oadp-operator
- [#2178 install upstream nightly build of kubevirt and HCO](https://github.com/openshift/oadp-operator/pull/2178) — openshift/oadp-operator
- [#91 OADP-1.6 must-gather updates](https://github.com/openshift/oadp-must-gather/pull/91) — openshift/oadp-must-gather
- [#2180 [oadp-1.6] OADP-7869: Fix stale resourceAnnotations/resourceLabels after DPA patch](https://github.com/openshift/oadp-operator/pull/2180) — openshift/oadp-operator
- [#2176 OADP-7869: Fix stale resourceAnnotations/resourceLabels after DPA patch](https://github.com/openshift/oadp-operator/pull/2176) — openshift/oadp-operator
- [#90 OADP-7872: Add VM file restore CRDs to must-gather](https://github.com/openshift/oadp-must-gather/pull/90) — openshift/oadp-must-gather
- [#2177 [oadp-1.6] Pass DATAMOVER_IMAGE env var to kubevirt-datamover-controller deployment](https://github.com/openshift/oadp-operator/pull/2177) — openshift/oadp-operator
- [#2172 Pass DATAMOVER_IMAGE env var to kubevirt-datamover-controller deployment](https://github.com/openshift/oadp-operator/pull/2172) — openshift/oadp-operator
- [#2170 OADP-7868: Skip CLI/VMDP download setup when Console CRD is absent](https://github.com/openshift/oadp-operator/pull/2170) — openshift/oadp-operator
- [#396 [oadp-1.6] OADP-6693: Propagate reclaim space schedule annotation to restored PVCs](https://github.com/openshift/openshift-velero-plugin/pull/396) — openshift/openshift-velero-plugin
- [#395 OADP-6693: Propagate reclaim space schedule annotation to restored PVCs](https://github.com/openshift/openshift-velero-plugin/pull/395) — openshift/openshift-velero-plugin

**migtools** (8)
- [#59 feat: add --max-incremental-backups flag to cap chain length](https://github.com/migtools/kubevirt-datamover-controller/pull/59) — migtools/kubevirt-datamover-controller
- [#14 [oadp-1.6] feat: propagate backup-pvc-size annotation from VM to DataUpload](https://github.com/migtools/kubevirt-datamover-plugin/pull/14) — migtools/kubevirt-datamover-plugin
- [#13 feat: propagate backup-pvc-size annotation from VM to DataUpload](https://github.com/migtools/kubevirt-datamover-plugin/pull/13) — migtools/kubevirt-datamover-plugin
- [#62 [oadp-1.6] fix: detect VMB failure when Done=True and size temp PVC from source disk](https://github.com/migtools/kubevirt-datamover-controller/pull/62) — migtools/kubevirt-datamover-controller
- [#61 fix: detect VMB failure when Done=True and size temp PVC from source disk](https://github.com/migtools/kubevirt-datamover-controller/pull/61) — migtools/kubevirt-datamover-controller
- [#183 [oadp-1.6] Default namespace to openshift-adp instead of velero](https://github.com/migtools/oadp-cli/pull/183) — migtools/oadp-cli
- [#182 Default namespace to openshift-adp instead of velero](https://github.com/migtools/oadp-cli/pull/182) — migtools/oadp-cli
- [#54 Issue 46: Add pvcSizes to per-VM index file](https://github.com/migtools/kubevirt-datamover-controller/pull/54) — migtools/kubevirt-datamover-controller

**Other** (7)
- [#9768 Inherit insecureSkipTLSVerify from BSL config for CLI downloads](https://github.com/velero-io/velero/pull/9768) — velero-io/velero
- [#9750 fix: improve error handling for discarded hooks in WaitExecHookHandler](https://github.com/velero-io/velero/pull/9750) — velero-io/velero
- [#9740 fix: lint permission issue](https://github.com/velero-io/velero/pull/9740) — velero-io/velero
- [#20 Add Markdown output format to release-sources tool](https://github.com/oadp-rebasebot/oadp-rebase/pull/20) — oadp-rebasebot/oadp-rebase
- [#254 [1.14] Bump Golang to 1.25.9 and go.mod to fix CVEs.](https://github.com/velero-io/velero-plugin-for-gcp/pull/254) — velero-io/velero-plugin-for-gcp
- [#9736 CBT bitmap implementation](https://github.com/velero-io/velero/pull/9736) — velero-io/velero
- [#9739 Set permissions to the actions](https://github.com/velero-io/velero/pull/9739) — velero-io/velero
## Issues/PRs Commented On (23)

**migtools** (1)
- [#63 Ambiguous handling: LookupLatestCheckpoint returns (nil, nil) – force full backup not guaranteed](https://github.com/migtools/kubevirt-datamover-controller/issues/63) — migtools/kubevirt-datamover-controller

**Other** (22)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#24000 .buildkit_qemu_emulator: operation not supported](https://github.com/containers/podman/issues/24000) — containers/podman
- [#394 [Feature Request] Wyze Lock Bolt](https://github.com/SecKatie/ha-wyzeapi/issues/394) — SecKatie/ha-wyzeapi
- [#2229 feat: add `list_pull_request_review_threads` tool to expose PRRT_ node IDs for resolving threads](https://github.com/github/github-mcp-server/issues/2229) — github/github-mcp-server
- [#101 Future: UDP proxy](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#5113 Docker for Mac hangs while starting up.  Stuck on "Docker Desktop is Starting"](https://github.com/docker/for-mac/issues/5113) — docker/for-mac
- [#6120 Docker process doesn't free up memory - macOS, Apple Silicon, Virtualization.framework](https://github.com/docker/for-mac/issues/6120) — docker/for-mac
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#17836 `docker build` fails when using BuildKit due to missing API](https://github.com/containers/podman/issues/17836) — containers/podman
- [#28439 podman machine start reports success on macOS Apple Silicon, but VM falls into emergency mode with Ignition/fsck root UUID errors](https://github.com/containers/podman/issues/28439) — containers/podman
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#2722 pre-existing CRD owners found for owned CRD(s) of dependent CSV](https://github.com/operator-framework/operator-lifecycle-manager/issues/2722) — operator-framework/operator-lifecycle-manager
- [#9760 Allow Velero kubernetes objects to be backed up with If-None-Match bucket policies enabled.](https://github.com/velero-io/velero/issues/9760) — velero-io/velero
- [#9702 Make lint on fresh install gives me  permission denied](https://github.com/velero-io/velero/issues/9702) — velero-io/velero
- [#2240 Feature: Add `in_reply_to` support for replying to existing PR review comment threads](https://github.com/github/github-mcp-server/issues/2240) — github/github-mcp-server
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9429 velero doesn't correctly handle an empty ProviderSnapshotID](https://github.com/velero-io/velero/issues/9429) — velero-io/velero
- [#115489 apiserver does not retry generateName on collisions](https://github.com/kubernetes/kubernetes/issues/115489) — kubernetes/kubernetes
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
## Issues Closed (4)

**openshift** (1)
- [#2108 BSL validation should require region when s3Url is set to a non-AWS endpoint](https://github.com/openshift/oadp-operator/issues/2108) — openshift/oadp-operator

**Other** (3)
- [#6206 rbd: getRBDSnapID and ProcessMetadata issues in snapshot metadata path](https://github.com/ceph/ceph-csi/issues/6206) — ceph/ceph-csi
- [#386 SessionStart hook command hardcodes versioned Homebrew node path, breaks on brew upgrade](https://github.com/mksglu/context-mode/issues/386) — mksglu/context-mode
- [#2722 pre-existing CRD owners found for owned CRD(s) of dependent CSV](https://github.com/operator-framework/operator-lifecycle-manager/issues/2722) — operator-framework/operator-lifecycle-manager
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
