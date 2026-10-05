/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / Full GUT frontier pass
-/
import SSBX.Foundation.Doctrine.FullGUTNativeFrontier
import SSBX.Foundation.Doctrine.FullGUTEnrichedFrontier
import SSBX.Foundation.Doctrine.FullGUTLawvereFrontier
import SSBX.Foundation.Doctrine.FullGUTT5Frontier
import SSBX.Foundation.Doctrine.FullGUTTier1Frontier
import SSBX.Foundation.Doctrine.FullGUTTier2Frontier
import SSBX.Foundation.Doctrine.FullGUTTier3Frontier
import SSBX.Foundation.Doctrine.FullGUTG11Frontier
import SSBX.Foundation.R.D6_Tests

/-!
# Foundation.Doctrine.FullGUTFrontier

Single downstream package for the current theorem-grade FullGUT frontier.

This file is intentionally only an aggregator.  It combines already-closed
downstream packages without importing native semantic or finite-field
dependencies back into `FullGUT.lean`.
-/

namespace SSBX.Foundation.Doctrine.FullGUTFrontier

open SSBX.Foundation.Doctrine.FullGUTNativeFrontier
open SSBX.Foundation.Doctrine.FullGUTT5Frontier
open SSBX.Foundation.Doctrine.FullGUTTier1Frontier
open SSBX.Foundation.Doctrine.FullGUTTier2Frontier
open SSBX.Foundation.Doctrine.FullGUTTier3Frontier
open SSBX.Foundation.Doctrine.FullGUTG11Frontier
open SSBX.Foundation.Doctrine.FullGUT
open SSBX.Foundation.Doctrine.Instance
open SSBX.Foundation.R.ClaimZ
open SSBX.Foundation.R.ClaimZF2
open SSBX.Foundation.R.D6Tests
open SSBX.Foundation.R.UniquenessAlgebraic
open SSBX.Foundation.R.UniquenessF2
open SSBX.Foundation.R.UniquenessGeneral
open SSBX.Foundation.R.UniquenessGeneralField
open SSBX.Foundation.Wen.Embeddings.HeisenbergWeylZModP

universe u

/-- Scoped D6 audit certificate for the current FullGUT D5/F₂-D6 pair.

This is a compact downstream package for the exact fixed pair already proved
in `FullGUT.lean` plus the recorded-candidate audit from `D6_Tests.lean`.
It does not assert global D6 exhaustiveness for arbitrary future
falsification formulations. -/
structure CurrentScopedD6AuditCertificate : Type 1 where
  exact :
    D6ExactForD5 current_scoped_D5_claim claim_z_falsification_F2
  exact_from_component_coverage :
    D6ExactForD5 current_scoped_D5_claim claim_z_falsification_F2
  sound :
    D6SoundForD5 current_scoped_D5_claim claim_z_falsification_F2
  component_coverage :
    D6ComponentCoverageForD5 current_scoped_D5_claim claim_z_falsification_F2
  exhaustive :
    D6ExhaustiveForD5 current_scoped_D5_claim claim_z_falsification_F2
  iff_not_D5 :
    D6_holds claim_z_falsification_F2 ↔
      ¬D5_holds current_scoped_D5_claim
  refuted :
    ¬D6_holds claim_z_falsification_F2
  routes_refuted :
    ¬ claim_z_falsification_F2.not_analytic ∧
      ¬ claim_z_falsification_F2.not_synthetic ∧
      ¬ claim_z_falsification_F2.not_D2_consistent
  recorded_candidates_refuted :
    ¬ (is_hott_witness claim_z_falsification_F2 ∨
        is_ETCS_witness claim_z_falsification_F2 ∨
        is_SDG_witness claim_z_falsification_F2)
  /-- The currently recorded candidate predicates are exactly route-2
  synthetic-failure predicates for the concrete F₂ D6 bundle.
  This audits only the current record, not future D6 candidates. -/
  recorded_candidates_iff_synthetic_route :
    (is_hott_witness claim_z_falsification_F2 ∨
        is_ETCS_witness claim_z_falsification_F2 ∨
        is_SDG_witness claim_z_falsification_F2) ↔
      claim_z_falsification_F2.not_synthetic

/-- The current scoped D6 audit certificate is closed for the present
D5/F₂-D6 pair. -/
theorem current_scoped_D6_audit_certificate :
    Nonempty CurrentScopedD6AuditCertificate :=
  ⟨{
    exact := current_scoped_D6_exact_for_D5
    exact_from_component_coverage :=
      current_scoped_D6_exact_from_component_coverage
    sound := current_scoped_D6_sound_for_D5
    component_coverage := current_scoped_D6_component_coverage_for_D5
    exhaustive := current_scoped_D6_exhaustive_for_D5
    iff_not_D5 := current_scoped_D6_iff_not_D5
    refuted := current_scoped_D6_refuted_from_exactness
    routes_refuted := current_scoped_D6_all_routes_refuted_from_soundness
    recorded_candidates_refuted := F2_recorded_candidates_do_not_falsify
    recorded_candidates_iff_synthetic_route :=
      D6_candidate_record_iff_not_synthetic claim_z_falsification_F2 }⟩

/-- Direct audit accessor: the currently recorded HoTT/ETCS/SDG predicates
are exactly the current route-2 synthetic-failure predicate for the concrete
F₂ D6 bundle.

This does not claim that future D6 tests are exhausted by these recorded
candidate predicates. -/
theorem current_scoped_D6_recorded_candidates_iff_synthetic_route :
    (is_hott_witness claim_z_falsification_F2 ∨
        is_ETCS_witness claim_z_falsification_F2 ∨
        is_SDG_witness claim_z_falsification_F2) ↔
      claim_z_falsification_F2.not_synthetic :=
  D6_candidate_record_iff_not_synthetic claim_z_falsification_F2

/-- Current theorem-grade FullGUT frontier.

