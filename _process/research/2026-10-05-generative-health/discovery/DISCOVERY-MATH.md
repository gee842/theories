# Costly discovery, validation, and establishment under maintained inquiry

Research candidate / internal mathematical analysis. Prepared 5 October 2026. This is a scoped extension of the establishment calculation, not a universal law of invention or a claim of theorem priority.

## 1. What is added, and what is inherited

The earlier [establishment result](../../../history/2026-10-05-generative-health/MATHEMATICAL-ANALYSIS.md) assumes a successor design is already available. The present extension charges candidate production, noisy validation, and installation to the same physical effort that maintains both current functioning and the capacity to inquire. It supplies an exact resource clock and exact true/false installation probabilities for a declared batch protocol, plus a finite sufficient confidence-and-resource bound.

It does **not** derive how new concepts or useful designs are invented. Candidate quality follows a supplied stochastic law. In this respect the existing situated-discovery experiment has a richer mechanism: its learner constructs contextual policies within a supplied grammar. The present reduction isolates integration with maintenance and paid installation.

The existing [candidate-discovery analysis](../../2026-10-04-integrated-evolution/candidate-discovery-math.md) already distinguishes nomination, fresh validation, rights, and implementation costs. The [prospective-revision analysis](../../2026-10-04-integrated-evolution/prospective-revision-math.md) already distinguishes anomalies from useful new questions and prices fresh validation. The [recurrent-inquiry analysis](../../../history/2026-10-04-integrated-evolution/recurrent-inquiry-math.md) already prices inquiry upkeep and explains why unused capacity can have future value. Its procurement allowance is supplied externally; operation and implementation are not jointly financed by the production-margin calculation below. Those earlier results are inherited, not rediscovered here.

## 2. The exact work available while operation and inquiry survive

Let two independently specified supports be `c_1` for current operation and `c_2` for inquiry. Their floors `c_i* > 0` are required throughout the interval. Inquiry at its floor means the apparatus and competence remain functional; actually producing or testing a candidate still consumes additional work.

Allocate maintenance efforts `u_1,u_2 >= 0` subject to `u_1+u_2 <= 1`, with

\[
\dot c_i=\alpha_i u_i-\delta_i c_i,
\qquad c_i(0)=c_{i0}\ge c_i^*,\qquad i=1,2.
\tag{D1}
\]

The remaining effort `w=1-u_1-u_2` can perform discovery, validation, or installation. It is work capacity, not cash that can be spent several times. Assume positive finite parameters and define

\[
p_i=\frac{\delta_i c_i^*}{\alpha_i},
\qquad
t_i=\frac1{\delta_i}\log\frac{c_{i0}}{c_i^*},
\qquad p_1+p_2\le1.
\tag{D2}
\]

### Proposition D1: joint maintenance leaves an exact work frontier

The maximum cumulative nonmaintenance work executable by deadline `T` is

\[
\boxed{B(T)=T-p_1(T-t_1)_+-p_2(T-t_2)_+.}
\tag{D3}
\]

**Proof.** For either support, nonnegative maintenance and its floor imply

\[
c_i(t)\ge\max\{c_i^*,c_{i0}e^{-\delta_i t}\}.
\]

The integrated identity

\[
\alpha_i\int_0^T u_i(t)dt
=c_i(T)-c_{i0}+\delta_i\int_0^T c_i(t)dt
\]

therefore gives a minimum maintenance bill `p_i(T-t_i)_+`. It is attained by `u_i=0` before `t_i` and `u_i=p_i` afterward. The two minimizing schedules are jointly admissible because their total never exceeds `p_1+p_2<=1`. Subtracting their summed work from `T` proves (D3). ∎

This consumes inherited reserve before maintaining each support at its floor. It is optimal in the stated deterministic model, **not a robust reserve recommendation**. Shocks, protected reserve margins, repair delays, and construction decay change the calculation.

Two regimes follow exactly:

- If `s=1-p_1-p_2>0`, then after both reserves are used, `B(T)=sT+p_1t_1+p_2t_2`; recurring margin pays for additional work.
- If `p_1+p_2=1`, the lifetime nonmaintenance allowance is finite: `B(infinity)=p_1t_1+p_2t_2`. Both supports can remain functional forever while eventually no effort remains to use inquiry or establish anything else.

If initial capacities equal both floors and `p_1+p_2=1`, then `B(T)=0` for every `T`. Maintaining an inquiry apparatus is thus distinct from financing any inquiry through it.

Work-consuming jobs below are divisible and resumable, have no decay, and produce their feedback when their required work finishes. There are no extra calendar waiting times or rare-case arrival constraints. Under those assumptions, any sequential protocol whose realized work is at most `B(T)` can be executed on the maximizing work clock by `T`. This claim would not survive uncharged experimental delays or a change in the sampling distribution induced by the schedule.

