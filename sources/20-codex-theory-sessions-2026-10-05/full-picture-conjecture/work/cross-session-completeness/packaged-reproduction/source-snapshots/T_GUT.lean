/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / GUT-C Path C
-/
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Iso
import Mathlib.CategoryTheory.Endomorphism
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Limits.Shapes.Terminal
import Mathlib.CategoryTheory.Limits.Shapes.Biproducts
import SSBX.Foundation.R.Scope

/-!
# Foundation.Doctrine.T_GUT — The T_GUT Lawvere theory (skeleton)

**Reference**: `docs-next/00_start/gut-c-doctrine.md` v0.2 §§3.3, 3.4, 3.5.

This file provides the **API surface** of the proposed `T_GUT` enriched
Lawvere theory underpinning the GUT-C Universal Sayability theorem. The
free enriched-theory quotient and naturality across realisation morphisms
remain future infrastructure; the carrier, structural, core-generator,
and current standard-law adequacy package are formalised below without
`sorry`.

## Doctrinal anchor

Per `gut-c-doctrine.md` v0.2 §3.3 the T_GUT theory is presented by an
indexed family of generators, one for each P-property:

| Generator | Arity / type | Encodes |
|---|---|---|
| `id_δ : δ_T → δ_T`                                       | (1, 1)              | P1 (distinction) |
| `compose N M : δ_T^⊗N ⊗ δ_T^⊗M → δ_T^⊗(N+M)`             | (N+M, N+M)          | P2 (composition) |
| `morP3 N M : δ_T^⊗N → δ_T^⊗M`                            | (N, M)              | P3 (relations) |
| `square N : δ_T^⊗N → δ_T^⊗(2N)`                           | (N, 2N)             | P4 (scale) |
| `hom N M : (δ_T^⊗N ⊸ δ_T^⊗M) → δ_T^⊗(N·M)`               | (N*M, N*M)          | P5 (Hom-as-content) |
| `modal_V4 : δ_T → δ_T^⊗2 ⊗ δ_T^⊗2`                       | (1, 4)              | P6 (V₄ modality) |
| `invo3 : δ_T^⊗3 → δ_T^⊗3` with `invo3 ∘ invo3 = id`    | (3, 3)              | P7a (involution) |
| `iso4 : δ_T^⊗4 ≅ End(δ_T^⊗2)`                    | (4, 4)              | P7b (generalized) |

The equational laws encode the *intended categorical content* of each
generator (associativity for `compose`, diagonal compatibility for
`square`, involutivity for `invo3`, naturality / iso conditions for
`iso4`, etc.).

## Scope

* `TGUTOp`  — the syntactic signature of generators (an `inductive`)
* `TGUTOp.arity` — the (input, output) δ-tensor-power arities
* `TGUTLaw` — the equational laws as a syntactic `inductive`
* `TGUTPresentation` — bundles signature + laws (a record)
* `TGUTRealisation C δ` — a *realisation* in an ambient SMCC `C` at
  generator object `δ`: it is an `ℕ`-indexed family of objects of `C`
  with the structural coherences making it a candidate `T_GUT`-model
* `TGUTRealisation.canonical` — the canonical tensor-power realisation
  `n ↦ δ^⊗n` in any SMCC `C` with chosen `δ`
* `TGUTRealisation.componentIso` — the layer-by-layer component iso
  `M.R n ≅ tensorPow δ n`, by induction on `n` using
  `R_unit / R_gen / R_tensor`
* `TGUTRealisation.universal_sayability` — legacy carrier/component
  theorem using the old `RealIso` API
* `TGUTRealisation.universal_sayability_core_full` — full core
  carrier/generator transport from adequacy plus canonical-transport data
* `TGUTRealisation.universal_sayability_complete_of_adequate` — scoped
  law-package theorem from intrinsic adequacy plus explicit transport,
  semantic, and ops predicates

## Design decisions

1. **SMCC vs Cartesian**: we target generic symmetric monoidal `C`
   rather than the cartesian case, because:
   * the GUT-A/B base `FinVect_{F_q}` is intrinsically *not* cartesian
     (tensor product is not the categorical product there)
   * `gut-c-doctrine.md` v0.2 §3.3 explicitly cites SMCC + biproducts
   * the quantum instance (FdHilb) requires a non-cartesian tensor
   `HasFiniteBiproducts C` is kept as a separate hypothesis where needed
   (it gives the "direct-sum" interpretation of `compose`).

2. **Generators as syntactic terms, equations as separate `Prop`s**: we
   keep `TGUTOp` and `TGUTLaw` as plain `inductive`s rather than packaging
   them as a free-V-category modulo equations. The free-V-category
   construction depends on infrastructure (`LawvereTheory`, weighted
   enriched limits) that is *not* yet in Mathlib (cf. §11.1 PR-2 and
   §11.1 PR-3 of `gut-c-doctrine.md` v0.2). When that infrastructure
   lands, the construction in §6 below ports trivially to it.

3. **Realisation as a record, model as an isomorphism**: a
   `TGUTRealisation C δ` is a record bundling the structural data of a
   would-be T_GUT-model (the underlying ℕ-indexed family + the seven
   generator morphisms). The Universal Sayability theorem states that
   any such realisation is *isomorphic* (in the appropriate sense) to
   the canonical tensor-power realisation. The structural part of the
   isomorphism (component family `M.R n ≅ tensorPow δ n`) is proven
   here by induction on `n` (see `componentIso`). Non-vacuous coherence
   now lives in `CoherentCoreRealIso`, `FullCoherentCoreRealIso`, and
   `CompleteUniversalSayability`; the older `RealIso` wrapper is
   deliberately carrier-only.

4. **Independence from G1**: per the task spec we depend only on Mathlib
   primitives, *not* on any GUT-C `LawvereTheory` typeclass. This keeps
   the file building in the current Mathlib snapshot.

## Status

Build target: `lake build SSBX.Foundation.Doctrine.T_GUT` succeeds. The
legacy carrier theorem, archived structural theorem, scoped full-core
theorem, and split current-law package are all formalised. Remaining
work is per-instance: prove `IsAdequate` for concrete realisations,
prove any claimed canonical transport / semantic / ops predicates where
they are actually true, prove ops equivalence where a meaningful ops
target exists, and extend the new realisation-morphism naturality API
with any needed composition/functoriality laws.
-/

namespace SSBX.Foundation.Doctrine

open CategoryTheory MonoidalCategory CategoryTheory.Limits

universe v u

/-! ## § 1 Signature — the generators of T_GUT

Per `gut-c-doctrine.md` v0.2 §3.3 the T_GUT theory has eight generator
families. We encode them as a flat `inductive`, indexed by the natural
numbers controlling the relevant tensor powers.
-/

/-- The signature of `T_GUT`: an indexed family of operations.

Each constructor corresponds to a row in the §3.3 generator table of
`gut-c-doctrine.md` v0.2. The arities are recorded by `TGUTOp.arity`
(see below). -/
inductive TGUTOp : Type
  /-- `id_δ : δ_T → δ_T` — the distinction identity (encodes P1). -/
  | id_δ : TGUTOp
  /-- `compose N M : δ_T^⊗N ⊗ δ_T^⊗M → δ_T^⊗(N+M)` —
      direct-sum embedding (encodes P2). -/
  | compose : ℕ → ℕ → TGUTOp
  /-- `square N : δ_T^⊗N → δ_T^⊗(2N)` —
      doubling / squaring (encodes P4). -/
  | square : ℕ → TGUTOp
  /-- `hom N M : (δ_T^⊗N ⊸ δ_T^⊗M) → δ_T^⊗(N·M)` —
      Hom-as-content (encodes P5). -/
  | hom : ℕ → ℕ → TGUTOp
  /-- `modal_V4 : δ_T → δ_T^⊗2 ⊗ δ_T^⊗2` —
      V₄ four-modality embedding (encodes P6, conditional). -/
  | modal_V4 : TGUTOp
  /-- `invo3 : δ_T^⊗3 → δ_T^⊗3` with `invo3 ∘ invo3 = id` —
      aspect involution (encodes P7a). -/
  | invo3 : TGUTOp
  /-- `iso4 : δ_T^⊗4 ≅ End(δ_T^⊗2)` —
      Wedderburn-style endomorphism iso (encodes P7b, generalized). -/
  | iso4 : TGUTOp
  /-- `morP3 N M : δ_T^⊗N → δ_T^⊗M` — generic morphism family
      (encodes P3 relations / bilinear classifications). -/
  | morP3 : ℕ → ℕ → TGUTOp
  deriving DecidableEq, Repr

namespace TGUTOp

/-! ## § 2 Arity — input and output δ-tensor-power indices

For an operation `g : TGUTOp`, `g.arity = (n, m)` means
`g : δ_T^⊗n → δ_T^⊗m` in any T_GUT-model. The Hom-as-content
constructor `hom N M` represents `(δ^⊗N ⊸ δ^⊗M)` *as* `δ^⊗(N·M)`,
which is why its input and output arities both equal `N · M`.
-/

/-- The (input arity, output arity) of each T_GUT generator, expressed
in δ-tensor-power indices. -/
def arity : TGUTOp → ℕ × ℕ
  | .id_δ          => (1, 1)
  | .compose N M   => (N + M, N + M)
  | .square N      => (N, 2 * N)
  | .hom N M       => (N * M, N * M)
  | .modal_V4      => (1, 4)
  | .invo3        => (3, 3)
  | .iso4  => (4, 4)
  | .morP3 N M    => (N, M)

/-- Input arity of a generator. -/
def src (g : TGUTOp) : ℕ := g.arity.1

/-- Output arity of a generator. -/
def tgt (g : TGUTOp) : ℕ := g.arity.2

@[simp] theorem src_id_δ : (id_δ).src = 1 := rfl
@[simp] theorem tgt_id_δ : (id_δ).tgt = 1 := rfl
@[simp] theorem src_compose (N M : ℕ) : (compose N M).src = N + M := rfl
@[simp] theorem tgt_compose (N M : ℕ) : (compose N M).tgt = N + M := rfl
@[simp] theorem src_square (N : ℕ) : (square N).src = N := rfl
@[simp] theorem tgt_square (N : ℕ) : (square N).tgt = 2 * N := rfl
@[simp] theorem src_hom (N M : ℕ) : (hom N M).src = N * M := rfl
@[simp] theorem tgt_hom (N M : ℕ) : (hom N M).tgt = N * M := rfl
@[simp] theorem src_modal_V4 : (modal_V4).src = 1 := rfl
@[simp] theorem tgt_modal_V4 : (modal_V4).tgt = 4 := rfl
@[simp] theorem src_invo3 : (invo3).src = 3 := rfl
@[simp] theorem tgt_invo3 : (invo3).tgt = 3 := rfl
@[simp] theorem src_iso4 : (iso4).src = 4 := rfl
@[simp] theorem tgt_iso4 : (iso4).tgt = 4 := rfl
@[simp] theorem src_relate (N M : ℕ) : (morP3 N M).src = N := rfl
@[simp] theorem tgt_relate (N M : ℕ) : (morP3 N M).tgt = M := rfl

/-- The full list of "structural" T_GUT generators (excluding the
parametric families). Useful for case analyses on the generator
type up to choice of indices. -/
def atomic : List TGUTOp :=
  [.id_δ, .modal_V4, .invo3, .iso4]

end TGUTOp

/-! ## § 3 Equational laws

These are the equations imposed on the free SMCC-enriched theory
generated by `TGUTOp`. Each is recorded here as a syntactic tag; the
*semantic content* (i.e., when a realisation `R` of T_GUT in a base
SMCC `C` is said to *satisfy* the law) is registered in §5 via
`TGUTRealisation.Satisfies`.

Per `gut-c-doctrine.md` v0.2 §3.3 the list below covers the explicitly
named laws; additional naturality / coherence laws will be added during
γ.1's full Lawvere presentation. -/

/-- The equational laws of T_GUT. -/
inductive TGUTLaw : Type
  /-- `invo3 ∘ invo3 = id_{δ^⊗3}` — P7a involutivity. -/
  | invo3_involutive : TGUTLaw
  /-- `square_N = (id ⊗ id) ∘ Δ_N`, the diagonal compatibility (P4). -/
  | square_diagonal : ℕ → TGUTLaw
  /-- `compose N M` is the inverse of the structural tensor decomposition
      `R_tensor N M`. This is the local law that connects the generator
      interpretation of composition to carrier additivity. -/
  | compose_tensor_inverse : ℕ → ℕ → TGUTLaw
  /-- `hom N M` transports along the canonical carrier iso to the canonical
      Hom generator. This is the explicit core-generator coherence law for P5. -/
  | hom_canonical_transport : ℕ → ℕ → TGUTLaw
  /-- `invo3` transports along the canonical carrier iso to the canonical
      atom generator. This is stronger than mere involutivity and records
      the core-generator square needed by full carrier coherence. -/
  | invo3_canonical_transport : TGUTLaw
  /-- `iso4` transports along the canonical carrier iso to the
      canonical Wedderburn generator. The end-object semantics remain a
      separate obligation; this law records the core carrier square. -/
  | iso4_canonical_transport : TGUTLaw
  /-- `R_tensor 0 N` agrees with `R_unit` and the left unitor. -/
  | tensor_unit_left : ℕ → TGUTLaw
  /-- `R_tensor N 0` agrees with `R_unit` and the right unitor. -/
  | tensor_unit_right : ℕ → TGUTLaw
  /-- `R_tensor` is associative up to the ambient associator. -/
  | tensor_assoc : ℕ → ℕ → ℕ → TGUTLaw
  /-- `compose` is associative:
      `compose (N+M) K ∘ (compose N M ⊗ id) = compose N (M+K) ∘ (id ⊗ compose M K)`. -/
  | compose_assoc : ℕ → ℕ → ℕ → TGUTLaw
  /-- `compose N 0 = id_{δ^⊗N}` (right unit) — `compose` is unital. -/
  | compose_unit_right : ℕ → TGUTLaw
  /-- `compose 0 M = id_{δ^⊗M}` (left unit) — `compose` is unital. -/
  | compose_unit_left : ℕ → TGUTLaw
  /-- `hom_NM ∘ curry_NM = id` — the Hom-as-content compatibility (P5).
      Internally: `hom N M` is the inverse of the curry-isomorphism
      `(δ^⊗N ⊸ δ^⊗M) ≅ δ^⊗(N·M)`. -/
  | hom_NM_curry_compat : ℕ → ℕ → TGUTLaw
  /-- `iso4 ∘ iso4⁻¹ = id` plus naturality —
      Wedderburn invariance (P7b). -/
  | iso4_iso : TGUTLaw
  /-- `modal_V4 ∘ modal_V4` factors through `id ⊗ id` —
      V₄ idempotency on the modality lattice (P6). -/
  | modal_V4_idempotent : TGUTLaw
  deriving DecidableEq, Repr

