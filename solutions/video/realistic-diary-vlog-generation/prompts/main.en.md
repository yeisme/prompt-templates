{{provider_banner}}

# Realistic Diary Vlog Video Generation Prompt (on-camera dialogue day diary)

This template renders into a prompt delivered directly to a video generation model, for a "protagonist speaks directly to the camera" realistic diary vlog: on-camera dialogue, believable lip sync, and acoustic-space continuity. The consumer binds every variable before rendering; the rendered result is the final prompt body and must not be rewritten afterwards.

Family boundary: use `realistic-vlog-shot-generation` for ambience-only candid vlogs, `realistic-docu-vlog-generation` for off-camera voiceover narration, and this template when the subject speaks to the camera and lip sync matters.

## How to use

1. Fill all required inputs per the companion contract; provide `character_ref` when a character asset exists (`@uuid` and positional refs like `@image1` are both accepted).
2. Optional: set `provider_banner` to keep a delivery-platform banner line (e.g. `Made with Seedance 2.5`); leave empty to omit it.
3. Write `story_beats` per the "Diary timeline" structure; every line in `dialogue_script` must bind to a beat.
4. Review the rendered prompt against the self-check list before submitting it to a video model.

## Footage specification and style

`{{footage_style}}`. Total duration `{{duration_s}}` seconds, resolution `{{resolution}}`, aspect ratio `{{aspect_ratio}}`. Diary summary: `{{scenario_summary}}`.

## Subject and consistency lock

Subject: `{{subject_identity}}`. Wardrobe logic: `{{wardrobe_and_accessories}}`. Character asset reference: `{{character_ref}}`.

Consistency lock (non-negotiable for the whole video): `{{consistency_lock}}`

Wardrobe logic means a believable chain of outfit changes across the day (e.g. homewear → streetwear → rehearsal wear); every change must be motivated by a diary event, and the outfit never drifts within one location.

## Camera formats and texture

Camera declaration: `{{camera_formats}}`. Imperfections that must be preserved: `{{camera_imperfections}}`. Camera prohibitions: `{{camera_exclusions}}`.

## Diary timeline

`{{story_beats}}`

Beat structure: each beat carries a time range, a location with its acoustic space (e.g. bedroom / street / rehearsal room), a capture format (from the set declared in `camera_formats`), 1-3 observable actions, and a dialogue binding key (beats without dialogue are marked none); ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps; natural pauses and breathing room are allowed, but every event needs a filmable cause.

## On-camera dialogue

`{{dialogue_script}}`

Language: `{{dialogue_language}}`. Dialogue rules: every line lands on its bound beat; dialogue exists only as natural spoken voice on the audio track and never produces subtitles, titles, or any on-screen text; the text is preserved verbatim and must not be rewritten or translated; dialogue beats must visibly show the subject speaking with lip movement that credibly matches the line; dialogue is an occasional intimate address — do not assign speech to every beat.

## Audio design

Location sound and acoustic spaces: `{{ambience_design}}`. Audio prohibitions: `{{audio_exclusions}}`.

The acoustic space must change believably with each location (close quiet bedroom, open street reverb, reflective rehearsal room, etc.), and room tone stays present throughout.

## Realism constraints

`{{realism_rules}}`

Default realism rules (merged unless overridden by `realism_rules`): accurate anatomy and natural body mechanics, believable lip sync, natural blinking, breathing and expressions, real hair and fabric movement, correct lighting and shadows; no face drift, no duplicated subject, no plastic skin, no distorted hands, no floating props, no environment morphing.

## Ending and final feel

Ending directive: `{{ending_directive}}`. Final feel: `{{final_feel}}`.

## Global constraints (must remain at the end of the rendered prompt)

- The consistency lock holds for the entire video: face, hairstyle, body, and personality never drift; outfit changes follow only the wardrobe logic.
- No subtitles, titles, translations, logos, watermarks, UI elements, or any on-screen text; dialogue exists only as natural spoken audio.
- The camera is never visible, including mirrors and reflections; selfie beats must keep a believable handheld distance and angle.
- No commercial posing and no glamour lighting; light always comes from ordinary in-scene sources.
- Every event must have a filmable cause; no objects or effects appearing from nowhere.
- The timeline covers the whole duration continuously; the acoustic space switches with each location; the ending follows `{{ending_directive}}` exactly.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): commercial posing, glamour lighting, polished commercial look, gimbal/drone/impossible camera movement; face drift, duplicated subject, plastic skin, distorted hands, floating props, environment morphing, unmotivated wardrobe changes; lip sync mismatch, robotic announcer voice; subtitles, titles, on-screen text, logos, watermarks, UI elements; camera visible in frame, mirror crew reveal; objects appearing from nowhere, causeless events.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. If `character_ref` is set, it comes from the consumer's registered asset library; no invented references.
3. Beat time ranges cover 0-`{{duration_s}}`s continuously; every beat carries a location with acoustic space, and its capture format comes from the set declared in `camera_formats`.
4. Every dialogue line binds to an existing dialogue beat; the text matches `dialogue_script` verbatim; the share of dialogue beats stays "occasional address".
5. The wardrobe logic chain is complete: every outfit change is motivated by a diary event.
6. Consistency lock, realism constraints (including lip sync), audio and camera prohibitions survive intact; the no-subtitles ban appears in dialogue rules, global constraints, and negative prompts.

Honest fallback: when a required variable is missing, a dialogue line cannot bind to a beat, or the timeline cannot cover the full duration, stop rendering and list the gaps; never invent asset references, rewrite dialogue text, or skip the consistency lock.
