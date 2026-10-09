# P9b、P10 与 P11 的独立审查 / Independent review of P9b, P10 and P11

2026-10-09, Asia/Bangkok. **Independent AI review by a separate agent (Claude Opus 5.5) that did not write the work under review.** It was requested within Ren's continuing instruction to pursue the Theory of Becoming and "prove the necessary proofs" ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)). This file is the only repository file the reviewer created or changed. No repository checker or render tool was run, and nothing was committed. The probes and audit files were compiled in a scratch directory outside the repository; their sources are in the appendix.

**摘要（中文）。** P9b、P10 与 P11 的全部 Lean 声明在仓库外从 prelude 重新编译，公理报告为空。311 项定理／588 项声明审计、回执 `20261009T032004.394466Z`、17 个模块的核心闭包、记录的哈希与别名都对。数学被接受。审计覆盖 227 条声明（84 条探针声明，其中 56 项定理；143 条核心声明），全部不依赖任何公理。问题仍在定义、散文与对应之间。

- **P9b。** G1–G12 中十一项关闭，其中 G2 以披露关闭；G1 部分关闭。新的 `MetSince` 排除了 `FallingNeed` 与 `RisingNeed`，但带来一个未披露的代价。所需增长之后，一次把水平压到**曾被满足的旧所需**之下的汲取，既不断裂也不侵蚀（`Stunted`，H1）。读作“低于那时的所需，也低于现在的所需”的最小形式计入它，并且仍排除三个 P9b 见证。`Determined` 与“动作可取”合乎散文，但根模块说明把 `Determined` 写成了定义的一部分（H2）。G8 与 G11 各留一处残余（H3）。
- **P10。** `Paid` 只说事件所在之步家族中有某个条件变化（`paid_iff`）。它不涉及生起的形成：一个与之无关的振荡条件就能“支付”（`Tide`）。它也不看该形成开始汲取的那一步：正面见证 `Bloom` 只是空洞地满足它（H4）。“严格强于”在 P10 自身的意义上成立（`Tide.still`），但所引的见证没有任何上升。P10 的“更新”是净上升，看不见同步的更新，P11 的 `Garden` 不满足 `Paid`；流的形式 `unceasing_supplied` 同时覆盖两者（H5）。“任何有限部分都不能独自不息”需要耗散前提：一个封闭循环的有限家族可以不息（`Recycle`，H6）。把 `Arises` 称为“生生的第二个生”、把 `Growth` 称为“以消耗进行的生成”，在用词上与 Ren 2026-10-09 关于生成与退化不重叠的话及该来源的 AI 修正说明相冲突（H7）。
- **P11。** 作为蕴含，“严格的层级”不成立，因为不止地更多不蕴含不息（`more_without_arising`）；成立的是三者各自所需之更新的层级（H8）。`More` 数的是流中的取用者，不是活的或依存的形成（`more_without_living_takers`、`Crowd`，H9）。“供给没有最终的界”依赖每个取用者至少取一个单位，这是一个未点明的实质前提（H10）。“给予者越来越多”强于定理：给予者可以在无穷多步上为零（`Pulse`，H11）。“没有一个有限的部分独自承担”在封闭循环中不成立（`Cycle`，H12）。
- **非二元方法与来源。** 没有引入展开之外的来源；太阳作为表示所省略的关系，处理正确。但纯净核心新增了 Ren 已纠正过的支付与账目用语（H13）。把形成与条件分为两类，省略了“生作为生的条件”（H14）。没有替 Ren 选择 living 的读法，AI 论证都有标注。

## 0. Scope, materials and method

**Object.** The state of `main` at `c48ec435`:

- **P9b (`579a11c8`).** The corrections answering G1–G12 of [BECOMING-P8-P9-P7B-REVIEW](BECOMING-P8-P9-P7B-REVIEW.md):
  - study [§12](BECOMING-RENEWAL-READING.md) and the edits it lists;
  - the repaired `Web.MetSince`;
  - `Determined`, `Shock.determined` and `Pool.determined`;
  - the new witnesses `FallingNeed`, `RisingNeed`, `Gap`, `Immediate`, `ThirdParty`, `Substitution.slow`, `Hidden`, `Tagged`, `Later`, `Pinned.drawing_interacts`, `one_use_connects` and `drawing_reaches`;
  - the six corrected records.
- **P10 (`5669f67d`).** [Becoming.Generation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean); study §13 and its English paragraph; record [unceasing-generation-needs-renewal](../../../../theories/becoming/results/records/unceasing-generation-needs-renewal.md).
- **P11 (`c48ec435`).** [Becoming.Flow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean); study §14 and its English paragraph; record [more-needs-renewers](../../../../theories/becoming/results/records/more-needs-renewers.md).
- **The chapter.** [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md): §2 "继续生成" and "更多" (lines 191–197), §6.3, §6.5, the §8 row "继续生成", the §9 table and the §10 glossary.

**Materials.** The working tree was clean at `c48ec4354b65…`, so every file below equals its committed bytes.

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `f21826582ae940fd` |
| chapter `THE-THEORY-OF-BECOMING.md` | `b0a78584537e152b` |
| previous review `BECOMING-P8-P9-P7B-REVIEW.md` | `7f0334aff71d61c2` |
| `NONDUAL-METHOD.md` | `8c48b03a167a8909` |
| receipt `becoming-verification.json` (run `20261009T032004.394466Z`) | `ce2c455e5ecdbbfb` |
| `Becoming.lean` | `920f3c9d04d7ccb8` |
| `Becoming/Generation` / `Flow` | `0c32526f6f00dff5` / `4970873512ed140b` |
| `Becoming/Dependence` / `Joint` / `Substitution` | `1eed73008c4a77ab` / `6dde12eea575c7aa` / `0681ead7c079bfe7` |
| `Becoming/Ranking` / `Correspondence` / `Return` | `5cc891314f1c76ea` / `175bba2053215adc` / `5b94e4adc0f76213` |
| `Becoming/Bridge` (unchanged since `b9954b90`) | `33f961da3d4ecaa9` |
| records unceasing-generation-needs-renewal / more-needs-renewers | `d632197b199e6bc4` / `bc34f6733cc6f2c7` |
| records becoming-stepwise-reading / joint-difference-making / ranking-under-readings | `24154d28ddf870e3` / `345de569b1706af9` / `61cfe272fed50ada` |
| records substitution-preserves-consumption / condition-correspondence-discipline / becoming-finite-horizon | `9a62a29121b2296c` / `a6fb0e4654c24278` / `b95b1003673dff19` |
| records becoming-renewal-reading / becoming-dependence-dynamics | `1ca745af2cbc8ee5` / `ca9c697e54354eb0` |

**Read in full:**

- [AGENTS.md](../../../../AGENTS.md);
- study §§12–14 and the English P9b, P10 and P11 paragraphs;
- the previous review;
- `Generation`, `Flow`, and the P9b parts of `Dependence`, `Joint`, `Ranking`, `Substitution` and `Correspondence`;
- the ten record JSONs above;
- the chapter sections listed;
- the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md).

**Ren's words read**, for provenance:

