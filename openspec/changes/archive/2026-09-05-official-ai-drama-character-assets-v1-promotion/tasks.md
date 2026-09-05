# 任务

- [x] 1. 删除旧 1.x 包目录并晋升 v2 内容为正式 `ai-drama-character-assets@1.0.0`。
  - Evidence（2026-09-05）：旧目录（main/isolated/staged 角色、templates/profiles/examples/fixtures）整体移除；v2 目录晋升为无后缀正式名；solution/document/contract/fixture metadata 全部经 Registry CLI 重放（7 角色 × zh-CN/en solution 注册、共享 schema artifact、14 contracts、7 document descriptors、31 fixture cases，`contract/document/fixture validate` 全 success）。
- [x] 2. 共享 schema `$id` 去 `-v2` 并级联绑定。
  - Evidence（2026-09-05）：`document artifact replace --expected-digest` 更新 schema（`$id` 改为 `…/promptrepo/ai-drama-character-assets/modular-slot-bundle.v1`），character 7 角色 + background-v2 4 角色全部 `document schema rebind` + `fixture set refresh` 成功。
- [x] 3. 版本命名规则落入仓库文档。
  - Evidence（2026-09-05）：AGENTS.md「内容与语言」新增命名规则；docs/authoring.md 版本后缀段落改写；docs/modular-visual-assets-v2.md、docs/README.md、docs/ai-drama-templates-test-guide-2026-09-02.md、preset-matrix 引用更新。
- [x] 4. 全仓验证。
  - Evidence（2026-09-05）：`catalog build/validate` success（29 solutions，digest `sha256:64069a7e…07c06`）；全仓 22 个 fixture set `fixture validate` 全绿（顺带修复 storyboard-breakdown、ai-film-multi-profile-production 等 9 处在途正文导致的 stale source binding）；`openspec validate --all --strict` 16 passed / 0 failed。
- [x] 5. 消费端 canary 迁移（Scaena + Eikona，外部仓）。
  - Evidence（2026-09-05）：scaena `efc37e22`——TestOfficialCharacterAssetPromptConformance 重写为 7 slot 角色解析+digest 链+31 fixture cases+preview lineage 安全 ref，`task test:integration:official-character-asset-canary` evidence passed；eikona `d73c9422`——TestOfficialCharacterAssetFixtureCanary 重写为新 manifest 面，旧 1.x planner 测试改读本地 testdata（legacy 兼容），live scenario 同步，integration evidence passed（run integration-20260905T191214Z）。
  - `agent/scaena` official_character_asset_canary 与 `cli/eikona` official character asset canary scenario / promptbundle 测试从旧 1.x 角色迁移到模块化 7 角色。
- [x] 6. 记录未触发真实 Provider、未发布 release 的交付边界。
  - Evidence（2026-09-05）：全程 provider_calls=0（canary evidence 字段固定输出）；无 commit/tag/push/publish 宣称 release；maturity 保持 exploratory；模板仓提交 58226bb、scaena efc37e22、eikona d73c9422 均为本地提交未推送。旧 1.x ref（`…@1.0.0#hairstyle-sheet-v1`）compat-only 语义由 `legacy-hairstyle-compat` fixture 保留。
