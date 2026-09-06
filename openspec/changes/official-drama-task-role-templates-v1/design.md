# Design: 做剧任务角色模板与 Skill 依赖削减

## 1. 目标架构：三层分工

把"做剧"能力从单一 Skill 矩阵重构为三层，模板成为任务角色的 canonical 载体：

| 层 | 载体 | 职责 | 特征 |
| --- | --- | --- | --- |
| 模板层 | 本仓库 `solutions/writing/ai-drama-*` | 任务角色的方法、输入合同、输出合同、质量门槛 | 确定性编译、版本化 exact ref、provider-free、无宿主依赖 |
| 路由层 | `.skills/yeisme/ai-drama/ai-drama-router` | 十五轴意图识别、originality 门禁、artifact lifecycle、阶段衔接、模板 ref 解析 | 唯一 Skill 入口，轻量，不承载创作方法 |
| 编排层 | `ai-drama-production-orchestrator`、`ai-drama-producer`、`ai-drama-context-pack-builder`、宿主 CLI | 跨阶段运行/恢复、预算/批次、宿主 artifact 读取、provider 调度 | 需要工具与宿主状态，不可模板化 |

判断标准：一个能力若只需要"输入投影 → 方法 → 语义化 proposal"，它属于模板层；若需要读宿主状态、调用工具、持有门禁权限或跨 owner 编排，它留在 Skill 层。

## 2. 迁移映射（第一波）

| 模板 solution | 吸收的 Skill | 输出 proposal | 关键门禁（从 Skill 迁入模板质量门槛） |
| --- | --- | --- | --- |
| `writing/ai-drama-format-strategy` | `ai-drama-format-strategist` | `DramaFormatContract` proposal | 形态必须改变结构判断；副类型不得建立第二条主故事引擎；制作密度冲突先降级 |
| `writing/ai-drama-story-architecture` | `ai-drama-story-architecture` | `StoryProposal` | beat 十字段（goal/obstacle/choice/cost/new_information/relationship_delta/emotion_*/visual_action/next_question）；choice/cost 缺失只能 draft |
| `writing/ai-drama-character-engine` | `ai-drama-character-engine` | `CharacterProposal` | 动机-秘密-知识边界一致性；行动可模拟；不给作者方便型行为 |
| `writing/ai-drama-showrunner` | `ai-drama-showrunner` | `ShowrunnerPlan` proposal | >5 集必须 proof slice（3 集、每集一个核心场景合同、A/B 候选策略差异≥2 维）；expansion gate 四条件 |
| `writing/ai-drama-scene-writing` | `screenplay-scene-writer`（路由矩阵角色面） | `SceneDraft` proposal | 可拍性（动作/空间/转场可执行）；潜台词显式；对白服务人物声音 |
| `writing/ai-drama-critic-review` | `ai-drama-critic-panel` | `CriticReviewFindings` | 同比较类才可比较；findings 带稳定 code/severity/observable basis；修复有界、单变量 |

第二波（后续 change，不在本 change）：`ai-drama-director`（导演调度）、`ai-drama-visual-language`、`ai-drama-edit-and-sound`、`ai-drama-continuity-supervisor` 中尚未被 `video/ai-film-multi-profile-production` 覆盖的部分，以及 `ai-drama-assessment` 的 rubric 面（其合同冻结门禁保留在 Skill 层）。

## 3. 模板形态

- 单一 `main` 角色，英文模板 `prompts/main.en.md`，companion contract `contracts/main.en.json`。
- 输入全部是有界安全投影 JSON（`format_contract_json`、`context_pack_json`、`creative_brief_json`、`task_delta_json`、`output_language` 等），由消费方 owner 筛选；敏感输入标 `sensitivity: sensitive`。
- 输出为语义化 proposal（semantic fields + findings + bounded_next_actions + uncertainty），不带 canonical refs、digest、accepted 状态、provider 字段。
- 阶段链用 exact ref 衔接：`promptrepo://official/writing/ai-drama-format-strategy@1.0.0` 的输出投影可作为 `ai-drama-story-architecture` 的 `format_contract_json` 输入；模板间不复制正文或 schema。
- 中文译文 `docs/template-zh-CN.md` 仅供人工审阅（仓库 locale 政策）。

## 4. Skill 依赖削减（由 `.skills/yeisme` 变更执行）

- 路由表：被迁移意图的 Primary 从子 Skill 改为模板 exact ref（消费方经 `template-registry prompt compile` 或 owner CLI 编译），constraint Skill 保留。
- 退役：`ai-drama-format-strategist`、`ai-drama-story-architecture`、`ai-drama-character-engine`、`ai-drama-showrunner`、`ai-drama-critic-panel` 五个 Skill 目录。
- 保留：`ai-drama-router`（瘦身为模板路由）、`ai-drama-assessment`（评估合同门禁）、`ai-drama-context-pack-builder`（宿主 artifact 投影）、`ai-drama-producer`、`ai-drama-production-orchestrator`、`ai-drama-director`、`ai-drama-visual-language`、`ai-drama-edit-and-sound`、`ai-drama-continuity-supervisor`、`ai-drama-video-reference-director`（第二波候选）、`manga-drama-project-starter`、`auctra-ai-drama-panel-handoff`。
- 解析策略新增：模板承载意图的 `resolution_status=template_ref_available`，不再触发 `needs_install_decision` 或 Skill 安装。
- 独立 Agent 最短路径：只装 `ai-drama-router` 一个 Skill + 模板目录即可跑全任务角色链，不再按需安装矩阵子 Skill。

## 5. 边界

- 模板不执行 provider、不写 canonical、不持有 originality 决策（留在 Router 门禁）。
- 不修改既有 `video/` 做剧 solution 的 ID、正文或 ref。
- 评估合同（`AssessmentContract` 冻结、score eligibility）仍归 `ai-drama-assessment` Skill；`ai-drama-critic-review` 只做候选比较与有界修复建议，不合成未经合同批准的综合分。