- [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md);
- [以关系结构分开更新型与消耗型形成](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md);
- the two vocabulary corrections, [付费记录](../../../../sources/15-codex-theory-conversations/2026-10-06-nondual-core-tree-continuation.md#subsequent-wording-correction-6-october-2026) and [recipient, money, pay](../../../../sources/15-codex-theory-conversations/2026-10-06-foundational-vocabulary-correction.md);
- [the pure core](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md).

**No external literature was newly read.** The physical examples used here (nutrient cycling, free energy, a minimum metabolic uptake) come from the reviewer's prior knowledge.

**Recompilation.** In a scratch directory outside the repository, the committed bytes of the core closure were compiled in dependency order with Lean 4.29.1 (commit `f72c35b3`), using `LEAN_PATH=. lean -o X.olean X.lean`. The order was `GenerativeCore` (with `import Std` removed, as the checker does), `InquirySufficiency`, `RelationalRenewal`, `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Metaethics, Ranking, Correspondence, Generation, Flow}` and `Becoming`. All 17 modules exit 0 from the prelude. The 12 periphery modules that `Becoming.Bridge` imports, and the bridge itself, also exit 0, for 30 modules in all.

- **Receipt.** The status is `passed`, with Lean 4.29.1 `f72c35b3`; `core_closure` lists 17 modules; all 30 `source_sha256` entries equal the current files.
- **Counts.** `^theorem` per module:
  - Frame 11, Inquiry 6, Renewal 6, Dependence 51, Return 29, Horizon 14;
  - Joint 20, Substitution 7, Metaethics 35, Ranking 27, Correspondence 25;
  - Generation 18, Flow 28, Bridge 34.

  That makes 311 theorems, as the receipt, the chapter (§9) and the records state. The receipt's 588 declaration audits have empty reports for every spine and bridge module. `Generation` has 39 declarations and `Flow` has 47.
- **Records.** The `references` hashes of all 13 records changed since `b9954b90` equal the current files. Every proof binding's `sha256_pointer` into the receipt equals the bound source's hash. The P9b records carry `reviewed_at_utc` 03:10:36Z, the P9b commit time. The two new records carry 03:14:37Z and 03:21:53Z, just before their commits.
- **Names.**
  - `Aliases.lean` (sha256 `13f77828fa8bec3e…`) runs `#check @` on all 205 aliases of those 13 records. 174 resolve in the core.
  - `AliasesBridge.lean` (`a6a070aa0b177432…`) shows that 26 more resolve through `Becoming.Bridge`.
  - The remaining five (`commonAction_iff_commonResponse`, `implements_iff_commonResponse`, `implements_refine`, `safeOn_iff_commonResponse` and `safeOn_refine`, in becoming-spine-instances) are theorems of the Mathlib periphery (`CorrectionInquiry`), which was not rebuilt. That record changed only its validation scope and hashes in these commits.
  - A second pass, `Names.lean` (`c4c6fcd136d28d5d…`) with `NamesLast.lean` and `NamesBridge.lean`, resolves all 329 qualified names cited anywhere in the ten records listed above.
- **Axioms.** `Audit.lean` (`223ebf29ce344c4c…`) prints the axioms of 227 declarations: every probe declaration (84), every declaration of `Generation` and `Flow` (86), and 57 P9b declarations and core lemmas. All 227 report "does not depend on any axioms". `NamesBridge.lean` does the same for the two bridge theorems of ranking-under-readings.

**Probes.** Three files import the unchanged `Becoming` and compile with exit 0 and no warnings:

| File | sha256 prefix | Theorems | Defs / inductives |
|---|---|---|---|
| `P9bProbes.lean` | `fc668c2fa584f2e1` | 7 | 3 |
| `P10Probes.lean` | `af36b1fdcef4b49a` | 17 | 11 |
| `P11Probes.lean` | `f58b55fc72592d1d` | 32 | 14 |

The probes avoid `simp` and `omega`. `decide` is used once, on a closed numeral, after `rw`.

The probes are minimal models that satisfy the published definitions unchanged. Following the nondual method, they show what the definitions admit, not what actual systems usually do. Where a fuller account would exclude a probe, the relation that excludes it is one the representation omits; the probe does not refute the theory. A probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels.**

- *error*: a definition does not match its stated meaning, or a stated claim is false of the definitions.
- *overclaim*: the prose is stronger than the Lean.
- *missing counterexample*: a relevant witness is absent from the comparison or the record.
- *presentation*: wording, provenance or bookkeeping.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P9b: are G1–G12 closed? Is the new `MetSince` faithful, and does it bring new pathologies? Do `Determined` and availability match the prose? Does the narrowed prose match the Lean? | **Eleven of twelve are closed (G2 by disclosure); G1 is partly closed.** `MetSince` now reads "met at its own need at some step of an unbroken tenure, with the present need no greater". It excludes `FallingNeed` and `RisingNeed` as intended. It brings one undisclosed pathology: after a dependent's need has grown, a draw that takes the level below the need that *was* met is neither breaking nor undermining. A minimum form fixes this and keeps the three P9b exclusions. Availability is in the definition, and `Determined` is stated and proved for `Shock` and `Pool`. The prose matches, except that the root module doc makes `Determined` part of the definition, and the dichotomy also needs the dependence to be held and met at the withheld configuration. Elsewhere the narrowed prose matches the Lean; two residuals of G8 and G11 remain. | H1, H2, H3 |
| 2. P10: are `Arises`, `Unceasing`, `Paid`, `Still` and `RenewedBy` reasonable? Are there hollow ways to unceasing generation? Is "strictly stronger" supported? Does `conserved_ceases` warrant "no finite part is unceasing on its own"? | **`Arises`, `Unceasing` and `Still` are reasonable formal carriers of becoming active, not ceasing to arise, and nothing rising.** `Arises` is weak as "the second 生 of 生生". `RenewedBy` correctly forbids an outside source, but its conclusion is only as strong as the unconstrained `renews`. `Paid` is the weak point. It requires only that some condition of the family change at the arising step. It is not tied to the arising formation, and it looks at the arising step rather than the step at which the formation draws. Hollow ways: unceasing generation by a flicker "paid" by an unrelated oscillation, or by mere re-activation; and "renewing activity recurs" with `renews := True`. A closed recycling family is not hollow, but it defeats the AI reading of `conserved_ceases`. **"Strictly stronger" is true in P10's own sense** (`Tide.still`), but the cited witness has no rise. P10's renewal is a net rise, so concurrent renewal is invisible and P11's `Garden` fails `Paid`. **The AI argument is not warranted** without a dissipation premise. | H4, H5, H6, H7 |
| 3. P11: is `More` a fair reading of 更多生? What is the take/give versus draws/requires/active gap? Are the glosses of the two unboundedness theorems right? Is the hierarchy strict, and in what sense? Is the structural reading of 生生 accurate? | **`More` is a fair, labelled reading of "ever more formations take from a finite family".** It is not a reading of "more formations living on the same conditions": flow and web are tied only through levels and active givers, so takers need not be active, dependent or drawing. **The table and glossary glosses** ("没有最终的界") **are correct; the prose "越来越多 / ever more givers" is not.** Supply without bound rests on a minimum uptake per taker that is not named. **The hierarchy is strict only as a ranking of the renewal each property needs, in flow terms; the three properties are not ordered by implication.** The structural reading is labelled as an AI argument, but it overstates "ever more" and "no finite part bears it alone", and it omits that renewers may be the takers themselves. | H8, H9, H10, H11, H12, H14 |
| 4. Nondual method | **No outside source, owner or recipient is introduced.** The sun and Garden's renewers are treated as omitted relations, and a formation can both take and give. But the pure core gains payment and ledger vocabulary that Ren corrected on 2026-10-06. `stock` adds levels across heterogeneous conditions, which matters for `conserved_ceases`. The formation/condition split omits life as a condition of life. | H6, H13, H14 |
| 5. Provenance; choices made on Ren's behalf | **No reading of `living` is chosen for Ren.** Ren's words are quoted exactly, and the readings and AI arguments are labelled. Two provenance issues remain. First, `Arises` is called "the second 生 of 生生" and `Growth` "generation by consumption", without a label, in tension with Ren's 2026-10-09 statement and that source's AI correction note. Second, 更多 is read as a count of takers but glossed as "more formations living on the same conditions". | H7, H9 |
| 6. Records | **Counts, run, closure, hashes, aliases and validation scopes are correct** (311 / 588, run `20261009T032004.394466Z`, 17 modules). Corrections are needed to claims, correspondence, hypotheses and counterexamples: more-needs-renewers (H8, H9, H10, H11, H12); unceasing-generation-needs-renewal (H4, H5, H6, H7); becoming-stepwise-reading (H1); and one stale sentence in becoming-renewal-reading (H3). | H1, H3–H12 |

**Status of G1–G12.**

| Item | Status | Evidence |
|---|---|---|
| G1 | partly closed | `MetSince` redefined; `FallingNeed.never_met_not_undermining` and `RisingNeed.grown_need_not_met` are theorems. The rising-need choice is disclosed (§12.4 rebuttal 1), but its cost is not: once the need grows, a draw below the need that was met counts for nothing stepwise (H1). |
| G2 | closed by disclosure | `Gap.lapse_starts_afresh`; record hypothesis and §7.1; a tenure through bounded absence listed as open. |
| G3 | closed | Hypothesis "焦点形成有一个使每个所需仍被满足的事件时" added; `Immediate.stepwise_ranks_absence`. |
| G4 | closed | Narrowed to the two-part family; `ThirdParty.restraint_unranked_stepwise`; §11.3 item 5 "部分". |
| G5 | closed | "Until it switches"; `slow_withheld_two_steps`; the general case labelled as argued, not formalized. |
| G6 | closed | Availability in `MakesDifference`; `Determined`, with `Shock.determined` and `Pool.determined`; `Hidden`, `Tagged`; the modelling instruction corrected. Root doc wording (H2). |
| G7 | closed | Gloss narrowed to structural coincidence; `Later.drawing_connects_earlier`, `Pinned.drawing_interacts`. |
| G8 | closed, one residual | `one_use_connects`; condition-correspondence-discipline corrected. becoming-renewal-reading keeps the old wording (H3). |
| G9 | closed | `drawing_reaches`; "Q5 只排除共同依存的一半". |
| G10 | closed | "纪律所省略的关系（经由共同条件的共同构成）". |
| G11 | closed for the named locations | §9, joint-difference-making, §8.2, chapter §6.3, the English P7b bullet and becoming-finite-horizon corrected. Two unnamed sentences in §8.5 keep "Ren 的判决" (H3). |
| G12 | closed | Per-stage counts in §9; ranking record limitations and counterexamples; glossary entries 交互, 承担, 惰性条件; §8.5 last paragraph narrowed. |

## 2. Findings

### H1. missing counterexample: a grown need erases the met history, so stunting is neither breaking nor undermining

**Location.**

- `Becoming.Dependence` module doc (lines 53–62) and the `MetSince` docstring.
- Study §12.1 G1 row; §12.3 item 1 ("重定义 `MetSince`…：完成（G1）"); §12.4 rebuttal 1 ("修正把它定为不算，并以 `RisingNeed` 写明，所以它是公开的选择，不是隐去的反例").
- Record becoming-stepwise-reading: `counterexamples` and `limitations`.

**What the Lean says.** `MetSince t g c := ∃ s ≤ t, (tenure from s to t) ∧ need s ≤ level s ∧ need t ≤ need s`, and `UnderminingOn` asks `level (t+1) < need t`. Once the need has grown above every need that was met, no `s` qualifies.

**Evidence.** `Stunted.grown_need_erases_met_level`:

- The web is `Dependent`.
- The grower depends on the condition at every step. It needs 1 at step 0, which is met at level 1, and 2 from step 1 on, which is never met.
- The drawer draws from step 1, and its step 1 takes the level from 1 to 0, below the need of 1 that was met at step 0.
- That step breaks nothing, because the grown need was not met at step 1.
- The drawer undermines at no step, yet the whole-run reading counts it consuming.

**Why it matters.** The case is ordinary: a juvenile, a growing settlement or a developing capacity whose need has grown. A draw that takes the condition below even what it once had, and below what it needs now, is invisible to the stepwise reading, while a dependent whose need stayed constant would make the same draw undermining. §12.4 presents the rising-need choice as public and costless ("不是隐去的反例"); this is the hidden cost.

**Correction.** Use the minimum form, `UnderminingMin` in the appendix: the drawer draws, and after the step the level is below **both** a need met during the unbroken tenure **and** the present need. Its properties:

- `undermining_min`: every event that undermines under the published definition undermines in the minimum form.
- `min_undermining`: with constant needs the two forms agree, so every existing witness is unchanged.
- `min_form_separates`: the minimum form counts `Stunted` and still excludes `FallingNeed`, `RisingNeed` and `Gap.away`.
- `BreakingOn.undermining` survives (argued: take `s = t`).

Read in words: the draw fails a need that was met and fails the present one. Growth beyond what was ever met still does not count, which keeps `RisingNeed`; a fall below what was met does count. If the published form is kept instead, add `Stunted` as a counterexample, say in §12.4 and the module doc that "a draw below a once-met need is not undermining after the need has grown", and change §12.3 item 1 to "部分完成".

### H2. presentation: the root doc writes `Determined` into the definition, and the dichotomy needs a third condition

**Location.** [Becoming.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming.lean) line 34 ("difference-making, relative to a move that determines the step and can still be taken once a part is withheld"); `Becoming.Joint` module doc lines 13–17 ("It reads as intended when the move determines the step … and can be taken from every withheld configuration").

**What the Lean says.** `MakesDifference` contains availability, `∃ t, P.step (withhold f s) a t`, but not `Determined`. `Determined` is a separate definition; no theorem takes it as a hypothesis, and it is proved only for `Shock` and `Pool`. §12.3 item 5 says so ("不作为定义的前提"), which is correct.

**Evidence.** `determined_dichotomy`. Assume four things: the process is `Determined`, the move breaks the dependence, the move is available from the withheld configuration, and the dependence still holds and is met there. Then either the withheld part makes the difference, or the same move breaks the dependence from the withheld configuration. Without the last assumption there is a third case, immediate from the definitions. If withholding the part leaves the dependence unmet (the part was itself a support), `Keeps` and `Breaks` both fail at the withheld configuration, so neither disjunct holds.

**Why it matters.** The root doc is the first summary a reader meets, and it describes a definition that is not the one in `Joint`. The third case is the familiar one in which the withheld part is a supporter. The test then says neither "it made the difference" nor "the loss happens anyway".

**Correction.** Root doc: "relative to a move that can still be taken once a part is withheld; it reads as intended when the move determines the step (`Determined`)". In the `Joint` doc, add: "and the dependence still holds and is met with the part withheld; when withholding the part itself leaves the dependence unmet, the test is silent". Optionally add `determined_dichotomy` as a theorem.

### H3. presentation: two residuals of G8 and G11

- **G8.** Record becoming-renewal-reading, `correspondence`: "它排除不了人人汲取并依存的被更新条件" / "does not exclude a renewed condition every formation draws on and depends on". After `one_use_connects`, this should read "a renewed condition every formation depends on at a positive level, used once by one living event". P9b, P10 and P11 changed only that record's validation scope and hashes.
- **G11.** Study §8.5, lines 384 ("Ren 的判决是否要求越过阈值之前的事件按整段分类来判") and 387 ("能否给出 Ren 的判决"). G11 did not name these two sentences, but they make the same attribution. Write "对 Ren 所采纳的问题的判决", as chapter §6.3 now does.

### H4. overclaim (definition): `Paid` is tied neither to the arising formation nor to the step at which it draws

**Location.**

- `Web.Paid` and its docstring; the `Generation` module doc ("If each arising at a step where no condition of a finite family rises lowers one of them").
- Study §13 Delta, "Supplied premises" and rebuttals 2–3 ("它是对应前提：生成不是无代价的，形成须从条件中取得"; "每次在没有更新之步的生起都付出条件").
- Chapter §2 line 191 ("若生起由一个有限条件家族的下降支付"); the §8 row ("生起须支付").
- Record unceasing-generation-needs-renewal: `hypotheses` ("Generation is not free"), `claim` and `title`.

**What the Lean says.** `Paid cs event := ∀ t, event t → Still cs t → ∃ c ∈ cs, Falls t c`. With `event := fun t => ∃ f, Arises t f`, it mentions neither `f`'s `requires` nor its `draws`. It looks at the arising step itself, the step from `t` to `t + 1`, at whose end the formation first becomes active.

**Evidence.**

- `paid_iff`: `Paid cs event` holds exactly when at every event step some condition of the family rises or falls. So `Unceasing.rises` says: at infinitely many steps some condition of a finite natural-valued family changes, so some condition rises at infinitely many steps. Arising marks the steps and does nothing else.
- `Tide.unrelated_payment`: a tide alternates 0, 1, 0, 1. A flicker that neither requires nor draws on anything arises at every odd step, and each arising is "paid" by the tide's fall. The family `[()]` meets `Dependent`, `RenewedBy`, `Paid` and `Unceasing`, so every premise of `regeneration_recurs` holds.
- `bloom_paid_vacuously`: every arising of the bloom happens at a step where its condition **rises**. The bloom becomes active when the sun has restored its support, and it draws at the next step. So the positive witness of P10 meets `Paid` only vacuously: no arising there is paid by a fall.
- `trivial_renews`: with `renews := True`, the conclusion of `regeneration_recurs` follows from `Unceasing` alone. The theorem's "renewing activity recurs" is therefore only as strong as the application's `renews`. The record says that `renews` is an application duty. `Balances.renewedBy` in P11 supplies a substantive one.

**Why it matters.** Rebuttal 2 reads the premise as "a formation must take from conditions". The definition says something weaker and differently timed. Where activity is gated by support, as in `Bloom` and the study's support-gated laws, a formation arises when its condition is restored and takes afterwards, so `Paid` checks the wrong step. The theorem is correct; what it shows about generation rests on a premise whose gloss does not match it.

**Correction.**

- Either tie the premise to the arising formation at its first active step. In flow terms: `∀ t f, Arises t f → f ∈ L.present (t+1) ∧ 0 < total cs (L.take (t+1) f)`. This implies the premise `fed` of `unceasing_supplied` (H5); the implication is argued, not formalized, and goes through `takers_le_load`.
- Or keep `Paid` and gloss it accurately: "at each arising step at which no condition of the family rises, one of them falls (whatever its relation to the arising formation)". Then drop "形成须从条件中取得" from rebuttal 2, and add `Tide` and `bloom_paid_vacuously` to the record.

### H5. missing counterexample: the strictness witness has no rise, and P10's renewal cannot see concurrent renewal

**Location.**

- Study §13 bullet 1 ("不息的生成严格强于复现的更新：… 更新复现却可以没有任何生起（`renewal_without_generation`）"); the English P10 paragraph.
- Chapter §2 lines 191 and 193 ("renewal can recur with nothing arising").
- Record unceasing-generation-needs-renewal: `claim` and `counterexamples`.
- Study §14 bullet 4 ("在平衡的流中它是定理").

**What the Lean says.** The conclusion of `Unceasing.rises` and `regeneration_recurs` is renewal in the sense of `Rises`, a net rise in level, made by a `Regenerating` formation. `Commons.renewal_without_generation` shows `Renewed ()`, which is every dependence kept, and no arising.

**Evidence.**

- `commons_sharing_never_rises`: in the cited witness the level is constant, so nothing rises. Renewal there is in the dependence sense, not in the sense the implication concludes.
- `Tide.renewal_recurs_without_arising`: with the flicker removed, the tide rises at arbitrarily late steps, every rise is made by the moon, `Regenerating` recurs, and generation is not unceasing. This is a witness of strictness in P10's own sense. So the claim is true; it is the citation that is mismatched.
- `garden_unpaid`: P11's paradigm `Garden` is `Unceasing`, never rises, and fails `Paid [()]`. There, renewal concurrent with drawing keeps the level constant, and `Rises`, `Paid` and `RenewedBy` cannot see it. P10's "unceasing generation needs renewal" therefore does not apply to the main witness of P11, although §14 presents P11 as continuing P10.
- `unceasing_supplied` (positive): in a balanced flow where the family is drawn on at the step after each arising (`fed`), unceasing generation needs the family to be given something at arbitrarily late steps. `fed_witnesses`: both `Garden` and `Bloom` meet `fed`. With `Acting`, the giving is done by active formations.

**Why it matters.** "Unceasing generation needs renewal" is P10's headline. In net-rise terms it covers only unfoldings in which arising happens where the family stays still and some condition falls. The flow form covers sustained concurrent renewal and makes the P10–P11 chain coherent.

**Correction.** Cite `Tide.still` (or an equivalent with rises) for strictness, and describe the Commons witness as "dependence kept, no arising". State that `Rises` is a net rise and that concurrent renewal falls outside `Paid` (`Garden`). Add the flow form, `unceasing_supplied` with `fed` tied to the arising formation (H4), as the general statement; P10's form is then its net-rise special case.

### H6. overclaim: "no finite part is unceasing on its own" needs dissipation

**Location.**

- Study §13 bullet 3: "一个总水平从不上升的有限家族，即每次更新都由它自身的下降支付，不能维持不息的生成（`conserved_ceases`）……若把太阳的条件放进家族并照实支付，生成会停止。所以在这些前提下，任何有限部分都不能独自不息".
- Study rebuttal 4: "`conserved_ceases` 说明，把太阳自身的条件也照实计入时，有限的部分不能独自不息".
- Chapter §2 line 191: "总水平从不上升的有限家族不能维持不息的生成；作者由此论证，任何有限部分都不能独自不息".
- Record unceasing-generation-needs-renewal, `correspondence` (zh and en): "a finite family whose total never rises cannot be unceasing, so no finite part is unceasing on its own".

The record `claim`, the module doc and the English summary state the premise ("that lowers it").

**What the Lean says.** `conserved_ceases` has two premises: `conserved`, that the total never rises, and `costly`, that every arising strictly lowers the total.

**Evidence.** `Recycle.closed_unceasing`:

- One unit moves between two pools. The bloom depends on pool `a` at need 1 and draws on it, passing the unit to `b`. The carrier returns it.
- The web is `Dependent`. `RenewedBy`, `Paid` and `Unceasing` hold, so every premise of `regeneration_recurs` holds. `Paid` holds because each arising step is one at which `a` rises.
- The total is constant, so it never rises, and no arising lowers it.

A closed finite family thus sustains unceasing generation on its own. The three places that omit `costly` state something false of the definitions.

**Why it matters.** The inference "every finite part needs something beyond itself" is what makes unceasing generation "belong to the larger unfolding". Material cycles such as nutrient cycling meet `conserved` without `costly`. The argument goes through for a quantity that every arising dissipates; read for free energy, that is a second-law premise. That premise is physical, not a consequence of the theorem.

There is a second dependence on units. `stock` adds levels across conditions, so whether a step conserves or lowers the total depends on the units chosen for each condition: an arising that moves one unit from `a` to `b` lowers `2a + b` and conserves `a + b`. The nondual method says "Do not silently assume that all conditions are owned, transferable, additive, scarce or commensurable". `paid_finitely` and `Unceasing.rises` do not depend on units, because the total is only a descent measure there; any positive weighting works (argued). `conserved_ceases` does depend on them.

**Correction.** In the four places, state the premise: "每次生起都使封闭家族的总水平下降（耗散）". Add: "物质循环不满足它（`Recycle`）；对每次生起都耗散的量（例如自由能）成立". State `conserved_ceases` for a single condition or for a stated weighting, and disclose that the total presupposes commensurable units.

### H7. presentation (provenance): `Arises` as "the second 生 of 生生", and "generation by consumption"

**Location.**

- The `Generation` module doc ("This module states the second 生 of 生生"; "Generation by consumption ceases").
- Study §13 intro ("本节在核心上陈述生生的第二个“生”"), Delta ("以消耗进行的生成停止") and bullet 2 ("以消耗进行的生成不能不息……只有退化的一侧不能不息").
- Chapter §2 line 191 ("生生的第二个“生”这样陈述"; "生起以消耗进行，生成停止") and line 193 ("Generation by consumption ceases").
- Record unceasing-generation-needs-renewal, `correspondence` ("只有退化的一侧不能不息，与 Ren 所说的生成与退化不重叠相合").

**What the Lean says.** `Arises t f := ¬ active t f ∧ active (t+1) f`. It does not ask that `f` be new, living under any reading, renewing, or persistent. `Growth.ceases` calls cells that arise while consuming an unrenewed condition "generation".

**Evidence.** Ren, 2026-10-09: "为什么？我G0是什么？generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧" ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)). The source's AI correction note says that reading the formal `generative` as "any realized new organization" is the AI's formalization reading, not Ren's G0. It also says that "持续" in "持续形成新组织" already excludes the consuming type.

