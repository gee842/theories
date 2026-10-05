# Physical constraints on paid access to retained support

5 October 2026. AI-authored conditional derivation and primary-source audit. The [paid-access protocol](../../../../experiments/shared-renewal-capability/paid-access/PROTOCOL.md) was fixed before its outcome calculation. This note neither fits its rates nor assumes a favorable outcome.

**Result.** The three proposed CF-access reactions have a common reversible completion with the parent chemistry. They also impose a restriction absent from the work-token ledger: stabilizing stored support reduces the free energy available when it is spent. A finite energy window, sufficiently rapid and selective access, sufficiently slow leakage, and an explicit source inventory are independently testable requirements. Detailed balance alone establishes none of their empirical values. A new seven-capture coupling bound transfers either sign of a strictly separated finite-time comparison, if the measured or stipulated approximation error is small enough. It cannot turn a negative or unresolved original comparison into a positive result.

## 1. Specify the chemistry before interpreting its usefulness

Use the CF-storage parent in [Useful retention, §§2 and 6](USEFUL-RETENTION-MECHANISM.md), retaining its free-F channels. Add exactly

\[
D+CF\longrightarrow R+C,\qquad
R+CF\longrightarrow A_i+C,\qquad
A_i+R+CF\longrightarrow A_i+G_i+C,
\tag{1}
\]

with propensities \(hD\,CF,s_iR\,CF,q_iA_iR\,CF\). There is no bound-packet copying channel, no direct \(CF\to C+F\), and no CF-catalyzed free-F recycling in the fixed protocol. Omission means omission of the entire reversible pair in a completion. It must not mean keeping a catalytic forward reaction while deleting its required backward partner.

Introduce finite charged and spent carrier species \(H_f,L_f\). The source is

\[
H_f+C\rightleftharpoons CF,
\qquad a^+_{\rm cap}=\frac gB H_fC,
\qquad H_f(0)=B,\quad L_f(0)=1.
\tag{2}
\]

Every packet expenditure produces one \(L_f\). Thus (1) has products \(R+C+L_f\), \(A_i+C+L_f\), and \(A_i+G_i+C+L_f\), respectively. Charged-carrier leakage is \(CF\to C+L_f\); charged-carrier wear is \(CF\to D+F\), which releases, rather than spends, its packet. The conserved moieties are

\[
\begin{split}
N={}&R+C+CF+Y+D+\sum_i(A_i+G_i+GF_i+2YG_i)=4,\\
H_f+L_f+U={}&B+3,\qquad U=F+CF+GF_0+GF_1.
\end{split}
\tag{3}
\]

The three additions preserve material. Recycling spends one packet to raise the functional-material count by one; formation and fabrication each spend one unit of the assigned \(W=N-D+U\) ledger. These facts do not identify W with chemical free energy. Nor do the two abstract moiety balances establish atom, charge or proton balance for an actual molecule: an identified chemistry must supply those additional balances.

## 2. One potential assignment for every route

Use ideal dilute, normalized unit-volume stochastic mass action with falling factorials. The reverse of a copying reaction producing \(2A_i\) uses \(A_i(A_i-1)\); the reverse of free reproduction uses \(Y(Y-1)\), without an extra factor of one-half. Changing this convention requires changing rate constants consistently.

Retain all potentials in the [integrated reversible completion](INTEGRATED-THERMODYNAMICS.md), and add

\[
\varphi_{CF}=\varphi_C+\varphi_F-\ln K_C=4M-\ln K_C.
\tag{4}
\]

Here \(\varphi_D=\varphi_{L_f}=0\); \(\varphi_C=\varphi_Y=\varphi_{A_i}=\varphi_{G_i}=M\); \(\varphi_R=2M\), \(\varphi_F=3M\), \(\varphi_{H_f}=4M-\ln B\), \(\varphi_{GF_i}=4M-\ln K_F\), and \(\varphi_{YG_i}=2M-\ln K_Y\). Potentials are in \(k_BT\) units with reference-volume factors absorbed. \(K_F=\alpha_b/\rho_F\) and \(K_Y=\mu/\nu\) come from the retained passive binding pairs. \(K_C>0\) is an energetic parameter of CF. Because direct \(C+F\rightleftharpoons CF\) is absent, it is **not** a measured on/off-rate ratio in this particular repertoire.

