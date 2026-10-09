# P11b 与 P12 的独立审查 / Independent review of P11b and P12

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写 P11b 或 P12。对象：`main` 的 `e5430db5`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote neither phase. Object: `main` at `e5430db5`.

**摘要（中文）。** P11b 与 P12 的全部 Lean 声明在仓库之外从前导重新编译，19 个核心模块的公理报告为空。回执 `20261009T045039.065929Z`（422 项定理／760 项声明审计，核心闭包 19 个模块）、记录的哈希与别名都对。数学被接受，没有发现数学错误。审计覆盖 780 条声明，全部不依赖任何公理：710 条核心声明，其中 Identity 72 条、Population 29 条；另有 70 条探针声明，其中 41 项定理。问题在前提的陈述、散文与对应之间，共十二项（I1–I12）。

- **P11b。** H1–H14 全部关闭，残余四项。
  - `Flow.More.unceasing` 还需要第三个前提：流的 `present` 不重复。只缺这一前提时，普查、Taking 与不止地更多同时成立，而没有任何生起（`Repeated`）。章节两处省去了它，照字面是错的（I1）。
  - `More.unceasing` 及其改认形式，在核心中没有一个满足全部前提的正面见证。`Garden` 满足它们（I2）。
  - 流的形式 `replenishment_recurs` 的证明丢弃了 `Arises`，生起只提供“任意晚的步有正的取用”。取用者恒定、没有任何生起的流，同样需要补充复现（`Steady`）。§15.4 反驳 2 说 `ArisesTaking` 的内容正在于生起与取用的联系，这强于定理（I3）。
  - 命名与记账上另有小问题（I4）。
- **P12。** 改认不变与依赖同一的清单逐项正确，两个连续定理的方向也正确。问题如下。
  - **单向的连续（I5）。** 连续是相对于一个参照命名的单向条件。见证中的两种命名只单向保持连续（`lineage_one_way`、`succession_one_way`）。双向读时，生起与侵蚀恰被保持（`arises_iff_of_keepsActive_both`、`undermining_of_inverse_keepsTenure`）。这回答了记录所列的“反方向在什么附加条件下成立”。
  - **休眠（I6）。** 即使双向保持连续，跨过一个休眠步把终结者与后来的开始者接起来，仍改变形成的类（`Dormancy`）。“接续”被定义为在同一步终结与开始，不覆盖这种情形。
  - **改名（I7）。** “名字不承载任何东西”与“跨步的同一由命名规定”并置，字面上矛盾。改名不变只说明标签的选择不起作用。方法要求所防的偷渡恰在名字跨步的模式之中，而改名按构造保持这一模式，所以改名不变检查不到它。
  - **命名造成的生起（I8）。** 单由命名造成的不息生成，可以满足 `Unceasing.regeneration_recurs` 的全部前提（`TideFlip`）。`Depletes` 不筛掉命名的产物。P10 不受影响，理由只在于结论只关乎条件。
  - **分裂（I9）。** “在每种同一的读法下”与“分裂与合并改变形成的数目”都不成立。每步形成的数目由每步的关系确定，分裂改变的是延续关系。把新形成读作从既有形成萌出时，普查、不重复、Taking 与不止地更多都成立，而第一步之后没有任何生起（`Budding`）。
  - **谱系（I10）。** 谱系的 AI 论证说，谱系的持续“落在维持与更新上”，可见证中没有任何条件。这里的二选一出自单一的命名层次：把谱系本身也命名为一个形成，谱系每步活跃，成员同时不息地生起（`Layered`）。表示省略的是部分与整体的关系。
  - **继承者（I11）。** `Succession` 的继承者从不活跃。继承者活跃、并在第一个活跃步被满足时，结论照样成立（`ActiveHeir`）。
  - **记录（I12）。** 依赖同一的读法，没有在其所属的记录中注明。
- **非二元方法与来源。** 没有替 Ren 选择接续或 living 的读法，AI 论证都有标注，Ren 的原话引用准确。问题在于 I7（对方法检查的说法过强）与 I10（把单层表示的省略呈现为交给 Ren 的二选一）。

**Summary (English).** Every Lean declaration of P11b and P12 recompiles from the prelude outside the repository, and the 19 core modules have empty axiom reports. The receipt `20261009T045039.065929Z` (422 theorems, 760 declaration audits, a core closure of 19 modules), the record hashes and the aliases are correct. The mathematics is accepted, and no mathematical error was found. 780 declarations were audited and none depends on any axiom: 710 core declarations, including 72 of `Identity` and 29 of `Population`, and 70 probe declarations, 41 of them theorems. The twelve findings concern the statement of premises, the prose and the correspondence.

- **P11b.** H1–H14 are closed.
  - `More.unceasing` has a third necessary premise, a flow listing each formation once (`Repeated`), and the chapter omits it (I1).
  - Its premises have no joint witness in the core; `Garden` is one (I2).
  - The flow form uses arising only to obtain recurring uptake, and a steady population needs the same replenishment (`Steady`, I3).
  - Four small residuals remain (I4).
- **P12.** The invariance lists are exact and the continuity theorems point the right way. The problems:
  - Continuity is one-sided. Read both ways, it fixes arising and undermining exactly (I5).
  - A join across a dormant step still changes a formation's class (I6).
  - "Names carry nothing" overreaches, and renaming invariance cannot check the method requirement it is said to check (I7).
  - `Depletes` does not screen arisings made by naming (I8).
  - Splits change the continuation relation, not the number of formations. Under budding, more without end forces no arising (I9).
  - The lineage dilemma comes from a single naming level (I10).
  - The succession witness's heir never lives (I11).
  - The records whose readings depend on identity do not say so (I12).
- **Ren.** No reading is chosen for Ren.

## 0. Scope, materials and method

**Object.** The state of `main` at `e5430db512144111d419743a74a941710087a455`:

- **P11b (`6106b651`).** The corrections answering H1–H14 of [BECOMING-P9B-P10-P11-REVIEW](BECOMING-P9B-P10-P11-REVIEW.md):
  - `MetAbove`, the minimum form of `UnderminingOn`, and `Stunted` (`Dependence`);
  - `UnderminingFor` and `undermining_for_zero` (`Return`);
  - `determined_dichotomy` (`Joint`);
  - in `Generation`, `Paid`→`Depletes`, `depletes_iff`, `dissipation_ceases`, `Tide`, `Recycle` and `Bloom.arises_on_rise`;
  - in `Flow`, `Taking`, `ArisesTaking`, `replenishment_recurs`, `renewing_recurs`, `Balances.replenished_over`, `Balances.renewers_over`, `Pulse`, `Cycle`, `Garden.growers_take`, `Garden.undepleted` and `Bloom.takes`;
  - the new module [Becoming.Population](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Population.lean);
  - the renamed vocabulary;
  - study §15;
  - the records becoming-stepwise-reading, becoming-return-grades, joint-difference-making, becoming-renewal-reading, becoming-dependence-dynamics, unceasing-generation-needs-renewal and more-needs-renewers.
- **P12 (`e5430db5`).** The P12 work:
  - [Becoming.Identity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Identity.lean);
  - study §16 and its English paragraph;
  - the record [identity-across-steps](../../../../theories/becoming/results/records/identity-across-steps.md);
  - in the chapter [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md), §1 "跨步的同一" (line 131) and its summary bullet (line 141), §2 "继续生成" and "更多" (lines 193–199), the §8 rows (lines 421, 423), the §9 table (lines 452–453) and the glossary (lines 492–497);
  - the records whose validation scope or limitations P12 amended.

**Isolation.** The snapshot is a `git archive e5430db5` in the reviewer's scratch directory. Nothing in the live repository or its `.git` was modified, no `make` target or repository checker was run against it, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where the previous reviews live.

**Materials** (sha256 prefixes of the snapshot files):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `a6ec86355481fd08` |
| chapter `THE-THEORY-OF-BECOMING.md` | `f88cd935570eb0bd` |
| previous review `BECOMING-P9B-P10-P11-REVIEW.md` | `aa26b8372d8c1b89` |
| `NONDUAL-METHOD.md` / `AGENTS.md` | `8c48b03a167a8909` / `da432369737e9a1f` |
| receipt `becoming-verification.json` (run `20261009T045039.065929Z`) | `a81c134959be0c10` |
| `Becoming.lean` / `check_becoming.py` | `c2e3d73d863879ff` / `145bb21437f2ef47` |
| `Becoming/Identity` / `Population` | `949f2daa560f57a9` / `e8570df9baa4085d` |
| `Becoming/Generation` / `Flow` | `a166e615429bee37` / `87076627398d5a5d` |
| `Becoming/Dependence` / `Joint` / `Return` | `327bfe27ba666e55` / `fd6264879ce9bbb1` / `371bfe39b12593d0` |
| `Becoming/Bridge` (unchanged) | `33f961da3d4ecaa9` |
| records identity-across-steps / more-needs-renewers / unceasing-generation-needs-renewal | `dd3795dae96dcd4c` / `bf429984b98ee290` / `14c8486ba2187ef5` |
| records becoming-stepwise-reading / becoming-return-grades / joint-difference-making | `7cb9874e3ddb2592` / `fc13474e284216c5` / `aa85d8e028784634` |
| records becoming-renewal-reading / becoming-dependence-dynamics / substitution-preserves-consumption | `bb900bfeb5c5d0bd` / `7d469b8a9a38f122` / `405afef233799424` |

**Read in full:**

- AGENTS.md;
- study §15, §16 and the English P11b and P12 paragraphs;
- the previous review;
- `Identity` and `Population` in full, and the P11b changes to `Dependence`, `Return`, `Joint`, `Generation` and `Flow`, from the diffs `c48ec435..6106b651` and `6106b651..e5430db5`;
- the nine record JSONs above;
- the chapter sections listed;
- the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md).

**Ren's words read**, for provenance:

- [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) (`740126fcca587edb`);
- [以关系结构分开更新型与消耗型形成](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md) (`a12a64304d9cb974`);
- [the pure core](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md) (`f7d31d6df74b8d8a`);
- the vocabulary corrections, [recipient, money, pay](../../../../sources/15-codex-theory-conversations/2026-10-06-foundational-vocabulary-correction.md) (`222d407ab761a945`) and [付费记录](../../../../sources/15-codex-theory-conversations/2026-10-06-nondual-core-tree-continuation.md) (`65a9677dfe6ff0ba`).

**No external literature was read.** Budding, cell division, dormancy and seed banks are mentioned from the reviewer's prior knowledge, as kinds of cases, not as evidence.

**Recompilation.** The committed bytes were compiled in the receipt's order with Lean 4.29.1 (commit `f72c35b3`), using `LEAN_PATH=<build> lean -o X.olean X.lean`.

- **Core.** `GenerativeCore` (with `import Std` removed, as the checker does), `InquirySufficiency`, `RelationalRenewal`, `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Population, Identity, Metaethics, Ranking, Correspondence}` and `Becoming`. All 19 modules exit 0 from the prelude, without warnings.
- **Bridge.** In a second directory, the 12 periphery modules that `Becoming.Bridge` imports and the bridge itself also exit 0, for 32 modules in all.

