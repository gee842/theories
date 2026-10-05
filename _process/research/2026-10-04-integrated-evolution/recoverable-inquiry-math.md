# Recoverable inquiry: observation, productive stock, and cumulative harm

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. These are conditional modeling results using established information inequalities, filtering, dynamic programming, and resource accounting. They do not constitute a new universal law. This memo proposes mathematics and audit criteria; it does not implement the experiment.

## 1. Recovery is a joint information-and-resource property

Suspending inquiry can be reasonable after negative evidence. Recoverability requires more than retaining the formal permission to ask again: the institution must receive information or follow a suitable reopening schedule, preserve enough productive stock through the delay, and finance every step before its benefit arrives. Continuous activity, one provider's permanent existence, and preservation of the ability to investigate when needed are different outcomes.

A smallest useful finite model has productive stock \(x_t\), liquid funds \(b_t\), readiness \(r_t\), and an unobserved binary hazard \(h_t\). Readiness includes a rebuild countdown if rebuilding takes time. A paid diagnostic observes a noisy signal of the current hazard. An intervention \(a_t\in\{0,1\}\) can prevent its damage; production then supplies funds for future inquiry. For example,

\[
x_{t+1}=\min\{X,\max\{0,x_t+g-dh_t(1-a_t)\}\},
\qquad d>g\ge0,
\tag{1}
\]

\[
b_{t+1}=\min\{B,b_t-C_t+Y_t\},
\qquad Y_t=\kappa x_t,
\qquad b_t\ge C_t.
\tag{2}
\]

Here \(C_t\) charges any rebuilding, sensing, intervention, and readiness upkeep chosen that period before income arrives. Monetary output, operating loss, and physical stock are distinct quantities. Production above the reserve cap must go somewhere explicit; transfers should not be counted as additional consumption. Inputs supporting productive renewal \(g\) are part of the supplied production technology or environmental boundary. Endogenous income does not make the modeled institution a physically closed system.

The hidden hazard may follow a declared Markov kernel. Its rate is supplied, not rediscovered by the controller. With finite stock, integer cash flows, bounded readiness counters, finite observations, and a finite horizon, this model permits exact enumeration or dynamic programming over reachable beliefs. Rebuilding, tests, and intervention need not all fit into one period: their chronological substeps can be separate states. If sensing precedes intervention, the intervention must be allowed to depend on that newly observed result.

## 2. Ordinary production is already an observation channel

All visible information belongs in the filtering problem: income, stock changes, cash changes, public interventions, failures, and elapsed time. In (1)–(2), an exact income observation reveals the corresponding stock. When no intervention masks damage, the stock transition can reveal the preceding hazard. A paid diagnostic can then buy earlier information, or help decide when to stop a protective intervention that makes healthy and hazardous production look alike. It cannot be credited with information already available for free in the specified ordinary operation.

For a posterior \(p_t=\Pr(h_t=1\mid\mathcal H_t)\) and a paid signal \(w\) with likelihood \(\ell_h(w)\), the diagnostic update is

\[
p_t^w=\frac{p_t\ell_1(w)}{p_t\ell_1(w)+(1-p_t)\ell_0(w)}.
\tag{3}
\]

Subsequent visible production updates this posterior again using its **joint** likelihood with already observed data. Deterministically linked stock and income are not independent pieces of evidence. If \(\bar p_t\) is the posterior after the full period and the hazard kernel has transition probabilities \(q_{01},q_{10}\), then

\[
p_{t+1}=q_{01}(1-\bar p_t)+(1-q_{10})\bar p_t.
\tag{4}
\]

Thus even uninformative silence does not freeze belief: elapsed time under a known transition law can justify scheduled reopening. The correct impossibility concerns discrimination between worlds, not an inability to change behavior without a new signal.

Let \(P_0^O,P_1^O\) be the laws of the entire observable dormant history through a deadline in healthy and hazardous worlds, under the same controller and information interface. Include internal randomization and every public trace. For any event \(G\) that the controller reopens by the deadline,

\[
\Pr_1(G)\le\Pr_0(G)+\operatorname{TV}(P_1^O,P_0^O).
\tag{5}
\]

