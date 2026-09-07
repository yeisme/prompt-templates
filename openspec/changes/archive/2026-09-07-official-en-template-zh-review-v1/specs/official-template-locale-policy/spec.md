## ADDED Requirements

### Requirement: 新 Agent solution 必须只注册英文模板
官方内容仓 SHALL 对新 Agent 可编译 solution 只注册 `en` template 与 contract。

#### Scenario: 创建新 solution
- **WHEN** maintainer 使用 Template Registry CLI 注册新方案
- **THEN** `templates` SHALL 只包含英文 role
- **AND** 中文说明 SHALL 通过 localized display text 与 review document 提供

### Requirement: 中文审阅译文不得进入编译
`docs/template-zh-CN.md` MUST NOT 出现在 catalog template path 或 companion contract identity 中。

#### Scenario: catalog build
- **WHEN** solution 同时有英文模板和中文审阅文档
- **THEN** catalog SHALL 只列出英文模板

### Requirement: 已发布引用不得原地断代
已发布双语 solution MUST 保留旧 exact ref，迁移 SHALL 通过新版本完成。

#### Scenario: 未发布方案收口
- **WHEN** origin/main 不包含该 solution
- **THEN** maintainer MAY 在首次发布前移除中文 template binding
