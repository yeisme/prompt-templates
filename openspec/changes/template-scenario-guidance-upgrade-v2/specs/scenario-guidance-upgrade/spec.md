## ADDED Requirements

### Requirement: Data-only tutorial scenarios
The system SHALL author exact-bound positive and negative tutorial cases without executing documentation or case-supplied programs.

#### Scenario: Invalid input
- **WHEN** a negative case is validated
- **THEN** its declared rejection must match input contract or declared tutorial data-shape checks

### Requirement: Section reads
The system SHALL preserve full-guide behavior and expose explicit role sections with full and content digests.

#### Scenario: Stale section
- **WHEN** the guide changes after discovery
- **THEN** the old section resource is rejected

### Requirement: Protected skill upgrade
The system SHALL require a matching plan and preserve user edits during upgrade and recovery.

#### Scenario: Interrupted promotion
- **WHEN** promotion stops between runtimes
- **THEN** the original transaction can restore prior files only when affected paths still match recorded states

### Requirement: Evidence boundaries
The system SHALL record engineering, authored scenario and human review results separately.

#### Scenario: Local compile
- **WHEN** a fixed local scenario compiles with a configured deny backend
- **THEN** observed backend requests are recorded independently of real Provider acceptance
