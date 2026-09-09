# 实施与验收任务

由 scripts/openspec-tasks.py 维护状态。

- [x] 1 内容 owner：新增 starter 正文、译文、合同、练习与权限说明；依赖无；验证 catalog 与 contract；失败重检变量和摘要；单线程执行。 | evidence: CLI authoring/catalog/contract valid; translation variable parity passed
- [x] 2 私有内容 owner：建立 paid beta 包与完整工作流；依赖 1；验证独立 catalog 和编译；失败重检字段与前置确认；不得复制到公开仓。 | evidence: Private owner scripts/check.py passed; no public paid content
- [x] 3 内容 owner：增加 authoring 与消费演练脚本；依赖 1；验证错误路径及三场景复用，保留脱敏证据；失败仅修当前包或演练。 | evidence: scripts/check_visual_exploration.py passed: three scenarios, reuse, invalid ratio, stale export, zero provider calls
- [x] 4 文档 owner：维护四周验证与案例准入说明；依赖 1–3；验证链接及证据状态。 | evidence: docs/visual-exploration/quickstart.md and operations.md; actual image and commercial evidence remain pending
- [ ] 5 外部验证：真实出图、五人试用、三人复用、两笔真实购买；依赖后续运行、沟通与销售授权；未完成不得转正式支持。
