# AI Drama Visual Asset Profile Matrix

## Directory order is not dependency order

```text
face-master
  → expression-sheet (face level)
  → body-master
  → accept base-wardrobe front master
  → turnaround side view
  → turnaround back view
  → local 1x3 review contact sheet
  → wardrobe-sheet (additional looks) ∥ hairstyle-sheet (only for multiple hairstyles)
  → action-sheet
  → prop-scene-sheet
  → shot-keyframe
```

`expression-sheet-v1` can start after face-master acceptance and does not depend on body or wardrobe canon. `turnaround-three-view-v1` keeps its stable profile ID, but production means three independent artifacts: accept the base-wardrobe front master first, then generate side and back views. The consumer builds the review contact sheet locally.

## Identity, hair, and wardrobe boundaries

- Hairline and base hairstyle silhouette belong to the face identity anchor.
- Replacement hairstyles require a separate hairstyle task and face-identity revalidation before acceptance.
- Expression tasks cannot change hair or turn a presentation-only neckline into wardrobe canon.
- Wardrobe tasks own structure, material, coverage, and accessories only.
- The face master remains identity truth; expression, wardrobe, action, and shot artifacts cannot replace it.

## Profiles

| Profile | Asset level | Main result | Required inputs | Key gate | Downstream |
|---|---|---|---|---|---|
| `face-master-v1` | face identity | one neutral front face master | subject + identity refs | adult, single subject, no wardrobe/background contamination | SubjectVersion / expression |
| `expression-sheet-v1` | face performance | six independent cells + review contact sheet | accepted face master + capture lock | identity/capture/range | performance refs |
| `body-master-v1` | body identity | one front full-body master | accepted face master + body facts | full body, stable anatomy, neutral presentation | wardrobe / action |
| `turnaround-three-view-v1` | body + base wardrobe | accepted front master + independent side/back + local contact sheet | accepted face/body/front wardrobe refs | one view per job, real back view, stable marker and shoes | production subject |
| `wardrobe-sheet-v1` | wardrobe | layered wardrobe sheet | body master + wardrobe facts | material/coverage | wardrobe versions |
| `action-sheet-v1` | full-body performance | action phases | body + wardrobe + prop refs | grip, balance, direction | shot assets |
| `prop-scene-sheet-v1` | prop/scene | reusable prop or scene anchors | exact domain refs | structure and spatial facts | keyframes |
| `shot-keyframe-v1` | shot | one generatable keyframe | accepted shot intent + exact refs | no new story facts | Eikona candidates |
| `continuity-repair-v1` | bounded repair | repaired candidate | typed finding + exact source | failed dimension only | renewed review |
