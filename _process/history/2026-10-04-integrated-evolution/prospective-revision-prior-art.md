# Prospective preservation and paid model audits: prior-art audit

5 October 2026. This memo concerns choosing a record format before knowing which later question will matter, then paying for an evidence-based challenge to a current model. The proposed test examines temporal order in a binary switching history under a composite constant-rate null. This is a design and literature audit, not a report of the completed institutional experiment.

The strongest contribution target is explicit coupling: an earlier preservation decision changes which later audits are feasible; audit costs and statistical resolution affect whether a challenge receives consideration; an admitted model changes action only through a specified decision rule. Each component has substantial prior art. The test can supply a reason to reconsider a model without already identifying a true replacement, and it cannot itself invent an unanticipated concept.

## Focused primary sources

**1. Tishby, Pereira, and Bialek, [The information bottleneck method](https://www.princeton.edu/~wbialek/our_papers/tishby%2Bal_99.pdf), September 1999 manuscript, posted to arXiv in April 2000.** The method chooses a compressed representation of one variable while preserving information about a specified relevance variable. Its objective trades \(I(X;\widetilde X)\) against \(I(\widetilde X;Y)\), given the joint distribution. This directly precedes purposeful preservation under limited representational capacity. It also exposes the assumption: relevance and its distribution are supplied. The objective is not a universal measure of every future question, and mutual information is not identical to the value of a particular costly action. The full manuscript and its variational objective were inspected.

**2. Russo and Van Roy, [Learning to Optimize via Information-Directed Sampling](https://arxiv.org/pdf/1403.5556v7), inspected July 2017 v7 manuscript; published in Operations Research in 2018.** Their policy balances immediate regret against information about the optimal action, accommodating observations that inform other actions. It supplies a close primary precedent for selecting experience because of its future decision value, rather than maximizing immediate reward or indiscriminate knowledge acquisition. Its information-ratio rule is a tractable policy with regret guarantees under stated assumptions, not generally the exact finite-horizon Bellman optimum. It does not by itself provide institutional model admission or discovery outside its supplied probabilistic structure.

**3. Gelman, Meng, and Stern (1996), [Posterior predictive assessment of model fitness via realized discrepancies](https://sites.stat.columbia.edu/gelman/research/published/A6n41.pdf).** They compare observed discrepancies with predictive replications and specify which auxiliary features remain fixed. Equations (2)–(7) distinguish sampling and posterior-predictive reference distributions, which coincide for a statistic pivotal conditional on the auxiliary information. This is a direct precedent for checking a model against aspects of its evidence that its fitted predictions can conceal. Our proposed audit instead has a nuisance-free conditional null distribution, so its error guarantee should be proved directly rather than imported from generic posterior predictive checking. The main article's framework was inspected; the linked PDF also contains discussion and rejoinder.

**4. Hemerik and Goeman (2018), [Exact testing with random permutations](https://link.springer.com/article/10.1007/s11749-017-0571-1).** Section 2 and Theorem 1 give the level guarantee for a fixed transformation group under null invariance. Their later results address valid random-permutation implementations. This supplies the immediate foundation for conditioning on the total number of binary switches and testing their arrangement. In a small finite example, enumerate the conditional orbit directly and include ties in the tail probability. “Exact” here can mean finite-sample validity with rejection probability at most the nominal level; discrete tests need not attain that level. The published article was inspected.

**5. Fithian, Sun, and Taylor, [Optimal Inference After Model Selection](https://arxiv.org/pdf/1410.2597v4), April 2017 v4 of a 2014 working paper.** They formulate selective error conditional on a question being selected and derive tests in exponential-family settings. Proposition 3 separates conditioning on coarser and finer selection information. This directly applies when an institution audits cases selected because they already look suspicious. It does not imply that every decision to skip a fixed test invalidates the unconditional error bound. The distinction between selective and per-episode errors below is essential. The current v4 formulation was inspected.

**6. Ben-David, Lu, Luu, and Pál (2010), [Impossibility Theorems for Domain Adaptation](https://proceedings.mlr.press/v9/david10a.html).** Added in final review after U exposed the central identification limit. The paper studies adaptation with labeled source observations and unlabeled target data, showing failures under insufficient assumptions and indistinguishable tasks for which reweighting has different effects. This is a closer precedent for missing target-relevant information than compression alone. It does not establish the present paid admission protocol; our bounded-test proof is supplied directly. The primary proceedings abstract was inspected.

No claim of priority for compression, purposeful experimentation, model checking, conditional testing, or observation-based nonidentifiability is warranted. The earlier [model-revision audit](model-revision-inheritance-prior-art.md) covers model-relative sufficiency and the distinction between conditioning within a model and expanding its support.

## Choosing what to preserve before the question arrives

Let \(D\) be the observed history, \(Q\) a later question, \(\Theta\) the relevant latent state or model, and \(f\) a record format selected before \(D\) and \(Q\). A minimal decision formulation is

\[
\min_{f\in\mathcal F}\;
\mathbb E\left[
c_{\mathrm{store}}(f,D)
+\min_a \mathbb E[\ell_Q(\Theta,a)\mid f(D),Q]
\right].
\]

This expression assumes that the question is revealed before the response. Paid inspection, testing, transmission, and implementation can replace the inner minimum with the appropriate continuation problem. It also assumes the initial observation and encoding interfaces: choosing a record format is not the same as deciding which experiences are acquired in the first place.

The prior joint law of \((\Theta,D,Q)\), possible formats, feasible actions, and losses do substantive work. A distribution over later questions makes preservation prospective rather than a hindsight ranking, but does not make the questions genuinely unforeseen to the modeler. If that distribution is unknown, a specified ambiguity set and minimax or regret criterion are alternatives; they introduce other assumptions rather than eliminating the choice.

A useful elementary check illustrates the boundary. Suppose question zero occurs with probability \(1-\lambda\), question one with probability \(\lambda\), and the question is revealed at handoff. A richer format costs an additional \(\Delta C\), has identical optimized continuation loss for question zero, and improves it by \(B>0\) for question one. Then the richer format pays exactly when

\[
\lambda B>\Delta C.
\]

This is a standard expected-value calculation, not a general archive threshold: if the question is not revealed, policy constraints differ, or costs depend on history, recompute the joint problem. Even here, high storage cost or a low probability of the relevant question favors compression. No universal maximization of memory follows.

## An exact conditional audit of temporal order

Let \(B_1,\ldots,B_N\) be consecutive, completely observed switch indicators. Under the null they are independent Bernoulli variables with the same unknown rate \(h\). For \(K=\sum_i B_i\), every binary arrangement with \(K=k\) has equal conditional probability:

\[
P_h(B=b\mid K=k)=\binom Nk^{-1}.
\]

The nuisance parameter cancels. The result also holds for a mixture over constant \(h\), and more generally for an exchangeable binary history conditional on its count. It does not hold for arbitrary policy-selected, irregularly spaced, or missing observations without further argument.

For \(N=2m\), let \(A\) count switches in the first half, and define the prespecified discrepancy \(T=|K-2A|\). Its conditional distribution is determined by

\[
P(A=a\mid K=k)=
\frac{\binom ma\binom m{k-a}}{\binom{2m}k},
\qquad \max(0,k-m)\le a\le\min(m,k).
\]

Define

\[
p(b)=\sum_{a:\,|k-2a|\ge T(b)}
\frac{\binom ma\binom m{k-a}}{\binom{2m}k}.
\]

Rejecting when \(p\le\alpha\) satisfies

\[
P_h(p\le\alpha\mid K=k)\le\alpha
\quad\text{and hence}\quad
P_h(p\le\alpha)\le\alpha
\]

for every null rate, on every conditioning event with positive probability. Degenerate counts give \(p=1\). This is the standard finite conditional permutation argument. It does not estimate the probability that the null is true, and its rejection need not establish a single change point, its location, or the proposed two rates.

### Archive limitations and a necessary distinction

A count-only archive cannot calculate the observed arrangement discrepancy. If its randomized rejection probability is only \(r(k)\) and it must satisfy the same **conditional-on-every-count** level guarantee, then \(r(k)\le\alpha\) for each count. Consequently its power is at most \(\alpha\) under any alternative distribution of that count. A deterministic count-only rule with this guarantee and \(\alpha<1\) never rejects.

There is a separate, stronger directional indistinguishability result: equal-length slow-then-fast and fast-then-slow alternatives induce the same distribution of \(K\). Any count-only procedure has the same output distribution under those two alternatives and cannot learn their order. An independent fair initial state makes the public endpoint uninformative about that order as well; a known initial state adds only parity already contained in \(K\).

Do not generalize this to “counts contain no evidence against any constant-rate model.” A heterogeneous-rate count distribution can differ from a constant-rate binomial distribution. A different unconditional test can use that difference. The proposed audit deliberately conditions it away to test arrangement without knowing the constant rate.

### Small archives can make the admission gate ineffective

At \(N=4,K=2\), the most extreme midpoint discrepancy has two arrangements among six, giving two-sided \(p=1/3\). No arrangement in a four-transition archive passes this nonrandomized audit at \(\alpha=.05\). At \(N=8,K=4\), the two extreme arrangements give \(p=2/70\), so rejection becomes possible.

Possible does not mean powerful. Direct finite summation at \(\alpha=.05\), with rate .05 in the first half and .45 in the second, gives:

| Observed transition indicators, \(N\) | Probability the specified audit rejects |
|---:|---:|
| 4 | 0 |
| 8 | .033400418828125 |
| 12 | .052794563631811 |
| 16 | .198392502256310 |
| 24 | .476495854620963 |

These are planning calculations for this fixed statistic and alternative, not held-out evidence or a recommendation to tune after evaluation. Nonadmission in the small cases can be forced by discreteness or low power. It must not be interpreted as evidence that the current model is adequate.

The numbers are reproducible with the following standard-library calculation; no simulation or estimated null parameters are involved:

```python
from math import comb

for m in (2, 4, 6, 8, 12):
    power = 0.0
    for a in range(m + 1):
        for b in range(m + 1):
            k, t = a + b, abs(b - a)
            numerator = sum(
                comb(m, j) * comb(m, k - j)
                for j in range(max(0, k - m), min(m, k) + 1)
                if abs(k - 2*j) >= t
            )
            # Exact comparison with alpha=1/20; avoid tail-rounding decisions.
            if 20 * numerator <= comb(2*m, k):
                power += (comb(m, a) * .05**a * .95**(m-a)
                          * comb(m, b) * .45**b * .55**(m-b))
    print(2*m, power)
```

## Paid selection: which error rate is protected?

Let \(R\) be rejection by one fixed, predeclared test and \(S\) the event that the institution performs its audit.

**Per-episode false admission:** even when selection favors suspicious histories,

\[
P_h(S\cap R)\le P_h(R)\le\alpha.
\]

Declining to run this one test cannot enlarge its rejection event. This observation assumes that the test itself, its threshold, and its data window remain fixed.

**False rejection among audited cases:** \(P_h(R\mid S)\) can exceed \(\alpha\) if selection depends on arrangement. If selection depends only on \(K\), independent randomization, and other cues that leave the conditional arrangement law unchanged, the conditional guarantee also protects the audited cases. Otherwise use the appropriate selection-conditioned reference distribution if that is the error rate being claimed.

**Search over tests or windows:** choosing a midpoint, discrepancy, direction, or archive window after seeing order is a different procedure. Calibrate the maximum/search statistic over its null orbit, account for selection, adjust multiple tests, or use fresh evidence. Repeated opportunities across succession also need an explicit cumulative error criterion. A one-episode level guarantee does not imply a lifetime guarantee.

Acquisition rules matter independently of reporting rules. Consecutive null switches are exchangeable, but a retained sample chosen from them because it looked unusual need not be. A policy can alter which observations are available and thereby invalidate naive permutations of the observed subset. The likelihood and permutation reference must match the actual acquisition and selection protocol.

## What an evidence-triggered admission mechanism establishes

A paid audit can make **activation** of a supplied alternative depend on retained evidence instead of a calendar or an automatic handoff. That is a useful advance in the institutional mechanism. It does not make the alternative's vocabulary, change-point structure, or admissible rates endogenous discoveries. The audit statistic already encodes one way the current model might fail.

Rejection says that the observed arrangement is atypical under the declared null at a controlled error rate. Other mechanisms—measurement changes, omitted covariates, serial dependence, selective sampling, or another temporal pattern—can produce that result. The candidate therefore needs its own predictive or decision assessment. A rule that forces a particular replacement immediately upon rejection is a supplied institutional rule whose costs and mistakes should be evaluated, not a theorem that rejection identifies truth.

Keep the planner's broader uncertainty separate from the institution's restricted current model. If the planner values preservation because ordered regimes might matter, its metamodel already admits that possibility. A current operational rule can still prohibit using it until a paid audit passes, but this is a controlled representation or authority restriction. It is not an ordinary Bayesian posterior that both assigns zero probability to an alternative and anticipates learning that alternative through conditioning.

Similarly, specify what payment buys. If the actor already sees the full order to decide whether to purchase an audit, payment buys analysis, certification, or authority rather than acquisition of that order. If payment buys access, its decision must depend only on information available before access. Audit requests, format choices, expenditures, and silence can themselves convey information and must enter successor inference when visible. A deterministic audit result is a function of its underlying evidence, not a second independent observation to multiply into a likelihood.

The useful contribution would be a verified account of how prospective preservation, feasible criticism, and consequential revision fit together under stated costs and uncertainty. Necessary controls include null calibration, low-power histories, high audit costs, sufficient-summary versus raw-record equivalence where it holds, and a misspecified alternative that rejects the null without improving action. More admissions, more inquiry, and more memory are not by themselves evidence of better coordination.