P10 uses "生成" for every arising, consuming arisings included, and then says the result accords with non-overlap. The non-overlap it proves is at the level of continuation: under `Paid`, arising on unrenewed conditions ceases. At the level of single events, `Arises` includes consuming arisings. In fact the result **supports** the AI note's claim that "持续" excludes consumption, under P10's premises; that is worth stating as such.

**Why it matters.** Calling every arising "the second 生 of 生生" is a reading of Ren's words. It is broader than the scopes Ren accepted ("我觉得这几个都很有意义，都可以是", [source](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)), each of which concerns 生, not becoming active. Yet it is not labelled as the author's reading; only "stated on the whole" is labelled. "Generation by consumption" uses the very term Ren separated from degeneration. "Only the degenerative side cannot be unceasing" says more than is shown: the theorems show that arising paid by unrenewed conditions ceases, and that unceasing arising is consistent with renewal in one witness. They do not show that every non-consuming pattern can be unceasing, and `Commons.sharing` renews with no arising at all.

**Correction.**

- Gloss `Arises` as "arising (becoming active), the formal carrier of one reading of the second 生 (author's reading)".
- Rename "generation by consumption" to "arising on a consumed condition / 以消耗为条件的生起".
- In the record: "在这些前提下，由不被更新的条件支付的生起不能不息；在继续的层面，这与 Ren 所说的生成与退化不重叠相合（作者的读法）；在单个事件的层面，`Arises` 包括以消耗为条件的生起".
- Leave the scope of 生 for the second 生 to Ren.

### H8. overclaim: "strict hierarchy". More without end does not imply unceasing generation

**Location.**

- Chapter §2 line 195 ("所以复现的更新、不息的生成与不止地更多构成严格的层级，每一层需要的更新都比前一层多") and line 197 ("form a strict hierarchy").
- Study §14 bullet 1 ("一个层级") and the English P11 paragraph ("So recurring renewal, unceasing generation and more without end form a strict hierarchy").
- Record more-needs-renewers, `claim` (zh and en). The same record's `next_delta` lists "whether more implies unceasing under stated correspondence" as open.
- The `Flow` module doc ("each needs more renewal than the one before it") is closer, but it mixes P10's net-rise sense with the flow sense.

**What the Lean says.** `Bloom.not_more` gives `Unceasing ∧ ¬ More`, and `renewal_without_generation` gives renewal with no arising. Nothing proves `More → Unceasing`, and nothing proves "unceasing needs renewal" in flow terms.

**Evidence.**

- `more_without_arising`: Garden's flow with every formation active at every step. `Balances`, `Acting`, `Capacity 1`, `Dependent` and `More` hold, and nothing ever arises, so `¬ Unceasing`.
- `garden_unpaid`: P10's link from unceasing generation to renewal does not reach `Garden` (H5).
- What holds is a chain of necessary conditions in flow terms:
  - unceasing generation (with `fed`) needs the family to be given something at arbitrarily late steps (`unceasing_supplied`);
  - more without end needs what it is given to have no eventual bound (`supply_unbounded`);
  - the second condition implies the first;
  - `Bloom` meets the first and not the second, so the chain is strict.

**Why it matters.** "Strict hierarchy" is P11's summary result in the chapter, the record claim and the English summary. As stated, it suggests that each level contains the previous one. It does not; and the record lists the missing implication as open while its claim asserts the hierarchy.

**Correction.**

- Write: "在平衡的流中，三者各自所需的更新构成严格的层级：不息的生成（家族在每次生起之后一步被取用时）需要给予在任意晚的步出现；不止地更多需要给予没有最终的界；`Bloom` 分开二者。三者本身不按蕴含排列：不止地更多不蕴含不息（`more_without_arising`）".
- Alternatively, prove `More → Unceasing` under the correspondence `active t f ↔ f ∈ present t`, with `present t` free of duplicates, and state that correspondence. Argued, not formalized: if nothing arises from step N on, the active formations from N on are among the finitely many active at N. With no duplicates, `takers` is bounded by their number, which contradicts `More`.

### H9. overclaim (correspondence): `More` counts takers in the flow, not living or dependent formations

**Location.**

- Study §14 intro and rebuttal 2 ("这是作者的读法：更多的形成依赖同一组条件而活").
- Record more-needs-renewers, `correspondence` ("more formations living on the same conditions").
- Chapter §2 line 195 ("更多的生").
- The `Flow` module doc ("More 生 needs ever more formations renewing its conditions").

**What the Lean says.** `takers cs t` counts entries of `present t` with positive `take`. `Flow` meets `Web` only through `Balances` (levels) and `Acting` (givers are active). Nothing ties `take` to `draws` or `requires`, or `present` to `active`. The readings of `living` are defined on the web.

**Evidence.**

- `more_without_living_takers`: Garden's flow on a web in which only renewers are ever active. All premises hold, together with `Unceasing` and `More`, and no formation that takes is ever active.
- `Crowd.drawing_without_taking`: ever more formations are active, depend on the condition at need 1 and draw on it. The flow records no taking, and `More` fails.

The gap therefore runs in both directions.

**Why it matters.** The reading's gloss names 活 (living, active) and 依赖 (dependence), which are web relations that `More` does not measure. P11's structural reading of 生生 then speaks of "更多的生" on the strength of a flow count. The record's correspondence duty mentions only that the flow records actual take and give, and that `present` lists each formation once. In the scope question, the AI promised not to presuppose a quantity metric for 生 ("不会预先把“生”缩成数量指标", AI-authored, [source](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)). A count is acceptable as one labelled reading, which P11 says it is. The gloss should describe the count, not more.

