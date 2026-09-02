# AI 做剧模块化视觉资产模板 v2

状态：`archived 2026-09-02（内容已实现，provider-free 验证通过；maturity=exploratory，未发布 release）`  
OpenSpec：[`official-ai-drama-modular-visual-assets-v2`](../openspec/changes/archive/2026-09-02-official-ai-drama-modular-visual-assets-v2/proposal.md)

## 设计目标

v2 不再让一张“角色完成图”同时承担身份、头发、服装、装饰和背景。每个可复用资产都先有独立设计，再针对角色、视角和风格生成实际渲染。

两个 solution family 的边界如下：

- `ai-drama-character-assets@2.0.0`：头部核心、身体核心、头发/表面层、服装、装饰和角色预览；
- `ai-drama-background-assets@2.0.0`：独立语义物件、空场景壳和环境预览。

Prompt Repository 只提供 Prompt 正文、输入变量、输出要求、失败模式、评审清单、rights 和 maturity。图片生成、Alpha QA、候选选择、运行证据和 production acceptance 属于 Eikona/Scaena。

## 模板矩阵

| Template ID | 状态 | 主要职责 | Canonical output |
| --- | --- | --- |
| `head-core-bald-v1` | 已实现 | 完整无头发头部身份 | 透明 RGBA，独立视图 |
| `body-core-neutral-v1` | 已实现 | 身体比例与 topology | 透明 RGBA，完整中性覆盖 |
| `surface-coat-hair-v1` | 已实现 | 头发、毛发、鳞片等表面层 | 透明 RGBA，独立设计/贴合渲染 |
| `wearable-garment-v1` | 已实现 | 单件衣服、鞋、盔甲 | 透明 RGBA，单件/贴合渲染 |
| `wearable-accessory-v1` | 已实现 | 首饰、腰封、胸针、角、尾等 | 透明 RGBA，单件/贴合渲染 |
| `semantic-object-v1` | 已实现 | 独立可交互物件 | 默认透明 RGBA |
| `empty-scene-shell-v1` | 已实现 | 无人物无物件的空间壳 | 完整不透明画布 |
| `*-layer-preview-v1` | 已实现 | 检查层级、贴合、遮挡 | 非 canonical preview |
| `*-harmonized-preview-v1` | 已实现 | 检查整体色彩、材质、光线 | 非 canonical preview |

## 无头发完整头模

`head-core-bald-v1` 的第一视图是严格正脸 detail，但它不是“只剩脸皮的面具”。必须保留完整头顶、后脑轮廓、双耳、自然头皮、下颌与脸部身份，这样后续头发层才能稳定贴合。

正向控制重点：

```text
完整无头发头部核心，严格正脸，yaw=0、pitch=0、roll=0，双眼水平并直视镜头；完整头顶、后脑轮廓、双耳、自然头皮、完整下颌；正交感镜头，均匀柔光，真实皮肤纹理；独立透明 RGBA PNG，干净抗锯齿边缘。
```

禁止项重点：

```text
头发，假发，发际线造型，发饰，簪子，珠花，头冠，耳饰，项链，脖子，肩膀，衣服，领口，身体，背景，场景，地面，环境投影，悬浮阴影，白底，黑底，棋盘格，多视图拼图，侧转，俯仰，透视畸变。
```

完整 head core 还需要左前 3/4、左侧、背面、右侧、右前 3/4。每个视图独立生成；contact sheet 由消费者在本地拼，不要求 Provider 一次生成网格。

## 身体核心

身体核心的职责是比例、体型、肢体和 topology，不是裸体解剖参考。默认使用无品牌、无装饰、完整覆盖的中性基础外观。未成年人必须使用年龄适配、非成人化的姿态、材质和覆盖策略；任何年龄都不要求显式解剖细节。

非人角色沿用同一 `body_core`：四足、翼型、蛇形、机械等差异由 `topology_family` 描述。毛发、鳞片外层、衣服、盔甲和尾翼等根据职责进入 `surface_coat`、`wearable` 或 `extension_part`。

## 头发、服饰和装饰

这些资产都要声明：

- 连接/贴合接口；
- layer order；
- silhouette、material、color regions；
- 遮挡和碰撞风险；
- 允许继承和禁止继承；
- 需要的视图和证据。

