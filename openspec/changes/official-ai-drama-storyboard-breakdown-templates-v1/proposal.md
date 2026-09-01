## Why

Scaena 现有分镜 Skill 与 owner request 只有 `instruction_profile_ref/version`，没有一个中文优先、可固定版本、可离线检查的官方模型提示方案。更关键的是，旧 owner delivery 要求模型直接生成 UTF-8 byte offsets、line numbers、durable refs、digests 和 timestamps，这些应由 Scaena deterministic compiler 负责，不应写进 Prompt。

本变更新增一个官方 AI 短剧分镜拆解 solution：模型只依据 Scaena 提供的 segment IDs 和文本产生 semantic storyboard plan；Scaena 用固定 input/output contract 执行，Skill 只选择 scenario profile 和触发公开命令。

## Owner Fit

- **Admission：`fit`（content）。** 本仓库拥有 Prompt 正文、examples、taxonomy、locale、rights、maturity 和 content fixtures。
- `promptrepo://` URI、inspect/render DTO 属于 `shared/promptrepo`；catalog/release metadata 属于 Template Registry；provider execution、成本、candidate 和 review 属于 Scaena。
- 本 change 不执行模型、不持久化用户剧本、不创建领域状态。

## What Changes

- 新增 `video/ai-drama-storyboard-breakdown` solution，`zh-CN` 为 source locale，`en` 为 reviewed adaptation。
- 定义输入：episode profile、direction、ordered source segments、known entity refs、continuity facts、prompt locale 和 output schema version；不接收 credential 或 hidden provider payload。
- 定义输出：scene/shot local keys、source/dialogue segment refs、dramatic purpose、action summary、shot size、camera angle/movement、duration、voice-over/SFX、entity mentions、continuity notes、reviewable image instruction 和 typed findings。
- 明确禁止模型输出/猜测 byte offsets、line numbers、Scaena refs、digests、timestamps、acceptance state、cost receipt 或完整 chain-of-thought。
- 提供四个共享引擎 profile：`vertical-short-drama-v1` first-support；`dialogue-dense-v1`、`manga-panel-v1`、`ad-microdrama-v1` exploratory。
- 提供 valid fixtures：竖屏冲突场、双人密集对白、漫剧动作段、15–30 秒广告微短剧；invalid fixtures：unknown segment、越序引用、shot 无 purpose/duration/prompt、伪造 offsets/digests/accepted、超出 shot/duration bounds、复制 hidden prompt。
- 提供 review checklist、failure modes、repair hints、rights 与 maturity；不复制 Scaena schema source 或 Scaena provider policy。
- 所有 `solution.json`、catalog、release manifest、contract metadata 与 digests 通过 Template Registry CLI/service 生成；人工只编辑 Prompt prose、examples 和指南。

## Capabilities

### New Capabilities

- `official-ai-drama-storyboard-breakdown-templates`: 官方中文优先分镜拆解 Prompt solution、scenario profiles、semantic output contract、fixtures、i18n、rights 与 maturity。

### Modified Capabilities

无。现有短剧、角色一致性和视觉 Prompt solutions 保持兼容。

## Non-Goals

- 不执行 provider 调用、估算/批准成本、解析 credential 或保存用户剧本。
- 不拥有 source offsets、candidate refs、ProductionGraph、accept/reject、export 或 evidence。
- 不新增同义 Skill；现有 `scaena-storyboard-breakdown` 仅消费本 solution ref/digest。
- 不承诺图片/视频 generation quality；image instruction 只是可审阅的下游生成输入。

## Impact

- 新增 solution 内容、fixtures、author guide 与 OpenSpec，不修改现有 solution IDs。
- 初始 `rights=internal`、`maturity=exploratory`；只有 `vertical-short-drama-v1` 在 provider-free conformance、Scaena compiler fixture 和一轮受控 owner canary 后可提议 `first-support`。
- Prompt body 只在显式 inspect/render/review 中出现；普通 catalog、CLI output、logs、events 和 evidence 保持 refs/digests，不泄漏正文。
