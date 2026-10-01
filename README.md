# GORVET UI/UX Designer

A vendor-neutral collection of **Agent Skills** for planning, designing, implementing, and reviewing production UI/UX without falling into generic AI-generated interface patterns.

It is designed for any agent runtime that supports the open `SKILL.md` Agent Skills format. It does **not** require Codex, Claude Code, Cursor, Gemini CLI, OpenCode, or any specific vendor. Capabilities are detected at runtime and the skills degrade gracefully when browsing, rendering, screenshots, or repository tools are unavailable.

## Principles

- **Short pipeline, specialized expertise.** The orchestration stays practical; specialist skills load only when relevant.
- **Inspect before inventing.** Existing stack, tokens, components, product patterns, project documents, and references are sources of truth.
- **Content and task before decoration.** Structure follows user goals and information relationships.
- **Reuse before custom code.** Existing component > existing pattern > framework primitive > framework utility > new reusable component > custom styling > hardcoded value.
- **Every visual device must earn its place.** Cards, borders, shadows, gradients, pills, icons, motion, and oversized type need a functional or brand reason.
- **Accessibility is product quality.** It is designed in, not bolted on after implementation.
- **SEO applies when discoverability matters.** Public/indexable pages get technical SEO attention; private/admin surfaces do not receive meaningless SEO work.
- **Adapters are optional.** Framework-specific skills can refine implementation, but GORVET works without them.

## The pipeline

The operational pipeline is intentionally short:

**Context → Design → Build → Review**

The orchestrator selects specialist skills inside those stages. A small change may use only Context → Build → Review. A new product surface may use IA, usability, design system, accessibility, SEO, forms, interaction, implementation, and QA as needed.

See [docs/PIPELINE.md](docs/PIPELINE.md).

## Skills

| Skill | Purpose |
|---|---|
| `gorvet-ui-pipeline` | Orchestrates the shortest professional path for the task. |
| `gorvet-project-context` | Reads project specs, references, stack, components, tokens, screenshots, and constraints. |
| `gorvet-information-architecture` | Navigation, hierarchy, taxonomy, search, filtering, labels, and wayfinding. |
| `gorvet-ux-usability` | Task flow, affordances, feedback, error prevention, cognitive load, and recovery. |
| `gorvet-ui-structure-design` | Greyboxing, hierarchy, composition, density, visual direction, anti-AI defaults. |
| `gorvet-design-system` | Tokens, primitives, components, variants, responsive contracts, and system consistency. |
| `gorvet-interaction-patterns` | Pattern selection and behavior for dialogs, drawers, tabs, tables, menus, disclosure, feedback, etc. |
| `gorvet-forms` | Forms, validation, data entry, onboarding, checkout, and error recovery. |
| `gorvet-ux-content` | Labels, actions, errors, empty states, onboarding, and interface microcopy. |
| `gorvet-accessibility` | Semantic HTML, keyboard, focus, screen readers, contrast, motion, zoom, and inclusive defaults. |
| `gorvet-frontend-seo` | Crawlability, metadata, canonicalization, structured data, internal linking, and indexable rendering. |
| `gorvet-ui-implementation` | Implements against the detected stack while respecting existing systems and optional adapters. |
| `gorvet-visual-qa` | Rendered visual, responsive, state, accessibility smoke, and reference comparison. |
| `gorvet-quality-audit` | Final cross-cutting review for AI defaults, duplication, hardcoding, accessibility, SEO, and maintainability. |

## Project specification input

GORVET can work from a project document in the same way a coding agent can work from a software architecture document. Provide any accessible source such as Markdown, text, DOCX, PDF, screenshots, exported design references, or images.

The optional [`PROJECT_UI_SPEC.md`](templates/PROJECT_UI_SPEC.md) template can describe:

- product, users, and core tasks;
- required visual direction and brand rules;
- colors, CSS variables, design tokens, Tailwind theme values, Bootstrap variables, typography;
- approved/rejected components and patterns;
- reference screenshots/images and what should be learned from them;
- responsive, accessibility, SEO, content, and performance constraints;
- implementation constraints and framework-specific requirements;
- explicit "do not" rules and acceptance criteria.

The document is not mandatory. If it does not exist, GORVET inspects the project and proceeds with the best available evidence.

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

A redesign specification may intentionally override an old design system. Do not preserve legacy inconsistency merely because it already exists.

## Optional framework adapters

GORVET does not require adapters. It can work directly with Bootstrap, Tailwind, Angular Material, shadcn, CSS/SCSS, CSS Modules, styled systems, or other detected approaches.

An adapter is useful only when the project has conventions that cannot be reliably inferred from generic frontend knowledge: repository layout, helper functions, template/meta systems, response contracts, proprietary components, routing conventions, or internal architecture.

See [docs/ADAPTERS.md](docs/ADAPTERS.md).

## Installation

This repository follows the open Agent Skills directory format. Install the individual skill folders in the skill location supported by your agent runtime, or install the complete collection if your client supports multi-skill repositories.

No runtime-specific files are required by the skills themselves.

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
