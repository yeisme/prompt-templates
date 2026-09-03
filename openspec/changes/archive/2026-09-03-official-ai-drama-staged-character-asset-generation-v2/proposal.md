## Why

现有角色资产包已经声明 face master、body master 和 turnaround 的依赖，也把 `views[]` 建模为独立视图；但旧的实测入口仍可能把整份元 Prompt 或“三等分面板”说明直接发送给图片 Provider，结果是一张图内重复人物、侧背视图错位，并且无法逐张返修。需要把“脸模先定版、主视图通过后再扩图、每张图独立生成”的生产语义提升为可验证合同。

## What Changes

- 新增阶段化角色资产生产合同：`face-master → body-master → base-wardrobe-front → derived views`，每一阶段都必须等待上游接受结果。
- 将 production `turnaround-three-view-v1` 明确为三个独立 artifact jobs；每个 job 只生成一个视图和一个人物实例。
- 保留现有 profile ID、schema version 与 valid fixture 的读取兼容，不把旧 profile 重命名或删除。
- 将 provider 生成的多宫格限定为 non-production quick preview；production 联系表由 consumer 对已生成单图进行确定性本地拼接。
- 新增脸部主视图、身体主视图和阶段门禁 fixtures，并补充元 Prompt 直发、单次多视图、缺失 accepted upstream ref 等 invalid cases。
- 文档提供“先脸、再主视图、后侧背图”的最短人工审稿流程与未来付费 canary 顺序。

## Capabilities

### New Capabilities

- `official-ai-drama-staged-character-assets`: 角色资产的阶段依赖、单视图生产语义、本地联系表和兼容迁移合同。

### Modified Capabilities

- 无。`official-ai-drama-character-asset-templates` v1 和既有 profile 保持可读，本变更通过新增字段、fixtures 与 consumer 约束扩展生产语义。

## Impact

- 影响 `solutions/video/ai-drama-character-assets/` 的公开 Prompt、task modules、fixtures、使用说明、审稿清单和失败模式文档。
- Prompt 仓库继续只拥有公开内容与 conformance 语义，不执行模型、不保存图片，也不决定候选接受或生产冻结。
- Eikona 负责把每个 view 编译为独立 provider job、生成本地联系表并记录运行证据；Scaena 继续负责 canonical SubjectVersion 和 production acceptance。
- 迁移是 additive：旧 quick-preview 内容仍可读取，但不得作为 production acceptance evidence。
