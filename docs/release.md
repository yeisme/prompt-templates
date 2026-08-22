# 发布与验证

结构化 metadata 由 Template Registry CLI 生成：

```bash
template-registry catalog build --repository . --json
template-registry catalog validate --repository . --json
```

同一输入必须生成相同 solution/template/catalog digest。正文、tags、capabilities、rights 或 locale 变化需要重新 build，并通过 pull request review。已发布版本不原地修改；创建新 version 并保留 replacement/rollback 说明。

当前仓库保持 private。公开前需要单独决定内容许可、代码/Schema 许可和签名策略。

首批内容统一保持 `exploratory`。`first-support` 不是编辑完成标记，必须同时具备 fixture 执行、人工评审、rights 结论和已知失败记录；`mature` 还要求真实脱敏使用证据和稳定修复历史。