Identical laws give identical reopening probabilities. No rule using only that channel can simultaneously reopen rarely when healthy and reliably by the deadline when hazardous. Periodic reopening remains possible and may be valuable; it pays for the resulting lack of discrimination. The claim fails if the supposedly identical channel omits informative income or stock changes. It also concerns the full history law, not just equal one-period marginal means.

## 3. Information needed before the recovery deadline

Suppose the chosen controller must satisfy \(\Pr_0(G)\le\alpha\) and \(\Pr_1(G)\ge1-\beta\), with \(\alpha+\beta<1\). Data processing through the binary decision gives

\[
\operatorname{KL}(P_1^O\Vert P_0^O)
\ge \operatorname{kl}(1-\beta,\alpha),
\tag{6}
\]

where \(\operatorname{kl}(u,v)=u\log(u/v)+(1-u)\log((1-u)/(1-v))\). To verify the inequality, first map the history to \(\mathbf1_G\); binary KL is minimized over the stated error constraints at \((1-\beta,\alpha)\). This is a standard change-of-measure argument. A primary treatment accommodating adaptive observations and stopping is Kaufmann, Cappé, and Garivier's [*On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models*, Lemma 1](https://jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf).

For an explicitly scoped experiment in which ordinary observations contribute at most \(I_o\) divergence and every paid sample contributes at most \(D\) conditional divergence, a hard maximum \(n\) paid samples implies

\[
nD+I_o\ge\operatorname{kl}(1-\beta,\alpha).
\tag{7}
\]

The bound follows from the chain rule for KL. For independent fixed-law paid samples the contribution is exactly \(nD\); for adaptive samples an expectation of their conditional divergences replaces it. The inherited history and action-dependent ordinary observations must be included. Perfectly identifying ordinary evidence has infinite KL against an incompatible deterministic alternative and makes this finite-information lower bound uninformative, as it should.

Equation (7) is necessary, not sufficient. A particular test can need more samples, additional delay, or more cash. If each sample costs \(k\), arrives at rate at most \(v\), and only \(D_{\mathrm{time}}\) time remains after rebuild and deployment, then \(n\le vD_{\mathrm{time}}\) and its cost must fit the intervening cash path. More statistical stringency can therefore make a correction physically or financially unreachable even when sufficient evidence would eventually exist.

## 4. A closed-form stock and cash deadline

A continuous certificate makes the timing constraint explicit. Suppose an uncorrected hazard drains stock at rate \(d>0\), so before effective correction

\[
x(t)=x_0-dt,
\qquad x(t)\ge x_{\min}.
\tag{8}
\]

Let the earliest feasible effective correction take detection delay, rebuilding, testing, and deployment times \(\tau_o,\tau_r,\tau_t,\tau_a\). If those stages are serial, a necessary condition is

\[
\tau_o+\tau_r+\tau_t+\tau_a
\le\frac{x_0-x_{\min}}d.
\tag{9}
\]

Parallel stages require the length of their actual critical path instead of this sum. A strict margin is appropriate if touching the boundary is failure or if delays are uncertain. No financing or information improvement after this physical deadline can reverse the stipulated irreversible stock loss.

Suppose pre-correction output is \(\kappa x(t)\), ordinary expense plus sentinel upkeep is \(o+s\), and inquiry/rebuild payments \(K_j\) occur at times \(t_j\). With no reserve ceiling reached along this prefix,

\[
b(t)=b_0+(\kappa x_0-o-s)t-\frac{\kappa d}{2}t^2
-\sum_{j:t_j\le t}K_j.
\tag{10}
\]

Every payment must be affordable when due, and \(b(t)\ge0\) must hold throughout. On intervals between payments this function is concave, so checking their endpoints, including immediately after each deduction, suffices. A positive final balance alone does not certify prefunding of earlier payments. If a cap binds and overflow becomes inaccessible, (10) overestimates later usable cash; the clipped path must be tracked instead. Borrowing requires an explicit credit and repayment rule.

Even reaching a sustainable productive state can require bridge liquidity. After effective correction, suppose

\[
\dot x=g-\delta x,\quad x_*=g/\delta,\quad
\dot b=\kappa x-o-m,
\qquad \delta>0,
\tag{11}
\]

where \(m\) is recurring protection/inquiry expense. Let \(x_c,b_c\) be stock and cash at correction, define \(A=\kappa x_*-o-m\), and define \(D=\kappa(x_*-x_c)\). When \(A>0\), \(D>A\), and the reserve ceiling does not bind during the cash dip, the exact minimum occurs at \(s_*=\delta^{-1}\log(D/A)\). Integration yields the necessary and sufficient cash condition for this recovery trajectory:

\[
\boxed{b_c\ge\frac{D-A-A\log(D/A)}{\delta}.}
\tag{12}
\]

For \(D\le A\), cash never initially decreases and no additional bridge is needed. For \(A=0,D>0\), the total asymptotic dip is \(D/\delta\); for \(A<0\), this maintained regime eventually consumes any finite cash reserve. The productive trajectory must separately remain above its physical floor. Equation (12) distinguishes a positive long-run output margin from the ability to finance recovery to it. It is a trajectory certificate, not a complete model of resource regeneration.

## 5. Viability with uncertainty and evidence-guided suspension

Let \(z=(x,b,r,\pi)\) contain the visible physical/financial state, readiness, and posterior distribution over hidden regimes. Let \(\mathcal K\) be the declared safe region. Test affordability and rebuilding constraints determine the available actions \(\mathcal A(z)\). A sensing action followed by an intervention conditional on its result should be represented as such a contingent action or as two decision stages.

For robust finite-horizon viability, begin with \(\mathcal V_0=\mathcal K\) and recurse

\[
\mathcal V_{n+1}=\left\{z\in\mathcal K:
\exists a\in\mathcal A(z)\text{ such that every possible successor }z'
\text{ lies in }\mathcal V_n\right\}.
\tag{13}
\]

“Possible” ranges over the hidden states in the belief support and every stipulated disturbance or observation with positive conditional probability. A finite sequence of false-negative tests with positive probability can make this set much smaller than an expected-loss calculation suggests. The robust set can be empty; the model should not claim a guarantee merely because simulated average behavior looks safe.

For probabilistic safety, let \(V_0(z)=\mathbf1_{\mathcal K}(z)\) and use the Bayesian successor kernel:

