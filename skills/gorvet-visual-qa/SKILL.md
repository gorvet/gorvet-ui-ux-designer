---
name: gorvet-visual-qa
description: Perform visual and responsive QA on implemented interfaces using rendered pages, screenshots, or static code evidence. Use after UI implementation or when diagnosing an existing screen; verifies hierarchy, spacing, states, references, responsiveness, and visible defects.
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
- long content, overflow and truncation;
- empty/loading/error/disabled/selected/success states;
- mobile/narrow, intermediate and wide behavior relevant to the product;
- keyboard focus visibility and obvious accessibility regressions;
- comparison with project references/specification when supplied;
- visual evidence of hardcoded drift or duplicate component styling.

## Iteration

Fix high-impact visible defects, re-render/reinspect when possible, and avoid endless polish loops. Prioritize task clarity, accessibility, responsive correctness and system consistency before decorative refinement.

Use `gorvet-quality-audit` when generic AI patterns or broader implementation quality need a final pass.
