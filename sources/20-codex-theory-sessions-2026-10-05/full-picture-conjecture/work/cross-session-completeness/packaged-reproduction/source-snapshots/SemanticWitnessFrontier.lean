/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / Full GUT native-semantics pass
-/
import SSBX.Foundation.Doctrine.Instance.HeytingCategoryNative
import SSBX.Foundation.Doctrine.Instance.HilbertEnriched
import SSBX.Foundation.Doctrine.Instance.TopologicalNativeLocale
import SSBX.Foundation.Order.HeytingBimorphism

/-!
# Foundation.Doctrine.Instance.SemanticWitnessFrontier

This file bundles the currently closed native semantic witness fronts.

It is intentionally an aggregator, not a claim upgrade: the fields below
point to theorem-grade packages that already exist for Heyting, stabilizer
quantum/Hilbert, and locale/frame semantics.  It also records negative
boundaries when a tempting categorical target is ruled out.  The still-open
positive categorical targets remain open: full `FdHilb` dagger-SMCC,
exponential-frame / `MonoidalClosed Frm`, and Power/enriched all-semantics.
-/

namespace SSBX.Foundation.Doctrine.Instance

open CategoryTheory
open SSBX.Foundation.Order
open SSBX.Foundation.Wen.Embeddings
open SSBX.Foundation.Modern.Quantum
open StabilizerQM (PauliBase)

universe u

/-- The scoped Heyting anchor frontier around `DiamondH4`.

This records the existing theorem-grade classification and P3 refinement for
the minimum non-Boolean four-element Heyting anchor.  It is deliberately not a
cartesian-closed-category claim about bundled `HeytAlg`. -/
structure HeytingDiamondH4Frontier : Type 1 where
  anchor_existence_and_uniqueness :
    (Fintype.card DiamondH4 = 4 ∧
      (DiamondH4.himp
          (DiamondH4.himp DiamondH4.mid1 DiamondH4.bot)
          DiamondH4.bot ≠
        DiamondH4.mid1)) ∧
    (∀ (H : Type) [HeytingAlgebra H] [Fintype H] [DecidableEq H],
      Fintype.card H = 4 →
      (⊥ : H) ≠ ⊤ →
      ¬ (∀ x : H, ∃ y : H, x ⊓ y = ⊥ ∧ x ⊔ y = ⊤) →
      Nonempty (H ≃o DiamondH4))
  linear_order_iso :
    Nonempty (DiamondH4 ≃o SSBX.Foundation.Order.Chain4)
  himp_agrees_with_transferred_himp :
    ∀ a b : DiamondH4, DiamondH4.himp a b = (a ⇨ b)
  refined_p3 :
    (¬ ∃ φ : DiamondH4 → DiamondH4 → DiamondH4,
      SSBX.Foundation.Order.IsHeytingBilinear φ) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.inf2 DiamondH4) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.sup2 DiamondH4) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.proj1 DiamondH4) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.proj2 DiamondH4) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.constBot DiamondH4) ∧
    SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.constTop DiamondH4)
  p3_framework :
    (∀ (H : Type) [HeytingAlgebra H] (_ : (⊥ : H) ≠ ⊤),
      ¬ ∃ φ : H → H → H, SSBX.Foundation.Order.IsHeytingBilinear φ) ∧
    (∀ (H : Type) [DistribLattice H] [BoundedOrder H],
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.inf2 H) ∧
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.sup2 H) ∧
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.proj1 H) ∧
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.proj2 H) ∧
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.constBot H) ∧
      SSBX.Foundation.Order.IsSubBimorphism
        (SSBX.Foundation.Order.constTop H))
  strong_eval_codomain_trivial :
    ∀ {A B C : Type} [HeytingAlgebra A] [HeytingAlgebra B]
      [HeytingAlgebra C] {φ : A → B → C},
      SSBX.Foundation.Order.IsHeytingBilinear₂ φ → (⊥ : C) = ⊤

/-- The current native semantic witness frontier.

