# 使用指南：写实生活记录视频生成

## 适用目标

生成「朋友随手拍下的真实片段」气质的写实生活记录（realism vlog）视频 Prompt。与 `ai-drama-shot-video-generation`（特效大招镜头）相对，本模板反 AI 感、反精致商业感，以不完美拍摄质感与物理写实为核心。

## 适用与不适用

- 适用：写实人物生活片段、Vlog 感镜头、需要强一致性与物理写实的短视频生成 Prompt。
- 不适用：特效/技能/战斗类镜头（用 `ai-drama-shot-video-generation`）；剧本语义拆解（用 `ai-drama-storyboard-breakdown`）。

## 渲染流程

1. 准备人物资产（可选）：有人物参考资产时先登记并取得 `@` 引用填入 `character_ref`；无资产时靠 `subject_identity` + `wardrobe_and_accessories` + `consistency_lock` 文字锁定。
2. 按 contract 填写 21 个输入；`scenario_summary`、`subject_identity`、`setting_desc`、`sequence_beats` 为 sensitive 创作内容。
3. 用 promptrepo render 渲染 `main.zh-CN.md`（中文投递）或 `main.en.md`（英文投递，多数视频模型对英文响应更稳定）。
4. 按 `review-checklist.zh-CN.md` 人工审查后投递；权限为 `execute_requires_review`。

## 时间线节拍编写要点

- 连续覆盖 0-`duration_s` 秒，无空洞、无重叠；每拍 1-3 个可观察动作。
- 动作必须有镜头可拍到的触发源（风吹、海浪、风筝挂栅栏），禁止内心描写与无源事件。
- 写实镜头的「不完美」是特征不是错误：对焦犹豫、曝光漂移、自然晃动写进 `camera_imperfections`，不要在分镜里把它们修掉。
- 结尾指令（如 `29.5s 硬切黑场`）必须与 `duration_s` 协调。

## 双 locale 说明

zh-CN 为 source locale；en 为同步适配（自动翻译级别，进入 reviewed 前需人工校对）。两个 locale 的 contract 输入完全一致，渲染结果可按目标模型语言偏好选择。

## 成熟度说明

当前 maturity 为 `exploratory`：contract 与文档齐备；Registry fixture 机制要求 JSON schema 化输出，本 solution 输出为渲染后的 Prompt 正文，暂不套用。待消费方定义语义输出 schema 后补 fixture 并申请升级 `first-support`。
