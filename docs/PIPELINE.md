# GORVET pipeline

The pipeline is deliberately small. Specialist skills are capabilities, not mandatory ceremonies, but applicable quality domains must not be skipped merely to shorten the path.

## 1. Context

Use `gorvet-project-context` to resolve what is being built, for whom, with what constraints, and on top of what existing system.

Inputs may include project documents, requirements, architecture documents, code, screenshots, references, existing components, design tokens, and the live/rendered product.

Resolve enough context to route correctly: new vs existing surface, human-facing intent, public/indexable vs private where relevant, stack/system, reusable assets, reference lessons and material constraints.

Output is concise resolved context, not a report unless persistence is useful.

## 2. Design

For substantial new/redesigned UI, begin with `gorvet-ui-structure-design` as the interface architect. It determines the necessary structure, hierarchy, sequence, component model, actions, states and responsive transformation from the real task/content **before** visual decoration.

Then select only the other specialists needed:

- `gorvet-information-architecture`
- `gorvet-ux-usability`
- `gorvet-ux-research-testing` when material product/user uncertainty requires evidence
- `gorvet-design-system`
- `gorvet-interaction-patterns`
- `gorvet-forms`
- `gorvet-ux-content`
- `gorvet-accessibility`
- `gorvet-frontend-seo` for public/indexable surfaces

The design stage resolves decisions before code. It does not require lengthy paperwork.

### Anti-AI preflight

Before implementation, substantial new visual structure must pass the preflight in `gorvet-ui-structure-design`:

- structure still works without decorative effects;
- sections/components are derived from content/tasks, not a generic page template;
- repeated eyebrow/header/card/CTA silhouettes are justified semantically;
- cards, pills, gradients, glass, blobs, giant type and motion are not being bundled merely to signal “modern/premium”;
- references are decomposed into transferable principles rather than superficial brand motifs;
- whitespace is allowed to remain whitespace.

## 3. Build

`gorvet-ui-implementation` implements using the detected/requested stack.

Priority:

1. existing project component;
2. existing project pattern;
3. existing semantic token;
4. existing framework/library component;
5. framework utility;
6. new reusable component or semantic token;
7. custom CSS/implementation;
8. hardcoded one-off values only when justified.

If compatible framework-specific skills are available, use them as adapters for technical contracts.

## 4. Review

`gorvet-visual-qa` inspects the result using the strongest evidence available: rendered UI/browser first, screenshots second, static code as fallback.

`gorvet-quality-audit` is the final cross-cutting completion gate for substantial new/redesigned UI. It checks generic AI-style accumulation, architecture, system discipline, UX, accessibility, SEO applicability and maintainability. When editing capability exists, material blockers/major defects should be corrected before delivery and re-checked once.

A successful build is not evidence of a successful interface.

## Required baselines

These are routing rules, not page-type templates:

- human-facing UI → accessibility baseline applies;
- public + indexable surface → frontend SEO analysis applies;
- substantial new/redesigned UI → final Quality Audit applies;
- implemented UI → Visual QA uses the strongest available evidence and states any limitation.

The depth of each specialist varies with the task.

## Adaptive routing examples

### Small established change
Context → Build → Review.

### New screen in an established product
Context → UI Architecture + relevant Design specialists → Build → Review.

### New product / missing design system
Context → UI Architecture + relevant IA/usability/system/accessibility (+ SEO and other specialists where applicable) → Build → Review.

### Existing poor UI
Context → Visual QA/Quality Audit → targeted Design → Build → Review.

### Form-heavy flow
Context → UI Architecture + Forms + Accessibility + UX Content + Interaction → Build → Review.

These examples illustrate domains; they are not hardcoded triggers for page types. Infer the needed structure/components/specialists from the actual request.
