# AI 做剧官方模板测试与今日状态（2026-09-02）

最后核对时间：2026-09-02（UTC）。

## 今日结论

`official-ai-drama-modular-visual-assets-v2` 的内容实现全部完成：两个 2.0.0 family 共 11 个模板（`head-core-bald-v1`、`body-core-neutral-v1`、`surface-coat-hair-v1`、`wearable-garment-v1`、`wearable-accessory-v1`、`character-layer-preview-v1`、`character-harmonized-preview-v1`、`semantic-object-v1`、`empty-scene-shell-v1`、`environment-layer-preview-v1`、`environment-harmonized-preview-v1`）均有手写 zh-CN 正文、contract、document 与共享 schema 绑定，并配 11 个 fixture 集 / 42 cases（20 valid、22 invalid）。

实际成熟度仍是 `exploratory`：本波全部验证为 provider-free（真实 Provider 调用次数 = 0），没有 Eikona 真实渲染、Scaena 装配或人工评审记录；`first-support` 门槛（fixture 执行、人工评审、rights 结论、已知失败记录齐全）尚未满足。`en` 适配尚未开始（规则已就绪：逐 role 绑定 source digest）。

## 今日证据

| 检查项 | 结果 | 关键数据 |
| --- | --- | --- |
| OpenSpec strict | 通过 | `openspec validate --all --strict --no-interactive`：11 passed, 0 failed |
| Template Registry catalog | 通过 | 19 solutions；连续两次 build digest 一致 `sha256:cb1dda68199eed2150f7bcd4c6128ab19322f693a980b5f59d003fdcffb35582`；validate success |
| contract validate ×11 | 通过 | 2.3/2.4/3.3 七个新模板 8–10 inputs；四个已落地模板 refresh 后仍通过 |
| document validate ×11 | 通过 | 全部绑定共享 schema `character_asset.modular_slot_bundle.v1`（digest `sha256:aa06ba9aeed92c7fb11c0e1d152375c1da58360ccb84276b6473c70251d217f5`） |
| fixture validate ×11 | 通过 | 42 cases（20 valid / 22 invalid）；provider calls=0；valid 输出经 Registry 语义门 + schema 双重校验 |
| 1.x 不可变 | 通过 | `git status` 过滤后 1.x 目录零改动；1.x catalog 地址不重定向 |
| 真实 Provider | 未执行 | 本波不调用任何 Provider；上一波（2026-08-31）的两次真实调用与费用记录见 2026-08-31 指南 |

## 本波关键决策

- **共享 schema 扩展预览面**：`character_asset.modular_slot_bundle.v1` 经 `document artifact replace` 增补 `preview_lineage`（仅 `slot_id=preview` 必填、其他 slot 禁用）与 `policy_echo.preview_purpose`，11 个 document 全部 rebind 到同一文件，无复制漂移。
- **回显字段命名**：Registry fixture 门禁止 valid fixture 输出出现任何归一化后以 `ref` 结尾的键，因此 v2 共享 schema 用 `subject_version`（1.x 为 `subject_version_ref`）与 lineage 项 `source_version` + `artifact_digest`；lineage 之外的 durable ref 仍一律禁止。
- **fixture 侧补充稳定码**：`HEAD_CORE_ISOLATION_CONTAMINATION` 覆盖首饰/脖肩类污染（prompt 声明的失败码为"至少"集，fixture 可在其上扩展并已在 preset matrix 登记）。
- **1.x 兼容 fixture**：`surface-coat-hair-v1` 的 `legacy-hairstyle-compat` case 以 `promptrepo://official/video/ai-drama-character-assets@1.0.0#hairstyle-sheet-v1` 作 compat-only 参考，断言不重定向、不升格 canonical。

## 已知缺口（阻塞 first-support/release）

- Eikona 尚未按 v2 slot 合同做真实渲染与 Alpha/污染 QA；Scaena 尚未消费 preview lineage。
- Registry 当前只有 graph-kit / ui-template 两类 structured release family，prompt-solution release family 缺位，2.0.0 的 immutable release 无法建立（上一波已记录的外部 blocker，本波如实保留）。
- `en` 适配未开始；rights 复核与人工评审记录未建。

## 标准证据目录

- 共享 schema：`solutions/video/ai-drama-character-assets-v2/contracts/schemas/character_asset.modular_slot_bundle.v1.schema.json`；
- fixture manifests：`solutions/video/ai-drama-character-assets-v2/contracts/fixtures/*.fixtures.json`、`solutions/video/ai-drama-background-assets-v2/contracts/fixtures/*.fixtures.json`；
- preset matrix：`solutions/video/ai-drama-character-assets-v2/docs/preset-matrix.zh-CN.md`、`solutions/video/ai-drama-background-assets-v2/docs/preset-matrix.zh-CN.md`。
