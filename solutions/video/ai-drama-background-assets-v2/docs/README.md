<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI 做剧模块化环境资产 v2：完整使用教程

独立语义物件与无人物空场景壳的模块化环境资产

## 如何提出需求

适用目标：由 Eikona 按 slot 渲染；空场景壳必须零人物零物件且完整不透明。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI 做剧模块化环境资产 v2」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-drama-background-assets-v2@2.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

semantic-object-v1 与 empty-scene-shell-v1 分别准备语义物件和空场景壳；environment-layer-preview-v1 检查单层布局，environment-harmonized-preview-v1 检查整体环境。后两者需要真实、已接受的上游引用。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `empty-scene-shell-v1`

职责：Create a reusable empty environment without foreground subjects.

精确引用：`promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en`；role：`empty-scene-shell-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs empty-scene-shell-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/empty-scene-shell-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（定义、接口、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"location":"南方小镇茶馆内堂","fixed_structures":["木柱","二层回廊","柜台","楼梯"],"anchors":["入口门框中轴","柜台左角","楼梯第三级"],"activity_zones":["堂中八仙桌区"],"lighting":"午后侧光自西窗","time":"未时","weather":"晴","reverse_anchors":"复用同一锚点与光源方向","inherit":[],"forbid":["humans","human_traces","loose_objects","brand_text"],"view_plan":[{"view_id":"master_wide","reason":"主机位锁全场锚点"},{"view_id":"reverse_counter","reason":"反打复用锚点"}]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette","light_logic"],"forbid":["creator_identity","protected_works","human_figure"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布语义与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"16:9","canvas":"opaque_full_canvas","single_view":true} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.background_asset_prompt_input.v2"] | eikona.background_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["environment_shell"] | environment_shell |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `view_plan_json` | string／必填 | geometry-adaptive 视图计划与选择原因 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"view":{"view_id":"master_wide","reason":"主机位锁全场锚点与预留区"}} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example empty-scene-shell-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'empty-scene-shell-v1' --output 'empty-scene-shell-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'empty-scene-shell-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'empty-scene-shell-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 empty-interior-anchors；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.design_spec_json": {
      "value": "{\"location\":\"南方小镇茶馆内堂\",\"fixed_structures\":[\"木柱\",\"二层回廊\",\"柜台\",\"楼梯\"],\"anchors\":[\"入口门框中轴\",\"柜台左角\",\"楼梯第三级\"],\"activity_zones\":[\"堂中八仙桌区\"],\"lighting\":\"午后侧光自西窗\",\"time\":\"未时\",\"weather\":\"晴\",\"reverse_anchors\":\"复用同一锚点与光源方向\",\"inherit\":[],\"forbid\":[\"humans\",\"human_traces\",\"loose_objects\",\"brand_text\"],\"view_plan\":[{\"view_id\":\"master_wide\",\"reason\":\"主机位锁全场锚点\"},{\"view_id\":\"reverse_counter\",\"reason\":\"反打复用锚点\"}]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\",\"light_logic\"],\"forbid\":[\"creator_identity\",\"protected_works\",\"human_figure\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"16:9\",\"canvas\":\"opaque_full_canvas\",\"single_view\":true}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.background_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "environment_shell",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.view_plan_json": {
      "value": "{\"view\":{\"view_id\":\"master_wide\",\"reason\":\"主机位锁全场锚点与预留区\"}}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.view_plan_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en","role":"empty-scene-shell-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks empty-scene-shell-v1 -->
### 结果示例与检查

示例目标：Empty scene shell。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `environment-harmonized-preview-v1`

职责：Review the assembled environment for visual consistency.

精确引用：`promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en`；role：`environment-harmonized-preview-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs environment-harmonized-preview-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/environment-harmonized-preview-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `preview_kind` | enum／必填 | 本模板锁定的预览用途；由用户选择并确认 | enum=["harmonized_read"] | harmonized_read |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"environment_shell":[{"ref":"slot:empty-scene-shell-v1@rev-0006","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"semantic_object":[{"ref":"slot:semantic-object-v1@rev-0007","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布策略与协调选项 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"16:9","canvas":"opaque_full_canvas","single_view":true,"harmonize":["light","color"],"preserve":["anchors","light_direction","activity_zones"]} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.background_asset_prompt_input.v2"] | eikona.background_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["preview"] | preview |
| `source_refs_json` | string／必填 | 分层 source 的精确 refs（slot/version/digest/view）JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"slot_id":"environment_shell","source_version":"slot:empty-scene-shell-v1@rev-0006","artifact_digest":"sha256:c024e698d7cdd0f3ee897d7ea41d154131dead5f01667e2f2433cb969aaf4bb2","view_id":"adaptive"},{"slot_id":"semantic_object","source_version":"slot:semantic-object-v1@rev-0007","artifact_digest":"sha256:c6dcc4a87e11542d39554977ee3369c08db78c2a7499cd40400a0a4ef69ddec0","view_id":"adaptive"}] |
| `view_id` | enum／必填 | 本轮唯一合成视图（六视图或 adaptive）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter", "adaptive"] | adaptive |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example environment-harmonized-preview-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-harmonized-preview-v1' --output 'environment-harmonized-preview-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-harmonized-preview-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-harmonized-preview-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 env-harmonized-lineage；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.preview_kind": {
      "value": "harmonized_read",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"environment_shell\":[{\"ref\":\"slot:empty-scene-shell-v1@rev-0006\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"semantic_object\":[{\"ref\":\"slot:semantic-object-v1@rev-0007\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"16:9\",\"canvas\":\"opaque_full_canvas\",\"single_view\":true,\"harmonize\":[\"light\",\"color\"],\"preserve\":[\"anchors\",\"light_direction\",\"activity_zones\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.background_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "preview",
      "kind": "user",
      "source": "user"
    },
    "main.source_refs_json": {
      "value": "[{\"slot_id\":\"environment_shell\",\"source_version\":\"slot:empty-scene-shell-v1@rev-0006\",\"artifact_digest\":\"sha256:c024e698d7cdd0f3ee897d7ea41d154131dead5f01667e2f2433cb969aaf4bb2\",\"view_id\":\"adaptive\"},{\"slot_id\":\"semantic_object\",\"source_version\":\"slot:semantic-object-v1@rev-0007\",\"artifact_digest\":\"sha256:c6dcc4a87e11542d39554977ee3369c08db78c2a7499cd40400a0a4ef69ddec0\",\"view_id\":\"adaptive\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "adaptive",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.output_schema_version,main.preview_kind,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.source_refs_json,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en","role":"environment-harmonized-preview-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks environment-harmonized-preview-v1 -->
### 结果示例与检查

示例目标：Environment harmonization preview。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `environment-layer-preview-v1`

职责：Preview environment layer placement and spatial alignment.

精确引用：`promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en`；role：`environment-layer-preview-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs environment-layer-preview-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/environment-layer-preview-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `preview_kind` | enum／必填 | 本模板锁定的预览用途；由用户选择并确认 | enum=["layer_alignment"] | layer_alignment |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"environment_shell":[{"ref":"slot:empty-scene-shell-v1@rev-0006","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"semantic_object":[{"ref":"slot:semantic-object-v1@rev-0007","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布策略与协调选项 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"16:9","canvas":"opaque_full_canvas","single_view":true,"composite":"anchor_placement_echo"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.background_asset_prompt_input.v2"] | eikona.background_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["preview"] | preview |
| `source_refs_json` | string／必填 | 分层 source 的精确 refs（slot/version/digest/view）JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"slot_id":"environment_shell","source_version":"slot:empty-scene-shell-v1@rev-0006","artifact_digest":"sha256:c024e698d7cdd0f3ee897d7ea41d154131dead5f01667e2f2433cb969aaf4bb2","view_id":"adaptive"},{"slot_id":"semantic_object","source_version":"slot:semantic-object-v1@rev-0007","artifact_digest":"sha256:c6dcc4a87e11542d39554977ee3369c08db78c2a7499cd40400a0a4ef69ddec0","view_id":"adaptive"}] |
| `view_id` | enum／必填 | 本轮唯一合成视图（六视图或 adaptive）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter", "adaptive"] | adaptive |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example environment-layer-preview-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-layer-preview-v1' --output 'environment-layer-preview-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-layer-preview-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'environment-layer-preview-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 env-layer-lineage；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.preview_kind": {
      "value": "layer_alignment",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"environment_shell\":[{\"ref\":\"slot:empty-scene-shell-v1@rev-0006\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"semantic_object\":[{\"ref\":\"slot:semantic-object-v1@rev-0007\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"16:9\",\"canvas\":\"opaque_full_canvas\",\"single_view\":true,\"composite\":\"anchor_placement_echo\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.background_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "preview",
      "kind": "user",
      "source": "user"
    },
    "main.source_refs_json": {
      "value": "[{\"slot_id\":\"environment_shell\",\"source_version\":\"slot:empty-scene-shell-v1@rev-0006\",\"artifact_digest\":\"sha256:c024e698d7cdd0f3ee897d7ea41d154131dead5f01667e2f2433cb969aaf4bb2\",\"view_id\":\"adaptive\"},{\"slot_id\":\"semantic_object\",\"source_version\":\"slot:semantic-object-v1@rev-0007\",\"artifact_digest\":\"sha256:c6dcc4a87e11542d39554977ee3369c08db78c2a7499cd40400a0a4ef69ddec0\",\"view_id\":\"adaptive\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "adaptive",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.output_schema_version,main.preview_kind,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.source_refs_json,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en","role":"environment-layer-preview-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks environment-layer-preview-v1 -->
### 结果示例与检查

示例目标：Environment layer preview。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `semantic-object-v1`

职责：Create a separately reusable environment object.

精确引用：`promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en`；role：`semantic-object-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs semantic-object-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/semantic-object-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（定义、接口、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"object":"雁翎刀","geometry":"长条形单刃，左右对称","scale_anchor":"全长 1.02 米","material":"夹钢刀身，木柄缠绳","state":"完好","states":["完好","卷刃"],"grip":"柄部持握接口","movable":["刀鞘分离"],"inherit":[],"forbid":["hands","human","environment","brand_text"],"view_plan":[{"view_id":"side_full","reason":"长条对称物件，侧视一图锁定全长与刃口"},{"view_id":"detail_habaki","reason":"刃根结构需特写核对"}],"required_evidence":["尺度","状态"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette","material_rendering"],"forbid":["creator_identity","protected_works","human_figure"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布语义与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.background_asset_prompt_input.v2"] | eikona.background_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["semantic_object"] | semantic_object |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `view_plan_json` | string／必填 | geometry-adaptive 视图计划与选择原因 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"view":{"view_id":"side_full","reason":"长条对称物件，侧视一图锁定全长与刃口，正反面差异可忽略"}} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example semantic-object-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'semantic-object-v1' --output 'semantic-object-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'semantic-object-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en' --role 'semantic-object-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 adaptive-view-plan-reasoned；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.design_spec_json": {
      "value": "{\"object\":\"雁翎刀\",\"geometry\":\"长条形单刃，左右对称\",\"scale_anchor\":\"全长 1.02 米\",\"material\":\"夹钢刀身，木柄缠绳\",\"state\":\"完好\",\"states\":[\"完好\",\"卷刃\"],\"grip\":\"柄部持握接口\",\"movable\":[\"刀鞘分离\"],\"inherit\":[],\"forbid\":[\"hands\",\"human\",\"environment\",\"brand_text\"],\"view_plan\":[{\"view_id\":\"side_full\",\"reason\":\"长条对称物件，侧视一图锁定全长与刃口\"},{\"view_id\":\"detail_habaki\",\"reason\":\"刃根结构需特写核对\"}],\"required_evidence\":[\"尺度\",\"状态\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\",\"material_rendering\"],\"forbid\":[\"creator_identity\",\"protected_works\",\"human_figure\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.background_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "semantic_object",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.view_plan_json": {
      "value": "{\"view\":{\"view_id\":\"side_full\",\"reason\":\"长条对称物件，侧视一图锁定全长与刃口，正反面差异可忽略\"}}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.view_plan_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets-v2@2.0.0?locale=en","role":"semantic-object-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks semantic-object-v1 -->
### 结果示例与检查

示例目标：Semantic environment object。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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

声明的消费者：eikona, scaena。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->
