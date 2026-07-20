# Activity Log

> **Period:** 2026-07-06 — 2026-07-20
> **Generated:** 2026-07-20 10:57:37 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 30 |
| PRs Opened | 54 |
| PRs Reviewed | 92 |
| Issues/PRs Commented | 33 |
| Issues Closed | 14 |

---

## PRs Merged (30)

**velero-io** (4)
- [#10019 Remove Auto Request Review workflow in favor of CODEOWNERS](https://github.com/velero-io/velero/pull/10019) — velero-io/velero
- [#9886 Scrub Restic references from main Velero docs](https://github.com/velero-io/velero/pull/9886) — velero-io/velero
- [#313 [release-1.14] Fix prevent amz-checksum encapsulation when checksumAlgorithm=""](https://github.com/velero-io/velero-plugin-for-aws/pull/313) — velero-io/velero-plugin-for-aws
- [#9960 Ensure Dependabot PRs get changelog-not-required label](https://github.com/velero-io/velero/pull/9960) — velero-io/velero

**openshift** (6)
- [#63 Group all Go dependency updates in Dependabot](https://github.com/openshift/restic/pull/63) — openshift/restic
- [#81959 Require GH Actions checks, remove redundant Prow tests for velero + plugin forks](https://github.com/openshift/release/pull/81959) — openshift/release
- [#81949 oadp: Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/81949) — openshift/release
- [#81885 remove go1.25 pin from unit tests](https://github.com/openshift/release/pull/81885) — openshift/release
- [#81523 oadp-cli: Add oadp-1.4 branch to tide queries](https://github.com/openshift/release/pull/81523) — openshift/release
- [#538 UPSTREAM: <carry>: Update kopia to migtools/kopia 1.3 branch](https://github.com/openshift/velero/pull/538) — openshift/velero

**migtools** (2)
- [#28 Group all Go dependency updates in Dependabot](https://github.com/migtools/filebrowser/pull/28) — migtools/filebrowser
- [#177 Group all Go dependency updates in Dependabot](https://github.com/migtools/udistribution/pull/177) — migtools/udistribution

**Other** (18)
- [#165 fix: add curl retry flags to download calls](https://github.com/helm/kind-action/pull/165) — helm/kind-action
- [#320 Copilot/refactor default models usage](https://github.com/caozhiyuan/copilot-api/pull/320) — caozhiyuan/copilot-api
- [#319 fix: override Vertex/Bedrock providers in Claude Code env command](https://github.com/caozhiyuan/copilot-api/pull/319) — caozhiyuan/copilot-api
- [#158 Enhance README with OADP Rebase Pages information](https://github.com/oadp-rebasebot/oadp-rebase/pull/158) — oadp-rebasebot/oadp-rebase
- [#495 ⚡ Bolt: Optimize file staleness checks with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/495) — kaovilai/dotfiles
- [#502 🔒 Fix insecure curl -k usage in MinIO scripts](https://github.com/kaovilai/dotfiles/pull/502) — kaovilai/dotfiles
- [#500 🧹 Extract common logic in socktainer-symlink functions](https://github.com/kaovilai/dotfiles/pull/500) — kaovilai/dotfiles
- [#487 ⚡ perf: optimize process formatting in kill-stuck-qemu](https://github.com/kaovilai/dotfiles/pull/487) — kaovilai/dotfiles
- [#498 ⚡ Optimize GitHub PR Diff Fetching Concurrency](https://github.com/kaovilai/dotfiles/pull/498) — kaovilai/dotfiles
- [#499 ⚡ perf: optimize `dco` git commit signoff checking with single git log query](https://github.com/kaovilai/dotfiles/pull/499) — kaovilai/dotfiles
- [#506 ⚡ Bolt: Optimize brew list performance by caching list into array](https://github.com/kaovilai/dotfiles/pull/506) — kaovilai/dotfiles
- [#516 ⚡ Bolt: [performance improvement] fix compinit startup check](https://github.com/kaovilai/dotfiles/pull/516) — kaovilai/dotfiles
- [#497 🔒 Fix Arbitrary Code Execution in registry login](https://github.com/kaovilai/dotfiles/pull/497) — kaovilai/dotfiles
- [#488 🔒 Fix eval() vulnerability in verify-migration](https://github.com/kaovilai/dotfiles/pull/488) — kaovilai/dotfiles
- [#514 🔒 Fix insecure TLS validation in ROSA STS login](https://github.com/kaovilai/dotfiles/pull/514) — kaovilai/dotfiles
- [#4 Cherry-pick #317 fix: disable Vertex/Bedrock in Claude Code env onto dev](https://github.com/kaovilai/copilot-api/pull/4) — kaovilai/copilot-api
- [#2 Default Claude Code setup to latest opus/sonnet/haiku per size tier](https://github.com/kaovilai/copilot-api/pull/2) — kaovilai/copilot-api
- [#45 Update README.md to document current image variants and workflows](https://github.com/konveyor/builder/pull/45) — konveyor/builder
## PRs Opened (54)

**velero-io** (16)
- [#10034 chore: pin helm/kind-action to commit with curl retry fix](https://github.com/velero-io/velero/pull/10034) — velero-io/velero
- [#10030 Fix flaky TestKopiaObjectWriterEx_ConcurrentAsyncErrors](https://github.com/velero-io/velero/pull/10030) — velero-io/velero
- [#10028 Bump actions/labeler from v5 to v6](https://github.com/velero-io/velero/pull/10028) — velero-io/velero
- [#10027 Add set-based label selector test and docs coverage for restore](https://github.com/velero-io/velero/pull/10027) — velero-io/velero
- [#10025 Add make test-e2e-kind: self-contained e2e run in a single container](https://github.com/velero-io/velero/pull/10025) — velero-io/velero
- [#10024 Derive dev-tool CLI versions from go.mod (ginkgo, protoc-gen-go, goimports)](https://github.com/velero-io/velero/pull/10024) — velero-io/velero
- [#10021 Replace engineerd/setup-kind action with kind CLI + curl retries](https://github.com/velero-io/velero/pull/10021) — velero-io/velero
- [#321 [release-1.13] Fix volume snapshotter usage of AAD URI (backport of #256)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/321) — velero-io/velero-plugin-for-microsoft-azure
- [#320 [release-1.14] Fix volume snapshotter usage of AAD URI (backport of #256)](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/320) — velero-io/velero-plugin-for-microsoft-azure
- [#313 [release-1.14] Fix prevent amz-checksum encapsulation when checksumAlgorithm=""](https://github.com/velero-io/velero-plugin-for-aws/pull/313) — velero-io/velero-plugin-for-aws
- [#319 Add CODEOWNERS for automatic review requests](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/319) — velero-io/velero-plugin-for-microsoft-azure
- [#261 Add CODEOWNERS for automatic review requests](https://github.com/velero-io/velero-plugin-for-gcp/pull/261) — velero-io/velero-plugin-for-gcp
- [#312 Add CODEOWNERS for automatic review requests](https://github.com/velero-io/velero-plugin-for-aws/pull/312) — velero-io/velero-plugin-for-aws
- [#10019 Remove Auto Request Review workflow in favor of CODEOWNERS](https://github.com/velero-io/velero/pull/10019) — velero-io/velero
- [#318 Fix Auto Request Review workflow: bump action version and pass token](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/318) — velero-io/velero-plugin-for-microsoft-azure
- [#10010 Design for CRD schema validation at server startup](https://github.com/velero-io/velero/pull/10010) — velero-io/velero

**openshift** (11)
- [#2313 Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2313) — openshift/oadp-operator
- [#444 OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/444) — openshift/openshift-velero-plugin
- [#63 Group all Go dependency updates in Dependabot](https://github.com/openshift/restic/pull/63) — openshift/restic
- [#81959 Require GH Actions checks, remove redundant Prow tests for velero + plugin forks](https://github.com/openshift/release/pull/81959) — openshift/release
- [#442 Support Azure Workload Identity (WIF) in image stream registry env vars](https://github.com/openshift/openshift-velero-plugin/pull/442) — openshift/openshift-velero-plugin
- [#81949 oadp: Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/81949) — openshift/release
- [#81885 remove go1.25 pin from unit tests](https://github.com/openshift/release/pull/81885) — openshift/release
- [#2308 Export pod inspect functions for external consumption](https://github.com/openshift/oc/pull/2308) — openshift/oc
- [#81523 oadp-cli: Add oadp-1.4 branch to tide queries](https://github.com/openshift/release/pull/81523) — openshift/release
- [#538 UPSTREAM: <carry>: Update kopia to migtools/kopia 1.3 branch](https://github.com/openshift/velero/pull/538) — openshift/velero
- [#81508 WIP rehearse change: update e2e test command to include DNM flag](https://github.com/openshift/release/pull/81508) — openshift/release

**migtools** (7)
- [#124 feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/124) — migtools/kubevirt-datamover-controller
- [#119 ci: upgrade workflow actions off deprecated Node 20](https://github.com/migtools/kubevirt-datamover-controller/pull/119) — migtools/kubevirt-datamover-controller
- [#115 feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/115) — migtools/kubevirt-datamover-controller
- [#177 Group all Go dependency updates in Dependabot](https://github.com/migtools/udistribution/pull/177) — migtools/udistribution
- [#28 Group all Go dependency updates in Dependabot](https://github.com/migtools/filebrowser/pull/28) — migtools/filebrowser
- [#110 Fix evaluateVMBackupStatus to read VMBackup failure detail from Reason, not Message](https://github.com/migtools/kubevirt-datamover-controller/pull/110) — migtools/kubevirt-datamover-controller
- [#109 Fix evaluateVMBackupStatus treating real VMBackup failures as success](https://github.com/migtools/kubevirt-datamover-controller/pull/109) — migtools/kubevirt-datamover-controller

**Other** (20)
- [#538 ⚡ Bolt: Remove redundant compinit to improve shell startup time](https://github.com/kaovilai/dotfiles/pull/538) — kaovilai/dotfiles
- [#536 ⚡ Bolt: Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/536) — kaovilai/dotfiles
- [#532 ⚡ Bolt: [performance improvement] Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/532) — kaovilai/dotfiles
- [#158 Enhance README with OADP Rebase Pages information](https://github.com/oadp-rebasebot/oadp-rebase/pull/158) — oadp-rebasebot/oadp-rebase
- [#165 fix: add curl retry flags to download calls](https://github.com/helm/kind-action/pull/165) — helm/kind-action
- [#526 ⚡ Bolt: Optimize cache expiration checks by removing external stat calls](https://github.com/kaovilai/dotfiles/pull/526) — kaovilai/dotfiles
- [#46 Centralize build scheduling into a single version-aware dispatcher](https://github.com/konveyor/builder/pull/46) — konveyor/builder
- [#4 Cherry-pick #317 fix: disable Vertex/Bedrock in Claude Code env onto dev](https://github.com/kaovilai/copilot-api/pull/4) — kaovilai/copilot-api
- [#320 Copilot/refactor default models usage](https://github.com/caozhiyuan/copilot-api/pull/320) — caozhiyuan/copilot-api
- [#2 Default Claude Code setup to latest opus/sonnet/haiku per size tier](https://github.com/kaovilai/copilot-api/pull/2) — kaovilai/copilot-api
- [#319 fix: override Vertex/Bedrock providers in Claude Code env command](https://github.com/caozhiyuan/copilot-api/pull/319) — caozhiyuan/copilot-api
- [#1 Override Vertex/Bedrock providers in generated Claude Code env command](https://github.com/kaovilai/copilot-api/pull/1) — kaovilai/copilot-api
- [#1531 fix(cli): pass through update subcommand to claude directly](https://github.com/slopus/happy/pull/1531) — slopus/happy
- [#519 ⚡ Bolt: Optimize cache file age checks using native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/519) — kaovilai/dotfiles
- [#147 Add Thai QR (PromptPay) payment method to Pay Me section](https://github.com/kaovilai/kaovilai.pw/pull/147) — kaovilai/kaovilai.pw
- [#45 Update README.md to document current image variants and workflows](https://github.com/konveyor/builder/pull/45) — konveyor/builder
- [#285 Add exclude directive for phantom kcp/sdk version (#283)](https://github.com/vmware-tanzu/crash-diagnostics/pull/285) — vmware-tanzu/crash-diagnostics
- [#1 Fixing issue 283 in crash diagnostics](https://github.com/kaovilai/tanzu-crash-diagnostics/pull/1) — kaovilai/tanzu-crash-diagnostics
- [#518 ⚡ Bolt: [performance improvement] optimize file age check in .zshrc](https://github.com/kaovilai/dotfiles/pull/518) — kaovilai/dotfiles
- [#517 ⚡ Bolt: optimize manual package installation](https://github.com/kaovilai/dotfiles/pull/517) — kaovilai/dotfiles
## PRs Reviewed (92)

**velero-io** (24)
- [#10007 Issue 9997: cancel ongoing PVB on timeout](https://github.com/velero-io/velero/pull/10007) — velero-io/velero
- [#10033 Prioritize exact namespace match in restore](https://github.com/velero-io/velero/pull/10033) — velero-io/velero
- [#9967 add documentation for backup filters](https://github.com/velero-io/velero/pull/9967) — velero-io/velero
- [#10000 Fix stale backupLastSuccessfulTimestamp metric after schedule deletion](https://github.com/velero-io/velero/pull/10000) — velero-io/velero
- [#10016 add documentation for fine-grained restore filters](https://github.com/velero-io/velero/pull/10016) — velero-io/velero
- [#9974 Disable fips140 enforcement because Kopia doesn't support it.](https://github.com/velero-io/velero/pull/9974) — velero-io/velero
- [#9969 Add design doc for dynamic CLI resource autocompletion](https://github.com/velero-io/velero/pull/9969) — velero-io/velero
- [#9994 Block dev for block uploader backup](https://github.com/velero-io/velero/pull/9994) — velero-io/velero
- [#10011 Fine grained backup filters for 1.18](https://github.com/velero-io/velero/pull/10011) — velero-io/velero
- [#317 Bump golang.org/x/crypto from 0.46.0 to 0.52.0](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/317) — velero-io/velero-plugin-for-microsoft-azure
- [#10002 [CP-1.18]Add maintainers as code owners (#9998)](https://github.com/velero-io/velero/pull/10002) — velero-io/velero
- [#9998 Add maintainers as code owners](https://github.com/velero-io/velero/pull/9998) — velero-io/velero
- [#9999 [release-1.18] Fix PodVolumeBackup metadata loss on fs-backup timeout](https://github.com/velero-io/velero/pull/9999) — velero-io/velero
- [#10001 Skip upstream-only workflows on forks](https://github.com/velero-io/velero/pull/10001) — velero-io/velero
- [#9995 Fix PodVolumeBackup metadata loss on fs-backup timeout](https://github.com/velero-io/velero/pull/9995) — velero-io/velero
- [#9983 Add structured JSON output for velero restore describe command](https://github.com/velero-io/velero/pull/9983) — velero-io/velero
- [#9989 fix globalExcludes lookup](https://github.com/velero-io/velero/pull/9989) — velero-io/velero
- [#9990 fix rate limit issue for e2e-test-kind job](https://github.com/velero-io/velero/pull/9990) — velero-io/velero
- [#9992 Bump docker/setup-qemu-action from 3 to 4](https://github.com/velero-io/velero/pull/9992) — velero-io/velero
- [#9984 File system restore happens in parallel](https://github.com/velero-io/velero/pull/9984) — velero-io/velero
- [#9982 Validate user-provided labels and annotations in maintenance job](https://github.com/velero-io/velero/pull/9982) — velero-io/velero
- [#9966 add cli for create/view restore resource policies](https://github.com/velero-io/velero/pull/9966) — velero-io/velero
- [#9979 Block uploader backup implementation](https://github.com/velero-io/velero/pull/9979) — velero-io/velero
- [#9978 Add image volume type support to volume policies](https://github.com/velero-io/velero/pull/9978) — velero-io/velero

**openshift** (44)
- [#2308 [oadp-1.6] Add pods/log RBAC for kubevirt datamover controller](https://github.com/openshift/oadp-operator/pull/2308) — openshift/oadp-operator
- [#2311 update go.mod](https://github.com/openshift/oadp-operator/pull/2311) — openshift/oadp-operator
- [#2297 Add pods/log RBAC for kubevirt datamover controller](https://github.com/openshift/oadp-operator/pull/2297) — openshift/oadp-operator
- [#2306 OADP-8445: Add readiness probes to CLI and VMDP](https://github.com/openshift/oadp-operator/pull/2306) — openshift/oadp-operator
- [#2303 update go.mod](https://github.com/openshift/oadp-operator/pull/2303) — openshift/oadp-operator
- [#81944 Add Prow presubmit CI for migtools/kopia oadp-1.3 through 1.6](https://github.com/openshift/release/pull/81944) — openshift/release
- [#544 Fix CVE-2026-34986](https://github.com/openshift/velero/pull/544) — openshift/velero
- [#132 Merge https://github.com/openshift/oadp-must-gather:oadp-1.5 (93d7396) into oadp-1.5](https://github.com/openshift/oadp-must-gather/pull/132) — openshift/oadp-must-gather
- [#143 Fix CVE-2026-29181](https://github.com/openshift/oadp-must-gather/pull/143) — openshift/oadp-must-gather
- [#146 Merge https://github.com/openshift/oadp-must-gather:oadp-1.6 (6f83cfa) into oadp-1.6](https://github.com/openshift/oadp-must-gather/pull/146) — openshift/oadp-must-gather
- [#81828 add migtools kubevirt plugin  image build and basic ci ](https://github.com/openshift/release/pull/81828) — openshift/release
- [#2295 Fix CVE-2026-34986](https://github.com/openshift/oadp-operator/pull/2295) — openshift/oadp-operator
- [#155 Merge https://github.com/velero-io/velero-plugin-for-aws:v1.10.1 (5c92b55) into oadp-1.4](https://github.com/openshift/velero-plugin-for-aws/pull/155) — openshift/velero-plugin-for-aws
- [#2300 Backport cli e2e 1.3](https://github.com/openshift/oadp-operator/pull/2300) — openshift/oadp-operator
- [#2299 Backport cli download 1.3](https://github.com/openshift/oadp-operator/pull/2299) — openshift/oadp-operator
- [#81879 Added Prow CI oadp-1.3 cli](https://github.com/openshift/release/pull/81879) — openshift/release
- [#94 Merge https://github.com/vmware-tanzu/velero-plugin-for-csi:v0.6.3 (18cc41e) into oadp-1.3](https://github.com/openshift/velero-plugin-for-csi/pull/94) — openshift/velero-plugin-for-csi
- [#548 UPSTREAM: <carry>: Fix non-constant format strings flagged by go vet](https://github.com/openshift/velero/pull/548) — openshift/velero
- [#547 Fix gofmt alignment and missing blob.Storage mock methods](https://github.com/openshift/velero/pull/547) — openshift/velero
- [#294 Fix 4 CVEs (CVE-2026-25681, CVE-2026-27136, CVE-2026-33814, ...)](https://github.com/openshift/hypershift-oadp-plugin/pull/294) — openshift/hypershift-oadp-plugin
- [#139 remove oc cli from konflux build](https://github.com/openshift/oadp-must-gather/pull/139) — openshift/oadp-must-gather
- [#2293 Added oadp-cli-binaries-rhel9 to bundle/image-references for oadp-1.4](https://github.com/openshift/oadp-operator/pull/2293) — openshift/oadp-operator
- [#59 Fix CVE-2025-65637](https://github.com/openshift/restic/pull/59) — openshift/restic
- [#137 remove the oc binary](https://github.com/openshift/oadp-must-gather/pull/137) — openshift/oadp-must-gather
- [#136 oadp-dev: remove oc from oadp-must-gather](https://github.com/openshift/oadp-must-gather/pull/136) — openshift/oadp-must-gather
- [#2291 Backport cli download 1.4](https://github.com/openshift/oadp-operator/pull/2291) — openshift/oadp-operator
- [#2292 Backport cli e2e 1.4](https://github.com/openshift/oadp-operator/pull/2292) — openshift/oadp-operator
- [#81580 Added e2e-test-cli-aws job for oadp-1.4](https://github.com/openshift/release/pull/81580) — openshift/release
- [#541 Merge https://github.com/velero-io/velero:v1.16.2 (a608082) into oadp-1.5](https://github.com/openshift/velero/pull/541) — openshift/velero
- [#540 Merge https://github.com/velero-io/velero:v1.14.0 (2fc6300) into oadp-1.4](https://github.com/openshift/velero/pull/540) — openshift/velero
- [#133 Merge https://github.com/openshift/oadp-must-gather:oadp-1.3 (99e56dd) into oadp-1.3](https://github.com/openshift/oadp-must-gather/pull/133) — openshift/oadp-must-gather
- [#81619 Add mirroring for v1.26 konveyor golang builder](https://github.com/openshift/release/pull/81619) — openshift/release
- [#81582 update golang builder to match ocpbuilder](https://github.com/openshift/release/pull/81582) — openshift/release
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

**migtools** (15)
- [#128 [oadp-1.6] Migrate from deprecated s3/manager to s3/transfermanager](https://github.com/migtools/kubevirt-datamover-controller/pull/128) — migtools/kubevirt-datamover-controller
- [#94 UPSTREAM: <carry>: Fix test mocks for controller-runtime v0.24.0](https://github.com/migtools/oadp-vm-file-restore/pull/94) — migtools/oadp-vm-file-restore
- [#116 Refactored objectstore to prepare for Azure/GCP support](https://github.com/migtools/kubevirt-datamover-controller/pull/116) — migtools/kubevirt-datamover-controller
- [#234 Merge https://github.com/migtools/oadp-cli:oadp-dev (7e52e4a) into oadp-dev](https://github.com/migtools/oadp-cli/pull/234) — migtools/oadp-cli
- [#117 [oadp-1.6] Stream datamover pod logs to controller on pod termination](https://github.com/migtools/kubevirt-datamover-controller/pull/117) — migtools/kubevirt-datamover-controller
- [#107 Stream datamover pod logs to controller on pod termination](https://github.com/migtools/kubevirt-datamover-controller/pull/107) — migtools/kubevirt-datamover-controller
- [#114 [oadp-1.6] Phase 0+1: DataDownload prerequisites and shared helper extraction](https://github.com/migtools/kubevirt-datamover-controller/pull/114) — migtools/kubevirt-datamover-controller
- [#32 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-dev (f7b4df7) into oadp-dev](https://github.com/migtools/kubevirt-datamover-plugin/pull/32) — migtools/kubevirt-datamover-plugin
- [#77 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.7.1 (c30669d) into oadp-1.4](https://github.com/migtools/kubevirt-velero-plugin/pull/77) — migtools/kubevirt-velero-plugin
- [#227 Merge https://github.com/migtools/oadp-cli:oadp-1.4 (ab82758) into oadp-1.4](https://github.com/migtools/oadp-cli/pull/227) — migtools/oadp-cli
- [#364 Merge https://github.com/migtools/oadp-non-admin:oadp-dev (58c8b91) into oadp-dev](https://github.com/migtools/oadp-non-admin/pull/364) — migtools/oadp-non-admin
- [#43 Merge https://github.com/project-velero/kopia:v0.23.1-velero-patch (d83462d) into oadp-dev](https://github.com/migtools/kopia/pull/43) — migtools/kopia
- [#76 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.6.2 (d08eee6) into oadp-1.3](https://github.com/migtools/kubevirt-velero-plugin/pull/76) — migtools/kubevirt-velero-plugin
- [#176 Bump golang.org/x/crypto from 0.41.0 to 0.52.0](https://github.com/migtools/udistribution/pull/176) — migtools/udistribution
- [#90 Bump google.golang.org/grpc from 1.77.0 to 1.79.3 in the go_modules group across 1 directory](https://github.com/migtools/oadp-vm-file-restore/pull/90) — migtools/oadp-vm-file-restore

**Other** (9)
- [#155 fix git query issue that is causing miscount](https://github.com/oadp-rebasebot/oadp-rebase/pull/155) — oadp-rebasebot/oadp-rebase
- [#3157 ART-21639: preserve Dockerfile reinstall commands](https://github.com/openshift-eng/art-tools/pull/3157) — openshift-eng/art-tools
- [#1 Override Vertex/Bedrock providers in generated Claude Code env command](https://github.com/kaovilai/copilot-api/pull/1) — kaovilai/copilot-api
- [#443 e2e: Add e2e test for verifying hooks execution on virt-launcher pod included via AdditionalItems when backup uses labelSelector](https://github.com/kubevirt/kubevirt-velero-plugin/pull/443) — kubevirt/kubevirt-velero-plugin
- [#146 Add rebasebot config for migtools/oadp-cli oadp-1.3](https://github.com/oadp-rebasebot/oadp-rebase/pull/146) — oadp-rebasebot/oadp-rebase
- [#135 Modularize remediate.sh into discrete functions](https://github.com/oadp-rebasebot/oadp-rebase/pull/135) — oadp-rebasebot/oadp-rebase
- [#45 Update README.md to document current image variants and workflows](https://github.com/konveyor/builder/pull/45) — konveyor/builder
- [#120 Handle missing Quay images gracefully in CVE scan](https://github.com/oadp-rebasebot/oadp-rebase/pull/120) — oadp-rebasebot/oadp-rebase
- [#117 Add Trivy-based CVE scanning pipeline](https://github.com/oadp-rebasebot/oadp-rebase/pull/117) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (33)

**velero-io** (14)
- [#9381 Unhandled Error: Failed to watch authorization](https://github.com/velero-io/velero/issues/9381) — velero-io/velero
- [#9483 Remove Restic from Velero Doc](https://github.com/velero-io/velero/issues/9483) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#9429 velero doesn't correctly handle an empty ProviderSnapshotID](https://github.com/velero-io/velero/issues/9429) — velero-io/velero
- [#8801 Design configurable restore of Running/Completed/Failed Jobs](https://github.com/velero-io/velero/issues/8801) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9858 Add global VolumePolicy](https://github.com/velero-io/velero/issues/9858) — velero-io/velero
- [#5470 Add CODEOWNERS files voting](https://github.com/velero-io/velero/issues/5470) — velero-io/velero
- [#8668 Download Links for S3 Bucket content are broken when using SSE-C encryption](https://github.com/velero-io/velero/issues/8668) — velero-io/velero
- [#8277 CSI Backup fails upon provisioner and csi driver mismatch (everest-csi)](https://github.com/velero-io/velero/issues/8277) — velero-io/velero
- [#7564 Add support to output restore describe in multiple format like backups](https://github.com/velero-io/velero/issues/7564) — velero-io/velero
- [#9600 Deprecation: Remove `BackupStorageLocation.Spec.ObjectStorage.CACert` inline field in favor of `CACertRef` secret reference](https://github.com/velero-io/velero/issues/9600) — velero-io/velero

**openshift** (4)
- [#439 Image stream backup: Azure Workload Identity (WIF) not supported in registry env var wiring](https://github.com/openshift/openshift-velero-plugin/issues/439) — openshift/openshift-velero-plugin
- [#281 Move to FIPS enabled builder](https://github.com/openshift/velero/issues/281) — openshift/velero
- [#254 oadp-1.2 missing OWNERS file for tide](https://github.com/openshift/velero/issues/254) — openshift/velero
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero

**migtools** (2)
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#112 Temp backup PVC hardcoded to 10Gi (ensureTempPVC), causing silent backup failures for larger disks](https://github.com/migtools/kubevirt-datamover-controller/issues/112) — migtools/kubevirt-datamover-controller

**Other** (13)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#6786 Build cancellation leaves orphaned QEMU processes: no timeout on state polling loop](https://github.com/podman-container-tools/buildah/issues/6786) — podman-container-tools/buildah
- [#15702 Subsequent funnel of the same name from different node breaks HTTPS](https://github.com/tailscale/tailscale/issues/15702) — tailscale/tailscale
- [#317 Command used when Vertex AI is set up for Claude Code does not override Vertex AI.](https://github.com/caozhiyuan/copilot-api/issues/317) — caozhiyuan/copilot-api
- [#18471 IncrementalBackup: backup fails with "No space left on device" shortly after creating the qcow2 metadata overlay, unrelated to any volume's real free space](https://github.com/kubevirt/kubevirt/issues/18471) — kubevirt/kubevirt
- [#81 https://www.google.com/maps/ -> https://www.google.com/maps/?authuser=1](https://github.com/URLAutoRedirector/URLAutoRedirector/issues/81) — URLAutoRedirector/URLAutoRedirector
- [#1013 Support mDNS for name and service resolution](https://github.com/tailscale/tailscale/issues/1013) — tailscale/tailscale
- [#1419 `kubectl explain -o md`](https://github.com/kubernetes/kubectl/issues/1419) — kubernetes/kubectl
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#245 Package errors looking for new maintainers](https://github.com/pkg/errors/issues/245) — pkg/errors
- [#2387 Downgrade min go adopt https://github.com/googleapis/google-api-go-client/pull/3640](https://github.com/sigstore/fulcio/issues/2387) — sigstore/fulcio
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
- [#502 Enhancement: Allow combining `run_if_changed` and `skip_if_only_changed` for more flexible job triggering](https://github.com/kubernetes-sigs/prow/issues/502) — kubernetes-sigs/prow
## Issues Closed (14)

**velero-io** (1)
- [#9959 Ensure Dependabot PRs get changelog-not-required label](https://github.com/velero-io/velero/issues/9959) — velero-io/velero

**openshift** (3)
- [#552 Configure required_status_checks.contexts in Prow branch protection (velero + plugin forks)](https://github.com/openshift/velero/issues/552) — openshift/velero
- [#281 Move to FIPS enabled builder](https://github.com/openshift/velero/issues/281) — openshift/velero
- [#254 oadp-1.2 missing OWNERS file for tide](https://github.com/openshift/velero/issues/254) — openshift/velero

**migtools** (1)
- [#112 Temp backup PVC hardcoded to 10Gi (ensureTempPVC), causing silent backup failures for larger disks](https://github.com/migtools/kubevirt-datamover-controller/issues/112) — migtools/kubevirt-datamover-controller

**Other** (9)
- [#164 Transient curl failures during kind/kubectl download abort the whole job (no retry)](https://github.com/helm/kind-action/issues/164) — helm/kind-action
- [#15702 Subsequent funnel of the same name from different node breaks HTTPS](https://github.com/tailscale/tailscale/issues/15702) — tailscale/tailscale
- [#318 Should also have an environment variable for the default Opus model, allowing opus+sonnet+haiku usage.](https://github.com/caozhiyuan/copilot-api/issues/318) — caozhiyuan/copilot-api
- [#317 Command used when Vertex AI is set up for Claude Code does not override Vertex AI.](https://github.com/caozhiyuan/copilot-api/issues/317) — caozhiyuan/copilot-api
- [#18471 IncrementalBackup: backup fails with "No space left on device" shortly after creating the qcow2 metadata overlay, unrelated to any volume's real free space](https://github.com/kubevirt/kubevirt/issues/18471) — kubevirt/kubevirt
- [#81 https://www.google.com/maps/ -> https://www.google.com/maps/?authuser=1](https://github.com/URLAutoRedirector/URLAutoRedirector/issues/81) — URLAutoRedirector/URLAutoRedirector
- [#1358 bug: gateway crash-loops on macOS — binds to VM-internal podman bridge IP (10.89.0.1) on host](https://github.com/NVIDIA/OpenShell/issues/1358) — NVIDIA/OpenShell
- [#44 Update README.md to reflect current repo](https://github.com/konveyor/builder/issues/44) — konveyor/builder
- [#2387 Downgrade min go adopt https://github.com/googleapis/google-api-go-client/pull/3640](https://github.com/sigstore/fulcio/issues/2387) — sigstore/fulcio
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
