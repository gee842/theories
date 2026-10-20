import Becoming.Learning

/-!
# Proposition identity: what identifying interderivable propositions keeps and loses

Lean's `propext` (`(a ↔ b) → a = b`) identifies propositions that derive each other. The core
does not use it: every source declaration has an empty axiom report. This module states, with no
axiom, what `propext` says in the theory's own terms, which readings need it and which do not, and
what the identification keeps and loses. It is about the proof language, not about a web.

* **`propext` is a lumping of every reading.** An interderivation (`Interderivation`) is a pair of
  propositions with a derivation each way, and it has two ends (`endOf`). A reading of propositions
  `g` is lumped by interderivability where `g ∘ endOf` is lumped (`Learning.Lumped`) by the
  interderivation, forgetting which end is read: then `g` takes one value at both ends of every
  interderivation (`lumped_iff`). `propext`, as a proposition (`Extensional`), holds exactly where
  every reading of propositions into propositions is so lumped (`extensional_iff_lumped`), and then
  every reading into any type is (`lumped_of_extensional`).
* **Readings built from relations need nothing.** A formula (`Formula`) is built from atoms, `⊤`,
  `⊥`, `∧`, `∨`, `→` and `∀`, `∃` over any type. Its reading respects interderivability of the
  atoms with no axiom (`Formula.eval_congr`), so a reading of one proposition through a formula,
  the other atoms held fixed, takes interderivable propositions to interderivable ones
  (`Formula.read_congr`). What it gives is `↔`, not `=`.
* **The reading that needs it reads by name.** The identity reading (`byName`) is lumped by
  interderivability exactly where `propext` holds (`byName_lumped_iff`), and where it is lumped every
  reading is (`lumped_of_byName`). So `propext` asks no more of any reading than of this one: that a
  proposition is nothing beyond what derives it and what it derives.
* **What a derivation carries.** Any two witnesses of `a ↔ b` are equal (`iff_witness_unique`), as
  are any two derivations of `b` from `a` (`derivation_unique`): identifying `a` with `b` along an
  interderivation forgets no choice of witness. Between types it would: `Bool` has two different
  self-inverse maps, the identity and negation (`two_equivalences`), so identifying types along an
  equivalence would forget which one.
* **What is lost is the course.** For any equation `e : a = b` between propositions, transport
  along `e` with a motive that does not depend on the proposition is the identity
  (`transport_const`): the outcome is kept. Along `rfl` it is the identity by computation
  (`transport_refl`). That transport along `propext` does not compute is a kernel observation,
  not a theorem: the closed value `Eq.rec 0 (propext …) : Nat` is provably `0` (by
  `transport_const`, with `propext` reported), while `#reduce` stops at the transport and neither
  `rfl` nor `decide` proves it `0` (Lean 4.29.1; the record gives the check).

So where a result would need `=` between propositions, the core states `↔`. Excluding `propext`
gives up no relation and no witness; it gives up replacing `↔` by `=`, which would keep every
outcome and stop the course of a value transported along it. Whether every reading of a
proposition is relational, which is `propext` itself, is not proved here: `Extensional` is a
hypothesis, never a conclusion (that Lean's logic without the axiom does not prove it is known
metatheory, not checked here). The representation commits to Lean's `Prop` with definitional proof
irrelevance. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

universe u v

namespace PropositionIdentity

/-! ## `propext` as a lumping of every reading -/

/-- `propext`, stated as a proposition: interderivable propositions are equal. -/
def Extensional : Prop := ∀ a b : Prop, (a ↔ b) → a = b

