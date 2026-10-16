# 4. Restructure plan

[Review summary](README.md) · [Architecture](ARCHITECTURE.md) · [What is proved](PROVED.md) · [What needs to change](CHANGES.md) · [Restructure plan](RESTRUCTURE-PLAN.md)

> AI-authored section of the whole-repository review of 16–17 October 2026 (read-only, HEAD `0cfb9c567`; Claude Opus 5.5 reviewers with adversarial verification). Not Ren's text and not external review. Paths are repository-relative; counts are as measured by the reviewers at that HEAD.

**Scope of the numbers.** Tracked-file counts were measured with `git ls-files` at HEAD `0cfb9c56` on 2026-10-16. The total is 70,495 tracked files: experiments/ 57,568, of which the Lean tree holds 51,163; sources/ 6,373; _process/ 4,289; drafts/ 1,339; theories/ 704; worldbuilding/ 164; tools/ 17; output/ 14; tmp/ 10; about 16 root files. All other figures come from the area reviewers, as cited.

**Rules for the whole plan**
- Nothing is deleted. Every move preserves the file's bytes and gets a manifest entry. Frozen copies, receipts, edit ledgers and failed attempts stay retrievable at a recorded path.
- Links are rewritten only in live files. Frozen evidence keeps its old paths, and those paths resolve through manifests. This follows the 10-09 rename precedent (`_process/architecture/rename-2026-10-09.json`, `check_rename.py`).
- A record's source hash is carried over only for exact path substitutions. Any other byte change is re-read and rebound through RESULT-WORKFLOW. A hash is never refreshed blind.
- Ren's text changes only with Ren. That covers OPENING.md, AGENTS.md, goal scopes, the generativity chain and the quoted directive text.

### 4.1 Target tree

The principle is one responsibility per top-level area, and fewer copies rather than new layers. Each area gets a `history/` sibling at the same depth for what it retires.

```
README.md            generated: Ren's opening (unchanged) → "What is established" → "Start here"
AGENTS.md            instructions (rewrite needs Ren)
RESULTS.md           THE single result register (grouped by layer: core / bridge / periphery / argument / target)
GOALS.md             generated; scopes ordered by authorization state
OPEN-QUESTIONS.md    generated: targets, §8 groups, decisions pending Ren, next_delta
DEPENDENCIES.md      generated compact adjacency + used-by (≈30–100 KB, was 555 KB)
RESEARCH.md, MAP.md, GLOSSARY.md   short stubs/current pages that keep their paths and anchors
Makefile, .gitignore, .gitattributes, .github/

theories/becoming/            canonical theory
  OPENING.md                  Ren's text
  chapters/                   THE-THEORY-OF-BECOMING.md + current studies (~30–60, see 4.2), README.md (generated chapter index)
  results/                    records/, data/, generated views (RESULT-REGISTER.md → stub)
  history/                    retired chapters (same depth as chapters/), verification/, lineage/shengsheng-buxi/
theories/<15 branch folders>/ September syntheses, kept in place with a generated status header

experiments/integrated-correction/general-framework/generative-basis/lean/   Lean root (stays; see below)
  becoming/                   pure core + bridge package, check_becoming.py, receipts
  becoming/becoming-checks/   receipts in place; copies in a content-addressed store (4.3)
  deeper/, inquiry-root/, universal-ethics/, …   periphery (paths unchanged)
  history/                    unreferenced run folders, connected/, earlier stage material (inside LEAN_ROOT)
experiments/                  experiments + generated index; experiments/history/ for the 5-Oct IC and general-framework studies

_process/
  BECOMING-WORKBOARD.md       live board ≤15 KB
  RESEARCH-DIRECTIVES.md, DIRECTIVE-INDEX.md (generated), goals/, RESULT-WORKFLOW.md, research-config.json
  architecture/               manifests, hash-addressed history/ (unchanged), moves/ (receipts per batch), repairs/
  research/2026-10-05-generative-foundation-review/   the one live study
     root-foundation/         ~60–150 live files + generated index
     history/                 retired packets, landing kits, 10-06 working set (same depth as root-foundation/)
  research/2026-10-05-concern-theory/   stays (freeze-pinned)
  history/                    retired studies, 2026-09 corpus pages, handoffs, workboard log

sources/                      imported originals only; README.md, GROUPS.json, generated SOURCES.md, MANIFEST.tsv
tools/research/               all shared infrastructure, including paths.py, moves.py, landing/, lean_scan.py
tools/publishing/             PDF/site builders (from tmp/pdfs)
drafts/                       dated drafts + generated README index
output/                       exports + README (source → builder → export)
(tmp/, work/ ignored; nothing tracked)
```

**Where the Lean package lives.** I recommend keeping it at `experiments/integrated-correction/general-framework/generative-basis/lean/` for now, documenting the path once in README and experiments/README, and pointing every README on the directory chain to `becoming/`.

