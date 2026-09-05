# 失败模式：精调参数化抓拍镜头

| 失败模式 | 表现 | 处理 |
| --- | --- | --- |
| 量化参数丢失 | 55cm、68%、45° 被改成 "slightly" | 检查绑定是否原样传递；禁止文学化改写 |
| 语法断裂 | "lips bends forward" 类动词冲突 | pose 改分词形式（bending/lying/turning） |
| 可选段残留 | 空子句留下多余标点或空格 | 子句变量必须自带标点；不用时绑空字符串 |
| 色板溢出 | 百分比合计不为 100 或未降序 | 按 contract 约定修正 palette_sentence |
| 棚拍感 | 均匀布光、无颗粒、磨皮 | 检查 quality/negatives 绑定是否被替换 |
| 直闪不像手机 | 光线柔和均匀 | light_key 必须保留 hard shadows、 pale highlights 等直闪特征 |