**Correction.**

- Add a correspondence premise, for example `Taking W := ∀ t f c, f ∈ present t → 0 < take t f c → W.active t f ∧ W.draws t f c`, together with its converse as an application duty (`Crowd`).
- Or restate the reading as "ever more formations take from the family".
- If "living" is meant, say which reading. Under the stepwise working candidate, a taker that undermines is not living.

### H10. overclaim (undisclosed premise): a minimum uptake per taker carries `supply_unbounded`

**Location.** Study §14 (Delta, "Supplied premises", rebuttal 4) and the chapter. Both name `Capacity` as the correspondence premise for givers, but not its counterpart for takers. The record's `hypotheses` says only "amounts taken and given are natural numbers". The Lean docstring of `takers_le_load` does say "Formations taking from the family take at least one unit each".

**What the Lean says.** `takers_le_load` (count ≤ total) converts "at least K takers" into "at least K units taken". This step is valid because a positive natural number is at least 1.

**Evidence (argued, not formalized; the core has only natural numbers).** With rational amounts, let `t` takers each take `1/t` at step `t`. Then the load is 1 per step, a supply of 1 per step balances it, `More` holds, and the supply is bounded. With natural numbers this cannot happen, because the unit is fixed.

**Why it matters.** The substantive content of P11 is that more needs unbounded supply. That holds exactly when each living formation needs at least a fixed minimum uptake, which is plausible (a minimum metabolic rate) but not necessary: efficiency and miniaturization are routes to "more 生 on the same conditions". Those routes bear on Ren's words about rising possibility and complexity.

**Correction.** State the premise as a hypothesis in the record, the study and the chapter: "每个取用者每步至少取用一个单位（取用有正的下限）". Add: "取用可以无限变小时，更多的取用者不需要更多的供给".

### H11. overclaim: "越来越多 / ever more givers"

**Location.**

- Study §14 bullet 1 ("还需要给予者越来越多") and bullet 2 ("更多的生需要越来越多给予更新的形成参与").
- The English P11 paragraph ("more 生 needs ever more renewing formations").
- Chapter §2 line 195 (both phrases) and line 197 ("ever more givers").
- Record more-needs-renewers, `correspondence` (en: "more 生 needs ever more renewing formations").
- The `Flow` module doc ("More 生 needs ever more formations renewing its conditions").

**What the Lean says.** `renewers_unbounded`: `¬ ∀ t ≥ T₀, renewers t ≤ M`. That is "no eventual bound": the number exceeds every bound at arbitrarily late steps. The chapter tables, the glossary and the record title say exactly this.

**Evidence.** `Pulse.pulsed`. `half t` growers each take one unit. At step `2m`, `2m` renewers each give one; at odd steps none gives. `Balances`, `Acting`, `Capacity 1` and `More` hold. At every odd step there are zero renewers and the supply is zero.

**Why it matters.** "越来越多" and "ever more" read as eventually increasing, or at least eventually large at every step; the theorem gives neither. The study's own "持续的更多" bullet is careful about the sustained reading for takers but not for givers.

**Correction.** Either write "给予者的数目没有最终的界（可以在无穷多步上为零）", or prove the averaged statement. Argued from `accumulates`, not formalized: over any N steps from S beyond the step from which at least K formations take, the total given is at least K·N − stock S. So over long stretches the average supply, and under `Capacity` the average number of givers, grows without bound. That would justify "越来越多" in an averaged sense.

### H12. overclaim: "更多的要求沿展开传递下去，没有一个有限的部分独自承担"

**Location.** Study §14 bullet 4 ("若照实计入，它们也须被更新：更多的要求沿展开传递下去，没有一个有限的部分独自承担。这与 §13 的 `conserved_ceases` 是同一件事的两面").

**What the Lean says.** Nothing in `Flow` relates what a formation gives to what it takes or to its own conditions.

**Evidence.** `Cycle.closed_more`:

- Each formation taking part takes one unit and gives one back to the same condition, so the givers' own condition is the family and is counted.
- `Balances`, `Acting`, `Capacity 1`, `Dependent`, `Unceasing` and `More` hold.
- The family's total never changes, and `renewers = takers` at every step.

No supply from outside the family is needed, and the renewers are the takers themselves.

**Why it matters.** As in H6, the regress needs dissipation: each giving must cost the giver's conditions more than it gives. Without that premise, the AI argument states something false of the definitions. `Cycle` also bears on the structural reading of 生生. "更多的生需要越来越多给予更新的形成" is met when every living formation renews what it takes, so the "renewing formations" need not be a further class. That may be closer to 生生 than a separate class of renewers.

**Correction.** State the dissipation premise, or drop "没有一个有限的部分独自承担". Add `Cycle` to the boundary of the structural reading: "给予者可以就是取用者自身".

### H13. presentation (nondual method; Ren's vocabulary corrections): payment and ledger vocabulary in the pure core

**Location.**

- `Web.Paid`, `paid_finitely`, and "pays for only finitely many events" in `Generation`.
- "支付前提", "由家族支付", "生成不是无代价的" and "付出条件" in study §13; "Generation is not free" in the record.
- "生起须支付" in the chapter's §8 row; "由…下降支付" in chapter §2.
- `ledger`, and "账目" in study §14; `supply`.
- "给予者 / givers" next to "取用者 / takers".

**Evidence.**

- Ren on 2026-10-06: "“付费记录”? 这个词选的很诡异，太市场了，不够基本" ([source](../../../../sources/15-codex-theory-conversations/2026-10-06-nondual-core-tree-continuation.md#subsequent-wording-correction-6-october-2026)) and "why did we use recipient, money, pay in our foundation? they are not the best word choice" ([source](../../../../sources/15-codex-theory-conversations/2026-10-06-foundational-vocabulary-correction.md)).
- Ren on 2026-10-09, about the core: "if name is not the best to represent our truth, update them as well" ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-elegance-and-names)).
- The nondual method: "Do not promote payment, a fixed resource budget or a universally positive cost into a generative primitive". For a support quantity, name "depletion, replenishment or restoration / 消耗、补充或恢复 … Use payment for an actual payment". It also places scalar accounting in particular realizations.
- The method allows existing local names such as `paid` to remain. These names are new, and they sit in the pure core at its most foundational point, "unceasing generation needs renewal".

**Why it matters.** "生成不是无代价的" states a universal positive cost, which is exactly what the method declines to make primitive. In the Lean it is a premise, not a primitive, and that is to P10's credit. But the name and the gloss present it as a fact about generation.

**Correction (the reviewer's suggestions; the names are Ren's to choose).**

| Current | Suggested |
|---|---|
| `Paid` | `Depletes` |
| `paid_finitely` | `depletes_finitely` |
| 支付前提 / payment premise | 消耗前提 / depletion premise |
| 生成不是无代价的 | 在没有补充之步，生起消耗家族中的某个条件 |
| `ledger` / 账目 | 消耗与补充的平衡 / balance of depletion and replenishment |
| `supply` | `replenishment` / 补充 |
| 给予者 | 补充者 / replenishing formations |

`renewers` and `takers` (取用者) can stay.

### H14. presentation (nondual method): the formation/condition split omits life as a condition of life

**Location.** Study §14 bullet 2 and the record's `correspondence` (the structural reading of 生生); chapter §2 line 195.

**What the Lean says.** `Web F C` and `Flow F C` relate formations to conditions. The type allows `C := F`, but nothing links a formation's activity to its level as a condition.

**Why it matters.** In 生生, living formations are conditions of further living formations: parents and offspring, a forest and its understory, a community and its learners. The structural reading says that more 生 needs more renewing formations. It cannot say that the renewing is done *by* the more 生, or that the formations are each other's conditions, except through a proxy condition. Under the nondual method this is a relation the representation omits, not a refutation. It belongs in the boundary of the reading, because the reading is offered as a sense of 生生.

**Correction.** Add to the boundary: "在 `Web` 与 `Flow` 中，形成与条件是两类：一个形成本身作为另一个形成的条件（生作为生的条件）只能经由代理条件表示，二者之间没有联系；这是表示所省略的关系".

## 3. What remains sound

- **The theorems.** Every P9b, P10 and P11 theorem holds as stated: the proofs check and the axiom reports are empty in the 17-module core closure recompiled from the prelude. The counts, receipt, hashes and aliases are correct.
- **P9b.**
  - The new `MetSince` excludes `FallingNeed` and `RisingNeed`, and all existing witnesses keep their conclusions.
  - `Gap` is disclosed.
  - Availability is part of `MakesDifference`. `Determined` holds for `Shock` and `Pool`, and `Hidden` and `Tagged` are correct.
  - `Immediate`, `ThirdParty` and `slow` are correctly stated and glossed, as are `Later`, `Pinned.drawing_interacts`, `one_use_connects` and `drawing_reaches`.
  - The practice of moving probes into the core as theorems continues.
- **P10.**
  - `stock_le`, `stock_lt`, `paid_finitely`, `Unceasing.rises`, `regeneration_recurs`, `substitution_defers` and `conserved_ceases` are correct as stated. `paid_finitely` and `Unceasing.rises` do not depend on the units of the conditions.
  - `Growth.ceases` and `Relay.defers` are fair witnesses of the ceasing side.
  - `Bloom.unceasing` and `Bloom.readings` are correct, and the cost that the stepwise reading credits no bloom is disclosed.
  - Rebuttal 3, that a flickering formation counts as unceasing, is a fair concession.
  - `RenewedBy` forbidding a source outside the unfolding, with the sun as one of the formations, is a sound use of the nondual method (rebuttal 4), within H6.
- **P11.**
  - `ledger`, `accumulates`, `takers_le_load`, `supply_le`, `supply_unbounded` and `renewers_unbounded` are correct.
  - `Balances.renewedBy` turns P10's `RenewedBy` into a theorem with a substantive `renews`. This is real progress.
  - Rebuttal 4 is correct: `supply_unbounded` needs no `Capacity`.
  - `Garden.more` and `Bloom.not_more` are correct. The sustained reading of `More` and the duplicates in `present` are disclosed (bullet 3, rebuttal 3).
  - A formation can both take and give, so the roles are not fixed kinds.
  - The chapter's §8 row, §9 table and glossary entries for 生起, 不息, 流 and 不止地更多 match the Lean.
- **Labelling.** Ren's words are quoted exactly. The readings are labelled "作者的读法" and the further interpretations "AI 论证". Neither P10 nor P11 states diversity, complexity or possibility, or claims an ethical ranking. No reading of `living` is chosen for Ren. The records state "尚无独立反审".

## 4. What would change these verdicts

1. **`MetSince`.** Adopting the minimum form, `UnderminingMin`, in `UnderminingOn`, `UnderminingFor` and `Web.relations`, or disclosing `Stunted`. G1 and H1 would close.
2. **`Paid`.** Tying `Paid` to the arising formation at its first active step, or restating P10 in flow form (`unceasing_supplied` with a tied `fed`). H4 and H5 would close, and "unceasing generation needs renewal" would cover `Garden`.
3. **Dissipation.** A dissipation premise stated in the AI arguments, or the arguments withdrawn. H6 and H12 would close. A dissipative flow theorem in which every giving costs the giver more than it gives would make the regress argument a theorem.
4. **`More → Unceasing`.** A theorem under `active ↔ present` with no duplicates (argued in H8). "Strict hierarchy" would then hold as an implication under a stated correspondence.
5. **`Taking`.** A correspondence `Taking` tying `take` to `active` and `draws`, and its converse as a duty. H9 would close.
6. **Minimum uptake.** An explicit premise, or rational amounts with a stated floor. H10 would close.
7. **Averaged "ever more".** The averaged theorem argued in H11. The wording "越来越多" could then stay, in its averaged sense.
8. **Names.** Renames following Ren's vocabulary corrections (H13), and a boundary sentence on life as a condition of life (H14).
9. **Ren's choices.** Ren's choice of the scope of 生 for the second 生 and for 更多, and Ren's words on whether consuming arisings are 生成 at all. These would settle H7 and the provenance half of H9.

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 against the unchanged `c48ec435` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. All three probe files compile with exit 0 and no warnings. `Audit.lean` prints the axioms of 227 declarations, every one of which reports "does not depend on any axioms". `Names.lean` (328 `#check @` lines), `Aliases.lean` (205) and `AliasesBridge.lean` (31) are mechanical name checks and are not reproduced; their hashes and results are in §0.

