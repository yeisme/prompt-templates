# AI Drama Critic Review

Compares two or more candidates within one comparison class with evidence-anchored findings and bounded single-variable repairs. Absorbs the retired `ai-drama-critic-panel` skill.

- Compile ref: `promptrepo://official/writing/ai-drama-critic-review@1.0.0?locale=en`
- Inputs: candidates, assessment goal, rubric (empty object for qualitative-only)
- Output: `CriticReviewFindings`; `assessment_not_comparable` on class mismatch; no composite score without a frozen rubric
- Consumers: Auctra review owners, standalone agents
- Boundary: no author-source inference, no medium/platform labels, no acceptance authority
