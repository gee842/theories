import GenerativeCore

/-!
# Inclusive possibility and coherent becoming

Different realizations may be included without permitting unsupported switches
between their continuations. A pooled edge relation is exact for their union of
finite endpoint histories precisely when that union is closed under joining.
The positive construction keeps operative context, and allows it to change by
the same joint step relation. No favourable direction, persistence, totality,
probability, observer or normative premise is imposed.

Types, the interpretation of a context and the joint relation remain inputs.
This is a conditional coherence theorem, not the deduction of reality's laws.
-/

namespace Generative.BecomingCompatibility

universe u v w
variable {I : Type u} {S : Type v} {A : Type w}

def pooled (family : I → Process S A) : Process S A where
  step s a t := ∃ i, (family i).step s a t

def InOne (family : I → Process S A) (s : S) (word : List A) (t : S) : Prop :=
  ∃ i, Trace (family i) s word t

def JoinClosed (family : I → Process S A) : Prop :=
  ∀ s m t xs ys, InOne family s xs m → InOne family m ys t →
    InOne family s (xs ++ ys) t

theorem one_history_enters_pool (family : I → Process S A)
    {s t : S} {word : List A} (h : InOne family s word t) :
    Trace (pooled family) s word t := by
  obtain ⟨i, hi⟩ := h
  exact trace_map (P := family i) (Q := pooled family)
    (f := fun x => x) (fun _ _ _ hs => ⟨i, hs⟩) hi

/-- Joining is the exact missing condition, not an assumed ethical direction.
An inhabited family supplies the zero-event history. -/
theorem pooling_exact_iff_join_closed (family : I → Process S A) (seed : I) :
    (∀ s word t, Trace (pooled family) s word t ↔ InOne family s word t) ↔
      JoinClosed family := by
  constructor
  · intro exactness s m t xs ys hx hy
    apply (exactness s (xs ++ ys) t).mp
    exact trace_append_iff.mpr
      ⟨m, one_history_enters_pool family hx, one_history_enters_pool family hy⟩
  · intro joins s word t
    constructor
    · intro h
      induction h with
      | nil s => exact ⟨seed, .nil s⟩
      | @cons s m t a rest hs _ ih =>
        obtain ⟨i, hi⟩ := hs
        exact joins s m t [a] rest ⟨i, .cons hi (.nil m)⟩ ih
    · exact one_history_enters_pool family

/-- A tag retains the declared context; it need not be a physical object. -/
def retained (family : I → Process S A) : Process (I × S) A where
  step before a after := before.1 = after.1 ∧ (family before.1).step before.2 a after.2

theorem retained_trace_iff (family : I → Process S A)
    {i j : I} {s t : S} {word : List A} :
    Trace (retained family) (i, s) word (j, t) ↔
      i = j ∧ Trace (family i) s word t := by
  constructor
  · intro h
    have general : ∀ {before after : I × S} {as : List A},
        Trace (retained family) before as after →
        before.1 = after.1 ∧ Trace (family before.1) before.2 as after.2 := by
      intro before after as ht
      induction ht with
      | nil x => exact ⟨rfl, .nil x.2⟩
      | @cons x y z a rest hs _ ih =>
        refine ⟨hs.1.trans ih.1, .cons hs.2 ?_⟩
        exact hs.1.symm ▸ ih.2
    exact general h
  · rintro ⟨rfl, h⟩
    exact trace_map (P := family i) (Q := retained family)
      (f := fun x => (i, x)) (fun _ _ _ hs => ⟨rfl, hs⟩) h

theorem retained_realizes_union (family : I → Process S A)
    (s : S) (word : List A) (t : S) :
    (∃ i j, Trace (retained family) (i, s) word (j, t)) ↔ InOne family s word t := by
  constructor
  · rintro ⟨i, j, h⟩
    exact ⟨i, ((retained_trace_iff family).mp h).2⟩
  · rintro ⟨i, h⟩
    exact ⟨i, i, (retained_trace_iff family).mpr ⟨rfl, h⟩⟩

/-- Context and visible conditions participate jointly; changing context is
allowed only through the supplied actual relation. No external selector. -/
def evolving (R : I → S → A → I → S → Prop) : Process (I × S) A where
  step before a after := R before.1 before.2 a after.1 after.2

def eraseContext (R : I → S → A → I → S → Prop) : Process S A where
  step s a t := ∃ i j, R i s a j t

