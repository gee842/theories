# Revising the scope of a stated reason: finite closure, diffusion, and retraction

5 October 2026. A mathematical continuation of the concern-learning specimen. This memo works only inside a declared finite model. It does not derive bearer-independent reasons from physics or claim that every recipient's standing is determined by a graph score.

## 1. Warrant, retained evidence, and operational delivery

A node is a **case–reason pair**, not a whole person. A case includes the context relevant to one explicitly named reason: for example, one specified kind and degree of avoidable harm under an available action. Different reasons or stakes have separate coordinates. Equal treatment of this reason coordinate does not imply identical needs, identical interventions, or identical all-things-considered duties.

The following objects are distinct:

1. **Warrant graph** `W=(V,F)`: an undirected edge `{i,j}` records independently warranted equivalence of the properties declared relevant to this particular normalized reason. A certificate concerns those properties, not whether the eventual choice is favorable. Similar appearance alone is not a certificate.
2. **Procedural commitment:** the evaluator accepts that changing the bearer while preserving those relevant properties does not change this reason's force. One or more anchor cases `A⊆V` have a declared positive reason value. This is a normative/procedural premise, not a finding of statistical similarity or a law of survival.
3. **Retained certificate graph** `K_t`: records the equivalences the process has audited and retains as valid. In the noiseless sound-certificate model, its edges belong to W. A mistaken certificate can be defeated by relevant counterevidence; the record then needs correction.
4. **Installed transfer graph** `D_t`: an edge `i→j` means an admitted reason or its support can actually enter the update at j. In the baseline, each retained certificate is represented by both orientations. Access failures, refusal, or asymmetric delivery can make D directed and incomplete even while K retains a valid certificate. A missing installed edge does not refute the warrant, erase a valid retained reason, or remove standing.

The operational state `x_i(t)` measures the procedure's currently installed support for this reason. It can initially be zero outside anchors. Zero means absent operative support in this implementation; it does not mean the recipient has no standing or that the underlying reason is false.

Graph harmonic extension and its random-walk interpretation are established mathematical machinery, including Zhu, Ghahramani, and Lafferty, *Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions* (ICML 2003), https://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf, especially §§2–3. The application below keeps its graph and boundary assumptions explicit; it makes no novelty claim for harmonic learning and does not turn that method into a moral justification. All stated propositions are proved directly here.

## 2. What hard bearer-independent reason preservation forces

Write the exact commitment as

\[
y_i=y_j\quad\text{for every }\{i,j\}\in F,
\qquad y_a=\beta_a>0\quad(a\in A).
\]

**S1 — Component closure and its limit.** These constraints are consistent if and only if all anchors inside each connected component prescribe the same value. When consistent, every node in an anchored component has that component's anchor value. Each component with no anchor has one unconstrained common value.

**Proof.** Equality propagates along every finite path, so all values in a component coincide. This makes conflicting anchors impossible and propagates a consistent anchor to every node there. Conversely, assign each anchored component its common anchor value and each unanchored component any common value. Every edge equality and anchor condition then holds. ∎

Thus the stated premises force transfer within their justified closure, not universal scope. In an unanchored component, assigning all values zero or all values one can satisfy exactly the same edge and anchor data. Restricting values to `[0,1]` still leaves that underidentification. No observation elsewhere removes it without a new reason, an added valid relation, or another explicit commitment.

If a new recipient is connected by a genuinely warranted edge to an anchored component, retaining the old identity exclusion violates this declared hard commitment. That is a logical consequence of the commitment plus the certificate. It is not proof that an actual learner will implement the consequence.

**Mistaken equivalence matters.** If an edge omits a relevant difference, closure transfers the reason incorrectly. If two anchors inside a putative equivalence component prescribe different values, the constraint system reports a conflict. It does not decide whether to revise an anchor, the normalization, the relevance specification, or the edge. Averaging the two values is a different procedure, not a proof that the conflict was resolved.

## 2a. A finite operative reason-admission procedure

A Boolean procedure makes the logical installation step concrete before considering emotional or numerical salience. Fix a graph D of available, admitted transfer routes whose certificates are valid. Let S_0=A be accepted anchors and set

