# What an optimal foundational formulation can and cannot mean

5 October 2026. Adversarial mathematical review for the proposed reformulation of *Alignment as the Reproduction of Its Conditions*. This is new working analysis. The existing [foundation dossier](../FOUNDATION.md), its semantic state tuple, source snapshots and proofs are preserved as alternatives and evidence. This note does not claim a new universal optimality theorem or a completed novelty assessment.

## 1. Verdict and constructive recommendation

The strongest formulation should make the **situated causal process and its preservation requirements primary**, while treating a semantic tuple as one possible coordinate system. Describe actual mechanisms, actors' information and operative permissions, boundary inputs, timing, consequences, and the changes that can revise these conditions. Then state which distinctions a representation must preserve.

This earns two exact, useful optima in bounded classes:

1. The **unique coarsest faithful deterministic state quotient** for a specified finite intervention-and-observation contract. It minimizes the number of retained state distinctions among that class, preserves the relevant controlled path laws, and therefore preserves the corresponding stated decision problems.
2. The **least dependency-closed coordinate set** for supplied finite local mechanisms and seed outputs. It is optimal among coordinate sets satisfying that syntactic closure requirement, and is a constructive sufficient route to faithful reduction.

Neither theorem says the selected representation is the best causal science, the best observer memory, the most interpretable explanation, or the uniquely correct ontology. The tuple remains useful because it supplies interpretable hypotheses about mechanisms, measurements and interventions. Replacing it with an abstract kernel without that information would lose explanatory content despite greater formal generality.

A defensible claim is: **the preferred foundation supplies a rule for deriving the least adequate representation relative to a declared question and mechanism class, rather than imposing one supposedly minimal list of world-substances.** It must preserve a way to revise the question and class themselves. This is an optimality principle with exact bounded realizations, not a uniquely best model of all science.

## 2. Unrestricted encoding makes dimensional minimality empty

**Counterexample 1 — one variable contains the tuple.** Let the existing finite tuple range over a set `S` of `N` states. Choose any bijection `e:S->{0,...,N−1}`. Define the encoded transition by pushing the old transition through `e`, and decode every observation and intervention interface. Nothing is lost, yet the model now has one variable. The same construction works for any finite number of original coordinates.

Consequently, counting named variables cannot prove that three, five or eight primitives are minimal. A single arbitrary-precision real or integer can conceal an enormous state space. A meaningful comparison must charge for distinguishable states, precision, description length in a fixed language, execution cost, measurement access, or loss of modular intervention structure. These criteria need not choose the same representation.

The retained semantic tuple should therefore be labeled an **interpretable factorization**, not an independently proved irreducible ontology. A one-symbol encoding is a recoding, not a scientific discovery.

## 3. Conflicting objectives prevent an unqualified best representation

**Counterexample 2 — incompatible one-bit summaries.** Let `X,Y` be independent fair bits, and allow a deterministic summary with only two values. One future task predicts `X`; another predicts `Y`. Keeping `X` gives error vector `(0,1/2)`, and keeping `Y` gives `(1/2,0)`. No two-valued summary permits zero error on both, because all four pairs have positive probability and exact answers reconstruct the pair. Thus there is no summary simultaneously minimizing both errors. Weighted, lexicographic, minimax or hard-constraint comparisons make different commitments.

This is not a flaw in plural evaluation. It means that the phrase *optimal representation* must specify the comparison. Compression, causal faithfulness, explanation, inference cost, privacy, decentralization and revisability are different desiderata. The theory should permit a partial order and report incomparability.

Even exactness has a scope. A representation exact for present intervention effects may discard the experiment needed to identify a future mechanism. A representation optimal for average loss can violate a protected rare-event condition. A central analyst's smallest state need not be a participant's available state.

## 4. The exact finite optimum that is already justified

Fix a finite state model `S`, finite permitted inputs `U`, kernels `K_u`, and a preservation contract. The contract includes:

- Independently specified consequence labels and finite monitors for relevant process events, costs and deadlines.
- Every participant's actual observation map and action permissions.
- The permitted intervention family, with its implementation and boundary interpretation.
- Any installed controller memory or persistent disturbance needed for the claimed Markov description.

These objects describe what is to be preserved. They do not imply that the analyst sees everything, that participants share observations, or that the contract is ethically exhaustive.

