# 使用说明：修仙朦胧风风格层

## 适用目标

修仙、仙侠、玄幻人物出图的可复用风格层。核心：柔雾、低饱和、逆光、半透明材质、古典东方建筑、克制情绪。只换人物与场景，风格段固定。

## 变量绑定

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `persona` | 是 | 人物身份，如 "A white-robed sword immortal"、"A demon lord in dark robes" |
| `scene` | 是 | 修仙场景，如 "amid a peach-blossom hidden realm"、"above a cloud-sea immortal sect" |
| `reference_mist_block` | 否 | 贴近柔雾参考图时绑入增强段（英文见 contract 示例），否则空字符串 |
| `format_clause` | 否 | 画幅前缀，如 "Vertical 9:16 "；不用则空字符串 |

## 渲染与投递

- 渲染结果是最终 Prompt 正文，直接投递图像模型；默认模型 `openai/gpt-5.4-image-2`。
- 公式：人物身份 + 修仙场景 + 飘逸古装 + 含蓄神态 + 云雾 + 逆光 + 柔焦 + 低饱和月白雾金配色 + 浅景深 + 中国仙侠电影感（后七项已在固定风格段内）。

## 审阅

对照自检清单：低饱和、逆光、柔雾、克制情绪是否保留；人物是否摆拍感；有没有霓虹色/硬光/高反差混入。
