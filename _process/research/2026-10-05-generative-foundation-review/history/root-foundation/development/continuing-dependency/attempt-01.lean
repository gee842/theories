import FormedSelection

/-!
Necessary reconstruction support under all sixteen unchanged material events,
and a reached-shape contrast where equal aggregate energy admits different
continuations. No controller, sensor, goal update or autonomous wear is added.
The accompanying mathematical note gives the constructive sufficiency argument.
-/
namespace Generative.ReconstructionRequirement

open FormedSelection

def aGrowth : Event → Nat
  | .formA | .localCopyA | .bulkCopyA => 1
  | _ => 0

def count (e : Event) (es : List Event) := tally (eventIndicator e) es

theorem step_a_growth {M : Nat} {s t : State} {e : Event}
    (h : Step M s e t) : aCount t ≤ aCount s + aGrowth e := by
  rcases h with ⟨_, he, rfl⟩
  cases e <;> cases hr : s.resident <;>
    simp_all [Enabled, advance, aCount, activeResident, aGrowth] <;> omega

theorem trace_a_growth {M : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) : aCount t ≤ aCount s + tally aGrowth es := by
  induction h with
  | nil => simp [tally]
  | cons hs _ ih =>
    have hh := step_a_growth hs
    simp only [tally]
    omega

theorem growth_repair_cost (e : Event) :
    aGrowth e + eventIndicator .repair e ≤ expenditure e := by
  cases e <;> decide

theorem growth_repair_trace_cost (es : List Event) :
    tally aGrowth es + count .repair es ≤ tally expenditure es := by
  induction es with
  | nil => rfl
  | cons e es ih =>
    have hh := growth_repair_cost e
    simp only [count, tally] at *
    omega