Each field is either a closed nonempty package or a family of closed packages
over the explicit parameters where the current theorem is scoped. -/
structure SemanticWitnessFrontier : Type (u + 2) where
  finite_heytalg_closed :
    ∀ (P : NativeHeytAlg.Presentation),
      [Fintype P.system.toFormalPresentation.Obj] →
      [Fintype P.system.toFormalPresentation.Mor] →
      [Fintype P.system.toFormalPresentation.Rel] →
      [Fintype P.system.toFormalPresentation.Op] →
      [Fintype P.system.toFormalPresentation.Rule] →
      [Fintype P.system.toFormalPresentation.Proof] →
      P.system.SatisfiesD1 →
        Nonempty (NativeHeytAlg.FiniteClosedFullGUT P)
  encodable_heytalg_closed :
    ∀ (P : NativeHeytAlg.Presentation),
      [Encodable P.system.toFormalPresentation.Obj] →
      [Encodable P.system.toFormalPresentation.Mor] →
      [Encodable P.system.toFormalPresentation.Rel] →
      [Encodable P.system.toFormalPresentation.Op] →
      [Encodable P.system.toFormalPresentation.Rule] →
      [Encodable P.system.toFormalPresentation.Proof] →
      P.system.SatisfiesD1 →
        Nonempty (NativeHeytAlg.EncodableClosedStreamFullGUT P)
  finite_heytalg_hom_closed :
    ∀ (P : NativeHeytAlg.HomPresentation),
      [Fintype P.system.toFormalPresentation.Obj] →
      [Fintype P.system.toFormalPresentation.Mor] →
      [Fintype P.system.toFormalPresentation.Rel] →
      [Fintype P.system.toFormalPresentation.Op] →
      [Fintype P.system.toFormalPresentation.Rule] →
      [Fintype P.system.toFormalPresentation.Proof] →
      P.system.SatisfiesD1 →
        Nonempty P.FiniteHomClosedFullGUT
  encodable_heytalg_hom_closed :
    ∀ (P : NativeHeytAlg.HomPresentation),
      [Encodable P.system.toFormalPresentation.Obj] →
      [Encodable P.system.toFormalPresentation.Mor] →
      [Encodable P.system.toFormalPresentation.Rel] →
      [Encodable P.system.toFormalPresentation.Op] →
      [Encodable P.system.toFormalPresentation.Rule] →
      [Encodable P.system.toFormalPresentation.Proof] →
      P.system.SatisfiesD1 →
        Nonempty P.EncodableHomClosedStreamFullGUT
  heytalg_posetal_closed_end_action :
    ∀ (P : NativeHeytAlg.HomPresentation),
      Nonempty (NativeHeytAlg.HomPresentation.HeytAlgPosetalClosedEndAction P)
  heytalg_hom_eval_transport :
    ∀ (P : NativeHeytAlg.HomPresentation)
      (f : P.system.toFormalPresentation.Mor)
      (a b : P.system.toFormalPresentation.Obj),
      P.morHom f (a ⊓ (a ⇨ b)) ≤ P.morHom f b
  heytalg_hom_curry_transport :
    ∀ (P : NativeHeytAlg.HomPresentation)
      (f : P.system.toFormalPresentation.Mor)
      (a b c : P.system.toFormalPresentation.Obj),
      P.morHom f (a ⊓ b) ≤ P.morHom f c ↔
        P.morHom f b ≤ P.morHom f a ⇨ P.morHom f c
  indexed_heytalg_posetal_closed :
    ∀ {ι : Type} (C : ι → HeytAlg),
      Nonempty (NativeHeytAlg.IndexedPosetalClosedSemantics.{0} C)
  finite_indexed_heytalg :
    ∀ {ι : Type} (C : ι → HeytAlg), [DecidableEq ι] → (base : ι) →
      [Fintype ι] → [∀ i j, Fintype (C i ⟶ C j)] →
        Nonempty (NativeHeytAlg.FiniteIndexedCategoryFullGUT C base)
  encodable_indexed_heytalg :
    ∀ {ι : Type} (C : ι → HeytAlg), [DecidableEq ι] → (base : ι) →
      [Encodable ι] → [∀ i j, Encodable (C i ⟶ C j)] →
        Nonempty (NativeHeytAlg.EncodableIndexedCategoryStreamFullGUT C base)
  heytalg_bool_cartesian_exponent_obstruction :
    ¬ ∃ E : HeytAlg, NativeHeytAlg.BoolCartesianExponentRepresentation E
  heytalg_no_unit_to_nontrivial :
    ∀ {E : HeytAlg.{0}}, (⊥ : E) ≠ ⊤ →
      IsEmpty (HeytAlg.of PUnit.{1} ⟶ E)
  bool_himp_not_sub_bimorphism :
    ¬ SSBX.Foundation.Order.IsSubBimorphism
      (SSBX.Foundation.Order.himp2 Bool)
  heytalg_categorical_boundary :
    Nonempty NativeHeytAlg.HeytAlgCategoricalBoundary
  diamondH4_anchor :
    HeytingDiamondH4Frontier
  single_qubit_hilbert_dagger :
    Nonempty ConcreteSingleQubitHilbertDaggerBridge
  single_qubit_matrix_dagger_full_gut :
    Nonempty NativeStabilizerQuantum.ConcreteSingleQubitMatrixDaggerFullGUT
  n_qubit_hilbert_bridge :
    ∀ n : ℕ, Nonempty (NQubitQuantumToHilbertBridge n)
  n_qubit_hilbert_dagger_operator :
    ∀ (n : ℕ) (hn : 1 ≤ n),
      Nonempty (ConcreteNQubitHilbertDaggerOperatorBridge n hn)
  r_to_hilbert_quantum :
    ∀ n : ℕ, RToHilbertQuantumWitness n
  r_to_hilbert_end_action :
    ∀ n : ℕ, Nonempty (RToHilbertEndAction n)
  r_to_hilbert_tensor_boundary :
    RToHilbertTensorBoundary
  r_to_hilbert_substrate_action_boundary :
    Nonempty RToHilbertSubstrateActionBoundary
  finite_hilbert_dagger_boundary :
    Nonempty FinHilbDaggerBoundary
  finite_coordinate_hilbert_tensor_boundary :
    Nonempty FinHilbCoordinateTensorBoundary
  finite_coordinate_hilbert_tensor_isometry_boundary :
    Nonempty FinHilbCoordinateTensorIsometryBoundary
  finite_coordinate_hilbert_tensor_coherence_boundary :
    Nonempty FinHilbCoordinateTensorCoherenceBoundary
  finite_coordinate_hilbert_dagger_tensor_boundary :
    Nonempty FinHilbCoordinateDaggerTensorBoundary
  finite_coordinate_hilbert_kronecker_morphism_boundary :
    Nonempty FinHilbCoordinateKroneckerMorphismBoundary
  finite_coordinate_hilbert_tensor_product_comparison_boundary :
    Nonempty FinHilbCoordinateTensorProductComparisonBoundary
  finite_coordinate_hilbert_tensor_product_isometry_boundary :
    Nonempty FinHilbCoordinateTensorProductIsometryBoundary
  stabilizer_hilbert_boundary :
    Nonempty StabilizerHilbertCoherenceBoundary
  matrix_hilbert_scalar :
    ∀ {m n : ℕ} (a : ℂ) (A : Matrix (Fin m) (Fin n) ℂ),
      matrixHilbLinearMap (a • A) = a • matrixHilbLinearMap A
  matrix_hilbert_adjoint :
    ∀ {m n : ℕ} (A : Matrix (Fin m) (Fin n) ℂ),
      LinearMap.adjoint (matrixHilbLinearMap A) =
        matrixHilbLinearMap (Matrix.conjTranspose A)
  pauli_base_hilbert_adjoint :
    ∀ p : PauliBase,
      LinearMap.adjoint (pauliBaseHilbEnd p) = pauliBaseHilbEnd p
  pauli_n_hilbert_adjoint :
    ∀ {n : ℕ} (p : StabilizerQM.PauliN n),
      LinearMap.adjoint (pauliNHilbEnd p) = pauliNHilbEnd p
  r_to_hilbert_end_adjoint :
    ∀ {n : ℕ} (v : SSBX.Foundation.R.R (2 * n)),
      LinearMap.adjoint (rToHilbEnd v) = rToHilbEnd v
  r_to_hilbert_end_projective_add_scalar :
    ∀ {n : ℕ} (u v : SSBX.Foundation.R.R (2 * n)),
      rToHilbEnd v ≫ rToHilbEnd u =
        (PhasedPauli.PauliPhase.toComplex
            (PhasedPauli.pauliNPhase
              (HilbertPauliFunctor.rToPauli u)
              (HilbertPauliFunctor.rToPauli v)) •
          matrixHilbLinearMap
            (HilbertPauliFunctor.rToHilbert (n := n) (u + v)) :
          (nQubitHilb n) →ₗ[ℂ] (nQubitHilb n))
  phased_pauli_hilbert_adjoint :
    ∀ {n : ℕ} (P : PhasedPauli.PhasedPauliN n),
      LinearMap.adjoint (phasedPauliNHilbEnd P) =
        phasedPauliNHilbEnd (PhasedPauli.PhasedPauliN.dagger P)
  pauli_hilbert_tensor_coherence :
    SSBX.Foundation.Wen.Embeddings.HilbertPauliFunctor.PauliHilbertTensorCoherence
  phased_pauli_hilbert_action :
    ∀ n : ℕ, Nonempty (PhasedPauliNHilbertAction n)
  phased_pauli_hilbert_tensor_action :
    Nonempty PhasedPauliNHilbertTensorAction
  generic_n_qubit_hilbert_operator :
    ∀ {n : ℕ} (P : NativeStabilizerQuantum.NQubitPresentation n),
      [Fintype P.system.toFormalPresentation.Mor] →
      [Fintype P.system.toFormalPresentation.Rel] →
      [Fintype P.system.toFormalPresentation.Op] →
      [Fintype P.system.toFormalPresentation.Rule] →
      [Fintype P.system.toFormalPresentation.Proof] →
      P.system.SatisfiesD1 →
        Nonempty (NQubitPresentationHilbertDaggerOperatorBridge P)
  n_qubit_matrix_tensor_unit :
    ∀ {n : ℕ} (U : NativeStabilizerQuantum.NQubitPresentation 0)
      (P : NativeStabilizerQuantum.NQubitPresentation n),
        Nonempty (NativeStabilizerQuantum.NQubitMatrixTensorUnitWitness U P)
  concrete_n_qubit_matrix_tensor_unit_boundary :
    ∀ (n : ℕ) (hn : 1 ≤ n),
      Nonempty
        (NativeStabilizerQuantum.ConcreteNQubitMatrixTensorUnitBoundary n hn)
  n_qubit_matrix_tensor :
    ∀ (n m : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m),
      Nonempty
        (NativeStabilizerQuantum.ConcreteNQubitMatrixTensorFullGUT
          n m hn hm)
  n_qubit_matrix_tensor_assoc :
    ∀ (n m k : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m) (hk : 1 ≤ k),
      Nonempty
        (NativeStabilizerQuantum.ConcreteNQubitMatrixTensorAssocFullGUT
          n m k hn hm hk)
  n_qubit_matrix_tensor_coherence_boundary :
    ∀ (U : NativeStabilizerQuantum.NQubitPresentation 0)
      {n m k : ℕ}
      (P : NativeStabilizerQuantum.NQubitPresentation n)
      (Q : NativeStabilizerQuantum.NQubitPresentation m)
      (R : NativeStabilizerQuantum.NQubitPresentation k),
        Nonempty
          (NativeStabilizerQuantum.NQubitMatrixTensorCoherenceBoundary
            U P Q R)
  phased_monoidal_stabilizer :
    ∀ (n m k : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m) (hk : 1 ≤ k),
      Nonempty
        (NativeStabilizerQuantum.ConcreteNQubitPhasedMonoidalMatrixOperatorFullGUT
          n m k hn hm hk)
  phased_unital_monoidal_stabilizer :
    ∀ (n m k : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m) (hk : 1 ≤ k),
      Nonempty
        (NativeStabilizerQuantum.ConcreteNQubitPhasedUnitalMonoidalMatrixOperatorBoundary
          n m k hn hm hk)
  topological_native_frame :
    Nonempty TopologicalNativeFrameWitness
  topological_locale :
    Nonempty (TopologicalNativeLocaleWitness.{u})
  topological_locale_represented_closed :
    Nonempty (TopologicalNativeLocaleRepresentedClosedWitness.{u})
  topological_locale_unit_closed :
    Nonempty (TopologicalNativeLocaleUnitClosedWitness.{u})
  topological_locale_represented_right_uncurry_eval :
    ∀ {X Z Y : Frm.{u}} (E : FrmExponentialData X Z)
      (k : Y ⟶ E.exp),
      (frmTensorClosedHomEquiv_of_exponentialData E Y).symm k =
        frmTensorHom k (𝟙 X) ≫ E.eval
  topological_locale_represented_left_uncurry_eval :
    ∀ {X Z Y : Frm.{u}} (E : FrmExponentialData X Z)
      (k : Y ⟶ E.exp),
      (frmTensorClosedHomEquiv_of_exponentialData_braiding E Y).symm k =
        (frmBraiding X Y).hom ≫ frmTensorHom k (𝟙 X) ≫ E.eval
  topological_locale_unit_right_curry :
    ∀ Y Z : Frm.{u},
      Nonempty ((frmTensorObj Y frmTensorUnit ⟶ Z) ≃ (Y ⟶ Z))
  topological_locale_unit_right_naturality :
    ∀ {Z Y Y' : Frm.{u}} (f : Y' ⟶ Y)
      (h : frmTensorObj Y frmTensorUnit ⟶ Z),
      frmTensorClosedHomEquiv_of_exponentialData
          (frmTensorUnitExponentialData Z) Y'
          (frmTensorHom f (𝟙 frmTensorUnit) ≫ h) =
        f ≫ frmTensorClosedHomEquiv_of_exponentialData
          (frmTensorUnitExponentialData Z) Y h
  topological_locale_unit_left_curry :
    ∀ Y Z : Frm.{u},
      Nonempty ((frmTensorObj frmTensorUnit Y ⟶ Z) ≃ (Y ⟶ Z))
  topological_locale_unit_left_naturality :
    ∀ {Z Y Y' : Frm.{u}} (f : Y' ⟶ Y)
      (h : frmTensorObj frmTensorUnit Y ⟶ Z),
      frmTensorClosedHomEquiv_of_exponentialData_braiding
          (frmTensorUnitExponentialData Z) Y'
          (frmTensorHom (𝟙 frmTensorUnit) f ≫ h) =
        f ≫ frmTensorClosedHomEquiv_of_exponentialData_braiding
          (frmTensorUnitExponentialData Z) Y h

