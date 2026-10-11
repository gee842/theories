# Evidence from the branch "Current math core (fork)": what a framing keeps and loses, and what makes a split make sense

Written by the AI (Claude Opus 5.5) on 12 October 2026, in answer to Ren's two messages on this branch
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md)). The first said that describing seems to separate the whole into a projection made of words and to lose something ("wave/particle, 道可道非常道"). The second asked what makes a split make sense, and what makes a pair a pair.

This file is evidence for a conversation. It is not a claim on the [work board](../../../../../BECOMING-WORKBOARD.md), it is not landed, and it is not a result of its own.

- **Written before reading the board.** Sections 1–8 were written in scratch before this branch read the board.
- **Written after reading the board.** Section 9, section 10, the parity theorem in section 1, `liar_each_through_other` and `MakesSense.now_alone_iff` were added afterwards. They are short corollaries for the same answer.
- **Overlap with P69.** The parts that overlap P69 are handed to its owner, "Current math core" [1c3084], under the board's rule 2. The owner decides whether to merge, cite or drop them.
- **No other claims.** The branch claims no other item without Ren's go.

## Check

`Saying.lean` imports nothing. Run it from this directory:

```
~/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean Saying.lean
```

- **Result.** The check exits 0 with no error or warning.
- **Axioms.** There are 56 `#print axioms` lines at the end, one for each theorem in the file, and each reports "does not depend on any axioms".
- **No escapes.** The file contains no `sorry`, `axiom`, `Classical`, `native_decide` or `admit`.
- **Hash.** sha256 `1f97aec46003a0178ff6f45923f79a134eae78b346feb90e0e644bbf63dab3f3`.

## What it builds on

| Earlier result | What this file adds |
|---|---|
| [`RelationalFormation`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalFormation.lean) (8 October): `Rectangular`, `product_rectangular`, `diagonal_not_rectangular` | Describing each part by what it can be gives back the whole exactly when the whole is rectangular (`separation_faithful_iff`). `product_rectangular` shows that a product is rectangular; the new half is the converse, that a rectangular whole is the product of what each part can be. `same_separated` restates `diagonal_not_rectangular` as surplus: the separate description admits `(true, false)`. `whole_not_in_pairs` adds a relation that every pair leaves free and the whole does not. |
| [`RootCoverageBoundary`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/global/formal/CoverageBoundary.lean) (7 October; [note](../../ROOT-MATHEMATICAL-COMPLETION-BOUNDARY.md)): `no_complete_fixedpoint_free`, `external_reading_covers`, `diagonal_extension_strict` | The exact condition: a family of readings indexed by what it reads says every reading exactly when the values have nothing to tell apart (`complete_iff_no_difference`, for decidable values and inhabited carriers). The one-step extension is iterated into an unfolding (`Unfolds`: keep what was said, say next what was missed). Every gap is new (`Unfolds.gap_new`, `Unfolds.gaps_differ`), the unfolding never returns (`Unfolds.never_returns`), and no finite stock holds the gaps (`finite_stock`, a constructive pigeonhole; `Unfolds.unheld`). A witness that such an unfolding exists: `unfolds`, `unfolding_open`. |
| P66 [`Becoming.Mechanism`](../becoming-p64-p68-landing/lean/Becoming/Mechanism.lean) (landing package): `GoAlike`, `carries_law_iff`, `goAlike_const` | A law is not enough for sense. The constant reading carries one (`const_carries`), but it is sufficient only where nothing registered ever differs (`const_sufficient_iff`). A split that loses no registered difference and adds no idle one is unique, and it carries the law (`MakesSense.*`). |

## Against P69's draft

The comparison is with `Becoming.Unfolding` as it stood in the owner's scratch (`/private/tmp/claude-501/-Users-ren-theories/e2a8824b-beaa-4b8e-9f70-f9716e01002c/scratchpad/p69/work/Becoming/Unfolding.lean`, 768 lines, read on 12 October 2026). The owner's draft records `configurations-alike-by-relation` and `process-and-frame-as-readings` were also read. Where the two overlap, the draft is the more general: it covers branching laws, claims and two frames.

