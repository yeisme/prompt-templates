# 使用指南：AI 短剧镜头级视频生成

## 适用目标

把「蓄力-爆发型大招镜头」的视频生成 Prompt 从一次性手写文章升级为可复用模板：角色、技能、敌方、场景、运镜、分镜全部参数化，渲染结果直接投递给支持资产引用（`@ref`）的视频生成模型。

## 适用与不适用

- 适用：AI 短剧/漫剧的单镜头或连续镜头视频生成 Prompt，尤其是有明确蓄力期与爆发期结构的大招镜头。
- 不适用：剧本到分镜的语义拆解（用 `ai-drama-storyboard-breakdown`）；多 Profile 生产编译与语义提案（用 `ai-film-multi-profile-production`）；角色/背景资产生成（用 `ai-drama-*-assets-v2`）。

## 渲染流程

1. 准备资产：角色、武器、敌方、场景资产需先在消费方资产库登记，取得稳定的 `@` 引用。
2. 按 contract 填写 28 个输入；其中 `character_core`、`ultimate_skill_visual`、`enemy_desc`、`enemy_counterattack`、`scene_desc`、`shot_list` 为 sensitive 创作内容，不进入日志与证据。
3. 用 promptrepo render 渲染 `main.en.md`，确认无残留占位符（本 solution 为单语言 `en` 模板；中文阅读版见 `docs/template-zh-CN.md`，仅供人工审阅不进编译）。
4. 按 `review-checklist.zh-CN.md` 人工审查渲染结果。
5. 投递视频生成模型；权限为 `execute_requires_review`，未经人工审查不得直接执行。

## 分镜表编写要点

- 时间区间连续覆盖 0-`duration_s` 秒，无空洞、无重叠。
- 每镜动作数 ≤ `max_actions_per_second`（默认 3）。
- 蓄力期镜头只写蓄力与敌方反击；爆发期写释放与清场；收尾镜头写余波与定格。
- 每镜注明运镜、冲击帧等级（一/二/三级）与隐形剪辑点（甩摇、遮挡、爆闪、盲区、CRANE）。

## 两层行为约束

模板把角色行为约束拆成蓄力期（`charge_phase_rule`）与爆发收尾期（`release_phase_rule`）两层，解决原始手写法中「全程悬空绝不落地」与「结尾落地收剑定格」互相矛盾的问题。填写时两层规则不得冲突；分镜中每个镜头的动作必须能归入对应阶段。

## 成熟度说明

当前 maturity 为 `exploratory`：contract 与文档齐备，但 Registry 的 fixture 机制要求 JSON schema 化输出，而本 solution 的输出是渲染后的 Markdown Prompt 正文，暂不套用结构化 fixture。待消费方（如 Scaena）定义镜头 Prompt 的语义输出 schema 后，再补 fixture set 并申请升级 `first-support`。
