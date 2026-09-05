# 使用说明：ICONIC LANDMARK SERIES 城市地标海报

## 适用目标

以固定视觉系统批量扩展城市地标海报/封面系列：上半真实摄影、下半极简矢量解构、建筑档案排版，系列内所有城市共享同一套版式与风格栈。

## 变量绑定

- 33 个变量全部由城市 spec 注入；推荐消费方式为 Eikona iconic-landmark 海报导演技能（`.skills/yeisme/eikona-image/eikona-iconic-landmark-poster-director`）的 `render_poster.py`，直接从 `assets/cities/<id>.json` 渲染，支持 variants 变体合并。
- `series_no` 全系列唯一，三位数字（如 `001`）；新增城市后运行 `render_poster.py --reindex` 检查冲突。
- `negative_extra` 只放城市专属负面词，固定基线已在模板内。

## 渲染与投递

- 渲染结果是最终 Prompt 正文，直接投递图像模型。默认画幅 `2:3`，模型 `openai/gpt-5.4-image-2`。

## 审阅

按 manifest tags 管理：`series.no` 定位系列位置，`variant:*` 区分基础版与封面变体，`palette.accent:*` 做跨城色彩一致性审查。