The package cannot move alone. `check_becoming.py` uses `LEAN_ROOT=HERE.parent` and compiles 215 sources across 6 sibling locations. It resolves the three FOUNDATION modules (`GenerativeCore.lean`, `inquiry-root/sufficiency/InquirySufficiency.lean`, `deeper/RelationalRenewal.lean`) by file stem anywhere under the Lean root.

Moving the whole Lean tree to a top-level `lean/` would cost the following:
- About 1,741 live files would need rewriting (about 23,150 occurrences): 220 record JSONs, 42 chapters, about 1,160 study files, AGENTS.md, the board and the `lean_catalogue.py` group rules.
- 124 of 351 live Lean-tree scripts use fixed `parents[N]` and would need editing.
- Every open worktree would conflict.
- About 1,028 evidence files (31,168 occurrences) would need a former-path table.

If Ren wants the move, it is the last batch: one prefix rule, at a merged quiet point, followed by one fresh core run (Decision 4). The three foundation modules stay where they are. Moving them into `becoming/` would rename modules and change core bytes; `GenerativeCore.lean` is freeze-pinned and cited by 181 live checkers.

### 4.2 History layout and what moves

**Layout rule.** Retired material goes into a directory named exactly `history`, placed as a sibling at the same depth as the material it replaces. This choice satisfies four constraints at once:

| Constraint | Why `history/` at the same depth satisfies it |
|---|---|
| `check_becoming.py` ARCHIVE regex | Already skips a path component named `history`, so a module copy under `history/` is never taken as a second live module. |
| `research.py` default discovery | Already excludes `history` parts (research.py:113-123). |
| Relative links | Same-depth moves keep `../../` links valid (about 97% for the chapters). |
| Lean receipt discovery | Lean history stays under LEAN_ROOT, so `passed_receipts` still finds the only receipts for 23 inherited spine modules (receipts kept inside deeper/ run folders). |

`_process/architecture/history/<hash>/` stays as it is. Its paths are hash-bound in records' `text_versions` and in `history-manifest.json`. It gets a generated `INDEX.md` (directory → original path, version, date, kind) and no renames.

**What every history root carries**
- `MANIFEST.json`: old path, new path, sha256, git blob id, move commit, reason ("superseded", "failed attempt", "applied kit; do not rerun").
- A generated `INDEX.md`.
- A per-batch receipt in `_process/architecture/moves/moves-<date>-<batch>.{json,tsv}`, verified by a new `check_moves.py` (the 10-09 checker stays untouched and must keep passing).
- Labelled, registered reading editions wherever links were adapted.

**Moves, in batch order** (counts are per reviewer, re-verified by a full-repo grep immediately before each batch):

