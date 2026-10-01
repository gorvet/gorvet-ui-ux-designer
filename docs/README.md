# GORVET UI/UX Designer — Documentation

This directory documents the GORVET UI/UX Designer system itself. Users do not need to edit files inside `docs/` for normal use.

## Documents

- [`PIPELINE.md`](PIPELINE.md) — detailed behavior of the adaptive Context → Design → Build → Review pipeline and routing examples.
- [`PROJECT_INPUTS.md`](PROJECT_INPUTS.md) — how GORVET consumes external project requirements, software architecture documents, colors/tokens, screenshots, visual references, and other evidence supplied in chat or stored in the target project.
- [`ADAPTERS.md`](ADAPTERS.md) — contract for optional framework/project-specific skills such as GFrame adapters.

## Where project-specific documentation belongs

Project-specific briefs, architecture documents, design specifications, screenshots, references, or persistent design memory belong to the project being developed or may simply be attached/provided in the conversation. They do not belong inside the installed GORVET skill package.

GORVET must work even when no project specification is provided by inspecting the available code, design system, components, tokens, and existing UI.
