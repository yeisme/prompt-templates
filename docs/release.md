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

## Graph Kit first-support release

`graph/longform.generic.v2@1.0.0` 已完成一次本地结构化闭包 canary：catalog、
document/fixture、closure validate、Git export 和 restore 均通过；Registry 只输出
exact refs/digests，不输出模板正文。Auctra 消费端另行验证了 preview → apply →
review accept → rollback，双方不共享项目内容。

Graph Kit 此次记录仍只证明本地 release lock 与 evidence；它没有因为仓库公开或其它
solution 被推送而自动获得独立 immutable release。任一 child digest 变化必须创建新
版本，不能就地替换已发布 `1.0.0`。

首批内容统一保持 `exploratory`。`first-support` 不是编辑完成标记，必须同时具备 fixture 执行、人工评审、rights 结论和已知失败记录；`mature` 还要求真实脱敏使用证据和稳定修复历史。
