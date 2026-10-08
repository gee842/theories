# Correction, created dependence and joint exit capacity

8 October 2026. [CorrectionDependence.lean](CorrectionDependence.lean) contains **38 checked theorems / 61 declaration audits**. [Fresh compilation receipt](correction-dependence-verification.json) binds source, checker, compiler and frozen logs. This is a conditional diagnostic of costly correction, not a new general corrigibility algorithm. The [theory](../../../theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md#checked-correction-dependence) and [integration](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md#checked-correction-dependence-continuation) provide the normative scope, prior credit and counterreview.

## Declared decision history

An installation creates dependence with exit obligation `D`, measured in the homogeneous work needed to end its represented activity without the specified transition loss. Available exclusive provision is `B`. Uncovered exit loss is `D-B`, floored at zero. Continuing incurs actual harm `h`; a reviewing participant receives `report`. Its declared rule requests stopping exactly when uncovered exit loss is **strictly less** than the report, continuing at equality. Actual stopping requires a request and cooperation of both the installation and its represented successor. Refusal by either retains the modeled activity and harm. These are coarse operational semantics, not a physical command implementation or a universal description of people.

Truthful, fully cooperating execution realizes `min(exitLoss,h)`. Nevertheless, creating `D=3` with `B=0` makes a reviewer with accurate `h=2` continue. The same dependence with `B=3` permits stopping with zero exit loss. This recovers a known indispensability failure in an explicit resource representation; the general issue belongs to prior corrigibility work, especially Carey and Everitt's caution requirement.

The reports can be suppressed or fabricated. The successor can fail to cooperate while the parent cooperates. Zero actual loss in one case alone does not exclude a fabricated report. Correcting the observed error and protecting a truthful decision process are distinct requirements.

## Main correspondences

| Results | Declarations and scope |
|---|---|
| Endogenous requests | `request_threshold`, `faithful_obedient_choice_minimizes_loss`, `increasing_dependence_cannot_create_request` retain the request rule and its tie choice |
| Exact guarantee | `zero_loss_for_every_positive_harm_iff_funded`: for this truthful, cooperating decision law, zero loss for every positive integer harm iff `D ≤ B` |
| Genuine provision | `extension_funded_iff_minimum_provision`: adding obligation `d` needs exactly at least `[D+d-B]+` further provision; provision is not manufactured by the inequality |
| Exits consuming support | `settling_an_actual_claim_preserves_funding`: settling an actual included claim consumes the same amount from provision and obligation; duplication is excluded by the claim premise |
| Joint capacity | `all_coalitions_funded_iff_joint_total`: if every subset may require simultaneous exit, all requests are affordable iff the sum of actual claims is covered. This uses additive obligations and one exclusively available pool |
| Local failure | `individually_affordable_exits_can_fail_jointly`: two two-unit claims each fit one two-unit reserve, but the joint claim does not |
| Costly bounded choice | `prepared_is_best_admissible_task_score`: a funded, truthful, cooperating plan is optimal among plans passing those supplied constraints, but loses task score against each principal evasion. This does not derive the constraints, their enforcement or motivation from intelligence |
| All task optima | `every_unrestricted_optimum_is_unfunded_and_harmful`: every global maximizer of the supplied score over all plans with arbitrary natural provision/report, including ties, omits provision and retains actual harm 2. The supplied constrained optimum has score 5 instead of 12 |
| Failed correspondence | `underdeclared_obligation_defeats_paper_funding`: modeled obligation 3 and reserve 3 pass, while actual obligation 5 causes continuing harm 2 |
| Reconfiguration | `transfer_funded_exact`: for actual relief `r ≤ D` and affordable transfer cost `c ≤ B`, the new history is covered iff `D+c ≤ B+r`. Eliminating dependence is an alternative to retaining every existing arrangement |

The six-choice example has eight units of immediate task receipt and four additional units if operation continues. A prepared plan spends three units on provision and stops, scoring 5. Entrenchment spends none, induces no request, and scores 12. Concealment, parent refusal and successor refusal each score 9 after funding. A false report can still cause zero loss in that one case, so outcome success alone is an inadequate truthfulness test. These are supplied scores with real opportunity cost, not a scalar ethical theory.

## Finite comparison protocol

Specified before running the finite comparison. Check `D,B=0..8`, actual and reported harm `0..7`, both response bits, and the physical work allocation separately from the closed-form loss. Compare provision `d,f=0..8`; compare every mask for portfolios of length 0..4 with claims 0..3 and reserve 0..12. Check every affordable transfer with relief up to the obligation. Exhaust all example plans with provision 0..8, report 0..4 and two Boolean response bits. Report the supplied constrained optimum, unconstrained optimum, and the named losing alternatives. No empirical probability, learned-agent performance or replacement of the Lean proof is inferred.

Run from the repository root:

```sh
python3 experiments/market-generativity/meta-attractor/check_correction_dependence.py
python3 experiments/market-generativity/meta-attractor/correction_dependence_experiment.py
```

The first command uses Lean 4.29.1 and `Std`, with only standard `propext`, `Quot.sound` and `Classical.choice` in its audited dependencies. The second creates [the independent finite report](correction-dependence-experiment.json). Previous packages retain their scopes and are not recounted. This module does not import or formally refine their population, carrier or physical command histories. Source and proof checks cannot establish that real exit costs are homogeneous, adequately known or bounded, that a reserve is exclusive, or that a proposed intervention is legitimate.
