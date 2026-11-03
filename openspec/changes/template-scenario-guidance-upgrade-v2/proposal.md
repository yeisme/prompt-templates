# Why

第一轮覆盖了全库教程，但业务输入有占位值，读取粒度过大，独立用户缺少受保护升级路径。

# What Changes

全库有效案例、分段教程与英文后继 recipe。复用现有 fixture 与应用服务，所有案例是数据，不执行 Markdown。

# Capabilities

## New Capabilities
- `scenario-guidance-upgrade`: 有效案例、按需指南与可靠升级。

## Modified Capabilities

旧全文读取、原 FixtureSet 规则和历史 recipe 保留。

# Impact

内容、SDK、Registry 和 Skills 各自维护真源。CLI/MCP 增量字段兼容；安装基线由本地 CLI 写入，无数据库业务迁移。无发布、部署或付费调用。
