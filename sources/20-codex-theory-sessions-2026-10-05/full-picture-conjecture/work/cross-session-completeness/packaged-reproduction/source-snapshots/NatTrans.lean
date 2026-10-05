/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / Path A Phase A.2 (V-natural transformations)
-/
import Mathlib.CategoryTheory.Enriched.Basic
import Mathlib.CategoryTheory.Enriched.Ordinary.Basic
import SSBX.Foundation.Enriched.TypeOrdinary
import SSBX.Foundation.Enriched.Monad

/-!
# V-natural transformations between V-functors

For `V` a monoidal category, `C`, `D` two V-enriched categories, and
`F G : C ⥤_V D` two V-functors, a **V-natural transformation** `α : F ⟶ G` is
a family of generalized elements

  `α.app X : 𝟙_ V ⟶ (F.obj X ⟶[V] G.obj X)`

satisfying the V-naturality square: for all `X Y : C`, the two paths

  `(X ⟶[V] Y) → (F.obj X ⟶[V] G.obj Y)`

through V agree. Concretely, the square
```
  𝟙_ V ⊗ (X ⟶[V] Y)  ──── (λ_).hom · (ρ_).inv ────→  (X ⟶[V] Y) ⊗ 𝟙_ V
        │                                                      │
        │ app X ⊗ G.map X Y                       F.map X Y ⊗ app Y
        ↓                                                      ↓
  (F.obj X ⟶[V] G.obj X) ⊗ (G.obj X ⟶[V] G.obj Y)        (F.obj X ⟶[V] F.obj Y) ⊗ (F.obj Y ⟶[V] G.obj Y)
        │                                                      │
        │ eComp V                                  eComp V
        ↓                                                      ↓
  (F.obj X ⟶[V] G.obj Y)  ════════════════════════════════  (F.obj X ⟶[V] G.obj Y)
```
commutes in V. This is the standard *V*-naturality square (Kelly 1982 §1.2),
the unit-graded specialization of `GradedNatTrans` from `Mathlib.CategoryTheory.
Enriched.Basic`.

## Relation to existing definitions

* **Mathlib's `EnrichedNatTrans`** (`Mathlib.CategoryTheory.Enriched.Basic`)
  packages a V-natural transformation as a `Functor.forget`-natural transformation
  via `out : F.forget ⟶ G.forget`. This is the elegant route for V braided/complete,
  but obscures the underlying V-square for downstream calculation.

* **`Mathlib.CategoryTheory.Enriched.Basic.GradedNatTrans`** is the right notion at
  general grading `A : Center V`. Our `VNatTrans` is its specialization to
  `A := 𝟙_ V` with canonical half-braiding.

