<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI 电影多 Profile 生产编译：完整使用教程

将剧作、资产、场景、镜头、声音和连续性编译为可审查语义提案

## 如何提出需求

适用目标：由 Auctra、Scaena、Eikona、Sonora 消费安全投影；不执行 Provider 或接受 canonical state。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI 电影多 Profile 生产编译」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-film-multi-profile-production@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

project-intent 确定制作意图，scene-package 组织场景，asset-dependency 明确资产依赖，shot-audio-intent 描述镜头与声音，shot-prompt 交接具体提示。continuity-review 检查已生成结果，failure-restructure 仅在有实际失败证据时调整。使用 accepted_source_projection 和 active_reference_bindings 传递已接受事实。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `asset-dependency`

职责：Identify the visual assets required by the production plan.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`asset-dependency`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs asset-dependency -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/asset-dependency.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-asset-dependency-semantic-output-v1"] | ai-film-asset-dependency-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | cinematic_live_action |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example asset-dependency -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'asset-dependency' --output 'asset-dependency-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'asset-dependency' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'asset-dependency' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-asset-dramatic-function；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-asset-dependency-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "cinematic_live_action",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"asset-dependency"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks asset-dependency -->
### 结果示例与检查

示例目标：Asset dependencies。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/asset-dependency.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `continuity-review`

职责：Review cross-shot character, environment and narrative continuity.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`continuity-review`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs continuity-review -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/continuity-review.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"facts":[{"id":"f1","text":"两位成年角色在旧车站核对信件地址","source":"synthetic-script-01"}],"scene_id":"station-01"} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"bindings":[{"id":"binding-01","source":"synthetic-script-01","inherit":["人物身份","地点","道具"],"forbid":["未给出的历史事实"]}]} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"locked":["人物身份","左腕布绳","信件状态"],"time":"同一傍晚","space":"同一候车室"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-continuity-review-semantic-output-v1"] | ai-film-continuity-review-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | cinematic_live_action |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"max_revisions":1,"escalate_on":["missing_source","identity_conflict"],"automatic_provider_retry":false} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"scope":["station-01"],"allowed_changes":["对话表达","动作节奏"],"preserve":["旧地址是唯一已知线索"],"decision":"是否先核对地址"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example continuity-review -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'continuity-review' --output 'continuity-review-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'continuity-review' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'continuity-review' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"facts\":[{\"id\":\"f1\",\"text\":\"两位成年角色在旧车站核对信件地址\",\"source\":\"synthetic-script-01\"}],\"scene_id\":\"station-01\"}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"bindings\":[{\"id\":\"binding-01\",\"source\":\"synthetic-script-01\",\"inherit\":[\"人物身份\",\"地点\",\"道具\"],\"forbid\":[\"未给出的历史事实\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"locked\":[\"人物身份\",\"左腕布绳\",\"信件状态\"],\"time\":\"同一傍晚\",\"space\":\"同一候车室\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-continuity-review-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "cinematic_live_action",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"max_revisions\":1,\"escalate_on\":[\"missing_source\",\"identity_conflict\"],\"automatic_provider_retry\":false}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"scope\":[\"station-01\"],\"allowed_changes\":[\"对话表达\",\"动作节奏\"],\"preserve\":[\"旧地址是唯一已知线索\"],\"decision\":\"是否先核对地址\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"continuity-review"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks continuity-review -->
### 结果示例与检查

示例目标：Continuity review。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/continuity-review.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `failure-restructure`

职责：Revise a failed production plan while preserving its accepted intent.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`failure-restructure`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs failure-restructure -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/failure-restructure.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-failure-restructure-semantic-output-v1"] | ai-film-failure-restructure-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | stylized_animation |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example failure-restructure -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'failure-restructure' --output 'failure-restructure-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'failure-restructure' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'failure-restructure' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-red-risk-restructure；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-failure-restructure-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "stylized_animation",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"failure-restructure"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks failure-restructure -->
### 结果示例与检查

示例目标：Failure restructuring。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/failure-restructure.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `project-intent`

职责：Describe the production intent and required output profile.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`project-intent`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs project-intent -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/project-intent.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-project-intent-semantic-output-v1"] | ai-film-project-intent-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | cinematic_live_action |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example project-intent -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'project-intent' --output 'project-intent-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'project-intent' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'project-intent' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-live-action-two-hander；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-project-intent-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "cinematic_live_action",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"project-intent"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks project-intent -->
### 结果示例与检查

