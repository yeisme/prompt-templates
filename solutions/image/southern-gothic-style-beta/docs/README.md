# southern-gothic-style-beta

美国南部哥特（Southern Gothic）完整风格包：优雅与腐烂并存——褪色的旧日荣光，在繁茂自然、宗教象征与缓慢腐烂之中，隐藏着暴力、罪恶与秘密。绘画/摄影/AI 生图通用；风格段固定，只换场景、人物与可选主题句。

- 风格层模板（Agent/模型消费）：`../prompts/main.en.md`
- 中文阅读版（人工审阅，不进编译）：`template-zh-CN.md`
- 使用指南：`usage.zh-CN.md`
- 已知失败模式：`failure-modes.zh-CN.md`
- 绑定实例：`../examples/bayou-widow-vigil.zh-CN.md`

Exact ref：

```text
promptrepo://official/image/southern-gothic-style-beta@1.0.0-beta.1?locale=en
```

家族边界：安静纪实摄影滤镜（柔和阴天光、素装家庭、绝不奇观化）走 `southern-gothic-documentary`；新英格兰小镇哥特走 `new-england-gothic-documentary`。视频侧把本模板关键词段填入 `video-prompt-optimization-beta` 的 `style_requirements` 联动。出图执行交 Eikona，不在本模板。