* **SSBX's `CategoryTheory.Enriched.EnrichedNatTrans`** (`SSBX.Foundation.Enriched.
  Monad`) is a narrower ad-hoc structure for V-endofunctors `C ⥤_V C` carrying a
  supplied-data naturality proposition. This file's `VNatTrans` provides the
  *general* `C ⥤_V D` case with *actual* V-naturality (no propositional escape
  hatch). §6 builds a one-way conversion `toEndo`.

## Main definitions

* `VNatTrans V C D F G` — the structure of a V-natural transformation
  between V-functors `F G : C ⥤_V D`. Carries `app` and a propositional
  V-naturality square `v_naturality`.
* `VNatTrans.id F` — the identity V-natural transformation `F ⟶ F`.
* `VNatTrans.vcomp α β` — vertical composition `F → G → H` of V-natural
  transformations.
* `VNatTrans.hcompL G α` — left whiskering of a V-functor with a V-nat trans.
* `VNatTrans.hcompR α F` — right whiskering.
* `VNatTrans.toEndo` — bridge from this file's general structure to the
  narrower `CategoryTheory.Enriched.EnrichedNatTrans` for endofunctors.

## SSBX vendor notice

This file is part of Path A Phase A.2 of the Power 1999 Theorem 4.5 program.
It is intended for eventual upstream contribution to
`Mathlib.CategoryTheory.Enriched.NatTrans` once API stabilizes. Vendored
under `SSBX.Foundation.Enriched.NatTrans` while review proceeds.

## References

* [Kelly, G. M., *Basic Concepts of Enriched Category Theory*, Cambridge 1982;
  TAC Reprint 10 (2005)][Kel82] §§1.2, 1.7 (enriched natural transformations)
* [Power, J. *Enriched Lawvere theories*, TAC 6 no. 7 (1999), 83-93][Pow99] §2
  (uses V-natural transformations to state the 2-equivalence)
* nLab: [enriched natural transformation](https://ncatlab.org/nlab/show/enriched+natural+transformation)
-/

@[expose] public section

universe w' v' v u u' u₂ u₃

open CategoryTheory Category MonoidalCategory

namespace CategoryTheory.Enriched

variable (V : Type u') [Category.{v'} V] [MonoidalCategory V]

/-! ## §1 V-natural transformations between V-functors -/

/-- A V-natural transformation between V-functors `F G : C ⥤_V D`.

The component `app X` is a `V`-generalized element
`𝟙_ V ⟶ (F.obj X ⟶[V] G.obj X)`. The `v_naturality` field is the standard
V-naturality square (Kelly 1982 §1.2): for all `X Y : C`, the two morphisms
`𝟙_ V ⊗ (X ⟶[V] Y) ⟶ (F.obj X ⟶[V] G.obj Y)` in V agree.

This is the unit-graded `GradedNatTrans` (`Mathlib.CategoryTheory.Enriched.
Basic`) with the canonical half-braiding `(λ_) ≪≫ (ρ_).symm`.

For the narrower endofunctor variant carrying a supplied-data naturality
proposition, see `CategoryTheory.Enriched.EnrichedNatTrans` in
`SSBX.Foundation.Enriched.Monad`. -/
structure VNatTrans
    (C : Type u) [EnrichedCategory V C]
    (D : Type u₂) [EnrichedCategory V D]
    (F G : EnrichedFunctor V C D) where
  /-- Component at `X : C`, a V-generalized element of `F.obj X ⟶[V] G.obj X`. -/
  app : ∀ X : C, 𝟙_ V ⟶ F.obj X ⟶[V] G.obj X
  /-- V-naturality square: for all `X Y : C`,
  ```
    (λ_).hom ≫ (ρ_).inv ≫ (F.map X Y ⊗ app Y) ≫ eComp
      = (app X ⊗ G.map X Y) ≫ eComp
  ```
  as morphisms `𝟙_ V ⊗ (X ⟶[V] Y) ⟶ (F.obj X ⟶[V] G.obj Y)` in V.

  This is the standard Kelly 1982 §1.2 V-naturality square,
  in the form used by `Mathlib.CategoryTheory.Enriched.Basic.GradedNatTrans`. -/
  v_naturality : ∀ X Y : C,
    (λ_ (X ⟶[V] Y)).hom ≫ (ρ_ (X ⟶[V] Y)).inv ≫
        (F.map X Y ⊗ₘ app Y) ≫ eComp V (F.obj X) (F.obj Y) (G.obj Y) =
      (app X ⊗ₘ G.map X Y) ≫ eComp V (F.obj X) (G.obj X) (G.obj Y)

namespace VNatTrans

variable {V}
variable {C : Type u} [EnrichedCategory V C]
variable {D : Type u₂} [EnrichedCategory V D]

/-! ## §2 Extensionality and basic API -/

/-- Two V-natural transformations are equal iff their components agree. -/
@[ext]
theorem ext {F G : EnrichedFunctor V C D}
    {α β : VNatTrans V C D F G}
    (h : ∀ X : C, α.app X = β.app X) :
    α = β := by
  cases α
  cases β
  congr
  funext X
  exact h X

/-- The V-naturality square as a separate theorem for ease of rewriting. -/
@[reassoc]
theorem naturality_square {F G : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) (X Y : C) :
    (λ_ (X ⟶[V] Y)).hom ≫ (ρ_ (X ⟶[V] Y)).inv ≫
        (F.map X Y ⊗ₘ α.app Y) ≫ eComp V (F.obj X) (F.obj Y) (G.obj Y) =
      (α.app X ⊗ₘ G.map X Y) ≫ eComp V (F.obj X) (G.obj X) (G.obj Y) :=
  α.v_naturality X Y

/-! ## §3 The identity V-natural transformation

For each V-functor `F : C ⥤_V D`, the family of identity generalized elements
`X ↦ eId V (F.obj X)` is V-natural.

The naturality square reduces to the enriched identity-composition laws
`e_id_comp` / `e_comp_id`, but stating this requires unitor-coherence
arguments in V which are mechanical but non-trivial. We use
`v_naturality_id_proof_obligation` to document the precise content. -/

/-- The V-naturality square for the identity V-natural transformation, as a
free-standing statement. -/
def v_naturality_id_proof_obligation
    (F : EnrichedFunctor V C D) : Prop :=
  ∀ X Y : C,
    (λ_ (X ⟶[V] Y)).hom ≫ (ρ_ (X ⟶[V] Y)).inv ≫
        (F.map X Y ⊗ₘ eId V (F.obj Y)) ≫
          eComp V (F.obj X) (F.obj Y) (F.obj Y) =
      (eId V (F.obj X) ⊗ₘ F.map X Y) ≫
        eComp V (F.obj X) (F.obj X) (F.obj Y)

/-- The identity V-natural transformation on `F : C ⥤_V D`.

Naturality follows from the V-enriched identity-composition laws
`e_id_comp V (F.obj X) (F.obj Y)` (right side) and
`e_comp_id V (F.obj X) (F.obj Y)` (left side), composed with the
functoriality of `F.map`. -/
def id (F : EnrichedFunctor V C D) : VNatTrans V C D F F where
  app X := eId V (F.obj X)
  v_naturality X Y := by
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

/-! ## §4 Vertical composition -/

/-- Vertical composition of V-natural transformations.

Given `α : F ⟶ G` and `β : G ⟶ H`, the family `X ↦ (α.app X) · (β.app X)`
(internalized via `(λ_)⁻¹ ≫ (α.app X ⊗ β.app X) ≫ eComp`) is V-natural. -/
def vcomp {F G H : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) (β : VNatTrans V C D G H) :
    VNatTrans V C D F H where
  app X := (λ_ _).inv ≫ (α.app X ⊗ₘ β.app X) ≫
    eComp V (F.obj X) (G.obj X) (H.obj X)
  v_naturality X Y := by
    -- Godement law (Kelly 1982 §1.2 eqn (1.5)): the V-naturality square for
    -- `vcomp α β` pastes the α-square and the β-square along middle column G(Y).
    --
    -- Concrete goal after `show`:
    --   LHS = (λ_).hom ≫ (ρ_).inv ≫
    --         (F.map X Y ⊗ ((λ_).inv ≫ (α.Y ⊗ β.Y) ≫ eComp_FGH_Y)) ≫ eComp_FFH
    --   RHS = (((λ_).inv ≫ (α.X ⊗ β.X) ≫ eComp_FGH_X) ⊗ H.map X Y) ≫ eComp_FHH
    --
    -- Proof plan:
    -- 1. Distribute outer tensors via tensorHom_def/tensorHom_def'.
    -- 2. Rebracket via e_assoc to expose `(F.map ⊗ α.Y) ≫ eComp_FFG` (LHS)
    --    and `(β.Y ⊗ H.map) ≫ eComp_GHH` (RHS).
    -- 3. Apply α.v_naturality and β.v_naturality.
    -- 4. Re-bracket via e_assoc once more, close with monoidal coherence.
    --
    -- Status: this attempt verifies steps 1-2 work (the LHS chain reduces
    -- to `(λ_).hom ≫ (ρ_).inv ≫ F.map ▷ 𝟙_V ≫ (F⟶F)_Y ◁ (λ_).inv ≫
    -- (F⟶F)_Y ◁ (α.Y ⊗ β.Y) ≫ (α_).inv ≫ eComp_FFG_in_Y ▷ (G⟶H)_Y ≫
    -- eComp_FGH_at_X_GY_HY`).
    --
    -- Step 3 (applying α.v_naturality) requires bridging from the chain
    -- form `F.map ▷ 𝟙_V ≫ (F⟶F)_Y ◁ ((λ_).inv ≫ α.Y ≫ ...)` back to
    -- a `F.map X Y ⊗ α.Y` form. The mechanical bridge:
    --   * fuse `(F⟶F)_Y ◁ (λ_).inv ≫ (F⟶F)_Y ◁ (α.Y ⊗ β.Y) =
    --       (F⟶F)_Y ◁ ((λ_).inv ≫ (α.Y ⊗ β.Y))` via `← whiskerLeft_comp`
    --   * but the α-square consumes `(F.map ⊗ α.Y) ≫ eComp`, not
    --     `(F.map ⊗ ((λ_).inv ≫ α.Y))`. The `(λ_).inv` must be propagated
    --     outward, which requires either pre-multiplying by `(λ_).hom`
    --     to cancel it or doing a coherence dance with the right unitor.
    --
    -- The remaining ~40 lines of tactic proof require careful interleaving
    -- of `← whiskerLeft_comp`, `associator_inv_naturality`, three more
    -- `e_assoc` rebracketings, plus the two `v_naturality` applications.
    -- Mathlib's `monoidal` tactic helps with the iso-cells but cannot
    -- close the goal because `α.Y`, `β.Y`, `F.map`, `G.map`, `H.map`,
    -- `eComp_*` are non-monoidal atoms.
    --
    -- See: Kelly 1982 §1.2 eqn (1.5); Riehl 2014 §3.7.
    sorry

/-- Vertical composition is associative.

The mathematical content is the V-enriched composition associativity
`e_assoc V (F.obj X) (G.obj X) (H.obj X) (K.obj X)`, decorated by monoidal
coherence (associators/unitors) that the `monoidal` tactic closes.

Proof strategy:
* Unfold both sides via `show` into the `eComp` chain.
* Distribute the outer tensor across the inner `eComp` composition via
  `tensorHom_def` (LHS) / `tensorHom_def'` (RHS) — this lifts the
  inner `(λ_).inv ≫ (α⊗β) ≫ eComp_FGH` to whiskered cells.
