# Formation and full carrier turnover under one common reaction law

5 October 2026. AI-assisted continuation from commit `f81afc0`. This note uses exactly the N=4 material-fabricator generator in [Architecture formation](ARCHITECTURE-FORMATION-CRITIQUE.md), with a declared parameter class. It adds no reaction, selected intervention or external reset. The [N=3 return study](../../../history/2026-10-05-support-and-shared-generativity/completion/RENEWAL-RETURN.md) supplies the earlier repair idea, but its probabilities are not transferred to this different generator.

**Result and limit.** One autonomous finite-rate model can form fabrication and gating capability from their absence, deliver captured support, and replace every original A, C, G and Y carrier while returning to the same supported state. Six fresh packets are necessary and attainable for full turnover in the assigned work ledger; formation adds two. There is a strict comparison between the two endogenous formation branches for this same complete joint event, rather than only for an earlier delivery event.

The explicit certificate is extremely conservative: its favorable-branch probability lower bound is about **1.24 × 10⁻²¹**, and the sufficient parameter witness has m about **2.43 × 10²¹**, with some rates scaling as m³. This proves consistency and a nonempty finite-rate mathematical class. It supplies no achievable molecular rate bounds, likely renewal, empirical realization, overall architecture prevalence or universal direction. The incident source and the allowed reaction repertoire remain supplied assumptions.

## 1. Retained law and an identical joint assay for both branches

Use species

\[
(R,C,Y,D,F,A_0,A_1,G_0,G_1,GF_0,GF_1,YG_0,YG_1).
\]

All reactions, including competing formation and copying, are the unchanged architecture law. In particular,

\[
R+F\xrightarrow{\sigma_i}A_i,\qquad
A_i+R+F\xrightarrow{\rho_i}2A_i,\qquad
A_i+R+F\xrightarrow{\kappa_i}A_i+G_i,
\]

with mass-action propensities \(\sigma_iRF,\rho_iA_iRF,\kappa_iA_iRF\). Fabricators wear to D at rate \(\eta_iA_i\). There is no uncatalyzed gate fabrication. Type 0 binding suppresses Y reproduction, \(\zeta_0=0\); type 1 binding retains it, \(\zeta_1=1\). Bound Y of either type cannot recycle. All other original plant, binding, leakage and wear channels remain active where their reactants are present.

The common preparation and selected entry state are

\[
Z_0:\ R=3,Y=1,F=2;
\qquad P_{00}=P_4:\ A_0=C=YG_0=1,F=2.
\tag{1}
\]

Unlisted species are zero. Both have N=4 and W=6, for

\[
N=R+C+Y+D+\sum_i(A_i+G_i+GF_i+2YG_i),\quad
U=F+\sum_iGF_i,\quad W=N-D+U.
\tag{2}
\]

To avoid building an A0 preference into the target, let \(\mathcal P\) contain all states \(P_{ij}\) with \(A_i=C=YG_j=1,F=2\), everything else zero. Define the **same** event \(E_H^{\rm full}\) for every trajectory:

1. At the second fresh capture, enter some \(P_{ij}\in\mathcal P\).
2. Mark the A, C, G and Y functional carriers present at that entry.
3. At the eighth fresh capture, by time H, return to that same count/type state \(P_{ij}\), after each of those four marked carriers has undergone its wear reaction.

This is a hitting and fresh-delivery event. It does not require survival after the eighth capture until H. Initial packets are not fresh captures. Material can be recycled after a carrier wears; replacement of functional carriers does not require replacement of their constituent atoms. The marks distinguish an old carrier from a newly assembled one and do not affect any propensity. An experimental readout would need its own observation and resource account.

Let I=i mean that the first actual reaction from Z0 forms Ai. The quantities compared are

\[
J_i^{\rm full}(H)=\Pr_{Z_0}(I=i,E_H^{\rm full}).
\tag{3}
\]

Both branches, competing first reactions and every later failure belong to one law. These are unconditional branch contributions, not an intervention contrast or architectural prevalence. The exhibited successful route uses \(P_{00}\); the target also permits the other types.

The process stopped at the eighth capture is finite-state after adding its capture counter, entry type and finite carrier marks: before that capture U≤9, and at the stopping jump U≤10. Material N stays four. Its success probability is therefore an ordinary finite stopped-generator quantity. No overflow truncation is necessary for this particular capped assay.

## 2. An actual path replacing all four entry carriers

The six-event formation route is unchanged:

