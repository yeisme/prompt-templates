# 用法：镜头技术提示词

## 定位

这是一个**选型 + 绑定**层，不是又一套生成模板。150 条技术是现成的镜头语言词汇表；本 solution 把「选一条技术、绑定主体、投递」标准化。它服务的两个阶段：

1. **分镜拆解**（配 `ai-drama-storyboard-breakdown`）：每镜头确定一条主技术，`when_to_use` 提供选型依据，写进分镜的 camera/lighting 字段。
2. **镜头生成**（配 `ai-drama-shot-video-generation` 或直投图像模型）：`technique_prompt_bound` 直接成为镜头 prompt 的技术段。

## 选型流程

1. 从叙事意图出发（要观众感到什么），不是从「这个运镜酷」出发：
   - 地理/规模/压迫感 → Camera Work 的 Aerial/Bird's Eye/Crane；
   - 心理亲近/揭示 → Close-Up/Extreme Close-Up/Insert；
   - 情绪与氛围 → Lighting 全类（Backlight/Chiaroscuro/Blue Hour…）；
   - 节奏与转场 → Editing（Smash Cut/Jump Cut/Whip Pan…）；
   - 叙事结构 → Storytelling（Flashback/Cliffhanger/Motif…）；
   - 片种风格 → Genres & Styles（Film Noir/Wuxia/Giallo…）。
2. 候选技术读 spec 的 `when_to_use`（何时用）与 `common_mistakes`（三条翻车模式）做最终裁决；`difficulty` 高的技术（Vertigo Effect、One-er 等）需要更强的模型执行力。
3. 一个镜头只选一条主技术（contract `constraint:single_technique_per_shot`）。叠加第二条技术的 prompt 段是翻车主因。

## 绑定与投递

1. 取 spec `prompt_template`，把 `[Subject]` 替换为具体可拍主体（角色/物体/场景描述，写实在动作或状态，不写形容词堆砌）。
2. 除替换外不得改动：镜头、胶片、灯光语言就是技术本身。
3. 七个输入：`technique_id`（150 值 enum）、`technique_name`、`subject`、`technique_prompt_bound`（绑定后正文）、`target`（image|video）、`extra_directives`（时长/节奏等投递参数，可选）、`negative_prompts`（可选覆盖）。
4. `target=video` 时技术内运动语言保留一次且一致；`target=image` 时丢弃纯运动语言而不是与之矛盾。

## Scaena 消费

```bash
scaena prompt-asset repository sync
scaena prompt-asset catalog inspect 'promptrepo://official/video/cinematique-shot-techniques-beta@1.0.0-beta.1?locale=en' --json
```

分镜/生成工作流里由 storyboard prompt 编译或 shot 生成消费方完成绑定；人审通过 `preview`/`stage` 回执。

## 未来扩展

- **加一条技术**：新增 `assets/techniques/<id>.json`（schema 同现有 spec，`prompt_template` 必须含 `[Subject]`）→ 跑 `python3 scripts/cinematique_reindex.py`（会输出新 enum 值清单）→ `contract input set --name technique_id` 用新清单重放 enum → `contract refresh` + `catalog build/validate` + `prompt repository sync`。
- **改技术正文**：直接改 spec；`prompt_template` 改动属于内容变更，版本号递增并保留 replacement 说明。
- **上游新增库**（站方 v0.2+ 或同类库）：同 spec schema 可直接并入本库；结构不同的另立 solution，勿在本库混装。
- **转正**：完成一次真实剧集「分镜选型→绑定→出图/出片→人审」回执后，按仓库版本命名政策去 beta 后缀、版本重置 `1.0.0`。
