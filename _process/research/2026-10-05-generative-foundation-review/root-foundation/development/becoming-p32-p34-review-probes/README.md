# Thirteenth review: probes and the drafts reviewed

2026-10-10. Lean probes written by the independent reviewer (a Claude Opus 5.5 agent that did not write the work) for the [review of P32 to P34 and the P35/P36 drafts](../../BECOMING-P32-P34-REVIEW.md), commit `7f69f455`, with the two drafts it reviewed. **These are review evidence, not registered results.** They are not in the Becoming package and have no checker receipt. The results that P34b and P35 moved into the core are cited from the package and its receipt, not from here (study §46 and §48).

| File | SHA-256 | Content |
|---|---|---|
| `D35.lean` | `cb04495e4bf9e89e409842448af1230aeb312fb88008a8c6b28a4565c4d51e26` | draft P35 as reviewed: `since`, `Settles`, `change_within`, `Closing`, `enclosed_counting`; 48 declarations |
| `D36.lean` | `6e219ae82307702552b0388ca137a5bb51da98f20c014add5d8366377a3c2fe7` | draft P36 as reviewed: `below`, `Settles.reach`, `Closed`, `finite_counting`; 22 declarations |
| `DraftAudit.lean` | `8bca27b8f91c29038727b0c2a0aea70a567be5131e868d64974f742b99827e35` | the reviewer's axiom audit of the two drafts |
| `Review13.lean` | `08ff23259f272c30a4f54d76fa43100706b8678be9132208804a6d40edd011dd` | probes Q1–Q8: 42 declarations and 8 `example`s |
| `Review13Audit.lean` | `f91a71703d451fe36d85dd715c9b5777f46b464eca1c029cdb329b8ed2f77264` | the probes' axiom audit |

`draft-audit.log` and `probe-audit.log` hold the reviewer's audit output: none of the drafts' 144 constants and none of the probes' 78 constants depends on any axiom. The `Nat.*` lines of `probe-audit.log` are the reviewer's comparison with the prelude (Q8), not probes. The drafts import `Becoming.Openness` at `7f69f455`; the probes import `Becoming` and `D36`.

## Where the probes went

- **Q1 `Balance`, `tally_balance`, `tally_le`, `tally_of_balance`, `tally_iff`, `balance_not_tally`:** in the core `Balance`, `Tally.balance`, `Tally.ceasing_le`, `tally_iff` and `balance_not_tally` (finding U1). `ceasing_bound_law` is kept here; its content is `balance_not_tally` with `Tally.ceasing_le`.
- **Q2 `tally_congr`, `tally_iff_counted`:** `Tally.congr` and `tally_iff_counted` (U7).
- **Q3 `since_le`, `since_zero_le`, `settles_zero`, `settles_iff_zero`, `same_laws`:** `occurrences_le`, `occurrences_zero_le`, `ChangeBound.from_zero`, `changeBound_iff_zero` and `World.enclosed_iff_finite_counting` (U4). The law is now stated once, with a change bound from the first step.
- **Q4 `tended_dissipation_idle`, `tended_not_binds`:** `World.tended_not_binds`, which adds that bounded transmission is idle too (U3); P36 renamed it `World.openQueue_not_binds`.
- **Q5 `FirstChange.*`, `lpo_of_settlesEnds`, `lpo_of_finiteEnds`:** `Swap.*`, `ChangeBound.lpo_of_ends` and `World.lpo_of_finite_ends` (U5). `Swap` counts with `mark` where the probes used `ind`.
- **Q6 `OneSwap.*`, `closed_dissipation_binds`:** `World.replaced`, `World.finite_dissipation_binds` and `World.replaced_attains`, with `Swap` at a sequence that is `true` throughout.
- **Q7 `binds_arising`, `binds_adds`:** `World.binds_arising` and `World.binds_adds` (U3).
- **Q8:** the drafts' arithmetic now reuses `RelationalRenewal.le_sub_from_add` and `Fin.eq_of_val_eq`, and the core's arithmetic is gathered at the head of `Becoming.Dependence` (U6).

The drafts' `Closing` and `Closed` worlds became `EnclosedQueue` with `World.enclosedQueue` and `FiniteQueue` with `World.finiteQueue`: natural-number relata, no ground relata, no start step and no exchange before it. `since` became `occurrences`, `Settles` became `ChangeBound`, and `below` became `placesBelow`.
