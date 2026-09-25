# Full T_GUT Proof Plan

> Status: post-instance-adequacy layer. Structural universal sayability is archived as an intermediate milestone; the current generic theorem is scoped by intrinsic adequacy plus explicit transport, semantic, and ops predicates. The five primary Type-level instances now prove intrinsic `IsAdequate`.
>
> Scope: `formal/SSBX/Foundation/Doctrine/T_GUT.lean` first, then per-instance files under `formal/SSBX/Foundation/Doctrine/Instance/`.
>
> Doctrine guardrail: this plan keeps the proof R-family / carrier-parametric and keeps Atlas or instance-specific semantic names out of the core.
>
> **Status authority (2026-05-21)**: this plan describes phase intent and milestone checklists; for the live theorem-by-theorem status (scoped vs closed vs open) and the "scoped vs absolute" wording policy, see [`claim-status-ledger.md`](claim-status-ledger.md) v0.8. Current closures relevant to this plan: `universal_sayability` (`Core`), `universal_sayability_structural_of_adequate` (archived), `universal_sayability_core_full`, and `universal_sayability_complete_of_adequate` are all closed; 5 primary Type-level SMCC instances (Algebraic, Witt, Heyting, Quantum, Topological) prove intrinsic `IsAdequate` and ship complete law-package theorems with scoped non-identity ops comparison targets; 3 ops (`square_mor`, `relate_mor`, `modal_V4_mor`) are factored out of the core. Open items beyond this plan's scope: full Power 1999 §4.5 V-natural theorem ([`enriched-universal-sayability-plan.md`](enriched-universal-sayability-plan.md)), bundled `HeytAlg` CCC / full `FdHilb` / non-cartesian `Frm` tensor-exponential semantics, and the Heisenberg-Weyl ↔ Cell256 bridge ([`heisenberg-weyl-narrative.md`](heisenberg-weyl-narrative.md)).

## 0. Current state

The current Lean development now has the core API, the scoped full-core carrier/generator theorem, and a split current law package:

- `TGUTLaw` is the syntactic law tag type and now includes the local carrier law `compose_tensor_inverse`, tensor-unit and tensor-associativity law families, and explicit canonical transport laws for `hom_mor`, `atom_3_mor`, and `wedderburn_4_mor`.
- `TGUTPresentation.laws` is a predicate `TGUTLaw → Prop`, so it can represent all indexed law families, not just a finite sample list.
- `TGUTPresentation.standard` now selects only intrinsic laws expected to be satisfiable by the real instance files. Canonical comparison, semantic Hom/Wedderburn, and ops laws are split into `canonicalTransport`, `semantic`, and `opsCoherence`.
- `TGUTRealisationCore` contains the universal carrier data: `R`, `R_unit`, `R_gen`, `R_tensor`, `compose_mor`, `hom_mor`, `atom_3_mor`, and `wedderburn_4_mor`.
- `TGUTRealisation` extends the core with the instance-specific operations `square_mor`, `relate_mor`, and `modal_V4_mor`.
- `Satisfies` is non-vacuous for `atom_3_involutive`, `compose_tensor_inverse`, the tensor coherence laws, core-generator canonical transport laws, compose associativity/unit laws, Hom/curry semantics, Wedderburn/end semantics, square/diagonal semantics, and modal idempotent-factorisation semantics.
- `HomCurryCoherence` uses represented Hom data: a local `homCarrier`, an iso `R (N*M) ≅ homCarrier`, an evaluation map, and compatibility with `hom_mor`.
- `WedderburnEndCoherence` uses represented End/action data: a local `endCarrier`, an iso `R 4 ≅ endCarrier`, action/unit/composition maps, action laws, and compatibility with `wedderburn_4_mor`.
- `SquareDiagonalCoherence` and `ModalV4IdempotentCoherence` make the ops laws explicit without claiming a generic canonical ops target.
- `CoreRealIso`, `CoreStructuralCoherence`, `CoreTensorCoherence`, and `CoherentCoreRealIso` give the archived structural proof targets.
- `CoreGeneratorCoherence` and `FullCoherentCoreRealIso` give the current full-core carrier/generator proof target.
- `CoreRealisationHom`, `RealisationHom`, and the forgetful maps from full coherent isomorphisms give a non-vacuous naturality API for realisation morphisms; identity and composition laws are now formalized for the morphism records. Category/functor instances remain optional future packaging.
- `TypeCatRFamily.lean` factors the shared finite-coordinate `Type` tensor split and proves the tensor-unit, tensor-associativity, compose-unit, and compose-associativity laws used by the primary Type-level instances.
- `OpsCoherence` and `FullCoherentRealIso` state the per-instance ops-isomorphism target; no generic theorem produces them because ops are not canonical in arbitrary SMCCs.
- `componentIso` constructs the layerwise carrier isomorphism from any core realisation to the canonical tensor-power realisation.
- `universal_sayability_structural_of_adequate` is archived as the completed structural milestone: it requires only `M.IsAdequate`, derives `CoreTensorCoherence`, and proves `CoreStructuralCoherence` for `componentIso`.
- `universal_sayability_core_full` now requires `M.IsAdequate` plus `M.HasCanonicalTransport` and returns `FullCoherentCoreRealIso`, combining structural coherence with core-generator coherence.
- `universal_sayability_complete_of_adequate` now requires `M.IsAdequate`, `M.HasCanonicalTransport`, `M.HasSemanticCoherence`, and `M.HasOpsCoherence`; it bundles the complete current generic law package when all four predicates are supplied.

