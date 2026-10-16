# A declared mesoscopic realization of shared renewal

AI-authored formal development, 5 October 2026, continuing Ren's supporting-condition research. This document supplies a stochastic model for the [shared renewal equations](../../../history/2026-10-05-support-and-shared-generativity/outputs/shared-generative-direction-mathematics.md), with an explicit event repertoire, accounting identities, and a scoped absorption theorem. It is a **declared mesoscopic realization, not an identified physical theory**. The event laws, packet size, reaction capabilities, and source are assumptions; they have not been derived uniquely from the deterministic drift or from fundamental physical laws.

The explanatory state includes material forms, their common usable-energy reserve, and their relation to incident support. No individual's fitness or welfare is taken as a substitute for this joint state.

## 1. State, parameters, and declared scale

Fix a volume or system-size parameter \(V>0\), a material concentration \(M>0\), and an integer \(N=VM\ge1\). Material counts satisfy

\[
n_R+n_C+n_Y+n_D=N.
\]

Let \(n_F\in\mathbb N_0\) count packets of usable energy, each assigned work value \(\varepsilon>0\). Define

\[
(R,C,Y,D)=\frac{(n_R,n_C,n_Y,n_D)}V,
\qquad E=\frac{\varepsilon n_F}{V}.
\tag{1}
\]

Thus a material event changes a concentration by \(1/V\); an energy-packet event changes \(E\) by \(\varepsilon/V\). The equality between one packet's value and the cost of recycling one material unit is a chosen granularity. It does not identify a molecular energy quantum. Initial energy need not be at equilibrium: any finite initial \(n_F\) is permitted. Approximating a macroscopic initial reserve uses a sequence with \(\varepsilon n_F^{(V)}(0)/V\to E(0)\), with integer rounding where necessary.

The quantities \(E,H,I\) are normalized by \(V\). If \(V\) is physical volume, \(I\) is incident power density: mean total incident energy over time \(t\) is \(IVt\), and its normalized value is \(It\). If \(V\) is an abstract system-size scale, use the same normalization consistently.

For the construction and absorption proof assume finite parameters

\[
a,b,d,\ell,\varepsilon>0,\quad
\beta,k,\theta\ge0,\quad
0\le\eta\le1,\quad 0\le I<\infty,
\qquad g=\frac{\eta I}{M}<\infty.
\tag{2}
\]

The original deterministic example has positive \(\beta,k\); allowing their zero values here causes no difficulty. Positive wear rates \(b,d\), positive assembly rate \(a\), and positive reserve leakage \(\ell\) are substantive premises of the absorption theorem. The energy state space is unbounded even though \(N\) is finite.

## 2. Event table

The process is a continuous-time Markov chain with the following state-dependent propensities. Catalysts shown on both sides are unchanged by the event.

| Event | Count update | Propensity |
|---|---|---|
| \(R\to C\) | \(n_R-1,\ n_C+1\) | \(a n_R\) |
| \(C\to D\) | \(n_C-1,\ n_D+1\) | \(b n_C\) |
| \(R+Y\to2Y\) | \(n_R-1,\ n_Y+1\) | \(\beta n_Rn_Y/V\) |
| \(Y\to D\) | \(n_Y-1,\ n_D+1\) | \(d n_Y\) |
| Capture into the reserve | \(n_F+1\) | \(g n_C/\varepsilon\) |
| Reserve leakage | \(n_F-1\) | \(\ell n_F\) |
| \(D+F+C\to R+C\) | \(n_D-1,\ n_R+1,\ n_F-1\) | \(k\varepsilon n_Fn_Dn_C/V^2\) |
| \(D+F+Y\to R+Y\) | Same update | \(k\varepsilon\theta n_Fn_Dn_Y/V^2\) |

Every propensity vanishes when a required reactant is absent. Recycling consumes an available packet and cannot overdraw the reserve. All events preserve total material. The two recycling channels have the same state increment but different catalytic propensities; retaining their labels records which available pathway contributed.

