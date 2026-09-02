## Why

现有角色模板以脸模、身体、服装或发型成品图为主，仍容易把身份、头发、服饰、装饰和背景一次性烘焙到同一画面。为了支持换发、换装、局部修复、连续性复用和 Scaena 分镜装配，Prompt Repository 需要提供一组真正按资产语义隔离的官方解决方案，而不是继续叠加更长的单图提示词。

## What Changes

- 新增 `ai-drama-character-assets@2.0.0`，提供 `head-core-bald-v1`、`body-core-neutral-v1`、`surface-coat-hair-v1`、`wearable-garment-v1`、`wearable-accessory-v1`、`character-layer-preview-v1` 与 `character-harmonized-preview-v1`。
- `head-core-bald-v1` 生成完整无头发头模：保留头顶、后脑、双耳、自然头皮与脸部身份，不包含头发、发饰、耳饰、脖子、肩膀、衣服、背景或外部投影；正脸 detail 是第一视图，但 canonical core 支持六视图。
- `body-core-neutral-v1` 生成与头模分离的中性身体核心，并按年龄、物种和 topology family 应用安全覆盖；未成年人不得出现显式解剖细节。
- `surface-coat-hair-v1` 将头发作为可替换表面层设计，记录发际线接口、体积、长度、分区、遮挡和禁止继承项；不携带首饰、衣服或背景。
- `wearable-garment-v1` 与 `wearable-accessory-v1` 分开服装和装饰，支持单件设计、穿戴接口、层级顺序、碰撞/遮挡、材质与颜色约束；不得污染身份或场景。
- 新增 `ai-drama-background-assets@2.0.0`，提供 `semantic-object-v1`、`empty-scene-shell-v1`、环境分层预览和 harmonized preview。语义物件必须独立，空场景壳必须无人物和人形痕迹。
- 角色核心和贴合型资产使用六视图合同；物件使用 geometry-adaptive view plan，并在输入/输出中声明选择原因。
- Prompt 输出继续编译为现有 Prompt Bundle/PromptRepo 消费合同；模板只拥有正文、变量、失败模式、评审清单、rights 与 maturity，不拥有执行、候选选择或 production acceptance。
- 保持 `ai-drama-character-assets@1.x`、`ai-drama-background-assets@1.x`、`face-master-v1` 和 `face-mask-front-v1` 不可变。新 canonical 头部入口是 `head-core-bald-v1`，旧模板只作为兼容入口保留。

## Capabilities

### New Capabilities

- `official-modular-character-asset-templates`: 定义头部核心、身体核心、头发/表面层、单件服饰与装饰的官方 Prompt 解决方案和隔离规则。
- `official-modular-environment-asset-templates`: 定义独立语义物件、空场景壳和环境隔离负面规则。
- `official-modular-asset-preview-templates`: 定义分层预览与 harmonized preview，明确预览不是新的 canonical 资产。

### Modified Capabilities

无。1.x 解决方案、历史 profile 与地址保持不变，2.0.0 作为新 major 并行发布。

## Impact

- 影响 `solutions/video/ai-drama-character-assets/`、`solutions/video/ai-drama-background-assets/`、fixtures、作者指南和测试指南。
- Template Registry 负责由内容源生成 catalog、contract 和 fixture 索引；本 change 不手写结构化 catalog。
- Eikona 通过 `promptrepo://` / `prompt_ref` 消费模板并负责执行与运行证据；Scaena 只消费 Eikona refs 与 readiness facts。
- 所有新生图示例使用 canonical model ref `openai/gpt-5.4-image-2`；自动化验证不得调用真实 Provider。
