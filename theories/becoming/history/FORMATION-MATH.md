# Formation of effective correction through a constructed alternative

AI-generated mathematical proposal for Ren's research program, 5 October 2026. This is an exact conditional game, not an empirical law, novelty claim, ethical justification, or account of the invention of its physical repertoire. The accompanying finite-game experiment is completed and reported in [FORMATION.md](FORMATION.md).

## What changes from the previous theory

The earlier correction model supplied a binding F rule and charged the carrier for using it. The renewal and selection models charged contributors and their replacement, but retained an allocation rule or supplied causal benefit. Here the incumbent has no obligation to protect the participant. A participant can construct and operate an alternative use of its own rival input. Effective correction is the incumbent's best response to the participant's available choices, and construction and upkeep can themselves be selected by their consequences for the participant.

This moves the assumed mechanism down one level. It still assumes physical technologies, who can move the input, observability, the cost of interference, and current ownership of actual receipts. In particular, costly-to-remove de facto access is supplied rather than derived. The model tests what follows from those premises and when the arrangement does not form.

## 1. Physical game and supplied repertoire

A participant has one unit of labor or another rival input per episode. It can use that input in joint production or in an alternative facility, not both. In joint production the incumbent receives a dependence rent r above its available replacement activity. The participant retains gross usable resources b if an observable safeguard has already been installed, or x=b-h if joint production proceeds without that safeguard, where h>0. These are actual private receipts after the modeled harm, not additive social-welfare numbers. The input/output mapping and the ability to retain these receipts are supplied physical and access assumptions.

Without a functioning alternative, the participant's refusal gives o0<x. Paying startup K builds a durable alternative facility. Paying m each episode activates its current service and gives gross alternative receipt o, where

\[
0\le o_0<x<o<b,\qquad K,m>0.
\tag{A1}
\]

Operation is paid before current receipts. An idle installed facility remains present in this simple version; handoff and physical deterioration are extensions, not silently included in m. The same rival input must be withheld from joint production to obtain o. There is no free duplication of work or double counting of the receipts.

A common consumption/maintenance obligation ell is also prefunded at the episode opening. Cash is nonnegative at every prefix, and borrowing is unavailable. The participant knows the offered current physical action; no private detection probability is inserted. Observation and the simple decision rule are included in the supplied operating capability m. The model does not explain open-ended diagnosis, unknown harms, or the discovery of the alternative technology.

After the participant decides whether to activate its installed facility, the incumbent chooses a current action:

- S: pay c>0 and physically install the safeguard before the participant commits its input.
- B: pay chi>0 to block the alternative for this episode, then offer harmful joint production.
- H: offer harmful joint production without blockage; this costs zero.

The participant observes the implemented action and then chooses the location of its input. Blocking is unilateral and does not require the participant's consent. It is temporary: the underlying installed facility remains for the following episode, but the episode's operation payment is already sunk. Setting chi=+infinity removes blockage from the repertoire.

The incumbent's incremental payoffs are r-c under S if the input is supplied, r-chi under B if supplied, and r under an accepted H. An H offer followed by refusal gives incremental payoff zero; any already-paid S or B cost remains lost if participation is refused. All incumbent costs are prefunded. For the basic closed-form theorem they are available actions; where incumbent cash is insufficient, the unavailable action is removed, never treated as financed by future production.

The protection is physically in place before the participant supplies input. This is not a promise to pay or protect later. Once those temporal and physical facts change, this game no longer implements the same incentive.

## 2. Exact current-action theorem

First fix an already activated alternative. Its operation cost is sunk at the response gate. By (A1), the participant supplies input after S, supplies input after B, and refuses H. Thus the incumbent compares exactly

\[
S:r-c,\qquad B:r-\chi,\qquad H:0.
\tag{A2}
\]

When r,c,chi have no relevant equality, backward induction gives:

| Smallest of r, c, chi | Incumbent action | Participant gross receipt | Outcome |
|---|---|---|---|
| c | S | b | Joint production with protection |
| chi | B | x | Blocked alternative and harmful participation |
| r | H | o | Exit from joint production |

In particular,

\[
\boxed{S\text{ is uniquely selected}\iff c<\min(r,\chi).}
\tag{A3}
\]

