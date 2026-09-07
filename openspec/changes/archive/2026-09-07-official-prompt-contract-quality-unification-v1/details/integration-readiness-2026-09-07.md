# 模板集成 readiness（2026-09-07）

当前 catalog 有 40 个 solution，所有 solution 都已有 discovery tags 与粗粒度 capabilities。新增 `agent/template-skill-integration-design-beta@1.0.0-beta.1?locale=en` 可编译 Integration Brief；Film 七个英文 role 已使用具体 `required_capabilities`。

剩余 11 个集成缺口：

| 批次 | Solution | 缺口 | 处理方式 |
| --- | --- | --- | --- |
| 1 | `general/structured-summary` | `main.en` contract | 升级 source boundary、输出结构和最小 fixture |
| 1 | `office/meeting-action-summary` | `main.en` contract | 明确事实、决定、owner、due date 与 unknown |
| 1 | `research/evidence-research-brief` | `main.en` contract | 明确 source/citation/conflict 与 evidence gate |
| 2 | `engineering/bug-root-cause-analysis` | `main.en` contract | 绑定 reproduction、evidence、hypotheses 和 verification |
| 2 | `product/prd-acceptance-criteria` | `main.en` contract | 绑定用户、能力 ledger、acceptance 与 test evidence |
| 2 | `agent/tool-use-handoff` | `main.en` contract | 绑定 owner、tool capability、permission 和 result handoff |
| 3 | `writing/longform-outline` | `main.en` contract | 绑定 premise、audience、structure 和 constraints |
| 3 | `learning/socratic-study-plan` | `main.en` contract | 绑定目标、基线、节奏和 assessment |
| 3 | `marketing/xhs-campaign-copy` | `main.en` contract | 绑定产品事实、受众、平台限制和 claims review |
| 3 | `video/short-drama-character-consistency` | `main.en` contract | 绑定角色事实、镜头输入和 continuity findings |
| 4 | `graph/longform.generic.v2` | 无英文 Agent template | 建立新英文 exact version；历史中文 Graph Kit 保持兼容，不原地改写 |

前三批分别对应 tasks 4.1、4.2、4.3。每个模板完成条件是英文 contract、placeholder parity、provider-free validate/preview、公开虚构 fixture 和目标消费者 canary。Graph Kit 单独走 locale/version migration，不能把历史 `zh-CN` exact ref 静默改成 `en`。
