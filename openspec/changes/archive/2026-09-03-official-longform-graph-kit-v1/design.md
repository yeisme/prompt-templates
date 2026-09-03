## Context

官方仓拥有内容和 taxonomy，不拥有 Auctra workspace 或 Registry state。Graph Kit 必须作为一个 atomic solution/release 分发：任一 required child 变化都产生新 Kit version，不能独立更新 lens/view/schema 后仍复用旧 manifest version。

## Goals / Non-Goals

**Goals:**

- 提供可被 Promptrepo exact structured document flow 读取的完整通用 Graph Kit。
- 让 Registry 对整个 closure 做 publish/install/Git export/restore。
- 以跨题材 synthetic fixtures 证明不硬编码《逆誓龙王》。 

**Non-Goals:**

- 不保存私有 Overlay、source refs、项目 fixture 或生成内容。
- 不调用模型、provider 或自动接受任何 Auctra review。

## Decisions

### D1：一个 atomic solution/release

Solution ID 为 `longform.generic.v2`，manifest 锁定所有 required child exact refs/digests。任何 required child bytes 变化都 bump solution version，避免拼装未测试组合。

### D2：中文 canonical、机器 ID 稳定英文

Guide、review checklist 和 failure guidance 使用中文；schema fields、panel IDs、error codes、capabilities、rights、maturity 和 address 使用稳定英文。

### D3：fixtures 只用 synthetic scenario

至少包含一个跨题材 valid fixture，以及 missing ID、duplicate identity、dangling relation、state conflict、source drift、HTML sentinel、missing child 和 digest drift 负例。Fixtures 不复制 Nishi 字段值或绝对路径。

### D4：全部 metadata 由 Registry CLI author

先人工撰写内容 source，再使用 `catalog solution init/template add`、`document init/artifact add`、`fixture set init/case add` 和 release authoring commands 生成结构化 assets；不得手写 digest/manifest。

## Risks / Trade-offs

- [Kit 内容与 Auctra compiler 漂移] → compatibility 声明、exact Promptrepo/Registry version、Auctra conformance test。
- [官方内容混入项目专用 schema] → synthetic cross-genre fixture、private sentinel scan 和禁止项目路径规则。

## Migration Plan

1. 等待/验证 Promptrepo conformance 与 Registry structured authoring 能力。
2. 创建中文 source 内容并由 Registry CLI 生成完整 metadata/fixtures。
3. build/validate catalog，生成 local immutable release closure。
4. Auctra 使用 exact local Git/CAS release 完成 upgrade/rollback。

回滚：Auctra repin previous exact version；官方仓保留旧 version 不修改。

## Open Questions

无。
