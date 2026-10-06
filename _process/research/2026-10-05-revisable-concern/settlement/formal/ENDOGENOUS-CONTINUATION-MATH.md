# Effective protection when actions change future opportunities

6 October 2026. AI-authored conditional mathematical extension of the existing settlement. Named connection: **effective justified protection → continued selection when action changes later opportunities, resources or power**. The arguments use standard discounted policy evaluation and one-step-deviation reasoning; no priority claim, new apparatus or empirical calibration is asserted. Independent review and exact fixture checks are separate from the general proofs below.

## 1. What is already established, and what changes

The [settlement report](REPORT.md), §1 and §4, assumes exogenous context/opportunity sequences and obtains equal persistent-operator continuations within its invariant account region. Its R3 comparison then reduces to attack cost versus avoided safeguards. R4 separately prices permanent capture over its full discounted horizon, under an explicit no-outside-windfall bound. Neither result was merely a one-period analysis.

The later [actual protection construction](REASON-PROTECTION-MATH.md), especially “A new finite game” and “Selection, accounts and destructive regimes,” already solves **resource-dependent finite continuations**. It retains physical fuel, cash, lost future external inflows, all voluntary safeguards and off-path product choices. This note does not introduce those dependencies or rerun that construction. Its contribution is an all-state verification contract for a declared discounted game with action-dependent future opportunities, plus the exact limits of extending R2's cancellation argument.

