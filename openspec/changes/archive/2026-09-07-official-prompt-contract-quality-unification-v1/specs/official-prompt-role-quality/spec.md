## ADDED Requirements

### Requirement: Exact template roles declare their consumer capability

Each multi-owner structured Prompt role SHALL declare its exact required consumer capability through its document descriptor, while solution capabilities remain coarse discovery metadata.

#### Scenario: A consumer evaluates one film role

- **WHEN** a consumer resolves an exact film template role
- **THEN** the role descriptor SHALL identify one stable task capability
- **AND** the consumer SHALL NOT infer support from an unrelated role in the same solution

### Requirement: Provider delivery body excludes authoring and review instructions

A direct Provider integration SHALL consume a dedicated delivery role whose rendered body contains only Provider-facing content.

#### Scenario: Rendering a Provider delivery role

- **WHEN** the delivery role is rendered with a valid contract
- **THEN** the result SHALL exclude authoring instructions and human review checklist sections
- **AND** the companion validation policy SHALL remain available outside the Provider payload

### Requirement: Locale and contract documentation stays internally consistent

Usage documentation SHALL match the current contract input count and SHALL distinguish draft synchronized adaptations from human-reviewed locales.

#### Scenario: Reviewing the Vlog Provider compatibility update

- **WHEN** `provider_banner` is present in both locale contracts
- **THEN** usage documentation SHALL report 22 inputs
- **AND** bilingual step numbering SHALL be sequential
- **AND** the English locale SHALL not be described as reviewed before human equivalence review
