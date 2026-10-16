import FormationRoot
import SuccessionPreparation

/-!
# Restoration changes the conditions of further activity

The existing material process supplies the changing conditions themselves:
repair restores the site; the same restored site no longer admits repair and
can capture available support. Consumption can reopen capture without damaging
the site. No completion label, demand field, controller or value score is added.
The laws remain the existing conditional material model, not a derivation of
all chemistry, cognition, ethical significance or indefinite regeneration.
-/

namespace Generative.RepairApplicability

open FormedSelection

theorem bit_bound (b : Bool) : bit b ≤ 1 := by cases b <;> decide

/-- Exact disturbance/restoration balance, independent of an observer's score. -/
theorem step_restoration_balance {material : Nat} {s t : State} {event : Event}
    (step : Step material s event t) :
    bit t.intact + eventIndicator .damage event =
      bit s.intact + eventIndicator .repair event := by
  rcases step with ⟨_, enabled, rfl⟩
  cases event <;> cases hi : s.intact <;>
    simp_all [Enabled, advance, bit, eventIndicator]

theorem trace_restoration_balance {material : Nat} {s t : State} {events : List Event}
    (history : Generative.Trace (rootProcess material) s events t) :
    bit t.intact + tally (eventIndicator .damage) events =
      bit s.intact + tally (eventIndicator .repair) events := by
  induction history with
  | nil => simp only [tally, Nat.add_zero]
  | cons step _ ih =>
    have localBalance := step_restoration_balance step
    simp only [tally]
    omega

theorem tally_zero_of_absent (target : Event) {events : List Event}
    (absent : target ∉ events) : tally (eventIndicator target) events = 0 := by
  induction events with
  | nil => rfl
  | cons event events ih =>
    have unequal : event ≠ target := by
      intro equal
      exact absent (List.mem_cons.mpr (Or.inl equal.symm))
    have tail : target ∉ events := fun h => absent (List.mem_cons.mpr (Or.inr h))
    simp only [tally, eventIndicator, unequal, ↓reduceIte, Nat.zero_add]
    exact ih tail

/-- Once intact, every later repair must be matched by actual later damage. -/
theorem later_repairs_bounded_by_new_damage {material : Nat} {s t : State}
    {events : List Event} (history : Generative.Trace (rootProcess material) s events t)
    (restored : s.intact = true) :
    tally (eventIndicator .repair) events ≤ tally (eventIndicator .damage) events := by
  have balance := trace_restoration_balance history
  have upper := bit_bound t.intact
  rw [restored] at balance
  change bit t.intact + _ = 1 + _ at balance
  omega

/-- An admissible further repair after restoration requires an intervening
damage event in the very same prefix, not merely the passage of time. -/
theorem new_repair_requires_intervening_damage {material : Nat} {s t u : State}
    {events : List Event} (history : Generative.Trace (rootProcess material) s events t)
    (restored : s.intact = true) (repair : Step material t .repair u) :
    Event.damage ∈ events := by
  by_cases occurred : Event.damage ∈ events
  · exact occurred
  · have balance := trace_restoration_balance history
    have zero := tally_zero_of_absent .damage occurred
    have damaged := repair.2.1.2.1
    rw [restored, damaged, zero] at balance
    change 0 + 0 = 1 + _ at balance
    omega

/-- Restoration itself removes the material condition for more repair and
damage-triggered formation, while preserving the remaining capacities. -/
theorem repair_removes_own_condition {material : Nat} {s t : State}
    (step : Step material s .repair t) :
    t.intact = true ∧ ¬ Enabled material t .repair ∧
    ¬ Enabled material t .formA ∧ ¬ Enabled material t .formH ∧
    t.fuel + 1 = s.fuel ∧ t.source = s.source ∧ t.localFuel = s.localFuel := by
  rcases step with ⟨_, enabled, rfl⟩
  simp only [advance, Enabled]
  have fuel := enabled.2.2
  exact ⟨rfl, by simp, by simp, by simp, by omega, rfl, rfl⟩

theorem restored_capture_uses_current_conditions {material : Nat} {s t : State}
    (step : Step material s .repair t) (empty : s.localFuel = false)
    (source : 0 < s.source) : Enabled material t .capture := by
  rcases step with ⟨_, _, rfl⟩
  exact ⟨rfl, empty, source⟩

theorem capture_removes_own_condition {material : Nat} {s t : State}
    (step : Step material s .capture t) :
    t.localFuel = true ∧ ¬ Enabled material t .capture ∧
    t.intact = s.intact ∧ t.fuel = s.fuel ∧ t.source + 1 = s.source := by
  rcases step with ⟨_, enabled, rfl⟩
  exact ⟨rfl, by simp [Enabled, advance], rfl, rfl, by
    change s.source - 1 + 1 = s.source
    have positive := enabled.2.2
    omega⟩

/-- Existing local use can reopen capture while the restored site stays intact.
Captured local fuel does not replenish the separate common fuel account. -/
theorem local_copy_reopens_capture {material : Nat} {s t : State}
    (step : Step material s .localCopyA t) (intact : s.intact = true)
    (source : 0 < s.source) :
    Enabled material t .capture ∧ ¬ Enabled material t .repair ∧
    t.intact = s.intact ∧ t.fuel = s.fuel ∧ t.source = s.source := by
  rcases step with ⟨_, _, rfl⟩
  exact ⟨⟨intact, rfl, source⟩, by simp [Enabled, advance, intact], rfl, rfl, rfl⟩

