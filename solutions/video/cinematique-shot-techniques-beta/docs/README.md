# Cinematique Shot Technique Prompts（beta）

150 条电影拍摄技术提示词库，来自 vvsvs.pro/cinematique（Free Tool — Open Source；上游 grokfilm.app by Tetsuo Corp，VVSVS 混编扩充）。每条技术包含：运镜/布光/构图/剪辑/叙事/特效/风格分类、难度、mood、影史摘要、`[Subject]` 占位的提示词模板、适用时机、AI 执导要点、常见错误与关联技术。

## 结构

```text
assets/techniques/<id>.json   150 条技术 spec（人工可编辑源内容）
assets/index.json             由 scripts/cinematique_reindex.py 生成的索引（禁止手写）
prompts/main.en.md            唯一注册模板（Agent 编译正文）
contracts/main.en.json        CLI 生成合同（7 输入，technique_id 为 150 值 enum）
docs/                         人类审阅文档（中文）+ 来源与授权
examples/                     绑定实例
```

## 一句话用法

分镜或镜头生成阶段，按叙事意图选一条技术（`assets/index.json` + spec 的 `when_to_use`/`common_mistakes` 做选型护栏），把 spec `prompt_template` 中的 `[Subject]` 替换为具体主体后作为 `technique_prompt_bound` 绑定，渲染投递图像/视频模型。详见 `docs/usage.zh-CN.md`。

## 状态

- 版本 `1.0.0-beta.1`；未经真实剧集生产验证，转正需一次完整分镜→出图/出片回执。
- rights `external-attributed`；再分发边界见 `docs/provenance.zh-CN.md`。
