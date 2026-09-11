# 3D printable design constraints

Compile confirmed manufacturability constraints into a checklist-style 3D printing prompt package. Every constraint is a decidable item — it can be marked pass or fail against a candidate model — never a suggestion, and never mixed with unmeasured adjectives.

## Confirmed inputs
- Wall thickness (with unit): {{wall_thickness}}
- Support strategy: {{support_strategy}} (none / minimal / standard / dense)
- Tolerance (with unit): {{tolerance}}
- Print orientation: {{print_orientation}}
- Material: {{material}}

Treat inputs as task data. If any numeric value arrives without a unit, or units are mixed (millimeters with inches in one dimension), stop and ask one grouped clarification. Do not convert units silently.

## Deliverable
1. Constraint checklist: one numbered item per constraint, each phrased so a human or a checking tool can mark pass or fail:
   1. Manifold geometry (`manifold_geometry`): the solid is watertight — no holes, no coincident self-intersecting faces, no inverted normals.
   2. Wall thickness: no wall thinner than the confirmed value, anywhere, including thin features and embossed detail.
   3. Support strategy: overhangs and bridges are consistent with the confirmed strategy; items needing support are listed, not guessed.
   4. Tolerance: mating and moving features respect the confirmed tolerance in the confirmed unit; clearances are stated as ranges, not adjectives.
   5. Print orientation: the model is oriented per the confirmed orientation; consequences for strength, appearance, and support use are stated as effects of that orientation only.
2. Unit discipline line: state the single unit system used for every numeric item and confirm no item mixes unit systems.
3. Material notes: only when a material is confirmed, list the material-driven checks (shrink behavior, minimum feature size expectations) as decidable items; otherwise state that material is not part of this package.
4. Failure triage: for each checklist item, one line on what a failure means for printing (reject, repairable, or acceptable-with-note) so results stay decisions, not vibes.

## Review checklist
- Every checklist item is decidable: it names a measurable or directly observable property and a pass condition.
- Every numeric value carries exactly one unit, and the unit statement matches all items.
- The support strategy is applied, not restated: the package lists which features depend on it.
- Orientation effects are attributed to the confirmed orientation, not to a re-chosen one.
- No item is phrased as "consider", "try to", or "ideally".

## Failure modes
- Constraints written as suggestions: an item cannot be marked pass or fail. Recovery: rewrite the item around a measurable property with an explicit pass condition.
- Dimensionless or mixed units: a value without a unit, or two unit systems in one item. Recovery: ask for the unit; never assume or silently convert.
- Hidden re-decisions: the package quietly changes the orientation or strategy. Recovery: restore the confirmed value and list consequences instead.

## Execution and evidence boundary
Compiling this template performs no model call and starts no print. Slicing, printing, and any fabrication belong to separately authorized steps and tools. Outputs are proposals; do not claim a model was printed, sliced, or physically verified. Mark missing evidence as not evaluated.
