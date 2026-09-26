# Precision-Parameterized Candid Shot

This template produces a single precision-parameterized candid shot prompt. Unlike the random-matrix package, nothing is sampled here: every variable is bound exactly from a shot spec (JSON), and quantified parameters (cm, percentages, degrees) go straight into the body. The consumer binds all variables before rendering; the rendered result is the final prompt body without further rewriting.

## Slot convention

Optional clause variables (`perspective_clause`, `sections_block`, `foreground_sentence`, `light_fill_clause`, `palette_sentence`, `background_sentence`, `fingerprints_sentence`, `tail_clause`) carry their own punctuation and leading spaces/newlines; bind them to an empty string when unused and the whole clause disappears. `genre` defaults to "candid lifestyle photo"; use a different genre phrase (e.g. editorial portrait) for non-candid shots.

Vertical 9:16 high-fashion magazine editorial photograph, a sweet, slightly mixed-heritage young adult East Asian woman with an elegant, light-mature air posed gracefully against a minimalist gray studio backdrop with a calm, confident, elegant expression with lively eyes.
She wears a black fitted high-neck short-sleeve top, a beige-apricot champagne-gold lace-embroidered short skirt, black semi-sheer tights, and black patent pointed-toe stiletto heels — French vintage socialite style in a black-and-gold palette with a premium banquet feel.
Hair and accessories: a low coiled updo, a black vintage veiled mini cocktail hat with a black rose ornament, and silver drop earrings.
Typography: elegant English typography laid out as part of the magazine composition; no logos, no watermarks.
Camera positioned at eye level, classic studio fashion framing, 85mm portrait lens, full-body editorial composition with the complete outfit visible, magazine-cover layout with strong visual impact.
Soft, even studio lighting of high-end fashion editorial quality, gentle modeling on the face and fabric textures. Main colors: black, champagne gold, apricot beige, silver, soft gray. A minimalist gray studio backdrop, clean and premium.
fashion magazine editorial photography, high-end studio portrait, real human skin texture, real lace embroidery texture, subtle film grain, high dynamic range, 4K, ultra detailed, a premium banquet mood with strong visual impact, no eerie expression, no stiff limbs, no deformed hands, no extra hands or limbs, no unbalanced proportions, no low quality or blur, no overexposure, no cheap look, no cluttered background, no cartoonish look, no exaggerated makeup, no watermarks, no logos, no text errors, no dull lifeless eyes, photorealistic.

## Self-check

- Quantified parameters (cm, %, degrees) survive verbatim and are not rewritten as vague adjectives.
- Palette percentages sum to 100 in descending order (when `palette_sentence` is used).
- Foreground occlusion carries a percentage (when `foreground_sentence` is used).
- Negatives are complete; no studio-lighting vocabulary leaks in.
