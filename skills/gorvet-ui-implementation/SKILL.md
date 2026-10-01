---
name: gorvet-ui-implementation
description: Implement approved UI/UX decisions in any detected frontend stack while preserving existing architecture, tokens, components, utilities, semantics, and optional framework-specific adapters. Use for production frontend coding after or during design decisions.
license: MIT
metadata:
  author: GORVET
---

# UI Implementation

Do not assume a framework. Inspect the project and implement in its existing system.

## Detect

Identify relevant rendering/frontend framework, styling approach, theme/tokens, component library, icons, state/data patterns, tests, and optional framework-specific skills.

Common technologies such as Bootstrap, Tailwind, Angular Material, shadcn, CSS/SCSS, React/Vue/Angular/Svelte, server templates, and plain HTML/CSS do **not** require an adapter. Work with them directly.

## Reuse hierarchy

Prefer:

1. existing project component;
2. existing project pattern;
3. existing semantic token;
4. framework/library component;
5. framework utility;
6. new reusable component/token when recurrence justifies it;
7. custom CSS/implementation;
8. hardcoded one-off values only as a justified last resort.

## Rules

- Do not introduce another UI framework for a local task.
- Do not hardcode colors/sizes/spacing that already have semantic tokens or utilities.
- Do not reimplement framework primitives unnecessarily.
- Do not create wrapper components that only rename an existing primitive without adding product meaning.
- Preserve native semantics and accessibility behavior.
- Keep responsive behavior explicit rather than accidental wrapping.
- Handle loading, empty, error, disabled, selected, overflow and long-content states relevant to the task.
- Keep custom CSS low-specificity and scoped to the right layer.

## Optional adapters

If a compatible framework/project skill exists, consult it for mandatory repository structure, helpers, metadata, rendering, assets, response contracts and proprietary components. Universal GORVET decisions govern UI/UX intent; the adapter governs technical contracts.

If no adapter exists, continue normally.