/-! ## § 4 Presentation — bundling signature + laws

We package the signature `TGUTOp` together with a law predicate on
`TGUTLaw` as a single `TGUTPresentation`. The predicate shape is
intentional: several T_GUT laws are parametric families indexed by
natural numbers, so a finite list cannot express the standard
presentation. In a future revision (once `LawvereTheory` is in Mathlib,
PR-2 of §11.1 of the doctrine doc), this presentation will quotient the
free SMCC-enriched theory.
-/

/-- A *presentation* of T_GUT bundles the syntactic signature and the
equational laws. This is the data of a Lawvere theory *modulo* the
quotient construction that turns it into a small V-category. -/
structure TGUTPresentation : Type where
  /-- The generators (signature). -/
  ops : List TGUTOp
  /-- The equational laws, as a predicate so parametric law families are included. -/
  laws : TGUTLaw → Prop

/-- The intrinsic `T_GUT` presentation used by `IsAdequate`.

This includes the carrier-parametric laws that are not comparison-specific
and are expected to be satisfiable by the concrete instance files.  It
deliberately excludes:

* canonical transport laws, which compare a model to `canonical δ`;
* semantic Hom/Wedderburn laws, which require represented Hom/end-object
  infrastructure and are intentionally not interpreted as all functions
  in the current cartesian `Type 0` carrier readings;
* ops-level laws for `square` and `modal_V4`, which remain per-instance. -/
def TGUTPresentation.standard : TGUTPresentation where
  ops :=
    [.id_δ, .modal_V4, .invo3, .iso4]
    -- Parametric families are conceptually included for *every*
    -- `(N, M) : ℕ × ℕ`; we record the atomic ops here for inspection.
  laws := fun
    | .invo3_involutive => True
    | .compose_tensor_inverse _ _ => True
    | .tensor_unit_left _ => True
    | .tensor_unit_right _ => True
    | .tensor_assoc _ _ _ => True
    | .compose_assoc _ _ _ => True
    | .compose_unit_right _ => True
    | .compose_unit_left _ => True
    | _ => False

/-- Canonical-comparison laws for the particular comparison map
`componentIso δ M`.

These are not intrinsic laws of a realisation.  In particular,
`invo3_canonical_transport` would force any transported atom map to be
the canonical atom map.  The canonical atom is now the generic symmetric
three-factor reversal, so primary TypeCat R-family instances can use the
same coordinate reversal without adding semantic names to the core. -/
def TGUTPresentation.canonicalTransport : TGUTPresentation where
  ops := [.hom 0 0, .invo3, .iso4]
  laws := fun
    | .hom_canonical_transport _ _ => True
    | .invo3_canonical_transport => True
    | .iso4_canonical_transport => True
    | _ => False

/-- Semantic laws that require represented Hom/end-object interpretation
data beyond the current carrier-level instance files. -/
def TGUTPresentation.semantic : TGUTPresentation where
  ops := [.hom 0 0, .iso4]
  laws := fun
    | .hom_NM_curry_compat _ _ => True
    | .iso4_iso => True
    | _ => False

/-- Per-instance operational laws.  These are intentionally separate from
the universal core because `square` and `modal_V4` are not canonical in an
arbitrary SMCC. -/
def TGUTPresentation.opsCoherence : TGUTPresentation where
  ops := [.modal_V4]
  laws := fun
    | .square_diagonal _ => True
    | .modal_V4_idempotent => True
    | _ => False

/-! ## § 5 Realisations in a symmetric monoidal category

A *realisation* of `T_GUT` in a symmetric monoidal category `C` at a
chosen generator object `δ : C` is the data of an `ℕ`-indexed
family of objects `R : ℕ → C` (interpreting the abstract `δ_T^⊗n`)
together with morphisms interpreting each generator and the structural
coherences that say `R 0 = ⊤` (or `𝟙_ C`), `R 1 = δ`, and
`R (n + m) ≅ R n ⊗ R m`.

This is essentially the *forgetful* shape of a T_GUT-model: it does
*not* require the equational laws (§3) to be discharged. A realisation
that satisfies the laws is what `TGUTRealisation.Satisfies` records.
-/

variable (C : Type u) [Category.{v} C]

variable [MonoidalCategory C] in
/-- A `TGUTRealisationCore C δ` is the **universal / structural** data of
a T_GUT realisation in `C` at the chosen generator `δ`. Per the §3.3
table this contains the fields that admit a *canonical* universal
construction in any SMCC:

* `R n` interprets the abstract object `δ_T^⊗n`
* `R_unit : R 0 ≅ 𝟙_ C` — the empty tensor power is the monoidal unit
* `R_gen : R 1 ≅ δ` — the generator is `δ`
* `R_tensor n m : R (n + m) ≅ R n ⊗ R m` — tensor-power additivity
* `compose_mor N M : R N ⊗ R M ⟶ R (N + M)` — inverse of additivity
* `hom_mor N M`     — `R (N · M) ⟶ R (N · M)`, the curry identification
* `invo3_mor`      — the `δ^⊗3 → δ^⊗3` involution carrier (the
  canonical realisation uses symmetric three-factor reversal)
* `iso4_mor`— the `δ^⊗4 ≅ δ^⊗4` Wedderburn iso carrier

**Doctrinal change (2026-05-17, Option A refactor)**: the three
*instance-specific* morphisms `square_mor`, `morP3_mor`, `modal_V4_mor`
have been factored out into `TGUTRealisationOps` (below) because they
have **no canonical universal definition** in a general SMCC (a general
SMCC has no diagonal `δ ⟶ δ ⊗ δ` and no canonical map between distinct
tensor powers — see the docstring of `TGUTRealisation.canonical`). This
honest split removes 3 `sorry`s from `canonical` and re-localises them
to per-instance constructors where they are mathematically meaningful.

A realisation is **not** required to satisfy the equational laws
(§3); that condition is recorded separately as
`TGUTRealisation.Satisfies` (see below). -/
structure TGUTRealisationCore (δ : C) where
  /-- The underlying `ℕ`-indexed family of objects: `R n` interprets
      `δ_T^⊗n`. -/
  R : ℕ → C
  /-- `R 0 ≅ 𝟙_ C`: the empty tensor power is the monoidal unit. -/
  R_unit : R 0 ≅ 𝟙_ C
  /-- `R 1 ≅ δ`: the generator. -/
  R_gen : R 1 ≅ δ
  /-- `R (n + m) ≅ R n ⊗ R m`: tensor-power additivity. -/
  R_tensor : ∀ n m, R (n + m) ≅ R n ⊗ R m
  /-- Interpretation of `compose N M : δ^⊗N ⊗ δ^⊗M → δ^⊗(N+M)`. -/
  compose_mor : ∀ N M, R N ⊗ R M ⟶ R (N + M)
  /-- Interpretation of `hom N M : (δ^⊗N ⊸ δ^⊗M) → δ^⊗(N·M)`,
      represented (in the realisation) as an endomorphism of
      `R (N · M)` (the "curry-identification" lives in this morphism). -/
  hom_mor : ∀ N M, R (N * M) ⟶ R (N * M)
  /-- Interpretation of `invo3 : δ^⊗3 → δ^⊗3`. -/
  invo3_mor : R 3 ⟶ R 3
  /-- Interpretation of `iso4 : δ^⊗4 ≅ End(δ^⊗2)`,
      expressed as an isomorphism `R 4 ≅ R 2 ⟶ R 2 ↦ R 2` — concretely
      we record it as an iso `R 4 ≅ R (2 * 2)` (which collapses to
      `R 4 ≅ R 4` definitionally; the *non-trivial* content lives in
      `wedderburn_factors_through_End` below, registered in §5.1). -/
  iso4_mor : R 4 ≅ R 4

/-- The **instance-specific** operational layer attached to a
`TGUTRealisationCore`. These three morphisms have NO canonical
universal definition in a general SMCC — they require a per-base
choice (a diagonal, a bilinear form, a Pauli-type operator, etc.):

* `square_mor N : R N ⟶ R (2 * N)`     — needs a diagonal δ^N ⟶ δ^N ⊗ δ^N
* `morP3_mor N M : R N ⟶ R M`         — no canonical map between distinct tensor powers
* `modal_V4_mor : R 1 ⟶ R 2 ⊗ R 2`     — needs a diagonal δ ⟶ δ ⊗ δ

Per `gut-c-doctrine.md` v0.2 §3.5 these are *instance-specific* data,
not universal. The per-instance constructors live in
`Foundation/Doctrine/Instance/*` and supply real morphisms appropriate
to the chosen SMCC base (FinVect: F_q-bilinear duplication; HeytAlg:
meet diagonal; FdHilb: Pauli; Frm: frame diagonal). -/
structure TGUTRealisationOps {δ : C} [MonoidalCategory C]
    (M : TGUTRealisationCore C δ) where
  /-- Interpretation of `square N : δ^⊗N → δ^⊗(2N)`. -/
  square_mor : ∀ N, M.R N ⟶ M.R (2 * N)
  /-- Interpretation of `morP3 N M : δ^⊗N → δ^⊗M`. -/
  morP3_mor : ∀ N M_, M.R N ⟶ M.R M_
  /-- Interpretation of `modal_V4 : δ → δ^⊗2 ⊗ δ^⊗2`,
      i.e. `R 1 ⟶ R 2 ⊗ R 2`. The codomain is `R 2 ⊗ R 2`
      (= `R 4` up to `R_tensor 2 2`). -/
  modal_V4_mor : M.R 1 ⟶ M.R 2 ⊗ M.R 2

variable [MonoidalCategory C] in
/-- A **bundled** `TGUTRealisation C δ` = `Core` + `Ops`.

This is the back-compat layer: prior code that wrote
`M : TGUTRealisation C δ` and accessed `M.R / M.R_unit / … /
M.square_mor / M.morP3_mor / M.modal_V4_mor` continues to compile
because `extends TGUTRealisationCore C δ` inherits all 8 Core
projections and we re-export the 3 Ops projections inline.

Doctrinally, *prefer*  `TGUTRealisationCore C δ` for any new code
that does not need the Ops fields — universal_sayability is now stated
at Core level. -/
structure TGUTRealisation (δ : C) extends TGUTRealisationCore C δ where
  /-- Interpretation of `square N : δ^⊗N → δ^⊗(2N)`. -/
  square_mor : ∀ N, R N ⟶ R (2 * N)
  /-- Interpretation of `morP3 N M : δ^⊗N → δ^⊗M`. -/
  morP3_mor : ∀ N M, R N ⟶ R M
  /-- Interpretation of `modal_V4 : δ → δ^⊗2 ⊗ δ^⊗2`,
      i.e. `R 1 ⟶ R 2 ⊗ R 2`. The codomain is `R 2 ⊗ R 2`
      (= `R 4` up to `R_tensor 2 2`). -/
  modal_V4_mor : R 1 ⟶ R 2 ⊗ R 2

namespace TGUTRealisation

variable {C}

section
variable [MonoidalCategory C] {δ : C}

/-- Project a bundled `TGUTRealisation` to its instance-specific
operational layer `TGUTRealisationOps`. -/
def toOps (M : TGUTRealisation C δ) : TGUTRealisationOps C M.toTGUTRealisationCore where
  square_mor   := M.square_mor
  morP3_mor   := M.morP3_mor
  modal_V4_mor := M.modal_V4_mor

/-- Bundle a `Core` + `Ops` into a `TGUTRealisation`. -/
def ofCoreOps (M : TGUTRealisationCore C δ) (O : TGUTRealisationOps C M) :
    TGUTRealisation C δ where
  toTGUTRealisationCore := M
  square_mor   := O.square_mor
  morP3_mor   := O.morP3_mor
  modal_V4_mor := O.modal_V4_mor

/-! ### § 5.1 Generator dispatch

For each `g : TGUTOp` and each realisation `M`, dispatch `g` to the
corresponding morphism of `M`. The output lives in `M.R g.tgt`; the
input domain is `M.R g.src`. -/

/-- The interpretation of a syntactic generator `g : TGUTOp` in the
realisation `M`. The result lives in `M.R g.src ⟶ M.R g.tgt`. -/
noncomputable def interp (M : TGUTRealisation C δ) : ∀ (g : TGUTOp),
    M.R g.src ⟶ M.R g.tgt
  | .id_δ          => 𝟙 (M.R 1)
  | .compose N M_  =>
      -- compose : R (N+M) ⟶ R (N+M) — bracketed as
      -- `R (N+M) ≅ R N ⊗ R M ⟶ R (N+M)`
      (M.R_tensor N M_).hom ≫ M.compose_mor N M_
  | .square N      => M.square_mor N
  | .hom N M_      => M.hom_mor N M_
  | .modal_V4      =>
      -- modal_V4 : R 1 ⟶ R 4 — bracketed via
      -- `R 1 ⟶ R 2 ⊗ R 2 ≅ R (2+2) = R 4`
      M.modal_V4_mor ≫ (M.R_tensor 2 2).inv
  | .invo3        => M.invo3_mor
  | .iso4  => M.iso4_mor.hom
  | .morP3 N M_   => M.morP3_mor N M_

end

/-! ## § 6 The canonical (tensor-power) realisation

In any symmetric monoidal category `C` with chosen object `δ : C` we
have a canonical realisation sending `n ↦ δ^⊗n`. The seven generator
morphisms are interpreted by the obvious structural morphisms (identity,
associator coercions, etc.). -/

