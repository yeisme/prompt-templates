## 1. Solution authoring foundation

- [ ] 1.1 Use Template Registry authoring commands to create the solution, roles, contracts and fixture skeletons
  - Acceptance：no hand-written `solution.json`/schema/fixture manifest/catalog；stable exact dependency refs to existing official solutions。
  - Verify：catalog build/validate commands from local `AGENTS.md`。
  - 当前状态（2026-09-03 复验）：结构化 metadata 已全部经 Registry authoring 命令生成或重放——`solution add`（zh-CN×7 + en×7）、`contract init/input set/validate`（14 个 sidecar）、`document init/validate`（14 个 descriptor）、`fixture validate`（7 组 zh-CN manifest）与 `catalog build/validate`（2026-09-03 复验 digest `sha256:cb1dda68199eed2150f7bcd4c6128ab19322f693a980b5f59d003fdcffb35582`，19 solutions 连续两次构建一致、工作树零漂移）；无手写结构化文件。仍无法完成的唯一子项：依赖 solution（`ai-drama-character-assets@1.0.0`、`ai-drama-storyboard-breakdown@1.0.0`）需要 exact released `promptrepo://` dependency refs，而 Registry 当前 `graph-kit release create` 的 required-role 合同锁定 graph-kit profile（`internal/structuredrelease` `requiredGraphKitRoles`），尚无覆盖普通 prompt solution 的 immutable release/snapshot CLI 面（2026-09-03 对照 template-registry HEAD 复验：新增的 `ui-template release` family 面向 UI template artifact，与本 solution 的七 role prompt 形态不匹配；内容仓 `releases/` 仍无任何 prompt solution release；`solution add` 亦无 dependency-ref 参数）；不得伪造 receipt，消费方继续 fail-closed 返回 `DEPENDENCY_RELEASE_UNAVAILABLE`。

- [x] 1.2 Author Chinese source prompts for seven roles
  - Depends on：1.1。
  - Acceptance：owner boundary、seven layers、typed/bounded inputs、semantic output、QC、failure、bounded repair；no hidden prompt or chain-of-thought request。
  - Verify：content lint and human review checklist。

- [x] 1.3 Author four profile modules
  - Depends on：1.1、1.2。
  - Acceptance：shared semantics、profile-specific risk/evidence/rights/duration rules、truthful candidate maturity。
  - Verify：profile matrix conformance fixtures。

## 2. Contracts, examples and fixtures

- [x] 2.1 Define input/output contracts through Registry authoring flow
  - Depends on：1.2、1.3。
  - Acceptance：no canonical ref/digest/accepted/budget/provider fields in model output；safe bounded JSON transport where needed。
  - Verify：document/contract validation commands provided by Template Registry。

- [x] 2.2 Add valid fixture matrix for four profiles and hybrid audio/restructure
  - Depends on：2.1。
  - Acceptance：seven valid cases in design；expected semantic output and safe findings。
  - Verify：fixture validate + owner consumer offline conformance commands。

- [x] 2.3 Add invalid fixture matrix with stable reason codes
  - Depends on：2.1。
  - Acceptance：dramatic-function、state-change、profile-switch、GEO、inherit collision、multi-change shot、unobservable emotion、invented claim、forbidden terminal、broad reroll、unbounded repair。
  - Verify：every invalid case fails before provider execution in consumer conformance。

- [x] 2.4 Add Chinese docs/examples/review/failure guides
  - Depends on：1.2、2.2、2.3。
  - Acceptance：clearly distinguishes template content owner from Auctra/Scaena/Eikona/Sonora execution/acceptance。
  - Verify：`git diff --check -- solutions/video/ai-film-multi-profile-production docs openspec/changes/official-ai-film-multi-profile-production-templates-v1`。

