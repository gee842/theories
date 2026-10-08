# Local optimization and collective loss checks

8 October 2026. [CollectiveDestruction.lean](CollectiveDestruction.lean) has **32 new theorems / 41 audited declarations**, checked using Lean 4.29.1 and `Std`. The [receipt](collective-verification.json) records source, checker and compiler hashes and dependencies for each declaration. The proof audit permits only the disclosed standard logical dependencies `propext`, `Quot.sound` and `Classical.choice`; it adds no axioms or unchecked placeholders.

The [theory](../../../theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md) explains the mechanism and interpretation. The [study and author counterreview](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md) preserve the correspondence obligations, subsequent population composition and remaining institutional formation connection. These are conditional results; no old proofs are recounted as new.

| Role | Declarations | Scope |
|---|---|---|
| Individual versus joint ordering | `unilateral_gap`, `dilemma_conditions`, `joint_race_pareto_inferior` | Generic integer payoff identity; supplied population interpretation; concrete two-position joint loss |
| Exact local fidelity | `race_strictly_best`, `restraint_best`, `restraint_strictly_best`, `exact_local_optimization` | Exact one-period optimization; not whole repeated-game optimization |
| Best-response robustness | `low_best_response_must_race`, `high_best_response_must_restrain`, `threshold_racing_also_optimal` | Strict low/high regions; genuine indifference at q = 2 |
| Dynamic approach | `low_history`, `restraint_bound`, `capacity_bound`, `finite_destructive_entry`, `destructive_absorbing`, `exact_basin` | Finite arrival in reduced coordinates for every kₜ ≥ 1; exact basin depends on declared tie rule |
| Capability | `growing_capability_enters`, `greater_capability_depletes_faster`, `zero_throughput_preserves_capacity` | Supplied throughput, including increasing schedules; no endogenous intelligence formation |
| Prevention and its limits | `protection_for_any_best_responses`, `protection_preserves`, `late_protection_does_not_restore`, `threshold_race_enters_basin` | Effective q ≥ 3; strict best response; preserving v does not restore it |
| Causal and composition witnesses | `unilateral_restraint_does_not_stop_pressure`, `joint_restraint_preserves`, `separate_safety_checks_do_not_compose` | Joint restraint changes the transition; unilateral restraint cannot stop the other's pressure; isolated approvals can overbook a shared limit |
| General proof certificates | `rank_entry`, `invariant_history` | Supplied rank, closure and preservation obligations; no automatic applicability |

## Reproduce

```sh
python3 experiments/market-generativity/meta-attractor/check_collective.py
```

The checker compiles the frozen actual module and generated audit in a fresh temporary directory, using the already installed compiler. It stores the checked source and logs in [collective-verification](collective-verification/) without touching the adjacent studies' receipts or sources. No dependency installation is needed.

## Model correspondence

The pair `(restraint, capacity)` represents effective institutional consequences and a particular shared continuation capability. Neither is an all-purpose welfare or life score. Utility, institution effects, positive throughput, lack of renewal and initial basin membership are supplied. Best-response fidelity is formally established for the stated stage payoff. The stock coordinate does not enter that objective; longer-horizon concern for it would change the decision problem.

This first module does not construct reproduction, differential replacement, funding of protection, physical execution at zero shared capacity, stochastic recurrence, a compact full-state attractor, or empirical correspondence. The [population continuation](POPULATION-README.md) now supplies a separate checked composition of bounded contract replacement, internally financed correction, renewal and actual material-guarded core histories. It adds 71 theorems / 100 audits without changing or recounting this module's 32/41. Institutional formation, protected collection and actual correspondence remain open.
