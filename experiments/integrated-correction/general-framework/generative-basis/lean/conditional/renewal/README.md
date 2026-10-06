# Renewal and closure: Phases 1 and 2

6 October 2026 (UTC). AI-assisted Lean development for Phases 1 and 2 of the [renewal–closure roadmap](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-ROADMAP.md). The [Phase 1 note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE1.md) states the claim, the conventions and the prior-art check. The [Phase 2 note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE2.md) records sufficiency, the link between the two models, and the exact condition.

## The main result

**Renewal–closure theorem** (`renewal_closure_theorem`, in `RenewalCharacterization.lean`). Assume finitely many kinds and spans between one and `D`. Then some execution stays live forever, with no organization imported after the start, **if and only if** the law has a *self-renewing population*. That is a nonempty list of kinds such that:
- each kind in it has a supporter in it whose span is at least two;
- its tokens open over their spans at least what forming them demands: `Σ demand ≤ Σ rate · span`.

Without such a population, every execution stops being live by an explicit time (`no_self_renewing_population_explicit_deadline`). With rates at most `A` and positive formation demands, that time is `((1 + A·D)^W · P₀ + 2) · W`. Here `W = (n + 1)·D + 1`, and `P₀` is the initial reserve plus what the initial tokens can open.

**Keeping designated kinds** (`renewal_keeping_theorem`). The proof is carried out for any decidable set of designated kinds. Some execution keeps a live token of a designated kind at every time exactly when some self-renewing population contains a designated kind. The renewal theorem is the case where every kind is designated. When the means of correction (records, readers) are designated, this decides whether correction capacity can be renewed along with the rest. In `lapsingCorrection`, a closure that exactly renews itself supports a correction kind that falls short. The closure renews forever, but no execution keeps the correction kind (`lapsing_correction_cannot_be_kept`).

## What is proved

**`RenewalClosure.lean`: late activity descends from a realized closure.**

`OccurrenceSupport` is the shared interface. Each organized kind that occurs at a positive time needs an earlier occurrence of a supporting kind that can still support it (`reach`). No organization arrives from outside after time zero. Raw flows are not represented and may stay external.

- `late_occurrence_descends_from_realized_closure`: suppose every kind is listed and reach is at most `D`. Then an occurrence after `n·D` descends through support edges from a nonempty closed walk of kinds. Every kind on that walk actually occurred in the last `n·D` time units. The proof is a backward support chain plus a pigeonhole argument written here, so it avoids library lemmas with classical dependencies.
- `closed_walk_dependence_closed`: the kinds of such a walk form a closed set in Montévil and Mossio's sense. Each depends on a member and supports a member. For a single self-supporting kind, the paper's "other constraint" holds between distinct occurrences.
- `acyclic_support_deadline`, `episode_acyclic_deadline`: without a nonempty type cycle, nothing occurs after `n·D`. For `SupportNecessity`'s episode systems, nothing is alive after `(n+1)·L`. **No rank certificate is supplied.** This closes the gap `SupportNecessity` names ("No finite-graph cycle-extraction theorem is claimed here").
- `episodeSupport`: episode systems are instances of the interface.

**`RenewalAccounting.lean`: constraints that bring in less than their formation demands.**

`channelProcess` is a `Process` on whole configurations: the reserve plus every token's remaining span. On each tick:
- spans fall by one, and tokens on their last tick leave;
- live tokens open arrival at their kind's rate;
- forming a token makes a demand on the reserve (the U1 law);
- each formed token needs a support token that survives the tick.

The main results:
- `short_renewal_depletes`: if `rate k * span k < demand k` for every kind, a combined potential strictly decreases on every tick on which some token is alive. The potential is remaining life plus `D` times (reserve plus what live tokens can still open).
- `short_renewal_deadline`, `short_kinds_cannot_renew_forever`: these follow by the core `Depletion` theorems. Renewal lasts at most the starting potential in ticks, and no infinite renewing execution exists. **This holds whatever the support edges are.**
- `closedOpenShort_ticks`, `closed_open_short_cannot_renew_forever`: a single self-supporting kind with rate 1, span 3 and demand 4. It is closed and open to unbounded flow, and it really does renew for a tick, yet it cannot renew forever. **Closure plus openness is not sufficient.**

