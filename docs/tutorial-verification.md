# 全库教程验证

2026-11-03：87 个方案均有 docs/README.md 完整教程，107 个英文角色覆盖逐字段输入、合成 CLI 练习与等价 MCP 步骤。5 个历史图谱角色提供指南与领域交接，不伪装为通用编译。原有说明及专业链接保留。

```bash
python3 scripts/author_guides.py --check
python3 scripts/check_guides.py --registry ../../backend-server/template-registry/dist/template-registry
```

[最终证据](../temp/integration-test-runs/20261103T033551Z-guides-1e019215/summary.json)：112 个指南读取、107 个编译/导出/校验成功，provider_calls=0。该验证执行教程原文中的命令，确认来自合成用户输入，不代替真实用户决定。

catalog validate、可丢弃副本 catalog build 与 digest 不变检查、26 项 OpenSpec 验证通过。全部新增教程链接已检查；四个相关 Skill 和受影响 runtime/内置包一致。未改变模板正文、合同、rights 或 maturity。

语义复杂字段的 {} 演示传输形状，不是有效的已接受业务产物。已有 fixture 的教程链接其输出示例；最终模型效果与消费方接受需独立验证。
