---
name: gorvet-design-system
description: Create, audit, extend, or map design systems across frontend and editable design tools, preserving semantic tokens, components, variants, states, and responsive contracts. Use when consistency and reuse span more than one isolated screen or when transferring a system between destinations.
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

## Destination mapping

Inspect the authoritative system and the destination's existing library before creating anything. For the slice actually used, contribute a compact source → destination mapping to the [pipeline design contract](../gorvet-ui-pipeline/SKILL.md#design-contract): semantic token/component identity, existing destination reference, relevant variant/state or mode, and any capability gap. A short note or existing library references suffice; do not inventory the whole system.

Preserve semantic meaning, aliases, themes/modes and variant/state relationships using the destination's supported mechanisms (for example variables/styles and component instances in an editable tool, or tokens and component props in code). Reuse and bind existing resources before creating equivalents. Different names may map to the same meaning; identical names alone do not prove equivalence. Do not detach instances, flatten variants or duplicate tokens merely to simplify construction.

If no equivalent exists, define only the missing reusable slice and retain its source relationship. If a required binding/state cannot be represented, record the fallback and its limit for Design to resolve and Review to verify; do not claim unsupported fidelity. The destination's mandatory technical contracts determine how resources are created and bound. A local label/content change using established resources needs no mapping artifact.

## CSS/frontend architecture

- low specificity and component-local responsibility;
- semantic HTML first;
- existing utilities/tokens before custom declarations;
- avoid deep location-dependent selectors;
- avoid dependencies for trivial presentational needs;
- component/container responsive behavior when appropriate.

## Scope

For a new product, establish the smallest useful system slice rather than an exhaustive library. For an existing product, extend the current system unless the project explicitly calls for redesign/migration.
