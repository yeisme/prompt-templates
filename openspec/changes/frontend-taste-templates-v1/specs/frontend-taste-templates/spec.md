# 前端 Taste 模板

## ADDED Requirements

### Requirement: 唯一 owner 与可复现交接
系统 SHALL 使用固定版本和明确合同，并保留 canonical owner。

#### Scenario: 跨入口接续
- **WHEN** 已有任务从 CLI 切换到 MCP 或 DSH
- **THEN** 使用原引用、revision 和固定内容，不复制私有领域状态

### Requirement: 显式执行与证据
系统 SHALL 区分编译、执行、用户采纳与远端发布。

#### Scenario: 本地验证
- **WHEN** 编译或 fixture 验证通过
- **THEN** 不将其标记为模型执行、浏览器设计质量或生产发布
