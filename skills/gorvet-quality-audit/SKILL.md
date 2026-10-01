---
name: gorvet-quality-audit
description: Run a final cross-cutting audit of UI/UX work for generic AI design defaults, typographic/editorial drift, density/viewport problems, unnecessary complexity, design-system drift, duplicate components, hardcoded styling, accessibility risk, SEO applicability, and maintainability. Use as a completion gate for substantial new or redesigned interfaces and when refactoring AI-generated UI.
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

## 2. Composition, density and viewport gate

Check the page as a composition, not only as independent components.

- Identify the intended first, second and third attention targets in each major viewport. Several equally dominant elements competing simultaneously is a hierarchy defect.
- Check realistic laptop viewport heights as well as widths. A hero that only feels complete on a tall design canvas should be revised.
- Do not require the first viewport to contain headline, long copy, multiple CTAs, tags, metrics, a showcase panel and decorative background effects at once.
- Flag high-complexity side-by-side modules when simultaneous viewing is not functionally useful.
- Check that whitespace is allowed to separate hierarchy rather than being filled with another card, badge, illustration, metric or effect.
- Decorative grid/dot/noise/gradient/glow backgrounds must remain subordinate to content and must not be used automatically to signal technology/AI.
- Density must follow content/task needs rather than visual abundance.

If the first screen feels clipped, cramped, noisy or visually unresolved at a common target viewport, completion fails until hierarchy/density is corrected.

## 3. Typography and editorial consistency

Treat typography as a system.

Check:

- coherent hierarchy across `h1`, `h2`, `h3`, supporting/subheading copy, body, labels and metadata;
- proportional scale without exaggerated display sizes or arbitrary jumps;
- appropriate line-height, measure, weight and spacing, not font-size alone;
- responsive type that preserves relationships instead of carrying oversized desktop scale into smaller viewports;
- headings/titles that do not end in periods by default;
- short display/supporting copy vs normal prose punctuation handled according to semantic role;
- no body/supporting text made artificially small simply to exaggerate headline contrast.

Follow an explicit project/editorial style guide when one exists.

## 4. System discipline

Check for:

- raw/hardcoded values that duplicate tokens/utilities;
- duplicate near-identical components;
- new dependencies that solve trivial problems;
- custom controls where native/library primitives exist;
- local fixes that should be a shared component/token change;
- inconsistent states, radius, spacing, type or color semantics;
- a second token/component system created unnecessarily beside the project system.

## 5. UX quality

Check task/content clarity, primary action, feedback, recovery, empty/error/loading states where relevant, avoidable steps, hidden frequent actions, and misleading disabled states.

For content-led/public pages, also verify that the section/component architecture follows the information rather than a generic page template.

## 6. Accessibility gate

Accessibility baseline applies to human-facing UI. Critical keyboard, focus, semantics, labels, contrast/state cues, zoom/reflow, motion and dynamic behavior issues block completion when applicable.

Review ARIA intentionality: generic containers should not receive ARIA merely for decoration; redundant visual diagrams may need to be hidden from assistive technology; live regions must be justified by meaningful updates; ARIA states must match real interaction state.

If a deeper accessibility specialist was needed, ensure its critical findings were actually resolved rather than only mentioned.

## 7. SEO gate

For public indexable pages, verify that technical SEO intent is coherent and that relevant `gorvet-frontend-seo` decisions were implemented.

Deployment-dependent items such as canonical URL, `og:url`, absolute social-image URL, sitemap location or `hreflang` destinations may be deferred when required information is unavailable, but the dependency must be recognized explicitly. Silent omission is not analysis.

For private/admin UI, do not create unnecessary SEO work.

## 8. Evidence and correction

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
