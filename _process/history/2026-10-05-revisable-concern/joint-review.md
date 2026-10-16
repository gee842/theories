# Independent review: scope learning and strategic access

5 October 2026. Reviewed the finalized `scope-math.md` and its interface with `access-math.md`. No author file was edited. Independent executable reconstruction: `independent_scope_audit.py`; results: `independent-scope-results.json`.

## Verdict

No substantive mathematical error found in the stated finite fixed-graph results. The division between Boolean admission, quantitative uptake, independent warrant, retained certificates, and operational delivery is coherent. The cut model is compatible **only within its now-explicit pre-admission or genuinely live-authority scope**; a communication cut is not a theorem of memory loss or normative retraction.

Two minor domain clarifications are worth making before preservation:

1. **Scope §3, definition of D/P, before S2.** Say explicitly: “For each free target j, an off-diagonal operational edge `i→j` is present exactly when `P_ji>0`; incoming edges to a pinned anchor do not affect its update.” The present statement that a positive matrix entry represents an edge does not literally exclude a nominal admitted edge into a free node with zero update weight. If such zero-weight edges count as D edges, the reachability/positivity equivalence fails: an anchor-to-target nominal edge with `P_target,target=1` leaves the target at zero. The proof and intended meaning already use positive support, so this is a domain clarification rather than a new limitation. The free-target qualification permits a bidirectional certificate graph while anchors ignore incoming updates.

2. **S2 maximum bound.** Explicitly assume at least one anchor, or define the stated upper bound as `max({0}∪{β_a:a∈A})`. With no anchors and zero initialization the conclusion is still zero, but `max_a β_a` is otherwise undefined. S1 and S1b legitimately discuss unanchored components, so spelling out the whole-graph empty-anchor case prevents ambiguity.

## Checks by claim

- **S1 hard closure and conflict:** equalities propagate along connected components; distinct anchor values in one component are inconsistent. Harmonic interpolation does not solve those hard equalities. The `1, 3/2, 2` path witness is correctly interpreted.
- **S1b Boolean admission:** I reconstructed all satisfying truth assignments of the anchor-plus-edge-implication clauses, independently of iterative propagation. For all **4,096 directed graphs on four nodes**, the intersection of satisfying assignments equals anchor reachability. There were **6,912 satisfying assignments** and **16,384 round-containment checks**. In **1,664 graphs**, other fixed points exist; the note correctly claims the *least* fixed point rather than uniqueness without coverage.
- **S2 averaging:** positivity from zero matches paths in the positive-weight graph. Unique global attraction requires every free node to reach an anchor in the reverse dependency walk; simple target reachability is insufficient when another closed dependency class can dilute it. The finite-path contraction argument is valid. Anchored bidirectional components with common boundary value converge to that value; unanchored zero components remain zero by initialization, not logical identification.
- **S3 deadlines:** explicit full-path enumeration independently matched **882 finite-time hitting probabilities across 49 rational dependency matrices**. The reverse-walk orientation and `τ_A≤t` indexing are correct. The strict threshold preserves the tie boundary. This describes algorithmic propagation, not a probability of moral standing.
- **S4 additions:** eventual convergence is justified under finitely many monotone additions and eventually fixed positive weights. The transient `7/8→11/16` example is exact and correctly defeats a blanket finite-time monotonicity claim.
- **S5 leakage:** the fixed point `λ(I−λQ)^{-1}Rβ` and discounted hitting expression are correct. Leakage guarantees forgetting of an isolated initial state, but also attenuates warranted remote influence and can remove valid concern after obstruction. The note correctly refuses to equate leakage with justified certificate retraction.
- **Retraction versus obstruction:** provenance invalidation is restricted to defeated certificates in K and preserves alternative derivations. Blocking D alone neither defeats W nor invalidates retained K. The isolated retained-state witness confirms the distinction. Paid storage/retrieval and explicit erasure or revocation attacks are necessary to connect this to strategic suppression of an already learned reason.

## Bridge to the cut model

The Boolean admission procedure supplies an exact bridge: before new claim admission, deleting every anchor-to-target route prevents that procedure from admitting the target, while leaving its warrant untouched. The controller can then compare a declared finite avoided burden against actual suppression costs. Shared cuts can avoid several burdens at once. This does not automatically cover numerical action thresholds: surviving paths may be too slow or diluted, and a retained local certificate may make the old path unnecessary.

Consequently preserve all three distinctions in the main chapter: **new admission versus retained concern; reachable support versus adequate/timely action; valid reason versus actual authority to implement it.** The current two memos already provide these qualifications. No further substantive change is required for their stated finite claims.

The independent checks are mathematical reconstructions of authored cases. They do not validate the anchors, relevance standard, certificate accuracy, material implementation, or actual strategic behavior of institutions.
