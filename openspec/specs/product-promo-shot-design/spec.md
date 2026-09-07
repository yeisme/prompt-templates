# product-promo-shot-design Specification

## Purpose
TBD - created by archiving change official-product-promo-shot-design-beta-v1. Update Purpose after archive.
## Requirements
### Requirement: Product facts and creative decisions remain distinct
The brief role SHALL identify source-grounded product facts, unknowns, confirmed decisions and creative proposals as distinct output fields.

#### Scenario: Unsupported product claim
- **WHEN** a requested selling point is not supported by an imported source
- **THEN** the claim appears in unknowns or unresolved decisions and does not appear as a product fact

### Requirement: Exact shot-library resolution
The shot-plan role SHALL resolve a shot card from a supplied index and pinned revision and SHALL preserve the card name, style key, document path, implementation path and preview status.

#### Scenario: Unknown card name
- **WHEN** a selected shot name is absent from the supplied library index
- **THEN** the plan keeps the mapping unresolved and does not invent an implementation

### Requirement: Dependent two-step recipe
The reusable workflow SHALL compile the brief first and SHALL keep shot planning in `needs_step_output` until an actual accepted brief is imported.

#### Scenario: Recipe compiles before brief output exists
- **WHEN** all confirmed inputs are present but no brief step output has been bound
- **THEN** the package exposes the ready brief prompt and a pending shot-plan template without claiming the second step is runnable

### Requirement: Domain execution remains outside compilation
The templates SHALL describe capture, generation, Remotion implementation, editing, review and delivery as downstream owner actions and SHALL make zero provider calls during compilation.

#### Scenario: video-shotcraft canary
- **WHEN** the output targets the pinned external video-shotcraft Skill
- **THEN** the handoff contains the exact upstream revision and required inputs without copying its implementation assets or granting execution authority

