# Code-Doc Gap — what wen-substrate promises vs what Lean delivers

> **D7 transparency document.** An honest, section-by-section map between the claims
> made in [`wen-substrate/`](wen-substrate/00-README.md) and the Lean code under
> `formal/SSBX/Foundation/` that currently backs them.
>
> v1.52 · 2026-05-21 · companion to wen-substrate. Last verified: 2026-05-21.
> For the current high-level proof-strength ledger, read
> [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 (2026-05-21) — it is
> the authoritative status surface; this document maps section-by-section paths
> and is downstream of the ledger.
>
> **v1.52 delta** since v1.51:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateDaggerTensorBoundary`, packaging Hilbert-adjoint
> compatibility for the finite-coordinate tensor frontier: structural
> `LinearIsometryEquiv` maps have adjoint equal to inverse, Kronecker tensor
> maps obey conjugate-transpose dagger, and the tensor-product comparison
> isometry has adjoint equal to inverse. This is still not a bundled
> `DaggerCategory`, monoidal category, Hilbert tensor-product functor, full
> `FdHilb`, or dagger-SMCC theorem.
>
> **v1.51 delta** since v1.50:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateTensorCoherenceBoundary`, proving triangle, pentagon,
> braiding involution, and both braided hexagons for the product-coordinate
> `LinearIsometryEquiv` reindexing maps. `SemanticWitnessFrontier`,
> `FullGUTNativeFrontier`, and `FullGUTFrontier` expose the package through
> direct accessors. This is still not a bundled monoidal category, naturality
> theorem, Hilbert tensor-product functor, full `FdHilb`, or dagger-SMCC
> semantics.
>
> **v1.50 delta** since v1.49:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateTensorIsometryBoundary`, upgrading the product-coordinate
> tensor/unit reindexing maps to `LinearIsometryEquiv`s for the left and right
> unitors, associator, and braiding. The package records norm preservation for
> each of those finite-coordinate maps and is exposed through
> `SemanticWitnessFrontier`, `FullGUTNativeFrontier`, and `FullGUTFrontier`.
> This is still not a bundled monoidal category, a pentagon/triangle coherence
> theorem, a Hilbert tensor-product functor, full `FdHilb`, or dagger-SMCC
> semantics.
>
> **v1.49 delta** since v1.48:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateTensorProductIsometryBoundary`, upgrading the finite
> coordinate algebraic tensor comparison to a `LinearIsometryEquiv`. The
> package proves the isometry's underlying linear equivalence is the existing
> coordinate tensor-product comparison, preserves norm, and keeps the same
> Kronecker naturality for matrix-presented finite-coordinate maps. This is
> still not a bundled tensor on arbitrary `FinHilbObject`s, full `FdHilb`, a
> Hilbert tensor-product functor, or dagger-SMCC semantics.
>
> **v1.48 delta** since v1.47:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateTensorProductComparisonBoundary`, comparing
> `coordinateHilbOf (ι × κ)` with Mathlib's algebraic tensor product
> `coordinateHilbOf ι ⊗[ℂ] coordinateHilbOf κ` by the tensor product of
> standard bases. Its naturality law says `TensorProduct.map` on
> finite-coordinate matrix-presented maps corresponds under this comparison to
> the existing Kronecker coordinate map. `SemanticWitnessFrontier`,
> `FullGUTNativeFrontier`, and `FullGUTFrontier` expose the boundary through
> direct accessors. This is a finite-coordinate algebraic tensor comparison
> boundary only; it is not a bundled tensor on arbitrary `FinHilbObject`s, a
> Hilbert tensor-product functor, full `FdHilb`, or a dagger-SMCC theorem.
>
> **v1.47 delta** since v1.46:
> `R/GUTAClosure.lean` now exposes `scoped_gut_a_closed`, a public R-layer
> aggregate for the scoped F₂/GUT-A boundary. It packages Phase 0
> (`scoped_phase_zero_closed`), Phase 1 (`scoped_phase_one_closed`), the T5-A
> synthetic core (`T5_A_aggregator`), T5-A side items 8/9/11
> (`T5_A_full_side_obligations`), and the concrete F₂ D5/D6 exact/refuted
> package. This closes Scoped GUT-A, not absolute FullGUT or automatic semantic
> witness construction.
>
> **v1.46 delta** since v1.45:
> `R/PhaseZero/Closure.lean` now exposes `scoped_phase_zero_closed`, an
> acyclic aggregate for the completed scoped F₂/GUT-A Phase 0 layer. It
> packages `complete_phase_zero` with G6.1 (`T_P3_arf_surjective`,
> `T_P3_sigma_uniqueness_R2`), G6.2 (`T_P6_minimality_packaged`,
> `T_P6_lorentzian_bridge`), G6.3 (`T_P7b_full`,
> `T_P7b_form_b_packaged`), and `R4_structurally_minimal_full`. This
> closes Phase 0 at the scoped boundary, not the later all-dimensional
> Witt-Arf / arbitrary simple-algebra / GUT-C obligations.
>
> **v1.45 delta** since v1.44:
> `R/JudgmentRequest.lean` now proves `isWord_append` and
> `evalDsumEq_append_proven`, turning the direct-sum append judgment from a
> single smoke case into a general theorem for valid finite R words.
> `R/Code/Check.lean` now exposes `CheckedTerm.WellFormed`,
> `Env.WellFormed`, `validateWord_ok_rank?`, and
> `checked_append_wellFormed`, giving the checker a theorem-backed
> compositional rank invariant. The full recursive `checkTerm_wellFormed`
> theorem remains a separate proof obligation.
>
> **v1.44 delta** since v1.43:
> `R/RWord.lean` now proves general parse/render round trips:
> `parseChars?_renderChars`, `parseString?_render`, `rank?_render`, and
> `parseAt?_render`. Rendered `R N` values therefore parse back at the same
> fixed rank by theorem, not just by executable examples. The same pass adds
> `parseChars?_append`, `parseString?_append`, `rank?_append`, and
> `parseAt?_eq_some_rank?`, so successful fixed-rank parses and valid word
> concatenation expose their rank facts directly.
>
> **v1.43 delta** since v1.42:
> `Wen/Analysis.lean` now names the whole-file Wen-to-R.Code demo check as
> `analyzeContent_demo_ledger_states`, proving the expected per-line ledger
> states for the sample source (`proven`, one `overclaims`, one `refuted`,
> then the remaining proven judgment checks). This makes the finite
> end-to-end demo citable without changing the claim boundary: it is still a
> concrete executable smoke theorem, not frontend soundness for arbitrary Wen
> files.
>
> **v1.42 delta** since v1.41:
> `R/JudgmentRequest.lean`, `R/Code/Judgment.lean`, and
> `Wen/ElabToRCode.lean` now promote their executable smoke checks from
> anonymous examples to named theorem hooks: direct-sum proof, prefix
> overclaiming, visible/residual conjunction, R.Code scope reuse, and the
> minimal Wen-to-R.Code lowering demos. These are finite executable
> boundary theorems, not soundness for the whole Wen frontend or every
> runtime judgment.
>
> **v1.41 delta** since v1.40:
> `Order/HeytingBimorphism.lean` now proves the full Boolean
> sub-bimorphism classification as `Bool_isSubBimorphism_iff`: a binary
> operation `Bool → Bool → Bool` preserves `⊔` and `⊓` separately iff it is
> one of `inf2`, `sup2`, `proj1`, `proj2`, `constBot`, or `constTop`.
> The proof is a local truth-table/monotonicity argument, not an imported
> finite-distributive-lattice Birkhoff theorem, and it does not generalize
> the classification to arbitrary Heyting algebras.
>
> **v1.41 delta** since v1.40:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `FinHilbCoordinateKroneckerMorphismBoundary`, proving that arbitrary
> finite-index coordinate matrix morphisms tensor by Kronecker product between
> product-indexed coordinate Hilbert objects, with identity, composition, and
> Hilbert-adjoint compatibility. `SemanticWitnessFrontier`,
> `FullGUTNativeFrontier`, and `FullGUTFrontier` forward this boundary through
> direct accessors. This is a finite-coordinate matrix boundary, not a bundled
> `FdHilb` monoidal category, Hilbert tensor-product functor, or dagger-SMCC.
>
> **v1.40 delta** since v1.39:
> `Doctrine/FullGUTT5Frontier.lean` now exposes direct accessors for the
> canonical finite-field all-split T5 branch
> (`current_R_T5_canonical_field_all_split`) and the raw-core T5 boundary
> (`current_R_T5_raw_core_successor_and_gated_direct_sum`): raw
> `P1P7_Core` gives successor coherence, while arbitrary all-split coherent
> T5 remains gated by an explicit direct-sum structural witness.
> `Doctrine/FullGUTFrontier.lean` forwards the same boundary at the combined
> frontier, and `R/ClaimZ.lean` adds
> `D6ExactForD5.all_routes_refuted_of_D5`, a projection from exact D6 plus
> a proved D5 claim to refutation of all three D6 routes.
> `Doctrine/Instance/HilbertEnriched.lean` also exposes scalar transport for
> coordinate Hilbert maps and the R-side projective additive law
> `rToHilbEnd_projective_add_smul`, forwarded by `SemanticWitnessFrontier` as
> a scalar/projective witness rather than strict additive composition.  This
> is still not raw arbitrary all-split T5, global D6 exhaustiveness, or full
> `FdHilb`.
>
> **v1.39 delta** since v1.38:
> `Doctrine/Instance/HeytingNative.lean` now exposes
> `HomPresentation.mor_map_eval_le` and `mor_map_curry_iff`, direct native
> transport lemmas for the posetal meet/implication closed laws.
> `Order/HeytingBimorphism.lean` proves
> `himp2_not_isSubBimorphism_Bool`, making explicit that Boolean implication
> is an internal hom in the preorder sense, not a binary lattice
> sub-bimorphism.  `Doctrine/Instance/HilbertEnriched.lean` now also proves
> self-adjointness for PauliBase, PauliN, and R-side finite-Hilbert
> endomorphisms.  `SemanticWitnessFrontier` forwards these as scoped native
> witness accessors without claiming bundled `HeytAlg` CCC or full `FdHilb`.
>
> **v1.38 delta** since v1.37:
> `Doctrine/Instance/SemanticWitnessFrontier.lean` now exposes the Hilbert
> adjoint laws directly as `SemanticWitnessFrontier.matrix_hilbert_adjoint`
> and `SemanticWitnessFrontier.phased_pauli_hilbert_adjoint`.  This is an
> accessor/API closure for the already proved coordinate stabilizer Hilbert
> adjoint facts; it does not upgrade the claim to full `FdHilb`.
>
> **v1.37 delta** since v1.36:
> `Doctrine/Instance/HilbertEnriched.lean` now proves
> `matrixHilbLinearMap_adjoint_conjTranspose`, identifying the Hilbert
> adjoint of a coordinate matrix action with conjugate transpose, and
> `phasedPauliNHilbEnd_adjoint`, identifying the phase-bearing Pauli dagger
> with the finite-Hilbert adjoint.  The action packages and
> `StabilizerHilbertCoherenceBoundary` now carry these adjoint laws.  This is
> still scoped coordinate stabilizer/Hilbert semantics, not a bundled
> `FdHilb` dagger-SMCC theorem.
>
> **v1.36 delta** since v1.35:
> `Order/FrmClosed.lean` now exposes the represented exponential evaluation
> morphism `FrmExponentialData.eval` and proves
> `frmTensorClosedHomEquiv_of_exponentialData_symm_eq_tensor_eval`: uncurrying
> a supplied exponential map is `(k ⊗ id) ≫ eval`.  This is the expected
> closed-category equation for explicitly supplied `FrmExponentialData`, still
> below constructing arbitrary exponential frames or `MonoidalClosed Frm`.
>
> **v1.35 delta** since v1.34:
> `Order/HeytingInternalHom.lean` now exposes reusable `HeytingHom` transport
> lemmas for the posetal closed structure:
> `HeytingPosetalClosed.map_hom_eval_le` and
> `HeytingPosetalClosed.map_hom_curry_iff`.  The indexed bundled-`HeytAlg`
> transport lemmas in `HeytingCategoryNative.lean` now call this shared API.
> This is still the thin/preorder Heyting closure, not a bundled `HeytAlg`
> cartesian-closed category theorem.
>
> **v1.34 delta** since v1.33:
> `Enriched/Cotensor.lean` no longer says the `V = Type` cotensor instance is
> already installed.  The header now matches the code: `TypeCotensorStatementData`
> is supplied data, and the file exposes `typeCotensor_functionSpace` and
> `typeCotensor_universal` as direct accessors for that supplied package.
>
> **v1.33 delta** since v1.32:
> `Enriched/Power.lean` removes the obsolete carrier-only reverse Power
> accessors (`monad_induces_theory_statement` and
> `comparison_monad_induces_theory_carrier`).  `FullGUTEnrichedFrontier`
> now forwards only the structured supplied package
> `comparison_monad_induces_theory_package`, so the reverse Power boundary no
> longer exposes a bare `Nonempty (Type u)` surface.
>
> **v1.32 delta** since v1.31:
> `Doctrine/EnrichedLawvereTheory.lean` now exposes the skeletal
> `FreeVCategory` generator and arity data as explicit definitions
> (`FreeVCategory.enrichedLawvereTheorySig` and
> `FreeVCategory.enrichedAritySkeleton`) instead of typeclass instances.
> Even after a client supplies ordinary/enriched category structure on the
> object skeleton, class search no longer treats that skeleton as canonical
> enriched Lawvere-theory data.
>
> **v1.31 delta** since v1.30:
> `Enriched/Weighted.lean` now states its weight boundary as an object-level
> skeleton only: `VWeight V J` carries `J → V` data and does not pretend to
> include enriched functoriality.  The file adds object-level extensionality,
> the constant-weight object projection, and the selected weighted-limit object
> projection.  Full V-functorial weights and the real weighted-limit universal
> property remain supplied/future enriched infrastructure.
>
> **v1.30 delta** since v1.29:
> `Doctrine/EnrichedLawvereTheory.lean` strengthens `MonadTheoryData`: the
> supplied reverse Power construction now carries the reconstructed carrier's
> ordinary `Category`, `EnrichedOrdinaryCategory`, and
> `EnrichedLawvereTheory` structures, not only a bare carrier type.
> `Enriched/Power.lean` exposes `comparison_monad_induces_theory_package`,
> and `FullGUTEnrichedFrontier` forwards it.  This is still supplied data, but
> the missing reverse-Power obligations are no longer hidden behind
> `Nonempty (Type u)`.
>
> **v1.29 delta** since v1.28:
> `R/ClaimZ.lean` now exposes `D6ComponentCoverageForD5.of_D5_holds`,
> making explicit that component coverage is vacuous for a scoped D5 package
> that is already proved. `Doctrine/FullGUTFrontier.lean` records that the
> current HoTT/ETCS/SDG predicates are exactly the present route-2 synthetic
> audit predicates for the concrete F₂ D6 bundle.  `Instance/TopologicalNativeLocale.lean`
> and `Instance/SemanticWitnessFrontier.lean` now expose the concrete right
> and left currying equivalences and naturality laws for the unit frame
> exponential `[𝟙, Z] = Z`.  These are scoped audit/native-boundary closures,
> not global D6 exhaustiveness or `MonoidalClosed Frm`.
>
> **v1.28 delta** since v1.27:
> `Doctrine/EnrichedLawvereTheory.lean` no longer installs an automatic
> ordinary `Category` instance for the skeletal `FreeVCategory V`.  Downstream
> instances that use `FreeVCategory` as an ordinary/enriched category must now
> supply the real `Category` / `EnrichedOrdinaryCategory` data explicitly.  This
> removes a globally available placeholder while preserving the arity/generator
> skeleton.
>
> **v1.27 delta** since v1.26:
> `Doctrine/FullGUTEnrichedFrontier.lean` now also exposes enriched
> model-morphism identity, composition, underlying transformation projection,
> extensionality, and unit/associativity laws through
> `CurrentEnrichedLawvereFullGUTFrontier`.  This packages the existing
> `EnrichedModelMorphism` category boundary for downstream certificates; it is
> not a 2-categorical enriched-theory theorem or a V-natural equivalence of all
> models.
>
> **v1.26 delta** since v1.25:
> `Doctrine/FullGUTLawvereFrontier.lean` now packages the ordinary
> Lawvere-theory frontier as `CurrentLawvereTheoryFullGUTFrontier`, exposing
> chosen-power projections, theory-morphism/model-pullback laws, the free
> term-category construction, and supplied Lawvere/finitary-monad comparison
> accessors without claiming the constructive equivalence.  `FullGUTFrontier`
> carries this package.  `FullGUTEnrichedFrontier` also exposes the supplied
> free/forgetful object laws, weighted-limit comparison laws, filtered
> preservation projection, enriched-preservation-from-forgetful-iso, symmetric
> tensor boundary, and GUT-C supplied universal-sayability boundary.  These are
> accessor closures over explicit data, not automatic Power 1999 semantics.
>
> **v1.25 delta** since v1.24:
> `Doctrine/FullGUTEnrichedFrontier.lean` now exposes enriched theory-morphism
> functor projection and extensionality laws in
> `CurrentEnrichedLawvereFullGUTFrontier`: `enriched_theory_hom_id_functor`,
> `enriched_theory_hom_comp_functor`, and `enriched_theory_hom_ext`.  This
> closes a reusable accessor layer for the existing morphism API; it is not a
> bundled category of enriched theories or a Power 1999 semantic theorem.
>
> **v1.24 delta** since v1.23:
> `Doctrine/FullGUTFrontier.lean` now flattens the remaining R/T5 frontier
> accessors: `current_full_gut_R_T5_field_ringEquiv_by_charClass`,
> `current_full_gut_R_T5_field_coherent_from_direct_sum`, and
> `current_full_gut_R_T5_f2_side_obligations`.  These forward the existing
> char-class ring-equivalence dispatcher, supplied-direct-sum field coherent
> bridge, and scoped F₂ side-obligation package; they do not derive arbitrary
> non-canonical coherence or ring data from raw satisfier hypotheses.
>
> **v1.23 delta** since v1.22:
> `Doctrine/FullGUTEnrichedFrontier.lean` now exposes the supplied enriched
> free-model and ordinary free/forgetful adjunction boundary as fields of
> `CurrentEnrichedLawvereFullGUTFrontier`: `supplied_free_v_models`,
> `supplied_free_forgetful_adjunction`, and
> `free_forgetful_forgetful_free_obj`.  These fields forward explicit
> `HasFreeVModels` / `FreeForgetfulAdjunctionData`; they do not construct
> free V-models, prove an enriched adjunction, or close Power 1999.
>
> **v1.22 delta** since v1.21:
> `Doctrine/FullGUTFrontier.lean` now exposes the algebraic coherent all-split
> T5 bridge at the combined frontier as
> `CurrentFullGUTFrontier.R_T5_algebraic_coherent_from_direct_sum` and the
> direct accessor `current_full_gut_R_T5_algebraic_coherent_from_direct_sum`.
> This forwards the already-closed `T5AlgebraicCoherentDirectSumGUTBPackage`
> construction from a supplied direct-sum structural witness; it still does
> not derive that witness or the non-canonical finite-field ring/coherence
> data from raw satisfier hypotheses.
>
> **v1.21 delta** since v1.20:
> `Doctrine/FullGUT.lean` now proves
> `current_scoped_D6_component_coverage_for_D5` and reconstructs exactness as
> `current_scoped_D6_exact_from_component_coverage`.  `FullGUTFrontier` exposes
> both fields in the scoped D6 audit certificate and headline frontier.  This
> makes the current D5/F₂-D6 exactness auditable through the component-coverage
> interface, still only for the current scoped pair.
>
> **v1.20 delta** since v1.19:
> `Doctrine/FullGUTFrontier.lean` now exposes
> `D6_exact_from_component_coverage` as a field of `CurrentFullGUTFrontier`.
> Downstream users can construct exact scoped D5/D6 certificates from matched
> soundness plus componentwise D5-failure coverage without reaching back into
> lower-level ClaimZ plumbing.  This is still an interface theorem, not global
> D6 exhaustiveness.
>
> **v1.19 delta** since v1.18:
> `Order/FrmClosed.lean` now constructs the concrete unit-exponential data
> `frmTensorUnitExponentialData`, and `Order/FrmClosedBraided.lean` packages
> it as `frmTensorUnitRepresentedClosedBoundary`.  `TopologicalNativeLocale`
> and `SemanticWitnessFrontier` expose the corresponding
> `TopologicalNativeLocaleUnitClosedWitness`.  This closes the canonical
> `[𝟙, Z] = Z` represented `Frm` case while leaving non-unit exponentials and
> full `MonoidalClosed Frm` open.
>
> **v1.18 delta** since v1.17:
> `R/ClaimZ.lean` now adds
> `D6ExactForD5.of_sound_and_component_coverage`, the direct constructor
> from matched D6 soundness plus componentwise D5-failure coverage to exact
> D5/D6 equivalence.  This is still a scoped pair theorem; it removes
> boilerplate without asserting global D6 exhaustiveness.
> `Doctrine/EnrichedLawvereTheory.lean` also adds
> `freeForgetfulAdjunction_forgetful_free_obj`, composing the supplied
> free-model and generator-evaluation object laws into one accessor while
> staying below an automatically constructed enriched adjunction.
>
> **v1.17 delta** since v1.16:
> `Doctrine/Instance/HilbertEnriched.lean` now proves
> `rToHilbEnd_tensor_append` and includes it in `RToHilbertTensorBoundary`.
> The stabilizer R-to-Hilbert tensor boundary therefore records both the
> matrix-level append theorem and the represented finite-Hilbert endomorphism
> theorem.  This remains a coordinate Pauli/stabilizer result, not a full
> `FdHilb` monoidal functor.
>
> **v1.16 delta** since v1.15:
> `R/ClaimZ.lean` now defines `D6ComponentCoverageForD5` and proves
> `D6ExhaustiveForD5.of_component_coverage`.  This is the theorem-grade
> D6 coverage interface: if every named D5 conjunct failure is routed to a
> selected D6 falsification bundle, the matched `¬D5_holds -> D6_holds`
> exhaustive direction follows automatically.  It is still pair-scoped
> coverage, not unrestricted global D6 exhaustiveness.
>
> **v1.15 delta** since v1.14:
> `R/UniquenessAlgebraic.lean` now names
> `T5AlgebraicCoherentDirectSumGUTBPackage` and proves
> `T5_algebraic_coherent_GUT_B_package_of_direct_sum`.  This bridges the
> algebraic carrier-4 matrix-ring package with the generic coherent-core
> all-split package under a supplied direct-sum witness.  `FullGUTT5Frontier`
> exposes the bridge as `algebraic_coherent_from_direct_sum` plus a direct
> accessor.  The theorem remains honestly structure-gated; it does not derive
> all-split coherence from raw algebraic data.
>
> **v1.14 delta** since v1.13:
> `UniversalFormalSubstrateCertificate` now exposes the finite/stream
> formal-embedding and formal-isomorphism transport theorems as certificate
> fields.  Downstream users of `claim_z_universal_formal_substrate` therefore
> get the R-realisation reuse rules directly from the headline package.
>
> **v1.13 delta** since v1.12:
> `Doctrine/FullGUT.lean` now adds `FormalTranslation.Embedding`, proves
> identity/composition closure for embeddings, and proves finite-layer and
> stream-layer faithful R-realisation pullback along embedding translations.
> This is the theorem-grade subpresentation/subtheory transport rule: if a
> target formal presentation is already faithfully realised in R, an injective
> structure-preserving source translation inherits a faithful R-realisation.
>
> **v1.12 delta** since v1.11:
> `Doctrine/FullGUT.lean` now defines `FormalPresentationIso` and proves
> finite-layer and stream-layer faithful R-realisation transport across such
> isomorphisms, including `faithfulRRealisation_iff` and
> `faithfulRStreamRealisation_iff`.  This closes a reusable semantic-witness
> transport API: once a presentation has a faithful R-realisation, any
> isomorphic formal presentation inherits it without redoing the encoding.
>
> **v1.11 delta** since v1.10:
> `Doctrine/FullGUT.lean` now defines
> `categoryPresentationMor.map`, proves its identity/composition laws, defines
> `categoryFormalTranslation`, and proves
> `category_functor_finite_encodable_T1T3_stack`.  Finite and encodable small
> category functors now enter the same finite/stream T1+T3 code-natural,
> identity, and composition stack as arbitrary formal translations.  This is a
> syntactic/functorial R-code theorem; intended semantic preservation remains
> the separate native witness layer.
>
> **v1.10 delta** since v1.09:
> `Doctrine/FullGUT.lean` now adds
> `FiniteEncodableFormalPresentationT1T3Stack` and
> `finite_encodable_formal_presentation_T1T3_stack`, a pointwise certificate
> bundling faithful finite R-realisation, faithful stream R-realisation,
> finite/stream translation naturality, identity, and composition for a
> composable pair of formal translations whose presentations are both finite
> and encodable.  This is a packaging theorem over the existing T1/T3 stack;
> it does not construct intended semantic preservation beyond D1 data.
>
> **v1.09 delta** since v1.08:
> The current scoped frontier now has named boundary certificates instead of
> only nested record fields.  `R/UniquenessGeneral.lean` names the raw-core
> successor package as `T5SuccessorGUTBPackage` and exposes
> `T5_raw_core_successor_and_gated_direct_sum`, while
> `R/UniquenessGeneralField.lean` exposes
> `T5_field_canonical_and_gated_noncanonical_boundary`.  `FullGUTFrontier.lean`
> adds `CurrentScopedD6AuditCertificate`, bundling exactness, soundness,
> exhaustiveness, route refutation, and recorded-candidate refutation for the
> current scoped F₂ D5/D6 pair.  Native semantic modules also add named
> certificates: `HeytAlgCategoricalBoundary`,
> `NQubitMatrixTensorCoherenceBoundary`,
> `RToHilbertSubstrateActionBoundary`,
> `FrmRepresentedClosedBoundary`, and
> `TopologicalNativeLocaleRepresentedClosedWitness`, with
> `SemanticWitnessFrontier` exposing them.  These are scoped/certificate
> closures; they do not construct arbitrary semantic-preservation witnesses,
> a bundled `HeytAlg` CCC, full `FdHilb`, `MonoidalClosed Frm`, global D6, or
> raw arbitrary all-split T5.
>
> **v1.08 delta** since v1.07:
> Frontier/API accessors were flattened for the next automatic-witness pass.
> `FullGUTT5Frontier.lean` adds direct theorem names
> `current_R_T5_canonical_field_coherent_all_split` and
> `current_R_T5_field_ringEquiv_by_charClass`.
> `SemanticWitnessFrontier.lean` exposes direct native witness fields for the
> all-`n` Hilbert bridge, single-qubit matrix dagger FullGUT, concrete
> n-qubit matrix tensor split/associativity, and the native topological frame
> package.  On the enriched side, `Cotensor.lean` proves
> `cotensorLift_coev_precomp`, `Finitary.lean` exposes
> `filteredConicalColimitPreservation_holds`, `EnrichedLawvereTheory.lean`
> exposes free/forgetful object compatibility accessors, and `Power.lean`
> exposes Power-facing round-trip-law accessors.  These are all local
> accessor/coherence closures; they do not construct full `FdHilb`,
> `MonoidalClosed Frm`, arbitrary semantic witnesses, or Power 1999.
>
> **v1.07 delta** since v1.06:
> `Doctrine/FullGUT.lean` now exposes the scoped D5/F₂-D6 exactness
> projections directly as `current_scoped_D6_sound_for_D5` and
> `current_scoped_D6_exhaustive_for_D5`, and records them in
> `CurrentFullGUTBoundaryCertificate`.  `R/UniquenessGeneralField.lean` adds
> `T5_field_coherent_GUT_B_package_canonical_auto`, producing the canonical
> finite-field direct-sum witness together with the coherent field GUT-B
> package.  `FullGUTT5Frontier` and `FullGUTFrontier` expose that canonical
> coherent finite-field branch.  These are scoped/canonical closures; they do
> not prove global D6 exhaustiveness or derive coherence for arbitrary
> non-canonical finite-field satisfiers.
>
> **v1.06 delta** since v1.05:
> The enriched supplied-data layer now exposes more of the proof fields that
> were already required. `Cotensor.lean` adds the coevaluation round-trip
> simp theorems `cotensorEquiv_id_eq_cotensorCoev` and
> `cotensorLift_cotensorCoev`; `Weighted.lean` exposes the supplied weighted
> universal-property and comparison proofs through `weightedLimit_universal`,
> `cotensor_terminal_comparison_holds`, and
> `conical_constant_comparison_holds`; `EnrichedLawvereTheory.lean` exposes
> the supplied Power comparison round-trip proofs as
> `comparison_theory_roundTrip_holds` and
> `comparison_monad_roundTrip_holds`, and `FullGUTEnrichedFrontier` records
> those accessors.  These are all accessor/API closures over explicit data,
> not constructions of weighted limits, cotensors, or Power 1999.
>
> **v1.05 delta** since v1.04:
> `Foundation/Enriched/Cotensor.lean` now exposes the supplied cotensor
> universal-property naturality as `cotensorEquiv_naturality`, and derives
> `cotensorLift_naturality` for precomposition in the ordinary source object.
> This is a real API theorem from the `HasCotensor` data already required by
> the interface; it still does not construct cotensors for `Type`, `FdHilb`,
> or arbitrary enriched categories, and it is not the Power 1999 theorem.
>
> **v1.04 delta** since v1.03:
> `Foundation/Order/FrmBraided.lean` now proves the standard two-variable
> Joyal-Tierney braiding naturality square `frmBraiding_naturality`, and
> `TopologicalNativeLocaleWitness` records it directly.  This packages the
> ordinary braided naturality law from the existing concrete pairing proof; it
> does not construct exponential frames or `MonoidalClosed Frm`.
> `Foundation/Doctrine/EnrichedLawvereTheory.lean` also gives
> `EnrichedModelMorphism` explicit identity/composition projections and local
> `id_comp`, `comp_id`, and `comp_assoc` laws, then reuses them in the model
> category instance.  This is model-morphism API closure, not the Power 1999
> V-natural semantic theorem.
>
> **v1.03 delta** since v1.02:
> The ordinary Lawvere-theory layer now has theorem-backed underlying-functor
> laws for theory morphism identity/composition:
> `LawvereTheoryHom.comp_id_functor`, `id_comp_functor`, and
> `comp_assoc_functor`.  Model restriction of scalars also exposes
> `Model.pullback_id_functor` and `Model.pullback_comp_functor`.
> `CurrentFullGUTFrontier` now provides direct finite/stream enriched-Lawvere
> bridge accessors, rather than forcing downstream code to unpack the nested
> enriched frontier, and direct R/T5 accessors for the canonical finite-field
> all-split package plus the supplied-direct-sum coherent bridge.  These are
> still ordinary-D1 representation bridges and structure-gated T5 accessors,
> not enriched semantic-preservation, Power 1999, or raw-core all-split T5.
>
> **v1.02 delta** since v1.01:
> The enriched Lawvere theory morphism API now proves the expected local
> identity and associativity laws:
> `EnrichedLawvereTheoryHom.comp_id`,
> `EnrichedLawvereTheoryHom.id_comp`, and
> `EnrichedLawvereTheoryHom.comp_assoc`.  The enriched frontier exposes these
> laws alongside the constructors.  We still intentionally avoid a bundled
> category instance for enriched theories until the object bundling is worth
> adding.
>
> **v1.01 delta** since v1.00:
> `Foundation/Doctrine/EnrichedLawvereTheory.lean` now gives
> `EnrichedLawvereTheoryHom` a small 1-morphism API: finite-product
> preservation can be transported across the underlying `EnrichedFunctor.forget`
> isomorphisms, and enriched theory morphisms have identity, composition, and
> extensionality lemmas. `FullGUTEnrichedFrontier` exposes the identity and
> composition constructors as frontier fields. This is deliberately the
> composable morphism layer only; it is not a full `Category` instance for
> enriched theories, not the Power 1999 equivalence, and not automatic
> V-natural semantic preservation.
>
> **v1.00 delta** since v0.99:
> `Foundation/Order/FrmClosedBraided.lean` now derives a braided represented
> exponential equivalence from supplied `FrmExponentialData`:
> `frmTensorClosedHomEquiv_of_exponentialData_braiding`, plus apply and
> source-naturality laws.  `TopologicalNativeLocaleWitness` records these
> fields, so the locale/frame branch now says exactly how represented currying
> interacts with the concrete Joyal-Tierney braiding.  This still assumes
> supplied exponential data; it does not construct exponential frames or
> register `MonoidalClosed Frm`.
> `FullGUTT5Frontier` now exposes the already-proved arbitrary-δ coherent T5
> bridge from a supplied `DirectSumStructuralIso`, and `FullGUTFrontier`
> exposes the current F₂ D6 recorded-candidate audit.  These are frontier
> accessors, not automatic all-split coherence or global D6 exhaustiveness.
>
> **v0.97 delta** since v0.96:
> The scoped native frontier now exposes another layer of accessor-grade
> evidence without strengthening the global claim.  Indexed bundled `HeytAlg`
> families have objectwise posetal evaluation/currying transport lemmas;
> `SemanticWitnessFrontier` carries the indexed posetal-closed package and the
> pure Heyting closed end-action.  `HilbertEnriched.lean` adds direct
> `RToHilbertEndAction` and `RToHilbertTensorBoundary` packages, recording
> involution/projective-addition and tensor-append compatibility for the
> R-to-Hilbert Pauli bridge.  `EnrichedLawvereTheory.lean` exposes supplied
> free-model/free-forgetful accessors, while
> `FullGUTEnrichedFrontier.lean` exposes supplied Power comparison,
> theory-to-monad, and Type arity-skeleton frontiers.  These are still scoped
> witness accessors, not automatic all-semantics construction.
>
> **v0.98 delta** since v0.97:
> The native semantic frontier now also carries the `DiamondH4` Heyting anchor
> package: existence/uniqueness of the four-element non-Boolean Heyting
> algebra, its linear-chain order iso, implication agreement, refined P3
> sub-bimorphism frontier, and the strong Heyting-bilinear evaluation
> obstruction.  The enriched frontier also exposes the supplied-data reverse
> Power accessor from a finitary V-monad to its reconstructed theory carrier.
> These tighten the audit surface while still stopping below bundled
> `HeytAlg` CCC and the Power 1999 construction theorem.
>
> **v0.99 delta** since v0.98:
> `Doctrine/Instance/HilbertEnriched.lean` now exposes
> `StabilizerHilbertCoherenceBoundary`, a dedicated package for the current
> coordinate finite-Hilbert stabilizer facts: matrix identity/composition,
> phase-bearing Pauli composition/dagger/tensor, R-to-Hilbert projective
> action, Pauli-Hilbert tensor coherence, and generic/concrete n-qubit
> operator bridges.  `SemanticWitnessFrontier` cites this package directly.
> This is a cleaner API for the stabilizer/Hilbert boundary; it is still not
> a bundled `FdHilb`, dagger-SMCC, or global monoidal functor theorem.
>
> **v0.96 delta** since v0.95:
> The native/frontier packages now expose another set of already-proved
> scoped laws: bundled Heyting end-actions preserve `⊥` and `⊤`; the locale
> witness records the generic `frameCoprod` JT universal property and
> tensor-hom extensionality; `RToHilbertQuantumWitness` records projective
> R-addition as Hilbert matrix multiplication up to retained Pauli phase; the
> semantic frontier exposes Pauli-Hilbert tensor coherence and n-qubit tensor
> units; the R/T5 frontier carries `T5_A_full_side_obligations`; and the
> FullGUT boundary/frontier carry direct refutation of the current concrete F₂
> D6 bundle. These are scoped witness/aggregation upgrades, not global D6,
> raw-core all-split T5, full `FdHilb`, or `MonoidalClosed Frm`.
> `CurrentRT5Frontier` also exposes the existing
> `T5_field_ringEquiv_by_charClass` dispatcher; that dispatcher still delegates
> to supplied `p7b_ring_equiv` data for arbitrary satisfiers.
>
> **v0.95 delta** since v0.94:
> `Doctrine/Instance/TopologicalNativeLocale.lean` now exposes the already
> proved concrete `Frm` braiding hexagons and symmetry equations directly in
> `TopologicalNativeLocaleWitness`, and records the represented
> `FrmExponentialData` currying bridge plus its source naturality as supplied
> data fields. This tightens the native locale/frame witness without claiming
> construction of exponential frame objects or `MonoidalClosed Frm`.
>
> **v0.94 delta** since v0.93:
> `Doctrine/Instance/HeytingCategoryNative.lean` now proves that the bundled
> `HeytAlg` end-action transports the native posetal Heyting evaluation and
> currying laws (`HeytAlgPosetalClosedEndAction.map_eval_le` and
> `map_curry_iff`). This strengthens the positive native Heyting layer while
> preserving the proven obstruction to a global bundled `HeytAlg` exponential.
>
> **v0.93 delta** since v0.92:
> `Doctrine/Instance/SemanticWitnessFrontier.lean` now exposes the global
> retained-phase Pauli tensor/action package
> `PhasedPauliNHilbertTensorAction`, so the native witness frontier cites the
> tensor-append Hilbert action theorem already proved in `HilbertEnriched.lean`.
>
> **v0.92 delta** since v0.91:
> `FullGUT.lean` now stores route-by-route refutation of the current concrete
> F₂ D6 bundle in `CurrentFullGUTBoundaryCertificate`, and
> `FullGUTFrontier.lean` exposes the same field in `CurrentFullGUTFrontier`.
> This tightens the scoped D5/D6 audit trail without claiming global D6
> exhaustiveness.
>
> **v0.91 delta** since v0.90:
> `FullGUTEnrichedFrontier.lean` now packages the finite/stream enriched
> Lawvere ordinary-D1 bridge as `CurrentEnrichedLawvereFullGUTFrontier`, and
> `FullGUTFrontier.lean` includes it in `CurrentFullGUTFrontier`. The top
> frontier now exposes the scoped enriched representation bridge alongside the
> native semantic and T5 frontiers.
>
> **v0.90 delta** since v0.89:
> `Doctrine/FullGUTEnrichedFrontier.lean` now connects finite and encodable
> enriched Lawvere theories to the existing FullGUT representation stack via
> their underlying ordinary small-category presentation and chosen generator:
> `enriched_lawvere_finite_full_gut` and
> `enriched_lawvere_encodable_stream_full_gut`. This is a D1/representation
> bridge, not the missing Power 1999 all-enriched semantic theorem.
>
> **v0.89 delta** since v0.88:
> `Doctrine/Instance/HilbertEnriched.lean` now proves the retained-phase Pauli
> tensor-append action theorem `phasedPauliNHilbEnd_tensor`, packages it with
> composition and dagger in `PhasedPauliNHilbertTensorAction`, and strengthens
> `RToHilbertQuantumWitness` with the concrete signed commutation law. This
> closes the current coordinate stabilizer tensor/action boundary; it remains
> below a bundled full `FdHilb` dagger-SMCC or monoidal functor theorem.
>
> **v0.88 delta** since v0.87:
> `Wen/Embeddings/PhasedPauli.lean` now exports the matrix two-sided inverse
> lemmas `PhasedPauliN.toHilbert_mul_dagger` and
> `PhasedPauliN.toHilbert_dagger_mul`, and includes them in
> `PhasedPauliN.HilbertCoherence`. `HilbertEnriched.lean` now proves the
> finite-Hilbert endomorphism inverse law from those reusable matrix lemmas.
>
> **v0.87 delta** since v0.86:
> `Wen/Embeddings/PhasedPauli.lean` now equips phase-bearing Pauli words with
> dagger, proves `PhasedPauliN.toHilbert_dagger`, and proves
> `PhasedPauliN.toHilbert_mem_unitary`. `Doctrine/Instance/HilbertEnriched.lean`
> lifts this to finite-Hilbert endomorphisms via
> `phasedPauliNHilbEnd_dagger_comp` and records the law in
> `PhasedPauliNHilbertAction`. This closes the scoped retained-phase
> dagger/unitary action layer, still below bundled `FdHilb` dagger-SMCC.
>
> **v0.86 delta** since v0.85:
> `Enriched/Power.lean` exposes supplied-data Power accessors:
> `comparison_theory_induces_monad` and the structured reverse package
> `comparison_monad_induces_theory_package`. These project explicit comparison
> data; they do not construct the Power 1999 equivalence. `R/ClaimZ.lean` and
> `Doctrine/FullGUT.lean` also add soundness-only D6 route refutation:
> `D6SoundForD5.not_D6_of_D5`,
> `D6SoundForD5.all_routes_refuted_of_D5`, and
> `current_scoped_D6_all_routes_refuted_from_soundness`, keeping global D6
> exhaustiveness separate.
>
> **v0.85 delta** since v0.84:
> `Doctrine/Instance/HeytingCategoryNative.lean` now proves a concrete bundled
> `HeytAlg` cartesian-exponential obstruction:
> `no_bool_cartesian_exponent_representation` rules out even objectwise Hom-set
> representations `(C ⟶ E) ≃ (HeytAlg.of (C × Bool) ⟶ HeytAlg.of Bool)` for
> all `C`. `SemanticWitnessFrontier` exposes this as
> `heytalg_bool_cartesian_exponent_obstruction`, so the native frontier records
> both the positive posetal/indexed Heyting packages and the negative bundled
> cartesian-closure boundary.
>
> **v0.84 delta** since v0.83:
> `Doctrine/Instance/SemanticWitnessFrontier.lean` now exposes the retained-phase
> finite-Hilbert action through `SemanticWitnessFrontier.phased_pauli_hilbert_action`.
> The frontier package can therefore cite the exact `PhasedPauliN` endomorphism
> action on coordinate finite-Hilbert objects, while still keeping full `FdHilb`
> dagger-SMCC semantics open. `Foundation/Order/FrmClosed.lean` also adds
> represented exponential supplied data (`FrmExponentialData`) and
> `frmTensorClosedHomEquiv_of_exponentialData`, composing the existing
> tensor-to-JT-bilinear equivalence with an explicit currying equivalence
> without claiming `MonoidalClosed Frm`.
>
> **v0.83 delta** since v0.82:
> `Foundation/R/UniquenessGeneral.lean` now exposes the generic all-split T5
> bridge directly: `T5DirectSumGUTBPackage`,
> `T5_direct_sum_GUT_B_package`, `T5CoherentDirectSumGUTBPackage`, and
> `T5_coherent_GUT_B_package_of_direct_sum`.  A supplied
> `P1P7_Core.DirectSumStructuralIso` is converted into the coherent GUT-B
> package at the raw-core level. This does not derive arbitrary all-split
> coherence from raw `P1P7_Core`; it makes the exact required witness reusable.
>
> **v0.82 delta** since v0.81:
> `Doctrine/Instance/HilbertEnriched.lean` now proves coordinate finite-Hilbert
> matrix functoriality: identity matrices act as identity morphisms and matrix
> multiplication is categorical composition for `matrixHilbMap`. The same file
> also lifts retained-phase Pauli words to concrete finite-Hilbert endomorphisms
> via `phasedPauliNHilbEnd`, with composition represented by morphism
> composition. This strengthens the scoped stabilizer Hilbert witness; it still
> does not claim full `FdHilb` dagger-SMCC semantics.
>
> **v0.81 delta** since v0.80:
> `Atlas/Yi/Classical/Diagonal/GodelLi.lean` no longer extends the trust base
> with `axiom kleene_recursion_axiom`. The classical Yi diagonal wrappers now
> take an explicit `KleeneInverter` witness, and `Modern/DaoLi.lean` / the wall
> citation registry follow that conditional theorem shape. The canonical
> R-family diagonal anchor remains the axiom-free R-side file using
> `KleeneInverter` as an explicit hypothesis.
>
> **v0.80 delta** since v0.79:
> `Modern/KolmogorovExt.lean` removes the remaining six `True` anchors by
> exposing actual Mathlib theorem shapes for Markov's inequality, the strong
> law of large numbers, the one-dimensional central limit theorem, monotone
> convergence, dominated convergence, and Fatou's lemma.
>
> **v0.79 delta** since v0.78:
> ClaimZ/R audit cleanup removes three more vacuous tails:
> `ClaimZ/Analytic/P1.lean` now makes `D1_implies_P1_exists` return the
> actual P1 conclusion; `R/D6_Tests.lean` replaces candidate `∧ True`
> predicates with route-tagged witnesses; `Wen/MetaInterp/Universal.lean`
> drops `∧ True` from its semantic frontier summaries.
>
> **v0.78 delta** since v0.77:
> `Doctrine/Instance/Quantum.lean` replaces the legacy Hilbert/Pauli
> `∃ _, True` witnesses with named concrete maps and `Nonempty` witnesses:
> `P7b_quantum_anchor2`, `pauliToHilbert`, and `rToHilbert`. This removes
> vacuous tails from the quantum consistency anchors while keeping the full
> `FdHilb` / algebra-surjectivity theorem open.
>
> **v0.77 delta** since v0.76:
> `Hierarchy/ZoneClassifier/WallCitations.lean` changes the citation sentinel
> from a theorem returning `True` to a `PUnit` registry definition that still
> references every cited theorem. Broken citations still fail compilation, but
> the file no longer contributes a vacuous theorem.
>
> **v0.76 delta** since v0.75:
> `Modern/KolmogorovExt.lean` replaces eight measure/probability anchor
> placeholders with concrete Mathlib-backed objects or theorems: Dirac,
> counting, and Lebesgue measures; indicator measurability; event
> independence as the intersection/product equivalence; conditional
> probability as scaled restriction; the Bayes cross-product law; and the
> DaYan counting measure. Markov/LLN/CLT/MCT/DCT/Fatou remain explicit future
> anchors.
>
> **v0.75 delta** since v0.74:
> `EnrichedLawvereTheory.lean` strengthens the compatibility arity helper
> from a bare `∃ n, True` index witness to an iso-carrying
> `∃ n, Nonempty (X ≅ arityObj V T n)` witness, and adds `arityIso` for the
> chosen ordinary isomorphism. This removes a vacuous arity theorem without
> claiming the full Power-style enriched universal-sayability theorem.
>
> **v0.74 delta** since v0.73:
> `HeytingNative.lean` adds the bare native Heyting closed FullGUT packages
> `FiniteClosedFullGUT` and `EncodableClosedStreamFullGUT`, bundling the
> finite/stream native Heyting FullGUT witnesses with the already-proved
> posetal meet/implication closed structure. `SemanticWitnessFrontier` exposes
> these through `finite_heytalg_closed` and `encodable_heytalg_closed`.
>
> **v0.73 delta** since v0.72:
> `Foundation/Order/FrmClosedBraided.lean` adds
> `FrmJTBilin.swap_postcomp` and `FrmJTBilin.swap_precomp`, and extends
> `FrmJTBilinBraidedBoundary` with those swap-functoriality laws. This
> improves the existing braided tensor-bilinear boundary without claiming an
> exponential frame object or `MonoidalClosed Frm`.
>
> **v0.72 delta** since v0.71:
> `QuantumNativeDagger.lean` adds generic
> `NQubitMatrixDaggerFullGUT` / `NQubitMatrixOperatorFullGUT` packages for any
> finite native `NQubitPresentation`. `HilbertEnriched.lean` lifts this to
> `NQubitPresentationHilbertDaggerOperatorBridge`, and
> `SemanticWitnessFrontier.generic_n_qubit_hilbert_operator` exposes the
> automatic scoped witness family.
>
> **v0.71 delta** since v0.70:
> `CurrentFullGUTBoundaryCertificate` and downstream
> `CurrentFullGUTFrontier` now expose the scoped D5/F₂-D6 exactness package,
> the iff boundary, and the fixed-pair exhaustiveness direction directly.
> This is still scoped exactness, not global D6 exhaustiveness.
>
> **v0.70 delta** since v0.69:
> `T5FieldCoherentDirectSumGUTBPackage` names the coherent field all-split
> bridge, and `CurrentRT5Frontier.field_coherent_from_direct_sum` exposes it
> from the downstream R/T5 frontier package.
>
> **v0.69 delta** since v0.68:
> `Doctrine/FullGUT.lean` adds `current_scoped_D6_of_not_D5`, the scoped
> exhaustiveness direction for the current FullGUT D5/F₂-D6 pair.
> `Foundation/R/UniquenessGeneralField.lean` adds
> `T5_field_coherent_GUT_B_package_of_direct_sum`, packaging coherent field
> GUT-B consequences when the direct-sum structural witness is supplied.
>
> **v0.68 delta** since v0.67:
> `Foundation/Doctrine/EnrichedLawvereTheory.lean` removes the remaining
> enriched sketch `True` markers in the additive, linear, 2-Lawvere,
> symmetric-theory-tensor, and GUT-C universal-sayability sketch declarations.
> Each is now an explicit supplied-data boundary.
>
> **v0.67 delta** since v0.66:
> `Foundation/Doctrine/FullGUTFrontier.lean` adds the downstream
> `CurrentFullGUTFrontier` package, combining the native-semantic frontier with
> the R/T5 frontier while keeping both dependency-heavy branches out of
> `FullGUT.lean`.
>
> **v0.66 delta** since v0.65:
> `Foundation/Doctrine/FullGUTT5Frontier.lean` adds the downstream
> `CurrentRT5Frontier` package, combining `CurrentScopedT5` with the
> automatic-characteristic canonical finite-field all-split theorem without
> importing field/Wedderburn dependencies back into `FullGUT.lean`.
> `Foundation/R/D6_Tests.lean` adds
> `F2_recorded_candidates_do_not_falsify`, proving that the current
> HoTT/ETCS/SDG recorded candidate predicates do not apply to the concrete
> F₂ falsification bundle.
>
> **v0.65 delta** since v0.64:
> `UniquenessGeneralField.CharClass.char_neq_two` now stores the promised
> prime-characteristic proof, and `CharClass.ofFiniteField`,
> `T5_field_canonical_auto`, and
> `T5_field_direct_sum_GUT_B_package_canonical_auto` construct the canonical
> finite-field branch without an externally supplied `CharClass` tag.
>
> **v0.64 delta** since v0.63:
> `Foundation/R/UniquenessGeneralField.lean` adds
> `canonicalAlgebraicField`, `T5_field_canonical`, and
> `T5_field_direct_sum_GUT_B_package_canonical`, upgrading the canonical
> field-valued R-family from prime-field-specific all-split packages to any
> finite-carrier field once a `CharClass` tag is supplied. v0.65 removes that
> tag from the canonical finite-field theorem. This still does not
> derive ring/coherence data for arbitrary non-canonical satisfiers.
>
> **v0.63 delta** since v0.62:
> `Foundation/Doctrine/FullGUT.lean` adds the T6 self-articulation syntax
> package: `rFamilySelfPresentation`, `rFamilySelfPresentation_satisfiesD1`,
> `rFamilySelfPresentation_stream_realisation`, and
> `rFamily_self_articulation`. `CurrentScopedT6` now carries this explicit
> R-family self-syntax witness beside the F₂ self theorem and primary TypeCat
> package. This is a scoped syntax/stream theorem, not a semantic evaluator for
> every future native category.
>
> **v0.62 delta** since v0.61:
> `Foundation/Order/FrmClosedBraided.lean` adds
> `FrmJTBilinBraidedBoundary` / `frmJTBilin_braided_boundary`, proving that
> the tensor-to-JT-bilinear equivalence respects the concrete `Frm` braiding by
> variable swap. `TopologicalNativeLocaleWitness` now carries this symmetric
> tensor-boundary package without claiming an exponential frame object or
> `MonoidalClosed Frm`.
>
> **v0.61 delta** since v0.60:
> `Foundation/Doctrine/Instance/HilbertEnriched.lean` adds
> `RToHilbertQuantumWitness` / `r_to_hilbert_quantum_witness`, packaging the
> composed `R (2*n) → Mat_{2^n}(ℂ)` bridge as faithful and landing in
> self-adjoint unitaries. `SemanticWitnessFrontier` exposes this direct
> R-substrate quantum witness.
>
> **v0.60 delta** since v0.59:
> `Foundation/Order/FrmClosed.lean` packages the JT-bilinear functorial
> boundary as `FrmJTBilinFunctorialBoundary` /
> `frmJTBilin_functorial_boundary`, including identity, composition,
> interchange, and tensor-to-bilinear naturality laws. `TopologicalNativeLocale`
> now carries this package without claiming `MonoidalClosed Frm`.
>
> **v0.59 delta** since v0.58:
> `Foundation/Doctrine/Instance/HilbertEnriched.lean` adds the all-`n`
> finite-Hilbert bridge `NQubitQuantumToHilbertBridge` and
> `ConcreteNQubitHilbertDaggerOperatorBridge`, bundling faithful Pauli-word
> endomorphisms of `ℂ^(2^n)` with the existing phased stabilizer
> matrix-operator frontier. `SemanticWitnessFrontier` now exposes this family.
>
> **v0.58 delta** since v0.57:
> `Foundation/R/UniquenessGeneralField.lean` adds
> `T5_field_direct_sum_GUT_B_package_at_ZMod`, closing the canonical
> prime-field `ZMod p` branch at the all-split GUT-B level by reusing the
> identity direct-sum coherence of `canonicalRFamily`.
>
> **v0.57 delta** since v0.56:
> `Foundation/R/UniquenessAlgebraic.lean` and
> `UniquenessGeneralField.lean` add all-split direct-sum algebraic/field
> packages. These require a supplied `DirectSumStructuralIso` and combine it
> with cardinality recovery plus the carrier-4 matrix-ring witness. v0.64
> later generalizes the canonical all-split field package beyond `ZMod p`.
>
> **v0.56 delta** since v0.55:
> `Foundation/Doctrine/FullGUTNativeFrontier.lean` adds a downstream
> package combining `ConditionalAbsoluteFullGUT`,
> `UniversalFormalSubstrateCertificate`, `ScopedCoordinateFullGUT`, and
> `SemanticWitnessFrontier`. It preserves dependency direction and does not
> import native instance files back into `FullGUT.lean`.
>
> **v0.55 delta** since v0.54:
> `Foundation/Doctrine/Instance/SemanticWitnessFrontier.lean` adds
> `SemanticWitnessFrontier` and `semantic_witness_frontier_nonempty`,
> bundling only already-closed native witness fronts for Heyting,
> stabilizer quantum/Hilbert, and locale/frame semantics. It deliberately
> excludes open `HeytAlg` CCC, full `FdHilb`, exponential-frame, and
> Power/enriched all-semantics claims.
>
> **v0.54 delta** since v0.53:
> `Foundation/Doctrine/FullGUT.lean` adds
> `current_scoped_D6_refuted_from_exactness`, a scoped citation bridge
> deriving concrete F₂ D6 refutation from the proved scoped D5 package and
> `current_scoped_D6_exact_for_D5`. This is not global D6 exhaustiveness.
>
> **v0.53 delta** since v0.52:
> `Foundation/Doctrine/Instance/HilbertEnriched.lean` adds
> `ConcreteSingleQubitHilbertDaggerBridge`, bundling the concrete Pauli
> action on the qubit Hilbert object with the single-qubit
> matrix-level dagger/unitary witness. This is still below full `FdHilb`
> dagger-SMCC semantics.
>
> **v0.52 delta** since v0.51:
> `Foundation/R/UniquenessAlgebraic.lean` and
> `UniquenessGeneralField.lean` add successor packages for algebraic/field
> satisfiers, bundling raw-core successor coherence and cardinality recovery
> with the supplied carrier-4 matrix-ring witness. These packages do not
> derive the ring witness or all-split coherence from raw hypotheses.
>
> **v0.51 delta** since v0.50:
> `Foundation/Doctrine/FullGUT.lean` re-exports the raw-core successor
> theorem as `full_gut_successor_package_delta` and threads it through
> `UniversalFormalSubstrateCertificate` and `CurrentScopedT5`.
>
> **v0.50 delta** since v0.49:
> `Foundation/R/UniquenessGeneral.lean` adds
> `P1P7_Core.successor_GUT_B_package`, bundling the strongest structural
> theorem derivable from raw `P1P7_Core`: layerwise equivalence,
> successor-split coherence, and cardinality recovery. All-split direct-sum
> coherence remains exactly gated by `P1P7_CoherentCore`.
>
> **v0.49 delta** since v0.48:
> `Foundation/Doctrine/Instance/QuantumNativeDagger.lean` adds
> `ConcreteNQubitPhasedMonoidalMatrixOperatorFullGUT`, bundling phased
> stabilizer matrix-operator semantics with binary tensor splits and
> three-factor matrix associativity for nonempty qubit blocks. This remains
> a stabilizer matrix theorem, not a full `FdHilb` dagger-SMCC functor.
>
> **v0.48 delta** since v0.47:
> `Foundation/Doctrine/Instance/HeytingCategoryNative.lean` adds
> `IndexedPosetalClosedSemantics` and threads it through finite/encodable
> indexed bundled-`HeytAlg` FullGUT packages. This records per-object Heyting
> evaluation/currying for every indexed bundled algebra; it still does not
> claim a categorical exponential object or CCC structure for `HeytAlg`.
>
> **v0.47 delta** since v0.46:
> `Foundation/R/Distinction/Prop.lean` replaces the δ = Prop P3/P5b/P6/P7b
> `True := trivial` status notes with explicit `PropObligationStatus` tags.
> The file remains a status witness for the non-algebraic Prop branch, not an
> algebraic F₂ theorem.
>
> **v0.46 delta** since v0.45:
> `Foundation/Doctrine/Instance/SpectralZeta.lean` and
> `LSeriesSMCC.lean` no longer use `Prop := True` as research-conjecture
> statement sites. Connes-Weil positivity and the finer zeta/distinctness
> conjectures now require explicit supplied data records.
>
> **v0.45 delta** since v0.44:
> `Foundation/Doctrine/T_GUT.lean` removes the legacy
> `RealIso.coherent : Prop := True` compatibility field. `RealIso` is now
> exactly a carrier/component iso wrapper; non-vacuous structural, generator,
> and ops coherence remains in `CoherentCoreRealIso`,
> `FullCoherentCoreRealIso`, and `FullCoherentRealIso`.
>
> **v0.44 delta** since v0.43:
> `Foundation/Doctrine/Instance/Topological.lean` no longer proves the
> frame-vs-Heyting morphism-class differential by `True := trivial`; it now
> requires explicit `FrameVsHeytingMorphismDifferentialData`. The concrete
> strict-inclusion counterexample remains future category-theory plumbing.
>
> **v0.43 delta** since v0.42:
> `Foundation/Enriched/Cotensor.lean` replaces the remaining `V = Type`
> cotensor `True` statement with `TypeCotensorStatementData`, which requires
> an explicit function-space identification and universal-property proof. The
> real Type-as-enriched cotensor instance remains open.
>
> **v0.42 delta** since v0.41:
> `Foundation/Enriched/Weighted.lean`, `Monad.lean`, and `Finitary.lean` no
> longer hide their Phase 1.2-1.4 obligations behind load-bearing
> `True := trivial` fields or unconditional Type-specialisation statements.
> Weighted limits now carry explicit supplied universal-property data;
> enriched natural transformations, enriched monads, and finitary enriched
> monads now carry explicit supplied law/comparison data. The real weighted
> universal property, V-natural transformation calculus, Type-as-enriched
> monad comparison, and filtered-colimit preservation theorem remain open.
>
> **v0.41 delta** since v0.40:
> `Foundation/Doctrine/Instance/QuantumNativeDagger.lean` adds
> `ConcreteNQubitPhasedMatrixOperatorFullGUT` and
> `concrete_n_qubit_phased_matrix_operator_full_gut`, bundling the existing
> n-qubit matrix-operator FullGUT package with retained-phase Hilbert
> composition/tensor coherence from `PhasedPauliN`. This remains scoped to
> stabilizer matrix semantics, not full `FdHilb`.
>
> **v0.40 delta** since v0.39:
> `Foundation/Doctrine/Instance/HeytingCategoryNative.lean` adds
> `EncodableHomClosedStreamFullGUT` and
> `encodable_hom_closed_stream_full_gut_nonempty`, the stream-level analogue
> of the finite native Heyting-hom posetal-closed/end-action package. This is
> still scoped native Heyting semantics, not a bundled `HeytAlg` CCC theorem.
>
> **v0.39 delta** since v0.38:
> `Foundation/Doctrine/EnrichedLawvereTheory.lean` replaces
> `enriched_lawvere_iff_finitary_v_monad : True` with explicit
> `EnrichedLawvereFinitaryMonadComparisonData`. `Foundation/Enriched/Power.lean`
> now projects supplied `TheoryMonadData`, `MonadTheoryData`, and comparison
> data instead of returning `True` bridge statements. The real Power 1999
> construction and 2-equivalence remain open.
>
> **v0.38 delta** since v0.37:
> `Foundation/R/ClaimZ.lean` adds reusable exact-D6 corollaries:
> `D6ExactForD5.D6_of_not_D5`, `D6ExactForD5.not_D6_of_D5`, and
> `D6ExactForD5.of_D5_holds_and_D6_refuted`. `ClaimZF2.lean` specializes
> those to the concrete F₂ D5/D6 pair, and `Doctrine/FullGUT.lean` proves
> `current_scoped_D6_exact_for_D5` plus
> `current_scoped_D6_iff_not_D5` for the current scoped FullGUT D5 package.
> This is scoped exactness, not global D6 exhaustiveness.
>
> **v0.37 delta** since v0.36:
> `Foundation/R/UniquenessGeneral.lean` adds
> `P1P7_CoherentCore.coherent_GUT_B_package`, bundling the coherent GUT-B
> consequences in one theorem: layerwise equivalence, supplied all-split
> direct-sum structural isomorphism, and cardinality recovery through the
> chosen equivalences. This closes the theorem package for coherent cores; it
> still does not derive all-split coherence from raw `P1P7_Core`.
>
> **v0.36 delta** since v0.35:
> `Foundation/Doctrine/T_GUT_Enriched.lean` replaces its three remaining
> `True` headline markers with `EnrichedUniversalSayabilityScopedStatement`,
> a proof that the ordinary complete and scope-aware T_GUT law packages are
> recovered inside any enriched ambient carrying the required ordinary laws,
> plus the concrete finite-Hilbert qubit bridge. `LawvereTheory.lean` replaces
> `lawvereTheory_equiv_finitaryMonad_skeleton : True` with explicit supplied
> comparison data `LawvereTheoryFinitaryMonadComparisonData`, adds
> `MonadLawvereTheoryData`, and exposes projection lemmas for `monadOfTheory`
> / `theoryOfMonad`. The full Power/Lawvere monad equivalence remains open.
>
> **v0.35 delta** since v0.34:
> `Foundation/Doctrine/Instance/HilbertEnriched.lean` no longer uses a
> `Unit`-like `FinHilb` placeholder or `True := trivial` intent markers: it
> now defines `FinHilbObject`, the linear-map category of finite-dimensional
> complex Hilbert objects, coordinate spaces `coordinateHilb n`, and the
> faithful Pauli-to-qubit endomorphism bridge `QuantumToHilbertBridge`.
> `QuantumNativeDagger.lean` packages coordinate FullGUT, matrix dagger/unitary
> semantics, and all-n Pauli operator spanning as
> `concrete_n_qubit_matrix_operator_full_gut`. `HeytingCategoryNative.lean`
> adds the posetal-closed `HeytAlg` end-action package, and `FrmClosed.lean`
> adds pre/post-composition API for JT-bilinear maps. These are scoped native
> semantic steps; bundled `HeytAlg` CCC, full `FdHilb` dagger-SMCC, and
> `MonoidalClosed Frm` remain open.
>
> **v0.34 delta** since v0.33:
> `Foundation/Wen/Embeddings/PauliRingIso.lean` now proves general
> n-qubit Pauli spanning. `pauliToHilbert_linearIndependent n` uses the
> Hilbert-Schmidt orthogonality theorem for recursive Pauli matrices;
> `pauliToHilbert_span_top n` closes the dimension argument; and
> `pauli_n_qubit_spans n` gives the actual finite-sum expansion equation
> for every `Mat_{2^n}(ℂ)` matrix. This closes the scoped Pauli
> vector-space spanning target, not the full `FdHilb` dagger-SMCC theorem.
>
> **v0.33 delta** since v0.32:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` replaces the old
> one-qubit identity sanity placeholder with a real matrix equality.
> `Foundation/Wen/Embeddings/PauliRingIso.lean` now names the general
> n-qubit Pauli spanning theorem as `PauliNSpanningWitness n`, whose field is
> the actual finite-sum expansion equation through `pauliNLinearCombination`;
> the single-qubit coefficient theorem `pauli_single_qubit_spans` is proved.
> At that revision, general n-qubit spanning remained a real proof
> obligation; v0.34 closes it by orthogonality and dimension.
>
> **v0.32 delta** since v0.31:
> `Foundation/Wen/Embeddings/PhasedPauli.lean` now packages the phase-bearing
> stabilizer matrix facts as `PhasedPauliN.HilbertCoherence`. The certificate
> bundles exact same-width composition, tensor append, signed commutation, and
> the retained phase / `R.sigma` swap law. This gives downstream code a stable
> theorem package without upgrading the claim to a full `FdHilb` monoidal
> functor.
>
> **v0.31 delta** since v0.30:
> `Foundation/Wen/Embeddings/PhasedPauli.lean` now defines phase-bearing
> tensor append `PhasedPauliN.tensor` and proves `PhasedPauliN.toHilbert_tensor`.
> The theorem says the exact phase-bearing Hilbert representation respects
> Pauli-word tensor append through the same explicit `hilbertTensorEquiv`
> basis split. This strengthens the stabilizer tensor story while remaining
> below a bundled `FdHilb` monoidal functor.
>
> **v0.30 delta** since v0.29:
> `Foundation/Doctrine/Instance/QuantumNativeDagger.lean` now lifts signed
> symplectic commutation to native n-qubit presentations. The
> `NQubitMatrixDaggerWitness` package includes `signed_commutation`, proving
> that the Hilbert matrices for two presentation objects commute or
> anticommute according to `coordinateSymplectic`. This is still a
> matrix-level stabilizer witness, not a full `FdHilb` dagger-SMCC theorem.
>
> **v0.29 delta** since v0.28:
> `Foundation/Wen/Embeddings/PhasedPauli.lean` now connects retained central
> phases to the symplectic commutation bridge. `pauliNPhase_swap` proves that
> swapping two n-qubit Pauli words changes the retained phase by exactly the
> sign determined by `R.sigma`; `pauliNPhase_eq_swap_iff_sigma_false` gives
> the phase-level commute criterion; and `pauliToHilbert_signed_commutation`
> proves the concrete Hilbert matrices commute or anticommute according to
> that same symplectic bit.
>
> **v0.28 delta** since v0.27:
> `Foundation/Wen/Embeddings/StabilizerQM.lean` now defines the n-qubit
> mod-phase anticommutation parity and proves
> `PauliN.anticommuteParity_eq_sigma` plus
> `PauliN.commutesModPhase_iff_sigma_false`. `HilbertPauliFunctor.lean`
> replaces its former reverse-direction commutation skeleton with
> `reverse_preserves_commutation` /
> `reverse_commutesModPhase_iff_sigma_false`, using the existing
> `R (2*n) ≃ PauliN n` round trip. This closes the n-qubit mod-phase
> σ/commutation bridge; retained central phase algebra remains in
> `PhasedPauli.lean`.
>
> **v0.27 delta** since v0.26:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` now packages the
> recursive Pauli-to-Hilbert tensor facts as `PauliHilbertTensorCoherence`.
> The package includes arbitrary block splitting, left/right 0-qubit tensor
> units, and three-factor associativity for the coordinate matrix
> representation. This is a theorem-grade coordinate coherence certificate,
> not yet a bundled monoidal functor into `FdHilb`.
>
> **v0.26 delta** since v0.25:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` now proves
> `pauliToHilbert_append_tensor_assoc`, comparing the two binary tensor
> decompositions of three appended Pauli words after the explicit
> `Nat.add_assoc` basis cast `hilbertAddAssocCast`. `QuantumNativeDagger.lean`
> lifts this to presentations as `NQubitMatrixTensorAssocWitness` and packages
> the concrete nonempty branch in `concrete_n_qubit_matrix_tensor_assoc_full_gut`.
> This closes coordinate matrix tensor associativity for native stabilizer
> presentations; a bundled monoidal `FdHilb` functor is still a separate target.
>
> **v0.25 delta** since v0.24:
> `Doctrine/Instance/QuantumNativeDagger.lean` now packages the Pauli-word
> tensor split at the native presentation layer. `nQubitAppendObj` appends
> the Pauli coordinates of two native presentations,
> `nQubitMatrixRep_appendObj` proves the appended object is represented by
> the Kronecker product of the two Hilbert matrices via `hilbertTensorEquiv`,
> and `concrete_n_qubit_matrix_tensor_full_gut` bundles the concrete nonempty
> `(n,m,n+m)` package. This closes coordinate matrix tensor-split semantics
> for native stabilizer presentations; a full monoidal `FdHilb` functor is
> still separate.
>
> **v0.24 delta** since v0.23:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` now proves the
> arbitrary Pauli-word tensor split:
> `pauliToHilbert_append_tensor`. The proof introduces the recursive basis
> split `hilbertTensorEquiv`, aligned with the existing head/tail recursion,
> and shows that `Fin.append` of Pauli words maps to the Kronecker product
> of the two Hilbert matrices up to that explicit reindexing. This closes the
> coordinate-level Pauli tensor functoriality obligation for the concrete
> matrix representation; full native `FdHilb` dagger-SMCC semantics remains
> a separate target.
>
> **v0.23 delta** since v0.22:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` now exposes the
> proof-facing tensor-recursion lemmas `pauliToHilbert_zero`,
> `pauliToHilbert_succ`, and `pauliToHilbert_cons`. This makes the successor
> split of the recursive Hilbert representation theorem-grade API rather than
> only a definitional comment. Arbitrary `n+m` tensor-split functoriality was
> closed in v0.24.
>
> **v0.22 delta** since v0.21:
> `Foundation/Wen/Embeddings/PhasedPauli.lean` now lifts retained phases from
> one qubit to arbitrary same-width Pauli strings. `pauliNPhase` is the
> recursive phase factor, `pauliToHilbert_mul_phase` proves exact n-qubit
> matrix multiplication as that phase times phase-quotient composition, and
> `PhasedPauliN.toHilbert_compose` packages a phase-bearing Pauli-string
> representation whose Hilbert matrices multiply exactly. This still does not
> prove full `FdHilb` dagger-SMCC semantics.
>
> **v0.21 delta** since v0.20:
> `Foundation/Wen/Embeddings/PhasedPauli.lean` adds the retained central phase
> syntax `{1,-1,i,-i}`, its complex scalar interpretation, and the exact
> single-qubit multiplication theorem
> `pauliBaseToHilbert_mul_phase`. This closes the single-qubit phase table for
> the chosen Pauli matrix representatives. The same file now also proves
> same-width n-qubit retained multiplication; full `FdHilb` dagger-SMCC
> semantics remain open.
>
> **v0.20 delta** since v0.19:
> `Foundation/Wen/Embeddings/HilbertPauliFunctor.lean` now proves that every
> recursive n-qubit Pauli Hilbert matrix is self-adjoint and unitary:
> `pauliToHilbert_conjTranspose` and `pauliToHilbert_mem_unitary`.  It also
> proves Hilbert-Schmidt orthogonality / faithfulness
> (`pauliToHilbert_trace_inner`, `pauliToHilbert_injective`) and the composed
> `R (2*n) → Hilbert(2^n)` bridge is injective and lands in self-adjoint
> unitaries.
> `Doctrine/Instance/QuantumNativeDagger.lean` packages this as
> `NQubitMatrixDaggerWitness` and
> `concrete_n_qubit_matrix_dagger_full_gut`, combining the existing
> nonempty Pauli-coordinate FullGUT package with matrix faithfulness and
> matrix-level dagger/unitary semantics. This still does not prove arbitrary
> native `FdHilb` dagger-SMCC semantics.
>
> **v0.19 delta** since v0.18:
> `Foundation/Order/HeytingInternalHom.lean` now records the positive
> native Heyting closed boundary: every Heyting algebra is cartesian closed
> as a thin preorder via `a ⊓ b ≤ c ↔ b ≤ a ⇨ c`, and
> `NativeHeytAlg.Presentation.posetalInternalHom` exposes that witness to
> the native FullGUT branch. This does not contradict the strong
> separately-`HeytingHom` obstruction in `HeytingBimorphism.lean`.
> `Foundation/Order/FrmClosed.lean` now proves the adjunction-facing
> `Frm` tensor boundary: morphisms `X ⊗ Y ⟶ Z` are equivalent to
> Joyal-Tierney bilinear maps `X → Y → Z`; the native locale witness records
> that equivalence. The actual exponential frame object and
> `MonoidalClosed Frm` instance remain open.
>
> **v0.18 delta** since v0.17:
> `Foundation/Order/FrmBraided.lean` now closes the Mathlib class layer for
> the Joyal-Tierney `Frm` tensor: `frmBraiding_hexagon_forward` and
> `frmBraiding_hexagon_reverse` prove the two braided hexagons, and
> `frmBraidedCategory` / `frmSymmetricCategory` register
> `BraidedCategory Frm` and `SymmetricCategory Frm`. The native locale witness
> now records these class instances. Closed/internal-Hom structure and a full
> non-cartesian `Frm` T_GUT theorem remain open.
>
> **v0.17 delta** since v0.16:
> `Foundation/Order/HeytingBimorphism.lean` now includes the heterogeneous
> strong Heyting-bilinear/evaluation-like predicate `IsHeytingBilinear₂`.
> The theorem `IsHeytingBilinear₂.codomain_trivial` proves that any
> separately-`HeytingHom` map `A → B → C` forces the codomain `C` to satisfy
> `⊥ = ⊤`, and `IsHeytingBilinear₂.no_nontrivial_codomain` rules out such
> maps into nontrivial codomains. This is an obstruction theorem for bundled
> `HeytAlg` internal-Hom/currying semantics, not a positive internal-Hom
> construction.
>
> **v0.16 delta** since v0.15:
> `Foundation/Order/FrmBraided.lean` adds the concrete Joyal-Tierney
> braiding boundary for `Frm`: the swapped `frameCoprodPairing` is
> JT-bilinear, `frmBraidingHom` sends pairings to swapped pairings,
> `frmBraiding` is an isomorphism, and `frmBraiding_naturality_left` /
> `frmBraiding_naturality_right` prove the two naturality squares.
> `Doctrine/Instance/TopologicalNativeLocale.lean` now records this
> braiding boundary in `TopologicalNativeLocaleWitness`. The class-level
> braided/symmetric closure was added later in v0.18, and the tensor-to-
> bilinear boundary was added later in v0.19; exponential-frame /
> `MonoidalClosed Frm` structure and the full non-cartesian `Frm` T_GUT
> theorem remain open.
>
> **v0.15 delta** since v0.14:
> `Foundation/R/ClaimZ.lean` now makes the D6 boundary theorem-grade:
> `not_D6_holds_iff_all_routes_refuted` normalizes route refutation, and
> `D6SoundForD5` / `D6ExhaustiveForD5` / `D6ExactForD5` separate soundness
> from exhaustiveness instead of burying the converse in prose.
> `ClaimZF2.lean` proves scoped exactness for the current concrete F₂ D5/D6
> pair via `claim_z_F2_D6_exact_for_D5`, while `D6_Tests.lean` audits the
> current HoTT/ETCS/SDG candidate predicates as exactly route-2
> synthetic-failure attempts. `UniquenessGeneral.lean` adds
> `P1P7_CoherentCore.ofDirectSumStructuralIso`, making supplied all-split
> T5 coherence interchangeable with the coherent-core structure without
> deriving it from raw `P1P7_Core`. `QuantumNativeDagger.lean` now also
> proves projective Pauli multiplication:
> `pauliBaseToHilbert_compose_projective`. These are scoped closures, not
> global D6 exhaustiveness, raw-core all-split T5, or full `FdHilb`.
>
> **v0.14 delta** since v0.13:
> `Doctrine/Instance/QuantumNativeDagger.lean` adds a matrix-level dagger
> witness for the native stabilizer branch: the concrete Pauli matrices are
> proved self-adjoint and unitary, the single-qubit dagger token is
> represented by conjugate transpose, and phase-quotient composition is
> represented by matrix multiplication up to a central phase.
> `Doctrine/Instance/TopologicalNativeLocale.lean`
> adds the native locale/frame boundary package: the existing frame-cube
> witness, the Joyal-Tierney monoidal structure on `Frm`, the exact
> opposite-category monoidal structure on `Frmᵒᵖ` underlying locales, the
> `topToLocale ⊣ Locale.pt` adjunction, and faithfulness of compact Hausdorff
> spaces into locales. These are honest boundary witnesses; they still do not
> prove full `FdHilb` dagger-SMCC semantics, Pauli syntax with retained
> central phases, a Hilbert tensor-product functor, exponential-frame /
> `MonoidalClosed Frm`, or a non-cartesian `Frm` T_GUT theorem.
>
> **v0.13 delta** since v0.12:
> `Doctrine/Instance/HeytingCategoryNative.lean` now uses Mathlib's bundled
> `HeytAlg` category rather than a local placeholder bundle. Existing
> `NativeHeytAlg.HomPresentation`s lift to a bundled `HeytAlg` end-action
> (`heytAlg_end_action_nonempty`), and finite/encodable indexed families
> `ι → HeytAlg` now feed ordinary small-category presentations through the
> conditional-absolute FullGUT stack via
> `finite_indexed_category_full_gut_nonempty` and
> `encodable_indexed_category_stream_full_gut_nonempty`. This closes the
> ordinary bundled-category witness layer. It still does not prove that
> bundled `HeytAlg` is cartesian closed; the thin/preorder currying witness
> is closed separately in v0.19.
>
> **v0.12 delta** since v0.11:
> `Doctrine/Instance/QuantumNative.lean` now extends the native stabilizer
> branch from one-qubit Pauli matrices to finite/encodable nonempty
> `n`-qubit Pauli-coordinate presentations. `NQubitPresentation` represents
> objects as `StabilizerQM.PauliN n` and exposes the proved
> `coordinateRep : Obj → R (2*n)`, with composition as R-addition, identity
> as zero, and the transported symplectic pairing alternating. Concrete
> `concrete_n_qubit_stabilizer_coordinate_full_gut` /
> `concrete_n_qubit_stabilizer_coordinate_stream_full_gut` packages are closed
> for `n ≥ 1`. This still does not prove the Hilbert tensor-product or full
> `FdHilb` dagger-SMCC theorem.
>
> **v0.11 delta** since v0.10:
> `Doctrine/Instance/HeytingNative.lean` now adds
> `NativeHeytAlg.HomPresentation`, where every syntax morphism carries a native
> `HeytingHom` compatible with source/target, identity, and composition.
> `finite_hom_full_gut_nonempty` and
> `encodable_hom_stream_full_gut_nonempty` package this morphism layer through
> the existing finite/stream FullGUT witnesses. This is still not a bundled
> `HeytAlg` category or internal-Hom theorem.
>
> **v0.10 delta** since v0.9:
> `Doctrine/Instance/TopologicalNativeFrame.lean` closes the current native
> frame-cube witness: Sierpinski cube frame coproducts
> `frameCoprod (Fin N → Prop) (Fin M → Prop) ≃o Fin (N*M) → Prop` and
> strong JT-bilinear unique factorisation through `FrameHom`. This is not the
> full non-cartesian `Frm` T_GUT theorem or frame exponential/internal-Hom.
>
> **v0.9 delta** since v0.8: `Doctrine/Instance/QuantumNative.lean` closes
> the finite/encodable single-qubit stabilizer witness branch.
> `NativeStabilizerQuantum.SingleQubitPresentation` records a formal system
> with object semantics equivalent to `PauliBase`, named compose/identity/
> dagger tokens, and a faithful `2 × 2` complex Pauli matrix representation.
> `concrete_single_qubit_stabilizer_matrix_full_gut` gives the no-parameter
> concrete package and imports the Pauli-basis theorem that `Mat₂(ℂ)` is
> spanned by the single-qubit Pauli matrices. This is not the full `FdHilb`
> category, dagger-SMCC, or tensor-compatible n-qubit Hilbert theorem.
>
> **v0.8 delta** since v0.7: `Doctrine/Instance/HeytingNative.lean` closes the
> first automatic native semantic-witness branch. Finite native
> Heyting-algebra presentations now construct `SemanticsPreservable` and a
> faithful R-realisation via `NativeHeytAlg.finite_full_gut`; encodable
> presentations construct the stream analogue via
> `NativeHeytAlg.encodable_stream_full_gut`. This is not the full bundled
> `HeytAlg` category or internal-Hom theorem.
>
> **v0.7 delta** since v0.6: `Doctrine/FullGUT.lean` now exposes the stable
> conditional-absolute theorem `absolute_conditional_full_gut` and package
> theorem `conditional_absolute_full_gut`. This closes the absolute interface
> for all `AdmissibleFormalSystem`s that supply `SemanticsPreservable` (or
> `StreamSemanticsPreservable` for the stream branch). It does **not**
> construct those semantic-preservation witnesses automatically; native
> `HeytAlg` / `FdHilb` / `Frm`, Power/enriched all-semantics,
> raw-core all-split coherent T5, and D6 exhaustiveness remain open.
>
> **v0.6 delta** since v0.5: `Doctrine/FullGUT.lean` now exposes the stable
> scoped-coordinate package name `ScopedCoordinateFullGUT` and theorem
> `scoped_coordinate_full_gut`. This theorem packages the current finite/encodable
> representation stack, code-level T3, F₂/GUT-A, GUT-B structural boundaries,
> primary TypeCat represented/coordinate packages, R-scope boundary, concrete F₂
> D6 refutation, and small-category/Lawvere D1 entry points. It closes the
> scoped/coordinate GUT only. It does **not** close absolute FullGUT, full
> Claim Z/T0, bundled `HeytAlg` category semantics, native `FdHilb` / `Frm`
> semantics, Power/enriched
> all-semantics, raw-core all-split coherent T5, or D6 exhaustiveness.
>
> **v0.4 delta** since v0.3: top-level doctrine pointers now treat
> `wen-substrate/` + `08-obligations.md` as the current entry and
> `wen-algebra.md` v0.6 as a historical foundation layer. This document
> continues to track code-doc gaps. In particular, full Claim Z / T0,
> full articulation T2/T3, full structural T5, and final GUT-C are not marked complete:
> `T5_general` is layerwise type equivalence. In `T_GUT`, the older
> `universal_sayability` remains carrier/component-level,
> `universal_sayability_structural_of_adequate` is now archived as the
> structural milestone, `universal_sayability_core_full` gives a scoped
> core carrier/generator transport theorem from adequacy plus explicit
> canonical-transport data, and `universal_sayability_complete_of_adequate`
> packages the current generic law bundle from split adequacy/transport/
> represented semantic/ops predicates. The semantic side now uses explicit
> represented Hom/End data rather than Mathlib `Closed` / internal-hom
> structure. Algebraic/F₂ has a represented semantic witness
> (`algebraicF2_hasSemanticCoherence`) and complete law package theorem
> (`algebraicF2_complete_universal_sayability`) using `R.LinHom N M ≃ R (N*M)`
> and the `R4.EndR2` action/unit/compose laws. WittLift now also has a
> represented coordinate semantic witness
> (`witt_hasSemanticCoherence`) and complete law package theorem
> (`witt_complete_universal_sayability`): `R (N*M)` is interpreted as a
> Witt-coordinate matrix for Hom evaluation and `R 4` as 2×2 Witt matrices
> with proved action/unit/compose laws. This is represented R-family
> semantics, not a proof of a stronger p-adic/Λ-ring universal adjunction.
> Heyting, Quantum, and Topological now also have represented coordinate
> semantic witnesses and complete law-package theorems:
> `heyting_hasSemanticCoherence`, `quantum_HasSemanticCoherence`, and
> `topological_hasSemanticCoherence` close Hom/End at the TypeCat
> coordinate layer. These do not claim the stronger `HeytAlg` internal Hom,
> Hilbert/dagger `FdHilb`, or non-cartesian `Frm` tensor/exponential
> semantics. The primary instance
> `relate_mor` definitions are now total coordinate maps; the five primary Type-level instances prove
> intrinsic `IsAdequate` via the shared `TypeCatRFamily` helper and have local
> square/modal ops-law witnesses. `AlgebraicOpsTarget.lean` now closes both
> the identity algebraic F₂ ops target and a non-identity Boolean-carrier
> F₂ target via coordinatewise `ZMod 2 ≃ Bool`; `WittOpsTarget.lean`,
> `LogicalOpsTarget.lean`, and `QuantumOpsTarget.lean` close scoped
> non-identity ops comparisons to direct coordinate targets (Witt
> coefficient streams, Bool truth values, and Pauli bit pairs).
> `PrimaryComplete.lean` bundles the five primary complete law-package
> theorems and these scoped ops equivalences in one roster. The finite
> F₂ Claim Z package is now closed at its scoped level:
> `claim_z_for_F2_nat` supplies embedding naturality,
> `claim_z_for_F2_holds` supplies the D5 witness, and
> `claim_z_F2_D6_refuted` refutes the current concrete F₂
> falsification bundle. `uniq_prop_F2` / `claim_z_for_F2_uniq` point
> at `T5_A_aggregator`.
> `Doctrine/FullGUT.lean` now adds the theorem-grade interface for the
> next layer: `FormalPresentation`, `REncoding`, `StructurePreservingRMap`,
> `FaithfulRRealisation`, faithful R-realisation for arbitrary finite
> D1-satisfying formal presentations, finite-discrete faithful
> R-realisation, composable `FormalTranslation`, finite `FormalTranslation` code naturality, plus
> stream-level `FaithfulRStreamRealisation` for arbitrary encodable
> D1-satisfying presentations, and stream-level `FormalTranslation`
> code naturality for arbitrary encodable source/target presentations. It also bridges
> `FormalPresentation.SatisfiesD1` into ClaimZ's `D1Articulation`
> interface, with recursive expressibility still supplied explicitly. The conditional
> certificate theorem `full_gut_universal_sayability` now packages these
> branches and adds finite/encodable `AdmissibleFormalSystem` corollaries.
> The certificate also separates the GUT-B structural boundary: raw
> `P1P7_Core` supplies successor-split coherence, while
> `P1P7_CoherentCore` supplies the explicit all-split direct-sum coherence
> needed for arbitrary `(n,m)` structural squares.
> The FullGUT R-map interfaces now preserve proof conclusions and
> operation-as-object embedding in both finite-layer and stream
> realisations, matching the `FormalTranslation` preservation API.
> `current_scoped_D5_holds` now packages the current finite/encodable,
> F₂, GUT-B, and primary-TypeCat branches into a scoped D5 bundle, and
> `current_full_gut_theorem_stack` keeps that scoped D5 proof together
> with the theorem-bearing substrate certificate, including the generic
> R-scope boundary.
> `ScopedCoordinateFullGUT` / `scoped_coordinate_full_gut` is the stable
> headline for exactly this scoped coordinate closure.
> `absolute_conditional_full_gut` and `conditional_absolute_full_gut` close
> the higher conditional-absolute interface: any admissible D1 system with a
> supplied `SemanticsPreservable` witness has a faithful R-realisation.
> This does not close all automatic witness construction; finite/encodable
> native Heyting witnesses are now closed, while bundled `HeytAlg`, native
> `FdHilb`, native `Frm`, Power/enriched all-semantics,
> raw-core all-split coherent T5, and D6 exhaustiveness remain open.
> `Doctrine/T_GUT_Enriched.lean` now has a first non-vacuous enriched
> bridge: `EnrichedTGUTRealisation.complete_of_plain_law_packages` says an
> enriched ambient category can reuse the already-proven ordinary complete
> T_GUT law package; `enriched_plain_law_packages_specialise_to_categorical`
> records the same scoped projection as a theorem. The matching
> `scope_aware_of_plain_law_packages` /
> `enriched_plain_law_packages_specialise_to_scope_aware` bridge also
> threads the generic R-scope boundary through the enriched ambient.
> `PrimaryComplete.lean`
> now bundles scope-aware law packages for all five primary TypeCat
> instances, reusing the generic R-scope boundary. `EnrichedLawvereTheory.lean`
> now carries explicit arity objects and ordinary arity isomorphisms, and
> replaces the old `freeVFunctor`, free/forgetful adjunction, and Power
> fake constructors with explicit `HasFreeVModels`,
> `FreeForgetfulAdjunctionData`, `TheoryMonadData`, and
> `MonadTheoryData`. The ordinary sibling `LawvereTheory.lean` now exposes
> the chosen power projection helpers, proves the model forgetful functor
> full/faithful, and records `FinitaryMonadData` / `TheoryMonadData` /
> `monadOfTheory` plus `MonadTheoryData` / `theoryOfMonad` as supplied
> data for both finitary-monad directions.
> `EnrichedLawvereTheory.lean` also projects plain Lawvere theories into
> `Type`-enriched signature/arity skeletons and projects cartesian enriched
> theories back to the plain signature. This is not Power 1999 and not
> V-natural enriched universal sayability.
> `Foundation/R/T5AClosure.lean` now packages the T5-A side obligations
> that used to be prose-only: the canonical R∞ profinite witness,
> external-overlay transport after uniqueness, satisfier-level R₄
> cardinality/ring equivalence, canonical R₄ action laws, and transported
> atomic action semantics for arbitrary F₂ satisfiers. It also adds
> `T5ANativeAtomicActionData`: if a satisfier supplies an independent
> native action plus transport compatibility with canonical `R 4 = End(R 2)`,
> the identity and composition action laws are derived. This closes the
> current scoped Lean form without claiming every satisfier has such native
> action data automatically.
>
> **v0.3 delta** since v0.2 (which tracked v1.3): wen-substrate has advanced to v1.4,
> adding a fourth level to the R-Family abstraction tower — §3.7.8 **distinction
> monism**, sitting below operation monism (§3.7). The squaring operator Σ acts on
> *distinctions*, not types; the primitive `o`/`x` is the observable binary difference
> itself, with classical/quantum/semantic/propositional/traditional realizations as
> siblings. The realization parameter `k` is renamed to **`δ`** (lowercase delta) to
> stop presupposing algebraic structure; `k` (ring/field) becomes one *class* of
> δ-realization (the algebraic class — §3.6's parametric framework continues
> unchanged, just re-read as "the algebraic-class δ-realizations"). A new Lean file
> `Foundation/R/Distinction.lean` (~230 LOC, 0 sorry, 0 axiom) lands the substrate
> type `Distinction` with `o`/`x` constructors, `Distinction ≃ Bool` (classical
> realization), and the δ-parametric carrier `R' N δ := Fin N → δ` with bridge
> `R' N Bool = R N` (rfl). A new sub-section §1.3c records this; the §3.1 module
> catalog gains an entry; §5 gains a "what is solid" bullet.
>
> **Four-level abstraction tower** (deepest → most concrete) — the v1.4 picture:
>
> 1. **§3.7.8 Distinction monism** — `Foundation/R/Distinction.lean`. Substrate-
>    level primitive: the observable binary difference `o`/`x` itself, prior to
>    any algebraic, logical, or linguistic structure. δ-realization-independent.
> 2. **§3.7.8 δ-parametric substrate** — `R' N δ := Fin N → δ` in the same
>    file. Polymorphic over the realization parameter δ; no typeclass on δ.
> 3. **§3.6 parametric R-Family** — `Foundation/R/Parametric.lean`. The
>    *algebraic class* of δ-realizations: `RFamily k N := Fin N → k` with `k`
>    a ring/field. The v1.4 reframing reads `k` as "algebraic-class δ".
> 4. **§3.7 operation monism** — `Foundation/R/OperationMonism.lean`. The
>    operator layer above carriers: `Σ : X ↦ X × X` + iteration `RTower X k`;
>    carriers are theorems about Σ, not premises.
>
> **δ-realization framework — non-algebraic siblings of `k`** (per §3.7.8 of
> wen-substrate v1.4):
>
> * **Classical computational** — `δ = Bool`, the existing F₂ realization
>   (`R' N Bool = R N` rfl). This is the F₂ minimum-instance substrate.
> * **Quantum** — `δ` = computational-basis kets `{|0⟩, |1⟩}` (no Lean bridge yet)
> * **Propositional** — `δ = Prop` (logical realization; no Lean bridge yet)
> * **Per-language vocabularies** — `δ` = a finite binary lexical distinction
>   in some natural language (linguistic realization; no Lean bridge yet)
> * **阳/阴 (yang/yin) classical-traditional** — `δ` = the binary distinction
>   of the yi-jing tradition (cultural-traditional realization; surfaces in
>   `Foundation/Atlas/Yi/` as named-element overlays)
>
> The algebraic `k` (ring/field) of §3.6 is one *class* of these δ-realizations;
> the others are first-class siblings, not specializations.
>
> **Foundational lineage** for the "distinction" terminology — why §3.7.8 is
> named as it is:
>
> * **Spencer-Brown**, *Laws of Form* (1969) — the act of distinction as the
>   primitive operation; "Draw a distinction" is the first move
> * **Bateson**, *Steps to an Ecology of Mind* (1972) — information is "a
>   difference that makes a difference"; the unit of mind is the difference
> * **Wheeler**, "Information, Physics, Quantum: The Search for Links" (1989)
>   — "it from bit": physical existence derives from binary informational
>   distinction
> * **阳/阴 yi-jing tradition** — the binary distinction (solid line / broken
>   line) as the substrate of all hexagram-level articulation, ~3000 years
>
> These four lineages converge on the same primitive: a binary observable
> distinction is prior to algebra, prior to logic, prior to language. The
> `Distinction` type in `Foundation/R/Distinction.lean` formalises this
> primitive.
>
> **v0.2 delta** since v0.1 (which tracked v1.0.3): wen-substrate has advanced to v1.3,
> adding three substantive content layers — §3.7 operation monism, §3.8 RPattern
> substrate + Wen.Core 12-instr ISA, and §4.7bis X²-256 conditional UG with full
> uniqueness chain (six new Lean files, combined `0 sorry`, including the BA-preserving
> Birkhoff step 4 closed unconditionally via self-built Mathlib infrastructure). New
> rows are appended in §1.3a (§3.7), §1.3b (§3.8), and §1.4a (§4.7bis); existing rows
> are re-annotated where their status has changed.

---

## Preface

`wen-substrate.md` is a foundational document. It states a maximal claim
(R-Family **is** the universal formal substrate; Claim Z: "formal" ≡
"R-Family-articulable"), defends it structurally, and exposes a Part VIII
proof programme (D1–D3, T1–T8, plus Phase 0 sub-theorems T_P3 / T_P6 /
T_P7a / T_P7b). The Lean codebase under `formal/SSBX/Foundation/` is the
formalization arm of the project. The two are **not yet co-extensive**.

This document exists so that contributors and reviewers can see, at a
glance:

* what wen-substrate **says** at each section,
* what Lean code (if any) **currently backs** that claim,
* and **what the gap is**.

The goal is calibration, not retreat: every claim in wen-substrate
remains made; the proof programme in Part VIII §8.10 enumerates how those
claims will be discharged; this document tracks the present line between
"proved in Lean" / "partial mechanization" / "doc-only structural argument".

See **Part VIII §8.10** of wen-substrate for the canonical priority order
of proof obligations; this document mirrors that ordering in §2 below.

Conventions used in the status column of the tables that follow:

* `✓ proven` — Lean theorem corresponding directly to the claim
* `⚠ partial` — Lean has skeleton / weaker form (e.g., `Equiv` where `RingEquiv` is needed)
* `□ open` — no Lean equivalent yet; doc-only or programmatic
* `—` — no Lean equivalent intended at this stage (e.g., abstract conceptual definition)

All file paths are relative to repository root.

---

## §1 What v1.4 promises — section-by-section map

### §1.1 Part I (Core definitions, §1.5.1–§1.5.6)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §1.5.1 | Formal articulation: 7-component definition | conceptual; no Lean carrier needed | — |
| §1.5.2 | Universal formal substrate: closed generative framework | conceptual | — |
| §1.5.3 | Minimality: closure-generative not symbol-fewest | conceptual | — |
| §1.5.4 | Equivalence of substrates (5 specializations) | conceptual | — |
| §1.5.5 | Embedding (partial systems): `S ↪ R` | conceptual | — |
| §1.5.6 | R-Family-over-`k` as full structured object | `Foundation/R/Parametric.lean` (`RFamily k N`) — carrier only | ⚠ partial |

### §1.2 Part II (Necessary properties P1–P7)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §2.1 P1 | `F_2` minimum base | `Foundation/R/Basic.lean` — `R N := Fin N → Bool` | ✓ proven |
| §2.2 P2 | Direct sum `R_M ⊕ R_N ≅ R_{M+N}` | `Foundation/R/DirectSum.lean` — `directSumEquiv : R (N + M) ≃ R N × R M` | ✓ proven |
| §2.3 P3 | 3-layer bilinear: `L_0` dot, `L_1` σ, `L_2` `q`/Arf family | `Foundation/R/Bilinear.lean` — `dot`, `sigma`, `q`, `arf`, `dot_eq_sigma_xor_LL` | ✓ proven |
| §2.3 P3 note | L2 form / Arf-binary classification and scoped uniqueness anchors | `Foundation/R/PhaseZero.lean` — `T_P3_arf_binary`, `T_P3_arf_surjective`, `T_P3_sigma_uniqueness_R2`, packaged by `T_P3`; `Foundation/R/PhaseZero/Closure.lean` — `scoped_phase_zero_closed` | ✓ closed at scoped F₂ Phase 0 boundary; broader all-dimensional up-to-isometry remains outside Phase 0 |
| §2.4 P4 | Squaring tower `R_N → R_{2N}` | `Foundation/R/Squaring.lean`, `Foundation/R/SubTower.lean` | ✓ proven |
| §2.4 P4 | Cross-scale self-similarity (Δ, π_i, f^⊕2) | `Foundation/R/DirectSum.lean` — `delta`, `takeLeft` / `takeRight`, `liftOplus2`, `crossScaleSelfSimilarity` | ✓ proven |
| §2.5 P5 | `Hom(R_n, R_m) ≅ R_{nm}` (cardinality) | `Foundation/R/Hom.lean` — `card_eq_R : Fintype.card (LinHom N M) = 2^(N*M)` | ✓ proven |
| §2.5 P5 | `R_4 ≅ End(R_2) ≅ M_2(F_2)` as ring | `Foundation/R/PhaseZero.lean` — `T_P7b_ring_equiv`; `Foundation/R/PhaseZero/TP7bUniqueness.lean` — `T_P7b_full`; `Foundation/R/R4Minimality.lean` — `R4_structurally_minimal_full` | ✓ closed at scoped F₂ boundary |
| §2.5 P5 | `R̂ := lim_← R_{2^k}` (continuum / Cantor space) | `Foundation/RInfty/Profinite.lean` — `L_inf`, `fromStream`/`toStream`, final-coalgebra | ⚠ partial (structural skeleton; no continuum identification proved as cardinality theorem) |
| §2.6 P6 | `R_2 ≅ V_4` as 4-modality carrier | `Foundation/Atlas/Yi/Shi.lean` — `Shi := R 2`, with V_4 group structure | ✓ proven |
| §2.7 P7a | `R_3` coordinate reversal and 4+4 split | `Foundation/R/PhaseZero.lean` — `T_P7a`; `Foundation/R/PhaseZero/Closure.lean` — `scoped_phase_zero_closed` | ✓ proven |
| §2.7 P7b | `R_4 ≅ M_2(F_2)` as F_2-algebra (Wedderburn forced) | `Foundation/R/PhaseZero.lean` — `T_P7b_ring_equiv`; `Foundation/R/PhaseZero/TP7bUniqueness.lean` — `T_P7b_full`; `Foundation/R/PhaseZero/TP7bFormB.lean` — `T_P7b_form_b_packaged`; `Foundation/R/R4Minimality.lean` — `R4_structurally_minimal_full` | ✓ closed at scoped F₂ Phase 0 boundary |

### §1.3 Part III (R-Family emerges, §3.5 cosmology, §3.6 parametric)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §3.1 | R-Family as 12-item structure | `Foundation/R/RFamilyStructure.lean` — Σ-first records `RFamilySigmaCore`, `RFamilyConsequences`, `RFamilyStructure`; canonical witness `d2_complete` | ✓ closed for canonical F₂ D2 record |
| §3.5.1 | `R_∞ = R̂` profinite, cardinality 2^ℵ₀, ≅ Cantor space | `Foundation/RInfty/Profinite.lean` — bijection to `Stream' (R 8)` proven; explicit "continuum" / "Cantor space" identification with Mathlib's `Cantor` (if it existed) not asserted | ⚠ partial |
| §3.5.4 | `R_4` phenomenology matrix (4×4 = 16 cells) | conceptual + traditional reading | □ open (interpretive overlay) |
| §3.5.5 | `R_8` = first culturally salient articulation layer | `Foundation/Atlas/Yi/Hexagrams.lean`, `Cell256.lean` (= Hexagram × Shi) | ✓ proven (as carrier) |
| §3.6 | Parametric R-Family-over-`k` | `Foundation/R/Parametric.lean` — `RFamily k N := Fin N → k`, plus `instFintype`, `instDecidableEq`, `instInhabited` | ⚠ partial (skeleton; per-base P1–P7 instances deferred) |
| §3.6.7 | Per-base bridge to ℝ, ℂ, ℂ_p, etc. | not present — Mathlib bridge work future | □ open (D3 obligation) |

### §1.3a Part III additions: §3.7 operation monism (new in v1.2/v1.3)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §3.7.1–§3.7.7 | R-Family below the base — `Σ : X ↦ X × X` + iteration; carriers are *theorems* about `Σ`, not premises | `Foundation/R/OperationMonism.lean` — `Sigma X := X × X`, `Sigma.map`, `RTower X k` (functor + iteration), `rtower_no_typeclass` (witness: no typeclass on `X` required), `BoolTower`/`PUnitTower` cross-sections; 0 sorry; **additive, non-replacing** (does not retype downstream files). | ✓ proven (doctrinally; not yet load-bearing for downstream substrate) |
| §3.7.6 | `Foundation/R/OperationMonismBridge.lean` connecting `RTower Bool` to the existing `R N` carriers | present (`Foundation/R/OperationMonismBridge.lean`); imports `Basic.lean` and `OperationMonism.lean` | ✓ proven (skeleton) |

### §1.3b Part III additions: §3.8 RWord / RPattern substrate + Wen.Core 12-instr ISA (new in v1.3, renamed in v0.6 cleanup)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §3.8.0 | `RWord` strict arbitrary-rank `o`/`x` parser / renderer; theorem-backed parse/render round trips (`parseAt?_render`, `rank?_render`), parse-success rank extraction, and valid-word append rank law; direct-sum splits such as `R 10 ≃ R 8 × R 2` and `R 12 ≃ R 8 × R 4` | `Foundation/R/RWord.lean` | ✓ proven |
| §3.8.1 | `RPattern` as face-lattice (Phases A–D): `empty` identity, `merge` partial monoid, `restrict` codim-raising, `mergeAll` list fold, `support` algebra (`support_mergeFn = ∪`, `support_restrict = ∩`) | `Foundation/R/RPattern.lean` | ✓ proven |
| §3.8.2 | Wen.Core 12-primitive ISA (`nop` / `merge` / `restrict` / `push` / `pop` / `flipBit` / `writeBit` / `xorMask` / `branchBitEq` / `jump` / `halt` / `mergePrior`); semantics; State invariants (`initial` = (pc=0, cur=`RPattern.empty`, history=[], halted=false)) | `Foundation/Wen/Core/Instruction.lean` + `State.lean` + `Machine.lean` | ✓ proven |
| §3.8.3 | Codim filtration relation to R-Tower; `{R₀, R₂, R₄, R₈}` ↔ `{support size 0, 2, 4, 8}` | `Foundation/R/RPattern.lean` (lattice picture); cross-referenced in `Foundation/Wen/Core/Instruction.lean` header | ✓ proven (structural; identity at the support-size level) |
| §3.8.4 | `ConstraintDemo`: `agreementProg_halts`, `conflictProg_halts` (substrate detects contradiction), `restrictProg_forgets_bit_2` (codim-raising mid-program) | `Foundation/Wen/Core/ConstraintDemo.lean` — 3 theorems proven by `rfl` from small fuel bounds | ✓ proven |

### §1.3c Part III additions: §3.7.8 distinction monism (new in v1.4)

The fourth (deepest) level of the R-Family abstraction tower. Σ acts on
*distinctions*, not on types. The primitive `o`/`x` is the observable binary
difference itself; classical/quantum/semantic/propositional/traditional readings
are siblings (the classical computational realization is `Distinction ≃ Bool`).
The realization parameter is renamed `k → δ`; algebraic `k` (ring/field) is one
*class* of δ-realization.

Foundational lineage (Spencer-Brown 1969, Bateson 1972, Wheeler 1989, 阳/阴
tradition) — see the v0.3 delta block above for the full enumeration of why
the primitive is named "distinction" and what the δ-realization siblings are.

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §3.7.8 | `Distinction` as substrate-level primitive type with `o`/`x` constructors; classical computational realization `Distinction ≃ Bool` | `Foundation/R/Distinction.lean` — `inductive Distinction \| o \| x` with derived `DecidableEq`, `Repr`, `Fintype`; `Distinction.toBool` / `ofBool` + round-trip lemmas; `Distinction.equivBool : Distinction ≃ Bool`; `Distinction.card : Fintype.card Distinction = 2`. 0 sorry, 0 axiom. | ✓ proven |
| §3.7.8 | δ-parametric substrate carrier `R' N δ := Fin N → δ` (δ-realization-independent) | `Foundation/R/Distinction.lean` — `def R' (N : ℕ) (δ : Type) : Type := Fin N → δ` | ✓ proven |
| §3.7.8 | Bridge: existing F₂ R-Family is `δ = Bool` realization of `R'` | `Foundation/R/Distinction.lean` — `R' N Bool = R N` (rfl) and `Nonempty (R' N Distinction ≃ R N)` | ✓ proven |
| §3.7.8 | `k` (ring/field) reframed as the *algebraic class* of δ-realizations (no doctrinal change to §3.6; just re-reading the parameter) | `Foundation/R/Parametric.lean` continues unchanged — now read as "the algebraic-class δ-realization" | — (doctrinal re-reading; no Lean delta) |

### §1.4 Part IV (Universal coverage + six major claims)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §4.1.5b | ℂ-Hilbert IS R-Family-over-ℂ (at carrier level) | none; carrier identity is `ℂ^{2^n} = R_{2^n}^{(ℂ)}`, but no Mathlib bridge | □ open |
| §4.1–§4.6 | Mathematics / language / spacetime / computation / physics coverage | per-domain naming in `Foundation/Atlas/`, but "universal coverage" is structural, not Lean-checked | □ open (T1 / T2 obligations) |
| §4.6.5 | Six universal claims (§4.7–§4.12) are **stated at full strength but programmatic** | this is already the doc's self-assessment | — |
| §4.7 | R-Family as Chomsky's UG (unconditional form) | doc-only | □ open (programmatic) |
| §4.7bis | X²-256 IS UG (conditional form): existence | `Foundation/Wen/X2Codes.lean` — `wenCodeUG : UGCandidate`, 8 axes, dual / palindrome / compPal involutions, 16/16/16/4/4/0 sub-lattice cardinality theorems, `Sayable` / `Silent` split (8 sayable, 248 silent), 0 sorry | ✓ proven |
| §4.7bis.5 (a) | `axes = 8` forced from minimality | `Foundation/Wen/X2CodesMinimal.lean` — `UGCandidateMinimal` with (M1) squaring-tower / (M2) four corners / (M3) tower-depth minimality; `theorem minimal_forces_axes_eight`; 0 sorry | ✓ proven |
| §4.7bis.5 (b) | Naming-density: atom support = `IsX2 ∩ (Pal ∪ CompPal)` from (ℤ/2)² | `Foundation/Wen/X2CodesNaming.lean` — `NamingLocus`, `theorem seeded_atoms_are_naming_locus`, orbit counts, `UGCandidateNamed`, `wenCodeUGNamed`; 0 sorry | ✓ proven |
| §4.7bis.5 (c) | F₂-forcing chain (Stone–Birkhoff): 5 steps incl. BA-preserving step 4 | `Foundation/Wen/F2Forcing.lean` — `step1_bitcube_BA`, `step2_holds`, `step3_BR_char_two`, `step4_holds` + `step4_birkhoff_BAiso_holds` (unconditional via self-built `finiteLatticeToCompleteLattice` / `finiteBooleanAlgebraToCompleteBooleanAlgebra` / `finiteBooleanAlgebraToCABA`), `step5_holds`, `chain_holds`; 0 sorry | ✓ proven (unconditional, including BA-iso refinement) |
| §4.7bis.5 (d) | `face_uniqueness_conjecture` (DualIso form) | `Foundation/Wen/X2CodesFace.lean` — `bridge`, `bridge_dual_comm`, `theorem face_dual_uniqueness`, `theorem face_full_uniqueness` (under atom-compatibility), `theorem face_uniqueness : face_uniqueness_conjecture`; 0 sorry | ✓ proven (DualIso form; full-Iso form under atom hypothesis) |
| §4.7bis.5 — original | `OpenProblem2.uniqueness_conjecture` (full-Iso on `UGCandidateRich`, no atom hypothesis) | `Foundation/Wen/X2CodesUniqueness.lean` — recorded as `def uniqueness_conjecture : Prop`; *provably impossible* without atom hypothesis (different label strings give dual-iso but not full-iso candidates) | □ open as Prop / **provably false** without atom hypothesis — retained as scaffold; superseded by `face_uniqueness` (DualIso) and `face_full_uniqueness` (atom-pinned full Iso) |
| §4.8 | R-Family as substrate of all computable cognition | doc-only | □ open (programmatic) |
| §4.9 | R-Family as algebraic phenomenology | doc-only | □ open (programmatic) |
| §4.10 | R-Family as substrate of decidable formal systems; Gödel at R_8 | `Foundation/Atlas/Yi/Diagonal.lean` (~647 LOC, 0 axiom diagonal); `Foundation/Wen/MetaInterp/GodelR8.lean` (anchor + cross-reference) | ✓ proven (at R_8 layer for ISA on Hexagram × Shi) |
| §4.11 | R-Family as bridge between informational and physical | doc-only; self-rated speculative in §4.6.5 | □ open |
| §4.12 | R-Family as what "formal" means | doc-only; structural defense | □ open (Claim Z) |

### §1.5 Part VII (Direct claim + Claim Z)

| wen-substrate | Claim | Lean backing | Status |
|---|---|---|---|
| §7.1 | R-Family IS the universal formal substrate | structural argument across Parts II–VI; `absolute_conditional_full_gut` / `conditional_absolute_full_gut` closes the conditional-absolute interface, while `ScopedCoordinateFullGUT` / `scoped_coordinate_full_gut` packages the current coordinate theorem stack | ✅ conditional-absolute interface closed; automatic semantic construction and unrestricted T0 remain open |
| §7.8 Claim Z | "formal" ≡ "R-Family-articulable" by definition | bi-directional structural-analytic theorem (§7.8.3); three falsification routes (§7.8.8); current scoped D5 branch closed by `current_scoped_D5_holds` and packaged by `scoped_coordinate_full_gut`; conditional-absolute theorem stack closed by `conditional_absolute_full_gut` | ⚠ conditional/scoped branches closed; automatic witness construction, absolute Claim Z, and D6 exhaustiveness remain open |

---

## §2 Proof obligation status — Part VIII §8.10 priority order

The §8.10 ordering, with current Lean status against each item:

| # | Obligation | What | Status | Notes |
|---|---|---|---|---|
| 1 | **D1** | Definition of formal articulation (§1.5.1) | ⚠ partial globally; ✅ F₂ analytic closure closed | `Doctrine/FullGUT.lean` defines `FormalPresentation` and proves `formalPresentation_satisfiesD1_to_D1Articulation`, plus process and non-process wrappers around `ClaimZ.d1_implies_P`. `R/ClaimZ/Analytic.lean` closes the F₂-Boolean analytic `D1 => P1-P7` branch via `D1_implies_Phase1Closure_F2` and `D1_implies_PClosure_at_F2`; `R/ClaimZ/Analytic/Closure.lean` exposes public aggregate `scoped_phase_one_closed`. It now also proves `categoryFormalPresentation_satisfiesD1` for every small category with decidable object equality and a chosen base object, with `lawvereFormalPresentation_satisfiesD1` as the Lawvere-theory corollary. `Closure/PhiOperator.lean` projects the fixed-point `D1` candidate into a witnessed ClaimZ D1 interface via `ArticulationCandidate.ClaimZBridge.D1_toD1Articulation_fields_hold`. Recursive expressibility remains explicit input for arbitrary presentations; verification against finite-limit theory, institutions, doctrines, and polymorphic/non-F₂ analytic closure remains open. |
| 2 | **D2** | R-Family as full enriched structure (§3.1) | ✓ closed for canonical Σ-first F₂ record | Companion doc `r-family-definition.md` now presents the Σ-first normal form. Lean module `Foundation/R/RFamilyStructure.lean` defines `RFamilySigmaCore`, `RFamilyConsequences`, `RFamilyStructure`, `canonicalRFamilyStructure`, `carrier_is_theorem_at_power`, and `d2_complete`. This closes canonical D2 only; the D3/δ-polymorphic full record remains separate. |
| 3 | **D3** | Parametric R-Family over arbitrary base (§3.6) | ⚠ partial | `Foundation/R/Parametric.lean` defines `RFamily k N := Fin N → k` with basic instances (`Fintype`, `DecidableEq`, `Inhabited`). Per-base lemma porting (P1–P7 over `ℝ`, `ℂ`, `ℂ_p`, `ℤ_p`, `ℚ_p`) requires Mathlib bridge work — explicitly deferred per §3.6.7. (Under v1.4, `k` is re-read as the *algebraic class* of δ-realization; the underlying §3.7.8 substrate `R' N δ := Fin N → δ` is in `Foundation/R/Distinction.lean` with `R' N Bool = R N` rfl.) |
| 4a | **T_P3** | Bilinear classification (P3): L0/L1/L2 scoped F₂ anchors | ✓ closed at scoped F₂ Phase 0 boundary | `Foundation/R/PhaseZero.lean` packages `T_P3`, `T_P3_arf_surjective`, and `T_P3_sigma_uniqueness_R2`; broader all-dimensional up-to-isometry remains separate. |
| 4b | **T_P6** | V_4 carrier minimality (P6) | ✓ proven | `Foundation/R/PhaseZero.lean` packages pure R-core `T_P6` (cardinality `|R 2| = 4`, coordinate flips `R2.flip0` / `R2.flip1`, composite `R2.flip01`, and commutation/involution laws). The explicit minimality lemma "≥2 distinct commuting non-identity involutions ⟹ ≥4 elements" is discharged in `Foundation/R/PhaseZero/TP6Minimality.lean` (`card_ge_four_of_two_commuting_involutions` + `T_P6_card_ge_four` applied to `R 2`). 0 sorry, 0 axiom. |
| 4c | **T_P7a** | Coordinate reversal forces 4+4 split | ✓ proven | `Foundation/R/PhaseZero.lean` `T_P7a` package: defines pure `R3.swap02` (coordinate 0 ↔ 2), proves it involutive, gives `R3.palindromes` / `R3.nonPalindromes` length 4 and Nodup, and proves `swap02_fixed_iff_mem_palindromes`. Atlas/Yi names are downstream wrappers. 0 sorry, 0 axiom. |
| 4d | **T_P7b** | Wedderburn: `R_4 ≅ M_2(F_2)` as F_2-algebra | ✓ closed at scoped F₂ Phase 0 boundary | `Foundation/R/PhaseZero.lean` `T_P7b` and `T_P7b_ring_equiv`; `Foundation/R/PhaseZero/TP7bUniqueness.lean` `T_P7b_full`; `Foundation/R/PhaseZero/TP7bFormB.lean` `T_P7b_form_b_packaged`; `Foundation/R/R4Minimality.lean` `R4_structurally_minimal_full`; `Foundation/R/PhaseZero/Closure.lean` `scoped_phase_zero_closed`. Full arbitrary simple finite F₂-algebra classification remains separate. |
| 5 | **T1** | Weak universality / encoding theorem | □ open | Per-system Lean encodings (the `R_8` ISA, the YiInstr machine, `BaguaTuring`) exist as proofs of concept, but the abstract "every formally describable system embeds in some R-Family-over-k" theorem is not stated. |
| 6 | **T6** | Self-articulation theorem | ✅ closed at scoped syntax/stream level | `Foundation/Doctrine/FullGUT.lean` now defines `rFamilySelfPresentation`, a concrete `FormalPresentation` for R-family layer objects, morphism syntax, relation tokens, operation tokens (`unit`, `tensor`, `compose`, `hom`, `atom3`, `wedderburn4`), rule syntax, and proof syntax. `rFamilySelfPresentation_satisfiesD1` proves the D1 interface, `rFamilySelfPresentation_stream_realisation` gives a faithful `RStream` realisation via the generic encodable-presentation theorem, and `rFamily_self_articulation` packages the T6 witness. `Foundation/R/Hom.lean` `card_eq_R` remains the Hom-as-content cardinality component. This does not claim a semantic evaluator for every future native category. |
| 7 | **T2** | Case-by-case articulation theorems | □ open | Programmatic per wen-substrate §8.3 / §8.9 Phase II. The list of target case studies (propositional logic, FOL, λ-calculus, type theory, automata, category fragments, stabilizer QM) has no Lean theorem yet. |
| 8 | **T3** | Naturality theorem | ⚠ partial — finite/encodable code naturality closed | `claim_z_for_F2_nat` closes naturality for the finite F₂ embedding package, and `Doctrine/FullGUT.lean` now proves `finite_formal_translation_code_naturality` and `encodable_formal_translation_code_naturality`: every finite or encodable `FormalTranslation` induces commuting R-code maps on object/morphism/relation/op/rule/proof encodings plus proof-conclusion and operation-as-object structural maps. The finite and stream packages also preserve identity and composition of `FormalTranslation` on valid codes, and `FormalTranslation.category_laws` proves identity/associativity extensionally on the six syntactic maps. Full semantic articulation naturality across all formal-system categories remains open and depends on intended T2 bridges. |
| 9 | **T4** | Minimality theorem (especially step 3) | ⚠ partial → mostly closed for classical-Boolean scope | Originally **Open Problem #1** in wen-substrate §8.4. Strategy A (Stone–Birkhoff chain) **discharged in `Foundation/Wen/F2Forcing.lean` (`chain_holds`, including the BA-preserving Birkhoff step 4 via `step4_birkhoff_BAiso_holds`)** for classical-Boolean carriers; non-classical scopes (intuitionistic constructive content, quantum at C*-level, modal, substructural) remain open per §8.4.4. |
| 10 | **T5** | Uniqueness up to equivalence | ⚠ partial — conditional UG case closed; GUT-B successor-structural closed | Phase III at full generality. `Foundation/R/UniquenessGeneral.lean` now includes `P1P7_Core.successor_structural_iso`: every δ-polymorphic core has recursively chosen layer equivalences to `R N δ` commuting with each successor split; arbitrary `(n,m)` coherence still needs explicit unit/associativity laws. **For the conditional UG case (§4.7bis), structurally-forced uniqueness (`DualIso` form on `UGCandidateFace`) is closed (`theorem face_uniqueness`), and the atom-pinned full-`Iso` form is closed under explicit atom-compatibility hypothesis (`theorem face_full_uniqueness`)** — both in `Foundation/Wen/X2CodesFace.lean`. The general substrate-uniqueness theorem (ZFC ↔ ETCS-style cross-foundation bi-interpretability) remains open. |
| 11 | **T7–T8** | Semantic overlay theorems (conservativity, non-arbitrariness) | □ open | Phase III. |
| 12 | **Domain T's** | UG, cognition, phenomenology, physical-info, formal-articulation | ⚠ partial — UG existence/uniqueness closed conditionally | Per-domain proof obligations from §4.7–§4.12. §4.7 (unconditional UG) doc-only; **§4.7bis (conditional UG) closed across 6 Lean files** (`X2Codes`, `X2CodesUniqueness`, `X2CodesFace`, `X2CodesNaming`, `X2CodesMinimal`, `F2Forcing`) with combined `0 sorry`; §4.8–§4.12 doc-only. |

---

## §3 Lean module catalog

Quick file → topic listing of the foundational R-Family modules. All paths
relative to repo root.

### §3.1 Core R-Family (`formal/SSBX/Foundation/R/`)

| File | One-line summary |
|---|---|
| `R/Basic.lean` | `R N := Fin N → Bool`; `AddCommGroup`, basis, zero/one/constx, decidable equality, `Fintype` — the canonical F_2-vector-space carrier. |
| `R/DirectSum.lean` | `directSumEquiv : R (N + M) ≃ R N × R M`; `takeLeft` / `takeRight` projections; `append`. P2. |
| `R/Bilinear.lean` | `dot`, `sigma` (symplectic), `q` (quadratic refinement, v1.0.1 form), `arf`; polarization `dot_eq_sigma_xor_LL`. P3. |
| `R/Tensor.lean` | Tensor structure on R-Family carriers. |
| `R/Squaring.lean` | Squaring step `R (2*N) ≅ R N × R N`; iterated tower. P4. |
| `R/SubTower.lean` | Sub-tower (e.g., `{R_1, R_2, R_4, R_8}` self-similar squaring sub-sequence). |
| `R/Hom.lean` | `LinHom N M := Fin M → Fin N → Bool`; matrix view, `apply`, composition; `card_eq_R : card (LinHom N M) = 2^(N*M)`. P5 cardinality. |
| `R/Aut.lean` | Automorphisms of `R N`. |
| `R/DirectDecomp.lean` | Direct decomposition utilities. |
| `R/BeyondR8.lean` | Structure beyond `R 8` (the cultural ceiling). |
| `R/Parametric.lean` | `RFamily k N := Fin N → k` parametric carrier over arbitrary `k`; `Fintype`/`DecidableEq`/`Inhabited` instances; F_2-specialization `RFamily Bool N = R N` (definitional). D3 skeleton. Under v1.4, `k` is read as the *algebraic class* of δ-realization (one of: ring/field). |
| `R/PhaseZero.lean` / `R/PhaseZero/Closure.lean` | Phase 0 small theorems per wen-substrate §8.8: parent `T_P3`, `T_P6`, `T_P7a`, `T_P7b`; aggregate `scoped_phase_zero_closed` packages G6.1/G6.2/G6.3 extensions and `R4_structurally_minimal_full`. 0 sorry, 0 axiom. |
| `R/RFamilyStructure.lean` | D2 Σ-first Lean object. Defines `RFamilySigmaCore` (`RTower Bool` and `RTower Bool k ≃ R (2^k)`), `RFamilyConsequences` (12-item bundle), `RFamilyStructure`, `canonicalRFamilyStructure`, and `d2_complete`. The old marker remains only for compatibility. |
| `R/OperationMonism.lean` | §3.7: `Sigma X := X × X`, `RTower X k`, `rtower_no_typeclass`, `BoolTower`/`PUnitTower`. The operator-monism layer of the abstraction tower; additive, non-replacing. |
| `R/OperationMonismBridge.lean` | Bridge from `RTower Bool` to the existing `R N` carriers. |
| `R/RWord.lean` | §3.8: arbitrary-rank strict `o`/`x` parsing/rendering for `R N`, fixed-rank parser, Sigma-rank parser, and direct-sum split helpers (`R 10 ≃ R 8 × R 2`, `R 12 ≃ R 8 × R 4`, `R 16 ≃ R 8 × R 8`). |
| `R/RPattern.lean` | §3.8: `RPattern N := Fin N → Option Bool`; `empty` identity; `compatible`/`merge`/`mergeFn`; `restrict`; `mergeAll` list fold; `support` algebra (`support_mergeFn = ∪`, `support_restrict = ∩`); R-tower codim filtration. |
| `R/Distinction.lean` | §3.7.8 (deepest level of the v1.4 abstraction tower): `Distinction` inductive type with `o`/`x` constructors (`DecidableEq`/`Repr`/`Fintype` derived); `toBool`/`ofBool` round-trip + `Distinction.equivBool : Distinction ≃ Bool` (classical computational realization); `Distinction.card = 2`; `R' N δ := Fin N → δ` δ-parametric substrate (no typeclass on δ); bridge `R' N Bool = R N` (rfl) and `Nonempty (R' N Distinction ≃ R N)`. ~230 LOC, 0 sorry, 0 axiom. |

### §3.2 R_4 specifics (`formal/SSBX/Foundation/R4/`)

| File | One-line summary |
|---|---|
| `R4/Enumeration.lean` | Enumeration of `R 4`'s 16 elements; helper constructors. |
| `R4/Bilinear.lean` | Bilinear forms specialized to `R 4`. |
| `R4/EndR2.lean` | `R 4 = End(R 2)`: `asMatrix`, `applyR2`, `composeR2`, `idR4`; `matrixEquiv : R 4 ≃ (Fin 2 → Fin 2 → Bool)` (Equiv). T_P7b target. |
| `R4/HomMat.lean` | Matrix-form Hom view for R_4. |
| `R4/GL2Embedding.lean` | `GL_2(F_2)` subgroup structure on rank-2 R_4 elements. |
| `R4/RankStratification.lean` | Rank stratification of the 16 elements of `R 4`. |
| `R4/AutA8.lean` | Automorphism group of R_4 (related to symmetric group S_3 / GL_2(F_2)). |

### §3.2a Atlas overlays moved out of R core

| File | One-line summary |
|---|---|
| `Atlas/Role/Phantom.lean` | Opt-in phantom role tags for `R N` elements. |
| `Atlas/Role/StateOp.lean` | Opt-in state/operator dual reading on R_4. |
| `Atlas/Judgment/{Information,Attractor,Behavior}.lean` | Opt-in judgment and trajectory classifications over `R N`. |
| `Atlas/Judgment/R8/{Information,Attractor,Behavior}.lean` | R_8 specializations of the judgment overlays. |
| `Atlas/R8/Spacetime.lean` | Opt-in spacetime / causality overlay on R_8. |

### §3.3 R_∞ / profinite (`formal/SSBX/Foundation/RInfty/`)

| File | One-line summary |
|---|---|
| `RInfty/Profinite.lean` | Squaring tower above `R 8`; `L n` finite block; `L_inf` coherent prefixes; `fromStream`/`toStream` bijection to `Stream' (R 8)`; final-coalgebra `coalg`/`L_inf_isFinalCoalgebra`. P5 inverse-limit skeleton (no Mathlib `Cantor` identification yet). |

### §3.4 Atlas/Yi naming overlay (`formal/SSBX/Foundation/Atlas/Yi/`)

| File | One-line summary |
|---|---|
| `Atlas/Yi/YiCore.lean` | Atlas-Yi naming hooks for R-Family carriers. |
| `Atlas/Yi/Bagua.lean` | 8-trigram structure on `R 3`. |
| `Atlas/Yi/Hexagrams.lean` | 64-hexagram structure on `R 6` (= R_3 ⊕ R_3). |
| `Atlas/Yi/Names.lean` | Canonical name table for trigrams / hexagrams. |
| `Atlas/Yi/Operators.lean` | 易 operators (反 / 错 / 综 / etc.) on Bagua. |
| `Atlas/Yi/Positions.lean` | Position structure within hexagrams. |
| `Atlas/Yi/Sheng.lean` | 生 (generation) structure. |
| `Atlas/Yi/Shi.lean` | `Shi := R 2` with V_4 Klein-four-group structure (= 道/已/今/未). P6. |
| `Atlas/Yi/ShiBridge.lean` | Bridge between Shi and other R_2 readings. |
| `Atlas/Yi/Cell128.lean` | Cell128 (Hexagram × Z/2-like) — historical. |
| `Atlas/Yi/Cell256.lean` | Cell256 := Hexagram × Shi (= R_8). |
| `Atlas/Yi/BenZheng.lean` | 本/征 partition on Bagua (P7a content). |
| `Atlas/Yi/Stratify.lean` | Stratification of R_8 cells. |
| `Atlas/Yi/Tradition.lean` | Traditional Yi readings. |
| `Atlas/Yi/WenSpec.lean` | 文 specification overlay. |
| `Atlas/Yi/DaoSource.lean` | 道源 self-referential structure. |
| `Atlas/Yi/YiInstr.lean` | Yi-flavoured instruction set (ISA for hexagram-shaped programs). |
| `Atlas/Yi/Diagonal.lean` | Halting / Gödel diagonal on R_8 ISA (~647 LOC, 0 axiom). §4.10 anchor. |
| `Atlas/Yi/Classical/...` | Classical (algebra/cells/computation/core/diagonal) refinements — multiple modules. |

### §3.5 Wen/MetaInterp (`formal/SSBX/Foundation/Wen/MetaInterp/`)

`Foundation/Wen/MetaInterp/GodelR8.lean` — re-export anchor for the R_8 Gödel/halting
result under the name requested by wen-substrate §4.10. The canonical zero-axiom
diagonal anchor is `Foundation/Atlas/Yi/Diagonal.lean`; the classical
`Atlas/Yi/Classical/Diagonal/GodelLi.lean` overlay is Kleene-conditional rather
than an unconditional trust-base extension.

### §3.6 Wen/Core — RPattern-native interpreter (`formal/SSBX/Foundation/Wen/Core/`)

The canonical `Wen.Core` machine operating on `RPattern 8` (per §3.8). All
files 0 sorry.

| File | One-line summary |
|---|---|
| `Wen/Core/Instruction.lean` | 12-constructor ISA: `nop`, `merge`, `restrict`, `push`, `pop`, `flipBit`, `writeBit`, `xorMask`, `branchBitEq`, `jump`, `halt`, `mergePrior`. Convenience constructors (`pinBit`, `mergeBit`, `forget`, `branchIf{Set,Clear}`). |
| `Wen/Core/State.lean` | State record (pc, cur, history, halted); `State.initial` (cur = `RPattern.empty`), `State.init` (cur = ofFull input); initial-state simp lemmas. |
| `Wen/Core/Machine.lean` | Small-step semantics `executeInstr`; `runFuel`; partial-aware lemmas for `flipBit`, `branchBitEq` (taken/skip/unspec), `mergePrior` (success/empty-history/conflict). |
| `Wen/Core/Examples.lean` | Sample programs + helper combinators. |
| `Wen/Core/ConstraintDemo.lean` | `mergeProg : List RPattern 8 → List Instr`; three operational theorems: `agreementProg_halts`, `conflictProg_halts` (incompatible merge detected), `restrictProg_forgets_bit_2`. ~150 LOC, 0 sorry. |

### §3.7 Wen — conditional UG chain (`formal/SSBX/Foundation/Wen/`)

The six-file Open-Problem-#2 chain (per §4.7bis). All files 0 sorry; combined `0 sorry`.

| File | LOC | Role |
|---|---:|---|
| `Wen/X2Codes.lean` | 303 | `wenCodeUG : UGCandidate` — existence witness. 8 axes, dual/palindrome/compPal involutions, 16/16/16/4/4/0 cardinality theorems, `Sayable`/`Silent` split. |
| `Wen/X2CodesUniqueness.lean` | 221 | `UGCandidate.Hom` / `UGCandidate.Iso` category; `carrier_equiv_wenCode`; `UGCandidateRich` with palindrome+compPal+commutativity; `wenCodeUGRich`. `OpenProblem2.uniqueness_conjecture : Prop` — recorded but **provably impossible without atom hypothesis**; superseded by `face_uniqueness`. |
| `Wen/X2CodesFace.lean` | 246 | `UGCandidateFace` with `dual_is_bitwise_not` axiom; `WenCode.bitsEquiv`; `bridge` + `bridge_dual_comm`; **`theorem face_dual_uniqueness`** (DualIso form); **`theorem face_full_uniqueness`** (full Iso under atom-compatibility); **`theorem face_uniqueness : face_uniqueness_conjecture`** — Open Problem #2 item (d) closed. |
| `Wen/X2CodesNaming.lean` | 277 | `NamingLocus := IsX2 ∩ (IsPalindrome ∪ IsCompPal)`; orbit-decomposition counts; **`theorem seeded_atoms_are_naming_locus`** — atom support = NamingLocus. Item (b) closed. |
| `Wen/X2CodesMinimal.lean` | 283 | `UGCandidateMinimal` with M1/M2/M3 axioms; **`theorem minimal_forces_axes_eight`** — axes=8 forced from minimality. Item (a) closed. |
| `Wen/F2Forcing.lean` | 550 | Stone–Birkhoff chain steps 1–5 unconditional, **including BA-iso refinement** (`step4_birkhoff_BAiso_holds` via self-built `finiteLatticeToCompleteLattice`/`finiteBooleanAlgebraToCompleteBooleanAlgebra`/`finiteBooleanAlgebraToCABA`); `chain_holds`. Item (c) closed. |

---

## §4 Reading guide

Three intended audiences:

* **Foundational claim reviewers** (interested in whether the substrate
  claim holds up): read wen-substrate Parts I–VII and Claim Z (§7.8); then
  read §1 of this document to see which claims have Lean backing and which
  rest on structural argument.

* **Contributors / formalizers** (interested in what to work on next):
  read wen-substrate Part VIII (especially §8.10 priority order and §8.8
  Phase 0 sub-theorems); then read §2 of this document for current per-
  obligation status; pick an item marked `□ open` or `⚠ partial`.

* **Code archeologists** (interested in what is already in the codebase):
  read §3 of this document for the module catalog with one-line summaries.

---

## §5 Honest summary

**What is solid in Lean** (proven, 0-axiom or with explicitly named axioms):

* R_N base carrier (`Foundation/R/Basic.lean`): `R N := Fin N → Bool` with `AddCommGroup`, basis, `Fintype`, decidable equality
* Direct sum (`Foundation/R/DirectSum.lean`): `directSumEquiv` as full bidirectional bijection
* Three bilinear/quadratic layers at the F_2 instance (`Foundation/R/Bilinear.lean`): `dot`, `sigma`, `q`, `arf`, polarization identity
* Squaring tower (`Foundation/R/Squaring.lean`, `SubTower.lean`)
* `R_4 ≅ Mat_{2×2}(F_2)` as an `Equiv` (`Foundation/R4/EndR2.lean`)
* Hom-as-content cardinality (`Foundation/R/Hom.lean`): `card_eq_R : card (LinHom N M) = 2^(N·M)`
* R_∞ inverse-limit skeleton with `Stream' (R 8)` bijection and final-coalgebra property (`Foundation/RInfty/Profinite.lean`)
* 8-trigram naming, 64-hexagram naming, V_4 Shi structure (`Foundation/Atlas/Yi/`)
* Cell256 := Hexagram × Shi (= R_8)
* R_8 Gödel undecidability with 0 axioms in the kernel (`Foundation/Atlas/Yi/Diagonal.lean`, anchored at `Foundation/Wen/MetaInterp/GodelR8.lean`)
* Parametric `RFamily k N` carrier-level skeleton (`Foundation/R/Parametric.lean`)
* **§3.7 operation monism** (`Foundation/R/OperationMonism.lean`): `Sigma X := X × X`, `RTower X k`, `rtower_no_typeclass` — substrate-as-operator layer; additive, non-replacing
* **§3.7.8 distinction-monism layer** (`Foundation/R/Distinction.lean`): primitive `Distinction` type with `o`/`x` constructors, `Distinction ≃ Bool` (classical computational realization), δ-parametric carrier `R' N δ := Fin N → δ`. The substrate is δ-realization-independent; the existing F₂ R-Family is `δ = Bool`. The deepest (fourth) level of the R-Family abstraction tower, sitting below operation monism. ~230 LOC, 0 sorry, 0 axiom.
* **§3.8 RWord substrate** (`Foundation/R/RWord.lean`): arbitrary-rank `o`/`x` words as `R N`; direct-sum splits for `R 10`, `R 12`, `R 16`, and block decompositions.
* **§3.8 RPattern substrate** (`Foundation/R/RPattern.lean`): face lattice of `R N`; `empty` identity, `merge` partial commutative monoid (Phases A–D), `mergeAll` list fold, `support` algebra
* **§3.8 Wen.Core 12-instr RPattern-native interpreter** (`Foundation/Wen/Core/`): ISA + small-step semantics + `ConstraintDemo` operational theorems (agreement / conflict-as-halt / restrict-as-forgetting)
* **§4.7bis conditional UG — Open Problem #2 closed across 6 files, combined `0 sorry`**:
  * existence: `wenCodeUG : UGCandidate` (`Wen/X2Codes.lean`)
  * cardinality + Hom/Iso category + Rich (ℤ/2)² closure (`Wen/X2CodesUniqueness.lean`)
  * face-lattice frame + `theorem face_uniqueness` (DualIso form) + `theorem face_full_uniqueness` (atom-compat hypothesis) (`Wen/X2CodesFace.lean`)
  * naming-density forced from (ℤ/2)² orbits: `theorem seeded_atoms_are_naming_locus` (`Wen/X2CodesNaming.lean`)
  * `theorem minimal_forces_axes_eight` (`Wen/X2CodesMinimal.lean`)
  * Stone–Birkhoff F₂-forcing chain incl. BA-preserving step 4 (`step4_birkhoff_BAiso_holds`) via self-built `finiteLatticeToCompleteLattice`/`...BooleanAlgebraToCABA` Mathlib infrastructure (`Wen/F2Forcing.lean`)
* **Strategy A discharge for T4 / Open Problem #1 (classical-Boolean scope)**: same `F2Forcing.lean` chain

**What is open / programmatic** (stated in wen-substrate but not yet
formalized to the depth claimed):

* Automatic semantic-preservation construction for unrestricted FullGUT /
  unrestricted Claim Z / unrestricted T0. The new `conditional_absolute_full_gut`
  theorem closes the conditional absolute interface, while
  `scoped_coordinate_full_gut` closes only the scoped coordinate package.
* Native category-specific semantics: bundled `HeytAlg` internal-Hom semantics,
  full Hilbert/dagger `FdHilb` semantics, and non-cartesian `Frm`
  tensor/exponential semantics remain open.
* Power/enriched all-semantics: the current enriched files carry scoped bridges
  and supplied data, not a theorem about all V-enriched SMCCs or Power 1999
  universal sayability.
* Arbitrary-satisfier coherent T5: raw `P1P7_Core` gives successor-structural
  coherence; arbitrary `(n,m)` all-split coherence still requires the
  `P1P7_CoherentCore` data, and arbitrary finite-field satisfier derivation is
  still structure-gated.
* D6 exhaustiveness: the concrete F₂ D6 bundle is refuted, but the converse
  claim that every failure of Claim Z falls into the three D6 routes remains
  meta-level open.
* General semantic T1/T2/T3 across all intended formal-system categories. The
  finite F₂ `claim_z_for_F2_nat` / `claim_z_for_F2_holds` item and
  finite/encodable `FormalTranslation` code-naturality packages are closed, but
  they remain scoped code-level results.
* T4 step 3 outside the classical-Boolean scope: non-classical extensions
  (intuitionistic constructive content, quantum at C*-level, modal,
  substructural) — see §8.4.4.

**Net position**: the Lean codebase now proves the conditional-absolute FullGUT
interface through `absolute_conditional_full_gut` /
`conditional_absolute_full_gut`, and the scoped coordinate GUT package through
`ScopedCoordinateFullGUT` / `scoped_coordinate_full_gut`. The remaining
automatic semantic-witness constructors beyond the scoped native certificates,
enriched all-semantics, arbitrary coherent-T5, D6-exhaustiveness, and full
semantic T1/T2/T3 obligations are still open.

This is the honest state of the formalization arm of the wen-substrate
project as of 2026-05-21. For the authoritative per-claim status table, see
[`claim-status-ledger.md`](claim-status-ledger.md) v0.8 (2026-05-21); for
build verification cadence, see [`build-and-verify.md`](build-and-verify.md);
for explicit axiom / partial / opaque boundaries, see
[`trust-boundaries.md`](trust-boundaries.md).

---

*Companion document to [`wen-substrate.md`](wen-substrate.md) v1.4.*
*The two will be revised in tandem.*
