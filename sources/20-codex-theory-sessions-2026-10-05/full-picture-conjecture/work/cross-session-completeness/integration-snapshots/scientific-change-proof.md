# Conditional results for mechanisms of scientific change

These results support the [mechanistic synthesis](mechanisms-of-scientific-change.md). They are conditional applications of established probability, learning, and dynamical reasoning. They are not presented as new mathematical discoveries or empirical laws of science.

## A useful representation can be inaccessible through individually improving steps

Let independent fair bits X₁,…,Xₖ, with k≥2, generate

\[
Y=X_1\mathbin{\mathrm{XOR}}\cdots\mathbin{\mathrm{XOR}}X_k
\mathbin{\mathrm{XOR}}E,
\qquad E\sim\mathrm{Bernoulli}(\epsilon),\quad 0\le\epsilon<1/2.
\]

The noise E is independent of all the feature bits. The learner can represent any Boolean prediction based on a retained subset of the features. Its objective is prediction error plus λ times the number of retained features, with λ≥0. Starting from no features, it permits only one-feature extensions that strictly improve the estimated objective; it cannot skip rejected intermediate representations.

First take exact risk evaluation. Conditional on any proper subset of the k bits, an unseen fair bit leaves Y fair. Every such predictor therefore has true error 1/2. A singleton scores 1/2+λ; the constant predictor scores 1/2. With λ>0 the extension is worse; with λ=0 it ties and fails the strict-improvement rule. The learner never takes its first step. Yet the complete parity predictor scores ε+kλ, which is better if

\[
k\lambda<\tfrac12-\epsilon.
\]

The obstruction is a restriction on the path of generation or admission. The linked data can contain information about the complete relation. This is not an observation-equivalence result.

A robust version allows risk-estimation error at most δ simultaneously for the baseline and every candidate considered. If λ>2δ, all singleton extensions still fail. If additionally

\[
\tfrac12-\epsilon-k\lambda>2\delta,
\]

the full candidate still wins when available. This is conditional on the simultaneous accuracy event. Establishing that event's probability requires the sampling and fitting protocol, including selection among candidates. A pointwise bound for one fixed predictor is not enough for arbitrary reuse of the fitting sample.

This cost is per feature; the numerical experiments use a different stated penalty per additional table cell. They instantiate the same obstruction but should not be described as numerically identical objectives. Multi-feature proposals, a different representation grammar, or permission for neutral intermediate moves can remove the obstruction.

## Effective testability depends on the available protocols

Fix two hypothesis packages θ₀ and θ₁, a deadline d, budget B, and feasible protocol class Π(A,B,d), where A records installed capabilities and access. A protocol includes experiments, measurements, record use, computation, and stopping. Write Pᵢᵖ for the complete accessible-transcript law under package i and protocol p.

The contrast is locally effectively testable at error limits (α,β) if an available p and possibly randomized decision rule φ satisfy

\[
\mathbb E_0^p\phi\le\alpha,\qquad
\mathbb E_1^p(1-\phi)\le\beta.
\]

For each protocol,

\[
\alpha+\beta\ge1-\operatorname{TV}(P_0^p,P_1^p)
\]

is necessary. Consequently

\[
\alpha+\beta\ge1-\sup_{p\in\Pi(A,B,d)}
\operatorname{TV}(P_0^p,P_1^p)
\]

is a useful impossibility bound. Total variation alone does not characterize every individually specified error pair. A supremum also need not be attained.

If Π(A₀,B,d)⊆Π(A₁,B,d), every error pair attainable with A₀ remains attainable with A₁: keep the old protocol. Strict improvement occurs, for example, when all old transcript laws coincide but a newly feasible, affordable, timely observation perfectly distinguishes the packages. Without that observation, α+β<1 is impossible; with it, both errors can be zero.

The inclusion requires that added capability can be ignored without losing old access or imposing extra costs. An obligatory maintenance bill, changed target, or destructive intervention can invalidate it. Existing substitutes can eliminate strict improvement. Feasibility also does not imply that an investigator has formulated the question, obtained permission, or selected the test.

For an empirical application, measure access independently of the outcome being explained: executable instrument functions, calibration, retained record fields, trained operators, permissions, restoration delays, and prices. Defining capability as whatever would have averted an observed failure makes the explanation circular.

## Maintenance and reconstruction can have different thresholds

Let Cₜ∈{0,1} indicate an installed diagnostic capability. Maintenance costs m>0 per period; reconstruction costs k>m. Each period supplies funding rₜ that cannot be saved or borrowed against future receipts. There is no substitute or external restoration. Under a stipulated policy that maintains or reconstructs whenever affordable,

\[
C_{t+1}=1
\quad\Longleftrightarrow\quad
(C_t=1\text{ and }r_t\ge m)
\text{ or }(C_t=0\text{ and }r_t\ge k).
\]

At a constant m≤r<k, both states are absorbing. There are two stationary point-mass distributions, and the long-run state depends on the initial capability. Along an increasing funding path, reconstruction occurs only at k. Along a decreasing path, loss occurs only below m. This is an exact hysteresis mechanism.

