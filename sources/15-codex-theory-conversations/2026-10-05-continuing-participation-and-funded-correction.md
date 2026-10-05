# Continuing participation and funded correction

Research continuation, 5 October 2026, Asia/Bangkok. AI-generated research assistance under Ren's direction, with mathematical, implementation, and primary-literature reviews by three returning agents. Ren requested: “continue please”. This eleventh cycle implements the preceding frontier of personal cost incidence, continuing refusal, and funded compensation. It is a research snapshot, not an empirical study or a verbatim conversation.

**An initially acceptable correction can cease to be acceptable when people learn who bears its burden. Making it acceptable again can require resources at a particular time, even when it produces a positive total gain.** Three obstacles must be distinguished: insufficient gains, their distribution, and the ability to finance an acceptable distribution. The new experiment puts all three inside the same productive system.

The preceding [plural-requirements study](2026-10-05-plural-requirements-and-attainable-correction.md) asked whether one policy could meet several expected bounds. It did not allocate losses to individuals or give them an implemented refusal decision. This extension supplies two distinct personal loss functions and checks the same policy again after public information and recommendations arrive.

## Agreement is a condition at histories

Let \(h\) be a public history, including revealed lottery outcomes, and \(a\) a publicly disclosed recommendation. For participant \(i\), let \(V_i^\pi(h,a)\) be expected remaining loss under continuation policy \(\pi\), and \(D_i(h)\) the remaining loss from the specified refusal. Where that participant can refuse, continuing participation requires

\[
V_i^\pi(h,a)\le D_i(h)
\quad\text{for every reached recommendation and every participant.}
\]

This is stronger than comparing initial expectations before someone learns their role. The relevant comparison includes all future consequences, not merely immediate effort. Public randomization cannot average away a refusal incentive after its outcome is known. Past sunk expenses must be treated consistently on both branches.

For a finite tree with permanent passive refusal, no other deviations, a fixed executable recommendation rule, and acceptance at indifference, these inequalities also exclude profitable history-dependent stopping. At the final gate, refusal cannot improve the participant's outcome. Induction gives the same result at each preceding gate, including strategies that wait and refuse later. This establishes compatibility with the modeled refusal rights. It does not establish truthful reporting, agreement about probabilities, all-action incentive compatibility, or legitimate authority.

The implementation retains full public histories. If \(y_j\) is the occupancy of recommendation \(j\), \(\mathcal T(j)\) its action subtree including itself, and \(\ell_{ik}\) participant \(i\)'s expected immediate loss at action \(k\), its participation row is

\[
\sum_{k\in\mathcal T(j)}y_k\ell_{ik}-y_jD_i(h_j)\le0.
\]

Unique parent histories and probability-flow equations make this the reach-weighted conditional comparison. Unreached subtrees have zero occupancy. The code separately reconstructs conditional losses at every strictly positive occupancy, so rare violations cannot hide behind small probability weights.

