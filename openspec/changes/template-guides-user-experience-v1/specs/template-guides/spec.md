## ADDED Requirements

### Requirement: Exact guide access
The system SHALL expose solution guides bound to an exact template reference and role without requiring a compilable contract.

#### Scenario: Explicit read
- **WHEN** a client discovers a guide
- **THEN** metadata contains snapshot and digest and body requires explicit resource read or file export

#### Scenario: Changed guide
- **WHEN** the guide or snapshot changes before resource read
- **THEN** the old resource fails rather than silently returning different content

### Requirement: Complete tutorials
Every solution SHALL document inputs, examples, confirmation, delivery, recovery and rights for its registered roles.

#### Scenario: Local verification
- **WHEN** synthetic tutorial examples are checked
- **THEN** supported English Markdown roles compile and export without provider calls and owner-only roles remain explicit
