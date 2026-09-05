## Why

Auctra 已接入公共 Prompt Repository，但官方仓没有满足其 writing/revision 能力过滤的模板；Digital Human 的 Persona Package 也缺少可由 Registry 确定性编译的官方 system prompt 方案。

## What Changes

- 新增双语 `writing/revision-assistant@1.0.0`。
- 新增双语 `agent/digital-human-persona-system@1.0.0`。
- 新增双语 `image/xhs-product-cover-v2@2.0.0`，补齐 Eikona 通用图像消费能力并保留 v1 精确引用。
- 保持已有模板、引用、rights 和成熟度不变。

## Capabilities

### New Capabilities

- `cross-project-prompt-consumers`: 为文本修订、通用图像生成和数字人 Persona 提供可验证官方模板。

### Modified Capabilities

无。

## Impact

模板内容属于本仓库；Auctra 继续拥有 canonical text/review，Eikona 继续拥有 provider、Visual Job、review 和 artifact，Digital Human 继续拥有 Persona、avatar、voice、memory、knowledge 和 runtime。
