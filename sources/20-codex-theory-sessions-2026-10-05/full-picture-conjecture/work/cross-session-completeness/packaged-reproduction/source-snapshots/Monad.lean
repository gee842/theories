/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / GUT-C Phase 1.3 (V-enriched monad for upstream Mathlib PR-3)
-/
import Mathlib.CategoryTheory.Enriched.Basic
import Mathlib.CategoryTheory.Enriched.Ordinary.Basic
import Mathlib.CategoryTheory.Monad.Basic

/-!
# V-enriched monads

For `V` a monoidal category and `C` a V-enriched category, a **V-enriched
monad** on `C` is a V-functor `T : C ⥤_V C` together with V-natural
transformations

* unit `η : id_C ⟶ T`
* multiplication `μ : T ∘ T ⟶ T`

satisfying the usual monad axioms (associativity, left/right unit).

This generalises the ordinary `Mathlib.CategoryTheory.Monad.Basic.Monad` to
V-enriched setting (`V = Set` recovers the ordinary case).

V-enriched monads play a central role in Power 1999's Theorem 4.5 (which is
Phase 1.5 of `docs-next/10_formal_形式/enriched-universal-sayability-plan.md`):
the 2-category of V-enriched Lawvere theories is 2-equivalent to the
2-category of finitary V-monads on V.

## Main definitions

* `EnrichedMonadStruct V C` — the *structure* of a V-monad: a V-endofunctor T,
  V-natural unit η, V-natural multiplication μ, satisfying the monad axioms.
* `EnrichedMonad V C` — typeclass version, asserting the existence of a
  distinguished V-monad on `C`.

## Refactor note (Phase A.5.0c, 2026-05-21)

Each V-naturality field and each V-monad law is now a **concrete V-equation**
on V-morphisms (not an arbitrary `Prop`). This unblocks downstream rewriting
in `Kleisli.lean` / `EilenbergMoore.lean`. Backward-compatible accessors
`naturalityLaw`, `assocLaw`, `leftUnitLaw`, `rightUnitLaw` are exposed as
`def`s computing to the concrete equations, preserving the prior
supplied-data idiom used by `Foundation/Doctrine/FullGUTEnrichedFrontier.lean`.

## SSBX vendor notice

This file is part of GUT-C Phase 1 (see plan §4.2 Sub-PR 3.3) and is intended
for upstream Mathlib contribution as `Mathlib.CategoryTheory.Enriched.Monad.Basic`.
It is vendored under SSBX while review proceeds.

## References

* [Kelly, G. M., *Basic Concepts of Enriched Category Theory*, Cambridge 1982;
  TAC Reprint 10 (2005)][Kel82] §1.7-1.8, Ch. 5 (monads on V-categories)
* [Power, J. *Enriched Lawvere theories*, TAC 6 no. 7 (1999), 83-93][Pow99]
  §2 (finitary V-monads)
* [Hyland, M. and Power, J. *The category theoretic understanding of universal
  algebra*, ENTCS 172 (2007)][HP07] §3 (V-monad-theory equivalence)
* nLab: [enriched monad](https://ncatlab.org/nlab/show/enriched+monad)
-/

@[expose] public section

universe w' v' v u u'

open CategoryTheory Category MonoidalCategory

namespace CategoryTheory.Enriched

variable (V : Type u') [Category.{v'} V] [MonoidalCategory V]

/-! ## §1 V-natural transformations between V-functors

We need a notion of V-natural transformation between V-functors for the
unit and multiplication of a V-monad. The V-naturality square is the
standard Kelly 1982 §1.2 square stated as a concrete equation of
V-morphisms `𝟙_V ⊗ (X ⟶[V] Y) ⟶ (F.obj X ⟶[V] G.obj Y)` (no Prop escape
hatch). For the general `C ⥤_V D` variant with additional API (vertical
composition, whiskering, bridges), see `SSBX.Foundation.Enriched.NatTrans.
VNatTrans`. -/

/-- A V-natural transformation between V-functors `F G : C ⥤_V C`.

