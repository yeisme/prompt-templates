# official-ai-drama-isolated-visual-assets Specification

## Purpose
TBD - created by archiving change official-ai-drama-isolated-visual-assets-v1. Update Purpose after archive.
## Requirements
### Requirement: 系统必须提供零人物背景兼容模板
系统 MUST 提供 `clean-background-plate-v1`，固定 `subject_count=0` 和完整不透明画布。新的可拆物件和空场景壳语义由模块化 v2 模板定义。

#### Scenario: 背景输入包含人形痕迹
- **WHEN** 输入包含人物、人影、倒影、剪影、雕像、人体模特、人物照片或海报
- **THEN** 校验返回 blocking finding

### Requirement: 人物和背景必须保持运行隔离
人物和背景 MUST 使用独立 job、run 与 review artifact；基础资产阶段 MUST NOT 合成。

#### Scenario: 同一请求要求人物与背景成品图
- **WHEN** 基础资产请求同时要求人物和完整场景合成
- **THEN** validation 返回隔离 finding 或拆分建议
- **AND** 不得创建一个同时承担人物与背景 canonical 职责的基础资产