A deterministic partition `P` is faithful when every contract label, observation and permission is constant within a block and, for every input `u` and pair `s,t` in one block,

\[
\sum_{v\in B}K_u(s,v)=\sum_{v\in B}K_u(t,v)
\quad\text{for every destination block }B\in P.
\tag{1}
\]

**Scoped optimality result.** Start from equality of the complete contract tuple, then repeatedly split states with unequal vectors of transition probabilities into current blocks under any input. The fixed point `P*` is the unique coarsest faithful partition. Every other faithful deterministic partition refines it. Therefore `P*` minimizes retained state count; its quotient is unique up to renaming within this class.

**Proof.** Refinement terminates because every strict step adds a block. At termination, (1) holds. Let `Q` be any faithful partition refining the initial contract partition. Inductively, if `Q` refines the current partition, every current block is a union of `Q` blocks. Equal transition probabilities to each `Q` block imply equal probabilities to their unions. Therefore no pair merged by `Q` is separated by the next refinement. Thus `Q` refines every iteration, including `P*`. Least state count and uniqueness follow. The equal block rows define the quotient kernel. Preserved participant observations permit corresponding policies, and induction preserves the relevant joint path law. ∎

For any fixed distribution over fine states, `q*(S)` is a deterministic function of every faithful summary `q(S)`. Hence `H(q*(S))<=H(q(S))`. This is a distribution-specific information consequence of refinement, not a new causal optimality result. Equality under a distribution can leave extra distinctions on null sets. State count also bounds the smallest fixed-width encoding, but several larger partitions can require the same rounded-up bit count.

