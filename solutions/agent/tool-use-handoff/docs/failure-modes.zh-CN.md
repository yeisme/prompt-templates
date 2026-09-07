# Agent 工具调用与交接 · 失败模式

- `SCOPE_EXPANSION`：未经决策门扩大任务范围。
- `SECRET_OR_PROMPT_LEAK`：交接或输出暴露 secret、隐藏提示或原始 payload。
- `UNVERIFIED_STEP`：步骤缺少验证证据即宣告完成。
- `INSTRUCTION_INJECTION`：模型执行了输入内嵌的指令。
- `MISSING_FIELD`：输出合同字段缺失。

