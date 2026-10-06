import GenerativeCore
import FormedSelection

/-!
Finite material recording under a supplied assembly and commitment law.
Only completed trials implement the capacity/source-backed teacher macro.
Partial trials keep escrow and the pending observation in their real state.
No probability, scheduler fairness, unbounded storage or calibration is derived.
-/

namespace RecordedEvidence

open FormedSelection (bit occupied)

inductive Pending where
  | idle | awaiting | latched (value : Bool)
deriving DecidableEq, Repr

def busy : Pending → Nat | .idle => 0 | _ => 1
def pendingWord : Pending → List Bool | .latched b => [b] | _ => []

structure State where
  plant : FormedSelection.State
  slots : Nat
  blank : Nat
  pending : Pending
  escrow : Nat
  records : List Bool
deriving DecidableEq, Repr

def handoff (s : FormedSelection.State) : State := ⟨s, 0, 0, .idle, 0, []⟩
def materialUsed (s : State) : Nat := FormedSelection.population s.plant + 2 * s.slots
def energy (s : State) : Nat := FormedSelection.energy s.plant + s.escrow
def observed (s : State) : List Bool := s.records ++ pendingWord s.pending
def Valid (material : Nat) (s : State) : Prop :=
  s.slots = s.blank + busy s.pending + s.records.length ∧
  s.escrow = busy s.pending ∧ materialUsed s ≤ material

inductive Event where
  | assemble | reserve | observe (value : Bool) | commit (value : Bool)
deriving DecidableEq, Repr

def CanAdmit (s : State) : Prop :=
  s.pending = .idle ∧ 0 < s.blank ∧ 2 ≤ s.plant.fuel ∧ 2 ≤ s.plant.source

def Enabled (s : State) : Event → Prop
  | .assemble => s.pending = .idle ∧ 0 < s.plant.aFree ∧
      0 < s.plant.hFree ∧ 0 < s.plant.fuel
  | .reserve => CanAdmit s
  | .observe _ => s.pending = .awaiting ∧ 2 ≤ s.plant.source
  | .commit b => s.pending = .latched b

def receipt (b : Bool) : Nat := if b then 0 else 2

def advance (s : State) : Event → State
  | .assemble => { s with
      plant := { s.plant with aFree := s.plant.aFree - 1, hFree := s.plant.hFree - 1, fuel := s.plant.fuel - 1 },
      slots := s.slots + 1, blank := s.blank + 1 }
  | .reserve => { s with
      plant := { s.plant with fuel := s.plant.fuel - 2 },
      blank := s.blank - 1, pending := .awaiting, escrow := 1 }
  | .observe b => { s with
      plant := { s.plant with fuel := s.plant.fuel + receipt b, source := s.plant.source - receipt b }, pending := .latched b }
  | .commit b => { s with pending := .idle, escrow := 0, records := s.records ++ [b] }

def Step (material : Nat) (s : State) (a : Event) (t : State) : Prop :=
  Valid material s ∧ Enabled s a ∧ t = advance s a
def process (material : Nat) : Generative.Process State Event := ⟨Step material⟩
def spending : Event → Nat | .observe _ => 0 | _ => 1
def assemblyCount : Event → Nat | .assemble => 1 | _ => 0
def emission : Event → List Bool | .observe b => [b] | _ => []
def tally (weight : Event → Nat) : List Event → Nat
  | [] => 0 | a :: as => weight a + tally weight as
def word : List Event → List Bool
  | [] => [] | a :: as => emission a ++ word as
def ones : List Bool → Nat
  | [] => 0 | b :: bs => bit b + ones bs

instance (material : Nat) (s : State) : Decidable (Valid material s) := by
  unfold Valid; infer_instance
instance (s : State) : Decidable (CanAdmit s) := by
  unfold CanAdmit; infer_instance
instance (s : State) (a : Event) : Decidable (Enabled s a) := by
  cases a <;> unfold Enabled <;> infer_instance
instance (material : Nat) (s : State) (a : Event) (t : State) :
    Decidable (Step material s a t) := by
  unfold Step; infer_instance

