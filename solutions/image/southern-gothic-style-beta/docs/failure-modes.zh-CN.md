# southern-gothic-style-beta 已知失败模式

| 症状 | 归因 | 修复 | 不要做 |
| --- | --- | --- | --- |
| 出图变成古堡/吸血鬼/幽灵怪物 | 风格被误读为欧洲哥特 | 检查 setting 是否含南方地标（苔藓/沼泽/庄园/棉田）；negative 段未被裁剪 | 往正文加"不要吸血鬼"式否定句 |
| 变成血腥恐怖片海报 | 怪诞被放大成 splatter | theme_clause 收敛为道德张力而非暴力直给；确认 negative 里 gore 项在位 | 堆更多恐怖关键词求"更哥特" |
| 明快糖水色/高饱和 | 色彩段被模型先验覆盖 | format_clause 加 `Vintage tintype look,` 或 `faded film photograph,` 强化褪色介质 | 加"低饱和"重复词——正文已固化色彩段 |
| 人物变成时尚摆拍/glamour | subjects 写了姿态过强的描述 | subjects 只写身份与静态动作（standing on the porch, holding a worn Bible）；风格段自带庄重气质 | 在 subjects 里写"时尚/性感/自信"类词 |
| 场景太干净、物件崭新 | 材质段未触发 | setting 点名 1–2 个衰败锚点（peeling paint, rusted truck, mold stains） | 只写"a beautiful old house"指望风格段补全 |
| 光线变成黄金时刻大片光 | 模型先验偏爱讨好评 | 光线段已固化压抑明暗；format_clause 避免 golden-hour 字样 | 加 HDR、postcard light 等词 |
| 宗教象征完全消失 | theme_clause 缺失 | 注入 `, religious symbolism: a roadside shrine, hymnals stacked on the porch` | 把宗教元素写死进 setting 每次复用 |
| 风格塌缩成普通乡村照 | 只换了 setting 没绑风格段 | 确认消费方渲染的是完整模板正文而非片段 | 手拼几个关键词当模板用 |
| 空景时残留人物描述痕迹 | subjects 留了占位文本 | subjects 留空（渲染为空景/静物），不要写 "none" | 在 subjects 里写"无人物" |