- [x] 2.5 Add reviewed English adaptation
  - Depends on：2.4。
  - Acceptance：source digest traceable；machine ids/variables unchanged；not auto-marked reviewed。
  - Verify：locale freshness validation。
  - Evidence（2026-09-02）：七个 role 的 `prompts/*.en.md` 与四个 `profiles/*.en.md` 由 authoring 会话逐篇人工撰写并逐项校对（非机器翻译直出标记）；`solution add --locale en`×7、`contract init + input set`×7×7、`document init`×7 全部经 Registry CLI 完成；`contract validate --locale en`（含 exact placeholder coverage）与 `document validate --locale en` 对七个 role 全部 success；en sidecar 的 type/required/enum/min-max length/sensitivity 与 zh-CN 逐项等价，schema ref 指向同一份 schema；逐 role 的 zh-CN source digest → en digest 绑定与评审记录登记于 `docs/i18n.md`，`docs/en-adaptation-draft.md` draft 导览随之作废删除；owner-handoff-guide 同步更正英文 locale 状态。

## 3. Release and consumer evidence

- [x] 3.1 Run Prompt Repository catalog and fixture validation
  - Depends on：2.1–2.5。
  - Verify：`(cd backend-server/template-registry && go run ./cmd/template-registry catalog build --repository ../../data/yeisme-prompt-templates --json)` and the matching `catalog validate` command。
  - Evidence（2026-09-02）：正式命令本身已可构建运行——`backend-server/template-registry` 工作树对 `github.com/yeisme/promptrepo` 的 pin 已更新至包含 `uitemplatefs` 的 `v0.4.1-0.20260901214202-4f239f57d74f`（该 pin 在 template-registry 仓为并行在途改动；本会话另以 committed HEAD snapshot + 本地 workspace canary 复核过同一命令语义，二者结论一致）。catalog build 连续两次输出同一 digest `sha256:01195cc686ea75ea0f900000f388e7e106493f284d4fb002c98f065ac170daf2`（17 solutions），`catalog validate` success；七个 role 的 zh-CN `fixture validate` 全部 success（case_count 3/2/3/6/2/2/3，manifest digest 逐一登记）；en locale 的 contract/document validate 全部 success。

- [x] 3.2 Record provider-free Auctra/Scaena/Eikona/Sonora consumer conformance refs
  - Depends on：3.1 and owner implementations。
  - Acceptance：content repository stores only immutable evidence refs/safe summaries；no provider call requirement for local closeout。
  - Evidence（2026-09-02）：四个 owner implementation change 均已在其仓库归档并提交，`docs/consumer-conformance-refs.zh-CN.md` 登记了 repo、归档 change id、提交 hash（Auctra `a62226d`、Scaena `d3f4cd0`、Eikona `d4c57dc`、Sonora `ea4beba`）与安全摘要（provider_called=false、fixture-only、无 payload）；登记规则明确只接受已提交的归档记录作为 immutable ref，owner-local temp evidence 目录按政策不入库；dependency release gate 保持 fail-closed；本地 closeout 无 provider 调用。

- [ ] 3.3 Publish an immutable internal exploratory release through Registry workflow
  - Depends on：3.1、human content review。
  - Acceptance：rights/maturity/locale/dependency refs correct；release does not claim first-support。
  - 当前状态（2026-09-03 复验）：3.1 与 reviewed English locale 已满足；仍无法完成的原因有二——(a) Registry 当前唯一覆盖 prompt solution 的结构化 immutable release CLI（`graph-kit release create`）把 required roles 锁定为 graph-kit profile（manifest/source_adapter/lens/view/validator），本 solution 的七 role 形态与其不匹配，也没有覆盖普通 prompt solution 的 release artifact family（2026-09-03 对照 template-registry HEAD 复验不变：`internal/structuredrelease` 仍按 `requiredGraphKitRoles` 锁定，新增 `ui-template release` family 面向 UI template artifact 不适用，内容仓 `releases/` 无任何 prompt solution release）；(b) 正式 internal immutable release 还需要维护者 Git commit/tag 固定与发布授权（与 `ai-drama-character-assets@1.0.0` release candidate 的先例一致：candidate 文档记录可以生成，immutable release 不得宣称已存在）。不得发布或宣称 exploratory release 已存在。

- [x] 3.4 Run final OpenSpec validation
  - Verify：`openspec validate --all --strict`。
  - Evidence：2026-08-31 执行 `openspec validate --all --strict --no-interactive`，10 passed、0 failed；2026-09-02 en locale 与 conformance refs 落地后复验，11 passed、0 failed，`git diff --check -- solutions/video/ai-film-multi-profile-production docs openspec/changes/official-ai-film-multi-profile-production-templates-v1` 干净。
