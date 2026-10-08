import Std

/- A restricted identification audit, not a zero-premise ethical theorem.
One history carries a protection status and a secondary count. The two explicit
comparators test inferential sufficiency, not the entire relational ontology. -/
namespace PracticalPriorityIdentification

abbrev History := Bool × Nat

def LexLe (a b : History) : Prop :=
  (a.1 = false ∧ b.1 = true) ∨ (a.1 = b.1 ∧ a.2 ≤ b.2)

def score (weight : Nat) (a : History) : Nat :=
  (if a.1 then weight else 0) + a.2

def FiniteLe (weight : Nat) (a b : History) : Prop := score weight a ≤ score weight b

theorem lex_refl (a : History) : LexLe a a := Or.inr ⟨rfl, Nat.le_refl _⟩

theorem lex_trans {a b c : History} (hab : LexLe a b) (hbc : LexLe b c) : LexLe a c := by
  rcases a with ⟨p, x⟩
  rcases b with ⟨q, y⟩
  rcases c with ⟨r, z⟩
  cases p <;> cases q <;> cases r <;> simp_all [LexLe] <;> omega

theorem finite_trans (weight : Nat) {a b c : History}
    (hab : FiniteLe weight a b) (hbc : FiniteLe weight b c) : FiniteLe weight a c :=
  Nat.le_trans hab hbc

theorem finite_protection_positive (weight n : Nat) (positive : 0 < weight) :
    score weight (false, n) < score weight (true, n) := by
  simp [score]
  omega

theorem finite_secondary_positive (weight : Nat) (protection : Bool) (n : Nat) :
    score weight (protection, n) < score weight (protection, n + 1) := by
  simp [score]

/-- Every pairwise weak comparison agrees throughout the bounded domain. -/
theorem bounded_comparison_agreement (bound : Nat) (a b : History)
    (ha : a.2 ≤ bound) (hb : b.2 ≤ bound) :
    LexLe a b ↔ FiniteLe (bound + 1) a b := by
  rcases a with ⟨p, x⟩
  rcases b with ⟨q, y⟩
  cases p <;> cases q <;> simp_all [LexLe, FiniteLe, score] <;> omega

def secondaryBound : List History → Nat
  | [] => 0
  | h :: hs => max h.2 (secondaryBound hs)

theorem member_bounded {sample : List History} {h : History} (mem : h ∈ sample) :
    h.2 ≤ secondaryBound sample := by
  induction sample with
  | nil => simp at mem
  | cons x xs ih =>
    rcases List.mem_cons.mp mem with eq | tail
    · subst h
      exact Nat.le_max_left _ _
    · exact Nat.le_trans (ih tail) (Nat.le_max_right _ _)

theorem every_finite_sample_agrees (sample : List History) :
    ∀ a ∈ sample, ∀ b ∈ sample,
      (LexLe a b ↔ FiniteLe (secondaryBound sample + 1) a b) := by
  intro a ha b hb
  exact bounded_comparison_agreement _ _ _ (member_bounded ha) (member_bounded hb)

theorem outside_sample_reversal (sample : List History) :
    LexLe (false, secondaryBound sample + 2) (true, 0) ∧
    ¬ LexLe (true, 0) (false, secondaryBound sample + 2) ∧
    score (secondaryBound sample + 1) (true, 0) <
      score (secondaryBound sample + 1) (false, secondaryBound sample + 2) := by
  simp [LexLe, score]

theorem reversing_history_unobserved (sample : List History) :
    (false, secondaryBound sample + 2) ∉ sample := by
  intro h
  have bound := member_bounded h
  simp at bound
  omega

/-- A different finite weight can fit each finite sample; one fixed weight cannot
have lexical scope over every possible history in this represented family. -/
theorem no_fixed_finite_weight_is_lexical (weight : Nat) :
    ¬ (∀ a b : History, LexLe a b ↔ FiniteLe weight a b) := by
  intro same
  have h := (same (true, 0) (false, weight + 1)).mpr
    (show FiniteLe weight (true, 0) (false, weight + 1) by simp [FiniteLe, score])
  simp [LexLe] at h

theorem finite_agreement_without_global_identification (sample : List History) :
    ∃ weight : Nat, 0 < weight ∧
      (∀ a ∈ sample, ∀ b ∈ sample, LexLe a b ↔ FiniteLe weight a b) ∧
      ¬ (∀ a b : History, LexLe a b ↔ FiniteLe weight a b) :=
  ⟨secondaryBound sample + 1, by omega, every_finite_sample_agrees sample,
    no_fixed_finite_weight_is_lexical _⟩

/-- An exactly symmetric local history. Real asymmetry in undertaking or control
would invalidate the symmetry premise. -/
def SwapInvariant (assigned : Bool → Prop) : Prop :=
  ∀ a, assigned a ↔ assigned (!a)

def ExactlyOne (assigned : Bool → Prop) : Prop :=
  (assigned true ∧ ¬ assigned false) ∨ (assigned false ∧ ¬ assigned true)

theorem symmetric_assignment_not_unique {assigned : Bool → Prop}
    (same : SwapInvariant assigned) : ¬ ExactlyOne assigned := by
  intro h
  rcases h with h | h
  · exact h.2 ((same true).mp h.1)
  · exact h.2 ((same false).mp h.1)

theorem two_assignments_fit_one_task :
    ExactlyOne (fun a => a = true) ∧ ExactlyOne (fun a => a = false) := by
  constructor
  · exact Or.inl ⟨rfl, by decide⟩
  · exact Or.inr ⟨rfl, by decide⟩

end PracticalPriorityIdentification
