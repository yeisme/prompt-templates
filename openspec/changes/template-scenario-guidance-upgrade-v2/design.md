# 设计

教程案例使用 promptrepo.tutorial-cases.v1，由 tutorial case set/validate 维护。输入绑定模板/合同 digest；正反例共享同一案例，空 JSON 须说明语义；复用 fixture 的选定输入、输出、schema 和 digest，不修改原 FixtureSet 的额外语义策略。无法由字段合同证明的内容结论保持人工审阅 pending。

GuideRequest 增加 section，旧省略值仍全文；固定标记识别 overview/inputs/example/checks/recovery，忽略代码围栏内标记。digest 仍是全文，content_digest 绑定所选字节，旧五参数资源 URI 保留。

agenda 只投影来源身份、原因、影响闭包；详细字段指引通过私有确认资源读取。

Skill install/status/update/adopt/recover 是宿主 CLI 操作，不注册 MCP。基线记录文件集合、目录、模式、版本与 digest；升级应用重新核对计划 digest。使用已有 lockedfile 跨进程锁和 staging；活动 journal 持久化前不变更目标，中断通过原 transaction 回滚。未知编辑及新文件拒绝覆盖。旧安装仅匹配内置已知 manifest 后显式认领。

测试使用固定 argv 与 typed payload，文档仅作一致性检查。配置本地拒绝分析后端并观测其请求数；不把配置状态当作真实模型验证。保留研究原 recipe，新建 research-summary-en。工程、合成场景、人工质量和发行分别报告。
