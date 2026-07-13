# Activity Log

> **Period:** 2026-06-29 — 2026-07-13
> **Generated:** 2026-07-13 10:58:49 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 5 |
| PRs Opened | 17 |
| PRs Reviewed | 83 |
| Issues/PRs Commented | 22 |
| Issues Closed | 8 |

---

## PRs Merged (5)

**openshift** (4)
- [#81523 oadp-cli: Add oadp-1.4 branch to tide queries](https://github.com/openshift/release/pull/81523) — openshift/release
- [#538 UPSTREAM: <carry>: Update kopia to migtools/kopia 1.3 branch](https://github.com/openshift/velero/pull/538) — openshift/velero
- [#81353 oadp-operator-1.5: Update image tag from ubi9-v1.23 to ubi9-v1.25](https://github.com/openshift/release/pull/81353) — openshift/release
- [#412 Exclude KCP SDK version to work around crash diagnostics issue](https://github.com/openshift/openshift-velero-plugin/pull/412) — openshift/openshift-velero-plugin

**migtools** (1)
- [#83 Phase 0+1: DataDownload prerequisites and shared helper extraction](https://github.com/migtools/kubevirt-datamover-controller/pull/83) — migtools/kubevirt-datamover-controller
## PRs Opened (17)

**openshift** (6)
- [#2308 Export pod inspect functions for external consumption](https://github.com/openshift/oc/pull/2308) — openshift/oc
- [#81523 oadp-cli: Add oadp-1.4 branch to tide queries](https://github.com/openshift/release/pull/81523) — openshift/release
- [#538 UPSTREAM: <carry>: Update kopia to migtools/kopia 1.3 branch](https://github.com/openshift/velero/pull/538) — openshift/velero
- [#81508 WIP rehearse change: update e2e test command to include DNM flag](https://github.com/openshift/release/pull/81508) — openshift/release
- [#81353 oadp-operator-1.5: Update image tag from ubi9-v1.23 to ubi9-v1.25](https://github.com/openshift/release/pull/81353) — openshift/release
- [#412 Exclude KCP SDK version to work around crash diagnostics issue](https://github.com/openshift/openshift-velero-plugin/pull/412) — openshift/openshift-velero-plugin

**Other** (11)
- [#519 ⚡ Bolt: Optimize cache file age checks using native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/519) — kaovilai/dotfiles
- [#285 Add exclude directive for phantom kcp/sdk version (#283)](https://github.com/vmware-tanzu/crash-diagnostics/pull/285) — vmware-tanzu/crash-diagnostics
- [#518 ⚡ Bolt: [performance improvement] optimize file age check in .zshrc](https://github.com/kaovilai/dotfiles/pull/518) — kaovilai/dotfiles
- [#517 ⚡ Bolt: optimize manual package installation](https://github.com/kaovilai/dotfiles/pull/517) — kaovilai/dotfiles
- [#516 ⚡ Bolt: [performance improvement] fix compinit startup check](https://github.com/kaovilai/dotfiles/pull/516) — kaovilai/dotfiles
- [#515 ⚡ Bolt: fix compinit cache skip caused by bare glob conditional](https://github.com/kaovilai/dotfiles/pull/515) — kaovilai/dotfiles
- [#514 🔒 Fix insecure TLS validation in ROSA STS login](https://github.com/kaovilai/dotfiles/pull/514) — kaovilai/dotfiles
- [#513 ⚡ Bolt: [performance improvement] fix compinit caching by properly evaluating extended_glob](https://github.com/kaovilai/dotfiles/pull/513) — kaovilai/dotfiles
- [#512 ⚡ Bolt: optimize brew list N+1 query in migrate-laptop](https://github.com/kaovilai/dotfiles/pull/512) — kaovilai/dotfiles
- [#511 ⚡ Bolt: [performance improvement] fix compinit caching to speed up shell startup](https://github.com/kaovilai/dotfiles/pull/511) — kaovilai/dotfiles
- [#510 ⚡ Bolt: [optimize brew list check]](https://github.com/kaovilai/dotfiles/pull/510) — kaovilai/dotfiles
## PRs Reviewed (83)

**velero-io** (14)
- [#9969 Add design doc for dynamic CLI resource autocompletion](https://github.com/velero-io/velero/pull/9969) — velero-io/velero
- [#9992 Bump docker/setup-qemu-action from 3 to 4](https://github.com/velero-io/velero/pull/9992) — velero-io/velero
- [#9984 File system restore happens in parallel](https://github.com/velero-io/velero/pull/9984) — velero-io/velero
- [#9990 fix rate limit issue for e2e-test-kind job](https://github.com/velero-io/velero/pull/9990) — velero-io/velero
- [#9989 fix globalExcludes lookup](https://github.com/velero-io/velero/pull/9989) — velero-io/velero
- [#310 Fix SSE-C signed URLs](https://github.com/velero-io/velero-plugin-for-aws/pull/310) — velero-io/velero-plugin-for-aws
- [#9982 Validate user-provided labels and annotations in maintenance job](https://github.com/velero-io/velero/pull/9982) — velero-io/velero
- [#9966 add cli for create/view restore resource policies](https://github.com/velero-io/velero/pull/9966) — velero-io/velero
- [#9979 Block uploader backup implementation](https://github.com/velero-io/velero/pull/9979) — velero-io/velero
- [#9978 Add image volume type support to volume policies](https://github.com/velero-io/velero/pull/9978) — velero-io/velero
- [#9960 Ensure Dependabot PRs get changelog-not-required label](https://github.com/velero-io/velero/pull/9960) — velero-io/velero
- [#311 Bump golang.org/x/net from 0.48.0 to 0.55.0](https://github.com/velero-io/velero-plugin-for-aws/pull/311) — velero-io/velero-plugin-for-aws
- [#9958 Bump golang.org/x/net from 0.49.0 to 0.55.0 in /pkg/apis](https://github.com/velero-io/velero/pull/9958) — velero-io/velero
- [#9955 Early frequent polling for CSI snapshots to handle Windows VSS timeout](https://github.com/velero-io/velero/pull/9955) — velero-io/velero

**openshift** (55)
- [#139 remove oc cli from konflux build](https://github.com/openshift/oadp-must-gather/pull/139) — openshift/oadp-must-gather
- [#2293 Added oadp-cli-binaries-rhel9 to bundle/image-references for oadp-1.4](https://github.com/openshift/oadp-operator/pull/2293) — openshift/oadp-operator
- [#59 Fix CVE-2025-65637](https://github.com/openshift/restic/pull/59) — openshift/restic
- [#137 remove the oc binary](https://github.com/openshift/oadp-must-gather/pull/137) — openshift/oadp-must-gather
- [#136 oadp-dev: remove oc from oadp-must-gather](https://github.com/openshift/oadp-must-gather/pull/136) — openshift/oadp-must-gather
- [#2291 Backport cli download 1.4](https://github.com/openshift/oadp-operator/pull/2291) — openshift/oadp-operator
- [#2277 Merge https://github.com/openshift/oadp-operator:oadp-1.4 (dbc2eda) into oadp-1.4](https://github.com/openshift/oadp-operator/pull/2277) — openshift/oadp-operator
- [#2292 Backport cli e2e 1.4](https://github.com/openshift/oadp-operator/pull/2292) — openshift/oadp-operator
- [#81580 Added e2e-test-cli-aws job for oadp-1.4](https://github.com/openshift/release/pull/81580) — openshift/release
- [#541 Merge https://github.com/velero-io/velero:v1.16.2 (a608082) into oadp-1.5](https://github.com/openshift/velero/pull/541) — openshift/velero
- [#540 Merge https://github.com/velero-io/velero:v1.14.0 (2fc6300) into oadp-1.4](https://github.com/openshift/velero/pull/540) — openshift/velero
- [#155 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.10.1 (5c92b55) into oadp-1.4](https://github.com/openshift/velero-plugin-for-aws/pull/155) — openshift/velero-plugin-for-aws
- [#133 Merge https://github.com/openshift/oadp-must-gather:oadp-1.3 (99e56dd) into oadp-1.3](https://github.com/openshift/oadp-must-gather/pull/133) — openshift/oadp-must-gather
- [#81619 Add mirroring for v1.26 konveyor golang builder](https://github.com/openshift/release/pull/81619) — openshift/release
- [#425 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.3 (d54e604) into oadp-1.3](https://github.com/openshift/openshift-velero-plugin/pull/425) — openshift/openshift-velero-plugin
- [#81582 update golang builder to match ocpbuilder](https://github.com/openshift/release/pull/81582) — openshift/release
- [#94 Merge https://github.com/vmware-tanzu/velero-plugin-for-csi:v0.6.3 (18cc41e) into oadp-1.3](https://github.com/openshift/velero-plugin-for-csi/pull/94) — openshift/velero-plugin-for-csi
- [#93 Fix podvolume import path for velero v1.12.1+](https://github.com/openshift/velero-plugin-for-csi/pull/93) — openshift/velero-plugin-for-csi
- [#81579 Bump OADP operator build_root to ubi9-v1.25](https://github.com/openshift/release/pull/81579) — openshift/release
- [#2287 chore(deps): bump golang.org/x/net from 0.47.0 to 0.55.0](https://github.com/openshift/oadp-operator/pull/2287) — openshift/oadp-operator
- [#2286 chore(deps): bump github.com/moby/spdystream from 0.5.0 to 0.5.1](https://github.com/openshift/oadp-operator/pull/2286) — openshift/oadp-operator
- [#2285 chore(deps): bump go.opentelemetry.io/otel from 1.38.0 to 1.41.0](https://github.com/openshift/oadp-operator/pull/2285) — openshift/oadp-operator
- [#2284 chore(deps): bump go.opentelemetry.io/otel/sdk from 1.38.0 to 1.43.0](https://github.com/openshift/oadp-operator/pull/2284) — openshift/oadp-operator
- [#2283 chore(deps): bump github.com/go-jose/go-jose/v4 from 4.1.3 to 4.1.4](https://github.com/openshift/oadp-operator/pull/2283) — openshift/oadp-operator
- [#2282 chore(deps): bump google.golang.org/grpc from 1.77.0 to 1.79.3](https://github.com/openshift/oadp-operator/pull/2282) — openshift/oadp-operator
- [#2281 Bump CSV metadata to v1.4.11](https://github.com/openshift/oadp-operator/pull/2281) — openshift/oadp-operator
- [#2288 chore(deps): bump github.com/aws/aws-sdk-go-v2/service/s3 from 1.48.0 to 1.97.3](https://github.com/openshift/oadp-operator/pull/2288) — openshift/oadp-operator
- [#431 Update setup-envtest to release-0.22](https://github.com/openshift/openshift-velero-plugin/pull/431) — openshift/openshift-velero-plugin
- [#128 Merge https://github.com/openshift/oadp-must-gather:oadp-1.5 (24f9314) into oadp-1.5](https://github.com/openshift/oadp-must-gather/pull/128) — openshift/oadp-must-gather
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

**migtools** (9)
- [#176 Bump golang.org/x/crypto from 0.41.0 to 0.52.0](https://github.com/migtools/udistribution/pull/176) — migtools/udistribution
- [#90 Bump google.golang.org/grpc from 1.77.0 to 1.79.3 in the go_modules group across 1 directory](https://github.com/migtools/oadp-vm-file-restore/pull/90) — migtools/oadp-vm-file-restore
- [#357 Merge https://github.com/migtools/oadp-non-admin:oadp-1.4 (3048717) into oadp-1.4](https://github.com/migtools/oadp-non-admin/pull/357) — migtools/oadp-non-admin
- [#355 Merge https://github.com/migtools/oadp-non-admin:oadp-1.5 (aad3132) into oadp-1.5](https://github.com/migtools/oadp-non-admin/pull/355) — migtools/oadp-non-admin
- [#34 fix: update Go dependencies to address HIGH CVEs](https://github.com/migtools/kopia/pull/34) — migtools/kopia
- [#356 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (b9fbb18) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/356) — migtools/oadp-non-admin
- [#26 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-1.6 (56450ca) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-plugin/pull/26) — migtools/kubevirt-datamover-plugin
- [#216 test: assert schedule, backup-location, must-gather, setup commands in root help](https://github.com/migtools/oadp-cli/pull/216) — migtools/oadp-cli
- [#212 Strip nonadmin oadp 1.4](https://github.com/migtools/oadp-cli/pull/212) — migtools/oadp-cli

**Other** (5)
- [#135 Modularize remediate.sh into discrete functions](https://github.com/oadp-rebasebot/oadp-rebase/pull/135) — oadp-rebasebot/oadp-rebase
- [#45 Update README.md to document current image variants and workflows](https://github.com/konveyor/builder/pull/45) — konveyor/builder
- [#120 Handle missing Quay images gracefully in CVE scan](https://github.com/oadp-rebasebot/oadp-rebase/pull/120) — oadp-rebasebot/oadp-rebase
- [#117 Add Trivy-based CVE scanning pipeline](https://github.com/oadp-rebasebot/oadp-rebase/pull/117) — oadp-rebasebot/oadp-rebase
- [#117 [improve] manifests: add explicit imagePullPolicy: IfNotPresent to workload pods](https://github.com/kaovilai/k8s-cbt-s3mover-demo/pull/117) — kaovilai/k8s-cbt-s3mover-demo
## Issues/PRs Commented On (22)

**velero-io** (4)
- [#8277 CSI Backup fails upon provisioner and csi driver mismatch (everest-csi)](https://github.com/velero-io/velero/issues/8277) — velero-io/velero
- [#7564 Add support to output restore describe in multiple format like backups](https://github.com/velero-io/velero/issues/7564) — velero-io/velero
- [#9600 Deprecation: Remove `BackupStorageLocation.Spec.ObjectStorage.CACert` inline field in favor of `CACertRef` secret reference](https://github.com/velero-io/velero/issues/9600) — velero-io/velero
- [#9712 Retrieve chagneId from snapshot](https://github.com/velero-io/velero/issues/9712) — velero-io/velero

**openshift** (3)
- [#281 Move to FIPS enabled builder](https://github.com/openshift/velero/issues/281) — openshift/velero
- [#254 oadp-1.2 missing OWNERS file for tide](https://github.com/openshift/velero/issues/254) — openshift/velero
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero

**migtools** (1)
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller

**Other** (14)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#1419 `kubectl explain -o md`](https://github.com/kubernetes/kubectl/issues/1419) — kubernetes/kubectl
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#245 Package errors looking for new maintainers](https://github.com/pkg/errors/issues/245) — pkg/errors
- [#2387 Downgrade min go adopt https://github.com/googleapis/google-api-go-client/pull/3640](https://github.com/sigstore/fulcio/issues/2387) — sigstore/fulcio
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
- [#502 Enhancement: Allow combining `run_if_changed` and `skip_if_only_changed` for more flexible job triggering](https://github.com/kubernetes-sigs/prow/issues/502) — kubernetes-sigs/prow
- [#101 Future: UDP proxy](https://github.com/pyamsoft/tetherfusenet/issues/101) — pyamsoft/tetherfusenet
- [#7520 [Workaround in description] Mac is detecting Docker as a malware and keeping it from starting](https://github.com/docker/for-mac/issues/7520) — docker/for-mac
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#134 `tide` not honoring multiple reviewer branch protection](https://github.com/kubernetes-sigs/prow/issues/134) — kubernetes-sigs/prow
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
- [#70329 runtime: 1.23 hangs when running under qemu-user [bisected]](https://github.com/golang/go/issues/70329) — golang/go
## Issues Closed (8)

**velero-io** (1)
- [#9959 Ensure Dependabot PRs get changelog-not-required label](https://github.com/velero-io/velero/issues/9959) — velero-io/velero

**openshift** (2)
- [#281 Move to FIPS enabled builder](https://github.com/openshift/velero/issues/281) — openshift/velero
- [#254 oadp-1.2 missing OWNERS file for tide](https://github.com/openshift/velero/issues/254) — openshift/velero

**Other** (5)
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#44 Update README.md to reflect current repo](https://github.com/konveyor/builder/issues/44) — konveyor/builder
- [#2387 Downgrade min go adopt https://github.com/googleapis/google-api-go-client/pull/3640](https://github.com/sigstore/fulcio/issues/2387) — sigstore/fulcio
- [#116 The logic for Prow test name is not correct.](https://github.com/kaovilai/github-bot-command-palette/issues/116) — kaovilai/github-bot-command-palette
- [#114 fix /override "Lint / Lint (ubuntu-latest) (pull_request)" to be /override "Lint (ubuntu-latest)"](https://github.com/kaovilai/github-bot-command-palette/issues/114) — kaovilai/github-bot-command-palette
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
