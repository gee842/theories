import Std

/-!
# Paid damage-coupled response and material retention

This module checks the discrete seven-event law. It contains no stochastic
rates, numerical probability theorem, identified chemistry or learning claim.
Disabled kinetic channels can only remove paths from this relation.
-/

namespace EndogenousRetention

structure Config where
  n : Nat
  m : Nat
  b : Nat
deriving DecidableEq, Repr

/-- Reduced physical state: intact sites, regulators, usable fuel, incident fuel. -/
structure State where
  c : Nat
  g : Nat
  f : Nat
  e : Nat
deriving DecidableEq, Repr

inductive Event where
  | damage | fabricate | repair | capture | copy | wear | leak
deriving DecidableEq, Repr

def damaged (k : Config) (s : State) : Nat := k.n - s.c
def precursor (k : Config) (s : State) : Nat := k.m - s.g

def Valid (k : Config) (s : State) : Prop :=
  s.c ≤ k.n ∧ s.g ≤ k.m ∧ s.f ≤ k.b

def Enabled (k : Config) (s : State) : Event → Prop
  | .damage => 0 < s.c
  | .fabricate => s.c < k.n ∧ s.g < k.m ∧ 0 < s.f
  | .repair => 0 < s.g ∧ s.c < k.n ∧ 0 < s.f
  | .capture => 0 < s.c ∧ 0 < s.e ∧ s.f < k.b
  | .copy => 0 < s.g ∧ s.g < k.m ∧ 0 < s.f
  | .wear => 0 < s.g
  | .leak => 0 < s.f

def advance (s : State) : Event → State
  | .damage => { s with c := s.c - 1 }
  | .fabricate => { s with g := s.g + 1, f := s.f - 1 }
  | .repair => { s with c := s.c + 1, f := s.f - 1 }
  | .capture => { s with f := s.f + 1, e := s.e - 1 }
  | .copy => { s with g := s.g + 1, f := s.f - 1 }
  | .wear => { s with g := s.g - 1 }
  | .leak => { s with f := s.f - 1 }

def Step (k : Config) (s : State) (a : Event) (t : State) : Prop :=
  Valid k s ∧ Enabled k s a ∧ t = advance s a

instance (k : Config) (s : State) : Decidable (Valid k s) := by
  unfold Valid
  infer_instance

instance (k : Config) (s : State) (a : Event) : Decidable (Enabled k s a) := by
  cases a <;> unfold Enabled <;> infer_instance

instance (k : Config) (s : State) (a : Event) (t : State) :
    Decidable (Step k s a t) := by
  unfold Step
  infer_instance

/-- Every intermediate state is carried through the path. -/
inductive Trace (k : Config) : State → List Event → State → Prop where
  | nil (s : State) : Trace k s [] s
  | cons {s u t : State} {a : Event} {as : List Event} :
      Step k s a u → Trace k u as t → Trace k s (a :: as) t

def expenditure : Event → Nat
  | .fabricate | .repair | .copy | .leak => 1
  | .damage | .capture | .wear => 0

def copyIncrement : Event → Nat
  | .copy => 1
  | _ => 0

def spent : List Event → Nat
  | [] => 0
  | a :: as => expenditure a + spent as

def copies : List Event → Nat
  | [] => 0
  | a :: as => copyIncrement a + copies as

variable {k : Config} {s t : State} {a : Event} {as : List Event}

theorem step_valid (h : Step k s a t) : Valid k t := by
  rcases h with ⟨hv, he, rfl⟩
  cases a <;> simp_all [Valid, Enabled, advance] <;> omega

theorem trace_valid (hv : Valid k s) (h : Trace k s as t) : Valid k t := by
  induction h with
  | nil => exact hv
  | cons hs _ ih => exact ih (step_valid hs)

theorem material_ledgers (hv : Valid k s) :
    s.c + damaged k s = k.n ∧ s.g + precursor k s = k.m := by
  simp only [Valid] at hv
  simp only [damaged, precursor]
  omega

