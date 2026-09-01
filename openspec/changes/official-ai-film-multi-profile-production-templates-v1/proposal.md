## Why

官方内容库已经有角色资产和分镜拆解 solution，但尚未覆盖“剧作意图→场景闭包→镜头 Prompt→声音意图→连续性质检→失败重构”的完整电影生产编译。缺少统一模板时，各 owner 会重复写长 Prompt、混入自身不拥有的字段，并把模型输出误当成 canonical revision。

## What Changes

- 新增官方中文优先 solution `video/ai-film-multi-profile-production`（最终稳定 ID 由 Registry authoring flow 确认）。
- 使用一个 solution + required `profile_id` 支持 `cinematic_live_action`、`motion_comic`、`stylized_animation` 和 `brand_film`，不创建四套独立 catalog/state。
- 提供六个主角色模板：project intent、asset dependency、scene package、shot prompt、continuity review、failure restructure；另提供 ShotAudioIntent 辅助模块。
- 通过 exact `promptrepo://` dependency refs 复用官方角色资产和分镜拆解 solution，不复制其正文或 schema。
- 固定 Prompt layering、reference inheritance、positive continuity locks、observable performance、single-variable reroll 和 bounded repair 规则。
- 模型只输出 semantic proposal/findings，不输出 owner refs、digest、accepted、budget receipt、provider payload 或最终 delivery verdict。
- 提供四 profile 的 valid/invalid fixture matrix、中文 source、英文 reviewed 适配、rights 与 maturity 计划。

## Capabilities

### New Capabilities

- `official-ai-film-multi-profile-production-templates`: 四 profile 共用的端到端 AI 电影 Prompt 解决方案包与 conformance 内容。

### Modified Capabilities

无。现有角色资产和 storyboard breakdown solution 保持独立、可版本固定。

## Impact

- 内容路径：计划新增 `solutions/video/ai-film-multi-profile-production/`，所有 machine metadata 由 Template Registry CLI/application service 生成。
- Consumer：Auctra、Scaena、Eikona、Sonora；各自拥有 typed input/output validator、execution、review 和 acceptance。
- Public ref/DTO：`shared/promptrepo`；catalog/release：`backend-server/template-registry`。
- 根级依赖：`openspec/changes/ai-film-federated-production-workbench-v1/`。
