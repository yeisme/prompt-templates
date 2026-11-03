<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI 做剧空场景背景资产：完整使用教程

生成零人物、完整不透明的可复用场景背景板

## 如何提出需求

适用目标：人物与背景分开生成和审阅，基础资产阶段不合成。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI 做剧空场景背景资产」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-drama-background-assets@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

clean-background-plate-v1 生成净背景方案；实际背景产物形成后，validate-background-plate-v1 才检查空间与连续性。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `clean-background-plate-v1`

职责：Create a subject-free background plate for shot composition.

精确引用：`promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en`；role：`clean-background-plate-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs clean-background-plate-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/clean-background-plate-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `activity_zone` | string／必填 | 后续人物可进入的无遮挡空间区域；由用户选择并确认 | min_length=1；max_length=8192 | 画面中央留出宽两米的净空，不摆放家具或悬挂物 |
| `aspect_ratio` | string／必填 | 输出画幅，例如16:9或9:16；由用户选择并确认 | min_length=1；max_length=8192 | 16:9 |
| `camera` | string／必填 | 镜头高度、方向、焦段感和透视关系；由用户选择并确认 | min_length=1；max_length=8192 | eye-level medium shot, 50 mm equivalent, fixed position south of the action axis |
| `lighting` | string／必填 | 主光源方向、强度、色温和环境光；由用户选择并确认 | min_length=1；max_length=8192 | 左前方柔和天光，右侧弱反射补光，阴影方向保持一致 |
| `location_anchor` | string／必填 | 建筑、空间结构、入口、主要表面与可复用锚点；由用户选择并确认 | min_length=1；max_length=8192 | 北侧木门、东侧石墙和中央地砖交点作为空间锚点 |
| `time_weather` | string／必填 | 时间、天气和空气状态；由用户选择并确认 | min_length=1；max_length=8192 | 阴天傍晚；地面干燥，无雨雪特效 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example clean-background-plate-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'clean-background-plate-v1' --output 'clean-background-plate-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'clean-background-plate-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'clean-background-plate-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.activity_zone": {
      "value": "画面中央留出宽两米的净空，不摆放家具或悬挂物",
      "kind": "user",
      "source": "user"
    },
    "main.aspect_ratio": {
      "value": "16:9",
      "kind": "user",
      "source": "user"
    },
    "main.camera": {
      "value": "eye-level medium shot, 50 mm equivalent, fixed position south of the action axis",
      "kind": "user",
      "source": "user"
    },
    "main.lighting": {
      "value": "左前方柔和天光，右侧弱反射补光，阴影方向保持一致",
      "kind": "user",
      "source": "user"
    },
    "main.location_anchor": {
      "value": "北侧木门、东侧石墙和中央地砖交点作为空间锚点",
      "kind": "user",
      "source": "user"
    },
    "main.time_weather": {
      "value": "阴天傍晚；地面干燥，无雨雪特效",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.activity_zone,main.aspect_ratio,main.camera,main.lighting,main.location_anchor,main.time_weather --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en","role":"clean-background-plate-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks clean-background-plate-v1 -->
### 结果示例与检查

示例目标：Clean background plate。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
合成内容示例（供理解输出方向，未运行模型）：镜头方案候选：0–8 秒进入阅读角，8–20 秒翻书并展示环境，20–30 秒停留灯下。声音和身份连续性需逐镜核对；没有实际视频产物。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。

<!-- guide:end -->
## 角色 `validate-background-plate-v1`

职责：Review a background plate for isolation and reuse.

精确引用：`promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en`；role：`validate-background-plate-v1`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs validate-background-plate-v1 -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/validate-background-plate-v1.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `authoring_json` | string／必填 | 待校验的地点、机位、时间天气、光线、画幅、活动区和禁止项；由对应上游/领域 owner 提供 JSON 文本；按本角色案例与语义合同填写；案例提供有来源的合成业务数据；真实使用由对应 owner 检查语义与引用，不将编译成功当成领域接受。 | min_length=2；max_length=262144 | {"activity_zone":"画面右下至桥前保留无遮挡活动区","aspect_ratio":"16:9","camera":"河岸平视广角，镜头朝向石桥，弱透视","lighting":"左后方冷色天光，桥下柔和环境光","location_anchor":"古镇石桥与河岸台阶，桥洞和远端牌楼位置固定","profile_id":"clean-background-plate-v1","requested_elements":["empty street","unoccupied boat"],"subject_count":0,"time_weather":"清晨薄雾，无雨","transparent_required":false} |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example validate-background-plate-v1 -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'validate-background-plate-v1' --output 'validate-background-plate-v1-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'validate-background-plate-v1' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en' --role 'validate-background-plate-v1' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 clean-background-valid；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.authoring_json": {
      "value": "{\"activity_zone\":\"画面右下至桥前保留无遮挡活动区\",\"aspect_ratio\":\"16:9\",\"camera\":\"河岸平视广角，镜头朝向石桥，弱透视\",\"lighting\":\"左后方冷色天光，桥下柔和环境光\",\"location_anchor\":\"古镇石桥与河岸台阶，桥洞和远端牌楼位置固定\",\"profile_id\":\"clean-background-plate-v1\",\"requested_elements\":[\"empty street\",\"unoccupied boat\"],\"subject_count\":0,\"time_weather\":\"清晨薄雾，无雨\",\"transparent_required\":false}",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.authoring_json --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-background-assets@1.0.0?locale=en","role":"validate-background-plate-v1"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks validate-background-plate-v1 -->
### 结果示例与检查

示例目标：Background plate review。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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