One graphical construction also makes incident support explicit. Let incident packet arrivals be Poisson with rate \(IV/\varepsilon\). Accept each arrival into the reserve with probability \(\eta n_C/N\), using an independent uniform mark conditional on the current state. This gives capture intensity

\[
\frac{IV}{\varepsilon}\frac{\eta n_C}{N}
=\frac{g n_C}{\varepsilon}.
\]

Rejected arrivals do not enter the modeled reserve. Captured energy is pathwise a subset of realized incident energy. The deterministic quantity \(It\) is its mean input scale, not a hard bound on the fluctuating incident energy in every time interval. Poisson arrival statistics and the capture probability are declared assumptions, not consequences of specifying mean illumination.

## 3. Exact accounting and deterministic scaling

Let \(K_{\mathrm{cap}},K_{\mathrm{leak}},K_{C\mathrm{wear}},K_{Y\mathrm{wear}}\) count the indicated events after time zero. For

\[
H=E+\varepsilon(R+C+Y)
=\frac{\varepsilon}{V}(n_F+n_R+n_C+n_Y),
\]

the pathwise identity is

\[
H(t)-H(0)=\frac{\varepsilon}{V}
\left[K_{\mathrm{cap}}(t)-K_{\mathrm{leak}}(t)
-K_{C\mathrm{wear}}(t)-K_{Y\mathrm{wear}}(t)\right].
\tag{3}
\]

Assembly merely transfers active material. Recycling exchanges one reserve packet for one usable material unit, leaving this reduced work-equivalent quantity unchanged. Its conditional infinitesimal drift is therefore

\[
\mathcal L_VH=gC-\ell E-\varepsilon(bC+dY).
\tag{4}
\]

Writing \(J=kED(C+\theta Y)\), the five concentration coordinate drifts are exactly

\[
\begin{aligned}
\mathcal L_VR&=J-aR-\beta RY,&
\mathcal L_VC&=aR-bC,\\
\mathcal L_VY&=\beta RY-dY,&
\mathcal L_VD&=bC+dY-J,\\
\mathcal L_VE&=gC-\ell E-\varepsilon J.
\end{aligned}
\tag{5}
\]

These are the previously specified differential-equation vector field evaluated at the random present state. They do not give closed equations for the mean concentrations: for example, \(\mathbb E[ECD]\) generally differs from \(\mathbb E[E]\mathbb E[C]\mathbb E[D]\).

More formally, with concentration increments \(\nu_j/V\), including energy entries \(\pm\varepsilon/V\), the generator has the density-dependent form

\[
\mathcal L_V f(x)
=V\sum_j\alpha_j(x)\left[f(x+\nu_j/V)-f(x)\right].
\tag{6}
\]

The coordinate drift is \(\sum_j\nu_j\alpha_j(x)\). The chosen events also specify a local fluctuation covariance \(V^{-1}\sum_j\alpha_j(x)\nu_j\nu_j^{\mathsf T}\). A different microscopic event decomposition can preserve the drift while changing this covariance and rare-transition probabilities.

Along a sequence \(V\to\infty\) with \(VM\) integral, fixed parameters, and initial concentrations converging to a finite deterministic state, the density-dependent law-of-large-numbers framework gives convergence in probability to the differential-equation trajectory on each fixed finite time interval. Polynomial rate functions are locally Lipschitz; material boundedness and the bounded-rate incoming packet construction provide the needed finite-horizon control of the energy coordinate. This is a finite-horizon limit. It is not a theorem exchanging \(V\to\infty\) with \(t\to\infty\), nor a claim of uniform accuracy for extinction times or near a separatrix.

## 4. Nonexplosion and boundary behavior

Capture has the uniform upper bound

\[
\Lambda=\frac{gN}{\varepsilon}
=\frac{\eta IV}{\varepsilon}<\infty.
\]

Construct candidate captures using a Poisson process of rate \(\Lambda\), accepting a candidate with probability \(n_C/N\). This is equivalent to the preceding two-stage thinning of incident arrivals. On each finite interval,

\[
n_F(t)\le n_F(0)+K_{\mathrm{candidate}}(t).
\]

