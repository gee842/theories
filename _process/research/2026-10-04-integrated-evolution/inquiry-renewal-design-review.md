# Renewal of inquiry from situated proposals and observed credit

5 October 2026. Design review for a small repeated-project experiment. The root owns implementation. This memo distinguishes an exact financing result from claims about discovery, social value, and institutional protection. No simulation is reported here.

## The smallest defensible mechanism

The proposed experiment can show that an inquiry process with positive expected value may fail to finance its next attempt. Its distinctive ingredients should remain observable: participants see local data, those observations select a proposal, fresh evidence determines admission, a separate observation determines funding credit, and a cash ledger determines whether another attempt is feasible. The simulator's hidden project type can evaluate these rules but must not enter their decisions or payouts.

Use a new independent project each round. Two observable contexts A/B each occupy half the affected population. In a genuine project, one context has need probability .65 and the other .15; a null project has .2 in both. The genuine context and project mixture are drawn from a declared stationary distribution. An institution that cannot observe the current hidden type is not forgetting an earlier diagnosis of the same project. This independence also makes the reserve balance sufficient for the financing state: it contains information about past projects, but none about the next independently drawn type. Persistent project types would require additional belief state.

Participants in each context obtain four paid baseline observations. Their observed need counts select the largest count at least two, breaking ties with an independent fair coin. If neither count reaches two, no proposal is produced. The grammar contains only two rules, responding in A or responding in B. Hidden need probabilities are not inputs to selection. This implements data-based selection of a candidate from a finite vocabulary, not unconstrained concept formation.

For a latent project with probabilities \(p_A,p_B\), the probability of an ordinary A proposal is

\[
\pi_A=
\sum_{a=2}^4 P[N_A=a]
\left(P[N_B<a]+\tfrac12P[N_B=a]\right),
\]

and similarly for B. These formulae evaluate the implemented observation rule; they must not replace its information set with the true probabilities. An agenda-override control that forces A with probability \(\kappa\), otherwise following the local observations, has \(\pi_A^\kappa=\kappa+(1-\kappa)\pi_A\) and \(\pi_B^\kappa=(1-\kappa)\pi_B\). This describes an exogenous allocation bias. Without an explicit strategic actor or private payoff, call it an agenda override rather than an equilibrium theory of capture.

## Independent validation and monitoring

The concrete proposal uses sixteen fresh baseline need observations in the selected context. It tests the need probability against .4, since response costs .4 and perfectly prevents unit loss. At nominal .05, the exact upper-tail critical count is eleven; discreteness makes the actual null rejection rate below .05. Repeated tests are on independent new projects, not repeated optional looks at the same evidence.

Known perfect response efficacy is a supplied structural assumption. Under it, untreated baseline need observations can establish whether response is worthwhile, without a treatment trial. If efficacy is unknown, these observations are insufficient: fresh randomized treatment/control evidence would be needed. Preserve that boundary explicitly.

After admission, an independent third sample of eight untreated control need labels supplies the performance-credit signal. Credit is triggered when its observed need fraction exceeds .4, equivalently at least four positives, and when the selected context is recognizable in the incumbent's funding ledger. A ledger recognizing A only must affect funding credit, not silently suppress B's validation, deployment, or measured welfare. Then the comparison isolates recognition of beneficial work from its actual effectiveness.

Let \(V(p)=P[\operatorname{Bin}(16,p)\ge11]\) and \(M(p)=P[\operatorname{Bin}(8,p)\ge4]\). For a given project mixture and proposal rule, the probability of earning a grant during a funded round is

\[
r=E_\theta\sum_{j\in\{A,B\}}
\pi_j(\theta)V(p_j)M(p_j)L_j,
\]

where \(L_j\) is the ledger-recognition indicator. The proposal, validation, and monitoring samples are independent conditional on project type. Both useful and false proposals can occasionally receive credit; no grant is paid using the hidden expected effect.

The flat grant of five is an institutional payment recognizing an estimated improvement. It is not the realized profit of the intervention, an unbiased estimate of that profit, or a conserved treatment benefit. This distinction resolves the initial concern about truth-based payouts. The monitoring sample is an observable signal, and the grant must be financed separately from actual ordinary output.

For forty future cases and a half-population intervention, expected operating improvement per funded round is

