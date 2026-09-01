## 1. Solution authoring foundation

- [ ] 1.1 Use Template Registry authoring commands to create the solution, roles, contracts and fixture skeletons
  - Acceptance：no hand-written `solution.json`/schema/fixture manifest/catalog；stable exact dependency refs to existing official solutions。
  - Verify：catalog build/validate commands from local `AGENTS.md`。
  - 当前状态：solution、七个 role contract/document/fixture manifest 与 catalog 均可被 Registry validator 读取；但依赖的角色资产和 storyboard solution 尚无 Registry immutable release/snapshot receipt，不能伪造 exact `promptrepo://` dependency refs，因此该 acceptance 尚未完成。

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

- [ ] 2.5 Add reviewed English adaptation
  - Depends on：2.4。
  - Acceptance：source digest traceable；machine ids/variables unchanged；not auto-marked reviewed。
  - Verify：locale freshness validation。
  - 当前状态：仅有明确标记为 draft 的英文导览，尚无人类内容评审与 locale freshness receipt，不得登记为 reviewed locale。

## 3. Release and consumer evidence

- [ ] 3.1 Run Prompt Repository catalog and fixture validation
  - Depends on：2.1–2.5。
  - Verify：`(cd backend-server/template-registry && go run ./cmd/template-registry catalog build --repository ../../data/yeisme-prompt-templates --json)` and the matching `catalog validate` command。
  - 当前状态：2026-08-31 的临时 Go workspace canary 中，catalog build/validate 对 16 个 solution 成功，catalog digest 为 `sha256:59b2114a62cc255b08ffaf54cf0905664e3837ed0bfc342275d5c874d2d7519e`；正式命令仍因已固定的 `github.com/yeisme/promptrepo@v0.2.0` 不包含本地 `uitemplatefs` 包而无法构建，且 2.5 尚未完成，所以不能勾选。

- [ ] 3.2 Record provider-free Auctra/Scaena/Eikona/Sonora consumer conformance refs
  - Depends on：3.1 and owner implementations。
  - Acceptance：content repository stores only immutable evidence refs/safe summaries；no provider call requirement for local closeout。
  - 当前状态：四个 owner implementation change 已完成或归档，但 3.1 尚未关闭；只有 owner-local 临时 evidence path，尚无可登记为 immutable 的跨仓库 evidence refs。

- [ ] 3.3 Publish an immutable internal exploratory release through Registry workflow
  - Depends on：3.1、human content review。
  - Acceptance：rights/maturity/locale/dependency refs correct；release does not claim first-support。
  - 当前状态：human content review、reviewed English locale、exact dependency release refs 与正式 Registry build 均未满足；不得发布或宣称 exploratory release 已存在。

- [x] 3.4 Run final OpenSpec validation
  - Verify：`openspec validate --all --strict`。
  - Evidence：2026-08-31 执行 `openspec validate --all --strict --no-interactive`，10 passed、0 failed。
