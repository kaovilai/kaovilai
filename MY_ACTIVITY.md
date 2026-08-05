# Activity Log

> **Period:** 2026-07-22 — 2026-08-05
> **Generated:** 2026-08-05 14:14:21 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 62 |
| PRs Opened | 82 |
| PRs Reviewed | 98 |
| Issues/PRs Commented | 42 |
| Issues Closed | 30 |

---

## PRs Merged (62)

**velero-io** (3)
- [#10024 Derive dev-tool CLI versions from go.mod (ginkgo, protoc-gen-go, goimports)](https://github.com/velero-io/velero/pull/10024) — velero-io/velero
- [#10030 Fix flaky TestKopiaObjectWriterEx_ConcurrentAsyncErrors](https://github.com/velero-io/velero/pull/10030) — velero-io/velero
- [#10049 Fix CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/pull/10049) — velero-io/velero

**openshift** (35)
- [#2353 Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2353) — openshift/oadp-operator
- [#2352 Add datadownloads RBAC to kubevirt-datamover ClusterRole](https://github.com/openshift/oadp-operator/pull/2352) — openshift/oadp-operator
- [#82762 Add CI image substitutions for OADP plugin images (base_images + operator.substitutions)](https://github.com/openshift/release/pull/82762) — openshift/release
- [#2340 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2340) — openshift/oadp-operator
- [#460 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/460) — openshift/openshift-velero-plugin
- [#458 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/458) — openshift/openshift-velero-plugin
- [#150 Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/150) — openshift/oadp-must-gather
- [#459 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/459) — openshift/openshift-velero-plugin
- [#82764 Bump openshift-velero-plugin CI memory limit from 4Gi to 8Gi](https://github.com/openshift/release/pull/82764) — openshift/release
- [#2344 Add missing image-producing repo badges to README](https://github.com/openshift/oadp-operator/pull/2344) — openshift/oadp-operator
- [#2341 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2341) — openshift/oadp-operator
- [#2342 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2342) — openshift/oadp-operator
- [#559 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/559) — openshift/velero
- [#561 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/561) — openshift/velero
- [#557 Remove inactive users from OWNERS](https://github.com/openshift/velero/pull/557) — openshift/velero
- [#82747 Remove unused releases: blocks from OADP ci-operator configs](https://github.com/openshift/release/pull/82747) — openshift/release
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/161) — openshift/velero-plugin-for-microsoft-azure
- [#76 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/76) — openshift/velero-plugin-for-legacy-aws
- [#75 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/75) — openshift/velero-plugin-for-legacy-aws
- [#74 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/74) — openshift/velero-plugin-for-legacy-aws
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/162) — openshift/velero-plugin-for-gcp
- [#154 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/154) — openshift/oadp-must-gather
- [#153 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/153) — openshift/oadp-must-gather
- [#155 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/155) — openshift/oadp-must-gather
- [#152 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/152) — openshift/oadp-must-gather
- [#77 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/77) — openshift/velero-plugin-for-legacy-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/161) — openshift/velero-plugin-for-aws
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/162) — openshift/velero-plugin-for-microsoft-azure
- [#560 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/560) — openshift/velero
- [#5329 pkg/steps: pin bundle builds to amd64 nodes](https://github.com/openshift/ci-tools/pull/5329) — openshift/ci-tools
- [#2313 Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2313) — openshift/oadp-operator
- [#82434 Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/82434) — openshift/release
- [#82429 Bump migtools/kubevirt-datamover-controller build root to ubi9-v1.26](https://github.com/openshift/release/pull/82429) — openshift/release
- [#82189 Exclude copilot/* branches from migtools branch protection](https://github.com/openshift/release/pull/82189) — openshift/release
- [#444 OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/444) — openshift/openshift-velero-plugin

**migtools** (11)
- [#371 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/371) — migtools/oadp-non-admin
- [#40 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/40) — migtools/kubevirt-datamover-plugin
- [#157 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/157) — migtools/kubevirt-datamover-controller
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#143 oadp-1.6: Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/143) — migtools/kubevirt-datamover-controller
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#142 Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/142) — migtools/kubevirt-datamover-controller
- [#115 feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/115) — migtools/kubevirt-datamover-controller
- [#77 Force full backup when BSL checkpoint validation cannot confirm a valid chain](https://github.com/migtools/kubevirt-datamover-controller/pull/77) — migtools/kubevirt-datamover-controller
- [#119 ci: upgrade workflow actions off deprecated Node 20](https://github.com/migtools/kubevirt-datamover-controller/pull/119) — migtools/kubevirt-datamover-controller
- [#110 Fix evaluateVMBackupStatus to read VMBackup failure detail from Reason, not Message](https://github.com/migtools/kubevirt-datamover-controller/pull/110) — migtools/kubevirt-datamover-controller

**Other** (13)
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
- [#149 Fix command bar overlapping review dialog comment box](https://github.com/kaovilai/github-bot-command-palette/pull/149) — kaovilai/github-bot-command-palette
- [#174 Addressing date and time display per browser timezone](https://github.com/kaovilai/kaovilai.pw/pull/174) — kaovilai/kaovilai.pw
- [#3 Follow-up fixes for #967 subagent routing opt-out and provenance scoping](https://github.com/kaovilai/context-mode/pull/3) — kaovilai/context-mode
- [#2 Reduce permission-classifier false positives on injected subagent routing block](https://github.com/kaovilai/context-mode/pull/2) — kaovilai/context-mode
- [#148 Group Dependabot updates per ecosystem](https://github.com/kaovilai/github-bot-command-palette/pull/148) — kaovilai/github-bot-command-palette
- [#138 Add structured payload picker dialog (stacked on #137)](https://github.com/kaovilai/github-bot-command-palette/pull/138) — kaovilai/github-bot-command-palette
- [#137 Add OpenShift static command profiles (payload, verified, jira, labels, specialized)](https://github.com/kaovilai/github-bot-command-palette/pull/137) — kaovilai/github-bot-command-palette
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
- [#2 Add PAT-free gh-aw agentic workflows](https://github.com/kaovilai/redirector/pull/2) — kaovilai/redirector
- [#1 Add Dependabot config with grouped PRs](https://github.com/kaovilai/redirector/pull/1) — kaovilai/redirector
- [#2 Implement Route 127 trailer strategy calculator as a static GitHub Pages site](https://github.com/kaovilai/route-127-trailer-nc/pull/2) — kaovilai/route-127-trailer-nc
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
## PRs Opened (82)

**velero-io** (1)
- [#10077 Add Dependabot auto-approve workflow](https://github.com/velero-io/velero/pull/10077) — velero-io/velero

**openshift** (40)
- [#2358 [oadp-1.4] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2358) — openshift/oadp-operator
- [#2357 [oadp-1.5] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2357) — openshift/oadp-operator
- [#2353 Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2353) — openshift/oadp-operator
- [#2352 Add datadownloads RBAC to kubevirt-datamover ClusterRole](https://github.com/openshift/oadp-operator/pull/2352) — openshift/oadp-operator
- [#2350 Add e2e coverage for kubevirt-datamover: multi-PVC VMs and incremental backup sequence](https://github.com/openshift/oadp-operator/pull/2350) — openshift/oadp-operator
- [#5354 Support github_merge_blocks_policy in per-repo supplemental prow config](https://github.com/openshift/ci-tools/pull/5354) — openshift/ci-tools
- [#2346 docs: add CI plugin image sync guidance to common.go](https://github.com/openshift/oadp-operator/pull/2346) — openshift/oadp-operator
- [#82764 Bump openshift-velero-plugin CI memory limit from 4Gi to 8Gi](https://github.com/openshift/release/pull/82764) — openshift/release
- [#2345 Add CI plugin image substitution guide and developer comments](https://github.com/openshift/oadp-operator/pull/2345) — openshift/oadp-operator
- [#82762 Add CI image substitutions for OADP plugin images (base_images + operator.substitutions)](https://github.com/openshift/release/pull/82762) — openshift/release
- [#2344 Add missing image-producing repo badges to README](https://github.com/openshift/oadp-operator/pull/2344) — openshift/oadp-operator
- [#82747 Remove unused releases: blocks from OADP ci-operator configs](https://github.com/openshift/release/pull/82747) — openshift/release
- [#77 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/77) — openshift/velero-plugin-for-legacy-aws
- [#76 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/76) — openshift/velero-plugin-for-legacy-aws
- [#75 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/75) — openshift/velero-plugin-for-legacy-aws
- [#74 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/74) — openshift/velero-plugin-for-legacy-aws
- [#155 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/155) — openshift/oadp-must-gather
- [#154 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/154) — openshift/oadp-must-gather
- [#153 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/153) — openshift/oadp-must-gather
- [#152 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/152) — openshift/oadp-must-gather
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/162) — openshift/velero-plugin-for-gcp
- [#460 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/460) — openshift/openshift-velero-plugin
- [#162 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/162) — openshift/velero-plugin-for-microsoft-azure
- [#459 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/459) — openshift/openshift-velero-plugin
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/161) — openshift/velero-plugin-for-microsoft-azure
- [#458 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/458) — openshift/openshift-velero-plugin
- [#73 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/73) — openshift/velero-plugin-for-legacy-aws
- [#72 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/72) — openshift/velero-plugin-for-legacy-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/161) — openshift/velero-plugin-for-aws
- [#2342 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2342) — openshift/oadp-operator
- [#2341 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2341) — openshift/oadp-operator
- [#2340 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2340) — openshift/oadp-operator
- [#561 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/561) — openshift/velero
- [#560 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/560) — openshift/velero
- [#559 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/559) — openshift/velero
- [#557 Remove inactive users from OWNERS](https://github.com/openshift/velero/pull/557) — openshift/velero
- [#5334 test/e2e: unpin optional-operators fixture from EOL ocp/4.6 integrated stream](https://github.com/openshift/ci-tools/pull/5334) — openshift/ci-tools
- [#82434 Update image tag from ubi9-v1.25 to ubi9-v1.26](https://github.com/openshift/release/pull/82434) — openshift/release
- [#82429 Bump migtools/kubevirt-datamover-controller build root to ubi9-v1.26](https://github.com/openshift/release/pull/82429) — openshift/release
- [#5329 pkg/steps: pin bundle builds to amd64 nodes](https://github.com/openshift/ci-tools/pull/5329) — openshift/ci-tools

**migtools** (16)
- [#41 Add RestoreItemAction plugins to trigger kubevirt datamover restore](https://github.com/migtools/kubevirt-datamover-plugin/pull/41) — migtools/kubevirt-datamover-plugin
- [#253 Fix #252: Add exact-output assertion for schedule create example normalization](https://github.com/migtools/oadp-cli/pull/253) — migtools/oadp-cli
- [#48 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/48) — migtools/kopia
- [#40 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/40) — migtools/kubevirt-datamover-plugin
- [#157 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/157) — migtools/kubevirt-datamover-controller
- [#251 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/251) — migtools/oadp-cli
- [#371 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/371) — migtools/oadp-non-admin
- [#47 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/47) — migtools/kopia
- [#38 Cherry-pick PR #37: bump kubevirt-datamover-controller for Azure support](https://github.com/migtools/kubevirt-datamover-plugin/pull/38) — migtools/kubevirt-datamover-plugin
- [#149 Cherry-pick #131: Azure BSL support to oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/149) — migtools/kubevirt-datamover-controller
- [#146 Fix E2E manager image build by copying all manager source in Dockerfile](https://github.com/migtools/kubevirt-datamover-controller/pull/146) — migtools/kubevirt-datamover-controller
- [#144 Bump golangci-lint to v2.12.2 to match CI and support Go 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/144) — migtools/kubevirt-datamover-controller
- [#143 oadp-1.6: Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/143) — migtools/kubevirt-datamover-controller
- [#142 Bump GitHub Actions to node24 runtime versions](https://github.com/migtools/kubevirt-datamover-controller/pull/142) — migtools/kubevirt-datamover-controller
- [#141 1.6: Bump Dockerfile Go version from 1.25 to 1.26](https://github.com/migtools/kubevirt-datamover-controller/pull/141) — migtools/kubevirt-datamover-controller
- [#136 Remove 'mrnold' from OWNERS file](https://github.com/migtools/kubevirt-datamover-controller/pull/136) — migtools/kubevirt-datamover-controller

**Other** (25)
- [#149 Fix command bar overlapping review dialog comment box](https://github.com/kaovilai/github-bot-command-palette/pull/149) — kaovilai/github-bot-command-palette
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
- [#174 Addressing date and time display per browser timezone](https://github.com/kaovilai/kaovilai.pw/pull/174) — kaovilai/kaovilai.pw
- [#1034 fix(routing): self-identify subagent routing block, add opt-out (#967)](https://github.com/mksglu/context-mode/pull/1034) — mksglu/context-mode
- [#3 Follow-up fixes for #967 subagent routing opt-out and provenance scoping](https://github.com/kaovilai/context-mode/pull/3) — kaovilai/context-mode
- [#2 Reduce permission-classifier false positives on injected subagent routing block](https://github.com/kaovilai/context-mode/pull/2) — kaovilai/context-mode
- [#148 Group Dependabot updates per ecosystem](https://github.com/kaovilai/github-bot-command-palette/pull/148) — kaovilai/github-bot-command-palette
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
- [#1 fix: enforce Spec.OperationTimeout in DataUpload/DataDownload controllers](https://github.com/kaovilai/kubevirt-datamover-controller/pull/1) — kaovilai/kubevirt-datamover-controller
- [#3 Add design docs for one-click community rule install via marketplace deep links](https://github.com/kaovilai/redirector/pull/3) — kaovilai/redirector
- [#2 Add PAT-free gh-aw agentic workflows](https://github.com/kaovilai/redirector/pull/2) — kaovilai/redirector
- [#1 Add Dependabot config with grouped PRs](https://github.com/kaovilai/redirector/pull/1) — kaovilai/redirector
- [#2 Implement Route 127 trailer strategy calculator as a static GitHub Pages site](https://github.com/kaovilai/route-127-trailer-nc/pull/2) — kaovilai/route-127-trailer-nc
- [#138 Add structured payload picker dialog (stacked on #137)](https://github.com/kaovilai/github-bot-command-palette/pull/138) — kaovilai/github-bot-command-palette
- [#137 Add OpenShift static command profiles (payload, verified, jira, labels, specialized)](https://github.com/kaovilai/github-bot-command-palette/pull/137) — kaovilai/github-bot-command-palette
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
## PRs Reviewed (98)

**velero-io** (24)
- [#10158 ci: add backport/cherry-pick GitHub Action for release branches](https://github.com/velero-io/velero/pull/10158) — velero-io/velero
- [#10096 feat(e2e) :- add E2E test for BSL ReadOnly mode validation](https://github.com/velero-io/velero/pull/10096) — velero-io/velero
- [#10119 Fix csi pvc restore action](https://github.com/velero-io/velero/pull/10119) — velero-io/velero
- [#10104 Update Restore Exposer and PVC CSI to support in-place restore](https://github.com/velero-io/velero/pull/10104) — velero-io/velero
- [#10102 Verify extracted item paths stay inside the backup directory](https://github.com/velero-io/velero/pull/10102) — velero-io/velero
- [#10121 Enhancement: fail-fast on velero install wait](https://github.com/velero-io/velero/pull/10121) — velero-io/velero
- [#10132 Do not assume a port name is a string when clearing node ports](https://github.com/velero-io/velero/pull/10132) — velero-io/velero
- [#10127 feat(cli): add velero client set-context-as-velero-namespace command](https://github.com/velero-io/velero/pull/10127) — velero-io/velero
- [#10147 docs: document ownership loss on mount-constant filesystems](https://github.com/velero-io/velero/pull/10147) — velero-io/velero
- [#323 Bump google.golang.org/grpc from 1.79.3 to 1.82.1](https://github.com/velero-io/velero-plugin-for-microsoft-azure/pull/323) — velero-io/velero-plugin-for-microsoft-azure
- [#10157 docs: update community page backlog links away from classic projects](https://github.com/velero-io/velero/pull/10157) — velero-io/velero
- [#10103 Add regression test for additional item with invalid JSON](https://github.com/velero-io/velero/pull/10103) — velero-io/velero
- [#10106 Fix some issues for CBT features:](https://github.com/velero-io/velero/pull/10106) — velero-io/velero
- [#10098 Implement server default restore resource modifier](https://github.com/velero-io/velero/pull/10098) — velero-io/velero
- [#10070 Add snapshotClass parameter to volume policy snapshot action](https://github.com/velero-io/velero/pull/10070) — velero-io/velero
- [#10135 Bump github/codeql-action from 3 to 4.37.3](https://github.com/velero-io/velero/pull/10135) — velero-io/velero
- [#10097 feat(e2e) :- add E2E test for restore hook failure policies](https://github.com/velero-io/velero/pull/10097) — velero-io/velero
- [#10123 Feature: Add support for server args to velero install Deployment](https://github.com/velero-io/velero/pull/10123) — velero-io/velero
- [#10110 refactor(serverstatus): Remove outdated Kubernetes v1.9.0 workaround](https://github.com/velero-io/velero/pull/10110) — velero-io/velero
- [#10090 fix(kopia): fix block restore write loop slice bounds](https://github.com/velero-io/velero/pull/10090) — velero-io/velero
- [#10113 Site: update homepage CTA and add LinkedIn to footer](https://github.com/velero-io/velero/pull/10113) — velero-io/velero
- [#10101 [Cherry-Pick] RIA MustInclude annotation and VSC fix for 1.18](https://github.com/velero-io/velero/pull/10101) — velero-io/velero
- [#10083 ci(push): pin action versions to commit SHAs and restrict permissions](https://github.com/velero-io/velero/pull/10083) — velero-io/velero
- [#264 Bump golang.org/x/crypto from 0.51.0 to 0.52.0](https://github.com/velero-io/velero-plugin-for-gcp/pull/264) — velero-io/velero-plugin-for-gcp

**openshift** (38)
- [#2349 feat: use velero SA and add bound-sa-token volume for KDM controller](https://github.com/openshift/oadp-operator/pull/2349) — openshift/oadp-operator
- [#2356 [oadp-1.6] Fix DPA reconcile race: use MergeFrom patch for status update](https://github.com/openshift/oadp-operator/pull/2356) — openshift/oadp-operator
- [#2328 [oadp-1.6] Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2328) — openshift/oadp-operator
- [#158 [oadp-1.4] Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/158) — openshift/oadp-must-gather
- [#159 [oadp-1.6] Gather PVC/PV/Namespace(SCC) data for Backup/Restore namespaces](https://github.com/openshift/oadp-must-gather/pull/159) — openshift/oadp-must-gather
- [#82902 tide: set github_merge_blocks_policy to block for OADP repos](https://github.com/openshift/release/pull/82902) — openshift/release
- [#451 [oadp-1.6] OADP-7384: Copy imagestream images from the stream's own repository](https://github.com/openshift/openshift-velero-plugin/pull/451) — openshift/openshift-velero-plugin
- [#2329 [oadp-1.5] Add e2e test for ImageStream stale cross-namespace tag reference (OVP#443)](https://github.com/openshift/oadp-operator/pull/2329) — openshift/oadp-operator
- [#151 Remove inactive users from OWNERS](https://github.com/openshift/oadp-must-gather/pull/151) — openshift/oadp-must-gather
- [#2330 Merge https://github.com/openshift/oadp-operator:oadp-1.5 (a9247ea) into oadp-1.5](https://github.com/openshift/oadp-operator/pull/2330) — openshift/oadp-operator
- [#456 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/456) — openshift/openshift-velero-plugin
- [#453 Bump google.golang.org/grpc from 1.81.1 to 1.82.1](https://github.com/openshift/openshift-velero-plugin/pull/453) — openshift/openshift-velero-plugin
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/159) — openshift/velero-plugin-for-gcp
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/160) — openshift/velero-plugin-for-microsoft-azure
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/160) — openshift/velero-plugin-for-gcp
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/159) — openshift/velero-plugin-for-aws
- [#161 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-gcp/pull/161) — openshift/velero-plugin-for-gcp
- [#159 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-microsoft-azure/pull/159) — openshift/velero-plugin-for-microsoft-azure
- [#160 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/160) — openshift/velero-plugin-for-aws
- [#558 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero/pull/558) — openshift/velero
- [#2339 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2339) — openshift/oadp-operator
- [#457 Remove inactive users from OWNERS](https://github.com/openshift/openshift-velero-plugin/pull/457) — openshift/openshift-velero-plugin
- [#70 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/70) — openshift/velero-plugin-for-legacy-aws
- [#2338 Remove inactive users from OWNERS](https://github.com/openshift/oadp-operator/pull/2338) — openshift/oadp-operator
- [#158 Remove inactive users from DOWNSTREAM_OWNERS](https://github.com/openshift/velero-plugin-for-aws/pull/158) — openshift/velero-plugin-for-aws
- [#2337 update TROUBLESHOOTING.md to use oc oadp CLI instead of velero pod -exec alias](https://github.com/openshift/oadp-operator/pull/2337) — openshift/oadp-operator
- [#2331 docs: fix links, restic refs, and typos in examples and root-level docs](https://github.com/openshift/oadp-operator/pull/2331) — openshift/oadp-operator
- [#455 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.4 (b4148a4) into oadp-1.4](https://github.com/openshift/openshift-velero-plugin/pull/455) — openshift/openshift-velero-plugin
- [#2334 docs: fix broken links, stale paths, and typos across root and developer docs](https://github.com/openshift/oadp-operator/pull/2334) — openshift/oadp-operator
- [#2336 docs: remove entirely obsolete documentation files](https://github.com/openshift/oadp-operator/pull/2336) — openshift/oadp-operator
- [#2335 docs: fix restic→kopia, field names, and plugin refs in config docs](https://github.com/openshift/oadp-operator/pull/2335) — openshift/oadp-operator
- [#2332 docs: move obsolete designs to docs/design/obsolete/ and update design docs](https://github.com/openshift/oadp-operator/pull/2332) — openshift/oadp-operator
- [#2333 docs: add deprecation banners to obsolete VSM/ODF blog posts](https://github.com/openshift/oadp-operator/pull/2333) — openshift/oadp-operator
- [#157 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.4)](https://github.com/openshift/velero-plugin-for-gcp/pull/157) — openshift/velero-plugin-for-gcp
- [#156 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.3)](https://github.com/openshift/velero-plugin-for-gcp/pull/156) — openshift/velero-plugin-for-gcp
- [#158 Fix ObjectExists to handle wrapped storage.ErrObjectNotExist errors (oadp-1.5)](https://github.com/openshift/velero-plugin-for-gcp/pull/158) — openshift/velero-plugin-for-gcp
- [#556 Fix CI workflows: MinIO image, Go version, linter action, and typos](https://github.com/openshift/velero/pull/556) — openshift/velero
- [#2325 [oadp-1.4] OADP-8486: Added startup probe](https://github.com/openshift/oadp-operator/pull/2325) — openshift/oadp-operator

**migtools** (31)
- [#372 ⬆ Bump hadolint/hadolint-action from 3.1.0 to 3.4.0](https://github.com/migtools/oadp-non-admin/pull/372) — migtools/oadp-non-admin
- [#161 [oadp-1.6] feat: add bound-sa-token projected volume to datamover pod for STS auth](https://github.com/migtools/kubevirt-datamover-controller/pull/161) — migtools/kubevirt-datamover-controller
- [#31 chore(deps): bump dompurify from 3.4.4 to 3.4.12 in /frontend](https://github.com/migtools/filebrowser/pull/31) — migtools/filebrowser
- [#158 feat: add bound-sa-token projected volume to datamover pod for STS auth](https://github.com/migtools/kubevirt-datamover-controller/pull/158) — migtools/kubevirt-datamover-controller
- [#138 build(deps): bump github.com/google/cel-go from 0.26.0 to 0.29.0](https://github.com/migtools/kubevirt-datamover-controller/pull/138) — migtools/kubevirt-datamover-controller
- [#238 Bump google.golang.org/grpc from 1.77.0 to 1.82.1](https://github.com/migtools/oadp-cli/pull/238) — migtools/oadp-cli
- [#255 Remove dead oadp-operator replace directive](https://github.com/migtools/oadp-cli/pull/255) — migtools/oadp-cli
- [#242 Merge https://github.com/migtools/oadp-cli:oadp-1.4 (2c406b4) into oadp-1.4](https://github.com/migtools/oadp-cli/pull/242) — migtools/oadp-cli
- [#156 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-controller/pull/156) — migtools/kubevirt-datamover-controller
- [#247 [oadp-1.4] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/247) — migtools/oadp-cli
- [#245 [oadp-1.6] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/245) — migtools/oadp-cli
- [#246 [oadp-1.5] OADP-8508: Fix schedule create examples showing velero instead of oc oadp](https://github.com/migtools/oadp-cli/pull/246) — migtools/oadp-cli
- [#34 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vmdp/pull/34) — migtools/oadp-vmdp
- [#32 Remove inactive users from OWNERS](https://github.com/migtools/filebrowser/pull/32) — migtools/filebrowser
- [#33 Remove inactive users from OWNERS](https://github.com/migtools/filebrowser/pull/33) — migtools/filebrowser
- [#249 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/249) — migtools/oadp-cli
- [#97 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vm-file-restore/pull/97) — migtools/oadp-vm-file-restore
- [#35 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vmdp/pull/35) — migtools/oadp-vmdp
- [#370 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/370) — migtools/oadp-non-admin
- [#46 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/46) — migtools/kopia
- [#250 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/250) — migtools/oadp-cli
- [#248 Remove inactive users from OWNERS](https://github.com/migtools/oadp-cli/pull/248) — migtools/oadp-cli
- [#96 Remove inactive users from OWNERS](https://github.com/migtools/oadp-vm-file-restore/pull/96) — migtools/oadp-vm-file-restore
- [#39 Remove inactive users from OWNERS](https://github.com/migtools/kubevirt-datamover-plugin/pull/39) — migtools/kubevirt-datamover-plugin
- [#369 Remove inactive users from OWNERS](https://github.com/migtools/oadp-non-admin/pull/369) — migtools/oadp-non-admin
- [#45 Remove inactive users from OWNERS](https://github.com/migtools/kopia/pull/45) — migtools/kopia
- [#180 Remove inactive users from OWNERS](https://github.com/migtools/udistribution/pull/180) — migtools/udistribution
- [#151 [oadp-1.6] ci: fix lint for golangci-lint v2](https://github.com/migtools/kubevirt-datamover-controller/pull/151) — migtools/kubevirt-datamover-controller
- [#150 [oadp-1.6] Issue #26: Azure BSL support](https://github.com/migtools/kubevirt-datamover-controller/pull/150) — migtools/kubevirt-datamover-controller
- [#239 Backport must gather image 1.6](https://github.com/migtools/oadp-cli/pull/239) — migtools/oadp-cli
- [#148 [oadp-1.6] feat: implement downloader runtime for VM restore (issue #73 Phase 2)](https://github.com/migtools/kubevirt-datamover-controller/pull/148) — migtools/kubevirt-datamover-controller

**Other** (5)
- [#168 [ImgBot] Optimize images](https://github.com/kaovilai/kaovilai.pw/pull/168) — kaovilai/kaovilai.pw
- [#175 Bump actions to latest and apply blocked Dependabot updates (vite 8, TypeScript 6) with config fixes](https://github.com/kaovilai/kaovilai.pw/pull/175) — kaovilai/kaovilai.pw
- [#3 Add design docs for one-click community rule install via marketplace deep links](https://github.com/kaovilai/redirector/pull/3) — kaovilai/redirector
- [#70 Sync activity log update schedule with PR badges workflow](https://github.com/kaovilai/kaovilai/pull/70) — kaovilai/kaovilai
- [#68 Emit JSON exports (open-prs.json, activity.json) alongside markdown reports](https://github.com/kaovilai/kaovilai/pull/68) — kaovilai/kaovilai
## Issues/PRs Commented On (42)

**velero-io** (16)
- [#10120 Enhancement: Fail-fast in `velero install --wait` on Deployment ReplicaFailure](https://github.com/velero-io/velero/issues/10120) — velero-io/velero
- [#10026 Restore logs endless watch errors for API groups without watch support (e.g. authorization.openshift.io)](https://github.com/velero-io/velero/issues/10026) — velero-io/velero
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#8686 Avoid overwriting during backup to support object lock enabled buckets](https://github.com/velero-io/velero/issues/8686) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#3194 Have the Velero CLI use the active namespace in the current context](https://github.com/velero-io/velero/issues/3194) — velero-io/velero
- [#9965 Add safe auto-merge workflow for high-confidence Dependabot PRs](https://github.com/velero-io/velero/issues/9965) — velero-io/velero
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#8466 Velero doesnt do well with Minio bucket versioning ](https://github.com/velero-io/velero/issues/8466) — velero-io/velero
- [#9957 `VolumeSnapshotContent` resources are forcefully restored, ignoring `includedResources` and `excludedResources` filters](https://github.com/velero-io/velero/issues/9957) — velero-io/velero
- [#10092 Deprecate the block volume backup/restore functionality through Kopia file system uploader](https://github.com/velero-io/velero/issues/10092) — velero-io/velero
- [#9600 Deprecation: Remove `BackupStorageLocation.Spec.ObjectStorage.CACert` inline field in favor of `CACertRef` secret reference](https://github.com/velero-io/velero/issues/9600) — velero-io/velero
- [#10078 CI to check doc compliance with code change](https://github.com/velero-io/velero/issues/10078) — velero-io/velero
- [#9093 Publish releases to winget-pkgs](https://github.com/velero-io/velero/issues/9093) — velero-io/velero
- [#8807 Support per-storageclass VSClass annotation](https://github.com/velero-io/velero/issues/8807) — velero-io/velero

**openshift** (3)
- [#1832 e2e jobs for other repos](https://github.com/openshift/oadp-operator/issues/1832) — openshift/oadp-operator
- [#2343 Investigate making plugin repo changes immediately available for OADP-operator e2e tests](https://github.com/openshift/oadp-operator/issues/2343) — openshift/oadp-operator
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero

**migtools** (12)
- [#155 DataUpload/DataDownload controllers never populate Status.StartTimestamp, CompletionTimestamp, or Progress](https://github.com/migtools/kubevirt-datamover-controller/issues/155) — migtools/kubevirt-datamover-controller
- [#154 Failed datamover operations leave scratch/temp PVCs and pods behind indefinitely, with unbounded pod-log emission](https://github.com/migtools/kubevirt-datamover-controller/issues/154) — migtools/kubevirt-datamover-controller
- [#153 rebindPVToNamespace cannot recover if source PVC is deleted but the rebind didn't finish (crash mid-flow)](https://github.com/migtools/kubevirt-datamover-controller/issues/153) — migtools/kubevirt-datamover-controller
- [#152 No operational signal for PVs left in Retain policy after a completed upload/download rebind](https://github.com/migtools/kubevirt-datamover-controller/issues/152) — migtools/kubevirt-datamover-controller
- [#123 DataUpload/DataDownload controllers treat all dependency-lookup errors as terminal Failed](https://github.com/migtools/kubevirt-datamover-controller/issues/123) — migtools/kubevirt-datamover-controller
- [#122 GenerateName + cached-client lookups risk false "not found" or duplicate child pod/PVC creation](https://github.com/migtools/kubevirt-datamover-controller/issues/122) — migtools/kubevirt-datamover-controller
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller
- [#120 Cancellation cleanup errors are logged but not propagated, phase moves to Canceled regardless](https://github.com/migtools/kubevirt-datamover-controller/issues/120) — migtools/kubevirt-datamover-controller
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#160 Checkpoint index records requested PVC size, not actual PV capacity, undersizing restore scratch space](https://github.com/migtools/kubevirt-datamover-controller/issues/160) — migtools/kubevirt-datamover-controller
- [#74 Force full backup when BSL checkpoint validation fails](https://github.com/migtools/kubevirt-datamover-controller/issues/74) — migtools/kubevirt-datamover-controller
- [#73 Implement DataDownload controller for VM restore](https://github.com/migtools/kubevirt-datamover-controller/issues/73) — migtools/kubevirt-datamover-controller

**Other** (11)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#1997 [CNCF LFX Proposal] Velero CSI E2E Testing](https://github.com/cncf/mentoring/issues/1997) — cncf/mentoring
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#132 Dynamic Prow Plugin Detection per Repo](https://github.com/kaovilai/github-bot-command-palette/issues/132) — kaovilai/github-bot-command-palette
- [#736 Tide status controller falsely reports "In merge pool." for PRs blocked by a never-triggered required context](https://github.com/kubernetes-sigs/prow/issues/736) — kubernetes-sigs/prow
- [#110 [improve] Performance: add Vite manual chunk splitting for better browser caching](https://github.com/kaovilai/kaovilai.pw/issues/110) — kaovilai/kaovilai.pw
- [#255 Advertise if a Storage Solution requires Long-Term Retention of Snapshots](https://github.com/kubernetes-csi/external-snapshot-metadata/issues/255) — kubernetes-csi/external-snapshot-metadata
- [#4564 Upgrade AWS SDK to /v2](https://github.com/distribution/distribution/issues/4564) — distribution/distribution
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
- [#121 [FEATURE] Matrix Strategy Multi-Arch example](https://github.com/redhat-actions/buildah-build/issues/121) — redhat-actions/buildah-build
- [#330 Omit  ANTHROPIC_MODEL: sonnetModel ?? opusModel, from claude-code so selected model option sticks](https://github.com/caozhiyuan/copilot-api/issues/330) — caozhiyuan/copilot-api
## Issues Closed (30)

**velero-io** (9)
- [#10044 Azure Files SMB / Blobfuse / gcsfuse: restore silently loses file ownership — chown/chmod fake success, no error exists to surface](https://github.com/velero-io/velero/issues/10044) — velero-io/velero
- [#10099 Update velero.io community pages](https://github.com/velero-io/velero/issues/10099) — velero-io/velero
- [#9719 Velero Server Default Restore Resource Modifier](https://github.com/velero-io/velero/issues/9719) — velero-io/velero
- [#10022 Flaky unit test:  TestBlockUploaderBackup/success_full_backup](https://github.com/velero-io/velero/issues/10022) — velero-io/velero
- [#10042 Add `.github` repo](https://github.com/velero-io/velero/issues/10042) — velero-io/velero
- [#10050 nits for fine-grained filter docs](https://github.com/velero-io/velero/issues/10050) — velero-io/velero
- [#10023 Ginkgo CLI Version Mismatch GoMod Import](https://github.com/velero-io/velero/issues/10023) — velero-io/velero
- [#10029 Flaky test: TestKopiaObjectWriterEx_ConcurrentAsyncErrors can observe async error before all writes are queued](https://github.com/velero-io/velero/issues/10029) — velero-io/velero
- [#10048 CI: make Bitnami MinIO Dockerfile SHA lookup resilient to API/rate-limit failures](https://github.com/velero-io/velero/issues/10048) — velero-io/velero

**openshift** (6)
- [#2236 Flaky E2E: DPA reconciliation race condition causes NoDefaultBackupLocation test failure](https://github.com/openshift/oadp-operator/issues/2236) — openshift/oadp-operator
- [#2351 kubevirt-datamover ClusterRole missing RBAC for Phase 3 (DataDownload) support](https://github.com/openshift/oadp-operator/issues/2351) — openshift/oadp-operator
- [#149 Gather PVC/PV/Namespace(SCC) data for backed-up/restored app namespaces to diagnose restore permission/ownership bugs](https://github.com/openshift/oadp-must-gather/issues/149) — openshift/oadp-must-gather
- [#5328 src-bundle build flake: no node selector lets buildah pod land on arm64 node, fails pulling amd64-only pipeline:src manifest list](https://github.com/openshift/ci-tools/issues/5328) — openshift/ci-tools
- [#363 Remove CODEGEN_VERSION from Makefile.prow](https://github.com/openshift/velero/issues/363) — openshift/velero
- [#443 OADP-7384: ImageStream backup fails with `manifest unknown` when a status tag item references another namespace's repository and that reference is stale](https://github.com/openshift/openshift-velero-plugin/issues/443) — openshift/openshift-velero-plugin

**migtools** (4)
- [#162 Narrow retry/crash races: non-idempotent scratch PVC/pod creation, and an unresumable orphaned PV after a mid-rebind crash](https://github.com/migtools/kubevirt-datamover-controller/issues/162) — migtools/kubevirt-datamover-controller
- [#160 Checkpoint index records requested PVC size, not actual PV capacity, undersizing restore scratch space](https://github.com/migtools/kubevirt-datamover-controller/issues/160) — migtools/kubevirt-datamover-controller
- [#118 lint workflow is using node20](https://github.com/migtools/kubevirt-datamover-controller/issues/118) — migtools/kubevirt-datamover-controller
- [#108 evaluateVMBackupStatus misses real VMBackup failures due to exact-match on Progressing.Reason=="Failed"](https://github.com/migtools/kubevirt-datamover-controller/issues/108) — migtools/kubevirt-datamover-controller

**Other** (11)
- [#147 group dependabot prs into ecosystems.. ie typescript, actions, etc.](https://github.com/kaovilai/github-bot-command-palette/issues/147) — kaovilai/github-bot-command-palette
- [#69 activity.json is not updated the same time as .md files.](https://github.com/kaovilai/kaovilai/issues/69) — kaovilai/kaovilai
- [#673 Tide gets stuck retrying unmergeable PR instead of advancing to next candidate](https://github.com/kubernetes-sigs/prow/issues/673) — kubernetes-sigs/prow
- [#1 Implement my gemini app into github pages static](https://github.com/kaovilai/route-127-trailer-nc/issues/1) — kaovilai/route-127-trailer-nc
- [#146 https://legacy.kaovilai.pw/pay-me this section has thai qr code payment info. add it to here](https://github.com/kaovilai/kaovilai.pw/issues/146) — kaovilai/kaovilai.pw
- [#67 Add JSON export alongside MY_ACTIVITY.md / MY_PULL_REQUESTS.md for site consumption](https://github.com/kaovilai/kaovilai/issues/67) — kaovilai/kaovilai
- [#74 gh aw compile isn't available in this environment prevent use gh aw install action](https://github.com/kaovilai/kaovilai.pw/issues/74) — kaovilai/kaovilai.pw
- [#1492 Move CRD installs out of Reconcile](https://github.com/stolostron/multiclusterhub-operator/issues/1492) — stolostron/multiclusterhub-operator
- [#8 [FEATURE] Support Vertex AI via ADC credentials](https://github.com/ferrumclaudepilgrim/claude-code-android/issues/8) — ferrumclaudepilgrim/claude-code-android
- [#121 [FEATURE] Matrix Strategy Multi-Arch example](https://github.com/redhat-actions/buildah-build/issues/121) — redhat-actions/buildah-build
- [#330 Omit  ANTHROPIC_MODEL: sonnetModel ?? opusModel, from claude-code so selected model option sticks](https://github.com/caozhiyuan/copilot-api/issues/330) — caozhiyuan/copilot-api
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
