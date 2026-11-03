<!-- solution-tutorial:start -->
<!-- guide:begin overview global -->
# Auctra 通用长篇知识图谱套件：完整使用教程

面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

## 如何提出需求

适用目标：通过 Auctra Graph Kit 精确引用安装；先 preview/apply，再经 review accept 切换。本教程以“梳理虚构长篇故事”为合成练习，产物是可审阅的提示词或领域交接包。

> 请使用「Auctra 通用长篇知识图谱套件」帮我完成任务。先读取对应版本的完整指南和字段要求，再告诉我需要补充哪些资料。我的练习资料是：林舟只知道旧地址；顾遥知道信件来源但尚未告诉林舟。 请保留已提供信息，集中询问关键选择；编译完成后告诉我产物位置、检查方法和下一步。

## 版本、许可与准备

- 方案：`graph/longform.generic.v2@1.0.0`；成熟度：`first-support`；rights：`internal`。
- 先按仓库[安装说明](../../../../README.md)配置来源。下方命令需要当前源码对应的 CLI、POSIX shell 和 jq；在独立项目目录执行。
- 英文模板可接收中文资料。教程不会修改模板、合同或许可；internal、preview 与 execute_requires_review 各自生效。
- 示例只用于本地编译与人工审阅，不证明模型质量、素材授权或生产可用。真实敏感资料通过 stdin/输入文件传递，不写命令历史。

## 角色与衔接

这是单角色任务：先补齐输入并确认，编译后将提示词交给用户选择的消费方。

多个角色的下方练习各自使用独立会话，不能代替跨角色 recipe。复用工作流时通过 recipe 命令绑定真实前序产物；needs_step_output 必须等待外部结果。

<!-- guide:end -->
## 角色 `lens`

职责：面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

精确引用：`promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN`；role：`lens`。
合同许可：`internal`；permissions：`review`。

<!-- guide:begin inputs lens -->
### 输入字段

历史领域角色按原消费合同交接。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example lens -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'lens' --output 'lens-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'lens' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 领域专用角色

该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN","role":"lens"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks lens -->
### 结果示例与检查

示例目标：Lens。关系与知识状态有文本来源，推测不能当成正史写入。
合成内容示例（供理解输出方向，未运行模型）：知识差异示例：顾遥知道信件来源，林舟只知道旧地址。两条知识声明分别绑定其来源片段，不能自动传播为双方共同知识。
领域接受由原 owner 验证。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/lens.zh-CN.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `manifest`

职责：面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

精确引用：`promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN`；role：`manifest`。
合同许可：`internal`；permissions：`review`。

<!-- guide:begin inputs manifest -->
### 输入字段

历史领域角色按原消费合同交接。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example manifest -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'manifest' --output 'manifest-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'manifest' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 领域专用角色

该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN","role":"manifest"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks manifest -->
### 结果示例与检查

示例目标：Manifest。关系与知识状态有文本来源，推测不能当成正史写入。
输出结构示例见 [dangling-relation.output](../fixtures/manifest.zh-CN/dangling-relation.output.json)、[digest-drift.output](../fixtures/manifest.zh-CN/digest-drift.output.json)、[duplicate-identity.output](../fixtures/manifest.zh-CN/duplicate-identity.output.json)。这些是仓库合成 fixture，不是模型实测结果；逐字段核对对应 schema 和来源。
领域接受由原 owner 验证。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/manifest.zh-CN.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `source_adapter`

职责：面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

精确引用：`promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN`；role：`source_adapter`。
合同许可：`internal`；permissions：`review`。

<!-- guide:begin inputs source_adapter -->
### 输入字段

历史领域角色按原消费合同交接。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example source_adapter -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'source_adapter' --output 'source_adapter-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'source_adapter' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 领域专用角色

该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN","role":"source_adapter"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks source_adapter -->
### 结果示例与检查

示例目标：Source_Adapter。关系与知识状态有文本来源，推测不能当成正史写入。
合成内容示例（供理解输出方向，未运行模型）：知识差异示例：顾遥知道信件来源，林舟只知道旧地址。两条知识声明分别绑定其来源片段，不能自动传播为双方共同知识。
领域接受由原 owner 验证。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/source_adapter.zh-CN.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `validator`

职责：面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

精确引用：`promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN`；role：`validator`。
合同许可：`internal`；permissions：`review`。

<!-- guide:begin inputs validator -->
### 输入字段

历史领域角色按原消费合同交接。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example validator -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'validator' --output 'validator-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'validator' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 领域专用角色

该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN","role":"validator"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks validator -->
### 结果示例与检查

示例目标：Validator。关系与知识状态有文本来源，推测不能当成正史写入。
合成内容示例（供理解输出方向，未运行模型）：知识差异示例：顾遥知道信件来源，林舟只知道旧地址。两条知识声明分别绑定其来源片段，不能自动传播为双方共同知识。
领域接受由原 owner 验证。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/validator.zh-CN.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
## 角色 `view`

