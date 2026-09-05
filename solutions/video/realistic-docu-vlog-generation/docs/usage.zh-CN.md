# 使用指南：写实纪实 Vlog 视频生成（VO 旁白一日记录）

## 适用目标

生成「主人公自述一天」的写实纪实 Vlog Prompt：逐拍旁白（VO）、音乐弧线、每拍可切换的混合机位（DV 跟拍/自拍/固定机位/蒙太奇）。与 `realistic-vlog-shot-generation`（无旁白、纯环境音、单一拍摄风格）互补：只要内容需要 VO 自述或配乐弧线，就用本模板。

## 适用与不适用

- 适用：一日记录、演出/活动幕后自述、人物纪实短片等 VO 驱动的写实视频。
- 不适用：无旁白纯抓拍 vlog（用 `realistic-vlog-shot-generation`）；特效大招镜头（用 `ai-drama-shot-video-generation`）。

## 渲染流程

1. 有人物参考资产时登记并取得 `@` 引用填入 `character_ref`。
2. 按 contract 填写 24 个输入；`scenario_summary`、`subject_identity`、`story_beats`、`voiceover_script` 为 sensitive 创作内容。
3. 渲染 `main.en.md`（本 solution 为单语言 `en` 模板，locale 政策见仓库 `docs/locale-policy.md`；中文阅读版见 `docs/template-zh-CN.md`；变量内容语言与骨架 locale 独立，可填中文值）。
4. 按 `review-checklist.zh-CN.md` 人工审查后投递；权限为 `execute_requires_review`。

## 结构要点

- **节拍即调度单**：每拍必须含时间区间、拍摄格式（只能取 `camera_formats` 声明的集合）、1-3 个可观察动作、VO 绑定键；蒙太奇拍列 3-5 个快切画面。
- **VO 逐字锁定**：`voiceover_script` 的文本渲染后不得改写；每句通过绑定键落到节拍；VO 只进音轨，绝不产生字幕。
- **音乐弧线对齐结尾**：`music_arc` 的高潮点必须与 `ending_directive` 协调（如结尾拍音乐 peak + 强光 + 切黑）。
- **无文字铁律**：字幕/标题/UI/Logo/水印禁令同时出现在 VO 规则、全局约束与负面提示词三处；摄像机不入境（含镜面反射）。

## Provider 兼容

Provider 名只作兼容信息：`provider_banner` 可选保留平台标识行；资产引用接受 `@uuid` 与 `@image1` 位置引用。完整绑定示例见 `examples/kpop-show-day.zh-CN.md`。

## 成熟度说明

当前 maturity 为 `exploratory`。Registry fixture 机制要求 JSON schema 化输出，本 solution 输出为渲染后的 Prompt 正文，暂不套用；待消费方定义语义输出 schema 后补 fixture 并申请升级 `first-support`。
