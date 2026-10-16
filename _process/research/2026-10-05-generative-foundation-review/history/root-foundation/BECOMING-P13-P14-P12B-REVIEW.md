# P13、P14 与 P12b 的独立审查 / Independent review of P13, P14 and P12b

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写这三个阶段。对象：`main` 的 `3828bcf8`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of the three phases. Object: `main` at `3828bcf8`.

**摘要（中文）。** 三个阶段的全部 Lean 声明都在仓库之外从前导重新编译，核心闭包 21 个模块的公理报告为空。回执 `20261009T060305.410034Z`（559 项定理／948 项声明审计，核心闭包 21 个模块）、16 份变更记录的 185 个引用哈希与 50 个证明绑定都对，281 个别名中只有未重建的外围的五个没有解析。数学被接受，没有发现数学错误。共审计 1029 条声明，全部不依赖任何公理：898 条核心声明（其中 Dissipation 38、Roles 71、Correspondence 50、Flow 94、Population 45、Identity 122），50 条桥接声明，81 条探针声明（其中 57 项定理）。问题在前提的陈述、散文与对应之间，共十一项（J1–J11）。

- **P13（耗散）。** `runs_down`、`takers_within`、`taking_ceases`、`opens`、`finite_ceases` 都对，`Frontier` 非空地满足耗散。问题如下。
  - **有限支撑（J1）。** `Dissipative` 只约束在某步封闭的有限家族。某个形成在一步中与无穷多个条件交换时，没有家族封闭，耗散就是空的。这时补充者可以什么都不取而给予（`Spray`）。所以“给予总使补充者所取的条件付出多于所给”、“前提要求补充者的代价表示为它所取的条件”在定义上不成立，需要一个有限支撑的前提。
  - **任何持续的取用（J2）。** 定理只用复现的取用。一个恒定的取用者，没有生起也不更多，同样需要越出每个有限家族（`Lone`）。把“整体”读作“不断的更多”的形式内容，比定理更窄；这是 I3 的同一模式。
  - **见证（J3）。** `Frontier` 的生长者不依存于任何东西，`opens_of_arising` 没有见证，此前的流不满足耗散也没有定理。`Rooted` 与 `core_flows_not_dissipative` 补上。
- **P14（角色）。** `roles_*` 对所列读法逐项成立；`coextinct`、`ends_when_consumed`、`Mutualism`、`Predation`、`Brood` 与对应一节都对。H14 得到回答，超出它要求的界限句。问题如下。
  - **同一对应（J4）。** 一类读法的内容在于“条件 x 就是形成 x”，这由共同的索引给出。`Web X X` 本身就是 `F = C` 的两类网，包含是双向的。把条件一侧按对合重新标号，检查过的两类读法都不变，而体现与承担自身改变（`relabel`）。所以“恰是”“所以没有引入独立的本体”“省略的正是体现”说得过强。这与 I7 是同一模式。
  - **估值看不见体现（J5）。** `Mutualism.apart` 中蜜蜂与花都体现、彼此依存并汲取，两种估值都不关联它们。体现本身不进入估值，只有自身依存的回路进入。
  - **终结（J6）。** `ending_breaks` 读的是终结之步的汲取，不问是什么终结了它。花因自身的取用而凋，从不取用的蜜蜂在那一步的事件仍不是 living，花自己的最后一个事件也不是（`Wilting`）。“以汲取终结另一个生命”“它的吃断裂兔的依存”读出了定理没有的因果。交给 Ren 的选择是真的，但它的范围（旁观者、自然死亡、生命自己的最后事件）没有说明。
  - **生由生（J7）。** `arises_given` 的给予者只是一个活跃的关系项。不体现、不承担自身、不依存于任何东西的太阳可以是唯一的给予者（`SunSeed`）。“一个生命的生起由另一个生命的活动给出”强于定理。
  - **覆盖与界限（J8）。** “已陈述的读法都不变”应为“列出的”。“一类读法不保持 Acting、Taking 与 Dissipative”照字面是错的：探针证明它们保持（Dissipative 从两类到一类）。
- **P12b。** I1–I12 全部处理，探针移入核心，两向连续定理与 `Dormancy`、`TideFlip`、`Layered`、活着的继承者都对。`Flow.More.unceasingFrom` 不是空的：在含合并的延续下也适用（`Merge`），可判定性由普查与可判定的延续给出（`continuesDec`）。问题如下。
  - **分裂不是精确的界限（J9）。** `NoSplit` 是充分条件，不是必要条件：循环中形成 0 在第一步延续为两个，生起照样不息（`split_unceasing`）。“分裂恰是界限”沿用了第五次审查 §4 第 6 项的措辞，那里已经说得过强。
  - **章节省去前提（J10）。** “在每种没有分裂的延续下更多迫使生起”省去普查、`present` 不重复与 Taking（`dormant_no_census`）；§8 的“生由生”省去平衡与 Acting。这是 I1 的同一模式。
  - **记账（J11）。** §8 审查一行过期；模块数口径不一；一处“证明它”、一处“耗尽”；“代价／付出／cost”仍属支付一族；两份记录的审查时间未刷新。
- **非二元方法、Ren 的原话与读法选择。** 没有替 Ren 选择生生、living、接续或终结的读法；Ren 的原话引用准确；AI 读法都有标注。问题在 J4（以共同的索引给出的同一被当作结果）、J6 与 J7（标注的读法强于定理），以及 J1 的注释。

**Summary (English).** Every Lean declaration of the three phases recompiles from the prelude outside the repository, and the 21 modules of the core closure have empty axiom reports. The receipt `20261009T060305.410034Z` (559 theorems, 948 declaration audits, closure of 21), the 185 reference hashes and 50 proof bindings of the 16 changed records are correct, and of their 281 aliases only the five in the unrebuilt periphery do not resolve. The mathematics is accepted; no mathematical error was found. 1029 declarations were audited and none depends on any axiom: 898 core declarations (Dissipation 38, Roles 71, Correspondence 50, Flow 94, Population 45, Identity 122), 50 bridge declarations and 81 probe declarations, 57 of them theorems. The eleven findings (J1–J11) concern premises, prose and correspondence.

- **P13.** The lemmas and `Dissipative.opens` hold, and `Frontier` meets dissipation non-vacuously.
  - `Dissipative` is vacuous at a step where some formation exchanges with infinitely many conditions; a renewer then gives while taking nothing (`Spray`). The gloss that dissipation makes giving cost the renewer needs a finite-support premise (J1).
  - The theorem uses only recurring uptake: a single steady consumer needs the frontier too (`Lone`). Reading 整体 as the content of "不断的更多" is narrower than the theorem, the I3 pattern again (J2).
  - `Frontier`'s growers depend on nothing, `opens_of_arising` has no witness, and that the earlier flows fail dissipation is not a theorem; `Rooted` and `core_flows_not_dissipative` supply both (J3).
- **P14.** Each listed `roles_*` reading holds, and coextinction, `Mutualism`, `Predation`, `Brood` and the new Correspondence section are correct. H14 is answered, beyond its requested boundary sentence.
  - The one-kind reading's content is the identification of condition `x` with formation `x`, supplied by the shared index. `Web X X` is itself a two-kind web; relabelling the condition side keeps every checked two-kind reading and changes `Embodied` and `SelfBearing`. "Is exactly", "introduces no independent ontology" and "omits exactly embodiment" overstate; this is the I7 pattern again (J4).
  - Embodiment does not enter either valuation: in `Mutualism.apart` both relata are embodied and unrelated (J5).
  - `ending_breaks` reads drawing at the step of an ending, whatever causes it: a bee that takes nothing is not living when the flower wilts by its own taking, nor is the flower's own last event (`Wilting`). "Ending another life by drawing on it" reads in causation. The choice left to Ren is real, but its scope is undisclosed (J6).
  - `arises_given` names an active giver, not a life: a sun that is not embodied, bears on nothing and depends on nothing can be the only giver (`SunSeed`) (J7).
  - "Every stated reading" should be "every listed reading", and the Chinese boundary "does not keep Acting, Taking and Dissipative" is false: the probes keep them (J8).
- **P12b.** I1–I12 are all addressed. The two-way theorems, `Dormancy`, `TideFlip`, `Layered` and the living heir are correct. `Flow.More.unceasingFrom` is non-vacuous, including under merges (`Merge`), and its decidability premise follows from a census and a decidable continuation (`continuesDec`).
  - `NoSplit` is sufficient, not necessary: a single split leaves generation unceasing (`split_unceasing`). "Splits are exactly the boundary" follows the fifth review's own overstated §4 wording (J9).
  - The chapter states "more forces arising under every continuation without splits" without census, distinctness and `Taking` (`dormant_no_census`), and "life from life" without balance and `Acting` (J10).
  - Bookkeeping: a stale review row, inconsistent module counts, "proves it", "耗尽", the "cost" family of words, two unrefreshed stamps (J11).
- **Ren.** No reading of 生生, `living`, succession or ending is chosen for Ren, Ren's words are quoted exactly, and the AI readings are labelled. J4, J6 and J7 are where a supplied identification or a labelled reading says more than the Lean.

## 0. Scope, materials and method

**Object.** `main` at `3828bcf8829f9b0fe8eb6560190a4c07324a7e3c`:

- **P13 (`23770e91`).** [Becoming.Dissipation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean) (`ClosedAt`, `DissipatesOn`, `Dissipative`, `runs_down`, `takers_within`, `taking_ceases`, `opens`, `finite_ceases`, `More.opens`, `opens_of_arising`, `Frontier`); study §17 and its English paragraph; the record [no-finite-part-bears-taking](../../../../theories/becoming/results/records/no-finite-part-bears-taking.md); the chapter sentences on dissipation (§2 line 199, §8 line 429, §9 line 460).
- **P14 (`a739e232`).** [Becoming.Roles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean); the new section of [Becoming.Correspondence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean) (line 522 to the end, with its module-doc paragraph); study §18 and its English paragraph; the record [life-as-condition-of-life](../../../../theories/becoming/results/records/life-as-condition-of-life.md); chapter §1 line 132, the summary bullet line 143, §2 lines 203–205, §8 line 429, §9 lines 461 and 464, glossary line 508.
- **P12b (`3828bcf8`).** The corrections answering I1–I12 of [BECOMING-P11B-P12-REVIEW](BECOMING-P11B-P12-REVIEW.md) in `Flow`, `Population` and `Identity`; study §19 and its English paragraph; the records identity-across-steps, more-needs-renewers, unceasing-generation-needs-renewal, becoming-stepwise-reading and becoming-renewal-reading; chapter lines 131, 142, 195–199, 427–431.

**Isolation.** The snapshot is a `git archive 3828bcf8` in the reviewer's scratch directory. Nothing in the live repository or its `.git` was modified, no `make` target or repository checker was run against it, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`.

**Materials** (sha256 prefixes of the snapshot files):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `b10705896b57a97e` |
| chapter `THE-THEORY-OF-BECOMING.md` | `81e893a946e3c536` |
| previous review `BECOMING-P11B-P12-REVIEW.md` | `84766b7a6f16b582` |
| `NONDUAL-METHOD.md` / `AGENTS.md` | `8c48b03a167a8909` / `da432369737e9a1f` |
| receipt `becoming-verification.json` (run `20261009T060305.410034Z`) / `check_becoming.py` | `4150009b948fc538` / `8943dc4021c5cdbd` |
| `Becoming/Dissipation` / `Roles` / `Correspondence` | `7e34f997ca4f97be` / `46a88434b73a9c0f` / `7c0f50d676eea472` |
| `Becoming/Flow` / `Population` / `Identity` | `3f2bfedaa2198ed9` / `27a40fbc515a2311` / `0ee05c6ed4336b25` |
| records no-finite-part-bears-taking / life-as-condition-of-life / identity-across-steps | `28711fb3bf95ccac` / `767ad4e8c43e719f` / `d2d607af92329bd6` |
| records more-needs-renewers / unceasing-generation-needs-renewal | `78ae72067647e461` / `538ba929bf5b1004` |
| records condition-correspondence-discipline / becoming-renewal-reading / becoming-stepwise-reading | `f88cc62c2b00e239` / `5f0920e3c3744058` / `193896130b073985` |