\[
\text{form }A_0,\quad\text{fabricate }G_0,\quad\text{bind }Y,
\quad R\to C,\quad\text{capture},\quad\text{capture}.
\tag{4}
\]

It spends the two initial packets on A and G formation, and captures two new packets before entering P4. No wear or leakage occurs on this selected route; their hazards are still charged to its probability.

The following 21 events then return to P4. For readability, table states use only \((R,C,Y,D,F,A_0,G_0,YG_0)\); all other species are zero on this selected path. A0, A1 and gate-type competitors remain available in the law and its exit rates.

| Step | Existing reaction | State after the event |
|---:|---|---|
| 1 | Original A0 wears | (0,1,0,1,2,0,0,1) |
| 2 | C-catalyzed recycling | (1,1,0,0,1,0,0,1) |
| 3 | Template-free A0 formation | (0,1,0,0,0,1,0,1) |
| 4 | Capture | (0,1,0,0,1,1,0,1) |
| 5 | Original C wears | (0,0,0,1,1,1,0,1) |
| 6 | YG0 dissociates | (0,0,1,1,1,1,1,0) |
| 7 | Y-catalyzed recycling | (1,0,1,0,0,1,1,0) |
| 8 | Y binds G0 | (1,0,0,0,0,1,0,1) |
| 9 | R assembles into C | (0,1,0,0,0,1,0,1) |
| 10 | Capture | (0,1,0,0,1,1,0,1) |
| 11 | Original G0 wears in YG0 | (0,1,1,1,1,1,0,0) |
| 12 | C- or Y-catalyzed recycling | (1,1,1,0,0,1,0,0) |
| 13 | Free Y reproduces | (0,1,2,0,0,1,0,0) |
| 14 | Capture | (0,1,2,0,1,1,0,0) |
| 15 | Capture | (0,1,2,0,2,1,0,0) |
| 16 | Tagged original Y wears | (0,1,1,1,2,1,0,0) |
| 17 | C- or Y-catalyzed recycling | (1,1,1,0,1,1,0,0) |
| 18 | A0 fabricates G0 | (0,1,1,0,0,1,1,0) |
| 19 | Y binds G0 | (0,1,0,0,0,1,0,1) |
| 20 | Capture | (0,1,0,0,1,1,0,1) |
| 21 | Capture | P4 |

The two recycling channels in steps 12 and 17 have the same state update, so their propensities can be added. In step 16 the original Y is only one of two free constituents. In the exchangeable tagged realization its selected wear intensity is d, while total Y wear remains 2d in the exit intensity. The count law is unchanged. Merely counting one Y wear would not establish the required original-Y replacement.

The timing of fuel use is essential. A replacement starts with two packets and spends both before replenishing only one. This leaves precisely one packet for C repair, so recycling exhausts fuel before C assembly and disables competing fuel-driven construction. During Y succession two packets are captured **before** the worn Y is recycled. The recovered R can then go directly into gate construction; it is not left competing with reproduction while awaiting another capture. The route requires finite reaction races throughout and includes no controller that orders them.

Reproduction is useful in step 13 and destructive to C repair in step 8. Its regulation is consequently specific to the material state, not a universal advantage of suppressing reproduction.

## 3. Exact minimum capture budget

For any P4-to-P4 return, the W balance is

\[
K_{\rm cap}=K_{\rm leak}+K_{\rm ble\!ak}
+B_A+B_G+D_A+D_G+D_C+D_Y,
\tag{5}
\]

where B counts births or fabrication and D counts constituent wear. Copying counts as an A birth. Total A and gate counts return, so \(B_A=D_A\) and \(B_G=D_G\). Wearing each of the four marked entry carriers requires \(D_A,D_G,D_C,D_Y\ge1\). Therefore

\[
\boxed{K_{\rm cap}\ge2+2+1+1=6.}
\tag{6}
\]

The displayed path attains six, with four recyclings, one A birth, one G birth and exactly one wear in each role. Its fuel balance is \(6-4-1-1=0\); its W balance is \(6-4-2=0\). Formation from Z0 adds one A birth and one G birth before recovering W=6, so the combined minimum is **eight fresh captures**. The selected 27-event path attains it.

This is a minimum within the assigned packet/work ledger. It is not a calibrated lower bound on chemical free energy or dissipation. Supplying six or eight packets also does not by itself ensure their capture, timing or successful allocation.

## 4. Derived kernels and safe continuation

