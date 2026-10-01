---
name: gorvet-visual-qa
description: Perform visual and responsive QA on implemented interfaces using rendered pages, screenshots, or static code evidence. Use after UI implementation or when diagnosing an existing screen; verifies hierarchy, spacing, states, references, responsiveness, accessibility smoke checks, and visible AI-template defects.
license: MIT
metadata:
  author: GORVET
---

# Visual QA

A successful build is not proof of a successful interface.

## Evidence levels

Use the strongest available evidence:

1. rendered interactive interface in a browser/runtime;
2. supplied screenshots at relevant states/viewports;
3. static markup/styles/components as a fallback.

State what could not be visually verified. Never pretend static code review is rendered QA.

## Inspect

- primary hierarchy and action prominence;
- grouping/proximity/alignment;
- density and scanability;
- typography and content measure;
- surface/border/shadow/radius consistency;
- section/component silhouette repetition that exposes a generic template;
- unnecessary decorative completion: icons, pills, badges, metrics, cards, blobs, gradients or dividers that do not add meaning;
- long content, overflow and truncation;
- empty/loading/error/disabled/selected/success states where relevant;
- mobile/narrow, intermediate and wide behavior relevant to the product;
- keyboard focus visibility and obvious accessibility regressions;
- comparison with project references/specification when supplied;
- whether reference principles were transferred rather than superficial brand motifs copied;
- visual evidence of hardcoded drift or duplicate component styling.

## Anti-template visual pass

Temporarily ignore the copy and compare the silhouettes of major regions. If many unrelated sections collapse to the same anatomy (for example eyebrow + giant heading + lede + card grid, or rounded CTA band), treat that as a design defect unless the repeated semantics justify it.

Also inspect whether “modernity” is being manufactured by stacking effects such as glass + gradient + large radius + shadow + glow + reveal motion. Prefer a smaller coherent motif set.

## Iteration

Fix high-impact visible defects, re-render/reinspect when possible, and avoid endless polish loops. Prioritize task/content clarity, accessibility, responsive correctness, architecture and system consistency before decorative refinement.

Use `gorvet-quality-audit` as the final completion gate for substantial new/redesigned UI.