**Read in full:** AGENTS.md; the nondual method; the previous review; study §17–§19 and the English P13, P14 and P12b paragraphs; `Dissipation` and `Roles` in full; the new Correspondence section; the P12b changes to `Flow`, `Population` and `Identity` (diffs `e5430db5..3828bcf8`); the seven record JSONs whose claims, hypotheses or limitations changed; the chapter lines listed above.

**Ren's words read**, for provenance: [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) (`740126fcca587edb`), whose line 12 the study quotes exactly; [recipient, money, pay](../../../../sources/15-codex-theory-conversations/2026-10-06-foundational-vocabulary-correction.md) (`222d407ab761a945`).

**No external literature was read.** Wilting, pollination and dormancy are kinds of cases, not evidence.

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`), `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order.

- **Core.** `GenerativeCore` (with `import Std` removed, as the checker does), `InquirySufficiency`, `RelationalRenewal`, `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Population, Identity, Dissipation, Roles, Metaethics, Ranking, Correspondence}` and `Becoming`: all 21 modules exit 0 from the prelude.
- **Bridge.** In a second directory, the 12 periphery modules that `Becoming.Bridge` imports and the bridge itself exit 0.

The checks:

- **Receipt.** Status `passed`, Lean 4.29.1 `f72c35b3`, `core_compiles_from_prelude: true`, `core_closure` of 21 modules; all 34 `source_sha256` entries equal the snapshot files.
- **Counts.** Theorems per module: Frame 11, Inquiry 6, Renewal 6, Dependence 53, Return 29, Horizon 14, Joint 21, Substitution 7, Generation 30, Flow 60, Population 33, Identity 77, Dissipation 28, Roles 54, Metaethics 35, Ranking 27, Correspondence 34, Bridge 34: 559. The 17 spine modules have 898 declarations, and with Bridge's 50 that makes 948. The chapter's §9 table agrees.
- **Records.** The 16 records changed in `e5430db5..3828bcf8`: all 185 `references` hashes equal the snapshot files, and all 50 proof bindings' `sha256_pointer`, resolved in their receipts, equal the bound sources. The `reviewed_at_utc` stamps precede their commits (05:12:53Z before P13 at 05:15:10Z, 05:45:34Z before P14 at 05:47:21Z, 06:09:26Z before P12b at 06:16:16Z); two are not refreshed after P12b's wording changes (J11).
- **Names.** `Aliases.lean` (`d1002cd0f4862319…`) runs `#check @` on all 281 aliases of the 16 records: 250 resolve in the core, 26 more through `Becoming.Bridge` (`AliasesBridge.lean`, `c24d0d738a937382…`), and the remaining five are the `CorrectionInquiry` theorems of the unrebuilt Mathlib periphery reported before. Of 778 qualified declaration names in the `references`, 767 resolve; the other 11 are the same periphery declarations of becoming-spine-instances.
- **Axioms.** `CoreAudit.lean` (`47b261ab8f6f8167…`, 898 lines generated from the receipt) and `BridgeAudit.lean` (`d82e44cb81b1d2e5…`, 50 lines) print the axioms of every spine and bridge declaration; `ProbeAudit.lean` (`cb6f6c9831537f6a…`) prints those of all 81 probe declarations. All 1029 report "does not depend on any axioms".

**Probes.** Three files import the unchanged `Becoming` and compile with exit 0 and no warnings:

| File | sha256 prefix | Theorems | Defs / inductives / instances |
|---|---|---|---|
| `P13Probes.lean` | `793c295a2a552f71` | 23 | 8 |
| `P14Probes.lean` | `37411358daaddbb1` | 27 | 11 |
| `P12bProbes.lean` | `a40c8cd0600fe226` | 7 | 5 |

