# Bounded alternatives to changed recipient evaluation

6 October 2026. AI-authored mathematical identification study. The conditional analytical scope, independent finite checks and frozen formal receipt are accepted in [internal collaborating-AI review](BOUNDED-IDENTIFICATION-REVIEW.md). This extends the accepted [value–expectancy ambiguity](IDENTIFICATION.md) and implements the quantitative discriminator requested in [reward learning and recipient choice](../../../../theories/becoming/chapters/REWARD-LEARNING-AND-RECIPIENT-CHOICE.md). It adds no participant observations, source audit, fitted psychological model or reanalysis of the accepted dataset. No historical priority is claimed for logistic inequalities, overlap bounds or sensitivity analysis.

**Contribution.** Once the alternative choice mechanism and its allowable changes are bounded, unchanged evaluation permits only a bounded change in offered target-directed responding. The sharp main bound uses the two marginal response levels, so it does not require observing each person's counterfactual response gate. It still requires a justified bound on changes in the choice score on a common paired population. Exceeding the bound rejects that restricted alternative; it does not uniquely identify newly acquired concern.

## 1. Population, response and score

Let a probability space describe a common target population of persons and offered contexts, including any latent histories required to define their two potential conditions. The two conditions are indexed by `j=0,1`. At each paired unit let

\[
0\le r_j\le1,\qquad p_j=\sigma(z_j),\qquad
\sigma(z)=\frac1{1+e^{-z}},\qquad \ell_j=r_jp_j.
\]

Here `r_j` is the probability of a valid response, and `p_j` is the conditional probability that a response selects the target-directed option. At `r_j=0`, that observed conditional probability is undefined; `p_j` is a declared extension of the latent choice model, with no effect on `ℓ_j`. Thus `ℓ_j` is the probability of a target-directed response per offered opportunity. A nonresponse is not a selection of the opposite option. No independence between the gate, score, person or context is assumed. All expectations below concern the same population measure:

\[
R_j=E[r_j],\quad L_j=E[\ell_j],\quad \Delta=L_1-L_0.
\]

The theorem is equally a weighted finite-population statement. It concerns population probabilities; an observed finite sample requires a separate uncertainty calculation. Random assignment can identify marginal potential means under its usual sampling and observation conditions. It does not identify the cross-condition pairing of latent scores or make post-assignment eligible samples the same population.

For interpretation, consider the explicitly restricted score law

\[
z_j=b_j+v_jq_j+\beta_je_j. \tag{1}
\]

`q_j` is a signed, factual expectation of the target consequence; `v_j` is its evaluative coefficient; `e_j` is the expected private-payoff contrast; `β_j` is its sensitivity; and `b_j` includes the remaining declared baseline influences. These are model variables, not transparent measurements or terms estimated by the preceding reanalysis. The unit and scale of each variable, including the logistic noise scale, must be fixed. Moving changes in demand, attention, habit or noise into an unrestricted `b_j` defeats a finite bound.

Under unchanged evaluation `v_1=v_0=v`, suppose on a covered set `G` that

\[
|v|\le V,\quad |\beta_0|\le B,\quad |e_1|\le E,\quad
|b_1-b_0|\le d_b,\quad |q_1-q_0|\le d_q,
\]
\[
|e_1-e_0|\le d_e,\qquad |\beta_1-\beta_0|\le d_\beta.
\]

Then the identity

\[
z_1-z_0=(b_1-b_0)+v(q_1-q_0)
 +\beta_0(e_1-e_0)+(\beta_1-\beta_0)e_1
\]

gives the sufficient score budget

\[
|z_1-z_0|\le D:=d_b+Vd_q+Bd_e+Ed_\beta. \tag{2}
\]

Stable private-payoff sensitivity sets `d_β=0`; a bound on its level alone does not remove the final term. Heterogeneous persons may have different stable values and sensitivities. The subsequent probability bound is sharp for the resulting score class. A particular decomposition or observed covariate support may make the triangle bound (2) conservative; sharpness for an unrestricted score class does not prove simultaneous attainability of every proposed measurement budget.

## 2. Logistic displacement lemma

For `D≥0`, define

