# Prospective retention and evidence-triggered revision

5 October 2026. Design and adversarial review, before implementation audit. This memo recommends a small exact experiment and records limits on its interpretation. No simulation or implementation is supplied here.

## The key separation

Preserving a distinction, detecting that an incumbent frame omits structure, and establishing that a replacement policy improves outcomes are three different achievements. The proposed experiment can separate them using independent episodes and two independent evidence stages. Its strongest contribution would be this separation under explicit retention and inquiry costs, not a new permutation-testing theorem or a general solution to institutional openness.

An initial candidate needed correction. Slow–fast and fast–slow four-transition histories have the same total-count distribution as each other, but not generally the same count distribution as a mixture of homogeneous slow and fast histories. Therefore the former pair alone does not justify saying that counts cannot distinguish ordered from homogeneous models. A matched count distribution must be constructed explicitly. The revised E/P/T construction below does that while retaining an iid-compatible exchangeable null.

## A minimal exact world family

Let each episode contain four historical switch bits \(W=(W_1,\ldots,W_4)\), a public final historical state \(Z\), and a later binary need. Independently across episodes, first draw

\[
K\sim\operatorname{Binomial}(4,1/4).
\]

Conditional on \(K\ne2\), choose a word uniformly among words with that count in every world. Conditional on \(K=2\), define a clustered word as 0011 or 1100. In exchangeable world E, choose uniformly among all six words, so clustering probability is \(1/3\). In worlds P and T, choose equally between the two clustered words, so clustering probability is one. E's unconditional historical word distribution is exactly four independent Bernoulli(1/4) bits.

Take the initial state fair and independent, which makes endpoint \(Z\) independent of the word. Write \(d=(W_3+W_4)-(W_1+W_2)\). In E and T, the next flip probability is .25. In P, it is .45 for \(d>0\), .05 for \(d<0\), and .25 for \(d=0\). Need is the next state after that flip. The next-flip mechanism in P is an expressly supplied hypothetical persistence rule; it is not derived merely from historical clustering.

By reversal symmetry, every world has the same conditional next-flip probability .25 after observing only \(K,Z\). Consequently the complete observable distribution of count-only records, endpoints, and next outcomes agrees across E/P/T. Any inference rule using only those records has the same rejection probability in each world. Its power equals its actual size, which need not equal its nominal significance threshold. More count records cannot break this equivalence. A rule can still act without learning—for example, always admitting the candidate—but that is not evidence extracted from counts.

P and T have the same complete historical word distribution. Therefore even a perfect archive audit cannot distinguish persistent predictive structure from historical structure that fails to carry forward. T is the essential control against turning historical rejection into automatic policy endorsement.

With response cost .3, unit untreated loss, and supplied perfect response efficacy, the incumbent responds when \(Z=1\) and otherwise does nothing. Its expected operating loss is .275 in all three worlds. A supplied candidate grammar contains the additional response rule \(Z=0,d>0\). The candidate's eligibility probabilities are

\[
\pi_E=69/512,
\qquad \pi_P=\pi_T=87/512.
\]

Its gross per-future-episode improvement over the incumbent is \(\Delta_\theta=\pi_\theta(p_\theta-.3)\), with eligible need probabilities \(p_P=.45\) and \(p_E=p_T=.25\). It helps in P and harms in E/T before adding ongoing information costs.

## Retain before inspecting; test without stopping rules

Choose a fixed audit quota \(m\) and its episode indices before observing their contents. Retain those complete words independently of their values. An existing routine stream can supply the underlying episodes; if acquisition itself costs time or money, charge it explicitly and use a common acquisition window across policies. Selecting only striking records after reading them would be a different experiment.

Among the \(m\) retained words, let \(J\) count records with \(K=2\) and let \(X\) count clustered records among them. Under E,

\[
J\sim\operatorname{Binomial}(m,27/128),
\qquad X\mid J=j\sim\operatorname{Binomial}(j,1/3).
\]

Use the predeclared upper-tail conditional p-value. For \(j=0\), do not reject. A deterministic discrete test has size at most \(\alpha\); exact equality requires an explicitly randomized boundary. Under P/T, \(X=J\), so at \(\alpha=.05\) the audit rejects exactly when \(J\ge3\). This gives exact power without Monte Carlo. Null size is the finite sum over \(j\) of its binomial probability times the conditional rejection probability.

