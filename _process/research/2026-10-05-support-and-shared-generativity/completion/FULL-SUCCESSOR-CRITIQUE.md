# Full successor semantics and reserve control

5 October 2026. AI-assisted independent mathematical audit following commit `eec090f006aec898fe0de13836122b70f92175be`. This note concerns the same 42-channel, unit-positive-coefficient CF paid-access law, material N=4, initial R3,Y1,F2, and common absolute deadlines 1, 3 and 10. It introduces no reaction, favorable rate, reset, selected entrance route, or new success probability calculation.

**Main findings.** Free reserves are not globally bounded by material conservation. An explicit positive-rate cycle pumps an additional free packet while restoring its material preparation. Nevertheless the mobile packet pool is dominated by a simple immigration–death process. This gives a rigorous, much smaller reserve-tail bound suitable for a complete successor calculation. A full successor must still start from the actual entrance distribution, record wear of its four original carriers, preserve inherited reserve and count failed entrances. Entering the organization is not renewing it.

## 1. The requested whole event

Retain the [complete entrance family](FULL-ENTRY-SUCCESSOR.md)

\[
\mathcal P=\{P_{ij}(m):A_i=CF=YG_j=1,\ F=m\ge0\},
\]

with all other counts zero. Let \(\tau\) be its first entrance time. At \(\tau\), tag the four functional carriers: A, C, G and Y. A charged CF contains the C carrier and a packet; YG contains two distinct material carriers. A fuel packet is not a fifth tagged carrier.

Let \(\sigma\) be the first time after \(\tau\) when all four originals have experienced their own wear and the physical state belongs to \(\mathcal P\) again. Wear marks are permanent even if the material is subsequently recycled into a new functional carrier. Thus this is replacement of the original functional carriers, not disappearance of the conserved material atoms. The task must state which interpretation it intends.

The complete-turnover event is

\[
\mathcal R_H=\{\tau\le\sigma\le H\}.
\tag{S1}
\]

The corresponding reserve-restoring event at that **first completed turnover** is

\[
\mathcal R_H^{\rm restore}
=\{\tau\le\sigma\le H,\ F_\sigma\ge F_\tau\}.
\tag{S2}
\]

The final fabricator and gate types may differ from their entrance types unless a separately declared task requires otherwise. Entrance and endpoint labels are distinct observables. The denominator is the original preparation, not the entrants or their survivors.

If the first completed turnover has lower reserve, it succeeds at (S1) and fails at (S2). Continuing until a later reserve-restoring visit would define a different stopping rule and a different event. Neither rule is intrinsically wrong; silently switching them would change the claimed result.

The exact composition remains