The right side is almost surely finite. All material counts are bounded by \(N\); leakage and recycling rates are bounded by a fixed multiple of \(n_F\), and remaining rates are bounded constants. Thus the total event intensity is bounded on each finite interval by an almost surely finite random constant. The process is nonexplosive.

The face \(n_Y=0\) is invariant. A new \(Y\) process requires a seed or a new formation event. A single founder as \(V\to\infty\) has vanishing initial concentration; it is a different scaling from a fixed positive seed concentration. Establishment probabilities and times growing with \(V\) require additional analysis.

The **all-degraded material face** is

\[
n_R=n_C=n_Y=0,\qquad n_D=N,
\]

with arbitrary \(n_F\ge0\). It is invariant, but its positive-energy states are not absorbing: remaining packets leak at rate \(\ell n_F\). The single final absorbing state is

\[
z_\dagger=(n_R,n_C,n_Y,n_D,n_F)=(0,0,0,N,0).
\tag{7}
\]

Once the material face is reached, finitely many packets disappear by a pure-death process in finite time almost surely. In contrast, absence of \(C\) alone need not be permanent when \(R>0\), because the supplied assembly event \(R\to C\) remains available.

## 5. Almost-sure absorption for finite material count

**Theorem.** Under (2), for fixed finite \(N\) and any finite initial packet count, the process reaches \(z_\dagger\) in finite time almost surely. No bound on the expected lifetime or useful lifetime scale is asserted here.

The proof cannot use a finite-state-chain argument: \(n_F\) is unbounded. We instead give a domination and repeated-trial argument.

**Energy domination.** Let \(U\) receive every candidate capture at rate \(\Lambda\), and let each of its packets have an independent exponential lifetime with rate \(\ell\). Start with \(U(0)=n_F(0)\). Maintain the actual reserve packets as a subset of these labeled dominating packets. An accepted candidate adds the same packet to both processes; a rejected candidate adds it only to \(U\). The inherited packet lifetimes implement actual leakage at rate \(\ell n_F\). Recycling removes the selected packet from the actual reserve but leaves its dominating counterpart until its independent leakage time. Thus

\[
n_F(t)\le U(t)\quad\text{for all }t.
\]

The marginal process \(U\) is the immigration–death chain with arrival rate \(\Lambda\) and departure rate \(\ell u\) at state \(u\). For \(\Lambda>0\) it is irreducible and has normalized stationary law

\[
\varpi_u=e^{-\Lambda/\ell}
\frac{(\Lambda/\ell)^u}{u!},
\]

as verified by \(\varpi_u\Lambda=\varpi_{u+1}\ell(u+1)\). Consequently it is positive recurrent and visits zero infinitely often almost surely from any finite initial state. If \(\Lambda=0\), it is a pure-death process that reaches zero in finite time almost surely and remains there.

**A uniform positive-probability trial.** Let

\[
B=(a+b+d)N+\frac{\beta N^2}{V}>0,
\quad r_0=\min(a,b,d)>0,
\quad \Delta=\frac{1}{2B},
\quad T=2N\Delta.
\]

Whenever \(U=0\), the actual reserve is empty. Consider the next interval of duration \(T\). The event of no candidate capture has probability \(e^{-\Lambda T}\). Conditional on that event, neither capture nor recycling can occur, and the total material-event rate is at most \(B\).

From any material configuration, choose the finite sequence: assemble every remaining \(R\) into \(C\), then let every \(C\) wear into \(D\), then let every \(Y\) wear into \(D\), without \(Y\)-assembly events. It requires at most \(2N\) events. Whenever its next required event exists, its rate is at least \(r_0\). In a slot of duration \(\Delta\), the probability of exactly that event and no other material event is at least

\[
r_0\Delta e^{-B\Delta}.
\]

This follows by integrating its jump density over the slot and using the upper bound \(B\) for total hazards before and after the jump. If the sequence finishes early, the state is already absorbing while candidate captures remain excluded. Since \(r_0\Delta\le1/2\), a uniform lower bound for completing the whole trial is

