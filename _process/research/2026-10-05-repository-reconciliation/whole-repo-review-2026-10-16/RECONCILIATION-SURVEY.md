# Docs reconciliation plan (agent H, read-only survey, 17 Oct 2026)

> Saved 17 October 2026 from the read-only survey by agent H. Tiers 1–2 were carried out (receipts RA–RE, RG; see [the restructure report](RESTRUCTURE-REPORT.md)); tier 3 awaits Ren. Paths named `scratchpad/recon/*.tsv` are the plans now in `_process/architecture/moves/plans/reconciliation/`.

Ren (17 Oct): "a lot files may overlap or just speaking about the same thing in different places, please do a docs reconciliation after restructuring."

Survey of main at f583ce6b4 plus the uncommitted work in flight (language splits in chapters/studies/meta-attractor, navigation.py stubs, goal `state` fields). Nothing in the repository was edited. Ready-made move plans are in `scratchpad/recon/R?.tsv`; all rows are also listed in the appendix. Every old path was checked against `git ls-files -z`; no new path exists yet.

## How the survey was done

- Scope: 20,299 live tracked files (not `sources/`, any `history/`, `.claude/`). Of these, 777 Markdown files outside drafts/, worldbuilding/, records and lean-declarations, with evidence paths excluded (runs/, frozen/, snapshots/, review-history/, checks/<n>/, becoming-checks, timestamp folders).
- Exact duplicates: grouped by git blob id (`git ls-files -s`).
- Near-duplicates: character 40-gram shingles (sampled 1/16) over normalized text (link targets, anchors and Markdown punctuation removed). For each pair, containment = shared / own shingles. A second pass on chapters, studies and records used 30-grams (1/8), and a third used sentence-level trigram matching on the hand-written process pages.
- Pins were checked against `_process/architecture/moves/plans/PINNED.tsv`, freeze JSONs and `.py` hard-coding. Record citations were checked by grepping `results/records/*.json`, and goal citations by grepping `_process/goals/*.json`.

## Main finding

Text-level duplication among live hand-written docs is small. The 32 kept chapters share almost no text with each other (highest containment 2%) or with the new English canonical chapter (below 1%). The rewritten process pages (AGENTS, RESULT-WORKFLOW, REPOSITORY-LAYOUT, MAP, tools README, architecture README, board) share at most 1–5 sentences per pair. The real overlap is in four places:

1. **Generated pages that repeat each other.** The 229-row register appears five times, and the scope list twice.
2. **Superseded versions still live in dated projects.** IASEAI v3–v7.2 hold 970 files; there are also whitepaper v0.1–v1.0 and the opening drafts.
3. **Applied kits and byte copies left beside live files.** These are the agentdojo `integration/before/` + `rebased-*` copies and the-fork `revisions/`.
4. **The same thing explained in several places.**
   - "Where to start" and "what lives where" appear in 4–5 pages.
   - Six READMEs are stacked dated status logs.
   - Four executed study plans remain live.
   - A few pages make statements the restructure has made false.

The order below is by value per effort. Tiers 1–2 need no Ren decision and fit in about two hours. Tier 3 needs Ren. Tier 4 is optional.

## Preconditions (all tiers)

- Run after the language-split agents and the navigation agent have finished and the integrator has committed their work. Several rows below name `.zh.md` files that are still untracked: CONTINUATION-GROUNDING-PLAN, PART-II-INVENTORY, the P42-P43/P49/RENEWAL-READING reviews, and THEORY-OF-BECOMING/BECOMING-FOUNDATION/G0-WARRANT. The move tool checks blob identity, so these must be committed first. Re-run the row validation (the snippet at the end) right before each move, because more `.zh.md` siblings may have appeared. Each `.zh.md` moves with its English file.
- Per batch:
  1. `python3 -B tools/research/research.py move --plan <tsv> --summary`.
  2. Read the conflicts, then `--apply --batch R<n>`.
  3. Verify with `research.py move --check _process/architecture/moves/R<n>.json`.
  4. Run `make research-check` (errors []), `research.py links` (no new broken links over the 1213 baseline), `make research-test`, and `make research-render` (integrator only).
- Records: every item below is a **move** (paths re-keyed, hashes carried) or a **shorten-in-place of an uncited page**. **No item merges a record-cited file.** The only rebinding needed is the normal path re-key the tool does. Flags are given where a record or goal names a path.

---

## Tier 1: no Ren decision, high value

### 1. Register and scope copies (generated): finish the stubs. In flight, so verify, don't redo

