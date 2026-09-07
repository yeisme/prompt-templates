## 为什么

官方 Prompt 内容已具备 catalog、companion contract 和部分结构化 document，但当前仍有三处跨模板不一致：多 owner solution 只声明粗粒度 solution capability；direct-to-provider 正文混入 authoring guide 与人工 checklist；基础模板缺少与高阶模板相同的输入、输出和失败语义。

同时，`realistic-vlog-shot-generation` 的当前 Provider 兼容改动新增 `provider_banner` 后，文档仍写 21 个输入，双语使用步骤编号重复，英文 locale 的校对状态表述也不够明确。

## 变更内容

- 用既有 document descriptor `required_capabilities` 维护 role 级消费能力，不把所有 owner capability 合并到 solution。
- 为 direct-to-provider solution 增加独立 delivery role，使最终 Provider 正文不包含维护说明或 review checklist。
- 按风险分三批升级基础模板的 companion contract、untrusted source boundary、typed output 与 fixture。
- 建立 exact address/digest 与 owner conformance 的证据表，未闭环前只标记 `semantic_alignment_only`。
- 先修复当前 Vlog 模板的输入计数、双语步骤编号与 locale 校对状态说明。

## 能力归属

- 分类：`fit`
- canonical owner：本官方内容仓的 Prompt 正文、locale、contract、document descriptor 与 fixture。
- Registry CLI 负责生成结构化 metadata；Auctra、Scaena、Eikona、Sonora 各自负责执行适配与证据。

## 影响

已发布 snapshot 不原地改写；新增 role/version 采用 additive 方式。当前未发布 Vlog 改动在 catalog build 前同步刷新 contract digest。