For m=1 and k=3, initial C=1 and funding sequence (0,2,3,2) give states (1,0,0,1,1), including the initial state. Funding restored to 2 sustains existing capability but does not reconstruct it. A temporary increase to 3 does.

Combined with the previous result, the two histories can have different attainable error guarantees at equal current funding. They are not identical complete states: installed capability differs. The explanation records a durable consequence of history rather than violating a Markov description with a sufficiently rich state.

Allowing savings, credit, replacement, or a rebuilding grant can remove permanent trapping. A finite deadline can still make a reconstruction delay consequential. These conditions must be checked in a real institution.

If instead an absent capability is restored with probability ρ>0 each period and an installed one is lost with probability η>0, with both below one, the transition matrix is

\[
\begin{pmatrix}1-\rho&\rho\\\eta&1-\eta\end{pmatrix}.
\]

Its unique stationary installed share is ρ/(ρ+η). Starting absent, mean time to first restoration is 1/ρ and restoration by T periods has probability 1−(1−ρ)ᵀ. This is no longer a permanent absorbing trap. Small restoration rates can instead explain long-lived deficits and finite-horizon inaccessibility.

## Method prevalence does not identify its cause

Let x(t) be the share using a method. Differential expansion with advantage s>0 can generate

\[
\dot x=sx(1-x).
\]

The identical equation results in a fixed population if nonusers switch at per-person rate sx and no one switches back. One process changes which people or groups occupy the population; the other changes existing people's practices.

Aggregate shares therefore do not distinguish these mechanisms. Within-person switching can itself reflect learning, imitation, incentives, or compliance. Useful data include stable actor identities, entry and exit, resources, evidence received, beliefs, and actual procedures. These are additional observations, not conclusions recoverable from the prevalence curve alone.

## What a fresh check of an edited rule establishes

The supplied rule-edit experiment compares incumbent and edited procedures on paired tasks. Let D be incumbent loss minus edited loss for one task pair, including the declared prediction errors and operating expenses. The task family and both procedures are fixed before the checking sample. The selected edit is independent of the fresh checking outcomes, conditional on the discovery history.

In the default experiment, each policy's cash expense is between 8.75 and 20.06 units, and each has between 0 and 64 prediction errors. Hence D∈[−75.31,75.31]. For n independent task pairs and μ=E[D], Hoeffding's inequality gives

\[
\Pr\!\left(\bar D-\mu\ge
150.62\sqrt{\frac{\log(1/\alpha)}{2n}}\right)\le\alpha.
\]

Accepting the edit only when the corresponding lower bound is positive controls the probability of accepting an edit with nonpositive mean gain at α for this one fixed check. Selection from the earlier discovery data does not invalidate the bound because the checking sample is fresh and the bound holds for any selected fixed edit satisfying the range assumptions.

At n=256 and α=.05 the radius is approximately 11.521238. The noiseless interaction task has gain 20.69, so the reported lower bound is 9.168762. Because this world is noiseless and balanced, the 20.69 gain also follows by exact calculation over every possible relevant feature pair and complement, independently of the confidence bound.

The guarantee concerns expected episode loss under the declared stationary task family. It is not a guarantee for every task, unrestricted distribution shift, total research profitability, or an unlimited sequence of attempts. Rechecking until a result passes requires a sequentially valid procedure or an explicit error allocation. The saved follow-up with a larger sample uses a new seed and is a separate study; it is not an extension of the failed checking prefix.

The selected edit removes one prefix-improvement condition. The edit grammar, protected access, prediction objective, outer checking rule, prices, and availability of routine outcome feedback are supplied. The result demonstrates endogenous choice and enactment of a local rule revision within those conditions, not the invention of every condition supporting that revision.

## A finite sequence of revisions can have an explicit error allowance

In the separate three-phase experiment, the installed rule carries forward and the edit toggles the prefix requirement in either direction. Before each check, condition on all prior history and freeze the current rule, proposed edit, task law, sample size, and costs. Fresh checking outcomes then satisfy the preceding bound conditionally at the phase allowance αₜ.

Let Fₜ mean that phase t accepts an edit whose expected episode gain under that phase's task law is nonpositive. Conditional error control implies P(Fₜ)≤αₜ after averaging over the previous history. Therefore

\[
\Pr\left(\bigcup_{t=1}^{3}F_t\right)
\le\sum_{t=1}^{3}\Pr(F_t)
\le\sum_{t=1}^{3}\alpha_t=.05,
\]

using αₜ=.05/3. Independence of the phase decisions is unnecessary; freshness and the conditional bound are what matter. A failed discovery screen produces no accepted edit and does not increase this bound.

This finite guarantee permits the rule to be revised and later revised back. It does not certify a lifetime of unlimited checks, detect distribution changes, guarantee adequate statistical power, or finance future checks. In the implementation the three task phases, study times, budgets, and sample sizes are supplied. Claims about endogenous trigger selection or resource renewal would require additional mechanisms.
