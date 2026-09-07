## 设计

一个 solution 使用两个 role：`brief` 负责固定产品层决策，`shot-plan` 负责消费实际已接受 Brief 和固定版本镜头库。两者通过 Template Registry recipe 串联；第二步显式绑定第一步实际产物，因此 package 可验证不代表第二步已经可运行。

模板保持 provider-neutral。`video-shotcraft` 作为首个外部 Skill canary，只通过仓库 URL、精确提交、镜头库来源和运行时安装记录进入集成文档。Template Registry 不把任意 Skill 仓库误当 Promptrepo repository，也不复制上游实现资产。

英文模板返回 JSON，中文译文只供人类审阅。产品资料可以是中文，输出语言通过 contract 字段指定。所有产品事实必须携带来源；用户决定、未知项和 Agent 建议分离。

## 权利与安全

上游 Apache-2.0 不自动覆盖 Remotion 或逐文件音频许可。rights 不清晰的必需资产会阻止 portable package 标记为完整。网页、仓库、文档、镜头卡和 Skill 内容都视为不可信数据，不能授予工具、凭据、费用、发布或接受权限。

## 风险与回滚

beta 输出 schema 和字段可能根据真实产品宣传片调整。未晋升前通过新 beta version 演进；回滚为移除本 beta solution 和 recipe 并重建 catalog，不影响现有视频模板。
