# Code quality template and Skill contract

## ADDED Requirements

### Requirement: Code quality review output is evidence bounded

The repository SHALL provide an English-compilable code quality review template with a stable structured output contract. Findings MUST carry severity, confidence, category, location, evidence references, impact, recommendation, verification, and status. Unknown facts MUST remain unknown.

#### Scenario: Review with a supported finding

- **WHEN** an Agent supplies a bounded change scope and evidence-backed file observation
- **THEN** the compiled output contains a stable finding ID, repository-relative location, evidence reference, and verification step
- **AND** the output does not contain source bodies, credentials, provider payloads, or hidden reasoning

#### Scenario: Review without enough evidence

- **WHEN** a possible issue cannot be tied to an evidence reference
- **THEN** the output marks the issue as `unknown` or omits it
- **AND** the output identifies a next diagnostic action instead of inventing a conclusion

### Requirement: Test gaps and refactor plans remain separate from execution

The repository SHALL provide test-gap and refactor-plan templates. Test-gap output MUST distinguish covered checks, missing evidence, and recommended test level. Refactor-plan output MUST require confirmation and MUST NOT claim that source edits were applied.

#### Scenario: Review findings produce a test gap

- **WHEN** a test-gap template receives a review packet and test inventory
- **THEN** it returns a prioritized gap with a supported verification command or an explicit unknown state

#### Scenario: Refactor plan requires confirmation

- **WHEN** a refactor-plan template receives review and test-gap packets
- **THEN** `requires_confirmation` is `true`
- **AND** every step has repository-relative paths, edit boundaries, verification, and rollback information
- **AND** no source patch or automatic edit command is returned

### Requirement: The audit recipe preserves step output bindings

The repository SHALL provide a `code-quality-audit-v1` recipe whose steps run review, test-gap, and refactor-plan in dependency order. Later steps MUST consume earlier outputs through `step_output` bindings.

#### Scenario: Audit recipe validates

- **WHEN** the Registry validates `recipes/code-quality-audit-v1.json`
- **THEN** the recipe is a valid acyclic DAG with `review` before `test-gap` and `refactor-plan`
- **AND** the bindings reference exact `locale=en` template refs