头发可以读取头型和头皮接口，但不能复制脸部表情、首饰、衣服或背景。衣服可以读取身体比例和贴合点，但不能复制脸、头发、身份表情或场景。装饰应按单件设计，耳饰、项链、腰封、胸针和头饰不能打包成一张不可拆的“装饰套装图”。

## 物件与空场景

`semantic-object-v1` 用于任何可搬动、可持有、可变化或参与剧情的物件。武器、杯子、书、车辆、箱子、食物都应独立；输出不包含手、人物、腰带、桌面或环境。

`empty-scene-shell-v1` 只包含固定空间结构：建筑、地形、固定设施、光线逻辑、机位、深度和遮挡。禁止：

- 人物、肢体、人影、倒影；
- 海报、照片、电视画面中的人物；
- 雕像、模特、人体立牌；
- 车辆中的驾驶员和乘客；
- 桌上杯子、武器、箱子等独立物件。

背景输出必须完整不透明。透明输出、棋盘格、白底抠图或黑底抠图都不符合 scene-shell contract。

## Preview 的边界

layer preview 用于检查对齐、穿插和遮挡；harmonized preview 用于检查整体色彩、材质和光线。二者都必须记录 exact source refs，并标记 `canonical=false`。

即使 harmonized preview 看起来最完整，它也不能替代无头发头模、身体核心、头发、衣服或场景壳。Eikona 接受 preview 也不等于 Scaena 已冻结角色或批准生产。

## 版本兼容

`ai-drama-character-assets@1.x`、`ai-drama-background-assets@1.x`、`face-master-v1` 和 `face-mask-front-v1` 保持不可变。新 canonical 头部入口为 `head-core-bald-v1`；旧消费者不会自动跳转到 2.0.0。

结构化 catalog、contract 和 fixture 索引由 Template Registry CLI 生成。2026-09-02 起两个 family 的全部 11 个模板（7 角色/环境 + 4 预览）已由 CLI 完成正文、contract、document、共享 schema 绑定与 fixture 集（42 cases）并全部通过 `contract/document/fixture/catalog validate`；但这不代表 Provider 实拍验证或 release 已发布。

## 共享词汇（stable vocabulary）

以下 machine ID 是两个 v2 solution family 的稳定词汇，不翻译、不随 profile 改名；模板正文、contract input enum、fixture 与 preview 输出必须使用同一组值。

### Slot（资产槽位）

| Slot ID | 职责 | 输出画布 |
| --- | --- | --- |
| `head_core` | 无头发头部核心身份与几何 | 透明 RGBA |
| `body_core` | 身体比例、肢体与 topology | 透明 RGBA |
| `surface_coat` | 头发、毛发、鳞片等可替换表面层 | 透明 RGBA |
| `wearable` | 单件服装、鞋、盔甲 | 透明 RGBA |
| `accessory` | 单件装饰（首饰、腰封、胸针等） | 透明 RGBA |
| `extension_part` | 角、尾、翼等扩展部件 | 透明 RGBA |
| `semantic_object` | 独立可交互物件 | 默认透明 RGBA |
| `environment_shell` | 无人物无物件的空场景壳 | 完整不透明 |
| `preview` | 分层/harmonized 检查图 | `canonical=false` |

### DesignSpec（设计规格）

一个 slot 的一份可审阅设计声明，至少包含：`attachment_interface`/`fit_interface`（与核心或其他层的连接/贴合接口）、`layer_order`、`silhouette`、`material`、`color_regions`、`occlusion_rules`、`collision_risks`、`inherit[]`、`forbid[]`、`view_plan`、`required_evidence`。DesignSpec 是设计事实的集合，不是一次生成结果；模型输出不得伪造 DesignSpec 已被接受。

### RenderRevision（单视图渲染修订）

对一个 slot 的一个视图、依据当前 DesignSpec 与 active bindings 的一次可追溯渲染建议。每次 RenderRevision 只允许一个 `change_scope` 变量类（identity preservation、capture lock、camera motion、action timing、lighting、material state、layer state）；同一 DesignSpec 的多视图是多个独立 RenderRevision，禁止用一张网格图代替。

