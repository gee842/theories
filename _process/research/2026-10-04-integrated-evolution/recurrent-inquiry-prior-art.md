# Recurrent inquiry, negative evidence, and succession: prior-art audit

5 October 2026. Primary-source audit for the next research cycle. This memo evaluates the revised two-module design: **A**, dynamic control of inquiry and rebuildable capacity with freely retained beliefs; **B**, a single paid evidence channel at succession, conditioning on every surviving cue, including silence. It does not describe these modules as an implemented joint model of endogenous upkeep and paid intergenerational memory. The accompanying [design review](recurrent-inquiry-design-review.md) specifies the proposed experiment.

The strongest available contribution is a small, auditable demonstration of when preserving an investigative option pays despite declining to investigate immediately, alongside a correctly specified succession channel. Belief-state control, the decision value of negative results, optimal costly observation, and the information carried by nontransmission are established foundations. “A shared-purpose agent should sometimes conserve resources for future information” is already directly modeled in the literature.

## Five close primary anchors

**1. Smallwood and Sondik (1973), [The Optimal Control of Partially Observable Markov Processes over a Finite Horizon](https://doi.org/10.1287/opre.21.5.1071).** The finite-state, finite-horizon partially observed control framework uses state probabilities to represent uncertainty; its optimal payoff is piecewise linear and convex in those probabilities. Their maintenance example makes the connection to maintaining a physical capability particularly close. Our belief/capacity controller is an application and state augmentation of this framework, not a new decision principle. Access qualification: the publisher abstract was inspected; the full article was not available through the retrieved page.

**2. Reisinger and Tam, [Markov decision processes with observation costs: framework and computation with a penalty scheme](https://arxiv.org/abs/2201.07908), [version 3 manuscript, December 2023](https://arxiv.org/pdf/2201.07908v3), [journal DOI](https://doi.org/10.1287/moor.2023.0172).** They optimize when to purchase state observations and which controls to use, with finite- and infinite-horizon formulations, an augmented description involving elapsed time since observation, and computation through quasi-variational inequalities. Their principal observation-cost model holds a chosen action fixed between observations; it should not be cited as identical to every controlled-sensing model. It directly precedes the broad proposal to make inquiry timing endogenous to expected value. Rebuildable inquiry equipment supplies an additional state and action interface in our proposed example. The relevant framework and restriction were checked in the full version 3 manuscript.

**3. Nayyar, Başar, Teneketzis, and Veeravalli, [Optimal Strategies for Communication and Remote Estimation with an Energy Harvesting Sensor](https://arxiv.org/abs/1205.6018), [full manuscript](https://arxiv.org/pdf/1205.6018).** This is the closest combined precedent: a sensor and estimator share an objective, communication consumes replenishable energy, and preserving energy can improve future communication. Silence depends on private observations and available energy. Lemma 2, equation (9), updates the joint state/energy posterior using the nontransmission policy; Theorem 1 gives a finite-horizon dynamic program over communication prescriptions. Threshold simplifications require additional symmetry assumptions and are not general results. The sensor's own observation is free in this model. Our costly diagnosis and equipment rebuilding therefore differ from its physical primitives, while our common-interest allocation and selective transmission mechanisms substantially overlap. The full arXiv v1 manuscript was inspected; its arXiv submission is May 2012. This memo relies on those stated results rather than assuming a later journal version is identical.

**4. De Oliveira, [Blackwell’s Informativeness Theorem Using Diagrams](https://henriquedeoliveira588309899.wordpress.com/wp-content/uploads/2020/12/blackwells-informativeness-theorem-using-diagrams.pdf), author manuscript dated November 2017.** This primary proof of the established Blackwell theorem characterizes informativeness through garbling and the decision rules an experiment permits. More usable information cannot lower an optimal decision maker's gross value when it can be ignored and the comparison holds feasible choices and costs fixed. Theorem 5 discusses the corresponding dynamic comparison using adapted garblings: being more informative at each separate date is insufficient for every sequential decision problem. Our timing and memory interfaces must therefore be compared as information histories, not just as counts of records or marginal accuracy scores. This establishes no general preference for costly acquisition, compulsory disclosure, or unlimited storage. The full manuscript was inspected.

**5. Carley (1992), [Organizational Learning and Personnel Turnover](https://doi.org/10.1287/orsc.3.1.20).** A computational organization model studies repeated decisions, experience, distributed individual information, and turnover. Performance depends on task and organizational structure; institutional memory can reside in individuals and advisory relationships. This precedes the claim that succession and distributed memory alter organizational learning. It does not establish that turnover is universally harmful, or solve our proposed paid-archive optimization. Access qualification: the primary publisher abstract was inspected; claims here are limited accordingly.

## Elementary checks for the proposed modules

The following deductions are worked checks of standard decision theory, not claimed new theorems from this project.

### A negative result can be the source of a test's value

Let hidden need be \(X\in\{0,1\}\), with belief \(b=P(X=1)\). Taking no preventive action incurs loss \(H X\); prevention costs \(c\) and eliminates that loss, where \(0<c<H\). Before a test, optimal expected loss is

\[
L(b)=\min(Hb,c).
\]

A perfect observation permits prevention exactly when need is present, giving expected loss \(bc\) before the test charge. Thus the gross one-period value of perfect information is

\[
G(b)=\min(Hb,c)-bc
=\begin{cases}
b(H-c),&b\le c/H,\\
c(1-b),&b\ge c/H.
\end{cases}
\]

For \(H=10,c=4,b=.7\), prevention without inquiry costs 4. Inquiry followed by a contingent response costs 2.8 before the test charge. The 1.2 improvement comes entirely from avoiding an unnecessary intervention after a negative result: probability .3 times cost 4. With a test charge .5, inquiry pays. At \(b=.9\), its gross value is only .4 and the same test does not pay in the one-period problem.

The information value peaks at the action threshold \(b=c/H\), not generally at maximum uncertainty \(b=.5\). A negative result need not justify further testing, and a lack of validated improvements need not imply that an investigation was worthless. Conversely, a test with an irrelevant outcome or excessive cost can be wasteful. “Negative evidence” needs a known observation likelihood; an inconclusive measurement and evidence that need is absent are different events.

For an arbitrary diagnostic \(Y\), the gross value is

\[
L(b)-\sum_y P(y)L(b_y)\ge0,
\qquad b_y=P(X=1\mid Y=y).
\]

This follows because the agent can ignore the signal, equivalently from the concavity of \(L\) and posterior averaging. It assumes the diagnostic has no other physical effect, costs are excluded from this comparison, and the probabilistic model and feasible responses are held fixed. Net value can be negative after acquisition or storage charges. The inequality is ex ante; it does not assert that every realized branch delivers an improvement.

### Old evidence loses predictive force through state change

For a known binary Markov chain, write

\[
\alpha=P(X_{t+1}=1\mid X_t=0),\qquad
\beta=P(X_{t+1}=0\mid X_t=1).
\]

Without another observation, the belief obeys

\[
\Psi(b)=\alpha+(1-\alpha-\beta)b.
\]

If \(\alpha+\beta>0\), its stationary fixed point is \(\pi=\alpha/(\alpha+\beta)\), and

\[
\Psi^k(b)=\pi+(1-\alpha-\beta)^k(b-\pi).
\]

Under \(0<\alpha+\beta<1\), a perfect negative observation starts at zero and moves toward \(\pi\) as the observation ages. This is not forgetting the evidence; it is using it correctly for a changing state. If \(\alpha+\beta>1\), the deviations alternate sign, so monotone decay must not be claimed for every binary chain. With \(\alpha=\beta=0\), the state is static and perfect evidence remains decisive indefinitely.

This distinction limits claims about revising explanations. The model changes the state under a known transition law; it does not discover that the transition law, diagnostic likelihood, relevant variable, or purpose was wrong. Under these fixed assumptions, a retained sufficient belief and the known model can replace the full raw history for current decision making. An experiment cannot demonstrate a unique need for a paid raw archive while leaving that sufficient belief available for free. Unknown future questions or model revision could make raw records useful, but those require an expanded model.

### Keeping the capacity to inquire is a continuation-value decision

Let \(V_t(b,z)\) denote minimum expected future cost, where \(z\) is publicly known inquiry capacity. At a decision node where upkeep of cost \(m\) affects only whether next period starts ready or down, and leaves the next-belief distribution otherwise unchanged, upkeep is preferred exactly when

\[
m\le
\mathbb E\left[V_{t+1}(b',\mathrm{down})-
V_{t+1}(b',\mathrm{ready})\right].
\]

Ties admit either choice. Rebuilding is included among the future actions determining \(V\). This is a Bellman comparison under the specified timing, not an independent law requiring maintenance. If upkeep also enables the current test, changes hidden-state transitions, or carries a signaling effect, this shortened expression is incomplete.

The sharp witness is a reachable state with **no current test but strictly preferred upkeep**, together with its continuation-value gap and probability of occurrence. That separates preserving an option from continually exercising it. Expensive or delayed rebuilding can create this gap. With immediate free rebuilding and otherwise identical capabilities, it disappears. A last-period decision to stop upkeep follows from zero terminal value and does not establish an institutional tendency toward degeneration.

The model must include free observations supplied by outcomes, visible balances, previous actions, and equipment state whenever those are informative. Excluding a diagnostic while accidentally retaining its answer through an observed loss would invalidate the comparison. Resource caps constrain feasible policies; equal caps do not imply equal expenditure.

### Silence at succession is an observation, with a policy-dependent likelihood

Suppose a predecessor receives evidence \(E=e\), with probability \(q_e\) and posterior \(b_e=P(X=1\mid E=e)\). It sends a payload with probability \(d_e\); otherwise the successor observes silence \(\varnothing\). When silence has positive probability,

\[
P(X=1\mid M=\varnothing)
=\frac{\sum_e q_e(1-d_e)b_e}
{\sum_e q_e(1-d_e)}.
\]

The unconditional prior is appropriate only when this expression happens to equal it. With inherited public cues \(C\), use the conditional distributions given \(C\) and the actual transmission policy. A visible capacity or previous action can reveal predecessor information even if no document survives.

For a particularly sharp check, let the predecessor know binary \(X\) perfectly and have one reliable, publicly known messaging opportunity. Sending only when \(X=1\) reveals both states: a payload identifies one, silence identifies zero. Sending only when \(X=0\) also reveals both. With a constant charge \(a\) per payload and no other charges, choosing the rarer state achieves complete information for expected publication cost

\[
a\min(b,1-b).
\]

This is an attainable coding cost under those assumptions, not a claim that full revelation is always optimal after charging for it. It also exposes why a no-payload arm need not be a no-information arm. Failure to send can mean a different thing if the predecessor may be unavailable, the channel may fail, or the protocol is unknown; those contingencies belong in the likelihood. The physical reliability of the omission channel is a supplied resource in this simple model.

For finite evidence and message sets, a useful exact check of a selected channel \(\kappa(m\mid e)\) is

\[
J(\kappa)
=\sum_m\min_a\sum_e q_e\kappa(m\mid e)
\mathbb E[\ell(X,a)\mid E=e]
+\sum_{e,m}q_e\kappa(m\mid e)c(e,m).
\]

Messages include silence. The inner minimum is the receiver's best response to each message; zero-probability messages contribute zero. The formula avoids fabricating a posterior where Bayes' denominator is zero. Its conditional version handles public cues. In a binary, truthful-publication benchmark, enumerating allowed sender rules and receiver actions is enough to check an optimum without a hidden forgetting rule.

## What would make the experiment informative

Module A can contribute a transparent **mechanism separation**: current information value, the future value of a ready inquiry capability, rebuild delay, and the effect of a changing need. Compare the adaptive optimum with the best permitted ex ante capacity schedule, under the same observation and procurement interface. A weak arbitrary calendar is not an adequate baseline. Report the no-test/upkeep witness, its strict action-value gap, expected decision loss, and separate diagnosis, upkeep, rebuild, and response expenses. Include static need, prohibitive diagnostic cost, free informative feedback, and immediate free rebuild controls. Repeat early decisions under a longer horizon or keep the finite-horizon qualification explicit.

Module B can contribute a clean comparison of no paid publication, full publication, and optimized contingent publication. Report publication cost, all positive-probability cue/message posteriors, and successor decision loss. A selected positive-only or negative-only scheme may exploit informative absence, so count what the successor knows rather than equating payload count with information. If a claimed archive effect vanishes once the silence posterior is corrected, retain that failure as a result.

The integration still outstanding is substantial: derive successor cues from the earlier upkeep and inquiry policy; charge the actual retention and communication processes; and retain the joint likelihood of everything that survives. Calling two separate modules an integrated mechanism would conceal that work. Neither module recreates the previous study's candidate discovery and fresh causal validation; both supply the relevant state and information technology in advance.

## Boundary between a structural result and an ethical conclusion

An exact policy is optimal for a specified objective, model, horizon, and information interface. It does not establish that the objective is legitimate, that the modeled losses exhaust what matters, or that actual institutions will select that policy. Shared purpose is an assumption isolating an informational mechanism, not a solution to disagreement about purposes.

Blackwell dominance cannot by itself establish a duty to disclose, a right to inspect, or a universal prohibition on secrecy. Those commitments need a normative argument or an explicit constraint. Conversely, finding that selective communication minimizes a common expected loss does not justify real-world concealment: affected persons, privacy, accountability, changing questions, and unequal authority may be outside that objective. The same mathematics can expose these omissions but cannot supply their ethical weights.

The reusable framing is narrower and stronger than “always inquire” or “always preserve everything”: evaluate whether a system preserves the future ability to obtain and act on consequential information, while accounting for costs, delays, changing conditions, and the information already conveyed by its own behavior. A solved binary example can make that framing testable. It does not yet establish a universal direction of social evolution, a novel foundation for all information control, or an alignment solution.
