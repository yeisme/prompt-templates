{{provider_banner}}

# AI Drama Shot Video Generation Prompt (charge-up ultimate-skill shot)

This template renders into a shot-level prompt delivered directly to a video generation model. The consumer binds every variable and validates asset references before rendering; the rendered result is the final video-generation prompt body and must not be rewritten afterwards.

## How to use

1. Fill all required inputs per the companion contract. `character_ref` is a required asset reference; `weapon_ref`, `enemy_ref`, and `scene_ref` are required whenever the corresponding assets exist.
2. Write `shot_list` per the storyboard-slot structure in "Shot-by-shot slots"; actions per shot must not exceed `{{max_actions_per_second}}` per second.
3. Review the rendered prompt against the self-check list before submitting it to a video model.

## Global setup (quality and VFX rules)

`{{quality_profile}}`. Style: `{{style_keywords}}`. Total duration `{{duration_s}}` seconds, aspect ratio `{{aspect_ratio}}`, no UI. Color grading: `{{color_grading}}`. VFX mix: `{{effect_mix}}`. Safety protocol: `{{gore_protocol}}`.

## Character setup

`{{character_label}}`: strictly follow `{{character_ref}}`. Wardrobe anchors (anti-clipping): `{{wardrobe_anchors}}`. Weapon: `{{weapon_desc}}`, strictly follow `{{weapon_ref}}`.

Core behavior setup: `{{character_core}}`.

Behavior constraints are enforced in two layers and must not override each other:

- Charge-phase constraint: `{{charge_phase_rule}}`
- Release-and-finale constraint: `{{release_phase_rule}}`

## Ultimate skill setup

Ultimate skill [ `{{ultimate_skill_name}}` ]: `{{ultimate_skill_visual}}`.

## Enemy group

`{{enemy_desc}}` (asset reference: `{{enemy_ref}}`). Counterattack patterns: `{{enemy_counterattack}}`. Death reactions: `{{enemy_death_reaction}}`.

## Scene setup

`{{scene_desc}}` (asset reference: `{{scene_ref}}`). Rigid geometry anchors: `{{scene_anchors}}` — these anchors must stay recognizable for the whole video; VFX must never swallow them completely.

## Camera specification

`{{camera_spec}}`

Default specification (applies where `camera_spec` does not override): cut to a new camera position every 2-3 seconds with no hard cuts; transitions are limited to whip pans, foreground occlusion, VFX flash-overs, blind-spot cheats (0.1s), and wide crane moves. Handheld follow with high-frequency breathing shake, low inertia delay, fast shutter, and strong motion blur. Impact frames are graded: regular kills trigger level one, charge compression triggers level two, the ultimate release triggers level three.

## Shot-by-shot slots

`{{shot_list}}`

Storyboard structure (required per shot): shot number and time range (covering 0-`{{duration_s}}`s with no gaps or overlaps), actions 1-N (no more than `{{max_actions_per_second}}` actions per second), camera move, impact-frame level, and the invisible cut point. Charge-phase shots only show charging and enemy counterattacks; release-phase shots only show the release and the wipe-out; finale shots show aftermath and the freeze.

## Global constraints and anti-break rules (must remain at the end of the rendered prompt)

- 8k resolution, Masterpiece, highest quality. Strictly no more than `{{max_actions_per_second}}` actions per second.
- Constant motion throughout: absolutely no frozen frames, static camera, slow-motion stutter, or standing-still charging.
- Character behavior follows the two-layer constraints: during the charge phase obey `{{charge_phase_rule}}`; only in the release-and-finale phase may the actions declared in `{{release_phase_rule}}` occur (landing, sheathing, freeze-standing).
- One camera position every 2-3 seconds, joined seamlessly by whip pans, occlusion, and flash-overs; no hard cuts or fade-to-black transitions.
- The safety protocol `{{gore_protocol}}` holds for the whole video: all enemy hits and deaths are represented only by the particles and effects the protocol allows.
- Strict hand physics: gripping, swinging, and seal-forming must be precise; no extra fingers or deformities.
- Prevent the wardrobe anchors listed in `{{wardrobe_anchors}}` from clipping or disappearing during high-speed movement and spins.
- VFX must never cover the character's face; `{{scene_anchors}}` stay recognizable as rigid geometry anchors.
- The final second must complete the wipe-out: all enemies destroyed, a clean frame, and the character frozen per the finale constraint.

## Negative prompts

`{{negative_prompts}}`

Default negatives (merged unless overridden by `negative_prompts`): hard cuts, jarring transitions, fade-to-black transitions, empty shots, static camera, no motion at frame 0, standing-still charging; source-less floating VFX, VFX covering the face; blood, wound close-ups, dismemberment; enemies with no hit reactions; slow motion, stutter, frozen frames, lag, character leaving the frame; landing at the start, ending the ultimate early, timeline errors that wipe enemies early, a freeze with enemies left alive; UI, subtitles, watermarks; character deformation, twisted limbs, extra fingers, melted blurry figures; weapons inconsistent with `{{weapon_desc}}`.

## Post-render self-check

1. All variables are bound; no leftover placeholders remain.
2. Asset references (starting with `@`) all come from the consumer's registered asset library; none are invented.
3. Shot time ranges cover 0-`{{duration_s}}`s continuously with no gaps or overlaps; per-shot action counts stay within the limit.
4. Charge-phase shots contain no finale actions (landing, sheathing, freeze-standing), and enemies are not wiped out before the release phase.
5. The safety protocol, negative prompts, and global constraints sections survive intact in the rendered result.
6. Wardrobe anchors and geometry anchors are echoed in both global constraints and the storyboard, not mentioned only once.

Honest fallback: when a required variable is missing or an asset reference is unregistered, stop rendering and list the gaps; never invent asset references or skip the safety protocol.
