# Precision-Parameterized Candid Shot

This template produces a single precision-parameterized candid shot prompt. Unlike the random-matrix package, nothing is sampled here: every variable is bound exactly from a shot spec (JSON), and quantified parameters (cm, percentages, degrees) go straight into the body. The consumer binds all variables before rendering; the rendered result is the final prompt body without further rewriting.

## Slot convention

Optional clause variables (`perspective_clause`, `foreground_sentence`, `light_fill_clause`, `palette_sentence`, `background_sentence`, `fingerprints_sentence`, `tail_clause`) carry their own punctuation and leading spaces; bind them to an empty string when unused and the whole clause disappears.

{{orientation}} {{aspect}} candid lifestyle photo, {{subject_description}} {{pose}} with {{expression}}.
{{pronoun}} wears {{wardrobe}}.
{{camera_position_clause}}, {{lens}} lens{{perspective_clause}}, {{framing}}.{{foreground_sentence}}
{{light_key}}{{light_fill_clause}}.{{palette_sentence}}{{background_sentence}}{{fingerprints_sentence}}
{{quality}}, {{atmosphere}}, {{negatives}}{{tail_clause}}.

## Self-check

- Quantified parameters (cm, %, degrees) survive verbatim and are not rewritten as vague adjectives.
- Palette percentages sum to 100 in descending order (when `palette_sentence` is used).
- Foreground occlusion carries a percentage (when `foreground_sentence` is used).
- Negatives are complete; no studio-lighting vocabulary leaks in.
