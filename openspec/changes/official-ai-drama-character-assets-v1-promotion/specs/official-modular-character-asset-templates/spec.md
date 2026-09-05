## MODIFIED Requirements

### Requirement: 官方角色模板必须覆盖模块化人物槽位
`ai-drama-character-assets@1.0.0`（2026-09-05 由 `-v2@2.0.0` 晋升为无后缀正式目录）SHALL 提供 `head-core-bald-v1`、`body-core-neutral-v1`、`surface-coat-hair-v1`、`wearable-garment-v1` 和 `wearable-accessory-v1`。每个模板 MUST 输出一个主要 slot，不得把 sibling slot 或背景烘焙进同一 canonical asset。

#### Scenario: 生成角色头部核心
- **WHEN** authoring input 选择 `head-core-bald-v1`
- **THEN** Prompt Bundle 只要求完整无头发头部、自然头皮、双耳和脸部身份
- **AND** 禁止头发、发饰、耳饰、脖子、肩膀、服装、背景和外部投影

## ADDED Requirements

### Requirement: 元 Prompt 不得直接进入图片 Provider
仓库的 compiler meta-prompt、schema instruction 或要求模型输出 Prompt Bundle 的正文 MUST NOT 直接作为图片生成请求。图片 Provider 只能收到 consumer 从已验证 Bundle 为单一 view 渲染的用户级视觉 Prompt。

#### Scenario: 实测程序尝试发送元说明 Prompt
- **WHEN** canary 输入是要求生成 `character_asset.modular_slot_bundle.v1` JSON 的元 Prompt
- **THEN** consumer 以 `CHARACTER_ASSET_META_PROMPT_FORBIDDEN` 或等价 stable reason code 在 Provider 调用前拒绝
- **AND** 不创建图片 run 或 artifact