The checks:

- **Receipt.** The status is `passed`, with Lean 4.29.1 `f72c35b3` and `core_compiles_from_prelude: true`. `core_closure` lists 19 modules, and all 32 `source_sha256` entries equal the snapshot files.
- **Counts.** `theorems` per module in the receipt:
  - Frame 11, Inquiry 6, Renewal 6, Dependence 53, Return 29, Horizon 14;
  - Joint 21, Substitution 7, Generation 30, Flow 58, Population 20, Identity 46;
  - Metaethics 35, Ranking 27, Correspondence 25, Bridge 34.

  That makes 422 theorems. The 15 spine modules have 710 declarations, and with Bridge's 50 that makes 760, as the receipt, the chapter's §9 table and the records state.
- **Records.** The `references` hashes of all 14 records changed in `c48ec435..e5430db5` equal the snapshot files, and every proof binding's `sha256_pointer` equals the bound source's hash. The `reviewed_at_utc` stamps are:
  - 04:41:28Z for the P11b-corrected records, before the P11b commit at 04:46:24Z;
  - 04:55:29Z for identity-across-steps, before the P12 commit at 04:58:06Z;
  - still 00:55:55Z for becoming-renewal-reading and becoming-dependence-dynamics (I4).
- **Names.**
  - `Aliases.lean` (sha256 `2bc28a89957513df…`) runs `#check @` on all 238 aliases of the 14 records. 207 resolve in the core.
  - `AliasesBridge.lean` (`60115ff958c74a45…`) resolves 26 more through `Becoming.Bridge`.
  - The remaining five are the same theorems of the unrebuilt Mathlib periphery (`CorrectionInquiry`, in becoming-spine-instances) that the previous review reported.
  - A pass over all 585 qualified declaration names in those records' `references` resolves 574. The other 11 are declarations of `CorrectionInquiry`, `CorrectionBoundary` and `ObservationChange` in the Mathlib periphery. They include `Becoming.cell` and are all cited by becoming-spine-instances, whose P11b and P12 changes were validation scope only.
- **Axioms.**
  - `CoreAudit.lean` (`c4f3c0c432e90bf9…`, 710 lines generated from the receipt) prints the axioms of every declaration of the 15 spine modules.
  - `ProbeAudit.lean` (`6bb62128b3f34624…`) prints the axioms of every probe declaration (70).
  - All 780 report "does not depend on any axioms".
  - Lean 4.29.1's `Nat.succ_ne_zero` reports `propext`, so the probes use a local `succ_ne_zero` proved by `Nat.noConfusion`. The core does not use it.

**Probes.** Two files import the unchanged `Becoming` and compile with exit 0 and no warnings:

| File | sha256 prefix | Theorems | Defs / inductives / instances |
|---|---|---|---|
| `P11bProbes.lean` | `35dc0d8956dddf50` | 6 | 5 |
| `P12Probes.lean` | `a8f00c8dff188670` | 35 | 24 |

The probes avoid `simp` and `omega`. `decide` is used only on closed numeral (in)equalities.

The probes are minimal models that satisfy the published definitions unchanged. Following the nondual method, they show what the definitions admit, not what actual systems usually do. Where a fuller account would exclude a probe, the relation that excludes it is one the representation omits; the probe does not refute the theory. A probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels.**

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose is stronger than the Lean, including a stated theorem with a premise left out.
- *missing counterexample*: a relevant witness is absent from the comparison or the record. This includes a positive witness of joint satisfiability.
- *presentation*: wording, provenance or bookkeeping.

No finding is an *error*.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P11b: are H1–H14 closed? | **All fourteen are closed.** The minimum form is adopted, and `Stunted` is a theorem. `determined_dichotomy` and the root doc are corrected. `Depletes` and `depletes_iff` state the content of the old premise. The flow form `ArisesTaking` ties the premise to the arising formation. `dissipation_ceases` states its premise. `More.unceasing` proves the implication under a census. `Taking` is added; minimum uptake is disclosed; the averaged theorems and `Pulse`, `Cycle` and the H14 boundary are in place. Four residuals remain: a necessary premise omitted in the chapter, a missing joint witness, the idle arising in the flow form, and bookkeeping. | I1–I4 |
| 2. P11b: are `Population` and the flow form correct and faithfully glossed? | **Correct; mostly faithful.** `arises_of_more`, `unceasing_of_growth` and `More.unceasing` hold as stated, and `Dormant`, `Inactive` and `Crowd` show what they claim. **The chapter states `More.unceasing` without the premise that `present` lists each formation once**; with only that premise missing, the conclusion fails (`Repeated`). `replenishment_recurs` is true, but its proof discards `Arises`: the content is that recurring uptake needs recurring replenishment, which a steady population of takers meets as well. | I1, I2, I3 |
| 3. P12: is the list "preserved by every re-identification" exact? Does "names carry nothing" overreach? | **The list is exact**: each item is proved, and each reading left off it is changed by `Turnover`. "改名保持全部读法" goes beyond the five `rename_*` theorems, and **"names carry nothing" overreaches**. The cross-step pattern of names carries identity, which P12 itself shows to be substantive. Renaming preserves that pattern by construction, so renaming invariance cannot check the method requirement against smuggling by naming. | I7 |
| 4. Are `KeepsActive` and `KeepsTenure` the right continuity readings, and do the theorems run the right way? | **The directions are right**: keeping continuing activity can only hide arising, and keeping continuing dependence can only add undermining. **The readings are one-sided**, relative to a reference naming. Read in both namings, they fix arising and undermining exactly; this answers the record's open converse. Neither reading constrains a formation's class over the run, even both ways: joins across a dormant step change it. | I5, I6 |
| 5. Do `Lineage` and `Succession` keep continuity as claimed? | **One way only.** The joined naming keeps the apart naming's continuities; the apart naming does not keep the joined naming's (`lineage_one_way`, `succession_one_way`). `Lineage` has no relations besides activity, and `Succession`'s heir never lives. The conclusions survive a heir that lives (`ActiveHeir`). | I5, I10, I11 |
| 6. Is `More.unceasing_reidentified` non-vacuous, and what does it say? | **Non-vacuous**: `Garden` meets every premise, so its generation is unceasing under every re-identification. It says that, **for one-to-one identity**, the arising that more forces is not an artefact of naming. It does not hold "under every reading of identity": with budding read as continuation, the same growth forces no arising. | I2, I9 |
| 7. Is the boundary for splits and merges stated correctly? | **No.** Splits do not "change the number of formations"; per-step counts are fixed by each step's relations. They change the continuation relation from one-to-one to one-to-many, and that exclusion carries the census result. | I9 |
| 8. Is the effect on P10 stated correctly? | **The conclusion is right, and one of its two reasons is not general.** `Unceasing.rises` is unaffected because its conclusion concerns conditions only. That arisings made by naming fail `Depletes` is a property of `Turnover`: with the moon's and the flicker's names exchanged, `Tide.still` meets every premise of `regeneration_recurs` with arisings made by naming alone. | I8, I12 |
| 9. Nondual method; provenance; choices made for Ren | **No outside source or independent owner is introduced, and no reading of succession, 生生不息 or `living` is chosen for Ren.** The AI arguments are labelled, and Ren's words are quoted exactly. Two framing issues remain. The method check is overstated (I7). A single-level representation's omission of part and whole is presented as an either/or for Ren, with an unsupported "falls under maintenance and renewal", and without noting the "不断创造" of Ren's quoted words (I10). | I7, I10 |
| 10. Records, receipt and counts | **Counts, run, closure, hashes, aliases and bindings are correct** (422 / 760, run `20261009T045039.065929Z`, 19 modules). Corrections are needed in identity-across-steps (I5–I10), more-needs-renewers (I1–I3), unceasing-generation-needs-renewal (I3, I8, I12), becoming-stepwise-reading and becoming-renewal-reading (I12), and two bookkeeping items (I4). | I1–I12 |

**Status of H1–H14.**

| Item | Status | Evidence |
|---|---|---|
| H1 | closed | `MetAbove`, the minimum `UnderminingOn`; `Stunted.stunting_undermines`; the P9b exclusions kept; `RisingNeed` disclosed as a choice. Docstring wording in I4. |
| H2 | closed | Root doc corrected; `Joint` doc adds the third case; `determined_dichotomy`. |
| H3 | closed | Both residual sentences corrected; `reviewed_at_utc` not refreshed (I4). |
| H4 | closed | `Depletes`, `depletes_iff`, `Tide.unrelated_depletion`, `Bloom.arises_on_rise`; the tied version is the flow form `ArisesTaking`. The name still says depletion (I4). |
| H5 | closed | `Tide.renewal_without_arising` for strictness; `Garden.undepleted`; flow form `replenishment_recurs`, `renewing_recurs`. What the flow form uses is in I3. |
| H6 | closed | `dissipation_ceases`; premise stated; `Recycle.closed_unceasing`. |
| H7 | closed | `Arises` labelled as one formal carrier, in the author's reading; "以消耗为条件的生起". |
| H8 | closed | `Flow.More.unceasing`; `Bloom.counted`; `Dormant`, `Inactive`; "hierarchy" narrowed. Third premise omitted in the chapter and without a necessity witness (I1); no joint witness (I2). |
| H9 | closed | `Flow.Taking`; `Crowd.drawing_without_taking`; the gloss narrowed. |
| H10 | closed | Minimum uptake stated in the record, §14 and the chapter. |
| H11 | closed | `Pulse.pulsed`; `Balances.replenished_over`, `renewers_over`; "越来越多" in the averaged sense only. |
| H12 | closed | Claim withdrawn; `Cycle.closed_more`; dissipation premise named. |
| H13 | closed | Renames carried out and listed; residual "giver" wording (I4). |
| H14 | closed | Boundary sentence on life as a condition of life. |

## 2. Findings

### I1. overclaim (omitted premise) and missing counterexample: `present` without repetition is a third necessary premise of `More.unceasing`

**Location.**

- Chapter §2 "更多" (line 197): "在活跃形成的普查之下，只有活跃的形成取用、且只从它汲取的条件取用时，不止地更多蕴含不息的生成（`More.unceasing`）……没有普查，或取用者从不活跃时，不止地更多可以没有任何生起". English (line 199): "Under a census of active formations, with only active formations taking from what they draw on, more without end implies unceasing generation, strictly; without the census or with inactive takers it does not."
- Chapter §1 "跨步的同一" (line 131): "在活跃形成的普查之下，由“更多”迫使的不息在每种命名下成立". This omits both the distinctness of `present` and `Taking`.
- Study §15.1 H8 and §15.2 give necessity witnesses for the census (`Dormant`) and `Taking` (`Inactive`) only.

**What the Lean says.** `Flow.More.unceasing` (Population.lean:161) takes `census`, `distinct : ∀ t, Distinct (L.present t)`, `taking` and `more`. The record more-needs-renewers and §15.1 state the second premise; the chapter does not.

**Evidence.** `Repeated.more_without_arising`. One formation is always active, and a census lists it. The flow lists it `t` times at step `t`, each entry taking one unit and giving one back. The flow balances, only active formations give and take, and only from what they draw on. Generation is more without end, and nothing ever arises. Only `distinct` fails.