\[
S_{t+1}=S_t\cup\{j:\exists i\in S_t\text{ with }i\to j\text{ in }D\}.
\]

An accepted node means this particular reason has been admitted into the procedure; it is not an assertion of an all-things-considered duty or a scalar value of the whole recipient. Every transfer carries its anchor-and-edge provenance. Each round requires its declared actual communication, checking, and admission operations.

**S1b — Least admission closure and exact delay.** The accepted set after t parallel rounds is precisely the set of nodes at directed distance at most t from A. The least fixed point is anchor reachability, attained after at most `|V|−1` rounds when A is nonempty. A node's first admission round is its shortest directed distance; unreachable nodes are never admitted by this procedure.

**Proof.** The statement at t=0 is the initialization. One additional update appends at most one edge to a previously admitted path, and every path of length at most t+1 either already qualified or has a predecessor at distance at most t. Induction proves the characterization. A reachable node has a simple path from an anchor of at most `|V|−1` edges. The resulting reachability set is closed and is contained in every edge-closed superset of A, proving leastness. ∎

This is actual procedural scope expansion from initially unadmitted cases, not a direct reward for protecting them. It relies on the explicit commitment to accept certified reason-preserving transfers. A learner can decline that procedure; factual information alone does not compel its execution.

**Memory changes a cut model.** If validated reasons have already been retained, the correct starting set is the retained set S_0, not necessarily the original anchors. A blocked operational edge cannot remove members from this monotone admission rule. Reachability from the original anchors characterizes new or reset successor admission only when no relevant prior admissions or copies survive. To remove an already retained operative reason, an adversarial model needs an additional mechanism—memory erasure, suppressed retrieval, revoked authority, or another specified failure—not a silent reset of S.

If a certificate is actually defeated, a different update is needed: invalidate derivations using it and recompute from remaining valid anchor/certificate records, preserving any alternative valid derivation. Mere communication obstruction triggers no such warrant invalidation. The averaging model below then describes numerical uptake and response delays, which need not coincide with Boolean admission.

## 3. An explicit local update that starts at zero

Fix D and nonnegative weights. At a free node j, let its update row average the states of its admitted incoming predecessors, optionally including its own state. Write

\[
x_j(t+1)=\sum_{i\in V}P_{ji}x_i(t),\qquad
\sum_iP_{ji}=1.
\]

For a free target j, an off-diagonal installed edge `i→j` exists if and only if `P_{ji}>0`. Pinned anchors ignore any incoming certificate edges for purposes of their update; their outgoing transfer routes remain available. If j has no incoming transfer, set `P_{jj}=1`. At every anchor a, set `P_{aa}=1`, all other entries of that row zero, and pin `x_a(t)=β_a`. Start with `x_j(0)=0` at free nodes. Anchors have already been established; their origin and maintenance remain premises or belong to the earlier learning model.

One concrete baseline for an accepted undirected graph is lazy weighted averaging:

\[
P_{jj}=1/2,\qquad P_{ji}=\frac{w_{ij}}{2\sum_{k\sim j}w_{jk}}
\quad(i\sim j),
\]

with positive symmetric edge weights, for nonisolated free nodes. An isolated free node keeps its state. Every update and observation requires an actual implementation and paid opportunity; mathematical ticks are not free work.

Order free nodes U before anchors A. Then

\[
x_U(t+1)=Qx_U(t)+R\beta,
\qquad
x_U(t)=\sum_{k=0}^{t-1}Q^kR\beta.
\tag{1}
\]

**S2 — Exact convergence and coverage.** Assume finite V, fixed P, and nonnegative anchor values.

1. From the stated zero free initial state, every coordinate is nondecreasing, bounded above by `max({0}∪{β_a:a∈A})`, and converges to the least nonnegative fixed point of (1).
2. If anchors are positive, a node acquires positive support at some finite time if and only if it is reachable from an anchor in D.
3. The fixed point is unique and attracts every free initial vector if and only if every free node is reachable from some anchor. Equivalently, the reverse dependency walk defined by P has no closed class entirely among free nodes.
4. For the baseline bidirectional graph, all nodes in a component anchored at a common β converge to β. An unanchored component stays zero from the declared zero initialization; its value is not logically identified by that default.

