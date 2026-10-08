# Population replacement and corrective funding

8 October 2026. Continuation of the [collective-attractor study](../../../theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md#population-replacement-and-internally-funded-correction), after Ren requested work until a substantive wall. [Integration and counterreview](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md#continuation-to-the-institutional-wall) state the institutional formation/correspondence limit.

**71 new theorems / 100 audited declarations** are checked with Lean 4.29.1. [PopulationCorrection.lean](PopulationCorrection.lean) contains 61 theorems; [PopulationRealization.lean](PopulationRealization.lean) contains 10. The [receipt](population-verification.json) binds every source and log, the checker, compiler and per-declaration axiom audit. Permitted standard logical dependencies are `propext`, `Quot.sound` and `Classical.choice`. There are no added axioms, admitted proofs or unchecked decision shortcuts.

The existing [first construction](COLLECTIVE-README.md) remains 32/41, not recounted as new. `GenerativeCore` and `CollectiveDestruction` are frozen and freshly compiled as dependencies. The actual economic projection and guarded carrier trace are proved, rather than composed only by citations.

| Checked connection | Main declarations | Scope |
|---|---|---|
| Current local optimum to bounded allocation | `locally_optimal_revision`, `strict_revision_advantage`, `revised_slot_is_optimal`, `revision_quota` | Only available revisions; inherited contracts can remain currently suboptimal |
| Accounting and funding | `operating_receipts_accounted`, `treasury_accounted`, `correction_stays_funded` | Declared receipts and enforceable collection; F ≤ N for persistent funding |
| All positive schedules | `funding_iff_ledger`, `exact_schedule_activation_boundary`, `exact_schedule_topup` | Initial r ≤ N and F ≤ N; kₜ ≥ 1 for finite exhaustion of counterfactual contributors |
| Rate comparison and unit case | `faster_replacement_reduces_available`, `unit_available_is_triangle` | Pointwise greater revision throughput reduces pre-activation contributions |
| Both eventual regimes | `schedule_shortfall_is_destructive`, `destructive_region_absorbing`, `schedule_sufficiency_reaches_full_state` | Finite arrival and persistence in reduced coordinates; supplied renewal law |
| Loss and intervention | `growth_eventually_destructive`, `slow_recovery_has_real_loss`, `boosted_growth_preserves_floor` | Six-slot example: slow recovery passes through v = 0; growing throughput plus one reserve unit preserves v ≥ 4 |
| Institutional failure | `exact_funded_leak_tolerance`, `all_renewing_leak_tolerance`, `identical_local_ordering_different_funding` | Funding failures under specified diversion, not a proof of its endogenous choice |
| Longer-horizon countercheck | `arbitrary_finite_horizon_defection` | Original stage game, fixed always-escalating opponent, finite nonnegative integer weights |
| Actual succession | `actual_generation`, `actual_core_history`, `exact_economic_projection`, `distinct_generation_carriers` | Requires N material parts before each generation and supplied N arrivals |
| Realization failures | `missing_parts_disable`, `constructive_economy_can_lack_realization`, `destructive_economy_with_actual_successors` | Economic success is not sufficient material support; v is not all support |

## Reproduce

```sh
python3 experiments/market-generativity/meta-attractor/check_population.py
python3 experiments/market-generativity/meta-attractor/population_experiment.py
```

The formal checker builds frozen sources in a new temporary directory and preserves its snapshots/logs in [population-verification](population-verification/). It never overwrites the first-round proof receipt or another study's proof files. No dependency installation is needed. The supplementary [finite checks](population-experiment.json) compare actual per-slot revisions and receipt accounting to the aggregate recurrence in 24,744 cases, test 9,949 schedule boundaries and 10,247 transfers, and preserve three illustrative histories. These calculations do not replace the universal Lean claims or constitute empirical evidence.

## Correspondence and hypotheses

N is a fixed number of operating contracts; r is the number whose actual activity replenishes the represented shared capacity. Old contracts operate and contribute before bounded revisions take effect in the next generation. F is both the enforceable institution's per-round cost and its reserve target. B is actual retained money; surplus is released and accounted for. v is a particular capacity with explicit regeneration, floor and cap. The model supplies the binary repertoire, current-return objective, full use of revision opportunities, revenue production and collection, material arrival and capability schedule.

Gross receipts of 7 per renewing contract and 8 per escalator split into contributions and private receipts. Utility additionally includes shared escalation effects. Arithmetical coverage of replacement costs is a claim about funds; actual carrier enablement requires material parts separately. The external-input interface is a bounded representation of supplying relations, not a claim that they exist outside the common process.

The model does not derive the collection institution, commitment formation, its legitimacy or resistance to agent-chosen rule changes. The transfer theorem does not supply a donor or show that activating enforcement prevents all interim harm. The finite-horizon lemma is separate from the population recurrence. Descriptive stability, v and monetary return are not a universal ethical metric. No theorem of inevitable AI destruction or cooperation is asserted.