The probes are term-mode only: no tactic, no `simp`, `omega` or `decide`. In Lean 4.29.1, `Nat.succ_ne_zero` and, in one draft probe, a `nomatch` on an equation between numerals reported `propext`; the probes use `Nat.lt_irrefl` and `Nat.noConfusion` instead. The probes are minimal models satisfying the published definitions unchanged. Following the nondual method, they show what the definitions admit, not what actual systems do; a probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels.** *error*: a definition does not match its stated meaning, or a mathematical claim is false. *overclaim*: the prose is stronger than the Lean, including a premise left out. *missing counterexample*: a relevant witness, including a positive joint witness, is absent. *presentation*: wording, provenance or bookkeeping. No finding is an *error*.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P13: is `Dissipative` the premise the prose says? | **It is per-formation dissipation on closed finite families, as defined; it is not "giving always costs the renewer".** On every finite closed family each formation gives less than it takes when it takes. Where no finite family is closed, it says nothing (`Spray`). It excludes `Garden`, `Cycle`, `Pulse`, `Steady`, `Repeated` and `Bloom`, as the prose says of `Garden`, `Bloom` and `Cycle` (`core_flows_not_dissipative`). `Recycle` has no flow; its premise is the web-level `dissipation_ceases` of P11b, and §17 relates the two correctly. | J1, J3 |
| 2. P13: does "no finite part bears continued taking" overreach? | **The theorem is correct and "finite part" is disclosed as a finite family of conditions.** Its conclusion, open at arbitrarily late steps, can be met by exchange unrelated to the family (`Spray`'s sink). "Continued taking" includes a steady consumer (`Lone`), so the 整体 reading is narrower than the theorem. "被耗散的家族耗尽" says more than `taking_ceases`. | J1, J2, J11 |
| 3. P13: is `Frontier` non-degenerate? | **For dissipation, yes**: at each step `{pool, fuel t}` is closed, so `Dissipative` binds. **Its growers depend on nothing** (`requires := False`); `Rooted` gives the dependent version with census, `Unceasing` and `opens_of_arising`. | J3 |
| 4. P14: does it answer H14? | **Yes.** H14 found that nothing links a formation's activity to its level as a condition; `Embodied` is that link, and `coextinct` is a real consequence. The link and the identification beneath it are supplied, which is the correct status, but the prose presents them as results. | J4, J5 |
| 5. P14: is "two kinds = one kind with no formation as condition" exact? | **The embedding is exact for the listed readings. "恰是 / is / exactly embodiment / 没有引入独立的本体" overstate.** `Web X X` is a two-kind web with `F = C`; what the one-kind reading adds is the identification of condition `x` with formation `x`. Relabelling keeps the checked two-kind readings and changes `Embodied` and `SelfBearing`. | J4 |
| 6. P14: do the `roles_*` equivalences cover the readings claimed? | **Each item of the module doc's list has a theorem.** "已陈述的读法 / every stated reading" overreaches. The boundary "不保持 Acting、Taking 与 Dissipative" is false: `roles_acting`, `roles_taking`, `roles_census`, `roles_distinct` and `roles_dissipative` hold. | J8 |
| 7. P14: do `Embodied` and `SelfBearing` make "condition of itself" non-vacuous? | **Yes**, with witnesses (`Brood`, `Mutualism`, `Predation`). Under `Dependent` and `Embodied`, a self-dependence is met exactly while the relatum is active (`selfBearing_met_iff`): it adds no information beyond activity, and its effect is to recode an ending as a broken dependence. | J6 |
| 8. P14: do `ending_breaks` and `arises_given` say what the prose says? | **No.** `ending_breaks` is co-occurrence with an ending of any cause (`Wilting`). `arises_given` names an active giver, not a life (`SunSeed`). | J6, J7 |
| 9. P14: do the valuation parts choose a reading for Ren? | **No.** Whether drawing at an ending counts against living is left to Ren. The scope of that choice is not shown to Ren: bystanders, natural deaths and the life's own last event. | J6 |
| 10. P12b: are I1–I12 resolved? | **All twelve are addressed; see the table below.** Two patterns recur in the new phases: an omitted premise (I1 → J10) and a supplied correspondence presented as a result (I7 → J4). | J9, J10 |
| 11. P12b: is `Flow.More.unceasingFrom` non-vacuous? | **Yes.** It applies to the identity continuation (`Garden.counted`), every re-identification (`continuation_reidentify`) and a continuation with merges (`Merge.unceasing`). Rebuttal 3 is right: under a census, a decidable continuation makes `Continues` decidable (`continuesDec`, `unceasingFrom_of_decidable`). | — |
| 12. P12b: is `NoSplit` the exact boundary? | **No. It is sufficient, not necessary** (`split_unceasing`). Merges are allowed and `Budding` defeats it, as claimed. | J9 |
| 13. P12b: the two-way continuity theorems | **Correct and correctly glossed.** The back direction alone excludes joins at a single step (`no_join`). | — |
| 14. P12b: is `Dormancy` a genuine witness? | **Yes.** No formation is active or depends at two successive steps; the late formation depends on nothing, and the class changes because it draws on the pool whose dependence the needy formation loses. | — |
| 15. P12b: is `Layered` described as an omission? | **Yes**, in the module doc, study §19, the record's counterexample and the chapter. | — |
| 16. Nondual method; Ren's words; vocabulary | **No reading is chosen for Ren, Ren's words are exact, and AI readings are labelled.** J4 repeats the I7 pattern; J6 and J7 are labelled readings stronger than the Lean. No payment, ledger, supply or giver word is new; "代价 / 付出 / cost" remains. | J4, J6, J7, J11 |
| 17. Records, receipt and counts | **Correct** (559 / 948, run `20261009T060305.410034Z`, 21 modules), with bookkeeping in J11. | J11 |

**Status of I1–I12.**

| Item | Status | Evidence |
|---|---|---|
| I1 | closed | `Repeated.more_without_arising` in `Population`; chapter §1, §2 and §8 state distinctness. The new `unceasingFrom` sentences omit it again (J10). |
| I2 | closed | `Garden.census`, `Garden.counted`, `Cycle.census`, `Cycle.counted`, `Garden.unceasing_reidentified`. |
| I3 | closed | `uptake_needs_replenishment`, `Steady.steady`, rebuttal 2 and the chapter corrected. J2 is the same pattern in P13. |
| I4 | closed | (a) left to Ren; (b) `MetAbove` doc; (c) the half of `Taking` used; (d) "giver" renamed; (e) stamp refreshed. "Cost" wording remains (J11). |
| I5 | closed | `Reidentify.back` and the six two-way theorems; `Lineage.one_way`, `Succession.one_way`. |
| I6 | closed | `Dormancy.keeps_both`, `Dormancy.classes`; 接续 widened. |
| I7 | closed | "标签不承载任何东西"; the pattern of names disclosed as a correspondence premise. |
| I8 | closed | `TideFlip.naming_meets_premises`; the P10 paragraph corrected. |
| I9 | closed, with an overclaim | `Web.Continues`, `NoSplit`, `Flow.More.unceasingFrom`, `continuation_reidentify`, `Budding`. "Exact boundary" overstates (J9). |
| I10 | closed | `Layered.both`; two levels, part–whole omitted; "落在维持与更新上" removed. |
| I11 | closed | `Succession`'s heir is active and supported at step two. |
| I12 | closed | limitation sentences in four records. |

## 2. Findings

### J1. overclaim (undisclosed premise): `Dissipative` binds only where a finite family is closed

**Location.**

- Dissipation.lean:17–18: "Giving then always costs the conditions the renewer takes from more than it gives."
- Flow.lean:47–51: "needs dissipation: every giving costing the renewer's conditions more than it gives".
- Chapter §2 (line 199): "在耗散之下，即给予总使补充者所取的条件付出多于所给时".
- Study §17 rebuttal 1 (line 988): "`Dissipative` 太强，排除了任何“免费”的补充者。对，这正是前提的内容".
- Record no-finite-part-bears-taking, hypothesis 2: "It requires the renewer's cost to be represented as conditions it takes from"; Roles.lean:51–52 and §18 rebuttal 5: "耗散之下给予须付出所取的条件".

**What the Lean says.** `Dissipative := ∀ cs t, Distinct cs → ClosedAt cs t → DissipatesOn cs t`. If at step `t` some formation taking part exchanges with infinitely many conditions, no finite family is closed at `t`, and `Dissipative` says nothing about `t`.

**Evidence.** `Spray.free_renewer`. A sink takes one unit from and gives one unit to every auxiliary condition `n + 1`; a renewer gives the pool one unit and takes nothing; a consumer takes one unit from the pool. The flow balances, only active formations give and take, only from what they draw on, activity needs support, and `Dissipative` holds (`Spray.dissipative`, from `fresh`: no finite list contains every positive index). At every step the renewer gives and takes nothing.

**Why it matters.** The theorems are untouched: `Spray` meets their conclusions, since every family is open. But the gloss that rebuttal 1 calls "the content of the premise" is false of the definition. The conclusion "some formation taking part exchanges beyond the family" is then met by the sink's exchange, which nets zero and never touches the pool; the pool is sustained by a free renewer.

**Correction.** Add a finite-support premise: at each step some finite family without repetition is closed (equivalently, since `present` is a list, each formation taking part exchanges with finitely many conditions). Over that family `DissipatesOn` gives each formation's whole giving and taking, so a formation that gives takes more than it gives; state this as a theorem (not formalized here). Until then, restrict the glosses: zh "在耗散之下，在有封闭的有限家族的步上，给予须以更多的取用为条件"; and add `Spray` to the record's counterexamples.

### J2. overclaim (AI reading): the requirement comes from any continued taking, not from "more"

**Location.** Study §17 "对生生（作者的读法）" (line 984): "在耗散之下，不断的更多不能由任何有限的部分承担……作者把这读作原话中“整体”的一种形式内容". Chapter §2 (line 199): "作者把它读作“生生”的一种结构：……在耗散之下，它由越出每个有限部分的展开承担".

**What the Lean says.** `Dissipative.opens` needs only `∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t`. `More.opens` and `opens_of_arising` are two cases.

**Evidence.** `Lone.persistence_needs_frontier`. One eater takes one unit from the pool at every step; a sun burns the `t`th fuel (two units) and gives the pool one. The flow balances and is dissipative; nothing arises; generation is not more; every finite family without repetition containing the pool is open at arbitrarily late steps.

**Why it matters.** This is the I3 pattern again: the requirement is carried by recurring uptake, whether from generation, more or maintenance. Under dissipation, keeping one consumer alive already reaches beyond every finite family. Reading 整体 as the formal content of "不断的更多" picks out a case, not the content.

**Correction.** zh: "在耗散之下，复现的取用，无论来自不止的更多、生成还是维持，都不能由任何有限的条件家族独自承担（`Lone`）；作者把这读作原话中“整体”的一种形式内容". Move `Lone` into `Dissipation`.

### J3. missing counterexample (witness strength): `Frontier` depends on nothing; `opens_of_arising` has no witness

**Location.** `Frontier` (Dissipation.lean:228–); record no-finite-part-bears-taking counterexample 3; study §17 table and rebuttal 1.

**What the Lean says.** `Frontier.web` has `requires _ _ _ := False` and the pool at level 0, so `Dependent` holds vacuously and the growers live on nothing. No census is given, and `opens_of_arising` is never instantiated. That `Garden` and `Bloom` (rebuttal 1) and `Cycle` (the record) fail `Dissipative` is stated, not proved.

**Evidence.**

- `Rooted.rooted`: `Frontier.flow` on a web whose pool holds one unit and whose growers depend on it at need one while active. Balance, `Acting`, `Taking`, `Dependent`, a census, `Dissipative`, `More` and `Unceasing` hold together, and the pool's families are open by `opens_of_arising`.
- `core_flows_not_dissipative`: `Garden`, `Cycle`, `Pulse`, `Steady`, `Repeated` and `Bloom` all fail `Dissipative`, by `finite_ceases` on their single condition.

**Correction.** Move both into the core; cite `Rooted` as the joint witness in the record and §17.

### J4. overclaim (nondual method): which condition is which formation is supplied by the shared index

**Location.**

- Chapter §1 (line 132): "两类的表示恰是没有形成作为条件的一类读法"; summary bullet (line 143): "the two-kind representation is the one-kind reading in which no formation is a condition"; §9 (line 461) "两类读法是其特例"; glossary (line 508).
- Study §18 "两类是一类的特例" (line 1044): "所以两类的表示没有引入独立的本体……它省略的正是体现"; rebuttal 3 (line 1056): "两类读法恰是没有体现的一类读法".
- Record life-as-condition-of-life, counterexample 2: "what the two-kind representation omits is exactly embodiment".

**What the Lean says.** `Web.roles` embeds `Web F C` into `Web (F ⊕ C) (F ⊕ C)` and keeps the listed readings. Conversely, a one-kind `Web X X` is already a two-kind `Web F C` with `F = C = X`. What the one-kind reading adds is that condition `x` and formation `x` are one relatum, and that is given by the shared index type. `Embodied` (`active t x ↔ 0 < level t x`) and `SelfBearing` (`requires t x x`) read exactly that identification.

**Evidence.** `relabel W π` renames the condition side by `π`.

- For an involution `π`: `relabel_dependent`, `relabel_undermining` and `relabel_interaction_connected`. `Dependent`, undermining, the living events and the connection of the interaction valuation are unchanged.
- `apart_relabelled`: `Mutualism.apart`, where neither relatum bears on itself, relabelled by `other` is a web in which both bear on themselves, each drawing only on "itself".
- `Wilting.relabelled_not_embodied`: the embodied flower, relabelled by `swap`, is not embodied.

**Why it matters.** As in P12, labels carry nothing and the pattern of identification carries the content. Here the pattern is formation–condition identity rather than identity across steps, and it is supplied by the representation. Whether the bee draws on the flower or on itself is fixed by nothing the two-kind readings see. P14's achievement stands: the identification is now expressible, which H14 asked for. But "恰是", "所以没有引入独立的本体" and "省略的正是体现" present a supplied correspondence as a result, the pattern I7 corrected.

**Correction.** zh: "两类的读法可以嵌入一类读法（其中没有形成作为条件），保持列出的读法。一类读法另需一个对应：哪个条件就是哪个形成；它由共同的索引给出，是表示的前提，两类读法检查不到它（`relabel`）。体现与承担自身是在这一对应下的读法。" Replace "省略的正是体现" with "省略的是形成与条件的同一对应". Add the identification to the record's hypotheses as an application duty, beside `Embodied`.

### J5. presentation (omission): embodiment does not enter either valuation

**Location.** Study §18 bullets "两类是一类的特例" and "直接的关系"; record life-as-condition-of-life counterexample 1.

**Evidence.** `apart_embodied`: in `Mutualism.apart` both relata are embodied, activity needs support, and each depends on and draws on the other; neither co-participation nor interaction relates the bee to the flower.

**Why it matters.** In `apart` each relatum is, as a condition, exactly the other's activity, which is what "life as a condition of life" means. Both valuations relate events only through a shared condition, and a relatum's own events are not participants in its standing as a condition. So embodiment is invisible to the valuations; only a self-dependence (`SelfBearing.interacts`) connects a drawer to the drawn-on life. The study states the mechanism but frames the two-kind omission as embodiment, which suggests the one-kind reading recovers it in the valuations.

**Correction.** Add: "体现本身不进入两种估值：估值只经由共同的条件关联事件；只有承担自身把体现的关系项的活动接到汲取它的事件上（`apart` 中两者都体现而不相关）。这是估值所省略的关系。" A valuation relating a drawer to the events of the embodied relatum it draws on would be a new result.

### J6. overclaim: `ending_breaks` is co-occurrence with an ending of any cause

**Location.** Roles.lean:49–51: "`ending_breaks` makes ending another life by drawing on it count against living"; Roles.lean:40–41: "its eating breaks the hare's own dependence"; study §18 bullet "终结另一个生命" (line 1048); chapter §2 (lines 203, 205); P14 English summary: "whether ending another life should so count".

**What the Lean says.** `Embodied.ending_breaks`: any `f` drawing on `x` at step `t`, where `x` is embodied, bears on itself, is active at `t` and not at `t + 1`, is `BreakingOn t f x`. Nothing asks whether the drawing ends `x`. Under `Dependent`, `Embodied` and `SelfBearing`, `x`'s self-dependence is met exactly while `x` is active (`selfBearing_met_iff`), so it is broken across `t` exactly when `x` ends. `Predation` has no flow: the hare's end is the schedule `uneaten`.

**Evidence.** `Wilting.wilting`. The flower is embodied, bears on itself and wilts across step two by its own taking; the bee takes nothing ever. The flow balances, `Acting`, `Taking` and `Dependent` hold. The bee's drawing at step two is breaking and undermining, and so is the flower's own last event, since it draws on itself.

**Why it matters.** The content is "drawing on a self-bearing life at its last step is not living, whatever ends it". It counts against a pollinator present at a natural death, and against a life's own last event, exactly as against a predator. Leaving the choice to Ren is right, but Ren is shown only the predator. A causal reading, that the drawing ends the life, needs a counterfactual relation such as the but-for of `Joint`, which is not stated here.

**Correction.** Roles.lean: "`ending_breaks` counts drawing on a life that bears on itself, at the step at which it ends, against living, whatever ends it". Study and chapter: "在承担自身的生命终结之步汲取它，不论是什么终结了它，是断裂；这包括旁观的汲取者、自然的终结与生命自身的最后事件（`Wilting`）。是否应如此属于 Ren". Predation: "the fox draws on the hare across the step at which it ends". Move `Wilting` and `selfBearing_met_iff` into `Roles`.

### J7. overclaim: `arises_given` names an active giver, not a life

**Location.** Roles.lean:34–36 and the docstring at :305 ("Life from life"); record title "life given by life" and hypothesis 3; study §18 heading and bullet "生由生给予（作者的读法）" (line 1046): "一个生命的生起由另一个生命的活动给出"; chapter §2 heading and line 203 ("（AI 论证）"); P14 English summary "life from life", unlabelled; §8 (line 429), §9 (line 461).

**What the Lean says.** The conclusion is `∃ f, W.active t f ∧ f ∈ L.present t ∧ 0 < L.give t f x ∧ f ≠ x`. Nothing requires `f` to be embodied, to bear on itself, to depend on anything, or to be living.

**Evidence.** `SunSeed.sun_gives`: a seed is embodied and arises across step zero; the flow balances and only active relata give; the only giver is a sun that is not embodied, does not bear on itself and depends on nothing.

**Why it matters.** The AI reading is labelled, but a label does not license a content the theorem does not give. The theorem says an embodied relatum arises only through the giving of another active relatum: life from activity.

**Correction.** Retitle as "体现的关系项只经由另一个活跃者的给予而生起". "Life from life" holds only under a supplied premise, for example that only embodied relata give; state that variant if wanted, as a correspondence.

### J8. presentation: what the one-kind reading keeps

**Location.** Chapter line 132 "已陈述的读法……都不变" and line 143 "keeps every stated reading". Study §18 Delta boundary (line 1019) and boundary (line 1062), record zh limitation: "一类读法不保持 Acting、Taking 与 Dissipative 的陈述". Record `next_delta`: "keeping Acting and Taking".

**What the Lean says.** Every reading in the module doc's list has a `roles_*` theorem. The list is not every stated reading: `Acting`, `Taking`, `Census`, `ClosedAt`, `Dissipative`, `Capacity` and `Interacts` are stated and not covered.

**Evidence.** `roles_acting` and `roles_taking` (iff), `roles_census`, `roles_distinct`, and `roles_dissipative` (from the two-kind flow to the one-kind; the converse is not formalized here).

**Correction.** "列出的读法 / every listed reading". Move the five probes into `Roles`, drop the zh boundary clause (the English "is not shown to keep" is accurate today), and close the `next_delta` item.

### J9. overclaim: `NoSplit` is sufficient, not the exact boundary

**Location.** Study §19.1 I9 (line 1100): "所以分裂恰是界限"; §19.3 item 6 (line 1138): "限定由精确的界限代替"; §19.4 rebuttal 2 (line 1147): "新的是界限的精确：没有分裂时（允许合并），更多迫使生起；有分裂时不然"; record identity-across-steps, `Budding` counterexample: "splits are exactly what defeats “more forces arising”".

**What the Lean says.** `Flow.More.unceasingFrom` assumes `NoSplit`; `Budding` gives one continuation with splits under which the conclusion fails.

**Evidence.** `split_unceasing`: in the cycle, formation 0 continues as itself and as formation 1 at step one, and otherwise each formation continues itself. `NoSplit` fails, and formations still arise under this continuation at arbitrarily late steps.

**Why it matters.** A split does not by itself defeat arising; what defeats it in `Budding` is that every new formation continues an existing one. The fifth review's §4 item 6 proposed the wording "with `Budding` showing that splits are what defeat it"; that wording overstated, and P12b followed it.

**Correction.** "没有分裂是充分条件；萌出表明有的分裂使结论失效（`Budding`），一次分裂不必（`split_unceasing`）". An exact boundary would be a new result.

### J10. overclaim (omitted premise): the chapter's summaries of `unceasingFrom` and `arises_given`

**Location.** Chapter summary bullet (line 142): "more forces arising under every continuation without splits"; §8 (line 427): "在每种没有分裂的延续下更多迫使生起"; record identity-across-steps title. Identity.lean:97–99 states the census and omits distinctness and `Taking`. §8 (line 429): "体现的生命只经由另一个活跃形成的给予而生起" omits balance and `Acting`.

**Evidence.** `dormant_no_census`: under the identity continuation `Dormant` has no split, `Taking`, distinct `present` and more without end, and nothing arises.

**Correction.** "在普查、`present` 不重复与 Taking 之下，在每种没有分裂的延续下更多迫使生起"; "在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃者的给予而生起". The record's hypotheses already state these; the title can say "under a census".

### J11. presentation: bookkeeping and vocabulary

- **(a) Stale review row.** Chapter §8 (line 431): "跨步的同一（P12）与耗散（P13）尚未经独立审查". P12 was reviewed by the fifth review, which the row does not list; P14 and P12b are not mentioned.
- **(b) Module counts.** The P12, P13 and P14 English paragraphs say 19, 20 and 21 modules (the core closure); P12b's "over 19 modules" is the package count used in condition-correspondence-discipline (17 spine modules, the root and the bridge). Say which.
- **(c) "Proves it."** Flow.lean:50–51: "`Becoming.Dissipation` states that premise and proves it" should be "proves what it carries".
- **(d) "耗尽".** §9 (line 460): "被耗散的家族耗尽". `takers_within` and `taking_ceases` bound the takers and stop the taking; the stock need not reach zero. Write "取用终止".
- **(e) Vocabulary.** "代价", "付出" and "cost" (Dissipation.lean:17, Roles.lean:51, the record's hypothesis, §17 rebuttal 1, §18 rebuttal 5 and boundary) belong to the pay family Ren questioned on 2026-10-06. "给予须以取用为条件 / giving needs uptake" says the same. Ren decides.
- **(f) Stamps.** P12b changed the wording of no-finite-part-bears-taking and life-as-condition-of-life (history entries present), and their `reviewed_at_utc` stay 05:12:53Z and 05:45:34Z.

## 3. What remains sound

- **The theorems.** Every P13, P14 and P12b theorem holds as stated. The 21-module core recompiles from the prelude with empty axiom reports; counts, receipt, hashes, aliases and bindings are correct.
- **P13.** `replenishment_takers`, `runs_down`, `takers_within`, `taking_ceases`, `takers_pos_of_sub`, `Dissipative.opens`, `finite_ceases`, `More.takers_recur`, `takers_recur_of_arising`, `More.opens` and `opens_of_arising` are correct. `Frontier` is balanced and dissipative with a closed family at every step, and more without end. The boundaries are honest: dissipation is a physical premise; "finite part" is a finite family of conditions; arising without taking is unconstrained (`Tide`); the heat-death comparison is labelled an analogy. Rebuttal 5 on distinct families is right.
- **P14.** Each listed `roles_*` reading holds, with `roles_event_injective`, `roles_event_onto` and the two valuation connections. `SelfBearing.stands`, `active_of_bearing`, `active_along`, `coextinct` and `ends_when_consumed` are correct, and `coextinct`'s scope under `Dependent` (no reserves or dormancy) is disclosed. `Mutualism.connected`, `significant_iff`, `apart_not_connected` and `apart_not_interacting` are correct. `Brood` shows the premises of `arises_given` consistent with unceasing generation. `Embodied`, `SelfBearing` and `Dependent` are disclosed as representational premises, and whether ending counts against living is left to Ren.
- **P12b.** Each I1–I12 correction is in the Lean, the records and the chapter as claimed. The two-way theorems are exact. `Dormancy`, `TideFlip`, `Layered`, `Succession` with a living heir, `Garden.unceasing_reidentified`, `Repeated` and `Steady` are genuine witnesses. `Flow.More.unceasingFrom` is non-vacuous under merges, and its decidability premise is mild (rebuttal 3). Probe content continues to move into the core.
- **Method and provenance.** No source outside the unfolding is introduced. Ren's words are quoted exactly, and AI readings are labelled. Neither phase states diversity, complexity or possibility, or claims an ethical ranking.

## 4. What would change these verdicts

1. **Finite support (J1).** A finite-support premise, with the theorem that under it a giving formation takes more than it gives, and `Spray` in the record.
2. **Any continued taking (J2, J3).** The 整体 reading restated for recurring uptake with `Lone`; `Rooted` and `core_flows_not_dissipative` in the core.
3. **The identification (J4, J5).** The one-kind identification stated as a correspondence premise with `relabel`, and the valuations' omission of embodiment disclosed. A valuation reading embodiment directly would be a new result.
4. **Endings and giving (J6, J7).** `ending_breaks` glossed as co-occurrence with `Wilting` in the core and the scope of Ren's choice shown; `arises_given` retitled, or "life from life" proved under a stated premise that only lives give.
5. **Keeping (J8).** The five `roles_*` probes in the core and the boundary sentence corrected.
6. **Splits (J9, J10).** "Sufficient" for "exact", `split_unceasing` in the record, and the premises restored in the chapter. A necessary and sufficient condition on continuations would be a new result.
7. **Bookkeeping (J11).** The six items.
8. **Ren's choices.** These stay open and are not settled here: whether drawing at an ending counts against living, and for which drawers; the reading of succession; at which level 生生不息 is read; the names (`Depletes` and the cost wording).

**Not checked.**

- The Mathlib periphery (`CorrectionInquiry`, `CorrectionBoundary`, `ObservationChange`) was not rebuilt; its five aliases and eleven declaration names in becoming-spine-instances were not resolved. That record changed only its validation scope in these commits.
- The generated overview pages and `make research-check` were not run, since they write into the live repository.
- No external literature was consulted.
- Parity between the Chinese and English texts was checked only for the passages quoted above.
- The converse of `roles_dissipative` and the finite-support theorem proposed in J1 were not formalized.

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 against the unchanged `3828bcf8` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. The three probe files compile with exit 0 and no warnings. `ProbeAudit.lean` prints the axioms of all 81 probe declarations, and every one reports "does not depend on any axioms". `CoreAudit.lean` (898 `#print axioms` lines generated from the receipt), `BridgeAudit.lean` (50), `Aliases.lean` (281 `#check @` lines) and `Decls.lean` (778) are mechanical and are not reproduced; their hashes and results are in §0.

### `P13Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P13, P14 and P12b: the P13 part

Each probe is a minimal model satisfying the published definitions at `3828bcf8`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P13Probe

open Becoming

/-! ## N1. Every core flow on one condition with recurring taking fails `Dissipative` -/

theorem unit_every : ∀ c : Unit, c ∈ [()]
  | () => .head []

theorem unit_distinct : Distinct [()] := ⟨fun mem => (nomatch mem), trivial⟩

/-- By `Dissipative.finite_ceases`, a balanced flow on one condition whose takers recur is
not dissipative. -/
theorem not_dissipative {F : Type} {L : Flow F Unit} {W : Web F Unit} (balances : L.Balances W)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers [()] t) : ¬ L.Dissipative :=
  fun dissipative =>
    Flow.Dissipative.finite_ceases balances dissipative unit_distinct unit_every [()] recurs

/-- The garden, the cycle, the pulse, the steady consumer, the repeated formation and the
bloom all fail `Dissipative`: each witness of `Becoming.Flow` and `Becoming.Population`
in which taking recurs gives without taking enough. -/
theorem core_flows_not_dissipative :
    ¬ Garden.flow.Dissipative ∧ ¬ Cycle.flow.Dissipative ∧ ¬ Pulse.flow.Dissipative ∧
    ¬ Steady.flow.Dissipative ∧ ¬ Repeated.flow.Dissipative ∧ ¬ Bloom.flow.Dissipative :=
  ⟨not_dissipative Garden.more.1 Garden.more.2.2.2.2.2.2.takers_recur,
   not_dissipative Cycle.closed_more.1 Cycle.closed_more.2.2.2.2.2.2.1.takers_recur,
   not_dissipative Pulse.pulsed.1 Pulse.pulsed.2.2.2.1.takers_recur,
   not_dissipative Steady.steady.1 fun N => ⟨N, Nat.le_refl N, Nat.zero_lt_one⟩,
   not_dissipative Repeated.more_without_arising.2.1 Repeated.more_without_arising.2.2.2.2.1.takers_recur,
   not_dissipative Bloom.not_more.1 (Flow.takers_recur_of_arising (W := Bloom.web) fun N =>
     match Bloom.unceasing.2.2.2.1 N with
     | ⟨t, f, later, arises⟩ => ⟨t, f, later, Bloom.takes.2 t f arises⟩)⟩

/-! ## N2. `Dissipative` is vacuous at a step where some formation exchanges with
infinitely many conditions: a renewer can then give from nothing -/

namespace Spray

/-- A sink exchanging with every auxiliary condition, a renewer, and a consumer. -/
inductive Who where
  | sink
  | renewer
  | consumer

/-- Condition `0` is the pool; `n + 1` are auxiliary conditions. The sink takes one unit
from every auxiliary condition and gives it back; the renewer gives the pool one unit,
taking nothing; the consumer takes one unit from the pool. -/
def flow : Flow Who Nat where
  present _ := [.sink, .renewer, .consumer]
  take _ f c := match f, c with
    | .sink, _ + 1 => 1
    | .sink, 0 => 0
    | .renewer, _ => 0
    | .consumer, 0 => 1
    | .consumer, _ + 1 => 0
  give _ f c := match f, c with
    | .sink, _ + 1 => 1
    | .sink, 0 => 0
    | .renewer, 0 => 1
    | .renewer, _ + 1 => 0
    | .consumer, _ => 0

/-- Every condition holds one unit; all are active; the consumer depends on the pool at
need one and draws it; the sink draws every auxiliary condition. -/
def web : Web Who Nat where
  level _ _ := 1
  active _ _ := True
  requires _ f c := match f with
    | .consumer => c = 0
    | .sink | .renewer => False
  need _ _ _ := 1
  draws _ f c := match f, c with
    | .sink, _ + 1 => True
    | .sink, 0 => False
    | .renewer, _ => False
    | .consumer, 0 => True
    | .consumer, _ + 1 => False

/-- Every finite list of conditions misses one. -/
theorem fresh (cs : List Nat) : ¬ (total cs (fun c => c) + 1) ∈ cs :=
  fun mem => Nat.not_succ_le_self _ (le_total_of_mem (q := fun c => c) mem)

/-- No finite family is closed at any step, so dissipation holds vacuously. -/
theorem dissipative : flow.Dissipative := fun cs _ _ closed =>
  absurd ((closed .sink (.head _) _ (fresh cs)).1 : (1 : Nat) = 0) (fun h => Nat.noConfusion h)

/-- The flow balances, only active formations take and give, only from what they draw on,
activity needs support, and the flow is dissipative; yet at every step the renewer gives
the pool one unit while taking nothing from any condition, and one formation takes from
the pool. -/
theorem free_renewer :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ web.Dependent ∧
    flow.Dissipative ∧
    (∀ t, 0 < flow.give t .renewer 0 ∧ ∀ c, flow.take t .renewer c = 0) ∧
    ∀ t, 0 < flow.takers [0] t :=
  ⟨fun _ c => match c with
    | 0 => rfl
    | _ + 1 => rfl,
   fun _ _ _ _ _ => trivial,
   fun _ f c _ takes => match f, c, takes with
    | .sink, _ + 1, _ => ⟨trivial, trivial⟩
    | .consumer, 0, _ => ⟨trivial, trivial⟩
    | .sink, 0, takes => absurd takes (Nat.lt_irrefl 0)
    | .renewer, _, takes => absurd takes (Nat.lt_irrefl 0)
    | .consumer, _ + 1, takes => absurd takes (Nat.lt_irrefl 0),
   fun _ f _ _ depends => match f, depends with
    | .consumer, _ => Nat.le_refl 1
    | .sink, h | .renewer, h => (nomatch h),
   dissipative,
   fun _ => ⟨Nat.zero_lt_one, fun _ => rfl⟩,
   fun _ => Nat.zero_lt_one⟩

end Spray

/-! ## N3. Persistence alone, with nothing arising and no growth, needs the frontier -/

namespace Lone

open Frontier (Condition unburnt burning)

/-- A sun and one eater, both always active. -/
inductive Who where
  | sun
  | eater

/-- The sun burns the `t`th fuel, two units, and gives the pool one; the eater takes one
unit from the pool. -/
def flow : Flow Who Condition where
  present _ := [.sun, .eater]
  take t f c := match f, c with
    | .sun, .pool => 0
    | .sun, .fuel n => 2 * burning n t
    | .eater, .pool => 1
    | .eater, .fuel _ => 0
  give _ f c := match f, c with
    | .sun, .pool => 1
    | .sun, .fuel _ => 0
    | .eater, _ => 0

/-- The pool holds nothing between steps; the `n`th fuel holds two units until it burns. -/
def web : Web Who Condition where
  level t c := match c with
    | .pool => 0
    | .fuel n => 2 * unburnt n t
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws t f c := match f, c with
    | .sun, .pool => False
    | .sun, .fuel n => n = t
    | .eater, .pool => True
    | .eater, .fuel _ => False

theorem balances : flow.Balances web
  | _, .pool => rfl
  | t, .fuel n => show 2 * unburnt n (t + 1) + 2 * burning n t = 2 * unburnt n t from
      (Nat.left_distrib 2 _ _).symm.trans (congrArg (2 * ·) (Frontier.burns n t))

theorem dissipative : flow.Dissipative
  | ds, t, distinct, closed, f, mem => match f, mem with
    | .eater, _ => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_zero ds)).trans
        (Nat.zero_add _))) (sign_le _)
    | .sun, mem =>
      have gives : total ds (flow.give t .sun) ≤ 1 :=
        total_le_at (q := flow.give t .sun) (a := .pool) (fun c given => match c, given with
          | .pool, _ => rfl
          | .fuel _, given => absurd given (Nat.lt_irrefl 0)) distinct
      have burnt : flow.take t .sun (.fuel t) = 2 :=
        (congrArg (2 * ·) (Frontier.burning_self t)).trans (Nat.mul_one _)
      match Nat.decLe (total ds (flow.give t .sun) + sign (total ds (flow.take t .sun)))
          (total ds (flow.take t .sun)) with
      | isTrue le => le
      | isFalse not => absurd (fun inside : Condition.fuel t ∈ ds => not
          (Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
            (Nat.le_trans (Nat.le_of_eq burnt.symm) (le_total_of_mem inside))))
          fun outside => Nat.noConfusion (burnt.symm.trans (closed .sun mem (.fuel t) outside).1)

