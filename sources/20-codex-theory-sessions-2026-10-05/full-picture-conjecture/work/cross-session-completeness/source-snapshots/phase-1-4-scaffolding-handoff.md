# Phase 1-4 Scaffolding Handoff (Checkpoint 2026-05-18; status updates 2026-05-19, 2026-05-21)

**This document is the companion to**
`docs-next/10_formal_形式/enriched-universal-sayability-plan.md` (the plan).

**Read order**:

1. **Plan §0-3** — understand goal and architecture
2. **This doc §1** — see what was actually built (vs planned)
3. **This doc §2** — locate every placeholder
4. **This doc §3** — pick up where work left off
5. **Plan Appendix C** — cold-start resumption protocol (still valid)

**Live status (2026-05-21)**: see [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 row "V-enriched universal sayability". `T_GUT_Enriched.enriched_universal_sayability_at_Hilbert_statement` now returns the concrete `QuantumToHilbertBridge` and `enriched_universal_sayability_statement` is the scoped ordinary-law bridge `EnrichedUniversalSayabilityScopedStatement`. The headline real Power 1999 §4.5 theorem remains the supplied data, not its construction. The build/jobs counts in §1 below (4191 jobs after PR #70) are point-in-time snapshots from 2026-05-18 and have advanced since.

## Status update (2026-05-19)

The original checkpoint below described Phase 4 as statement-only scaffolding.
That is no longer accurate for the ordinary-law bridge:

- `T_GUT_Enriched.lean` now proves `EnrichedUniversalSayabilityScopedStatement`,
  a non-vacuous scoped bridge from enriched ambient data back to the ordinary
  complete and scope-aware T_GUT law-package theorems.
- `enriched_universal_sayability_at_Hilbert_statement` now returns the concrete
  `QuantumToHilbertBridge`, not `True`.
- `LawvereTheory.lean` now gates the Lawvere theory / finitary monad comparison
  behind explicit `LawvereTheoryFinitaryMonadComparisonData`.
- `Weighted.lean`, `Monad.lean`, and `Finitary.lean` now gate the Phase 1.2-1.4
  universal-property, naturality, monad-law, finitary-preservation, and
  Type-specialisation claims behind explicit supplied law data instead of
  load-bearing `True := trivial` fields.
- `Cotensor.lean` now gates the `V = Type` cotensor bridge behind
  `TypeCotensorStatementData`, including an explicit function-space
  identification and supplied universal-property proof.

The remaining open work is still the hard Power-style V-natural theorem:
real cotensor and weighted-limit universal properties, enriched natural
transformation calculus, enriched finitary monads over filtered conical
colimits, a real category-level Lawvere/monad equivalence, and full
monoidal/dagger/closed `FdHilb`.

## §1 What was built (PR #70, 2026-05-18)

### Files created

```
formal/SSBX/Foundation/Enriched/
├── Cotensor.lean         ~190 LOC  (Phase 1.1)
├── Weighted.lean         ~150 LOC  (Phase 1.2)
├── Monad.lean            ~140 LOC  (Phase 1.3)
├── Finitary.lean          ~95 LOC  (Phase 1.4)
└── Power.lean            ~135 LOC  (Phase 1.5)

formal/SSBX/Foundation/Doctrine/
├── EnrichedLawvereTheory.lean  [modified: supplied data replaces executable sorry]
├── Instance/HilbertEnriched.lean  ~140 LOC  (Phase 3)
└── T_GUT_Enriched.lean         ~150 LOC  (Phase 4)
```

Total: 7 new files, ~1000 LOC scaffolding, all under namespace
`CategoryTheory.Enriched` (for Phase 1) and `SSBX.Foundation.Doctrine.*`
(for Phases 3-4).

### Build state

```
lake build SSBX  →  4191 jobs ✓
```

(Baseline before this work was 4184 jobs. +7 files → +7 jobs.)

### Axiom state

```
#print axioms CategoryTheory.Enriched.Power.theory_monad_equiv
  → does not depend on any axioms

#print axioms SSBX.Foundation.Doctrine.enriched_universal_sayability_statement
  → does not depend on any axioms
```

At the original checkpoint, the new phase declarations were `True := trivial`.
As of the 2026-05-19 update, the Phase 4 enriched bridge and ordinary Lawvere
comparison boundary are no longer fake `True` markers; they require explicit
law-package or comparison data. **The existing 0-axiom 0-sorry framework is
completely unchanged.**

### Sorry state

| File | Sorry count | Status |
|---|---|---|
| `EnrichedLawvereTheory.lean` | 0 executable sorry | `freeVFunctor` / free-forgetful adjunction / Power directions now require explicit data |
| All 7 new files | 0 | Phase 1.2-1.5 and Phase 4 bridges are supplied-data boundaries; remaining real theorem obligations are explicit |

The former `freeVFunctor` sorry is no longer executable proof debt.  It has
been replaced by explicit object-level free-model data, and the ordinary
free/forgetful adjunction is now a projection from explicit
`FreeForgetfulAdjunctionData`; Phase 1.5 must still construct the real
enriched functor and adjunction rather than route through supplied data.

## §2 Placeholder inventory — what each `True` represents

This is the **debt ledger**. Each entry is either a remaining placeholder or a
supplied-data boundary that needs to be replaced with real mathematical content
during phase elaboration.

### Cotensor.lean (Phase 1.1)

| Location | Current boundary | Real content needed |
|---|---|---|
| `hasCotensor_Type_statement_form` | supplied `TypeCotensorStatementData` | The actual `HasCotensor` instance for V = Type (cotensor = function space `X → Y`) |

### Weighted.lean (Phase 1.2)

| Location | Current boundary | Real content needed |
|---|---|---|
| `HasWeightedLimit.universal` | supplied `universalProperty` proof | The actual universal property: for any cone over D with V-weight W, a unique factor through `limit` |
| `cotensor_is_weighted_limit_over_terminal_statement` | supplied `CotensorTerminalWeightedLimitComparisonData` | Theorem: when J = terminal V-category, weighted V-limit = V-cotensor |
| `conical_limit_is_constant_weighted_statement` | supplied `ConicalConstantWeightedLimitComparisonData` | Theorem: when W = constant 𝟙_V, weighted V-limit = conical V-limit |

### Monad.lean (Phase 1.3)

| Location | Current boundary | Real content needed |
|---|---|---|
| `EnrichedNatTrans.naturality` | supplied `naturalityLaw` proof | The V-naturality square: `F.map ≫ eHomWhiskerLeft (app Y) = eHomWhiskerRight (app X) ≫ G.map` |
| `EnrichedMonadStruct.assoc` | supplied `assocLaw` proof | Monad associativity: `T(μ_X) ≫ μ_X = μ_(TX) ≫ μ_X` |
| `EnrichedMonadStruct.left_unit` | supplied `leftUnitLaw` proof | Left unit: `η_(TX) ≫ μ_X = 𝟙` |
| `EnrichedMonadStruct.right_unit` | supplied `rightUnitLaw` proof | Right unit: `T(η_X) ≫ μ_X = 𝟙` |
| `enrichedMonad_Type_specialises_to_Monad_statement` | supplied `EnrichedMonadTypeSpecialisationData` | Theorem: V = Type recovers Mathlib's ordinary `Monad` |

### Finitary.lean (Phase 1.4)

| Location | Current boundary | Real content needed |
|---|---|---|
| `PreservesFilteredConicalColimits` | `Nonempty FilteredConicalColimitPreservationData` | Real preservation predicate over `HasConicalColimit` of filtered shapes |
| `finitary_enriched_monad_Type_specialises_statement` | supplied `FinitaryEnrichedMonadTypeSpecialisationData` | Theorem: V = Type specialisation recovers ordinary finitary monad |

### Power.lean (Phase 1.5) — **the deep one**

| Location | Placeholder | Real content needed |
|---|---|---|
| `theory_induces_monad_statement` | supplied `TheoryMonadData` projection | Real Power 1999 §3 construction remains open. |
| `monad_induces_theory_package` | supplied `MonadTheoryData` projection carrying carrier/category/enrichment/theory data | Real Power 1999 §4 construction remains open. |
| `theory_monad_equiv` | supplied `EnrichedLawvereFinitaryMonadComparisonData` | **THE THEOREM** remains open: the 1-categorical / 2-categorical equivalence with round-trip construction. |
| `power_bridge_for_enriched_lawvere_theory` | supplied comparison-data bridge | Wrapper for downstream code; no fake equivalence claim. |

### EnrichedLawvereTheory.lean (Phase 2)

| Location | Placeholder | Real content needed |
|---|---|---|
| line ~885 `freeVFunctor` | explicit `HasFreeVModels` data | Real V-functor `C ⥤ EnrichedModel V T C` constructed via Phase 1.5's Power 4.5 + V-cocompleteness |
| `freeForgetfulAdjunction` | explicit `FreeForgetfulAdjunctionData` | Construct the supplied ordinary adjunction data from Power 1999 §2 Thm 2.4, then upgrade it to the enriched adjunction |
| `enriched_lawvere_iff_finitary_v_monad` (existing) | supplied `EnrichedLawvereFinitaryMonadComparisonData` | The same boundary as `Power.theory_monad_equiv`, without fabricating Power 4.5. |

### HilbertEnriched.lean (Phase 3)

| Location | Placeholder | Real content needed |
|---|---|---|
| `FinHilbObject` | closed finite-Hilbert-object category with linear maps | Still not the full monoidal/dagger/closed `FdHilb` category |
| `qubit_hilb_object_nonempty` / `TGUTRealisation_Hilb_intent_statement` | non-vacuous object witness | Actual `TGUTRealisationCore FinHilb ℂ` instance remains future work |
| `quantum_to_hilbert_bridge_nonempty` / `quantum_forgetful_to_hilbert_statement` | faithful Pauli-to-qubit endomorphism bridge | Full functor PauliBase-Quantum → monoidal/dagger `FdHilb` remains future work |

### T_GUT_Enriched.lean (Phase 4)

| Location | Placeholder | Real content needed |
|---|---|---|
| `enriched_universal_sayability_statement` | `EnrichedUniversalSayabilityScopedStatement` | Closed scoped bridge: enriched ambient + ordinary law packages recover complete and scope-aware ordinary T_GUT. Full V-natural `EnrichedRealIso` theorem still needs Power 4.5. |
| `enriched_plain_law_packages_specialise_to_scope_aware` | ordinary-law bridge | Closed scoped Type-specialisation bridge. Full enriched-to-ordinary equivalence still needs the real `Type`-as-V coherence theorem. |
| `enriched_universal_sayability_at_Hilbert_statement` | `Nonempty QuantumToHilbertBridge` | Closed concrete Pauli-to-qubit finite-Hilbert-object bridge. Full monoidal/dagger `FdHilb` instantiation remains open. |
| `v0_6_completion_criteria_recorded_statement` | scoped theorem package | Closed record of the scoped enriched bridge plus Hilbert bridge. Full Power-style v0.6 completion remains open. |

## §3 Pick-up protocol (cold start)

### §3.1 Verify nothing regressed

```bash
# From repo root:

# 1. Full SSBX build
lake build SSBX
# Expected: 4191 jobs (or more if other PRs landed), build succeeds

# 2. Existing 0-axiom check (must not regress)
cat > /tmp/verify_baseline.lean << 'EOF'
import SSBX.Foundation.Doctrine.T_GUT
import SSBX.Foundation.Doctrine.Instance.Topological
import SSBX.Foundation.Doctrine.Instance.Heyting
import SSBX.Foundation.Doctrine.Instance.Algebraic
import SSBX.Foundation.Doctrine.Instance.Quantum

#print axioms SSBX.Foundation.Doctrine.TGUTRealisation.universal_sayability
#print axioms SSBX.Foundation.Doctrine.Instance.P3_topological
#print axioms SSBX.Foundation.Doctrine.Instance.P3_heyting
#print axioms SSBX.Foundation.Doctrine.Instance.quantum_universal_sayability_witness
#print axioms SSBX.Foundation.Doctrine.Instance.GUT_A_recovery_at_4
EOF
lake env lean /tmp/verify_baseline.lean
# Expected: each → [propext, Classical.choice, Quot.sound]

# 3. Phase 1-4 scoped bridge check
cat > /tmp/verify_scaffold.lean << 'EOF'
import SSBX.Foundation.Enriched.Power
import SSBX.Foundation.Doctrine.T_GUT_Enriched

#print axioms CategoryTheory.Enriched.Power.theory_monad_equiv
#print axioms SSBX.Foundation.Doctrine.enriched_universal_sayability_statement
EOF
lake env lean /tmp/verify_scaffold.lean
# Expected: no nonstandard axioms; Phase 4 bridge is no longer a fake True marker.
```

### §3.2 Choose where to pick up

The highest-leverage work is **Phase 1.5** (Power 1999 Theorem 4.5). Closing
that unblocks Phase 2 (replace explicit `HasFreeVModels` data with a real functor) and Phase 4 (real
`enriched_universal_sayability`). Suggested phase priority:

1. **Phase 1.5 elaboration** — Power 1999 §§3-4 constructive formalization
   - Real `theory_monad_equiv : EnrichedLawvereTheory V ≃ FinitaryEnrichedMonad V`
   - Likely 1500-3000 LOC of dense category theory
   - Requires real implementations of Phases 1.1-1.4 placeholders too
   - **Estimate: 2-3 months focused work**

2. **Phase 2 close** — once Phase 1.5 has real Power 4.5
   - Replace supplied `HasFreeVModels` / `freeVFunctor` data with proof routing through `theory_monad_equiv`
   - Construct `FreeForgetfulAdjunctionData` from the real Power adjunction and upgrade it to the enriched adjunction
   - **Estimate: 1-2 weeks after Phase 1.5**

3. **Phase 3 elaboration** — FinHilb SMCC
   - Mathlib upstream: bundled `FinHilb` category, Hilbert tensor as
     monoidal structure
   - SSBX-local: `TGUTRealisationCore FinHilb ℂ` instance
   - **Estimate: 1-2 months**

4. **Phase 4 close** — real `enriched_universal_sayability`
   - Replace `True := trivial` with proper V-quantified theorem
   - Prove via Phase 1.5 Power 4.5
   - Instantiate at FinHilb (Phase 3)
   - Verify non-vacuous
   - **Estimate: 1 month after Phases 1.5 + 2 + 3**

### §3.3 If you're going to work on Phase 1.5

This is the deepest sub-task. Recommended reading order:

1. Power, J. 1999. *Enriched Lawvere theories*. TAC 6 no. 7. — read §§1-4 fully
2. Kelly 1982 §§3.7 (cotensors), §5 (V-monads), §6 (V-product-preserving V-functors)
3. Hyland-Power 2007 ENTCS 172. — modern survey
4. Mathlib's existing `Mathlib.CategoryTheory.Monad.*` — for the ordinary case patterns

Then the elaboration plan:

- Replace the supplied `EnrichedNatTrans.naturalityLaw` with the real square
- Replace the supplied `EnrichedMonadStruct.assoc/leftUnitLaw/rightUnitLaw` with real axioms once the whiskering API exists
- Define forward functor `theoryToMonad` (Power 1999 §3 construction)
- Define backward functor `monadToTheory` (Power 1999 §4 construction)
- Prove they are mutual inverses (this is the hard part)

Likely 8-15 PRs to upstream (each Mathlib PR conservatively 100-300 LOC). Multi-month engagement with Mathlib reviewers.

### §3.4 If you're going to work on Phase 4 (assuming Phase 1.5 is done)

Once Phase 1.5 lands real `theory_monad_equiv`:

1. Open `T_GUT_Enriched.lean`
2. Strengthen `enriched_universal_sayability_statement` from the current scoped
   ordinary-law bridge to the real Power-style V-natural theorem:
   - Add proper `[Category V] [SMCC V] [HasCotensors V] ...` instances
   - State the theorem with real quantifier
   - Prove: apply `theory_monad_equiv`, then use free-forgetful adjunction
3. Update `#print axioms` should show `[propext, Classical.choice, Quot.sound]` (no more "does not depend on any axioms")
4. Add a Phase 4.1 follow-up file with the FinHilb instantiation:
   - Import HilbertEnriched.lean (assumed Phase 3 elaborated)
   - Specialise to V = FinHilb
   - Verify non-vacuous

### §3.5 Verification checklist (after any phase elaboration)

```bash
# 1. Build clean
lake build SSBX

# 2. Old 0-axiom theorems still 0-axiom
# (run verify_baseline.lean from §3.1)

# 3. New theorems show real axioms now (not "does not depend on any axioms")
# (run verify_scaffold.lean from §3.1)

# 4. No executable sorry in the enriched bridge files
grep -rn "sorry" formal/SSBX/Foundation/Enriched/ formal/SSBX/Foundation/Doctrine/T_GUT_Enriched.lean

# 5. No new axioms beyond Lean standard 3
grep -rn "^axiom " formal/SSBX/Foundation/
# Expected: 0 results (per [[no-axiom-for-zero-sorry]])
```

## §4 Cross-references

### In this codebase

- **Plan**: `docs-next/10_formal_形式/enriched-universal-sayability-plan.md` (PR #69)
- **E1 closure**: `docs-next/10_formal_形式/E1-rtower-theta-experiment.md` (PR #69) — why we're doing v0.6 (not RH-attack)
- **Phase 1-4 scaffolding code**: this PR (#70)
- **Existing universal_sayability**: `formal/SSBX/Foundation/Doctrine/T_GUT.lean:691`
- **Existing 4 substrates**: `formal/SSBX/Foundation/Doctrine/Instance/{Algebraic,Heyting,Quantum,Topological}.lean`

### Memory entries

- `[[e1-rtower-rh-closed]]` — RH is closed; this work is framework completion not RH attack
- `[[no-axiom-for-zero-sorry]]` — meta-rule: don't axiom out sorries; PR #51 incident
- `[[dont-drop-theorems]]` — meta-rule: don't weaken theorems
- `[[v4-shi-doctrine-out-2026-05-17]]` — V₄ retired; doesn't affect this work
- `[[squaring-tower]]` — R-tower structure; relevant for Phase 3 (Hilb realization)

### External

- Power 1999. *Enriched Lawvere theories*. TAC 6 no. 7. — primary mathematical reference
- Kelly 1982. *Basic Concepts of Enriched Category Theory*. — foundational V-category theory
- Hyland-Power 2007. ENTCS 172. — modern survey
- Mathlib zulip `#category-theory` — for upstream PR coordination

## §5 Honest disclaimers (for the agent picking this up)

1. **This is still not the full enriched theorem.** The scoped ordinary-law bridge is closed, but Plan §10's Power-style V-natural acceptance criteria remain open.

2. **The math is hard.** Power 1999 §§3-4 is roughly 30 pages of dense V-enriched category theory. Formalizing it is a real multi-month research project, not a weekend hack.

3. **Mathlib coordination required.** The lower-level pieces (V-cotensor, weighted V-limits) realistically belong in Mathlib, not SSBX. Plan for upstream PR engagement.

4. **You will not "finish" Phase 1 in one session.** Set realistic milestones — e.g., "elaborate `EnrichedNatTrans.naturality` properly" might be one session's deliverable.

5. **Verify, don't trust.** After each elaboration, run §3.5 checklist. The PR #51 incident (provably-False axiom slipped past local typechecking) is a permanent reminder that build-success ≠ correctness.

6. **Stay honest about state.** If a session can't make a placeholder real, leave it as placeholder with updated doc. Don't game the metric by routing through other placeholders.

---

**End of handoff.**

**Last updated**: 2026-05-18 (immediately after PR #70 scaffolding land).

**Next checkpoint**: when Phase 1.5 elaboration produces real `theory_monad_equiv`. Update this doc's §2 inventory and §3 pick-up plan accordingly.
