import Std

/-!
Induction characterizes generation within a supplied zero/successor carrier.
Constructor separation is a distinct condition. Together these give the
natural-number representation and its recursive mapping property. Predicate
admission, the ambient natural numbers and the carrier are explicit inputs;
their independent foundational warrant is not concluded here.
-/
namespace InductiveDomain
universe u v
variable {A : Type u} {B : Type v}

def iterate (z : A) (s : A → A) : Nat → A
  | 0 => z
  | n+1 => s (iterate z s n)

def Generated (z : A) (s : A → A) (a : A) : Prop := ∃ n, iterate z s n = a

def NoJunk (z : A) (s : A → A) : Prop := ∀ a, Generated z s a

def Closed (z : A) (s : A → A) (P : A → Prop) : Prop := P z ∧ ∀ a, P a → P (s a)

def FullInduction (z : A) (s : A → A) : Prop := ∀ P, Closed z s P → ∀ a, P a

def SelectedInduction (C : (A → Prop) → Prop) (z : A) (s : A → A) : Prop :=
  ∀ P, C P → Closed z s P → ∀ a, P a

theorem generated_closed (z : A) (s : A → A) : Closed z s (Generated z s) := by
  refine ⟨⟨0, rfl⟩, ?_⟩
  rintro a ⟨n, rfl⟩
  exact ⟨n+1, rfl⟩

theorem generated_least (z : A) (s : A → A) (P : A → Prop) (h : Closed z s P)
    {a : A} (ha : Generated z s a) : P a := by
  obtain ⟨n, rfl⟩ := ha
  induction n with
  | zero => exact h.1
  | succ n ih => exact h.2 _ ih

theorem fullInduction_iff_noJunk (z : A) (s : A → A) : FullInduction z s ↔ NoJunk z s :=
  ⟨fun h => h (Generated z s) (generated_closed z s),
    fun h P hp a => generated_least z s P hp (h a)⟩

theorem selected_iff_noJunk (C : (A → Prop) → Prop) (z : A) (s : A → A)
    (hg : C (Generated z s)) : SelectedInduction C z s ↔ NoJunk z s :=
  ⟨fun h => h (Generated z s) hg (generated_closed z s),
    fun h P _ hp a => generated_least z s P hp (h a)⟩

structure Separated (z : A) (s : A → A) : Prop where
  injective : Function.Injective s
  not_zero : ∀ a, s a ≠ z

theorem iterate_injective (z : A) (s : A → A) (h : Separated z s) :
    Function.Injective (iterate z s) := by
  intro n
  induction n with
  | zero =>
    intro m he
    cases m with
    | zero => rfl
    | succ m => exact False.elim (h.not_zero _ he.symm)
  | succ n ih =>
    intro m he
    cases m with
    | zero => exact False.elim (h.not_zero _ he)
    | succ m => exact congrArg Nat.succ (ih (h.injective he))

noncomputable def index (z : A) (s : A → A) (h : NoJunk z s) (a : A) : Nat :=
  Classical.choose (h a)

theorem iterate_index (z : A) (s : A → A) (h : NoJunk z s) (a : A) :
    iterate z s (index z s h a) = a := Classical.choose_spec (h a)

theorem index_iterate (z : A) (s : A → A) (h : NoJunk z s) (hs : Separated z s) (n : Nat) :
    index z s h (iterate z s n) = n := iterate_injective z s hs (iterate_index z s h _)

structure NatEquivalence (z : A) (s : A → A) where
  toCarrier : Nat → A
  toNat : A → Nat
  left_inverse : ∀ n, toNat (toCarrier n) = n
  right_inverse : ∀ a, toCarrier (toNat a) = a
  zero : toCarrier 0 = z
  successor : ∀ n, toCarrier (n+1) = s (toCarrier n)

noncomputable def naturalEquivalence (z : A) (s : A → A)
    (h : NoJunk z s) (hs : Separated z s) : NatEquivalence z s where
  toCarrier := iterate z s
  toNat := index z s h
  left_inverse := index_iterate z s h hs
  right_inverse := iterate_index z s h
  zero := rfl
  successor _ := rfl

def Hom (z : A) (s : A → A) (b : B) (t : B → B) (f : A → B) : Prop :=
  f z = b ∧ ∀ a, f (s a) = t (f a)