### View plan（视图计划）

- 角色核心与贴合型资产使用六视图合同：`detail_front`（严格正脸 detail，第一视图）、`front_left_three_quarter`、`left_profile`、`back`、`right_profile`、`front_right_three_quarter`。
- 物件使用 geometry-adaptive view plan：由物件几何（长条、扁平、对称、封闭容器等）选择最少充分视图，并在输出中声明选择原因。
- contact sheet 只能由消费方在本地用独立 artifacts 合成。

### Isolation（隔离）

每个模板只生成自己 slot 的内容；其他 slot、人物、背景、文字、水印、边框、棋盘格与伪透明边缘都是污染。人物类 slot 输出透明 RGBA 与干净抗锯齿边缘；`environment_shell` 输出完整不透明画布。

### Inherit / forbid（继承与禁止继承）

每个 reference binding 必须显式声明允许继承与禁止继承的字段；未声明即禁止。核心规则：`identity_source` 不得继承表情、妆容、首饰、服装、背景；`wardrobe_source` 不得继承脸、发际线、表情、身体身份；`style_source` 只提供原创维度化视觉约束，不复刻在世创作者或受保护作品。

### Preview（预览）

`preview` slot 的输出必须携带 `preview_lineage`（`canonical=false`、`purpose` 与 `source_refs[]`；每项含 `slot_id`、`source_version`、`artifact_digest`、`view_id`，按 slot 稳定排序）并精确回显消费方输入；preview 不得作为任何 source slot 的替代 ref，不得宣称 subject frozen 或 production ready。字段命名说明：共享 schema 顶层回显字段为 `subject_version`（而非 1.x 的 `subject_version_ref`），source lineage 项使用 `source_version`——Registry fixture 校验禁止 valid fixture 输出出现任何 `*ref` 键，该命名使预览 lineage 与 fixture 门共存；lineage 之外的 durable ref 仍一律禁止。

### 共享输出合同

两个 family 的模板共用同一输出 schema `character_asset.modular_slot_bundle.v1`（canonical 文件：`solutions/video/ai-drama-character-assets-v2/contracts/schemas/character_asset.modular_slot_bundle.v1.schema.json`，由 Registry `document artifact add` 生成与校验）。它承载 slot/view/RenderRevision/policy_echo 词汇的机器面，并包含预览专用面：`preview_lineage`（仅 `slot_id=preview` 的 bundle 必填、其他 slot 禁用，经 `allOf` if/then 表达）与 `policy_echo.preview_purpose`；character 与 environment 模板的 document descriptor 都绑定该 exact 文件与 digest，不允许各自复制漂移。

## 版本、locale、rights 与 maturity 规则

- 版本：`ai-drama-character-assets-v2@2.0.0` 与 `ai-drama-background-assets-v2@2.0.0` 是并行新 major；1.x 目录、template ID、正文与 fixture 不修改、不重定向。Registry authoring CLI 以 solution id 定位目录，因此 2.0.0 family 使用版本后缀目录；其 catalog 稳定地址为 `promptrepo://official/video/ai-drama-character-assets-v2@2.0.0` 与 `promptrepo://official/video/ai-drama-background-assets-v2@2.0.0`。2.x 内的加法演进递增 patch/minor，不原地覆盖已发布版本。
- Source digest：`zh-CN` 是 source locale；每个 role 的 template digest 即该 role 的 source digest。`en` 适配逐 role 绑定 source digest（同 `ai-film-multi-profile-production/docs/i18n.md` 的做法），source 变化后对应 en 适配立即 stale，必须重新评审 placeholder/约束等价并重跑 contract validate 后才能继续标注 reviewed；machine ID、slot/view enum、schema 字段与失败码不翻译。
- Rights：默认 `internal`；示例与 fixture 只使用原创虚构角色与非品牌材料，不含真人肖像、受保护角色复刻、品牌 claim、credential 或 provider payload。
- Maturity：2.0.0 内容初始一律 `exploratory`；`first-support` 需要 fixture 执行、人工评审、rights 结论与已知失败记录齐全；`mature` 另需真实脱敏使用证据。任何模板不得因正文完成而自称 first-support。
