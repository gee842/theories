# 1. Repository architecture

[Review summary](README.md) · [Architecture](ARCHITECTURE.md) · [What is proved](PROVED.md) · [What needs to change](CHANGES.md) · [Restructure plan](RESTRUCTURE-PLAN.md)

> AI-authored section of the whole-repository review of 16–17 October 2026 (read-only, HEAD `0cfb9c567`; Claude Opus 5.5 reviewers with adversarial verification). Not Ren's text and not external review. Paths are repository-relative; counts are as measured by the reviewers at that HEAD.

### 1.1 The repository in numbers

At HEAD `0cfb9c567` git tracks **70,495 files** (about 3.4 GB in the checkout, 21,188 distinct blobs). `.git` is 5.8 GB. The private GitHub copy is 1.44 GB, and `main` = `origin/main`.

The files the theory actually lives in are a small fraction:
- **Canonical material** is about 735 files, roughly 1%: the chapter and opening, 229 records, the pure Lean spine, tools, goals and root pages.
- **Timestamped run folders** hold 50,191 files (71%) in 885 folders, most of them Lean checker receipts with frozen copies of sources and logs.
- **Empty files**: 12,647 tracked files have zero bytes, nearly all `.log`.

| Top level | Tracked files | Notes |
|---|---|---|
| `experiments/` | 57,568 | 52,696 under `integrated-correction/`, and 51,163 of those in its `lean/` tree |
| `sources/` | 6,373 | about 1.7 GB on disk, 1.35 GB of it third-party data and AI-session snapshots |
| `_process/` | 4,289 | 3,641 in the single study folder `2026-10-05-generative-foundation-review/` |
| `drafts/` | 1,339 | 1,113 of them the IASEAI paper line v1–v7.3 |
| `theories/` | 704 | 643 in `becoming/`; 61 in 16 frozen September branch folders |
| `worldbuilding/` | 164 | self-contained subproject, 159 MB of binaries |
| `tools/` | 17 | `tools/research/`: 9 modules and 7 test files |
| `output/`, `tmp/` | 15, 10 | exports and scratch, both tracked |
| root files | 12 `.md` plus `Makefile`, CI | 1.2 MB in all; `DEPENDENCIES.md` alone is 555 KB |

Growth in tracked files: 3,889 on 10-05, 41,518 on 10-10, 70,495 on 10-16. Almost all of the growth is receipts and copies, not theory.

### 1.2 The layers as they are now

Read from the top down, each layer depends on the ones below it.

