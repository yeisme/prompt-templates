# southern-gothic-style-beta 使用指南

美国南部哥特（Southern Gothic）完整风格包：优雅与腐烂并存的褪色旧日荣光，在繁茂自然、宗教象征与缓慢腐烂中藏着暴力、罪恶与秘密。适用于绘画/摄影/AI 生图；风格段固定，只换场景、人物与可选主题句。

## 何时用本模板

- 要生成南部哥特风格化的图像：老宅、沼泽、传教士、寡妇、旧南方家族、怪诞边缘人物。
- 要完整呈现"怪诞之美"（grotesque elegance）与强明暗反差的南方光线，不限纪实摄影。

何时不该用（重要边界）：

- 要**安静纪实摄影**滤镜——柔和阴天光、无笑容素装家庭、绝不奇观化 → 用 `southern-gothic-documentary`（同 scenario 的 restrained 姊妹篇）。
- 要**新英格兰小镇**哥特纪实 → `new-england-gothic-documentary`。
- 要东方仙侠氤氲风格层 → `xianxia-hazy-fantasy`。
- 视频镜头提示词编译 → `video-prompt-optimization-beta`，把本模板的关键词段填入其 `style_requirements` 变量联动。

## 输入变量

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `setting` | 是 | 场景：沼泽边褪色的维多利亚庄园、小镇教堂墓地、棉田尽头的木板屋…… |
| `subjects` | 否 | 人物及动作；留空生成空景/静物。人物自带风格段气质（庄重怪诞、道德矛盾），只写身份与姿态 |
| `format_clause` | 否 | 媒介/画幅/相机前缀：`Photorealistic 35mm photograph,` / `Oil painting on canvas,` / `Cinematic 2.39:1 film still,` / `Vintage tintype look,` |
| `theme_clause` | 否 | 主题强化句（句首带空格或逗号）：`, family secrets and inherited sin hanging over the scene` / `, a funeral gathering after the storm` |

## 风格段的固化内容（不可改写）

总气质（优雅的腐烂/宁静下的危险）→ 自然（繁盛到腐败）→ 人物（怪诞之美）→ 色彩（褪色土地色系）→ 光线（强明暗反差的压抑南方光）→ 材质（时间侵蚀）→ 关键词串 → Negative prompt（排除欧洲哥特陈词、超自然怪物、恐怖刻奇、糖水色、现代干净物件）。

主题层（家族秘密、宗教狂热、罪与救赎、死亡、贫困、种族历史、阶级、孤独、暴力、被压抑的欲望）不写死在风格段——经 `theme_clause` 按需注入，保持风格层的通用性。

## 消费方式

Exact ref：

```text
promptrepo://official/image/southern-gothic-style-beta@1.0.0-beta.1?locale=en
```

出图执行交 Eikona（`yeisme-eikona-cli-runtime`）；本模板只产出提示词正文。
