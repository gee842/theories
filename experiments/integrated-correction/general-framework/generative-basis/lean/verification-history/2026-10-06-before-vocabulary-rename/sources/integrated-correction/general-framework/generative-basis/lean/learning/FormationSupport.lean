import ResourceContinuation
import FormationRoot

/-!
# Actual support accounts for paid formation

These are accounts of the existing sixteen-event law, with all intermediate
states preserved. Capture transfers one unit from the finite source into the
local store. It credits usable support but does not credit the closed account.
Event tallies describe this law; they are not an endogenous reward signal.
-/

namespace FormedSelection.Support

open Generative.Conditional

def usable (s : State) : Nat := s.fuel + bit s.localFuel
def captureAmount (a : Event) : Nat := eventIndicator .capture a
def localExpenditure : Event → Nat
  | .localCopyA | .localCopyH | .leakLocal => 1
  | _ => 0

def eventQuantity (weight : Event → Nat) : State → Event → State → Nat :=
  fun _ a _ => weight a

variable {material : Nat} {s m t : State} {a : Event} {as bs : List Event}

theorem step_source_ledger (h : Step material s a t) :
    t.source + captureAmount a = s.source := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, advance, captureAmount, eventIndicator] <;> omega

theorem step_local_ledger (h : Step material s a t) :
    bit t.localFuel + localExpenditure a = bit s.localFuel + captureAmount a := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> cases hl : s.localFuel <;>
    simp_all [Enabled, advance, bit, localExpenditure, captureAmount, eventIndicator]

theorem step_usable_ledger (h : Step material s a t) :
    usable t + expenditure a = usable s + captureAmount a := by
  have he := step_energy_ledger h
  have hs := step_source_ledger h
  simp only [usable, energy] at *
  omega

theorem usable_account (material : Nat) :
    AccountLaw (rootProcess material) usable
      (eventQuantity expenditure) (eventQuantity captureAmount) := by
  intro s a t h
  have he := step_usable_ledger h
  simp only [eventQuantity]
  omega

theorem local_account (material : Nat) :
    AccountLaw (rootProcess material) (fun s => bit s.localFuel)
      (eventQuantity localExpenditure) (eventQuantity captureAmount) := by
  intro s a t h
  have he := step_local_ledger h
  simp only [eventQuantity]
  omega

theorem source_account (material : Nat) :
    AccountLaw (rootProcess material) State.source
      (eventQuantity captureAmount) (eventQuantity (fun _ => 0)) := by
  intro s a t h
  have he := step_source_ledger h
  simp only [eventQuantity]
  omega

theorem closed_account (material : Nat) :
    AccountLaw (rootProcess material) energy
      (eventQuantity expenditure) (eventQuantity (fun _ => 0)) := by
  intro s a t h
  have he := step_energy_ledger h
  simp only [eventQuantity]
  omega

/-- Event-only weights are justified by this concrete law, while the root
    history still keeps each actual resource-bearing intermediate state. -/
theorem root_trace_account (demand credit : Event → Nat)
    (h : Generative.Trace (rootProcess material) s as t) :
    SupportTrace (rootProcess material) (eventQuantity demand) (eventQuantity credit)
      s as t (tally demand as) (tally credit as)
        (tally (fun a => credited (credit a)) as) := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih => exact .cons hs ih

theorem root_account_bound (reserve : State → Nat) (demand credit : Event → Nat)
    (law : AccountLaw (rootProcess material) reserve
      (eventQuantity demand) (eventQuantity credit))
    (h : Generative.Trace (rootProcess material) s as t) :
    tally demand as + reserve t ≤ reserve s + tally credit as :=
  support_trace_balance reserve law (root_trace_account demand credit h)

theorem tally_zero (as : List Event) : tally (fun _ => 0) as = 0 := by
  induction as with
  | nil => rfl
  | cons a as ih => simp [tally, ih]

theorem root_usable_bound (h : Generative.Trace (rootProcess material) s as t) :
    tally expenditure as + usable t ≤ usable s + tally captureAmount as :=
  root_account_bound usable expenditure captureAmount (usable_account material) h

theorem root_local_bound (h : Generative.Trace (rootProcess material) s as t) :
    tally localExpenditure as + bit t.localFuel ≤
      bit s.localFuel + tally captureAmount as :=
  root_account_bound (fun s => bit s.localFuel) localExpenditure captureAmount
    (local_account material) h

theorem root_source_bound (h : Generative.Trace (rootProcess material) s as t) :
    tally captureAmount as + t.source ≤ s.source := by
  simpa only [tally_zero, Nat.add_zero] using
    root_account_bound State.source captureAmount (fun _ => 0) (source_account material) h

theorem root_closed_bound (h : Generative.Trace (rootProcess material) s as t) :
    tally expenditure as + energy t ≤ energy s := by
  simpa only [tally_zero, Nat.add_zero] using
    root_account_bound energy expenditure (fun _ => 0) (closed_account material) h

theorem root_local_source_bound (h : Generative.Trace (rootProcess material) s as t) :
    tally localExpenditure as + bit t.localFuel + t.source ≤
      bit s.localFuel + s.source := by
  have hl := root_local_bound h
  have hs := root_source_bound h
  omega

/-- A cycle must return the finite source and all energy stores too. -/
theorem closed_cycle_has_no_expenditure
    (h : Generative.Trace (rootProcess material) s as s) : tally expenditure as = 0 := by
  have hb := root_closed_bound h
  omega

theorem closed_cycle_has_no_capture
    (h : Generative.Trace (rootProcess material) s as s) : tally captureAmount as = 0 := by
  have hb := root_source_bound h
  omega

