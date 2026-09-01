## 1. Solution contracts

- [ ] 1.1 通过 Template Registry CLI 创建/升级 `ai-drama-character-assets@2.0.0` 与 `ai-drama-background-assets@2.0.0` 结构化 skeleton，不修改 1.x。
- [ ] 1.2 定义 shared slot、DesignSpec、RenderRevision、view plan、isolation、inherit/forbid 和 preview vocabulary。
- [ ] 1.3 为 `zh-CN` source 与 `en` adaptation 建立版本、source digest、rights 和 maturity 规则。

## 2. Character templates

- [ ] 2.1 实现 `head-core-bald-v1`，覆盖严格正脸 detail、完整头顶/后脑/双耳、六视图、透明输出和 blocking negative constraints。
- [ ] 2.2 实现 `body-core-neutral-v1`，覆盖 age band、neutral coverage、topology family 和未成年人安全门。
- [ ] 2.3 实现 `surface-coat-hair-v1`、`wearable-garment-v1`、`wearable-accessory-v1`，覆盖接口、层级、遮挡、碰撞与禁止继承。
- [ ] 2.4 实现 character layer/harmonized preview，明确 `canonical=false` 与 exact source lineage。

## 3. Environment templates

- [ ] 3.1 实现 `semantic-object-v1` 及 geometry-adaptive view plan。
- [ ] 3.2 实现 `empty-scene-shell-v1`，覆盖零人物、零人形痕迹、零独立物件和完整不透明画布。
- [ ] 3.3 实现 environment layer/harmonized preview，保持无人物边界。

## 4. Fixtures and validation

- [ ] 4.1 增加有效成人、未成年人安全、非人 topology、六视图和自适应物件视图 fixtures。
- [ ] 4.2 增加头发/发饰/首饰/脖肩/背景污染、服装污染身份、场景人物/海报/雕像/倒影/物件污染的 blocking fixtures。
- [ ] 4.3 增加 preview source lineage、canonical false 和旧 1.x 不变的兼容 fixtures。
- [ ] 4.4 运行 catalog build/validate 与 `openspec validate --all --strict --no-interactive`，不得调用真实 Provider。

## 5. Documentation

- [x] 5.1 发布模块化视觉资产 v2 设计说明并更新文档索引。
- [ ] 5.2 实现后更新 preset matrix、authoring guide 和 dated test guide，明确实际成熟度和 Provider-free 证据。
