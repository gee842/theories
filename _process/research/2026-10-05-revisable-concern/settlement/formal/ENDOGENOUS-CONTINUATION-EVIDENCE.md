# Endogenous continuation: comparators and empirical requirements

6 October 2026. AI-authored supporting audit for **effective justified protection when present decisions change future opportunities or control**. This note supplies primary-source comparators and measurement requirements, not a new experiment, equilibrium proof or ethical foundation.

## What is already established locally

[Settlement REPORT](REPORT.md), §§1,3–4, supplies exogenous contexts and equal operator continuations within its renewable region; R4 already bounds permanent capture without an outside windfall. The [development proposal](../../../2026-10-05-generative-foundation-review/root-foundation/development/GOVERNANCE-CONTINUATION-GAP.md) identifies the narrower cancellation gap.

**[REASON-PROTECTION-MATH](REASON-PROTECTION-MATH.md) already handles resource-dependent continuations.** Its finite game retains physical fuel, source, cash, archive and opportunity state; production failure can remove future inflows, and extra voluntary safeguards remain alternatives. It does not assume equal future resources. The new interface therefore concerns the validity of a proposed protective continuation under additional action-dependent opportunities, oversight or rents. It is not the discovery that present actions affect the future.

## Three source comparators

**One-stage deviation.** Ozdaglar's author-produced MIT [Lecture12](https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/688240e73afefbf4a6293fef0e529398_MIT6_254S10_lec12.pdf), pp23–25, states the criterion for observed-action multistage games and extends it under continuity at infinity. Uniformly bounded stage payoffs with discount below one supply that tail condition. It tests every player and history, with conformity to the proposed strategy after the deviation. This is an authoritative exposition of established game theory, not a new research result.

**Bellman verification.** Bertsekas's author-produced MIT [Lecture15](https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/ec7b70a77571e2f2c48a5a0fa5fa23d5_MIT6_231F15_Lec15.pdf), pp2–4,7,10–12, gives bounded discounted policy evaluation, Bellman optimality, contraction and a policy-value residual bound. Fixed-policy value and optimal value are different objects. The discounted finite-state case is an appropriate conventional comparator; arbitrary governance dynamics do not inherit its assumptions merely by being written as states.

**Instrumental power.** Turner et al., [NeurIPS2021 final paper](https://proceedings.neurips.cc/paper/2021/file/c26820b8a4c1b3c2aa868d6d57e14a79-Paper.pdf), §§3–6, establishes sufficient structural conditions for optimal policies to preserve options. Its comparisons use specified reward-distribution permutation orbits, not observed frequencies of human or learned-agent preferences. Published Theorem6.13 concerns average-optimal policies under copy/disjoint-support premises. Page9 leaves connection to near-one discounted optimality probabilities open; p10 limits extension to learned, partially observed systems. The readable OpenReview submission uses different Blackwell-optimal terminology and must not replace this final result.

## Correct comparison for this interface

Fix an actual decision maker, information/history state, feasible actions, opponents' complete contingent strategies, reward interpretation and discount clock. For proposed protection `p`, deviation `a`, and candidate continuation value `V`, write the actor's comparison as

\[
g(s,a):=r(s,p)-r(s,a),\qquad
g(s,a)\geq\delta\{\mathbb E[V(s')\mid s,a]-\mathbb E[V(s')\mid s,p]\}.
\]

This is our application of the standard comparison. Strict inequality removes that deviation as a tie; it does not establish unique equilibrium globally. The continuation must itself be evaluated under the candidate policy or bounded against admissible alternatives. Assigning a favorable `V` is not verification. A fixed-opponent MDP certifies a best response, not the credibility of all other players' reactions. A subgame-perfect claim needs their decisions checked as well, including off-path histories. Dated trustee selves are not silently replaced by the persistent operator.

The state must preserve information relevant to future feasible actions, observations and payoffs. A Markov compression requires justification. Within-episode moves do not each acquire an extra discount factor unless time actually advances. Costs already paid cannot be refunded by a state reset; a carried cash balance is not an additional receipt at every step. If a deviation destroys future auditing or authority, the resulting branch belongs in the comparison. Current incentive compatibility and continued physical/legal ability to protect remain separate obligations.

Greater patience weights the continuation difference more strongly, but that difference can itself vary with the discount factor and equilibrium selection. No unconditional monotonicity follows. A long future can make preserved cooperation valuable or make durable domination lucrative under different specified incentives. Neither conclusion creates another person's standing.

## What empirical evidence would have to identify

| Quantity | Required observation or independently defended bound |
|---|---|
| Current margin | Actual receipts, payments, delays and feasible alternatives, attributed to the decision maker; distinguish money from inferred utility. |
| State transition | Effect of the action on audit access, authority, enforcement, information, resources and future opportunity; action-conditioned association alone may reflect selection. |
| Continuation | Measured outcomes under a stated subsequent policy, or conservative bounds including off-path states; disclose censoring and institutional change. |
| Valuation/time | Independently identified objective or admissible preference set and horizon/discount range; do not choose them to make protection optimal. |
| Protection | Recipient-specific consequences and continuing access to remedy, recorded separately from operator return. |

For a genuinely bounded flow objective, known lower/upper flow bounds give a conservative continuation-span bound; transition uncertainty can then widen the required current margin. Bellman residual bounds are useful only when residuals cover the relevant state/action domain under a justified transition model. A low on-policy prediction error cannot certify unseen capture branches. When utilities or transitions are only partially identified, test the inequality over the retained set or report the region left undecided. A sufficiently profitable feasible counterexample can reject a proposed certificate; selected protected trajectories cannot establish its universal validity.

Existing AgentDojo traces and the Robodebt implementation reports do not identify the required opponent discount, private utility and causal continuation law. They can motivate omitted states and endpoints; this note extracts no empirical continuation estimate from them. Operator utility is a behavioral/model input, never a definition of justified protection, patient welfare or legitimate authority.

## Access and version limits

MIT materials were read through the official PDF text reader. Lecture12 p25's extracted inequality points opposite to p23 and its verbal no-gain criterion; no uninspected glyph is used as proof. The comparison above uses the no-profitable-deviation orientation. Blackwell1965's publisher page returned only an iframe and its download route failed; Hendon–Jacobsen–Sloth1996 was accessible only at abstract level, so neither supplies an uninspected theorem here. One mistaken MIT link resolved to a blocked donation page; it supplied no evidence and caused no transaction.

The final Turner PDF was successfully retrieved and visually inspected on pp1–3,6,8–10 after empty text extraction. Its [minimal source package](../../../../../sources/35-endogenous-continuation-comparators-2026-10-06/README.md) preserves exact bytes and scope. No supplementary-proof audit, new model run or empirical prevalence finding is claimed.
