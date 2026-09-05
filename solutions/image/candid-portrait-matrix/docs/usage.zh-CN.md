# 使用说明：真实生活摄影抓拍写真（随机矩阵）

## 适用目标

批量生成互不重复的夏日抓拍写真候选图，强调非常规机位、前景遮挡与偶然抓拍感；也支持单图手工绑定。

## 变量绑定

- 全部 12 个维度变量（`expression` / `wardrobe` / `scene` / `moment` / `shot` / `lens` / `camera` / `composition` / `foreground` / `light` / `palette` / `state`）必须从 contract 枚举池取值。
- `subject` 为自由文本，但必须写明 adult 与镜头感。
- 推荐消费方式：Eikona candid-photo 导演技能的采样器（`.skills/yeisme/eikona-image/eikona-candid-photo-director`）按 seed 确定性采样、校验兼容约束并输出 tags；不要手工编造组合。

## 渲染与投递

- 渲染结果是最终 Prompt 正文，直接投递图像模型，不做二次改写。
- 默认画幅 `9:16`，模型 `openai/gpt-5.4-image-2`。

## 审阅

按批次 manifest 的 tags 筛选淘汰方向；淘汰后用同 seed + 新 exclude 重采，或换 seed。
