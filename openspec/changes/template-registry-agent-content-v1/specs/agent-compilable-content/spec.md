## ADDED Requirements

### Requirement: Compatible successor templates
The repository SHALL provide bilingual strict input contracts for summary, meeting and evidence research successor templates without changing previously published bodies.

#### Scenario: Compile a successor
- **WHEN** Registry receives confirmed typed inputs for a successor
- **THEN** deterministic compilation succeeds and records the exact template digest

### Requirement: Deferred step output
The research-summary recipe SHALL keep the summary step pending until a real research output is imported.

#### Scenario: Missing research output
- **WHEN** only initial research inputs are confirmed
- **THEN** the summary step is needs_step_output and no intermediate output is invented