The native-semantic field packages the conditional/scoped FullGUT theorem stack
with the current native witness families.  The R/T5 field packages scoped T5
with the canonical finite-field all-split and split-coherent field branches.
The scoped D6 fields expose
the exact fixed-pair relation between the current scoped D5 package and the
concrete F₂ falsification bundle.  This remains a frontier certificate: it
does not make semantic witnesses automatic for every admissible system, and it
does not derive all-split data for raw non-canonical satisfiers or global D6
exhaustiveness. -/
structure CurrentFullGUTFrontier : Type (u + 2) where
  tier1 :
    Nonempty CurrentTier1Closure
  tier2 :
    Nonempty CurrentTier2Closure.{u}
  tier3 :
    Nonempty CurrentTier3Closure.{u}
  g11 :
    Nonempty CurrentG11Closure.{u}
  native_semantic :
    Nonempty (CurrentNativeSemanticFullGUTFrontier.{u})
  lawvere_theory :
    Nonempty (SSBX.Foundation.Doctrine.FullGUT.CurrentLawvereTheoryFullGUTFrontier.{u})
  enriched_lawvere :
    Nonempty
      (SSBX.Foundation.Doctrine.FullGUT.CurrentEnrichedLawvereFullGUTFrontier.{u, u, u})
  enriched_lawvere_finite_bridge :
    ∀ (V : Type u) [CategoryTheory.Category.{u} V] [CategoryTheory.MonoidalCategory.{u} V]
      (T : Type) [CategoryTheory.SmallCategory T]
      [CategoryTheory.EnrichedOrdinaryCategory V T]
      [CategoryTheory.EnrichedDoctrine.EnrichedLawvereTheory.{u, u, 0, 0, u} V T]
      [DecidableEq T] [Fintype T] [∀ X Y : T, Fintype (X ⟶ Y)],
      Nonempty
        (FaithfulRRealisation
          (categoryFormalPresentation T
            (CategoryTheory.EnrichedLawvereTheory.generator V T))
          Bool)
  enriched_lawvere_stream_bridge :
    ∀ (V : Type u) [CategoryTheory.Category.{u} V] [CategoryTheory.MonoidalCategory.{u} V]
      (T : Type) [CategoryTheory.SmallCategory T]
      [CategoryTheory.EnrichedOrdinaryCategory V T]
      [CategoryTheory.EnrichedDoctrine.EnrichedLawvereTheory.{u, u, 0, 0, u} V T]
      [DecidableEq T] [Encodable T]
      [∀ X Y : T, Encodable (X ⟶ Y)],
      Nonempty
        (FaithfulRStreamRealisation
          (categoryFormalPresentation T
            (CategoryTheory.EnrichedLawvereTheory.generator V T)))
  enriched_lawvere_type_model_bridge_equivalence :
    ∀ (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
      [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C],
      Nonempty
        (letI :
          CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
            (Type u) T :=
          CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
        CategoryTheory.Model T C ≌
          CategoryTheory.EnrichedDoctrine.EnrichedFiniteModel (Type u) T C)
  R_T5 : Nonempty CurrentRT5Frontier
  R_T5_canonical_field_all_split :
    ∀ k : Type, [Field k] → [Fintype k] → [DecidableEq k] →
      T5FieldDirectSumGUTBPackage (T5_field_canonical_auto k)
  R_T5_canonical_field_coherent_all_split :
    ∀ k : Type, [Field k] → [Fintype k] → [DecidableEq k] →
      ∃ hDirect :
        P1P7_Core.DirectSumStructuralIso
          (T5_field_canonical_auto k).toP1P7_Satisfier_Algebraic.toP1P7_Core,
        T5FieldCoherentDirectSumGUTBPackage
          (T5_field_canonical_auto k) hDirect
  R_T5_raw_core_successor_and_gated_direct_sum :
    ∀ {δ : Type} [Fintype δ] [DecidableEq δ] [Inhabited δ]
      (S : P1P7_Core δ),
        T5SuccessorGUTBPackage S
          ∧ (∀ hDirect : P1P7_Core.DirectSumStructuralIso S,
              T5CoherentDirectSumGUTBPackage S hDirect)
  R_T5_generic_split_coherent_GUT_B_package :
    ∀ {δ : Type} [Fintype δ] [DecidableEq δ]
      (S : P1P7_SplitCoherentCore δ),
        T5SplitCoherentGUTBPackage S
  R_T5_generic_coherent_from_direct_sum :
    ∀ {δ : Type} [Fintype δ] [DecidableEq δ]
      (S : P1P7_Core δ)
      (hDirect : P1P7_Core.DirectSumStructuralIso S),
        T5CoherentDirectSumGUTBPackage S hDirect
  R_T5_algebraic_coherent_from_direct_sum :
    ∀ (k : Type) [Field k] [Fintype k] [DecidableEq k]
      (S : P1P7_Satisfier_Algebraic k)
      (hDirect : P1P7_Core.DirectSumStructuralIso S.toP1P7_Core),
        T5AlgebraicCoherentDirectSumGUTBPackage S hDirect
  R_T5_field_ringEquiv_by_charClass :
    ∀ (k : Type) [Field k] [Fintype k] [DecidableEq k]
      (S : P1P7_Satisfier_Field k),
      @Nonempty
        (@RingEquiv
          (S.toP1P7_Satisfier_Algebraic.toP1P7_Core.carrier 4)
          (Matrix (Fin 2) (Fin 2) k)
          S.toP1P7_Satisfier_Algebraic.p7b_mul_instance (matMulInstance k)
          S.toP1P7_Satisfier_Algebraic.p7b_add_instance (matAddInstance k))
  R_T5_field_coherent_from_direct_sum :
    ∀ (k : Type) [Field k] [Fintype k] [DecidableEq k]
      (S : P1P7_Satisfier_Field k)
      (hDirect :
        P1P7_Core.DirectSumStructuralIso
          S.toP1P7_Satisfier_Algebraic.toP1P7_Core),
        T5FieldCoherentDirectSumGUTBPackage S hDirect
  R_T5_field_split_coherent_direct_sum :
    ∀ (k : Type) [Field k] [Fintype k] [DecidableEq k]
      (S : P1P7_SplitCoherentCore k),
        T5FieldDirectSumGUTBPackage (splitCoherentFieldSatisfier k S)
  R_T5_field_split_coherent_coherent :
    ∀ (k : Type) [Field k] [Fintype k] [DecidableEq k]
      (S : P1P7_SplitCoherentCore k),
      ∃ hDirect :
        P1P7_Core.DirectSumStructuralIso
          (splitCoherentFieldSatisfier k S).toP1P7_Satisfier_Algebraic.toP1P7_Core,
        T5FieldCoherentDirectSumGUTBPackage
          (splitCoherentFieldSatisfier k S) hDirect
  R_T5_f2_side_obligations :
    ∀ S : P1P7_Satisfier_F2,
      T5AItem8RInfty
        ∧ T5AItem9CoreModality
        ∧ T5AItem11AtomicRing S
        ∧ T5AItem11AtomicActionR
        ∧ Nonempty (T5AAtomicActionTransport S)
  D6_exact_from_component_coverage :
    ∀ {claim : D5_UniversalClaim} {falsif : D6_ClaimZFalsified},
      D6SoundForD5 claim falsif →
      D6ComponentCoverageForD5 claim falsif →
        D6ExactForD5 claim falsif
  D6_exact_routes_refuted_of_D5 :
    ∀ {claim : D5_UniversalClaim} {falsif : D6_ClaimZFalsified},
      D6ExactForD5 claim falsif →
      D5_holds claim →
        ¬ falsif.not_analytic ∧
          ¬ falsif.not_synthetic ∧
          ¬ falsif.not_D2_consistent
  scoped_D6_exact :
    D6ExactForD5 current_scoped_D5_claim claim_z_falsification_F2
  scoped_D6_sound :
    D6SoundForD5 current_scoped_D5_claim claim_z_falsification_F2
  scoped_D6_component_coverage :
    D6ComponentCoverageForD5 current_scoped_D5_claim claim_z_falsification_F2
  scoped_D6_exact_from_component_coverage :
    D6ExactForD5 current_scoped_D5_claim claim_z_falsification_F2
  scoped_D6_exhaustive :
    D6ExhaustiveForD5 current_scoped_D5_claim claim_z_falsification_F2
  scoped_D6_iff_not_D5 :
    D6_holds claim_z_falsification_F2 ↔
      ¬D5_holds current_scoped_D5_claim
  scoped_D6_of_not_D5 :
    ¬D5_holds current_scoped_D5_claim →
      D6_holds claim_z_falsification_F2
  scoped_D6_refuted :
    ¬D6_holds claim_z_falsification_F2
  scoped_D6_routes_refuted :
    ¬ claim_z_falsification_F2.not_analytic ∧
      ¬ claim_z_falsification_F2.not_synthetic ∧
      ¬ claim_z_falsification_F2.not_D2_consistent
  scoped_D6_recorded_candidates_refuted :
    ¬ (is_hott_witness claim_z_falsification_F2 ∨
        is_ETCS_witness claim_z_falsification_F2 ∨
        is_SDG_witness claim_z_falsification_F2)
  scoped_D6_recorded_candidates_iff_synthetic_route :
    (is_hott_witness claim_z_falsification_F2 ∨
        is_ETCS_witness claim_z_falsification_F2 ∨
        is_SDG_witness claim_z_falsification_F2) ↔
      claim_z_falsification_F2.not_synthetic
  scoped_D6_audit :
    Nonempty CurrentScopedD6AuditCertificate

/-- The current theorem-grade FullGUT frontier is closed at its stated scoped
boundary. -/
theorem current_full_gut_frontier :
    Nonempty CurrentFullGUTFrontier :=
  ⟨{
    tier1 := current_tier1_closure
    tier2 := current_tier2_closure
    tier3 := current_tier3_closure
    g11 := current_g11_closure
    native_semantic := current_native_semantic_full_gut_frontier
    lawvere_theory :=
      SSBX.Foundation.Doctrine.FullGUT.current_lawvere_theory_full_gut_frontier
    enriched_lawvere :=
      SSBX.Foundation.Doctrine.FullGUT.current_enriched_lawvere_full_gut_frontier
    enriched_lawvere_finite_bridge :=
      SSBX.Foundation.Doctrine.FullGUT.enriched_lawvere_finite_full_gut
    enriched_lawvere_stream_bridge :=
      SSBX.Foundation.Doctrine.FullGUT.enriched_lawvere_encodable_stream_full_gut
    enriched_lawvere_type_model_bridge_equivalence := by
      intro T C _ _ _ _
      exact ⟨CategoryTheory.EnrichedDoctrine.finiteTypeModelBridgeEquivalence T C⟩
    R_T5 := current_R_T5_frontier
    R_T5_canonical_field_all_split := fun k _ _ _ =>
      T5_field_direct_sum_GUT_B_package_canonical_auto k
    R_T5_canonical_field_coherent_all_split := fun k _ _ _ =>
      T5_field_coherent_GUT_B_package_canonical_auto k
    R_T5_raw_core_successor_and_gated_direct_sum := fun {_δ} _ _ _ S =>
      T5_raw_core_successor_and_gated_direct_sum S
    R_T5_generic_split_coherent_GUT_B_package := fun {_δ} _ _ S =>
      T5_split_coherent_GUT_B_package S
    R_T5_generic_coherent_from_direct_sum := fun {_δ} _ _ S hDirect =>
      T5_coherent_GUT_B_package_of_direct_sum S hDirect
    R_T5_algebraic_coherent_from_direct_sum := fun _k _ _ _ S hDirect =>
      T5_algebraic_coherent_GUT_B_package_of_direct_sum S hDirect
    R_T5_field_ringEquiv_by_charClass := fun _k _ _ _ S =>
      T5_field_ringEquiv_by_charClass S
    R_T5_field_coherent_from_direct_sum := fun _k _ _ _ S hDirect =>
      T5_field_coherent_GUT_B_package_of_direct_sum S hDirect
    R_T5_field_split_coherent_direct_sum := fun k _ _ _ S =>
      T5_field_split_coherent_direct_sum_GUT_B_package k S
    R_T5_field_split_coherent_coherent := fun k _ _ _ S =>
      T5_field_split_coherent_coherent_GUT_B_package k S
    R_T5_f2_side_obligations := T5_A_full_side_obligations
    D6_exact_from_component_coverage := fun hSound hCoverage =>
      D6ExactForD5.of_sound_and_component_coverage hSound hCoverage
    D6_exact_routes_refuted_of_D5 := fun hExact hD5 =>
      hExact.all_routes_refuted_of_D5 hD5
    scoped_D6_exact := current_scoped_D6_exact_for_D5
    scoped_D6_sound := current_scoped_D6_sound_for_D5
    scoped_D6_component_coverage :=
      current_scoped_D6_component_coverage_for_D5
    scoped_D6_exact_from_component_coverage :=
      current_scoped_D6_exact_from_component_coverage
    scoped_D6_exhaustive := current_scoped_D6_exhaustive_for_D5
    scoped_D6_iff_not_D5 := current_scoped_D6_iff_not_D5
    scoped_D6_of_not_D5 := current_scoped_D6_of_not_D5
    scoped_D6_refuted := current_scoped_D6_refuted_from_exactness
    scoped_D6_routes_refuted :=
      current_scoped_D6_all_routes_refuted_from_soundness
    scoped_D6_recorded_candidates_refuted :=
      F2_recorded_candidates_do_not_falsify
    scoped_D6_recorded_candidates_iff_synthetic_route :=
      current_scoped_D6_recorded_candidates_iff_synthetic_route
    scoped_D6_audit := current_scoped_D6_audit_certificate }⟩

/-- Direct top-level accessor for the scoped/coordinate Tier-1 closure
certificate. -/
theorem current_full_gut_tier1_closure :
    Nonempty CurrentTier1Closure :=
  current_tier1_closure

/-- Direct top-level accessor for the scoped/coordinate Tier-2 closure
certificate. -/
theorem current_full_gut_tier2_closure :
    Nonempty CurrentTier2Closure.{u} :=
  current_tier2_closure

/-- Direct top-level accessor for the scoped/coordinate Tier-3 closure
certificate. -/
theorem current_full_gut_tier3_closure :
    Nonempty CurrentTier3Closure.{u} :=
  current_tier3_closure

/-- Direct top-level accessor for the scoped G11 cut-1 closure certificate.

This closes canonical finite-field, prime-field, structure-gated arbitrary
field, and odd-prime discriminant branches only at their stated scopes. -/
theorem current_full_gut_g11_closure :
    Nonempty CurrentG11Closure.{u} :=
  current_g11_closure

/-- Direct top-level accessor for the current odd-prime Heisenberg-Weyl
coordinate boundary.

This gives the `ZMod p` phase-space/R-layer equivalence and alternating
symplectic laws.  It is not yet the clock/shift matrix representation or full
finite-dimensional Hilbert semantics. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_coordinate_boundary
    (p n : ℕ) [Fact (Nat.Prime p)] [Fact (p ≠ 2)] :
    Nonempty (PhasePoint.SymplecticBoundary p n) :=
  current_g11_odd_prime_heisenberg_weyl_coordinate_boundary p n

/-- Direct top-level accessor for the odd-prime supplied-character
Heisenberg-Weyl clock/shift matrix boundary.

Given an additive phase character on `ZMod p`, the one-site clock and shift
matrices satisfy the supplied-character commutation law.  This is not yet a
multi-site commutator-phase package, irreducibility/faithfulness theorem, or
full `FdHilb` semantics. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_clock_shift_boundary
    (p : ℕ) [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) :
    Nonempty (PhasePoint.AdditivePhase.ClockShiftBoundary p) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.clock_shift_boundary p χ

/-- Direct top-level accessor for the odd-prime supplied-character multi-site
phase-point matrix boundary.

This supplies a matrix for every phase-space point and proves zero acts as the
identity inside the boundary package; the package also carries projective
multiplication and the symplectic commutator-phase law.  It is not yet the
irreducibility/faithfulness or full `FdHilb` theorem. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_matrix_boundary
    (p n : ℕ) [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) :
    Nonempty (PhasePoint.AdditivePhase.PhasePointMatrixBoundary p n) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_matrix_boundary p n χ

/-- Direct top-level accessor for the odd-prime supplied-character projective
phase-point multiplication law. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_projective_mul
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) (u v : PhasePoint p n) :
    PhasePoint.AdditivePhase.phasePointMatrix χ u *
        PhasePoint.AdditivePhase.phasePointMatrix χ v =
      χ.phase (PhasePoint.AdditivePhase.phaseDot (p := p)
        (PhasePoint.zCoord v) (PhasePoint.xCoord u)) •
        PhasePoint.AdditivePhase.phasePointMatrix χ (u + v) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_projective_mul χ u v