职责：面向长篇小说分支规划的五角色精确闭包，覆盖十个知识图谱面板、校验、动态更新与回滚

精确引用：`promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN`；role：`view`。
合同许可：`internal`；permissions：`review`。

<!-- guide:begin inputs view -->
### 输入字段

历史领域角色按原消费合同交接。

| 字段 | 类型／必填 | 说明与来源 | 允许值和约束 | 练习值 |
| --- | --- | --- | --- | --- |

字段名和 enum 值必须保持原样；空字符串不等于缺省值。空对象只允许用于字段说明明确列出的初始状态。引用缺失、枚举拼错、把 JSON 字符串传成对象或把建议当成事实，都应先修正再确认。

<!-- guide:end -->
<!-- guide:begin example view -->
### 查阅指南与输入合同

```bash
template-registry prompt guide --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'view' --output 'view-guide.md' --json
template-registry prompt inspect --ref 'promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN' --role 'view' --json
```

guide 导出不能覆盖已有文件；重复练习请换目录。读取教程成功不代表该角色能够由通用编译器执行。

### 领域专用角色

该角色使用历史审阅 locale 或结构化文档格式，不提供通用 session compile 示例。使用上方 guide 查询拿到教程，并把 exact ref、role、当前 digest 和输入交给声明的消费方；不得把中文/YAML 文件复制成英文 Markdown 绕过准入。

### 等价 MCP 操作

1. 在 tools/list 确认 `template_registry_guide`，调用参数 `{"ref":"promptrepo://official/graph/longform.generic.v2@1.0.0?locale=zh-CN","role":"view"}`；用 resources/read 读取返回 resource。
2. 调用 `template_registry_inspect` 查看字段与实际可用性。客户端不用安装 CLI，资料 path 属于 server project。
3. 可编译角色按 session_create → source_import → session_update 推进，使用本角色输入表和 CLI 练习中的 JSON fields；每次取返回的最新 revision。
4. session_show 返回待确认 resource 后显式读取；收到真实用户答复再调用 session_confirm。
5. compile 后根据 ready/waiting 状态交付。export 的路径属于服务端；需要取回 portable ZIP 时读取会话返回或 server 声明的 compile/package resource，不能把服务端路径当成本机下载。
6. 未连接 author 工具、解析器或分析后端时报告缺口，不虚构安装工具。MCP 的实际 inputSchema 优先于旧教程。

<!-- guide:end -->
<!-- guide:begin checks view -->
### 结果示例与检查

示例目标：View。关系与知识状态有文本来源，推测不能当成正史写入。
合成内容示例（供理解输出方向，未运行模型）：知识差异示例：顾遥知道信件来源，林舟只知道旧地址。两条知识声明分别绑定其来源片段，不能自动传播为双方共同知识。
领域接受由原 owner 验证。
合成验收记录示例：输入已确认；提示包已校验；模型执行尚未进行；最终内容待用户或领域工具审阅。
逐项检查：输出是否满足该角色职责、所有必填字段是否有来源、引用是否真实存在、未知信息是否明确标注、实际素材是否满足许可。
结构化输出另须遵循[document descriptor](../contracts/documents/view.zh-CN.document.json)绑定的 schema；JSON 语法正确不代表语义合格。

<!-- guide:end -->
<!-- guide:begin recovery global -->
## 失败恢复、复用与交接

- `needs_input`：按缺失字段补值；`needs_analysis`：显式处理资料分析，不能仅凭导入就宣布读懂图片。
- `needs_confirmation`：读取待确认内容，收到答复后确认；`needs_step_output`：等待前序真实结果并导入。
- `REVISION_CONFLICT`：重新读取原 session，再合并改动；不要新建替代会话隐藏冲突。
- `GUIDE_NOT_FOUND`：当前快照缺教程；`GUIDE_STALE`：重新发现指南并核对版本；不自动切换模板版本。
- 导出结果未知时核对原产物和回执，不盲目覆盖或重导出。单条 prompt 导出不是 bundle，不使用 bundle verify 校验单文件。

```bash
template-registry prompt session list --sort activity --json
template-registry prompt commands --operation session.update --operation session.confirm --json
```

从列表选择原 session，使用 session describe/read 核对后更新输入；未变化的确认保持有效，变化的字段重新确认。跨项目导入包创建新会话，接收方重新确认。

声明的消费者：auctra。交接 exact ref、role、snapshot/template/contract digest、已接受输入和包位置。生成图片、视频、音频、写入正史或发布仍由对应 owner 执行。

编译、包校验、最终内容效果与发布是独立结果；本教程不提升 maturity 或修改 rights。
<!-- guide:end -->
<!-- solution-tutorial:end -->
