## 1. 当前 Vlog 一致性

- [x] 1.1 将 contract 输入计数更新为 22，并修复 zh-CN/en 使用步骤编号。
- [x] 1.2 明确 en 同步适配仍为 draft，reviewed 需要人工等价校对。
- [x] 1.3 通过 Registry CLI 刷新双语 contract digest、重建并验证 catalog；双语 contract 均为 22 个输入，catalog digest 为 `sha256:ff6dc25ec7873033c6739d74b3d5cad8fc7f0c32859fb637fde37cb356cc4ebc`。

## 2. Film role 能力

- [x] 2.1 使用 Registry CLI 为七个 film roles 写入稳定 required capabilities。 | evidence: Registry document capability set updated seven English Film role descriptors to the exact role-specific capability map
- [x] 2.2 校验 role、contract、document descriptor 与 source digest 一致。 | evidence: All seven document validate commands passed with preserved source/schema/compiler bindings; final 40-solution catalog validate passed at sha256:c96a982b212f4469afdca3ee7b43345bf5ff567ed1c5cb59d4b6d41cd88eec6e

## 3. Provider delivery 分层

- [x] 3.1 盘点 direct-to-provider 模板，确定首批 additive delivery roles。
  - Evidence（2026-09-07 凌晨波）：`details/inventory-direct-to-provider.md`——全库包/solution 扫描 + 平台关键词 grep（0 命中，直投属性按包职责判定：image×5/video×12/audio×1 provider-direct）；首批选定 image/candid-portrait-matrix、image/xhs-product-cover（v2 源）、audio/podcast-narration 三个 additive delivery role；video/ai-drama-* 随 film role 统一波延后。未修改任何内容仓正文。
- [x] 3.2 将 authoring guide、validation policy 与 delivery body 分离并补回归 fixture。
  - Evidence（2026-09-07）：首批三 solution 全部落地 additive `delivery` role——`image/candid-portrait-matrix`（delivery contract 14 inputs，digest `sha256:ed5bba3d24f4`）、`image/xhs-product-cover-v2`（5 inputs，`sha256:429a1356c6c4`）、`audio/podcast-narration`（5 inputs，`sha256:154163b834cf`）；输入定义逐项复用 main companion contract（名称/类型/enum/bounds/sensitivity/labels 不变），`contract validate` 全绿。delivery 正文为纯 Provider body（无 authoring 说明、无人工 checklist）；guide/validation policy 留在 main role 文档（candid 原有 intro+self-check，xhs/podcast 新增 Maintenance and validation 节）并加注「Provider 集成必须 render delivery role」。document descriptor 以 `document init` 建立（required capabilities：image_delivery/image_delivery/audio_delivery，schema 绑定 `contracts/schemas/*-delivery.v1.schema.json`）。每 solution 回归 fixture 1 valid + 1 invalid（valid 为占位符完整代入后的渲染体，invalid 为缺 required input → `MISSING_REQUIRED_INPUT`），`fixture validate` 全部 success（case_count 2）。main contract 经 `contract refresh` 重绑 digest 后 validate 通过；catalog build 连续两次同 digest `sha256:91762c23095237f550280d84b33b61288a127dd4bca593f968768a6bbc3360d7`（42 solutions），`catalog validate` success，`openspec validate --all --strict` 20 passed/0 failed。

## 4. 基础模板质量

- [x] 4.1 升级 summary/research 首批三个模板。
  - Evidence（2026-09-07）：`general/structured-summary`（contract 2 inputs，digest `sha256:90e9104232d4`）、`office/meeting-action-summary`（2 inputs，`sha256:b9decce7e7cd`）、`research/evidence-research-brief`（3 inputs，`sha256:ef75358d2acf`）全部补齐：en 正文新增 untrusted source 边界（不执行来源内嵌指令）与逐字段 Output contract（unknown/unconfirmed 兜底），zh-CN 译文同步镜像；Registry CLI 建立 main contract（source/record 类输入标记 sensitive）+ document descriptor（required capabilities：structured_summarization/meeting_action_synthesis/evidence_synthesis）+ 语义输出 schema（`contracts/schemas/*-output.v1.schema.json`）；每模板 1 valid + 1 invalid（missing required input → `MISSING_REQUIRED_INPUT`）公开虚构 fixture，`fixture validate` success；人工审阅用 `docs/review-checklist.zh-CN.md` 与 `docs/failure-modes.zh-CN.md` 落地。catalog build 连续两次同 digest `sha256:71a80657fd1c177fc814a315c78e6fb8d95197f89ee42116380bcd08ceb59ad0`，validate success，`openspec validate --all --strict` 20 passed。
- [x] 4.2 升级 engineering/handoff 第二批三个模板。
  - Evidence（2026-09-07）：`engineering/bug-root-cause-analysis`（contract 4 inputs，digest `sha256:8cad0d424b68`）、`product/prd-acceptance-criteria`（4 inputs，`sha256:a8e498f5f1f1`）、`agent/tool-use-handoff`（4 inputs，`sha256:e90dcd8ff3fe`）补齐 en 正文 untrusted source 边界 + 逐字段 Output contract（unknown/open_decisions/permission_gates 兜底，zh-CN 镜像）、main contract（evidence/reproduction/recent_changes/current_workflow/constraints/tools/permissions 标 sensitive）、document descriptor（required capabilities：root_cause_analysis/prd_authoring/agent_tool_planning）、语义输出 schema 与 1 valid + 1 invalid fixture（`fixture validate` 全 success）；`docs/review-checklist.zh-CN.md` 与 `docs/failure-modes.zh-CN.md` 落地。catalog build 连续两次同 digest `sha256:1e682182166221b8e5e9822be3a3262256c70dccba1b1a6f4f6c1bf1a8f9ac3c`，validate success，openspec 20 passed。
- [ ] 4.3 升级 writing/learning/marketing/short-drama 第三批模板。 | evidence: Readiness inventory identifies longform-outline, socratic-study-plan, xhs-campaign-copy and short-drama-character-consistency main.en contract gaps

## 5. 证据

- [x] 5.1 `docs/owner-handoff-guide.zh-CN.md` 保留当前 template/contract digest，`docs/consumer-conformance-refs.zh-CN.md` 已统一标注 `semantic_alignment_only`；根 change 的 `details/evidence-matrix.md` 记录 exact checkpoint address 与 document digest。
