# Contributing

Contributions are welcome.

## Rules

1. Keep skills vendor-neutral. Refer to capabilities (repository access, browser rendering, screenshots) instead of proprietary tool names unless documenting an optional example.
2. Keep the pipeline short. Add a specialist skill when it isolates meaningful expertise; do not add mandatory stages without evidence.
3. Prefer progressive disclosure. Put core operational rules in `SKILL.md`; move detailed checklists, patterns, and examples into `references/`.
4. Do not introduce universal visual taste as a rule. Prefer context, function, brand, accessibility, and evidence.
5. Do not weaken accessibility or semantic HTML for visual convenience.
6. Add framework-specific behavior as an optional adapter rather than contaminating universal skills.
7. Run `python scripts/validate_skills.py` before submitting changes.

## Pull requests

Describe:

- problem being solved;
- affected skill(s);
- why the change belongs in the universal layer or an adapter;
- any new references/standards used;
- expected effect on context/token use.
