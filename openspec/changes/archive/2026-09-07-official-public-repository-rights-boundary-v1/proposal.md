## Why

GitHub 仓库已经公开，但发布文档仍声明仓库 private，且仓库没有统一 LICENSE。用户可能把“公开可见”误解为所有模板、Schema、外部资产和用户素材都可自由复用。

## What Changes

- 明确 public visibility 与 content permission 分离。
- 保留每个 solution 的 `rights` 和 contract 的 `license/permissions`，不批量改写为开源。
- 分开说明外部仓库许可、软件许可、媒体许可和用户素材权利。
- 修正过时的 private repository 发布说明。

## Capabilities

### New Capabilities

- `public-repository-rights-boundary`: 公开目录的可见性、模板权限和外部资产权利可分别审查。

### Modified Capabilities

- `official-prompt-release`: public repository 发布不得暗示 restrictive solution 已获得开放复用许可。

## Impact

不改变 solution、contract、catalog schema 或 digest。只修正文档和 release governance；任何未来 rights/license 放宽仍需逐 solution 决策和新版本。