The current development is therefore **complete for the scoped generic T_GUT proof package as currently formalized**. The completed part is:

- adequacy projects to non-vacuous tensor-unit and tensor-associativity laws;
- those laws prove `CoreStructuralCoherence` for `componentIso`;
- `universal_sayability_structural_of_adequate` needs only `M.IsAdequate` and is retained as an archived structural theorem;
- canonical transport projects to non-vacuous Hom/Atom/Wedderburn transport laws;
- compose generator coherence is derived from `compose_tensor_inverse` plus structural tensor coherence;
- `universal_sayability_core_full` needs `M.IsAdequate` plus `M.HasCanonicalTransport`;
- `universal_sayability_complete_of_adequate` packages intrinsic, transport, semantic, and ops predicates without pretending they all follow from intrinsic adequacy.

What remains open is **semantic strengthening beyond the scoped TypeCat coordinate packages**: the algebraic, Witt, Heyting, quantum, and topological Type-level instances now prove `IsAdequate` for the intrinsic standard laws, use shared coordinate reversal for `atom_3_mor`, provide represented Hom/Wedderburn witnesses, and prove complete law-package theorems. Their direct non-identity ops comparison targets are also closed where meaningful: algebraic/F₂ Bool, Witt coefficient streams, Heyting/Topological Bool coordinates, and quantum Pauli bit pairs. The remaining obligations are the stronger category-specific upgrades: p-adic/Λ-ring Witt semantics, bundled `HeytAlg` internal Hom semantics, the next Hilbert ladder beyond the finite-coordinate tensor/unit reindexing, coherence, and dagger/tensor boundaries (naturality, then bundled `FdHilb`), non-cartesian `Frm` tensor/exponential semantics, and any later universal theorem over arbitrary SMCC ops. The legacy `RealIso.coherent` field is also still a placeholder, so consumers that need non-vacuous coherence should use `CoherentCoreRealIso`, `FullCoherentCoreRealIso`, `CoreRealisationHom`, `RealisationHom`, or `CompleteUniversalSayability`.

## 1. Final theorem target

The archived structural theorem, now completed and no longer the headline target, is:

```lean
theorem universal_sayability_structural_of_adequate
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate) :
    Nonempty
      (CoherentCoreRealIso M.toTGUTRealisationCore (canonical δ))
```

This theorem says: every adequate T_GUT realisation has a structurally coherent carrier isomorphism to the canonical tensor-power realisation. It is kept as an audit boundary and compatibility layer.

The current headline core theorem is:

```lean
theorem universal_sayability_core_full
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport) :
    Nonempty
      (FullCoherentCoreRealIso M.toTGUTRealisationCore (canonical δ))
```

This theorem adds core-generator transport for `compose`, `hom`, `atom_3`, and `wedderburn_4`, but only for comparison-compatible realisations.

The current headline generic law theorem is:

```lean
theorem universal_sayability_complete_of_adequate
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate)
    (hTransport : M.HasCanonicalTransport)
    (hSemantic : M.HasSemanticCoherence)
    (hOps : M.HasOpsCoherence) :
    Nonempty (CompleteUniversalSayability M)
```

