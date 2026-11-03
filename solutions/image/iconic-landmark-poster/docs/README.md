<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# ICONIC LANDMARK SERIES 城市地标海报：完整使用教程

固定视觉系统（上半真实摄影 + 下半矢量解构 + 建筑档案排版）的城市地标海报 Prompt，城市差异全部变量化

## 如何提出需求

适用目标：配合消费侧渲染器按城市 spec 绑定变量；支持同城多变体与系列索引。本教程以“为虚构的阅读活动设计视觉”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「ICONIC LANDMARK SERIES 城市地标海报」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`image/iconic-landmark-poster@1.0.0`；成熟度：`exploratory`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `main`

职责：Fixed visual system (photo upper + vector lower + archival typography) city landmark poster prompt with fully parameterized city content

精确引用：`promptrepo://official/image/iconic-landmark-poster@1.0.0?locale=en`；role：`main`。
合同许可：`internal`；permissions：`execute_requires_review, preview`。

<!-- guide:begin inputs main -->
### 输入字段

本角色案例真源：[正例与反例](../tutorials/main.en.json)；人工内容审阅尚未完成。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |
| `aspect` | string／可选 | 画幅，城市 spec 注入，英文；由用户选择并确认 | default=2:3 | 2:3 |
| `background` | string／必填 | 远景弱化，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Modern London buildings may appear faintly in the distance, but must be de-emphasized |
| `city_name` | string／必填 | 城市名，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | LONDON |
| `clouds` | string／必填 | 云量，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | A few characteristically British stratus layers and soft cumulus, a slightly overcast feel, but never gloomy |
| `coordinates` | string／必填 | 经纬度，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | 51.5007° N<br>0.1246° W |
| `easter_egg` | string／可选 | 城市彩蛋，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Optionally hide one tiny minimalist red London double-decker bus silhouette as an easter egg, no larger than 1% of the frame |
| `est` | string／必填 | EST 年份，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | 1859 |
| `feel` | string／必填 | 整体气质，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Keep the feel of an architectural design archive; never drift into tourist cartoon illustration |
| `footer` | string／必填 | 底部脚注，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | PALACE OF WESTMINSTER |
| `hero_features` | string／必填 | hero 摄影特征，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | the gilded clock dial, the Gothic Revival spire, the finely detailed stone facade, the vertical window tracery, the crowning pinnacle |
| `hero_identity` | string／必填 | hero 识别元素，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | the tall rectangular tower shaft, the four large clock faces, the gilded clock-face ornament, the Gothic window tracery, the spire structure, the slender pinnacle |
| `hero_palette` | string／必填 | hero 配色，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | light sandstone, warm beige, grayish brown, low-saturation gold, deep gray-blue |
| `hero_placement` | string／必填 | hero 位置与比例，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Big Ben / Elizabeth Tower sits right of the visual center, the full tower clearly visible from its base to the spire tip, uncropped, with strictly true architectural proportions |
| `hero_simplification` | string／必填 | hero 解构规则，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Simplify the complex Gothic structure into rectangles + thin vertical lines + triangles + pointed arches + ultra-fine geometric lines; render each clock face as a single restrained pale-gold circle; no thick black outlines |
| `landmarks_line` | string／必填 | 核心地标组合，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Big Ben / Elizabeth Tower + Palace of Westminster + River Thames |
| `lens` | string／必填 | 镜头参数，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | 50-85mm architectural photography, medium-telephoto compression, building verticals kept perfectly straight, no fisheye, no exaggerated wide-angle distortion |
| `negative_extra` | string／可选 | 城市专属负面词，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | cartoon Big Ben, chibi London, children's book illustration, neon London, wrong Big Ben proportions, bent clock tower, missing clock face, incorrect Gothic structure, duplicated clock tower, London Eye stealing the subject, cheap tourist postcard style |
| `quality` | string／必填 | 质感尾词，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | authentic London travel photography, premium architectural photography, cinematic golden hour, real stone texture, natural HDR, high dynamic range, 4K |
| `rim_light` | string／必填 | 轮廓光，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Sunlight passes through the clouds from behind the side, tracing a delicate golden rim light along Big Ben's edges |
| `river` | string／必填 | 前景水体，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | The broad River Thames fills the foreground, occupying about 20-25% of the photography area; the water is low-saturation blue-gray with fine natural ripples and slight building reflections |
| `river_lines` | string／必填 | 水体抽象线条，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | A single ultra-fine deep gray-blue horizontal line beneath the buildings sets the baseline, with 5-7 ultra-thin horizontal lines of varying lengths below it in mist blue, gray-blue, and light navy, abstracting the Thames water surface |
| `scale_reference` | string／可选 | 比例参照物，城市 spec 注入，英文；来自已提供资料或已接受引用；合成引用不可当成真实资产 | 合同未附加范围限制 | A single very small London tour boat may appear as a scale reference, but must not steal the subject |
| `series_no` | string／必填 | 系列编号，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | 001 |
| `sky_gradient` | string／必填 | 天空渐变，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | a natural gradient from pale gray-blue to soft misty violet to light peach pink to faint warm gold |
| `skyline` | string／必填 | 天际线与石材，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | The Palace of Westminster stretches horizontally beside Big Ben, forming the classic London skyline; the buildings use real warm beige stone, with soft golden highlights where the setting sun strikes |
| `subtitle` | string／必填 | 副标题，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | LONDON, UNITED KINGDOM |
| `sun` | string／必填 | 几何太阳，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | A huge translucent geometric circle sun sits behind and slightly left of Big Ben, in very soft British mist pink / Dusty Rose / Pale Peach; the circle is partially occluded by Big Ben and the Palace; no realistic sun texture |
| `supporting` | string／必填 | 配景建筑解构，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | A simplified Palace of Westminster extends horizontally to the left of Big Ben; the complex Gothic facade is highly geometricized, keeping only the row of spires, the rectangular main body, the towers, the pointed-arch windows, and the horizontal base; the building must be clearly lower than Big Ben |
| `supporting_palette` | string／必填 | 配景配色，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | beige-gray, sand, light brown, gray-blue, pale gold |
| `time` | string／必填 | 时间设定，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | London evening, golden hour transitioning into blue hour |
| `title_line1` | string／必填 | 主标题第一行，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | LONDON |
| `title_line2` | string／必填 | 主标题第二行，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | BIG BEN |
| `viewpoint` | string／必填 | 摄影视点，城市 spec 注入，英文；由用户选择并确认 | 合同未附加范围限制 | Viewing the Palace of Westminster from near the south bank of the River Thames |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example main -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/image/iconic-landmark-poster@1.0.0?locale=en' --role 'main' --output 'main-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/image/iconic-landmark-poster@1.0.0?locale=en' --role 'main' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 完整 CLI 练习

