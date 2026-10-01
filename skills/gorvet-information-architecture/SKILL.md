---
name: gorvet-information-architecture
description: Organize navigation, hierarchy, taxonomy, labels, search, filtering, metadata, URLs, content grouping, and wayfinding. Use when users must find, browse, compare, filter, or understand structured information.
license: MIT
metadata:
  author: GORVET
---

# Information Architecture

Design for finding **and** understanding.

## Decision order

1. user task and likely entry point;
2. content objects, states, relationships and scale;
3. organization scheme;
4. hierarchy and labels;
5. navigation/wayfinding;
6. search/filter/sort when justified;
7. URL/state persistence for web products;
8. responsive and accessible behavior.

## Rules

- Prefer user vocabulary over internal org language.
- Use one dominant organizing principle per view when possible.
- Use hierarchy for stable parent/child structures; facets for independent attributes; search when users often know what they want.
- Tabs represent peer views of the same context, not unrelated destinations.
- Filters narrow a set; they are not a substitute for primary navigation.
- Breadcrumbs communicate location, not click history.
- Every deep-entry screen should answer: where am I, what is here, where can I go, what changed?
- Preserve useful search/filter/sort/pagination state in URLs when shareability/restoration matters and privacy allows it.
- Do not add search to compensate for bad labels or grouping.

## Handoff

Specify navigation model, labels, grouping, search/filter rules, state/URL behavior, and relevant responsive/accessibility requirements. Avoid decorative layout decisions unless they affect comprehension.
