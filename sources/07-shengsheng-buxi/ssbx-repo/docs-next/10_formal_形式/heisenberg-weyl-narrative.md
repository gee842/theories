# Heisenberg-Weyl Stream — Coordinate Hilbert Boundary at GUT G11

> v0.1 · 2026-05-21 · narrative companion to the Lean source under
> `formal/SSBX/Foundation/Wen/Embeddings/Heisenberg*.lean` and
> `formal/SSBX/Foundation/Doctrine/Instance/{Quantum,HilbertEnriched}.lean`.
> Cross-link [claim-status-ledger.md](claim-status-ledger.md) v0.8 (2026-05-21).

This document narrates the ~25 commits, leading up to commit `588f37a` (Add
coordinate Hilbert dagger tensor boundary), that build out the odd-prime
Heisenberg-Weyl group and its concrete coordinate Hilbert action at the GUT
G11 frontier. The work is theorem-grade Lean code with no narrative companion
until now. The structure of this document mirrors that of the existing
[`quantum-roadmap.md`](quantum-roadmap.md) and uses the status vocabulary
fixed in [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 (closed /
scoped / schema / external route / sketch / placeholder / open).

The reading rule is the standard rule of the ledger: **read no more into a
theorem name than its Lean statement actually says.** No new mathematical
claim is made in this document beyond what is already in the Lean theorems.
Theorem names are quoted verbatim with `file:line` references so future
readers can `grep` and locate the actual statement.

---

## §1. Why this stream exists

### 1.1 G11 in the gut-roadmap

The current snapshot of [`gut-roadmap.md`](gut-roadmap.md) places the odd-prime
Heisenberg-Weyl work inside **G11** ("T5-B parametric over k (algebraic
class)"), and inside the G11 cut-1 plan:

> **G11** | T5-B parametric over k (algebraic class) | ✅ scoped cut-1 closed
> for canonical finite fields, prime fields, structure-gated arbitrary field
> satisfiers, odd-prime discriminant classification, odd-prime Heisenberg-Weyl
> phase-space/R-coordinate symplectic boundary, primitive complex additive
> phase, one-site clock/shift commutation, multi-site zero phase-point matrix
> identity, multi-site projective multiplication, symplectic commutator phase,
> left/right unitarity, phase-point matrix faithfulness, pure-shift coordinate
> reachability, pure-clock coordinate projectors, coordinate matrix-unit
> Fourier sums, phase-point matrix span/top, invariant-subspace
> irreducibility, the scoped concrete finite-Hilbert operator boundary, the
> scoped concrete finite-Hilbert object action boundary, the scoped
> finite-Hilbert dagger boundary, and finite-coordinate algebraic/isometric
> tensor-product comparison/naturality; arbitrary raw non-canonical
> finite-field satisfier synthesis plus full `FdHilb` categorical semantics
> remain open.

The same ledger paragraph appears in
[`gut-roadmap.md` §三 G7 row](gut-roadmap.md), which records that odd-prime
Heisenberg-Weyl phase-space/R-coordinate and supplied-character operator
boundaries have **moved out of G7** (the F₂/stabilizer-Hilbert branch was
closed in `FullGUTTier2Frontier.current_tier2_G7_cross_base_stabilizer_hilbert`
some time earlier) **and into G11**, because the symplectic form changes
shape for `p ≠ 2` and the F₂-XOR shortcut no longer applies.

### 1.2 "Quantum = classical R-family + Hilbert encoding"

The slogan that drives this stream lives one level above G11 in the
quantum-roadmap. The classical R-family layers `Rₙ` carry exactly `2ⁿ`
elements, and the quantum upgrade replaces each carrier `Rₙ` by the standard
finite-dimensional Hilbert space `(ℂ²)⊗ⁿ ≃ ℂ^(2ⁿ)` while keeping the
*algebraic skeleton* (R-hierarchy, V₄ Shi, (Z/2)⁸ Cayley regular rep, 道 as
origin, OX literals) unchanged. The Heisenberg-Weyl stream is the
realisation, at characteristic `p ≠ 2`, that "quantum = classical R-family
plus Hilbert encoding": phase space `(ZMod p)^{2n}` is the R-family
coordinate carrier with a non-XOR symplectic form, and the clock/shift
unitary operators on `ℂ^{p^n}` are the Hilbert encoding.

### 1.3 The pre-existing F₂ stabilizer stream

The F₂ case had already been closed before the work documented here:

- `Foundation/Wen/Embeddings/StabilizerQM.lean` (~743 lines) — `PauliN n ≃
  R (2 * n) (Bool)`, mod-phase commutation through `R.sigma`, σ as the
  symplectic form, and the V₄ ≃ R 2 ≃ PauliBase bridge.
- `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` (~960 lines) — the
  `2^n × 2^n` complex matrix representation `pauliToHilbert`, its
  faithfulness, unitarity, Hilbert-Schmidt orthogonality, and tensor
  coherence.
- `Foundation/Wen/Embeddings/PhasedPauli.lean` (~542 lines) — retained
  central phases, exact composition law, signed commutation.
- `Foundation/Wen/Embeddings/PauliRingIso.lean` (~700 lines) — the n-qubit
  Pauli spanning theorem for `Mat_{2^n}(ℂ)`.

The 25 commits documented here add the **`p ≠ 2` analogue** of the same
structures, but **leave the field generic** — every Lean theorem in this
stream is parametric over an arbitrary modulus / odd prime and an arbitrary
finite coordinate basis.

---

## §2. What was closed

Quick map of the new files (line counts approximate):

| File | LOC | Role |
|---|---|---|
| `Foundation/Wen/Embeddings/HeisenbergWeylZModP.lean` | ~232 | Phase space `(ZMod p)^{2n}`, alternating symplectic pairing, equivR bridge to R-family |
| `Foundation/Wen/Embeddings/HeisenbergWeylOperators.lean` | ~1164 | Supplied additive characters, primitive complex character, clock/shift matrices, phase-point matrices, full operator boundary |
| `Foundation/Doctrine/Instance/HilbertEnriched.lean` | ~2282 | `FinHilbObject`, coordinate Hilbert spaces, finite-coordinate tensor/unit/coherence/dagger/Kronecker boundaries, Heisenberg-Weyl `FinHilbObject` action |
| `Foundation/Doctrine/Instance/Quantum.lean` | ~1370 | The canonical `TGUTRealisation (Type 0) PauliBase` and the universal-sayability anchor for quantum |

### 2.1 `HeisenbergWeylZModP` — the coordinate phase-space layer

The file deliberately stops short of the Hilbert layer: no primitive root of
unity, no matrices, no `FdHilb` claims. It supplies the algebra of the finite
phase space `(ZMod p)^{2n}`.

**Carrier and R-family bridge**:

- `PhasePoint p n : Type` —
  `Fin n → ZMod p × ZMod p`, with per-site `xCoord` (shift exponent) and
  `zCoord` (clock exponent).
  See `HeisenbergWeylZModP.lean:39`.
- `PhasePoint.equivR (p n : ℕ) : PhasePoint p n ≃ R (2 * n) (ZMod p)` —
  the coordinate equivalence between the Heisenberg-Weyl phase-space
  carrier and the R-family layer `R (2*n)` over `ZMod p`. Same blockwise
  shape as the F₂ stabilizer / Pauli embedding, now with `ZMod p` instead
  of `Bool`. See `HeisenbergWeylZModP.lean:92`.

**Standard alternating symplectic pairing**:

- `PhasePoint.symplectic (u v : PhasePoint p n) : ZMod p` —
  `∑ᵢ xᵤᵢ zᵥᵢ - zᵤᵢ xᵥᵢ`.
  See `HeisenbergWeylZModP.lean:114`.
- `symplectic_self`, `symplectic_swap`, `symplectic_add_left`,
  `symplectic_add_right`, `symplectic_neg_left`,
  `symplectic_neg_right` — alternating, skew, additive, scalar-coherent
  laws. Critically, **none of these proofs require the odd-prime
  hypothesis**; they hold for every modulus. See `HeisenbergWeylZModP.lean:158-200`.
- `PhasePoint.symplecticBoundary (p n : ℕ) : SymplecticBoundary p n` —
  the closed package of the four laws plus the R-family bridge. See
  `HeisenbergWeylZModP.lean:218`.

The odd-prime hypothesis (`Nat.Prime p`, `p ≠ 2`) is **explicitly deferred**
to the operator branch (next file). The intent is to share the same
"R-family carrier with an alternating pairing" shape with the F₂ stabilizer
branch.

### 2.2 `HeisenbergWeylOperators` — the supplied-character operator boundary

This is the workhorse of the stream (~1164 lines). The design choice is
**data-oriented**: instead of constructing a primitive complex `p`-th root
of unity from analytic first principles every time, the file accepts an
`AdditivePhase p` as supplied data, proves the matrix algebra from the
character laws, and then separately gives `AdditivePhase.primitiveComplex p`
as the canonical Mathlib-backed instance.

**Supplied additive phase characters**:

- `AdditivePhase p : Type` — three fields: a function `phase : ZMod p →
  ℂ`, with `map_zero : phase 0 = 1` and `map_add : ∀ a b, phase (a + b) =
  phase a * phase b`. See `HeisenbergWeylOperators.lean:34`.
- `AdditivePhase.ofAddChar`, `toAddChar` — bridges to Mathlib's
  `AddChar (ZMod p) ℂ`. See `HeisenbergWeylOperators.lean:46-55`.
- `AdditivePhase.primitiveComplex (p : ℕ) [NeZero p] : AdditivePhase p` —
  the standard primitive complex additive phase, built from Mathlib's
  `Complex.isPrimitiveRoot_exp` and `AddChar.zmodChar`. See
  `HeisenbergWeylOperators.lean:69`.
- `primitiveComplex_isPrimitive` — confirms the primitive root assignment
  lands in `IsPrimitive`. See `HeisenbergWeylOperators.lean:75`.
- `phase_injective_of_isPrimitive` — primitive characters separate
  points of `ZMod p`. See `HeisenbergWeylOperators.lean:82`.
- `primitiveComplex_phase_injective` — corollary for the canonical phase.
  See `HeisenbergWeylOperators.lean:96`.
- `phase_star` / `phase_star_mul_self` /
  `phase_mul_star_self` / `phase_neg_mul_self` /
  `phase_ne_zero` — root-of-unity facts needed for unitarity later.
  See `HeisenbergWeylOperators.lean:103-139`.

**One-site clock and shift matrices**:

- `AdditivePhase.clockMatrix χ : Matrix (ZMod p) (ZMod p) ℂ` —
  diagonal with entries `χ.phase i`. See
  `HeisenbergWeylOperators.lean:142`.
- `AdditivePhase.shiftMatrix p : Matrix (ZMod p) (ZMod p) ℂ` —
  the cyclic shift with the row/column convention
  `(shift)ᵢⱼ = 1 if j = i + 1`. See `HeisenbergWeylOperators.lean:150`.
- `AdditivePhase.shift_mul_clock` — the core commutation identity
  `X Z = χ(1) • Z X`. See `HeisenbergWeylOperators.lean:165`.
- `AdditivePhase.ClockShiftBoundary p` /
  `AdditivePhase.clockShiftBoundary` — the closed one-site package. See
  `HeisenbergWeylOperators.lean:180-205`.

**Multi-site phase-point matrices**:

- `AdditivePhase.CoordinateBasis p n : Type` — the multi-site basis
  `Fin n → ZMod p`. See `HeisenbergWeylOperators.lean:210`.
- `AdditivePhase.phasePointMatrix χ (u : PhasePoint p n) :
  Matrix (CoordinateBasis p n) (CoordinateBasis p n) ℂ` —
  shift by `xCoord u`, multiply by `χ (z · r)`. The defining recursion
  composes one clock and one shift block per site. See
  `HeisenbergWeylOperators.lean:391`.
- `phasePointMatrix_zero` — the zero phase-space point gives the
  identity matrix. See `HeisenbergWeylOperators.lean:401`.
- `phasePointMatrix_mul` — **projective multiplication**: the
  matrices compose with cocycle `χ (⟨z_v, x_u⟩)`. See
  `HeisenbergWeylOperators.lean:464`.
- `phasePointMatrix_commutator` — **symplectic commutator phase**:
  swapping multiplication order multiplies by `χ (symplectic u v)`.
  This is the operator-side avatar of the symplectic form from
  `HeisenbergWeylZModP`. See `HeisenbergWeylOperators.lean:498`.
- `phasePointMatrix_conjTranspose_mul_self` and
  `phasePointMatrix_mul_conjTranspose_self` — left- and right-unitarity
  of the phase-point matrices, for every nonzero modulus. See
  `HeisenbergWeylOperators.lean:513` and `:552`.

**Faithfulness and pure-shift reachability**:

- `phasePointMatrix_injective_of_phase_injective` — when the supplied
  phase is injective on `ZMod p`, the phase-point matrix map separates
  phase-space points. See `HeisenbergWeylOperators.lean:1002`.
- `phasePointMatrix_injective_of_isPrimitive` /
  `primitiveComplex_phasePointMatrix_injective` — the primitive
  complex phase gives a faithful operator representation. See
  `HeisenbergWeylOperators.lean:1060` and `:1069`.
- `phasePointMatrix_pureShiftPoint` — phase-points whose `zCoord` is
  zero act as pure coordinate permutations. See
  `HeisenbergWeylOperators.lean:590`.
- `phasePointMatrix_coordinate_reachable_by_pure_shift` — every
  coordinate matrix entry `M r q = 1` is reachable by some pure-shift
  phase-point. See `HeisenbergWeylOperators.lean:600`.

**Coordinate projectors and Fourier sums**:

- `coordinateProjectorSum χ q : Matrix (CoordinateBasis p n) ...` —
  an unnormalised Fourier-style sum over `z`, with phase
  `χ (-(z · q))`, of pure-clock phase-points. See
  `HeisenbergWeylOperators.lean:673`.
- `coordinateProjectorSum_apply_of_ne` / `_apply_same` /
  `_apply` — extracts a single diagonal coordinate, scaled by the
  basis cardinality. See `HeisenbergWeylOperators.lean:683-749`.
- `coordinateMatrixUnitSum χ r q : Matrix ...` — the Fourier sum that
  isolates the matrix unit at `(r, q)`. See
  `HeisenbergWeylOperators.lean:754`.
- `coordinateMatrixUnitSum_apply` — exactly one nonzero entry, value
  `Fintype.card (CoordinateBasis p n)`. See
  `HeisenbergWeylOperators.lean:765`.
- `coordinateMatrixUnitSum_mem_span` / `_eq_card_smul_single` —
  rephrases the Fourier sum as a finite linear combination of
  phase-point matrices, scaled by the basis cardinality. See
  `HeisenbergWeylOperators.lean:828-845`.

**Span and irreducibility**:

- `matrix_single_mem_span_phasePointMatrix` — every coordinate matrix
  unit is in the ℂ-linear span of the phase-point matrices, provided
  the supplied phase is injective. See
  `HeisenbergWeylOperators.lean:861`.
- `phasePointMatrix_span_eq_top` — the phase-point matrices span the
  **entire matrix algebra** on `CoordinateBasis p n`. See
  `HeisenbergWeylOperators.lean:890`.
- `phasePointMatrix_span_mulVec_mem` — every operator in the span
  preserves any phase-point-invariant subspace. See
  `HeisenbergWeylOperators.lean:911`.
- `phasePointMatrix_invariant_subspace_eq_top` — **irreducibility**:
  any nonzero subspace stable under every phase-point matrix is all of
  `CoordinateBasis p n → ℂ`. See
  `HeisenbergWeylOperators.lean:938`.

**Packaged boundary**:

- `AdditivePhase.PhasePointMatrixBoundary p n` — collects every fact
  above into one structure. See
  `HeisenbergWeylOperators.lean:1079`.
- `AdditivePhase.phasePointMatrixBoundary` — closed witness. See
  `HeisenbergWeylOperators.lean:1135`.
- `AdditivePhase.phasePointMatrixBoundary_nonempty` — nonempty
  witness corollary. See `HeisenbergWeylOperators.lean:1154`.

### 2.3 The F₂ companions (pre-existing, used as the F₂ analogue)

The Heisenberg-Weyl stream does **not** replace the F₂ stabilizer stream; it
parallels it. The relevant pre-existing files are referenced here for
context but were not modified by these 25 commits:

- `Foundation/Wen/Embeddings/StabilizerQM.lean` — `PauliN n ≃ R (2 * n)`
  (`StabilizerQM.equiv`), mod-phase commutation through `R.sigma`
  (`PauliN.commutesModPhase_eq_not_sigma`, `commutesModPhase_iff_sigma_false`),
  single-qubit V₄ bridge (`SingleQubit.equivR2`, `baseEquivV4`).
- `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` — the recursive
  `pauliToHilbert`, its tensor coherence (`pauliHilbertTensorCoherence`,
  `pauliToHilbert_append_tensor`, `pauliToHilbert_tensor_unit_left`,
  `pauliToHilbert_tensor_unit_right`, `pauliToHilbert_append_tensor_assoc`),
  faithfulness, Hilbert-Schmidt orthogonality, self-adjointness, unitarity,
  and the composed `rToHilbert : R (2*n) → Matrix (Fin (2^n)) (Fin (2^n)) ℂ`
  bridge.
- `Foundation/Wen/Embeddings/PauliRingIso.lean` — `pauli_lin_indep`,
  `pauli_span_full`, `pauli_n_qubit_spans`, and the set-level
  `R 4 ≃ pauliF2Image` correspondence.
- `Foundation/Wen/Embeddings/PhasedPauli.lean` — retained central phases
  `PauliPhase`, exact same-width composition (`pauliToHilbert_mul_phase`),
  signed commutation (`pauliToHilbert_signed_commutation`),
  phase-bearing tensor append (`PhasedPauliN.toHilbert_tensor`), packaged
  `PhasedPauliN.HilbertCoherence`.

These are the F₂ analogue at `p = 2` of the same boundary the Heisenberg-Weyl
stream now supplies at general odd prime `p`.

### 2.4 `HilbertEnriched` — finite-Hilbert object, dagger, coordinate tensor

This is the bulk of the actual new categorical content (~2282 lines), and
the part that the most recent five commits in particular extend (commits
`5734d31` → `dd59239` → `0cb0682` → `1072bae` → `588f37a`).

The file is **explicit** that it does **not** build the full `FdHilb`
dagger-SMCC; it builds a concrete finite-Hilbert-object category and a
collection of scoped boundary packages.

**The finite-Hilbert object category**:

- `FinHilbObject : Type 1` — a finite-dimensional complex inner-product
  space, packaged as a `structure` with `NormedAddCommGroup`,
  `InnerProductSpace ℂ`, and `FiniteDimensional ℂ` instance fields. See
  `HilbertEnriched.lean:114`.
- `instance FinHilbObject.category : Category FinHilbObject` — morphisms
  are `H →ₗ[ℂ] K`. This is **not** the operator-bounded-map category and
  is **not** yet a dagger or symmetric monoidal closed category. See
  `HilbertEnriched.lean:131`.
- `coordinateHilb (n : ℕ) : FinHilbObject` — `EuclideanSpace ℂ (Fin n)`.
  See `HilbertEnriched.lean:214`.
- `qubitHilb : FinHilbObject` — `coordinateHilb 2`. See
  `HilbertEnriched.lean:221`.
- `coordinateHilbOf (ι : Type) [Fintype ι] : FinHilbObject` —
  arbitrary finite-index coordinate Hilbert object. This is the version
  used by the Heisenberg-Weyl coordinate basis. See
  `HilbertEnriched.lean:320`.

**Scoped finite-Hilbert dagger boundary**:

- `finHilbDagger : (H ⟶ K) → (K ⟶ H)` — `LinearMap.adjoint`. See
  `HilbertEnriched.lean:159`.
- `finHilbDagger_id`, `finHilbDagger_comp`, `finHilbDagger_dagger` — the
  three dagger laws on linear-map morphisms. See
  `HilbertEnriched.lean:164-179`.
- `FinHilbDaggerBoundary : Type 1` / `fin_hilb_dagger_boundary_nonempty`
  — the structure plus its nonempty witness. See
  `HilbertEnriched.lean:187` and `:204`. This is **the scoped dagger
  boundary**, not a bundled `DaggerCategory`.

**Finite-coordinate tensor / unit boundary** (commit `5734d31`, `0cb0682`,
`1072bae` extend this):

- `coordinateHilbTensorObj (ι κ : Type) [Fintype ι] [Fintype κ] :
  FinHilbObject` — `coordinateHilbOf (ι × κ)`. See
  `HilbertEnriched.lean:339`. Note: this is **product-coordinate**, not a
  Hilbert tensor product.
- `coordinateHilbTensorUnit : FinHilbObject` —
  `coordinateHilbOf PUnit`. See `HilbertEnriched.lean:344`.
- `coordinateHilbTensorLeftUnitor`, `_RightUnitor`, `_Associator`,
  `_Braiding` — coordinate reindexing equivalences induced by
  `Equiv.punitProd`, `Equiv.prodPUnit`, `Equiv.prodAssoc`,
  `Equiv.prodComm`. See `HilbertEnriched.lean:348-370`.
- `FinHilbCoordinateTensorBoundary` /
  `fin_hilb_coordinate_tensor_boundary_nonempty` — the closed package
  at object-and-reindexing level. See `HilbertEnriched.lean:379` and
  `:401`. This is **not** a bundled monoidal category, **not** a
  Hilbert tensor product, **not** a monoidal functor theorem.

**Finite-coordinate tensor / unit reindexing isometry boundary** (commit
`dd59239`):

- `coordinateHilbReindexIsometry e` —
  `LinearIsometryEquiv.piLpCongrLeft 2 ℂ ℂ e`. See
  `HilbertEnriched.lean:422`.
- `coordinateHilbTensorLeftUnitorIsometry`, `_RightUnitorIsometry`,
  `_AssociatorIsometry`, `_BraidingIsometry` — the same unitor /
  associator / braiding lifted from linear equiv to linear isometry
  equiv. See `HilbertEnriched.lean:428-447`.
- `FinHilbCoordinateTensorIsometryBoundary` /
  `fin_hilb_coordinate_tensor_isometry_boundary_nonempty` — the
  isometric upgrade of the linear boundary. See
  `HilbertEnriched.lean:458` and `:489`. Norm-preservation laws are
  recorded as explicit fields.

**Finite-coordinate tensor coherence boundary** (commit `1072bae`):

- `coordinateHilbReindexIsometry_trans` — coordinate reindexing
  isometries compose under `Equiv` composition. See
  `HilbertEnriched.lean:523`.
- `coordinateHilbTensor_triangle_isometry` — coordinate triangle
  coherence. See `HilbertEnriched.lean:537`.
- `coordinateHilbTensor_pentagon_isometry` — coordinate pentagon
  coherence. See `HilbertEnriched.lean:551`.
- `coordinateHilbTensor_braiding_involutive_isometry` — braiding
  involution. See `HilbertEnriched.lean:569`.
- `coordinateHilbTensor_braiding_hexagon_isometry` and
  `coordinateHilbTensor_braiding_inv_hexagon_isometry` — the two
  braided hexagons. See `HilbertEnriched.lean:583` and `:602`.
- `FinHilbCoordinateTensorCoherenceBoundary` /
  `fin_hilb_coordinate_tensor_coherence_boundary_nonempty` — the
  packaged triangle / pentagon / braiding-involution / hexagons.
  See `HilbertEnriched.lean:625` and `:670`. The Lean docstring is
  explicit: this is **not** a bundled monoidal category, **not** a
  naturality theorem, **not** a Hilbert tensor-product functor, **not**
  a dagger-SMCC theorem.

**Finite-coordinate dagger / tensor boundary** (commit `588f37a`, the
latest):

- `coordinateHilbKroneckerMap_adjoint` —
  `LinearMap.adjoint (coordinateHilbKroneckerMap A B) =
  coordinateHilbKroneckerMap (Aᴴ) (Bᴴ)`. See
  `HilbertEnriched.lean:814`.
- `FinHilbCoordinateDaggerTensorBoundary` /
  `fin_hilb_coordinate_dagger_tensor_boundary_nonempty` — the
  dagger-and-Kronecker boundary. See `HilbertEnriched.lean:1247` and
  `:1296`. This is the **dagger/tensor compatibility** for the
  Kronecker tensor on matrix-presented morphisms.

**Coordinate Kronecker tensor on matrix morphisms** (commit `b30ae50`):

- `coordinateHilbKroneckerMap (A : Matrix κ ι ℂ) (B : Matrix υ τ ℂ) :
  coordinateHilbTensorObj ι τ ⟶ coordinateHilbTensorObj κ υ` —
  `matrixHilbMapOf (A ⊗ₖ B)`. See `HilbertEnriched.lean:783`.
- `coordinateHilbKroneckerMap_id` — identity on identity. See
  `HilbertEnriched.lean:790`.
- `coordinateHilbKroneckerMap_comp` — Kronecker tensoring respects
  categorical composition. See `HilbertEnriched.lean:799`.
- `FinHilbCoordinateKroneckerMorphismBoundary` /
  `fin_hilb_coordinate_kronecker_morphism_boundary_nonempty` —
  Kronecker tensor as a (matrix-presented) morphism boundary. See
  `HilbertEnriched.lean:834` and `:873`.

**Coordinate algebraic tensor-product comparison** (commit `5734d31`):

- `coordinateHilbTensorProductComparison (ι τ : Type) :
  (coordinateHilbOf ι ⊗[ℂ] coordinateHilbOf τ) ≃ₗ[ℂ]
  coordinateHilbOf (ι × τ)` —
  the identification of Mathlib's algebraic tensor product with the
  product-indexed coordinate Hilbert object. See
  `HilbertEnriched.lean:917`.
- `coordinateHilbTensorProductComparison_toMatrix` — identity matrix in
  the standard product-of-bases. See `HilbertEnriched.lean:927`.
- `coordinateHilbTensorProductComparison_kronecker_naturality` — the
  algebraic-tensor `TensorProduct.map` and the coordinate Kronecker
  map agree under the comparison. See `HilbertEnriched.lean:966`.
- `FinHilbCoordinateTensorProductComparisonBoundary` /
  `fin_hilb_coordinate_tensor_product_comparison_boundary_nonempty` —
  the packaged comparison. See `HilbertEnriched.lean:1015` and `:1048`.

**Coordinate isometric tensor-product comparison** (commit `0cb0682`):

- `coordinateHilbTensorProductIsometryComparison` — isometric upgrade of
  the above algebraic comparison. See `HilbertEnriched.lean:1069`.
- `FinHilbCoordinateTensorProductIsometryBoundary` /
  `fin_hilb_coordinate_tensor_product_isometry_boundary_nonempty` —
  the isometric package. See `HilbertEnriched.lean:1119` and `:1149`.

**Heisenberg-Weyl `FinHilbObject` action** (commit `c54e42e` `Lift
Heisenberg-Weyl operators to finite Hilbert objects`):

- `heisenbergWeylHilb (p n : ℕ) : FinHilbObject` —
  `coordinateHilbOf (CoordinateBasis p n)`. See
  `HilbertEnriched.lean:1945`.
- `heisenbergWeylHilbEnd χ (u : PhasePoint p n) :
  heisenbergWeylHilb p n ⟶ heisenbergWeylHilb p n` — the phase-point
  matrix lifted to a `FinHilbObject` endomorphism. See
  `HilbertEnriched.lean:1952`.
- `heisenbergWeylHilbEnd_zero` — zero phase-space point gives the
  identity endomorphism. See `HilbertEnriched.lean:1959`.
- `heisenbergWeylHilbEnd_projective_comp` — the **projective
  composition law**: composing endomorphisms is the cocycle-scaled
  endomorphism for `u + v`, with cocycle `χ (⟨z_v, x_u⟩)`. See
  `HilbertEnriched.lean:1974`.
- `heisenbergWeylHilbEnd_adjoint` — Hilbert adjoint of the
  endomorphism is the conjugate-transpose phase-point matrix action.
  See `HilbertEnriched.lean:2002`.
- `heisenbergWeylHilbEnd_comp_adjoint` /
  `heisenbergWeylHilbEnd_adjoint_comp` — right- and left-unitarity in
  the concrete `FinHilbObject`, for every nonzero modulus. See
  `HilbertEnriched.lean:2021` and `:2045`.
- `HeisenbergWeylFiniteHilbertObjectActionBoundary p n` /
  `heisenberg_weyl_finite_hilbert_object_action_boundary_nonempty` —
  the packaged finite-Hilbert object action boundary, with character,
  Hilbert object, action, zero/projective composition, adjoint,
  unitarity, and the underlying matrix boundary. See
  `HilbertEnriched.lean:2069` and `:2110`.

This is the lift from "phase-point matrices in
`Matrix (CoordinateBasis p n) (CoordinateBasis p n) ℂ`" to
"endomorphisms of `FinHilbObject`".

### 2.5 `Doctrine/Instance/Quantum.lean` — the canonical TGUTRealisation

The Heisenberg-Weyl stream lands in the existing quantum doctrine instance
through the same `TGUTRealisation` interface already in place for the F₂
stabilizer branch.

**The canonical realisation**:

- `TGUTRealisation.quantum : TGUTRealisation (Type 0) PauliBase` —
  the canonical T_GUT realisation with carrier `R n := PauliN n =
  Fin n → PauliBase`, in the cartesian monoidal `Type 0` category, with
  generator `δ = PauliBase` (the single-qubit Pauli group mod phase).
  See `Quantum.lean:320`.
- `quantum_IsAdequate` — intrinsic standard `T_GUT` laws closed. See
  `Quantum.lean:498`.
- `quantum_HasCanonicalTransport` — canonical-transport laws closed. See
  `Quantum.lean:520`.
- `quantum_HasOpsCoherence` — split `square_diagonal` and
  `modal_V4_idempotent` ops-coherence laws closed. See
  `Quantum.lean:574`.
- `quantum_HasSemanticCoherence` — represented Hom/curry, atomic action,
  and Wedderburn semantic witnesses closed at coordinate level.

**The complete universal-sayability anchor for quantum**:

- `quantum_complete_universal_sayability :
  Nonempty (TGUTRealisation.CompleteUniversalSayability
    TGUTRealisation.quantum)` —
  the headline theorem. It is built from `IsAdequate`,
  `HasCanonicalTransport`, `HasSemanticCoherence`, and
  `HasOpsCoherence` via
  `TGUTRealisation.universal_sayability_complete_of_adequate`. See
  `Quantum.lean:771`.
- `quantum_universal_sayability_witness :
  Nonempty (TGUTRealisation.RealIso
    TGUTRealisation.quantum.toTGUTRealisationCore
    (TGUTRealisation.canonical (PauliBase : Type 0)))` —
  legacy carrier-level witness. See `Quantum.lean:1135`.

The Heisenberg-Weyl coordinate / operator boundaries supply the **operator
side** that the universal-sayability anchor depends on for `p ≠ 2`. The
**categorical-quantum-side** universal sayability for the Heisenberg-Weyl
representation **does not yet exist as a single theorem**; the closed
content is the per-boundary structure list above.

---

## §3. Status (per claim-status-ledger v0.8 categories)

The Heisenberg-Weyl stream is **closed at boundary-package level**, **scoped
to supplied characters / odd primes / parametric field**, and has explicit
**open** items for full `FdHilb` dagger-SMCC and for the Cell256 / R₈
specialisation.

### 3.1 Closed

Each theorem below is a non-placeholder Lean theorem whose statement carries
the claimed content. No `axiom`, no `sorry`.

| Theorem | Where | What it closes |
|---|---|---|
| `PhasePoint.symplectic_self`, `_swap`, `_add_left`, `_add_right`, `_neg_*` | `HeisenbergWeylZModP.lean:158-200` | alternating / skew / additive / scalar-coherent symplectic pairing on `(ZMod p)^{2n}`, **every modulus** |
| `PhasePoint.equivR` | `HeisenbergWeylZModP.lean:92` | the coordinate equivalence `PhasePoint p n ≃ R (2*n) (ZMod p)` |
| `PhasePoint.symplecticBoundary` | `HeisenbergWeylZModP.lean:218` | packaged coordinate boundary, every modulus |
| `AdditivePhase.primitiveComplex` / `primitiveComplex_isPrimitive` / `primitiveComplex_phase_injective` | `HeisenbergWeylOperators.lean:69-99` | the canonical primitive complex additive character |
| `AdditivePhase.shift_mul_clock` | `HeisenbergWeylOperators.lean:165` | one-site clock/shift commutation `X Z = χ(1) • Z X` |
| `AdditivePhase.clockShiftBoundary` | `HeisenbergWeylOperators.lean:191` | packaged one-site boundary |
| `AdditivePhase.phasePointMatrix_zero` | `HeisenbergWeylOperators.lean:401` | zero phase-point gives identity matrix |
| `AdditivePhase.phasePointMatrix_mul` | `HeisenbergWeylOperators.lean:464` | projective multiplication with cocycle `χ (⟨z_v, x_u⟩)` |
| `AdditivePhase.phasePointMatrix_commutator` | `HeisenbergWeylOperators.lean:498` | symplectic commutator phase |
| `AdditivePhase.phasePointMatrix_conjTranspose_mul_self` / `_mul_conjTranspose_self` | `HeisenbergWeylOperators.lean:513`, `:552` | left- and right-unitarity at every nonzero modulus |
| `AdditivePhase.phasePointMatrix_injective_of_phase_injective` / `_of_isPrimitive` | `HeisenbergWeylOperators.lean:1002`, `:1060` | faithfulness from injective phase |
| `AdditivePhase.phasePointMatrix_coordinate_reachable_by_pure_shift` | `HeisenbergWeylOperators.lean:600` | pure-shift coordinate reachability |
| `AdditivePhase.coordinateProjectorSum_apply` | `HeisenbergWeylOperators.lean:738` | pure-clock projector identifies a single coordinate |
| `AdditivePhase.coordinateMatrixUnitSum_apply` / `_eq_card_smul_single` | `HeisenbergWeylOperators.lean:765`, `:842` | Fourier-sum identification of matrix units |
| `AdditivePhase.phasePointMatrix_span_eq_top` | `HeisenbergWeylOperators.lean:890` | phase-point matrices span the full coordinate matrix algebra |
| `AdditivePhase.phasePointMatrix_invariant_subspace_eq_top` | `HeisenbergWeylOperators.lean:938` | irreducibility |
| `AdditivePhase.phasePointMatrixBoundary` | `HeisenbergWeylOperators.lean:1135` | packaged operator boundary |
| `FinHilbObject` / `FinHilbDaggerBoundary` / `fin_hilb_dagger_boundary_nonempty` | `HilbertEnriched.lean:114`, `:187`, `:204` | concrete finite-Hilbert object category and scoped dagger boundary |
| `FinHilbCoordinateTensorBoundary` / `_isometry` / `_coherence` / `_dagger_tensor` | `HilbertEnriched.lean:379`, `:458`, `:625`, `:1247` | finite-coordinate object tensor / unit / coherence / dagger boundaries |
| `FinHilbCoordinateKroneckerMorphismBoundary` | `HilbertEnriched.lean:834` | Kronecker tensor as a matrix-presented morphism boundary |
| `FinHilbCoordinateTensorProductComparisonBoundary` / `_Isometry` | `HilbertEnriched.lean:1015`, `:1119` | comparison with Mathlib's algebraic tensor product |
| `heisenbergWeylHilbEnd` / `_projective_comp` / `_adjoint` / `_comp_adjoint` / `_adjoint_comp` | `HilbertEnriched.lean:1952-2065` | lift of phase-point matrices to `FinHilbObject` endomorphisms |
| `HeisenbergWeylFiniteHilbertObjectActionBoundary` / `_nonempty` | `HilbertEnriched.lean:2069`, `:2110` | packaged finite-Hilbert object action |
| `TGUTRealisation.quantum` | `Quantum.lean:320` | the canonical `TGUTRealisation (Type 0) PauliBase` instance |
| `quantum_complete_universal_sayability` | `Quantum.lean:771` | the headline universal-sayability anchor for quantum |

### 3.2 Scoped

The closed theorems above are real theorems but are scoped along three axes:

- **Parametric over arbitrary modulus / odd prime `p` and arbitrary field
  `ZMod p`**. Every theorem in `HeisenbergWeylZModP` and `HeisenbergWeylOperators`
  has `(p n : ℕ)` as parameters. The `p ≠ 2` hypothesis is **introduced only
  where the analytic primitive character is needed** (via `NeZero p` plus
  the primitive-root data). Cell256 (i.e. `p = 2`, `n = 8`) is **not yet
  wired in**; see §3.3.
- **Supplied data**: most theorems take a supplied `AdditivePhase p` rather
  than constructing one. The canonical analytic instance
  `AdditivePhase.primitiveComplex p [NeZero p]` is supplied separately;
  faithfulness etc. then specialise to it.
- **Coordinate / linear-map / matrix layer**: `FinHilbObject` is the
  ordinary linear-map category, not the bounded-operator dagger SMCC.
  The tensor object is `coordinateHilbOf (ι × κ)`, **not** a Mathlib
  `TensorProduct ⊗ₕ`. The algebraic-tensor comparison with
  `coordinateHilbOf ι ⊗[ℂ] coordinateHilbOf κ` exists at coordinate level
  but does **not** upgrade to a Hilbert tensor product on arbitrary
  finite-dimensional Hilbert spaces.

The ledger row that summarises this is the **G11 finite-field cut-1** entry
in [`claim-status-ledger.md`](claim-status-ledger.md) v0.8, and the
**Native stabilizer quantum witness** row, which both explicitly call out
that "full `FdHilb` / dagger-SMCC semantics remains open".

### 3.3 Open

Three load-bearing things remain open at the categorical / wiring level:

1. **Full `FdHilb` dagger-SMCC**. The `FinHilbObject` category here is
   the linear-map category; it carries the scoped adjoint dagger boundary
   `FinHilbDaggerBoundary` but is **not** a bundled `DaggerCategory`.
   `coordinateHilbTensorObj` is product-coordinate, **not** a Hilbert
   tensor product; the existence of an isometric tensor-product comparison
   `FinHilbCoordinateTensorProductIsometryBoundary` only matches the
   product-coordinate object against Mathlib's algebraic
   `TensorProduct ⊗[ℂ]`, it does not exhibit a Hilbert SMCC. **Open**
   per the ledger; the next quantum target named in the ledger §G11 row
   is "a genuine bundled `FdHilb`/dagger-category layer, then monoidal
   Hilbert functor data". No theorem in this stream claims it.

2. **Categorical exponential / monoidal-closed Hilbert**. No statement
   in this stream constructs an exponential object for finite-dimensional
   Hilbert spaces or a `MonoidalClosed FinHilbObject` instance. The
   represented currying / evaluation infrastructure exists on the `Frm`
   side via `FrmExponentialData`, but the corresponding Hilbert
   construction is **open**. Per ledger row "HeytAlg internal-Hom /
   FdHilb / Frm semantics", full Hilbert/dagger semantics is open.

3. **Bridge to Cell256 / R₈ / 易卦**. The Heisenberg-Weyl theorems are
   parametric in `p, n`. The Cell256 specialisation (`p = 2`, `n = 8`)
   should recover the R₈ Hilbert encoding of the eight-yao 易卦 layer
   per the `quantum-roadmap.md` table. **This specialisation has not been
   wired**: no Lean theorem of the form
   `(ZMod 2)^{2*8}-HW ≃ R(2*8)-Bool ≃ Cell256` recovers Cell256
   operations from the supplied-character phase-point matrices at `p = 2,
   n = 8`. See §6 below.

### 3.4 Schema / placeholder / external route

- `HilbertPauliFunctor.rfamilyZModP (p : ℕ) (N : ℕ) : Type :=
  RFamily (ZMod p) N` — explicitly a **schema** placeholder for the
  `RFamily (ZMod p)` carrier. The docstring states the symplectic /
  Pauli commutation structure does **not** lift uniformly from F₂; the
  Heisenberg-Weyl operator stream is the substitute for that schema. See
  `HilbertPauliFunctor.lean:938`.
- No `external route` or `sketch` claims are added in this stream — the
  Heisenberg-Weyl content is fully formal in Lean.

---

## §4. Where the claim sits in universal sayability

The closed obligation at the quantum side of the universal-sayability claim
is `quantum_complete_universal_sayability` (`Quantum.lean:771`):

```
quantum_complete_universal_sayability :
  Nonempty (TGUTRealisation.CompleteUniversalSayability
    TGUTRealisation.quantum)
```

This is built from `quantum_IsAdequate`, `quantum_HasCanonicalTransport`,
`quantum_HasSemanticCoherence`, `quantum_HasOpsCoherence` via
`TGUTRealisation.universal_sayability_complete_of_adequate`. The
Heisenberg-Weyl stream **does not directly enter** this proof; the proof
goes through the **F₂ stabilizer** branch (carrier `PauliN n ≃ R (2*n)
Bool` with σ as the commutator form).

What the Heisenberg-Weyl stream **does** is supply the matching boundary
packages **at `p ≠ 2`**, so that the same shape of proof can be replayed at
characteristic `p ≠ 2` once a `TGUTRealisation` instance carrying
`PhasePoint p` (or equivalently `RFamily (ZMod p)`) as carrier is wired in.

The slogan from the task brief —

> "we claim everything sayable is representable"

— maps to two ledger rows in [`claim-status-ledger.md`](claim-status-ledger.md):

- **Full GUT theorem interface** (`absolute_conditional_full_gut`,
  `conditional_absolute_full_gut`) — the closed schema.
- **Native stabilizer quantum witness** — the F₂ instance of the schema.

The Heisenberg-Weyl stream extends the **list of closed boundary packages**
under the second row to include odd-prime phase-space coordinates,
operators, finite-Hilbert objects, dagger, coordinate tensor / unit /
coherence, Kronecker morphism, and algebraic/isometric tensor-product
comparison. It does **not** supply a new `CompleteUniversalSayability`
theorem at `p ≠ 2`; that synthesis still needs (a) a `TGUTRealisation`
instance with `R n := PhasePoint p n` (or
`RFamily (ZMod p) (2*n)`) as its underlying carrier, and (b) the
canonical-transport / semantic / ops coherence laws for that instance.

What is **not yet supplied** by this stream:

- **V-enriched Power-1999 closure** — open at the ledger level
  (`HeytAlg internal-Hom / FdHilb / Frm semantics` row). The
  `coordinateHilbTensorProductComparison` and its isometric upgrade
  identify the product-coordinate object with Mathlib's algebraic
  tensor product, but do **not** exhibit a monoidal-closed Hilbert
  structure or a Power 1999 enriched universal sayability proof.

---

## §5. Connection to the R-tower

The R-family carrier `R N δ = Fin N → δ` for `δ = ZMod p` carries the same
shape as the phase-space `PhasePoint p n`:

- `PhasePoint p n ≃ R (2 * n) (ZMod p)` —
  `PhasePoint.equivR (HeisenbergWeylZModP.lean:92)` is the formal bridge.
- Each phase-space coordinate splits into `(xCoord, zCoord) ∈ ZMod p × ZMod p`,
  matching the R-family blockwise convention used throughout the
  stabilizer / Pauli embedding.
- The alternating symplectic pairing `PhasePoint.symplectic` is the
  obvious R-family-side bilinear form
  `Σᵢ xᵤᵢ zᵥᵢ - zᵤᵢ xᵥᵢ`; at `p = 2` this is the F₂-symplectic form
  `R.sigma` from `Foundation/R/Bilinear.lean` (modulo carrier conversion).

So at `p = 2`, the Heisenberg-Weyl phase space **reduces to** the F₂
symplectic R-family of the stabilizer branch, and the symplectic pairing
specialises to `R.sigma`. The matching equivalence on the F₂ side is
`StabilizerQM.equiv : PauliN n ≃ R (2 * n)` (with `R (2*n)` being
`R (2*n) Bool`).

The expected next step — the Cell256 specialisation at `p = 2, n = 8` —
would compose:

```
HilbertPauliFunctor.boolEquivZMod2  -- Bool ≃ ZMod 2
HilbertPauliFunctor.rfamilyBoolEquivZMod2  -- RFamily Bool N ≃ RFamily (ZMod 2) N
PhasePoint.equivR  -- PhasePoint 2 n ≃ R (2*n) (ZMod 2)
```

and recover Cell256 (the R₈ layer) from `PhasePoint 2 8`. This is the
**obvious next step**; it is **not yet wired**. See §6.

---

## §6. Connection to Cell256 / 易卦 — the gap

The expected next theorem, in narrative form:

> There is an explicit specialisation functor
> `(ZMod 2)^{2n}-HW → R(2n)-Bool` at `n = 8` that recovers Cell256
> operations.

Such a functor does **not yet exist as a Lean theorem in this stream**.

What does exist that would feed it:

- `PhasePoint.equivR (p := 2) (n := 8) :
  PhasePoint 2 8 ≃ R (2 * 8) (ZMod 2)` — coordinate-level
  identification of the Heisenberg-Weyl `p = 2, n = 8` carrier with the
  R-family `R 16 (ZMod 2)` carrier. **Closed.**
- `HilbertPauliFunctor.boolEquivZMod2 : Bool ≃ ZMod 2` and
  `HilbertPauliFunctor.rfamilyBoolEquivZMod2 (N : ℕ) :
  RFamily Bool N ≃ RFamily (ZMod 2) N` — carrier-level bridges
  between `Bool` and `ZMod 2`. **Closed**, in
  `HilbertPauliFunctor.lean:899-919`.
- `Foundation/Bagua/Cell256.lean` — the R₈ Cell256 layer with V₄ Shi
  + Cayley regular rep. **Pre-existing.**

What would be required to close the gap (this stream does **not** supply
these):

1. A theorem of the form
   `RFamily (ZMod 2) (2 * 8) ≃ R (2 * 8) Bool ≃ Cell256` exhibiting the
   carrier round-trip.
2. A theorem matching `PhasePoint.symplectic` at `p = 2, n = 8` against
   `R.sigma : R 16 × R 16 → Bool` modulo the `Bool ≃ ZMod 2` bridge.
3. A theorem identifying the supplied-character phase-point matrices
   `phasePointMatrix χ` at `p = 2, n = 8` with the F₂-Pauli matrices
   `pauliToHilbert (rToPauli v)` for the corresponding R-family vector.

The first item is essentially trivial via the existing bridges; the second
and third require either (a) supplied data on the F₂ side that the F₂
`R.sigma` agrees with `PhasePoint.symplectic` modulo `Bool ≃ ZMod 2`, or
(b) a small specialisation theorem identifying the
`phasePointMatrix (primitiveComplex 2)` matrices at `p = 2` with the
phase-quotient Pauli matrices `pauliBaseToHilbert`.

None of these specialisation theorems is in the closed list above. They are
**open** items at the "Cell256 / 易卦 wiring" interface.

---

## §7. What's NOT claimed

To prevent over-reading, this section enumerates what the Heisenberg-Weyl
stream does **not** establish.

- **No axiom-free FdHilb**. The work here builds a concrete
  `FinHilbObject` category with linear-map morphisms and a scoped
  dagger boundary `FinHilbDaggerBoundary`. It is **not** a bundled
  Mathlib `DaggerCategory`, **not** a Mathlib `MonoidalCategory`, and
  **not** a Mathlib `SymmetricMonoidalCategory`. The ledger row
  "HeytAlg internal-Hom / FdHilb / Frm semantics" remains open at the
  categorical / exponential level.
- **No monoidal-closed `Frm` or `HeytAlg`**. The `Frm` side has
  `FrmExponentialData` / `FrmRepresentedClosedBoundary` already
  closed elsewhere (`TopologicalNativeLocale` / `FrmClosed.lean`); the
  Heisenberg-Weyl stream does **not** transport any of that to the
  Hilbert side. No exponential object, no internal-Hom, no
  `MonoidalClosed FinHilbObject` is constructed.
- **No automatic semantic witness for arbitrary SMCCs**. The closed
  obligation in `Quantum.lean:771`
  (`quantum_complete_universal_sayability`) is for the **fixed**
  realisation `TGUTRealisation.quantum`, not for "every SMCC". The
  Heisenberg-Weyl stream does not change this.
- **No claim at `p = 2` carrier**. The `HeisenbergWeylZModP.lean`
  laws are valid for every modulus, but the canonical
  `primitiveComplex p` requires `NeZero p` and the docstring says
  "the future operator representation will [need `p ≠ 2`]" — even
  though the operator-side theorems in `HeisenbergWeylOperators.lean`
  use only `NeZero p`, the **intended scope** is `p` odd prime, with
  Cell256 / F₂ handled by the stabilizer branch instead.
- **No Power-1999 enriched closure**. The closure of universal
  sayability under V-enrichment (Power 1999) is **open** at the
  ledger level and is **not** addressed by this stream.
- **No new universal sayability claim at quantum**. The closed
  theorem `quantum_complete_universal_sayability` is built from the
  pre-existing F₂ stabilizer machinery. The Heisenberg-Weyl stream
  adds **boundary content** for the odd-prime branch but does not
  produce a new top-level universal-sayability theorem at `p ≠ 2`.

---

## §8. Summary

The Heisenberg-Weyl stream is **scoped closed** at the boundary-package
level, **scoped to** supplied characters and odd-prime moduli over an
arbitrary field `ZMod p`, and **open** at: (a) full `FdHilb` dagger-SMCC,
(b) categorical exponential / monoidal-closed Hilbert, and (c) the
Cell256 / R₈ specialisation that would bridge to the 易卦 layer. The
closed content lives in `HeisenbergWeylZModP.lean`,
`HeisenbergWeylOperators.lean`, and `HilbertEnriched.lean`, and lands as
canonical `TGUTRealisation` data and an auxiliary boundary list inside
`Doctrine/Instance/Quantum.lean`.

For exact ledger row mapping see [claim-status-ledger.md](claim-status-ledger.md)
v0.8 (2026-05-21), in particular:

- **G11 finite-field cut-1** — names the Heisenberg-Weyl coordinate /
  operator boundaries and the scoped concrete finite-Hilbert operator,
  object-action, and dagger boundaries as closed.
- **Native stabilizer quantum witness** — names the
  `FinHilbObject` category, scoped `FinHilbDaggerBoundary`, scoped
  `FinHilbCoordinateTensorBoundary` and variants, scoped Kronecker
  morphism boundary, and the `heisenbergWeylHilbEnd` action.
- **HeytAlg internal-Hom / FdHilb / Frm semantics** — names full
  `FdHilb` / dagger-SMCC, `MonoidalClosed Frm`, and exponential-frame
  / non-cartesian Frm tensor-exponential T_GUT as the still-open
  categorical targets.
- **FullGUT combined frontier package** — exposes the direct
  accessors `current_full_gut_g11_odd_prime_heisenberg_weyl_*` for the
  closed boundary list, including
  `_phase_point_matrix_span_top`,
  `_phase_point_invariant_subspace_eq_top`,
  `_finite_hilbert_operator_boundary`,
  `_finite_hilbert_object_action_boundary`,
  `_finite_hilbert_dagger_boundary`.

The narrative slogan — "quantum = classical R-family + Hilbert encoding"
— is matched at the level of the closed Lean boundaries: phase space
`(ZMod p)^{2n}` is the R-family carrier (`PhasePoint.equivR`), the
alternating symplectic pairing is the F₂ generalisation of `R.sigma`,
the supplied-character phase-point matrices are the unitary clock/shift
operators with cocycle = character of the symplectic pairing, and the
finite-Hilbert lift `heisenbergWeylHilbEnd` is the categorical
endomorphism action on the concrete `FinHilbObject`. The next
substantive step, beyond polishing, is the bridge from this scoped
boundary list to a bundled `FdHilb` dagger-SMCC and to the Cell256 /
R₈ / 易卦 specialisation at `p = 2, n = 8`.
