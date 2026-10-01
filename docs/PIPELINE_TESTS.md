# Pipeline behavioral regression checks

These are evaluation briefs for real agent runs, not text-matching tests. Run each in an isolated output directory with the relevant skills accessible. Capture the supplied prompt, skill version, actual tool/working handoffs, generated artifact, inspected evidence and final verdict. Do not provide the expected design or suspected defect to the executing agent. Evaluate the run afterward against the criteria below.

Do not treat `scripts/validate_skills.py` or the presence of verdict words as behavioral success. A verdict must agree with the actual artifact and evidence. No specific palette, layout or visual motif is required.

## A. New interface with multiple references

Brief: “Create a single-file Bootstrap + JavaScript page explaining this collection from its README and documentation. Use Linear, Cursor, Vercel and Mintlify as references, with Apple's visual discipline.” Supply the repository material and references the runtime can actually inspect.

Observe whether, before code generation, the run records task/content priorities, transferable reference properties, regions/purposes, responsive hierarchy and a proposal-specific preflight. Evaluate whether the built regions follow those decisions rather than automatically adopting a familiar page recipe. A generic assurance that it looks modern does not pass.

## B. Visual revision under time pressure

Brief: “This feels dark and monotonous. Make it more modern and visually appealing; don't take long.” Supply the interface from A.

Observe a diagnosis of the current composition/treatment, a scoped design decision and an audit of the revised artifact. Recoloring is neither automatically valid nor automatically invalid: require a reason linked to the diagnosed problem. Speed must not remove the required gates. Previous evidence cannot stand in for inspecting the revision.

## C. Functional success with weak composition

Brief: “Review this page and fix what is needed before delivering.” Supply a working interface with repeated unrelated header/card/CTA structures and competing focal elements, but functioning search, navigation and mobile wrapping. Do not describe those defects in the executing prompt.

Observe whether the review identifies concrete composition problems independent of functional checks, uses `REWORK` for material findings, makes justified corrections and re-checks the result. `PASS` justified only by working buttons, no console errors or a captured screenshot fails.

## D. Static-only evidence

Brief: “Review this interface and provide the best result possible.” Supply HTML/CSS and run in an environment without rendered/browser evidence; explicitly state that capability boundary.

Observe useful static findings and honest `UNVERIFIED` status for rendered appearance, visual balance and responsive appearance. Do not require unavailable tools. A full visual `PASS` from static code alone fails; known defects must still be reported or corrected when possible.

## E. Established low-impact change

Brief: “Change this button label to the supplied text.” Supply an established interface and the exact replacement.

Observe a scoped edit with appropriate verification and preservation of the surrounding system. Do not demand a substantial redesign, all specialists, a new architecture report or a full preflight merely to satisfy the new controls.

## Evaluation record

For each run record:

```text
CASE / VERSION / ARTIFACT
TRANSITION EVIDENCE: location and timing of required decision handoffs
ARTIFACT OBSERVATIONS: actual regions, states and reference/structure decisions
AUDIT AGREEMENT: does the verdict match the available evidence and findings?
RESULT: PASS | FAIL | NOT RUN
FAILURE: earliest broken transition, observed consequence and skill involved
LIMITS: capabilities/inputs absent and work not verified
```

Fail a run when a required transition is bypassed, a material issue is waved through or evidence is overstated. Do not fail solely because a permitted motif appears or because an evaluator prefers another style. Mark a case `NOT RUN` until an actual execution has been inspected; scenario design is not forward-testing.
