# Yeisme Prompt Templates 仓库指令

本仓库是 Yeisme 官方中文优先 Prompt 解决方案内容源。它拥有经过评审的 Prompt 正文、示例、分类、tags、i18n 适配和内容成熟度，不拥有模型执行、用户仓库状态、Provider credential 或领域资产生命周期。

Active skills 由根目录 `.skills/profiles/targets/data/yeisme-prompt-templates.txt` 声明，并同步到本仓库 `.agents/skills/` 与 `.claude/skills/`。

<!-- runtime-skills:start -->
- `yeisme-prompt-repository-router`
- `natural-writing-editor`
- `yeisme-evolutionary-change-policy`
- `ai-native-cli-output-contract`
- `review`
<!-- runtime-skills:end -->

## 内容与语言

- Locale 政策见 `docs/locale-policy.md`：solution 默认单语言，locale 可为任意 BCP 47 语言；`zh-CN` 是仓库 `default_locale` 与文档默认语言，不再强制 zh-CN 源 + en 适配配对。
- Agent 编译约定（2026-09-05 起，image 包先行，scaena 项目统一遵循）：进入编译器/投递给模型的模板正文一律为 `main.en.md`；`main.zh-CN.md` 只作人工审阅译文，不进入编译。包内中文译文须在头部标注该身份。
- Prompt、指南和示例可以人工编辑；`repository.json`、`solution.json`、`catalog.json`、release manifest 和 lock 必须由 Template Registry CLI 生成（含 `solution locale remove` 的 locale 移除）。
- machine IDs、目录名、schema keys、tags、capabilities、rights 和 maturity 使用稳定英文。
- 版本命名（2026-09-05 起）：正式版本用无后缀 solution id，从 `1.0.0` 起版；非正式（未转正）版本的目录名或版本号必须带 `beta` 或 `alpha` 标识（如 `xxx-assets-beta`、`2.0.0-beta.1`）。转正时去后缀目录、版本重置 `1.0.0`，内容整体晋升并经 Registry CLI 重放 metadata；禁止再用裸 `-v2` 目录表达"并行未转正 major"（`ai-drama-background-assets-v2` 为存量豁免，转正时一并收敛）。
- 不记录隐藏系统提示、真实用户数据、Provider payload、credential、完整思维链或未脱敏运行证据。

## 边界

- 不在本仓库实现 Git/GitHub/S3 adapter、搜索引擎或模型调用。
- 不复制 Sonora、Eikona、Scaena、Pinax 或 Auctra 的领域状态。
- 官方条目必须是解决方案包，而不是只有一段 Prompt 字符串；至少包含适用目标、输入变量、输出要求、评审清单、失败模式、rights 与 maturity。
- 任何第二 locale 的自动翻译只能作为 draft，进入 reviewed 前需要人工校对；不为「完整性」补 locale（见 `docs/locale-policy.md`）。

## Skill 路由

- 内容正文、分类、locale、rights 与 maturity 变更先使用 `yeisme-prompt-repository-router` 确认本仓库是否为 canonical owner。
- 中文正文、英文适配和终稿自然度使用 `natural-writing-editor`，但不得改变稳定 ID、变量、schema、rights 或 maturity 语义。
- `promptrepo://` ref、template address、inspect/render/preview DTO 属于 `shared/promptrepo`；Registry service、CAS、Git mirror、安装和审计状态属于 `backend-server/template-registry`。
- 稳定字段、digest、URI、错误码或兼容性变化使用 `yeisme-evolutionary-change-policy`；结构化输出和正文泄露边界使用 `ai-native-cli-output-contract`。

## 维护命令

从 Yeisme 根仓库使用当前 `backend-server/template-registry` 源码运行维护工具，不依赖用户环境里可能缺失或过期的全局二进制：

```bash
(cd backend-server/template-registry && go run ./cmd/template-registry catalog build --repository ../../data/yeisme-prompt-templates --json)
(cd backend-server/template-registry && go run ./cmd/template-registry catalog validate --repository ../../data/yeisme-prompt-templates --json)
openspec validate --all --strict
```

## 完成标准

- Catalog build/validate 通过且结果确定。
- 中文正文完整；英文状态与中文 source digest 可追踪。
- 所有结构化 metadata 均由维护命令生成。
- Git diff 不包含 secret、cache、数据库、运行目录或测试 evidence。

配置或更新 skills 后，从根目录运行：

```bash
scripts/skills.sh sync-target data/yeisme-prompt-templates
scripts/skills.sh validate-subprojects-runtime
```
