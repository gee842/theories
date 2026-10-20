import Becoming.ExactRecordRuns

/-!
# Exact readings of a run's registered record: the condition of resolution

`KnowledgeCorrespondence.exact_possible_iff_resolves` states that some reading of the evidence is
exact on a domain exactly where the evidence resolves the target. Its proof builds the reading by
choosing a history for each evidence (`KnowledgeCorrespondence.decoder`), so it inherits
`Classical.choice`. Read with the runs of a process as histories, the record a registration
leaves along a run before step `t` as evidence and a two-valued reading of the configuration at
`t` as target (`ExactRecordRuns`):

* **Some reading of the record is exact at step `t` on a domain of runs exactly where runs of the
  domain with one record before `t` have one value at `t`** (`exact_possible_iff`).

This module belongs to the periphery-join ring. No ethical predicate or ranking occurs. It
inherits `propext`, `Classical.choice` and `Quot.sound` from
`KnowledgeCorrespondence.exact_possible_iff_resolves` and adds no axiom of its own.
-/

namespace Becoming

open Generative

universe u v w

namespace ExactRecordRunsInherited

open KnowledgeCorrespondence ExactRecordRuns

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- **Some reading of the record is exact at step `t` on a domain of runs exactly where runs of the
domain with one record before `t` have one value at `t`.** -/
theorem exact_possible_iff (D : Run P → Prop) (reg : S → R) (val : S → Bool) (t : Nat) :
    (∃ answer, ExactOn D (recordBefore reg t) (valueAt val t) answer) ↔
      Resolves D (recordBefore reg t) (valueAt val t) :=
  exact_possible_iff_resolves D (recordBefore reg t) (valueAt val t)

end ExactRecordRunsInherited

end Becoming
