# Continuing participation: design and adversarial review

5 October 2026. Independent proposal for the next finite experiment. This document supplies a minimal design and an analytic witness, not results from a completed implementation. The prior stock, noisy diagnostic, repair, and recurrent-fault dynamics are inherited. Individual incidence, ownership, refusal, and compensation are new declared modeling choices. No earlier files were edited.

## The change that must be made explicit

The plural-correction cycle imposed several aggregate consequence bounds. This cycle should represent **two actual modeled participants**, each with a separately computed continuation loss and an available refusal action. The question is whether a policy can remain acceptable to each participant after the evidence, exposure assignment, and current proposal that the policy actually discloses.

The relevant distinction is between ex ante acceptability and continuing participation. A lottery can be acceptable before its outcome is known while the person selected for its burden would refuse afterward. Neither an aggregate expected-harm bound nor an initial individual-rationality test resolves that issue.

These are established questions in limited-commitment and self-enforcing-contract theory. [Thomas and Worrall's own later account of their self-enforcing wage-contract model](https://www.timworrall.com/wpapers/sewcreduxR.pdf) explicitly treats the need for both sides to prefer continuation and discusses the importance of specifying the underlying game and outside option. [Kocherlakota (1996)](https://academic.oup.com/restud/article-abstract/63/4/595/1520475) studies risk sharing with symmetric information and no commitment, including the role of history. The proposed addition is an auditable coupling of that familiar participation requirement to paid noisy inquiry, shared productive liquidity, and physically consequential repair. It is not a new derivation of consent, bargaining, or distributive justice.

## A minimal accounting specification

Two named participants, A and B, each own one half of a shared liquid account. Ownership is fixed and common knowledge. The productive stock, current cash, apparatus readiness, and all observations are public. The hidden fault is known through the same public Bayesian belief to both participants; there are no private types or privately diagnostic experiences in the minimal version.

Inherited operating costs are paid from the shared account before production. Compensation to an exposed participant is also paid before production and must be affordable in the same prefix. It leaves the shared account and becomes that participant's private receipt. Once paid, it cannot be silently clawed back or reused to finance the common apparatus. If reinvestment or private credit is later permitted, it requires new explicit actions and participation constraints.

For current repair choice u and compensation c, the account update is

\[
b'=\min\{8,b-\mathrm{operating\ spend}-c+Y\},
\]

where Y is the inherited actual production income. Overflow is paid out equally to the owners, and the remaining balance is divided equally at the terminal date, including at an early absorbing collapse. The pathwise financial identity is

\[
\Delta b+\mathrm{operating\ spend}+\mathrm{compensation}
 +\mathrm{owner\ dividends}=Y.
\]

The compensation receipt is included in the recipient's private payoff. Aggregating both participants' financial receipts cancels compensation as a transfer, although moving it out of the productive reserve can still alter future feasible actions and output. A compensation payment c from a half-owned account is **not** a free c gain for its recipient: before future liquidity effects, the recipient gains c/2 net of their own lost account share, while the other owner loses c/2.

Define participant i's finite-horizon loss as

\[
L_i=\mathrm{personally\ assigned\ intervention\ burden}
 +\mathrm{personally\ assigned\ diagnostic\ burden}
 +k_i\mathbf1\{\mathrm{terminal\ collapse}\}
 -\mathrm{private\ financial\ receipts}_i.
\]

The k_i and burden valuations are supplied individual preferences expressed in declared payoff units. They may initially be symmetric for an exact control and later differ in a declared sweep. The method does not require maximizing L_A+L_B or assigning a common interpersonal utility. It does assume each participant can rank lotteries by the stated expected loss. Their common monetary accounting does not establish that actual people possess these preferences.

Do not add cumulative expenditure minus output to these losses: operating costs already reduce the owners' dividends and terminal balances. Do not add the terminal cash again after including its payout. If terminal stock salvage is included, state its separate ownership and valuation; the clean analytic witness below excludes it. Print operating expenditure, output, compensation, dividends, and terminal account balance separately to make the financial identity inspectable.

## Exposed burden must not introduce unmodeled private evidence

The safest isolation module assigns a fixed, publicly known burden of one to the participant exposed to each repair. Assignment is a fair public A/B lottery independent of the hidden fault and future damage. The burden is known from the action and assignment, so it supplies no additional signal about the fault.

An alternative is to assign the earlier target-absent burden to one participant. But if that participant experiences a burden whose occurrence reveals that the fault was absent, the event is a **private observation**. It must enter the information structure and possibly strategic reporting. Keeping a single public posterior while ignoring such information would invalidate the intended participation comparison. One can explicitly assume that target-dependent burden is not observed until the terminal date, but a fixed per-repair burden avoids that extra interpretive assumption. The two versions coincide numerically in the one-round example below when the target-absent burden is valued at two and its probability is one half; they are not equivalent in general.

Diagnostics should likewise have a specified personal incidence, such as .025 burden to each participant per diagnostic, if retaining the earlier aggregate .05 burden. This is separate from its monetary operating cost. A claimed protection for intervention subjects must not neglect costs imposed on the person financing the intervention.

## Public chronology and refusal

Use a short full public-history tree, preferably horizon two before attempting three. Keep exact rational beliefs where possible. Each history records the actual stock, cash, readiness, previous observations and payments, public exposure assignments, publicly disclosed choices, and any continuation commitments the participant is meant to believe.

A workable round has the following sequence:

1. Public stock, cash, readiness, and belief are available. Draw and disclose the prospective repair-exposure assignment.
2. The public mechanism proposes apparatus support and optional diagnostic expenditure. If either participant refuses, invoke the fixed fallback from the present state before charging those proposed costs. If both accept, pay actual costs, perform any diagnostic, and publicly disclose its result.
3. Propose the current repair and any compensation after the actual evidence. Both participants can refuse again. The fallback now begins from the actual post-diagnostic cash and information, because accepted inquiry costs are already sunk. If both accept, pay repair and compensation before output and execute production.
4. Observe actual stock and income, update the public belief from the full likelihood, distribute overflow, and move to the next public history.

The fallback should be completely specified: no further paid diagnosis, apparatus support, compensation, or repair; ordinary production and hidden-fault transitions continue; ownership, dividends, and terminal payouts are preserved. It is a priced wait-without-correction continuation, not confiscation. Its expected continuation loss is computable by a simple backward recursion under the same physical and information laws.

This is a **supplied refusal option**, not proof that it is the best real-world outside option. There is no private withdrawal, liquidation, unilateral operation, borrowing, or renegotiation unless explicitly added. If the intended game gives participants those alternatives, their values must also constrain participation. A participant's rational acceptance relative to a poor fallback does not establish uncoerced or legitimate consent. The mechanism also needs a stated source of credible continuation: a committed public recommendation/payment rule with participants free to refuse at every decision is a tractable assumption; unrestricted future renegotiation is a different model.

## Conditional participation and sufficient state

At every reachable consent history h, including the currently disclosed assignment, diagnostic result, and proposal lottery outcome, require

\[
\mathbb E[L_i^{\mathrm{remaining}}\mid h,\mathrm{continue},\pi]
 \le V_i^{\mathrm{fallback}}(h),\qquad i=A,B.
\]

Past receipts and burdens are sunk and cancel from the comparison under the declared additive, risk-neutral preferences. They must not be refunded on the refusal branch or counted again as future benefit. A promised future transfer counts only through a future policy that is itself affordable and satisfies both participants' future participation constraints.

Checking this inequality only before the current action lottery is insufficient. Publicly revealing a chosen policy or action changes what remains uncertain. The smallest honest randomization convention is fresh public action randomization at the current node, followed by consent conditioned on its result; future draws remain unknown until made. If the entire policy seed is disclosed initially, participants must instead condition on that revealed seed. Averaging their evaluation across already disclosed seeds would manufacture cooperation.

The full history tree is a safe finite representation. It is not a claim that history can never be compressed: under appropriate conditions a physical state together with promised continuation values and relevant identities can suffice. The earlier `(time, stock, cash, readiness, belief)` state alone cannot be assumed sufficient for an arbitrary history-dependent contract. Two identical physical states may come with different disclosed promises, compensation histories, or future lottery information. Any merging must prove those differences irrelevant for the actual available continuations.

In a tree-occupancy formulation, let d(h) be the probability of reaching consent history h and W_i(h;y) the unconditional occupancy-weighted sum of participant i's **remaining** losses below h. Then

\[
W_i(h;y)\le d(h)V_i^{\mathrm{fallback}}(h)
\]

is linear in the tree occupancies. At a zero-probability history it is vacuous; assign an admissible fallback there. Unique history descendants make the continuation sums unambiguous. Include immediate proposed payments and burdens exactly once in W_i, according to the consent node's timing. Keeping proposal/lottery outcomes as explicit nodes prevents a constraint from accidentally protecting only an average across proposals.

The mechanism can seek any policy meeting a supplied productive-reliability bound plus these individual constraints, without optimizing an aggregate interpersonal loss. A tie rule that accepts exact indifference is an explicit behavioral convention. Report minimal reachable participation slack and optionally require a small positive slack at non-fallback proposals, rather than concealing binding constraints with numerical tolerances.

## Exact one-round witness

Use inherited physical parameters, horizon one, x=1, b=8, ready=1, p=1/2, and no diagnostic. Each owner has a terminal-collapse penalty of one. Each repair imposes fixed burden one on its publicly assigned subject. The shared account is split equally, and any compensation goes to that subject.

Refusal means no repair. The damage probability is .45, next stock is two with probability .55 and zero with probability .45, and expected output is 2.2. Each person's expected loss is

\[
L_i^{\mathrm{fallback}}=.45-\frac{8+2.2}{2}=-4.65.
\]

Repair costs three, eliminates current fault, and yields next stock three with probability .9 or one with probability .1, hence expected output 5.6 and no collapse. Without compensation, the exposed person's loss is

\[
1-\frac{8-3+5.6}{2}=-4.30,
\]

while the other owner's loss is −5.30. The exposed person is .35 worse than refusal; the other is .65 better. Before the fair assignment, however, each expects loss −4.80 and prefers this repair lottery to refusal by .15. This is a precise counterexample to inferring continuing participation from ex ante individual approval.

Pay compensation one from the reserve to the subject before output. Upfront spending is 3+1≤8. The remaining account plus owner dividends have expected total 8−3−1+5.6=9.6. The subject receives private compensation one in addition to their half share, and incurs burden one. Both participants therefore have loss

\[
L_{\mathrm{subject}}=1-1-9.6/2=-4.80,
\qquad L_{\mathrm{other}}=-9.6/2=-4.80.
\]

Both strictly prefer continuation by .15 **after assignment and the compensation proposal are known**. The donor's cost is fully represented. This exact witness requires no claim that diagnosis is beneficial and no fictitious ground-truth payment. The compensation is paid for accepting exposure, not conditioned on a hidden state.

The fair-assignment, no-compensation case and the compensated case have identical physical repair outcomes. Their difference lies in the conditional distribution of personal losses. In longer horizons compensation can also reduce future available liquidity; that additional physical consequence must be computed rather than assumed away. The numbers and preferences above are constructed to isolate the mechanism, not empirically fitted social values.

## Required comparisons and failure criteria

1. **Ex ante versus post-disclosure participation.** Recover the exact example. The no-compensation repair lottery must pass initial participation but fail the exposed participant's later condition. A solver that calls it continuing-participation feasible has conditioned at the wrong information set.
2. **Both participants versus subject-only checks.** Compare the same action space with the donor constraint retained or omitted. The latter is explicitly a defective/one-sided mechanism control, not a legitimate compensation result. Retain cases where generous compensation is blocked by the donor or by cash.
3. **Paid versus invented transfers.** Verify prefix affordability branch by branch and the pathwise money identity. No output from the upcoming production round or unpriced external payment can fund current compensation. Aggregate private financial receipts plus operating spend must equal initial wealth plus output, with terminal balances and overflow counted exactly once.
4. **Full fallback valuation.** Independently enumerate the no-repair continuation for one and two rounds, including passive Bayesian updates, ordinary damage, cash caps, ownership, and early collapse. The fallback at a post-test refusal must use the already-paid test's actual cash and observed result.
5. **Promises and lotteries.** Construct two publicly distinct histories with the same physical state if the proposed contract permits different continuation promises. They must not be merged without an equivalence argument. Conditional evaluations must not average over a disclosed assignment or policy seed.
6. **Existing information discipline.** Independently enumerate latent fault/sensor/damage outcomes for a short horizon and verify the filter. A fixed repair burden generates no new signal. If target-dependent or privately observed costs are used, explicitly extend the information structure before interpreting the public policy.
7. **Policy reconstruction.** Extract an implementable public-history policy from any occupancy solution. Recompute each positive-reach consent node's two conditional continuation losses separately from the LP matrix construction and compare them to its fallback values. Report maximum violation, minimum meaningful slack, and probabilities of any displayed witness paths.
8. **Preserve countercases.** Keep settings where no repair is required, where positive total gains cannot make both participants better off under available transfers, where compensation restores participation, and where it would restore payoff balance but cannot be financed. Diagnostic use may rationally be zero. Those outcomes constrain the theory rather than undermine the experiment.

A successful calculation would show one conditional route from an ex ante attractive correction policy to one that remains acceptable after its burdens become personally known. It would not establish that all necessary correction can be voluntarily financed, that monetary compensation is always appropriate, or that the specified refusal game represents political legitimacy. Those are separate questions the finite model should leave visible.

## Adopted implementation specification

The root subsequently adopted fixed public repair burden one, collapse loss one for each participant, and total diagnostic burden .05 split equally. The shared reserve is half-owned; compensation k is restricted to `{0,1,2}`, occurs only with a repair, and leaves the productive account for the assigned worker's private wallet. Repair and payment are atomic after acceptance: there is no intervening gate at which a participant can take the payment and then refuse its agreed repair. Private withdrawals are not available to finance later cooperation.

The implementation will use the equivalent incremental loss accounting

\[
\ell_i=\tfrac12(\mathrm{operating\ expense}-Y)
 +\tfrac{k}{2}-k\mathbf1\{i=\mathrm{worker}\}
 +u\mathbf1\{i=\mathrm{worker}\}+.025\,\mathbf1\{\mathrm{test}\},
\]

plus terminal collapse loss one. Relative to the total-receipts accounting above, each loss is shifted by the constant initial half-account wealth. This constant cancels from a participation comparison at the same history. The formula correctly charges both owners for compensation before crediting the private recipient, and its summed transfer term is zero. Account cash still falls by k, so the future financing consequence is retained despite this algebraic cancellation in total immediate loss. No additional terminal cash reward should be appended.

Accordingly the exact one-round example reports incremental losses: refusal −.65 for each; uncompensated repair −.30 for the assigned worker and −1.30 for the other participant; compensation one gives −.80 for each. These are the earlier values plus four when initial cash is eight. The same incremental values hold at initial cash three/four for the relevant affordable choices. Cash three permits the physical repair but cannot prefix-finance compensation one; cash four can pay repair three plus compensation one before output. This is a sharper liquidity control than comparing cash two/eight, because the uncompensated repair is physically available in both cells.

The adopted mechanism will disclose the fair worker assignment before the opening support/test recommendation, and disclose a separate repair/transfer recommendation after any diagnostic result. Refusal permanently ends active cooperation but leaves passive production and equal property claims intact. The proposed full public-history tree and per-action subtree participation inequalities are appropriate for those stated information sets. This section records a design agreement; code and independent implementation tests had not yet been provided at the time of this memo update.

## Implementation audit and independent tests

5 October 2026, subsequent pass. Reviewed `experiments/continuing-participation/model.py`, the original `development.json`, and the later additions for lexicographic witness selection and actual-veto replay. Created the explicitly assigned `test_model.py`; all nine tests pass. No root model, analysis, or protocol files were edited. No substantive implementation defect was found in this pass.

The tree preserves public histories instead of merging identical physical states. Each non-root node has one unique parent action, and its ancestor-action list includes exactly the recommendations on its path. Separate roots disclose the fair initial worker assignment; future assignments are independent public chance branches. Inquiry and response recommendations are distinct nodes, so paying an inquiry cost does not remove the later opportunity to reject a repair. Public state descriptions contain the Bayesian fault probability, not the hidden fault itself. Fixed assigned repair burden introduces no private diagnostic observation.

For each recommendation j, the participation matrix includes its own immediate expected loss and all occupied descendant losses, then subtracts that recommendation's occupancy times the passive fallback value at its current node. Unique history descendants make this exactly the reach-weighted conditional continuation comparison. A response-node fallback uses the actual post-inquiry cash and publicly observed posterior. Inquiry costs already accepted at the parent are not refunded on that later refusal, while refusing the opening inquiry itself pays none of those proposed costs.

The `retire` recommendation embeds the full passive remainder, including future ordinary output, fault transitions, cash caps, owner claims, and terminal collapse. Its larger stage vector is an analytical absorption of that entire tail, not a one-round physical expenditure. Terminal cash is tracked for conservation but is not added to the incremental loss objective, avoiding double counting. Compensation is paid only with repair, enters shared cash before output, and is credited privately to the assigned worker. Its two individual loss contributions cancel in their sum; its cash reduction still constrains later actions.

The root added a reporting selection rule: first minimize terminal failure, then physical expenditure among failure-optimal policies, then compensation among both preceding optima. This removes arbitrary waste from failure-optimal displayed witnesses without identifying that scalar hierarchy as either participant's own preference. The original development outputs precede this tie rule and are retained. Reported optimum and final-witness quantities should be tied to their corresponding saved implementation version.

The ex ante mode constrains both initial expected losses but permits later refusals to be profitable. Its raw outcomes are therefore a **commitment benchmark**, not the predicted execution of those recommendations under the continuing veto. The added backward replay handles this distinction: it first computes future behavior with refusals, then replaces a currently unacceptable recommendation with the current passive fallback. At every consent gate, both participants compare the recommendation's actual replay continuation with the same outside option. Indifference within the declared tolerance means acceptance. A continuing-feasible policy should be unchanged by replay, which the tests verify.

Independent checks include:

* The passive fallback is reproduced by directly enumerating the hidden fault and damage history, with no calls to the implementation's diagnostic or production-filter helpers. Tests cover zero through three remaining rounds, collapsed and live stocks, cash zero/four/eight, and supplied fault probabilities zero, one tenth, one half, and one.
* Every action stage on a two-round tree is checked against primitive latent-event probabilities and the declared individual accounting formula. Branchwise affordability, rebuilding delay, response-recipient identity, and `next cash − cash + operating expense + compensation + overflow − output = 0` all hold.
* The exact one-round worker/donor outcomes reproduce the design witness. Cash three allows physical repair but no compensation one; continuing participation therefore attains failure .45 while the ex ante commitment benchmark attains zero. Cash four permits compensation one, with failure zero and losses −.80 for each participant. At higher cash, compensation two is correctly unacceptable to the financing owner in this example.
* A deliberately arbitrary, full-support randomized policy on a two-round public tree is propagated forward to obtain occupancies. A separate backward recursion using independently calculated stage vectors yields each recommendation's continuation losses. For every action and both participants, these agree with the corresponding participation-matrix row divided by that action's occupancy. The complete terminal probability, monetary identity, and summed individual-loss identity also agree.
* Diagnostic branches at prior one half have probability one half and posterior .9/.1; the test's actual three-unit prefix expense leaves cash five from cash eight. Each response fallback matches the independently calculated passive value from its resulting posterior and current cash. A proposed inquiry followed by retirement is rejected at the opening in veto replay and therefore incurs no diagnostic charge.
* Veto replay is independently recomputed for one- and two-round policies across cash three/four/eight. Every tested continuing-feasible policy retains its original outcome vector. The one-round ex ante repair benchmark, which uses no compensation under the minimal-transfer tie rule, instead replays to passive failure .45 and zero repair expense.

The preserved two-round countercase is material. After a first repair, a low-stock branch can reach a final state with stock one and fault probability .1. Passive continuation gives loss −1.49 to each participant, sum −2.98. Repair has total loss −1.6, regardless of how the supplied compensation is split; no transfer can make both participants prefer it in that one-round continuation. Thus both the no-compensation and compensated continuing mechanisms retain terminal failure .017 in the checked two-round case. Compensation repairs a distributional obstacle in the one-round witness; it does not erase negative total continuation surplus in this later state. Calling every refusal a financing or coordination failure would misdescribe this result.

The final report should retain the distinction between the supplied refusal game and general legitimacy. The tests validate this finite public-information implementation, its accounting, and the conditional inequalities. They do not establish calibration of individual preferences, a bargaining equilibrium under alternative deviations, or indefinite cooperation.