**Proof.** Formula (1) is a nonnegative partial sum and hence increases. Convex averaging with pinned boundaries bounds it by the maximum of zero and the anchor values. If A is empty, the zero initial state remains zero. Its finite-dimensional limit satisfies the fixed-point equation by continuity. Any nonnegative fixed point h obeys `h≥Σ_{k<t}Q^kRβ`, so the limit is the least one.

A positive entry of `Q^kR` is exactly a product of positive transition weights along a reverse dependency path to an anchor, equivalently a forward installed-transfer path from an anchor. This proves statement 2.

Suppose every free node reaches an anchor. Select from each such node a reverse path to an anchor of length at most L=|U|. Finitely many positive transition weights have a positive minimum p. The probability of following the selected path and being absorbed by time L is at least ε=p^L. Therefore every row sum of `Q^L` is at most `1−ε`; repeated blocks give `||Q^{kL}||_∞≤(1−ε)^k`. Thus `Q^t→0`, the series converges, and

\[
x_U^*=(I-Q)^{-1}R\beta
\]

is unique and globally attracting. The case U empty is immediate. Conversely, if a free node cannot reach an anchor in the reverse walk, a finite closed free class exists. Altering the constant boundary value assigned to that class gives a different fixed extension; the fixed point is not uniquely anchor-determined. One explicit fixed extension is the expected terminal boundary value after declaring such closed classes absorbing boundaries. This proves statement 3.

On a bidirectional anchored component with common β, the constant vector β is a fixed point and statement 3 makes it the attracting one. An unanchored zero component has no source and remains zero. ∎

The proof of global attraction needs a fixed finite graph and fixed positive weights. Connectivity alone is not enough under arbitrarily shrinking time-dependent attention. For a single free node with anchor value one, take `x(t+1)=(1−ε_t)x(t)+ε_t`, where `ε_t=2^{−t−2}`. The edge exists at every date, but `x(t)=1−∏_{k<t}(1−ε_k)≤Σ_{k<t}ε_k<1/2`. A threshold of 3/4 is never crossed.

## 4. Hard equality and soft diffusion are different claims

With equal anchors on a valid bidirectional equivalence component, local averaging eventually implements the hard equality closure. At finite times it generally has not done so. The delay can matter to recipients.

With unequal anchors, averaging gives a harmonic compromise. For a three-node path with endpoint anchors one and two, the middle converges to 3/2. But the hard edge equalities require all three values to coincide and are inconsistent. The harmonic answer does not establish a morally correct interpolation between incompatible premises.

Directed partial delivery creates another distinction. Let anchor a have value one; let unanchored u keep zero; and let target j average a and u equally. Then a reaches j, but `x_j=1/2`. The qualitative existence of a route supplies positive support without equal support. Global anchor reachability, or an appropriate restriction on the target's dependency basin, is needed for full equal-anchor convergence.

For a permitted directed graph, the mathematical threshold concerns installed influence. It does not weaken the hard commitment corresponding to an independently warranted undirected equivalence. The strategic obstruction analysis can cut D while leaving W unchanged.

## 5. Exact finite-time meaning and deadlines

For normalized anchors `β_a=1`, define a Markov chain with transition matrix P, so its moves follow the update's reverse dependency direction. Anchors are absorbing. Let `τ_A` be its first hitting time of an anchor, with `τ_A=0` when starting at one.

**S3 — Finite-time transfer.** Under the fixed graph and zero free initialization,

\[
\boxed{x_j(t)=\Pr_j(\tau_A\le t).}
\tag{2}
\]

**Proof.** At time zero both sides equal one on anchors and zero elsewhere. Conditioning the hitting event on the first transition gives precisely the averaging recurrence. Induction proves the identity. ∎

If a declared feasible action is uniquely selected exactly when `x_j(t)>θ_j`, where θ_j incorporates the other fixed learned factors and action costs, then its selection **by deadline t** is equivalent to `Pr_j(τ_A≤t)>θ_j`. This equivalence uses the monotone fixed-graph trajectory from zero; it does not apply unchanged to arbitrary initial states or changing graphs. Equality remains a tie.

