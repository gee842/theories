# Handoff: formal unification of the generative core in Lean

7 October 2026. Thread "Lean proof of the generative core" (branch `claude/project-thread-mlqbun`). Ren's goal for this thread: **formal unification**. That means one Lean entry in which every package applies to the same generative process, with each connection proved rather than asserted. Standing rules apply: no assumptions and no axioms (not even `propext` or `Quot.sound`), monist and relational framing, and auto-commit and merge to main after each finished piece.

## What is proved, and where

All modules are in `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/`. Every declaration listed audits completely empty. `python3 check_contact_formation.py` (Lean 4.29.1 on `PATH`) builds them with the 32-module core and the imported valuation and alignment modules: 46 modules, 801 audits, all empty.

| Module | Content |
|---|---|
| `ContactFormation`, `FormationClosure`, `AcquiredContact` | Contact changes only through formation. Formation draws on pairs recovered from the port's own failed transfers. A two-probe inquiry decides formation and calibrates receipts. |
| `PortValuation`, `ValuationInCore` | The formation disposition as a valuation organization with a derived consequence law; every organization embeds in the core. |
| `RevisingPort` (61 declarations) | The port plus its retained reading as **one process**. Every history is both the valuation organization's run (`memory_trace`) and a port history (`port_trace`). The class changes only through its own selection, and once met it forms exactly when blocked. The encounter's parts are proved necessary: `decision_rule_unique`, `one_output_cannot_decide`, `broken_reset_cannot_decide`, `unconsumed_formation_unbacked`. The reading is set apart only by which steps change it (`reading_changes_only_at_encounters`). |
| `RelationalCut` | The activity/formation split is derived for every process as a relation of each step to a coordinate (`cut_trace_iff`). |
| `PortAlignment` | `InquiryRelevance` and `InquiryWarrant` read on the port's own response table: relevance and transfer adequacy hold. Mismatches are proved: three tables, not four (`table_never_both`), and the formation decision is not a one-entry continuation (`formation_outside_continuations`). |

Write-ups:
- [CONTACT-FORMATION-LAW.md](../research/2026-10-05-generative-foundation-review/root-foundation/CONTACT-FORMATION-LAW.md) covers the whole track.
- [UNIFIED-ENTRY.md](../research/2026-10-05-generative-foundation-review/root-foundation/UNIFIED-ENTRY.md) is the connected/separate table for all packages, plus the splits and inputs ledger.

`GenerativeCore` (28/28) and `Depletion` (5/5) were audited declaration by declaration and are already axiom-free.

## What is open, and why

- **U1/U2 for the whole port.** `NativePortContinuation` (the native port as a sustain-law instance) is only on the rename branch `claude/project-thread-x1q9hl`, which waits on Ren's merge. Until it lands, recovery and formation cannot be shown to be supported stages under the new names.
- **Formation's interface draw.** Still assumed. No current result needs it; settle it with U1 for the whole port, where a result either needs it or it is dropped.
- **Formation as one event, rather than a rearrangement of the port's material.** A decision card was put to Ren (options: material slot / keep as one event, proved minimal / also drop the demand). It is unanswered; work proceeded on "keep, proved minimal".
- **Recovery rate (10 per pair) and the phase-cycle inputs.** Owned by the "Ground the remaining process-law obligations" thread.
- **Renewal–closure and ethical naturalism.** Not yet connected to the port; candidate bridges are in UNIFIED-ENTRY.md.
- The alignment package's own theorems still use `propext`/`Quot.sound`. `PortAlignment` therefore restates what it needs and shares only definitions. The checker builds imported packages (valuation, alignment) without counting their own audits or warnings; the audits of our modules are transitive, so they would show any axiom reached.

## Exact next step

1. After `x1q9hl` lands on main, merge main into this branch. Expect the token renames (`fuel→held`, `spent→enacted`, `income→arrived`, `wasted→dissipated`, `charge→support`, `Payable→Supportable`, `debit→enact`, `bill→draw`); the rename thread said it will carry them into these modules.
2. Prove recovery and formation continue (`Continues`) like native supported stages. That gives `SustainLaw` and a strictly falling potential for `FormationClosure.process` and the revising port, and therefore `no_infinite_execution_under_depletion` for the whole revising port. Decide formation's draw there.
3. Then attempt the renewal bridge: is the formed contact adequate in renewal's sense (opening ≥ formation demand), so that the port's deadline comes from its finite source?

## Resume point

The thread stopped at a clean boundary: no proof is half-finished, and every module above is merged to main. Work last merged at `fc57476`; this handoff update is merged after it. Branch: `claude/project-thread-mlqbun`.

## Open items for Ren

- The formation decision card (material slot / keep as one event / drop the draw) is unanswered.
- The rename branch `claude/project-thread-x1q9hl` needs Ren's word to merge; step 1 above waits on it.

## Spawning a continuation

Give the new thread: this file, [UNIFIED-ENTRY.md](../research/2026-10-05-generative-foundation-review/root-foundation/UNIFIED-ENTRY.md), and the standing rules (no assumptions, no axioms including `propext`/`Quot.sound`, monist and relational names and prose, auto-merge to main after re-running `check_contact_formation.py`). Start at "Exact next step" item 1. If the rename has not landed, start at item 3 (the renewal bridge), which does not touch renamed fields.
