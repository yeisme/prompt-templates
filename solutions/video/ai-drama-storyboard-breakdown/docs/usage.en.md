# Usage

This solution converts one Scaena-split and numbered episode into `storyboard.semantic_plan.v1`. It does not read arbitrary files directly and does not create a Scaena candidate.

Before use, you need:

- one exact episode;
- validated direction and profile;
- complete, untruncated source segments within owner limits;
- exact Prompt address plus contract, document, Schema, and fixture digests;
- compatible execution and data policy;
- independent approval for the current model call.

Recommended flow: provider-free inspect/validate → Scaena render snapshot → Scaena model run → Scaena deterministic compiler → findings/diff → human review → accept or reject.

See `preset-matrix.en.md` for the four profiles, their default pacing, quality gates, and visual asset handoffs. Pass storyboard `image_instruction` values to the visual asset owner, then combine them with subject, wardrobe, reference-role, and continuity templates from `video/ai-drama-character-assets` to create a reviewable Prompt Bundle.

This solution does not own provider choice, cost, credentials, retry policy, acceptance, export, or image generation.
