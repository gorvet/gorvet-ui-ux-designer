---
name: gorvet-quality-audit
description: Run a final cross-cutting audit of UI/UX work for generic AI design defaults, typographic/editorial drift, density/hierarchy problems, unnecessary complexity, design-system drift, duplicate components, hardcoded styling, accessibility risk, SEO applicability, and maintainability. Use as a completion gate for substantial new or redesigned interfaces and when refactoring AI-generated UI.
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

## 2. Composition, focal hierarchy and density gate

Check the interface as a composition, not only as independent components.

For every major section or functional region:

- identify the intended first, second and third attention targets;
- verify that several equally dominant elements are not competing simultaneously unless the task requires true side-by-side comparison;
- verify that supporting tags, metrics, metadata, previews, diagrams, code samples or secondary actions visibly recede from the region's main purpose;
- flag high-complexity side-by-side modules when simultaneous viewing is not functionally useful;
- check that whitespace is allowed to separate hierarchy rather than being filled with another card, badge, illustration, metric or effect;
- require decorative grid/dot/noise/gradient/glow backgrounds to remain subordinate to content and interaction;
- ensure density follows content/task needs rather than visual abundance.

Responsive states must preserve or deliberately re-map that priority. Do not keep every desktop element equally prominent simply because it fits.

If a major region feels cramped, noisy, visually unresolved or lacks a clear focal order, completion fails until hierarchy/density is corrected.

## 3. Typography and editorial consistency

Treat typography as a system.

Check:

- coherent hierarchy across primary title, section/region headings, component headings, supporting/subheading copy, body, labels and metadata;
- proportional scale without exaggerated display sizes or arbitrary jumps;
- appropriate line-height, measure, weight and spacing, not font-size alone;
- responsive type that preserves relationships instead of carrying oversized desktop scale into smaller spaces;
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

For every interface, verify that region/component architecture follows the actual information and task relationships rather than a generic page, dashboard or component template.

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

Always record a concise final verdict for substantial new/redesigned UI, including when no material finding remains:

```text
VERDICT: PASS | REWORK | UNVERIFIED
SCOPE / EVIDENCE: actual regions, states, viewports and evidence inspected
COMPOSITION: concrete repetition, focal-hierarchy and reference-transfer observations
FINDINGS / CORRECTIONS: severity, affected element, fix and re-check result
LIMITS / DEFERRALS: unverified applicable domains and missing dependencies, or none
```

- **PASS:** applicable checks have sufficient evidence, no blocker/major finding remains, and material corrections have been re-checked. Optional deployment-dependent SEO values may remain explicitly deferred; do not invent them to pass.
- **REWORK:** a blocker/major finding remains, or required execution evidence is missing but can be obtained. Correct the issue and re-check affected regions before delivery; do not let time pressure or functional success override the verdict.
- **UNVERIFIED:** an applicable quality domain cannot be evaluated sufficiently because of a genuine capability/input limitation. Identify the domain, evidence available and dependency needed. Known material defects remain named; do not disguise them as lack of evidence. Deliver only with an explicit bounded status, not as fully audited work.

Use concrete element/region names or selectors and observations, not generic assurances such as “modern”, “clean” or “no AI patterns”. On a pass, record what was compared and why recurring structures/effects serve the content. An image capture proves capture, not that its composition was assessed. An accessibility or functional check does not substitute for the composition audit.

Static evidence may support implementation findings; it cannot establish rendered typography, visual balance or responsive appearance. Keep those domains `UNVERIFIED` when rendered evidence is unavailable. On a revision, inspect the actual new artifact and affected cross-region patterns rather than carrying over the previous verdict.

Prioritize remaining findings as BLOCKERS, MAJOR, MODERATE or OPTIONAL POLISH. Keep the record proportional to the task and available in the working handoff; the user-facing delivery may remain brief.
