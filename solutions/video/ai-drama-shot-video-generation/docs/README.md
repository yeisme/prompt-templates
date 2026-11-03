<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# AI Drama Shot Video Generation：完整使用教程

Compile character, ultimate skill, enemies, scene, camera, and per-second storyboard into a shot-level prompt for direct video-model delivery

## 如何提出需求

适用目标：Use for AI drama charge-up ultimate-skill shot generation and human review; consumed by domain owners such as Scaena。本教程以“制作虚构阅读活动的短片方案”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「AI Drama Shot Video Generation」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`video/ai-drama-shot-video-generation@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Compile character, ultimate skill, enemies, scene, camera, and per-second storyboard into a shot-level prompt for direct video-model delivery

精确引用：`promptrepo://official/video/ai-drama-shot-video-generation@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, inspect, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | enum／可选 | 输出视频画幅；由用户选择并确认 | enum=["16:9", "9:16", "1:1", "2.39:1"]；default=16:9 | 16:9 |
| `camera_spec` | string／必填 | 镜头切换节奏、转场白名单、手持参数与冲击帧分级；由用户选择并确认 | min_length=10；max_length=4096 | 中景固定机位起始，格挡时缓慢推进，结束退回双人全景 |
| `character_core` | string／必填 | 角色全片的核心行为与站位设定；由用户选择并确认 | min_length=10；max_length=4096 | 先观察再防御，动作简洁；不会突然改变武器或服装 |
| `character_label` | string／必填 | 角色在 Prompt 中的称呼；由用户选择并确认 | min_length=2；max_length=128 | 角色A（女帝） |
| `character_ref` | string／必填 | 已登记角色资产的 @ 引用，禁止编造；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=2；max_length=256 | @ef946113-3379-4497-86e6-4dc529266c1d |
| `charge_phase_rule` | string／必填 | 蓄力阶段角色的行为红线，如全程悬空、绝不落地；由用户选择并确认 | min_length=10；max_length=4096 | 蓄力期间全程悬空施法，绝不落地、零站桩、零停顿 |
| `color_grading` | string／必填 | 色彩空间、暗部与高光色调倾向；由用户选择并确认 | min_length=4；max_length=2048 | 色彩空间Rec.2020，暗部偏幽紫，高光偏黑金 |
| `duration_s` | integer／必填 | 镜头总时长，分镜表必须连续覆盖；由用户选择并确认 | min=5；max=120；default=30 | 30 |
| `effect_mix` | string／必填 | 能量体/水墨/流体等特效类型与占比描述；由用户选择并确认 | min_length=4；max_length=2048 | 能量体60% + 水墨20% + 流体20% |
| `enemy_counterattack` | string／必填 | 蓄力期敌方的反击手段与强度；由用户选择并确认 | min_length=10；max_length=4096 | 格挡后退半步，随后一次低速横向试探，不连续追加动作 |
| `enemy_death_reaction` | string／必填 | 符合安全协议的受击与消亡表现；由用户选择并确认 | min_length=10；max_length=4096 | 被绞碎时喷发魂火痛苦抽搐，灰飞烟灭前发出凄厉惨叫，最后化为紫黑冥烬 |
| `enemy_desc` | string／必填 | 敌方群体构成与出场方式；由用户选择并确认 | min_length=10；max_length=4096 | 两名虚构成年训练者按顺序进入画面，不同时围攻或出现复制人物 |
| `enemy_ref` | string／可选 | 已登记敌方资产的 @ 引用；有对应资产时必填；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=0；max_length=256 | @image1 |
| `gore_protocol` | string／必填 | 血液/断肢等敏感内容的替代表现协议；由用户选择并确认 | min_length=4；max_length=2048 | ZeroBlood协议：严禁任何血液、断肢，受击全由粒子特效替代 |
| `max_actions_per_second` | integer／必填 | 每秒钟允许的最大动作数，防崩硬约束；由用户选择并确认 | min=1；max=5；default=3 | 3 |
| `negative_prompts` | string／必填 | 负面约束清单；模板内置默认负面项会并入；由用户选择并确认 | min_length=10；max_length=8192 | 不出现商标、额外人物或未提供的事实 |
| `provider_banner` | string／可选 | 可选的投递平台标识行，渲染在 Prompt 顶部；留空则省略；由用户选择并确认 | min_length=0；max_length=256 | Made with Seedance 2.5 |
| `quality_profile` | string／必填 | 渲染引擎、分辨率、帧率、HDR、胶片颗粒等整块画质规格描述；由用户选择并确认 | min_length=10；max_length=4096 | UE5.4 Path Tracing，Lumen全局光照，8K分辨率，60fps，12bit HDR1500，PBR物理材质渲染，35mm Kodak 5219胶片颗粒45% |
| `release_phase_rule` | string／必填 | 爆发与收尾阶段允许的动作，如落地收剑定格；由用户选择并确认 | min_length=10；max_length=4096 | 爆发后允许落地收剑、冷酷定格站立 |
| `scene_anchors` | string／必填 | 全片必须保持可辨识的刚性场景元素；由用户选择并确认 | min_length=4；max_length=2048 | 残破战车、断裂战旗、古战场白骨 |
| `scene_desc` | string／必填 | 场景氛围与环境描述；由用户选择并确认 | min_length=10；max_length=4096 | 虚构训练庭院，平整地面、石墙和一个木门，无围观人群 |
| `scene_ref` | string／可选 | 已登记场景资产的 @ 引用；有对应资产时必填；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=0；max_length=256 | @image1 |
| `shot_list` | string／必填 | 按分镜槽位结构编写的逐镜头指令，时间区间连续覆盖全片；由用户选择并确认 | min_length=10；max_length=65536 | 镜头1：建立庭院和站位；镜头2：完整显示一次格挡；镜头3：退步并结束训练 |
| `style_keywords` | string／必填 | 整体美术风格关键词组合；由用户选择并确认 | min_length=4；max_length=2048 | 顶级院线级真人特效大电影风格，真人实拍电影质感，次世代超写实，废土修仙融合 |
| `ultimate_skill_name` | string／必填 | 大招名称；由用户选择并确认 | min_length=2；max_length=128 | 冥狱剑仙阵 |
| `ultimate_skill_visual` | string／必填 | 法阵/符咒/飞剑等核心视觉与蓄力-爆发机制描述；由用户选择并确认 | min_length=10；max_length=4096 | 一道蓝色弧光沿练习刀运动轨迹消散，不遮住肢体与接触点 |
| `wardrobe_anchors` | string／必填 | 需要防穿模/防丢失的服装与外观特征清单；由用户选择并确认 | min_length=4；max_length=2048 | 橘红围巾、土黄长裙 |
| `weapon_desc` | string／可选 | 武器外观与特效描述；无武器镜头可留空；由用户选择并确认 | min_length=0；max_length=2048 | 长剑（通体黑金色，刃口流淌紫黑色深渊剑气） |
| `weapon_ref` | string／可选 | 已登记武器资产的 @ 引用；有武器资产时必填；来自已提供资料或已接受引用；合成引用不可当成真实资产 | regex=^@[A-Za-z0-9][A-Za-z0-9:._/-]{0,255}$；min_length=0；max_length=256 | @image1 |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/video/ai-drama-shot-video-generation@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/video/ai-drama-shot-video-generation@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/video/ai-drama-shot-video-generation@1.0.0?locale=en' --role 'main' --goal '制作虚构阅读活动的短片方案' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "30 秒短片：进入阅读角、翻开书、停在灯光下；不含真实人物、品牌或未授权音乐。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.aspect_ratio": {
      "value": "16:9",
      "kind": "user",
      "source": "user"
    },
    "main.camera_spec": {
      "value": "中景固定机位起始，格挡时缓慢推进，结束退回双人全景",
      "kind": "user",
      "source": "user"
    },
    "main.character_core": {
      "value": "先观察再防御，动作简洁；不会突然改变武器或服装",
      "kind": "user",
      "source": "user"
    },
    "main.character_label": {
      "value": "角色A（女帝）",
      "kind": "user",
      "source": "user"
    },
    "main.character_ref": {
      "value": "@ef946113-3379-4497-86e6-4dc529266c1d",
      "kind": "user",
      "source": "user"
    },
    "main.charge_phase_rule": {
      "value": "蓄力期间全程悬空施法，绝不落地、零站桩、零停顿",
      "kind": "user",
      "source": "user"
    },
    "main.color_grading": {
      "value": "色彩空间Rec.2020，暗部偏幽紫，高光偏黑金",
      "kind": "user",
      "source": "user"
    },
    "main.duration_s": {
      "value": 30,
      "kind": "user",
      "source": "user"
    },
    "main.effect_mix": {
      "value": "能量体60% + 水墨20% + 流体20%",
      "kind": "user",
      "source": "user"
    },
    "main.enemy_counterattack": {
      "value": "格挡后退半步，随后一次低速横向试探，不连续追加动作",
      "kind": "user",
      "source": "user"
    },
    "main.enemy_death_reaction": {
      "value": "被绞碎时喷发魂火痛苦抽搐，灰飞烟灭前发出凄厉惨叫，最后化为紫黑冥烬",
      "kind": "user",
      "source": "user"
    },
    "main.enemy_desc": {
      "value": "两名虚构成年训练者按顺序进入画面，不同时围攻或出现复制人物",
      "kind": "user",
      "source": "user"
    },
    "main.enemy_ref": {
      "value": "@image1",
      "kind": "user",
      "source": "user"
    },
    "main.gore_protocol": {
      "value": "ZeroBlood协议：严禁任何血液、断肢，受击全由粒子特效替代",
      "kind": "user",
      "source": "user"
    },
    "main.max_actions_per_second": {
      "value": 3,
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
    "main.quality_profile": {
      "value": "UE5.4 Path Tracing，Lumen全局光照，8K分辨率，60fps，12bit HDR1500，PBR物理材质渲染，35mm Kodak 5219胶片颗粒45%",
      "kind": "user",
      "source": "user"
    },
    "main.release_phase_rule": {
      "value": "爆发后允许落地收剑、冷酷定格站立",
      "kind": "user",
      "source": "user"
    },
    "main.scene_anchors": {
      "value": "残破战车、断裂战旗、古战场白骨",
      "kind": "user",
      "source": "user"
    },
    "main.scene_desc": {
      "value": "虚构训练庭院，平整地面、石墙和一个木门，无围观人群",
      "kind": "user",
      "source": "user"
    },
    "main.scene_ref": {
      "value": "@image1",
      "kind": "user",
      "source": "user"
    },
    "main.shot_list": {
      "value": "镜头1：建立庭院和站位；镜头2：完整显示一次格挡；镜头3：退步并结束训练",
      "kind": "user",
      "source": "user"
    },
    "main.style_keywords": {
      "value": "顶级院线级真人特效大电影风格，真人实拍电影质感，次世代超写实，废土修仙融合",
      "kind": "user",
      "source": "user"
    },
    "main.ultimate_skill_name": {
      "value": "冥狱剑仙阵",
      "kind": "user",
      "source": "user"
    },
    "main.ultimate_skill_visual": {
      "value": "一道蓝色弧光沿练习刀运动轨迹消散，不遮住肢体与接触点",
      "kind": "user",
      "source": "user"
    },
    "main.wardrobe_anchors": {
      "value": "橘红围巾、土黄长裙",
      "kind": "user",
      "source": "user"
    },
    "main.weapon_desc": {
      "value": "长剑（通体黑金色，刃口流淌紫黑色深渊剑气）",
      "kind": "user",
      "source": "user"
    },
    "main.weapon_ref": {
      "value": "@image1",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.aspect_ratio,main.camera_spec,main.character_core,main.character_label,main.character_ref,main.charge_phase_rule,main.color_grading,main.duration_s,main.effect_mix,main.enemy_counterattack,main.enemy_death_reaction,main.enemy_desc,main.enemy_ref,main.gore_protocol,main.max_actions_per_second,main.negative_prompts,main.provider_banner,main.quality_profile,main.release_phase_rule,main.scene_anchors,main.scene_desc,main.scene_ref,main.shot_list,main.style_keywords,main.ultimate_skill_name,main.ultimate_skill_visual,main.wardrobe_anchors,main.weapon_desc,main.weapon_ref --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/video/ai-drama-shot-video-generation@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：AI Drama Shot Video Generation。镜头时长、人物身份、空间连续性和声音衔接可检查；提示包不等于视频。
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
