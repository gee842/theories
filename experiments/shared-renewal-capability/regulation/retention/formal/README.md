# Checked event structure of formed regulation and material retention

6 October 2026. This formalization checks the seven-event law in the [mathematical development](../../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-MATH.md). Its 32 new theorem declarations pass Lean 4.29.1 using `Std`. The [verification record](verification.json) separately records the existing root module compiled as a dependency.

| Source | Checked claim |
|---|---|
| [Retention.lean](Retention.lean) | Explicit reactant guards and updates; state validity and material ledgers on every finite path; fuel/spent ledger and copy budget; the low-fuel bootstrap trap; an exact decreasing rank, event-count bound and terminal characterization; the six-event paid formation/repair/capture/copy witness. |
| [RootBridge.lean](RootBridge.lean) | Exact equivalence with paths in the existing `Generative.Process` and `Generative.Trace` interface; fuel and copy budgets, bootstrap obstruction, witness and actual-successor composition transported into that root. |

## Match to the mathematical law

`Config` stores `(N,M,B)` and `State` stores `(C,G,F,E)`. Damaged sites and precursor are derived as `D=N-C` and `P=M-G`. `Valid` requires `C≤N`, `G≤M` and `F≤B`; `step_valid` checks that every guarded update preserves these constraints. Consequently the derived material totals remain exactly N and M on arbitrary valid paths. B is a physical storage-capacity assumption, not a numerical cutoff.

The seven events are `damage`, `fabricate`, `repair`, `capture`, `copy`, `wear` and `leak`. `Enabled` records only their reactant/capacity conditions. Their stochastic mass-action rates are not formalized. The relation admits all enabled channels; setting a kinetic coefficient to zero can only remove paths, preserving the universal path bounds. The terminal equivalence corresponds to actual kinetics when damage, wear and leak remain positive. Other experimental control laws require their own checks.

For every finite trace, the theorem `trace_fuel_ledger` states

\[
F_{\rm final}+E_{\rm final}+\text{spent}=F_{\rm initial}+E_{\rm initial}.
\]

`spent` counts one unit for each fabrication, repair, copy or leak; capture transfers a source unit into usable fuel. `trace_copy_budget` therefore proves that total copies cannot exceed the initial usable and incident fuel together. There is no resource reset between the trace's events.

`bootstrap_under_two_fuel` proves that when C=G=0 and F<2 initially, every reachable state still has C=0 and F+G≤1. Repair, capture and copying remain unavailable there. Abundant inaccessible incident fuel does not bypass the bootstrap cost.

The rank

\[
V=4E+2F+C+G
\]

falls by exactly two on capture and leakage, and by exactly one on every other event. Thus every event trace has length at most its initial V, no nonempty trace returns to its own starting state, and no infinite event sequence exists. This is a property of the closed finite-stock law, not a universal generativity measure. Elapsed physical time is not bounded; an absorbing process can remain in its terminal state forever. Virtual uniformization self-loops are not physical events in this relation.

For a valid state, terminality is equivalent to C=G=F=0; inaccessible E may remain. The supplied witness starts `(C,G,F,E)=(0,0,2,2)` with `(N,M,B)=(1,3,2)` and follows fabrication, repair, capture, copy, capture, copy to `(1,3,0,0)`. Separate theorems check that repair enables capture and capture enables copying at the corresponding states. Positive probability of a path under positive finite rates is a separate stochastic argument, not part of this discrete witness theorem.

## Reproduce and inspect

Run `python3 check.py` in this directory. The script explicitly selects `lean +leanprover/lean4:v4.29.1`, locates and hashes that compiler, and copies the frozen sources into a fresh temporary build. The existing [GenerativeCore.lean](../../../../integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) is read at its original repository path, hashed, and compiled there as a dependency; it is not duplicated or edited in this development. No existing project object file can replace the recorded source.

The script rejects proof placeholders, custom axioms, unsafe declarations and native decision shortcuts. Every new named theorem must have a corresponding axiom audit. The compiler logs and source/compiler hashes are retained in [verification.json](verification.json) and [verification/](verification/). Standard Lean foundational dependencies are disclosed; they are not new physical premises. Compilation must finish without warnings, sources must remain unchanged during verification, and all audits must pass.

The checker writes only this directory's verification record and logs. Its successful result certifies the formal deductions, not the Python implementation, probability bounds, empirical chemistry, useful-variant selection, learning or the whole unified foundation. These limits and the new connection to the root are recorded in the [formal scope note](../../../../../_process/history/2026-10-05-support-and-shared-generativity/completion/ENDOGENOUS-REGULATION-LEAN.md).
