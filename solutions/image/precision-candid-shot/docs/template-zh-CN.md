> 人工审阅译文。编译与 Agent 投递以 `../prompts/main.en.md` 为准；本文件不注册为模板、不进入 catalog，也不参与编译。

# 精调参数化抓拍镜头

本模板生成一条单镜头精调抓拍 Prompt。与随机矩阵包的区别：本包不做采样，每个变量由 shot spec（JSON）精确绑定，量化参数（cm、百分比、角度）直接进正文。消费方在渲染前完成全部变量绑定；渲染结果是最终 Prompt 正文，不经过二次改写。

正文的规范投递语言为英文（`main.en.md`），本文档是人工审阅译文，不进入编译。

## 槽位约定

可选子句变量（`perspective_clause`、`foreground_sentence`、`light_fill_clause`、`palette_sentence`、`background_sentence`、`fingerprints_sentence`、`tail_clause`）自带标点与前导空格；不使用时绑定为空字符串，对应内容整段消失。

{{orientation}} {{aspect}} candid lifestyle photo, {{subject_description}} {{pose}} with {{expression}}.
{{pronoun}} wears {{wardrobe}}.
{{camera_position_clause}}, {{lens}} lens{{perspective_clause}}, {{framing}}.{{foreground_sentence}}
{{light_key}}{{light_fill_clause}}.{{palette_sentence}}{{background_sentence}}{{fingerprints_sentence}}
{{quality}}, {{atmosphere}}, {{negatives}}{{tail_clause}}.

## 自检清单

- 量化参数（cm、%、degrees）原样保留，未被改写成模糊形容词。
- 色块百分比合计 100 且按降序排列（如使用 `palette_sentence`）。
- 前景遮挡带百分比（如使用 `foreground_sentence`）。
- 负向词齐全，无棚拍词汇混入。
