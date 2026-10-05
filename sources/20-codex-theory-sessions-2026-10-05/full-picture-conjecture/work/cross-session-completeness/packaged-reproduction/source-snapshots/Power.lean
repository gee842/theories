/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / GUT-C Phase 1.5 (Power 1999 Theorem 4.5 for upstream Mathlib PR-3)
-/
import Mathlib.CategoryTheory.Enriched.Basic
import Mathlib.CategoryTheory.Enriched.Ordinary.Basic
import SSBX.Foundation.Enriched.Cotensor
import SSBX.Foundation.Enriched.Weighted
import SSBX.Foundation.Enriched.Monad
import SSBX.Foundation.Enriched.Finitary
import SSBX.Foundation.Doctrine.EnrichedLawvereTheory

/-!
# Power 1999 Theorem 4.5: V-enriched Lawvere theories ≃ finitary V-monads

This is the **central theorem** of Power 1999's *Enriched Lawvere theories*
(TAC 6 no. 7), and the **load-bearing** dependency of Phase 4
(`enriched_universal_sayability`) of the GUT-C v0.6 plan.

## Statement

The 2-category of V-enriched Lawvere theories is 2-equivalent to the
2-category of finitary V-monads on V.

Specifically, there are functors

* `theoryToMonad : EnrichedLawvereTheory V T → FinitaryEnrichedMonad V T'`
* `monadToTheory : FinitaryEnrichedMonad V T' → EnrichedLawvereTheory V T`

which are mutual inverses up to natural isomorphism.

## Status (Phase 1.5 supplied-data boundary)

This file delivers a **supplied-data boundary**:

* A projection from supplied theory-to-monad data to a finitary V-monad.
* A projection from supplied monad-to-theory data to a reconstructed carrier.
* A comparison package that must be supplied explicitly by the caller.

The actual proof of the equivalence is **not** fabricated here.  The central
technical content of Power 1999's paper, roughly a 30-page proof, remains the
substantial mathematical work of Phase 1.5 elaboration.

When the proof is closed, the supplied-data boundary here should be replaced
with a constructive proof following Power 1999 §4 + Kelly 1982 Ch. 5.

## SSBX vendor notice

Phase 1.5 of GUT-C (see plan §4.2 Sub-PR 3.5), intended for upstream as
`Mathlib.CategoryTheory.Enriched.Power`. Vendored under SSBX while review
proceeds.

## References

* [Power, J. *Enriched Lawvere theories*, TAC 6 no. 7 (1999), 83-93][Pow99]
  — THE central reference (this file's content); esp. §3 (forward direction),
  §4 (backward direction + Theorem 4.5)
* [Hyland, M. and Power, J. *The category theoretic understanding of
  universal algebra*, ENTCS 172 (2007)][HP07] §3 — modern exposition
* [Kelly, G. M., *Basic Concepts of Enriched Category Theory*, Cambridge
  1982; TAC Reprint 10 (2005)][Kel82] §6.5 (V-T-models), Ch. 5 (V-monads)
* [Lawvere, F. W. *Functorial Semantics of Algebraic Theories*, PhD 1963;
  TAC Reprint 5 (2004)][Law63] — V = Set case
-/

@[expose] public section

universe w' v' v u u'

open CategoryTheory Category MonoidalCategory

namespace CategoryTheory.Enriched.Power

variable (V : Type u') [Category.{v'} V] [MonoidalCategory V]

/-! ## §1 The forward functor: theory → monad

Given a V-enriched Lawvere theory `T`, the **algebraic V-monad** of `T`
acts on `V` by sending `X : V` to the free `T`-algebra on `X`. This is the
forward direction of Power 1999 Theorem 4.5.

Current boundary — full construction is Power 1999 §3. -/