\[
v=E_\theta\sum_j\pi_j(\theta)V(p_j)
\,20(p_j-.4).
\]

The financing quantity \(5r-1\) and social net value \(v-1-h\), where \(h\) is declared contact harm, are different. A persuasive illustrative case should show both positive rather than quietly treating a positive grant drift as proof of beneficial inquiry. The null and agenda-override controls should preserve cases where protecting inquiry instead funds costly or harmful activity.

Per-project size control is not lifetime error control. With continuing inquiry and a positive stationary probability of a false admission, indefinitely many false deployments may occur over an infinite sequence. Report their rate and expected harm. Do not describe the lifetime institution as having at most a .05 probability of any false action. The monitor's additional threshold also does not convert noisy positive credit into unbiased contribution accounting.

## A cash ledger that does not create funding

Let reserve \(B_t\) be integer-valued between zero and capacity \(B\). A funded attempt costs a prepaid retainer of one, covering local observation, validation, and reserved monitoring capacity even when some slots are unused. This fixed contract is a simplifying resource assumption; paying only for observations actually used would require a different branch-cost kernel.

Let \(a_t=1_{B_t\ge1}\). The institution produces ordinary cash output six each round, including rounds without inquiry. With credit indicator \(I_t\), the nominal transfer rule is

\[
g_t=f+(5-f)I_t,\qquad
B_{t+1}=\min\{B,B_t-a_t+g_t\},
\]

with \(I_t=0\) when inquiry is inactive. The performance-funded rule has \(f=0\); the protected rule has \(f=1\). The actual deposit is

\[
D_t=B_{t+1}-(B_t-a_t).
\]

At the reserve cap, \(D_t\) can be smaller than nominal \(g_t\). The unused allocation must remain with ordinary operations, not disappear. Ordinary consumption is \(O_t=6-D_t\), giving the exact identity

\[
B_t+6=a_t+O_t+B_{t+1}.
\]

This makes both rules feasible under the same supplied production flow, while preserving their different expenditure histories. Optional contact harm is a separate welfare effect unless it is explicitly a monetary payment; do not quietly subtract it from both accounts.

Transfers cancel from undiscounted social accounting only when the reserve's terminal value is included. Summing the identity gives ordinary consumption plus terminal reserve, minus initial reserve, equal to \(6T-\sum_t a_t\). Adding intervention benefits and contact harms then gives a transparent welfare criterion. Subtracting both the deposit and the retainer would double-count inquiry's monetary cost. A discounted objective or a reserve with imperfect terminal value would change this cancellation.

The ordinary output is the maintained funding source. It is not produced by successful inquiry in this isolation model, and the production inputs that make it continue are not endogenized. Thus a protected transfer removes a financing barrier only because an independently continuing activity can support it. It does not show how a wholly self-financing system generates resources after every productive activity has stopped.

## Finite buffers: a precise conditional absorption result

For \(f=0\), state zero is absorbing. In a positive state, the next reserve is \(\min(B,b+4)\) with probability \(r\), otherwise \(b-1\). If \(r<1\), a run of \(B\) noncredit rounds empties any reserve. Independence gives

\[
P(T>nB)\le[1-(1-r)^B]^n,
\qquad E[T]\le\frac{B}{(1-r)^B},
\]

where \(T\) is the time to loss of funding from an initially positive reserve. The same argument works with a uniform positive conditional lower bound on a noncredit round; full independence is stronger than necessary. Positive nominal mean drift \(5r-1>0\) does not invalidate the result, because favorable surpluses are capped while a long sequence of losses remains possible.

This is a standard finite-buffer/absorbing-chain phenomenon, not a new universal law of institutions. Infinite time and finite capacity are consequential assumptions. A large buffer may have a very long useful lifetime; report finite-horizon survival, lifetime quantiles or means, and sensitivity to \(B\), rather than replacing those quantities with the statement that failure is certain eventually. The exact finite-state transient matrix yields survival and expected lifetime directly.

An uncapped reserve is a useful theoretical countercontrol. For the same independent increments and \(5r>1\), eventual ruin need not have probability one. The probability from reserve \(b\) is \(z^b\), where the smaller root \(z\in(0,1)\) satisfies \(z=(1-r)+rz^5\). Borrowing, outside replenishment, a change in the rule when the reserve is low, or persistent learning that removes the chance of noncredit can also defeat the stated absorption conditions. They should be described as changed assumptions, not counterexamples to the finite model's proof.