/-- One formation takes from the pool at every step, nothing ever arises and generation is
not more without end; under dissipation every finite family containing the pool is open at
arbitrarily late steps all the same. -/
theorem persistence_needs_frontier :
    flow.Balances web ∧ flow.Dissipative ∧ (∀ t, flow.takers [.pool] t = 1) ∧
    (∀ t f, ¬ web.Arises t f) ∧ ¬ flow.More [.pool] ∧
    ∀ {ds : List Condition}, Distinct ds → Condition.pool ∈ ds →
      ∀ T, ¬ ∀ t, T ≤ t → flow.ClosedAt ds t :=
  ⟨balances, dissipative, fun _ => rfl, fun _ _ arises => arises.1 trivial,
   fun more => match more 2 with
    | ⟨T, many⟩ => Nat.not_succ_le_self 1 (many T (Nat.le_refl T)),
   fun distinct pool T => Flow.Dissipative.opens (cs := [Condition.pool]) balances dissipative
     distinct (fun c inside => match c, inside with | .pool, _ => pool)
     (fun N => ⟨N, Nat.le_refl N, Nat.zero_lt_one⟩) T⟩

end Lone

/-! ## N4. The frontier with growers that depend on the pool: every premise of
`More.unceasing` and of `opens_of_arising` holds too -/

