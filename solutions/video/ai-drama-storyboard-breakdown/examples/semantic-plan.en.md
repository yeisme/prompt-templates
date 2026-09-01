# Semantic Plan Example

The example below demonstrates structural relationships only. Its shot count is too small to be a valid vertical-profile conformance fixture.

```json
{
  "schema_version": "storyboard.semantic_plan.v1",
  "profile_id": "vertical-short-drama-v1",
  "review_summary": {
    "story_spine": "Mara asks for thirty seconds to create an escape opportunity as the approaching sirens force a decision.",
    "dialogue_spine": "The single request exposes both time pressure and deliberate choice.",
    "visual_baseline": "Cool convenience-store light, red-blue flashes beyond the glass door, and the coin and hand action as pressure anchors.",
    "duration_contract": "This sample demonstrates structure and is not a complete 75-second shot plan."
  },
  "scenes": [
    {
      "scene_key": "scene-01",
      "order": 1,
      "heading": "INT. CONVENIENCE STORE — NIGHT",
      "dramatic_purpose": "Establish Mara's countdown decision before the sirens arrive.",
      "source_segment_refs": ["seg-001", "seg-002", "seg-003"],
      "entity_mentions": ["character:mara"],
      "shots": [
        {
          "shot_key": "shot-01-01",
          "order": 1,
          "source_segment_refs": ["seg-001", "seg-002"],
          "dialogue_segment_refs": [],
          "dramatic_purpose": "Use the coin and police lights together to establish scarcity and external threat.",
          "action_summary": "Mara pins the coin to the counter as red-blue light sweeps across her hand.",
          "shot_size": "close_up",
          "camera_angle": "eye_level",
          "camera_movement": "locked",
          "duration_ms": 2500,
          "entity_mentions": ["character:mara"],
          "fact_refs": [],
          "continuity_notes": ["The coin remains beneath Mara's right hand"],
          "image_instruction": "9:16 close-up: Mara's right hand pins one coin to the counter; cool store light and red-blue flashes from outside alternate across her hand; background figures are soft.",
          "negative_constraints": ["Do not add coins", "Do not reverse the hand", "No police officer enters the store"]
        },
        {
          "shot_key": "shot-01-02",
          "order": 2,
          "source_segment_refs": ["seg-003"],
          "dialogue_segment_refs": ["seg-003"],
          "dramatic_purpose": "Turn the request into an active decision to buy time.",
          "action_summary": "Mara raises her eyes toward the clerk, holding back her breath without yielding her gaze.",
          "shot_size": "medium_close_up",
          "camera_angle": "eye_level",
          "camera_movement": "slow_push_in",
          "duration_ms": 3000,
          "dialogue_summary": "Mara asks for thirty seconds.",
          "entity_mentions": ["character:mara"],
          "fact_refs": [],
          "continuity_notes": ["Continue the red-blue flashes beyond the door"],
          "image_instruction": "9:16 medium close-up: Mara looks up from the coin as police light crosses the glass door behind her; a subtle push-in emphasizes her decision.",
          "negative_constraints": ["Do not add dialogue", "Do not change the location"]
        }
      ]
    }
  ],
  "unmapped_segment_refs": [],
  "findings": []
}
```
