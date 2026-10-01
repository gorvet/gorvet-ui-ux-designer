---
name: gorvet-ui-structure-design
description: Architect interface structure and visual hierarchy from real content, tasks, relationships, actions, and constraints. Use to decide regions, sections, component patterns, sequence, density, responsive transformation, typographic hierarchy, and visual direction while actively avoiding generic AI-generated composition.
license: MIT
metadata:
  author: GORVET
---

# UI Architecture & Visual Structure

Design in this order:

**intent → content → relationships → hierarchy → grouping → sequence → component model → interaction → responsive transformation → visual treatment**

Do not start from a page-type template. Infer the structure from the task and available content.

## 1. Architecture before styling

Before choosing gradients, radius, cards, shadows, glass, pills, icons, oversized type, animation, or decorative imagery, resolve:

- what the interface must help the user understand or accomplish;
- what information/actions actually need to exist;
- which regions/sections are necessary and why;
- primary, secondary, supporting and contextual hierarchy;
- which items belong together and which need separation;
- sequence / reading / task order;
- the semantic pattern or component that best represents each relationship;
- relevant states and responsive transformations.

Every major region should have a product, content, navigation, task, or trust purpose. Do not add regions merely because a familiar UI template usually contains them.

Whitespace is a valid completed state. Do not add icons, badges, metrics, labels, cards, blobs, gradients, dividers, metadata or helper copy merely to make an area feel filled.

## 2. Choose structures by semantics

Examples:

- table for row/column comparison;
- list for repeated vertically scanned items;
- card for a genuinely bounded object, entity, choice or task;
- panel/sidebar for persistent secondary context;
- disclosure for optional complexity;
- timeline/sequence when order or progression is the information;
- editorial flow when narrative and pacing matter;
- dashboard only when monitoring/metrics are truly the task.

A visual container is not a default component. Use grouping, spacing and typography before adding a bordered/rounded surface when they communicate the relationship sufficiently.

## 3. Structure-only pass

The composition should still make sense if decorative effects are temporarily removed.

Before styling, mentally reduce the proposal to neutral type, spacing and simple boundaries. Verify that hierarchy, rhythm, grouping, sequence and actions remain clear. If the design only feels intentional after adding gradients, shadows, glass, pills, blobs or motion, revisit the architecture.

## 4. Typographic hierarchy

Typography is a hierarchy, not a collection of independent font sizes.

- Establish clear relationships among page/view title, section/region headings, component headings, supporting/subheading copy, body, labels and metadata.
- Size, weight, line-height, measure and spacing must work together; do not rely on font size alone to communicate hierarchy.
- Adjacent semantic levels should be visually distinguishable without creating arbitrary jumps.
- Do not make an `h1`, `h2` or display heading enormous merely to manufacture visual impact or a “premium” feeling.
- Display scale must be proportional to content importance, available space, density, surrounding elements and expected reading distance.
- A heading should not dominate a region so strongly that supporting content becomes cramped or illegible unless that scale is intentionally central to the composition.
- Do not shrink body/supporting text excessively to make headings appear more dramatic.
- Preserve coherent hierarchy across breakpoints; responsive typography should reduce extremes rather than simply clamp a giant desktop scale.
- Semantic heading level and visual size are related but not identical: preserve document semantics while styling according to the actual information hierarchy.

When reviewing an interface, compare the full scale as a system (`primary title → section/region title → component title → supporting copy → body → metadata`) rather than evaluating each size in isolation.

## 5. Section/region hierarchy and density

Every major section or functional region should have a clear internal hierarchy.

- Be able to identify what should attract attention first, second and third within that region.
- One dominant focal element is usually enough. Secondary modules must visibly recede unless simultaneous comparison is the actual task.
- Do not place several large/high-contrast elements side by side merely because they are all important. Sequence, group or subordinate them according to the information relationship.
- Avoid dense split compositions when both sides contain high-complexity content. Use simultaneous columns only when viewing both at once materially helps comprehension or task completion.
- Do not fill every column, edge or empty region. Breathing room is part of hierarchy, not unused capacity.
- Density should follow task/content needs. More information visible at once is not automatically more useful.
- Supporting elements such as metadata, tags, metrics, secondary actions, previews, diagrams or code examples should not compete with the region's main purpose.
- Background treatment must remain subordinate to foreground content. Decorative grids, dot matrices, glows, gradient fields, noise, blobs or technical line patterns are not default signals for “AI”, “developer”, “technical” or “modern”.
- If background decoration competes with text, controls, data or focal hierarchy, simplify or remove it.

Responsive layouts must preserve this hierarchy. A change of viewport may reorder or collapse content, but it should not create new competition between elements that were correctly prioritized at another size.

## 6. Anti-AI preflight

Read `references/ai-default-patterns.md` before finalizing substantial new visual structure.

Check for formulaic composition before implementation:

- repeated `eyebrow → large heading → subtitle → cards` anatomy across unrelated regions;
- cards used where plain content/grouping would be clearer;
- pill labels/buttons as automatic styling;
- giant type used as a substitute for hierarchy;
- generic SaaS/dashboard/component recipes applied without task justification;
- overloaded split compositions with equally dominant content on both sides;
- decorative completion: adding elements because whitespace feels unfinished;
- automatic reveal-on-scroll or hover-lift behavior without interaction/narrative purpose;
- a bundle of gradients + glass + large radius + shadows + glows used to manufacture “modern/premium”;
- decorative grid/dot/noise backgrounds used automatically to communicate technology or AI.

One device may be justified. The default bundle is not.

## 7. Motif discipline

Prefer a small, coherent visual vocabulary over many unrelated premium-UI effects.

Choose which devices carry the identity: for example typography + composition + motion, or color + geometry + imagery. Do not automatically add every available device. Repetition should create a system, not expose a template.

## 8. Reference decomposition

When a visual reference or brand example is supplied, decompose it before borrowing from it:

- structure;
- composition;
- pacing/rhythm;
- typography;
- density/whitespace;
- interaction;
- motion;
- surface treatment;
- brand-specific devices.

Extract transferable principles relevant to the task. Do not infer superficial motifs merely from a brand name. For example, “Apple-like” must not automatically mean giant type, glass, gradients, floating orbs or reveal animations.

## 9. Visual direction

Only after architecture is stable, derive typography, spacing, color, surfaces, depth, imagery and motion from product, audience, brand, task frequency, data density, references and the existing system.

Do not apply a universal “premium SaaS” style.

Before adding a container, border, shadow, radius, gradient, pill, icon, eyebrow, accent, oversized type, CTA panel, decorative background or animation, ask whether it communicates hierarchy, grouping, affordance, state, sequence, emphasis, elevation, continuity or brand character. If none apply, simplify.

## 10. Responsive architecture

Responsive design is not only wrapping columns. Decide what reorders, collapses, persists, becomes disclosure, changes density, or needs a different interaction at narrow/intermediate/wide sizes. Preserve each region's priority structure through those transformations.

## Handoff

Keep it implementation-ready and concise:

```text
INTENT
STRUCTURE / REGIONS
HIERARCHY + SEQUENCE
COMPONENT MODEL + PURPOSE
ACTIONS / INTERACTIONS
STATES
RESPONSIVE TRANSFORMATION
TYPOGRAPHIC HIERARCHY
REGION FOCAL + DENSITY PRIORITIES
VISUAL DIRECTION + MOTIFS
ANTI-AI RISKS TO AVOID
```

Avoid arbitrary pixels when the project already has a token/utility system.