section Canonical

variable [MonoidalCategory C]

/-- Iterated tensor power `δ^⊗n` for a chosen object `δ : C`. By
convention `tensorPow δ 0 = 𝟙_ C` (the monoidal unit). -/
def tensorPow (δ : C) : ℕ → C
  | 0     => 𝟙_ C
  | n + 1 => δ ⊗ tensorPow δ n

@[simp] theorem tensorPow_zero (δ : C) : tensorPow δ 0 = 𝟙_ C := rfl

@[simp] theorem tensorPow_succ (δ : C) (n : ℕ) :
    tensorPow δ (n + 1) = δ ⊗ tensorPow δ n := rfl

/-- **Tensor-power additivity** in a monoidal category:
`δ^⊗(n+m) ≅ δ^⊗n ⊗ δ^⊗m`. Proof is by induction on `n`:

* `n = 0`: `tensorPow δ m ≅ 𝟙_C ⊗ tensorPow δ m` via the inverse left
  unitor `(λ_ _).symm`.
* `n = k+1`: chain `tensorPow δ ((k+1)+m) = tensorPow δ ((k+m)+1)
  = δ ⊗ tensorPow δ (k+m) ≅[IH] δ ⊗ (tensorPow δ k ⊗ tensorPow δ m)
  ≅[α.symm] (δ ⊗ tensorPow δ k) ⊗ tensorPow δ m
  = tensorPow δ (k+1) ⊗ tensorPow δ m`.

The first equality uses `Nat.succ_add` (definitional in Lean 4 since
`(k+1)+m = Nat.succ (k+m) = (k+m)+1`), routed via `eqToIso`. -/
noncomputable def tensorPow_add (δ : C) :
    ∀ n m, tensorPow δ (n + m) ≅ tensorPow δ n ⊗ tensorPow δ m
  | 0,     m => by
      -- tensorPow δ (0 + m) = tensorPow δ m
      -- need: tensorPow δ m ≅ tensorPow δ 0 ⊗ tensorPow δ m
      --                     = 𝟙_C ⊗ tensorPow δ m
      exact eqToIso (by rw [Nat.zero_add]) ≪≫ (λ_ (tensorPow δ m)).symm
  | k + 1, m => by
      -- (k+1) + m = k + m + 1 = (k+m).succ  -- by Nat.succ_add
      have hcomm : (k + 1) + m = (k + m) + 1 := by omega
      -- tensorPow δ ((k+m)+1) = δ ⊗ tensorPow δ (k+m)
      -- IH: tensorPow δ (k+m) ≅ tensorPow δ k ⊗ tensorPow δ m
      -- δ ⊗ (tensorPow δ k ⊗ tensorPow δ m) ≅ (δ ⊗ tensorPow δ k) ⊗ tensorPow δ m
      -- = tensorPow δ (k+1) ⊗ tensorPow δ m
      exact eqToIso (congrArg (tensorPow δ) hcomm)
        ≪≫ (Iso.refl (δ ⊗ tensorPow δ (k + m)))
        ≪≫ (Iso.refl δ ⊗ᵢ tensorPow_add δ k m)
        ≪≫ (α_ δ (tensorPow δ k) (tensorPow δ m)).symm

/-- Swap the two visible tensor factors of `δ^⊗2`.

The tensor powers in this file are right-associated:
`tensorPow δ 2 = δ ⊗ (δ ⊗ 𝟙_ C)`.  This helper uses the ambient
symmetric braiding to swap the two `δ` factors while leaving the terminal
unit tail in place. -/
noncomputable def tensorPow2Swap [SymmetricCategory C] (δ : C) :
    tensorPow δ 2 ⟶ tensorPow δ 2 := by
  show δ ⊗ (δ ⊗ 𝟙_ C) ⟶ δ ⊗ (δ ⊗ 𝟙_ C)
  exact
    (α_ δ δ (𝟙_ C)).inv ≫
      ((β_ δ δ).hom ⊗ₘ 𝟙 (𝟙_ C)) ≫
      (α_ δ δ (𝟙_ C)).hom

/-- Swap the first and second `δ` factors of `δ^⊗3`, preserving the
right-associated tensor-power shape. -/
noncomputable def tensorPow3Swap12 [SymmetricCategory C] (δ : C) :
    tensorPow δ 3 ⟶ tensorPow δ 3 := by
  show δ ⊗ (δ ⊗ (δ ⊗ 𝟙_ C)) ⟶ δ ⊗ (δ ⊗ (δ ⊗ 𝟙_ C))
  exact
    (α_ δ δ (δ ⊗ 𝟙_ C)).inv ≫
      ((β_ δ δ).hom ⊗ₘ 𝟙 (δ ⊗ 𝟙_ C)) ≫
      (α_ δ δ (δ ⊗ 𝟙_ C)).hom

/-- Swap the second and third `δ` factors of `δ^⊗3`, preserving the
right-associated tensor-power shape. -/
noncomputable def tensorPow3Swap23 [SymmetricCategory C] (δ : C) :
    tensorPow δ 3 ⟶ tensorPow δ 3 := by
  show δ ⊗ tensorPow δ 2 ⟶ δ ⊗ tensorPow δ 2
  exact 𝟙 δ ⊗ₘ tensorPow2Swap δ

/-- The canonical `invo3` map: three-factor reversal
`δ₀ ⊗ δ₁ ⊗ δ₂ ↦ δ₂ ⊗ δ₁ ⊗ δ₀`.

It is expressed as the Coxeter word `s₁ s₂ s₁` in the two adjacent swaps,
so it only uses the symmetric monoidal structure already required by the
T_GUT doctrine. -/
noncomputable def tensorPow3Reverse [SymmetricCategory C] (δ : C) :
    tensorPow δ 3 ⟶ tensorPow δ 3 :=
  tensorPow3Swap12 δ ≫ tensorPow3Swap23 δ ≫ tensorPow3Swap12 δ

/-- The canonical T_GUT **Core** realisation in `(C, δ)` at the chosen
generator `δ`. Sends `n ↦ δ^⊗n` (iterated left-associated tensor power).

**Status (post Option-A refactor, 2026-05-17)**: **0 sorry**. All 8 Core
fields admit a universal construction in any SMCC:

| field             | universal definition                |
|---|---|
| `R`               | `tensorPow δ`                       |
| `R_unit`          | `Iso.refl _` (`tensorPow δ 0 = 𝟙_C`) |
| `R_gen`           | `ρ_ δ` (right unitor, `δ ⊗ 𝟙_C ≅ δ`) |
| `R_tensor n m`    | `tensorPow_add δ n m`               |
| `compose_mor N M` | `(tensorPow_add δ N M).inv`         |
| `hom_mor N M`     | `𝟙 (tensorPow δ (N * M))`           |
| `invo3_mor`      | `tensorPow3Reverse δ`               |
| `iso4_mor`| `Iso.refl _`                         |

The three *instance-specific* operations (`square_mor`, `morP3_mor`,
`modal_V4_mor`) have been refactored out into `TGUTRealisationOps` —
they have no canonical universal definition in a general SMCC (a
diagonal `δ ⟶ δ ⊗ δ` would force cartesianness). Per
`gut-c-doctrine.md` v0.2 §3.5 these are *instance-specific* data; the
per-instance constructors live in `Foundation/Doctrine/Instance/*`.
-/
noncomputable def canonical [SymmetricCategory C] (δ : C) :
    TGUTRealisationCore C δ where
  R := tensorPow δ
  R_unit := Iso.refl _
  R_gen := by
    -- `R 1 = δ ⊗ 𝟙_ C ≅ δ` via the right unitor
    show tensorPow δ 1 ≅ δ
    -- tensorPow δ 1 = δ ⊗ 𝟙_ C
    exact ρ_ δ
  R_tensor n m := tensorPow_add δ n m
  compose_mor N M_ := (tensorPow_add δ N M_).inv
  hom_mor N M_ := 𝟙 (tensorPow δ (N * M_))
  invo3_mor := tensorPow3Reverse δ
  iso4_mor := Iso.refl _

end Canonical

/-! ## § 7 Universal Sayability — the headline GUT-C theorem

> **Theorem (GUT-C — Universal Sayability across SMCCs)**
>
> Let `C` be a symmetric monoidal category with biproducts and a
> chosen object `δ : C`. Let `R_C := TGUTRealisation.canonical δ` be the
> canonical tensor-power realisation. Then any other realisation
> `M : TGUTRealisation C δ` is isomorphic (as a realisation) to `R_C`.

The old notion of *isomorphism between realisations* used here was the
component-wise one: a family of isos `M.R n ≅ R_C.R n`. The legacy
`RealIso` wrapper remains for older callers as a carrier-only package;
non-vacuous commuting squares now live in `CoherentCoreRealIso`,
`FullCoherentCoreRealIso`, and `FullCoherentRealIso` below. -/

section UniversalSayability

variable [MonoidalCategory C]

/-- A *morphism* of realisations is a natural family of morphisms
`M.R n ⟶ N.R n` commuting with the structural isos and the generator
morphisms. We bundle only the underlying components here — naturality
in `n` and commutation with each generator are the *Phase γ.3* content
and are not enforced at this skeleton level.

