# Initial formal audit of the joint formation theorem

5 October 2026. Reviewed `joint-formation-math.md` against the production game's timing and action structure. This is an internal mathematical review, distinct from an independent implementation of the full finite game.

## Verdict

**The main theorem appears repairable and no counterexample has been found, but the present infinite-game proof should not yet be accepted as written.** Its Bellman-contraction argument verifies a discounted best response after trustee strategies are fixed. That fact does not by itself establish all trustee deviations or an equilibrium of the whole dynamic game. A complete repair is available through off-path payoff bounds, finite-horizon induction, and a discounted limit. The expensive-raid bound is sound once embedded in that repaired induction.

Two smaller model-alignment issues also need correction: the written witness charges cue fee one, while the production witness charges control fee two plus zero cue fee; and evidence alone is an additional analytical action absent from the production code. The latter can be retained as a dominated extension in the theorem class, but cannot be claimed to have been tested throughout the full computational grid.

## 1. Finance identity and the relevant invariant

The prefix condition

\[
B_* = \ell+a+\max(0,D-R)
\]

is correct: the lesson requires B>=ell+a before its receipt, and the gate subsequently requires B-ell-a+R>=D. Under R-a>D, D<R and B*=ell+a.

For a shared learned controller using the verified gate, both admitted and refused production leave

\[
B'=B-\ell-a+R-D+y,\quad y\in\{b,o\}.
\]

The stated R+o>=ell+a+D therefore ensures B'>=B>=B*. Shared calibration with disabled alignment and an open profile also keeps every operator response in this region because it omits the D payment.

This invariant does not automatically cover every deviation by a trustee. A no-lesson branch or an expensive identity/gate branch can leave the region. Therefore the proof cannot assume that their continuation values equal V*. This is exactly where payoff bounds must replace the unproved equality.

## 2. Off-path comparisons that repair trustee optimality

Let M=B-ell-a+R be cash after valid shared calibration and before the warm decision. Suppose the verified profile induces safe production. Its warm score, after removing the common M, is b-D.

For an open profile, safeguarding is strictly dominated for the operator by harmful admitted production: both give the same trustee receipt b and hence the same next cash, but harm saves c. This comparison does not require any hypothesis about the continuation value at that cash. An optimal operator action can therefore produce either admitted harm or refusal, but not an otherwise identical costly safeguard. The warm score is bounded above by max(b-q,o), which is strictly below b-D under q>D and b-D>o.

For a cue profile with positive fee d_C, an admitted mask costs epsilon<c, yields the same receipt b and next cash as a safeguard, and causes harm. Thus safeguarding cannot be an optimal response. The warm score is at most max(b-q,o)-d_C, again strictly below b-D. A cheaper admitted bypass only strengthens this conclusion. For evidence alone with a positive fee and no input restriction, the same argument gives an upper bound max(b-q,o)-d_E. These bounds allow the operator to prefer refusal for any strategic reason; they do not assume that it myopically chooses harm.

For the cold self, no calibration can never yield closing cash above

\[
B-\ell+b,
\]

because every profile expense is nonnegative and b>o. Identity-gated calibration can never yield more than

\[
B-\ell-a+R-j+b.
\]

Safe shared calibration gives B-ell-a+R-D+b, strictly exceeding the first bound by R-a-D and the second by j-D. These inequalities hold regardless of how the operator behaves in off-region continuations. If an identity option is unaffordable, removing it creates no difficulty.

When teaching is disabled, shared calibration gives q=0. The open profile under the candidate high-region continuation attains the upper bound M+b. Every nonzero-fee profile gives less and withdrawal gives less because b>o. No lesson and identity calibration are likewise inferior. This establishes the trustee response to the pre-learning attack, rather than inserting that response by declaration.

These are sufficient off-path bounds; the theorem need not pretend that all off-path states are viable or solve them by the same formula.

## 3. A full finite-horizon induction

Define S_N=sum_{t=0}^{N-1}delta^t and V_N=(r-c)S_N, with V_0=0. Induct on the number N of remaining episodes for every B>=B*.

1. After valid shared calibration and a verified gate, all operator responses lead to B'>=B*. By the induction hypothesis their continuation values equal V_{N-1}. Therefore the operator strictly safeguards: r-c exceeds r-chi_B and zero.
2. The off-path bounds above now make the verified profile strictly optimal for the warm self, and shared calibration strictly optimal for the cold self, without needing continuation equalities for their other branches.
3. If alignment is disabled, shared calibration and an open profile lead to the same high-region continuation after either receipt. Current harmful production uniquely beats costly safeguarding and refusal. The trustee choices used for this attack are optimal by their cash bounds.
4. At the opening operator decision, no attack gives r-c+delta V_{N-1}; alignment disablement gives r-chi_E+delta V_{N-1}. The first is strictly larger.

