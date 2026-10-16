# Reconstruction and the conditions needed afterward

6 October 2026. AI-authored external analysis of the unchanged material law.
This study derives the actual requirements a future learner would have to acquire;
it does not implement that learner. The [protocol](PROTOCOL.md) fixed the finite
grid and witness comparison before execution, after inspection of the existing
source. [Producer](study.py), [results](results.json),
[independent checker](independent_check.py) and
[verification receipt](independent-check.json) preserve the evidence.

## Exact alternatives under the declared contract

An active resident begins with common fuel F, source E and local occupancy L,
where L is zero or one. The task is to add n A units while preserving total H
and the active resident, with at least n available precursor places. The final
site condition and local occupancy are unrestricted. In the actual witness, n
is fixed by a preceding lost A, not by allowing a controller to create its own
need. This count-maintenance scope is a local operational target, not an ethical
requirement to preserve every current organization.

The least initial common fuel is:

| Initial site | Exact requirement |
|---|---|
| Intact | `max(n − L − E, 0)` |
| Damaged | `min(max(n − L, 0), 1 + max(n − L − E, 0))` |

The damaged alternatives have different effects: use local/common support without
repair, or repair once to make source-backed copying possible. A reconstructed
count need not imply a repaired site. Bulk copying remains available wherever
its actual common-fuel and material prerequisites hold.

The [mathematical account](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CONTINUING-DEPENDENCY-MATH.md)
proves necessity across every admitted finite history and constructs sufficient
routes. The new Lean development formalizes the general necessary bound and the
concrete continuation contrast; general constructive sufficiency is currently
a hand proof, also checked over the finite grid. No new stochastic-control or
universal planning theorem is claimed.

The complete reachability computation uses all sixteen original event kinds,
including formation, bulk copying, wear, damage and leaks. Its 4,800 starting
configurations induce 34,744 distinct graph states and 217,030 edges. The formula
agrees everywhere. All 4,096 feasible cases have checked constructive words,
totaling 11,584 events; the other 704 cases remain infeasible at that scope.
These are finite configurations, not independent empirical observations.

## Equal energy can leave unequal repair capacity

The original 94-event formation history starts without variants or a resident
and reaches free A 38, free H 39, an active resident, an intact site, one local unit,
common fuel 293 and source 216. Its total A count is 39, including the resident.

A declared finite disturbance history of 292 common leaks, one local leak and
one free-A wear reaches free A 37, H 39, an active intact site, local 0, common 1 and
source 216. These are admitted losses in the same history; no balance is reset.

Two routes replace the lost A:

| After reconstruction | Local capture then copy | Bulk copy |
|---|---:|---:|
| Free A / total A | 38 / 39 | 38 / 39 |
| Free H / total H | 39 / 39 | 39 / 39 |
| Resident / site / local store | Active / intact / empty | Active / intact / empty |
| Common fuel | 1 | 0 |
| Incident source | 215 | 216 |
| Total stored energy | 216 | 216 |

Both fulfill the current count-restoration target. Impose the same later damage:
the local route still permits repair, while the bulk route does not. No native
event increases common fuel, so the latter cannot restore repair capacity by
another sequence. Its remaining source cannot cross into that compartment.
The independent checker also explores all 3,120 descendants and 7,642 edges of
that damaged endpoint; none recovers an intact site or positive common fuel.

The complete local branch has 392 events, ends with energy 215 and accounts for
375 expended units of the original 590. The complete bulk branch has 390 events,
ends damaged with energy 216 and accounts for 374 expended units. Their common
comparison point before the imposed damage has equal energy 216. Comparing the
later unequal endpoints would answer a different question.

The richer ancestor also admits bulk reconstruction after wear. With no lost A,
the empty continuation meets the count-restoration target. These controls preserve
the adequate alternative and no-current-need cases. Requiring a response to the
later damage changes the continuation contract; it cannot be inferred solely
from a preferred route's retained capacity.

## Verification and scope

Independent code imports neither this producer nor the native process module.
It reconstructs all event rules, graph profiles, positive witnesses, the four
source definitions composing the 94-event ancestor, and 13 stored history records
containing 1,179 overlapping event occurrences. Source hashes bind nine inputs.
These overlaps are not separate trials. The
[review](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CONTINUING-DEPENDENCY-REVIEW.md)
states the formal and independent-computation scopes.

The positive channel relation is taken from the existing active `process.py` law
with zero repair-loss probability; it matches the sixteen-event Lean relation.
The calculation asks which finite histories are possible. It does not give a
learner authority to choose wear/damage, estimate the probability of the long
disturbance sequence, or prove a scheduler will realize a favorable continuation.
The original finite-stock termination result remains unchanged.

This is a concrete reason an exact continuation model must retain differentiated
support relations. It is not a claim that scalar summaries are always inadequate,
that the original general core lost these fields, or that one route is ethically
better because it preserves this organization. The
[integration](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CONTINUING-DEPENDENCY-INTEGRATION.md)
connects this result to the unfinished acquisition and whole-process account.

To reproduce the new finite checks, run `python3 -B study.py` and
`python3 -B independent_check.py` in this directory. No new packages are needed.

## Subsequent acquired use in a continued material history

The additive [acquisition study](acquisition/README.md) now forms records and a
reader from the original ancestor, retains their occupied material in subsequent
native guards, and uses actual port-bound effects to select a later copy/repair
continuation. Its twenty fixed cases have independent full-state reconstruction.
This supplies a declared contact/reader specialization; it does not retroactively
turn the dependency characterization above into a learner or change its law,
proof scope or preserved results. An informed native rule remains adequate
without acquisition when the relevant action correspondence is already known.


## A retained repair route does not dominate every realization probability

The exploratory [whole-future race](whole_future_race.py) compares the saved local and bulk endpoints after the same free-A wear, under the unchanged default stochastic law. Its explicit target is uninterrupted A restoration with H preserved, before further wear, damage or support leakage. Every native competing channel is retained. This is a two-transient-state first-event calculation, not unrestricted eventual repair or a whole ethical comparison.

Exact fractions give success approximately 0.999880469930 for the common-reserve configuration and 0.999920645158 for the other. The common reserve enables later repair but also competing H copying and common leakage in this episode. The [hash-bound result](whole-future-race.json) matches separately written hand equations and accounts for all outcome probability. This does not establish ethical superiority of either route or invalidate the earlier existential repair result. The [ethical integration](../../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/WHOLE-PROCESS-GROUNDING-ARGUMENT.md#9-renewal-must-include-the-selection-of-actual-continuations) explains why actual selection must join reachability in the whole-future account.

Run `python3 -B whole_future_race.py` to reproduce this separate calculation. The original study, law and result files are unchanged.
