# AI Drama Story Architecture

Turns a story idea into a verifiable dramatic structure: conflict chain and ten-field beat cards. Absorbs the retired `ai-drama-story-architecture` skill.

- Compile ref: `promptrepo://official/writing/ai-drama-story-architecture@1.0.0?locale=en`
- Inputs: format contract projection (ideally from `ai-drama-format-strategy`), creative brief, canon snapshot, task delta
- Output: `StoryProposal` with beat cards; beats missing `choice` or `cost` stay `draft`
- Consumers: Auctra story/episode owners, standalone agents
- Boundary: proposal only; never overwrites canonical screenplay
