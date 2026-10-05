# Repeated renewal: a rate-derived reliability boundary

5 October 2026. Independent AI-assisted critique and positive design constraint after `e214ecf80474396856e176430e0a8f86e819ddc4`. This note uses the existing 42-channel forward chemistry and its actual organizational successor states. It changes no reaction, rate or assay. The companion [composition note](REPEATED-RENEWAL-COMPOSITION.md) supplies the full successor/time/resource kernel; the result here bounds that kernel from a specific physical mechanism rather than assigning an unfavorable success probability.

**Advance.** In the current four-slot law, each returned organization again has exactly one Y carrier. Before replacing that carrier, it must produce a descendant faster than it can lose its only lineage. This gives a uniform cycle-success bound, independent of the amount of stored fuel or the capture rate. At unit rates, ten complete turnovers have probability at most **59049/1048576 ≈ 0.0563135**, even starting from an already formed organization and allowing unlimited time. The existing positive first-successor results remain valid; they cannot constitute reliable repeated operation in this architecture. A paid lineage-protection, replacement, restart or redundancy mechanism is now a concrete necessary research target.

## 1. Declared process and scope

Use the same finite material count N=4, the same 42 elementary forward channels, and the same family of organization states P_ij(m): one fabricator A_i, one gate G_j bound to the sole Y carrier, one charged capture unit CF, and m free packets. At a cycle boundary, label the four currently present original carriers. A completed cycle is the first later admitted organization after all four originals have worn. Carrier replacement and type changes are allowed as already declared. This is the [full-successor event](FULL-SUCCESSOR-RESULT.md), iterated at its actual stopping boundaries, not repeated fresh preparation.

The proof uses only the following facts about the channel table:

1. Y is born only through free or permitted bound reproduction. If the common free coefficient is β and bound coefficients are ζ_jβ with 0≤ζ_j≤1, total birth intensity is at most β R L, where L is the number of Y carriers, free or bound.
2. Every intact Y carrier wears at rate d in either binding state. No channel creates a Y lineage from L=0; reverse wear or immigration is absent.
3. Material count is conserved; Y occupies one material unit and R another.
4. Every admitted organization has L=1. Its incoming reserve, fabricator and gate types may vary.

The certified current case has β=d=g=1. The rate symbols below expose the mechanism and permit the explicitly stated class extension. A changed law with immigration, reverse Y wear, autonomous template-free Y production, nonconstant protected wear, or several Y carriers at return needs a new bound. Source power alone does not change these four premises.

Analyst labels define a path event; they do not install a physical sensor or controller. Their experimental observation is a separate paid operation (§6).

## 2. Uniform singleton-lineage race

Before the first new Y birth after an organizational boundary, L=1 and R≤N−1. Consequently its birth intensity is at most

\[
\lambda=\beta(N-1),\qquad q=\frac{\lambda}{\lambda+d}.
\tag{C1}
\]

Couple all possible Y births to a rate-λ Poisson proposal stream, accepting a proposal with the current actual birth-rate/λ probability. The original Y has a separate Exp(d) wear clock because its wear hazard remains d in every free/bound state. Until the first birth or this wear, all other reactions can alter the acceptance rate and binding state but cannot invalidate those bounds.

Let T be the duration of a successful complete original-carrier turnover; set T=∞ on noncompletion/failure under the declared cycle rule. Complete turnover requires at least one Y birth before the only original Y wears. In particular, if T≤t, the first potential birth occurs by t and before that original wear. Therefore, uniformly over every organizational state x, its reserve and gate/fabricator type,

\[
\Pr_x(T\le t)\le G(t)
=q\bigl(1-e^{-(\lambda+d)t}\bigr),\qquad t\ge0.
\tag{C2}
\]

This is an order of cumulative subprobabilities, not an assertion that the actual return-time density is pointwise below the exponential density. The proposal may be rejected, and a successful birth is only one necessary part of turnover. Every other obstruction can reduce actual success further. Integrating (C2) to infinite time gives the uniform row bound q.

For N=4 and unit rates, q=3/4. This improves the earlier [general Y-extinction argument](SUCCESSION-DIRECTION-CRITIQUE.md): the first required birth has only one parent, so the relevant rate bound is 3β, rather than the general maximum 4β when several Y carriers exist. It also differs from the older [N=3 exact-return result](RENEWAL-RETURN.md), which used another chemistry and a single prepared state. Here the bound holds over the whole actual N=4 organization/reserve family.

## 3. Finite-deadline repetition without an independence assumption

At the first successful cycle boundary, there is again one Y carrier. Strong Markov conditioning applies at the actual boundary, retaining reserve, types and support state. Let p_n(x,H) be the probability of n further complete cycles by H. The uniform bound (C2) gives

\[
\boxed{p_n(x,H)\le G^{*n}([0,H])
=q^n\left[1-e^{-(\lambda+d)H}
\sum_{k=0}^{n-1}\frac{((\lambda+d)H)^k}{k!}\right].}
\tag{C3}
\]

