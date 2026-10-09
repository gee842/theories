# P23c、P24 与 P25 的独立审查 / Independent review of P23c, P24 and P25

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写这三个阶段。对象：`main` 的 `63437779`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of the three phases. Object: `main` at `63437779`.

**摘要（中文）。** 核心闭包的 29 个模块（26 个核心模块与 3 个基础模块）在仓库之外从前导重新编译，退出码为 0，没有警告；1732 条源声明（核心 1612、基础 120）的公理报告全部为空。闭包的 4894 个常量中，依赖公理的只有 34 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列完全相同；自第九次审查新增的 4 条属于 `Grazing`、`Scatter` 与 `Exposed` 的构造子。回执 `20261009T132323.308231Z`（1016 项定理／1662 项声明审计，核心闭包 29 个模块，包 27 个模块）、42 个源哈希与保留运行的 258 个产物都对。29 份变更记录的 348 个引用哈希与 90 个证明绑定都对；498 个别名中 457 个在核心中解析，其余 41 个属于未重建的桥接（26）、外围（5）与继承模块（10）。数学被接受，Lean 中没有发现数学错误。本审查写了 36 条探针声明（25 项定理），都不依赖任何公理。问题共十一项（O1–O11）：两项散文与记录中的错误，六项过强（其中两项是 M1 的残留，替 Ren 选择或排除了读法，一项预设了 Ren 尚未作出的选择的范围），一项缺少反例，两项表述与记账。

- **P24（前提的地图）。** 蕴含、八个独立性见证、`none_follows`、`mutualism_premised` 与 `premised_rests` 都对；每个见证都满足其余七个前提。问题在范围与散文（O9）。
  - 地图不含有限、被围住与可判定性。加上有限或每步被围住，只有活跃者给予就由只有活跃者取用与耗散推出（P24 自己的 `acting_of_enclosed`）；所以“没有一个前提藏在其余之中”只相对于这八个。
  - “普查在有限世界中自动成立”漏掉活动可判定；不给可判定性，这句对每个世界成立就是排中律（探针 Q9）。
  - 五个见证没有流或没有被围住的步，其余前提空成立。这足以证明独立；探针 Q10 给出平衡的一个有交换的见证。
- **P25（开放）。** 所立者的规律（`stock_eq`、`standing_runs_down`、`change_lowers`、`stills`）与世界上的读法都对。问题如下。
  - **“起作用的是被围住，不是有限”（O1，最严重之一）。** 定理用的是每步有限：活动的普查加每个关系项体现，给出所立者的普查。`kindling`（核心中已有）有活动的普查、每步被围住、生起者体现、平衡、耗散，而生起不息（Q1）；`ember` 每步被围住、每个关系项体现、平衡、耗散，没有普查，生起不息（Q2）。所以每步有限与被围住都起作用；不需要的是整个世界有限。章节的“开放是生起不息的条件”与记录标题“被围住的世界归于静止而不需要有限”不加这些前提就是错的。
  - **开放项已有答案（O2）。** “只要求生起者体现时被围住的世界是否归于静止”：在活动的普查之下不是（`kindling`）；有所立者的普查时生起停止（Q3），止息不一定（`dusk`）。
  - **可判定的相等（O3）。** 不是构造性证明的要求：`rests_enclosed` 与 `arising_opens` 不用它也成立（Q4）。
  - **exposed。** 它是真见证：八个前提推不出被围住。但章节由它推出“开放不由八个前提推出”（O4），这需要另一个见证：互利者满足全部八个而每步被围住（Q6）。记录说它的总水平“随世界不断上升”（O5）；实际每步都是一（Q5）。它的八个前提中有三个空成立，只披露了耗散一个（O6）。
- **P23c（第九次审查的处理）。** M2–M10 关闭，M1 部分关闭。
  - **M1 的残留（O7、O8，最严重之一）。** 世界的部分已改名，但“形成有限多时生成不息恰当止息不息”仍在章节 §2 与 §9、`Change`、根模块、README 与记录中（O7）。章节第 4 条、§2、§8 现状行、词汇表与一份记录说活动的读法“不是 Ren 的‘生成的’‘退化的’”，而 §8 把它列为 Ren 可选的候选；计划 §6 又把“作为关系不重叠”写成 Ren 定下的（O8）。三种地位并存。
  - **grazing（O10）。** 它不落在 §8 所写的选择内。但在活动需要支持之下，依存不变而被侵蚀的关系项在该步之后必不活跃（Q8）：grazing 的“不活”与 `ending_breaks` 一样是与终结同时发生的侵蚀。说它“不论终结之步的判定如何”，预设了 Ren 的选择只涉及被汲取者自身的终结。
  - 其余表述与记账见 O11：`law_decides` 只证明一个方向却写作“就是排中律”；`selected_le` 的说明仍称“选择项”；§2 的消耗句缺“被取用”；七个、八个与十个前提三种计数并列而没有说明关系；“最后一个‘giver’已去掉”不准确；P24 与 P25 的提交带着晚于提交的审查时间，已在 P23c 改正。
- **Ren 的原话与读法。** Ren 的原话在 `Space`、章节 §2 与 space-and-its-parts 中引用准确；章节第 4 条、§26 与 coming-and-ceasing-keep-pace 改写为“Ren 说二者不重叠”，丢了原话的“吧”与语境；计划 §6 把 AI 的“作为关系”记在 Ren 名下（O8）。名称都列为 Ren 的选择。没有发现支付、账目或“给予者”用语进入生生的表述。

**Summary (English).** The 29 modules of the core closure (26 core and 3 foundation modules) recompile from the prelude outside the repository, with exit 0 and no warnings, and all 1732 of their source declarations (1612 core, 120 foundation) have empty axiom reports. Of the closure's 4894 constants, the only ones depending on an axiom are 34 compiler-generated `injEq` lemmas, each depending only on `propext`; they are exactly the 34 the receipt lists, and the 4 added since the ninth review belong to constructors of `Grazing`, `Scatter` and `Exposed`. The receipt `20261009T132323.308231Z` (1016 theorems and 1662 declaration audits; core closure 29 modules, package 27) is correct, as are its 42 source hashes and the 258 artifacts of its retained run. For the 29 records changed by P24, P25 and P23c, 348 reference hashes and 90 proof bindings are correct; of their 498 aliases, 457 resolve in the core, and the other 41 belong to the unrebuilt bridge (26), the periphery (5) and inherited modules (10). The mathematics is accepted; no mathematical error was found in the Lean. This review wrote 36 probe declarations (25 of them theorems), none of which depends on any axiom. The eleven findings (O1–O11) are: two errors, in prose and in a record; six overclaims, two of them residues of M1 that choose or exclude a reading for Ren and one that presumes the scope of a choice Ren has not made; one missing counterexample; and two items of presentation and bookkeeping.

