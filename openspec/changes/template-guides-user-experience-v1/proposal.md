# Why

用户需要全库逐个教程，并从 CLI/MCP 获取与精确模板对应的使用说明。现有帮助、内置 Skill 与文档存在漂移。

# What Changes

增加可选指南读取合同、显式导出/resource 访问、来源一致性校验，补齐全库教程与 Skills。保持原接口、模板及许可不变。

# Capabilities

## New Capabilities
- `template-guides`: 完整教程的安全读取和使用。

## Modified Capabilities

无破坏性修改。

# Impact

SDK 拥有来源合同，Registry 拥有 CLI/MCP，模板库拥有正文，Skills 真源拥有交互。仅本地验证；不发布、不部署、不调用 Provider。
