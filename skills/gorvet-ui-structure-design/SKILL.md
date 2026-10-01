---
name: gorvet-ui-structure-design
description: Design interface hierarchy, greyboxing, composition, density, spacing, typography, surfaces, and visual direction from real content and user tasks. Use to create or critique visual UI while avoiding generic AI-generated composition.
license: MIT
metadata:
  author: GORVET
---

# UI Structure & Visual Design

Design in this order:

**content → relationships → hierarchy → grouping → interaction → layout → components → visual treatment**

## Structure first

Resolve reading/action order, primary versus secondary content, grouping, density, scanability, states, and responsive transformation before decoration.

Choose structures by semantics:

- table for row/column comparison;
- list for repeated vertically scanned items;
- card for a genuinely bounded object/task;
- panel/sidebar for persistent secondary context;
- disclosure for optional complexity;
- dashboard only when monitoring/metrics are truly the task.

## Visual direction

Derive typography, spacing, color, surfaces, depth and imagery from product, audience, brand, task frequency, data density, references and existing system. Do not apply a universal “premium SaaS” style.

## Intentionality rule

Before adding a container, border, shadow, radius, gradient, pill, icon, accent, oversized type or animation, ask whether it communicates hierarchy, grouping, affordance, state, sequence, emphasis, elevation, or brand character. If none apply, simplify.

Read `references/ai-default-patterns.md` during substantial design/review work.

## References

When visual references are supplied, extract characteristics such as hierarchy, rhythm, density, typographic contrast, surface logic, image treatment and navigation behavior. Do not blindly clone composition or ignore explicit project tokens.

## Handoff

Keep it implementation-ready:

```text
HIERARCHY
LAYOUT / GROUPING
COMPONENTS + PURPOSE
STATES
RESPONSIVE
VISUAL DIRECTION
```

Avoid arbitrary pixels when the project already has a token/utility system.
