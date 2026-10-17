import Becoming.ReducedRuns
import CompositionalTransmission

/-!
# Query traces: the records a course of queries delivers

`CompositionalTransmission` lets one participant learn through another's actual responses: a
query `e` sent in an exchange takes the sender's response to `e` and appends it, with the query,
to the receiver's samples (`send`), and a lesson sends a list of queries in turn (`lesson`).
`CompositionalFormation` states which constructed operations a list of samples fits (`fits`).
This module reads the exchange as a process of the spine: its configurations are exchanges, its
moves are queries, and a query takes an exchange to the exchange after that query is sent
(`queryProcess`, a law of change with moves, `Assurance.ofMap`). A course of this process is
exactly a lesson (`trace_iff`), so the receiver's record at the end of a course is the record the
lesson delivers. The periphery's laws of records are then stated of the courses.

* **The courses are the lessons.** A lesson is the fold of its queries (`lesson_foldl`), and a
  course of the query process from an exchange along a list of queries ends exactly at that
  lesson's exchange (`trace_iff`, through `ReducedRuns.trace_foldl`).
* **The record follows the sender's operation.** Every course along the three basic queries from a
  sender running the operation that ignores the second argument of each join ends with the
  receiver holding that operation's records, which are not the records of the usual
  operation (`course_records_follow_sender`).
* **A delivered record can fit a departing operation.** Every course along the basic queries from
  a sender running the operation for the collapsed code ends with the receiver holding that
  code's trial records (`basic_course_records`); a constructed operation fits that record and still
  departs from the code on the novel expression (`course_record_fits_departing_operation`).
* **A longer course separates them.** Every course along the basic queries followed by the novel
  expression, from the same sender with support for all four responses, ends with the record
  extended by the novel response (`extended_course_records`); that record rejects the departing
  operation and fits the sender's own (`extended_course_separates_operations`).

The periphery's general laws of a single send and of lessons (`delivery_uses_actual_response`,
`absent_response_does_not_fabricate_sample`, `lesson_preserves_joint_support`) have nonempty axiom
reports, so no theorem here uses them.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace QueryTraces

open Generative.CompositionalAcquisition (Expr novel trialRecords eval usual)
open Generative.CompositionalFormation (fits operate programFor collapsed duplicated)
open Generative.CompositionalTransmission
  (send lesson source blank basic extended programRecords selective
   teacher_program_changes_received_evidence)

/-- A query takes an exchange to the exchange after that query is sent. -/
def deliver (x : CompositionalTransmission.Exchange) (e : Expr) :
    CompositionalTransmission.Exchange :=
  send e x

/-- The exchange read as a process: configurations are exchanges, moves are queries. -/
def queryProcess : Process CompositionalTransmission.Exchange Expr := Assurance.ofMap deliver

/-- **A lesson is the fold of its queries.** -/
theorem lesson_foldl :
    ∀ (es : List Expr) (x : CompositionalTransmission.Exchange), lesson es x = es.foldl deliver x
  | [], _ => rfl
  | e :: es, x => lesson_foldl es (send e x)

/-- Every lesson is a course of the query process. -/
theorem lesson_trace :
    ∀ (es : List Expr) (x : CompositionalTransmission.Exchange),
      Trace queryProcess x es (lesson es x)
  | [], x => .nil x
  | e :: es, x => .cons (rfl : send e x = deliver x e) (lesson_trace es (send e x))

/-- **The courses of the query process are exactly the lessons.** A course from an exchange along
a list of queries ends at `y` exactly when `y` is the exchange that lesson leaves. -/
theorem trace_iff {x y : CompositionalTransmission.Exchange} {es : List Expr} :
    Trace queryProcess x es y ↔ y = lesson es x :=
  ⟨fun course => (ReducedRuns.trace_foldl course).trans (lesson_foldl es x).symm,
   fun ends => ends ▸ lesson_trace es x⟩

/-- **The record follows the sender's operation.** Every course of the query process along the
basic queries, from a sender running the operation that ignores the second argument of each join
to a fresh receiver, ends with the receiver holding that operation's records, and those are not
the records of the usual operation. -/
theorem course_records_follow_sender {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source selective 7, blank 25 8⟩ basic y) :
    y.receiver.samples = programRecords selective ∧
      programRecords selective ≠ trialRecords usual :=
  (trace_iff.mp course) ▸ teacher_program_changes_received_evidence

/-- Every course along the basic queries from a sender running the operation for the collapsed
code ends with the receiver holding that code's trial records. -/
theorem basic_course_records {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source (programFor collapsed) 7, blank 25 8⟩ basic y) :
    y.receiver.samples = trialRecords collapsed :=
  (trace_iff.mp course) ▸ (rfl :
    (lesson basic ⟨source (programFor collapsed) 7, blank 25 8⟩).receiver.samples =
      trialRecords collapsed)

/-- **A delivered record can fit a departing operation.** At the end of every course along the
basic queries from a sender running the operation for the collapsed code, the constructed
operation that duplicates the first argument fits the receiver's record, and that operation
departs from the code on the novel expression. -/
theorem course_record_fits_departing_operation {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source (programFor collapsed) 7, blank 25 8⟩ basic y) :
    fits duplicated y.receiver.samples = true ∧
      operate duplicated novel ≠ eval collapsed novel :=
  (basic_course_records course) ▸
    Generative.CompositionalFormation.old_record_can_admit_wrong_constructed_operation

/-- Every course along the basic queries followed by the novel expression, from a sender running
the operation for the collapsed code with support for all four responses, ends with the trial
records extended by the novel response. -/
theorem extended_course_records {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y) :
    y.receiver.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] :=
  (trace_iff.mp course) ▸ (rfl :
    (lesson extended ⟨source (programFor collapsed) 11, blank 25 8⟩).receiver.samples =
      trialRecords collapsed ++ [(novel, eval collapsed novel)])

/-- **A longer course separates the operations.** At the end of every such extended course the
receiver's record rejects the operation that duplicates the first argument and fits the sender's
own operation. -/
theorem extended_course_separates_operations {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y) :
    fits duplicated y.receiver.samples = false ∧
      fits (programFor collapsed) y.receiver.samples = true :=
  (extended_course_records course) ▸
    Generative.CompositionalFormation.asymmetric_composition_exposes_the_new_failure

end QueryTraces

end Becoming