The gate tests exchangeability against this particular clustered alternative. It does not establish every possible form of temporal dependence, identify a causal mechanism, or select the uniquely correct successor model. The alternative statistic and finite grammar are supplied in advance. A larger adaptive grammar requires a correspondingly calibrated maximum statistic, mixture test, multiple-testing rule, or independent discovery stage.

Conditional permutation validity rests on the specified symmetry, not on the mere act of shuffling. The theoretical basis is established prior art; see [Hemerik and Goeman, *Exact testing with random permutations*](https://arxiv.org/abs/1411.7565). Independent episodes and selection of retained indices before their values are seen make the binomial reduction valid here.

## Confirm the action on independent evidence

After audit rejection, fund a fixed validation pool of \(L\) fresh episodes, independent of the audit conditional on the world. Retain the features needed to identify eligibility and measure the later outcome. Charge for all \(L\) attempted records, including the ineligible ones; do not charge only for the selected informative observations.

The eligibility count is random. Conditional on \(J_v=j\), eligible needs are binomial with probability \(p_\theta\). A one-sided test against .3 asks whether response improves **gross operating outcomes** on eligible cases. Eligible cases have \(Z=0\), so the incumbent leaves them untreated and their need is uncensored in the proposed setup. Perfect response efficacy is already supplied by the environment; this procedure does not estimate an unknown treatment effect. If efficacy is uncertain, a randomized treatment comparison is needed instead.

The audit and validation evidence must remain disjoint. Candidate direction, threshold, and validation test cannot be chosen after seeing the validation outcomes. A single predeclared candidate avoids a multiplicity issue; trying several candidates on the same validation pool would reintroduce it. Adaptive holdout reuse is a separate statistical problem, as developed by [Dwork et al., *Generalization in Adaptive Data Analysis and Holdout Reuse*](https://arxiv.org/abs/1506.02629).

A successful validation then permits deployment on a third, fresh future population. Analytic risk calculation under the known synthetic world can replace sampling that population. The audit's rejection and the validation's acceptance are events computed from observations, not truth labels passed to the institutional rule.

Two limits matter. First, testing against .3 does not certify net improvement after an ongoing raw-record fee \(r\) per future episode. Net benefit requires \(\pi_\theta(p_\theta-.3)>r\). One may state that validation certifies only the gross criterion and account for fees in the ex ante decision objective, or design a different paid-benefit test. Second, E/T's .25 validation null is away from the .3 boundary. Add a boundary control with positive-sign probability .3, negative-sign probability .2, and tied probability .25 if the intended report includes calibration near that boundary. Reversal still preserves the aggregate .25 flip probability.

## Prospective choice and consistent resource accounting

Let \(A_\theta(m)\) be audit rejection probability and \(V_\theta(L)\) validation acceptance probability, conditional on the world. With fixed future deployment horizon \(H\), audit fee \(c_a\), validation fee \(c_v\), and ongoing fee \(r\), the proposed incremental expected cost is

\[
C_\theta(m)
=m c_a+A_\theta(m)\left[
L c_v+V_\theta(L)H(r-\Delta_\theta)
\right].
\]

This factorization requires audit/validation/future independence conditional on the world. It also requires consistent chronology: reserve the same \(L\)-episode validation phase for every policy, keep incumbent behavior during it, and charge collection only when funded. Then validation-phase operating outcomes are common across policies. If validation instead delays deployment by a variable amount inside a fixed total horizon, the lost deployment time must enter the calculation. Likewise, historical audit quota must not silently change the length of the common baseline period.

The realized inquiry bill is \(m c_a+G Lc_v+G B Hr\), where \(G\) and \(B\) are gate and validation indicators. Keep this bill separate from the expected operating improvement. A prior-weighted optimum over \(m\) is prospective if the prior and costs are available before retention and no future private contents enter the choice. It is an optimum over this **specified workflow**, not over all Bayesian decisions, record formats, stopping rules, or possible candidate languages.

Compare at least the zero-audit policy, a protected positive quota, the prior-optimal quota, and a rule that admits the question directly and pays for validation without an archive gate. The last control can beat the gate when inquiry into the supplied candidate is already cheap and worthwhile. That possibility should be retained, not tuned away. A cost-blind maximum archive should also sometimes lose when preservation is expensive or future opportunity is small.

Equal caps do not mean equal expenditure. Report actual component costs and the expected inquiry-cost/operating-loss frontier. For a matched-resource information control, let the count-only arm buy extra count records with the same paid resource rather than merely wasting the difference; its distributional equivalence across worlds still prevents identification. Where exact integer matching is inconvenient, an ex ante lottery over adjacent feasible quotas gives an explicitly prior-matched expected expenditure, not branch-by-branch equality. Never describe the latter as actual identical spending on every realization.

## What would falsify the proposed interpretation

1. **Retention mechanism:** If a count-only inference rule distinguishes E/P/T above its size, the implementation has leaked order, world identity, or another unequal signal. If randomly permuting the retained audit words fails to remove audit power under a reconstructed null, inspect the test and selection logic.
2. **Admission versus efficacy:** P and T must have identical audit behavior but different successful deployment value. If rejection alone is reported as evidence for beneficial revision, the two stages have been conflated. The validation boundary control distinguishes calibration from merely easy null rejection avoidance.
3. **Value of preservation:** If raw retention is always chosen despite arbitrarily high retention fees, zero future opportunity, or an available cheaper direct-validation route, the objective or feasible comparator is incomplete. A nonzero optimum at chosen parameters is not itself a universal preservation principle.

Finally, a prior over E/P/T represents uncertainty about a mechanism, not uncertainty over which future question will be asked. This model demonstrates retention before evidence and data-triggered admission within a supplied finite question family. To model the literal claim that the later question is unknown, introduce a task variable—such as an order-insensitive summary task versus a continuation decision—revealed only after retention, and specify its ex ante distribution. A myopic institution that deletes order can be optimal for the first task or within a restricted old frame; it is not thereby globally optimal for every current prediction problem. No unknown-question, unrestricted ethical, or universal institutional conclusion follows from the narrower benchmark alone.

## Expanded design: useful inquiry without a historical anomaly

The subsequent design adds a fourth world U and an explicit future task variable. This section supersedes the earlier proposal's three-world and single-task limits where stated. It remains a design audit, not a report of executed tests.

U has E's historical word distribution, including clustering probability \(q=1/3\), but P's future rule: positive \(d\) predicts a .45 flip probability, negative \(d\) predicts .05, and tied \(d\) predicts .25. Therefore every archive-only rule based on the specified historical words and endpoint has exactly the same observation distribution in E and U, while the candidate's future benefit differs. An anomaly gate calibrated under E will also open only at its size in U. Lack of historical anomaly cannot certify that prospective validation lacks value.

This impossibility must be stated relative to the archive fields. The retained four-switch windows do not contain linked subsequent outcome targets. If an archive already contained each full word together with its later need, E and U would be distinguishable from those paired observations. Conversely, even adding the later target to a **count-only** archive does not help here: \((K,Z,Y)\) has the same joint distribution in all four worlds. Conditional on every count, reversal pairs positive and negative \(d\) with equal probability, so the conditional next-flip probability is .25. Independent episodes preserve that equivalence for any finite sample of count-only records.

For a continuous audit family with clustering probability \(q\in[1/3,1]\), define positive-sign future probability \(p\), negative-sign probability \(.5-p\), and tied probability .25. The eligibility probability is

\[
\tau(q)=P(Z=0,d>0)=\frac{60+27q}{512},
\qquad \tau_{\min}=\frac{69}{512}.
\]

E, T use \(p=.25\); P, U use \(p=.45\). E/U have \(q=1/3\), P/T have \(q=1\). Routine aggregate performance and count-only records remain identical throughout this family. The raw archive can inform the clustering parameter but cannot establish the future persistence parameter without an appropriate linked outcome measurement.

### A conservative paid-deployment validation threshold

Let response cost \(c=.3\), ongoing raw-information fee \(f=.002\) per deployment episode, and gross gain \(\Delta(q,p)=\tau(q)(p-c)\). The proposed fixed validation threshold is

\[
p_* = c+\frac{f}{\tau_{\min}}
     = .314840579710\ldots.
\]

This supplies a valid conservative test for nonpositive **ongoing paid-deployment** value within the declared family. Indeed,

\[
\tau(q)(p-c)-f\le0
\quad\Longrightarrow\quad
p\le c+f/\tau(q)\le p_*.
\]

Conditional on the number of eligible records in the fixed validation pool, a one-sided binomial upper-tail test against \(p_*\) therefore has false-admission probability at most its nominal level for every nonbeneficial member of that family. Averaging over the random eligibility count preserves the bound. Opening validation according to independent archive evidence or a precommitted bypass probability also preserves it. This does not require treating the realized eligibility fraction as known without uncertainty: the deterministic bound \(\tau\ge\tau_{\min}\) comes from the declared family.

The bound ceases to be justified if eligibility probabilities below \(\tau_{\min}\) are admitted. It also does not certify recovery of the already paid archive and validation charges. Those costs belong in the prospective workflow objective; once sunk, they are separate from the marginal decision to deploy.

Calibration controls should distinguish two boundaries. At every \(q\), \(p=p_*\) is the binomial-test boundary. At \(q>1/3\), it already gives strictly positive paid-deployment value. The true net-zero boundary is

\[
p_{\mathrm{net}}(q)=c+f/\tau(q),
\]

which equals \(p_*\) only at the minimum-eligibility endpoint. Include both boundary types, as well as an intermediate \(q\), and do not label all \(p_*\) cases false-benefit nulls. Conservative loss of power near \(p_{\mathrm{net}}(q)\) is an expected tradeoff of the fixed threshold.

### Archive choice before one of two supplied questions is known

Choose and pay for \(m\) raw historical windows before a task variable \(Q\) is revealed. Let \(Q=0\) ask only about \(K\), which all arms already retain, and let \(Q=1\) ask the continuation-action question. Set \(P(Q=1)=\lambda\), independently of world and historical data. This implements uncertainty over which of **two supplied questions** will matter; it does not implement an unconceived question or an unrestricted future language.

The proposed numerical design uses \(L=1024\), \(H=500\), \(c_a=.02\), \(c_v=.002\), \(f=.002\), and \(m\in\{0,\ldots,128\}\). The archive fee is prepaid acquisition/retention/reserved audit computation, including when \(Q=0\). Only \(Q=1\) can open fresh validation and deployment. Its common validation phase uses incumbent actions in every arm. The later episode pool is fully charged whenever opened, whether or not many records meet eligibility. The supplied sweep \(\lambda\in\{.01,.1,.25,.5,1\}\) and baseline .5 are prospective parameters, not post-observation weights.

Allow direct prospective validation even without an anomaly. If \(A_\theta(m)\) is gate probability and an independent bypass is selected with probability \(\eta\) after no gate, the probability of opening validation is

\[
R_\theta(m,\eta)
=A_\theta(m)+[1-A_\theta(m)]\eta.
\]

The expected incremental workflow cost is then

\[
C_\theta(m,\eta)
=m c_a+\lambda R_\theta(m,\eta)
\left[Lc_v+V_\theta(L)H(f-\Delta_\theta)\right].
\]

All conditional independence and common-phase accounting requirements from the earlier section still apply. Realized inquiry costs are \(mc_a+1_{Q=1}O[Lc_v+B Hf]\), with opening indicator \(O\) and validation acceptance indicator \(B\). This makes clear that equal ceilings do not equal actual expenditure, and that direct validation pays no inquiry charge on \(Q=0\).

For a declared prior, the objective is affine in \(\eta\) at fixed \(m\), so a Bayesian expected-cost optimum occurs at an endpoint, with possible ties. At \(\eta=1\), any positive \(m\) adds an archive fee without changing the subsequent workflow, and is dominated by direct validation with \(m=0\). Thus the relevant pure alternatives are audit-first quotas, direct validation, and no inquiry. This endpoint argument does not extend unchanged to an added expected-budget constraint or minimax regret: those criteria can favor randomization. At \(\lambda=0\), positive paid retention is dominated analytically.

U makes the direct-validation comparator indispensable. If an archive gate is the only permitted route, the construction would force a failure that a feasible paid inquiry route could overcome. Showing the choice between these routes, including cases where archives are not purchased, is a stronger result than presenting a protected archive as uniformly desirable. The experiment's prospective optimum remains conditional on the supplied question distribution, world prior or stated robust criterion, prices, fixed tests, and finite workflow.

## Implementation audit: exact prospective workflow

5 October 2026. Reviewed `experiments/prospective-revision/model.py`, `test_model.py`, `PROTOCOL.md`, and `config.json`. No substantive implementation error was found in the reviewed configuration. The analysis/reporting script was not yet part of this review.

The atom generator implements the declared world law: it assigns the common binomial count mass, distributes that mass across words according to the clustering parameter, draws a fair independent endpoint, and supplies the stipulated conditional next-need probability. The conditional test integrates over a random informative-record count rather than treating an expected count as observed. Zero informative records cannot reject. Audit and validation use separate thresholds and eligibility probabilities. The paid-benefit threshold is computed from the declared lower eligibility bound, and the tests distinguish its boundary from the true net-zero boundary at each clustering parameter.

The calculation receives a world argument to evaluate conditional expectations, not to select the institution's realized action using a hidden label. The procedure itself is determined by the retained sample, fixed p-value rules, and the precommitted workflow. Costs are averaged over worlds only after these conditional expectations are calculated. Prospective archive choice can therefore use the stated prior without handing the realized world to the institution.

Timing and fees are consistent with the protocol. Archive cost is charged before the later question and is not multiplied by its probability. Validation and deployment terms are multiplied by that probability. Every opened validation cohort costs its full fixed size times the fee, including ineligible observations. The running fee is paid on all deployment decisions after acceptance. Incumbent outcomes during the common validation phase are omitted as a common constant, and the total-loss output names its narrower scope as continuation deployment plus expenses. The conservative branch bound includes archive, complete validation, and complete running fees, and workflows are filtered by that bound.

I independently recomputed the following values using elementary binomial probability recurrences and finite sums, without calling the implementation's test-probability functions to obtain the independent values. Audit power for the clustered world used the separate closed form \(P[\operatorname{Bin}(28,27/128)\ge3]\). Validation critical counts were obtained by summing elementary null binomial masses from the upper tail; alternative probabilities were then weighted by independently computed eligibility-count masses. Expected cost was separately enumerated over question, audit, and validation events.

| Quantity | Independent result | Absolute difference from implementation |
|---|---:|---:|
| P audit power, \(m=28\) | .953298817144033 | \(4.45\times10^{-16}\) |
| P validation acceptance | .974165211839390 | \(9.44\times10^{-15}\) |
| U validation acceptance | .938375371870296 | \(7.00\times10^{-15}\) |
| E validation acceptance | .000257667823946441 | \(5.43\times10^{-20}\) |
| P incremental loss, \(m=28,\eta=0,\lambda=.5\) | −3.917040743637173 | \(5.25\times10^{-14}\) |

These are exact finite-model expectations evaluated in floating point; agreement is numerical verification of the specified experiment. In particular, the small E validation acceptance is not a general false-positive estimate from an empirical sample. The independent boundary controls are needed for the near-threshold calibration claim.

The finite-workflow minimax program is also formulated consistently. Its statewise comparator is the best feasible workflow in each world, and its lottery is chosen before data, question, and world. The nonnegative mixture weights sum to one, and each world's mixture regret is bounded by the common optimization variable. The reported dual value uses the equality multiplier because the inequality right-hand sides are zero; the reduced-cost check has the appropriate signs. This supports a finite-workflow robust comparison, not unrestricted robust optimality or an outcome-predicting oracle.

Two reporting boundaries remain material. The full historical law shared by E/U is the law of the retained word and endpoint, not a raw word already linked to its subsequent target. The tests correctly verify the former and the separate count/endpoint/target equivalence. Also, information costs are fully counted but not equal across policies: the common branch cap and explicit expense components must not be summarized as an equal-spending experiment. No root implementation or test files were edited during this audit.
