## Why

Auctra 只有内置 experimental Graph Kit，没有可由 Promptrepo Git/GitHub source 获取、由 Registry 原子发布和回滚的官方通用 solution。需要一个中文优先、跨题材、完整 closure 的官方 longform Graph Kit，才能完成真实 first-support 升级/回滚验收。

## What Changes

- 新增 `longform.generic.v2` 官方 solution，包含 Graph Kit manifest、source adapters、lens、views、validators、schemas 和 synthetic fixtures 的完整 closure。
- `zh-CN` 为 canonical 内容，首个版本不要求未审阅英文适配。
- 内容覆盖十面板、legacy migration guidance、planning/canon separation、stale/cache、gap review 和安全输出约束，但不包含任何真实小说人物、剧情、路径或 Overlay。
- `solution.json`、document descriptors、schemas/compiler profiles、fixture manifest、catalog 和 release metadata 全部由 Template Registry CLI 生成；Prompt/guide prose 可人工编辑。
- maturity 首发为 `first-support` 仅表示官方 Kit 内容/closure 通过 owner 验证，不替代 Auctra domain acceptance。

## Capabilities

### New Capabilities

- `official-longform-graph-kit`: 官方中文长篇 Graph Kit solution 内容、完整 closure、fixtures、rights 和 maturity。

### Modified Capabilities

- 无。

## Impact

- 新增官方 solution 目录及 CLI-authored contracts/fixtures/catalog entries。
- 依赖 Promptrepo Graph Kit conformance 和 Registry structured release closure。
- 不执行 provider、GitHub push、公开 release 或 Nishi 内容上传。
