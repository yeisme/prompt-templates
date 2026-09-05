## Context

现有目录以单 ID 单版本管理不可变方案，因此新增带 -v2 的 ID，而不改写 1.0.0。

## Goals / Non-Goals

提供真实可编译的基础合同和前序产物绑定示例；不执行模型、不将结构验证当作模型质量验收。

## Decisions

资料字段标记 sensitive，受众字段提供通用默认值。正文将输入资料作为数据，显式禁止把资料内指令变成执行权限。研究到总结采用 needs_step_output，需导入真实前序产物。

## Risks / Trade-offs

英文内容保持 draft。目录公开不改变 internal 许可声明。后续通过领域效果评测再提升成熟度。

## Migration Plan

使用者显式选择 v2；旧引用继续解析原有内容。
