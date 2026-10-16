# Durable concern inputs from paid noisy evidence

6 October 2026. AI-authored mathematical continuation of the [concern learner](learning-formal.md), its [paid action and succession model](dynamics-formal.md), and the [acquired consequence teacher](../../history/2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-TO-LEARNING-MATH.md). The named connection is **actually acquired consequence records → retained estimates → a warranted input to protective choice**. The results concern a declared operational model, not the origin of felt valence, moral standing or shared evaluation.

The repository already proves [stationary cumulative-evidence consistency and anytime likelihood certification](../../../experiments/history/2026-10-05-general-framework/reproduction-test/adaptive-evidence/FORMAL.md), including recurrent fixed-batch mistakes, changing-world failures and memory costs. The [general confidence controller](../../history/2026-10-05-specialist-dossier/final-synthesis/ADAPTIVE-OPTIMUM.md) already joins model retention to paid action requirements. We reuse that established statistical machinery. The contribution here is its exact interface with the concern score: constant-gain noisy teaching cannot generally provide durable protective choice, whereas retained evidence can support a signed joint lower certificate, with its costs and lifetime error allowance carried through succession.

## 1. The existing assumptions being replaced

The learned-action model selects repair exactly when

\[
z_t[b+H g_t w_t]>a,
\tag{1}
\]

where H>0 is a specified baseline harm, a>0 is the repair-attempt cost, b≥0 is the cheaper private unprotected cost, and g,w supply the installed shared evaluation route. Ties select the unprotected action. The case a>b rules out obtaining the relevant strict preference from private benefit alone when z≤1. Actual repair efficacy is Q: the corresponding recipient harm is (1−Q)H in the deterministic outcome model.