The later per-instance full theorem should additionally prove `FullCoherentRealIso` with `OpsCoherence` for `square`, `relate`, and `modal_V4` against an instance-specific ops target.

Do not read these generic theorems themselves as proving transport, semantic, or ops-isomorphism predicates for any concrete instance. They say what follows once the relevant predicates are supplied; concrete intrinsic `IsAdequate` is now supplied separately for the five primary Type-level instances.

## 2. Invariants and non-negotiable rules

1. **No fake proof by `True` for core content.**
   If a law has no real statement yet, name the blocker as a structure or leave an explicit hypothesis.

2. **No new axioms to close proof gaps.**
   `sorry` is visible debt; an axiom silently pollutes the trust base.

3. **Core and ops stay separated.**
   The core proof uses `R_unit`, `R_gen`, `R_tensor`, `compose_mor`, `hom_mor`, `atom_3_mor`, and `wedderburn_4_mor`. It must not require `square_mor`, `relate_mor`, or `modal_V4_mor`.

4. **Adequacy must mean all standard law instances.**
   Keep `TGUTPresentation.laws : TGUTLaw → Prop`; do not regress to a finite law list.

5. **Make failure modes explicit.**
   If a theorem cannot be proved from current data, add the missing law or missing semantic data rather than weakening the theorem.

## 3. Phase A — make tensor coherence law-level data (completed)

### Goal

Make `CoreTensorCoherence` derivable from adequacy.

### Why

`componentIso` is recursively built through `R_tensor 1 k`. To prove it commutes with arbitrary `R_tensor n m`, the chosen tensor decomposition must satisfy unit and associativity coherence. Raw `TGUTRealisationCore` does not guarantee this.

### Tasks

1. Add law constructors to `TGUTLaw`:

```lean
| tensor_unit_left : ℕ → TGUTLaw
| tensor_unit_right : ℕ → TGUTLaw
| tensor_assoc : ℕ → ℕ → ℕ → TGUTLaw
```

2. Include all three law families in `TGUTPresentation.standard.laws`.

3. Add concrete `Satisfies` clauses matching `CoreTensorCoherence`:

```lean
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
```

4. Prove projection theorem:

```lean
theorem core_tensor_coherence_of_adequate
    (M : TGUTRealisation C δ) (h : M.IsAdequate) :
    CoreTensorCoherence M.toTGUTRealisationCore
```

### Acceptance criteria

- `core_tensor_coherence_of_adequate` is proven with no `sorry` and no new axioms.
- The proof is a direct constructor proof using `h (.tensor_unit_left n) trivial`, etc.

### Status

Completed by the structural-core milestone. Keep this section as the audit record for the laws that now feed the structural theorem.

## 4. Phase B — prove `componentIso` structural coherence (completed)

### Goal

Prove:

```lean
noncomputable theorem componentIso_structural_coherent
    (δ : C) (M : TGUTRealisationCore C δ)
    (hM : CoreTensorCoherence M) :
    CoreStructuralCoherence
      (M := M)
      (N := canonical δ)
      (componentIso δ M)
```

### Helper lemmas

Add small local lemmas before the main theorem:

```lean
@[simp] theorem componentIso_zero_hom
    (δ : C) (M : TGUTRealisationCore C δ) :
    (componentIso δ M 0).hom = M.R_unit.hom := rfl
```

Add successor unfolding lemmas for `componentIso`, and matching unfolding lemmas for:

- `tensorPow_add δ 0 m`
- `tensorPow_add δ (k + 1) m`

These lemmas should expose definitions without relying on brittle large `simp` calls.

### Proof structure

1. `unit_hom`:
   - unfold `componentIso 0`;
   - reduce to `M.R_unit.hom ≫ Iso.refl.hom = M.R_unit.hom`.

2. `gen_hom`:
   - unfold `componentIso 1`;
   - use `hM.tensor_unit_right 1`;
   - use naturality of the right unitor for `M.R_gen.hom`.

3. `tensor_hom`:
   - induct on the first index `n`;
   - base `n = 0`: use `hM.tensor_unit_left m` and the definition of `tensorPow_add δ 0 m`;
   - step `n + 1`: use `hM.tensor_assoc 1 n m`, rewrite the recursive middle component by the induction hypothesis, and close with the recursive definitions of `componentIso` and `tensorPow_add`.