### `P9bProbes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P9b, P10 and P11: the P9b part

Each probe is a minimal model satisfying the published definitions at `c48ec435`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P11Probe

open Becoming

/-! ## K1. A grown need erases the met history: stunting is neither breaking nor undermining -/

namespace Stunted

inductive F where
  | grower
  | drawer

/-- The level is 1 at steps 0 and 1 and 0 from step 2. The grower depends on the
condition throughout; it needs 1 at step 0 (met) and 2 from step 1 (never met), and is
active at step 0 only. The drawer draws from step 1, and its step 1 takes the level from
1 to 0, below the need that was met. -/
def web : Web F Unit where
  level t _ := match t with
    | 0 => 1
    | 1 => 1
    | _ + 2 => 0
  active t f := match f with
    | .grower => t = 0
    | .drawer => 1 ≤ t
  requires _ f _ := match f with
    | .grower => True
    | .drawer => False
  need t f _ := match f with
    | .grower => match t with
      | 0 => 1
      | _ + 1 => 2
    | .drawer => 0
  draws t f _ := match f with
    | .grower => False
    | .drawer => 1 ≤ t

theorem level_le_one : ∀ t, web.level t () ≤ 1
  | 0 => Nat.le_refl 1
  | 1 => Nat.le_refl 1
  | _ + 2 => Nat.zero_le 1

theorem need_late : ∀ t, 1 ≤ t → web.need t .grower () = 2
  | _ + 1, _ => rfl

/-- The grower's dependence holds without a break and was met at step 0 at need 1. The
drawer's step 1 takes the level from 1 to 0, below that met need. The step breaks
nothing (the grown need 2 was not met at step 1), the drawer undermines at no step, and
the whole-run reading counts it consuming. -/
theorem grown_need_erases_met_level :
    web.Dependent ∧
    (∀ t, web.requires t .grower ()) ∧
    web.need 0 .grower () ≤ web.level 0 () ∧
    web.draws 1 .drawer () ∧ web.level 2 () < web.need 0 .grower () ∧
    ¬ web.Broken 1 .grower () ∧
    (∀ t, ¬ web.UnderminingAt t .drawer) ∧
    web.ConsumingIn .drawer :=
  ⟨fun t f active c depends => match f, active, depends with
    | .grower, active, _ => by
      show web.need t .grower () ≤ web.level t ()
      subst active
      exact Nat.le_refl 1,
   fun _ => trivial, Nat.le_refl 1, Nat.le_refl 1, Nat.zero_lt_one,
   fun ⟨_, met, _⟩ => Nat.not_succ_le_self 1 (Nat.le_trans met (level_le_one 1)),
   fun t ⟨(), drawn, g, depends, ⟨s, _, _, met, noMore⟩, _⟩ => match g, depends with
    | .grower, _ => Nat.not_succ_le_self 1
        (Nat.le_trans (Nat.le_of_eq (need_late t drawn).symm)
          (Nat.le_trans noMore (Nat.le_trans met (level_le_one s)))),
   ⟨1, (), Nat.le_refl 1, .grower, 1, trivial, fun t _ =>
     Nat.lt_of_le_of_lt (level_le_one t) (Nat.lt_succ_self 1)⟩⟩

end Stunted

/-! ## K2. A minimum form of undermining excludes the three P9b witnesses and keeps K1 -/

section MinForm

variable {F C : Type}

/-- Undermining read through the smaller of the need then and the need now: the drawer
draws, and after the step the level is below both a need met during the unbroken tenure
and the present need. -/
def UnderminingMin (W : Web F C) (t : Nat) (f : F) : Prop :=
  ∃ c, W.draws t f c ∧ ∃ g, W.requires t g c ∧ ∃ s, s ≤ t ∧
    (∀ u, s ≤ u → u ≤ t → W.requires u g c) ∧ W.need s g c ≤ W.level s c ∧
    W.level (t + 1) c < W.need s g c ∧ W.level (t + 1) c < W.need t g c

/-- Every undermining event under the published `MetSince` is undermining in the
minimum form. -/
theorem undermining_min {W : Web F C} {t : Nat} {f : F} :
    W.UnderminingAt t f → UnderminingMin W t f
  | ⟨c, drawn, g, depends, ⟨s, le, tenure, met, noMore⟩, fell⟩ =>
    ⟨c, drawn, g, depends, s, le, tenure, met, Nat.lt_of_lt_of_le fell noMore, fell⟩

/-- With constant needs the two forms agree. -/
theorem min_undermining {W : Web F C} {t : Nat} {f : F}
    (constant : ∀ s u g c, W.need s g c = W.need u g c) :
    UnderminingMin W t f → W.UnderminingAt t f
  | ⟨c, drawn, g, depends, s, le, tenure, met, _, fell⟩ =>
    ⟨c, drawn, g, depends, ⟨s, le, tenure, met, Nat.le_of_eq (constant t s g c)⟩, fell⟩

end MinForm

/-- The minimum form counts the stunting draw, and still counts no drawer of
`FallingNeed`, `RisingNeed` or the lapsed `Gap.away`. -/
theorem min_form_separates :
    UnderminingMin Stunted.web 1 .drawer ∧
    (∀ t, ¬ UnderminingMin FallingNeed.web t .drawer) ∧
    (∀ t, ¬ UnderminingMin RisingNeed.web t .drawer) ∧
    (∀ t, ¬ UnderminingMin Gap.away t .drawer) :=
  ⟨⟨(), Nat.le_refl 1, .grower, trivial, 0, Nat.zero_le 1, fun _ _ _ => trivial,
     Nat.le_refl 1, Nat.zero_lt_one, Nat.zero_lt_two⟩,
   fun _ ⟨_, _, g, depends, s, _, _, met, _, _⟩ => match g, depends with
    | .late, _ => Nat.not_le_of_gt (FallingNeed.unmet s) met,
   fun t ⟨_, _, g, depends, s, _, _, met, below, _⟩ => match g, depends with
    | .grower, _ =>
      if early : s < 5 then
        Nat.not_le_of_gt below (Nat.le_trans
          (Nat.le_of_eq (RisingNeed.need_early early)) (RisingNeed.level_pos (t + 1)))
      else
        Nat.not_succ_le_self 1 (Nat.le_trans
          (Nat.le_of_eq (RisingNeed.need_grown (Nat.ge_of_not_lt early)).symm)
          (Nat.le_trans met (Nat.le_of_eq (RisingNeed.level_late (Nat.ge_of_not_lt early))))),
   fun _ ⟨_, drawn, g, depends, s, _, tenure, met, _, _⟩ => match g, depends with
    | .migrant, _ =>
      if early : s < 4 then tenure 3 (Nat.le_of_lt_succ early) drawn rfl
      else Nat.not_succ_le_zero 0
        (Nat.le_trans met (Nat.le_of_eq (Gap.levels_low (Nat.ge_of_not_lt early))))⟩

/-! ## K3. With a determined step and an available move, the but-for test is a dichotomy -/

section Dichotomy

variable {S A F C : Type}

/-- When the move determines the step, is available from the withheld configuration,
and the dependence still holds and is met there, either the withheld part makes the
difference or the same move still breaks the dependence from the withheld
configuration. -/
theorem determined_dichotomy (K : Dependence S F C) {P : Generative.Process S A}
    (determined : Determined P) {withhold : F → S → S} {f : F} {s : S} {a : A} {g : F}
    {c : C} (breaks : K.BreaksBy P s a g c) {t₀ : S}
    (available : P.step (withhold f s) a t₀) (depends : K.requires (withhold f s) g c)
    (met : K.need (withhold f s) g c ≤ K.level (withhold f s) c) :
    K.MakesDifference P withhold f s a g c ∨ K.BreaksBy P (withhold f s) a g c :=
  match Nat.lt_or_ge (K.level t₀ c) (K.need (withhold f s) g c) with
  | .inl fell => .inr ⟨t₀, available, depends, met, fell⟩
  | .inr held => .inl ⟨breaks, ⟨t₀, available⟩, fun _ step =>
      (determined _ _ _ _ available step) ▸ (⟨met, held⟩ : K.Keeps (withhold f s) t₀ g c)⟩

end Dichotomy

end P11Probe
```

### `P10Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P9b, P10 and P11: the P10 part

Each probe is a minimal model satisfying the published definitions at `c48ec435`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P11Probe

open Becoming

section General

variable {F C : Type}

/-! ## N1. `Paid` says only that some condition of the family changes at the event's step -/

/-- Constructively, across each step some condition of a finite family rises, or none
does. -/
theorem rises_or_still (W : Web F C) (t : Nat) :
    ∀ cs : List C, (∃ c, c ∈ cs ∧ W.Rises t c) ∨ W.Still cs t
  | [] => .inr fun _ mem => nomatch mem
  | c :: cs => match Nat.decLt (W.level t c) (W.level (t + 1) c) with
    | isTrue rises => .inl ⟨c, .head cs, rises⟩
    | isFalse flat => match rises_or_still W t cs with
      | .inl ⟨d, mem, rises⟩ => .inl ⟨d, .tail c mem, rises⟩
      | .inr still => .inr fun d mem => match mem with
        | .head _ => flat
        | .tail _ mem => still d mem

/-- `Paid` holds exactly when, at every step of the event, some condition of the family
rises or falls. -/
theorem paid_iff (W : Web F C) (cs : List C) (event : Nat → Prop) :
    W.Paid cs event ↔ ∀ t, event t → ∃ c, c ∈ cs ∧ (W.Rises t c ∨ W.Falls t c) :=
  ⟨fun paid t happens => match rises_or_still W t cs with
    | .inl ⟨c, mem, rises⟩ => ⟨c, mem, .inl rises⟩
    | .inr still => match paid t happens still with
      | ⟨c, mem, falls⟩ => ⟨c, mem, .inr falls⟩,
   fun changes t happens still => match changes t happens with
    | ⟨c, mem, .inl rises⟩ => absurd rises (still c mem)
    | ⟨c, mem, .inr falls⟩ => ⟨c, mem, falls⟩⟩

/-- With `renews` unconstrained, the conclusion of `Unceasing.regeneration_recurs`
follows from unceasing generation alone: any formation active after it arises counts. -/
theorem trivial_renews (W : Web F C) {c : C} {cs : List C} (mem : c ∈ cs)
    (unceasing : W.Unceasing) (T : Nat) :
    ¬ ∀ t, T ≤ t → ∀ f, ¬ W.Regenerating (fun _ _ _ => True) cs t f :=
  fun none => match unceasing T with
  | ⟨t, f, later, _, active⟩ => none (t + 1) (Nat.le_succ_of_le later) f ⟨active, c, mem, trivial⟩

end General

/-! ## N2. An unrelated oscillating condition pays for any arising -/

namespace Tide

inductive Who where
  | moon
  | flicker

/-- Nothing at even steps, one unit at odd steps. -/
def tide : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n + 2 => tide n

theorem tide_even : ∀ n, tide (2 * n) = 0
  | 0 => rfl
  | n + 1 => tide_even n

theorem tide_odd : ∀ n, tide (2 * n + 1) = 1
  | 0 => rfl
  | n + 1 => tide_odd n

/-- The moon is always active. The flicker is active where the tide is out. Nothing
depends on or draws on the tide: no formation requires or draws on any condition. -/
def web : Web Who Unit where
  level t _ := tide t
  active t f := match f with
    | .moon => True
    | .flicker => tide t = 0
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

def renews (_ : Nat) (f : Who) (_ : Unit) : Prop :=
  match f with
  | .moon => True
  | .flicker => False