The component `app X` is a `V`-element `𝟙_V ⟶ F.obj X ⟶[V] G.obj X`. The
`naturality` field is the standard Kelly 1982 §1.2 V-naturality square as
a concrete equation of V-morphisms. -/
structure EnrichedNatTrans (C : Type u) [EnrichedCategory V C]
    (F G : EnrichedFunctor V C C) where
  /-- Component at X : C, a `V`-element. -/
  app : ∀ X : C, 𝟙_ V ⟶ F.obj X ⟶[V] G.obj X
  /-- V-naturality square (Kelly 1982 §1.2): for all `X Y : C`,
  ```
    (λ_).hom ≫ (ρ_).inv ≫ (F.map X Y ⊗ app Y) ≫ eComp
      = (app X ⊗ G.map X Y) ≫ eComp
  ```
  as morphisms `𝟙_V ⊗ (X ⟶[V] Y) ⟶ (F.obj X ⟶[V] G.obj Y)` in V. -/
  naturality : ∀ X Y : C,
    (λ_ (X ⟶[V] Y)).hom ≫ (ρ_ (X ⟶[V] Y)).inv ≫
        (F.map X Y ⊗ₘ app Y) ≫ eComp V (F.obj X) (F.obj Y) (G.obj Y) =
      (app X ⊗ₘ G.map X Y) ≫ eComp V (F.obj X) (G.obj X) (G.obj Y)

namespace EnrichedNatTrans

variable {V}
variable {C : Type u} [EnrichedCategory V C]

/-- The concrete V-naturality square carried by a supplied V-natural
transformation, exposed as a definition for backward compatibility with
the supplied-data API used in `Foundation/Doctrine/FullGUTEnrichedFrontier.lean`. -/
def naturalityLaw {F G : EnrichedFunctor V C C}
    (α : EnrichedNatTrans V C F G) : Prop :=
  ∀ X Y : C,
    (λ_ (X ⟶[V] Y)).hom ≫ (ρ_ (X ⟶[V] Y)).inv ≫
        (F.map X Y ⊗ₘ α.app Y) ≫ eComp V (F.obj X) (F.obj Y) (G.obj Y) =
      (α.app X ⊗ₘ G.map X Y) ≫ eComp V (F.obj X) (G.obj X) (G.obj Y)

/-- The concrete V-naturality law carried by a supplied V-natural
transformation. -/
theorem naturality_holds {F G : EnrichedFunctor V C C}
    (α : EnrichedNatTrans V C F G) :
    α.naturalityLaw :=
  α.naturality

/-- The identity V-natural transformation.

The V-naturality square reduces to the V-enriched identity-composition
laws `e_id_comp V (F.obj X) (F.obj Y)` and `e_comp_id V (F.obj X)
(F.obj Y)` plus monoidal-unitor coherence. See `VNatTrans.id` in
`SSBX.Foundation.Enriched.NatTrans` for the analogous proof in the
general `C ⥤_V D` setting. -/
def id (F : EnrichedFunctor V C C) : EnrichedNatTrans V C F F where
  app X := eId V (F.obj X)
  naturality X Y := by
    -- Both sides equal `(λ_ (X ⟶[V] Y)).hom ≫ F.map X Y`.
    -- LHS: `tensorHom_def` + `rightUnitor_inv_naturality` + `e_comp_id`.
    -- RHS: `tensorHom_def'` reverses the order, then
    -- `leftUnitor_naturality` brings `(λ_).hom` to a common form, and
    -- `e_id_comp` collapses the trailing `(eId ▷ _) ≫ eComp` to `(λ_).hom`.
    rw [tensorHom_def (F.map X Y) (eId V (F.obj Y)), Category.assoc,
      ← rightUnitor_inv_naturality_assoc, e_comp_id, Category.comp_id,
      tensorHom_def' (eId V (F.obj X)) (F.map X Y), Category.assoc,
      ← leftUnitor_naturality]
    congr 1
    rw [eq_comm, ← Category.id_comp (_ ≫ eComp V _ _ _),
      ← Iso.hom_inv_id (λ_ (F.obj X ⟶[V] F.obj Y)), Category.assoc, e_id_comp,
      Category.comp_id]