For each retained pair \(\alpha\rightleftharpoons\gamma\), choose

\[
k_-=k_+\exp[\varphi\cdot(\gamma-\alpha)].
\tag{5}
\]

Then \(\pi(n)\propto e^{-\varphi\cdot n}/\prod_s n_s!\) satisfies edgewise detailed balance on the finite conserved chemical class. This is the ideal-mixture stochastic framework of [Rao and Esposito (2018), Eqs. 13–14, 41–42 and 51–54](https://arxiv.org/pdf/1805.12077v2). The claim concerns the chemical network, not irreversible analyst tags, a stopping rule or a physical measurement device.

Write \(t=e^{-M}\). Replace the old free-packet source pair and add these pairs to the parent completion:

| Forward reaction | Added reverse propensity |
|---|---:|
| \(H_f+C\to CF\), rate \(gH_fC/B\) | \((g/K_C)t\,CF\) |
| \(CF\to C+L_f\), rate \(\ell_c CF\) | \(\ell_cK_Ct^3 C L_f\) |
| \(CF\to D+F\), rate \(bCF\) | \(bK_CtDF\) |
| \(D+CF\to R+C+L_f\), rate \(hD\,CF\) | \(hK_CtRCL_f\) |
| \(R+CF\to A_i+C+L_f\), rate \(s_iR\,CF\) | \(s_iK_Ct^4 A_iCL_f\) |
| \(A_i+R+CF\to A_i+G_i+C+L_f\), rate \(q_iA_iR\,CF\) | \(q_iK_Ct^4 A_iG_iCL_f\) |

Together with the parent pairs this gives 38 reversible pairs. Type 0 lacks both directions of bound reproduction; type 1 retains both. Reverse charged-carrier wear and reverse paid recycling contain \(K_Ce^{-M}\), so their intrinsic forward bias requires \(M>\ln K_C\), as well as the corresponding \(K_F,K_Y\) constraints for parent bound wear. Large K_C cannot be treated as an independent improvement in retention with no access cost.

### Route identities that measured constants must satisfy

Let \(K_{\rm free}\) be the equilibrium constant of \(R+F\rightleftharpoons A_i+L_f\), and \(K_{\rm paid}\) that of \(R+CF\rightleftharpoons A_i+C+L_f\), in the same standard-state convention. Necessarily

\[
K_{\rm free}=K_C K_{\rm paid}.
\tag{6}
\]

The identical relation holds for free versus paid recycling, and free versus paid gate fabrication. It follows directly from their shared species potentials, even when direct C/F binding is absent. If such a binding pair were added, (6) would be its explicit closed-cycle constraint.

Template-free free-F formation and free-F copying share the same net reaction, so they have the same equilibrium constant. If bound-packet copying were later added, it would have the same equilibrium constant as bound-packet formation. The copying catalyst changes forward and backward kinetics together. Likewise, A_i cancels from the gate-fabrication affinity, and Y or bound YG cancels from its reproduction affinity. Different equilibrium constants for catalyst-only alternatives require additional driven stoichiometry; they cannot be justified by calling one route useful.

## 3. A physical class defined by independently measurable restrictions

The following are constraints on a candidate chemistry, not claims that the current symbolic species meet them.

### Available energy has a window

At a specified set of positive activities, let the dimensionless chemical potentials be \(\mu_s=\varphi_s+\ln a_s\). Define the available energy of a stored packet and of the source by

\[
E_b=\mu_{CF}-\mu_C-\mu_{L_f},\qquad
E_H=\mu_{H_f}-\mu_{L_f}.
\tag{7}
\]

The paid affinities are

\[
\begin{array}{ll}
\mathcal A_D=E_b-(\mu_R-\mu_D),&
\mathcal A_{A_i}=E_b-(\mu_{A_i}-\mu_R),\\
\mathcal A_{G_i}=E_b-(\mu_{G_i}-\mu_R),&
\mathcal A_{\rm cap}=E_H-E_b.
\end{array}
\tag{8}
\]

Thus demanding access bias at least \(a_{\rm use}>0\) and capture bias at least \(a_{\rm cap}>0\) entails

\[
\boxed{d_{\max}+a_{\rm use}\le E_b\le E_H-a_{\rm cap}},
\quad
d_{\max}=\max\{\mu_R-\mu_D,\mu_{A_i}-\mu_R,\mu_{G_i}-\mu_R\}.
\tag{9}
\]

In particular \(E_H\ge d_{\max}+a_{\rm use}+a_{\rm cap}\). If the measured activity range supplies no such window, this strongly forward-driven class is excluded regardless of catalytic speed. Equation (9) is a requirement for the declared bias margins, not a claim that occasional uphill fluctuations or weaker net currents are impossible. At the N=4 count scale some species are absent; logarithms of their activities must not be used as a substitute for the exact edge free energy and falling-factorial rates. The count-state check below supplies that distinct calculation.

At fixed activities, increasing the standard stabilization \(\ln K_C\) lowers E_b, improves capture bias, and reduces access bias. Each net captured-and-spent packet in a completed catalytic cycle contributes the source-to-waste conversion \(H_f\to L_f\); passive binding cannot provide an extra independent cycle affinity. Activities, accumulated waste and source depletion change this balance during a batch.

### Rates require finite service capacity and selectivity

An energetic downhill direction does not imply a fast reaction. Characterize packet leakage, charged-carrier wear, productive access, side reactions and release independently of the eventual succession outcome. At a fixed count state, if a required next reaction has hazard v and every other reaction has combined hazard u, the exact probability of that reaction occurring first by time \(\tau\) is

\[
\frac{v}{v+u}\bigl(1-e^{-(v+u)\tau}\bigr).
\tag{10}
\]

For a prescribed next-event probability p, even an unlimited deadline requires \(v\ge pu/(1-p)\). Some competing events may permit other successful routes; (10) bounds this particular stage criterion, not the entire assay. It provides a directly measurable kinetic requirement without assuming that every competing reaction is harmful. In particular, Y reproduction can supply Y replacement after wear; suppressing it cannot be represented as pure killing throughout full succession.

The ternary laws \(q_iA_iR\,CF\), \(\kappa_iA_iRF\) and \(\rho_iA_iRF\) must also be justified as chemical kinetics. If a proposed elementary mechanism uses one fabricator through sequential binding and turnover, a finite catalytic turnover ceiling \(k_{\rm cat}A_i\) applies to that mechanism. On the claimed low-occupancy domain, its effective mass-action approximation must satisfy, for example, \(q_iR\,CF\lesssim k_{\rm cat}\), with the analogous bounds for free-F routes. This is a conditional mechanism check, not a universal bound on every possible chemistry. Association, dissociation, intermediate occupancy and relaxation times must support the reduction; enzyme saturation cannot be omitted because it gives the desired outcome. Additional intermediate states must carry their material and energy costs.

The no-release condition also needs kinetic evidence. A physical CF made by ordinary binding may dissociate as \(CF\to C+F\); that channel destroys the old one-slot availability argument. Local detailed balance permits omission of both directions in an abstract repertoire, but does not prove the omission accurate for an identified molecule. Measure or bound such bypass hazards. If an extra channel's total rate is at most \(r_{\rm bypass}\) on the reference domain, it contributes at most \(Tr_{\rm bypass}\) to a finite-history coupling error. Exactly absent type-0 bound reproduction is similarly a specificity assumption to replace by a measured small bound where appropriate.

### Fix concentration, volume and source preparation

The protocol's all-positive-coefficients-equal-one convention is moderate in its normalized count/time model. Constants for different molecularities have different physical units. Equal numerical values do not establish comparable laboratory rates.

For a real association step with second-order coefficient \(k_{\rm cap}\), source concentration \(c_H\) gives \(g=k_{\rm cap}c_H\). At fixed reaction volume, B, concentration and g cannot be varied independently. Enlarging a single well-mixed volume while holding the four internal molecules fixed also changes their other encounter propensities. A separate reservoir could hold more molecules at unchanged concentration, but then its transport/interface dynamics and energetic account must be supplied.

Likewise, choosing \(\varphi_{H_f}=4M-\ln B\) for every B constructs a mathematical family of source specifications; it is not changing the inventory of one already identified chemical species at fixed standard potential. A physical validation should insert measured B, concentration, potentials and rates into the error criterion, or explicitly specify a realizable reservoir scaling. Reservoir preparation, waste removal, mixing and physical tag/readout costs are not repaid merely because the event probability improves.

## 4. The seven-capture finite-source comparison

The fixed assay starts at \(R=3,Y=1,F=2\), enters \(P_{ij}=\{A_i=YG_j=CF=1\}\) at its first forward capture, and assesses return to the same core count/type state after all four entry carriers have worn at its seventh forward capture. Its primary deadline is T=10. A reverse reaction producing a packet is not a forward capture. We compare unconditional events \(J_i=\Pr(I=i,\text{complete assay})\), where I labels the first actual template-free formation. The assay and its sign calculation belong to the linked protocol.

Before capture K, let j be the completed forward-capture count. On any original trajectory,

\[
H_f=B-j,\qquad U\le2+j,\qquad L_f=3+j-U.
\tag{11}
\]

For K=7, \(U\le8\) and \(1\le L_f\le9\). Couple all common reactions, molecule selections and observation tags identically. At each original capture after j previous captures, accept it for the finite-source process with probability \(1-j/B\). This exactly gives the finite-source capture intensity until the first mismatch. Added reverse reactions are separate unmatched clocks.

There are at most K captures before stopping. With \((B)_K=B(B-1)\cdots(B-K+1)\), the probability of avoiding every depletion mismatch, conditional on any original capture history, is at least \((B)_K/B^K\). If all added reverse hazards sum to at most \(r_*\) on the original domain, full-history coupling gives

\[
\begin{split}
|\widetilde J_i-J_i|&\le\epsilon(B,T),\\
\epsilon(B,T)&:=1-\frac{(B)_K}{B^K}e^{-Tr_*}\\
&\le\frac{K(K-1)}{2B}+Tr_*.
\end{split}
\tag{12}
\]

The product bound follows from multiplying the acceptance probabilities, and \(1-\prod_j(1-j/B)\le\sum_jj/B\). It improves the older uniform-clock bound \(TgN(K-1)/B\) without adjusting kinetics or observing outcomes. Reverse events can alter source counts after divergence; no assertion about those paths is needed. Early physical failure or an earlier observation stop only reduces the number of captures.

For either sign, if the reference comparison has a certified strict separation \(0<\Delta\le|J_0-J_1|\), its sign survives whenever

\[
2\epsilon(B,T)<\Delta.
\tag{13}
\]

The error also bounds individual event predictions. It does not transfer an infinite-horizon statement, an unbounded reward, exact absorption or a global ordering of all events. If additional kinetic/coarse-graining discrepancies admit a common-clock hazard bound r_extra, add \(Tr_{\rm extra}\). A discrepancy requiring memory or new hidden intermediates needs its own approximation argument, not automatic inclusion as a mass-action rate.

## 5. An exact reverse envelope for the fixed all-unit law

Set \(K_C=K_F=K_Y=1\) in the conditional potential construction, and retain the protocol's unit forward constants. This specifies an algebraic reversible family; it does not estimate its potentials from measurements. The parent reverse channels remain as tabulated in the earlier completion, with the new CF table above. Their total added reverse intensity is exactly

\[
r_{\rm rev}(n)=h_1(n)t+h_3(n)t^3+h_4(n)t^4,
\tag{14}
\]

where, writing \(L=L_f\),

\[
\begin{split}
h_1={}&C+Y(Y-1)+6D+CF+3DF+2RCL+RYL\\
&+Y\,YG_1+2YD+(G_0+G_1)D,\\
h_3={}&L(1+C+G_0+G_1),\\
h_4={}&L\sum_i[A_i^2+A_iG_i+A_iC+A_iG_iC].
\end{split}
\tag{15}
\]

For example, the 2RCL term combines reverse free-C recycling and reverse paid recycling. The A_i² term combines reverse template-free formation and reverse copying, \(A_i+A_i(A_i-1)\). The CF reverse capture is t CF, not t FC. Existing passive dissociations are common channels, not approximation errors.

Exact enumeration of all 39,579 count/stock/capture tuples satisfying (3) and (11), a superset of reachable original states, gives independent coefficient maxima

\[
\boxed{r_*\le120e^{-M}+45e^{-3M}+144e^{-4M}.}
\tag{16}
\]

The maxima occur respectively at \(D=4,F=8,L=1\), at \(G_1=4,F=0,L=9\), and at \(A_1=4,F=0,L=9\), all with j=6 and unlisted core counts zero. They need not occur on the same path. The sum of maxima is a conservative bound, not an exact maximum of r_rev and not an event-probability computation.

Combining (12) and (16) yields the directly evaluable sufficient condition

\[
\boxed{\Delta>
2\left[\frac{21}{B}
+10\bigl(120e^{-M}+45e^{-3M}+144e^{-4M}\bigr)\right].}
\tag{17}
\]

No B or M is chosen to declare a positive physical example here. If the reference result is negative, (17) preserves that negative sign. If it is zero or unresolved, this perturbation result supplies no direction. Measured non-unit constants require evaluating their actual reverse hazards rather than reusing (16). The available margin must also pay for omitted release, imperfect blocking and justified reduction errors.

The chemical state after a return is different because H_f and L_f changed. A repeated-return kernel cannot be reused as if the source reset. Reverse wear can create functional species, and reverse expenditures can recreate packets. Consequently the old six-capture minimum and exact availability/absorption arguments for the forward repertoire do not automatically hold in the completed chemistry; the assay still explicitly assesses its seventh forward capture. A finite closed chemical system with the stated thermal bath has an equilibrium detailed-balance law, not an indefinitely maintained chemical nonequilibrium steady state. Under type-exchange-symmetric potentials and a swap-invariant connected class, equilibrium architecture weights remain equal even when a kinetic channel pair is absent for one type. Useful finite transient delivery is a distinct question.

## 6. What the preserved RNA evidence can actually identify

The preserved [Bansho et al. (2016) paper](../../../../sources/24-rna-network-evidence-2026-10-05/Bansho-2016.pdf), Table 1 and associated Results, reports purified-replicase kinetic assays. Original-host \(k_{cat}=0.22\pm0.016\ {m min}^{-1}\), \(K_m=0.76\pm0.32\) nM; evolved-host values are \(0.094\pm0.017\) and \(2.4\pm1.2\). The reported errors are SEs, and enzyme activity assumes all purified replicase is active. These are useful measured biochemical constraints, not elementary CF rates.

There is an unresolved printed inconsistency, verified visually on page 4049: those evolved-host central values give \(0.094/2.4\approx0.03917\), whereas the table prints 0.0039 and the text/table report a 74-fold reduction. The component central values imply approximately 7.39-fold. The efficiency unit printed as nM/min also conflicts dimensionally with \(k_{cat}/K_m\), whose unit is \({\rm nM}^{-1}{\rm min}^{-1}\). No column is silently corrected. The parasite values 0.034/min and 48 nM give approximately 0.000708, consistent with that row's printed efficiency. A targeted primary-source search did not identify a correction; this does not establish none exists. [Author-hosted original](https://webpark2056.sakura.ne.jp/papers/2016_Bansho.pdf).

The [Mizuuchi et al. (2022) main paper](../../../../sources/24-rna-network-evidence-2026-10-05/Mizuuchi-2022.pdf), Methods, sets effective \(k_{ij}=\ln R_{\rm eff}\) from separately measured replication fold changes. Their model combines translation, template properties and catalysis; its compartment volume is normalized to one. The [supplement](../../../../sources/24-rna-network-evidence-2026-10-05/Mizuuchi-2022-SI.pdf), Text 4, adds translated replicase with host translation coefficients set to one, parasite coefficients zero, and translation capacity 30. Those settings are not elementary association measurements. The authors explicitly omit RNA–replicase association and dissociation because the required experimental data are unavailable. Their RNA assays and reconstitutions constrain effective interaction/specification differences; they do not supply storage affinities, reverse hazards, access-release rates or a CF identification. [Published study](https://doi.org/10.1038/s41467-022-29113-x).

Accordingly, a useful next empirical calculation would propagate independently obtained rate/affinity intervals through an identified reaction/transport model, accounting for these unresolved quantities and supplied transfer conditions. It would test a held-out joint delivery-and-renewal observable against the established replication model. Assigning RNA to A, enzyme to G and nutrients to F because the symbols fit would not perform that identification. The present papers also do not independently test this later model's seven-capture target.

## Reproducibility and read scope

The following self-contained standard-library code reproduces the finite coefficient envelope. It enumerates an a priori conservation domain; it does not search kinetic parameters, fit experimental output, or calculate the primary event's sign. Executed 5 October 2026 with the bundled Python runtime; it returned `39579 {1: 120, 3: 45, 4: 144}`. The edgewise detailed-balance proof is algebraic in (4)–(5); this small check verifies (15)–(16), not microscopic chemical feasibility.

```python
S = ('R', 'C', 'CF', 'Y', 'D', 'A0', 'A1', 'G0', 'G1',
     'GF0', 'GF1', 'YG0', 'YG1')
w = {s: 2 if s.startswith('YG') else 1 for s in S}

def rows(i, remaining):
    if i == len(S):
        if remaining == 0:
            yield {}
        return
    s = S[i]
    for n in range(remaining // w[s] + 1):
        for row in rows(i + 1, remaining - n * w[s]):
            yield {s: n, **row}

maxima, count = {1: 0, 3: 0, 4: 0}, 0
for z in rows(0, 4):
    for j in range(7):
        bound = z['CF'] + z['GF0'] + z['GF1']
        for F in range(2 + j - bound + 1):
            L = 3 + j - F - bound
            R, C, CF, Y, D = (z[s] for s in ('R', 'C', 'CF', 'Y', 'D'))
            A, G = [z['A0'], z['A1']], [z['G0'], z['G1']]
            h1 = (C + Y*(Y-1) + 6*D + CF + 3*D*F + 2*R*C*L
                  + R*Y*L + Y*z['YG1'] + 2*Y*D + sum(G)*D)
            h3 = L*(1 + C + sum(G))
            h4 = L*sum(a*a + a*g + a*C + a*g*C for a, g in zip(A, G))
            count += 1
            for p, value in ((1, h1), (3, h3), (4, h4)):
                maxima[p] = max(maxima[p], value)
assert count == 39579 and maxima == {1: 120, 3: 45, 4: 144}
print(count, maxima)
```

Read the parent retention note, earlier integrated thermodynamic note, and the frozen paid-access protocol. Reused the previously inspected Rao–Esposito published-version manuscript; reread its ideal-mixture assumptions, state free energy and local detailed balance. Read the preserved RNA papers' relevant biochemical Methods/model passages and Mizuuchi supplementary Text 4; visually inspected Bansho Table 1 in its original PDF. No raw RNA data, Bansho supplementary kinetic curves, author simulation code or new molecular experiment was reanalyzed. A publisher/PMC opening initially failed; the existing author-hosted original PDFs supplied the source text, with the printed Bansho values also returned by primary-source web search.

All three preserved RNA PDF hashes matched their [manifest](../../../../sources/24-rna-network-evidence-2026-10-05/MANIFEST.json). No source bytes were edited. Antecedents at reading:

| File | SHA-256 |
|---|---|
| USEFUL-RETENTION-MECHANISM.md | `0313fc92e856f3de983232361884f3133a23cfecf9b74ed0ca8b6cb2a3c5ff37` |
| INTEGRATED-THERMODYNAMICS.md | `3f0c7ae294539ff5004d5e8fe56519719ff9166ddff24ec4cc164727a720f559` |
| paid-access/PROTOCOL.md | `440bd7d4031b9a51db9a92142d752e3ff4c133ee6f2ebfe218d50414dfade55d` |

The earlier huge-rate positive witness is not reused. This note supplies chemical consistency, an improved approximation bound, and physical exclusion/identification criteria. Favorable full-succession direction, microscopic specificity, practical rates and empirical validation remain separate questions.