**Doctrinal note (Option A refactor, 2026-05-17)**: stated at *Core*
level — universal sayability is fundamentally about carrier uniqueness,
which lives in the universal `TGUTRealisationCore`. Coherence with the
instance-specific `Ops` morphisms is a separate (per-instance) claim. -/
structure Hom {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying family of component morphisms. -/
  component : ∀ n, M.R n ⟶ N.R n

/-- Legacy carrier-only realisation isomorphism.

This wrapper is retained for older callers that only need layerwise
component isos. New code should use `CoherentCoreRealIso` or
`FullCoherentCoreRealIso` for non-vacuous coherence.

**Doctrinal note (Option A refactor, 2026-05-17)**: stated at *Core*
level for the same reason as `Hom` above — the universal-sayability
statement is about carrier uniqueness. -/
structure RealIso {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying family of component isos. -/
  iso : ∀ n, M.R n ≅ N.R n

/-- A minimal **Core-level** realisation isomorphism that exposes the
carrier components needed for universal sayability without committing
to the full tensor/generator commuting-square package of Phase γ.3.

`unit_hom` and `gen_hom` are intentionally just the level-`0` and
level-`1` carrier maps induced by `iso`. This records the unit and
generator carrier witnesses in an API-stable bundle while avoiding any
new coherence obligations that existing `TGUTRealisationCore` data does
not yet enforce. -/
structure CoreRealIso {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying family of component isos. -/
  iso : ∀ n, M.R n ≅ N.R n

namespace CoreRealIso

variable {δ : C} {M N : TGUTRealisationCore C δ}

/-- The carrier morphism at the monoidal-unit layer. -/
def unit_hom (e : CoreRealIso M N) : M.R 0 ⟶ N.R 0 :=
  (e.iso 0).hom

/-- The carrier morphism at the generator layer. -/
def gen_hom (e : CoreRealIso M N) : M.R 1 ⟶ N.R 1 :=
  (e.iso 1).hom

/-- The minimal carrier-level witness forgets to the existing `RealIso` API. -/
def toRealIso (e : CoreRealIso M N) : RealIso M N where
  iso := e.iso

@[simp] theorem unit_hom_eq_apply (e : CoreRealIso M N) :
    e.unit_hom = (e.iso 0).hom :=
  rfl

@[simp] theorem gen_hom_eq_apply (e : CoreRealIso M N) :
    e.gen_hom = (e.iso 1).hom :=
  rfl

end CoreRealIso

/-- The concrete structural commuting-square predicate for a core-level
component iso.  This is the non-vacuous replacement for the old carrier-only
`RealIso` coherence placeholder: it asks the component isos to commute with
the unit, generator, and tensor-power structural isos.

It is kept as a separate predicate rather than forced onto every raw
`TGUTRealisationCore`, because the current Core record stores structural
isomorphisms but does not yet require their unit/associativity coherence. -/
structure CoreStructuralCoherence {δ : C} {M N : TGUTRealisationCore C δ}
    (iso : ∀ n, M.R n ≅ N.R n) : Prop where
  /-- Compatibility with `R 0 ≅ 𝟙_ C`. -/
  unit_hom : (iso 0).hom ≫ N.R_unit.hom = M.R_unit.hom
  /-- Compatibility with `R 1 ≅ δ`. -/
  gen_hom : (iso 1).hom ≫ N.R_gen.hom = M.R_gen.hom
  /-- Compatibility with the tensor-power decomposition `R (n+m) ≅ R n ⊗ R m`. -/
  tensor_hom : ∀ n m,
    (iso (n + m)).hom ≫ (N.R_tensor n m).hom =
      (M.R_tensor n m).hom ≫ ((iso n).hom ⊗ₘ (iso m).hom)

/-- Coherence laws for the structural tensor decomposition stored in a
`TGUTRealisationCore`. The raw core record contains arbitrary isomorphisms
`R_tensor n m`; these laws say that they form the expected monoidal
additivity data with respect to `R_unit` and the associator.

This is the minimal missing hypothesis for deriving
`CoreStructuralCoherence` of `componentIso` from the core data itself. The
derived proof is intentionally left to the next γ.3 step rather than hidden
behind a vacuous adequacy assumption. -/
structure CoreTensorCoherence {δ : C} (M : TGUTRealisationCore C δ) : Prop where
  /-- `R_tensor 0 n` agrees with `R_unit` and the left unitor. -/
  tensor_unit_left : ∀ n,
    (M.R_tensor 0 n).hom ≫
      (M.R_unit.hom ⊗ₘ 𝟙 (M.R n)) ≫
      (λ_ (M.R n)).hom =
        (eqToIso (congrArg M.R (Nat.zero_add n))).hom
  /-- `R_tensor n 0` agrees with `R_unit` and the right unitor. -/
  tensor_unit_right : ∀ n,
    (M.R_tensor n 0).hom ≫
      (𝟙 (M.R n) ⊗ₘ M.R_unit.hom) ≫
      (ρ_ (M.R n)).hom =
        (eqToIso (congrArg M.R (Nat.add_zero n))).hom
  /-- The two decompositions of `R ((a + b) + c)` into
      `(R a ⊗ R b) ⊗ R c` agree up to associativity. -/
  tensor_assoc : ∀ a b c,
    (M.R_tensor (a + b) c).hom ≫
      ((M.R_tensor a b).hom ⊗ₘ 𝟙 (M.R c)) =
        (eqToIso (congrArg M.R (Nat.add_assoc a b c))).hom ≫
        (M.R_tensor a (b + c)).hom ≫
        (𝟙 (M.R a) ⊗ₘ (M.R_tensor b c).hom) ≫
        (α_ (M.R a) (M.R b) (M.R c)).inv

/-- A core realisation isomorphism with the structural commuting squares
spelled out.  This is the target shape for the full T_GUT carrier proof;
`CoreRealIso` remains the minimal API-stable carrier witness. -/
structure CoherentCoreRealIso {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying family of component isos. -/
  iso : ∀ n, M.R n ≅ N.R n
  /-- Unit/generator/tensor structural coherence. -/
  structural_coherent : CoreStructuralCoherence (M := M) (N := N) iso

namespace CoherentCoreRealIso

variable {δ : C} {M N : TGUTRealisationCore C δ}

/-- A structurally coherent core iso forgets to the legacy carrier-only
`RealIso` wrapper. -/
def toRealIso (e : CoherentCoreRealIso M N) : RealIso M N where
  iso := e.iso

/-- Forget the structural commuting squares and keep the carrier-level API. -/
def toCoreRealIso (e : CoherentCoreRealIso M N) : CoreRealIso M N where
  iso := e.iso

end CoherentCoreRealIso

/-- Core-generator commuting squares for a component iso.

This deliberately covers only the universal Core generators:
`compose_mor`, `hom_mor`, `invo3_mor`, and `iso4_mor`.
The ops-level generators (`square`, `morP3`, `modal_V4`) are
instance-specific and stay out of the core theorem. -/
structure CoreGeneratorCoherence {δ : C} {M N : TGUTRealisationCore C δ}
    (iso : ∀ n, M.R n ≅ N.R n) : Prop where
  /-- Compatibility with the raw composition generator
      `R n ⊗ R m ⟶ R (n+m)`. -/
  compose_hom : ∀ n m,
    M.compose_mor n m ≫ (iso (n + m)).hom =
      ((iso n).hom ⊗ₘ (iso m).hom) ≫ N.compose_mor n m
  /-- Compatibility with the Hom-as-content generator. -/
  hom_hom : ∀ n m,
    M.hom_mor n m ≫ (iso (n * m)).hom =
      (iso (n * m)).hom ≫ N.hom_mor n m
  /-- Compatibility with the `invo3` involution carrier. -/
  invo3_hom :
    M.invo3_mor ≫ (iso 3).hom =
      (iso 3).hom ≫ N.invo3_mor
  /-- Compatibility with the Wedderburn carrier iso's forward map. -/
  iso4_hom :
    M.iso4_mor.hom ≫ (iso 4).hom =
      (iso 4).hom ≫ N.iso4_mor.hom

/-- Structural naturality squares for a morphism between core realisations. -/
structure CoreHomStructuralCoherence {δ : C} {M N : TGUTRealisationCore C δ}
    (component : ∀ n, M.R n ⟶ N.R n) : Prop where
  /-- Naturality with `R 0 ≅ 𝟙_ C`. -/
  unit_hom : component 0 ≫ N.R_unit.hom = M.R_unit.hom
  /-- Naturality with `R 1 ≅ δ`. -/
  gen_hom : component 1 ≫ N.R_gen.hom = M.R_gen.hom
  /-- Naturality with the tensor-power decomposition. -/
  tensor_hom : ∀ n m,
    component (n + m) ≫ (N.R_tensor n m).hom =
      (M.R_tensor n m).hom ≫ (component n ⊗ₘ component m)

/-- Core-generator naturality squares for a morphism between core realisations. -/
structure CoreHomGeneratorCoherence {δ : C} {M N : TGUTRealisationCore C δ}
    (component : ∀ n, M.R n ⟶ N.R n) : Prop where
  /-- Naturality with the raw composition generator. -/
  compose_hom : ∀ n m,
    M.compose_mor n m ≫ component (n + m) =
      (component n ⊗ₘ component m) ≫ N.compose_mor n m
  /-- Naturality with the Hom-as-content generator. -/
  hom_hom : ∀ n m,
    M.hom_mor n m ≫ component (n * m) =
      component (n * m) ≫ N.hom_mor n m
  /-- Naturality with the `invo3` carrier involution. -/
  invo3_hom :
    M.invo3_mor ≫ component 3 =
      component 3 ≫ N.invo3_mor
  /-- Naturality with the Wedderburn carrier automorphism. -/
  iso4_hom :
    M.iso4_mor.hom ≫ component 4 =
      component 4 ≫ N.iso4_mor.hom

/-- A non-vacuous morphism of core realisations. -/
structure CoreRealisationHom {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying layerwise morphisms. -/
  component : ∀ n, M.R n ⟶ N.R n
  /-- Structural naturality. -/
  structural_natural :
    CoreHomStructuralCoherence (M := M) (N := N) component
  /-- Core-generator naturality. -/
  generator_natural :
    CoreHomGeneratorCoherence (M := M) (N := N) component

namespace CoreRealisationHom

variable {δ : C} {M N P Q : TGUTRealisationCore C δ}

/-- Extensionality for core realisation morphisms.  The coherence fields are
proofs, so the component family determines the morphism. -/
@[ext] theorem ext (f g : CoreRealisationHom M N)
    (h : ∀ n, f.component n = g.component n) : f = g := by
  cases f with
  | mk f_component f_structural f_generator =>
    cases g with
    | mk g_component g_structural g_generator =>
      have hcomponent : f_component = g_component := funext h
      subst hcomponent
      simp

/-- Identity morphism of a core realisation. -/
def id (M : TGUTRealisationCore C δ) : CoreRealisationHom M M where
  component n := 𝟙 (M.R n)
  structural_natural := by
    refine
      { unit_hom := ?_
        gen_hom := ?_
        tensor_hom := ?_ }
    · simp
    · simp
    · intro n m
      simp
  generator_natural := by
    refine
      { compose_hom := ?_
        hom_hom := ?_
        invo3_hom := ?_
        iso4_hom := ?_ }
    · intro n m
      simp
    · intro n m
      simp
    · simp
    · simp

/-- Composition of core realisation morphisms. -/
def comp (g : CoreRealisationHom N P) (f : CoreRealisationHom M N) :
    CoreRealisationHom M P where
  component n := f.component n ≫ g.component n
  structural_natural := by
    refine
      { unit_hom := ?_
        gen_hom := ?_
        tensor_hom := ?_ }
    · rw [Category.assoc, g.structural_natural.unit_hom,
        f.structural_natural.unit_hom]
    · rw [Category.assoc, g.structural_natural.gen_hom,
        f.structural_natural.gen_hom]
    · intro n m
      rw [Category.assoc, g.structural_natural.tensor_hom]
      rw [← Category.assoc, f.structural_natural.tensor_hom]
      simp [Category.assoc]
  generator_natural := by
    refine
      { compose_hom := ?_
        hom_hom := ?_
        invo3_hom := ?_
        iso4_hom := ?_ }
    · intro n m
      rw [← Category.assoc, f.generator_natural.compose_hom]
      rw [Category.assoc, g.generator_natural.compose_hom]
      simp
    · intro n m
      rw [← Category.assoc, f.generator_natural.hom_hom]
      rw [Category.assoc, g.generator_natural.hom_hom]
      rw [Category.assoc]
    · rw [← Category.assoc, f.generator_natural.invo3_hom]
      rw [Category.assoc, g.generator_natural.invo3_hom]
      rw [Category.assoc]
    · rw [← Category.assoc, f.generator_natural.iso4_hom]
      rw [Category.assoc, g.generator_natural.iso4_hom]
      rw [Category.assoc]

@[simp] theorem comp_component (g : CoreRealisationHom N P)
    (f : CoreRealisationHom M N) (n : ℕ) :
    (comp g f).component n = f.component n ≫ g.component n :=
  rfl

@[simp] theorem id_component (n : ℕ) :
    (id M).component n = 𝟙 (M.R n) :=
  rfl

@[simp] theorem comp_id (f : CoreRealisationHom M N) :
    comp (id N) f = f := by
  ext n
  simp [comp, id]

@[simp] theorem id_comp (f : CoreRealisationHom M N) :
    comp f (id M) = f := by
  ext n
  simp [comp, id]

@[simp] theorem comp_assoc (h : CoreRealisationHom P Q)
    (g : CoreRealisationHom N P) (f : CoreRealisationHom M N) :
    comp h (comp g f) = comp (comp h g) f := by
  ext n
  simp [comp, Category.assoc]

end CoreRealisationHom

/-- A core realisation isomorphism carrying both structural coherence and
the universal core-generator commuting squares. -/
structure FullCoherentCoreRealIso {δ : C} (M N : TGUTRealisationCore C δ) where
  /-- The underlying family of component isos. -/
  iso : ∀ n, M.R n ≅ N.R n
  /-- Unit/generator/tensor structural coherence. -/
  structural_coherent : CoreStructuralCoherence (M := M) (N := N) iso
  /-- Coherence for the universal core generators. -/
  generator_coherent : CoreGeneratorCoherence (M := M) (N := N) iso

namespace FullCoherentCoreRealIso

variable {δ : C} {M N : TGUTRealisationCore C δ}

/-- Forget generator coherence but retain structural coherence. -/
def toCoherentCoreRealIso (e : FullCoherentCoreRealIso M N) :
    CoherentCoreRealIso M N where
  iso := e.iso
  structural_coherent := e.structural_coherent

/-- Forget all commuting squares and keep the carrier-level API. -/
def toCoreRealIso (e : FullCoherentCoreRealIso M N) : CoreRealIso M N where
  iso := e.iso

/-- Forget invertibility but retain the non-vacuous naturality squares. -/
def toCoreRealisationHom (e : FullCoherentCoreRealIso M N) :
    CoreRealisationHom M N where
  component n := (e.iso n).hom
  structural_natural :=
    { unit_hom := e.structural_coherent.unit_hom
      gen_hom := e.structural_coherent.gen_hom
      tensor_hom := fun n m => e.structural_coherent.tensor_hom n m }
  generator_natural :=
    { compose_hom := fun n m => e.generator_coherent.compose_hom n m
      hom_hom := fun n m => e.generator_coherent.hom_hom n m
      invo3_hom := e.generator_coherent.invo3_hom
      iso4_hom := e.generator_coherent.iso4_hom }

/-- A fully coherent core iso forgets to the legacy carrier-only `RealIso`
wrapper. -/
def toRealIso (e : FullCoherentCoreRealIso M N) : RealIso M N where
  iso := e.iso

end FullCoherentCoreRealIso

/-- Ops-level commuting squares for a component iso between bundled
realisations.

Unlike `CoreGeneratorCoherence`, this is not part of the universal core
theorem: `square`, `morP3`, and `modal_V4` have no canonical definition
in an arbitrary SMCC. Instance files must provide these fields when the
chosen base gives those operations real meaning. -/
structure OpsCoherence {δ : C} {M N : TGUTRealisation C δ}
    (iso : ∀ n, M.R n ≅ N.R n) : Prop where
  /-- Compatibility with `square_mor`. -/
  square_hom : ∀ n,
    M.square_mor n ≫ (iso (2 * n)).hom =
      (iso n).hom ≫ N.square_mor n
  /-- Compatibility with `morP3_mor`. -/
  relate_hom : ∀ n m,
    M.morP3_mor n m ≫ (iso m).hom =
      (iso n).hom ≫ N.morP3_mor n m
  /-- Compatibility with `modal_V4_mor`. -/
  modal_V4_hom :
    M.modal_V4_mor ≫ ((iso 2).hom ⊗ₘ (iso 2).hom) =
      (iso 1).hom ≫ N.modal_V4_mor

/-- Ops-level naturality squares for a morphism between bundled realisations. -/
structure OpsHomCoherence {δ : C} {M N : TGUTRealisation C δ}
    (component : ∀ n, M.R n ⟶ N.R n) : Prop where
  /-- Naturality with `square_mor`. -/
  square_hom : ∀ n,
    M.square_mor n ≫ component (2 * n) =
      component n ≫ N.square_mor n
  /-- Naturality with `morP3_mor`. -/
  relate_hom : ∀ n m,
    M.morP3_mor n m ≫ component m =
      component n ≫ N.morP3_mor n m
  /-- Naturality with `modal_V4_mor`. -/
  modal_V4_hom :
    M.modal_V4_mor ≫ (component 2 ⊗ₘ component 2) =
      component 1 ≫ N.modal_V4_mor

/-- A non-vacuous morphism of bundled realisations, including ops. -/
structure RealisationHom {δ : C} (M N : TGUTRealisation C δ) where
  /-- The underlying layerwise morphisms. -/
  component : ∀ n, M.R n ⟶ N.R n
  /-- Structural naturality for the core carrier data. -/
  structural_natural :
    CoreHomStructuralCoherence
      (M := M.toTGUTRealisationCore) (N := N.toTGUTRealisationCore) component
  /-- Naturality for core generators. -/
  generator_natural :
    CoreHomGeneratorCoherence
      (M := M.toTGUTRealisationCore) (N := N.toTGUTRealisationCore) component
  /-- Naturality for instance-specific ops. -/
  ops_natural : OpsHomCoherence (M := M) (N := N) component

namespace RealisationHom

variable {δ : C} {M N P Q : TGUTRealisation C δ}

/-- Extensionality for bundled realisation morphisms.  Coherence fields are
proofs, so the component family determines the morphism. -/
@[ext] theorem ext (f g : RealisationHom M N)
    (h : ∀ n, f.component n = g.component n) : f = g := by
  cases f with
  | mk f_component f_structural f_generator f_ops =>
    cases g with
    | mk g_component g_structural g_generator g_ops =>
      have hcomponent : f_component = g_component := funext h
      subst hcomponent
      simp

/-- Identity morphism of a bundled realisation. -/
def id (M : TGUTRealisation C δ) : RealisationHom M M where
  component n := 𝟙 (M.R n)
  structural_natural := (CoreRealisationHom.id M.toTGUTRealisationCore).structural_natural
  generator_natural := (CoreRealisationHom.id M.toTGUTRealisationCore).generator_natural
  ops_natural := by
    refine
      { square_hom := ?_
        relate_hom := ?_
        modal_V4_hom := ?_ }
    · intro n
      simp
    · intro n m
      simp
    · simp

/-- Composition of bundled realisation morphisms, including ops naturality. -/
def comp (g : RealisationHom N P) (f : RealisationHom M N) :
    RealisationHom M P where
  component n := f.component n ≫ g.component n
  structural_natural := (CoreRealisationHom.comp
    ({ component := g.component
       structural_natural := g.structural_natural
       generator_natural := g.generator_natural } :
        CoreRealisationHom N.toTGUTRealisationCore P.toTGUTRealisationCore)
    ({ component := f.component
       structural_natural := f.structural_natural
       generator_natural := f.generator_natural } :
        CoreRealisationHom M.toTGUTRealisationCore N.toTGUTRealisationCore)).structural_natural
  generator_natural := (CoreRealisationHom.comp
    ({ component := g.component
       structural_natural := g.structural_natural
       generator_natural := g.generator_natural } :
        CoreRealisationHom N.toTGUTRealisationCore P.toTGUTRealisationCore)
    ({ component := f.component
       structural_natural := f.structural_natural
       generator_natural := f.generator_natural } :
        CoreRealisationHom M.toTGUTRealisationCore N.toTGUTRealisationCore)).generator_natural
  ops_natural := by
    refine
      { square_hom := ?_
        relate_hom := ?_
        modal_V4_hom := ?_ }
    · intro n
      rw [← Category.assoc, f.ops_natural.square_hom]
      rw [Category.assoc, g.ops_natural.square_hom]
      rw [Category.assoc]
    · intro n m
      rw [← Category.assoc, f.ops_natural.relate_hom]
      rw [Category.assoc, g.ops_natural.relate_hom]
      rw [Category.assoc]
    · rw [← MonoidalCategory.tensorHom_comp_tensorHom]
      rw [← Category.assoc, f.ops_natural.modal_V4_hom]
      rw [Category.assoc, g.ops_natural.modal_V4_hom]
      rw [Category.assoc]

@[simp] theorem comp_component (g : RealisationHom N P)
    (f : RealisationHom M N) (n : ℕ) :
    (comp g f).component n = f.component n ≫ g.component n :=
  rfl

@[simp] theorem id_component (n : ℕ) :
    (id M).component n = 𝟙 (M.R n) :=
  rfl

@[simp] theorem comp_id (f : RealisationHom M N) :
    comp (id N) f = f := by
  ext n
  simp [comp, id]

@[simp] theorem id_comp (f : RealisationHom M N) :
    comp f (id M) = f := by
  ext n
  simp [comp, id]

@[simp] theorem comp_assoc (h : RealisationHom P Q)
    (g : RealisationHom N P) (f : RealisationHom M N) :
    comp h (comp g f) = comp (comp h g) f := by
  ext n
  simp [comp, Category.assoc]

end RealisationHom

/-- A full bundled-realisation iso, including per-instance ops coherence.

There is intentionally no generic theorem producing this against
`canonical δ`: the canonical construction is Core-only. Per-instance files
should build a comparison target with meaningful ops and then prove this
predicate there. -/
structure FullCoherentRealIso {δ : C} (M N : TGUTRealisation C δ) where
  /-- The underlying family of component isos. -/
  iso : ∀ n, M.R n ≅ N.R n
  /-- Unit/generator/tensor structural coherence. -/
  structural_coherent :
    CoreStructuralCoherence
      (M := M.toTGUTRealisationCore) (N := N.toTGUTRealisationCore) iso
  /-- Core-generator coherence. -/
  generator_coherent :
    CoreGeneratorCoherence
      (M := M.toTGUTRealisationCore) (N := N.toTGUTRealisationCore) iso
  /-- Per-instance ops coherence. -/
  ops_coherent : OpsCoherence (M := M) (N := N) iso

namespace FullCoherentRealIso

variable {δ : C} {M N : TGUTRealisation C δ}

/-- Forget invertibility but retain all non-vacuous naturality squares. -/
def toRealisationHom (e : FullCoherentRealIso M N) : RealisationHom M N where
  component n := (e.iso n).hom
  structural_natural :=
    { unit_hom := e.structural_coherent.unit_hom
      gen_hom := e.structural_coherent.gen_hom
      tensor_hom := fun n m => e.structural_coherent.tensor_hom n m }
  generator_natural :=
    { compose_hom := fun n m => e.generator_coherent.compose_hom n m
      hom_hom := fun n m => e.generator_coherent.hom_hom n m
      invo3_hom := e.generator_coherent.invo3_hom
      iso4_hom := e.generator_coherent.iso4_hom }
  ops_natural :=
    { square_hom := fun n => e.ops_coherent.square_hom n
      relate_hom := fun n m => e.ops_coherent.relate_hom n m
      modal_V4_hom := e.ops_coherent.modal_V4_hom }

end FullCoherentRealIso

/-! ### § 7.1 Layer-by-layer component iso

The first ingredient of `universal_sayability` is the *layerwise* iso
`M.R n ≅ tensorPow δ n` for each `n : ℕ`. This is the structural
content of the theorem and is proven by induction on `n` using the
three structural isos `R_unit / R_gen / R_tensor` of `M`:

* `n = 0`: `M.R 0 ≅ 𝟙_ C = tensorPow δ 0` via `M.R_unit`.
* `n = k + 1`: chain
    `M.R (k + 1) ≅ M.R (1 + k)`              -- eqToIso (commutativity of ℕ)
    `             ≅ M.R 1 ⊗ M.R k`            -- M.R_tensor 1 k
    `             ≅ δ ⊗ tensorPow δ k`        -- M.R_gen ⊗ᵢ IH
    `             = tensorPow δ (k + 1)`     -- rfl (by tensorPow_succ)

The proof does *not* depend on the seven generator morphisms or the
equational laws — only on the structural isos. This is the "free part"
of the theory uniqueness: the carrier-shape uniqueness is determined
by `R 1 ≅ δ` and the tensor-power additivity. -/
noncomputable def componentIso (δ : C) (M : TGUTRealisationCore C δ) :
    ∀ n, M.R n ≅ tensorPow δ n
  | 0 => M.R_unit
  | k + 1 =>
      -- tensorPow δ (k + 1) = δ ⊗ tensorPow δ k  (by rfl via tensorPow_succ)
      -- Chain: M.R (k+1) ≅ M.R (1+k) ≅ M.R 1 ⊗ M.R k ≅ δ ⊗ tensorPow δ k
      have hcomm : k + 1 = 1 + k := by omega
      eqToIso (congrArg M.R hcomm)
        ≪≫ M.R_tensor 1 k
        ≪≫ (M.R_gen ⊗ᵢ componentIso δ M k)

@[simp] theorem componentIso_zero_hom
    (δ : C) (M : TGUTRealisationCore C δ) :
    (componentIso δ M 0).hom = M.R_unit.hom := rfl

@[simp] theorem componentIso_zero_inv
    (δ : C) (M : TGUTRealisationCore C δ) :
    (componentIso δ M 0).inv = M.R_unit.inv := rfl

@[reassoc]
theorem componentIso_hom_naturality
    (δ : C) (M : TGUTRealisationCore C δ) {n m : ℕ} (h : n = m) :
    (componentIso δ M n).hom ≫ eqToHom (by simp [h]) =
      eqToHom (by simp [h]) ≫ (componentIso δ M m).hom :=
  eqToHom_iso_hom_naturality (componentIso δ M) h

@[reassoc]
theorem R_tensor_hom_naturality_left
    (M : TGUTRealisationCore C δ) {n n' m : ℕ} (h : n = n') :
    (M.R_tensor n m).hom ≫ eqToHom (by simp [h]) =
      eqToHom (by simp [h]) ≫ (M.R_tensor n' m).hom :=
  eqToHom_iso_hom_naturality (fun k => M.R_tensor k m) h

theorem R_tensor_hom_naturality_left_tensor
    (M : TGUTRealisationCore C δ) {n n' m : ℕ} (h : n = n') :
    (M.R_tensor n m).hom ≫
        ((eqToIso (congrArg M.R h)).hom ⊗ₘ 𝟙 (M.R m)) =
      (eqToIso (congrArg M.R (congrArg (fun k => k + m) h))).hom ≫
        (M.R_tensor n' m).hom := by
  simpa [eqToIso.hom] using R_tensor_hom_naturality_left (M := M) (m := m) h

@[reassoc]
theorem R_tensor_hom_naturality_left_tensor_comp
    (M : TGUTRealisationCore C δ) {n n' m : ℕ} {X Y : C}
    (h : n = n') (f : M.R n' ⟶ X) (g : M.R m ⟶ Y) :
    (M.R_tensor n m).hom ≫
        (((eqToIso (congrArg M.R h)).hom ≫ f) ⊗ₘ g) =
      (eqToIso (congrArg M.R (congrArg (fun k => k + m) h))).hom ≫
        (M.R_tensor n' m).hom ≫ (f ⊗ₘ g) := by
  calc
    (M.R_tensor n m).hom ≫
        (((eqToIso (congrArg M.R h)).hom ≫ f) ⊗ₘ g)
        =
      (M.R_tensor n m).hom ≫
        (((eqToIso (congrArg M.R h)).hom ⊗ₘ 𝟙 (M.R m)) ≫
          (f ⊗ₘ g)) := by
          rw [tensorHom_comp_tensorHom]
          simp
    _ =
      ((M.R_tensor n m).hom ≫
        ((eqToIso (congrArg M.R h)).hom ⊗ₘ 𝟙 (M.R m))) ≫
        (f ⊗ₘ g) := by
          simp [Category.assoc]
    _ =
      ((eqToIso (congrArg M.R (congrArg (fun k => k + m) h))).hom ≫
        (M.R_tensor n' m).hom) ≫
        (f ⊗ₘ g) := by
          rw [R_tensor_hom_naturality_left_tensor (M := M) (m := m) h]
    _ =
      (eqToIso (congrArg M.R (congrArg (fun k => k + m) h))).hom ≫
        (M.R_tensor n' m).hom ≫ (f ⊗ₘ g) := by
          simp [Category.assoc]

theorem associator_hom_tensorHom_tensorHom_inv
    {X₁ X₂ X₃ Y₁ Y₂ Y₃ : C}
    (f₁ : X₁ ⟶ Y₁) (f₂ : X₂ ⟶ Y₂) (f₃ : X₃ ⟶ Y₃) :
    (α_ X₁ X₂ X₃).hom ≫ (f₁ ⊗ₘ (f₂ ⊗ₘ f₃)) ≫
        (α_ Y₁ Y₂ Y₃).inv =
      ((f₁ ⊗ₘ f₂) ⊗ₘ f₃) := by
  have h := associator_naturality f₁ f₂ f₃
  rw [← Category.assoc]
  rw [← h]
  simp [Category.assoc]

variable [SymmetricCategory C]

/-- The recursively constructed component isomorphism commutes with the
unit, generator, and tensor structure whenever the source core's tensor
decomposition satisfies the standard unit and associativity laws. -/
theorem componentIso_structural_coherent
    (δ : C) (M : TGUTRealisationCore C δ)
    (hM : CoreTensorCoherence M) :
    CoreStructuralCoherence
      (M := M) (N := canonical δ) (componentIso δ M) := by
  constructor
  · simp [canonical]
  · simp [componentIso, canonical]
    have hnat :
        (M.R_gen.hom ⊗ₘ M.R_unit.hom) ≫ (ρ_ δ).hom =
          (𝟙 (M.R 1) ⊗ₘ M.R_unit.hom) ≫
            (ρ_ (M.R 1)).hom ≫ M.R_gen.hom := by
      calc
        (M.R_gen.hom ⊗ₘ M.R_unit.hom) ≫ (ρ_ δ).hom
            =
          ((𝟙 (M.R 1) ⊗ₘ M.R_unit.hom) ≫
            (M.R_gen.hom ⊗ₘ 𝟙 (𝟙_ C))) ≫
            (ρ_ δ).hom := by
              rw [tensorHom_comp_tensorHom]
              simp
        _ =
          (𝟙 (M.R 1) ⊗ₘ M.R_unit.hom) ≫
            ((M.R_gen.hom ⊗ₘ 𝟙 (𝟙_ C)) ≫ (ρ_ δ).hom) := by
              simp [Category.assoc]
        _ =
          (𝟙 (M.R 1) ⊗ₘ M.R_unit.hom) ≫
            (ρ_ (M.R 1)).hom ≫ M.R_gen.hom := by
              rw [tensorHom_id, rightUnitor_naturality]
    calc
      (M.R_tensor 1 0).hom ≫ (M.R_gen.hom ⊗ₘ M.R_unit.hom) ≫ (ρ_ δ).hom
          =
        (M.R_tensor 1 0).hom ≫
          ((𝟙 (M.R 1) ⊗ₘ M.R_unit.hom) ≫
            (ρ_ (M.R 1)).hom ≫ M.R_gen.hom) := by
            rw [hnat]
      _ =
        ((eqToIso (congrArg M.R (Nat.add_zero 1))).hom) ≫
          M.R_gen.hom := by
            simpa [Category.assoc] using
              congrArg (fun f => f ≫ M.R_gen.hom) (hM.tensor_unit_right 1)
      _ = M.R_gen.hom := by
            have hEq : congrArg M.R (Nat.add_zero 1) = rfl := by
              apply Subsingleton.elim
            rw [hEq]
            simp
  · intro n m
    induction n with
    | zero =>
        simp [componentIso, canonical, tensorPow_add]
        let i := componentIso δ M m
        symm
        calc
          (M.R_tensor 0 m).hom ≫ (M.R_unit.hom ⊗ₘ i.hom)
              =
            (M.R_tensor 0 m).hom ≫
              ((M.R_unit.hom ⊗ₘ 𝟙 (M.R m)) ≫
                (𝟙 (𝟙_ C) ⊗ₘ i.hom)) := by
                rw [tensorHom_comp_tensorHom]
                simp [i]
          _ =
            ((M.R_tensor 0 m).hom ≫
              (M.R_unit.hom ⊗ₘ 𝟙 (M.R m)) ≫
              (λ_ (M.R m)).hom) ≫
              (λ_ (M.R m)).inv ≫
              (𝟙 (𝟙_ C) ⊗ₘ i.hom) := by
                simp [Category.assoc]
          _ =
            (eqToIso (congrArg M.R (Nat.zero_add m))).hom ≫
              (λ_ (M.R m)).inv ≫
              (𝟙 (𝟙_ C) ⊗ₘ i.hom) := by
                rw [hM.tensor_unit_left m]
          _ =
            (eqToIso (congrArg M.R (Nat.zero_add m))).hom ≫
              i.hom ≫
              (λ_ (tensorPow δ m)).inv := by
                rw [id_tensorHom]
                rw [← leftUnitor_inv_naturality i.hom]
    | succ n ih =>
        simp [componentIso, canonical, tensorPow_add]
        erw [componentIso_hom_naturality_assoc δ M
          (by omega : n + 1 + m = (n + m) + 1)]
        simp [componentIso]
        have ih' :
            (componentIso δ M (n + m)).hom ≫ (tensorPow_add δ n m).hom =
              (M.R_tensor n m).hom ≫
                ((componentIso δ M n).hom ⊗ₘ (componentIso δ M m).hom) := by
          simpa [canonical] using ih
        rw [← id_tensorHom]
        rw [tensorHom_comp_tensorHom_assoc]
        simp only [Category.comp_id]
        have hTensorIH :
            M.R_gen.hom ⊗ₘ
                ((componentIso δ M (n + m)).hom ≫
                  (tensorPow_add δ n m).hom) =
              M.R_gen.hom ⊗ₘ
                ((M.R_tensor n m).hom ≫
                  ((componentIso δ M n).hom ⊗ₘ
                    (componentIso δ M m).hom)) := by
          exact congrArg (fun f => M.R_gen.hom ⊗ₘ f) ih'
        erw [hTensorIH]
        let hFirst : n + 1 = 1 + n := by omega
        let hFirstAdd : (n + 1) + m = (1 + n) + m :=
          congrArg (fun k => k + m) hFirst
        erw [R_tensor_hom_naturality_left_tensor_comp M
          hFirst
          ((M.R_tensor 1 n).hom ≫
            (M.R_gen.hom ⊗ₘ (componentIso δ M n).hom))
          ((componentIso δ M m).hom)]
        have hAssocPost := congrArg
          (fun f =>
            (eqToIso (congrArg M.R hFirstAdd)).hom ≫
            f ≫
              ((M.R_gen.hom ⊗ₘ (componentIso δ M n).hom) ⊗ₘ
                (componentIso δ M m).hom))
          (hM.tensor_assoc 1 n m)
        have hAssocCollapse :
            ((M.R_tensor 1 n).hom ⊗ₘ 𝟙 (M.R m)) ≫
                (α_ (M.R 1) (M.R n) (M.R m)).hom ≫
                (M.R_gen.hom ⊗ₘ
                  ((componentIso δ M n).hom ⊗ₘ
                    (componentIso δ M m).hom)) ≫
                (α_ δ (tensorPow δ n) (tensorPow δ m)).inv =
              (((M.R_tensor 1 n).hom ≫
                  (M.R_gen.hom ⊗ₘ (componentIso δ M n).hom)) ⊗ₘ
                (componentIso δ M m).hom) := by
          calc
            ((M.R_tensor 1 n).hom ⊗ₘ 𝟙 (M.R m)) ≫
                (α_ (M.R 1) (M.R n) (M.R m)).hom ≫
                (M.R_gen.hom ⊗ₘ
                  ((componentIso δ M n).hom ⊗ₘ
                    (componentIso δ M m).hom)) ≫
                (α_ δ (tensorPow δ n) (tensorPow δ m)).inv
                =
              ((M.R_tensor 1 n).hom ⊗ₘ 𝟙 (M.R m)) ≫
                (((M.R_gen.hom ⊗ₘ (componentIso δ M n).hom) ⊗ₘ
                  (componentIso δ M m).hom)) := by
                  rw [associator_hom_tensorHom_tensorHom_inv]
            _ =
              (((M.R_tensor 1 n).hom ≫
                  (M.R_gen.hom ⊗ₘ (componentIso δ M n).hom)) ⊗ₘ
                (componentIso δ M m).hom) := by
                  rw [tensorHom_comp_tensorHom]
                  simp
        simpa [componentIso, canonical, tensorPow_add, Category.assoc,
          ← id_tensorHom, ← tensorHom_id, tensorHom_comp_tensorHom,
          hAssocCollapse, associator_naturality, ih'] using
          hAssocPost.symm

/-! ### § 7.2 Adequacy and core-generator transport

The transport laws live here rather than in §5 because they refer to
`componentIso`, the canonical carrier isomorphism constructed in §7.1.
-/

/-- Represented Hom-as-content witness.

This avoids pretending that the endomorphism `hom_mor N M` alone is the
Hom/curry representation, and it also avoids forcing the ambient category's
internal Hom to be the intended semantic Hom.  The law supplies an explicit
represented Hom carrier, an isomorphism from the `R (N*M)` layer to that
carrier, an evaluation morphism, and a compatibility equation saying the
stored `hom_mor` acts trivially after passing to the representing carrier. -/
structure HomCurryCoherence {δ : C} (M : TGUTRealisation C δ) (N M_ : ℕ) where
  /-- The semantic Hom carrier represented by `R (N*M_)`. -/
  homCarrier : C
  /-- The `R (N*M_)` layer represents the chosen semantic Hom carrier. -/
  homIso : M.R (N * M_) ≅ homCarrier
  /-- Evaluation of represented semantic Hom content. -/
  eval : M.R N ⊗ homCarrier ⟶ M.R M_
  /-- The stored Hom generator is the identity once transported to the
      representing carrier. -/
  hom_mor_compat : M.hom_mor N M_ ≫ homIso.hom = homIso.hom

/-- Local diagonal witness for the squaring law.

Generic SMCCs have no canonical diagonal `X ⟶ X ⊗ X`; an adequate model
must therefore supply the diagonal through which `square_mor` factors. -/
structure SquareDiagonalCoherence {δ : C} (M : TGUTRealisation C δ) (n : ℕ) where
  /-- The diagonal represented by the squaring generator after unpacking
      `R (2*n)` as `R n ⊗ R n`. -/
  diagonal : M.R n ⟶ M.R n ⊗ M.R n
  /-- `square_mor` factors through the chosen diagonal. -/
  square_factors :
    M.square_mor n ≫
        (eqToIso (congrArg M.R (by omega : 2 * n = n + n))).hom ≫
        (M.R_tensor n n).hom =
      diagonal

/-- Idempotent factorisation witness for the V4 modality generator.

The shape is deliberately ops-level: it records the idempotent carrier
through which `modal_V4_mor` factors without claiming a canonical
universal definition in every SMCC. -/
structure ModalV4IdempotentCoherence {δ : C} (M : TGUTRealisation C δ) where
  /-- The carrier of the modality image. -/
  modalCarrier : C
  /-- Projection onto the modality carrier. -/
  project : M.R 2 ⊗ M.R 2 ⟶ modalCarrier
  /-- Inclusion back into `R 2 ⊗ R 2`. -/
  include_mor : modalCarrier ⟶ M.R 2 ⊗ M.R 2
  /-- The projection/inclusion pair is idempotent on the image. -/
  idempotent : project ≫ include_mor ≫ project = project
  /-- `modal_V4_mor` lands in that idempotent image. -/
  modal_factors : M.modal_V4_mor ≫ project ≫ include_mor = M.modal_V4_mor

/-- Wedderburn/end-object compatibility law using represented end data.

The field `iso4_mor : R 4 ≅ R 4` only stores a carrier
automorphism. The real P7b content is that `R 4` represents a semantic
endomorphism carrier for `R 2`, together with its action, unit, and
composition.  This structure records those represented operations and the
compatibility of the stored carrier automorphism with the represented end
carrier. -/
structure WedderburnEndCoherence {δ : C} (M : TGUTRealisation C δ) where
  /-- The represented semantic endomorphism carrier. -/
  endCarrier : C
  /-- The `R 4` layer represents the chosen endomorphism carrier of `R 2`. -/
  endIso : M.R 4 ≅ endCarrier
  /-- Action of represented endomorphisms on `R 2`. -/
  action : M.R 2 ⊗ endCarrier ⟶ M.R 2
  /-- The identity represented endomorphism. -/
  unit : 𝟙_ C ⟶ endCarrier
  /-- Composition of represented endomorphisms. -/
  comp : endCarrier ⊗ endCarrier ⟶ endCarrier
  /-- Acting by the represented identity is the identity action. -/
  action_unit :
    (ρ_ (M.R 2)).inv ≫ (𝟙 (M.R 2) ⊗ₘ unit) ≫ action = 𝟙 (M.R 2)
  /-- Acting by a composite agrees with successive actions. -/
  action_comp :
    (α_ (M.R 2) endCarrier endCarrier).hom ≫
        (𝟙 (M.R 2) ⊗ₘ comp) ≫ action =
      (action ⊗ₘ 𝟙 endCarrier) ≫ action
  /-- The stored Wedderburn carrier automorphism preserves the end carrier. -/
  wedderburn_compat : M.iso4_mor.hom ≫ endIso.hom = endIso.hom

namespace WedderburnEndCoherence

variable {δ : C} {M : TGUTRealisation C δ}

/-- The action transported back to the stored `R 4` carrier. -/
noncomputable def representedAction (h : WedderburnEndCoherence M) :
    M.R 2 ⊗ M.R 4 ⟶ M.R 2 := by
  exact (𝟙 (M.R 2) ⊗ₘ h.endIso.hom) ≫ h.action

/-- The represented identity transported back to the stored `R 4` carrier. -/
noncomputable def representedUnit (h : WedderburnEndCoherence M) :
    𝟙_ C ⟶ M.R 4 :=
  h.unit ≫ h.endIso.inv

/-- The represented composition transported back to the stored `R 4` carrier. -/
noncomputable def representedComp (h : WedderburnEndCoherence M) :
    M.R 4 ⊗ M.R 4 ⟶ M.R 4 :=
  (h.endIso.hom ⊗ₘ h.endIso.hom) ≫ h.comp ≫ h.endIso.inv

end WedderburnEndCoherence

/-- The proposition that the realisation `M` satisfies law `ℓ`.

The clauses are non-vacuous: where the raw realisation record does not
determine a law by itself, the law requires explicit witness data rather
than reducing to `True`. -/
def Satisfies {δ : C} (M : TGUTRealisation C δ) : TGUTLaw → Prop
  | .invo3_involutive   => M.invo3_mor ≫ M.invo3_mor = 𝟙 (M.R 3)
  | .iso4_iso      => Nonempty (WedderburnEndCoherence M)
  | .modal_V4_idempotent => Nonempty (ModalV4IdempotentCoherence M)
  | .compose_tensor_inverse N M_ =>
      (M.R_tensor N M_).hom ≫ M.compose_mor N M_ = 𝟙 (M.R (N + M_)) ∧
      M.compose_mor N M_ ≫ (M.R_tensor N M_).hom = 𝟙 (M.R N ⊗ M.R M_)
  | .hom_canonical_transport N M_ =>
      M.hom_mor N M_ ≫
          (componentIso δ M.toTGUTRealisationCore (N * M_)).hom =
        (componentIso δ M.toTGUTRealisationCore (N * M_)).hom ≫
          (canonical δ).hom_mor N M_
  | .invo3_canonical_transport =>
      M.invo3_mor ≫ (componentIso δ M.toTGUTRealisationCore 3).hom =
        (componentIso δ M.toTGUTRealisationCore 3).hom ≫
          (canonical δ).invo3_mor
  | .iso4_canonical_transport =>
      M.iso4_mor.hom ≫
          (componentIso δ M.toTGUTRealisationCore 4).hom =
        (componentIso δ M.toTGUTRealisationCore 4).hom ≫
          (canonical δ).iso4_mor.hom
  | .tensor_unit_left n =>
      (M.R_tensor 0 n).hom ≫
        (M.R_unit.hom ⊗ₘ 𝟙 (M.R n)) ≫
        (λ_ (M.R n)).hom =
          (eqToIso (congrArg M.R (Nat.zero_add n))).hom
  | .tensor_unit_right n =>
      (M.R_tensor n 0).hom ≫
        (𝟙 (M.R n) ⊗ₘ M.R_unit.hom) ≫
        (ρ_ (M.R n)).hom =
          (eqToIso (congrArg M.R (Nat.add_zero n))).hom
  | .tensor_assoc a b c =>
      (M.R_tensor (a + b) c).hom ≫
        ((M.R_tensor a b).hom ⊗ₘ 𝟙 (M.R c)) =
          (eqToIso (congrArg M.R (Nat.add_assoc a b c))).hom ≫
          (M.R_tensor a (b + c)).hom ≫
          (𝟙 (M.R a) ⊗ₘ (M.R_tensor b c).hom) ≫
          (α_ (M.R a) (M.R b) (M.R c)).inv
  | .square_diagonal n        => Nonempty (SquareDiagonalCoherence M n)
  | .compose_assoc a b c      =>
      ((M.compose_mor a b) ⊗ₘ 𝟙 (M.R c)) ≫
          M.compose_mor (a + b) c =
        (α_ (M.R a) (M.R b) (M.R c)).hom ≫
          (𝟙 (M.R a) ⊗ₘ M.compose_mor b c) ≫
          M.compose_mor a (b + c) ≫
          (eqToIso (congrArg M.R (Nat.add_assoc a b c))).inv
  | .compose_unit_right n     =>
      M.compose_mor n 0 =
        (𝟙 (M.R n) ⊗ₘ M.R_unit.hom) ≫
          (ρ_ (M.R n)).hom ≫
          (eqToIso (congrArg M.R (Nat.add_zero n))).inv
  | .compose_unit_left n      =>
      M.compose_mor 0 n =
        (M.R_unit.hom ⊗ₘ 𝟙 (M.R n)) ≫
          (λ_ (M.R n)).hom ≫
          (eqToIso (congrArg M.R (Nat.zero_add n))).inv
  | .hom_NM_curry_compat N M_  => Nonempty (HomCurryCoherence M N M_)

/-- A realisation satisfies every law selected by a presentation. -/
def SatisfiesPresentation {δ : C} (M : TGUTRealisation C δ)
    (P : TGUTPresentation) : Prop :=
  ∀ ℓ, P.laws ℓ → M.Satisfies ℓ

/-- An *adequate* realisation satisfies every intrinsic law in the standard
presentation.  Canonical comparison, semantic closed/end-object, and ops laws
are split into separate predicates below so `IsAdequate` remains satisfiable
by the intended instance files. -/
def IsAdequate {δ : C} (M : TGUTRealisation C δ) : Prop :=
  M.SatisfiesPresentation TGUTPresentation.standard

/-- The realisation satisfies the canonical-transport comparison laws for
the `componentIso` comparison to `canonical δ`. -/
def HasCanonicalTransport {δ : C} (M : TGUTRealisation C δ) : Prop :=
  M.SatisfiesPresentation TGUTPresentation.canonicalTransport

/-- The realisation satisfies semantic Hom/Wedderburn laws requiring closed
or end-object infrastructure. -/
def HasSemanticCoherence {δ : C} (M : TGUTRealisation C δ) : Prop :=
  M.SatisfiesPresentation TGUTPresentation.semantic

/-- The realisation satisfies ops-level laws for the instance-specific
generators. -/
def HasOpsCoherence {δ : C} (M : TGUTRealisation C δ) : Prop :=
  M.SatisfiesPresentation TGUTPresentation.opsCoherence

/-- The R-kernel boundary facts needed to account for scoped sayings.

These facts do not add new `T_GUT` generators.  They expose the generic
R-family information accounting layer: projection fibers, partial coverage,
law-mediated recovery, predicate descent, operation descent, and the odd/even
residual boundaries. -/
structure RScopeBoundary : Prop where
  /-- A block projection fiber over `R N` has exactly `2^K` completions. -/
  visible_fiber_card :
    ∀ (N K : ℕ) (a : SSBX.Foundation.R.R N),
      Fintype.card { w : SSBX.Foundation.R.R (N + K) //
        SSBX.Foundation.R.R.visible w = a } = 2 ^ K
  /-- If the residual rank is nonzero, the visible carrier alone cannot recover it. -/
  no_carrier_recovery :
    ∀ {N K : ℕ}, 0 < K →
      ¬ SSBX.Foundation.R.R.CarrierRecoversResidual N K
  /-- A set of residual labels covers all full words exactly when it is all labels. -/
  coverage_complete :
    ∀ (N K : ℕ) (Q : Set (SSBX.Foundation.R.R K)),
      SSBX.Foundation.R.R.coveredBy (N := N) (K := K) Q = Set.univ ↔
        Q = Set.univ
  /-- A law that determines residual labels upgrades equal visible parts to full equality. -/
  law_recovers :
    ∀ (N K : ℕ) (P : SSBX.Foundation.R.R (N + K) → Prop),
      SSBX.Foundation.R.R.LawDeterminesResidual P →
        ∀ {w₁ w₂ : SSBX.Foundation.R.R (N + K)},
          P w₁ → P w₂ →
            SSBX.Foundation.R.R.visible w₁ = SSBX.Foundation.R.R.visible w₂ →
              w₁ = w₂
  /-- Predicate descent through the block scope is independence from residual labels. -/
  block_predicate_descent :
    ∀ (N K : ℕ) (P : SSBX.Foundation.R.R (N + K) → Prop),
      (SSBX.Foundation.R.R.blockScope N K).DescendsPred P ↔
        ∀ (a : SSBX.Foundation.R.R N)
          (q₁ q₂ : SSBX.Foundation.R.R K),
            P (SSBX.Foundation.R.R.slice a q₁) ↔
              P (SSBX.Foundation.R.R.slice a q₂)
  /-- Mask translation descends through the block scope by projecting the mask. -/
  block_mask_descent :
    ∀ (N K : ℕ) (m : SSBX.Foundation.R.R (N + K)),
      (SSBX.Foundation.R.R.blockScope N K).DescendsEndOp
        (fun w => w + m)
  /-- Every odd rank splits as an even prefix and a one-bit residual. -/
  odd_residual :
    ∀ n : ℕ,
      Nonempty
        (SSBX.Foundation.R.R (2 * n + 1) ≃
          SSBX.Foundation.R.R (2 * n) × SSBX.Foundation.R.R 1)
  /-- The next even rank splits as the same even prefix and a two-bit residual. -/
  next_even_residual :
    ∀ n : ℕ,
      Nonempty
        (SSBX.Foundation.R.R (2 * n + 2) ≃
          SSBX.Foundation.R.R (2 * n) × SSBX.Foundation.R.R 2)

/-- The generic R-scope boundary package supplied by the R tower kernel. -/
theorem rScopeBoundary : RScopeBoundary where
  visible_fiber_card := by
    intro N K a
    exact SSBX.Foundation.R.R.visibleFiber_card_pow (N := N) (K := K) a
  no_carrier_recovery := by
    intro N K hK
    exact SSBX.Foundation.R.R.not_carrierRecoversResidual_of_pos
      (N := N) (K := K) hK
  coverage_complete := by
    intro N K Q
    exact SSBX.Foundation.R.R.coveredBy_eq_univ_iff (N := N) (K := K) Q
  law_recovers := by
    intro N K P hP w₁ w₂ hw₁ hw₂ hv
    exact SSBX.Foundation.R.R.full_eq_of_lawDeterminesResidual
      (N := N) (K := K) (P := P) hP hw₁ hw₂ hv
  block_predicate_descent := by
    intro N K P
    exact SSBX.Foundation.R.R.blockScope_descendsPred_iff
      (N := N) (K := K) P
  block_mask_descent := by
    intro N K m
    exact SSBX.Foundation.R.R.blockScope_mask_descends
      (N := N) (K := K) m
  odd_residual := by
    intro n
    exact ⟨SSBX.Foundation.R.R.oddResidualEquiv n⟩
  next_even_residual := by
    intro n
    exact ⟨SSBX.Foundation.R.R.nextEvenResidualEquiv n⟩

/-- A realisation has the generic R-scope boundary accounting layer. -/
def HasScopeCoherence {δ : C} (_M : TGUTRealisation C δ) : Prop :=
  RScopeBoundary

omit [SymmetricCategory C] in
/-- The R-scope boundary is generic kernel mathematics, independent of the
particular realisation. -/
theorem hasScopeCoherence {δ : C} (M : TGUTRealisation C δ) :
    M.HasScopeCoherence :=
  rScopeBoundary

/-- Adequacy exposes the concrete `invo3` involutivity law. -/
theorem invo3_involutive_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) :
    M.invo3_mor ≫ M.invo3_mor = 𝟙 (M.R 3) :=
  h .invo3_involutive trivial

/-- Adequacy exposes the local law identifying `compose_mor` with the inverse
of the tensor decomposition. -/
theorem compose_tensor_inverse_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) (N M_ : ℕ) :
    (M.R_tensor N M_).hom ≫ M.compose_mor N M_ = 𝟙 (M.R (N + M_)) ∧
      M.compose_mor N M_ ≫ (M.R_tensor N M_).hom = 𝟙 (M.R N ⊗ M.R M_) :=
  h (.compose_tensor_inverse N M_) trivial

/-- Canonical-transport data exposes the Hom generator's comparison square. -/
theorem hom_canonical_transport_of_canonical_transport
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasCanonicalTransport) (N M_ : ℕ) :
    M.hom_mor N M_ ≫
        (componentIso δ M.toTGUTRealisationCore (N * M_)).hom =
      (componentIso δ M.toTGUTRealisationCore (N * M_)).hom ≫
        (canonical δ).hom_mor N M_ :=
  h (.hom_canonical_transport N M_) trivial

/-- Canonical-transport data exposes the `invo3` generator's comparison square. -/
theorem invo3_canonical_transport_of_canonical_transport
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasCanonicalTransport) :
    M.invo3_mor ≫ (componentIso δ M.toTGUTRealisationCore 3).hom =
      (componentIso δ M.toTGUTRealisationCore 3).hom ≫
        (canonical δ).invo3_mor :=
  h .invo3_canonical_transport trivial

/-- Canonical-transport data exposes the Wedderburn generator's comparison square. -/
theorem iso4_canonical_transport_of_canonical_transport
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasCanonicalTransport) :
    M.iso4_mor.hom ≫
        (componentIso δ M.toTGUTRealisationCore 4).hom =
      (componentIso δ M.toTGUTRealisationCore 4).hom ≫
        (canonical δ).iso4_mor.hom :=
  h .iso4_canonical_transport trivial

/-- Semantic coherence exposes the Hom/curry representation law. -/
theorem hom_curry_coherence_of_semantic_coherence
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasSemanticCoherence) (N M_ : ℕ) :
    Nonempty (HomCurryCoherence M N M_) :=
  h (.hom_NM_curry_compat N M_) trivial

/-- Semantic coherence exposes the Wedderburn/end-object representation law. -/
theorem wedderburn_end_coherence_of_semantic_coherence
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasSemanticCoherence) :
    Nonempty (WedderburnEndCoherence M) :=
  h .iso4_iso trivial

/-- Ops coherence exposes the square/diagonal ops law. -/
theorem square_diagonal_coherence_of_ops_coherence
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasOpsCoherence) (n : ℕ) :
    Nonempty (SquareDiagonalCoherence M n) :=
  h (.square_diagonal n) trivial

/-- Ops coherence exposes the V4 idempotent-factorisation ops law. -/
theorem modal_V4_idempotent_coherence_of_ops_coherence
    {δ : C} (M : TGUTRealisation C δ) (h : M.HasOpsCoherence) :
    Nonempty (ModalV4IdempotentCoherence M) :=
  h .modal_V4_idempotent trivial

/-- Adequacy exposes associativity of the composition generator. -/
theorem compose_assoc_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) (a b c : ℕ) :
    ((M.compose_mor a b) ⊗ₘ 𝟙 (M.R c)) ≫
        M.compose_mor (a + b) c =
      (α_ (M.R a) (M.R b) (M.R c)).hom ≫
        (𝟙 (M.R a) ⊗ₘ M.compose_mor b c) ≫
        M.compose_mor a (b + c) ≫
        (eqToIso (congrArg M.R (Nat.add_assoc a b c))).inv :=
  h (.compose_assoc a b c) trivial

/-- Adequacy exposes the right unit law for the composition generator. -/
theorem compose_unit_right_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) (n : ℕ) :
    M.compose_mor n 0 =
      (𝟙 (M.R n) ⊗ₘ M.R_unit.hom) ≫
        (ρ_ (M.R n)).hom ≫
        (eqToIso (congrArg M.R (Nat.add_zero n))).inv :=
  h (.compose_unit_right n) trivial

/-- Adequacy exposes the left unit law for the composition generator. -/
theorem compose_unit_left_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) (n : ℕ) :
    M.compose_mor 0 n =
      (M.R_unit.hom ⊗ₘ 𝟙 (M.R n)) ≫
        (λ_ (M.R n)).hom ≫
        (eqToIso (congrArg M.R (Nat.zero_add n))).inv :=
  h (.compose_unit_left n) trivial

/-- Adequacy exposes the tensor-unit and tensor-associativity laws as
`CoreTensorCoherence` for the underlying core. -/
theorem core_tensor_coherence_of_adequate
    {δ : C} (M : TGUTRealisation C δ) (h : M.IsAdequate) :
    CoreTensorCoherence M.toTGUTRealisationCore where
  tensor_unit_left n := h (.tensor_unit_left n) trivial
  tensor_unit_right n := h (.tensor_unit_right n) trivial
  tensor_assoc a b c := h (.tensor_assoc a b c) trivial

/-- Intrinsic adequacy plus canonical transport gives the full
core-generator commuting squares for `componentIso`.

The `compose` square is derived from `compose_tensor_inverse` and the
tensor structural square. The remaining core-generator squares are explicit
transport laws in `TGUTLaw`, because the current carrier data alone does
not determine those transports. -/
theorem componentIso_generator_coherent_of_adequate_transport
    {δ : C} (M : TGUTRealisation C δ) (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport)
    (hStructural :
      CoreStructuralCoherence
        (M := M.toTGUTRealisationCore)
        (N := canonical δ)
        (componentIso δ M.toTGUTRealisationCore)) :
    CoreGeneratorCoherence
      (M := M.toTGUTRealisationCore)
      (N := canonical δ)
      (componentIso δ M.toTGUTRealisationCore) := by
  constructor
  · intro n m
    let i := componentIso δ M.toTGUTRealisationCore
    have hCompose := compose_tensor_inverse_of_adequate M hAdequate n m
    have hTensor := hStructural.tensor_hom n m
    change M.compose_mor n m ≫ (i (n + m)).hom =
      ((i n).hom ⊗ₘ (i m).hom) ≫ ((canonical δ).R_tensor n m).inv
    apply (Iso.eq_comp_inv ((canonical δ).R_tensor n m)).mpr
    calc
      (M.compose_mor n m ≫ (i (n + m)).hom) ≫
          ((canonical δ).R_tensor n m).hom
          =
        M.compose_mor n m ≫
          ((M.R_tensor n m).hom ≫ ((i n).hom ⊗ₘ (i m).hom)) := by
            simpa [Category.assoc, i] using
              congrArg (fun f => M.compose_mor n m ≫ f) hTensor
      _ =
        (M.compose_mor n m ≫ (M.R_tensor n m).hom) ≫
          ((i n).hom ⊗ₘ (i m).hom) := by
            simp [Category.assoc]
      _ = ((i n).hom ⊗ₘ (i m).hom) := by
            rw [hCompose.2]
            simp
  · intro n m
    simpa using hom_canonical_transport_of_canonical_transport M hTransport n m
  · simpa using invo3_canonical_transport_of_canonical_transport M hTransport
  · simpa using iso4_canonical_transport_of_canonical_transport M hTransport

/-- The carrier-level universal-sayability witness with explicit unit
and generator carrier maps. This is a non-invasive strengthening of
`componentIso`: it reuses the same layerwise isomorphisms and merely
packages their level-`0` and level-`1` morphisms for downstream code
that wants named carrier witnesses before the full γ.3 coherence
predicate is available. -/
noncomputable def coreRealIso (δ : C) (M : TGUTRealisationCore C δ) :
    CoreRealIso M (canonical δ) where
  iso := componentIso δ M

/-- **Carrier-level coherent universal sayability** — every Core
realisation is isomorphic to the canonical tensor-power realisation in
the minimal `CoreRealIso` sense, with named unit and generator carrier
maps supplied by `coreRealIso`. -/
theorem universal_sayability_core (δ : C) (M : TGUTRealisationCore C δ) :
    Nonempty (CoreRealIso M (canonical δ)) :=
  ⟨coreRealIso δ M⟩

/-- **Structurally coherent carrier-level universal sayability** — if the
`componentIso` family satisfies the concrete unit/generator/tensor
commuting-square predicate, then the universal-sayability witness upgrades
from the minimal `CoreRealIso` API to a `CoherentCoreRealIso`.

This is retained as the archived structural milestone: the stronger
adequacy-based theorem below now derives this hypothesis and the later
`universal_sayability_core_full` additionally records core-generator
coherence. -/
theorem universal_sayability_structural
    (δ : C) (M : TGUTRealisationCore C δ)
    (h : CoreStructuralCoherence (M := M) (N := canonical δ) (componentIso δ M)) :
    Nonempty (CoherentCoreRealIso M (canonical δ)) :=
  ⟨{ iso := componentIso δ M, structural_coherent := h }⟩

/-- Archived structural milestone of adequacy-threaded universal sayability.

Adequacy includes the tensor-unit and tensor-associativity law families,
so it supplies the `CoreTensorCoherence` needed by
`componentIso_structural_coherent`. New consumers should usually prefer
`universal_sayability_core_full`, which extends this witness with
core-generator coherence while keeping ops coherence per-instance. -/
theorem universal_sayability_structural_of_adequate
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate) :
    Nonempty
      (CoherentCoreRealIso M.toTGUTRealisationCore (canonical δ)) :=
  universal_sayability_structural
    δ
    M.toTGUTRealisationCore
    (componentIso_structural_coherent
      δ
      M.toTGUTRealisationCore
      (core_tensor_coherence_of_adequate M hAdequate))

/-- **Full core coherent universal sayability** — intrinsic adequacy plus
canonical transport upgrades the carrier iso to commute with the universal core generators
`compose / hom / invo3 / iso4` as well as the structural
unit/generator/tensor data.

The theorem is intentionally Core-only: ops-level generators remain
instance-specific and are not part of this universal carrier milestone.
The canonical transport hypothesis is separate because it is not an
intrinsic law of every intended realisation. -/
theorem universal_sayability_core_full
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport) :
    Nonempty
      (FullCoherentCoreRealIso M.toTGUTRealisationCore (canonical δ)) := by
  let hStructural :=
    componentIso_structural_coherent
      δ
      M.toTGUTRealisationCore
      (core_tensor_coherence_of_adequate M hAdequate)
  exact
    ⟨{ iso := componentIso δ M.toTGUTRealisationCore
       structural_coherent := hStructural
       generator_coherent :=
        componentIso_generator_coherent_of_adequate_transport
          M hAdequate hTransport hStructural }⟩