| # | Layer | Location | Size | Status |
|---|---|---|---|---|
| 0 | **Front door** | `README.md` (generated from `theories/becoming/OPENING.md`, prose hard-coded at `tools/research/navigation.py:220`, and 4 featured records), `RESULTS.md`, `GOALS.md`, `OPEN-QUESTIONS.md`, `DEPENDENCIES.md`, `RESEARCH.md`, `AGENTS.md` | 12 root pages | `AGENTS.md` is hand-written; 6 pages are generated; `MAP`/`GLOSSARY`/`TIMELINE`/`BOOKS` are September hand-written pages still linked as current |
| 1 | **Canonical statement** | `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md` and `theories/becoming/OPENING.md` | 962,442 B in 1,897 lines (single lines up to 12.4 KB); opening 23 KB | Canonical. The chapter states the theory three times: "stated in full" (L60–127, 72 KB), the body §1–§6.15, and "Part I stated whole" (L1131–1327, 108 KB). Apparatus: §8 open programme, §9 module table, §10 glossary |
| 1′ | **Method** | `theories/becoming/chapters/NONDUAL-METHOD.md` | 26 KB | Required reading (AGENTS); English only |
| 2 | **Result records** | `theories/becoming/results/records/*.json` (canonical) and `*.md` (generated) | 229 records: 458 files, 23 MB (12.3 MB JSON, 11 MB pages) | 210 theorem / 7 assessment / 5 argument / 4 open target (by kind). 117 on schema 1, 112 on schema 2. 138 have their canonical source in the Becoming package |
| 3a | **Lean spine: core** | `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/*.lean` plus root `Becoming.lean` | 128 core modules + root; 6,918 core theorems | Pure. The closure is CORE (129) + FOUNDATION (3, in other folders: `lean/GenerativeCore.lean`, `lean/inquiry-root/sufficiency/InquirySufficiency.lean`, `lean/deeper/RelationalRenewal.lean`) = 132 modules. Compiles from the prelude; empty core axiom report |
| 3b | **Lean spine: bridge** | same folder: `Bridge`, `CompositionBridge`, `CoursesBridge`, `GranularityBridge`, `Instances`, `JoiningBridge`, `RenewalBridge`, `RepairComparison` | 8 modules | Imports periphery modules, restates them on the core (`*_by_core`). Spine = 137 modules, 7,214 theorems (receipt 20261016T124157.989030Z) |
| 3c | **Lean periphery** | `lean/universal-ethics/` (143 live modules), `lean/deeper/` (95), `lean/inquiry-root/` (26 + 46 in `sufficiency/`), `systems-complexity/`, `learning/`, `naturalism/`, `conditional/`, root `lean/*.lean` (32); also `experiments/market-generativity`, `shared-renewal-capability`, `valuation-development` | about 450 live modules, mostly 6–9 October | 45 periphery modules are compiled in each spine run as inherited modules. Mathlib modules use Lean 4.30.0-rc2 against an external pin (`lean/periphery-mathlib-pin`). `Becoming/FallibleInquiry.lean` is periphery code sitting in the core folder, with its own checker |
| 3d | **Checker and receipts** | `lean/becoming/check_becoming.py` (2,334 lines, 67% of it SCOPE prose), `scratch_build.py`, `becoming-verification.json` (2.4 MB), `becoming-checks/` | 171 runs, 31,786 files, 446 MB (3,014 unique blobs) | Enforcement is real: closure purity, a `#print axioms` check per declaration, environment `collectAxioms`, a prelude-only recompile, and failure on any warning. The step cache lives at `~/.cache/becoming-lean` (3.4 GB, outside the repo). Records bind 36 of the 171 runs |
| 4 | **Studies** | `_process/research/2026-10-05-generative-foundation-review/root-foundation/` | 2,208 flat files plus `development/` (1,274) and 4 small evidence subfolders | The live study is `BECOMING-RENEWAL-READING.md` (2.39 MB, §1–§165, 158 records bind its sha256). Also `DELEGATED-CHOICES.md` (D1–D39), `MODULE-CLASSIFICATION.md` (I4a), 19 review reports and the plans. About 123 files are live; the rest are 5–9 October packets |
| 4′ | **Earlier studies** | nine other folders in `_process/research/2026-10-0{4,5}-*` | 469 files | Historical. Linked from no current navigation |
| 5 | **Earlier chapters** | the other 138 files in `theories/becoming/chapters/` (+ `verification/`, 13 files) | 6.3 MB; 128 files last changed on or before 10-10 | Mostly historical. About 20 are still current or record-bound (§2 of this report). Only §11 of the canonical chapter classifies them |
| 6 | **Experiments** | `experiments/*` (22 directories outside `integrated-correction`) and the non-Lean parts of `integrated-correction/` | 4,872 and 1,533 files | Empirical reanalyses, synthetic cycles, two non-theory projects. 7 records cite this layer |
| 7 | **Sources** | `sources/` | 6,373 files | `15-codex-theory-conversations/` (262 directive records) is the canonical store of Ren's words. 00–14 are imported originals. 16–42 plus the named folders are AI-session snapshots and third-party data. `SOURCES.md` (369 KB) is the only manifest, and it stops at 10-09 |
| 8 | **Navigation and catalogues** | `theories/becoming/results/*.md`, `results/data/`, `results/lean-declarations/` | 28 files, 19 MB (`lean-index.json` 8.2 MB) | Generated by six generators in `tools/research/`. Only `registry.py` and `navigation.py` run inside `make research-check` |
| 9 | **Governance** | `AGENTS.md`, `_process/RESULT-WORKFLOW.md`, `_process/goals/*.json` (15), `_process/RESEARCH-DIRECTIVES.md` (70 KB), `_process/BECOMING-WORKBOARD.md` (276 KB), `_process/research-config.json` | — | Hand-kept except `GOALS.md` (generated from the goal JSON) |
| 10 | **History mechanism** | `_process/architecture/` | 120 files: `history/` 113 files, 12 MB in 99 hash-named directories; `rename-2026-10-09.json` 780 KB; `check_rename.py` | Sound but opaque: 14 view versions, each kept twice (raw + reading edition), plus 85 record snapshots |
| 11 | **Outside the theory** | `theories/<16 branch folders>/`, `drafts/`, `worldbuilding/`, `output/`, `tmp/`, `experiments/circular-construction`, `experiments/guardian-anarchy` (gitlink, no `.gitmodules`) | — | Reached only through the frozen `MAP.md` |

