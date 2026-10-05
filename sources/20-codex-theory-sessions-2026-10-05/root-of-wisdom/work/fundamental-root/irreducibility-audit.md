# Constructive audit: an irreducible root rather than a list of capacities

Independent research memo, 5 October 2026. Read-only review of the current root formalization and the latest scientific-principles and recursive-self-modeling work.

## Conclusion for the revision

The current tuple of judgment, generation, and revision specifies an architecture. It does not establish a smallest generative principle. The user is correct that a revision should seek a deeper invariant rather than attach further mechanisms to that tuple.

The strongest compact mathematical candidate found in this audit is:

> A representation may forget a distinction exactly to the extent that forgetting it leaves every admitted, independently interpreted consequence unchanged.

This admits a precise minimality theorem. The theorem is about faithful representation of a specified causal process. It supplies a structural root for objective understanding and connects directly to action, self-modeling, discovery, and inquiry. Its extension to wisdom requires a justified account of which consequences matter. Its extension to a universal physical law requires actual governing dynamics. Neither extension follows from invariance alone.

This is a positive mathematical result with a precise boundary, not a proof that a larger unification is impossible.

## The compact theorem

Begin with a deterministic controlled process: states X, a fixed common alphabet of admitted actions A, transitions T_a:X→X, and an independently interpreted consequence map c:X→Y. For a finite action word w, write T_w for the corresponding composite; the empty word leaves the state unchanged. The maps and action scope are supplied, not selected after seeing which answer would make the theorem true.

Define consequential equivalence by

    x ≈ y  iff  c(T_w x) = c(T_w y) for every finite word w in A*.

The all-words quantifier means that a distinction is disposable only if it cannot become consequential later. It does not require executing infinitely many actions to use a finite known process.

Let q*:X→X/≈ map each state to its equivalence class. Then there are well-defined quotient dynamics and output satisfying

    q* ∘ T_a = T̄_a ∘ q*,       c = c̄ ∘ q*.

Conversely, suppose q:X→Z is surjective onto its used states and admits exact dynamics and interpretation satisfying

    q ∘ T_a = G_a ∘ q,         c = d ∘ q.

Then there is a unique map h:Z→X/≈ such that q*=h∘q. Therefore every exact sufficient representation retains at least the distinctions retained by q*. Among representations with no duplicate consequential behavior, the result is unique up to relabeling.

### Proof

If x≈y, the empty word gives c(x)=c(y). For every action a and continuation v, equality for the word beginning with a gives c(T_v(T_a x))=c(T_v(T_a y)); hence T_a x≈T_a y. Both quotient definitions are therefore independent of representative.

For the converse, induction on word length gives q(T_w x)=G_w(q(x)). Thus q(x)=q(y) implies equal outputs after every word and hence x≈y. Define h(q(x))=[x]. The implication just proved makes this definition well-defined; surjectivity makes it unique. Any two exact representations whose fibers equal ≈ are bijective relabelings of the same quotient. □

This is a standard style of state-minimization/behavioral-equivalence argument; no novelty claim is needed. In a finite supplied system it gives an actual procedure: start with the partition by c; repeatedly split classes whose states have successors in different current classes under some action; stop when no split remains. The stable partition is ≈. Each strict refinement increases the number of classes, so finite termination follows.

### Independent exact verification completed

The script `check_coarsest_quotient.py` enumerates every three-state, two-total-action transition system (729 tables) and every binary state-output assignment (8), giving **5,832 systems**. For each it checks all five state partitions directly against output preservation and transition closure, independently computes a partition-refinement result, and compares the results. All **29,160 direct partition checks** matched the claimed unique coarsest faithful result; **9,990 faithful partitions** all factor onto the computed result.

A separate breadth-first search through paired states examined all **17,496 state pairs**. It produced and replayed an actual finite distinguishing action word for each of **11,772 inequivalent pairs**; the other **5,724 pairs** have no distinguishing continuation in their finite pair graph. The exact quotient sizes were one state in 1,458 systems, two in 1,350, and three in 3,024. All **34,992 bijective coordinate transports** preserved the quotient equivalence relation. The record stores count histograms and reproducible hashes of the complete system and witness sequences, rather than presenting a large archive as new evidence.