/-- Direct top-level accessor for the odd-prime supplied-character symplectic
commutator-phase law. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_commutator_phase
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) (u v : PhasePoint p n) :
    PhasePoint.AdditivePhase.phasePointMatrix χ u *
        PhasePoint.AdditivePhase.phasePointMatrix χ v =
      χ.phase (PhasePoint.symplectic u v) •
        (PhasePoint.AdditivePhase.phasePointMatrix χ v *
          PhasePoint.AdditivePhase.phasePointMatrix χ u) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_commutator_phase χ u v

/-- Direct top-level accessor for odd-prime supplied-character left unitarity
of phase-point matrices. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_left_unitary
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) (u : PhasePoint p n) :
    Matrix.conjTranspose (PhasePoint.AdditivePhase.phasePointMatrix χ u) *
        PhasePoint.AdditivePhase.phasePointMatrix χ u =
      1 := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_left_unitary χ u

/-- Direct top-level accessor for odd-prime supplied-character right unitarity
of phase-point matrices. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_right_unitary
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p) (u : PhasePoint p n) :
    PhasePoint.AdditivePhase.phasePointMatrix χ u *
        Matrix.conjTranspose (PhasePoint.AdditivePhase.phasePointMatrix χ u) =
      1 := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_right_unitary χ u

