# 失败模式

| 现象 | 稳定处理 |
|---|---|
| 主体年龄不明确 | `ADULT_SUBJECT_REQUIRED`，停止生成 |
| 多个身份来源冲突 | `IDENTITY_SOURCE_CONFLICT`，请求 owner 选择 |
| 固定任务缺少 seed policy | `FIXED_SEED_REQUIRED`，补齐 task |
| 左右 marker 与参考镜像 | `MARKER_MIRROR_CONFLICT`，不得自行翻转 |
| 半透明外层缺少内层覆盖 | `MATERIAL_COVERAGE_INVALID`，修正 wardrobe |
| 背面出现正面五官或胸前结构 | `BACK_VIEW_CONFLICT`，回到 layout/QC |
| 鞋型或关键配件漂移 | `WARDROBE_CONTINUITY_DRIFT`，有界修复 |
| 使用 DRAFT/stale reference | `REFERENCE_NOT_PRODUCTION_READY`，更换 exact accepted ref |
| production task 使用 replace override | `PRODUCTION_REPLACE_OVERRIDE_FORBIDDEN`，拒绝执行 |
| 未知字段或 Provider 参数进入 bundle | `PROMPT_BUNDLE_FORBIDDEN_FIELD`，provider call 前失败 |
| 把仓库 main 编译元 Prompt 直接发送给图片模型 | `CHARACTER_ASSET_META_PROMPT_FORBIDDEN`，改为读取已验证 Bundle 的单视图输出 |
| Production 要求 Provider 一次生成三视图宫格 | `CHARACTER_ASSET_PROVIDER_GRID_FORBIDDEN`，拆成独立 view jobs 并本地拼联系表 |
| Body master 缺少 accepted face master | `CHARACTER_ASSET_UPSTREAM_NOT_ACCEPTED`，先完成脸模人审 |
| 侧面或背面缺少 accepted base-wardrobe front | `CHARACTER_ASSET_UPSTREAM_NOT_ACCEPTED`，先接受正面主视图 |
| 旧 Bundle 的 composition 仍写“三格等宽” | `LEGACY_MULTI_PANEL_LAYOUT_NORMALIZED`，production compiler 正规化为单视图 composition |
| Expression task 缺少 accepted face master | `FACE_MASTER_REQUIRED`，不得用 body/wardrobe/expression artifact 替代身份真源 |
| Production expression 请求一次生成六格图 | `EXPRESSION_SET_INVALID`，改为六个独立 cells 加确定性联系表 |
| 表情标签重复、缺失或 depiction 数不匹配 | `EXPRESSION_SET_INVALID`，修正稳定 view keys 和 required cell set |
| 表情强度为范围、文本级别或超出 0..4 | `EXPRESSION_INTENSITY_INVALID`，改为单个整数 |
| 表情 instruction 改变 head pose、肩线、裁切或 gaze lock | `EXPRESSION_CAPTURE_CONFLICT`，只保留脸部肌肉 delta |
| Expression task 顺带更换发髻或束发 | `HAIRSTYLE_RELOCK_REQUIRED`，进入独立 hairstyle/relock task |
| 单格换脸、泪痣/发际线/基础发型漂移 | `EXPRESSION_IDENTITY_DRIFT`，保持 exact refs 并有界修复该格 |
| 多个标签生成近乎相同的表情 | `EXPRESSION_RANGE_COLLAPSE`，只增强相应 cell 的可观察肌肉差异 |
| 表情超出档位、出现滑落泪水、露齿怒吼或身体反应 | `EXPRESSION_RANGE_OVERSHOOT`，只降低该格强度 |
| 两格以上同时发生身份或 capture 漂移 | 升级为批次级 baseline blocker，检查 face master、binding 和 capture lock |
| 把 expression sheet 标记为 LoRA-ready dataset | 拒绝训练就绪声明，转入独立 dataset profile 和 rights/coverage gate |

权限、费用、digest、owner revision 或 acceptance blocker 不能通过重写 Prompt 绕过。
