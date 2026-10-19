import Becoming.ReducedRuns
import Becoming.TrainingProcessesInherited
import CompositionalFormation

/-!
# Formation traces: the formation apparatus's moves as a process (periphery-join ring)

`CompositionalFormation` has an apparatus whose configuration holds wires, an installed program,
support and spent amounts, parts and used parts, a blocked flag, samples and the attempts made. Its
moves are placing a socket (`place`), inspecting the wired route against the samples with the
primitives of some evidence (`inspect`), discarding the wiring (`discard`), developing a route by
searching the generated routes (`develop`), encountering a further demonstration of a code on an
expression (`encounter`), and reconsidering the installed program against the samples
(`reconsider`). This module reads them as one process of the spine: configurations are the
apparatus's configurations, moves are these six (`FormationMove`), and each move takes a
configuration where the periphery's function takes it (`formationProcess`, a law of change with
moves, `Assurance.ofMap`). A course of the process ends exactly where its moves, taken in turn,
take the start (`trace_iff`). The periphery's laws are then stated of the moves and courses.

* **Conserved amounts.** Every move keeps support plus spent (`step_support`), so every course
  does (`course_support`); a placing move keeps parts plus used parts (`place_parts`).
* **Inspection.** An inspection from an unblocked configuration with support installs a program
  exactly where the program wired with the evidence's primitives fits the samples
  (`inspect_installed`). Where the samples are the trial records of a code `c` and the wired route
  is generated, an installed program carries the primitives of `c` to every expression's value,
  given distinct primitives (`inspection_transfers`) or the trial records extended by the novel
  demonstration (`extended_inspection_transfers`); where the wired route is `c`'s own, inspection
  installs `c`'s program (`inspection_installs_own`).
* **The example courses.** From the configuration the periphery prepares by training, the one-move
  course `[develop]` builds and replaces a wrong route, keeps the acquired records, executes the
  novel expression and spends seven units (`develop_course_*`); with too few parts or too little
  support, or with the switched or collapsed code, it ends as the periphery states
  (`develop_course_no_parts`, `develop_course_partial`, `develop_course_short`,
  `develop_course_switched`, `develop_course_collapsed`, `develop_course_unobserved`). Removing the
  installed program from where the course ends keeps its attempts and removes its response
  (`develop_course_removed`). The three-move course `[develop, encounter, reconsider]` for the
  collapsed code replaces the failing route and keeps the cost of failure, or blocks without
  parts (`repair_course_*`). The training step that prepares the start installs the code but gives
  no response (`training_alone_no_response`).

This module belongs to the periphery-join ring. It adds no axiom of its own and uses no `simp`,
`omega` or `decide`. Its declarations inherit `propext` from the definitions of `develop`,
`reconsider` and `train` (through `readEvidence`), and `Quot.sound` as well from
`placing_preserves_support`, `placing_accounts_parts`, `inspecting_preserves_support`,
`discarding_preserves_support`, `development_preserves_support`, `encounter_preserves_support`,
`reconsideration_preserves_support`, `correct_program_fits_actual_records`,
`accepted_generated_program_transfers` and `extra_probe_restores_transfer_for_generated_routes`;
the example courses inherit `propext` from the periphery's `decide` witnesses. No ethical predicate
or ranking occurs.
-/

namespace Becoming

open Generative

namespace FormationTracesInherited

open Generative.CompositionalAcquisition
  (Code Expr Evidence novel usual switched trialRecords eval train initial)
open Generative.CompositionalFormation
  (Program Route place inspect discard develop encounter reconsider respond fits operate programFor
   routeFor generatedRoutes prepared collapsed duplicated further)

/-- The moves of the formation apparatus. -/
inductive FormationMove where
  | place (socket : Bool)
  | inspect (e : Evidence)
  | discard
  | develop
  | encounter (c : Code) (e : Expr)
  | reconsider

/-- Where each move takes a configuration: the periphery's function for that move. -/
def formationStep (s : CompositionalFormation.Frame) :
    FormationMove → CompositionalFormation.Frame
  | .place socket => place socket s
  | .inspect e => inspect e s
  | .discard => discard s
  | .develop => develop s
  | .encounter c e => encounter c e s
  | .reconsider => reconsider s

