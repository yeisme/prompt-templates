# 贴地姿势句模板（人工审阅译文）

> 本文档是人工审阅译文，不进入编译。编译与投递只使用 `prompts/main.en.md`。

本模板编译一条标准化的英文姿势句，描述坐、跪、卧或其过渡的贴地姿势，用作任何图像提示词风格层的 pose 槽位。25 个已审阅姿势在 `assets/poses/*.json`；成品可复制句在 `examples/<id>/pose-clause.en.md`。

方向一律 camera-relative：`frame-left` / `frame-right` 指观众看到的画面左/右，绝不使用人物自身的左右。绑定全部变量后渲染；渲染结果是可直接复制的动作句，不再改写。

**贴地姿势句模板：**

> {{pose_lead}} {{lower_limbs}} {{upper_limbs}} {{torso_head}} {{weight_silhouette}}
>
> 即：引导短语（姿势名 + 冒号）→ 下肢句 → 上肢句 → 躯干与头部句 → 重心与轮廓句。

## 自检

- 四个部位句齐全且顺序固定：下肢、上肢、躯干与头部、重心与轮廓。
- 方向只用 frame-left / frame-right；不出现人物自身左右。
- 全句读起来是一口气的观察描述；不混入镜头、光线、服装或风格词汇。
