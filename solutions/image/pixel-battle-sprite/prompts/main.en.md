# Pixel Battle Sprite Sheet (4x4, transparent RGBA)

Convert a character into a high-quality chibi pixel-art battle sprite and generate a 4x4 transparent-background PNG sprite sheet. The consumer binds the character (reference image and/or description) and optional combat style before rendering; the rendered result is the final prompt body without further rewriting. Reference images are attached by the consumer at generation time, not embedded in this template.

## Core goal

Output exactly one true-transparent RGBA PNG sprite sheet of {{character}}:

- Exactly 4 columns x 4 rows, 16 sequential animation frames.
- Frame order: left to right, then top to bottom.
- All cells exactly the same size; fixed camera; consistent character scale; stable ground baseline; consistent registration point / anchor.
- Exactly one complete character per cell; character, weapon, and effects never exceed the cell; generous transparent margins on all sides.
- No text, numbers, numbering, grid lines, watermarks, borders, or background scenery.

## Character fidelity

Strictly follow the reference image ({{reference_binding}}) and convert it into a recognizable chibi pixel-art sprite, preserving exactly: hairstyle and hair color, major facial features, outfit structure, main color relationships, weapon or gear, body proportions, and signature ornaments. Across all 16 frames keep identical: character identity, head-to-body ratio, hairstyle structure, outfit structure, weapon size and shape, primary/secondary color relationships, and pixel scale. No face swaps, outfit swaps, weapon morphing, color drift, or proportion changes between frames.

## Combat action

{{combat_style}}

Build one complete loopable combat move and distribute it naturally across the 16 frames: ready stance → anticipation → wind-up → startup → strike → impact peak → follow-through → effect fade → recovery → back to ready stance. Every frame must show real frame-by-frame animation change: body pose, weight shift, foot support, torso twist, arm drive, leg action, weapon trajectory, cloth/hair/cape inertia, and effect appearance/build-up/fade. Never fake animation by only translating, rotating, scaling, or duplicating a static figure. Frame 16 must flow naturally back into frame 1 for an infinite loop.

Recommended allocation: frames 1-3 ready stance and slight anticipation; 4-5 clear wind-up and startup; 6-8 high-speed strike; 9 impact peak with the strongest action and effect; 10-11 follow-through and effect fade; 12-15 recovery; 16 nearly identical to frame 1 for a smooth loop.

## Pixel-art style

High-quality 16-bit game style pixel art: sharp pixel edges, no blurry interpolation, clear silhouettes, readable action silhouettes, a restrained unified palette, clear value steps, one consistent pixel scale for character, weapon, clothing, and effects, professional game-sprite finish. Avoid modern high-resolution illustration texture, soft brushes, heavy semi-transparent anti-aliasing, blurry edges, and non-pixelated effects.

## Transparency

The background must be true transparent RGBA: pure transparent alpha, no background color, no checkerboard, no black/white/solid backing, no low-alpha colored residue, no semi-transparent dirty edges, no noise. Areas outside the character stay cleanly transparent; character, weapon, and effect edges stay crisply pixel-clipped. Glow effects stay contained, never polluting large transparent areas or leaving low-alpha color residue.

## Pre-generation checklist

1. Exactly 16 frames; strictly 4x4; ordered left-to-right, top-to-bottom; all cells identical in size.
2. One complete character per cell; character and weapon never cropped; stable character size; stable ground baseline; consistent registration point.
3. Consistent identity, outfit, and weapon across frames; real frame-by-frame motion; clear attack rhythm; frame 16 loops back to frame 1.
4. True transparent RGBA; no text, grid lines, watermarks, backgrounds, or dirty pixels in transparent areas.

Generate only this single 4x4 transparent PNG sprite sheet.
