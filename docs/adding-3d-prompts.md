# 添加 3D 模型提示词内容：决策指南（beta）

面向所有 Agent：往这套体系里加 3D 模型与空间资产提示词内容时，先选对层级，再按对应食谱执行。不要新建平行的提示词存放点。

本类别由 OpenSpec change `official-3d-model-templates-beta-v1` 定义，首批 5 个 solution 均为 beta/exploratory，真实 3D provider 验证完成前不得转正式版本，文档不宣称已验证的生成质量。

## 决策树

```text
要加什么？
├─ 一个文生 3D 单物体方案（主体/用途/风格/面数可参数化）
│   → 扩展 text-to-3d-object-beta；结构变化才新建同 package 成员
├─ 一个图生 3D 方案（参考图 + 视角/遮挡策略）
│   → 扩展 image-to-3d-refine-beta；参考图只持 exact ref，不复制正文
├─ 一个场景/多物体空间布局方案
│   → 扩展 3d-scene-layout-beta；字段保持 provider-neutral，不耦合 SceneGEO
├─ 一个 3D 打印/可制造性约束方案
│   → 扩展 3d-printable-design-beta；约束必须是可判定条目
├─ 一个 3D 资产评审清单
│   → 扩展 3d-asset-review-beta；每项 pass/fail/unknown 三态
├─ 一条「概念图 → 3D → 评审」多步流程
│   → recipe concept-to-3d-asset-beta 的变体；步骤只引用 exact locale=en ref
└─ 一种全新结构（现有槽位装不下）
    → solutions/3d/ 新包；先读 docs/authoring.md，并按「能扩展就不新建」评审
```

## 通用硬规则

- 模板正文只注册 `en`；中文译文放包内 `docs/template-zh-CN.md`，标注人工审阅身份，不注册、不进 digest。
- `solution.json`、`catalog.json`、contract、recipe、document descriptor 一律由 Template Registry CLI 生成，禁止手写。
- 3D 执行、candidate、production override、frozen asset 归 Scaena；空间感知证据归 Anatomia；概念图归 Eikona。模板不授予工具、凭据、费用或发布权限。
- 编译期 `provider_calls=0`；普通输出不含模板正文、用户值或凭据。
- 无真实尺度锚点时显式标记相对比例，不使用米制「1:1」表述。
- 非正式版本必须带 `beta`/`alpha` 标识；正式版本无后缀、从 `1.0.0` 起版（见根 AGENTS.md 版本命名条）。

## taxonomy 约定

- category/modality：`3d`。
- artifact：`model_3d`（单物体）、`scene_layout`（场景布局）。
- constraint：`manifold_geometry`（可制造几何）、`scale_anchored`（有尺度锚点）、`multi_view_consistency`（多视角一致）。
- capability：`model3d`、`scene_spatial`；provider-neutral，不用 `tripo`/`meshy`/`scaena` 等名字。

## 食谱 A：扩展既有 solution（默认）

1. 确认需求确实落在现有 5 个 solution 的某个槽位外，才改 contract；优先改模板正文与评审清单。
2. 修改后用 Registry CLI 重放 metadata：

   ```bash
   template-registry contract refresh --repository data/yeisme-prompt-templates --package 3d --id <solution-id> --json
   template-registry catalog build --repository data/yeisme-prompt-templates --json
   template-registry catalog validate --repository data/yeisme-prompt-templates --json
   ```

3. 中文译文同步更新 `docs/template-zh-CN.md`，跑变量 parity 校验。

## 食谱 B：新 solution

首批 5 个 solution 均按 `scripts/author_3d_templates.py` 的序列经 CLI 生成，可在维护时重放：