/-- The formation apparatus read as a process. -/
def formationProcess : Process CompositionalFormation.Frame FormationMove :=
  Assurance.ofMap formationStep

/-- Every list of moves is a course of the formation process, ending where the moves take it. -/
theorem course_of_moves : ∀ (ms : List FormationMove) (s : CompositionalFormation.Frame),
    Trace formationProcess s ms (ms.foldl formationStep s)
  | [], s => .nil s
  | m :: ms, s => .cons (rfl : formationStep s m = formationStep s m) (course_of_moves ms _)

/-- **The courses of the formation process end exactly where their moves take the start.** -/
theorem trace_iff {s t : CompositionalFormation.Frame} {ms : List FormationMove} :
    Trace formationProcess s ms t ↔ t = ms.foldl formationStep s :=
  ⟨ReducedRuns.trace_foldl, fun ends => ends ▸ course_of_moves ms s⟩

/-! ## Conserved amounts -/

/-- **Every move keeps support plus spent.** -/
theorem step_support (s : CompositionalFormation.Frame) :
    ∀ m, (formationStep s m).support + (formationStep s m).spent = s.support + s.spent
  | .place socket => CompositionalFormation.placing_preserves_support socket s
  | .inspect e => CompositionalFormation.inspecting_preserves_support e s
  | .discard => CompositionalFormation.discarding_preserves_support s
  | .develop => CompositionalFormation.development_preserves_support s
  | .encounter c e => CompositionalFormation.encounter_preserves_support c e s
  | .reconsider => CompositionalFormation.reconsideration_preserves_support s

/-- **Every course of the formation process keeps support plus spent.** -/
theorem course_support : ∀ {s t : CompositionalFormation.Frame} {ms : List FormationMove},
    Trace formationProcess s ms t → t.support + t.spent = s.support + s.spent
  | _, _, [], .nil _ => rfl
  | s, _, m :: _, .cons moved rest =>
    (course_support rest).trans
      ((congrArg (fun x : CompositionalFormation.Frame => x.support + x.spent) moved).trans
        (step_support s m))

/-- **A placing move keeps parts plus used parts.** -/
theorem place_parts {s t : CompositionalFormation.Frame} {socket : Bool}
    (step : formationProcess.step s (.place socket) t) :
    t.parts + t.usedParts = s.parts + s.usedParts :=
  (congrArg (fun x : CompositionalFormation.Frame => x.parts + x.usedParts) step).trans
    (CompositionalFormation.placing_accounts_parts socket s)

/-! ## Inspection -/

/-- **An inspection from an unblocked configuration with support installs a program exactly where
the program wired with the evidence's primitives fits the samples.** -/
theorem inspect_installed {s t : CompositionalFormation.Frame} {e : Evidence}
    (step : formationProcess.step s (.inspect e) t) (ready : s.blocked = false)
    (support : 1 ≤ s.support) :
    t.installed = if fits ⟨e.first, e.second, s.wires⟩ s.samples = true
      then some ⟨e.first, e.second, s.wires⟩ else none :=
  have open_ : ¬ s.blocked = true := fun blocked => Bool.noConfusion (ready.symm.trans blocked)
  have inner : (inspect e s).installed = if fits ⟨e.first, e.second, s.wires⟩ s.samples = true
      then some ⟨e.first, e.second, s.wires⟩ else none := by
    unfold inspect
    rw [if_neg open_, if_pos support]
  (congrArg CompositionalFormation.Frame.installed step).trans inner

/-- Where a Boolean test installs `p` or nothing, an installed program is `p` and the test
held. -/
theorem installed_of_test {b : Bool} {p q : Program}
    (installed : (if b = true then some p else none) = some q) : b = true ∧ q = p :=
  match b, installed with
  | true, installed => ⟨rfl, (Option.some.inj installed).symm⟩
  | false, installed =>
    have absent : (none : Option Program) = some q := installed
    nomatch absent

