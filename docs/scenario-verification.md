# 第二轮有效案例与指南验证

2026-11-03，本地数据与工程检查完成：87 个方案、107 个英文角色、107 个正例、137 个反例。42 个角色引用已有语义 fixture；正文、合同、rights、maturity 和原 catalog digest 未改变。

教程和固定验证器都读取 CLI-authored tutorials/<role>.en.json。检查来源、类型、约束、JSON 结构、明确的空初始状态和预期拒绝码；已有输出 schema 按原绑定校验。旧 FixtureSet 的额外语义策略不被覆盖，无 schema 的内容检查保留人工待审。

[最终证据](../temp/integration-test-runs/20261103T044357Z-scenarios-191f843c/summary.json)：112 个指南读取、107 个编译/导出/校验闭环、137 个反例检查和两条多步骤流程通过；本地拒绝后端观测分析请求为 0，真实 Provider 验证未运行。

研究工作流新增 research-summary-en，原 research-summary.json 保留。研究→总结、Brief→镜头计划均导入明确标注的合成前序结果，验证原会话接续、修订冲突和上游修改后的下游失效。

目前仍有 7 个合法空 JSON，每项有业务说明；通用占位文案为 0。人工内容质量、真实用户体验、领域接受与模型效果不因编译或 schema 通过而升级。

维护与验证：

```bash
python3 scripts/tutorial_cases.py --registry ../../backend-server/template-registry/dist/template-registry
python3 scripts/author_guides.py
python3 scripts/tutorial_cases.py --check --registry ../../backend-server/template-registry/dist/template-registry
python3 scripts/author_guides.py --check
python3 scripts/check_guides.py --registry ../../backend-server/template-registry/dist/template-registry
```

前两条是作者操作，会通过 CLI 更新案例并重生成指南；后三条是检查。check_guides 不执行文档中的 shell，也不提供案例自定义命令。

宿主磁盘满曾中断一次复验，失败记录保留在 20261103T043303Z-scenarios-0c451601；最终使用内存临时盘重跑通过。
