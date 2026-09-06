# official-drama-task-role-templates Specification

## ADDED Requirements

### Requirement: 做剧任务角色模板必须可独立编译

每个做剧任务角色 solution SHALL 只依赖其 companion contract 声明的输入即可编译，不要求安装任何 Skill、宿主仓库或 Provider 配置。模板输出 SHALL 是语义化 proposal（含 findings 与 bounded next actions），MUST NOT 包含 canonical refs、digest、accepted 状态、预算回执或 Provider 字段。

#### Scenario: 独立 Agent 编译故事架构模板

- **WHEN** Agent 通过 `template-registry prompt compile` 提交 `writing/ai-drama-story-architecture@1.0.0` 的完整输入
- **THEN** 编译 SHALL 成功产出可投递模型的结构化提示包
- **AND** SHALL NOT 要求安装 ai-drama Skills 或配置 Provider。

### Requirement: 形态策略模板必须输出可执行形态合同提案

`writing/ai-drama-format-strategy` SHALL 输出 `format_profile`、主/副类型、观众承诺、结构单位、时长与集数形态、回报节拍、可重复故事引擎、制作密度与状态字段；状态字段 SHALL 限定为 `ready`、`needs_format_decision`、`needs_audience`、`genre_conflict`、`production_mismatch`。

#### Scenario: 形态未定时要求决策

- **WHEN** 两种候选形态会实质改变结构、成本或用户承诺，且输入未包含决定
- **THEN** proposal 状态 SHALL 为 `needs_format_decision`
- **AND** SHALL 列出备选形态与各自结构后果，不替用户猜承载形态。

### Requirement: 故事架构模板必须输出十字段 beat cards

`writing/ai-drama-story-architecture` 输出的每个 beat SHALL 标注 `goal`、`obstacle`、`choice`、`cost`、`new_information`、`relationship_delta`、`emotion_before`、`emotion_after`、`visual_action`、`next_question`。`choice` 或 `cost` 缺失的 beat SHALL 标记为 `draft` 且 MUST NOT 进入生产拆解建议。

#### Scenario: beat 缺少代价

- **WHEN** 某个 beat 的 `cost` 无法从输入推导
- **THEN** 该 beat SHALL 保留在 proposal 中并标记 `draft`
- **AND** findings SHALL 指出缺失字段与一个最小补齐动作。

### Requirement: 分集规划模板必须执行 proof slice 与 expansion gate

`writing/ai-drama-showrunner` 在新写或大幅重写超过 5 集时 SHALL 只输出 proof slice（3 个代表性压力场景集、每集一个核心场景合同、每场景至少两个策略差异候选），并输出 `expansion_gate`（状态变化、证据、Dialogue Live Test、用户声音选择）与 `unresolved_voice_questions`；用户确认主要人物声音前 MUST NOT 输出剩余全集内容。

#### Scenario: 请求全集一次生成

- **WHEN** 用户要求一次产出 10 集分集大纲而主要人物声音未确认
- **THEN** proposal SHALL 只包含 proof slice 与 gate 条件
- **AND** SHALL 说明剩余批次以每批最多 5 集在 gate 通过后继续。

### Requirement: 场景写作模板必须输出可拍场景草案

`writing/ai-drama-scene-writing` SHALL 输出 entry state、人物目标、可执行动作、对白与潜台词分离、信息释放次序、代价与 exit state；动作与转场描述 SHALL 可转成场面执行，MUST NOT 只用抽象情绪词替代可拍描述。

#### Scenario: 动作描述不可执行

- **WHEN** 生成的场景草案中存在无法转成场面行动的抽象描述
- **THEN** 该段 SHALL 标记为 `draft`
- **AND** findings SHALL 给出可执行化改写方向。

### Requirement: 评审模板必须执行同比较类约束

`writing/ai-drama-critic-review` SHALL 只在同一比较类（候选题材镜头、rubric、评价目标一致）内比较；每条 finding SHALL 带稳定失败 code、severity、observable basis 和一个最小修复步骤；修复建议 SHALL 有界、单变量。证据不足时 SHALL 输出定性观察并拒绝合成综合数字分。

#### Scenario: 跨题材候选比较

- **WHEN** 输入候选分属不同题材镜头或评价目标
- **THEN** proposal SHALL 返回 `assessment_not_comparable` 状态
- **AND** SHALL 说明不可比较的具体维度，不给排名或综合分。

### Requirement: 阶段链必须通过 exact ref 衔接

做剧模板之间 SHALL 通过 `promptrepo://official/writing/<solution>@<version>` exact ref 表达依赖；上游模板的输出投影 SHALL 能直接作为下游模板的同名输入；模板 MUST NOT 复制其他模板的正文、schema 或质量门槛。

#### Scenario: 形态合同投影进入故事架构

- **WHEN** `ai-drama-format-strategy` 的 proposal 经 owner 筛选后作为 `format_contract_json` 输入 `ai-drama-story-architecture`
- **THEN** 故事架构模板 SHALL 接受该投影而不要求重新填写形态字段
- **AND** findings SHALL 检出投影与创意简报的冲突。