**Proof.** The participant's three responses follow from strict inequalities o<b, x>o0, and o>x. Comparing r-c with r-chi and zero yields c<chi and c<r. The other cases follow identically. This is backward induction in the stated current game. No collective benevolence, binding corrective gate, or threatened future punishment is required. ∎

At equality the best-response correspondence is set-valued. Equality does not justify assuming protective tie-breaking. A sure guarantee against every optimal incumbent response requires strict inequalities. Given an explicit tie-selection rule, weak versions can be computed separately.

If S or B is unaffordable, maximize (A2) only over available actions. Mere willingness to pay c does not make a prefunded safeguard executable. If safe production is selected, incumbent income r-c is positive relative to its baseline; that favorable flow does not retroactively pay its first bill.

## 3. Upkeep and formation are additional decisions

Suppose the incumbent's current payoffs have no continuation effect for it: each episode has a fresh short-lived incumbent maximizing this episode's receipts. A persistent actor with consequential future control is analyzed separately below.

Let y be the participant receipt from the selected row of the table. If the participant does not activate, its baseline refusal gives o0<x, so the incumbent offers harmful joint production and the participant receives x. The active current gain before startup, relative to nonactivation, is

\[
a=y-x-m.
\tag{A4}
\]

Therefore:

\[
a_S=h-m,\qquad a_B=-m<0,\qquad a_H=o-x-m.
\tag{A5}
\]

An affordable active facility is privately selected in the current episode exactly when a>0, with indifference at equality. Thus a technologically effective ability to force safeguards may still go unused if upkeep costs at least the avoided harm. Conversely, the alternative can be worth constructing because it supports exit, even when it induces no change in the incumbent.

The blockade row is especially important: with perfectly anticipated blockage, activation is worse than remaining inactive. The equilibrium may exhibit neither an operating corrective institution nor actual blockage expenditure. Cheap interference can deter construction and operation before an observable suppression event occurs.

For T stationary remaining episodes, participant discount factor delta in (0,1], and no handoff costs, define

\[
A_T(\delta)=\sum_{t=0}^{T-1}\delta^t.
\]

Assume a>0 and that the activated path is executable throughout. Relative to remaining inactive, immediate installation and continued operation have present value

\[
\boxed{A_T(\delta)a-K.}
\tag{A6}
\]

It is strictly preferred to never installing iff K<A_T(delta)a. This is a conditional profitability statement; neither liquidity nor a safe transition is inferred from it. Discounting is only this participant's declared intertemporal evaluation, not a universal value scalar or an excuse to discount others' standing.

For a stationary, unconstrained case, if installation is profitable at some date, installing at the earliest feasible date is best. Let F(t)=delta^t[A_{T-t}(delta)a-K]. For delta<1,

\[
F(t)-F(t+1)=\delta^t[a-(1-\delta)K].
\]

Whenever F(t)>0, the bracket is positive because A_{T-t}<=1/(1-delta). At delta=1, the difference is a>0. This ordering requires that installation and subsequent operation at the earlier date are executable; it does not permit borrowing against F(t).

## 4. Exact resource prefixes and the bootstrap barrier

Write w for cash at an episode opening, before current costs. On an installation-and-activation episode,

\[
w\ge K+m+\ell,\qquad
w'=w-K-m-\ell+y.
\tag{A7}
\]

On later active episodes,

\[
w\ge m+\ell,\qquad w'=w-m-\ell+y.
\tag{A8}
\]

Inactive episodes require w>=ell and give w'=w-ell+x. No current production can finance an earlier cost prefix.

Put q=y-m-ell. Immediate installation followed by exactly T active episodes is cash feasible iff

\[
\boxed{w_0\ge K+m+\ell+\max\{0,-(T-1)q\}.}
\tag{A9}
\]

**Proof.** The cash before active episode t, after paying startup once, is w0-K+tq. Every opening t=0,...,T-1 must be at least m+ell. The smallest of those affine quantities occurs at t=0 if q>=0 and t=T-1 if q<0. The post-episode receipt is nonnegative by (A1), so all final prefixes are covered. ∎

