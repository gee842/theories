# From the event law to joint capability tests

5 October 2026. AI-assisted formal continuation for Ren. This connects the [stochastic realization](STOCHASTIC-REALIZATION.md) to finite-horizon joint tests in the same process. It supplies a real, limited bridge in the [common specification](../../../../theories/becoming/chapters/FORMAL-SPECIFICATION.md). It does not introduce a favorable birth–death chain or assume nested capability levels.

## 1. The installed process and the assay

Use the existing event table, with material counts \((R,C,Y,D)\), usable-energy packets \(F\), and no extra production channel. Here letters denote counts rather than concentrations because \(V=1\). Set

\[
N=3,\quad V=\varepsilon=a=b=d=\beta=k=\ell=g=1,
\qquad x_0=(0,1,1,1,1).
\tag{1}
\]

A compatible incident source has \(\eta=1,I=3\). Compare supplied catalytic coefficients \(\theta=0\) and \(\theta=4\), keeping preparation and all other rates fixed. The second arrangement has an additional contribution to recycling through its existing \(Y\). Both recycling channels consume actual reserve packets. Identifying real catalysts and explaining how to construct or select the stronger coupling remain separate tasks. This is a parameter intervention between supplied arrangements, not a free physical conversion of one arrangement into the other.

The numerical specimen is weakly driven: its reduced work-equivalent drift is \(\mathcal LH=-F-Y\). It is not a test of sustained positive deterministic operation under ample support. This limitation matters to Ren's proposed support-conditional direction. The short-time comparison below extends separately to any fixed finite capture coefficient, but the numerical fixed-reliability crossing is reported only for (1).

Let \(J_H\) count completed \(D\to R\) recycling events, and \(B_H\) count completed \(R\to C\) assembly events. Let \(A_H=R_H+C_H+Y_H\). Define

\[
E_{j,b,f}(H)=
\{J_H\ge j,\ B_H\ge b,\ F_H\ge f,\ A_H\ge1\},
\quad(j,b,f)\in\{0,1\}^3.
\tag{2}
\]

Every test is joint. Event counts are delivered conversions, which can include repeated turnover; they are not claims about net growth of a structure. Remaining \(F\) is readiness for further work, not a second completed productive function. Because the all-degraded material face is absorbing for active material, \(A_H\ge1\) also ensures that activity has not vanished earlier. This protects continuation through this finite horizon, not every carrier or indefinite persistence.

The protocol is the actual autonomous run for \(H\). An analyst can define event counters without supplying those counters as information to a controller. There is no feedback controller, external optimizer, free actor readout or unpriced action in this calculation. Observing these tests experimentally would require an instrument and its effects to be specified.

For this singleton protocol class define the installed reliable region

\[
\mathcal C^{\rm run}_{H,\alpha}(x_0;\theta)
=\{(j,b,f)\in\{0,1\}^3:
\Pr_\theta(E_{j,b,f}(H))\ge\alpha\}.
\tag{3}
\]

This is an exact restricted capability region. For any larger implementable protocol class containing this run, it is an inner bound. Failure here does not prove that every possible controller fails. The probabilities are unconditional probabilities of jointly passing the tests; they are not normalized by survival.

## 2. Exact short-time conclusions

Write \(\lambda=1+\theta\). At (1), total recycling intensity is \(\lambda\). The only first events that remove the last reserve packet are leakage, intensity one, and recycling, intensity \(\lambda\). Thus

\[
\Pr_\theta(J_H\ge1,A_H\ge1)=\lambda H+O(H^2),
\tag{4}
\]

\[
\Pr_\theta(F_H\ge1,A_H\ge1)
=1-(2+\theta)H+O(H^2).
\tag{5}
\]

The activity condition changes neither first-order coefficient because at least two jumps are needed to lose both initial active structures. Increasing \(\theta\) from zero to four therefore improves one upward event and worsens another for sufficiently small positive \(H\). The joint delivery/readiness law, treating failed activity as a bottom outcome, is not stochastically ordered in either direction.

There is a positive joint construction result. Initial \(R=0\), so the only two-event path that both recycles and assembles is

\[
D+F\longrightarrow R,\qquad R\longrightarrow C.
\]

Its rate product at the two successive states is \(\lambda a\), giving

