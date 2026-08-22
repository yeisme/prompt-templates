## Why

中文用户需要按任务快速找到可直接使用、可评审、可复现的 Prompt 方案，而不是在模型名和零散字符串中搜索。官方仓库需要建立十二类中文优先导航、英文同步适配和 CLI 生成的稳定 catalog。

## What Changes

- 建立独立官方内容仓库和维护边界。
- 定义十二类 taxonomy、namespace tags、solution package 和 maturity。
- 首发每个类目一个中英双语 solution，共十二个常见方案。
- 通过 Template Registry CLI 生成 repository/solution/catalog structured metadata。
- 建立中文 source、英文 reviewed adaptation、版本、digest、rights 和发布治理。

## Capabilities

### New Capabilities

- `official-prompt-solutions`：十二类中文优先 Prompt 解决方案内容。
- `official-prompt-i18n`：zh-CN source、en adaptation 与 locale fallback。
- `official-prompt-release`：确定性 catalog build/validate、版本和回滚。

### Modified Capabilities

- 无。

## Impact

- 远程仓库：`https://github.com/yeisme/prompt-templates`，初始 private。
- 消费合同：`promptrepo.catalog.v0.1` 与 `promptrepo://` exact refs。
- 维护依赖：Template Registry `repository`、`solution`、`catalog` commands。