theorem trace_material_ledgers (hv : Valid k s) (h : Trace k s as t) :
    t.c + damaged k t = k.n ∧ t.g + precursor k t = k.m :=
  material_ledgers (trace_valid hv h)

theorem step_fuel_ledger (h : Step k s a t) :
    t.f + t.e + expenditure a = s.f + s.e := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, advance, expenditure] <;> omega

theorem trace_fuel_ledger (h : Trace k s as t) :
    t.f + t.e + spent as = s.f + s.e := by
  induction h with
  | nil => simp [spent]
  | cons hs _ ih =>
    have hh := step_fuel_ledger hs
    simp only [spent]
    omega

theorem copy_increment_le_expenditure (a : Event) :
    copyIncrement a ≤ expenditure a := by
  cases a <;> decide

theorem copies_le_spent (as : List Event) : copies as ≤ spent as := by
  induction as with
  | nil => simp [copies, spent]
  | cons a as ih =>
    have hh := copy_increment_le_expenditure a
    simp only [copies, spent]
    omega

theorem trace_copy_budget (h : Trace k s as t) : copies as ≤ s.f + s.e := by
  have hh := trace_fuel_ledger h
  have hc := copies_le_spent as
  omega

/-- A bootstrap trap, not a universal condition on every organization. -/
def BootstrapTrap (s : State) : Prop := s.c = 0 ∧ s.f + s.g ≤ 1

theorem bootstrap_step (ht : BootstrapTrap s) (h : Step k s a t) :
    BootstrapTrap t := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [BootstrapTrap, Enabled, advance] <;> omega

theorem bootstrap_trace (ht : BootstrapTrap s) (h : Trace k s as t) :
    BootstrapTrap t := by
  induction h with
  | nil => exact ht
  | cons hs _ ih => exact ih (bootstrap_step ht hs)

theorem bootstrap_under_two_fuel (hc : s.c = 0) (hg : s.g = 0)
    (hf : s.f < 2) (h : Trace k s as t) : t.c = 0 ∧ t.f + t.g ≤ 1 := by
  apply bootstrap_trace (s := s) (k := k) (as := as)
  · unfold BootstrapTrap
    omega
  · exact h

theorem bootstrap_forbids_productive_steps (ht : BootstrapTrap s)
    (h : Step k s a t) : a ≠ .repair ∧ a ≠ .capture ∧ a ≠ .copy := by
  rcases h with ⟨_, he, _⟩
  cases a <;> simp_all [BootstrapTrap, Enabled] <;> omega

/-- A ranking of this closed finite-stock law, not a universal measure of value. -/
def rank (s : State) : Nat := 4 * s.e + 2 * s.f + s.c + s.g

def rankDrop : Event → Nat
  | .capture | .leak => 2
  | _ => 1

theorem exact_step_rank_drop (h : Step k s a t) :
    rank t + rankDrop a = rank s := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, advance, rank, rankDrop] <;> omega

theorem every_step_decreases_rank (h : Step k s a t) : rank t < rank s := by
  rcases h with ⟨_, he, rfl⟩
  cases a <;> simp_all [Enabled, advance, rank] <;> omega

theorem trace_rank_bound (h : Trace k s as t) : as.length + rank t ≤ rank s := by
  induction h with
  | nil => simp
  | cons hs _ ih =>
    have hh := every_step_decreases_rank hs
    simp only [List.length_cons]
    omega

theorem trace_length_bound (h : Trace k s as t) : as.length ≤ rank s := by
  have hh := trace_rank_bound h
  omega

theorem no_nonempty_return (h : Trace k s as s) (hne : as ≠ []) : False := by
  have hh := trace_rank_bound h
  cases as with
  | nil => exact hne rfl
  | cons a as => simp only [List.length_cons] at hh; omega

theorem no_infinite_event_path (states : Nat → State) (events : Nat → Event)
    (h : ∀ n, Step k (states n) (events n) (states (n + 1))) : False := by
  have hh : ∀ n, n + rank (states n) ≤ rank (states 0) := by
    intro n
    induction n with
    | zero => omega
    | succ n ih =>
      have hr := every_step_decreases_rank (h n)
      omega
  have exceeded := hh (rank (states 0) + 1)
  omega

