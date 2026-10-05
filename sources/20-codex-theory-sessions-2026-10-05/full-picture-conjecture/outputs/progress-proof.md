# Exact conditions for protected recurring progress

Prepared 2026-10-05. This is a mathematical characterization for a specified finite game, with an independent small-class implementation check for full observation and a proved obligation-monitor extension for partial observation. It does not establish that any physical or social domain satisfies that game model. It extends indefinite safety by requiring recurrent registered progress; it does not establish unbounded semantic novelty.

## A precise attainable answer

Let S be a finite state set, K ⊆ S the safe states, and P ⊆ K the states registered as progress. At each state s, the fully informed controller chooses an available action a, and an adversarial environment chooses the next state in F(s,a). Available actions have nonempty successor sets. The controller acts before the environment chooses the successor; there is no fairness restriction on that choice. The action sets are finite for the implementation below. A deadlock loses the infinite-continuation objective, even if its state lies in K or P.

Define, for T ⊆ K,

    CPre_K(T) = {s ∈ K : some available a has ∅ ≠ F(s,a) ⊆ T}.

An action with an unsafe possible successor does not satisfy this predecessor. Neither does an empty successor set. Thus restricting to the safe subgame must not mean silently deleting unsafe successors while retaining the original action.

The desired objective is: every resulting run is infinite, stays in K, and visits P infinitely often. Its exact winning region is

    W = νZ ⊆ K . μY ⊆ K . ((P ∩ CPre_K(Z)) ∪ CPre_K(Y)).       (1)

Here μ is the least fixed point and ν the greatest fixed point on subsets of K. In particular, s₀ ∈ W if and only if a causal strategy can guarantee this objective against every allowed environmental choice. A deterministic strategy depending only on the present state is sufficient. The theorem is conditional on the specified dynamics, observations, action order, safety predicate, and progress predicate, but it is an exact characterization within that class.

This is an instance of established Büchi-game theory. Section 2 provides our direct proof in this controlled-transition notation; source capsule A records the primary text and the slightly different displayed formula there. No novelty claim is made for the fixed-point method.

## Direct proof and a checkable controller certificate

Write Φ(Z) for the inner least fixed point in (1). All operators are monotone. Compute Z₀ = K, Zₙ₊₁ = Φ(Zₙ). This sequence decreases and stabilizes in the finite subset lattice. Each evaluation of Φ starts Y₀ = ∅ and iterates

    Yᵢ₊₁ = (P ∩ CPre_K(Z)) ∪ CPre_K(Yᵢ).

**Sufficiency.** At the final outer fixed point W, let r(s) be the first positive index i at which s enters the inner iteration. Rank-one states belong to P and have an available action into W. Every higher-rank state has an available action whose successors all have strictly smaller rank. Choose one such action at every state of W. Every successor stays in W. From any state, a rank-one progress state is reached after at most r(s)−1 transitions. From a rank-one state the next transition returns to some state of W, and the same descent repeats. All resulting runs are infinite and safe and visit P infinitely often.

Every W state consequently has an action into W. Hence P ∩ W = P ∩ CPre_K(W), so all progress states in W are rank one. The maximum rank is at most |W|. The extracted controller reaches the first progress state within at most |W|−1 transitions and has at most |W| transitions between successive progress visits. These are event-step bounds; a bound on elapsed physical time additionally requires bounds on event duration.

**Necessity.** Let V be the true winning region, allowing arbitrary causal history-dependent strategies. After any reachable history of a winning strategy, its residual strategy wins from the current state. Every successor permitted by its chosen action is therefore in V. In particular, any progress state reached by the strategy lies in T = P ∩ CPre_K(V).

The least fixed point Φ(V) is the finite sure-reachability attractor to T within K. To see the relevant direction without assuming memoryless winning strategies, consider a safe state outside this attractor. Every available action has either an unsafe successor or a successor still outside the attractor; otherwise that state would have entered the next attractor layer. The environment can select such a successor at each step. A deadlock already loses. Otherwise the controller either leaves K or avoids T forever. But a safety-and-Büchi winning strategy must eventually reach a progress state, and every such state lies in T. Contradiction. Thus V ⊆ Φ(V).