**Why it matters.** As written, the chapter's sentence is false of the definitions: `Repeated` meets its premises and not its conclusion. The premise is not a technicality. Where a flow is read from records, one formation can appear in several entries: an aggregate split by source, or a formation recorded once per condition. Counting entries then counts one living formation many times.

**Correction.**

- Chapter zh: "在活跃形成的普查之下，流的 `present` 每步每个形成只列一次，只有活跃的形成取用时，不止地更多蕴含不息的生成……没有普查、`present` 有重复、或取用者从不活跃时，不止地更多可以没有任何生起（`Dormant`、`Repeated`、`Inactive`）". Make the same change in English.
- §1 bullet: "在普查、`present` 不重复与 Taking 之下".
- Move `Repeated` into `Population` beside `Dormant` and `Inactive`, and list it in more-needs-renewers' counterexamples.

### I2. missing counterexample (joint witness): no core witness meets every premise of `More.unceasing`

**Location.** `Becoming.Population`; `Flow.More.unceasing_reidentified` (Identity.lean:299); records more-needs-renewers and identity-across-steps.

**What the Lean says.** Each core witness misses at least one premise:

- `Bloom.counted` meets the census, distinctness and `Taking`, but not `More`.
- `Dormant` has no census.
- `Inactive` has no `Taking`.

`Garden.more` proves `Unceasing ∧ More` directly, but there is no census theorem for it. So no core declaration shows that the four premises of `More.unceasing` hold together.

**Evidence.**

- `GardenCensus.census`, `GardenCensus.distinct`, `GardenCensus.everywhere`: the garden's active formations are listed once at each step, its flow lists each once, and with `Garden.growers_take.1` and `Garden.more` every premise of `More.unceasing_reidentified` holds. Its generation is therefore unceasing under every re-identification.
- `Budding.growth_without_arising` (first five conjuncts) gives the same for `Cycle`.

**Why it matters.** A theorem whose premises are never shown to hold together could be vacuous. Here they do hold together, so the implication is substantive, and the record can say so.

**Correction.** Add `Garden.census` and `Cycle.census` to the core, and cite them as positive instances in §15.2, §16 and both records.

### I3. overclaim: in the flow form, arising contributes only recurring uptake

**Location.**

- `replenishment_recurs` (Flow.lean:310–328), docstring "Unceasing generation of formations that take needs replenishment".
- Study §15.4 rebuttal 2 (line 873): "`ArisesTaking` 的内容正在于这一联系：生起的形成本身在其第一个活跃步从家族取用".
- Chapter §2 "继续生成" (line 193): "平衡的流给出不需要净上升的形式：在第一个活跃步从家族取用的形成不息地生起时，补充与补充者在任意晚的步出现". The §8 row (line 423): "在平衡的流中，取用者不息地生起需要补充复现".
- Record unceasing-generation-needs-renewal, flow form.

**What the Lean says.** In the proof of `replenishment_recurs`, the pattern `⟨t, _, later, _, present, takes⟩` discards the `Arises` component of `ArisesTaking`. The proof uses only this: at arbitrarily late steps some formation listed in `present (t + 1)` takes from the family, so uptake is positive at arbitrarily late steps.

**Evidence.**

- `uptake_needs_replenishment`: in a balanced flow, positive uptake at arbitrarily late steps needs replenishment at arbitrarily late steps; no arising is mentioned. `replenishment_recurs_from_uptake` derives the premise and conclusion of `replenishment_recurs` from it.
- `Steady.steady`: a consumer and a renewer, both always active. The flow balances, only active formations give and take, and only from what they draw on; activity needs support. Uptake is positive at every step, nothing ever arises, and replenishment recurs.

**Why it matters.** The theorem and its gloss are true. But it is presented as the flow form of "continuing generation needs renewal", and rebuttal 2 places its content in the link between arising and taking. Its content is a conservation statement: a finite family that keeps being taken from must keep being replenished. Maintaining a constant population of takers needs this just as much. What separates generation from maintenance here is strictness (`Tide.renewal_without_arising`), not the need for replenishment. For the theory's message this matters: renewal is needed by continuing uptake, whether that uptake comes from generation or from maintenance.

**Correction.**

- Add `uptake_needs_replenishment` to `Flow` as the general theorem, and derive `replenishment_recurs` from it.
- Gloss: "在平衡的流中，任意晚的步上有正的取用，就需要任意晚的步上有补充；取用的形成不息地生起是其一种情形，恒定的取用者群体是另一种（`Steady`）".
- Rebuttal 2: replace "部分对" with "对：生起只经由它带来的取用起作用；`ArisesTaking` 把生起与取用连起来，使定理可以读作关于生成的定理，但定理所用的只是取用".

### I4. presentation: four P11b residuals

- **(a) The name `Depletes`.** By `depletes_iff`, the premise holds at an event step exactly when some condition of the family changes; a rise counts. `Bloom.arises_on_rise` shows every bloom arising at a rise, where the premise holds with nothing depleted. Rebuttal 4 says the content is now stated, which is true, but the name still says depletion. A literal name such as `FallsWhenStill` would match the definition (Generation.lean:109–112). Ren chooses the name.
- **(b) The `MetAbove` docstring** (Dependence.lean:315–317) says the dependence "has held without a break". The definition asks only that `requires` hold at each step of the tenure; the dependence may be `Broken` within it. Write "held at every step, met or not".
- **(c) `Taking` in `More.unceasing`.** `More.unceasing` uses only the activity half of `Taking` (Population.lean:167, `.1`). The chapter and the record list "且只从它汲取的条件取用" as a premise. Say that only "only active formations take" is used.
- **(d) H13 residuals.** Flow.lean:46 has "every giving costing the giver's conditions more than it gives". The receipt's scope text has "every rise is made by an active giver" and "the givers grow". more-needs-renewers' `next_delta` has "每次给予都使给予者付出多于所给". The rename 给予者 → 补充者 is not complete. "Giving" is not payment vocabulary, so this is consistency only.
- **(e) A stale timestamp.** becoming-renewal-reading changed its `correspondence` in P11b (H3), but its `reviewed_at_utc` stays 00:55:55Z.

### I5. overclaim: continuity is one-sided; read in both namings, it fixes arising and undermining exactly

**Location.**

- Identity.lean:59: "Both namings in each witness keep every continuing activity and dependence." Also :43–51 and :65–67.
- Study §16, bullet "连续排除什么" (line 927): "两个定理各有一个方向，反方向的反例恰是接续". Also rebuttal 2 (line 935).
- Record identity-across-steps: `limitations` ("each continuity theorem has one direction") and `next_delta` ("under what added conditions the converse of each continuity theorem holds").
- Chapter §1 (line 131) and glossary 连续 (line 496).

**What the Lean says.** `KeepsActive σ W` constrains σ relative to `W`'s naming: a formation that `W` takes as continuing keeps its new name. Nothing constrains a name that continues only under the new naming. The reference naming is thus privileged, and the new naming may join where the old one did not.

**Evidence.**

- `lineage_one_way`: `Lineage.one` keeps the apart naming's continuing activity. The apart naming, read back from the one-naming (`inv Lineage.one`), does not keep the one-naming's continuing activity: the lineage is active at every step, and no member is active at two successive steps.
- `succession_one_way`: the same holds for `KeepsTenure`.
- `arises_iff_of_keepsActive_both` and `unceasing_iff_of_keepsActive_both`: suppose σ keeps `W`'s continuing activity and `inv σ` keeps the re-identified web's. Then `x` arises at `t` under the new names exactly when `σ.old (t + 1) x` arises under the old, so `Unceasing` is exactly preserved.
- `metAbove_of_inverse_keepsTenure` and `undermining_of_inverse_keepsTenure`: if `inv σ` keeps the new naming's continuing dependences, undermining under the new names is undermining under the old. With `undermining_of_keepsTenure`, undermining is exactly preserved.

**Why it matters.** "Both namings keep every continuing activity and dependence" reads as symmetric, but it holds one way. The witnesses depend on that asymmetry. A one-sided condition lets the new naming create a continuity, by joining, but never remove one. Read symmetrically, so that the two namings agree on which formations continue, same-step succession is excluded and arising and undermining are fixed. That succession "remains open" is a consequence of choosing the one-sided reading. Both are readings, and the choice should be stated. This also answers the record's open converse.

**Correction.**

- Identity.lean:59: "In each witness the joined naming keeps every continuing activity and dependence of the apart naming; the apart naming does not keep the joined naming's (`lineage_one_way`, `succession_one_way`)."
- Add the four theorems above to `Identity`.
- Study and record: "两向保持连续时，生起与侵蚀恰被保持；单向时，新命名可以制造连续（接起来），不能去掉连续。接续开放，是因为连续取单向的读法".
- Close the `next_delta` item.

### I6. missing counterexample: under continuity in both namings, joining across a dormant step changes a formation's class

**Location.**

- Identity.lean:48–51: "Such a re-identification can still join a formation that ends at a step with one that begins there: whether the one that begins continues the one that ends is succession."
- Study §16, bullet "连续排除什么" (line 927), and rebuttal 2 (line 935): "排除这类改认后剩下的只有接续".
- Glossary 接续 (line 497): "把在某步终结的形成与在该步开始的形成接为同一个".
- Chapter §1 (line 131): "剩下的是接续". Summary bullet (line 141): "continuity of activity and dependence leaves only succession open".

**What the Lean says.** `KeepsActive` and `KeepsTenure` constrain names only across a step at which a formation is active, or depends, on both sides. Across a step at which a formation is inactive and depends on nothing, nothing is constrained.

**Evidence.** `Dormancy` has three formations:

- `early` is active at step 0 only, needs one unit of a spring that holds one unit, and draws it;
- `late` is active at step 2 only and draws the pool;
- `needy` needs two units of the pool at step 0.

The web is `Dependent` (`dependent`). `join` gives `late` the name `early` from step 1 on.

- `keeps_both`: `join` keeps every continuing activity and dependence, and so does its inverse. No formation continues across any step under either naming, so the conditions hold trivially, and that is the point.
- `classes`: named apart, `early` renews in the run and `late` consumes. Joined, the formation named `early` consumes and does not renew.

**Why it matters.** A formation's class over the run, renewing or consuming, is the central object of the relational reading. P12 correctly says it depends on identity, and it offers continuity as constraining identity "up to succession". Yet continuity does not constrain the class at all, in either reading, and not only through same-step succession. Dormancy, seed banks, hibernation, seasonal return and resumed practices are ordinary cases of this. "剩下的只有接续" holds only if succession includes joins across any number of inactive steps.

**Correction.**

- Glossary 接续: "把在某步终结的形成与在该步或其后开始的形成接为同一个（中间可以有不活跃、不依存的步，例如休眠）".
- Identity.lean:48–49: "join a formation that ends with one that begins at that step or later".
- Add: "连续不约束形成在整段上的类：两向保持连续的改认仍可改变它（`Dormancy`）". Move `Dormancy` into `Identity` as a witness.

### I7. overclaim (nondual method): "names carry nothing"