- **Files:** `RESULTS.md`, `RESEARCH.md`, `theories/becoming/README.md`, `theories/becoming/chapters/CLAIMS.md`, `theories/becoming/results/RESULT-REGISTER.md`, `GOALS.md`, `theories/becoming/results/ROADMAP.md`.
- **Evidence:** containment RESEARCH→RESULTS 0.95; RESULTS→theories/becoming/README 1.00; RESULTS→CLAIMS 1.00; CLAIMS→RESEARCH 0.97; GOALS→ROADMAP 1.00 (ROADMAP→GOALS 0.96). The same headings appear in all of them: "Registered results", "Discovery and evidence", "Preserved history", and the 13 goal headings in both GOALS and ROADMAP.
- **Most informative:** `RESULTS.md` (register) and `GOALS.md` (scopes).
- **Action:** stubs, as RESTRUCTURE-PLAN §4.5 says. The uncommitted `tools/research/navigation.py` diff already adds `stub` kinds for RESEARCH.md, theories/becoming/README.md and CLAIMS.md, and a `roadmap` stub for ROADMAP.md. Check after the next render that:
  - (a) each stub keeps its `<a id>` blocks, so inbound links resolve (RESEARCH.md has 80 referrers and CLAIMS.md up to 192);
  - (b) `results/RESULT-REGISTER.md` is also reduced. It is written by `registry.py`/`build_result_registry`, not by `navigation.PAGES`, and is **not yet in the stub list**. Make it a stub to RESULTS.md as well, or state why it stays;
  - (c) theories/becoming/README.md becomes a folder index (OPENING, canonical chapter, chapters/, results/, history/), not a fourth register.

### 2. Applied integration kit with byte copies (experiments, agentdojo)

- **Files:** `experiments/agentdojo-evidence-boundary/correction-action/continuation/integration/`. It holds 19 files: `BEFORE.json`, `CHECKS.json`, `README-EDIT.json`, `REBASED-EDITS.json`, `RESULT.json`, and `before/00..07-*.md`, `before/rebased-00..04-*.md`, `before/continuation-README.md`.
- **Evidence:** `before/01-README.md` vs `before/rebased-01-README.md` Jaccard 1.00. Pairs 00/rebased-00 and 02/rebased-02 are 0.99. `06-` and `rebased-04-ALIGNMENT-FRONTIER-ASSESSMENT.md` are byte-identical. `before/04-ALIGNMENT-COMPLETION.md` is 0.99 contained in `chapters/ALIGNMENT-COMPLETION.md`. `before/05-README.md` is 0.99 of `foundation-assessment/README.md`.
- These are the "before" snapshots of an edit kit applied on 6 October. There are 0 records and 0 live referrers. Only receipts mention the path: H5.json, review-data.json and the kit's own JSON. No checker reads it (the only `.py` that names it is already in history).
- **Action:** retire the whole kit as one unit (an applied kit, as in H5). See `RA.tsv`, row 1.

### 3. The fork's byte copy of its own README

- **Files:** `theories/the-fork-and-cooperative-infrastructure/revisions/2026-09-07-before-productive-foundation.md` and `revisions/README.md`.
- **Evidence:** 0.91 of the copy is contained in the live README; its own README calls it an "exact byte copy of the previous main README". This is exactly what Ren's rule ("never keep copies beside live files") forbids.
- **Action:** rename the directory to the sibling `history/`. The depth is the same, so the copy's relative links still resolve. See `RA.tsv`, row 2. The tool rewrites the two referrers: the fork README and `worldbuilding/research/2026-09-07-abundance-source-reading.md`.

### 4. IASEAI paper: eleven superseded editions live (dated project, clear duplicates)

- **Files:** `drafts/2026-10-02-iaseai-selecting-the-selectors/` holds `v3 v4 v5 v5-codex v6 v6-planning v6.1 v6.2 v7 v7.1 v7.2` and `versions/v1`, plus `V3/V5/V6/V6.1-PLAN.md`. That is 970 tracked files, about 35 MB.
- **Evidence:**
  - 72 groups of byte-identical Markdown across editions. Examples: `src/supp/07_S7.md` is identical in v6.2, v7, v7.1, v7.2 and v7.3; `src/supp/02_S2.md` is identical in v7 through v7.3; many core sections of v7.2 and v7.3 are identical.
  - `v6.2/planning/snapshots/draftA/` duplicates v6.1.
  - v7.3 (2026-10-05 00:11) is the newest edition. Its README, CHANGELOG and CLAIMS describe themselves as extending the preserved earlier editions.
- **Most informative:** `v7.3/`. Keep as well: `submission/`, `build/`, `output/`, `reviews/`, `experiment/`, `supporting-material/`, `NOTES.md`, the PDF and `TALK-PROPOSAL-2026-10-06.json`. These are the v2 submission state and talk materials, and which edition was submitted is not recorded.
- **Pins:** no record, goal or freeze pins any edition path.
  - `V73-INTEGRATION-CHECKS.json` names only v7.3, which stays.
  - `SESSION-OUTCOME-SNAPSHOT.json` names v7.2. It is a snapshot (evidence), so it is not rewritten and its old path resolves through the manifest.
  - `v7.3/checks_v73.py` mentions `../v6.2` etc. only in its docstring.
  - Live referrers that the tool will rewrite: `theories/meta-attractor/README.md` (v6.1), `theories/relational-self-and-datong/README.md`, `GFR/root-foundation/META-ATTRACTOR-RECONCILIATION.md`, `results/SESSION-RESULTS.md`, `results/data/session-results.json`, `results/data/source-index.json`, `drafts/2026-10-04-no-safe-way-to-win/TALK.md`, `drafts/2026-10-04-soi-si-lom-5-2/integration/*`, and links inside v7.3 and supporting-material.
