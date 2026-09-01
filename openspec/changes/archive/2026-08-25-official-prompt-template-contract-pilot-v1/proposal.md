## Why

官方目录已有中文/英文 Prompt 正文和确定性 catalog，但消费者无法仅凭 catalog 知道每个 `{{variable}}` 应填什么类型、是否必填、默认值、示例、许可和执行前 review 要求。本 change 使用 Template Registry CLI 为首个图像方案和首个 Sonora 音频方案生成双语 companion `TemplateContract` sidecar，验证中文优先、英文同步适配、敏感输入与 catalog digest 隔离方案。

## What Changes

- 为 `image/xhs-product-cover@1.0.0` 的 `main.zh-CN` 与 `main.en` 生成 `promptrepo.template-contract.v0.1` sidecar。
- 为 `audio/podcast-narration@1.0.0` 的 `main.zh-CN` 与 `main.en` 生成同 schema sidecar，声明 `audience`、`duration`、`script`、`show_positioning`、`tone`，其中 `script` 为 sensitive。
- 声明 `product`、`audience`、`selling_point`、`visual_style`、`aspect_ratio` 五个实际占位符。
- `zh-CN` 和 `en` sidecar 使用相同稳定字段名、类型与 enum；example 按 locale 适配，label/description 同时提供中文和英文。
- 图像 sidecar 标记 `license=internal`、`permission=preview`、`permission=execute_requires_review`；音频 sidecar 标记 `inspect`、`preview`、`tts_handoff`。这些 metadata 都不授予 Provider 或付费执行权限。
- 所有 JSON 均由 Template Registry CLI 生成，不手工编辑；catalog digest 保持不变。

## Compatibility and Rollback

这是 additive pilot。旧消费者忽略 `contracts/` 后仍读取相同 catalog 和 Prompt。回滚可停止生成/消费 sidecar，并继续使用已有 catalog；不得删除或改义现有 Prompt 变量。sidecar schema 后续变更遵循至少两个 minor releases 的兼容窗口。

## Impact

- canonical content owner：本仓库。
- structured writer：Template Registry CLI。
- public runtime DTO：`github.com/yeisme/promptrepo` 后续可消费的 `TemplateContract`。
- Provider calls、外部写入和发布：0。