variable {material : Nat} {s m t : State} {a : Event} {as bs : List Event}

theorem handoff_valid (h : FormedSelection.Valid material s₀) :
    Valid material (handoff s₀) := by
  simpa [Valid, handoff, busy, materialUsed, FormedSelection.Valid] using h

theorem handoff_accounts (s₀ : FormedSelection.State) :
    energy (handoff s₀) = FormedSelection.energy s₀ ∧
    materialUsed (handoff s₀) = FormedSelection.population s₀ := by
  simp [handoff, energy, materialUsed]

theorem step_valid (h : Step material s a t) : Valid material t := by
  rcases h with ⟨hv, he, rfl⟩
  cases a <;> cases hp : s.pending <;>
    simp_all [Valid, Enabled, CanAdmit, advance, materialUsed,
      FormedSelection.population, busy, List.length_append] <;> omega

theorem step_material (h : Step material s a t) : materialUsed t = materialUsed s := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, CanAdmit, advance, materialUsed,
    FormedSelection.population] <;> omega

theorem step_energy (h : Step material s a t) : energy t + spending a = energy s := by
  rcases h with ⟨hv, he, rfl⟩
  cases a with
  | observe b => cases b <;>
      simp_all [Valid, Enabled, advance, energy, spending,
        FormedSelection.energy, receipt, busy] <;> omega
  | assemble =>
      simp_all [Valid, Enabled, advance, energy, spending, FormedSelection.energy, busy] <;> omega
  | reserve =>
      simp_all [Valid, Enabled, CanAdmit, advance, energy, spending,
        FormedSelection.energy, busy] <;> omega
  | commit b =>
      simp_all [Valid, Enabled, advance, energy, spending, FormedSelection.energy, busy] <;> omega

theorem step_observation_word (h : Step material s a t) :
    observed t = observed s ++ emission a := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, CanAdmit, advance, observed, pendingWord, emission]

theorem step_slots (h : Step material s a t) : t.slots = s.slots + assemblyCount a := by
  rcases h with ⟨_, _, rfl⟩
  cases a <;> rfl

theorem trace_valid (hv : Valid material s)
    (h : Generative.Trace (process material) s as t) : Valid material t := by
  induction h with
  | nil => exact hv
  | cons hs _ ih => exact ih (step_valid hs)

theorem trace_material (h : Generative.Trace (process material) s as t) :
    materialUsed t = materialUsed s := by
  induction h with
  | nil => rfl
  | cons hs _ ih => exact ih.trans (step_material hs)

theorem trace_energy (h : Generative.Trace (process material) s as t) :
    energy t + tally spending as = energy s := by
  induction h with
  | nil => simp [tally]
  | cons hs _ ih =>
      have he := step_energy hs
      simp only [tally]
      omega

theorem trace_observation_word (h : Generative.Trace (process material) s as t) :
    observed t = observed s ++ word as := by
  induction h with
  | nil => simp [word]
  | cons hs _ ih =>
      rw [ih, step_observation_word hs]
      simp [word, List.append_assoc]

theorem trace_slots (h : Generative.Trace (process material) s as t) :
    t.slots = s.slots + tally assemblyCount as := by
  induction h with
  | nil => simp [tally]
  | cons hs _ ih =>
      have he := step_slots hs
      simp only [tally]
      omega

theorem complete_record (h : Generative.Trace (process material) s as t)
    (start : s.pending = .idle) (finish : t.pending = .idle) :
    t.records = s.records ++ word as := by
  simpa [observed, pendingWord, start, finish] using trace_observation_word h

theorem handoff_complete_record
    (h : Generative.Trace (process material) (handoff s₀) as t)
    (finish : t.pending = .idle) : t.records = word as := by
  simpa [handoff] using complete_record h rfl finish

theorem record_capacity (hv : Valid material s) : s.records.length ≤ s.slots := by
  simp only [Valid] at hv
  omega

