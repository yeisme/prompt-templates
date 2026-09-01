# official-template-contract-pilot Specification

## Purpose
TBD - created by archiving change official-prompt-template-contract-pilot-v1. Update Purpose after archive.
## Requirements
### Requirement: Official contract sidecars MUST describe actual placeholders

Every declared input SHALL correspond to an exact `{{name}}` placeholder in the selected Prompt. Required/default/type/enum semantics SHALL be equivalent across reviewed locale adaptations.

#### Scenario: The Xiaohongshu cover contract is inspected

- **WHEN** a consumer loads either the zh-CN or en main contract
- **THEN** it SHALL find exactly `product`, `audience`, `selling_point`, `visual_style`, and `aspect_ratio`
- **AND** the corresponding Prompt SHALL contain every declared placeholder.

#### Scenario: The podcast narration contract is inspected

- **WHEN** a consumer loads either the zh-CN or en main contract
- **THEN** it SHALL find exactly `audience`, `duration`, `script`, `show_positioning`, and `tone`
- **AND** `script` SHALL be required and sensitive with no default, example, or enum value.

### Requirement: Chinese-first guidance MUST remain available across locales

The zh-CN contract SHALL be the source contract. The en adaptation SHALL keep stable machine names and equivalent constraints, and SHALL retain reviewed zh-CN labels/descriptions alongside English guidance.

#### Scenario: A Chinese user inspects the English template

- **WHEN** locale `en` is selected but display locale is zh-CN
- **THEN** the consumer SHALL be able to show zh-CN labels/descriptions from the sidecar
- **AND** it SHALL not translate or rename machine input keys.

### Requirement: Sidecars MUST NOT change catalog identity

Generated contract files SHALL remain outside `promptrepo.catalog.v0.1`. Catalog build and validate SHALL return the same digest before and after the pilot sidecars when Prompt and solution metadata are unchanged.

#### Scenario: The official catalog is rebuilt

- **WHEN** all image and audio pilot sidecars exist
- **THEN** catalog digest SHALL remain `sha256:d252148bb4e4f6be95f99848dd49bad43b6414f4b7ccd520fe71b3616ad37b2f`
- **AND** catalog output SHALL contain no input, license, permission, default, or example fields.

