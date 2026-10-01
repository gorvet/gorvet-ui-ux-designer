---
name: gorvet-ui-implementation
description: Implement approved UI/UX decisions in any requested or detected frontend stack while preserving existing architecture, tokens, components, utilities, semantics, and optional framework-specific adapters. Use for production frontend coding in new frontends or existing projects.
license: MIT
metadata:
  author: GORVET
---

# UI Implementation

Support both existing projects and new frontends. Do not invent a framework when the user already requested a stack or when plain HTML/CSS/JS is sufficient.

## Mode A — Existing project

Inspect the relevant project before editing. Identify rendering/frontend framework, styling approach, theme/tokens, component library, icons, state/data patterns, tests, and optional framework-specific skills.

Preserve the established architecture unless the task explicitly requires a redesign/migration.

## Mode B — New frontend

When no existing project/system exists:

1. use the user's requested stack if one is specified;
2. otherwise choose the smallest appropriate implementation approach for the task;
3. establish only the minimal reusable foundations needed by the design (for example semantic variables/tokens, container/rhythm rules, and a few repeated components);
4. do not fabricate a large design system, dependency stack, build pipeline, or component abstraction for a one-page result;
5. keep the output runnable and easy to adopt.

Examples: a requested HTML + Bootstrap + JS landing should remain HTML + Bootstrap + JS; a plain static page does not need React merely because the runtime can generate it.

For substantial new/redesigned UI, require the architecture decision handoff and `PASS` preflight from `gorvet-ui-structure-design` before implementation. If they are missing, resolve that design work first; loading the skill or receiving brand names does not satisfy the gate. If implementation changes the approved composition materially, re-check the affected design decisions before continuing.

Common technologies such as Bootstrap, Tailwind, Angular Material, shadcn, CSS/SCSS, React/Vue/Angular/Svelte, server templates, and plain HTML/CSS/JS do **not** require an adapter. Work with them directly.

## Reuse hierarchy

For existing projects prefer:

1. existing project component;
2. existing project pattern;
3. existing semantic token;
4. framework/library component;
5. framework utility;
6. new reusable component/token when recurrence justifies it;
7. custom CSS/implementation;
8. hardcoded one-off values only as a justified last resort.

For new frontends, the same principle becomes: requested stack/framework primitive → minimal semantic foundation → reusable pattern where recurrence justifies it → custom one-off only when appropriate.

## Rules

- Do not introduce another UI framework for a local task.
- Do not hardcode colors/sizes/spacing that already have semantic tokens or utilities.
- Do not reimplement framework primitives unnecessarily.
- Do not create wrapper components that only rename an existing primitive without adding product meaning.
- Preserve native semantics and accessibility behavior.
- Keep responsive behavior explicit rather than accidental wrapping.
- Handle loading, empty, error, disabled, selected, overflow and long-content states when relevant to the interface.
- Keep custom CSS low-specificity and scoped to the right layer.
- Implement the approved architecture; do not replace it with a familiar template during coding.
- Do not add decorative effects, sections, cards, metrics, icons, badges or animation merely to make the implementation feel more complete.

## Optional adapters

If a compatible framework/project skill exists, consult it for mandatory repository structure, helpers, metadata, rendering, assets, response contracts and proprietary components. Universal GORVET decisions govern UI/UX intent; the adapter governs technical contracts.

If no adapter exists, continue normally.
