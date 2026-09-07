## 为什么

官方仓已有视频与图像方案采用英文投递，但部分新方案仍同时注册中英文模板和 contract。中文审阅文档与 Agent 正文没有稳定边界。

## 变更内容

- repository default locale 改为 `en`。
- 九个未发布方案只注册英文模板与英文 contract。
- 中文正文迁入 `docs/template-zh-CN.md`，保留中文 catalog 显示文案。
- 更新 authoring、i18n、发行和消费文档。
- 已发布旧双语方案不原地删除。

## 影响

catalog schema 不变；catalog digest 随未发布内容 metadata 更新。Graph Kit 与 UI review 等专用结构按例外单独管理。
