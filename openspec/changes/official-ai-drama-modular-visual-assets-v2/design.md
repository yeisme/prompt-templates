## Context

`ai-drama-character-assets` 已有 face、body、wardrobe、hairstyle 等模板，`ai-drama-background-assets` 已有空背景方向，但这些模板仍以“生成一个可用成品”为主。新的模块化生产要求模板直接表达资产边界、接口和禁止继承项：无头发头模不能被发型污染，服装不能复制脸，场景壳不能偷偷带入人物或可搬动物件。

Prompt Repository 只负责可评审 Prompt 解决方案。它不负责 Provider 能力、Alpha 客观 QA、运行证据、候选选择、subject freeze 或 ProductionGraph acceptance。因此 2.0.0 必须把执行后才能确认的事项写成 `quality_checks` / `review_checklist`，而不是用 Prompt 文案假装已经满足。

## Goals / Non-Goals

### Goals

- 提供角色核心、表面层、单件穿戴物、独立物件和空场景壳的完整官方模板族。
- 让所有模板共享稳定 slot、DesignSpec、RenderRevision、view plan 和 isolation vocabulary。
- 让正脸无头发头模成为第一个垂直切片，同时不把完整头部核心缩减成只有一张脸面具。
- 让人物透明资产和完整不透明背景分别有清晰的输出要求和负面规则。
- 保持 1.x 版本不可变，允许旧消费者继续按历史地址读取。

### Non-Goals

- 不执行模型，不保存真实 Prompt payload、credential、run 或 artifact。
- 不用一张 provider-generated grid 代替多个独立生产视图。
- 不生成 3D mesh、UV、albedo、rig 或 motion proof。
- 不让 preview 模板产生新的 canonical identity、wearable、object 或 scene-shell 资产。

## Decisions

### 1. 2.0.0 使用两个 solution family，共享一套 slot contract

`ai-drama-character-assets@2.0.0`：

| Template | Slot / role | 主要输出 |
| --- | --- | --- |
| `head-core-bald-v1` | `head_core` | 完整无头发头部核心，透明 RGBA |
| `body-core-neutral-v1` | `body_core` | 中性完整覆盖身体核心，透明 RGBA |
| `surface-coat-hair-v1` | `surface_coat` | 独立头发/毛发层设计与 fitted render |
| `wearable-garment-v1` | `wearable` | 单件服装设计与 fitted render |
| `wearable-accessory-v1` | `accessory` / `extension_part` | 单件装饰或扩展部件 |
| `character-layer-preview-v1` | preview | 分层对齐/遮挡预览 |
| `character-harmonized-preview-v1` | preview | 整体协调预览 |

`ai-drama-background-assets@2.0.0`：

| Template | Slot / role | 主要输出 |
| --- | --- | --- |
| `semantic-object-v1` | `semantic_object` | 独立物件设计/渲染，默认透明 |
| `empty-scene-shell-v1` | `environment_shell` | 无人物、无物件的完整不透明空场景 |
| `environment-layer-preview-v1` | preview | 壳体与物件的分层占位预览 |
| `environment-harmonized-preview-v1` | preview | 环境整体协调预览，仍不含人物 |

不创建每个年龄、物种或题材的独立 template ID。差异通过 `topology_family`、`age_band`、`coverage_policy`、`style_profile` 和 constraints 进入 authoring input。

### 2. Provider Prompt 使用固定编译顺序

角色类模板按以下顺序编译：

1. canonical identity/topology anchors；
2. 当前 slot 的设计职责；
3. view/camera capture lock；
4. isolation/crop/transparent output；
5. material/light behavior；
6. must-preserve interfaces；
7. forbidden inheritance 与 negative constraints。

环境类模板按：空间/物件定义 → geometry/view/camera → scene emptiness → light/material → preserve → forbidden subjects/traces 编译。

固定顺序比把用户字段直接拼接在末尾更容易测试，也能防止“华丽古装”这类描述覆盖无发饰、无背景或单件资产约束。

### 3. `head-core-bald-v1` 同时支持 detail front 和完整六视图

第一视图 `detail_front` 使用严格正脸、正交感镜头、yaw/pitch/roll=0、双眼水平直视，保留完整头顶、后脑轮廓、双耳、自然头皮、下颌和脸部身份。它不出现头发、发际线造型、发饰、耳饰、脖子、肩膀、衣服、背景、地面或投影。

