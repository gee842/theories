# Handoff: how valuation develops (valuation-development study)

7 October 2026. AI-authored handoff from the project thread "How valuation develops", written at Ren's request at the end of the axiom-free round. Branch `claude/project-thread-mx6miu`; this round's last commit on main before the handoff is `6ca9789`.

## Resume state (wrap-up, 7 October 2026, 09:50 UTC)

The study stopped at a continuable position: no proof is half-finished and nothing is uncommitted. Ren asked every thread to wrap up.

- **Branch:** `claude/project-thread-mx6miu`, identical to `main` after this handoff commit.
- **Verified on:** main at `5b109655`, merged into the branch. All eight valuation modules and their imports (18 modules) were rebuilt from scratch, and the eight `*Audit.lean` files were rerun:
  - 130 results;
  - 118 of them print "does not depend on any axioms";
  - no `sorryAx`, `native_decide` or errors.
- **Nothing upstream has changed:** `ResourceContinuation.lean` and `lean/conditional/renewal/` were not touched on main between `2acd0f1` and `5b109655`, so the 12 inherited results are unchanged.
- **To resume:** run the builder with core Lean 4.29.1 (`/opt/lean/lean-4.29.1-linux/bin` on `PATH`). It must resolve imports across `experiments/`, because `LineageInProcess` and `ValuationRenewal` import the core modules. Then follow "Exact next step" below.
- **A new agent picking this up** should read, in order:
  1. this file;
  2. §18 of the argument (the input-status table);
  3. `AxiomFree.lean` (the proof style that keeps results axiom-free).

## What the study answers

How organized processes form and revise their own selective dispositions (operational valuation) without an analyst supplying a reward function. Read the [argument](../research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md) (§§1–19), the [current formulation](../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/VALUATION-DEVELOPMENT.md) and the [formal companion](../../experiments/valuation-development/README.md).

## What is proved, and where

There are 130 core-Lean 4.29.1 results in `experiments/valuation-development/lean/`. Each module has an `*Audit.lean` file and a saved `*audit-output.txt`.

| Module | Results | Content |
|---|---|---|
| `AxiomFree.lean` | lemmas | Nat and List lemmas proved by structural induction, so that no proof needs `propext` or `Quot.sound` |
| `ValuationDevelopment.lean` | 33 | U1–U6: retention, unreached extension, prediction/scoring trade-off, coupling and proxy capture, convergence and divergence, separable capacities (§§1–11) |
| `ClosedLoopValuation.lean` | 11 | C1: under contraction, amplification needs a selection difference; witnesses (§12) |
| `ExplorationCoverage.lean` | 11 | E1: coverage, whatever its source, equalizes estimates; curiosity and optimism witnesses (§13) |
| `ValuationCompletion.lean` | 15 | Changing worlds, noise floor, interaction, level-5 route revision, level-6 coupling formed by pairing (§14) |
| `ValuationBridges.lean` | 33 | Chance: finite weighted laws, escape bound, coverage with probability ≥ 1 − (r/q)^n, noisy lock-in. Lineage: ledgers closed under succession and division (§16) |
| `LineageInProcess.lean` | 14 | The ledger is an instance of the core support law (`AccountLaw`, U1), and the lineage bound is its prefix bound. The renewal channel process obeys U1; lineage and renewal–closure hold on one process; persistence is decided by population membership (§17) |
| `ValuationRenewal.lean` | 7 | A valuation in the process decides what is formed. Some valuation keeps a kind forever exactly when a self-renewing population contains it. The contraction hypothesis is necessary (§18) |
| `OneProcess.lean` | 6 | Organization/world and one center/another are cuts of one joint process, and neither cut is privileged (§19) |

**Axioms.** 118 of the 130 results print "does not depend on any axioms". The other 12 (8 in `LineageInProcess`, 4 in `ValuationRenewal`) inherit `propext` and `Quot.sound` only from the shared theorems they call, which are listed below; their own proof steps are axiom-free. There are no custom axioms, no `sorry` and no `native_decide`.

**Inputs.** §18 has a table classifying every input of the study: derived from the process, proved necessary by a countermodel, or quantified over. The support relation's decision procedure is passed in as model data, `[DecidableRel law.edge]`, so no axiom is used.

## What is open, and why

1. **The last 12 results are not yet axiom-free.** Their axioms come from:
   - `support_trace_balance`, `execution_interval_balance`, `unbounded_demand_requires_unbounded_credit` and `interval_total_unit_bound` in `lean/conditional/ResourceContinuation.lean`. The dependency-map thread made this file axiom-free on branch `claude/project-thread-x1q9hl`, which is waiting on Ren to reach main.
   - `renewal_keeping_theorem`, `renewal_closure_theorem`, `renewal_dichotomy_keeping`, `steady_renews`, `steady_fixed`, `steady_contains_fresh`, `steady_within`, `lapsing_closure_renews_forever` and `lapsing_correction_cannot_be_kept` in `lean/conditional/renewal/`. The renewal thread is rewriting these.
2. **Not formalized:** joint probability laws for two learners; probability laws whose total varies by state; joint processes of more than two centers.
3. **Handed on to other work:**
   - empirical identification (§9);
   - particular kinds, rates and presented conditions from the native process (process-law work);
   - the ethical question of which valuations ought to form (ethical-naturalism thread).

## Exact next step

When the axiom-free `ResourceContinuation` and renewal packages are on main:

1. Merge main into the branch.
2. Rebuild, in dependency order, every module in `experiments/valuation-development/lean/` and the core files that import them:
   - `PortValuation.lean`, `ValuationInCore.lean` and `RevisingPort.lean`, all in `inquiry-root/sufficiency/`;
   - their dependencies in `experiments/integrated-correction/general-framework/generative-basis/lean`.
3. Regenerate `lineage-audit-output.txt` and `valuation-renewal-audit-output.txt`.
4. Confirm all 130 results are empty.
5. Update the axiom paragraph in the companion README, the `propext` row of the §18 table, and the RESEARCH.md entry.
6. If a renewal theorem's signature changes, adapt the call sites only, as was done in commit `fafb4da`.

## Conventions in force

- **Merge procedure (Ren's standing rule):** commit, merge `origin/main` into the branch, rebuild and audit, then push to main.
- **No assumptions or axioms:** report anything that cannot be removed or proved necessary to Ren.
- **Monist and relational reading:** derive splits as cuts of one process, as in `OneProcess.lean`.
- **No market vocabulary:** use held (存), enacted (化) and arrived (来).
