# R35 other items: E5, E13, G12, G11/G13, E12 (read-only preparation, 20 October 2026)

Lean README lines and worktrees were measured on 87ecfdee5; everything else on 4c40745f8. Data: `data/e13-banners.tsv`, `data/worktrees.json`, `data/worktrees.tsv`.

## E5 — "registration" in the Lean README

File: `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md`. On 87ecfdee5, after R28, it has **20 lines** with "registr". (On 4c40745f8 there were 27; R28 already rewrote some.) The replacements follow the adopted vocabulary (study §7: couples into / coupling / the map / lumping, 识 only for the derived structure; "refutes" → "excludes"; "learner" → "extrapolation"; "record" → "prefix"). These are the same words the record titles took in N5 and N6.

| line | module | current phrase(s) | proposed |
|---|---|---|---|
| 33 | Diagonal | "a registration within what it registers" | "a family of readings within what it reads" |
| 34 | Context | "contextual registration … where the registrations glue" | "claims shown in context … where what the contexts show glues" |
| 95 | Stock | "jointly with a registration exactly where the registration admits it" | "jointly with a map exactly where the map admits it" |
| 155 | Testing | "what registers in a formation …; registration refutes the model; a judgment from registration …; respond only through their own registration" | "what couples into a formation …; what couples in excludes the model; a judgment from what couples in …; respond only through their own couplings" |
| 156 | Runaway | "what a loop through its own registration cannot register; a policy through registration …; exchange following registration" | "what a loop through its own couplings cannot couple in; a policy through the couplings …; exchange following the couplings" |
| 157 | Response | "responding through registration; the dual of the registration closure" | "responding through the couplings; the dual of the coupling closure" |
| 158 | Counterfactual | "the least registration" | "the least coupling" |
| 159 | Selection | "selection through registration (×2); registers them alike; pooled registration (×2); beyond the registration closure (×2)" | "selection through the couplings; couples them alike; pooled couplings; beyond the coupling closure" |
| 167 | Learning | "the registration of a law keeping its record" | "the map of a law keeping its prefix"; also "refuted" → "excluded" |
| 184 | Contacts | "registration through addressed contacts" | "coupling through addressed contacts" |
| 187 | Learnable | "what a learner can learn through its registration; the same registered future; read off the registration; alike across the registration" | "what an extrapolation can learn through a map; the same future through the map; read off the map; alike through the map" (record title: "What an extrapolation can learn through a map") |
| 188 | Distinguishing | "frames whose moves carry the registration" | "frames whose moves carry the map" |
| 209 | Readings | "the registrations in context of a run; quantum registrations" | "what a run shows in context; quantum readings" |
| 216 | Sensitivity | "the least registration (×3); the registrations it reads through" | "the least coupling; the couplings it reads through" |
| 217 | Tail | "has no least registration; a counterexample to the least registration" | "has no least coupling; a counterexample to the least coupling" |
| 218 | Courses | "registrations at listed dates" | "readings at listed dates" |
| 230 | Thresholds | "a law reading through a registration; policies through registration" | "a law reading through a map; policies through the couplings" |
| 245 | LearnableRuns | "a learner reading a run's registration" | "an extrapolation reading a run through a map" |
| 270 | DiagonalRuns | "completing a registration within what it registers" | "completing a family of readings within what it reads, as a process" |
| 287 | RevisionRuns | "the history of a run's registrations" | "the history of a run's lumpings" |

Leave alone: physics uses of "two registers" (if still present) and "registered as superseded" (bookkeeping; "listed as superseded" is optional). Lean identifiers in backticks are R30's job, and none of the phrases above is an identifier.

**README.zh.md** has 22 lines with 识, at lines 30–130. In 30, 31, 96–102, 106, 107 ("经登记读出" in 107 is the old word), 111, 113, 116 and 130 it stands for the primitive relation. Replace it there by 耦合入 / 耦合 / 映射 / 归并, following the English rows above. One example: "经识的选择" → "经耦合的选择", "识闭包" → "耦合闭包". Keep 识 only where the row states the derived structure, as in Learning and Readings, where it is the lumping a history induces. The terms come from study §7(b).

**Dependency.** R31 may make the module table generated from module docstrings. If R31 lands first, apply these edits to the docstring source, the `/-! … -/` head of each module. That is a docs-only change in the core, so the receipt rehashes and there is no proof change. If R31 does not, apply them to both READMEs directly.

## E13 — dated round banners at chapter heads

Per chapter: the dated banners before the first `##`, and their bytes (`data/e13-banners.tsv`).

