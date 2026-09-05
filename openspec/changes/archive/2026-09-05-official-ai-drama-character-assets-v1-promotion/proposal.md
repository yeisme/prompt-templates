# 提案：ai-drama-character-assets v2 晋升正式 v1

## 问题

`ai-drama-character-assets`（旧 1.x：main/isolated-character-assets-v1/staged-character-production-v2 角色）与 `ai-drama-character-assets-v2`（模块化 7 角色）并存。旧 1.x 包的 fixture 集与 Registry fixture 门存在不可调和冲突（valid 输出禁止 `*ref` 键 vs 1.x 合同要求 `subject_version_ref`），其内容已被模块化 family 完全承接，维护双包只产生持续阻塞。

## 变更

- 删除旧 1.x 目录（含 `face-master-v1`、`face-mask-front-v1` 等角色、templates/profiles/examples 与其 fixture 集）。
- `ai-drama-character-assets-v2@2.0.0` 内容整体晋升为正式 `ai-drama-character-assets@1.0.0`（无后缀目录，7 角色 × zh-CN/en，31 fixture cases），全部结构化 metadata 经 Registry CLI 重放生成。
- 共享 schema `character_asset.modular_slot_bundle.v1` 的 `$id` 去除 `-v2`；`ai-drama-background-assets-v2` 对该 schema 的 document/fixture 绑定经 `document schema rebind` + `fixture set refresh` 级联更新。
- 建立版本命名规则：正式版本用无后缀 id 从 1.0.0 起版；非正式（未转正）版本的目录名或版本号必须带 `beta`/`alpha` 标识（写入 AGENTS.md 与 docs/authoring.md）。
- 退役描述旧 1.x 内容的两个 spec（`official-ai-drama-character-asset-templates`、`official-ai-drama-staged-character-assets`）；`official-modular-character-asset-templates` 的版本引用改为 `@1.0.0`，并承接"元 Prompt 不得直接进入图片 Provider"要求。

## 兼容性

- 旧 1.x hairstyle/turnaround 类 ref（如 `…ai-drama-character-assets@1.0.0#hairstyle-sheet-v1`）按 compat-only 遗留输入处理（`legacy-hairstyle-compat` fixture 保持该语义）。
- Scaena/Eikona 官方 canary 消费面需从旧 1.x 角色迁移到模块化角色（外部仓任务，见 tasks）。
- `ai-drama-background-assets-v2@2.0.0` 身份不变（仅 schema 绑定 digest 级联）；`ai-drama-background-assets@1.x` 不变。