### Acceptance criteria

- `componentIso_structural_coherent` is proven with no additional assumptions beyond `CoreTensorCoherence M`.
- No generator laws are used in this proof.

### Status

Completed by the structural-core milestone. This is the proof boundary: it establishes unit/generator-carrier/tensor structural coherence, not generator-morphism coherence.

## 5. Phase C — remove explicit structural hypothesis from adequacy theorem (completed)

### Goal

Record the completed replacement of the adequacy bridge that previously asked for `hStructural`, with a theorem deriving it from adequacy.

### Implementation

```lean
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
```

### Acceptance criteria

- No explicit `CoreStructuralCoherence` argument remains.
- The theorem is the first real structural universal-sayability theorem.

### Status

Completed by the structural-core milestone. Future work must not reopen this theorem by adding generator or ops obligations to it; those belong in separate full-core and per-instance structures.

## 6. Phase D — split structural and generator coherence (completed)

### Goal

Keep `CoreStructuralCoherence` focused on `R_unit`, `R_gen`, and `R_tensor`; add a separate predicate for core generator commuting squares.

### New structure

```lean
structure CoreGeneratorCoherence
    {δ : C}
    {M N : TGUTRealisationCore C δ}
    (iso : ∀ n, M.R n ≅ N.R n) : Prop where
  compose_hom : ∀ n m, ...
  hom_hom : ∀ n m, ...
  atom_3_hom : ...
  wedderburn_4_hom : ...
```

The exact fields should be commuting-square equations of the form:

```lean
(iso source).hom ≫ N.generator = M.generator ≫ (iso target).hom
```

For endomorphism-like generators, source and target are the same layer. For tensor-source generators such as `compose_mor`, use the induced tensor map on the source.

For the canonical target, the intended shapes are:

```lean
-- compose
((iso n).hom ⊗ₘ (iso m).hom) ≫ N.compose_mor n m =
  M.compose_mor n m ≫ (iso (n + m)).hom

-- hom
(iso (n * m)).hom ≫ N.hom_mor n m =
  M.hom_mor n m ≫ (iso (n * m)).hom

-- atom_3
(iso 3).hom ≫ N.atom_3_mor =
  M.atom_3_mor ≫ (iso 3).hom

-- wedderburn_4 carrier map
(iso 4).hom ≫ N.wedderburn_4_mor.hom =
  M.wedderburn_4_mor.hom ≫ (iso 4).hom
```

### Acceptance criteria

- `CoreGeneratorCoherence` has no ops fields.
- It contains no `True` fields.
- Each field is backed by a named, non-vacuous law/projection theorem from the relevant split predicate.
- If a generator is not yet provable, leave the full theorem blocked or requiring an explicit hypothesis rather than weakening the field.

### Status

Completed. `CoreGeneratorCoherence` is defined in `T_GUT.lean` with concrete fields for `compose_mor`, `hom_mor`, `atom_3_mor`, and `wedderburn_4_mor`; ops fields remain outside the core.

## 7. Phase E — prove compose generator coherence (completed)

### Goal

Use `compose_tensor_inverse` and `CoreStructuralCoherence.tensor_hom` to show that the `compose` generator commutes with the canonical realisation.

### Tasks

1. Split the existing compose inverse projection into two rewrite-friendly lemmas if the proof needs them:

```lean
theorem tensor_hom_compose_of_adequate ...
theorem compose_tensor_hom_of_adequate ...
```

2. Prove the compose field of `CoreGeneratorCoherence`.

3. Expose the result through the aggregate generator-coherence theorem:

```lean
theorem componentIso_generator_coherent_of_adequate ...
```

### Proof idea

`compose_mor` is the inverse of `R_tensor`. Once `componentIso` commutes with `R_tensor`, it also commutes with the inverse maps. The canonical `compose_mor` is already `(tensorPow_add δ n m).inv`.

### Acceptance criteria

- `compose_hom` is proven from:
  - `CoreStructuralCoherence.tensor_hom`,
  - `compose_tensor_inverse_of_adequate`,
  - category associativity and iso cancellation.

### Status

