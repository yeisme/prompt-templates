## 1. 依赖与内容边界

- [x] 1.1 固定 `longform.generic.v2` identity、rights、maturity、compatibility 和 atomic child closure 清单。
- [x] 1.2 确认 Promptrepo Graph Kit conformance 与 Registry structured authoring/release commands 可用。
- [x] 1.3 编写中文 source guide/template prose，覆盖十面板、状态分离、legacy migration、stale/cache、gap review、安全输出和 rollback。

## 2. CLI-authored solution closure

- [x] 2.1 使用 Registry catalog commands 创建 solution/template metadata，不手写 `solution.json` 或 digest。
- [x] 2.2 使用 Registry document commands 创建 descriptor、schemas 和 declarative compiler profile。
- [x] 2.3 使用 Registry fixture commands 创建 cross-genre valid 与 migration/digest/stale/HTML failure cases。
- [x] 2.4 使用 Registry release commands 生成完整 atomic closure、Git tree 和 release lock；不 push/publish。

## 3. 验证与 handoff

- [x] 3.1 运行 catalog build/validate、fixture/document/release validate 和 private-content sentinel scan。
- [x] 3.2 由 Auctra 使用 exact local release 完成 preview/apply/accept/rollback conformance。
- [x] 3.3 更新内容 docs，运行 `openspec validate official-longform-graph-kit-v1 --strict --no-interactive`，记录 exact refs/digests handoff。**Evidence (2026-09-01):** Registry release `srel_7f617a8ec4a7e367d961aa61`，closure `sha256:52e3efaf8a18b761500a715f0a86e2ae70f8578268c2540e5f47f5138206b0c7`，release `sha256:c747eb3bb00e33a29547d0d18639e51cbb605bea6227561d10d5a8f707adffbf`，Git revision `013b1f6bb327e463bd8a6c2d93b1bd8f94c52c3e`；无远端写入。
