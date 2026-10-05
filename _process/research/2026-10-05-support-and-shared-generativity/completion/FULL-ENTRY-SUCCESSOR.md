# All formation histories and the actual successor interface

5 October 2026. AI-assisted continuation of the paid-access law at commit047a8c5. The [protocol](../../../../experiments/shared-renewal-capability/full-entry/PROTOCOL.md) was recorded before this calculation. Earlier selected-entry and seven-capture results remain unchanged.

**Result.** The complete entrance law to a declared organizational family retains a small blocking-gate advantage when every formation route is included. This now has rigorous probability bounds, rather than only a positive selected-route contribution. The unchanged dynamics nevertheless leave almost no occupation of that family at time10. Formation, occupation and complete renewal remain different observables. The full entrance distribution also carries unequal reserves and mixed types, which the next successor calculation must retain.

## 1. Common law and complete entrance family

Use the exact42 forward channels, all positive effective coefficients one, zeta0=0,zeta1=1, and common initial state R3,Y1,F2. Define

\[
\mathcal P=\{P_{ij}(m): A_i=CF=YG_j=1,\ F=m\ge0;\ i,j\in\{0,1\}\},
\]

with other counts zero. This is a specific physically described organization, not every possible generative arrangement. Unlike the earlier event, entry can occur after any first reaction, at any capture count, with either matching or mismatched fabricator/gate types, and with any free reserve. Let tau be the first time the process enters this family. A failed preparation retains its probability mass.

The primary observables at H10 are the unconditional probabilities Pr(tau≤H, gate at entry=j). Diagnostic times1 and3 were declared before computation. Also calculate actual occupation Pr(X_H∈P_ij(any m)) and integrated occupation E∫_0^H1{X_t∈P_ij(any m)}dt. An entered organization can leave, fail or return; first-entry success does not freeze the physical law for the latter two observables.

The [producer](../../../../experiments/shared-renewal-capability/full-entry/compute.py) explicitly lists all42 channels, with catalysts and both type-specific competitors. Its table was independently inspected against the [machine-checked typed vocabulary](TYPED-RENEWAL-FORMALIZATION.md); all inputs and outputs match. That source comparison is not yet a formal proof of Python enumeration or mass-action semantics.

## 2. Exact state reduction and truncation error

Material N4 is conserved. Total packets U=F+CF+GF0+GF1 can increase only through fresh capture. Bounded material and capture intensity imply nonexplosion: on any bounded time interval, captures are dominated by a finite-rate Poisson process, U is almost surely bounded, and every other propensity is bounded on the resulting finite count-state domain.

For these organizational assays, Y+YG0+YG1=0 and V=R+C+CF+F+GF0+GF1=0 are invariant failure faces in the declared forward law. Killing upon either loss preserves the requested entrance and occupation quantities. It does not claim loss of every other function, and it cannot be reused after introducing reverse wear or a restart pathway. No minimal-work or prescribed-capture pruning is used.

Before this killing, C≤3 because at least one material unit belongs to the Y lineage. Therefore source captures are dominated by Poisson(3H), and U≤2+number of captures. A free-packet overflow above90 before H10 requires at least89 captures. A positive-series rational bound gives

\[
\Pr(\text{overflow by10})\le
\Pr(\operatorname{Pois}(30)\ge89)
<2.474\times10^{-18}.
\tag{1}
\]

The bound divides a geometric majorant of the exponential tail by a lower partial sum for exp(30); its exact rational value is saved. The stopped graph contains34,196 live states and two loss states. Killing overflow underestimates each entrance/occupation probability by at most (1), and integrated occupation by at most H times (1). Every killed transition remains in the outgoing hazard.

## 3. Certified whole-entrance comparison

The [integer certificate](../../../../experiments/shared-renewal-capability/full-entry/certify.py) uses uniformization rate807 and Poisson mean8070. All nonnegative transition-numerator rows sum to807. Success iterates are bounded with int64 arithmetic at scale2^53; their largest possible accumulated numerator, including upward rounding, is below2^63. Thus integer overflow cannot invalidate the enclosure. The absorption vectors mark the two entry gate types, including both fabricator types and every retained free reserve.

Poisson weights are enclosed as arbitrary-precision integer ratios relative to the mode, using scale2^192. Exact recurrence propagates outward-rounded bounds both down to zero and up to order10,000. A geometric upper tail and rational normalizing-sum bounds enclose the weighted probability. This avoids floating exponential evaluation. Finally the original-process upper endpoint adds the killed-overflow bound. The saved [certificate](../../../../experiments/shared-renewal-capability/full-entry/certificate.json) supplies exact fractions; the following decimal endpoints are rounded outward:

| First organization has gate | Unconditional probability by10 |
|---|---:|
| Blocking, j0 | [0.00122046147710, 0.00122046147717] |
| Nonblocking, j1 | [0.00117785304329, 0.00117785304336] |