/-- Every premise of `Unceasing.regeneration_recurs` holds with the family `[()]`, the
flicker arises at every odd step, and each arising is "paid" by the tide's fall, though
the flicker neither depends nor draws on the tide. -/
theorem unrelated_payment :
    web.Dependent ∧ web.RenewedBy renews ∧
    web.Paid [()] (fun t => ∃ f, web.Arises t f) ∧ web.Unceasing ∧
    (∀ t, ¬ web.requires t .flicker () ∧ ¬ web.draws t .flicker ()) ∧
    ∀ T, ¬ ∀ t, T ≤ t → ∀ f, ¬ web.Regenerating renews [()] t f :=
  have paid : web.Paid [()] fun t => ∃ f, web.Arises t f :=
    fun _ ⟨f, inactive, active⟩ _ => match f, inactive, active with
    | .moon, inactive, _ => absurd trivial inactive
    | .flicker, inactive, active =>
      ⟨(), .head [], Nat.lt_of_le_of_lt (Nat.le_of_eq active) (Nat.pos_of_ne_zero inactive)⟩
  have made : web.RenewedBy renews := fun _ _ _ => ⟨.moon, trivial, trivial⟩
  have unceasing : web.Unceasing := fun N =>
    ⟨2 * N + 1, .flicker, Nat.le_succ_of_le (Nat.le_mul_of_pos_left N Nat.zero_lt_two),
      fun out => Nat.noConfusion ((tide_odd N).symm.trans out),
      tide_even (N + 1)⟩
  ⟨fun _ _ _ _ depends => False.elim depends, made, paid, unceasing,
   fun _ => ⟨id, id⟩, Web.Unceasing.regeneration_recurs web made paid unceasing⟩

/-- The same tide and moon with nothing arising: the tide rises at arbitrarily late
steps, every rise is made by the moon, and the moon's renewing recurs, while generation
is not unceasing. This is recurring renewal without generation in the sense of
`Unceasing.rises` and `Unceasing.regeneration_recurs`. -/
def still : Web Who Unit :=
  { web with active := fun _ f => match f with
    | .moon => True
    | .flicker => False }

theorem renewal_recurs_without_arising :
    still.RenewedBy renews ∧ (∀ T, ∃ t, T ≤ t ∧ still.Rises t ()) ∧
    (∀ T, ∃ t f, T ≤ t ∧ still.Regenerating renews [()] t f) ∧ ¬ still.Unceasing :=
  ⟨fun _ _ _ => ⟨.moon, trivial, trivial⟩,
   fun T => ⟨2 * T, Nat.le_mul_of_pos_left T Nat.zero_lt_two, by
     show tide (2 * T) < tide (2 * T + 1)
     rw [tide_even T, tide_odd T]
     exact Nat.zero_lt_one⟩,
   fun T => ⟨T, .moon, Nat.le_refl T, trivial, (), .head [], trivial⟩,
   fun unceasing => match unceasing 0 with
    | ⟨_, f, _, inactive, active⟩ => match f, inactive, active with
      | .moon, inactive, _ => inactive trivial
      | .flicker, _, active => active⟩

end Tide

/-- The cited witness of renewal without generation has no rise at all: in the sharing
run of the commons the level is constant, so `RenewedBy` holds for every `renews` and
`Unceasing.rises` has nothing to say there. -/
theorem commons_sharing_never_rises :
    ∀ t, ¬ (Commons.conditions.dependence.along Commons.sharing).Rises t () :=
  fun _ rises => Nat.lt_irrefl 1 rises

/-- Every arising of the bloom happens at a step where its condition rises, so the
positive witness meets `Paid` only vacuously: no bloom's arising is paid by a fall. -/
theorem bloom_paid_vacuously : ∀ t f, Bloom.web.Arises t f → Bloom.web.Rises t () :=
  fun _ f ⟨inactive, active⟩ => match f, inactive, active with
  | .sun, inactive, _ => absurd trivial inactive
  | .bloom, inactive, active => Nat.lt_of_lt_of_le (Nat.gt_of_not_le inactive) active

/-! ## N3. A closed family that recycles sustains unceasing generation -/

namespace Recycle

inductive Pool where
  | a
  | b

inductive Who where
  | carrier
  | bloom

/-- One unit, at `a` at even steps and at `b` at odd steps. -/
def atA : Nat → Nat
  | 0 => 1
  | 1 => 0
  | n + 2 => atA n

def atB : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n + 2 => atB n

/-- The bloom depends on `a` at need 1, is active where `a` supports it and draws on it
then, passing the unit to `b`; the carrier, always active, returns it to `a`. -/
def web : Web Who Pool where
  level t c := match c with
    | .a => atA t
    | .b => atB t
  active t f := match f with
    | .carrier => True
    | .bloom => 1 ≤ atA t
  requires _ f c := match f, c with
    | .bloom, .a => True
    | .bloom, .b => False
    | .carrier, .a => False
    | .carrier, .b => False
  need _ _ _ := 1
  draws t f c := match f, c with
    | .bloom, .a => 1 ≤ atA t
    | .bloom, .b => False
    | .carrier, .a => False
    | .carrier, .b => False

def renews (_ : Nat) (f : Who) (_ : Pool) : Prop :=
  match f with
  | .carrier => True
  | .bloom => False

theorem stock_one : ∀ t, web.stock [.a, .b] t = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => stock_one t

theorem atA_even : ∀ n, atA (2 * n) = 1
  | 0 => rfl
  | n + 1 => atA_even n

theorem atA_odd : ∀ n, atA (2 * n + 1) = 0
  | 0 => rfl
  | n + 1 => atA_odd n

/-- The family's total never rises (it is constant), every premise of
`Unceasing.regeneration_recurs` holds, the bloom arises at every odd step, and no arising
lowers the total: `conserved_ceases` needs its premise that each arising lowers the
total. -/
theorem closed_unceasing :
    web.Dependent ∧ web.RenewedBy renews ∧
    web.Paid [.a, .b] (fun t => ∃ f, web.Arises t f) ∧ web.Unceasing ∧
    (∀ t, web.stock [.a, .b] (t + 1) ≤ web.stock [.a, .b] t) ∧
    (∀ t f, web.Arises t f → ¬ web.stock [.a, .b] (t + 1) < web.stock [.a, .b] t) ∧
    ∀ T, ¬ ∀ t, T ≤ t → ∀ f, ¬ web.Regenerating renews [.a, .b] t f :=
  have paid : web.Paid [.a, .b] fun t => ∃ f, web.Arises t f :=
    fun _ ⟨f, inactive, active⟩ still => match f, inactive, active with
    | .carrier, inactive, _ => absurd trivial inactive
    | .bloom, inactive, active =>
      absurd (Nat.lt_of_lt_of_le (Nat.gt_of_not_le inactive) active) (still .a (.head _))
  have made : web.RenewedBy renews := fun _ _ _ => ⟨.carrier, trivial, trivial⟩
  have unceasing : web.Unceasing := fun N =>
    ⟨2 * N + 1, .bloom, Nat.le_succ_of_le (Nat.le_mul_of_pos_left N Nat.zero_lt_two),
      fun one => Nat.not_succ_le_zero 0 (Nat.le_trans one (Nat.le_of_eq (atA_odd N))),
      Nat.le_of_eq (atA_even (N + 1)).symm⟩
  ⟨fun _ f active c depends => match f, c, active, depends with
    | .bloom, .a, active, _ => active,
   made, paid, unceasing,
   fun t => Nat.le_of_eq ((stock_one (t + 1)).trans (stock_one t).symm),
   fun t _ _ falls => Nat.lt_irrefl 1
     (Nat.lt_of_le_of_lt (Nat.le_of_eq (stock_one (t + 1)).symm)
       (Nat.lt_of_lt_of_le falls (Nat.le_of_eq (stock_one t)))),
   Web.Unceasing.regeneration_recurs web made paid unceasing⟩

end Recycle

/-! ## N4. The P11 garden is unceasing with no rise: P10's payment premise fails there -/

/-- In `Garden`, renewers and growers arise at every step, the level never rises, and
arising is not `Paid` by the family `[()]`. Concurrent renewal that balances drawing is
invisible to `Rises`, `Paid` and `RenewedBy`. -/
theorem garden_unpaid :
    Garden.web.Unceasing ∧ (∀ t, ¬ Garden.web.Rises t ()) ∧
    ¬ Garden.web.Paid [()] (fun t => ∃ f, Garden.web.Arises t f) :=
  ⟨Garden.more.2.2.2.2.2.1, fun _ rises => Nat.lt_irrefl 1 rises,
   fun paid => match paid 0 ⟨(.renewer, 0), Nat.lt_irrefl 0, Nat.zero_lt_one⟩
      (fun _ _ rises => Nat.lt_irrefl 1 rises) with
    | ⟨_, _, falls⟩ => Nat.lt_irrefl 1 falls⟩

/-! ## N5. A flow form of "unceasing generation needs renewal" covers both witnesses -/

section FlowForm

variable {F C : Type}

/-- In a balanced flow, if the family is drawn on at the step after each arising,
unceasing generation needs the family to be given something at arbitrarily late steps. -/
theorem unceasing_supplied {L : Flow F C} {W : Web F C} {cs : List C}
    (balances : L.Balances W) (fed : ∀ t f, W.Arises t f → 0 < L.load cs (t + 1))
    (unceasing : W.Unceasing) (T : Nat) : ¬ ∀ t, T ≤ t → L.supply cs t = 0 :=
  fun none =>
    have step : ∀ t, T ≤ t → W.stock cs (t + 1) + L.load cs t = W.stock cs t :=
      fun t later => (Flow.ledger balances cs t).trans
        ((congrArg (W.stock cs t + ·) (none t later)).trans (Nat.add_zero _))
    falls_finitely (W.stock cs) T
      (fun t later => Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq (step t later)))
      fun N => match unceasing (N + T) with
      | ⟨t, f, later, arises⟩ =>
        ⟨t + 1, Nat.le_succ_of_le (Nat.le_trans (Nat.le_add_right N T) later),
          Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right (fed t f arises))
            (Nat.le_of_eq (step (t + 1)
              (Nat.le_succ_of_le (Nat.le_trans (Nat.le_add_left T N) later))))⟩

end FlowForm

theorem glow_le_two : ∀ n, Bloom.glow n ≤ 2
  | 0 => Nat.le_refl 2
  | 1 => Nat.le_succ 1
  | n + 2 => glow_le_two n

/-- Both the garden and the bloom meet the premise that the family is drawn on at the
step after each arising. -/
theorem fed_witnesses :
    (∀ t f, Garden.web.Arises t f → 0 < Garden.flow.load [()] (t + 1)) ∧
    (∀ t f, Bloom.web.Arises t f → 0 < Bloom.flow.load [()] (t + 1)) :=
  ⟨fun t _ _ => Nat.lt_of_lt_of_le (Nat.zero_lt_succ t)
     (Nat.le_trans (Nat.le_of_eq (Garden.taken_eq (t + 1)).symm) (Nat.le_add_right _ 0)),
   fun t f ⟨inactive, active⟩ => match f, inactive, active with
    | .sun, inactive, _ => absurd trivial inactive
    | .bloom, _, active => by
      have two : Bloom.glow (t + 1) = 2 := Nat.le_antisymm (glow_le_two (t + 1)) active
      show 0 < 0 + (2 * (Bloom.glow (t + 1) - 1) + 0) + 0
      rw [two]
      decide⟩

end P11Probe
```

### `P11Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P9b, P10 and P11: the P11 part

Each probe is a minimal model satisfying the published definitions at `c48ec435`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P11Probe

open Becoming

/-! ## M1. More without end, nothing ever arising -/

/-- The garden's flow, with every formation active at every step. -/
def dormant : Web (Garden.Kind × Nat) Unit :=
  { Garden.web with active := fun _ _ => True }

/-- Every premise of `More.renewers_unbounded` holds and generation is more without end,
yet no formation ever arises: `More` does not imply `Unceasing`. -/
theorem more_without_arising :
    Garden.flow.Balances dormant ∧ Garden.flow.Acting dormant ∧
    Garden.flow.Capacity [()] 1 ∧ dormant.Dependent ∧ Garden.flow.More [()] ∧
    ¬ dormant.Unceasing :=
  ⟨Garden.more.1, fun _ _ _ _ _ => trivial, Garden.more.2.2.1,
   fun _ _ _ _ _ => Nat.le_refl 1, Garden.more.2.2.2.2.2.2,
   fun unceasing => match unceasing 0 with
    | ⟨_, _, _, inactive, _⟩ => inactive trivial⟩

/-! ## M2. More without end, no taker ever active -/

/-- The garden's flow, with only renewers ever active. -/
def drains : Web (Garden.Kind × Nat) Unit :=
  { Garden.web with active := fun t f => f.1 = .renewer ∧ f.2 < t }