theorem evolving_projects (R : I → S → A → I → S → Prop)
    {before after : I × S} {word : List A}
    (h : Trace (evolving R) before word after) :
    Trace (eraseContext R) before.2 word after.2 :=
  trace_map (P := evolving R) (Q := eraseContext R)
    (f := fun p => p.2) (fun s _ t hs => ⟨s.1, t.1, hs⟩) h

/-- Reuses the existing exact-projection contract; no new independent result
is claimed for the general lifting theorem. -/
theorem erasure_exact_iff_context_lifting (R : I → S → A → I → S → Prop) :
    (∀ i s a t, (∃ j k, R j s a k t) → ∃ k, R i s a k t) ↔
      (∀ i s word t, Trace (eraseContext R) s word t ↔
        ∃ j, Trace (evolving R) (i, s) word (j, t)) := by
  constructor
  · intro lifts i s word t
    constructor
    · intro h
      have lift : ∀ (p : I × S) a t, (eraseContext R).step p.2 a t →
          ∃ q, (evolving R).step p a q ∧ q.2 = t := by
        intro p a t hs
        obtain ⟨j, hj⟩ := lifts p.1 p.2 a t hs
        exact ⟨(j, t), hj, rfl⟩
      obtain ⟨⟨j, z⟩, ht, heq⟩ := trace_lift
        (P := evolving R) (Q := eraseContext R) (q := fun p => p.2)
        (s := (i, s)) lift h
      exact ⟨j, heq ▸ ht⟩
    · rintro ⟨j, h⟩
      exact evolving_projects R h
  · intro exactness i s a t h
    obtain ⟨j, hj⟩ := (exactness i s [a] t).mp (trace_singleton_iff.mpr h)
    exact ⟨j, trace_singleton_iff.mp hj⟩

/-- Endpoint support is derived from the common history, not selected afresh
from all contexts after each step. This is a mathematical description; it does
not assume that a physical observer computes it. -/
def Arrives (R : I → S → A → I → S → Prop) (initial : I → Prop)
    (start : S) (word : List A) (finish : S) (j : I) : Prop :=
  ∃ i, initial i ∧ Trace (evolving R) (i, start) word (j, finish)

def Advance (R : I → S → A → I → S → Prop) (possible : I → Prop)
    (s : S) (a : A) (t : S) (j : I) : Prop :=
  ∃ i, possible i ∧ R i s a j t

theorem arrivals_append (R : I → S → A → I → S → Prop)
    (initial : I → Prop) (s : S) (xs ys : List A) (t : S) (k : I) :
    Arrives R initial s (xs ++ ys) t k ↔
      ∃ m, Arrives R (Arrives R initial s xs m) m ys t k := by
  constructor
  · rintro ⟨i, hi, h⟩
    obtain ⟨⟨j, m⟩, hx, hy⟩ := trace_append_iff.mp h
    exact ⟨m, j, ⟨i, hi, hx⟩, hy⟩
  · rintro ⟨m, j, ⟨i, hi, hx⟩, hy⟩
    exact ⟨i, hi, trace_append_iff.mpr ⟨(j, m), hx, hy⟩⟩

theorem arrivals_singleton (R : I → S → A → I → S → Prop)
    (possible : I → Prop) (s : S) (a : A) (t : S) (j : I) :
    Arrives R possible s [a] t j ↔ Advance R possible s a t j := by
  constructor
  · rintro ⟨i, hi, h⟩
    exact ⟨i, hi, trace_singleton_iff.mp h⟩
  · rintro ⟨i, hi, h⟩
    exact ⟨i, hi, trace_singleton_iff.mpr h⟩

theorem arrivals_snoc (R : I → S → A → I → S → Prop)
    (initial : I → Prop) (s : S) (word : List A) (a : A) (t : S) (j : I) :
    Arrives R initial s (word ++ [a]) t j ↔
      ∃ m, Advance R (Arrives R initial s word m) m a t j := by
  constructor
  · intro h
    obtain ⟨m, hm⟩ := (arrivals_append R initial s word [a] t j).mp h
    exact ⟨m, (arrivals_singleton R _ m a t j).mp hm⟩
  · rintro ⟨m, hm⟩
    exact (arrivals_append R initial s word [a] t j).mpr
      ⟨m, (arrivals_singleton R _ m a t j).mpr hm⟩