\[
m(D)=\tanh(D/4)=\frac{e^{D/2}-1}{e^{D/2}+1}.
\]

If `|z_1−z_0|≤D`, then `|σ(z_1)−σ(z_0)|≤m(D)`. For `D>0` this bound is attained at `z_0=−D/2`, `z_1=D/2` and at the reversed pair. For `D=0` the difference is zero.

**Proof.** Monotonicity reduces the positive displacement to `σ(z+D)−σ(z)`. Put `A=e^D≥1` and `t=e^z>0`. The difference is

\[
\frac{(A-1)t}{(1+At)(1+t)}.
\]

For `A>1`, its derivative has the sign of `1−At²`, so its maximum occurs at `t=A^{-1/2}`. Substitution yields `(√A−1)/(√A+1)`. Exchanging the two scores bounds the negative displacement. This is an analytical real-variable argument, separate from the finite rational probability theorem.

## 3. Main theorem: marginal response levels suffice

Assume `Pr(G)≥1−ε`, where `0≤ε≤1`, and `|z_1−z_0|≤D` on `G`. Outside `G`, scores and gates may be arbitrary. Set

\[
m=m(D),\qquad H=\max\{0,R_0+R_1-1-\varepsilon\}.
\]

Then

\[
\boxed{-R_0+(1-m)H\ \le\ \Delta\ \le\ R_1-(1-m)H.} \tag{3}
\]

Both endpoints are sharp suprema over this population class at fixed `R_0,R_1,D,ε`. The same theorem holds directly for arbitrary probabilities `p_j∈[0,1]` satisfying `|p_1−p_0|≤m` on `G`; in that larger probability class its extrema are attained.

**Proof of the upper bound.** Define the fractional common response amount `h=min(r_0,r_1)`. On `G`, write

\[
r_1p_1-r_0p_0
=(r_1-h)p_1+h(p_1-p_0)-(r_0-h)p_0
\le r_1-(1-m)h.
\]

Outside `G`, the difference is at most `r_1`. Therefore

\[
\Delta\le R_1-(1-m)E[\mathbf1_Gh]. \tag{4}
\]

Pointwise `h≥r_0+r_1−1`, while `0≤h≤1`. Consequently

\[
E[\mathbf1_Gh]=E[h]-E[\mathbf1_{G^c}h]
\ge R_0+R_1-1-\varepsilon,
\]

and it is also nonnegative. Since `1−m≥0`, (4) proves the upper bound. Interchanging the condition labels gives the lower bound. The proof uses only bounded measurable variables; it requires no independence, common realized response coins, or identification of the latent joint distribution of gates.

**Sharpness construction.** Let `O=max(0,R_0+R_1−1)` and `a=min(O,ε)`. Use the following population strata; all displayed masses are nonnegative and sum to one:

| Stratum | Mass | `(r_0,r_1)` | Score/probability assignment for the upper endpoint |
| --- | ---: | --- | --- |
| Both respond, uncovered | `a` | `(1,1)` | `p_0→0`, `p_1→1` |
| Both respond, covered | `O−a` | `(1,1)` | `z_0=−D/2`, `z_1=D/2` |
| Only condition 1 responds | `R_1−O` | `(0,1)` | equal scores tending to `+∞` |
| Only condition 0 responds | `R_0−O` | `(1,0)` | equal scores tending to `−∞` |
| Neither responds | `1−R_0−R_1+O` | `(0,0)` | equal finite scores |

Only the first stratum is uncovered, so its mass is at most `ε`. The limiting contrast is

\[
(R_1-O)+a+m(O-a)
=R_1-(1-m)\max(0,R_0+R_1-1-\varepsilon).
\]

Every finite score choice respects the covered displacement bound. Taking its magnitude to infinity approaches the endpoint. If arbitrary `[0,1]` choice probabilities are allowed, replacing the limits by `0` or `1` attains it exactly. Reversing scores establishes the lower endpoint. Some boundary configurations need no infinite limits, but a general finite-logit maximum is not claimed.

The overlap term is essential. If `R_0+R_1≤1+ε`, the sharp interval reduces to the trivial `[-R_0,R_1]`: response selection and the uncovered portion can hide all informative common response. If both conditions always respond, (3) becomes

