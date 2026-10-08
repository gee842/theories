# Physical repair, succession and return after renewed capture

5 October 2026. AI-assisted continuation from repository commit `348d826`, using the same paid allocation network with \(\zeta=0\). This extends [Allocation control](ALLOCATION-CONTROL.md) beyond its first-capture result. No reaction, initial preparation or frozen experiment is changed.

**Results.** The autonomous network admits exact return paths that rebuild C, replace G, and let a daughter Y replace its parent while recovering the same material/fuel state. A combined turnover uses the minimum four captured packets allowed by the declared ledger. Lower bound probabilities compose uniformly at the actual return state. The changed allocation gate also improves a damage-conditioned repair kernel by blocking a reaction that irreversibly destroys repair access. These results coexist with a severe repair bound: at the earlier numerical witness, after C wears in the specified one-packet state, the probability of *any* return is at most \(1/72\).

Positive return paths and a conditional comparison do not establish reliable indefinite renewal, nor do they transfer the earlier paid first-hit advantage to unrestricted repeated operation.

## 1. Entry state and retained physical law

Keep coordinates \((R,C,Y,D,F,G,GF,YG)\), unit volume and packet value, conserved material N=3, and the reaction law in the allocation note. Bound Y cannot reproduce or recycle; free Y can do both. Define

\[
P=(0,1,0,0,1,0,0,1).
\tag{1}
\]

This state has capture machinery, one Y bound to a gate, and one free packet. It is attained on the paid route from \(S=(2,0,1,0,1,0,0,0)\) when the first four events are build, bind, assemble C, capture. It is a physical entry state, not a reset applied after a vaguely defined successful episode.

The complete exit intensity, retaining all competing hazards, is

\[
\begin{aligned}
\lambda(x)={}&aR+(b+g)C+\beta RY+d(Y+YG)+\ell F\\
&+kFD(C+\theta Y)+\kappa RF+\delta(G+GF+YG)\\
&+\alpha_b G F+(\rho+\ell_b)GF+\mu GY+\nu YG.
\end{aligned}
\tag{2}
\]

All subsequent path probabilities use (2), not just the listed favorable reaction rates. Parameters are finite and positive for the displayed routes. The incident source and all reaction constants remain fixed through the episodes.

## 2. Three physical returns

Each arrow below is an existing reaction. No intermediate state is supplied externally. Each completed route returns exactly to P and keeps total Y positive.

### C wears and is rebuilt

| Event | State after event |
|---|---|
| C wear | \((0,0,0,1,1,0,0,1)\) |
| YG dissociation | \((0,0,1,1,1,1,0,0)\) |
| Y-catalyzed recycling | \((1,0,1,0,0,1,0,0)\) |
| Bind Y | \((1,0,0,0,0,0,0,1)\) |
| Assemble C | \((0,1,0,0,0,0,0,1)\) |
| Capture | P |

The selected propensities are \(b,\nu,k\theta,\mu,a,g\). The packet initially present pays for recycling the worn C. Dissociation makes Y available to perform that reaction; rebinding protects the recovered R from Y reproduction. Only after C is rebuilt can another packet be captured. Binding and dissociation are actual finite reactions, not decisions made by an external scheduler.

### G wears and is rebuilt

| Event | State after event |
|---|---|
| Gate constituent wears in YG | \((0,1,1,1,1,0,0,0)\) |
| Capture | \((0,1,1,1,2,0,0,0)\) |
| Recycle D, through either catalyst | \((1,1,1,0,1,0,0,0)\) |
| Build G | \((0,1,1,0,0,1,0,0)\) |
| Bind Y | \((0,1,0,0,0,0,0,1)\) |
| Capture | P |

The selected propensities are \(\delta,g,2k(1+\theta),\kappa,\mu,g\). Combining the two recycling labels is legitimate because their state updates coincide; their intensities add. Two newly captured packets pay the losses from gate wear and reconstruction while restoring the initial reserve.

### Y succession through temporary loss of G

| Event | State after event |
|---|---|
| Gate constituent wears in YG | \((0,1,1,1,1,0,0,0)\) |
| Recycle D | \((1,1,1,0,0,0,0,0)\) |
| Free Y reproduces | \((0,1,2,0,0,0,0,0)\) |
| Capture | \((0,1,2,0,1,0,0,0)\) |
| One Y wears | \((0,1,1,1,1,0,0,0)\) |
| Recycle D | \((1,1,1,0,0,0,0,0)\) |
| Capture | \((1,1,1,0,1,0,0,0)\) |
| Build G | \((0,1,1,0,0,1,0,0)\) |
| Bind Y | \((0,1,0,0,0,0,0,1)\) |
| Capture | P |

