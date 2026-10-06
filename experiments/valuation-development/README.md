# Valuation development: formal companion

7 October 2026. This is the formal companion to the [valuation-development argument](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md). It checks six conditional universals about how an organization's selective dispositions can change through its own history, together with the finite countermodels showing that their hypotheses cannot be dropped. It is AI-authored and has not yet been independently reviewed.

## Contents

| File | Purpose |
|---|---|
| [lean/ValuationDevelopment.lean](lean/ValuationDevelopment.lean) | 28 theorems: U1 retention, U2 extension underdetermination, U3 prediction/valuation trade-off, U4 coupling and proxy capture, U5 convergence and divergence, U6 separable capacities |
| [lean/Audit.lean](lean/Audit.lean) | `#print axioms` for every theorem |
| [lean/audit-output.txt](lean/audit-output.txt) | Saved audit result |
| [lean/lean-toolchain](lean/lean-toolchain) | `leanprover/lean4:v4.29.1` |

## Reproduce

The development uses core Lean only, with no Mathlib and no Lake project.

```sh
cd experiments/valuation-development/lean
lean -o ValuationDevelopment.olean ValuationDevelopment.lean
LEAN_PATH=. lean Audit.lean
rm -f ValuationDevelopment.olean ValuationDevelopment.ilean
```

Result on 7 October 2026: 25 theorems depend on no axioms. `coupled_signal_bounded`, `shared_exposure_contracts` and `shared_exposure_converges` depend on `propext` and `Quot.sound`, through `omega` and `simp`. There are no custom axioms and no `sorry`.

## Scope

- The universals quantify over every `Org` (selection plus retention law) and every consequence law.
- The countermodels are concrete finite witnesses checked by evaluation.
- `halving_nonexpanding_on_sample` is checked only over values below 8.
- Selection is deterministic. U5's contraction theorem covers shared exposure only; closed-loop amplification is open.
- This is formal mathematics about the stated representation. It is not empirical evidence and not an ethical result.
