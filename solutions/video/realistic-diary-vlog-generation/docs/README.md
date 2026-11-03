<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# Realistic Diary Vlog Generation：完整使用教程

Compile subject, selfie/follow camera formats, on-camera dialogue with lip sync, acoustic-space continuity, and realism constraints into a diary vlog prompt for direct video-model delivery

## 如何提出需求

适用目标：Use for on-camera-dialogue day-diary realistic video generation and human review; complements the VO-driven realistic-docu-vlog-generation and ambience-only realistic-vlog-shot-generation。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「Realistic Diary Vlog Generation」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/realistic-diary-vlog-generation@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Compile subject, selfie/follow camera formats, on-camera dialogue with lip sync, acoustic-space continuity, and realism constraints into a diary vlog prompt for direct video-model delivery

精确引用：`promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, inspect, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `ambience_design` | string／必填 | 各地点的现场声与 room tone；声学空间随地点真实变化；由用户选择并确认 | min_length=10；max_length=4096 | 卧室近距安静、街道开阔混响、排练室反射声；room tone 全程存在 |
| `aspect_ratio` | enum／可选 | 输出视频画幅；由用户选择并确认 | enum=["16:9", "9:16", "1:1"]；default=16:9 | 16:9 |
| `audio_exclusions` | string／必填 | 禁止的声音元素；由用户选择并确认 | min_length=4；max_length=2048 | 无配乐、无音效堆砌、无字幕配音 |
| `camera_exclusions` | string／必填 | 禁止的拍摄手法；由用户选择并确认 | min_length=4；max_length=2048 | 无商业摆拍、glamour 广告打光、稳定器与不可能的机位 |
| `camera_formats` | string／必填 | 全片允许的拍摄格式集合，如自拍、朋友手持跟拍、固定机位；由用户选择并确认 | min_length=10；max_length=4096 | 手持自拍 + 亲密朋友手持跟拍 + 自然固定机位 |
| `camera_imperfections` | string／必填 | 必须保留的真实拍摄瑕疵；由用户选择并确认 | min_length=10；max_length=4096 | 手持晃动、小幅失焦、普通室内光、自然停顿 |
| `character_ref` | string／可选 | 已登记人物资产的 @ 引用，支持 @uuid 与 @image1 位置引用；有资产时必填；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=0；max_length=256 | @image1 |
| `consistency_lock` | string／必填 | 全片不可放宽的面部/发型/体型/性格锁定声明；由用户选择并确认 | min_length=10；max_length=2048 | 全片保持完全一致的面部、发型、体型与性格气质 |
| `dialogue_language` | string／必填 | 台词使用的自然语言与语感要求；由用户选择并确认 | min_length=2；max_length=128 | 自然日语口语 |
| `dialogue_script` | string／必填 | 逐句出镜台词与节拍绑定键；渲染后逐字保留；由用户选择并确认 | min_length=10；max_length=16384 | 林舟：“这封信还没有寄出去。”顾遥：“先看看地址是否仍然存在。” |
| `duration_s` | integer／必填 | 视频总时长，时间线必须连续覆盖；由用户选择并确认 | min=5；max=120；default=60 | 60 |
| `ending_directive` | string／必填 | 结尾执行方式；由用户选择并确认 | min_length=4；max_length=2048 | 安静的夜间道别，录制自然结束 |
| `final_feel` | string／必填 | 成片整体气质声明；由用户选择并确认 | min_length=10；max_length=2048 | 克制、平静，保留日常行为的节奏与细节 |
| `footage_style` | string／必填 | 整体影像气质声明；由用户选择并确认 | min_length=4；max_length=2048 | photorealistic personal vlog |
| `negative_prompts` | string／必填 | 负面约束清单；模板内置默认负面项会并入；由用户选择并确认 | min_length=10；max_length=8192 | 不出现商标、额外人物或未提供的事实 |
| `provider_banner` | string／可选 | 可选的投递平台标识行，渲染在 Prompt 顶部；留空则省略；由用户选择并确认 | min_length=0；max_length=256 | Made with Seedance 2.5 |
| `realism_rules` | string／必填 | 解剖、唇形同步、物理、光影等写实要求；由用户选择并确认 | min_length=10；max_length=4096 | 自然遮挡、真实接触和连续光照；禁止瞬移、额外手指和无来源物件 |
| `resolution` | enum／可选 | 输出视频分辨率；由用户选择并确认 | enum=["720p", "1080p", "4K"]；default=1080p | 1080p |
| `scenario_summary` | string／必填 | 一句话说明谁记录怎样的一天；由用户选择并确认 | min_length=10；max_length=2048 | 成年访客走进虚构阅读角，翻开书，停在窗边灯光下 |
| `story_beats` | string／必填 | 按节拍结构编写的时间线，每拍含地点/声学空间、机位与台词绑定键；由用户选择并确认 | min_length=10；max_length=65536 | 入场观察，发现未寄出的信，核对旧地址，保留去向未知的结尾 |
| `subject_identity` | string／必填 | 面部、发型、年龄感、性格气质等特征；由用户选择并确认 | min_length=10；max_length=4096 | 成年访客林舟，短黑发、深蓝外套、左腕布绳，所有镜头保持一致 |
| `wardrobe_and_accessories` | string／必填 | 一天内合理的换装链条与配饰清单；换装须有日记事件支撑；由用户选择并确认 | min_length=4；max_length=4096 | 深蓝外套、米色内搭、左腕布绳；无商标，不在镜头间变化 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.ambience_design": {
      "value": "卧室近距安静、街道开阔混响、排练室反射声；room tone 全程存在",
      "kind": "user",
      "source": "user"
    },
    "main.aspect_ratio": {
      "value": "16:9",
      "kind": "user",
      "source": "user"
    },
    "main.audio_exclusions": {
      "value": "无配乐、无音效堆砌、无字幕配音",
      "kind": "user",
      "source": "user"
    },
    "main.camera_exclusions": {
      "value": "无商业摆拍、glamour 广告打光、稳定器与不可能的机位",
      "kind": "user",
      "source": "user"
    },
    "main.camera_formats": {
      "value": "手持自拍 + 亲密朋友手持跟拍 + 自然固定机位",
      "kind": "user",
      "source": "user"
    },
    "main.camera_imperfections": {
      "value": "手持晃动、小幅失焦、普通室内光、自然停顿",
      "kind": "user",
      "source": "user"
    },
    "main.character_ref": {
      "value": "@image1",
      "kind": "user",
      "source": "user"
    },
    "main.consistency_lock": {
      "value": "全片保持完全一致的面部、发型、体型与性格气质",
      "kind": "user",
      "source": "user"
    },
    "main.dialogue_language": {
      "value": "自然日语口语",
      "kind": "user",
      "source": "user"
    },
    "main.dialogue_script": {
      "value": "林舟：“这封信还没有寄出去。”顾遥：“先看看地址是否仍然存在。”",
      "kind": "user",
      "source": "user"
    },
    "main.duration_s": {
      "value": 60,
      "kind": "user",
      "source": "user"
    },
    "main.ending_directive": {
      "value": "安静的夜间道别，录制自然结束",
      "kind": "user",
      "source": "user"
    },
    "main.final_feel": {
      "value": "克制、平静，保留日常行为的节奏与细节",
      "kind": "user",
      "source": "user"
    },
    "main.footage_style": {
      "value": "photorealistic personal vlog",
      "kind": "user",
      "source": "user"
    },
    "main.negative_prompts": {
      "value": "不出现商标、额外人物或未提供的事实",
      "kind": "user",
      "source": "user"
    },
    "main.provider_banner": {
      "value": "Made with Seedance 2.5",
      "kind": "user",
      "source": "user"
    },
    "main.realism_rules": {
      "value": "自然遮挡、真实接触和连续光照；禁止瞬移、额外手指和无来源物件",
      "kind": "user",
      "source": "user"
    },
    "main.resolution": {
      "value": "1080p",
      "kind": "user",
      "source": "user"
    },
    "main.scenario_summary": {
      "value": "成年访客走进虚构阅读角，翻开书，停在窗边灯光下",
      "kind": "user",
      "source": "user"
    },
    "main.story_beats": {
      "value": "入场观察，发现未寄出的信，核对旧地址，保留去向未知的结尾",
      "kind": "user",
      "source": "user"
    },
    "main.subject_identity": {
      "value": "成年访客林舟，短黑发、深蓝外套、左腕布绳，所有镜头保持一致",
      "kind": "user",
      "source": "user"
    },
    "main.wardrobe_and_accessories": {
      "value": "深蓝外套、米色内搭、左腕布绳；无商标，不在镜头间变化",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.ambience_design,main.aspect_ratio,main.audio_exclusions,main.camera_exclusions,main.camera_formats,main.camera_imperfections,main.character_ref,main.consistency_lock,main.dialogue_language,main.dialogue_script,main.duration_s,main.ending_directive,main.final_feel,main.footage_style,main.negative_prompts,main.provider_banner,main.realism_rules,main.resolution,main.scenario_summary,main.story_beats,main.subject_identity,main.wardrobe_and_accessories --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Realistic Diary Vlog Generation。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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
