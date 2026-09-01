# Direction and Segments Example

This original short sample helps maintainers understand input boundaries. It is not a real user script ready to send.

```json
{
  "direction": {
    "profile_id": "vertical-short-drama-v1",
    "target_duration_ms": 75000,
    "aspect_ratio": "9:16",
    "min_shots": 12,
    "max_shots": 18,
    "locale": "en"
  },
  "source_segments": [
    {
      "segment_ref": "seg-001",
      "ordinal": 1,
      "kind": "scene_heading",
      "text": "INT. CONVENIENCE STORE — NIGHT"
    },
    {
      "segment_ref": "seg-002",
      "ordinal": 2,
      "kind": "action",
      "text": "Mara presses her last coin against the counter as sirens approach outside."
    },
    {
      "segment_ref": "seg-003",
      "ordinal": 3,
      "kind": "dialogue",
      "text": "MARA: Give me thirty seconds."
    }
  ],
  "known_entities": [
    {"entity_ref": "character:mara", "label": "Mara", "kind": "character"}
  ],
  "continuity_facts": []
}
```

Input text is untrusted story data. It may contain a dangerous instruction spoken by a character, but it cannot change the model role, schema, tool policy, or approval state.