For \(f=1\), a funded reserve never decreases: after paying one, the floor restores at least one. An inactive reserve receives one and can resume on the next round when \(B\ge1\). Thus continuous inquiry after initial funding is guaranteed by the chosen floor equaling the retainer. This is not an independently discovered benefit of protection. The empirical or practical questions concern whether that allocation is affordable, beneficial, resistant to diversion, and worth its opportunity cost. Protection preserves the ability to test bad proposals as well as good ones.

## Comparisons and falsification checks

The proposed constant transfer \(\mu=5r\) is a useful smoothing benchmark if its use of the stationary model parameter is explicit. It matches the performance rule's **nominal mean grant in an active round**. It does not match accepted deposits after clipping, expenditure after the performance rule stops, or total realized funding. If \(\mu\ge1\), continuous replenishment can maintain inquiry without a funding gap. An institution would need an estimate or prior to implement that schedule; knowing \(r\) analytically is a benchmark, not a free observed signal.

Use the same initial reserve, production technology, project distribution, evidence rules, and feasible costs across policies. Report realized/expected retainer counts, actual accepted transfers, ordinary consumption, terminal reserve, false deployments, operating gains, and contact harm. Equal initial wealth or equal output capacity is not equal spending. A separate finite-horizon expected-expenditure frontier can compare policies at a common expected resource use, but must retain its horizon and criterion. Do not erase the lifetime funding difference by calling an active-round mean match exact resource matching.

The strongest discriminating checks are:

1. **Financing versus usefulness:** With the same proposal/validation kernel and positive net operating value, vary only reserve capacity or the allocation rule. The closed finite-buffer rule must match its absorbing-chain calculation; removing the cap or enabling inactive-state replenishment should break the corresponding premise.
2. **Recognition versus effect:** Switching a symmetric ledger from both contexts to A only should change credit probability without changing the candidate's expected operating value per funded round. Any direct change in proposal quality or validation behavior would confound this comparison.
3. **Protection versus capture:** Null projects, deliberately noisy local reports, and the declared A override must be allowed to reduce or reverse protected inquiry's value. Fresh validation must not see the proposal-generation outcomes again. If a grant follows the latent benefit rather than the third observed sample, the supposed information constraint has been bypassed.
4. **Resource conservation:** Every branch must satisfy the ledger identity, including cap overflow, inactivity, false admission, and a paid retainer with no proposal. No inquiry may occur below the financing threshold merely because the hidden project is valuable.

## Closest prior art and contribution boundary

