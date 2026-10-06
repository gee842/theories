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

## Next: renewability of whole configurations

The remaining Phase 2b items concern whole configurations rather than laws.
1. Define when a configuration is renewable, meaning some renewing history starts from it.
2. Show that a goal projection cannot capture renewability.
3. Classify which steps keep the possibility of renewal and which lose it.
4. Map the §15 pair from `AcquiredInitiationConstraint` into constraint–flow form, as an interface to prove rather than assume.
