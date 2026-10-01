# GORVET UI/UX Designer

A vendor-neutral collection of **Agent Skills** for planning, architecting, designing, implementing, and reviewing production UI/UX without falling into generic AI-generated interface patterns.

It is designed for agent runtimes that support the open `SKILL.md` Agent Skills format. The repository also includes a root `plugin.json` manifest so the same source tree can be packaged for ChatGPT-compatible plugin installation. Capabilities are detected at runtime and the skills degrade gracefully when browsing, rendering, screenshots, or repository tools are unavailable.

## Principles

- **Short pipeline, specialized expertise.** The orchestration stays practical; specialist skills load only when relevant.
- **Inspect before inventing.** Existing stack, tokens, components, product patterns, project documents, and references are sources of truth.
- **Architecture before decoration.** Infer regions, hierarchy, sequence, component model and responsive behavior from real tasks/content before styling.
- **Content and task before decoration.** Structure follows user goals and information relationships.
- **Reuse before custom code.** Existing component > existing pattern > framework primitive > framework utility > new reusable component > custom styling > hardcoded value.
- **Every visual device must earn its place.** Cards, borders, shadows, gradients, pills, icons, eyebrows, motion and oversized type need a functional, narrative or brand reason.
- **Avoid AI-style bundles.** Do not combine glass, gradients, giant radius, shadows, glows, pills, blobs and reveal motion merely to manufacture “modern/premium”.
- **Whitespace is valid.** Do not add decorative elements just because an area feels empty.
- **Accessibility is product quality.** A human-facing interface always gets an accessibility baseline; depth varies with complexity and risk.
- **SEO applies when discoverability matters.** Public/indexable pages get technical SEO analysis; private/admin surfaces do not receive meaningless SEO work.
- **Review is a gate.** Substantial new/redesigned UI is not complete until visual QA and the final quality audit have been applied using the strongest evidence available.
- **Adapters are optional.** Framework-specific skills can refine implementation, but GORVET works without them.

## Architecture

```text
                  GORVET UI/UX DESIGNER
                           │
                           ▼
                  gorvet-ui-pipeline
                           │
          ┌────────────────┴────────────────┐
          │                                 │
       CONTEXT                            DESIGN
          │                                 │
 Project Context                 UI Architecture & Structure
 - task/users                    - necessary regions/sections
 - surface/discoverability       - hierarchy + sequence
 - stack/system                  - component model + purpose
 - tokens/components             - states + responsive behavior
 - references                    - anti-AI preflight
          │                                 │
          │                  ┌──────────────┼──────────────┐
          │                  │              │              │
          │                 IA          Usability      Design System
          │                  │              │              │
          │               Research        Forms       Interaction
          │                  │              │              │
          │               UX Content   Accessibility      SEO
          │                                 │
          └────────────────┬────────────────┘
                           ▼
                         BUILD
                           │
                  UI Implementation
                           │
             detected/requested stack
       HTML/CSS/JS · Bootstrap · Tailwind · React · Vue · ...
                           │
                           ▼
                         REVIEW
                           │
                       Visual QA
                           │
                    Quality Audit Gate
                           │
                  fix material defects
                           │
                        DELIVER
```

The pipeline remains **Context → Design → Build → Review**. The internal specialist route changes according to the actual decision domains in the task; page types are not hardcoded templates.

See [docs/PIPELINE.md](docs/PIPELINE.md).

## Skills

