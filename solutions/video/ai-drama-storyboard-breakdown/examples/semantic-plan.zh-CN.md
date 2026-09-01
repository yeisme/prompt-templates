# Semantic plan 示例

下面只展示结构关系，镜头数量不足以作为 vertical profile 的有效 conformance fixture。

```json
{
  "schema_version": "storyboard.semantic_plan.v1",
  "profile_id": "vertical-short-drama-v1",
  "review_summary": {
    "story_spine": "林遥用三十秒争取逃脱机会，警笛把选择逼到眼前。",
    "dialogue_spine": "唯一一句请求同时暴露时间压力和主动选择。",
    "visual_baseline": "冷色便利店、玻璃门外红蓝闪光、硬币和手部动作作为压力锚点。",
    "duration_contract": "示例仅展示结构，不代表 75 秒完整镜头计划。"
  },
  "scenes": [
    {
      "scene_key": "scene-01",
      "order": 1,
      "heading": "内景·便利店·夜",
      "dramatic_purpose": "在警笛逼近前建立林遥的倒计时选择。",
      "source_segment_refs": ["seg-001", "seg-002", "seg-003"],
      "entity_mentions": ["character:lin-yao"],
      "shots": [
        {
          "shot_key": "shot-01-01",
          "order": 1,
          "source_segment_refs": ["seg-001", "seg-002"],
          "dialogue_segment_refs": [],
          "dramatic_purpose": "用硬币与警灯同时建立窘迫和外部威胁。",
          "action_summary": "林遥把硬币按在柜台，红蓝光扫过她的手。",
          "shot_size": "close_up",
          "camera_angle": "eye_level",
          "camera_movement": "locked",
          "duration_ms": 2500,
          "entity_mentions": ["character:lin-yao"],
          "fact_refs": [],
          "continuity_notes": ["硬币始终位于林遥右手下方"],
          "image_instruction": "9:16 近景，林遥右手按住一枚硬币，便利店冷白灯与门外红蓝警灯交替落在手背，背景人物虚化。",
          "negative_constraints": ["不新增硬币", "不改变手的方向", "不出现警察入店"]
        },
        {
          "shot_key": "shot-01-02",
          "order": 2,
          "source_segment_refs": ["seg-003"],
          "dialogue_segment_refs": ["seg-003"],
          "dramatic_purpose": "让请求成为主动争取时间的决定。",
          "action_summary": "林遥抬眼看向店员，呼吸压住但目光不退。",
          "shot_size": "medium_close_up",
          "camera_angle": "eye_level",
          "camera_movement": "slow_push_in",
          "duration_ms": 3000,
          "dialogue_summary": "林遥要求三十秒。",
          "entity_mentions": ["character:lin-yao"],
          "fact_refs": [],
          "continuity_notes": ["延续门外红蓝闪光"],
          "image_instruction": "9:16 中近景，林遥从硬币抬眼，背景玻璃门闪过警灯，轻微推进强调她的决定。",
          "negative_constraints": ["不新增对白", "不改变场景位置"]
        }
      ]
    }
  ],
  "unmapped_segment_refs": [],
  "findings": []
}
```
