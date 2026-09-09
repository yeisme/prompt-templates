# Cinematique Shot Technique Prompt (single technique)

This template renders one film technique from the Cinematique library (`assets/techniques/`) into a ready-to-deliver shot prompt for an AI image or video generator. The consumer selects a technique, binds its library prompt to the subject, and renders; the rendered result is the final generation prompt body and must not be rewritten afterwards.

Library provenance: 150 techniques vendored from vvsvs.pro/cinematique (Free Tool — Open Source; built on grokfilm.app by Tetsuo Corp, remixed & expanded by VVSVS). Keep the `source` attribution block when re-exporting technique content.

## How to use

1. Select one technique per shot. Pick by category (Camera Work / Lighting / Composition / Editing / Storytelling / Visual Effects & Promptable FX / Genres & Styles), mood, and narrative intent — the index is `assets/index.json`; each spec carries `when_to_use` and `common_mistakes` as selection guardrails. `technique_id` must be one of the contract enum values.
2. Bind the subject: take the spec's `prompt_template` and replace the `[Subject]` placeholder with `{{subject}}` (a character, object, or scene description). The bound text becomes `technique_prompt_bound`. Do not edit any other part of the library prompt — the lens, film stock, and lighting language are the technique.
3. Apply the spec's `directing_the_ai` and `common_mistakes` while reviewing the rendered prompt; they are the acceptance criteria for this shot, not decoration.
4. `{{target}}` states the delivery surface: `image` keeps the prompt as one still frame direction; `video` additionally honors any motion language the technique prompt contains.

## Technique

Technique: `{{technique_name}}` (id: `{{technique_id}}`, category: see index). Difficulty and moods live in the technique spec; the selection rationale should reference the spec's `when_to_use`.

## Prompt body (bound library prompt)

{{technique_prompt_bound}}

## Consumer directives

Target surface: `{{target}}`. Additional per-shot directives: {{extra_directives}}

Default directives (merged unless overridden by `extra_directives`): preserve the technique's stated camera, lens, and lighting language exactly; keep one dominant visual device per shot; do not stack a second technique's prompt fragment into the same delivery.

## Negative prompts

{{negative_prompts}}

Default negatives (merged unless overridden by `negative_prompts`): cluttered frame, extra limbs, deformed faces, text, watermark, logo, UI overlay; contradicting the technique's stated lighting or camera language.

## Post-render self-check

1. `technique_id` exists in `assets/index.json`; the bound prompt is the spec's `prompt_template` verbatim except for the `[Subject]` substitution.
2. `{{subject}}` is a concrete, filmable description; no `[Subject]` placeholder and no unresolved template variable survives in the rendered result.
3. Exactly one technique drives the shot; `extra_directives` adjusts delivery parameters, never a second technique's prompt text.
4. The rendered prompt still carries the technique's camera/lens/film/lighting language; it was not paraphrased away.
5. For `target=video`, motion implied by the technique is stated once and consistently; for `target=image`, motion-only language is dropped rather than contradicted.

Honest fallback: when `technique_id` is not in the index, or the spec prompt cannot be bound to a concrete subject, stop rendering and list the gap; never invent a technique, never deliver an unbound `[Subject]`.