Completed inside `componentIso_generator_coherent_of_adequate`. The implementation did not need standalone compose helper lemmas; the compose field is proved directly from `compose_tensor_inverse_of_adequate`, `hStructural.tensor_hom`, associativity, and iso cancellation.

## 8. Phase F — remaining core generator transport laws (completed for transport)

### Goal

Close the remaining full-core generator commuting squares by adding explicit, non-vacuous transport laws and adequacy projection theorems.

This phase is about **generator transport along the component iso**. It is not, by itself, the deeper semantic interpretation of Atom, Hom/curry, or Wedderburn/End. Those deeper semantics are future semantic strengthening unless implemented and wired into the theorem statements.

### 8.1 `atom_3`

Current law:

```lean
M.atom_3_mor ≫ M.atom_3_mor = 𝟙 (M.R 3)
```

This only says involutive. It does not by itself say the atom map transports to the canonical atom map.

Add a stronger non-vacuous law if needed:

```lean
| atom_3_transport : TGUTLaw
```

with satisfaction:

```lean
(componentIso δ M.toTGUTRealisationCore 3).hom ≫ (canonical δ).atom_3_mor =
  M.atom_3_mor ≫ (componentIso δ M.toTGUTRealisationCore 3).hom
```

If this is too specific to canonical comparison, formulate it as naturality or a presentation equation that determines `atom_3_mor` uniquely.

Then expose:

```lean
theorem atom_3_transport_of_adequate ...
```

### 8.2 `hom_mor`

`hom_NM_curry_compat` is no longer `True`; it now requires `Nonempty (HomCurryCoherence M n m)`.

For the full-core commuting square, first add a non-vacuous transport law:

```lean
| hom_transport : ℕ → ℕ → TGUTLaw
```

with satisfaction shaped like:

```lean
(componentIso δ M.toTGUTRealisationCore (n * m)).hom ≫
    (canonical δ).hom_mor n m =
  M.hom_mor n m ≫
    (componentIso δ M.toTGUTRealisationCore (n * m)).hom
```

Then expose:

```lean
theorem hom_transport_of_adequate ...
```

The semantic package is implemented as represented Hom data:

```lean
homCarrier : C
homIso : M.R (n * m) ≅ homCarrier
eval : M.R n ⊗ homCarrier ⟶ M.R m
```

### 8.3 `wedderburn_4`

For the full-core commuting square, first add a non-vacuous carrier-transport law:

```lean
| wedderburn_4_transport : TGUTLaw
```

with satisfaction shaped like:

```lean
(componentIso δ M.toTGUTRealisationCore 4).hom ≫
    (canonical δ).wedderburn_4_mor.hom =
  M.wedderburn_4_mor.hom ≫
    (componentIso δ M.toTGUTRealisationCore 4).hom
```

Then expose:

```lean
theorem wedderburn_4_transport_of_adequate ...
```

The previous `pending : True` placeholder has been replaced. `WedderburnEndCoherence` now requires represented End/action data:

```lean
endCarrier : C
endIso : M.R 4 ≅ endCarrier
action : M.R 2 ⊗ endCarrier ⟶ M.R 2
unit : 𝟙_ C ⟶ endCarrier
comp : endCarrier ⊗ endCarrier ⟶ endCarrier
```

It also requires identity-action and composition-action compatibility laws.

### Acceptance criteria

- No core generator field is proven from mere involutivity, mere existence of an iso, or a `True` placeholder.
- Each remaining generator field has a non-vacuous adequacy projection theorem.
- Missing semantic representations are explicit future debt, not hidden inside the full-core generator theorem.

### Status

Completed for carrier transport and represented coordinate semantics. The implemented law constructors are named `hom_canonical_transport`, `atom_3_canonical_transport`, and `wedderburn_4_canonical_transport`; their adequacy projection theorems feed `componentIso_generator_coherent_of_adequate`. The five primary TypeCat instances provide represented Hom/curry and Wedderburn/End witnesses. Stronger category-specific semantic upgrades remain future work.

## 9. Phase G — full core coherent isomorphism (completed)

### Goal

Bundle structural and generator coherence.

### New structure

```lean
structure FullCoherentCoreRealIso
    {δ : C} (M N : TGUTRealisationCore C δ) where
  iso : ∀ n, M.R n ≅ N.R n
  structural_coherent : CoreStructuralCoherence (M := M) (N := N) iso
  generator_coherent : CoreGeneratorCoherence (M := M) (N := N) iso
```

