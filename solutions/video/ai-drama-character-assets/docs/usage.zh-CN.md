# 使用说明

本 solution 把已校验的角色、服装、任务、参考绑定和连续性约束编译为 `character_asset.prompt_bundle.v1`。它适合角色母版、三视图、服装/表情/动作 sheet、道具/场景资产、分镜关键帧和有界连续性修复。

## 先按依赖排产

不要按 preset 目录顺序排队。推荐顺序是：

```text
face-master
→ expression-sheet
→ body-master
→ 基础服装正面主视图
→ 独立侧面图
→ 独立背面图
→ 本地 turnaround 联系表
→ 其余 wardrobe ∥ 多发型 hairstyle/relock
→ action-sheet
→ prop-scene-sheet
→ shot-keyframe
```

表情表只依赖 accepted face master。基础发型随 face identity 锁定；只有确实需要多个发型时才增加 hairstyle task。Turnaround 不再一次生成三宫格：先接受穿基础服装的正面主视图，再逐张生成侧面和背面。

## Character master 推荐流程

1. 兼容流程继续生成 `face-master-v1`：正面平视、中性表情、肩部以上、干净背景；人工确认脸型、五官、肤色、发际线、基础发型和永久 marker。
2. 使用 exact accepted face master 生成一张 `body-master-v1`：正面全身、中性站姿、完整头脚；只接受身体比例，不接受剧情服装。
3. 使用 accepted face/body 生成 `turnaround-three-view-v1` 的 front：这是穿基础服装的角色主视图。
4. Front 通过后，分别生成 `left_profile` 和 `back`。每次 Provider job 只允许一个 view 和一个候选 artifact。
5. Eikona 按稳定顺序把三张单图拼成 1×3 审稿联系表；联系表只用于 review，不替代单图 acceptance 或返修。

仓库的 `main` Prompt 是编译说明，目标是输出 `character_asset.prompt_bundle.v1`，不能直接发送给图片模型。图片模型只能接收 Eikona 从已验证 Bundle 渲染出的单视图 Prompt。

## 正脸面具式脸模流程

1. 选择 `face-mask-front-v1`，并把 `task.isolation_mode` 设为 `transparent_subject`。
2. 输入只允许一个成年原创角色身份；人物头部锁定 `yaw=0`、`pitch=0`、`roll=0`，双眼水平并直视镜头。
3. 画面只保留完整脸部、双耳、自然发际线和少量向后贴合的基础头发轮廓；沿完整下颌线收口，不出现脖子、肩膀、衣服或领口。
4. Eikona 为该 profile 单独渲染 Provider Prompt，不修改通用 `detail` 构图。
5. `quality.check` 使用 `transparent_required=true`、`min_transparent_fraction=0.10`、`aspect_ratio=1:1`、`min_width=1024`、`fail_mode=block`。
6. 人工检查绝对正脸、脸部完整、无发饰首饰、无背景残留，以及透明边缘无白边或黑边。

人物候选通过 Eikona review 只表示当前候选可继续使用，不等于 Scaena `frozen` 或 production accepted。

推荐流程：

1. Auctra/故事 owner 提供已接受的角色与场景 refs。
2. Scaena 或视觉生产 owner 选择 `asset_profile_id` 并冻结 task、layout、reference roles 和 QC。
3. Promptrepo provider-free inspect、contract validate 和 render。
4. 用户确认故事脊柱、逐镜节拍、对白主干、视觉基调和时长合同后，Eikona 才可进入实际生成审批。
5. Eikona 使用 canonical 模型引用 `openai/gpt-5.4-image-2` 执行已批准任务，并保存自己的资产、成本和 evidence。
6. 视觉候选经过身份、材料、方向、构图和连续性审查后，才可由资产 owner 接受。

## Expression sheet 推荐流程

1. Scaena/视觉 owner 提供 exact accepted face master ref、digest 和 capture lock。
2. Prompt compiler 输出六个独立 expression views；每个 view 恰好一个主体和一个表情 delta。
3. Eikona 用 canonical model `openai/gpt-5.4-image-2` 执行独立任务，不让 provider 生成六格网格或文字。
4. 每格独立审查；失败格最多生成两个有界 repair candidates。
5. 使用稳定 artifact title 拼接 3×2 联系表：

```bash
eikona review contact-sheet <run_id> --cols 3 --agent
```

6. 人工接受单格和 review packet；contact sheet 只用于审稿，不能替代 face master。

Quick preview 可以临时生成一张六格图，但必须标记 non-production，不能跳过独立 cell、逐格 QC、exact ref/digest 或 human review。

`fixed`/`family_locked` seed 只描述重跑和比较策略。它不能替代 identity reference，也不能保证远端 provider 像素级复现。

同机位六表情不是 LoRA-ready dataset。若要训练角色模型，应创建独立数据集 profile，并补充训练权利、来源 lineage、去重和跨角度/景别/光线覆盖。

本仓库不保存用户图片、SubjectVersion、Provider credential、成本回执或 production acceptance。
