# 使用说明：南部哥特纪实摄影风格层

## 适用目标

美国南方题材、安静纪实摄影方向出图的可复用风格层。核心：南部哥特氛围、湿热衰败、严肃朴素的人物、家族沉默与承继的忧伤、无魅力化无风格化摆拍。只换人物与场景，风格段固定。

## 变量绑定

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `subjects` | 是 | 人物及神态姿态。示例一（少女）：`a teenage girl in a faded pale dress and worn sneakers, solemn expression, awkward posture of adolescence`；示例二（全家福）：`a poor multigenerational white Southern family dressed plainly, serious expressions, no smiles, the grandmother seated in the center, children barefoot` |
| `setting` | 是 | 场景与时刻。示例一（荒地）：`a neglected field behind a small Southern town, tall dry grass, an abandoned swing set, a distant church, humid cloudy afternoon`；示例二（农舍）：`in front of a decaying farmhouse, overgrown yard, rusted farm tools, an old pickup truck, late summer heat` |
| `format_clause` | 否 | 画幅前缀，如 "Vertical 9:16 "；不用则空字符串 |

## 渲染与投递

- 渲染结果是最终 Prompt 正文，直接投递图像模型；默认模型 `openai/gpt-5.4-image-2`。
- 公式：人物 + 场景 + 南部哥特氛围 + 家族沉默/承继忧伤 + 严肃素装无摆拍 + 湿阴天柔光低饱和 + 纪实质感（人物、场景外均已在固定风格段内）。

## 审阅

对照自检清单：湿阴天光与低饱和是否保留、人物是否严肃无笑容无摆拍、皮肤是否原始未修饰、有无恐怖片化/时尚大片化/明信片金光混入、普通生活是否被奇观化。
