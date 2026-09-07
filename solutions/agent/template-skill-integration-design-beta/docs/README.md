# 模板与 Skill 集成设计（beta）

用于把已确认的多模态需求编译成 Integration Brief。它不执行图片、视频、文档、剪辑或发布操作；实际集成由 `template-registry-integration-designer` Skill 调用 Registry CLI 和领域 owner 完成。

适合：

- 新建或整合模板与 Skill；
- 设计图片、视频、文档、音频、剪辑或多步骤工作流；
- 规划 tags、capabilities、recipe、持久化、编译、安装和交接；
- 在实现前集中列出最多三个关键用户问题。

当前 maturity 为 `exploratory`。需要通过更多真实项目的 provider-free 集成评审后再提升。
