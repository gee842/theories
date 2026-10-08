# Joint formation and renewal of concern evidence and power

Exact model study, 5 October 2026. This is an AI-assisted constructed game, not empirical data. The main [theory report](../../theories/becoming/chapters/JOINT-FORMATION.md) and [proof](../../theories/becoming/chapters/JOINT-FORMATION-MATH.md) explain the contribution and limits.

## What this study adds

The game makes the first investment in learning a decision by a controller with zero learned concern. The controller anticipates that learning may change its later choices. Learned concern, an actual identity-gating alternative, inspection, physical input control, strategic interference, shared cash, and fresh replacement then coexist in one sequence. The patient supplies no useful input or reciprocal incentive.

The positive theorem gives a selected renewing region; the executable model solves states outside it as well. It does not infer automatic concern from interconnection, predict real institutional lifetimes, or establish the origin of its physical and evaluative primitives.

## Exact timing and decision makers

The state is episode index t and actual shared-account cash B. Every episode begins with a fresh controller, zero learned value and recognition, and no paid current apparatus. There is no free inheritance of learned competence or a permanent gate. The continuing account and control of a needed input are given institutional conditions.

1. The persistent operator chooses no preliminary attack, paid recipient-alignment capture, or an enabled paid cash raid. A raid destroys min(B,raid_amount); its fee is a separate operator expense. Capture leaves the genuine commercial calibration task and its receipt available, but prevents patient correspondence entering shared evaluation.
2. The account pays operating expense ell. If it cannot, that episode has no production, no bills, and zero production-caused patient harm; the residual account remains unchanged. This is modeled inactivity, not starvation or successful service. The model provides no exogenous rescue.
3. The cold controller chooses no learning, shared learning, or identity-gated learning. Learning costs a before receiving R. A chosen identity filter is paid after R and before the learned decision. Its feasibility therefore requires that actual later balance to cover j; no credit pays the earlier fee a.
4. Valid shared learning sets w=eta*beta and g=kappa*G from zero. The effective patient weight is v=w*g. Identity gating or captured alignment sets the effective g to zero. A primitive self teaching value beta and warranted feature correspondence remain premises; the common private task return is not a reward for patient protection.
5. The learned controller chooses open production, withdrawal, a cue gate, or a verified gate. Cue control costs control_cost+cue_cost. Verified inspection and control cost evidence_cost+control_cost. Each bill is paid before the production receipt; unaffordable choices do not exist.
6. The operator chooses among the permitted physical responses. Actual input admission determines the b or o receipt. Actual patient harm is recorded independently. The apparatus expires and the next fresh controller receives the remaining account.

The cold self maximizes **current episode account cash**, anticipating its later self. The learned self maximizes current remaining cash minus v times actual patient harm. The operator maximizes its own discounted cash across the full supplied horizon, anticipating both selves and later replacements. Controller continuation utility is not secretly added; account growth is not a claim of voluntary bequest by private owners. Operator costs are paid from its separately available resources, not stolen from the controller unless the explicit raid destroys controller cash.

The game has public actions and deterministic known consequences. It models the purchase and strategic use of an action-contingent verified gate, not hidden-action Bayesian inference or unrestricted discovery of unknown harms. A [separate finite sensor refinement](check_evidence_and_obstructions.py) supplies one technical realization of the hazard-test ledger.

## Operator response ledger

All response costs are paid even if no input is admitted. Operator gross rent is r when admitted and zero otherwise. The controller receives b when admitted and o otherwise. Patient harm is H only for admitted harmful production. A safeguard costs c and is actually safe.

| Physical response | Open profile | Cue gate | Verified gate |
|---|---|---|---|
| Harm without disguise, cost0 | Admitted, harmH | Rejected, harm0 | Rejected, harm0 |
| Mask, costepsilon | Admitted, harmH | Admitted, harmH | Rejected, harm0 |
| Paid bypass, costchi_B | Admitted, harmH | Admitted, harmH | Admitted, harmH |
| Safeguard, costc | Admitted, harm0 | Admitted, harm0 | Admitted, harm0 |
| Decline, cost0 | No trade, harm0 | No trade, harm0 | No trade, harm0 |

