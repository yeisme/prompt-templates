# AI 做剧人物/背景隔离资产模板 v1

状态：candidate（内容已实现，provider-free 验证通过；人物侧 fixture 集被 Registry 禁止 `*ref` 键的语义门阻塞，见下；maturity=exploratory，未发布 release）
OpenSpec：[`official-ai-drama-isolated-visual-assets-v1`](../openspec/changes/official-ai-drama-isolated-visual-assets-v1/proposal.md)

本 change 是 `face-mask-front-v1` 与 `clean-background-plate-v1` 的窄兼容切片；头发、服饰、整套资产包与可拆物件等模块化能力由 `official-ai-drama-modular-visual-assets-v2` 承接。

## 交付内容

- `ai-drama-character-assets` 新增 role `isolated-character-assets-v1`：`face-mask-front-v1` 只允许一个 `detail` view（yaw/pitch/roll=0），沿完整下颌线收口，输出真实透明 Alpha 的 RGBA PNG；禁止背景、外部投影、悬浮阴影、发饰首饰与脖子肩膀。`face-master-v1` 既有语义不变。
- `task.isolation_mode` 可选枚举（`studio_neutral` 缺省 / `transparent_subject` / `environment_only`）：`environment_only` 阻断角色编译并返回 `ENVIRONMENT_ONLY_REQUIRES_BACKGROUND_TEMPLATE`，转交背景模板；不改动已发布 1.0.0 消费面。
- 新 solution `ai-drama-background-assets@1.0.0`（exploratory）：`clean-background-plate-v1` 直接可渲染零人物背景板（固定 `subject_count=0`、完整不透明画布）与 `validate-background-plate-v1` 校验合同。
- 人物与背景分属独立任务、run 与 review artifact；基础资产阶段禁止合成，合成只属于后续 shot/keyframe 工作流。

## Provider-free 验证记录（2026-09-02）

- `isolated-character-assets-v1` 与 `clean-background-plate-v1`、`validate-background-plate-v1` 的 `contract validate`、`document validate` 全部 success（Template Registry CLI）。
- `validate-background-plate-v1` fixture 集 `fixture validate` success：5 cases（1 valid + 4 invalid，稳定码覆盖人物/倒影/投影/雕像人形痕迹阻断）。
- `isolated-character-assets-v1` fixture 集 6 cases（1 valid + 5 invalid，新增 `face-mask-environment-only-handoff` 覆盖 environment_only 转交阻断）；**该集 `fixture validate` 当前失败**：Registry fixture 门禁止 valid 输出含 `*ref` 键，而 1.x `character_asset.prompt_bundle.v1` 合同要求 bundle 必含 `subject_version_ref`（Eikona 已归档 compiler 以 `DisallowUnknownFields` 强制该字段，模块化 v2 已按 `subject_version` 规避但明确决定 1.x 不改）。这是 Registry 门与 1.x bundle 合同的上游冲突，需要跨仓协调（门加 allowlist 或统一迁移），本内容仓不单方面重命名字段。
- catalog build 连续两次 digest 一致（`sha256:cb1dda68199eed2150f7bcd4c6128ab19322f693a980b5f59d003fdcffb35582`，19 solutions），`catalog validate` success。

## 交付边界

- 真实 Provider 调用次数 = 0：全部 fixture 为本地 JSON，无 credential、无 Provider payload、无运行证据入库。
- 未发布任何 release：无 commit/tag/push/publish 动作宣称发布；`promptrepo://official/video/ai-drama-character-assets@1.0.0` 已发布物不原地修改、不重解释。当前内容形成 1.1.0 release candidate（人物侧）与 1.0.0 exploratory candidate（背景侧），正式 internal immutable release 另行执行——Registry 现有 immutable release CLI（`graph-kit release create`）只锁 graph-kit profile，尚无普通 prompt solution 的 release family，且发布需要维护者 Git commit/tag 固定与授权。
- maturity 保持 `exploratory`，不宣称 first-support、production-ready 或 LoRA-ready。
- 回滚：移除消费方对 `face-mask-front-v1` 与 `ai-drama-background-assets` 的引用即可；旧 `face-master-v1` 路径继续工作。
