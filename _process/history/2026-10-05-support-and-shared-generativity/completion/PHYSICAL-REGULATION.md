# Constructed physical regulation of shared renewal

5 October 2026. AI-assisted formal development for Ren. This extends the same [mesoscopic renewal process](STOCHASTIC-REALIZATION.md) with explicit regulator material, fuel binding, inhibition, wear, and reconstruction. It supplies a physical reaction model rather than a controller granted instantaneous access to the global reserve. Its reaction repertoire and rate constants remain supplied assumptions. This document proves accounting and scoped structural results; it does not claim a favorable numerical outcome.

The [prospective experiment protocol](../../../../experiments/shared-renewal-capability/regulation/PROTOCOL.md) fixes the five comparison arms and numerical cases. The separate [formation-lag result](REGULATION-LAG.md) sharpens the short-time comparison. Shared specifications and indexes are not edited by this note.

## 1. State, source, and what begins absent

Use count state

\[
x=(R,C,Y,D,F,G,GF,YG),\qquad
x_0=(0,1,1,1,1,0,0,0).
\tag{1}
\]

Here \(G\) is a free inhibitor, \(GF\) is an inhibitor holding one fuel packet, and \(YG\) is a complex containing one \(Y\) and one inhibitor. Complex names denote single count coordinates, not multiplication. A propensity written \(\alpha_b G F\) does denote the product of the free counts. The symbol \(\alpha_b\) below is the protocol's fuel-association parameter `alpha`; assay reliability is written separately as \(\alpha_{\rm test}\).

Free \(G\) can bind \(Y\), disabling that constituent's recycling function. Fuel binding competes for \(G\), leaving more \(Y\) available under suitable conditions. These encounters occur at finite mass-action rates. The mechanism neither reads a globally supplied reserve value nor changes an externally selected policy. Its local molecules interact with fuel and catalyst molecules.

All regulator forms begin absent. Formation converts existing usable material and one actual packet into a regulator. The possible fabrication reaction and binding chemistry are specified in advance; their evolutionary origin or selection is not thereby explained.

For all calculations here \(V=\varepsilon=1\), total material is three, and the original rates satisfy \(a=b=\beta=d=k=\ell=1\), with recycling amplification \(\theta=4\). Compare capture parameters \(g=4\) and \(g=8\) separately. With \(\eta=1\) and \(M=N=3\), compatible incident packet rates are \(I=gN=12\) and 24. Within each source condition, all arms have the same source and initial stocks. These sources differ from the earlier \(g=1\) assay; improvement here would not show that regulation rescues that earlier preparation under its original support.

## 2. Complete event repertoire

All propensities below are evaluated at the current count state. A reaction is disabled when any consumed input is absent. Let \(\delta\) be the wear rate per regulator, \(\rho\) the fuel dissociation rate, \(\mu\) the inhibitor association rate, and \(\nu\) the inhibitor dissociation rate. Bound fuel leaks at \(\ell_b=\ell\).

| Event | Propensity | Change of work-equivalent \(W\) defined below |
|---|---:|---:|
| \(R\to C\) | \(aR\) | 0 |
| \(C\to D\) | \(bC\) | −1 |
| \(R+Y\to2Y\) | \(\beta RY\) | 0 |
| \(R+YG\to Y+YG\) | \(\beta R\,YG\) | 0 |
| \(Y\to D\) | \(dY\) | −1 |
| Capture: \(F\to F+1\) | \(gC\) | +1 |
| Free fuel leakage: \(F\to F-1\) | \(\ell F\) | −1 |
| \(D+F+C\to R+C\) | \(kFDC\) | 0 |
| \(D+F+Y\to R+Y\) | \(k\theta FDY\) | 0 |
| Construction: \(R+F\to G\) | \(\kappa RF\) | −1 |
| \(G\to D\) | \(\delta G\) | −1 |
| \(G+F\to GF\) | \(\alpha_b G F\) | 0 |
| \(GF\to G+F\) | \(\rho GF\) | 0 |
| Bound fuel leakage: \(GF\to G\) | \(\ell_b GF\) | −1 |
| Bound regulator wear: \(GF\to D+F\) | \(\delta GF\) | −1 |
| \(G+Y\to YG\) | \(\mu GY\) | 0 |
| \(YG\to G+Y\) | \(\nu YG\) | 0 |
| Regulator wear in \(YG\): \(YG\to Y+D\) | \(\delta YG\) | −1 |
| \(Y\) wear in \(YG\): \(YG\to G+D\) | \(dYG\) | −1 |