theorem growth_repair_support {M n : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (restored : aCount s + n ≤ aCount t) :
    n + count .repair es ≤ s.fuel + bit s.localFuel + s.source := by
  have hg := trace_a_growth h
  have hc := growth_repair_trace_cost es
  have he := trace_energy_ledger h
  unfold energy at he
  omega

theorem step_source_balance {M : Nat} {s t : State} {e : Event}
    (h : Step M s e t) : t.source + eventIndicator .capture e = s.source := by
  rcases h with ⟨_, he, rfl⟩
  cases e <;> simp_all [Enabled, advance, eventIndicator] <;> omega

theorem trace_source_balance {M : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) : t.source + count .capture es = s.source := by
  induction h with
  | nil => simp [count, tally]
  | cons hs _ ih =>
    have hh := step_source_balance hs
    simp only [count, tally] at *
    omega

theorem no_capture_support {M n : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (restored : aCount s + n ≤ aCount t)
    (none : count .capture es = 0) : n ≤ s.fuel + bit s.localFuel := by
  have hg := trace_a_growth h
  have hc := growth_repair_trace_cost es
  have he := trace_energy_ledger h
  have hs := trace_source_balance h
  unfold energy at he
  omega

theorem step_intact_from_damage {M : Nat} {s t : State} {e : Event}
    (h : Step M s e t) (before : s.intact = false) (after : t.intact = true) :
    e = .repair := by
  rcases h with ⟨_, _, rfl⟩
  cases e <;> simp_all [advance]

theorem capture_from_damage_requires_repair {M : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (damaged : s.intact = false)
    (captured : 0 < count .capture es) : 0 < count .repair es := by
  induction h with
  | nil => simp [count, tally] at captured
  | @cons s u t e es hs ht ih =>
    by_cases er : e = .repair
    · subst e
      simp [count, tally, eventIndicator]
    · have headZero : eventIndicator .repair e = 0 := by
        simp [eventIndicator, er]
      have uc : u.intact = false := by
        cases hu : u.intact
        · rfl
        · exact False.elim (er (step_intact_from_damage hs damaged hu))
      have ec : e ≠ .capture := by
        intro ec
        subst e
        have enabled := hs.2.1.1
        simp_all
      have headCaptureZero : eventIndicator .capture e = 0 := by
        simp [eventIndicator, ec]
      have tailCaptured : 0 < count .capture es := by
        simpa [count, tally, headCaptureZero] using captured
      have tailRepair := ih uc tailCaptured
      simpa [count, tally, headZero] using tailRepair

theorem repairs_cost_common (es : List Event) :
    count .repair es ≤ tally commonExpenditure es := by
  induction es with
  | nil => rfl
  | cons e es ih =>
    have hh : eventIndicator .repair e ≤ commonExpenditure e := by cases e <;> decide
    simp only [count, tally] at *
    omega

/-- Least common-support expression from the accompanying constructive argument.
This module proves its necessity for every admitted trace, without restricting
the competing native event routes. -/
def requiredCommon (n : Nat) (s : State) : Nat :=
  if s.intact then n - (bit s.localFuel + s.source)
  else min (n - bit s.localFuel) (1 + (n - (bit s.localFuel + s.source)))

theorem reconstruction_common_necessary {M n : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (restored : aCount s + n ≤ aCount t) :
    requiredCommon n s ≤ s.fuel := by
  have total := growth_repair_support h restored
  cases hi : s.intact
  · simp only [requiredCommon, hi, Bool.false_eq_true, ↓reduceIte]
    by_cases hc : count .capture es = 0
    · have local := no_capture_support h restored hc
      exact Nat.le_trans (Nat.min_le_left _ _) (by omega)
    · have repair := capture_from_damage_requires_repair h hi (by omega)
      have common := trace_common_ledger h
      have costs := repairs_cost_common es
      have needed : 1 + (n - (bit s.localFuel + s.source)) ≤ s.fuel := by omega
      exact Nat.le_trans (Nat.min_le_right _ _) needed
  · simp only [requiredCommon, hi, ↓reduceIte]
    omega

theorem zero_common_is_permanent {M : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (zero : s.fuel = 0) : t.fuel = 0 := by
  have hh := trace_common_ledger h
  omega

theorem no_future_repair_from_zero_common {M : Nat} {s t : State} {es : List Event}
    (h : Trace M s es t) (zero : s.fuel = 0) : ¬ Enabled M t .repair := by
  have hh := zero_common_is_permanent h zero
  intro he
  have positive := he.2.2
  omega

def deficit : State := ⟨37,39,.active,true,false,1,216⟩
def localRestored : State := ⟨38,39,.active,true,false,1,215⟩
def bulkRestored : State := ⟨38,39,.active,true,false,0,216⟩
def afterFreshRepair : State := ⟨38,39,.active,true,false,0,215⟩

theorem local_reconstruction : Trace 78 deficit [.capture,.localCopyA] localRestored := by
  apply Trace.cons (u := ⟨37,39,.active,true,true,1,215⟩) (by decide)
  exact Trace.cons (by decide) (Trace.nil _)

theorem bulk_reconstruction : Trace 78 deficit [.bulkCopyA] bulkRestored := by
  exact Trace.cons (by decide) (Trace.nil _)

theorem same_reconstruction_same_total_support :
    aCount localRestored = aCount bulkRestored ∧
    hCount localRestored = hCount bulkRestored ∧
    localRestored.resident = bulkRestored.resident ∧
    localRestored.intact = bulkRestored.intact ∧
    localRestored.localFuel = bulkRestored.localFuel ∧
    energy localRestored = 216 ∧ energy bulkRestored = 216 := by decide

theorem local_route_allows_fresh_damage_repair :
    Trace 78 localRestored [.damage,.repair] afterFreshRepair := by
  apply Trace.cons (u := ⟨38,39,.active,false,false,1,215⟩) (by decide)
  exact Trace.cons (by decide) (Trace.nil _)

theorem bulk_route_blocks_repair_after_damage :
    Step 78 bulkRestored .damage (advance bulkRestored .damage) ∧
    ¬ Enabled 78 (advance bulkRestored .damage) .repair := by decide

theorem bulk_route_no_continuation_can_restore_repair {t : State} {es : List Event}
    (h : Trace 78 bulkRestored es t) : ¬ Enabled 78 t .repair :=
  no_future_repair_from_zero_common h rfl

end Generative.ReconstructionRequirement

#print axioms Generative.ReconstructionRequirement.step_a_growth
#print axioms Generative.ReconstructionRequirement.trace_a_growth
#print axioms Generative.ReconstructionRequirement.growth_repair_cost
#print axioms Generative.ReconstructionRequirement.growth_repair_trace_cost
#print axioms Generative.ReconstructionRequirement.growth_repair_support
#print axioms Generative.ReconstructionRequirement.step_source_balance
#print axioms Generative.ReconstructionRequirement.trace_source_balance
#print axioms Generative.ReconstructionRequirement.no_capture_support
#print axioms Generative.ReconstructionRequirement.step_intact_from_damage
#print axioms Generative.ReconstructionRequirement.capture_from_damage_requires_repair
#print axioms Generative.ReconstructionRequirement.repairs_cost_common
#print axioms Generative.ReconstructionRequirement.reconstruction_common_necessary
#print axioms Generative.ReconstructionRequirement.zero_common_is_permanent
#print axioms Generative.ReconstructionRequirement.no_future_repair_from_zero_common
#print axioms Generative.ReconstructionRequirement.local_reconstruction
#print axioms Generative.ReconstructionRequirement.bulk_reconstruction
#print axioms Generative.ReconstructionRequirement.same_reconstruction_same_total_support
#print axioms Generative.ReconstructionRequirement.local_route_allows_fresh_damage_repair
#print axioms Generative.ReconstructionRequirement.bulk_route_blocks_repair_after_damage
#print axioms Generative.ReconstructionRequirement.bulk_route_no_continuation_can_restore_repair