- **Action:** retire to `drafts/2026-10-02-iaseai-selecting-the-selectors/history/<edition>/` (`RB.tsv`, 16 rows). Afterwards, add a 10-line `README.md` at the project root: v7.3 is current, `history/` holds the editions, `submission/` is the submitted v2. Optionally, the integrator can add a status line to `NOTES.md` saying it describes v2.

### 5. Executed study plans still live (root-foundation)

| File | Status in its own text | Superseded by | Records |
|---|---|---|---|
| `REGISTRATION-AND-TESTING-PLAN.md` | "the stage is done as unification plan P49" | record testing-within-registration, study §70 | 2 |
| `WUMING-BOUNDARY-PLAN.md` | "B1 and B2 are stated and checked as … P62 … B5 in `Becoming.Capture`" | the P62 modules `Becoming.Seeking` and `Becoming.Capture` and their records | 2 |
| `CONTINUATION-GROUNDING-PLAN.md` (+ `.zh.md`) | plan for P39–P44, all landed | canonical §6.7–6.11; records one-axiom-yields-g0, feedback-and-reach, axiom-decomposition | 5 |
| `PART-II-INVENTORY.md` + `.py` (+ `.zh.md`) | inventory of Part II on 11 Oct; Part II was folded by P128 (16 Oct) | canonical §6.15 (it cites the inventory as "the inventory of 11 October", which is dated evidence) | 0 |

- **Action:** retire to `_process/research/2026-10-05-generative-foundation-review/history/root-foundation/` (`RD.tsv`).
- **Note:** RESTRUCTURE-PLAN §4.4 said to append dated status lines to these plans. This item goes further, under Ren's 17 Oct "only the latest, most informative version stays live". **The integrator should confirm the deviation.** If not, append the status lines instead.
- Keep `BECOMING-UNIFICATION-PLAN.md` (the P-number register; cited by 41 records), `ZERO-PREMISE-PLAN.md` (its inventory script is live), `THEOREM-CONNECTIVITY.*`, `DECIDABILITY-INVENTORY.*` and `DELEGATED-CHOICES.md` (cited by canonical §8). They get status lines only.
- `PART-II-INVENTORY.py` moves one level deeper. It is not run by any checker, and once moved it is evidence.
- Ren's words quoted in these plans stay verbatim in the moved files. Each is also in `sources/15-*`.

### 6. Statements made false by the restructure (hand pages; small edits)

| Page | Stale text | Fix |
|---|---|---|
| `_process/REPOSITORY-LAYOUT.md` | "Each batch also writes a receipt `_process/architecture/moves/moves-<date>-<batch>.{json,tsv}`, verified by `check_moves.py`". In fact the receipts are `moves/H1.json`… with plans in `moves/plans/*.tsv`, there is no `check_moves.py`, and verification is `research.py move --check RECEIPT`. Also "Some of these pages … arrive batch by batch", "`chapters/CLAIMS.md` and `results/RESULT-REGISTER.md` become stubs", and "(… `evidence restore`, being built)". | Correct the receipt and check names. Drop the transitional sentence after Tier 1 item 1 lands. Put "being built" in the present tense only if `evidence restore` exists. |
| `_process/architecture/moves/plans/README.md` | "Status: **plan only. Nothing has been moved, added or committed.**" | Add a status line: H1–H7 applied in 71edc7b91…19c1acfa4, with the receipts named. |
| `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md` §11 (L1608, L1647) | "Until the plan is carried out, those files remain in `chapters/`" and "Under plan H4 they move …" | Past tense: they moved to `../history/` (receipt H4.json). This goes through the integrator's canonical queue, not a direct edit. |
| `_process/research/README.md` (7 lines) | Says studies are not moved and that RESEARCH.md is "the single research index". Both are false now. | Shorten to a pointer (see `RG.tsv` last row, a `--keep-references` replace). The new text lists the live studies (generative-foundation-review; concern-theory, freeze-pinned; the pinned remnants of integrated-evolution, causal-foundations, generative-health, revisable-concern and support-and-shared-generativity; repository-reconciliation) and points to `_process/history/INDEX.md` and REPOSITORY-LAYOUT. |
| `_process/reading-notes/README.md` | The "input files" table describes `hb-*`/`cb-*` as present; H1 moved them. | One line: the inputs are in `_process/history/…` (H1 receipt). The out-* files stay. |

---

## Tier 2: no Ren decision, medium value

### 7. "Where to start" and "what lives where" said in 4–5 places

