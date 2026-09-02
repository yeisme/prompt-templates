# Owner Handoff Guide（provider-free）

本指南只描述安全 handoff。当前 solution `video/ai-film-multi-profile-production@1.0.0` 为 internal / exploratory；它没有发布，英文 locale 已有 reviewed 适配（逐 role 绑定 `docs/i18n.md` 中的 zh-CN source digest），但 dependency release gate 尚未满足。每个 Owner 在 gate 未满足时必须停止在 provider 调用之前。

## 当前 checkpoint 的精确模板/合同 digest

| Role | Template digest | Contract digest |
| --- | --- | --- |
| `project-intent` | `sha256:f4ea4e5c2fe01eb0befba6da7d9e1eb97a0d39f9379608d58991124e9fc2e5ac` | `sha256:b18d47605beb674b7f14a3c1e9a42da0a1cd377ebe18909ac096391d4f309a7d` |
| `asset-dependency` | `sha256:a95a6cbd8708dae1b0a6fe9ebefd47df8c1694a29830b1472d504981272f9593` | `sha256:c452f0fbb4d8ba1fd000ee9b5cdac6e6b2be8fa182712bd71ee3ad92319bc0d0` |
| `scene-package` | `sha256:5ae339e960deb40e5ef78e9f6a4ebec53739e5d88d57fe0c9a540e593b235e92` | `sha256:5f9a2f8b7e6f0b998470608c759085b57a53a147985de333e796e78321e23441` |
| `shot-prompt` | `sha256:a95842c57297aac6fa618d0ff17e73e175750255fa099cff57acba5ffb6cc595` | `sha256:c3fe1142e5244ca45ce0402dfaa8ffc86a7471ef1f86444bf56e3b35b8b91281` |
| `shot-audio-intent` | `sha256:4f5763c70d6643d72f42178306027269c7a32db60a0a359d5cd9660c31b1140f` | `sha256:27c1e001a6cd687711213f786793dd31017d8d427fb310eb0400aa8b7ca28c5a` |
| `continuity-review` | `sha256:4adb3f5e0c3f4f3e6fd383cce592533841ddd6cffbcc5059b63e98acf7665453` | `sha256:7de7b8c542200c0503d7098df4dacfdeecaf7e536f9a371f0b766ac50043d44b` |
| `failure-restructure` | `sha256:9b997d8dc5d7fa1ba03dd53bffff2c1171e38ca1317085140af1de6f812f5c42` | `sha256:9205acbba5ee4befc22e13de2fd8016d8ca11cc9cc0d8de64573f7db6819299d` |

这些是未发布 checkpoint 的校验值，不是 immutable release address；每次 source/contract 更新都必须重新读取 catalog 与 contract，而非复用本表。英文 locale 的 template/contract digest 见 `docs/i18n.md` 与 `contracts/<role>.en.json`；en 与 zh-CN 的约束（type、required、enum、length、sensitivity）逐项等价。

## Auctra

- Artifact：`project-intent` 与 `failure-restructure` 的语义 proposal。
- Safe input refs：已校验的 brief/角色/产品事实投影；禁止把 project canon、用户文本全文或未核验 claim 送入内容仓库。
- Expected template/contract：从 catalog 的 `project-intent` 或 `failure-restructure` template digest 与对应 contract digest 精确读取；不接受“最新版”别名。
- Provider policy：本 solution 不调用 provider；Auctra 自己决定其受权执行。
- Persistence boundary：Auctra 保存 candidate/review/evidence；内容仓库只保存 fixture 和安全 ref。
- Validation：先运行所属 role 的 Registry contract/document/fixture validate，再运行 Auctra 自有 input validator。
- Next owner：Scaena 接收已验证的场景义务；dependency release 不可用时返回 `DEPENDENCY_RELEASE_UNAVAILABLE`。

## Scaena

- Artifact：`scene-package`、`shot-prompt`、`continuity-review` 的 semantic proposal。
- Safe input refs：安全 scene intent、SceneGEO、active bindings、continuity evidence summary、音频意图；媒体 bytes 和 canonical scene/shot state 不出 Owner。
- Expected template/contract：采用 catalog 对应 template digest + role contract digest；schema 必须为对应 `ai-film-<role>-semantic-output-v1`。
- Provider policy：不由本 solution 执行生成；Scaena 的执行、验收、edit/delivery 状态保持本地。
- Persistence boundary：Scaena 保存 package/shot/review candidate 与 evidence；内容仓库不保存 acceptance。
- Validation：Owner parser 先检查 JSON shape/ref/digest/inherit/forbid，再运行 Registry fixture validate；多人物缺 GEO 必须在 provider 前拒绝。
- Next owner：Eikona 接收单主体/单视图资产义务，Sonora 接收已批准声音意图。

## Eikona

- Artifact：`asset-dependency` 提供的阶段 DAG 与 reference-binding proposal。
- Safe input refs：face/body/wardrobe/location/prop 的安全 binding，及单一变化 scope；无资产 bytes、无 credential、无 release status。
- Expected template/contract：`asset-dependency` 的 catalog template digest、contract digest 与 role-specific schema。
- Provider policy：内容 solution 不出图；若 Eikona 已获执行授权，仍须在自身 Owner 内创建候选和 evidence。
- Persistence boundary：资产状态、图片、接受和版本属于 Eikona；内容仓库只保存 provider-free semantic fixture。
- Validation：DAG、binding collision、单主体/单视图和运动试镜义务先验；无 immutable dependency release 时 fail closed。
- Next owner：Scaena 仅接收已验证的安全资产投影，不接收 provider payload。

## Sonora

- Artifact：`shot-audio-intent` 的 segment/sync/replacement proposal。
- Safe input refs：line source、speaker/listener、时长窗、scene audio context、rights policy；未给出的台词/读音/claim 必须保持 unknown。
- Expected template/contract：`shot-audio-intent` 的 catalog template digest、contract digest 与 role-specific schema。
- Provider policy：本 solution 不生成 voice/mix；Sonora 执行和最终混音仍是其 Owner 决定。
- Persistence boundary：voice/segment/readiness/mix/replacement 在 Sonora；内容仓库不写最终 audio ref 或 delivery。
- Validation：检查 listener knowledge、音画窗口、native replacement policy 与 forbidden terminal fields；调用 provider 前完成。
- Next owner：Scaena 可消费安全音频意图，最终交付仍由各自 Owner 验证。

## 共用命令与 release gate

在本地开发 canary 中，用临时 workspace 执行 Registry catalog/contract/document/fixture validation。默认 Registry module 目前缺失 `github.com/yeisme/promptrepo/uitemplatefs`，因此默认命令不能作为通过证据；不能把本地 `go.work` 技巧写入正式用户工作流。正式 dependency 与 release 只可由 Registry immutable release workflow 提供。
