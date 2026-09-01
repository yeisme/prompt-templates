# 人工审查清单

## 身份与身体

- 是否只有一个有效 identity source？
- 五官、发型、肤色区间和身体比例是否跨视图一致？
- 是否明确为成年角色，且没有用妆容或服装代替身份？
- Face master 是否仍是身份真源，而不是被 expression、wardrobe 或 shot artifact 替代？

## 服装与材料

- 内外层、颜色、材料、闭合方式和鞋型是否一致？
- 透明或半透明材料是否有合法的不透明内层 coverage？
- 是否新增了品牌、Logo、铭文或未授权设计？

## 构图与连续性

- marker、左右方向、屏幕方向和旋转方向是否正确？
- 每个 Provider job 是否只生成一个 view、一个人物实例和一张候选图？
- 正面主视图是否在人审通过后才允许侧面和背面进入生成？
- 多视图单图是否等比例、同镜头距离，且背面确实没有正面五官？
- 1×3 联系表是否由本地 renderer 拼接，并保留三个 source artifact refs？
- 道具手、动作阶段、背景锚点和光源方向是否连续？

## Character master 生成前

- Face master 是否为一张正面平视、中性表情、干净背景的独立 bust，而不是多宫格或服装表？
- Body master 是否绑定 exact accepted face master，并且只使用中性基础层？
- Turnaround front 是否绑定 accepted face/body，并被明确标为 base-wardrobe 主视图？
- Side/back 是否同时绑定 accepted face、body 和 front master 的 exact version/digest？
- 输入是否为已验证的 `character_asset.prompt_bundle.v1` 单视图渲染结果，而不是仓库 `main` 编译元 Prompt？

## Expression sheet 生成前

- 是否绑定 exact accepted face master，并保留 version/digest/approval evidence？
- 是否为 `subject_count=1`、`depiction_count=6`？
- Production 是否使用六个独立 cells，而不是要求 provider 生成一张六格图？
- 是否提供正面平视、bust 裁切、head pose、gaze target、人物占比、曝光和光源方向的 capture lock？
- 基础发际线和基础发型是否锁定？若更换发型，是否已转入 hairstyle/relock task？
- `wardrobe_json` 是否为空或只含 non-canonical presentation，而没有提前接受服装？
- 六个 view keys、标签和 `0..4` 单值强度是否完整、唯一、稳定排序？

## Expression sheet 逐格审查

- 每个 artifact 是否恰好一个成年主体、一个 bust portrait、一个表情 delta？
- 脸型、五官间距、肤色、泪痣、发际线和基础发型外轮廓是否保持不变？
- Head pose、gaze target、肩线、裁切、曝光和背景是否与 baseline 一致？
- 是否只改变眉部、眼睑、眼周湿润度、嘴唇、下颌/面颊张力和呼吸观感？
- 是否出现妆容、首饰、服装设计、文字或其他未授权元素？
- 表情是否符合标签和强度，且没有用露齿、泪水滑落、后仰或换光线过度表达？

## Expression sheet 跨格审查

- 六格并排时是否仍可明确判定为同一个人？
- Neutral 是否可作为其他五格的可靠 baseline？
- 各表情是否可辨认，是否存在 range collapse 或 range overshoot？
- Contact sheet 标签是否来自 artifact title，而不是模型生成文字？
- 单格 repair 是否保留其他五格和原始 reference lineage？
- 两格以上同时漂移时，是否已升级为 baseline blocker，而不是继续逐格堆 Prompt？
- Contact sheet 是否只作为 review derivative，未被注册为 face identity source？

## 参考与安全

- 每个参考是否只承担声明的 role？
- 是否混入 DRAFT、stale、rejected 或 version/digest 不匹配的引用？
- Prompt 是否含 credential、Provider、成本、执行、acceptance 或伪造 receipt？

Prompt Bundle 通过结构检查不等于图片已生成，也不等于视觉质量或生产接受已经通过。

Expression sheet 通过审查也不等于 LoRA-ready。训练用途必须另行检查训练权利、来源、去重和角度/景别覆盖。
