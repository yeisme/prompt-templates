# Failure Modes

| Condition | Stable handling |
|---|---|
| Adult status is unclear | `ADULT_SUBJECT_REQUIRED`; stop generation |
| Identity sources conflict | `IDENTITY_SOURCE_CONFLICT`; ask the owner to select |
| Fixed task lacks seed policy | `FIXED_SEED_REQUIRED` |
| Typed marker conflicts with a mirrored reference | `MARKER_MIRROR_CONFLICT` |
| Translucent outer layer lacks opaque coverage | `MATERIAL_COVERAGE_INVALID` |
| Back view contains front-facing anatomy or garment structure | `BACK_VIEW_CONFLICT` |
| Shoe or key accessory drifts | `WARDROBE_CONTINUITY_DRIFT`; bounded repair |
| DRAFT/stale reference is used | `REFERENCE_NOT_PRODUCTION_READY` |
| Production task requests replace override | `PRODUCTION_REPLACE_OVERRIDE_FORBIDDEN` |
| Unknown field or provider parameter enters the bundle | `PROMPT_BUNDLE_FORBIDDEN_FIELD` |
| Repository compiler meta-prompt is submitted to an image model | `CHARACTER_ASSET_META_PROMPT_FORBIDDEN`; consume a validated single-view bundle job |
| Production requests one provider-generated turnaround grid | `CHARACTER_ASSET_PROVIDER_GRID_FORBIDDEN`; create independent jobs and a local contact sheet |
| Body master lacks an accepted face master | `CHARACTER_ASSET_UPSTREAM_NOT_ACCEPTED`; complete face review first |
| Side/back view lacks an accepted base-wardrobe front master | `CHARACTER_ASSET_UPSTREAM_NOT_ACCEPTED`; accept the front master first |
| Legacy composition still describes equal panels | `LEGACY_MULTI_PANEL_LAYOUT_NORMALIZED`; normalize to single-view production composition |
| Expression task lacks accepted face master | `FACE_MASTER_REQUIRED` |
| Production requests one generated six-cell grid | `EXPRESSION_SET_INVALID` |
| Expression labels are missing/duplicated or depiction count mismatches | `EXPRESSION_SET_INVALID` |
| Intensity is a range, text label, or outside 0..4 | `EXPRESSION_INTENSITY_INVALID` |
| Expression changes head pose, shoulders, crop, or gaze lock | `EXPRESSION_CAPTURE_CONFLICT` |
| Expression task also changes hairstyle | `HAIRSTYLE_RELOCK_REQUIRED` |
| A cell changes face, marker, hairline, or base hair | `EXPRESSION_IDENTITY_DRIFT` |
| Distinct labels produce nearly identical expressions | `EXPRESSION_RANGE_COLLAPSE` |
| Expression exceeds its level or adds tears, shouting, or body reaction | `EXPRESSION_RANGE_OVERSHOOT` |

Two or more identity/capture drifts are a batch baseline blocker. A LoRA-ready claim is rejected and routed to a separate dataset profile and rights/coverage gate. Permission, cost, digest, owner revision, and acceptance blockers cannot be bypassed by rewriting the Prompt.
