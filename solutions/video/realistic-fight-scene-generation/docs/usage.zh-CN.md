# 使用指南：写实近身格斗视频生成（双人物 ACT 跟随）

## 适用目标

生成无特效、强物理的双人写实近身格斗视频 Prompt：双参考图身份锁定、攻防物理可审查、行动轴线与空间连续性、ACT 第三人称跟随镜头。

与家族内其他模板的边界：

| 需求 | 模板 |
| --- | --- |
| 特效/技能/大招镜头（法阵、剑气、清屏） | `ai-drama-shot-video-generation` |
| 无台词纯环境音抓拍 vlog | `realistic-vlog-shot-generation` |
| 画外 VO 自述 + 音乐弧线 | `realistic-docu-vlog-generation` |
| 出镜口播 + 唇形同步 | `realistic-diary-vlog-generation` |
| 双人物写实格斗（本模板） | `realistic-fight-scene-generation` |

## 渲染流程

1. 两组人物参考图先登记为资产，分别取得 `protagonist_ref` 与 `antagonist_ref`；两者必须不同。
2. 按 contract 填写 29 个输入；`scenario_summary`、`protagonist_identity`、`antagonist_identity`、`scene_desc`、`scene_layout`、`fight_beats` 为 sensitive 创作内容。
3. 渲染 `main.en.md`（本 solution 为单语言 `en` 模板，locale 政策见仓库 `docs/locale-policy.md`；中文阅读版见 `docs/template-zh-CN.md`，仅供人工审阅不进编译）。
4. 按 `review-checklist.zh-CN.md` 人工审查后投递；权限为 `execute_requires_review`。

## 结构要点

- **节拍即动作设计稿**：每拍含时间区间、机位、攻防动作（起点/路径/接触点/结果）、隐形切点、向下一拍延续的惯性/位置/朝向/伤势。
- **空间连续性是一等约束**：`scene_layout` 写清开场站位、移动路径与行动轴线；切镜不改变地物位置，不越轴（除非环绕镜头明确展示换位）。
- **攻守平衡**：`fight_arc` 必须让主角经历失势与危险化解；禁止无伤碾压与木桩敌人，已写入固定规则与默认负面项。
- **环境参与有损毁边界**：`environment_interaction` 写明哪些物件可被撞、损毁到什么程度（如闸机挡板可弯曲不脱离、玻璃震颤不碎）。
- **ACT 感≠游戏 UI**：血条/准星/按钮/速度线/子弹时间在全局约束与负面提示词双重封禁。

## Provider 兼容

Provider 名只作兼容信息：`provider_banner` 可选；位置引用建议主角 `@image1`、敌人 `@image2`，投递时图像槽位顺序与引用一致。完整绑定示例见 `examples/rain-night-station-fight.zh-CN.md`。

## 成熟度说明

当前 maturity 为 `exploratory`。Registry fixture 机制要求 JSON schema 化输出，本 solution 输出为渲染后的 Prompt 正文，暂不套用；待消费方定义语义输出 schema 后补 fixture 并申请升级 `first-support`。