These are established dynamic-participation structures. [Kocherlakota (1996)](https://academic.oup.com/restud/article-abstract/63/4/595/1520475) studies risk sharing with symmetric information and no commitment; [Ligon, Thomas and Worrall (2002)](https://ligon.github.io/papers/ligon-thomas-worrall02/) develop dynamic informal insurance with limited commitment. Our contribution sought here is a transparent coupling to paid correction, productive renewal, and actual cash timing, not a new discovery of participation constraints. The [prior-art audit](../../_process/research/2026-10-04-integrated-evolution/continuing-participation-prior-art.md) also distinguishes continuation promises, financing, and public information.

## Personal incidence and the source of compensation

The inherited physical model is unchanged: hidden faults affect visible production; repair costs three; tests and diagnostic readiness cost money; rebuilding takes time; stock zero is absorbing; income arrives after expenses; retained cash is capped at eight. Stock and its deterministically linked income provide one joint observation. The wrapper adds two half-owners, A and B, and a fair public assignment each round identifying who bears a repair's fixed nonmonetary burden.

Both owners receive half the output and bear half the shared physical expenses. The assigned person incurs repair burden one. Each incurs a terminal collapse loss of one in the baseline, with six as a sensitivity control. Test disruption is shared. These are supplied quasilinear preferences. The fixed repair burden replaces the earlier target-absence measure as personal exposure; it does not privately reveal whether the hidden fault was present.

A payment \(k\) is withdrawn from the joint reserve and paid privately to the repair worker. The worker therefore gains only \(k/2\) net: they already owned half the money withdrawn. The other owner loses \(k/2\). Ignoring this ownership would count compensation as a free benefit. The two personal losses sum to

\[
L_A+L_B=\text{physical expense}-\text{output}
+\text{repair burden}+\text{test burden}
+2\gamma\,\text{collapse indicator},
\]

where \(\gamma\) is the per-owner terminal collapse loss. Transfers cancel in this sum. They nevertheless reduce the reserve available to fund later production and correction. Privately received payments cannot be redeposited under the declared action set. No borrowing or unsecured deferred payment is available.

Either owner may veto before setup/testing and again after any diagnostic result, before repair. A veto permanently ends active cooperation; passive production continues through the same horizon with both property claims intact. This is a collective veto over active cooperation, not individual departure while the other runs the plant. The fallback uses the actual stock, cash, and posterior. A test already accepted and paid is not refunded at the later gate.

Compensation and observable repair execute together after both accept. This conditional exchange is a supplied local commitment technology. If the recipient could take the payment and then refuse the same repair while keeping it, the payment would be sunk on both branches and the claimed incentive would disappear. The model does not explain who maintains that conditional execution mechanism.

## Exact one-period result

Start at stock one, fault probability one-half, and repair burden one. Passive production has expected output 2.2 and collapse probability .45. Each owner's remaining loss is

\[
D=-2.2/2+.45=-.65.
\]

Repair gives expected output 5.6 and zero terminal collapse. Before compensation, the worker's loss is \(3/2-5.6/2+1=-.30\); the other owner's loss is \(-1.30\). Before the fair assignment, each expects \(-.80\), preferring repair to passive production by .15. Total gain is .30. After assignment, the worker prefers refusal by .35.

An owned-pool payment changes these losses to

\[
L_W(k)=-.30-k/2,\qquad L_O(k)=-1.30+k/2.
\]

Both accept exactly when

\[
.7\le k\le1.3.
\]

Repair and payment must be financed before output. With divisible payments, the minimum current reserve is therefore 3.7. With the implemented grid \(k\in\{0,1,2\}\), it is four. At reserve three, repair is physically affordable and acceptable initially, but fails continued acceptance. At reserve four, payment one makes both owners' losses \(-.80\) and implements repair under the stated rights.

More generally, for a fixed terminal correction with uncompensated losses \(\ell_W,\ell_O\), refusal losses \(d_W,d_O\), physical expense \(c\), and reserve \(b\), a nonnegative payment from a half-owned pool exists precisely when

\[
\left[\max\{0,2(\ell_W-d_W)\},\;2(d_O-\ell_O)\right]
\cap[0,b-c]
\]

contains an allowed payment. This elementary interval separates the recipient's requirement, the other owner's willingness to fund it, and liquidity. It assumes no later consequence changes with the remaining reserve. In a multi-period model those consequences must be recomputed; the terminal formula cannot simply be reused unchanged.

## What the complete finite comparison shows

The declared run retains 92 policy comparisons: three horizons, five initial reserves, two payment action sets, initial-only versus continuing participation, and burden/collapse-valuation controls. The reported frontier minimizes collapse subject to participation, then physical expense, then payouts among tied solutions. This is an analyst's reliability comparison, not an agreed social objective or a bargaining solution.

| Case | Initial-only commitment benchmark | Continuing veto, no payment | Continuing veto, funded payment |
|---|---:|---:|---:|
| One period, reserve 3, collapse loss 1 | 0% | 45% | 45% |
| One period, reserve 4, collapse loss 1 | 0% | 45% | 0% |
| Two periods, reserve 4, collapse loss 6 | 0% | 1.7% | 1.7% |
| Two periods, reserve 5, collapse loss 6 | 0% | 1.7% | 0% |

Numbers are minimum modeled collapse probabilities, not empirical estimates. Initial-only values assume execution. Replaying those selected commitment policies with actual later veto raises their collapse probability to 45% in the first two rows and 1.7% in the last two. Continuing-compatible policies replay unchanged to numerical tolerance.

The two-period comparison locates a later funding obstruction. After the first repair, a .1-probability branch leaves stock one and next fault probability .1. Initial reserve four leaves three available there; initial reserve five leaves four. At collapse loss six, the final repair requires payment in \([.68,1.32]\) for both to accept. The allowed payment one is affordable only in the latter case. It is paid on the .1-probability branch, so expected payout is .1. Ordinary shared future output supports initial participation; it does not prefund a payment due before that output.

The counterweights matter. At the same final physical state but baseline collapse loss one, passive personal loss is \(-1.49\), while the uncompensated repair losses total \(-1.60\). Passive total loss is \(-2.98\), so repair is worse overall by 1.38. No transfer can make both better in this terminal comparison. More generally the compensation interval is \([2.72-.34\gamma,\;.34\gamma-.72]\); total surplus becomes nonnegative only at \(\gamma\ge86/17\). The higher-loss case is a different stated valuation, not a correction to the baseline preferences.

In the baseline two- and three-period cases with reserve at least three, future benefits make initial repair acceptable without payment, and the best continuing collapse probability is 1.7%. More money and allowed payments do not remove the later lack of gains. Reducing one-period repair burden to .5 removes the need for payment; increasing it to 1.5 removes the initial aggregate gain, so even the commitment benchmark chooses passive production. These controls prevent a universal prescription to compensate or accumulate reserves.

None of the 92 selected policies buys a paid diagnostic. Inquiry remains available and correctly costed, but these parameters provide no selected diagnostic-use result. The finding concerns participation and finance; it does not establish a new benefit from maintaining inquiry.

## Verification, interpretation, and the next question

All nine independently constructed tests pass, covering latent physical enumeration, public histories, action-conditioned participation, personal and cash accounting, post-test fallback, prefunding, conditional payment, and backward veto replay. Across the 92 comparisons, the largest flow residual is \(5.56\times10^{-16}\), policy-evaluation discrepancy \(1.07\times10^{-14}\), and primary primal–dual gap \(2.78\times10^{-16}\). No positive conditional refusal gain was measured for the continuing policies; their replay discrepancy is at most \(3.56\times10^{-15}\). These are floating-point checks, not interval proofs or empirical validation. [Inputs, development cases, tests, complete results, and inspected figure](../../experiments/continuing-participation/README.md) remain available.

For the broader theory, the conditional lesson is that renewal may require preserving the capacity to make correction acceptable when its actual incidence becomes known. Material feasibility, expected collective benefit, personal willingness, and financed implementation are distinct. A promising AI-supported reform should therefore identify whose burden changes, what they know when they can object, what refusal actually leaves them, and who can fund a different arrangement. The model does not specify legitimate preferences or rights, derive purpose formation, model an AI agent's incentives, or establish a universal alignment solution.

There is also a danger inside the inequality itself: making refusal worse raises \(D_i\), which can make participation easier without improving continuation. Acceptance alone cannot distinguish better cooperation from manufactured dependence. Our experiment holds refusal rules and property claims fixed; it has not modeled deliberate degradation of the fallback. Protecting meaningful refusal is an explicit normative commitment, not a consequence of minimizing collapse.

The next test should give a participant one concrete, funded action they control after refusing, then ask how shared production and access to that alternative coevolve. A narrow design is an optional allocation from earned output into a private backup service, compared with an equal nominal but revocable pooled earmark. The backup must be usable during cooperation too, so staying is not artificially penalized. Report the cost to working cash, each person's continuation loss, and the alternative they can actually execute. Private custody remains a supplied control primitive, not an explanation of protection against confiscation.

An independent diagnostic has no decision value under the present rule forbidding every active response after veto. First make a real alternative executable; then examine its cost, reliability, and control. A credible future claim or lending instrument would separately expand the payment action set. Merely naming a promise would not explain its enforcement. This keeps the north star in view: the ability to discover, negotiate, refuse, and enact warranted change must have a material and institutional basis, while its legitimacy remains open to argument.
