<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 产品宣传片 Brief 与镜头设计：完整使用教程

根据产品事实生成 Brief，并用固定镜头库生成可追溯镜头计划

## 如何提出需求

适用目标：中文正文只供人工审阅；Agent 编译使用英文 role。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「产品宣传片 Brief 与镜头设计」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/product-promo-shot-design-beta@1.0.0-beta.1`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

brief → 用户接受实际 Brief → shot-plan。shot-plan 使用固定镜头库版本及已接受 Brief；不要把第一步提示词当成 Brief 结果。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `brief`

职责：Create a source-grounded product promo brief and exact shot-library plan

精确引用：`promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en`；role：`brief`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs brief -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/brief.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `audience_and_outcome` | string／必填 | 已确认的受众、观看情境和业务或传播结果；由用户选择并确认 | min_length=1；max_length=8192 | Product teams evaluating a local project workspace; explain the core workflow. |
| `brand_constraints_json` | string／必填 | 品牌 token、视觉规则和允许偏离项 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"tone":["precise","calm","tactile"]} |
| `creative_mode` | enum／必填 | 产品宣传片规划的已确认协作模式；由用户选择并确认 | enum=["template_adaptation", "agent_directed", "guided_collaboration"] | guided_collaboration |
| `data_handling_policy` | enum／必填 | 采集或生成资产中可见产品数据的确认规则；由用户选择并确认 | enum=["public_demo_only", "synthetic_or_redacted", "mixed_with_review"] | synthetic_or_redacted |
| `delivery_requirements_json` | string／必填 | 时长、画幅、语言、音频、字幕、变体和可编辑性 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"duration_seconds":30,"aspect_ratio":"16:9","frame_rate":30,"language":"zh-CN","captions":true,"audio":"sfx_only","editable_timeline":true} |
| `output_language` | enum／必填 | 语义 Brief 的输出语言；由用户选择并确认 | enum=["en", "zh-CN"] | zh-CN |
| `product_facts_json` | string／必填 | 带来源的产品事实 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=524288 | {"facts":[{"fact":"Atlas Desk organizes project notes and tasks in one local workspace.","source_id":"product-readme"}]} |
| `rights_constraints_json` | string／必填 | 资产、音乐、字体、代码、署名和可搬运约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"upstream_code":"Apache-2.0","remotion_license":"review_required","audio":"verified_files_only"} |
| `source_inventory_json` | string／必填 | 导入来源的 ID、位置、digest 与可搬运信息 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=524288 | {"sources":[{"source_id":"product-readme","portable":true}]} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example brief -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'brief' --output 'brief-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'brief' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'brief' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 video-shotcraft-guided；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.audience_and_outcome": {
      "value": "Product teams evaluating a local project workspace; explain the core workflow.",
      "kind": "user",
      "source": "user"
    },
    "main.brand_constraints_json": {
      "value": "{\"tone\":[\"precise\",\"calm\",\"tactile\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.creative_mode": {
      "value": "guided_collaboration",
      "kind": "user",
      "source": "user"
    },
    "main.data_handling_policy": {
      "value": "synthetic_or_redacted",
      "kind": "user",
      "source": "user"
    },
    "main.delivery_requirements_json": {
      "value": "{\"duration_seconds\":30,\"aspect_ratio\":\"16:9\",\"frame_rate\":30,\"language\":\"zh-CN\",\"captions\":true,\"audio\":\"sfx_only\",\"editable_timeline\":true}",
      "kind": "user",
      "source": "user"
    },
    "main.output_language": {
      "value": "zh-CN",
      "kind": "user",
      "source": "user"
    },
    "main.product_facts_json": {
      "value": "{\"facts\":[{\"fact\":\"Atlas Desk organizes project notes and tasks in one local workspace.\",\"source_id\":\"product-readme\"}]}",
      "kind": "user",
      "source": "user"
    },
    "main.rights_constraints_json": {
      "value": "{\"upstream_code\":\"Apache-2.0\",\"remotion_license\":\"review_required\",\"audio\":\"verified_files_only\"}",
      "kind": "user",
      "source": "user"
    },
    "main.source_inventory_json": {
      "value": "{\"sources\":[{\"source_id\":\"product-readme\",\"portable\":true}]}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.audience_and_outcome,main.brand_constraints_json,main.creative_mode,main.data_handling_policy,main.delivery_requirements_json,main.output_language,main.product_facts_json,main.rights_constraints_json,main.source_inventory_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en","role":"brief"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks brief -->
### 结果示例与检查

示例目标：Brief。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
输出结构示例见 [video-shotcraft-guided.output](../fixtures/brief.en/video-shotcraft-guided.output.json)。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/brief.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `shot-plan`

职责：Create a source-grounded product promo brief and exact shot-library plan

精确引用：`promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en`；role：`shot-plan`。
合同许可：`internal`；permissions：`execute_requires_review, preview, step_output_binding`。

<!-- guide:begin inputs shot-plan -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/shot-plan.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_brief_json` | string／必填 | 经用户接受的 product_promo_brief.v1 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=524288 | {"schema_version":"product_promo_brief.v1","product_facts":[{"fact":"Atlas Desk organizes project notes and tasks in one local workspace.","source_id":"product-readme"}],"unknowns":[],"audience":"Product teams evaluating a local project workspace","intended_outcome":"Explain the board-search-review workflow","creative_mode":"guided_collaboration","feature_priorities":[{"feature_or_message":"Project board","priority":1,"evidence_source_ids":["product-readme"],"reason":"Primary workspace"}],"brand_motion_lens":{"tone":["precise","calm","tactile"]},"data_and_rights":{"data":"synthetic_or_redacted","audio":"verified_files_only","remotion_license":"review_required"},"delivery":{"duration_seconds":30,"aspect_ratio":"16:9","frame_rate":30,"language":"zh-CN","captions":true,"audio":"sfx_only","editable_timeline":true},"confirmed_decisions":["guided collaboration","synthetic demo data","30 seconds","16:9","Chinese captions"],"creative_proposals":[],"unresolved_decisions":[]} |
| `downstream_owner` | string／必填 | 消费镜头计划的稳定 Owner 或执行 profile；由用户选择并确认 | regex=^[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=1；max_length=256 | external:video-shotcraft |
| `execution_constraints_json` | string／必填 | 已安装能力、环境限制、数据规则和评审门禁 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"runtime":"Node 22","renderer":"Remotion","deterministic":true,"independent_subagent_authorized":false,"review_gate":"human_review_before_render"} |
| `output_language` | enum／必填 | 语义镜头计划的输出语言；由用户选择并确认 | enum=["en", "zh-CN"] | zh-CN |
| `selected_shot_cards_json` | string／必填 | 用户指定的卡名与 style key，未指定时为空 JSON 列表；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | [{"name":"spotlight-hero-card","style_key":"spotlight-hero-card"}] |
| `shot_library_index_json` | string／必填 | 固定镜头卡名称、样式、来源路径、实现路径和预览状态 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=2097152 | {"repository":"https://github.com/Vincentwei1021/video-shotcraft","revision":"5f047c7cfe10d6616fe59160a750fcfaea510b2e","cards":[{"name":"spotlight-hero-card","styles":[{"key":"spotlight-hero-card","preview_status":"available"}],"source":"references/shots/opening/spotlight-hero-card.md","implementation_path":"demos/opening/spotlight-hero-card/SpotlightHeroCard.tsx"}]} |
| `shot_library_revision` | string／必填 | 精确 Git 提交、release tag 或不可变库修订；由用户选择并确认 | regex=^[A-Za-z0-9][A-Za-z0-9._/-]{6,255}$；min_length=7；max_length=256 | 5f047c7cfe10d6616fe59160a750fcfaea510b2e |
| `source_asset_map_json` | string／必填 | 可用产品状态、截图、页面、媒体和 rights 信息 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=524288 | {"assets":[{"asset_id":"board-view","state":"synthetic project board","portable":true}]} |
| `timing_and_audio_constraints_json` | string／必填 | 时长、帧率、节拍、旁白、字幕和声音约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"duration_seconds":30,"frame_rate":30,"brand_hold_frames":30,"audio":"licensed_sfx_only"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example shot-plan -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'shot-plan' --output 'shot-plan-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'shot-plan' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en' --role 'shot-plan' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 video-shotcraft-guided；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_brief_json": {
      "value": "{\"schema_version\":\"product_promo_brief.v1\",\"product_facts\":[{\"fact\":\"Atlas Desk organizes project notes and tasks in one local workspace.\",\"source_id\":\"product-readme\"}],\"unknowns\":[],\"audience\":\"Product teams evaluating a local project workspace\",\"intended_outcome\":\"Explain the board-search-review workflow\",\"creative_mode\":\"guided_collaboration\",\"feature_priorities\":[{\"feature_or_message\":\"Project board\",\"priority\":1,\"evidence_source_ids\":[\"product-readme\"],\"reason\":\"Primary workspace\"}],\"brand_motion_lens\":{\"tone\":[\"precise\",\"calm\",\"tactile\"]},\"data_and_rights\":{\"data\":\"synthetic_or_redacted\",\"audio\":\"verified_files_only\",\"remotion_license\":\"review_required\"},\"delivery\":{\"duration_seconds\":30,\"aspect_ratio\":\"16:9\",\"frame_rate\":30,\"language\":\"zh-CN\",\"captions\":true,\"audio\":\"sfx_only\",\"editable_timeline\":true},\"confirmed_decisions\":[\"guided collaboration\",\"synthetic demo data\",\"30 seconds\",\"16:9\",\"Chinese captions\"],\"creative_proposals\":[],\"unresolved_decisions\":[]}",
      "kind": "user",
      "source": "user"
    },
    "main.downstream_owner": {
      "value": "external:video-shotcraft",
      "kind": "user",
      "source": "user"
    },
    "main.execution_constraints_json": {
      "value": "{\"runtime\":\"Node 22\",\"renderer\":\"Remotion\",\"deterministic\":true,\"independent_subagent_authorized\":false,\"review_gate\":\"human_review_before_render\"}",
      "kind": "user",
      "source": "user"
    },
    "main.output_language": {
      "value": "zh-CN",
      "kind": "user",
      "source": "user"
    },
    "main.selected_shot_cards_json": {
      "value": "[{\"name\":\"spotlight-hero-card\",\"style_key\":\"spotlight-hero-card\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.shot_library_index_json": {
      "value": "{\"repository\":\"https://github.com/Vincentwei1021/video-shotcraft\",\"revision\":\"5f047c7cfe10d6616fe59160a750fcfaea510b2e\",\"cards\":[{\"name\":\"spotlight-hero-card\",\"styles\":[{\"key\":\"spotlight-hero-card\",\"preview_status\":\"available\"}],\"source\":\"references/shots/opening/spotlight-hero-card.md\",\"implementation_path\":\"demos/opening/spotlight-hero-card/SpotlightHeroCard.tsx\"}]}",
      "kind": "user",
      "source": "user"
    },
    "main.shot_library_revision": {
      "value": "5f047c7cfe10d6616fe59160a750fcfaea510b2e",
      "kind": "user",
      "source": "user"
    },
    "main.source_asset_map_json": {
      "value": "{\"assets\":[{\"asset_id\":\"board-view\",\"state\":\"synthetic project board\",\"portable\":true}]}",
      "kind": "user",
      "source": "user"
    },
    "main.timing_and_audio_constraints_json": {
      "value": "{\"duration_seconds\":30,\"frame_rate\":30,\"brand_hold_frames\":30,\"audio\":\"licensed_sfx_only\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_brief_json,main.downstream_owner,main.execution_constraints_json,main.output_language,main.selected_shot_cards_json,main.shot_library_index_json,main.shot_library_revision,main.source_asset_map_json,main.timing_and_audio_constraints_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/product-promo-shot-design-beta@1.0.0-beta.1?locale=en","role":"shot-plan"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks shot-plan -->
### 结果示例与检查

示例目标：Shot Plan。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
输出结构示例见 [video-shotcraft-guided.output](../fixtures/shot-plan.en/video-shotcraft-guided.output.json)。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/shot-plan.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

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

# 产品宣传片镜头设计 beta

本方案补充“真实产品资料和页面 → 已确认产品宣传片 Brief → 镜头卡映射与镜头计划”的语义层。它不负责页面采集、Remotion 编码、渲染、剪辑、费用、发布或资产接受。

可编译模板只有英文：

- `brief`：固定产品事实、受众、创作模式、品牌、交付、数据和 rights，生成 `product_promo_brief.v1`。
- `shot-plan`：消费已接受 Brief、固定版本的镜头库索引和资产映射，生成 `product_promo_shot_plan.v1`。

中文译文只在 `template-zh-CN.md` 中供人工审阅。中文产品资料可以通过英文 contract 注入，`output_language` 决定模型产物语言。

## 与 video-shotcraft 的集成

首个 canary 使用 `Vincentwei1021/video-shotcraft` 的提交 `5f047c7cfe10d6616fe59160a750fcfaea510b2e`。该仓库是完整外部 Skill 和 Remotion 生产工具包，不是 Promptrepo 模板仓，因此：

- Template Registry 不把它加入 `prompt repository`；
- Agent runtime 单独安装并固定外部 Skill；
- `gallery/api/library.json` 作为带修订号的公开镜头库来源导入当前 Registry session；
- 本方案的 `brief` 与 `shot-plan` 通过 recipe 串联；
- 生成的语义镜头计划交给 `video-shotcraft` 或 Scaena/Remotion owner 执行。

详细边界、安装和恢复见 `video-shotcraft-integration.md`。CLI 生成的 recipe 位于 `examples/video-shotcraft-product-promo.recipe.json`。

公开合成 example 由 Registry fixture 命令生成，可直接查看或复制为自己的输入文件：

- `fixtures/brief.en/video-shotcraft-guided.input.json`
- `fixtures/brief.en/video-shotcraft-guided.output.json`
- `fixtures/shot-plan.en/video-shotcraft-guided.input.json`
- `fixtures/shot-plan.en/video-shotcraft-guided.output.json`

这些 example 不含真实产品资料、凭据或 Provider payload。替换字段后仍需在自己的 session 中导入、确认和编译，不能把 fixture 的确认状态带入真实任务。