/-- Direct top-level accessor for odd-prime supplied-character phase-point
faithfulness when the supplied phase separates `ZMod p`. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_faithful_of_phase_injective
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (hχ : Function.Injective χ.phase) :
    Function.Injective
      (fun u : PhasePoint p n =>
        PhasePoint.AdditivePhase.phasePointMatrix χ u) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_faithful_of_phase_injective χ hχ

/-- Direct top-level accessor for primitive-complex odd-prime phase-point
faithfulness. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_primitive_complex_phase_point_faithful
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)] :
    Function.Injective
      (fun u : PhasePoint p n =>
        PhasePoint.AdditivePhase.phasePointMatrix
          (PhasePoint.AdditivePhase.primitiveComplex p) u) := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.primitive_complex_phase_point_faithful

/-- Direct top-level accessor for the first odd-prime supplied-character
cyclicity boundary: every coordinate matrix entry is hit by a pure shift
phase-point operator. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_coordinate_reachable_by_pure_shift
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (r q : PhasePoint.AdditivePhase.CoordinateBasis p n) :
    ∃ u : PhasePoint p n,
      PhasePoint.AdditivePhase.phasePointMatrix χ u r q = 1 := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_coordinate_reachable_by_pure_shift χ r q

/-- Direct top-level accessor for the odd-prime supplied-character
pure-clock projector orthogonality boundary. The projector is unnormalized:
its selected diagonal entry is the coordinate-basis cardinality. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_coordinate_projector_sum
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (hχ : Function.Injective χ.phase)
    (q r s : PhasePoint.AdditivePhase.CoordinateBasis p n) :
    PhasePoint.AdditivePhase.coordinateProjectorSum χ q r s =
      if s = r then
        if r = q then
          Fintype.card (PhasePoint.AdditivePhase.CoordinateBasis p n)
        else
          0
      else
        0 := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_coordinate_projector_sum χ hχ q r s

