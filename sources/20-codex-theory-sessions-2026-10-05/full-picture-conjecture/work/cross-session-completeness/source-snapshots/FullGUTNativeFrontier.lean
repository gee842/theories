/-
Copyright (c) 2026 SSBX contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: SSBX / Full GUT native-semantics pass
-/
import SSBX.Foundation.Doctrine.FullGUT
import SSBX.Foundation.Doctrine.Instance.SemanticWitnessFrontier

/-!
# Foundation.Doctrine.FullGUTNativeFrontier

Downstream package combining the theorem-grade FullGUT stack with the current
native semantic witness frontier.

This file is intentionally separate from `FullGUT.lean`: the native semantic
instance files depend on the FullGUT interface, so importing them back into
`FullGUT.lean` would create the wrong dependency direction.
-/

namespace SSBX.Foundation.Doctrine.FullGUTNativeFrontier

open SSBX.Foundation.Doctrine.FullGUT
open SSBX.Foundation.Doctrine.Instance

universe u

/-- Current FullGUT theorem stack together with the native semantic witness
frontier.

The first component is the conditional/scoped FullGUT theorem stack; the
second component is the closed frontier of native witness families.  This
does not remove the explicit semantic-preservation hypotheses from the
conditional absolute theorem, and it does not claim the still-open categorical
or enriched targets. -/
structure CurrentNativeSemanticFullGUTFrontier : Type (u + 2) where
  conditional_absolute : Nonempty ConditionalAbsoluteFullGUT
  substrate_certificate : Nonempty UniversalFormalSubstrateCertificate
  scoped_coordinate : Nonempty ScopedCoordinateFullGUT
  native_semantic_frontier : Nonempty (SemanticWitnessFrontier.{u})

/-- The current downstream package combining FullGUT and native semantic
witness frontiers is closed at its stated scope. -/
theorem current_native_semantic_full_gut_frontier :
    Nonempty (CurrentNativeSemanticFullGUTFrontier.{u}) :=
  ⟨{
    conditional_absolute := conditional_absolute_full_gut
    substrate_certificate := full_gut_universal_sayability
    scoped_coordinate := scoped_coordinate_full_gut
    native_semantic_frontier := semantic_witness_frontier_nonempty }⟩

/-- Direct native-frontier accessor for the current R-substrate-to-Hilbert
action boundary.

This packages faithful coordinate R-to-Hilbert witnesses, represented
endomorphism actions, and tensor append at stabilizer width.  It is not a
full `FdHilb` functoriality theorem. -/
theorem current_native_semantic_r_to_hilbert_substrate_action_boundary :
    Nonempty RToHilbertSubstrateActionBoundary :=
  r_to_hilbert_substrate_action_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-Hilbert dagger
boundary.

This records Hilbert adjoint as an identity-preserving, composition-reversing,
involutive operation on the concrete finite-Hilbert-object linear-map
category.  It is not a bundled `FdHilb` dagger-SMCC theorem. -/
theorem current_native_semantic_finite_hilbert_dagger_boundary :
    Nonempty FinHilbDaggerBoundary :=
  fin_hilb_dagger_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate Hilbert
tensor/unit object boundary.

This records the coordinate tensor shape `ι × κ`, the coordinate unit
`PUnit`, and the unit/associativity/braiding reindexing equivalences.  It is
not a bundled `FdHilb` monoidal category or Hilbert tensor-product functor. -/
theorem current_native_semantic_finite_coordinate_hilbert_tensor_boundary :
    Nonempty FinHilbCoordinateTensorBoundary :=
  fin_hilb_coordinate_tensor_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate Hilbert
tensor/unit isometry boundary.

This upgrades the product-coordinate unitors, associator, and braiding from
linear reindexing equivalences to linear isometry equivalences.  It is not a
bundled `FdHilb` monoidal category, coherence theorem, Hilbert tensor-product
functor, or dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_tensor_isometry_boundary :
    Nonempty FinHilbCoordinateTensorIsometryBoundary :=
  fin_hilb_coordinate_tensor_isometry_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate Hilbert
tensor coherence boundary.

This packages triangle, pentagon, braiding involution, and both braided
hexagons for the product-coordinate `LinearIsometryEquiv` reindexing maps.
It is not a bundled `FdHilb` monoidal category, naturality theorem, Hilbert
tensor-product functor, or dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_tensor_coherence_boundary :
    Nonempty FinHilbCoordinateTensorCoherenceBoundary :=
  fin_hilb_coordinate_tensor_coherence_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate Hilbert
