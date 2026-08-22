# Short-drama Character-consistent Shot Prompt

Using `{{character_bible}}`, `{{reference_assets}}`, `{{shot_intent}}`, and `{{previous_shot}}`, produce a video-shot prompt that preserves character continuity.

Hard constraints:

- Preserve face shape, hair, costume, age, body type, signature items, and screen direction.
- Specify shot size, camera position, movement, duration, action boundaries, and emotional change.
- Do not add undeclared characters, props, injuries, or costume changes.
- If inputs conflict, report the conflict and choose a conservative option instead of rewriting the character bible.

Output: main shot prompt, continuity locks, negative constraints, repair prompt, human review points.
