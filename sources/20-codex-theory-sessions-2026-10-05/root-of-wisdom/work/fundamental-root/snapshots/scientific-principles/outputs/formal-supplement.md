# Supplementary proofs and verification scope

This note adds the resource coupling argument and explicit decision assumptions to the [main investigation](scientific-principles-investigation.md). All results are conditional applications of established mathematics. The numerical checks are synthetic verification, not empirical experiments.

## A finite information and budget bound

Consider two finite-history models with identical initial transcript laws. Suppose at most N further observations are possible. At every common history and available action, assume the total variation between the two conditional laws of the complete next observed increment is at most ε. The increment must include observed resource changes, available-action changes, and other cues. A common policy includes adaptive choices and stopping; after it stops, append an identical terminal symbol.

Couple initial histories and policy randomization. Whenever histories still agree, maximally couple the next increments. They remain equal at that step with conditional probability at least 1−ε. Induction gives probability at least (1−ε)ᴺ that the full histories remain equal. Consequently,

\[
\operatorname{TV}(P_0^\pi,P_1^\pi)\le1-(1-\varepsilon)^N,
\qquad \alpha+\beta\ge(1-\varepsilon)^N.
\]

If every observation costs at least c>0 from a nonreplenished budget B, N≤⌊B/c⌋. This is a necessary bound, often loose. It fails if informative initial or passive evidence is excluded, the conditional ε bound ceases to hold after an intervention, or resources replenish and allow additional observations. The main report instead uses the abstract attainable separation D(B,d), which needs fewer structural assumptions but must be bounded or computed to guide a real inquiry.

This proof does not assume the observer is causally passive. It assumes the actual action-dependent transcript laws satisfy the stated bound. Calling every process causally embedded is insufficient to establish that premise.

## Why a free information option cannot worsen optimal risk

Fix a joint probability law for state Θ and available reports, an action set, and an integrable loss L(Θ,a). Let information F be contained in G, and define

\[
R(F)=\inf_{a\text{ measurable with respect to }F}E[L(\Theta,a)].
\]

Every F-based rule is also G-based, so R(G)≤R(F). This is inclusion of permitted decision rules. It requires that extra information may be ignored and does not remove old actions, change the target, impose unavoidable processing costs, or alter the loss. It concerns the optimum, not the behavior of a bounded real reader.

For a fair binary state with unit classification loss, acting without a signal has risk .5. A symmetric diagnostic of accuracy .9 permits risk .1. Gross decision value is .4; testing at cost .6 in the same loss units is worse. A perfect destructive test that eliminates the valuable action violates the unchanged-action premise altogether. These cases distinguish information from the net value of its acquisition.

## Two distinct ways to control repeated error

For fixed hypotheses and deterministic test allocations αⱼ, if each true-null test obeys P(false rejection at j)≤αⱼ, then the union bound gives P(any false rejection)≤Σⱼαⱼ. Independence is unnecessary. The fixed-prefix spending example uses this argument.

For adaptively selected hypotheses and predictable allocations, a sufficient condition is validity of the true-null test conditional on the selection history, with Σⱼαⱼ≤α almost surely. Conditional expectation followed by the union bound yields the same global guarantee. Ordinary unconditional validity for a fixed, unselected hypothesis does not automatically establish this stronger condition.

A different route controls a whole process. Under a declared positive null conditional mass pₜ and a normalized forecast qₜ selected before Yₜ, let

\[
M_t=\prod_{s=1}^{t}\frac{q_s(Y_s\mid H_{s-1})}{p_s(Y_s\mid H_{s-1})},\qquad M_0=1.
\]

The conditional expectation of each ratio is one, so M is a nonnegative martingale. Let τ be its first crossing of 1/α. For finite n, bounded stopping gives

\[
1=E[M_{\tau\wedge n}]\ge\alpha^{-1}P(\tau\le n).
\]

Taking n upward bounds the probability of ever crossing by α. A nonnegative supermartingale suffices. Choosing qₜ using Yₜ invalidates this proof. A composite null requires a guarantee for each null law; an estimated denominator is not automatically safe. This argument explains the simple likelihood-ratio rule used in the report. [Howard et al. 2020](https://arxiv.org/pdf/1808.03204v7)

## Identifiability is not uniform finite discrimination

For a target Q(θ), identification from a given data distribution means that Pθ=Pθ′ implies Q(θ)=Q(θ′) throughout the declared class. It does not require identifying every feature of θ. Even if a parameter is identifiable, arbitrarily close probability laws can prevent a single finite-sample procedure from uniformly distinguishing nearby parameter values with small errors.

For composite hypotheses, overlapping distributions defeat uniform discrimination across the overlap. Disjoint but arbitrarily close families can also have weak uniform finite-sample performance. The main report's exact optimum (1−TV)/2 pertains to two supplied simple hypotheses, equal priors, and unit error loss. It is not a general theorem that every scientific question can be reduced to those premises.

## What was checked

The main [calculation](reproduce.py) uses standard-library rational arithmetic. It checks the 20-toss .5-versus-.75 example, 100-observation stopping rules, a causal observational-equivalence example, a sensor-calibration example, and the common-failure replication model. Its [results](verification-results.json) retain exact fractions.

An independent investigator also enumerated 35 four-outcome probability laws against each other and all 16 deterministic binary decisions: 19,600 exact checks of the total-variation inequality and optimal-risk identity. Randomized tests are covered by the written proof and convexity, not by claiming an infinite enumeration.

A separately implemented rational recurrence reproduced the main sequential probabilities. Exhaustive enumeration of 4,096 length-12 paths under p=.5 and p=.75 independently checked both threshold-crossing probabilities and expected sample counts. The delivered main script includes its own exhaustive length-10 checks under both laws with a nonvacuous terminal test.

The independent formal memo additionally used p=.8 and a horizon of 200. Ordinary repeated inspection then had false-alarm probability .244627302, compared with .000489253 under the displayed spending schedule and .036712796 for the .8 likelihood-ratio rule. These are different declared experiments, not inconsistent reruns of the main .75/100 calculation; neither establishes universal efficiency rankings.

Proof review found and corrected a random-entry-time qualification in the permanent-error argument, an omitted initial-law condition in adaptive indistinguishability, and an incorrect citation link. Method review also corrected an evaluation-control interpretation and matched the marginal miss probabilities in the independent-check comparison. The [decision record](research-record.md) retains those corrections.
