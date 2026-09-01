## Context

电影 Prompt 不是“一条三千字散文”，而是 accepted refs、固定 profile、scene geometry、action/performance/audio 变量和输出合同的编译结果。内容仓库只提供公开可审阅的模板与 fixtures；Auctra/Scaena/Eikona/Sonora 负责把 canonical facts 投影为 bounded inputs，并在输出后创建 candidate/review。

## Goals / Non-Goals

### Goals

- 一套 shared engine 支持四 profile，不复制 owner 状态或 catalog entry。
- 把剧作编译、资产依赖、SceneGEO、ShotAudioIntent、连续性和失败重构串成模板系统。
- 让每个模板只解决一种 artifact/decision，输出可审计 semantic result。
- 用 exact refs/digests、继承/禁止继承和 positive locks 降低身份/服装/空间漂移。
- 为 Auctra/Scaena/Eikona/Sonora 提供明确 handoff，不把 consumer 实现放进内容仓库。

### Non-Goals

- 不执行模型、不持有 provider credential/route/cost。
- 不保存用户项目、媒体、owner state、raw provider payload 或 full chain-of-thought。
- 不让 Prompt 生成 canonical owner ref、digest、accepted/frozen/delivered 状态。
- 不把 expression sheet 宣称为 LoRA-ready dataset。
- 不把四 profile 宣称为 mature，直到四个完整 canary 通过。

## Decisions

### 1. 一个 solution，多个 role 与 profile

计划目录：

```text
solutions/video/ai-film-multi-profile-production/
  prompts/
    project-intent.zh-CN.md
    asset-dependency.zh-CN.md
    scene-package.zh-CN.md
    shot-prompt.zh-CN.md
    shot-audio-intent.zh-CN.md
    continuity-review.zh-CN.md
    failure-restructure.zh-CN.md
  profiles/
    cinematic-live-action.zh-CN.md
    motion-comic.zh-CN.md
    stylized-animation.zh-CN.md
    brand-film.zh-CN.md
  docs/
  examples/
  contracts/          # Registry generated
  fixtures/           # Registry generated manifests + canonical cases
```

角色资产和 storyboard breakdown 通过 exact released `promptrepo://` refs 声明为 dependencies；新 solution 只定义跨阶段组合和缺失角色，不复制依赖正文。

### 2. Prompt Bundle 使用七层结构

```text
1. owner_boundary_and_safety
2. profile_contract
3. accepted_source_projection
4. active_reference_bindings
5. task_delta
6. output_schema_and_findings
7. self_check_without_chain_of_thought
```

每层职责：

- owner boundary：声明候选/建议，不接受 canon，不执行工具；
- profile：时长、画面、声音、rights/claim 与风险优先级；
- source projection：只使用 consumer 给出的 accepted/current safe facts；
- references：exact refs、revision/digest、inherit/forbid；
- task delta：本轮唯一可变维度；
- output：typed semantic fields 与 findings；
- self-check：只输出 summary/findings/repair actions，不输出内部推理链。

### 3. 六个主模板各自只负责一种决策

#### `project-intent`

消费 brief/story/asset inventory safe projection，输出主题候选、情感主角、欲望/需要、角色压力、asset dramatic function、场景 obligation 与风险 finding。它不能生成最终镜头或 owner handoff digest。

#### `asset-dependency`

消费 accepted production intent 与资产 inventory，输出 semantic dependency plan：face→expression、body/base wardrobe→turnaround、wardrobe/hairstyle variants、action/interaction still evidence、location/prop/state、scene binding。它不执行 Eikona，也不接受资产。

#### `scene-package`

消费 accepted scene intent、SceneGEO、asset/audio safe projections，输出 closure analysis、missing dependency、prototype/production readiness proposal、coverage/risk 与 hero fallback。最终 package id/digest 由 Scaena 编译。

#### `shot-prompt`

消费一个已定义 shot function 和 exact bindings，输出 provider-neutral sections：first frame、camera/optics、action timeline、observable performance、physics、lighting、audio role、positive continuity locks 与 bounded negatives。一次只承担一个主要动作/情绪变化。

#### `continuity-review`

消费可见 evidence summaries，输出 rule-level finding、criticality suggestion、evidence refs、repair suggestion 与 uncertainty。模型不能签署 waiver 或计算 owner final verdict。

#### `failure-restructure`

消费最近 attempts 的 safe failure summary，判断应拆镜、固定机位、减少人物、缩短时长、从已建立接触开始、改 reaction/insert/sound bridge 或改写场景。它不能发起新 provider run。

### 4. ShotAudioIntent 是单独模块

`shot-audio-intent` 输出 speaker/line refs、语言/读音、时长窗口、sync action、listener reaction、ambience/Foley/music/silence role、native source policy 与 replacement policy。它不生成台词、voice asset、provider Prompt 或 final mix。

### 5. Reference binding 强制 inherit/forbid

示例约束：

