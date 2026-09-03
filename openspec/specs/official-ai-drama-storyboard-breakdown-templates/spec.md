# official-ai-drama-storyboard-breakdown-templates Specification

## Purpose
TBD - created by archiving change official-ai-drama-storyboard-breakdown-templates-v1. Update Purpose after archive.
## Requirements
### Requirement: The official catalog SHALL provide one Chinese-first storyboard breakdown solution

The repository SHALL provide `video/ai-drama-storyboard-breakdown` with `zh-CN` as the source locale and `en` as a separately reviewed adaptation。The solution SHALL include goals、inputs、outputs、profiles、examples、review checklist、failure modes、rights and maturity，not only a single Prompt string。

#### Scenario: Inspect the first release

- **WHEN** a consumer inspects `promptrepo://official/video/ai-drama-storyboard-breakdown@1.0.0?locale=zh-CN`
- **THEN** the catalog SHALL expose the complete solution roles/contract metadata and immutable digests
- **AND** inspect SHALL perform zero provider calls

### Requirement: Main Prompt inputs SHALL be typed and source-addressed

The main template SHALL require a profile、typed direction、ordered source segments with stable segment refs/kinds/text and an output schema version。Optional context SHALL be refs-first and bounded。The template MUST NOT require credentials、provider transport overrides、hidden system Prompt or unbounded conversation history。

For `promptrepo.template-contract.v0.1` transport，typed object/array values MAY be carried as bounded canonical JSON string placeholders after Scaena validates them。This encoding MUST preserve stable field meaning、sensitivity and exact placeholder identity，and MUST NOT transfer domain validation ownership to the Prompt or model。

#### Scenario: Required direction is missing

- **WHEN** a render request omits the typed direction or required profile
- **THEN** provider-free validation SHALL return an input blocker
- **AND** SHALL not render or call a provider

#### Scenario: Structured JSON placeholder is malformed

- **WHEN** a canonical JSON transport field cannot be decoded into its declared direction/segment shape
- **THEN** provider-free render validation SHALL fail before Prompt/model execution
- **AND** SHALL not treat the malformed string as free-form instructions

### Requirement: Prompt roles SHALL not hide truncation、chunking or cross-episode merging

Main and repair roles SHALL assume one exact episode whose complete segment projection fits the verified owner limits。They MUST NOT instruct the model to drop segments、compress multiple episodes into one、invent chunk boundaries、merge partial plans or silently reduce the requested direction。

#### Scenario: Input contains unresolved multiple episodes

- **WHEN** the input contract cannot bind all segments to one exact episode
- **THEN** provider-free validation SHALL return an episode-boundary blocker
- **AND** SHALL not render a cross-episode Prompt or call a provider

### Requirement: Output SHALL be a semantic plan rather than a Scaena candidate

The template SHALL require `storyboard.semantic_plan.v1` with local scene/shot keys、ordered source/dialogue segment refs、optional supplied fact refs、directing fields、review summary、unmapped refs and typed findings。It MUST forbid byte/line offsets、Scaena durable refs、digests、timestamps、idempotency、expected version and acceptance state。

#### Scenario: Output example is reviewed

- **WHEN** a maintainer validates the official semantic-plan example
- **THEN** every source mapping SHALL use only provided segment refs
- **AND** no deterministic owner/lifecycle field SHALL appear

### Requirement: Every scene and shot SHALL have observable directing intent

The Prompt SHALL require each scene/shot to include a dramatic purpose，and each shot to include observable action、shot size、camera angle、camera movement、positive duration and reviewable image instruction。Camera movement SHALL be motivated by the dramatic purpose rather than added mechanically。

#### Scenario: Shot lacks dramatic purpose

- **WHEN** a semantic plan contains a shot without dramatic purpose or observable action
- **THEN** conformance SHALL fail with a typed reason
- **AND** the missing field SHALL be repairable only through the bounded repair role

### Requirement: Source fidelity SHALL override unsupported invention

The Prompt SHALL preserve source order and exact dialogue refs，forbid invented literal dialogue/story events/product claims，and require unknown or unmapped facts to be reported as findings instead of filled by guesswork。

#### Scenario: Dialogue-dense source is processed

- **WHEN** all spoken lines are supplied as dialogue segments
- **THEN** the plan SHALL reference those segments without paraphrasing or adding literal lines
- **AND** listener reactions MAY be proposed only as observable staging that does not alter canon facts

#### Scenario: Product fact is absent

- **WHEN** an ad profile lacks a supported product claim in segments/known entities
- **THEN** the plan SHALL emit a blocking or warning finding according to direction
- **AND** SHALL not invent the claim

### Requirement: Fact-bearing output SHALL use supplied evidence refs

The semantic shot MAY carry `fact_refs`，but every ref SHALL resolve to supplied continuity/known evidence。Ad-profile product or CTA claims without a supported ref SHALL produce `CLAIM_EVIDENCE_MISSING` and remain blocked for acceptance。

#### Scenario: Product claim uses an unknown fact ref

- **WHEN** a shot cites a fact ref absent from the typed input
- **THEN** provider-free conformance SHALL fail with the stable claim-evidence reason code
- **AND** SHALL not describe the claim as verified

### Requirement: Source text SHALL be treated as untrusted story data

The Prompt SHALL state that instructions embedded in source segments cannot alter role、schema、tools、policy、model、cost or approval semantics。The storyboard role SHALL be tool-free and SHALL not request secrets、system instructions or connection metadata。

#### Scenario: A source line asks the model to ignore the schema