**Location.**

- Identity.lean:16: "Names carry nothing. A renaming preserves …".
- Study §16 Delta (line 894): "改名保持追随形成的全部读法". Interpretation (line 924): "名字不承载本体。改名保持全部这些读法：形式变量只经由它们的关系起作用。这是方法要求“不能以分别命名偷渡独立本体”在这一表示中的一个检查".
- Chapter §1 (line 131): "改名保持全部读法：名字不承载任何东西". Summary bullet (line 141): "names carry nothing".
- English summary (line 1051): "A renaming preserves every reading, so names carry nothing."
- Record identity-across-steps: the `title`, and the `correspondence` ("Invariance under renaming is also a check, in this representation, of the method requirement …").

**What the Lean says.** The five `rename_*` theorems show five readings invariant under a bijection constant across steps. Rebuttal 1 rightly calls this an instance of a metatheorem: relationally defined predicates are invariant under isomorphism.

**Evidence.** The chapter sentence that says "名字不承载任何东西" begins "一步的哪个形成延续前一步的哪个，由表示的命名规定". `Turnover` shows that the cross-step pattern of names carries the class, tenure, undermining, transformation and arising. A renaming preserves that pattern by construction, which is why it changes nothing. What is shown, then, is that the choice of labels is idle once the pattern is fixed. Through their pattern across steps, the names carry identity. "全部读法" and "every reading" also go beyond the five theorems: a reading that names a particular formation ("the moon renews the tide") is invariant only if its referent is renamed with it.

**Why it matters.** The method requirement guards against an independent entity entering through separate naming. In this representation, that can happen in two places: the cross-step pattern of names (identity) and the sort split of formations and conditions (H14). Renaming invariance can detect neither, because renaming preserves both. To call it a check of the method gives an assurance it cannot give. The check P12 actually performs is `Turnover`, together with the disclosure that the index type supplies identity (Identity.lean:68–70). That deserves the name.

**Correction.**

- Replace "names carry nothing / 名字不承载任何东西" with "labels carry nothing / 标签不承载任何东西: a renaming preserves every reading defined from the relations (checked for five)".
- Add: "名字跨步的模式承载同一。这是表示给出的对应前提，`Turnover` 表明它是实质的；方法要求在这里的检查是这一披露，不是改名不变".
- Change the record title accordingly.

### I8. missing counterexample: arisings made by naming alone can meet every premise of `Unceasing.regeneration_recurs`

**Location.**

- Study §16, bullet "对 P10 的影响" (line 929): "它的前提 Depletes 要求……而 Turnover 中单由改认制造的生起不降低任何条件，Depletes 不成立，定理不适用".
- Identity.lean:41–42.
- Record identity-across-steps: `dependencies[1].detail` ("arisings made by re-identification alone, lowering no condition, do not meet Depletes") and `counterexamples[0]`.

**What the Lean says.** `Depletes` (Generation.lean:111) requires that at each event step at which no condition of the family rises, one falls. By `depletes_iff`, this says that some condition of the family changes. It is not tied to the arising formation (H4).

**Evidence.** `TideFlip.naming_meets_premises`. `Tide.still` has no arising. `flip` exchanges the names of the moon and the flicker at odd steps, which breaks the moon's continuing activity. The flipped web:

- is `Dependent`;
- is `RenewedBy` the moon's renewing, carried to the new names;
- meets `Depletes` for its arisings, since the tide changes at every step;
- is `Unceasing`.

So `Unceasing.regeneration_recurs` applies, and its conclusion holds. Every arising in this web is made by the naming.

**Why it matters.** The study gives two reasons why P10 is unaffected. The first, that the conclusion concerns conditions only, is correct and sufficient. The second is a property of `Turnover`, not of naming; read generally, the record's sentence ("naming-made arisings do not meet Depletes") is false. Together with I3 and H4, this shows what the P10 theorems need: conditions that change, or uptake that recurs. The "generation" in their premises may be an artefact of naming. What excludes naming artefacts is a naming that keeps continuing activity relative to a reference naming (`arises_of_keepsActive`), not `Depletes`.

**Correction.**

- Replace the second reason: "`Depletes` 不系于生起的形成，不筛掉命名的产物（`TideFlip`）。定理不受影响，是因为结论只关乎条件；它的前提 `Unceasing` 依赖同一，要把它读作关于生成的定理，需要命名保持持续的活动（`arises_of_keepsActive`）".
- Restrict the record's dependency detail to `Turnover` ("in `Turnover` those arisings lower no condition and `Depletes` fails"), and add `TideFlip` as a counterexample.

### I9. overclaim: "unceasing under every reading of identity"; splits do not change the number of formations

**Location.**

- Identity.lean:12–13: "Splits and merges, which change how many formations there are, are not re-identifications". Also :29–30 ("the arising it forces is not an artefact of naming") and :67–68 ("Where generation is more without end under a census, it is unceasing under every reading of identity").
- Study §16 (line 888): "分裂与合并改变形成的数目，不是改认". Interpretation (line 925): "不息本身依赖同一……由“更多”迫使的不息却不依赖". Rebuttal 3 (line 937).
- Record identity-across-steps: `hypotheses[0]` ("splits and merges change the number of formations and are not covered"); `claim` ("它所迫使的生起不是命名的产物"); `next_delta` ("the form of 'more implies unceasing' under splits and merges").

**What the Lean says.** Re-identification preserves the number of active formations at each step (`Census.reidentify`). So does any reading of identity, since the per-step count is a per-step relation. In a split, one formation at `t` is continued by two at `t + 1`. That changes the continuation relation, from a bijection to a one-to-many relation; it changes the number of formations at no step. A one-to-one naming must count one of the two as arising.

**Evidence.**

- `ArisesFrom W R t f`: `f` is active after the step and continues no formation active before it, under a continuation relation `R`. `arisesFrom_self`: with `R` the identity, this is `Arises`.
- `Budding.growth_without_arising`. In `Cycle`, formation `n` is active from step `n + 1` on. The census, a `present` without repetition, `Taking`, `More [()]` and `Unceasing` all hold. Let `R t g f := g = f ∨ g = 0`, so that every new formation buds from formation 0. Then no formation arises after step 1.

**Why it matters.** For one-to-one namings, the claim that the arising forced by `More` "is not an artefact of naming" is true, and it is the substance of `More.unceasing_reidentified`. Under every reading of identity, it is not true. A reading on which one formation continues as several absorbs the growth without arising; budding, clonal growth and cell division are such cases. What survives every reading is the count: ever more formations active. The stated reason for excluding splits is mistaken, and it hides that the exclusion carries the result. This answers the record's `next_delta` item: under splits, more does not imply arising.

**Correction.**

- Identity.lean:67–68: "under every one-to-one reading of identity".
- Identity.lean:12–13, the study and the record hypothesis: "Splits and merges, in which one formation continues as several or several as one, are not re-identifications; they change the continuation relation, not the number of formations at any step".
- Add: "在把新形成读作既有形成的延续（萌出、分裂）的读法下，不止地更多不迫使任何生起（`Budding`）；迫使的是活跃形成的数目没有界".
- A theorem for every continuation relation in which no formation continues as two (merges allowed) is argued by pigeonhole but not formalized here (§4, item 6).

### I10. presentation (nondual method; provenance): the lineage AI argument

**Location.**

- Study §16, the AI argument (line 928): "一个谱系的成员交替生起：分开命名是不息的生成，作为一个命名是一个形成的持续。“生生不息”若读作谱系的持续，它落在维持与更新上；若读作成员不断生起，它落在 §13 的不息上……这两个选择属于 Ren".
- The same in the record's `correspondence`.
- Identity.lean:66–67: "whether a lineage is one formation continuing or many generated … is a further reading".

**What the Lean says.** `Lineage.web` has level 0 and no `requires` or `draws`; only activity alternates.

**Evidence.**

- `Lineage` has no conditions. Under the one-naming, the lineage's `RenewingIn` holds vacuously, and nothing is maintained or renewed. "落在维持与更新上" is not shown.
- `Layered.both`: name the lineage itself as a formation beside its members. Then one web has the lineage active at every step and its members arising without end. The web cannot say that the lineage is constituted by its members: `Web` has no part–whole relation.
- Ren, 2026-10-07: "我的答案是生生不息 - 一种整体的，不断创造更多生的方向……" ([source](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)).

**Why it matters.** The either/or comes from a single naming level: one index type cannot name both the lineage and its members. Under the nondual method, that is a relation the representation omits, part and whole in one unfolding. It should be disclosed as an omission, not offered as a choice between persistence and generation. Offering "a lineage's continuation" as a reading of 生生不息 also sets aside the "不断创造" of Ren's quoted words, without noting this. The study rightly leaves the choice to Ren and labels the argument. The issue is how the choice is framed.

**Correction.** Replace the AI argument with: "谱系与成员是同一展开的两个层次：作为整体的谱系持续，正由成员不息地生起而成（`Layered`）；单一命名层次只能表示其一。部分与整体的关系是这一表示所省略的关系。把“生生不息”读到谱系、成员或两者的层次，属于 Ren；只读作持续与 Ren 原话中的“不断创造”之间的张力，应写明". Drop "落在维持与更新上", or show it in a witness with conditions.

### I11. presentation (witness strength): `Succession`'s heir never lives

**Location.** Identity.lean:636–637 ("the heir is never supported and never active") and :55–58; the study's `Succession.readings` row.

**What the Lean says.** The heir requires the pool from step 1, at need 2, and is never active; its dependence is never met.

**Evidence.** `ActiveHeir.readings`:

- the heir is active at step 1 and supported there (need 1, pool 1), and needs 2 from step 2;
- the web is `Dependent`, and `succeeds` keeps every continuing activity and dependence;
- named apart, no draw from step 1 on undermines;
- with the heir succeeding the elder, every draw from step 2 on undermines.

**Why it matters.** With a heir that never lives, the inheritance witness looks like an artefact of a formation that never takes part. The phenomenon survives with a heir that lives and is supported, so the claim stands and the witness can be stronger.

**Correction.** Replace `Succession` with `ActiveHeir`, or add `ActiveHeir` beside it.

### I12. presentation (propagation): records whose readings depend on identity do not say so

**Location.** Three records state readings that P12 shows depend on identity across steps:

- unceasing-generation-needs-renewal: `Unceasing`;
- becoming-stepwise-reading: the tenure, undermining and stepwise `living`;
- becoming-renewal-reading: `RenewingIn` and `ConsumingIn`.

A fourth, more-needs-renewers, concludes `Unceasing`; that conclusion is invariant only under one-to-one identity (I9). P12 added pointers to identity-across-steps only in becoming-dependence-dynamics and substitution-preserves-consumption. The four above changed only their validation scope.

**Why it matters.** The canonical record governs the summaries. A reader of unceasing-generation-needs-renewal finds no mention that a naming can make or remove `Unceasing`, and no mention that its premise `Depletes` does not exclude this (I8).

**Correction.** Add one limitation sentence to each, pointing to identity-across-steps. For example: "`Unceasing`（形成的类；任期与侵蚀）依赖跨步的同一（identity-across-steps）；保持持续活动的命名不制造生起".