/-- **An inspection against a code's trial records installs only a program that evaluates every
expression as the code does**, where the wired route is generated and the code's primitives
differ. -/
theorem inspection_transfers {s t : CompositionalFormation.Frame} {c : Code} {o : List Bool}
    {q : Program} (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (support : 1 ≤ s.support)
    (records : s.samples = trialRecords c) (generated : s.wires ∈ generatedRoutes 2)
    (distinct : c.first ≠ c.second) (installed : t.installed = some q) :
    ∀ x, operate q x = eval c x :=
  match installed_of_test ((inspect_installed step ready support).symm.trans installed) with
  | ⟨accepted, same⟩ => same ▸
      CompositionalFormation.accepted_generated_program_transfers c s.wires distinct generated
        (records ▸ accepted)

/-- **An inspection against a code's trial records extended by the novel demonstration installs
only a program that evaluates every expression as the code does**, where the wired route is
generated. -/
theorem extended_inspection_transfers {s t : CompositionalFormation.Frame} {c : Code}
    {o : List Bool} {q : Program}
    (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (support : 1 ≤ s.support)
    (records : s.samples = trialRecords c ++ [(novel, eval c novel)])
    (generated : s.wires ∈ generatedRoutes 2) (installed : t.installed = some q) :
    ∀ x, operate q x = eval c x :=
  match installed_of_test ((inspect_installed step ready support).symm.trans installed) with
  | ⟨accepted, same⟩ => same ▸
      CompositionalFormation.extra_probe_restores_transfer_for_generated_routes c s.wires
        generated (records ▸ accepted)

/-- **Where the wired route is a code's own and the samples are its trial records, inspection
installs the code's program.** -/
theorem inspection_installs_own {s t : CompositionalFormation.Frame} {c : Code} {o : List Bool}
    (step : formationProcess.step s (.inspect ⟨c.first, c.second, o⟩) t)
    (ready : s.blocked = false) (support : 1 ≤ s.support)
    (records : s.samples = trialRecords c) (wired : s.wires = routeFor c) :
    t.installed = some (programFor c) :=
  have fitsOwn : fits ⟨c.first, c.second, s.wires⟩ s.samples = true :=
    records ▸ wired ▸ CompositionalFormation.correct_program_fits_actual_records c
  (inspect_installed step ready support).trans
    ((if_pos fitsOwn).trans
      (congrArg (fun r : Route => (some ⟨c.first, c.second, r⟩ : Option Program)) wired))

/-! ## The example courses -/

/-- **The training step that prepares the start installs the usual code, and the apparatus formed
from it gives no response to the novel expression.** -/
theorem training_alone_no_response {l : CompositionalAcquisition.Learner}
    (step : TrainingProcessesInherited.trainProcess.step (initial 18) usual l) :
    l.code = some usual ∧
      respond (CompositionalFormation.fromLearner l 4) novel = none :=
  step ▸ CompositionalFormation.interpretation_alone_does_not_supply_route

section Develop

variable {y : CompositionalFormation.Frame}

/-- **The one-move course builds a wrong route, tries it and replaces it.** -/
theorem develop_course_replaces (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.attempts = [([false, false], false), ([false, true], true)] ∧
      y.installed = some (programFor usual) :=
  (trace_iff.mp course) ▸ CompositionalFormation.incorrect_route_is_built_tried_and_replaced

/-- **The one-move course keeps the records of the training that prepared it.** -/
theorem develop_course_records (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.samples = (train usual (initial 18)).records :=
  (trace_iff.mp course) ▸ CompositionalFormation.development_retains_actual_acquisition

/-- **Where the one-move course ends, the formed route executes the novel expression.** -/
theorem develop_course_executes (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    respond y novel = some ([false, false, true], 0) :=
  (trace_iff.mp course) ▸ CompositionalFormation.formed_route_executes_novel_expression

/-- **The one-move course's account:** seven units spent, four left, four parts used, none left. -/
theorem develop_course_account (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    y.spent = 7 ∧ y.support = 4 ∧ y.usedParts = 4 ∧ y.parts = 0 ∧
      7 + y.spent + y.support = 18 :=
  (trace_iff.mp course) ▸ CompositionalFormation.whole_example_account

/-- **Removing the installed program where the one-move course ends keeps the attempts and
removes the response.** -/
theorem develop_course_removed (course : Trace formationProcess (prepared 18 4) [.develop] y) :
    ({y with installed := none} : CompositionalFormation.Frame).attempts = y.attempts ∧
      respond {y with installed := none} novel = none :=
  (trace_iff.mp course) ▸
    CompositionalFormation.retained_verdict_does_not_replace_damaged_connection

/-- **Without parts the one-move course keeps the record but blocks formation.** -/
theorem develop_course_no_parts (course : Trace formationProcess (prepared 18 0) [.develop] y) :
    y.samples = trialRecords usual ∧ y.blocked = true ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ CompositionalFormation.no_parts_preserves_record_but_blocks_formation

/-- **With one part the one-move course keeps what the partial assembly consumed.** -/
theorem develop_course_partial (course : Trace formationProcess (prepared 18 1) [.develop] y) :
    y.wires = [false] ∧ y.spent = 1 ∧ y.parts = 0 ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ CompositionalFormation.partial_assembly_keeps_consumption

/-- **With fourteen units the one-move course forms the route but leaves no support to execute
the novel expression.** -/
theorem develop_course_short (course : Trace formationProcess (prepared 14 4) [.develop] y) :
    y.installed = some (programFor usual) ∧ respond y novel = none :=
  (trace_iff.mp course) ▸ CompositionalFormation.interpreted_and_formed_can_lack_execution_support

/-- **For the switched code the one-move course tries three routes and forms the reversed one.** -/
theorem develop_course_switched
    (course : Trace formationProcess (prepared 22 6 switched) [.develop] y) :
    y.attempts = [([false, false], false), ([false, true], false), ([true, false], true)] ∧
      respond y novel = some ([true, false, false], 0) :=
  (trace_iff.mp course) ▸ CompositionalFormation.reverse_order_requires_different_formed_route

/-- **For the collapsed code the one-move course forms a route that fails the novel
expression.** -/
theorem develop_course_collapsed
    (course : Trace formationProcess (prepared 15 2 collapsed) [.develop] y) :
    y.installed = some duplicated ∧ respond y novel = some ([false, false, false, false], 0) :=
  (trace_iff.mp course) ▸ CompositionalFormation.expanded_repertoire_can_form_a_failing_route

/-- **Unobserved, the failing route stays installed and answers the further expression.** -/
theorem develop_course_unobserved
    (course : Trace formationProcess (prepared 27 6 collapsed) [.develop] y) :
    y.installed = some duplicated ∧ respond y further = some ([false, false], 14) :=
  (trace_iff.mp course) ▸ CompositionalFormation.unobserved_failure_can_retain_wrong_operation

end Develop

section Repair

variable {y : CompositionalFormation.Frame}

/-- The three-move course of repair for the collapsed code. -/
def repair : List FormationMove := [.develop, .encounter collapsed novel, .reconsider]

/-- **The repair course rebuilds from the fresh record.** -/
theorem repair_course_rebuilds
    (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    y.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
      y.attempts =
        [([false, false], true), ([false, false], false), ([false, false], false),
          ([false, true], true)] ∧
      y.installed = some (programFor collapsed) :=
  (trace_iff.mp course) ▸ CompositionalFormation.fresh_record_changes_actual_reconstruction

/-- **The repaired route answers a further expression no record holds.** -/
theorem repair_course_further (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    further ∉ y.samples.map Prod.fst ∧ respond y further = some ([false, false, false], 0) :=
  (trace_iff.mp course) ▸
    CompositionalFormation.repaired_operation_uses_a_further_untrained_expression

/-- **The repair course keeps the cost of failure:** sixteen units spent and six parts used. -/
theorem repair_course_account (course : Trace formationProcess (prepared 27 6 collapsed) repair y) :
    y.spent = 16 ∧ y.support = 4 ∧ y.usedParts = 6 ∧ y.parts = 0 ∧
      7 + y.spent + y.support = 27 :=
  (trace_iff.mp course) ▸ CompositionalFormation.repair_keeps_the_cost_of_failure

/-- **With two parts the repair course records the discrepancy but blocks.** -/
theorem repair_course_no_parts
    (course : Trace formationProcess (prepared 27 2 collapsed) repair y) :
    y.blocked = true ∧ y.samples = trialRecords collapsed ++ [(novel, eval collapsed novel)] ∧
      y.installed = none ∧ respond y further = none :=
  (trace_iff.mp course) ▸ CompositionalFormation.discrepancy_alone_does_not_supply_repair_parts

end Repair

end FormationTracesInherited

end Becoming
