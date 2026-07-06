# Activity Log

> **Period:** 2026-06-22 — 2026-07-06
> **Generated:** 2026-07-06 11:28:30 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 6 |
| PRs Opened | 26 |
| PRs Reviewed | 73 |
| Issues/PRs Commented | 15 |
| Issues Closed | 2 |

---

## PRs Merged (6)

**openshift** (3)
- [#81353 oadp-operator-1.5: Update image tag from ubi9-v1.23 to ubi9-v1.25](https://github.com/openshift/release/pull/81353) — openshift/release
- [#412 Exclude KCP SDK version to work around crash diagnostics issue](https://github.com/openshift/openshift-velero-plugin/pull/412) — openshift/openshift-velero-plugin
- [#2255 fix(design): correct kubevirt datamover restore workflow](https://github.com/openshift/oadp-operator/pull/2255) — openshift/oadp-operator

**migtools** (1)
- [#83 Phase 0+1: DataDownload prerequisites and shared helper extraction](https://github.com/migtools/kubevirt-datamover-controller/pull/83) — migtools/kubevirt-datamover-controller

**Other** (2)
- [#503 ⚡ Optimize PR title extraction to avoid subshells in loop](https://github.com/kaovilai/dotfiles/pull/503) — kaovilai/dotfiles
- [#6203 rbd: add debug logging to ProcessMetadata for CBT diagnostics](https://github.com/ceph/ceph-csi/pull/6203) — ceph/ceph-csi
## PRs Opened (26)

**openshift** (3)
- [#81353 oadp-operator-1.5: Update image tag from ubi9-v1.23 to ubi9-v1.25](https://github.com/openshift/release/pull/81353) — openshift/release
- [#412 Exclude KCP SDK version to work around crash diagnostics issue](https://github.com/openshift/openshift-velero-plugin/pull/412) — openshift/openshift-velero-plugin
- [#2255 fix(design): correct kubevirt datamover restore workflow](https://github.com/openshift/oadp-operator/pull/2255) — openshift/oadp-operator

**Other** (23)
- [#517 ⚡ Bolt: optimize manual package installation](https://github.com/kaovilai/dotfiles/pull/517) — kaovilai/dotfiles
- [#516 ⚡ Bolt: [performance improvement] fix compinit startup check](https://github.com/kaovilai/dotfiles/pull/516) — kaovilai/dotfiles
- [#515 ⚡ Bolt: fix compinit cache skip caused by bare glob conditional](https://github.com/kaovilai/dotfiles/pull/515) — kaovilai/dotfiles
- [#514 🔒 Fix insecure TLS validation in ROSA STS login](https://github.com/kaovilai/dotfiles/pull/514) — kaovilai/dotfiles
- [#513 ⚡ Bolt: [performance improvement] fix compinit caching by properly evaluating extended_glob](https://github.com/kaovilai/dotfiles/pull/513) — kaovilai/dotfiles
- [#512 ⚡ Bolt: optimize brew list N+1 query in migrate-laptop](https://github.com/kaovilai/dotfiles/pull/512) — kaovilai/dotfiles
- [#511 ⚡ Bolt: [performance improvement] fix compinit caching to speed up shell startup](https://github.com/kaovilai/dotfiles/pull/511) — kaovilai/dotfiles
- [#510 ⚡ Bolt: [optimize brew list check]](https://github.com/kaovilai/dotfiles/pull/510) — kaovilai/dotfiles
- [#509 ⚡ Bolt: [performance improvement] Optimize file age checks with native Zsh globs](https://github.com/kaovilai/dotfiles/pull/509) — kaovilai/dotfiles
- [#507 ⚡ Bolt: [Optimize N+1 `brew list` in migrate-laptop.zsh]](https://github.com/kaovilai/dotfiles/pull/507) — kaovilai/dotfiles
- [#506 ⚡ Bolt: Optimize brew list performance by caching list into array](https://github.com/kaovilai/dotfiles/pull/506) — kaovilai/dotfiles
- [#505 ⚡ Bolt: Optimize Zsh cache expiration checking with native globbing](https://github.com/kaovilai/dotfiles/pull/505) — kaovilai/dotfiles
- [#503 ⚡ Optimize PR title extraction to avoid subshells in loop](https://github.com/kaovilai/dotfiles/pull/503) — kaovilai/dotfiles
- [#502 🔒 Fix insecure curl -k usage in MinIO scripts](https://github.com/kaovilai/dotfiles/pull/502) — kaovilai/dotfiles
- [#501 ⚡ Optimize brew package checks in migrate-laptop](https://github.com/kaovilai/dotfiles/pull/501) — kaovilai/dotfiles
- [#500 🧹 Extract common logic in socktainer-symlink functions](https://github.com/kaovilai/dotfiles/pull/500) — kaovilai/dotfiles
- [#499 ⚡ perf: optimize `dco` git commit signoff checking with single git log query](https://github.com/kaovilai/dotfiles/pull/499) — kaovilai/dotfiles
- [#498 ⚡ Optimize GitHub PR Diff Fetching Concurrency](https://github.com/kaovilai/dotfiles/pull/498) — kaovilai/dotfiles
- [#497 🔒 Fix Arbitrary Code Execution in registry login](https://github.com/kaovilai/dotfiles/pull/497) — kaovilai/dotfiles
- [#496 🧹 [code health] Extract shared socktainer socket check](https://github.com/kaovilai/dotfiles/pull/496) — kaovilai/dotfiles
- [#495 ⚡ Bolt: Optimize file staleness checks with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/495) — kaovilai/dotfiles
- [#494 ⚡ Bolt: Optimize cache-file-expired with ZSH native globbing](https://github.com/kaovilai/dotfiles/pull/494) — kaovilai/dotfiles
- [#493 ⚡ Bolt: Fix ZSH glob qualifier evaluation to properly cache compinit](https://github.com/kaovilai/dotfiles/pull/493) — kaovilai/dotfiles
## PRs Reviewed (73)

**velero-io** (8)
- [#9960 Ensure Dependabot PRs get changelog-not-required label](https://github.com/velero-io/velero/pull/9960) — velero-io/velero
- [#9958 Bump golang.org/x/net from 0.49.0 to 0.55.0 in /pkg/apis](https://github.com/velero-io/velero/pull/9958) — velero-io/velero
- [#9955 Early frequent polling for CSI snapshots to handle Windows VSS timeout](https://github.com/velero-io/velero/pull/9955) — velero-io/velero
- [#9945 Block uploader snapshot operations](https://github.com/velero-io/velero/pull/9945) — velero-io/velero
- [#9943 Make pkg/apis its own Go module](https://github.com/velero-io/velero/pull/9943) — velero-io/velero
- [#308 Fix prevent amz-checksum encapsulation when checksumAlgorithm=""](https://github.com/velero-io/velero-plugin-for-aws/pull/308) — velero-io/velero-plugin-for-aws
- [#309 Backport to 1.14: Only set PutObject Tagging when tags are configured](https://github.com/velero-io/velero-plugin-for-aws/pull/309) — velero-io/velero-plugin-for-aws
- [#9941 Decide restorePVC volumeMode by data mover type](https://github.com/velero-io/velero/pull/9941) — velero-io/velero

**openshift** (47)
- [#128 Merge https://github.com/openshift/oadp-must-gather:oadp-1.5 (24f9314) into oadp-1.5](https://github.com/openshift/oadp-must-gather/pull/128) — openshift/oadp-must-gather
- [#2277 Merge https://github.com/openshift/oadp-operator:oadp-1.4 (c6f4473) into oadp-1.4](https://github.com/openshift/oadp-operator/pull/2277) — openshift/oadp-operator
- [#151 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.12.2 (82b9141) into oadp-1.5](https://github.com/openshift/velero-plugin-for-aws/pull/151) — openshift/velero-plugin-for-aws
- [#291 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (8cfc49a) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/291) — openshift/hypershift-oadp-plugin
- [#428 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.5 (9b8be06) into oadp-1.5](https://github.com/openshift/openshift-velero-plugin/pull/428) — openshift/openshift-velero-plugin
- [#2278 Merge https://github.com/openshift/oadp-operator:oadp-1.5 (181c14d) into oadp-1.5](https://github.com/openshift/oadp-operator/pull/2278) — openshift/oadp-operator
- [#2279 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (28bfc07) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2279) — openshift/oadp-operator
- [#430 UPSTREAM: <carry>: Fix GetVolumesByPod call signature](https://github.com/openshift/openshift-velero-plugin/pull/430) — openshift/openshift-velero-plugin
- [#65 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (733bf70) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/65) — openshift/velero-plugin-for-legacy-aws
- [#429 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (49477eb) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/429) — openshift/openshift-velero-plugin
- [#152 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.14.1 (96a651c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-aws/pull/152) — openshift/velero-plugin-for-aws
- [#129 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (1ba3932) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/129) — openshift/oadp-must-gather
- [#290 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (8d962a0) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/290) — openshift/hypershift-oadp-plugin
- [#425 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.3 (e0a65b1) into oadp-1.3](https://github.com/openshift/openshift-velero-plugin/pull/425) — openshift/openshift-velero-plugin
- [#123 Add joeavaikath to OWNERS](https://github.com/openshift/oadp-must-gather/pull/123) — openshift/oadp-must-gather
- [#2276 Remove duplicate legacy controller-gen variable and target](https://github.com/openshift/oadp-operator/pull/2276) — openshift/oadp-operator
- [#2273 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (a92f1dd) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2273) — openshift/oadp-operator
- [#426 Bump github.com/sigstore/fulcio from 1.8.5 to 1.8.6](https://github.com/openshift/openshift-velero-plugin/pull/426) — openshift/openshift-velero-plugin
- [#2274 Fix non-constant format string errors for Go 1.24](https://github.com/openshift/oadp-operator/pull/2274) — openshift/oadp-operator
- [#535 UPSTREAM: <carry>: fix context leak in backupper_test.go](https://github.com/openshift/velero/pull/535) — openshift/velero
- [#534 Merge https://github.com/velero-io/velero:v1.12.4 (7d8417b) into oadp-1.3](https://github.com/openshift/velero/pull/534) — openshift/velero
- [#146 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.1 (6902b36) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/146) — openshift/velero-plugin-for-gcp
- [#150 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.1 (6fb0379) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/150) — openshift/velero-plugin-for-microsoft-azure
- [#424 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (6d49e00) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/424) — openshift/openshift-velero-plugin
- [#63 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (dd8b87c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/63) — openshift/velero-plugin-for-legacy-aws
- [#287 Add joeavaikath to OWNERS](https://github.com/openshift/hypershift-oadp-plugin/pull/287) — openshift/hypershift-oadp-plugin
- [#289 Add joeavaikath to OWNERS](https://github.com/openshift/hypershift-oadp-plugin/pull/289) — openshift/hypershift-oadp-plugin
- [#288 Add joeavaikath to OWNERS](https://github.com/openshift/hypershift-oadp-plugin/pull/288) — openshift/hypershift-oadp-plugin
- [#113 Fix HIGH/CRITICAL CVEs in indirect dependencies](https://github.com/openshift/oadp-must-gather/pull/113) — openshift/oadp-must-gather
- [#279 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (b0e1d41) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/279) — openshift/hypershift-oadp-plugin
- [#2251 Merge https://github.com/openshift/oadp-operator:oadp-1.6 (157bce8) into oadp-1.6](https://github.com/openshift/oadp-operator/pull/2251) — openshift/oadp-operator
- [#2254 Update e2e and kubevirt-dm design to use custom volume policy](https://github.com/openshift/oadp-operator/pull/2254) — openshift/oadp-operator
- [#81032 run ipv6 in aws with OADP](https://github.com/openshift/release/pull/81032) — openshift/release
- [#139 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.14.1 (96a651c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-aws/pull/139) — openshift/velero-plugin-for-aws
- [#61 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (402da86) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/61) — openshift/velero-plugin-for-legacy-aws
- [#523 Bump dependencies to fix CVEs](https://github.com/openshift/velero/pull/523) — openshift/velero
- [#54 Fix CVEs in go-jose/v4, x/crypto, x/net, and x/sys](https://github.com/openshift/restic/pull/54) — openshift/restic
- [#522 Upgrade Go module dependencies to address the following CVEs:](https://github.com/openshift/velero/pull/522) — openshift/velero
- [#518 Merge https://github.com/velero-io/velero:v1.18.2-rc.2 (c253c7f) into oadp-1.6](https://github.com/openshift/velero/pull/518) — openshift/velero
- [#53 fix 18 CVE's :/](https://github.com/openshift/restic/pull/53) — openshift/restic
- [#520 Fix golangci-lint version extraction for go install format](https://github.com/openshift/velero/pull/520) — openshift/velero
- [#108 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (45b1dec) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/108) — openshift/oadp-must-gather
- [#138 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.14.1 (96a651c) into oadp-1.6](https://github.com/openshift/velero-plugin-for-aws/pull/138) — openshift/velero-plugin-for-aws
- [#278 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (85a2ff2) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/278) — openshift/hypershift-oadp-plugin
- [#60 Merge https://github.com/openshift/velero-plugin-for-legacy-aws:oadp-1.6 (06af804) into oadp-1.6](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/60) — openshift/velero-plugin-for-legacy-aws
- [#133 Merge https://github.com/velero-io/velero-plugin-for-gcp:v1.14.1 (6902b36) into oadp-1.6](https://github.com/openshift/velero-plugin-for-gcp/pull/133) — openshift/velero-plugin-for-gcp
- [#137 Merge https://github.com/velero-io/velero-plugin-for-microsoft-azure:v1.14.1 (6fb0379) into oadp-1.6](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/137) — openshift/velero-plugin-for-microsoft-azure

**migtools** (14)
- [#357 Merge https://github.com/migtools/oadp-non-admin:oadp-1.4 (3048717) into oadp-1.4](https://github.com/migtools/oadp-non-admin/pull/357) — migtools/oadp-non-admin
- [#30 CVE-2026-24051 and CVE-2026-39883](https://github.com/migtools/kopia/pull/30) — migtools/kopia
- [#34 fix: update Go dependencies to address HIGH CVEs](https://github.com/migtools/kopia/pull/34) — migtools/kopia
- [#355 Merge https://github.com/migtools/oadp-non-admin:oadp-1.5 (aad3132) into oadp-1.5](https://github.com/migtools/oadp-non-admin/pull/355) — migtools/oadp-non-admin
- [#356 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (b9fbb18) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/356) — migtools/oadp-non-admin
- [#26 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (56450ca) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/26) — migtools/kubevirt-datamover-plugin
- [#216 test: assert schedule, backup-location, must-gather, setup commands in root help](https://github.com/migtools/oadp-cli/pull/216) — migtools/oadp-cli
- [#212 Strip nonadmin oadp 1.4](https://github.com/migtools/oadp-cli/pull/212) — migtools/oadp-cli
- [#89 [oadp-1.6] Detect backup type mismatch between controller and virt-controller](https://github.com/migtools/kubevirt-datamover-controller/pull/89) — migtools/kubevirt-datamover-controller
- [#208 Merge https://github.com/migtools/oadp-cli:oadp-1.6 (b907efb) into oadp-1.6](https://github.com/migtools/oadp-cli/pull/208) — migtools/oadp-cli
- [#85 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-1.6 (779bb06) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/85) — migtools/kubevirt-datamover-controller
- [#23 Only create DataUpload if matching custom volume policy is found](https://github.com/migtools/kubevirt-datamover-plugin/pull/23) — migtools/kubevirt-datamover-plugin
- [#353 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (c965753) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/353) — migtools/oadp-non-admin
- [#31 fix(deps): remediate HIGH/CRITICAL CVEs in Go dependencies](https://github.com/migtools/kopia/pull/31) — migtools/kopia

**Other** (4)
- [#258 Add retainBaseSnapshot field to SnapshotMetadataService CRD](https://github.com/kubernetes-csi/external-snapshot-metadata/pull/258) — kubernetes-csi/external-snapshot-metadata
- [#117 [improve] manifests: add explicit imagePullPolicy: IfNotPresent to workload pods](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/117) — kaovilai/k8s-cbt-s3mover-demo
- [#75 Update Velero 1.6 rebase target to v1.18.2-rc.2](https://github.com/oadp-rebasebot/oadp-rebase/pull/75) — oadp-rebasebot/oadp-rebase
- [#69 Enable hypershift-oadp-plugin in rebase-status and auto-rebase for all branches](https://github.com/oadp-rebasebot/oadp-rebase/pull/69) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (15)

**velero-io** (4)
- [#9712 Retrieve chagneId from snapshot](https://github.com/velero-io/velero/issues/9712) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#9858 Add global VolumePolicy](https://github.com/velero-io/velero/issues/9858) — velero-io/velero
- [#9922 Identify e2e (nightly) requirements for CNCF-managed cloud accounts onboarding (AWS, GCP, Azure, vSphere)](https://github.com/velero-io/velero/issues/9922) — velero-io/velero

**migtools** (1)
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller

**Other** (10)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#502 Enhancement: Allow combining `run_if_changed` and `skip_if_only_changed` for more flexible job triggering](https://github.com/kubernetes-sigs/prow/issues/502) — kubernetes-sigs/prow
- [#101 Future: UDP proxy](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#134 `tide` not honoring multiple reviewer branch protection](https://github.com/kubernetes-sigs/prow/issues/134) — kubernetes-sigs/prow
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
- [#70329 runtime: 1.23 hangs when running under qemu-user [bisected]](https://github.com/golang/go/issues/70329) — golang/go
- [#17875 VEP#25 Enhancement: Incremental VirtualMachineBackup delta is always relative to VirtualMachineBackupTracker.status.latestCheckpoint only (no arbitrary base checkpoint)](https://github.com/kubevirt/kubevirt/issues/17875) — kubevirt/kubevirt
- [#2463 Unable to skopeo copy from multi platform oci-archive to registry.](https://github.com/podman-container-tools/skopeo/issues/2463) — podman-container-tools/skopeo
## Issues Closed (2)

**Other** (2)
- [#116 The logic for Prow test name is not correct.](https://github.com/kaovilai/github-bot-command-palette/issues/116) — kaovilai/github-bot-command-palette
- [#114 fix /override "Lint / Lint (ubuntu-latest) (pull_request)" to be /override "Lint (ubuntu-latest)"](https://github.com/kaovilai/github-bot-command-palette/issues/114) — kaovilai/github-bot-command-palette
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
