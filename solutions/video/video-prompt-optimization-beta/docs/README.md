<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 视频提示词编译（模型无关）：完整使用教程

把粗略分镜或故事概要编译成一条扩散类音视频联合生成模型可直接提交的提示词正文：正向排除、声音与器物纪律、时长与逐句语速核算，平台差异经输入变量声明

## 如何提出需求

适用目标：由 Scaena 等 Agent 消费方编译使用；提交参数、生成执行与验收归生成层与验证层。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「视频提示词编译（模型无关）」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/video-prompt-optimization-beta@1.0.0-beta.1`；成熟度：`exploratory`；rights：`unknown`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：把粗略分镜或故事概要编译成一条扩散类音视频联合生成模型可直接提交的提示词正文：正向排除、声音与器物纪律、时长与逐句语速核算，平台差异经输入变量声明

精确引用：`promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en`；role：`main`。
合同许可：`internal`；permissions：`preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `dialogue_script` | string／可选 | 用户台词逐字稿；留空表示全片无台词；由用户选择并确认 | 合同未附加范围限制 | 林舟：“这封信还没有寄出去。”顾遥：“先看看地址是否仍然存在。” |
| `duration_budget` | string／可选 | 目标时长或约束；含目标模型单次生成上限则一并给出（常见 5–30s）；由用户选择并确认 | 合同未附加范围限制 | 30 seconds |
| `extra_constraints` | string／可选 | 编译正文必须遵守的用户额外约束；由用户选择并确认 | 合同未附加范围限制 | 不使用真实品牌、未授权音乐或未经确认的资产；缺项标为待补 |
| `generation_mode` | enum／必填 | 提交素材形态，决定正文信息加减法策略；由用户选择并确认 | enum=["t2v", "first_frame", "first_last_frame", "reference_image", "reference_video", "edit_extend"]；default=t2v | t2v |
| `media_reference_syntax` | string／可选 | 目标平台正文内指代素材的原生语法，如 @图片1（名称）、@image1 或 UUID；留空改用位置描述；来自已提供资料或已接受引用；合成引用不可当成真实资产 | 合同未附加范围限制 | @image1 指代用户提供且已核对的首帧；示例引用为合成标识 |
| `output_language` | enum／可选 | 提交正文语言；由用户选择并确认 | enum=["zh", "en"]；default=zh | zh |
| `reference_manifest` | string／可选 | 上传顺序、名称与类型：角色视觉先验/场景/帧锚点；来自已提供资料或已接受引用；合成引用不可当成真实资产 | 合同未附加范围限制 | @image1: 合成首帧；@image2: 合成服装参考；真实使用必须先导入对应素材 |
| `source_brief` | string／必填 | 粗略分镜或故事概要原文；来自已提供资料或已接受引用；合成引用不可当成真实资产 | min_length=4 | 30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 |
| `style_requirements` | string／可选 | 用户指定的画质/风格/基调要求；由用户选择并确认 | 合同未附加范围限制 | 自然光、克制色彩、清晰动作；同一人物和场景保持连续性 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.dialogue_script": {
      "value": "林舟：“这封信还没有寄出去。”顾遥：“先看看地址是否仍然存在。”",
      "kind": "user",
      "source": "user"
    },
    "main.duration_budget": {
      "value": "30 seconds",
      "kind": "user",
      "source": "user"
    },
    "main.extra_constraints": {
      "value": "不使用真实品牌、未授权音乐或未经确认的资产；缺项标为待补",
      "kind": "user",
      "source": "user"
    },
    "main.generation_mode": {
      "value": "t2v",
      "kind": "user",
      "source": "user"
    },
    "main.media_reference_syntax": {
      "value": "@image1 指代用户提供且已核对的首帧；示例引用为合成标识",
      "kind": "user",
      "source": "user"
    },
    "main.output_language": {
      "value": "zh",
      "kind": "user",
      "source": "user"
    },
    "main.reference_manifest": {
      "value": "@image1: 合成首帧；@image2: 合成服装参考；真实使用必须先导入对应素材",
      "kind": "user",
      "source": "user"
    },
    "main.source_brief": {
      "value": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。",
      "kind": "user",
      "source": "user"
    },
    "main.style_requirements": {
      "value": "自然光、克制色彩、清晰动作；同一人物和场景保持连续性",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.dialogue_script,main.duration_budget,main.extra_constraints,main.generation_mode,main.media_reference_syntax,main.output_language,main.reference_manifest,main.source_brief,main.style_requirements --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：视频提示词编译（模型无关）。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
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

# video-prompt-optimization-beta

模型无关的视频提示词编译模板：把粗略分镜/故事概要编译成一条可直接提交的专业提示词正文，适用于扩散类音视频联合生成模型。固化的方法论来自 Scaena 生产链路：正向排除（否定卡）、静默镜声源纪律（声音卡）、器物与反射规则（器物卡）、参考素材指代协议（按目标平台声明）、设定档案先行、时长与逐句语速核算、180° 轴线与六层镜头结构、出片前自检。参考素材指代语法、时长上限、素材互斥等平台差异全部通过变量声明，不固化任何单家模型协议。

- 编译模板（Agent/模型消费）：`../prompts/main.en.md`
- 中文阅读版（人工审阅，不进编译）：`template-zh-CN.md`
- 使用指南：`usage.zh-CN.md`
- 评审清单：`review-checklist.zh-CN.md`
- 已知失败模式：`failure-modes.zh-CN.md`
- 绑定实例：`../examples/bank-card-relay.zh-CN.md`

Exact ref：

```text
promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en
```

家族边界：变量值齐全的蓄力大招渲染走 `ai-drama-shot-video-generation`；运镜/布光技术选型走 `cinematique-shot-techniques-beta`。提交参数确认、生成执行与出片验收归 Scaena 生成/验证层，不在本模板。
