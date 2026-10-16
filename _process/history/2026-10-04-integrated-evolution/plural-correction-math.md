# Plural requirements on attainable correction

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. This memo applies established occupation-measure, linear-programming, and separation results to several requirements on a corrective institution. It does not introduce a new mathematical foundation for plural values. Altman's [*Constrained Markov Decision Processes*](https://www-sop.inria.fr/members/Eitan.Altman/PAPERS/h.pdf), especially its introduction and occupation-measure chapters, directly develops control with multiple constrained criteria. The proposed interpretation and finite experiment should be assessed on that basis.

## 1. Several requirements without a shared total ranking

Reuse the finite recoverable-inquiry model's physical dynamics, observation chronology, permitted actions, and initial distribution. A policy controls diagnostic readiness, observations, and repair using its actual information. Define three consequences, all oriented so smaller is preferred:

\[
F(\pi)=\Pr_\pi(\text{productive collapse within the horizon}),
\]

\[
H(\pi)=\mathbb E_\pi\sum_t
\left[\mathbf1\{\text{repair while its fault target is absent}\}
+.05\,\mathbf1\{\text{test}\}\right],
\]

\[
C(\pi)=\mathbb E_\pi\sum_t(\text{expenditure}_t-\text{output}_t).
\tag{1}
\]

The third consequence omits the earlier terminal-stock valuation and scalar collapse penalty. Collapse is now separately constrained. Cash-prefunding and reserve restrictions remain physical admissibility conditions on every branch, regardless of expected \(C\).

Given bounds \(u=(f,h,c)\), ask whether a **single policy** satisfies

\[
F(\pi)\le f,\qquad H(\pi)\le h,\qquad C(\pi)\le c.
\tag{2}
\]

This supplies thresholds without supplying a complete ranking of every pair of outcomes. The implemented occupancy formulation uses a common known probabilistic model. It also requires declared consequences, acceptable bounds, information, and a common set of executable policies. These are not automatically neutral or legitimate choices. The three coordinates can represent distinct constituencies' requirements, but they are not actual per-person exposures, consent, bargaining power, strategic behavior, or an equilibrium. Section 8 explains a broader finite-policy formulation that does not require a common world model or prior.

Because healthy repair can also restore stock in the inherited dynamics, target-absent repair remains a specified burden measure rather than a synonym for harmful error. No mathematical argument turns the chosen bounds into the correct social requirements.

## 2. The attainable set has a finite, checkable representation

Index living, time-indexed belief states by \(v\) and admissible actions by \(a\). Let \(y(v,a)\) be the probability that the controller visits \(v\) and uses \(a\). The occupancy equations are

\[
\sum_a y(v,a)-\sum_{w,a}P(v\mid w,a)y(w,a)=\rho(v),
\qquad y(v,a)\ge0,
\tag{3}
\]

where \(\rho\) places mass one at the initial state. Write these as \(Ay=\rho\). Transitions to terminal nodes exit the living flow. Fold terminal failure into each predecessor action's expected failure indicator; terminal salvage and scalar failure penalties are excluded. Let \(G\) contain the three corresponding expected consequence coefficients, so \(Gy=(F,H,C)\).

Every admissible policy, including one depending on its whole observed history, induces such an occupancy vector. Conversely, a feasible occupancy vector can be implemented by the randomized Markov rule

\[
\pi(a\mid v)=\frac{y(v,a)}{\sum_{a'}y(v,a')}
\tag{4}
\]

at reached states. At zero-occupancy states any admissible action can be specified. The full belief state must actually be sufficient for future transitions and these additive expected consequences; it is not permissible to discard relevant public information when constructing it.

Since the horizon and graph are finite, occupancies have bounded total mass and the nonempty set

\[
\mathcal Y=\{y\ge0:Ay=\rho\}
\]

is a compact polytope. Hence

\[
\mathcal Z=G\mathcal Y
\tag{5}
\]

is a compact convex polytope of attainable expected consequences. Ex ante lotteries over deterministic policies give the same expected attainable set. For three coordinates, any point of \(\mathcal Z\) can be represented by a mixture of at most four deterministic-policy consequence vectors, by the finite-dimensional convex-hull bound. Recovering that small mixture is different from extracting the direct occupancy policy (4).

Convexity here relies on allowing randomization and evaluating expectations. If only deterministic policies are permitted, the convexified calculation can declare feasible a requirement that no allowed policy meets. Whether constituencies accept the lottery is additional to whether its expectation satisfies (2).