theorem root_local_copy_bound
    (h : Generative.Trace (rootProcess material) s as t) :
    tally (eventIndicator .localCopyA) as + tally (eventIndicator .localCopyH) as ≤
      bit s.localFuel + s.source := by
  have he : ∀ a : Event,
      eventIndicator .localCopyA a + eventIndicator .localCopyH a ≤ localExpenditure a := by
    intro a
    cases a <;> decide
  have ht : tally (eventIndicator .localCopyA) as + tally (eventIndicator .localCopyH) as ≤
      tally localExpenditure as := by
    clear h
    induction as with
    | nil => simp [tally]
    | cons a as ih =>
      have hp := he a
      simp only [tally]
      omega
  have hb := root_local_source_bound h
  omega

theorem capture_absent_tally (h : Event.capture ∉ as) : tally captureAmount as = 0 := by
  induction as with
  | nil => rfl
  | cons a as ih =>
    simp only [List.mem_cons, not_or] at h
    simp [tally, captureAmount, eventIndicator, Ne.symm h.1, ih h.2]

/-- With no initially stored local fuel, actual local expenditure needs a
    capture event in the very same history. Common fuel cannot bypass this. -/
theorem local_expenditure_requires_capture
    (empty : s.localFuel = false) (h : Generative.Trace (rootProcess material) s as t)
    (used : 0 < tally localExpenditure as) : Event.capture ∈ as := by
  by_cases hc : Event.capture ∈ as
  · exact hc
  · have hb := root_local_bound h
    have hz := capture_absent_tally hc
    simp only [empty, bit, Nat.zero_add, hz] at hb
    omega

/-- A continuation inherits the actual successor's remaining stocks. It gets
    neither the original reserve nor a replenished source at the handoff. -/
theorem root_prefix_continuation_bound
    (h : Generative.Trace (rootProcess material) s (as ++ bs) t) :
    ∃ m, Generative.Trace (rootProcess material) s as m ∧
      Generative.Trace (rootProcess material) m bs t ∧
      tally expenditure bs + energy t ≤ usable m + m.source ∧
      tally captureAmount bs + t.source ≤ m.source := by
  obtain ⟨m, ha, hb⟩ := Generative.trace_append_iff.mp h
  refine ⟨m, ha, hb, ?_, root_source_bound hb⟩
  have hc := root_closed_bound hb
  simp only [energy, usable] at *
  omega

/-- The existing paid formation witness saturates its usable account. -/
theorem paid_witness_account :
    SupportTrace (rootProcess 3) (eventQuantity expenditure) (eventQuantity captureAmount)
      initial witnessEvents copied 5 1 1 := by
  simpa only [witnessEvents, tally, expenditure, captureAmount, eventIndicator,
    credited, Event.noConfusion, ↓reduceIte, Nat.reduceAdd] using
      root_trace_account expenditure captureAmount root_formation_to_copy

theorem paid_witness_saturates :
    usable initial = 4 ∧ initial.source = 1 ∧ usable copied = 0 ∧ copied.source = 0 ∧
      tally expenditure witnessEvents = usable initial + tally captureAmount witnessEvents := by
  decide

def witnessPrefix : List Event := [.formH, .formA, .associateA, .repair]
def witnessTail : List Event := [.capture, .localCopyA]

/-- Actual repair consumes the initial common fuel; only one source unit is
    available for the succeeding capture/copy segment. -/
theorem paid_witness_handoff :
    Generative.Trace (rootProcess 3) initial witnessPrefix repaired ∧
      Generative.Trace (rootProcess 3) repaired witnessTail copied ∧
      usable repaired = 0 ∧ repaired.source = 1 ∧
      tally expenditure witnessTail = 1 := by
  constructor
  · apply Generative.Trace.cons (m := formedH) (by change Step 3 _ _ _; decide)
    apply Generative.Trace.cons (m := formed) (by change Step 3 _ _ _; decide)
    apply Generative.Trace.cons (m := associated) (by change Step 3 _ _ _; decide)
    apply Generative.Trace.cons (m := repaired) (by change Step 3 _ _ _; decide)
    exact .nil _
  · constructor
    · apply Generative.Trace.cons (m := captured) (by change Step 3 _ _ _; decide)
      apply Generative.Trace.cons (m := copied) (by change Step 3 _ _ _; decide)
      exact .nil _
    · decide

theorem copied_cannot_pay_more
    (h : Generative.Trace (rootProcess 3) copied as t) :
    tally expenditure as = 0 ∧ tally captureAmount as = 0 := by
  have hc := root_closed_bound h
  have hs := root_source_bound h
  have he : energy copied = 0 := by decide
  have hz : copied.source = 0 := by decide
  constructor <;> omega

#print axioms step_source_ledger
#print axioms step_local_ledger
#print axioms step_usable_ledger
#print axioms usable_account
#print axioms local_account
#print axioms source_account
#print axioms closed_account
#print axioms root_trace_account
#print axioms root_account_bound
#print axioms tally_zero
#print axioms root_usable_bound
#print axioms root_local_bound
#print axioms root_source_bound
#print axioms root_closed_bound
#print axioms root_local_source_bound
#print axioms closed_cycle_has_no_expenditure
#print axioms closed_cycle_has_no_capture
#print axioms root_local_copy_bound
#print axioms capture_absent_tally
#print axioms local_expenditure_requires_capture
#print axioms root_prefix_continuation_bound
#print axioms paid_witness_account
#print axioms paid_witness_saturates
#print axioms paid_witness_handoff
#print axioms copied_cannot_pay_more

end FormedSelection.Support
