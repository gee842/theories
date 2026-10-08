# Posted commitments and the limits of instrumental correction

8 October 2026. [CorrectionCommitment.lean](CorrectionCommitment.lean) adds **35 checked theorems / 47 declaration audits**, importing the unchanged [CorrectionDependence.lean](CorrectionDependence.lean). The [receipt](correction-commitment-verification.json) freezes both sources, compiles them in a fresh directory and audits each new declaration; inherited results are not recounted. The [current theory](../../../theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md#checked-instrumental-commitment) and [integration](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md#checked-instrumental-commitment-continuation) retain motivation, authority and institutional assumptions separately.

## The mechanism and actual costs

The previous plan has task score at most 12. Its best affordable, funded, truthful and jointly cooperating plan scores 5. The new mechanism keeps every old plan available. Before choosing, the installation posts a stake `F` under supplied custody. An audit has `n>0` equally likely outcomes, chosen without advance access by the installation. Compliant plans lose the stake on `g` outcomes; violating plans lose it on `b` outcomes, with `0≤g,b≤n`. Every individual realization either returns the stake or transfers it to the custodian; the two amounts sum to `F`. No unbacked penalty is promised. The audit classifier is tied to the previous explicit plan conditions, but acquiring its real-world truth is not solved.

The installation values task return and lost stake linearly in the same units. Stake refund returns its own property, so the original posting and later refund cancel when no seizure occurs. A common audit fee and initial wealth can be omitted from comparisons but remain real budget requirements. Holding costs and risk sensitivity beyond this linear model are absent. These assumptions are material: a goal that does not value the collateral loss need not respond this way.

The sum of actual realized task-minus-confiscation payoffs over the `n` possible outcomes equals the declared score. This is an expectation numerator, not `n` sequential deployments or `n` actual deposits. The audit changes incentives; a missed violation can still leave physical harm. The positive result applies to optimizing choice before the draw, not to guaranteed rescue after arbitrary deviation.

## Exact results

Write `p₀=g/n`, `p₁=b/n` and let `T=7` be the maximum task advantage of violating in the inherited example. Every global maximizing plan satisfies the correction conditions **iff** `(p₁−p₀)F>T`. Lean checks the division-free equivalent `gF+7n<bF` and then invokes the inherited actual shutdown/loss theorem. Equality retains a harmful maximizing tie. An approximate optimizer requires the strict margin to exceed its allowed score error; a half-unit expected error defeats the minimally separated numerical example.

For a general nonnegative scaled temptation `G`, a stake up to available capacity `W` can satisfy `gF+G<bF` iff the maximum stake `W` can. With separately required exit reserve `E` and audit expenditure `A`, and `E+A≤W`, joint feasibility is exactly `g(W−E−A)+G<b(W−E−A)`. Exit provision cannot simultaneously be the stake available for forfeiture in this accounting. A different rule earmarking forfeiture for exit would require its own timing/custody proof.

For `n=2,g=0,b=1,T=7`, stake 14 retains a harmful tie; stake 15 makes every optimum pass. Exit preparation 3, audit cost 1 and stake 15 need 19 initial units; 18 cannot fund all three with a strict incentive margin. Initial liquidity is supplied before the receipts of the modeled activity; its formation is not derived. Deterrence does not establish participation: `n=2,g=1,b=2,F=15` separates compliant and violating choices while every available deployment plan has negative expected score. Abstention with zero score then wins.

Internal transfers cancel in a coalition's joint gain. For integer temptation `T` and external expected loss `L`, a transfer making both parties strictly gain exists iff `L+1<T`; the one-unit gap is an integer granularity effect. If seizure is merely a transfer to a collaborating custodian, it is not that coalition's external loss. Setting actual violating-plan seizure to zero restores the old incentive. These are arithmetic coalition controls, not a general equilibrium or account of which coalitions form.

## Declaration map

| Interface | Main checked declarations |
|---|---|
| Exact optimizing choice | `every_best_passes_iff_separation`, `prepared_best_under_separation`, `entrenched_best_without_separation` |
| Actual correction | `escrow_optimum_executes_previous_correction` |
| Selected plan and resources | `every_best_is_prepared`, `optimum_fits_joint_resource_budget`: for a nonempty audit lottery and strict separation, the maximizing plan is the original three-unit preparation and fits the declared joint budget |
| Real settlement | `settlement_conserves_posted_stake`, `lottery_total_is_declared_penalty`, `declared_score_is_sum_of_lottery_payoffs` |
| Imperfect optimization | `approximate_margin_suffices`, `approximation_can_restore_a_harmful_choice` |
| Finite means | `implementable_stake_iff_available_capacity`, `jointly_fundable_deterrence_exact` |
| Failure conditions | `no_discrimination_no_deterrence`, `lost_custody_restores_old_incentive`, `stronger_temptation_can_exceed_any_fixed_capacity` |
| Participation and coalitions | `abstention_beats_every_plan_in_participation_failure`, `profitable_integer_side_agreement_iff` |

## Pre-execution finite protocol

Enumerate `n=1..6`, every `g,b=0..n`, `F=0..24`, and the inherited 180 plans (`provision=0..8`, `report=0..4`, both response bits). For each plan, execute every possible lottery realization and sum actual confiscations and private returns. Compare every optimizing tie against the exact separation inequality; check approximation allowances 0..3. Enumerate general temptation 0..30, counts 0..5 and available stake 0..20. For combined budgets use wealth 0..20, exit reserve 0..4, audit cost 0..2, temptation 0..20 and counts 0..2; explicitly search feasible stakes. Check integer side payments for temptation and external loss 0..20. Retain the named boundary, false-positive, approximation and participation examples. These are synthetic mechanism checks, not empirical audit calibration or learned-agent tests.

```sh
python3 experiments/market-generativity/meta-attractor/check_correction_commitment.py
python3 experiments/market-generativity/meta-attractor/correction_commitment_experiment.py
```

The [finite report](correction-commitment-experiment.json) binds the protocol, script and both formal sources. The fresh Lean 4.29.1 receipt permits only standard `propext`, `Quot.sound` and `Classical.choice`; no custom axiom, admitted proof or unchecked native shortcut is used. Conventional expected-penalty incentives and coalition reasoning retain their prior credit. This is a composed conditional explanation of instrumental compliance; intrinsic concern, sound open-ended classification, custody formation and arbitrary self-modification preservation remain unresolved.
