# 失败模式：贴地姿势库

| 失败模式 | 表现 | 处理 |
| --- | --- | --- |
| 主体左右混入 | his/her/their left 出现，模型镜像出错 | 渲染脚本 fail-closed 拦截；改写为 frame-left / frame-right 或 one side 中性表述 |
| 部位缺段 | 只写腿和手，躯干或重心句丢失 | 四句齐绑；脚本校验四字段非空且句号结尾 |
| 风格词泄漏 | 姿势句里混入镜头、光线、服装、风格词 | 删掉相关词；脚本 ban 词表校验（camera/lens/light/wardrobe 等） |
| 与风格层冲突 | 姿势要求仰头但风格层要求低头对视 | 优先保姿势库的部位事实；风格层的神态条款改用与姿势兼容的表述（如 distant gaze 而非 eye contact） |
| 家族误配 | 需要跪撑类却选了侧坐类 | 按 `docs/pose-spec.md` 家族表选型；同族内再比对重心/轮廓句 |
| 机位方向歧义 | "toward frame right" 被读成主体右侧 | 保持 frame- 前缀完整拼写；不要缩写为 left/right 裸词 |
