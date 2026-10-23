# style-scene-pairing-beta 使用指南

全球"风格 × 场景 × 主题"配对编译模板：输入创作地理单元与经核实的场景事实，输出合理性分级、敏感性检查、主提示词与混合风格变体。框架原则：地区事实先进合理性判断，再选风格——先挑 aesthetic 再强迫地方配合是反模式。

## 何时用本模板

- 为某国家/地区/文化景观选择合适的视觉风格，或校验一个已有"风格 × 地点"组合的合理性。
- 生成全球风格配对数据集的条目（配对评估 + prompt + 置信级）。
- 扩展风格库时判断新风格词的层级（历史谱系 / 地域衍生 / 视觉移植）。

何时不该用：

- 风格已定、只要风格层渲染 → 各风格层模板（`southern-gothic-style-beta`、`xianxia-hazy-fantasy` 等），把本模板的 Primary prompt 填进它们的 `setting`/`format_clause` 变量。
- 视频镜头编译 → `video-prompt-optimization-beta`，风格线索填 `style_requirements`。
- 批量系列数据（320 地理单元主表）→ 本模板产出单条配对；批量存储参照 `iconic-landmark-poster` 的 cities spec 或 `candid-portrait-matrix` 的矩阵模式另建数据 solution。

## 输入变量

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `geo_unit` | 是 | 创作地理单元：M49 国家/地区（`日本（JPN）`）或次国家/生态区（`美国｜南阿巴拉契亚（X-USA-APP）`，X- 前缀为本项目内部创作代码，非官方行政代码） |
| `scene_facts` | 是 | 场景事实层：建筑/城市、森林/湿地、草原/农业、沙漠/高山、工业/交通设施、文化/宗教景观——来自权威来源的事实描述 |
| `target_styles` | 是 | 一个主风格 + 至多两个次风格（32 词表内；不确定时写候选方向由模板评估） |
| `medium` | 否 | `painting` / `photography` / `film` / `game` / `ai_image` |
| `themes_focus` | 否 | 主题方向：家族记忆、去工业化、朝圣、边境、殖民现代性…… |
| `source_notes` | 否 | 来源与置信说明：来源分级 S/A/A-/B+/B/C/D，机构名与访问情况 |
| `output_language` | 否 | 输出语言，默认 `zh` |

## 固化的框架规则（模板内部执行）

1. 三层风格体系判定：历史谱系（Romanticism/Symbolism…）≠ 地域文化模式（Southern Gothic/Folk Horror）≠ 网络视觉语汇（Dark Academia/Analog Horror——只作处理层）。
2. style_relation 三级：`NATIVE_OR_HISTORIC` / `REGIONAL_DERIVATIVE` / `TRANSCULTURAL_VISUAL`，须引用场景事实作证据。
3. 匹配分公式：25% 环境地貌 + 20% 建筑/材质 + 20% 文学艺术谱系 + 20% 社会历史主题 + 15% 媒介可转译性 − 文化误读惩罚（硬门槛）。
4. 敏感性硬门槛：原住民宗教、奴隶制、殖民史、强迫劳动、墓葬、圣地——只描绘空间、光线、材料与历史记忆；真实信仰不得写成"邪教/巫术/野蛮仪式"；触发即转人工审核。
5. 输出五块：Pairing assessment / Sensitivity check / Primary prompt / Mixed-style variant / Confidence（A/B/C/Review）。

## 来源分级速查

S 官方中文国际/国家资料（UNESCO 中文站等）＞ A 官方原始资料（UNESCO WHC、UN M49、NPS、Parks Canada）＞ A- 官方博物馆/档案 ＞ B+ 同行评议研究 ＞ B 博物馆学术资源（Met Heilbrunn）＞ C 高质量二手（JSTOR Daily）＞ D 社交/aesthetic 站（只用于发现关键词，不作事实依据）。权威性优先于语言，同等级资料优先中文。

## 消费方式

Exact ref：

```text
promptrepo://official/image/style-scene-pairing-beta@1.0.0-beta.1?locale=en
```

框架方法论源：用户 2026-10 全球风格×场景×主题配对研究（以 Southern Gothic 为核心的跨地域视觉创作框架）。产出 prompt 的出图执行交 Eikona。
