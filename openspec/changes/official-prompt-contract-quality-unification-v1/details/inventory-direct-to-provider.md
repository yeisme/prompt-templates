# Direct-to-provider 模板盘点（task 3.1，2026-09-07 凌晨波）

## 分类（按 2026-09-07 内容仓现状扫描）

| 类别 | solutions | 判定依据 |
| --- | --- | --- |
| **provider-direct 正文**（输出即发 Provider） | `image/`：candid-portrait-matrix、iconic-landmark-poster、precision-candid-shot、xhs-product-cover、xhs-product-cover-v2（5）；`video/`：ai-drama-* 系列 11 + ai-film-multi-profile-production（12）；`audio/`：podcast-narration（1） | 正文为生成指令/画面/分镜/音频描述，consumer 拿走即投喂生成平台 |
| 纯文本产出 | `general/`×2、`office/`×2、`research/`×2、`engineering/`×1、`product/`×1、`learning/`×1、`agent/`×2、`graph/`×1、`writing/`×8 | 输出为文档/分析/文案，人消费或下游工具消费 |

扫描方式：包/solution 清单 + 正文平台关键词全库 grep（suno/fish audio/midjourney/即梦/可灵/veo 等，0 命中——当前正文均 provider-neutral 表述，直投属性来自包职责而非平台绑定）。

## 首批 additive delivery roles（建议）

按「已有多 role 结构、正文最稳定、消费方明确」选首批 3 个：

1. **`image/candid-portrait-matrix`** → 新增 `delivery` role（复用 main 意图与 companion contract）
2. **`image/xhs-product-cover`**（取 v2 为源，v1 保持只读快照）→ 同上
3. **`audio/podcast-narration`** → 同上

暂不入选：`video/ai-drama-*`（量大且 storyboard/asset 演进活跃，随 film role 统一波一起做）；`writing/ai-drama-*`（正文仍纯文本产出）。

## 3.2 分离口径（给下一批执行者）

对首批每个 solution：authoring guide（变量说明/维护者提示）与 validation policy（确定性检查/人工 review）留在 main role 文档；delivery body 成为独立 role 的唯一正文（唯一允许发送给 Provider 的部分）；复用同一 source intent + companion contract，禁止运行时按 Markdown 标题裁剪；每 solution 补最小回归 fixture（1 valid + 1 invalid）。
