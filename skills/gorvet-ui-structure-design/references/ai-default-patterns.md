# AI-default warning signals

These are **signals to inspect**, not universal bans. A pattern is acceptable when it is justified by task, content, brand, state, or hierarchy. The main failure mode is formulaic repetition: the same presentational recipe is applied to unrelated content because it is an easy default rather than because the interface needs it.

## Structure
- everything wrapped in cards;
- cards nested inside cards;
- every section treated with identical visual weight;
- automatic three-column feature grids;
- dashboard/KPI widgets where no monitoring task exists;
- hero sections inside operational tools;
- excessive centered composition or artificial symmetry;
- floating containers without structural purpose;
- repeating the same section anatomy everywhere, especially `eyebrow → large heading → subtitle/paragraph → content`;
- treating every important CTA as a separate promotional panel/card instead of integrating it naturally into the information flow;
- oversized CTA bands or callout boxes used as a default ending for sections/pages;
- repeatedly separating content into visually isolated blocks when whitespace and hierarchy would be enough;
- overloaded split heroes that place a dense text stack beside an equally dense showcase/code/diagram card without a real comparison need;
- forcing every important message, CTA, metric, tag and visual into the first viewport.

## Density and viewport
- first-screen compositions where headline, paragraph, CTAs, chips, metrics and a showcase panel all compete for attention;
- heroes that feel clipped or overcrowded at common laptop heights;
- filling every horizontal column or empty region because whitespace is treated as wasted space;
- multiple high-complexity modules placed side by side with no dominant focal area;
- content density chosen for visual abundance rather than task/content needs;
- layouts tuned only for very wide/tall mockup canvases instead of realistic viewport ranges.

## Surfaces and decoration
- the same large radius everywhere;
- oversized rounded rectangles around ordinary content or CTAs;
- shadows on every surface;
- borders around every conceptual group;
- glassmorphism without layer logic;
- gradient blobs or gradient text used as automatic personality;
- glow used as filler;
- pills used for ordinary labels/actions without semantic reason;
- colored/tinted section backgrounds added mainly to create visual variety rather than communicate grouping or state;
- grid, dot-matrix, noise, technical-line or blueprint-style backgrounds used automatically to signal “AI”, “developer” or “modern”;
- multiple background effects (gradient + grid + glow + noise) competing with the actual content.

## Content and section framing
- invented metrics, testimonials, activity, or metadata;
- decorative badges and icons added to fill space;
- generic eyebrow labels and SaaS marketing copy;
- an eyebrow above nearly every heading, regardless of whether a secondary label adds information;
- repeatedly using the same `eyebrow + title + subtitle` hierarchy for sections with different semantic roles;
- generic uppercase micro-labels such as “WHY US”, “OUR PROCESS”, “KEY FEATURES”, or “PIPELINE” when the main heading already provides the context;
- helper text that repeats what the control or heading already communicates;
- redundant intro copy whose only purpose is to fill the canonical section-header pattern.

## Typography
- huge headings that reduce task density or dominate most of the viewport without narrative reason;
- exaggerated jumps between display headings and body/supporting text;
- shrinking supporting/body text to make headings appear more dramatic;
- all-caps/tracked labels everywhere;
- treating small uppercase brand-colored eyebrows as a mandatory visual signature across the whole page;
- monospace metadata without a product reason;
- one highlighted/gradient/italic headline word as a default motif;
- the same generic type treatment regardless of product context.

## Calls to action
- every CTA placed inside a rounded card with generous padding and a contrasting/tinted background;
- large rounded CTA containers that visually overpower the action itself;
- repeating `headline + supporting copy + primary button + secondary button` as a universal CTA formula;
- adding a secondary CTA only to create visual balance rather than because users need a second path;
- turning simple navigation/action links into promotional blocks without a product reason.

## Interaction
- modal for every detail/edit flow;
- `hover: scale(...)` or hover-lift on every card;
- reveal-on-scroll attached to nearly every section merely to make the page feel dynamic;
- decorative micro-animation without feedback, continuity or narrative value;
- hiding common actions inside menus merely to look clean.

## Implementation
- hardcoded colors despite tokens;
- arbitrary spacing values despite utilities/scales;
- duplicate components instead of variants/reuse;
- custom controls replacing native semantics without need;
- custom CSS that duplicates framework utilities;
- introducing another UI framework for one screen.

## Repetition test
When reviewing a page, ignore the copy and compare section silhouettes. If many sections reduce to the same header stack, same rounded container, same card grid, and same CTA treatment, the layout is probably being driven by a template rather than by content semantics.

Vary structure only when the content relationship changes; do not vary it merely for novelty. Conversely, do not force unrelated content into the same composition merely for visual consistency.

## Focal-load test
At each major viewport, identify the intended first, second and third attention targets. If several large/high-contrast elements demand equal attention simultaneously, simplify, sequence or reduce one of them.

The first viewport does not need to contain the whole argument. Prioritize comprehension over visual abundance.

## Accumulation rule
One signal does not make an interface generic. Multiple unrelated defaults appearing together without product justification indicate design convergence and should trigger revision.
