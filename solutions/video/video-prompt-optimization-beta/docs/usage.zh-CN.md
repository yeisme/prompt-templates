# video-prompt-optimization-beta 使用指南

把粗略分镜、故事概要或失败返工需求，编译成扩散类音视频联合生成模型可直接提交的专业提示词正文。模型无关：平台差异（指代语法、时长上限、素材互斥）全部经输入变量声明。源方法论来自 Scaena 生产链路的 `wan3-prompt-optimizer` 技能（以万相3.0 实测为底），本 solution 把其中的通用规律固化为可由 Agent 编译的模板。

## 何时用本模板

- 有一段粗略创意/分镜/故事概要，要变成单条可提交的视频生成提示词。
- 需要按生成形态（T2V/首帧/首尾帧/全能参考/编辑延长）做正确的信息加减法。
- 需要正向排除（否定卡）、声音设计（声音卡）、器物与反射纪律（器物卡）、时长与语速核算、180° 轴线与六层镜头结构。
- 目标模型不确定或会更换——协议差异用变量适配，不需要换模板。

何时不该用：

- 已知完整变量值、只需渲染既有镜头模板 → `ai-drama-shot-video-generation`（蓄力大招）等渲染型家族成员。
- 要做 150 条运镜/布光/构图技术选型 → `cinematique-shot-techniques-beta`。
- 要做跨资产（图+视频+剪辑）联动工作流 → 先用 `template-registry-integration-designer` 分类。
- 提交参数确认、生成执行、出片验收 → Scaena 生成/验证层，不在本模板。

## 输入变量

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `generation_mode` | 是 | `t2v` / `first_frame` / `first_last_frame` / `reference_image` / `reference_video` / `edit_extend` |
| `source_brief` | 是 | 粗略分镜或故事概要，原文即可，不需要预处理 |
| `reference_manifest` | 否 | 上传素材映射：序号、名称、类型（角色视觉先验/场景/帧锚点），含上传顺序 |
| `media_reference_syntax` | 否 | 目标平台正文内指代素材的原生语法，例 `@图片1（名称）`、`@image1` 或 UUID 引用；留空用位置描述 |
| `dialogue_script` | 否 | 用户台词逐字稿；留空表示全片无台词 |
| `duration_budget` | 否 | 目标时长或时长约束；含目标模型单次生成上限则一并给出 |
| `style_requirements` | 否 | 用户指定的画质/风格/基调要求 |
| `extra_constraints` | 否 | 用户额外约束（禁止事项、商业要求等） |
| `output_language` | 否 | 正文语言，默认 `zh`（输出协议结构标记为中文【】〖〗•） |

## 编译流程（模板内部固化的顺序）

1. 形态判定与减法策略选择（T2V 全写 / 首帧只写运动 / 全能参考分视觉先验与帧锚点）。
2. 建〖设定档案〗（世界四要素、三张词表、服装状态机、声源清单、光源纪律）。
3. 时长核算（需求时长 = ⌈台词字数÷4⌉ + 静默秒数；超模型上限按拆分判据）与逐句语速校准。
4. 空间锚定（【场景与空间说明】+ 180° 轴线）与动作具象化（起点→过程→终点）。
5. 按【全局设定】五行 + 逐镜六层结构写出正文，全部用正向目标状态，素材按 `media_reference_syntax` 指代。
6. 出片前自检清单（否定卡扫描、器物卡、声音卡、互斥检查、语速一致性）。

## 输出契约

- 单个输出块：提示词正文（纯文本、【】〖〗• 协议、从【全局设定】起），正文前可附至多几条准备说明（形态确认、时长核算、素材映射）。
- 正文不含提交参数（分辨率/比例/时长字段/seed/水印/negative 通道），不含 Markdown，单镜 ≤200 字。
- 纯画面（无原生音频）模型上，声音设计行转为后期剪辑层的音效简报。
- 模板不提交、不生成、不验收；执行与验收归 Scaena 生成层与验证层。

## 平台适配说明

- 指代语法：通过 `media_reference_syntax` 声明，模板不预设 `@图片N` 或 `@imageN`。
- 时长上限：通过 `duration_budget` 带入（常见 5–30s），拆分策略按上限比例通用化。
- 互斥规则：多数平台 `reference_*` 与 `first_frame`/`last_frame` 互斥，模板要求按目标平台核实。
- negative 通道：有独立通道的平台，排除词经提交层写入通道，正文仍保持纯正向。

## 家族选择矩阵（视频生成侧）

| 需求 | Solution |
| --- | --- |
| 粗略概要 → 可提交正文（编译型，模型无关） | 本模板 `video-prompt-optimization-beta` |
| 变量值齐全的蓄力大招镜头渲染 | `ai-drama-shot-video-generation` |
| 运镜/布光/构图技术选型与绑定 | `cinematique-shot-techniques-beta` |
| 无台词纯环境音抓拍 vlog | `realistic-vlog-shot-generation` |
| 画外 VO 自述 + 音乐弧线 | `realistic-docu-vlog-generation` |
| 出镜口播 + 唇形同步 | `realistic-diary-vlog-generation` |
| 双人物写实格斗 | `realistic-fight-scene-generation` |
| 穿越机环绕双人刀战 | `fpv-sword-duel-generation-beta` |
| 穿搭拼贴首帧 + 卡点换装 | `outfit-collage-transition-director` |

## 消费方式

Exact ref（Agent 编译消费，provider-free inspect/preview）：

```text
promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en
```

方法论源：`agent/scaena/.claude/skills/wan3-prompt-optimizer`（万相3.0 实测底座，通用规律已抽入本模板）。提交与验收仍走 Scaena 生成层（`scaena video generate`）与验证流程。
