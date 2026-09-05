{{provider_banner}}

# Realistic Docu-Vlog Video Generation Prompt (VO day-in-the-life)

This template renders into a prompt delivered directly to a video generation model, for a "protagonist narrates one day of their life" documentary vlog: per-beat voiceover, a music arc, and mixed camera formats. The consumer binds every variable before rendering; the rendered result is the final prompt body and must not be rewritten afterwards.

## How to use

1. Fill all required inputs per the companion contract; provide `character_ref` when a character asset exists (`@uuid` and positional refs like `@image1` are both accepted).
2. Optional: set `provider_banner` to keep a delivery-platform banner line (e.g. `Made with Seedance 2.5`); leave empty to omit it.
3. Write `story_beats` per the "Story timeline" structure; every VO line in `voiceover_script` must bind to a beat.
4. Review the rendered prompt against the self-check list before submitting it to a video model.

## Footage specification and style

`{{footage_style}}`. Era texture: `{{era_aesthetic}}`. Total duration `{{duration_s}}` seconds, resolution `{{resolution}}`, aspect ratio `{{aspect_ratio}}`. Story summary: `{{scenario_summary}}`.

## Subject and consistency lock

Subject: `{{subject_identity}}`. Outfit and accessories: `{{wardrobe_and_accessories}}`. Character asset reference: `{{character_ref}}`.

Consistency lock (non-negotiable for the whole video): `{{consistency_lock}}`

## Camera formats and texture

Mixed camera declaration: `{{camera_formats}}`. Imperfections that must be preserved: `{{camera_imperfections}}`. Camera prohibitions: `{{camera_exclusions}}`.

## Story timeline

`{{story_beats}}`

Beat structure: each beat carries a time range, a capture format (from the set declared in `camera_formats`), 1-3 observable actions, and a VO binding key (beats without voiceover are marked none); ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps; montage beats list 3-5 quick-cut inserts.

## Voiceover script (VO)

`{{voiceover_script}}`

Tone requirement: `{{vo_tone}}`. VO rules: every VO line lands on its bound beat; the voiceover exists only as natural human voice on the audio track and never produces subtitles, titles, or any on-screen text; VO text must not be rewritten, and the tone stays a private self-narration.

## Audio design

Location ambience: `{{ambience_design}}`. Music arc: `{{music_arc}}`. Audio prohibitions: `{{audio_exclusions}}`.

## Realism constraints

`{{realism_rules}}`

Default realism rules (merged unless overridden by `realism_rules`): accurate anatomy and natural body mechanics, real physics, natural blinking, breathing and expressions, believable hair and fabric movement, realistic vehicle reflections and crowd behavior, physically plausible stage lighting; no CGI look, plastic skin, beauty filters, impossible camera movement, distorted hands, duplicated people, warped faces, or wardrobe drift.

## Ending and final feel

Ending directive: `{{ending_directive}}`. Final feel: `{{final_feel}}`.

## Global constraints (must remain at the end of the rendered prompt)

- The consistency lock holds for the entire video: identity, face, hairstyle, body, and wardrobe never drift.
- No subtitles, titles, translations, logos, watermarks, UI elements, or any on-screen text; dialogue and voiceover exist only as natural audio.
- The camera is never visible, including in mirrors or reflections.
- Every event must have a filmable cause; no objects or effects appearing from nowhere.
- The timeline covers the whole duration continuously; the music arc and the ending directive (`{{ending_directive}}`) stay consistent.
- Camera prohibitions and audio prohibitions hold for the entire video.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): polished commercial look, gimbal/drone/impossible camera movement, CGI look, plastic skin, beauty filters; distorted hands, duplicated people, warped faces, wardrobe drift, environment morphing; subtitles, titles, on-screen text, logos, watermarks, UI elements; objects appearing from nowhere, causeless events, camera visible in frame.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. If `character_ref` is set, it comes from the consumer's registered asset library; no invented references.
3. Beat time ranges cover 0-`{{duration_s}}`s continuously; every beat's capture format comes from the set declared in `camera_formats`.
4. Every VO line binds to an existing beat; VO text matches `voiceover_script` verbatim.
5. Consistency lock, realism constraints, audio and camera prohibitions survive intact.
6. The music arc's peak does not conflict with the ending directive; the no-subtitles ban appears in both global constraints and negative prompts.

Honest fallback: when a required variable is missing, a VO line cannot bind to a beat, or the timeline cannot cover the full duration, stop rendering and list the gaps; never invent asset references, rewrite VO text, or skip the consistency lock.