\[
p=e^{-\Lambda T}
\left(r_0\Delta e^{-B\Delta}\right)^{2N}>0.
\tag{8}
\]

This lower bound is deliberately loose and is not a quantitative lifetime estimate.

**Stopping times and repetition.** Set

\[
\tau_1=\inf\{t\ge0:U(t)=0\},\qquad
\tau_{j+1}=\inf\{t\ge\tau_j+T:U(t)=0\}.
\]

All these stopping times are finite almost surely by the preceding recurrence or pure-death result. Their trial windows do not overlap. The joint graphical construction and the strong Markov property give, conditionally on the full history through \(\tau_j\), a probability at least \(p\) of reaching \(z_\dagger\) by \(\tau_j+T\), whenever absorption has not already occurred. Independence of different trials is not required. Iterated conditional probabilities give

\[
\Pr(\text{no absorption after the first }j\text{ trials})
\le(1-p)^j\longrightarrow0.
\]

A successful finite-numbered trial finishes at a finite time. This proves the theorem.

Finite \(N\), bounded candidate capture, and positive leakage are used essentially in this proof. Vanishing wear, immigration of active material, independent powered creation of usable material, a new \(Y\) nucleation route, or other changes require a new analysis. The theorem describes this repertoire, not the fate of every illuminated physical system.

## 6. What remains unidentified

The packet process supplies a well-defined law once its parameters, scale, and event assumptions are fixed. It has not been identified from molecular observations. In particular:

- Packet size, incoming statistics, reaction waiting-time assumptions, and hidden intermediate states determine noise and rare transitions. The deterministic vector field does not uniquely determine them.
- The event repertoire supplies assembly, capture, and catalytic capabilities. It does not derive those capabilities, their origin, or the underlying physical laws. The usable form \(R\) is already suitable for the stipulated assembly events.
- A thermodynamic realization still needs material identities, reaction free energies, a source and receiving environment, and appropriate reverse pathways or justified irreversible limits. Equation (3) is bookkeeping; it does not establish local detailed balance or calculate entropy production.
- At fixed finite \(N\), the only long-run stationary law is concentrated at \(z_\dagger\). A long-lived active transient or a distribution conditioned on continued activity is a different object. Its existence, accuracy, and lifetime scales have not been calculated here.
- The positive restart rate in the earlier finite birth–death illustration cannot be obtained from this event table: its empty active-material face has no restart event. A physical restart mechanism would have to be specified and paid for.
- Capacity assays still require executable protocols, horizons, protected supports, and declared stochastic success criteria. Projecting this process onto a capacity level does not automatically give a Markov chain; omitted reserves, material composition, or source phase can retain consequential memory.

No universal directional conclusion follows. The positive catalytic contribution of \(Y\) is stipulated, and the earlier invasion condition does not require that contribution. Even after choosing this stochastic law, favorable transition ratios or stochastic dominance of capacity distributions remain results to prove for specified comparisons. The finite-system absorption theorem is an explicit obstruction to treating deterministic coexistence as eternal persistence or as a universal stationary direction toward 善.

## Sources and relation to the existing study

- [Shared generative direction: mathematical companion](../../../history/2026-10-05-support-and-shared-generativity/outputs/shared-generative-direction-mathematics.md): the deterministic \(R,C,Y,D,E\) equations, their work-equivalent identity, invasion and coexistence results, capacity inclusion tests, and the separate conditional birth–death theorem.
- [Shared generative direction: research report](../../../history/2026-10-05-support-and-shared-generativity/outputs/shared-generative-direction.md): the proposed direction, mechanism, and remaining reduction obligations.
- [Renewing access to support: mathematical companion](../../../history/2026-10-05-support-and-shared-generativity/outputs/renewing-access-to-support-mathematics.md): the preceding endogenous-capture construction and inaccessible material boundary.
- [Study index](../../../history/2026-10-05-support-and-shared-generativity/README.md): retained reports, verification artifacts, and source genealogy.

This document adds a declared event realization and the scoped proof above. It records no empirical experiment, calibrated physical parameters, or completed derivation of capability-level transition rates.
