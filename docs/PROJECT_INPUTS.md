# Project inputs

GORVET can consume project-specific material in the same way a coding agent consumes a software architecture or requirements document. These inputs are external to the installed skill package: the user may attach them in chat, expose them from the target repository, or provide them through whatever file/context mechanism the current agent runtime supports.

No fixed filename or template is required.

## Accepted evidence

Use any source the current runtime can actually inspect, including:

- Markdown or text requirements;
- DOCX/PDF briefs and architecture documents;
- repository documentation;
- screenshots and visual references;
- design-system/token exports;
- CSS variables, Sass maps, Tailwind configuration, Bootstrap variables or theme configuration;
- component-library documentation;
- existing production screens/components;
- brand guides, color specifications, typography rules and explicit do/don't rules.

Never claim to have read a source the runtime cannot access.

## Useful project-spec content

A project document may define any combination of:

- product, audience, tasks and workflows;
- scope and acceptance criteria;
- frontend/rendering/styling stack;
- component and icon libraries;
- colors, CSS variables, semantic tokens and theme values;
- typography, spacing, radius, border, elevation and layout rules;
- approved or deprecated components/patterns;
- responsive requirements;
- accessibility target and known audience needs;
- SEO requirements for public/indexable surfaces;
- reference images/screens and what should or should not be learned from them;
- mandatory technical/framework constraints.

GORVET should use what is supplied, not require every category.

## Authority levels

Not every input has equal authority.

### Normative
Explicit requirements that must be followed unless impossible, unsafe, inaccessible, or in conflict with a higher mandatory constraint.

Examples: approved brand colors, semantic token names, required component library, target WCAG level, supported platforms, forbidden dependencies.

### Existing source of truth
Current design system, semantic tokens, approved components, framework contracts and established production conventions.

### Reference / inspiration
Screenshots, competitor examples, moodboards and visual samples. Extract relevant properties such as density, hierarchy, rhythm, surface treatment, typography behavior and interaction patterns. Do not copy blindly.

### Heuristic
GORVET defaults used only when stronger evidence is absent.

## Conflict handling

When sources conflict:

1. identify the conflict;
2. determine authority and recency;
3. preserve mandatory technical and accessibility constraints;
4. follow explicit redesign requirements over legacy styling when clearly intended;
5. otherwise prefer the established semantic system;
6. surface unresolved material conflicts instead of silently choosing.

## Project-local design memory

When a long-running project benefits from persistent UI decisions, the agent may create or update a concise project-local file such as `DESIGN.md`, `UI-SYSTEM.md`, or an existing design-system document inside the target project repository.

That file is project data, not part of the GORVET installation. Do not create it merely because the pipeline ran; create it only when it prevents future rediscovery or inconsistency.