Indefinite stationary operation with finite initial reserve is possible exactly when q>=0 and w0>=K+m+ell. This concerns the prescribed active path, not the optimal behavior of every actor or resilience to extra shocks.

A sharp permanent bootstrap case is

\[
x=\ell,\quad w_0\ge\ell,\quad w_0<K+m+\ell.
\tag{A10}
\]

The inactive process preserves w0 exactly and can never accumulate the missing startup/operation cash. This remains true even if (A3), a>0, and K<A_T(delta)a hold. Positive value and a stable operating regime do not create access to the resources required to enter it.

With x>ell, the earliest combined installation-and-activation date under continued inactivity is

\[
t_* = \max\!\left\{0,\left\lceil
\frac{K+m+\ell-w_0}{x-\ell}\right\rceil\right\},
\tag{A11}
\]

provided initial baseline consumption is affordable and the post-installation path meets (A9). The remaining horizon T-t* may then be too short to recover K. If x<ell, waiting depletes the reserve and cannot solve an initial funding shortfall without another action or receipt.

Credible one-episode refusal requires only the available current option. An indefinitely self-supported fallback requires its own resource condition o-m-ell>=0, plus the necessary opening reserve. A claim that the participant can survive indefinitely outside must not be inferred merely from o>x.

## 5. Succession is both a transfer and a fresh choice

At a known handoff, suppose preserving the facility's operability costs J>=0 before the next episode. This may represent reauthorization, transport, retraining, or reconstruction. If the successor is to operate immediately, the actual inherited reserve must cover J+m+ell. A promise that a wealthy predecessor could pay is not an inherited balance.

If a fixed preserved process requires such a fee every L episodes and otherwise remains in the same regime, each renewal block changes reserve by

\[
L(y-m-\ell)-J.
\tag{A12}
\]

Starting at a handoff, perpetual active operation through these regular handoffs has exact conditions

\[
\boxed{L(y-m-\ell)\ge J,\qquad
w_{\mathrm{handoff}}\ge J+m+\ell.}
\tag{A13}
\]

Here J>=0 makes the first inequality imply nonnegative within-block net flow. Sufficiency follows by paying the prefix, then completing L episodes and arriving at least as well funded for the next handoff. Necessity follows from the mandatory first bill and the fixed negative block drift if the first inequality fails. At first creation K replaces J, while the first later handoff must still satisfy its own bill. Consequently initial startup affordability alone is insufficient when J exceeds K or the first block's surplus.

These are financing conditions for a prescribed continuation. If handoff is a choice and rebuilding K is an available alternative, the successor compares preserving J, rebuilding K, remaining idle, and exiting using its own remaining life and actual consequences. In a stationary isolated L-episode block with no additional continuation or resource effects, preservation's private gain over inactivity is A_L(delta)a-J. It is selected only when that gain is positive and executable; if rebuilding is cheaper and equivalent, preservation cannot be claimed uniquely optimal. The accompanying dynamic program retains these alternatives.

A change in the successor incumbent's r or chi can remove (A3) while leaving every piece of participant equipment intact. Succession of the equipment, succession of funding, and succession of effective bargaining conditions are different events. The model also does not prove that a departing owner voluntarily bequeaths a needed reserve. A freely consumable bequest with no benefit to the departing actor requires another incentive or a transfer mechanism; financial sufficiency is not a theory of its selection.

## 6. Why rival substitution and costly access are indispensable

If using the alternative requires no input withheld from joint production and can be combined freely with it, the participant compares x+o from harmful cooperation with o from refusal. With x>0 it accepts harmful cooperation. The outside receipt can improve welfare while providing no leverage over the incumbent. The cost of refusal to the incumbent must follow from actual substitution, not from adding an output term named an outside option.

If r=0 while c>0, protective joint production is more expensive for the incumbent than refusal, regardless of the participant's stake. This is a no-dependence counterexample: production can continue elsewhere without responding to this participant. When constructing the outside option is profitable and financed, the participant may still escape. Those who lack a feasible substitute remain unprotected by this mechanism.

If chi is cheaply revocable by the incumbent and chi<c, a promised alternative does not implement (A3). Finite chi explicitly admits interference. Infinite chi should not be interpreted as a costlessly supplied moral right; it is an especially strong physical/control assumption.

