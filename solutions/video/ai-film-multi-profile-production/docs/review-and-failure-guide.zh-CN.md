# 审查与失败重构指南

## 审查顺序

先审剧作再审可生成性：情感主角、欲望/阻力/选择/代价、场景权力变化、资产戏剧功能。然后审资产依赖、SceneGEO、active bindings、单镜头变量、声音意图和连续性。没有证据的项目必须是 `unknown`，不是默认通过。

## 固定 failure code

| 类别 | 代码 | 最小处理 |
| --- | --- | --- |
| 剧作 | `ASSET_WITHOUT_DRAMATIC_FUNCTION`、`NO_EMOTIONAL_PROTAGONIST`、`NO_SCENE_STATE_CHANGE` | 补人物选择/状态变化，不扩写资产展览 |
| 空间/绑定 | `MISSING_SCENE_GEO`、`AXIS_UNRESOLVED`、`IDENTITY_WARDROBE_INHERIT_COLLISION` | 补一个 GEO 或修一个 binding 维度 |
| 镜头 | `PROFILE_SWITCH_AT_SHOT`、`MULTI_CHANGE_SHOT`、`UNOBSERVABLE_EMOTION` | 保持 profile，拆镜或改可观察行为 |
| 安全/事实 | `FORBIDDEN_PROVIDER_PAYLOAD`、`FORBIDDEN_OWNER_TERMINAL_FIELD`、`INVENTED_PRODUCT_CLAIM` | 删除禁止字段，回到 safe fact source |
| 重构 | `REROLL_SCOPE_TOO_BROAD`、`RETRY_THRESHOLD_REACHED`、`BASELINE_BINDING_BLOCKER` | 限定一个变量；阈值后重构/升级 Owner review |

## Bounded repair

一个 finding 只允许修其指向变量类。不得一次同时替换身份、衣物、机位、动作、灯光、风格或 profile。连续 10–15 次同类失败、或多 cell/shot 同时身份/capture 漂移时，停止“增加形容词”，转向拆镜、固定机位、减少人物、缩短时长、从已建立接触开始、反应镜/插入镜/声音桥，或重写场景覆盖。

## Handoff

内容仓库 handoff 仅包括模板 role、profile、safe input projection、semantic output、fixture ref、finding 与不确定性。不得将 provider 请求、媒体 bytes、owner secret、批准状态、预算或完整推理写入该仓库。各 consumer owner 应把 safe evidence refs 留在自己的 change；本 solution 只能登记现有 immutable safe ref，不能伪造 conformance。
