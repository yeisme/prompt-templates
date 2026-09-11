# 分类与标签

## 十三类导航

| ID | 中文名称 | 典型任务 |
| --- | --- | --- |
| `general` | 通用处理 | 总结、提取、改写、翻译、比较 |
| `writing` | 写作与内容 | 文章、小说、剧本、文案、世界观 |
| `image` | 图像与视觉 | 生图、编辑、封面、海报、角色设定 |
| `video` | 视频与短剧 | 分镜、连续性、镜头、图生视频 |
| `audio` | 音频与语音 | 配音、播客、字幕、声音设计 |
| `research` | 研究与分析 | 调研、证据、竞品、报告 |
| `product` | 产品与设计 | PRD、用户研究、验收、设计评审 |
| `marketing` | 营销与电商 | 小红书、抖音、电商、广告、增长 |
| `office` | 办公与知识 | 邮件、会议、纪要、文档、表格 |
| `engineering` | 编程与工程 | 代码、调试、测试、架构、安全 |
| `agent` | Agent 与自动化 | workflow、tool use、review、handoff |
| `learning` | 学习与教育 | 教学、练习、解释、测验、学习计划 |
| `3d` | 3D 模型与空间资产（beta 试点） | 文生 3D、图生 3D、场景布局、3D 打印约束、资产评审 |

## Namespace tags

官方 tags 使用 `namespace:value`：`category`、`job`、`scenario`、`artifact`、`modality`、`constraint`、`audience`、`platform`、`use`、`workflow`、`locale`、`maturity`、`rights`。ID 使用 ASCII lower snake_case，显示名和别名按 locale 管理。

一个 solution 只有一个 primary category，但可以通过其他 tags 跨入口发现。模型名和 Provider 名只能作为兼容信息，不能成为一级分类。

`solution.capabilities` 是 provider-neutral 粗粒度兼容能力；document descriptor 的 `required_capabilities` 是具体 role 的准入能力。不要再使用 `capability:*` tag 复制同一语义。

```bash
template-registry solution tag set --repository . --package video --id campaign-production --tag job:plan --tag artifact:storyboard --tag modality:video --tag workflow:film-production --json
template-registry solution capability set --repository . --package video --id campaign-production --capability storyboard --capability source_mapping --json
template-registry document capability set --repository . --package video --id campaign-production --role shot-prompt --locale en --capability film_shot_semantics --json
```