Observability, private control of the input, alternative capacity, and sufficiently costly interference are jointly necessary in this particular implementation. The model cannot generate them by calling them institutions. Their own construction, defense, coordination and spread remain further mechanisms to explain.

## 7. A persistent incumbent can defeat the one-episode threshold

The fresh-incumbent assumption matters even when all current responses are perfectly observed. An incumbent who values future control may pay a larger current cost to remove later corrective capacity.

Use two episodes, no discount, x=ell=2, b=5, o=4, o0=0, m=1, K=1, participant initial cash w0=4, and incumbent r=4,c=1,chi=3/2. Startup is optional at either date; installed assets can idle; lapse does not erase the asset; rebuilding is allowed when needed and affordable.

With an activated facility, the current condition c<min(r,chi) holds. A fresh incumbent safeguards each episode. Immediate construction and operation finish with participant cash 7, compared with 4 under permanent inactivity: a gain of 3.

For a persistent incumbent, consider activation in episode 1. After paying K+m+ell, the participant has zero cash. If the incumbent safeguards, receipt 5 permits activation in episode 2, and the incumbent receives (r-c)+(r-c)=6. If it blocks now, the participant receives x=2. This is below the next opening m+ell=3; baseline net saving is zero. The second episode therefore has harmful participation without activation, giving the incumbent

\[
(r-\chi)+r=13/2>6.
\tag{A14}
\]

Unblocked refusal gives the participant o=4, preserving second-episode operation, and gives the incumbent only 0+(r-c)=3. Thus blocking is its uniquely optimal response to first-episode activation. Participant final cash would be 2, a loss of 2 against inactivity.

Anticipating this, the participant optimally activates only in the last episode. It can either wait to build or build early and leave the asset idle; both end with cash 5, a gain of 1. Permanent inactivity ends with 4. Thus the exact equilibrium is delayed activation, not necessarily delayed physical construction. In the last episode there is no future control prize, and the incumbent safeguards.

Allowing lapse and rebuilding does not undo this counterexample: after the damaging first block, the participant cannot afford even maintenance, so paying additional startup cost cannot help. The problem is delivered liquidity, not a fictional deletion of the technology.

This example shows why (A3) cannot be promoted into a general repeated-game equilibrium criterion. Myopic current payoffs, actor replacement, financial predation, and continuation values must be distinguished. It is a concrete research bridge to the formation of durable authority rather than a reason to hide the narrower model.

### General two-episode proposition

Let

\[
x=\ell,\quad w_0=K+m+\ell,\quad b=\ell+h,\quad
\ell+m\le o<b,\quad 0\le o_0<\ell,
\]

\[
h>K+m,\qquad r>\chi>c>0,\qquad \chi<2c.
\tag{A15}
\]

Use no discount and the action order above, with installed assets freely able to idle or be abandoned and rebuilt. Then a fresh incumbent in each episode induces immediate operation twice, whereas a persistent incumbent induces operation only in the final episode. Early dormant construction and last-episode construction are payoff-equivalent; there is no claim of a unique construction date.

**Proof.** In the final episode c<min(r,chi) makes S uniquely optimal after activation. Operation is privately better than inactivity by h-m>0. If first-episode activation occurs, every initial cost has been paid from w0, leaving zero before receipts. S leaves participant cash b>=ell+m, H with credible refusal leaves cash o>=ell+m, while B leaves cash ell<ell+m. In the first two cases final operation occurs; in the third, baseline resources remain ell and even upkeep is unaffordable. The persistent incumbent therefore compares 2(r-c), r-c, and 2r-chi. Blockage uniquely wins: chi<2c beats repeated safeguarding, while r>chi implies 2r-chi>r-c. First-episode operation consequently ends with participant cash ell. Permanent inactivity ends with w0. Delayed operation ends with b>w0 because h>K+m, and is therefore selected. Its preceding inactive episode does not benefit the incumbent from spending c or chi, since final construction and operation are already financed. For fresh incumbents the current strict payoff comparison gives S in both active episodes, leaving participant cash 2b-m-ell. This exceeds delayed operation's b by h-m>0, so immediate operation twice is selected. Abandoning and rebuilding an unchanged facility spends K without a benefit, and after early blockage even m is unaffordable; including those actions cannot change the conclusions. ∎

