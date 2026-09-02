# 模块化角色资产预设矩阵 v2

适用：`ai-drama-character-assets-v2@2.0.0`（`promptrepo://official/video/ai-drama-character-assets-v2@2.0.0`）。当前 maturity=`exploratory`，1.x 目录与其 preset 语义不变；本文只描述 2.0.0。

## 生产 DAG（目录序不等于依赖序）

```text
head-core-bald-v1（detail_front 先接受，再补其余五视图）
  → body-core-neutral-v1（与头模并行，按 age_band/topology_family）
  → surface-coat-hair-v1（继承头型/头皮接口，不碰脸）
  ∥ wearable-garment-v1（单件，按层级逐件）
  ∥ wearable-accessory-v1（单件装饰 / extension_part）
  → character-layer-preview-v1（对齐/穿插/遮挡检查，canonical=false）
  → character-harmonized-preview-v1（协调 read，canonical=false）
```

每个视图是独立 RenderRevision；contact sheet 只由 consumer 本地拼。preview 永远在尾部且不回写任何 source。

## 角色槽位矩阵

| Template | Slot | 主要产物 | 必需输入 | 关键门禁 | 下游 |
|---|---|---|---|---|---|
| `head-core-bald-v1` | `head_core` | 无头发头模六视图（透明 RGBA） | DesignSpec + head 绑定 | 无发/饰/脖肩/背景污染；`detail_front` 捕获锁 | surface_coat / accessory / 预览 |
| `body-core-neutral-v1` | `body_core` | 中性覆盖身体核心六视图 | DesignSpec + age_band + topology_family | neutral coverage；minor 安全门；非人拓扑不烘焙外层 | wearable / extension / 预览 |
| `surface-coat-hair-v1` | `surface_coat` | 头发/毛发层设计与贴合渲染 | head 锚 + 层 DesignSpec | 只继承头型与头皮接口；无五官/首饰污染 | layer preview |
| `wearable-garment-v1` | `wearable` | 单件服装贴合渲染 | body 锚 + 单件 DesignSpec | 单件合同；不继承脸/发/身份 | layer / harmonized preview |
| `wearable-accessory-v1` | `accessory` / `extension_part` | 单件装饰或扩展部件 | 贴合锚 + 单件 DesignSpec | 单件合同；不打包套装 | layer preview |
| `character-layer-preview-v1` | `preview` | 分层对齐检查图 | exact source_refs + 绑定 | `canonical=false` + lineage 精确回显 | 人工审阅（不产 canonical） |
| `character-harmonized-preview-v1` | `preview` | 整体协调检查图 | exact source_refs + 协调选项 | source refs 仍是唯一 canonical inputs | 人工审阅（不产 canonical） |

## 稳定失败码

`head-core`：`HEAD_CORE_HAIR_CONTAMINATION`、`MISSING_SCALP_INTERFACE`、`VIEW_CONTRACT_VIOLATION`、`MINOR_ADULTIFICATION_RISK`、`TRANSPARENCY_CONTRACT_VIOLATION`（fixture 侧另用隔离码 `HEAD_CORE_ISOLATION_CONTAMINATION` 覆盖首饰/脖肩类污染）。
`body-core`：`MINOR_SAFETY_GATE_BLOCKED`、`EXPLICIT_ANATOMY_REQUESTED`、`BODY_CORE_WARDROBE_CONTAMINATION`、`TOPOLOGY_FAMILY_MISMATCH`。
`surface-coat`：`SURFACE_COAT_ATTACH_INTERFACE_MISSING`、`SURFACE_COAT_IDENTITY_CONTAMINATION`、`SURFACE_COAT_JEWELRY_CONTAMINATION`、`SURFACE_COAT_BACKGROUND_CONTAMINATION`。
`wearable-garment`：`WEARABLE_FIT_INTERFACE_MISSING`、`WEARABLE_IDENTITY_CONTAMINATION`、`WEARABLE_SINGLE_ITEM_VIOLATION`、`WEARABLE_SCENE_CONTAMINATION`。
`wearable-accessory`：`ACCESSORY_FIT_INTERFACE_MISSING`、`ACCESSORY_IDENTITY_CONTAMINATION`、`ACCESSORY_SINGLE_ITEM_VIOLATION`、`ACCESSORY_ISOLATION_CONTAMINATION`。
preview：`PREVIEW_SOURCE_LINEAGE_MISSING`、`PREVIEW_SOURCE_DIGEST_MISMATCH`、`PREVIEW_CANONICAL_CLAIM_FORBIDDEN`、`PREVIEW_SUBJECT_FREEZE_CLAIM_FORBIDDEN`。

## Fixture 覆盖（provider-free）

`head-core-six-view-v1`（10 cases：六视图 valid + 4 blocking）、`body-core-six-view-v1`（6）、`surface-coat-six-view-v1`（4，含 1.x 兼容 case）、`garment-six-view-v1`（3）、`accessory-six-view-v1`（3）、`layer-preview-stack-v1`（3）、`harmonized-read-v1`（2）。全部由 Registry `fixture set init/case add` 生成并通过 `fixture validate`；不调用真实 Provider。