There is no recycling catalyzed by \(YG\). Bound \(Y\) retains its assembly function and its original per-constituent wear rate. Its daughter is free \(Y\). These explicit reactions prevent inhibition from secretly changing reproduction or making \(Y\) immune to wear. Each regulator constituent likewise wears at rate \(\delta\) whether free, fuel-bound, or catalyst-bound. The two constituents of \(YG\) can wear independently.

Bound-regulator wear releases its already-held packet; it does not create a new packet. Bound fuel has the same leakage rate as free fuel, so the binding state is not granted an additional storage-longevity advantage. Dissociation can still delay availability, and binding can change which reactions can consume the packet.

## 3. Exact material and fuel ledgers

The invariant material count, total packet inventory, total regulator count, and total \(Y\) count are

\[
N=R+C+Y+D+G+GF+2YG=3,
\]

\[
U=F+GF,\qquad T=G+GF+YG,\qquad L=Y+YG.
\tag{2}
\]

\(GF\) contains one material unit and one packet; \(YG\) contains two material units. Define the reduced work-equivalent quantity

\[
\boxed{W=N-D+U=F+R+C+Y+G+2GF+2YG.}
\tag{3}
\]

Thus **both \(GF\) and \(YG\) count twice in \(W\)**, for different reasons. Construction exchanges one usable structural unit and one packet for one regulator, dissipating one assigned work unit. Binding moves material or fuel between explicit states and has zero increment in this reduced ledger.

Let \(K_{\rm cap},K_{\rm leak},K_{\rm ble\!ak},K_{\rm rec},K_{\rm build}\) count capture, free leakage, bound leakage, recycling through either catalyst, and every construction after time zero. Let \(K_{Cw}\) count \(C\) wear; \(K_{Yw}\) include both free and bound \(Y\) wear; and \(K_{Gw}\) include regulator wear in all three regulator states. Pathwise,

\[
\boxed{U_t-U_0=K_{\rm cap}-K_{\rm leak}-K_{\rm ble\!ak}
-K_{\rm rec}-K_{\rm build}.}
\tag{4}
\]

\[
D_t-D_0=K_{Cw}+K_{Yw}+K_{Gw}-K_{\rm rec},
\]

\[
\boxed{W_t-W_0=K_{\rm cap}-K_{\rm leak}-K_{\rm ble\!ak}
-K_{\rm build}-K_{Cw}-K_{Yw}-K_{Gw}.}
\tag{5}
\]

Also \(T_t-T_0=K_{\rm build}-K_{Gw}\). Every reconstruction therefore draws on actual usable material and a packet at its event time. No repair is booked as an unpriced future promise. In particular,

\[
K_{\rm build}+K_{\rm rec}\le U_0+K_{\rm cap}.
\tag{6}
\]

For the recycling intensity \(J=kFD(C+\theta Y)\) and construction intensity \(K=\kappa RF\), the exact conditional drifts include

\[
\mathcal LU=gC-\ell F-\ell_b GF-J-K,
\]

\[
\mathcal LT=K-\delta T,\qquad
\mathcal LL=\beta RL-dL,
\]

\[
\mathcal LW=gC-\ell F-\ell_b GF-K-bC-dL-\delta T.
\tag{7}
\]

