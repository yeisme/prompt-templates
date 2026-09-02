## ADDED Requirements

### Requirement: 每个语义物件必须独立设计和输出
`semantic-object-v1` SHALL 表达一个可搬动、可持有、可交互或具有剧情状态的对象，并默认输出透明 RGBA。模板 MUST 禁止人物、手、身体、场景、地面和无关道具进入 canonical object asset。

#### Scenario: 独立武器物件
- **WHEN** 输入描述一把具有损坏前后状态的武器
- **THEN** 每个状态拥有独立 DesignSpec/RenderRevision ref
- **AND** 输出不包含持有者、手、腰带或场景背景

### Requirement: 空场景壳必须无人物和独立物件
`empty-scene-shell-v1` SHALL 输出完整不透明的建筑、地形、固定设施、灯光、机位、深度和遮挡结构。它 MUST 排除人物、肢体、人影、倒影、照片、海报人物、雕像、模特、车辆乘员和所有独立 `semantic_object`。

#### Scenario: 室内空场景包含桌上杯子
- **WHEN** 候选场景壳包含可搬动杯子
- **THEN** review checklist 将杯子标记为应拆分的 `semantic_object`
- **AND** 该候选不得作为干净 empty scene shell 接受

### Requirement: 物件视图必须按几何自适应
`semantic-object-v1` SHALL 根据 topology/geometry family 选择 view plan，并记录 rationale。模板 MUST 不对所有物件机械要求六视图，也不得遗漏风险所需的左右、背面、顶部、底部、细节或变形状态。

#### Scenario: 平面徽章物件
- **WHEN** 物件为正反面信息不同的平面徽章
- **THEN** view plan 至少包含 front、back 和必要 detail
- **AND** 不要求无生产价值的角色式六视图

### Requirement: 人物与背景输出语义必须相反且明确
人物/物件隔离资产 SHALL 要求透明 Alpha；`environment_shell` SHALL 要求完整不透明画布。模板 MUST 将棋盘格、纯色抠图底、白底或黑底与真实透明 Alpha 区分开。

#### Scenario: 场景模板收到透明背景要求
- **WHEN** `empty-scene-shell-v1` 输入要求透明输出
- **THEN** 模板验证返回 blocking output finding
- **AND** 提示改用完整不透明 scene-shell contract
