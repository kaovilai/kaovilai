# Activity Log

> **Period:** 2026-09-11 — 2026-09-25
> **Generated:** 2026-09-25 11:33:49 UTC

| Metric | Count |
|--------|-------|
| PRs Merged | 19 |
| PRs Opened | 19 |
| PRs Reviewed | 41 |
| Issues/PRs Commented | 32 |
| Issues Closed | 8 |

---

## PRs Merged (19)

**velero-io** (7)
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero
- [#9646 Fix backup-finalizer: do not set backup phase to Completed before PutBackupMetadata succeeds](https://github.com/velero-io/velero/pull/9646) — velero-io/velero
- [#10275 Implement namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10275) — velero-io/velero
- [#9221 docs: Document --write-sparse-files flag for disk space issues during restore](https://github.com/velero-io/velero/pull/9221) — velero-io/velero
- [#9772 Design: namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/9772) — velero-io/velero
- [#10027 Add set-based label selector test and docs coverage for restore](https://github.com/velero-io/velero/pull/10027) — velero-io/velero
- [#9575 Add configurable tolerations for PodVolumeBackup and data mover pods](https://github.com/velero-io/velero/pull/9575) — velero-io/velero

**openshift** (6)
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator
- [#2453 OADP-6065: auto-detect AWS region for CloudStorage-backed BSLs](https://github.com/openshift/oadp-operator/pull/2453) — openshift/oadp-operator
- [#2452 OADP-7984: fix(nodeagent): propagate PodConfig.PriorityClassName to node-agent ConfigMap](https://github.com/openshift/oadp-operator/pull/2452) — openshift/oadp-operator
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release
- [#449 Detect SCC UID/GID-range mismatch on namespace restore](https://github.com/openshift/openshift-velero-plugin/pull/449) — openshift/openshift-velero-plugin

**migtools** (1)
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore

**Other** (5)
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
- [#1 Bring vendor/amazon/maverick blobs in sync with the lineage-20 device tree manifest](https://github.com/kaovilai/android_vendor_amazon_maverick/pull/1) — kaovilai/android_vendor_amazon_maverick
- [#7 Add safe Dependabot auto-merge workflow for npm patch/minor updates](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/7) — kaovilai/bandwidth-hero-proxy2
- [#14 Fix healthcheck: use 127.0.0.1 instead of localhost](https://github.com/kaovilai/copilot-api/pull/14) — kaovilai/copilot-api
- [#13 Lower ambiguous-timeout budget to 80s to beat client watchdogs](https://github.com/kaovilai/copilot-api/pull/13) — kaovilai/copilot-api
## PRs Opened (19)

**velero-io** (3)
- [#10565 Add e2e test for namespace selection by label in resource policy](https://github.com/velero-io/velero/pull/10565) — velero-io/velero
- [#10555 Fix e2e-test-kind and changelog-check CI flakes](https://github.com/velero-io/velero/pull/10555) — velero-io/velero
- [#10534 Add changelog-bot workflow to add changelogs via /changelog comment](https://github.com/velero-io/velero/pull/10534) — velero-io/velero

**openshift** (5)
- [#2454 OADP-8056: create Secret from inline CACert and use CACertRef for BSL cert rotation](https://github.com/openshift/oadp-operator/pull/2454) — openshift/oadp-operator
- [#2453 OADP-6065: auto-detect AWS region for CloudStorage-backed BSLs](https://github.com/openshift/oadp-operator/pull/2453) — openshift/oadp-operator
- [#2452 OADP-7984: fix(nodeagent): propagate PodConfig.PriorityClassName to node-agent ConfigMap](https://github.com/openshift/oadp-operator/pull/2452) — openshift/oadp-operator
- [#2450 fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2450) — openshift/oadp-operator
- [#85460 oadp/operator-sdk-bundle-image: retry oc calls around MCP rollout DNS flake](https://github.com/openshift/release/pull/85460) — openshift/release

**migtools** (2)
- [#108 [oadp-1.6] Fix MinIO create-bucket Job timeout by switching mc image to quay.io (cherry-pick #107)](https://github.com/migtools/oadp-vm-file-restore/pull/108) — migtools/oadp-vm-file-restore
- [#107 Fix MinIO create-bucket Job timeout by switching mc image to quay.io](https://github.com/migtools/oadp-vm-file-restore/pull/107) — migtools/oadp-vm-file-restore

**Other** (9)
- [#121974 feat(browser): recognize Comet (Perplexity) for real-profile browsing](https://github.com/NousResearch/hermes-agent/pull/121974) — NousResearch/hermes-agent
- [#197 fix(cve-scan): run go mod vendor for vendored downstream repos](https://github.com/oadp-rebasebot/oadp-rebase/pull/197) — oadp-rebasebot/oadp-rebase
- [#4 Throwaway: trigger fork CI](https://github.com/kaovilai/cliprelay/pull/4) — kaovilai/cliprelay
- [#116 OtpExtractor: support alphanumeric OTP codes](https://github.com/geekflyer/cliprelay/pull/116) — geekflyer/cliprelay
- [#3 WIP: OTP extractor pattern fixes (Copilot workspace — do not merge)](https://github.com/kaovilai/cliprelay/pull/3) — kaovilai/cliprelay
- [#1 Bring vendor/amazon/maverick blobs in sync with the lineage-20 device tree manifest](https://github.com/kaovilai/android_vendor_amazon_maverick/pull/1) — kaovilai/android_vendor_amazon_maverick
- [#7 Add safe Dependabot auto-merge workflow for npm patch/minor updates](https://github.com/kaovilai/bandwidth-hero-proxy2/pull/7) — kaovilai/bandwidth-hero-proxy2
- [#14 Fix healthcheck: use 127.0.0.1 instead of localhost](https://github.com/kaovilai/copilot-api/pull/14) — kaovilai/copilot-api
- [#13 Lower ambiguous-timeout budget to 80s to beat client watchdogs](https://github.com/kaovilai/copilot-api/pull/13) — kaovilai/copilot-api
## PRs Reviewed (41)

**velero-io** (10)
- [#10579 Change hashing algorithm to HMAC-SHA256-128 for kopia repo](https://github.com/velero-io/velero/pull/10579) — velero-io/velero
- [#10572 Add architecture entry point and roadmap change process](https://github.com/velero-io/velero/pull/10572) — velero-io/velero
- [#10580 docs: fix --use-volume-snapshots=false in Tencent Cloud guide](https://github.com/velero-io/velero/pull/10580) — velero-io/velero
- [#10568 Document maintainer contact info and shared responsibility](https://github.com/velero-io/velero/pull/10568) — velero-io/velero
- [#10539 [Backport release-1.18] Fix backup queue permanently stuck when a dequeued backup completes during the patch](https://github.com/velero-io/velero/pull/10539) — velero-io/velero
- [#10537 Add doc for block data mover](https://github.com/velero-io/velero/pull/10537) — velero-io/velero
- [#10530 Identify the backed-up volume by CSI volume handle in the in-place restore pre-flight check](https://github.com/velero-io/velero/pull/10530) — velero-io/velero
- [#10526 Fix schedule create dropping backup type](https://github.com/velero-io/velero/pull/10526) — velero-io/velero
- [#10524 test: use the Kind constant instead of the string literal](https://github.com/velero-io/velero/pull/10524) — velero-io/velero
- [#10523 Let uploader to control fallback centrally](https://github.com/velero-io/velero/pull/10523) — velero-io/velero

**openshift** (16)
- [#582 Remove bz-pr-action GitHub Actions workflow](https://github.com/openshift/velero/pull/582) — openshift/velero
- [#480 Merge https://github.com/openshift/openshift-velero-plugin:oadp-1.6 (4ae9c74) into oadp-1.6](https://github.com/openshift/openshift-velero-plugin/pull/480) — openshift/openshift-velero-plugin
- [#2466 [oadp-1.4] OADP-8835: feat(bsl): concatenate all CA certificates from BSLs and include system defaults](https://github.com/openshift/oadp-operator/pull/2466) — openshift/oadp-operator
- [#99 Remove obsolete bz-on-pr-create workflow](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/99) — openshift/velero-plugin-for-legacy-aws
- [#110 Remove obsolete bz-on-pr-create workflow](https://github.com/openshift/velero-plugin-for-legacy-aws/pull/110) — openshift/velero-plugin-for-legacy-aws
- [#2457 [oadp-1.6] Grant VMFR controller PVC delete permission](https://github.com/openshift/oadp-operator/pull/2457) — openshift/oadp-operator
- [#578 Pin Bitnami MinIO source for kind E2E tests](https://github.com/openshift/velero/pull/578) — openshift/velero
- [#313 Merge https://github.com/openshift/hypershift-oadp-plugin:oadp-1.6 (d81e9e5) into oadp-1.6](https://github.com/openshift/hypershift-oadp-plugin/pull/313) — openshift/hypershift-oadp-plugin
- [#2455 [oadp-1.6] fix(virt-kdm-e2e): retry known transient flakes in guest-exec/checksum paths](https://github.com/openshift/oadp-operator/pull/2455) — openshift/oadp-operator
- [#2456 Grant VMFR controller PVC delete permission](https://github.com/openshift/oadp-operator/pull/2456) — openshift/oadp-operator
- [#85502 Update OADP builder images to ubi9-v1.26](https://github.com/openshift/release/pull/85502) — openshift/release
- [#85499 Update migtools/oadp-cli builder to ubi9-v1.26 for oadp-dev, oadp-1.5, oadp-1.6](https://github.com/openshift/release/pull/85499) — openshift/release
- [#474 Bump google.golang.org/grpc from 1.83.1 to 1.83.2](https://github.com/openshift/openshift-velero-plugin/pull/474) — openshift/openshift-velero-plugin
- [#2449 [oadp-1.6] chore(deps): migrate MinIO image registry from Docker Hub to Quay](https://github.com/openshift/oadp-operator/pull/2449) — openshift/oadp-operator
- [#2448 chore(deps): migrate MinIO image registry from Docker Hub to Quay](https://github.com/openshift/oadp-operator/pull/2448) — openshift/oadp-operator
- [#84954 Remove OADP rebasebot periodic jobs](https://github.com/openshift/release/pull/84954) — openshift/release

**migtools** (13)
- [#110 Merge https://github.com/migtools/oadp-vm-file-restore:oadp-1.6 (a725c94) into oadp-1.6](https://github.com/migtools/oadp-vm-file-restore/pull/110) — migtools/oadp-vm-file-restore
- [#241 Merge https://github.com/migtools/kubevirt-datamover-controller:oadp-1.6 (6a1a241) into oadp-1.6](https://github.com/migtools/kubevirt-datamover-controller/pull/241) — migtools/kubevirt-datamover-controller
- [#387 Merge https://github.com/migtools/oadp-non-admin:oadp-1.6 (24ca6dd) into oadp-1.6](https://github.com/migtools/oadp-non-admin/pull/387) — migtools/oadp-non-admin
- [#54 fix(gcs): use service-account credential options](https://github.com/migtools/kopia/pull/54) — migtools/kopia
- [#39 fix(gcs): use service-account credential options](https://github.com/migtools/oadp-vmdp/pull/39) — migtools/oadp-vmdp
- [#41 Merge https://github.com/filebrowser/filebrowser:v2.63.23 (e8a388f) into oadp-1.6](https://github.com/migtools/filebrowser/pull/41) — migtools/filebrowser
- [#43 [oadp-1.6] remove release job in filebrowser](https://github.com/migtools/filebrowser/pull/43) — migtools/filebrowser
- [#189 Bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/189) — migtools/udistribution
- [#236 Fix default max concurrent data movers](https://github.com/migtools/kubevirt-datamover-controller/pull/236) — migtools/kubevirt-datamover-controller
- [#105 [oadp-1.6] OADP-7467: Fix VMFR restore namespace access](https://github.com/migtools/oadp-vm-file-restore/pull/105) — migtools/oadp-vm-file-restore
- [#190 Bump go.opentelemetry.io/otel/sdk from 1.38.0 to 1.45.0](https://github.com/migtools/udistribution/pull/190) — migtools/udistribution
- [#235 Fix default max concurrent data movers](https://github.com/migtools/kubevirt-datamover-controller/pull/235) — migtools/kubevirt-datamover-controller
- [#62 update kubevirt-datamover-controller dependency and remove replace](https://github.com/migtools/kubevirt-datamover-plugin/pull/62) — migtools/kubevirt-datamover-plugin

**Other** (2)
- [#620 :sparkles: Restrict operand egress via NetworkPolicy](https://github.com/konveyor/operator/pull/620) — konveyor/operator
- [#192 update plugins to 1.14.3-rc.2](https://github.com/oadp-rebasebot/oadp-rebase/pull/192) — oadp-rebasebot/oadp-rebase
## Issues/PRs Commented On (32)

**velero-io** (21)
- [#10310 Include the errors/warnings from node-agent and data-mover pods in the velero backup/restore get/describe commands](https://github.com/velero-io/velero/issues/10310) — velero-io/velero
- [#7507 E2E: Add CSI snapshot tests to kind cluster](https://github.com/velero-io/velero/issues/7507) — velero-io/velero
- [#9476 Remove whitelist for tolerations of PodVolumeBackup Pod](https://github.com/velero-io/velero/issues/9476) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#9260 Add CRD version compatibility validation during server startup](https://github.com/velero-io/velero/issues/9260) — velero-io/velero
- [#9735 Velero should add a clear error when data mover pod is unschedulable due to affinity/topology mismatch](https://github.com/velero-io/velero/issues/9735) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
- [#10545 CRD schema check: make `warn` mode non-blocking and bound `strict` mode with a shared timeout](https://github.com/velero-io/velero/issues/10545) — velero-io/velero
- [#10544 CRD schema check: self-resolution for `strict` mode failures (`/readyz` instead of crash-loop)](https://github.com/velero-io/velero/issues/10544) — velero-io/velero
- [#9556 Block level backup/restore support](https://github.com/velero-io/velero/issues/9556) — velero-io/velero
- [#8707 Support multiple transmission protocols](https://github.com/velero-io/velero/issues/8707) — velero-io/velero
- [#10340 Bug: EphemeralContainers are missing from ServiceAccount token filtering in PodAction](https://github.com/velero-io/velero/issues/10340) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#2812 Restore fails with error "no space left on device" if PVCs are 100% utilised during backup](https://github.com/velero-io/velero/issues/2812) — velero-io/velero
- [#8279 backupRepository can become stale if velero deployment is not running to observe bsl update/create](https://github.com/velero-io/velero/issues/8279) — velero-io/velero
- [#10232 DownloadRequest reaches Processed with a signed URL for an object that does not exist](https://github.com/velero-io/velero/issues/10232) — velero-io/velero
- [#8263 Fatal: unable to open config file results in PartiallyFailed Backup](https://github.com/velero-io/velero/issues/8263) — velero-io/velero
- [#9318 Behavior of skip volume policy is strange/problematic](https://github.com/velero-io/velero/issues/9318) — velero-io/velero
- [#9453 DataUpload tasks stuck in Prepared phase for extended periods](https://github.com/velero-io/velero/issues/9453) — velero-io/velero
- [#9963 velero-plugin-for-aws >= 1.14.1 makes S3 region mandatory](https://github.com/velero-io/velero/issues/9963) — velero-io/velero
- [#3218 S3 client-side encryption support](https://github.com/velero-io/velero/issues/3218) — velero-io/velero

**openshift** (2)
- [#597 Testing Operators Built With The Operator SDK and Deployed Through OLM](https://github.com/openshift/ci-docs/issues/597) — openshift/ci-docs
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator

**migtools** (2)
- [#99 Add OADP e2e test coverage for kubevirt-datamover](https://github.com/migtools/kubevirt-datamover-controller/issues/99) — migtools/kubevirt-datamover-controller
- [#14 Handle guest agent connectivity and SkipQuiesce for VirtualMachineBackup](https://github.com/migtools/kubevirt-datamover-controller/issues/14) — migtools/kubevirt-datamover-controller

**Other** (7)
- [#39 Tracking Out of Date Golang Versions](https://github.com/redhat-best-practices-for-k8s/telco-bot/issues/39) — redhat-best-practices-for-k8s/telco-bot
- [#12543 Issue can land permanently blocked on a "recovery owner"/disposition state when the run that created it terminates](https://github.com/paperclipai/paperclip/issues/12543) — paperclipai/paperclip
- [#181212 Home Assistant 2026.9.0 – “Could not load Home Assistant” after update](https://github.com/home-assistant/core/issues/181212) — home-assistant/core
- [#18963 VEP #25: Infer backup target StorageClass from source VM volumes](https://github.com/kubevirt/kubevirt/issues/18963) — kubevirt/kubevirt
- [#2 OtpExtractor: support alphanumeric OTP codes](https://github.com/kaovilai/cliprelay/issues/2) — kaovilai/cliprelay
- [#2525 `pull_request_review_write` combines create/submit/delete into one tool, making fine-grained permissions by method impossible](https://github.com/github/github-mcp-server/issues/2525) — github/github-mcp-server
- [#36873 Bug: AI Assistant "Connect a model" fails with "The service returned an unexpected response" on custom OpenAI-compatible Base URLs](https://github.com/n8n-io/n8n/issues/36873) — n8n-io/n8n
## Issues Closed (8)

**velero-io** (6)
- [#10564 E2E test coverage for namespace selection by label in resource policy](https://github.com/velero-io/velero/issues/10564) — velero-io/velero
- [#9645 backup-finalizer: do not set backup phase to Completed in-memory before PutBackupMetadata succeeds](https://github.com/velero-io/velero/issues/9645) — velero-io/velero
- [#7492 ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/7492) — velero-io/velero
- [#10545 CRD schema check: make `warn` mode non-blocking and bound `strict` mode with a shared timeout](https://github.com/velero-io/velero/issues/10545) — velero-io/velero
- [#8363 VolumePolicies filter volumes to snapshot by volume name](https://github.com/velero-io/velero/issues/8363) — velero-io/velero
- [#9771 Design: ResourcePolicy-based namespace selection by label](https://github.com/velero-io/velero/issues/9771) — velero-io/velero

**openshift** (2)
- [#448 Feature request: detect/reconcile SCC UID/GID-range mismatch on Namespace restore](https://github.com/openshift/openshift-velero-plugin/issues/448) — openshift/openshift-velero-plugin
- [#2386 Expose kubevirt-datamover-controller --max-concurrent-data-movers via DPA CRD](https://github.com/openshift/oadp-operator/issues/2386) — openshift/oadp-operator
---

*This report is automatically generated by GitHub Actions on the same schedule as the PR badges update.*