For a monotone operator, every postfixed set lies in its greatest fixed point. Therefore V ⊆ W. The rank construction proves W ⊆ V, establishing equality and the stated memoryless controller.

**Certificate form.** A finite set U ⊆ K containing the initial state, a selected nonempty-successor action at every s ∈ U, and positive integer ranks bounded by m suffice if: (i) actions at progress states stay in U; (ii) actions at non-progress states strictly decrease rank; and (iii) rank one occurs only at progress states. The fixed point constructs such a certificate whenever the objective is achievable. Conversely, such a certificate proves safety and recurrence directly. This is a concrete answer, not merely a request to test indefinitely.

Formal-core peer review: the independent formal agent checked the sufficiency/completeness argument on 2026-10-05 and confirmed the reachability-complement argument and rank bounds. This is a mathematical review, not a proof-assistant verification.

## Independent implementation check

`progress-check.py` implements (1). Its comparison oracle does not use a fixed point: it enumerates deterministic state-based policies, forms the induced successor graph, and rejects an initial state if an unsafe or deadlocked state is reachable or if a reachable directed cycle can remain entirely outside P. In a finite nondeadlocking graph, such a cycle exists exactly when an adversarial infinite run can eventually avoid P. The oracle therefore checks every environment path for each enumerated policy.

The verifier also checks the ranks/actions extracted from (1), and compares (1) with the standard variant whose second disjunct is guarded by ¬P. Their final winning sets agree in all checked cases. The primary source displays that guarded variant; our direct proof above establishes the unguarded variant independently.

Completed results in `progress-check-results.json`:

| Class | Plant/safety/progress cases | Initial-state verdicts | Policy enumerations |
|---|---:|---:|---:|
| All 256 two-state, two-action plants; each successor set may be empty; all 9 pairs P ⊆ K ⊆ S | 2,304 | 4,608 | 9,216 |
| All 2,401 plants with two safe controlled states, two actions each, and one fixed unsafe absorbing sink; nonempty successor subsets; all 4 progress sets | 9,604 | 28,812 | 38,416 |
| Seeded additional plants of sizes 3–6, 125 per size | 500 | 2,250 | 15,000 |

All comparisons and certificates passed. Four explicit edge examples below also passed. A policy enumeration means one positional choice tuple considered by the oracle; already-established winning initial states can skip redundant policy evaluation. The counts do not represent empirical observations or distinct mathematical theorems. These checks cover complete small classes plus a reproducible sample, and support the implementation; the general result rests on the proof.

## Controls that separate the requirements

1. **One success then stasis:** s → p → d → d, all states safe, P = {p}. Infinite safety is possible and progress is reached once, but W is empty. Reachability is insufficient for recurrence.
2. **Recovery and reset:** at s choose either s or p; from p return to s; P = {p}. Choosing recovery each time gives W = {s,p} and progress every two steps. This proves a maintained cycle of registered success, with no new states required.
3. **Unfair indefinite postponement:** s has an action with successors {s,p}, and p returns to s. The environment may always select s, so W is empty for P = {p}. A separate probabilistic model could yield an almost-sure result; possibility of success is insufficient for this adversarial guarantee.
4. **Progress deadlock:** P = K = {p}, with no available nonempty-successor action. The state is losing. The nonemptiness condition prevents a vacuous universal-successor test from labeling it winning.

## Exact extension under partial observation

Equation (1) is proved here for full observation. A concrete state-based controller cannot be deployed when two indistinguishable states require different choices. The companion safety result computes a greatest fixed point over information sets and requires one action to work for every state currently possible.

For recurrence there is a second issue: progress itself may be hidden. Consider two states a and b, one observation, forced transitions a → b → a, initial information set {a,b}, and P = {a}. Every actual path visits P infinitely often. The current information set nevertheless remains {a,b} forever and is never contained in P. Therefore applying a Büchi target of “current information set is contained in P” would reject a winning hidden-progress system. It certifies repeated *knowledge that progress holds now*, which is stronger in this example.

The missing memory can be supplied exactly in the finite, sure-winning setting. Maintain a pair (B,O): B is the nonempty current information set, and O ⊆ B ∖ P contains endpoints of compatible histories still owing a visit to P during the current progress round. Initially O₀ = B₀ ∖ P. For an action a and next observation class o, write

    Post(D,a) = ⋃{F(s,a) : s ∈ D},
    B' = Post(B,a) ∩ o,
    O' = B' ∖ P                         if O = ∅,
         (Post(O,a) ∩ o) ∖ P            otherwise.                 (2)

