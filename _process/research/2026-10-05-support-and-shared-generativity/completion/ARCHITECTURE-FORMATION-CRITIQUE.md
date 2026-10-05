# Forming fabrication capability under one fixed physical law

5 October 2026. AI-assisted mathematical critique and construction, continuing from commit `348d82644a92315a0ea415a9edc44708e27ad516`. The [allocation theorem](ALLOCATION-CONTROL.md) pays for G molecules but compares supplied construction-channel availability. The [completion plan](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/COMPLETION-PLAN.md) correctly leaves physical implementation of that difference open.

**Advance.** A material fabricator can replace the free channel switch. The construction below has one generator, two competing fabricator types formed from absence, explicit costs, decay and a paid replacement route. A finite theorem compares their unconditional contributions to a common delivery event. A separate exact frequency calculation shows why that functional advantage need not select the useful fabricator. Neither result completes spontaneous shared generative direction.

## 1. What must become a state, and what can remain a law

It is unnecessary to require the laws themselves to construct their own existence. The obligation is narrower: if changing an installed organization changes which reactions occur, the organization should be a physical state and the change should have a physical trajectory under common laws.

Replace the directly enabled reaction R+F→G by a reaction catalyzed by a material fabricator A. Its propensity is zero when A is absent, without changing the generator. The chemical specificity of A remains part of the supplied law. This explains formation of an allowed organization; it does not explain why the world supplies those molecular possibilities or discover an unlimited new reaction vocabulary.

There is an immediate resource obstruction. If a retained fabricator, a gate, C and Y each require a separate material unit, simultaneous presence needs at least four units. Adding a retained fabricator to the previous N=3 successful state without changing its budget is impossible. An N=3 implementation instead needs an explicit shared-function species, consumption of the fabricator, or material turnover. None may be inserted silently.

## 2. A minimal candidate with material fabricators

Use types i=0,1. G0 blocks bound reproduction, with zeta0=0; G1 retains the original bound-reproduction law, with zeta1=1. Both bind fuel and Y under the same remaining constants. Keep the original plant reactions and labeled gate complexes, but remove all uncatalyzed gate-production channels. Add, for each type,

| Reaction | Propensity | Work-equivalent increment |
|---|---|---:|
| R+F→Ai | sigma_i RF | −1 |
| Ai+R+F→2Ai | rho_i Ai RF | −1 |
| Ai+R+F→Ai+Gi | kappa_i Ai RF | −1 |
| Ai→D | eta_i Ai | −1 |

The first reaction forms a fabricator without a template; the second copies one already present. Both spend a precursor and packet. Gate fabrication returns the catalyst. There is no free Ai-type conversion, no free G production and no externally selected change of rates during a run. The entire reaction list, including both alternatives, is fixed before the preparation.

The conserved material and reduced work ledger are

\[
N=R+C+Y+D+\sum_i(A_i+G_i+GF_i+2YG_i),
\quad U=F+\sum_iGF_i,\quad W=N-D+U.
\tag{1}
\]

Capture adds one packet and one W; recycling preserves W; formation, copying, leakage and wear charge the stated losses. Binding preserves this reduced ledger. This is not a thermodynamic identification of binding free energy or of achievable rate constants.

The proposed material budget is N=4 and the common preparation is

\[
Z_0:\quad R=3,\quad Y=1,\quad F=2,
\qquad C=D=A_i=G_i=GF_i=YG_i=0.
\tag{2}
\]

Both fabrication capacities and all gates are initially absent. W0=6. Take all relevant constants finite and positive, with sigma0=sigma1=sigma, kappa0=kappa1=kappa, and eta0=eta1=eta. Copying rates can differ. The supplied environmental capture rate is gC; no input is captured without C.

**No-template obstruction.** If every reaction creating any Ai requires an Ai already present, the face A0=A1=0 is invariant. Autocatalytic copying alone cannot explain formation from (2). A paid template-free route, an explicitly imported seed, or a different reachable intermediate is necessary. Here the sigma reactions supply that route. This is a statement about reaction access, not an assertion that a spontaneous formation rate is physically known.

## 3. A finite theorem comparing actually generated alternatives

Define the common target E_H: the second fresh capture occurs by H with at least one fabricator, at least one gate constituent, C and total Y present, and W at least its initial value 6. The initially supplied packets do not count as fresh captures. This is delivery with retained machinery and recovered assigned work, not indefinite persistence or terminal readiness after H.

Let I=i mean that the **first actual reaction** from Z0 is template-free formation of Ai. These events are endogenous branches of the same process. Other possible first events are retained in the law. Compare

\[
J_i(H)=\Pr_{Z_0}(I=i,\ E_H).
\tag{3}
\]

These are unconditional branch contributions. They are not an intervention contrast, total architectural prevalence, or a claim that successful organizations are selected. Since both formation propensities are 6sigma at Z0, the two branches have identical occurrence probabilities and conditional first-waiting-time laws.

I and the capture counters are analyst event labels; they supply no observations or control to the physical process. Implementing an experimental readout of this event needs its own observation and resource account.