The selected propensities are

\[
\delta,\ k(1+\theta),\ \beta,\ g,\ 2d,
\ k(1+\theta),\ g,\ \kappa,\ \mu,\ g.
\tag{3}
\]

This route needs three captured packets, two recyclings, one gate build, and one gate and one Y wear. The gate's material temporarily becomes a second Y; material from the worn Y can then become the replacement gate. The finite N=3 stock therefore does not prevent succession: all three functional forms need not remain simultaneously installed during every intermediate moment.

**Identity qualification.** One Y wear after the population reaches two does not prove that the original Y wore. For that stronger event, use the usual exchangeable labeled realization of the count law: reproduction preserves the parent and produces a daughter; each Y constituent wears independently at rate d. Requiring the original to wear selects rate d instead of total rate \(2d\) at that step, or probability one half conditional on a Y-wear event there. This tagged process projects to the unchanged count law. The tag is analytical bookkeeping, not a control signal. The checker and the full-turnover certificate below use this stricter original-Y event.

Reproduction is helpful in this succession context while it is destructive in the fuel-empty C-repair context. The network is not being assigned a universal preference for suppressing reproduction.

## 3. Full turnover and the four-packet minimum

Concatenate the C-return route with the tagged Y-succession route. This is a 16-event macrocycle returning to P. The original C has worn and been reassembled; the original G has worn and been rebuilt; and the tagged original Y has worn after producing its surviving daughter. Returning counts alone would not establish these facts; the selected events and tagged refinement do.

The exact event totals are

| Event | Count |
|---|---:|
| Fresh captures | 4 |
| Recyclings | 3 |
| Gate builds | 1 |
| C wears | 1 |
| Y wears | 1 |
| G wears | 1 |
| Free or bound packet leaks | 0 |

The fuel identity gives \(\Delta U=4-3-1=0\). For \(W=N-D+U\), the work identity gives \(\Delta W=4-1-1-1-1=0\). No reserve or material is replaced outside the reaction law.

More generally, every physical P-to-P return obeys

\[
K_{\rm cap}=K_{\rm leak}+K_{\rm ble\!ak}+K_{\rm build}
+K_{Cw}+K_{Yw}+K_{Gw}.
\tag{4}
\]

Gate count also returns, so \(K_{\rm build}=K_{Gw}\). A return with at least one wear in every functional role therefore requires

\[
\boxed{K_{\rm cap}\ge1+1+1+1=4.}
\tag{5}
\]

The selected tagged macrocycle attains this minimum. Four packets is an exact lower bound in the declared packet/work ledger, not a calibrated thermodynamic free-energy or dissipation bound.

## 4. Exact path kernels and finite-time certificates

Let a selected route have successive pre-event states \(x_0=P,x_1,\ldots,x_{n-1}\), selected event intensities \(r_j>0\), and total exit intensities \(\lambda_j=\lambda(x_{j-1})\). Its subprobability return-time measure is the convolution

\[
K_{\rm path}(dt)=
\mathop{*}_{j=1}^{n}\left[r_j e^{-\lambda_jt}\,dt\right].
\tag{6}
\]

Every selected jump is required to be the next event; other events do not count as this certificate, even though some may permit other repairs. Its total mass and Laplace transform are

\[
p_{\rm path}=\prod_{j=1}^{n}\frac{r_j}{\lambda_j},\qquad
\int e^{-st}K_{\rm path}(dt)=\prod_{j=1}^{n}\frac{r_j}{\lambda_j+s}.
\tag{7}
\]

Thus the return clock is derived from the reaction law and generally is not exponential. An inverse mean time is not substituted for a regime-transition rate.

A useful finite-time lower bound is

\[
\boxed{K_{\rm path}([0,T])\ge
\prod_{j=1}^{n}\frac{r_j}{\lambda_j}
\left(1-e^{-\lambda_jT/n}\right)>0.}
\tag{8}
\]

This requires every holding interval to finish within T/n. It includes all competing hazards and does not condition on their absence for free.