**Proof.** For n=1 this is (C2). If the result holds for n−1, condition on the next return time t and its actual state y. The remaining success probability is at most G^{*(n−1)}([0,H−t]), independently of y. This is a nonnegative decreasing function of t. Cumulative subprobability dominance in (C2), with missing mass at ∞, implies the same order when integrating such functions. Thus the integral is at most the convolution in (C3). Induction completes the proof. The convolution of n copies of the defective exponential measure has mass q^n and the displayed Erlang time law. No independence or identical distribution of the actual cycles is assumed.

For an original preparation with successful entrance measure F_p(dt,dx), the unconditional n-cycle probability is at most the integral of the right side of (C3) at remaining time H−t against F_p. A looser bound is Pr(entrance by H)q^n. Failed formations remain in the denominator. Applying the entered-organization bound directly gives a still looser unconditional upper bound and does not silently reset the source or clock.

For unit N=4 rates, eventual upper bounds are:

| Complete turnovers n | Necessary success upper bound (3/4)^n |
|---:|---:|
| 1 | 0.75 |
| 2 | 0.5625 |
| 5 | 0.2373046875 |
| 10 | 0.05631351470947265625 |
| 20 | approximately 0.003171212 |

For n-cycle reliability at least 1−ε, a necessary rate/material condition is

\[
\frac{\beta(N-1)}d
\ge\frac{(1-\epsilon)^{1/n}}{1-(1-\epsilon)^{1/n}}.
\tag{C4}
\]

If β=d and only N changes while returns still contain exactly one Y, ten-cycle reliability requires N≥96 for 90%, N≥196 for 95%, and N≥996 for 99%. These are exact necessary thresholds, not suggested efficient designs or sufficient conditions. Additional material must actually be supplied, organized and supported. Finite deadlines impose (C3) in addition; merely increasing stored packets does not change (C4).

## 4. Capture throughput is a separate bottleneck

Let m_0,…,m_n be the actual reserves at n successive organizational boundaries and K_r the number of fresh captures during cycle r. The typed ledger and required original-carrier wear give

\[
K_r\ge6+m_r-m_{r-1},\qquad
\sum_{r=1}^nK_r\ge6n+m_n-m_0.
\tag{C5}
\]

Thus **final** reserve restoration m_n≥m_0 already requires at least 6n captures. Intermediate cycles need not each restore reserve. Tag reset at each boundary declares the new originals; it does not reset material, reserve or the external source.

Until Y-lineage extinction, at most three material units can be uncharged capture units. Fresh capture therefore has predictable intensity at most 3g. A dominating rate-3g Poisson proposal stream gives

\[
\Pr_x(\text{n turnovers by H and }m_n\ge m_0)
\le\Pr\{\mathrm{Pois}(3gH)\ge6n\}.
\tag{C6}
\]

Lineage extinction makes the target impossible, so there is no need to bound subsequent irrelevant captures. From an original preparation the same total-horizon bound is conservative: formation consumes part of the available time and may require extra captures. Combine (C3) and (C6) by their **minimum**, never by multiplying dependent events. These constraints identify different mechanisms: adequate energy throughput cannot remove singleton-lineage loss; lineage protection cannot supply the minimum work input.

The [exact diagnostic](../../../../experiments/shared-renewal-capability/repeated-renewal-critique/README.md) uses rational arithmetic and directed exponential enclosures. It certifies the quoted thresholds and finite-deadline upper-bound expressions. It does not calculate actual repeated-turnover probabilities or replace the general proofs with finite examples.

## 5. What a constructive reliability result must derive

The obstruction gives an experimentally meaningful next target: measure or derive the competition between required lineage production and irreversible loss over **all actual successful successor states**, then construct a supported way to change it. Candidate mechanisms include protected backup copies, an actual template-free/restart channel, or a larger coupled unit whose surviving partners can reseed a lost component. Their construction, access, loss and source costs must be present in the law. None is installed by calling the event “generativity.”

There is a useful sufficient race criterion for a concrete candidate. Suppose its actual continuation is partitioned into r physical stages with invariant safe regions. In stage j, the hazard of the required forward transition is at least a_j>0, fatal loss is at most b_j, and every other transition stays in that stage's certified region. A forward transition enters the next certified region; after the last, the actual successor lies in the region where the same bounds and funded support apply again. Every stage has its declared resource budget paid and every-prefix feasibility established.

Couple a rate-a_j forward clock and rate-b_j potential loss clock. Actual success can occur earlier and actual fatal loss later. With allocated duration t_j, conditional stage success is at least

\[
\ell_j=\frac{a_j}{a_j+b_j}
\bigl(1-e^{-(a_j+b_j)t_j}\bigr).
\tag{C7}
\]

An n-cycle sequence under those maintained premises then has success at least (∏_jℓ_j)^n within nΣ_jt_j and the paid total budget. This follows by conditional multiplication, not independence. A finite-time mechanism meeting nΣ_j(1−ℓ_j)≤ε yields reliability at least1−ε. Unlike assigning a favorable cycle probability, each a_j,b_j and safe-region closure can be checked directly against a reaction/event table and measured supporting conditions.

