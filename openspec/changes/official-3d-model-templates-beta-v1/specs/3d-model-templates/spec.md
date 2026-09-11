## ADDED Requirements

### Requirement: 文生 3D 单物体模板
系统 SHALL 以 beta exact ref 提供 `text-to-3d-object-beta` 英文可编译模板，把确认后的主体描述、用途、风格与约束编译为 provider-neutral 的文生 3D 提示包。

#### Scenario: 编译文生 3D 提示包
- **WHEN** 用户确认主体、用途（game/print/background）、目标风格、面数级别与对称性约束
- **THEN** Registry 在零 provider 调用下编译并导出提示包，记录 exact template digest

#### Scenario: 用途缺失时拒绝
- **WHEN** 用途或主体描述缺失或未确认
- **THEN** 编译以可读错误拒绝并列出缺失字段，不编造默认值

### Requirement: 图生 3D 精修模板
系统 SHALL 提供 `image-to-3d-refine-beta` 模板，将参考图 exact ref、视角补全策略与背面/遮挡推测约束编译为图生 3D 提示包。

#### Scenario: 参考图驱动的编译
- **WHEN** 用户提供参考图 ref 并确认多视角一致性与不可见面推测策略
- **THEN** 编译产物引用该 exact ref 且声明 `multi_view_consistency` 约束，不复制参考图正文

### Requirement: 场景布局模板
系统 SHALL 提供 `3d-scene-layout-beta` 模板，输出 provider-neutral 的空间字段（物体清单、相对位置、尺度锚点、相机占位），不直接绑定 Scaena `SceneGEO` schema。

#### Scenario: Scaena 契约演进不破坏模板
- **WHEN** Scaena `SceneGEO` 或 `ReplicaStage` 契约发生 additive 或 major 变化
- **THEN** `3d-scene-layout-beta` 的 contract 无需 major 升级，兼容映射由后续 change 承担

#### Scenario: 无尺度锚点时显式声明
- **WHEN** 用户无法提供真实尺度参照
- **THEN** 编译产物显式标记尺度为相对比例，不使用米制「1:1」表述

### Requirement: 3D 打印约束模板
系统 SHALL 提供 `3d-printable-design-beta` 模板，把可制造性硬约束编译为检查清单式提示包。

#### Scenario: 打印约束编译
- **WHEN** 用户确认壁厚、支撑策略、公差与成型方向
- **THEN** 编译产物包含 `manifold_geometry` 约束与逐条可检查的打印约束清单

### Requirement: 3D 资产评审模板
系统 SHALL 提供 `3d-asset-review-beta` 评审清单模板，覆盖几何完整性、UV/贴图、比例与使用权。

#### Scenario: 评审清单覆盖四类检查
- **WHEN** 任意 3D 生成候选进入评审
- **THEN** 模板输出的清单逐项覆盖几何完整性、UV/贴图质量、比例一致性与 `rights_review`

### Requirement: 概念图到 3D 资产 recipe
系统 SHALL 提供 recipe `concept-to-3d-asset-beta`，表达「Eikona 概念图 → 图生 3D 精修 → 资产评审 → 显式导出」DAG，步骤只引用 exact `locale=en` template ref。

#### Scenario: 依赖缺失时不编造中间产物
- **WHEN** 概念图步骤尚无已接受的输出
- **THEN** 图生 3D 步骤保持 needs_step_output，不发明中间结果

#### Scenario: 步骤失效沿 DAG 传播
- **WHEN** 任一上游步骤的输入确认被撤销
- **THEN** 下游步骤按 DAG 失效传播规则标记失效

### Requirement: taxonomy 注册
系统 SHALL 在仓库分类法中注册 `3d` 一级类别与增量 namespace 值：`modality:3d`、`artifact:model_3d`、`artifact:scene_layout`、`constraint:manifold_geometry`、`constraint:scale_anchored`、`constraint:multi_view_consistency`，capabilities 增加 `model3d`、`scene_spatial`。

#### Scenario: 跨入口发现
- **WHEN** 消费方按 capability `model3d` 或 artifact `model_3d` 检索
- **THEN** 不依赖项目名即可发现 `3d` package 下对应 solution

### Requirement: locale 与元数据纪律
系统 SHALL 只为 5 个 solution 注册英文模板与英文 contract，中文译文以 `docs/template-zh-CN.md` 人工审阅形式存在；`solution.json`、`catalog.json` 与 recipe 元数据全部由 Registry CLI 生成。

#### Scenario: 中文不可编译
- **WHEN** 以 `locale=zh-CN` 请求编译任意 3d solution
- **THEN** Registry 拒绝编译，中文译文不进入 catalog template 列表或内容 digest

### Requirement: 3D 执行边界
系统 SHALL 保持模板只表达 Prompt 语义，不授予工具、凭据、费用或发布权限；3D 执行与 canonical 资产状态留在各自 owner。

#### Scenario: 模板不触发真实生成
- **WHEN** Agent 编译或导出任意 `3d` package 提示包
- **THEN** `provider_calls=0`，且普通输出不含模板正文、用户值或凭据

### Requirement: 转正门禁
系统 SHALL 让全部 5 个 solution 保持 beta ID 与 exploratory maturity，直到真实 provider 验证与评审完成。

#### Scenario: 未完成外部验证
- **WHEN** 尚未运行真实 3D provider 或完成评审
- **THEN** 文档与 catalog 不宣称已验证的生成质量，solution 不转为正式版本
