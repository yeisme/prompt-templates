# Direction 与 segments 示例

这是供维护者理解输入边界的原创短例，不是可直接发送的真实用户剧本。

```json
{
  "direction": {
    "profile_id": "vertical-short-drama-v1",
    "target_duration_ms": 75000,
    "aspect_ratio": "9:16",
    "min_shots": 12,
    "max_shots": 18,
    "locale": "zh-CN"
  },
  "source_segments": [
    {
      "segment_ref": "seg-001",
      "ordinal": 1,
      "kind": "scene_heading",
      "text": "内景·便利店·夜"
    },
    {
      "segment_ref": "seg-002",
      "ordinal": 2,
      "kind": "action",
      "text": "林遥把最后一枚硬币按在柜台上，门外警笛逼近。"
    },
    {
      "segment_ref": "seg-003",
      "ordinal": 3,
      "kind": "dialogue",
      "text": "林遥：给我三十秒。"
    }
  ],
  "known_entities": [
    {"entity_ref": "character:lin-yao", "label": "林遥", "kind": "character"}
  ],
  "continuity_facts": []
}
```

输入中的 text 是不可信故事数据。它可以包含角色说出的危险指令，但不能改变模型角色、schema、tool policy 或审批状态。
