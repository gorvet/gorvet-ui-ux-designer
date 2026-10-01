---
name: gorvet-interaction-patterns
description: Select and specify UI interaction patterns and component behavior, including dialogs, drawers, menus, tabs, disclosure, tables, lists, selection, commands, feedback, loading, and state transitions. Use when choosing how an interaction should work, not merely how it looks.
license: MIT
metadata:
  author: GORVET
---

# Interaction Patterns

Choose the simplest familiar pattern that fits the task.

## Pattern questions

Before selecting a pattern, determine:

- navigation or action?
- persistent or temporary context?
- blocking or non-blocking?
- single object or collection?
- reversible or destructive?
- frequent expert action or rare guided action?
- does the user need comparison, orientation, or focus?

## Defaults

- Use links for navigation and buttons for actions.
- Use inline editing when context matters and the change is small.
- Use a modal for focused blocking decisions/short tasks, not as a default detail page.
- Use drawers when temporary secondary context benefits from preserving the underlying page.
- Use tabs for stable peer views of the same object/context.
- Use accordions/disclosure for optional related detail, not to hide primary content.
- Use menus for compact secondary actions, not the primary action.
- Use tables when column alignment/comparison is meaningful; otherwise prefer lists.
- Keep loading, disabled, selected, empty, success and error states explicit.

## Interaction contract

For interactive patterns specify trigger, state, keyboard behavior, focus behavior, dismissal/cancel, success/error, responsive adaptation, and what happens to URL/history when navigation-like state changes.

Avoid custom controls when native/platform behavior already solves the problem.
