# N6: names that still carry a retired sense (proposal, nothing renamed)

The reading pass changed prose only; every Lean statement is unchanged and `code_of` is identical
to the base. The declarations below are the leftover senses of the naming study (section 8 of
[REGISTRATION-VOCABULARY-STUDY](../../REGISTRATION-VOCABULARY-STUDY.md)) and the others the pass
found. Their docstrings now read in the adopted words, so a name and its docstring can disagree
(for example `order_registers`, whose docstring says the order "makes a difference").

Each rename would be an N5-style migration: a row in a rename table, the Lean edit, a core checker
run, records rebound with history notes, and the chapter's table of retired Lean names extended.
None is needed for any statement to hold. They are offered for Ren to take, change or leave.

Counts: Lean files using the name / records and chapter files mentioning it.

| Current name | What it states (docstring as now read) | Proposed | Other option | Reason | Uses |
|---|---|---|---|---|---|
| `Order.order_registers` (two, in the sharing and the dependence witnesses) | the order of exchanges joined by a relatum or a dependence makes a difference | `order_shows` | `order_makes_difference` | S2 "shows"; matches the record title now "Only the order of change shows" | 1 / 1 |
| `ReferencePlan.revise_registers_failure` | the revision contacts every failed address | `revise_contacts_failure` | `revise_answers_failure` | the rule's output contacts the address (`Contacts.Answers`) | 2 / 1 |
| `ReferencePlan.frozen_blind` | the frozen rule does not read the failure | `frozen_constant` | `frozen_ignores_failure` | follows `Contacts.Blind` below | 1 / 1 |
| `ReferencePlanTraces.revise_registers` | a revise step's method contacts the failed address it answers | `revise_contacts_failed` | — | as above | 2 / 1 |
| `ReferencePlanTraces.frozen_leaves_unregistered` | at every retained method some failure is left unanswered by every frozen step | `frozen_leaves_unanswered` | — | the docstring's own word | 1 / 0 |
| `ReferencePlanTraces.first_round_registers`, `second_round_registers` | the round gains the choice at a contact through the installed contacts | `first_round_gains`, `second_round_gains` | — | the docstring's own word | 1 / 0 |
| `Contacts.Blind`, `blind_answers_iff`, `blind_misses`, `finite_blind_answers` | a rule whose output does not depend on the failure (`ρ D r = ρ D none`) | `Contacts.ConstantInFailure`, `constant_answers_iff`, `constant_misses`, `finite_constant_answers` | `Contacts.IgnoresFailure` | the definition is exactly constancy in the failure argument; "blind" is a sense metaphor | 2 / 1 |
| `namespace Registration` in `Becoming.Revision` (`keeps_iff`, `History`, `Keeps`, `retained_gains`, `through_history_later`) | a lumping at each configuration and the history of lumpings drawn | `namespace Lumping` | `namespace Distinctions` | the module header now reads "Selection when the lumping itself changes" | 5 / 4 |
| `TypicalRuns.record`, `ofRecord`, `record_ofRecord`, `Records`, `courses_records`, `records_*`, `histories_records` | the prefix of `n` steps of a run; listing every such prefix once | `runPrefix`, `ofPrefix`, `runPrefix_ofPrefix`, `Prefixes`, `courses_prefixes`, `prefixes_*`, `histories_prefixes` | `Words` for `Records` | L-prefix; `prefix` alone is a Lean keyword | 9 / 13 (mostly `Records` in prose of other senses) |
| `ExactRecordRuns.recordBefore` (and the module name) | the prefix before step `t` of a run's course through a map | `prefixBefore` | module `ExactPrefixRuns` | L-prefix; a module rename moves a file and its receipts, so it is listed separately | 2 / 0 |
| `Branching.carries_unregistered` | carrying a law needs equality on the description, or claims that tell it apart | `carries_untold` | `carries_needs_claims` | S6 "tells apart" | 2 / 3 |
| `Branching.refutes_registered` | excluding a model needs the outcome claimed | `excludes_claimed` | `excludes_needs_claims` | S5 "excludes", as the docstring reads | 1 / 1 |
| `Confound.varied_refutes` | varying the move against the hidden bit excludes the projection | `Confound.varied_excludes` | — | S5, as the docstring and records now read | 2 / 4 |
| `Likeness.level_registers` | the claims reading the level of the condition tell it apart | `level_tells_apart` | — | S6 | 1 / 1 |
| `SelectionRuns.selects_through_coupling` | a selection through the course is through the lumping the map makes along the run | `selects_through_lumping` | — | the statement is about a map's lumping, not a web's coupling | 1 / 1 |
| `ExchangeLaw.ReadsFinitely.through_of_observed` | a law reading finitely many conditions reads through every coupling by level that holds what it is sensitive to | `through_of_byLevel` | `through_of_coupledByLevel` | S2: "observes" is coupling by level | 2 / 2 |
| `Identification.bounded_hypothesis` | on a history with at most N states some lasso candidate within N accords | `bounded_candidate` | — | L-elim: hypotheses are candidates | 1 / 1 |
| `section Registered` in `Becoming.Unfolding` | laws read through a map | `section ThroughMap` | — | not a declaration; the section name is code, so it waits for the same migration | 1 / 0 |

Kept on reading, with no proposal:

- `Learning.answerTo`, `answerStep`: the value set against an extrapolation's proposal; "answer" is a
  structural word here (the diagonal course answers the extrapolation at every step), not the
  register sense.
- `Parting.candidates`: already the adopted word (L-elim). Its argument is still named `record`; a
  local variable, renamed with the module if `TypicalRuns` is.
- Record ids that hold the old words (`subthreshold-registration`, `contextual-registration`,
  `registration-within-what-it-registers`, `runaway-distance-unregistered`,
  `selection-under-registration-revision`, `sensitivity-is-the-least-registration`,
  `only-the-order-of-change-registers`, `learning-by-refutation`, `testing-within-registration`,
  `learnable-through-registration`, `selection-through-registration`,
  `selection-through-a-model-of-the-options`, `formed-copying-registration`): ids are links, kept by
  rule; the titles now read in the adopted words.
- The periphery's names (`CopyingRegistration`, `registered_operation_refines`,
  `PluralRecords`, `MachineInstances` learners): outside the core and the task.
