# 使用说明

本 solution 用于把 Scaena 已切分、已编号的单集剧本 segments 转成 `storyboard.semantic_plan.v1`。它不直接读取任意文件，也不创建 Scaena candidate。

使用前必须具备：

- 一个 exact episode；
- 通过校验的 direction 与 profile；
- 完整、未截断且在 owner limits 内的 source segments；
- exact Prompt address、contract、document、Schema 和 fixture digests；
- compatible execution/data policy；
- 当前模型调用的独立批准。

推荐流程：provider-free inspect/validate → Scaena render snapshot → Scaena model run → Scaena deterministic compiler → findings/diff → 人工 review → accept 或 reject。

四类预设及其默认节奏、质量门和视觉资产 handoff 见 `preset-matrix.zh-CN.md`。分镜中的 `image_instruction` 应继续交给视觉资产 owner，并结合 `video/ai-drama-character-assets` 的主体、服装、参考角色和连续性模板生成可审查 Prompt Bundle。

本 solution 不负责 Provider 选择、费用、credential、重试策略、accept、export 或出图。