/-- Every premise holds, generation is unceasing and more without end, and no formation
that takes is ever active: `More` counts entries that take, living or not. -/
theorem more_without_living_takers :
    Garden.flow.Balances drains ∧ Garden.flow.Acting drains ∧
    Garden.flow.Capacity [()] 1 ∧ drains.Dependent ∧ drains.Unceasing ∧
    Garden.flow.More [()] ∧
    ∀ t f, 0 < total [()] (Garden.flow.take t f) → ¬ drains.active t f :=
  ⟨Garden.more.1,
   fun t f _ mem gives => match f, gives with
    | (.renewer, _), _ => ⟨rfl, Garden.present_active t _ mem⟩
    | (.grower, _), gives => absurd gives (Nat.lt_irrefl 0),
   Garden.more.2.2.1, fun _ _ _ _ _ => Nat.le_refl 1,
   fun N => ⟨N, (.renewer, N), Nat.le_refl N, fun ⟨_, early⟩ => Nat.lt_irrefl N early,
     rfl, Nat.lt_succ_self N⟩,
   Garden.more.2.2.2.2.2.2,
   fun _ f takes ⟨renewer, _⟩ => match f, takes, renewer with
    | (.renewer, _), takes, _ => absurd takes (Nat.lt_irrefl 0)⟩

/-! ## M3. Ever more formations draw and depend; the flow records no taking -/

namespace Crowd

def present : Nat → List Nat
  | 0 => []
  | n + 1 => n :: present n

/-- Formation `n` is active from step `n + 1`, depends on the condition at need 1 and
draws on it while active. The level is 1 throughout. -/
def web : Web Nat Unit where
  level _ _ := 1
  active t n := n < t
  requires t n _ := n < t
  need _ _ _ := 1
  draws t n _ := n < t

/-- The flow lists the active formations and records that none takes or gives. -/
def flow : Flow Nat Unit := ⟨present, fun _ _ _ => 0, fun _ _ _ => 0⟩

theorem total_zero' : ∀ as : List Nat, total as (fun _ => sign (0 + 0)) = 0
  | [] => rfl
  | _ :: as => (Nat.zero_add _).trans (total_zero' as)

/-- The flow balances the web and only active formations give; ever more formations are
active, depend on the condition and draw on it, yet no formation takes and `More`
fails. `Flow.take` is not tied to `Web.draws`. -/
theorem drawing_without_taking :
    flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧
    (∀ K, ∃ T, ∀ t, T ≤ t → ∀ n, n < K → web.active t n ∧ web.requires t n () ∧
      web.draws t n ()) ∧
    ¬ flow.More [()] :=
  have none : ∀ t, flow.takers [()] t = 0 := fun t => total_zero' (present t)
  ⟨fun t _ => (congrArg (1 + ·) (total_zero (present t))).trans
      (congrArg (1 + ·) (total_zero (present t)).symm),
   fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0),
   fun _ _ _ _ _ => Nat.le_refl 1,
   fun K => ⟨K, fun _ later _ below =>
     have active := Nat.lt_of_lt_of_le below later
     ⟨active, active, active⟩⟩,
   fun more => match more 1 with
    | ⟨T, many⟩ => Nat.not_succ_le_zero 0
        (Nat.le_trans (many T (Nat.le_refl T)) (Nat.le_of_eq (none T)))⟩

end Crowd

/-! ## M4. More without end in a closed family whose total never changes -/

namespace Cycle

/-- Each formation taking part takes one unit and gives one back. -/
def flow : Flow Nat Unit := ⟨Crowd.present, fun _ _ _ => 1, fun _ _ _ => 1⟩

theorem taken_eq : ∀ t, flow.taken t () = t
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (taken_eq n)).trans (Nat.add_comm 1 n)

theorem given_eq : ∀ t, flow.given t () = t
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (given_eq n)).trans (Nat.add_comm 1 n)

theorem takers_eq : ∀ t, flow.takers [()] t = t
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (takers_eq n)).trans (Nat.add_comm 1 n)

theorem renewers_eq : ∀ t, flow.renewers [()] t = t
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (renewers_eq n)).trans (Nat.add_comm 1 n)

theorem present_lt : ∀ t n, n ∈ Crowd.present t → n < t
  | m + 1, _, .head _ => Nat.lt_succ_self m
  | m + 1, n, .tail _ mem => Nat.lt_succ_of_lt (present_lt m n mem)

/-- Every premise of `More.renewers_unbounded` holds, generation is unceasing and more
without end, and the family's total never changes: each formation renews what it takes.
No supply from outside the family is needed. -/
theorem closed_more :
    flow.Balances Crowd.web ∧ flow.Acting Crowd.web ∧ flow.Capacity [()] 1 ∧
    Crowd.web.Dependent ∧ Crowd.web.Unceasing ∧ flow.More [()] ∧
    (∀ t, Crowd.web.stock [()] (t + 1) = Crowd.web.stock [()] t) ∧
    ∀ t, flow.renewers [()] t = flow.takers [()] t :=
  ⟨fun t _ => (congrArg (1 + ·) (taken_eq t)).trans (congrArg (1 + ·) (given_eq t).symm),
   fun t n _ mem _ => present_lt t n mem,
   fun _ _ _ => Nat.le_refl 1,
   fun _ _ _ _ _ => Nat.le_refl 1,
   fun N => ⟨N, N, Nat.le_refl N, Nat.lt_irrefl N, Nat.lt_succ_self N⟩,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (takers_eq t).symm)⟩,
   fun _ => rfl,
   fun t => (renewers_eq t).trans (takers_eq t).symm⟩

end Cycle

/-! ## M5. Renewers can be absent at every other step while generation is more -/

namespace Pulse

open Garden

def growers : Nat → List (Kind × Nat)
  | 0 => []
  | n + 1 => (.grower, n) :: growers n

def renewerList : Nat → List (Kind × Nat)
  | 0 => []
  | n + 1 => (.renewer, n) :: renewerList n

def half : Nat → Nat
  | 0 => 0
  | 1 => 0
  | n + 2 => half n + 1

def isEven : Nat → Bool
  | 0 => true
  | 1 => false
  | n + 2 => isEven n

/-- `2 m` renewers at step `2 m`, none at odd steps. -/
def pulse (t : Nat) : Nat :=
  match isEven t with
  | true => 2 * half t
  | false => 0

/-- Empty at even steps; `m` at step `2 m + 1`. -/
def stored (t : Nat) : Nat :=
  match isEven t with
  | true => 0
  | false => half t

/-- At step `t`, `half t` growers each take one unit, and `pulse t` renewers each give
one. -/
def flow : Flow (Kind × Nat) Unit where
  present t := renewerList (pulse t) ++ growers (half t)
  take _ f _ := match f.1 with
    | .renewer => 0
    | .grower => 1
  give _ f _ := match f.1 with
    | .renewer => 1
    | .grower => 0

def web : Web (Kind × Nat) Unit where
  level t _ := stored t
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ f _ := f.1 = .grower

theorem half_even : ∀ m, half (2 * m) = m
  | 0 => rfl
  | m + 1 => congrArg (· + 1) (half_even m)

theorem half_odd : ∀ m, half (2 * m + 1) = m
  | 0 => rfl
  | m + 1 => congrArg (· + 1) (half_odd m)

theorem even_even : ∀ m, isEven (2 * m) = true
  | 0 => rfl
  | m + 1 => even_even m

theorem even_odd : ∀ m, isEven (2 * m + 1) = false
  | 0 => rfl
  | m + 1 => even_odd m

theorem parity : ∀ t, (∃ m, t = 2 * m) ∨ ∃ m, t = 2 * m + 1
  | 0 => .inl ⟨0, rfl⟩
  | t + 1 => match parity t with
    | .inl ⟨m, h⟩ => .inr ⟨m, congrArg (· + 1) h⟩
    | .inr ⟨m, h⟩ => .inl ⟨m + 1, congrArg (· + 1) h⟩

theorem total_append {α : Type} (q : α → Nat) (bs : List α) :
    ∀ as : List α, total (as ++ bs) q = total as q + total bs q
  | [] => (Nat.zero_add _).symm
  | a :: as => (congrArg (q a + ·) (total_append q bs as)).trans (Nat.add_assoc _ _ _).symm

theorem renewers_take (t : Nat) : ∀ n, total (renewerList n) (fun f => flow.take t f ()) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (renewers_take t n)

theorem growers_take (t : Nat) : ∀ n, total (growers n) (fun f => flow.take t f ()) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (growers_take t n)).trans (Nat.add_comm 1 n)

theorem renewers_give (t : Nat) : ∀ n, total (renewerList n) (fun f => flow.give t f ()) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (renewers_give t n)).trans (Nat.add_comm 1 n)

theorem growers_give (t : Nat) : ∀ n, total (growers n) (fun f => flow.give t f ()) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (growers_give t n)

theorem renewers_count_take (t : Nat) :
    ∀ n, total (renewerList n) (fun f => sign (total [()] (flow.take t f))) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (renewers_count_take t n)

theorem growers_count_take (t : Nat) :
    ∀ n, total (growers n) (fun f => sign (total [()] (flow.take t f))) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (growers_count_take t n)).trans (Nat.add_comm 1 n)

theorem renewers_count_give (t : Nat) :
    ∀ n, total (renewerList n) (fun f => sign (total [()] (flow.give t f))) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (renewers_count_give t n)).trans (Nat.add_comm 1 n)

theorem growers_count_give (t : Nat) :
    ∀ n, total (growers n) (fun f => sign (total [()] (flow.give t f))) = 0
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (growers_count_give t n)

theorem taken_eq (t : Nat) : flow.taken t () = half t :=
  (total_append _ _ _).trans ((congrArg (· + _) (renewers_take t _)).trans
    ((Nat.zero_add _).trans (growers_take t _)))

theorem given_eq (t : Nat) : flow.given t () = pulse t :=
  (total_append _ _ _).trans ((congrArg (_ + ·) (growers_give t _)).trans
    ((Nat.add_zero _).trans (renewers_give t _)))

theorem takers_eq (t : Nat) : flow.takers [()] t = half t :=
  (total_append _ _ _).trans ((congrArg (· + _) (renewers_count_take t _)).trans
    ((Nat.zero_add _).trans (growers_count_take t _)))

theorem renewers_eq (t : Nat) : flow.renewers [()] t = pulse t :=
  (total_append _ _ _).trans ((congrArg (_ + ·) (growers_count_give t _)).trans
    ((Nat.add_zero _).trans (renewers_count_give t _)))

theorem half_ge : ∀ K t, 2 * K ≤ t → K ≤ half t
  | 0, _, _ => Nat.zero_le _
  | K + 1, t + 2, le => Nat.succ_le_succ (half_ge K t (Nat.le_of_succ_le_succ (Nat.le_of_succ_le_succ le)))
  | _ + 1, 0, le => absurd le (Nat.not_succ_le_zero _)
  | _ + 1, 1, le => absurd (Nat.le_of_succ_le_succ le) (Nat.not_succ_le_zero _)

theorem balances_even (m : Nat) :
    web.level (2 * m + 1) () + flow.taken (2 * m) () =
      web.level (2 * m) () + flow.given (2 * m) () := by
  rw [taken_eq, given_eq]
  show stored (2 * m + 1) + half (2 * m) = stored (2 * m) + pulse (2 * m)
  unfold stored pulse
  rw [even_odd m, even_even m, half_odd m, half_even m]
  exact (Nat.two_mul m).symm.trans (Nat.zero_add _).symm

theorem balances_odd (m : Nat) :
    web.level (2 * m + 1 + 1) () + flow.taken (2 * m + 1) () =
      web.level (2 * m + 1) () + flow.given (2 * m + 1) () := by
  rw [taken_eq, given_eq]
  show stored (2 * (m + 1)) + half (2 * m + 1) = stored (2 * m + 1) + pulse (2 * m + 1)
  unfold stored pulse
  rw [even_odd m, even_even (m + 1), half_odd m]
  exact (Nat.zero_add m).trans (Nat.add_zero m).symm

/-- The flow balances, every formation is active, each gives at most one unit, and
generation is more without end; yet at every odd step no formation gives. "Renewers
with no eventual bound" is not "ever more renewers at every step". -/
theorem pulsed :
    flow.Balances web ∧ flow.Acting web ∧ flow.Capacity [()] 1 ∧ flow.More [()] ∧
    ∀ T, ∃ t, T ≤ t ∧ flow.renewers [()] t = 0 ∧ flow.supply [()] t = 0 :=
  ⟨fun t _ => match parity t with
    | .inl ⟨m, h⟩ => h ▸ balances_even m
    | .inr ⟨m, h⟩ => h ▸ balances_odd m,
   fun _ _ _ _ _ => trivial,
   fun _ f _ => match f with
    | (.renewer, _) => Nat.le_refl 1
    | (.grower, _) => Nat.zero_le 1,
   fun K => ⟨2 * K, fun t later => Nat.le_trans (half_ge K t later)
     (Nat.le_of_eq (takers_eq t).symm)⟩,
   fun T => ⟨2 * T + 1, Nat.le_succ_of_le (Nat.le_mul_of_pos_left T Nat.zero_lt_two),
     (renewers_eq _).trans (show pulse (2 * T + 1) = 0 by unfold pulse; rw [even_odd T]),
     (congrArg (· + 0) (given_eq _)).trans
       (show pulse (2 * T + 1) + 0 = 0 by unfold pulse; rw [even_odd T])⟩⟩