theorem material_capacity (hv : Valid material s) : 2 * s.records.length ≤ material := by
  have hc := record_capacity hv
  simp only [Valid, materialUsed] at hv
  omega

theorem full_slot_blocks_admission (h : s.blank = 0) : ¬ CanAdmit s := by
  simp [CanAdmit, h]

theorem source_guard (h : s.plant.source < 2) : ¬ CanAdmit s := by
  simp only [CanAdmit]
  omega

theorem busy_blocks_admission (h : s.pending ≠ .idle) : ¬ CanAdmit s := by
  simp [CanAdmit, h]

theorem preallocated_writer (ha : CanAdmit s) (b : Bool) :
    Enabled (advance s .reserve) (.observe b) ∧
    Enabled (advance (advance s .reserve) (.observe b)) (.commit b) ∧
    (advance s .reserve).escrow = 1 := by
  rcases ha with ⟨_, _, _, hs⟩
  simp [Enabled, advance, hs]

def completedUpdate (s : State) (b : Bool) : State :=
  { s with
    plant := { s.plant with fuel := s.plant.fuel - 2 + receipt b, source := s.plant.source - receipt b },
    blank := s.blank - 1, pending := .idle, escrow := 0, records := s.records ++ [b] }

theorem macro_update (s : State) (b : Bool) :
    advance (advance (advance s .reserve) (.observe b)) (.commit b) =
      completedUpdate s b := by rfl

theorem completed_trial (hv : Valid material s) (ha : CanAdmit s) (b : Bool) :
    Generative.Trace (process material) s [.reserve, .observe b, .commit b]
      (completedUpdate s b) := by
  have h₁ : Step material s .reserve (advance s .reserve) := ⟨hv, ha, rfl⟩
  have hw := preallocated_writer ha b
  have h₂ : Step material (advance s .reserve) (.observe b)
      (advance (advance s .reserve) (.observe b)) := ⟨step_valid h₁, hw.1, rfl⟩
  have h₃ : Step material (advance (advance s .reserve) (.observe b)) (.commit b)
      (completedUpdate s b) := ⟨step_valid h₂, hw.2.1, rfl⟩
  exact .cons h₁ (.cons h₂ (.cons h₃ (.nil _)))

theorem trace_run (h : Generative.Trace (process material) s as t) :
    t = as.foldl advance s := by
  induction h with
  | nil => rfl
  | cons hs _ ih =>
      rcases hs with ⟨_, _, rfl⟩
      exact ih

/-- Exactness is for a capacity/source-backed macro retaining the physical state. -/
theorem completed_trial_iff (b : Bool) :
    Generative.Trace (process material) s [.reserve, .observe b, .commit b] t ↔
      Valid material s ∧ CanAdmit s ∧ t = completedUpdate s b := by
  constructor
  · intro h
    obtain ⟨u, hs, _⟩ := Generative.trace_cons_iff.mp h
    refine ⟨hs.1, hs.2.1, ?_⟩
    simpa only [List.foldl_cons, List.foldl_nil, macro_update] using trace_run h
  · rintro ⟨hv, ha, rfl⟩
    exact completed_trial hv ha b

theorem macro_teacher_stocks (ha : CanAdmit s) (b : Bool) :
    (completedUpdate s b).plant.fuel + 2 = s.plant.fuel + receipt b ∧
    (completedUpdate s b).plant.source + receipt b = s.plant.source := by
  cases b <;> simp_all [CanAdmit, completedUpdate, receipt] <;> omega

theorem ones_append (xs ys : List Bool) : ones (xs ++ ys) = ones xs + ones ys := by
  induction xs with
  | nil => simp [ones]
  | cons x xs ih => simp [ones, ih, Nat.add_assoc]

theorem macro_counts (s : State) (b : Bool) :
    (completedUpdate s b).records.length = s.records.length + 1 ∧
    ones (completedUpdate s b).records = ones s.records + bit b := by
  simp [completedUpdate, ones_append, ones]