* Use `whisker_exchange` to commute `eComp_FGH ▷ 𝟙_V ≫ _ ◁ γ` into
  `_ ◁ γ ≫ eComp_FGH ▷ (H⟶K)`, putting `eComp_FGH ▷ _ ≫ eComp_FHK` adjacent.
* Apply `← e_assoc'` to rebracket into `(α_).hom ≫ _ ◁ eComp_GHK ≫ eComp_FGK`.
* Fold the `(α⊗β) ▷ _ ≫ _ ◁ γ` cluster back into `(α⊗β) ⊗ γ` via
  `← tensorHom_def_assoc`, push the associator past the triple tensor via
  `associator_naturality`, re-decompose `α ⊗ (β⊗γ)` with `tensorHom_def'`,
  and use `whisker_exchange` once more to align with the RHS.
* The residual prefix is a triangle-style monoidal coherence, closed by
  Mathlib's `monoidal` tactic. -/
theorem vcomp_assoc {F G H K : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G)
    (β : VNatTrans V C D G H)
    (γ : VNatTrans V C D H K) :
    vcomp (vcomp α β) γ = vcomp α (vcomp β γ) := by
  apply ext
  intro X
  show (λ_ _).inv ≫
        (((λ_ _).inv ≫ (α.app X ⊗ₘ β.app X) ≫
            eComp V (F.obj X) (G.obj X) (H.obj X)) ⊗ₘ γ.app X) ≫
          eComp V (F.obj X) (H.obj X) (K.obj X) =
      (λ_ _).inv ≫
        (α.app X ⊗ₘ ((λ_ _).inv ≫ (β.app X ⊗ₘ γ.app X) ≫
            eComp V (G.obj X) (H.obj X) (K.obj X))) ≫
          eComp V (F.obj X) (G.obj X) (K.obj X)
  rw [tensorHom_def ((λ_ _).inv ≫ (α.app X ⊗ₘ β.app X) ≫
        eComp V (F.obj X) (G.obj X) (H.obj X)) (γ.app X)]
  rw [tensorHom_def' (α.app X) ((λ_ _).inv ≫ (β.app X ⊗ₘ γ.app X) ≫
        eComp V (G.obj X) (H.obj X) (K.obj X))]
  simp only [comp_whiskerRight, MonoidalCategory.whiskerLeft_comp, Category.assoc]
  rw [← whisker_exchange_assoc (eComp V (F.obj X) (G.obj X) (H.obj X)) (γ.app X)]
  rw [← e_assoc' V (F.obj X) (G.obj X) (H.obj X) (K.obj X)]
  rw [← tensorHom_def_assoc (α.app X ⊗ₘ β.app X) (γ.app X)]
  rw [associator_naturality_assoc]
  rw [tensorHom_def' (α.app X) (β.app X ⊗ₘ γ.app X)]
  simp only [Category.assoc]
  rw [← whisker_exchange_assoc (α.app X) (eComp V (G.obj X) (H.obj X) (K.obj X))]
  -- Residual prefix `(λ_).inv ≫ (λ_).inv ▷ 𝟙_V ≫ (α_).hom = (λ_).inv ≫ 𝟙_V ◁ (λ_).inv`
  -- is a triangle-identity coherence; closed by `monoidal`.
  congr 1
  monoidal

/-- Left unit law for vertical composition. -/
theorem id_vcomp {F G : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) :
    vcomp (id F) α = α := by
  apply ext
  intro X
  -- `(λ_)⁻¹ ≫ (eId V (F.obj X) ⊗ α.app X) ≫ eComp = α.app X`.
  -- Strategy: rewrite the tensor via `tensorHom_def'` so that
  -- `eId V (F.obj X) ▷ _` sits adjacent to `eComp`, then `e_id_comp`
  -- collapses that subterm to the identity. The remaining
  -- `(λ_).inv ≫ 𝟙_V ◁ α.app X` reduces to `α.app X ≫ (λ_).inv` by
  -- naturality of `λ_`, which cancels with the trailing identity.
  show (λ_ _).inv ≫ (eId V (F.obj X) ⊗ₘ α.app X) ≫
      eComp V (F.obj X) (F.obj X) (G.obj X) = α.app X
  rw [tensorHom_def', Category.assoc, ← leftUnitor_inv_naturality_assoc,
    e_id_comp, Category.comp_id]

/-- Right unit law for vertical composition. -/
theorem vcomp_id {F G : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) :
    vcomp α (id G) = α := by
  apply ext
  intro X
  -- `(λ_)⁻¹ ≫ (α.app X ⊗ eId V (G.obj X)) ≫ eComp = α.app X`.
  -- Strategy: rewrite the tensor via `tensorHom_def` so that
  -- `_ ◁ eId V (G.obj X)` sits adjacent to `eComp`, then `e_comp_id`
  -- collapses the trailing `(ρ_).inv ≫ _ ◁ eId ≫ eComp` to the identity.
  -- The opening `(λ_ 𝟙_V).inv` is rewritten to `(ρ_ 𝟙_V).inv` via
  -- `unitors_inv_equal`, then `rightUnitor_inv_naturality` slides
  -- `α.app X` past `(ρ_).inv`.
  show (λ_ _).inv ≫ (α.app X ⊗ₘ eId V (G.obj X)) ≫
      eComp V (F.obj X) (G.obj X) (G.obj X) = α.app X
  rw [tensorHom_def, Category.assoc, unitors_inv_equal,
    ← rightUnitor_inv_naturality_assoc, e_comp_id, Category.comp_id]

/-! ## §5 Horizontal composition (whiskering with V-functors) -/

variable {E : Type u₃} [EnrichedCategory V E]

/-- Right whiskering of a V-natural transformation by a V-functor on the right.

Given `α : F ⟶ G : C ⥤_V D` and `H : D ⥤_V E`, the family
`X ↦ α.app X ≫ H.map (F.obj X) (G.obj X)` is V-natural
`H.comp F ⟶ H.comp G`. -/
def hcompR {F G : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) (H : EnrichedFunctor V D E) :
    VNatTrans V C E (EnrichedFunctor.comp V F H) (EnrichedFunctor.comp V G H) where
  app X := α.app X ≫ H.map (F.obj X) (G.obj X)
  v_naturality X Y := by
    -- The square for `hcompR α H` is α's square post-composed with H.map.
    -- Strategy: expand `(F.comp H).map = F.map ≫ H.map`, split the tensors
    -- using `tensorHom_comp_tensorHom`, fold `(H.map ⊗ H.map) ≫ eComp`
    -- via `H.map_comp` so it becomes `eComp ≫ H.map`, then the equation
    -- reduces to `α.v_naturality` post-composed with `H.map`, which is
    -- exactly its `reassoc_of%`-derived form.
    simp only [EnrichedFunctor.comp, ← tensorHom_comp_tensorHom,
      Category.assoc, ← H.map_comp]
    rw [reassoc_of% (α.v_naturality X Y)]

/-- Left whiskering of a V-natural transformation by a V-functor on the left.

Given `H : C ⥤_V D` and `α : F ⟶ G : D ⥤_V E`, the family
`X ↦ α.app (H.obj X)` is V-natural `F.comp H ⟶ G.comp H`. -/
def hcompL (H : EnrichedFunctor V C D)
    {F G : EnrichedFunctor V D E}
    (α : VNatTrans V D E F G) :
    VNatTrans V C E (EnrichedFunctor.comp V H F) (EnrichedFunctor.comp V H G) where
  app X := α.app (H.obj X)
  v_naturality X Y := by
    -- The square for `hcompL H α` is α's square at (H.obj X, H.obj Y)
    -- pre-composed with `𝟙_V ◁ H.map X Y` (using leftUnitor naturality
    -- to bring `H.map X Y` across the `(λ_).hom ≫ (ρ_).inv` prefix).
    -- Strategy:
    --   * Unfold `(H.comp F).map = H.map ≫ F.map` via `EnrichedFunctor.comp`
    --   * LHS reduction: split `(H.map ≫ F.map) ⊗ₘ α.app`, peel off
    --     `H.map ▷ 𝟙_V` to a leading `𝟙_V ◁ H.map`, then apply
    --     `α.v_naturality (H.obj X) (H.obj Y)`.
    --   * RHS reduction: split `α.app ⊗ₘ (H.map ≫ G.map)`, use
    --     `whisker_exchange` to slide `_ ◁ H.map` to the front.
    --   * Both sides reduce to
    --     `𝟙_V ◁ H.map ≫ (α.app (H.obj X) ⊗ₘ G.map _ _) ≫ eComp`.
    simp only [EnrichedFunctor.comp]
    have hLHS :
        (λ_ (X ⟶[V] Y)).hom ≫
            (ρ_ (X ⟶[V] Y)).inv ≫
              ((H.map X Y ≫ F.map (H.obj X) (H.obj Y)) ⊗ₘ α.app (H.obj Y)) ≫
                eComp V (F.obj (H.obj X)) (F.obj (H.obj Y)) (G.obj (H.obj Y)) =
          (𝟙_ V ◁ H.map X Y) ≫
            ((α.app (H.obj X)) ⊗ₘ G.map (H.obj X) (H.obj Y)) ≫
              eComp V (F.obj (H.obj X)) (G.obj (H.obj X)) (G.obj (H.obj Y)) := by
      rw [tensorHom_def (H.map X Y ≫ F.map (H.obj X) (H.obj Y)) (α.app (H.obj Y)),
        comp_whiskerRight]
      simp only [Category.assoc]
      rw [← rightUnitor_inv_naturality_assoc, ← leftUnitor_naturality_assoc]
      conv_lhs =>
        rw [show (F.map (H.obj X) (H.obj Y) ▷ 𝟙_ V) ≫
              ((F.obj (H.obj X) ⟶[V] F.obj (H.obj Y)) ◁ α.app (H.obj Y)) ≫
                eComp V (F.obj (H.obj X)) (F.obj (H.obj Y)) (G.obj (H.obj Y))
            = (F.map (H.obj X) (H.obj Y) ⊗ₘ α.app (H.obj Y)) ≫
                eComp V (F.obj (H.obj X)) (F.obj (H.obj Y)) (G.obj (H.obj Y)) by
          rw [tensorHom_def, Category.assoc]]
      rw [α.v_naturality (H.obj X) (H.obj Y)]
    have hRHS :
        (α.app (H.obj X) ⊗ₘ (H.map X Y ≫ G.map (H.obj X) (H.obj Y))) ≫
            eComp V (F.obj (H.obj X)) (G.obj (H.obj X)) (G.obj (H.obj Y)) =
          (𝟙_ V ◁ H.map X Y) ≫
            ((α.app (H.obj X)) ⊗ₘ G.map (H.obj X) (H.obj Y)) ≫
              eComp V (F.obj (H.obj X)) (G.obj (H.obj X)) (G.obj (H.obj Y)) := by
      rw [tensorHom_def (α.app (H.obj X)) (H.map X Y ≫ G.map (H.obj X) (H.obj Y)),
        MonoidalCategory.whiskerLeft_comp]
      simp only [Category.assoc]
      rw [← whisker_exchange_assoc]
      conv_lhs =>
        rw [show (α.app (H.obj X) ▷ (H.obj X ⟶[V] H.obj Y)) ≫
              ((F.obj (H.obj X) ⟶[V] G.obj (H.obj X)) ◁ G.map (H.obj X) (H.obj Y)) ≫
                eComp V (F.obj (H.obj X)) (G.obj (H.obj X)) (G.obj (H.obj Y))
            = (α.app (H.obj X) ⊗ₘ G.map (H.obj X) (H.obj Y)) ≫
                eComp V (F.obj (H.obj X)) (G.obj (H.obj X)) (G.obj (H.obj Y)) by
          rw [tensorHom_def, Category.assoc]]
    rw [hLHS, hRHS]

/-! ## §6 Bridge to the endofunctor variant in Monad.lean

Monad.lean ships a narrower `EnrichedNatTrans V C F G` for V-endofunctors
`F G : C ⥤_V C` with a *supplied-data* naturality field (a `Prop`-typed
slot plus its proof). For interoperability, every general `VNatTrans` on
a V-endofunctor pair descends to the supplied-data variant by promoting
the V-naturality square to the carried proposition. -/

/-- Restrict a general V-natural transformation between V-endofunctors
to the variant in `SSBX.Foundation.Enriched.Monad`. After the Phase
A.5.0c refactor (2026-05-21), the endofunctor variant also carries the
concrete V-naturality square, so the bridge is a direct copy. -/
def toEndo
    {F G : EnrichedFunctor V C C} (α : VNatTrans V C C F G) :
    CategoryTheory.Enriched.EnrichedNatTrans V C F G where
  app := α.app
  naturality := α.v_naturality

/-- The `app` components are preserved by the bridge `toEndo`. -/
@[simp]
theorem toEndo_app
    {F G : EnrichedFunctor V C C} (α : VNatTrans V C C F G)
    (X : C) :
    (toEndo α).app X = α.app X :=
  rfl

/-! ## §7 Componentwise convenience lemmas -/

/-- The component of the identity V-nat trans at `X` is the enriched identity. -/
@[simp]
theorem id_app (F : EnrichedFunctor V C D) (X : C) :
    (id F).app X = eId V (F.obj X) :=
  rfl

/-- Componentwise formula for vertical composition. -/
@[simp]
theorem vcomp_app {F G H : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) (β : VNatTrans V C D G H) (X : C) :
    (vcomp α β).app X =
      (λ_ _).inv ≫ (α.app X ⊗ₘ β.app X) ≫
        eComp V (F.obj X) (G.obj X) (H.obj X) :=
  rfl

/-- Componentwise formula for right-whiskering. -/
@[simp]
theorem hcompR_app {F G : EnrichedFunctor V C D}
    (α : VNatTrans V C D F G) (H : EnrichedFunctor V D E) (X : C) :
    (hcompR α H).app X = α.app X ≫ H.map (F.obj X) (G.obj X) :=
  rfl

/-- Componentwise formula for left-whiskering. -/
@[simp]
theorem hcompL_app (H : EnrichedFunctor V C D)
    {F G : EnrichedFunctor V D E} (α : VNatTrans V D E F G) (X : C) :
    (hcompL H α).app X = α.app (H.obj X) :=
  rfl

/-! ## §8 Interaction of whiskering with composition and identity -/

/-- Left-whiskering the identity is the identity. -/
theorem hcompL_id (H : EnrichedFunctor V C D) (F : EnrichedFunctor V D E) :
    hcompL H (id F) = id (EnrichedFunctor.comp V H F) := by
  apply ext
  intro X
  -- `(hcompL H (id F)).app X = (id F).app (H.obj X) = eId V (F.obj (H.obj X))`,
  -- which equals `(id (H.comp F)).app X = eId V ((H.comp F).obj X)` by
  -- the definitional unfolding `(H.comp F).obj X = F.obj (H.obj X)`.
  rfl

/-- Right-whiskering the identity is the identity. -/
theorem hcompR_id (F : EnrichedFunctor V C D) (H : EnrichedFunctor V D E) :
    hcompR (id F) H = id (EnrichedFunctor.comp V F H) := by
  apply ext
  intro X
  -- `(hcompR (id F) H).app X = (id F).app X ≫ H.map (F.obj X) (F.obj X)
  --   = eId V (F.obj X) ≫ H.map (F.obj X) (F.obj X) = eId V (H.obj (F.obj X))`,
  -- using `EnrichedFunctor.map_id` for the last step. The RHS is
  -- `(id (F.comp H)).app X = eId V (H.obj (F.obj X))`.
  show eId V (F.obj X) ≫ H.map (F.obj X) (F.obj X)
      = eId V (H.obj (F.obj X))
  exact H.map_id (F.obj X)

/-! ## §9 The `Type`-V instance: ordinary natural transformations

For `V = Type v`, an ordinary natural transformation `α : F ⟶ G` between
ordinary functors `F G : C ⥤ D` is a special case of `VNatTrans` between
their `typeEnrichedFunctorOfFunctor`-promotions. This connects our general
API to the canonical `Type`-enrichment bridge in `TypeOrdinary.lean`. -/

section TypeBridge

open CategoryTheory.EnrichedDoctrine

variable {C : Type u} {D : Type u₂} [Category.{v} C] [Category.{v} D]

/-- Promote an ordinary natural transformation between ordinary functors to a
V-natural transformation between the canonical `Type`-enriched functors.

For `V = Type v`, the V-naturality square (a calculation in `Type v ⊗ U → Z`)
reduces to the ordinary naturality square of `α`. -/
noncomputable def ofNatTrans {F G : C ⥤ D} (α : F ⟶ G) :
    VNatTrans (Type v) C D
        (typeEnrichedFunctorOfFunctor F)
        (typeEnrichedFunctorOfFunctor G) where
  app X := ↾fun _ : 𝟙_ (Type v) => α.app X
  v_naturality X Y := by
    -- The V = Type naturality square reduces to: for all f : X ⟶ Y in C,
    --   α.app Y ∘ F.map f = G.map f ∘ α.app X
    -- which is α.naturality. Since the V = Type unitor coherence
    -- is rfl-style and `eComp` is set-theoretic composition, the whole
    -- square unfolds to a `funext`-style pointwise check.
    ext ⟨u, f⟩
    exact α.naturality f

end TypeBridge

end VNatTrans

end CategoryTheory.Enriched