/-- The canonical comparison map as a non-vacuous morphism of core
realisations once intrinsic adequacy and canonical transport are supplied. -/
noncomputable def componentIso_core_realisation_hom_of_adequate_transport
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport) :
    CoreRealisationHom M.toTGUTRealisationCore (canonical δ) := by
  let hStructural :=
    componentIso_structural_coherent
      δ
      M.toTGUTRealisationCore
      (core_tensor_coherence_of_adequate M hAdequate)
  exact
    FullCoherentCoreRealIso.toCoreRealisationHom
      { iso := componentIso δ M.toTGUTRealisationCore
        structural_coherent := hStructural
        generator_coherent :=
          componentIso_generator_coherent_of_adequate_transport
            M hAdequate hTransport hStructural }

/-- Core universal sayability as a naturality-carrying morphism. -/
theorem universal_sayability_core_natural
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport) :
    Nonempty (CoreRealisationHom M.toTGUTRealisationCore (canonical δ)) :=
  ⟨componentIso_core_realisation_hom_of_adequate_transport
    δ M hAdequate hTransport⟩

/-- The complete generic law package currently supplied by the split
adequacy, transport, semantic, and ops predicates.

This bundles the full core carrier/generator iso together with the
non-vacuous semantic and ops-law obligations.
It still does not assert per-instance ops equivalence to a canonical ops
model; that requires `FullCoherentRealIso` in the relevant instance file. -/
structure CompleteUniversalSayability {δ : C} (M : TGUTRealisation C δ) where
  /-- Full core carrier/generator coherence with the canonical core. -/
  core :
    FullCoherentCoreRealIso M.toTGUTRealisationCore (canonical δ)
  /-- Hom/curry semantics for every Hom generator. -/
  hom_curry : ∀ n m, Nonempty (HomCurryCoherence M n m)
  /-- Wedderburn/end-object semantics. -/
  wedderburn_end : Nonempty (WedderburnEndCoherence M)
  /-- Square/diagonal laws for the ops layer. -/
  square_diagonal : ∀ n, Nonempty (SquareDiagonalCoherence M n)
  /-- V4 idempotent factorisation for the ops layer. -/
  modal_V4_idempotent : Nonempty (ModalV4IdempotentCoherence M)
  /-- Associativity of the composition generator. -/
  compose_assoc : ∀ a b c,
    ((M.compose_mor a b) ⊗ₘ 𝟙 (M.R c)) ≫
        M.compose_mor (a + b) c =
      (α_ (M.R a) (M.R b) (M.R c)).hom ≫
        (𝟙 (M.R a) ⊗ₘ M.compose_mor b c) ≫
        M.compose_mor a (b + c) ≫
        (eqToIso (congrArg M.R (Nat.add_assoc a b c))).inv
  /-- Right unit law for the composition generator. -/
  compose_unit_right : ∀ n,
    M.compose_mor n 0 =
      (𝟙 (M.R n) ⊗ₘ M.R_unit.hom) ≫
        (ρ_ (M.R n)).hom ≫
        (eqToIso (congrArg M.R (Nat.add_zero n))).inv
  /-- Left unit law for the composition generator. -/
  compose_unit_left : ∀ n,
    M.compose_mor 0 n =
      (M.R_unit.hom ⊗ₘ 𝟙 (M.R n)) ≫
        (λ_ (M.R n)).hom ≫
        (eqToIso (congrArg M.R (Nat.zero_add n))).inv