## 3. Phase I gives either a common witness or a common obstruction

Choose declared positive coordinate scales \(s=(s_F,s_H,s_C)\). They make the diagnostic margin interpretable across unlike units; changing them can change its value and the selected certificate, but not the sign of exact feasibility. Solve

\[
\begin{aligned}
t_*={}&\min_{y,t} t,\\
\text{subject to }&Ay=\rho,\quad y\ge0,\\
&Gy-st\le u,\qquad t\in\mathbb R.
\end{aligned}
\tag{6}
\]

Equivalently, \(t_* = \min_{z\in\mathcal Z}\max_i(z_i-u_i)/s_i\). Because \(\mathcal Z\) is compact, the optimum is attained. Thus \(t_*\le0\) exactly when a jointly feasible policy exists. A negative value supplies common normalized slack; zero is a boundary witness. Positive values require an obstruction, not a policy described as satisfying the original bounds.

The dual is

\[
\begin{aligned}
t_*={}&\max_{w,v}\ \rho^\top v-u^\top w,\\
&w\ge0,\quad w^\top s=1,\quad A^\top v\le G^\top w.
\end{aligned}
\tag{7}
\]

To derive it, use multipliers \(w\ge0\) on \(Gy-st-u\le0\) and \(v\) on \(\rho-Ay=0\). Minimization over free \(t\) requires \(w^\top s=1\), while minimization over nonnegative \(y\) requires \(G^\top w-A^\top v\ge0\). Finite LP strong duality applies because (6) is feasible and bounded. These are established separation/duality methods; see Boyd and Vandenberghe's [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), chapters 2 and 5.

Every dual-feasible pair proves the inequality

\[
w^\top z\ge \rho^\top v\quad\text{for every attainable }z.
\tag{8}
\]

If the margin \(m=\rho^\top v-w^\top u\) is positive, any vector satisfying all requirements would contradict (8). Normalized nonnegative weights \(\lambda_i=w_is_i\) sum to one; an equivalent dual form is

\[
t_*=\max_{\lambda\ge0,\,\sum_i\lambda_i=1}
\min_{z\in\mathcal Z}\sum_i\lambda_i\frac{z_i-u_i}{s_i}.
\tag{9}
\]

The weights certify incompatibility. They are neither consent to trade away a constituency's requirement nor a discovered common welfare function. Likewise, the phase-I minimizer is a computational witness of the smallest maximum normalized violation, not an ethically privileged compromise when the requirements are infeasible.

The certificate has a quantitative implication. Any relaxation \(\Delta\ge0\) that could make \(u+\Delta\) attainable must satisfy

\[
w^\top\Delta\ge m.
\tag{10}
\]

If only coordinate \(i\) can be relaxed and \(w_i>0\), at least \(m/w_i\) is necessary. If \(w_i=0\), relaxing only that coordinate cannot defeat this certificate. These conditions are generally necessary rather than sufficient: other separating inequalities may still prevent feasibility. Changes to the action set or productive technology change \(\mathcal Z\) itself and require a new calculation.

## 4. Separate attainability and pairwise compatibility are insufficient

Consider a one-step system with three deterministic consequence vectors

\[
z^1=(1,0,0),\quad z^2=(0,1,0),\quad z^3=(0,0,1).
\tag{11}
\]

Its randomized attainable set is their convex hull. Require \(u=(.3,.3,.3)\). Each coordinate separately can be zero, with positive slack. Every pair of requirements can also be met: choose the action placing its unit consequence in the remaining coordinate. Yet every policy satisfies

\[
z_1+z_2+z_3=1>.9=u_1+u_2+u_3.
\tag{12}
\]

Joint feasibility is impossible. With unit scales, the uniform mixture produces \((1/3,1/3,1/3)\), giving phase-I value \(1/30\), and the certificate uses \(w=(1/3,1/3,1/3)\). This is a finite theorem about coupled attainable consequences, not about an assumed refusal to cooperate.

The phrase “componentwise slack” needs precision. Slack in coordinate minima attained by different policies is insufficient. Positive slack in **all coordinates of one common policy** is sufficient by definition and provides a robustness margin. Confusing these is a substantive mathematical error.

Improvements in all separately optimized indicators need not even improve joint feasibility across different technologies. For example, replace the attainable segment joining \((0,2)\) and \((2,0)\) by the segment joining \((-1,4)\) and \((4,-1)\). Each separate minimum improves from zero to minus one, but the minimum possible maximum coordinate worsens from one to 1.5. Requirements \((1.1,1.1)\) are feasible before the change and infeasible afterward. Such comparisons do not contradict action-set monotonicity: the new attainable set did not contain the old one.