### A lower bound for the blocking branch

An actual six-event route is:

1. form A0, spending one R and F;
2. let A0 fabricate G0, spending another R and F;
3. bind G0 to Y;
4. assemble the remaining R into C;
5. capture one new packet;
6. capture a second new packet.

Exclude all competing events on this particular route, including dissociation and every wear event. All material is retained. At its end A0=1, C=1, YG0=1, F=2, so W=6 again. It satisfies the same target offered to either architecture. All rejected events still appear in the race denominators.

The six total rates at the successive states are

\[
\begin{aligned}
\Lambda_0&=12\sigma+3a+3\beta+d+2\ell,\\
\Lambda_1&=2\kappa+4\sigma+2\rho_0+2a+2\beta+d+\eta+\ell,\\
\Lambda_2&=\mu+a+\beta+d+\delta+\eta,\\
\Lambda_3&=a+\nu+d+\delta+\eta,\\
\Lambda_4&=g+b+d+\delta+\eta+\nu,\\
\Lambda_5&=\Lambda_4+\ell.
\end{aligned}
\tag{4}
\]

For example, after A0 forms there are R=2 and F=1: each template-free competitor has rate 2sigma, copying A0 has rate 2rho0, and G0 fabrication has rate 2kappa. After the gate forms F=0, so further fabrication, copying and fuel binding are disabled. In the last two phases Y remains bound on the chosen route, excluding fuel binding and keeping the displayed leakage rate correct.

Exponential races and requiring each phase to finish within H/6 give

\[
J_0(H)\ge L_0(H):=
\frac{6\sigma}{\Lambda_0}
\frac{2\kappa}{\Lambda_1}
\frac{\mu}{\Lambda_2}
\frac{a}{\Lambda_3}
\frac{g}{\Lambda_4}
\frac{g}{\Lambda_5}
\prod_{j=0}^{5}(1-e^{-\Lambda_jH/6}).
\tag{5}
\]

This includes the probability and time of creating fabrication capability, not merely performance conditioned on finding it already installed.

### An upper bound for the nonblocking branch

After first forming A1, the state has R=2, Y=1, F=1 and A1=1. Before the **first C assembly**, there can be no capture, and U cannot exceed 1. Forming A0 and then fabricating G0 needs two packet expenditures, so G0 cannot appear in this interval. Copying does not provide a cheaper route, and no free type conversion is present.

Consequently all bound Y that can occur before first C retains its reproduction channel. While total Y is positive, the competing C-versus-Y allocation propensities are aR and beta R L, with L≥1. At any such allocation, the conditional chance of C is at most a/(a+beta). Other events may change L or terminate the opportunity, but cannot make this bound larger. Y extinction is irreversible for the target.

There are initially two R units and at most one packet-funded recycling before first C. Thus at most three C-or-Y allocation events can occur before first C; fabricator formation and fabrication can only reduce that budget. Mark the successive allocation events with independent uniforms. Their C probabilities are each bounded by a/(a+beta), so a union bound gives

\[
J_1(H)\le
\frac{6\sigma}{\Lambda_0}
\min\!\left\{1,\frac{3a}{a+\beta}\right\}.
\tag{6}
\]

The target needs C and a surviving Y lineage. A1 may later give way to A0 or help form G0 **after a first capture**; the bound does not deny those paths. It bounds their necessary earlier first-C event, before new fuel is available. It therefore remains valid for the two-capture target.

### Nonempty finite-rate gain class

Fix any H>0 and positive finite a,b,d,delta,eta,nu,g,ell,k and copying rates. In the declared unit setting choose

\[
\beta=m,\quad\sigma=m^2,\quad
\kappa=m^3,\quad\mu=m^2.
\tag{7}
\]

As m grows, the first three probability factors in (5) tend to 1/2, 1, 1, and their timing factors tend to 1. The remaining factors are fixed and positive. Hence L0(H) tends to the strictly positive value

\[
\frac12\frac{a}{\Lambda_3}\frac{g}{\Lambda_4}\frac{g}{\Lambda_5}
\prod_{j=3}^{5}(1-e^{-\Lambda_jH/6}),
\]

whereas the right side of (6) tends to zero. Therefore, **for every fixed positive H there is a sufficiently large finite m for which J0(H)>J1(H)**. No infinite rate is used in the resulting model. This is a sufficient existence class, not chemical calibration or an assertion that one fixed model wins at all horizons.

The proof supplies an advantage of two equally offered, dynamically generated branches under one fixed generator. It does not count other first-event histories as failures, condition away formation expense, or show that the useful architecture becomes more prevalent. Up to the second capture, N is fixed and U≤4, so a stopped finite-state calculation can check the full event without a fuel truncation. No numerical evaluation is claimed in this note.

## 4. Replacement is possible, but sustained maintenance needs a flux

At the successful return state A0=1, C=1, YG0=1, F=2, an actual paid replacement cycle is

