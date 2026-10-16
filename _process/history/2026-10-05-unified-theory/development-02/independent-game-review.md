# Independent joint-formation game review

Verdict: **ACCEPT for implementation consistency with the declared finite game.** No implementation blocker was found. This is an exact mathematical/software check, not empirical validation, a proof about arbitrary institutions, or certification of indefinite renewal.

Reviewed production file: `/Users/ren/theories/experiments/joint-formation/model.py`.

Production SHA-256: `b8e5fed50c9d8056ea4ba80daec4dac2f79d1b1143484d60a8e043828784b77b`.

The interpretation follows `PROTOCOL.md` frozen at `8a5bf6f` and `TIMING-CLARIFICATION.md` at `5f40dc0`. The independent implementation is `independent_game_check.py`; machine-readable output is `independent-game-check-results.json` in this directory. Production decision logic is imported only by the comparison adapter, after the independent reference and accounting functions are defined.

## Reconstruction and checks

The independent reference reconstructs backward induction from feasible payments, physical admission/harm transitions, and each decision maker's objective. It does not call production `Game` or its decision helpers to calculate reference outcomes. Both trustee selves maximize their own current episode objective; only the operator values future episodes. The cold self anticipates the later warm self, while the warm self uses the newly learned concern coefficient. These distinct objectives must remain explicit.

All **484** comparisons matched exact rational operator values and complete realized path dictionaries. They cover **1,264** realized episodes, **241** fresh-operator cases, **243** persistent-operator cases, and **250** cases with reversed tie priorities. The selected test set consists of nineteen named controls at horizons 1, 2, 3, and 6, both operator discounts, and both tie orders, plus 180 deterministically sampled grid cases. It is independent selected-case verification, not a second execution of the entire main grid.

The accounting check independently verifies each cash prefix, feasibility of paying the lesson before its private return, identity filtering after that return, apparatus charges, actual receipts and patient harm, next-episode account rollover, learned coefficient products, and the discounted sum of operator payoffs. The checked controls intentionally include **58** episodes in which operation is unaffordable.

The default four-episode case independently yields shared learning, verified gate construction, and operator safeguarding in every episode, with no preattack. Closing balances are `10, 15, 20, 25`; the operator's discounted value is `45/8`. Apparatus and learning are repurchased each episode. No inventory, permanent learned trustee, or free gate survives succession.

## Discriminating controls

The following are named three-episode persistent-operator runs under default tie selection. Other horizons and reversed selections were also checked.

| Control | Independently verified behavior |
| --- | --- |
| Cheap reserve raid | Repeated destruction of two cash units prevents learning each episode; three harmful productive episodes result. |
| Expensive reserve raid | No raid; all three episodes protect the patient productively. |
| Zero learned value, or zero recipient alignment | Commercial learning persists, but no protective apparatus is purchased and harm occurs. |
| Concern coefficient 6 | All three episodes protect productively at the primary apparatus price. |
| Zero private learning return | No learning and no protection. |
| Free identity gating | The cold self chooses filtered learning; no patient protection. |
| Cheap alignment capture | Capture eliminates recipient routing while retaining the commercial return; no protective apparatus is bought. |
| Cheap bypass, unauthenticated cue only, or no control | Anticipated ineffectiveness prevents apparatus investment; the realized path may contain no actual bypass or mask. This is deterrence failure, not absence of an available attack. |
| Poor initial account | The first episode does not learn; its production receipt finances protection in subsequent episodes. |
| Bootstrap trap | A smaller production receipt leaves the account below the lesson payment threshold indefinitely within the modeled horizon. |
| Resource failure | The first harmful episode is followed by inability to operate. Later recorded zero harm is not successful productive protection. |
| Partial learning factors | With the same product of learning factors, the primary protection path is recovered. |
| Zero operator rent | Default tie selection chooses harm among equally profitable zero-payoff alternatives. Reversed ties can select different actions; this boundary is not a strict prediction. |

The script also checks a high-subsistence transition control, internally named `gate_then_failure`. That label is only a case identifier: its three-episode persistent default path is preempted by alignment capture and does **not** demonstrate a verified gate followed by failure. No result should infer behavior from the case's label.

## Material premises and limits

1. **Available self-insulation mechanisms are restricted.** The cold self can choose the modeled shared and identity-filtered architectures. It cannot freely precommit the future warm self to open production, dispose of the gate authority, or lock the relevant budget away while keeping the same commercial return. These are substantive restrictions on the architecture repertoire.

   In the primary episode, the protective route closes with `W − ell − a + R − D + b`. A feasible commitment preserving the commercial return and forcing open production at cost `s` closes with `W − ell − a + R − s + b`. Therefore the money-only cold self strictly prefers the latter whenever `s < D`. At `s = 0`, the primary case closes with 13 rather than 10 and formation fails even when identity filtering is expensive. For positive `s`, the mechanism must also satisfy its stated payment timing and liquidity constraints; the zero-cost counterexample needs no extra initial funds. Equality gives indifference, not unique protective selection.

   Thus the scope condition is that the **least available effective means of avoiding the future protection expenditure while retaining the commercial return is sufficiently costly**; `s > D` gives the strict comparison against such an alternative. The current game enumerates particular alternatives, not all possible self-insulation methods. A countermodel adding inexpensive commitment should be presented separately from the frozen main grid. The protective outcome is conditional institutional selection, not a universal consequence of selfish learning.

2. **Evidence here is a verification technology with strategic use.** The game has perfect information about deterministic primitives. The paid apparatus supplies a truthful action-contingent signal to a binding gate; it is not Bayesian discovery of an unknown hazard or unknown intervention efficacy. Learning of the concern coefficient is separate. The nondestructive probe, truthful verified signal, and the physical force of the gate are admitted primitives.

3. **Alignment capture is selective.** It blocks recipient routing while preserving the private commercial return. That distinction explains why corrupted learning can still be purchased and cannot be silently generalized to attacks destroying every kind of useful learning.

4. **Renewal uses an inherited account and supplied installation rights.** Trustees start without learned concern, and evidence/control must be repurchased. Cash nevertheless passes to a successor through the given account. Private extraction, refusal to bequeath, origin of gate authority, and endogenous inheritance law are not solved by this game. The operator has no modeled liquidity constraint.

5. **Inability to operate has a narrow meaning.** If postattack cash is below subsistence, the residual account is carried forward, subsistence is not paid, and modeled patient harm is zero. This is a cessation convention rather than a model of starvation, death, patient welfare, or a successful protective institution. The reported controller net cash excludes the separately recorded reserve destruction; comparisons of total account change must use opening and closing balances or add that destruction explicitly.

6. **Tie priorities select equilibria.** Exact equality is resolved by declared action order, with a reversed-order sensitivity run. A strict positive region can support a robust qualitative claim; equality cases cannot establish unique architecture, attack, or protective choice. Persistent-versus-fresh comparisons concern different operator objectives, and neither is a generic policy-quality ranking.

The declared primary mechanism remains internally coherent with these qualifications: privately valuable learning can create a concern coefficient; a later self can pay for verified control; that control can induce a strategic operator to safeguard; and a sufficiently replenished inherited account can finance repetition. The audit does not establish that these prerequisites arise under every broader action repertoire.