## 3. What remains sound

- **The theorems.** Every P11b and P12 theorem holds as stated. The proofs check, and the axiom reports are empty in the 19-module core recompiled from the prelude. The counts, receipt, hashes, aliases and bindings are correct.
- **P11b.**
  - The minimum form of undermining keeps the P9b exclusions and counts `Stunted`. The rising-need choice is disclosed with its cost.
  - `determined_dichotomy`, `depletes_iff`, `dissipation_ceases`, `Recycle`, `Tide.renewal_without_arising` and `Bloom.arises_on_rise` are correct and correctly glossed.
  - The averaged theorems, `Pulse` and `Cycle` are correct, and "越来越多" is kept only in the averaged sense.
  - `arises_of_more`, `unceasing_of_growth` and `More.unceasing` are correct. Strictness by `Bloom.counted` is correct, and `Dormant`, `Inactive` and `Crowd` show what they claim.
  - The practice of moving probe content into the core as theorems continues.
  - The vocabulary renames follow Ren's corrections, and the names are left for Ren to settle.
- **P12.**
  - `Reidentify` is well defined. Both `Web.reidentify` and `Flow.reidentify` keep every step's relations.
  - Every item of the "preserved by every re-identification" list is proved. Every reading said to depend on identity is changed by `Turnover`, whose relations at each step are unchanged and whose activity still needs support.
  - `Census.reidentify`, `Taking.reidentify` and `reidentify_more` are correct.
  - `arises_of_keepsActive`, `unceasing_of_keepsActive`, `Reidentify.steady`, `metAbove_of_keepsTenure` and `undermining_of_keepsTenure` are correct and point in the stated directions.
  - The boundary sentences are accurate where they speak of one-to-one correspondence. These are "连续是一种同一的读法，不是同一的定义", "接续怎样读属于 Ren", "不处理分裂与合并" and "不说哪个形成生起".
  - Rebuttal 5, that the census result trades identity for a count, is exactly right and is what I9 builds on.
- **Method and provenance.**
  - No source outside the unfolding is introduced.
  - The representation's supply of identity through the index type is disclosed as a correspondence claim.
  - Ren's words are quoted exactly, and the readings and AI arguments are labelled.
  - The records state "尚无独立反审".
  - Neither phase states diversity, complexity or possibility, or claims an ethical ranking.

## 4. What would change these verdicts

1. **`More.unceasing`.** Stating the distinctness premise in the chapter, and moving `Repeated` and a census for `Garden` and `Cycle` into the core, would close I1 and I2.
2. **The flow form.** `uptake_needs_replenishment` in the core, with rebuttal 2 revised, would close I3. A dissipative flow theorem would make generation, rather than uptake, carry the requirement.
3. **Two-sided continuity.** The four both-ways theorems in `Identity`, with the one-sided reading named as a choice, would close I5 and the record's open converse.
4. **Dormancy.** `Dormancy` as a witness, 接续 widened to joins across inactive steps, and a sentence that continuity does not constrain a formation's class would close I6. A continuity reading that reaches across dormancy would be a new result, for example continuity of a dependence that persists while inactive.
5. **Labels and identity.** Rewording "names carry nothing" as in I7 would close it.
6. **Splits.** The one-to-one qualifier and the corrected description of splits would close I9. A theorem showing that more without end forces arising under every continuation relation in which no formation continues as two (merges allowed), with `Budding` showing that splits are what defeat it, would replace the qualifier by an exact boundary.
7. **The lineage.** Reframing it as two levels of one unfolding with part and whole omitted, and dropping or supporting "落在维持与更新上", would close I10. A representation with a part–whole relation among formations would make it a theorem.
8. **Witnesses and records.** `ActiveHeir` (I11), the limitation sentences (I12), and the residuals of I4 would close the rest.
9. **Ren's choices.** These stay open:
   - the reading of succession;
   - whether 生生不息 is read at the level of the lineage, of its members or both;
   - whether a tenure continues through succession under the working reading "不侵蚀".

   None of them is settled by any finding here.

**Not checked.**

- The Mathlib periphery (`CorrectionInquiry`, `CorrectionBoundary`, `ObservationChange`) was not rebuilt. Its five aliases and eleven declaration names in becoming-spine-instances were not resolved; that record changed only its validation scope in these commits.
- `Becoming.Bridge` was recompiled, and its aliases resolve, but its 50 declarations were not individually re-audited for axioms. The receipt reports them empty.
- The generated overview pages and `make research-check` were not run, since they write into the live repository.
- No external literature was consulted.
- Parity between the Chinese and English texts was checked only for the passages quoted above.

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 against the unchanged `e5430db5` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. Both probe files compile with exit 0 and no warnings. `ProbeAudit.lean` prints the axioms of all 70 probe declarations, and every one reports "does not depend on any axioms". `CoreAudit.lean` (710 `#print axioms` lines generated from the receipt's declaration list), `Aliases.lean` (238 `#check @` lines) and `AliasesBridge.lean` (31) are mechanical and are not reproduced; their hashes and results are in §0.

### `P11bProbes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P11b and P12: the P11b part

Each probe is a minimal model satisfying the published definitions at `e5430db5`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P12Probe

open Becoming

/-! ## L1. Without `present` free of repetition, more without end comes with nothing
arising, under a census and `Taking` -/

namespace Repeated

/-- `n` entries, all the same formation. -/
def rep : Nat → List Unit
  | 0 => []
  | n + 1 => () :: rep n

/-- One formation, always active, drawing on the condition; the flow lists it `t` times
at step `t`, each entry taking one unit and giving one back. -/
def web : Web Unit Unit where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

def flow : Flow Unit Unit := ⟨rep, fun _ _ _ => 1, fun _ _ _ => 1⟩

theorem ones : ∀ n, total (rep n) (fun _ => 1) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (ones n)).trans (Nat.add_comm 1 n)

theorem census : web.Census fun _ => [()] :=
  fun _ => ⟨⟨fun mem => (nomatch mem), trivial⟩,
    fun f => ⟨fun _ => match f with | () => .head [], fun _ => trivial⟩⟩

/-- A census lists the one active formation, the flow balances, only active formations
give and take, and only from what they draw on; generation is more without end, and
nothing ever arises. The one premise of `Flow.More.unceasing` that fails is that
`present` lists each formation once. -/
theorem more_without_arising :
    web.Census (fun _ => [()]) ∧ flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧
    flow.More [()] ∧ ¬ (∀ t, Distinct (flow.present t)) ∧ ∀ t f, ¬ web.Arises t f :=
  ⟨census, fun _ _ => rfl, fun _ _ _ _ _ => trivial, fun _ _ _ _ _ => ⟨trivial, trivial⟩,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (ones t).symm)⟩,
   fun distinct => (distinct 2).1 (.head []),
   fun _ _ arises => arises.1 trivial⟩

end Repeated

/-! ## L2. The flow form uses arising only to mark steps of positive uptake -/

section Uptake

variable {F C : Type}

/-- In a balanced flow, positive uptake at arbitrarily late steps needs replenishment at
arbitrarily late steps. No arising is mentioned. -/
theorem uptake_needs_replenishment {L : Flow F C} {W : Web F C} {cs : List C}
    (balances : L.Balances W) (uptake : ∀ N, ∃ t, N ≤ t ∧ 0 < L.uptake cs t) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.replenishment cs t = 0 :=
  fun none =>
    have step : ∀ t, T ≤ t → W.stock cs (t + 1) + L.uptake cs t = W.stock cs t :=
      fun t later => (balances.over cs t).trans
        ((congrArg (W.stock cs t + ·) (none t later)).trans (Nat.add_zero _))
    falls_finitely (W.stock cs) T
      (fun t later => Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq (step t later)))
      fun N => match uptake (N + T) with
      | ⟨t, later, positive⟩ =>
        ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
          Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right positive)
            (Nat.le_of_eq (step t (Nat.le_trans (Nat.le_add_left T N) later)))⟩

/-- `replenishment_recurs` is this theorem applied to the steps after each arising:
`ArisesTaking` enters only through the positive uptake it gives. -/
theorem replenishment_recurs_from_uptake {L : Flow F C} {W : Web F C} {cs : List C}
    (balances : L.Balances W) (arising : ∀ N, ∃ t f, N ≤ t ∧ L.ArisesTaking W cs t f)
    (T : Nat) : ¬ ∀ t, T ≤ t → L.replenishment cs t = 0 :=
  uptake_needs_replenishment balances (fun N => match arising N with
    | ⟨t, _, later, _, present, takes⟩ =>
      ⟨t + 1, Nat.le_succ_of_le later, Flow.uptake_pos present takes⟩) T

end Uptake

namespace Steady

/-- A consumer (`true`) and a renewer (`false`), both always active. -/
def web : Web Bool Unit where
  level _ _ := 1
  active _ _ := True
  requires _ f _ := f = true
  need _ _ _ := 1
  draws _ f _ := f = true

def flow : Flow Bool Unit where
  present _ := [true, false]
  take _ f _ := match f with
    | true => 1
    | false => 0
  give _ f _ := match f with
    | true => 0
    | false => 1

/-- The flow balances, only active formations give and take, from what they draw on;
uptake is positive at every step and nothing ever arises, yet replenishment is needed at
arbitrarily late steps, exactly as for unceasing generation of takers. -/
theorem steady :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ web.Dependent ∧
    (∀ t, 0 < flow.uptake [()] t) ∧ (∀ t f, ¬ web.Arises t f) ∧
    ∀ T, ¬ ∀ t, T ≤ t → flow.replenishment [()] t = 0 :=
  have positive : ∀ t, 0 < flow.uptake [()] t := fun _ => Nat.zero_lt_one
  have balances : flow.Balances web := fun _ _ => rfl
  ⟨balances, fun _ _ _ _ _ => trivial,
   fun _ f _ _ takes => match f, takes with
    | true, _ => ⟨trivial, rfl⟩
    | false, takes => absurd takes (Nat.lt_irrefl 0),
   fun _ _ _ _ _ => Nat.le_refl 1, positive, fun _ _ arises => arises.1 trivial,
   uptake_needs_replenishment balances fun N => ⟨N, Nat.le_refl N, positive N⟩⟩

end Steady

end P12Probe
```

### `P12Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P11b and P12: the P12 part

Each probe is a minimal model satisfying the published definitions at `e5430db5`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P12Probe

open Becoming

