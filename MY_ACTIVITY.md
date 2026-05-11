# Activity Log

> **Period:** 2026-04-27 — 2026-05-11
> **Generated:** 2026-05-11 10:59:42 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 12 |
| PRs Opened | 9 |
| PRs Reviewed | 47 |
| Issues/PRs Commented | 26 |
| Issues Closed | 14 |

---

## PRs Merged (12)

**openshift** (5)
- [#2184 Increase Fedora VM startup timeout to 20 minutes](https://github.com/openshift/oadp-operator/pull/2184) — openshift/oadp-operator
- [#500 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/500) — openshift/velero
- [#498 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest, migrate config](https://github.com/openshift/velero/pull/498) — openshift/velero
- [#501 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/501) — openshift/velero
- [#2109 OADP-5777: Require region in BSL validation when s3Url is set, fix nil config skipping region auto-detection](https://github.com/openshift/oadp-operator/pull/2109) — openshift/oadp-operator

**Other** (7)
- [#19 fix: stop plaintext fallback when encryption fails](https://github.com/WinShell-Bhanu/Clipsync/pull/19) — WinShell-Bhanu/Clipsync
- [#94 Implement priority class support for Velero components](https://github.com/kaovilai/velero/pull/94) — kaovilai/velero
- [#17 fix: require digit proximity for OTP keyword matching](https://github.com/WinShell-Bhanu/Clipsync/pull/17) — WinShell-Bhanu/Clipsync
- [#15 fix: restrict accessibility service to least-privilege permissions](https://github.com/WinShell-Bhanu/Clipsync/pull/15) — WinShell-Bhanu/Clipsync
- [#16 fix: store encryption key in macOS Keychain instead of UserDefaults](https://github.com/WinShell-Bhanu/Clipsync/pull/16) — WinShell-Bhanu/Clipsync
- [#18 fix: validate FCM push notification URLs against domain allowlist](https://github.com/WinShell-Bhanu/Clipsync/pull/18) — WinShell-Bhanu/Clipsync
- [#14 fix: use HTTPS for IP geolocation and disable cleartext traffic](https://github.com/WinShell-Bhanu/Clipsync/pull/14) — WinShell-Bhanu/Clipsync
## PRs Opened (9)

**openshift** (5)
- [#2198 fix: handle not-found error in nodeagent DaemonSet deletion](https://github.com/openshift/oadp-operator/pull/2198) — openshift/oadp-operator
- [#2196 docs: add podConfig documentation for tolerations, nodeSelector, labels, and env](https://github.com/openshift/oadp-operator/pull/2196) — openshift/oadp-operator
- [#501 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/501) — openshift/velero
- [#500 UPSTREAM: <drop>: Drop coverprofile, update golangci-lint to v2.5.0, fix envtest](https://github.com/openshift/velero/pull/500) — openshift/velero
- [#2184 Increase Fedora VM startup timeout to 20 minutes](https://github.com/openshift/oadp-operator/pull/2184) — openshift/oadp-operator

**Other** (4)
- [#2 feat(libpod): Add Podman /libpod/* API endpoints](https://github.com/kaovilai/socktainer/pull/2) — kaovilai/socktainer
- [#8 feat: implement Docker/Podman socket compatibility via launchd activation](https://github.com/us/mocker/pull/8) — us/mocker
- [#9772 Design: namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/9772) — velero-io/velero
- [#9770 design: Kubernetes name length enforcement for Velero-created objects (#8815)](https://github.com/velero-io/velero/pull/9770) — velero-io/velero
## PRs Reviewed (47)

**openshift** (15)
- [#2192 [oadp-1.6] OADP-6734: Add podLabels and podAnnotations for maintenance and data mover pods](https://github.com/openshift/oadp-operator/pull/2192) — openshift/oadp-operator
- [#2197 [oadp-1.6] fix: add /tmp emptyDir volume to KDM controller deployment](https://github.com/openshift/oadp-operator/pull/2197) — openshift/oadp-operator
- [#2191 fix: add /tmp emptyDir volume to KDM controller deployment](https://github.com/openshift/oadp-operator/pull/2191) — openshift/oadp-operator
- [#2190 OADP-6734: Add podLabels and podAnnotations for maintenance and data mover pods](https://github.com/openshift/oadp-operator/pull/2190) — openshift/oadp-operator
- [#2189 [oadp-1.6] feat: add KubevirtDatamoverConfig to DPA for max incremental backups](https://github.com/openshift/oadp-operator/pull/2189) — openshift/oadp-operator
- [#2179 feat: add KubevirtDatamoverConfig to DPA for max incremental backups](https://github.com/openshift/oadp-operator/pull/2179) — openshift/oadp-operator
- [#2188 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (3fa3730) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2188) — openshift/oadp-operator
- [#250 Update velero dependency to latest oadp-1.6 branch (v1.18.1-rc.1)](https://github.com/openshift/hypershift-oadp-plugin/pull/250) — openshift/hypershift-oadp-plugin
- [#2187 OADP-7882: add dpa config to disable early csi polling interval](https://github.com/openshift/oadp-operator/pull/2187) — openshift/oadp-operator
- [#499 Optimize VSC handle readiness polling for VSS backups (cp from upstream 1.18)](https://github.com/openshift/velero/pull/499) — openshift/velero
- [#2182 [oadp-1.6] OADP-5777: Require region in BSL validation when s3Url is set, fix nil config skipping region auto-detection](https://github.com/openshift/oadp-operator/pull/2182) — openshift/oadp-operator
- [#2181 OADP-7882: add dpa config to disable early csi polling interval](https://github.com/openshift/oadp-operator/pull/2181) — openshift/oadp-operator
- [#91 OADP-1.6 must-gather updates](https://github.com/openshift/oadp-must-gather/pull/91) — openshift/oadp-must-gather
- [#2180 [oadp-1.6] OADP-7869: Fix stale resourceAnnotations/resourceLabels after DPA patch](https://github.com/openshift/oadp-operator/pull/2180) — openshift/oadp-operator
- [#90 OADP-7872: Add VM file restore CRDs to must-gather](https://github.com/openshift/oadp-must-gather/pull/90) — openshift/oadp-must-gather

**migtools** (15)
- [#67 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-1.6 (e770f03) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/67) — migtools/kubevirt-datamover-controller
- [#68 [oadp-1.6] fix: replace custom AWS credential parser with SDK's built-in parser](https://github.com/migtools/kubevirt-datamover-controller/pull/68) — migtools/kubevirt-datamover-controller
- [#188 Hardcode VERSION to oadp-dev for standardised version reporting](https://github.com/migtools/oadp-cli/pull/188) — migtools/oadp-cli
- [#189 Hardcode VERSION to oadp-1.6 for standardised version reporting](https://github.com/migtools/oadp-cli/pull/189) — migtools/oadp-cli
- [#66 fix: replace custom AWS credential parser with SDK's built-in parser](https://github.com/migtools/kubevirt-datamover-controller/pull/66) — migtools/kubevirt-datamover-controller
- [#336 fix: pass logger to UpdateBackupStorageLocation](https://github.com/migtools/oadp-non-admin/pull/336) — migtools/oadp-non-admin
- [#65 [oadp-1.6] feat: add --max-incremental-backups flag to cap chain length](https://github.com/migtools/kubevirt-datamover-controller/pull/65) — migtools/kubevirt-datamover-controller
- [#187 Cherry-pick: Fix CLI version in Konflux builds](https://github.com/migtools/oadp-cli/pull/187) — migtools/oadp-cli
- [#59 feat: add --max-incremental-backups flag to cap chain length](https://github.com/migtools/kubevirt-datamover-controller/pull/59) — migtools/kubevirt-datamover-controller
- [#14 [oadp-1.6] feat: propagate backup-pvc-size annotation from VM to DataUpload](https://github.com/migtools/kubevirt-datamover-plugin/pull/14) — migtools/kubevirt-datamover-plugin
- [#13 feat: propagate backup-pvc-size annotation from VM to DataUpload](https://github.com/migtools/kubevirt-datamover-plugin/pull/13) — migtools/kubevirt-datamover-plugin
- [#62 [oadp-1.6] fix: detect VMB failure when Done=True and size temp PVC from source disk](https://github.com/migtools/kubevirt-datamover-controller/pull/62) — migtools/kubevirt-datamover-controller
- [#61 fix: detect VMB failure when Done=True and size temp PVC from source disk](https://github.com/migtools/kubevirt-datamover-controller/pull/61) — migtools/kubevirt-datamover-controller
- [#183 [oadp-1.6] Default namespace to openshift-adp instead of velero](https://github.com/migtools/oadp-cli/pull/183) — migtools/oadp-cli
- [#182 Default namespace to openshift-adp instead of velero](https://github.com/migtools/oadp-cli/pull/182) — migtools/oadp-cli

**Other** (17)
- [#9781 [1.18] Bump Velero dependencies to latest version](https://github.com/velero-io/velero/pull/9781) — velero-io/velero
- [#88 Update errors](https://github.com/velero-io/velero-plugin-example/pull/88) — velero-io/velero-plugin-example
- [#293 Bump aws-sdk-go-v2 for AWS European Sovereign Cloud support](https://github.com/velero-io/velero-plugin-for-aws/pull/293) — velero-io/velero-plugin-for-aws
- [#9776 Fix prow-action workflow permissions for issue commands](https://github.com/velero-io/velero/pull/9776) — velero-io/velero
- [#86 update dependencies](https://github.com/velero-io/velero-plugin-example/pull/86) — velero-io/velero-plugin-example
- [#9778 Bump Velero dependencies to latest version.](https://github.com/velero-io/velero/pull/9778) — velero-io/velero
- [#9779 Update CODE OF CONDUCT for CNCF compliance](https://github.com/velero-io/velero/pull/9779) — velero-io/velero
- [#87 allow docker to cache dependencies](https://github.com/velero-io/velero-plugin-example/pull/87) — velero-io/velero-plugin-example
- [#84 fix badge](https://github.com/velero-io/velero-plugin-example/pull/84) — velero-io/velero-plugin-example
- [#21 Fix macOS compatibility issues for rebase workflow](https://github.com/oadp-rebasebot/oadp-rebase/pull/21) — oadp-rebasebot/oadp-rebase
- [#9773 docs(aws-plugin): update version](https://github.com/velero-io/velero/pull/9773) — velero-io/velero
- [#9775 [main] Some updates for actions on main branch.](https://github.com/velero-io/velero/pull/9775) — velero-io/velero
- [#82 chore: update golang](https://github.com/velero-io/velero-plugin-example/pull/82) — velero-io/velero-plugin-example
- [#80 update base debian image](https://github.com/velero-io/velero-plugin-example/pull/80) — velero-io/velero-plugin-example
- [#81 update busybox](https://github.com/velero-io/velero-plugin-example/pull/81) — velero-io/velero-plugin-example
- [#20 Add Markdown output format to release-sources tool](https://github.com/oadp-rebasebot/oadp-rebase/pull/20) — oadp-rebasebot/oadp-rebase
- [#9768 Inherit insecureSkipTLSVerify from BSL config for CLI downloads](https://github.com/velero-io/velero/pull/9768) — velero-io/velero
## Issues/PRs Commented On (26)

**openshift** (2)
- [#2005 Use must-gather from new repo](https://github.com/openshift/oadp-operator/issues/2005) — openshift/oadp-operator
- [#2057 kubevirt-dm: Velero Upstream Changes (Policy Actions)](https://github.com/openshift/oadp-operator/issues/2057) — openshift/oadp-operator

**migtools** (1)
- [#63 Ambiguous handling: LookupLatestCheckpoint returns (nil, nil) – force full backup not guaranteed](https://github.com/migtools/kubevirt-datamover-controller/issues/63) — migtools/kubevirt-datamover-controller

**Other** (23)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#27211 Ambiguous Podman Multi-Arch Build Output: Silent Single-Arch Image Creation](https://github.com/containers/podman/issues/27211) — containers/podman
- [#145 OWNERS.md Missing](https://github.com/konveyor/enhancements/issues/145) — konveyor/enhancements
- [#9744 Bug: Restore stuck in Finalizing phase indefinitely due to unbounded hook-tracker wait](https://github.com/velero-io/velero/issues/9744) — velero-io/velero
- [#2229 feat: add `list_pull_request_review_threads` tool to expose PRRT_ node IDs for resolving threads](https://github.com/github/github-mcp-server/issues/2229) — github/github-mcp-server
- [#394 [Feature Request] Wyze Lock Bolt](https://github.com/SecKatie/ha-wyzeapi/issues/394) — SecKatie/ha-wyzeapi
- [#9760 Allow Velero kubernetes objects to be backed up with If-None-Match bucket policies enabled.](https://github.com/velero-io/velero/issues/9760) — velero-io/velero
- [#1495 Feature: `container manifest` subcommand for multi-arch OCI image index creation](https://github.com/apple/container/issues/1495) — apple/container
- [#9709 CBT interfaces](https://github.com/velero-io/velero/issues/9709) — velero-io/velero
- [#11 feat: manifest list assembly workarounds (Podman/skopeo) — tracking issue for #9 pending apple/container#1495](https://github.com/us/mocker/issues/11) — us/mocker
- [#7 Feature request: Docker/Podman-compatible socket via launchd socket activation (mocker system service)](https://github.com/us/mocker/issues/7) — us/mocker
- [#6206 rbd: getRBDSnapID and ProcessMetadata issues in snapshot metadata path](https://github.com/ceph/ceph-csi/issues/6206) — ceph/ceph-csi
- [#24000 .buildkit_qemu_emulator: operation not supported](https://github.com/containers/podman/issues/24000) — containers/podman
- [#101 Future: UDP proxy](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#5113 Docker for Mac hangs while starting up.  Stuck on "Docker Desktop is Starting"](https://github.com/docker/for-mac/issues/5113) — docker/for-mac
- [#6120 Docker process doesn't free up memory - macOS, Apple Silicon, Virtualization.framework](https://github.com/docker/for-mac/issues/6120) — docker/for-mac
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#17836 `docker build` fails when using BuildKit due to missing API](https://github.com/containers/podman/issues/17836) — containers/podman
- [#28439 podman machine start reports success on macOS Apple Silicon, but VM falls into emergency mode with Ignition/fsck root UUID errors](https://github.com/containers/podman/issues/28439) — containers/podman
- [#8815 Ensure object creation does not exceed Kubernetes maximum name length](https://github.com/velero-io/velero/issues/8815) — velero-io/velero
- [#9714 Verify ChangeId retrieve for Ceph](https://github.com/velero-io/velero/issues/9714) — velero-io/velero
- [#2722 pre-existing CRD owners found for owned CRD(s) of dependent CSV](https://github.com/operator-framework/operator-lifecycle-manager/issues/2722) — operator-framework/operator-lifecycle-manager
- [#9702 Make lint on fresh install gives me  permission denied](https://github.com/velero-io/velero/issues/9702) — velero-io/velero
## Issues Closed (14)

**openshift** (2)
- [#2183 e2e Kubevirt disk timeout issues](https://github.com/openshift/oadp-operator/issues/2183) — openshift/oadp-operator
- [#2108 BSL validation should require region when s3Url is set to a non-AWS endpoint](https://github.com/openshift/oadp-operator/issues/2108) — openshift/oadp-operator

**Other** (12)
- [#12 OTP keyword matching is overly broad, forwarding non-OTP messages](https://github.com/WinShell-Bhanu/Clipsync/issues/12) — WinShell-Bhanu/Clipsync
- [#8 Accessibility Service config requests broader permissions than code uses](https://github.com/WinShell-Bhanu/Clipsync/issues/8) — WinShell-Bhanu/Clipsync
- [#11 macOS encryption key stored in UserDefaults instead of Keychain](https://github.com/WinShell-Bhanu/Clipsync/issues/11) — WinShell-Bhanu/Clipsync
- [#13 FCM push messages accept arbitrary URLs for updates and announcements](https://github.com/WinShell-Bhanu/Clipsync/issues/13) — WinShell-Bhanu/Clipsync
- [#7 Plaintext fallback when encryption fails silently exposes clipboard data](https://github.com/WinShell-Bhanu/Clipsync/issues/7) — WinShell-Bhanu/Clipsync
- [#11 feat: manifest list assembly workarounds (Podman/skopeo) — tracking issue for #9 pending apple/container#1495](https://github.com/us/mocker/issues/11) — us/mocker
- [#9 Cleartext HTTP used for IP geolocation with usesCleartextTraffic enabled app-wide](https://github.com/WinShell-Bhanu/Clipsync/issues/9) — WinShell-Bhanu/Clipsync
- [#9 feat: `mocker manifest` command for multi-arch OCI image index assembly](https://github.com/us/mocker/issues/9) — us/mocker
- [#7 Feature request: Docker/Podman-compatible socket via launchd socket activation (mocker system service)](https://github.com/us/mocker/issues/7) — us/mocker
- [#6206 rbd: getRBDSnapID and ProcessMetadata issues in snapshot metadata path](https://github.com/ceph/ceph-csi/issues/6206) — ceph/ceph-csi
- [#386 SessionStart hook command hardcodes versioned Homebrew node path, breaks on brew upgrade](https://github.com/mksglu/context-mode/issues/386) — mksglu/context-mode
- [#2722 pre-existing CRD owners found for owned CRD(s) of dependent CSV](https://github.com/operator-framework/operator-lifecycle-manager/issues/2722) — operator-framework/operator-lifecycle-manager
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
