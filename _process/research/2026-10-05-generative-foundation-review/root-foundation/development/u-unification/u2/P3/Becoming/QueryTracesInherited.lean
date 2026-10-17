import Becoming.Branching
import Becoming.QueryTraces
import Becoming.FormationTracesInherited

/-!
# Query traces and succession runs (periphery-join ring)

`Becoming.QueryTraces` reads the exchange of `CompositionalTransmission` as a process whose moves
are queries (`queryProcess`), with its courses exactly the lessons (`QueryTraces.trace_iff`), and
`Becoming.FormationTracesInherited` reads the formation apparatus's moves as a process
(`formationProcess`). The periphery's learner after a lesson (`learn`) is what the formation move
`develop` makes of the receiver where a course of queries ends. A successor (`successor`) is the
learner a fresh participant becomes after the basic lesson from a teacher, so succession is a
determined law (`Law.process successor`), and the periphery's cohorts are its runs: every run from
a starting configuration passes through the cohorts from it (`run_cohort`, through
`Branching.law_run_state`). This module states the periphery's laws of transmission of these
steps, courses and runs.

* **One query.** A query step from a ready receiver with support appends the sender's actual
  response and leaves the sender the support its response leaves (`step_delivers`); where the sender
  gives no response, the step adds no sample (`step_adds_nothing_without_response`).
* **A conserved amount.** Along every course of queries the sender's and receiver's support and
  spent amounts together are unchanged (`course_joint_support`).
* **The record's composite response decides the interpretation.** A course that omits the
  composite query gives no interpretation (`course_without_composite`), and a course from a sender
  whose composite response is reversed gives the switched code (`course_reversed_composite`).
* **Learning after a course.** Developing what a course delivers reconstructs the operation that
  ignores each join's second argument whatever the support (`learned_selective_funded`), loses a
  distinction the usual task makes (`learned_selective_loses_distinction`), forms different
  operations from the same teacher after different courses (`learned_depends_on_course`), and is
  blocked where the receiver's support cannot cover the extended course
  (`learned_blocked_short`).
* **Succession runs.** A succession step keeps an installed program whose route is generated, whose
  primitives differ and whose support is at least seven (`succession_step_keeps`). Every run of
  succession from a teacher running a code's program keeps, at every date, a program evaluating
  every expression as the code does (`succession_keeps_correspondence`); from the selective teacher
  every date keeps the lost distinction (`succession_keeps_lost_distinction`); from the collapsed
  code's teacher every later date holds the duplicating program, which fails the novel expression
  (`succession_stabilizes_change`). From the formed teacher the run holds the usual program at
  dates zero, one and two (`formed_succession_teaches`, `formed_succession_second`); from the
  teacher with an execution-only budget the basic course delivers only the two primitive records
  and the successor is blocked (`budget_succession_blocked`). A peer at date one of the run from
  the collapsed code's teacher holds the duplicating program; one further demonstration and
  reconsideration repair it where the demonstrator runs the code's program (`peer_repair`) and
  keep it where the demonstrator runs the duplicating program (`peer_keeps_error`).

This module belongs to the periphery-join ring. It adds no axiom of its own and uses no `simp`,
`omega` or `decide`. Its declarations inherit `propext` from the definitions of `develop`,
`reconsider`, `learn`, `successor`, `cohort`, `limitedCohort` and `interpretationFromRecords`
(through `readEvidence`) and from `delivery_uses_actual_response`,
`absent_response_does_not_fabricate_sample` and the periphery's `decide` witnesses
(`missing_composite_record_blocks_interpretation`,
`corrupted_composite_record_changes_interpretation`,
`extra_funding_does_not_fix_transmitted_content`,
`faithfully_reconstructed_operation_can_lose_a_task_distinction`,
`same_teacher_different_encounters_change_reconstruction`,
`received_disagreement_is_not_automatically_repaired`,
`formed_teacher_can_teach_after_supported_preparation`,
`successful_reconstruction_can_teach_a_later_participant`,
`execution_only_budget_can_interrupt_teaching`,
`peer_demonstration_can_repair_without_new_generation`,
`erroneous_peer_demonstration_can_preserve_error`), and `Quot.sound` as well from
`lesson_preserves_joint_support`, `reconstructed_successor_retains_operation`,
`every_cohort_retains_all_expression_correspondence`,
`task_distinction_loss_can_recur_in_every_cohort` and
`stabilized_change_can_fail_the_original_task`.
No ethical predicate or ranking occurs.
-/

namespace Becoming

open Generative

namespace QueryTracesInherited