namespace Rooted

open Frontier (Condition Formation growers unburnt burning)

/-- `Frontier.flow` on a web whose pool holds one unit throughout, and whose growers depend
on it at need one while active. -/
def web : Web Formation Condition where
  level t c := match c with
    | .pool => 1
    | .fuel n => (n + 1) * unburnt n t
  active t f := match f with
    | .sun => True
    | .grower i => i < t
  requires t f c := match f, c with
    | .grower i, .pool => i < t
    | .grower _, .fuel _ => False
    | .sun, _ => False
  need _ _ _ := 1
  draws t f c := match f, c with
    | .sun, .pool => False
    | .sun, .fuel n => n = t
    | .grower i, .pool => i < t
    | .grower _, .fuel _ => False

theorem balances : Frontier.flow.Balances web
  | t, .pool => show 1 + (0 + total (growers t) _) = 1 + (t + total (growers t) _) from
      (congrArg (fun x => 1 + (0 + x)) (Frontier.growers_take t t)).trans
        ((congrArg (1 + ·) ((Nat.zero_add t).trans (Nat.add_zero t).symm)).trans
          (congrArg (fun x => 1 + (t + x)) (Frontier.growers_give t .pool t)).symm)
  | t, .fuel n => Frontier.balances t (.fuel n)

theorem growers_lt : ∀ t i, Formation.grower i ∈ growers t → i < t
  | n + 1, _, .head _ => Nat.lt_succ_self n
  | n + 1, i, .tail _ mem => Nat.lt_succ_of_lt (growers_lt n i mem)

theorem growers_listed : ∀ t i, i < t → Formation.grower i ∈ growers t
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | m + 1, i, lt => match Nat.lt_or_ge i m with
    | .inl below => .tail _ (growers_listed m i below)
    | .inr above => Eq.subst (motive := fun j => Formation.grower j ∈ growers (m + 1))
        (Nat.le_antisymm above (Nat.le_of_lt_succ lt)) (.head _)

theorem growers_distinct : ∀ t, Distinct (growers t)
  | 0 => trivial
  | n + 1 => ⟨fun mem => Nat.lt_irrefl n (growers_lt n n mem), growers_distinct n⟩

theorem sun_fresh : ∀ t, ¬ Formation.sun ∈ growers t
  | n + 1, .tail _ mem => sun_fresh n mem

theorem present_distinct (t : Nat) : Distinct (Frontier.flow.present t) :=
  ⟨sun_fresh t, growers_distinct t⟩

theorem census : web.Census Frontier.flow.present := fun t =>
  ⟨present_distinct t, fun f => match f with
    | .sun => ⟨fun _ => .head _, fun _ => trivial⟩
    | .grower i => ⟨fun lt => .tail _ (growers_listed t i lt), fun mem => match mem with
        | .tail _ mem => growers_lt t i mem⟩⟩

theorem burning_pos : ∀ n t, 0 < (n + 1) * burning n t → n = t := fun n t positive =>
  match h : burning n t with
  | 0 => absurd (Eq.subst (motive := fun b => 0 < (n + 1) * b) h positive) (Nat.lt_irrefl 0)
  | _ + 1 => Frontier.burning_at n t (Eq.subst (motive := fun b => 0 < b) h.symm (Nat.succ_pos _))

theorem taking : Frontier.flow.Taking web := fun t f c mem takes => match f, c, mem, takes with
  | .sun, .fuel n, _, takes => ⟨trivial, burning_pos n t takes⟩
  | .sun, .pool, _, takes => absurd takes (Nat.lt_irrefl 0)
  | .grower i, .pool, .tail _ mem, _ => ⟨growers_lt t i mem, growers_lt t i mem⟩
  | .grower _, .fuel _, _, takes => absurd takes (Nat.lt_irrefl 0)

theorem acting : Frontier.flow.Acting web := fun _ f c _ gives => match f, c, gives with
  | .sun, _, _ => trivial
  | .grower _, .pool, gives => absurd gives (Nat.lt_irrefl 0)
  | .grower _, .fuel _, gives => absurd gives (Nat.lt_irrefl 0)

theorem dependent : web.Dependent := fun _ f _ c depends => match f, c, depends with
  | .grower _, .pool, _ => Nat.le_refl 1
  | .grower _, .fuel _, h => (nomatch h)
  | .sun, _, h => (nomatch h)

instance decActive (t : Nat) (f : Formation) : Decidable (web.active t f) :=
  match f with
  | .sun => isTrue trivial
  | .grower i => Nat.decLt i t

/-- Each grower arises at its step and takes from the pool at its first active step. -/
theorem arises_taking (t : Nat) : Frontier.flow.ArisesTaking web [.pool] t (.grower t) :=
  ⟨⟨Nat.lt_irrefl t, Nat.lt_succ_self t⟩, .tail _ (.head _), Nat.zero_lt_one⟩

/-- With the growers depending on the pool, the frontier meets every premise of
`Flow.More.unceasing` together with balance, `Acting`, `Dependent` and `Dissipative`: its
generation is unceasing, and every finite family containing the pool is open at
arbitrarily late steps, by `opens_of_arising` as well as by `More.opens`. -/
theorem rooted :
    Frontier.flow.Balances web ∧ Frontier.flow.Acting web ∧ Frontier.flow.Taking web ∧
    web.Dependent ∧ web.Census Frontier.flow.present ∧ Frontier.flow.Dissipative ∧
    Frontier.flow.More [.pool] ∧ web.Unceasing ∧
    ∀ {ds : List Condition}, Distinct ds → Condition.pool ∈ ds →
      ∀ T, ¬ ∀ t, T ≤ t → Frontier.flow.ClosedAt ds t :=
  ⟨balances, acting, taking, dependent, census, Frontier.dissipative, Frontier.more,
   Flow.More.unceasing census present_distinct taking Frontier.more,
   fun distinct pool T => Flow.opens_of_arising balances Frontier.dissipative distinct
     (fun c inside => match c, inside with | .pool, _ => pool)
     (fun N => ⟨N, .grower N, Nat.le_refl N, arises_taking N⟩) T⟩

