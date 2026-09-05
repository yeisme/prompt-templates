# 实例：K-pop 新星演出前一日（30 秒 VO 纪实 Vlog）

本例展示 `realistic-docu-vlog-generation` 绑定为一条「韩国新星演出日自述」Prompt。无 Provider 横幅（`provider_banner` 留空）。

## 变量绑定

| 变量 | 值 |
| --- | --- |
| `footage_style` | `photorealistic live-action video` |
| `era_aesthetic` | `千禧年初（early-2000s）消费级 DV 质感` |
| `duration_s` / `resolution` / `aspect_ratio` | `30` / `1080p` / `16:9` |
| `scenario_summary` | `一位二十代中段的新锐流行歌手兼社媒创作者，记录演出开始前的一天` |
| `subject_identity` | `同一位韩国女性，二十代中段；保持确切面部身份、发型与外观` |
| `wardrobe_and_accessories` | `日常私服（耳环、包、鞋随节拍出现但不换装）；舞台段可进入演出服但须在同一天逻辑内` |
| `consistency_lock` | `全片保持完全一致的面部身份、发型、体型与外观` |
| `character_ref` | 有参考图时填 `@image1` 等位置引用 |
| `camera_formats` | `手持 DV 跟拍 + 不完美手持自拍 + 自然固定机位 + 后台快切蒙太奇` |
| `camera_imperfections` | `真实手抖、自动对焦犹豫、轻微运动模糊、曝光漂移、不完美构图、可见皮肤毛孔、自然的头发与织物运动` |
| `camera_exclusions` | `无精致商业广告质感、稳定器、无人机与不可能的机位运动` |
| `ambience_design` | `房间、公寓、车辆、后台与人群的自然现场声全程存在` |
| `music_arc` | `配乐逐渐推进为充满能量的现代流行曲，在结尾拍达到高潮` |
| `audio_exclusions` | `无字幕、标题、翻译、Logo、水印、UI 元素；对白只以自然声音存在` |
| `vo_tone` | `平静、亲密、不完美，像私密的自我倾诉` |
| `realism_rules` | `准确解剖与自然身体力学，自然眨眼呼吸与表情，真实的头发运动、车辆反射、人群行为与舞台灯光` |
| `ending_directive` | `音乐达到高潮，强光充满画面，切黑` |
| `final_feel` | `一段真实的私人影像日记：平凡的一天在舞台强光中变得值得铭记` |
| `negative_prompts` | `商业广告感，稳定器/无人机/不可能机位，CGI 感，塑料皮肤，美颜滤镜；手部畸形，人物复制，面部扭曲，服装漂移；字幕，标题，屏幕文字，Logo，水印，UI；摄像机入境` |

## 故事时间线（`story_beats`）

```text
[0-4s] 固定机位｜她在阳光充足的韩式公寓醒来，微笑，伸手拿手机。VO 绑定：vo1
[4-8s] 手持 DV 蒙太奇｜快切：扎头发、戴耳环、拿包、穿鞋、冲出门（5 个 insert）。VO 绑定：none
[8-13s] 手持自拍｜豪华保姆车内，窗外是类首尔城市街景；她疲惫但开心。VO 绑定：vo2
[13-17s] 固定/贴拍 insert｜音乐、耳机、饮料、轻点的运动鞋、城市倒影；自然车辆声。VO 绑定：none
[17-22s] 后台蒙太奇｜快切：工作人员、化妆、发型、服装、闪烁的舞台灯；她在镜前停下深呼吸。VO 绑定：vo3
[22-26s] 手持跟拍｜她穿过昏暗走廊走向明亮的舞台，人群声渐起；她转身露出自信微笑。VO 绑定：none
[26-30s] 大全景+特写｜舞台揭晓，数千观众灯海、演唱会灯光与烟雾；特写她看向镜头。VO 绑定：vo4
```

## 旁白脚本（`voiceover_script`）

```text
vo1（0-4s）：Some days start before I'm ready for them.
vo2（8-13s）：I spend so much of my life moving… sometimes the road feels more familiar than home.
vo3（17-22s）：And then… everything happens at once.
vo4（26-30s）：This moment… is why I keep going.
```

## 渲染与投递

- VO 为英文原句，投递英文模型渲染 `main.en.md`；VO 文本逐字保留，不翻译、不改写。
- 自检重点：VO 绑定键 vo1-vo4 全部落在存在的节拍上；无字幕禁令三节齐出；音乐 peak 与结尾切黑对齐。