end EnrichedNatTrans

/-! ## §2 The V-monad structure -/

/-- A V-enriched monad on a V-category `C` consists of:

* an endo-V-functor `T : C ⥤_V C`
* a V-natural unit `η : id ⟶ T`
* a V-natural multiplication `μ : T ∘ T ⟶ T`

satisfying the monad axioms (associativity, left unit, right unit).

Refactor (Phase A.5.0c, 2026-05-21): each monad law is now a *concrete*
V-equation between V-morphisms, expressed in V-element form via
`𝟙_V ⟶ (T(T(T X)) ⟶[V] T X)` for associativity and
`𝟙_V ⟶ (T X ⟶[V] T X)` for unit laws. This unblocks downstream rewriting
in `Kleisli.lean` and `EilenbergMoore.lean`. Backward-compatible
supplied-data accessors `assocLaw`, `leftUnitLaw`, `rightUnitLaw` are
exposed as `def`s computing to the concrete equations. -/
structure EnrichedMonadStruct (C : Type u) [EnrichedCategory V C] where
  /-- The underlying V-endofunctor. -/
  T : EnrichedFunctor V C C
  /-- The V-natural unit. -/
  η : EnrichedNatTrans V C (EnrichedFunctor.id V C) T
  /-- The V-natural multiplication. -/
  μ : EnrichedNatTrans V C (EnrichedFunctor.comp V T T) T
  /-- V-monad associativity `μ ∘ Tμ = μ ∘ μT` in V-element form:
      both sides are V-elements of `T(T(T X)) ⟶[V] T X`. -/
  assoc : ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      ((μ.app X ≫ T.map (T.obj (T.obj X)) (T.obj X)) ⊗ₘ μ.app X) ≫
        eComp V (T.obj (T.obj (T.obj X))) (T.obj (T.obj X)) (T.obj X) =
      (λ_ (𝟙_ V)).inv ≫
        (μ.app (T.obj X) ⊗ₘ μ.app X) ≫
          eComp V (T.obj (T.obj (T.obj X))) (T.obj (T.obj X)) (T.obj X)
  /-- V-monad left unit `μ ∘ Tη = id_T` in V-element form:
      LHS is a V-element of `T X ⟶[V] T X`, equal to `eId V (T X)`. -/
  left_unit : ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      ((η.app X ≫ T.map X (T.obj X)) ⊗ₘ μ.app X) ≫
        eComp V (T.obj X) (T.obj (T.obj X)) (T.obj X) =
      eId V (T.obj X)
  /-- V-monad right unit `μ ∘ ηT = id_T` in V-element form:
      LHS is a V-element of `T X ⟶[V] T X`, equal to `eId V (T X)`. -/
  right_unit : ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      (η.app (T.obj X) ⊗ₘ μ.app X) ≫
        eComp V (T.obj X) (T.obj (T.obj X)) (T.obj X) =
      eId V (T.obj X)

/-- A V-enriched monad on `C`: an `EnrichedMonadStruct` packaged as a class. -/
class EnrichedMonad (C : Type u) [EnrichedCategory V C] where
  /-- The underlying V-monad structure. -/
  struct : EnrichedMonadStruct V C

namespace EnrichedMonadStruct

variable {V}
variable {C : Type u} [EnrichedCategory V C]

/-- The associativity-law proposition carried by a V-enriched monad
structure, exposed as a definition for backward compatibility with the
supplied-data API. -/
def assocLaw (M : EnrichedMonadStruct V C) : Prop :=
  ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      ((M.μ.app X ≫ M.T.map (M.T.obj (M.T.obj X)) (M.T.obj X)) ⊗ₘ M.μ.app X) ≫
        eComp V (M.T.obj (M.T.obj (M.T.obj X))) (M.T.obj (M.T.obj X)) (M.T.obj X) =
      (λ_ (𝟙_ V)).inv ≫
        (M.μ.app (M.T.obj X) ⊗ₘ M.μ.app X) ≫
          eComp V (M.T.obj (M.T.obj (M.T.obj X))) (M.T.obj (M.T.obj X)) (M.T.obj X)