[Learning §4](learning-formal.md#4-learning-recognition-and-transferable-correspondence-from-zero) supplies an exact correspondence target σ. [Learning §6](learning-formal.md#6-can-self-relevant-evidence-favor-a-shared-architecture) validates a shared predictor only across the tested contexts; it expressly does not identify every new recipient's target. [Dynamics §7](dynamics-formal.md#7-correcting-a-harmful-action-rather-than-endlessly-increasing-concern) can suspend immediately on E≤0 only because its assay is exact, E=Q. A noisy negative reading cannot inherit that exact-sign interpretation.

Here numerical targets reach the process only through paid records. For the general convergence result, take bounded acquired streams with means β∈[0,1], σ∈[0,1], and p_z=(Q+1)/2∈[0,1], where Q∈[−1,1]. Their installed numerical summaries are

\[
w_n=\overline Y_n,\qquad g_n=\overline G_n,\qquad
z_n=2\overline Z_n-1.
\tag{2}
\]

The signed efficacy encoding admits harmful interventions instead of excluding them by definition. The relation between Z and Q is a supplied calibrated measurement law with an independently grounded baseline. It is not direct access to a hidden outcome oracle. A support-loss event can physically generate Y, as in the preceding paid-teacher study; an acquired correspondence record G still requires a validated matching procedure. This note does not derive σ, the completeness of that procedure, the self teacher's experiential interpretation, or the shared route from accurate prediction alone.

## 2. Constant gain fails an eventual positive margin

Consider the fully funded recurrence

\[
w_{n+1}=r w_n+\eta Y_{n+1},\qquad
0\le r<1,\quad\eta>0,\quad 0\le Y_n\le B,
\tag{3}
\]

with w₀≥0, independent identically distributed observations and p₀=Pr(Y_n=0)>0. Let M=max{w₀,ηB/(1−r)}. Induction gives 0≤w_n≤M.

**T1 — Recurrent loss of a positive action margin.** For every θ>0, w_n≤θ infinitely often almost surely. Consequently, if a>b, g_n∈[0,1] and z_n≤1, the repair choice (1) fails infinitely often almost surely, regardless of how well the other two coordinates are maintained.

**Proof.** Choose an integer L≥1 with r^L M≤θ; when r=0, L=1 suffices. Divide the observations into disjoint length-L blocks. Each block is all zero with probability p₀^L>0, independently of the other blocks. The probability of no such block after any fixed block index is the limit of (1−p₀^L)^k, hence zero. A countable union shows that all-zero blocks occur infinitely often almost surely. At their endpoints, w has decreased to at most r^L M. For the action claim choose θ=(a−b)/H>0. Since the bracket in (1) is nonnegative and g≤1, z≤1 gives

\[
z[b+Hgw]\le b+Hw\le a.
\]

Thus strict protective choice fails at infinitely many fully paid dates. ∎

This is not the earlier failure from unpaid gaps or memory loss: every update in (3) was paid and its actual observation was retained through the stated rule. It also does not say constant gain is useless for tracking changes. It shows that a favorable mean cannot supply the earlier all-date durability claim.

For an exact witness, let Y be Bernoulli(3/4), η=1/4, r=3/4, w₀=0, and keep g=z=1. With b=0, H=1, a=1/2, the mean coefficient tends to 3/4. Nevertheless, every run of three zero readings gives w≤27/64<1/2, and such runs recur almost surely. This fixture tests reliability of w with g,z supplied; it is not acquired correspondence.

## 3. Retained averages can supply eventual choice

Assume each of the three declared source sequences is stationary, independent and identically distributed within that stream, with values in [0,1] and the stated means. Actual acquisition preserves a prefix of each such sequence in chronological order: no outcome-selected omissions, substitutions, duplication or relabeling are allowed. A history-dependent schedule may choose which stream to acquire next or stop acquiring, but this source-sequence premise must remain valid under the physical sampling procedure. Independence between different streams is unnecessary. Actual counts may differ: at decision date t use w=\overline Y_{N_w(t)}, g=\overline G_{N_g(t)}, z=2\overline Z_{N_z(t)}−1. A zero count uses no claimed estimate; initial operative coefficients may remain zero.

Each average is implementable by

\[
\overline X_{n+1}=\overline X_n+
\frac{X_{n+1}-\overline X_n}{n+1},
\tag{4}
\]

or by preserving the actual sum and count. Unpaid opportunities do not increment n. There is no extra forgetting or unmodeled attenuation in this construction.

**T2 — Eventual durable choice under stationary acquired evidence.** Suppose all three counts tend to infinity, all observations, writes and subsequent decisions are actually affordable, the sufficient records are preserved between decisions and through succession, and

\[
\Delta=Q[b+H\sigma\beta]-a>0.
\tag{5}
\]

Then almost surely there is a finite decision date after which (1) holds at every decision. The result concerns eventual choice; it does not promise protection during initial learning.

**Proof.** The sample averages converge almost surely to their means. One elementary route uses centered bounded observations X_i−EX_i: independence and zero means leave only the one-index and paired-index terms in the fourth moment, giving E[(\overline X_n−EX)^4]≤3/n². Markov's inequality makes the probability of an error greater than any fixed ε bounded by 3/(n²ε⁴), a summable series. The probability of any such error after N tends to zero with the series tail. Applying this to a countable sequence ε→0 proves convergence. Intersect the three probability-one events. Counts tending to infinity and continuity of z[b+Hgw] then give convergence of the installed score to a+Δ; eventually it exceeds a. ∎

With fixed deterministic recipient efficacy Q, every repair after that date has actual harm (1−Q)H. A required harm ceiling H_max needs the additional true condition Q≥1−H_max/H. If instead Q is an average causal effect of stochastic individual treatment, the conclusion is about choice and expected harm reduction. A positive mean efficacy does not guarantee each individual is protected. Independent individual failure with fixed positive probability produces infinitely many failures during infinitely many deployments. No coefficient convergence removes that fact.

There is generally no deterministic finite date after which every history is protected. For a Bernoulli teacher with parameter strictly between zero and one, arbitrarily long finite strings of zero readings have positive probability. “Eventually almost surely,” “by a fixed deadline with high probability,” and “on every physical history” remain different claims.

## 4. An anytime finite certificate from actual counts

For this section the three streams are Bernoulli. Their probabilities are β, σ and p_z=(Q+1)/2. Fix one lifetime error allowance α∈(0,1). At count n≥1 in stream i let s be its actual success count and put

\[
\alpha_i(n)=\frac{\alpha}{3n(n+1)},\qquad
T_{n,q}(s)=\sum_{k=s}^n{n\choose k}q^k(1-q)^{n-k}.
\tag{6}
\]

Let d_n be the largest power of two no greater than n and D_n={k/d_n:0≤k≤d_n}. Its mesh tends to zero and is less than 2/n. Define

\[
L_i(n,s)=\max\left(\{0\}\cup
\{q\in D_n:T_{n,q}(s)\le\alpha_i(n)\}\right),
\qquad L_i(0,0)=0.
\tag{7}
\]

The grid makes the rule finite and, for rational α, exactly computable using acquired integer counts. It does not assume the true probability lies on the grid. In a single unknown stream with the other coordinates supplied, replace α/[3n(n+1)] by α/[n(n+1)]; the three-stream certificate must not be inferred from that simpler fixture.

**T3 — Simultaneous lower validity.** With probability at least 1−α, all three lower bounds are below their respective true probabilities at every count, including counts selected at data-dependent funded stopping times.

**Proof.** Fix a stream, n and true probability p. If L(n,S)>p, some admitted q>p satisfies T_{n,q}(S)≤α_i(n). Binomial upper tails are nondecreasing in q, so T_{n,p}(S)≤α_i(n). Under S∼Bin(n,p), the event T_{n,p}(S)≤c is an upper set of integer counts whose probability is at most c: at its smallest attainable count s₀, that probability is exactly T_{n,p}(s₀)≤c. Therefore Pr(L>p)≤α_i(n). No union over grid points is needed; their rejection events are nested. Sum over n using Σ_{n≥1}1/[n(n+1)]=1, then over the three streams. No independence between streams or successive looks is needed for this union bound. Every data-dependent count is included in the simultaneous event. ∎

The fixed-n binomial calculation is unconditional on remaining solvent long enough to acquire n records. A stopped learner holds a prefix of the declared source sequence, and its certificate event is a subset of the simultaneous event already bounded over all counts. The distribution of its records conditional on survival or on having reached n need not itself be Bin(n,p). This construction does not remove failed histories or replace their probability law with that of selected survivors.

Write ℓ_w=L_w, ℓ_g=L_g and ℓ_z=2L_z−1. An installed conservative action gate may certify only if

\[
\boxed{\ell_z>0,\qquad
\ell_z[b+H\ell_g\ell_w]>a.}
\tag{8}
\]

On the simultaneous-validity event, Q≥ℓ_z>0, β≥ℓ_w≥0 and σ≥ℓ_g≥0. Monotonicity on this nonnegative region proves Q[b+Hσβ]>a. Thus the probability that this rule ever falsely certifies the true fixed-model score is at most α, at any funded inspection or stopping time. The explicit positive-efficacy requirement avoids multiplying a negative lower bound by a lower estimate of the bracket, which would not in general yield a lower bound for the product.

This certifies the declared model score. The architecture must actually route the certificate into its decision and pay for repair; a record that is merely displayed cannot guarantee action. A deterministic harm ceiling can additionally require ℓ_z≥1−H_max/H. When Q describes average response, that remains an expected-effect certificate, not an individual-outcome guarantee. None of these inequalities certifies the normative relevance of σ or creates shared evaluation.

**T4 — Consistency of the finite certificate.** If a stream continues under its stationary Bernoulli law, L_i(n,S_n)→p_i almost surely. Consequently, under (5), continued complete sampling eventually makes (8) hold at every later inspection almost surely.

**Proof.** T3's fixed-count bound gives Σ_n Pr(L_n>p)<∞. Therefore L_n>p happens only finitely often almost surely, so the upper limit is at most p. The empirical frequency converges to p. Fix ε>0. For p>0 choose, for large n, a grid point between max(0,p−ε) and p−ε/2, shrinking ε below p if needed. Eventually S_n/n≥q+ε/4. The elementary Bernoulli Chernoff bound gives T_{n,q}(S_n)≤exp(−2n(ε/4)²), which is eventually smaller than α/[3n(n+1)]. This q is admitted, proving the lower limit. When p=0, all observed counts are zero almost surely and L=0. The endpoint p=1 satisfies the same lower argument. Combine the three convergences with the strict margin. ∎

For completeness, the bound used here follows directly from the Bernoulli moment generating function. For X∼Bernoulli(q), put ψ(t)=log E exp[t(X−q)]. Its second derivative is the variance of a Bernoulli variable under exponential tilting, at most 1/4, and ψ(0)=ψ′(0)=0. Integrating twice gives ψ(t)≤t²/8 for t≥0. Independence and Markov's inequality therefore give

\[
\Pr_q(S_n/n-q\ge\varepsilon)
\le\exp\{n[-t\varepsilon+t^2/8]\}.
\]

Choosing t=4ε yields exp(−2nε²), uniformly in q. This exponential eventually falls below the polynomial allowance in (6).

The Chernoff inequality, cumulative consistency and lifetime error allocation are standard machinery already used in the earlier evidence study. T3 and T4 have different meanings: a chosen upper bound on **ever** making a false certificate versus eventual correctness with no deterministic completion time. Neither proves validity after an unmodeled change.

## 5. No finite zero-error replacement for the exact assay

**T5 — Overlapping finite records obstruct zero-error deployment.** Consider two fixed worlds with identical accessible preparation and action costs, one with Q_+>0 and a score satisfying (5), and another with Q_-<0. Take finite or countable action and observation alphabets, as in the Bernoulli experiment here. Suppose every finite acquired transcript having positive probability in the helpful world also has positive probability in the harmful world, under the same admissible record-based policy. If that policy commits to repair after a finite transcript with positive probability in the helpful world, it also commits with positive probability in the harmful world.

**Proof.** The event of finite commitment is a countable union over finite decision times and finite transcripts. Positive probability gives some finite component with positive probability; its transcript and policy's conditional commitment have positive probability in both worlds. ∎

Bernoulli efficacy assays with probabilities strictly between zero and one have this overlap, including p_z=3/4 versus p_z=1/4, corresponding to Q=1/2 versus Q=−1/2. Adaptive paid stopping does not create a zero-error exact sign observation. A controller demanding zero probability of harmful deployment cannot make a nontrivial finite commitment on those overlapping records alone. Additional exact information or a declared positive error allowance changes the question; withholding a decision does not itself protect an ongoing recipient.

## 6. Resource, retention and change obligations

Every observation, record update, communication, transmission, protective action and necessary upkeep has an actual pre-return cost C_k. With actual available return R_k, retain

\[
B_k\ge C_k,\qquad B_{k+1}=B_k-C_k+R_k.
\tag{9}
\]

The [existing prefix-budget theorem](dynamics-formal.md#6-payment-and-the-order-of-events) applies to this complete cost sequence. Neither the expectation of future returns nor a favorable coefficient pays an earlier bill. Observations from stopped or failed histories must not disappear from the accounting. A resource-conditioned survivor sample is not automatically an iid evidence stream.

The infinite-sampling conclusions require continuing actual support. Finite closed fuel with a positive price per observation cannot realize them. Exact Bernoulli sums and counts require growing retained counters, O(log n) bits per stream, plus their storage, update and transmission machinery. No claim of fixed memory or constant physical write cost is made. Between updates and across successors, the full sufficient counts and model provenance must survive at their paid fidelity; transmitting only an attenuated coefficient does not implement (4) or (7).

The lifetime α allowance is retained too. Re-reading the same evidence does not create another independent sample. Starting a successor does not reset n or permit spending α anew. Separate conditionally valid episodes can allocate α_j with Σ_jα_j≤α, as in the earlier evidence study; the physical validity of a changed episode must be established rather than assumed by resetting counters.

Accumulation has a change cost. After N noiseless readings of one followed by k readings of zero, the retained average is N/(N+k); it remains above θ∈(0,1) while k<N(1/θ−1). Old evidence can therefore delay response to a changed dependency for a duration growing with N. Constant gain can respond faster, while T1 forbids its general stationary all-date guarantee. A paid change detector, qualified reset or finite-window policy needs its own error, response-time and harm account. Neither estimator is a universal solution.

## 7. What this closes and leaves supplied

Exact constant β, σ and Q need not arrive as repeated noise-free scalar inputs for eventual protective choice or a finite confidence certificate. Actual paid records can support those conclusions under an identified stationary observation law, retained sufficient evidence, a strict true-model margin and continuing feasible action. The constant-gain obstruction shows why the earlier mean recurrence cannot establish that result by itself.

The bridge does not derive the calibration of the assays, relevant correspondence, the updater or sensor's formation, shared evaluation, recipient standing, permission for probes, or guaranteed physical support. Probe harms retain their own ledger from the dynamics study; a statistical certificate does not erase them. Pathwise eventual choice, an anytime bounded risk of false certification, deterministic recipient protection, and expected individual outcomes are separate statements with separate premises. The next integration must implement and test those premises within the actual resource history, preserving rejected and underfunded histories rather than selecting successful learners afterward.