| # | What | Target | Files | Ren? |
|---|---|---|---|---|
| H1 | Root/process corpus: TIMELINE, BOOKS, originals of MAP and GLOSSARY (short stubs stay at the root), THEORY-DIGEST, THEORY-TEMPLATE, COVERAGE, CRITIQUE-FINDINGS, timeline-raw.tsv, read-pass-1-plan.json | `_process/history/2026-09-consolidation/` | 10 | yes |
| H1 | reading-notes inputs hb-01..03, cb-01..07 (the cited out-* notes stay) | `…/2026-09-consolidation/reading-notes-inputs/` | 10 | no |
| H1 | CLOUD-HANDOFF-2026-10-07 + handoffs/ | `_process/history/2026-10-07-handoffs/` | 10 | no |
| H1 | architecture repair evidence: start-state, validation, rename receipt + checker | `_process/architecture/repairs/{2026-10-08,2026-10-09-rename}/` (check_rename.py depth adjusted, `--follow`) | 4 | no |
| H2 | Workboard landed rows (lines 36–151 closed rows, 156–374 log), verbatim, with source commit | `_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-16.md` | 1 new | no |
| H3 | Eight 10-04/05 studies (integrated-evolution, causal-foundations, direction-frontier, generative-health, repository-reconciliation, revisable-concern, support-and-shared-generativity, unified-theory); concern-theory stays (freeze pin) | `_process/history/<study>/` (same depth) | 421 | yes |
| H3 | 10-05 specialist dossier (REVIEW, FOUNDATION*, OPTIMAL-FOUNDATION, optimal-foundation/, final-synthesis/, review-support/, MANIFEST, DOCUMENT-CHECKS) | `_process/history/2026-10-05-specialist-dossier/` | 37 | yes |
| H4 | Quiet chapters (no ties to canonical, goals, records or tools): about 70 safe, up to 100 if the chain-linked ones go through the chain workflow | `theories/becoming/history/` | 70–100 | yes |
| H4 | `chapters/verification/` (with FORMATION-MATH and SYNTHESIS-RECORD links) | `theories/becoming/history/verification/` | 13 | no |
| H4 | synthesis-a/b/c lineage files | `theories/becoming/history/lineage/shengsheng-buxi/` + README | 3 | no |
| H5 | root-foundation free pre-10-10 packets (not cited by records, chain, catalogue, tools or freezes) + 32 early development dirs | `_process/research/2026-10-05-generative-foundation-review/history/<programme>/` | 1,643 + 319 | yes |
| H5 | 50 spent landing kits (p49–p127, integration-i3c..i4c, landing-kit; p77, p88 excluded as record-bound) | `<study>/history/landings/<P-item>/` (same depth as development/) | 527 | yes |
| H5 | 10-06 working set (BEFORE snapshots, attempts, reviews, accepted, extraction, scripts) | `<study>/history/2026-10-06-working-set/` | 411 | yes |
| H5 | executed plans (general-laws PLAN, OPEN-ISSUES-PLAN, audits, batch notes, prototypes) | `<study>/history/plans/2026-10-14-general-laws/` | 143 | yes |
| H6 | experiments IC 5-Oct financial study (CENTRAL-CLAIM, RESULTS, model, constitutional-extension, governance-closure, viability-control, systems-dynamics, …) | `experiments/history/2026-10-05-integrated-correction/` (same depth) | 63 | yes |
| H6 | general-framework README/review/closure-study/gap-resolution/reproduction-test | `experiments/history/2026-10-05-general-framework/` | 142 | yes |
| H6 | generative-basis 5-Oct study files (MANIFEST, CHECKPLANs, formal/, checks/, figures/, review/, integration/, renewal-closure/) | `experiments/history/2026-10-05-generative-basis-study/` | 24 | yes |
| H7 | universal-ethics unreferenced runs (49 failed, 46 without receipt kept as evidence) | `lean/history/universal-ethics-runs/` | 9,608 | yes |
| H7 | deeper/ + inquiry-root/ unreferenced runs (72 failed, 56 superseded, 2 no receipt) | `lean/history/{deeper,inquiry-root}/` | 2,706 | yes |
| H7 | `lean/connected/` (6-Oct builds; 0 records; its checkers no longer pass) | `lean/history/connected/` | 357 | yes |
| H7 | other periphery runs (systems-complexity, new-possibilities, learning dev) + 12 unreferenced experiment runs | `<package>/history/` | 255 + 393 | yes |

"lean/" in the table abbreviates the Lean root.

**Retired from navigation but left in place.** These paths stay, get a banner or a generated status entry, and are excluded from default discovery:
- The 31 tied chapters, including GENERATIVE-GROUNDING (1,025 live inbound links, 2 goal records), UNIFIED-ETHICAL-GROUNDING (2,544 anchored links), UNIVERSAL-ETHICAL-MINIMUM, HUIGEN, ETHICAL-LEARNING, G0-WARRANT and START-HERE.
- The 505 tied root-foundation packets, until `reviewed_version` follows moves (phase 2 of H5).
- The 12 historical 4–5 Oct experiment dirs (359 files).
- The 10-06 lean-root checker archives (`verification-history/`, `legacy-replays/` and others; 350 files, hard-coded paths).
- The 105 per-family periphery checkers.
- sources/20–25 AI session snapshots: recommended in place with a README and a `frozen` class in GROUPS.json, because about 67k receipt references bind sources/ paths.

**Pinned files that never move**
- sources/ originals.
- Every FREEZE or preregistration manifest and every file it pins (selective-handoff/FREEZE.json is already broken by the 10-09 rename; repair it by a reconciliation sidecar, never in place).
- All `*-verification.json` and run receipts cited by records or inherited by the core receipt.
- MARKET-INTERNET-DEGENERATION.md (5 records) and BECOMING-RENEWAL-READING.md (158 records; `path#anchor` citations).
- `build_*.py` (ROOT=parents[4]).

### 4.3 Evidence compression and retention

**Retention rule.** Keep in place, whole:
1. Every `verification.json` and receipt.
2. Every run or file named by a record (proof_bindings, references, counterexamples), by a current receipt's `retained_run`/`inherited_receipts`, or by any Markdown link or plain-text mention. About 30 `<Module>.lean` copies are cited in backticks.
3. The latest passed run per checker.
4. The two newest becoming runs (20261016T121942, 20261016T124157).
5. The three path-cited copies (two `Becoming.RegroupingSelection.lean`, one `Becoming.Testing.lean`).

Everything else may be compressed. Bytes are never removed from the tree without Ren's explicit approval (Decision 3).

