# 做剧视觉资产预设矩阵

## 目录序不等于依赖序

Preset 在目录、表格或 UI 中的排列只用于查找，不能作为生产排队依据。实际依赖图为：

```text
face-master
  → expression-sheet（脸部级）
  → body-master
  → 基础服装正面主视图
  → turnaround-left-profile
  → turnaround-back
  → 本地 1×3 审稿联系表
  → wardrobe-sheet（其余服装） ∥ hairstyle-sheet（仅多发型时）
  → action-sheet
  → prop-scene-sheet
  → shot-keyframe
```

`expression-sheet-v1` 在 face master 接受后即可开始，不依赖 body master 或 wardrobe canon。`turnaround-three-view-v1` 保持原 profile ID，但 production 语义是三个独立 artifacts：先接受基础服装正面主视图，再生成侧面和背面；联系表只由 consumer 本地拼接。

## 身份、发型与服装边界

- 发际线和基础发型外轮廓属于 face identity anchor，随 face master 锁定。
- 大礼发髻、夜行束发等替换发型需要独立 hairstyle task；每个新发型接受前必须重新验证脸部身份。
- Expression task 不得顺带改发型，也不得把可见领口写成 wardrobe canon。
- Wardrobe task 只拥有服装结构、材料、覆盖和配件，不得改脸、发际线或基础发型。
- Face master 始终是身份真源；expression、wardrobe、action 或 shot artifact 都不能反向替代它。

## Profile 矩阵

| Profile | 资产层级 | 主要产物 | 必需输入 | 关键门禁 | 下游 |
|---|---|---|---|---|---|
| `face-master-v1` | 脸部身份 | 一张中性正面脸部主视图 | subject + identity refs | 成年、单主体、无服装/背景污染 | SubjectVersion / expression |
| `face-mask-front-v1` | 脸部身份 | 一张正脸面具式透明 PNG | subject + identity refs + `transparent_subject` | yaw/pitch/roll=0、无装饰、无脖肩、Alpha≥10% | SubjectVersion / body master |
| `expression-sheet-v1` | 脸部表演 | 六个独立 expression cells + 审稿联系表 | accepted face master + capture lock | 不换脸、不换基础发型、不改机位 | 表演引用与压力测试 |
| `body-master-v1` | 身体比例 | 一张正面全身比例母版 | accepted face master + body task | 完整头脚、弱透视、中性基础层 | 基础服装 / 动作资产 |
| `turnaround-three-view-v1` | 身体与基础衣 | 正面主视图 + 独立侧面/背面 + 本地联系表 | accepted face/body/front wardrobe refs + marker/layout | 一 view 一 job、主视图先接受、背面真实、鞋型稳定 | 连续性与角色表 |
| `wardrobe-sheet-v1` | 服装 | 其余服装拆层表 | body + wardrobe + material zones | coverage、无品牌发明 | 镜头服装绑定 |
| `action-sheet-v1` | 身体动作 | 动作阶段表 | action task + body/wardrobe/prop refs | 持握手、方向、阶段 | 分镜动作关键帧 |
| `prop-scene-sheet-v1` | 道具/空间 | 道具或场景表 | prop/location facts | 结构与平面不漂移 | Scaena 场景装配 |
| `shot-keyframe-v1` | 镜头 | 镜头关键帧 | accepted shot intent | 不新增故事事实 | 视频模型输入 |
| `continuity-repair-v1` | 有界修复 | 修复候选 | typed finding + same refs | 不扩大修复范围 | 候选复审 |

`hairstyle-sheet` 是条件能力：只有项目明确需要多个发型时才建立；它不属于所有角色的必经步骤。在稳定 profile 正式发布前，consumer 应把它保留为 owner task，而不是伪装成 wardrobe 或 expression 变体。

## Expression production 形态

Production expression sheet 不是 provider 生成的一张六格图，而是：

```text
六个稳定 view_key
  → 六个独立图像任务
  → 逐格 QC / 局部 repair
  → Eikona 3×2 contact sheet
  → 人工接受
```

单次六格图只适合 quick preview，必须标记 non-production。生成模型不负责写 `neutral`、`grief-held` 等文字；语义标签由 artifact title 和联系表渲染器添加。

所有 profile 共用一个 Prompt Bundle schema。预设改变生成约束，不改变角色、资产、生产或接受状态的 canonical owner。

`face-mask-front-v1` 与 `face-master-v1` 并存：前者用于透明二维身份锚，后者继续服务既有 bust/中性棚拍消费者。不得把通用 `detail`、表达表或旧脸部母版裁成面具式脸模。

## Turnaround production 形态

```text
accepted face master
  → accepted body master
  → base-wardrobe front 主视图
  → left-profile 单图
  → back 单图
  → Eikona 本地 1×3 contact sheet
```

旧的“三格等宽排列”内容可以作为 quick preview 或兼容输入读取，但 production consumer 必须拆成独立 jobs。若调用方显式要求 Provider 一次生成三宫格，应在 Provider 调用前阻断。
