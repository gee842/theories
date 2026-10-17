# U: every spine theorem on the base, or apart for a stated reason

17 October 2026. Board item U, on Ren's "let's first complete the unification" and "finish all before you return" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-17-complete-unification.md)). Integrator: the session "Repository completion review and restructure". Study: [section 166](../../BECOMING-RENEWAL-READING.md#166-every-spine-theorem-on-the-base-u).

**Result.** 44 join modules (484 theorems, every declaration with an empty axiom report) state the laws of 78 core modules of runs, processes, traces, frames, worlds, flows and webs. They landed in the core with receipt `20261017T071851.986246Z` (181 spine modules). In the [connectivity measure](../../THEOREM-CONNECTIVITY.md), apart theorems fall from 1,019 of 7,214 to 195 of 7,698. Every one of the 134 apart roots has a category and reason in [THEOREM-CONNECTIVITY-APART.json](../../THEOREM-CONNECTIVITY-APART.json), and `THEOREM-CONNECTIVITY.py --check` fails on any new unexplained one. The modules themselves live in the package (`experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`); this folder keeps how they were made.

| File | What it is |
|---|---|
| [U-BRIEF.md](U-BRIEF.md) | The brief each batch worked from: what a join is, the standard, the categories, the tools |
| [apart_roots.py](apart_roots.py) | The measure with trees overlaid, and the roots among the apart theorems |
| [apart-before.json](apart-before.json), [apart-after.json](apart-after.json) | Every apart theorem before (main 7b1e7450b) and after (all join modules overlaid) |
| [integrate.py](integrate.py), [scope.json](scope.json) | Registration of the modules in the core (CORE list, root imports and layer bullets, scope sentences) |
| `pilot/`, `A1/` … `D2/` | Per batch: `classification.json` (roots left apart, with reasons) and `REPORT.md` (the batch's report; saved by the integrator from the agent's final message, since subagents may not write report files) |
| [save_report.py](save_report.py) | That saving step |

Batches: pilot (the integrator: Seeking, Capture, the two course worlds, ethics and bridge classification), A1 (Selection, Learning, Learnable, Identification, Description), A2 (Likeness, Copying, CrossSituational, Retrodiction, Readout, Contacts, Revision, ContinuingRevision), B1 (Attraction, Recurrence, Branching, Lasting, Openness, Horizon, Countdown, Viability, Counterfactual), B2 (Tail, Sensitivity, Decidedness, Diagonal, Listing, Refinement, Order, OrderNormal), C1 (Coupling, Propagation, Loops, Closing, Thresholds, Frequency, Remainder, Routes, Observation), C2 (Typicality, Situations, Gluing, Context, Quantum, Weighted, Courses, Readings), D1 (ReferencePlan, Composition, Joining, Testing), D2 (Boundaries, Population, Evolution, Entropy, OneStep, Identity, Locality, Stock, Change, Space, Reserve, Sampling, Units, Interdependence). Batches A1–D2 were Claude Opus 5.5 subagents working from the brief in scratch; the integrator reviewed the joins they flagged and removed three where the run played no role in the law (`run_closed_cannot_select`, `share_rises_along`, `chsh_wins_iff`), classifying their roots instead; the three `*_in_context` lemmas, as thin, stay only as helpers of the context-freedom theorems.

## U2: the follow-through (17 October 2026)

Ren, on U's open items: "let's fix all these" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-17-unification-follow-through.md)). Board item U2. The folder [u2/](u2/) keeps the work:

| File | What it is |
|---|---|
| [u2/relabel_docstrings.py](u2/relabel_docstrings.py) | Retired labels in the spine's Lean comments and the checker's scope sentences replaced by the current terms (comment text only; code checked unchanged) |
| [u2/U2-PERIPHERY-BRIEF.md](u2/U2-PERIPHERY-BRIEF.md), [u2/batches.json](u2/batches.json) | The brief and the eight batches (P1–P8) that join the 54 periphery modules with apart roots |
| [u2/U2-ADDENDUM-AXIOM-RING.md](u2/U2-ADDENDUM-AXIOM-RING.md) | The periphery-join ring: joins through periphery proofs that carry axioms, named `…Inherited`, imported by nothing in the core or the bridge |
| [u2/periphery-before.json](u2/periphery-before.json) | The apart theorems of spine and periphery before the periphery joins (814 of the periphery's 1,282 apart, 524 roots) |
| `u2/P1/` … `u2/P8/` | Per batch: `classification.json` and `REPORT.md` (P2 and P3 also keep their first-pass report), as in U; the modules themselves landed in the package (`f36a93aaa`), with ten names renamed for market words (`UnitTraces.oneStep_*`, `ReconfigurationProcesses` `draw`) |

Landed 17 October 2026 (`f36a93aaa`, core receipt `20261017T113233.209872Z`): periphery apart 814 → 229 and roots 524 → 171, spine apart 186 → 180 of 8,007 and roots 125 → 122, every root classified; [study §167](../../BECOMING-RENEWAL-READING.md#167-the-unification-follow-through-u2).