Reachability says eventual positivity, not timely protection. A chain of length d gives zero support before d updates. Small edge weights can make support negligible long after the first positive update. When every free node reaches an anchor, the proof of S2 yields the explicit lower bound

\[
x_j(kL)\ge1-(1-\varepsilon)^k.
\]

This is a sufficient deadline bound, often conservative. A threshold below one is eventually crossed; a strict threshold at or above one cannot be crossed from this initialization. The action's actual efficacy, authority, and financing remain additional requirements.

The probability interpretation describes the averaging algorithm's influence paths. It is not a probability that the recipient possesses moral standing or that the stated ethical reason is true.

## 6. Incremental admission after an observed counterexample

A finite procedural revision rule can be fully stated. In this baseline K is sound and its admitted edges are made available bidirectionally in D; strategic obstruction is a separate modification:

1. Enumerate candidate case–reason pairs and retain their relevant-property records separately from identity labels.
2. On a paid audit, test whether a candidate pair has a certificate of equivalence under the declared relevance specification. A counterexample to an identity-gated rule is a case with the same relevant properties and a different bearer, for which the procedure currently denies the anchored reason.
3. If the certificate is valid and no recorded relevant defeater applies, admit both transfer orientations. Do not require protective behavior itself as the certificate.
4. Run the paid local update. If new evidence invalidates the certificate, use an explicit retraction procedure rather than pretending the old graph was correct.

This rule makes acceptance of a counterexample consequential within the declared procedural commitment. It does not prove that an uncommitted actor must accept the commitment, that finite observations reveal every relevant property, or that factual similarity by itself supplies normative standing.

For a noiseless finite feature model, certificates can be equality of complete recorded relevant-property vectors. Outside that model, unobserved relevant differences and measurement error require an evidence standard and error analysis. Two possible worlds agreeing on every available observation but differing in an unobserved relevant property defeat any universal certificate guarantee based solely on those observations.

**S4 — Eventual closure under finite valid additions.** Use the bidirectional baseline: every admitted undirected edge supplies both transfer orientations. Suppose these edges are only added, each added edge is warranted, positive weights become fixed when their graph becomes fixed, and the initial free state is zero. Since there are finitely many potential edges, the sequence has a final admitted graph after its last actual addition. Thereafter S2 applies from the then-current bounded state. Every final anchored component with common anchor one converges to one; final unanchored components remain zero. If every edge in a designated finite warranted set is eventually audited and admitted, the same statement holds for that set's final component closure.

**Proof.** There are finitely many successful additions and each happens at a finite date, so their dates have a finite maximum. Apply the fixed-graph contraction on each final anchored component. A final unanchored component could not have been anchored earlier, because additions cannot disconnect a path; it therefore never receives an anchor source and stays zero. ∎

No uniform completion deadline follows from eventual audit without a bound on the audit schedule. Unlimited graph growth, endless retractions, or diminishing update weights require additional conditions.

**Adding an edge can temporarily reduce an existing score.** Let anchor a=1 be joined to j, initially zero, and let an isolated k also begin at zero. After three of the stated lazy updates, `x_j=7/8` and `x_k=0`. Add the valid edge `{j,k}`. The next scores are

\[
x_j^+=\tfrac12(7/8)+\tfrac14(1)+\tfrac14(0)=11/16,
\qquad x_k^+=\tfrac12(0)+\tfrac12(7/8)=7/16.
\]

A threshold 4/5 at j switches from protective to nonprotective. The hard reason closure widens and both free nodes eventually approach one, yet existing operational support drops at a finite date on the declared from-zero trajectory. Normalized attention to new cases can dilute old support. More admitted edges therefore need not produce a finite-time monotone benefit under a fixed attention budget.

## 7. Retraction needs more than deleting an edge

Suppose a mistaken edge carried an anchor's value to j. After learning, j has positive state. Delete that edge when its certificate is defeated. If j is now isolated, ordinary averaging gives `x_j^+=x_j`; the unsupported value remains forever. Correcting a defeated certificate alone does not retract the installed conclusion. Conversely, if the edge merely became unavailable while its warrant and record remain valid, retaining the learned support is appropriate; it is not evidence of a stale inference.

