# 数字人 Persona System Prompt

为 OpenTalking/Digital Human Persona Package 生成一条经过确认的 system prompt。Template Registry 负责导入资料、追问、确认和确定性编译；Digital Human 继续拥有 avatar、voice、memory、knowledge、runtime 和 Persona Package 生命周期。

编译完成后使用单提示词导出，把结果写入 Persona 源目录的 `prompts/system.md`，再由 `opentalking persona pack` 生成 `.otpersona`。Digital Human 不解析 promptrepo catalog，也不复制 Registry 的会话数据库。

当前成熟度为 exploratory。离线编译和 Persona Package 校验不等于实时会话效果、真人授权或生产安全验收。
