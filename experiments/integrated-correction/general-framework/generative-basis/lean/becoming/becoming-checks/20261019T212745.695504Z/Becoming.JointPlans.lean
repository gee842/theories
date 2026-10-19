import Becoming.Prelude

/-!
# Joint plans: nested decompositions of a ternary relation, and what their leaves draw on

A ternary relation `J s l r` says that `s` holds `l` and `r` together; nothing more is assumed of
it. A joint plan is a finite binary nesting of leaves (`JointPlan`), and a configuration realizes
it where it holds together parts realizing its two sides, down to leaves read at the parts
(`JointPlan.Realizes`). Each node keeps its own witness: nothing fixes which particular parts are
used, or shared across branches.

* **Exclusive footprints.** Where the footprint of each part a whole holds lies within the whole's
  (`PartsWithin`), what the leaves of a realized plan draw on, joined in order
  (`JointPlan.draws`), lies within the root's footprint (`JointPlan.within_of_realizes`); where
  also the two parts' footprints share nothing (`PartsApart`), it repeats nothing
  (`JointPlan.nodup_of_realizes`), so the root's footprint supports it (`Supports`,
  `JointPlan.supports_of_realizes`). Two facts of lists carry this at every universe
  (`ListTests.mem_append_iff` of `Becoming.Prelude`, and `nodup_append_of_apart`).

Nothing here reads a frame or a labelled process. These declarations were stated in
`Becoming.Composition` and are moved here unchanged, with their names, so that the modules using
them without a frame (`Becoming.ListFootprints`) do not import it (board item W). The laws of
plans read through a description stay in `Becoming.Composition`, and those of joint frames in
`Becoming.JointPlanFrames`. No ethical predicate, ranking or axiom occurs.
-/

/-! ## Nested decompositions and exclusive footprints (moved from `Becoming.Composition`) -/

namespace Becoming

universe u v w u' u'' w' x'

/-- A joint plan: a finite binary nesting of leaves. -/
inductive JointPlan (Q : Type w) where
  | leaf (q : Q)
  | pair (left right : JointPlan Q)

section Plans

variable {S : Type u} {K : Type w'} {Q : Type w}

/-- A configuration realizes a plan where it holds together parts realizing its two sides, down to
leaves read at the parts. Each node has its own witness. -/
def JointPlan.Realizes {X : Type u} (J : X → X → X → Prop) (leaf : X → Q → Prop) :
    X → JointPlan Q → Prop
  | s, .leaf q => leaf s q
  | s, .pair p q => ∃ x y, J s x y ∧ JointPlan.Realizes J leaf x p ∧ JointPlan.Realizes J leaf y q

end Plans

section Footprints

variable {S : Type u} {K : Type w'} {R : Type x'}

/-- Two lists without repetition and with no member in common join without repetition. -/
theorem nodup_append_of_apart {α : Type u} :
    ∀ {l m : List α}, l.Nodup → m.Nodup → (∀ a, a ∈ l → a ∈ m → False) → (l ++ m).Nodup
  | [], _, _, distinct, _ => distinct
  | a :: l, _, .cons fresh distinct, distinct', apart =>
    .cons (fun b mem same => match ListTests.mem_append_iff.mp mem with
      | .inl inside => fresh b inside same
      | .inr outside => apart a (.head l) (Eq.subst (motive := fun x => x ∈ _) same.symm outside))
      (nodup_append_of_apart distinct distinct' fun b mem => apart b (.tail a mem))

/-- The footprint of each part a whole holds lies within the whole's. -/
def PartsWithin (footprint : S → R → Prop) (J : S → S → S → Prop) : Prop :=
  ∀ s l r, J s l r → (∀ a, footprint l a → footprint s a) ∧ (∀ a, footprint r a → footprint s a)

/-- The two parts a whole holds have no footprint in common. -/
def PartsApart (footprint : S → R → Prop) (J : S → S → S → Prop) : Prop :=
  ∀ s l r, J s l r → ∀ a, footprint l a → footprint r a → False

/-- A configuration's footprint supports a list where the list repeats nothing and each member lies
within the footprint. -/
def Supports (footprint : S → R → Prop) (s : S) (xs : List R) : Prop :=
  xs.Nodup ∧ ∀ a, a ∈ xs → footprint s a

/-- What the leaves of a plan draw on, joined in order. -/
def JointPlan.draws : JointPlan (List R) → List R
  | .leaf xs => xs
  | .pair p q => JointPlan.draws p ++ JointPlan.draws q

/-- What the leaves of a realized plan draw on lies within the root's footprint, where each part's
footprint lies within its whole's. -/
theorem JointPlan.within_of_realizes {footprint : S → R → Prop} {J : S → S → S → Prop}
    (within : PartsWithin footprint J) :
    ∀ (p : JointPlan (List R)) (s : S), JointPlan.Realizes J (Supports footprint) s p →
      ∀ a, a ∈ p.draws → footprint s a
  | .leaf _, _, supports => supports.2
  | .pair p q, s, ⟨l, r, joint, left, right⟩ => fun a mem => match ListTests.mem_append_iff.mp mem with
    | .inl inside => (within s l r joint).1 a (JointPlan.within_of_realizes within p l left a inside)
    | .inr outside => (within s l r joint).2 a (JointPlan.within_of_realizes within q r right a outside)

/-- What the leaves of a realized plan draw on repeats nothing, where each part's footprint lies
within its whole's and the two parts' footprints share nothing. -/
theorem JointPlan.nodup_of_realizes {footprint : S → R → Prop} {J : S → S → S → Prop}
    (within : PartsWithin footprint J) (apart : PartsApart footprint J) :
    ∀ (p : JointPlan (List R)) (s : S), JointPlan.Realizes J (Supports footprint) s p →
      p.draws.Nodup
  | .leaf _, _, supports => supports.1
  | .pair p q, s, ⟨l, r, joint, left, right⟩ =>
    nodup_append_of_apart (JointPlan.nodup_of_realizes within apart p l left)
      (JointPlan.nodup_of_realizes within apart q r right) fun a inside outside =>
        apart s l r joint a (JointPlan.within_of_realizes within p l left a inside)
          (JointPlan.within_of_realizes within q r right a outside)

/-- **Exclusive footprints support every leaf.** Where each part's footprint lies within its
whole's and the two parts' footprints share nothing, the root's footprint supports what all the
leaves of a realized plan draw on: nothing repeats, and everything lies within it. -/
theorem JointPlan.supports_of_realizes {footprint : S → R → Prop} {J : S → S → S → Prop}
    (within : PartsWithin footprint J) (apart : PartsApart footprint J) (p : JointPlan (List R))
    (s : S) (realizes : JointPlan.Realizes J (Supports footprint) s p) :
    Supports footprint s p.draws :=
  ⟨JointPlan.nodup_of_realizes within apart p s realizes,
   JointPlan.within_of_realizes within p s realizes⟩

end Footprints

end Becoming
