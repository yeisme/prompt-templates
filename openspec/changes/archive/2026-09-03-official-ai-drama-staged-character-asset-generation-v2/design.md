## Context

`character_asset.prompt_bundle.v1` 已把每个视图放在独立的 `views[]` 条目中，但武侠三视图 fixture 的 `composition_layout` 仍描述“三格等宽排列”，实测程序又把仓库的编译元 Prompt 直接交给图片模型，最终得到一张模型自行排版的多宫格图片。该路径无法保证背面、无法单独返修，也跳过 face master 与主视图的人审门。

本变更只调整官方内容与 consumer conformance 语义。Prompt 仓库不执行 Provider；Eikona 负责单图生成和本地联系表；Scaena 负责角色版本、continuity lock 与 production acceptance。

## Goals / Non-Goals

**Goals:**

- 让角色资产按脸模、身体、基础服装正面主视图、派生侧背视图逐级生成和接受。
- 保证 production 路径每个 Provider job 只请求一个视图、一个人物实例和一张候选图。
- 让 `turnaround-three-view-v1` 继续可读，同时把三个 `views[]` 解释为三个独立 artifacts。
- 让联系表成为对单图 artifacts 的确定性本地审稿投影，而不是模型生成结果。
- 提供可离线验证的 fixtures、reason codes 和未来付费 canary 顺序。

**Non-Goals:**

- 不新增图片 Provider、模型或图像后处理依赖。
- 不在 Prompt 仓库记录接受状态、图片 bytes、Provider payload 或运行证据。
- 不把 Eikona 的 human accept 等同于 Scaena production freeze。
- 不在本变更中完成 LoRA、真人数字替身、视频运动稳定性或全自动审稿。

## Decisions

### 1. 生产 DAG 以“可接受的最小主资产”为门

```text
face-master-front
  → body-master-front
  → base-wardrobe-front（角色主视图）
  → turnaround-left-profile
  → turnaround-back
  → local-contact-sheet-1x3
```

- `face-master-front`：中性表情、正面平视、bust/portrait、干净背景，只锁身份、肤色范围、永久 marker、发际线和基础发型。
- `body-master-front`：正面全身、中性站姿，继承 accepted face master，只锁身体比例与基础轮廓，不提前接受剧情服装。
- `base-wardrobe-front`：正面全身主视图，继承 accepted face/body，并绑定一套基础服装；它是后续旋转视图的视觉锚。
- `turnaround-left-profile` 与 `turnaround-back`：各自独立生成，必须同时绑定 accepted face、body 和 base-wardrobe-front；不得并行抢跑到主视图接受之前。

选择串行门而不是一次生成三视图，是因为角色身份、衣服结构和视图旋转属于不同失败维度。先接受主资产后，侧背图可以有界返修，不需要整张重抽。

### 2. 现有 profile ID 保持稳定，stage 由 profile 与 view role 共同推导

不新增 `turnaround-single-view-v2`，也不删除 `turnaround-three-view-v1`。Consumer 按以下规则解释：

| Profile | View | Stage |
| --- | --- | --- |
| `face-master-v1` | `front` 或 `detail` | face master |
| `body-master-v1` | `front` | body master |
| `turnaround-three-view-v1` | `front` | base wardrobe main view |
| `turnaround-three-view-v1` | `left_profile` / `right_profile` / `back` | derived turnaround view |

Bundle schema version 保持 `character_asset.prompt_bundle.v1`。新 authoring task 可以 additive 地声明 `execution_mode=independent_artifacts`、`provider_artifact_count_per_job=1` 和 `review_layout=turnaround_contact_sheet_1x3`；不认识这些 authoring hints 的旧 consumer 仍能读取 `views[]`，但不能因此宣称 production conformance。

### 3. 每个独立 job 使用单视图 composition

Compiler 为每个 view 构造单独 Prompt：复用 identity/body/wardrobe/camera/continuity 公共段，只追加当前 view instruction，并将 composition 正规化为“单人、单视图、单张图、完整入画”。它不得把“三格”“网格”“contact sheet”或其他视图的 instruction 发送给 Provider。

旧 fixture 或旧 Bundle 若带有多宫格 `composition_layout`，production consumer 必须在 Provider 调用前正规化并报告 `LEGACY_MULTI_PANEL_LAYOUT_NORMALIZED`；若调用方显式要求 production grid，则以 `CHARACTER_ASSET_PROVIDER_GRID_FORBIDDEN` 阻断。Quick preview 可以单独保留，但必须标记 non-production，不能进入逐视图 acceptance。

### 4. 联系表只使用确定性本地排版

当正面、侧面、背面候选均存在时，Eikona 可以按固定 view order 创建 1×3 review contact sheet。联系表只保存 artifact refs、顺序、尺寸与 digest；标签由本地渲染添加，不要求图片模型生成文字。任何单图更新都只重建联系表，不重新调用 Provider。

### 5. Face master 是下一次真实 canary 的唯一首测目标

未来获得明确付费授权时，先只生成一张 face master：正面、成年、中性表情、干净背景、无多宫格。人审通过后才允许 body/master-front canary。旧官方三视图实测保留为失败证据，但不得作为模板质量通过结论。

### 6. Fixtures 分为阶段正例与执行负例

新增或调整的正例覆盖 face master、body master、base wardrobe front 和既有 turnaround split。负例覆盖：元 Prompt 直发、production multi-panel、body 缺 accepted face、derived view 缺 accepted front、back instruction 出现正面五官、同一 job 含多个 views。

Structured JSON/YAML 与 manifests 必须通过 Template Registry authoring service/CLI 写入和重新生成；普通中文 Prompt prose 与说明文档可以人工编辑。

## Risks / Trade-offs

- [阶段增加后出图次数变多] → 先用单张低风险 master 做门禁，失败只返修当前阶段，减少整组报废和重复费用。
- [旧 composition 文本仍含三格语义] → production compiler 强制单视图正规化并输出兼容 finding；内容 fixture 同步迁移为独立 artifact 语义。
- [accepted ref 语义不由 Prompt schema证明] → Prompt 只声明 exact refs；接受状态由 Eikona resolver/review state验证，Scaena再做自身 admission。
- [侧背视图过度依赖正面参考导致复制正面] → derived view Prompt 明确旋转目标与禁止项，并保留 face/body/wardrobe 分工，不把一张主视图当作唯一身份真源。
- [本地联系表被误当 canonical 图片] → 联系表 artifact role 固定为 `review_projection`，单图 artifacts 才能进入逐视图接受与返修。

## Migration Plan

1. 保留现有 schema/profile IDs，新增阶段化 OpenSpec 与 provider-free conformance。
2. 通过 Template Registry authoring 命令新增 face/body fixtures，并把 turnaround composition 调整为独立 artifacts。
3. Eikona 先 dual-read 旧/new Bundle，production 一律拆 view；旧多宫格文本仅产生 compatibility finding。
4. 修正付费 canary 为 face-master-only，默认测试与集成测试仍保持 provider calls=0。
5. 验证完成后再把文档中的旧三视图实测标记为 execution-design failure，等待新的逐阶段人审结果。
6. 回滚只移除新增 authoring hints/fixtures 和 staged execution gate；旧 profile、旧 fixtures 与历史实测证据保持只读，不删除、不重写。

## Open Questions

- 首次 face master 人审通过后，是否需要把 `right_profile` 加入首个 turnaround wave，留待真实质量证据后决定；当前 first slice 维持 front、left_profile、back。
