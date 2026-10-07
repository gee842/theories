import CompletionRole

/-! Finite-subset completion and the hidden-budget obstruction.
The finite subsets are extensional predicates with a finite-list witness. No
enumeration of all external subsets or effective construction is asserted.
-/
namespace CompletionExamples
open CompletionWarrant
universe u

structure FinitePart (α : Type u) where
  mem : α → Prop
  finite : ∃ l : List α, ∀ a, mem a ↔ a ∈ l

theorem FinitePart.ext {α : Type u} {A B : FinitePart α}
    (h : ∀ a, A.mem a ↔ B.mem a) : A = B := by
  cases A with
  | mk am af =>
    cases B with
    | mk bm bf =>
      have he : am = bm := funext (fun a => propext (h a))
      cases he
      rfl

def finiteOrder (α : Type u) : Poset (FinitePart α) where
  le A B := ∀ a, A.mem a → B.mem a
  refl _ _ h := h
  trans h k _ ha := k _ (h _ ha)
  antisymm h k := FinitePart.ext (fun a => ⟨h a, k a⟩)

def emptyPart (α : Type u) : FinitePart α where
  mem _ := False
  finite := ⟨[], by simp⟩

def singletonPart {α : Type u} (a : α) : FinitePart α where
  mem b := b = a
  finite := ⟨[a], by simp⟩

def unionPart {α : Type u} (A B : FinitePart α) : FinitePart α where
  mem a := A.mem a ∨ B.mem a
  finite := by
    obtain ⟨l, hl⟩ := A.finite
    obtain ⟨k, hk⟩ := B.finite
    exact ⟨l ++ k, fun a => by simp [hl a, hk a]⟩

def partsOf {α : Type u} (S : α → Prop) : Ideal (finiteOrder α) where
  mem A := ∀ a, A.mem a → S a
  nonempty := ⟨emptyPart α, fun _ h => False.elim h⟩
  lower h k a ha := k a (h a ha)
  directed hA hB := ⟨unionPart _ _,
    (fun a h => h.elim (hA a) (hB a)),
    (fun _ h => Or.inl h), (fun _ h => Or.inr h)⟩

def unionContents {α : Type u} (I : Ideal (finiteOrder α)) : α → Prop :=
  fun a => ∃ A, I.mem A ∧ A.mem a

theorem union_partsOf {α : Type u} (S : α → Prop) (a : α) :
    unionContents (partsOf S) a ↔ S a := by
  constructor
  · rintro ⟨A, hA, ha⟩
    exact hA a ha
  · intro ha
    exact ⟨singletonPart a, (fun b hb => hb ▸ ha), rfl⟩

theorem finite_cover {α : Type u} (I : Ideal (finiteOrder α)) (l : List α)
    (h : ∀ a, a ∈ l → unionContents I a) :
    ∃ A, I.mem A ∧ ∀ a, a ∈ l → A.mem a := by
  induction l with
  | nil =>
    obtain ⟨A, hA⟩ := I.nonempty
    exact ⟨A, hA, by simp⟩
  | cons a l ih =>
    obtain ⟨A, hA, ha⟩ := h a (by simp)
    obtain ⟨B, hB, hb⟩ := ih (fun b hbl => h b (by simp [hbl]))
    obtain ⟨C, hC, hac, hbc⟩ := I.directed hA hB
    refine ⟨C, hC, ?_⟩
    intro b hbl
    rcases List.mem_cons.mp hbl with rfl | hbl
    · exact hac b ha
    · exact hbc b (hb b hbl)

theorem partsOf_union {α : Type u} (I : Ideal (finiteOrder α)) :
    partsOf (unionContents I) = I := by
  apply Ideal.ext
  intro A
  constructor
  · intro hA
    obtain ⟨l, hl⟩ := A.finite
    obtain ⟨B, hB, hb⟩ := finite_cover I l (fun a ha => hA a ((hl a).mpr ha))
    exact I.lower (fun a ha => hb a ((hl a).mp ha)) hB
  · intro hA a ha
    exact ⟨A, hA, ha⟩

theorem union_order_iff {α : Type u} (I J : Ideal (finiteOrder α)) :
    Ideal.LE I J ↔ ∀ a, unionContents I a → unionContents J a := by
  constructor
  · rintro h a ⟨A, hA, ha⟩
    exact ⟨A, h A hA, ha⟩
  · intro h A hA
    have hp : (partsOf (unionContents J)).mem A :=
      fun a ha => h a ⟨A, hA, ha⟩
    rwa [partsOf_union J] at hp