/-- Direct top-level accessor for the odd-prime supplied-character
matrix-unit Fourier boundary. The sum is unnormalized: the selected entry is
the coordinate-basis cardinality. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_coordinate_matrix_unit_sum
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (hχ : Function.Injective χ.phase)
    (r q a b : PhasePoint.AdditivePhase.CoordinateBasis p n) :
    PhasePoint.AdditivePhase.coordinateMatrixUnitSum χ r q a b =
      if a = r ∧ b = q then
        Fintype.card (PhasePoint.AdditivePhase.CoordinateBasis p n)
      else
        0 := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_coordinate_matrix_unit_sum χ hχ r q a b

/-- Direct top-level accessor for the odd-prime supplied-character matrix-span
boundary: phase-point matrices span the full coordinate matrix algebra. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_matrix_span_top
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (hχ : Function.Injective χ.phase) :
    Submodule.span ℂ
        (Set.range
          (fun u : PhasePoint p n =>
            PhasePoint.AdditivePhase.phasePointMatrix χ u)) =
      ⊤ := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_matrix_span_top χ hχ

/-- Direct top-level accessor for the odd-prime supplied-character
irreducibility boundary: every nonzero coordinate subspace stable under all
phase-point matrices is the whole coordinate Hilbert space. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_phase_point_invariant_subspace_eq_top
    {p n : ℕ} [Fact (Nat.Prime p)] [Fact (p ≠ 2)]
    (χ : PhasePoint.AdditivePhase p)
    (hχ : Function.Injective χ.phase)
    (W : Submodule ℂ (PhasePoint.AdditivePhase.CoordinateBasis p n → ℂ))
    (hW : ∀ u : PhasePoint p n,
      ∀ v : PhasePoint.AdditivePhase.CoordinateBasis p n → ℂ,
        v ∈ W →
          Matrix.mulVec
            (PhasePoint.AdditivePhase.phasePointMatrix χ u) v ∈ W)
    (hne : W ≠ ⊥) :
    W = ⊤ := by
  rcases current_g11_odd_prime_heisenberg_weyl_supplied_character_operator_boundary with ⟨h⟩
  exact h.phase_point_invariant_subspace_eq_top χ hχ W hW hne

/-- Direct top-level accessor for the scoped odd-prime Heisenberg-Weyl
finite-Hilbert operator semantic boundary.

This bundles the supplied-character operator package with phase-point
matrices, unitarity, full coordinate matrix-algebra span, and
invariant-subspace irreducibility. It is not the full `FdHilb`
dagger-SMCC theorem. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_finite_hilbert_operator_boundary :
    Nonempty CurrentG11OddPrimeHeisenbergWeylFiniteHilbertOperatorBoundary :=
  current_g11_odd_prime_heisenberg_weyl_finite_hilbert_operator_boundary

/-- Direct top-level accessor for the scoped odd-prime Heisenberg-Weyl
finite-Hilbert object action boundary.

This says phase-space points act as projective unitary linear endomorphisms
of the concrete coordinate finite-Hilbert object via the existing
supplied-character phase-point matrices. It is not full `FdHilb`
categorical semantics. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_finite_hilbert_object_action_boundary :
    Nonempty CurrentG11OddPrimeHeisenbergWeylFiniteHilbertObjectActionBoundary :=
  current_g11_odd_prime_heisenberg_weyl_finite_hilbert_object_action_boundary

/-- Direct top-level accessor for the scoped odd-prime Heisenberg-Weyl
finite-Hilbert dagger boundary.

This combines the concrete phase-point object action with the finite-Hilbert
adjoint laws for the ambient linear-map category. It is not full `FdHilb`
categorical semantics or a dagger-SMCC theorem. -/
theorem current_full_gut_g11_odd_prime_heisenberg_weyl_finite_hilbert_dagger_boundary :
    Nonempty CurrentG11OddPrimeHeisenbergWeylFiniteHilbertDaggerBoundary :=
  current_g11_odd_prime_heisenberg_weyl_finite_hilbert_dagger_boundary

