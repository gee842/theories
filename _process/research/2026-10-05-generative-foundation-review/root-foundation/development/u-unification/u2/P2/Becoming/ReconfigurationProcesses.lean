import GenerativeCore
import CorrectionReconfiguration

/-!
# Reconfiguration as a process: the rearrangement step of `CorrectionReconfiguration`

`CorrectionReconfiguration.reconfigure` replaces the arrangement of a managed installation (its
roster, each member's fault formula and the root-fault bounds) by a candidate arrangement, where
the step is open, the candidate's induced fault sets are separated (`ready`), and the reserve and
the time left cover the step's own cost together with the response cost of the candidate; the
step renews the installation's epoch and serial and charges the cost, and otherwise there is no
step. A partial transition is a process of the core: its configurations are the managed
installations, its actions the rearrangements (whether the step is open, its cost, the depth of
response provided for, the candidate), and its steps are the transitions `reconfigure` gives
(`process`, `step_iff`); an action is enabled exactly where `reconfigure` gives a configuration
(`enabled_iff`). This module states the module's computed cases as laws of that process.

* **No step to a roster sharing a cause.** From the original installation the process has no
  step to the arrangement in which two reviewers fail by one shared cause (`shared_cause_no_step`,
  through `CorrectionReconfiguration.reform_rejects_shared_control`).
* **A step to the repaired roster.** From the original installation the process steps to the
  repaired four-member arrangement, and every such step leaves reserve 18, spends 2, and renews
  the epoch to 8 and the serial to 1 (`separated_repair_steps`, through
  `CorrectionReconfiguration.repaired_reform_installs`).
* **The step's cost alone is not enough.** From an installation whose reserve covers the step's
  own cost but not that cost together with the candidate's response cost, the process has no step
  (`own_cost_alone_no_step`, through `CorrectionReconfiguration.review_alone_funded_is_not_enough`),
  and with exactly that combined reserve and time it has one (`combined_cost_steps`, through
  `CorrectionReconfiguration.exact_combined_budget_suffices`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative CorrectionReconfiguration

namespace ReconfigurationProcesses

/-- A rearrangement: whether the step is open, its cost, the depth of response it provides for,
and the candidate arrangement. -/
structure Rearrangement where
  opened : Bool
  cost : Nat
  depth : Nat
  candidate : Arrangement

/-- The reconfiguration process: a managed installation steps by a rearrangement to the
configuration `reconfigure` gives. -/
def process : Process Managed Rearrangement :=
  ⟨fun old m new => reconfigure m.opened m.cost m.depth m.candidate old = some new⟩

/-- **The steps of the process are the transitions of `reconfigure`.** -/
theorem step_iff {old new : Managed} {m : Rearrangement} :
    process.step old m new ↔ reconfigure m.opened m.cost m.depth m.candidate old = some new :=
  Iff.rfl

/-- **A rearrangement is enabled exactly where `reconfigure` gives a configuration.** -/
theorem enabled_iff {old : Managed} {m : Rearrangement} :
    Enabled process old m ↔ (reconfigure m.opened m.cost m.depth m.candidate old).isSome = true :=
  ⟨fun ⟨_, h⟩ => (congrArg Option.isSome h).trans rfl,
   fun h => match e : reconfigure m.opened m.cost m.depth m.candidate old with
    | some new => ⟨new, e⟩
    | none => Bool.noConfusion ((congrArg Option.isSome e).symm.trans h)⟩

/-- The rearrangement to the arrangement whose first two reviewers share a cause. -/
def toMerged : Rearrangement := ⟨true, 2, 0, merged3⟩

/-- The rearrangement to the repaired four-member arrangement. -/
def toRepaired : Rearrangement := ⟨true, 2, 0, repaired4⟩

/-- The original installation with reserve 12. -/
def lowReserve : Managed :=
  ⟨separate3, {FaultTolerantCorrection.initial with
    state := {FaultTolerantCorrection.initial.state with reserve := 12}}⟩

/-- The original installation with reserve and deadline 13. -/
def combinedReserve : Managed :=
  ⟨separate3, {FaultTolerantCorrection.initial with
    state := {FaultTolerantCorrection.initial.state with reserve := 13, deadline := 13}}⟩

/-- **No step to a roster sharing a cause.** From the original installation the reconfiguration
process has no step to the arrangement whose first two reviewers fail by one cause. -/
theorem shared_cause_no_step : ¬ Enabled process original toMerged :=
  fun ⟨_, h⟩ => nomatch reform_rejects_shared_control.symm.trans h

/-- **A step to the repaired roster.** From the original installation the reconfiguration process
steps to the repaired arrangement, and every such step leaves reserve 18, spends 2, and renews the
epoch to 8 and the serial to 1. -/
theorem separated_repair_steps :
    Enabled process original toRepaired ∧
      ∀ next, process.step original toRepaired next →
        next.installation.state.reserve = 18 ∧ next.installation.state.spent = 2 ∧
          next.installation.state.authority = 8 ∧ next.installation.serial = 1 :=
  have installs := repaired_reform_installs
  ⟨enabled_iff.mpr installs.1, fun next h =>
    have same : renewed = next := congrArg (fun o => Option.getD o original) (step_iff.mp h)
    ⟨Eq.subst (motive := fun x : Managed => x.installation.state.reserve = 18) same installs.2.1,
     Eq.subst (motive := fun x : Managed => x.installation.state.spent = 2) same installs.2.2.1,
     Eq.subst (motive := fun x : Managed => x.installation.state.authority = 8) same
       installs.2.2.2.1,
     Eq.subst (motive := fun x : Managed => x.installation.serial = 1) same installs.2.2.2.2⟩⟩

/-- **The step's own cost alone is not enough.** From the installation with reserve 12, which
covers the rearrangement's cost of 2 but not that cost with the repaired arrangement's response
cost, the reconfiguration process has no step to the repaired arrangement. -/
theorem own_cost_alone_no_step :
    toRepaired.cost ≤ lowReserve.installation.state.reserve ∧
      ¬ Enabled process lowReserve toRepaired :=
  ⟨review_alone_funded_is_not_enough.1,
   fun ⟨_, h⟩ => nomatch review_alone_funded_is_not_enough.2.symm.trans h⟩

/-- **The combined cost is enough.** From the installation with reserve and deadline 13, exactly
the rearrangement's cost with the repaired arrangement's response cost, the reconfiguration
process steps to the repaired arrangement. -/
theorem combined_cost_steps : Enabled process combinedReserve toRepaired :=
  enabled_iff.mpr exact_combined_budget_suffices

end ReconfigurationProcesses

end Becoming
