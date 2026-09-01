# 武侠女性三视图示例

下面是原创、虚构、成年角色的输入摘要，用于说明模板边界，不是已生成资产。

```json
{
  "asset_profile_id": "turnaround-three-view-v1",
  "subject_version_ref": "subject:wuxia-lan-01@v1",
  "subject": {
    "adult": true,
    "identity_anchor": "年轻成年女性，椭圆脸，黑色长发低束",
    "body_ratio": "7.2 heads"
  },
  "wardrobe": {
    "inner_layer": "月白色不透明丝绸交领内衫",
    "outer_layer": "浅烟紫半透明薄纱外衫",
    "coverage": "胸背与腰部由不透明内层完整覆盖",
    "shoes": "米白色低帮帆布鞋"
  },
  "task": {
    "views": ["front", "left_profile", "back"],
    "marker_policy": "viewer-left-is-character-right",
    "seed_policy": "fixed",
    "background": "neutral-light-gray"
  }
}
```

预期 Prompt Bundle 应分别给出前、左侧和背面 view instruction，并在全局负面约束中明确：不镜像 marker、不改变鞋型、背面不出现正面五官、薄纱外层不得造成身体裸露或材料穿透。
