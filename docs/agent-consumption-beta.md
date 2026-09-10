# 总结、会议纪要与研究简报模板（beta）

这三个方案适合需要整理现有资料的 Agent 用户。先提供原始资料与目标读者，再编译提示词，由 Agent 或模型生成结果。编译本身不会生成最终总结或研究结论。

| 方案 | 主要输入 | 目标产物 |
|---|---|---|
| general/structured-summary-beta | source_text、target_audience | 结构化总结提示词 |
| office/meeting-action-summary-beta | meeting_record、team | 会议纪要提示词 |
| research/evidence-research-brief-beta | sources、research_question、decision_maker | 证据研究简报提示词 |

三个方案的版本均为 `2.0.0-beta.1`，成熟度为 `exploratory`，真实模型输出质量仍需检查。使用前请查看各方案的 `solution.json` 和 contract 中的许可与权限；公开可读不自动授予执行或商用授权，详见[内容许可](../RIGHTS.md)。

## 使用步骤

1. 按[首页](../README.md)安装 Template Registry 并同步模板来源。
2. 请 Agent 查看目标模板的输入要求和使用许可，确认该版本可用且允许你的用途。
3. 提供自己的资料，核对受众等默认值。缺失信息应保留为待确认，不由 Agent 编造。
4. 确认输入后编译并导出提示包，再由 Agent 或模型执行提示。
5. 对照原始资料检查结果，尤其是事实、决定、负责人和未解决的问题。

模板为英文，中文资料可以作为输入。各方案的 `docs/template-zh-CN.md` 提供人工审阅译文。

## 虚构示例：会议纪要

输入资料：“周二例会决定先测试新封面。设计同事准备两个版本，完成时间尚未确定。下次会议讨论测试结果。”目标读者为项目团队。

合格结果应区分已确认决定、行动项和待确认信息：测试新封面是决定；准备两个版本是行动项；具体负责人姓名、截止日期和下次会议日期均未提供，应标为待确认。不能补出人名、日期或测试结论。

这段示例说明检查标准，不代表实际模型评测结果。

## 连续处理研究资料

`recipes/research-summary.json` 提供两步骤示例：先生成研究简报，再基于实际简报结果生成面向读者的总结提示。必须先导入第一步的真实结果；出现 `needs_step_output` 时，表示尚缺前一步输出。

如需查看完整的会话创建、确认、编译和导出命令，可参考[视觉探索入门指南](visual-exploration/quickstart.md)。不同模板的输入字段不同，应以目标模板返回的要求为准。
