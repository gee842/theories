# From damaged support capture to material retention of a formed response

6 October 2026. AI-authored mathematical development for Ren's [accepted derivation path](../../../../theories/becoming/chapters/GENERATIVE-GROUNDING.md#accepted-work-sequence). This note introduces a separate declared reaction law. It does not replace the earlier [failed regulator](PHYSICAL-REGULATION.md) or [paid allocation gate](ALLOCATION-CONTROL.md), and it does not identify actual molecules.

**Connection addressed:** organizational dependency → an internal difference → costly response formation → changed support capture → changed copying of the response. The achieved result is a conditional construction and an exact positive-rate copying-gain bound. The law supplies a site scaffold, the repair and autocopy repertoire, fuel chemistry and incident support. It does not derive individual learning, preference for useful variants in a shared pool, or revision of the copying mechanism.

**Current verification:** the analytical proofs and rational certificates received a [separate internal review](ENDOGENOUS-REGULATION-REVIEW.md). The [executable process](../../../../experiments/shared-renewal-capability/regulation/retention/README.md) now computes exact terminal expectations and outward-enclosed finite-horizon comparisons, with controls and actual-successor interventions. The [Lean extension](ENDOGENOUS-REGULATION-LEAN.md) proves the discrete event ledgers, bootstrap obstruction, rank bound, positive path and exact connection to the previous causal root. It does not mechanize the stochastic expected-copy theorem. The review's shared-pool neutrality result still blocks automatic useful-variant selection; the [next analytical extension](CONSEQUENCE-RETENTION-SELECTION.md) studies differential access under explicit additional premises.

## 1. Declared process and independent continuation task

Let the integer state be

\[
x=(C,D,P,G,F,E),\qquad C+D=N,\quad P+G=M,\quad 0\leq F\leq B.
\]

C is an intact site that can capture incident support; D is the same site in a damaged state. P is available regulator precursor, G an assembled regulator, F usable fuel, and E a finite incident-support stock. The fixed site scaffold is supplied: G begins absent, but the whole organization does not begin from unstructured material.

The continuation task is further capture of E into usable F, together with preservation or restoration of the capture sites. It is specified without counting G as success. Copy count and surviving G are separate response-retention observables. An observer may record all three without influencing any transition.

| Event | State change | Propensity |
|---|---|---|
| Damage | C → D | αC |
| Damage-coupled fabrication | D + P + F → D + G | κDPF |
| Repair | G + D + F → G + C | ρGDF |
| Capture | C + E → C + F | gCE 1\{F < B\} |
| Copying | G + P + F → 2G | βGPF |
| Regulator wear | G → P | δG |
| Fuel leakage | F → spent | ℓF |

All rates are nonnegative. In the positive-rate witness below they are strictly positive. A consumed F becomes spent support in fabrication, repair and copying as well as leakage; omitted spent products are accounting variables, not erased energy. Wear returns usable precursor but no fuel. This precursor recovery is a supplied coarse chemistry; no claim of molecular or thermodynamic identification follows from the ledger.

B is a declared physical storage-capacity law: capture stops when storage is full. It is not a neutral numerical truncation. Finite E already bounds fuel by F₀+E₀ even without this capacity assumption. The theorem's process has B=2 as part of its specified dynamics.

There is no separately read, costless sensor. D is an actual damaged site whose encounter with P and F catalyzes paid fabrication. Sensing and formation are bundled in that encounter. Thus this model explains a direct damage-coupled response, not formation of an independently replaceable measuring device. Its useful response chemistry is supplied, including the sign of repair and autocopy specificity. Its formation is endogenous under those laws.

The causal loop is explicit:

\[
D\longrightarrow\text{fabrication of G}\longrightarrow C
\longrightarrow\text{capture of F}\longrightarrow\text{copying of G}.
\]

No success, fitness, survival-value or observer reward variable enters a propensity. The last link consumes actual captured fuel. Copying also consumes fuel inherited from the initial preparation, so its mere occurrence does not identify mediation by repair; interventions must establish the additional consequence-coupled component.

## 2. Exact accounting and local drift

Let A, R, K and L count fabrication, repair, copying and leakage events along a history; let J count captures. Every path satisfies

\[
F_t=F_0+J_t-A_t-R_t-K_t-L_t,\qquad E_t=E_0-J_t,
\]

and hence