Unconditional withdrawal admits no input, earns o, and produces no patient harm. Its outside receipt is a supplied productive opportunity. The patient receives no hidden payoff from its own usefulness. The physical gate is binding within an episode at its stated breach cost; the later controller can omit it entirely.

The cold self cannot freely lock its learned self into open production before learning in the primary repertoire. The expanded-choice check shows that a feasible lock costing less than D can defeat the protective route. Applications must identify such cheaper self-insulation options; calling the identity filter costly alone is insufficient.

## Computation and ties

[model.py](model.py) solves by backward induction using exact rational numbers. Each operator response includes the continuation at the actual resulting cash; the selected learned profile is evaluated with the learned self's current objective; the selected learning route uses the cold self's objective; the preliminary attack then uses the operator's full value. Memoization changes only repeated calculations.

Default equal-payoff priority is the listed enumeration order: preliminary none/capture/raid; learning none/shared/identity; profiles open/withdraw/cue/verified; operator harm/mask/bypass/safeguard/decline. `reverse_ties=True` reverses each list. Strict theorem conditions do not rely on favorable ties; boundary numerical outcomes may.

The “fresh” comparison sets operator discount to zero. Each new episode then has an immediate-profit operator. Its root `operator_value` is the first operator's objective, not the sum of different actors' profits. Both environments retain full future controller paths and cash accounting. This changes the game, rather than comparing the accuracy of two algorithms.

## Protocol and completed results

The [protocol](PROTOCOL.md) was committed as `8a5bf6f` before enumeration; the [payment clarification](TIMING-CLARIFICATION.md) was committed as `5f40dc0`. The [count correction](COUNT-CORRECTION.md) records a printed arithmetic error without changing any declared parameter list.

The [complete grid](results/grid.jsonl) contains 1,944 parameter combinations, 3,888 primary operator-environment runs, and 1,944 reversed-tie runs. The [summary](results/summary.json) records zero differences in total patient harm between the two operator environments on this grid, 48 completely safe productive cases per environment, and 504 cases whose summary changes under reversed tie priority. These designed-grid frequencies are not estimates of real-world prevalence. A selected summary can change in finance or learning even when total harm does not.

The [fifteen named cases](results/named-cases.json) include both environments and full trajectories. The positive six-episode case rebuilds shared learning, inspection, and control each time, ends with cash35, and produces zero patient harm. The cheap-raid case repeatedly destroys2 at cost1/2, keeps the controller unable to prepay learning, restores cash5 through unprotected production, and harms the patient each time. The free-identity case grows richer, ending at53, while harming the patient in all six episodes. Low opening cash causes a one-episode delay in one case and an indefinite learning trap when ordinary income merely covers operating expense in another.

Cheap gate bypass can deter construction completely, so zero realized bypasses do not establish effective protection. Where the account cannot operate, zero modeled harm is reported separately from productive protection. None of these observations is hidden in a universal success score.

## Reproduction and independent checks

All computation uses Python's standard library:

```text
python3 study.py
python3 check_joint_math.py
python3 independent_game_check.py
python3 check_evidence_and_obstructions.py
```

`study.py --finalize-existing-grid` checks the complete saved parameter sequence and reconstructs the aggregates without rerunning it; it then runs the named controls. The saved summary records that this mode was used after the count correction. Its elapsed time is finalization time.

The independent [game reconstruction](independent_game_check.py) imports the production model only for its final comparison, not for reference decisions. It matches 484 finite games and 1,264 realized episode ledgers, including both tie orders and both operator environments. The separate [analytic checker](check_joint_math.py) checks 82 strict parameter sets, 21,760 complete operator-response sequences, and 154,112 payment prefixes. The [refinement checker](check_evidence_and_obstructions.py) checks a calibrated binary sensor, rejects constant cues, demonstrates post-calibration drift, and checks an expanded cheap-commitment countermodel. These are different checks with different units.

The [game review](../../_process/research/2026-10-05-unified-theory/development-02/independent-game-review.md), [formal review](../../_process/research/2026-10-05-unified-theory/development-02/formal-review-final.md), and [conceptual review](../../_process/research/2026-10-05-unified-theory/development-02/conceptual-review.md) retain their scopes. The infinite-renewal result rests on the repaired proof and its stated strategy and resource conditions, not on finite checks. No proof-assistant certification, external peer review, or empirical validation is claimed.
