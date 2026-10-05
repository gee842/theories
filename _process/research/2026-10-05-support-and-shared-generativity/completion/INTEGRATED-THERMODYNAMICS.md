# Thermodynamics of the common formation-and-turnover model

5 October 2026. AI-authored conditional derivation, continuing after `f81afc0`. This extends the [material-fabricator model](ARCHITECTURE-FORMATION-CRITIQUE.md) itself, with both architectures and their formation routes in one generator. It does not substitute the earlier N=3 first-capture model for the new integrated assay. The [previous reversible embedding](THERMODYNAMIC-EMBEDDING.md) supplies the thermodynamic convention; the finite-source approximation and rate bounds below are new.

**Conditional result.** Every certified strict finite-time comparison between the two endogenous branch contributions of the N=4 formation-plus-full-turnover assay has a finite, reversible mass-action realization with the same comparison sign. The construction uses one common potential assignment, positive reverse reactions and a finite initial source stock. Source depletion and reverse reactions receive separate quantitative error budgets. This is consistency and robustness within ideal stochastic chemical thermodynamics, not a molecular design, rate calibration or empirical validation.

**The explicit witness is extreme.** It retains the integrated proof's rate scale \(m\approx2.43\times10^{21}\), some forward constants of order \(m^3\), and a tiny certified event margin. The thermodynamic certificate adds approximately \(9.78\times10^{24}\) charged source carriers and selects potential scale \(M=299\). Its guaranteed surviving branch-probability difference is only greater than \(3.09\times10^{-22}\). These are finite mathematical bounds; none is an identified laboratory rate, a success-probability estimate or a practical design claim.

## 1. The physical process and observed event

Use the common species and the exact integrated assay in [Formation and full carrier turnover](INTEGRATED-FORMATION-RENEWAL.md):

\[
(R,C,Y,D,F,A_0,A_1,G_0,G_1,GF_0,GF_1,YG_0,YG_1).
\]

The backbone count is

\[
N=R+C+Y+D+\sum_{i=0}^1(A_i+G_i+GF_i+2YG_i)=4.
\tag{1}
\]

The preparation has \(R=3,Y=1,F=2\), with every other species absent. Each type has template-free formation \(R+F\to A_i\), copying \(A_i+R+F\to2A_i\), catalytic gate fabrication \(A_i+R+F\to A_i+G_i\), and fabricator wear \(A_i\to D\). Their propensities are \(\sigma_i RF,\rho_i A_iRF,\kappa_i A_iRF,\eta_i A_i\). Here \(\rho_i\) denotes copying; use \(\rho_F\) for fuel dissociation to avoid the older notation collision.

Type 0 blocks bound reproduction: \(\zeta_0=0\). Type 1 retains it: \(\zeta_1=1\). Both retain the other declared plant and gate reactions, including no recycling catalyzed by either bound-Y complex. The reaction repertoire and its chemical specificity remain assumptions.

The integrated observable enters a count/type state

\[
P_{ij}:\quad A_i=C=YG_j=1,\quad F=2,
\]

at the second **forward source capture**, then returns to that same count/type state at the eighth forward capture with each of the four functional carriers present at entry having undergone its specified wear event. The bound complex contains two carriers. The assay therefore includes two entry captures and six captures during a full replacement cycle. Let \(I=i\) mean that the first actual reaction is template-free formation of \(A_i\); the quantities compared are the unconditional joint probabilities

\[
J_i(T)=\Pr(I=i,\ \text{the integrated event by }T).
\tag{2}
\]

The same type-neutral event is offered to both branches; the useful selected route uses \(P_{00}\). Both alternatives occur within one law, not in externally switched generators. The event flags and carrier tags are analyst records. They neither influence the chemistry nor provide a free physical memory or readout device. If a reaction selects among indistinguishable constituents, the coupling below uses the same constituent selection until its first unmatched event.

The general bounds use a stop at the \(K\)-th forward capture, with \(K=8\) here. Any earlier declared failure can also stop the assay. Producing a packet by reverse leakage or reverse synthesis is **not** a forward source capture.

## 2. Finite source and common potentials

Add a charged source carrier \(H_f\) and spent carrier \(L_f\). Initially

\[
H_f=B,\quad L_f=1,\qquad B\ge K,
\tag{3}
\]

where \(B\) is a finite integer common to the entire process. Capture is

