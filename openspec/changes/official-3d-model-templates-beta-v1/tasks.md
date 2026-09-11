# 实施与验收任务

由 scripts/openspec-tasks.py 维护状态。

- [ ] 1 内容 owner：用 Registry CLI 为 `3d` package 生成 5 个 beta solution 骨架（`text-to-3d-object-beta`、`image-to-3d-refine-beta`、`3d-scene-layout-beta`、`3d-printable-design-beta`、`3d-asset-review-beta`）并设置 tags/capabilities；依赖无；验证 `catalog build` 与 `catalog validate` 通过；失败重检 solution id、package 目录与 metadata 重放；单线程执行。 | evidence: catalog build/validate passed; 5 solutions registered with beta ids
- [ ] 2 内容 owner：撰写 `text-to-3d-object-beta` 与 `3d-printable-design-beta` 英文模板正文、contract、评审清单与失败模式；依赖 1；验证 contract 校验与编译演练（缺字段拒绝、成功导出、provider_calls=0）；失败重检变量与必填字段。 | evidence: contract valid; compile dry-run passed with provider_calls=0
- [ ] 3 内容 owner：撰写 `image-to-3d-refine-beta` 与 `3d-scene-layout-beta` 英文模板正文与 contract，场景字段保持 provider-neutral；依赖 1；验证 contract 校验与编译演练；失败重检变量与来源声明；可与任务 2 并行。 | evidence: contract valid; scene fields documented as provider-neutral
- [ ] 4 内容 owner：撰写 `3d-asset-review-beta` 评审清单模板（几何完整性、UV/贴图、比例、rights_review）；依赖 1；验证 contract 校验；可与任务 2、3 并行。 | evidence: contract valid; review checklist covers geometry/uv/scale/rights
- [ ] 5 内容 owner：用 Registry CLI 注册 recipe `concept-to-3d-asset-beta`，步骤引用 exact `locale=en` ref；依赖 2、3、4；验证 recipe DAG、依赖循环与失效传播校验；失败重检步骤 ref 与输出绑定。 | evidence: recipe DAG validation passed; exact refs resolve
- [ ] 6 内容 owner：为 5 个 solution 撰写 `docs/template-zh-CN.md` 中文审阅译文并标注人工审阅身份；依赖 2、3、4；验证变量 parity 与 locale 政策（中文不可编译、不进 catalog digest）；失败重检变量集合差异。 | evidence: translation variable parity passed; zh-CN not registered as compilable locale
- [ ] 7 文档 owner：更新仓库 README 类别索引与 taxonomy 增量说明；依赖 1–6；验证链接与类别清单一致；失败重检索引条目。 | evidence: README category index includes 3d package; taxonomy additions documented
- [ ] 8 外部阶段：真实 3D provider 调用、费用授权、Scaena 字段映射与转正评审；依赖后续运行与发布授权；未完成不得转正式支持。