### 1.3 Working flow (how a result reaches `main`)

The flow below is reconstructed from the board, AGENTS.md, the landing kits and the checker:

1. **Claim.** Add a row to `_process/BECOMING-WORKBOARD.md`. AGENTS requires this before new Lean ("One theory, worked together").
2. **Scratch.** Work in a git worktree under `.claude/worktrees/`, `/private/tmp/…/wt` or `~/.codex/worktrees`. `scratch_build.py` compiles and stores passed steps in the shared cache, using the checker's own cache keys (toolchain, binary sha, step bytes, closure keys).
3. **Check.** `check_becoming.py` writes `becoming-checks/<UTC>/verification.json` together with drivers, logs and copied sources. The latest receipt is copied to `becoming-verification.json`. Periphery modules have their own `check*.py` (117 in `universal-ethics` alone) and their own `*-checks/<UTC>/` folders.
4. **Landing kit.** A folder in `root-foundation/development/becoming-pNN-landing/` holds the Lean copies, study-section drafts (`study_zh.md` and `study_en.md` with `{S}` placeholders), record generators and an `apply_docs.py`/`repoint.py`. Shared tooling lives in `development/becoming-general-laws-plan/integration/` (`rebind_batch.py`, `merge_records.py`, `notes-batch*.json`); it was last used today for P130 (`notes-batch37`) and has no tests. There are 50 such kits.
5. **Record and study.** The new record JSON goes in `results/records/`, a section is appended to `BECOMING-RENEWAL-READING.md`, and the chapter is edited by hand (§9 row, glossary, summaries). Any edit to the chapter or the study puts every record that binds those files by sha256 out of date. They are then rebound, which adds one "rebound, claim unchanged" history note per record: 1,052 from chapter edits and 1,598 from study appends.
6. **Render and check.** `make research-render` runs `navigation.py` (11 overview pages), `registry.render_index` (`RESULT-REGISTER.md`) and the 229 record pages, behind overwrite guards (`_process/architecture/generated-manifest.json`, 242 entries). Then `make research-check` runs: today it reports 0 errors, 0 drift and 440 style warnings. The reading catalogue, Lean catalogue, generativity chain and session map are **not** part of this check, and all four are stale.
7. **Queue and merge.** The board's landing queue sets the order. The integrator merges to `main` and pushes, and the board row is closed. CI (`.github/workflows/research.yml`) should then rerun the test and check targets, but it has not run since 10-15 because of GitHub billing. With a depth-1 checkout it would also fail: 248 record/source pairs report drift when no reviewed versions are available.

What this flow produces as a side effect: about 10 new files per landing, one rebind note per bound record per landing, a full copy of every compiled source in each run folder, and a worktree checkout of about 3.6 GB per agent. 69 such checkouts take about 228 GB on a volume that is 91% full.

### 1.4 What kind of thing each file is

