## ADDED Requirements

### Requirement: Integration brief classification
The template SHALL classify requested capabilities as template, Skill, recipe, or domain execution without granting execution authority.

#### Scenario: Multimodal production request
- **WHEN** confirmed inputs contain image generation, shot animation, editing and delivery
- **THEN** the output separates semantic templates, host Skills, recipe dependencies and domain-owned execution

### Requirement: Dependency-aware questions
The template SHALL report only unresolved decisions and SHALL return no more than three next questions ordered by dependency.

#### Scenario: Missing downstream target
- **WHEN** the final artifact is known but the execution owner and acceptance gate are unknown
- **THEN** those decisions appear before detailed provider settings

### Requirement: Integration lifecycle
The output SHALL define tags, capabilities, persistence, invalidation, provider-free compilation, Skill installation and exact-ref/digest handoff.

#### Scenario: Reusable recipe
- **WHEN** two or more template steps depend on prior outputs
- **THEN** the brief defines an acyclic recipe and marks actual step outputs as pending domain execution
