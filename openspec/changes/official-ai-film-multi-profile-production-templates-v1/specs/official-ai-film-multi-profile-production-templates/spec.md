## ADDED Requirements

### Requirement: Official film production content SHALL use one solution with four profiles

The official package SHALL use one solution identity and require one `profile_id` from `cinematic_live_action|motion_comic|stylized_animation|brand_film`. Profiles SHALL share the same owner-boundary, evidence, repair and output semantics and MUST NOT create four independent state systems.

#### Scenario: Consumer selects motion comic

- **WHEN** the consumer resolves the motion-comic profile
- **THEN** it SHALL receive profile constraints layered over the same solution roles
- **AND** SHALL not resolve a separate canonical production owner

### Requirement: Official package SHALL cover the full semantic compilation chain

The solution SHALL provide project-intent, asset-dependency, scene-package, shot-prompt, ShotAudioIntent, continuity-review and failure-restructure roles. Each role SHALL declare goals, typed/bounded inputs, semantic outputs, owner boundary, QC, failure modes and bounded repair.

#### Scenario: Consumer needs only shot prompt compilation

- **WHEN** accepted upstream refs already exist
- **THEN** it MAY render only the shot-prompt role
- **AND** SHALL not require the model to regenerate project intent or asset canon

### Requirement: Existing official solutions SHALL be referenced, not copied

Character asset and storyboard breakdown capabilities SHALL use exact released `promptrepo://` dependency refs. The new solution MUST NOT duplicate their mutable bodies, schemas or fixture truth.

#### Scenario: Character asset dependency updates

- **WHEN** a newer character asset release exists
- **THEN** the film solution SHALL remain pinned to its declared compatible release
- **AND** any upgrade SHALL create a reviewed new solution release

### Requirement: Prompt Bundle SHALL separate fixed rules, accepted facts and task delta

Every role SHALL layer owner/safety rules, profile contract, accepted source projection, exact reference bindings, one task delta, output/findings contract and bounded self-check. Source story data SHALL be treated as untrusted content and MUST NOT override role/schema/policy.

#### Scenario: Source text contains prompt injection

- **WHEN** a scene line asks the model to ignore schema or reveal secrets
- **THEN** the role SHALL treat it only as story data
- **AND** output SHALL remain in the declared semantic schema

### Requirement: Reference binding SHALL declare inherit and forbid scopes

Identity, wardrobe, location and prop references SHALL declare exact roles, versions/digests, inherited dimensions and forbidden influence. Multi-reference composition MUST NOT erase source lineage or claim pixel-level identity guarantees.

#### Scenario: Identity source contains dramatic makeup

- **WHEN** makeup is not part of the accepted identity canon
- **THEN** the identity binding SHALL list makeup under forbidden influence
- **AND** the shot Prompt SHALL not inherit it implicitly

### Requirement: Shot prompts SHALL describe one major change and observable performance

One shot role SHALL focus on one primary action/emotional change, with first-frame lock, camera/optics, action timeline, gaze/breath/muscle/weight behavior, physics, light/audio roles and positive continuity locks. Abstract emotion alone SHALL be invalid.

#### Scenario: One shot requests many story events

- **WHEN** a task combines entry, discovery, argument, explosion and orbit camera in one short shot
- **THEN** validation SHALL return a shot-restructure finding
- **AND** SHALL propose multiple causal beats or coverage shots

### Requirement: Reroll and repair SHALL be bounded

Each reroll SHALL declare one allowed variable class. Repair SHALL change only finding-targeted dimensions and preserve accepted refs/profile/prompt snapshot. After retry threshold, failure-restructure SHALL recommend a structural alternative instead of adding unbounded adjectives.

#### Scenario: Identity drift affects multiple expression cells

- **WHEN** two or more cells drift in identity/capture
- **THEN** repair SHALL raise a baseline/reference blocker
- **AND** SHALL not keep repairing each cell independently

### Requirement: Model output SHALL not create canonical owner facts

Templates MUST prohibit canonical refs/digests, timestamps, idempotency, expected versions, accepted/frozen/delivered states, budget/provider receipts, credentials, raw provider payloads and chain-of-thought. Consumer owners SHALL append deterministic fields after validation and human review.

#### Scenario: Model emits `accepted=true`

- **WHEN** semantic output contains an owner terminal field
- **THEN** consumer conformance SHALL reject it with a stable forbidden-field reason
- **AND** no canonical mutation or provider rerun SHALL occur

### Requirement: Locale, rights and maturity SHALL be explicit

`zh-CN` SHALL be the source locale; `en` SHALL remain draft/stale until human review against the source digest. Initial rights SHALL be internal and maturity SHALL remain exploratory/profile-candidate until provider-free conformance, owner consumer tests, human content review and four complete profile canaries pass.

#### Scenario: Only one profile canary passes

- **WHEN** brand-film evidence passes but other profiles do not
- **THEN** the package SHALL not claim unified first-support maturity
- **AND** each profile SHALL retain its truthful readiness label

### Requirement: Structured metadata SHALL be authored through Template Registry

Machine-readable solution metadata, contracts, schemas, fixture manifests, catalog and release locks MUST be created/updated by Template Registry CLI/application service. Prompt/profile/example prose MAY be edited directly.

#### Scenario: Catalog validation runs

- **WHEN** content prose and CLI-authored structured assets are ready
- **THEN** catalog build/validate SHALL be deterministic
- **AND** secret/raw Prompt evidence/private project data scans SHALL pass
