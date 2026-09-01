# 设计：隔离资产模板与合同

## 角色侧

`face-mask-front-v1` 继续输出 `character_asset.prompt_bundle.v1`，并由 Eikona 映射为 `face_master` / `face_master_candidate`。它只允许一个 `detail` view，正脸角度固定为 `yaw=0`、`pitch=0`、`roll=0`。

`task.isolation_mode` 为可选枚举：

- `studio_neutral`：兼容默认值。
- `transparent_subject`：人物独立透明资产。
- `environment_only`：阻断角色编译并转交背景模板。

## 背景侧

`clean-background-plate-v1` 是直接可渲染的 PromptRepo 模板，输入地点锚点、机位、时间/天气、光线、画幅和人物活动预留区。它固定 `subject_count=0`，禁止一切人物、人形痕迹和透明输出。

## 边界

人物脸模允许面部自身的自然明暗，但禁止背景投影、外部落影和悬浮阴影。背景画布必须完整不透明。人物和背景的合成只属于后续 shot/keyframe 工作流。

## 发布与回滚

内容以 `1.1.0` release candidate 交付；`1.0.0` 不重解释。回滚时移除新 profile/solution 的消费引用即可，旧 `face-master-v1` 路径继续工作。
