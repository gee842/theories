# Renewal and closure: Phase 2b, the conditions of correction and whole configurations

6 October 2026 (UTC). AI-authored, continuing the [roadmap](RENEWAL-CLOSURE-ROADMAP.md#phase-2b--renewability-of-whole-configurations-p-c) after [Phase 2](RENEWAL-CLOSURE-PHASE2.md). It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). The Lean package is [`lean/conditional/renewal/`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md).

**Transition addressed.** This phase links the renewal–closure theorem to the [research center](RENEWAL-CLOSURE-ROADMAP.md#11-what-this-serves-the-whole-unfolding): how the whole unfolding generates or damages the conditions of its later realization, renewal and correction. Kinds, edges, spans, demands and rates stay supplied inputs. Nothing here ranks histories ethically.

## Done: whether correction capacity can be renewed

Records, readers and other means of correction are constraints in this model. They are retained, they enable a process, and they wear over a longer span. So whether correction can continue is a question of the same kind as whether organization can continue. The Phase 2 proof answers both, because it was carried out for designated kinds.

**Theorem** (`renewal_keeping_theorem`). Assume finitely many kinds and spans between one and `D`, and let `K` be any decidable set of designated kinds. Some execution keeps a live token of a designated kind at every time **if and only if** some self-renewing population contains a designated kind. Without one, every execution loses its designated kinds by an explicit time computed from the initial configuration (`no_keeping_population_explicit_deadline`).

The renewal–closure theorem is the case where every kind is designated. Its dichotomy, necessity and deadline are now derived from the general versions, so there is one proof.

**The proof's new step** (`kept_kind_descends`). A designated token alive late in an execution was formed recently. Its formation descends from a realized cycle through a walk, and every kind on the cycle and the walk was formed within the preceding `(n + 1) · D` ticks. In the dichotomy, there are two cases.
- If an excess kind is formed late, its cycle and walk are joined with the designated kind's cycle and walk, and the excess kind is repeated enough times.
- Otherwise, the window without short formations contains the designated kind's whole cycle and walk.

**Example: correction lapses while the closure renews** (`lapsingCorrection`). Kind `false` supports itself and exactly brings in its demand (rate 1, span 3, demand 3). It supports a correction kind `true` that falls short (demand 4).
- The closure renews forever (`lapsing_closure_renews_forever`).
- No execution keeps the correction kind forever (`lapsing_correction_cannot_be_kept`). Any population containing it falls short in aggregate (`lapsing_correction_gap`), so by the theorem every execution loses it by an explicit time.

So an organization can go on renewing itself while its capacity for correction cannot be kept. **Renewal of the organization does not carry renewal of correction with it.** Whether correction can be kept depends on how much the population that includes the means of correction brings in. If some kind in a population with the correction kind brings in more than its demand, both can be kept.

## What this does and does not show

- It covers the conditions of correction only as constraints that must stay present: tokens of designated kinds. Whether those tokens actually correct anything, what they record, or how a reader uses them is not modeled.
- Like the renewal theorem, it is about laws: whether some history keeps the designated kinds. It does not say which history occurs.

## Done: renewability of whole configurations

`RenewalConfigurations.lean`. A configuration is the reserve plus every token with its remaining span. It is **renewable** when some execution that stays live forever starts from it.

1. **Viability** (`renewable_iff_step`). A configuration within span is renewable exactly when it is live and some step leads to a renewable configuration.
2. **Renewability is not gained from within** (`renewability_not_generated`). Along any execution, if the start is not renewable, no later configuration is. A configuration with nothing alive forms nothing (`dead_stays_dead`), and a live configuration with a renewable successor is itself renewable. So a history without imported organization can keep the possibility of renewal it starts with, or lose it, but it cannot create it.
3. **Import can create it** (`renewable_of_more`). Adding reserve or tokens from outside keeps a configuration renewable. The model locates the generation of the possibility of renewal at what enters from outside the given history.
4. **What a history generates is the standing renewal** (`seeded_renewable`). Suppose a configuration seeds every kind of a self-renewing population, meaning each has a supporter present that survives the next tick. Suppose also that it holds `D + 1` times the population's formation demand. Then forming the population on each of the next `D + 1` ticks reaches the steady configuration, which renews forever. The history realizes a renewal that the configuration made possible.
5. **No goal projection decides renewability.** One self-supporting kind with rate 1, span 3 and demand 3 shows this twice:
   - Two configurations with the same reserve and the same kinds present differ only in a token's remaining span. One is renewable and the other is not (`renewability_not_function_of_reserve_and_kinds`).
   - Two configurations with the same tokens differ only in reserve, with the same result (`renewability_not_function_of_tokens`).
6. **Damage is a local choice** (`keeping_and_losing_renewal`). From one renewable configuration, forming a token keeps renewability, and forming nothing loses it for good, by item 2. The second successor holds more reserve than the first. An appraisal by held provision would rank the two the wrong way round with respect to renewal.

**What this says about the research center, at this scope.** Within a history that imports no organization, the possibility of renewing the conditions of activity is given at the start. The unfolding then either realizes it as a standing organization or damages it, and damage cannot be undone from within. "Generation" here therefore means realization: building the standing organization the configuration made possible. Creating new possibility needs something to enter from outside. Item 5 shows that whole configurations, including ages and reserve, carry what a goal projection drops. That is the §15 point in constraint–flow form.

**Gaps that remain.**
- Item 4 is sufficient, not necessary. It needs every kind of the population to be seeded at once. A configuration whose seeds only *reach* a population may still be renewable through a periodic, phase-locked regime. For example, a two-kind cycle with span 2 can only alternate, so it never has both kinds fresh on the same tick. Characterizing renewable configurations exactly needs periodic standing renewals, not only fixed points.
- The reserve threshold `(D + 1) · formation` ignores arrivals during the build, so it is coarse.
- The §15 pair from `AcquiredInitiationConstraint` has not yet been mapped into constraint–flow form.

## Premises under Ren's no-assumption rule (6 October 2026)

Ren, 6 October, on another thread's list of remaining assumptions: "we should have no assumption, no axioms", to be "a rule that every agent knows". The coordinator relayed it as: every input a result relies on must be derived in Lean from the process, or proved necessary for the stated claim. These are the premises the renewal package still takes, with what will be done about each. Removing them is the next work, in this order.

| Premise | Where | Status and next step |
|---|---|---|
| Spans bounded by `D` | all main theorems | **To be derived.** With finitely many listed kinds, `D` is the largest span on the list. |
| Rates bounded by `A` | explicit deadlines | **To be derived** the same way. |
| Spans positive | sufficiency, keeping | **To be removed.** A kind with span 0 opens nothing, so it can be dropped from any self-renewing population. For keeping, the designated kind's span being positive becomes part of the condition. |
| Initial tokens within span | `Execution` | **To be removed.** The windows start after the longest initial token instead. |
| Finitely many kinds | all main theorems | **To be proved necessary.** With kinds `ℕ` and a chain `k → k + 1`, a history renews forever with no self-renewing population. |
| Positive formation demand | explicit deadlines only | **To be proved necessary** for a deadline computed from the initial configuration. A free kind that brings in more than its demand can fund a short closure for arbitrarily long from the same start. |
| Decidable equality of kinds | pigeonhole | Used only to find the repeated kind constructively. It holds for every finite enumeration of kinds. It will be stated as part of the finiteness premise. |
| The law itself: kinds, edges, spans, demands, rates | everywhere | **Supplied local-model inputs.** Deriving the constraint–flow form from the generative core is roadmap Phase 4. It is the remaining foundational step for this package. |
| Lean's `propext` and `Quot.sound` | most proofs, through `omega`, `simp` and core list lemmas | The core packages have empty axiom reports. Removing these means rewriting the arithmetic and list steps by hand. It is queued after the items above. |