## 3. Paid candidate production and fresh noisy validation

Each candidate costs `g>0` work to produce. It has a hidden quality label `G` or `D` with independent probability `theta` of `G`, where `0<theta<1`. A `G` candidate, once fully installed, meets the specified successor requirement; a `D` candidate does not. The label is available to the model analyst, not to the selecting process. The Bernoulli quality law is supplied; it does not explain a grammar, learning, creativity, neutral intermediates, or the source of useful forms.

For a frozen candidate, each fresh validation observation costs `v>0` work and is Bernoulli with probability `r_G` if the candidate is good and `r_D` otherwise, with

\[
0<r_D<r_G<1.
\tag{D4}
\]

Observations are independent conditional on candidate quality; candidate trials are independent across attempts. These are stipulated validation likelihoods, not a theorem that an arbitrary observed association is causal evidence. A real application must identify and validate its observation model, use appropriate interventions, and account for unsafe experimental outcomes.

A fixed batch protocol buys `n>=1` observations, then accepts when at least `k` are positive. Define its exact sensitivity and false-acceptance probability by binomial tails:

\[
a_{n,k}=\Pr\{\operatorname{Bin}(n,r_G)\ge k\},
\qquad
b_{n,k}=\Pr\{\operatorname{Bin}(n,r_D)\ge k\}.
\tag{D5}
\]

A rejected candidate is discarded and a fresh candidate may be attempted. A first accepted candidate stops inquiry and costs another `e>0` work to install. The installation bill includes the specified preparation and commissioning; actual permission must exist and cannot be created by assigning it a monetary equivalent. Current operation and inquiry remain above their floors through installation. Claims about the good successor's functioning afterward require the corresponding delivered initial conditions and operating model. A bad installation is separately counted, not certified as safe.

Records and computation needed for this finite protocol must remain available. The analysis prices each sample and assumes that price and the maintained inquiry interface suffice for its necessary retention and processing. It does not separately optimize archival compression or transmit beliefs across successors. Known likelihoods, public protocol, and trusted execution are declared boundary assumptions.

## 4. Exact timely-success and false-installation probabilities

Fix `n,k` and stop at the first acceptance. The maximum number of complete attempts that can be financed while reserving the installation bill is

\[
N=\max\left\{0,\left\lfloor\frac{B(T)-e}{g+nv}\right\rfloor\right\}.
\tag{D6}
\]

This is a capacity for attempts, not a guarantee that any candidate passes. Deliberately taking fewer attempts is permitted. Write

\[
A=\theta a_{n,k}+(1-\theta)b_{n,k}.
\]

For `N>=0` and `A>0`, the exact probabilities are

\[
\boxed{P_G=\frac{\theta a_{n,k}}{A}\bigl[1-(1-A)^N\bigr],}
\tag{D7}
\]

\[
\boxed{P_D=\frac{(1-\theta)b_{n,k}}{A}\bigl[1-(1-A)^N\bigr],
\quad P_{\varnothing}=(1-A)^N.}
\tag{D8}
\]

If `A=0`, there is no installation. **Proof:** the probability that attempt `j` is the first accepted good candidate is `(1-A)^(j-1) theta a`; sum this geometric series for `j=1,...,N`. The bad-candidate expression is identical with its corresponding probability, and the remaining event is `N` rejections. Every accepting branch can pay `e` because (D6) reserved it. ∎

The frontier is exact for this specified batch and stopping protocol. It is not an optimum over sequential tests, adaptive sample sizes, alternative candidate generators, parallel search, or all statistical procedures. A finite declared collection of `n,k,N` designs can be compared exactly: maximize `P_G` subject to `P_D<=epsilon` and the work constraint. Randomized selection between designs, if allowed, convexifies their attainable probability pairs.

It is essential to subtract `e` before financing the last possible attempt. A procedure can otherwise obtain evidence for a good candidate yet have no remaining work to establish it. Such an event counts as validation without installation, not successful succession.

More time alone does not make a fixed noisy first-acceptance rule arbitrarily reliable. If enough recurring work permits `N` to grow indefinitely, its limiting probability of a good installation is `theta a/A`, below one whenever bad acceptance has positive probability. More attempts also increase the probability of a bad installation. Reliability needs a changed validation policy, not merely more funding for the same fixed rule.

## 5. Exact numerical witness

Take `alpha_1=alpha_2=delta_1=delta_2=1`, both floors and initial capacities equal to `1/4`, and `T=24`. Then `p_1=p_2=1/4`, both reserve durations are zero, and `B(T)=T/2=12`. Both service and inquiry remain exactly at their floors under the work-maximizing allocation.