Taken together, the two files give two independent necessary conditions for endless renewal without imported organization:
- a realized closure (from finite reach and finitely many kinds);
- some kind that brings in at least what its formation demands.

**`RenewalSufficiency.lean`: closed populations that bring in enough renew forever.**

Take a list `B` of kinds, repeats allowed, formed afresh on every tick. In the steady configuration `steady law B N`, each entry of `B` keeps one token of every age within its kind's span.
- `steady_fixed`: one tick ages every token, drops those on their last tick and adds the new formations. It returns exactly the same configuration.
- `steady_renews`, `steady_endless`: that tick is admissible and live when every formed kind has a supporter in `B` with span at least two, and `Σ demand ≤ Σ rate · span` over `B`. The steady configuration then renews forever, with any reserve, including none.
- `balanced_closure_renews` **(B)**: a support-closed list of kinds that each bring in at least their formation demand renews forever.
- `excess_supported_by_closure_renews` **(E)**: a support-closed list `C` that also supports a kind `q` with `demand q < rate q · span q` renews forever. Here `q` is formed `formation law C` times per tick next to `C`. The kinds of `C` may all fall short.
- `closed_open_balanced_renews_forever`: the self-supporting kind with rate 1 and span 3 renews forever at demand 3. At demand 4 it cannot (`closed_open_short_cannot_renew_forever`). The exact threshold is visible in one kind.

**`RenewalLink.lean`: both necessary conditions hold on one history.**

An `Execution` is a supplied sequence of `channelProcess` ticks. Its only extra premise is that initial tokens hold no more than their kind's span.
- `token_origin`: every token either came from the initial configuration or was formed on a definite earlier tick. Its remaining span records how long ago that was.
- `executionSupport`: formations are occurrences in the sense of `OccurrenceSupport`. A support edge needs span at least two, because the supporter must survive the tick on which it acts. **The timescale separation that Montévil and Mossio put into the definition of a constraint comes out here as a consequence of the accounting.**
- `live_late_descends_from_realized_closure`: in any execution, a live configuration after `(n + 1) · D` descends from a closed walk of such supporters. Each kind on that walk was formed within the preceding `(n + 1) · D` ticks.
- `endless_renewal_needs_closure_and_adequate_kind`: an execution that stays live forever has both a realized closure at every late time and a kind with `demand ≤ rate · span`.

**`RenewalCharacterization.lean`: the exact condition.**

- `self_renewing_renews_forever`: sufficiency, through the steady configuration as an execution (`steadyExecution`).
- `renewal_dichotomy_keeping`: for any execution and designated kinds, either some self-renewing population contains a designated kind, or the execution holds no designated live token at some time by `(P + 2) · W`, where `P` is the opening potential at time `W`. `renewal_dichotomy` is the case where every kind is designated. The proof has two cases.
  - Suppose a kind that brings in more than its demand is formed after time `W`. Its formation descends from a realized cycle, and so does a designated kind kept at time `W` (`kept_kind_descends`). The two cycles with their walks, plus enough repeats of the excess kind, form a self-renewing population (`cycle_with_tail`, `excess_population`).
  - Otherwise, the opening potential cannot rise, and each formation of a short kind lowers it (`stretch_potential`, `stretch_potential_short`). So some window of length `W` has no short formation. A designated kind kept at its end descends from a cycle and walk of kinds all formed in that window, so they all bring in enough.