- **P24 (the map of premises).** The implications, the eight independence witnesses, `none_follows`, `mutualism_premised` and `premised_rests` are correct, and each witness meets the other seven premises. The findings concern scope and prose (O9).
  - The map leaves out finiteness, enclosure and decidability. With finiteness, or with every step enclosed, only active relata giving follows from only active relata taking and dissipation (P24's own `acting_of_enclosed`). "No premise hides in the others" holds only relative to the eight.
  - "A census holds automatically in finite worlds" omits decided activity. Over every world without it, that sentence is excluded middle (probe Q9).
  - Five witnesses have no flow or no enclosed step, so other premises hold vacuously in them. That suffices for independence; probe Q10 gives a balance witness with exchange at every step.
- **P25 (openness).** The standing laws (`stock_eq`, `standing_runs_down`, `change_lowers`, `stills`) and their reading of worlds are correct.
  - **"Enclosure, not finiteness, does the work" (O1, among the most serious).** The theorems use finiteness at each step: a census of activity with every relatum embodied gives a census of what stands. `kindling`, already in the core, has a census of activity, every step enclosed, embodied arising, balance and dissipation, and arising never ceases (Q1). `ember` has every step enclosed, every relatum embodied, balance and dissipation, no census, and arising never ceases (Q2). So finiteness at each step and enclosure both do work; what is not needed is a finite world. The chapter's "openness is a condition of arising without end" and the record title "an enclosed world comes to rest without being finite" are false without those premises.
  - **An open item is already answered (O2).** "Whether an enclosed world comes to rest when only whatever arises is embodied": under a census of activity, no (`kindling`). With a census of what stands, arising stops (Q3); ceasing need not (`dusk`).
  - **Decidable equality (O3)** is not required by the constructive proof: `rests_enclosed` and `arising_opens` hold without it (Q4).
  - **`exposed`** is a genuine witness that the eight premises do not give enclosure. The chapter infers from it that "openness does not follow from the eight premises" (O4); that needs another witness, mutualists meeting all eight with every step enclosed (Q6). The record says its total standing "keeps rising with the world" (O5); it is one at every step (Q5). Three of its eight premises hold vacuously, and only dissipation is disclosed (O6).
- **P23c (handling of the ninth review).** M2–M10 are closed; M1 is partly closed.
  - **Residues of M1 (O7, O8, among the most serious).** The parts of the space are renamed, but "with finitely many formations, generation is unceasing exactly when some formation ceases at arbitrarily late steps" remains in chapter §2 and §9, `Change`, the root module, the README and a record (O7). Chapter item 4, §2, the §8 status row, the glossary and one record say that the activity reading "is not Ren's 'generative' and 'degenerative'", while §8 lists it as a candidate for Ren's choice, and plan §6 records "as relations they do not overlap" as decided by Ren (O8). Three statuses stand side by side.
  - **`grazing` (O10)** lies outside the choice as §8 words it. But where activity needs support, a relatum whose unchanged dependence is undermined is not active after the step (Q8). So grazing's verdict is, like `ending_breaks`, undermining that co-occurs with an ending. "Whatever is chosen about drawing at an ending" presumes that Ren's choice concerns only the ending of the relatum drawn on.
  - Presentation and bookkeeping are in O11: `law_decides` proves one direction and is glossed "is excluded middle"; `selected_le` still says "the selection term"; the depletion sentence of §2 drops "taken from"; the counts of seven, eight and ten premises stand side by side without their relation; "the last 'giver' is gone" is inaccurate; the P24 and P25 commits carried stamps later than themselves, corrected in P23c.
- **Ren.** Ren's words are quoted exactly in `Space`, chapter §2 and space-and-its-parts. Chapter item 4, study §26 and coming-and-ceasing-keep-pace paraphrase them as "Ren says those do not overlap", dropping the closing 吧 and the context; plan §6 records the AI's "as relations" under Ren's name (O8). Names are listed as Ren's to choose. No payment, ledger or "giver" vocabulary enters the account of 生生.

## 0. Scope, materials and method

**Object.** `main` at `63437779ab8bd9d694b4541681b6d980a4c05b08`, through three commits:

- **P24 (`e5b61937`, 12:56:19Z).** [Becoming.Premises](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Premises.lean) in full; study §32 and the English P24 paragraph; the record [map-of-premises](../../../../theories/becoming/results/records/map-of-premises.md); plan row 241.
- **P25 (`a69455e3`, 13:13:31Z).** [Becoming.Openness](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Openness.lean) in full; study §33 and the English P25 paragraph; the record [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md); plan row 242.
- **P23c (`63437779`, 13:42:39Z).** The changes to `Space`, `Evolution`, `Premises` and `Openness`; study §34, the in-place corrections it lists in §26 and §28–§33, and the English P23c paragraph; the chapter (items 2, 4, 8, 10, §2, §8, §9 and glossary); foundation §5; plan §6 and §9; the eight records named in §34.

**Isolation.** The object was exported with `git archive 63437779` into the reviewer's scratch directory, and every file was read from there. Read-only `git show`, `git diff` and `git log` were used on the live repository for the stamps and diffs of the three commits. Nothing in the live repository or its `.git` was modified. During the review another session committed P26 (`f1ef72d2`, "Prove that ceasing needs arising, and the rest theorem"), P27 (`439d18bc`) and P28 (`24ab3973`); in between, the live tree had uncommitted changes to `Openness.lean`, `Population.lean`, the chapter, the study and records. None of that was read. No `make` target or repository checker was run, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where reviews are filed.

**Materials** (sha256 prefixes at `63437779`; each equals the exported file):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` / plan `BECOMING-UNIFICATION-PLAN.md` | `37c092be82ff7932` / `169cf5d6a2b7c204` |
| chapter `THE-THEORY-OF-BECOMING.md` / `BECOMING-FOUNDATION.md` | `184e37b56a07da15` / `712683243bda053c` |
| ninth review `BECOMING-P18B-P23-REVIEW.md` / `NONDUAL-METHOD.md` | `791888ed3aab6185` / `8c48b03a167a8909` |
| `_process/RESULT-WORKFLOW.md` / `AGENTS.md` | `ee0dd6a46e20f4ff` / `da432369737e9a1f` |
| receipt `becoming-verification.json` (= the retained run's `verification.json`) / `check_becoming.py` | `3c857657f8cfe3e5` / `de570572ae40cfb6` |
| `Becoming.lean` / package `README.md` | `d49bc80a445db17e` / `3f7f1498b55b574e` |
| `Becoming/Premises` / `Openness` / `Space` / `Evolution` | `d927cabd34d8449a` / `221b6a4eb1aa3165` / `d0d5ef4ce1b7511e` / `3ba9b515ebae3cad` |
| `Becoming/Change` / `Roles` / `Dissipation` / `Flow` | `6ef06dafae509c60` / `07086627aee4f9af` / `941026b4548d30da` / `22fd0168ed9a8027` |
| `Becoming/Population` / `Generation` / `Dependence` | `4c802d07f8ed0194` / `d2ae85e475265c41` / `d93f543b97124f23` |
| records map-of-premises / continued-change-needs-openness | `4e0cf515d7f9a7bd` / `043290fc3b37f627` |
| records space-and-its-parts / evolution-on-descent / rising-and-falling-in-one-exchange | `d7f0ea8bdb6361f3` / `6af3cd61a059cc6a` / `b6bd24e66eaf838d` |
| records coming-and-ceasing-keep-pace / theory-of-becoming-foundation / generation-is-replenishment | `57ada4d74a202a43` / `3f3e4d23594385bc` / `1cade5cf6780e3e2` |

**Read in full:** AGENTS.md, the nondual method, `RESULT-WORKFLOW.md` and the ninth review; `Premises`, `Openness` and `Space`; study §32–§34 and the English P24, P25 and P23c paragraphs; the JSON of map-of-premises and continued-change-needs-openness, and the P23c diffs of the other six named records. **Read in part:** the definitions the new modules use (`Web`, `Flow`, `Balances`, `Acting`, `Taking`, `ClosedAt`, `DissipatesOn`, `Dissipative`, `Enclosed`, `Around`, `Enclosed.around`, `Census`, `Distinct`, `Embodied`, `Supported`, `Dependent`, `MetAbove`, `UnderminingOn`, `DescendsAt`, `TransmitsWithin`, `Handing`, `Kindling`, `Frontier`, `Dusk`, `Mutualism`, `Spending`, `Leaking`, `Grazing`, `Undecided`, `ending_breaks`); the `Evolution` docstrings; `Change.lean:40–47` and `:450–460`; the root module's scope text; the chapter's full statement (lines 60–124), §2 (lines 190–290), §8 (lines 495–581), §9 (lines 600–625) and glossary (lines 640–721); foundation §5; plan §6 and §9; study §26 (lines 1640–1655) and the English P19 paragraph, for the in-place marks.

**Ren's words read**, for provenance:

| Source | sha256 prefix |
|---|---|
| [以关系结构分开更新与消耗](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md) | `a12a64304d9cb974` |
| [完整的生成之论](../../../../sources/15-codex-theory-conversations/2026-10-09-complete-theory-of-becoming.md) | `3ad2bca66a1e4fea` |

Study §33 quotes the second exactly ("aim a complete theory of becoming, and finish related work"). The first is the source of M1 and of O8.

**No external literature was read.**

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order.

- **Core.** All 29 modules of the receipt's `core_closure` exit 0 from the prelude with no warnings: `GenerativeCore` (with `import Std` removed, as the checker does), `InquirySufficiency`, `RelationalRenewal`, `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Change, Population, Identity, Wholes, Dissipation, Roles, Reserve, Evolution, Space, Premises, Openness, Metaethics, Ranking, Correspondence, Descent}` and the root module `Becoming`.
- **Bridge and periphery.** Not rebuilt; their bytes match the receipt.

The checks:

- **Receipt.** Status `passed`, Lean 4.29.1 `f72c35b3`, `core_compiles_from_prelude: true`, `source_unchanged_during_check: true`, a `core_closure` of 29 modules. All 42 `source_sha256` entries equal the object's files, and the checker hash equals `check_becoming.py`. The 258 artifacts of `becoming-checks/20261009T132323.308231Z` match their recorded hashes.
- **Counts.** Theorems per module: Premises 35, Openness 20, Space 47 (29 at P22), Evolution 25 (21 at P21). The package goes 939 → 974 (P24) → 994 (P25) → 1016 (P23c) theorems, as the study, the plan and the chapter's §9 say. The closure's source declarations are 1732 (1056 theorems).
- **Records.** The 29 records changed in `e5b61937^..63437779` have 348 `references` hashes, all equal to the object's files. All 90 proof bindings resolve their pointers to the bound sources' hashes and `passed`.
- **Names.** `Aliases.lean` (`77e9009d0df7f7ff…`) runs `#check @` on the 498 aliases of those records; 457 resolve in the core, and the other 41 are 26 `Becoming.Bridge`, 5 `CorrectionInquiry` periphery, and 10 inherited names (`BecomingCompatibility` 4, `OperativeCoherence` 6). `Names.lean` (`113542997a566235…`) does the same for the 1410 declaration names in their `references`: 1326 resolve, and none of the 84 that do not is a core declaration. Every P24, P25 and P23c declaration resolves.
- **Axioms.** `CoreAudit.lean` (`ffa18c5af0db67cd…`; `import Becoming` and 1732 `#print axioms` lines generated from the receipt) reports "does not depend on any axioms" for all 1732. `EnvAudit.lean` (`420f85b14528ce05…`, the checker's environment audit) enumerates every constant of the closure with `Lean.collectAxioms`: the per-module counts equal the receipt's `core_closure_constants` (4894 in all; Evolution 152, Space 238, Premises 245, Openness 79), and exactly 34 depend on an axiom, all `propext`, all generated `injEq` lemmas, whose names equal the receipt's `generated_axiom_dependencies`. The probe audits are in the appendix.

**Probes.** One file, `Review10.lean` (`ffc217787fa28534…`, 374 lines), imports the unchanged `Becoming` and compiles with exit 0 and no warnings. It has 25 theorems, 8 definitions and 3 instances, in ten groups Q1–Q10. Term mode only, no tactic. The probes are minimal models satisfying the published definitions unchanged, or theorems over those definitions. Following the nondual method, they show what the definitions admit, not what actual systems do; a probe refutes a sentence only where the sentence claims more than the definitions give.

| Probe | Shows | Finding |
|---|---|---|
| Q1 `q1_kindling` | `kindling` has a census of activity, embodied arising, balance, dissipation, every step enclosed (also around the active relata), and arising recurs; it is not embodied, and what stands cannot be listed | O1, O2 |
| Q2 `q2_ember` | kindling's flow with every relatum embodied: every step enclosed, embodied, balanced, dissipative, decidable equality, arising recurs, and no census | O1 |
| Q3 `q3_rests_standing`, `q3_dusk` | with a census of what stands, embodied arising, balance, dissipation and enclosure around what stands from some step on, arising does not recur; in `dusk` the same premises hold and ceasing recurs | O2 |
| Q4 `rests_enclosed_nn`, `arising_opens_nn` | `rests_enclosed` and `arising_opens` without `DecidableEq` | O3 |
| Q5 `q5_exposed` | in `exposed` what stands is listed, its total is one at every step, the holder falls across every step, no step is enclosed around what stands, and the world is not finite | O1, O5, O6 |
| Q6 `q6_mutualism` | mutualists meet all eight premises and every step is enclosed | O4 |
| Q7 `q7_living_crosses_ceasing` | with grazing's activity decided, the four ceasing corners of "living crosses" | O10 |
| Q8 `q8_undermined_inactive`, `q8_grazing` | under `Dependent`, a relatum whose unchanged dependence is undermined is not active after the step; grazing's browser is such a relatum | O10 |
| Q9 `q9_counted_decides` | if every finite world has a census, with no decidability supplied, every proposition is decided | O9 |
| Q10 `q10_draining` | a world meeting every premise but balance, with taking and dissipation binding at every step | O9 |

**Severity labels** (as in the ninth review).

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose is stronger than the Lean, including where a premise is left out or a reading is presented as settled.
- *missing counterexample*: a relevant witness is absent or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

No Lean statement is wrong. Both *errors* (O4, O5) are false sentences in prose; the Lean they cite is correct.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P24: are the implications correct, with their hypotheses stated? | **In the Lean, yes.** `Dependent.carried`, `Embodied.arising`, `Finite.counted` (with decided activity), `Finite.enclosed`, `acting_of_enclosed` (with every step enclosed) and `Finite.acting` hold. The prose drops decided activity for the census in three places, and states `acting_of_enclosed` per step while the theorem assumes every step enclosed. | O9 |
| 2. P24: does each witness meet the other seven? | **Yes, all eight.** Vacuity is in the table under O9: four witnesses have no flow, `scatter` has no enclosed step, and `novel` is the only witness in which all seven hold non-vacuously. That suffices for independence. | O9 |
| 3. P24: is `none_follows` the right statement? | **Yes.** For each listed `P`, not every world meeting the other listed premises meets `P`. `Q ≠ P` excludes only `P` itself, because the witnesses show the eight are pairwise different predicates. `independent` gives the stronger existential form. | — |
| 4. P24: are "eight premises" and "no premise hides in the others" fair? | **Relative to the eight, yes, and the boundary says so.** The map omits finiteness, enclosure and decidability, which the rest theorems use. Adding finiteness or every-step enclosure makes `Acting` follow; adding finiteness with decided activity makes `Counted` follow. | O9 |
| 5. P24: `mutualism_premised` and `premised_rests`? | **Correct.** `premised_rests` uses three of the eight (balance, dissipation, embodiment) with finiteness and decided activity; "the eight together" reads as if all were used. | O9 |
| 6. P25: are the standing laws correct? | **Yes.** `stock_eq`, `fall_lowers_on`, `standing_runs_down`, `standing_never_rises`, `change_lowers`, `stills`, `standingCensus`, `rises_of_arises`, `falls_of_ceases`, `rests_around`, `rests_enclosed` and `arising_opens` hold as glossed in the module. | — |
| 7. P25: does enclosure, not finiteness, do the work? | **No.** Finiteness at each step (a census, with every relatum embodied) and enclosure both do work (Q1, Q2, Q5). Finiteness of the world is not needed. | O1 |
| 8. P25: is "every relatum embodied" needed? | **With a census of activity, yes** (Q1, `kindling`). With a census of what stands, embodied arising suffices for arising (Q3) and not for ceasing (`dusk`). The study's and chapter's open item is answered. | O1, O2 |
| 9. P25: is `exposed` genuine, and its vacuity disclosed? | **Genuine for "enclosure does not follow from the eight".** Three of its eight premises hold vacuously; one is disclosed. The record misstates its total standing (Q5), and the chapter infers from it a conclusion it does not support (Q6). | O4, O5, O6 |
| 10. P25: is decidable equality honest or avoidable? | **Avoidable** for the world theorems (Q4). Only `Enclosed.aroundStanding`, a positive statement, uses it. | O3 |
| 11. P23c: are M1–M10 handled? | **M2–M10 closed; M1 partly.** See the table below. | O7, O8, O11 |
| 12. P23c: is any reading still chosen for Ren? | **Yes, in two ways.** The activity reading is excluded in five canonical places (and in the study and one record) and offered as a candidate in §8; plan §6 attributes the relational non-overlap to Ren. "Generation is unceasing exactly when ceasing recurs" survives at web level. | O7, O8 |
| 13. P23c: `law_decides`? | **The statement is correct; the gloss overstates.** It proves law → excluded middle; "is excluded middle" also claims the converse, which is not stated. | O11 |
| 14. P23c: does `grazing` rest on no choice of Ren's? | **On none listed.** Under `Dependent` its verdict is undermining that co-occurs with the dependent relatum's ending (Q8), the structure `ending_breaks` discloses. Its ceasing corner needs an instance the core lacks (Q7). | O10 |
| 15. P23c: is `leaking` non-vacuous? | **Yes.** The family of both sides is closed and taken from at every step (`leaking_world`, last conjunct), and dissipation binds there. | — |
| 16. P23c: is the `price` gloss corrected? | **Yes**, in the module doc, `selected`, `price`, the chapter, the glossary, the record and §29; one docstring (`selected_le`) still says "the selection term". | O11 |
| 17. P23c: are in-place corrections marked? | **Yes.** §26 and §28–§33 and the English paragraphs mark each changed sentence and quote the original. One marked paragraph (§26, line 1643) keeps the unmarked sentence "生成不息恰当止息不息". | O7 |
| 18. P23c: Ren's words and AI elaboration? | **Quoted exactly in `Space`, chapter §2 and space-and-its-parts; paraphrased in item 4, §26 and one record**, and the AI's "as relations" is attributed to Ren in plan §6 (a line older than P24). | O8 |
| 19. Stamps | **At the object, every stamp is at or before its commit.** The P24 and P25 commits each carried a later stamp; P23c corrected both. | O11 |
| 20. Records, receipt and counts | **Correct.** | — |

**Status of M1–M10.**

| Item | Status | Evidence |
|---|---|---|
| M1 | partly closed | `World.ArisingRecurs`, `CeasingRecurs`, `arising_iff_ceasing`, `arising_opens` renamed; `Space.lean:6–21` quotes Ren and gives two readings; §8 lists the reading of the proposal as Ren's first choice; plan rows 237 and §9 criterion 3 carry P23c notes. Residues: "generation is unceasing exactly when ceasing" at web level (O7); the activity reading excluded in five places while §8 offers it (O8). |
| M2 | closed, with residues | `Undecided`, `undecided_world`, `law_decides` in the core; decidability in the three commitment lists (chapter line 196, §8 line 545, foundation line 78), the logical commitment (line 546), foundation row 1, item 4's `rests` clause and the foundation record. Residues: §9 `Change` row, README `Change` row, the `unceasing_iff` docstring, and P24's census sentences (O9, O11). |
| M3 | closed, one residue | `selected_uniform`, `unselected`; module doc, `selected`, `price`, chapter item 2, §2, glossary, record and §29 corrected. `Evolution.lean:180` (`selected_le`) still says "the selection term" (O11). |
| M4 | closed | Item 4's clause now has balance and embodied members. |
| M5 | closed, one residue | (a) "at a step at which a family is dissipated on" in item 4, the record title, §9, root and README. (b) "dissipated on and taken from" in §8 row 509, §9 row 613 and plan row 235. Chapter §2 (lines 271, 273) still says "the depletion premise above follows" without "taken from" (O11). |
| M6 | closed | Item 8, §2, §8 and §9 state the bound; `Slack` is in the core. |
| M7 | closed as asked | `grazing`, `grazing_world`, `grazing_not_self`; `living_crosses` uses it. Scope note in O10. |
| M8 | closed | `leaking`, `leaking_world`; `rests_needs` uses it; the forced vacuity of `flicker` is stated. |
| M9 | closed | Item 2 has three sub-tags; wisdom is under empirical correspondence; §31 and plan row 238 state which criteria are met. |
| M10 | closed at the object | All stamps are at or before their commits; the foundation record uses the chapter's terms; §29's "给予者" is marked. Notes in O11. |

## 2. Findings

O1–O6 concern P25, O9 concerns P24, O7, O8 and O10 concern P23c, and O11 spans all three. O1 and O8 are the most serious.

### O1. overclaim (omitted premise): "enclosure, not finiteness" leaves out finitely many standing at each step

**Location.**

- `Openness.lean:6–7`: "This module states what does the work: not finiteness but enclosure." `:24–25`: "Finiteness is not needed." `:33–35`: "the standing laws need no embodiment, and the reading of worlds uses it to turn arising and ceasing into rising and falling".
- Record continued-change-needs-openness. Title: "an enclosed world comes to rest without being finite". Claim: "Finiteness is not needed". Correspondence: "this result shows that enclosure, not finiteness, does the work".
- Chapter item 4 (zh 76, en 108): "起作用的是被围住，不是有限 / Enclosure, not finiteness, does the work".
- Chapter §2 (zh 215, en 219): "使世界归于静止的是被围住，不是有限 … 所以开放是生起不息的条件 / What brings a world to rest is enclosure, not finiteness … openness is a condition of arising without end".
- Chapter §8 row 510: "被围住的世界不需要有限就归于静止，生起不息需要开放". The census and embodiment are absent from the whole clause.
- Foundation row 5 (line 76): "a world meeting all eight with no step enclosed generates without end, so what brings a world to rest is enclosure, a further condition, not finiteness".
- Study §33: intro (line 1987), "本节回答：起作用的是被围住，不是有限"; heading of line 2021, "有限不是关键"; English P25 (line 2355).

**What the Lean says.**

- `rests_around` and `rests_enclosed` assume a census of activity and every relatum embodied. `standingCensus` turns the two into a census of what stands, and `stills` runs on that census. Finitely many stand at each step.
- The record's hypotheses say so, and so does the body of study line 2021: "只要每步立着的有限多个被列出". Plan rows 242 and 264 and README line 44 also state the theorem with its premises. Only the headline drops them.
- `exposed` is neither finite nor enclosed, so it cannot separate enclosure from finiteness. Given the eight premises, it shows that enclosure is needed.

**Probes.**

- Q2 (`q2_ember`). Take kindling's flow and make each relatum active exactly while it stands. Every step is enclosed, every relatum is embodied, the flow balances and dissipates, and equality is decided. Arising recurs; only the census fails.
- Q1 (`q1_kindling`). `kindling` is already in the core, as the infinite world of `rests_needs`. It has a census of activity, embodied arising, balance and dissipation, and every step is enclosed, including around the active relata. Arising recurs. What fails is embodiment: every unburnt fuel stands, so what stands cannot be listed.
- Q5 (`q5_exposed`). In `exposed`, what stands at each step is listed. A census of what stands holds there, so `exposed` fails enclosure alone.

**Why it matters.**

- In `rests`, finiteness does two jobs: finitely many relata give both a census and enclosure. P25 shows that finitely many standing at each step, together with enclosure, can replace the finiteness of the whole world. That is a real generalization.
- The slogan says instead that finiteness does no work. The chapter's "openness is a condition of arising without end" states the necessary condition without the census and embodiment under which it holds.
- `kindling` is a core world in which arising never ends while every step is enclosed. A reader of §2, §8 or the foundation would conclude the opposite.

**Correction.**

- Say "what brings a world to rest is enclosure together with finitely many standing at each step (a census of activity with every relatum embodied); the world itself need not be finite".
- In §2 and §8: "in a world with a census whose relata are all embodied, balanced and dissipative, arising without end needs steps not enclosed".
- Record title: "… a world with finitely many standing at each step comes to rest once enclosed, without being finite".
- Next to `exposed`, the witness that enclosure cannot be dropped, cite `kindling` or Q2 as the witness that the census and embodiment cannot be dropped.
- Add to `Openness.lean:33–35` that embodiment, together with the census of activity, gives the census of what stands.

### O2. missing counterexample: the open item on embodied arising is already answered

**Location.**

- Chapter §8, further proofs (zh 571, en 578): "whether an enclosed world comes to rest when only whatever arises is embodied, not every relatum".
- Study §33 rebuttal 2 (line 2029): "是否可以只用生起者体现得到生起复现的部分，列为下一步".
- Record continued-change-needs-openness, next_delta: "Rest when only whatever arises is embodied rather than every relatum; enclosure without decidable equality".
- Record map-of-premises, next_delta: "whether all premises bring a world to rest under a census and enclosure rather than finiteness". P25 answers this, yet it was still listed at P23c.

**What the Lean says, with the probes.**

| Premises (all with balance, dissipation, embodied arising) | Arising | Ceasing | Witness |
|---|---|---|---|
| census of activity, every step enclosed | recurs | — | `kindling` (Q1) |
| census of what stands, enclosed around it from some step on | stops | — | `q3_rests_standing` (Q3) |
| the same, no census of activity (in `dusk` every relatum `f ≥ t` is active at step `t`) | stops | can recur | `dusk` (`q3_dusk`, Q3) |
| the same, with a census of activity | stops | stops (hand argument below) | — |

- **The hand argument.** Once arising has stopped, the finitely many active relata can only cease. So they cease finitely often. This review did not formalize it.
- **Enclosure without decidable equality** is answered by Q4 (O3).

**Why it matters.**

- The open programme lists as open a question whose negative answer is a core world (`kindling`). That world is already used in `rests_needs`, in the same module chain.
- Rebuttal 2 reasons only about ceasing, from relata that are active without standing. On the arising side, the obstacle is infinitely many standing at once, which is O1 again.

**Correction.**

- Replace the open item with the answer: `kindling` for "no"; Q3 for arising under a census of what stands; `dusk` for ceasing. Q3 can move into `Openness`.
- Update both next_delta fields.

### O3. overclaim: decidable equality is not needed for rest from enclosure

**Location.**

- Study §33 rebuttal 3 (line 2031): "是构造性证明的要求：把立着的两个列表合并为一个不重复的家族要判定相等".
- Record continued-change-needs-openness. Limitations: "decidable equality is a requirement of the constructive proof". Hypotheses: "rests_enclosed and arising_opens also need equality of relata to be decidable".
- `Openness.lean:184` and `:194`: `[DecidableEq w.Relatum]`.

**What the Lean says.**

- Only `Enclosed.aroundStanding` uses decidable equality. That lemma has a positive conclusion: an enclosed step is enclosed around what stands.
- The world theorems have negative conclusions. The comparisons that `stills` makes are comparisons of natural numbers, which are decided.

**Probe Q4.**

- `nn_around`: without decidable equality, an enclosed step is not not enclosed around any list.
- `stills_nn`: runs `stills` when the enclosure is only not refuted.
- `rests_enclosed_nn` and `arising_opens_nn`: the two world theorems, without `DecidableEq`.

All are axiom-free.

**Why it matters.** The text states as a limitation something the result does not have. The chapter treats decidability as a logical commitment of the representation (line 546), so a needless instance enlarges the stated commitments. Severity is low.

**Correction.**

- Drop the instance from `rests_enclosed` and `arising_opens`, as Q4 shows how. Alternatively, keep it and write "the proof given uses decidable equality; it is not needed".
- Update the record's hypotheses, limitations and next_delta, and rebuttal 3.

### O4. error (in prose): `exposed` is cited for "openness does not follow from the eight premises"

**Location.**

- Chapter item 4. Zh 76: "满足全部八个前提而没有一步被围住的世界生起不息，所以开放不由八个前提推出（`World.exposed_world`）". En 108: "so openness does not follow from the eight premises".
- Chapter §2. Zh 215: "所以开放是生起不息的条件，不是前提的推论". En 219: "not a consequence of the premises".
- §8 row 510: "满足全部前提的开放世界生起不息".

**What the Lean says.**

- `exposed_world` gives a world meeting the eight premises in which no step is enclosed. So enclosure does not follow from the eight. Study lines 2023 and 2027 say exactly this, correctly.
- To show that openness does not follow, one needs a world meeting the eight with every step enclosed.
- The §8 sentence reads as a general law. It describes one world.

**Probe Q6.** `mutualism` meets all eight premises, and every step is enclosed: the world is finite, and its flow is still. Arising does not recur. Together with `exposed`, the eight premises decide neither enclosure nor openness.

**Correction.**

- Item 4: "so enclosure does not follow from the eight premises (`exposed_world`); nor does openness (`mutualism_premised`, `Finite.enclosed`)".
- §2: "openness is, under these premises, a condition of arising without end; the eight premises decide neither it nor enclosure".
- §8: "a world meeting all eight with no step enclosed arises without end".

The intended point, that rest does not follow from the eight premises without enclosure, is correct.

### O5. error (in a record): the total standing of `exposed` does not rise

**Location.** Record continued-change-needs-openness, correspondence: "its total standing keeps rising with the world / 它的总水平随世界不断上升".

**What the Lean says.**

- What stands in `exposed` is the holder alone. The ground relata stand at zero at every step.
- Q5 (`q5_exposed`): the total standing is one at every step, and the holder falls across every step.
- Nothing rises in total. What is unbounded is the number of relata the world exchanges with.

**Correction.** "Its total standing stays at one; what is unbounded is the number of relata it exchanges with, each at zero net."

### O6. presentation (vacuity): what `exposed` exercises

**Vacuity.**

| Premise in `exposed` | How it holds | Disclosed |
|---|---|---|
| Dependent | vacuously: nothing is required (`requires := False`) | no |
| Transmitting | vacuously: there is no dependence to transmit | no |
| Taking | half by fiat: the taker is active (binding), and it draws on everything (`draws := True`) | stated in the docstring of `web` only |
| Dissipative | vacuously: no step is enclosed | yes (study lines 2023, 2027; record) |
| Balanced, Acting, Embodied, Counted | non-vacuously | — |

**Other points.**

- `rests_enclosed` uses four of the eight: census, embodiment, balance and dissipation. "Meets all eight premises" adds four that play no part in the rest theorem.
- The openness `exposed` exhibits is a zero-net exchange with relata standing at zero (disclosed, rebuttal 1). At world level, "needs openness" therefore means exchange with relata beyond every finite family at arbitrarily late steps. Nothing need flow in.
- At family level, drawing in has content (`generation_draws_in`). At world level, no "beyond" exists from which anything is drawn. The record title "continued change needs openness" reads naturally as needing inflow.

**Correction.**

- In study §33 and in the record's counterexamples, list which premises hold vacuously in `exposed`, and say that the rest theorem uses four.
- In the claim, say that openness here is exchange beyond every finite family, and that `exposed` meets it with zero net flow.

### O7. overclaim (residue of M1): "generation is unceasing exactly when ceasing recurs" survives at web level

**Location.**

- `Change.lean:43–45` (module doc) and `:454–455` (`unceasing_iff`): "where the formations are finitely many, generation is unceasing exactly when some formation ceases at arbitrarily late steps".
- `Becoming.lean:70–72`, with the same wording.
- README line 34, Change row: "形成有限多时，生成不息恰当止息在任意晚的步出现".
- Chapter §2. Zh 196: "形成有限多且活动可判定时，生成不息恰当某个形成在任意晚的步止息". En 203: "generation is unceasing exactly when ceasing is".
- Chapter §9, Change row (line 609): "形成有限多时生成不息恰当止息不息".
- Record coming-and-ceasing-keep-pace, claim: "形成有限多时，生成不息恰当某个形成在任意晚的步止息（Web.unceasing_iff）".
- Study §26 (line 1643): "所以在形成有限多的展开中，生成不息恰当止息不息：没有只生不灭的有限世界". This sentence is unmarked, though it sits in the paragraph that carries the P23c mark.
- Foundation row 5: `exposed` "generates without end".

**What the Lean says.**

- `Web.Unceasing` is "some formation arises at arbitrarily late steps", and `World.ArisingRecurs := w.web.Unceasing`. `unceasing_iff` is the web form of `arising_iff_ceasing`.
- P23c renamed the world form and left the web wording unchanged.
- The chapter labels "生成不息" as the author's reading of the second 生 (line 267). These sentences carry no such label.
- Within the chapter, item 4 says that the activity reading is not Ren's "生成的", while §2 line 196 calls arising recurrence "生成不息" and ties it to ceasing. That ties the chapter's word for Ren's "generative" (生成) to ceasing, which M1 asked to remove.

**Correction.**

- Write "arising recurs exactly when ceasing recurs" (生起复现恰当止息复现) in these places, with decidability where the web form needs it (O11). Write "arises without end" in foundation row 5.
- Alternatively, keep "生成不息" only with the label "(the author's reading of the second 生 as arising)".

### O8. overclaim (a reading chosen for Ren; residue of M1): the activity reading has three statuses

**Location and statuses.**

- **Excluded.**
  - Chapter item 4 (76, 108): "这是活动的读法，不是 Ren 的“生成的”“退化的” / This is the reading of activity, not Ren's 'generative' and 'degenerative'".
  - §2 (215, 219): "生起复现与止息复现不是 Ren 的“生成的”“退化的”".
  - §8 row 510 and glossary line 693.
  - Record coming-and-ceasing-keep-pace, correspondence: "This is not a reading of Ren's 'generative, degenerative': Ren says those do not overlap".
  - Study §26 (line 1643) and the English P19 paragraph.
- **A candidate for Ren's choice.**
  - Chapter §8, Ren's choices, first item: "活动的读法（生起复现与止息复现，有限世界中二者重合），或关系的读法 …，或其他".
  - `Space.lean:11–18`: "Which parts Ren's 'generative' and 'degenerative' name is Ren's to choose … The spine offers two readings".
  - space-and-its-parts.
  - Study §34.4, rebuttal 1: "脊柱上的两种候选都写出".
- **Settled by Ren as relational.** Plan §6, item 2 (line 168), under "由 Ren 定下": "生成与退化作为关系不重叠（Ren 追问，`renewing_not_consuming`）". This line predates P24: it comes from checkpoint `4e7642e1`. P23c did not touch it, and the ninth review did not flag it.

**Ren's words.** After "为什么？我G0是什么？", Ren wrote "generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧". The sentence ends in 吧. The qualifier "作为关系" and the citation of `renewing_not_consuming` come from the AI correction note in the same source: "生成与退化作为关系不重叠，已由 `renewing_not_consuming` 证明". The chapter's "Ren 说二者不重叠 / Ren says those do not overlap" drops the 吧 and the context. Chapter §2 quotes the sentence exactly.

**Why it matters.**

- A reading cannot be excluded for Ren and also offered to Ren as a candidate.
- The exclusion is the AI's inference from Ren's words: if the two do not overlap, a reading on which they coincide is not what Ren means. The inference is reasonable, but it is the AI's, and it decides the first item of §8.
- Plan §6 records an AI gloss as Ren's decision.

**Correction.**

- Choose one status in the canonical texts. If the choice stays with Ren, replace "不是 Ren 的…" with Ren's quoted words and a labelled inference. For example: "Ren 问“…但是他们不overlap吧”（原话）；在活动的读法下二者在有限世界中重合，所以若取不重叠，这一读法不是其所指（AI 推论）".
- In plan §6, separate Ren's words from the AI's "作为关系" and `renewing_not_consuming`.

This review does not choose.

### O9. overclaim (omitted premise) and presentation: P24's census sentence, the reach of the map, and vacuity

**(a) Decidability omitted.**

- Where: study §32 (line 1970), "一个在有限世界中自动成立：普查"; record map-of-premises, correspondence, "hold automatically in finite worlds (a census)"; chapter §9, Premises row (618), "有限世界有普查".
- The module doc, `Finite.counted`, the record's claim and its hypotheses all state decidability.
- Q9 (`q9_counted_decides`): if every finite world has a census, with no decidability supplied, every proposition is decided. The witness is one relatum, active exactly when `Q`, with no flow. This is the commitment of M2 again.

**(b) Pointwise or global.**

- The `acting_of_enclosed` docstring and the record's claim say "only active relata give across every enclosed step". The theorem assumes every step enclosed.
- The pointwise form holds by the same proof but is not stated. The record's hypotheses state the global form.

**(c) Vacuity of the witnesses.** Each witness proves independence correctly. The table lists the other premises that hold vacuously in each.

| World (fails) | Vacuous among the premises it meets |
|---|---|
| `strained` (Dependent) | Acting, Taking, Dissipative, Transmitting (no flow) |
| `unbalanced` (Balanced) | Acting, Taking, Dissipative, Transmitting (no flow) |
| `scatter` (Acting) | Dependent (nothing required), Dissipative (no enclosed step; disclosed), Transmitting (levels steady) |
| `morsel` (Taking) | Dependent (nothing required), Acting (nothing given), Transmitting (nothing descends) |
| `keeping` (Dissipative) | Transmitting (levels steady) |
| `latent` (Embodied) | Dependent (never active), Acting, Taking, Dissipative, Transmitting (no flow) |
| `multitude` (Counted) | Dependent (nothing required), Acting, Taking, Dissipative, Transmitting (no flow) |
| `novel` (Transmitting) | none |
| `mutualism` (all eight) | Acting, Taking, Dissipative, Transmitting (no flow) |
| `exposed` (all eight, P25) | Dependent, Transmitting, Dissipative; Taking by drawing on everything (O6) |

- So the independence of activity needing support, balance, embodiment and the census is shown by worlds without flow, in which the four flow premises (Acting, Taking, Dissipative, Transmitting) hold vacuously. That suffices logically.
- Q10 (`q10_draining`) gives a balance witness in which taking, dissipation, dependence and embodiment bind at every step. Acting and Transmitting still hold vacuously there, since nothing is given.
- No world in the core meets all eight with each binding. Such a world, finite, exchanging and depending, would show that the conjunction is met by more than a still world before `premised_rests` brings it to rest. This review did not build one.

**(d) "All of them together".** The record title, the module doc ("the eight together") and chapter §9 row 618 ("全部前提一起归于静止") overstate how many premises are used. `premised_rests` uses balance, dissipation and embodiment (through embodied arising), with finiteness and decided activity. The other five play no part.

**(e) What the map omits.**

- The map leaves out finiteness, enclosure and decidability, the premises on which the rest theorems turn.
- With them added, `Acting` follows (`Finite.acting`, `acting_of_enclosed`), and so does `Counted` (`Finite.counted`).
- The record's limitations say that independence is relative to the eight. Study line 1971 ("没有一个前提藏在其余之中：每个都是对世界的独立限定") needs the same qualifier.

**Correction.**

- Add decidability in the three places.
- State `acting_of_enclosed` pointwise, or word it globally.
- Add a vacuity column to the independence table of §32 and to the record.
- Write "uses three of the eight" for `premised_rests`.
- Qualify study line 1971.

### O10. overclaim (presumes the scope of a choice Ren has not made): `grazing`

**Location.**

- `Space.lean:660–663`: "A finite world in which arising recurs and not every event is living, whatever is chosen about drawing at an ending".
- Chapter item 10 (88, 120): "不活的一边不依赖对终结之步自我汲取的判定".
- Study §34, rebuttal 3 (line 2104): "它不依赖终结之步自我汲取的判定".

**What the Lean says.**

- `grazing_world` and `grazing_not_self` are correct. The grazer draws only on the pool, the pool is never active, and the grazer's own dependence stays met.
- The undermined relatum, the browser, is active only at step 0. The undermining therefore co-occurs with the browser's ending.
- Q8 shows that this is forced. Suppose activity needs support, a dependence persists across a step at no lower need, and the condition falls below that need. Then the relatum depending is not active after the step (`q8_undermined_inactive`). `q8_grazing` applies this to the browser.
- So in any world where activity needs support, every undermining of an unchanged dependence co-occurs with the ending of the relatum depending.
- `Roles` discloses this structure for `ending_breaks`: "co-occurrence with the ending, whatever ends it … That the drawing ends the relatum would need a counterfactual relation".

**Why it matters.**

- §8 words the choice for drawing on an embodied, self-bearing relatum at its own ending. `grazing` lies outside that wording.
- Whether Ren's reading of 生生 counts drawing that co-occurs with another relatum's ending against living is the same kind of question. Under `Dependent`, it covers every undermining of an unchanged dependence.
- "Whatever is chosen" presumes that Ren's choice concerns only the drawn relatum's own ending.

**Also.**

- Chapter item 10 says that living "跨越生起与止息 / crosses arising and ceasing".
- `living_crosses` states only the arising corners. The ceasing corners follow through `arising_iff_ceasing` only with decided activity, and the core has no decidability instance for `grazing`.
- Q7 supplies the instance and proves the four ceasing corners. The claim is true, but the core does not check it.

**Correction.**

- Write "outside the choice as §8 words it".
- Add to §8 the question whether undermining that co-occurs with the ending of the relatum depending counts against living, and for which drawers. Note that under `Dependent` every undermining of an unchanged dependence is such an undermining (Q8).
- Either add `grazing_decided` and the ceasing corners to the core, or say "crosses arising" only.

### O11. presentation

- **(a) `law_decides`.** Locations: `Space.lean:759`, chapter §2 (215, 219), §8 row 510, chapter line 546 and glossary line 693. The theorem proves that the law implies excluded middle. "Is excluded middle / 就是排中律" asserts an equivalence, and the converse is not stated. Write "implies excluded middle", or state the converse.
- **(b) `arising_opens`.** The theorem proves `¬ ∀ t, T ≤ t → Enclosed t`. The gloss "needs at arbitrarily late steps a step not enclosed" reads as `∃ t, T ≤ t ∧ ¬ Enclosed t`, which is constructively stronger. Write "not every step from any point on is enclosed".
- **(c) Residues of M2.** Decidability is missing in the §9 Change row (609), the README Change row (34), `Change.lean:43–45`, the `unceasing_iff` docstring (454) and `Becoming.lean:70–72`. `unceasing_iff` takes the section variable `[∀ t f, Decidable (W.active t f)]`.
- **(d) Residue of M3.** `Evolution.lean:180`, the `selected_le` docstring, still reads "the selection term is at most …". §34.1 keeps `selected_le` "as a statement about the weighted total".
- **(e) Residue of M5(b).** Chapter §2 line 271 reads "上面作为前提的消耗由此推出" and line 273 reads "and the depletion premise above follows". Both lack the qualifier that §8 row 509, §9 and the plan carry: "for events whose family is dissipated on and taken from at each step".
- **(f) Counts.**
  - Chapter §2 and §8 row 510 give "seven premises" (`contingent`) and then "the remaining eight" (P24). Study §31 and §34 give "the ten premises stated of worlds".
  - All three counts are correct. The text does not say that the eight are the seven without the reserve (which follows from activity needing support) plus a census and bounded transmission, nor that the ten add the two weaker forms.
  - The foundation record still says "seven of which are shown met by some worlds and not by others".
- **(g) "The last 'giver' is gone"** (English P23c, line 2372). `World.Scatter.Relatum.giver` (P24) remains in the core. It is a witness constructor, not vocabulary for 生生, so it falls outside Ren's correction. Write "the last 给予者 in the account" or rename the constructor.
- **(h)** In the map-of-premises history, "integration note.premised_rests" lacks a space.
- **(i) Stamps.** The P24 commit (12:56:19Z) carried 13:00 for map-of-premises, and the P25 commit (13:13:31Z) carried 13:30 for continued-change-needs-openness. P23c disclosed both and corrected them (§34.1, M10). generation-is-replenishment moved from 12:10 to 12:05 with no content change. Whether 12:05 is the actual revision time cannot be checked from the repository.

## 3. What remains sound

**Build and receipt.**

- The 29 modules of the core closure compile from the prelude, exit 0, with no warnings.
- All 1732 source declarations have empty axiom reports. Of the 4894 constants, the only ones with an axiom are the 34 generated `injEq` lemmas, on `propext`, exactly as the receipt lists them.
- The receipt's counts, source hashes and retained artifacts are correct, as are the 348 reference hashes and 90 proof bindings of the 29 changed records.

**P24.**

- `Dependent.carried`, `Embodied.arising`, `Finite.counted`, `Finite.enclosed`, `acting_of_enclosed`, `Finite.acting` and `follows` are correct, with their hypotheses in the signatures.
- Each of the eight witnesses meets the other seven and fails its own (`independent`).
- `none_follows` is the right statement. `Q ≠ P` removes only `P`, since the witnesses show the eight are pairwise different predicates.
- `mutualism_premised` and `premised_rests` are correct.
- The record's hypotheses and limitations state decidability, global enclosure, and the relativity of independence to the eight.

**P25.**

- `StandingCensus.stock_eq`, `fall_lowers_on`, `standing_runs_down`, `standing_never_rises`, `change_lowers`, `stills`, `standingCensus`, `rises_of_arises`, `falls_of_ceases`, `rests_around`, `rests_enclosed`, `arising_opens` and `exposed_world` are correct.
- The standing laws are a real generalization of `rests`. The finiteness of the whole world gives way to finitely many standing at each step together with enclosure (O1 concerns only how this is stated).
- The record's hypotheses, the body of study line 2021, plan rows 242 and 264, and README line 44 state the theorem with its premises.
- Study lines 2023 and 2027 say correctly that enclosure does not follow from the eight premises, and that a dissipation excluding `exposed` would be a further premise, to be stated openly.

**P23c.**

- The renaming to `ArisingRecurs`, `CeasingRecurs` and `arising_iff_ceasing` is correct, and the statements are unchanged.
- `Undecided`, `undecided_world` and `law_decides` are correct.
- `grazing_world` and `grazing_not_self` are correct.
- `leaking_world` is correct, and its dissipation binds at every step.
- `selected_uniform`, `unselected` and `Slack` are correct.
- Every sentence changed in place in §26 and §28–§33 is marked and quotes the original (O7 notes one sentence in §26 left unchanged), and §34.1 records the handling item by item. The P24 and P25 stamps were disclosed and corrected.

**Ren and method.**

- Ren's words are quoted exactly in `Space`, chapter §2 and space-and-its-parts, and the readings and names are listed as Ren's.
- No payment, cost, ledger or "giver" vocabulary enters the account of 生生. "Draws in", "replenishment" and "taken from" describe relations within one unfolding.
- The worlds are read with one kind of relatum, as roles in one exchange. No module evaluates openness, rest or living.
- The nondual boundary of the method holds. The probes here show what the definitions admit, not what actual systems do.

## 4. What would change the verdicts

1. **O1.** State the rest theorem with finitely many standing at each step in every headline (module doc, record title and correspondence, chapter item 4, §2, §8 row 510, foundation row 5, study §33 and English P25). Verdict 7 then becomes "yes, as qualified".
2. **O2.** Replace the open item with its answer (`kindling`; Q3 for arising; `dusk` for ceasing) and update both next_delta fields.
3. **O3.** Remove `DecidableEq` from `rests_enclosed` and `arising_opens`, or say it is not needed. Verdict 10 then has nothing left to qualify.
4. **O4, O5.** Correct the two sentences. Cite `mutualism_premised` for openness not following.
5. **O7, O8.** M1 closes when two things are done. First, the web-level wording says "arising recurs" or carries the author's label. Second, the canonical texts give the activity reading one status, with Ren quoted rather than paraphrased. Plan §6 should separate Ren's words from the AI's "as relations".
6. **O9–O11.** Make the qualifications and edits listed.
7. **Withdrawals.**
   - Ren stating that the activity reading is not what Ren meant would reduce O8 to quoting that statement.
   - Ren stating that the choice about drawing at an ending concerns only the drawn relatum's own ending would remove O10's main point. The Q7 note would remain.
   - No change of wording can remove the counterexamples of O1, O2 and O4. They are theorems about the published definitions.

**Ren's choices still open.**

- These are as listed in §34.3 item 7: the reading of the proposal's "generative, degenerative"; the readings of 生, 生生 and the second 生, including whether arising that depends on depletion counts as generation; drawing at an ending; the reading of continuation and the level at which 生生不息 is read; living-on and descent as direct valuations; names.
- This review adds two:
  - whether undermining that co-occurs with the ending of the relatum depending counts against living (O10);
  - whether "openness" (开放) names exchange beyond every finite family or inflow (O6).

**Not checked.**

- **Rebuilt and run.**
  - The bridge and periphery were not rebuilt; their bytes match the receipt.
  - No `make` target, `research-check` or `research-render` was run.
- **Not read.**
  - No external literature.
  - P26 (`f1ef72d2`), P27 (`439d18bc`) and P28 (`24ab3973`), committed during the review, which may already address some of these findings.
- **Checked only in part.**
  - Chinese–English parity was checked only at the cited lines.
  - The vacuity tables in O6 and O9 were read from the proofs; they are not stated as theorems, except for Q10.
- **Not formalized or built.**
  - The hand argument in O2 (ceasing stops under a census of activity once arising has stopped).
  - A world meeting all eight premises with each binding (O9(c)).

## Appendix A. Probe source

`Review10.lean` (sha256 `ffc217787fa285343bb79a8bedcb7f05c18f9a5f6b41b7585c0a32017f3c5b81`, 374 lines; next to this review). Compiled with `LEAN_PATH=<core build>:. lean -o Review10.olean Review10.lean`: exit 0, no warnings, no `sorry`, no tactic.

```lean
import Becoming

/-!
Probes of the tenth independent review (P24, P25, P23c). Each is term-mode and
axiom-free; none is part of the repository.
-/

namespace Review10

open Becoming

/-! ## Q1. Kindling: a census of activity, enclosure and embodied arising do not bring rest -/

/-- Which side a kindling side is. -/
def kside : Kindling.Relatum → Bool
  | .side x => x
  | .fuel _ => false

/-- The index of a fuel. -/
def kfuel : Kindling.Relatum → Nat
  | .side _ => 0
  | .fuel n => n

theorem side_mem_sides : ∀ x : Bool,
    Kindling.Relatum.side x ∈ [Kindling.Relatum.side true, .side false]
  | true => .head _
  | false => .tail _ (.head _)

/-- Every fuel stands at the first step. -/
theorem unburnt_zero : ∀ n, Frontier.unburnt n 0 = 1
  | 0 => rfl
  | _ + 1 => rfl

theorem fuel_stands (n : Nat) : 0 < 2 * Frontier.unburnt n 0 :=
  Eq.subst (motive := fun m => 0 < 2 * m) (unburnt_zero n).symm Nat.zero_lt_two

/-- In kindling the holder is the one active relatum: a census of activity exists. -/
theorem kindling_census :
    World.kindling.web.Census fun t => [Kindling.Relatum.side (Handing.holder t)] :=
  fun t => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side b => ⟨fun active => Eq.subst
          (motive := fun c => Kindling.Relatum.side c ∈ [Kindling.Relatum.side (Handing.holder t)])
          ((Exposed.stands_iff b t).mp active).symm (.head _),
        fun mem => (Exposed.stands_iff b t).mpr (match mem_cons_cases mem with
          | .inl same => congrArg kside same
          | .inr no => nomatch no)⟩
    | .fuel n => ⟨fun no => False.elim no,
        fun (mem : Kindling.Relatum.fuel n ∈ [Kindling.Relatum.side (Handing.holder t)]) =>
          match mem with
          | .tail _ no => (nomatch no)⟩⟩

/-- Every step of kindling is enclosed around the active relata. -/
theorem kindling_around (t : Nat) :
    World.kindling.flow.AroundStanding (fun t => [Kindling.Relatum.side (Handing.holder t)]) t :=
  match Kindling.around t with
  | ⟨es, distinct, sides, closed⟩ =>
    ⟨es, distinct,
     fun _ mem => match mem_cons_cases mem with
      | .inl same => Eq.subst (motive := fun d => d ∈ es) same.symm (sides _ (side_mem_sides _))
      | .inr no => (nomatch no),
     fun _ mem => match mem_cons_cases mem with
      | .inl same => Eq.subst (motive := fun d => d ∈ es) same.symm (sides _ (side_mem_sides _))
      | .inr no => (nomatch no),
     closed⟩

/-- Kindling has a census of activity, whatever arises in it is embodied, its flow balances
and dissipates, every step is enclosed (around the active relata too), and arising recurs.
It is not embodied, and what stands in it at a step cannot be listed: every unburnt fuel
stands. So in `World.rests_around` and `World.rests_enclosed`, embodiment cannot be
weakened to embodied arising; embodiment there also bounds what stands. -/
theorem q1_kindling :
    World.kindling.Counted ∧ World.kindling.ArisingEmbodied ∧ World.kindling.Balanced ∧
    World.kindling.Dissipative ∧
    (∀ t, World.kindling.flow.AroundStanding
      (fun t => [Kindling.Relatum.side (Handing.holder t)]) t) ∧
    (∀ t, World.kindling.flow.Enclosed t) ∧
    World.kindling.ArisingRecurs ∧ ¬ World.kindling.Embodied ∧
    ¬ ∃ stand, World.kindling.web.StandingCensus stand :=
  ⟨⟨_, kindling_census⟩, World.kindling_arising, World.kindling_world.1, World.kindling_world.2.1,
   kindling_around,
   fun t => match kindling_around t with
    | ⟨es, distinct, _, _, closed⟩ => ⟨es, distinct, closed⟩,
   World.kindling_world.2.2.2.1,
   fun embodied => (embodied (.fuel 0) 0).mpr (fuel_stands 0),
   fun ⟨stand, census⟩ => beyond_not_mem ((stand 0).map kfuel)
     (mem_map_of (g := kfuel)
       (((census 0).2 (.fuel (beyond ((stand 0).map kfuel)))).mp (fuel_stands _)))⟩

/-! ## Q2. Ember: without a census, an embodied, enclosed world need not come to rest -/

namespace Ember

/-- Kindling's levels, with each relatum active exactly while it stands, and no
dependence. -/
def web : Web Kindling.Relatum Kindling.Relatum where
  level t c := Kindling.web.level t c
  active t c := 0 < Kindling.web.level t c
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Ember

/-- Kindling's flow with every fuel embodied: infinitely many relata stand and are active
at each step. -/
def ember : World :=
  ⟨Kindling.Relatum, Kindling.flow, Ember.web⟩

/-- Equality of relata is decided, so every hypothesis of `rests_enclosed` but the census
can be supplied. -/
def decEqRelatum : (a b : Kindling.Relatum) → Decidable (a = b)
  | .side true, .side true => isTrue rfl
  | .side false, .side false => isTrue rfl
  | .side true, .side false =>
    isFalse fun h => Bool.noConfusion (show true = false from congrArg kside h)
  | .side false, .side true =>
    isFalse fun h => Bool.noConfusion (show false = true from congrArg kside h)
  | .fuel n, .fuel m => match Nat.decEq n m with
    | isTrue same => isTrue (congrArg Kindling.Relatum.fuel same)
    | isFalse other => isFalse fun h => other (congrArg kfuel h)
  | .side _, .fuel _ => isFalse fun h => Kindling.Relatum.noConfusion h
  | .fuel _, .side _ => isFalse fun h => Kindling.Relatum.noConfusion h

instance : DecidableEq ember.Relatum := decEqRelatum

/-- Every step enclosed, every relatum embodied, balanced, dissipative, and arising recurs;
there is no census. So the census in `World.rests_enclosed` cannot be dropped: finitely
many standing at each step does work there. -/
theorem q2_ember :
    (∀ t, ember.flow.Enclosed t) ∧ ember.Embodied ∧ ember.Balanced ∧ ember.Dissipative ∧
    ember.ArisingRecurs ∧ ¬ ember.Counted :=
  ⟨fun t => match Kindling.around t with
    | ⟨es, distinct, _, closed⟩ => ⟨es, distinct, closed⟩,
   fun _ _ => Iff.rfl,
   Kindling.balances, Kindling.dissipative,
   fun N => match Kindling.kindling.2.2.2.2.2 true N with
    | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩,
   fun ⟨alive, census⟩ => beyond_not_mem ((alive 0).map kfuel)
     (mem_map_of (g := kfuel)
       (((census 0).2 (.fuel (beyond ((alive 0).map kfuel)))).mp (fuel_stands _)))⟩

/-! ## Q3. With what stands listed, embodied arising suffices for arising; not for ceasing -/

/-- With a census of what stands, whatever arises embodied, balance, dissipation and every
step from some step on enclosed around what stands, arising does not recur. -/
theorem q3_rests_standing {w : World} {stand : Nat → List w.Relatum}
    (census : w.web.StandingCensus stand) (embodied : w.ArisingEmbodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) : ¬ w.ArisingRecurs :=
  fun arising => Flow.stills balanced dissipative census around fun N =>
    match arising N with
    | ⟨t, x, later, arises⟩ => ⟨t, x, later, .inl (Web.ComesToStand.rises
        ⟨fun standing => arises.1 ((embodied t x arises t).mpr standing),
         (embodied t x arises (t + 1)).mp arises.2⟩)⟩

/-- In `dusk` nothing stands, nothing arises, the flow is still and every step is
enclosed around what stands; ceasing recurs. -/
theorem q3_dusk :
    World.dusk.web.StandingCensus (fun _ => []) ∧ World.dusk.ArisingEmbodied ∧
    World.dusk.Balanced ∧ World.dusk.Dissipative ∧
    (∀ t, World.dusk.flow.AroundStanding (fun _ => []) t) ∧ World.dusk.CeasingRecurs :=
  ⟨fun _ => ⟨trivial, fun c => match c with
     | .inl _ => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => (nomatch no)⟩
     | .inr _ => ⟨fun no => absurd no (Nat.lt_irrefl 0), fun no => (nomatch no)⟩⟩,
   fun t x arises => match x, arises with
     | .inl f, arises => absurd arises (Dusk.nothing_arises t f)
     | .inr _, arises => False.elim arises.2,
   fun _ c => match c with
     | .inl _ => rfl
     | .inr _ => rfl,
   fun _ _ _ _ _ present => (nomatch present),
   fun _ => ⟨[], trivial, fun _ no => (nomatch no), fun _ no => (nomatch no),
     fun _ present => (nomatch present)⟩,
   World.separate.2.1⟩

/-! ## Q4. Decidable equality is not needed for rest from enclosure -/

theorem nn_em (P : Prop) : ¬¬(P ∨ ¬P) :=
  fun h => h (.inr fun p => h (.inl p))

/-- Without decided equality, an enclosed step is not not enclosed around any family. -/
theorem nn_around {F C : Type} {L : Flow F C} {t : Nat} (enclosed : L.Enclosed t) :
    ∀ ds : List C, ¬¬ L.Around ds t
  | [] => fun no => match enclosed with
    | ⟨es, distinct, closed⟩ => no ⟨es, distinct, fun _ mem => (nomatch mem), closed⟩
  | a :: ds => fun no => nn_around enclosed ds fun ⟨es, distinct, sub, closed⟩ =>
    nn_em (a ∈ es) fun decided => match decided with
    | .inl inside => no ⟨es, distinct, fun c mem => match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun d => d ∈ es) same.symm inside
        | .inr mem => sub c mem, closed⟩
    | .inr outside => no ⟨a :: es, ⟨outside, distinct⟩, fun c mem => match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun d => d ∈ a :: es) same.symm (.head es)
        | .inr mem => .tail a (sub c mem),
      fun f present c out => closed f present c fun inside => out (.tail a inside)⟩

theorem nn_aroundStanding {F C : Type} {L : Flow F C} {t : Nat} (enclosed : L.Enclosed t)
    (stand : Nat → List C) : ¬¬ L.AroundStanding stand t :=
  fun no => nn_around enclosed (stand t ++ stand (t + 1)) fun ⟨es, distinct, within, closed⟩ =>
    no ⟨es, distinct, fun c mem => within c (mem_append_left _ mem),
      fun c mem => within c (mem_append_right _ mem), closed⟩

/-- `Flow.stills` with the enclosure only not refuted: the comparisons of totals are
decided, so that is enough. -/
theorem stills_nn {F C : Type} {L : Flow F C} {W : Web F C} {stand : Nat → List C}
    (balances : L.Balances W) (dissipative : L.Dissipative)
    (census : W.StandingCensus stand) {T : Nat}
    (around : ∀ t, T ≤ t → ¬¬ L.AroundStanding stand t) :
    ¬ ∀ N, ∃ t c, N ≤ t ∧ (W.Rises t c ∨ W.Falls t c) :=
  fun changing => falls_finitely (fun t => W.stock (stand t) t) T
    (fun t later => match Nat.decLe (W.stock (stand (t + 1)) (t + 1)) (W.stock (stand t) t) with
      | isTrue le => le
      | isFalse nle => absurd
          (fun a => nle (Flow.standing_never_rises balances dissipative census a))
          (around t later))
    fun N => match changing (N + T) with
    | ⟨t, _, later, changes⟩ => ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
        match Nat.decLt (W.stock (stand (t + 1)) (t + 1)) (W.stock (stand t) t) with
        | isTrue lt => lt
        | isFalse nlt => absurd
            (fun a => nlt (Flow.change_lowers balances dissipative census a changes))
            (around t (Nat.le_trans (Nat.le_add_left T N) later))⟩

/-- `World.rests_enclosed` without `DecidableEq`. -/
theorem rests_enclosed_nn {w : World} (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) : ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  match counted with
  | ⟨alive, census⟩ =>
    have still := stills_nn balanced dissipative (World.standingCensus census embodied)
      fun t later => nn_aroundStanding (enclosed t later) alive
    ⟨fun arising => still fun N => match arising N with
      | ⟨t, x, later, arises⟩ => ⟨t, x, later, .inl (World.rises_of_arises embodied arises)⟩,
     fun ceasing => still fun N => match ceasing N with
      | ⟨t, x, later, ceases⟩ => ⟨t, x, later, .inr (World.falls_of_ceases embodied ceases)⟩⟩

/-- `World.arising_opens` without `DecidableEq`. -/
theorem arising_opens_nn {w : World} (counted : w.Counted) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) (arising : w.ArisingRecurs)
    (T : Nat) : ¬ ∀ t, T ≤ t → w.flow.Enclosed t :=
  fun enclosed => (rests_enclosed_nn counted embodied balanced dissipative enclosed).1 arising

/-! ## Q5. Exposed: what stands is listed and its total stays at one -/

theorem holder_stands_one : ∀ t, Handing.stands (Handing.holder t) t = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Handing.stands_two (Handing.holder t) t).trans (holder_stands_one t)

theorem holder_falls : ∀ t, Handing.stands (Handing.holder t) (t + 1) = 0
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (Handing.stands_two (Handing.holder t) (t + 1)).trans (holder_falls t)

/-- In `exposed` what stands at each step is listed (the holder); the total standing is one
at every step; the holder falls across every step; no step is enclosed around what stands;
the world is not finite. -/
theorem q5_exposed :
    World.exposed.web.StandingCensus (fun t => [Exposed.Relatum.side (Handing.holder t)]) ∧
    (∀ t, World.exposed.web.stock [Exposed.Relatum.side (Handing.holder t)] t = 1) ∧
    (∀ t, World.exposed.web.Falls t (Exposed.Relatum.side (Handing.holder t))) ∧
    (∀ t, ¬ World.exposed.flow.AroundStanding
      (fun t => [Exposed.Relatum.side (Handing.holder t)]) t) ∧
    ¬ World.exposed.Finite :=
  ⟨World.standingCensus Exposed.census (fun _ _ => Iff.rfl),
   fun t => show Handing.stands (Handing.holder t) t + 0 = 1 from holder_stands_one t,
   fun t => show Handing.stands (Handing.holder t) (t + 1) < Handing.stands (Handing.holder t) t from
     Nat.lt_of_lt_of_le (Nat.lt_of_le_of_lt (Nat.le_of_eq (holder_falls t)) Nat.zero_lt_one)
       (Nat.le_of_eq (holder_stands_one t).symm),
   fun t ⟨es, distinct, _, _, closed⟩ => Exposed.open_at t ⟨es, distinct, closed⟩,
   fun ⟨all, _, every⟩ => Exposed.outside all (every _)⟩

/-! ## Q6. Openness does not follow from the eight premises either -/

/-- Mutualism meets all eight premises and every step is enclosed. With `exposed_world`,
the eight premises decide neither enclosure nor openness. -/
theorem q6_mutualism :
    World.mutualism.Premised ∧ (∀ t, World.mutualism.flow.Enclosed t) ∧
    ¬ World.mutualism.ArisingRecurs :=
  ⟨World.mutualism_premised, World.mutualism_finite.enclosed, World.mutualism_world.2.1⟩

/-! ## Q7. Living crosses ceasing, with grazing's activity decided -/

instance grazing_decided : ∀ t x, Decidable (World.grazing.web.active t x)
  | t, .side y => Nat.decLt 0 (Handing.stands y t)
  | _, .pool => isFalse id
  | t, .grazer => Nat.decEq t 0
  | t, .browser => Nat.decEq t 0

/-- Among finite worlds, ceasing recurring or not occurs both with every event living and
with some event not living; the not-living corners are `grazing` and `drawdown`. -/
theorem q7_living_crosses_ceasing :
    (World.handing.Finite ∧ World.handing.CeasingRecurs ∧ World.handing.Living) ∧
    (World.grazing.Finite ∧ World.grazing.CeasingRecurs ∧ ¬ World.grazing.Living) ∧
    (World.mutualism.Finite ∧ ¬ World.mutualism.CeasingRecurs ∧ World.mutualism.Living) ∧
    (World.drawdown.Finite ∧ ¬ World.drawdown.CeasingRecurs ∧ ¬ World.drawdown.Living) :=
  ⟨⟨World.handing_finite, World.handing_world.2.2.1, World.handing_world.2.2.2.1⟩,
   ⟨World.grazing_finite,
    (World.arising_iff_ceasing World.grazing_finite).mp World.grazing_arising,
    World.grazing_world.2.2.1⟩,
   ⟨World.mutualism_finite, World.mutualism_world.2.2.1, World.mutualism_world.2.2.2.1⟩,
   ⟨World.drawdown_finite,
    fun ceasing => World.drawdown_world.2.1
      ((World.arising_iff_ceasing World.drawdown_finite).mpr ceasing),
    World.drawdown_world.2.2.2.1⟩⟩

/-! ## Q8. Under `Dependent`, an undermined dependence belongs to a relatum not active after
the step -/

/-- Where activity needs support, if the condition falls below a dependence's need and the
dependence persists at no lower need, the dependent relatum is not active after the step. -/
theorem q8_undermined_inactive {F C : Type} {W : Web F C} (dependent : W.Dependent)
    {t : Nat} {g : F} {c : C} (below : W.level (t + 1) c < W.need t g c)
    (persists : W.requires (t + 1) g c) (noLess : W.need t g c ≤ W.need (t + 1) g c) :
    ¬ W.active (t + 1) g :=
  fun active => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le below
    (Nat.le_trans noLess (dependent (t + 1) g active c persists)))

/-- In `grazing` the browser, whose dependence the grazer's event undermines, is not active
after that step. -/
theorem q8_grazing : ¬ World.grazing.web.active 1 .browser :=
  q8_undermined_inactive World.grazing_dependent (t := 0) (c := .pool)
    (Nat.lt_succ_self 1) trivial (Nat.le_refl 2)

/-! ## Q9. Without decidability, "a finite world has a census" is excluded middle -/

namespace Choice

def web (Q : Prop) : Web Unit Unit where
  level _ _ := 0
  active _ _ := Q
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

end Choice

/-- One relatum, active exactly when `Q`, with no flow. -/
def choice (Q : Prop) : World :=
  ⟨Unit, Flow.still, Choice.web Q⟩

theorem unit_mem_decides {Q : Prop} : ∀ {l : List Unit}, (Q ↔ () ∈ l) → Q ∨ ¬ Q
  | [], iff => .inr fun q => (nomatch iff.mp q)
  | () :: _, iff => .inl (iff.mpr (.head _))

theorem q9_counted_decides (law : ∀ w : World, w.Finite → w.Counted) (Q : Prop) : Q ∨ ¬ Q :=
  match law (choice Q) ⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩ with
  | ⟨_, census⟩ => unit_mem_decides (Q := Q) ((census 0).2 ())

/-! ## Q10. A balance witness for the map of premises with exchange at every step -/

/-- `Leaking`'s flow on `Spending`'s web: the holder takes its own unit at every step, drawing
on it, and gives nothing. -/
def draining : World :=
  ⟨Bool, World.Leaking.flow, World.Spending.web⟩

instance draining_decided : ∀ t x, Decidable (draining.web.active t x) :=
  fun t x => Nat.decLt 0 (Handing.stands x t)

/-- Every premise but balance, with taking and dissipation non-vacuous: the family of both
sides is closed and taken from at every step. -/
theorem q10_draining :
    draining.MeetsAllBut World.Balanced ∧
    ∀ t, World.Leaking.flow.ClosedAt [true, false] t ∧
      0 < total [true, false] (World.Leaking.flow.take t (Handing.holder t)) :=
  ⟨.of (fun _ => Handing.dependent) (fun ne => absurd rfl ne)
     (fun _ _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0))
     (fun _ => World.Spending.taking) (fun _ => World.leaking_world.2.2.1)
     (fun _ _ _ => Iff.rfl)
     (fun _ => World.Finite.counted (w := draining) ⟨[true, false], Handing.distinct, Handing.every⟩)
     (fun _ => ⟨0, fun _ _ _ _ descends _ => absurd descends.2.1 (Nat.lt_irrefl 0)⟩)
     World.leaking_world.2.2.2.2.1,
   World.leaking_world.2.2.2.2.2⟩

end Review10
```

## Appendix B. Probe axiom audit

`Review10Audit.lean` (sha256 `69902f8c73454138188e179fea3b19b38a097bf627e7d013d7f3f15164012f6f`) enumerates every constant the probe module adds, including auxiliary and generated ones, with `Lean.collectAxioms`, and prints the axioms of the thirteen main probes:

```lean
import Lean
import Review10
open Lean Elab Command
#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review10 | throwError "no module"
  let mut count := 0
  let mut withAx := 0
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then
        withAx := withAx + 1
        logInfo m!"AXIOMS {n} {axioms.toList}"
  logInfo m!"CONSTANTS Review10 {count} WITHAXIOMS {withAx}"
#print axioms Review10.q1_kindling
#print axioms Review10.q2_ember
#print axioms Review10.q3_rests_standing
#print axioms Review10.q3_dusk
#print axioms Review10.rests_enclosed_nn
#print axioms Review10.arising_opens_nn
#print axioms Review10.q5_exposed
#print axioms Review10.q6_mutualism
#print axioms Review10.q7_living_crosses_ceasing
#print axioms Review10.q8_undermined_inactive
#print axioms Review10.q8_grazing
#print axioms Review10.q9_counted_decides
#print axioms Review10.q10_draining
```

Output:

```text
CONSTANTS Review10 95 WITHAXIOMS 0
'Review10.q1_kindling' does not depend on any axioms
'Review10.q2_ember' does not depend on any axioms
'Review10.q3_rests_standing' does not depend on any axioms
'Review10.q3_dusk' does not depend on any axioms
'Review10.rests_enclosed_nn' does not depend on any axioms
'Review10.arising_opens_nn' does not depend on any axioms
'Review10.q5_exposed' does not depend on any axioms
'Review10.q6_mutualism' does not depend on any axioms
'Review10.q7_living_crosses_ceasing' does not depend on any axioms
'Review10.q8_undermined_inactive' does not depend on any axioms
'Review10.q8_grazing' does not depend on any axioms
'Review10.q9_counted_decides' does not depend on any axioms
'Review10.q10_draining' does not depend on any axioms
```

`Review10Print.lean` (sha256 `ce8fd68c71293b447b1bd0bbde488bf0c1e2493045643b5d4372454a1ca09bf6`) runs `#print axioms` on each of the 36 source declarations (25 theorems, 8 definitions, 3 instances). All 36 report "does not depend on any axioms":

`kside`, `kfuel`, `side_mem_sides`, `unburnt_zero`, `fuel_stands`, `kindling_census`, `kindling_around`, `q1_kindling`, `Ember.web`, `ember`, `decEqRelatum`, `instDecidableEqRelatumEmber`, `q2_ember`, `q3_rests_standing`, `q3_dusk`, `nn_em`, `nn_around`, `nn_aroundStanding`, `stills_nn`, `rests_enclosed_nn`, `arising_opens_nn`, `holder_stands_one`, `holder_falls`, `q5_exposed`, `q6_mutualism`, `grazing_decided`, `q7_living_crosses_ceasing`, `q8_undermined_inactive`, `q8_grazing`, `Choice.web`, `choice`, `unit_mem_decides`, `q9_counted_decides`, `draining`, `draining_decided`, `q10_draining`.

## Appendix C. Core audit

`CoreAudit.lean` (sha256 `ffa18c5af0db67cdf48b4aac147afb636bd396d176908eba473b2ec4aab97fe9`): `import Becoming` and one `#print axioms` line for each of the 1732 source declarations the receipt lists for the 29 closure modules. All 1732 report "does not depend on any axioms".

`EnvAudit.lean` (sha256 `420f85b14528ce054087131a212c1c881294b396992b9f6a221a294a26bc77f0`, the checker's environment audit instantiated for the closure): constants per module, each equal to the receipt's `core_closure_constants`.

| Module | Constants | Module | Constants |
|---|---|---|---|
| `GenerativeCore` | 54 | `Becoming.Identity` | 487 |
| `Becoming.Frame` | 61 | `Becoming.Wholes` | 147 |
| `InquirySufficiency` | 107 | `Becoming.Dissipation` | 318 |
| `Becoming.Inquiry` | 15 | `Becoming.Roles` | 463 |
| `RelationalRenewal` | 134 | `Becoming.Reserve` | 144 |
| `Becoming.Renewal` | 58 | `Becoming.Evolution` | 152 |
| `Becoming.Dependence` | 475 | `Becoming.Space` | 238 |
| `Becoming.Return` | 84 | `Becoming.Premises` | 245 |
| `Becoming.Horizon` | 43 | `Becoming.Openness` | 79 |
| `Becoming.Joint` | 203 | `Becoming.Metaethics` | 226 |
| `Becoming.Substitution` | 40 | `Becoming.Ranking` | 170 |
| `Becoming.Generation` | 216 | `Becoming.Correspondence` | 159 |
| `Becoming.Flow` | 225 | `Becoming.Descent` | 117 |
| `Becoming.Change` | 96 | `Becoming` | 0 |
| `Becoming.Population` | 138 |  |  |
| total | 4894 | | |

The 34 constants with an axiom, all generated `injEq` lemmas depending only on `propext`, equal to the receipt's `generated_axiom_dependencies` (the four added since the ninth review are marked \*):

`Generative.Process.mk.injEq`, `Becoming.Run.mk.injEq`, `Becoming.Frame.mk.injEq`, `Generative.InquirySufficiency.Policy.respond.injEq`, `Generative.InquirySufficiency.Policy.inquire.injEq`, `RelationalRenewal.Unfolding.mk.injEq`, `RelationalRenewal.Law.mk.injEq`, `Becoming.Conditions.mk.injEq`, `Becoming.Crossing.State.mk.injEq`, `Becoming.Crossing.Move.fall.injEq`, `Becoming.Dependence.mk.injEq`, `Becoming.Pinned.State.mk.injEq`, `Becoming.Web.mk.injEq`, `Becoming.Pool.Draw.mk.injEq`, `Becoming.Pool.State.mk.injEq`, `Becoming.Shock.State.mk.injEq`, `Becoming.Shock.Move.calm.injEq`, `Becoming.Flow.mk.injEq`, `Becoming.Reidentify.mk.injEq`, `Becoming.Confluence.Formation.new.injEq`, `Becoming.Generations.Formation.member.injEq`, `Becoming.Frontier.Formation.grower.injEq`, `Becoming.Frontier.Condition.fuel.injEq`, `Becoming.Kindling.Relatum.side.injEq`, `Becoming.Kindling.Relatum.fuel.injEq`, `Becoming.SprayHanding.Relatum.aux.injEq`, `Becoming.SprayHanding.Relatum.side.injEq`, `Becoming.World.Grazing.Relatum.side.injEq` \*, `Becoming.World.mk.injEq`, `Becoming.World.Scatter.Relatum.ground.injEq` \*, `Becoming.Exposed.Relatum.side.injEq` \*, `Becoming.Exposed.Relatum.ground.injEq` \*, `Becoming.Valuation.mk.injEq`, `Becoming.Web.Condition.mk.injEq`.
