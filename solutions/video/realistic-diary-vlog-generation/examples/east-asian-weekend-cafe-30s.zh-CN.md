# 实例：东亚女性周末咖啡日记（30 秒，Seedance 2.5，1080p，9:16）

本例展示 `realistic-diary-vlog-generation` 绑定为一条「原创东亚女性、真人 vlog 气质」的 30 秒口播日记。人物为虚构原创，不指向任何真实个人或公众人物。身份静帧由 Eikona 生成，投递时按位置引用绑定。

## 结构判断

- 对镜头短口播 + 唇形同步 → 走日记口播流，不用纯环境音或画外 VO。
- 全片同一套外出服，无换装；服装逻辑写「当天不换装」。
- 画幅 9:16、时长 30 秒、分辨率 1080p，对应 Seedance 2.5 HD 竖屏短视频。横屏只需把 `aspect_ratio` 改为 `16:9`。
- `@image1` 全身定妆、`@image2` 自拍脸锁、`@image3` 开场构图。`character_ref` 合同只收一个引用，故填 `@image1`；其余两张写入一致性锁定。

## 变量绑定

| 变量 | 值 |
| --- | --- |
| `provider_banner` | `Made with Seedance 2.5` |
| `footage_style` | `photorealistic personal diary vlog, real smartphone footage, unpolished weekend morning` |
| `duration_s` / `resolution` / `aspect_ratio` | `30` / `1080p` / `9:16` |
| `scenario_summary` | `同一位二十多岁东亚女性记录周末早晨：从公寓厨房出门，走到街角咖啡馆坐一会儿，再走回树荫街道` |
| `subject_identity` | `严格继承 @image1 的面部、发型、体型与气质：二十多岁东亚女性，椭圆脸，自然内双，黑棕微卷中长发与帘式刘海，少许飞发；安静、略害羞、不设防。@image2 锁定自拍口播脸部；@image3 锁定开场厨房自拍构图` |
| `wardrobe_and_accessories` | `燕麦色宽松针织开衫 + 白色圆领棉 T + 中蓝直筒牛仔裤 + 无品牌白低帮运动鞋；左肩米白帆布托特，细金圈耳环，左手细表。全片不换装` |
| `consistency_lock` | `全片保持 @image1 的确切面部、发型、体型与服装；口播拍对齐 @image2；开场构图对齐 @image3。无面部漂移、无换人、无无故换装` |
| `character_ref` | `@image1` |
| `camera_formats` | `手持自拍 + 亲密朋友手持跟拍 + 咖啡馆自然固定机位` |
| `camera_imperfections` | `手持手机轻微晃动、随意构图、小幅失焦、窗光曝光不均、自然停顿与呼吸` |
| `camera_exclusions` | `无商业摆拍、glamour 广告打光、稳定器、无人机、不可能机位、镜面穿帮` |
| `dialogue_language` | `自然普通话口语，轻声、像对朋友说话，不播音` |
| `ambience_design` | `现场原生声：公寓厨房近距安静与水壶底噪，楼道脚步与关门，咖啡馆杯盘与低声交谈，窗外树荫街道的风与远处车流；room tone 全程存在，声学空间随地点切换` |
| `audio_exclusions` | `无配乐、罐头音效、播音腔、字幕、屏幕文字、Logo、水印` |
| `realism_rules` | `准确解剖与自然身体力学，可信唇形同步，自然眨眼呼吸与表情，真实头发与织物运动；无面部漂移、人物复制、塑料皮肤、手部畸形、悬浮道具` |
| `ending_directive` | `她端着杯子走出咖啡馆，回头看镜头，手持跟拍自然结束，不切黑场` |
| `final_feel` | `一段真实的私人周末早晨：亲密、随意、不完美，像后来舍不得删的手机录像` |
| `negative_prompts` | `商业摆拍，glamour 打光，精致广告质感，稳定器/无人机；面部漂移，人物复制，塑料皮肤，手部畸形，无故换装；唇形不匹配，播音腔；字幕，标题，屏幕文字，Logo，水印；摄像机机身入境，镜面穿帮；品牌，地标，可读招牌` |

## 日记时间线（`story_beats`）

```text
[0-6s] 公寓厨房（近距安静）｜手持自拍｜她看着镜头，拿起可复用咖啡杯，开始录。台词：d1
[6-12s] 公寓门厅→楼道（室内安静）｜朋友手持跟拍｜她挎上托特包，开门下楼往外走。台词：none
[12-20s] 街角咖啡馆（室内嘈杂）｜跟拍进门后切窗边固定机位｜她点单、坐到窗边、揭开杯盖看窗外。台词：none
[20-26s] 咖啡馆座位（近距嘈杂）｜手持自拍｜她对镜头短说一句，喝一小口。台词：d2
[26-30s] 咖啡馆外树荫街道（开阔）｜朋友手持跟拍后拉｜她端杯走出来，回头看镜头，录制自然结束。台词：none
```

## 出镜台词（`dialogue_script`）

```text
d1（0-6s）：早。我先出门买杯咖啡。
d2（20-26s）：周末早上这样待一会儿，挺好的。
```

## 渲染与投递

- 模板 ref：`promptrepo://official/video/realistic-diary-vlog-generation@1.0.0?locale=en`
- Seedance 2.5：`duration=30`，`ratio=9:16`，`resolution=1080p`，任务意图 `reference`（非纯 text）。
- 资产槽位：`@image1` 全身定妆，`@image2` 自拍脸锁，`@image3` 9:16 开场帧；可选把 `@image3` 同时作为 first_frame。
- 自检重点：口播拍 2/5，符合偶尔自述；d1/d2 全部落在口播拍；全片不换装；无字幕禁令三节齐出；声学空间按厨房/楼道/咖啡馆/街道切换。
- 原生音频写入 Prompt，仅作样片/口型参考；生产默认仍是生成后替换，除非声音权利、逐句审听与可编辑性证据齐全。