| Ref role | inherit | forbid |
| --- | --- | --- |
| `identity_source` | face geometry、skin marker、hairline、base hairstyle silhouette | source expression、makeup、wardrobe、background、dramatic grade |
| `wardrobe_source` | silhouette、layer order、seams、material、color placement | face、hairline、expression、body identity |
| `location_source` | architecture、anchor placement、surface、light-source logic | accidental people、shot-specific camera drift |
| `prop_source` | geometry、scale、material、open/closed state | holder identity、unrelated background/style |

多参考合并发生在 binding 语义层。Prompt 不宣称像素拼接能保证身份或材质一致。

### 6. Positive locks 优先于无界 negative list

模板应优先写：

```text
Exactly two visible characters throughout.
Roco remains frame-left; Milo remains frame-right.
One relic box remains centered on the table.
The established room architecture and light direction remain constant.
```

negative constraints 只补充常见失败，不重复整份 canon。每次 reroll 必须声明 `change_scope`，默认只改变一个变量；若同时改变 identity、camera、action、lighting 和 style，validator 应返回 `REROLL_SCOPE_TOO_BROAD`。

### 7. 表演必须可观察

禁止只写抽象情绪。模板要求把情绪翻译为 gaze、blink、breath、jaw、muscle tension、weight shift、gesture timing 与 reaction lead/lag。non-speaker reaction 可以在 line 结束前启动，但不得泄露尚未成立的信息。

### 8. Profile matrix

| `profile_id` | Readiness | 主要优先级 | 特殊检查 |
| --- | --- | --- | --- |
| `cinematic_live_action` | candidate | identity、performance、physics、native audio | hands/props、lip-sync、lighting stress、reaction coverage |
| `motion_comic` | candidate | keyframe readability、screen direction、audio pacing | panel density、limited motion、caption/subtitle、silhouette |
| `stylized_animation` | candidate | style/shape/motion rules | turnaround、deformation limits、color/material consistency |
| `brand_film` | candidate | product truth、claim、CTA、delivery | logo/text geometry、fact refs、rights、duration/CTA timing |

四 profile 必须通过各自完整 canary 才晋级 first-support。内容 release 初始保持 `maturity=exploratory` 或 profile-level candidate。

### 9. Semantic output 不包含确定性 owner 字段

禁止模型输出：canonical project/scene/shot/artifact ref、digest、timestamp、idempotency、expected version、accepted/rejected/frozen/delivered、budget reservation/receipt、provider payload、credential、tool call 或 chain-of-thought。

允许输出：local semantic keys、source refs、decision summary、observable plan、findings、risk、fallback、repair actions 和 uncertainty。consumer validator 负责把 semantic output 编译为 owner candidate。

### 10. Bounded repair 只修 finding 指向维度

repair 输入包含原 semantic output safe projection、typed findings、同一 source refs、profile 和 prompt snapshot。它不能扩大 story、改变未受影响字段、换 model/provider 或自动重新运行。两个以上 cell/shot 同时 identity/capture 漂移时，升级 baseline/binding blocker，不逐项堆形容词。

### 11. Fixture matrix

Valid：

1. live-action two-hander scene package + shot prompt；
2. motion-comic dialogue scene with audible animatic obligations；
3. stylized-animation action with shape/motion rules；
4. brand-film product truth/CTA scene；
5. asset-first dramatic function compilation；
6. one failed native audio segment replacement；
7. red-risk shot restructure preserving causal beat。

Invalid：

- asset showcase without dramatic function；
- no emotional protagonist where profile requires one；
- scene with no state change；
- profile switch at shot level；
- missing SceneGEO/axis for multi-character shot；
- identity/wardrobe inherit collision；
- Prompt asks one shot to perform multiple major changes；
- unobservable emotion only；
- raw Prompt/provider payload/credential field；
- invented dialogue/product claim/fact ref；
- model outputs accepted/digest/receipt；
- reroll changes multiple variable classes；
- failure repair adds adjectives after retry threshold instead of restructuring。

### 12. Structured assets 由 Registry CLI 生成

`solution.json`、contracts、schemas、fixture manifests、catalog、release manifest 与 lock 都必须由 Template Registry CLI/application service 创建或修改。作者只 patch Prompt prose、profile prose、examples 和普通 docs。

## Compatibility and rollback

- 现有角色资产/storyboard solutions 保持独立，使用 exact immutable dependency refs。
- 新 solution 不修改 `promptrepo://` DTO；需要 object/array input 时沿用消费 owner 的 bounded canonical JSON string transport，直到 shared contract additive 支持。
- 回滚删除 active catalog mapping，不删除 immutable release；consumer 回到既有 exact refs。

## Validation

Provider-free commands：

```bash
(cd backend-server/template-registry && go run ./cmd/template-registry catalog build --repository ../../data/yeisme-prompt-templates --json)
(cd backend-server/template-registry && go run ./cmd/template-registry catalog validate --repository ../../data/yeisme-prompt-templates --json)
cd data/yeisme-prompt-templates && openspec validate official-ai-film-multi-profile-production-templates-v1 --strict
```

Consumer conformance 由各 owner change 使用 fixtures 证明，本仓库不调用 provider。
