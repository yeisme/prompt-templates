## Context

本仓库是官方中文优先内容源。结构化角色资产包需要同时服务两类用户：普通创作者希望复制/编辑一份完整 YAML/JSON；Scaena/Eikona consumer 需要 exact schema、descriptor、compiler profile、prompt sections和 fixtures。machine metadata 必须由 Registry authoring service写，Prompt prose和指南可人工编辑。

## Goals / Non-Goals

**Goals:**

- 提供 production-oriented、中文自然、字段稳定的角色资产模板包。
- 让完整 JSON和模块化 YAML表达相同 canonical task。
- 用 fixtures固定成人、左右 marker、材料覆盖、三视图、鞋型、reference roles、QC和输出语义。
- 让 Markdown Prompt sections继续可读可审，但不成为角色事实的第二真源。
- 让资产 preset 按依赖关系编译，而不是按目录或展示顺序执行。
- 让表情资产在最少变量条件下生成、逐格审阅和局部修复，同时保持 face master 为唯一身份真源。

**Non-Goals:**

- 不保存真实人物图、用户项目或 provider结果。
- 不执行 compiler、Schema validator或生成模型。
- 不替代Scaena角色/服装/连续性 canonical state。
- 不修改旧 solution或强制用户一次迁移。
- 不把 expression sheet 描述成 LoRA 训练集，也不在本 change 中设计训练、微调或数据集发布流程。

## Decisions

### 1. 新 solution 而不是扩写旧 Markdown solution

目录设计：

```text
solutions/video/ai-drama-character-assets/
  solution.json
  contracts/
    documents/
    inputs/
  schemas/
  templates/
    characters/
    wardrobes/
    tasks/
    plans/
    qc/
  prompts/
    sections/
  compiler-profiles/
  fixtures/
    valid/
    invalid/
  docs/
```

旧 `short-drama-character-consistency` 保持 v1；新 solution可以在用途说明中引用旧 solution，但不共享可变文件或隐式 latest。

### 2. YAML 为主作者体验，JSON 为对等格式

官方 source优先提供 YAML，所有重要 fixture同时提供规范化 JSON。两者通过相同 Schema、canonical digest和Scaena compiler fixture验证。YAML不使用 anchor/alias/tag/merge key，避免作者示例诱导不安全语法。

### 3. 武侠三视图 fixture 的模块拆分

```text
character/wuxia-female-v1
wardrobe/wuxia-hanfu-moonwhite-v1
task/character-turnaround-three-view-v1
layout/turnaround-three-view-v1
qc/character-turnaround-production-v1
```

完整 single-file fixture保留用户原始体验；模块化 fixture通过 exact logical refs组合。左右 marker、配饰、材料 zone、view rotation和鞋型使用机器字段，中文 prose用于美术意图。

### 4. Prompt section 模板不重复完整事实

sections按 identity、body、wardrobe/material、layout/view、camera/light、reference responsibilities、constraints和QC hints组织。Compiler profile只声明section order、字段映射、constraint precedence和locale fallback；不包含代码。

中文 first slice 使用一个 `main` role 和九个 `asset_profile_id`，避免把每种生图任务复制成独立 solution：

| Profile | 产物 |
|---|---|
| `face-master-v1` | 脸部身份母版 |
| `body-master-v1` | 全身比例母版 |
| `turnaround-three-view-v1` | 前侧背三视图 |
| `wardrobe-sheet-v1` | 服装材料拆层表 |
| `expression-sheet-v1` | 表情表 |
| `action-sheet-v1` | 动作阶段表 |
| `prop-scene-sheet-v1` | 道具或场景资产表 |
| `shot-keyframe-v1` | 分镜关键帧 Prompt |
| `continuity-repair-v1` | typed finding 有界修复 |

Profile 只改变 Prompt 编译约束，不改变 SubjectVersion、视觉资产、ProductionGraph 或 acceptance 的 canonical owner。

### 5. 预设执行顺序由依赖决定

官方文档 SHALL 使用以下依赖图作为生产顺序，而不是沿用 preset 文件的目录顺序：

```text
face-master
  → expression-sheet（脸部级）
  → body-master
  → 基础服装定稿
  → turnaround-three-view
  → wardrobe-sheet（其余服装） ∥ hairstyle-sheet（仅多发型时）
  → action-sheet
  → prop-scene-sheet
  → shot-keyframe
```

基础发际线和基础发型外轮廓属于身份锚点，随 face master 锁定。替换发髻、束发或其他剧情发型时，consumer 必须创建独立 hairstyle task，并在接受新发型后重新验证脸部身份；不得通过 wardrobe task 或 expression task 顺带改发型。

Turnaround 必须穿已定稿的基础服装，用它作为前、侧、背三视图的对照锚，因此不能提前到 base wardrobe 之前。

### 6. Expression sheet 是独立 cells，不是模型生成的六格图

`expression-sheet-v1` 的 canonical task 约束为：

- exact accepted face master 是唯一 `identity_source`；
- `subject_count=1`、`depiction_count=6`；
- `layout=expression_contact_sheet_3x2` 只定义审稿排列，不要求 provider 在一张图中画六格；
- `output_intent=independent_cells_plus_contact_sheet`；
- 每个 cell 生成恰好一个成年主体，使用稳定 `view_key` 和语义 artifact title；
- `wardrobe_json` 可保持空对象；可见领口属于 `presentation_only`，不得创建或覆盖 wardrobe canon；
- face master 继续是身份真源，accepted expression artifact 只能成为表演/表情引用，不能升级为新的 face master。