\[
|\Delta|\le\varepsilon+(1-\varepsilon)m(D). \tag{5}
\]

Equal response **levels** can still be low enough to give little information. Equal response **differences** alone give none: two equal-sized strata can have opposite exclusive gates, identical scores within each pair, and scores respectively tending to `+∞` and `−∞`. Then `R_0=R_1=1/2`, `D=ε=0`, yet `Δ→1/2`. Marginal response equality does not establish individual gate preservation.

## 4. Stronger gate knowledge gives different envelopes

These results concern additional information and should not be substituted for one another. They do not replace (3) when only marginal response levels are measured.

### Unitwise gate cap

Suppose throughout the covered set that `|r_1−r_0|≤ρ`, with `0≤ρ≤1`. Define `A=e^D` and `c=1−ρ`. Then the sharp covered-pair displacement bound is

\[
U(D,\rho)=
\begin{cases}
\rho,& Ac\le1,\\[2mm]
\displaystyle\frac{(\sqrt A-\sqrt c)^2}{A-1},& Ac>1.
\end{cases} \tag{6}
\]

Thus `|Δ|≤U(D,ρ)` under complete coverage. With arbitrary uncovered mass at most `ε`, a valid sharp bound without fixed marginal response constraints is

\[
|\Delta|\le\varepsilon+(1-\varepsilon)U(D,\rho). \tag{7}
\]

**Proof.** For fixed probabilities with `p_1≥p_0`, maximizing over admissible gates sets `r_1=1`, `r_0=1−ρ`. If `p_1<p_0`, every admissible positive displacement is at most `ρ`, already approached by equal scores tending to `+∞`. Monotonicity in `p_1` therefore reduces the global supremum to

\[
\sup_{t>0}\left\{\frac{At}{1+At}-\frac{ct}{1+t}\right\}. \tag{8}
\]

Its derivative is `A/(1+At)²−c/(1+t)²`. If `Ac≤1`, it is nonnegative and (8) tends to `1−c=ρ`. If `Ac>1`, it changes sign once at

\[
t_* = \frac{\sqrt A-\sqrt c}{A\sqrt c-\sqrt A}>0.
\]

Substitution gives the second branch of (6). `D=0` always falls in the first branch, avoiding division by zero. Exchanging conditions gives the absolute bound; mixing uncovered extreme pairs gives (7). For `ρ=0`, (6) reduces to `m(D)`; for `ρ=1`, it is one. These are suprema under finite logits.

### Mean absolute gate change

If instead complete score coverage holds and only `E|r_1−r_0|≤ρ` is justified, the sharp envelope without fixed marginal levels is

\[
|\Delta|\le\rho+(1-\rho)m(D). \tag{9}
\]

To prove the positive direction, let `d=(r_1−r_0)_+`. If `r_1≥r_0`, the preceding decomposition bounds displacement by `d+(1−d)m`; if `r_1<r_0`, it is at most `m`, the same expression with `d=0`. Average and use `E[d]≤ρ`. Reverse labels for the negative direction. Sharpness follows by mixing mass `ρ` of exclusive condition-1 responders with equal high scores and mass `1−ρ` of full responders at centered scores `±D/2`. This differs from a pointwise `ρ` cap. In particular, `|E[r_1]−E[r_0]|≤ρ` is insufficient for (9).

With both additional gate information and marginal levels, take the intersection of the valid inequalities. This note does not claim that this intersection is always the sharp region for every combined constraint set.

## 5. Which measurements could justify the premises?

The score bound is a substantive restriction, not a conclusion of the algebra. The accepted [identification note](IDENTIFICATION.md) permits exactly compensating changes in latent valuation and private expectancy. This result narrows that class only when the nuisance budgets and their coverage have independent support.

