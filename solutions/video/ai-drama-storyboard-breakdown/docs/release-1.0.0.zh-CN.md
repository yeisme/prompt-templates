# 1.0.0 internal release candidate

## 结论

`video/ai-drama-storyboard-breakdown@1.0.0` 已通过本地 internal/exploratory release-candidate gate，可进入维护者后续的 Git immutable release 流程。当前 solution 保持：

- rights：`internal`；
- maturity：`exploratory`；
- exact solution ref：`promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0`；
- catalog digest：`sha256:f2ee99e6316530669753907f603a72bffaeb8d3d4d8178c3d7384d837c355122`。

本次任务没有 commit、tag、push、publish，也没有创建公开供应链发布；因此本文件记录的是已验证的 release candidate，不冒充已经完成的 immutable release。

## 验证摘要

- 中文 main/repair contract 分别为 12/13 inputs，template digests 为 `sha256:6817dc387a99f04a0ea81c66f2713ec41be63576052f50cbd47199e61adec4d9` 与 `sha256:e985526d747415fce8163d69d0a187c966c4f3b6ff85e3fdf9d5ae5f47dcaddd`。
- 英文 main/repair contract 分别为 12/13 inputs，template digests 为 `sha256:4ac12800275c376a907e8ce852e59601eeba72077729a8cff12faa85050de379` 与 `sha256:55b4abf62e956b13cfb87ce5ed8f8c695c1ba964db7d58eeb83a94f4295f1434`；英文文档显式追踪对应中文 source digests。
- Schema digest：`sha256:372dbe848d2961538f4efc8a69b6fc380805cfca9181007af79f03cb9da81e04`；compiler profile digest：`sha256:c45c33ccb12f6fbb0c023ad73a724aba3794f503ac4aac416d58725264171625`。
- main fixture manifest digest：`sha256:a08b321e9ec374bd81c4338c5870a85e2e317800bd9ece73dc888ef33918dff3`，共 16 例，其中 6 valid、10 invalid；广告 claim 缺少已知证据时精确返回 `CLAIM_EVIDENCE_MISSING`。
- repair fixture manifest digest：`sha256:325609cb8726894d313d637b7f8cd524a3c7cdd74be5c5ce9674aecc48690254`，共 3 例，其中 2 valid、1 invalid。
- Scaena evidence：`agent/scaena/temp/integration-test-runs/20260831-014817.682201358-system-3378671-1/`，覆盖四profile、exact input/output bytes与digests、invalid exact reason codes、广告 claim 证据缺失、source injection canary、revision lineage、bounded repair和未受影响shots保持，provider calls=0。
- catalog 连续两次 build digest 一致，随后 validate 通过；对应 OpenSpec strict validation 通过。

## Rights 与质量边界

示例与文档使用原创虚构片段，不包含受保护长对白、在世导演 persona、真实用户文本、credential、Provider payload、隐藏系统 Prompt 或完整思维链。该 solution 只负责生成可审查的语义计划，不负责 accept、费用、模型选择、Provider 调用或 production 状态。

当前 provider-free conformance 证明结构、约束与确定性，不证明 live model 质量。四个 profile 继续保持既有 exploratory/candidate 边界，不应据此整体提升为 production-ready。

## Immutable release 与回滚

维护者若后续授权正式 internal release，应固定 Git commit/tag、上述 catalog digest 与 solution version，不得原地覆盖 `1.0.0`。发布前发现问题时直接撤回 candidate；发布后发现问题时恢复上一已知良好的 Git/tag 与 catalog mapping，并以新版本发布修复，保留 `1.0.0` digest lineage。