theorem empty_support_cannot_advance (R : I → S → A → I → S → Prop)
    (s : S) (a : A) (t : S) (j : I) :
    ¬ Advance R (fun _ => False) s a t j := by
  rintro ⟨_, impossible, _⟩
  exact impossible

theorem actual_step_supplies_advance (R : I → S → A → I → S → Prop)
    {possible : I → Prop} {i j : I} {s t : S} {a : A}
    (hi : possible i) (h : R i s a j t) : Advance R possible s a t j :=
  ⟨i, hi, h⟩

/-- Two declarations are not two independent substances. This finite control
tests the proposed operation of forgetting which relation supports an edge. -/
def splitFamily (b : Bool) : Process Nat Unit where
  step s _ t := (b = false ∧ s = 0 ∧ t = 1) ∨ (b = true ∧ s = 1 ∧ t = 2)

theorem pooled_crosses_incompatible_contexts :
    Trace (pooled splitFamily) 0 [(), ()] 2 := by
  exact .cons ⟨false, Or.inl ⟨rfl, rfl, rfl⟩⟩
    (.cons ⟨true, Or.inr ⟨rfl, rfl, rfl⟩⟩ (.nil 2))

theorem no_single_context_supports_crossing : ¬ InOne splitFamily 0 [(), ()] 2 := by
  rintro ⟨i, h⟩
  obtain ⟨m, first, rest⟩ := trace_cons_iff.mp h
  obtain ⟨n, second, _⟩ := trace_cons_iff.mp rest
  cases first with
  | inl hf =>
    cases second with
    | inl hs => exact Nat.noConfusion (hf.2.2.symm.trans hs.2.1)
    | inr hs => exact Bool.noConfusion (hf.1.symm.trans hs.1)
  | inr hf => exact Nat.noConfusion hf.2.1

theorem split_family_not_join_closed : ¬ JoinClosed splitFamily := by
  intro h
  exact no_single_context_supports_crossing
    (((pooling_exact_iff_join_closed splitFamily false).mpr h 0 [(), ()] 2).mp
      pooled_crosses_incompatible_contexts)

theorem retained_excludes_crossing :
    ¬ ∃ i j, Trace (retained splitFamily) (i, 0) [(), ()] (j, 2) := by
  intro h
  exact no_single_context_supports_crossing ((retained_realizes_union _ _ _ _).mp h)

/-- A real context change is part of the same event that changes the position.
The continuation terminates at 2; no unending growth is assumed. -/
def changingRelation (i : Bool) (s : Nat) (_ : Unit) (j : Bool) (t : Nat) : Prop :=
  (i = false ∧ s = 0 ∧ j = true ∧ t = 1) ∨
  (i = true ∧ s = 1 ∧ j = true ∧ t = 2)

theorem actual_context_change_joins_history :
    Trace (evolving changingRelation) (false, 0) [(), ()] (true, 2) :=
  .cons (m := (true, 1)) (Or.inl ⟨rfl, rfl, rfl, rfl⟩)
    (.cons (Or.inr ⟨rfl, rfl, rfl, rfl⟩) (.nil (true, 2)))

theorem changed_context_is_formed :
    Advance changingRelation (fun i => i = false) 0 () 1 true ∧
      ¬ ((true : Bool) = false) := by
  constructor
  · exact ⟨false, rfl, Or.inl ⟨rfl, rfl, rfl, rfl⟩⟩
  · intro h; cases h

theorem changed_history_has_supported_endpoint :
    Arrives changingRelation (fun i => i = false) 0 [(), ()] 2 true :=
  ⟨false, rfl, actual_context_change_joins_history⟩

theorem changed_history_really_ends (j : Bool) (t : Nat) :
    ¬ changingRelation true 2 () j t := by
  intro h
  cases h with
  | inl h => cases h.1
  | inr h => cases h.2.1

theorem erasure_can_start_from_wrong_context :
    Trace (eraseContext changingRelation) 0 [()] 1 ∧
      ¬ ∃ j, Trace (evolving changingRelation) (true, 0) [()] (j, 1) := by
  constructor
  · exact trace_singleton_iff.mpr ⟨false, true, Or.inl ⟨rfl, rfl, rfl, rfl⟩⟩
  · rintro ⟨j, h⟩
    have hs := trace_singleton_iff.mp h
    cases hs with
    | inl h => cases h.1
    | inr h => exact Nat.noConfusion h.2.1

end Generative.BecomingCompatibility
