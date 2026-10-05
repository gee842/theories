# A reversible thermodynamic embedding of the paid allocation theorem

5 October 2026. AI-authored conditional construction and proof, continuing the repository at `348d82644a92315a0ea415a9edc44708e27ad516`. This addresses the reaction-law gap in [ALLOCATION-CONTROL.md](ALLOCATION-CONTROL.md); it does not identify chemistry, fit rates, or alter that theorem's original network. The [resource-allocation baseline](RESOURCE-ALLOCATION-BASELINE.md) remains the conventional biological comparison.

**Result.** The allocation witness admits a finite, reversible mass-action extension satisfying local detailed balance, with an explicit source carrier, spent carrier and standard chemical potentials. A coupling bound transfers the existing first-capture comparison to this extension. At the declared potential scale, its construction-disabled success probability is below 0.068707 and its constructed success probability is above 0.112345, preserving the common reliability threshold 0.1. These are certified bounds within a formal thermodynamic model, not measured probabilities or evidence that the required molecular specificity and rates are attainable.

The construction is a finite chemical system in an isothermal bath, relaxing toward equilibrium. It does not require an infinite chemical reservoir during this particular assay and does not establish sustained operation. Reverse reactions remove several exact absorbing boundaries of the old network.

## 1. Thermodynamic requirements and source scope

