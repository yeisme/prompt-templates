# 内容编写指南

每个 solution 是可执行方案包，不是孤立 Prompt。正文应明确：

1. 角色和目标；
2. 必填输入变量；
3. 不可放宽的约束；
4. 输出结构；
5. 自检清单；
6. 无法满足时的诚实回退。

变量使用 `{{variable_name}}`。不要要求模型输出隐藏思维过程；需要解释时，只要求结论、关键证据、风险、权衡和下一步。

Locale 遵循 `docs/locale-policy.md`：Agent 可编译 solution 只注册 `en` 模板和 `en` contract。中文翻译放在 `docs/template-zh-CN.md`，只供人类审阅。

成熟度：

- `exploratory`：结构完整但验证有限；
- `first-support`：fixture render、人工评审、rights 和已知失败齐全；
- `mature`：有真实脱敏使用证据和稳定修复记录。

Prompt Markdown 可人工编辑。完成正文后运行 `template-registry solution add ...` 生成或更新 `solution.json`，再运行 catalog build/validate。

需要让 inspect 告诉用户“填什么”时，为实际占位符生成 companion contract。不得手写 JSON；先初始化，再逐字段维护：

```bash
template-registry solution add --repository . --package image --id product-cover --version 1.0.0 --category image --locale en --title 'Product Cover' --summary 'Generate a product-cover prompt' --prompt-path solutions/image/product-cover/prompts/main.en.md --role main --json
template-registry solution locale describe --repository . --package image --id product-cover --locale zh-CN --title '产品封面' --summary '生成产品封面提示词' --usage '中文说明仅供人工审阅' --json
template-registry contract init --repository . --package image --id product-cover --role main --locale en --license internal --permission preview --permission execute_requires_review --json
template-registry contract input set --repository . --package image --id product-cover --role main --locale en --name product --type string --required --example 'portable coffee cup' --label-zh-CN '产品' --label-en 'Product' --description-zh-CN '需要展示的真实产品' --description-en 'The real product to feature' --json
template-registry contract validate --repository . --package image --id product-cover --role main --locale en --json
```

contract input 必须与正文中的 `{{name}}` 一致。example 只能使用公开、虚构、非敏感内容；敏感字段不能声明 default、example 或 enum。

## 模块化视觉资产 v2 的 authoring 循环

`ai-drama-*-assets-v2` 的每个模板角色都走同一条 CLI 链（preset matrix 见 `docs/modular-visual-assets-v2.md` 模板矩阵；差异只进 contract input，不复制模板 ID）：

1. 手写 `prompts/<role>.en.md`（slot 职责、编译顺序、blocking negatives、稳定失败码），中文审阅译文写入 `docs/template-zh-CN.md`。
2. `solution add` 注册角色——同 solution 追加模板时必须原样重复该 locale 的 title/summary/usage，否则会整块覆盖 locale 文案。
3. `contract init` + 逐个 `contract input set`（enum 只收稳定 machine ID）+ `contract validate`。
4. 共享输出 schema 只落一份 artifact（`document artifact add --kind schema --stdin`，JCS 落盘）；每个角色的 `document init --schema-path` 绑定同一文件，改 schema 用 `document artifact replace --expected-digest` + 全角色 `document schema rebind`，不允许复制漂移。
5. `fixture set init` + `fixture case add --stdin`（envelope 为 `{"input":…,"output":…}`，按 case_id 升序添加）+ `fixture validate`。

fixture 命名规则：valid fixture 输出中禁止出现任何以 `ref` 结尾（归一化后）或 `digest/timestamp/provider` 等键——因此 v2 共享 schema 的回显字段命名为 `subject_version`、lineage 项命名为 `source_version` + `artifact_digest`；invalid 输出不受此限但仍须通过 schema。版本后缀目录（如 `ai-drama-background-assets-v2`）用于并行演进期（Registry 同 id 不允许双版本）；2026-09-05 起 `ai-drama-character-assets-v2` 已晋升为正式 `ai-drama-character-assets@1.0.0`，旧 1.x 目录移除。此后非正式版本的目录名或版本号必须带 `beta`/`alpha` 标识，正式版本用无后缀 id 从 1.0.0 起版。
