{{provider_banner}}

# Realistic Close-Combat Video Generation Prompt (dual-character ACT follow)

This template renders into a prompt delivered directly to a video generation model, for a two-person realistic close-combat scene: dual reference identity lock, auditable fight physics, axis-of-action and spatial continuity, and ACT-style third-person follow camera. The consumer binds every variable before rendering; the rendered result is the final prompt body and must not be rewritten afterwards.

Family boundary: VFX/ultimate-skill shots use `ai-drama-shot-video-generation`; the three realistic vlog flows have their own templates. This template covers VFX-free, physics-first, two-person fight scenes.

## How to use

1. Fill all required inputs per the companion contract. `protagonist_ref` and `antagonist_ref` are both required reference images (`@uuid` and positional refs like `@image1`/`@image2` accepted) and must not point to the same asset.
2. Optional: set `provider_banner` to keep a delivery-platform banner line; leave empty to omit it.
3. Write `fight_beats` per the "Fight timeline" structure, covering 0-`{{duration_s}}`s continuously.
4. Review the rendered prompt against the self-check list before submitting it to a video model.

## Footage specification and style

`{{footage_style}}`. Total duration `{{duration_s}}` seconds, resolution `{{resolution}}`, aspect ratio `{{aspect_ratio}}`, frame rate `{{frame_rate}}`. Scenario summary: `{{scenario_summary}}`. Style reference: `{{style_reference}}` — inherit only the temperament and lens language; never copy the referenced work's characters, locations, or specific shots.

## Dual characters and consistency lock

Protagonist: `{{protagonist_identity}}`, strictly following `{{protagonist_ref}}`. Antagonist: `{{antagonist_identity}}`, strictly following `{{antagonist_ref}}`.

Fighting-style contrast: `{{character_dynamics}}`.

Consistency lock (non-negotiable for the whole video): `{{dual_consistency_lock}}`

Fixed rules: the two never swap identities; no face drift, age change, hairstyle change, body or height-proportion change, wardrobe-color change, or shoe/accessory change; no third combatant may appear.

## Scene and spatial continuity

`{{scene_desc}}`

Layout and axis of action: `{{scene_layout}}`

Lighting and materials: `{{lighting_palette}}`

Fixed rules: the scene's spatial layout stays identical across all shots — doors, pillars, fixtures, and railings never move between cuts; unless a wrap-around shot explicitly shows a position swap, both fighters keep a clear axis of action and the camera never crosses the line without cause.

## Action principles

`{{action_principles}}`

Fixed physics rules: every attack must show its origin, travel path, contact point, and result; a block must genuinely redirect the attack; the receiver's head, shoulders, torso, footwork, and center of gravity react along the force direction; no air punches, no limbs passing through bodies, no unprovoked staggering, no gratuitous spinning, no chained flips, no levitation or exaggerated flight; actions may be fast, but key contact points stay clear — never hide movement behind chaotic blur.

Structural arc: `{{fight_arc}}`

Environment participation: `{{environment_interaction}}`

Fixed rules: both sides must land meaningful offense and defense — the protagonist may not dominate unharmed, and the antagonist may not wait like a sandbag; the protagonist's setback and recovery must come from judgment, center-of-gravity control, or environment use, never from nowhere.

## Fight timeline

`{{fight_beats}}`

Beat structure: each beat carries a time range, a camera position (from the set declared in "Camera rules"), offense/defense actions with origin/path/contact/result, an invisible cut point (body occlusion, pillar wipe, whip pan, impact shake, action match), and the momentum/position/orientation/injury state carried into the next beat; ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps.

## Camera rules

Follow positions: `{{camera_follow_spec}}`

Invisible cuts and continuity: `{{cut_rules}}`

Camera motion: `{{camera_motion_rules}}`

Fixed rules: the camera moves fast but with real weight — no floating, teleporting, frantic spinning, or constant irregular shake; impact shake is extremely short, low-amplitude, and aligned with the force direction; moderate motion blur is allowed, but faces, hands, feet, and contact points stay sharp at key moments; the ACT feel comes from protagonist-centered framing, third-person follow, spatial progression, and timely action feedback — never from game UI.

## Realism constraints

`{{realism_rules}}`

Default realism rules (merged unless overridden by `realism_rules`): hyper-real skin and muscle tension, fabric folds, wet hair, sweat and rain reflections; real metal, concrete, glass, and wet-floor materials; high contrast with retained shadow detail and unclipped highlights; no wax-figure skin, no plastic CG look, no noise grain, no sharpening halos, no compression blocks.

## Audio design

`{{audio_design}}`

Fixed rules: location sound stays strictly synchronized with on-screen events; music is limited to an extremely restrained low-frequency pulse and must never cover fight sound effects; no dialogue unless `audio_design` explicitly declares it.

## Ending and final feel

Ending directive: `{{ending_directive}}`. Final feel: `{{final_feel}}`.

## Global constraints (must remain at the end of the rendered prompt)

- The dual-character consistency lock holds for the entire video: no identity swap, no face drift, no wardrobe or body change, no third combatant.
- Every cut continues the previous shot's momentum, positions, body orientation, injuries, and attack direction; no teleporting, no position-swap errors, no sudden resets to standing, no unjustified line-crossing.
- Scene layout and lighting stay consistent for the whole video; environment objects join the fight only within the damage limits of `{{environment_interaction}}`.
- Every attack and block follows the fixed physics rules; both sides land meaningful offense and defense, and the protagonist goes through the arc's setback and recovery.
- No health bars, crosshairs, button prompts, speed lines, freeze frames, bullet time, long slow motion, fisheye, or any text UI.
- The timeline covers the whole duration continuously; the ending follows `{{ending_directive}}` exactly.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): identity swap, face drift, wardrobe change, body-proportion mutation, extra people, duplicated people, extra limbs, hyper-extended joints, bodies passing through each other, characters sticking together; air hits, inertia-less motion, a passive waiting antagonist, unexplained sliding, teleporting, levitation, wire-fu, energy blasts, exaggerated shockwaves, wall explosions; an unharmed dominant protagonist, a punch-bag antagonist; meaningless empty shots, hero entrance, long staring, repeated moves, abrupt cut to black; fisheye, long slow motion, bullet time, freeze frame, speed lines, health bars, crosshairs, button prompts, text UI; wax skin, plastic CG look, noise, sharpening halos, compression blocks.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. Both reference images come from the registered asset library and differ from each other; no invented references.
3. Beat time ranges cover 0-`{{duration_s}}`s continuously; every beat carries origin/path/contact/result and a momentum handoff into the next beat.
4. Every beat's camera position comes from the declared set; every cut uses the invisible-cut whitelist.
5. Each arc phase (seize / counter / pursuit / setback / escape / regain / finish) is identifiable in the beats.
6. Consistency lock, spatial continuity, physics rules, and the no-UI ban all appear in global constraints and negative prompts.

Honest fallback: when a required variable is missing, a reference image is unregistered, both refs point to the same asset, or the timeline cannot cover the full duration, stop rendering and list the gaps; never invent asset references or skip the consistency lock and physics rules.