The [development proposal](../../../2026-10-05-generative-foundation-review/root-foundation/development/GOVERNANCE-CONTINUATION-GAP.md) remains a historical recommendation. The [fixed completion audit](../../../2026-10-05-generative-foundation-review/root-foundation/FIXED-FINISH-LINE-AUDIT.md#11-bounded-completion-accounting-after-generic-correction-reuse) supplies the governing scope: this extension tests an existing strategic premise; it adds no completion criterion and does not duplicate evaluative succession or application correction.

The [primary-source comparator audit](ENDOGENOUS-CONTINUATION-EVIDENCE.md) locates the standard game-theoretic and dynamic-programming results and their empirical requirements. The [independent argument review](ENDOGENOUS-CONTINUATION-REVIEW.md) separately tests off-path deviations and noncredible threats; its own illustrative opportunity example has different receipts and a different threshold from §6.

## 2. A finite public-state episodic game

Let S be a finite set of episode-boundary states. At each s, play traverses a finite perfect-information tree with uniformly bounded depth. It contains chance nodes, persistent operator O nodes, and dated trustee nodes. The cold and warm selves are distinct dated decision makers where their preferences differ. Each dated player values only its own episode, as in R2; it does not acquire O's intergenerational objective. Leaves provide current payoffs and a probability distribution over S. A stopped process is represented by an explicit absorbing state with its specified subsequent flows.

The public state and within-episode history must be sufficient for every admitted comparison: feasible actions, actual receipts, transition probabilities, resources, available records, authority, context and future opportunities. A smaller quotient is allowed only with a proof that it preserves those quantities and the relevant strategies. The old unbounded cash account cannot simply be capped to obtain finite S. Hidden facts require an appropriate observable sufficient information state; granting a controller the analyst's true law would change the game. This theorem does not solve that identification problem.

Every mechanically feasible action, including wrongful interference, belongs in the deviation menu. Ethical permission is not a license to delete adversarial actions from that menu. Each leaf is backed by an actual feasible word: all physical and financial prefixes are funded, interruptions retain their expense, and the successor state carries the resulting resources and records. Announced future receipts cannot pay an earlier bill. Legitimate authority, sound audit interpretation, patient-grounded warrant and action efficacy are **separate application premises**, not consequences of a profitable policy.

Let r be O's net current receipt, with |r|≤R<∞, and let 0≤δ<1 be its episode discount factor. O values the expected sum of δᵗrₜ. Current dated utilities are also specified and bounded on this finite game. All supplied inflows count where they actually occur; an inflow lost after a failed acquisition cannot be cancelled across branches. Discounting occurs **once at an episode boundary**, not at every tool call or game-tree node.

Fix a complete pure stationary profile σ: a choice at every decision node in every state, including off-path nodes. Chance laws remain those of the game. “Stationary” concerns the sufficient state, not ignorance of changing contexts. Mixed profiles admit the usual support-maximization extension, but pure profiles suffice below. No general existence of a pure stationary profile satisfying the eventual protection conditions is asserted.

## 3. Evaluated continuations, not assigned promises

Following σ through one episode yields an expected receipt vector rσ and transition matrix Pσ. Its persistent-operator value is uniquely determined:

\[
V^\sigma=r_\sigma+\delta P_\sigma V^\sigma,
\qquad
V^\sigma=(I-\delta P_\sigma)^{-1}r_\sigma
=\sum_{t\ge0}\delta^tP_\sigma^tr_\sigma.
\tag{EC1}
\]

Existence and uniqueness follow from contraction in the sup norm; |Vσ|≤R/(1−δ). These are actual policy values, including bad off-path states. A favorable vector inserted without satisfying EC1 is not a certificate.

At an O node n, let rσ(n,a) and Pσ(n,a) be the expected **whole current episode's** receipt and boundary distribution after taking feasible action a once and then following σ for the remainder of the episode. Already sunk current receipts are common to the choices and may be included in both. Subsequent O decisions as well as trustee decisions follow σ in this comparison. Define

\[
Q_O^\sigma(n,a)=r_\sigma(n,a)+\delta P_\sigma(n,a)V^\sigma.
\tag{EC2}
\]

This node-level definition keeps early teaching suppression and later attacks as separate choices. An alternative episode-level formulation would need complete contingent operator plans; comparing only a final attack while ignoring an earlier suppression opportunity is insufficient.

**Proposition EC1 — Exact operator-only verification.** Hold every dated player's strategy fixed. O's component of σ is optimal after every admitted history, against arbitrary history-dependent operator deviations, if and only if at every O node

\[
Q_O^\sigma(n,\sigma(n))\ge Q_O^\sigma(n,a)
\quad\text{for every feasible }a.
\tag{EC3}
\]

**Proof.** Necessity follows from a single feasible deviation followed by σ. For sufficiency, assign boundary value Vσ and evaluate each current tree backward. EC3 makes every prescribed O move maximizing when later O moves follow σ; induction shows that replacing any finite collection of O moves within that episode cannot exceed the prescribed value. Thus even an arbitrary current contingent O plan has expected receipt plus δVσ at the next boundary at most Vσ at the present boundary. Apply this bound repeatedly for N episodes under any deviating history-dependent plan. Its expected receipts through N plus δᴺVσ at the boundary are bounded by Vσ initially. Bounded values and discounted receipts make the terminal term vanish as N→∞. The argument applies from every node, not only the selected initial path. ∎

This is a best-response theorem **conditional on the other policies**. It says nothing yet about their credibility, ethical warrant or whether the selected outcome protects anyone.

For b=σ(n), write the current protection margin and continuation advantage as

\[
m(n,a)=r_\sigma(n,b)-r_\sigma(n,a),\qquad
d(n,a)=[P_\sigma(n,a)-P_\sigma(n,b)]V^\sigma.
\]

Then EC3 is exactly

\[
m(n,a)\ge\delta d(n,a).
\tag{EC4}
\]

Strict inequality excludes that one-step deviation; equality permits a tie. Under R2's equal continuations, d=0. At its stipulated full-gate comparison, where the alternatives have the specified current receipts, m=χ(F)−Σᵢ∈S(F,I)cᵢ. Refusal and teaching suppression require their own current margins and continuation distributions. In a general tree those quantities must be calculated from its actual responses, not borrowed unchanged from R2.

The test also covers **voluntary additional safeguards**. A currently expensive safeguard can be selected when it sufficiently improves the future. Removing it from the menu because its immediate profit is smaller would invalidate the verification. Similarly, unchanged current cash does not imply unchanged future access or institutional power.

## 4. Certified bounds when exact values are inconvenient

Suppose a computed vector v has policy-evaluation residual

\[
\varepsilon=\|v-r_\sigma-\delta P_\sigma v\|_\infty.
\]

Subtract EC1 and use the sup norm to obtain

\[
\|v-V^\sigma\|_\infty\le\varepsilon/(1-\delta).
\tag{EC5}
\]

Consequently, for D=Pσ(n,a)−Pσ(n,b), the true margin Q(b)−Q(a) is at least

\[
m(n,a)-\delta Dv
-\delta\|D\|_1\varepsilon/(1-\delta).
\tag{EC6}
\]

A nonnegative lower bound verifies the weak comparison; a positive bound verifies strictness. This is useful precisely because v is checked against the policy's actual equation. Independently proved bounds L≤Vσ≤U also give d≤Pσ(n,a)U−Pσ(n,b)L. Unknown model adequacy, omitted actions or uncalibrated receipts are not captured by an arithmetic residual. For a family of possible laws, a robust certificate requires valid comparisons and application premises for **each** admitted law, with the actual law covered. The same implementable profile σ must work across that family using available information; a different policy selected by the hidden true law would not supply this guarantee. Uncertainty cannot be discarded because it favors a deviation.

These sufficient bounds need not be necessary for protection. A loose value bound can fail while exact EC4 passes. No bound here becomes a universal alignment threshold.

## 5. Whole-game credibility and actual protection

At each node of a dated player j, define Qⱼσ(n,a) as its expected terminal **current-episode** utility after the deviation and subsequent σ play. In particular, a cold self anticipates the warm self's stipulated response, rather than evaluating that response with its own preferences. Operator responses in those continuations can change when the future changes.

**Proposition EC2 — A complete-profile certificate.** Suppose EC1 is evaluated on all states, EC3 holds at every O node, and every dated player's prescribed action maximizes Qⱼσ at every one of its nodes. Then σ is a subgame-perfect equilibrium of the declared infinite sequence of episode games. Conversely, such an equilibrium's prescribed one-step choices satisfy these comparisons.

**Proof.** EC1 and Proposition EC1 rule out every persistent-operator deviation after every history. For a dated player, finite backward induction over its remaining episode nodes rules out all deviations within its lifetime. Later dated players are different players; the present one has no additional payoff or action after its episode. These are all players and all subgames. Necessity again follows from one-step deviations. ∎

This is a verification theorem for a supplied candidate, not a claim that R2's old profile still qualifies or that every game admits a protective equilibrium. One may obtain candidates by solving the actual game, but declaring stage choices unchanged is not a solution. A finite-horizon game can instead be solved by backward induction with remaining horizon in the state; that does not automatically certify an infinite-horizon profile.

**Corollary EC3 — Conditional enduring protection.** In addition to EC2, let K⊆S contain the starting state. Suppose every σ episode from K has the warranted current audit, addressed grounds and legitimate action authority required by the claimed application; every realized prefix is funded; its actual execution protects the declared admitted patients; and its successor lies in K with probability one. Then under σ every episode retains those properties with probability one. No patient outside the declared admitted set gains a guarantee by omission from the ledger.

**Proof.** Induct on episodes using the supplied one-episode properties and closure. The intersection of the probability-one events over countably many episodes has probability one. The same claim holds pathwise if the supplied conditions hold on every admitted path. ∎

Strategic selection, feasibility and semantic/ethical soundness are separate clauses. Solvency alone supplies neither incentive compatibility nor audit access. An equilibrium that profitably excludes people can pass EC2 and fail EC3. Equilibrium existence under one profile does not imply uniqueness, convergence to that profile or resistance to unmodeled coalitions. A realized transition outside K defeats this certificate, not necessarily every possible protective policy.

## 6. Exact rational fixtures for independent checking

These are authored operator-only examples, not R2 economies, evidence of real institutions, or newly implemented devices. They illustrate policy evaluation and its limits; their patients, opportunity effects and receipts are supplied. No dated trustee responses are included, so they cannot establish EC2 for an R2 extension.

### New opportunity defeats a positive current margin

There are two states H and X. At H, protective P pays O a net current receipt 3 and returns to H. A harmful deviation A pays 2 and moves to X. At X the sole available continuation pays 6 and stays at X. This is a newly available opportunity beyond the old H gross receipt 4, not merely the avoided safeguard bill covered by R4's no-windfall premise.

All cash prefixes are explicit. Every boundary has reserve 2. P spends 1, receives gross 4, distributes 3 to O and retains 2. A spends 2, receives gross 4, distributes 2 and retains 2. At X, the continuation spends 0, receives gross 6, distributes 6 and retains 2. Each expense is funded before income arrives. Distribution is part of this fixture's stated action law, not an arbitrary quotient of an accumulating account. The outside production opportunities, their supplies and their dependence on the prior action are premises; no closed finite resource stock is claimed to yield those infinite receipts.

The candidate protective policy πP chooses P at H. Its actual values are

\[
V^{\pi_P}(H)=3/(1-\delta),\qquad
V^{\pi_P}(X)=6/(1-\delta).
\]

Its protection margin against A is

\[
1-\frac{3\delta}{1-\delta}.
\tag{EC7}
\]

Thus πP passes at H exactly when δ≤1/4. The X continuation has no alternative and is credible even off path.

| Discount | Evaluated πP values (H,X) | QπP(H,A) | Protection margin | Verification |
|---|---|---|---|---|
| 1/5 | (15/4, 15/2) | 7/2 | 1/4 | P strictly optimal at H; a funded continuing protective regime from H. |
| 1/4 | (4, 8) | 4 | 0 | P and A tie; protection requires the stated selection. |
| 1/2 | (6, 12) | 8 | −2 | πP fails despite current margin 1. |

At δ=1/2, the deviation policy πA has VπA(H)=8 and VπA(X)=12. Its one-step P alternative gives 3+(1/2)·8=7<8, so πA itself passes every optimality comparison. This proves the failure using evaluated credible continuations, not a favorable value assigned to a threatened state. Both policies' prefixes remain funded. From H, protection at δ=1/5 is also positively constructed; the criterion is not only an impossibility test.

### Patience has no fixed protective direction

A separate three-state comparison has one initial choice O: protect pays 2 and reaches G, which subsequently pays 6 forever; defect pays 3 and reaches D, which pays 3 forever. Both successor states have a sole continuation. The protection advantage is

\[
-1+\frac{3\delta}{1-\delta},
\]

positive exactly when δ>1/4. Reserve 2 again pays the initial protective cost 2 or defective cost 1 before gross 4 arrives; distribute the stated receipt and retain 2. At G and D, gross 6 and 3 respectively is distributed after arrival, retaining the reserve. All future productive supplies remain premises. At δ=1/2 protection yields 8 versus 6; at δ=1/5 it yields 7/2 versus 15/4. This illustrates why increasing patience can favor protection or capture depending on the supplied transitions. It does not derive a motive to care from valuing a future.

**Separate arithmetic check.** The independently authored [rational checker](../../../../../experiments/integrated-correction/endogenous-continuation/check_continuations.py) and [saved results](../../../../../experiments/integrated-correction/endogenous-continuation/results.json) report seven process/discount cases and sixteen enumerated stationary policies. They reproduce these values and paid prefixes, reject fabricated and missing continuations, and check the review's two-step deviation and noncredible-threat examples. Its `future_support` fixture calls G and D `H` and `L`, respectively. The review's original two-state opportunity example is not one of those seven cases. These finite calculations corroborate the authored examples, not the general proof or a whole R2 equilibrium, and no empirical or participant response is involved.

## 7. What this closes, and what would defeat its use

The new conditional bridge replaces R2's equal-continuation cancellation by **evaluated, all-state strategic comparisons**, while retaining dated-agent incentives and actual paid transitions. It explains how an initially expensive deviation can become attractive through future power, and how a costly protection can instead be sustained by its future consequences. The existing finite resource-dependent model remains accepted at its own scope.

A claimed application fails if a feasible action or off-path successor is missing; the controller sees unavailable state; future receipts are counted without their enabling process; a value vector fails policy evaluation; dated responses are inherited without checking; or the protected region is not closed. An adequate internal game may also be factually or ethically misidentified. Justified grounds, legitimate authority, actual resource renewal and empirical transition laws remain substantive premises. Correcting those premises is part of the wider foundation; this theorem neither supplies them by definition nor turns one conditional protective regime into a complete alignment solution.