- **Files:** `AGENTS.md` "Start here" (Ren's text); `MAP.md` "Where to start" and "Top-level layout" table; `_process/REPOSITORY-LAYOUT.md` target tree and "Where things go"; `_process/navigation/REPOSITORY.md` (new, in flight; it renders the same "Location | Responsibility" table into README and BRIEF); `_process/BRIEF.md` (generated).
- **Evidence:** the README/BRIEF table rows (`theories/`, `_process/research/`, `experiments/`, `sources/`, `tools/research/`) restate MAP's table. MAP's table restates LAYOUT's tree (2 near-identical sentences). The reading order README → canonical → method → results/goals appears in AGENTS, MAP and BRIEF.
- **Action (merge):**
  - **MAP.md** becomes the single reader-facing "where to start + top-level layout" page.
  - **REPOSITORY-LAYOUT** stays the writer-facing rules page. Remove its prose "areas" paragraphs that only restate the tree, and keep the rules (history layout, path roles, evidence store, where-things-go).
  - **`_process/navigation/REPOSITORY.md`** should drop its location table and link to MAP, so README and BRIEF carry the reading order and one link.
  - Leave AGENTS "Start here" as is (Ren's text). It is agent-facing and consistent with MAP.
  - Add a link from MAP's "earlier theory folders" table to `results/THEORY-MAP.md` (the long generated bilingual branch readings), so the two are not parallel indexes.

### 8. Stacked dated status logs used as READMEs (replace pattern: `--keep-references`, `RG.tsv`)

| README | Stacked dated paragraphs | Size | Pins / records |
|---|---|---|---|
| `GFR/foundation-assessment/README.md` | 8 (all 6 Oct) | 8.5 KB | 0 records. Its insertions are recorded in `*-INDEX-EDITS.json` ledgers (evidence, not re-checked by any live checker; FRONTIER-CHECK reads only `FRONTIER-*.md`, ALIGNMENT-COMPLETION and two sources READMEs). |
| `lean/deeper/README.md` | 34 | 31 KB | none |
| `lean/universal-ethics/generative-capacity/README.md` | 10 | 44 KB | none |
| `lean/inquiry-root/README.md` | 11 | 21 KB | none |
| `lean/universal-ethics/README.md` | 12 | 11 KB | none |
| `generative-basis/mathematical-abstraction/README.md`, `…/constitution/README.md` | 11, 8 | 12 KB, 8 KB | none |

- **Action:** move each original byte-for-byte to the sibling `history/`, using the same-depth paths in `RG.tsv` (`lean/history/<dir>/README.md` beside H7's run folders; `generative-basis/history/mathematical-abstraction/…`). Then write a short index at the old path: module, checker, latest receipt, and the records that bind it, read off the directory, plus one line pointing to the status log in history.
- Inbound links are not rewritten; they still land on the new index.
- This closes open decision 4 in `moves/plans/README.md` for the README only. The MARKET-* files in foundation-assessment stay, because they are record-bound and depth-pinned.

### 9. Spine reviews of 9–11 October (evidence, not current)

- **Files:** 17 `BECOMING-*-REVIEW.md` in root-foundation (P7 … P49, R1-R2, RENEWAL-READING-REVIEW), about 1.2 MB, plus 3 `.zh.md` siblings. Each is cited by 1–8 records; none is read by a checker.
- **Why:** AGENTS says "frozen copies and repeated reviews are evidence, not results". The current review state is in `BECOMING-EIGHTEENTH-REVIEW`, `BECOMING-RELEASE-READINESS-REVIEW` and `BECOMING-GENERAL-LAWS-REVIEW`, which stay, and canonical §8.8 summarizes the review status.
- **Action:** retire to the study's `history/root-foundation/` (`RE.tsv`). The tool re-keys the records' paths with hashes carried, so no rebinding is needed. This is the integrator's call: H5 kept them under "class 1", and moving them is reversible.

### 10. Older whitepaper editions (dated project)

- **Files:** in `drafts/2026-09-05-generative-foundations/`: `WHITEPAPER.md` (which is v0.1, 5 Sep), `WHITEPAPER-v0.2…v1.0.md`, `README-v1.0.md`, `宣言-v1.0.md`, `_v1-build/`, `_v1-parts/`, the `v0.x-*`/`v1.0-*` notes and checks, and `formal/README-v1.1.md`. That is 50 files.
- **Evidence:** `README-v1.1.md` names `WHITEPAPER-v1.1.md` and `宣言-v1.1.md` as the current edition.
- **Action:** retire to `…/history/` (`RC.tsv`). Optionally, rename `README-v1.1.md` → `README.md` (a move with link rewrite) so the project has an index. `v1.1-修订前校验.json` and `_v11-build` stay, since they belong to v1.1.

---

## Tier 3: needs Ren

### 11. Superseded 9-October chapters (roles now held by the canonical chapter)

- **Files:** `chapters/THEORY-OF-BECOMING.md` (§11: "Read at its date … not a current statement"), `chapters/BECOMING-FOUNDATION.md` ("the foundational scope of 9 October"), `chapters/THE-THEORY-OF-EVOLUTION.md` ("Read at its date"), `chapters/G0-WARRANT.md` ("its framing is historical"), each with its `.zh.md`.
- **Overlap:** by role, not by text (text containment with the canonical chapter is below 1%). BECOMING-FOUNDATION §5's "required content / current evidence / remaining inference" table is the older form of canonical §8.1–8.2. THEORY-OF-BECOMING's argument is restated in canonical §1–2, and G0-WARRANT's in §6.
- **Why Ren:**
  - `_process/goals/theory-of-becoming.json` names BECOMING-FOUNDATION and THE-THEORY-OF-EVOLUTION, `theory-of-evolution.json` names THE-THEORY-OF-EVOLUTION, and `generative-relation-change-session.json` names THEORY-OF-BECOMING. A move rewrites goal JSON paths, and AGENTS says a goal record changes only with its authorization.
  - BECOMING-FOUNDATION is the statement source of the open target `theory-of-becoming-foundation`, whose wording "Ren keeps" (canonical §8.1). Its anchors `#whole-and-manifold` and `#5-completion-audit-and-next-central-inference` are cited. A move keeps them; a merge would need record rebinding, so **do not merge**.
  - Records citing these chapters (re-keyed by the tool): THEORY-OF-BECOMING 5, BECOMING-FOUNDATION 3, G0-WARRANT 2.
- **Action, if Ren agrees:** retire via `RF.tsv` and update canonical §11 rows to "in history".
- **Without Ren:** leave in place. §11 already labels them.
- G0-WARRANT has no goal pin, so it can move on the integrator's call. §11 says it "is kept for its analysis of what each kind of support contributes", so its own author chose to keep it; I would ask rather than override.

### 12. Opening drafts (Ren's text)

- **Files:** in `drafts/2026-10-10-opening/`: `OPENING-DRAFT.md` and `OPENING-V2…V6.md`, plus `OPENING-V6-PROPOSAL.md`.
- **Evidence:** `OPENING-V6.md` is byte-identical to `theories/becoming/OPENING.md` (blob fbfc0578).
- **Action:** retire to `drafts/2026-10-10-opening/history/` (`RH.tsv`). Keep `OPENING-NOTES.md` and `OPENING-REVIEW.md`, which are live notes for the next revision. No text changes, but it is Ren's opening lineage, so ask first.

### 13. September theory-folder READMEs with stacked October status paragraphs

- **Files:** 13 of the 16 folders (e.g. `theories/meta-attractor/README.md` has 29 bold-dated paragraphs at the top; the-fork has 58).
- RESTRUCTURE-PLAN §4.1 says these folders get "a generated status header". The October paragraphs are AI-written status that is now in the records and the canonical chapter. The syntheses below them (September, Ren's corpus readings) stay.
- **Action:** replace each top stack with a generated status header from `navigation.py`, and move the removed paragraphs verbatim to `theories/<folder>/history/README-status-2026-10.md`.
- This is large (13 files, in-place edits under language split) and the plan marks it as a header Ren sees on every branch, so propose it to Ren first.
- The README↔`synthesis-*.md` containment (0.25–0.45 of each synthesis in its README) is by design: the README is the synthesis' reading. No action.

### 14. LOST-ARTIFACTS.md

Open decision 1 in `moves/plans/README.md`. It is an action list only Ren can close. Keep it, and link it from `_process/README` or MAP. No move.

---

## Tier 4: optional, the integrator's call

### 15. Results-folder reading views (generated; tool changes)

- **Files:**
  - `results/README.md`, `THEORY-MAP.md`, `ARGUMENTS-A-L.md` and `ARGUMENTS-M-Z.md` are written by `reading_catalogue.py` from data frozen on 2026-10-08 (680 KB bilingual; 104 of the 139 catalogued chapters are now in history).
  - `SESSION-RESULTS.md` is written by `session_map.py`, dated 10-08.
  - `RESULT-REGISTER.md`: see item 1.
- **Overlap:** `results/README.md`'s "reading routes" table repeats BRIEF's "Discovery and evidence" links. The chapter-status list exists three times: canonical §11 (current), `results/README` + ARGUMENTS (10-08), and `moves/plans/H4-keep.txt`.
- **Action:**
  - Make canonical §11 the single chapter-status list (it is already the current one).
  - Have `reading_catalogue.index()` emit a short results-folder index that labels the ARGUMENTS and THEORY-MAP volumes "dated reading catalogue, 2026-10-08", with no reading-routes table.
  - Retire SESSION-RESULTS (+ `data/session-results.json` + the `SESSION-*.json` inputs in root-foundation) only if `session_map` is dropped from render/check. Otherwise keep it, labelled as dated.
- **Do not hand-edit:** all of these are generated.

### 16. Lift remaining pins, then retire the pinned historical chapters and study remnants

- `experiments/shared-renewal-capability/discovery/exact_check.py:104-112` hard-codes FORMAL-SPECIFICATION, FORMAL-CORE and five study leftovers (`2026-10-04-integrated-evolution/*` ×2, `causal-foundations/outputs/formal-results.md`, `generative-health/discovery/DISCOVERY-MATH.md`, `revisable-concern/.../FEATURE-CONSTRUCTION.md`).
- `foundation-assessment/FRONTIER-CHECK.py:69,120` hard-codes `chapters/ALIGNMENT-COMPLETION.md`. FRONTIER-CHECK's sha is bound in `FRONTIER-INTEGRATION.json`.
- Retargeting is a one-line edit each. But `exact_check.py` writes `exact-check.json` in place with `input_sha256` and `script_sha256`, so re-running it would overwrite a receipt. That is not allowed ("receipts never overwritten").
- **Recommendation:** leave them pinned. §11 already labels the chapters "Historical, pinned".
- The 21 other `support-and-shared-generativity/completion/*` pins (12 checkers) are the same case.

### 17. No action (checked)

- Experiments' `development/*-before-*` protocol copies, `frozen/`, `review-history/` and `runs/*/snapshots/` duplicates are preregistration/freeze evidence (44 freeze manifests in shared-renewal-capability). Leave them.
- `theories/evolving-community-swarms/context/2026-09-07-updated-vision.md` contains all of `next-vision/*` (containment 1.0 of each). It is a provenance record "as delivered", with an identical copy in sources. Keep it.
- `THE-THEORY-OF-BECOMING-REFERENCE.md` vs the canonical chapter (0.105/0.055 shared) is by design: the declaration lists were moved out of the chapter. `BECOMING-RENEWAL-READING.md` (study log, 158 records) sharing about 9% with the canonical chapter is expected.
- Concern-theory internal pages (START-HERE/THEORY/CLAIMS/RESEARCH-RECORD) are inside a freeze-pinned study. Leave them.
- `_process/architecture/README.md` is the dated 8 Oct repair record. Keep it, and possibly add one pointer line to REPOSITORY-LAYOUT.
- `RESULT-WORKFLOW` "Shared validation and discovery" repeats 5 command lines of `tools/research/README.md`. This is optional: keep the four `make` targets in the workflow and link the tool README for the rest.
- worldbuilding `assets-v2…v5`, `reviews/2026-09-07-v4|v5`, `embodied-copy-v4` and `reader-v5` look like edition stacks. They are outside scope ("clear duplicates" not established without image comparison); left for the worldbuilding owner.

---

## Items needing Ren (collected)

1. Item 11: retiring THEORY-OF-BECOMING, BECOMING-FOUNDATION and THE-THEORY-OF-EVOLUTION (goal records name them; the theory-of-becoming-foundation target wording is Ren's). G0-WARRANT is optional.
2. Item 12: the opening drafts (Ren's text lineage).
3. Item 13: the generated status header that replaces the October stacks in the September folder READMEs.
4. Item 14: LOST-ARTIFACTS.
5. Item 7: AGENTS.md "Start here" stays as is. Any change is Ren's.
6. Observation for the integrator (not part of this plan): the in-flight work edits all 15 `_process/goals/*.json` (adds `"state"`). Goal scopes are Ren's; the change appears to be metadata only, but it should be confirmed as covered by the approved plan ("GOALS.md is ordered by state").

## Records whose cited files change

- **Re-keyed by moves (no rebinding):**
  - item 5: WUMING 2, REGISTRATION 2, CONTINUATION-GROUNDING 5;
  - item 9: 1–8 per review, 79 record citations in all;
  - item 11, if approved: 10;
  - item 4: 0;
  - items 2, 3, 8 and 10: 0.
- **Merges:** none proposed, so no record rebinding.
- **Regenerate after moves:** `source-index.json`, `generativity-chain.json` (the chain is Ren's; follow its maintenance record and do not refresh historical evidence), `lean-index.json`, the ARGUMENTS volumes and SESSION-RESULTS, via `make research-render` and the catalogue builders, as after H4/H5.

## Effort estimate

- Tier 1: about 75 min. Items 2–5 are four move batches using prepared TSVs; item 6 is five small edits; item 1 is a check of in-flight work.
- Tier 2: about 60 min. Item 8 is 8 short index READMEs; items 9–10 are two move batches; item 7 is two page edits.
- Total about 2.5 h for one agent. Tier 3 waits for Ren; Tier 4 is optional.

## Re-validation snippet (run before each batch)

```sh
python3 -B - <<'EOF'
import subprocess,os,sys
R='/Users/ren/theories'
ls=set(subprocess.run(['git','-C',R,'ls-files','-z'],capture_output=True,text=True).stdout.split('\0'))
for l in open(sys.argv[1] if len(sys.argv)>1 else 'plan.tsv'):
    o,new,_=l.rstrip('\n').split('\t')
    n=sum(x.startswith(o) for x in ls) if o.endswith('/') else int(o in ls)
    if not n or os.path.exists(os.path.join(R,new.rstrip('/'))): print('PROBLEM',o,n)
EOF
```
Also add any `NAME.zh.md` sibling that has appeared since this survey (`ls <dir>/*.zh.md`).

---

## Appendix: move rows (`old<TAB>new<TAB>reason`)

The same rows are in `scratchpad/recon/RA.tsv` … `RH.tsv`. `RG` rows are a **replace** batch (`--keep-references`). All others are plain moves.


### RA

```
experiments/agentdojo-evidence-boundary/correction-action/continuation/integration/	experiments/agentdojo-evidence-boundary/correction-action/continuation/history/integration/	applied 6-Oct integration kit: edit ledgers (BEFORE/CHECKS/README-EDIT/REBASED-EDITS/RESULT.json) and before/ + rebased-* byte copies of the pages it edited (01/rebased-01 Jaccard 1.0; 04 = 0.99 of chapters/ALIGNMENT-COMPLETION.md); 0 records, 0 live referrers
theories/the-fork-and-cooperative-infrastructure/revisions/	theories/the-fork-and-cooperative-infrastructure/history/	byte copy of the 2026-09-07 README before the productive-foundation revision (0.91 of it is in the live README); same depth, so its relative links still resolve
```

### RB

```
drafts/2026-10-02-iaseai-selecting-the-selectors/v3/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v3/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v4/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v4/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v5/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v5/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v5-codex/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v5-codex/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v6/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v6/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v6-planning/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v6-planning/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v6.1/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v6.1/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v6.2/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v7/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v7/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v7.1/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v7.1/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/v7.2/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v7.2/	superseded paper edition; v7.3 (2026-10-05) is the latest and links to it; many files byte-identical across v7-v7.3
drafts/2026-10-02-iaseai-selecting-the-selectors/versions/v1/	drafts/2026-10-02-iaseai-selecting-the-selectors/history/v1/	v1 notes, sources and PDF, already a version copy
drafts/2026-10-02-iaseai-selecting-the-selectors/V3-PLAN.md	drafts/2026-10-02-iaseai-selecting-the-selectors/history/V3-PLAN.md	executed edition plan
drafts/2026-10-02-iaseai-selecting-the-selectors/V5-PLAN.md	drafts/2026-10-02-iaseai-selecting-the-selectors/history/V5-PLAN.md	executed edition plan
drafts/2026-10-02-iaseai-selecting-the-selectors/V6-PLAN.md	drafts/2026-10-02-iaseai-selecting-the-selectors/history/V6-PLAN.md	executed edition plan
drafts/2026-10-02-iaseai-selecting-the-selectors/V6.1-PLAN.md	drafts/2026-10-02-iaseai-selecting-the-selectors/history/V6.1-PLAN.md	executed edition plan
```

### RC

```
drafts/2026-09-05-generative-foundations/WHITEPAPER.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v0.2.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v0.2.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v0.3.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v0.3.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v0.4.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v0.4.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v0.5.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v0.5.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v0.6.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v0.6.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/WHITEPAPER-v1.0.md	drafts/2026-09-05-generative-foundations/history/WHITEPAPER-v1.0.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/README-v1.0.md	drafts/2026-09-05-generative-foundations/history/README-v1.0.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/宣言-v1.0.md	drafts/2026-09-05-generative-foundations/history/宣言-v1.0.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/_v1-build/	drafts/2026-09-05-generative-foundations/history/_v1-build/	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/_v1-parts/	drafts/2026-09-05-generative-foundations/history/_v1-parts/	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.2-修订说明.md	drafts/2026-09-05-generative-foundations/history/v0.2-修订说明.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.3-整合与来源.md	drafts/2026-09-05-generative-foundations/history/v0.3-整合与来源.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.4-原版校验.json	drafts/2026-09-05-generative-foundations/history/v0.4-原版校验.json	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.4-整合与证明说明.md	drafts/2026-09-05-generative-foundations/history/v0.4-整合与证明说明.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.4-检查记录.txt	drafts/2026-09-05-generative-foundations/history/v0.4-检查记录.txt	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.5-原版校验.json	drafts/2026-09-05-generative-foundations/history/v0.5-原版校验.json	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.5-整合说明.md	drafts/2026-09-05-generative-foundations/history/v0.5-整合说明.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.5-检查记录.txt	drafts/2026-09-05-generative-foundations/history/v0.5-检查记录.txt	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.6-原版校验.json	drafts/2026-09-05-generative-foundations/history/v0.6-原版校验.json	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.6-整合说明.md	drafts/2026-09-05-generative-foundations/history/v0.6-整合说明.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.6-完整性与形式化审计.md	drafts/2026-09-05-generative-foundations/history/v0.6-完整性与形式化审计.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v0.6-检查记录.txt	drafts/2026-09-05-generative-foundations/history/v0.6-检查记录.txt	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v1.0-检查记录.json	drafts/2026-09-05-generative-foundations/history/v1.0-检查记录.json	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v1.0-原版校验.json	drafts/2026-09-05-generative-foundations/history/v1.0-原版校验.json	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v1.0-审读意见.md	drafts/2026-09-05-generative-foundations/history/v1.0-审读意见.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v1.0-整合说明.md	drafts/2026-09-05-generative-foundations/history/v1.0-整合说明.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/v1.0-检查记录.txt	drafts/2026-09-05-generative-foundations/history/v1.0-检查记录.txt	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
drafts/2026-09-05-generative-foundations/formal/README-v1.1.md	drafts/2026-09-05-generative-foundations/history/formal/README-v1.1.md	superseded whitepaper edition or its notes; README-v1.1 names WHITEPAPER-v1.1 as the current edition (WHITEPAPER.md is v0.1)
```

### RD

```
_process/research/2026-10-05-generative-foundation-review/root-foundation/REGISTRATION-AND-TESTING-PLAN.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/REGISTRATION-AND-TESTING-PLAN.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/WUMING-BOUNDARY-PLAN.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/WUMING-BOUNDARY-PLAN.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTINUATION-GROUNDING-PLAN.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CONTINUATION-GROUNDING-PLAN.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTINUATION-GROUNDING-PLAN.zh.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CONTINUATION-GROUNDING-PLAN.zh.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/PART-II-INVENTORY.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/PART-II-INVENTORY.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/PART-II-INVENTORY.zh.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/PART-II-INVENTORY.zh.md	executed plan
_process/research/2026-10-05-generative-foundation-review/root-foundation/PART-II-INVENTORY.py	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/PART-II-INVENTORY.py	executed plan
```

### RE

```
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P7-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P7-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P11B-P12-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P11B-P12-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P13-P14-P12B-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P13-P14-P12B-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P15-P16-P16B-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P15-P16-P16B-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P16C-P17-P18-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P16C-P17-P18-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P18B-P23-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P18B-P23-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P23C-P24-P25-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P23C-P24-P25-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P25B-P29-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P25B-P29-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P30-P31-P29B-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P30-P31-P29B-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P32-P34-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P32-P34-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P34B-P38C-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P34B-P38C-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P42-P43-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P42-P43-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P42-P43-REVIEW.zh.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P42-P43-REVIEW.zh.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P49-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P49-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P49-REVIEW.zh.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-P49-REVIEW.zh.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-R1-R2-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-R1-R2-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.zh.md	_process/research/2026-10-05-generative-foundation-review/history/root-foundation/BECOMING-RENEWAL-READING-REVIEW.zh.md	spine review of 9-11 Oct landings; evidence for the records that cite it (paths re-keyed, hashes carried); later reviews (GENERAL-LAWS, EIGHTEENTH, RELEASE-READINESS) stay live
```

### RF

```
theories/becoming/chapters/THEORY-OF-BECOMING.md	theories/becoming/history/THEORY-OF-BECOMING.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/THEORY-OF-BECOMING.zh.md	theories/becoming/history/THEORY-OF-BECOMING.zh.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/BECOMING-FOUNDATION.md	theories/becoming/history/BECOMING-FOUNDATION.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/BECOMING-FOUNDATION.zh.md	theories/becoming/history/BECOMING-FOUNDATION.zh.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md	theories/becoming/history/THE-THEORY-OF-EVOLUTION.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/G0-WARRANT.md	theories/becoming/history/G0-WARRANT.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
theories/becoming/chapters/G0-WARRANT.zh.md	theories/becoming/history/G0-WARRANT.zh.md	9-Oct chapter, read at its date (canonical section 11); its role is stated in the canonical chapter
```

### RG

```
_process/research/2026-10-05-generative-foundation-review/foundation-assessment/README.md	_process/research/2026-10-05-generative-foundation-review/history/foundation-assessment/README.md	stack of 8 dated 6-Oct status paragraphs; a short file index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/lean/deeper/README.md	experiments/integrated-correction/general-framework/generative-basis/lean/history/deeper/README.md	dated status log (stacked 8-Oct paragraphs); a module/checker/receipt index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/README.md	experiments/integrated-correction/general-framework/generative-basis/lean/history/inquiry-root/README.md	dated status log (stacked 8-Oct paragraphs); a module/checker/receipt index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/README.md	experiments/integrated-correction/general-framework/generative-basis/lean/history/universal-ethics/README.md	dated status log (stacked 8-Oct paragraphs); a module/checker/receipt index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/README.md	experiments/integrated-correction/general-framework/generative-basis/lean/history/universal-ethics/generative-capacity/README.md	dated status log (stacked 8-Oct paragraphs); a module/checker/receipt index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/README.md	experiments/integrated-correction/general-framework/generative-basis/history/mathematical-abstraction/README.md	dated status log; a short index is written at the old path
experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/README.md	experiments/integrated-correction/general-framework/generative-basis/history/mathematical-abstraction/constitution/README.md	dated status log; a short index is written at the old path
_process/research/README.md	_process/history/research-README-2026-10-08.md	stale study-directory page (says studies are not moved; points to RESEARCH.md as the research index); a short index of the remaining live studies is written at the old path
```

### RH

```
drafts/2026-10-10-opening/OPENING-DRAFT.md	drafts/2026-10-10-opening/history/OPENING-DRAFT.md	first opening draft (10-10), superseded by V2-V6 and OPENING.md
drafts/2026-10-10-opening/OPENING-V2.md	drafts/2026-10-10-opening/history/OPENING-V2.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
drafts/2026-10-10-opening/OPENING-V3.md	drafts/2026-10-10-opening/history/OPENING-V3.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
drafts/2026-10-10-opening/OPENING-V4.md	drafts/2026-10-10-opening/history/OPENING-V4.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
drafts/2026-10-10-opening/OPENING-V5.md	drafts/2026-10-10-opening/history/OPENING-V5.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
drafts/2026-10-10-opening/OPENING-V6.md	drafts/2026-10-10-opening/history/OPENING-V6.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
drafts/2026-10-10-opening/OPENING-V6-PROPOSAL.md	drafts/2026-10-10-opening/history/OPENING-V6-PROPOSAL.md	superseded opening draft (OPENING-V6.md is byte-identical to theories/becoming/OPENING.md)
```