Thus the entire N-episode game selects the stated protected process and has value V_N on the region. At N=1 no continuation hypothesis is needed, so the induction begins. If additional off-path subgames contain ties, any specified optimal tie selection is acceptable; strict selected actions on the claimed protected path remain unchanged.

The model has finite action sets at every decision node. Backward induction solves finite off-region subgames separately, so their equilibria exist even though the proof never assigns them the high-region value.

## 4. Repairing the infinite persistent-operator claim

The existing contraction paragraph is correct only as a best-response statement for a fixed trustee policy. It can remain as an additional verification after the whole strategy profile is justified, but should not be the only bridge to an infinite-game equilibrium.

One adequate existence argument uses the finite equilibria just constructed. For a fixed initial state, the infinite history tree is finitely branching and has countably many finite decision nodes. Extend each finite-horizon equilibrium arbitrarily beyond its terminal horizon. A diagonal subsequence then converges pointwise at every finite node to a pure strategy profile.

The operator's one-period receipts are uniformly bounded above and below because the repertoire and all its per-episode costs are finite constants. For delta<1, the tail of its discounted payoff is uniformly bounded by a constant times delta^N/(1-delta). Each dated trustee's payoff depends only on its finite current episode. Consequently an improvement by either a dated trustee or the operator in a limiting subgame would yield an improvement in sufficiently long finite games: stabilize the relevant finite prefix and make the operator's remaining tail smaller than the alleged gain. This contradicts finite-game subgame perfection.

The limit is therefore a subgame-perfect equilibrium of the infinite game. All finite equilibria choose the strict protected process on B>=B*, so their limit does too. Its operator value is (r-c)/(1-delta), and the same cash invariant covers every date. This proves existence of the claimed selected process; it need not claim uniqueness of the entire off-path infinite equilibrium or of every stationary strategy.

The argument is for a fixed declared perfect-information game. It does not cover an omitted private-information game, arbitrary unbounded attack costs or receipts, or undiscounted infinite operator utility. The separately stated finite-horizon delta=1 case remains valid.

## 5. Destructive raid extension

The sufficient bound k>c/(1-delta) is valid, but should be incorporated into the induction rather than invoked as a detached comparison against an assumed baseline.

With N periods left, the operator's total return after paying a destructive raid cost k at the current opening is at most

\[
rS_N-k,
\]

under every subsequent behavior of every actor: its pre-cost stage receipt is at most r, and all later costs are nonnegative. Under the induction above, declining the raid and following the selected protective continuation attains

\[
(r-c)S_N.
\]

The raid is therefore strictly inferior whenever k>cS_N. The uniform discounted bound k>c/(1-delta) makes this comparison hold at every finite remaining horizon. Other trustee deviations are still bounded by Section 2, regardless of how raids change off-region operator behavior. The finite-game induction and the same discounted limit then cover the enlarged game.

An equivalent first-destructive-attack argument can be used after the equilibrium is constructed. Before that first attack, temporary deviations along the selected trustee policy cannot earn more than the protected stage profit or escape the region. At the destructive attack date, the remaining maximum gain is c/(1-delta), below its price. Merely saying that one raid is expensive, while leaving prior policy selection unjustified, would not suffice; the repaired induction supplies that missing link.

This bound permits the raid to destroy the entire subsequent protection capacity. It requires the stated universal per-period gross-profit cap r and positive immediate payment k. Loot returned to the operator, a larger subsequent productive opportunity, or an attack financed by later receipts would change the bound or timing. It is sufficient, not necessary.

For the witness delta=1/2 and c=1, a cost-three raid passes the bound two. A cost-one-half raid destroying two units can instead implement the W=5 to W=3 to W=5 harmful cycle; that adverse game still requires its own continuation solution and is not ruled out by the positive theorem.

## 6. Model correspondence edits

- Set the mathematical witness's cue fee to **two**, matching production's control_cost=2 and cue_cost=0. Its masked warm score is then 5-3.5-2=-0.5, rather than 0.5. Both remain below the verified score two; the theorem is unchanged.
- Label evidence alone as an optional analytical extension, absent from the frozen production menu. The off-path bound proves it cannot displace the verified action in the theorem class. Do not claim that the finite-grid program explicitly enumerated it, or that the same simple dominance reasoning applies to every parameter regime and strategic continuation outside the theorem class.
- Replace the unsupported whole-game contraction inference with the complete finite induction and discounted-limit argument. Contraction may be retained only as a fixed-trustee best-response corroboration.
- Keep “an equilibrium with strict selected actions” distinct from uniqueness of the whole infinite game. Off-path ties and unreachable strategies can remain multiple.

With these repairs, the proof can support the main conditional joint-formation result. They clarify the actual dynamic argument rather than weakening the protected construction to a merely prescribed schedule.
