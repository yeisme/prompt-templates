# AI Drama Scene Writing

Compiles one shootable scene draft: executable action, separated subtext, ordered information release, cost, and exit state. Absorbs the `screenplay-scene-writer` task role from the routing matrix.

- Compile ref: `promptrepo://official/writing/ai-drama-scene-writing@1.0.0?locale=en`
- Inputs: scene contract, canon snapshot, style constraints, candidate strategy, dialogue language
- Output: `SceneDraft` proposal; `draft_status=reviewable` only when every contract field is honored
- Consumers: Auctra scene candidates and A/B strategy trials, standalone agents
- Boundary: draft only; `selected` is not `accepted`