- **Factual competence and private expectancy:** equal objective contingencies do not imply equal `q` or `e`. Validated reports with `|q_j−q̂_j|≤c_j` can support `|q_1−q_0|≤|q̂_1−q̂_0|+c_0+c_1`, and similarly for private expectancy. But the paired report difference itself needs justification. Small differences of group means can conceal large opposite individual changes. A fallible reporting law must be included rather than treated as direct access to belief.
- **Fixed decision scale and bounded alternatives:** monetary sensitivity, response noise, baseline demand, attention and perseveration must be fixed or bounded in the proposed model class. An unrestricted baseline or arbitrarily large private-payoff sensitivity reproduces the prior ambiguity. A justified experimental clamp or independent calibration can supply a restriction; choosing convenient constants after inspecting the contrast cannot.
- **Common covered pairs:** the theorem uses one event `G` on which the pairwise score bound holds. If condition-specific measurement-validity events have uncovered fractions `ε_0` and `ε_1`, only their intersection is automatically covered with error at most `min(1,ε_0+ε_1)`. Equal per-arm coverage `1−ε` does not in general justify paired coverage `1−ε`; the union bound gives `1−2ε`. Additional evidence about dependence can improve it. Measurement validity in both arms also does not itself prove a bound on their cross-condition difference.
- **Response and eligibility:** count offered opportunities as well as valid responses. Post-assignment exclusions can change the population in each arm. Conditional means among separately eligible groups cannot be inserted into (3) as if they were common-population potential means. An identified target population, justified selection adjustment, or an explicit additional missingness/selection bound is necessary. The old all-saved sensitivity still does not recover unsaved participants.
- **Consequential interpretation:** `q` must concern a separately identified target consequence. Target-liked selections, believed gift probabilities and actual welfare are distinct. An effective coefficient does not separate learned valuation from transfer-route strength or decision noise without further measurements. Rejecting unchanged `v` within (1) does not establish ethical standing or exclude every affective or normative mechanism omitted from the restricted law.

There is no assertion that the existing reward-learning archive supplies these measurements. Its actual task histories and post-task awareness report do not establish the needed pairwise latent budgets. No constants are fitted to turn its accepted uncertain contrast into a new finding. The proposed new-recipient, contingent-versus-yoked training comparison remains unrun; its role is to supply a possible future setting in which these assumptions could be assessed.

## 6. Statistical use and decision rule

Coverage `1−ε` is a population exception fraction, not a confidence level. `D` is a mechanism/measurement sensitivity parameter, not a standard error. These quantities must not be exchanged with sampling uncertainty.

Write the upper envelope as `B(R_0,R_1,D,ε)`. It is nonincreasing in `R_0` and nondecreasing in `R_1,D,ε`: when the overlap is positive, its derivatives with respect to the two response levels are `−(1−m)` and `m`; when it is zero they are `0` and `1`. Monotonicity remains valid at the joining boundary.

A simultaneous confidence region for `(Δ,R_0,R_1)` can be compared with the null region `Δ≤B`. Reject the restricted positive-direction null only when the entire confidence region lies above that region. A simple conservative sufficient rule uses simultaneous bounds `Δ≥ℓ_Δ`, `R_0≥ℓ_0`, `R_1≤u_1` and justified upper budgets `D≤D_max`, `ε≤ε_max`:

\[
\ell_\Delta>B(\ell_0,u_1,D_{\max},\varepsilon_{\max}). \tag{10}
\]

Response endpoints are constrained to `[0,1]`. The bounds must be jointly valid, for example by an explicitly allocated error allowance; several separate nominal intervals do not automatically supply one joint guarantee. If the budget statements themselves have a separate error probability, their joint failure must also enter the stated error accounting. The negative-direction test interchanges conditions. This note supplies no new confidence calculation or test result for the old data.

**One conservative fixed-sample recipe.** Suppose the independent sampling units are participants, arm counts `n_0,n_1>0` are fixed, and both arms represent the declared common target population. Each participant supplies an offered target-directed response fraction and an offered valid-response fraction in `[0,1]`; repeated trials do not become independent participants. For `0<α<1`, put

\[
u_j=\sqrt{\frac{\log(8/\alpha)}{2n_j}}.
\]

Give each of the four means `L_0,R_0,L_1,R_1` its sample mean plus or minus its arm's `u_j`, clipped to `[0,1]`. Each interval fails with probability at most `α/4`, so all four cover jointly with probability at least `1−α`. The within-participant correlation of target-directed responding and valid responding is allowed; independence is required across the participant units used for each mean. Use

\[
\ell_\Delta=\ell_{L_1}-u_{L_0}
\]