For either selected path, let \(r_j\) be its chosen reaction intensity and \(\lambda_j\) the sum of **all** available reaction intensities at the pre-event state. A tagged old-Y wear uses r=d and still includes both Y wears in lambda. The exact path-time subprobability kernel is

\[
K(dt)=\mathop{*}_j[r_j e^{-\lambda_jt}\,dt].
\tag{7}
\]

Let F be the six-step formation kernel and K the 21-step turnover kernel. Then

\[
J_0^{\rm full}(H)\ge(F*K)([0,H]).
\tag{8}
\]

Every alternative exit is included in lambda. It is excluded from this particular sufficient route, not erased from the process or asserted to be globally unsuccessful. The exact kernels generally are not exponential, so no inverse mean time is substituted for a Markov regime-transition rate.

Upon actual return to P4, the autonomous count process has the same law conditional on its full entry history, provided the stipulated constants and support are time-homogeneous. Exchangeability gives the same tagged continuation law when the currently present carriers are marked for the next assay. No physical state is reset and the marks are not actor input. Thus the selected probability of entry and n specified turnovers by total time H is

\[
(F*K^{*n})([0,H]).
\tag{9}
\]

With separate deadlines, \(F([0,t_0])K([0,t_1])^n\) is a lower bound for completion by \(t_0+nt_1\). This is a genuine P1-compatible continuation certificate at a specified full state. It does not attach a continuation guarantee to every trajectory that merely captures energy, and it does not imply likely or infinite repetition. With a finite depleting source or aging state, that additional state must be retained and the bound must be re-established uniformly; the fixed-source return kernel cannot be reused silently.

## 5. A strict comparison for the complete event

### Necessary earlier access bounds the whole competing branch

The earlier A1 obstruction still applies to this stronger event. After first forming A1 from Z0, only one packet remains. Before first C assembly there is no capture. A0 formation and subsequent G0 fabrication need two packets, so the blocking gate cannot yet be produced. While any Y remains, C-versus-Y allocation has conditional C probability at most \(a/(a+\beta)\). At most three such allocations are possible: two initial R units and at most one packet-funded recycling. Y extinction permanently defeats the full event.

With equal formation rates, therefore,

\[
J_1^{\rm full}(H)\le
\frac{6\sigma}{12\sigma+3a+3\beta+d+2\ell}
\min\!\left\{1,\frac{3a}{a+\beta}\right\}.
\tag{10}
\]

This bounds a necessary part of the same complete event. It allows all later architecture changes and all later successful repair routes; it does not claim they are impossible after the first capture.

### A finite sufficient rate class preserves the entire favorable route

In the declared unit setting take

\[
\beta=m,\quad\sigma_0=\sigma_1=\mu=m^2,
\quad\kappa_0=\kappa_1=k=m^3,\qquad m\ge1.
\tag{11}
\]

Set all remaining constants to one except fabricator-copy rates \(\rho_0=1,\rho_1=2\); retain \(\zeta_0=0,\zeta_1=1\). Fuel dissociation has unit rate, denoted omega in the checker to distinguish it from fabricator copying. No rate changes during a trajectory. The stronger recycling scale matters: after C wears and Y dissociates, recycling must have a nonvanishing chance against rapid rebinding. The earlier first-delivery parameter hierarchy alone does not guarantee this.

Each selected intensity is \(r_j(m)=c_jm^{p_j}\). The complete exit intensity is a polynomial in m with nonnegative coefficients and degree at most \(p_j\). Consequently, for m≥1,

\[
\frac{r_j(m)}{\lambda_j(m)}\ge
\frac{r_j(1)}{\lambda_j(1)}.
\tag{12}
\]

Here is the full hazard check; the turnover numbering matches the preceding table. All inactive species still have their channels in the generator, with zero reactant-dependent propensity.

| Phase | Selected rate r | Complete exit intensity lambda |
|---|---:|---:|
| Formation 1 | 6m² | 12m²+3m+6 |
| Formation 2 | 2m³ | 2m³+4m²+2m+7 |
| Formation 3 | m² | m²+m+4 |
| Formation 4 | 1 | 5 |
| Formation 5 | 1 | 6 |
| Formation 6 | 1 | 7 |
| Turnover 1 | 1 | 8 |
| Turnover 2 | 2m³ | 2m³+7 |
| Turnover 3 | m² | 2m²+7 |
| Turnover 4 | 1 | 6 |
| Turnover 5 | 1 | 7 |
| Turnover 6 | 1 | 5 |
| Turnover 7 | m³ | m³+m²+5 |
| Turnover 8 | m² | m²+m+4 |
| Turnover 9 | 1 | 5 |
| Turnover 10 | 1 | 6 |
| Turnover 11 | 1 | 7 |
| Turnover 12 | 2m³ | 2m³+5 |
| Turnover 13 | m | m+5 |
| Turnover 14 | 1 | 5 |
| Turnover 15 | 1 | 6 |
| Turnover 16 | 1 | 7 |
| Turnover 17 | 4m³ | 4m³+6 |
| Turnover 18 | m³ | m³+2m²+m+7 |
| Turnover 19 | m² | m²+5 |
| Turnover 20 | 1 | 6 |
| Turnover 21 | 1 | 7 |