\[
H_f+C\rightleftharpoons F+C,
\qquad a_{\rm cap}^+=\frac gB H_fC.
\tag{4}
\]

Every packet-consuming event produces one \(L_f\): free and bound leakage, both recycling channels, template-free formation, copying and catalytic fabrication. The other stoichiometries are unchanged. The second conserved moiety is

\[
H_f+L_f+F+GF_0+GF_1=B+3.
\tag{5}
\]

The full chemical count space is finite for every finite \(B\), regardless of whether the monitored event occurs. A thermal bath maintains the stipulated temperature. No chemical species is chemostatted in this construction.

In the same normalized unit-volume/falling-factorial convention as the previous embedding, define

\[
K_F=\frac{\alpha_b}{\rho_F},\qquad K_Y=\frac\mu\nu,
\qquad t=e^{-M},\qquad M>0.
\]

The two types share these binding constants as in the common generator. Assign dimensionless standard potentials, in \(k_BT\) units,

\[
\begin{aligned}
&\varphi_D=\varphi_{L_f}=0,\qquad
\varphi_C=\varphi_Y=\varphi_{A_i}=\varphi_{G_i}=M,\\
&\varphi_R=2M,\quad\varphi_F=3M,\quad
\varphi_{H_f}=4M-\ln B,\\
&\varphi_{GF_i}=4M-\ln K_F,\qquad
\varphi_{YG_i}=2M-\ln K_Y.
\end{aligned}
\tag{6}
\]

The shift \(-\ln B\) declares the source's reference potential so its population-dependent chemical potential initially corresponds to \(4M\), in this normalization. It also makes the capture reverse coefficient independent of \(B\): \((g/B)e^{-(M-\ln B)}=gt\). Choosing a larger source stock is not free preparation, nor does this assignment demonstrate an actual fuel chemistry.

For any retained reaction \(\alpha\rightleftharpoons\gamma\), set

\[
k_-=k_+\exp[\varphi\cdot(\gamma-\alpha)].
\tag{7}
\]

With \((n)_\alpha=\prod_s n_s!/(n_s-\alpha_s)!\), this implies

\[
\pi(n)k_+(n)_\alpha
=\pi(n+\gamma-\alpha)k_-(n+\gamma-\alpha)_\gamma,
\quad
\pi(n)\propto\frac{e^{-\varphi\cdot n}}{\prod_s n_s!}
\tag{8}
\]

