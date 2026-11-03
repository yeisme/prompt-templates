<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI 做剧模块化角色资产：完整使用教程

无头发头模、中性身体核心与可替换表面/穿戴层的模块化角色资产

## 如何提出需求

适用目标：由 Eikona 按 slot 渲染单视图；Scaena 只消费安全 refs；preview 不是 canonical 资产。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI 做剧模块化角色资产」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-drama-character-assets@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

先建立 head-core-bald-v1 与 body-core-neutral-v1；surface-coat-hair-v1、wearable-garment-v1、wearable-accessory-v1 分别描述表面和单件穿戴。character-layer-preview-v1 检查单层组合，character-harmonized-preview-v1 检查整体。各层通过已接受引用衔接，不能由目录顺序推断可覆盖基础身份。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `body-core-neutral-v1`

职责：Create a neutral body proportion reference for reusable character assembly.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`body-core-neutral-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs body-core-neutral-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/body-core-neutral-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `age_band` | enum／必填 | minor/unknown 触发最保守覆盖与安全门；由用户选择并确认 | enum=["adult", "minor", "unknown"] | adult |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（锚点、接口、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"proportions":"7.2 头身，肩胯平衡","posture_anchor":"自然直立，双臂下垂","fit_interfaces":["颈肩衔接","腰线","腕踝边界"],"coverage":"neutral_full","observable_features":["惯用右手","站姿重心居中"],"view_plan":["detail_front","front_left_three_quarter","left_profile","back","right_profile","front_right_three_quarter"],"required_evidence":["比例锚点","贴合接口"],"forbid":["face","hair","wardrobe","accessory","environment"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"body_core":[{"ref":"slot:body-core-neutral-v1@rev-0002","inherit":["body_proportion","fit_landmarks"],"forbid":["face","hairline","expression","body_identity","environment"]}],"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette","fabric_rendering"],"forbid":["creator_identity","protected_works"]}]} |
| `render_policy_json` | string／必填 | 画幅、透明输出与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["body_core"] | body_core |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `topology_family` | enum／必填 | 角色身体/头部结构族；由用户选择并确认 | enum=["humanoid", "quadruped", "winged", "serpentine", "mechanical"] | humanoid |
| `view_id` | enum／必填 | 本轮唯一生产视图（六视图合同）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example body-core-neutral-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'body-core-neutral-v1' --output 'body-core-neutral-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'body-core-neutral-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'body-core-neutral-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 adult-humanoid-front；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.age_band": {
      "value": "adult",
      "kind": "user",
      "source": "user"
    },
    "main.design_spec_json": {
      "value": "{\"proportions\":\"7.2 头身，肩胯平衡\",\"posture_anchor\":\"自然直立，双臂下垂\",\"fit_interfaces\":[\"颈肩衔接\",\"腰线\",\"腕踝边界\"],\"coverage\":\"neutral_full\",\"observable_features\":[\"惯用右手\",\"站姿重心居中\"],\"view_plan\":[\"detail_front\",\"front_left_three_quarter\",\"left_profile\",\"back\",\"right_profile\",\"front_right_three_quarter\"],\"required_evidence\":[\"比例锚点\",\"贴合接口\"],\"forbid\":[\"face\",\"hair\",\"wardrobe\",\"accessory\",\"environment\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"body_core\":[{\"ref\":\"slot:body-core-neutral-v1@rev-0002\",\"inherit\":[\"body_proportion\",\"fit_landmarks\"],\"forbid\":[\"face\",\"hairline\",\"expression\",\"body_identity\",\"environment\"]}],\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\",\"fabric_rendering\"],\"forbid\":[\"creator_identity\",\"protected_works\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "body_core",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.topology_family": {
      "value": "humanoid",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.age_band,main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.topology_family,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"body-core-neutral-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks body-core-neutral-v1 -->
### 结果示例与检查

示例目标：Neutral body reference。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `character-harmonized-preview-v1`

职责：Review a visually harmonized assembled character.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`character-harmonized-preview-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs character-harmonized-preview-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/character-harmonized-preview-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `preview_kind` | enum／必填 | 本模板锁定的预览用途；由用户选择并确认 | enum=["harmonized_read"] | harmonized_read |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"head_core":[{"ref":"slot:head-core-bald-v1@rev-0003","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"body_core":[{"ref":"slot:body-core-neutral-v1@rev-0002","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"surface_coat":[{"ref":"slot:surface-coat-hair-v1@rev-0004","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"wearable":[{"ref":"slot:wearable-garment-v1@rev-0005","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布策略与协调选项 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"harmonize":["light","material_feel","color"],"preserve":["source_designs","digests"]} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["preview"] | preview |
| `source_refs_json` | string／必填 | 分层 source 的精确 refs（slot/version/digest/view）JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"slot_id":"body_core","source_version":"slot:body-core-neutral-v1@rev-0002","artifact_digest":"sha256:995b22dc4023327e9188c914e6573a711e579b4871b011ed0beb4e5c5f720027","view_id":"detail_front"},{"slot_id":"head_core","source_version":"slot:head-core-bald-v1@rev-0003","artifact_digest":"sha256:0f4d3d3b709b29b41183dc503062e42ab80ed2146ac034bbd0ee2870aca1d747","view_id":"detail_front"},{"slot_id":"surface_coat","source_version":"slot:surface-coat-hair-v1@rev-0004","artifact_digest":"sha256:78e47cdcad87dfc087a617409a008d247f9e28d01eba2f9a894edae00b7b1d53","view_id":"detail_front"},{"slot_id":"wearable","source_version":"slot:wearable-garment-v1@rev-0005","artifact_digest":"sha256:a007531ab58ee741a47988287737368e8e9f0c52e283f33de507696798fe54ff","view_id":"detail_front"}] |
| `view_id` | enum／必填 | 本轮唯一合成视图（六视图或 adaptive）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter", "adaptive"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example character-harmonized-preview-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-harmonized-preview-v1' --output 'character-harmonized-preview-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-harmonized-preview-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-harmonized-preview-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 harmonized-read-lineage；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
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
      "value": "{\"head_core\":[{\"ref\":\"slot:head-core-bald-v1@rev-0003\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"body_core\":[{\"ref\":\"slot:body-core-neutral-v1@rev-0002\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"surface_coat\":[{\"ref\":\"slot:surface-coat-hair-v1@rev-0004\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"wearable\":[{\"ref\":\"slot:wearable-garment-v1@rev-0005\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"harmonize\":[\"light\",\"material_feel\",\"color\"],\"preserve\":[\"source_designs\",\"digests\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "preview",
      "kind": "user",
      "source": "user"
    },
    "main.source_refs_json": {
      "value": "[{\"slot_id\":\"body_core\",\"source_version\":\"slot:body-core-neutral-v1@rev-0002\",\"artifact_digest\":\"sha256:995b22dc4023327e9188c914e6573a711e579b4871b011ed0beb4e5c5f720027\",\"view_id\":\"detail_front\"},{\"slot_id\":\"head_core\",\"source_version\":\"slot:head-core-bald-v1@rev-0003\",\"artifact_digest\":\"sha256:0f4d3d3b709b29b41183dc503062e42ab80ed2146ac034bbd0ee2870aca1d747\",\"view_id\":\"detail_front\"},{\"slot_id\":\"surface_coat\",\"source_version\":\"slot:surface-coat-hair-v1@rev-0004\",\"artifact_digest\":\"sha256:78e47cdcad87dfc087a617409a008d247f9e28d01eba2f9a894edae00b7b1d53\",\"view_id\":\"detail_front\"},{\"slot_id\":\"wearable\",\"source_version\":\"slot:wearable-garment-v1@rev-0005\",\"artifact_digest\":\"sha256:a007531ab58ee741a47988287737368e8e9f0c52e283f33de507696798fe54ff\",\"view_id\":\"detail_front\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"character-harmonized-preview-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks character-harmonized-preview-v1 -->
### 结果示例与检查

示例目标：Character harmonization preview。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `character-layer-preview-v1`

职责：Preview the alignment of character layers before harmonization.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`character-layer-preview-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs character-layer-preview-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/character-layer-preview-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `preview_kind` | enum／必填 | 本模板锁定的预览用途；由用户选择并确认 | enum=["layer_alignment"] | layer_alignment |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"head_core":[{"ref":"slot:head-core-bald-v1@rev-0003","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"body_core":[{"ref":"slot:body-core-neutral-v1@rev-0002","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"surface_coat":[{"ref":"slot:surface-coat-hair-v1@rev-0004","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}],"wearable":[{"ref":"slot:wearable-garment-v1@rev-0005","inherit":["read_only"],"forbid":["rewrite","extend_scope"]}]} |
| `render_policy_json` | string／必填 | 画幅、画布策略与协调选项 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"composite":"layer_stack_echo"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["preview"] | preview |
| `source_refs_json` | string／必填 | 分层 source 的精确 refs（slot/version/digest/view）JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"slot_id":"body_core","source_version":"slot:body-core-neutral-v1@rev-0002","artifact_digest":"sha256:995b22dc4023327e9188c914e6573a711e579b4871b011ed0beb4e5c5f720027","view_id":"detail_front"},{"slot_id":"head_core","source_version":"slot:head-core-bald-v1@rev-0003","artifact_digest":"sha256:0f4d3d3b709b29b41183dc503062e42ab80ed2146ac034bbd0ee2870aca1d747","view_id":"detail_front"},{"slot_id":"surface_coat","source_version":"slot:surface-coat-hair-v1@rev-0004","artifact_digest":"sha256:78e47cdcad87dfc087a617409a008d247f9e28d01eba2f9a894edae00b7b1d53","view_id":"detail_front"},{"slot_id":"wearable","source_version":"slot:wearable-garment-v1@rev-0005","artifact_digest":"sha256:a007531ab58ee741a47988287737368e8e9f0c52e283f33de507696798fe54ff","view_id":"detail_front"}] |
| `view_id` | enum／必填 | 本轮唯一合成视图（六视图或 adaptive）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter", "adaptive"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example character-layer-preview-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-layer-preview-v1' --output 'character-layer-preview-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-layer-preview-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'character-layer-preview-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 lineage-exact-composite；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
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
      "value": "{\"head_core\":[{\"ref\":\"slot:head-core-bald-v1@rev-0003\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"body_core\":[{\"ref\":\"slot:body-core-neutral-v1@rev-0002\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"surface_coat\":[{\"ref\":\"slot:surface-coat-hair-v1@rev-0004\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}],\"wearable\":[{\"ref\":\"slot:wearable-garment-v1@rev-0005\",\"inherit\":[\"read_only\"],\"forbid\":[\"rewrite\",\"extend_scope\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"composite\":\"layer_stack_echo\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "preview",
      "kind": "user",
      "source": "user"
    },
    "main.source_refs_json": {
      "value": "[{\"slot_id\":\"body_core\",\"source_version\":\"slot:body-core-neutral-v1@rev-0002\",\"artifact_digest\":\"sha256:995b22dc4023327e9188c914e6573a711e579b4871b011ed0beb4e5c5f720027\",\"view_id\":\"detail_front\"},{\"slot_id\":\"head_core\",\"source_version\":\"slot:head-core-bald-v1@rev-0003\",\"artifact_digest\":\"sha256:0f4d3d3b709b29b41183dc503062e42ab80ed2146ac034bbd0ee2870aca1d747\",\"view_id\":\"detail_front\"},{\"slot_id\":\"surface_coat\",\"source_version\":\"slot:surface-coat-hair-v1@rev-0004\",\"artifact_digest\":\"sha256:78e47cdcad87dfc087a617409a008d247f9e28d01eba2f9a894edae00b7b1d53\",\"view_id\":\"detail_front\"},{\"slot_id\":\"wearable\",\"source_version\":\"slot:wearable-garment-v1@rev-0005\",\"artifact_digest\":\"sha256:a007531ab58ee741a47988287737368e8e9f0c52e283f33de507696798fe54ff\",\"view_id\":\"detail_front\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"character-layer-preview-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks character-layer-preview-v1 -->
### 结果示例与检查

示例目标：Character layer preview。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `head-core-bald-v1`

职责：Create an isolated head identity reference without hair or accessories.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`head-core-bald-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs head-core-bald-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/head-core-bald-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `age_band` | enum／必填 | minor/unknown 触发最保守覆盖与安全门；由用户选择并确认 | enum=["adult", "minor", "unknown"] | adult |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（锚点、接口、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"identity_anchor":"成年女性，鹅蛋脸，眉目清朗，左眉尾小疤","scalp_interface":{"hairline":"完整自然发际线接口","crown":"颅顶弧线完整","ear_seats":"双耳贴合位保留"},"skin":"真实皮肤纹理，哑光","permanent_features":["左眉尾小疤","耳垂圆形"],"view_plan":["detail_front","front_left_three_quarter","left_profile","back","right_profile","front_right_three_quarter"],"required_evidence":["完整头顶","后脑轮廓","双耳","自然头皮"],"forbid":["hair","makeup","jewelry","neck","shoulders","clothing","background"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"head_core":[{"ref":"slot:head-core-bald-v1@rev-0003","inherit":["head_shape","scalp_contour","attachment_landmarks"],"forbid":["expression","makeup","jewelry","wardrobe","background"]}],"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette","stroke_softness"],"forbid":["creator_identity","protected_works"]}]} |
| `render_policy_json` | string／必填 | 画幅、透明输出与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["head_core"] | head_core |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `topology_family` | enum／必填 | 角色身体/头部结构族；由用户选择并确认 | enum=["humanoid", "quadruped", "winged", "serpentine", "mechanical"] | humanoid |
| `view_id` | enum／必填 | 本轮唯一生产视图（六视图合同）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter"] | back |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example head-core-bald-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'head-core-bald-v1' --output 'head-core-bald-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'head-core-bald-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'head-core-bald-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 view-back；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.age_band": {
      "value": "adult",
      "kind": "user",
      "source": "user"
    },
    "main.design_spec_json": {
      "value": "{\"identity_anchor\":\"成年女性，鹅蛋脸，眉目清朗，左眉尾小疤\",\"scalp_interface\":{\"hairline\":\"完整自然发际线接口\",\"crown\":\"颅顶弧线完整\",\"ear_seats\":\"双耳贴合位保留\"},\"skin\":\"真实皮肤纹理，哑光\",\"permanent_features\":[\"左眉尾小疤\",\"耳垂圆形\"],\"view_plan\":[\"detail_front\",\"front_left_three_quarter\",\"left_profile\",\"back\",\"right_profile\",\"front_right_three_quarter\"],\"required_evidence\":[\"完整头顶\",\"后脑轮廓\",\"双耳\",\"自然头皮\"],\"forbid\":[\"hair\",\"makeup\",\"jewelry\",\"neck\",\"shoulders\",\"clothing\",\"background\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"head_core\":[{\"ref\":\"slot:head-core-bald-v1@rev-0003\",\"inherit\":[\"head_shape\",\"scalp_contour\",\"attachment_landmarks\"],\"forbid\":[\"expression\",\"makeup\",\"jewelry\",\"wardrobe\",\"background\"]}],\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\",\"stroke_softness\"],\"forbid\":[\"creator_identity\",\"protected_works\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "head_core",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.topology_family": {
      "value": "humanoid",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "back",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.age_band,main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.topology_family,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"head-core-bald-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks head-core-bald-v1 -->
### 结果示例与检查

示例目标：Bald head identity。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `surface-coat-hair-v1`

职责：Create an isolated hair layer matched to the character identity.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`surface-coat-hair-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs surface-coat-hair-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/surface-coat-hair-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `age_band` | enum／必填 | minor/unknown 触发非成人化造型与最保守策略；由用户选择并确认 | enum=["adult", "minor", "unknown"] | adult |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（贴合接口、层级、遮挡/碰撞、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"layer":"surface_coat","attachment_interface":{"hairline":"贴合同一发际线接口","crown_anchor":"颅顶"},"silhouette":"低束发髻，碎发收拢","material":"哑光黑发，真实发流","color_regions":["深黑主区","鬓角深棕过渡"],"length":"及肩低束","occlusion_rules":["双耳上缘轻度遮挡"],"collision_risks":["与高领内衫领口碰撞"],"layer_order":2,"inherit":["head_shape","scalp_contour","attachment_landmarks"],"forbid":["facial_features","expression","jewelry","wardrobe","background"],"view_plan":["detail_front","front_left_three_quarter","left_profile","back","right_profile","front_right_three_quarter"],"required_evidence":["贴合接口","后脑轮廓"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"head_core":[{"ref":"slot:head-core-bald-v1@rev-0003","inherit":["head_shape","scalp_contour","hairline_landmarks"],"forbid":["facial_features","expression","jewelry","wardrobe","background"]}],"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette"],"forbid":["creator_identity","protected_works"]}]} |
| `render_policy_json` | string／必填 | 画幅、透明输出与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["surface_coat"] | surface_coat |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `topology_family` | enum／必填 | 角色身体/头部结构族；由用户选择并确认 | enum=["humanoid", "quadruped", "winged", "serpentine", "mechanical"] | humanoid |
| `view_id` | enum／必填 | 本轮唯一生产视图（六视图合同）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example surface-coat-hair-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'surface-coat-hair-v1' --output 'surface-coat-hair-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'surface-coat-hair-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'surface-coat-hair-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 adult-hair-layer-detail-front；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.age_band": {
      "value": "adult",
      "kind": "user",
      "source": "user"
    },
    "main.design_spec_json": {
      "value": "{\"layer\":\"surface_coat\",\"attachment_interface\":{\"hairline\":\"贴合同一发际线接口\",\"crown_anchor\":\"颅顶\"},\"silhouette\":\"低束发髻，碎发收拢\",\"material\":\"哑光黑发，真实发流\",\"color_regions\":[\"深黑主区\",\"鬓角深棕过渡\"],\"length\":\"及肩低束\",\"occlusion_rules\":[\"双耳上缘轻度遮挡\"],\"collision_risks\":[\"与高领内衫领口碰撞\"],\"layer_order\":2,\"inherit\":[\"head_shape\",\"scalp_contour\",\"attachment_landmarks\"],\"forbid\":[\"facial_features\",\"expression\",\"jewelry\",\"wardrobe\",\"background\"],\"view_plan\":[\"detail_front\",\"front_left_three_quarter\",\"left_profile\",\"back\",\"right_profile\",\"front_right_three_quarter\"],\"required_evidence\":[\"贴合接口\",\"后脑轮廓\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"head_core\":[{\"ref\":\"slot:head-core-bald-v1@rev-0003\",\"inherit\":[\"head_shape\",\"scalp_contour\",\"hairline_landmarks\"],\"forbid\":[\"facial_features\",\"expression\",\"jewelry\",\"wardrobe\",\"background\"]}],\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\"],\"forbid\":[\"creator_identity\",\"protected_works\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "surface_coat",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.topology_family": {
      "value": "humanoid",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.age_band,main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.topology_family,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"surface-coat-hair-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks surface-coat-hair-v1 -->
### 结果示例与检查

示例目标：Hair surface layer。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `wearable-accessory-v1`

职责：Create an isolated wearable accessory reference.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`wearable-accessory-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs wearable-accessory-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/wearable-accessory-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `age_band` | enum／必填 | minor/unknown 触发非成人化佩戴与最保守策略；由用户选择并确认 | enum=["adult", "minor", "unknown"] | adult |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（贴合接口、单件边界、层级、遮挡/碰撞、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"item":"鹿角状头角（extension_part）","attachment_interface":{"anchor":"颅顶角基接口"},"articulation":"微动自由度 5°","layer_order":2,"silhouette":"后掠双角","material":"骨质哑光","color_regions":["灰白主区"],"occlusion_rules":["高于 surface_coat"],"collision_risks":["与低枝碰撞"],"inherit":["head_anchor_geometry"],"forbid":["facial_features","expression","wardrobe","background"],"view_plan":["detail_front","front_left_three_quarter","left_profile","back","right_profile","front_right_three_quarter"],"required_evidence":["连接边界","自由度"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"body_core":[{"ref":"slot:body-core-neutral-v1@rev-0002","inherit":["head_anchor_geometry","hair_anchor"],"forbid":["facial_features","expression","hair","wardrobe","background"]}],"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette"],"forbid":["creator_identity","protected_works"]}]} |
| `render_policy_json` | string／必填 | 画幅、透明输出与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot（装饰或扩展部件）；由用户选择并确认 | enum=["accessory", "extension_part"] | extension_part |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `topology_family` | enum／必填 | 角色身体/头部结构族；由用户选择并确认 | enum=["humanoid", "quadruped", "winged", "serpentine", "mechanical"] | humanoid |
| `view_id` | enum／必填 | 本轮唯一生产视图（六视图合同）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example wearable-accessory-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-accessory-v1' --output 'wearable-accessory-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-accessory-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-accessory-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 extension-part-horn；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.age_band": {
      "value": "adult",
      "kind": "user",
      "source": "user"
    },
    "main.design_spec_json": {
      "value": "{\"item\":\"鹿角状头角（extension_part）\",\"attachment_interface\":{\"anchor\":\"颅顶角基接口\"},\"articulation\":\"微动自由度 5°\",\"layer_order\":2,\"silhouette\":\"后掠双角\",\"material\":\"骨质哑光\",\"color_regions\":[\"灰白主区\"],\"occlusion_rules\":[\"高于 surface_coat\"],\"collision_risks\":[\"与低枝碰撞\"],\"inherit\":[\"head_anchor_geometry\"],\"forbid\":[\"facial_features\",\"expression\",\"wardrobe\",\"background\"],\"view_plan\":[\"detail_front\",\"front_left_three_quarter\",\"left_profile\",\"back\",\"right_profile\",\"front_right_three_quarter\"],\"required_evidence\":[\"连接边界\",\"自由度\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"body_core\":[{\"ref\":\"slot:body-core-neutral-v1@rev-0002\",\"inherit\":[\"head_anchor_geometry\",\"hair_anchor\"],\"forbid\":[\"facial_features\",\"expression\",\"hair\",\"wardrobe\",\"background\"]}],\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\"],\"forbid\":[\"creator_identity\",\"protected_works\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "extension_part",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.topology_family": {
      "value": "humanoid",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.age_band,main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.topology_family,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"wearable-accessory-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks wearable-accessory-v1 -->
### 结果示例与检查

示例目标：Accessory layer。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `wearable-garment-v1`

职责：Create an isolated garment reference for character assembly.

精确引用：`promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`；role：`wearable-garment-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs wearable-garment-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/wearable-garment-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `age_band` | enum／必填 | minor/unknown 触发 age-appropriate 覆盖与非成人化剪裁；由用户选择并确认 | enum=["adult", "minor", "unknown"] | adult |
| `design_spec_json` | string／必填 | 该 slot 的设计规格 JSON（贴合接口、单件边界、层级、遮挡/碰撞、继承/禁止）；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"item":"月白色丝绸交领内衫（单件）","fit_interface":{"肩线":"贴合 body_core 肩锚","腰线":"自然落腰","袖窿":"直袖"},"layer_order":1,"silhouette":"直身宽袖","material":"不透明丝绸","color_regions":["月白主色","衣缘细青线"],"occlusion_rules":["内搭层压住 body_core 覆盖"],"collision_risks":["与腰封碰撞"],"inherit":["body_proportion","fit_landmarks"],"forbid":["face","hairline","expression","body_identity","environment"],"view_plan":["detail_front","front_left_three_quarter","left_profile","back","right_profile","front_right_three_quarter"],"required_evidence":["贴合点","开合方式"]} |
| `output_schema_version` | enum／必填 | Prompt Bundle 输出 schema 版本；由用户选择并确认 | enum=["character_asset.modular_slot_bundle.v1"] | character_asset.modular_slot_bundle.v1 |
| `reference_bindings_json` | string／必填 | 带 inherit/forbid 的安全绑定 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"body_core":[{"ref":"slot:body-core-neutral-v1@rev-0002","inherit":["body_proportion","fit_landmarks"],"forbid":["face","hairline","expression","body_identity","environment"]}],"style_source":[{"ref":"reference:style-ink-wash-01@v1","inherit":["color_palette","fabric_rendering"],"forbid":["creator_identity","protected_works"]}]} |
| `render_policy_json` | string／必填 | 画幅、透明输出与单视图渲染策略 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=32768 | {"aspect_ratio":"3:2","canvas":"transparent_rgba","single_view":true,"edge":"anti_aliased"} |
| `schema_version` | enum／必填 | 消费方输入合同版本；由用户选择并确认 | enum=["eikona.character_asset_prompt_input.v2"] | eikona.character_asset_prompt_input.v2 |
| `slot_id` | enum／必填 | 本模板锁定的 slot；由用户选择并确认 | enum=["wearable"] | wearable |
| `style_profile_json` | string／必填 | 原创维度化视觉约束 JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=65536 | {"palette":"低饱和墨青与月白","stroke":"柔边写实","light":"均匀柔光","forbidden":["在世创作者复刻","受保护作品风格"]} |
| `topology_family` | enum／必填 | 角色身体/头部结构族；由用户选择并确认 | enum=["humanoid", "quadruped", "winged", "serpentine", "mechanical"] | humanoid |
| `view_id` | enum／必填 | 本轮唯一生产视图（六视图合同）；由用户选择并确认 | enum=["detail_front", "front_left_three_quarter", "left_profile", "back", "right_profile", "front_right_three_quarter"] | detail_front |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example wearable-garment-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-garment-v1' --output 'wearable-garment-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-garment-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en' --role 'wearable-garment-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 adult-single-garment-front；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.age_band": {
      "value": "adult",
      "kind": "user",
      "source": "user"
    },
    "main.design_spec_json": {
      "value": "{\"item\":\"月白色丝绸交领内衫（单件）\",\"fit_interface\":{\"肩线\":\"贴合 body_core 肩锚\",\"腰线\":\"自然落腰\",\"袖窿\":\"直袖\"},\"layer_order\":1,\"silhouette\":\"直身宽袖\",\"material\":\"不透明丝绸\",\"color_regions\":[\"月白主色\",\"衣缘细青线\"],\"occlusion_rules\":[\"内搭层压住 body_core 覆盖\"],\"collision_risks\":[\"与腰封碰撞\"],\"inherit\":[\"body_proportion\",\"fit_landmarks\"],\"forbid\":[\"face\",\"hairline\",\"expression\",\"body_identity\",\"environment\"],\"view_plan\":[\"detail_front\",\"front_left_three_quarter\",\"left_profile\",\"back\",\"right_profile\",\"front_right_three_quarter\"],\"required_evidence\":[\"贴合点\",\"开合方式\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "character_asset.modular_slot_bundle.v1",
      "kind": "user",
      "source": "user"
    },
    "main.reference_bindings_json": {
      "value": "{\"body_core\":[{\"ref\":\"slot:body-core-neutral-v1@rev-0002\",\"inherit\":[\"body_proportion\",\"fit_landmarks\"],\"forbid\":[\"face\",\"hairline\",\"expression\",\"body_identity\",\"environment\"]}],\"style_source\":[{\"ref\":\"reference:style-ink-wash-01@v1\",\"inherit\":[\"color_palette\",\"fabric_rendering\"],\"forbid\":[\"creator_identity\",\"protected_works\"]}]}",
      "kind": "user",
      "source": "user"
    },
    "main.render_policy_json": {
      "value": "{\"aspect_ratio\":\"3:2\",\"canvas\":\"transparent_rgba\",\"single_view\":true,\"edge\":\"anti_aliased\"}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "eikona.character_asset_prompt_input.v2",
      "kind": "user",
      "source": "user"
    },
    "main.slot_id": {
      "value": "wearable",
      "kind": "user",
      "source": "user"
    },
    "main.style_profile_json": {
      "value": "{\"palette\":\"低饱和墨青与月白\",\"stroke\":\"柔边写实\",\"light\":\"均匀柔光\",\"forbidden\":[\"在世创作者复刻\",\"受保护作品风格\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.topology_family": {
      "value": "humanoid",
      "kind": "user",
      "source": "user"
    },
    "main.view_id": {
      "value": "detail_front",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.age_band,main.design_spec_json,main.output_schema_version,main.reference_bindings_json,main.render_policy_json,main.schema_version,main.slot_id,main.style_profile_json,main.topology_family,main.view_id --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en","role":"wearable-garment-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks wearable-garment-v1 -->
### 结果示例与检查

示例目标：Garment layer。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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
