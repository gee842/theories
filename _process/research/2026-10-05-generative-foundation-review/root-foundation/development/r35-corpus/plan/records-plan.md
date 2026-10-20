# R35 records plan (read-only preparation, 20 October 2026)

Measured on main 4c40745f8, with E3 and E8 rerun on 87ecfdee5 (after R28's landing). Rerun the scripts on the landing head before applying: R29–R34 rebind records.
Scripts: `scripts/history_compaction.py`, `scripts/supersession.py`. Data: `data/history-compaction.tsv`, `data/history-classes.json`, `data/supersession.tsv`, `data/supersession.json`, `data/id-renames-impact.tsv`.

## 0. Do first: the two proposals approved on 20 October (R25 → R35)

The board says R35 applies them and then removes them from "Decisions pending Ren". Ren's source is `sources/15-codex-theory-conversations/2026-10-20-fix-all-twentieth-review.md`.

1. **Target 1's formal part, restated.** Every central law holds over every ExchangeLaw/ExchangeRelation. Each World premise is a reading or a state of the law. The families are joined by definition (R28 landed that join, cb1be1f3c). Apply it in three places:
   - `_process/goals/theory-of-becoming.json`, the target-1 text;
   - the record `theory-of-becoming-foundation`, its statement and limits plus one history note (substantive);
   - the GOALS render (`make research-render`).
2. **K1–K7 adopted (study §218 table).** Apply them in two places:
   - the board's target sentence;
   - the four parts of `_process/RESEARCH-DIRECTIVES.md`.
   Then remove both entries from the board's pending section.

## (a) E3: compacting record histories

**Measure.** The read-only classifier is `history_compaction.py`. It classifies each note in this order:
- the first note: kept;
- substantive: kept. These notes match statement, title, premise, law, supersession, correction, reading or vocabulary cues, after parenthetical descriptions of other files are removed;
- bookkeeping: condensed. These are rebind, re-point, rehash, receipt, source maintenance, reconciliation or drift notes with no substantive cue;
- other: kept, to stay conservative.

| | before (87ecfdee5) | after |
|---|---|---|
| records | 279 | 279 |
| history notes | 12,077 | 2,939 (+1 condensing note per record) |
| of which condensed | — | 9,416 bookkeeping |
| kept: first / substantive / other | — | 279 / 1,448 / 934 |
| median notes per record | 32 | 9 |
| record JSON bytes | 17.16 MB | ~9.44 MB |

The largest cases (from the 4c40745f8 run) are census-balance 162 → 21, laws-of-one-step 136 → 22, counting-standing-and-dependence 131 → 17 and recurring-reference-revision 125 → 11. R28 alone added 193 bookkeeping notes; that is the growth E3 describes.

**Script design: `research.py compact-history [--dry-run] [--ids …]`**, a new subcommand in `tools/research`.
1. Refuse to run on a dirty tree, as `move` does.
2. For each record with at least one bookkeeping note, call the existing `snapshot` code path. It writes the full pre-compaction JSON as a `text_versions` entry ("history before compaction, 2026-10-2x"), so nothing is lost. Git also holds every byte.
3. Replace the bookkeeping notes with one `{en, zh}` note giving their count and date range, and naming the snapshot.
4. Leave `reviewed_at` and `status` unchanged, and do not touch `validation_scope`.
5. Keep the first, substantive and other notes in their order.
6. `--dry-run` prints this table. The classifier (STRONG/BOOK regexes) lives in `tools/research/history_notes.py`, with tests that cover the 12 sampled notes per class in `data/history-classes.json`.
7. Write a receipt to `_process/architecture/compactions/<date>.json` with per-record counts and sha256 before and after.

**Stop the regrowth.** This is the larger half of E3. Add `tools/research/repoint.py`, one shared tool that replaces the per-kit copies (`rehash_refs.py`, `repoint_drift.py`, `rebind.py` in r21, r22, g1, k1, md1, rc, rg and other kits). It updates the pointers and `validation_scope`, and writes **no** history note when only hashes, receipts or line spans change. Instead it appends one line per landing to `_process/architecture/rebinds.jsonl`: date, commit, record IDs and the reason. The registry rule that a changed binding needs a note, if one exists, accepts a rebinds.jsonl entry. Do this before R35's moves: the chapter edits re-point about 150 records, and the moves re-key references in about 60 more.

## (b) E8: records whose proofs bind superseded modules

Totals: **55 records** (E8 said 53) carry **151 retired proof references**, of which **143 have proof_bindings**. Superseded means a module in `development/bridge-fold/retire.json`, or a file under `lean/history/`. The per-record list, with the retired modules, the core modules still cited and `stated_by_not_cited`, is in `data/supersession.tsv`.

**The edit for each retired proof reference, in the record JSON:**
1. Set `references[i].role` from `proof` to `provenance`. Its `declarations` stay, so the record still shows where the law was first stated.
2. Delete the `proof_bindings` entry whose `source` is that path. The registry requires source role `proof`, so it would fail otherwise.
3. If `stated_by` lists a core module that the record does not yet cite, add a `proof` reference to that module. Give it the declarations under their current names (after R30's renames) and a `proof_binding` to the current core receipt. The column is in `supersession.tsv`. Example: becoming-spine-instances lacks Acceptance, Frontier, GuardHorizon, MoveOutcomeProcesses, PositiveGround, ProfileReach, ScopedReach and SeedReach.
4. Add one history note: "proof references to superseded periphery modules re-roled as provenance; current proof is <modules>".
5. After this, 54 of the 55 keep at least one core proof binding.

**Special cases**
- `derivation-soundness` is left with **no** binding after the re-role. Add a `proof` reference to `Becoming/Derivation.lean` (core) with its theorem names, plus a binding to the current core receipt. This must happen in the same commit.
- `becoming-spine-instances`: its canonical source is `lean/history/…/Bridge.lean`, and it has 12 retired references. Two options:
  - (A, recommended) set `canonical_source` to the core module that now states most of it (`Becoming/Lifting.lean`; EdgeClosure for the edge laws), retitle it "Spine instances in the core", and apply steps 1–4;
  - (B) status `superseded`, with `superseded_by` pointing at the records of the modules in its stated_by list.
  A is better: the record still collects the instance laws in one place.
- `conditional-foundation-assessment` is reviewed-scoped. Its canonical source is the history file `FIXED-FINISH-LINE-AUDIT.md`, and its subject (the conditional finish line) was folded into §6.15. Set `status: superseded` and `superseded_by: theory-of-becoming-foundation`. `theory-of-becoming-foundation` lists it in `dependencies`: move it to `related`, and add a history note to both records.
- The `wisdom-root` record has 5 retired references and 25 in the core. Only the re-role is needed.

**Check.** Run `make research-check` and `research-test`. This needs no Lean run, because the bindings point at receipts that already exist.

## (c) E7: law families

`family` is the session-map field F01–F22 (`results/data/session-results.json`, regex `F\d\d`). It is required, and F01 alone holds 155 records, so it cannot carry law families. Proposal: a new data file `theories/becoming/results/data/law-families.json`, mapping each family id to {title en/zh, the member records in order, a one-paragraph shared statement, and its lead record}. RESULTS.md and the record pages render a "Family" line from it, through `registry.py` and `navigation.py`; the records themselves do not change. `research-check` verifies that every member exists and that no record sits in two families.

| family | lead | members |
|---|---|---|
| census (11) | census-balance | census-balance, whole-law-of-counting, bounded-census-keeps-pace, census-balance-under-continuation, census-read-off-the-exchange, counting-where-the-counts-exist, counts-exist-where-decided, counting-under-enclosure, counting-standing-and-dependence, coming-and-ceasing-keep-pace, ceasing-needs-arising |
| sums over histories (4) | sum-over-histories-exact | sum-over-histories-exact, sums-over-histories-by-support-horizon-and-order, losses-of-the-sum-over-histories, orders-as-a-sum-over-histories |
| laws of one step (3) | laws-of-one-step | laws-of-one-step, laws-of-one-step-complete, one-step-missing-laws |
| law along a run (3) | a-law-through-a-projection-along-one-run | a-law-through-a-projection-along-one-run (G3), a-law-through-coupling-along-one-run (G4), a-law-through-changing-coupling-along-one-run (G5) |
| settling (3) | when-the-runs-of-a-process-settle | when-the-runs-of-a-process-settle (Settling), the-last-change-of-a-run (LastChange), how-often-couplings-act (Frequency) |

**Title fixes**
- `ceasing-needs-arising` is titled "The census law", which collides with the lead. Retitle it "Ceasing needs arising".
- **The one step:** use "The laws of one step" (laws-of-one-step), "The laws of one step are complete" (laws-of-one-step-complete; now "Completeness…") and "What the laws of one step leave out" (one-step-missing-laws; now "What the stated laws of one step miss"). That is one noun phrase across the three. The third depends on the second, and its statement already says what is left out.

**Settling calibration, stated once.** "A run settles exactly where it is decided whether it changes again: deciding settling for every run is LPO." The law is stated in `when-the-runs-of-a-process-settle` (statement and limits). In LastChange and Frequency, replace the restated sentence with "settling is calibrated in when-the-runs-of-a-process-settle", and add a `dependencies` edge to it. Each change is one substantive history note per record.

## (d) E4: renaming 21 IDs

These IDs carry retired labels (g0, axiom, part-one, registration, correction). Counts are measured on 4c40745f8: live files that mention the id / records that reference it.

| old id | proposed id | live files | records | also in |
|---|---|---|---|---|
| alignment-direction-g0-j | alignment-direction-under-living-significance | 121 | 31 | research-config; goals generative-alignment, explicit-axiom-route |
| practical-judgment-g0-j | practical-judgment-under-living-significance | 135 | 34 | research-config; goals universal-intelligence-session, generative-alignment, explicit-axiom-route |
| held-lives-g0-is-centering | living-significance-on-held-lives | 83 | 11 | |
| self-good-reachable-g0 | own-good-to-reachable-living-significance | 96 | 15 | goal universal-intelligence-session |
| one-axiom-yields-g0 | continuation-condition-yields-living-significance | 141 | 38 | research-config |
| axiom-decomposition | continuation-condition-decomposition | 94 | 10 | |
| closure-verdict-meets-axiom | closure-verdict-meets-continuation-condition | 92 | 10 | |
| wisdom-root-part-one | wisdom-root-zero-axiom | 113 | 14 | |
| selection-through-registration | selection-through-couplings | 131 | 25 | research-config; goal meta-attractor-integration-session |
| selection-under-registration-revision | selection-under-lumping-revision | 108 | 12 | goal meta-attractor-integration-session; **chain** |
| testing-within-registration | testing-within-couplings | 147 | 42 | |
| subthreshold-registration | differences-below-threshold | 107 | 16 | |
| learnable-through-registration | learnable-through-a-map | 103 | 14 | research-config |
| contextual-registration | claims-shown-in-context | 119 | 16 | |
| formed-copying-registration | formed-contacts-change-copying | 89 | 5 | **chain** |
| registration-within-what-it-registers | readings-within-what-they-read | 107 | 13 | |
| sensitivity-is-the-least-registration | sensitivity-is-the-least-coupling | 79 | 7 | |
| only-the-order-of-change-registers | only-the-order-of-change-shows | 86 | 7 | |
| runaway-distance-unregistered | runaway-distance-uncoupled | 119 | 22 | research-config |
| formed-copying-correction | formed-rejoining-of-a-successor | 79 | 2 | **chain** |
| market-partial-correction-boundary | market-partial-rejoining-boundary | 101 | 6 | **chain** |

The proposed IDs follow the current titles and the adopted vocabulary (study §7; M4 "rejoining"). One assumption: the new titles from R30's rename table should be checked against these before applying. A background R30 draft is running, so take its title column if it differs.

**The four chain-bound IDs** (marked chain) are named in `generativity-chain.json` (about l.1423, by record path and sha256) and in `GENERATIVITY-CHAIN.md`. Ren's curated chain changes only through `GENERATIVITY-CHAIN-INDEX-RECORD`, so rename these four in a separate step. It goes with a maintenance-record entry that rebinds the chain's record paths and hashes. The record's hash changes anyway, because the id is inside the JSON. The chain's historical evidence is not refreshed.

**Tooling needed.** No alias or redirect support exists. `orphan_pages` fails on any results `.md` without a record, and nothing maps old IDs.
1. A `research.py rename-id OLD NEW [--dry-run]` subcommand, which:
   - renames `records/OLD.json` and its rendered page with `git mv`;
   - sets `id`, and appends OLD to a new optional `former_ids` list (schema: an array of strings, unique across the registry, never equal to a live id);
   - rewrites `dependencies`, `related`, `superseded_by` and `instances` in all records;
   - rewrites research-config, `_process/goals/*.json` and live Markdown links and mentions. It reuses `moves.py`'s rewrite engine, so `sources/` and history are never touched;
   - writes a receipt under `_process/architecture/renames/`.
2. Redirect stubs. The registry renders `results/records/OLD.md` as a one-line "renamed to NEW" page from `former_ids`, and `orphan_pages` accepts a page whose name is in some `former_ids`. Old links in history and sources therefore still resolve.
3. `research-find` also matches `former_ids`.
4. Tests: a rename round-trip, a collision refusal, and a stub render.
5. Apply all 17 non-chain renames in one batch, so the record pages render once. R30 owns Lean names, not record IDs, so coordinate only on titles.