- `renews_forever_has_self_renewing_population`, `renewal_closure_theorem`, `renewal_keeping_theorem`: necessity, and the two equivalences.
- `potential_growth`, `potential_bound`, `no_keeping_population_explicit_deadline`, `no_self_renewing_population_explicit_deadline`: the deadlines from the initial configuration alone.
- `closed_open_short_has_no_self_renewing_population`: the single short kind of Phase 1 is decided by the law.
- `dangling_support_renews_forever`, `dangling_kind_outside_every_closure`, `dangling_closure_falls_short`. A short self-supporting kind supports a second kind that supports nothing but brings in more than its demand. The second kind is in no closed set of the support relation, and the closure alone falls short, yet the law renews forever. **Renewal still needs a realized two-sided closure (`live_late_descends_from_realized_closure`). But the population that renews need only be closed under support. The kind that captures the flow can sit outside every two-sided closure of the support relation, and it is generative only through the provision it opens.**

**`RenewalConfigurations.lean`: renewability of whole configurations.**

A configuration (reserve plus every token with its remaining span) is `Renewable` when some execution that stays live forever starts from it.
- `renewable_iff_step`: a configuration within span is renewable exactly when it is live and some step leads to a renewable configuration.
- `renewability_not_generated`: along any execution, if the start is not renewable, no later configuration is. A history can keep or lose the possibility of renewal, but cannot create it from within.
- `renewable_of_more`: adding reserve or tokens from outside keeps renewability. Possibility can be created only by what enters from outside.
- `seeded_renewable`: a configuration that seeds every kind of a self-renewing population, with `D + 1` times its formation demand in reserve, reaches the steady configuration within `D + 1` ticks.
- `renewability_not_function_of_reserve_and_kinds`, `renewability_not_function_of_tokens`: no goal projection decides renewability. Configurations that differ only in a token's age, or only in reserve, differ in renewability.
- `keeping_and_losing_renewal`: from one renewable configuration, forming a token keeps renewability, while forming nothing loses it for good. The second successor holds more reserve.

`RenewalClosure`'s window theorems now also state that the walk's occurrences come no later than the late occurrence (`s ≤ t`), and they cover the walk from the cycle as well as the cycle. The proofs build them that way, and the exact conditions need both.

## What is not yet proved

- That the aggregate condition is equivalent to the roadmap's two named cases, a cycle of kinds that each bring in enough or an excess kind supported from a cycle, as a statement about the law alone. The necessity proof constructs one of the two, and sufficiency is proved for each, but the static cycle extraction is not stated.
- An exact characterization of renewable configurations. `seeded_renewable` is sufficient but not necessary: phase-locked cycles can renew without ever having all kinds fresh at once.
- **The premises listed in the [Phase 2b note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE2B.md#premises-under-rens-no-assumption-rule-6-october-2026).** Under Ren's no-assumption rule, each is to be derived (bounded spans and rates), removed (positive spans, initial tokens within span), or proved necessary (finitely many kinds, positive demand for the explicit deadline). The law itself stays a supplied input until Phase 4. Lean's `propext` and `Quot.sound` are to be removed after that.
- The generalizations of Phase 3 (several required supporters, several flows) and the derivation of constraints inside the core (Phase 4).

Kinds, edges, spans, demands and rates are supplied inputs. Nothing here says which history occurs, that a system reaches the steady configuration, or that continuation is favorable.

## Verify

From this directory, with Lean 4.29.1 through elan or on `PATH`, run `python3 check.py`.

The checker:
- requires the inherited `GenerativeCore`, `Depletion` and `SupportNecessity` to match the hashes in their own receipts;
- builds all nine modules fresh in a temporary directory;
- rejects `sorry`, custom axioms and warnings;
- requires every new theorem to be audited.

The [receipt](verification.json) records **135 new audits**: 19 with empty axiom reports, and 116 that depend only on Lean's standard `propext` and `Quot.sound`. This is the same allowance as the conditional package. `Classical.choice` is avoided throughout; the note on `omega` in the Phase 2 note says how.
