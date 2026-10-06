# Renewal and closure: Phase 2 results

6 October 2026 (UTC). AI-authored, continuing the [roadmap](RENEWAL-CLOSURE-ROADMAP.md) after [Phase 1](RENEWAL-CLOSURE-PHASE1.md). It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md): constraint and flow are articulations, relative to timescale, of one activity. The Lean package is [`lean/conditional/renewal/`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md).

**Transition addressed.** Organization → its own continuation. The question is when a supplied constraint–flow law admits a history that renews its organization forever without importing any. Kinds, support edges, spans, formation demands and arrival rates stay supplied inputs.

## What is proved

The checker passed with 67 new audits across four modules: 12 with empty axiom reports, and the rest depending only on `propext` and `Quot.sound`. There is no `sorry`, no `Classical.choice` and no warning.

### Sufficiency: a standing renewal (`RenewalSufficiency.lean`)

Let `B` be a list of kinds, repeats allowed, formed afresh on every tick. In the steady configuration, each entry of `B` keeps one token of every age within its span.

1. **The steady configuration is a fixed point of one tick** (`steady_fixed`). Aging moves every block of tokens one age older and drops the oldest; the new formations restore the youngest block.
2. **That tick is admissible** (`steady_renews`) when two conditions hold. Each formed kind has a supporter in `B` with span at least two. And `B` is balanced in aggregate: `Σ demand ≤ Σ rate · span` over `B`. Live tokens then open exactly `Σ rate · span`, so the configuration renews forever with no reserve (`steady_endless`).
3. **Two corollaries:**
   - **(B)** A support-closed list of kinds that each bring in at least their demand renews forever (`balanced_closure_renews`).
   - **(E)** A support-closed list `C` that supports a kind `q` with `demand q < rate q · span q` renews forever (`excess_supported_by_closure_renews`), however far the kinds of `C` fall short. The population is `C` plus `formation C` copies of `q`.
4. **The threshold is visible in one kind.** The self-supporting kind with rate 1 and span 3 renews forever at demand 3 (`closed_open_balanced_renews_forever`), and cannot at demand 4 (`closed_open_short_cannot_renew_forever`, Phase 1).

The [preliminary enumerations](../../../../experiments/integrated-correction/general-framework/generative-basis/renewal-closure/preliminary/README.md) showed that a balanced kind started from a single token needs a reserve buffer to get going. The steady configuration needs none. Which configurations can reach it is a question for Phase 2b.

### One model: both necessary conditions on one history (`RenewalLink.lean`)

An `Execution` is a supplied sequence of `channelProcess` ticks whose initial tokens hold no more than their kind's span.

5. **Every token has an origin** (`token_origin`). It came from the initial configuration, or it was formed on a definite earlier tick and its remaining span records how long ago.
6. **Executions are occurrence-support systems** (`executionSupport`). Formations are occurrences. A support edge needs a supporter with span at least two, because the supporter must survive the tick on which it acts.
7. **Live configurations descend from a realized closure** (`live_late_descends_from_realized_closure`). After `(n + 1) · D` ticks, every live configuration descends from a closed walk of such supporters, and each kind on the walk was formed in the preceding `(n + 1) · D` ticks.
8. **Both conditions on the same history** (`endless_renewal_needs_closure_and_adequate_kind`). An execution that stays live forever has a realized closure at every late time and a kind with `demand ≤ rate · span`.

**Timescale separation is derived here, not assumed.** Montévil and Mossio define a constraint as something conserved at the timescale of the process it constrains. In this model, that separation follows from the accounting: a supporter that does not outlast the tick cannot support (item 6). The bound is the minimal one, span at least two.

## What remains: the exact condition

**Target.** Under finitely many kinds, spans between 1 and `D`, and decidable kind equality:

> A law admits an execution that stays live forever **if and only if** there is a nonempty list of kinds `B` such that each kind in `B` has a supporter in `B` with span at least two, and `Σ demand ≤ Σ rate · span` over `B`.

This one condition covers both of the earlier cases. Sufficiency is item 2. Necessity needs one more step: showing that the kind that brings in enough is on, or is supported from, the realized closure. Items 7 and 8 give the closure and the kind separately. The planned argument:

1. **An early excess kind.** Suppose an excess kind is formed late. Its formation descends from a realized cycle through a support walk. The cycle plus that walk is support-closed and contains the excess kind, and (E)'s population over it is balanced in aggregate.
2. **Otherwise, the reserve bound.** If no excess kind is formed during a long stretch, the opening potential (reserve plus what live tokens can still open) cannot rise during it. Each formation of a short kind lowers it by at least one. So among `K + 1` consecutive windows of length `(n + 1) · D + 1`, where `K` is the potential at the start, some window contains no short formation.
3. **The closure at the end of that window.** The live configuration there descends from a cycle whose kinds were all formed inside the window. So every kind on the cycle brings in at least its demand, which is case (B).

Step 3 needs the window theorem to say that the walk's occurrences are no later than the late occurrence. `support_walk` constructs them that way but does not yet state it, so `RenewalClosure` will be strengthened in place.

## Lean notes

- `omega` can bring in `Classical.choice` in two ways. It splits existential hypotheses left in context: `have ⟨…⟩ := h` keeps `h`, while `obtain` clears it. And on a goal that is not arithmetic, it proves `False` by classical contradiction: `False.elim (by omega)` avoids that.
- `Live` is witnessed constructively by searching the token list, and the adequate kind by a decidable search through the listed kinds (`find_or_none`).

These are possibility constraints on renewing the conditions of activity, within the stated scope. They do not say which history occurs, that a system reaches the steady configuration, or that continuation is favorable.