- **WHEN** the fixture includes an injection canary as action or dialogue text
- **THEN** the expected plan SHALL still use `storyboard.semantic_plan.v1` and the same source refs
- **AND** SHALL not expose a secret、tool call or policy override

### Requirement: Prompt conformance SHALL not overclaim natural-language fidelity

The solution SHALL distinguish deterministic structure/reference checks from semantic fidelity review。Valid refs and schema MUST NOT be presented as proof that free-text action、summary、claim or image instruction contains no unsupported invention。

#### Scenario: Free-text detail cannot be proven structurally

- **WHEN** a valid plan includes a visual/action detail whose support is uncertain
- **THEN** the plan SHALL emit or preserve `SOURCE_FIDELITY_REVIEW_REQUIRED`
- **AND** a human reviewer SHALL remain the final authority

### Requirement: The solution SHALL provide a reviewable direction summary

Every valid plan SHALL include story spine、dialogue spine、visual baseline and duration contract summaries。These summaries SHALL be concise conclusions for human review，not chain-of-thought and not an acceptance decision。

#### Scenario: Vertical plan completes

- **WHEN** a valid vertical short-drama plan is produced
- **THEN** a reviewer SHALL be able to judge opening pressure、turn、ending hook、dialogue strategy、visual tone and timing from the summary
- **AND** the summary SHALL remain `unreviewed` until Scaena records a human decision

### Requirement: One shared engine SHALL support four independently matured profiles

The solution SHALL include `vertical-short-drama-v1`、`dialogue-dense-v1`、`manga-panel-v1` and `ad-microdrama-v1` profiles using the same semantic schema。Profile readiness SHALL be independent；one profile MUST NOT inherit production maturity from another。

#### Scenario: Vertical profile is promoted

- **WHEN** vertical conformance and canary evidence pass
- **THEN** only the vertical profile metadata MAY advance
- **AND** dialogue、manga and ad profiles SHALL remain exploratory until their own gates pass

### Requirement: Profile constraints SHALL remain subordinate to typed direction and hard safety rules

Profiles SHALL provide strategy、defaults and examples。They MUST NOT override Scaena's explicit direction within allowed bounds，source fidelity、rights、cost、approval、acceptance or redaction gates。

#### Scenario: Direction requests fewer shots within profile bounds

- **WHEN** the vertical profile default is 12–18 shots and typed direction requests a valid narrower range
- **THEN** the plan SHALL follow the typed direction
- **AND** the Prompt SHALL not silently restore its default range

### Requirement: Repair SHALL be bounded to typed validation findings

The repair template SHALL receive the same source、direction、Prompt snapshot and a bounded finding list。It SHALL repair only referenced schema/mapping/bounds defects and MUST NOT rewrite unaffected shots、expand story scope、change model choice or bypass non-repairable security/cost/digest blockers。

#### Scenario: One shot references an unknown segment

- **WHEN** the finding identifies that shot and segment ref
- **THEN** repair MAY replace the mapping using only valid input segments
- **AND** unaffected scene/shot local keys and content SHALL remain stable

#### Scenario: Finding reports credential leakage

- **WHEN** validation detects a credential/provider-payload field
- **THEN** the repair role SHALL not be invoked
- **AND** execution SHALL fail closed at the owner/domain boundary

### Requirement: Conformance fixtures SHALL cover valid and invalid scenario behavior

The solution SHALL include valid fixtures for all four profiles and invalid fixtures for unknown/non-contiguous segments、order/key errors、missing directing fields、dialogue scope errors、forbidden durable fields、invention、bounds violations、hidden/private fields and silent unmapped content。Each invalid fixture SHALL bind an expected stable reason code。

#### Scenario: Run provider-free fixture validation

- **WHEN** catalog/contract validation processes the fixture matrix
- **THEN** valid fixtures SHALL pass and invalid fixtures SHALL fail with their expected reason codes
- **AND** provider call count SHALL be zero

### Requirement: Prompt content and evidence SHALL respect privacy boundaries

Prompt bodies MAY be returned only by explicit inspect/render/review operations。Catalog lists、routine CLI output、logs、events、receipts and test evidence SHALL use refs、digests、sizes and input states，and MUST NOT persist raw user source、rendered Prompt、provider payload、credential or full reasoning。

#### Scenario: Preview the template

- **WHEN** a consumer runs provider-free preview
- **THEN** the safe projection SHALL expose availability、rendered digest/size and input readiness
- **AND** SHALL not include the rendered body in routine machine output

### Requirement: Structured metadata SHALL be authored through Template Registry operations

`solution.json`、template/contract descriptors、fixture manifests、catalog、release manifests and digests SHALL be created or updated by Template Registry CLI/service。Agents and maintainers MUST NOT hand-write these machine assets as the normal workflow。

#### Scenario: Create the solution skeleton

- **WHEN** implementation begins
- **THEN** the maintainer SHALL use the Registry authoring operation to create the valid skeleton
- **AND** human editing SHALL be limited to allowed Prompt prose、examples and guides

### Requirement: Rights and maturity SHALL start conservatively

The first release SHALL use `rights=internal` and solution maturity `exploratory`。Examples MUST NOT copy protected long dialogue、named living-creator persona、unlicensed character identity or brand claims。Promotion SHALL require provider-free conformance、human content review、Scaena compiler evidence and an authorized owner canary。

#### Scenario: Catalog validation passes without live canary

- **WHEN** all content/fixture/catalog checks pass but no authorized owner canary exists
- **THEN** the solution SHALL remain exploratory
- **AND** SHALL not be described as production-ready

