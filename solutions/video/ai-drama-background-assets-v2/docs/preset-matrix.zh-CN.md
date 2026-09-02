# 模块化环境资产预设矩阵 v2

适用：`ai-drama-background-assets-v2@2.0.0`（`promptrepo://official/video/ai-drama-background-assets-v2@2.0.0`）。当前 maturity=`exploratory`，1.x 目录与其 preset 语义不变；本文只描述 2.0.0。

## 生产 DAG

```text
empty-scene-shell-v1（主机位先接受，反打复用同一锚点）
  ∥ semantic-object-v1（每物件独立，geometry-adaptive 视图）
  → environment-layer-preview-v1（落位/遮挡/预留区检查，canonical=false）
  → environment-harmonized-preview-v1（协调 read，仍零人物）
```

场景壳与物件可并行；preview 只做装配检查，不改锚点、不新增物件、不带入人物。

## 槽位矩阵

| Template | Slot | 主要产物 | 必需输入 | 关键门禁 | 下游 |
|---|---|---|---|---|---|
| `semantic-object-v1` | `semantic_object` | 独立物件设计/渲染（默认透明） | DesignSpec + geometry-adaptive view plan | 零人物/手/环境附着；视图带选择原因 | 环境预览 / 剧情状态引用 |
| `empty-scene-shell-v1` | `environment_shell` | 无人物无物件空场景（完整不透明） | DesignSpec + 视图计划 | 零人物零人形痕迹零独立物件；锚点稳定 | 环境预览 / 分镜装配 |
| `environment-layer-preview-v1` | `preview` | 壳体+物件分层占位检查图 | exact source_refs | `canonical=false` + lineage 精确回显 + 零人物 | 人工审阅（不产 canonical） |
| `environment-harmonized-preview-v1` | `preview` | 环境整体协调检查图 | exact source_refs + 协调选项 | 锚点/光源方向/预留区不改写 | 人工审阅（不产 canonical） |

## 稳定失败码

`semantic-object`：`OBJECT_HUMAN_CONTAMINATION`、`OBJECT_ENVIRONMENT_CONTAMINATION`、`MISSING_VIEW_PLAN_REASON`、`OBJECT_STATE_MISMATCH`、`UNDECLARED_BRAND_TEXT`。
`empty-scene-shell`：`SCENE_HUMAN_TRACE_DETECTED`、`SCENE_LOOSE_OBJECT_DETECTED`、`OPAQUE_CANVAS_VIOLATION`、`ACTIVITY_ZONE_BLOCKED`、`ANCHOR_REDESIGNED_ON_REVERSE`。
preview：`PREVIEW_SOURCE_LINEAGE_MISSING`、`PREVIEW_SOURCE_DIGEST_MISMATCH`、`PREVIEW_CANONICAL_CLAIM_FORBIDDEN`、`PREVIEW_SUBJECT_FREEZE_CLAIM_FORBIDDEN`、`PREVIEW_ENVIRONMENT_HUMAN_TRACE_DETECTED`。

## Fixture 覆盖（provider-free）

`object-adaptive-view-v1`（3 cases）、`scene-shell-anchors-v1`（4）、`environment-layer-preview-v1`（2）、`environment-harmonized-read-v1`（2）。全部由 Registry `fixture set init/case add` 生成并通过 `fixture validate`；不调用真实 Provider。
