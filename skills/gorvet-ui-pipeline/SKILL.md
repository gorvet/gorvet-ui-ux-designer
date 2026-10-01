---
name: gorvet-ui-pipeline
description: Coordinate the GORVET UI/UX Designer pipeline across any frontend stack. Use for new interfaces, redesigns, frontend implementation, UI reviews, or substantial UX work; routes only the specialist skills needed for Context → Design → Build → Review.
license: MIT
metadata:
  author: GORVET
---

# GORVET UI/UX Pipeline

Use the shortest professional path that produces a reliable result.

## Four stages

1. **Context** — understand task, users, project specification, references, existing UI, stack, tokens, components, constraints, and optional adapters.
2. **Design** — invoke only the specialist skills whose decision domains are present.
3. **Build** — implement using the existing stack and design system before creating new primitives.
4. **Review** — verify the rendered/resulting interface when possible, then run targeted quality checks and refine.

## Adaptive routing

- Small change in established UI: Context → Build → Review.
- New screen in established product: Context → relevant Design specialists → Build → Review.
- New product/system: Context → IA/usability/structure/design-system/accessibility (+ other specialists) → Build → Review.
- Existing weak UI: Context → QA/Audit → targeted Design → Build → Review.

Do not run every skill by default. Specialist count is not pipeline length.

## Specialist routing

Use when relevant:

- information hierarchy/navigation/search → `gorvet-information-architecture`
- task flow/usability/recovery → `gorvet-ux-usability`
- visual composition/greybox/density → `gorvet-ui-structure-design`
- tokens/components/system consistency → `gorvet-design-system`
- interaction choice/state behavior → `gorvet-interaction-patterns`
- forms/data entry/checkout → `gorvet-forms`
- interface labels/errors/microcopy → `gorvet-ux-content`
- accessibility/inclusive behavior → `gorvet-accessibility`
- public/indexable search discoverability → `gorvet-frontend-seo`
- code implementation → `gorvet-ui-implementation`
- rendered result → `gorvet-visual-qa`
- final cross-cutting audit → `gorvet-quality-audit`

## Handoffs

Pass decisions, not essays. Keep working context compact:

- Context: requirements, source-of-truth hierarchy, stack, reusable system, references, risks.
- Design: hierarchy, patterns, states, responsive rules, visual/system decisions.
- Build: reuse decisions, files/areas changed, new tokens/components only if needed.
- Review: defects found, corrections made, anything not verified.

Create persistent documentation only when it prevents future rediscovery. Do not require a document for each stage.

## Completion

Do not call UI work complete merely because code compiles. When visual evidence is available, inspect the result. When accessibility/SEO apply, their critical requirements are part of completion, not optional polish.