/-- A pair of propositions with a derivation each way. -/
def Interderivation : Type := {ab : Prop × Prop // ab.1 ↔ ab.2}

/-- The two ends of an interderivation: `true` reads the first, `false` the second. -/
def endOf : Interderivation × Bool → Prop
  | (d, true) => d.1.1
  | (d, false) => d.1.2

/-- The interderivation, forgetting which end is read. -/
def relation : Interderivation × Bool → Interderivation := Prod.fst

/-- A reading of propositions is lumped by interderivability exactly where it takes one value at
the two propositions of every interderivation. -/
theorem lumped_iff {V : Type v} (g : Prop → V) :
    Learning.Lumped relation (fun i => g (endOf i)) ↔ ∀ a b : Prop, (a ↔ b) → g a = g b :=
  ⟨fun lumped a b h => lumped (⟨(a, b), h⟩, true) (⟨(a, b), h⟩, false) rfl,
   fun respects i i' same =>
    match i, i', same with
    | (_, true), (_, true), rfl => rfl
    | (_, false), (_, false), rfl => rfl
    | (d, true), (_, false), rfl => respects d.1.1 d.1.2 d.2
    | (d, false), (_, true), rfl => (respects d.1.1 d.1.2 d.2).symm⟩

/-- **`propext` is a lumping of every reading**: interderivable propositions are equal exactly where
every reading of propositions into propositions is lumped by interderivability. -/
theorem extensional_iff_lumped :
    Extensional ↔ ∀ g : Prop → Prop, Learning.Lumped relation (fun i => g (endOf i)) :=
  ⟨fun ext g => (lumped_iff (V := Prop) g).mpr fun a b h => congrArg g (ext a b h),
   fun all a b h => (lumped_iff (V := Prop) (fun p => p)).mp (all fun p => p) a b h⟩

/-- Where `propext` holds, every reading of propositions into any type is lumped by
interderivability. -/
theorem lumped_of_extensional (ext : Extensional) {V : Type v} (g : Prop → V) :
    Learning.Lumped relation (fun i => g (endOf i)) :=
  (lumped_iff g).mpr fun a b h => congrArg g (ext a b h)

/-! ## Readings built from relations -/

/-- A formula built from relations alone: atoms, the two constants, the connectives and
quantifiers over any type. -/
inductive Formula (α : Type u) : Type (u + 1) where
  | atom : α → Formula α
  | top : Formula α
  | bot : Formula α
  | and : Formula α → Formula α → Formula α
  | or : Formula α → Formula α → Formula α
  | imp : Formula α → Formula α → Formula α
  | all {β : Type u} : (β → Formula α) → Formula α
  | ex {β : Type u} : (β → Formula α) → Formula α

/-- The proposition a formula states where atom `x` states `ρ x`. -/
def Formula.eval {α : Type u} (ρ : α → Prop) : Formula α → Prop
  | .atom x => ρ x
  | .top => True
  | .bot => False
  | .and p q => p.eval ρ ∧ q.eval ρ
  | .or p q => p.eval ρ ∨ q.eval ρ
  | .imp p q => p.eval ρ → q.eval ρ
  | .all f => ∀ b, (f b).eval ρ
  | .ex f => ∃ b, (f b).eval ρ

/-- **Readings built from relations need no axiom**: interderivable atoms give interderivable
formulas. -/
theorem Formula.eval_congr {α : Type u} {ρ σ : α → Prop} (h : ∀ x, ρ x ↔ σ x) :
    ∀ φ : Formula α, φ.eval ρ ↔ φ.eval σ
  | .atom x => h x
  | .top => Iff.rfl
  | .bot => Iff.rfl
  | .and p q =>
    have hp := eval_congr h p
    have hq := eval_congr h q
    ⟨fun ⟨x, y⟩ => ⟨hp.1 x, hq.1 y⟩, fun ⟨x, y⟩ => ⟨hp.2 x, hq.2 y⟩⟩
  | .or p q =>
    have hp := eval_congr h p
    have hq := eval_congr h q
    ⟨fun t => t.elim (fun x => .inl (hp.1 x)) (fun y => .inr (hq.1 y)),
     fun t => t.elim (fun x => .inl (hp.2 x)) (fun y => .inr (hq.2 y))⟩
  | .imp p q =>
    have hp := eval_congr h p
    have hq := eval_congr h q
    ⟨fun f x => hq.1 (f (hp.2 x)), fun f x => hq.2 (f (hp.1 x))⟩
  | .all f =>
    ⟨fun k b => (eval_congr h (f b)).1 (k b), fun k b => (eval_congr h (f b)).2 (k b)⟩
  | .ex f =>
    ⟨fun ⟨b, x⟩ => ⟨b, (eval_congr h (f b)).1 x⟩, fun ⟨b, x⟩ => ⟨b, (eval_congr h (f b)).2 x⟩⟩

/-- Where the atoms are the proposition read (`none`) and fixed propositions (`some y`). -/
def Formula.atoms {β : Type u} (fixed : β → Prop) (a : Prop) : Option β → Prop
  | none => a
  | some y => fixed y

/-- The reading of a proposition through a formula, the other atoms held fixed. -/
def Formula.read {β : Type u} (φ : Formula (Option β)) (fixed : β → Prop) (a : Prop) : Prop :=
  φ.eval (Formula.atoms fixed a)

/-- A reading through a formula takes interderivable propositions to interderivable ones. -/
theorem Formula.read_congr {β : Type u} (φ : Formula (Option β)) (fixed : β → Prop) {a b : Prop}
    (h : a ↔ b) : φ.read fixed a ↔ φ.read fixed b :=
  Formula.eval_congr (fun
    | none => h
    | some _ => Iff.rfl) φ

/-! ## The reading by name -/

/-- The reading that reads a proposition by itself, by name. -/
def byName : Prop → Prop := fun p => p

/-- **The reading that needs `propext` reads by name**: it is lumped by interderivability exactly
where `propext` holds. -/
theorem byName_lumped_iff : Learning.Lumped relation (fun i => byName (endOf i)) ↔ Extensional :=
  lumped_iff (V := Prop) byName

/-- Where the reading by name is lumped by interderivability, every reading is. -/
theorem lumped_of_byName (lumped : Learning.Lumped relation (fun i => byName (endOf i)))
    {V : Type v} (g : Prop → V) : Learning.Lumped relation (fun i => g (endOf i)) :=
  lumped_of_extensional (byName_lumped_iff.mp lumped) g

/-! ## What a derivation carries -/

/-- Any two witnesses of an interderivation are equal. -/
theorem iff_witness_unique {a b : Prop} (h h' : a ↔ b) : h = h' := rfl

/-- Any two derivations of `b` from `a` are equal. -/
theorem derivation_unique {a b : Prop} (f f' : a → b) : f = f' := rfl

/-- Negation on `Bool`. -/
def flip : Bool → Bool
  | true => false
  | false => true

/-- **Between types an equivalence carries content**: `Bool` has two different self-inverse maps. -/
theorem two_equivalences :
    (∀ x, (fun y : Bool => y) ((fun y : Bool => y) x) = x) ∧ (∀ x, flip (flip x) = x) ∧
      (fun y : Bool => y) ≠ flip :=
  ⟨fun _ => rfl, fun | true => rfl | false => rfl,
   fun same => Bool.noConfusion (congrFun same true)⟩

/-! ## What is lost is the course -/

/-- Transport along any equation of propositions, with a motive that does not depend on the
proposition, keeps the value. -/
theorem transport_const {V : Sort v} {a b : Prop} (e : a = b) (x : V) :
    @Eq.rec Prop a (fun _ _ => V) x b e = x :=
  @Eq.rec Prop a (fun b e => @Eq.rec Prop a (fun _ _ => V) x b e = x) rfl b e

/-- Along a reflexivity the transport is the identity by computation. -/
theorem transport_refl {V : Sort v} {a : Prop} (x : V) :
    @Eq.rec Prop a (fun _ _ => V) x a rfl = x := rfl

end PropositionIdentity

end Becoming
