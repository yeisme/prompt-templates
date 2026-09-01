# 提案：AI 做剧人物/背景隔离资产 v1

> 状态说明：该 change 保留为 `face-mask-front-v1` 与 `clean-background-plate-v1` 的窄兼容切片。新的模块化人物、物件、场景和预览能力由 `official-ai-drama-modular-visual-assets-v2` 承接；本 change 不扩张为头发、服饰或整套资产包 owner。

## 问题

既有 `face-master-v1` 面向肩部以上的中性棚拍母版，不能稳定表达“只有正脸、无发饰、无脖子肩膀、真实透明 Alpha”的独立脸模；角色 solution 也混有场景能力，缺少严格的零人物背景模板。

## 变更

- 保留 `face-master-v1` 语义，新增 `face-mask-front-v1`。
- 新增可选 `task.isolation_mode`，缺省为 `studio_neutral`。
- 新增 `ai-drama-background-assets` 和 `clean-background-plate-v1`。
- 人物与背景分属独立任务、run 和 review artifact，基础资产阶段禁止合成。
- 新增 valid/invalid fixtures，覆盖透明人物与零人物背景的阻断规则。

## 兼容性

这是加法变更。旧 profile、旧 schema version 和旧 fixture 保持可读；`environment_only` 不改变角色 Bundle，而是明确转交背景 solution。`1.0.0` 发布物不原地修改，当前内容形成 `1.1.0` release candidate，真实发布另行执行。
