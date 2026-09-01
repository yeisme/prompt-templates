## ADDED Requirements

### Requirement: 官方目录必须覆盖十二类中文导航

仓库 SHALL 提供 general、writing、image、video、audio、research、product、marketing、office、engineering、agent 与 learning 十二个 primary categories。每个首发类目 SHALL 至少有一个完整 solution package。

#### Scenario: 用户浏览音频类目

- **WHEN** consumer 按 `category:audio` 搜索
- **THEN** catalog SHALL 返回中文播客旁白方案及其输入、能力、rights 和 maturity
- **AND** SHALL NOT 要求用户先选择模型或 Provider。

### Requirement: Solution 必须包含可执行合同

每个 solution SHALL 包含目标、输入变量、强约束、输出结构、自检、失败回退、tags、capabilities、rights 和 maturity。只有 Prompt 字符串的条目 MUST NOT 进入 first-support catalog。

#### Scenario: 缺少 rights

- **WHEN** solution metadata 没有 rights
- **THEN** catalog validation SHALL 失败
- **AND** 条目不得发布为 first-support。
