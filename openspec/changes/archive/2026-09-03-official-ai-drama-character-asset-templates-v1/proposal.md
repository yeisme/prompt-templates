## Why

官方 Prompt 仓库已有短剧人物一致性 Markdown 模板，但缺少可供 Scaena/Eikona 直接验证和编译的角色资产 YAML/JSON、JSON Schema、声明式 compiler profile 和 conformance fixtures。需要把用户提供的武侠女性三视图规范沉淀为中文优先的官方解决方案包，而不是继续维护一段难以复用的大 Prompt。

现有预设还容易把目录排列误读为生产依赖：表情表被放在服装附近，但它本质上只依赖已接受的 face master；基础发型属于身份锚点，只有多发型需求才需要独立 hairstyle/relock；turnaround 则必须等待基础服装定稿。若不把这些依赖写进规范，consumer 会提前绑定 wardrobe、让表情资产污染身份，或把一次六格生成误当作 production-ready 表情包。

## What Changes

- 新增 `video/ai-drama-character-assets` 解决方案包，中文为 source locale，英文为 reviewed adaptation。
- 提供 Character、Wardrobe、Task、ReferenceBinding、QC、PromptBundle 的 Schema source/release artifacts。
- 提供脸部母版、身体母版、三视图、服装、表情、动作、道具/场景、分镜关键帧和 continuity repair 预设，共用一个 provider-neutral Prompt Bundle schema。
- 首个 conformance fixture 为成年武侠女性三视图：月白/浅烟紫汉服、薄纱与不透明丝绸层次、帆布鞋、固定左右 marker 和三视图对齐。
- 提供等价 JSON/YAML valid fixtures，以及 duplicate key、镜像 marker、薄纱覆盖错误、固定 seed 缺失、背面五官和 DRAFT reference 等 invalid fixtures。
- 提供声明式 compiler profile和 Markdown Prompt section templates；不在仓库放可执行 compiler 代码。
- 明确角色资产的依赖序与目录序无关：`face-master → expression-sheet → body-master → base wardrobe → turnaround`，多服装与多发型在各自 gate 后并行。
- 将 `expression-sheet-v1` 定义为脸部级校准资产：从 exact accepted face master 编译六个独立 expression cells，再由 Eikona 确定性生成审稿联系表；不要求 wardrobe canon，不让模型生成网格或文字。
- 明确 reference 继承白名单、禁止继承项、表情强度标尺、capture lock、family-locked seed 语义、逐格 QC 和有界 repair。
- 明确 expression sheet 不是 LoRA-ready dataset；训练用途必须进入独立数据集 profile、rights gate 和去重/覆盖验证。
- 中文 first slice 提供 `wuxia-female-turnaround` 和 `manga-shot-keyframe` 两个 valid fixtures，以及成年身份、固定 seed、marker 镜像、材料覆盖、背面、鞋型、DRAFT reference、production replace override 和 forbidden field 九个 invalid cases。
- 所有 solution/descriptor/Schema/compiler/fixture manifests 通过 Template Registry authoring service生成，人工只维护允许的 Prompt prose和经 CLI transaction 编辑的 YAML/JSON source。

## Capabilities

### New Capabilities

- `official-ai-drama-character-asset-templates`: 官方角色资产结构化模板、Schema、编译配置、i18n 和 fixtures。

### Modified Capabilities

- 无。现有 `short-drama-character-consistency` Markdown solution 保持兼容。

## Impact

- 新增官方 solution 目录、作者指南和 OpenSpec；不调用模型、不保存用户资产、不拥有 Scaena/Eikona状态。
- Scaena 继续拥有 SubjectVersion、capture/continuity lock 和 production freeze；Eikona 继续拥有生成、候选、联系表、反馈和 handoff。Prompt 仓库只拥有公开模板正文和 conformance 语义。
- Catalog/release metadata 由 Template Registry CLI生成并校验。
- 发布 channel 首期保持 internal/exploratory，conformance和consumer canary通过后再晋级。