def Terminal (k : Config) (s : State) : Prop :=
  ∀ a t, ¬ Step k s a t

theorem terminal_iff (hv : Valid k s) :
    Terminal k s ↔ s.c = 0 ∧ s.g = 0 ∧ s.f = 0 := by
  constructor
  · intro ht
    have hc : s.c = 0 := by
      by_cases hn : s.c = 0
      · exact hn
      · exact False.elim (ht .damage (advance s .damage)
          ⟨hv, by simp only [Enabled]; omega, rfl⟩)
    have hg : s.g = 0 := by
      by_cases hn : s.g = 0
      · exact hn
      · exact False.elim (ht .wear (advance s .wear)
          ⟨hv, by simp only [Enabled]; omega, rfl⟩)
    have hf : s.f = 0 := by
      by_cases hn : s.f = 0
      · exact hn
      · exact False.elim (ht .leak (advance s .leak)
          ⟨hv, by simp only [Enabled]; omega, rfl⟩)
    exact ⟨hc, hg, hf⟩
  · rintro ⟨hc, hg, hf⟩ a t ⟨_, he, _⟩
    cases a <;> simp_all [Enabled]

def witnessConfig : Config := ⟨1, 3, 2⟩
def initial : State := ⟨0, 0, 2, 2⟩
def afterFormation : State := ⟨0, 1, 1, 2⟩
def afterRepair : State := ⟨1, 1, 0, 2⟩
def afterFirstCapture : State := ⟨1, 1, 1, 1⟩
def afterFirstCopy : State := ⟨1, 2, 0, 1⟩
def afterSecondCapture : State := ⟨1, 2, 1, 0⟩
def finalState : State := ⟨1, 3, 0, 0⟩
def witnessEvents : List Event := [.fabricate, .repair, .capture, .copy, .capture, .copy]

theorem witness_from_absence : Trace witnessConfig initial witnessEvents finalState := by
  apply Trace.cons (u := afterFormation) (by decide)
  apply Trace.cons (u := afterRepair) (by decide)
  apply Trace.cons (u := afterFirstCapture) (by decide)
  apply Trace.cons (u := afterFirstCopy) (by decide)
  apply Trace.cons (u := afterSecondCapture) (by decide)
  apply Trace.cons (u := finalState) (by decide)
  exact Trace.nil _

theorem witness_accounting :
    initial.g = 0 ∧ finalState.c = 1 ∧ finalState.g = 3 ∧
    copies witnessEvents = 2 ∧ spent witnessEvents = 4 ∧
    finalState.e = 0 ∧ finalState.f = 0 := by decide

theorem repair_restores_capture :
    ¬ Enabled witnessConfig afterFormation .capture ∧
    Enabled witnessConfig afterRepair .capture := by decide

theorem copying_requires_actual_capture :
    ¬ Enabled witnessConfig afterRepair .copy ∧
    Enabled witnessConfig afterFirstCapture .copy := by decide

#print axioms step_valid
#print axioms trace_valid
#print axioms material_ledgers
#print axioms trace_material_ledgers
#print axioms step_fuel_ledger
#print axioms trace_fuel_ledger
#print axioms copy_increment_le_expenditure
#print axioms copies_le_spent
#print axioms trace_copy_budget
#print axioms bootstrap_step
#print axioms bootstrap_trace
#print axioms bootstrap_under_two_fuel
#print axioms bootstrap_forbids_productive_steps
#print axioms exact_step_rank_drop
#print axioms every_step_decreases_rank
#print axioms trace_rank_bound
#print axioms trace_length_bound
#print axioms no_nonempty_return
#print axioms no_infinite_event_path
#print axioms terminal_iff
#print axioms witness_from_absence
#print axioms witness_accounting
#print axioms repair_restores_capture
#print axioms copying_requires_actual_capture

end EndogenousRetention