## 5. Restriction, resources, and information comparisons

**Action restriction.** If \(\Pi_R\subseteq\Pi\) under the same model, initial condition, and consequence definitions, then

\[
\mathcal Z_R\subseteq\mathcal Z,
\qquad t_*^R(u)\ge t_*(u).
\tag{13}
\]

Thus a no-test or forced-continuous policy class cannot create an expected-consequence vector unavailable to an otherwise identical adaptive class. A feasible restricted policy is also a feasible unrestricted witness; an unrestricted infeasibility certificate also rules out the restricted class. The reverse implications do not hold. This statement does not imply that an arbitrary heuristic using more actions performs better.

**More accessible cash.** Greater initial cash or a larger reserve cap gives a comparable expansion when the richer controller can reproduce the old actions using an internal shadow account, and all other dynamics and consequence definitions are unchanged. Under the same production and action realization, monotonicity of the cash recursion preserves affordability. In the present \(C=\mathbb E[\text{expense}-\text{output}]\) accounting, additional initial capital is not charged. Its acquisition cost must be added if the comparison is meant to include that cost. A larger productive stock, changed technology, or new mandatory expenditure is not automatically the same emulation argument.

**Lower fees.** If every old action sequence remains available, its physical outcomes and burden are unchanged, and its monetary expense decreases, then the old \((F,H,C)\) can be matched or improved coordinatewise. Literal inclusion of \(\mathcal Z\) need not follow because the \(C\) coordinate has changed. The clean object is the set of satisfiable upper bounds,

\[
\mathcal U=\mathcal Z+\mathbb R_+^3.
\tag{14}
\]

The old \(\mathcal U\) is contained in the improved one. A feasibility margin comparison is valid with the same threshold and scales.

**More informative observations.** If a richer observation can be transformed into the old one by a known randomized garbling, with the same timing, physical consequences, available actions, and cost, the controller can reproduce every old policy. Hence the old attainable set is included in the richer one. The sufficiency argument is direct emulation and is part of the established comparison-of-experiments framework; see Blackwell's primary [*Comparison of Experiments*](https://digicoll.lib.berkeley.edu/record/112749/files/math_s2_article-08.pdf). A more accurate signal that is slower, costly, compulsory, or changes who may act need not satisfy this ordering. All visible ordinary production and inherited information must be included when defining the channels.

These are single-controller comparisons of feasible policies under plural requirements. They do not prove that giving information to one strategic participant improves a decentralized game's outcome, nor that an institution will choose the feasible policy or respect the stated constraints.

## 6. Expectation, probability, and realized protection

The failure coordinate already is a probability: \(F\le f\) means \(\Pr(\text{collapse})\le f\). In contrast, bounds on \(H\) and \(C\) are expectations and need not hold on each trajectory. A policy lottery can satisfy them even when every component violates some requirement on its realized branches.

For the triangle example, use thresholds \((1/3,1/3,1/3)\). The uniform lottery meets all expected bounds exactly, yet every realized action produces a one in one coordinate. The probability of satisfying all three corresponding trajectory-wise bounds is zero. Ex ante feasibility and ex post protection are different properties.

An expected nonnegative burden gives only bounds such as \(\Pr(H_{\mathrm{real}}>a)\le\mathbb E[H_{\mathrm{real}}]/a\), which can be weak. Net expenditure can be negative, so this nonnegative-variable inequality cannot be applied to \(C\) without an appropriate transformation. Hard cash affordability remains separately enforced by the action graph.

A requirement such as \(\Pr(H_{\mathrm{real}}>h_0)\le\delta\), or a joint chance constraint on collapse and cumulative burden, changes the model. It generally requires tracking the relevant cumulative quantity or its posterior distribution. The current belief state is sufficient for additive expectations; it is not automatically sufficient for the distribution of cumulative hidden target-absence events. Simply reinterpreting the existing expectation constraint as a chance constraint is invalid.

## 7. Numerical witnesses, robust margins, and model limits

For a feasible occupancy, extract (4), propagate it forward on the original graph, and recompute all three consequences and branchwise cash constraints. This is a concrete policy witness. Report a threshold-boundary case as such; near-zero LP status alone is not a robust certificate.

