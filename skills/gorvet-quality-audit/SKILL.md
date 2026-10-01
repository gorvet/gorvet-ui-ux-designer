---
name: gorvet-quality-audit
description: Run a final cross-cutting audit of UI/UX work for generic AI design defaults, unnecessary complexity, design-system drift, duplicate components, hardcoded styling, accessibility risk, SEO applicability, and maintainability. Use before declaring substantial frontend work complete or when refactoring AI-generated UI.
license: MIT
metadata:
  author: GORVET
---

# UI Quality Audit

Audit by impact, not by number of findings.

## 1. Intentionality

Every major visual device should communicate hierarchy, grouping, interaction, state, sequence, emphasis, elevation, or brand. If not, simplify.

Read `references/ai-default-patterns.md` and look for accumulation of unrelated AI defaults rather than banning individual styles.

## 2. System discipline

Check for:

- raw/hardcoded values that duplicate tokens/utilities;
- duplicate near-identical components;
- new dependencies that solve trivial problems;
- custom controls where native/library primitives exist;
- local fixes that should be a shared component/token change;
- inconsistent states, radius, spacing, type or color semantics.

## 3. UX quality

Check task clarity, primary action, feedback, recovery, empty/error/loading states, avoidable steps, hidden frequent actions, and misleading disabled states.

## 4. Accessibility

Critical keyboard, focus, semantics, labels, contrast/state cues and dynamic behavior issues block completion when applicable.

## 5. SEO

For public indexable pages, verify that technical SEO intent is coherent. For private/admin UI, do not create unnecessary SEO work.

## 6. Output

Return only prioritized findings:

```text
BLOCKERS
MAJOR
MODERATE
OPTIONAL POLISH
```

Whenever possible, fix blockers/major issues instead of merely listing them.