/-- Direct top-level accessor for the current R-substrate-to-Hilbert action
boundary exposed by the native semantic frontier.

This is scoped to the coordinate stabilizer branch; it is not full `FdHilb`
functoriality. -/
theorem current_full_gut_native_r_to_hilbert_substrate_action_boundary :
    Nonempty RToHilbertSubstrateActionBoundary :=
  current_native_semantic_r_to_hilbert_substrate_action_boundary

/-- Direct top-level accessor for the scoped finite-Hilbert dagger boundary.

This records Hilbert adjoint on finite-dimensional complex Hilbert objects as
an involutive, composition-reversing operation on linear morphisms. It is not
a bundled `FdHilb` dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_hilbert_dagger_boundary :
    Nonempty FinHilbDaggerBoundary :=
  current_native_semantic_finite_hilbert_dagger_boundary

/-- Direct top-level accessor for the scoped finite-coordinate Hilbert
tensor/unit object boundary.

This is the coordinate object-level tensor/unit package: product-indexed
coordinate objects with unit, associativity, and braiding reindexing
equivalences. It is not a full `FdHilb` monoidal-category theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_tensor_boundary :
    Nonempty FinHilbCoordinateTensorBoundary :=
  current_native_semantic_finite_coordinate_hilbert_tensor_boundary

/-- Direct top-level accessor for the scoped finite-coordinate Hilbert
tensor/unit isometry boundary.

This upgrades the coordinate unit, associativity, and braiding reindexing
maps to norm-preserving linear isometry equivalences. It is still below a
bundled `FdHilb` monoidal-category theorem or Hilbert tensor-product functor. -/
theorem current_full_gut_native_finite_coordinate_hilbert_tensor_isometry_boundary :
    Nonempty FinHilbCoordinateTensorIsometryBoundary :=
  current_native_semantic_finite_coordinate_hilbert_tensor_isometry_boundary

/-- Direct top-level accessor for the scoped finite-coordinate Hilbert tensor
coherence boundary.

This forwards triangle, pentagon, braiding involution, and braided hexagon
laws for product-coordinate isometric reindexing maps. It is not a bundled
`FdHilb` monoidal category, naturality theorem, or dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_tensor_coherence_boundary :
    Nonempty FinHilbCoordinateTensorCoherenceBoundary :=
  current_native_semantic_finite_coordinate_hilbert_tensor_coherence_boundary

/-- Direct top-level accessor for the scoped finite-coordinate Hilbert
dagger/tensor boundary.

This forwards Hilbert-adjoint compatibility for structural coordinate
isometries, Kronecker tensor maps, and the tensor-product comparison
isometry. It is not a bundled `FdHilb` dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_dagger_tensor_boundary :
    Nonempty FinHilbCoordinateDaggerTensorBoundary :=
  current_native_semantic_finite_coordinate_hilbert_dagger_tensor_boundary

/-- Direct top-level accessor for the scoped finite-coordinate Hilbert
Kronecker morphism boundary.

This extends the coordinate tensor/unit object package to matrix-presented
coordinate morphisms via Kronecker product, with identity, composition, and
adjoint laws. It is not a bundled `FdHilb` monoidal or dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_kronecker_morphism_boundary :
    Nonempty FinHilbCoordinateKroneckerMorphismBoundary :=
  current_native_semantic_finite_coordinate_hilbert_kronecker_morphism_boundary

/-- Direct top-level accessor for the finite-coordinate comparison between
product-indexed Hilbert objects and Mathlib algebraic tensor products.

The comparison is natural for matrix-presented coordinate morphisms through
the Kronecker map. It remains a finite-coordinate algebraic tensor comparison
boundary, not a bundled `FdHilb` monoidal or dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_tensor_product_comparison_boundary :
    Nonempty FinHilbCoordinateTensorProductComparisonBoundary :=
  current_native_semantic_finite_coordinate_hilbert_tensor_product_comparison_boundary

/-- Direct top-level accessor for the finite-coordinate isometric comparison
between product-indexed Hilbert objects and Mathlib algebraic tensor products.

This upgrades the coordinate algebraic tensor comparison to a norm-preserving
linear isometry equivalence. It remains finite-coordinate and matrix-presented,
not a bundled `FdHilb` monoidal or dagger-SMCC theorem. -/
theorem current_full_gut_native_finite_coordinate_hilbert_tensor_product_isometry_boundary :
    Nonempty FinHilbCoordinateTensorProductIsometryBoundary :=
  current_native_semantic_finite_coordinate_hilbert_tensor_product_isometry_boundary

/-- Direct top-level accessor for the strongest current finite-Hilbert
stabilizer coherence boundary.

This forwards the coordinate matrix identity/composition/adjoint, Pauli/R
Hilbert action, and tensor-coherence package without claiming a bundled
dagger-SMCC for all finite-dimensional Hilbert spaces. -/
theorem current_full_gut_native_stabilizer_hilbert_coherence_boundary :
    Nonempty StabilizerHilbertCoherenceBoundary :=
  current_native_semantic_stabilizer_hilbert_coherence_boundary

/-- Direct top-level accessor for the concrete stabilizer matrix tensor-unit
boundary exposed by the native semantic frontier.

This is scoped to the concrete 0-qubit unit against nonempty `n`-qubit
Pauli-coordinate blocks; it is not a 0-qubit D1/FullGUT theorem. -/
theorem current_full_gut_native_concrete_n_qubit_matrix_tensor_unit_boundary
    (n : ℕ) (hn : 1 ≤ n) :
    Nonempty
      (NativeStabilizerQuantum.ConcreteNQubitMatrixTensorUnitBoundary n hn) :=
  current_native_semantic_concrete_n_qubit_matrix_tensor_unit_boundary n hn

/-- Direct top-level accessor for the concrete phased stabilizer matrix
operator boundary with tensor splits, associativity, and 0-qubit unit
coherence.