theorem parts_order_iff {α : Type u} (S T : α → Prop) :
    Ideal.LE (partsOf S) (partsOf T) ↔ ∀ a, S a → T a := by
  constructor
  · intro h a ha
    exact h (singletonPart a) (fun b hb => hb ▸ ha) a rfl
  · intro h A hA a ha
    exact h a (hA a ha)

/- A hidden finite budget is one enduring relation within a history. Projecting
it away exchanges the quantifiers below; it does not create a concrete run. -/
def BudgetRun (budget ticks : Nat) : Prop := ticks ≤ budget

theorem every_finite_budget_run : ∀ ticks, ∃ budget, BudgetRun budget ticks :=
  fun ticks => ⟨ticks, Nat.le_refl ticks⟩

theorem no_budget_runs_forever : ¬ ∃ budget, ∀ ticks, BudgetRun budget ticks := by
  rintro ⟨budget, h⟩
  have hf := h (budget + 1)
  unfold BudgetRun at hf
  omega

def Tick (budget before after : Nat) : Prop := before < budget ∧ after = before + 1

theorem tick_history_identity (budget : Nat) (states : Nat → Nat)
    (initial : states 0 = 0) (steps : ∀ n, Tick budget (states n) (states (n+1))) :
    ∀ n, states n = n := by
  intro n
  induction n with
  | zero => exact initial
  | succ n ih => simpa [ih] using (steps n).2

theorem no_infinite_concrete_tick_run (budget : Nat) :
    ¬ ∃ states : Nat → Nat, states 0 = 0 ∧
      ∀ n, Tick budget (states n) (states (n+1)) := by
  rintro ⟨states, initial, steps⟩
  have h := (steps budget).1
  rw [tick_history_identity budget states initial steps budget] at h
  exact Nat.lt_irrefl budget h

theorem finite_concrete_tick_run (length : Nat) :
    ∃ states : Nat → Nat, states 0 = 0 ∧
      ∀ n, n < length → Tick length (states n) (states (n+1)) := by
  exact ⟨id, rfl, fun _ hn => ⟨hn, rfl⟩⟩

theorem ideal_finite_upper {α : Type u} (P : Poset α) (I : Ideal P) (l : List α)
    (hl : ∀ a, a ∈ l → I.mem a) :
    ∃ r, I.mem r ∧ ∀ a, a ∈ l → P.le a r := by
  induction l with
  | nil =>
    obtain ⟨r, hr⟩ := I.nonempty
    exact ⟨r, hr, by simp⟩
  | cons a l ih =>
    obtain ⟨r, hr, hu⟩ := ih (fun b hb => hl b (by simp [hb]))
    obtain ⟨s, hs, has, hrs⟩ := I.directed (hl a (by simp)) hr
    refine ⟨s, hs, ?_⟩
    intro b hb
    rcases List.mem_cons.mp hb with rfl | hb
    · exact has
    · exact P.trans (hu b hb) hrs

/-- Existing finite least upper bounds are preserved by principal embedding. -/
theorem finite_lub_preserved {α : Type u} (P : Poset α) (l : List α) (p : α)
    (upper : ∀ a, a ∈ l → P.le a p)
    (least : ∀ r, (∀ a, a ∈ l → P.le a r) → P.le p r) :
    (∀ a, a ∈ l → Ideal.LE (principal P a) (principal P p)) ∧
    ∀ I : Ideal P, (∀ a, a ∈ l → Ideal.LE (principal P a) I) →
      Ideal.LE (principal P p) I := by
  refine ⟨fun a ha => principal_mono P (upper a ha), ?_⟩
  intro I hI
  obtain ⟨r, hr, hu⟩ := ideal_finite_upper P I l
    (fun a ha => (principal_le_iff P a I).mp (hI a ha))
  exact (principal_le_iff P p I).mpr (I.lower (least r hu) hr)

noncomputable def boundedPart (S : Nat → Prop) (n : Nat) : FinitePart Nat := by
  classical
  exact ⟨fun a => S a ∧ a < n, List.filter (fun a => decide (S a)) (List.range n),
    fun a => by simp [and_comm]⟩

