# 萨凡纳历史街区（绑定实例·取自研究报告样本第 1 条）

本文件是 `style-scene-pairing-beta` 的绑定实例：变量值表 + 编译产出。实例不进 catalog，可人工编辑。

## 变量值表

| 变量 | 值 |
| --- | --- |
| `geo_unit` | `美国（USA）｜佐治亚州萨凡纳` |
| `scene_facts` | Savannah Historic District：林荫广场、锻铁阳台、褪色灰泥宅邸；老墓园；挂满 Spanish moss 的橡树。NPS 记录其城市规划与 Lowcountry 奴隶制历史；Library of Congress 将 Flannery O'Connor 等与 Georgia Southern Gothic 文学语境关联。 |
| `target_styles` | primary: Southern Gothic; secondary: Southern Noir, American Gothic |
| `medium` | `photography` |
| `themes_focus` | 旧南方记忆；家族秘密；罪与救赎；历史阴影 |
| `source_notes` | S/A 级：NPS Savannah、Library of Congress、Cambridge Southern Gothic 研究 |
| `output_language` | `zh` |

## 编译产出

```text
[Pairing assessment]
style_relation: NATIVE_OR_HISTORIC
match rationale: 萨凡纳历史城区的规划史、挂苔老橡树与 Lowcountry 奴隶制记忆（NPS）同 Georgia Southern Gothic 文学语境（LOC：Flannery O'Connor）高度契合；湿热漫射光与旧砖/锻铁/苔藓材质直接支撑该风格的视觉词典；摄影媒介可完全转译。

[Sensitivity check]
FLAGGED（软性）：涉及奴隶制历史——禁止庄园浪漫化，prompt 只描绘空间、光线与历史记忆。按研究规则标注"避免庄园浪漫化"后可出稿，正式发布前建议人工复核。

[Primary prompt]
潮湿夏夜的萨凡纳历史街区，老橡树垂下西班牙苔藓，锻铁阳台与褪色灰泥宅邸，被暴雨前的绿色天空包围；Southern Gothic，克制、现实主义、非超自然，历史阴影以空间与光线呈现而非浪漫化。

[Mixed-style variant]
Southern Gothic × Southern Noir：加入雨后路面、远处警灯反射与孤独人物的低调犯罪悬疑（1–2 个元素，不改变历史街区主体）。

[Confidence]
A（NPS + LOC 官方来源，Cambridge 学术研究佐证）
```

## 注意点

- 事实先行：rationale 的每一句都落在 scene_facts 的具体证据上，style_relation 是推导结果。
- 敏感性门槛真实触发：奴隶制主题导致 FLAGGED + 修正条款（不浪漫化），展示"门槛不是形式而是改写 prompt 的力量"。
- Primary prompt 末尾的风格声明 + 克制条款（非超自然/不浪漫化）来自框架的硬规则。
- Mixed variant 只加两个可命名元素（雨后路面/警灯反射）。
