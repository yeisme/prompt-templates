## 目录

Agent solution 使用 `prompts/<role>.en.md`、`contracts/<role>.en.json` 和 `docs/template-zh-CN.md`。中文文档必须有 review-only notice，并保持变量集合、约束与输出结构等价。

## Metadata

使用 `solution locale remove` 移除未发布中文 template binding，再用 `solution locale describe` 恢复中文显示文本。`repository locale set` 修改仓库默认值；catalog 由 CLI 重建。

## 兼容

只迁移 origin/main 尚不存在的九个方案：三个 Agent 编译 beta 基础模板、文本修订、数字人 Persona 与四个图像方案。已发布旧双语版本保留 exact ref，后续新版本采用统一结构。

## 验证

检查九个 solution 的 template locale 只有 `en`、中文文档存在、中文 contract 不存在，并运行 catalog build/validate 与 Registry official conformance。
