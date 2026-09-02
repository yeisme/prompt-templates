## 1. Solution contracts

- [x] 1.1 通过 Template Registry CLI 创建/升级 `ai-drama-character-assets@2.0.0` 与 `ai-drama-background-assets@2.0.0` 结构化 skeleton，不修改 1.x。
  - Evidence（2026-09-02）：两个 2.0.0 family skeleton 全部经 Registry authoring 命令生成——`solution add`×4（zh-CN）、`document artifact add`（共享输出 schema `character_asset.modular_slot_bundle.v1`，JCS canonical 落盘）、`contract init/input set/validate`×4、`document init/validate`×4，全部 success；catalog build 连续两次 digest 一致（`sha256:d53090b6bd3dbd847ceb5130a4d45149a247722f540843a2444cb5159d9047e4`，19 solutions），catalog validate 通过；`git status` 证明 1.x 目录零改动。命名决策：Registry authoring 以 solution id 定位目录且同 id 不允许双版本，故 2.0.0 family 采用版本后缀 id——稳定地址为 `promptrepo://official/video/ai-drama-character-assets-v2@2.0.0` 与 `promptrepo://official/video/ai-drama-background-assets-v2@2.0.0`（规则已写入 `docs/modular-visual-assets-v2.md` 版本节）。
- [x] 1.2 定义 shared slot、DesignSpec、RenderRevision、view plan、isolation、inherit/forbid 和 preview vocabulary。
  - Evidence（2026-09-02）：`docs/modular-visual-assets-v2.md` 新增“共享词汇（stable vocabulary）”节——9 个 slot ID 表、DesignSpec 必含字段（attachment/fit interface、layer_order、silhouette、material、color_regions、occlusion/collision、inherit/forbid、view_plan、required_evidence）、RenderRevision 单 change_scope 语义、六视图合同与 geometry-adaptive view plan、isolation、inherit/forbid 核心规则、preview `canonical=false` 边界；同一组 machine ID 进入 contract input enum（slot_id/view_id/topology_family/age_band/canvas_policy）与共享 schema enum。
- [x] 1.3 为 `zh-CN` source 与 `en` adaptation 建立版本、source digest、rights 和 maturity 规则。
  - Evidence（2026-09-02）：`docs/modular-visual-assets-v2.md` 新增“版本、locale、rights 与 maturity 规则”节——2.0.0 并行新 major 与 1.x 不可变、zh-CN 为 source locale 且 template digest 即 source digest、en 适配逐 role 绑定 source digest（stale 即重评审，沿用 `ai-film-multi-profile-production/docs/i18n.md` 的登记方式）、rights 默认 internal、maturity 初始一律 exploratory 及 first-support/mature 门槛。

## 2. Character templates

- [x] 2.1 实现 `head-core-bald-v1`，覆盖严格正脸 detail、完整头顶/后脑/双耳、六视图、透明输出和 blocking negative constraints。
  - Evidence（2026-09-02）：`solutions/video/ai-drama-character-assets-v2/prompts/head-core-bald-v1.zh-CN.md` 实现——`detail_front` 严格正脸（yaw/pitch/roll=0、正交感镜头）为第一视图、完整头顶/后脑/双耳/自然头皮/完整下颌、六视图合同（六 view 各为独立 RenderRevision）、透明 RGBA 与干净抗锯齿边缘、blocking negatives 显式清单（头发/发饰/耳饰/脖肩/衣服/背景/棋盘格/拼图等）；contract 10 inputs（含 slot/view/topology/age enum 与 JSON transport）、document 绑定共享 schema；contract/document validate success，稳定失败码 `HEAD_CORE_HAIR_CONTAMINATION`、`MISSING_SCALP_INTERFACE`、`VIEW_CONTRACT_VIOLATION`、`MINOR_ADULTIFICATION_RISK`、`TRANSPARENCY_CONTRACT_VIOLATION`。