\[
\Pr(\mathcal R_H\text{ with }q)
=\int E(dt,d\xi)\int K_\xi(ds,d\xi',d\ell)
\mathbf1\{t+s\le H,\ q(\xi,\xi',\ell)\},
\tag{S3}
\]

where E is the unnormalized first-entrance measure and K is the first completed-turnover kernel with the actual types, reserve and any environmental memory. The same absolute deadline leaves only H−t after entrance. A fresh full H for each entrant is a different question. The strong Markov property applies to the complete physical/record state, not automatically to a coarse count description missing relevant history.

The existing [typed reserve ledger](RESERVE-SENSITIVE-TURNOVER.md) gives, for each realized completion,

\[
K_{\rm capture}\ge6+m'-m.
\tag{S4}
\]

This is a necessary count, not a success probability or a positive path theorem. Event (S2) consequently requires at least six fresh captures after entry. A turnover financed by spending inherited reserve remains a valid (S1) success; it must not be reported as reserve-restoring renewal.

## 2. A precise carrier lift

A four-slot representation can realize the tagged process without changing its count-state law. Slots are conserved material units. The initial tags attach to the four slots at entrance, whose current roles are A, C, G and Y. Free packets remain a separate count. Each YG bond links its G slot to its Y slot and retains both identities.

The following semantic conditions are necessary.

- An A copying event preserves the template A slot and turns the consumed R slot into the new A. Free or bound Y reproduction likewise preserves the parent Y slot and assigns the R slot to the new Y.
- Binding and dissociation preserve both carrier identities. G–fuel binding preserves the G slot; fuel remains an untagged packet.
- GF wear marks the G slot and releases its packet. YG G-wear marks only G and releases the same Y. YG Y-wear marks only Y and releases the same G.
- C↔CF charging/leakage and paid access to a CF packet preserve its C carrier. CF wear marks that carrier. No recycling, assembly, formation or fabrication clears a wear mark.
- Every elementary choice of catalyst and consumed slot retains its multiplicity. Equivalent choices may be summed only after their rates and destinations are correctly formed. Existing YG complexes are actual bonds, not all possible G/Y pairings.

Before an original's first wear, its role and architectural type remain the same; the 42-channel law has no unmarked alternative route that turns a surviving original A into another type or a surviving original Y into something else. Therefore wear of all four originals entails at least one wear in each role, supplying the hypotheses of (S4). Counting four arbitrary wear events would not supply those hypotheses.

Slots whose originals have already worn can be canonically permuted because no future target distinguishes their former identities. The permutation must carry their current species and every bond endpoint along with it, and may not exchange surviving original identities. For this to be an exact quotient, sum the rates of all outgoing raw transitions to each canonical destination. The natural proof is an action of permutations of already-worn slots that preserves rates, physical outcomes and target flags. Such a quotient changes computational representation, not chemistry or failure probabilities.

When every original has worn, all four slots are eligible for this quotient; only the physical counts/bonds and any still-required entrance metadata remain. It is then unnecessary to retain four distinguishable dead-original names. The separate carrier-semantics audit checks this lifting obligation; no new success probability is inferred from a correct lift.

## 3. Material conservation does not bound free reserve

Two charged carriers give a material-restoring pump:

\[
\begin{aligned}
2CF+F^m
&\longrightarrow CF+D+F^{m+1} &&\text{CF wear},\\
&\longrightarrow R+C+F^{m+1} &&\text{paid recycling},\\
&\longrightarrow2C+F^{m+1} &&\text{assembly},\\
&\longrightarrow2CF+F^{m+1} &&\text{two captures}.
\end{aligned}
\tag{S5}
\]

Here \(F^m\) denotes a count of m packets, not a molecular complex. All unmentioned material is unchanged. The two captures supply two work units, and the carrier wear loses one; the net extra packet is paid for by the environmental source. Every selected reaction has positive rate. Leakage and all competing reactions remain present; the probability of any finite prescribed repetition is positive, not one.

From the actual initial R3,Y1,F2, two assemblies and two captures reach CF2,R1,Y1,F2. Thus the pump can repeat while retaining a Y lineage and remaining outside the entrance family. After n repetitions, the route

\[
\text{A formation}\to\text{CF wear}\to\text{paid recycling}
\to\text{G fabrication}\to\text{Y binding}\to\text{capture}
\tag{S6}
\]

first enters \(P_{ii}(n+1)\). The earlier direct five-event route first enters \(P_{ii}(0)\). Therefore every nonnegative free reserve occurs on some positive-probability first-entrance path. Every such finite path can fit within any positive deadline, albeit with potentially minute probability.

Consequently no hard finite cap on F or total packets U follows from N=4, including when all entrance histories are retained. The one-slot retained-scaffold restriction from [the earlier storage note](USEFUL-RETENTION-MECHANISM.md) must not be applied after scaffold turnover opens further material slots. The old capture-count truncation remains valid, but it is conservative rather than necessary.

A useful supplementary count is

\[
Q=F+GF_0+GF_1,\qquad
S=W+Q=N-D+CF+2Q.
\tag{S7}
\]

Every capture raises S by one and every other declared channel preserves or decreases it. Initially S=8. Thus \(S_t\le8+K_{\rm capture}(t)\). At \(P_{ij}(m)\), S=5+2m, so first entry requires at least 2m−3 captures when that bound is positive. This does not impose a finite reserve maximum; the pump meets continued growth by consuming further source captures. S is a derived counting potential, not an independently calibrated thermodynamic free energy.

## 4. Leakage gives a stronger probabilistic reserve bound

Although F and U are unbounded, the mobile pool Q has a simple domination. Under the exact unit-coefficient forward law:

1. Its only upward reaction is CF wear, which raises Q by one, with propensity CF.
2. Before Y-lineage loss, at least one of the four material units belongs to Y, so CF≤3.
3. Free-fuel and GF leakage remove mobile packets at total propensity F+GF0+GF1=Q. Formation, fabrication and free-fuel recycling can only add further losses from Q.
4. Fuel binding, dissociation and GF wear preserve Q. Capturing into CF is not a birth in Q.

Stop Q at zero if the Y lineage is lost; that failure cannot later satisfy these organizational tasks. Couple it to an immigration–death process Z with birth rate 3, death rate z in state z, and Z0=2. Every actual birth can be embedded in a rate-3 stream with unused births assigned only to Z. Match each actual mobile packet with one Z particle, remove both on its unit-rate leakage, and allow extra actual consumptions to remove only the actual packet. Remaining Z particles have their own unit-rate death clocks. This constructs

\[
Q_t\le Z_t\quad\text{for every }t\ge0
\tag{S8}
\]

before the task's irreversible failure, without assuming that Q itself is a Markov state.

Each initial Z particle survives to t with probability e−t. Independently, rate-3 Poisson arrivals survive by independent exponential thinning. Hence

\[
Z_t\overset d=\operatorname{Bin}(2,e^{-t})
+\operatorname{Pois}(3(1-e^{-t})).
\tag{S9}
\]

For M≥2, an upcrossing from Q≤M to Q≥M+1 requires a CF-wear birth while Q=M. By the counting-process compensator, its expected number before H is at most

\[
3\int_0^H\Pr(Q_t=M)dt
\le3\int_0^H\Pr(Z_t\ge M)dt.
\]

The probability of at least one such crossing is at most the expected count. The binomial term in (S9) is at most 2 and the Poisson mean is at most 3, giving the conservative, easy-to-certify bound

\[
\boxed{
\Pr\{\sup_{t\le H}Q_t>M\}
\le\min\{1,\ 3H\Pr(\operatorname{Pois}(3)\ge M-2)\}.
}
\tag{S10}
\]

This simultaneously bounds overflow of F beyond M and first entry with reserve m>M. It includes the whole history from R3,Y1,F2, with all unfavorable events retained. It is not a stationary approximation or conditioning on survival. The process is stopped only at an exact task-failure boundary.

At H=10, exact rational positive-series bounds give:

| Threshold M | Upper bound for any mobile-pool upcrossing above M |
|---:|---:|
| 20 | <1.074×10^-7 |
| 25 | <6.217×10^-12 |
| 27 | <9.223×10^-14 |
| 30 | <1.251×10^-16 |
| 35 | <1.049×10^-21 |
| 40 | <4.180×10^-27 |
| 90 | <8.082×10^-93 |

Thus, for example, a free-packet cap of 40 can have a stronger a priori error bound than the earlier cap-90 capture-count estimate. Choosing and recording a computational cap from a stated accuracy requirement changes numerical approximation, not the physical model. It does not authorize dropping a failure branch, changing a rate, or reporting a sign smaller than all remaining numerical error.

For general positive coefficients, the same argument uses CF-wear bound \(\lambda=3b\) and per-packet leakage lower bound \(\ell_* =\min(\ell_F,\ell_{GF})>0\). The dominating process has stationary Poisson parameter \(\lambda/\ell_*\). The displayed numerical table belongs only to the declared unit rates. Reverse channels, packet-producing sources outside CF wear, or loss of the positive leakage bound require a new argument.

This whole-preparation bound must not be applied unmodified to a conditional kernel newly started at \(P_{ij}(m)\): its initial mobile pool is m, not 2. For the unconditioned composition (S3), however, the common initial-state bound controls every pre-entry and post-entry overflow up to the same absolute H. This avoids multiplying a global truncation error by the number of entry-reserve classes.

## 5. Truncating entrance reserve without selecting successful histories

One permissible computational decomposition retains every first entry with m≤M and omits all higher-reserve first entries. Let

\[
\varepsilon_{\rm ent}(H)
=\Pr\{\tau\le H,\ F_\tau>M\}.
\tag{S11}
\]

It can be bounded either by (S10), or by a separately certified high-reserve reward in the first-entrance graph. The latter may be sharper; its numerical enclosure and any graph overflow must be included. None of this permits renormalizing retained entrants to probability one.

Suppose the retained calculation has interval [L,U] for the same whole-preparation event, including all exits and the absolute deadline, while additional within-path killing has probability at most \(\varepsilon_{\rm cap}\) in the original process. Then

\[
\Pr(\mathcal R_H)\in
[L,\ U+\varepsilon_{\rm ent}+\varepsilon_{\rm cap}],
\tag{S12}
\]

and the same holds for the reserve-restoring event and separately retained entrance classes. If the error bounds overlap, the sum is still conservative. A global cap error need only be added once to the complete composed probability. For a directional comparison, the certified lower endpoint of one event must exceed the certified upper endpoint of the other; rounding, entry truncation and later overflow all count.

The entry reserve is passive metadata for the post-entry dynamics. It changes the initialization and the endpoint predicate \(m'\ge m\), but does not change a reaction channel. Therefore one may share the same tagged transition matrix across entry-reserve classes, propagating separate source/right-hand-side columns or convolving each entry source with that common semigroup. This saves duplicating the physical graph; it does not allow averaging away the reserve dependence of the target. Initial architectural labels can likewise remain passive classification records while the final types evolve under the common law.

A numerical warning matters for rare events: a 2^53-scale integer iteration can have an absolute rounding enclosure that exceeds a tiny omitted entrance mass. More matrix steps do not repair that floor. A high-reserve reward may need higher precision, or one can use a threshold whose analytic bound (S10) already meets the required absolute accuracy. No particular sign or practical reliability follows before the successor calculation is actually certified.

## 6. Necessary-time bounds that keep entry separate from renewal

At any entrance, each original carrier has first-wear hazard exactly one in every allowed binding state. Until its own wear, its role persists. The two constituents of YG have distinct unit-rate wear channels. Thus their four first-wear times can be constructed as independent Exp(1) clocks, started at entrance by the memoryless/strong Markov property. Other reactions alter binding and resources but not these four hazards.

For any entry \(\xi\), a complete turnover by elapsed time s requires all four first wears, so

\[
K_\xi([0,s])\le(1-e^{-s})^4.
\tag{S13}
\]

This is an upper bound because wear may cause unrecoverable failure, and rebuilding takes additional time and resources. A proof that the wear clocks finish is not a proof that a successor exists.

A reserve-restoring turnover also requires at least six fresh post-entry captures by (S4). Capture intensity before lineage loss is at most three. Therefore

\[
K_\xi^{\rm restore}([0,s])
\le\min\{(1-e^{-s})^4,
\Pr(\operatorname{Pois}(3s)\ge6)\}.
\tag{S14}
\]

No independence between the wear event and capture count is asserted; taking the minimum of two necessary-event bounds does not require it. Integrating the right sides of (S13) or (S14) against E(dt,dξ), with s=H−t, bounds the corresponding unconditional events. These bounds can serve as checks on a numerical result. They do not give a lower bound, order the two gate types, or establish indefinite repetition. The earlier finite-lineage extinction limitation still applies to this finite-material forward law.

## 7. Exact check and review scope

The independent [checker](../../../../experiments/shared-renewal-capability/full-successor-critique/exact_check.py) reconstructs all 42 inputs/outputs without importing the producer. It verifies material conservation, every increment of W, Q and S, the positive-rate pump, first-entry paths for several finite m, and the displayed analytic tail upper bounds. [Recorded results](../../../../experiments/shared-renewal-capability/full-successor-critique/exact-check.json) preserve exact rational values, input hashes and the script hash. All assertions use integers or exact rational arithmetic; decimal values are presentation only.

For the Poisson tail, the checker divides a geometric majorant of \(\sum_{k\ge n}3^k/k!\) by a finite positive partial sum below \(e^3\). This yields a rational upper bound, with no unverified exponential evaluation. The stochastic coupling, compensator and carrier-clock arguments are proved in the note rather than inferred from finite tests.

Read scope: the frozen full-entry producer and successor note were read in full, alongside the storage/pump-relevant parts of the earlier retention note and the previously reviewed typed and reserve-ledger interfaces. The independent carrier-lift reviewer is separately checking the new implementation. This note does not rerun the entrance producer, validate chemistry, certify a new full-successor probability, or edit its protocol or computation. Its positive contribution is a tractable and rigorously bounded route to that still-required whole-ensemble calculation.