variable {F F' C : Type}

/-! ## M1. Continuity read in both namings fixes arising and undermining -/

/-- The same correspondence read from the new naming back to the old. -/
def inv (σ : Reidentify F F') : Reidentify F' F :=
  ⟨σ.new, σ.old, σ.new_old, σ.old_new⟩

/-- If the old names keep the continuing activity of the new naming, every arising under
the old names is an arising under the new. -/
theorem arises_of_inverse_keepsActive {W : Web F C} {σ : Reidentify F F'}
    (back : (inv σ).KeepsActive (W.reidentify σ)) {t : Nat} {f : F} (arises : W.Arises t f) :
    (W.reidentify σ).Arises t (σ.new (t + 1) f) :=
  have after : (W.reidentify σ).active (t + 1) (σ.new (t + 1) f) :=
    Eq.subst (motive := fun g => W.active (t + 1) g) (σ.old_new (t + 1) f).symm arises.2
  ⟨fun before =>
    have same : σ.old (t + 1) (σ.new (t + 1) f) = σ.old t (σ.new (t + 1) f) :=
      back t _ before after
    arises.1 (Eq.subst (motive := fun g => W.active t g)
      (same.symm.trans (σ.old_new (t + 1) f)) before),
   after⟩

/-- Continuity of activity read in both namings: arising is exactly preserved. -/
theorem arises_iff_of_keepsActive_both {W : Web F C} {σ : Reidentify F F'}
    (keeps : σ.KeepsActive W) (back : (inv σ).KeepsActive (W.reidentify σ)) (t : Nat)
    (x : F') : (W.reidentify σ).Arises t x ↔ W.Arises t (σ.old (t + 1) x) :=
  ⟨Web.arises_of_keepsActive keeps,
   fun arises => Eq.subst (motive := fun y => (W.reidentify σ).Arises t y) (σ.new_old (t + 1) x)
     (arises_of_inverse_keepsActive back arises)⟩

theorem unceasing_iff_of_keepsActive_both {W : Web F C} {σ : Reidentify F F'}
    (keeps : σ.KeepsActive W) (back : (inv σ).KeepsActive (W.reidentify σ)) :
    (W.reidentify σ).Unceasing ↔ W.Unceasing :=
  ⟨Web.unceasing_of_keepsActive keeps,
   fun unceasing N => match unceasing N with
    | ⟨t, f, later, arises⟩ => ⟨t, σ.new (t + 1) f, later, arises_of_inverse_keepsActive back arises⟩⟩

/-- If the old names keep the continuing dependences of the new naming, a dependence met
while it held under the new names was met while it held under the old. -/
theorem metAbove_of_inverse_keepsTenure {W : Web F C} {σ : Reidentify F F'}
    (back : (inv σ).KeepsTenure (W.reidentify σ)) {t : Nat} {y : F'} {c : C} {m : Nat} :
    (W.reidentify σ).MetAbove t y c m → W.MetAbove t (σ.old t y) c m
  | ⟨s, le, held, met, above⟩ =>
    have same : ∀ u, s ≤ u → u ≤ t → σ.old u y = σ.old t y :=
      Reidentify.steady (σ := inv σ) (W := W.reidentify σ) back held
    ⟨s, le, fun u a b => Eq.subst (motive := fun g => W.requires u g c) (same u a b) (held u a b),
     Eq.subst (motive := fun g => W.need s g c ≤ W.level s c) (same s (Nat.le_refl s) le) met,
     Eq.subst (motive := fun g => m < W.need s g c) (same s (Nat.le_refl s) le) above⟩

/-- Continuity of dependence read from the new naming: no undermining is added. With
`undermining_of_keepsTenure`, undermining is exactly preserved. -/
theorem undermining_of_inverse_keepsTenure {W : Web F C} {σ : Reidentify F F'}
    (back : (inv σ).KeepsTenure (W.reidentify σ)) {t : Nat} {x : F'} :
    (W.reidentify σ).UnderminingAt t x → W.UnderminingAt t (σ.old t x)
  | ⟨c, drawn, y, depends, met, fell⟩ =>
    ⟨c, drawn, σ.old t y, depends, metAbove_of_inverse_keepsTenure back met, fell⟩

/-- Both succession witnesses keep continuity only one way: naming the lineage as one
makes a continuity of activity the apart naming lacks. -/
theorem lineage_one_way :
    Lineage.one.KeepsActive Lineage.web ∧
    ¬ (inv Lineage.one).KeepsActive (Lineage.web.reidentify Lineage.one) :=
  ⟨Lineage.readings.1, fun back => Lineage.readings.2.2
    ((unceasing_iff_of_keepsActive_both Lineage.readings.1 back).mpr Lineage.readings.2.1)⟩

/-- The heir succeeding the elder makes a continuity of dependence (across step 0) that
the apart naming lacks. -/
theorem succession_one_way :
    Succession.succeeds.KeepsTenure Succession.web ∧
    ¬ (inv Succession.succeeds).KeepsTenure Succession.inherited :=
  ⟨Succession.readings.2.1, fun back =>
    Succession.readings.2.2.2.1 1 (Nat.le_refl 1)
      (Eq.subst (motive := fun f => Succession.web.UnderminingAt 1 f) (Succession.after_drawer 1)
        (undermining_of_inverse_keepsTenure back (Succession.readings.2.2.2.2 1)))⟩

/-! ## M2. Under continuity in both namings, joining across a dormant step still changes
the class of a formation -/

/-- `Nat.succ_ne_zero` reports `propext` in Lean 4.29.1; this one does not. -/
theorem succ_ne_zero {n : Nat} : n + 1 ≠ 0 := fun h => Nat.noConfusion h

namespace Dormancy

inductive Who where
  | early
  | late
  | needy

inductive Cond where
  | spring
  | pool

/-- `early` is active at step 0 only, needs one unit of a spring that holds one unit, and
draws it; `late` is active at step 2 only and draws the pool; `needy` needs two units of
the pool at step 0, where the pool supports it. No formation is active, or depends on
anything, at two successive steps. -/
def web : Web Who Cond where
  level t c := match c with
    | .spring => 1
    | .pool => Turnover.pool t
  active t f := match f with
    | .early => t = 0
    | .late => t = 2
    | .needy => t = 0
  requires t f c := match f, c with
    | .needy, .pool => t = 0
    | .early, .spring => t = 0
    | .needy, .spring => False
    | .early, .pool => False
    | .late, _ => False
  need _ f _ := match f with
    | .needy => 2
    | .early => 1
    | .late => 0
  draws t f c := match f, c with
    | .early, .spring => t = 0
    | .late, .pool => t = 2
    | .early, .pool => False
    | .late, .spring => False
    | .needy, _ => False

def swap : Who → Who
  | .early => .late
  | .late => .early
  | .needy => .needy

def after : Nat → Who → Who
  | 0, f => f
  | _ + 1, f => swap f

theorem after_after : ∀ t f, after t (after t f) = f
  | 0, _ => rfl
  | _ + 1, .early | _ + 1, .late | _ + 1, .needy => rfl

/-- From step 1 on, `late` bears the name `early`. -/
def join : Reidentify Who Who := ⟨after, after, after_after, after_after⟩

abbrev joined : Web Who Cond := web.reidentify join

theorem activeOld : ∀ t f, web.active t f → web.active (t + 1) f → False
  | t, .early, _, next => succ_ne_zero next
  | t, .needy, _, next => succ_ne_zero next
  | _, .late, now, next => absurd (Eq.subst (motive := fun n => n + 1 = 2) now next) (by decide)

theorem activeNew : ∀ t x, joined.active t x → joined.active (t + 1) x → False
  | 0, .early, _, next => absurd (a := (1 : Nat) = 2) next (by decide)
  | 0, .late, now, _ => absurd (a := (0 : Nat) = 2) now (by decide)
  | 0, .needy, _, next => absurd (a := (1 : Nat) = 0) next (by decide)
  | _ + 1, .early, now, next => absurd (Eq.subst (motive := fun n => n + 1 = 2) now next) (by decide)
  | m + 1, .late, now, _ => succ_ne_zero now
  | m + 1, .needy, now, _ => succ_ne_zero now

/-- Every dependence holds at step 0 only. -/
theorem only_zero : ∀ t f c, web.requires t f c → t = 0
  | _, .needy, .pool, h => h
  | _, .early, .spring, h => h
  | _, .needy, .spring, h => (nomatch h)
  | _, .early, .pool, h => (nomatch h)
  | _, .late, _, h => (nomatch h)

theorem dependent : web.Dependent := fun t f _ c depends =>
  match f, c, t, depends with
  | .needy, .pool, 0, _ => Nat.le_refl 2
  | .early, .spring, 0, _ => Nat.le_refl 1
  | .needy, .pool, _ + 1, h => absurd h succ_ne_zero
  | .early, .spring, _ + 1, h => absurd h succ_ne_zero
  | .needy, .spring, _, h => (nomatch h)
  | .early, .pool, _, h => (nomatch h)
  | .late, _, _, h => (nomatch h)

theorem requiresOld : ∀ t g c, web.requires t g c → web.requires (t + 1) g c → False :=
  fun t g c _ next => succ_ne_zero (only_zero (t + 1) g c next)

theorem requiresNew : ∀ t x c, joined.requires t x c → joined.requires (t + 1) x c → False :=
  fun t x c _ next => succ_ne_zero (only_zero (t + 1) (after (t + 1) x) c next)

/-- The join keeps every continuing activity and dependence, read in both namings. -/
theorem keeps_both :
    join.KeepsActive web ∧ (inv join).KeepsActive joined ∧
    join.KeepsTenure web ∧ (inv join).KeepsTenure joined :=
  ⟨fun t f now next => (activeOld t f now next).elim,
   fun t x now next => (activeNew t x now next).elim,
   fun t g c now next => (requiresOld t g c now next).elim,
   fun t x c now next => (requiresNew t x c now next).elim⟩

theorem consumed : web.Consumed .pool :=
  ⟨.needy, 0, rfl, fun t later => match t, later with
    | _ + 1, _ => Nat.lt_succ_self 1
    | 0, h => absurd h (Nat.lt_irrefl 0)⟩

/-- Named apart, `early` renews in the run (its spring keeps it) and `late` consumes. Joined across the
dormant step, with continuity kept in both namings, the formation named `early`
consumes and does not renew. -/
theorem classes :
    web.RenewingIn .early ∧ web.ConsumingIn .late ∧
    joined.ConsumingIn .early ∧ ¬ joined.RenewingIn .early :=
  ⟨fun _ c joins => match c, joins with
    | .spring, _ => fun _ g depends => match g, depends with
      | .early, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩
      | .needy, h | .late, h => (nomatch h)
    | .pool, .inl h | .pool, .inr h => (nomatch h),
   ⟨2, .pool, rfl, consumed⟩,
   ⟨2, .pool, rfl, (web.reidentify_consumed join .pool).mpr consumed⟩,
   fun renewing => Nat.not_succ_le_self 1
     (((web.reidentify_renewed join .pool).mp (renewing 2 .pool (.inr rfl))) 0 .needy rfl).2⟩

end Dormancy


/-! ## M3. A naming alone can meet every premise of `Unceasing.regeneration_recurs` -/

namespace TideFlip

def swap : Tide.Formation → Tide.Formation
  | .moon => .flicker
  | .flicker => .moon

def turn : Bool → Tide.Formation → Tide.Formation
  | true, f => swap f
  | false, f => f

theorem turn_turn : ∀ b f, turn b (turn b f) = f
  | true, .moon | true, .flicker | false, _ => rfl

/-- At every odd step the moon and the flicker exchange names. -/
def flip : Reidentify Tide.Formation Tide.Formation :=
  ⟨fun t => turn (odd t), fun t => turn (odd t), fun t => turn_turn (odd t),
    fun t => turn_turn (odd t)⟩

/-- The tide and the moon, with nothing arising (`Tide.still`), named by `flip`. -/
abbrev flipped : Web Tide.Formation Unit := Tide.still.reidentify flip

/-- The moon's renewing, carried to the new names. -/
def renews (t : Nat) (x : Tide.Formation) (c : Unit) : Prop := Tide.renews t (flip.old t x) c

theorem tide_changes : ∀ t, Tide.tide t < Tide.tide (t + 1) ∨ Tide.tide (t + 1) < Tide.tide t
  | 0 => .inl Nat.zero_lt_one
  | 1 => .inr Nat.zero_lt_one
  | n + 2 => tide_changes n

/-- Under the new names the name `moon` arises at every odd step. -/
theorem arises : ∀ t, odd t = true → flipped.Arises t .moon := fun _ o =>
  ⟨fun h => Tide.Formation.noConfusion
    ((Eq.subst (motive := fun b => turn b .moon = .moon) o h : turn true .moon = .moon)),
   Eq.subst (motive := fun b => turn b .moon = .moon) (congrArg (!·) o).symm rfl⟩

/-- `Tide.still` has no arising. Named by `flip`, which breaks the moon's continuing
activity, it meets every premise of `Unceasing.regeneration_recurs`: the tide changes at
every arising step, every rise is made by an active renewer, and generation is
unceasing. The conclusion (renewal recurs) is true; the generation is the naming's. -/
theorem naming_meets_premises :
    (∀ t f, ¬ Tide.still.Arises t f) ∧ ¬ flip.KeepsActive Tide.still ∧
    flipped.Dependent ∧ flipped.RenewedBy renews ∧
    flipped.Depletes [()] (fun t => ∃ x, flipped.Arises t x) ∧ flipped.Unceasing ∧
    ∀ T, ¬ ∀ t, T ≤ t → ∀ x, ¬ flipped.Regenerating renews [()] t x :=
  have made : flipped.RenewedBy renews := fun t _ _ =>
    ⟨flip.new t .moon, flip.old_new t .moon,
     Eq.subst (motive := fun f => Tide.renews t f ()) (flip.old_new t .moon).symm trivial⟩
  have depletes : flipped.Depletes [()] fun t => ∃ x, flipped.Arises t x :=
    (Web.depletes_iff flipped [()] _).mpr fun t _ => ⟨(), .head [], tide_changes t⟩
  have unceasing : flipped.Unceasing := fun N => match h : odd N with
    | true => ⟨N, .moon, Nat.le_refl N, arises N h⟩
    | false => ⟨N + 1, .moon, Nat.le_succ N, arises (N + 1) (congrArg (!·) h)⟩
  ⟨Tide.renewal_without_arising.2.2.2,
   fun keeps => Tide.Formation.noConfusion (keeps 0 .moon rfl rfl),
   (Tide.still.reidentify_dependent flip).mpr (fun _ _ _ _ depends => (nomatch depends)),
   made, depletes, unceasing,
   Web.Unceasing.regeneration_recurs flipped made depletes unceasing⟩

end TideFlip

/-! ## M4. `More.unceasing_reidentified` has a positive instance -/

namespace GardenCensus

open Garden (Kind)

theorem distinct : ∀ t, Distinct (Garden.present t)
  | 0 => trivial
  | n + 1 => ⟨fun mem => match mem_cons_cases mem with
      | .inl same => Kind.noConfusion (congrArg Prod.fst same)
      | .inr mem => Nat.lt_irrefl n (Garden.present_active n _ mem),
     fun mem => Nat.lt_irrefl n (Garden.present_active n _ mem), distinct n⟩

theorem listed : ∀ t (f : Kind × Nat), f.2 < t → f ∈ Garden.present t
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | n + 1, (k, i), lt => match Nat.lt_or_ge i n with
    | .inl below => .tail _ (.tail _ (listed n (k, i) below))
    | .inr above =>
      have same : n = i := Nat.le_antisymm above (Nat.le_of_lt_succ lt)
      match k with
      | .renewer => Eq.subst (motive := fun j => (Kind.renewer, j) ∈ Garden.present (n + 1))
          same (.head _)
      | .grower => Eq.subst (motive := fun j => (Kind.grower, j) ∈ Garden.present (n + 1))
          same (.tail _ (.head _))

/-- The garden's formations active at each step are listed once. -/
theorem census : Garden.web.Census Garden.present :=
  fun t => ⟨distinct t, fun f => ⟨listed t f, Garden.present_active t f⟩⟩

/-- Every premise of `More.unceasing_reidentified` holds in the garden, so its generation
is unceasing under every re-identification. -/
theorem everywhere (σ : Reidentify (Kind × Nat) F') : (Garden.web.reidentify σ).Unceasing :=
  Flow.More.unceasing_reidentified (decide := fun t f => Nat.decLt f.2 t) (L := Garden.flow)
    census distinct Garden.growers_take.1 Garden.more.2.2.2.2.2.2 σ

end GardenCensus

/-! ## M5. With continuation read one to many, growth forces no arising -/

/-- Arising relative to a continuation relation: active after the step, and continuing
no formation active before it. -/
def ArisesFrom (W : Web F C) (R : Nat → F → F → Prop) (t : Nat) (f : F) : Prop :=
  W.active (t + 1) f ∧ ¬ ∃ g, W.active t g ∧ R t g f

/-- With each formation continuing only itself, this is `Arises`. -/
theorem arisesFrom_self (W : Web F C) (t : Nat) (f : F) :
    ArisesFrom W (fun _ g f => g = f) t f ↔ W.Arises t f :=
  ⟨fun ⟨after, nothing⟩ => ⟨fun before => nothing ⟨f, before, rfl⟩, after⟩,
   fun ⟨before, after⟩ => ⟨after, fun ⟨_, active, same⟩ =>
     before (Eq.subst (motive := fun h => W.active t h) same active)⟩⟩

namespace Budding

theorem distinct : ∀ t, Distinct (Cycle.present t)
  | 0 => trivial
  | n + 1 => ⟨fun mem => Nat.lt_irrefl n (Cycle.present_lt n n mem), distinct n⟩

theorem listed : ∀ t n, n < t → n ∈ Cycle.present t
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | m + 1, n, lt => match Nat.lt_or_ge n m with
    | .inl below => .tail _ (listed m n below)
    | .inr above => Eq.subst (motive := fun j => j ∈ Cycle.present (m + 1))
        (Nat.le_antisymm above (Nat.le_of_lt_succ lt)) (.head _)

theorem census : Cycle.web.Census Cycle.present :=
  fun t => ⟨distinct t, fun n => ⟨listed t n, Cycle.present_lt t n⟩⟩

instance active (t n : Nat) : Decidable (Cycle.web.active t n) := Nat.decLt n t

/-- Every formation continues itself, and every new formation buds from formation 0. -/
def buds (_ : Nat) (g f : Nat) : Prop := g = f ∨ g = 0

/-- In the cycle, a census lists the active formations once, the flow lists each once,
only active formations take, and generation is more without end, so it is unceasing.
Read with budding as continuation, nothing arises after the first step. -/
theorem growth_without_arising :
    Cycle.web.Census Cycle.present ∧ (∀ t, Distinct (Cycle.flow.present t)) ∧
    Cycle.flow.Taking Cycle.web ∧ Cycle.flow.More [()] ∧ Cycle.web.Unceasing ∧
    ∀ t, 1 ≤ t → ∀ f, ¬ ArisesFrom Cycle.web buds t f :=
  ⟨census, distinct, Cycle.closed_more.2.2.1, Cycle.closed_more.2.2.2.2.2.2.1,
   Flow.More.unceasing (L := Cycle.flow) (cs := [()])
     census distinct Cycle.closed_more.2.2.1 Cycle.closed_more.2.2.2.2.2.2.1,
   fun _ late _ ⟨_, nothing⟩ => nothing ⟨0, late, .inr rfl⟩⟩

end Budding

/-! ## M6. Succession with an heir that is active -/

namespace ActiveHeir

inductive Formation where
  | drawer
  | elder
  | heir

/-- The pool of `Turnover`. The elder needs two units at step 0, where it is active. The
heir depends on the pool from step 1, needing one unit at step 1, where it is active,
and two from step 2. -/
def web : Web Formation Unit where
  level t _ := Turnover.pool t
  active t f := match f with
    | .drawer => True
    | .elder => t = 0
    | .heir => t = 1
  requires t f _ := match f with
    | .drawer => False
    | .elder => t = 0
    | .heir => 1 ≤ t
  need t f _ := match f with
    | .drawer => 0
    | .elder => 2
    | .heir => match t with
      | 1 => 1
      | _ => 2
  draws _ f _ := match f with
    | .drawer => True
    | .elder => False
    | .heir => False

def swap : Formation → Formation
  | .drawer => .drawer
  | .elder => .heir
  | .heir => .elder

def after : Nat → Formation → Formation
  | 0, f => f
  | _ + 1, f => swap f

theorem after_after : ∀ t f, after t (after t f) = f
  | 0, _ => rfl
  | _ + 1, .drawer | _ + 1, .elder | _ + 1, .heir => rfl

theorem after_drawer : ∀ t, after t .drawer = .drawer
  | 0 => rfl
  | _ + 1 => rfl

def succeeds : Reidentify Formation Formation := ⟨after, after, after_after, after_after⟩

abbrev inherited : Web Formation Unit := web.reidentify succeeds

/-- The web is `Dependent` and the heir is active at step 1. Succession keeps every
continuing activity and dependence. Named apart, no draw after step 0 undermines; with
the heir succeeding the elder, every draw from step 2 undermines. -/
theorem readings :
    web.Dependent ∧ web.active 1 .heir ∧
    succeeds.KeepsActive web ∧ succeeds.KeepsTenure web ∧
    (∀ t, 1 ≤ t → ¬ web.UnderminingAt t .drawer) ∧
    (∀ t, 2 ≤ t → inherited.UnderminingAt t .drawer) :=
  ⟨fun t f active _ depends => match f, t, active, depends with
    | .drawer, _, _, h => (nomatch h)
    | .elder, 0, _, _ => Nat.le_refl 2
    | .elder, _ + 1, h, _ => absurd h succ_ne_zero
    | .heir, 1, _, _ => Nat.le_refl 1
    | .heir, 0, h, _ => absurd (a := (0 : Nat) = 1) h (by decide)
    | .heir, _ + 2, h, _ => absurd (Nat.succ.inj h) succ_ne_zero,
   rfl,
   fun t f now next => match f, now, next with
    | .drawer, _, _ => (after_drawer (t + 1)).trans (after_drawer t).symm
    | .elder, _, next => absurd next succ_ne_zero
    | .heir, now, next => absurd (Eq.subst (motive := fun n => n + 1 = 1) now next) (by decide),
   fun t g _ now next => match g, t, now, next with
    | .drawer, _, h, _ => (nomatch h)
    | .elder, t, _, next => absurd next succ_ne_zero
    | .heir, _ + 1, _, _ => rfl
    | .heir, 0, now, _ => absurd now (Nat.not_succ_le_zero 0),
   fun t late ⟨_, _, g, depends, ⟨s, before, held, met, above⟩, _⟩ =>
    match g, depends, held, met, above with
    | .drawer, h, _, _, _ => (nomatch h)
    | .elder, h, _, _, _ => Nat.not_succ_le_zero 0 (Eq.subst (motive := fun n => 1 ≤ n) h late)
    | .heir, _, held, met, above =>
      have early : 1 ≤ s := held s (Nat.le_refl s) before
      have one_lt : 1 < web.need s .heir () := Nat.lt_of_le_of_lt
        (Nat.le_of_eq (Turnover.pool_late (Nat.succ_le_succ (Nat.zero_le t))).symm) above
      have le_one : web.need s .heir () ≤ 1 :=
        Nat.le_trans met (Nat.le_of_eq (Turnover.pool_late early))
      Nat.lt_irrefl 1 (Nat.lt_of_lt_of_le one_lt le_one),
   fun t late => match t, late with
    | m + 2, _ => ⟨(), trivial, .elder, Nat.succ_le_succ (Nat.zero_le (m + 1)),
        ⟨0, Nat.zero_le _, fun u _ _ => match u with
          | 0 => rfl
          | v + 1 => Nat.succ_le_succ (Nat.zero_le v),
         Nat.le_refl 2, Nat.lt_succ_self 1⟩,
        Nat.lt_succ_self 1⟩
    | 0, h => absurd h (by decide)
    | 1, h => absurd h (by decide)⟩

end ActiveHeir

/-! ## M7. Named at two levels, a lineage persists and its members arise without end -/

namespace Layered

inductive Who where
  | first
  | second
  | line

/-- `Lineage.web` with the lineage itself named as a third formation, always active. The
web has no relation saying that `line` is constituted by the members; that part–whole
relation is what a single naming level omits. -/
def web : Web Who Unit where
  level _ _ := 0
  active t w := match w with
    | .first => odd t = false
    | .second => odd t = true
    | .line => True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Members arise without end while the lineage is active at every step, as some member
is. -/
theorem both :
    web.Unceasing ∧ ∀ t, web.active t .line ∧ (web.active t .first ∨ web.active t .second) :=
  have arises : ∀ t, odd t = true → web.Arises t .first := fun _ odd' =>
    ⟨fun even => (nomatch odd'.symm.trans even), congrArg (!·) odd'⟩
  ⟨fun N => match h : odd N with
    | true => ⟨N, .first, Nat.le_refl N, arises N h⟩
    | false => ⟨N + 1, .first, Nat.le_succ N, arises (N + 1) (congrArg (!·) h)⟩,
   fun t => ⟨trivial, match h : odd t with
    | true => .inr h
    | false => .inl h⟩⟩

end Layered

end P12Probe
```

### `ProbeAudit.lean`

```lean
import P11bProbes
import P12Probes

#print axioms P12Probe.Repeated.rep
#print axioms P12Probe.Repeated.web
#print axioms P12Probe.Repeated.flow
#print axioms P12Probe.Repeated.ones
#print axioms P12Probe.Repeated.census
#print axioms P12Probe.Repeated.more_without_arising
#print axioms P12Probe.uptake_needs_replenishment
#print axioms P12Probe.replenishment_recurs_from_uptake
#print axioms P12Probe.Steady.web
#print axioms P12Probe.Steady.flow
#print axioms P12Probe.Steady.steady
#print axioms P12Probe.inv
#print axioms P12Probe.arises_of_inverse_keepsActive
#print axioms P12Probe.arises_iff_of_keepsActive_both
#print axioms P12Probe.unceasing_iff_of_keepsActive_both
#print axioms P12Probe.metAbove_of_inverse_keepsTenure
#print axioms P12Probe.undermining_of_inverse_keepsTenure
#print axioms P12Probe.lineage_one_way
#print axioms P12Probe.succession_one_way
#print axioms P12Probe.succ_ne_zero
#print axioms P12Probe.Dormancy.Who
#print axioms P12Probe.Dormancy.Cond
#print axioms P12Probe.Dormancy.web
#print axioms P12Probe.Dormancy.swap
#print axioms P12Probe.Dormancy.after
#print axioms P12Probe.Dormancy.after_after
#print axioms P12Probe.Dormancy.join
#print axioms P12Probe.Dormancy.joined
#print axioms P12Probe.Dormancy.activeOld
#print axioms P12Probe.Dormancy.activeNew
#print axioms P12Probe.Dormancy.only_zero
#print axioms P12Probe.Dormancy.dependent
#print axioms P12Probe.Dormancy.requiresOld
#print axioms P12Probe.Dormancy.requiresNew
#print axioms P12Probe.Dormancy.keeps_both
#print axioms P12Probe.Dormancy.consumed
#print axioms P12Probe.Dormancy.classes
#print axioms P12Probe.TideFlip.swap
#print axioms P12Probe.TideFlip.turn
#print axioms P12Probe.TideFlip.turn_turn
#print axioms P12Probe.TideFlip.flip
#print axioms P12Probe.TideFlip.flipped
#print axioms P12Probe.TideFlip.renews
#print axioms P12Probe.TideFlip.tide_changes
#print axioms P12Probe.TideFlip.arises
#print axioms P12Probe.TideFlip.naming_meets_premises
#print axioms P12Probe.GardenCensus.distinct
#print axioms P12Probe.GardenCensus.listed
#print axioms P12Probe.GardenCensus.census
#print axioms P12Probe.GardenCensus.everywhere
#print axioms P12Probe.ArisesFrom
#print axioms P12Probe.arisesFrom_self
#print axioms P12Probe.Budding.distinct
#print axioms P12Probe.Budding.listed
#print axioms P12Probe.Budding.census
#print axioms P12Probe.Budding.active
#print axioms P12Probe.Budding.buds
#print axioms P12Probe.Budding.growth_without_arising
#print axioms P12Probe.ActiveHeir.Formation
#print axioms P12Probe.ActiveHeir.web
#print axioms P12Probe.ActiveHeir.swap
#print axioms P12Probe.ActiveHeir.after
#print axioms P12Probe.ActiveHeir.after_after
#print axioms P12Probe.ActiveHeir.after_drawer
#print axioms P12Probe.ActiveHeir.succeeds
#print axioms P12Probe.ActiveHeir.inherited
#print axioms P12Probe.ActiveHeir.readings
#print axioms P12Probe.Layered.Who
#print axioms P12Probe.Layered.web
#print axioms P12Probe.Layered.both
```

### `ProbeAudit` output

```text
'P12Probe.Repeated.rep' does not depend on any axioms
'P12Probe.Repeated.web' does not depend on any axioms
'P12Probe.Repeated.flow' does not depend on any axioms
'P12Probe.Repeated.ones' does not depend on any axioms
'P12Probe.Repeated.census' does not depend on any axioms
'P12Probe.Repeated.more_without_arising' does not depend on any axioms
'P12Probe.uptake_needs_replenishment' does not depend on any axioms
'P12Probe.replenishment_recurs_from_uptake' does not depend on any axioms
'P12Probe.Steady.web' does not depend on any axioms
'P12Probe.Steady.flow' does not depend on any axioms
'P12Probe.Steady.steady' does not depend on any axioms
'P12Probe.inv' does not depend on any axioms
'P12Probe.arises_of_inverse_keepsActive' does not depend on any axioms
'P12Probe.arises_iff_of_keepsActive_both' does not depend on any axioms
'P12Probe.unceasing_iff_of_keepsActive_both' does not depend on any axioms
'P12Probe.metAbove_of_inverse_keepsTenure' does not depend on any axioms
'P12Probe.undermining_of_inverse_keepsTenure' does not depend on any axioms
'P12Probe.lineage_one_way' does not depend on any axioms
'P12Probe.succession_one_way' does not depend on any axioms
'P12Probe.succ_ne_zero' does not depend on any axioms
'P12Probe.Dormancy.Who' does not depend on any axioms
'P12Probe.Dormancy.Cond' does not depend on any axioms
'P12Probe.Dormancy.web' does not depend on any axioms
'P12Probe.Dormancy.swap' does not depend on any axioms
'P12Probe.Dormancy.after' does not depend on any axioms
'P12Probe.Dormancy.after_after' does not depend on any axioms
'P12Probe.Dormancy.join' does not depend on any axioms
'P12Probe.Dormancy.joined' does not depend on any axioms
'P12Probe.Dormancy.activeOld' does not depend on any axioms
'P12Probe.Dormancy.activeNew' does not depend on any axioms
'P12Probe.Dormancy.only_zero' does not depend on any axioms
'P12Probe.Dormancy.dependent' does not depend on any axioms
'P12Probe.Dormancy.requiresOld' does not depend on any axioms
'P12Probe.Dormancy.requiresNew' does not depend on any axioms
'P12Probe.Dormancy.keeps_both' does not depend on any axioms
'P12Probe.Dormancy.consumed' does not depend on any axioms
'P12Probe.Dormancy.classes' does not depend on any axioms
'P12Probe.TideFlip.swap' does not depend on any axioms
'P12Probe.TideFlip.turn' does not depend on any axioms
'P12Probe.TideFlip.turn_turn' does not depend on any axioms
'P12Probe.TideFlip.flip' does not depend on any axioms
'P12Probe.TideFlip.flipped' does not depend on any axioms
'P12Probe.TideFlip.renews' does not depend on any axioms
'P12Probe.TideFlip.tide_changes' does not depend on any axioms
'P12Probe.TideFlip.arises' does not depend on any axioms
'P12Probe.TideFlip.naming_meets_premises' does not depend on any axioms
'P12Probe.GardenCensus.distinct' does not depend on any axioms
'P12Probe.GardenCensus.listed' does not depend on any axioms
'P12Probe.GardenCensus.census' does not depend on any axioms
'P12Probe.GardenCensus.everywhere' does not depend on any axioms
'P12Probe.ArisesFrom' does not depend on any axioms
'P12Probe.arisesFrom_self' does not depend on any axioms
'P12Probe.Budding.distinct' does not depend on any axioms
'P12Probe.Budding.listed' does not depend on any axioms
'P12Probe.Budding.census' does not depend on any axioms
'P12Probe.Budding.active' does not depend on any axioms
'P12Probe.Budding.buds' does not depend on any axioms
'P12Probe.Budding.growth_without_arising' does not depend on any axioms
'P12Probe.ActiveHeir.Formation' does not depend on any axioms
'P12Probe.ActiveHeir.web' does not depend on any axioms
'P12Probe.ActiveHeir.swap' does not depend on any axioms
'P12Probe.ActiveHeir.after' does not depend on any axioms
'P12Probe.ActiveHeir.after_after' does not depend on any axioms
'P12Probe.ActiveHeir.after_drawer' does not depend on any axioms
'P12Probe.ActiveHeir.succeeds' does not depend on any axioms
'P12Probe.ActiveHeir.inherited' does not depend on any axioms
'P12Probe.ActiveHeir.readings' does not depend on any axioms
'P12Probe.Layered.Who' does not depend on any axioms
'P12Probe.Layered.web' does not depend on any axioms
'P12Probe.Layered.both' does not depend on any axioms
```