end Pulse

end P11Probe
```

### `Audit.lean`

```lean
import P9bProbes
import P10Probes
import P11Probes
-- probes
#print axioms P11Probe.Stunted.F
#print axioms P11Probe.Stunted.web
#print axioms P11Probe.Stunted.level_le_one
#print axioms P11Probe.Stunted.need_late
#print axioms P11Probe.Stunted.grown_need_erases_met_level
#print axioms P11Probe.UnderminingMin
#print axioms P11Probe.undermining_min
#print axioms P11Probe.min_undermining
#print axioms P11Probe.min_form_separates
#print axioms P11Probe.determined_dichotomy
#print axioms P11Probe.rises_or_still
#print axioms P11Probe.paid_iff
#print axioms P11Probe.trivial_renews
#print axioms P11Probe.Tide.Who
#print axioms P11Probe.Tide.tide
#print axioms P11Probe.Tide.tide_even
#print axioms P11Probe.Tide.tide_odd
#print axioms P11Probe.Tide.web
#print axioms P11Probe.Tide.renews
#print axioms P11Probe.Tide.unrelated_payment
#print axioms P11Probe.Tide.still
#print axioms P11Probe.Tide.renewal_recurs_without_arising
#print axioms P11Probe.commons_sharing_never_rises
#print axioms P11Probe.Recycle.Pool
#print axioms P11Probe.Recycle.Who
#print axioms P11Probe.Recycle.atA
#print axioms P11Probe.Recycle.atB
#print axioms P11Probe.Recycle.web
#print axioms P11Probe.Recycle.renews
#print axioms P11Probe.Recycle.stock_one
#print axioms P11Probe.Recycle.atA_even
#print axioms P11Probe.Recycle.atA_odd
#print axioms P11Probe.Recycle.closed_unceasing
#print axioms P11Probe.garden_unpaid
#print axioms P11Probe.unceasing_supplied
#print axioms P11Probe.glow_le_two
#print axioms P11Probe.fed_witnesses
#print axioms P11Probe.dormant
#print axioms P11Probe.more_without_arising
#print axioms P11Probe.drains
#print axioms P11Probe.more_without_living_takers
#print axioms P11Probe.Crowd.present
#print axioms P11Probe.Crowd.web
#print axioms P11Probe.Crowd.flow
#print axioms P11Probe.Crowd.total_zero'
#print axioms P11Probe.Crowd.drawing_without_taking
#print axioms P11Probe.Cycle.flow
#print axioms P11Probe.Cycle.taken_eq
#print axioms P11Probe.Cycle.given_eq
#print axioms P11Probe.Cycle.takers_eq
#print axioms P11Probe.Cycle.renewers_eq
#print axioms P11Probe.Cycle.present_lt
#print axioms P11Probe.Cycle.closed_more
#print axioms P11Probe.Pulse.growers
#print axioms P11Probe.Pulse.renewerList
#print axioms P11Probe.Pulse.half
#print axioms P11Probe.Pulse.isEven
#print axioms P11Probe.Pulse.pulse
#print axioms P11Probe.Pulse.stored
#print axioms P11Probe.Pulse.flow
#print axioms P11Probe.Pulse.web
#print axioms P11Probe.Pulse.half_even
#print axioms P11Probe.Pulse.half_odd
#print axioms P11Probe.Pulse.even_even
#print axioms P11Probe.Pulse.even_odd
#print axioms P11Probe.Pulse.parity
#print axioms P11Probe.Pulse.total_append
#print axioms P11Probe.Pulse.renewers_take
#print axioms P11Probe.Pulse.growers_take
#print axioms P11Probe.Pulse.renewers_give
#print axioms P11Probe.Pulse.growers_give
#print axioms P11Probe.Pulse.renewers_count_take
#print axioms P11Probe.Pulse.growers_count_take
#print axioms P11Probe.Pulse.renewers_count_give
#print axioms P11Probe.Pulse.growers_count_give
#print axioms P11Probe.Pulse.taken_eq
#print axioms P11Probe.Pulse.given_eq
#print axioms P11Probe.Pulse.takers_eq
#print axioms P11Probe.Pulse.renewers_eq
#print axioms P11Probe.Pulse.half_ge
#print axioms P11Probe.Pulse.balances_even
#print axioms P11Probe.Pulse.balances_odd
#print axioms P11Probe.Pulse.pulsed
#print axioms P11Probe.bloom_paid_vacuously
-- Becoming.Generation and Becoming.Flow, every declaration
#print axioms Becoming.total
#print axioms Becoming.Web.Arises
#print axioms Becoming.Web.Unceasing
#print axioms Becoming.Web.Rises
#print axioms Becoming.Web.Falls
#print axioms Becoming.Web.Still
#print axioms Becoming.Web.Paid
#print axioms Becoming.Web.RenewedBy
#print axioms Becoming.Web.Regenerating
#print axioms Becoming.Web.stock
#print axioms Becoming.Web.stock_le
#print axioms Becoming.Web.stock_lt
#print axioms Becoming.Web.paid_finitely
#print axioms Becoming.Web.Unceasing.rises
#print axioms Becoming.Web.Unceasing.regeneration_recurs
#print axioms Becoming.Web.substitution_defers
#print axioms Becoming.Web.conserved_ceases
#print axioms Becoming.Commons.renewal_without_generation
#print axioms Becoming.Growth.left
#print axioms Becoming.Growth.web
#print axioms Becoming.Growth.left_succ_le
#print axioms Becoming.Growth.left_late
#print axioms Becoming.Growth.ceases
#print axioms Becoming.Relay.Source
#print axioms Becoming.Relay.reserve
#print axioms Becoming.Relay.dependsOn
#print axioms Becoming.Relay.source
#print axioms Becoming.Relay.web
#print axioms Becoming.Relay.reserve_succ_le
#print axioms Becoming.Relay.defers
#print axioms Becoming.Bloom.Formation
#print axioms Becoming.Bloom.glow
#print axioms Becoming.Bloom.glow_even
#print axioms Becoming.Bloom.glow_odd
#print axioms Becoming.Bloom.web
#print axioms Becoming.Bloom.back
#print axioms Becoming.Bloom.renews
#print axioms Becoming.Bloom.unceasing
#print axioms Becoming.Bloom.readings
#print axioms Becoming.sign
#print axioms Becoming.count
#print axioms Becoming.steps
#print axioms Becoming.sign_le
#print axioms Becoming.sign_le_one
#print axioms Becoming.le_mul_sign
#print axioms Becoming.total_le
#print axioms Becoming.total_add
#print axioms Becoming.total_zero
#print axioms Becoming.total_mul
#print axioms Becoming.total_swap
#print axioms Becoming.total_pos
#print axioms Becoming.count_le
#print axioms Becoming.total_le_count
#print axioms Becoming.steps_ge
#print axioms Becoming.steps_le
#print axioms Becoming.Flow
#print axioms Becoming.Flow.taken
#print axioms Becoming.Flow.given
#print axioms Becoming.Flow.Balances
#print axioms Becoming.Flow.Acting
#print axioms Becoming.Flow.load
#print axioms Becoming.Flow.supply
#print axioms Becoming.Flow.takers
#print axioms Becoming.Flow.renewers
#print axioms Becoming.Flow.More
#print axioms Becoming.Flow.Capacity
#print axioms Becoming.Flow.ledger
#print axioms Becoming.Flow.accumulates
#print axioms Becoming.Flow.Balances.renewedBy
#print axioms Becoming.Flow.takers_le_load
#print axioms Becoming.Flow.supply_le
#print axioms Becoming.Flow.More.supply_unbounded
#print axioms Becoming.Flow.More.renewers_unbounded
#print axioms Becoming.Garden.Kind
#print axioms Becoming.Garden.present
#print axioms Becoming.Garden.flow
#print axioms Becoming.Garden.web
#print axioms Becoming.Garden.taken_eq
#print axioms Becoming.Garden.given_eq
#print axioms Becoming.Garden.takers_eq
#print axioms Becoming.Garden.present_active
#print axioms Becoming.Garden.more
#print axioms Becoming.Bloom.flow
#print axioms Becoming.Bloom.balances
#print axioms Becoming.Bloom.takers_le
#print axioms Becoming.Bloom.not_more
-- P9b declarations and core lemmas relied on
#print axioms Becoming.Web.MetSince
#print axioms Becoming.Web.MetSince.now
#print axioms Becoming.Web.UnderminingOn
#print axioms Becoming.Web.UnderminingFor
#print axioms Becoming.FallingNeed.web
#print axioms Becoming.FallingNeed.need_late
#print axioms Becoming.FallingNeed.need_pos
#print axioms Becoming.FallingNeed.unmet
#print axioms Becoming.FallingNeed.never_met_not_undermining
#print axioms Becoming.RisingNeed.web
#print axioms Becoming.RisingNeed.need_early
#print axioms Becoming.RisingNeed.need_grown
#print axioms Becoming.RisingNeed.level_pos
#print axioms Becoming.RisingNeed.level_late
#print axioms Becoming.RisingNeed.grown_need_not_met
#print axioms Becoming.Gap.levels
#print axioms Becoming.Gap.away
#print axioms Becoming.Gap.held
#print axioms Becoming.Gap.levels_high
#print axioms Becoming.Gap.levels_low
#print axioms Becoming.Gap.lapse_starts_afresh
#print axioms Becoming.NewNeed.never_met_not_undermining
#print axioms Becoming.Determined
#print axioms Becoming.Dependence.MakesDifference
#print axioms Becoming.Dependence.Overdetermined.no_difference
#print axioms Becoming.Shock.determined
#print axioms Becoming.Shock.move_decides
#print axioms Becoming.Pool.determined
#print axioms Becoming.Pool.difference_belongs_to_the_joint
#print axioms Becoming.Pool.within_share_undermines
#print axioms Becoming.Hidden.process
#print axioms Becoming.Hidden.shock_in_the_step
#print axioms Becoming.Tagged.process
#print axioms Becoming.Tagged.start
#print axioms Becoming.Tagged.move_unavailable
#print axioms Becoming.Ranking.Immediate.law
#print axioms Becoming.Ranking.Immediate.law_low
#print axioms Becoming.Ranking.Immediate.focal_withheld
#print axioms Becoming.Ranking.Immediate.stepwise_ranks_absence
#print axioms Becoming.Ranking.ThirdParty.courses
#print axioms Becoming.Ranking.ThirdParty.dependent
#print axioms Becoming.Ranking.ThirdParty.over_below_seven
#print axioms Becoming.Ranking.ThirdParty.stops_supports
#print axioms Becoming.Ranking.ThirdParty.focal_three
#print axioms Becoming.Ranking.ThirdParty.restraint_unranked_stepwise
#print axioms Becoming.Ranking.malignant_restraint
#print axioms Becoming.Ranking.stepwise_unranked
#print axioms Becoming.Substitution.slow
#print axioms Becoming.Substitution.slow_withheld_two_steps
#print axioms Becoming.Substitution.stepwise_credits_substitution
#print axioms Becoming.Web.drawing_reaches
#print axioms Becoming.Web.Condition.single
#print axioms Becoming.Web.one_use_connects
#print axioms Becoming.Later.web
#print axioms Becoming.Later.drawing_connects_earlier
#print axioms Becoming.Pinned.drawing_interacts
#print axioms Becoming.falls_finitely
```

### `NamesBridge.lean` (in the bridge build)

```lean
import Becoming.Bridge
#check @Becoming.Ranking.undisturbed_eq
#check @Becoming.Ranking.wholeRun_iff
#print axioms Becoming.Ranking.undisturbed_eq
#print axioms Becoming.Ranking.wholeRun_iff
```

### `NamesLast.lean`

```lean
import Becoming
#check @RelationalRenewal.fluctuating_neither
#print axioms RelationalRenewal.fluctuating_neither
```
