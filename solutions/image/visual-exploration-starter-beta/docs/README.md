<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 三方向视觉探索入门包：完整使用教程

让 Agent 帮你比较视觉方向并在新任务中复用

## 如何提出需求

适用目标：免费 beta；英文编译，中文指南，出图另行确认。本教程以“为虚构的阅读活动设计视觉”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「三方向视觉探索入门包」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`image/visual-exploration-starter-beta@1.0.0-beta.1`；成熟度：`exploratory`；rights：`free-evaluation`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Explore, compare and reuse three visual directions with an Agent

精确引用：`promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en`；role：`main`。
合同许可：`LicenseRef-Yeisme-Free-Evaluation`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | string／必填 | 比例；由用户选择并确认 | regex=^(1:1\|4:5\|3:4\|16:9\|9:16)$；min_length=1；max_length=2000 | 16:9 |
| `audience` | string／必填 | 受众；由用户选择并确认 | min_length=1；max_length=2000 | 初次了解该项目的读者 |
| `brief` | string／必填 | 需求；由用户选择并确认 | min_length=1；max_length=8000 | 虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。 |
| `constraints` | string／必填 | 硬约束；由用户选择并确认 | min_length=1；max_length=2000 | 只使用给定资料；未知内容明确标注 |
| `output_language` | string／必填 | 说明语言；由用户选择并确认 | min_length=1；max_length=2000 | zh-CN |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en' --role 'main' --goal '为虚构的阅读活动设计视觉' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.aspect_ratio": {
      "value": "16:9",
      "kind": "user",
      "source": "user"
    },
    "main.audience": {
      "value": "初次了解该项目的读者",
      "kind": "user",
      "source": "user"
    },
    "main.brief": {
      "value": "虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。",
      "kind": "user",
      "source": "user"
    },
    "main.constraints": {
      "value": "只使用给定资料；未知内容明确标注",
      "kind": "user",
      "source": "user"
    },
    "main.output_language": {
      "value": "zh-CN",
      "kind": "user",
      "source": "user"
    }
  }
}
INPUT
)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
template-registry prompt session describe "$session_id" --json
printf 'Confirm the tutorial inputs above? Type yes: '
read -r answer
test "$answer" = yes || exit 1
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.aspect_ratio,main.audience,main.brief,main.constraints,main.output_language --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/image/visual-exploration-starter-beta@1.0.0-beta.1?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Visual exploration starter。主体、构图与风格一致；引用图中的未知材质不能写成事实。
合成内容示例（供理解输出方向，未运行模型）：画面候选：以黄铜桌灯和打开的书为主体，保持无品牌；根据「三方向视觉探索入门包」的风格与构图字段调整表现。这里只描述待生成画面，不展示或声称已经出图。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
<!-- guide:begin recovery global -->
## 失败恢复、复用与交接

- `needs_input`：按缺失字段补值；`needs_analysis`：显式处理资料分析，不能仅凭导入就宣布读懂图片。
- `needs_confirmation`：读取待确认内容，收到答复后确认；`needs_step_output`：等待前序真实结果并导入。
- `REVISION_CONFLICT`：重新读取原 session，再合并改动；不要新建替代会话隐藏冲突。
- `GUIDE_NOT_FOUND`：当前快照缺教程；`GUIDE_STALE`：重新发现指南并核对版本；不自动切换模板版本。
- 导出结果未知时核对原产物和回执，不盲目覆盖或重导出。单条 prompt 导出不是 bundle，不使用 bundle verify 校验单文件。

```bash
template-registry prompt session list --sort activity --json
template-registry prompt commands --operation session.update --operation session.confirm --json
```

从列表选择原 session，使用 session describe/read 核对后更新输入；未变化的确认保持有效，变化的字段重新确认。跨项目导入包创建新会话，接收方重新确认。

声明的消费者：eikona。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->

## 原有专项说明

# 三方向视觉探索入门包 · beta

适合已经使用 Agent、但还没有确定画面方向的中文创作者。给出需求、受众、硬约束和比例，获得三套可比较的方向说明与独立英文出图提示词。

这个免费包能完成一次完整探索。它不生成图片，不保证不同模型的效果，也不替你确认最终方向。当前为 `exploratory`：编译与复用演练可本地验证，真实出图和用户试用待完成。

## 第一次使用

从仓库根目录打开 [可运行演练](../../../../docs/visual-exploration/quickstart.md)。英文模板负责 Agent 编译，中文输入和说明受支持。

## 给 Agent 的阅读顺序

请把本目录和这些链接交给 Agent，让它先读取工具能力，再按输入合同提问。网页或文档不会替你执行模型调用。

1. [方案清单 `solution.json`](../solution.json)：确认 package、solution、版本和公开角色。
2. [输入合同 `main.en.json`](../contracts/main.en.json)：确认必填字段、类型、默认值和边界。
3. [英文 Agent 模板 `main.en.md`](../prompts/main.en.md)：编译后输出三个方向和独立提示词。
4. [中文阅读指南 `template-zh-CN.md`](template-zh-CN.md)：了解输入、评审和复用方法。
5. [练习示例 `examples.md`](examples.md)：检查方向差异和事实清理。
6. [使用许可 `LICENSE.md`](LICENSE.md)：确认执行、修改和商用边界。

固定版本入口可用于复现本次行为；`main` 可能继续更新，获取新版前请重新核对版本和合同。仓库级流程见 [visual-exploration quickstart](../../../../docs/visual-exploration/quickstart.md) 和 [仓库文档目录](../../../../docs/README.md)。

你需要提供：需求、目标受众、必须保留/避免的内容、画面比例、说明语言。检查 Agent 是否保留真实主体、是否给出三种不同构图与表现方式、是否明确说明取舍。确认方向后再决定是否授权图像工具执行。

## 三个公开练习

- 产品宣传：无品牌米白色陶瓷杯，不添加性能、价格或认证信息。
- 活动视觉：虚构的周末植物交换会，不编造真实地点、主办方或票价。
- 内容封面：面向初学者的“整理工作台”文章，不添加作者或阅读量。

每个练习均换一个主体再运行一次；第二次不能继承第一次的品牌、活动或事实约束。完整练习见[练习示例](examples.md)。

## 使用边界

免费评估权限见[使用许可](LICENSE.md)，不改变仓库里其他模板的权限。拟支持环境为 Eikona + `openai/gpt-5.4-image-2`，尚无真实图像验证；其他环境仅提供通用导出。模型调用费用不包含在模板中。

本页提供免费 beta 的使用说明，付费方案尚未开放销售。

## 复制给 Agent 的任务起点

请读取本页、`solution.json`、`contracts/main.en.json` 和 `prompts/main.en.md`，先向我询问需求、受众、硬约束、比例和说明语言。确认输入后再编译，输出三个方向和各自取舍，等待我选择；图片生成、精修、费用和模型调用是后续独立步骤。更换主体时建立新会话，重新确认输入并检查旧事实没有残留。
