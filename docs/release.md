# 发布与验证

结构化 metadata 由 Template Registry CLI 生成：

```bash
template-registry catalog build --repository . --json
template-registry catalog validate --repository . --json
```

包含 companion contract 的 solution 还需运行：

```bash
template-registry contract validate --repository . --package image --id xhs-product-cover --role main --locale zh-CN --json
template-registry contract validate --repository . --package image --id xhs-product-cover --role main --locale en --json
template-registry contract validate --repository . --package image --id xhs-product-cover-v2 --role main --locale en --json
template-registry contract validate --repository . --package audio --id podcast-narration --role main --locale zh-CN --json
template-registry contract validate --repository . --package audio --id podcast-narration --role main --locale en --json
```

contract sidecar 绑定 template digest，但不进入 catalog digest。Prompt 正文变化后必须先重新生成/更新 contract，再通过 contract validate；不得通过手工修改 digest 绕过校验。

同一输入必须生成相同 solution/template/catalog digest。正文、tags、capabilities、rights 或 locale 变化需要重新 build，并通过 pull request review。已发布版本不原地修改；创建新 version 并保留 replacement/rollback 说明。

当前仓库公开可读，但 GitHub visibility 不改变 solution 的 `rights` 或 contract 的 `license/permissions`。仓库不设置一个覆盖全部内容的统一开源许可；发布时必须保留逐 solution 权限、外部资产许可和用户素材权利的边界，详见 `RIGHTS.md`。

## Graph Kit 版本验证

本地验证与公开发布应分别记录。发布 Graph Kit 前，需要验证 catalog、文档、fixture、结构化闭包、导出和恢复，并核对消费方的预览、应用、接受和回滚流程。

本地 release lock 或验证证据不能代替可获取的正式版本。已发布内容的任一子项 digest 变化都需要创建新版本，不能原地替换已发布 `1.0.0`。

首批内容统一保持 `exploratory`。`first-support` 不是编辑完成标记，必须同时具备 fixture 执行、人工评审、rights 结论和已知失败记录；`mature` 还要求真实脱敏使用证据和稳定修复历史。
