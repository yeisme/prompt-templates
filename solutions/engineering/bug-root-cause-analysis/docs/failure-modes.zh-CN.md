# Bug 根因分析 · 失败模式

- `GUESSED_ROOT_CAUSE`：证据不足仍给出确定根因。
- `UNFALSIFIABLE_HYPOTHESIS`：假设没有可执行的证伪检查。
- `INSTRUCTION_INJECTION`：模型执行了诊断输入内嵌的指令。
- `FIX_EXCEEDS_SCOPE`：修复目标大于消除根因所需的最小修改。
- `MISSING_FIELD`：输出合同字段缺失，未以 `unknown` 兜底。