This builds directly on the [existing local proof](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md). The mathematical lineage is established stochastic bisimulation and state aggregation; Givan, Dean and Greig also analyze how restricted symbolic representations trade smaller quotients against the cost of operating on them. [Primary manuscript](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

### A second optimum for supplied local mechanisms

For updates `z_i^+=F_i^u(z_Parents,eta)`, let the seed include every coordinate needed for the contract. Iterating

\[
R_{n+1}=R_n\cup\bigcup_{i\in R_n,u}\operatorname{Pa}_i^u
\]

gives the unique least parent-closed set. Every admissible parent-closed coordinate set contains it; it therefore minimizes any monotone coordinate-inclusion cost in that restricted class. Shared noise is allowed when its joint fresh law and selectors are correctly represented.

**Counterexample 3 — structural closure is not semantic minimality.** If the written update is `x'=x XOR y XOR y`, with `y'=y`, the read graph includes `y`, but the true update of `x` is just `x`. A seed concerned only with `x` has a two-state semantic quotient, whereas literal syntactic closure retains four coordinate states. The structural method is constructive and conservative; it must not be advertised as the universal smallest representation. See the [local structural theorem and its caveats](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/STRUCTURAL-CLOSURE.md).

## 5. This optimum is not minimality over every kind of predictor

**Counterexample 4 — output prediction can merge states that strong bisimulation separates.** Consider states `A,B,C,D,E,G,H`. Give `A,B` label `start`, `C,D,E` label `middle`, and distinct absorbing labels to `G,H`. Let `A->C`; `B->D/E` with equal probability; `C->G/H` with equal probability; `D->G`; and `E->H`.

Starting from either `A` or `B`, the complete label sequence is `start,middle,G,G,...` or `start,middle,H,H,...`, each with probability one half. Yet `C,D,E` cannot share a strong block, since their transition masses to the distinguished terminal labels differ. The successor block laws from `A` and `B` consequently differ. Thus complete output-trace equivalence is weaker than the strong state quotient contract.

A different class of predictive presentations may legitimately compress more when its question is only the label process. Conversely, stronger interventions or process observations can make the extra distinctions essential. Do not rename a theorem about one class as *the smallest possible model*.

The computational-mechanics literature supplies another precise sense of optimality: causal-state partitions of histories are minimal among equally predictive history partitions under the paper's specified input-output process assumptions. That is a valuable alternative, not proof that every minimal causal, physical or decentralized representation is identical. [Barnett and Crutchfield, primary paper, especially the minimality result](https://csc.ucdavis.edu/~cmg/papers/et1.pdf).

## 6. The analyst's state is not a controller's information

**Counterexample 5 — perfect latent representation can imply an impossible policy.** A hidden fair bit `B` is fixed; a controller must choose action `a=B` to succeed, and receives no observation. Keeping both latent states is a perfect physical representation. A controller given the latent state succeeds with probability one; the actual controller cannot exceed one half. Compression did not create the error—silently treating retained analyst state as an observation did.

**Counterexample 6 — finite world, infinitely many exact belief states.** A hidden fixed parameter is `theta=1/3` or `2/3` with equal prior probability; observations are conditionally independent Bernoulli draws. The physical latent process has only two parameter states. After `n` successive ones,

\[
\Pr(\theta=2/3\mid1^n)=\frac{2^n}{1+2^n},\qquad
\Pr(Y_{n+1}=1\mid1^n)=\frac{1+2^n/(1+2^n)}3.
\]

These predictions are distinct for every `n`. Any exact predictor answering the next-observation question from every such history must distinguish infinitely many histories. The smallest latent physical model and the smallest observer-implementable predictive memory are different questions. One continuous posterior coordinate does not imply a finite information budget.

For partial observation, define optimality over an explicitly permitted class: analyst state quotients, sufficient observer histories, finite-state controllers, approximate beliefs, or predictive tests. Do not move between them without a theorem and matching initial information assumptions.

## 7. Decentralization adds an implementation constraint

**Counterexample 7 — pooled observations create a nonexistent remedy.** Let `X,Y` be independent fair bits. Agent 1 sees only `X`; agent 2 sees only `Y`. They cannot communicate, and agent 1 alone must report `X XOR Y`. A central model pooling both signals succeeds surely. Every admissible agent-1 policy has success probability at most one half, even with an independent common randomizer. Preserving the joint global state therefore does not by itself preserve feasible decentralized behavior.

The contract must retain each local information history, not only their union. It must also preserve which randomness is public, private, or correlated, and when recommendations become visible. A policy using unavailable correlated signals is not made executable by having the correct marginal action probabilities. The existing public-recommendation participation result is deliberately narrower than arbitrary decentralized strategic coordination.

Preservation under the same admissible decentralized strategy profiles is possible; solving for optimal decentralized profiles is a separate problem. A single-observer belief-support recursion must not be relabeled a solution of that problem.

## 8. Legitimacy can depend on the process that an output-optimal model erases

**Counterexample 8 — identical agreement, different formation.** Two histories end in the same signed rule and the same subsequent material behavior. In one, signature followed voluntary deliberation; in the other, an undisclosed credible threat secured it. An endpoint contract containing only signature and output merges these histories perfectly. It does not preserve a process requirement about threat-free consent.

If such a requirement matters, include the relevant history or a justified monitor in the preservation contract. This does not make the threat observable when it is not; uncertainty and identification limits remain. The analyst's decision that a process feature matters is a normative and scientific commitment, not something the minimal quotient can discover unaided.

**Counterexample 9 — acceptance improves by destroying refusal.** With losses oriented downward, let continuation loss remain `V=2`. If an institution worsens refusal from `O=1` to `O=3`, refusal changes from preferable to unacceptable and the participation margin `O−V` improves from `−1` to `1`. A model optimizing that margin alone favors manufactured dependence. Protecting meaningful refusal requires explicit consequences and process constraints beyond observed willingness.

Therefore the proposed foundation should distinguish actual behavior, attainability, stated agreement, and justified agreement. Minimality cannot decide whose interests count or legitimate a contracted set of affected parties. The [existing normative construction](../../../../experiments/integrated-correction/general-framework/gap-resolution/NORMATIVE.md) already makes these distinctions and should remain part of the preferred formulation.

## 9. Expanding goals or interventions can invalidate yesterday's optimum

**Counterexample 10 — a previously irrelevant bit acquires causal importance.** Let state `(x,j)` have passive update `x'=x`, `j'=j`; the protected label is `x`. The optimal passive quotient keeps only `x`. Add an intervention `switch` with `x'=j`. States formerly merged now yield different protected outcomes, so `j` is required. Alternatively, adding a protected concern about `j` forces the same refinement without changing dynamics.

For a nested sequence of finite contracts on the same supplied state and kernels, retaining old requirements while adding labels, intervention modes or model constraints can only refine the coarsest faithful partition. This is an exact monotonicity result. It does not say whether adding a new concern is legitimate or how an agent invents its representation.

**Counterexample 11 — all conceivable tests force identity.** If every singleton query `1{S=s}` is a required current-state test, any faithful deterministic summary must be injective: merging distinct `s,t` violates the query for `s`. More generally, every lossy finite-history summary fails some newly chosen singleton history query. Thus demanding exact readiness for *every imaginable future question* makes nontrivial compression impossible.

A universal foundation should be open to contract extension, not promise a single finite compressed state adequate for every future purpose. Recompute or enlarge a representation when justified new distinctions arise. Expanding a descriptive language and retaining an ethical right to challenge its boundary are separate mechanisms that each need resources and actual access.

Intervention scope is likewise substantive in causal-abstraction research. Rubenstein and colleagues formalize consistency through agreement on corresponding interventions; Beckers and Halpern distinguish increasingly demanding abstraction conditions, including whether differences can be hidden by a chosen distribution or restricted intervention set. These are direct precedents for declaring, rather than universalizing, the preservation contract. [Rubenstein et al.](https://arxiv.org/abs/1707.00819), [Beckers and Halpern](https://arxiv.org/abs/1812.03789).

## 10. Optimal representation is not optimal causal science

**Counterexample 12 — observationally identical causal roots.** In model A, `X=U`, `Y=X`, with fair exogenous `U`. In model B, `Y=U`, `X=Y`. Both give precisely the same observed joint law: equal fair bits. Under `do(X=0)`, however, model A makes `Y=0` surely while model B leaves `Y` fair. Perfect passive compression or likelihood fit cannot choose between these causal explanations.

The quotient theorem is conditional on a supplied kernel family. If that family is wrong, a provably optimal quotient can be a provably optimal summary of the wrong model. A successful causal foundation must constrain how mechanisms are identified, how rivals are tested, which interventions discriminate them, and how the model can be revised. The tuple's named factors may help design these experiments even when the semantic quotient has fewer states.

Similarly, a dense minimal transition matrix may obscure sparse local mechanisms; the shortest state list may demand expensive inference; an interpretable factorization may repeat states while making a causal intervention easy to specify. The appropriate scientific comparison reports these tradeoffs instead of treating one coordinate or state count as a universal objective.

## 11. Recommended decision procedure and wording

1. **Keep the old tuple.** Present it as an interpretable coordinate alternative useful for measurement and domain mapping. Do not delete its distinctions or portray abstraction as empirical progress by itself.
2. **Make the process contract explicit.** Name the relevant participants, consequences, process monitors, intervention modes, local information, permissions, time semantics and boundary assumptions. Mark which are empirical hypotheses and which are normative commitments.
3. **Derive adequacy before minimizing.** A candidate must first preserve the contract. The finite strong quotient and structural closure are two proved routes, with different optimality classes.
4. **State the cost being optimized.** Use exact state minimality where its theorem applies. Treat interpretability, mechanism sparsity, privacy, computational tractability and prospective revision as additional criteria, potentially incomparable.
5. **Preserve policy admissibility.** Keep latent analyst variables distinct from every actor's observation history. Include public and private randomness and continuing participation events where relevant.
6. **Test causal rivals.** State which intervention or new observation would distinguish the selected mechanism from a simpler alternative. A minimal representation is not a substitute for that evidence.
7. **Version and reopen the contract.** A new affected party, question or intervention can require refinement. Its legitimate admission must not depend only on showing an anomaly in the old representation, which may have erased the necessary distinction.

Recommended scoped statement:

> The foundational object is a situated causal process whose activities alter the conditions of later activity, selection and revision. A formulation is adequate when it preserves the declared consequences of admissible interventions under the participants' actual information and implementation constraints. Within the specified finite deterministic-quotient class, there is a unique least-distinguishing adequate state representation. Mechanism identification, normative justification and justified expansion of the preservation contract remain separate tasks.

This is a stronger and more defensible optimality claim than naming a fixed tuple “best in science.” It gives a constructive optimum, explicit counterexamples to overreach, and a reason to retain the old tuple as a scientifically useful alternative.

## Review status

The counterexamples and the short quotient argument above were checked directly by elementary reasoning. No new empirical experiment or numerical benchmark is claimed. Primary literature was browsed for the precise comparison classes; this is a targeted audit, not an exhaustive novelty search. Other agents should independently check any new theorem or implementation included in the coordinating synthesis, especially if it replaces strong state quotients with history equivalence, decentralized policies or a looser family of future tests.
