---
name: gorvet-design-system
description: Create, audit, or extend frontend design systems with semantic tokens, primitives, components, variants, responsive contracts, states, and maintainable CSS/component architecture. Use when consistency and reuse span more than one isolated screen.
license: MIT
metadata:
  author: GORVET
---

# Design System Engineering

Design systems are reusable decisions, not a component inventory for its own sake.

## Layer model

**foundations/tokens → primitives → components → compositions/templates → product examples**

## Audit before adding

Inspect existing semantic tokens, components, variants, duplicated patterns, raw values, and style drift. Normalize before expanding when practical.

## Tokens

Prefer semantic meaning over appearance:

- `text.muted`, `surface.raised`, `border.focus`, `action.primary.bg`
- not `gray500-label`, `blue-button`, or one-off raw values.

Use the project's existing token format. Do not create a parallel token system because another format is fashionable.

## Components

A reusable component needs:

- purpose and “use/do not use” boundary;
- anatomy/content contract;
- meaningful variants only;
- interactive and async states;
- accessibility contract;
- responsive behavior;
- implementation guidance and realistic examples.

Prefer fewer well-defined variants over near-duplicates.

## CSS/frontend architecture

- low specificity and component-local responsibility;
- semantic HTML first;
- existing utilities/tokens before custom declarations;
- avoid deep location-dependent selectors;
- avoid dependencies for trivial presentational needs;
- component/container responsive behavior when appropriate.

## Scope

For a new product, establish the smallest useful system slice rather than an exhaustive library. For an existing product, extend the current system unless the project explicitly calls for redesign/migration.
