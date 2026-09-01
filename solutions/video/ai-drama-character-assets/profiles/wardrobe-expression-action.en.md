# Wardrobe, Expression, and Action Profiles

## Wardrobe sheet

Depends on an accepted body master. A base wardrobe must also be accepted before the turnaround.

- Separate inner layer, outer layer, sash/belt, shoes, jewelry, and detachable accessories.
- State material, color, structure, closure, coverage, and wear without substituting brand names for design facts.
- Keep identity, body proportions, and camera consistent across the sheet.
- Wardrobe references may influence structure, material, and coverage only; they must not change the face, hairline, base hairstyle, or body proportions.

## Expression sheet

### Role and dependency

The expression sheet is a face-level performance calibration asset. It depends only on the exact accepted face master. It does not depend on the body master, wardrobe canon, or turnaround, and it never replaces the face master as identity truth.

The base hairline and hairstyle silhouette are locked with the face master. A ceremonial updo, action hairstyle, or other replacement hairstyle requires a separate hairstyle/relock task before expression compilation continues.

### Production task

```text
subject_count = 1
depiction_count = 6
layout = expression_contact_sheet_3x2
output_intent = independent_cells_plus_contact_sheet
seed_policy = family_locked
```

`layout` controls review order only. Each provider call creates one adult subject and one expression, without a grid or text. Six artifacts use stable `view_key` values and semantic titles; Eikona then creates the deterministic 3×2 contact sheet.

A visible neckline is `presentation_only`: it may provide safe coverage and stable shoulder/neck contours, but it does not create a wardrobe version and must not flow into downstream wardrobe canon. `wardrobe_json` may be empty for this profile.

### Reference boundary

Identity sources may influence facial proportions, feature spacing, skin-tone range, permanent markers, hairline, and base hairstyle silhouette. They must not influence source expression, gaze, makeup, jewelry, wardrobe, background, dramatic grading, or undeclared lighting.

Camera and light come from the task capture lock. Identity similarity never authorizes the identity reference to control composition.

### Capture lock

All six cells lock front eye-level capture, bust-to-shoulder crop, head yaw/pitch/roll, gaze target unless explicitly varied, eye-line height, head scale, crop, focal-length impression, exposure, key-light direction, and background.

Only brow, eyelid, periocular moisture, mouth corner, lip opening, jaw, cheek tension, and breath impression may change. Do not use head tilt, shoulder movement, body lean, camera push, or lighting changes to simulate intensity.

### Intensity scale

| Intensity | Meaning |
|---:|---|
| 0 | neutral baseline; no emotional signal |
| 1 | micro; minimal muscle signal |
| 2 | subtle-readable; restrained but legible |
| 3 | clear-controlled; explicit and controlled |
| 4 | strong-controlled; strong while identity and anatomy remain stable |

Intensity is one integer. Ranges such as `2→3` and labels such as `medium-high` are invalid.

### Recommended six cells

| View key | Label / intensity | Observable delta | Must not escalate to |
|---|---|---|---|
| `view-expression-01-neutral` | `neutral / 0` | fully relaxed brow, eyes, lips, and jaw | any emotional signal |
| `view-expression-02-reserved-smile` | `reserved-smile / 2` | closed-lip small smile; slightly softer eyelids | teeth or laughter |
| `view-expression-03-grief-held` | `grief-held / 3` | inner brow lift, lower-lid tension, moist eye line, lower-lip tension | falling tears or lowered head |
| `view-expression-04-cold-anger` | `cold-anger / 3` | lowered brows, upper-lid tension, compressed lips, slight masseter tension | redness, bared teeth, or glaring |
| `view-expression-05-startled-fear` | `startled-fear / 2` | raised upper lids, slight inner-brow lift, parted lips, held breath | pupil requirements or head/shoulder recoil |
| `view-expression-06-resolve` | `resolve / 4` | stable lower lids, settled brows, compressed lips, stronger jaw tension | raised chin or changed head pitch |

### Seed, QC, and repair

`family_locked` supports comparable reruns; it is not an identity lock or a promise of pixel-level provider determinism. Identity is established through exact refs/digests, capture lock, per-cell QC, and human review.

Generate one baseline candidate per cell. A failed cell may receive at most two repair candidates. Change only the failed dimension: facial delta/intensity, identity preservation, capture lock, or `must_not_influence`/presentation constraints. If two or more cells drift in identity or capture, stop cell-level repair and inspect the face master, reference binding, and capture baseline.

### Training boundary

Six near-duplicate frontal cells are useful for performance calibration and identity stress testing, but they are not a LoRA-ready dataset. Training requires a separate profile, rights lineage, deduplication, angle/shot/light coverage, and a training-specific acceptance gate.

## Action sheet

Depends on the accepted body master, exact wardrobe version, and exact prop refs used by the action.

- Split complex action into anticipation, contact, and result.
- Lock grip hand, prop direction, center of gravity, screen direction, and wardrobe continuation.
- Each cell expresses one main phase; motion blur must not conceal anatomy.
- Full-body expression, balance, and physical reaction belong here; the expression sheet does not provide full-body performance coverage.

Readiness: exploratory.
