# Project UI specification intake

A project specification is optional but powerful. Treat it as structured evidence, similar to a software architecture document.

## Accepted source types

Use any source the current agent runtime can actually read:

- Markdown/text;
- DOCX/PDF;
- repository documentation;
- screenshots and image references;
- exported design-system/token files;
- CSS variables, Sass maps, Tailwind config, theme configuration;
- component-library documentation.

Never pretend to have read a source the runtime cannot access.

## Reference authority

Not every input has equal authority.

### Normative
Explicit requirements that must be followed unless they conflict with a mandatory technical/accessibility constraint.

Examples: approved colors, logo clearspace, token names, required component library, target WCAG level, supported breakpoints, forbidden dependencies.

### Existing source of truth
Current design system, semantic tokens, approved components, production conventions.

### Reference / inspiration
Screenshots, competitor examples, moodboards, visual samples. Extract useful properties such as density, hierarchy, rhythm, surface treatment, typography behavior, and interaction patterns. Do not copy blindly.

## Conflict handling

When two sources conflict:

1. identify the conflict;
2. determine authority and recency;
3. preserve mandatory technical/accessibility constraints;
4. follow explicit redesign requirements over legacy styling when clearly intended;
5. otherwise prefer the established semantic system;
6. surface unresolved material conflicts instead of silently choosing.

## Persistent design memory

Create/update `DESIGN.md` only when the project will benefit from persistent decisions across sessions or agents. Keep it concise and operational.