| Class | What belongs here | Where it lives now | Problem |
|---|---|---|---|
| **Canonical (hand-edited, authoritative)** | Chapter, opening, method, record JSON, spine `.lean`, `check_becoming.py`, goal JSON, directive records, directive register, AGENTS, RESULT-WORKFLOW, research-config, curated chain JSON, reading-catalogue JSON, `standard-boundaries.json` | Scattered: `theories/becoming/`, `experiments/…/lean/becoming/`, `_process/`, `sources/15-…`, `theories/becoming/results/data/` | The spine sits 7 levels deep under three superseded 5-October study names. The foundation modules sit in three other folders |
| **Generated (rebuilt from canonical)** | 12 overview pages, 229 record pages, `RESULT-REGISTER`, `ROADMAP`, `CLAIMS`, `BRIEF`, the study README, Lean catalogue (14 files, 17.2 MB), reading catalogue, chain page, receipts | Mixed in among canonical files, with nothing in the name to mark them | 261 generated tracked files, 30 MB. The same 229-row register appears **five** times (`RESULTS`, `RESEARCH`, `theories/becoming/README`, `chapters/CLAIMS`, `results/RESULT-REGISTER`), about 350 KB. `GOALS` and `ROADMAP` repeat each other |
| **Hand-kept duplicates of generated facts** | Chapter §9 module table (130 rows), package README table (106 rows), `Becoming.lean` docstring (122 bullets, 105 KB), `check_becoming.py` SCOPE (1,565 lines), LEAN-INDEX | Five places | Already drifted: 18–21 stale counts, 6 P130 modules missing, the totals cite the superseded receipt (7,089 theorems vs 7,214) |
| **Evidence (frozen, byte-preserved, cited)** | Run folders, review reports, landing kits, edit ledgers (`*-EDITS.json`, 19.4 MB in A–H alone), before-snapshots, source manifests, freeze manifests | In place beside live work, never separated | 96% of the Lean tree (49,259 of 51,163 files). Receipts are cited from thousands of places, and 23 inherited modules have passed receipts only inside run folders (see §1.6) |
| **History (superseded, kept for provenance)** | September corpus pages, 10-07 handoffs, about 110 earlier chapters, about 2,000 study packets, 9 earlier studies, superseded plans | Mostly **not** marked as history. Only `_process/architecture/history/` and the legacy Lean `verification-history/` are labelled | `MAP.md` is linked from every generated page as the "Broader theory map". `GLOSSARY.md` calls itself "the canonical vocabulary" |
| **Scratch** | `tmp/` (10 tracked, including a 9.6 MB tarball), `work/` (empty), `__pycache__`, ignored `.olean` (about 60 MB), 88 registered worktrees (22 prunable), 142 local branches (131 merged) | Partly tracked | `tmp/` and `output/` are tracked; the root `.gitignore` has 3 lines |

### 1.5 Annotated tree (depth 2–4 where it matters)