/-- A V-enriched Lawvere theory induces a finitary V-monad once the Power
forward-construction data is supplied. -/
theorem theory_induces_monad_statement
    (T : Type u) [Category.{v} T] [EnrichedOrdinaryCategory V T]
    [EnrichedDoctrine.EnrichedLawvereTheory.{w'} V T]
    (data : EnrichedDoctrine.TheoryMonadData V T) :
    Nonempty (EnrichedDoctrine.FinitaryVMonad V) :=
  ⟨EnrichedDoctrine.monadOfTheory V T data⟩

/-! ## §2 The backward functor: monad → theory

Given a finitary V-monad on V, the **algebraic theory** of `T` is the
opposite of the V-category of free algebras `Kl(T)^op` restricted to the
"finitely-presented" objects (i.e., free algebras on `n`-fold tensor powers
of the generator).

Current boundary — full construction is Power 1999 §4.  The supplied reverse
data includes the carrier, category, enrichment, and enriched Lawvere-theory
structure.  We expose that package directly rather than a bare carrier type. -/

/-- A finitary V-monad induces a reconstructed V-enriched Lawvere theory once
the Power reverse-construction data is supplied. -/
theorem monad_induces_theory_package
    (M : EnrichedDoctrine.FinitaryVMonad V)
    (data : EnrichedDoctrine.MonadTheoryData.{w', v', u'} V M) :
    Nonempty (EnrichedDoctrine.MonadTheoryData.{w', v', u'} V M) :=
  EnrichedDoctrine.theoryOfMonadPackage V M data

/-! ## §3 Power 1999 Theorem 4.5 — the central equivalence

The 2-category of V-enriched Lawvere theories is 2-equivalent to the
2-category of finitary V-monads on V.

For Phase 1.5 minimum-viable we state the **1-categorical reduction**:
there is an equivalence of underlying 1-categories. The full 2-categorical
structure (Kelly-style adjoint 2-equivalence with coherent 2-cells) is
deferred to a follow-up sub-PR.

### Proof status

The theorem below returns explicit comparison data supplied by the caller.
Closing the real theorem means replacing this boundary with a constructive
Power 1999 §§3-4 formalisation. -/

/-- **Power 1999 Theorem 4.5** (1-categorical reduction).

V-enriched Lawvere theories and finitary V-monads on V are in bijective
correspondence at the 1-categorical level.

The full 2-equivalence (with adjoint 2-cells) is a follow-up; here we state
the 1-categorical version sufficient for downstream consumers
(Phase 2 `EnrichedLawvereTheory.lean` closing, Phase 4
`enriched_universal_sayability`).

**Proof boundary**: supplied comparison data.  Full proof is Power 1999
§§3-4. -/
theorem theory_monad_equiv
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :
    Nonempty
      (EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :=
  EnrichedDoctrine.enriched_lawvere_iff_finitary_v_monad V data

/-- Supplied comparison data gives the Power forward direction for each
chosen enriched Lawvere theory.

This is an accessor for explicit `theoryToMonad` data, not a construction of
the Power 1999 monad. -/
theorem comparison_theory_induces_monad
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (T : Type u) [Category.{v} T] [EnrichedOrdinaryCategory V T]
    [EnrichedDoctrine.EnrichedLawvereTheory.{w'} V T] :
    Nonempty (EnrichedDoctrine.FinitaryVMonad V) :=
  theory_induces_monad_statement V T (data.theoryToMonad T)

/-- Supplied comparison data exposes the raw theory-to-monad package for each
chosen enriched Lawvere theory. -/
theorem comparison_theoryToMonad_data_nonempty
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (T : Type u) [Category.{v} T] [EnrichedOrdinaryCategory V T]
    [EnrichedDoctrine.EnrichedLawvereTheory.{w'} V T] :
    Nonempty (EnrichedDoctrine.TheoryMonadData V T) :=
  ⟨data.theoryToMonad T⟩

/-- Supplied comparison data exposes the raw theory-to-monad package for each
chosen enriched Lawvere theory.  This is the direct payload accessor behind
`comparison_theoryToMonad_data_nonempty`. -/
def comparison_theoryToMonad_data
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (T : Type u) [Category.{v} T] [EnrichedOrdinaryCategory V T]
    [EnrichedDoctrine.EnrichedLawvereTheory.{w'} V T] :
    EnrichedDoctrine.TheoryMonadData V T :=
  data.theoryToMonad T

/-- Supplied comparison data gives the Power reverse direction as a full
supplied reconstructed-theory package.

This is still supplied data rather than a proof of Power 1999, but it no
longer hides category/enrichment/Lawvere-theory obligations behind a bare
carrier type. -/
theorem comparison_monad_induces_theory_package
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (M : EnrichedDoctrine.FinitaryVMonad V) :
    Nonempty (EnrichedDoctrine.MonadTheoryData.{w', v', u'} V M) :=
  monad_induces_theory_package V M (data.monadToTheory M)

/-- Supplied comparison data exposes the raw monad-to-theory package for each
chosen finitary V-monad. -/
theorem comparison_monadToTheory_data_nonempty
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (M : EnrichedDoctrine.FinitaryVMonad V) :
    Nonempty (EnrichedDoctrine.MonadTheoryData.{w', v', u'} V M) :=
  ⟨data.monadToTheory M⟩

/-- Supplied comparison data exposes the raw monad-to-theory package for each
chosen finitary V-monad.  This is the direct payload accessor behind
`comparison_monadToTheory_data_nonempty`. -/
def comparison_monadToTheory_data
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V)
    (M : EnrichedDoctrine.FinitaryVMonad V) :
    EnrichedDoctrine.MonadTheoryData.{w', v', u'} V M :=
  data.monadToTheory M

/-- Power-facing accessor for the supplied theory-side round-trip law. -/
theorem power_comparison_theory_roundTrip_holds
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :
    data.theoryRoundTrip :=
  EnrichedDoctrine.comparison_theory_roundTrip_holds V data

/-- Power-facing accessor for the supplied monad-side round-trip law. -/
theorem power_comparison_monad_roundTrip_holds
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :
    data.monadRoundTrip :=
  EnrichedDoctrine.comparison_monad_roundTrip_holds V data

/-! ## §4 Bridge to `EnrichedLawvereTheory.lean` (Phase 2 prep)

`formal/SSBX/Foundation/Doctrine/EnrichedLawvereTheory.lean` now exposes the
same supplied-data comparison boundary.  This file re-exports the Power-facing
projection name that downstream work can consume.

We provide here the bridge-statement that Phase 2 will consume. -/

/-- Bridge: supplied Power comparison data is available at the Power-facing
boundary. -/
theorem power_bridge_for_enriched_lawvere_theory
    (data :
      EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :
    Nonempty
      (EnrichedDoctrine.EnrichedLawvereFinitaryMonadComparisonData.{w', v', v, u, u'} V) :=
  theory_monad_equiv V data

end CategoryTheory.Enriched.Power