At the already committed allocation witness, exact selected-path probabilities are approximately \(1.4320\times10^{-10}\) for C repair, \(2.9002\times10^{-6}\) for G repair, and \(1.6151\times10^{-11}\) for tagged Y succession. The 16-event macrocycle has the exact unrestricted-time selected probability

\[
p_M=\frac{743736579615}{321555482252584977116432838099968}.
\tag{9}
\]

Every macrocycle exit rate at this witness is at least four. At T=4, each of 16 holding slots therefore has exponent at least one; \(e>2\) implies

\[
K_M([0,4])\ge\frac{p_M}{2^{16}}
\approx3.5293\times10^{-26}.
\tag{10}
\]

This is a very small constructive lower bound, not an estimate of the probability of all possible turnover routes. It establishes realizability and composability; it does not establish likely operation.

The [exact check](../../../../experiments/shared-renewal-capability/renewal-return/exact_check.py) and [results](../../../../experiments/shared-renewal-capability/renewal-return/exact-check.json) retain every intermediate state, selected rate, total hazard and work increment. The checker deliberately reuses the reviewed allocation event implementation; it is a path/accounting check, not an independent reimplementation or a simulation search.

## 5. A comparative repair kernel, derived independently of first-hit gain

Let

\[
D_C=(0,0,0,1,1,0,0,1)
\tag{11}
\]

be the actual state after C wears at P. From this state, stop at the first renewed capture; joint success requires total Y still positive. Let \(\mathcal R_\zeta(dt,E)\) be the subprobability of that success at time dt with actual endpoint in E, for otherwise identical gate laws and bound-reproduction parameter \(\zeta\).

**Repair-kernel comparison.** If \(0\le\zeta_0\le\zeta_1\), then

\[
\boxed{\mathcal R_{\zeta_0}\ge\mathcal R_{\zeta_1}
\quad\text{as measures of successful time and endpoint}.}
\tag{12}
\]

**Proof.** Before the first renewed capture, U is at most one. Initially R=C=0. R can only be obtained by spending the sole packet on recycling; then R=1,C=U=0. Fabrication cannot occur before capture: initially there is no R, and once R exists there is no fuel. If any reproduction consumes that R before assembly, it leaves R=C=U=0 and makes all future capture impossible. After assembly, R=0 until capture. Consequently the only transition at which \(\zeta\) matters before success is an irreversible killing of the repair opportunity.

Couple all remaining reactions, including binding, leakage and constituent wear, and obtain the larger killing rate by adding a reproduction clock. Every successful trajectory of the higher-\(\zeta\) process remains a successful trajectory of the lower-\(\zeta\) process with the same time and endpoint. Equivalently, using the \(\zeta=0\) stopped law,

\[
\mathcal R_\zeta([0,H],E)=
\mathbb E_0\!\left[
\mathbf1_{\{\tau\le H,\,L_\tau>0,\,X_\tau\in E\}}
\exp\!\left(-\zeta\int_0^\tau\beta R_tYG_t\,dt\right)
\right],
\tag{13}
\]

where the indicator is zero when no successful capture occurs. This finite pre-capture state space has U≤1, so the killing construction needs no unbounded-generator exchange. ∎

The improvement for endpoint E={P} is strict at every H>0 when \(a,\beta,\mu,\nu,k\theta,g>0\) and \(\zeta_0<\zeta_1\). The dissociate–recycle–bind–assemble–capture route has positive probability and spends a positive holding time with R=YG=1; its extra killing probability is strictly positive.

To include the actual damage event, require the first jump from P to be C wear. Its density is \(b e^{-\lambda(P)t}\), identical across architectures. Convolving this density with \(\mathcal R_\zeta(dt,\{P\})\) gives an exact C-repair return kernel. It strictly improves when bound reproduction is blocked. The damage is neither imposed freely nor assumed to occur at time zero: its probability and elapsed time are included.

The selected tagged Y-succession kernel is identical across \(\zeta\), since its R-positive states have no bound Y. Its convolution with this C-repair kernel therefore yields a comparative full-turnover certificate returning to P. This is a derived improvement for a specified physical cycle assay, not a deduction from the earlier first-capture comparison.

For the narrower six-event C path alone, the exact unrestricted-time probability ratio is

\[
\frac{p_C^{\zeta=0}}{p_C^{\zeta=1}}
=\frac{a+d+\delta+\nu+\beta}{a+d+\delta+\nu}.
\tag{14}
\]