以下值均为合成练习；请先阅读输入表。脚本只在你输入 yes 后记录确认，实际使用应替换成自己的资料和选择。每一步从当前回执取 revision，不固定写死版本号。

```bash
set -eu
state=$(template-registry prompt session create --ref 'promptrepo://official/image/iconic-landmark-poster@1.0.0?locale=en' --role 'main' --goal '为虚构的阅读活动设计视觉' --json)
session_id=$(printf '%s' "$state" | jq -er '.data.id')
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(printf '%s' '{"text": "虚构活动“周末阅读角”：桌边一盏灯、一册书，安静、温暖，不使用真人或商标。"}' | template-registry prompt source import --session "$session_id" --expected-revision "$revision" --id tutorial-source --stdin --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
state=$(template-registry prompt session update --session "$session_id" --expected-revision "$revision" --stdin --json <<'INPUT'
{
  "fields": {
    "main.aspect": {
      "value": "2:3",
      "kind": "user",
      "source": "user"
    },
    "main.background": {
      "value": "Modern London buildings may appear faintly in the distance, but must be de-emphasized",
      "kind": "user",
      "source": "user"
    },
    "main.city_name": {
      "value": "LONDON",
      "kind": "user",
      "source": "user"
    },
    "main.clouds": {
      "value": "A few characteristically British stratus layers and soft cumulus, a slightly overcast feel, but never gloomy",
      "kind": "user",
      "source": "user"
    },
    "main.coordinates": {
      "value": "51.5007° N\n0.1246° W",
      "kind": "user",
      "source": "user"
    },
    "main.easter_egg": {
      "value": "Optionally hide one tiny minimalist red London double-decker bus silhouette as an easter egg, no larger than 1% of the frame",
      "kind": "user",
      "source": "user"
    },
    "main.est": {
      "value": "1859",
      "kind": "user",
      "source": "user"
    },
    "main.feel": {
      "value": "Keep the feel of an architectural design archive; never drift into tourist cartoon illustration",
      "kind": "user",
      "source": "user"
    },
    "main.footer": {
      "value": "PALACE OF WESTMINSTER",
      "kind": "user",
      "source": "user"
    },
    "main.hero_features": {
      "value": "the gilded clock dial, the Gothic Revival spire, the finely detailed stone facade, the vertical window tracery, the crowning pinnacle",
      "kind": "user",
      "source": "user"
    },
    "main.hero_identity": {
      "value": "the tall rectangular tower shaft, the four large clock faces, the gilded clock-face ornament, the Gothic window tracery, the spire structure, the slender pinnacle",
      "kind": "user",
      "source": "user"
    },
    "main.hero_palette": {
      "value": "light sandstone, warm beige, grayish brown, low-saturation gold, deep gray-blue",
      "kind": "user",
      "source": "user"
    },
    "main.hero_placement": {
      "value": "Big Ben / Elizabeth Tower sits right of the visual center, the full tower clearly visible from its base to the spire tip, uncropped, with strictly true architectural proportions",
      "kind": "user",
      "source": "user"
    },
    "main.hero_simplification": {
      "value": "Simplify the complex Gothic structure into rectangles + thin vertical lines + triangles + pointed arches + ultra-fine geometric lines; render each clock face as a single restrained pale-gold circle; no thick black outlines",
      "kind": "user",
      "source": "user"
    },
    "main.landmarks_line": {
      "value": "Big Ben / Elizabeth Tower + Palace of Westminster + River Thames",
      "kind": "user",
      "source": "user"
    },
    "main.lens": {
      "value": "50-85mm architectural photography, medium-telephoto compression, building verticals kept perfectly straight, no fisheye, no exaggerated wide-angle distortion",
      "kind": "user",
      "source": "user"
    },
    "main.negative_extra": {
      "value": "cartoon Big Ben, chibi London, children's book illustration, neon London, wrong Big Ben proportions, bent clock tower, missing clock face, incorrect Gothic structure, duplicated clock tower, London Eye stealing the subject, cheap tourist postcard style",
      "kind": "user",
      "source": "user"
    },
    "main.quality": {
      "value": "authentic London travel photography, premium architectural photography, cinematic golden hour, real stone texture, natural HDR, high dynamic range, 4K",
      "kind": "user",
      "source": "user"
    },
    "main.rim_light": {
      "value": "Sunlight passes through the clouds from behind the side, tracing a delicate golden rim light along Big Ben's edges",
      "kind": "user",
      "source": "user"
    },
    "main.river": {
      "value": "The broad River Thames fills the foreground, occupying about 20-25% of the photography area; the water is low-saturation blue-gray with fine natural ripples and slight building reflections",
      "kind": "user",
      "source": "user"
    },
    "main.river_lines": {
      "value": "A single ultra-fine deep gray-blue horizontal line beneath the buildings sets the baseline, with 5-7 ultra-thin horizontal lines of varying lengths below it in mist blue, gray-blue, and light navy, abstracting the Thames water surface",
      "kind": "user",
      "source": "user"
    },
    "main.scale_reference": {
      "value": "A single very small London tour boat may appear as a scale reference, but must not steal the subject",
      "kind": "user",
      "source": "user"
    },
    "main.series_no": {
      "value": "001",
      "kind": "user",
      "source": "user"
    },
    "main.sky_gradient": {
      "value": "a natural gradient from pale gray-blue to soft misty violet to light peach pink to faint warm gold",
      "kind": "user",
      "source": "user"
    },
    "main.skyline": {
      "value": "The Palace of Westminster stretches horizontally beside Big Ben, forming the classic London skyline; the buildings use real warm beige stone, with soft golden highlights where the setting sun strikes",
      "kind": "user",
      "source": "user"
    },
    "main.subtitle": {
      "value": "LONDON, UNITED KINGDOM",
      "kind": "user",
      "source": "user"
    },
    "main.sun": {
      "value": "A huge translucent geometric circle sun sits behind and slightly left of Big Ben, in very soft British mist pink / Dusty Rose / Pale Peach; the circle is partially occluded by Big Ben and the Palace; no realistic sun texture",
      "kind": "user",
      "source": "user"
    },
    "main.supporting": {
      "value": "A simplified Palace of Westminster extends horizontally to the left of Big Ben; the complex Gothic facade is highly geometricized, keeping only the row of spires, the rectangular main body, the towers, the pointed-arch windows, and the horizontal base; the building must be clearly lower than Big Ben",
      "kind": "user",
      "source": "user"
    },
    "main.supporting_palette": {
      "value": "beige-gray, sand, light brown, gray-blue, pale gold",
      "kind": "user",
      "source": "user"
    },
    "main.time": {
      "value": "London evening, golden hour transitioning into blue hour",
      "kind": "user",
      "source": "user"
    },
    "main.title_line1": {
      "value": "LONDON",
      "kind": "user",
      "source": "user"
    },
    "main.title_line2": {
      "value": "BIG BEN",
      "kind": "user",
      "source": "user"
    },
    "main.viewpoint": {
      "value": "Viewing the Palace of Westminster from near the south bank of the River Thames",
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
state=$(template-registry prompt session confirm --session "$session_id" --expected-revision "$revision" --confirm-goal --fields main.aspect,main.background,main.city_name,main.clouds,main.coordinates,main.easter_egg,main.est,main.feel,main.footer,main.hero_features,main.hero_identity,main.hero_palette,main.hero_placement,main.hero_simplification,main.landmarks_line,main.lens,main.negative_extra,main.quality,main.rim_light,main.river,main.river_lines,main.scale_reference,main.series_no,main.sky_gradient,main.skyline,main.subtitle,main.sun,main.supporting,main.supporting_palette,main.time,main.title_line1,main.title_line2,main.viewpoint --sources tutorial-source --decision-ref tutorial-interactive-yes --json)
revision=$(printf '%s' "$state" | jq -er '.data.revision')
compiled=$(template-registry prompt compile --session "$session_id" --expected-revision "$revision" --json)
compile_id=$(printf '%s' "$compiled" | jq -er '.data.id')
template-registry prompt export --compile "$compile_id" --output "result-$session_id" --json
template-registry prompt bundle verify --path "result-$session_id" --json
```

成功时应得到 session id、递增 revision、compile id、导出位置和通过的包校验。若 inspect 返回 owner_only、格式或能力不支持，停止上述通用编译练习，采用下方领域交接；不要改合同绕过限制。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/image/iconic-landmark-poster@1.0.0?locale=en","role":"main"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks main -->
### 结果示例与检查

示例目标：ICONIC LANDMARK SERIES City Landmark Poster。主体、构图与风格一致；引用图中的未知材质不能写成事实。
合成内容示例（供理解输出方向，未运行模型）：画面候选：以黄铜桌灯和打开的书为主体，保持无品牌；根据「ICONIC LANDMARK SERIES 城市地标海报」的风格与构图字段调整表现。这里只描述待生成画面，不展示或声称已经出图。
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
