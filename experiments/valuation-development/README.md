# Valuation development: formal companion

7 October 2026. This is the formal companion to the [valuation-development argument](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md). It checks six results about how an organization's selective dispositions can change through its own history, together with the finite countermodels showing that their hypotheses cannot be dropped. It is AI-authored. A separate internal AI review compiled it independently and accepted it with corrections, which have been applied.

## Contents

| File | Purpose |
|---|---|
| [lean/ValuationDevelopment.lean](lean/ValuationDevelopment.lean) | 33 theorems: U1 retention, U2 extension underdetermination, U3 prediction/scoring trade-off, U4 coupling and proxy capture, U5 convergence and divergence, U6 separable capacities (levels 1–4) |
| [lean/Audit.lean](lean/Audit.lean) | `#print axioms` for every theorem |
| [lean/audit-output.txt](lean/audit-output.txt) | Saved audit result |
| [lean/ClosedLoopValuation.lean](lean/ClosedLoopValuation.lean) | 11 theorems (§12 of the argument): under per-encounter contraction, closed-loop amplification needs a selection difference; witnesses of amplification, self-confirming underestimates, scheduled variation and generative or degenerative fates |
| [lean/ClosedLoopAudit.lean](lean/ClosedLoopAudit.lean), [lean/closed-loop-audit-output.txt](lean/closed-loop-audit-output.txt) | `#print axioms` for the closed-loop module and its saved result |
| [lean/ExplorationCoverage.lean](lean/ExplorationCoverage.lean) | 11 theorems (§13): under retention exact for the option reached, in a world whose consequences do not change, coverage equalizes estimates whatever drives exploration; witnesses of retained curiosity and optimism covering and of a low estimate preventing coverage |
| [lean/ExplorationAudit.lean](lean/ExplorationAudit.lean), [lean/exploration-audit-output.txt](lean/exploration-audit-output.txt) | `#print axioms` for the exploration module and its saved result |
| [lean/ValuationCompletion.lean](lean/ValuationCompletion.lean) | 15 theorems (§14): stale estimates after a change, a noise floor (reached and kept) and noise-induced lock-in, reduction of interaction with a fixed partner and a joint-coverage witness, level-5 route revision and level-6 valuation of others formed by pairing, each reaching selection |
| [lean/CompletionAudit.lean](lean/CompletionAudit.lean), [lean/completion-audit-output.txt](lean/completion-audit-output.txt) | `#print axioms` for the completion module and its saved result |
| [lean/lean-toolchain](lean/lean-toolchain) | `leanprover/lean4:v4.29.1` |

## Reproduce

The development uses core Lean only, with no Mathlib and no Lake project.

```sh
cd experiments/valuation-development/lean
lean -o ValuationDevelopment.olean ValuationDevelopment.lean
LEAN_PATH=. lean Audit.lean
LEAN_PATH=. lean -o ClosedLoopValuation.olean ClosedLoopValuation.lean
LEAN_PATH=. lean ClosedLoopAudit.lean
LEAN_PATH=. lean -o ExplorationCoverage.olean ExplorationCoverage.lean
LEAN_PATH=. lean ExplorationAudit.lean
LEAN_PATH=. lean -o ValuationCompletion.olean ValuationCompletion.lean
LEAN_PATH=. lean CompletionAudit.lean
rm -f *.olean *.ilean
```

Result on 7 October 2026: 27 theorems depend on no axioms. `coupled_signal_bounded`, `shared_exposure_contracts`, `shared_exposure_converges`, `shared_exposure_equalizes` and `multistable_divergence_forever` depend on `propext` and `Quot.sound`. `rounding_gap_forever` depends on `propext` only. These come through `omega` and `simp`. There are no custom axioms, no `sorry` and no `native_decide`. The closed-loop module adds 11 theorems: 5 depend on no axioms and 6 depend on `propext` and `Quot.sound` only. The exploration module adds 11 theorems and the completion module 15, all depending on no axioms or only on standard `propext` and `Quot.sound`. In total there are 70 theorems.

## Scope

- The universals quantify over every `Org` (selection plus retention law) and every consequence law.
- The countermodels are concrete finite witnesses checked by evaluation.
- `halving_nonexpanding_on_sample` is checked only over values below 8.
- Everything is deterministic, and the noise floor has no probability law. Interaction covers two organizations with a common presented condition. Levels 5 and 6 are minimal witnesses whose route-switching rule and plasticity law are supplied.
- This is formal mathematics about the stated representation. It is not empirical evidence and not an ethical result.
