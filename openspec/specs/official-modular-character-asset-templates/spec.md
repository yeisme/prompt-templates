# official-modular-character-asset-templates Specification

## Purpose
TBD - created by archiving change official-ai-drama-modular-visual-assets-v2. Update Purpose after archive.
## Requirements
### Requirement: 官方角色模板必须覆盖模块化人物槽位
`ai-drama-character-assets@2.0.0` SHALL 提供 `head-core-bald-v1`、`body-core-neutral-v1`、`surface-coat-hair-v1`、`wearable-garment-v1` 和 `wearable-accessory-v1`。每个模板 MUST 输出一个主要 slot，不得把 sibling slot 或背景烘焙进同一 canonical asset。

#### Scenario: 生成角色头部核心
- **WHEN** authoring input 选择 `head-core-bald-v1`
- **THEN** Prompt Bundle 只要求完整无头发头部、自然头皮、双耳和脸部身份
- **AND** 禁止头发、发饰、耳饰、脖子、肩膀、服装、背景和外部投影

### Requirement: 角色身份必须由头部核心与身体核心共同定义
模板合同 SHALL 将 `head_core + body_core` 声明为 subject identity anchor。头发、服装、装饰和 extension MUST 作为可替换层引用该 anchor，并声明允许与禁止继承项。

#### Scenario: 发型层绑定角色
- **WHEN** hair DesignSpec 编译为 fitted render input
- **THEN** 它可以继承头型、头皮轮廓和 attachment landmarks
- **AND** 不得继承表情、服装、首饰或背景

### Requirement: 身体核心必须使用年龄适配中性覆盖
`body-core-neutral-v1` SHALL 使用无品牌、无装饰、完整覆盖的中性基础外观。未成年人 MUST 使用年龄适配、非成人化的姿态、材质和覆盖策略；任何年龄都不得要求显式解剖细节。

#### Scenario: 未成年人角色身体核心
- **WHEN** `age_band` 表示未成年人
- **THEN** 编译结果包含严格的 age-appropriate neutral coverage
- **AND** 成人化造型、透明材质和显式解剖要求形成 blocking finding

### Requirement: 角色生产视图必须独立生成
头部核心、身体核心和需要贴合证据的角色层 SHALL 支持六视图合同。每个 production view MUST 是单角色、单视角、单 artifact；模板不得要求 Provider 在一张图中生成 grid、contact sheet 或多个视图。

#### Scenario: 头部六视图 Bundle
- **WHEN** authoring input 请求完整 head core view set
- **THEN** Bundle 包含六个稳定排序的独立 view definitions
- **AND** 每个 view 的输出要求为单个透明 PNG artifact

### Requirement: 正脸头模必须使用严格捕获锁
`head-core-bald-v1` 的 `detail_front` view SHALL 固定 yaw=0、pitch=0、roll=0、双眼水平并直视镜头，保留完整头顶、后脑轮廓、双耳和下颌。它 MUST 不包含脖子、肩膀或服装，并要求真实透明 Alpha 和干净抗锯齿边缘。

#### Scenario: 输入要求灰色棚拍背景
- **WHEN** 用户约束要求灰色、白色、黑色或其他可见背景
- **THEN** 模板验证返回 blocking isolation finding
- **AND** 不得把该背景要求写入 production Prompt Bundle