```bash
# 从根仓库源码运行维护工具（不依赖全局二进制）
(cd backend-server/template-registry && go build -o /tmp/template-registry ./cmd/template-registry)

python3 scripts/author_3d_templates.py --registry /tmp/template-registry
# 等价手工序列（以 text-to-3d-object-beta 为例）：
#   solution add --package 3d --id <solution-id>-beta --version 1.0.0-beta.1 --category 3d \
#     --rights internal --maturity exploratory --locale en --title '<English title>' --summary '<summary>' \
#     --usage '<usage>' --role main --prompt-path solutions/3d/<solution-id>-beta/prompts/main.en.md \
#     --capability model3d --tag category:3d --tag modality:3d --tag artifact:model_3d --json
#   solution locale describe --package 3d --id <solution-id>-beta --locale zh-CN \
#     --title '<中文标题>' --summary '<中文摘要>' --usage '<beta 试点说明>'
#   contract init --package 3d --id <solution-id>-beta --role main --locale en --license internal \
#     --permission execute_requires_review --permission preview --json
#   contract input set ...   # 每个变量一次（enum 用 --enum，ref 校验用 --regex）
#   contract refresh ... && contract validate ...
#   catalog build && catalog validate
```

`--prompt-path` 指向的英文正文必须先存在；zh-CN 只经 `solution locale describe` 登记人类可读元数据，不注册模板、不建 contract。

## 食谱 C：recipe 变体

新多步流程一律注册为 recipe（`recipes/<id>.json`，由 `template-registry prompt recipe init|step|bind|preset` 生成 canonical JSON），步骤只引用 exact `locale=en` ref；依赖循环与失效传播由 Registry 编译期校验。

已注册的 `concept-to-3d-asset-beta` 为两步 DAG：

- `image-to-3d` → `promptrepo://official/3d/image-to-3d-refine-beta@1.0.0-beta.1?locale=en`：Eikona 概念图以外部 source 绑定（`reference_image_ref ← source: concept_image`）进入，参考图保持指针不复制；概念图未导入/未确认前该步骤被 source 确认门控挡住。
- `asset-review` → `promptrepo://official/3d/3d-asset-review-beta@1.0.0-beta.1?locale=en`：`asset_ref ← step_output: image-to-3d`；上游输出未接受前保持 `needs_step_output`，不编造中间产物。「显式导出提示包」以该步骤的 `output_requirement` 表达。

```bash
echo '{"id":"<recipe-id>","path":"recipes/<recipe-id>.json"}' | \
  /tmp/template-registry prompt recipe init --project . --stdin --json
echo '{"path":"recipes/<recipe-id>.json","step":{"id":"<step>","ref":"promptrepo://official/3d/<solution>@1.0.0-beta.1?locale=en","role":"main"}}' | \
  /tmp/template-registry prompt recipe step --project . --stdin --json
echo '{"path":"recipes/<recipe-id>.json","step_id":"<step>","field":"<input>","binding":{"kind":"source|field|step_output","ref":"<ref>"}}' | \
  /tmp/template-registry prompt recipe bind --project . --stdin --json
echo '{"path":"recipes/<recipe-id>.json"}' | \
  /tmp/template-registry prompt recipe validate --project . --stdin --json
```

## 转正条件

- 至少一个真实 3D provider 的端到端执行证据（另行授权与费用批准）。
- 评审清单在真实候选资产上跑通过至少一轮。
- 转正时去 `-beta` 后缀、版本重置 `1.0.0`，metadata 由 Registry CLI 重放。

## 验证

```bash
python3 scripts/author_3d_templates.py --registry /tmp/template-registry   # CLI 重放全部结构化 metadata
python3 scripts/check_3d_templates.py --registry /tmp/template-registry    # provider-free 验收
```

验收覆盖：5 个 solution 的编译演练（空会话拒绝、未确认拒绝、缺字段/非法枚举/非法 ref 拒绝、成功导出、`provider_calls=0`、复用无泄漏）、zh-CN 不可编译、recipe DAG/依赖循环校验与 exact ref 解析、中英变量 parity。证据按脱敏政策写入 `temp/integration-test-runs/`（不入库）。