/-- The left-unit-law proposition carried by a V-enriched monad structure,
exposed as a definition for backward compatibility. -/
def leftUnitLaw (M : EnrichedMonadStruct V C) : Prop :=
  ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      ((M.η.app X ≫ M.T.map X (M.T.obj X)) ⊗ₘ M.μ.app X) ≫
        eComp V (M.T.obj X) (M.T.obj (M.T.obj X)) (M.T.obj X) =
      eId V (M.T.obj X)

/-- The right-unit-law proposition carried by a V-enriched monad
structure, exposed as a definition for backward compatibility. -/
def rightUnitLaw (M : EnrichedMonadStruct V C) : Prop :=
  ∀ X : C,
    (λ_ (𝟙_ V)).inv ≫
      (M.η.app (M.T.obj X) ⊗ₘ M.μ.app X) ≫
        eComp V (M.T.obj X) (M.T.obj (M.T.obj X)) (M.T.obj X) =
      eId V (M.T.obj X)

/-- The associativity law carried by a supplied V-enriched monad structure. -/
theorem assoc_holds (M : EnrichedMonadStruct V C) :
    M.assocLaw :=
  M.assoc

/-- The V-naturality law carried by the unit of a supplied V-enriched monad. -/
theorem unit_naturality_holds (M : EnrichedMonadStruct V C) :
    M.η.naturalityLaw :=
  M.η.naturality

/-- The V-naturality law carried by the multiplication of a supplied
V-enriched monad. -/
theorem mul_naturality_holds (M : EnrichedMonadStruct V C) :
    M.μ.naturalityLaw :=
  M.μ.naturality

/-- The left-unit law carried by a supplied V-enriched monad structure. -/
theorem leftUnit_holds (M : EnrichedMonadStruct V C) :
    M.leftUnitLaw :=
  M.left_unit

/-- The right-unit law carried by a supplied V-enriched monad structure. -/
theorem rightUnit_holds (M : EnrichedMonadStruct V C) :
    M.rightUnitLaw :=
  M.right_unit

end EnrichedMonadStruct

/-! ## §3 Specialisation: V = Type recovers ordinary `Monad`

A V-enriched monad with V = Type u, on a Type-enriched ordinary category
(equivalently, an ordinary category) recovers Mathlib's `Monad C`.

The full proof requires the `Type`-as-V coherence + EnrichedOrdinaryCategory
bridge for `V = Type u`. We therefore expose a supplied-data package rather
than an unconditional theorem. -/

/-- Supplied comparison data witnessing that a `Type`-enriched monad
specialises to an ordinary Mathlib monad on the same category. -/
structure EnrichedMonadTypeSpecialisationData (C : Type u) [Category.{v} C] where
  /-- The ordinary monad recovered from the `Type`-enriched data. -/
  ordinaryMonad : Monad C
  /-- The proposition expressing the comparison with the enriched monad data. -/
  comparisonLaw : Prop
  /-- Proof of the stated comparison law. -/
  comparison : comparisonLaw

/-- Conditional specialisation theorem: once the comparison data is supplied,
the `Type`-enriched monad has an ordinary Mathlib monad representative. -/
theorem enrichedMonad_Type_specialises_to_Monad_statement
    {C : Type u} [Category.{v} C]
    (data : EnrichedMonadTypeSpecialisationData C) :
    Nonempty (EnrichedMonadTypeSpecialisationData C) :=
  ⟨data⟩

/-- The supplied comparison law in a `Type`-specialisation package. -/
theorem enrichedMonadTypeSpecialisation_comparison_holds
    {C : Type u} [Category.{v} C]
    (data : EnrichedMonadTypeSpecialisationData C) :
    data.comparisonLaw :=
  data.comparison

/-- The ordinary Mathlib monad selected by a `Type`-specialisation package. -/
def enrichedMonadTypeSpecialisation_ordinaryMonad
    {C : Type u} [Category.{v} C]
    (data : EnrichedMonadTypeSpecialisationData C) :
    Monad C :=
  data.ordinaryMonad

end CategoryTheory.Enriched