These are generator identities at the current state, not closed equations for expectations of products.

The protected plant quantity is

\[
\boxed{A=R+C+Y+YG.}
\tag{8}
\]

It excludes free or fuel-bound regulator material. In particular, \(G\)-only persistence does not count as continuing productive activity. Its drift is

\[
\mathcal LA=J-bC-dL-K.
\tag{9}
\]

Construction competes directly with plant material before any benefit of inhibition is obtained. The free-reserve assay still tests \(F_H\), not \(U_H\). A packet held in \(GF\) is not immediately available to the original productive reactions. Its recoverability can be assessed by an additional timed protocol, but must not be credited as free instantaneous access.

## 4. Exact finite-copy binding-sign theorem

This is a diagnostic of the supplied binding mechanism, separate from the full production experiment. Isolate the reversible binding subsystem: pause construction, wear, production, capture, and leakage, fix total regulator \(T=t\) and total \(Y\) count \(L=l\), and externally clamp free-fuel activity at \(f\). This last condition is a calibration boundary condition, not an assumption that the production process has a free fuel reservoir.

Write \(u=GF\), \(v=YG\), so free regulator is \(t-u-v\) and free \(Y\) is \(l-v\). For positive dissociation rates, the transitions are

\[
(u,v)\to(u+1,v):\ \alpha_b f(t-u-v),\qquad
(u,v)\to(u-1,v):\ \rho u,
\]

\[
(u,v)\to(u,v+1):\ \mu(t-u-v)(l-v),\qquad
(u,v)\to(u,v-1):\ \nu v.
\tag{10}
\]

Let \(K_F=\alpha_b/\rho\), \(K_Y=\mu/\nu\), and \((l)_v=l!/(l-v)!\). For \(0\le v\le\min(t,l)\), the stationary marginal satisfies

\[
\boxed{\pi_f(v)\propto
\binom{t}{v}(l)_v
\left[\frac{K_Y}{1+K_Ff}\right]^v.}
\tag{11}
\]

**Theorem.** Increasing \(f\) makes bound \(YG\) stochastically smaller and free \(Y=l-YG\) stochastically larger in this finite binding assay. No deterministic or large-copy approximation is required.

**Proof.** A joint stationary weight is

\[
w_f(u,v)=
\frac{t!}{(t-u-v)!u!v!}(l)_v(K_Ff)^uK_Y^v.
\]

The ratios along the two edges in (10) are respectively

\[
\frac{w_f(u+1,v)}{w_f(u,v)}
=\frac{K_Ff(t-u-v)}{u+1},
\qquad
\frac{w_f(u,v+1)}{w_f(u,v)}
=\frac{K_Y(t-u-v)(l-v)}{v+1}.
\]

They equal the corresponding forward/reverse rate ratios, proving detailed balance on the finite binding state space. Summing over \(u\) gives a factor \((1+K_Ff)^{t-v}\), which yields (11) after removing the common factor \((1+K_Ff)^t\).

For \(f_2>f_1\), the ratio \(\pi_{f_2}(v)/\pi_{f_1}(v)\) is proportional to a nonincreasing geometric factor in \(v\). Consequently its covariance with every increasing function of \(v\), under \(\pi_{f_1}\), is nonpositive. Since this density ratio has expectation one, every such function has no larger expectation under \(\pi_{f_2}\). This proves the stated stochastic order. Degenerate zero-association cases follow on their accessible supports by continuity; if fuel cannot bind, there is no fuel-dependent shift. ∎

If bound-fuel leakage is retained in the diagnostic while formation and wear remain paused and free fuel is still clamped, the same occupancy calculation uses \(K_F=\alpha_b/(\rho+\ell_b)\). It must then be described as an occupancy balance: the fuel-binding/leakage cycle dissipates packets, so thermodynamic equilibrium has not been established by a reversible-looking marginal chain.

