# Activity Log

> **Period:** 2026-07-16 — 2026-07-30
> **Generated:** 2026-07-30 17:58:02 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 30 |
| PRs Opened | 62 |
| PRs Reviewed | 80 |
| Issues/PRs Commented | 40 |
| Issues Closed | 24 |

---

## PRs Merged (30)

**velero-io** (6)
- [#10024 Derive dev-tool CLI versions from go.mod (ginkgo, protoc-gen-go, goimports)](https://github.com/velero-io/velero/pull/10024) — velero-io/velero
- [#10030 Fix flaky TestKopiaObjectWriterEx_ConcurrentAsyncErrors](https://github.com/velero-io/velero/pull/10030) — velero-io/velero
- [#10049 Fix CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/pull/10049) — velero-io/velero
- [#10019 Remove Auto Request Review workflow in favor of CODEOWNERS](https://github.com/velero-io/velero/pull/10019) — velero-io/velero
- [#9886 Scrub Restic references from main Velero docs](https://github.com/velero-io/velero/pull/9886) — velero-io/velero
- [#313 [release-1.14] Fix prevent amz-checksum encapsulation when checksumAlgorithm=""](https://github.com/velero-io/velero-plugin-for-aws/pull/313) — velero-io/velero-plugin-for-aws

**openshift** (7)
- [#5329 pkg/steps: pin bundle builds to amd64 nodes](https://github.com/openshift/ci-tools/pull/5329) — openshift/ci-tools
- [#2313 Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2313) — openshift/oadp-operator
- [#82434 Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/82434) — openshift/release
- [#82429 Bump migtools/kubevirt-datamover-controller build root to ubi9-v1.26](https://github.com/openshift/release/pull/82429) — openshift/release
- [#82189 Exclude copilot/* branches from migtools branch protection](https://github.com/openshift/release/pull/82189) — openshift/release
- [#444 OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/444) — openshift/openshift-velero-plugin
- [#63 Group all Go dependency updates in Dependabot](https://github.com/openshift/restic/pull/63) — openshift/restic

**migtools** (10)
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#143 oadp-1.6: Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/143) — migtools/kubevirt-datamover-controller
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#142 Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/142) — migtools/kubevirt-datamover-controller
- [#115 feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/115) — migtools/kubevirt-datamover-controller
- [#77 Force full backup when BSL checkpoint validation cannot confirm a valid chain](https://github.com/migtools/kubevirt-datamover-controller/pull/77) — migtools/kubevirt-datamover-controller
- [#119 ci: upgrade workflow actions off deprecated Node 20](https://github.com/migtools/kubevirt-datamover-controller/pull/119) — migtools/kubevirt-datamover-controller
- [#110 Fix evaluateVMBackupStatus to read VMBackup failure detail from Reason, not Message](https://github.com/migtools/kubevirt-datamover-controller/pull/110) — migtools/kubevirt-datamover-controller
- [#28 Group all Go dependency updates in Dependabot](https://github.com/migtools/filebrowser/pull/28) — migtools/filebrowser
- [#177 Group all Go dependency updates in Dependabot](https://github.com/migtools/udistribution/pull/177) — migtools/udistribution

**Other** (7)
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
- [#165 fix: add curl retry flags to download calls](https://github.com/helm/kind-action/pull/165) — helm/kind-action
- [#320 Copilot/refactor default models usage](https://github.com/caozhiyuan/copilot-api/pull/320) — caozhiyuan/copilot-api
- [#319 fix: override Vertex/Bedrock providers in Claude Code env command](https://github.com/caozhiyuan/copilot-api/pull/319) — caozhiyuan/copilot-api
- [#158 Enhance README with OADP Rebase Pages information](https://github.com/oadp-rebasebot/oadp-rebase/pull/158) — oadp-rebasebot/oadp-rebase
- [#495 ⚡ Bolt: Optimize file staleness checks with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/495) — kaovilai/dotfiles
- [#502 🔒 Fix insecure curl -k usage in MinIO scripts](https://github.com/kaovilai/dotfiles/pull/502) — kaovilai/dotfiles
## PRs Opened (62)

**velero-io** (21)
- [#10077 Add Dependabot auto-approve workflow](https://github.com/velero-io/velero/pull/10077) — velero-io/velero
- [#10054 Update security contact email and links in SECURITY.md](https://github.com/velero-io/velero/pull/10054) — velero-io/velero
- [#10051 docs: use consistent excludedNames glob pattern in filter design examples](https://github.com/velero-io/velero/pull/10051) — velero-io/velero
- [#10049 Fix CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/pull/10049) — velero-io/velero
- [#10047 Fix restore-wait init container ignoring pod-level securityContext](https://github.com/velero-io/velero/pull/10047) — velero-io/velero
- [#10041 [e2e][repro] NFSOwnership test: fs-backup restore silently loses file ownership on root-squashing NFS (#10040)](https://github.com/velero-io/velero/pull/10041) — velero-io/velero
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

**openshift** (11)
- [#5334 test/e2e: unpin optional-operators fixture from EOL ocp/4.6 integrated stream](https://github.com/openshift/ci-tools/pull/5334) — openshift/ci-tools
- [#82434 Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/82434) — openshift/release
- [#82429 Bump migtools/kubevirt-datamover-controller build root to ubi9-v1.26](https://github.com/openshift/release/pull/82429) — openshift/release
- [#5329 pkg/steps: pin bundle builds to amd64 nodes](https://github.com/openshift/ci-tools/pull/5329) — openshift/ci-tools
- [#449 Detect SCC UID/GID-range mismatch on namespace restore](https://github.com/openshift/openshift-velero-plugin/pull/449) — openshift/openshift-velero-plugin
- [#82189 Exclude copilot/* branches from migtools branch protection](https://github.com/openshift/release/pull/82189) — openshift/release
- [#297 [oadp-1.6] CNTRLPLANE-3167: support STS/IRSA credentials and standalone Velero](https://github.com/openshift/hypershift-oadp-plugin/pull/297) — openshift/hypershift-oadp-plugin
- [#150 Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/150) — openshift/oadp-must-gather
- [#2313 Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2313) — openshift/oadp-operator
- [#444 OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/444) — openshift/openshift-velero-plugin
- [#63 Group all Go dependency updates in Dependabot](https://github.com/openshift/restic/pull/63) — openshift/restic

**migtools** (13)
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#149 Cherry-pick #131: Azure BSL support to oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/149) — migtools/kubevirt-datamover-controller
- [#146 Fix E2E manager image build by copying all manager source in Dockerfile](https://github.com/migtools/kubevirt-datamover-controller/pull/146) — migtools/kubevirt-datamover-controller
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#143 oadp-1.6: Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/143) — migtools/kubevirt-datamover-controller
- [#142 Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/142) — migtools/kubevirt-datamover-controller
- [#141 1.6: Bump Dockerfile Go version from 1.25 to 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/141) — migtools/kubevirt-datamover-controller
- [#136 Remove 'mrnold' from OWNERS file](https://github.com/migtools/kubevirt-datamover-controller/pull/136) — migtools/kubevirt-datamover-controller
- [#124 feat: implement DataDownload controller for VM restore (issue #73 Phase 3)](https://github.com/migtools/kubevirt-datamover-controller/pull/124) — migtools/kubevirt-datamover-controller
- [#119 ci: upgrade workflow actions off deprecated Node 20](https://github.com/migtools/kubevirt-datamover-controller/pull/119) — migtools/kubevirt-datamover-controller
- [#115 feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/115) — migtools/kubevirt-datamover-controller
- [#177 Group all Go dependency updates in Dependabot](https://github.com/migtools/udistribution/pull/177) — migtools/udistribution
- [#28 Group all Go dependency updates in Dependabot](https://github.com/migtools/filebrowser/pull/28) — migtools/filebrowser

**Other** (17)
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
- [#552 ⚡ Bolt: [performance improvement] Replace find subprocesses with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/552) — kaovilai/dotfiles
- [#551 ⚡ Bolt: Remove redundant manual compinit](https://github.com/kaovilai/dotfiles/pull/551) — kaovilai/dotfiles
- [#550 ⚡ Bolt: [performance improvement] Remove redundant manual compinit execution](https://github.com/kaovilai/dotfiles/pull/550) — kaovilai/dotfiles
- [#549 ⚡ Bolt: [performance improvement] Remove redundant compinit](https://github.com/kaovilai/dotfiles/pull/549) — kaovilai/dotfiles
- [#548 ⚡ Bolt: Remove redundant compinit call for faster startup](https://github.com/kaovilai/dotfiles/pull/548) — kaovilai/dotfiles
- [#545 ⚡ Bolt: Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/545) — kaovilai/dotfiles
- [#544 ⚡ Bolt: [performance improvement] Remove redundant compinit](https://github.com/kaovilai/dotfiles/pull/544) — kaovilai/dotfiles
- [#543 ⚡ Bolt: [performance improvement] Replace find subprocesses with native Zsh globbing](https://github.com/kaovilai/dotfiles/pull/543) — kaovilai/dotfiles
- [#541 ⚡ Bolt: Remove redundant compinit for faster startup](https://github.com/kaovilai/dotfiles/pull/541) — kaovilai/dotfiles
- [#540 ⚡ Bolt: Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/540) — kaovilai/dotfiles
- [#538 ⚡ Bolt: Remove redundant compinit to improve shell startup time](https://github.com/kaovilai/dotfiles/pull/538) — kaovilai/dotfiles
- [#536 ⚡ Bolt: Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/536) — kaovilai/dotfiles
- [#532 ⚡ Bolt: [performance improvement] Remove redundant compinit for faster shell startup](https://github.com/kaovilai/dotfiles/pull/532) — kaovilai/dotfiles
- [#158 Enhance README with OADP Rebase Pages information](https://github.com/oadp-rebasebot/oadp-rebase/pull/158) — oadp-rebasebot/oadp-rebase
- [#165 fix: add curl retry flags to download calls](https://github.com/helm/kind-action/pull/165) — helm/kind-action
- [#526 ⚡ Bolt: Optimize cache expiration checks by removing external stat calls](https://github.com/kaovilai/dotfiles/pull/526) — kaovilai/dotfiles
## PRs Reviewed (80)

**velero-io** (25)
- [#10123 Feature: Add support for server args to velero install Deployment](https://github.com/velero-io/velero/pull/10123) — velero-io/velero
- [#10113 Site: update homepage CTA and add LinkedIn to footer](https://github.com/velero-io/velero/pull/10113) — velero-io/velero
- [#10101 [Cherry-Pick] RIA MustInclude annotation and VSC fix for 1.18](https://github.com/velero-io/velero/pull/10101) — velero-io/velero
- [#10098 Implement server default restore resource modifier](https://github.com/velero-io/velero/pull/10098) — velero-io/velero
- [#10097 feat(e2e) :- add E2E test for restore hook failure policies](https://github.com/velero-io/velero/pull/10097) — velero-io/velero
- [#10083 ci(push): pin action versions to commit SHAs and restrict permissions](https://github.com/velero-io/velero/pull/10083) — velero-io/velero
- [#10096 feat(e2e) :- add E2E test for BSL ReadOnly mode validation](https://github.com/velero-io/velero/pull/10096) — velero-io/velero
- [#10090 fix(kopia): fix block restore write loop slice bounds](https://github.com/velero-io/velero/pull/10090) — velero-io/velero
- [#264 Bump golang.org/x/crypto from 0.51.0 to 0.52.0](https://github.com/velero-io/velero-plugin-for-gcp/pull/264) — velero-io/velero-plugin-for-gcp
- [#265 Bump golang.org/x/net from 0.53.0 to 0.55.0](https://github.com/velero-io/velero-plugin-for-gcp/pull/265) — velero-io/velero-plugin-for-gcp
- [#10065 build(image): remove kubectl installation from build image](https://github.com/velero-io/velero/pull/10065) — velero-io/velero
- [#263 Bump google.golang.org/grpc from 1.73.0 to 1.82.1](https://github.com/velero-io/velero-plugin-for-gcp/pull/263) — velero-io/velero-plugin-for-gcp
- [#10066 Update Kopia(filesystem) uploader to support incremental and deleteExtraFile during restore](https://github.com/velero-io/velero/pull/10066) — velero-io/velero
- [#10071 Block uploader restore implementation](https://github.com/velero-io/velero/pull/10071) — velero-io/velero
- [#10056 design for RIA must-include-additional-items](https://github.com/velero-io/velero/pull/10056) — velero-io/velero
- [#10073 Issue #10043: Verify owner/permissions of restored entries and warn on mismatches](https://github.com/velero-io/velero/pull/10073) — velero-io/velero
- [#10074 Bump codecov/codecov-action from 6 to 7](https://github.com/velero-io/velero/pull/10074) — velero-io/velero
- [#10075 Bump actions/labeler from 5 to 7](https://github.com/velero-io/velero/pull/10075) — velero-io/velero
- [#10016 add documentation for fine-grained restore filters](https://github.com/velero-io/velero/pull/10016) — velero-io/velero
- [#323 Bump google.golang.org/grpc from 1.79.3 to 1.82.1](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/323) — velero-io/velero-plugin-for-microsoft-azure
- [#10064 Support set-based filter label selectors](https://github.com/velero-io/velero/pull/10064) — velero-io/velero
- [#10059 Update docs and governance links from vmware-tanzu to velero-io](https://github.com/velero-io/velero/pull/10059) — velero-io/velero
- [#314 Remove community health files now provided by org-level .github repo](https://github.com/velero-io/velero-plugin-for-aws/pull/314) — velero-io/velero-plugin-for-aws
- [#10033 Prioritize exact namespace match in restore](https://github.com/velero-io/velero/pull/10033) — velero-io/velero
- [#10011 Fine grained backup filters for 1.18](https://github.com/velero-io/velero/pull/10011) — velero-io/velero

**openshift** (26)
- [#2334 docs: fix broken links, stale paths, and typos across root and developer docs](https://github.com/openshift/oadp-operator/pull/2334) — openshift/oadp-operator
- [#2332 docs: move obsolete designs to docs/design/obsolete/ and update design docs](https://github.com/openshift/oadp-operator/pull/2332) — openshift/oadp-operator
- [#2335 docs: fix restic→kopia, field names, and plugin refs in config docs](https://github.com/openshift/oadp-operator/pull/2335) — openshift/oadp-operator
- [#2331 docs: fix links, restic refs, and typos in examples and root-level docs](https://github.com/openshift/oadp-operator/pull/2331) — openshift/oadp-operator
- [#2336 docs: remove entirely obsolete documentation files](https://github.com/openshift/oadp-operator/pull/2336) — openshift/oadp-operator
- [#2333 docs: add deprecation banners to obsolete VSM/ODF blog posts](https://github.com/openshift/oadp-operator/pull/2333) — openshift/oadp-operator
- [#157 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.4)](https://github.com/openshift/velero-plugin-for-gcp/pull/157) — openshift/velero-plugin-for-gcp
- [#156 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.3)](https://github.com/openshift/velero-plugin-for-gcp/pull/156) — openshift/velero-plugin-for-gcp
- [#158 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.5)](https://github.com/openshift/velero-plugin-for-gcp/pull/158) — openshift/velero-plugin-for-gcp
- [#556 Fix CI workflows: MinIO image, Go version, linter action, and typos](https://github.com/openshift/velero/pull/556) — openshift/velero
- [#2325 [oadp-1.4] OADP-8486: Added startup probe](https://github.com/openshift/oadp-operator/pull/2325) — openshift/oadp-operator
- [#555 [oadp-1.5] OADP-8502: Updated kopia dep to pull in tempdir fix](https://github.com/openshift/velero/pull/555) — openshift/velero
- [#2326 [oadp-1.3] OADP-8484: Added backfill to startup probe](https://github.com/openshift/oadp-operator/pull/2326) — openshift/oadp-operator
- [#2320 [oadp-1.6] OADP-8448: Added service account to dev branch](https://github.com/openshift/oadp-operator/pull/2320) — openshift/oadp-operator
- [#2324 [oadp-1.5] OADP-8485: Added startup probe](https://github.com/openshift/oadp-operator/pull/2324) — openshift/oadp-operator
- [#451 [oadp-1.6] OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/451) — openshift/openshift-velero-plugin
- [#2318 Added service account to dev branch](https://github.com/openshift/oadp-operator/pull/2318) — openshift/oadp-operator
- [#2317 OADP-8484: Add startup probe to CLI download server](https://github.com/openshift/oadp-operator/pull/2317) — openshift/oadp-operator
- [#295 Merge https://github.com/openshift/hypershift-oadp-plugin:main (e9dbba8) into main](https://github.com/openshift/hypershift-oadp-plugin/pull/295) — openshift/hypershift-oadp-plugin
- [#450 UPSTREAM: <carry>: Bump openshift/client-go and openshift/api to release-4.23](https://github.com/openshift/openshift-velero-plugin/pull/450) — openshift/openshift-velero-plugin
- [#2315 fix extended support versions](https://github.com/openshift/oadp-operator/pull/2315) — openshift/oadp-operator
- [#2309 [oadp-1.5] OADP-8455: Add readiness probes to CLI download server](https://github.com/openshift/oadp-operator/pull/2309) — openshift/oadp-operator
- [#2308 [oadp-1.6] Add pods/log RBAC for kubevirt datamover controller](https://github.com/openshift/oadp-operator/pull/2308) — openshift/oadp-operator
- [#2311 update go.mod](https://github.com/openshift/oadp-operator/pull/2311) — openshift/oadp-operator
- [#2306 OADP-8445: Add readiness probes to CLI and VMDP](https://github.com/openshift/oadp-operator/pull/2306) — openshift/oadp-operator
- [#2303 update go.mod](https://github.com/openshift/oadp-operator/pull/2303) — openshift/oadp-operator

**migtools** (28)
- [#151 [oadp-1.6] ci: fix lint for golangci-lint v2](https://github.com/migtools/kubevirt-datamover-controller/pull/151) — migtools/kubevirt-datamover-controller
- [#150 [oadp-1.6] Issue #26: Azure BSL support](https://github.com/migtools/kubevirt-datamover-controller/pull/150) — migtools/kubevirt-datamover-controller
- [#239 Backport must gather image 1.6](https://github.com/migtools/oadp-cli/pull/239) — migtools/oadp-cli
- [#148 [oadp-1.6] feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/148) — migtools/kubevirt-datamover-controller
- [#138 build(deps): bump github.com/google/cel-go from 0.26.0 to 0.29.0](https://github.com/migtools/kubevirt-datamover-controller/pull/138) — migtools/kubevirt-datamover-controller
- [#77 Merge https://github.com/kubevirt/kubevirt-velero-plugin:v0.7.1 (c30669d) into oadp-1.4](https://github.com/migtools/kubevirt-velero-plugin/pull/77) — migtools/kubevirt-velero-plugin
- [#367 Merge https://github.com/migtools/oadp-non-admin:oadp-dev (a041235) into oadp-dev](https://github.com/migtools/oadp-non-admin/pull/367) — migtools/oadp-non-admin
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#234 Merge https://github.com/migtools/oadp-cli:oadp-dev (0db1341) into oadp-dev](https://github.com/migtools/oadp-cli/pull/234) — migtools/oadp-cli
- [#36 [oadp-1.6] Bump kubevirt-datamover-controller for GCP Cloud Storage support](https://github.com/migtools/kubevirt-datamover-plugin/pull/36) — migtools/kubevirt-datamover-plugin
- [#368 [oadp-dev] Fix IncludedClusterScopedResources test panic](https://github.com/migtools/oadp-non-admin/pull/368) — migtools/oadp-non-admin
- [#35 Bump kubevirt-datamover-controller for GCP Cloud Storage support](https://github.com/migtools/kubevirt-datamover-plugin/pull/35) — migtools/kubevirt-datamover-plugin
- [#139 [oadp-1.6] Issue #95: Add GCP Cloud Storage support](https://github.com/migtools/kubevirt-datamover-controller/pull/139) — migtools/kubevirt-datamover-controller
- [#140 [oadp-1.6] ci: upgrade workflow actions off deprecated Node 20](https://github.com/migtools/kubevirt-datamover-controller/pull/140) — migtools/kubevirt-datamover-controller
- [#134 Issue #95: Add GCP Cloud Storage support](https://github.com/migtools/kubevirt-datamover-controller/pull/134) — migtools/kubevirt-datamover-controller
- [#132 [oadp-1.6] Fix evaluateVMBackupStatus to read VMBackup failure detail from Reason, not Message](https://github.com/migtools/kubevirt-datamover-controller/pull/132) — migtools/kubevirt-datamover-controller
- [#111 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-dev (3b532a1) into oadp-dev](https://github.com/migtools/kubevirt-datamover-controller/pull/111) — migtools/kubevirt-datamover-controller
- [#365 ⬆ Bump actions/setup-go from 5 to 7](https://github.com/migtools/oadp-non-admin/pull/365) — migtools/oadp-non-admin
- [#94 UPSTREAM: <carry>: Fix test mocks for controller-runtime v0.24.0](https://github.com/migtools/oadp-vm-file-restore/pull/94) — migtools/oadp-vm-file-restore
- [#235 [oadp-1.6] OADP-8340: Error when modifying DPA-managed BSL via --cacert and --credential](https://github.com/migtools/oadp-cli/pull/235) — migtools/oadp-cli
- [#129 Bump Dockerfile builder image to golang:1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/129) — migtools/kubevirt-datamover-controller
- [#128 [oadp-1.6] Migrate from deprecated s3/manager to s3/transfermanager](https://github.com/migtools/kubevirt-datamover-controller/pull/128) — migtools/kubevirt-datamover-controller
- [#116 Refactored objectstore to prepare for Azure/GCP support](https://github.com/migtools/kubevirt-datamover-controller/pull/116) — migtools/kubevirt-datamover-controller
- [#117 [oadp-1.6] Stream datamover pod logs to controller on pod termination](https://github.com/migtools/kubevirt-datamover-controller/pull/117) — migtools/kubevirt-datamover-controller
- [#114 [oadp-1.6] Phase 0+1: DataDownload prerequisites and shared helper extraction](https://github.com/migtools/kubevirt-datamover-controller/pull/114) — migtools/kubevirt-datamover-controller
- [#32 Merge https://github.com/migtools/kubevirt-datamover-plugin:oadp-dev (f7b4df7) into oadp-dev](https://github.com/migtools/kubevirt-datamover-plugin/pull/32) — migtools/kubevirt-datamover-plugin
- [#364 Merge https://github.com/migtools/oadp-non-admin:oadp-dev (58c8b91) into oadp-dev](https://github.com/migtools/oadp-non-admin/pull/364) — migtools/oadp-non-admin
- [#43 Merge https://github.com/project-velero/kopia:v0.23.1-velero-patch (d83462d) into oadp-dev](https://github.com/migtools/kopia/pull/43) — migtools/kopia

**Other** (1)
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
## Issues/PRs Commented On (40)

**velero-io** (22)
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#8466 Velero doesnt do well with Minio bucket versioning ](https://github.com/velero-io/velero/issues/8466) — velero-io/velero
- [#9957 `VolumeSnapshotContent` resources are forcefully restored, ignoring `includedResources` and `excludedResources` filters](https://github.com/velero-io/velero/issues/9957) — velero-io/velero
- [#10092 Deprecate the block volume backup/restore functionality through Kopia file system uploader](https://github.com/velero-io/velero/issues/10092) — velero-io/velero
- [#8686 Avoid overwriting during backup to support object lock enabled buckets](https://github.com/velero-io/velero/issues/8686) — velero-io/velero
- [#9600 Deprecation: Remove `BackupStorageLocation.Spec.ObjectStorage.CACert` inline field in favor of `CACertRef` secret reference](https://github.com/velero-io/velero/issues/9600) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#10078 CI to check doc compliance with code change](https://github.com/velero-io/velero/issues/10078) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#8807 Support per-storageclass VSClass annotation](https://github.com/velero-io/velero/issues/8807) — velero-io/velero
- [#8277 CSI Backup fails upon provisioner and csi driver mismatch (everest-csi)](https://github.com/velero-io/velero/issues/8277) — velero-io/velero
- [#9398 Velero Restore Does Not Preserve Original File Permissions on PVCs on AZURE](https://github.com/velero-io/velero/issues/9398) — velero-io/velero
- [#9951 v1.14.2 AWS plugin corrupts backups on S3-compatible backends via SDK checksum defaults](https://github.com/velero-io/velero/issues/9951) — velero-io/velero
- [#10020 E2E CI flake: "kind-action" curl connection reset during kind install](https://github.com/velero-io/velero/issues/10020) — velero-io/velero
- [#9381 Unhandled Error: Failed to watch authorization](https://github.com/velero-io/velero/issues/9381) — velero-io/velero
- [#9483 Remove Restic from Velero Doc](https://github.com/velero-io/velero/issues/9483) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#9429 velero doesn't correctly handle an empty ProviderSnapshotID](https://github.com/velero-io/velero/issues/9429) — velero-io/velero
- [#8801 Design configurable restore of Running/Completed/Failed Jobs](https://github.com/velero-io/velero/issues/8801) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9858 Add global VolumePolicy](https://github.com/velero-io/velero/issues/9858) — velero-io/velero

**openshift** (1)
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero

**migtools** (3)
- [#74 Force full backup when BSL checkpoint validation fails](https://github.com/migtools/kubevirt-datamover-controller/issues/74) — migtools/kubevirt-datamover-controller
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller
- [#112 Temp backup PVC hardcoded to 10Gi (ensureTempPVC), causing silent backup failures for larger disks](https://github.com/migtools/kubevirt-datamover-controller/issues/112) — migtools/kubevirt-datamover-controller

**Other** (14)
- [#1997 [CNCF LFX Proposal] Velero CSI E2E Testing](https://github.com/cncf/mentoring/issues/1997) — cncf/mentoring
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#736 Tide status controller falsely reports "In merge pool." for PRs blocked by a never-triggered required context](https://github.com/kubernetes-sigs/prow/issues/736) — kubernetes-sigs/prow
- [#110 [improve] Performance: add Vite manual chunk splitting for better browser caching](https://github.com/kaovilai/kaovilai.pw/issues/110) — kaovilai/kaovilai.pw
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
- [#4564 Upgrade AWS SDK to /v2](https://github.com/distribution/distribution/issues/4564) — distribution/distribution
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
- [#121 [FEATURE] Matrix Strategy Multi-Arch example](https://github.com/redhat-actions/buildah-build/issues/121) — redhat-actions/buildah-build
- [#330 Omit  ANTHROPIC_MODEL: sonnetModel ?? opusModel, from claude-code so selected model option sticks](https://github.com/caozhiyuan/copilot-api/issues/330) — caozhiyuan/copilot-api
- [#1807 Support Google Vertex AI with Application Default Credentials (ADC)](https://github.com/pingdotgg/t3code/issues/1807) — pingdotgg/t3code
- [#6786 Build cancellation leaves orphaned QEMU processes: no timeout on state polling loop](https://github.com/podman-container-tools/buildah/issues/6786) — podman-container-tools/buildah
- [#15702 Subsequent funnel of the same name from different node breaks HTTPS](https://github.com/tailscale/tailscale/issues/15702) — tailscale/tailscale
- [#317 Command used when Vertex AI is set up for Claude Code does not override Vertex AI.](https://github.com/caozhiyuan/copilot-api/issues/317) — caozhiyuan/copilot-api
- [#18471 IncrementalBackup: backup fails with "No space left on device" shortly after creating the qcow2 metadata overlay, unrelated to any volume's real free space](https://github.com/kubevirt/kubevirt/issues/18471) — kubevirt/kubevirt
## Issues Closed (24)

**velero-io** (6)
- [#10022 Flaky unit test:  TestBlockUploaderBackup/success_full_backup](https://github.com/velero-io/velero/issues/10022) — velero-io/velero
- [#10042 Add `.github` repo](https://github.com/velero-io/velero/issues/10042) — velero-io/velero
- [#10050 nits for fine-grained filter docs](https://github.com/velero-io/velero/issues/10050) — velero-io/velero
- [#10023 Ginkgo CLI Version Mismatch GoMod Import](https://github.com/velero-io/velero/issues/10023) — velero-io/velero
- [#10029 Flaky test: TestKopiaObjectWriterEx_ConcurrentAsyncErrors can observe async error before all writes are queued](https://github.com/velero-io/velero/issues/10029) — velero-io/velero
- [#10048 CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/issues/10048) — velero-io/velero

**openshift** (3)
- [#5328 src-bundle build flake: no node selector lets buildah pod land on arm64 node, fails pulling amd64-only pipeline:src manifest list](https://github.com/openshift/ci-tools/issues/5328) — openshift/ci-tools
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero
- [#443 OADP-7384: ImageStream backup fails with `manifest unknown` when a status tag item references another namespace's repository and that reference is stale](https://github.com/openshift/openshift-velero-plugin/issues/443) — openshift/openshift-velero-plugin

**migtools** (3)
- [#118 lint workflow is using node20](https://github.com/migtools/kubevirt-datamover-controller/issues/118) — migtools/kubevirt-datamover-controller
- [#108 evaluateVMBackupStatus misses real VMBackup failures due to exact-match on Progressing.Reason=="Failed"](https://github.com/migtools/kubevirt-datamover-controller/issues/108) — migtools/kubevirt-datamover-controller
- [#112 Temp backup PVC hardcoded to 10Gi (ensureTempPVC), causing silent backup failures for larger disks](https://github.com/migtools/kubevirt-datamover-controller/issues/112) — migtools/kubevirt-datamover-controller

**Other** (12)
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
---

*This report is automatically generated every Monday at 5am EST by GitHub Actions.*