\[
\boxed{F_t+E_t+A_t+R_t+K_t+L_t=F_0+E_0.}
\tag{1}
\]

The two material ledgers C+D=N and P+G=M are also invariant. With finite N,M,B,E₀ the reachable state space is finite, the rates are bounded, and the process is nonexplosive. No overflow approximation or favorable restart is required.

The generator gives

\[
\mathcal LC=\rho GDF-\alpha C,
\tag{2}
\]

\[
\mathcal LG=\kappa DPF+\beta GPF-\delta G,
\tag{3}
\]

\[
\mathcal LF=gCE\mathbf1_{F<B}-\kappa DPF-\rho GDF-\beta GPF-\ell F.
\tag{4}
\]

Consequently, with G₀=0,

\[
\mathbb E G_H=\mathbb E A_H+\mathbb E K_H-
\delta\int_0^H\mathbb E G_t\,dt,
\]

\[
\boxed{\mathbb E K_H=\int_0^H\beta\mathbb E[G_tP_tF_t]dt.}
\tag{5}
\]

These identities distinguish new fabrication, templated copying and continued presence. Setting β=0 removes copying, not all reconstruction: damage-coupled fabrication may still rebuild G. Positive stock alone cannot identify which route sustained it.

For an existing G, the local balance of copying and wear is βPF−δ per regulator. This statewise balance is not a population-average invasion theorem: fuel, sites, precursor and formation change jointly, and \(\mathbb E[GPF]\) is not generally \(\mathbb EG\,\mathbb EP\,\mathbb EF\). Useful repair can initially reduce F and copying before later capture compensates.

## 3. Bootstrap obstruction and a complete constructive path

Suppose all sites are damaged, G₀=0 and F₀<2. Then C can never become positive under this law. If F₀=0 there is neither fabrication nor repair. If F₀=1, fabrication consumes the only fuel; because capture requires C, neither capture nor repair can then occur. Copying, wear and leakage do not restore fuel. This holds even when E₀ is arbitrarily large.

Thus an incident source alone cannot bootstrap this response. At least two initially accessible fuel units are necessary for the all-damaged preparation: one for fabrication and one for repair. This is not a universal minimum for biological regulation; it follows from this repertoire's unit costs and absence of alternative routes.

For N=1, M=3, B≥2, use the single common preparation

\[
x_0=(0,1,3,0,2,2).
\tag{6}
\]

All arms have the same site scaffold, precursor, usable fuel and source stock. The path

\[
\text{fabricate, repair, capture, copy, capture, copy}
\tag{7}
\]

has strictly positive probability by any H>0 whenever κ,ρ,g,β are positive and the remaining rates finite. Its successive (C,G,P,F,E) states are

\[
\begin{aligned}
&(0,0,3,2,2)\to(0,1,2,1,2)\to(1,1,2,0,2)\\
&\to(1,1,2,1,1)\to(1,2,1,0,1)\\
&\to(1,2,1,1,0)\to(1,3,0,0,0).
\end{aligned}
\]

The two copy events are funded by actual new capture after repair, not by a fresh preparation. The original two fuel units pay fabrication and repair. This path realizes the named causal connection from an absent regulator under one law, but a positive path alone establishes neither typical success nor an advantage over alternatives.

## 4. Exact gain and failure boundary in the zero-loss reference law

First set α=δ=ℓ=0, retaining positive κ,ρ,g,β and preparation (6). This is a calculational reference, not the final positive-loss result.

The first event is fabrication, at rate 6κ. It leaves C=0,D=1,G=1,P=2,F=1,E=2. The second-event race has:

- further fabrication, rate 2κ;
- copying, rate 2β;
- repair, rate ρ.

If fabrication or copying wins, the last fuel is spent while C=0. Capture is thereafter impossible; the total copy count is respectively zero or one. If repair wins, C becomes one, D zero, and two subsequent captures fund exactly two copies almost surely. Finite waiting follows from g,β>0 and the remaining enabled finite sequence; intermediate capture order does not change the endpoint.

For the active process A and the repair-disabled process 0, therefore,

\[
\boxed{\mathbb E_A K_\infty=
\frac{2\beta+2\rho}{2\kappa+2\beta+\rho},\qquad
\mathbb E_0 K_\infty=\frac{2\beta}{2\kappa+2\beta}.}
\tag{8}
\]

Their difference is

