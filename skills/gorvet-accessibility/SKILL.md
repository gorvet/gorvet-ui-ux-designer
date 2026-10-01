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

## Test beyond automation

When capabilities are available, include keyboard walkthrough, focus review, semantic/DOM review, contrast, zoom/narrow viewport, and screen-reader smoke checks for critical flows. Automated scanners are useful but insufficient.

## Severity

Report blockers/major issues before minor polish and identify the affected interaction/user mode and a concrete verification step.
