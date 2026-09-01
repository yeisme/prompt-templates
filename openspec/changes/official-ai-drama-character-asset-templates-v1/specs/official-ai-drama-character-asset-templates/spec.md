## ADDED Requirements

### Requirement: 官方包必须提供完整和模块化两种作者体验
Solution MUST 包含可直接导入的完整角色资产 JSON/YAML，以及通过 exact refs组合的 Character、Wardrobe、Task、Layout和QC模块；两种表达 MUST 使用相同 Schema和compiler profile。

#### Scenario: 武侠女性三视图等价
- **WHEN** consumer加载single-file JSON和modular YAML fixtures
- **THEN** 它们产生相同canonical task和Prompt Bundle digest

### Requirement: 官方 YAML 必须遵守安全子集
官方模板 MUST 不使用 anchor、alias、merge key、自定义tag、非字符串map key、隐式timestamp或非有限数值，并 MUST 通过Promptrepo strict parser。

#### Scenario: 内容仓库验证
- **WHEN** catalog/release validation扫描所有YAML模板
- **THEN** 安全子集违规被blocking finding拒绝

### Requirement: 武侠三视图必须锁定身份、材料、视图和鞋型
Fixture MUST 结构化表达成年身份、左右marker、身体比例、汉服层级、薄纱/丝绸coverage、前侧背view、对齐、帆布鞋和blocking QC，不得只依赖positive/negative Prompt文字。

#### Scenario: 薄纱安全
- **WHEN** valid fixture描述胸前semi-transparent outer layer
- **THEN** 它同时绑定完整opaque inner coverage并通过material lint

### Requirement: 官方包必须提供 invalid conformance matrix
Solution MUST 提供至少 duplicate key、alias、fixed seed missing、marker mirror、material coverage、back face、shoe drift、DRAFT reference、production replace override和unknown field负向fixtures。

#### Scenario: Consumer conformance
- **WHEN** Promptrepo、Scaena或Eikona运行官方invalid fixture matrix
- **THEN** 每个fixture以预期stable reason code在provider call前失败

### Requirement: Compiler profile 必须声明式且公开可审阅
Compiler profile MUST 只声明section order、field mapping、constraint precedence、locale fallback和compatible implementation family，不得包含或引用可执行代码。

#### Scenario: 发布扫描
- **WHEN** profile包含script path或executable media type
- **THEN** Registry/content validation拒绝solution release

### Requirement: Metadata 必须由维护服务生成
`solution.json`、document descriptors、Schema/compiler/fixture manifests、catalog和release lock MUST 由Template Registry CLI/application service创建或修改；人工不得手写这些machine assets。

#### Scenario: Catalog build
- **WHEN** 作者完成Prompt prose和通过authoring service保存的structured source
- **THEN** Registry维护命令生成确定性metadata并通过catalog validate

### Requirement: 资产预设必须声明真实依赖序
Solution MUST 明确区分目录顺序和生产依赖顺序，并 MUST 将 `expression-sheet-v1` 定义为只依赖 accepted face master 的脸部级资产；`turnaround-three-view-v1` MUST 依赖已定稿的基础服装。

#### Scenario: Consumer 规划青衣资产
- **WHEN** consumer解析角色资产预设矩阵
- **THEN** 它在 face master 接受后即可规划 expression sheet
- **AND** 它在基础服装定稿前不得规划 production turnaround

### Requirement: Expression production 必须编译为独立 cells
Production `expression-sheet-v1` MUST 编译为六个独立生成单元，每个单元恰好包含一个成年主体和一个表情 delta；3×2 layout MUST 只用于确定性审稿联系表，不得要求 provider 在单张 production 图中同时生成六个身份实例。

#### Scenario: 生成青衣六表情
- **WHEN** task声明`subject_count=1`、`depiction_count=6`和`output_intent=independent_cells_plus_contact_sheet`
- **THEN** compiler输出六个稳定排序的expression views
- **AND** Eikona可用artifact title生成3×2联系表而不依赖图内文字

#### Scenario: Production 请求单次六格
- **WHEN** production task要求provider直接输出一张六格表情图
- **THEN** consumer以`EXPRESSION_SET_INVALID`或等价stable reason code在provider call前拒绝
- **AND** repair提示改用独立cells加contact sheet

