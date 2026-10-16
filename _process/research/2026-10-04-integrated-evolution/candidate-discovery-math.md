# Finite candidate discovery: statistical, identification, and resource constraints

Mathematical working memo, 5 October 2026. AI-generated research assistance for the candidate-generation experiment, following the situated-correction framework and its discriminating design. This memo supplies conservative finite-sample guarantees and elementary identification constraints. They are applications of established statistical mathematics, not new universal laws or an account of unrestricted novelty. Only this memo was edited by this agent.

## 1. Define the claim before defining success

Let a candidate \(h\) be a feature, contextual partition, or policy expression constructed from the institution's retained discovery records. Distinguish four claims:

1. The feature predicts an outcome in observational records.
2. Randomized evidence supports a beneficial action effect in its indicated context.
3. The feature identifies a difference in action effects across contexts.
4. The resulting policy is worth implementing, permitted, affordable, and timely.

These claims are not interchangeable. A feature unrelated to the true moderator can still define a beneficial policy if the intervention helps on average. Such a feature is not automatically a false policy discovery. Conversely, a statistically real interaction may have too small a benefit to pay the intervention cost.

The experiment should declare whether it tests useful policy formation, identification of a represented causal distinction, or both. Ground-truth feature labels in the simulator are useful diagnostics, but they do not replace the estimand.

The candidate grammar, observable variables, and allowable policies are supplied by the analyst. Searching this bounded grammar can add a distinction to the agent's active representation; it does not establish genuinely unanticipated concept formation.

## 2. A causal contrast with explicit assumptions

For a fixed candidate context \(h(X)=1\), let \(A\in\{0,1\}\) denote randomized action and let potential outcome \(Y(a)\) lie in a known interval of width \(R\). Larger outcomes are preferred for this declared endpoint. Define

\[
\tau_h=\mathbb E[Y(1)-Y(0)\mid h(X)=1].
\tag{1}
\]

Suppose confirmation obtains \(n_1>0\) independent treated observations and \(n_0>0\) independent control observations from that context. Required assumptions include:

- The candidate is fixed before confirmation outcomes are inspected.
- Context is measured before action; conditioning on an action-caused variable can invalidate the causal comparison.
- Action is randomized independently of potential outcomes within the candidate context, with both actions possible.
- Units provide independent observations under the stated sampling design; repeated measurements or overlapping delayed episodes are not silently counted as independent units.
- The recorded outcome corresponds to the assigned action and specified delay, without informative record loss or interference between units.
- The confirmation population is the population for the claimed contrast. Transport to later or differently distributed cases requires additional assumptions.

Then

\[
\widehat\tau_h=\bar Y_1-\bar Y_0
\]

