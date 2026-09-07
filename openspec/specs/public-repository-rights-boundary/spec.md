# public-repository-rights-boundary Specification

## Purpose
TBD - created by archiving change official-public-repository-rights-boundary-v1. Update Purpose after archive.
## Requirements
### Requirement: Public visibility does not widen content permission
The repository SHALL distinguish GitHub visibility from solution rights, template license and permission, external asset license, and user asset authority.

#### Scenario: Internal-rights solution in the public catalog
- **WHEN** a public catalog entry declares `rights: internal`
- **THEN** documentation keeps that restriction and does not describe the entry as open-source or freely reusable

### Requirement: External licenses remain scoped
External Skill, software, media, font, and product-asset licenses SHALL remain attached to their own artifacts and SHALL NOT propagate through a template reference or package export.

#### Scenario: Apache-licensed external Skill with separately licensed media
- **WHEN** an integration references an Apache-2.0 Skill whose runtime also uses separately licensed software or media
- **THEN** the integration records each rights check separately and blocks a complete portable claim when a required artifact is unresolved

