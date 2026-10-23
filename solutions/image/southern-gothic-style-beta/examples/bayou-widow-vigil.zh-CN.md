# 沼泽庄园守灵（绑定实例）

本文件是 `southern-gothic-style-beta` 的绑定实例：变量值表 + 渲染要点。实例不进 catalog，可人工编辑。

## 变量值表

| 变量 | 值 |
| --- | --- |
| `format_clause` | `Photorealistic 35mm photograph, faded film stock,` |
| `setting` | a decayed Victorian plantation house sinking into bayou wetlands at dusk, Spanish moss hanging from dead oaks, a rusted pickup abandoned in the overgrown drive, gravestones visible beyond the fence |
| `subjects` | A widow in her sixties standing on the sagging porch, holding a worn Bible, black lace dress damp with humid heat, gaze fixed on the water |
| `theme_clause` | `, a vigil kept for a husband the town never speaks of, inherited sin and quiet judgment hanging over the scene` |

## 渲染要点

- setting 提供了 4 个衰败锚点（庄园、苔藓、锈皮卡、墓地），材质段与色彩段围绕它们展开；不再额外堆形容词。
- subjects 只写身份+持物+视线（寡妇/旧圣经/望向水面），庄重与不安由风格段的人物气质行接管；黑色蕾丝裙与"潮湿"呼应材质段的 sweat/humidity。
- theme_clause 注入主题层（守灵/不被谈论的丈夫/继承的罪），把"家族秘密"落成一句可渲染的场面事实，而非抽象词。
- format_clause 的 faded film stock 与色彩段的"晒褪色胶片"互证，压住模型输出糖水色的先验。
- 预期 negative 生效位：无古堡/吸血鬼（欧洲哥特排除）、无 glamour（寡妇不被美颜）、无 HDR 黄金光（黄昏是暴风雨前的阴沉而非讨好的金色）。
