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
- public/indexable vs private/admin surface;
- rendering/frontend framework and styling system;
- component library and icon system;
- typography, colors, spacing, radius, elevation, breakpoints/containers;
- existing navigation, forms, tables/lists, feedback and state patterns;
- existing hardcoding, duplication, drift or accessibility debt;
- reference-image lessons: hierarchy, rhythm, density, layout, typography, surfaces, interaction.

Do not treat a screenshot as a specification unless it is marked normative.

## Output

Keep the resolved context concise:

```text
TASK / USERS
SOURCES OF TRUTH
STACK / SYSTEM
REUSE
REFERENCES
CONSTRAINTS
RISKS / MATERIAL CONFLICTS
```

Create/update `DESIGN.md` only when persistent project-wide memory is useful.
