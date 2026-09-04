# Consumer conformance refs（provider-free）

本文件只登记跨仓库 immutable evidence refs 与安全摘要；不保存 Prompt payload、媒体 bytes、provider 运行记录或 owner 私有状态。四个消费 Owner 的实现 change 均已在其仓库归档并提交，以下 ref 指向已提交（immutable）的归档 change 记录与其记录的 verification 证据。

当前统一证据等级：`semantic_alignment_only`。在各 Owner 完成当前 exact template/contract/document/source digest 的解析与领域 schema 验证前，不得提升为 `exact_template_conformance`。

边界声明：

- 这些 conformance 证明的是各 Owner 侧 film 工作流合同（handoff/场景晋级/资产投影/音频 readiness）在 provider-free fixture 下的行为，与本 solution 对应 role 的语义对齐；它们不宣称已按本 solution 当前 template digest 逐 fixture 执行。
- `temp/integration-test-runs/<run-id>/` 按项目 evidence 政策属于 owner-local、不入库、可清理；本仓只引用归档 change 文档中已提交的 run 记录与结论（`provider_called=false` 等），不依赖临时目录继续存在。
- dependency release gate 保持 fail-closed：在 Registry 提供依赖 solution 的 immutable release/snapshot receipt 前，消费方必须返回 `DEPENDENCY_RELEASE_UNAVAILABLE`（见 `docs/production-contract.zh-CN.md`）。
- 本地 closeout 不需要任何 provider 调用。

## Auctra（project-intent / failure-restructure 语义对齐）

- Evidence level：`semantic_alignment_only`。
- Ref：`cli/auctra` 归档 change `2026-08-31-auctra-film-production-intent-handoff-v1`（提交 `a62226d`）。
- 安全摘要：`auctra.production_intent_handoff.v1` 覆盖四 profile、两种 entry mode、stale source、missing dramatic function、brand short structure 与 overlay compatibility 的 fixture/component evidence；redacted evidence 位于 owner-local `temp/integration-test-runs/<run-id>/`；final gates 为 `task check` 与 `openspec validate --all --strict`。

## Scaena（scene-package / shot-prompt / continuity-review 语义对齐）

- Evidence level：`semantic_alignment_only`。
- Ref：`agent/scaena` 归档 change `2026-09-01-scaena-film-scene-promotion-continuity-v1`（提交 `d3f4cd0`）。
- 安全摘要：offline process e2e（`TestFilmScenePromotionOfflineProcessE2E`）覆盖 prototype package、production successor、人工晋级、连续性检查、final master verification、delivery receipt、stale expected version 与 blocked audio master；归档 verification 记录 run `temp/integration-test-runs/20260831-095619.319177895-system-1208182-1/summary.json`；fixture 不调用真实 provider，artifact 只记录 refs、状态与脱敏结果。

## Eikona（asset-dependency 语义对齐）

- Evidence level：`semantic_alignment_only`。
- Ref：`cli/eikona` 归档 change `2026-09-01-eikona-film-asset-profile-projection-v1`（提交 `d4c57dc`）。
- 安全摘要：provider-free 四 profile 与 dependency-failure 场景 run `temp/integration-test-runs/integration-20260831T060533.579285489Z/summary.json`，归档记录 `provider_called=false`、`run_count=0`；fixture 覆盖 DAG、missing dependency、hairstyle variant revalidation、inherit/forbid 与四 profile evidence axes。

## Sonora（shot-audio-intent 语义对齐）

- Evidence level：`semantic_alignment_only`。
- Ref：`cli/sonora` 归档 change `2026-08-31-sonora-film-audio-readiness-v1`（提交 `ea4beba`）。
- 安全摘要：fixture 场景覆盖 native segment 全留、单段替换、全拒绝、timeline stale、rights blocked、speaker mismatch 与 noise/room-tone failure；provider/network disabled；standard evidence bundle 由 `task test:integration` / `task test:e2e` 生成；ShotAudioIntent freeze、segment provenance、replacement 与 owner boundary 在协议文档中显式声明。

## 登记规则

- 只有已提交的归档 change 记录与其内嵌 verification 结论可作为 immutable ref；新增 owner 证据须先在 owner 仓归档，再在本表登记 repo、change id 与提交 hash。
- 本表不登记 digest 之外的任何 payload；owner 仓 evidence 目录清理不影响本表有效性。