open Generative.CompositionalAcquisition
  (Code Expr novel usual switched trialRecords eval p0 p1 orderProbe interpretationFromRecords)
open Generative.CompositionalFormation
  (Program respond operate programFor generatedRoutes prepared collapsed duplicated further)
open Generative.CompositionalTransmission
  (send lesson source blank basic extended selective joint00 successor cohort limitedCohort)
open QueryTraces (queryProcess)
open FormationTracesInherited (formationProcess)

/-! ## One query and the conserved amount -/

/-- **A query step delivers the sender's actual response.** From a ready receiver with support,
the step appends the query with the sender's response to the receiver's samples, and the sender
keeps the support its response leaves. -/
theorem step_delivers {x y : CompositionalTransmission.Exchange} {e : Expr}
    (step : queryProcess.step x e y) (ready : x.receiver.blocked = false)
    (support : 1 ≤ x.receiver.support) {out : List Bool} {remaining : Nat}
    (actual : respond x.sender e = some (out, remaining)) :
    y.receiver.samples = x.receiver.samples ++ [(e, out)] ∧ y.sender.support = remaining :=
  step ▸ CompositionalTransmission.delivery_uses_actual_response e x ready support out remaining
    actual

/-- **Without a response, a query step adds no sample.** -/
theorem step_adds_nothing_without_response {x y : CompositionalTransmission.Exchange} {e : Expr}
    (step : queryProcess.step x e y) (absent : respond x.sender e = none) :
    y.receiver.samples = x.receiver.samples :=
  step ▸ CompositionalTransmission.absent_response_does_not_fabricate_sample e x absent

/-- **Along every course of queries the joint support and spent amounts are unchanged.** -/
theorem course_joint_support {x y : CompositionalTransmission.Exchange} {es : List Expr}
    (course : Trace queryProcess x es y) :
    y.sender.support + y.sender.spent + y.receiver.support + y.receiver.spent =
      x.sender.support + x.sender.spent + x.receiver.support + x.receiver.spent :=
  (QueryTraces.trace_iff.mp course) ▸
    CompositionalTransmission.lesson_preserves_joint_support es x

/-! ## The composite response and the interpretation -/

/-- **A course that omits the composite query gives no interpretation.** -/
theorem course_without_composite {y : CompositionalTransmission.Exchange}
    (course : Trace queryProcess ⟨source (programFor usual) 4, blank 25 8⟩ [p0, p1] y) :
    interpretationFromRecords y.receiver.samples = none :=
  (QueryTraces.trace_iff.mp course) ▸
    CompositionalAcquisition.missing_composite_record_blocks_interpretation

/-- **A course from a sender whose composite response is reversed gives the switched code.** -/
theorem course_reversed_composite {y : CompositionalTransmission.Exchange}
    (course :
      Trace queryProcess ⟨source ⟨false, true, [true, false]⟩ 7, blank 25 8⟩ basic y) :
    interpretationFromRecords y.receiver.samples = some switched :=
  (QueryTraces.trace_iff.mp course) ▸
    CompositionalAcquisition.corrupted_composite_record_changes_interpretation

/-! ## Learning after a course -/

section Learning

variable {y y' : CompositionalTransmission.Exchange} {z z' : CompositionalFormation.Frame}

/-- **More support does not change what is reconstructed.** Developing what the basic course
from a well-supplied selective teacher delivers installs the selective program. -/
theorem learned_selective_funded
    (course : Trace queryProcess ⟨source selective 70, blank 100 80⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z) :
    z.installed = some selective :=
  (FormationTracesInherited.trace_iff.mp formed) ▸ (QueryTraces.trace_iff.mp course) ▸
    CompositionalTransmission.extra_funding_does_not_fix_transmitted_content

/-- **A faithful reconstruction can lose a distinction of the task.** Developing what the basic
course from the selective teacher delivers installs the selective program, which gives one value
to two expressions the usual code tells apart. -/
theorem learned_selective_loses_distinction
    (course : Trace queryProcess ⟨source selective 7, blank 25 8⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z) :
    z.installed = some selective ∧ operate selective joint00 = operate selective orderProbe ∧
      eval usual joint00 ≠ eval usual orderProbe :=
  (FormationTracesInherited.trace_iff.mp formed) ▸ (QueryTraces.trace_iff.mp course) ▸
    CompositionalTransmission.faithfully_reconstructed_operation_can_lose_a_task_distinction

