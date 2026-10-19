import Becoming.Assurance
import CompositionalAcquisition

/-!
# Training processes: the acquisition learner's step as a process (periphery-join ring)

`CompositionalAcquisition` has a learner holding an optional code, a support amount and a list of
records. Training under a code `c` (`train c`) spends the three trial records' cost when the
learner can afford it, appends those records and installs the code read from them; otherwise it
leaves the learner as it is. Executing an expression (`execute`) spends its cost from the
remaining support. This module reads training as a process of the spine: configurations are
learners, moves are codes, and the move `c` takes a learner to the learner `train c` leaves
(`trainProcess`, a law of change with moves, `Assurance.ofMap`; `step_iff` makes the reading
exact). The periphery's laws of training are then stated of its steps.

* **What a step keeps.** A step under `c` from a learner with at least seven units of support
  appends the trial records of `c` (`step_records`), leaves seven units fewer (`step_support`) and,
  where the two primitives of `c` differ, installs `c` (`step_installs`). A step the learner cannot
  afford leaves it unchanged (`step_rests_when_short`).
* **The installed code transfers.** After an affordable step the learner holds the code acquired
  from the trial records, and where the primitives differ that code evaluates every expression as
  `c` does (`step_code_transfers`). From a learner without records the step's records yield the
  evidence `c` shows (`step_evidence`).
* **Execution after a step.** Where the support covers the step and an execution, the execution
  returns `c`'s value and leaves support that, with the two costs, makes up the support before the
  step (`step_then_execute`). From eleven units the novel expression is executed with nothing left
  (`novel_after_step`); from seven units the code is installed but the novel expression cannot be
  executed (`installed_without_execution`).

This module belongs to the periphery-join ring. It adds no axiom of its own and uses no `simp`,
`omega` or `decide`. Its declarations inherit `propext` from the definition of `train` (through
`interpretationFromRecords` and `readEvidence`) and from `acquisition_cost`,
`training_uses_actual_records`, `training_support_conserved`, `insufficient_training_unchanged`,
`actual_records_supply_evidence`, `actual_records_form_interpretation`,
`novel_execution_from_acquisition` and `acquired_capacity_can_outlast_executable_support`, and
`Quot.sound` as well from `training_forms_interpreter`, `acquired_all_expressions`,
`acquired_execution` and `acquired_execution_conserved`. No ethical predicate or ranking occurs.
-/

namespace Becoming

open Generative

namespace TrainingProcessesInherited

open Generative.CompositionalAcquisition

/-- Training read as a process: configurations are learners, the move `c` trains under `c`. -/
def trainProcess : Process Learner Code := Assurance.ofMap fun s c => train c s

/-- **A step of the training process is exactly training.** -/
theorem step_iff {s t : Learner} {c : Code} : trainProcess.step s c t ↔ t = train c s := Iff.rfl

/-- **A step appends the trial records.** -/
theorem step_records {s t : Learner} {c : Code} (step : trainProcess.step s c t)
    (enough : 7 ≤ s.support) : t.records = s.records ++ trialRecords c :=
  step ▸ training_uses_actual_records c s enough

/-- **A step installs the code** where the learner can afford it and the primitives differ. -/
theorem step_installs {s t : Learner} {c : Code} (step : trainProcess.step s c t)
    (enough : 7 ≤ s.support) (distinct : c.first ≠ c.second) : t.code = some c :=
  step ▸ training_forms_interpreter c s enough distinct

/-- **A step spends seven units of support.** -/
theorem step_support {s t : Learner} {c : Code} (step : trainProcess.step s c t)
    (enough : 7 ≤ s.support) : t.support + 7 = s.support :=
  step ▸ training_support_conserved c s enough

/-- **A step the learner cannot afford leaves it unchanged.** -/
theorem step_rests_when_short {s t : Learner} {c : Code} (step : trainProcess.step s c t)
    (short : s.support < 7) : t = s :=
  step.trans (insufficient_training_unchanged c s short)

/-- **The installed code transfers.** After an affordable step the learner holds the code
acquired from the trial records; where the primitives differ, that code evaluates every expression
as `c` does. -/
theorem step_code_transfers {s t : Learner} {c : Code} (step : trainProcess.step s c t)
    (enough : 7 ≤ s.support) (distinct : c.first ≠ c.second) :
    t.code = some (acquire (observe c)) ∧ ∀ e, eval (acquire (observe c)) e = eval c e :=
  have afford : acquisitionCost c ≤ s.support :=
    Eq.subst (motive := fun k => k ≤ s.support) (acquisition_cost c).symm enough
  have trained : train c s = ⟨interpretationFromRecords (trialRecords c),
      s.support - acquisitionCost c, s.records ++ trialRecords c⟩ := if_pos afford
  ⟨(congrArg Learner.code (step.trans trained)).trans (actual_records_form_interpretation c),
   acquired_all_expressions c distinct⟩

/-- **From a learner without records, the step's records yield the evidence `c` shows.** -/
theorem step_evidence {n : Nat} {t : Learner} {c : Code}
    (step : trainProcess.step (initial n) c t) (enough : 7 ≤ n) :
    readEvidence t.records = some (observe c) :=
  (congrArg readEvidence (step_records step enough)).trans (actual_records_supply_evidence c)

/-- **Execution after a step.** Where the support covers the step and the execution of `e`, the
execution returns `c`'s value of `e`, and the support it leaves, with the costs of the execution
and of the step, makes up the support before the step. -/
theorem step_then_execute {s t : Learner} {c : Code} (e : Expr) (step : trainProcess.step s c t)
    (distinct : c.first ≠ c.second) (enough : 7 + operationCost c e ≤ s.support) :
    ∃ left, execute t e = some (eval c e, left) ∧ left + operationCost c e + 7 = s.support :=
  ⟨s.support - 7 - operationCost c e, step ▸ acquired_execution c s e distinct enough,
   acquired_execution_conserved c s e enough⟩

/-- **From eleven units, a step under the usual code executes the novel expression** with no
support left. -/
theorem novel_after_step {t : Learner} (step : trainProcess.step (initial 11) usual t) :
    execute t novel = some ([false, false, true], 0) :=
  step ▸ novel_execution_from_acquisition

/-- **From seven units, a step installs the usual code but leaves no support to execute the novel
expression.** -/
theorem installed_without_execution {t : Learner} (step : trainProcess.step (initial 7) usual t) :
    t.code = some usual ∧ execute t novel = none :=
  step ▸ acquired_capacity_can_outlast_executable_support

end TrainingProcessesInherited

end Becoming
