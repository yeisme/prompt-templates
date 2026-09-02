# official-modular-asset-preview-templates Specification

## Purpose
TBD - created by archiving change official-ai-drama-modular-visual-assets-v2. Update Purpose after archive.
## Requirements
### Requirement: 分层预览必须保留 exact source lineage
`character-layer-preview-v1` 和 `environment-layer-preview-v1` SHALL 引用稳定排序的 exact source refs、revisions 和 digests，并显示层级、对齐、穿插、遮挡或占位关系。预览 MUST 标记 `canonical=false`。

#### Scenario: 角色服装局部修复后重建预览
- **WHEN** garment RenderRevision 改变而 head/body/hair refs 不变
- **THEN** 只更新对应 preview revision 与 source digest
- **AND** 未修改的 source assets 不产生新 canonical revision

### Requirement: Harmonized preview 不得吞并源资产
`character-harmonized-preview-v1` 和 `environment-harmonized-preview-v1` SHALL 支持可选的统一光线、材质观感或色彩协调，同时 MUST 保留全部 source lineage，且不得成为新的 identity、wearable、object 或 scene-shell source。

#### Scenario: Harmonized preview 视觉效果最佳
- **WHEN** 人类接受 harmonized preview 作为组合参考
- **THEN** review 只接受该 preview revision
- **AND** source slot refs、DesignSpec 与 RenderRevision 仍是后续生成的 canonical inputs

### Requirement: Preview 不能宣称生产就绪
所有 preview template outputs MUST 明确区分 Prompt/render success、Eikona image review 与 Scaena production acceptance。它们 MUST 不输出 subject frozen、shot ready、production ready 或 final accepted。

#### Scenario: Pack 自动生成 batch preview
- **WHEN** batch preset 的所有必需源图已生成
- **THEN** 系统可以创建非 canonical preview
- **AND** pack-level `production_ready` 仍为 false，等待人类整体审阅