theorem composed_energy
    (hp : FormedSelection.Trace material s₀ ps s₁)
    (hr : Generative.Trace (process material) (handoff s₁) as t) :
    energy t + tally spending as + FormedSelection.tally FormedSelection.expenditure ps =
      FormedSelection.energy s₀ := by
  have he := trace_energy hr
  have hf := FormedSelection.trace_energy_ledger hp
  rw [(handoff_accounts s₁).1] at he
  omega

def initialPlant : FormedSelection.State := ⟨0, 0, .empty, false, false, 12, 18⟩
def preparedPlant : FormedSelection.State := ⟨2, 2, .active, true, false, 7, 16⟩
def preparation : List FormedSelection.Event :=
  [.formH, .formH, .formA, .associateA, .repair,
   .capture, .localCopyA, .capture, .localCopyA]

theorem actual_preparation : FormedSelection.Trace 5 initialPlant preparation preparedPlant := by
  unfold preparation
  apply FormedSelection.Trace.cons (u := FormedSelection.advance initialPlant .formH) (by decide)
  apply FormedSelection.Trace.cons (u := FormedSelection.advance
    (FormedSelection.advance initialPlant .formH) .formH) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .empty, false, false, 9, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, false, false, 8, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, true, false, 7, 18⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨0, 2, .active, true, true, 7, 17⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .active, true, false, 7, 17⟩) (by decide)
  apply FormedSelection.Trace.cons (u := ⟨1, 2, .active, true, true, 7, 16⟩) (by decide)
  apply FormedSelection.Trace.cons (u := preparedPlant) (by decide)
  exact .nil _

def installed : State :=
  ⟨⟨0, 0, .active, true, false, 5, 16⟩, 2, 2, .idle, 0, []⟩

theorem actual_assembly :
    Generative.Trace (process 5) (handoff preparedPlant) [.assemble, .assemble] installed := by
  apply Generative.Trace.cons (m := advance (handoff preparedPlant) .assemble)
    (by change Step 5 _ _ _; decide)
  apply Generative.Trace.cons (m := installed) (by change Step 5 _ _ _; decide)
  exact .nil _

def exhausted := completedUpdate (completedUpdate installed false) true

theorem actual_two_records :
    Generative.Trace (process 5) installed
      [.reserve, .observe false, .commit false, .reserve, .observe true, .commit true] exhausted := by
  have h₀ := completed_trial (material := 5) (s := installed) (by decide) (by decide) false
  have h₁ := completed_trial (material := 5) (s := completedUpdate installed false)
    (by decide) (by decide) true
  exact Generative.trace_append_iff.mpr ⟨_, h₀, h₁⟩

theorem fuel_cannot_replace_capacity :
    exhausted.records = [false, true] ∧ exhausted.plant.fuel = 3 ∧
    exhausted.plant.source = 14 ∧ exhausted.blank = 0 ∧ ¬ CanAdmit exhausted := by
  decide

theorem full_witness_accounts :
    energy exhausted + 13 = FormedSelection.energy initialPlant ∧
    materialUsed exhausted = 5 ∧ Valid 5 exhausted := by decide

#print axioms handoff_valid
#print axioms handoff_accounts
#print axioms step_valid
#print axioms step_material
#print axioms step_energy
#print axioms step_observation_word
#print axioms step_slots
#print axioms trace_valid
#print axioms trace_material
#print axioms trace_energy
#print axioms trace_observation_word
#print axioms trace_slots
#print axioms complete_record
#print axioms handoff_complete_record
#print axioms record_capacity
#print axioms material_capacity
#print axioms full_slot_blocks_admission
#print axioms source_guard
#print axioms busy_blocks_admission
#print axioms preallocated_writer
#print axioms macro_update
#print axioms completed_trial
#print axioms trace_run
#print axioms completed_trial_iff
#print axioms macro_teacher_stocks
#print axioms ones_append
#print axioms macro_counts
#print axioms composed_energy
#print axioms actual_preparation
#print axioms actual_assembly
#print axioms actual_two_records
#print axioms fuel_cannot_replace_capacity
#print axioms full_witness_accounts

end RecordedEvidence