The controller may choose a only if it is available with nonempty successors at every s ∈ B. The environment chooses any observation class with B' nonempty. The safe product states satisfy B ⊆ K; product transitions into a B' containing an unsafe state remain possible and therefore disqualify an action from a safe predecessor. The product progress set is Q = {(B,O) : O = ∅}. This differs from B ⊆ P: histories can discharge their obligations at different times.

**Pathwise equivalence.** Fix any infinite observation/action branch. Between resets, O contains exactly the endpoints of its compatible concrete histories that have avoided P since the round began. This invariant follows inductively from (2). If O becomes empty infinitely often, each actual concrete run visits P in each completed round. Conversely, if O is nonempty forever after some time, take the tree of outstanding concrete histories from that round. It has nodes at every later depth. Finiteness of S makes it finitely branching, so König's lemma gives an infinite concrete suffix that avoids P; a compatible finite prefix exists because its initial endpoint was in B. Thus some actual run on the branch violates recurrence. Therefore all compatible concrete runs satisfy GF P exactly when the monitor visits O = ∅ infinitely often.

There is no hidden choice of an impossible observation branch in this proof. Every infinite branch with successive nonempty B has finite compatible prefixes of every length. The same finite-branching argument supplies a compatible infinite concrete run. Controller choices are fixed by the common observation/action history, so the witness respects the same causal controller.

The finite pair arena has at most 3^|S| states, before removing empty or observation-inconsistent beliefs: each concrete state is outside B, in B without obligation, or in O. Apply (1) to this arena with safety B ⊆ K and progress O = ∅. The resulting initial pair is winning **if and only if** an observation-based causal controller can ensure concrete safety and GF P from every state in B₀. A positional strategy in the pair arena implements a finite-memory controller in the original plant. Conversely, every original observation-based strategy induces the same branch choices in the product, and the pathwise equivalence preserves its winning condition. No probability or fairness assumption is used.

For the hidden a ↔ b example, B stays {a,b} while O starts {b} and becomes empty after the next transition. The monitor accepts correctly although B never lies in P. A monitor that resets because only *some* compatible history made progress would be unsound.

This is a specialization of the established breakpoint construction (source D), with our explicit safety, action availability, and game-quantifier proof. `progress-check.py` above checks the fully observed solver, not the product-building code. If the product is implemented separately, meaningful verification checks its synthesized controller in the **concrete state × controller memory graph** for unsafe/deadlocked vertices and P-free cycles. Enumerating only observation-memoryless controllers is insufficient as an exact oracle: the synthesized controller may need obligation memory.

## Recurrence does not imply unbounded distinct novelty

Fix a finite set L of distinguishable novelty labels, and let each candidate achievement receive a label in L under an unchanged interpretation. Across any execution there can be at most |L| first occurrences of labels. This is the pigeonhole principle, independent of control policy, survival, recurrence, or randomness. Repeating registered progress infinitely often cannot overcome the bound.

The restriction is the **fixed finite label repertoire**, not merely a finite controller. A finite controller can produce output words of arbitrarily increasing length, and a finite nondeterministic graph can generate nonperiodic infinite output. All finite words over even a finite alphabet form an infinite repertoire. Histories, an external tape, growing artifacts, or an unbounded counter can therefore carry infinitely many distinct objects while controller memory remains finite. Counting every longer prefix as a new object makes even repetition “novel”; the scientific or semantic significance then lies in the chosen novelty criterion.

For a substantive unbounded-novelty claim, specify: what objects can grow; the equivalence relation defining sameness; what counts as improvement or useful novelty; what resources the distinction and validation require; and which environmental behaviors are quantified over. An unbounded artifact space defeats the finite-label impossibility theorem but does not itself guarantee production, value, or indefinite resources. A growing schema can be modeled inside a larger ambient language; this does not by itself show that the system anticipates every possible future conceptual distinction.