Two explicit responses have different meanings:

**Provenance invalidation after a defeated certificate.** Preserve the anchor-and-edge provenance of a transferred reason. When relevant evidence defeats a certificate in K, invalidate that certificate and recompute derivability from remaining valid records, preserving alternative derivations. Mark nodes with no remaining valid anchor derivation as unsupported by this route. Reinitializing their operational states to zero implements withdrawal of this particular derivation; it does not assert no independent reason or standing exists. **Do not do this merely because an operational edge in D is blocked.** A retained valid derivation continues to support the reason despite lost communication. Record storage, inspection, invalidation, retraining, and protected retrieval have actual costs and authority requirements. A simple finite implementation can inspect the retained certificate graph; efficient incremental implementations are possible but not assumed here.

**Leaky transfer.** For `0<λ<1`, keep anchors pinned and replace the free update by

\[
x_U(t+1)=\lambda[Qx_U(t)+R\beta].
\tag{3}
\]

**S5 — Forgetting unsupported influence.** For every fixed graph, (3) has the unique globally attracting fixed point

\[
x_U^*=\lambda(I-\lambda Q)^{-1}R\beta.
\]

Its contraction factor in maximum norm is at most λ. A disconnected free component loses any inherited unsupported state at least geometrically. From zero with positive anchors, positive limiting support still occurs exactly at anchor-reachable nodes. With unit anchors, the limit equals `E_j[λ^{τ_A} 1{τ_A<∞}]` for free j.

**Proof.** A substochastic Q has maximum row sum at most one, so multiplication by λQ contracts by at most λ. Summing its geometric series gives the fixed point and convergence. Each positive term corresponds to an anchor-reaching path and gains one factor λ per step. The expectation follows by grouping terms by hitting time. ∎

Leakage can remove obsolete unsupported influence, but it can also lose still-justified concern after mere communication blockage. It is not itself a normative certificate-retraction rule. It changes the target: it generally attenuates even warranted remote reasons below one. It therefore does not implement exact hard equality. A theory cannot claim both unrestricted forgetting and undiminished reason preservation without additional restoration or provenance machinery.

For arbitrary graph changes with fixed λ, two trajectories exposed to the same sequence contract toward one another by at most λ per step; this is fading initial-state dependence, not necessarily convergence to a fixed moral scope. Persistent changes can still produce a changing response.

## 8. Favorable information can fail to enter valuation

Consider two systems with identical accurate records of W, identical prediction of all recipient outcomes, and the same positive self anchor. System S installs the admitted bearer-independent transfer rule. System G stores the same equivalences only in its predictive representation and allows its evaluation row to copy self-related nodes alone. In G, other nodes retain zero operative support despite the favorable information.

Both fit all self-only training and all factual prediction tests. They differ on other-directed valuation because their installed procedures differ. Thus learning new facts can remove an epistemic excuse without causally removing an identity gate. If G has also undertaken the hard procedural commitment, its conduct violates that commitment; it is not a second consistent solution to S1 in an anchored component.

A complete scope-revision implementation therefore needs at least: a stated reason and relevance criterion, warranted case matching, authority to admit and retract relations, an installed valuation-transfer rule, paid update opportunities, protection of those routes from suppression, and an action route with sufficient resources and efficacy. The present note supplies finite logical and dynamical results for the first transfer steps. It does not derive the natural origin of the commitment or guarantee its strategic survival.

## 9. Verification

The adjacent `check_scope.py` uses exact rational arithmetic, graph enumeration, direct absorbing-walk propagation, and independent linear-system solutions. `scope-results.json` records checks of hard component closure, Boolean admission distances, finite-time hitting probabilities, directed reachability and dilution, stationary equality, edge-addition dilution, failed retraction, leaky correction, and diminishing-attention failure.

These are executable mathematical witnesses. They do not verify the ethical truth of the anchors, the completeness of a relevance criterion, or the real-world validity of a warrant edge. Those inputs remain exposed rather than being inferred from successful propagation.
