# AI-default warning signals

These are **signals to inspect**, not universal bans. A pattern is acceptable when it is justified by task, content, brand, state, or hierarchy. The main failure mode is formulaic repetition: the same presentational recipe is applied to unrelated content because it is an easy default rather than because the interface needs it.

## Structure
- everything wrapped in cards;
- cards nested inside cards;
- every section/region treated with identical visual weight;
- automatic three-column grids;
- dashboard/KPI widgets where no monitoring task exists;
- promotional hero treatment inside operational interfaces without a product reason;
- excessive centered composition or artificial symmetry;
- floating containers without structural purpose;
- repeating the same region anatomy everywhere, especially `eyebrow → large heading → subtitle/paragraph → content`;
- treating every important action as a separate promotional panel/card instead of integrating it naturally into the information flow;
- oversized callout blocks used as a default separator or ending;
- repeatedly separating content into visually isolated blocks when whitespace and hierarchy would be enough;
- dense split compositions that place high-complexity content beside another equally dominant content/data/code/diagram block without a simultaneous-viewing need.

## Density and focal hierarchy
- several large/high-contrast elements competing inside the same section or functional region;
- no clear first, second and third attention targets within a major region;
- filling every column, edge or empty area because whitespace is treated as wasted space;
- multiple high-complexity modules placed side by side with no dominant focal area;
- supporting metrics, tags, metadata, secondary actions, previews or diagrams competing with the region's main purpose;
- content density chosen for visual abundance rather than task/content needs;
- responsive layouts that preserve all desktop competition instead of re-prioritizing and simplifying.

## Surfaces and decoration
- the same large radius everywhere;
- oversized rounded rectangles around ordinary content or actions;
- shadows on every surface;
- borders around every conceptual group;
- glassmorphism without layer logic;
- gradient blobs or gradient text used as automatic personality;
- glow used as filler;
- pills used for ordinary labels/actions without semantic reason;
- colored/tinted backgrounds added mainly to create visual variety rather than communicate grouping or state;
- grid, dot-matrix, noise, technical-line or blueprint-style backgrounds used automatically to signal “AI”, “developer”, “technical” or “modern”;
- multiple background effects (gradient + grid + glow + noise) competing with the actual content.

## Content and framing
- invented metrics, testimonials, activity, or metadata;
- decorative badges and icons added to fill space;
- generic eyebrow labels and SaaS marketing copy;
- an eyebrow above nearly every heading, regardless of whether a secondary label adds information;
- repeatedly using the same `eyebrow + title + subtitle` hierarchy for regions with different semantic roles;
- generic uppercase micro-labels such as “WHY US”, “OUR PROCESS”, “KEY FEATURES”, or “PIPELINE” when the main heading already provides the context;
- helper text that repeats what the control or heading already communicates;
- redundant intro copy whose only purpose is to fill a canonical header pattern.

## Typography
- huge headings that reduce useful density or dominate a region without narrative/task reason;
- exaggerated jumps between display headings and body/supporting text;
- shrinking supporting/body text to make headings appear more dramatic;
- all-caps/tracked labels everywhere;
- treating small uppercase brand-colored eyebrows as a mandatory visual signature;
- monospace metadata without a product reason;
- one highlighted/gradient/italic headline word as a default motif;
- the same generic type treatment regardless of product context;
- headings/titles ending in periods by default rather than following editorial role.

## Calls to action
- every CTA/action placed inside a rounded card with generous padding and a contrasting/tinted background;
- large rounded CTA containers that visually overpower the action itself;
- repeating `headline + supporting copy + primary button + secondary button` as a universal action formula;
- adding a secondary CTA only to create visual balance rather than because users need a second path;
- turning simple navigation/action links into promotional blocks without a product reason.

## Interaction
- modal for every detail/edit flow;
- `hover: scale(...)` or hover-lift on every card;
- reveal-on-scroll attached to nearly every region merely to make the interface feel dynamic;
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
When reviewing an interface, ignore the copy and compare the silhouettes of major sections/regions. If unrelated regions reduce to the same header stack, rounded container, card grid, split composition, or action treatment, the layout is probably being driven by a template rather than by content semantics.

Vary structure only when the content relationship changes; do not vary it merely for novelty. Conversely, do not force unrelated content into the same composition merely for visual consistency.

## Focal-load test
For each major section or functional region, identify the intended first, second and third attention targets. If several large/high-contrast elements demand equal attention simultaneously, simplify, sequence, group or subordinate them.

Responsive behavior should preserve that priority, not merely keep all elements visible.

## Accumulation rule
One signal does not make an interface generic. Multiple unrelated defaults appearing together without product justification indicate design convergence and should trigger revision.
