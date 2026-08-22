# Yeisme 官方提示词方案库

这是面向中文用户的官方 Prompt 解决方案目录。内容按“用户要完成什么”组织，而不是按模型或供应商堆放。

首版提供十二个导航类目：通用处理、写作与内容、图像与视觉、视频与短剧、音频与语音、研究与分析、产品与设计、营销与电商、办公与知识、编程与工程、Agent 与自动化、学习与教育。

## 使用

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

首批 12 个方案标记为 `exploratory`：目录结构、双语合同与 digest 已验证，但不会因为“官方维护”就冒充已经完成真实模型或生产场景评测。通过 fixture、人工 review 和已知失败记录后，再逐项提升为 `first-support`。

## 内容结构

每个 solution 至少包含：

- 中文标题、摘要、使用方式和主 Prompt；
- job、artifact、scenario、modality、constraint 等稳定 tags；
- provider-neutral capabilities；
- rights、maturity、已知失败和评审要求；
- 英文同步适配及 freshness 关系。

维护方法见 [docs/README.md](docs/README.md)。