### Theorem

```lean
theorem universal_sayability_core_full
    (δ : C) (M : TGUTRealisation C δ)
    (hAdequate : M.IsAdequate) :
    Nonempty
      (FullCoherentCoreRealIso M.toTGUTRealisationCore (canonical δ))
```

### Acceptance criteria

- The theorem has no structural-coherence hypothesis.
- The theorem relies on `M.IsAdequate` for structural/compose coherence and `M.HasCanonicalTransport` for the comparison-specific generator squares.
- Any still-unproved generator law blocks this theorem honestly.
- The theorem does not claim Hom/curry or Wedderburn/End semantic adequacy unless those fields are present in `FullCoherentCoreRealIso`.

### Status

Completed as a scoped comparison theorem. `universal_sayability_core_full` requires `M.IsAdequate` plus `M.HasCanonicalTransport` and returns `FullCoherentCoreRealIso M.toTGUTRealisationCore (canonical δ)`.

## 10. Phase H — ops/per-instance coherence

The operations `square_mor`, `relate_mor`, and `modal_V4_mor` are intentionally outside `TGUTRealisationCore` because they have no canonical universal definition in an arbitrary SMCC.

Add a separate structure:

```lean
structure OpsCoherence
    {δ : C}
    (M N : TGUTRealisation C δ)
    (iso : ∀ n, M.R n ≅ N.R n) : Prop where
  square_hom : ∀ n, ...
  relate_hom : ∀ n m, ...
  modal_V4_hom : ...
```

Then prove per-instance theorems in:

- `formal/SSBX/Foundation/Doctrine/Instance/Algebraic.lean`
- `formal/SSBX/Foundation/Doctrine/Instance/Quantum.lean`
- `formal/SSBX/Foundation/Doctrine/Instance/Topological.lean`
- other instance files as they mature

### Acceptance criteria

- No general theorem over arbitrary SMCC claims canonical `square`, `relate`, or `modal_V4` coherence.
- Each instance theorem states and uses the exact extra structure that makes those operations meaningful.

## 11. Phase I — documentation and doctrine sync

Update documentation after each completed proof layer:

1. `docs-next/10_formal_形式/claim-status-ledger.md`
2. `docs-next/10_formal_形式/code-promise-gap.md`
3. `docs-next/10_formal_形式/wen-substrate/08-obligations.md` if the obligation status changes
4. Historical foundation docs such as `wen-algebra.md`, `v4-foundation.md`, `r4.md`, and `r8.md` only when they contain stale forward claims that need qualification
5. Do not cite or revive `史/` material for new doctrine.

Each doc update should say exactly which theorem is formalized and which obligations remain.

## 12. Build and verification plan

Because the formal build is expensive, use staged checks:

1. After small law/API edits:

```bash
lake env lean formal/SSBX/Foundation/Doctrine/T_GUT.lean
```

2. After completing a phase theorem:

```bash
lake build SSBX.Foundation.Doctrine.T_GUT
```

3. After touching instance files:

```bash
lake build SSBX.Foundation.Doctrine
```

4. Before final PR:

```bash
lake build
```

Do not run full builds repeatedly after purely documentary edits.

For document-only audits, no build is required. For the completed full-core Lean change, `lake build SSBX.Foundation.Doctrine.T_GUT` passed. For the instance-adequacy layer, the staged build of `T_GUT` plus the five primary instance targets passed.

## 13. Milestone checklist

### Structural core milestone

- [x] Add tensor coherence law constructors.
- [x] Add concrete `Satisfies` cases for tensor coherence.
- [x] Prove `core_tensor_coherence_of_adequate`.
- [x] Add helper lemmas for `componentIso` and `tensorPow_add`.
- [x] Prove `componentIso_structural_coherent`.
- [x] Remove explicit `hStructural` from `universal_sayability_structural_of_adequate`.

### Full core milestone