end Rooted

end P13Probe
```

### `P14Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P13, P14 and P12b: the P14 part

Each probe is a minimal model satisfying the published definitions at `3828bcf8`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P14Probe

open Becoming

/-! ## O1. `ending_breaks` reads drawing at the step of an ending, whatever ends it -/

namespace Wilting

inductive Relatum where
  | bee
  | flower

/-- One unit at step two: the flower's own taking as it wilts. -/
def fade : Nat → Nat
  | 0 => 0
  | 1 => 0
  | 2 => 1
  | _ + 3 => 0

/-- The bee stands at one throughout; the flower stands while unwilted, on the schedule
`Predation.uneaten`. The flower depends on itself at need one and draws on itself; the bee
draws on the flower and depends on nothing. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .bee => 1
    | .flower => Predation.uneaten t
  active t x := match x with
    | .bee => True
    | .flower => 0 < Predation.uneaten t
  requires _ x y := match x, y with
    | .flower, .flower => True
    | .flower, .bee => False
    | .bee, _ => False
  need _ _ _ := 1
  draws _ x y := match x, y with
    | .bee, .flower => True
    | .flower, .flower => True
    | .bee, .bee => False
    | .flower, .bee => False

/-- Only the flower takes, one unit from itself across step two. The bee takes nothing. -/
def flow : Flow Relatum Relatum where
  present _ := [.bee, .flower]
  take t x y := match x, y with
    | .flower, .flower => fade t
    | .flower, .bee => 0
    | .bee, _ => 0
  give _ _ _ := 0

theorem fade_active : ∀ t, 0 < fade t → 0 < Predation.uneaten t
  | 0, h => absurd h (Nat.lt_irrefl 0)
  | 1, h => absurd h (Nat.lt_irrefl 0)
  | 2, _ => Nat.zero_lt_one
  | _ + 3, h => absurd h (Nat.lt_irrefl 0)

theorem embodied : web.Embodied .flower := fun _ => Iff.rfl

theorem selfBearing : web.SelfBearing .flower := fun _ _ => ⟨trivial, Nat.zero_lt_one⟩

theorem dependent : web.Dependent := fun _ x active y depends => match x, y, active, depends with
  | .flower, .flower, active, _ => active
  | .flower, .bee, _, h => (nomatch h)
  | .bee, _, _, h => (nomatch h)

theorem ends : ¬ web.active 3 .flower := Nat.lt_irrefl 0

theorem bee_breaks : web.BreakingOn 2 .bee .flower :=
  Web.Embodied.ending_breaks (W := web) dependent embodied selfBearing (t := 2)
    Nat.zero_lt_one ends trivial

theorem own_breaks : web.BreakingOn 2 .flower .flower :=
  Web.Embodied.ending_breaks (W := web) dependent embodied selfBearing (t := 2)
    Nat.zero_lt_one ends trivial

/-- The flow balances, only active relata take, from what they draw on, and activity needs
support. The flower is embodied and bears on itself, and wilts across step two by its own
taking; the bee takes nothing, ever. Still, by `ending_breaks`, the bee's drawing at step
two breaks the flower's dependence and is undermining, and so is the flower's own last
event. -/
theorem wilting :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ web.Dependent ∧
    web.Embodied .flower ∧ web.SelfBearing .flower ∧
    (∀ t c, flow.take t .bee c = 0) ∧ (∀ t f, 0 < flow.take t f .flower → f = .flower) ∧
    web.BreakingOn 2 .bee .flower ∧ web.UnderminingAt 2 .bee ∧ web.UnderminingAt 2 .flower :=
  ⟨fun t c => match c, t with
    | .bee, _ => rfl
    | .flower, 0 => rfl
    | .flower, 1 => rfl
    | .flower, 2 => rfl
    | .flower, _ + 3 => rfl,
   fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0),
   fun t f c _ takes => match f, c, takes with
    | .flower, .flower, takes => ⟨fade_active t takes, trivial⟩
    | .flower, .bee, takes => absurd takes (Nat.lt_irrefl 0)
    | .bee, .bee, takes => absurd takes (Nat.lt_irrefl 0)
    | .bee, .flower, takes => absurd takes (Nat.lt_irrefl 0),
   dependent, embodied, selfBearing,
   fun _ c => match c with
    | .bee => rfl
    | .flower => rfl,
   fun _ f takes => match f, takes with
    | .flower, _ => rfl
    | .bee, takes => absurd takes (Nat.lt_irrefl 0),
   bee_breaks, ⟨.flower, bee_breaks.undermining⟩, ⟨.flower, own_breaks.undermining⟩⟩

end Wilting

/-! ## O2. `arises_given` names an active giver, not a life -/

namespace SunSeed

inductive Relatum where
  | sun
  | seed

def sprout : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- The sun is always active and stands at zero as a condition; the seed stands, and is
active, from step one. Nothing depends on or draws on anything. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .sun => 0
    | .seed => sprout t
  active t x := match x with
    | .sun => True
    | .seed => 0 < sprout t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- The sun gives the seed one unit across step zero. -/
def flow : Flow Relatum Relatum where
  present _ := [.sun]
  take _ _ _ := 0
  give t x y := match x, y with
    | .sun, .seed => Brood.first t
    | .sun, .sun => 0
    | .seed, _ => 0

/-- The flow balances and only active relata give; the seed is embodied and arises across
step zero, given by the sun alone. The sun is not embodied, does not bear on itself and
depends on nothing. -/
theorem sun_gives :
    flow.Balances web ∧ flow.Acting web ∧ web.Embodied .seed ∧ web.Arises 0 .seed ∧
    (∀ f, web.active 0 f ∧ f ∈ flow.present 0 ∧ 0 < flow.give 0 f .seed ∧ f ≠ .seed →
      f = .sun) ∧
    ¬ web.Embodied .sun ∧ ¬ web.SelfBearing .sun ∧ ∀ t c, ¬ web.requires t .sun c :=
  ⟨fun t c => match c, t with
    | .sun, _ => rfl
    | .seed, 0 => rfl
    | .seed, _ + 1 => rfl,
   fun _ f _ mem _ => match f, mem with
    | .sun, _ => trivial
    | .seed, .tail _ mem => (nomatch mem),
   fun _ => Iff.rfl,
   ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
   fun f ⟨_, mem, _, _⟩ => match f, mem with
    | .sun, _ => rfl
    | .seed, .tail _ mem => (nomatch mem),
   fun embodied => Nat.lt_irrefl 0 ((embodied 0).mp trivial),
   fun self => (self 0 trivial).1,
   fun _ _ h => h⟩

end SunSeed

/-! ## O3. Embodiment does not enter either valuation -/

section Apart

open Mutualism

variable {Pos : Type} (own sig : Pos → Relatum × Nat → Prop)

/-- In `Mutualism.apart` both relata are embodied and activity needs support; each depends
on and draws on the other; yet neither co-participation nor interaction relates the bee to
the flower. -/
theorem apart_embodied :
    (∀ x, apart.Embodied x) ∧ apart.Dependent ∧
    ¬ (apart.valuation own sig).Connected ∧ ¬ (apart.interaction own sig).Connected :=
  ⟨fun _ _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩, fun _ _ _ _ _ => Nat.le_refl 1,
   apart_not_connected own sig, apart_not_interacting own sig⟩

end Apart

/-! ## O4. Which condition is which formation is supplied by the shared index -/

section Relabel

variable {X : Type}

/-- The same web with the condition side relabelled by `π`: the formation side is
unchanged, and condition `y` is what condition `π y` was. -/
def relabel (W : Web X X) (π : X → X) : Web X X where
  level t y := W.level t (π y)
  active := W.active
  requires t g y := W.requires t g (π y)
  need t g y := W.need t g (π y)
  draws t g y := W.draws t g (π y)

variable {W : Web X X} {π : X → X}

