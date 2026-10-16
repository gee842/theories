# Continuing participation and funded compensation

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. This memo applies finite-horizon participation constraints, public-history flows, and resource accounting to the productive-correction model. These are established methods, not a new theorem about the universal organization of society. Its specific calculations and counterexample concern the declared finite experiment.

Limited commitment and the ability to leave are central to Ligon, Thomas, and Worrall's [*Informal Insurance Arrangements with Limited Commitment*](https://ligon.github.io/papers/ligon-thomas-worrall02/). Designer commitment is a separate issue in Doval and Skreta's [*Mechanism Design with Limited Commitment*](https://arxiv.org/abs/1811.03579). Neither citation makes this experiment a strategic-equilibrium analysis; the assumptions below specify what is and is not tested.

## 1. Incidence and refusal must precede the participation calculation

Index participants by \(i\). A public history \(h\) contains all publicly observed physical outcomes, diagnostic results, cash, worker assignments, recommendations, and relevant commitments. Let

\[
V_i(h)=\mathbb E[\text{future loss to }i\mid h,\text{continue under the proposed rule}],
\]

\[
O_i(h)=\mathbb E[\text{future loss to }i\mid h,\text{exercise the specified refusal option}].
\tag{1}
\]

Lower loss is preferred. Participation requires \(V_i(h)\le O_i(h)\). Refusal must have actual consequences: which productive assets remain available, whether passive output continues, whether the participant keeps previously received funds, and whether the institution closes or can resume. A zero outside value cannot be substituted for available passive production. If refusal merely skips one intervention and permits later reentry, its value must include that option; permanent retirement is a different contract.

The proposed experiment gives either participant a public veto followed by permanent passive operation: no further paid inquiry, repair, or compensation, while passive production and collapse exposure continue. Both participants have equal ownership of the pooled reserve and output. This is a specific outside option, not an account of all possible bargaining arrangements. There are no private signals, private reports, hidden effort choices, or unilateral alternative repair technologies.

Current participation compares future consequences from the decision being made. A diagnostic bill already paid before the result is disclosed is sunk at the later repair gate and appears on both sides of a full-history comparison. It must not be charged again only to continuation. Conversely, consent to the test belongs at its earlier gate, before its cost and disruption are incurred. Already received compensation retained upon exit is also sunk; it cannot be counted again as an inducement to perform a later task.

Sunk does not mean irrelevant to the physical state: paid fees reduce available cash; past events can change beliefs, stock, wealth, rights, and promised obligations. A physical belief state sufficient for production need not be sufficient for participation if it omits these distinctions. The experiment uses a full public tree rather than merging histories that may carry different continuations.

## 2. Three different times at which agreement can be tested

**Before uncertainty.** An initial requirement compares expected total loss before a public worker assignment or a policy lottery is drawn:

\[
\mathbb E V_i\le\mathbb E O_i.
\tag{2}
\]

**At a reached public history.** Continuing participation requires (1) after the observations and assignments available at that time.

**After a recommendation is disclosed.** If a randomized controller announces action \(a\), the relevant condition is

\[
V_i(h,a)\le O_i(h,a)
\quad\text{for every }(h,a)\text{ with positive probability}.
\tag{3}
\]

Averaging an objectionable announced action with an attractive action does not satisfy (3). A public assignment lottery can be acceptable before the worker is known while its realized work assignment is refused. If a complete policy lottery is publicly disclosed, that disclosure also belongs in the history; every disclosed policy must satisfy its own reached participation constraints. If the policy draw remains private but its current recommendation is public, condition instead on the posterior over hidden plans consistent with that recommendation. These are different information structures.

Condition (3) still compares expected future consequences. It does not guarantee that every eventual physical realization is harmless, nor that every stage gives a nonnegative immediate gain. Ashlagi, Daskalakis, and Haghpanah's [*Sequential Mechanisms with ex-post Participation Guarantees*](https://arxiv.org/abs/1603.07229) explicitly studies a stronger period-by-period individual-rationality requirement. It should not be conflated with the continuation comparison here.

### Finite stopping-time justification

Fix a committed continuation rule and a permanent-exit option with loss \(O_i(h)\). If (3) holds at every reached decision gate, no history-dependent choice of an exit time improves participant \(i\)'s expected loss while the others follow the rule. At the final gate this is the stated inequality. Inductively, if future optimal exit decisions cannot improve on following the rule, then at the present gate the best attainable loss is the minimum of \(O_i(h)\) and the rule's continuation loss. The latter is no larger. Finite backward induction proves the result.

This proves exit rationality relative to the specified fallback. It does not prove truthful reporting, effort incentives, coalition stability, fairness, or implementation when the controller can change promised future behavior. Temporary refusal with reentry requires a different deviation calculation, including its off-path continuations.

## 3. Full-history flow gives linear participation tests

For each publicly announced recommendation gate \(n=(h,a)\), let \(y_n\) be its probability of being reached and announced. Ordinary history-tree flow equations connect these occupancies to predecessor chance branches. Let \(\ell_i(j)\) be expected incremental loss attached to later occupied action \(j\), including appropriately assigned terminal losses. With \(D(n)\) the descendants including the action at \(n\), continuing participation has the unnormalized form

\[
\sum_{j\in D(n)}y_j\ell_i(j)-y_nO_i(n)\le0.
\tag{4}
\]

For \(y_n>0\), division by \(y_n\) recovers (3). For \(y_n=0\), flow forces all descendants' occupancies to zero and (4) is vacuous. Each node is a unique public history, so descendant mass belongs unambiguously to its ancestor. A state-merged occupancy matrix cannot simply use the same descendant construction.

The outside loss in (4) is fixed by the history and the specified passive-retirement process, including that history's posterior. It does not depend on hidden private information or an unmodeled policy-dependent refusal strategy. If refusal itself chooses among multiple future strategies, impose the appropriate comparison with each allowed deviation or solve the corresponding sequential mechanism problem. An outside value optimized under a changing endogenous policy cannot silently be treated as a fixed coefficient.

Finite affordable action enumeration, linear flow, initial participation, and rows (4) therefore form a finite LP. The adopted code minimizes collapse probability over this feasible set. That objective is an analyst's selection among consenting policies, not a shared complete ranking inferred from consent. The always-retire policy provides a feasible benchmark under the stated fallback.

The margin in an additively relaxed version of (4) is **reach-weighted**, not a uniform conditional violation. A conditional margin multiplied by endogenous \(y_n\) is generally bilinear. Report conditional refusal gains by evaluating the extracted policy and dividing only at genuinely reached gates; very rare gates can have small weighted residuals but substantial conditional violations. Numerical tolerances and any omitted tiny-probability gates must be disclosed. Exact zero residual has the theoretical meaning above.

## 4. Compensation redistributes wealth and uses scarce liquid funds

For a general treasury with cash \(b\), physical expenditure \(e\), output \(Y\), collected taxes \(\tau_i\), transfers \(t_i\), and participant private liquid holdings \(w_i\), one possible ledger is

\[
b'=b-e-\sum_i t_i+\sum_i\tau_i+\alpha_0Y,
\qquad
w_i'=w_i-\tau_i+t_i+\alpha_iY-c_i,
\tag{5}
\]

where \(\sum_{i\ge0}\alpha_i=1\) and \(c_i\) denotes private consumption. Adding the accounts cancels internal taxes and transfers:

\[
\Delta\!\left(b+\sum_iw_i\right)=Y-e-\sum_i c_i.
\tag{6}
\]

Collection, verification, enforcement, and transaction fees would be real costs if included. A transfer cannot be counted once as a payer's loss, again as a social loss, and omitted as the recipient's gain.

Funding still matters. If expenditure and compensation are due before this round's production, with no borrowing,

\[
e+\sum_i t_i\le b+\text{taxes actually collectible before performance}.
\tag{7}
\]

Future expected production is not prefunded cash. More generally, every realized prefix must fund all expenditures, due transfers, and required reserves from cash already accessible on that prefix. Credible credit or enforceable deferred payment changes this constraint and must be explicitly supplied. Unsecured promises do not constitute current liquidity.

### The adopted half-ownership incidence

Two participants own the reserve and output equally. The publicly assigned worker \(W\) bears unit burden when repair \(u=1\) occurs; a test has total disruption \(.05\). Conditional on repair, gross compensation \(k\) is paid from the pool to the worker. For participant \(i\), incremental loss is

\[
\ell_i=\tfrac12(e-Y)+\tfrac12k-k\mathbf1\{i=W\}
+u\mathbf1\{i=W\}+.025\,\mathbf1\{\text{test}\}.
\tag{8}
\]

Each participant additionally bears terminal collapse loss one. The \(k/2\) term charges each owner their half of the pool payout; the worker receives the full \(k\). Thus a worker's net compensation benefit is \(k/2\), and the other owner's net financing loss is \(k/2\). This matters for the required gross payment.

Summing personal losses eliminates compensation:

\[
\ell_A+\ell_B=e-Y+u+.05\,\mathbf1\{\text{test}\},
\tag{9}
\]

plus twice the terminal collapse indicator. The treasury nonetheless loses the full \(k\): cash evolves using physical expenditure **plus compensation** before output. Gross compensation can therefore reduce future repair capacity even though it is not an immediate aggregate resource loss. The model restricts future prefunding to the pool: workers cannot automatically lend their received private payouts back. Adding that ability is a different action set.

The implementation credits all output to the owners' economic position. Cash retained under the reserve cap remains jointly owned; excess cash is a separately reported external holding or distribution, not destroyed output. Terminal reserve is reported for accounting, not counted a second time as additional utility after its net accumulation has already entered (8). The initial reserve endowment is common to continuation and refusal and omitted from both loss comparisons.

## 5. Exact positive-surplus but illiquid repair example

Use one remaining production period, stock \(x=1\), fault probability \(p=1/2\), and no test or readiness expenditure. Healthy and faulty damage probabilities are \(.1\) and \(.8\). Output is twice next stock. Refusal causes passive production forever, which here means only this final period. Each owner bears collapse loss one.

Passive damage probability is \(.45\). Next stock is two without damage and zero with damage, hence expected output is \(2.2\), collapse probability is \(.45\), and each owner's refusal loss is

\[
O_A=O_B=-\tfrac12(2.2)+.45=-.65.
\tag{10}
\]

Repair costs three, resets the fault to healthy, and increases current stock recovery: next stock is three with probability \(.9\), one with probability \(.1\), and never zero. Expected output is \(5.6\). Conditional on the public worker assignment, losses under gross compensation \(k\) are

\[
V_W=-.3-\tfrac12k,
\qquad V_D=-1.3+\tfrac12k.
\tag{11}
\]

Both participants accept exactly when

\[
.7\le k\le1.3.
\tag{12}
\]

With no compensation, before a fair worker lottery each owner's expected loss is \(-.8\), a gain of \(.15\) relative to refusal. Aggregate loss falls from \(-1.3\) to \(-1.6\), so aggregate surplus is **.3**. After the worker is disclosed, that worker instead compares \(-.3\) with \(-.65\) and refuses. The distribution of a known physical burden, not disagreement about damage probabilities, produces the conflict.

With initial cash three, the physical repair is affordable, but no positive prefunded compensation is affordable. Within this one-period action set, the repair cannot satisfy continuing participation. With cash four and integer compensation grid containing one, choose \(k=1\). Both losses become \(-.8\), both accept, and \(3+1=4\) funds the repair and payment before output. With divisible payments, the minimum required cash is \(3.7\), not four. The integer-grid threshold is part of the experiment.

This is an exact counterexample to “positive total expected surplus makes an available intervention voluntarily executable.” It is not a theorem that the intervention is impossible under every financial institution: credible deferred compensation, credit, participant lending, or different property rights can change the feasible set.

### A continuation gate can fail for either of two different reasons

At a final gate with stock one and fault probability \(.1\), let each owner's collapse loss be \(\gamma\). Passive damage probability is \(.17\), expected output is \(3.32\), and passive per-owner loss is \(-1.66+.17\gamma\). Repair losses are still (11). Exact acceptable compensation therefore lies in

\[
[2.72-.34\gamma,\ .34\gamma-.72]\cap[0,b-3].
\tag{12a}
\]

For the baseline \(\gamma=1\), the acceptance interval is empty even without the cash restriction. Aggregate repair surplus is negative; additional reserve or a larger transfer grid alone cannot resolve this gate. For \(\gamma=6\), the interval before the cash cut is \([.68,1.32]\): an integer payment of one works with cash four but not cash three. The expected \(5.6\) units of later repair output do not pay a prefunded bill at the current gate.

More generally, aggregate repair surplus at this gate is \(.34\gamma-1.72\), nonnegative only for \(\gamma\ge86/17\). This threshold compares declared personal consequences. It is not evidence that the larger collapse-loss parameter is the correct preference. The baseline's uncompensable objection is a substantive counterweight to the higher-\(\gamma\) liquidity example.

## 6. General one-gate compensation cuts and their scope

First consider a terminal proposal with a separate payer. Recipients have quasilinear utilities and nonnegative shortfalls \(d_i\); the payer's nontransfer continuation surplus is \(S\), includes physical expenditure \(e\), and excludes transfers. Cash available before output is \(b\). If divisible nonnegative transfers have no further physical effects, funded participation is possible exactly when

\[
\sum_i d_i\le S,
\qquad e+\sum_i d_i\le b.
\tag{13}
\]

Necessity follows by summing recipients' minimum payments, the payer's participation condition, and cash feasibility. Sufficiency follows by paying each recipient exactly \(d_i\). Total surplus and prefix liquidity are distinct cuts.

For the half-owned pool with payment only to the worker, define the signed nontransfer loss differences \(d_W=V_W^0-O_W\), \(d_D=V_D^0-O_D\). For \(d_W>0\), exact one-gate feasibility instead requires a permitted payment in

\[
[2d_W,-2d_D]\cap[0,b-e].
\tag{14}
\]

Equation (12) is (14) with \(d_W=.35,d_D=-.65,e=3\). It is incorrect to apply (13) as if the worker did not already own half of the compensation pool.

Both exact tests hold for a terminal proposal, or for a fixed continuation whose nontransfer values and future feasibility do not change with the transfer. In a multiperiod productive system, payment changes next cash and can change later diagnostics, repair, output, and refusal values. Then \(V_i\) depends on the payment through the successor state. Transfers and the resulting continuation must be optimized jointly; calculating a shortfall under a no-transfer policy and adding money afterward is not generally valid. The full-history experiment enumerates cash-feasible compensated actions and follows their actual next cash.

## 7. Commitment and conditional payment are substantive assumptions

The proposed repair and payment are jointly implemented after both participants accept: payment is conditionally released with observable repair performance. If the worker can take the payment and then refuse without repayment, the payment is sunk at the work decision and this contract does not implement the claimed incentive. Escrow, simultaneous exchange, enforceable repayment, or an explicit repeated-game incentive must provide the required linkage.

Likewise, a promised future payment is not credible merely because the worker would accept it if paid. At a final payment date, a payer who can withhold a positive unsecured payment without consequences prefers to do so. Participation by recipients does not establish the payer's commitment. A model with an enforceable controller policy may study participants' exit choices, but it has not explained the origin, cost, or durability of that enforcement. If only one-period commitment is available, future rules must be chosen and checked under that restriction.

This experiment supplies a committed public controller, conditional current payments, public observations, and permanent passive retirement. It does not derive an immortal enforcement authority, a complete bargaining solution, or a general permission to monetize harm. Quasilinear loss and compensation are declared modeling assumptions; some rights, irreversible harms, or participation requirements may not admit monetary substitution.

## 8. Review of the initial implementation

Reviewed `experiments/continuing-participation/model.py` as present on 5 October 2026 during implementation. This is a mathematical source review, not a claim that all subsequent changes or numerical results have been audited.

- The tree keeps separate opening and response gates. Inquiry fees and test disruption are charged at opening; the response outside option starts after these costs, using remaining cash and the observed diagnostic posterior. This treats sunk fees consistently.
- Worker identity is publicly drawn before the opening gate and redrawn fairly before each later living round. Recommendations are checked individually after the controller's randomization. The initial two owners' constraints average over the first assignment, while continuing rows condition on the revealed assignment and recommendation.
- The ancestor-row construction in `build_matrices` sums occupied descendant losses and subtracts the recommendation occupancy times its passive outside loss, which implements (4) on this unmerged tree.
- Response affordability uses `3 * repair + compensation`; the monetary loss metric uses physical expenditure and ownership-adjusted compensation. The reported loss-sum identity therefore excludes compensation, while the cash identity includes it. This is the required distinction between incidence and liquidity.
- The passive fallback retains physical production and subsequent Markov belief updates. At collapse or horizon end it adds the same per-owner terminal collapse loss. It does not assume that refusal discards income already available from the shared plant.
- The updated `evaluate` reconstructs conditional continuation values and reports a refusal witness for every strictly positive action occupancy; an earlier \(10^{-10}\) reach cutoff was removed. A separate backward replay replaces a recommended action by passive retirement whenever either owner's loss, accounting for later vetoes, exceeds their outside loss by more than \(10^{-8}\). The reach cutoff is absent, but floating-point LP and refusal tolerances remain and must accompany numerical claims.
- Independent one-period executions matched the analytic example: at cash three, the ex ante solution has loss \(-.8\) each and failure zero but conditional refusal gain \(.35\); the continuing solution has loss \(-.65\) each and failure \(.45\). At cash four, the continuing solution has loss \(-.8\) each, failure zero, and gross compensation one. Cash-conservation residuals in these four runs were at most \(8.9\times10^{-16}\).

The one-period calculation in Section 5 is independently derived from the physical transition law. Multi-period numerical outcomes, test outcomes, and any later expanded compensation or credit action class require their own reported validation. Continuing participation remains a conditional feasibility result under the disclosed model and refusal rights, not a prediction that a real institution will respect those rights.
