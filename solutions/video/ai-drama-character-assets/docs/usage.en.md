# Usage

This solution compiles validated character, wardrobe, task, reference, and continuity data into `character_asset.prompt_bundle.v1`. It is provider-free and does not own Scaena SubjectVersion, Eikona runs/artifacts, human acceptance, or production state.

Before use, provide an exact subject version, accepted input refs required by the selected profile, a typed task, reference roles with status/version/digest, continuity constraints, an original dimensioned StyleLens, an exact Prompt address/contract/document/schema/compiler snapshot, and an independent execution approval for any later provider call.

Recommended flow:

```text
owner validation
  → provider-free Promptrepo inspect/validate/render
  → Eikona validate/plan
  → capability, permission, and cost gate
  → candidate generation
  → QC and human review
  → Scaena capture/freeze when authorized
```

Production dependency order is defined in `preset-matrix.en.md`, not by directory order. Expression production always uses six independent cells and a deterministic Eikona 3×2 contact sheet; a one-shot grid is preview-only. The full YAML and modular YAML authoring examples resolve to the same canonical task digest before Prompt compilation.

Character masters follow a separate staged gate: one neutral front face master, one front full-body master from the accepted face, one accepted base-wardrobe front master, then independently generated side and back views. Every Provider job produces one view and one candidate image. Eikona assembles the 1×3 review contact sheet locally; the contact sheet never replaces per-view acceptance or repair.

The repository `main` Prompt is a compiler instruction that returns `character_asset.prompt_bundle.v1`. It is not an image-generation prompt and must never be submitted directly to an image Provider.

Do not use these templates to imitate real actors or living creators, bypass rights/permission/cost gates, store credentials or provider payloads, accept assets automatically, or claim that expression cells are a LoRA-ready dataset.
