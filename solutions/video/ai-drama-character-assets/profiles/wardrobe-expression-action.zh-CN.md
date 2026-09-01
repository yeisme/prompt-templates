# 服装、表情与动作预设

## Wardrobe sheet

依赖：accepted body master；若为基础服装，还必须先于 turnaround 定稿。

- 分离内层、外层、腰封、鞋、首饰和可拆配件。
- 写清材料、颜色、结构、闭合、覆盖区域和磨损，不靠品牌名代替设计。
- 同一 sheet 保持人物身份、身体比例和镜头一致。
- 服装 reference 只继承结构、材料和覆盖，不得改脸、发际线、基础发型或身体比例。

## Expression sheet

### 资产定位与依赖

Expression sheet 是脸部级表演校准资产，只依赖 exact accepted face master。它不依赖 body master、基础服装或 turnaround，也不能替代 face master 成为新的身份真源。

基础发际线和基础发型外轮廓随 face master 锁定。若任务要求大礼发髻、夜行束发等新发型，必须停止 expression 编译并进入独立 hairstyle/relock 流程。

### Production task

Production task 应声明：

```text
subject_count = 1
depiction_count = 6
layout = expression_contact_sheet_3x2
output_intent = independent_cells_plus_contact_sheet
seed_policy = family_locked
```

`layout` 只决定审稿排列。Provider 每次只生成一个成年主体和一个表情，不生成六格网格，不生成文字标签。六个 artifact 使用稳定排序的 `view_key` 和 title，最后由 Eikona 拼成 3×2 联系表。

可见领口属于 `presentation_only`：例如月白色不透明交领内层只用于安全遮体和稳定肩颈轮廓，不创建 wardrobe version，也不得被下游继承为服装 canon。`wardrobe_json` 在此 profile 可以是空对象。

### Reference 继承边界

Identity source 只继承：

- 脸部骨骼比例和五官间距；
- 肤色范围和永久识别 marker；
- 发际线与基础发型外轮廓。

Identity source 禁止影响：

- 源图表情和视线；
- 妆容、首饰和服装；
- 背景、戏剧化调色和未声明灯光效果。

Camera/light 由 task 的 capture lock 提供，不能因为同一张 reference 同时“看起来像相同机位”就让 identity binding 越权承担构图角色。

### Capture lock

六个 cells 共同固定：

- 正面平视，bust 至肩；
- 头部 yaw、pitch、roll；
- gaze target，除非单格明确授权；
- 眼线高度、头部占比和裁切；
- 焦段观感、曝光、光源方向和背景。

只允许改变眉部、眼睑、眼周湿润度、嘴角、唇部开合、下颌与面颊肌肉张力，以及呼吸观感。不得用抬头、歪头、耸肩、后仰、推近镜头或换光线表现情绪强度。

### 强度标尺

| Intensity | 含义 |
|---:|---|
| 0 | neutral baseline，无情绪信号 |
| 1 | micro，只有微小肌肉信号 |
| 2 | subtle-readable，含蓄但可辨认 |
| 3 | clear-controlled，明确且受控 |
| 4 | strong-controlled，强烈但身份与解剖稳定 |

Intensity 必须是单个整数，不接受 `2→3`、`medium-high` 等范围或模糊值。

### 推荐六格

| View key | 标签 / 强度 | 可观察 delta | 禁止升级 |
|---|---|---|---|
| `view-expression-01-neutral` | `neutral / 0` | 眉眼、唇、下颌完全放松，作为比较锚 | 不加入情绪信号 |
| `view-expression-02-reserved-smile` | `reserved-smile / 2` | 闭唇浅笑，嘴角小幅上提，眼睑轻微柔化 | 不露齿、不大笑 |
| `view-expression-03-grief-held` | `grief-held / 3` | 内眉轻抬靠拢、下眼睑收紧、下眼缘湿润、下唇张力增加 | 不滑落泪水、不低头 |
| `view-expression-04-cold-anger` | `cold-anger / 3` | 眉部轻度压低靠拢、上眼睑张力、唇线压紧、咬肌轻绷 | 不涨红、不露齿、不瞪眼 |
| `view-expression-05-startled-fear` | `startled-fear / 2` | 上眼睑抬高、内眉轻抬、嘴唇微启、屏息感 | 不要求瞳孔变化、不带动头肩后缩 |
| `view-expression-06-resolve` | `resolve / 4` | 下眼睑稳定、眉部沉定、唇线压紧、下颌肌张力增加 | 不抬下颌、不改变 head pitch |

### Seed、QC 与 repair

`family_locked` 只表示同一任务族的比较和重跑策略，不保证远端 provider 像素级复现，也不是身份锁。身份通过 exact refs/digests、capture lock、逐格 QC 和人工审查确认。

首轮每格一个基线候选。单格失败时最多增加两个 repair candidates：

- 表情不足或过度：只改该格肌肉 delta/强度；
- 身份漂移：只加强 identity preservation 或降低 delta；
- 构图漂移：只修 capture lock；
- 发型、妆容或领口污染：只修 `must_not_influence` 和 presentation 约束。

两个及以上 cells 同时发生身份或 capture 漂移时，应停止逐格补丁，回查 face master、reference binding 或 capture baseline。

### 训练用途边界

六个同机位、同背景、同裁切的表情适合表演校准与身份压力测试，但不是 LoRA-ready dataset。训练包必须另设 profile，并补充训练权利、来源 lineage、去重、跨角度/景别/光线覆盖和训练专用 acceptance gate。

## Action sheet

依赖：accepted body master、所用 wardrobe version，以及动作涉及的 exact prop refs。

- 复杂动作拆为 anticipation、contact、result。
- 锁定持握手、道具方向、重心、屏幕方向和服装承接。
- 一格只表达一个主要动作阶段，避免模糊动态遮盖肢体问题。
- 全身表情、重心和身体反应在 action sheet 中验证；expression sheet 不承担全身表演覆盖。

Readiness：exploratory。