The strongest warranted present claim is consequently: **within the specified finite controlled model, safe repeated registered progress has an exact winning-region characterization and a finite controller certificate; under partial observation the controller also tracks outstanding progress obligations.** Whether P tracks worthwhile progress, whether the model keeps matching the world, and whether genuinely unbounded novelty is possible remain additional questions. They are not refuted by this theorem, and they are not answered by relabeling a recurrent cycle “generation.”

## Primary-source capsules and actual-body locators

The capsules below delimit source-derived discussion. The proofs, counterexamples, and interpretation above are our explicit mathematical reconstruction and application. No direct quotation is needed. All four linked PDF bodies were opened and the stated sections read on 2026-10-05; search snippets alone were not used as evidence.

**A. Grädel, Lücking, Naaf (2021), _Semiring Provenance for Büchi Games: Strategy Analysis with Absorptive Polynomials_.** [Primary PDF](https://arxiv.org/pdf/2109.08327). Read §1–2, PDF pp. 1–4, especially the nonempty-successor finite-arena definition on PDF p. 3; and §5.2, PDF pp. 9–10, printed pp. 75–76. The authors treat an infinite-visit target in finite games and state positional determinacy. Their winning formula nests a least fixed point inside a greatest one, using a target branch that returns to the outer set and a non-target branch that decreases toward it. Their displayed non-target branch has an explicit complement-of-target guard. This supports the established lineage of the method; (1), its action-first adversarial predecessor, and the direct proof above are our formulation. Their semiring provenance contribution is not needed here. (Capsule: approximately 130 words.)

**B. Mitchell, Budzis, Bolyachevets (2019 preprint), _Invariant, Viability and Discriminating Kernel Under-Approximation via Zonotope Scaling_.** [Primary PDF](https://arxiv.org/pdf/1901.01006). Read §1 and §3.1–3.2, PDF pp. 1–2, especially equations (1), (5)–(7). This work makes the distinction between controllable safety and adversarial disturbance explicit in a discrete-time affine setting. It defines state constraints, controls and disturbances and constructs sound underapproximations of relevant safety sets. We use it only to locate the mature viability/robust-safety context. Its continuous state space, finite-horizon computational constructions, and input-signal notation are not identical to our finite sequential game; its quantifier notation should not silently replace our explicit causal action-before-disturbance convention. No progress or novelty conclusion is taken from it. (Capsule: approximately 120 words.)

**C. Chatterjee and Doyen (2010), _The Complexity of Partial-Observation Parity Games_.** [Primary PDF](https://research-explorer.ista.ac.at/download/3858/7872/2010_LPAR_Chatterjee.pdf). Read §2, PDF pp. 2–5; §3 and Theorem 1, PDF pp. 5–6; §4.1, Lemma 1, PDF p. 6. The paper separates safety, reachability and infinite-visit objectives; defines observation-based strategies; distinguishes sure, almost-sure and limit-sure winning; and distinguishes objectives visible in observations from general hidden-state objectives. It gives an automaton-product reduction to visible objectives and proves pure strategies suffice for sure winning. These distinctions explain why observation and acceptance memory cannot be omitted from the recurrence specification. The two-state hidden-phase example above is our own counterexample to one tempting belief-target substitution. We do not reproduce the paper’s complexity survey or claim to have implemented its general reduction. (Capsule: approximately 140 words.)

**D. Boker, Kupferman, Rosenberg, _Alternation Removal in Büchi Automata_.** [Primary PDF](https://faculty.runi.ac.il/udiboker/files/AlternationRemoval.pdf). Read §1, especially PDF p. 2; §2–3, PDF pp. 4–5. The authors explain that a subset-contained-in-target acceptance test incorrectly demands simultaneous accepting visits by different runs. They describe the breakpoint construction as retaining a reachable-state set S together with O ⊆ S ∖ α, recording runs that still owe an accepting visit, and identify Miyano and Hayashi as its source. Their original results concern sharp translation bounds and improved constructions for restricted automata. We use the explicit two-set account as primary research context for our specialized monitor, not as a claim that our game construction or the breakpoint idea is new. The correctness proof of (2) above makes the adaptation independently assessable. (Capsule: approximately 140 words.)


This proof accompanies [What makes protected generation possible](conditions-for-continued-generation.md). The checkers, exact results, independent reviews, and target challenge are in the [evidence bundle](continuation-root-evidence.zip).
