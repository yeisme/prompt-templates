# 多 Profile 生产合同

本 solution 的中文正文是 source。它只输出 provider-free 的语义提案；Auctra、Scaena、Eikona、Sonora 分别把自己的安全事实投影为有界输入，并在各自 Owner 内创建 candidate、review、acceptance、delivery 与 provider run。

## 七层 bundle

所有 role 使用同一层序：

1. `owner_boundary_and_safety`：内容模板只建议，不拥有 canon。
2. `profile_contract`：profile 固定、rights/risk/evidence/duration/readiness 由 Owner 投影。
3. `accepted_source_projection`：只读取已接受/当前的安全事实。
4. `active_reference_bindings`：每项引用必须明示 `inherit` 与 `forbid`。
5. `task_delta`：一轮只允许有限、可审查的变化。
6. `output_schema_and_findings`：只产出语义字段、finding 和不确定性。
7. `self_check_without_chain_of_thought`：只返回结论与有限 repair，不展示内部推理。

Registry contract 的七个 transport inputs 全部有类型和长度上限：`profile_id`、`accepted_source_projection_json`、`active_reference_bindings_json`、`task_delta_json`、`output_schema_version`、`continuity_constraints_json`、`retry_policy_json`。JSON 字符串是临时的有界 transport，不是 canonical store，也不可携带 provider payload、credential、raw prompt 或 hidden prompt。

消费 Owner 必须在调用模板前执行可重放的输入 validator：每个 `*_json` 必须是单一 JSON object、无重复键、在各自长度/深度限制内；拒绝 owner-terminal 字段（含 canonical ref、digest、timestamp、idempotency、accepted/frozen/delivered、budget/receipt）、provider/model/tool/credential/raw-prompt 字段。`active_reference_bindings_json` 的每个 binding 必须同时含 `ref`、`digest`、非空 `inherit` 数组与非空 `forbid` 数组；同一属性不能同时被不同 role 以互斥方式继承。无效 URI、非 SHA-256 digest、缺失 inherit/forbid 或碰撞时返回 `INVALID_REFERENCE_BINDING` 或 `IDENTITY_WARDROBE_INHERIT_COLLISION`，并在 provider 调用前停止。`invalid-malformed-reference-binding` fixture 是该 gate 的 replay 样本。

## 允许与禁止的输出

允许：语义计划、可观察行动/表演、风险 finding、safe evidence locator、fallback、最小 repair action、uncertainty。

禁止：canonical project/scene/shot/artifact refs、digest、时间戳、idempotency、expected version、accepted/rejected/frozen/delivered、预算/receipt、provider/model 参数、工具调用、凭证、raw/hidden prompt、完整思维链。Owner 负责将通过验证的语义输出转换成其 candidate。

每个 role 现在绑定独立的 `ai-film-<role>-semantic-output-v1` schema。schema 在 root 级使用 required properties、typed nested values、`additionalProperties: false` 和 forbidden property-name gate；旧的通用 `ai-film-semantic-proposal-v1` 只保留为已生成历史 artifact，不能作为当前 role 的输出绑定。

## Binding 语义

多源参考在 binding 层组合，不使用脸图与服装图的像素级合成。`identity_source` 继承脸部几何、永久 marker、发际线、基础发型轮廓，禁止表情/妆容/衣服/背景；`wardrobe_source` 继承衣物结构和材料，禁止脸、发际线、表情和身体身份。location 与 prop 同样只继承各自的结构/物理事实。

## Profile 读取顺序

- `cinematic_live_action`：身份、表演、物理、手部、口型。
- `motion_comic`：关键帧可读、screen direction、字幕/声音节奏、有限运动。
- `stylized_animation`：shape language、turnaround、形变界限、色彩/材质。
- `brand_film`：产品事实、claim、rights、logo/text、CTA 与时长。

所有 profile 当前均为 internal / exploratory / candidate。任何 first-support、reviewed、mature、release 或正式交付主张必须由相应 Owner 的真实 evidence 和 human review 另行证明。

## Dependency release gate（当前阻断）

当前 catalog 可以观察到 `ai-drama-character-assets@1.0.0` 与 `ai-drama-storyboard-breakdown@1.0.0` 的本地版本与 digest，但没有相应的 Registry immutable release/snapshot receipt。因此这些 catalog 条目不是可消费的 exact dependency。所有 consumer 必须 fail closed，返回 `DEPENDENCY_RELEASE_UNAVAILABLE`，直到 Registry 提供每项 dependency 的 exact `promptrepo://` address、release/snapshot digest、兼容能力、升级/回滚规则和 immutable receipt。不得从本地 catalog 推断或拼造 release ref。