\[
\Pr_\theta(J_H\ge1,B_H\ge1,A_H\ge1)
=\frac{a\lambda}{2}H^2+O(H^3).
\tag{6}
\]

The same coefficient applies to the stronger endpoint test

\[
\Pr_\theta(C_H\ge2,Y_H\ge1,A_s\ge1\text{ for }0\le s\le H)
=\frac{a\lambda}{2}H^2+O(H^3).
\tag{7}
\]

This endpoint statement concerns an additional resident structure while retaining the other structure, rather than turnover alone. Conversely \(C_H\ge2\) and \(Y_H\ge2\) are jointly impossible at every time because \(N=3\), even though each target separately has a positive-probability construction path. Separately feasible components cannot be combined without a joint resource check.

For unit \(a\), requiring both conversions and retaining at least the initial one-packet reserve requires at least three events. The successful three-event orders are capture–recycle–assemble, recycle–capture–assemble, and recycle–assemble–capture. Their rate products are \(2\lambda,\lambda,2\lambda\), respectively. Hence

\[
\Pr_\theta(E_{1,1,1}(H))
=\frac{5\lambda}{6}H^3+O(H^4).
\tag{8}
\]

Thus a supported joint productive event can improve while a different readiness event worsens. No principle that identifies all useful changes with a single throughput rate follows.

**Finite-power extension.** Keep the same initial state and unit ordinary parameters but let \(g\ge0\) be any fixed finite capture coefficient, with the incident source changed consistently. Equations (4)–(7) retain their displayed leading coefficients: capture cannot by itself change whether an initially present packet remains above the one-packet threshold, and it is not on the minimal two-event construction path. Equation (8) instead has coefficient \(5g\lambda/6\). Consequently the short-time delivery/readiness non-dominance persists even with arbitrarily strong finite support, on a sufficiently short interval that can depend on \(g\). This is not a uniform-in-power time bound or a fixed-alpha region calculation for those other support values.

**Remainder justification.** The packet coordinate is unbounded, so a finite-state Taylor argument alone would be insufficient. After \(j\) jumps, \(F\le F_0+j\). For general fixed parameters, a valid upper bound on the total hazard is \(A+B(F_0+j)\), where

\[
A=(a+b+d)N+\beta N^2/V+gN/\varepsilon,
\qquad B=\ell+k\varepsilon N^2\max(1,\theta)/V^2.
\]

Integrating the first \(m\) jump-time densities over the ordered time simplex yields

\[
\Pr(N_H^{\rm jumps}\ge m)
\le\frac{H^m}{m!}
\prod_{j=0}^{m-1}[A+B(F_0+j)].
\tag{9}
\]

For each fixed jump count the finitely many reachable states also bound the waiting-time corrections. This proves the remainders in (4)–(8) at the displayed orders. The leading paths in (8) leave active material intact; activity protection does not alter that coefficient.

These local expansions establish delivery-law non-dominance. They alone do not establish incomparable regions at one fixed reliability, since the separating probability thresholds can differ. The following finite-time calculation supplies that stronger restricted comparison.

## 3. Certified probabilities from the same generator

Augment the original state with \(J\) and \(B\), each saturated at one. Saturation retains all information needed by (2). Bound energy by \(F\le K\) and send each would-be overflow to a distinguished absorbing state. All original rates remain unchanged until the first overflow. This is a comparison construction, not a physical rule that prohibits capture.

Let \(Q_K\) be the resulting finite generator and \(\Gamma\ge\max_x[-Q_K(x,x)]\). With \(P_K=I+Q_K/\Gamma\),

\[
e^{HQ_K}=\sum_{n=0}^\infty
e^{-\Gamma H}\frac{(\Gamma H)^n}{n!}P_K^n.
\tag{10}
\]

