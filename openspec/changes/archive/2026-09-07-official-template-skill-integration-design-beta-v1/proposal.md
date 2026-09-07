## Why

跨图片、视频、文档、剪辑和 Agent 工具链的集成需要一个可版本化的语义设计模板。仅靠 Skill 指令无法形成可编译、可确认、可导出的 Integration Brief。

## What Changes

- 新增 `agent/template-skill-integration-design-beta@1.0.0-beta.1` 英文 Agent 模板。
- 新增九字段英文 contract、中文显示 metadata 和人工审阅译文。
- 输出覆盖 asset 分类、用户问题、owner、tags/capabilities、recipe、持久化、编译、安装和交接。

## Capabilities

### New Capabilities

- `template-skill-integration-brief`: Provider-free reusable integration brief compilation.

### Modified Capabilities

None.

## Impact

本模板只输出语义 proposal，不执行工具或 Provider。实际 authoring 由 Template Registry CLI，实际工作流由 `template-registry-integration-designer` 和领域 owner 完成。
