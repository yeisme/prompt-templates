# 1.0.0 internal release candidate

## 结论

`video/ai-drama-character-assets@1.0.0` 已通过本地 internal/exploratory release-candidate gate，可进入维护者后续的 Git immutable release 流程。当前 solution 保持：

- rights：`internal`；
- maturity：`exploratory`；
- exact solution ref：`promptrepo://official/video/ai-drama-character-assets@1.0.0`；
- catalog digest：`sha256:f2ee99e6316530669753907f603a72bffaeb8d3d4d8178c3d7384d837c355122`。

本次任务没有 commit、tag、push、publish，也没有创建公开供应链发布；因此本文件记录的是已验证的 release candidate，不冒充已经完成的 immutable release。

## 验证摘要

- 中文与英文 `main` contract 均为 11 inputs，分别绑定 template digest `sha256:d588725273284c6220bd807a21c2719208a652e0d2d71275cfc93e384e8eb887` 与 `sha256:15980850c877b6b93dcdf52b4214f7280d1b1056ef865e90ecc1459602f1964c`。
- single-file JSON/YAML 的 canonical digest 相同：`sha256:9bf30747a50e7cab42b9a0a53b4995d403b91715978180b2e2252d687f6afa71`。
- 模块化 Character、Wardrobe、Task、Layout、QC 与 plan 共 6 个 exact source 已通过 descriptor、Schema/compiler binding 和 Scaena typed compile canary。
- fixture manifest digest：`sha256:d6f5b63c95fcf9f163210dfb7336373d001fa7d34eaf9f0d3b3745a9450ea7d7`；共29例，其中6 valid、23 invalid；新增 face master、body master、独立 turnaround，以及元 Prompt 直发、production grid、缺主视图负例；expression子矩阵仍为1 valid、9 invalid，另含duplicate-key与YAML alias strict-parser cases。
- Eikona evidence：`cli/eikona/temp/integration-test-runs/integration-20260831T014141.617746981Z/`，覆盖single-file JSON/YAML与模块化compile canonical bytes等价、duplicate-key/YAML alias精确错误码、六个独立views、稳定artifact titles、3×2 row-major contact sheet、单格双候选repair、多格baseline blocker，provider calls=0。
- Scaena evidence：`agent/scaena/temp/integration-test-runs/20260831-013932.027586444-system-3318703-1/`，覆盖official exact refs、6个模块、single-file/modular canonical task与Prompt Bundle digest等价、typed spec、零blocking finding、确定性bundle replay，provider calls=0。
- catalog 连续两次 build digest 一致，随后 validate 通过；对应 OpenSpec strict validation 通过。

## Rights 与质量边界

内容仅使用原创虚构角色、通用服饰与非品牌材料描述，不包含真人肖像、受保护角色复刻、品牌 claim、用户私有素材、credential、Provider payload 或完整思维链。expression contact sheet 只用于审阅，不能替代 accepted face master；同机位六表情不宣称 LoRA-ready。

本 candidate 没有 live provider 质量证据，不应提升为 `first-support` 或 `mature`，也不应描述为 production-ready。

## Immutable release 与回滚

维护者若后续授权正式 internal release，应固定 Git commit/tag、上述 catalog digest 与 solution version，不得原地覆盖 `1.0.0`。发布前发现问题时直接撤回 candidate；发布后发现问题时恢复上一已知良好的 Git/tag 与 catalog mapping，并以新版本发布修复，保留 `1.0.0` digest lineage。
