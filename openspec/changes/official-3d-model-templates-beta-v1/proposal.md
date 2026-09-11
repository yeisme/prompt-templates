# 官方 3D 模型模板类别试点

## Why
模板目录现有 13 个类别（image、video、writing、audio 等），没有任何 3D 模型与空间资产模板。仓库已确立 Anatomia（空间感知证据）→ Scaena（ReplicaStage、GLB 衍生）的 3D owner 架构，但 Prompt 语义层空缺：Agent 无法通过 exact ref 获得文生 3D、图生 3D、场景布局、3D 打印约束和 3D 资产评审的可编译提示方案。用户已确认方向：先做纯 Prompt 模板类别，执行层（3D provider adapter）不在本 change 范围。

## What Changes
- 新增 `3d` package，含 5 个 beta solution：`text-to-3d-object-beta`（文生 3D 单物体）、`image-to-3d-refine-beta`（图生 3D 精修）、`3d-scene-layout-beta`（场景布局）、`3d-printable-design-beta`（3D 打印约束）、`3d-asset-review-beta`（资产评审清单）。
- 新增 1 个 recipe：`concept-to-3d-asset-beta`，表达「Eikona 概念图 → 图生 3D → 评审 → 交付」DAG，步骤引用 exact `locale=en` ref。
- taxonomy 增量：`modality:3d`、`artifact:model_3d`、`artifact:scene_layout`、`constraint:manifold_geometry`、`constraint:scale_anchored`、`constraint:multi_view_consistency`，capabilities 增加 `model3d`、`scene_spatial`。
- 每个 solution 按仓库规范只注册英文模板与英文 contract，中文译文放 `docs/template-zh-CN.md` 供人工审阅；结构化 metadata 全部由 Template Registry CLI 生成。

## Capabilities
### New Capabilities
- `3d-model-templates`：发现、编译、导出与复用 3D 模型与空间资产提示方案。

## Impact
内容归本仓；3D 执行与 canonical state 仍归 Scaena/Anatomia，图像概念图归 Eikona，本 change 不新增 provider 调用、不授予工具或费用权限。场景布局模板输出通用字段，与 Scaena `SceneGEO`/`ReplicaStage` 的映射留作后续 additive change。真实 3D provider 调用、费用与正式转正为后续外部阶段。
