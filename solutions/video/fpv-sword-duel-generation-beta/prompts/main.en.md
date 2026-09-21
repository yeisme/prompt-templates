{{provider_banner}}

# Cinematic FPV Sword-Duel Video Generation Prompt (dual-palette blade VFX)

This template renders into a prompt delivered directly to a video generation model, for a two-person cinematic sword duel: first-frame composition lock, dual identity lock, two instantly distinguishable blade-VFX palettes bound to motion, FPV-orbit camera language, readable offense/defense, and a suppression-without-defeat arc. The consumer binds every variable before rendering; the rendered result is the final prompt body and must not be rewritten afterwards.

Family boundary: VFX-free physics-first close combat uses `realistic-fight-scene-generation`. Charge-up ultimate-skill wipe-out shots use `ai-drama-shot-video-generation`. This template covers FPV-orbit dual-swordsman duels whose visual peak is blade-path VFX plus clash destruction, not magic orbs or screen-clearing lasers.

## How to use

1. Fill all required inputs per the companion contract. `first_frame_ref` is the required t=0 composition and visual baseline (`@uuid` and positional refs like `@image1` accepted).
2. Optional: set `provider_banner` to keep a delivery-platform banner line; leave empty to omit it.
3. Write `fight_beats` per the "Duel timeline" structure, covering 0-`{{duration_s}}`s continuously. Beat 0 must inherit the first-frame composition for `{{first_frame_hold_s}}` seconds.
4. Review the rendered prompt against the self-check list before submitting it to a video model.

## Footage specification and style

`{{footage_style}}`. Quality profile: `{{quality_profile}}`. Total duration `{{duration_s}}` seconds, resolution `{{resolution}}`, aspect ratio `{{aspect_ratio}}`, frame rate `{{frame_rate}}`. Scenario summary: `{{scenario_summary}}`. Style reference: `{{style_reference}}` — inherit only the temperament, close-range pressure, and lens language; never copy the referenced work's characters, locations, or specific shots.

Fixed look: photoreal live-action cinematography with next-gen lighting, PBR materials, and fine cloth, hair, dust, stone, and metal-spark detail. The cut should feel like a high-end action demo: fast, but the offense/defense logic stays readable at every moment.

## First-frame lock

At t=0, strictly inherit `{{first_frame_ref}}` as the opening composition and the visual baseline for both fighters. Hold this exact framing for `{{first_frame_hold_s}}` seconds, then the FPV immediately orbits from the side at low altitude. Fighter A starts on the left of the first frame; Fighter B starts on the right. Do not restage, swap sides, change wardrobe, or invent a third combatant at the open.

## Dual characters and consistency lock

Fighter A (left, aggressor): `{{fighter_a_identity}}`

Fighter A VFX palette: `{{fighter_a_vfx}}`

Fighter B (right, pressed but unbeaten): `{{fighter_b_identity}}`

Fighter B VFX palette: `{{fighter_b_vfx}}`

Fighting-style contrast: `{{character_dynamics}}`

Consistency lock (non-negotiable for the whole video): `{{dual_consistency_lock}}`

Fixed rules: the two never swap identities; no face drift, age change, hairstyle change, body or height-proportion change, wardrobe-color change, or shoe/accessory change; no third combatant may appear. The two VFX palettes must stay instantly distinguishable in every clash: A's system stays darker, wilder, and more invasive; B's system stays colder, cleaner, and sharper. Blade VFX is ink-wind, vacuum cuts, and torn-air edges — never magic orbs, never laser cannons, never rainbow glow.

## Scene and spatial continuity

`{{scene_desc}}`

Layout and axis of action: `{{scene_layout}}`

Lighting and materials: `{{lighting_palette}}`

Fixed rules: the scene stays one ruined street / courtyard for the entire duration — no location change. Spatial layout stays identical across all shots; landmarks never teleport. Unless an FPV wrap-around explicitly shows a position swap, both fighters keep a clear axis of action. The camera may thread between them and orbit the clash point, but both stances and who is attacking / who is defending must remain readable.

## Action principles

`{{action_principles}}`

Fixed combat rules: every important attack shows origin, travel path, contact point, and result; a block must genuinely redirect or absorb the cut; footwork, hip rotation, and blade path stay physically connected. Short wall-runs, aerial crosses, and low-altitude bursts are allowed when they are readable and land with weight. No air-slicing with no contact, no limbs passing through bodies, no teleporting, no standing-pose duels, no long front-facing hero holds.

Structural arc: `{{fight_arc}}`

Fixed arc rule: Fighter A remains the aggressor and keeps heavy pressure. Fighter B is elite and stylish, but in this clip is forced onto defense, spatially compressed, and rhythm-locked — never defeated, never collapsing in disgrace, never losing composure. The ending stays unresolved: A holds the advantage, B survives the last wave.

Environment destruction: `{{environment_destruction}}`

