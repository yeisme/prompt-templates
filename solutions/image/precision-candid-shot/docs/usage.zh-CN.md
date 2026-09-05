# 使用说明：精调参数化抓拍镜头

## 适用目标

精确复现单张抓拍写真：机位高度（cm）、焦段、占幅比、前景遮挡比、色块百分比、光源方向全部量化，适合参考图与封面的单镜头生产。

## 变量绑定

- 推荐消费方式：Eikona precision-candid 导演技能（`.skills/yeisme/eikona-image/eikona-precision-candid-director`）的 `render_shot.py`，从 `assets/shots/<id>.json` 结构化字段自动生成全部子句并绑定。
- 可选子句（`perspective_clause`、`foreground_sentence`、`light_fill_clause`、`palette_sentence`、`background_sentence`、`fingerprints_sentence`、`tail_clause`）自带标点与前导空格；不使用时绑定为空字符串。
- 手工绑定时保持量化参数原样（cm、%、degrees），不要改写成模糊形容词。

## 渲染与投递

- 规范投递语言为英文（`main.en.md`）；`template-zh-CN.md` 是不参与编译的人工审阅译文。
- 默认画幅 `9:16`，模型 `openai/gpt-5.4-image-2`。

## 审阅

按 manifest tags 管理：`shot:*`、`lens:*`、`light.temperature:*`、`fingerprint:*`；combo 哈希即 spec 版本指纹。
