## ADDED Requirements

### Requirement: 官方 Graph Kit 必须是完整原子 solution closure
官方仓 MUST 提供 `longform.generic.v2` solution，manifest 锁定 source adapter、lens、view、validator、schema、compiler profile 和 fixture 的 exact refs/digests。任一 required child 改变 MUST 产生新 solution version。

#### Scenario: 完整 closure 被 catalog 构建
- **WHEN** Registry CLI build/validate official repository
- **THEN** solution 和所有 required child 均可解析且 digest 一致，缺任一 child 时验证失败

### Requirement: 官方 Kit 不得包含私有项目内容
Solution source、contracts、fixtures 和 metadata MUST NOT 包含真实项目人物/剧情、Nishi fixture、绝对路径、Overlay、source refs、credential、raw prompt 或 provider payload。

#### Scenario: 私有内容扫描
- **WHEN** catalog/fixture/release validation 扫描 official solution
- **THEN** 任一 private sentinel 或绝对项目路径使验证失败，且 routine output 不回显 body

### Requirement: 结构化 metadata 必须由 Registry CLI 生成
`solution.json`、catalog、document descriptors、schemas/compiler profiles、fixture manifest 和 release lock MUST 通过 Template Registry CLI/application service 创建和验证，不得由维护者直接拼写 digest 或 state。

#### Scenario: 创建官方 solution
- **WHEN** 维护者完成中文 source prose
- **THEN** 通过 Registry authoring commands 生成全部 structured assets，相同输入重放确定且不同 bytes 冲突或产生新 version

