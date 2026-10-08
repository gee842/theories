# What the start of the closure history must hold

7 October 2026. AI-assisted continuation of the [contact-formation track](CONTACT-FORMATION-LAW.md). `FormationClosure.start` begins with no spare pairs, nothing recovered, nothing dissipated, 200000 held units (`held`) and 20 source units. This note asks which of these follow from the activity that starts there. It follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md): held amount and source are coordinates of the one configuration, and the question is what the activity's own draws and conversions require of them.

**Formal status:** [StartingStock.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/StartingStock.lean), 25 declarations, every axiom report empty. It imports `RecoveryQuantum` and `FormationDraw`. It is checked by [check_stock_derivation.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_stock_derivation.py), which also recomputes the least start by independent Python search.

## Transition addressed

Activity of a history → the starting amounts it requires.

## What is derived

| Result | Lean statement |
|---|---|
| **Spare stock zero is forced.** From a beginning with nothing dissipated and nothing recovered, every formation of every later history is backed by ten dissipated units in that history exactly when the starting spare stock is zero | `backing_iff_empty_stock` |
| An inherited pair forms with nothing dissipated | `inherited_pair_forms_unbacked` |
| With nothing dissipated, the native backing invariant forces nothing recovered | `nothing_dissipated_nothing_recovered` |
| Below one draw, no event of the closure process completes | `nothing_held_nothing_proceeds` |
| Held amount plus cumulative draw is conserved up to arrival | `held_amount_conserved` |
| A history without arrival started holding its operations times `draw`, plus what remains | `held_covers_draws_before_arrival` |
| Every completed history converts ten source units per probe | `source_accounting` |
| **The closure history's least start.** It completes from held amount `f` and source `S` only if `f ≥ 114702` (seven draws of 16386) and `S ≥ 20` (two conversions); it completes at exactly that start and stops with one unit less of either | `history_needs`, `least_starting_stock` |

The 200000 and 20 of `FormationClosure.start` (`start_is_startWith`) are one admissible start above this minimum. The results of the closure track do not depend on those particular numbers.

## Status of each starting amount

- **Spare pairs: derived** (zero), relative to the claim that formations are backed by failures recorded in the same history. With any inherited pair the claim fails, as `inherited_pair_forms_unbacked` shows.
- **Recovered pairs: derived** (zero) from the backing invariant once nothing is dissipated.
- **Nothing dissipated at the beginning: not derived.** It is what "beginning" means in part 1. A start with prior dissipation is a later point of some longer history.
- **Held amount and source: minimum derived, existence proved necessary.** The least amounts are computed from the history's own draws and conversions. That there is any held amount or source at all is not derived: `nothing_held_nothing_proceeds` proves that without it no operation completes. Where it comes from belongs to the renewal question (how an activity renews what it draws on), which this note does not settle.

## What would change the account

An operation that completes with nothing held, or a conversion that does not lower the source coordinate. Either would break the conservation or source accounting used here.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`: `python3 check_stock_derivation.py`.
