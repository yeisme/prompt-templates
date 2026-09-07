## 设计

模板与 Skill 分层：模板把已确认字段编译为 Integration Brief；Skill 负责发现现有资产、向用户追问、调用 Registry、安装和下游交接。多步骤流程继续使用 Promptrepo recipe，不把工具命令嵌入模板作为执行指令。

模板正文只注册 `en`，中文放 `docs/template-zh-CN.md`。三项必填字段是目标、目标产物和模态/操作；上游、下游、约束、持久化、安装和已确认选择可逐步补齐。

输出必须区分 template、Skill、recipe 和 domain execution，最多给出三个下一轮问题，并明确编译、安装、执行和接受是独立状态。

## 风险与回滚

beta 模板可能需要根据真实集成场景调整字段。未晋升前通过新 beta version 演进；回滚为移除本 beta solution 并重建 catalog，不影响已有 exact refs。