| chapter | banners | dates | bytes | `-rounds` history file |
|---|---|---|---|---|
| THE-THEORY-OF-EVOLUTION | 15 | 5–9 Oct | 9,890 | new |
| WISDOM-AND-CONTEXT (zh 3) | 10 | 5–13 Oct | 6,304 | new |
| ALIGNMENT-COMPLETION | 4 | 5–6 Oct | 3,056 | moves whole (B1) |
| MATHEMATICAL-ROOT-FRONTIER | 4 | 5–7 Oct | 2,868 | moves whole (B1) |
| CHOICE-AND-GENERATIVE-CONTEXT (zh 3) | 4 | 8 Oct | 2,044 | new |
| BASIC-CONFLICT-JUDGMENT (zh 2) | 3 | 8 Oct | 2,076 | new |
| ZERO-AXIOM-PRACTICAL-JUDGMENT (zh 2) | 2 | 13–17 Oct | 1,636 | exists (`-rounds-2026-10-17`) |
| BECOMING-FOUNDATION (+zh) | 1 | 19 Oct | 1,456 | keep: a current status line |
| ETHICAL-LEARNING (+zh), PRACTICAL-JUDGMENT (+zh), MARKETS, MATHEMATICAL-CORE, SCIENTIFIC-PHILOSOPHY | 1 each | 6–13 Oct | 400–800 | new (ETHICAL-LEARNING exists) |
| FORMAL-SPECIFICATION, NONINSTRUMENTAL, PHILOSOPHICAL-ACCOUNT, PLURAL, RELATIONS (+zh) | 1 each | | | move whole (B1) |

**Edit.** For each chapter that stays live:
1. Move the banners verbatim into `theories/becoming/history/<NAME>-rounds-2026-10-20.md`, with provenance lines (source path and commit). Where a `-rounds-2026-10-17` file exists, append a dated section to it instead.
2. Replace the banners with **one** current status line: "Status: <live / live in part / historical in part>; current statement in chapter §n; earlier rounds: history/…".

**Drift.** Every edit above the first `##` drifts every record that cites the file without anchors. The records citing these chapters are: MARKETS 4, BECOMING-FOUNDATION 3, SCIENTIFIC-PHILOSOPHY 3, ETHICAL-LEARNING 2, PRACTICAL-JUDGMENT 2, BASIC-CONFLICT 1, CHOICE 1, WISDOM 1, ZERO-AXIOM 1, KNOWLEDGE 1; about 19 in all. Re-point them in one pass with E3's shared re-point tool, which writes no notes.

**Order.** Do this with batch B1, before the chapter-§11 edit, so all three re-point rounds happen once.

## G12 — splitting agreement by law level

Measured from `y1-changes/passages.json` (90 passages) and `ro-relational-sources/passages.json` (248).

| map | agreement | of which encoding-only / general / both | scope (general / mixed) | divergence (general / mixed) |
|---|---|---|---|---|
| Y1 (Changes) | 52 | 33 / 9 / 10 | 12 / 6 / 8 by level | 4 / 3 / 5 |
| RO (Chinese sources) | 95 | 4 / 84 / 7 | 85 / 9 | 49 / 10 |

Here "general" means the cited declaration is a law over every process or ExchangeLaw (core namespaces such as `Flow.*`, `ExchangeLaw.*`, `Law.*` and `Web.*`). "Encoding-only" means it is a fact about the hexagram encoding (`Becoming.Hexagram*` lemmas about `Fin 64`, tables, `decide`). So 33 of Y1's 52 agreements rest only on the encoding. That is the point of G12.

**Proposal.** Compute `law_level ∈ {general, encoding, mixed}` in `verify_mapping.py` and `verify_ro.py` from each cited declaration's module and namespace, instead of storing it in passages.json. Computing it avoids conflicts with ZH, which is actively extending both maps. Both verifiers print the split. Each chapter table (YI-ZHUAN and CHINESE-SOURCES) gets a "law level" column, and the summary line becomes "52 agree (19 through general laws, 33 through the encoding)". The table check stays exact, because `--table` regenerates the column. Changes in RO's chapter go through build_passages.py FIXES only. Coordinate with the ZH owner: either land with ZH, or have ZH rebase onto it.

## G11/G13 — the instance and applications ring

**Candidates** (theorem counts on 4c40745f8):
- Instances (G11): Hexagrams 72, HexagramLaws 130, HexagramPlaces 108, HexagramSites 103, HexagramSequences 98, PlaceTransitionNets 73.
- Applications (G13): these have no record and no chapter mention. Transactions 59, Reconfiguration 51, PooledEnvelopes 44, TreeSearch 35, Dispatch 34, GuardHorizon 32, ContingentPlans 18, Acceptance 17, RouteFormation 70, ResponseLearning 64, CodeAcquisition 39, PartialReadout 32, Coverage 22, SeedReach 15, ScopedReach 15, ProjectedLaws 28.
- ListTests, Naturals and IntegerOrder are support modules, not applications. They belong in R31's Prelude.

**Blockers.** A ring module cannot be imported by the core.
- `Commuting` imports `Hexagrams` (its "The Changes" section, 17 mentions). Split it into `Instances.CommutingChanges` before Hexagrams can leave.
- `WitnessRefinement` imports PooledEnvelopes, `JointPhase` imports ProjectedLaws, `LearnedGrouping` imports RouteFormation, `Actuation` imports ContingentPlans, and `AcceptanceFrames` imports Acceptance. Either move each importer's dependent section out with it, or keep these five in the core. Recommendation: keep them in the core (each is used), and ring only the importer-free modules.

