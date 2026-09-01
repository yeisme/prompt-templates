## 1. Generate pilot contracts

- [x] 1.1 使用 `contract init` 生成 zh-CN/en sidecar，并绑定各自 template digest。
- [x] 1.2 使用 `contract input set` 写入五个实际占位符、双语说明、enum/default/example。
- [x] 1.3 使用 `contract validate` 校验两份 sidecar。
- [x] 1.4 使用相同 CLI 为 `audio/podcast-narration` 生成并验证 zh-CN/en sidecar，`script` 标记 sensitive。

## 2. Verify compatibility

- [x] 2.1 重新执行 catalog build/validate，确认 digest 仍为 `sha256:d252148bb4e4f6be95f99848dd49bad43b6414f4b7ccd520fe71b3616ad37b2f`。
- [x] 2.2 使用 promptrepo v0.3 local SDK 与 Sonora build-tag canary 验证 inspect readiness、typed validate、provider-free preview、显式 output 和 body/value-free machine projection；公共 tag 发布仍是独立 release gate。

## 3. Documentation

- [x] 3.1 更新 authoring、i18n、release 与 README，说明 sidecar owner、真实命令和成熟度限制。
- [x] 3.2 严格验证本 change，并确认 diff 不包含 secret、运行 evidence 或手写结构化 metadata。

## Verification evidence

- zh-CN contract digest：`sha256:61d6a31afa393095e8eff2e4af068d0f7a9b3420cd6ea9efb71fc1b501d2c43a`。
- en contract digest：`sha256:f5144d46e73ddc3c50da95fc26dc1c584221ea51471505c91bd2bc29cc743c52`。
- audio zh-CN contract digest：`sha256:7bfa796fa3131687e09cf0d3c59aa2a532a566c293f73ba569f43331187ac395`。
- audio en contract digest：`sha256:009808b71180ddb61ed90248f68672660ab424c686d0ef8108996445dda4092c`。
- 两份 `template-registry contract validate --json` 均通过，字段数均为 5。
- catalog build/validate digest 保持 `sha256:d252148bb4e4f6be95f99848dd49bad43b6414f4b7ccd520fe71b3616ad37b2f`，solution_count=12。
- `openspec validate --all --strict --no-interactive`：2 changes passed，0 failed；`git diff --check` 与 secret pattern scan 通过。
- `task test:promptrepo-v03` 通过，Sonora 默认 `go.mod` 仍固定 v0.2.0 且没有 local replace；public v0.3 tag/正常 build 注册仍未执行。
