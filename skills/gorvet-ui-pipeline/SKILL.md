---
name: gorvet-ui-pipeline
description: Coordinate the GORVET UI/UX Designer pipeline across any frontend stack. Use for new interfaces, redesigns, frontend implementation, UI reviews, or substantial UX work; routes only the specialist skills needed for Context → Design → Build → Review while enforcing required quality gates.
license: MIT
metadata:
  author: GORVET
---

# GORVET UI/UX Pipeline

Use the shortest professional path that produces a reliable result. Specialist count is not pipeline length, but required quality domains must not be skipped merely to be shorter.

## Four stages

1. **Context** — understand task, users, surface, project specification, references, existing UI, stack, tokens, components, constraints, and optional adapters.
2. **Design** — resolve interface architecture first, then invoke only the specialist skills whose decision domains are present.
3. **Build** — implement using the existing/requested stack and design system before creating new primitives.
4. **Review** — inspect the resulting interface using the strongest evidence available, run the final quality gate, fix material defects when possible, then deliver.

## Context classification

Determine enough context to route correctly without creating bureaucracy:

- new vs existing interface;
- human-facing surface and primary user intent;
- public/indexable vs private/non-indexable when relevant;
- content/task complexity;
- requested/detected stack and existing system;
- supplied references and what they are meant to influence.

Ask only when missing information materially changes the solution.

## Design order

For substantial new or redesigned UI, `gorvet-ui-structure-design` acts as the interface architect before visual styling: infer necessary regions/sections, hierarchy, sequence, component patterns, actions, states and responsive transformation from the actual task/content.

Do not start from a generic landing/dashboard/template anatomy.

Then use other specialists only when their domains are present:

- information hierarchy/navigation/search → `gorvet-information-architecture`
- task flow/usability/recovery → `gorvet-ux-usability`
- unresolved user/task assumptions requiring evidence → `gorvet-ux-research-testing`
- interface architecture/greybox/composition/density/visual direction → `gorvet-ui-structure-design`
- tokens/components/system consistency → `gorvet-design-system`
- interaction choice/state behavior → `gorvet-interaction-patterns`
- forms/data entry/checkout → `gorvet-forms`
- labels/errors/microcopy/content clarity → `gorvet-ux-content`
- accessibility/inclusive behavior → `gorvet-accessibility`
- public/indexable search discoverability → `gorvet-frontend-seo`
- code implementation → `gorvet-ui-implementation`
- rendered/static visual result → `gorvet-visual-qa`
- final cross-cutting gate → `gorvet-quality-audit`

## Required baselines

- **Accessibility baseline applies to human-facing UI.** The depth varies with complexity/risk, but semantics, keyboard/focus, contrast/state cues, zoom/reflow and motion must not be silently ignored.
- **Public + indexable surfaces require frontend SEO analysis.** Implement what is supported by known deployment/project context; explicitly defer unknown deployment-specific values rather than silently omitting the domain.
- **Substantial new/redesigned UI requires final Quality Audit.** It is a completion gate.
- **Visual QA uses the strongest available evidence.** Render/browser/screenshots when available; static evidence otherwise, with limitations stated.

## Anti-AI control

Anti-AI quality is both preventive and corrective:

1. during Design, run the anti-AI preflight in `gorvet-ui-structure-design` before implementation;
2. during Review, run the repetition/accumulation checks in `gorvet-quality-audit`;
3. when material generic-template patterns remain and editing is possible, simplify/restructure before delivery.

Do not ban individual devices such as cards, gradients, pills, large type, glass, eyebrows or motion. Require a semantic, interaction, narrative or brand reason and avoid automatic bundles of “modern UI” effects.

## Adaptive routing examples

- Small change in established UI: Context → Build → Review.
- New screen in established product: Context → UI architecture + relevant Design specialists → Build → Review.
- New product/system: Context → UI architecture + relevant IA/usability/system/accessibility (+ other specialists) → Build → Review.
- Existing weak UI: Context → QA/Audit → targeted Design → Build → Review.

These are examples, not page-type triggers. Infer the needed specialists from the actual decision domains.

## Handoffs

Pass decisions, not essays. Keep working context compact:

- Context: requirements, source-of-truth hierarchy, stack, reusable system, references, risks.
- Design: architecture, hierarchy, component purposes, states, responsive rules, visual/system decisions, anti-AI risks.
- Build: reuse decisions, files/areas changed, new tokens/components only if needed.
- Review: evidence level, defects found, corrections made, anything not verified.

Create persistent documentation only when it prevents future rediscovery. Do not require a document for each stage.

## Observable execution gates

Reading a skill is preparation, not execution. For substantial new/redesigned UI, record the following concise decisions in the working handoff **before** crossing each transition. A compact tool-visible note or project artifact is sufficient; do not require user approval, a long report, or disclosure of private reasoning.

- **Context → Design:** task/content priorities, applicable constraints, and the specific properties to transfer from material references. Brand names alone are not a visual direction.
- **Design → Build:** proposed regions and their task/content purpose, focal hierarchy, responsive transformation, and the preflight verdict from `gorvet-ui-structure-design`. Build begins only after `PASS`; `REWORK` returns to Design. Record concrete decisions rather than “preflight done”.
- **Review → Delivery:** the `gorvet-quality-audit` verdict, identified regions/states, evidence actually inspected, material corrections and re-checks, and any unverified domain. Functional tests and screenshots alone do not establish visual quality.

Use the specialists' output contracts rather than inventing another checklist. If a required skill is unavailable, apply its known requirements explicitly and record that limitation; do not claim it was invoked. Missing execution evidence is an incomplete gate, not an implicit pass.

## Revisions and speed requests

Classify a follow-up by its effect, not by how few lines change. A request about modernity, visual appeal, monotony, density or resemblance to a reference requires inspecting the current composition and returning to Design + Review where the diagnosis calls for it. A palette-only change is valid when it addresses the diagnosed issue; do not assume it resolves a structural problem.

Carry forward still-valid context and decisions. Review both changed regions and any affected cross-page patterns. User requests for speed reduce scope and documentation, not applicable quality gates; report remaining verification limits instead of claiming an unsupported pass.

## Completion

Do not call UI work complete merely because code compiles. Completion means the result has passed the applicable architecture, accessibility, SEO, visual and quality checks with material defects fixed or explicitly bounded by runtime/project limitations.

`REWORK` prevents completion while material defects can be corrected. `UNVERIFIED` permits a bounded handoff when capabilities or inputs genuinely prevent verification, but it must not be described as a full quality pass. Mention unresolved material defects or verification limits briefly in delivery.