- [x] Define `CoreGeneratorCoherence` with concrete compose/hom/atom/wedderburn fields.
- [x] Prove compose generator coherence from `compose_tensor_inverse` plus structural coherence.
- [x] Add/prove non-vacuous `atom_3` transport projection.
- [x] Add/prove non-vacuous `hom_mor` transport projection.
- [x] Add/prove non-vacuous `wedderburn_4_mor` transport projection.
- [x] Prove `componentIso_generator_coherent_of_adequate` from those projections.
- [x] Define `FullCoherentCoreRealIso`.
- [x] Prove `universal_sayability_core_full`.

### Future semantic-strengthening milestone

- [x] Replace `hom_NM_curry_compat : True` with real closed-structure / curry semantics, or derive it from implemented closed data.
- [x] Replace `WedderburnEndCoherence.pending` with real `End(R 2)` carrier/action fields.
- [ ] Strengthen `atom_3` beyond transport if the intended atom semantics require uniqueness/classification data.
- [ ] Decide which semantic-strengthening fields, if any, belong in a later theorem beyond `universal_sayability_core_full`.

### Complete generic law milestone

- [x] Replace `hom_NM_curry_compat : True` with real local closed-structure / curry witness data.
- [x] Replace `WedderburnEndCoherence.pending` with internal-end carrier/action witness data.
- [x] Replace `square_diagonal` satisfaction placeholder with `SquareDiagonalCoherence`.
- [x] Replace `modal_V4_idempotent` satisfaction placeholder with `ModalV4IdempotentCoherence`.
- [x] Replace `compose_assoc` and compose unit placeholders with concrete equations.
- [x] Prove projection theorems for the strengthened laws.
- [x] Define `CompleteUniversalSayability`.
- [x] Prove `universal_sayability_complete_of_adequate`.

### Ops/per-instance milestone

- [x] Define `OpsCoherence`.
- [x] Define `FullCoherentRealIso`.
- [x] Add shared TypeCat finite-coordinate coherence helper for intrinsic tensor/compose laws.
- [x] Prove intrinsic `IsAdequate` for the algebraic, Witt, Heyting, quantum, and topological Type-level instances.
- [x] Replace constant placeholder `relate_mor` definitions in the algebraic, Witt, Heyting, quantum, and topological Type-level instances with total coordinate maps.
- [x] Prove the split `HasOpsCoherence` square/modal laws for those five instances.
- [x] Prove algebraic/F₂ ops equivalence (`OpsCoherence` / `FullCoherentRealIso`) against a non-identity Bool-coordinate comparison target.
- [x] Prove Witt ops equivalence against a non-identity coefficient-stream comparison target.
- [x] Prove Heyting and Topological ops equivalence against non-identity Bool-coordinate comparison targets.
- [x] Prove quantum ops equivalence against a non-identity bit-pair comparison target.
- [x] State the primary per-instance complete law-package roster in `PrimaryComplete.lean`.

## 14. Recommended implementation order

1. Decide whether the canonical atom should remain identity or be upgraded to a reversal-compatible canonical map.
2. Prove `HasCanonicalTransport` only for instances whose generator choices genuinely transport to canonical.
3. Prove `HasSemanticCoherence` only in categories where the Hom/Wedderburn semantics are actually modeled.
4. Prove `FullCoherentRealIso` per instance against an instance-specific ops target.
5. Sync the canonical status docs after each proof layer.

## 15. Definition of done

The structural core is done when:

1. `universal_sayability_structural_of_adequate` requires only `M.IsAdequate` and no explicit structural hypothesis.
2. The structural theorem includes only unit, generator-carrier, and tensor coherence.

Full-core generator coherence can be advertised only when:

1. `universal_sayability_core_full` states both required hypotheses: `M.IsAdequate` and `M.HasCanonicalTransport`.
2. `FullCoherentCoreRealIso` includes real `CoreGeneratorCoherence`.
3. Every core `Satisfies` case used by that theorem is non-vacuous.
4. Each non-compose generator field is supplied by an explicit projection theorem from `M.HasCanonicalTransport`; compose is derived from intrinsic adequacy.
5. No new axioms are introduced.
6. Any remaining `sorry` is documented as future infrastructure debt, not hidden in a theorem claimed as complete.

Generic T_GUT can be advertised only as: intrinsic adequacy plus explicit transport, semantic, and ops predicates yield the full current law package. The five primary Type-level instances can now be advertised as intrinsically adequate under `TGUTPresentation.standard`; any stronger concrete claim still requires the separately claimed transport, semantic, and ops coherence predicates.
