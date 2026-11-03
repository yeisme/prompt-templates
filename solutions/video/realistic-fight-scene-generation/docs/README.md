<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# Realistic Fight Scene Generation：完整使用教程

Compile dual-character identity lock, fight physics, axis of action, ACT follow camera, and per-beat choreography into a fight-scene prompt for direct video-model delivery

## 如何提出需求

适用目标：Use for VFX-free physics-first two-person fight scenes with human review; complements the VFX-driven ai-drama-shot-video-generation。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「Realistic Fight Scene Generation」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/realistic-fight-scene-generation@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Compile dual-character identity lock, fight physics, axis of action, ACT follow camera, and per-beat choreography into a fight-scene prompt for direct video-model delivery

精确引用：`promptrepo://official/video/realistic-fight-scene-generation@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, inspect, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `action_principles` | string／必填 | 动作组成与技术库（拳肘膝踢、擒拿、摔法等）；由用户选择并确认 | min_length=10；max_length=8192 | 现代实战拳法、肘击、膝撞、低位踢击、近身控制、擒拿拆解和短距离摔法 |
| `antagonist_identity` | string／必填 | 敌人的面部、年龄、发型、体型、服装、气质描述；由用户选择并确认 | min_length=10；max_length=4096 | 虚构成年对手，灰色训练服，使用软质练习刀，无真人对应 |
| `antagonist_ref` | string／必填 | 敌人参考图资产的 @ 引用，不得与主角引用相同；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=2；max_length=256 | @image2 |
| `aspect_ratio` | enum／可选 | 输出视频画幅；由用户选择并确认 | enum=["16:9", "9:16", "1:1", "2.39:1"]；default=16:9 | 16:9 |
| `audio_design` | string／必填 | 严格同步画面的现场声清单；默认无对白、音乐仅极克制低频脉冲；由用户选择并确认 | min_length=10；max_length=4096 | 脚步、翻页和室内底噪；没有未经授权音乐或真实人物声音 |
| `camera_follow_spec` | string／必填 | 主角中心机位集合与关键命中景别规则；由用户选择并确认 | min_length=10；max_length=4096 | 肩后、腰后、侧后第三人称跟随；关键格挡和重击短暂切入侧面中景或近景 |
| `camera_motion_rules` | string／必填 | 摄影机重量感、撞击震动与关键清晰度规则；由用户选择并确认 | min_length=10；max_length=4096 | 缓慢跟随主体，保持视线方向和接触点，不越过动作轴线 |
| `character_dynamics` | string／必填 | 双方的格斗风格与性格差异；由用户选择并确认 | min_length=10；max_length=4096 | 主角冷静精准动作幅度小、格挡后即反击；敌人力量更大、连续压迫与贴身撞击 |
| `cut_rules` | string／必填 | 切镜手段白名单与切镜后必须延续的状态；由用户选择并确认 | min_length=10；max_length=4096 | 优先连续动作；切镜保持人物位置、运动方向和道具握持一致 |
| `dual_consistency_lock` | string／必填 | 不交换身份/不变脸/不改服装体型/无第三者的锁定声明；由用户选择并确认 | min_length=10；max_length=2048 | 严格继承参考图两人的面部、体型、服装与气质，全程不得交换身份 |
| `duration_s` | integer／必填 | 视频总时长，格斗时间线必须连续覆盖；由用户选择并确认 | min=5；max=120；default=30 | 30 |
| `ending_directive` | string／必填 | 结尾执行方式；由用户选择并确认 | min_length=4；max_length=2048 | 最后一帧保持双方继续互相锁定的危险状态，为下一段战斗留下衔接 |
| `environment_interaction` | string／必填 | 环境物件参与战斗的方式与损毁边界；由用户选择并确认 | min_length=10；max_length=4096 | 立柱、闸机、玻璃护栏、积水参与战斗；闸机挡板可撞开弯曲但不脱离，玻璃震颤不碎，立柱不碎裂 |
| `fight_arc` | string／必填 | 整场格斗的阶段弧线与双方攻守平衡要求；由用户选择并确认 | min_length=10；max_length=4096 | 敌人抢攻→主角反击→绕柱追击→主角失势→危险拆解→夺回主动→环境摔投→最终反制；主角必须经历一次明显失势和一次危险化解 |
| `fight_beats` | string／必填 | 逐拍攻防编排：时间区间、机位、起点/路径/接触点/结果、隐形切点、惯性延续；由用户选择并确认 | min_length=10；max_length=131072 | 0–3 秒站位试探；3–7 秒一次格挡；7–10 秒退步拉开距离；没有伤口特写 |
| `final_feel` | string／必填 | 成片整体气质声明；由用户选择并确认 | min_length=10；max_length=2048 | 刺激而不混乱，凶狠但遵守人体力学，摄影机始终以主角为核心 |
| `footage_style` | string／必填 | 整体影像气质声明；由用户选择并确认 | min_length=4；max_length=2048 | 写实电影级实拍质感 |
| `frame_rate` | enum／可选 | 输出视频帧率；由用户选择并确认 | enum=["24fps", "25fps", "30fps", "50fps", "60fps"]；default=24fps | 24fps |
| `lighting_palette` | string／必填 | 主光、轮廓光、主色调与材质要求；由用户选择并确认 | min_length=10；max_length=4096 | 冷白顶灯主光（两盏偶尔闪烁），红色警示灯局部轮廓光，冷蓝灰主色 |
| `negative_prompts` | string／必填 | 负面约束清单；模板内置默认负面项会并入；由用户选择并确认 | min_length=10；max_length=8192 | 不出现商标、额外人物或未提供的事实 |
| `protagonist_identity` | string／必填 | 主角的面部、年龄、发型、体型、服装、气质描述；由用户选择并确认 | min_length=10；max_length=4096 | 虚构成年训练者林舟，深蓝训练服，使用软质练习刀 |
| `protagonist_ref` | string／必填 | 主角参考图资产的 @ 引用，不得与敌人引用相同；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=2；max_length=256 | @image1 |
| `provider_banner` | string／可选 | 可选的投递平台标识行，渲染在 Prompt 顶部；留空则省略；由用户选择并确认 | min_length=0；max_length=256 | Made with Seedance 2.5 |
| `realism_rules` | string／必填 | 皮肤、肌肉、衣料、材质、光影等写实要求；由用户选择并确认 | min_length=10；max_length=4096 | 自然遮挡、真实接触和连续光照；禁止瞬移、额外手指和无来源物件 |
| `resolution` | enum／可选 | 输出视频分辨率；由用户选择并确认 | enum=["720p", "1080p", "4K"]；default=1080p | 1080p |
| `scenario_summary` | string／必填 | 一句话说明谁与谁在何处对战；由用户选择并确认 | min_length=10；max_length=2048 | 成年访客走进虚构阅读角，翻开书，停在窗边灯光下 |
| `scene_desc` | string／必填 | 格斗场景的环境、材质与氛围细节；由用户选择并确认 | min_length=10；max_length=8192 | 虚构训练庭院，平整地面、石墙和一个木门，无围观人群 |
| `scene_layout` | string／必填 | 开场站位、战斗移动路径、关键地物位置与行动轴线规则；由用户选择并确认 | min_length=10；max_length=8192 | 两人相距两米沿东西轴站立，木门位于北侧，镜头留在南侧 |
| `style_reference` | string／必填 | 只继承气质与镜头语言的参照描述，不得照搬人物/场景/镜头；来自已提供资料或已接受引用；合成引用不可当成真实资产 | min_length=10；max_length=4096 | 现代硬派武术电影气质 + ACT 动作游戏第三人称战斗镜头 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/realistic-fight-scene-generation@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/realistic-fight-scene-generation@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/realistic-fight-scene-generation@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.action_principles": {
      "value": "现代实战拳法、肘击、膝撞、低位踢击、近身控制、擒拿拆解和短距离摔法",
      "kind": "user",
      "source": "user"
    },
    "main.antagonist_identity": {
      "value": "虚构成年对手，灰色训练服，使用软质练习刀，无真人对应",
      "kind": "user",
      "source": "user"
    },
    "main.antagonist_ref": {
      "value": "@image2",
      "kind": "user",
      "source": "user"
    },
    "main.aspect_ratio": {
      "value": "16:9",
      "kind": "user",
      "source": "user"
    },
    "main.audio_design": {
      "value": "脚步、翻页和室内底噪；没有未经授权音乐或真实人物声音",
      "kind": "user",
      "source": "user"
    },
    "main.camera_follow_spec": {
      "value": "肩后、腰后、侧后第三人称跟随；关键格挡和重击短暂切入侧面中景或近景",
      "kind": "user",
      "source": "user"
    },
    "main.camera_motion_rules": {
      "value": "缓慢跟随主体，保持视线方向和接触点，不越过动作轴线",
      "kind": "user",
      "source": "user"
    },
    "main.character_dynamics": {
      "value": "主角冷静精准动作幅度小、格挡后即反击；敌人力量更大、连续压迫与贴身撞击",
      "kind": "user",
      "source": "user"
    },
    "main.cut_rules": {
      "value": "优先连续动作；切镜保持人物位置、运动方向和道具握持一致",
      "kind": "user",
      "source": "user"
    },
    "main.dual_consistency_lock": {
      "value": "严格继承参考图两人的面部、体型、服装与气质，全程不得交换身份",
      "kind": "user",
      "source": "user"
    },
    "main.duration_s": {
      "value": 30,
      "kind": "user",
      "source": "user"
    },
    "main.ending_directive": {
      "value": "最后一帧保持双方继续互相锁定的危险状态，为下一段战斗留下衔接",
      "kind": "user",
      "source": "user"
    },
    "main.environment_interaction": {
      "value": "立柱、闸机、玻璃护栏、积水参与战斗；闸机挡板可撞开弯曲但不脱离，玻璃震颤不碎，立柱不碎裂",
      "kind": "user",
      "source": "user"
    },
    "main.fight_arc": {
      "value": "敌人抢攻→主角反击→绕柱追击→主角失势→危险拆解→夺回主动→环境摔投→最终反制；主角必须经历一次明显失势和一次危险化解",
      "kind": "user",
      "source": "user"
    },
    "main.fight_beats": {
      "value": "0–3 秒站位试探；3–7 秒一次格挡；7–10 秒退步拉开距离；没有伤口特写",
      "kind": "user",
      "source": "user"
    },
    "main.final_feel": {
      "value": "刺激而不混乱，凶狠但遵守人体力学，摄影机始终以主角为核心",
      "kind": "user",
      "source": "user"
    },
    "main.footage_style": {
      "value": "写实电影级实拍质感",
      "kind": "user",
      "source": "user"
    },
    "main.frame_rate": {
      "value": "24fps",
      "kind": "user",
      "source": "user"
    },
    "main.lighting_palette": {
      "value": "冷白顶灯主光（两盏偶尔闪烁），红色警示灯局部轮廓光，冷蓝灰主色",
      "kind": "user",
      "source": "user"
    },
    "main.negative_prompts": {
      "value": "不出现商标、额外人物或未提供的事实",
      "kind": "user",
      "source": "user"
    },
    "main.protagonist_identity": {
      "value": "虚构成年训练者林舟，深蓝训练服，使用软质练习刀",
      "kind": "user",
      "source": "user"
    },
    "main.protagonist_ref": {
      "value": "@image1",
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
    "main.scene_desc": {
      "value": "虚构训练庭院，平整地面、石墙和一个木门，无围观人群",
      "kind": "user",
      "source": "user"
    },
    "main.scene_layout": {
      "value": "两人相距两米沿东西轴站立，木门位于北侧，镜头留在南侧",
      "kind": "user",
      "source": "user"
    },
    "main.style_reference": {
      "value": "现代硬派武术电影气质 + ACT 动作游戏第三人称战斗镜头",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.action_principles,main.antagonist_identity,main.antagonist_ref,main.aspect_ratio,main.audio_design,main.camera_follow_spec,main.camera_motion_rules,main.character_dynamics,main.cut_rules,main.dual_consistency_lock,main.duration_s,main.ending_directive,main.environment_interaction,main.fight_arc,main.fight_beats,main.final_feel,main.footage_style,main.frame_rate,main.lighting_palette,main.negative_prompts,main.protagonist_identity,main.protagonist_ref,main.provider_banner,main.realism_rules,main.resolution,main.scenario_summary,main.scene_desc,main.scene_layout,main.style_reference --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/realistic-fight-scene-generation@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Realistic Fight Scene Generation。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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