The same run verifies the four-state hidden-bit repair below and the covariance counterexample: identity, toggle, and absorbing dynamics all satisfy transported coordinate covariance; identity and toggle even share invariance under the entire two-state permutation group while having different dynamics. A compact result is saved in `coarsest-quotient-checks.json`.

These are exact finite checks of the mathematics, not behavioral experiments or evidence that the theorem is wisdom's root. The general result rests on the proof; physical implementation, consequences worth preserving, stochastic or infinite-state generalization, and feasible discovery are not established by enumeration.

An additional targeted check addresses a limitation of that exhaustive domain: three-state binary-output systems need at most one strict refinement. The five-state chain with outputs `(0,0,0,0,1)`, step `(1,2,3,4,4)`, and wait equal to identity requires **three strict refinements** and retains all five states. Direct checks of all **52 partitions** leave exactly the identity partition faithful, with its factorization verified. For states 0 and 1, breadth-first search finds three step actions as the shortest distinguishing word; separate enumeration checks all seven shorter words. Every one of the ten state pairs has a replayed distinguishing word. These targeted counts are kept separate in the JSON: only this specified five-state system was checked, not all five-state dynamics.

### What “irreducible” means here

No two distinct quotient states can be merged while preserving every admitted consequence. A distinguishing action word witnesses each forbidden merger. This is a rigorous, scope-relative minimality claim, much stronger than counting the number of symbols or clauses in an equation.

Absolute “fewest axioms” is not well-defined without fixing a language and a notion of equivalence: a conjunction can be renamed as one axiom, and an entire theory can be packed into a defined predicate. The revised work should claim semantic irreducibility relative to an operational scope, not irreducibility from typographical brevity.

## Assumptions that cannot be removed silently

The theorem's two commuting requirements are independent:

1. **Dynamics alone do not preserve meaning.** A constant q gives perfectly closed constant abstract dynamics for every T, but cannot preserve a nonconstant c.
2. **Present meaning alone does not preserve futures.** Let x=(v,h) be two bits, let q(x)=c(x)=v, and let an action set T(v,h)=(h,h). Present output factors exactly, but the next abstract state is not determined by v. The hidden distinction becomes consequential.
3. **All-action scope matters.** With only the identity transition, the visible bit v is sufficient in that example. Add the revealing action and all four states become distinct. New feasible interventions can require a richer representation without invalidating the old result in its old scope.
4. **Semantic scope matters.** A constant c makes a one-state quotient adequate. Taking c to be the identity preserves every state. The theorem does not choose what is worth explaining.
5. **A realizability bridge is separate.** A mathematically available action or observation is not thereby physically executable, affordable, permitted, or timely. State-dependent legal actions, resources, clocks, and costs must be included explicitly before the theorem is applied. The simple common-action version above does not prove these conditions.
6. **Finite exact dynamics are a domain, not a universal ontology.** Stochastic systems require equality of relevant controlled laws, not equality of expected outputs alone. Continuous, partially observed, and unbounded systems need corresponding measurable or approximate versions. Finite implementation and discoverability do not follow from abstract quotient existence.

## What this unifies from the other sessions

### Recursive self-modeling

The existing abstraction result C06 and conservation result C07 already establish the local commuting-square conditions. The quotient theorem adds a coarsest sufficient state and a precise minimality criterion. A representation called “self-model,” “meta-model,” or “flat augmented state” should be judged by its retained consequential distinctions and implemented access, not its verbal depth.

The shift construction in experiment/identifiability-proof.md is decisive. The simultaneous transformation

    (x,b,d,g) ↦ (x+c,b−c,d−c,g+(1−a)c)

preserves complete accessible observation and action histories under its stipulated shift-closed class. It does not preserve squared error against a fixed absolute physical zero. Observation invariance therefore cannot certify a fixed absolute target. Moving the target together with the coordinates would be a different, fully transported description. This is precisely why “invariant” must always identify what transformations, interpretations, and targets are held fixed.

