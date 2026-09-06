# 实施与验收任务

由 scripts/openspec-tasks.py 维护状态。

- [x] 1.1 新增 `writing/ai-drama-format-strategy@1.0.0`：英文模板 + contract + 中文审阅译文 + README。| evidence: en 模板 + CLI 生成 contract（4 输入）+ template-zh-CN.md（带人工审阅头）+ README；占位符与输入一一对齐
- [x] 1.2 新增 `writing/ai-drama-story-architecture@1.0.0`：beat 十字段与 draft 门禁。| evidence: 十字段 beat card 契约写入模板 §4/§5；choice/cost 缺失保持 draft 的门禁落 spec scenario；5 输入对齐
- [x] 1.3 新增 `writing/ai-drama-character-engine@1.0.0`：动机/秘密/知识边界合同。| evidence: secret/knowledge_boundary/relationships/simulation_notes 全部入输出 schema；5 输入对齐
- [x] 1.4 新增 `writing/ai-drama-showrunner@1.0.0`：proof slice 与 expansion gate。| evidence: 3 集 proof slice、每集一个核心场景合同、A/B 候选≥2 维差异、四条件 expansion gate 全部入模板；5 输入对齐
- [x] 1.5 新增 `writing/ai-drama-scene-writing@1.0.0`：可拍场景草案合同。| evidence: 动作可执行/潜台词分离/dialogue_language（默认 zh-CN）/draft_status 门禁入模板；6 输入对齐
- [x] 1.6 新增 `writing/ai-drama-critic-review@1.0.0`：同比较类与有界修复。| evidence: comparison_class_check、assessment_not_comparable、无冻结 rubric 不给综合分、单变量修复入模板与 spec scenario；4 输入对齐
- [x] 2.1 六个 solution 的结构化 metadata 全部由 Template Registry CLI 生成。| evidence: solution add / solution locale describe / contract init / contract input set 全 CLI 落盘；scene-writing 正文补占位符后经 contract refresh 重放 digest（sha256 校验一致）
- [x] 3.1 `catalog build` 与 `catalog validate --json` 通过且结果确定。| evidence: 双命令 status=success；占位符↔输入核对脚本 6/6 ALL_ALIGNED
- [x] 3.2 端到端编译至少一个做剧模板。| evidence: file 源 add→sync→search 命中 story-architecture→session create→source import→update→confirm（全 5 字段）→compile（provider_calls=0）→export→bundle verify 全链 success；编译产物 main.txt 未绑定占位符为 0
- [x] 3.3 `openspec validate official-drama-task-role-templates-v1 --strict --no-interactive` 通过。| evidence: valid（2026-09-06）
- [x] 4.1 Skill 矩阵收编在 `.skills/yeisme` 变更中落地：路由表改指 exact ref、五个任务角色 Skill 退役、解析策略增加 `template_ref_available`。| evidence: ai-drama 子仓 feat(router) 提交 + .skills/yeisme change ai-drama-task-role-consolidation-v1 7/7；validate_drama_matrix.py 与 validate_skills.py 双 PASS（16→11 Skill）；root ordo profile 与双 runtime 镜像已同步