This remains a scoped stabilizer matrix theorem, not a full `FdHilb`
dagger-SMCC or all-quantum-semantics theorem. -/
theorem current_full_gut_native_concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary
    (n m k : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m) (hk : 1 ≤ k) :
    Nonempty
      (NativeStabilizerQuantum.ConcreteNQubitPhasedUnitalMonoidalMatrixOperatorBoundary
        n m k hn hm hk) :=
  current_native_semantic_concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary
    n m k hn hm hk

/-- Direct top-level accessor for the finite `Type` ordinary/enriched model
category equivalence.

This is scoped to ordinary Lawvere models and finite `Type`-enriched models;
it is not the Power 1999 theorem for arbitrary enriched semantics. -/
theorem current_full_gut_enriched_lawvere_type_model_bridge_equivalence
    (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
    [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C] :
    Nonempty
      (letI :
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
          (Type u) T :=
        CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
      CategoryTheory.Model T C ≌
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteModel (Type u) T C) :=
  ⟨CategoryTheory.EnrichedDoctrine.finiteTypeModelBridgeEquivalence T C⟩

/-- Direct top-level accessor for full faithfulness of the ordinary-to-finite
`Type` model bridge functor. -/
theorem current_full_gut_enriched_lawvere_ordinary_to_finite_type_model_bridge_fully_faithful
    (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
    [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C] :
    Nonempty
      (letI :
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
          (Type u) T :=
        CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
      (CategoryTheory.EnrichedDoctrine.finiteEnrichedModelOfModelFunctor T C).FullyFaithful) :=
  ⟨CategoryTheory.EnrichedDoctrine.finiteEnrichedModelOfModelFunctorFullyFaithful T C⟩

/-- Direct top-level accessor for full faithfulness of the finite-`Type` to
ordinary model bridge functor. -/
theorem current_full_gut_enriched_lawvere_finite_type_to_ordinary_model_bridge_fully_faithful
    (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
    [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C] :
    Nonempty
      (letI :
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
          (Type u) T :=
        CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
      (CategoryTheory.EnrichedDoctrine.modelOfFiniteEnrichedModelFunctor T C).FullyFaithful) :=
  ⟨CategoryTheory.EnrichedDoctrine.modelOfFiniteEnrichedModelFunctorFullyFaithful T C⟩

/-- Direct top-level accessor for categorical equivalence of the
ordinary-to-finite `Type` model bridge functor. -/
theorem current_full_gut_enriched_lawvere_ordinary_to_finite_type_model_bridge_is_equivalence
    (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
    [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C] :
    Nonempty
      (letI :
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
          (Type u) T :=
        CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
      (CategoryTheory.EnrichedDoctrine.finiteEnrichedModelOfModelFunctor T C).IsEquivalence) :=
  ⟨CategoryTheory.EnrichedDoctrine.finiteEnrichedModelOfModelFunctorIsEquivalence T C⟩

/-- Direct top-level accessor for categorical equivalence of the
finite-`Type` to ordinary model bridge functor. -/
theorem current_full_gut_enriched_lawvere_finite_type_to_ordinary_model_bridge_is_equivalence
    (T C : Type u) [CategoryTheory.SmallCategory T] [CategoryTheory.LawvereTheory T]
    [CategoryTheory.Category.{u} C] [CategoryTheory.Limits.HasFiniteProducts C] :
    Nonempty
      (letI :
        CategoryTheory.EnrichedDoctrine.EnrichedFiniteLawvereTheory
          (Type u) T :=
        CategoryTheory.EnrichedDoctrine.finiteEnrichedLawvereTheoryOfLawvereTheory T
      (CategoryTheory.EnrichedDoctrine.modelOfFiniteEnrichedModelFunctor T C).IsEquivalence) :=
  ⟨CategoryTheory.EnrichedDoctrine.modelOfFiniteEnrichedModelFunctorIsEquivalence T C⟩

/-- Direct top-level accessor for the algebraic coherent all-split bridge.

This is still structure-gated by the supplied direct-sum structural witness;
it only avoids forcing downstream files to unpack `CurrentFullGUTFrontier`. -/
theorem current_full_gut_R_T5_algebraic_coherent_from_direct_sum
    (k : Type) [Field k] [Fintype k] [DecidableEq k]
    (S : P1P7_Satisfier_Algebraic k)
    (hDirect : P1P7_Core.DirectSumStructuralIso S.toP1P7_Core) :
    T5AlgebraicCoherentDirectSumGUTBPackage S hDirect :=
  T5_algebraic_coherent_GUT_B_package_of_direct_sum S hDirect

/-- Direct top-level accessor for the canonical finite-field all-split branch. -/
theorem current_full_gut_R_T5_canonical_field_all_split
    (k : Type) [Field k] [Fintype k] [DecidableEq k] :
    T5FieldDirectSumGUTBPackage (T5_field_canonical_auto k) :=
  T5_field_direct_sum_GUT_B_package_canonical_auto k

/-- Direct top-level accessor for the canonical finite-field coherent
all-split branch. -/
theorem current_full_gut_R_T5_canonical_field_coherent_all_split
    (k : Type) [Field k] [Fintype k] [DecidableEq k] :
    ∃ hDirect :
      P1P7_Core.DirectSumStructuralIso
        (T5_field_canonical_auto k).toP1P7_Satisfier_Algebraic.toP1P7_Core,
      T5FieldCoherentDirectSumGUTBPackage
        (T5_field_canonical_auto k) hDirect :=
  T5_field_coherent_GUT_B_package_canonical_auto k

/-- Direct top-level accessor for the canonical/gated finite-field T5
boundary.

This is the compact theorem form: canonical finite-field R-families are
all-split/coherent all-split automatically, while arbitrary non-canonical
field satisfiers still require an explicit direct-sum structural witness. -/
theorem current_full_gut_R_T5_field_canonical_and_gated_noncanonical_boundary
    (k : Type) [Field k] [Fintype k] [DecidableEq k] :
    T5FieldDirectSumGUTBPackage (T5_field_canonical_auto k)
      ∧ (∃ hDirect :
          P1P7_Core.DirectSumStructuralIso
            (T5_field_canonical_auto k).toP1P7_Satisfier_Algebraic.toP1P7_Core,
          T5FieldCoherentDirectSumGUTBPackage
            (T5_field_canonical_auto k) hDirect)
      ∧ (∀ (S : P1P7_Satisfier_Field k)
          (hDirect :
            P1P7_Core.DirectSumStructuralIso
              S.toP1P7_Satisfier_Algebraic.toP1P7_Core),
          T5FieldCoherentDirectSumGUTBPackage S hDirect) :=
  T5_field_canonical_and_gated_noncanonical_boundary k

/-- Direct top-level accessor for the raw-core T5 boundary.

Raw `P1P7_Core` data proves successor coherence on its own; arbitrary
all-split coherent T5 remains explicitly gated by a supplied direct-sum
structural witness. -/
theorem current_full_gut_R_T5_raw_core_successor_and_gated_direct_sum
    {δ : Type} [Fintype δ] [DecidableEq δ] [Inhabited δ]
    (S : P1P7_Core δ) :
    T5SuccessorGUTBPackage S
      ∧ (∀ hDirect : P1P7_Core.DirectSumStructuralIso S,
          T5CoherentDirectSumGUTBPackage S hDirect) :=
  T5_raw_core_successor_and_gated_direct_sum S

/-- Direct top-level accessor for the split-coherent all-split T5 package. -/
theorem current_full_gut_R_T5_generic_split_coherent_GUT_B_package
    {δ : Type} [Fintype δ] [DecidableEq δ]
    (S : P1P7_SplitCoherentCore δ) :
    T5SplitCoherentGUTBPackage S :=
  T5_split_coherent_GUT_B_package S

/-- Direct top-level accessor for the generic coherent all-split bridge under
a supplied direct-sum structural witness. -/
theorem current_full_gut_R_T5_generic_coherent_from_direct_sum
    {δ : Type} [Fintype δ] [DecidableEq δ]
    (S : P1P7_Core δ)
    (hDirect : P1P7_Core.DirectSumStructuralIso S) :
    T5CoherentDirectSumGUTBPackage S hDirect :=
  T5_coherent_GUT_B_package_of_direct_sum S hDirect

/-- Direct top-level accessor for the char-class field ring-equivalence
dispatcher.  Arbitrary satisfiers still supply their field-satisfier data;
the dispatcher only removes downstream frontier unpacking. -/
theorem current_full_gut_R_T5_field_ringEquiv_by_charClass
    (k : Type) [Field k] [Fintype k] [DecidableEq k]
    (S : P1P7_Satisfier_Field k) :
    @Nonempty
      (@RingEquiv
        (S.toP1P7_Satisfier_Algebraic.toP1P7_Core.carrier 4)
        (Matrix (Fin 2) (Fin 2) k)
        S.toP1P7_Satisfier_Algebraic.p7b_mul_instance (matMulInstance k)
        S.toP1P7_Satisfier_Algebraic.p7b_add_instance (matAddInstance k)) :=
  T5_field_ringEquiv_by_charClass S

/-- Direct top-level accessor for the field coherent all-split bridge under a
supplied direct-sum structural witness. -/
theorem current_full_gut_R_T5_field_coherent_from_direct_sum
    (k : Type) [Field k] [Fintype k] [DecidableEq k]
    (S : P1P7_Satisfier_Field k)
    (hDirect :
      P1P7_Core.DirectSumStructuralIso
        S.toP1P7_Satisfier_Algebraic.toP1P7_Core) :
    T5FieldCoherentDirectSumGUTBPackage S hDirect :=
  T5_field_coherent_GUT_B_package_of_direct_sum S hDirect

/-- Direct top-level accessor for split-coherent field synthesis.

The split-coordinate laws synthesize both the carrier-4 matrix-ring field
satisfier data and the all-split direct-sum witness. This is stronger than
the supplied-direct-sum bridge, but it still does not apply to raw field
cores without split-coordinate laws. -/
theorem current_full_gut_R_T5_field_split_coherent_direct_sum
    (k : Type) [Field k] [Fintype k] [DecidableEq k]
    (S : P1P7_SplitCoherentCore k) :
    T5FieldDirectSumGUTBPackage (splitCoherentFieldSatisfier k S) :=
  T5_field_split_coherent_direct_sum_GUT_B_package k S

/-- Direct top-level accessor for the coherent-core package induced by a
split-coherent field core. -/
theorem current_full_gut_R_T5_field_split_coherent_coherent
    (k : Type) [Field k] [Fintype k] [DecidableEq k]
    (S : P1P7_SplitCoherentCore k) :
    ∃ hDirect :
      P1P7_Core.DirectSumStructuralIso
        (splitCoherentFieldSatisfier k S).toP1P7_Satisfier_Algebraic.toP1P7_Core,
      T5FieldCoherentDirectSumGUTBPackage
        (splitCoherentFieldSatisfier k S) hDirect :=
  T5_field_split_coherent_coherent_GUT_B_package k S

/-- Direct top-level accessor for the scoped F₂ side obligations package. -/
theorem current_full_gut_R_T5_f2_side_obligations
    (S : P1P7_Satisfier_F2) :
    T5AItem8RInfty
      ∧ T5AItem9CoreModality
      ∧ T5AItem11AtomicRing S
      ∧ T5AItem11AtomicActionR
      ∧ Nonempty (T5AAtomicActionTransport S) :=
  T5_A_full_side_obligations S

/-- Direct top-level accessor for route refutation from exact D6 evidence and
a held D5 claim. -/
theorem current_full_gut_D6_exact_routes_refuted_of_D5
    {claim : D5_UniversalClaim} {falsif : D6_ClaimZFalsified}
    (hExact : D6ExactForD5 claim falsif)
    (hD5 : D5_holds claim) :
    ¬ falsif.not_analytic ∧
      ¬ falsif.not_synthetic ∧
      ¬ falsif.not_D2_consistent :=
  hExact.all_routes_refuted_of_D5 hD5

end SSBX.Foundation.Doctrine.FullGUTFrontier