Fixed destruction rule: destruction has mass and force. Tiles, pillars, beams, banners, dust, and stone react to real clashes and blade-wind, not to decorative sparkle. Debris follows impact direction.

## Blade VFX binding

`{{vfx_binding_rules}}`

Clash tear: `{{clash_vfx}}`

Fixed VFX rules: every important cut carries a high-end blade-aura, and that aura is bound to blade path, body rotation, footwork, clash shock, and environment breakup. VFX never explodes unmotivated. On blade contact, black and cold-white systems tear against each other with sparks, transparent shock rings, and dust. VFX never covers faces at the moment of readable contact, and never becomes a giant energy beam or magic sphere.

## Duel timeline

`{{fight_beats}}`

Beat structure: each beat carries a time range, an FPV camera move (from the set declared in "Camera language"), offense/defense actions with origin/path/contact/result, bound VFX for that cut, environment reaction, and the momentum/position/orientation/pressure state carried into the next beat; ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps. Beat 0 inherits the first-frame composition for `{{first_frame_hold_s}}` seconds before the first orbit.

## Camera language

FPV orbit language: `{{camera_language}}`

Camera motion: `{{camera_motion_rules}}`

Fixed camera rules: FPV-style orbit runs through the whole clip — close high-speed wrap, low orbit, rear-side cut, ground skim, threading between the fighters, and high-speed spiral around the clash point. The camera is fast but never chaotic: it always keeps both stances and the attack/defense logic readable. Prefer side, rear-oblique, low, ground-skim, blade-wipe, and between-fighters paths over constant front-face close-ups. Do not linger on faces from the front. Do not fly away from the duel. Impact shake is extremely short and aligned with force. Moderate motion blur is allowed; faces, hands, blades, and contact points stay sharp at key moments. No game UI, no speed lines as overlay graphics, no bullet time, no long slow motion, no fisheye as a default look.

## Audio design

`{{audio_design}}`

Fixed rules: location sound stays strictly synchronized with on-screen events — steel, cloth, footwork, stone, dust, banners, and breath. Music, if any, is a restrained low-frequency pulse and must never cover blade contact. No dialogue unless `audio_design` explicitly declares it.

## Ending and final feel

Ending directive: `{{ending_directive}}`. Final feel: `{{final_feel}}`.

## Global constraints (must remain at the end of the rendered prompt)

- The first-frame lock holds at t=0: composition, wardrobe, faces, and left/right staging inherit `{{first_frame_ref}}` for `{{first_frame_hold_s}}` seconds.
- The dual-character consistency lock holds for the entire video: no identity swap, no face drift, no wardrobe or body change, no third combatant.
- The scene never changes; layout and lighting stay consistent; destruction follows `{{environment_destruction}}` and has mass.
- Fighter A keeps pressure; Fighter B is suppressed but unbeaten and composed; the ending does not declare a knockout.
- Dual VFX palettes stay instantly distinguishable and bound to blade path, body, clash, and debris — no magic orbs, no laser cannons, no rainbow xianxia glow.
- Every attack and block keeps origin/path/contact/result readable; FPV orbit never loses the axis of action.
- Camera prefers side / rear-oblique / low / ground-skim / blade-wipe / between-fighters; no constant front-face portraiture; no chaotic flying.
- No health bars, crosshairs, button prompts, graphic speed lines, freeze frames, bullet time, long slow motion, or any text UI.
- No blood, wound close-ups, or dismemberment.
- The timeline covers the whole duration continuously; the ending follows `{{ending_directive}}` exactly.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): sluggish motion, standing-pose duels, long front-facing portrait holds, cheap light waves, rainbow VFX, unmotivated flying, chaotic camera, stutter, unreadable choreography, instant knockout, blood, dismemberment, plastic CG, anime faces, toy-game look, magic orbs, laser cannons, characters turning their backs so the action is lost, sudden location change, identity swap, face drift, extra people, extra limbs, bodies passing through each other, teleporting, UI, subtitles, watermarks, fisheye as default, long slow motion, bullet time, freeze frame.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. `first_frame_ref` comes from the registered asset library; no invented reference.
3. Beat time ranges cover 0-`{{duration_s}}`s continuously; beat 0 holds the first-frame composition for `{{first_frame_hold_s}}` seconds; every beat carries origin/path/contact/result, bound VFX, and a momentum handoff.
4. Every beat's camera move comes from the declared FPV set; both stances stay readable; no constant front-face coverage.
5. A's VFX and B's VFX remain instantly distinguishable; VFX is bound to blade path and clash, not floating as orbs or beams.
6. The arc shows A pressing and B surviving under pressure; B is never knocked out and never loses composure.
7. Consistency lock, same-scene rule, destruction mass, no-UI ban, and no-gore rule all appear in global constraints and negative prompts.

Honest fallback: when a required variable is missing, the first-frame reference is unregistered, or the timeline cannot cover the full duration, stop rendering and list the gaps; never invent asset references or skip the first-frame lock, dual VFX distinguishability, or the unbeaten-suppression ending.
