# AI Drama Showrunner

Plans seasons and episodes with proof-slice batching, expansion gates, payoff windows, and suspense debt. Absorbs the retired `ai-drama-showrunner` skill.

- Compile ref: `promptrepo://official/writing/ai-drama-showrunner@1.0.0?locale=en`
- Inputs: format contract, story proposal projection, series context, task delta
- Output: `ShowrunnerPlan`; scopes over 5 episodes get a 3-episode proof slice plus a four-condition expansion gate
- Consumers: Auctra episode owners, standalone agents
- Boundary: user voice selection gates expansion; no unreviewed episode content
