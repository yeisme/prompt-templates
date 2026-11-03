<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# 真实生活摄影抓拍写真（随机矩阵）：完整使用教程

把主体与 12 个画面维度（表情/服装/场景/瞬间/景别/焦段/机位/构图/前景/光线/色彩/摄影状态）编译为可直接投递图像模型的抓拍写真 Prompt

## 如何提出需求

适用目标：配合消费侧采样器做批量候选生成与批内去重；单图使用时手工绑定全部变量。本教程以“为虚构的阅读活动设计视觉”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「真实生活摄影抓拍写真（随机矩阵）」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`image/candid-portrait-matrix@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

main 组织人物、镜头和姿态；delivery 按交付合同封装已选方向。先审阅实际图像，再处理需要图像结果的后续步骤。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `delivery`

职责：Prepare a structured handoff to the consuming production tool.

精确引用：`promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en`；role：`delivery`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs delivery -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/delivery.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `aspect` | enum／可选 | 目标画幅；由用户选择并确认 | enum=["9:16", "2:3", "3:4"]；default=9:16 | 9:16 |
| `camera` | enum／必填 | 机位取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extremely low angle near the water surface", "low-angle shot from beneath giant lotus leaves", "ground-level low angle", "low angle below the subject's waist", "eye-level candid shot", "slight high angle", "pronounced high-angle shot", "shooting down from the stairs above", "side shot through plants", "shooting from behind a door frame", "shooting indoors from outside the window", "long-distance shot from the front of the carriage", "shooting from behind the subject", "over-the-shoulder view", "tilted Dutch angle", "subject placed fully off-center", "photographer hidden behind environmental objects, paparazzi-style view"] | low-angle shot from beneath giant lotus leaves |
| `composition` | enum／必填 | 构图取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extreme negative space", "large expanse of sky", "large expanse of water", "subject pressed into the bottom third", "subject at the extreme edge", "centered composition occluded by foreground", "asymmetric composition", "diagonal composition", "perspective leading-line composition", "giant natural forms looming over the subject", "small-scale figure in an environmental portrait", "foreground occupying one third of the frame", "foreground occupying half the frame", "peeking through gaps in foliage", "door-frame framing", "window-frame framing", "lotus leaves forming a natural circular frame", "architectural geometry slicing the frame"] | lotus leaves forming a natural circular frame |
| `expression` | enum／必填 | 表情取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["cold and spaced out", "gently squinting", "natural squint from glaring sunlight", "faint almost-smile", "looking down, lost in thought", "eyes closed, feeling the wind", "suddenly looking back", "lifting eyes to the distance", "barely holding back a laugh", "just-woke-up laziness", "natural pause when caught by the camera", "slight frown", "thoughtfully pondering", "briefly dazed"] | faint almost-smile |
| `foreground` | enum／必填 | 前景取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["fully defocused lotus flowers", "giant lotus leaves", "tree leaves", "bamboo leaves", "white curtains", "glass reflection", "water-surface glare", "flower petals", "reeds", "door frame", "window frame", "car window glass", "bus seats", "transparent plastic curtain", "railing", "edge of a white wall", "wet tree branches"] | giant lotus leaves |
| `lens` | enum／必填 | 镜头焦段取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["24mm ultra-wide close range", "28mm wide angle", "35mm environmental portrait", "50mm natural perspective", "85mm compressed portrait", "105mm distant voyeuristic telephoto"] | 85mm compressed portrait |
| `light` | enum／必填 | 光线取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["harsh midsummer noon light", "dappled light through tree shade", "afternoon side-backlight", "low-angle evening backlight", "clear diffused light after rain", "high-contrast natural window light", "fill light reflected off water", "light bounced off white walls", "fine light flecks through leaves", "partially overexposed highlights", "subject at the light-shadow boundary", "bright background, subject slightly darker", "face lit by only a small patch of sunlight"] | dappled light through tree shade |
| `moment` | enum／必填 | 瞬间状态取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["just sat down", "about to stand up", "looking down, adjusting her skirt hem", "raising a hand to hold her hat", "wind lifting her hair", "peeking out from behind leaves", "bending over to touch the water", "stepping into water barefoot", "walking slowly along the boardwalk", "sitting at the stern, daydreaming", "looking sideways into the distance", "smoothing wind-tousled hair", "looking down while washing fruit", "napping against the window", "suddenly turning her head back", "eyes closed, basking in the sun", "stepping from shade into sunlight", "hand resting on the railing", "sitting on stone steps, swinging her legs", "shading herself with a giant lotus leaf", "crouching by the water", "leaning slightly back", "resting, propped on her hands", "accidentally caught while passing the lens"] | shading herself with a giant lotus leaf |
| `palette` | enum／必填 | 色彩取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["sky blue + verdant green + white", "deep green + creamy white + skin tone", "water blue + white + gray", "teal green + off-white + a few pink flowers", "deep blue night + cool white lamplight", "post-rain gray-blue + moist green"] | teal green + off-white + a few pink flowers |
| `scene` | enum／必填 | 场景取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["midsummer lotus pond", "old wooden boat", "lakeside wooden boardwalk", "shallow countryside stream", "waterside bamboo grove", "white-walled courtyard", "window of an old southern house", "modern glass greenhouse", "lakeside stone steps", "mountain road", "white seaside building", "city rooftop", "old public bus", "vintage train carriage", "minimalist guesthouse", "convenience-store freezer aisle", "washing fruit by the river", "bench under tree shade", "alley after rain", "old dock", "summer poolside", "reed-lined lakeshore", "countryside orchard", "white pavilion", "beneath giant lotus leaves"] | midsummer lotus pond |
| `shot` | enum／必填 | 景别取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extreme close-up facial detail", "shoulder-level close-up", "bust close-up", "waist-up medium close-up", "knee-up medium shot", "half-body environmental portrait", "full-body environmental portrait", "small-figure wide environmental composition"] | waist-up medium close-up |
| `state` | enum／必填 | 摄影状态取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["natural candid capture", "unposed", "accidentally caught by the photographer", "subject completely unaware of the camera", "slight motion blur", "partial defocus", "layered glass reflections", "real lens flare", "edge highlight bloom", "slight overexposure", "shallow depth of field", "long-distance compression", "close-range wide-angle distortion", "natural film grain", "slight digital noise", "instant point-and-shoot feel"] | natural candid capture |
| `subject` | string／必填 | 主体外观一句话，英文，须写明 adult 与镜头感；由用户选择并确认 | 合同未附加范围限制 | an adult East Asian woman with a quiet demeanor and natural camera awareness |
| `wardrobe` | enum／必填 | 服装风格取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["Brandy Melville style", "pure-and-sultry style", "glamorous stepmom style", "mature feminine style", "Chanel-inspired style", "homewear style", "Korean light-mature style", "French lazy-chic style", "minimalist aloof style", "old money style", "resort style", "urban commuter style", "sweet-and-cool style", "Y2K style", "K-pop girl-group off-duty style", "understated plain-water luxury", "low-saturation premium casual wear", "relaxed off-duty style"] | resort style |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example delivery -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'delivery' --output 'delivery-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'delivery' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'delivery' --goal '为虚构的阅读活动设计视觉' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "本次合成任务采用已验证案例 valid-lotus-pond；各字段以该案例的公开输入为准，不追加资料外事实。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.aspect": {
      "value": "9:16",
      "kind": "user",
      "source": "user"
    },
    "main.camera": {
      "value": "low-angle shot from beneath giant lotus leaves",
      "kind": "user",
      "source": "user"
    },
    "main.composition": {
      "value": "lotus leaves forming a natural circular frame",
      "kind": "user",
      "source": "user"
    },
    "main.expression": {
      "value": "faint almost-smile",
      "kind": "user",
      "source": "user"
    },
    "main.foreground": {
      "value": "giant lotus leaves",
      "kind": "user",
      "source": "user"
    },
    "main.lens": {
      "value": "85mm compressed portrait",
      "kind": "user",
      "source": "user"
    },
    "main.light": {
      "value": "dappled light through tree shade",
      "kind": "user",
      "source": "user"
    },
    "main.moment": {
      "value": "shading herself with a giant lotus leaf",
      "kind": "user",
      "source": "user"
    },
    "main.palette": {
      "value": "teal green + off-white + a few pink flowers",
      "kind": "user",
      "source": "user"
    },
    "main.scene": {
      "value": "midsummer lotus pond",
      "kind": "user",
      "source": "user"
    },
    "main.shot": {
      "value": "waist-up medium close-up",
      "kind": "user",
      "source": "user"
    },
    "main.state": {
      "value": "natural candid capture",
      "kind": "user",
      "source": "user"
    },
    "main.subject": {
      "value": "an adult East Asian woman with a quiet demeanor and natural camera awareness",
      "kind": "user",
      "source": "user"
    },
    "main.wardrobe": {
      "value": "resort style",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.aspect,main.camera,main.composition,main.expression,main.foreground,main.lens,main.light,main.moment,main.palette,main.scene,main.shot,main.state,main.subject,main.wardrobe --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en","role":"delivery"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks delivery -->
### 结果示例与检查

示例目标：Delivery handoff。主体、构图与风格一致；引用图中的未知材质不能写成事实。
输出结构示例见 [invalid-missing-subject.output](../fixtures/delivery.en/invalid-missing-subject.output.json)、[valid-lotus-pond.output](../fixtures/delivery.en/valid-lotus-pond.output.json)。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。
案例的 review_checks 是人工审阅依据；fixture 输出仅证明绑定和 schema 校验，不代表模型效果。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/delivery.en.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `main`

职责：Compile a subject plus 12 picture dimensions into a candid summer portrait prompt ready for image-model delivery

精确引用：`promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `aspect` | enum／可选 | 目标画幅；由用户选择并确认 | enum=["9:16", "2:3", "3:4"]；default=9:16 | 9:16 |
| `camera` | enum／必填 | 机位取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extremely low angle near the water surface", "low-angle shot from beneath giant lotus leaves", "ground-level low angle", "low angle below the subject's waist", "eye-level candid shot", "slight high angle", "pronounced high-angle shot", "shooting down from the stairs above", "side shot through plants", "shooting from behind a door frame", "shooting indoors from outside the window", "long-distance shot from the front of the carriage", "shooting from behind the subject", "over-the-shoulder view", "tilted Dutch angle", "subject placed fully off-center", "photographer hidden behind environmental objects, paparazzi-style view"] | extremely low angle near the water surface |
| `composition` | enum／必填 | 构图取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extreme negative space", "large expanse of sky", "large expanse of water", "subject pressed into the bottom third", "subject at the extreme edge", "centered composition occluded by foreground", "asymmetric composition", "diagonal composition", "perspective leading-line composition", "giant natural forms looming over the subject", "small-scale figure in an environmental portrait", "foreground occupying one third of the frame", "foreground occupying half the frame", "peeking through gaps in foliage", "door-frame framing", "window-frame framing", "lotus leaves forming a natural circular frame", "architectural geometry slicing the frame"] | extreme negative space |
| `expression` | enum／必填 | 表情取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["cold and spaced out", "gently squinting", "natural squint from glaring sunlight", "faint almost-smile", "looking down, lost in thought", "eyes closed, feeling the wind", "suddenly looking back", "lifting eyes to the distance", "barely holding back a laugh", "just-woke-up laziness", "natural pause when caught by the camera", "slight frown", "thoughtfully pondering", "briefly dazed"] | cold and spaced out |
| `foreground` | enum／必填 | 前景取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["fully defocused lotus flowers", "giant lotus leaves", "tree leaves", "bamboo leaves", "white curtains", "glass reflection", "water-surface glare", "flower petals", "reeds", "door frame", "window frame", "car window glass", "bus seats", "transparent plastic curtain", "railing", "edge of a white wall", "wet tree branches"] | fully defocused lotus flowers |
| `lens` | enum／必填 | 镜头焦段取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["24mm ultra-wide close range", "28mm wide angle", "35mm environmental portrait", "50mm natural perspective", "85mm compressed portrait", "105mm distant voyeuristic telephoto"] | 24mm ultra-wide close range |
| `light` | enum／必填 | 光线取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["harsh midsummer noon light", "dappled light through tree shade", "afternoon side-backlight", "low-angle evening backlight", "clear diffused light after rain", "high-contrast natural window light", "fill light reflected off water", "light bounced off white walls", "fine light flecks through leaves", "partially overexposed highlights", "subject at the light-shadow boundary", "bright background, subject slightly darker", "face lit by only a small patch of sunlight"] | harsh midsummer noon light |
| `moment` | enum／必填 | 瞬间状态取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["just sat down", "about to stand up", "looking down, adjusting her skirt hem", "raising a hand to hold her hat", "wind lifting her hair", "peeking out from behind leaves", "bending over to touch the water", "stepping into water barefoot", "walking slowly along the boardwalk", "sitting at the stern, daydreaming", "looking sideways into the distance", "smoothing wind-tousled hair", "looking down while washing fruit", "napping against the window", "suddenly turning her head back", "eyes closed, basking in the sun", "stepping from shade into sunlight", "hand resting on the railing", "sitting on stone steps, swinging her legs", "shading herself with a giant lotus leaf", "crouching by the water", "leaning slightly back", "resting, propped on her hands", "accidentally caught while passing the lens"] | just sat down |
| `palette` | enum／必填 | 色彩取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["sky blue + verdant green + white", "deep green + creamy white + skin tone", "water blue + white + gray", "teal green + off-white + a few pink flowers", "deep blue night + cool white lamplight", "post-rain gray-blue + moist green"] | sky blue + verdant green + white |
| `scene` | enum／必填 | 场景取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["midsummer lotus pond", "old wooden boat", "lakeside wooden boardwalk", "shallow countryside stream", "waterside bamboo grove", "white-walled courtyard", "window of an old southern house", "modern glass greenhouse", "lakeside stone steps", "mountain road", "white seaside building", "city rooftop", "old public bus", "vintage train carriage", "minimalist guesthouse", "convenience-store freezer aisle", "washing fruit by the river", "bench under tree shade", "alley after rain", "old dock", "summer poolside", "reed-lined lakeshore", "countryside orchard", "white pavilion", "beneath giant lotus leaves"] | midsummer lotus pond |
| `shot` | enum／必填 | 景别取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["extreme close-up facial detail", "shoulder-level close-up", "bust close-up", "waist-up medium close-up", "knee-up medium shot", "half-body environmental portrait", "full-body environmental portrait", "small-figure wide environmental composition"] | extreme close-up facial detail |
| `state` | enum／必填 | 摄影状态取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["natural candid capture", "unposed", "accidentally caught by the photographer", "subject completely unaware of the camera", "slight motion blur", "partial defocus", "layered glass reflections", "real lens flare", "edge highlight bloom", "slight overexposure", "shallow depth of field", "long-distance compression", "close-range wide-angle distortion", "natural film grain", "slight digital noise", "instant point-and-shoot feel"] | natural candid capture |
| `subject` | string／必填 | 主体外观一句话，英文，须写明 adult 与镜头感；由用户选择并确认 | 合同未附加范围限制 | a highly camera-savvy adult Korean Instagram influencer with fair skin and an exaggerated figure |
| `wardrobe` | enum／必填 | 服装风格取值，英文，须来自取值池并与场景类别兼容；由用户选择并确认 | enum=["Brandy Melville style", "pure-and-sultry style", "glamorous stepmom style", "mature feminine style", "Chanel-inspired style", "homewear style", "Korean light-mature style", "French lazy-chic style", "minimalist aloof style", "old money style", "resort style", "urban commuter style", "sweet-and-cool style", "Y2K style", "K-pop girl-group off-duty style", "understated plain-water luxury", "low-saturation premium casual wear", "relaxed off-duty style"] | Brandy Melville style |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en' --role 'main' --goal '为虚构的阅读活动设计视觉' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.aspect": {
      "value": "9:16",
      "kind": "user",
      "source": "user"
    },
    "main.camera": {
      "value": "extremely low angle near the water surface",
      "kind": "user",
      "source": "user"
    },
    "main.composition": {
      "value": "extreme negative space",
      "kind": "user",
      "source": "user"
    },
    "main.expression": {
      "value": "cold and spaced out",
      "kind": "user",
      "source": "user"
    },
    "main.foreground": {
      "value": "fully defocused lotus flowers",
      "kind": "user",
      "source": "user"
    },
    "main.lens": {
      "value": "24mm ultra-wide close range",
      "kind": "user",
      "source": "user"
    },
    "main.light": {
      "value": "harsh midsummer noon light",
      "kind": "user",
      "source": "user"
    },
    "main.moment": {
      "value": "just sat down",
      "kind": "user",
      "source": "user"
    },
    "main.palette": {
      "value": "sky blue + verdant green + white",
      "kind": "user",
      "source": "user"
    },
    "main.scene": {
      "value": "midsummer lotus pond",
      "kind": "user",
      "source": "user"
    },
    "main.shot": {
      "value": "extreme close-up facial detail",
      "kind": "user",
      "source": "user"
    },
    "main.state": {
      "value": "natural candid capture",
      "kind": "user",
      "source": "user"
    },
    "main.subject": {
      "value": "a highly camera-savvy adult Korean Instagram influencer with fair skin and an exaggerated figure",
      "kind": "user",
      "source": "user"
    },
    "main.wardrobe": {
      "value": "Brandy Melville style",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.aspect,main.camera,main.composition,main.expression,main.foreground,main.lens,main.light,main.moment,main.palette,main.scene,main.shot,main.state,main.subject,main.wardrobe --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/image/candid-portrait-matrix@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：Candid Lifestyle Portrait (Random Matrix)。主体、构图与风格一致；引用图中的未知材质不能写成事实。
合成内容示例（供理解输出方向，未运行模型）：画面候选：以黄铜桌灯和打开的书为主体，保持无品牌；根据「真实生活摄影抓拍写真（随机矩阵）」的风格与构图字段调整表现。这里只描述待生成画面，不展示或声称已经出图。
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

声明的消费者：eikona。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->
