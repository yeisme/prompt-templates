## 1. Solution 与作者合同

- [x] 1.1 使用Template Registry authoring service创建`video/ai-drama-character-assets` solution skeleton和中文locale；依赖：Registry structured authoring实现；验收：machine metadata非手写；验证：`(cd ../../backend-server/template-registry && go run ./cmd/template-registry catalog validate --repository ../../data/yeisme-prompt-templates --json)`。
- [x] 1.2 通过authoring service创建document descriptors、Schema IDs、compiler profile和fixture manifest skeleton；依赖：1.1；验收：source/digest绑定完整；验证：Registry structured validation。

## 2. 中文模板与 fixtures

- [x] 2.1 导入并规范化武侠女性三视图single-file JSON/YAML；依赖：1.2；验收：成人、左右marker、汉服材料、三视图、帆布鞋、QC完整；验证：Promptrepo/Scaena conformance fixture。JSON/YAML canonical digest 均为 `sha256:9bf30747a50e7cab42b9a0a53b4995d403b91715978180b2e2252d687f6afa71`。
- [x] 2.2 提取Character、Wardrobe、Task、Layout、QC模块化YAML；依赖：2.1；验收：编译结果与single-file canonical bytes/digest等价；验证：Eikona canonical compile canary与Scaena official module compile fixture。
- [x] 2.3 编写公开可审阅的中文Prompt sections和声明式compiler profile；依赖：1.2；验收：不重复维护完整角色事实、不含隐藏system prompt；验证：content review和compiler fixture。
- [x] 2.4 增加invalid fixture matrix；依赖：1.2；验收：每个fixture有expected reason code；验证：Promptrepo/Scaena/Eikona provider-free tests。
- [x] 2.5 完善expression-sheet依赖、独立cell、capture/intensity、reference边界、bounded repair和LoRA分界的OpenSpec、profile与中文指南；依赖：2.3；验收：目录序不再被描述为依赖序，production不生成单次六格图，face master保持身份真源；验证：OpenSpec strict和content review。
- [x] 2.6 通过Template Registry authoring service同步正式`main` Prompt正文，新增`qingyi-expression-calibration` valid fixture及expression invalid matrix，并把新增stable reason codes写入compiler/fixture manifests；依赖：2.5；验收：Prompt digest与所有machine metadata由CLI生成，provider calls=0；验证：Registry contract/fixture validate。
- [x] 2.7 增加Scaena/Eikona provider-free consumer canary：六个独立views、稳定artifact titles、3×2 contact sheet ordering、单格repair与多格baseline blocker；依赖：2.6；验收：现有`character_asset.prompt_bundle.v1`兼容；验证：owner focused tests和integration evidence。

## 3. i18n、rights 与文档

- [x] 3.1 完成英文reviewed adaptation，保持stable IDs/constraints不变；依赖：2.3；验收：中文source digest可追踪；验证：locale/catalog tests。
- [x] 3.2 完成rights/maturity、依赖矩阵、expression使用指南、失败模式、审查清单和consumer handoff文档；依赖：2.5；验收：initial internal/exploratory、无真人/品牌侵权素材、无LoRA-ready误导；验证：OpenSpec/content review。

## 4. Catalog 与发布门

- [x] 4.1 构建并验证catalog；依赖：3.1、3.2；验证：`template-registry catalog build --repository . --json` 连续两次得到同一 digest，随后 `template-registry catalog validate --repository . --json` 通过。
- [x] 4.2 运行严格OpenSpec验证；依赖：4.1；验证：`openspec validate official-ai-drama-character-asset-templates-v1 --strict --no-interactive`。
- [x] 4.3 完成internal/exploratory release-candidate gate与rollback packet；依赖：4.2；验收：exact `1.0.0`、rights、maturity、catalog digest和consumer evidence均已审查。本任务未commit、tag、push或publish，因此没有冒充已执行Git immutable release。

## 中文 first-slice evidence

- `contract validate`：main 11 inputs，placeholder 精确覆盖。
- `document artifact validate`：Prompt Bundle Schema 和 `eikona.character-asset.prompt-bundle.v1` 声明式 compiler profile 均由 Registry CLI 生成。
- `fixture validate`：3 valid、20 invalid；其中expression matrix为1 valid、9 invalid，并显式覆盖duplicate-key与YAML alias strict-parser cases；所有invalid cases绑定stable expected reason codes，Provider calls为0。
- JSON Schema：`wuxia-female-turnaround` 与 `manga-shot-keyframe` 两个 valid outputs 均通过 `character_asset.prompt_bundle.v1`。
- Expression spec/docs：已明确face-level依赖、独立cells、presentation-only领口、capture/intensity锁、seed语义、bounded repair与LoRA分界；未产生provider call。
- JSON/YAML source authoring：Registry `document source set`重放通过，canonical digest精确相同；模块化Character/Wardrobe/Task/Layout/QC/plan descriptors全部通过。
- English adaptation：`main.en` contract/document通过，placeholder与中文保持一致，英文i18n文档绑定中文source digest。
- Consumer evidence：Eikona `temp/integration-test-runs/integration-20260831T014141.617746981Z/`；Scaena `temp/integration-test-runs/20260831-013932.027586444-system-3318703-1/`，两者均passed且provider calls=0；Scaena artifact明确记录single-file/modular canonical task与Prompt Bundle digest均相等。
- Catalog/release candidate：14 solutions，确定性digest `sha256:f2ee99e6316530669753907f603a72bffaeb8d3d4d8178c3d7384d837c355122`；release packet见`docs/release-1.0.0.zh-CN.md`。
