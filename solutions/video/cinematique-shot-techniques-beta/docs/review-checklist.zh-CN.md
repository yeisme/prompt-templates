# 审阅清单

渲染结果投递前逐项核对：

- [ ] `technique_id` 在 `assets/index.json` 中存在，且与 `technique_name`、`technique_prompt_bound` 三者同源一个 spec。
- [ ] `technique_prompt_bound` 与 spec `prompt_template` 逐字一致，唯一差异是 `[Subject]` → `subject`。
- [ ] `subject` 是具体、可拍的描述；渲染结果无 `[Subject]`、无未解析变量残留。
- [ ] 一条主技术；`extra_directives` 只调投递参数（时长/画幅/节奏），未混入第二条技术的 prompt 文本。
- [ ] 技术的镜头/胶片/灯光语言未被改写或稀释。
- [ ] `target` 与投递面一致：video 保留运动语言一次且一致；image 丢弃纯运动语言。
- [ ] spec `common_mistakes` 三条逐条对照，当前镜头不命中任何一条。
- [ ] 负面清单生效（默认或覆盖），与技术的灯光/镜头语言不冲突。
- [ ] 对外再导出时保留 `source` 署名块（见 provenance）。