Let `g=v=1`, `e=4`, `theta=1/2`, `r_G=3/4`, and `r_D=1/4`.

| Protocol | Complete attempts N | Good installed | Bad installed | None installed |
|---|---:|---:|---:|---:|
| One observation, accept a positive | 4 | `45/64` = .703125 | `15/64` = .234375 | `1/16` = .0625 |
| Three observations, accept only three positives | 2 | `1539/4096` = .375732421875 | `57/4096` = .013916015625 | `625/1024` = .6103515625 |

For the second row, `a=27/64`, `b=1/64`, and `A=7/32`. It meets a .02 false-installation limit but has a substantially greater chance of no installation by the deadline. These are exact model probabilities, not simulation estimates or empirical frequencies. Neither row is asserted globally optimal.

With the same three-observation protocol, a work allowance of exactly four could finish one candidate's validation but cannot install it: `N=0` after the installation bill is correctly reserved. Its positive evidence, if produced without reserving installation work, would not eliminate the remaining physical cost.

## 6. A finite confidence guarantee with the full work bill

The fixed-test limit can be avoided with a paid, increasingly stringent protocol. This is an application of established fresh-testing and error-spending arguments already used in the earlier candidate-discovery work; the extension is charging its entire worst-case bill to (D3) while preserving both supports.

Suppose each fresh candidate has probability at least `theta_0>0` of being good, conditional on the past. Let a fixed validation threshold `h` satisfy `r_D<h<r_G`. Choose desired error allocation `0<epsilon<1` and set

\[
\epsilon_j=\frac{\epsilon}{j(j+1)}.
\]

For attempt `j`, choose the integer sample size

\[
n_j=\left\lceil\max\left\{
\frac{\log(1/\epsilon_j)}{2(h-r_D)^2},
\frac{\log 2}{2(r_G-h)^2}
\right\}\right\rceil.
\tag{D9}
\]

Accept when the sample mean is at least `h`. Fresh independent bounded-observation tails give conditional bad acceptance at most `epsilon_j` and good acceptance at least `1/2`. The union bound limits the chance of any bad installation through attempt `m` by `sum_{j<=m} epsilon_j < epsilon`.

At each reached attempt, conditional probability of a good acceptance is at least `theta_0/2`. Therefore the probability that all `m` attempts reject is at most `(1-theta_0/2)^m`. A first-acceptance protocol consequently satisfies

\[
\boxed{P_G\ge1-\epsilon-(1-\theta_0/2)^m}
\tag{D10}
\]

provided the deadline allows its complete worst-case bill:

\[
\boxed{B(T)\ge e+mg+v\sum_{j=1}^m n_j.}
\tag{D11}
\]

For a desired remaining miss allowance `eta`, take `m` large enough that `(1-theta_0/2)^m<=eta`; then true timely installation is at least `1-epsilon-eta`. These are sufficient, usually conservative bounds, not the exact best frontier. Negative right-hand sides in (D10) provide only the trivial lower bound zero.

This finite construction keeps its counters and memory requirements finite. Its work grows at order `m log(m/epsilon)` for fixed validation separation, rather than hiding increased confidence inside a costless oracle. Positive recurring margin makes every such finite work target eventually reachable **within the declared stable model**. At zero margin, the finite inherited allowance can prevent reaching it forever. No argument here supplies a positive candidate-quality bound, valid likelihoods, or stability against arbitrary future change.

## 7. Implications and scope

The coupled model exposes three different shortages:

1. The inquiry apparatus may cease to function because its own maintenance is unpaid.
2. The apparatus may remain available while all work is absorbed by maintaining the supports, leaving no effort for a test.
3. Discovery and validation may finish while the remaining work cannot install the candidate.

Success therefore cannot be diagnosed from proposal counts, accepted findings, apparatus survival, or present service alone. Each can rise while another indispensable stage fails.

The model also explicitly pays stages that have no current service return: candidate work and validation produce a possible route to later installation, not immediate incumbent output. That does not establish how useful routes containing neutral or harmful intermediates arise. Nor does it justify every speculative project. Choosing a program still needs a consequence model, acceptable trial risks, opportunity costs, and actual authority.

No cost is replenished by changing the organization's name. A repeated succession claim must show that each installed successor actually delivers the inquiry apparatus, operating support, future work supply, and retained information needed for the next cycle. The present calculation covers one deadline and one possible installation while preserving the incumbent and inquiry supports until that event. It does not give a free reset, an inherited-evidence model, or a complete recurrent innovation theory.

The defensible advance is narrow but useful: **the probability of reaching a validated, executable successor can be constrained jointly by maintenance, paid inquiry, statistical error, and installation, even when all parties share the same aim.** Candidate generation remains an independently specified mechanism that this stochastic reduction does not explain.