It equals 847 at the committed witness. That ratio is not the ratio for all repair trajectories; (12), rather than this path ratio, supplies the broader damaged-state comparison. Neither result compares unrestricted multi-cycle performance with an absent regulator from S.

## 6. Uniform conditional composition without a physical reset

The [P1 interface](../../../../theories/becoming/chapters/FORMAL-SPECIFICATION.md) requires a continuation guarantee conditional on the full modeled entry history. Here every certified macrocycle ends at the same full count state P. The same autonomous reaction law continues without changing a policy, supplying a packet, replacing material or reading the analyst's tags.

With time-homogeneous support, the Markov property gives the same return kernel after every such stopping time, conditional on every past history that reaches P through the certified event. If \(r(T)\) is the exact probability of a chosen macrocycle certificate within time T, m consecutive such cycles, each within T, have probability \(r(T)^m\) from P. Any uniform lower bound \(\underline r(T)\le r(T)\) gives the corresponding bound \(\underline r(T)^m\). This is an actual state-compatible composition; no separately chosen continuation for hidden histories is used.

The broader first-hit event in the allocation theorem does not always end at P: G may have worn or dissociated before capture. It cannot automatically use this singleton-entry guarantee. A compatible stronger entry event is the first four events build–bind–assemble–capture from S. At the committed witness its probability of completing by time three is at least

\[
p_{\rm entry}\ge\frac{2209}{24576}.
\tag{15}
\]

Together with (10), a completely physical finite certificate is

\[
\boxed{
\Pr_S(\text{entry and }m\text{ selected turnovers by }3+4m)
\ge\frac{2209}{24576}
\left(\frac{p_M}{2^{16}}\right)^m.
}
\tag{16}
\]

The bound is tiny and does not prove a favorable comparison from S. It does close the bookkeeping and conditional-interface gap for a realizable sequence. With time-varying support, aging hazards or hidden environment variables, the entry state must be enlarged or a new uniform bound established; this argument cannot silently discard them.

## 7. Sharp obstacles to reliable repair and indefinite return

At the damaged state \(D_C\), only four reactions are active: free-packet leakage at \(\ell\), YG dissociation at \(\nu\), Y wear at d, and gate wear at \(\delta\). Leakage leaves R=C=U=0; Y wear eliminates the last Y. Either event makes return to P impossible under this repertoire. Dissociation and gate wear can still permit rescue. Therefore, for **all** autonomous repair paths,

\[
\boxed{\Pr_{D_C}(\text{ever return to }P)
\le\frac{\nu+\delta}{\ell+\nu+\delta+d}.}
\tag{17}
\]

A target repair reliability \(r\in(0,1]\) consequently requires

\[
\boxed{\ell\le\frac{1-r}{r}(\nu+\delta)-d.}
\tag{18}
\]

If the right side is negative, no nonnegative leakage rate can meet this necessary condition. It is not sufficient: downstream competition and further wear can still defeat repair. The obstruction cannot be removed merely by increasing fabrication, binding or capture rates, which are disabled in the damaged state.

For \(\nu=\delta=d=1\), reliability one half requires \(\ell\le1\). The earlier paid-gain witness has \(\ell=141\), giving the all-path upper bound \(1/72\). This is conditional on actual entry into \(D_C\), not an unconditional failure probability for all repeated delivery trajectories.

There is also a simple return-level finiteness bound. At P,

\[
\lambda(P)=b+g+d+\delta+\ell+\nu.
\]

The next event kills the sole Y with probability \(\eta=d/\lambda(P)>0\). No reaction can restart an extinct Y lineage. Define strict returns as hits of P after a departure, excluding the holding interval at P itself. At each return the same conditional hazard applies. Thus the number N of further strict returns satisfies

\[
\Pr(N\ge m)\le(1-\eta)^m,\qquad
\mathbb E N\le\frac{1-\eta}{\eta}.
\tag{19}
\]

At the witness \(\eta=1/149\), so this coarse expected-return bound is 148. It covers more than actual turnover: reserve fluctuations can also produce count-state returns. It is not an estimate of useful completed repairs. In particular, no infinite sequence of P returns has positive probability. The earlier finite-material absorption theorem is also unaffected by deleting bound reproduction.

The resulting distinction is exact: the same process can supply real carrier succession, a better repair kernel, and positive probabilities of every finite number of returns while still lacking reliable repair in a damaged state and failing to persist indefinitely.