/-- Restoration and available future capture are distinct when support is absent. -/
theorem restoration_without_source_has_no_capture {material : Nat} {s t : State}
    (step : Step material s .repair t) (emptySource : s.source = 0) :
    t.intact = true ∧ ¬ Enabled material t .capture := by
  rcases step with ⟨_, _, rfl⟩
  exact ⟨rfl, by simp [Enabled, advance, emptySource]⟩

namespace Actual

/-- This is the already checked formation ancestor of the accepted successor. -/
def formed := SuccessionPreparation.formed 360 230
def disturbed := advance formed .damage
def restoredAgain := advance disturbed .repair
def worn := advance formed .wearFreeA
def locallyUsed := advance worn .localCopyA
def recaptured := advance locallyUsed .capture

theorem existing_formed_prefix :
    Generative.Trace (rootProcess 78) (SuccessionPreparation.start 360 230)
      SuccessionPreparation.word formed :=
  trace_to_root SuccessionPreparation.prospective_formation_trace

/-- Neither closure is explained by fuel/source exhaustion in this actual state. -/
theorem restored_with_spare_support :
    formed.intact = true ∧ formed.localFuel = true ∧ formed.fuel = 293 ∧
    formed.source = 216 ∧ formed.resident = .active ∧
    ¬ Enabled 78 formed .repair ∧ ¬ Enabled 78 formed .capture := by
  exact ⟨by decide, by decide, by decide, by decide, by decide, by decide, by decide⟩

theorem actual_disturbance_restoration :
    Generative.Trace (rootProcess 78) formed [.damage, .repair] restoredAgain ∧
    restoredAgain.intact = true ∧ restoredAgain.fuel = formed.fuel - 1 ∧
    restoredAgain.source = formed.source ∧ restoredAgain.localFuel = formed.localFuel := by
  refine ⟨.cons (m := disturbed) ?_ (.cons ?_ (.nil _)), by decide, by decide, by decide, by decide⟩
  · change Step 78 formed .damage disturbed
    decide
  · change Step 78 disturbed .repair restoredAgain
    decide

/-- A bounded actual suffix continues resource use/reconstruction after repair.
The first event releases occupied precursor; no free material is installed. -/
theorem actual_local_reconstruction_and_capture :
    Generative.Trace (rootProcess 78) formed
      [.wearFreeA, .localCopyA, .capture] recaptured ∧
    recaptured.intact = true ∧ recaptured.localFuel = true ∧
    recaptured.fuel = formed.fuel ∧ recaptured.source + 1 = formed.source ∧
    population recaptured = population formed := by
  refine ⟨.cons (m := worn) ?_ (.cons (m := locallyUsed) ?_ (.cons ?_ (.nil _))),
    by decide, by decide, by decide, by decide, by decide⟩
  · change Step 78 formed .wearFreeA worn
    decide
  · change Step 78 worn .localCopyA locallyUsed
    decide
  · change Step 78 locallyUsed .capture recaptured
    decide

theorem actual_continuation_keeps_whole_history :
    Generative.Trace (rootProcess 78) (SuccessionPreparation.start 360 230)
      (SuccessionPreparation.word ++ [.wearFreeA, .localCopyA, .capture]) recaptured ∧
    energy recaptured + tally expenditure
      (SuccessionPreparation.word ++ [.wearFreeA, .localCopyA, .capture]) =
      energy (SuccessionPreparation.start 360 230) := by
  have history := Generative.trace_append_iff.mpr
    ⟨formed, existing_formed_prefix, actual_local_reconstruction_and_capture.1⟩
  exact ⟨history, root_energy_ledger history⟩

end Actual
end Generative.RepairApplicability

#print axioms Generative.RepairApplicability.bit_bound
#print axioms Generative.RepairApplicability.step_restoration_balance
#print axioms Generative.RepairApplicability.trace_restoration_balance
#print axioms Generative.RepairApplicability.tally_zero_of_absent
#print axioms Generative.RepairApplicability.later_repairs_bounded_by_new_damage
#print axioms Generative.RepairApplicability.new_repair_requires_intervening_damage
#print axioms Generative.RepairApplicability.repair_removes_own_condition
#print axioms Generative.RepairApplicability.restored_capture_uses_current_conditions
#print axioms Generative.RepairApplicability.capture_removes_own_condition
#print axioms Generative.RepairApplicability.local_copy_reopens_capture
#print axioms Generative.RepairApplicability.restoration_without_source_has_no_capture
#print axioms Generative.RepairApplicability.Actual.existing_formed_prefix
#print axioms Generative.RepairApplicability.Actual.restored_with_spare_support
#print axioms Generative.RepairApplicability.Actual.actual_disturbance_restoration
#print axioms Generative.RepairApplicability.Actual.actual_local_reconstruction_and_capture
#print axioms Generative.RepairApplicability.Actual.actual_continuation_keeps_whole_history