This standard uniformization method turns the transient calculation into nonnegative weighted sums. See the [PRISM methods documentation](https://www.prismmodelchecker.org/manual/Main/AllOnOnePage) under CTMC Transient Analysis for its established use in continuous-time model checking; the application here is the declared assay and its physical event law.

Let \(s_L\) be the partial sum for a success event, \(o_L\) the partial overflow mass, and \(\delta_L\) the remaining Poisson mass. Coupling the two processes until overflow gives

\[
s_L\le \Pr_\theta(E(H))\le s_L+o_L+\delta_L.
\tag{11}
\]

The upper bound permits every overflow path to succeed after leaving the truncated state space. This is valid even if such a path later returns. A separate a priori overflow bound is the tail probability of \(\operatorname{Poisson}((gN/\varepsilon)H)\) at \(K-F_0+1\); the computation uses the often tighter explicitly calculated overflow mass.

The [implementation and frozen protocol](../../../../experiments/shared-renewal-capability/PROTOCOL.md) use directed decimal rounding for every positive sum, product and quotient. Adjacent representable values enclose the correctly rounded exponential. The Poisson remainder is bounded by one minus its lower accumulated mass. Thus arithmetic, uniformization truncation, and energy overflow are included in the output intervals. The full [results](../../../../experiments/shared-renewal-capability/results.json) retain every declared case and profile.

## 4. A fixed-reliability incomparability witness

At the prespecified \(H=1/4\), \(\alpha=1/2\), all probabilities include the activity requirement. Conservative enclosing intervals from the calculation are:

| Joint test | \(\theta=0\) | \(\theta=4\) |
|---|---:|---:|
| At least one recycling event | [0.21061941, 0.21061942] | [0.65972017, 0.65972018] |
| At least one usable packet remains | [0.64610782, 0.64610784] | [0.34433159, 0.34433160] |
| Both recycling and resident assembly | [0.02409502, 0.02409504] | [0.08665191, 0.08665193] |
| Both conversions and one packet retained | [0.00668343, 0.00668345] | [0.02104555, 0.02104557] |

The complete reliable sets on the declared eight-profile vocabulary are

\[
\mathcal C^{\rm run}_{1/4,1/2}(x_0;0)
=\{(0,0,0),(0,0,1)\},
\]

\[
\mathcal C^{\rm run}_{1/4,1/2}(x_0;4)
=\{(0,0,0),(1,0,0)\}.
\tag{12}
\]

Each loses a profile supplied by the other. This is a certified incomparable pair for the installed process, at the same horizon and reliability, derived from its event law and joint ledger. The intervals are far from the decision threshold; the conclusion does not depend on last-digit numerical noise.

Horizon matters. At \(H=0.05\), the two restricted reliable sets are equal. At \(H=1\), the \(\theta=4\) set strictly includes the \(\theta=0\) set on this vocabulary. Those three observations do not establish a comparison at untested horizons, other profiles, other preparations, or under all possible controllers.

The [independent check and review](ASSAY-REVIEW.md) reconstructed the generator without importing the producer and compared all 48 declared probabilities. The maximum floating discrepancy from the reported intervals is 2.78e-15, below the disclosed 1e-11 checking tolerance. Exact integer checks also cover all 1,000 physical states at N=3, F<=24 across the two catalytic coefficients, including actual untruncated boundary events. These checks support implementation correctness; the floating comparison itself is not the rigorous enclosure. The directed-mean computation is valid for the six exact declared rate-times-horizon values, and needs extension for arbitrary inexact inputs.

## 5. What this closes and leaves open

The event law now supplies joint finite-horizon output/readiness probabilities, all derived directly from the same stochastic realization. This closes a concrete mechanism-to-assay calculation and a restricted directional comparison. It does not need the earlier phenomenological birth–death rates or an unjustified Markov projection onto a scalar level.

The result also rejects one tempting broad identification: increasing a shared recycling coefficient need not expand every reliable installed possibility at a fixed time. The theory must account for resource allocation, timing and readiness alongside material renewal. This does not refute every proposed universal direction or establish universal degeneration; it supplies a counterexample that any revised positive claim must retain.

The next substantive physical question is how an organization acquires and maintains effective regulation of that tradeoff. A controller that can freely suppress expensive reactions would change the protocol class and might preserve older profiles, but its existence, information, actuation, delay and costs cannot be assumed. A physical gating mechanism and its formation are the next obligations.

The completed [joint-formation contribution](JOINT-FORMATION-INTEGRATION.md) gives a complementary strategic result about acquiring and rebuilding concern and effective control. It supplies neither this chemical controller nor a theorem that such controllers are generally selected. Connecting those levels requires a physical and informational interface, not matching labels.

The positive universal objective remains unresolved. The new result is a checked part of its actual argument, with both productive gains and a consequential boundary made explicit.
