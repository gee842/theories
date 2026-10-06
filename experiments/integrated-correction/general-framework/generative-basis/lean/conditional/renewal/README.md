# Renewal and closure: Phase 1

6 October 2026 (UTC). AI-assisted Lean development for Phase 1 of the [renewal–closure roadmap](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-ROADMAP.md). The [study note](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE1.md) states the claim, the conventions and the prior-art check.

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

## What is not yet proved

These are Phase 2 items:
- the exact condition when some kinds fall short and others do not (a balanced closure, or an excess kind reachable from a closure);
- sufficiency;
- the instance connecting `channelProcess` histories to `OccurrenceSupport`, which needs formation times tracked through ticks.

Kinds, edges, spans, demands and rates are supplied inputs. Nothing here says which history occurs, or that continuation is favorable.

## Verify

From this directory, with Lean 4.29.1 through elan or on `PATH`, run `python3 check.py`.

The checker:
- requires the inherited `GenerativeCore`, `Depletion` and `SupportNecessity` to match the hashes in their own receipts;
- builds all five modules fresh in a temporary directory;
- rejects `sorry`, custom axioms and warnings;
- requires every new theorem to be audited.

The [receipt](verification.json) records **32 new audits**: 8 with empty axiom reports, and 24 that depend only on Lean's standard `propext` and `Quot.sound`. This is the same allowance as the conditional package.
