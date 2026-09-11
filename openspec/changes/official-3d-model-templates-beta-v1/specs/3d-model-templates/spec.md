## ADDED Requirements

### Requirement: 可编译的 3D 模型模板包
系统 SHALL 以新的 beta exact ref 提供 `3d` package 下的英文可编译模板，覆盖文生 3D 单物体、图生 3D 精修、场景布局、3D 打印约束与资产评审，并保留现有引用不变。

#### Scenario: 用户编译并复用 3D 提示包
- **WHEN** 用户提供并确认目标产物、用途（游戏/打印/影视背景）、风格、尺度与约束
- **THEN** Registry 能在零 provider 调用下编译、导出和验证提示包，替换主题后可建立独立会话复用

#### Scenario: 缺字段或未确认时拒绝编译
- **WHEN** 必填输入缺失或用户尚未确认关键创作选择
- **THEN** 编译以可读错误拒绝，不调用任何模型或网络

### Requirement: 3D 执行边界
系统 SHALL 保持模板只表达 Prompt 语义，不授予工具、凭据、费用或发布权限；3D 执行与 canonical 资产状态留在各自 owner。

#### Scenario: 模板不触发真实生成
- **WHEN** Agent 编译或导出任意 `3d` package 提示包
- **THEN** `provider_calls=0`，且普通输出不含模板正文、用户值或凭据

### Requirement: 场景布局字段保持 provider-neutral
系统 SHALL 让 `3d-scene-layout-beta` 输出通用空间字段，不直接绑定 Scaena `SceneGEO` schema。

#### Scenario: Scaena 契约演进不破坏模板
- **WHEN** Scaena `SceneGEO` 或 `ReplicaStage` 契约发生 additive 或 major 变化
- **THEN** `3d-scene-layout-beta` 的 contract 无需 major 升级，兼容映射由后续 change 承担

### Requirement: 转正门禁
系统 SHALL 在所有 5 个 solution 保持 beta ID 与 exploratory maturity，直到真实 provider 验证与评审完成。

#### Scenario: 未完成外部验证
- **WHEN** 尚未运行真实 3D provider 或完成评审
- **THEN** 文档与 catalog 不宣称已验证的生成质量，solution 不转为正式版本