```
theories/                                   [repo root; 70,495 tracked files]
├─ README.md            gen   41 KB  OPENING + hard-coded intro + 4 pre-unification featured records
├─ RESULTS.md           gen   71 KB  register #1 (229 rows, alphabetical)
├─ RESEARCH.md          gen   74 KB  register #2 (titled "Research navigation")
├─ GOALS.md             gen   48 KB  15 goals, alphabetical (first priority is section 11 of 15)
├─ OPEN-QUESTIONS.md    gen   19 KB  4 open targets; §8 programme and Ren's pending decisions missing
├─ DEPENDENCIES.md      gen  555 KB  587 edge sections, no "used by" index
├─ AGENTS.md            hand  10 KB  working rules; last changed 10-11 (still frames G0 as an adopted axiom route)
├─ MAP / GLOSSARY / TIMELINE / BOOKS.md   hand, Sept., 467 KB together; MAP still linked as current
├─ Makefile, .github/workflows/research.yml   research-check/render/find/test/imports; CI not running
│
├─ theories/
│  ├─ becoming/                             643 files
│  │  ├─ OPENING.md                 canon  Ren's text (v6), AI footnotes, rendered into README
│  │  ├─ README.md                  gen    register #3 + 72 anchor stubs
│  │  ├─ synthesis-{a,b,c}-*.md     hist   444 KB, Sept. AI syntheses of the 生生不息论 corpus
│  │  ├─ chapters/                  152 files, 6.3 MB
│  │  │  ├─ THE-THEORY-OF-BECOMING.md  canon  962 KB; bound by sha256 as the statement source of 104 records
│  │  │  ├─ NONDUAL-METHOD.md          canon  method
│  │  │  ├─ CLAIMS.md                  gen    register #4
│  │  │  ├─ ~20 current/record-bound chapters (KNOWLEDGE, MARKETS-…, PRACTICAL-JUDGMENT, SCIENTIFIC-PHILOSOPHY,
│  │  │  │   WISDOM-AND-CONTEXT, ZERO-AXIOM-PRACTICAL-JUDGMENT, ALIGNMENT-DIRECTION, BECOMING-FOUNDATION, …)
│  │  │  ├─ ~115 historical chapters (5–10 Oct), none linking forward to the canonical chapter
│  │  │  │   largest: UNIFIED-ETHICAL-GROUNDING 412 KB, GENERATIVE-GROUNDING 409 KB, HUIGEN 247 KB
│  │  │  └─ verification/  13 files, 5-Oct release bundle (11 of 15 hashes stale)
│  │  └─ results/                   486 files, 42 MB
│  │     ├─ records/                458 = 229 JSON (canon) + 229 MD (gen), 23 MB
│  │     ├─ RESULT-REGISTER.md      gen    register #5
│  │     ├─ ROADMAP.md              gen    = GOALS.md
│  │     ├─ README.md, THEORY-MAP.md, ARGUMENTS-{A-L,M-Z}.md   gen (10-08 reading catalogue; stale hash)
│  │     ├─ GENERATIVITY-CHAIN.md   curated (Ren-requested), 568 KB; needs-review, no spine links
│  │     ├─ LEAN-INDEX.md, LEAN-DECLARATIONS.md, lean-declarations/ (10 pages, 5.8 MB)   gen; spine not its own group
│  │     ├─ SESSION-RESULTS.md      hist   10-09 session map
│  │     └─ data/                   8 files, 11 MB (lean-index.json 8.2 MB, committed 90 times)
│  └─ <16 branch folders>/          61 files, 55 MB; Sept. syntheses; only meta-attractor/ live
│
├─ experiments/                             57,568 files
│  ├─ integrated-correction/                52,696
│  │  ├─ README, CENTRAL-CLAIM, model/, … hist   5-Oct financial ODE study, still the entry README of the spine's tree
│  │  └─ general-framework/
│  │     ├─ README, closure-study/, gap-resolution/, reproduction-test/   hist (5 Oct)
│  │     └─ generative-basis/
│  │        ├─ README, formal/, checks/ …   hist (5 Oct)
│  │        ├─ mathematical-abstraction/ (543), noninstrumental-concern/ (336), ecological-selection/ (216),
│  │        │  inquiry-correspondence/ (98, canonical source of 4 empirical records), …
│  │        └─ lean/                        51,163 files, 848 MB on disk; README = 6-Oct changelog
│  │           ├─ becoming/                 31,995
│  │           │  ├─ Becoming.lean          root: 128 imports + about 1,130 lines of catalogue docstring
│  │           │  ├─ Becoming/              137 .lean = 128 core + 8 bridge + FallibleInquiry (periphery)
│  │           │  ├─ check_becoming.py, scratch_build.py, check_fallible_inquiry.py, lean-toolchain (4.29.1)
│  │           │  ├─ becoming-verification.json   current receipt (215/215 module hashes match HEAD)
│  │           │  ├─ README.md              250 KB; table lists 106 of 136 spine modules
│  │           │  ├─ becoming-checks/       171 runs, 31,786 files, 446 MB (13,817 .lean copies, 1,694 unique)
│  │           │  └─ fallible-inquiry-checks/  64 files
│  │           ├─ GenerativeCore.lean       FOUNDATION L0 (lives at lean root)
│  │           ├─ deeper/                   2,700 (95 modules; RelationalRenewal = FOUNDATION; 155 run folders)
│  │           ├─ inquiry-root/             2,954 (sufficiency/InquirySufficiency = FOUNDATION; 76 runs)
│  │           ├─ universal-ethics/         11,848 (143 modules; 345 run folders = 93% of its files;
│  │           │                             generative-capacity/check.py is the audit helper the core checker imports)
│  │           ├─ systems-complexity/ (563), learning/ (193), naturalism/ (55), conditional/ (45), connected/ (357, frozen)
│  │           └─ verification-history/, legacy-replays/, verification-runs/, verification/   hist (10-06)
│  ├─ shared-renewal-capability/            2,459 (16-level nested chain; paths up to 288 chars)
│  ├─ agentdojo-evidence-boundary/ (925), market-generativity/ (487, 10 records), valuation-development/ (32)
│  ├─ 5 retrospective empirical reanalyses, 10 synthetic 4–5 Oct cycles, 2 game studies, 1 RL pilot
│  ├─ circular-construction/ (482 tracked, 960 MB on disk), guardian-anarchy (gitlink, no .gitmodules)
│  └─ README.md                             hand, 23 dated status paragraphs; never mentions the spine
│
├─ _process/                                4,289 files
│  ├─ BECOMING-WORKBOARD.md         current  276 KB claim board + landing log (9 stale "handed to integrator" rows)
│  ├─ RESEARCH-DIRECTIVES.md        canon    70 KB register (links 55 of 264 directive records)
│  ├─ RESULT-WORKFLOW.md, research-config.json, goals/ (15 JSON)   canon
│  ├─ BRIEF.md                      gen      boilerplate (AGENTS start page)
│  ├─ THEORY-DIGEST, COVERAGE, CRITIQUE-FINDINGS, LOST-ARTIFACTS, CLOUD-HANDOFF-…, handoffs/ (9),
│  │  reading-notes/ (21, 4.2 MB), timeline-raw.tsv, read-pass-1-plan.json   Sept./10-07 layer
│  ├─ architecture/                 120: generated-manifest, history-manifest, history/ (12 MB), 10-09 rename receipt
│  └─ research/
│     ├─ README.md                  lists none of the studies
│     ├─ 2026-10-0{4,5}-*  (9 studies)      469 files, historical, orphaned from navigation
│     └─ 2026-10-05-generative-foundation-review/   3,641 files
│        ├─ REVIEW.md, FOUNDATION*.md, OPTIMAL-FOUNDATION.md, final-synthesis/, …   5-Oct dossier (hist)
│        ├─ foundation-assessment/ (105; 5 market records bind one file)
│        └─ root-foundation/
│           ├─ 2,208 flat files: about 123 live (BECOMING-RENEWAL-READING 2.39 MB, DELEGATED-CHOICES,
│           │   MODULE-CLASSIFICATION, THEOREM-CONNECTIVITY, 19 reviews, plans, record-bound packets)
│           │   + about 2,085 packets from 5–9 Oct (147 checkers, 377 receipts, 199 edit ledgers = 11.8 MB)
│           ├─ development/          1,274 files, 32 MB, no index: 50 spent landing kits, live landing tools,
│           │                        I4a pipeline, 10-06 before-snapshots (bytes exist nowhere else)
│           └─ reason-action-, recipient-renewal-, semantic-action-evidence/, pretraining-review/
│
├─ sources/                                 6,373 files, about 1.7 GB on disk
│  ├─ SOURCES.md                    369 KB only manifest; stopped 10-09; 43 broken links
│  ├─ 00–14                         imported originals (2021 → 09-2026), byte-preserved
│  ├─ 15-codex-theory-conversations/   262 directive records, canonical for Ren's words (2,254 files reference it)
│  ├─ 15-user-provided-2026-09-06/  second "15-"
│  ├─ 16–42 + named folders         Ren directions (16), friend ASR (18), AI session snapshots (20: 2,402 files,
│  │                                341 MB), third-party data (situated-recovery 423 MB plain git + 185 MB LFS,
│  │                                evolutionary-selection 348 MB); 32- and 36- each used twice
│
├─ tools/research/                  9 modules (research, registry, navigation, style, reading_catalogue,
│                                   lean_catalogue, generative_chain, session_map) + tests (101 tests)
├─ drafts/ (1,339), worldbuilding/ (164), output/ (15), tmp/ (10)   outside the theory
└─ .claude/worktrees/               58 directories, about 189 GB (excluded only via .git/info/exclude)
```

