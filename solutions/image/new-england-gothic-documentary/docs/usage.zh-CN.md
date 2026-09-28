# 使用说明：新英格兰哥特纪实摄影风格层

## 适用目标

美国小镇夜间题材、安静纪实摄影方向出图的可复用风格层。核心：环境纪实、新英格兰哥特氛围、大片空与暗、现场可用光、克制构图、孤独而非戏剧化、可信而非风格化。只换人物与场景，风格段固定。

## 变量绑定

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `subjects` | 是 | 画面中的人物及动作，如 "two ordinary middle-aged graffiti writers quietly working on a weathered brick wall, one standing and one crouching, worn work clothes, subtle spray-paint stains" |
| `setting` | 是 | 场景与时刻，如 "small industrial town in Vermont, pre-dawn October night, nearly deserted back street, old red-brick warehouses, wet cracked asphalt reflecting one sodium streetlight, dark wooded hills in the distance, faint church steeple" |
| `format_clause` | 否 | 画幅前缀，如 "Vertical 9:16 "；不用则空字符串 |

## 渲染与投递

- 渲染结果是最终 Prompt 正文，直接投递图像模型；默认模型 `openai/gpt-5.4-image-2`。
- 公式：人物 + 场景 + 环境纪实 + 新英格兰哥特氛围 + 空街与黑暗 + 小主体远景观察 + 可用光深阴影 + 炭灰/砖红/冷蓝色调 + 35mm 胶片颗粒（人物、场景外均已在固定风格段内）。

## 审阅

对照自检清单：空旷与黑暗是否保留、是否现场可用光、主体是否小而不摆拍、有无霓虹/人群/HDR 混入、情绪是否孤独克制而非戏剧化。