| Skill | Purpose |
|---|---|
| `gorvet-ui-pipeline` | Orchestrates the shortest professional path while enforcing applicable quality gates. |
| `gorvet-project-context` | Reads project specs, references, stack, components, tokens, screenshots, constraints, and decomposes reference lessons. |
| `gorvet-information-architecture` | Navigation, hierarchy, taxonomy, search, filtering, labels, and wayfinding. |
| `gorvet-ux-usability` | Task flow, affordances, feedback, error prevention, cognitive load, and recovery. |
| `gorvet-ux-research-testing` | Lightweight discovery and usability testing when product decisions lack evidence. |
| `gorvet-ui-structure-design` | Interface architecture, section/component model, hierarchy, sequence, responsive transformation, visual direction, and anti-AI preflight. |
| `gorvet-design-system` | Tokens, primitives, components, variants, responsive contracts, and system consistency. |
| `gorvet-interaction-patterns` | Pattern selection and behavior for dialogs, drawers, tabs, tables, menus, disclosure, feedback, etc. |
| `gorvet-forms` | Forms, validation, data entry, onboarding, checkout, and error recovery. |
| `gorvet-ux-content` | Labels, actions, errors, empty states, onboarding, and interface microcopy. |
| `gorvet-accessibility` | Semantic HTML, keyboard, focus, screen readers, contrast, motion, zoom, and inclusive defaults. |
| `gorvet-frontend-seo` | Crawlability, metadata, canonicalization, structured data, internal linking, social metadata, performance, and indexable rendering. |
| `gorvet-ui-implementation` | Implements against the detected/requested stack while respecting existing systems and optional adapters. |
| `gorvet-visual-qa` | Rendered/static visual, responsive, state, accessibility smoke, reference comparison, and anti-template review. |
| `gorvet-quality-audit` | Final completion gate for AI-default accumulation, architecture, duplication, hardcoding, accessibility, SEO, and maintainability. |

## Anti-AI design control

GORVET does not ban individual styles. A card, gradient, pill, large heading, glass surface, eyebrow or animation may be correct when it has a real purpose.

The system instead detects **formulaic accumulation** and template-driven composition, for example:

- repeated `eyebrow → huge heading → subtitle → card grid` section anatomy;
- automatic SaaS hero + metrics + features + rounded CTA recipes;
- cards where spacing/grouping would be clearer;
- pills as decorative labels rather than semantic tags/states;
- reveal-on-scroll and hover-lift applied everywhere;
- “modern UI bundles” made from gradients + glass + large radius + shadows + glows + blobs;
- copying superficial motifs from a named reference instead of transferring structure, pacing, hierarchy or interaction principles.

Substantial designs get an anti-AI preflight before implementation and a repetition/accumulation check during final review.

## Project inputs

Project-specific specifications **do not live inside the installed GORVET package**. The user can attach or provide them in chat, expose them from the target repository, or supply them through the current runtime's file/context mechanism.

Accepted inputs can include Markdown/text requirements, DOCX/PDF briefs, screenshots, visual references, CSS variables, design tokens, Tailwind/Bootstrap configuration, existing components, brand guides, architecture documents and acceptance criteria.

No fixed filename or editable internal template is required.

See [docs/PROJECT_INPUTS.md](docs/PROJECT_INPUTS.md).

## Source-of-truth precedence

When sources disagree, resolve them in this order unless the project explicitly defines another policy:

1. current explicit user/task instructions;
2. normative project requirements/specification;
3. mandatory technical/framework contracts;
4. established project design system and semantic tokens;
5. representative shipped screens and components;
6. visual references marked as inspiration;
7. framework defaults;
8. GORVET general heuristics.

A redesign specification may intentionally override old visual conventions. Accessibility and mandatory technical constraints still apply.

## Optional framework adapters

GORVET does not require adapters. It can work directly with Bootstrap, Tailwind, Angular Material, shadcn, CSS/SCSS, CSS Modules, styled systems, server templates, plain HTML/CSS/JS, or other detected approaches.

An adapter is useful only when the project has conventions that generic frontend knowledge cannot reliably infer: repository layout, helper functions, template/meta systems, response contracts, proprietary components, routing conventions, or internal architecture.

See [docs/ADAPTERS.md](docs/ADAPTERS.md).

## Installation

This repository follows the open Agent Skills directory format. Install individual skill folders or the complete collection according to the capabilities of your agent runtime.

For ChatGPT-compatible plugin installation, the repository includes `plugin.json` at the root so the same repository/ZIP can act as the plugin source. Other runtimes can ignore that manifest and consume `skills/` directly.

## Validation

Run:

```bash
python scripts/validate_skills.py
```

The validator checks folder/name consistency, required YAML fields, naming constraints, description length, and local Markdown references.

## License

MIT. Use it, modify it, fork it, improve it, and redistribute it. Contributions are welcome.

## Attribution and references

GORVET UI/UX Designer is an original synthesis informed by established UI/UX practice, the open Agent Skills specification, WCAG/WAI guidance, Google Search Central/web.dev, and public MIT-licensed agent-skill projects including `hueyexe/frontend-agent-skills`. See [NOTICE.md](NOTICE.md).
