# Handoff: renewal and closure of constraints

7 October 2026. AI-authored handoff from the project thread "How significant is the theory", written at Ren's request at the end of the axiom-free round. Branch `claude/project-thread-upsxp6`. This round's work is commit `ac6539c`, merged to main together with this handoff.

## What the study answers

Ren asked for a formal theory of renewal: one nontrivial theorem saying when a process renews the conditions of its own activity instead of importing organization, stated against Montévil and Mossio's closure of constraints. It serves the research center: how the whole unfolding generates or damages the conditions of its later realization, renewal and correction. Read the [roadmap](../research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-ROADMAP.md), the notes for [Phase 1](../research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE1.md), [Phase 2](../research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE2.md) and [Phase 2b](../research/2026-10-05-generative-foundation-review/root-foundation/RENEWAL-CLOSURE-PHASE2B.md), and the [Lean package README](../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md).

## What is proved, and where

All files are in `experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/`. Core Lean 4.29.1, no Mathlib. `python3 check.py` builds the eleven modules fresh, and its receipt `verification.json` records **219 audits, every one empty**. No declaration depends on any axiom, Lean's `propext`, `Quot.sound` and `Classical.choice` included. The checker now allows none.

| Module | Audits | Content |
|---|---|---|
| `RenewalBasics` | 35 | List and arithmetic facts proved by induction and case analysis, used in place of `omega`, `simp` and core lemmas that carry axioms |
| `RenewalClosure` | 21 | Late activity descends from a realized closed walk of kinds. Acyclic support has a deadline with no supplied rank, which closes the gap `SupportNecessity` named |
| `RenewalAccounting` | 12 | Kinds that open less than their formation demands end whatever their closure, so closure plus openness is not sufficient |
| `RenewalSufficiency` | 32 | A support-closed population that opens enough has a steady configuration and renews forever |
| `RenewalLink` | 16 | On one history, endless liveness needs both a realized closure and an adequate kind |
| `RenewalCharacterization` | 55 | `renewal_closure_theorem` and `renewal_keeping_theorem` with explicit deadlines (see below) |
| `RenewalConfigurations` | 29 | Renewability of whole configurations: never gained along a history without import; a seeded configuration reaches a standing renewal; no goal projection decides it |
| `RenewalPremises` | 19 | The two remaining premises are necessary: finitely many kinds, and positive formation demand for a deadline read from the start |

**Main result.** With finitely many kinds, some history stays live forever with no organization imported after the start exactly when some nonempty population of kinds is closed under support by constraints that outlast a tick and opens over its spans at least what forming it demands. Otherwise every history stops being live by an explicit time. The same holds for keeping a designated kind, such as a means of correction: some history keeps it exactly when a self-renewing population contains it with positive span. Span and rate bounds are read off the list of kinds. Histories may start anywhere, and equality of kinds need not be decidable.

**Downstream.** Rebuilt against this package, the valuation study now has 123 of its 130 results empty (all of `ValuationRenewal`). I regenerated its two affected audit outputs. The other 7, in `LineageInProcess`, wait only on the axiom-free `ResourceContinuation` on branch `claude/project-thread-x1q9hl`. `check_contact_formation.py` still passes (46 modules, 801 audits).

## What is open, and why

1. **The law is supplied.** Kinds, support edges, spans, demands and rates are local-model inputs. Roadmap Phase 4 derives them inside the core. Until then the theorem is conditional on a constraint–flow law, although every premise beyond the law itself is derived, removed or proved necessary (Phase 2b table).
2. **Static cycle extraction.** The aggregate condition is not yet stated as equivalent to the roadmap's two named cases (a cycle of adequate kinds, or an excess kind supported from a cycle) as a statement about the law alone.
3. **Exact characterization of renewable configurations.** `seeded_renewable` is sufficient but not necessary: phase-locked cycles renew without all kinds fresh at once.
4. **Phase 2b items not done.** Mapping the NONINSTRUMENTAL-CONCERN §15 pair into constraint–flow form, and classifying transitions by whether a closure forms, a closure breaks or a reserve crosses its threshold.
5. **Phase 3.** Several required supporters (hyperedges), several flows, and a canonical largest renewing set.
6. **Not claimed.** Which history occurs, that renewal is favorable, and any physical identification.

## Exact next step

Phase 4, deriving the constraint notion inside the core:

1. Fetch main.
2. In a new module beside the package, build a constraint–flow law from a core `Process`. Use `FormationClosure.law_constant` (now on main through the unification thread): a coordinate kept by every fast step changes only through formation events, so constraints and flows are distinguished by timescale within one process, not given as two kinds.
3. Prove the renewal–closure theorem holds for that derived law.
4. Then place the native port. With no closure, the theorem says it ends or imports organization. That should match `port_cannot_continue_indefinitely`, which is only on branch `claude/project-thread-x1q9hl` until Ren merges it. This is also step 3 of the [formal unification handoff](2026-10-07-formal-unification.md).

Keep every new audit empty: `check.py` now fails on any axiom.

## Conventions in force

- **Merge procedure (Ren's standing rule):** commit, merge `origin/main` into the branch, rerun `check.py` and the dependent builds, then push to main.
- **No assumptions or axioms:** derive each input or prove it necessary. Anything that can be neither goes to Ren with the attempts.
- **Avoid `omega`, closing `simp`, `funext` and Iff rewrites.** Use the helpers in `RenewalBasics`. Write pattern matches out case by case when a wildcard's compiled form brings in `propext`, as `freeFormation` does.
- **Monist and relational reading:** derive splits as relations within the one process. Avoid market vocabulary.
