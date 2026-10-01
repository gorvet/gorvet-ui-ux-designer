---
name: gorvet-ui-structure-design
description: Architect interface structure and visual hierarchy from real content, tasks, relationships, actions, and constraints. Use to decide regions, sections, component patterns, sequence, density, responsive transformation, and visual direction while actively avoiding generic AI-generated composition.
license: MIT
metadata:
  author: GORVET
---

# UI Architecture & Visual Structure

Design in this order:

**intent → content → relationships → hierarchy → grouping → sequence → component model → interaction → responsive transformation → visual treatment**

Do not start from a page-type template. Infer the structure from the task and available content.

## Architecture before styling

Before choosing gradients, radius, cards, shadows, glass, pills, icons, oversized type, animation, or decorative imagery, resolve:

- what the interface must help the user understand or accomplish;
- what information/actions actually need to exist;
- which regions/sections are necessary and why;
- primary, secondary, supporting and contextual hierarchy;
- which items belong together and which need separation;
- sequence / reading / task order;
- the semantic pattern or component that best represents each relationship;
- relevant states and responsive transformations.

Every major region should have a product, content, navigation, task, or trust purpose. Do not add sections merely because a familiar landing/dashboard template usually contains them.

Whitespace is a valid completed state. Do not add icons, badges, metrics, labels, cards, blobs, gradients, dividers, metadata or helper copy merely to make an area feel filled.

## Choose structures by semantics

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

## Structure-only pass

The composition should still make sense if decorative effects are temporarily removed.

Before styling, mentally reduce the proposal to neutral type, spacing and simple boundaries. Verify that hierarchy, rhythm, grouping, sequence and actions remain clear. If the design only feels intentional after adding gradients, shadows, glass, pills, blobs or motion, revisit the architecture.

## Anti-AI preflight

Read `references/ai-default-patterns.md` before finalizing substantial new visual structure.

Check for formulaic composition before implementation:

- repeated `eyebrow → large heading → subtitle → cards` section anatomy;
- cards used where plain content/grouping would be clearer;
- pill labels/buttons as automatic styling;
- giant type used as a substitute for hierarchy;
- generic SaaS hero/metrics/feature-grid/CTA recipes;
- decorative completion: adding elements because whitespace feels unfinished;
- automatic reveal-on-scroll or hover-lift behavior without interaction/narrative purpose;
- a bundle of gradients + glass + large radius + shadows + glows used to manufacture “modern/premium”.

One device may be justified. The default bundle is not.

## Motif discipline

Prefer a small, coherent visual vocabulary over many unrelated premium-UI effects.

Choose which devices carry the identity: for example typography + composition + motion, or color + geometry + imagery. Do not automatically add every available device. Repetition should create a system, not expose a template.

## Reference decomposition

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

## Visual direction

Only after architecture is stable, derive typography, spacing, color, surfaces, depth, imagery and motion from product, audience, brand, task frequency, data density, references and the existing system.

Do not apply a universal “premium SaaS” style.

Before adding a container, border, shadow, radius, gradient, pill, icon, eyebrow, accent, oversized type, CTA panel or animation, ask whether it communicates hierarchy, grouping, affordance, state, sequence, emphasis, elevation, continuity or brand character. If none apply, simplify.

## Responsive architecture

Responsive design is not only wrapping columns. Decide what reorders, collapses, persists, becomes disclosure, changes density, or needs a different interaction at narrow/intermediate/wide sizes.

## Handoff

Keep it implementation-ready and concise:

```text
INTENT
STRUCTURE / SECTION MAP
HIERARCHY + SEQUENCE
COMPONENT MODEL + PURPOSE
ACTIONS / INTERACTIONS
STATES
RESPONSIVE TRANSFORMATION
VISUAL DIRECTION + MOTIFS
ANTI-AI RISKS TO AVOID
```

Avoid arbitrary pixels when the project already has a token/utility system.
