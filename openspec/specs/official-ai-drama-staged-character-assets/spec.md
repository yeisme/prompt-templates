# official-ai-drama-staged-character-assets Specification

## Purpose
TBD - created by archiving change official-ai-drama-staged-character-asset-generation-v2. Update Purpose after archive.
## Requirements
### Requirement: 角色资产生产必须按主资产门禁推进
Production 角色资产 MUST 按 face master、body master、base-wardrobe front、derived turnaround views 的依赖推进。任何下游阶段 MUST 绑定 exact accepted upstream refs，并 MUST NOT 因为 bundle 可解析而跳过人工接受门。

#### Scenario: 主视图尚未接受时请求背面
- **WHEN** `turnaround-three-view-v1` 的 back view 缺少 accepted base-wardrobe-front ref
- **THEN** consumer 在 Provider 调用前阻断该 view
- **AND** 提示先完成人脸、身体和正面主视图门禁

### Requirement: Production 每个 view 必须成为独立 artifact job
Production compiler MUST 将 `views[]` 的每个条目编译为独立 job；每个 job MUST 只包含一个 view role、一个人物实例和一个预期图片 artifact。它 MUST NOT 请求 Provider 在一张图内生成 turnaround grid、contact sheet 或多个身份实例。

#### Scenario: 三视图 Bundle 进入 production
- **WHEN** consumer 读取含 front、left_profile、back 的 `turnaround-three-view-v1` Bundle
- **THEN** 它按稳定顺序得到三个独立 jobs
- **AND** 每个 job 的 `provider_artifact_count` 为 1

#### Scenario: 调用方显式请求 production 三宫格
- **WHEN** production task 要求单次 Provider 请求输出三视图网格
- **THEN** consumer 以 `CHARACTER_ASSET_PROVIDER_GRID_FORBIDDEN` 或等价 stable reason code 阻断
- **AND** Provider calls 保持为 0

### Requirement: 主视图必须先于派生旋转视图接受
`turnaround-three-view-v1` 的 front view MUST 作为 base-wardrobe main view 先生成和接受。Left/right profile 与 back views MUST 继承 accepted face、body 和 front wardrobe silhouette，并 MUST 保持各 reference 的 inherit/forbid 边界。

#### Scenario: 正面主视图通过后生成左侧面
- **WHEN** face、body 和 base-wardrobe front refs 均为 accepted 且版本/digest 精确匹配
- **THEN** left-profile job 可以进入既有 cost/auth/provider gate
- **AND** 它不得修改身份 marker、身体比例、服装层级或鞋型

### Requirement: Face master 必须是单张中性正面身份图
`face-master-v1` production output MUST 是一张成年主体的正面中性 bust/portrait，不得包含多宫格、服装设定表、侧背视图或第二个人物。它 MUST 只锁身份相关特征，不得接受剧情服装、背景或戏剧化灯光为角色 canon。

#### Scenario: 首次角色 canary
- **WHEN** 用户明确授权一次真实 face-master canary
- **THEN** 执行输入只包含一个 face-master front/detail view
- **AND** body、wardrobe 与 turnaround stages 保持未执行

### Requirement: Body master 必须继承 accepted face 并保持服装中性
`body-master-v1` MUST 绑定 exact accepted face master，生成一张正面全身中性站姿，并锁定身体比例、肩胯和四肢轮廓。它 MUST NOT 在该阶段接受剧情服装或派生视图。

#### Scenario: Body master 缺失 accepted face
- **WHEN** body-master task 没有可解析的 accepted face master ref
- **THEN** consumer 在 Provider 调用前返回 blocking finding
- **AND** 不创建 body artifact 或下游 stage

### Requirement: 联系表必须是本地 review projection
Turnaround contact sheet MUST 由 consumer 对独立图片 artifacts 进行确定性本地拼接。它 MUST 保留稳定 view order 和 source artifact refs，并 MUST NOT 替代单图 acceptance、单图 repair 或 canonical subject assets。

#### Scenario: 背面图局部返修
- **WHEN** back artifact 被替换而 front 与 left-profile 保持不变
- **THEN** consumer 只更新 back artifact ref 并重建本地联系表
- **AND** 不重新调用 Provider 生成 front 或 left-profile

### Requirement: 旧 profile 与 Bundle 必须保持可读兼容
Consumer MUST 继续读取既有 `character_asset.prompt_bundle.v1` 与现有九个 profile IDs。旧 Bundle 中的多宫格 composition 文本 MUST NOT 导致 production 单次多视图请求；consumer MUST 正规化为单视图 composition 或在无法安全正规化时阻断。

#### Scenario: 读取旧武侠三视图 fixture
- **WHEN** 旧 fixture 含“三格等宽排列”且 `views[]` 仍为 front、left_profile、back
- **THEN** production consumer 保留三个 view keys 与稳定顺序并拆成独立 jobs
- **AND** 输出 `LEGACY_MULTI_PANEL_LAYOUT_NORMALIZED` compatibility finding，不删除或重命名旧 profile

### Requirement: 元 Prompt 不得直接进入图片 Provider
仓库的 compiler meta-prompt、schema instruction 或要求模型输出 Prompt Bundle 的正文 MUST NOT 直接作为图片生成请求。图片 Provider 只能收到 consumer 从已验证 Bundle 为单一 view 渲染的用户级视觉 Prompt。

#### Scenario: 实测程序尝试发送 main Prompt 元说明
- **WHEN** canary 输入是要求生成 `character_asset.prompt_bundle.v1` JSON 的元 Prompt
- **THEN** consumer 以 `CHARACTER_ASSET_META_PROMPT_FORBIDDEN` 在 Provider 调用前拒绝
- **AND** 不创建图片 run 或 artifact