The present N=4 law does **not** meet such a high-reliability certificate: (C1) bounds its lineage race, and unchanged finite material cannot remove that limit. No concrete replacement mechanism satisfying (C7) is established here. The criterion identifies a falsifiable construction obligation; defining a region after selecting only successful trajectories would not satisfy it. Infinite successful continuation additionally requires feasible support at all stages and cumulative cycle times diverging. A fixed positive cycle-loss probability precludes that stronger event even when finite operation or an ensemble with paid restart remains useful.

## 6. RNA retention, physical reset and the unit of continuation

The [RNA one-stage calculation](RNA-PARTIAL-IDENTIFICATION.md) requires both RNA types to grow D-fold, then retains a fraction ρ=1/D of whole compartments and evaluates before fusion. For a specified tagged compartment sequence, conditionally uniform retention gives an upper bound ρ^n on surviving n such transfers. This is a statement about that tagged history. It does not bound an ensemble's ability to create useful daughters after replication, mixing or partition; those processes change the unit and the successor kernel.

There is also a stronger closure issue. Discarding whole compartments does not dilute the counts inside a retained compartment. In an unchanged bounded compartment, n successive D-fold rounds relative to each round's actual start require

\[
D^n(h_0+p_0)\le C.
\tag{C8}
\]

For the declared conventional two-RNA flow with r=b/a>1 and no mixing/partition/reset, the preserved trajectory relation p(t)=p_0[h(t)/h_0]^r strengthens this to the necessary finite-time condition

\[
D^nh_0+D^{nr}p_0<C.
\tag{C9}
\]

For example D=5,C=300,h_0=p_0=10 already excludes two unpartitioned rounds by (C8). More sharply, h_0=p_0=1 is a certified successful one-stage preparation in the earlier conventional calculation, yet its r>2 implies that two unpartitioned rounds would require 25+5^(2r)>650>300. These are model specifications and deductions, not measured biological capacities. The one-stage assay therefore cannot be iterated as J^n. An actual partition/transfer law must return material and association to a viable scale, with replenishment and waste accounted for. If the meaningful continuing organization spans several daughters, record their joint configuration instead of following one label. Daughter number alone is insufficient: the required host–parasite association and apparatus must actually be inherited or reconstructed.

Selection also requires a physical link to the shared task. For the same conventional equations, write f=p/(h+p) and φ=1−(h+p)/C. Direct differentiation gives

\[
\dot f=\frac{(b-a)h^2p\phi}{(h+p)^2}.
\tag{C10}
\]

Inside capacity, b>a increases parasite share. Meanwhile the joint D-fold feasibility boundary Dh_0+D^{b/a}p_0<C becomes more restrictive as b/a increases. This is a concrete kinetic mismatch between relative propagation and that shared task, not a free assignment of fitness weights. It does not show every faster parasite lowers every finite-horizon functional probability; it shows ordinary relative-frequency enrichment does not imply the declared joint replacement capacity. Actual compartment transfer can alter that relation and must be included before claiming ensemble direction.

A physical renewal assay must also survive its own measurement. Let M be the actual readout/preparation transition after a successful physical cycle. The repeatedly observed process uses K followed by M, with its time, material, information and apparatus costs, unless the readout is shown to preserve the declared continuation law. “Nondestructive” need mean functional continuation remains available; it need not mean microscopic state is unchanged. Destructive endpoint measurements on independent preparations can estimate one-cycle laws, but do not demonstrate repeated monitored operation of the same physical unit. Analyst tags used in the mathematical event alone add no free information to a physical controller.

## 7. Provenance, review and what remains open

Actual reading scope for this derivation: full DIRECTION-AND-TURNOVER, RENEWAL-RETURN, FULL-SUCCESSOR-RESULT, REPEATED-RENEWAL-COMPOSITION draft and RNA-PARTIAL-IDENTIFICATION §§1–2; targeted verification of the Y-birth/extinction premises in SUCCESSION-DIRECTION-CRITIQUE and the inherited throughput/ledger argument in FULL-SUCCESSOR-CRITIQUE. The new RNA statements are algebraic consequences of the conventional model already preserved there. No primary biological source was newly inspected, no new biological fact is asserted, and no additional physical calibration is claimed.

The companion exact record preserves the base commit and SHA-256 hashes of its source notes and script. Independent formal review accepted (C2)–(C3), emphasizing sub-CDF order and decreasing continuation functions. The current CarrierTurnover Lean source and note were independently read: their necessity/ledger statements are sound within the explicitly permissive observer, while particle/bond consistency and Python-to-observer refinement remain outside that proof. No independent recompilation was performed in this critique.

This closes a named interface: a positive one-turnover event no longer stands in for reliable repeated operation, and the missing physical mechanism is identified by a quantitative threshold. The stronger positive goal remains open. It requires an actual paid continuation or ensemble mechanism that changes these rate/closure conditions and delivers a declared finite reliability, followed by a justified relation to a widening jointly available task set. Neither rare success, survivor enrichment, nor this obstruction establishes a universal direction toward shared generativity or moral 善.