theorem boundedPart_increasing (S : Nat → Prop) {n m : Nat} (hnm : n ≤ m) :
    (finiteOrder Nat).le (boundedPart S n) (boundedPart S m) := by
  intro a ha
  exact ⟨ha.1, Nat.lt_of_lt_of_le ha.2 hnm⟩

theorem boundedParts_cover (S : Nat → Prop) (a : Nat) :
    (∃ n, (boundedPart S n).mem a) ↔ S a := by
  constructor
  · rintro ⟨n, hn⟩
    exact hn.1
  · intro ha
    exact ⟨a + 1, ha, Nat.lt_succ_self a⟩

def natOrder : Poset Nat where
  le := Nat.le
  refl := Nat.le_refl
  trans := Nat.le_trans
  antisymm := Nat.le_antisymm

def allNaturals : Ideal natOrder where
  mem _ := True
  nonempty := ⟨0, True.intro⟩
  lower _ _ := True.intro
  directed {p q} _ _ := ⟨max p q, True.intro,
    Nat.le_max_left _ _, Nat.le_max_right _ _⟩

def Unbounded (I : Ideal natOrder) : Prop :=
  ∀ n, ∃ m, I.mem m ∧ n ≤ m

theorem unbounded_allNaturals : Unbounded allNaturals :=
  fun n => ⟨n, True.intro, Nat.le_refl n⟩

theorem principal_not_unbounded (n : Nat) : ¬ Unbounded (principal natOrder n) := by
  intro h
  obtain ⟨m, hm, hn⟩ := h (n + 1)
  change m ≤ n at hm
  omega

theorem original_nat_no_greatest : ∀ n : Nat, ∃ m, n < m :=
  fun n => ⟨n + 1, Nat.lt_succ_self n⟩

theorem completed_nat_greatest : ∀ I : Ideal natOrder, Ideal.LE I allNaturals :=
  fun _ _ _ => True.intro

/-- The infinity reading cannot preserve this directed union. -/
theorem unbounded_reading_not_continuous :
    ¬ CompletionRole.Continuous (CompletionRole.idealDcpo natOrder)
      CompletionRole.truthDcpo Unbounded := by
  intro hc
  have hu := hc.preserves (principalFamily natOrder allNaturals)
    (CompletionRole.fromDirectedFamily (principalFamily_directed natOrder allNaturals))
  have he : (CompletionRole.idealDcpo natOrder).sup
      (principalFamily natOrder allNaturals)
      (CompletionRole.fromDirectedFamily
        (principalFamily_directed natOrder allNaturals)) = allNaturals :=
    union_principalFamily natOrder allNaturals
  rw [he] at hu
  have hright := Eq.mp hu unbounded_allNaturals
  obtain ⟨p, ⟨I, ⟨n, _, rfl⟩, hp⟩, ht⟩ := hright
  exact principal_not_unbounded n (Eq.mpr hp ht)

/-- Chronological right append need not preserve prefix order. -/
theorem right_append_not_prefix_monotone :
    ([] : List Bool).IsPrefix [false] ∧
      ¬ ([true] : List Bool).IsPrefix [false, true] := by
  constructor
  · exact ⟨[false], rfl⟩
  · rintro ⟨l, hl⟩
    cases hl

end CompletionExamples

#print axioms CompletionExamples.FinitePart.ext
#print axioms CompletionExamples.union_partsOf
#print axioms CompletionExamples.finite_cover
#print axioms CompletionExamples.partsOf_union
#print axioms CompletionExamples.union_order_iff
#print axioms CompletionExamples.parts_order_iff
#print axioms CompletionExamples.every_finite_budget_run
#print axioms CompletionExamples.no_budget_runs_forever
#print axioms CompletionExamples.tick_history_identity
#print axioms CompletionExamples.no_infinite_concrete_tick_run
#print axioms CompletionExamples.finite_concrete_tick_run
#print axioms CompletionExamples.ideal_finite_upper
#print axioms CompletionExamples.finite_lub_preserved
#print axioms CompletionExamples.boundedPart_increasing
#print axioms CompletionExamples.boundedParts_cover
#print axioms CompletionExamples.unbounded_allNaturals
#print axioms CompletionExamples.principal_not_unbounded
#print axioms CompletionExamples.original_nat_no_greatest
#print axioms CompletionExamples.completed_nat_greatest
#print axioms CompletionExamples.unbounded_reading_not_continuous
#print axioms CompletionExamples.right_append_not_prefix_monotone