| Target | Now | Proposal | Effect |
|---|---|---|---|
| `becoming/becoming-checks/` copies | 31,786 files, 446 MB; 1,694 unique of 13,817 .lean, 1,012 of 17,536 logs, 8,129 empty files | Content-addressed store `becoming-checks/_objects/<sha[0:2]>/<sha>` (no .lean suffix) plus `_objects/INDEX.json`, built from each receipt's `artifact_sha256` (165 receipts) and generated manifests for the 6 failed runs. Byte-identical blobs, so git gains no objects. Add `research.py evidence restore <run>`. | ~31,786 → ~3,650 files (−88%); working tree 446 → ~245 MB |
| deeper/, inquiry-root/ duplicates | 4,544 byte-identical files (e.g. two extra 8.68 MB copies of native-packet-correspondence.json) | Same object-store pattern under `lean/history/blobs/` with a manifest per run | −4,544 files (optional) |
| Future runs | — | `check_becoming.py` stops writing zero-byte logs and records log size + sha256; a criteria-version string joins the step-key context | about 25–40% fewer files per run |
| Record `history[]` | 2,662 of 4,283 (a–l) and ~1,977 of 3,281 (m–z) entries are mechanical rebind notes; ~5,365 in all, 4.8 MB | Step 1: render-side folding (no data change). Step 2 (Ren): snapshot each record (`research.py snapshot`), then move the mechanical class to `results/data/rebind-ledger.jsonl` with a one-line pointer. Corrections, reviews, Ren decisions and narrowed claims stay in the record. | record pages 11.0 → ~5.3–6.3 MB |
| `results/data/lean-index.json` 8.2 MB, `source-index.json` 1.3 MB | 121 commits; 225k-line diffs; scans untracked files | Discovery from `git ls-files`; drop development-attempt/archive bodies (keep paths + hashes); regenerate only at landings; `.gitattributes` `-diff linguist-generated` on data/*.json, lean-declarations/*.md, LEAN-*.md | ~8.6 → ~4.7 MB |
| `*-EDITS.json` ledgers (199 + 167, ~31 MB) | before-text not in git (tested) | Keep verbatim. Add a sidecar mapping payloads to blobs where one exists; mark the unique payloads. Exclude from default search. | navigation only |
| `UNIFIED-ETHICAL-GROUNDING-BEFORE-*` and similar snapshots (~2.1 MB, 33 files) | some receipt-bound | Index manifest (snapshot → commit/blob, sha256, binding receipts); exclude from discovery | navigation only |
| Large datasets (heald-2021 .mat 421 MB, karita, situated-discovery runs.jsonl 55 MB) | plain git | No LFS history rewrite: it would break 298 receipt `source_commit` fields and 293 cited SHAs. Written policy: new imports over 10–20 MB go to LFS or an external store with a committed manifest (url, sha256, size). | — |

An alternative from the git-health reviewer: replace 49,133 unreferenced non-JSON run-folder files with per-run `RETIRED-MANIFEST.json` plus a pushed anchor tag. That gives about −70% of tracked paths, but the bytes would then exist only in git history. It is not the default here and needs Ren's ruling on whether it counts as deletion.

### 4.4 Rewrites

**Ren's text (proposals only)**
- OPENING.md: collect the notes in `drafts/2026-10-10-opening/OPENING-V7-NOTES.md`. They cover conditions in paragraphs 9 and 13, the dissipation and closure readings, the limits of "explains good and evil", G0 immediacy, footnote labels, and the line-1 comment "version 5" → 6. Change OPENING.md only with Ren's go.

**Canonical chapter** (`THE-THEORY-OF-BECOMING.md`, 962 KB). Through the integrator's queue, in this order:
1. "In one sentence" (L28-59): one sentence per language plus a 5–8-line status box (no axiom; local-hypothesis laws; one axiom as condition, not asserted; G0 immediate from it; necessity open). The fold chronology moves to §6.15/§5 and a new `BECOMING-FORM-HISTORY.md` in the study.
2. "Stated in full" (L60-127, 71.8 KB): one paragraph per item, at most ~150 words and ≤5 declarations. The selection tables first go into records (map-of-premises, whole-law-of-counting, counting-under-enclosure, counting-standing-and-dependence, …) and a generated selection × law view, so nothing is lost.
3. Premise card (L128-170): blocks for representation commitments, local conditions (finite, enclosed, listed, decided), the eight World premises with Lean names (`World.contingent`, `World.independent`, `World.hatch_binds`) and corrected Logic/Dynamics rows.
4. Additions:
   - P130 (Runs, CourseWorlds, LearnableRuns, ParityReadings, FinerTraces, FormedLoops) and P114 Courses, stated as correspondence theorems. The reading "the one root is the run" stays Ren's.
   - I4b logical strength (DNE `Gated.origin_of_propositions_iff`, Markov `refutable_passes_iff_markov`, LLPO, dependent choice `runs_iff_selection`) in §8 L1460/1468.
   - The Onward fix at L1495/1508.
   - Condition fixes in Part I stated whole II.
5. §6: §6.7's N_std draft and D11–D15 narration go to a labelled history excerpt (Ren's quote stays in the chapter). §6.9 states only the corrected reading. §6.8–6.12 are rewritten in conditional voice. The §6.15 "22 theorems" becomes a generated count or is dated.
6. "Part I stated whole" (108 KB, ~420 declarations): a 1–2 page prose statement. Its declaration catalogue is generated from records (anchor kept; 9 inbound links).
7. §8: open items only, generated from records' status/next_delta; a "What stays Ren's" list including P120, P123, P125, P126, P127 and P130; reviews through R18 and release readiness. §9 and §10: generated (4.5). §11: generated from the chapter index.
8. Parity: full parallel English for §1–§7 with the same declarations and links. English meanings for the 190 Chinese-only glossary rows. Delegation formulas become `[AI reading, Dn]` markers. One delegation statement sits at the §6 head.

The chapter stays one file at its path for now. A split into part files is Decision 5.

**Top pages and process**
- README: Ren's opening, then a generated "What is established" block (counts from the committed receipt, 8–12 headline laws chosen by Ren, §6.15 conditional results, periphery labelled with premises and axiom footprint), then "Start here". The hard-coded prose at `navigation.py:220` moves to a Markdown file named in the config.
- AGENTS.md (Ren): new start path, G0 fold and P128 status, board rules 5/7/8, naming criteria, zero-premise-first, "note, don't follow blindly", path-limited commits, no-prune, accurate directive-register wording. The history copy (`0371e616118b4c19`) is preserved.
- BRIEF.md (via the generator): a 1–2-page method and reading-order page that links the workboard and labels the September folders historical.
- MAP.md: a short current corpus map at the same path; the 10-04 original goes to H1. Where the "Why, and what it means" section lives is Ren's call.
- NONDUAL-METHOD.md (Ren): a bilingual current method page in becoming vocabulary (P36b), about 8 KB; the current text goes to `theories/becoming/history/NONDUAL-METHOD-2026-10-10.md`.
- Workboard: the live board keeps rules, target, a "Now" block (integrator as confirmed by Ren, last pushed main, queue state), open claims, the landing queue (anchor `#落地队列--landing-queue` kept) and Ren's pending decisions. The integrator writes "landed <commit>, §N" into rows 41–51 and 60, and closes row 152 as superseded by P128. Rule 4 gains a clause letting the integrator append landing commits.
- Study plans (ZERO-PREMISE, CONTINUATION-GROUNDING, WUMING, REGISTRATION, UNIFICATION, PART-II-INVENTORY, THEOREM-CONNECTIVITY): dated status lines appended as added lines only. The UNIFICATION rename tables are copied to `_process/architecture/renames-becoming.md`.
- Large accreted chapters (PHILOSOPHICAL-ACCOUNT, PLURAL-SYSTEMS, RELATIONS-ACROSS-SCALES, ZERO-AXIOM-PRACTICAL-JUDGMENT, ETHICAL-LEARNING, EXPLANATORY-NECESSITY, KNOWLEDGE, GENERATIVE-GROUNDING): a compact current account at the same path, with the round logs moved verbatim to `theories/becoming/history/<NAME>-rounds-<date>.md` and every anchor kept by alias. This needs Ren (Decision 6).
- Records:
  - Headlines scoped to Lean strength: continued-change-needs-openness, becoming-finite-horizon, contextual-registration, continuous-time-as-tower, how-often-couplings-act, worlds-are-runs, rest-with-refinement-counted, no-finite-part-bears-taking and others (Ren reviews wording).
  - Stale next_delta fixed: laws-of-one-step, subthreshold-registration, recurrence-without-premise and about 30 others.
  - False "no-evaluation" boundaries removed.
  - F07 re-familied (12 axiom-free records leave it).
  - 54 schema-1 records migrated to schema 2.
  - Progress on theory-of-becoming-foundation added for P51, P107, P128 and P130.
  - New records: practical-alignment-application, empirical-discriminators, period-inquiry-lower-bound, and about 13 empirical assessment records copied verbatim from existing READMEs.

### 4.5 Reindexing and tool changes

**Generated views** (navigation.py / registry / catalogues, all with overwrite guards and `generated-manifest.json` entries):
- RESULTS.md is the single 229-row register. RESEARCH.md, theories/becoming/README.md, chapters/CLAIMS.md and results/RESULT-REGISTER.md become stubs; ROADMAP.md becomes a stub to GOALS. All preserved-history anchor blocks are kept. Inbound links: RESEARCH.md 80 files, CLAIMS.md up to 192.
- DEPENDENCIES.md becomes a compact adjacency with a stable `<a id>` per edge, plus a "Used by" list on every record page.
- OPEN-QUESTIONS.md: own header, 4 targets, §8 groups, pending-Ren decisions.
- GOALS.md is ordered by state.
- Indexes: the root-foundation study (and `REVIEWS.md` ledger), `development/INDEX.md` + `MANIFEST.json`, `chapters/README.md` (all files with status and successor), the experiments index (kind column), and `sources/README.md` + generated `SOURCES.md` from `GROUPS.json` (59 groups; aliases 32a/b, 36a/b).
- `_process/DIRECTIVE-INDEX.md` lists all 293 directive records with kind.
- `SPINE-MODULES.md` and the §9 count/layer/receipt columns come from the receipt plus `check_becoming.py` CORE/BRIDGE, with hand prose cells kept. 21 rows currently disagree and 6 are missing.
- The package README module table lists 128 core + 8 bridge modules, with FallibleInquiry marked periphery.
- LEAN-INDEX gains `becoming-core`/`becoming-bridge` groups from receipt layers.
- The bilingual glossary comes from `results/data/glossary.json`.
- `MODULE-CLASSIFICATION.md` is rerun on the current receipt.

**research-config.json** gains: history roots, the move-receipt directory, the README lead file, the featured-results list, the register page, the open-questions sources and the evidence classifier rules. The three currently unused keys get wired up.

**Tool changes (all before any move)**
- `tools/research/paths.py`: config-driven paths, the generated-page list and one shared evidence/path-role classifier. It replaces three divergent rule sets (lean_catalogue, I4a inventory, SPINE-INTEGRATION). `lean_catalogue.path_role` treats `history` as a saved copy.
- `tools/research/moves.py` + `_process/architecture/check_moves.py`: file-level moves with a blob-identity check; path re-keys with unchanged sha for every register kind; a referrer-relative link rewriter that also resolves strings in record history prose.
- `registry.reviewed_version` follows move receipts, or the 248 existing `changed_outside_cited` pairs and every moved source become drift. Rebind or review those 248 first.
- `research.py`: `links` (link check), `move --plan`, a `directive` search kind, size caps applied only to archives so the 2.4 MB live study becomes searchable, and a freeze checker using reconciliation sidecars.
- Hard-coded paths fixed:
  - `navigation.py:211-258, 273, 275`
  - `lean_catalogue.py:38-48, 190, 369`
  - `reading_catalogue.py:134, 145-151, 194` (the `CANON.glob` assertion is extended to history/)
  - `session_map.py` inputs
  - `check_release.py:116, 133` (the silent skip becomes a failure)
- `session_map --check` stops writing.
- Landing kit promoted to `tools/research/landing/` with tests (spec-driven; it replaces about 10 re-implemented scripts per landing). The original files stay byte-for-byte.
- `check_becoming.py` (bundled with the Lean batch):
  - pin FOUNDATION paths and assert CORE equals the root imports;
  - move SCOPE prose (1,565 lines) to `SCOPE.json`, with step keys unchanged;
  - add a criteria version;
  - extract the scanner to `tools/research/lean_scan.py` (or `becoming/audit_support.py`), leaving a re-exporting shim at `universal-ethics/generative-capacity/check.py` for 188 importers.

**Record canonical_source.** Re-pathed only by exact substitution with the hash carried: about 50 records for H5 phase 2, plus 7 records and 85 history links for record-bound development evidence (p72q, p77, p88, p130-frontier, migrations). Each re-path is verified against the move receipt.

### 4.6 Git hygiene (proposals only)

1. **Urgent, Ren.** Revoke the OpenRouter key (5 occurrences in `sources/14-claude-code-prompts/*` and `_process/reading-notes/cb-03.md`). Then replace it in the tree with a redacted reading edition, keeping the original in a private store. Add a credential-pattern check to research-check. Decide repository visibility (personal chats, memories, friends' transcripts, the Guardian Anarchy copies that sit on origin despite the local-only instruction).
2. Before removing any worktree, land the unlanded receipts: `.claude/worktrees/jolly-pike-140c94/…/becoming-checks/20261011T170859.998618Z` (cited on main) and the `review-wt` 20261016T112106.917817Z copy in /private/tmp. Copy the two dirty worktrees' untracked check runs into evidence.
3. Worktrees: 88 registered, 22 marked prunable, 79 at commits already in main, about 228 GB on a 91%-full disk. With Ren's go: non-forced `git worktree remove` for clean merged trees, after checking ListAgents and the board (land-p130, land-p129 and scoped-drift may be live). `git worktree prune` only with Ren's explicit go. Never use `--force`.
4. Add a sparse-checkout profile (`tools/research/sparse-profile` + recipe) for landing and agent worktrees: about 1 GB and about 11k files instead of 3.6 GB and 70k. It changes no data.
5. Object store, with Ren's go, while no session commits: `git -c gc.cruftPacks=true gc` with `gc.pruneExpire`, `reflogExpire`, `reflogExpireUnreachable` and `worktreePruneExpire` set to `never` (a persistent config change). APFS clone backup and `git fsck` before and after. This reclaims about 1.9 GB of duplicate packs and garbage; the 12 `tmp_obj_*` files go to an external archive with a sha256 manifest. Never use `--prune`.
6. Branches and refs: 142 local branches (131 merged), 9 merged `origin/claude/*`, 60 `refs/codex/*` (0.38 GB, including a 185 MB non-LFS blob). Keep them all. Optionally move superseded heads to `refs/archive/*`. Push by branch only, never with `--mirror`.
7. `.gitignore`: add `.claude/worktrees/`, `.lake/`, `*.olean`, `*.ilean`, `node_modules/`, `.venv/`, `*.blend1`, `*.download`, `.pytest_cache/` and `out/`. Add `tmp/` and `work/` only after the 10 tracked tmp/ files move (builders to `tools/publishing/`, the canvas source to `theories/architecture-for-a-living-earth/…`, Guardian Anarchy items per Ren). Check `git ls-files -i -c --exclude-standard` first.
8. CI: `actions/checkout@v4` with `fetch-depth: 0`, `filter: blob:none`. Billing is Ren's. Scoped drift reports "history unavailable" as a warning on shallow clones.
9. `experiments/guardian-anarchy`: a dangling gitlink with no `.gitmodules` and a local-only nested repo (2 commits). Make a git bundle backup outside the pushed tree, then follow Ren's choice: a tracked `.LOCAL.md` stub, or import under `drafts/2026-10-04-guardian-anarchy/site/`.
10. Ren's three recordings (213 MB, local only) and the untracked ASR pipelines in tmp/ need a backup. The pipelines (~100 KB of scripts and indexes, no audio) move into `sources/18-friend-conversations/<date>/pipeline/` after a secret check.

### 4.7 Phased execution

**Coordination for every phase**
- Claim one board item (e.g. "R-restructure: phase N").
- Unified head first (rule 7): all sessions merged, queue empty.
- One landing by the integrator; verify in a worktree; land when main is clean.
- Commit only owned paths with `git commit -m … -- <paths>`. Never commit in the shared checkout mid-merge.
- Re-read every shared record or page before editing, and reconcile any peer prose in generated files before rendering.

**Baseline verification for every phase:** `make research-check`, `make research-test`, `research.py links`, `research.py check --changed-since <phase-start>`, and `_process/architecture/check_rename.py` still passing. Phase-specific checks are in the table.

| Phase | Content | Depends on | Extra verification |
|---|---|---|---|
| P0 Preconditions | Key revocation and visibility decision (Ren); private backups (4.6 item 10, guardian bundle); land the unlanded receipts; record the baseline commit and a full-tree sha256 manifest; rebind or review the 248 drifting pairs | — | `git fsck`; baseline manifest committed |
| P1 Tooling | paths.py, moves.py/check_moves.py, move-aware `reviewed_version`, path_role `history`, research-find fixes, freeze checker + sidecars, generated-manifest pruning, landing kit promotion, CI fetch-depth, .gitignore, sparse profile | P0 | tests pinning current outputs of the three classifiers; Python read-only replay of `check_becoming.passed_receipts`/`receipts_for` over a simulated moved tree (no Lean) |
| P2 Navigation (no moves) | single register + stubs, DEPENDENCIES, OPEN-QUESTIONS, study/development/chapter/experiments/sources/directive indexes, architecture history INDEX, LEAN-INDEX groups, banners via catalogue `standing` field, §9/README module tables generated | P1 | anchor check for every stubbed page; diff of generated views against hand content |
| P3 Rewrites | workboard split, BRIEF, MAP, chapter rewrites (4.4 order), record wording/next_delta/F07/schema-2, plan status notes; Ren-gated ones (AGENTS, NONDUAL-METHOD, goals, README featured set) when approved | P2; Ren decisions | rebinding reviewed per record (no blind hash refresh); bilingual parity warning check |
| P4 History moves | batches H1 → H2 → H3 → H4 → H5 → H6, one receipt per batch, live links rewritten, evidence untouched | P1 tools; P2 indexes; Ren for each batch | `check_moves.py --receipt` (blob identity), preservation hashes vs the P0 manifest, `history-manifest.json` registration, record re-path verification, re-render of source-index/lean-index/catalogues, chain maintenance record for chain-linked paths |
| P5 Evidence compression | becoming-checks object store, deeper/inquiry dedupe (optional), record history render folding → ledger (Ren), lean-index slimming, .gitattributes | P1 (restore command), P4 H7 not required | every receipt's `artifact_sha256` resolvable through `_objects/INDEX.json`; restore round-trip for 3 sample runs; proof_bindings JSON pointers resolve |
| P6 Lean batch | H7 run-folder moves under LEAN_ROOT; docstring pass (Boundaries/Bridge/Relevance/Metaethics "condition of §6.15", Order P129 artifact, Units, Testing, Learning uniformity, Frequency natural-number strengths); checker edits from P1; optional renames (Ren); optional Lean-tree relocation last | P4, P5; quiet head | one fresh core run (`BECOMING_FRESH=1`) with its receipt committed and cited in the I5 report; periphery reruns for the 11 instance receipts that predate current core bytes; records rebound with history notes |
| P7 Git ops | worktree removal, cruft gc, refs archive | P0 item 2; Ren | `git fsck`, `git worktree list`, `git count-objects -vH` before and after |

### 4.8 Expected end state

The default scenario is: moves plus the becoming-checks object store, with no bytes removed from the tree. Moves alone do not change tracked counts; they change what is live.

| Area | Tracked now | Tracked after (default) | Live/navigable now → after |
|---|---|---|---|
| Lean tree | 51,163 (becoming-checks 31,786; universal-ethics 11,848) | ~23,000 (becoming-checks ~3,650); ~18,500 with the optional deeper/inquiry dedupe | ~13,000 universal-ethics/deeper/inquiry run files move under `lean/history/` |
| experiments/ other | 6,405 | 6,405 | 229 IC/general-framework files to `experiments/history/`; 12 dirs bannered |
| _process/ | 4,289 | ~4,295 (+indexes, receipts) | root-foundation top level 2,208 → ~565 after H5, → ~150 once tied packets can follow; 10 dated studies → 1 live + concern-theory; workboard 276 KB → ≤15 KB |
| theories/ | 704 | ~710 | chapters/ 139 .md → ~40–70 (canonical + current studies); canonical chapter 962 KB → target well under half after the apparatus is generated and the summaries are cut |
| Root pages | ~16 | ~16 | register copies 5 → 1 (4 stubs); DEPENDENCIES 555 → ~30–100 KB; September corpus pages 4 → 2 short stubs |
| sources/ | 6,373 | ~6,380 (+README, GROUPS.json, MANIFEST.tsv, directive index) | unchanged bytes; all 59 groups indexed |
| drafts/, worldbuilding/, output/, tmp/ | 1,339 / 164 / 14 / 10 | ~1,340 / 164 / ~16 / 0 | tmp/ ignored; drafts indexed |
| tools/ | 17 | ~35 (+paths, moves, landing, lean_scan, tests) | — |
| **Total** | **70,495** | **~42,400 (−40%)**; ~37,800 with the dedupe | — |

Other end-state figures:
- Working tree: becoming-checks 446 → ~245 MB.
- .git: about −1.9 GB after the cruft gc.
- Local disk: about −228 GB after worktree removal.
- The git-health alternative (manifest-only run folders) would reach about 21–22k tracked files, but only if Ren accepts bytes living only in git history.

### 4.9 Decisions for Ren (recommended option first)

1. **Moves or navigation only?** Recommended: move only the untied sets (H1–H7), each with a receipt; tied files stay in place with banners.
2. **History naming.** Recommended: a sibling `history/` at the same depth in each area. The hash-addressed `_process/architecture/history/` stays unchanged.
3. **Run-folder copies.** Recommended: a content-addressed store inside the tree, keeping the bytes. Not tarballs, and not git-history-only manifests.
4. **Lean package location.** Recommended: stay at the current path, documented. A top-level `lean/` move would be the optional last batch.
5. **Canonical chapter shape.** Recommended: one file. Generate §8–§10 and the catalogues, cut the three restatements, then revisit splitting into part files.
6. **Banners and log extraction on earlier chapters** (against §11 "不因本章而改写" and AGENTS "original scope"). Recommended: allow prepended dated bilingual banners and verbatim log moves, with the body untouched.
7. **Record history.** Recommended: render folding now; the rebind ledger after a snapshot of every record.
8. **Goal scopes.** Recommended: add an authorization-state field, with Ren marking which of the 11 session-era scopes are closed. Nothing is revoked.
9. **README featured results** (today: four pre-unification ethics records). Recommended: Ren picks 8–12 Part I laws plus the §6.15 conditional, each showing its status.
10. **AGENTS.md rewrite, and the wording of "G0 axiom route"** in AGENTS.md:19 and GOALS:75. Recommended: approve the rewrite stating the folded status.
11. **Corpus pages** (MAP, GLOSSARY, TIMELINE, BOOKS). Recommended: originals to `_process/history/2026-09-consolidation/`, a short current MAP, and GLOSSARY as a pointer to §10 plus a crosswalk.
12. **"Part I" label and §6.15 title.** Recommended: retire "Part I" (no Part II exists), with structural names and old anchors kept as aliases.
13. **Workboard integrator.** Confirm which session integrates now; it gets recorded in the "Now" block.
14. **Git operations.** Recommended: non-forced removal of clean, merged worktrees after the unlanded receipts land, cruft-pack gc with never-expire settings, and no pruning of refs.
15. **Privacy and visibility** (urgent): key revocation, whether the remote stays private, friends' consent, and the Guardian Anarchy copies. Recommended: revoke now; keep the repository private; move third-party and personal material to a private store with tracked stubs.
