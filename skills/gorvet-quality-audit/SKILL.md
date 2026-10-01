---
name: gorvet-quality-audit
description: Run a final cross-cutting audit of UI/UX work for generic AI design defaults, unnecessary complexity, design-system drift, duplicate components, hardcoded styling, accessibility risk, SEO applicability, and maintainability. Use as a completion gate for substantial new or redesigned interfaces and when refactoring AI-generated UI.
license: MIT
metadata:
  author: GORVET
---

# UI Quality Audit

Audit by impact, not by number of findings. For substantial new/redesigned UI, this is a completion gate, not optional polish.

## 1. Intentionality and anti-AI gate

Read `references/ai-default-patterns.md`.

Every major visual device should communicate hierarchy, grouping, interaction, state, sequence, emphasis, elevation, continuity, or brand. If not, simplify.

Run the repetition test: mentally ignore the copy and compare the silhouettes of major regions/sections. Flag template-driven repetition such as repeated eyebrow/header stacks, rounded content islands, identical card grids, universal CTA blocks, pills, hover-lift, reveal-on-scroll, or decorative gradients/glass/blobs that recur without semantic reason.

Also check for “modern UI bundles”: multiple unrelated premium effects combined by default rather than by a coherent visual language.

If generic AI-pattern accumulation materially weakens the design, do not merely report it. Restructure/simplify the affected areas before completion when editing capability exists.

## 2. System discipline

Check for:

- raw/hardcoded values that duplicate tokens/utilities;
- duplicate near-identical components;
- new dependencies that solve trivial problems;
- custom controls where native/library primitives exist;
- local fixes that should be a shared component/token change;
- inconsistent states, radius, spacing, type or color semantics;
- a second token/component system created unnecessarily beside the project system.

## 3. UX quality

Check task/content clarity, primary action, feedback, recovery, empty/error/loading states where relevant, avoidable steps, hidden frequent actions, and misleading disabled states.

For content-led/public pages, also verify that the section/component architecture follows the information rather than a generic page template.

## 4. Accessibility gate

Accessibility baseline applies to human-facing UI. Critical keyboard, focus, semantics, labels, contrast/state cues, zoom/reflow, motion and dynamic behavior issues block completion when applicable.

If a deeper accessibility specialist was needed, ensure its critical findings were actually resolved rather than only mentioned.

## 5. SEO gate

For public indexable pages, verify that technical SEO intent is coherent and that relevant `gorvet-frontend-seo` decisions were implemented. Missing deployment information may justify deferring specific items (for example a canonical URL), but silent omission is not a substitute for analysis.

For private/admin UI, do not create unnecessary SEO work.

## 6. Evidence and correction

Prefer to fix blockers and major issues before delivery, then re-check the affected areas once. Avoid endless polishing loops.

If the runtime cannot edit or render, state the limitation and return the highest-confidence audit possible from available evidence.

## Output

When findings remain, prioritize them:

```text
BLOCKERS
MAJOR
MODERATE
OPTIONAL POLISH
```

If no material finding remains, completion may proceed.