/-- Complete universal sayability together with the R-kernel scope boundary.

This layer states the boundary accounting around a saying: which visible scope
is being used, what residual information is hidden by that scope, which
judgments descend, and which operations can be run after projection. -/
structure ScopeAwareUniversalSayability {δ : C} (M : TGUTRealisation C δ) where
  /-- The existing complete carrier, semantic, and ops law package. -/
  complete : CompleteUniversalSayability M
  /-- The generic R-scope information accounting layer. -/
  scope : M.HasScopeCoherence

/-- **Complete generic T_GUT law package from the split law predicates**.

Intrinsic adequacy supplies structural and compose laws.  Canonical
transport supplies the comparison-specific generator squares.  Semantic
and ops coherence supply the remaining non-vacuous law witnesses. -/
theorem universal_sayability_complete_of_law_packages
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport)
    (hSemantic : M.HasSemanticCoherence)
    (hOps : M.HasOpsCoherence) :
    Nonempty (CompleteUniversalSayability M) := by
  let hStructural :=
    componentIso_structural_coherent
      δ
      M.toTGUTRealisationCore
      (core_tensor_coherence_of_adequate M hAdequate)
  exact ⟨
    { core :=
        { iso := componentIso δ M.toTGUTRealisationCore
          structural_coherent := hStructural
          generator_coherent :=
            componentIso_generator_coherent_of_adequate_transport
              M hAdequate hTransport hStructural }
      hom_curry := fun n m => hom_curry_coherence_of_semantic_coherence M hSemantic n m
      wedderburn_end := wedderburn_end_coherence_of_semantic_coherence M hSemantic
      square_diagonal := fun n => square_diagonal_coherence_of_ops_coherence M hOps n
      modal_V4_idempotent := modal_V4_idempotent_coherence_of_ops_coherence M hOps
      compose_assoc := fun a b c => compose_assoc_of_adequate M hAdequate a b c
      compose_unit_right := fun n => compose_unit_right_of_adequate M hAdequate n
      compose_unit_left := fun n => compose_unit_left_of_adequate M hAdequate n }⟩

