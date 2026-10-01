# GORVET pipeline

The pipeline is deliberately small. Specialist skills are capabilities, not mandatory ceremonies.

## 1. Context

Use `gorvet-project-context` to resolve what is being built, for whom, with what constraints, and on top of what existing system.

Inputs may include project documents, requirements, architecture documents, code, screenshots, references, existing components, design tokens, and the live/rendered product.

Output is a concise resolved context, not a report unless persistence is useful.

## 2. Design

Select only the specialists needed:

- `gorvet-information-architecture`
- `gorvet-ux-usability`
- `gorvet-ux-research-testing` when material product/user uncertainty requires evidence
- `gorvet-ui-structure-design`
- `gorvet-design-system`
- `gorvet-interaction-patterns`
- `gorvet-forms`
- `gorvet-ux-content`
- `gorvet-accessibility`
- `gorvet-frontend-seo` for public/indexable surfaces

The design stage resolves decisions before code. It should not produce lengthy paperwork unless the project needs persistent design memory.

## 3. Build

`gorvet-ui-implementation` implements using the detected stack.

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

`gorvet-visual-qa` checks the real result when visual evidence is available. `gorvet-quality-audit` performs a final cross-cutting audit.

A successful build is not evidence of a successful interface.

## Adaptive routing

### Small established change
Context → Build → Review.

### New screen in an established product
Context → relevant Design specialists → Build → Review.

### New product / missing design system
Context → IA/usability/(research when needed)/structure/design-system/accessibility (+ SEO where relevant) → Build → Review.

### Existing poor UI
Context → Visual QA/Quality Audit → targeted Design → Build → Review.

### Form-heavy flow
Context → Forms + Accessibility + UX Content + Interaction → Build → Review.

### Public marketing/content page
Context → IA + Structure + Design System + Accessibility + SEO → Build → Review.

Do not run a specialist because it exists. Run it because the task contains its decision domain.
