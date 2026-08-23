## 1. Foundation

- [x] 1.1 建立 AGENTS、CLAUDE、README、docs、OpenSpec 和 private remote；validation：repository review。
- [x] 1.2 使用维护命令初始化 repository.json；validation：repository init JSON success。

## 2. Initial catalog

- [x] 2.1 编写十二类 zh-CN source Prompts；validation：content review。
- [x] 2.2 编写十二类 en reviewed adaptations；validation：contract parity review。
- [x] 2.3 使用 `solution add` 生成每个 locale metadata；validation：solution count/locale count。

## 3. Build and release

- [x] 3.1 build/validate catalog，并确认相同输入 digest 稳定；validation：两次 build digest 相同。
- [x] 3.2 运行 strict OpenSpec validation 和 secret/path audit；validation：all pass。
- [x] 3.3 commit/push main，并保留 private visibility；validation：remote main/head check。

## Evidence

- Catalog：12 solutions、24 locale Prompt Markdown，catalog digest `sha256:d252148bb4e4f6be95f99848dd49bad43b6414f4b7ccd520fe71b3616ad37b2f`。
- Determinism：连续两次 build 的 `catalog.json` SHA-256 均为 `f78319451fdfdc62eac569ea3884823faed5080d189267b4ad496ed1b1c33e95`。
- Validation：`template-registry catalog validate --repository . --json`、`openspec validate --all --strict` 与 secret/path audit passed。
- Public SDK cutover canary：Template Registry 分别消费 `github.com/yeisme/promptrepo@v0.2.0-rc.1` 与 stable `v0.2.0` 后重新 validate/build；catalog digest 与文件 SHA-256 均保持不变。
