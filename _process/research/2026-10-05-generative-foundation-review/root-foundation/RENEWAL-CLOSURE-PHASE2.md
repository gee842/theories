# Renewal and closure: Phase 2 results

6 October 2026 (UTC). AI-authored, continuing the [roadmap](RENEWAL-CLOSURE-ROADMAP.md) after [Phase 1](RENEWAL-CLOSURE-PHASE1.md). It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md): constraint and flow are articulations, relative to timescale, of one activity. The Lean package is [`lean/conditional/renewal/`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md).

**Transition addressed.** Organization → its own continuation. The question is when a supplied constraint–flow law admits a history that renews its organization forever without importing any. Kinds, support edges, spans, formation demands and arrival rates stay supplied inputs.

## The renewal–closure theorem

**Theorem** (`renewal_closure_theorem`, `RenewalCharacterization.lean`). Assume finitely many kinds and spans between one and `D`. Some execution stays live forever, with no organization imported after the start, **if and only if** the law has a *self-renewing population*: a nonempty list of kinds `B` such that each kind in `B` has a supporter in `B` with span at least two, and `Σ demand ≤ Σ rate · span` over `B`.

**Deadline** (`no_self_renewing_population_explicit_deadline`). Without such a population, every execution stops being live by `((1 + A·D)^W · P₀ + 2) · W`. Here rates are at most `A`, formation demands are positive, `W = (n + 1)·D + 1`, and `P₀` is the initial reserve plus what the initial tokens can open. The bound is coarse: the exponential term only allows for growth before the decisive window.

The checker passed with 95 new audits across five modules: 14 with empty axiom reports, and the rest depending only on `propext` and `Quot.sound`. There is no `sorry`, no `Classical.choice` and no warning.

### How the target changed

The roadmap's [target](RENEWAL-CLOSURE-ROADMAP.md#32-statement) named two cases: (B) a cycle of kinds that each bring in enough, and (E) an excess kind reachable from a cycle. The proved condition is a single aggregate one. Both cases are instances. The necessity proof constructs one of the two, and sufficiency is proved for each. A statement that the aggregate condition is equivalent to "(B) or (E)" on the law alone would need cycle extraction from a static support-closed list; it is not stated. The deadline uses the roadmap's data: the number of kinds, the longest span, the initial reserve and the initial tokens. Positive formation demand is needed only for that explicit bound, and positive spans only for sufficiency.

### What it says about closure of constraints

1. **Closure plus openness is not sufficient** (Phase 1). The single self-supporting kind with rate 1 and span 3 renews forever at demand 3 and cannot at demand 4.
2. **Timescale separation is derived.** Supporters must outlast the tick on which they act (span at least two). This follows from the accounting, so it is not assumed.
3. **A two-sided closure is necessary but does not carry the provision by itself.** Every live configuration late in a history descends from a realized cycle, whose kinds each depend on and support a member. But the renewing population need only be closed under support. In the `danglingSupport` example, a short self-supporting kind supports a second kind that supports nothing. The second kind brings in more than its demand. It is in no closed set of the support relation, and the closure alone falls short. Yet the law renews forever.

   Read only through support, the closure misses the kind that captures the flow. Read with provision through the shared reserve as a second dependence, that kind is generative for the closure. Montévil and Mossio's "generative" covers both readings. The theorem fixes how much provision the closure must draw back through the constraints it supports.

## Components

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

### The exact condition (`RenewalCharacterization.lean`)

9. **Sufficiency as an execution** (`steadyExecution`, `self_renewing_renews_forever`). The steady configuration's tokens hold no more than their span, so it is an execution, and it stays live.
10. **The dichotomy** (`renewal_dichotomy`). For any execution, either the law has a self-renewing population, or the execution stops being live by `(P + 2) · W`, where `P` is the opening potential at time `W`.
    - *An excess kind formed late.* Its formation descends from a realized cycle through a support walk. The cycle plus the walk is support-closed and contains the excess kind (`cycle_with_tail`). Adding enough repeats of that kind gives a self-renewing population (`excess_population`).
    - *Otherwise.* Over the stretch, the opening potential cannot rise (`stretch_potential`). Each tick with a short formation lowers it by at least one (`stretch_potential_short`). So among `P + 1` windows of length `W`, one has no short formation. If the configuration at its end is live, it descends from a cycle whose kinds were all formed inside that window, so each brings in enough. Both searches are decided, so the proof is constructive.
11. **Necessity, the equivalence and the deadline** (`renews_forever_has_self_renewing_population`, `renewal_closure_theorem`, `no_self_renewing_population_deadline`). With positive demands, one tick multiplies the opening potential by at most `1 + A·D` (`potential_growth`), because formations are met from what is already held or opened. That gives the explicit bound from the initial configuration.
12. **Examples.** The single short kind of Phase 1 has no self-renewing population (`closed_open_short_has_no_self_renewing_population`). The `danglingSupport` law is discussed above.

`RenewalClosure`'s window theorems were strengthened in place to state that the walk's occurrences come no later than the late occurrence. The proofs already built them that way.

## What remains

- **The two named cases on the law alone**, as noted above.
- **Phase 2b: renewability of whole configurations.** The theorem is about laws: whether some history renews forever. The research center asks how a history generates or damages the conditions of its later realization. The next question is which configurations can still reach a standing renewal, and which histories lose that possibility. The dichotomy already gives one half: once no self-renewing population is reachable, the deadline applies.
- **Phase 3:** several required supporters per formation, several flows, and the canonical organization. **Phase 4:** deriving the constraint notion inside the core from `FormationClosure` and the native port.

## Lean notes

- `omega` can bring in `Classical.choice` in two ways. It splits existential hypotheses left in context: `have ⟨…⟩ := h` keeps `h`, while `obtain` clears it. And on a goal that is not arithmetic, it proves `False` by classical contradiction: `False.elim (by omega)` avoids that. An existential hypothesis that is still needed is cleared right after its use.
- `Live` is witnessed constructively by searching the token list, and the adequate kind by a decidable search through the listed kinds (`find_or_none`).

These are possibility constraints on renewing the conditions of activity, within the stated scope. They do not say which history occurs, that a system reaches the steady configuration, or that continuation is favorable.