The proof uses an actual reserve bottleneck, rather than an exogenously destructive block. Altering the initial reserve, allowing credit, keeping an independently funded operating reserve, or changing the counterparty's horizon can remove this particular predatory advantage. Those are discriminating interventions for a larger model.

### Affordable formation and strategically resilient formation differ

Under the other assumptions in (A15), now vary the initial cash w while keeping w>=ell. There are three exact regions:

\[
W_{\mathrm{aff}}=K+m+\ell,
\qquad
W_{\mathrm{res}}=K+2m+\ell.
\tag{A16}
\]

| Initial cash | Persistent-incumbent equilibrium operation |
|---|---|
| ell <= w < W_aff | No construction path can finance activation in either episode |
| W_aff <= w < W_res | Activation is deferred to the final episode |
| w >= W_res | Immediate protected operation in both episodes |

This distinguishes funding an apparently profitable first operation from funding enough continuation capacity to remove this particular strategic attack.

**Proof.** Below W_aff, inactive receipts exactly replace ell. Paying K earlier cannot increase cash; it merely leaves the same missing m at the later gate. No episode can finance activation. In the middle region an early block leaves w-K-m in [ell,ell+m), so final upkeep remains impossible. Safe or unblocked-refusal receipts do finance that upkeep because b>o>=ell+m and w>=W_aff. The previous strict comparison therefore still induces blockage after early activation; delayed activation gains h-m-K>0 over permanent inactivity. At or above W_res, even blockage leaves w-K-m>=ell+m, and safe or unblocked-refusal receipts leave at least as much. Every first-episode incumbent action therefore has the same final continuation value r-c. Its strict current comparison c<chi<r then uniquely selects S. Immediate operation twice gains h-m over delaying, and is privately profitable under (A15). ∎

At the numerical example, w=4 gives deferred operation and final participant cash 5. Raising initial cash to 5 leaves enough capacity after a hypothetical first block, so the persistent incumbent safeguards immediately; final participant cash is 8. No block is observed on either selected equilibrium path. The effect is anticipatory: the extra reserve changes what a block would accomplish and thereby changes the incumbent's chosen behavior.

The threshold is exact for this two-episode class. It does not make the capability invulnerable to arbitrary repeated blockage, theft, a different action repertoire, or unlimited future strategic control. Resilience here refers to removal of the specified equilibrium financing attack.

### Independent finite checks

The companion `verification/check_formation_math.py` uses exact rational arithmetic and imports no code from the coordinating agent's implementation. It checked 1,728 primitive stage games against (A3), 30,375 independently replayed cash-prefix cases against (A9), and 243 members of the general two-episode class (A15), plus 1,458 cash variations testing the three regions in (A16), using backward induction over installation, idling, abandonment, rebuilding, incumbent action, and actual participant input allocation. All passed. The focal fresh-incumbent, persistent-incumbent, and extra-reserve trajectories and counts are in `verification/math-proposal-checks.json`. These finite checks supplement the proofs; they are not empirical evidence or a proof of all parameter choices by exhaustive automation.

## 8. What the model establishes and does not

Established within stated assumptions:

1. A physical, funded participant option can cause a self-interested incumbent to select protection without a benevolent binding gate.
2. Three independent obstructions appear: insufficient incumbent dependence, cheap blockage, and unaffordable or privately unrewarding participant capability.
3. Safe cooperation, independent exit, dormant exploitation, and a bootstrap trap occupy different parameter regions.
4. A capacity can work without being exercised in realized equilibrium. Funding only actual withdrawals can therefore remove the means whose availability prevents harm.
5. Successor capacity requires actual funding and operative incentives. A longer-lived opponent can change equilibrium even under identical one-period parameters.

Not established: a universal trend toward these capabilities; protection of actors who cannot generate leverage; a derivation of ethical standing; an account of new-question discovery; formation of the action repertoire or de facto control itself; actual historical or experimental explanatory advantage. The specific mathematical ingredients are standard backward induction, intertemporal accounting, and limited-commitment reasoning. Their local contribution is the precise bridge from an installed corrective gate to selected, financed, contestable capability.
