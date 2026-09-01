# AI 做剧模块化视觉资产模板 v2

状态：`active proposal`  
OpenSpec：[`official-ai-drama-modular-visual-assets-v2`](../openspec/changes/official-ai-drama-modular-visual-assets-v2/proposal.md)

## 设计目标

v2 不再让一张“角色完成图”同时承担身份、头发、服装、装饰和背景。每个可复用资产都先有独立设计，再针对角色、视角和风格生成实际渲染。

两个 solution family 的边界如下：

- `ai-drama-character-assets@2.0.0`：头部核心、身体核心、头发/表面层、服装、装饰和角色预览；
- `ai-drama-background-assets@2.0.0`：独立语义物件、空场景壳和环境预览。

Prompt Repository 只提供 Prompt 正文、输入变量、输出要求、失败模式、评审清单、rights 和 maturity。图片生成、Alpha QA、候选选择、运行证据和 production acceptance 属于 Eikona/Scaena。

## 模板矩阵

| Template ID | 主要职责 | Canonical output |
| --- | --- | --- |
| `head-core-bald-v1` | 完整无头发头部身份 | 透明 RGBA，独立视图 |
| `body-core-neutral-v1` | 身体比例与 topology | 透明 RGBA，完整中性覆盖 |
| `surface-coat-hair-v1` | 头发、毛发、鳞片等表面层 | 透明 RGBA，独立设计/贴合渲染 |
| `wearable-garment-v1` | 单件衣服、鞋、盔甲 | 透明 RGBA，单件/贴合渲染 |
| `wearable-accessory-v1` | 首饰、腰封、胸针、角、尾等 | 透明 RGBA，单件/贴合渲染 |
| `semantic-object-v1` | 独立可交互物件 | 默认透明 RGBA |
| `empty-scene-shell-v1` | 无人物无物件的空间壳 | 完整不透明画布 |
| `*-layer-preview-v1` | 检查层级、贴合、遮挡 | 非 canonical preview |
| `*-harmonized-preview-v1` | 检查整体色彩、材质、光线 | 非 canonical preview |

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

结构化 catalog、contract 和 fixture 索引由 Template Registry CLI 生成。当前文档只说明 planned contract，不代表模板已经发布或 Provider 已通过实拍验证。