/-- The closed native semantic witness frontier, at the current scoped
boundary. -/
theorem semantic_witness_frontier_nonempty :
    Nonempty SemanticWitnessFrontier :=
  ⟨{
    finite_heytalg_closed := fun P _ _ _ _ _ _ hD1 =>
      NativeHeytAlg.finite_closed_full_gut_nonempty P hD1
    encodable_heytalg_closed := fun P _ _ _ _ _ _ hD1 =>
      NativeHeytAlg.encodable_closed_stream_full_gut_nonempty P hD1
    finite_heytalg_hom_closed := fun P _ _ _ _ _ _ hD1 =>
      NativeHeytAlg.HomPresentation.finite_hom_closed_full_gut_nonempty P hD1
    encodable_heytalg_hom_closed := fun P _ _ _ _ _ _ hD1 =>
      NativeHeytAlg.HomPresentation.encodable_hom_closed_stream_full_gut_nonempty
        P hD1
    heytalg_posetal_closed_end_action := fun P =>
      P.heytAlg_posetal_closed_end_action_nonempty
    heytalg_hom_eval_transport := fun P =>
      P.mor_map_eval_le
    heytalg_hom_curry_transport := fun P =>
      P.mor_map_curry_iff
    indexed_heytalg_posetal_closed := fun {_} C =>
      NativeHeytAlg.indexed_posetal_closed_semantics_nonempty C
    finite_indexed_heytalg := fun {_} C _ base _ _ =>
      NativeHeytAlg.finite_indexed_category_full_gut_nonempty C base
    encodable_indexed_heytalg := fun {_} C _ base _ _ =>
      NativeHeytAlg.encodable_indexed_category_stream_full_gut_nonempty C base
    heytalg_bool_cartesian_exponent_obstruction :=
      NativeHeytAlg.no_bool_cartesian_exponent_representation
    heytalg_no_unit_to_nontrivial :=
      NativeHeytAlg.no_unit_to_nontrivial_hom
    bool_himp_not_sub_bimorphism :=
      SSBX.Foundation.Order.himp2_not_isSubBimorphism_Bool
    heytalg_categorical_boundary :=
      NativeHeytAlg.heytAlg_categorical_boundary_nonempty
    diamondH4_anchor := {
      anchor_existence_and_uniqueness :=
        SSBX.Foundation.Order.DiamondH4_anchor_existence_and_uniqueness
      linear_order_iso :=
        SSBX.Foundation.Order.DiamondH4_iso_linear
      himp_agrees_with_transferred_himp :=
        SSBX.Foundation.Order.DiamondH4.himp_match
      refined_p3 :=
        SSBX.Foundation.Order.P3_heyting_refined_DiamondH4
      p3_framework :=
        SSBX.Foundation.Order.P3_heyting_framework
      strong_eval_codomain_trivial := fun h =>
        SSBX.Foundation.Order.IsHeytingBilinear₂.codomain_trivial h }
    single_qubit_hilbert_dagger :=
      concrete_single_qubit_hilbert_dagger_bridge_nonempty
    single_qubit_matrix_dagger_full_gut :=
      NativeStabilizerQuantum.concrete_single_qubit_matrix_dagger_full_gut
    n_qubit_hilbert_bridge :=
      n_qubit_quantum_to_hilbert_bridge_nonempty
    n_qubit_hilbert_dagger_operator :=
      concrete_n_qubit_hilbert_dagger_operator_bridge_nonempty
    r_to_hilbert_quantum := r_to_hilbert_quantum_witness
    r_to_hilbert_end_action := r_to_hilbert_end_action_nonempty
    r_to_hilbert_tensor_boundary := r_to_hilbert_tensor_boundary
    r_to_hilbert_substrate_action_boundary :=
      r_to_hilbert_substrate_action_boundary_nonempty
    finite_hilbert_dagger_boundary := fin_hilb_dagger_boundary_nonempty
    finite_coordinate_hilbert_tensor_boundary :=
      fin_hilb_coordinate_tensor_boundary_nonempty
    finite_coordinate_hilbert_tensor_isometry_boundary :=
      fin_hilb_coordinate_tensor_isometry_boundary_nonempty
    finite_coordinate_hilbert_tensor_coherence_boundary :=
      fin_hilb_coordinate_tensor_coherence_boundary_nonempty
    finite_coordinate_hilbert_dagger_tensor_boundary :=
      fin_hilb_coordinate_dagger_tensor_boundary_nonempty
    finite_coordinate_hilbert_kronecker_morphism_boundary :=
      fin_hilb_coordinate_kronecker_morphism_boundary_nonempty
    finite_coordinate_hilbert_tensor_product_comparison_boundary :=
      fin_hilb_coordinate_tensor_product_comparison_boundary_nonempty
    finite_coordinate_hilbert_tensor_product_isometry_boundary :=
      fin_hilb_coordinate_tensor_product_isometry_boundary_nonempty
    stabilizer_hilbert_boundary := stabilizer_hilbert_coherence_boundary_nonempty
    matrix_hilbert_scalar := matrixHilbLinearMap_smul
    matrix_hilbert_adjoint := matrixHilbLinearMap_adjoint_conjTranspose
    pauli_base_hilbert_adjoint := pauliBaseHilbEnd_adjoint
    pauli_n_hilbert_adjoint := pauliNHilbEnd_adjoint
    r_to_hilbert_end_adjoint := rToHilbEnd_adjoint
    r_to_hilbert_end_projective_add_scalar := rToHilbEnd_projective_add_smul
    phased_pauli_hilbert_adjoint := phasedPauliNHilbEnd_adjoint
    pauli_hilbert_tensor_coherence :=
      SSBX.Foundation.Wen.Embeddings.HilbertPauliFunctor.pauliHilbertTensorCoherence
    phased_pauli_hilbert_action := phased_pauli_n_hilbert_action_nonempty
    phased_pauli_hilbert_tensor_action :=
      phased_pauli_hilbert_tensor_action_nonempty
    generic_n_qubit_hilbert_operator := fun {_} P _ _ _ _ _ hD1 =>
      n_qubit_presentation_hilbert_dagger_operator_bridge_nonempty P hD1
    n_qubit_matrix_tensor_unit :=
      NativeStabilizerQuantum.n_qubit_matrix_tensor_unit_witness
    concrete_n_qubit_matrix_tensor_unit_boundary :=
      NativeStabilizerQuantum.concrete_n_qubit_matrix_tensor_unit_boundary
    n_qubit_matrix_tensor :=
      NativeStabilizerQuantum.concrete_n_qubit_matrix_tensor_full_gut
    n_qubit_matrix_tensor_assoc :=
      NativeStabilizerQuantum.concrete_n_qubit_matrix_tensor_assoc_full_gut
    n_qubit_matrix_tensor_coherence_boundary :=
      NativeStabilizerQuantum.n_qubit_matrix_tensor_coherence_boundary_nonempty
    phased_monoidal_stabilizer :=
      NativeStabilizerQuantum.concrete_n_qubit_phased_monoidal_matrix_operator_full_gut
    phased_unital_monoidal_stabilizer :=
      NativeStabilizerQuantum.concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary
    topological_native_frame :=
      topological_native_frame_witness
    topological_locale :=
      topological_native_locale_witness
    topological_locale_represented_closed :=
      topological_native_locale_represented_closed_witness
    topological_locale_unit_closed :=
      topological_native_locale_unit_closed_witness
    topological_locale_represented_right_uncurry_eval := fun E k =>
      frmTensorClosedHomEquiv_of_exponentialData_symm_eq_tensor_eval E k
    topological_locale_represented_left_uncurry_eval := fun E k =>
      frmTensorClosedHomEquiv_of_exponentialData_braiding_symm_eq_braiding_tensor_eval
        E k
    topological_locale_unit_right_curry := fun Y Z =>
      ⟨frmTensorClosedHomEquiv_of_exponentialData
        (frmTensorUnitExponentialData Z) Y⟩
    topological_locale_unit_right_naturality := fun f h =>
      frmTensorClosedHomEquiv_of_exponentialData_naturality
        (frmTensorUnitExponentialData _) f h
    topological_locale_unit_left_curry := fun Y Z =>
      ⟨frmTensorClosedHomEquiv_of_exponentialData_braiding
        (frmTensorUnitExponentialData Z) Y⟩
    topological_locale_unit_left_naturality := fun f h =>
      frmTensorClosedHomEquiv_of_exponentialData_braiding_naturality
        (frmTensorUnitExponentialData _) f h }⟩

end SSBX.Foundation.Doctrine.Instance
