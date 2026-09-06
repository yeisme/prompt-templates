## Why

AI 做剧能力目前以 16 个 Skill 的矩阵形态维护在 `.skills/yeisme/ai-drama/`。其中任务角色类 Skill（形态策略、故事架构、人物引擎、分集规划、场景写作、评审团）本质是"方法 + 输入合同 + 输出合同"的确定性提示内容，不依赖宿主工具；把它们留在 Skill 层造成三重成本：每个消费方（Auctra/Scaena/Eikona/Sonora/独立 Agent）必须安装并解析 Skill、内容无法版本化精确引用、与官方 Prompt 目录的 `promptrepo://` exact ref 生态脱节。

## What Changes

- 新增官方 `writing` 包做剧任务角色模板第一波，共六个 solution，每个单一 `main` 角色、英文可编译模板 + companion contract：
  - `writing/ai-drama-format-strategy@1.0.0`：剧型/形态/类型契约编译（吸收 `ai-drama-format-strategist` Skill）。
  - `writing/ai-drama-story-architecture@1.0.0`：premise/冲突链/beat cards（吸收 `ai-drama-story-architecture` Skill）。
  - `writing/ai-drama-character-engine@1.0.0`：动机/秘密/关系/知识边界（吸收 `ai-drama-character-engine` Skill）。
  - `writing/ai-drama-showrunner@1.0.0`：季/集规划 + proof slice + expansion gate（吸收 `ai-drama-showrunner` Skill）。
  - `writing/ai-drama-scene-writing@1.0.0`：可拍场景/动作/对白/潜台词/转场（吸收路由矩阵中 `screenplay-scene-writer` 角色面）。
  - `writing/ai-drama-critic-review@1.0.0`：多候选比较评审/选优/有界修复（吸收 `ai-drama-critic-panel` Skill）。
- 每个 solution 提供 owner 边界、安全投影输入、语义化输出 schema、无思维链自检，输出为 reviewable proposal，不是 canonical state。
- 模板之间通过 exact `promptrepo://official/writing/ai-drama-*@1.0.0` ref 衔接阶段链（format → story → showrunner → scene → critic），不复制彼此正文。
- 中文译文进 `docs/template-zh-CN.md` 供人工审阅，不注册为可编译模板。
- 配套 Skill 矩阵收编与依赖削减由 `.skills/yeisme` 仓库的变更执行；本 change 只定义模板侧合同与迁移映射。

## Capabilities

### New Capabilities

- `official-drama-task-role-templates`: AI 做剧任务角色的官方可编译模板：剧型策略、故事架构、人物引擎、分集规划、场景写作与多候选评审。

### Modified Capabilities

无。现有 `video/` 做剧资产/分镜/多 profile 生产 solution 保持独立、可版本固定。

## Impact

- 内容路径：`solutions/writing/ai-drama-*/`；结构化 metadata 由 Template Registry CLI 生成。
- 消费方：Auctra（canonical story/episode owner）、Scaena（生产编排）、独立 Agent（`template-registry prompt` 工作流）；各自拥有 typed validator、执行、评审与接受。
- Skill 矩阵：`.skills/yeisme/ai-drama` 中对应任务角色 Skill 退役，`ai-drama-router` 路由表改指模板 exact ref。
- Public ref/DTO：`shared/promptrepo`；catalog/release：`backend-server/template-registry`。
