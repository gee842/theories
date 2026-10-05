# When productive consequences select the response that produced them

6 October 2026. AI-authored analytical extension of [consequence-coupled reconstruction](ENDOGENOUS-REGULATION-MATH.md), starting from the [shared-pool neutrality result](ENDOGENOUS-REGULATION-REVIEW.md#why-this-does-not-yet-derive-selection-of-useful-responses). This addresses the next connection in the [accepted work sequence](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md#accepted-work-sequence): **changed continuation → differential retention of competing responses**.

**Result.** An exact generator criterion distinguishes increased reconstruction from selection of a useful variant. A finite, paid-association extension provides a positive expected-frequency effect without a success variable entering the law. The association and copying chemistry are supplied; association instances form within the process. This is conditional population selection, not individual learning, discovery of the architecture, or revision of the selector.

**Verification status:** mathematical proofs below; exact rational arithmetic checked and a separate collaborating-AI review accepted the drift calculation, path bound, coupling estimate and comparator neutrality. That review prompted explicit initial-state assumptions for the low-fuel obstruction and a precise catalytic-loss branching rule. This is internal analytical review, not external peer review, a full CTMC implementation or a Lean certificate. The existing Lean root does not automatically certify these results.

## 1. Exact frequency criterion

Let useful and alternative response counts be a,h, let n=a+h, and let p=a/n while a,h>0. Unused precursor is not a response and is excluded from n. Stop the process at the first extinction of either type, keeping its boundary value thereafter. At this stopping event n≥1 because each loss removes one molecule; freeze p at zero or one even if all molecules later disappear, so no 0/0 convention is needed. Assume a finite nonexplosive process and no new untemplated formation during the contest. Births copy their template's type; their actual state-dependent propensities are a b_a(x), h b_h(x). Loss propensities are a d_a(x), h d_h(x). Other events may alter resources, associations and rates but leave a,h unchanged. A birth or loss may simultaneously alter other state coordinates.

An a birth changes p by (1−p)/(n+1); an h birth changes it by −p/(n+1). An a loss changes it by −(1−p)/(n−1); an h loss changes it by p/(n−1). Therefore

\[
\boxed{\mathcal Lp
=np(1-p)\left[
\frac{b_a-b_h}{n+1}-\frac{d_a-d_h}{n-1}
\right].}
\tag{1}
\]

Because n≥2 in the interior, the local expected-frequency drift is positive exactly when

\[
\boxed{(n-1)(b_a-b_h)>(n+1)(d_a-d_h).}
\tag{2}
\]

This finite-population factor matters: subtracting per-capita birth and death differences without their distinct denominators is not the exact criterion. Production or repair has no separate term unless it changes actual access, copying or loss.

Writing τ for first type extinction, Dynkin's formula gives

\[
\mathbb E p_{H\wedge\tau}-p_0
=\mathbb E\int_0^{H\wedge\tau}\mathcal Lp(X_t)\,dt.
\tag{3}
\]

Thus nonnegative drift at every reachable interior state gives a submartingale; strict positive drift on a region occupied for positive expected time gives a strict increase. Positive drift at one state alone does not establish a net finite-horizon advantage. Correlations between resources and types remain inside the expectation.

In the original shared pool, b_a=b_h=βPF and d_a=d_h=δ, so (1) is zero even when only a repairs capture sites. Useful repair can increase total reproduction without increasing its producer's expected fraction. Type-specific immigration or fabrication would add \([(1-p)u_a-pu_h]/(n+1)\); it must not be hidden inside evidence for selection of existing variants.

## 2. A paid local-access extension

Retain a finite support stock E, common usable fuel F, precursor P and two response types. Add N capture sites j. Each site has condition c_j∈{0,1}, local fuel f_j∈{0,1}, and either a vacant position or one associated response molecule. Counts a,h include both free and associated molecules; P+a+h=M. Each free molecule can associate with any vacant site under the **same** law, regardless of repair efficacy. An offspring is initially free. The local fuel is chemically the same usable support in a distinct, access-restricted location; localization is a declared physical premise.

| Event | Physical change | Propensity |
|---|---|---|
| Association of type i at vacant j | Free molecule becomes resident; one F spent | ξ n_i^free F per vacant site |
| Effective repair | Resident a changes c_j:0→1; one F spent | ρF at each damaged a-occupied site |
| Capture | E→f_j at intact site with f_j=0 | gE per eligible site |
| Local copy | Resident template + P + f_j → resident + free offspring of that type | βP f_j per occupied site |
| Bulk copy | Any template + P + F → template + free same-type offspring | β₀ n_i P F for type i |
| Wear | Molecule → P; if resident, its position becomes vacant | δ per molecule |
| Site damage | c_j:1→0 | α per intact site |
| Leakage | One common or local fuel unit becomes spent | ℓ per fuel unit |

A nonrepairing h cannot perform effective repair. All other listed mechanisms are identical across types. Wear does not reset a site's condition or fuel: a later resident can inherit another molecule's repaired site. No event reads p, an analyst's success score, or a label meaning “deserves reinforcement.” The association chemistry makes access local without evaluating usefulness.

If B,R,K_l,K_b,L count association, repair, local copying, bulk copying and leakage, every path satisfies

\[
\boxed{F_t+\sum_j f_{j,t}+E_t+B_t+R_t+K_{l,t}+K_{b,t}+L_t
=F_0+\sum_j f_{j,0}+E_0.}
\tag{4}
\]

Capture relocates a finite support packet; it creates no new support. Association, repair and copying each consume a real unit. Wear returns precursor but not fuel. This is coarse material accounting, not a thermodynamic identification.

Set \(Q_i=\sum_{j:\,\mathrm{resident}(j)=i}f_j\). In the interior,

\[
b_a=\beta_0PF+\beta P Q_a/a,\qquad
b_h=\beta_0PF+\beta P Q_h/h,\qquad d_a=d_h=\delta.
\tag{5}
\]

Consequently the local drift favors a exactly when \(Q_a/a>Q_h/h\), provided βP>0. Repair can create that asymmetry through actual captured fuel. Occupancy, subsequent wear or capture by a different resident can also remove or reverse it. The conclusion comes from the access relation and realized state, not from declaring a higher intrinsic replication coefficient for the useful type.

## 3. A finite-horizon positive-rate witness

Start from a **contest preparation**, after response variants already exist:

\[
N=2,\quad a=h=P=1,\quad F=3,\quad E=1.
\tag{6}
\]

Both sites begin damaged, vacant and without local fuel. There are no initial associations. The two seeds and their inherited type-specific repair efficacy are supplied; this is not a new proof of variant origin. The previous construction supplies a route to forming a response, but does not by itself generate both types or exactly this preparation.

Take ξ=ρ=g=β=1. First set β₀=α=δ=ℓ=0 as a reference. Before the sole possible birth, at most two associations consume fuel. Three initial units therefore suffice for those associations and one effective repair. The active seed eventually associates and repairs its site; that site captures the one external packet; its resident copies. No h-associated site can repair or capture. With no loss, damage or bulk copying, that copy occurs almost surely and is of type a. The terminal frequency is 2/3; before the copy it is 1/2.

A quantitative horizon bound follows from the event sequence

\[
\text{h associates; a associates; a repairs; capture; a copies.}
\tag{7}
\]

The initial total association rate is 12; the first type is h with probability 1/2. Thereafter the exit rates along (7) are 2,1,1,1. Requiring every wait to be at most two units completes the sequence by H=10. Every listed rate is at least one. Since e²>7,

\[
\Pr((7)\text{ by }10)>\tfrac12(6/7)^5.
\]

Frequency never decreases in this reference, so

\[
\mathbb E p_{10}^{(0)}-\tfrac12
>\tfrac1{12}(6/7)^5
=\boxed{648/16807}.
\tag{8}
\]

Now restore **positive** site damage, molecule wear, fuel leakage and symmetric bulk copying:

\[
\alpha=\delta=\ell=\beta_0=\varepsilon=1/10000.
\tag{9}
\]

Couple to the reference until the first added event. N=2, n≤3 and the fuel ledger is bounded by four. Because P+n=3 with integer counts, Pn≤2. Thus the total added-event intensity is at most

\[
\varepsilon(2+3+4+8)=17\varepsilon.
\]

The bulk term uses PF n≤8; this deliberately loose bound suffices. Coupling failure by H=10 has probability at most 17εH=17/1000. A stopped frequency lies in [0,1], so its expectation changes by at most that probability. Hence

\[
\boxed{\mathbb E p_{10\wedge\tau}-\tfrac12
>\frac{648}{16807}-\frac{17}{1000}
=\frac{362281}{16807000}>0.0215.}
\tag{10}
\]

In the **repair-disabled comparator**, both sites remain damaged, no local fuel is ever captured, and both types have identical per-capita bulk copying and wear. Its stopped expected frequency is exactly 1/2 by (1), even though omitting repair saves fuel. Association can change where either type resides, but bulk copying is accessible to all templates at the same per-capita rate, and local copying remains disabled by zero local fuel. Hence unequal occupancy does not break the stated neutrality.

A separate **equally priced ineffective-repair comparator** retains the active resident's attempted repair at rate ρF and consumes one common F per attempt, but leaves its site damaged. No local fuel is captured in this arm either. Attempted repair changes common F without changing a,h; both types still have the same actual bulk-copying and wear rates. Its stopped expected frequency is therefore also 1/2. This matches the propensity rule and unit expenditure per attempted repair, not total realized spending: successful repair removes that site's damaged state, whereas failed attempts can recur.

Equation (10) is a positive causal expected-frequency contrast with both comparators. All arms retain identical initial resources and association rules; omitted repair saves its real cost, while ineffective repair pays without restoring the dependency. Birth always consumes P and wear of either type returns P; the changing denominator and precursor stock are not reset.

This establishes finite-horizon selection under a costed, finite-support localization mechanism. It does not establish reliable indefinite renewal, long-run fixation superiority, or natural rates. The interval and constants are a transparent uncalibrated existence witness.

## 4. Adverse regimes and work-induced wear

The access mechanism needs fuel to form and operate. With all sites initially damaged and vacant, empty local stores and F₀<2, no active seed can both associate and repair; uncaptured E alone cannot start the loop. An already associated active response is a different preparation and can repair with one common fuel unit. If E₀=0 and local fuel begins absent, no local births occur. Equal bulk copying and wear then keep expected frequency neutral, even while repair spends common fuel. A shared expense does not automatically produce selective disadvantage any more than a shared benefit produces selective advantage.

A further declared catalytic cost makes a negative regime explicit. Split the original repair propensity into a resident-preserving branch of rate (1−σ)ρF and a resident-consuming branch of rate σρF at each eligible site, for σ∈[0,1]. The latter returns precursor and leaves the repaired site vacant; both branches consume one F and restore the site. This is an actual reaction branch, not a fitness penalty appended to an assay. If J_a is the number of damaged a-occupied sites, total additional a-loss propensity is σρFJ_a. Thus

\[
d_a-d_h=\sigma\rho FJ_a/a.
\]

The exact condition becomes

\[
\boxed{(n-1)\beta P(Q_a/a-Q_h/h)
>(n+1)\sigma\rho FJ_a/a.}
\tag{11}
\]

With E₀=0, initially empty local stores and σ>0, the left side is always zero and the right side is nonnegative. The stopped frequency is a supermartingale. From (6), an active association and a catalytic-loss opportunity are reached with positive probability within any positive horizon, giving a strict negative expected-frequency change. Association can therefore form and repair can function while the useful variant is selectively disadvantaged. With support present, a repaired but vacated site can additionally be occupied by the alternative type. Neither private access nor useful contribution guarantees a favorable direction under all costs and turnover.

## 5. What this supplies to the next derivation

**Subsequent result, 6 October 2026:** the [formed-variant construction](FORMED-VARIANT-SELECTION-INTEGRATION.md) now supplies an initially variant-absent process with paid formation and actual mixed copying under one resource history. Its new law and expected-count statistic have their own proofs; the stopped-frequency result here is not automatically transferred. In particular, shared return need not be neutral for the newer count statistic. The preparation limitation recorded below remains a limitation of this earlier model; selector revision remains unresolved in both.

The original loop explains why a response can recreate material used in its copying. This extension specifies when that return changes its **relative** retention against an alternative: the operative issue is who can actually access the resulting support and who bears losses. The shared-pool counterexample and the paid-localization witness now occupy one generator framework.

What becomes explained conditionally is a route from productive action to preferential copying without an observer reward. What remains supplied is the variation repertoire, type inheritance, local-access chemistry, site scaffold, formation mechanism for associations, and the distinction between response efficacies. Association instances form at cost; the capacity to form them does not yet evolve here. The first construction and this contest have not yet been joined into one derivation that produces the needed preparation and both types.

Population selection is a possible precursor to learning, not its synonym. The next connection is to let access, sensing or copying mechanisms vary, explain their formation and inheritance, and show how changed consequences alter those mechanisms—including exploitation and misleading feedback. Deriving a selector's revision would require tracking those variants and costs inside the process; simply changing ξ, β or locality between analyst-selected arms would not do it.

Exact arithmetic used for (8)–(10):

```python
from fractions import Fraction as Q
gain = Q(1, 12) * Q(6, 7)**5
assert gain == Q(648, 16807)
assert gain - Q(17, 1000) == Q(362281, 16807000)
assert gain - Q(17, 1000) > Q(215, 10000)
```

The calculation checks constants only. The mechanism, stochastic coupling and scope require the proofs above and a separate review.