| Here | In the draft | Relation |
|---|---|---|
| `SameFuture` with `refl`, `symm`, `trans`, `registered`, `goes` | `Alike` with `refl`, `symm`, `trans`, `realized`, `step` | Same idea. Here it covers one determined law with one registration; there, claims-relative bisimulation. |
| `SameFuture.greatest`: every relation that keeps what is registered and goes on as itself lies within the same-registered-future relation | `Alike` defined as related by some `Bisimulation`; `Alike.trace`, `Alike.tests` | Here the trace form is the definition and the coinduction is the theorem. There the bisimulation is the definition and the trace form is the theorem. For one determined law they describe the same relation; that correspondence is not checked across the two files. |
| `MakesSense` with `sufficient`, `carries`, `unique`, `of_law`, `now_alone_iff` | none found | A projection whose kernel is exactly the canonical likeness. The law follows from it. P69's (3) may want it. |
| `SameAhead` with `symm`, `trans`, `next`; `new_each_moment`, `liar_two_states`, `liar_each_through_other` | `Shown`, `Shown.runs_of_new` | States derived from one registered unfolding, with no configuration type given, in answer to Ren's "change(now) -> future". It bears on (2) and (3). |

The draft keeps likeness as a relation because a quotient needs `Quot.sound`. Here a `MakesSense` projection is assumed given, so nothing needs a quotient.

## The rest, by section

| Section | Theorems | What they say |
|---|---|---|
| 1 Separation | `separated_of_whole`, `separation_faithful_iff`, `same_separated`, `whole_not_in_pairs` | Separation keeps every combination that occurs and loses exactly the relation, which reappears as freedom the parts do not have. Three parts can be related as a whole with every two of them free. |
| 2 A saying within | `gap_unsaid`, `Says.congr`, `complete_iff_no_difference` | Lawvere's diagonal as the gap of a saying within. Completeness from within holds exactly where there is nothing to tell apart. |
| 3 The saying as a becoming | `Unfolds.keeps_on`, `incomplete`, `gap_new`, `gaps_differ`, `never_returns`, `unheld`; `lt_split`, `two_ne_odd`, `finite_stock`; `unfolding_fresh`, `unfolding_zero`, `unfolds`, `unfolding_open` | The saying is never complete and never returns. What it misses is definite, new at each step and held by no finite stock. |
| 4 The liar | `not_not'`, `liar_moves`, `liar_returns` | No still value, a regular movement. This is the revision theory of truth in miniature. |
| 5 An odd cycle | `any_two_hold`, `three_do_not` | Any two of three "differs" hold together, and all three do not. |
| 6 Sense | `SameFuture.*`, `const_carries`, `const_sufficient_iff` | For one determined law: the minimal-automaton (Myhill–Nerode) split, and the deterministic case of causal states (Crutchfield and Young 1989; Shalizi and Crutchfield 2001). |
| 7 The pair | `pair_canonical`, `standing_alone`, `passing_alone`, `orbit_still`, `still_canonical` | Where the standing changes by the passing, the sensible split is the pair. Where nothing passes, the standing alone is that split. |
| 8 Moments | `SameAhead.*`, `new_each_moment`, `liar_zero_two`, `liar_two_states`, `liar_each_through_other` | The simplest rhythm has exactly two states, each defined through the other. |
| 9 Making sense | `MakesSense.sufficient`, `carries`, `unique`, `of_law`, `now_alone_iff`, `pair_makes_sense` | Uniqueness. The law comes out. What is registered now makes sense alone exactly where it fixes its own registered future. |
| 10 Three boxes | `views_agree`, `shown_in_context`, `not_one_view` | Specker's parable (1960): the views agree where they meet, every opening has a definite showing, and no single placement fits them all. Kochen and Specker (1967) proved that quantum mechanics has this shape with more observables. The three boxes are not themselves a quantum model. |

## Bearing on the core

These are readings, offered to Ren.

- **The core's `Frame` is non-contextual by type.** `realized : S → C → Prop` fixes each claim's status by the configuration alone. A contextual world fits a frame only when each claim is indexed by the context in which it is registered (`shown_in_context`). Read without its context, it does not fit (`not_one_view`).
- **The tests for a decomposition.** [`NONDUAL-METHOD`](../../../../../../theories/becoming/chapters/NONDUAL-METHOD.md) (line 77) asks of a decomposition what it preserves, what it omits, why it suits the question and how its terms stay related. This file gives a test for each part:
  - rectangularity, and relations held by no pair;
  - sufficiency relative to what is registered;
  - `MakesSense`, for idle distinctions;
  - gluing, for views.

## Limits

- **Scope.** The scope is a toy: `Bool`, `Nat`, one determined law and one linear time. For branching laws the right notion is bisimulation, as in P69's draft.
- **Physics.** The physics is cited and not proved.
- **Readings.** The readings of 阴阳, 道可道非常道 and Zhuangzi are the AI's. They are given in the conversation and are not part of the checked statements.