### 1.6 Main structural problems (ranked)

1. **There is no single place that says what is established.** The front door features four G0/J/assessment records from before the unification. No top-level page gives theorem counts or the spine's headline laws, and only 7 of the 138 Becoming-sourced records are linked from any goal. The canonical chapter carries that content, but it is 962 KB and states the theory three times (§1.2 layer 1). Its §9 count (7,089) trails the receipt (7,214), and it never mentions `Becoming.Runs` or the other P130 modules. *(major; this is what a reader actually hits)*

2. **Generated facts are kept by hand in five places, and they disagree.** The module catalogue lives in the chapter §9 table, the package README, the `Becoming.lean` docstring, the checker SCOPE and LEAN-INDEX. The register is rendered five times. The goals are rendered twice. Every landing therefore needs hand edits that drift, and Chinese/English parity breaks in exactly this hand-kept apparatus: the premise card, §8 table, §9 table and §10 glossary are Chinese only. *(major)*

3. **The rebind cascade comes from coupling by whole-file hashes.** 104 records bind the whole chapter by sha256, and 158 bind the whole 2.39 MB study log. Any edit or append forces a rebind. 62% of record history entries (5,365 of 7,564, 4.8 MB) are "rebound, claim unchanged". Coupling at this grain also makes any move or split of those two files a drift event for hundreds of records. *(major; the root cause of much of the bloat)*

