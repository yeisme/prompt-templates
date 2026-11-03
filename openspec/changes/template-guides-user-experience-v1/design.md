# 设计

新增可选 GuideReader，不改变 Client 必实现接口。指南固定为 solutions/<package>/<solution>/docs/README.md，按精确 ref/role 解析。指南独立于可编译性。Git 使用固定提交；file/S3 使用内容 digest，读取资源再次校验 revision、snapshot、digest。

Registry guide 返回正文之外的元数据与 resource；CLI --output 显式导出且拒绝覆盖和越界，MCP 使用 resources/read。教程是任务数据，不授予权限。

完整教程由内容 owner 的 author_guides.py 基于实际 contract 维护，保留原说明；check_guides.py 在临时项目中逐个执行合成 CLI 示例，证据不保留正文。

保持旧 schema、会话与编译行为；没有数据迁移。回退新增入口及文档不影响既有消费。SDK 工作区 replace 不代表独立发行验证。
