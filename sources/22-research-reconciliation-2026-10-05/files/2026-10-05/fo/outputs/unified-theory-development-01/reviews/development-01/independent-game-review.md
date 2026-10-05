# Independent strategic game audit

5 October 2026. Reviewed `experiments/constructed-correction/model.py` against its frozen `PROTOCOL.md`. The reviewed model SHA-256 is `29745b50a9eaa07e76e45373022f9b5e99b284c60c8a3e79e2ea0a629222b92b`.

**Verdict: the implemented exact finite-game recursion matches the independently reconstructed semantics in the tested cases. The main strategic-depletion witness is reproduced and unchanged by reversing operator tie preference. No blocking implementation error was found.** This is computational verification of an authored game, not empirical validation or a theorem about real institutions.

The [independent reference](<../../formation-study/independent_game_check.py>) builds separate budget, operator, and allocation nodes, then recursively resolves decision owners' objectives. Its definitions precede importing the production code; it does not call production `Game`, `choices`, `operator_moves`, or `Result` when generating reference outcomes. Import is used only for subsequent comparison. All arithmetic is rational. The [complete results](<../../formation-study/independent-game-check-results.json>) record code hashes and witnesses.

## Checks completed

- 1,269 dynamic comparisons over horizons one to three, initial cash and construction/upkeep ranges, fresh and persistent operators, all four participant policies, operator tie reversal, discounts one and three quarters, zero rent, and stronger alternatives.
- 128 complete one-period pure equilibrium correspondences, including off-path response ties, independently enumerated.
- 42 checks of the three strict one-period regions: safeguarding, blocking, and departure.
- Succession cases with initial ownership, handoffs in successive periods, bills zero/one/three/six, cheaper rebuilding, actual lapse, and changed successor interference costs.
- Every realized payment fits current cash; input is allocated only once; receipts reflect effective activation and interference; cash rolls forward correctly; discounted flows equal reported participant and operator values. At discount one, participant value equals final minus initial cash, which verifies that terminal wealth is not counted twice.
- No selected path reaches the explicit cessation rule. The reference retains that off-path rule and reproduces it as zero subsequent modeled payoffs.

## Main witness

With the protocol's two-period parameters and cash four:

| Environment | First action | First operator action | Participant value | Operator receipt sum |
|---|---|---|---:|---:|
| Fresh operator each period | Build and activate | Safeguard | 3 | 6 |
| One persistent operator | Stay inactive | Harm | 1 | 7 |
| Persistent operator, forced activation whenever affordable | Build and activate | Block | −2 | 13/2 |

The optimal persistent participant postpones construction until the second period. In the forced early-build continuation, interference leaves cash two, which can fund subsistence but not next-period activation. The operator's combined receipts are then larger than after immediate safeguarding. This is a real intertemporal distinction inside the declared game. The optimal participant anticipates it, so the main equilibrium path contains no observed first-period interference. This should be described as deterrence of formation, supported by an off-path credible intervention, rather than as observed first-period repression.

The identical selected fresh and persistent paths and values were reproduced with reversed operator tie preference. This protects the announced witness against that particular tie convention. It is not a general all-equilibrium statement for every parameter case.

## Baseline meaning that needs explicit reporting

The implementation makes final input allocation depend on current-period payoff for `never`, `always`, and `myopic`; only `optimal` uses continuation payoff. At the initial expenditure choice, `myopic` maximizes current payoff, `always` forces activation when affordable, and `never` restricts the available actions to idling/lapse. This is coherent once declared, but it is more specific than describing `always` as only an activation restriction.

I separately changed input allocation to the full remaining value in the independent reference, while preserving those fixed upkeep policies. Of 432 sensitivity comparisons, nine changed their selected outcomes. Thus the allocation convention is not automatically harmless. For example, a forced-activation participant may select harmful participation to avoid acquiring enough cash for another costly forced activation; a current-payoff allocator instead threatens departure, requiring the operator to block. The coordinator has confirmed the intended baselines include current-payoff allocation and will report that fact.

A precommitted heuristic can also change the operator's incentives. Consequently, comparisons across these policies are comparisons of different specified strategic responses; they are not a proof that an optimal participant weakly dominates every commitment policy in the same game. The main fresh-versus-persistent conclusion compares the same continuation-optimizing participant on both sides.

`vo` for fresh operators sums the realized receipts of successive one-period operators. It is a useful accounting quantity, but is not the utility of one decision maker optimizing that sum.

## Modeling boundaries

The game assumes completed observable safeguards, rival input control, a supplied action repertoire, adequate operator liquidity, effective instantaneous rebuilding, and declared access/handoff/interference technology. It does not establish the origin or legitimacy of these controls. A temporary block disables the alternative for the current period without destroying the installed asset; future influence is lost through operating liquidity. Describing it as confiscation of the durable asset would be inaccurate.

The termination branch explicitly stops future receipts and future subsistence rather than assigning a welfare penalty for death or deprivation. The production comment mentioning a “terminal failure penalty” is inaccurate wording; the actual rule is zero continuation. The tested core region avoids it on selected paths. Claims about broader parameter regions require reporting whether that convention begins selecting behavior.

The participant ordering selects lower current expenditure, retained access when the bill is tied, and then lexicographic action names. Allocation ties select participation. Operator ties use the chosen ordering. Enumerated point outcomes therefore select equilibria. Strict-region theorems and the specific tie-robust witness are stronger than the broader selected-grid counts and should remain distinguished.
