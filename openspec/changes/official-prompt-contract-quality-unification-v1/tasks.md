## 1. 当前 Vlog 一致性

- [x] 1.1 将 contract 输入计数更新为 22，并修复 zh-CN/en 使用步骤编号。
- [x] 1.2 明确 en 同步适配仍为 draft，reviewed 需要人工等价校对。
- [x] 1.3 通过 Registry CLI 刷新双语 contract digest、重建并验证 catalog；双语 contract 均为 22 个输入，catalog digest 为 `sha256:ff6dc25ec7873033c6739d74b3d5cad8fc7f0c32859fb637fde37cb356cc4ebc`。

## 2. Film role 能力

- [ ] 2.1 使用 Registry CLI 为七个 film roles 写入稳定 required capabilities。
- [ ] 2.2 校验 role、contract、document descriptor 与 source digest 一致。

## 3. Provider delivery 分层

- [ ] 3.1 盘点 direct-to-provider 模板，确定首批 additive delivery roles。
- [ ] 3.2 将 authoring guide、validation policy 与 delivery body 分离并补回归 fixture。

## 4. 基础模板质量

- [ ] 4.1 升级 summary/research 首批三个模板。
- [ ] 4.2 升级 engineering/handoff 第二批三个模板。
- [ ] 4.3 升级 writing/learning/marketing/short-drama 第三批模板。

## 5. 证据

- [x] 5.1 `docs/owner-handoff-guide.zh-CN.md` 保留当前 template/contract digest，`docs/consumer-conformance-refs.zh-CN.md` 已统一标注 `semantic_alignment_only`；根 change 的 `details/evidence-matrix.md` 记录 exact checkpoint address 与 document digest。
