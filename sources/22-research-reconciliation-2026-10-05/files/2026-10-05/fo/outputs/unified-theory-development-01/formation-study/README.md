# Constructed alternatives and strategic correction

This exact finite game tests how a participant's constructed alternative changes an operator's choices, and how the operator can change the participant's future ability to pay for that alternative. Research direction: Yongxu Ren; AI-assisted implementation and analysis, 5 October 2026. The [protocol](PROTOCOL.md) was committed as `1929eb5` before enumeration. Results are authored model cases, not measurements of real institutions.

The [theoretical report](<../FORMATION.md>) and [proofs](<../FORMATION-MATH.md>) explain the mechanism. Earlier [continuing participation](</Users/ren/theories/experiments/continuing-participation/README.md>) work already establishes compensation, participation, and dated liquidity distinctions; this study adds actual alternative construction and strategic interference with future operation.

## Main result

In the strict public one-period game, an activated alternative induces safeguarding exactly when safeguard cost is below both lost operator rent and the cost of blocking the alternative. With persistent control, an operator can pay more now to leave the participant unable to fund later resistance.

For a proved two-period class, first operation needs reserve `K+m+ell`; immediate operation resilient to the specified financing attack needs `K+2m+ell`. The focal example has thresholds four and five. With initial reserve four, a fresh operator safeguards twice; a persistent operator deters early activation. One extra unit restores immediate protection. The anticipated blockade is absent from the optimal realized path, although it explains that path.

![Exact model results](results/formation-and-strategic-reserve.png)

## Reproduction

The game and independent checkers use Python's standard library and exact rational arithmetic:

```text
python3 study.py
python3 independent_game_check.py
python3 check_formation_math.py
python3 formal_adversarial_check.py
```

The optional figure script additionally needs matplotlib and numpy:

```text
python3 plot_results.py
```

No original study module is imported by the independent reference implementation; it reconstructs the game first, then compares against `model.py`. The separate analytical checker imports no study code.

## Completed scope

| Record | Scope |
|---|---|
| [Summary](results/summary.json) | 1,152 parameter cases; 9,216 grid policy runs; 2,304 operator tie-sensitivity runs |
| [Full parameter grid](results/grid.json) | Every case, participant-policy outcome, and tie-sensitivity flag |
| [One-period games](results/static-games.json) | 480 complete equilibrium correspondences, including 116 strict theorem checks |
| [Named witnesses](results/witnesses.json) | Nine detailed control cases with all selected trajectories |
| [Succession](results/succession.json) | 36 handoff and successor-control cases, each under both operator environments |
| [Additive control](results/additive-control.json) | Why an equally available nonrival benefit cancels from the refusal comparison |
| [Independent game audit](independent-game-check-results.json) | 1,269 dynamic comparisons, 128 static correspondences, 42 strict checks |
| [Additional adversarial checks](formal-adversarial-checks.json) | 2,100 rational cases, including fractional reserves and exact boundaries |
| [Independent analytical checks](math-proposal-checks.json) | 1,728 stage games, 30,375 prefix cases, 243 two-period theorem cases, 1,458 reserve variations |

## Decision rules and scope details

`optimal` chooses upkeep and input allocation using full continuation value. `myopic` chooses both using current-period participant payoff, anticipating the operator response to its declared future behavior. `always` chooses the cheapest affordable active action and allocates input by current payoff. `never` chooses no construction or activation and allocates input by current payoff. Thus the heuristic comparisons change more than the quality of an optimizer. Operator behavior is recalculated in each environment; the rows are not a benchmark proving a proposed wisdom method beats algorithms solving the same optimization problem. An independent sensitivity check found differences in 9 of 432 cases when heuristic input allocation instead used continuation value, so this definition matters.

A fresh operator maximizes its current receipt. Its reported total operator value sums different actors' receipts; it is not one actor's continuation objective. A persistent operator maximizes its own remaining discounted receipts. All states and implemented actions are public; sensing, discovery, and the learning or computational cost of solving the game are not derived. The exact optimizer is an analytical benchmark under stated rationality assumptions.

The default tie order is harmful offer, blockage, safeguard for operators. Participant upkeep ties favor lower immediate expenditure, then retained access, then action name; input-allocation ties favor participation. This selects an equilibrium rather than enumerating every dynamic equilibrium. Reversing operator tie preference changes a recorded outcome in 97 of 2,304 grid environments. The strict two-period witness is unchanged. Full one-period correspondences retain all pure equilibria, including off-path participant indifference.

All subsistence, construction, activation, and handoff bills are prefunded. Every realized cash prefix and discounted payoff was checked. Terminal cash is not counted twice: at discount one the participant value equals final cash minus initial cash. A voluntarily chosen input allocation leaving less than the next subsistence bill ends modeled operation with zero further payoffs. No selected path in the main or independent checks reaches this boundary; the guaranteed baseline receipt covers subsistence. This convention is not a model of death or an ethical valuation of it.

Handoff preserves actual access at a cost, and rebuilding remains available. Where `J>K`, rebuilding can cap the burden of transfer; high handoff fees therefore need not eliminate operation. Continuing participant preferences and the receipt allocation persist through these transitions. Voluntary bequest, new successor preferences, evolving control rights, unknown harms, confiscation of the input itself, and unlimited horizons remain outside the result.

The supplied physical control assumptions are substantive: one rival input can be withheld; safeguard implementation is observable and precedes input delivery; interference has a stated real operator cost; productive opportunities recur; operator liquidity suffices. The result is a conditional explanation of selected protection, not an origin of these technologies or rights. Safe independent exit is reported separately from protected cooperation.
