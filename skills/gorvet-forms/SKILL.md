---
name: gorvet-forms
description: Design, critique, and implement forms, inputs, validation, onboarding, registration, checkout, settings, and data-entry flows. Use when users must enter, review, correct, or submit structured information.
license: MIT
metadata:
  author: GORVET
---

# Forms & Data Entry

Treat every field as effort and an opportunity for error.

## Decision order

**remove → infer → default → defer → ask → explain → validate → recover**

## Structure

- Group by user topic, not database schema.
- Use visible persistent labels; placeholder text is only supplementary.
- Use native controls when they match the question.
- Show short option sets directly; do not hide them in selects without reason.
- Use single-page forms for short coherent tasks; split only when length, branching, mobile focus or comprehension justify it.
- Avoid arbitrary multi-column forms that harm reading/tab order.

## Validation

- Prevent errors where possible.
- Do not scold users while they are still typing normal input.
- Validate at a humane time; after an error exists, give immediate helpful feedback during correction when useful.
- Explain problem + location + remedy.
- Long forms with multiple failures need an error summary plus field-level errors.
- Submission must communicate progress and prevent duplicates.

## Checkout/onboarding

Minimize distractions and unnecessary account/profile collection. Expose costs/consequences before commitment. Progress indicators must reflect a stable understandable sequence.

## Accessibility

Persistent labels, semantic grouping, keyboard order, focus after errors, programmatic invalid/help relationships, appropriate autocomplete/inputmode, and non-color error cues are part of the form contract.
