<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI 短剧分镜拆解：完整使用教程

把单集剧本 segments 转成可审查的导演语义分镜计划

## 如何提出需求

适用目标：用于 Scaena 剧本到分镜候选的主生成与有界修复。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI 短剧分镜拆解」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-drama-storyboard-breakdown@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

main 生成分镜语义方案；用户或领域验证器给出具体问题后，再以实际 semantic_plan 和 repair_findings 调用 repair。修复不能凭空重写来源。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Turn one episode of script segments into a reviewable directorial semantic storyboard plan

精确引用：`promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`inspect, preview, storyboard_handoff`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_story_context_refs_json` | string／必填 | Human-accepted story context references allowed for this run, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；首次从给定剧本创建分镜，没有已接受的长篇上下文引用；来源片段仍须提供。 | min_length=2；max_length=131072 | [] |
| `continuity_facts_json` | string／必填 | Continuity facts that shots may reference, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"fact_ref":"fact:noise-test","text":"本素材已确认产品运行时未惊醒隔壁房间内的宝宝。"},{"fact_ref":"fact:cta-view-details","text":"允许使用 CTA 文案“查看详情”。"}] |
| `direction_json` | string／必填 | Directorial objectives and hard constraints validated and serialized by Scaena；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"aspect_ratio":"9:16","cta_required":true,"duration_ms_max":22000,"duration_ms_min":18000,"shot_count_max":5,"shot_count_min":5} |
| `episode_ref` | string／必填 | Stable reference for the current and only allowed episode；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=1；max_length=256 | episode:ad-001 |
| `known_entities_json` | string／必填 | Controlled character, location, and prop entities serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"kind":"character","name":"妈妈","ref":"character:mother"},{"kind":"character","name":"宝宝","ref":"character:baby"},{"kind":"product","name":"静音搅拌机","ref":"product:quiet-blender"},{"kind":"location","name":"厨房","ref":"location:kitchen"},{"kind":"location","name":"婴儿房","ref":"location:nursery"}] |
| `locale` | enum／必填 | Locale used by the template body and output text；由用户选择并确认 | enum=["en"] | en |
| `output_schema_version` | enum／必填 | Directorial semantic plan schema version the model must return；由用户选择并确认 | enum=["storyboard.semantic_plan.v1"] | storyboard.semantic_plan.v1 |
| `profile_id` | enum／必填 | Controls shot rhythm and expression constraints；由用户选择并确认 | enum=["vertical-short-drama-v1", "dialogue-dense-v1", "manga-panel-v1", "ad-microdrama-v1"] | ad-microdrama-v1 |
| `revision_context_json` | string／必填 | Current redo scope and shot refs that must be preserved, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=524288 | {"mode":"new","preserve_shot_refs":[]} |
| `schema_version` | enum／必填 | Scaena input envelope version passed to the template；由用户选择并确认 | enum=["scaena.storyboard_prompt_input.v1"] | scaena.storyboard_prompt_input.v1 |
| `source_segments_json` | string／必填 | Current-episode script segments with stable segment_ref values, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=1048576 | [{"kind":"action","order":1,"segment_ref":"seg-a001","text":"宝宝刚睡着，厨房里的搅拌机突然启动。"},{"kind":"action","order":2,"segment_ref":"seg-a002","text":"妈妈冲向婴儿房门口。"},{"kind":"action","order":3,"segment_ref":"seg-a003","text":"门内的宝宝仍在熟睡。"},{"kind":"dialogue","order":4,"segment_ref":"seg-a004","speaker_ref":"character:mother","text":"原来它真的这么安静。"},{"kind":"action","order":5,"segment_ref":"seg-a005","text":"画面落到产品与“查看详情”按钮。"}] |
| `style_lens_summary` | string／必填 | Style-constraint summary without executable instructions；由用户选择并确认 | max_length=8192 | 先制造误会，再用可见结果和事实引用完成产品揭示。 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 ad-product-truth；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_story_context_refs_json": {
      "value": "[]",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_facts_json": {
      "value": "[{\"fact_ref\":\"fact:noise-test\",\"text\":\"本素材已确认产品运行时未惊醒隔壁房间内的宝宝。\"},{\"fact_ref\":\"fact:cta-view-details\",\"text\":\"允许使用 CTA 文案“查看详情”。\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.direction_json": {
      "value": "{\"aspect_ratio\":\"9:16\",\"cta_required\":true,\"duration_ms_max\":22000,\"duration_ms_min\":18000,\"shot_count_max\":5,\"shot_count_min\":5}",
      "kind": "user",
      "source": "user"
    },
    "main.episode_ref": {
      "value": "episode:ad-001",
      "kind": "user",
      "source": "user"
    },
    "main.known_entities_json": {
      "value": "[{\"kind\":\"character\",\"name\":\"妈妈\",\"ref\":\"character:mother\"},{\"kind\":\"character\",\"name\":\"宝宝\",\"ref\":\"character:baby\"},{\"kind\":\"product\",\"name\":\"静音搅拌机\",\"ref\":\"product:quiet-blender\"},{\"kind\":\"location\",\"name\":\"厨房\",\"ref\":\"location:kitchen\"},{\"kind\":\"location\",\"name\":\"婴儿房\",\"ref\":\"location:nursery\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "ad-microdrama-v1",
      "kind": "user",
      "source": "user"
    },
    "main.revision_context_json": {
      "value": "{\"mode\":\"new\",\"preserve_shot_refs\":[]}",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "scaena.storyboard_prompt_input.v1",
      "kind": "user",
      "source": "user"
    },
    "main.source_segments_json": {
      "value": "[{\"kind\":\"action\",\"order\":1,\"segment_ref\":\"seg-a001\",\"text\":\"宝宝刚睡着，厨房里的搅拌机突然启动。\"},{\"kind\":\"action\",\"order\":2,\"segment_ref\":\"seg-a002\",\"text\":\"妈妈冲向婴儿房门口。\"},{\"kind\":\"action\",\"order\":3,\"segment_ref\":\"seg-a003\",\"text\":\"门内的宝宝仍在熟睡。\"},{\"kind\":\"dialogue\",\"order\":4,\"segment_ref\":\"seg-a004\",\"speaker_ref\":\"character:mother\",\"text\":\"原来它真的这么安静。\"},{\"kind\":\"action\",\"order\":5,\"segment_ref\":\"seg-a005\",\"text\":\"画面落到产品与“查看详情”按钮。\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.style_lens_summary": {
      "value": "先制造误会，再用可见结果和事实引用完成产品揭示。",
      "kind": "user",
      "source": "user"
    },
    "main.locale": {
      "value": "en",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "storyboard.semantic_plan.v1",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_story_context_refs_json,main.continuity_facts_json,main.direction_json,main.episode_ref,main.known_entities_json,main.profile_id,main.revision_context_json,main.schema_version,main.source_segments_json,main.style_lens_summary,main.locale,main.output_schema_version --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：AI Drama Storyboard Breakdown。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/main.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `repair`

职责：Repair a reviewed storyboard while preserving source traceability.

精确引用：`promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en`；role：`repair`。
合同许可：`internal`；permissions：`inspect, preview, storyboard_handoff`。

<!-- guide:begin inputs repair -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/repair.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_story_context_refs_json` | string／必填 | Human-accepted story context references allowed for this run, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；首次从给定剧本创建分镜，没有已接受的长篇上下文引用；来源片段仍须提供。 | min_length=2；max_length=131072 | [] |
| `continuity_facts_json` | string／必填 | Continuity facts that shots may reference, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"fact_ref":"fact:key-on-table","text":"钥匙在第一镜被放到桌上，第二镜仍在原位。"}] |
| `direction_json` | string／必填 | Directorial objectives and hard constraints validated and serialized by Scaena；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"duration_ms_max":8000,"duration_ms_min":5000,"shot_count_max":2,"shot_count_min":2} |
| `episode_ref` | string／必填 | Stable reference for the current and only allowed episode；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=1；max_length=256 | episode:repair-001 |
| `known_entities_json` | string／必填 | Controlled character, location, and prop entities serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"kind":"character","name":"苏禾","ref":"character:su-he"},{"kind":"prop","name":"钥匙","ref":"prop:key"}] |
| `locale` | enum／必填 | Locale used by the template body and output text；由用户选择并确认 | enum=["en"] | en |
| `output_schema_version` | enum／必填 | Directorial semantic plan schema version the model must return；由用户选择并确认 | enum=["storyboard.semantic_plan.v1"] | storyboard.semantic_plan.v1 |
| `profile_id` | enum／必填 | Controls shot rhythm and expression constraints；由用户选择并确认 | enum=["vertical-short-drama-v1", "dialogue-dense-v1", "manga-panel-v1", "ad-microdrama-v1"] | dialogue-dense-v1 |
| `repair_findings_json` | string／必填 | Stable finding codes and targets allowed for this repair, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | [{"code":"DURATION_INVALID","message":"duration_ms must be positive","shot_key":"shot-01-02"}] |
| `schema_version` | enum／必填 | Scaena input envelope version passed to the template；由用户选择并确认 | enum=["scaena.storyboard_prompt_input.v1"] | scaena.storyboard_prompt_input.v1 |
| `semantic_plan_json` | string／必填 | Semantic plan parsed by Scaena that now requires bounded repair, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=1048576 | {"findings":[],"profile_id":"dialogue-dense-v1","review_summary":{"dialogue_spine":"一句话确认交接。","duration_contract":"第二镜时长无效。","story_spine":"苏禾交出钥匙。","visual_baseline":"钥匙保持在桌面。"},"scenes":[{"dramatic_purpose":"完成钥匙交接。","entity_mentions":["character:su-he","prop:key"],"heading":"内景·客厅·日","order":1,"scene_key":"scene-01","shots":[{"action_summary":"苏禾把钥匙放到桌上。","camera_angle":"top_down","camera_movement":"locked","continuity_notes":["钥匙位于桌面中央"],"dialogue_segment_refs":[],"dramatic_purpose":"建立交接物。","duration_ms":3000,"entity_mentions":["character:su-he","prop:key"],"fact_refs":["fact:key-on-table"],"image_instruction":"9:16 钥匙落在桌面中央。","negative_constraints":[],"order":1,"shot_key":"shot-01-01","shot_size":"insert","source_segment_refs":["seg-rp001"]},{"action_summary":"苏禾看向对方。","camera_angle":"eye_level","camera_movement":"locked","continuity_notes":["钥匙仍在桌面中央"],"dialogue_segment_refs":["seg-rp002"],"dialogue_summary":"苏禾说门从今天起归对方。","dramatic_purpose":"确认交接决定。","duration_ms":0,"entity_mentions":["character:su-he","prop:key"],"fact_refs":["fact:key-on-table"],"image_instruction":"9:16 苏禾中近景，桌面钥匙作为前景。","negative_constraints":["不新增对白"],"order":2,"shot_key":"shot-01-02","shot_size":"medium_close_up","source_segment_refs":["seg-rp002"]}],"source_segment_refs":["seg-rp001","seg-rp002"]}],"schema_version":"storyboard.semantic_plan.v1","unmapped_segment_refs":[]} |
| `source_segments_json` | string／必填 | Current-episode script segments with stable segment_ref values, serialized as JSON；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=1048576 | [{"kind":"action","order":1,"segment_ref":"seg-rp001","text":"苏禾把钥匙放到桌上。"},{"kind":"dialogue","order":2,"segment_ref":"seg-rp002","speaker_ref":"character:su-he","text":"门从今天起归你。"}] |
| `style_lens_summary` | string／必填 | Style-constraint summary without executable instructions；由用户选择并确认 | max_length=8192 | 保留第一镜，只修复第二镜时长。 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example repair -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'repair' --output 'repair-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'repair' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en' --role 'repair' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 bounded-duration-repair；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_story_context_refs_json": {
      "value": "[]",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_facts_json": {
      "value": "[{\"fact_ref\":\"fact:key-on-table\",\"text\":\"钥匙在第一镜被放到桌上，第二镜仍在原位。\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.direction_json": {
      "value": "{\"duration_ms_max\":8000,\"duration_ms_min\":5000,\"shot_count_max\":2,\"shot_count_min\":2}",
      "kind": "user",
      "source": "user"
    },
    "main.episode_ref": {
      "value": "episode:repair-001",
      "kind": "user",
      "source": "user"
    },
    "main.known_entities_json": {
      "value": "[{\"kind\":\"character\",\"name\":\"苏禾\",\"ref\":\"character:su-he\"},{\"kind\":\"prop\",\"name\":\"钥匙\",\"ref\":\"prop:key\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.profile_id": {
      "value": "dialogue-dense-v1",
      "kind": "user",
      "source": "user"
    },
    "main.repair_findings_json": {
      "value": "[{\"code\":\"DURATION_INVALID\",\"message\":\"duration_ms must be positive\",\"shot_key\":\"shot-01-02\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.schema_version": {
      "value": "scaena.storyboard_prompt_input.v1",
      "kind": "user",
      "source": "user"
    },
    "main.semantic_plan_json": {
      "value": "{\"findings\":[],\"profile_id\":\"dialogue-dense-v1\",\"review_summary\":{\"dialogue_spine\":\"一句话确认交接。\",\"duration_contract\":\"第二镜时长无效。\",\"story_spine\":\"苏禾交出钥匙。\",\"visual_baseline\":\"钥匙保持在桌面。\"},\"scenes\":[{\"dramatic_purpose\":\"完成钥匙交接。\",\"entity_mentions\":[\"character:su-he\",\"prop:key\"],\"heading\":\"内景·客厅·日\",\"order\":1,\"scene_key\":\"scene-01\",\"shots\":[{\"action_summary\":\"苏禾把钥匙放到桌上。\",\"camera_angle\":\"top_down\",\"camera_movement\":\"locked\",\"continuity_notes\":[\"钥匙位于桌面中央\"],\"dialogue_segment_refs\":[],\"dramatic_purpose\":\"建立交接物。\",\"duration_ms\":3000,\"entity_mentions\":[\"character:su-he\",\"prop:key\"],\"fact_refs\":[\"fact:key-on-table\"],\"image_instruction\":\"9:16 钥匙落在桌面中央。\",\"negative_constraints\":[],\"order\":1,\"shot_key\":\"shot-01-01\",\"shot_size\":\"insert\",\"source_segment_refs\":[\"seg-rp001\"]},{\"action_summary\":\"苏禾看向对方。\",\"camera_angle\":\"eye_level\",\"camera_movement\":\"locked\",\"continuity_notes\":[\"钥匙仍在桌面中央\"],\"dialogue_segment_refs\":[\"seg-rp002\"],\"dialogue_summary\":\"苏禾说门从今天起归对方。\",\"dramatic_purpose\":\"确认交接决定。\",\"duration_ms\":0,\"entity_mentions\":[\"character:su-he\",\"prop:key\"],\"fact_refs\":[\"fact:key-on-table\"],\"image_instruction\":\"9:16 苏禾中近景，桌面钥匙作为前景。\",\"negative_constraints\":[\"不新增对白\"],\"order\":2,\"shot_key\":\"shot-01-02\",\"shot_size\":\"medium_close_up\",\"source_segment_refs\":[\"seg-rp002\"]}],\"source_segment_refs\":[\"seg-rp001\",\"seg-rp002\"]}],\"schema_version\":\"storyboard.semantic_plan.v1\",\"unmapped_segment_refs\":[]}",
      "kind": "user",
      "source": "user"
    },
    "main.source_segments_json": {
      "value": "[{\"kind\":\"action\",\"order\":1,\"segment_ref\":\"seg-rp001\",\"text\":\"苏禾把钥匙放到桌上。\"},{\"kind\":\"dialogue\",\"order\":2,\"segment_ref\":\"seg-rp002\",\"speaker_ref\":\"character:su-he\",\"text\":\"门从今天起归你。\"}]",
      "kind": "user",
      "source": "user"
    },
    "main.style_lens_summary": {
      "value": "保留第一镜，只修复第二镜时长。",
      "kind": "user",
      "source": "user"
    },
    "main.locale": {
      "value": "en",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "storyboard.semantic_plan.v1",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_story_context_refs_json,main.continuity_facts_json,main.direction_json,main.episode_ref,main.known_entities_json,main.profile_id,main.repair_findings_json,main.schema_version,main.semantic_plan_json,main.source_segments_json,main.style_lens_summary,main.locale,main.output_schema_version --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en","role":"repair"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks repair -->
### 结果示例与检查

示例目标：Repair pass。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/repair.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

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