For an ideal dilute stochastic reaction network, chemical thermodynamics constrains forward/reverse ratios, not just material balance. The relevant primary framework is Rao and Esposito, [*Conservation laws and work fluctuation relations in chemical reaction networks*](https://doi.org/10.1063/1.5042253), J. Chem. Phys. 149, 245101 (2018), particularly the stochastic mass-action law, equilibrium weights, and local detailed balance in Eqs. 13–14, 41–42 and 51–54. Their [published-version author manuscript](https://arxiv.org/abs/1805.12077v2) was read in those sections. Their earlier [PRX framework](https://doi.org/10.1103/PhysRevX.6.041064), especially Eqs. 18–20 and 48–50, explains how reservoir exchanges supply cycle affinities. The finite construction and perturbation proof below are our derivation, not results claimed in either source.

Use the original unit-volume count convention. Absorb the fixed reference-concentration and volume factors into dimensionless standard potentials \(\varphi_i\), measured in \(k_BT\) units. This convention makes the reference population activity one. A reactant complex \(\alpha\) has stochastic multiplicity

\[
(n)_\alpha=\prod_i\frac{n_i!}{(n_i-\alpha_i)!},
\]

zero if an input is missing. For a reversible channel \(\alpha\rightleftharpoons\gamma\), choose

\[
\frac{k_+}{k_-}=\exp[-\varphi\cdot(\gamma-\alpha)].
\tag{1}
\]

The finite-state equilibrium weights are then

\[
\pi(n)\propto\frac{e^{-\varphi\cdot n}}{\prod_i n_i!},
\qquad
\Phi(n)=\varphi\cdot n+\sum_i\log(n_i!).
\tag{2}
\]

For every enabled transition \(n'=n+\gamma-\alpha\),

\[
\log\frac{k_+(n)_\alpha}{k_-(n')_\gamma}
=-[\Phi(n')-\Phi(n)],
\qquad
\pi(n)k_+(n)_\alpha=\pi(n')k_-(n')_\gamma.
\tag{3}
\]

The factorial ratio is essential at low copy number. In particular, the reverse of \(R+Y\to2Y\) has multiplicity \(Y(Y-1)\), not \(Y^2\). There is no additional factor of one half in this falling-factorial convention. A binomial convention would require a corresponding factor of two in its rate constant.

The original work-equivalent \(W\) is not \(k_BT\Phi\). A zero change in \(W\) neither requires zero affinity nor makes an arbitrarily chosen set of reverse constants consistent. Equation (1) enforces a single potential assignment across all channels and therefore the cycle constraints automatically.

## 2. Two explicit fuel-carrier states

Add \(H_f\), an available high-potential carrier, and \(L_f\), its spent form. They are finite-count species, not clamped chemostats in the construction below. Interpret \(F\) as a transferable intermediate state of this carrier. Keep the backbone material forms as distinct states of a conserved material moiety; \(GF\) contains one backbone and one carrier, while \(YG\) contains two backbones.

Replace capture by

\[
H_f+C\rightleftharpoons F+C.
\tag{4}
\]

Every original event that consumed a free or bound packet now produces one \(L_f\):

\[
F\rightleftharpoons L_f,\qquad
D+F+C\rightleftharpoons R+C+L_f,\qquad
D+F+Y\rightleftharpoons R+Y+L_f,
\]

\[
R+F\rightleftharpoons G+L_f,\qquad
GF\rightleftharpoons G+L_f.
\tag{5}
\]

The reverse directions will be rare but positive. All remaining original material changes are also made reversible. Retain the two existing binding pairs unchanged. The allocation architecture has \(\zeta=0\): the bound-reproduction channel is absent in **both** directions, and \(YG\) does not catalyze recycling. This is an assumed kinetic specificity. Detailed balance allows omission of a channel pair; it does not establish that a molecule has that specificity.

Both arms receive the same extended preparation

\[
(R,C,Y,D,F,G,GF,YG)=(2,0,1,0,1,0,0,0),
\qquad H_f=L_f=1.
\tag{6}
\]

Two exact conserved quantities are

\[
N=R+C+Y+D+G+GF+2YG=3,
\qquad
Q_f=H_f+L_f+F+GF=3.
\tag{7}
\]

There are only 512 nonnegative count states with these totals. Nonexplosion is immediate. This supplies stoichiometric moiety conservation, not a chemical-structure identification or a proof that all the proposed catalytic transitions are elementary reactions.

## 3. A compatible potential assignment and all reverse rates

Write

\[
K_F=\frac{\alpha_b}{\rho},\qquad
K_Y=\frac{\mu}{\nu},
\]

in the normalized count convention above. Fix a finite positive parameter \(M\), unrelated to the cellular mass in the Weiße baseline, and set

\[
\begin{array}{c|cccccccccc}
i&D&L_f&C&Y&G&R&F&H_f&GF&YG\\\hline
\varphi_i&0&0&M&M&M&2M&3M&4M&4M-\ln K_F&2M-\ln K_Y.
\end{array}
\tag{8}
\]

Thus the original passive binding constants satisfy Eq. (1) exactly. Let \(t=e^{-M}\). The remaining channels, their unchanged forward propensities, and their new reverse propensities are:

| Forward channel | Forward propensity | Reverse propensity at the current state |
|---|---:|---:|
| \(R\to C\) | \(aR\) | \(atC\) |
| \(C\to D\) | \(bC\) | \(btD\) |
| \(R+Y\to2Y\) | \(\beta RY\) | \(\beta tY(Y-1)\) |
| \(Y\to D\) | \(dY\) | \(dtD\) |
| \(H_f+C\to F+C\) | \(gH_fC\) | \(gtFC\) |
| \(F\to L_f\) | \(\ell F\) | \(\ell t^3L_f\) |
| \(D+F+C\to R+C+L_f\) | \(kFDC\) | \(ktRCL_f\) |
| \(D+F+Y\to R+Y+L_f\) | \(k\theta FDY\) | \(k\theta tRYL_f\) |
| \(R+F\to G+L_f\) | \(\kappa RF\) | \(\kappa t^4GL_f\) |
| \(G\to D\) | \(\delta G\) | \(\delta tD\) |
| \(GF\to G+L_f\) | \(\ell_b GF\) | \(\ell_bK_Ft^3GL_f\) |
| \(GF\to D+F\) | \(\delta GF\) | \(\delta K_FtDF\) |
| \(YG\to Y+D\) | \(\delta YG\) | \(\delta K_YtYD\) |
| \(YG\to G+D\) | \(dYG\) | \(dK_YtGD\) |

The two additional pairs remain \(G+F\rightleftharpoons GF\), with propensities \(\alpha_bG\,F\) and \(\rho GF\), and \(G+Y\rightleftharpoons YG\), with propensities \(\mu G\,Y\) and \(\nu YG\). In an association propensity, \(G\,F\) denotes the product of free counts; in a dissociation propensity, \(GF\) denotes the complex count. The checker uses separate species keys to avoid this typographical ambiguity.

Every constant follows from Eq. (8), rather than being independently suppressed. For example, the standard forward affinities of free wear, wear in \(GF\), and wear of either constituent in \(YG\) are respectively \(M\), \(M-\ln K_F\), and \(M-\ln K_Y\). Therefore require

\[
M>\max(0,\ln K_F,\ln K_Y)
\tag{9}
\]

to bias all the formerly one-way channels forward. Large binding affinity increases the reverse bound-wear constants relative to free wear; the factors \(K_F,K_Y\) cannot be discarded.

There is no zero-cost cycle contradiction. The material cycle \(R\to C\to D\to R\) consumes \(F\) and produces \(L_f\), with standard affinity \(3M\). Capture followed by leakage converts \(H_f\) to \(L_f\), with affinity \(4M\). When carrier states are included, a complete closed-state cycle has zero summed potential change. At finite \(M\), all retained channel pairs satisfy Eq. (3), and the finite system has the equilibrium weights in Eq. (2). A transient prepared far from equilibrium can nevertheless produce the required delivery before relaxation.

For the construction-disabled arm, remove **both** directions of the construction pair. Removing a detailed-balanced pair preserves Eq. (3) for every remaining pair. Other reverse reactions, notably \(D\to G\), can still create gate material. Consequently this arm approximates the old exactly gate-free reference on the finite assay; it is not exactly gate-free forever. Its rare new paths are included in the perturbation bound.

## 4. Why one source carrier is sufficient for this assay

Retain the original event: the first forward capture before deadline \(h\), with \(C\ge1\) and \(Y+YG\ge1\) at that jump. A reverse leakage/recycling/construction event that produces \(F\) is not counted as a new source capture. Reaction labels remain observable labels in the mathematical assay.

Stop at the first forward capture, marking success or failure according to total Y. Before that stopping time, an original one-way path has

\[
U=F+GF\le1,\qquad H_f=1,\qquad L_f=2-U\in\{1,2\}.
\tag{10}
\]

Only the initial packet can have been spent. Thus the new forward capture propensity \(gH_fC\) is **exactly** \(gC\) until the original assay stops. All other original forward and binding rates are also unchanged. The enlarged one-way process and the old stopped process therefore have identical core laws. There is no approximation from source depletion before the first capture.

This equality is specific to the stopped assay. After that capture the finite source is depleted, while the old process could receive more incident support. Nothing here equates their unrestricted trajectories, incident-photon statistics, later capture counts or long-run lifetimes. A multiple-capture or turnover-cycle assay needs a larger common charged inventory and a quantified source-depletion error, together with a new bound on reverse rates over its larger reachable domain. An open-source model with clamped carriers would instead require chemical work to maintain their potentials; that is a different thermodynamic boundary condition.

## 5. Finite-horizon perturbation theorem

Let \(X^i\) be the enlarged original process in arm \(i\), stopped at its first forward capture, and let \(\widetilde X^i\) be its reversible extension. Let \(\tau\) denote that capture time along the original path. On the finite pre-capture states in Eq. (10), let \(r_i(x)\) be the sum of all **new** reverse propensities. Do not include the two passive dissociation channels already present in the original process. If

\[
\sup_{x\text{ satisfying (7),(10)}}r_i(x)\le r_i^*,
\]

then

\[
\left|\Pr(\widetilde X^i\in\mathcal E_h)
-\Pr(X^i\in\mathcal E_h)\right|
\le1-\mathbb E\exp\!\left[-\int_0^{h\wedge\tau}r_i(X^i_s)\,ds\right]
\le1-e^{-hr_i^*}\le hr_i^*.
\tag{11}
\]

**Proof.** Use identical original reaction clocks while the two copies agree, adding independent state-dependent clocks for the new reverses. Until the first new reverse fires, both copies have the same core path, carrier counts and capture label. Given an original path, the survival probability of that extra clock is the exponential in Eq. (11). If it never fires before the assay stops or the deadline, the event indicators agree. A first new event may or may not change the outcome, which gives the first inequality. Uniform bounding of the integrated hazard gives the remaining inequalities. No claim about trajectories after divergence is needed. ∎

If the original gate-reference probability gap has certified lower bound \(m>0\), its sign persists whenever

\[
(1-e^{-hr_0^*})+(1-e^{-hr_1^*})<m.
\tag{12}
\]

The sufficient linear criterion is \(h(r_0^*+r_1^*)<m\). This is a precise rate-error criterion, not merely continuity without a usable radius. It also handles additional approximate forward rates by coupling common rates at their minimum and adding \(\sum_j|\widetilde a_j-a_j|\) to the unmatched-event hazard. Hidden-intermediate implementations require a separate justified reduction; adding their names alone does not supply that bound.

Small imperfect inhibition can be included similarly. If the omitted bound-reproduction pair is restored with forward coefficient \(\zeta\beta\), local detailed balance requires reverse coefficient \(\zeta\beta t\). On the pre-capture material class, \(R\,YG\le1\) and \(Y\,YG\le1\), so an additional mismatch envelope is \(\zeta\beta(1+t)\). Strict inequalities in Eq. (12) therefore permit a nonzero interval of imperfect blockade. They do not imply that the interval is experimentally attainable.

## 6. Exact witness and finite error budget

Use the unchanged forward witness from ALLOCATION-CONTROL, Eq. 21:

\[
a=b=d=\delta=\nu=1,\quad g=4,\quad
\ell=\ell_b=141,\quad\beta=3384,\quad
\kappa=162432,\quad\mu=159189,
\]

\[
k=1,\quad\theta=4,\quad\alpha_b=4,\quad\rho=1.
\tag{13}
\]

Then \(K_F=4\), \(K_Y=159189\). For either arm, the reverse table and the pre-capture constraints yield

\[
r_i(x)\le A t+B t^3+C_*t^4,
\tag{14}
\]

where

\[
\begin{aligned}
A&=3(a+b+d+g+\delta)+6\beta+4k(1+\theta)
+3\delta K_F+2(\delta+d)K_Y=657116,\\
B&=2\ell+6\ell_bK_F=3666,\\
C_*&=6\kappa=974592.
\end{aligned}
\tag{15}
\]

For example, \(Y(Y-1)\le6\), \(RC,RY,YD,GD\le2\), \(FC,DF\le3\), and \(L_f\le2\). These individually conservative bounds need not be simultaneously attained. They apply to all original pre-capture states, including those with no Y; reverse seeding after extinction is not omitted.

Choose \(M=20\), fixed in the [protocol](../../../../experiments/shared-renewal-capability/thermo-embedding/PROTOCOL.md) before executing the new checker. This is an algebraic witness chosen after the old probability bounds were known, not a parameter fit or an outcome-blind empirical prediction. The exact exponential-series bound is

\[
e^5>\sum_{j=0}^{7}\frac{5^j}{j!}=\frac{2701}{21}>128,
\qquad t=e^{-20}<2^{-28}.
\]

This also verifies Eq. (9). Exact rational arithmetic gives

\[
r_i^*<\frac{657116}{2^{28}}+
\frac{3666}{2^{84}}+\frac{974592}{2^{112}}
<\frac1{400}.
\tag{16}
\]

At the original deadline \(h=3\), each event-probability error is therefore strictly below \(3/400\). Applying this to the original analytical bounds gives

\[
\boxed{
\Pr_{\rm disabled}^{\rm rev}(\mathcal E_3)
<\frac{6769}{110592}+\frac3{400}
=\frac{189961}{2764800}<\frac1{10},
}
\]

\[
\boxed{
\Pr_{\rm constructed}^{\rm rev}(\mathcal E_3)
>\frac{2209}{18432}-\frac3{400}
=\frac{51769}{460800}>\frac1{10}.
}
\tag{17}
\]

The resulting guaranteed difference is

\[
\boxed{
\Pr_{\rm constructed}^{\rm rev}(\mathcal E_3)
-\Pr_{\rm disabled}^{\rm rev}(\mathcal E_3)
>\frac{120653}{2764800}>0.
}
\tag{18}
\]

The [exact checker](../../../../experiments/shared-renewal-capability/thermo-embedding/exact_check.py) and [saved result](../../../../experiments/shared-renewal-capability/thermo-embedding/exact-check.json) verify the two conserved moieties, all 16 reaction pairs, 1,915 enabled detailed-balance edges across 512 states, and the reverse-hazard envelope on 96 pre-capture states in each arm. They use exact rational coefficients and monomial exponents in \(t\); no trajectory simulation, fitting, numerical matrix exponential or rate search was performed. The disabled arm's removal of the construction pair preserves the checked edgewise identities for all its remaining channels.

## 7. What has and has not been physically established

This closes one formal gap: the positive finite-time allocation event is robust to a specified thermodynamically consistent reversal of the effective network. A naked irreversible reaction table is not thereby a complete thermodynamic description. The extension specifies extra carrier states, their finite initial stocks, chemical potentials and reverse propensities. Backbone precursors and the initial packet are also a prepared nonequilibrium resource; both arms receive the same preparation.

The potential assignment is not an equality between \(W\) and actual available work. For example, \(R\to C\) has zero \(\Delta W\) but standard free-energy drop \(Mk_BT\); binding also changes free energy while leaving that ledger unchanged. Standard potentials plus mixing specify the equilibrium free-energy structure. Separating heat from molecular enthalpy and entropy requires additional thermochemical information. At \(M=20\), the chosen standard difference between \(H_f\) and \(L_f\) is \(80k_BT\); this is a finite declared resource scale, not a measured packet value or a minimal energy requirement.

Several earlier exact statements **do not transfer**. Reverse wear can recreate C, Y and G from D; reverse recycling/construction can recreate packets and precursors. The old all-D/no-fuel state is therefore not absorbing in this extension, and the old absorption proof and irreversible opportunity-loss statement do not describe its infinite-time behavior. Its closed chemical dynamics is detailed-balanced at equilibrium, not an ongoing chemically driven nonequilibrium steady state. Equation (11) transfers the stated finite-time event, not indefinite persistence, the old early-time cubic coefficient, whole capability regions or every preparation. In particular it does not upgrade the original net comparison from S to the earlier preparation \(x_0\).

The following empirical obligations remain:

- Chemical structures and mechanisms must realize the assumed material forms, carrier exchange and selective suppression of reproduction/recycling by binding. Specifying standard potentials does not supply these structures.
- Achievable diffusion, association, fabrication and dissociation rates must permit the forward hierarchy. Local detailed balance constrains ratios but does not certify those absolute rates or independent tunability of barriers.
- If the listed third-order or lumped events hide intermediates, their elimination must preserve the event law within a stated error. Extra states, side reactions and spatial effects can consume the error budget.
- A physical source, sink and preparation process must deliver the specified finite stocks/potentials at the declared temperature and volume. Their preparation and reset cost is not demonstrated by the autonomous run.

The conclusion is an existence-and-robustness theorem within ideal stochastic chemical thermodynamics. It is stronger than material bookkeeping alone and weaker than a realizable molecular design, calibrated kinetics, experimental validation or spontaneous discovery of the architecture.

## Source and calculation provenance

Primary-source downloads were read in temporary storage; no external messages were sent. The 2018 author manuscript PDF from [arXiv](https://arxiv.org/pdf/1805.12077v2) has 30 pages, 971,982 bytes and SHA-256 `b50ad25234f782e08d8c15480df1ca8fe1c30734ec697d403795bda032b37dd9`. Reading focused on the stochastic rates, equilibrium distribution, local detailed balance, and reservoir-work discussion; the fluctuation-theorem proofs were not independently audited. The 2016 manuscript from [arXiv](https://arxiv.org/pdf/1602.07257) has 22 pages, 997,150 bytes and SHA-256 `ed86193f16e3df2561a52fda55bfc63ba6086969494520122485193d9fce77d1`; the closed/open network, cycle and affinity sections were inspected. Both were retrieved 5 October 2026.

The check protocol precedes its first execution. Its SHA-256 is `30705808c424850c0c3ead30d3133ffef638997d999e94a8409a82465bc52894`; the checker SHA-256 is recorded in the result JSON. The original source theorem and its independent review supply the original probability bounds; the new checker verifies the embedding algebra and their error-adjusted inequalities. These checks establish internal consistency under the stated laws, not empirical feasibility.
