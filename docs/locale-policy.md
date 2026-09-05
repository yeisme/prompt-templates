# Locale 政策：单语言模板与任意语言设计

## 原则

- 一个 solution 至少有一个 locale，**单语言是一等公民**：solution 可以且默认只维护一个 locale。
- locale 的选择是按 solution 的设计决策，可以是任意 BCP 47 语言（`zh-CN`、`en`、`ja`、`ko` 等）。仓库 `default_locale` 只决定 catalog 默认值与新 solution 的惯用起点，不强制任何 solution 双语。
- 不再要求「zh-CN 源 + en 首个同步适配」的固定配对。任何第二 locale 只有在确有该语言的投递或消费需求、且有人维护等价性时才添加；未经过人工校对的第二 locale 一律按 draft 管理。

## 三层语言必须分开判断

1. **模板骨架语言**：由 locale 决定，即 `prompts/<role>.<locale>.md` 的叙述语言。
2. **变量内容语言**：由消费方填入的值决定，可以与骨架语言不同（英文骨架 + 中文场景描述是合法渲染）。
3. **台词/VO 语言**：由 `dialogue_language`、`voiceover_script` 等输入独立声明，与骨架 locale 无关（英文模板 + 日语台词是标准用法）。

评审「某 locale 模板是否纯净」时只看骨架；渲染结果的语言构成是变量绑定问题，不是模板缺陷。

## 何时单语言、何时多 locale

- 默认单语言：内部内容、只有一个投递方向的模板。
- 加第二 locale 的充分条件：存在该语言的真实消费方（如英文投递的视频模型），且有人承担等价校对。
- 不为「完整性」补 locale；空挂的 draft locale 会被误认为可用版本。

## 移除 locale 的流程（演进式变更）

移除 locale 属于 `yeisme-evolutionary-change-policy` 管理的兼容变更，消费方可能已绑定该 locale：

1. 确认没有活跃消费方依赖该 locale（检索 refs 与消费记录）。
2. 元数据移除（不手写 JSON）：

   ```bash
   (cd backend-server/template-registry && go run ./cmd/template-registry solution locale remove --repository ../../data/yeisme-prompt-templates --package <package> --id <solution> --locale <locale> --json)
   ```

   该命令只改 `solution.json`（移除 locale 文案与模板绑定），并拒绝移除 solution 的最后一个 locale 或最后一个模板。
3. 命令输出 `orphan_paths`：对应的 `prompts/`、`contracts/`（含 `contracts/documents/`）文件由调用方显式删除；fixture 若绑定该 locale 一并处理。
4. 运行 `catalog build` + `catalog validate` 确认。
5. 在 solution 的 usage 文档中记录当前 locale 决策与移除原因。

## 人类可读文档的语言

docs、examples、评审清单等人类可读文档默认 zh-CN（仓库文档语言政策），与模板 locale 决策相互独立：英文单语言模板同样可以只有中文使用文档。

## 视频生成家族的统一约定（2026-09-05 起）

视频生成类 solution（`solutions/video/` 下直接投递视频模型的生成型模板）统一执行「**en 模板 + zh 阅读版**」双层结构：

- `prompts/<role>.en.md` 是唯一注册模板：英文骨架面向 agent 与视频模型消费，注册进 solution.json 与 catalog，contract 也只维护 en locale。
- `docs/template-zh-CN.md` 是中文阅读版：与英文模板逐节对应、变量名一致，仅供人工审阅，**不注册 locale、不进 catalog、不被 render**。
- 变量内容语言与台词语言仍按「三层语言」规则独立，不受 en 骨架约束。

新视频生成 solution 默认按此结构创建；历史双语 solution 迁移时用 `solution locale remove` 收编到单 en locale，中文模板正文移动为 `docs/template-zh-CN.md`。