For an infeasible case, report the nonnegative weights, their declared normalization/scales, and a positive separating margin. Independently recomputing \(\min_\pi w^\top(F,H,C)\) by backward dynamic programming checks the certificate without relying on the LP solver's multiplier sign convention. The scalar appears here as a proof of a violated necessary condition, not as the decision maker's objective.

If a numerical dual satisfies \(A^\top v\le G^\top w+\varepsilon\mathbf1\), and total occupancy is at most the horizon \(T\), it still supplies the weakened lower bound \(w^\top z\ge\rho^\top v-\varepsilon T\). Normalization, nonnegativity, primal flow, and consequence residuals should also be checked. These are numerical error bounds; a formal exact arithmetic or interval certificate would require controlling roundoff as well.

Model uncertainty is a different issue. Suppose each policy's true consequence vector differs from the modeled one by at most \(e_i\) in coordinate \(i\), uniformly over the relevant policies. A modeled common witness with \(z_i\le u_i-e_i\) remains feasible under that bound. A modeled separating gap \(m>w^\top e\) remains an obstruction. Without such a justified uniform error bound, solver precision says nothing about empirical model accuracy.

Separate feasibility in each possible environment can also be misleading if it uses different policies chosen with the hidden environment label. Robust plural feasibility requires one permitted observation-based policy that meets the bounds across the declared environments. Extending the consequence vector to environment-specific coordinates can express this, but the policy must remain common; allowing an oracle policy per environment changes the question.

The nontrivial output of this exercise is a common attainable policy or a checkable inequality excluding every policy in the declared class, with explicit margins and interventions that can change the obstruction. It does not settle who may set requirements, how disagreements should be resolved, whether randomization is acceptable, or what omitted constituencies would demand. Those are further coordination problems, not consequences of LP duality.

## 8. The convex argument can also accommodate different declared beliefs

The common-model occupancy LP is not the widest scope of the separation result. Let \(\Pi_D\) be a finite common set of executable deterministic observation-history policies. Let constituency \(i\) evaluate a policy using its own declared world model or prior \(P_i\) and its own measurable trajectory consequence \(g_i\):

\[
z_i(\pi)=\mathbb E_{P_i^\pi}[g_i],\qquad \pi\in\Pi_D.
\tag{15}
\]

The models can disagree about latent regimes or transition probabilities. The policy is nevertheless one actual mapping from observation histories to actions, not one separately optimized posterior policy for each evaluator.

Suppose a controller selects \(\pi\) through a publicly specified ex ante lottery with probabilities \(q_\pi\). The randomizer is independent of exogenous initial state and disturbances under each declared model; its specified probability law is the same across evaluations. Conditional trajectory laws given the selected policy do not depend further on the lottery weights. Then ordinary conditioning gives

\[
z_i(q)=\sum_{\pi\in\Pi_D}q_\pi\mathbb E_{P_i^\pi}[g_i],
\qquad
\mathcal Z_{\mathrm{plural\ beliefs}}
=\operatorname{conv}\{z(\pi):\pi\in\Pi_D\}.
\tag{16}
\]

The same phase-I and separation theorems apply to this finite convex hull. They therefore do not inherently require either a common scalar objective or a common probabilistic belief about the world. This is a stronger conditional statement than merely replacing one common utility with three common-model metrics.

Several assumptions carry the result. Policies must be defined on the union of all relevant finite observation histories, with the same executable action meanings. The admissible policy set must meet whatever physical or legal constraints are required across the stipulated models; it cannot change secretly with the evaluating constituency. Expectations must be finite. The common randomizer law and independence are implementation assumptions even when world beliefs differ. If different parties distrust that law, if the controller may condition its initial lottery on unavailable hidden state, or if strategic reactions depend on the whole announced lottery rather than the selected policy, the stated affinity needs a new argument.

Separate feasible policies \(\pi_i\), one for each constituency's model, remain insufficient. The vector \((z_1(\pi_1),z_2(\pi_2),z_3(\pi_3))\) is generally not the consequence vector of any common executable policy. A separating weighted sum across subjective evaluations is a mathematical obstruction to their simultaneous declared requirements; it need not equal one observer's expectation of an actual aggregate social loss.

This generalization is not implemented in the current experiment. A finite policy-table LP with columns \(z(\pi)\) is valid, but may be exponentially large. Independently constructing one occupancy policy for each model would not enforce a common controller. A more efficient joint formulation would have to preserve that shared-policy or nonanticipativity condition, potentially through an enriched common information state. No claim is made that the existing single-model occupancy matrix already solves it.
