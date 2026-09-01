# official-prompt-i18n Specification

## Purpose
TBD - created by archiving change official-prompt-catalog-foundation-v1. Update Purpose after archive.
## Requirements
### Requirement: zh-CN 必须是 source locale

每个首发 solution SHALL 提供完整 zh-CN title、summary、usage 与 main Prompt。en SHALL 保持输入契约、限制和输出结构等价，并由人工 review。

#### Scenario: 用户显式请求英文

- **WHEN** consumer 使用 `--locale en`
- **THEN** catalog SHALL 返回英文 title/summary/body ref
- **AND** machine ID、tag、capability 和 ref SHALL 保持英文稳定值而非本地化副本。

### Requirement: 缺失语言必须显式 fallback

消费者无法获得 requested locale 时 SHALL 明确 requested/resolved locale，不得静默声称翻译存在。

#### Scenario: 英文版本缺失

- **WHEN** en body 不存在而 zh-CN 可用
- **THEN** result SHALL 显示 fallback 到 zh-CN
- **AND** SHALL NOT 将自动翻译标记为 reviewed。

