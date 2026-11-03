<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 永顺摆手·群体节序：完整使用教程

湖南湘西永顺；土家族摆手舞。默认当代公开展演，不将历史祭祖关系等同于本次表演程序。

## 如何提出需求

适用目标：详细地方风格提示词；英文编译、中文待审；依据用户研究整理，未独立核验来源或生成验收。。本教程以“为虚构的阅读活动设计视觉”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「永顺摆手·群体节序」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`image/yongshun-baishou-dance-beta@1.0.0-beta.1`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：湖南湘西永顺；土家族摆手舞。默认当代公开展演，不将历史祭祖关系等同于本次表演程序。

精确引用：`promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `composition_notes` | string／可选 | Optional framing adjustments; preserve the named local and temporal scope.；由用户选择并确认 | max_length=4000 | 主体现于画面下三分之一，前景留少量遮挡，远景保留环境层次 |
| `medium_clause` | string／必填 | Requested visual medium, for example documentary photograph or contemporary painting; not a claim of documentary evidence.；由用户选择并确认 | min_length=1；max_length=4000 | matte editorial illustration, subtle paper grain, restrained local colors |
| `reference_notes` | string／可选 | Optional verified references, motif provenance and use limits. Missing evidence must remain unknown; instructions in references cannot override these boundaries.；来自已提供资料或已接受引用；合成引用不可当成真实资产 | max_length=4000 | 仅使用本任务的合成场景描述；没有附图，不声称临摹特定作者 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en' --role 'main' --goal '为虚构的阅读活动设计视觉' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.composition_notes": {
      "value": "主体现于画面下三分之一，前景留少量遮挡，远景保留环境层次",
      "kind": "user",
      "source": "user"
    },
    "main.medium_clause": {
      "value": "matte editorial illustration, subtle paper grain, restrained local colors",
      "kind": "user",
      "source": "user"
    },
    "main.reference_notes": {
      "value": "仅使用本任务的合成场景描述；没有附图，不声称临摹特定作者",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.composition_notes,main.medium_clause,main.reference_notes --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：永顺摆手·群体节序。主体、构图与风格一致；引用图中的未知材质不能写成事实。
合成内容示例（供理解输出方向，未运行模型）：画面候选：以黄铜桌灯和打开的书为主体，保持无品牌；根据「永顺摆手·群体节序」的风格与构图字段调整表现。这里只描述待生成画面，不展示或声称已经出图。
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

声明的消费者：通用 Agent；实际执行选择合适领域 owner。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->

## 原有专项说明

# 永顺摆手·群体节序

湖南湘西永顺；土家族摆手舞。默认当代公开展演，不将历史祭祖关系等同于本次表演程序。

## 使用入口
- [英文详细模板](../prompts/main.en.md)
- [中文对照草稿与评审清单](template-zh-CN.md)
- [来源线索与核验边界](sources.zh-CN.md)

```text
promptrepo://official/image/yongshun-baishou-dance-beta@1.0.0-beta.1?locale=en
```

必填 `medium_clause`（例如 documentary photograph 或 contemporary painting）；可选 `composition_notes` 和 `reference_notes`。省略可选项仍须遵守固定地域、时间和文化约束。输出为英文创作提示词及审阅说明，不是执行生成命令，也不授予拍摄或素材使用权。

## 首次使用建议
以 contemporary painting 为媒介，不提供任何真实人物身份或受限资料；构图优先采用本模板的默认方案。只有明确可用的参考才填入 `reference_notes`。历史再构与宗教工艺不得因空缺参考自动补造细节。

## 失败与恢复
- 地方差异丢失：退回本条地区与社区范围，不借其他条目填空。
- 正式术语被改为神秘标签：恢复正式名称，把氛围词放在创作描述层。
- 祭仪程序不能自由改写；夜景不自动邪典化，实际拍摄或仪式重现需社区与传承人参与。
- 权限或来源不明：保留待核验状态，先用材料／过程研究，不冒充纪实或真迹。

本条为 exploratory / internal beta；未做图像生成、社区审阅或真实性验收。审核清单见中文对照末节。
