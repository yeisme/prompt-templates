# Yeisme 官方提示词方案库

这是按任务组织的提示词方案库，涵盖写作修订、图像创作、视频与短剧、研究分析等场景。每个方案提供输入说明、输出要求和评审清单。模板以英文供 Agent 编译，配套中文指南和人工审阅译文。

## 开始使用

先查看模板的使用许可。公开可读不代表可自由执行、修改或商用；标记为 `internal` 的内容不能视为已获公开使用授权。视觉探索入门包提供单独的[免费评估许可](solutions/image/visual-exploration-starter-beta/docs/LICENSE.md)，其他模板以各自声明为准。完整说明见 [RIGHTS.md](RIGHTS.md)。

第一次使用可从[视觉探索入门指南](docs/visual-exploration/quickstart.md)开始，了解需要提供什么、如何导出提示包和检查结果。该包仍为 beta，指南说明了可用来源的前提。

### 交给 Agent 安装

> 安装 Yeisme 提示词体系：运行 `curl -fsSL https://raw.githubusercontent.com/yeisme/yeisme-dist/main/install.sh | bash -s template-registry` 安装 CLI，然后 `template-registry prompt skill install --runtime agents --json` 安装 Agent Skills，再登记官方模板库 `template-registry prompt repository add --id official --source github://yeisme/prompt-templates --revision main --trust official --json`（已登记会返回 ALREADY_EXISTS，属正常），最后 `template-registry prompt repository sync --id official --json`。完成后用 `template-registry prompt search --query '<你的需求>' --locale zh-CN --json` 选模板。

Windows 用户可从 [公开二进制发行页](https://github.com/yeisme/yeisme-dist/releases) 下载，CLI 细节见 [Template Registry](https://github.com/yeisme/template-registry)。

模板分为十二类：通用处理、写作与内容、图像与视觉、视频与短剧、音频与语音、研究与分析、产品与设计、营销与电商、办公与知识、编程与工程、Agent 与自动化、学习与教育。

## 使用

你可以通过 Template Registry 搜索、编译和导出提示包，也可以在支持 `promptrepo://` 引用的工具中使用模板。以下是部分模板的精确版本引用：

- `promptrepo://official/writing/revision-assistant@1.0.0?locale=en`：Auctra 与通用文本修订。
- `promptrepo://official/agent/digital-human-persona-system@1.0.0?locale=en`：编译 Digital Human Persona 的 system prompt。
- `promptrepo://official/image/xhs-product-cover-v2@2.0.0?locale=en`：用于产品封面创作，可由 Eikona 使用。
- `promptrepo://official/writing/ai-drama-format-strategy@1.0.0?locale=en` 等 `writing/ai-drama-*@1.0.0` 六件套：AI 做剧任务角色链（形态策略→故事架构→人物引擎→分集规划→场景写作→评审团）。

独立 Agent 用户可使用 [Template Registry](https://github.com/yeisme/template-registry)，通过 CLI 或本地 MCP 导入资料、确认输入、编译和导出提示包，无需安装其他 Yeisme 产品。首批兼容模板及多步骤示例见 [Agent 编译用基础模板（beta）](docs/agent-consumption-beta.md)。

本仓库公开可读不等于全部模板采用开源许可。每个 solution 的 `rights`、contract 的 `license/permissions`、外部资产许可和用户素材权利分别生效，详见 [Repository visibility and content rights](RIGHTS.md)。

在 Sonora 中添加并搜索官方仓库：

```bash
sonora prompt-asset repository add official \
  --source https://github.com/yeisme/prompt-templates \
  --revision main \
  --trust official

sonora prompt-asset repository sync official --agent
sonora prompt-asset catalog search "podcast narration" --locale en --json
```

支持此模板库的工具会根据自身能力筛选可用模板。

使用前请查看具体方案的 `maturity`、已知限制和评审要求。`exploratory` 表示仍处于探索阶段；`first-support` 表示已完成初步验证，不代表适用于所有模型和生产场景。

## 视觉探索入门包（beta）

[三方向视觉探索入门包](solutions/image/visual-exploration-starter-beta/docs/README.md)包含三个公开练习、英文模板、中文指南和复用检查。使用步骤见 [入门指南](docs/visual-exploration/quickstart.md)。该包尚未正式发布，图片效果尚未实测；使用前请确认所用仓库版本是否包含此包。

## AI 做剧模板

- `promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=en`：将剧本片段整理为分镜，提供四类剧型预设和结果检查示例。
- `promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=en`：人物母版、三视图、服装/表情/动作、道具/场景、分镜关键帧和连续性修复 Prompt Bundle。

这些模板提供提示内容与输出要求。实际模型调用和资产生成通过 Scaena、Eikona 等工具完成，费用与生成效果取决于所使用的模型和服务。

## 官方长篇知识图谱套件

`graph/longform.generic.v2` 是适用于 Auctra 的通用长篇知识图谱套件，帮助作者梳理人物、剧情、规则与来源之间的关系。它提供十个面板：
人物关系、分卷架构、权力反噬、阵营群体、后悔责任、伏笔回收、知识边界、连续性、
规则义务和来源缺口。

## 如何选择模板

先看适用任务和输入要求，再确认输出形式、使用许可与已知限制。英文模板可以接收中文资料；最终输出语言以模板支持的输入字段为准。

编译和导出得到的是提示包，后续需由 Agent 或模型处理。请按模板的评审清单检查结果，尤其是资料中的事实、缺失信息和未经确认的内容。

## 更多文档

- [分类与标签](docs/taxonomy.md)
- [模板语言说明](docs/locale-policy.md)
- [内容编写指南](docs/authoring.md)
- [完整文档索引](docs/README.md)
