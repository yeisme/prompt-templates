## 设计

### Role capability

`solution.json.capabilities` 继续服务搜索与粗筛。exact 执行准入由 role 对应 document descriptor 的 `required_capabilities` 表达：

| Role | Capability | Consumer |
| --- | --- | --- |
| `project-intent` | `film_project_intent` | Auctra |
| `asset-dependency` | `film_asset_dependency` | Eikona |
| `scene-package` | `film_scene_package` | Scaena |
| `shot-prompt` | `film_shot_semantics` | Scaena |
| `shot-audio-intent` | `film_audio_intent` | Sonora |
| `continuity-review` | `film_continuity_review` | Scaena |
| `failure-restructure` | `film_failure_restructure` | Auctra |

### Provider delivery 分层

每个 direct-to-provider solution 分成三种职责：

1. authoring guide：变量说明和维护者提示；
2. validation policy：确定性检查和人工 review；
3. delivery body：唯一允许发送给 Provider 的正文。

新增 delivery role 时复用同一 source 意图和 companion contract，不在运行时按 Markdown 标题裁剪正文。

### 基础模板升级批次

1. `structured-summary`、`meeting-action-summary`、`evidence-research-brief`；
2. `bug-root-cause-analysis`、`prd-acceptance-criteria`、`tool-use-handoff`；
3. writing、learning、marketing、short-drama 基础模板。

每批至少补齐输入声明、untrusted source 边界、输出字段/格式、failure mode、review checklist 和最小 fixture。成熟度只随 exact template conformance 与真实证据提升。

## 迁移与回滚

- 未发布候选可刷新 digest；已发布 ref 只新增 version/role。
- consumer 尚未支持 role capability 时返回 incompatible/needs_contract，不回退成错误的 generic support。
- 回滚新增 role 或 metadata 时保留旧 snapshot 和旧 generic discovery。