on the conserved finite state class. Thus the **unstopped physical network** is locally and equilibrium detailed-balanced. Stopping flags and irreversible analyst records are not thermodynamic chemical states; no equilibrium claim is made for that augmented observation process. This is the standard ideal-dilute stochastic framework of [Rao and Esposito, J. Chem. Phys. 149, 245101](https://doi.org/10.1063/1.5042253), Eqs. 13–14, 41–42 and 51–54.

### Template-free formation and copying must have one equilibrium constant

For both types, the augmented formation channels are

\[
R+F\rightleftharpoons A_i+L_f,
\qquad
A_i+R+F\rightleftharpoons2A_i+L_f.
\tag{9}
\]

Their common net conversion is \(R+F\rightleftharpoons A_i+L_f\). The template is a catalyst, not an independent energy source. Both forward/reverse constant ratios must equal \(e^{4M}\). Their reverse propensities are respectively

\[
\sigma_i t^4A_iL_f,\qquad
\rho_i t^4A_i(A_i-1)L_f.
\tag{10}
\]

The second expression uses an ordered falling factorial; no extra one-half appears. Different \(\rho_i\) change forward and reverse catalytic kinetics together. Choosing an independent copying equilibrium constant would create an inconsistent catalyst-only cycle unless extra fuel/reservoir stoichiometry were added.

Catalytic fabrication likewise has

\[
A_i+R+F\rightleftharpoons A_i+G_i+L_f,
\qquad a^-_{{\rm fab},i}=\kappa_i t^4A_iG_iL_f.
\tag{11}
\]

The \(A_i\) cancels from its reaction affinity but remains in both kinetic propensities. There is no uncatalyzed gate-production channel added by this construction.

## 3. Complete added reverse propensities

Existing passive binding/dissociation rates are retained exactly. The new reverse propensities are:

| Original forward channel, with spent carrier added where required | New reverse propensity |
|---|---:|
| \(R\to C\) | \(atC\) |
| \(C\to D\) | \(btD\) |
| \(R+Y\to2Y\) | \(\beta tY(Y-1)\) |
| \(Y\to D\) | \(dtD\) |
| \(H_f+C\to F+C\) | \(gtFC\) |
| \(F\to L_f\) | \(\ell t^3L_f\) |
| \(D+F+C\to R+C+L_f\) | \(ktRCL_f\) |
| \(D+F+Y\to R+Y+L_f\) | \(k\theta tRYL_f\) |
| \(R+F\to A_i+L_f\) | \(\sigma_i t^4A_iL_f\) |
| \(A_i+R+F\to2A_i+L_f\) | \(\rho_i t^4A_i(A_i-1)L_f\) |
| \(A_i+R+F\to A_i+G_i+L_f\) | \(\kappa_i t^4A_iG_iL_f\) |
| \(A_i\to D\) | \(\eta_i tD\) |
| \(G_i\to D\) | \(\delta tD\) |
| \(GF_i\to G_i+L_f\) | \(\ell_bK_Ft^3G_iL_f\) |
| \(GF_i\to D+F\) | \(\delta K_FtDF\) |
| \(YG_i\to Y+D\) | \(\delta K_YtYD\) |
| \(YG_i\to G_i+D\) | \(dK_YtG_iD\) |
| \(R+YG_1\to Y+YG_1\) | \(\beta tY\,YG_1\) |

Rows indexed by \(i\) occur for both types. Together with their two passive binding pairs per type, there are 31 reversible pairs. Type 0 has no bound-reproduction pair in either direction; type 1 has both directions. The reverse of a catalyzed conversion has its same catalyst. Bound wear affinities include \(M-\ln K_F\) and \(M-\ln K_Y\); the factors \(K_F,K_Y\) therefore cannot be omitted from the error budget. Taking \(M>\max(0,\ln K_F,\ln K_Y)\) biases those channels forward.

## 4. Error bound over the entire stopped assay

Couple the original process to the reversible finite-source process, retaining source/spent counters on the original path as bookkeeping. Before its \(K\)-th forward capture, if \(j\le K-1\) captures have occurred,

\[
H_f=B-j,\qquad
U=F+GF_0+GF_1\le F_0+j,\qquad
L_f=1+F_0+j-U.
\tag{12}
\]

Here \(F_0=2\). Consequently define

\[
U_*=K+1,\qquad L_*=K+2.
\tag{13}
\]

For the eight-capture assay these are 9 and 10. The bounds include every original history before stopping, not merely the selected successful route. Fuel binding, dissociation and regulator wear do not change total available carrier \(U\); each expenditure produces \(L_f\).

While the copies agree, their capture-rate difference is

\[
gC-\frac gB(B-j)C=\frac{gjC}{B}
\le\frac{gN(K-1)}B.
\tag{14}
\]

This is a genuine depletion error, unlike the zero error in the old first-capture embedding. Couple captures at their common minimum, and treat the excess original capture clock as an unmatched event. Couple every other original channel and constituent-selection mark identically. Add the new reverse clocks only to the reversible process.

Let \(r_\mathrm{rev}^*\) bound their summed rate on the original pre-stop domain. The total unmatched hazard is at most

\[
\varepsilon_*:=\frac{gN(K-1)}B+r_\mathrm{rev}^*.
\tag{15}
\]

Until the first unmatched event, physical histories, entry states, type labels, capture counts and carrier-wear records coincide. For each joint branch event,

\[
|\widetilde J_i(T)-J_i(T)|
\le1-e^{-T\varepsilon_*}\le T\varepsilon_*.
\tag{16}
\]

This follows from the survival probability of the unmatched clock; no behavior after divergence is assumed. The event may require a full return and multiple wear marks, because the argument couples histories rather than only terminal states.

If \(J_0(T)-J_1(T)\ge\Delta>0\), then

\[
\widetilde J_0(T)-\widetilde J_1(T)
\ge\Delta-2(1-e^{-T\varepsilon_*})
\ge\Delta-2T\varepsilon_*.
\tag{17}
\]

The two errors concern two observables under one physical law, not separate source preparations for two interventions. Equation (17) is a sufficient conservative bound; it does not condition away the occurrence or cost of formation.

## 5. A usable reverse-rate envelope

Let \(P=\lfloor N^2/4\rfloor\) and \(P_b=\lfloor N^2/8\rfloor\). For N=4 these are 4 and 2. Products of two distinct single-backbone counts are at most P; a product of free Y and a two-backbone bound complex is at most \(P_b\). The table yields

\[
r_\mathrm{rev}^*\le c_1t+c_3t^3+c_4t^4,
\tag{18}
\]

with finite explicitly known coefficients

\[
\begin{aligned}
c_1={}&N(a+b+d+gU_*)+\beta N(N-1)
+kP L_*(1+\theta)+\beta P_b\\
&+\sum_{i=0}^1\left[
N\eta_i+N\delta+\delta K_FNU_*+(\delta+d)K_YP
\right],\\
c_3={}&\ell L_*+\sum_{i=0}^1\ell_bK_FNL_*,\\
c_4={}&L_*\sum_{i=0}^1\left[
N\sigma_i+N(N-1)\rho_i+P\kappa_i
\right].
\end{aligned}
\tag{19}
\]

The term \(\beta P_b\) is the type-1 bound-reproduction reverse. The original copying rates may differ; both are charged. The use of individual maxima is deliberately conservative; no simultaneous attainability is needed. The coefficient \(gNU_*\) is independent of \(B\) because of the potential/rate normalization in Eq. (6).

## 6. Explicit finite certificate for any certified strict comparison

Take a finite deadline T and a certified positive margin \(\Delta\), preferably a rational lower bound for exact arithmetic. Set

\[
B=\max\left\{K,\left\lceil
\frac{8TgN(K-1)}\Delta\right\rceil\right\}.
\tag{20}
\]

Write \(C_*=c_1+c_3+c_4\), and choose a positive integer M such that

\[
2^M\ge\max\left\{2,\ 2K_F,\ 2K_Y,
\frac{8TC_*}{\Delta}\right\}.
\tag{21}
\]

This is a finite constructive choice; for rational inputs it requires only integer comparisons, not a parameter search or fitted exponential. Since \(e>2\), \(t=e^{-M}<2^{-M}<1\), so

\[
r_\mathrm{rev}^*\le C_*t<\frac{\Delta}{8T},
\qquad
\frac{gN(K-1)}B\le\frac{\Delta}{8T}.
\tag{22}
\]

The binding-affinity condition also holds because \(K_Ft,K_Yt<1/2\). Therefore

\[
|\widetilde J_i(T)-J_i(T)|<\frac\Delta4,
\qquad
\boxed{\widetilde J_0(T)-\widetilde J_1(T)>\frac\Delta2>0.}
\tag{23}
\]

This supplies the required common-model bridge once the integrated formation-and-turnover proof supplies \(T,\Delta\) and the forward constants. It preserves any existing positive comparison without altering its forward reaction hierarchy, but the source stock and potentials are chosen for that fixed assay and error tolerance. It is not one fixed finite reservoir certified for arbitrarily many turnovers or arbitrarily long deadlines.

## 7. Instantiation with the full integrated comparison

The [integrated proof and its saved arithmetic](../../../../experiments/shared-renewal-capability/integrated-formation/exact-check.json) give

\[
T=27,\quad K=8,\quad
L=\frac1{808804024575624000000},\quad
\Delta=\frac L2=\frac1{1617608049151248000000},
\]

\[
m=\frac3L=2426412073726872000000,
\quad\beta=m,\quad\sigma_i=\mu=m^2,
\quad\kappa_i=k=m^3.
\tag{24}
\]

Copying rates are \(\rho_0=1,\rho_1=2\); all remaining positive constants are one. The original lower and upper bounds are \(J_0(27)\ge L\) and \(J_1(27)\le3/[2(1+m)]<L/2\). These concern formation plus full turnover, not the older first-capture event.

For these constants, Eq. (19) simplifies to

\[
c_1=80m^3+16m^2+14m+136,\qquad
c_3=90,\qquad
c_4=80m^3+80m^2+360.
\tag{25}
\]

Applying the explicit rules (20)–(21) gives

\[
\boxed{B=9783293481266747904000000,\qquad M=299.}
\tag{26}
\]

Both source stock and potentials are fixed before the run and are the same for the endogenous branches. In particular, the source potential is \(\varphi_{H_f}=1196-\ln B\); its initial population-dependent potential in the adopted normalization is 1196. These are selected standard-state parameters in \(k_BT\) units, not measured fuel values or heat-release estimates. The total finite carrier stock is \(B+3\).

The exact error certificate yields

\[
|\widetilde J_i(27)-J_i(27)|
<\frac\Delta4=\frac L8
=\frac1{6470432196604992000000}.
\tag{27}
\]

Consequently,

\[
\widetilde J_0(27)>\frac{7L}{8},\qquad
\widetilde J_1(27)<\frac{5L}{8},\qquad
\boxed{\widetilde J_0(27)-\widetilde J_1(27)>
\frac1{3235216098302496000000}.}
\tag{28}
\]

The [prospective algebraic protocol](../../../../experiments/shared-renewal-capability/integrated-thermo/PROTOCOL.md), [checker](../../../../experiments/shared-renewal-capability/integrated-thermo/exact_check.py) and [saved certificate](../../../../experiments/shared-renewal-capability/integrated-thermo/exact-check.json) preserve the inputs and exact arithmetic. The audit verifies both moiety invariants and all 31 potential/rate identities, the reverse and depletion envelopes on 38,133 bounded original pre-stop count states, and 232,507 enabled edge detailed-balance identities from those states. The general rate identity proves detailed balance beyond that enumerated subset; the full finite chemical state class with its enormous B was not enumerated. No simulation, matrix exponential, parameter fit or outcome search was performed.

The integrated proof, checker and source-result hashes were checked before and after the run and recorded in the new JSON. The new check uses their saved full-event margin but does not rerun or modify their files. The protocol was written before this audit's first execution; the original comparison and its extreme witness were already known, so this is not empirical preregistration or independent prediction of those outcomes.

## 8. Remaining physical and inferential limits

The reverse extension admits paths excluded by the irreversible proof: reverse wear can create A, G, C or Y from D, and reverse formation/recycling can recreate packets and precursors. The old no-template invariance, exact absence of gate production in certain states, and absorbing all-D boundary do not transfer literally. Their finite-time impact on this observable is charged by Eq. (16), including histories with Y extinction. The old irreversible upper bound is used for its own model and then perturbed; it is not reproved by asserting the same impossible paths remain impossible.

The return is to the same **core** count/type state, not to the complete chemical source state. On the selected forward route, entry has \(H_f=B-2,L_f=3\), whereas the eighth-capture return has \(H_f=B-8,L_f=9\). Source and spent-carrier coordinates must be retained when predicting another excursion. The old identical-return kernel cannot therefore be iterated as if the reservoir reset itself. Likewise, the old six-capture minimum is a result for its irreversible ledger; adding reverse fuel-producing channels does not make that minimum a thermodynamic law. The present assay explicitly fixes its eighth forward capture as the assessed return.

The finite closed chemical system has equilibrium detailed balance. It is not a chemically maintained nonequilibrium steady state, and the result says nothing about indefinite replacement, eventual absorption, stationary useful-type prevalence or universal generative direction. More charged fuel permits a longer experiment; it does not give a finite stock an infinite lifetime. An open maintained source would need an explicit chemostat work account and different long-time analysis.

The work-equivalent \(W=N-D+U\) remains the assay's assigned ledger, not the chemical free energy. Some zero-W-increment reactions dissipate free energy, and some reverse fluctuations increase W. The initial precursor states and charged reservoir contain declared nonequilibrium resources, shared by both branches. Their preparation/reset cost is not proved repaid by the branch comparison.

Actual molecular structures, matching catalyst specificity, source/waste chemistry, rate magnitudes, spatial mixing and elimination of intermediate states remain unidentified. A common potential assignment removes an affinity contradiction; it does not make the fast fabrication, copying, recycling or association hierarchy physically achievable. If molecular mechanisms introduce additional channels or rate errors, their unmatched hazards or a justified coarse-graining error must fit within the remaining margin. Observation of the tagged turnover event also needs a separately costed measurement implementation.

## Provenance

Read the original material-fabricator proposal and its review, the earlier reversible proof and its exact audit, and the complete [integrated formation-and-turnover note](INTEGRATED-FORMATION-RENEWAL.md) with its saved result. The thermodynamic formulas use the previously inspected [Rao–Esposito published-version manuscript](https://arxiv.org/pdf/1805.12077v2), SHA-256 `b50ad25234f782e08d8c15480df1ca8fe1c30734ec697d403795bda032b37dd9`; no new empirical source is claimed. This note supplies a new algebraic embedding and error bound instantiated from the integrated comparison's own margin. Existing models and shared indexes were not edited.