In the actual experiment, \(F,T,L\) change, packets become sequestered, all binding transitions take time, and bound constituents can wear. Equation (11) is not substituted for these reactions. The theorem establishes a response sign under its diagnostic conditions; it neither proves accurate instantaneous sensing nor guarantees a net productive advantage in the coupled process.

## 5. Formation, lag, and recurrence are different claims

With \(\kappa=0\) and the preparation (1), all regulator forms remain absent. With \(\kappa>0\), a positive-probability formation route exists, but its inputs must first become jointly available. Initial \(R=0\), and the initial packet is consumed by the first recycling event. A first construction therefore requires at least three jumps. The leading successful orders are capture–recycle–construction and recycle–capture–construction.

Under the stated unit original rates, write \(\lambda=1+\theta\). The two rate products are \(2g\lambda\kappa\) and \(g\lambda\kappa\), giving

\[
\Pr(\text{at least one construction by }H)
=\frac{\kappa g\lambda}{2}H^3+O(H^4).
\tag{12}
\]

A subsequent inhibitor-binding event is required before \(YG\) appears. In particular, the regulator does not alter the initial first-order competition for fuel. The [lag analysis](REGULATION-LAG.md) provides the corresponding coupling and comparison bounds. Formation from zero is not equivalent to being available from time zero.

Reconstruction is an actual option of the same reaction law after wear, subject to available \(R,F\). Its rate is not prescribed to guarantee that a regulator survives or is replaced before a needed intervention. The exact accounting makes recurrence testable; it does not prove recurrence indefinitely.

## 6. Nonexplosion and finite-system absorption

**Nonexplosion.** Material conservation bounds every material and complex count. Total packet inventory is bounded pathwise by

\[
U_t\le U_0+K_{\rm candidate}(t),
\]

where candidate captures form a Poisson process of finite rate \(\Lambda=gN\), with actual captures accepted at probability \(C/N\). Binding and dissociation preserve \(U\); construction, recycling, and leakage only decrease it. Every propensity is therefore bounded on a finite interval by a constant plus a constant times this almost surely finite packet bound. The process is nonexplosive.

**Absorption theorem.** For finite \(N\), finite source and rate constants, positive free and bound leakage, positive \(a,b,d,\delta\), and the declared repertoire, the process reaches all material in \(D\) with no fuel in finite time almost surely. This is not a claim about its expected lifetime or useful performance horizon.

**Proof.** Use an immigration–death process \(\overline U\) with immigration \(\Lambda\) and per-packet death \(\ell_*:=\min(\ell,\ell_b)>0\). Track the actual free and bound packets as a subset of its labeled packets. Binding changes a packet's location but not its baseline leakage clock; additional leakage, construction, and recycling only remove actual packets sooner. Regulator wear in \(GF\) moves its packet back to the free pool. Thus \(U\le\overline U\) pathwise. The dominating process returns to zero infinitely often, or stays at zero when its immigration is zero.

Whenever \(\overline U=0\), actual \(F=GF=0\). On an interval with no candidate capture, construction, recycling, and fuel binding cannot occur. There is then a finite material-only route to all-\(D\): assemble every remaining \(R\) into \(C\), wear all \(C\), and wear all free or bound \(Y\) and regulator constituents. A \(YG\) complex requires two constituent-wear events. At most \(2N\) selected events suffice. Competing reproduction and inhibitor-binding events have bounded rates and can be excluded with positive probability.

For example, a uniform material-event hazard bound on this zero-fuel interval is

\[
B=(a+b+d+\delta+\nu)N+(\beta+\mu)N^2.
\]

Take \(r_*=\min(a,b,d,\delta)>0\), \(\Delta=1/(2B)\), and \(T_*=2N\Delta\). In each needed slot the probability of the selected event and no other material event is at least \(r_*\Delta e^{-B\Delta}\). Requiring no candidate capture gives the uniform trial success bound

\[
p=e^{-\Lambda T_*}
\left(r_*\Delta e^{-B\Delta}\right)^{2N}>0.
\]