**What check_becoming.py needs** (one checker run):
1. New lists `INSTANCES = [...]` and `APPLICATIONS = [...]`, added to `PURE` (still `Init`-only with empty axiom reports) and to the checked set. `source_file()` already maps nested names (`Becoming.Instances.X` → `Becoming/Instances/X.lean`).
2. Receipt `layer` values "instance" and "application", set where layer is assigned (about l.2873). The receipt schema accepts the new values.
3. An import-direction check: no CORE module imports an INSTANCES or APPLICATIONS module.
4. `lean_catalogue.py` gets `RECEIPT_GROUPS` and `GROUPS` entries for the ring, giving `lean-declarations/becoming-instances.md`. `THEOREM-CONNECTIVITY.py` classes the ring, and ring modules do not count as "apart".
5. Move the files with `git mv`, since lean sources are not move_pinned. Rename the modules to `Becoming.Instances.*` and update imports and `Becoming.lean`.
6. Rebind the records citing them (the Y1–Y5 and PT1 records; count them on the landing head) to the new paths and `/source_sha256/<Module>` pointers with the shared re-point tool. Update the passage-map declaration names, which ZH must also take.

Re-derive this list on R34's head: R29 (compression) and R31 (Prelude) both change membership.

## E12 — worktrees (37 besides main; .claude/worktrees ≈ 129 GB)

**Active; do not touch:**
- `agent-ae45fd9075b02ccd6`: the R29 agent, 12 dirty.
- `zhonghua`: ZH, 3 untracked.
- `agent-ab333e386f6f59ce1`: R28 agent, now clean at cb1be1f3c and an ancestor. Removable once its session confirms it is done.
- `wizardly-goldstine-4e6de8`: at 2b80b5500 (R25), clean, touched on 20 Oct. Confirm with its session.
- `keen-margulis-c70e97`: clean ancestor, touched on 20 Oct. Confirm.

**Not ancestors of main.** Give each a `refs/salvage/<name>` ref first, then remove:

| worktree (branch) | commits not on main | content on main? |
|---|---|---|
| compassionate-heisenberg (Z1) | 3 | 9 files same, 42 changed on main since; **18 only here** = dry-run receipt folder `becoming-checks/20261019T083809.972869Z`, not on main and not cited. Salvage ref keeps it |
| f3j-judgment-cd75fa | 12 (cherry: 8 equivalent on main, 4 not) | 9 same, 11 changed on main; relanded as F3J s1/s2/s3 |
| friendly-ellis (W step-1 plan) | 2 | 15 same, 3 changed on main |
| keen-jemison (RC kit) | 6 | 24 same, 4 changed; RC landed 860ebd030 |
| trusting-ptolemy (R20 review) | 2 | 1 same, 2 changed on main |
| unruffled-mendeleev (strange-kepler, RG kit) | 6 | 17 same, 4 changed; RG landed ce980ac0a |
| upbeat-lovelace (PT1) | 6 | 7 same, 8 changed; **18 only here** = dry-run receipt folder `20261019T090539.183632Z`, not on main and not cited |
| w-reroot (W2 pre-landing) | 1 | 35 same, 61 changed; W2+W3 landed 831fcaf73 |

**Ancestors with dirty trees:**
- `a2-chain`: 31 dirty files, each byte-identical to the A2 landing commit 29eb4ef3d, so their content is on main. Removable.
- Untracked dry-run receipt folders, none on main and none cited by a record:
  - epic-austin: 5 (20261019T090639, T091415, T092140, T103629, T104207);
  - g1: 20261019T003531;
  - great-stonebraker: 20261019T074455;
  - n6-reading: checks/becoming-checks/20261018T083745;
  - f3q: one log.
  These are rehearsal outputs of landed items, and the landed receipts are on main. They are build output, not data. If anyone wants them, tar them into `refs/salvage` as a blob commit first; otherwise remove them with the worktree.

**The other 18 ancestors** are clean, at heads already on main, and can be removed: charming-kirch, distracted-chaum, elastic-blackwell, elegant-dewdney, f3c, f3e, f3r, goofy-kare, goofy-villani, inspiring-shtern, kind-villani, modest-solomon, objective-lehmann, quirky-tesla, quizzical-ritchie, reverent-tu, unruffled-zhukovsky, xenodochial-bouman.

**Removal.** For each worktree: `git worktree remove <path>` (add `--force` only for the dry-run-receipt cases, after salvage), then `git branch -d` for merged branches. **Do not** run `git worktree prune` / `gc --prune`, per AGENTS. A registration whose folder is gone is removed with `git worktree remove` or by deleting `.git/worktrees/<name>`, once no session uses it.
