# Grounded Pose Clause Template

This template compiles one standardized English pose clause describing a grounded figure pose — seated, kneeling, lying or transitional — for use as the pose slot of any image-prompt style layer (documentary, editorial, illustration). The library of 25 reviewed poses lives in `assets/poses/*.json`; pre-rendered copy-paste clauses live in `examples/<id>/pose-clause.en.md`.

Directions are camera-relative: "frame-left" and "frame-right" describe what the viewer sees, never the subject's own left or right. Bind all variables from a pose spec before rendering; the rendered result is one copy-paste action clause without further rewriting.

{{pose_lead}} {{lower_limbs}} {{upper_limbs}} {{torso_head}} {{weight_silhouette}}

## Self-check

- All four body sections are present and in fixed order: lower limbs, upper limbs, torso and head, weight and silhouette.
- Directions are camera-relative (frame-left / frame-right); the subject's own left/right never appears.
- The clause reads as one breath of observation; no camera, lens, light, wardrobe or style vocabulary leaks in.
