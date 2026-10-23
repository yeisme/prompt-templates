# video-prompt-optimization-beta

模型无关的视频提示词编译模板：把粗略分镜/故事概要编译成一条可直接提交的专业提示词正文，适用于扩散类音视频联合生成模型。固化的方法论来自 Scaena 生产链路：正向排除（否定卡）、静默镜声源纪律（声音卡）、器物与反射规则（器物卡）、参考素材指代协议（按目标平台声明）、设定档案先行、时长与逐句语速核算、180° 轴线与六层镜头结构、出片前自检。参考素材指代语法、时长上限、素材互斥等平台差异全部通过变量声明，不固化任何单家模型协议。

- 编译模板（Agent/模型消费）：`../prompts/main.en.md`
- 中文阅读版（人工审阅，不进编译）：`template-zh-CN.md`
- 使用指南：`usage.zh-CN.md`
- 评审清单：`review-checklist.zh-CN.md`
- 已知失败模式：`failure-modes.zh-CN.md`
- 绑定实例：`../examples/bank-card-relay.zh-CN.md`

Exact ref：

```text
promptrepo://official/video/video-prompt-optimization-beta@1.0.0-beta.1?locale=en
```

家族边界：变量值齐全的蓄力大招渲染走 `ai-drama-shot-video-generation`；运镜/布光技术选型走 `cinematique-shot-techniques-beta`。提交参数确认、生成执行与出片验收归 Scaena 生成/验证层，不在本模板。