dagger/tensor boundary.

This packages Hilbert-adjoint compatibility for the finite-coordinate tensor
frontier: structural isometries have adjoint equal to inverse, Kronecker
matrix tensoring respects conjugate transpose, and the tensor-product
comparison isometry has adjoint equal to inverse.  It is not a bundled
`FdHilb` dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_dagger_tensor_boundary :
    Nonempty FinHilbCoordinateDaggerTensorBoundary :=
  fin_hilb_coordinate_dagger_tensor_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate Hilbert
Kronecker morphism boundary.

This extends product-indexed coordinate tensor objects to finite-coordinate
matrix morphisms via Kronecker product, with identity, composition, and
adjoint laws.  It remains a coordinate matrix boundary, not a bundled
`FdHilb` monoidal or dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_kronecker_morphism_boundary :
    Nonempty FinHilbCoordinateKroneckerMorphismBoundary :=
  fin_hilb_coordinate_kronecker_morphism_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate
comparison between product-indexed Hilbert objects and Mathlib algebraic
tensor products.

This comparison identifies `coordinateHilbOf (ι × κ)` with
`coordinateHilbOf ι ⊗[ℂ] coordinateHilbOf κ` through standard bases and is
natural for matrix-presented maps via the Kronecker boundary.  It is not a
bundled `FdHilb` tensor functor or dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_tensor_product_comparison_boundary :
    Nonempty FinHilbCoordinateTensorProductComparisonBoundary :=
  fin_hilb_coordinate_tensor_product_comparison_boundary_nonempty

/-- Direct native-frontier accessor for the scoped finite-coordinate isometric
comparison between product-indexed Hilbert objects and Mathlib algebraic
tensor products.

This refines the linear comparison to a `LinearIsometryEquiv` and keeps the
same Kronecker naturality for matrix-presented maps.  It is not a bundled
`FdHilb` tensor functor or dagger-SMCC theorem. -/
theorem current_native_semantic_finite_coordinate_hilbert_tensor_product_isometry_boundary :
    Nonempty FinHilbCoordinateTensorProductIsometryBoundary :=
  fin_hilb_coordinate_tensor_product_isometry_boundary_nonempty

/-- Direct native-frontier accessor for the strongest current finite-Hilbert
stabilizer coherence boundary.

This bundles the matrix identity/composition/adjoint laws, Pauli/R Hilbert
actions, tensor coherence, and native n-qubit operator packages already proved
at coordinate level.  It is not a bundled `FdHilb` dagger-SMCC theorem. -/
theorem current_native_semantic_stabilizer_hilbert_coherence_boundary :
    Nonempty StabilizerHilbertCoherenceBoundary :=
  stabilizer_hilbert_coherence_boundary_nonempty

/-- Direct native-frontier accessor for the concrete 0-qubit tensor-unit
boundary against a nonempty concrete `n`-qubit stabilizer matrix package.

This remains a concrete matrix boundary, not a full `FdHilb` monoidal functor
or a 0-qubit D1/FullGUT package. -/
theorem current_native_semantic_concrete_n_qubit_matrix_tensor_unit_boundary
    (n : ℕ) (hn : 1 ≤ n) :
    Nonempty
      (NativeStabilizerQuantum.ConcreteNQubitMatrixTensorUnitBoundary n hn) :=
  NativeStabilizerQuantum.concrete_n_qubit_matrix_tensor_unit_boundary n hn

/-- Direct native-frontier accessor for the concrete phased stabilizer matrix
package with binary tensor splits, associativity, and 0-qubit unit coherence.

This is scoped to concrete nonempty Pauli-coordinate blocks; it is not a
bundled dagger-SMCC theorem for all finite-dimensional Hilbert spaces. -/
theorem current_native_semantic_concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary
    (n m k : ℕ) (hn : 1 ≤ n) (hm : 1 ≤ m) (hk : 1 ≤ k) :
    Nonempty
      (NativeStabilizerQuantum.ConcreteNQubitPhasedUnitalMonoidalMatrixOperatorBoundary
        n m k hn hm hk) :=
  NativeStabilizerQuantum.concrete_n_qubit_phased_unital_monoidal_matrix_operator_boundary
    n m k hn hm hk

end SSBX.Foundation.Doctrine.FullGUTNativeFrontier