/-- **The same teacher, different courses, different reconstructions.** From the collapsed
code's teacher, developing after the basic course installs the duplicating program, and after the
extended course installs the code's own program. -/
theorem learned_depends_on_course
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ basic y)
    (formed : Trace formationProcess y.receiver [.develop] z)
    (course' : Trace queryProcess ⟨source (programFor collapsed) 11, blank 25 8⟩ extended y')
    (formed' : Trace formationProcess y'.receiver [.develop] z') :
    z.installed = some duplicated ∧ z'.installed = some (programFor collapsed) :=
  (FormationTracesInherited.trace_iff.mp formed) ▸ (QueryTraces.trace_iff.mp course) ▸
    (FormationTracesInherited.trace_iff.mp formed') ▸ (QueryTraces.trace_iff.mp course') ▸
    CompositionalTransmission.same_teacher_different_encounters_change_reconstruction

/-- **A received disagreement is not repaired without support.** With five units of receiver
support, developing after the extended course installs nothing. -/
theorem learned_blocked_short
    (course : Trace queryProcess ⟨source (programFor collapsed) 11, blank 5 8⟩ extended y)
    (formed : Trace formationProcess y.receiver [.develop] z) :
    z.installed = none :=
  (FormationTracesInherited.trace_iff.mp formed) ▸ (QueryTraces.trace_iff.mp course) ▸
    CompositionalTransmission.received_disagreement_is_not_automatically_repaired

end Learning

/-! ## Succession runs -/

section Succession

/-- **A succession step keeps an installed program** whose route is generated, whose primitives
differ and whose support is at least seven; the successor again has at least seven units. -/
theorem succession_step_keeps (r : Run (Law.process successor)) {p : Program} (n : Nat)
    (installed : (r.state n).installed = some p)
    (routes : p.route ∈ generatedRoutes 2) (distinct : p.first ≠ p.second)
    (enough : 7 ≤ (r.state n).support) :
    (r.state (n + 1)).installed = some p ∧ 7 ≤ (r.state (n + 1)).support :=
  (r.step n : r.state (n + 1) = successor (r.state n)) ▸
    CompositionalTransmission.reconstructed_successor_retains_operation (r.state n) p installed
      routes distinct enough

/-- The cohorts from a teacher are the orbit of succession from it. -/
theorem orbit_cohort (p : Program) : ∀ n, Law.orbit successor (source p 7) n = cohort p n
  | 0 => rfl
  | n + 1 => congrArg successor (orbit_cohort p n)

/-- The limited cohorts are the orbit of succession from the collapsed code's teacher. -/
theorem orbit_limited :
    ∀ n, Law.orbit successor (source (programFor collapsed) 7) n = limitedCohort n
  | 0 => rfl
  | n + 1 => congrArg successor (orbit_limited n)

/-- **Every run of succession from a teacher passes through the cohorts from it.** -/
theorem run_cohort {p : Program} {r : Run (Law.process successor)} (start : r.state 0 = source p 7)
    (n : Nat) : r.state n = cohort p n :=
  (Branching.law_run_state r n).trans
    ((congrArg (fun s => Law.orbit successor s n) start).trans (orbit_cohort p n))

/-- **Succession keeps the correspondence.** Every run of succession from a teacher running a
code's program, where the code's primitives differ, holds at every date a program evaluating every
expression as the code does. -/
theorem succession_keeps_correspondence {c : Code} {r : Run (Law.process successor)}
    (start : r.state 0 = source (programFor c) 7) (distinct : c.first ≠ c.second) (n : Nat)
    (e : Expr) : ∃ p, (r.state n).installed = some p ∧ operate p e = eval c e :=
  (run_cohort start n).symm ▸
    CompositionalTransmission.every_cohort_retains_all_expression_correspondence c distinct n e

/-- **Succession keeps a lost distinction.** Every run of succession from the selective teacher
holds the selective program at every date, and that program gives one value to two expressions the
usual code tells apart. -/
theorem succession_keeps_lost_distinction {r : Run (Law.process successor)}
    (start : r.state 0 = source selective 7) (n : Nat) :
    (r.state n).installed = some selective ∧
      operate selective joint00 = operate selective orderProbe ∧
      eval usual joint00 ≠ eval usual orderProbe :=
  (run_cohort start n).symm ▸
    CompositionalTransmission.task_distinction_loss_can_recur_in_every_cohort n

/-- **Succession stabilizes a change.** Every run of succession from the collapsed code's teacher
holds the duplicating program at every date after the first, and that program fails the novel
expression. -/
theorem succession_stabilizes_change {r : Run (Law.process successor)}
    (start : r.state 0 = source (programFor collapsed) 7) (n : Nat) :
    (r.state (n + 1)).installed = some duplicated ∧
      operate duplicated novel ≠ eval collapsed novel :=
  ((Branching.law_run_state r (n + 1)).trans
    ((congrArg (fun s => Law.orbit successor s (n + 1)) start).trans
      (orbit_limited (n + 1)))).symm ▸
    CompositionalTransmission.stabilized_change_can_fail_the_original_task n

/-- **The formed teacher teaches.** Where the run of succession starts where the formation course
`[develop]` from the prepared configuration ends, the teacher and its successor both hold the
usual program. -/
theorem formed_succession_teaches {r : Run (Law.process successor)}
    (start : Trace formationProcess (prepared 25 4) [.develop] (r.state 0)) :
    (r.state 0).installed = some (programFor usual) ∧
      (r.state 1).installed = some (programFor usual) := by
  have h0 := FormationTracesInherited.trace_iff.mp start
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  rw [h1, h0]
  exact CompositionalTransmission.formed_teacher_can_teach_after_supported_preparation

/-- **A reconstruction teaches a later participant:** on the same run, date two holds the usual
program. -/
theorem formed_succession_second {r : Run (Law.process successor)}
    (start : Trace formationProcess (prepared 25 4) [.develop] (r.state 0)) :
    (r.state 2).installed = some (programFor usual) := by
  have h0 := FormationTracesInherited.trace_iff.mp start
  have h2 : r.state 2 = successor (successor (r.state 0)) :=
    (r.step 1).trans (congrArg successor (r.step 0))
  rw [h2, h0]
  exact CompositionalTransmission.successful_reconstruction_can_teach_a_later_participant

/-- **An execution-only budget interrupts teaching.** Where the run of succession starts where the
formation course `[develop]` from eighteen units and four parts ends, the basic course from it
delivers only the two primitive records, and the successor is blocked with nothing installed. -/
theorem budget_succession_blocked {r : Run (Law.process successor)}
    {y : CompositionalTransmission.Exchange}
    (start : Trace formationProcess (prepared 18 4) [.develop] (r.state 0))
    (course : Trace queryProcess ⟨r.state 0, blank 25 8⟩ basic y) :
    y.receiver.samples = [(p0, [false]), (p1, [true])] ∧
      (r.state 1).installed = none ∧ (r.state 1).blocked = true := by
  have h0 := FormationTracesInherited.trace_iff.mp start
  have hy := QueryTraces.trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hy
  rw [h1, h0]
  exact CompositionalTransmission.execution_only_budget_can_interrupt_teaching

/-- **A peer's demonstration can repair without new generation.** On a run of succession from the
collapsed code's teacher with eleven units, the peer at date one holds the duplicating program;
one further query from a teacher running the code's program, followed by reconsideration, installs
the code's program, which answers the further expression. -/
theorem peer_repair {r : Run (Law.process successor)} {y : CompositionalTransmission.Exchange}
    {z : CompositionalFormation.Frame} (start : r.state 0 = source (programFor collapsed) 11)
    (course : Trace queryProcess ⟨source (programFor collapsed) 4, r.state 1⟩ [novel] y)
    (revised : Trace formationProcess y.receiver [.reconsider] z) :
    (r.state 1).installed = some duplicated ∧ z.installed = some (programFor collapsed) ∧
      respond z further = some ([false, false, false], 5) := by
  have hz := FormationTracesInherited.trace_iff.mp revised
  have hy := QueryTraces.trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hz
  subst hy
  rw [h1, start]
  exact CompositionalTransmission.peer_demonstration_can_repair_without_new_generation

/-- **An erroneous peer demonstration keeps the error.** On the same run, one further query from
a teacher running the duplicating program, followed by reconsideration, keeps the duplicating
program. -/
theorem peer_keeps_error {r : Run (Law.process successor)} {y : CompositionalTransmission.Exchange}
    {z : CompositionalFormation.Frame} (start : r.state 0 = source (programFor collapsed) 11)
    (course : Trace queryProcess ⟨source duplicated 5, r.state 1⟩ [novel] y)
    (revised : Trace formationProcess y.receiver [.reconsider] z) :
    z.installed = some duplicated := by
  have hz := FormationTracesInherited.trace_iff.mp revised
  have hy := QueryTraces.trace_iff.mp course
  have h1 : r.state 1 = successor (r.state 0) := r.step 0
  subst hz
  subst hy
  rw [h1, start]
  exact CompositionalTransmission.erroneous_peer_demonstration_can_preserve_error

end Succession

end QueryTracesInherited

end Becoming