\[
V_{n+1}(z)=\mathbf1_{\mathcal K}(z)
\max_{a\in\mathcal A(z)}\mathbb E[V_n(z')\mid z,a].
\tag{14}
\]

Then \(\{z:V_H(z)\ge1-\eta\}\) is the supplied model's horizon-\(H\) chance-safe set. Stochastic safety/reachability through dynamic programming is established methodology; see Abate, Prandini, Lygeros, and Sastry, [*Probabilistic Reachability and Safety for Controlled Discrete Time Stochastic Hybrid Systems*](https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202008/AbateProbabilistic2008.pdf). Here the belief state accounts for the observation restriction.

Expected loss, chance of productive collapse, unnecessary reopening, and cash exhaustion can be distinct criteria. A claimed optimal policy must state which are objectives and which are constraints. A fixed threshold policy can be a useful comparator without being called optimal. Always-on inquiry and no-inquiry should retain identical ordinary observation interfaces and production technologies.

If \(x\) itself is hidden, a posterior over \(x\) must replace the visible-stock state. A one-step indicator of a safe belief support gives a robust guarantee, while probabilistic safety generally needs a posterior that also tracks whether past failure has occurred. The simplest exact implementation avoids this complication by making physical collapse and current stock visible. Freely retained beliefs are an explicit memory assumption; this cycle does not thereby solve paid archival succession.

## 6. Lifetime error and finite evidence are not interchangeable

For candidate tests indexed by \(j\), conditional validity at predictable levels \(\alpha_j\) and a pathwise budget \(\sum_j\alpha_j\le\bar\alpha\) give

\[
\Pr(\text{any false acceptance})\le\bar\alpha.
\tag{15}
\]

The remaining error budget can be part of the controlled state. A fresh test is not licensed to reuse the full \(\bar\alpha\) at every restart. Conversely, failure to reject the current null is not proof that no hazard exists; use a posterior, a confidence bound with a specified decision threshold, or a test that explicitly addresses the negative conclusion.

Summable per-episode levels tend to zero. If every genuinely new episode permits at most a fixed total observation divergence \(I_{\max}<\infty\) before its recovery deadline, (6) prevents a fixed detection probability \(1-\beta>0\) at arbitrarily small \(\alpha_j\): \(\operatorname{kl}(1-\beta,\alpha_j)\) diverges. Thus this form of lifetime no-false-acceptance control, uniformly high power, and a uniformly bounded per-episode information/deadline budget cannot all be maintained indefinitely.

The scope is essential. This is not an impossibility of learning one stationary fact from accumulating observations, nor a theorem that every time-uniform method must use Bonferroni spending. [Howard, Ramdas, McAuliffe, and Sekhon's confidence sequences](https://arxiv.org/abs/1810.08240) provide established time-uniform inference under their stated processes. Repeatedly changing targets, recurrent independent candidate problems, and a single persistent hypothesis are different statistical objects. Reusing a confidence sequence after a regime change without a valid model for that change can invalidate its interpretation.

## 8. Cumulative harm must match the time horizon

A finite-horizon harm criterion can count injury from untreated hazards, investigation burden, and unnecessary intervention:

\[
\mathcal H_H(\pi)=\mathbb E_\pi\sum_{t=0}^{H-1}
\left[h_{\mathrm{hazard}}(x_t,h_t,a_t)
+h_{\mathrm{inquiry}}(u_t)+h_{\mathrm{intervention}}(h_t,a_t)\right].
\tag{16}
\]

Cash expenditures can appear separately if their social opportunity cost is already represented elsewhere. A budget on (16) is not the same as a familywise statistical error guarantee: a false alarm can be harmless or expensive, and a missed hazard can dominate both.

Finite **undiscounted lifetime** expected harm is much stronger. If every test incurs harm at least \(h_0>0\), then

\[
\mathbb E[\text{lifetime inquiry harm}]\ge h_0\mathbb E[N],
\tag{17}
\]

where \(N\) is the lifetime number of tests. A process requiring infinitely many tests in expectation cannot have finite lifetime inquiry harm under that premise. Recurrent unavoidable hazards can similarly make total physical harm diverge. A finite-horizon budget, discounted sum, long-run average rate, or excess loss relative to a declared baseline can be meaningful instead, but each changes the criterion and must be named accurately. Finite lifetime harm remains possible under finitely many relevant hazards, vanishing per-test harm, sufficient ordinary observations, or a durable response that eventually removes the need to test.

## 9. Discriminating controls and interpretation

The proposed model should preserve controls in which ordinary income reveals the hazard soon enough; detection is possible but rebuild arrives too late; long-run production is sufficient but bridge cash is not; negatives correctly support suspension; and a null environment makes continuous inquiry wasteful. If a sentinel's advantage disappears once visible production is included in filtering, that is an informative failed prediction rather than a reason to hide production from the controller.

Likewise, a deadline or cash threshold prescribed by the model is a feasibility boundary, not an emergent attractor. Endogenous recovery means that productive state, spending, evidence, and the choice to suspend or reopen interact along the path. It does not mean that the hazard family, legitimate purposes, standing to intervene, or renewable physical inputs have been endogenously explained. The strongest useful result would identify when an institution can suspend a function without losing the jointly observable, timely, and financeable route to restoring it.

## 10. Compatibility with the implemented finite experiment

The implementation specializes the architecture differently from the continuous certificates. Its state uses stock \(x\in\{0,1,2,3\}\), cash \(b\in\{0,\ldots,8\}\), readiness, and an exact rational fault belief. The selected chronology is: pay to retain or rebuild diagnostic readiness; optionally pay for a current diagnostic; choose a repair using that evidence; realize stochastic stock damage and resulting output; update from visible stock/output; then advance the hidden fault by its Markov transition. Readiness upkeep costs one, rebuilding costs three and takes until the next period, a test costs two, and a direct repair costs three. Direct repair remains available without buying a diagnostic.

The productive transition is \(x'=\operatorname{clip}(x+1+u-2D,0,3)\), except that zero stock is absorbing. The damage probability is .1 when healthy and .8 when faulty; repair \(u=1\) resets the current fault before damage. Output \(2x'\) arrives only afterward. Prefunding must therefore use current cash, not this later output. Physical renewal and income are state dependent; their probabilities and technological law remain supplied. Exact stock and income encode the same observation and enter filtering once through their joint likelihood.

The implemented diagnostic is binary and noisy, with sensitivity and specificity both .9. Its positive and negative likelihood ratios are respectively 9 and 1/9; neither result exposes the true hidden fault. Between the two fixed fault states its one-sample KL divergence is \(.8\log9\), which is finite. This revision removes the state-exclusive truthful outcomes of the earlier proposed erasure diagnostic. Nevertheless, the finite-information result (7) and alpha-spending obstruction remain separate lemmas: the finite controller updates beliefs and optimizes actions, and does not implement repeated hypothesis tests at a lifetime alpha budget. The stock/cash certificates in section 4 are analytic comparison cases, not equations claimed to govern this finite transition model.

The constraint is an ex ante expected sum of target-absent repairs plus .05 per test; .6 is the initial comparison budget and smaller budgets are also examined. The probability that a repair lacks its fault target uses the posterior **before** repair resets that target. Because the extra \(+u\) can improve stock even when the fault is absent, target-absent repair is not synonymous with a mistaken, harmful, or irrational action. The burden criterion is a supplied evaluative choice, not a statistical error probability. The objective is expected expenditure minus output, minus terminal stock value \(2x_H\), plus a twelve-unit penalty for productive collapse. Finite-horizon burden and expected cost are optimized; robust viability and a bound on collapse probability are not imposed.

A Lagrangian Bellman calculation generates policy candidates for this expectation constraint. Write \(C(\pi)\) for expected cost and \(R(\pi)\) for expected burden. For every multiplier \(\lambda\ge0\),

\[
\min_\pi\{C(\pi)+\lambda R(\pi)\}-\lambda\beta
\le \min_{\pi:R(\pi)\le\beta}C(\pi).
\tag{18}
\]

The code retains this dual lower bound and an upper bound from an ex ante mixture of two policies whose burdens bracket \(\beta\). Agreement certifies the finite problem to the reported numerical gap. The mixture does not give the controller knowledge of the hidden fault or permission to redraw a policy after seeing favorable outcomes. Its expected burden guarantee does not imply a pathwise harm ceiling or a guarantee for each component policy. A separate minimum-burden Bellman calculation certifies infeasibility instead of treating a forced continuous-testing policy as admissible at every budget.

## 11. Independent implementation audit

The inspected `experiments/recoverable-inquiry/model.py` uses exact `Fraction` beliefs and signal masses, then floating-point expectations in its finite dynamic program. The Bayes chronology is correct: noisy diagnostic conditioning precedes repair; target-absence burden refers to the pre-repair fault; repair resets the current fault; the public stock transition supplies passive evidence; and the onset/clearance kernel ages the posterior for the next period. At the stock ceiling, clipping can merge damage outcomes, and the filter correctly combines their probability before updating. Public income is the deterministic function of this stock and is not counted as an independent signal.

I added `experiments/recoverable-inquiry/test_model.py` and independently ran all seven tests successfully. They include full latent-state enumeration of production and next-regime probabilities, exact noisy Bayes calibration, a pre-repair burden check, branchwise monetary conservation and prefunding, and verification that rebuilding cannot buy a same-period diagnostic. The initial cash-two control confirms that later output cannot finance an initially unaffordable repair.

Optimization receives two independent checks. A one-period enumerator integrates latent fault, noisy signal, contingent action, and damage without using the model's filtering or action-generation functions; exhaustive pure and two-policy mixtures match the constrained solution across stocks, cash states, priors, and five burden budgets. A two-period state/action occupancy-flow linear program independently optimizes the generated Markov decision problem and matches the vectorized Bellman mixture in adaptive and no-test modes at four budgets. Its flow residuals, expected burden, and minimum-burden optima are checked. An always-testing one-period controller has minimum burden .05 and is therefore infeasible at .02; the independent LP confirms that certificate. Absorbing zero stock is also checked.

These tests do not independently re-enumerate the full eight-period problem. They verify elementary kernels and short-horizon optimization by methods different from the main recursion. Larger calculations remain numerical solutions of the audited finite model, with their own primal/dual gaps and full outputs to be retained.

The inspected development results preserve the negative and positive cases. At horizon five and burden budget .6, the optimum has zero tests and zero rebuilds, with cost −32.5972782. At horizon eight and budget .02, expected tests are .1375297 and rebuilds .2957523, with cost −43.12729236 and reported dual gap about \(5.65\times10^{-10}\). This second policy's productive-collapse probability is approximately .1243894. It is therefore an illustration of selective, paid recovery under an expected burden constraint, **not** a certified safe or indefinitely viable institution. The horizons and burden budgets differ, so the two cases do not isolate the effect of horizon alone.
