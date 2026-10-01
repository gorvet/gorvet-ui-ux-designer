---
name: gorvet-visual-qa
description: Perform visual and responsive QA on implemented interfaces using rendered pages, screenshots, or static code evidence. Use after UI implementation or when diagnosing an existing screen; verifies hierarchy, typography, density, spacing, states, references, responsiveness, accessibility smoke checks, and visible AI-template defects.
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
- whether each major section/functional region has a clear focal priority instead of several equally dominant modules;
- overloaded side-by-side compositions where dense content competes with another dense content/showcase/data/code/diagram block;
- supporting tags, metrics, secondary actions, previews or metadata competing with the region's main purpose;
- typography hierarchy, content measure and readable line-height;
- proportional relationships across page/view title, section/region headings, component headings, supporting copy, body and metadata;
- oversized display type that consumes disproportionate space or creates an artificial hierarchy gap;
- heading/supporting-copy punctuation that conflicts with their editorial role;
- surface/border/shadow/radius consistency;
- decorative background grids, dots, noise, glows or gradients that compete with content or act as automatic “tech/AI” styling;
- section/component silhouette repetition that exposes a generic template;
- unnecessary decorative completion: icons, pills, badges, metrics, cards, blobs, gradients or dividers that do not add meaning;
- long content, overflow and truncation;
- empty/loading/error/disabled/selected/success states where relevant;
- mobile/narrow, intermediate and wide behavior relevant to the product;
- whether responsive transformations preserve the hierarchy of each region;
- keyboard focus visibility and obvious accessibility regressions;
- suspicious ARIA on generic containers, redundant accessible names, or live regions tied to decorative/passive changes;
- comparison with project references/specification when supplied;
- whether reference principles were transferred rather than superficial brand motifs copied;
- visual evidence of hardcoded drift or duplicate component styling.

## Typography pass

Read the type system as a scale, not as isolated sizes. Confirm that semantic levels are distinguishable without exaggerated jumps, that body/supporting text has not been shrunk merely to make headings feel larger, and that responsive sizes remain proportionate.

Headings normally should not end in periods unless the project style guide or message intentionally requires punctuation. Treat short display subcopy differently from prose paragraphs.

## Region hierarchy and focal-load pass

For each major section or functional region, identify the intended first, second and third attention targets. If several large/high-contrast elements demand equal attention simultaneously, simplify, sequence, group or subordinate them.

Do not assume every visible area must be filled. Whitespace is not a defect and should not trigger another module, label, metric, illustration or background effect.

A region may contain many elements when the task requires density, but the user should still be able to distinguish primary content/action from supporting/contextual material.

## Anti-template visual pass

Temporarily ignore the copy and compare the silhouettes of major regions. If many unrelated regions collapse to the same anatomy (for example eyebrow + giant heading + lede + card grid, or rounded CTA band), treat that as a design defect unless the repeated semantics justify it.

Also inspect whether “modernity” is being manufactured by stacking effects such as glass + gradient + grid + large radius + shadow + glow + reveal motion. Prefer a smaller coherent motif set.

## Iteration

Fix high-impact visible defects, re-render/reinspect when possible, and avoid endless polish loops. Prioritize task/content clarity, accessibility, responsive correctness, architecture and system consistency before decorative refinement.

Use `gorvet-quality-audit` as the final completion gate for substantial new/redesigned UI.

Pass actual evidence and observations to the audit: region/state, viewport or static scope, observed hierarchy/repetition, defects corrected and re-check result. Capture alone is not a visual inspection; state the findings from the image or rendered interface. Keep functional results separate from composition findings. If only static evidence exists, explicitly leave rendered appearance unverified rather than describing the design as visually passed.