/-- **Scope-aware universal sayability**.

This is the conservative bridge from `T_GUT` to the R-scope theory: the usual
complete law package says the realisation can express the same R-core; the
scope boundary says whether a scoped expression is lossless, complete, or
recoverable only through an additional law. -/
theorem universal_sayability_scope_aware_of_law_packages
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport)
    (hSemantic : M.HasSemanticCoherence)
    (hOps : M.HasOpsCoherence) :
    Nonempty (ScopeAwareUniversalSayability M) := by
  rcases universal_sayability_complete_of_law_packages
    δ M hAdequate hTransport hSemantic hOps with ⟨hComplete⟩
  exact ⟨{ complete := hComplete, scope := hasScopeCoherence M }⟩

/-- Backward-compatible name for the complete law-package theorem.

Despite the name, intrinsic adequacy alone is intentionally not enough:
canonical transport, semantic closed/end-object coherence, and ops
coherence are separate law packages. -/
theorem universal_sayability_complete_of_adequate
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport)
    (hSemantic : M.HasSemanticCoherence)
    (hOps : M.HasOpsCoherence) :
    Nonempty (CompleteUniversalSayability M) :=
  universal_sayability_complete_of_law_packages
    δ M hAdequate hTransport hSemantic hOps

/-- **Legacy carrier-level universal sayability** — in any SMCC `C` with
chosen `δ`, every core realisation `M` has a layerwise component iso to
the canonical tensor-power realisation `canonical δ`.

