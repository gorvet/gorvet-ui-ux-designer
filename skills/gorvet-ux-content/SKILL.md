---
name: gorvet-ux-content
description: Write and review interface labels, buttons, headings, supporting copy, errors, empty states, success messages, onboarding, help text, notifications, and other UX microcopy. Use when wording, punctuation, hierarchy, trust, action, or recovery affect comprehension.
license: MIT
metadata:
  author: GORVET
---

# UX Content Design

Interface copy is part of interaction design.

## Principles

- Name things in the user's language, not internal implementation language.
- Buttons describe the action/outcome: `Save changes`, `Send invoice`, `Remove access`.
- Labels should remain understandable out of context where practical.
- Error messages explain what happened and how to recover.
- Empty states explain the state and the next useful action when one exists.
- Help text should add missing context, not restate the label.
- Warnings describe consequence before irreversible action.
- Success messages confirm what changed and what happens next.
- Avoid fake urgency, vague reassurance, and generic “Something went wrong” when a specific cause/remedy is known.

## Headings and punctuation

Treat headings and display copy differently from prose.

- Page/section/component headings (`h1`–`h6`) normally **do not end with a period**.
- Eyebrows, kickers, section indexes, labels and short display fragments do not use terminal periods by default.
- Question marks and exclamation marks are appropriate when they are semantically part of the heading. Colons, ellipses or other terminal punctuation require a deliberate editorial reason.
- Do not add a period merely because a heading is grammatically a complete sentence.
- A short supporting line that functions as display/subheading copy normally omits the final period when it is a single reinforcing statement.
- Supporting copy that functions as normal prose — especially multiple sentences or a developed paragraph — uses standard sentence punctuation.
- Do not infer punctuation from visual line count alone; line wrapping changes by viewport. Decide from the semantic role: display copy vs prose.

Follow an explicit project/editorial style guide when it defines another convention.

## Tone

Follow project voice/tone documents when supplied. Clarity and task completion outrank cleverness in operational UI.

## Scope discipline

Do not invent marketing claims, metrics, testimonials, or product capabilities to make the interface feel complete. Use realistic placeholders clearly marked as such only when prototyping requires them.