\[
\boxed{\mathbb E_AK_\infty-\mathbb E_0K_\infty
=\frac{\rho(4\kappa+2\beta)}
{(2\kappa+2\beta+\rho)(2\kappa+2\beta)}>0.}
\tag{9}
\]

This comparison gives the disabled process the fuel it saves by omitting repair. A separately matched-cost ineffective response, G+D+F→G+D+spent at rate ρGDF, spends the same attempted-response fuel without restoring C. Its expected copy count is

\[
\mathbb E_{\rm dead}K_\infty=
\frac{2\beta}{2\kappa+2\beta+\rho}.
\tag{10}
\]

At unit productive rates, the three values are 4/5, 1/2 and 2/5. The active process ends with three regulators precisely when repair wins the second race, and with two otherwise: its expected terminal G is 2+ρ/(2κ+2β+ρ), versus two for repair-disabled dynamics. These terminal-stock statements belong to the zero-loss reference only.

### Source support changes the sign

Keep the same preparation except set E₀=0. Repair then spends the final fuel without enabling a fresh capture. Its total copy expectation is \(2\beta/(2\kappa+2\beta+\rho)\), strictly below the repair-disabled value. The same response is a net copying burden when the dependency it repairs cannot provide support.

With E₀=1 the active expectation is \((2\beta+\rho)/(2\kappa+2\beta+\rho)\), exceeding the disabled value by \(2\kappa\rho/[(2\kappa+2\beta+\rho)(2\kappa+2\beta)]\) when κ>0. This smaller gain partly reflects preventing redundant fabrication. It must not be confused with the two-capture mechanism of (8).

Damage is consequently a conditionally useful physical signal, not a sufficient statistic for net benefit. A source can be exhausted while damage still induces costly fabrication. No law guarantees that this response discovers the changed meaning of its signal.

## 5. A finite-horizon theorem with all rates positive

Take (6), B=2, κ=ρ=g=β=1, H=12 and

\[
\alpha=\delta=\ell=\varepsilon=1/10000.
\tag{11}
\]

Both active and repair-disabled arms have these same positive wear, damage and leakage rates. Their only difference is whether repair occurs.

**Theorem.** The active law has at least 53/1250 more expected copy events by H=12 than the repair-disabled law; the inequality is strict.

**Proof.** In the zero-loss active reference, use two disjoint event classes. The first consists of fabrication followed by copying, both waits at most two time units. The branch probability is 2/5 and the exit rates are 6 and 5. The second follows (7), with every wait at most two; its branch probability is \((1/5)(2/3)=2/15\) and exit rates are 6,5,2,3,1,2. The factor 2/3 selects copying rather than a second capture at the fourth step. The first class contributes one copy; the second contributes two.

Since \(e^2>7\), each wait with exit rate q is at most two with probability \(1-e^{-2q}>1-7^{-q}\). Hence

\[
\begin{aligned}
\mathbb E_A^{(0)}K_{12}&>L,\\
L&=\frac25(1-7^{-6})(1-7^{-5})\\
&\quad+\frac4{15}\prod_{q\in(6,5,2,3,1,2)}(1-7^{-q})\\
&=\frac{35259954180435648}{56994475926865715}>\frac35.
\end{aligned}
\tag{12}
\]

The zero-loss disabled expectation at time 12 is at most its terminal value 1/2. Its gap from the active law is therefore greater than 1/10.

Couple each positive-loss arm to its own zero-loss reference until the first damage, wear or leakage event. Their combined nuisance intensity is bounded by

\[
\alpha C+\delta G+\ell F\leq\varepsilon(1+3+2)=6\varepsilon.
\]

Thus coupling failure by H has probability at most 6εH. Equation (1) bounds K_H between zero and F₀+E₀=4 in either process, including after coupling failure. The expected-copy perturbation is at most 4·6εH per arm. For the difference of both arms,

\[
\mathbb E_AK_{12}-\mathbb E_0K_{12}
>\frac1{10}-2\cdot4\cdot6\cdot\frac1{10000}\cdot12
=\boxed{\frac{53}{1250}}.
\tag{13}
\]

This proof includes regulator wear, site damage, leakage, formation cost, repair cost, copying cost, actual successors and a finite depleted source. It uses an intentionally simple uncalibrated parameter witness. It does not establish favorable rates in nature, efficient adaptation, or an all-times advantage. ∎

