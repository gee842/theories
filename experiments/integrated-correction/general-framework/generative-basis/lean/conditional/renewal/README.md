# Renewal and closure: Phases 1 and 2

6 October 2026 (UTC). AI-assisted Lean development for Phases 1 and 2 of the [renewal–closure roadmap](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-ROADMAP.md). The [Phase 1 note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE1.md) states the claim, the conventions and the prior-art check. The [Phase 2 note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE2.md) records sufficiency, the link between the two models, and what remains of the exact condition.

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

## What is not yet proved

- **The exact mixed case.** The target is that endless renewal holds exactly when there is an all-balanced closure, or an excess kind supported from a closure. Sufficiency is proved: (B) and (E). Necessity is proved only in its two separate halves: a closure is needed, and some kind must not fall short. The missing step is to show that the adequate kind sits on, or is supported from, the realized closure.
- Renewability of whole configurations, roadmap Phase 2b.

Kinds, edges, spans, demands and rates are supplied inputs. Nothing here says which history occurs, that a system reaches the steady configuration, or that continuation is favorable.

## Verify

From this directory, with Lean 4.29.1 through elan or on `PATH`, run `python3 check.py`.

The checker:
- requires the inherited `GenerativeCore`, `Depletion` and `SupportNecessity` to match the hashes in their own receipts;
- builds all seven modules fresh in a temporary directory;
- rejects `sorry`, custom axioms and warnings;
- requires every new theorem to be audited.

The [receipt](verification.json) records **67 new audits**: 12 with empty axiom reports, and 55 that depend only on Lean's standard `propext` and `Quot.sound`. This is the same allowance as the conditional package. `Classical.choice` is avoided throughout; the note on `omega` in the Phase 2 note says how.