\[
A_0\text{ wear},\quad C\text{-catalyzed recycling},\quad
A_0\text{ formation},\quad \text{capture},\quad\text{capture}.
\tag{8}
\]

Wear yields D=1. Recycling spends one packet to recover R; template-free formation spends the second to replace A0. Two captures restore the packet stock. C, Y and gate material can remain intact throughout. Every selected event has positive finite rate; competing wear, leakage and alternative formation remain in the denominators. Thus completion within any positive window has a positive path bound. Success returns to the same physical state by real events, not an external reset. Iterating via the strong Markov property proves positive probability of any specified finite number of such paid cycles.

This is reachability of replacement, not high reliability, positive stationary maintenance or inheritance fidelity. The original A0 molecule is lost; the sigma competition can rebuild A1 instead. Copying provides an additional paid renewal route where spare R and fuel exist, but no copying advantage is assumed. Eventual extinction in a finite degrading system is not removed by exhibiting a finite cycle.

A quantitative necessary condition follows from the ledger. Let Bi(T) count all Ai births, including copying, and Di(T) count Ai wear. Pathwise,

\[
A_i(T)-A_i(0)=B_i(T)-D_i(T).
\]

Each birth and wear costs one W, whereas gate fabrication consumes Ai only catalytically. If Kcap counts captured packets, nonnegative remaining W and the other nonnegative costs give

\[
\mathbb E K_{\rm cap}(T)+W(0)
\ge\sum_i\left[
\mathbb E A_i(T)-A_i(0)
+2\eta_i\int_0^T\mathbb E A_i(t)\,dt\right].
\tag{9}
\]

Thus maintaining mean fabricator counts mi over a long interval requires capture power at least 2 sum_i eta_i mi in this ledger, before leakage, gate fabrication or plant upkeep. Since capture intensity is gC, the actual jointly maintained source machinery must supply that flux. A source's availability alone does not certify capture, precursor repair or allocation of the resulting packets to fabricator renewal. This necessary condition is specific to the declared formation and wear costs, not a universal thermodynamic constant.

## 5. Why copying success does not imply shared generativity

The same fixed generator gives an exact counterexample to an automatic selection inference. Let n=A0+A1≥2 and x=A0/n. Take equal template-free rates sigma and equal wear eta, but rho0<rho1. The other physical reactions change neither fabricator count, so their immediate contribution to x is zero. Applying the generator to the fraction gives

\[
\boxed{
\mathcal Lx=
\frac{RF}{n+1}\left[
\sigma(1-2x)
+n x(1-x)(\rho_0-\rho_1)\right].}
\tag{10}
\]

Equal per-constituent wear cancels exactly in the fraction drift for n≥2. The two birth contributions use their actual changes (1−x)/(n+1) and −x/(n+1). At RF>0 and 1/2≤x<1, (10) is strictly negative. The useful blocking type is driven downward in relative abundance even though it can improve the delivery task. With the retained positive Y-recycling channel and N=4, a state with A0=A1=R=Y=F=1 is reachable: assemble C, capture twice, form each fabricator, let C wear, then recycle its material through Y. A larger material budget permits the same competition while capture and gate machinery coexist.

Improved shared capture can change the common RF factor, but cannot reverse this local sign. Preferential returns, spatial assortment, differential retention or another material coupling could change the result; such a coupling must enter the generator and be paid. Calling copying fitness 'generativity' would erase the distinction rather than prove it. Likewise, a larger share of A0 among successful delivery trajectories is a conditional observation, not an unconditional increase in A0 prevalence.

## 6. What remains before claiming architecture-level direction

This proposal closes one modeling gap: fabrication availability is now material, formed, worn and replaced under common laws. It proves a finite functional comparison of endogenous branches and supplies a necessary renewal flux. It leaves chemical feasibility, robust whole-law architecture prevalence, replication/retention of useful specificity, protection against faster copiers, and repeated joint performance open.

The next computation should use the same preparation and generator for all branches, record both formation types and all missed opportunities, and calculate unconditional formation, replacement and delivery probabilities together. It should test both the useful-delivery theorem and the adverse frequency drift. A claimed direction needs a mechanism that couples architecture's actual retention or propagation to the joint function, plus a justified class in which that coupling holds. The positive effect of a fabricated gate, by itself, supplies neither premise.

### Provenance and status

Read the allocation proof and current completion plan, using the previously reviewed gate event table. This note supplies new symbolic proofs and a proposed model; no physical data or new simulation is reported. Inspected source hashes:

- Allocation proof: `93ba1c7d550d64b3176e34c1826ae45889b0a68907e33d0c766825273be7f60b`.
- Completion plan: `28d8a430f54efaa51a3e8896ea8fd41ad4601fd0fe8f6e69c2fb9191930`.
- Physical regulation table/note: `de69fe40bd6f693c0c99f6eb87fd062810d2b696eb6f8057be6dd6d036b6bccc`.

Only this new critique file is authored here; existing models and results are preserved. The common-law architecture construction is a conditional formal candidate for review, not completion of the universal claim or a normative conclusion.