### Requirement: Expression task 不得依赖 wardrobe canon
Expression task MUST 只绑定 exact accepted face master 作为 identity source。可见领口 MAY 作为 non-canonical `presentation_only` 约束出现，但 MUST NOT 创建、替换或隐式接受 wardrobe version。

#### Scenario: Face master 后立即生成表情
- **WHEN** face master已接受且body/wardrobe尚未定稿
- **THEN** expression task可使用空`wardrobe_json`继续编译
- **AND** Prompt Bundle明确领口不得向下游继承为服装事实

### Requirement: Identity reference 必须声明继承与禁止继承边界
Expression identity binding MUST 继承脸部几何、五官关系、肤色范围、永久marker、发际线和基础发型外轮廓，并 MUST 禁止继承源表情、妆容、服装、背景和戏剧化调色。

#### Scenario: Identity source 同时含有戏剧化妆容
- **WHEN** accepted face image包含不属于身份本体的妆容或服装信息
- **THEN** compiler在reference policy中把这些方面列入`must_not_influence`
- **AND** 未声明的视觉信息不得进入expression continuity

### Requirement: 多发型必须经过独立 relock
基础发型 MUST 随 face master 锁定。Expression task MUST NOT 修改发型；任何替换发髻、束发或其他剧情发型 MUST 进入独立 hairstyle task，并在成为可用 reference 前重新验证脸部身份。

#### Scenario: Ceremony 发髻混入 expression task
- **WHEN** task在生成表情的同时请求把基础低束发改成礼服发髻
- **THEN** compiler以`HAIRSTYLE_RELOCK_REQUIRED`阻塞
- **AND** repair提示创建独立hairstyle/relock任务

### Requirement: Expression capture 与强度必须可比较
Task MUST 固定正面平视、bust裁切、头部姿态、gaze target、人物占比、曝光和主光方向。Intensity MUST 是`0..4`的单个整数；表情只能改变允许的脸部肌肉与呼吸观感，不得通过头部、肩线、镜头或服装变化表现强度。

#### Scenario: Resolve 改变头部角度
- **WHEN** cell instruction要求“下颌抬起”并改变既定head pitch
- **THEN** compiler产生`EXPRESSION_CAPTURE_CONFLICT`
- **AND** repair将其改写为下颌肌张力增加但头部角度不变

#### Scenario: 强度写成范围
- **WHEN** expression intensity为`2→3`或其他非单值
- **THEN** validation以`EXPRESSION_INTENSITY_INVALID`失败

### Requirement: Seed policy 不得冒充身份保证
`family_locked`或`fixed` seed MUST 只描述rerun/comparison policy。Solution MUST NOT 声称相同seed保证身份一致、像素级复现或跨provider确定性；production identity acceptance MUST 依赖exact refs/digests、QC evidence和human review。

#### Scenario: Provider只支持rerunnable seed
- **WHEN** Eikona capability evidence表明provider接受seed但不保证确定输出
- **THEN** review材料把运行标记为rerunnable而非deterministic
- **AND** identity QC仍保持blocking

### Requirement: Expression repair 必须有界
单个cell失败时，repair MUST 保持原identity、capture和reference lineage，只修改finding指向的expression、capture或presentation维度。两个及以上cells同时发生identity/capture drift时，系统 MUST 升级为批次级baseline blocker。

#### Scenario: 一个 grief-held cell 表情过度
- **WHEN** 只有该cell触发`EXPRESSION_RANGE_OVERSHOOT`
- **THEN** repair只降低该cell强度并保留其他五格

#### Scenario: 三个cells同时换脸
- **WHEN** 三个cells触发identity drift
- **THEN** 系统停止逐格repair并要求检查face master、binding或capture baseline

### Requirement: Expression sheet 不得声明为训练就绪数据集
Solution MUST 将 expression sheet 标记为表情校准和身份压力测试资产，而不是LoRA-ready dataset。任何训练用途 MUST 使用独立profile并补充训练权利、来源lineage、去重、角度/景别覆盖和专用acceptance gate。

#### Scenario: 用户计划训练 LoRA
- **WHEN** consumer希望把六个同机位expression cells用于训练
- **THEN** solution返回独立dataset profile需求
- **AND** 不把当前expression sheet标记为training-ready
