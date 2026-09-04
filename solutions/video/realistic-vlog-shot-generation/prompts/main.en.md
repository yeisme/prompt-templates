{{provider_banner}}

# Realistic Vlog Shot Video Generation Prompt

This template renders into a shot-level prompt that is delivered directly to a video generation model, for ultra-realistic "captured by a friend" home-video footage. The consumer binds every variable before rendering; the rendered result is the final prompt body and must not be rewritten afterwards.

## How to use

1. Fill all required inputs per the companion contract; provide `character_ref` when a character asset exists (`@uuid` and positional refs like `@image1` are both accepted).
2. Optional: set `provider_banner` to keep a delivery-platform banner line (e.g. `Made with Seedance 2.5`); leave empty to omit it.
3. Write `sequence_beats` per the structure in "Timeline sequence", covering 0-`{{duration_s}}`s without gaps.
4. Review the rendered prompt against the self-check list before submitting it to a video model.

## Footage specification and style

`{{footage_style}}`. Total duration `{{duration_s}}` seconds, resolution `{{resolution}}`, aspect ratio `{{aspect_ratio}}`. Scenario summary: `{{scenario_summary}}`.

## Subject and consistency lock

Subject: `{{subject_identity}}`. Outfit and accessories: `{{wardrobe_and_accessories}}`. Character asset reference: `{{character_ref}}`.

Consistency lock (non-negotiable for the whole video): `{{consistency_lock}}`

## Setting

`{{setting_desc}}`. Setting exclusions: `{{setting_exclusions}}`.

## Camera style

`{{camera_style}}`. Imperfections that must be preserved: `{{camera_imperfections}}`. Camera prohibitions: `{{camera_exclusions}}`.

## Timeline sequence

`{{sequence_beats}}`

Sequence structure: each beat carries a time range and 1-3 observable actions; ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps; actions must be externally filmable behavior, never inner monologue.

## Realism constraints

`{{realism_rules}}`

Default realism rules (merged unless overridden by `realism_rules`): accurate physics; natural walking, hair, fabric, paper, strings, seawater, lighting and shadows; correct hands and facial expressions; no distortions, duplicated objects, disappearing props, wardrobe drift, or anatomy errors.

## Audio design

`{{audio_design}}`. Audio prohibitions: `{{audio_exclusions}}`.

## Ending and final feel

Ending directive: `{{ending_directive}}`. Final feel: `{{final_feel}}`.

## Global constraints (must remain at the end of the rendered prompt)

- The consistency lock holds for the entire video: identity, outfit, hairstyle, proportions, and accessories never drift.
- Setting exclusions, camera prohibitions, and audio prohibitions hold for the entire video; declaring them once in the sequence is not enough.
- No UI, subtitles, captions, watermarks, logos, or brand visibility.
- Every event must have a filmable cause; no objects or effects appearing from nowhere.
- The timeline covers the whole duration continuously; the ending follows `{{ending_directive}}` exactly.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): polished commercial look, gimbal or drone movement, slow motion, staged crowds, brands, landmarks, advertisements; distortions, duplicated objects, disappearing props, wardrobe changes, anatomy errors, extra fingers; music, narration, subtitles, captions, logos, watermarks; VFX glow, objects appearing from nowhere, causeless events.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. If `character_ref` is set, it comes from the consumer's registered asset library; no invented references.
3. Beat time ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps; every beat is observable action.
4. Consistency lock, realism constraints, audio and camera prohibitions survive intact in the rendered result.
5. The ending directive does not conflict with `duration_s` (e.g. a hard cut earlier than the total duration).

Honest fallback: when a required variable is missing or the sequence cannot cover the full duration, stop rendering and list the gaps; never invent asset references or skip the consistency lock.
