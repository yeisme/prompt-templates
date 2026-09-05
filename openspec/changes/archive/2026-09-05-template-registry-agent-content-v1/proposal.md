## Why

外部 Agent 需要可以严格编译并携带来源资料的基础模板，同时必须保留已发布引用。

## What Changes

- 新增结构化总结、会议纪要、证据研究简报的 v2 后继方案和双语合同（2026-09-05 落地为 `-beta` 目录与 `2.0.0-beta.1` 版本，遵循新命名规则；见 `official-ai-drama-character-assets-v1-promotion`）。
- 使用 Registry CLI 生成 metadata、catalog 和研究到总结的多步骤方案。
- 保留原有模板正文、权限和许可，成熟度保持 exploratory。

## Capabilities

### New Capabilities
- `agent-compilable-content`: 独立 Registry 消费的官方基础模板。

### Modified Capabilities

无。

## Impact

内容 owner 只提供模板与声明。会话、导入和编译实现属于 Registry；实验包合同属于 promptrepo。