The newer anchor-mechanism.md goes beyond formal ambiguity: a model with the wrong zero-forcing anchor can absorb the mismatch into both sensor biases and regulate the wrong physical origin. Protected acquisition, model fit, and agreement between model and controller can coexist with consequential error. The benchmark's fixed priors are not shift-invariant, and its exact finite filter convergence is not proved; those limits should survive quotation.

### Scientific change

The recent integrated-scientific-inquiry.md is a substantive addition to the earlier separate components. It implements ordinary service and income, complaints, paid inquiry, a council changing the mandate, fresh method checks, deployment, upkeep, loss, and rebuilding within one cash account. It reports 1,920 held-out simulated runs, 460 reconstructed comparisons, and 188 enacted changes. These figures were read from the report, not independently rerun in this audit.

The model supplies the feature grammar, a particular admission-rule edit, two mandate alternatives, council constitution, and a fixed conditional testing rule. It proves that such a feedback loop can be implemented, not that it autonomously invents all conditions supporting inquiry.

In quotient terms, four changes are genuinely different:

* A newly attended population changes the consequence map whose distinctions must be preserved.
* A new composite feature refines the representational partition.
* A changed admission rule makes an already expressible candidate reachable by search.
* Restored instruments or resources expand the executable intervention/observation scope.

They can alter the minimum adequate representation or whether the investigator can discover it. A blanket “preserve invariance” rule cannot prescribe all four transitions without their actual mechanisms.

The strongest negative control is the falling-income environment: preserving inquiry depleted means and caused more unserved requests than a fixed operating policy. Invariant adequacy is not “maximize revision” or “always preserve every future investigation.” Which future differences deserve resources still needs justified priorities.

## Where falsifiability enters

The mathematical theorem cannot be empirically falsified while its premises remain true; it can be disproved by a counterexample or error in proof. An application can be falsified: name the physical process, intervention implementation, measurement meanings, and claimed representation, then find an admitted action sequence for which its transported prediction or consequence fails. A claim about an approximate model must state error tolerances and the domain in advance.

This creates a concrete missing-possibility detector when evidence is available: find states or histories that the model treats as equivalent but whose future consequences diverge under a permitted operation. That witness forces a split, a dynamics revision, or a revision of the alleged implementation correspondence.

It is not a universal discovery algorithm. The possible splitter may be unrepresented, unaffordable, inadmissible, or observationally inaccessible. The scientific model contributes bounded mechanisms for changing those conditions. No theorem guarantees that every missing consequential distinction will present a witness within finite resources.

## The ethical bridge and the user's full ambition

Do not silently substitute “minimal predictive state” for the user's ambition to understand wisdom, the fundamental root, and truth. The theorem can connect those ambitions, but it does not equate them.

A perfect causal quotient can serve domination as accurately as care. All empirical and representational claims can remain fixed while a decision maker adopts a different ordering over consequences. Symmetry and positive consideration also fail to choose a unique ordering: minimizing total burden and minimizing the sum of squared burdens are both symmetric and improve under a strict componentwise burden reduction, yet rank (0,5) and (3,3) differently.

The strongest justified formulation is therefore:

> The structural root of faithful understanding is preservation of consequential distinctions through possible change. Wisdom requires applying that capacity under defensible concern for what those changes do to beings.

This is not the whole requested universal truth. It is a precise candidate for a foundational component, with a minimality theorem and explicit bridges still to justify. A larger root could incorporate a defended ethical axiom or a substantive theory of value; simply defining consequences to include “the ethically right ones” would conceal that additional work.

## Source files actually read

* root-of-wisdom/outputs/root-of-wisdom-formalization.md (complete).
* recursive-self-modeling/outputs/claims.md (complete).
* recursive-self-modeling/outputs/experiment/identifiability-proof.md (complete).
* recursive-self-modeling/outputs/correction-access/anchor-mechanism.md (complete).
* recursive-self-modeling/outputs/research.md (targeted abstraction and invariance passages).
* scientific-principles/outputs/scientific-change-formal-results.md (complete).
* scientific-principles/outputs/integrated-scientific-inquiry.md (complete, across overlapping reads).
* scientific-principles/outputs/theory-of-scientific-change.md (substantial passages; final tool output truncated).

All source workspaces remained unchanged. This memo is a fresh analysis, not a source author's assertion that the full root was already proved.
