# Agent 编译用基础模板 v2

新增结构化总结、会议行动纪要和证据研究简报三个兼容后继版本，目录以 `-v2` 结尾，版本为 `2.0.0`。已有 `1.0.0` 正文和引用保持不变，沿用当前 Registry 单 ID 单版本目录的维护方式。

三个方案均有 zh-CN/en 正文和 CLI 生成的 companion contract，明确资料边界、输入变量、输出要求、缺失信息回退与检查要点。正文要求将来源作为数据，不授予工具执行权限。

| 方案 | 主要输入 | 目标产物 |
|---|---|---|
| general/structured-summary-v2 | source_text、target_audience | 结构化总结提示词 |
| office/meeting-action-summary-v2 | meeting_record、team | 会议纪要提示词 |
| research/evidence-research-brief-v2 | sources、research_question、decision_maker | 证据研究简报提示词 |

通过 Template Registry 的 prompt inspect、session、source、compile、export 和 bundle verify 消费。资料字段为 sensitive，不提供默认真实内容；受众字段有可查看、可覆盖的通用默认值。

当前成熟度保持 exploratory，英文适配按 draft 管理。离线编译、输入校验和包验证不证明真实模型输出质量；不得直接升级为 mature。

`recipes/research-summary.json` 是 CLI 生成的两步骤示例：先生成研究简报，再用实际简报结果生成面向读者的总结提示。第一步结果尚未导入时，第二步保持 needs_step_output，不伪造中间结果。

目录和双语 contract 由 Registry CLI 构建/验证；消费 conformance 由 Registry 的 TestOfficialTemplateCompilationConformance 完成，证据保留在消费 owner。
