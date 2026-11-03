<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# Auctra 创作分镜计划：完整使用教程

从已接受的导演场景计划投影编译单集创作分镜计划候选，映射到 auctra.storyboard_plan.v1

## 如何提出需求

适用目标：用于 Auctra 创作分镜主生成与有界修复；不生成生产候选。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「Auctra 创作分镜计划」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/auctra-creative-storyboard-plan@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Compile one episode creative storyboard plan candidate from an accepted auctra.director_scene_plan.v1 projection, mapping to auctra.storyboard_plan.v1

精确引用：`promptrepo://official/video/auctra-creative-storyboard-plan@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`inspect, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `accepted_source_refs_json` | string／必填 | beat/shot source_refs 唯一可引用的来源 ref 全集，JSON 序列化；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"refs":["scene:01","beat:01-a","beat:01-b","dialogue:01-05"]} |
| `continuity_refs_json` | string／必填 | 允许引用的人物、服装、道具、场地 refs，JSON 序列化；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"characters":["character:lin","character:zhao"],"wardrobe":["wardrobe:lin-suit-01"],"props":["prop:contract-paper"],"locations":["location:office-night"]} |
| `director_scene_plan_json` | string／必填 | 已接受的导演场景计划投影：场景主旨、拓扑、走位、镜头语法、声音策略；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"schema_version":"auctra.director_scene_plan.v1","plan_ref":"director-plan:ep01","episode":1,"scene_thesis":"Lin forces Zhao to sign away the factory under the guise of a toast","topology":{"zone_refs":["zone:desk","zone:door"],"axis_line":"desk-window"},"blocking":[{"beat_ref":"beat:01-a","zone_ref":"zone:desk","who_does":"Lin slides the contract across"}],"camera":{"grammar":"shot/reverse","cut_motivation":"power shifts per line"},"sound":{"strategy":"room tone only, no score"}} |
| `episode_ref` | string／必填 | 当前唯一允许的集数稳定 ref；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$ | episode:01 |
| `format_profile` | enum／必填 | 约束镜头预算与节奏的 Auctra 格式 profile；由用户选择并确认 | enum=["vertical-short-drama", "manga-drama"] | vertical-short-drama |
| `output_schema_version` | enum／必填 | 本模板锁定的语义输出 Schema；由用户选择并确认 | enum=["auctra-storyboard-plan-output-v1"] | auctra-storyboard-plan-output-v1 |
| `scene_contract_json` | string／必填 | 与本集计划相关的场景合同投影；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=131072 | {"scene_contract_ref":"scene-contract:01","entry":"Lin composed, Zhao cornered","goal":"Lin secures the signature","exit":"Zhao signs; Lin pockets the pen"} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/auctra-creative-storyboard-plan@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/auctra-creative-storyboard-plan@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/auctra-creative-storyboard-plan@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-ep01-confrontation；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.accepted_source_refs_json": {
      "value": "{\"refs\":[\"scene:01\",\"beat:01-a\",\"beat:01-b\",\"dialogue:01-05\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.continuity_refs_json": {
      "value": "{\"characters\":[\"character:lin\",\"character:zhao\"],\"wardrobe\":[\"wardrobe:lin-suit-01\"],\"props\":[\"prop:contract-paper\"],\"locations\":[\"location:office-night\"]}",
      "kind": "user",
      "source": "user"
    },
    "main.director_scene_plan_json": {
      "value": "{\"schema_version\":\"auctra.director_scene_plan.v1\",\"plan_ref\":\"director-plan:ep01\",\"episode\":1,\"scene_thesis\":\"Lin forces Zhao to sign away the factory under the guise of a toast\",\"topology\":{\"zone_refs\":[\"zone:desk\",\"zone:door\"],\"axis_line\":\"desk-window\"},\"blocking\":[{\"beat_ref\":\"beat:01-a\",\"zone_ref\":\"zone:desk\",\"who_does\":\"Lin slides the contract across\"}],\"camera\":{\"grammar\":\"shot/reverse\",\"cut_motivation\":\"power shifts per line\"},\"sound\":{\"strategy\":\"room tone only, no score\"}}",
      "kind": "user",
      "source": "user"
    },
    "main.episode_ref": {
      "value": "episode:01",
      "kind": "user",
      "source": "user"
    },
    "main.format_profile": {
      "value": "vertical-short-drama",
      "kind": "user",
      "source": "user"
    },
    "main.output_schema_version": {
      "value": "auctra-storyboard-plan-output-v1",
      "kind": "user",
      "source": "user"
    },
    "main.scene_contract_json": {
      "value": "{\"scene_contract_ref\":\"scene-contract:01\",\"entry\":\"Lin composed, Zhao cornered\",\"goal\":\"Lin secures the signature\",\"exit\":\"Zhao signs; Lin pockets the pen\"}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.accepted_source_refs_json,main.continuity_refs_json,main.director_scene_plan_json,main.episode_ref,main.format_profile,main.output_schema_version,main.scene_contract_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/auctra-creative-storyboard-plan@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Auctra creative storyboard plan。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
输出结构示例见 [invalid-forbidden-field.output](../fixtures/main.en/invalid-forbidden-field.output.json)、[invalid-unknown-source-ref.output](../fixtures/main.en/invalid-unknown-source-ref.output.json)、[valid-ep01-confrontation.output](../fixtures/main.en/valid-ep01-confrontation.output.json)。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/main.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

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

声明的消费者：auctra。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->

## 原有专项说明

# auctra-creative-storyboard-plan

Auctra 创作分镜（creative storyboard）主生成模板：从已接受的
`auctra.director_scene_plan.v1` 投影编译单集 beats/shots 计划候选，输出映射到
`auctra.storyboard_plan.v1`（编译合同见 `contracts/compilers/auctra.storyboard_plan.v1.json`）。

- Owner：模板正文归本仓；canonical 分镜计划、review、acceptance 归 Auctra（consumer）。
- 与 `ai-drama-storyboard-breakdown`（Scaena production storyboard）边界不同：本 solution 只服务
  Auctra 创作分镜链路（DirectorScenePlan → StoryboardPlan），不生成生产候选。
- 编译 locale 只有 `en`；`template-zh-CN.md` 是人工审阅译文，不注册、不参与 catalog/digest。
- 本方案 1.0.0 尚未发布 release/digest；消费方解析在 release 存在前保持 `unavailable`，不得以
  Scaena 模板替代。
