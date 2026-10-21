# Design handoff reinforcement review

Date: 2026-10-21. Scope: six requested skills and directly related pipeline documentation. Source-only update; no release, installation or external design modification.

## Confirmed diagnosis

The repository already required a pre-Build architecture handoff and proposal-specific `PASS` preflight. Brief-to-Build execution on substantial UI therefore violated an existing gate; the source inspection cannot establish why the reported agent bypassed it.

Confirmed gaps were explicit editable-design construction, source-to-destination system mapping, separate contract-conformance evidence, deviation disposition and review-only correction boundaries. Structure, visual hierarchy, anti-AI principles, adaptive scope and technical-adapter precedence already existed and were retained.

## Changed files and responsibility

| File | Purpose |
| --- | --- |
| `skills/gorvet-ui-pipeline/SKILL.md` | Own the existing handoff as the compact design contract, with scope, executor discretion and change handling. |
| `skills/gorvet-ui-structure-design/SKILL.md` | Make existing decisions addressable and actionable for either output mode. |
| `skills/gorvet-design-system/SKILL.md` | Own mapping and reuse of the system slice used in the destination. |
| `skills/gorvet-ui-implementation/SKILL.md` | Consume the contract through shared Build entry and functional/frontend or editable-design modes. |
| `skills/gorvet-visual-qa/SKILL.md` | Compare against the contract separately from visual quality; distinguish evidence capabilities. |
| `skills/gorvet-quality-audit/SKILL.md` | Classify deviations and correction disposition; preserve review-only scope. |
| `docs/PIPELINE.md` | Align the existing overview through links to the owning rules. |
| `docs/PIPELINE_TESTS.md` | Add four behavioral evaluation briefs without replacing existing regression cases. |
| `docs/HANDOFF_REVIEW.md` | Preserve this diagnosis, scenario walkthrough and verification limits. |

## Resulting flow

Design resolves architecture, treatment and applicable specialist decisions in the existing handoff. The pipeline consolidates only relevant commitments, system references, acceptance conditions and executor freedom. Build materializes them using mandatory destination contracts. Visual QA reports both conformance and visual quality; Quality Audit determines severity, required corrections and the evidence-supported verdict. A material capability conflict returns only the affected decision to Design before construction continues.

The four stages remain unchanged. Small established changes use the request and current system as their baseline. Review-only tasks stop at findings and recommendations.

## Manual scenario walkthrough

These are instruction-level evaluations using concrete hypothetical inputs and counterexamples, not executions of a design agent or inspections of generated interfaces. The four routes were traced across the edited skills; no live Figma file or frontend test project was created. Behavioral runs remain `NOT RUN` under `PIPELINE_TESTS.md`.

### 1. New landing in Figma from a brief

Input: editable workshop landing with supplied session content and a brand library. A sufficient contract could identify offer → session comparison → booking, the primary booking action, subdued supporting details, type/color roles bound to the existing system, and a narrow layout preserving that sequence. Exact layout/treatment must be resolved in Design, not inferred by the tool while creating nodes. Acceptance includes editable native elements, relevant component instances/bindings and represented narrow/wide states. Tool-specific prerequisites determine construction mechanics.

Trace result: pipeline contract → structure preflight → system mapping → editable Build → rendered/native conformance → deviation audit. No frontend framework is required. Counterexamples: a flattened image is a BLOCKER; a polished but materially different focal hierarchy is MAJOR; frames alone leave runtime behavior unproven. Instruction coverage is coherent; actual tool compliance remains unverified.

### 2. Existing frontend project

Input: session-selection screen in an established product. The contract can reference the existing selection component, primary-action token and typography roles, with concrete selected/empty/error behavior and summary-before-form order at narrow widths. Mapping may be existing project references; no duplicate token system or separate library inventory is needed.

Trace result: existing-project inspection → scoped Design decisions → frontend Build using current resources → conformance and visual checks → final audit. Counterexamples: replacing the shared selection component with a materially divergent clone or swapping primary/secondary prominence cannot pass merely because tests succeed. A framework constraint affecting the agreed layout returns that decision to Design. Instruction coverage is coherent; no frontend was executed.

### 3. Small change on an existing screen

Input: replace the button label with supplied text. The request and current component/style are the baseline. Build changes the label and verifies the affected content, instance/style preservation and possible overflow.

Trace result: Context → Build → scoped Review; no new contract file, architecture preflight, library map or full audit is required. The editable mode's system mapping consumes existing resources rather than requiring an additional artifact. Escalation occurs only if the change exposes material design decisions. Instruction coverage preserves the short route.

### 4. Audit without implementation

Input: inspect a screen with a visible hierarchy issue and return findings only. With a historical contract, QA reports expected-versus-observed decisions separately from visual defects. Without one, it evaluates supplied requirements and available quality evidence while identifying unavailable prior intent.

Trace result: Context → Review with no mutations. A material issue produces a remediation recommendation and may produce `REWORK`; it never grants editing authorization. Missing historical intent alone does not fail the audit; missing rendered evidence still limits visual claims. Instruction coverage is coherent for both baseline conditions.

## Validation and limits

- Repository validator: all 15 skills pass frontmatter/name/description and local-reference checks.
- Diff whitespace check: no errors.
- Manual ownership check: pipeline owns consolidation; structure owns design decisions; system owns mappings; implementation owns construction; visual QA owns conformance observations; audit owns severity/disposition. Consumer links replace a second orchestration/checklist.
- The scenario walkthrough confirms rule coverage, not agent reliability, artifact quality or tool behavior. Actual execution evidence is still needed for behavioral passes; cases F–I in `PIPELINE_TESTS.md` provide the corresponding briefs and failure criteria.
- Natural-language instructions cannot mechanically prevent an executor from bypassing a gate. Compliance still depends on the host loading and following the edited skills and destination instructions.
- The source repository was changed; an already installed plugin cache will continue using its installed version until updated through its normal release process.
