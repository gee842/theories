# One witness family? What R37b's witnesses share (20 October 2026)

A check of the Boundary of study §230, which says the queue and ring witnesses are not one parametrized family and that "a family parametrized by its flow and web would be World.of itself". Measured on main 2f14fde8f (Counting, Standing, CensusCounts, CensusBinding).

## What the witnesses share already

Every witness is `World.of carrier flow web` on one of two carriers: queue places (`Nat`, `OpenQueue.Relatum`, `Fin (FiniteQueue.size B)`) or ring seats (`Fin (Ring.size M)`). The census is already stated once per carrier (`Queue.line`/`listed`/`counts`, `Ring.seated`/`census`/`counts`, `openQueue_census`/`counts`), and each witness reuses it. What each witness states for itself is:

| part | lines (both modules) | shape |
|---|---|---|
| world definitions | ≈ 270 | level, flow, requires/need: the premise left out |
| `_decided` instances | ≈ 60 (20 × 3) | `inferInstanceAs` on the carrier's activity |
| `_meets` | ≈ 135 (11 × 12) | 8-case split over `Premise` from the world's premise tuple |
| `_binding` | ≈ 150 (8 × ≈18) | 8-case split joining `_holds` and `_binds` |
| `_binds`, `_dissipative`, `_exceeds`, … | ≈ 1,100 | each premise's instance in that world |
| witness tuples in the `_witnessed` lemmas | 14 tuples | `⟨w, decided, line, meets, listed, counts⟩` |

## Is a family possible?

Partly. "Would be World.of itself" was too quick. A carrier family with activity fixed, `queueWorld flow level requires` with `active := Queue.holds n c`, and a ring family on `Ring.web`, would cover about 12 queue witnesses and 6 ring witnesses. It would state the decision and census once. Four witnesses fall outside it:
- `waitingQueue`: active is `holds (n+1)`.
- `sourcedQueue`: a ground relatum is active.
- `activeRing`: active is `True`.
- `finiteQueue`: lives on `Fin` with `placesBelow`.

What it would save is the `_decided` instances and a word per tuple, about 60 lines. The census is already shared through the carriers. The rest is each premise's counterexample: what the world is and why each premise binds there. A family would only move that rest into arguments.

The eight-case split in `_meets` and `_binding` could take a helper such as `Meets.allBut (free : S q = false) (holds : ∀ p, p ≠ q → p.Holds w)`. The worlds' premise tuples are conjunctions whose statements stay, though, so each world still converts its tuple by cases. That would save under about 100 lines.

## The larger duplicate, which is not in the witnesses

Sixteen corollaries are proved twice: decided in Counting or Standing, counted in CensusCounts or CensusBinding. The proofs are nearly identical, about 770 lines between them (`binding_activity_iff`, `binding_arising_iff`, `binding_joint_iff`, `counting_binds_iff`, `finite_counting_binds_iff`, the enclosed and finite binding iffs, the two change-bound iffs, `enclosed_iff_finite_counting(_under)`, `standing_iff_counting`). The decided and counted laws are both iffs with the same tally side. So each counted corollary is the counted law, then the decided law, then the decided corollary:

```lean
((binding_counting_under_counted S).symm.trans (binding_counting_under S pointwise)).trans
  (binding_activity_iff S)
```

This is checked in Lean against main's oleans. Each result has an empty axiom report, and its statement is the counted theorem's own type (`type_of%`):
- `counted_from_decided.lean`: `counting_binds_iff_counted`, `finite_binding_joint_iff_counted` and `enclosed_binding_activity_iff_counted`.
- `decided_from_counted.lean`: the converse direction for `binding_activity_iff`.

This direction keeps the import order: the counted modules import Counting. It would replace about 370 lines of counted proofs with about 5 each, with no statement or name changed.

Two do not fit plainly:
- `enclosed_iff_finite_counting_under`: its decided form quantifies over pointwise `Q`, and its counted form over every `Q`. It needs a tally-level lemma (the two conditions agree exactly when the selection bounds change and binds counting), with both forms read from it.
- `standing_iff_counting`: 4 lines already.
