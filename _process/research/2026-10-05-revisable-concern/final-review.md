# Final independent review: revision and strategic access

5 October 2026. Reviewed `access-math.md`, the integrated `THEORY.md`, and `START-HERE.md`, against the finalized scope model. No root-authored or canonical file was edited. The two domain clarifications requested for `scope-math.md` were applied and checked separately.

## Verdict

**The substantive results are sound under their intended domains. Apply the explicit domain clarifications below before release.** The joint subset criterion is an exact iff for monotone gains and the specified feasible attack set. The combined chapter correctly separates warrant, retained support, procedural admission, numerical uptake, authority, paid conduct, and deadlines. It does not mistake a communication cut for memory erasure or successful propagation for moral justification.

## Corrections sent to the authors

1. **Cash and economic cost must have an explicit relationship.** Access §2 allows attack costs to include opportunity costs; §§3–4 then test affordability by `κ(S)≤L`. That test is exact if `c(F)` itself is the full upfront cash requirement. Otherwise use a distinct cash demand `p(F)` and define `κ_L(S)=min{c(F):F disconnects S and p(F)≤L}`. Example: an attack has economic cost 5, upfront cash demand 1, avoided burden 6, and reserve 1. It is feasible and profitable, although the unqualified test `κ=5>L=1` would call it unaffordable. The main chapter's general language about feasible attacks is compatible with either corrected formulation.

2. **Undeletable channels cannot be free cut edges.** The partition-cut and augmented-cut formulas must either assign an undeletable channel infinite capacity or exclude partitions that cross one. Omitting such a channel from the attack menu does not mean its crossing cost is zero. This matters particularly for the newly introduced source-to-anchor channels. State `κ(S)=∞` if no admissible disconnection exists. For finite computations, a capacity larger than the cost of an available finite comparison cut can stand in for infinity.

3. **State initial full reachability in the access appendix.** THEORY §8 already requires every target to be reachable in the intact graph. Put the same assumption in access §2 before the all-optima/some-optimum criteria. It is especially necessary for the weak-inequality existence statement: an already unreachable target with zero benefit has `κ=B=0`, satisfying a weak test even though no full-access outcome exists. With initial reachability, the no-attack comparator really is full access with payoff zero.

4. **Qualify retained records used as anchors.** A retained admission or a certificate/derivation sufficient to support the particular claim can supply an additional source. A retained equivalence certificate alone is an edge of K, not necessarily a positive anchor. Access §1's preceding sentence already uses “sufficient”; retain that qualification when describing additional anchors.

5. **THEORY §7 leakage domain:** write `0<λ<1`, not only `λ<1`. The scope proof and probabilistic interpretation use a positive contraction factor. The appendix already has the correct domain.

These changes expose existing intended assumptions; they do not require redesigning the finite game or transfer model.

## Exact strategic criterion

For initially reachable targets, nonnegative additive deletion costs, an empty attack with payoff zero, and a finite attack family, any excluding attack F satisfies `c(F)≥κ(S(F))`. Therefore strict subset inequalities make every excluding attack worse than the intact outcome. Conversely, when a cheapest cut of at least S costs no more than B(S), it can also exclude a superset S′. Monotonicity gives `B(S′)≥B(S)`, producing an excluding tie or improvement. This is exactly why the theorem requires monotone benefits. The weak version gives existence of an intact optimum; it does not select that optimum when exclusion ties.

A reserve filter preserves the proof if the minimizing cuts are genuinely feasible under that filter. With identical cash demand and attack cost, checking only subsets with `κ(S)≤L` is correct. With different demands, the constrained minimum `κ_L` is the appropriate object. The unconstrained augmented cut does not automatically solve a separate cash-constrained attack problem.

The additive augmented-cut identity is sound: the sink arcs encode the burdens of still-reachable claims; they do not carry claims themselves. Shared channels can make simultaneous exclusion cheaper than the sum of individual attacks. The supplied independent route can also travel from B through the shared review node to A; it is not limited to protecting B. The displayed cut values 3, 5, 5 are correct for that physical-channel example.

## Memory and practical scope

The pre-admission experiment is properly limited to new claims or genuinely untrained successor states. Surviving admissions, sufficient retained derivations, and continuing practices alter the source set and can make a former communication path unnecessary. To suppress an already effective concern, a model must include an actual retrieval, authority, memory, or implementation attack. Neither valid warrant nor normative standing is deleted by a delivery cut.

Boolean admission and numerical uptake remain separate. Reachability gives a least admission closure under the installed rule. Averaging can be diluted by an unanchored dependency, can arrive too late, and can temporarily decrease an old score when attention is renormalized. The main chapter retains the unit-anchor/zero-initial-state and fixed-process conditions needed for its finite-time hitting interpretation. Actual benefit and available money remain additional requirements.

The traceable-challenge protocol is a procedural commitment, not a theorem that favorable information must enter valuation. Its positive anchors, relevance language, certificate validity, authority, and direct intake for unfamiliar claims remain explicit. The main and reading guide do not overclaim invention of arbitrary values, universal moral convergence, or a complete resolution of plural duties.

## Independent verification

`independent_access_audit.py` uses residual max-flow augmentation, rather than the author's vertex-partition enumeration, and compares its answers with explicit deletion outcomes. `independent-access-results.json` records:

- 180 finite directed graph games;
- 540 subset cuts matched by residual flow;
- 180 additive augmented-cut optimizations;
- 1,438 strict/weak monotone subset comparisons with controller cash limits;
- explicit checks of the undeletable-edge, separate-cash, initially-unreachable-target, and onward-route cases.

All passed. These tests confirm the results under the stated domains and exhibit why the listed qualifications matter.

The only rerun of the scope checks was the affected domain subset: `check_scope.py --domain-only`. `scope-domain-checks.json` confirms the empty-anchor bound and the exact free-target edge/positive-weight correspondence, including the pinned-anchor exception. Existing broad checks were not repeated without a new reason.

All verification here concerns authored finite mathematical constructions. It does not validate ethical anchors, real equivalence certificates, actual institutional payoffs, or the completeness of any real attack model.