- [x] 2.2 实现 `body-core-neutral-v1`，覆盖 age band、neutral coverage、topology family 和未成年人安全门。
  - Evidence（2026-09-02）：`solutions/video/ai-drama-character-assets-v2/prompts/body-core-neutral-v1.zh-CN.md` 实现——`age_band` enum（adult/minor/unknown，unknown 触发最保守策略并输出 info finding）、所有年龄默认 neutral coverage 完整中性覆盖且不强调隐私部位、`topology_family` enum（humanoid/quadruped/winged/serpentine/mechanical）且非人拓扑不烘焙外层资产、未成年人安全门（minor 强制 age-appropriate 覆盖与非成人化姿态/材质/镜头；任何年龄显式解剖一律拒绝；`policy_echo.safety_gates` 审计）；contract 10 inputs、document 绑定共享 schema，contract/document validate success；稳定失败码 `MINOR_SAFETY_GATE_BLOCKED`、`EXPLICIT_ANATOMY_REQUESTED`、`BODY_CORE_WARDROBE_CONTAMINATION`、`TOPOLOGY_FAMILY_MISMATCH`、`VIEW_CONTRACT_VIOLATION`、`TRANSPARENCY_CONTRACT_VIOLATION`。未成年人安全与非人 topology 的 consumer 侧 blocking fixtures 属 4.1/4.2，不在本任务验收内。
- [ ] 2.3 实现 `surface-coat-hair-v1`、`wearable-garment-v1`、`wearable-accessory-v1`，覆盖接口、层级、遮挡、碰撞与禁止继承。
- [ ] 2.4 实现 character layer/harmonized preview，明确 `canonical=false` 与 exact source lineage。

## 3. Environment templates

- [x] 3.1 实现 `semantic-object-v1` 及 geometry-adaptive view plan。
  - Evidence（2026-09-02）：`solutions/video/ai-drama-background-assets-v2/prompts/semantic-object-v1.zh-CN.md` 实现——独立物件边界（无手/人物/环境附着）、默认透明 RGBA、`view_plan_json` 输入 + `view_role=adaptive` + `adaptive_view_reason` 输出构成 geometry-adaptive view plan（最少充分视图、声明选择原因、独立 RenderRevision）；contract 8 inputs、document 绑定共享 schema，contract/document validate success；稳定失败码 `OBJECT_HUMAN_CONTAMINATION`、`OBJECT_ENVIRONMENT_CONTAMINATION`、`MISSING_VIEW_PLAN_REASON`、`OBJECT_STATE_MISMATCH`、`UNDECLARED_BRAND_TEXT`。
- [x] 3.2 实现 `empty-scene-shell-v1`，覆盖零人物、零人形痕迹、零独立物件和完整不透明画布。
  - Evidence（2026-09-02）：`solutions/video/ai-drama-background-assets-v2/prompts/empty-scene-shell-v1.zh-CN.md` 实现——零人物与零人形痕迹清单（含照片/海报/屏幕人物/雕像/模特/倒影/车内驾驶员）、零独立物件、完整不透明画布合同（`canvas_policy=opaque_full_canvas`，禁止透明区域/棋盘格/抠图边缘）、反打复用空间锚点、活动预留区可读；contract/document validate success；稳定失败码 `SCENE_HUMAN_TRACE_DETECTED`、`SCENE_LOOSE_OBJECT_DETECTED`、`OPAQUE_CANVAS_VIOLATION`、`ACTIVITY_ZONE_BLOCKED`、`ANCHOR_REDESIGNED_ON_REVERSE`。
- [ ] 3.3 实现 environment layer/harmonized preview，保持无人物边界。

## 4. Fixtures and validation

- [ ] 4.1 增加有效成人、未成年人安全、非人 topology、六视图和自适应物件视图 fixtures。
- [ ] 4.2 增加头发/发饰/首饰/脖肩/背景污染、服装污染身份、场景人物/海报/雕像/倒影/物件污染的 blocking fixtures。
- [ ] 4.3 增加 preview source lineage、canonical false 和旧 1.x 不变的兼容 fixtures。
- [ ] 4.4 运行 catalog build/validate 与 `openspec validate --all --strict --no-interactive`，不得调用真实 Provider。

## 5. Documentation

- [x] 5.1 发布模块化视觉资产 v2 设计说明并更新文档索引。
- [ ] 5.2 实现后更新 preset matrix、authoring guide 和 dated test guide，明确实际成熟度和 Provider-free 证据。
