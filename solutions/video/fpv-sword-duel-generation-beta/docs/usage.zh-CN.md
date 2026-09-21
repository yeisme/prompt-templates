# 使用指南：电影级穿越机刀战视频生成

## 适用目标

生成双人电影级刀剑对拼视频 Prompt：首帧构图锁定、双人物身份锁定、两套一眼可区分且绑定刀路的特效、穿越机环绕镜头、可读攻防、以及「A 压制 / B 不败」的收束。

与家族内其他模板的边界：

| 需求 | 模板 |
| --- | --- |
| 特效/技能/大招镜头（法阵、清屏） | `ai-drama-shot-video-generation` |
| 双人物写实格斗（无特效、ACT 跟随） | `realistic-fight-scene-generation` |
| 穿越机环绕 + 双色刀气对拼（本模板） | `fpv-sword-duel-generation-beta` |
| 无台词纯环境音抓拍 vlog | `realistic-vlog-shot-generation` |
| 画外 VO 自述 + 音乐弧线 | `realistic-docu-vlog-generation` |
| 出镜口播 + 唇形同步 | `realistic-diary-vlog-generation` |

## 渲染流程

1. 将第 0 秒双人构图参考图登记为资产，取得 `first_frame_ref`（建议投递槽位 `@image1`）。
2. 按 contract 填写 32 个输入；`scenario_summary`、`fighter_a_identity`、`fighter_b_identity`、`scene_desc`、`scene_layout`、`fight_beats` 为 sensitive 创作内容。
3. 渲染 `main.en.md`（本 solution 为单语言 `en` 模板，locale 政策见仓库 `docs/locale-policy.md`；中文阅读版见 `docs/template-zh-CN.md`，仅供人工审阅不进编译）。变量内容可填中文。
4. 按 `review-checklist.zh-CN.md` 人工审查后投递；权限为 `execute_requires_review`。

## 结构要点

- **第 0 秒就是参考图**：`first_frame_ref` 同时锁构图和人物视觉；先按 `first_frame_hold_s` 钉住，再进入穿越机环绕。
- **特效必须跟刀走**：`fighter_a_vfx` 与 `fighter_b_vfx` 一眼可区分；`vfx_binding_rules` 把刀气绑在刀路、转体、步法和对拼上，禁止无源爆炸。
- **穿越机不是乱飞**：`camera_language` 声明允许的绕拍集合；始终能读出左右站位和攻防。正面人脸不是默认机位。
- **弧线是压制而不是击倒**：`fight_arc` 必须让 A 保持压迫、B 被压但不败、不失风度；结尾悬念保留。
- **破坏有质量**：`environment_destruction` 写清哪些物件可碎、碎到什么程度；碎片沿冲击方向走。

## Provider 兼容

Provider 名只作兼容信息：`provider_banner` 可选；首帧位置引用建议 `@image1`，投递时图像槽位与引用一致。完整绑定示例见 `examples/ruined-city-fpv-wuxia-duel.zh-CN.md`。

## 成熟度说明

当前 maturity 为 `exploratory`，目录与版本带 `beta`。Registry fixture 机制要求 JSON schema 化输出，本 solution 输出为渲染后的 Prompt 正文，暂不套用；待消费方定义语义输出 schema 后补 fixture 并申请升级 `first-support`。
