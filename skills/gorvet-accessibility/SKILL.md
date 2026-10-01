---
name: gorvet-accessibility
description: Design, implement, and review accessible inclusive interfaces. Use for semantic HTML, keyboard flows, focus management, screen-reader behavior, labels, contrast, target sizes, zoom/text resize, motion, dynamic updates, media alternatives, and WCAG-oriented quality.
license: MIT
metadata:
  author: GORVET
---

# Accessibility & Inclusive Design

Accessibility is normal product quality, not a final checkbox.

Default target: **WCAG 2.2 AA expectations** unless the project defines a stricter target. Do not make legal-conformance claims without appropriate validation.

## Core rules

- Native semantic HTML first; ARIA fills semantic gaps, it does not recreate missing behavior automatically.
- Links navigate; buttons act.
- Every interactive control is keyboard reachable, operable, and visibly focused.
- Source/reading order should match logical interaction order; do not repair bad order with positive `tabindex`.
- Persistent form labels; clear programmatic error/help relationships.
- Do not convey state by color alone.
- Maintain usable contrast for text, icons, focus and meaningful controls.
- Dynamic state changes that are not visually obvious to assistive technology need appropriate announcements.
- Modals/disclosures/menus require correct focus and keyboard behavior.
- Respect zoom, text resizing, narrow widths and content expansion.
- Motion must be purposeful and respect reduced-motion preferences.
- Touch targets and spacing must support motor accessibility.
- Decorative images use empty alternatives; informative media needs meaningful alternatives.

## ARIA intentionality

Do not add ARIA as decorative metadata or as a substitute for choosing the right semantic element.

- Prefer native elements and relationships (`nav`, `main`, `button`, headings, lists, form controls, `aria-labelledby` where appropriate) before generic `div` + ARIA.
- An `aria-label` on a generic container is not automatically useful. First decide whether the region/graphic is meaningful, interactive, redundant, or decorative.
- If a visual diagram/ornament repeats information already available in nearby text and adds no independent meaning, prefer hiding it from assistive technology (`aria-hidden="true"`) rather than giving it a verbose accessible name.
- If a custom visualization conveys unique information, expose that information through meaningful semantics/text, not only a label on an otherwise opaque container.
- Use `aria-live` only for updates that genuinely need announcement. Do not announce passive scroll-driven decoration/status changes or repeatedly restate visible content.
- Do not duplicate accessible names already provided by visible text unless the alternative name materially improves comprehension.
- Keep ARIA states (`aria-expanded`, `aria-pressed`, `aria-selected`, etc.) synchronized with real interaction state.

## Test beyond automation

When capabilities are available, include keyboard walkthrough, focus review, semantic/DOM review, contrast, zoom/narrow viewport, and screen-reader smoke checks for critical flows. Automated scanners are useful but insufficient.

## Severity

Report blockers/major issues before minor polish and identify the affected interaction/user mode and a concrete verification step.