**Adverse-regime corollary.** Keep the same positive rates, cap and horizon but set E₀=0 in both arms. Then the repair-disabled process has more expected copies than the active process by strictly more than 153/2500.

**Proof.** In the zero-loss reference the active expectation is at most its terminal value 2/5. The disabled process has first two exit rates 6 and 4 and conditional copy probability 1/2. Allowing each wait six time units gives

\[
\mathbb E_0^{(0)}K_{12}>
\tfrac12(1-7^{-18})(1-7^{-12})>49/100.
\]

The reference gap is greater than 9/100. With E₀=0, (1) bounds each copy count by two. The same coupling therefore loses at most \(2\cdot2\cdot6\varepsilon\cdot12=18/625\), giving \(9/100-18/625=153/2500\). Repair and damage sensing are unchanged; the source dependency no longer supplies material benefit. ∎

## 6. What the interventions identify

The all-damaged preparation is a structural diagnostic; additional intact-site preparations are needed to compare useful regulation where continued capture is already possible. The following interventions have different meanings and must not be pooled as independent confirmations:

| Intervention | Identified connection or limitation |
|---|---|
| κ=0 with G₀=0 | Formation absent; copying cannot create its own first template. |
| ρ=0 | Response cannot restore capture sites, while saving repair fuel. |
| Ineffective matched-cost repair | Same attempted expenditure fails to restore C; separates expense from repair effect. |
| g=0 or E₀=0 | Repaired sites cannot obtain further support; detects dependency and source limitation. |
| β=0 | Templated copying removed; fresh fabrication remains possible. |
| Formation independent of D, with explicit cost matching | Tests the value of damage coupling rather than usefulness of installed repair alone. |
| F₀<2 in the all-damaged preparation | Proved bootstrap failure, regardless of uncaptured source size. |
| Higher κ, insufficient source, or depleted source | Can expose redundant fabrication, precursor/fuel diversion and misleading damage signals. |

Copy counts, surviving regulators, site condition and fresh captures must be reported separately. Positive copied stock is not an independent proof of productive continuation. Also, a constitutionally constant repair catalyst would perform this same repair when present: this construction demonstrates damage-coupled formation and consequence-coupled material retention, not the superiority of sophisticated feedback over every open-loop design.

## 7. Finite support and the next missing connection

**Subsequent result, 6 October 2026:** the [formed-variant integration](FORMED-VARIANT-SELECTION-INTEGRATION.md) joins variant formation and mixed-population differential reconstruction under a newly declared law with continuous resource accounting. It addresses the preparation gap identified below without claiming an exact kinetic refinement of this earlier model. The origin and revision of the supplied sensing, access and copying architecture remain the next central connection.

Under α,δ,ℓ>0, every trajectory uses at most F₀+E₀ fuel-consuming events and captures at most E₀ packets. Almost surely any enabled leak, wear or damage eventually occurs unless its reactant has already disappeared. After the finitely many repairs and regulator births, intact sites and regulators therefore disappear almost surely; finite existing fuel leaks away. Some uncaptured E can remain inaccessible. The finite construction cannot support indefinite active renewal.

The material loop explains why restoring a productive dependency can cause additional copying of the response that restored it. It does not explain why the useful response defeats a useless competitor sharing the same fuel. Equal-rate variants can receive the same replenished fuel, so repair can subsidize a nonrepairing lineage. Local association, compartmentalization or another feedback route would need its own formation account; adding one by assumption would shift that part of the problem upstream.

At the original analytical checkpoint, interventions and open-loop comparisons remained unimplemented. The subsequent [gate audit](REGULATION-RETENTION-INTEGRATION.md) accepts the conditional milestone after those checks and the Lean bridge were completed. Empirical identification, composition with competing response formation and revision of the supplied sensing/copying architecture remain wider obligations. In particular, copying is a chemically supplied retention channel, not yet individual learning or selection over selectors.

The next compatible result should introduce actual alternative responses under this same resource history, establish which consequence-to-retention routes favor which variants, and preserve regimes of neutral sharing, exploitation and collapse. The [paid-association selection extension](CONSEQUENCE-RETENTION-SELECTION.md) now gives a conditional local-return mechanism and an exact frequency criterion, but begins with two supplied variant seeds and has not yet been composed with this formation process. That remaining composition matters: a separately chosen contest preparation is not the actual successor of the construction above.
