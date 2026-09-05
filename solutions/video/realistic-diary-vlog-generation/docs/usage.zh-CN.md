# 使用指南：写实日记 Vlog 视频生成（出镜口播一日记录）

## 适用目标

生成「主人公亲自对镜头说话」的写实日记 Vlog Prompt：出镜台词 + 唇形同步 + 随地点变化的声学空间。写实 vlog 家族三个模板的选择规则：

| 需求 | 模板 |
| --- | --- |
| 无台词、纯环境音抓拍 | `realistic-vlog-shot-generation` |
| 画外 VO 自述（无唇形问题）+ 音乐弧线 | `realistic-docu-vlog-generation` |
| 对镜头直接说话、需要唇形同步 | `realistic-diary-vlog-generation`（本模板） |

## 不适用

特效大招镜头（用 `ai-drama-shot-video-generation`）；剧本语义拆解（用 `ai-drama-storyboard-breakdown`）。

## 渲染流程

1. 有人物参考资产时登记并取得 `@` 引用填入 `character_ref`。
2. 按 contract 填写 22 个输入；`scenario_summary`、`subject_identity`、`story_beats`、`dialogue_script` 为 sensitive 创作内容。
3. 渲染 `main.en.md`（本 solution 为单语言 `en` 模板，locale 政策见仓库 `docs/locale-policy.md`；中文阅读版见 `docs/template-zh-CN.md`；台词语言由 `dialogue_language` 独立声明，与模板 locale 无关，如英文模板 + 日语台词）。
4. 按 `review-checklist.zh-CN.md` 人工审查后投递；权限为 `execute_requires_review`。

## 结构要点

- **节拍即调度单**：每拍含时间区间、地点与声学空间、拍摄格式（限 `camera_formats` 集合）、1-3 个动作、台词绑定键；允许自然停顿与空镜呼吸。
- **台词逐字锁定**：`dialogue_script` 渲染后不得改写或翻译；口播是「偶尔的亲密自述」，不要每拍都说话；口播拍必须画面可见人物说话且唇形可信。
- **声学空间连续性**：`ambience_design` 必须写清各地点的声学特征（卧室近距安静/街道开阔混响/排练室反射声），room tone 全程存在。
- **服装逻辑**：一天内的换装链条（居家→外出→排练）每次都有日记事件支撑；同一场景内服装不漂移。
- **无文字铁律**：字幕/标题/UI/Logo/水印禁令出现在台词规则、全局约束与负面提示词三处；摄像机不入境（含镜面反射）。

## Provider 兼容

Provider 名只作兼容信息：`provider_banner` 可选保留平台标识行；资产引用接受 `@uuid` 与 `@image1` 位置引用。完整绑定示例见 `examples/japanese-idol-private-day.zh-CN.md`。

## 成熟度说明

当前 maturity 为 `exploratory`。Registry fixture 机制要求 JSON schema 化输出，本 solution 输出为渲染后的 Prompt 正文，暂不套用；待消费方定义语义输出 schema 后补 fixture 并申请升级 `first-support`。
