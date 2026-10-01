---
name: gorvet-project-context
description: Inspect and resolve UI/UX project context before design or implementation. Use when requirements, project documents, screenshots, reference images, design tokens, stack, component libraries, or existing interfaces must be understood and reconciled.
license: MIT
metadata:
  author: GORVET
---

# Project Context & UI Audit

Inspect first. Ask only when missing information materially changes the solution.

## Inputs

Use any accessible evidence:

- current user instructions;
- project UI specification or software architecture/requirements document;
- repository code and configuration;
- CSS variables, theme files, Tailwind/Bootstrap/custom token systems;
- existing components and representative screens;
- screenshots, images, moodboards, design references;
- optional framework-specific skills/adapters.

Never claim to have inspected a file, image, browser state, or code path that is not accessible in the current runtime.

## Resolve authority

Default precedence:

1. current explicit task instructions;
2. normative project specification;
3. mandatory technical/framework contracts;
4. established semantic design system/tokens;
5. representative shipped screens/components;
6. inspiration/reference images;
7. framework defaults;
8. generic GORVET heuristics.

A clearly stated redesign requirement can override legacy visual conventions. Accessibility and mandatory technical constraints still apply.

## Inspect

Determine only what is relevant:

- product, audience, primary tasks, density and device context;
- new vs existing surface;
- public/indexable vs private/non-indexable when relevant;
- rendering/frontend framework and styling system;
- component library and icon system;
- typography, colors, spacing, radius, elevation, breakpoints/containers;
- existing navigation, forms, tables/lists, feedback and state patterns;
- existing hardcoding, duplication, drift or accessibility debt;
- references: what the user wants to learn from them and what should remain project-specific.

Do not treat a screenshot as a specification unless it is marked normative.

## Reference decomposition

Do not translate a named reference or screenshot directly into superficial visual motifs.

When references materially influence design, identify the relevant lessons across:

- structure and information emphasis;
- composition and hierarchy;
- pacing/rhythm/whitespace;
- typography behavior;
- density;
- interaction and navigation;
- motion/transition logic;
- surface treatment;
- brand-specific devices that should **not** be copied automatically.

For example, a request for an “Apple-like” experience may justify narrative pacing, focus, confident whitespace and restrained motion; it does not automatically justify glass, giant headings, gradients, floating spheres or reveal animations.

## Output

Keep the resolved context concise:

```text
TASK / USERS
SURFACE / DISCOVERABILITY
SOURCES OF TRUTH
STACK / SYSTEM
REUSE
REFERENCE LESSONS / NON-TRANSFERABLE MOTIFS
CONSTRAINTS
RISKS / MATERIAL CONFLICTS
```

Create/update project-local design documentation only when persistent project-wide memory is useful. Do not require the user to edit files inside the installed GORVET package.