示例目标：Project intent。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/project-intent.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `scene-package`

职责：Organize a production-ready scene package and its dependencies.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`scene-package`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs scene-package -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/scene-package.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-scene-package-semantic-output-v1"] | ai-film-scene-package-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | motion_comic |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example scene-package -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'scene-package' --output 'scene-package-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'scene-package' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'scene-package' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-motion-comic-dialogue；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-scene-package-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "motion_comic",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"scene-package"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks scene-package -->
### 结果示例与检查

示例目标：Scene package。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/scene-package.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `shot-audio-intent`

职责：Describe dialogue, voice and sound requirements for a shot.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`shot-audio-intent`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs shot-audio-intent -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/shot-audio-intent.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-shot-audio-intent-semantic-output-v1"] | ai-film-shot-audio-intent-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | brand_film |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example shot-audio-intent -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-audio-intent' --output 'shot-audio-intent-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-audio-intent' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-audio-intent' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-brand-cta；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-shot-audio-intent-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "brand_film",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"shot-audio-intent"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks shot-audio-intent -->
### 结果示例与检查

示例目标：Shot audio intent。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/shot-audio-intent.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `shot-prompt`

职责：Compile a shot-level video generation prompt.

精确引用：`promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en`；role：`shot-prompt`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs shot-prompt -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/shot-prompt.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_projection_json` | string／必填 | Owner筛选后的有界事实JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"rights":"internal","readiness":"candidate","facts":["fixture only safe fact"]} |
| `active_reference_bindings_json` | string／必填 | 带inherit和forbid的安全绑定JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"identity_source":{"ref":"fixture://identity-source-001","digest":"sha256:0000000000000000000000000000000000000000000000000000000000000000","inherit":["face_geometry"],"forbid":["wardrobe"]}} |
| `continuity_constraints_json` | string／必填 | Owner筛选的连续性规则JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"screen_direction":"locked","evidence_policy":"unknown_when_absent"} |
| `output_schema_version` | enum／必填 | 已绑定角色语义输出版本；由用户选择并确认 | enum=["ai-film-shot-prompt-semantic-output-v1"] | ai-film-shot-prompt-semantic-output-v1 |
| `profile_id` | enum／必填 | 固定生产Profile；由用户选择并确认 | enum=["cinematic_live_action", "motion_comic", "stylized_animation", "brand_film"] | stylized_animation |
| `retry_policy_json` | string／必填 | 有界修复和升级策略JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"single_variable_only":true,"threshold":10,"escalate_to":"owner_review"} |
| `task_delta_json` | string／必填 | 仅本次允许变化的有界JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"change_scope":["scene_coverage"],"requested_output":"semantic_proposal"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example shot-prompt -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-prompt' --output 'shot-prompt-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-prompt' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en' --role 'shot-prompt' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-stylized-action；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_projection_json": {
      "value": "{\"rights\":\"internal\",\"readiness\":\"candidate\",\"facts\":[\"fixture only safe fact\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.active_reference_bindings_json": {
      "value": "{\"identity_source\":{\"ref\":\"fixture://identity-source-001\",\"digest\":\"sha256:0000000000000000000000000000000000000000000000000000000000000000\",\"inherit\":[\"face_geometry\"],\"forbid\":[\"wardrobe\"]}}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_constraints_json": {
      "value": "{\"screen_direction\":\"locked\",\"evidence_policy\":\"unknown_when_absent\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "ai-film-shot-prompt-semantic-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "stylized_animation",
      "kind": "user",
      "source": "user"
    },
    "main.retry_policy_json": {
      "value": "{\"single_variable_only\":true,\"threshold\":10,\"escalate_to\":\"owner_review\"}",
      "kind": "user",
      "source": "user"
    },
    "main.task_delta_json": {
      "value": "{\"change_scope\":[\"scene_coverage\"],\"requested_output\":\"semantic_proposal\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_projection_json,main.active_reference_bindings_json,main.continuity_constraints_json,main.output_schema_version,main.profile_id,main.retry_policy_json,main.task_delta_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-film-multi-profile-production@1.0.0?locale=en","role":"shot-prompt"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks shot-prompt -->
### 结果示例与检查

示例目标：Shot prompt。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/shot-prompt.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

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