theorem hom_iterate (z : A) (s : A → A) (b : B) (t : B → B)
    (f : A → B) (hf : Hom z s b t f) (n : Nat) :
    f (iterate z s n) = iterate b t n := by
  induction n with
  | zero => exact hf.1
  | succ n ih =>
    change f (s (iterate z s n)) = t (iterate b t n)
    rw [hf.2, ih]

noncomputable def recurse (z : A) (s : A → A) (h : NoJunk z s)
    (b : B) (t : B → B) : A → B := fun a => iterate b t (index z s h a)

theorem recurse_iterate (z : A) (s : A → A) (h : NoJunk z s) (hs : Separated z s)
    (b : B) (t : B → B) (n : Nat) :
    recurse z s h b t (iterate z s n) = iterate b t n := by
  unfold recurse
  rw [index_iterate z s h hs]

theorem recurse_hom (z : A) (s : A → A) (h : NoJunk z s) (hs : Separated z s)
    (b : B) (t : B → B) : Hom z s b t (recurse z s h b t) := by
  constructor
  · exact recurse_iterate z s h hs b t 0
  · intro a
    obtain ⟨n, rfl⟩ := h a
    change recurse z s h b t (iterate z s (n+1)) = t (recurse z s h b t (iterate z s n))
    rw [recurse_iterate z s h hs, recurse_iterate z s h hs]
    rfl

theorem hom_unique (z : A) (s : A → A) (h : NoJunk z s)
    (b : B) (t : B → B) (f g : A → B) (hf : Hom z s b t f) (hg : Hom z s b t g) : f = g := by
  funext a
  obtain ⟨n, rfl⟩ := h a
  exact (hom_iterate z s b t f hf n).trans (hom_iterate z s b t g hg n).symm

theorem unique_recursion (z : A) (s : A → A) (h : NoJunk z s) (hs : Separated z s)
    (b : B) (t : B → B) : ∃ f : A → B, Hom z s b t f ∧ ∀ g, Hom z s b t g → g = f :=
  ⟨recurse z s h b t, recurse_hom z s h hs b t,
    fun g hg => hom_unique z s h b t g _ hg (recurse_hom z s h hs b t)⟩

theorem bool_generated : NoJunk false Bool.not := by
  intro a
  cases a with
  | false => exact ⟨0, rfl⟩
  | true => exact ⟨1, rfl⟩

theorem bool_fullInduction : FullInduction false Bool.not :=
  (fullInduction_iff_noJunk false Bool.not).mpr bool_generated

theorem bool_not_separated : ¬ Separated false Bool.not :=
  fun h => h.not_zero true rfl

def extraSuccessor : Option Nat → Option Nat
  | none => none
  | some n => some (n+1)

theorem extra_separated : Separated (some 0) extraSuccessor := by
  constructor
  · intro a b h
    cases a <;> cases b <;> simp [extraSuccessor] at h ⊢
    exact h
  · intro a
    cases a <;> simp [extraSuccessor]

theorem extra_iterate (n : Nat) : iterate (some 0) extraSuccessor n = some n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [iterate, ih, extraSuccessor]

theorem extra_not_noJunk : ¬ NoJunk (some 0) extraSuccessor := by
  intro h
  obtain ⟨n, hn⟩ := h none
  rw [extra_iterate] at hn
  cases hn

theorem nat_iterate (n : Nat) : iterate 0 Nat.succ n = n := by
  induction n with
  | zero => rfl
  | succ n ih => exact congrArg Nat.succ ih

theorem nat_generated : NoJunk 0 Nat.succ := fun n => ⟨n, nat_iterate n⟩

theorem nat_separated : Separated 0 Nat.succ :=
  ⟨fun _ _ h => Nat.succ.inj h, fun _ => Nat.noConfusion⟩

def OnlyGenerated : (Nat → Prop) → Prop := fun P => P = Generated 0 Nat.succ

theorem restricted_selected_induction : SelectedInduction OnlyGenerated 0 Nat.succ :=
  (selected_iff_noJunk OnlyGenerated 0 Nat.succ rfl).mpr nat_generated

theorem restricted_excludes_false : ¬ OnlyGenerated (fun _ => False) := by
  intro h
  have hz : Generated 0 Nat.succ 0 := ⟨0, rfl⟩
  change (fun _ : Nat => False) = Generated 0 Nat.succ at h
  rw [← h] at hz
  exact hz

theorem restricted_not_full : ¬ ∀ P : Nat → Prop, OnlyGenerated P :=
  fun h => restricted_excludes_false (h _)

end InductiveDomain
