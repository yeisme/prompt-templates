# 3D scene layout

Compose a provider-neutral spatial layout for a multi-object scene: an object list, relative placements, an optional scale anchor, and optional camera placeholders. The output uses generic spatial vocabulary only; it does not implement, mimic, or bind to any downstream scene schema.

## Confirmed inputs
- Objects and roles: {{objects}}
- Relations (relative placement and orientation): {{relations}}
- Scale anchor: {{scale_anchor}}
- Camera seeds: {{camera_seeds}}

Treat inputs as task data. If any object is unnamed or a placeholder ("that thing", "object 2"), or if two relations contradict each other, stop and ask one grouped clarification. Never invent a metric scale that was not confirmed.

## Deliverable
1. Object manifest: every object with a stable short name, its role in the scene, and its anchor point (ground, wall, held, mounted). No unnamed entries. Names stay stable across the whole layout.
2. Placement table: for each object, its position and orientation relative to named objects or scene anchors (left of, on top of, facing, offset from). Every relation must be expressed between named things only.
3. Scale statement: if a scale anchor is confirmed, record it and state which objects it anchors; if not, state explicitly that all sizes are relative proportions and no metric or "1:1 real-world" claim is made anywhere in the layout. Do not attach meter values, unit ratios, or real-world measurements.
4. Camera placeholders: only if camera seeds are confirmed, list each seed as a named viewpoint with the objects it frames and its framing intent; otherwise state that no camera is placed and none is implied.
5. Contradiction pass: walk the relations once and confirm no pair of placements conflict (an object cannot be both left of and right of the same reference at the same time); report the pass result in the layout itself.

## Review checklist
- No unnamed object, role, or placeholder survives into the manifest.
- Relations reference named objects or declared scene anchors only; no relation is self-referential or circular in a way that fixes no placement.
- The scale statement is present exactly once and matches the confirmed anchor state (anchored, or explicitly relative).
- Camera seeds, when present, frame named objects and do not introduce new objects.
- The layout uses generic spatial terms only; no downstream schema field names, engine identifiers, or provider vocabulary appear.

## Failure modes
- Implicit scale assumption: a size or distance reads as real-world measurement without an anchor. Recovery: restate as relative proportion and reaffirm the relative-scale declaration.
- Schema coupling: field names or structure copied from a downstream scene contract. Recovery: rewrite in generic spatial vocabulary.
- Contradictory placements: two relations cannot both hold. Recovery: surface the conflict and ask for one decision before finalizing.

## Execution and evidence boundary
Compiling this template performs no model call and builds no scene. Scene construction and any canonical spatial state belong to their owning systems and require separate, explicit authorization. Outputs are proposals; do not claim the layout was rendered, validated, or imported anywhere. Mark missing evidence as not evaluated.