Choose successive zero visits of \(\overline U\) separated by these trial windows. The strong Markov property makes the conditional failure probability after \(m\) trials at most \((1-p)^m\). A successful finite-numbered trial finishes at a finite time almost surely. ∎

The protected face \(A=0\) is invariant: it has no \(R,C,Y,YG\), hence no capture, plant assembly, or recycling. Regulator material and bound fuel cannot create plant material through the stated repertoire. Positive wear and leakage eventually remove them as well. Adding independent nucleation, plant immigration, zero wear, or a fuel-protected state changes these hypotheses and requires a new proof. The present gate can improve some finite-horizon outcomes without making indefinite persistence possible.

## 7. Fixed five-arm comparison

All arms use \(\delta=\rho=\nu=\ell_b=1\), with the original rates and preparation specified above. Each is evaluated at \(g=4,8\) and \(H=0.25,1,3\).

| Arm | \(\kappa\) | \(\alpha_b\) | \(\mu\) | Role |
|---|---:|---:|---:|---|
| absent | 0 | 0 | 0 | Original process at the same source |
| burden | 1 | 0 | 0 | Constructed inert material burden |
| buffer | 1 | 4 | 0 | Fuel binding without inhibition |
| inhibitor | 1 | 0 | 4 | Constant inhibition without fuel binding |
| responsive | 1 | 4 | 4 | Fuel-responsive inhibition |

Constructed arms share unit construction, leakage, and wear costs. Their realized construction counts, delays, captured inputs, and losses remain outcomes; equal rate constants do not mean equal pathwise expenditure. The factorial arms distinguish fuel buffering, catalytic inhibition, and the interaction between them. Comparing only the responsive arm with an absent regulator would leave those explanations mixed together.

Primary assays retain the eight profiles \((j,b,f)\in\{0,1\}^3\): completed recycling count at least \(j\), completed \(R\to C\) assembly count at least \(b\), **free** reserve \(F_H\ge f\), and \(A_H\ge1\). Reliability is \(\alpha_{\rm test}=0.5\). Secondary readouts distinguish whether any construction occurred and whether intact regulator material remains. None of these definitions labels persistent regulator material as success by itself.

The generator calculation and its numerical error status belong to the prospective experiment and its results. This note makes no prediction that the responsive arm wins, includes the reliable regions of other arms, or optimizes all protected functions. The autonomous run remains a singleton protocol class rather than the set of all physically realizable controllers.

## 8. Physical and interpretive limits

The model closes a concrete accounting gap: a regulatory relation can form from absent regulator material, consume resources, bind a local fuel signal, alter a catalytic reaction, wear, and be rebuilt through the same coupled process. The conditional binding theorem supplies the intended response sign. Whether that relation improves the original joint tests after all costs is a separate calculation.

Binding affinities, component identities, reaction free energies, source/sink coupling, and reverse pathways remain to be physically identified. Zero change in \(W\) does not mean that binding exchanges no heat or has zero Gibbs free-energy change. This ledger is a declared work-equivalent bookkeeping model, not a thermodynamic identification or entropy-production proof. Likewise, passive occupancy does not require inventing a fresh fuel debit for every association event; resource costs must come from the actual mechanism. The [primary push–pull sensing analysis of Govern and ten Wolde](https://pmc.ncbi.nlm.nih.gov/articles/PMC4267345/) concerns time-integrated biochemical readout with specified receptor, readout, and fuel resources. Its cost bounds are not universal per-event charges for the passive binding subsystem used here.

Neither physically possible construction nor a favorable assay would establish spontaneous discovery of the reaction repertoire, evolutionary selection of the architecture, normative correctness, or a universal direction toward 善. A failed comparison would likewise not disprove regulation in general. The result to retain is the exact mechanism, its paid interfaces, its measured joint consequences, and the conditions under which its advantages or failures occur.