**Proof strategy (Path 2 — layer-by-layer)**: the family is constructed
by `componentIso` above, by induction on `n` using the three structural
isos `R_unit / R_gen / R_tensor` of `M`.

**What this legacy theorem does NOT prove**:
* commutation with core generators — use `universal_sayability_core_full`
  for the non-vacuous Core theorem over `compose`, `hom`, `invo3`, and
  `iso4`.
* commutation with ops-level generators (`square`, `modal_V4`, `morP3`),
  which remains per-instance because those operations are not canonical in
  an arbitrary SMCC.
* naturality across morphisms of realisations — `RealIso` is currently
  bundled as iso-only, not as a 2-cell in a category of realisations.

**Specializations** (per `gut-c-doctrine.md` v0.2 §3.4):

| Base `C`       | `δ`         | Conclusion `M ≅ R_C` means … |
|---|---|---|
| `FinVect_{F_q}` | `F_q`       | `M = R`-family-over-`F_q` (recovers GUT-A/B algebraic) |
| `HeytAlg`       | `Prop`      | `M = ` Heyting R-family (new GUT-Heyting) |
| `FdHilb`        | `ℂ²` qubit  | `M = ` quantum stabilizer-style R-family (new GUT-Quantum) |
| `Frm`           | `Ω` Sierpinski | `M = ` topological R-family (new GUT-Topological) |
-/
theorem universal_sayability (δ : C) (M : TGUTRealisationCore C δ) :
    Nonempty (RealIso M (canonical δ)) :=
  ⟨{ iso := componentIso δ M }⟩

end UniversalSayability

/-! ## § 8 Reduction lemmas to GUT-A / GUT-B (sketches)

For the algebraic specializations (`C = FinVect_{F_q}`) the Universal
Sayability theorem above is intended to *recover* the existing
`T5_general` from `Foundation/R/UniquenessGeneral.lean`. We do not
formalize the reduction here; the file is the *abstract* layer of the
γ.1 framework. Concrete bridges live in the planned
`Foundation/Doctrine/Instance/Algebraic.lean`. -/

/-! ## § 9 Notes on the (3 × 3) of (P-property, base, specialisation)

Per `gut-c-doctrine.md` v0.2 §3.5, the same syntactic generator
(e.g. `morP3 N M`, encoding P3) gives different *concrete* content in
each base SMCC:

| Generator | `FinVect_{F_q}` | `HeytAlg` | `FdHilb` | `Frm` |
|---|---|---|---|---|
| `morP3` (P3)      | bilinear forms / Arf | Heyting lattice morphisms | dagger-symmetric forms | frame morphisms |
| `square` (P4)      | tensor squaring     | meet idempotence | tensor squaring  | meet squaring |
| `hom` (P5)         | LinHom = R(NM)      | Heyting impl    | dagger duality    | frame impl |
| `modal_V4` (P6)    | V₄ Shi              | classical mod.  | Pauli mod phase   | Sierpinski-like |
| `iso4` (P7b)| Mat₂(F_q)          | End(R₂) lattice | M₂(ℂ)             | End frame |

The single `T_GUT` presentation in this file is the *universal* one;
the per-base specializations are accessed via the concrete realisation
constructor `canonical` instantiated at the appropriate `(C, δ)`.
-/

end TGUTRealisation

end SSBX.Foundation.Doctrine