Production 路径由 Eikona 执行六个独立任务并拼接确定性 3×2 contact sheet。Quick/candidate 路径 MAY 生成单次六格预览，但必须标记为 non-production，不能替代独立 cells、逐格 QC 或 human acceptance。

### 7. Reference、capture、seed 与表情 delta 分离

Identity binding 只允许继承脸部骨骼比例、五官间距、肤色范围、永久识别 marker、发际线和基础发型外轮廓；必须禁止它把源图的表情、妆容、服装、背景或戏剧化调色带入新 cell。

Camera/light 不通过“identity reference 看起来相似”隐式推断。Task 必须提供 capture lock，至少固定正面平视、bust 裁切、头部 yaw/pitch/roll、gaze target、头部占比、曝光和主光方向。缺失时生成 blocking finding，而不是自行猜测。

表情强度使用单个整数：`0=neutral`、`1=micro`、`2=subtle-readable`、`3=clear-controlled`、`4=strong-controlled`。不接受 `2→3` 之类范围值，也不允许通过改变头部姿态、肩线或镜头来伪造强度。

`family_locked` 用于让一组 cells 可比较和可重跑；它不构成身份锁，也不保证远端 provider 产生像素级相同结果。身份稳定性仍由 exact refs、digest、capture lock、QC evidence 和 human review 决定。

### 8. Expression repair 只修改失败维度

首轮每个 required cell 生成一个基线候选。单格失败时，最多生成两个 repair candidates，并保持相同 identity/capture/reference lineage：

- 身份漂移：只加强 identity preservation 或降低 expression delta；
- 表情不足：只调整可观察肌肉 delta 或强度；
- 表情过度：只降低强度；
- 构图漂移：只修 capture lock；
- 发型、妆容或领口污染：只修 reference `must_not_influence` 与 presentation 约束。

若两个及以上 cells 同时发生身份或 capture 漂移，系统应把问题升级为批次级 reference/baseline blocker，不继续为每格堆叠形容词。

### 9. Expression sheet 与训练数据集分离

同机位、同背景、同裁切的六个表情适合身份压力测试和表演校准，但不具备跨角度、跨景别、跨光线覆盖，且近重复样本容易造成训练过拟合。因此本 solution 不得宣称其为“现成 LoRA 训练集”。未来训练包需要独立 profile、训练权利声明、来源 lineage、去重、角度/景别覆盖和训练专用 acceptance gate。

### 10. Fixture matrix

Valid first slice：CLI-authored `wuxia-female-turnaround` 和 `manga-shot-keyframe` canonical JSON fixtures。后续仍需补 modular YAML、JSON/YAML equivalence、no-reference quick 和 approved multi-reference production。

Expression first slice 需要新增一个 `qingyi-expression-calibration` valid fixture，以及 face master 缺失、expression label/intensity 无效、production single-grid、capture conflict、hairstyle relock 缺失、identity drift、range collapse 和 range overshoot 等 invalid fixtures。

Invalid：minor/age ambiguity、duplicate keys、YAML alias、fixed seed missing、subject/depiction mismatch、left/right marker swap、transparent layer without opaque coverage、back-face conflict、shoe type drift、DRAFT identity ref、replace Prompt override in production、unknown field，以及上述 expression 专用错误。

### 11. Rights 与 maturity

首期 `rights=internal`、`maturity=exploratory`。示例不得包含真实演员身份、未授权作品角色、品牌logo或可识别的受保护服装设计。通过consumer conformance、人审和至少一轮离线production fixture后才能提议晋级。

## Risks / Trade-offs

- [模板过长] → 完整fixture用于导入测试，日常作者使用模块化文件和说明文档。
- [中文字段值难以机器判断] →关键不变量同时提供number/enum/anchor，prose只补充意图。
- [Schema与模板不同步] →所有release metadata由Registry authoring/validation生成，catalog build作为硬门。
- [Prompt section变成隐藏系统Prompt] →只保存公开可审阅的用户级生成说明，不保存hidden system instruction。
- [单次六格较省事] →只允许作为 quick preview；production 使用独立 cells，避免跨格污染和整张重抽。
- [固定 seed 被误当身份锁] →文档明确区分 rerun control 与 identity evidence，远端 provider 的确定性以 capability evidence 为准。
- [最小领口提前变成服装 canon] →标记为 `presentation_only`，并在 reference policy 中禁止向下游 wardrobe 继承。
- [表情资产被直接用于训练] →明确 dataset profile、rights 和覆盖 gate 是独立能力，当前输出保持 non-training-ready。

## Migration Plan

1. Registry structured authoring operation可用后创建solution、descriptor、Schema和fixture skeleton。
2. 导入武侠女性三视图为single-file valid fixture并规范化。
3. 提取模块化YAML和compiler profile，验证canonical equivalence。
4. 添加invalid matrix和中英文文档。
5. 增加 expression calibration fixture、独立 cell 编译、contact-sheet ordering 与 bounded repair conformance。
6. Catalog build/validate、Promptrepo conformance、Scaena/Eikona consumer canary通过后创建internal release。
7. 回滚删除catalog active mapping，release保持不可变可审计；旧Markdown solution与既有 `character_asset.prompt_bundle.v1` consumer 不受影响。
