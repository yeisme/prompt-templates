# Yeisme 官方提示词方案库

这是面向中文用户的官方 Prompt 解决方案目录。内容按“用户要完成什么”组织，而不是按模型或供应商堆放。

首版提供十二个导航类目：通用处理、写作与内容、图像与视觉、视频与短剧、音频与语音、研究与分析、产品与设计、营销与电商、办公与知识、编程与工程、Agent 与自动化、学习与教育。

## 使用

独立 Agent 用户可使用 [Template Registry](https://github.com/yeisme/template-registry)，通过 CLI 或本地 MCP 导入资料、确认输入、编译和导出提示包，无需安装其他 Yeisme 产品。首批兼容模板及多步骤示例见 [Agent 编译用基础模板 v2](docs/agent-consumption-v2.md)。

在 Sonora 中添加并搜索官方仓库：

```bash
sonora prompt-asset repository add official \
  --source github://yeisme/prompt-templates \
  --revision main \
  --trust official

sonora prompt-asset repository sync official --agent
sonora prompt-asset catalog search "中文播客旁白" --locale zh-CN --json
```

其他 Yeisme CLI 使用相同 `promptrepo://` 引用与用户级 RepositoryProfile，只应用自己的领域兼容性过滤。

基础目录的 12 个方案和后续新增的 AI 做剧方案默认标记为 `exploratory`：目录结构、合同与 digest 已验证，但不会因为“官方维护”就冒充已经完成真实模型或生产场景评测。通过 fixture、人工 review 和已知失败记录后，再逐项提升为 `first-support`。

## AI 做剧模板

- `promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=zh-CN`：四类剧型预设、剧本 segments 到导演语义分镜、一次有界修复和 valid/invalid fixtures。
- `promptrepo://official/video/ai-drama-character-assets@1.0.0?locale=zh-CN`：人物母版、三视图、服装/表情/动作、道具/场景、分镜关键帧和连续性修复 Prompt Bundle。

两者只提供 provider-free inspect/render/preview 内容和合同。实际模型调用、费用批准、资产接受与交付仍由 Scaena、Eikona 等领域 owner 负责。

## 官方长篇知识图谱套件

`graph/longform.generic.v2` 是 Auctra 的通用长篇 Graph Kit：一个 immutable
structured closure，包含 manifest、source adapter、lens、view、validator 五个
角色，以及 schema、compiler profile 和九类安全/迁移 fixture。它声明十个面板：
人物关系、分卷架构、权力反噬、阵营群体、后悔责任、伏笔回收、知识边界、连续性、
规则义务和来源缺口。

当前本地 canary 已由 Template Registry CLI 完成 validate/release/restore，maturity
为 `first-support`；exact release/closure/tree digest 记录在 Registry 的
`docs/operations.md` 与 `openspec/changes/official-longform-graph-kit-v1/tasks.md`。
此仓库只保存通用模板，不保存《逆誓龙王》项目源文件、Overlay、投影或运行证据。

## 内容结构

每个 solution 至少包含：

- 中文标题、摘要、使用方式和主 Prompt；
- job、artifact、scenario、modality、constraint 等稳定 tags；
- provider-neutral capabilities；
- rights、maturity、已知失败和评审要求；
- 英文同步适配及 freshness 关系。

首批 `TemplateContract` pilot 已覆盖 `image/xhs-product-cover` 与 `audio/podcast-narration` 的 zh-CN/en 模板。结构化 sidecar 必须由 Template Registry CLI 维护：

```bash
template-registry contract validate --repository . --package image --id xhs-product-cover --role main --locale zh-CN --json
template-registry contract validate --repository . --package image --id xhs-product-cover --role main --locale en --json
template-registry contract validate --repository . --package audio --id podcast-narration --role main --locale zh-CN --json
template-registry contract validate --repository . --package audio --id podcast-narration --role main --locale en --json
template-registry catalog validate --repository . --json
```

sidecar 只声明字段、license、permission 和 digest，不包含真实用户值，也不授予 Eikona 或其他 Provider 执行权限。

验证 AI 做剧中文模板：

```bash
template-registry contract validate --repository . --package video --id ai-drama-storyboard-breakdown --role main --locale zh-CN --json
template-registry fixture validate --repository . --package video --id ai-drama-storyboard-breakdown --role main --locale zh-CN --validator-command-ref scaena.storyboard.semantic-plan.v1 --json
template-registry contract validate --repository . --package video --id ai-drama-character-assets --role main --locale zh-CN --json
template-registry fixture validate --repository . --package video --id ai-drama-character-assets --role main --locale zh-CN --validator-command-ref eikona.character-asset.prompt-bundle.v1 --json
template-registry catalog validate --repository . --json
```

维护方法见 [docs/README.md](docs/README.md)。