Consequently the blocking-gate first-entry advantage is at least4.2608433741e−5 in absolute probability. Both probabilities are about0.12 percent; all-pair entrance is about0.24 percent. This is a whole entrance-family result within one law. It does not condition on successful first reactions, successful entrants or surviving organizations, and does not establish a global type-prevalence theorem.

The certificate reuses the enumerated generator. The arithmetic enclosure and the independently inspected reaction-table correspondence have distinct evidential roles. No chemical identification or empirical frequency claim follows from normalized unit coefficients.

## 4. Formation does not imply later occupation

The [floating propagation](../../../../experiments/shared-renewal-capability/full-entry/results.json) retains all four pairs and every entry reserve. Its primary H10 values are:

| Fabricator/gate pair | First-entry probability | Actual occupation probability at10 | Expected occupation time through10 |
|---|---:|---:|---:|
| 00 | 0.00121916927 | 1.2010e−12 | 0.00021597304 |
| 01 | 1.0388e−6 | 6.0213e−15 | 2.1583e−7 |
| 10 | 1.2922e−6 | 8.0822e−15 | 2.7052e−7 |
| 11 | 0.00117681424 | 1.1982e−12 | 0.00020845891 |

Only the gate-total first-entry intervals above received directed certification. These occupation and individual-pair figures remain floating calculations with a rigorous truncation bound but no roundoff enclosure; particularly small occupation contrasts must not be called certified signs. Probability accounting is checked, but near-unit total mass does not itself bound the error in a rare coordinate.

The results demonstrate why a positive entrance comparison is an intermediate milestone. The model supplies no practically reliable operation at this preparation and timescale. Changing population size, source routing, material exchange or restart would change the physical law and requires a separately specified test. The prior finite-source seven-capture certificate also does not automatically transfer this unrestricted-capture event.

## 5. Exact entrance-to-successor composition

Let E(d t,d xi) be the complete, unnormalized first-entry measure, including entry types, free reserve and any environmental state. In the present count model xi=P_ij(m); in a finite-source model xi must also contain its actual fuel and waste. For the nonexplosive process, the entrance density on a count state xi has the usual killed-semigroup form

\[
E(dt,\xi)=\mu e^{tQ_{TT}}Q_{T\xi}\,dt,
\tag{2}
\]

where T is the complement of the entrance family and mu is the common initial distribution. An initial mass already inside the family adds a time-zero atom; this preparation has none. Equation(2) denotes the appropriate substochastic semigroup, not an assumption that an infinite matrix has bounded norm. The calculation above evaluates its time-integrated distribution with explicit truncation control.

At entry, mark the four current functional carriers. Extend the actual law by bookkeeping that records their subsequent wear without influencing reaction rates. Let K_xi(ds,d xi',d ell) be the subprobability law of first reaching the organizational family after all four originals have worn. It retains endpoint types, reserves, elapsed time and the ledger ell; paths that never complete retain the missing probability mass. Successor types can differ if the common task permits them. No source or reserve is reset.

For any measurable full-cycle test q on the entry and successor records, the actual composition is

\[
\Pr(\text{first completed turnover satisfies }q\text{ by }H)
=\int E(dt,d\xi)\int K_\xi(ds,d\xi',d\ell)
\mathbf1\{t+s\le H,\ q(\xi,\xi',\ell)\}.
\tag{3}
\]

This is a strong-Markov decomposition of one process, with its full entry distribution. It counts the specified first completed turnover. Success on a later repeated attempt after that first record fails q requires another continuation kernel or a different stopping rule. It is not a product of average success rates, nor does it require statistical independence between entry and continuation. If a prefix condition or quantity depends on earlier history beyond xi, retain it in the augmented entry state. If environments have unmodeled memory, a count-state kernel is insufficient. Analyst labels confer no free observations or control on an actor; a physical assay must account for implementing its readout.

The next numerical obligation is to construct the full tagged K_xi for the actual entrance support, including mixed types, inherited reserves and all failed exits. The earlier six-capture, m0 successor calculation is one restricted event, not this whole kernel.

## 6. Inherited reserves change the capture bound

For a successor returning to one fabricator, capture carrier, gate and Y, the work difference is m'−m. The same exact ledger gives

\[
K_{\rm capture}=m'-m+K_{\rm leak}+2D_A+2D_G+D_C+D_Y
\ge6+m'-m.
\tag{4}
\]

Full original-carrier wear supplies at least one wear in each role. Thus six captures remain necessary when the inherited reserve is restored or increased; spending inherited reserve can reduce the fresh-capture requirement. A favorable return count that ignores this spending could misidentify reserve exhaustion as sustained renewal. The separate [reserve-aware formalization](RESERVE-SENSITIVE-TURNOVER.md) machine-checks this generalized ledger consequence for typed traces; original-label tracking remains outside that proof.

The advance is a complete entrance law and a precise interface to complete successors. The remaining positive target is reliable, physically identified generation and regeneration of joint capabilities across that actual ensemble. It is not satisfied by the certified entrance advantage alone.
