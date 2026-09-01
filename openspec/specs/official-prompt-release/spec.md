# official-prompt-release Specification

## Purpose
TBD - created by archiving change official-prompt-catalog-foundation-v1. Update Purpose after archive.
## Requirements
### Requirement: Catalog 必须由 CLI 确定生成

Repository、solution 和 catalog structured metadata SHALL 由 Template Registry CLI 生成。相同输入 SHALL 产生相同 template、solution 与 catalog digest。

#### Scenario: 重新构建未变化仓库

- **WHEN** 维护者连续两次 build 且正文/metadata 未变化
- **THEN** catalog digest SHALL 相同
- **AND** validate SHALL 通过。

### Requirement: 发布必须可回滚且不泄露敏感信息

Release SHALL 固定 Git commit/tag、catalog digest 与 solution versions。仓库 MUST NOT 包含 credential、用户私有 Prompt、Provider payload、数据库、cache 或完整思维链。

#### Scenario: 公开许可尚未决定

- **WHEN** license/signing 仍未决
- **THEN** repository SHALL 保持 private
- **AND** MUST NOT 声称已完成公共供应链发布。