[Manso, *Motivating Innovation*](https://faculty.haas.berkeley.edu/manso/mi.pdf) already develops formal reasons that innovation incentives can require tolerance of early failure and rewards for longer-term success. [Aghion, Dewatripont, and Stein, *Academic Freedom, Private-Sector Focus, and the Process of Innovation*](https://www.nber.org/system/files/working_papers/w11542/w11542.pdf) analyzes the tradeoff between researchers' control and directed pursuit of commercially valuable projects. These preclude presenting protected inquiry or failure tolerance as novel general principles.

[Azoulay, Graff Zivin, and Manso, *Incentives and Creativity: Evidence from the Academic Life Sciences*](https://www.nber.org/system/files/working_papers/w15466/w15466.pdf) provides observational empirical evidence comparing funding arrangements. Its identification and setting are separate from this synthetic experiment; it is not validation of the present finite-buffer mechanism or chosen parameters.

The potential contribution is a transparent linkage of situated proposal production, independent evidence, incumbent-recognized observed credit, and a resource-conserving renewal process, with mechanisms separately removable. Its shared objective, two-rule grammar, efficacy law, and sustaining production flow remain supplied assumptions. No scalar objective here determines a universal ethical direction or proves that all inquiry deserves permanent support.

## Implementation audit: observed-credit kernel and finite reserve

5 October 2026. Reviewed `experiments/inquiry-renewal/model.py`, `test_model.py`, `PROTOCOL.md`, and `config.json`. The root's analysis script was still being prepared. No substantive error was found in the main configuration.

The episode calculation correctly sums the data-generated proposal probabilities, multiplies by the independent fresh validation probability, and uses the independent monitoring sample only for funding credit. Its use of hidden probabilities evaluates the expectation of these observable procedures; it does not supply those probabilities to proposal selection or grant eligibility. The supplied agenda override changes proposal selection before validation. The narrow ledger changes credit recognition only: proposals, validation/adoption probabilities, and expected operating improvement remain identical to the standard ledger. In the symmetric main world it halves credit probability exactly.

The new-project assumption is doing necessary work. Because each project's hidden orientation and samples are independent of earlier rounds, opening reserve does not reveal the current orientation. Credit events conditional on an active attempt therefore have the stationary probability used by the reserve chain. The same argument justifies expected useful/false adoption counts and social loss as expected active rounds times their per-active-round expectations, despite their within-round correlation with funding credit. The implemented outputs concern expectations; quantiles of cumulative welfare would require retaining more of that joint event distribution.

The cash update handles the cap correctly. Overflow is returned to the treasury, accepted deposit equals nominal grant minus spill, and an inactive round cannot earn an observed credit. Both branches satisfy

\[
\Delta B+\text{treasury retention}+\text{inquiry expense}=6.
\]

With the zero floor, state zero is absorbing. With floor one and retainer one, an empty account receives one at the end of its inactive round and resumes on the next round; an already active account remains fundable. A monetary control using retainer two and floor one correctly permits intermittent restart rather than uninterrupted activity. The model uses integer monetary units for its finite-state transition matrix; fractional units require rescaling the state space rather than silently rounding balances.

For independent verification, I recomputed the main episode using exact rational arithmetic, with need probabilities \(13/20\) and \(3/20\). Discovery count masses, tie probabilities, validation tails, and monitoring tails were calculated with elementary binomial coefficients, without the implementation's proposal or probability helpers. The validation critical count was independently recovered as eleven. The resulting credit probability and expected operating improvement agree with the reported floating-point values:

\[
r=.373252459768706,
\qquad v=2.0877536858285746.
\]

Thus the uncapped nominal funding drift is \(5r-1=.86626229884353\), while net social value per active round after retainer and .05 contact burden is \(1.0377536858285746\). Both are positive in this deliberately chosen illustrative case.

I then solved the cap-eight first-step lifetime equations by independent exact rational elimination, rather than calling the model's transition constructor or numerical linear solver:

\[
t_0=0,\qquad
t_b=1+(1-r)t_{b-1}+r t_{\min(8,b+4)}.
\]

Starting from eight, the expected funded lifetime is **98.60839117471514 rounds**, differing from the model's result by approximately \(1.6\times10^{-13}\). A separately constructed 80-digit probability recurrence produced these survival values:

| End of round | Probability still funded for the next round | Expected active rounds so far |
|---|---:|---:|
| 10 | .9584174691200243 | 9.94349523863898 |
| 100 | .3603774637704269 | 65.30333589539235 |
| 1000 | .00002015361246850229 | 98.60652863544779 |

The model agrees at the displayed precision. These calculations verify the finite model, not an empirical survival rate for research organizations. The positive-drift result refers to uncapped nominal funding income, not drift when the reserve is already full.

A control-consistency issue was reported to the root before analysis: the chain functions accept a monetary `cost` argument, but their social-loss multiplication initially used the per-active loss already stored in the episode. Changing the chain cost without rebuilding or adjusting that episode would misstate the social-cost control, even though the reserve transition and conservation calculation remained correct. The main configuration uses matching cost one throughout. Any control reporting social outcomes under a different retainer must keep the episode's cost and chain's cost consistent.

**Resolution, 5 October 2026:** The root reports that the episode now records `inquiry_cost` and `inquiry_harm`, while `run_chain` and `mean_matched_constant` reject a mismatched financial cost. The updated tests cover that rejection and agreement with a correctly rebuilt cost-two episode; all six tests pass. The initial results were preserved under `results-v1`, and the final rerun includes explicit no-inquiry and no-proposal controls without changing preexisting numerical cases. The control-consistency warning is therefore resolved. This records the root's correction and verification report; no additional audit or rerun was requested for this amendment.

The protocol also correctly narrows the outcome to shutdown of investigation while ordinary production continues, labels the constant-grant comparison as a nominal active-round mean match, and retains the known-efficacy and per-project-error limitations. No root code or test files were edited during this audit.
