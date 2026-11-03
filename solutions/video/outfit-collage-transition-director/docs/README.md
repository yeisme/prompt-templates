<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 穿搭拼贴首帧 + 卡点换装视频导演：完整使用教程

把人物锚点与造型清单编译为联动制作包：拼贴首帧图提示词、逐段换装视频时间轴、精简视频提示词与负面约束

## 如何提出需求

适用目标：用于同一角色多套穿搭拼贴首帧与卡点换装短视频；改写自导入的 female-outfit-director skill。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「穿搭拼贴首帧 + 卡点换装视频导演」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/outfit-collage-transition-director@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Compile character anchors and outfit lists into a linked package: collage first-frame image prompt, per-segment transition video timeline, compact video prompt, and negative constraints

精确引用：`promptrepo://official/video/outfit-collage-transition-director@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, inspect, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `beat_times` | string／可选 | 换装点时间序列；留空时按默认点等比例缩放；由用户选择并确认 | min_length=0；max_length=1024 | 1.25s, 2.95s, 4.40s, 6.55s |
| `camera_rule` | string／可选 | 留空用默认固定高机位；可要求正面固定、轻低机位、缓慢推近、轻横移或半环绕；由用户选择并确认 | min_length=0；max_length=2048 | 保持同一成年人物的面部比例和眼平机位，换装时不改变空间位置 |
| `character_anchors` | string／可选 | 角色名称、成年年龄感、族裔外观、脸型五官、肤色、妆容、发型发色、头饰耳饰、气质；留空且无参考图时用默认原创中国成年女性；由用户选择并确认 | min_length=0；max_length=4096 | 短黑发、椭圆脸、左腕布绳；不对应真人 |
| `collage_layout` | string／可选 | 留空时用默认五人拼贴版式；3-6 套造型需说明新布局逻辑；由用户选择并确认 | min_length=0；max_length=4096 | 三列等宽拼贴，同一机位，第一列深蓝外套、第二列灰色针织、第三列米色衬衫 |
| `ending_action` | string／可选 | 视频收尾动作；留空时保留最终造型展示；由用户选择并确认 | min_length=0；max_length=2048 | 人物整理袖口后自然停住，画面留出两秒稳定尾帧 |
| `image_aspect` | enum／可选 | 首帧拼贴图画幅；由用户选择并确认 | enum=["9:16", "16:9", "1:1", "3:4"]；default=9:16 | 9:16 |
| `image_style` | string／可选 | 背景、光线、主色系、小人物描边；留空用影棚默认值；由用户选择并确认 | min_length=0；max_length=4096 | 均匀柔光、写实布料、低饱和背景、清楚的轮廓 |
| `motion_tone` | string／可选 | 人物动作与表演基调；由用户选择并确认 | min_length=0；max_length=2048 | 轻柔、含蓄、优雅 |
| `outfit_list` | string／可选 | 初始主造型 + 4 套换装造型；留空时按风格方向推导；由用户选择并确认 | min_length=0；max_length=8192 | 深蓝外套与米色内搭；灰色针织与深色裤；米色衬衫与棕色裤 |
| `reference_image_ref` | string／可选 | 可选；已登记参考图的 @ 引用，提供时从中提取人物与版式；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=0；max_length=256 | @image1 |
| `sound_design` | string／可选 | 默认无 BGM，只保留机制音效；指定音乐时按要求编排；由用户选择并确认 | min_length=0；max_length=2048 | 换装节拍使用合成轻拍声，保留衣料摩擦，无音乐版权素材 |
| `style_direction` | string／可选 | 整体风格走向，用于补全造型与机制选择；由用户选择并确认 | min_length=0；max_length=2048 | 清冷汉服贵女 |
| `transition_mechanism` | enum／可选 | M1-M12 机制库之一；auto 时按风格映射选择并说明；由用户选择并确认 | enum=["auto", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"]；default=auto | auto |
| `video_aspect` | enum／可选 | 换装视频画幅；由用户选择并确认 | enum=["9:16", "16:9", "1:1"]；default=9:16 | 9:16 |
| `video_duration_s` | integer／必填 | 换装视频总时长；由用户选择并确认 | min=4；max=60；default=8 | 8 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/outfit-collage-transition-director@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/outfit-collage-transition-director@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/outfit-collage-transition-director@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.beat_times": {
      "value": "1.25s, 2.95s, 4.40s, 6.55s",
      "kind": "user",
      "source": "user"
    },
    "main.camera_rule": {
      "value": "保持同一成年人物的面部比例和眼平机位，换装时不改变空间位置",
      "kind": "user",
      "source": "user"
    },
    "main.character_anchors": {
      "value": "短黑发、椭圆脸、左腕布绳；不对应真人",
      "kind": "user",
      "source": "user"
    },
    "main.collage_layout": {
      "value": "三列等宽拼贴，同一机位，第一列深蓝外套、第二列灰色针织、第三列米色衬衫",
      "kind": "user",
      "source": "user"
    },
    "main.ending_action": {
      "value": "人物整理袖口后自然停住，画面留出两秒稳定尾帧",
      "kind": "user",
      "source": "user"
    },
    "main.image_aspect": {
      "value": "9:16",
      "kind": "user",
      "source": "user"
    },
    "main.image_style": {
      "value": "均匀柔光、写实布料、低饱和背景、清楚的轮廓",
      "kind": "user",
      "source": "user"
    },
    "main.motion_tone": {
      "value": "轻柔、含蓄、优雅",
      "kind": "user",
      "source": "user"
    },
    "main.outfit_list": {
      "value": "深蓝外套与米色内搭；灰色针织与深色裤；米色衬衫与棕色裤",
      "kind": "user",
      "source": "user"
    },
    "main.reference_image_ref": {
      "value": "@image1",
      "kind": "user",
      "source": "user"
    },
    "main.sound_design": {
      "value": "换装节拍使用合成轻拍声，保留衣料摩擦，无音乐版权素材",
      "kind": "user",
      "source": "user"
    },
    "main.style_direction": {
      "value": "清冷汉服贵女",
      "kind": "user",
      "source": "user"
    },
    "main.transition_mechanism": {
      "value": "auto",
      "kind": "user",
      "source": "user"
    },
    "main.video_aspect": {
      "value": "9:16",
      "kind": "user",
      "source": "user"
    },
    "main.video_duration_s": {
      "value": 8,
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.beat_times,main.camera_rule,main.character_anchors,main.collage_layout,main.ending_action,main.image_aspect,main.image_style,main.motion_tone,main.outfit_list,main.reference_image_ref,main.sound_design,main.style_direction,main.transition_mechanism,main.video_aspect,main.video_duration_s --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/outfit-collage-transition-director@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Outfit Collage + Beat-Synced Transition Video Director。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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

# outfit-collage-transition-director

同一角色多套穿搭拼贴首帧 + 卡点换装短视频的导演工作流模板。

- 编译模板（Agent/模型消费）：`../prompts/main.en.md`
- 中文阅读版（人工审阅，不进编译）：`template-zh-CN.md`
- 使用指南：`usage.zh-CN.md`
- 评审清单：`review-checklist.zh-CN.md`
- 已知失败模式：`failure-modes.zh-CN.md`
- 绑定实例：`../examples/hanfu-collage-m1.zh-CN.md`

上游来源：第三方 Skill `female-outfit-director`（仓库 `liyue-aigc/female-outfit-director@2d30d40`，仅作为改写来源引用，未导入本仓库 skills 体系）。
