# 使用说明：杂志封面半脸肖像风格层

## 适用目标

基于参考人物出杂志封面级高端肖像的可复用风格层。核心：恰好半脸的纵向中线切割、人物贴右侧、左侧大面积留白放宣传语与签名、可见毛孔发丝的真实质感。只换人物印象与文案，风格段固定。目标消费者为 Eikona 图像生成（参考图输入 + 正/负向提示词投递）。

## 变量绑定

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `persona` | 是 | 参考人物印象一句，如 “platinum pale-blonde hair with a light airy fringe, pale irises, fair skin, soft refined makeup, a quiet poised expression, gold star hair ornaments with pearl chains, wearing a soft light knit sweater” |
| `slogan` | 是 | 宣传语原文，逐字渲染，如 “Platinum Poise, Gilded Gaze.”；换人物时可按人物视觉印象重写（日语或英语） |
| `signature` | 是 | 签名原文，逐字渲染（含括号与符号），如 「[ SOPHIA AU ]」；即 「【在此输入签名】」 占位符的替换值 |
| `format_clause` | 否 | 画幅前缀，如 “Vertical 3:4 ”；不用则空字符串 |

## 渲染与投递

- 渲染结果是最终 Prompt 正文，连同参考图一起投递图像模型；负面提示词已在正文尾部 “Negative prompt:” 段内。
- 签名与宣传语都要求逐字精确：投递后先检查画面文字是否与绑定值一致，再决定接受。

## 审阅

对照自检清单：半脸切割是否沿中线、人物是否贴右、头顶发型是否入画、左侧留白是否干净、签名是否逐字精确、皮肤是否有真实肌理、是否只有宣传语与签名两处文字。