in (10), together with `ℓ_{R_0}` and `u_{R_1}`. Here the subscripts distinguish the interval upper endpoints from the radii `u_j`. The same four-mean region permits the mirrored negative test, without another error allowance, because both conclusions are sound whenever that region covers. This deliberately conservative recipe uses fixed, justified `D,ε`; an independently fallible calibration statement needs its own joint error budget.

The concentration step is standard [Hoeffding bounded-sum machinery (1963)](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf). A self-contained argument makes its assumptions explicit. For `X∈[0,1]` with mean `μ`, convexity gives `E[e^{tX}]≤1−μ+μe^t`. The centered log of this Bernoulli bound has value and derivative zero at `t=0`; its second derivative is at most `1/4`. Hence `E[e^{t(X−μ)}]≤e^{t²/8}`. Independence multiplies the bounds for `n` participants. Markov's inequality with `t=4u` gives an upper-mean tail at most `e^{-2nu²}`; applying it to the negative tail gives `2e^{-2nu²}`. Substituting the displayed radius gives `α/4`, and the four-event union bound gives the stated joint coverage. Equal participant means within an arm identify the population mean; the concentration inequality itself also applies to independent bounded observations with different means around their average expectation.

This recipe does not cover data-dependent sample sizes, optional stopping, selected favorable subgroups, or repeated reuse of a nominal allowance. Randomization alone does not supply independent sampling from a common population after exclusions. Designs using finite-population dependence or more assignment strata need an appropriate concentration argument and a declared joint allowance, rather than silently reusing the four-mean formula.

For predeclared strata with fixed nonnegative weights summing to one, apply (3) within each stratum and average the resulting bounds. This can retain stronger information than collapsing response levels or using the worst stratum budget. It requires the claimed common-population and coverage conditions within each stratum. In particular, the old equal-weight current-contingency contrast would require its own two strata's valid budgets; its existence does not validate them.

Failure to reject the bounded class does not identify its mechanism or prove no acquired valuation. Rejection implies that at least one class premise fails. Calling that failure changed valuation additionally requires defending the nuisance, measurement, population and choice-law restrictions. The contribution is a falsifiable threshold for a named alternative, not a data-independent preference for the evaluative explanation.

## 7. Scope of verification and next connection

The mathematical proof above covers general probability spaces and the real logistic envelope. The [additive formal package](../../../../experiments/recipient-value-learning/formal/README.md) passes a fresh frozen-source Lean 4.29.1 build with **27 theorem audits**, recorded in its [verification receipt](../../../../experiments/recipient-value-learning/formal/verification.json): sixteen for the finite rational population account and eleven for rational odds.

`OfferedChoice.signed_population_bound`, `mirrored_population_bound` and `good_overlap_lower` cover arbitrary finite rational weighted populations under their declared premises. `sharp_population_valid`, `sharp_population_account` and `sharp_population_attains` establish the general five-stratum construction, not merely one numerical example. The rational-odds module separately proves a pointwise quadratic equivalence, a sufficient certificate using a discriminant or nonnegative coefficients, transport through paired gates, and exact fourfold-odds attainment examples. It does not prove that the sufficient certificate is universally necessary.

These Lean results do not formalize real exponentials, square roots, the calculus giving (6), the probability-space integral proof, or the statistical sampling and measurement assumptions. Those remain at their stated analytical scope. The separate [saved numerical checks](../../../../experiments/recipient-value-learning/bounded-identification/checks.json) concern constructed populations, boundary formulas and counterexamples, with no empirical data input. The [review](BOUNDED-IDENTIFICATION-REVIEW.md) distinguishes analytical acceptance, numerical checking and inspection of the frozen proof receipt. No new scientific outcome has been computed here.

This advances **learning history → formation of evaluative influence** by replacing an unrestricted latent-alternative warning with an explicit observable response envelope and a measurement contract. It leaves formation of the sensing and evaluation mechanism, calibrated transfer, enduring selection over such mechanisms, delivered benefit and justified concern to their existing research branches. A future informative contrast would either exclude the bounded unchanged-evaluation class or preserve it as a viable explanation; neither result completes the unified foundation.