theorem relabel_dependent (inv : ∀ y, π (π y) = y) : (relabel W π).Dependent ↔ W.Dependent :=
  ⟨fun dependent t f active c depends =>
    have depends' : W.requires t f (π (π c)) :=
      Eq.subst (motive := fun z => W.requires t f z) (inv c).symm depends
    Eq.subst (motive := fun z => W.need t f z ≤ W.level t z) (inv c)
      (dependent t f active (π c) depends'),
   fun dependent t f active y depends => dependent t f active (π y) depends⟩

theorem relabel_undermining (inv : ∀ y, π (π y) = y) (t : Nat) (f : X) :
    (relabel W π).UnderminingAt t f ↔ W.UnderminingAt t f :=
  ⟨fun ⟨y, undermining⟩ => ⟨π y, undermining⟩,
   fun ⟨c, undermining⟩ => ⟨π c,
     Eq.subst (motive := fun z => W.UnderminingOn t f z) (inv c).symm undermining⟩⟩

/-- Relabelling the condition side by an involution keeps the connection of the
interaction valuation, as it keeps `Dependent` and undermining. -/
theorem relabel_interaction_connected (inv : ∀ y, π (π y) = y) {Pos : Type}
    (own sig : Pos → X × Nat → Prop) :
    ((relabel W π).interaction own sig).Connected ↔ (W.interaction own sig).Connected :=
  Valuation.connected_iff_of_map (q := fun e => e) (fun _ _ same => same)
    (fun e _ => ⟨e, rfl⟩)
    (fun e => ⟨fun ⟨active, sound⟩ =>
        ⟨active, fun u => sound ((relabel_undermining (W := W) inv e.2 e.1).mpr u)⟩,
      fun ⟨active, sound⟩ =>
        ⟨active, fun u => sound ((relabel_undermining (W := W) inv e.2 e.1).mp u)⟩⟩)
    (fun e e' => ⟨fun ⟨y, interacts⟩ => ⟨π y, interacts⟩,
      fun ⟨c, interacts⟩ => ⟨π c,
        Eq.subst (motive := fun z => W.Interacts z e e') (inv c).symm interacts⟩⟩)

end Relabel

open Mutualism in
/-- Relabelled by `other`, `Mutualism.apart` becomes a web in which the bee and the flower
each bear on themselves, while `Dependent` is unchanged. -/
theorem apart_relabelled :
    (∀ x, ¬ apart.SelfBearing x) ∧ (∀ x, (relabel apart other).SelfBearing x) ∧
    ((relabel apart other).Dependent ↔ apart.Dependent) :=
  ⟨apart_not_selfBearing, fun _ _ _ => ⟨rfl, Nat.zero_lt_one⟩,
   relabel_dependent fun y => match y with
    | .bee => rfl
    | .flower => rfl⟩

namespace Wilting

def swap : Relatum → Relatum
  | .bee => .flower
  | .flower => .bee

/-- Relabelled by `swap`, the wilting flower is no longer embodied. -/
theorem relabelled_not_embodied :
    web.Embodied .flower ∧ ¬ (relabel web swap).Embodied .flower :=
  ⟨embodied, fun embodied' => Nat.lt_irrefl 0 ((embodied' 3).mpr Nat.zero_lt_one)⟩

end Wilting

/-! ## O5. A self-dependence of an embodied relatum is met exactly while it is active -/

theorem selfBearing_met_iff {X : Type} {W : Web X X} (dependent : W.Dependent) {x : X}
    (embodied : W.Embodied x) (self : W.SelfBearing x) (t : Nat) :
    (W.requires t x x ∧ 0 < W.need t x x ∧ W.need t x x ≤ W.level t x) ↔ W.active t x :=
  ⟨fun ⟨_, positive, met⟩ => (embodied t).mpr (Nat.lt_of_lt_of_le positive met),
   fun active => ⟨(self t active).1, (self t active).2,
     dependent t x active x (self t active).1⟩⟩

/-! ## O6. The one-kind reading keeps `Acting`, `Taking`, a census and `Dissipative` -/

section Roles

variable {F C : Type}

theorem inl_inj : ∀ a b : F, (Sum.inl a : F ⊕ C) = Sum.inl b → a = b
  | _, _, rfl => rfl

theorem inr_not_mem {c : C} : ∀ {l : List F}, ¬ (Sum.inr c : F ⊕ C) ∈ l.map Sum.inl
  | [], mem => nomatch mem
  | _ :: l, mem => match mem_cons_cases mem with
    | .inr mem => inr_not_mem (l := l) mem

theorem roles_acting {L : Flow F C} {W : Web F C} : L.roles.Acting W.roles ↔ L.Acting W :=
  ⟨fun acting t f c mem gives => acting t (.inl f) (.inr c) (mem_map_of (g := Sum.inl) mem) gives,
   fun acting t x y mem gives => match x, y, mem, gives with
    | .inl f, .inr c, mem, gives => acting t f c (mem_of_map inl_inj mem) gives
    | .inl _, .inl _, _, gives => absurd gives (Nat.lt_irrefl 0)
    | .inr _, _, _, gives => absurd gives (Nat.lt_irrefl 0)⟩

theorem roles_taking {L : Flow F C} {W : Web F C} : L.roles.Taking W.roles ↔ L.Taking W :=
  ⟨fun taking t f c mem takes => taking t (.inl f) (.inr c) (mem_map_of (g := Sum.inl) mem) takes,
   fun taking t x y mem takes => match x, y, mem, takes with
    | .inl f, .inr c, mem, takes => taking t f c (mem_of_map inl_inj mem) takes
    | .inl _, .inl _, _, takes => absurd takes (Nat.lt_irrefl 0)
    | .inr _, _, _, takes => absurd takes (Nat.lt_irrefl 0)⟩

theorem roles_census {W : Web F C} {alive : Nat → List F} (census : W.Census alive) :
    W.roles.Census fun t => (alive t).map Sum.inl :=
  fun t => ⟨distinct_map inl_inj (census t).1, fun x => match x with
    | .inl f => ⟨fun active => mem_map_of (g := Sum.inl) (((census t).2 f).mp active),
        fun mem => ((census t).2 f).mpr (mem_of_map inl_inj mem)⟩
    | .inr _ => ⟨False.elim, fun mem => absurd mem inr_not_mem⟩⟩

theorem roles_distinct {L : Flow F C} {t : Nat} (distinct : Distinct (L.present t)) :
    Distinct (L.roles.present t) :=
  distinct_map inl_inj distinct

/-- The conditions of a one-kind family. -/
def inrs : List (F ⊕ C) → List C
  | [] => []
  | .inl _ :: l => inrs l
  | .inr c :: l => c :: inrs l

theorem mem_inrs {c : C} : ∀ {l : List (F ⊕ C)}, c ∈ inrs l → Sum.inr c ∈ l
  | .inl _ :: l, mem => .tail _ (mem_inrs (l := l) mem)
  | .inr _ :: l, mem => match mem_cons_cases (q := inrs l) mem with
    | .inl same =>
      Eq.subst (motive := fun z => (Sum.inr c : F ⊕ C) ∈ Sum.inr z :: l) same (.head _)
    | .inr mem => .tail _ (mem_inrs (l := l) mem)

theorem inrs_of_mem {c : C} : ∀ {l : List (F ⊕ C)}, Sum.inr c ∈ l → c ∈ inrs l
  | .inl _ :: l, mem => match mem_cons_cases mem with
    | .inr mem => (inrs_of_mem (l := l) mem : c ∈ inrs l)
  | .inr d :: l, mem => match mem_cons_cases mem with
    | .inl rfl => (.head _ : c ∈ c :: inrs l)
    | .inr mem => (.tail _ (inrs_of_mem (l := l) mem) : c ∈ d :: inrs l)

theorem distinct_inrs : ∀ {l : List (F ⊕ C)}, Distinct l → Distinct (inrs l)
  | [], _ => trivial
  | .inl _ :: l, ⟨_, distinct⟩ => (distinct_inrs (l := l) distinct : Distinct (inrs l))
  | .inr _ :: l, ⟨fresh, distinct⟩ =>
    ⟨fun mem => fresh (mem_inrs (l := l) mem), distinct_inrs (l := l) distinct⟩

theorem total_inrs {p : F ⊕ C → Nat} {q : C → Nat} (zero : ∀ f, p (.inl f) = 0)
    (same : ∀ c, p (.inr c) = q c) : ∀ l : List (F ⊕ C), total l p = total (inrs l) q
  | [] => rfl
  | .inl f :: l => (congrArg (· + total l p) (zero f)).trans
      ((Nat.zero_add _).trans (total_inrs zero same l))
  | .inr c :: l => congr (congrArg (· + ·) (same c)) (total_inrs zero same l)

/-- Dissipation carries over to the one-kind reading. -/
theorem roles_dissipative {L : Flow F C} (dissipative : L.Dissipative) : L.roles.Dissipative :=
  fun ds t distinct closed x mem => match x, mem with
  | .inr _, mem => absurd mem inr_not_mem
  | .inl f, mem =>
    have closed' : L.ClosedAt (inrs ds) t := fun g present c outside =>
      closed (.inl g) (mem_map_of (g := Sum.inl) present) (.inr c)
        fun inside => outside (inrs_of_mem inside)
    have dissipates := dissipative (inrs ds) t (distinct_inrs distinct) closed' f
      (mem_of_map inl_inj mem)
    have gives := total_inrs (p := L.roles.give t (.inl f)) (q := L.give t f)
      (fun _ => rfl) (fun _ => rfl) ds
    have takes := total_inrs (p := L.roles.take t (.inl f)) (q := L.take t f)
      (fun _ => rfl) (fun _ => rfl) ds
    Nat.le_trans (Nat.le_of_eq (congr (congrArg (· + ·) gives) (congrArg sign takes)))
      (Nat.le_trans dissipates (Nat.le_of_eq takes.symm))

end Roles

end P14Probe
```

### `P12bProbes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P13, P14 and P12b: the P12b part

Each probe is a minimal model satisfying the published definitions at `3828bcf8`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P12bProbe

open Becoming

/-! ## Q1. A split does not by itself defeat arising under a continuation -/

/-- Each formation of the cycle continues itself; at step one formation `0` also
continues as formation `1`. -/
def splitOnce (t g f : Nat) : Prop :=
  g = f ∨ (t = 1 ∧ g = 0 ∧ f = 1)

/-- The cycle under `splitOnce` has a split, and formations still arise under it at
arbitrarily late steps. `NoSplit` is sufficient for `Flow.More.unceasingFrom`, not
necessary for its conclusion. -/
theorem split_unceasing : ¬ Cycle.web.NoSplit splitOnce ∧ Cycle.web.UnceasingFrom splitOnce :=
  ⟨fun noSplit =>
      have split : (0 : Nat) = 1 := noSplit 1 0 0 1 Nat.zero_lt_one (.inl rfl)
        (.inr ⟨rfl, rfl, rfl⟩) (Nat.zero_lt_succ 1) (Nat.lt_succ_self 1)
      Nat.lt_irrefl 0 (Eq.subst (motive := fun k => 0 < k) split.symm Nat.zero_lt_one),
   fun N => ⟨N + 2, N + 2, Nat.le_add_right N 2, Nat.lt_succ_self (N + 2),
     fun ⟨_, active, continues⟩ => match continues with
      | .inl same => Nat.lt_irrefl (N + 2)
          (Eq.subst (motive := fun h => h < N + 2) same active)
      | .inr ⟨one, _, _⟩ => Nat.lt_irrefl 1
          (Eq.subst (motive := fun k => 1 < k) one (Nat.succ_lt_succ (Nat.zero_lt_succ N)))⟩⟩

/-! ## Q2. Merges keep `NoSplit`, and the theorem applies -/

namespace Merge

open Garden

/-- The `i`th renewer and the `i`th grower both continue as the `i`th renewer. -/
def mergeR (_ : Nat) (g f : Kind × Nat) : Prop :=
  f = (.renewer, g.2)

instance continuesDec : ∀ t f, Decidable (Garden.web.Continues mergeR t f)
  | _, (.grower, _) => isFalse fun ⟨_, _, same⟩ => Kind.noConfusion (congrArg Prod.fst same)
  | t, (.renewer, i) => match Nat.decLt i t with
    | isTrue lt => isTrue ⟨(.renewer, i), lt, rfl⟩
    | isFalse ge => isFalse fun ⟨_, active, same⟩ =>
        ge (Eq.subst (motive := fun j => j < t) (congrArg Prod.snd same).symm active)

theorem noSplit : Garden.web.NoSplit mergeR :=
  fun _ _ _ _ _ same same' _ _ => same.trans same'.symm

/-- Two formations active at step one continue as one after it. -/
theorem merges :
    Garden.web.active 1 (.renewer, 0) ∧ Garden.web.active 1 (.grower, 0) ∧
    mergeR 1 (.renewer, 0) (.renewer, 0) ∧ mergeR 1 (.grower, 0) (.renewer, 0) ∧
    Garden.web.active 2 (.renewer, 0) ∧ (Kind.renewer, 0) ≠ (Kind.grower, 0) :=
  ⟨Nat.zero_lt_one, Nat.zero_lt_one, rfl, rfl, Nat.zero_lt_succ 1,
   fun same => Kind.noConfusion (congrArg Prod.fst same)⟩

/-- With merges and no split, more without end makes formations arise under `mergeR`. -/
theorem unceasing : Garden.web.UnceasingFrom mergeR :=
  Flow.More.unceasingFrom (L := Garden.flow) Garden.census Garden.distinct
    Garden.growers_take.1 Garden.counted.2.2.2 noSplit

end Merge

/-! ## Q3. Without a census, no split is not enough -/

/-- In `Dormant`, under the identity continuation there is no split, only active formations
take, each formation taking part is listed once, and generation is more without end, yet
nothing arises under it. -/
theorem dormant_no_census :
    Dormant.web.NoSplit (fun _ g f => g = f) ∧ Garden.flow.More [()] ∧
    Garden.flow.Taking Dormant.web ∧ (∀ t, Distinct (Garden.flow.present t)) ∧
    ¬ Dormant.web.UnceasingFrom (fun _ g f => g = f) :=
  ⟨fun _ _ _ _ _ same same' _ _ => same.symm.trans same',
   Dormant.more_without_arising.2.2.2.2.2.1, Dormant.more_without_arising.2.2.1,
   Garden.distinct,
   fun unceasing => match (Dormant.web.unceasingFrom_self.mp unceasing) 0 with
    | ⟨t, f, _, arises⟩ => Dormant.more_without_arising.2.2.2.2.2.2 t f arises⟩

/-! ## Q4. Two-way continuity excludes a join at one step -/

/-- If the new naming's continuing activity keeps the old names, two formations named alike
across one step are one formation. -/
theorem no_join {F F' C : Type} {W : Web F C} {σ : Reidentify F F'}
    (kept : σ.back.KeepsActive (W.reidentify σ)) {t : Nat} {g h : F}
    (before : W.active t g) (after : W.active (t + 1) h) (same : σ.new t g = σ.new (t + 1) h) :
    g = h :=
  have before' : (W.reidentify σ).active t (σ.new t g) :=
    Eq.subst (motive := fun x => W.active t x) (σ.old_new t g).symm before
  have after' : (W.reidentify σ).active (t + 1) (σ.new t g) :=
    Eq.subst (motive := fun x => (W.reidentify σ).active (t + 1) x) same.symm
      (Eq.subst (motive := fun x => W.active (t + 1) x) (σ.old_new (t + 1) h).symm after)
  (σ.old_new t g).symm.trans ((kept t _ before' after').symm.trans
    ((congrArg (σ.old (t + 1)) same).trans (σ.old_new (t + 1) h)))

/-! ## Q5. Under a census, a decidable continuation gives the decidability the theorem asks -/

def decExists {α : Type} {p : α → Prop} [dec : ∀ a, Decidable (p a)] :
    ∀ l : List α, Decidable (∃ a, a ∈ l ∧ p a)
  | [] => isFalse fun ⟨_, mem, _⟩ => nomatch mem
  | a :: l => match dec a with
    | isTrue holds => isTrue ⟨a, .head l, holds⟩
    | isFalse lacks => match decExists l with
      | isTrue found => isTrue (match found with | ⟨b, mem, holds⟩ => ⟨b, .tail a mem, holds⟩)
      | isFalse absent => isFalse fun ⟨b, mem, holds⟩ => match mem_cons_cases mem with
        | .inl same => lacks (Eq.subst (motive := p) same holds)
        | .inr mem => absent ⟨b, mem, holds⟩

def continuesDec {F C : Type} {W : Web F C} {R : Nat → F → F → Prop}
    [∀ t g f, Decidable (R t g f)] {alive : Nat → List F} (census : W.Census alive)
    (t : Nat) (f : F) : Decidable (W.Continues R t f) :=
  have : ∀ g, Decidable (R t g f) := fun _ => inferInstance
  decidable_of_decidable_of_iff (p := ∃ g, g ∈ alive t ∧ R t g f)
    ⟨fun ⟨g, mem, r⟩ => ⟨g, ((census t).2 g).mpr mem, r⟩,
     fun ⟨g, active, r⟩ => ⟨g, ((census t).2 g).mp active, r⟩⟩

/-- The decidability premise of `Flow.More.unceasingFrom` follows from a census and a
decidable continuation. -/
theorem unceasingFrom_of_decidable {F C : Type} {W : Web F C} {R : Nat → F → F → Prop}
    [∀ t g f, Decidable (R t g f)] {L : Flow F C} {cs : List C} {alive : Nat → List F}
    (census : W.Census alive) (distinct : ∀ t, Distinct (L.present t)) (taking : L.Taking W)
    (more : L.More cs) (noSplit : W.NoSplit R) : W.UnceasingFrom R :=
  have : ∀ t f, Decidable (W.Continues R t f) := continuesDec census
  Flow.More.unceasingFrom census distinct taking more noSplit

end P12bProbe
```

### `ProbeAudit.lean`

```lean
import P13Probes
import P14Probes
import P12bProbes

#print axioms P13Probe.unit_every
#print axioms P13Probe.unit_distinct
#print axioms P13Probe.not_dissipative
#print axioms P13Probe.core_flows_not_dissipative
#print axioms P13Probe.Spray.Who
#print axioms P13Probe.Spray.flow
#print axioms P13Probe.Spray.web
#print axioms P13Probe.Spray.fresh
#print axioms P13Probe.Spray.dissipative
#print axioms P13Probe.Spray.free_renewer
#print axioms P13Probe.Lone.Who
#print axioms P13Probe.Lone.flow
#print axioms P13Probe.Lone.web
#print axioms P13Probe.Lone.balances
#print axioms P13Probe.Lone.dissipative
#print axioms P13Probe.Lone.persistence_needs_frontier
#print axioms P13Probe.Rooted.web
#print axioms P13Probe.Rooted.balances
#print axioms P13Probe.Rooted.growers_lt
#print axioms P13Probe.Rooted.growers_listed
#print axioms P13Probe.Rooted.growers_distinct
#print axioms P13Probe.Rooted.sun_fresh
#print axioms P13Probe.Rooted.present_distinct
#print axioms P13Probe.Rooted.census
#print axioms P13Probe.Rooted.burning_pos
#print axioms P13Probe.Rooted.taking
#print axioms P13Probe.Rooted.acting
#print axioms P13Probe.Rooted.dependent
#print axioms P13Probe.Rooted.decActive
#print axioms P13Probe.Rooted.arises_taking
#print axioms P13Probe.Rooted.rooted
#print axioms P14Probe.Wilting.Relatum
#print axioms P14Probe.Wilting.fade
#print axioms P14Probe.Wilting.web
#print axioms P14Probe.Wilting.flow
#print axioms P14Probe.Wilting.fade_active
#print axioms P14Probe.Wilting.embodied
#print axioms P14Probe.Wilting.selfBearing
#print axioms P14Probe.Wilting.dependent
#print axioms P14Probe.Wilting.ends
#print axioms P14Probe.Wilting.bee_breaks
#print axioms P14Probe.Wilting.own_breaks
#print axioms P14Probe.Wilting.wilting
#print axioms P14Probe.SunSeed.Relatum
#print axioms P14Probe.SunSeed.sprout
#print axioms P14Probe.SunSeed.web
#print axioms P14Probe.SunSeed.flow
#print axioms P14Probe.SunSeed.sun_gives
#print axioms P14Probe.apart_embodied
#print axioms P14Probe.relabel
#print axioms P14Probe.relabel_dependent
#print axioms P14Probe.relabel_undermining
#print axioms P14Probe.relabel_interaction_connected
#print axioms P14Probe.apart_relabelled
#print axioms P14Probe.Wilting.swap
#print axioms P14Probe.Wilting.relabelled_not_embodied
#print axioms P14Probe.selfBearing_met_iff
#print axioms P14Probe.inl_inj
#print axioms P14Probe.inr_not_mem
#print axioms P14Probe.roles_acting
#print axioms P14Probe.roles_taking
#print axioms P14Probe.roles_census
#print axioms P14Probe.roles_distinct
#print axioms P14Probe.inrs
#print axioms P14Probe.mem_inrs
#print axioms P14Probe.inrs_of_mem
#print axioms P14Probe.distinct_inrs
#print axioms P14Probe.total_inrs
#print axioms P14Probe.roles_dissipative
#print axioms P12bProbe.splitOnce
#print axioms P12bProbe.split_unceasing
#print axioms P12bProbe.Merge.mergeR
#print axioms P12bProbe.Merge.continuesDec
#print axioms P12bProbe.Merge.noSplit
#print axioms P12bProbe.Merge.merges
#print axioms P12bProbe.Merge.unceasing
#print axioms P12bProbe.dormant_no_census
#print axioms P12bProbe.no_join
#print axioms P12bProbe.decExists
#print axioms P12bProbe.continuesDec
#print axioms P12bProbe.unceasingFrom_of_decidable
```

### `ProbeAudit` output

```text
'P13Probe.unit_every' does not depend on any axioms
'P13Probe.unit_distinct' does not depend on any axioms
'P13Probe.not_dissipative' does not depend on any axioms
'P13Probe.core_flows_not_dissipative' does not depend on any axioms
'P13Probe.Spray.Who' does not depend on any axioms
'P13Probe.Spray.flow' does not depend on any axioms
'P13Probe.Spray.web' does not depend on any axioms
'P13Probe.Spray.fresh' does not depend on any axioms
'P13Probe.Spray.dissipative' does not depend on any axioms
'P13Probe.Spray.free_renewer' does not depend on any axioms
'P13Probe.Lone.Who' does not depend on any axioms
'P13Probe.Lone.flow' does not depend on any axioms
'P13Probe.Lone.web' does not depend on any axioms
'P13Probe.Lone.balances' does not depend on any axioms
'P13Probe.Lone.dissipative' does not depend on any axioms
'P13Probe.Lone.persistence_needs_frontier' does not depend on any axioms
'P13Probe.Rooted.web' does not depend on any axioms
'P13Probe.Rooted.balances' does not depend on any axioms
'P13Probe.Rooted.growers_lt' does not depend on any axioms
'P13Probe.Rooted.growers_listed' does not depend on any axioms
'P13Probe.Rooted.growers_distinct' does not depend on any axioms
'P13Probe.Rooted.sun_fresh' does not depend on any axioms
'P13Probe.Rooted.present_distinct' does not depend on any axioms
'P13Probe.Rooted.census' does not depend on any axioms
'P13Probe.Rooted.burning_pos' does not depend on any axioms
'P13Probe.Rooted.taking' does not depend on any axioms
'P13Probe.Rooted.acting' does not depend on any axioms
'P13Probe.Rooted.dependent' does not depend on any axioms
'P13Probe.Rooted.decActive' does not depend on any axioms
'P13Probe.Rooted.arises_taking' does not depend on any axioms
'P13Probe.Rooted.rooted' does not depend on any axioms
'P14Probe.Wilting.Relatum' does not depend on any axioms
'P14Probe.Wilting.fade' does not depend on any axioms
'P14Probe.Wilting.web' does not depend on any axioms
'P14Probe.Wilting.flow' does not depend on any axioms
'P14Probe.Wilting.fade_active' does not depend on any axioms
'P14Probe.Wilting.embodied' does not depend on any axioms
'P14Probe.Wilting.selfBearing' does not depend on any axioms
'P14Probe.Wilting.dependent' does not depend on any axioms
'P14Probe.Wilting.ends' does not depend on any axioms
'P14Probe.Wilting.bee_breaks' does not depend on any axioms
'P14Probe.Wilting.own_breaks' does not depend on any axioms
'P14Probe.Wilting.wilting' does not depend on any axioms
'P14Probe.SunSeed.Relatum' does not depend on any axioms
'P14Probe.SunSeed.sprout' does not depend on any axioms
'P14Probe.SunSeed.web' does not depend on any axioms
'P14Probe.SunSeed.flow' does not depend on any axioms
'P14Probe.SunSeed.sun_gives' does not depend on any axioms
'P14Probe.apart_embodied' does not depend on any axioms
'P14Probe.relabel' does not depend on any axioms
'P14Probe.relabel_dependent' does not depend on any axioms
'P14Probe.relabel_undermining' does not depend on any axioms
'P14Probe.relabel_interaction_connected' does not depend on any axioms
'P14Probe.apart_relabelled' does not depend on any axioms
'P14Probe.Wilting.swap' does not depend on any axioms
'P14Probe.Wilting.relabelled_not_embodied' does not depend on any axioms
'P14Probe.selfBearing_met_iff' does not depend on any axioms
'P14Probe.inl_inj' does not depend on any axioms
'P14Probe.inr_not_mem' does not depend on any axioms
'P14Probe.roles_acting' does not depend on any axioms
'P14Probe.roles_taking' does not depend on any axioms
'P14Probe.roles_census' does not depend on any axioms
'P14Probe.roles_distinct' does not depend on any axioms
'P14Probe.inrs' does not depend on any axioms
'P14Probe.mem_inrs' does not depend on any axioms
'P14Probe.inrs_of_mem' does not depend on any axioms
'P14Probe.distinct_inrs' does not depend on any axioms
'P14Probe.total_inrs' does not depend on any axioms
'P14Probe.roles_dissipative' does not depend on any axioms
'P12bProbe.splitOnce' does not depend on any axioms
'P12bProbe.split_unceasing' does not depend on any axioms
'P12bProbe.Merge.mergeR' does not depend on any axioms
'P12bProbe.Merge.continuesDec' does not depend on any axioms
'P12bProbe.Merge.noSplit' does not depend on any axioms
'P12bProbe.Merge.merges' does not depend on any axioms
'P12bProbe.Merge.unceasing' does not depend on any axioms
'P12bProbe.dormant_no_census' does not depend on any axioms
'P12bProbe.no_join' does not depend on any axioms
'P12bProbe.decExists' does not depend on any axioms
'P12bProbe.continuesDec' does not depend on any axioms
'P12bProbe.unceasingFrom_of_decidable' does not depend on any axioms
```
