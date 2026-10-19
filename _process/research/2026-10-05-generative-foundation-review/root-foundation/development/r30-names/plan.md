# R30 "one notion, one name": the rename table and how to apply it (draft)

**Applied 20 October 2026 (study §221).** This is the draft as written before R28 and R29 landed. The applied table, regenerated on R29's head and decided by `decide.py`, is [RENAME-TABLE.json](RENAME-TABLE.json); where it and this draft differ (dropped borderline groups, `Enough.*` kept, the `Unfolding` ports left for R34, `Web.Regenerating` → `ActiveRenewer`), the table and §221 hold.

Read-only draft, 20 October 2026, on main `c12eb6779` (before R28 and R29 land). Nothing in the repository was changed. Sources: twentieth review §4, lens B (B2, B3, B6, B13; B13's third `Coarse` withdrawn), F (F1, F3, F8, F9, F12, F14, §2f), A10, G9. Precedents: N5 (`development/n1-migration/`: `apply_renames.py`, `rebind_records.py`, 175 declarations, no aliases, one checker run), R22 (`development/r22-names/`: `rename.py table|text`, `rebind.py`, module renames with a `paths` map).

## Files

- `rename-draft.json`: 424 rows. Fields: `old_full_name`, `new_full_name`, `kind`, `module`, `line`, `reason` (finding id first), `definition` (comment-stripped body, ≤200 chars), `occurrences_in_core` (word-bounded `bare_token` and `qualified` counts with file counts, and whether the last component is unique among the core's 16,021 declarations), `cited_in` (chapter en/zh, OPENING, DC en+zh, records JSON, other live `theories/` pages and the Lean README, with the pattern used), `new_name_exists`, `new_last_component_elsewhere`, `confidence`, `justified`, `edit_mode`, `note`.
- `spec.py` holds the choices, `gen.py` regenerates the table (about 7 minutes; reads only), and `parse.py` is lens B's declaration parser, copied. Rerun on R29's head before applying: rows whose old name has gone (`Image`, `Law.*` twins, perhaps `LearnableRuns.*`) drop out.

## What the table proposes

| kind | rows | high | medium |
|---|---|---|---|
| declaration renames | 345 (186 are members moved with a namespace) | 172 | 173 |
| namespace renames | 12 | 11 | 1 |
| module renames | 4: Generation→Arising, Coupling→MoveFormation (high); Return→Restoration, PositiveGround→SecuredContent (medium) | 2 | 2 |
| binder | 1: `positive`→`relevance`, only where it is the relevance parameter (about 53 tokens in 8 modules) | | 1 |
| docstring | 1: Metaethics header "Universal Metaethical Core" | 1 | |
| delete | 1: `Image` → `Readout.image` (R29's item; listed so that R30 does not rename it) | 1 | |
| port | 28 `Unfolding` sites (Ranking 19, Relevance 5, ActiveReading 4) → `Web`, through `Web.static` | | 28 |
| keep (judged **not** justified by AGENTS' bar) | 32 | | |

The groups:
- **Returns, the other senses.** `Web.Returns`/`ReturnsWithin` → `Web.Restored`/`RestoredWithin` (F §2f #16: a dependence met again is "restored"). The root `Returns` of Frequency → `RoundTrip` (F §2f: loop "return" → round trip; at root it also shadows `Branching.Returns` wherever Branching is open). Their families follow. `Law.Returns`/`Lossless`/`Merges` are left to R28.
- **Lossless, the amount sense.** `Flow.Lossless`/`LosslessOn` → `Flow.Conserving`/`ConservingOn`, with 12 family members. `Merges` has only the Law/Branching pair, so it needs no row; Entropy:87/98 cite `Web.Merges` and `Web.merges_of_settles`, which do not exist, so fix those docstrings.
- **Settles/Rests.** `HistoryIdeals.Settles` → `HasLongest`, `Stretches.Settles` → `HasLatest`, `Narrowing.Settles` → `Decides` (medium), `Learnable(Runs).RestsFrom/Rests` → `PredictsFrom/Predicts` (`Accords` would collide with N5's `Learning.Accords`), `Enough.RestsFrom/Rests` → `StaysMetFrom/StaysMet` (medium, see the decisions below), and `Ranking.Rest` → `Ranking.Pause`. `World.RestsFrom` (停息) and `Enough.Settles` (D42's "settle") keep their names.
- **Keeps, Closed, Alike.** `Branching.Keeps` → `Essential` (medium). `Ideals.Closed` → `ScottClosed`. `GuardHorizon.Closed` → `ControlledInvariant` (medium). `ReferencePlan.Alike`/`Contacts.Alike` → `AgreeOn`.
- **generation.** 15 `Web.generation_*` → `Web.embodiedArising_*` (each statement is "embodied members arise at arbitrarily late steps"). `dissipation_generation_not_recurring` → `dissipation_arising_not_recurring`. `renewal_without_generation` → `renewal_without_arising`. `Web.Regenerating` and `regeneration_recurs` → `Replenishing` and `replenishment_recurs`. Module `Generation` → `Arising`. `contingent_generation*` and `Handoff.generation_by_bound*` → `newContent` (the SecuresPositiveGround sense). `ExchangeLaw.generation` → `ExchangeLaw.process`. `SharedCodes.generation` → `nextCohort`. `ResponseLearning.*generation*` → `*cohort*`. The witness `Generations` → `OverlappingLives` (optional, because `Lineage` and `Succession` are taken).
- **Ethics names.** `G0` → `LivingSignificance`, plus the 15 `g0_*` → `livingSignificance_*`. `SelfGood` (×2) → `SelfSignificance`, plus 4 family members. `SecuresPositiveGround` → `SecuresNewContent`. Module and namespace `PositiveGround` → `SecuredContent` (63 members; the arithmetic `positive_integral_*` and `positiveDomain` keep "positive"). `Clearing.free_rider_loses` → `Clearing.clearer_loses_dweller`, which says exactly what the theorem proves, unlike F's `nonDependent_loses`.
- **Other names that state a wrong meaning.** Module `Coupling` → `MoveFormation`, with its namespace. `Onward.DependentSelection` → `DependentChoice`. `Joining.Neutral` → `TwoSidedUnit` (medium: "neutral element" is standard algebra, but the word collides with the ethics' ∀-neutrality, and `Unit` alone would shadow Lean's `Unit`).
- **Namespace collisions (B13), qualified by module as in N3.** Order's `Crossing`, `Arising` and `Halving` → `Order.*`. Moving Order's `Arising` also frees `Becoming.Arising` for the renamed module. The others are Gluing's `Cycle`, Weighted's `Loop`, Pace's `Copying`, Entropy's `Settling`, Likeness's `Parting`, Identity's `Fork` and Labelled's `Circulation` (in each pair, the one that is not the module's namesake, or has fewer members). Both halves of Clearing, Shuttle, Lineage and the other `Loop`s are one witness each, so they stay. `RuleCapture.Counts` → `CarrierCounts` and `Countdown.Counts` → `CountedWork` (G9); the root `Counts` stays.
- **History/course (A10).** `Activation.History` → `TwoSteps`, `Registration.History` → `AlikeUpTo`, `Flow.history` (a number) → `exchangeCount`. Eleven `history`/`course` definitions are step-indexed sequences, which F §2f #13 calls course or history, so they stay.
- **Adjacent.** `SharedCodes.Image` → `Relabels` (it is a relation, not an image).

## Rows judged not justified (kept, `justified: false`)

- `Dependence.Keeps`, `Joining.Keeps`, `Footprinted.Keeps`, `Registration.Keeps`: exact English, local to their namespaces, and no Lean collision.
- `OneStep.Closed`, `SharedCodes.Closed`, `Undecided.Closed`.
- The three `Continues`: two are the continuation sense, and the third is continuity, which its docstring says.
- The three `Balanced`: they are one notion, the balance equation at three levels. Joining them is R33's work, not a rename.
- `HistoryIdeals.History`, which is the base notion.
- Eleven `course`/`history` definitions.
- `World.RestsFrom`, `Enough.Settles`, root `Counts`, `Law.Merges`.
- `Web.static` and its 6 lemmas, which are the bridge itself.

Borderline renames the board may decline. Each is marked medium with an alternative in `note`:
- `Narrowing.Settles` ("settles a question" is idiomatic);
- `GuardHorizon.Closed`;
- `Generations`;
- Slowing's `phase_*_return` names, which name an event of the witness;
- `Branching.Keeps`.

## Decisions to take with the landing

1. **静 and 停息 (F14).** `Enough.RestsFrom` → `StaysMetFrom` contradicts D42 ("come to rest = settle with the target met") and D45(4) ("seeking and extrapolation that come to rest take 停息"). Renaming needs a D42/D45(4) revision in the same landing:
   - 停息 means `World.RestsFrom` only;
   - 静 is a state the run leaves unchanged;
   - an extrapolation "predicts from T".

   If the revision is not taken, set the two Enough rows to `justified: false`. `Learnable.RestsFrom` → `PredictsFrom` is justified either way, because nothing in that definition rests.
2. `positive` → `relevance` is F9's proposal. Check every `open Frame` site, because `Frame.relevance` exists (it is reached by dot notation, so a binder does not shadow it).
3. The 28 `Unfolding` port sites are in Ranking, Relevance and ActiveReading, which R34 restates (`Pos := F`). Either R30 ports them (proof work: `Renewed`, `Dependent` and `ConsumingIn` of RelationalRenewal go to their `Web.static_*` forms, and the witnesses become `Web` literals), or R30 hands them to R34 and records that. Board rule 8: `deeper/RelationalRenewal.lean` keeps its bytes.

## How to apply

Do this in a worktree off main **after R28 and R29 have landed**, with a kit in `development/r30-names/` (copy `spec.py`, `gen.py` and `parse.py`; adapt R22's `rename.py`/`rebind.py` and N5's `apply_renames.py`). Regenerate the table on that head first.

1. **Modules** (4).
   - `git mv` Generation→Arising, Return→Restoration, Coupling→MoveFormation, PositiveGround→SecuredContent.
   - Fix the `import` lines in importers and in the root `Becoming.lean` (lines 34 and 293, and its module prose at 479, 565 and 1517).
   - Fix `check_becoming.py`: the module list at lines 73–86, the mapping at 161–162, the description at 490 and the Lean snippet at 2640 (which uses `SecuresPositiveGround`). The script and its receipts embed names, so its own text is part of the change.
   - Write a `modules` and a `paths` map, as R22 did.
2. **Namespaces** (12, plus `PositiveGround`, `Coupling`, `RuleCapture.Counts` and `Generations`).
   - Edit only the `namespace X` and `end X` lines in the defining module. Order has two `Crossing` blocks (1795 and 2779) and `Arising` at 1896/2811; `RuleCapture.Counts` has blocks at 389 and 603.
   - Uses inside a block do not change. The 186 member rows have `edit_mode: namespace line`.
   - Outside references are the qualified ones (`X.member`, and `open X`). Rewrite them only in files whose import closure contains the defining module, and pick the witness by its member set where both witnesses are visible: for example, Order's `Crossing.web` against Dependence's `Crossing.dependence`.
3. **Global names** (92 rows, `edit_mode: global`). These are unique compound names. Make one alternation sorted **longest first**, with Lean identifier boundaries `(?<![\w'.])(…)(?![\w'])`. `'`, `₀` and `?`/`!` suffixes count as identifier characters, so exclude them in both lookarounds. Apply the same alternation once more to the qualified forms (`Web.generation_opens`, `Becoming.…`). It runs on code and inside backticks in comments, not on prose words (the N5 rule).
4. **Scoped names** (67 rows, `edit_mode: scoped`). Their last component is shared (`Returns` ×4, `RestsFrom` ×4, `Settles` ×5, `Keeps` ×6, `Closed` ×5, `Alike` ×3, `Lossless` ×3, `Counts` ×3, `generation` ×2, `History` ×3) or is a plain word.
   - Rename the definition line and its qualified forms (`Web.Returns`, `Stretches.Settles`), and dot forms (`W.Returns`) only in the files listed by `occurrences_in_core.qualified`. Then build: every stale use of a removed constant fails to elaborate, and the compiler lists the rest.
   - The one silent risk is a bare name inside a namespace where another declaration of that name is visible, for example `Returns` in `namespace Web` once root `RoundTrip` and `Branching.Returns` are open. Step 7's statement fingerprint catches it.
5. **Binder** `positive` → `relevance`, only in the declarations that bind it at type `… → … → Prop` beside `G0`, `SecuresPositiveGround`, `articulates` or `PositionedArticulation`, and in their users. Arithmetic `positive` (`0 < k`) stays; Return.lean alone has 20 of those.
6. **Docstrings by reading, not substitution.**
   - Generation's header and `Web.Unceasing`'s "Generation does not cease".
   - Metaethics' header and its "S0 at a position" and "N_rel's rule" lines.
   - PositiveGround's header.
   - The "free rider" sentences (Significance:90, RelativePosition:49/621).
   - Entropy's stale `Web.Merges` reference.
   - `Arising.order_registers`/`Crossing.order_registers` still carry N1's retired word: optional.
7. **One checker run** (`check_becoming.py`, with a longer `LEAN_TIMEOUT` and reuse of passed steps).
   - Acceptance: empty axiom reports, the core imports only `Init`, and theorem and definition counts are unchanged (less `Image` if R29 has not deleted it).
   - **Statement preservation:** export every declaration's type before and after (the parser's `stmt`, or the checker's declaration export), apply the table and compare. They must be identical up to the renamed identifiers.
   - Rerun FallibleInquiry's checker if any name it imports changed, then the connectivity measure: renamed declarations keep their class.
8. **Text.** Run `rename.py text` over live text, with R22's exclusions (history, sources, receipts, reviews, `development/`, the workboard, generated pages). By the table, that covers:
   - the chapter (en: 75 hits; zh: 84);
   - the DC en/zh (20);
   - the Lean README en/zh (43);
   - OPENING's **AI-written** footnotes `[^good-evil]`, `[^aligned]` and `[^collective]` (4 hits, all `Clearing.free_rider_loses`; Ren's body is untouched);
   - 8 other `theories/` pages (84);
   - `MODULE-CLASSIFICATION.md/.zh.md` and `DECIDABILITY-INVENTORY.py`.

   Add the retired Lean names to the glossary's retired-names table (en and zh), as N5 did.
9. **Records.** 167 record JSONs name a renamed declaration or module, with 1,343 hits. About 467 of those hits, in about 140 files, are the module `Becoming.Coupling` in dependency lists.
   - Rebind with R22's `rebind.py` pattern: live fields renamed, references to changed files re-hashed, proof bindings rebound to the receipt, and a history note added.
   - Record IDs and slugs stay as stable IDs (F17).
   - Then `make research-render`, `research-check`, `research-links` and `research-test`.

## Estimated size

- **Lean core.**
  - About 395 counted token edits: global names plus qualified forms.
  - About 300–600 dot and bare edits found by the compiler on scoped names (inferred).
  - About 53 binder tokens and about 40 `namespace`/`end`/`import` lines.
  - About 71 files touched, plus the 4 renamed modules.
- **Text and checker.** About 300 hits in the chapter, DC, README and pages, and 7 in `check_becoming.py`.
- **Records.** 167 rebound.
- **Comparison.** N5 renamed 175 declarations in one checker run. This table holds 345 declaration rows, but 186 of them move with a namespace line, so the hand-checked set is about 160 (B's estimate), the same order as N5.

## Risks

- **Parallel landings.** R28 changes `Law.*` and makes `Web` an abbreviation; R29 deletes `Image`, the `Law` twins and possibly `LearnableRuns`. Regenerate the table on R29's head. A row whose old name has gone is dropped, not renamed.
- **New-name checks.** All 345 new declaration names are absent from the core. The only existing new name is `Becoming.Arising`, which is a namespace (Order's witness) and is moved in the same sweep. No two rows map to the same new name. Rerun the check after regeneration.
- **Collisions this sweep could create.** None found, but note:
  - `Becoming.Order.*` becomes a namespace. Lean core has no `Order` namespace, but check Mathlib-free `Init`.
  - `ExchangeLaw.process` sits beside `Law.process` by design.
  - `Restored` reads beside `Crossing.restoring` (another witness).
- **Counting limits.** Counts come from a regex over source, not from the elaborated environment.
  - For non-unique last components, `bare_token` includes the other senses and is an upper bound.
  - `cited_in` with pattern "backticked" (root `Returns`, `G0`) counts every backticked use of the word.
  - Treat both as review lists, not edit counts.
- **Prose.** The words "generation", "rest", "return", "free rider" and "positive ground" in the chapter and the records change by reading (R36 and F10). This table renames identifiers only.
- **Reasons with no AGENTS bar.** Medium rows whose reason is "one word per notion" without a wrong meaning or a Lean collision are the Slowing event names, `Narrowing.Settles` and `Generations`. Drop them if the board reads AGENTS' bar strictly.
