# Optional framework adapters

GORVET is self-sufficient. Adapters are optional specialist skills for project/framework knowledge that generic UI skills cannot infer reliably.

## What belongs in an adapter

- repository and module structure;
- routing/render/template contracts;
- proprietary helpers and components;
- asset registration/loading conventions;
- API/AJAX response contracts;
- server-rendered partial conventions;
- framework-specific metadata/SEO placement;
- internal validation and feedback helpers;
- constraints that must not be bypassed.

## What does not belong in an adapter

- general visual taste;
- generic accessibility guidance;
- generic form UX;
- generic navigation/IA;
- anti-AI styling rules;
- general SEO strategy;
- general responsive design;
- generic component-selection heuristics.

Those belong in GORVET universal skills.

## Cooperation contract

Universal skills govern **intent and quality**. Adapters govern **technical contracts**.

If an adapter exists, implementation should consult it. If none exists, `gorvet-ui-implementation` continues with the detected stack normally.

An adapter must never be required merely because the project uses Bootstrap, Tailwind, React, Angular, Vue, Svelte, or another common technology. GORVET must already understand and inspect those systems.