完整 core 还包含 front-left three-quarter、left profile、back、right profile、front-right three-quarter。每个视图是独立 production view；contact sheet 只能由 consumer 在本地从独立 artifacts 合成。

替代方案是继续沿用 face-mask front 作为 canonical identity。它缺少头顶、后脑和双耳几何，无法支撑独立头发层，因此只保留兼容用途。

### 4. 身体核心使用 neutral coverage，而不是裸模

`body-core-neutral-v1` 的目标是比例、体型、肢体和拓扑锚，不需要显式解剖。所有年龄默认使用无品牌、无装饰、紧凑但不强调身体隐私部位的完整中性覆盖。未成年人使用更严格的 age-appropriate coverage 和非成人化姿态/材质。

非人角色仍使用 `body_core`，由 topology family 选择四足、翼型、蛇形、机械等结构。模板必须禁止把衣服、毛发、配饰或环境烘焙进核心。

### 5. 头发、服饰和装饰必须声明接口与禁止继承

每个 DesignSpec 至少声明：

- `attachment_interface` / `fit_interface`；
- `layer_order`；
- `silhouette`、`material`、`color_regions`；
- `occlusion_rules` 与 `collision_risks`；
- `inherit[]` 和 `forbid[]`；
- `view_plan` 与 `required_evidence`。

头发可以继承 head shape、scalp contour、attachment landmarks，但禁止继承脸部表情、服装、首饰和背景。服装可以继承 body proportion 与 fit landmarks，但禁止继承 face、hair、identity expression 和 environment。

### 6. 物件和场景壳使用不同画布语义

`semantic-object-v1` 默认输出透明 RGBA，可按 geometry-adaptive view plan 生成独立视图。`empty-scene-shell-v1` 输出完整不透明画布，不要求透明，也不能留出伪透明棋盘格。

场景壳禁止人物和人形痕迹，包括照片、海报、电视画面中的人物、雕像、模特、影子、倒影、驾驶员和乘客。车辆如果本身是剧情物件，优先作为 `semantic_object`；如果只是固定环境结构，也必须为空车。

### 7. Preview 只检查关系，不创建新真源

layer preview 显示 source layers 的几何对齐、边缘、穿插和遮挡；harmonized preview 显示整体色彩、材质和光线协调。两个模板的 output contract 都必须声明：

- `canonical=false`；
- exact `source_refs[]` 与 digests；
- 不得作为 source slot 的替代 ref；
- 不能宣称 subject frozen 或 production ready。

### 8. 版本和发布保持加法兼容

1.x 目录、template ID、Prompt 文本和 fixture 继续不可变。2.0.0 使用新版本目录和新 template ID。新 consumer 可以显式迁移；旧 ref 不自动重定向。Catalog、contract 和 fixture index 由 Template Registry CLI 生成，避免手写结构化 metadata。

## Risks / Trade-offs

- [模板数量增加，作者输入更复杂] → 提供 shared Brief、默认 slot policy 和 preset 示例；不为每个题材复制模板。
- [模型可能仍生成头发或背景] → PromptRepo 提供明确 constraints 与 review checklist；Eikona 负责 Alpha、污染和人工 QA。
- [六视图导致成本增加] → production density 决定需要哪些视图；Prompt 模板只提供稳定 view contract。
- [preview 被消费者误用] → template output 和文档都要求 `canonical=false` 与 exact source lineage。
- [未成年人输入歧义] → 缺少明确 age band 时使用最保守 coverage policy，禁止成人化表现。

## Migration Plan

1. 创建 2.0.0 solution skeleton 与共享词汇，不修改 1.x。
2. 先完成 `head-core-bald-v1`、`body-core-neutral-v1` 和 fixtures。
3. 再加入 hair、garment、accessory、object、scene shell。
4. 最后加入 layer/harmonized previews 与多语言适配。
5. 通过 Template Registry build/validate 生成 catalog 和索引；provider-free consumer fixture 证明 Eikona 可解析。
6. 回滚时移除 2.0.0 catalog publication；1.x refs 和内容不受影响。

## Open Questions

无阻塞问题。各 topology family 的精确 view catalog 和英文 reviewed maturity 在内容实现阶段通过 fixture 与人工校对确定。