4. **Evidence, history and live work are not separated.**
   - 71% of tracked files sit in run folders, and only 98 of the 885 folders are bound by a record. In the Lean tree, 96% of files are snapshots or runs.
   - About 110 earlier chapters, about 2,085 study packets, 9 orphaned studies, the September corpus pages and 50 spent landing kits all sit beside live files.
   - None of these carries a status banner. Several still say "current", "active", or that G0 "is an adopted axiom".
   - The only classifier for the chapters is §11 of the canonical chapter, which lists G0-WARRANT as active and omits three live Codex-line chapters. *(major)*

5. **Location does not match role.**
   - The pure core sits under `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/`, three superseded 5-October study names deep. Its three FOUNDATION modules sit in three other folders. A periphery module (`FallibleInquiry`) sits in the core folder.
   - Each README on the path down to the spine (integrated-correction, general-framework, generative-basis, lean) is a stale changelog, and none links `lean/becoming/README.md`.
   - Relocating is expensive: 3,009 files contain the path string, and 124 scripts use fixed `parents[N]`. *(major, but only fixable at a quiet merged point and with Ren's go)*

6. **Verification signal is weaker than it looks.**
   - CI has been dead since 10-15, and it would fail on a shallow checkout even after billing is fixed.
   - Four of six generators are outside `research-check`, and all four are stale.
   - The committed receipt is a cached run: 44 steps ran and 659 were reused, 270 of them with logs only in `~/.cache`.
   - The fresh I5 run (703 steps, 0 reused, empty core axiom report) survives only as a summary without source hashes; its full receipt was in a wiped `/private/tmp` path. *(major for a "complete" claim; the proofs themselves are sound)*

7. **Hidden constraints block naive cleanup.**
   - The core checker's `passed_receipts` scans `LEAN_ROOT.rglob('*.json')`, and 23 inherited spine modules have passed receipts only inside `deeper/*-checks/<run>/`. Run folders therefore cannot leave the Lean root unless fresh consolidated receipts are issued first.
   - The chain's discovery glob is `root-foundation/*.md`, and `registry.reviewed_version` uses `git log --no-renames`.
   - The 10-09 rename tooling is tied to one receipt and has no generator committed.
   - A directory named exactly `history`, placed at the same depth as what it holds, is already excluded by the checker, `research.py working()` and the preservation list. That makes it the safe target layout. *(major; this governs the restructure plan)*

8. **Coordination state is stale.**
   - The board still shows P118–P127 and P108 as "verified in scratch, handed to the integrator", and Part II as "awaits Ren".
   - The first-priority goal's "Next" field is the 10-11 redirect.
   - AGENTS.md predates the P128 fold.
   - Governing Ren messages from 10-10 to 10-16 ("please, do all", "let's finish both", the review request itself) have no directive record, and the register misses 19 directive records from 10-09 to 10-16. *(major for provenance; minor in effort)*

9. **Physical health.**
   - There are 69 live worktree checkouts of about 3.6 GB each on a disk that is 91% full. All are merged, but one holds the only copy of a run cited on `main` (`20261011T170859.998618Z`).
   - Inside `.git`: 344 MB of `tmp_obj_*` garbage and a 1.82 GB pack wholly contained in another. `gc.pruneExpire=never` is set without matching reflog and worktree expiry.
   - Other loose ends: a gitlink without `.gitmodules`, tracked `tmp/` and `output/`, and 789 paths over 260 bytes. *(major for disk; minor for the theory)*

10. **The source layer is weakly indexed.**
    - `SOURCES.md` is a 369 KB append log that stopped on 10-09.
    - `make research-find` skips `sources/` entirely, and it skips files over 2 MB, which includes the main study.
    - Two folders are numbered `15-`, and 32 and 36 are each used twice.
    - About 14 AI research write-ups are filed among Ren's directives.
    - Of the 6,373 tracked source files, 1.35 GB is third-party data that could be downloaded again, while Ren's own 213 MB of audio exists only on local disk. *(minor to major, depending on what is being looked up)*