estimates (1). Randomization supplies the causal identification; the confidence calculation supplies an uncertainty bound. The potential-outcome distinction and randomized comparison have primary precedent in [Neyman's original experiment analysis, translated in 1990](https://doi.org/10.1214/ss/1177012031). The simple bound below uses independent sampling; it is not an automatic finite-population randomization interval for every assignment design.

## 3. A directly usable conservative confirmation rule

For a one-sided error allocation \(\alpha_h\), define

\[
\boxed{
r_h=R\sqrt{\frac12
\left(\frac1{n_1}+\frac1{n_0}\right)
\log\frac1{\alpha_h}},
\qquad
L_h=\widehat\tau_h-r_h.
}
\tag{2}
\]

The weighted form of [Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830) gives

\[
\Pr(\widehat\tau_h-\tau_h\geq r_h)\leq\alpha_h,
\quad\text{hence}\quad
\Pr(L_h>\tau_h)\leq\alpha_h.
\tag{3}
\]

Proof: the treated summands have range width \(R/n_1\) and control summands width \(R/n_0\). The sum of squared widths is \(R^2(1/n_1+1/n_0)\); applying the weighted bounded-sum inequality yields (2)–(3).

If action 1 costs an additional known constant \(c_h\) per treated case and requires practical margin \(m_h\geq0\), accept it only when

\[
\boxed{L_h>c_h+m_h.}
\tag{4}
\]

This controls acceptance of an action whose true benefit fails the declared threshold. Testing only \(\tau_h>0\) would not account for its cost. If costs vary across cases, incorporate the observed net outcome with its correct known range or bound the additional cost-estimation error separately.

For balanced arms \(n_1=n_0=n\),

\[
r_h=R\sqrt{\frac{\log(1/\alpha_h)}n}.
\tag{5}
\]

Balanced allocation minimizes this radius for a fixed total number of observations and equal ranges. Applying the inequality directly to the contrast avoids the additional conservatism of separately bounding each arm and adding those bounds.

This is a finite-sample conservative guarantee, not an exact permutation \(p\)-value or a claim of optimal statistical efficiency. The range \(R\) must be valid from the measurement model; using the observed sample range is not justified. Unbounded Gaussian outcomes do not satisfy this assumption. A known sub-Gaussian proxy permits a different concentration bound, while predeclared clipping changes the estimand.

If a subgroup has no observations in either arm, the rule cannot certify it.

## 4. Candidate selection, repeated testing, and familywise error

### Discovery-only selection does not require a search-size penalty

Let discovery data \(D\) generate any number of candidates and select one \(h(D)\). Freeze the candidate, action rule, endpoint, confirmation size, and acceptance threshold; then collect fresh independent confirmation data.

Conditional on \(D\), the chosen candidate is fixed. Therefore (3) applies conditionally and, after averaging over \(D\), controls its false acceptance at level \(\alpha\). The number of candidates searched only on discovery data does not enter the confirmation penalty. This is a validity result, not a power guarantee: an overfitted candidate can simply fail confirmation.

### Selection on confirmation requires simultaneous protection

If \(K\) candidates fixed before confirmation are all tested and confirmation itself chooses a winner, use \(\alpha_h=\alpha/K\). A union bound gives

\[
\boxed{
\Pr\left(\exists h:
L_h>c_h+m_h\ \text{but}\ \tau_h\leq c_h+m_h\right)
\leq\alpha.
}
\tag{6}
\]

The candidates' test statistics need not be independent for this union bound. Their individual bounds must remain valid.

For sequential candidate rounds, choose error allocations predictably, before each fresh confirmation batch, with

\[
\sum_{j\geq1}\alpha_j\leq\alpha.
\]

For example, \(\alpha_j=\alpha/[j(j+1)]\) has total \(\alpha\). Conditional validity in each round and the union bound control the probability of ever accepting a false claim. Reusing \(\alpha\) afresh in every round does not supply a lifetime \(\alpha\) guarantee.

Repeatedly altering candidates after viewing the same holdout is different from fresh confirmation. Calling a dataset “held out” does not preserve its independence after feedback-driven reuse. [Dwork et al.](https://arxiv.org/abs/1506.02629) provide primary analysis of adaptive holdout reuse and specialized methods for preserving validity. This memo does not implement those methods; the simplest experimental design uses a fresh batch after each frozen nomination.

### Looking repeatedly at the same accumulating test

A fixed-sample bound must not be repeatedly inspected with optional stopping at the first favorable result. For a fixed candidate and balanced accumulating arms, a simple conservative remedy allocates

\[
\alpha_n=\frac{6\alpha}{\pi^2n^2}
\]

to look \(n\), using

\[
r_n=R\sqrt{\frac{\log(\pi^2n^2/(6\alpha))}{n}}.
\tag{7}
\]

The union bound covers every integer look, so any stopping time inherits the error guarantee. This is deliberately conservative; [Howard, Ramdas, McAuliffe, and Sekhon](https://arxiv.org/abs/1810.08240) develop sharper time-uniform confidence sequences. Candidate rounds and repeated looks both need to share the total error budget.

## 5. Power, finite records, and the cost of small effects

Write \(t_h=c_h+m_h\), and suppose the true effect exceeds it by \(\Delta>0\). For balanced arms, a sufficient sample size for acceptance probability at least \(1-\beta\) is

\[
\boxed{
n\geq
\frac{R^2}{\Delta^2}
\left(
\sqrt{\log(1/\alpha_h)}
+
\sqrt{\log(1/\beta)}
\right)^2.
}
\tag{8}
\]

This follows by requiring the true margin to exceed the acceptance radius plus a lower-tail radius at level \(\beta\). Use a strict numerical margin if equality and the strict decision rule could matter.

For \(R=1,\ \alpha_h=.05,\ \beta=.2,\ \Delta=.25\), the bound requires 144 observations per arm after rounding upward. This is an illustrative sufficient requirement, not a universal minimum. If the candidate applies to only a small fraction of cases, many more encounters may be needed to obtain those subgroup observations.

There is also a procedure-specific impossibility: since \(\widehat\tau_h\leq R\), rule (4) cannot accept at all unless

\[
R-r_h>t_h.
\tag{9}
\]

Failure of this inequality proves that this conservative test cannot pass with the chosen sample size. It does not prove that every statistically valid method must fail.

### A simple information lower bound

Even a single fixed candidate cannot be reliably distinguished from an arbitrarily small effect with a fixed finite budget. Consider \(n\) treated outcomes: under the null they are independent Bernoulli\((1/2)\); under the alternative they are Bernoulli\((1/2+\varepsilon)\). Control observations have the same law in both worlds and supply no additional distinguishing information.

For the likelihood ratio \(L\),

\[
\mathbb E_0L=1,\qquad
\mathbb E_0L^2=(1+4\varepsilon^2)^n.
\]

If an acceptance event \(\mathcal A\) has false-positive probability at most \(\alpha\), Cauchy–Schwarz gives

\[
\boxed{
\Pr_1(\mathcal A)
\leq
\alpha+\sqrt{\alpha[(1+4\varepsilon^2)^n-1]}.
}
\tag{10}
\]

Consequently, power at least \(1-\beta>\alpha\) requires

\[
n\geq
\frac{\log[1+(1-\beta-\alpha)^2/\alpha]}
{\log(1+4\varepsilon^2)}.
\tag{11}
\]

This is an elementary likelihood-ratio testing bound, not a new theorem of discovery. It applies to the stated two-world experiment and displays the small-effect resource burden without assigning any particular candidate generator a guarantee.

## 6. A useful policy is different from a true moderating feature

The policy “use action 1 when \(h(X)=1\), otherwise use action 0” improves on action 0 everywhere by

\[
V_h=\Pr(h(X)=1)(\tau_h-c_h),
\tag{12}
\]

under the stated constant cost and stable deployment distribution. Positive \(\tau_h-c_h\) suffices for positive average improvement when the context has positive probability. It does not establish that \(h\) identifies the true causal distinction.

To test moderation, define

\[
\Gamma_h=\tau_h-\tau_{\neg h}.
\tag{13}
\]

The four cell means give a contrast with radius

\[
\boxed{
r_{\Gamma,h}
=R\sqrt{\frac12
\left(
\frac1{n_{1h}}+\frac1{n_{0h}}
+\frac1{n_{1\neg h}}+\frac1{n_{0\neg h}}
\right)\log\frac1{\alpha_h}}.
}
\tag{14}
\]

This requires positive sample counts in all four cells and the same fixed-candidate causal assumptions. A claim that both policy benefit and moderation are established should allocate error to the claims accordingly.

An irrelevant feature can correlate with the true context or select a subgroup with positive average treatment effect. Its policy can then be genuinely useful without recovering the scientist's named feature. The experiment should separately log feature recovery, statistical confirmation, true simulated policy value, and harmful false implementation.

Alternatively, randomize entire candidate policies against the baseline and test their net outcomes directly. That validates a policy comparison while making fewer claims about the discovered causal explanation.

## 7. Record loss can make a distinction unidentified

Consider a pre-action binary context \(X\) with probability \(1/2\), and randomized action independent of \(X\). Two possible worlds are

\[
W_+:\ Y=A X,
\qquad
W_-:\ Y=A(1-X).
\tag{15}
\]

If the stored records contain only \((A,Y)\), their distributions are identical in the two worlds: action 0 always produces zero, and action 1 produces a Bernoulli\((1/2)\) outcome. No amount of those stored records identifies which context benefits.

With an intervention cost \(c\in(1/2,1)\), the beneficial contextual policies differ. The right targeted policy has value \((1-c)/2>0\) in its world. Acting indiscriminately has value \(1/2-c<0\).

More generally, a policy using action 1 with probabilities \(p_0,p_1\) in the two contexts has values

\[
V_+=\tfrac12[(1-c)p_1-cp_0],
\qquad
V_-=\tfrac12[(1-c)p_0-cp_1].
\]

Their sum is \(\tfrac12(1-2c)(p_0+p_1)\leq0\). Thus no such policy has strictly positive value in both observationally indistinguishable worlds. The failure is identification, not lack of optimization.

This result concerns the specified compressed records and probing protocol. New trials retaining \(X\), or actions that generate different informative histories, can break the equivalence. It must not be generalized to impossibility under every imaginable future investigation.

## 8. Memory, candidate budgets, deadlines, and action rights

**Finite memory.** Raw records must retain the variables needed for later candidate construction and the join linking action to its delayed outcome. If every join key is erased before the outcome arrives and no sufficient replacement remains, the causal pair is unavailable. More observations of the surviving fields do not restore the lost link.

Do not equate statistical sample size with the number of raw rows simultaneously stored. After a candidate and endpoint are fixed, arm counts and sums can be accumulated in bounded memory. That compression may be sufficient for its planned test while being inadequate for unplanned future distinctions. Memory requirements depend on which future questions the representation preserves.

**Candidate budget.** Let nomination, confirmation, retention, and implementation each have explicit costs. Searching more discovery candidates costs computation and can worsen the chosen candidate's confirmation power, even when fresh validation keeps its false-acceptance probability controlled. A grammar lacking an adequate policy cannot obtain one from tighter significance thresholds.

**Rare contexts.** If relevant contexts occur independently with known probability \(\rho\), then among \(N\) encounters their count is Binomial\((N,\rho)\). For a design requiring \(2n\) qualifying cases, the exact completion probability is

\[
\Pr(\operatorname{Bin}(N,\rho)\geq2n).
\tag{16}
\]

An expected count \(N\rho=2n\) is not a high-probability completion guarantee. Balanced randomized assignment within qualifying cases can deliver the required arm counts after enough cases arrive.

**Deadline.** The relevant condition is

\[
t_{\mathrm{confirm}}
+\ell_{\mathrm{admission}}
+\ell_{\mathrm{authorization}}
+\ell_{\mathrm{implementation}}
\leq T_{\mathrm{last\ effective\ response}},
\tag{17}
\]

when the stages are sequential. Overlapping stages need their actual critical path. Outcome delay, candidate-generation time, and waiting for rare contexts belong in \(t_{\mathrm{confirm}}\). Statistical confirmation after the last effective response cannot deliver that recovery.

**Authority and resources.** A confirmed policy must belong to the implementable action set and have funded execution capacity. To isolate evidence admission experimentally, preserve the same actor-visible confirmation result in both arms and change its institutional standing. To isolate authority, preserve the accepted result and chosen policy while changing enactment rights. Deleting data tests a different gate.

**Practical value.** With a conservative lower count \(M_h\) of remaining relevant deployments, the prospective gain bound is \(M_h(L_h-c_h)\). It must be compared with inquiry, records, channel-maintenance, and implementation costs if the claim is that the whole discovery program pays. A positive per-case effect does not repay an arbitrarily expensive investigation. This comparison uses the application's declared common objective; other burdens and constraints remain separate outcomes.

## 9. Recommended first implementation

Use a discovery batch for unrestricted search within the declared finite grammar. Nominate one candidate or a small frozen shortlist. Fix confirmation sizes, endpoints, margins, allocation, and per-round error before fresh randomized observations. Use (2)–(6) for a transparent conservative acceptance rule. Save inconclusive and failed confirmations; do not silently nominate another candidate on the same unadjusted holdout.

Log raw availability, candidate expression, confirmation data identity, statistical result, admission decision, authorization, expenditure, and completed action separately. Include the absent-benefit world and misleading features. Distinguish rejection for lack of evidence from demonstrated absence of benefit.

The useful structural conclusion is conditional: reliable candidate discovery requires an identifiable contrast, a valid selection-and-testing protocol, enough timely informative exposure, and an executable response. Satisfying any one of these does not establish the others. These are established statistical and decision constraints applied to a particular maintained-discovery experiment.

## 10. Audit of the implemented confirmation and funding schedule

Implementation audit, 5 October 2026, of `experiments/history/situated-discovery/experiment.py` and `PROTOCOL.md` before held-out evaluation. This applies the preceding established statistical bound and ordinary cost accounting to the actual event loop; it introduces no new statistical theorem. The six renewal rates below were added during development, before evaluation outcomes were inspected.

**Why cash gating does not invalidate this confirmation.** Conditional on the world rule and pre-attempt history, the candidate is fixed. Its next 256 action slots contain a shuffled 128 A and 128 B assignments, independent of future cases. An unfunded slot waits; it is not replaced or advanced. A case enters that slot using only its candidate-membership bit, the slot's action, and calendar/cash state. The code does not use other current attributes or the current outcome to decide inclusion.

Condition additionally on the future membership sequence and the action order. These determine the sampled indices and whether completion occurs before the horizon. Within a qualifying context, the remaining attributes and outcome uniforms at those indices are still independent draws from the specified stationary population. Costlier B slots can therefore occur later without changing their outcome distribution. Normal record lifetime eight exceeds outcome lag two, so initiated confirmation records survive to linkage. The test is performed once, after all 128 outcomes in each arm have matured. Under this probabilistic model, the contrast of binary failure rates has the radius

\[
r=\sqrt{\frac{\log 80}{128}}\simeq0.1850258984.
\tag{18}
\]

The implementation accepts only when the estimated reduction in failures exceeds \(.25+r\). A fresh, adaptively reached attempt has the same conditional guarantee because its cases have not appeared in discovery or previous confirmation. Allocating \(.05/4\) to each of at most four attempts controls the probability of any acceptance of a nonpositive-value policy by .05. The 73 discovery candidates need no additional confirmation penalty. Incomplete attempts make no acceptance decision.

This argument uses the simulator's stated iid sampling model, not a claim about every deterministic pseudorandom seed sequence. It would not justify unchanged inference under calendar drift, outcome-dependent missing records, reused confirmation data, or inclusion based on additional current attributes that alter the within-context population. Independent uniform draws shared between paired experimental arms do not create dependence between distinct cases within an arm.

**Exact first-test bill.** With the normal retained records and these funding schedules, discovery captures blocks 0 through 4. At the beginning of block 5, outcomes from the first four blocks provide 512 linked discovery records, while the fifth block's 128 captured records are still pending. Nomination thus follows 640 paid captures. The full grammar and a complete first confirmation require

\[
\begin{aligned}
K_{\mathrm{first}}
&=640(.01)+73(.01)+256(.01+.005)+128(.25)\\
&=6.40+.73+35.84=42.97.
\end{aligned}
\tag{19}
\]

This is an expenditure floor for completing a first test, regardless of the candidate's true effect or the assignment order. It is not a sufficient condition for enough qualifying cases or a successful confirmation. Ignoring the extra delayed captures would give the weaker floor 41.69.

For the severe return-funded control, the entire 64-block allocation is

\[
8+4+2+1+.5+.25+58(.125)=23<42.97.
\tag{20}
\]

Its inability to complete even the first test is therefore prescribed by the funding constraint. It is not an emergent attracting state discovered through simulation.

**Funding before the deadline.** Validation by block 24 requires the last trial to be initiated by block 22 because outcomes arrive two blocks later. Consequently the entire first-test bill must already be paid by the end of block 22. Before first validation, define available cumulative funding by

\[
A_{22}(\rho)=\sum_{b=0}^{22}\max\{.125,8\rho^b\}.
\qquad A_{22}(\rho)\geq42.97
\tag{21}
\]

as a necessary condition for timely first validation. The global allocation cap does not bind here. Direct evaluation gives:

| Renewal rate \(\rho\) | Funding through block 22 | Passes necessary funding condition? |
|---|---:|---|
| .800 | 39.923539 | No |
| .810 | 41.857910 | No |
| .815 | 42.904090 | No |
| .816 | 43.120454 | Yes |
| .820 | 44.005937 | Yes |
| .900 | 72.909650 | Yes |

The funding-only boundary solving \(A_{22}(\rho)=42.97\) is approximately \(\rho=0.8153055884\). This brackets a necessary deadline constraint; it does not identify a sharp success threshold. Even when it is satisfied, the number and timing of qualifying cases can delay trial completion, and an uninformative or rejected first candidate can require further expenditure. Conversely, an eventual completed test after block 24 can still supply valid evidence while failing the prescribed timeliness criterion. Deadline and resource failures in this experiment must remain distinct from permanent closure, dynamical attraction, and the statistical validity of the resulting evidence.