The exact uniform race products are

\[
R_F=\frac1{33075},\qquad
R_K=\frac1{18340227314640000}.
\tag{13}
\]

Every displayed lambda is at least five. Requiring each of 27 holding intervals to finish within H/27 gives, for every m≥1,

\[
J_0^{\rm full}(H)\ge
R_FR_K\left(1-e^{-5H/27}\right)^{27}>0.
\tag{14}
\]

The right side is independent of m. Meanwhile (10) tends to zero as m grows. Thus **for every fixed H>0, sufficiently large finite m gives a strict favorable-branch advantage for formation plus complete original-carrier turnover in the same assay**. This does not prove that one fixed generator wins at all horizons or that favorable architectures become more prevalent.

### An exact, deliberately conservative witness

At H=27, a rational partial sum proves \(e^5>128\), and \((127/128)^{27}>3/4\). Hence

\[
J_0^{\rm full}(27)\ge
L:=\tfrac34R_FR_K
=\frac1{808804024575624000000}
\approx1.23639\times10^{-21}.
\tag{15}
\]

Set

\[
m=\frac3L=2426412073726872000000.
\tag{16}
\]

Equation (10) gives

\[
J_1^{\rm full}(27)\le\frac3{2(1+m)}<\frac L2,
\qquad
\boxed{J_0^{\rm full}(27)-J_1^{\rm full}(27)>\Delta:=\frac L2.}
\tag{17}
\]

This m is derived from the uniform inequalities, not obtained by a success-directed search. The resulting rates are finite but enormous. Neither their magnitude nor their ratios have been shown chemically achievable; the probability bound is not an estimate of actual total success. Smaller useful parameter regimes, robust reliability and attainable rate constraints remain open. The proved claim is a nonempty sufficient class under the specified law, not physical realization of that class.

For separately timed continuations the same calculations give

\[
F([0,6])\ge\frac1{44100},\qquad
K([0,21])\ge\frac1{24453636419520000}.
\tag{18}
\]

These lower bounds can be multiplied as in (9). They remain small and do not establish an infinite surviving process. For a finite-source thermodynamic transfer, the exact reference certificate is **T=27, Kcap=8, and margin Delta in (17)**; altering the source or adding reverse channels requires its own error bound on this complete stopped event.

## 6. What the integrated result closes, and what it leaves open

The bridge is now explicit under one common law: physical formation of fabrication capability; physical formation of a gate; shared capture; replacement of all four original functional carriers; recovery of the same material/fuel state; a conditional continuation kernel; and a strict comparison for the whole selected joint task. No free reset or selectively imported continuation state connects these stages.

Failures are retained both locally in every exit intensity and globally in the competing-branch upper bound. The common target does not require type 0 by name. The positive result nevertheless remains a branch contribution, not a retention or prevalence theorem. Its rates and reaction vocabulary are supplied, and its source is not generated by the subsystem.

Three interfaces are still distinct: achievable physical rates and thermodynamic/source accounting for this exact integrated event; reliable repeated performance under changing support; and a mechanism connecting useful joint function to endogenous retention or propagation. Full-turnover reachability and this finite branch comparison cannot replace any of them.

### Verification and provenance

The [exact checker](../../../../experiments/shared-renewal-capability/integrated-formation/exact_check.py), [saved result](../../../../experiments/shared-renewal-capability/integrated-formation/exact-check.json) and [experiment description](../../../../experiments/shared-renewal-capability/integrated-formation/README.md) preserve the complete event table, all 27 pre/post states, rate polynomials, material/work changes, tagged-Y selection and exact rational bounds. This is a new deterministic arithmetic/path check, not a simulation or parameter search. It does not independently validate chemical feasibility.

Frozen architecture source SHA256: `d20d3284cb2afe84884d567c7d39efe1b3a360fee9375b2158c8116fc7e50362`. Existing source files and results are unchanged.
