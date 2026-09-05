# 实例：Seedance 2.5 夏末傍晚手机录像

本例展示 `realistic-vlog-shot-generation` 如何绑定为一条 Seedance 2.5 投递的 30 秒写实手机录像 Prompt。Provider 名只出现在 `provider_banner` 兼容信息中，不进入 tags 与分类。

## 变量绑定

| 变量 | 值 |
| --- | --- |
| `provider_banner` | `Made with Seedance 2.5` |
| `footage_style` | `ultra-realistic personal smartphone video` |
| `duration_s` | `30` |
| `resolution` | `1080p` |
| `aspect_ratio` | `16:9` |
| `scenario_summary` | `同一位年轻女性在一个夏末傍晚的即兴外出` |
| `subject_identity` | `保持她的确切身份：面部、身体比例、发型` |
| `wardrobe_and_accessories` | `灰绿oversize亚麻衬衫、白色背心、浅蓝牛仔裤、运动鞋、棕色斜挎包、银色手镯` |
| `consistency_lock` | `全片保持完全一致的身份、面部、比例、发型、服装与配饰` |
| `character_ref` | `@image1`（Seedance 位置引用） |
| `setting_desc` | `公寓楼道、安静的居民区街道与花摊、傍晚小市集、步行观景台日落` |
| `setting_exclusions` | `无品牌、地标、广告或摆拍人群` |
| `camera_style` | `亲密朋友用老款智能手机手持拍摄` |
| `camera_imperfections` | `自然晃动、构图不完美、自动对焦犹豫、曝光变化、运动模糊、数码噪点、偶发的延迟反应` |
| `camera_exclusions` | `无稳定器、无人机、电影化调度、慢动作、美颜滤镜或商业广告质感` |
| `sequence_beats` | 见下方时间线 |
| `realism_rules` | `准确解剖与自然生物力学、真实物理、身份与服装一致、可信的光线递进；无视觉错误、物体复制、物体消失、手部畸形或环境形变` |
| `audio_design` | `只有现场自然声：脚步、车流、自行车、市集环境声、孩童声、纸飞机扑动、风声与真实的笑声` |
| `audio_exclusions` | `无音乐、旁白、音效、字幕、标题、Logo、水印或屏幕文字` |
| `final_feel` | `一段被遗忘的真实手机录像：普通傍晚意外变得难忘。温暖、抓拍感、年轻、怀旧、真实人性` |
| `ending_directive` | `26-30秒她发现镜头，微笑，伸手向镜头，笑声中录制戛然中断` |
| `negative_prompts` | `稳定器，无人机，电影化调度，慢动作，美颜滤镜，商业广告感；视觉错误，物体复制，物体消失，手部畸形，环境形变；音乐，旁白，音效，字幕，标题，Logo，水印，屏幕文字` |

## 时间线（`sequence_beats`）

```text
00-05s：她离开公寓，锁门，注意到镜头，微笑，下楼。
05-10s：她穿过安静的居民区，发现花摊，拿起一朵小黄花闻了闻，笑了。相机短暂对焦到花上。
10-15s：一架纸飞机落在她脚边。她把它扔回给孩子，继续走。
15-21s：在傍晚小市集，她买了一个桃子，咬了一口，露出真实惊讶的微笑。
21-26s：她走到步行观景台，看日落，享受这一刻，微风拂动她的头发与衬衫。
26-30s：她注意到镜头，微笑，伸手向镜头，笑声中录制戛然中断。
```

## 渲染与投递

- 英文投递渲染 `main.en.md`（本 solution 为单语言 `en` 模板）。
- 渲染结果第一行为 `Made with Seedance 2.5`（来自 `provider_banner`）。
- `character_ref=@image1` 要求投递时图像槽位 1 已绑定同一人物参考图；引用本身不携带图像数据。
- 投递前按 `docs/review-checklist.zh-CN.md` 核对。
