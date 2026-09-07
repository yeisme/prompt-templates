## Why

现有官方视频模板覆盖短剧分镜和单镜头生成，但没有“真实产品资料和页面 → 产品宣传片 Brief → 固定镜头库映射”的合同。外部 `video-shotcraft` 是完整 Skill 和 Remotion 工具包，直接注册为 Prompt 模板会丢失工具、状态、rights 和执行门禁。

## What Changes

- 新增 `video/product-promo-shot-design-beta@1.0.0-beta.1`。
- 新增 `brief` 和 `shot-plan` 两个英文 Agent role、中文人工审阅译文和 JSON 输出 descriptor。
- 新增 CLI 生成的两步骤 recipe 和 `video-shotcraft` 固定提交 canary 文档。
- 记录外部 Skill、Template Registry、Scaena/Remotion、Eikona 和 Sonora 的 owner 边界。

## Capabilities

### New Capabilities

- `product-promo-brief`: 把已确认产品事实、受众、创作模式、品牌、交付、数据和 rights 转成可审阅 Brief。
- `product-promo-shot-plan`: 把已接受 Brief 和固定镜头库映射为实现前的语义镜头计划。

### Modified Capabilities

None.

## Impact

编译期保持零 Provider 调用。页面采集、视觉/音频生成、Remotion 实现、剪辑、费用、发布和资产接受继续由领域 owner 负责。新方案为 beta，不改变现有 exact refs。
