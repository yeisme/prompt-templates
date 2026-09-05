## ADDED Requirements

### Requirement: Writing revision solution
The official repository SHALL expose a bilingual revision template with `revision`, `text`, and `writing` capabilities and a source-grounded input contract.

#### Scenario: Auctra discovers the template
- **WHEN** Auctra searches the official repository with its writing capability filter
- **THEN** `writing/revision-assistant@1.0.0` is compatible and can be inspected without provider calls

### Requirement: Digital-human persona solution
The official repository SHALL expose a bilingual persona system-prompt template that requires confirmed identity, audience, speaking, factual, and safety boundaries.

#### Scenario: Persona prompt export
- **WHEN** Template Registry compiles confirmed Persona inputs
- **THEN** the ready prompt can be explicitly exported to `prompts/system.md` without transferring Registry state or credentials

### Requirement: Eikona-compatible image solution
The official repository SHALL expose a new immutable bilingual cover template with `generation`, `image`, and `visual` capabilities while preserving the published v1 exact ref.

#### Scenario: Eikona resolves the compatible cover template
- **WHEN** Eikona resolves `image/xhs-product-cover-v2@2.0.0`
- **THEN** the solution passes its generic image capability filter without changing `image/xhs-product-cover@1.0.0`
