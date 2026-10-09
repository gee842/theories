# P8、P9 与 P7b 更正的独立审查 / Independent review of P8, P9 and the P7b corrections

2026-10-09, Asia/Bangkok. **Independent AI review by a separate agent (Claude Opus 5.5) that did not write the work under review.** It was requested within Ren's continuing instruction to pursue the Theory of Becoming and "prove the necessary proofs" ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)). This file is the only repository file the reviewer created or changed. No repository checker or render tool was run and nothing was committed.

**摘要（中文）。** 全部 P8、P9 与 P7b 的 Lean 声明在仓库外从 prelude 重新编译，公理报告为空；计数、哈希与别名都对。数学被接受。问题在定义与散文的对应上：

- `MetSince` 比较的是**现在**的所需与过去某步的水平。所需不变时，它就是“在依存成立期间曾被满足”；所需变化时不是，“在依存成立期间从未被满足的依存不使汲取者侵蚀”一句为假（G1）。依存中断一步即抹去历史（G2）。
- 逐步读法“失去与不在场的比较”须有一个被记入的焦点事件，这一假设在八处被省去（G3）。“失去的**只是**与不在场的比较”只在二元定律族中、对每步都满足所需的节制证明；有第三个形成共用条件时，逐步读法不把节制排在过度汲取之上（G4）。替代的消耗者“只在一步上不被记入”只对 `extracting` 成立（G5）。
- 相对于动作的 but-for 检验，在步骤关系是动作的函数、且动作在扣除后的配置上可取时才准确；记录中“把外来冲击写进过程”的建模指示恰会重新引入原问题（G6）。
- 交互纪律排除惰性条件，在声明的类中保持连通，没有偷渡独立实体。但它不排定时间、也不问汲取的效果，而散文说“一方的汲取落在另一方的支持上”（G7）；剩余的免费连通比记录所说更便宜（G8）；Q5 只有一半被排除（G9）；把共同依存称为“处境的相关”，应改为“表示所省略的关系”（G10）。
- 没有替 Ren 选择读法，也没有把 AI 文字当作 Ren 的原话；但“没有它更好”被写成“Ren 所采纳的判决的形式”（G11）。

## 0. Scope, materials and method

**Object.** The state of `main` at `b9954b90` (P7b), which includes P8 (`7103b4e1`) and P9 (`6e2d1f37`):

- P8: [Becoming.Ranking](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Ranking.lean); study [BECOMING-RENEWAL-READING](BECOMING-RENEWAL-READING.md) §9 and its English summary; record [ranking-under-readings](../../../../theories/becoming/results/records/ranking-under-readings.md); bridge theorems `Ranking.wholeRun_iff` and `Ranking.undisturbed_eq` in [Becoming.Bridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Bridge.lean).
- P9: [Becoming.Correspondence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean); study §10; record [condition-correspondence-discipline](../../../../theories/becoming/results/records/condition-correspondence-discipline.md).
- P7b: the corrections answering [BECOMING-P7-REVIEW](BECOMING-P7-REVIEW.md): study §11 and the edits in §§7.1, 8.1–8.7 and 9; the repaired `Web.MetSince`, `Web.UnderminingOn`, `UnderminingFor`, `Dependence.BreaksBy`, `MakesDifference`, `Overdetermined`; the new witnesses; the corrected records becoming-stepwise-reading, becoming-return-grades, becoming-finite-horizon, joint-difference-making, substitution-preserves-consumption and ranking-under-readings.
- The canonical chapter [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md) where it states these results: §2, §4, §6.3, §6.5, §8, §9 and the glossary.

**Materials.** The working tree was clean at `b9954b90c8fe…`; every file below equals its committed bytes.

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `4e0e051aff65f14e` |
| chapter `THE-THEORY-OF-BECOMING.md` | `306914ac837b2217` |
| previous review `BECOMING-P7-REVIEW.md` | `7bc5fa9ec5f0d0cc` |
| receipt `becoming-verification.json` (run `20261009T013859.515931Z`) | `22b132a24bb4503f` |
| `Becoming.lean` | `38a3c037c86ee522` |
| `Becoming/Dependence` / `Return` / `Horizon` / `Joint` | `bbca7ef1c9d8eaef` / `50a6b41474faa010` / `a7d7ad84853c9a16` / `c943547f421dbc2c` |
| `Becoming/Substitution` / `Metaethics` / `Ranking` / `Correspondence` | `9e97983f799cf216` / `8d5280463510b22a` / `3bbb2a4f4ed9dabe` / `5931ff6a3d65c72a` |
| `Becoming/Bridge` | `33f961da3d4ecaa9` |
| `GenerativeCore` / `InquirySufficiency` / `RelationalRenewal` / `RenewalComparison` | `e3daca1b729118fc` / `d4a95ca842f46ffa` / `b97719c886e3dcd0` / `438afd1164e6e594` |
| records ranking-under-readings / condition-correspondence-discipline | `25e1f18743a700f1` / `8504b10d99dfbd0f` |
| records becoming-stepwise-reading / becoming-return-grades / becoming-finite-horizon | `a96c8946fb458927` / `b25ddf0935f5342d` / `ca72b52f522bf7ed` |
| records joint-difference-making / substitution-preserves-consumption | `c7788466e11a6b86` / `f60ca27da4809a4b` |

**Read in full:** [AGENTS.md](../../../../AGENTS.md); study §§7–11 and the English summary; the two earlier independent reviews ([first](BECOMING-RENEWAL-READING-REVIEW.md), [second](BECOMING-P7-REVIEW.md)); the Lean modules listed above; the seven record JSONs; the chapter sections listed; the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). **Ren's words read:** [以关系结构分开更新型与消耗型形成](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md) and [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md), for provenance; the common-problem section of [collective destructive attractors](../../../../sources/15-codex-theory-conversations/2026-10-08-collective-destructive-attractors.md#common-problem-solving-and-awareness). **No external literature was newly read.** Ecological examples (dormancy, migration, seasonal use) are from the reviewer's prior knowledge.

**Recompilation.** In a scratch directory outside the repository, the committed bytes of the core closure were compiled in dependency order with Lean 4.29.1 (commit `f72c35b3`), `LEAN_PATH=. lean -o X.olean X.lean`: `GenerativeCore` (with `import Std` removed, as the checker does), `InquirySufficiency`, `RelationalRenewal`, `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Metaethics, Ranking, Correspondence}` and `Becoming`. All 15 exit 0 from the prelude. The 12 periphery modules that `Becoming.Bridge` imports, and the bridge itself, also exit 0.

- **Hashes.** All 28 source hashes in the receipt equal the current files. The reference hashes in the eight records touched (the seven above and becoming-dependence-dynamics) equal the current files.
- **Counts.** `^theorem` per module: Frame 11, Inquiry 6, Renewal 6, Dependence 39, Return 29, Horizon 14, Joint 16, Substitution 6, Metaethics 35, Ranking 19, Correspondence 21, Bridge 34: 236 theorems, as the receipt, the chapter and §11 state. The receipt's 451 declaration audits have empty axiom reports for every spine and bridge module; its 67 nonempty entries all belong to seven inherited periphery modules.
- **Names.** A scratch file `Names.lean` (`#check @` on all 216 aliases and proof bindings of the eight records; sha256 `1c7d2f3084b1a1bf…`) compiles: every name resolves.
- **Axioms.** `#print axioms` on 55 core declarations named in P8, P9 and P7b reports "does not depend on any axioms" for each; so do `Becoming.Ranking.wholeRun_iff` and `Becoming.Ranking.undisturbed_eq` through the bridge.

**Probes.** `P8P9Probes.lean` (sha256 `63d46c5d754b5b15…`) imports the unchanged `Becoming` and compiles with exit 0 (two unused-variable warnings). `Audit.lean` (`d92efec3e18e2c4e…`) prints the axioms of the 27 probe declarations and the 55 core declarations: 82 of 82 report "does not depend on any axioms". `AuditBridge.lean` (`468029476655e648…`) audits the two bridge theorems. The probes avoid `simp` and `omega`; `decide` is used only on closed numerals. The sources are in the appendix.

The probes are minimal models that satisfy the published definitions unchanged. Following the nondual method, they show what the definitions admit, not what actual systems usually do. Where a fuller account would exclude a probe, the relation that excludes it is what the representation omits; that is not a refutation of the theory. A probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels.** *error*: a definition does not match its stated meaning, or a stated claim is false of the definitions. *overclaim*: prose stronger than the Lean. *missing counterexample*: a relevant witness absent from the comparison or record. *presentation*: wording, provenance or bookkeeping.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Did P7b close F1–F15? Does `MetSince` formalize "met at some step while it held"? | **Eleven closed, three partly closed (F1, F6, F11); F15 closed for what it named.** The tenure clause excludes the `NewNeed` pathology. `MetSince` matches "met at some step while it held" **only when the need is constant** over the tenure. With a falling need, a dependence never met while it held makes a later drawer undermining; with a rising need, a need never met counts as once met. A one-step lapse in a dependence erases its history. | G1, G2 |
| 2. Does move-relative `MakesDifference` match its meaning? `Pool`? Joint prose? | **It matches when the step is a function of configuration and move, and the move is enabled at every withheld configuration.** Otherwise a shock inside the step relation makes the loss overdetermined again, and a move unavailable after withholding makes every part decisive vacuously. `Pool` and `Shock` satisfy both conditions, so `Pool` is correctly re-proved. Joint prose matches the Lean, except the record's instruction to write shocks "into the process". | G6, G12 |
| 3. P8: statements, `withheld_of_extends`, `credited`, `malignant_restraint` | **The Lean is correct and axiom-free, and the bridge correspondence is exact.** `withheld_of_extends` is correctly hypothesized (it needs only "credits only active events"). The `credited` hypothesis is disclosed in the theorem, the record's hypotheses and the §9 table, but **omitted in eight places** where the cost is stated. `malignant_restraint` is a fair witness **within the two-part family**; "only the comparison with absence is lost" generalizes beyond it. | G3, G4, G5, G12 |
| 4. P9: is interaction a good formalization? Are the theorems right? Any separate-entity presupposition? | **A reasonable, disclosed narrowing.** It excludes structurally inert conditions and keeps connection on the declared class. `connected_of_commons`, `significant_iff_of_commons`, `inert_connects`, `universal_connects` and `Shared.connection_by_living_use` are correctly stated and, with three caveats, correctly interpreted: interaction ignores time and effect while the gloss says it "bears on" support; the residual free connection needs only one drawing event; Q5 is only half excluded. **No separate-entity primitive is introduced**, but co-dependence should be named an omitted relation, not "correlation of situation". | G7, G8, G9, G10 |
| 5. Choices made for Ren; AI text as Ren's words | **No reading is chosen on Ren's behalf;** "working candidate, pending Ren's choice" is used consistently. No AI text is quoted as Ren's words. **One provenance slip:** the comparative form "better without it" is attributed to a verdict Ren adopted. | G11 |
| 6. Records | **Counts, hashes, aliases and validation scopes are correct** (236 theorems / 451 declaration audits, run `20261009T013859.515931Z`). Five records need corrections to claims, titles, limitations or counterexamples. | G1, G3–G8, G11, G12 |

**Status of F1–F15.**

| Item | Status | Evidence |
|---|---|---|
| F1 | partly closed | `MetSince` requires the dependence to hold from `s` to `t`; `NewNeed.never_met_not_undermining` is a theorem. The need is compared at `t`, not at `s` (G1); continuity resets on a gap (G2). |
| F2 | closed | `whole_run_credits_overdraw`, `amount_reading`, `Feedback.prefix_does_not_decide`; §8.5 constraint 1, §8.2, §8.6, chapter §6.3 and the record restated. |
| F3 | closed | `stepwise_credits_substitution`; "preserves" scoped to the whole-run reading. Its generalization to "every step but one" is new (G5). |
| F4 | closed | `Pool.within_share_undermines`, `Pinned.undermining_without_effect`; row (b) graded "部分". |
| F5 | closed | `Pinned`; §7.1 and the module doc say undermining reads co-participation in an unrestored shortfall. |
| F6 | partly closed | `BreaksBy` fixes the move; `Shock.move_decides`; `Pool` re-proved. Functionality and enabledness are unstated (G6). |
| F7 | closed | `no_finite_segment_makes_difference`, `breaking_event_makes_step_difference`; run and step tests separated in text and record. |
| F8 | closed | `LateMet.within_one_not_renewing`; "implies, not conversely". |
| F9 | closed | `cycle_reading_not_finite`; "event-level". |
| F10 | closed | `renewedWithin_zero`, `undermining_for_zero`; `p ≥ 1` stated. `escalation_undermines_for_every_cycle` still quantifies over all `p`, with the note. |
| F11 | partly closed | Criterion (a) relabelled; "adopted" replaced. Residual attribution of the comparative form (G11). |
| F12 | closed | The premise "if every formation draws on such a condition" added. |
| F13 | closed | "Four". |
| F14 | closed | "takes nothing (action 0)". |
| F15 | closed for what it named | The five records corrected; "his" replaced by "Ren's". The stepwise record's corrected claim inherits G1. |

## 2. Findings

### G1. error: `MetSince` compares the present need with a past level, so "never met while it held" holds only for constant need

**Location.**

- `Becoming.Dependence` module doc, lines 58–59 ("A dependence never met while it held makes no drawer undermining"), and the section header at line 401.
- Study §7.1, the "不侵蚀" row ("在依存成立期间从未被满足的依存不使汲取者侵蚀"); §11.1, F1 row; §11.3 item 1 ("完成"); §11.4 rebuttal 1 ("修正使定义合乎它要表达的意思（对它的一个依存，在成立期间曾被满足）"); English summary ("makes no drawer undermining through a dependence never met while it held"; "A dependence must now have been met at some step while it held").
- Chapter §2 (the bullet "在依存成立期间从未被满足的依存，不使汲取者侵蚀") and the glossary entry 侵蚀.
- Record becoming-stepwise-reading: `claim` ("a requirement never met while it held makes no event undermine"), the `NewNeed` counterexample sentence, and the P7b `history` entry ("主张中“从未被满足的依存”一句随之成立").

**What the Lean says.** `MetSince t g c := ∃ s, s ≤ t ∧ (∀ u, s ≤ u → u ≤ t → W.requires u g c) ∧ W.need t g c ≤ W.level s c`. Its docstring is accurate: "the condition met its present need". The prose reading, "met at some step while it held", is `need s ≤ level s` at some `s` in the tenure. The two coincide when the need is constant on `[s, t]`. `Web` admits changing needs: the module doc says formations "need more or less of it" (line 9).

**Evidence.**

- `FallingNeed.falling_need_undermines`. The web is `Dependent`. The level is 2 at step 0 and 0 afterwards. `late` depends on the condition at every step, needing 3 before step 5 and 1 from step 5. Its dependence is unmet at every step at which it holds and is never `Broken`. Yet `MetSince` holds from step 5 (present need 1, level 2 at step 0, when the need was 3), and every event of the drawer from step 5 undermines. The module's sentence is false of this web.
- `RisingNeed.rising_need_undermines`. The need is 1 and met at steps 0–4, then rises to 2 and is unmet from step 5. The need 2 was never met at a step at which it was the need, but `MetSince` counts it as met through the level at step 0. Every drawer event from step 5 undermines.

**Why it matters.** The P7b repair was meant to make the definition say what the prose says (§11.4 rebuttal 1). For constant needs it does. With a falling need, the original F1 pathology returns inside the tenure: a dependent never met at its own need makes later drawers undermining because an earlier level would have covered its smaller present need. A developing or recovering dependent, whose need changes, is the ordinary case the module doc names. `RisingNeed` is a second divergence: whether a dependence met at a smaller need counts as "met" when the need grows is a reading choice the prose does not state.

**Correction.** Either redefine, or narrow the prose.

- *Redefine* (the form the P7 review proposed; P7b kept the tenure but dropped the last two clauses): `∃ s ≤ t, (∀ u, s ≤ u → u ≤ t → requires u g c) ∧ need s g c ≤ level s c ∧ need t g c ≤ need s g c`. It excludes both probes. The existing witnesses have constant needs; by inspection they re-prove with the added clauses discharged by their current `met` proofs and `Nat.le_refl`. Apply it to `UnderminingFor` and `Web.relations`.
- *Narrow:* "with a constant need, a dependence never met while it held makes no drawer undermining". Add `FallingNeed` and `RisingNeed` as counterexamples.
- In both cases change §11.3 item 1 from "完成" to "部分完成" and correct the stepwise record's `history` sentence.

### G2. missing counterexample: a one-step lapse in a dependence erases its history

**Location.** The tenure clause of `MetSince`; record becoming-stepwise-reading `hypotheses` and `limitations`; study §7.1 cost column and §11.1 F1 row.

**What the Lean says.** The dependence must hold at every step from `s` to `t`. A dependence that lapses and re-forms starts a new tenure.

**Evidence.** `Gap.gap_erases_history`. Two webs differ only in whether the migrant's dependence holds at step 3. The level is 2 up to step 3 and 0 from step 4; the migrant needs 1, met at steps 0–2; the drawer draws from step 3. With the one-step gap, the drawer undermines at no step, though the whole-run reading counts it consuming. With the dependence held through step 3, it undermines at every step from 3.

**Why it matters.** Dormancy, migration and seasonal use (prior knowledge, no literature read) can each be represented with or without such a gap. The stepwise verdict flips on one step of representation. Treating a lapse as the end of the dependence may be the intended reading; it is a choice with consequences, and it is not disclosed.

**Correction.** Disclose in the stepwise record's `hypotheses` and in the §7.1 cost: "a dependence that lapses for one step and re-forms starts a new tenure; whether dormancy or absence is represented as continuing dependence is an application duty". Add `Gap` as a witness. If continuity through bounded absence is wanted, define the tenure with `ReturnsWithin p` or an explicit dormancy relation.

### G3. overclaim: the stepwise cost is stated without its hypothesis

**Location.**

- `Becoming.lean` root doc, lines 43–44 ("only the whole-run reading ranks the absence of an overdrawing formation above its occurrence").
- `Becoming.Ranking` module doc, closing paragraph, lines 36–38 ("no longer ranks the absence of an overdrawing formation above its occurrence").
- Study §9 interpretation ("在场的继续里它在损失之前的事件被记入，所以不在场不是扩展") and the English P8 summary ("Under the stepwise reading, the formation's events before the loss are credited, neither course extends the other").
- Chapter §6.5, bullet 3 and the English paragraph ("because the formation's events before the loss are credited").
- Record ranking-under-readings `title` ("loses 'better without the overdrawing formation'").
- Record becoming-stepwise-reading, `related` entry for ranking-under-readings ("no longer ranks the absence … above its occurrence").

**What the Lean says.** `stepwise_unranked` takes `credited : stepwise (course L) .occurs (.focal, t)`. `credited_before_loss` supplies it when some active step of the focal formation leaves every need met. The hypothesis is disclosed in the theorem, in the record's `hypotheses`, in the §9 table ("只要焦点形成有一个被记入的事件") and in the module's result bullet.

**Evidence.** `Immediate.stepwise_ranks_absence`. The law `⟨start 1, renew 1, needG 1, needF 0, draw 3, contrib 0⟩` meets every premise of `whole_run_extends` and `stepwise_unranked` except `credited` (`Immediate.in_family`). Its first step already takes the condition below support. No focal event is credited; under the stepwise reading too, the course without the formation extends the course with it, and every comparison satisfying C ranks the absence higher.

**Why it matters.** The two readings differ on the absence comparison only for formations that begin within support. A formation that overdraws from its first step, such as an arrival into a condition already at its margin, is ranked below its absence under both readings. Stated without the hypothesis, the cost overstates the difference between the readings, and it is the cost on which §8.5's split and §9's choices rest.

**Correction.** At each location add "when the formation has an event whose step leaves every need met". Add `Immediate` to the ranking record, as a scope note that the stepwise reading also ranks the absence higher when no focal event is credited.

### G4. overclaim: "what the stepwise reading loses is only the comparison with absence"

**Location.**

- `Becoming.Ranking` module doc, lines 37–38 ("what it loses is the comparison with non-existence"), and the `malignant_restraint` docstring, lines 373–374.
- `Becoming.lean` root doc ("Both the whole-run and the stepwise reading rank … restraint above overdraw").
- Study §9 interpretation, second paragraph ("逐步读法下 C 失去的只是与不在场的比较，不是与节制的比较"); §8.5 last paragraph ("§9 已证明这一点"); §11.3 item 5 ("代价限于与不在场的比较"); §11.4 rebuttal 3 ("这把 §9 的代价精确地限于与不在场的比较"); English P7b bullet "Restraint".
- Chapter §6.5, bullet 4 and the English paragraph.
- Record ranking-under-readings: `title`, the last sentence of `claim`, and `limitations` ("one pair of compared continuations").

**What the Lean says.** `restraint_ranks` assumes the stopping law meets every need at every step. In the two-part family, `stops_credited` then credits every event of `Part × Nat` under both readings: the stopping course is maximal, so it extends any course of the family that withholds at least one event. `malignant_restraint` is a fair instance: the first step is the same, credited in both courses, and the stopping law meets every need. "Only" is a universal claim over comparisons; the proof covers comparisons with a maximal course in a two-part family.

**Evidence.** `ThirdParty.restraint_unranked_stepwise`. A third formation shares the condition and is supported only at level 7. Both courses start 6 → 5. Under restraint the focal formation stops drawing for two steps, the level reaches 7 once, and the third formation takes 7 → 6; under overdraw the level falls to 0. In the static web, `draws` is constant in time and carries no amount. So the restrained focal formation's event at step 3 undermines the third formation's once-met dependence, while under overdraw the third formation is never met and the same event is credited (`focal_three`). Under the stepwise reading neither course extends the other, and extension itself is a comparison satisfying C that does not rank restraint higher. Under the whole-run reading restraint extends overdraw.

The loss comes through the already disclosed cost (b): undermining reads co-participation in a shortfall, not what a draw does. The probe adds that this cost reaches the restraint comparison once another formation shares the condition.

**Why it matters.** The restraint result is offered as confining the cost of the stepwise reading. It confines it in the two-part family. With a co-participant, the comparison restraint is meant to secure can be lost too. The previous review's expectation (BECOMING-P7-REVIEW §3, last paragraph, and §5 item 5: "would show that only the comparison with non-existence is lost") was itself too strong, and P7b adopted it. This finding corrects both.

**Correction.**

- Replace "only the comparison with absence" by: "the comparison with absence is lost; the comparison with a course that meets every need at every step is kept, in the two-part family".
- Ranking record: `limitations` should say three pairs of continuations (occurs/absent, sharing/winning, stops/overdraws) in the two-part family; add `ThirdParty` to `counterexamples`.
- §11.3 item 5: "部分：在二元定律族中".

### G5. overclaim: the substituting consumer is withheld "at one step only"

**Location.** `Becoming.Substitution` module doc, lines 25–28 ("credited at every step except the one at which the shared condition falls below support … after it, it draws on nothing"); `Becoming.lean` root doc, line 37 ("at every step but one"); chapter §2 (line 188, "逐步读法除一步外都记入它"), §4 (line 247, "它只在一步上不被记入") and the §9 table; English P7b bullet; record substitution-preserves-consumption `correspondence` ("such a winner is withheld at one step only"); record becoming-stepwise-reading `related` ("at every step but one"). Study §8.4 states the step for the witness only ("只在第 2 步") and is correct.

**What the Lean says.** `stepwise_credits_substitution` is proved for the law `extracting`, in which the shared condition falls below both formations' needs at the same step.

**Evidence.** `SlowSubstitution.withheld_two_steps`. The law `⟨start 5, renew 1, needG 3, needF 1, draw 2, contrib 0⟩` meets every premise of `persists_consuming`. The shared condition falls below the sustaining need at step 2 (3 → 2) but stays above the focal need, so the focal formation keeps drawing on it at step 3 (2 → 0). It undermines at steps 2 and 3. By argument, not formalized here, the withheld stretch grows with `needG − needF` relative to `draw − renew`.

**Why it matters.** "One step" suggests that substitution nearly erases the stepwise trace of consumption. In general the consumer is withheld at every step at which it keeps drawing after the sustaining formation's support fails, until its own support fails and it switches.

**Correction.** "Credited before the sustaining formation loses support; withheld from that step until it switches (one step in `extracting`)". Apply it at every location above.

### G6. overclaim (definition): the move-relative but-for test needs two unstated conditions

**Location.** `Becoming.Joint`: `MakesDifference`, `Overdetermined` and the module doc; record joint-difference-making `hypotheses` ("检验固定实际所取的动作") and `limitations` ("an application with exogenous shocks must write them into the process"); study §11.1 F6 row; chapter glossary 差别制造.

**What the Lean says.** `MakesDifference P withhold f s a g c := BreaksBy P s a g c ∧ ∀ t, P.step (withhold f s) a t → Keeps (withhold f s) t g c`. The second conjunct is universal over successors, with no clause that a successor exists. `Overdetermined` asks that some step by the move break the dependence from each withheld configuration.

**Evidence.**

- `Hidden.hidden_shock_overdetermines`. One move whose step relation can either renew and take, or empty the condition: the shock is written into the process, as the record instructs. The lone drawer's loss is then `Overdetermined` and its part makes no difference, though from the withheld configuration the calm outcome of the same move keeps the dependence. F6's original pathology returns.
- `Tagged.every_part_decisive`. The same dynamics as `Pool.process`, but each move names the configuration it is taken from. From a withheld configuration the move has no step, so each of the three drawers' parts "makes the difference" vacuously, and the loss is not overdetermined. Under `Pool.process`, from the same configuration, it is overdetermined.

**Why it matters.** The test is exact when the step is a function of configuration and move, and the move is enabled at every withheld configuration. `Pool` and `Shock` satisfy both, so `difference_belongs_to_the_joint`, `move_decides` and `Overdetermined.no_difference` stand as stated. The general definitions and the record's modelling instruction do not secure them.

**Correction.**

- Add `∃ t, P.step (withhold f s) a t` to `MakesDifference`. Either state functionality as a hypothesis, or for nondeterministic steps make the outcome part of the move.
- Change the record's instruction to "write exogenous shocks into the move, not into the step relation". Add both probes as counterexamples to the unhypothesized reading.
- Glossary 差别制造: "扣除一方的部分后，以同一动作的每一步都维持依存（且该动作可取）".

### G7. overclaim: interaction ignores time and effect, but is glossed as one's drawing bearing on another's support

**Location.** `Becoming.Correspondence`, the module doc (line 14) and the `Interacts` docstring (line 74: "the first's drawing bears on the second's support"); study §10 interpretation ("一方的汲取落在另一方的支持上") and rebuttal 1 ("在这一表示中，没有形成汲取的条件，其水平不受任何形成的活动影响"); English P9 summary; record condition-correspondence-discipline `correspondence` ("not one formation's activity bearing on another's support").

**What the Lean says.** `Interacts c e e' := (draws e.2 e.1 c ∧ Bearing e'.2 e'.1 c) ∨ (Bearing e.2 e.1 c ∧ draws e'.2 e'.1 c)`. Neither the order of the two steps nor any change of level enters. In `Web` the level is a free function; `draws` does not fix how the level moves, and a condition nothing draws on can change level.

**Evidence.**

- `Later.later_drawing_connects`. A drawing at step 5 interacts with, and connects, a dependence that held only at step 0, which it cannot bear on.
- `pinned_interacts`. In `Pinned`, the drawer's event interacts with the old dependent, though the levels are identical whether the drawer takes or rests.

Time-blindness is disclosed (record `hypotheses`, §10 rebuttal 4 and boundary); amount-blindness is disclosed (record `hypotheses`). Effect-blindness is not, and the gloss contradicts both.

**Why it matters.** What makes the discipline more than a stipulation is its warrant: a relation is one formation's activity bearing on another's support. The definition captures a structural co-incidence: a drawer and a positive-need dependent of the same condition, at any steps. That remains a reasonable narrowing. It is not the bearing relation the gloss names.

**Correction.** Gloss it as "one draws on a condition on which the other depends at a positive level, at any steps". State that the bearing reading needs an ordered, effect-sensitive version (drawing at or before the dependence's step, with a level that differs with the draw), and list it as open. Present rebuttal 1's sentence about levels as a correspondence intention, not a property of the representation.

### G8. missing counterexample: the residual free connection needs only one drawing event

**Location.** `universal_connects` docstring; record condition-correspondence-discipline `counterexamples` and `correspondence` ("a renewed condition that every formation draws on and depends on"); study §10 interpretation, last bullet; chapter §6.3 ("人人汲取并依存的被更新条件").

**Evidence.** `OneUse.one_use_connects`. For every web with one living event `d`, adjoin a condition held at level 1, on which every formation depends at level 1, and which only `d`'s formation draws on, at `d`'s step. The condition is renewed, `living` is unchanged, and the web is connected under interaction.

**Why it matters.** The factual claim an application must check is smaller than recorded: universal positive-level dependence and one living drawing event. Universal dependence is cheap to assert. The residual is "a condition everyone depends on at a positive level, used once", not "a condition everyone draws on and depends on".

**Correction.** Restate the residual in the record, §10 and chapter §6.3, and add `OneUse` as a witness. One way to raise its price, open: require the condition's level to vary with drawing (G7).

### G9. overclaim (minor): "Q5 不再成立"

**Location.** Study §10 Result block, `Integration` ("审查 Q4 在纪律下排除，Q5 不再成立，Q10 未解决").

**What the first review said.** Q5 had two halves: co-dependence alone is `related` (`co_requirement_relates`), and valuing any drawer transmits to every living dependent of the condition without consumption (`drawing_reaches`).

**Evidence.** `drawing_reaches_under_interaction`. Under N_rel with interaction as `related`, valuing any drawing event reaches every living event that depends on the condition at a positive level, at any step, whether or not the drawing undermines anything. The discipline removes the first half only. `valuing_undermining_reaches` likewise does not use the undermining.

**Why it matters.** "living 与 related 读同一种关系" (§10) and `valuing_undermining_reaches` may suggest that undermining carries the transmission. Drawing does.

**Correction.** "Q5's co-dependence half is excluded; its transmission half remains: any drawing transmits." The English summary is already scoped correctly.

### G10. presentation (AGENTS.md, nondual method): co-dependence called a "correlation of situation"

**Location.** Study §10 rebuttal 1 ("共同依存是处境的相关，不是一方的活动落在另一方的支持上"); record condition-correspondence-discipline `correspondence` ("a correlation of situation").

**Assessment.** The discipline does not introduce a separate-entity primitive. `Interacts` is symmetric and built from the relations of events to a condition. The index types of formations and conditions were already disclosed in `Web`, and `living` is unchanged. The framing is the issue. Calling co-dependence a mere correlation treats the two dependents as units whose only relation is one's causal impact on the other. Under the monist relational method, depending on one condition is already a formed relation. The dependents share one condition and, in `Shared`'s falling run, one loss. That is the common problem the AGENTS.md reminder asks to see before opposed interests. The discipline omits this relation by choice. It does not show that it is not a relation.

**Correction.** Name co-dependence as a relation the discipline omits ("co-constitution through a common condition"). Say that `Shared` exhibits the cost of omitting it, and drop "correlation". In rebuttal 1, the two plants under one sun are already related through the same light, even without shading; shading is an added relation, not the first one.

### G11. presentation (provenance): the comparative form "better without it" attributed to a verdict Ren adopted

**Location.**

- Study §9 interpretation: "要得到 Ren 所采纳的关于恶性增殖的判决的这一形式（“没有它更好”）".
- Record joint-difference-making, `related` entry for relational-reading-comparison: "the verdicts Ren adopted, recorded in that result".
- Lesser: study §8.2 ("Ren 采纳的判决"), chapter §6.3 ("Ren 所采纳的判决"), the English P7b bullet ("Ren's verdict on winning by consumption"), and record becoming-finite-horizon (`correspondence`, `related`: "the verdict Ren adopted"). These keep the coverage question open. They are compatible with "the problem Ren adopted", but use a different word from the P7b label.

**Evidence.** In the source, Ren quoted the AI review's statement of the problem and asked to separate the two kinds of formation by relational structure, "应该不需要任何axiom". Ren then asked "generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧". The source's "AI 修正说明" assigns "消耗更坏" to comparison C on the AI's formal route and calls C's defence a philosophical argument. relational-reading-comparison records C's rankings. "Better without it" is the AI's comparative form of the problem Ren adopted; it is not Ren's words.

**Choices for Ren.** None found. The reading is called "working candidate, pending Ren's choice" in study §7.1 and §9, the `Ranking` module doc, chapter §6.3 and §6.5, and the records. The split of §8.5 remains labelled "作者的候选分工（AI 论证，未经 Ren 确认）". No AI text is quoted as Ren's.

**Correction.** §9: "要得到关于恶性增殖的判决的比较形式（“没有它更好”，C 的 AI 形式路线）". joint-difference-making: "the C rankings recorded in that result, which formalize the problem Ren adopted". Elsewhere use "the problem Ren adopted" as P7b's own label does.

### G12. presentation: bookkeeping

- Study §9 Result block: "Becoming.Ranking 15 项定理". The module now has 19 (§11 and the receipt). Write "P8 时 15 项；P7b 后 19 项".
- Record ranking-under-readings: `limitations` says "one pair of compared continuations" (three now; G4). `counterexamples` lists only `malignant_ranking`; add `Immediate` (G3) and `ThirdParty` (G4) or their equivalents.
- Chapter glossary: 差别制造 lacks "same move" (G6). There are no entries for 交互 / interaction (`Interacts`), 承担 / bearing (`Bearing`) or 惰性 / idle (`Idle`).
- Study §8.5, last paragraph: "§9 已证明这一点" should become "§9 在二元定律族中、对每步都满足所需的节制证明了这一点" (G4).
- Record becoming-stepwise-reading: the P7b `history` sentence inherits G1.

## 3. What remains sound

- Every P8, P9 and P7b theorem: statement, proof and empty axiom report, recompiled from the prelude in the 15-module core closure; the two bridge theorems through the periphery.
- `MetSince`'s tenure clause, which excludes the `NewNeed` pathology, and every existing witness, all of which have constant needs.
- `BreaksBy` and the move-relative test for functional processes with enabled moves; `Pool.difference_belongs_to_the_joint` re-proved; `Shock.move_decides`; the separation of run-level and step-level tests.
- `withheld_of_extends`: general, one-directional as stated, and hypothesized exactly as needed. `whole_run_extends`, `whole_run_ranks`, `stepwise_contest` (sharing survives under the stepwise reading), and `restraint_ranks` and `malignant_restraint` within their family.
- The bridge correspondence: `wholeRun_iff` is `Iff.rfl`; `undisturbed_eq` equates levels; `Ranking.absent` is textually the same as `RenewalComparison.absent`.
- The correspondence discipline: `Idle.not_interacts`, `Idle.not_undermining`, `adjoin_living`, `inert_connects` (Q4 excluded), `UnderminingOn.interacts`, `connected_of_commons`, `significant_iff_of_commons`. The cost in `Shared` is proved and disclosed.
- The labelling: "working candidate, pending Ren's choice"; the split labelled as an AI argument; "no responsibility or duty" boundaries.
- P7b's practice of moving probes into the core as theorems and keeping old behaviour as named witnesses.

## 4. What would change these verdicts

1. `MetSince` redefined with `need s ≤ level s ∧ need t ≤ need s`, or the prose narrowed to constant need, with `FallingNeed` and `RisingNeed` as theorems. G1 and F1 would close.
2. A rule for lapsing dependence: a tenure through bounded absence, or a stated representation duty. G2 would close.
3. A restraint theorem beyond the two-part family, with co-drawers, or with amounts so that a restrained formation that takes nothing does not undermine. Either would show how far G4's counterexample reaches.
4. An ordered, effect-sensitive interaction, with `connected_of_commons` re-proved. G7 would close, and G8's residual would cost more.
5. Enabledness, and functionality or outcome-as-move, in `MakesDifference`, with `Pool` and `Shock` re-proved. G6 and F6 would close.
6. Ren's choice of reading, and Ren's words on events before the threshold and on whether "better without it" is Ren's verdict. These would settle how much G3 and G4 matter and would close G11.

## Appendix: probe sources

Compiled with Lean 4.29.1 against the unchanged `b9954b90` core bytes (with `import Std` removed from `GenerativeCore`, as the checker does). `Audit.lean` prints the axioms of 82 declarations, and `AuditBridge.lean` of two; every one reports "does not depend on any axioms".

### `P8P9Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P8, P9 and P7b

Each probe is a minimal model satisfying the published definitions at `b9954b90`
unchanged. It shows what the definitions admit, not what actual systems usually do.
-/

namespace P8Probe

open Becoming RelationalRenewal

/-! ## M1. A dependence never met while it held: the need falls -/

namespace FallingNeed

inductive F where
  | late
  | drawer

/-- The level is 2 at step 0 and 0 afterwards. `late` depends on the condition at every
step, needing 3 before step 5 and 1 from step 5; it is never active. `drawer` draws from
step 5. -/
def web : Web F Unit where
  level t _ := match t with
    | 0 => 2
    | _ + 1 => 0
  active t f := match f with
    | .late => False
    | .drawer => 5 ≤ t
  requires _ f _ := match f with
    | .late => True
    | .drawer => False
  need t f _ := match f with
    | .late => if t < 5 then 3 else 1
    | .drawer => 0
  draws t f _ := match f with
    | .late => False
    | .drawer => 5 ≤ t

theorem need_pos (p : Prop) [Decidable p] : 0 < (if p then 3 else 1) :=
  if h : p then by rw [if_pos h]; exact Nat.zero_lt_succ 2
  else by rw [if_neg h]; exact Nat.zero_lt_one

theorem need_late {t : Nat} (late : 5 ≤ t) : web.need t .late () = 1 :=
  if_neg (Nat.not_lt_of_le late)

/-- `late`'s dependence is unmet at every step at which it holds, and never broken. Yet
`MetSince` holds from step 5 (the present need, 1, is at most the level 2 at step 0, when
the need was 3), and every event of `drawer` from step 5 undermines through it. -/
theorem falling_need_undermines :
    web.Dependent ∧
    (∀ t, web.requires t .late () → web.level t () < web.need t .late ()) ∧
    (∀ t, ¬ web.Broken t .late ()) ∧
    (∀ t, 5 ≤ t → web.MetSince t .late () ∧ web.UnderminingAt t .drawer) := by
  have unmet : ∀ t, web.requires t .late () → web.level t () < web.need t .late ()
    | 0, _ => Nat.lt_succ_self 2
    | _ + 1, _ => need_pos _
  refine ⟨?_, unmet, fun t ⟨depends, met, _⟩ => Nat.not_le_of_gt (unmet t depends) met,
    fun t late => ?_⟩
  · intro _ f active _ depends
    cases f with
    | late => exact False.elim active
    | drawer => exact False.elim depends
  · have since : web.MetSince t .late () :=
      ⟨0, Nat.zero_le t, fun _ _ _ => trivial,
        Nat.le_trans (Nat.le_of_eq (need_late late)) (Nat.le_succ 1)⟩
    refine ⟨since, (), late, .late, trivial, since, ?_⟩
    show web.level (t + 1) () < web.need t .late ()
    rw [need_late late]
    exact Nat.zero_lt_one

end FallingNeed

/-! ## M2. A need that rises past the present level counts as once met -/

namespace RisingNeed

inductive F where
  | grower
  | drawer

/-- The level is 3 at step 0 and 1 afterwards; nothing draws before step 5. `grower`
depends throughout, needing 1 before step 5 and 2 from step 5. -/
def web : Web F Unit where
  level t _ := match t with
    | 0 => 3
    | _ + 1 => 1
  active t f := match f with
    | .grower => t < 5
    | .drawer => 5 ≤ t
  requires _ f _ := match f with
    | .grower => True
    | .drawer => False
  need t f _ := match f with
    | .grower => if t < 5 then 1 else 2
    | .drawer => 0
  draws t f _ := match f with
    | .grower => False
    | .drawer => 5 ≤ t

theorem need_grown {t : Nat} (late : 5 ≤ t) : web.need t .grower () = 2 :=
  if_neg (Nat.not_lt_of_le late)

theorem level_late {t : Nat} (late : 5 ≤ t) : web.level t () = 1 :=
  match t, late with
  | _ + 1, _ => rfl

/-- The grown need 2 was never met at any step at which it was the need, and the decline
at step 0 happened when the need was 1 and was met. `MetSince` compares the present need
with the level at step 0, so every event of `drawer` from step 5 undermines. -/
theorem rising_need_undermines :
    (∀ t, t < 5 → web.need t .grower () ≤ web.level t ()) ∧
    (∀ t, 5 ≤ t → web.level t () < web.need t .grower ()) ∧
    (∀ t, 5 ≤ t → web.MetSince t .grower () ∧ web.UnderminingAt t .drawer) := by
  refine ⟨fun t early => ?_, fun t late => ?_, fun t late => ?_⟩
  · show (if t < 5 then 1 else 2) ≤ web.level t ()
    rw [if_pos early]
    match t with
    | 0 => exact Nat.le_succ_of_le (Nat.le_succ 1)
    | _ + 1 => exact Nat.le_refl 1
  · rw [need_grown late, level_late late]
    exact Nat.lt_succ_self 1
  · have since : web.MetSince t .grower () :=
      ⟨0, Nat.zero_le t, fun _ _ _ => trivial,
        Nat.le_trans (Nat.le_of_eq (need_grown late)) (Nat.le_succ 2)⟩
    refine ⟨since, (), late, .grower, trivial, since, ?_⟩
    show web.level (t + 1) () < web.need t .grower ()
    rw [need_grown late]
    exact Nat.lt_succ_self 1

end RisingNeed

/-! ## M3. A one-step gap in a dependence erases its history -/

namespace Gap

inductive F where
  | migrant
  | drawer

def levels (t : Nat) : Nat := if t < 4 then 2 else 0

/-- The migrant depends on the condition at need 1, met at steps 0 to 2. In `gapWeb` the
dependence does not hold at step 3 (the migrant is away) and holds again from step 4; in
`heldWeb` it holds throughout. The level is 2 up to step 3 and 0 from step 4; the drawer
draws from step 3. The two webs differ only in `requires` at step 3. -/
def gapWeb : Web F Unit where
  level t _ := levels t
  active t f := match f with
    | .migrant => t < 3
    | .drawer => 3 ≤ t
  requires t f _ := match f with
    | .migrant => t ≠ 3
    | .drawer => False
  need _ f _ := match f with
    | .migrant => 1
    | .drawer => 0
  draws t f _ := match f with
    | .migrant => False
    | .drawer => 3 ≤ t

def heldWeb : Web F Unit :=
  { gapWeb with requires := fun _ f _ => match f with
    | .migrant => True
    | .drawer => False }

theorem levels_high {t : Nat} (early : t < 4) : levels t = 2 := if_pos early

theorem levels_low {t : Nat} (late : 4 ≤ t) : levels t = 0 := if_neg (Nat.not_lt_of_le late)

/-- With the one-step gap the drawer undermines at no step, though the whole-run reading
counts it consuming; with the dependence held through step 3 it undermines at every step
from 3. -/
theorem gap_erases_history :
    (∀ t, ¬ gapWeb.UnderminingAt t .drawer) ∧ gapWeb.ConsumingIn .drawer ∧
    (∀ t, 3 ≤ t → heldWeb.UnderminingAt t .drawer) := by
  refine ⟨fun t ⟨_, drawn, g, depends, ⟨s, before, held, met⟩, _⟩ => ?_, ?_, fun t late => ?_⟩
  · cases g with
    | drawer => exact depends
    | migrant =>
      match Nat.lt_or_ge s 4 with
      | .inl early =>
        exact held 3 (Nat.le_of_lt_succ early) drawn rfl
      | .inr late =>
        have low : levels s = 0 := levels_low late
        exact Nat.not_succ_le_zero 0 (Nat.le_trans met (Nat.le_of_eq low))
  · refine ⟨3, (), Nat.le_refl 3, .migrant, 4, (show (4 : Nat) ≠ 3 by decide), fun t later => ?_⟩
    show levels t < 1
    rw [levels_low (Nat.le_of_lt later)]
    exact Nat.zero_lt_one
  · refine ⟨(), late, .migrant, trivial,
      ⟨0, Nat.zero_le t, fun _ _ _ => trivial,
        Nat.le_trans (Nat.le_succ 1) (Nat.le_of_eq (levels_high (Nat.zero_lt_succ 3)).symm)⟩, ?_⟩
    show levels (t + 1) < 1
    rw [levels_low (Nat.succ_le_succ late)]
    exact Nat.zero_lt_one

end Gap

/-! ## R1. With no credited event, the stepwise reading ranks absence above occurrence -/

namespace Immediate

open Ranking

/-- Start at the sustaining need; the focal formation, needing nothing, draws three where
one is renewed. The first step already crosses support. -/
def law : Law := ⟨1, 1, 1, 0, fun _ => 3, fun _ => 0⟩

theorem law_low : ∀ n, Law.level law (n + 1) = 0
  | 0 => rfl
  | n + 1 => by
    rw [Law.level_succ, law_low n]
    rfl

/-- The law is in the family of `whole_run_extends` and `stepwise_unranked`. -/
theorem in_family :
    0 < law.needG ∧ law.needF ≤ law.needG ∧ law.needG ≤ law.start ∧
      ∀ t, 0 ≤ t → law.renew + law.contrib t < law.draw t :=
  ⟨Nat.zero_lt_one, Nat.zero_le 1, Nat.le_refl 1, fun _ _ => Nat.lt_succ_of_le (Nat.le_succ 1)⟩

theorem focal_withheld (t : Nat) : ¬ stepwise (course law) .occurs (.focal, t) :=
  fun ⟨_, notUndermining⟩ => notUndermining
    ⟨(), ⟨0, Nat.zero_lt_succ 2⟩, .sustaining, trivial,
      ⟨0, Nat.zero_le t, fun _ _ _ => trivial, Nat.le_refl 1⟩,
      (by show Law.level law (t + 1) < 1; rw [law_low t]; exact Nat.zero_lt_one)⟩

theorem absent_credits_sustaining (t : Nat) : stepwise (course law) .absent (.sustaining, t) :=
  ⟨absent_sustains law (Nat.le_refl 1) t, fun ⟨_, drawn, _⟩ => drawn⟩

/-- Under the stepwise reading the course without the focal formation extends the course
with it, so every comparison satisfying C ranks the absence higher. The hypothesis
`credited` of `stepwise_unranked` is needed, not idle. -/
theorem stepwise_ranks_absence :
    (∀ t, ¬ stepwise (course law) .occurs (.focal, t)) ∧
    ExtendsUnder (stepwise (course law)) .occurs .absent ∧
    ∀ Better, ComparisonUnder (stepwise (course law)) Better → Better .occurs .absent := by
  have ext : ExtendsUnder (stepwise (course law)) .occurs .absent :=
    ⟨fun e credited => match e, credited with
      | (.focal, t), credited => absurd credited (focal_withheld t)
      | (.sustaining, t), _ => absent_credits_sustaining t,
     (.sustaining, 1), trivial, absent_credits_sustaining 1, fun ⟨active, _⟩ =>
       Nat.not_succ_le_zero 0 (Nat.le_trans active (Nat.le_of_eq (law_low 0)))⟩
  exact ⟨focal_withheld, ext, fun _ ranks => ranks _ _ ext⟩

end Immediate

/-! ## R2. Outside the two-part family, restraint need not extend overdraw stepwise -/

namespace ThirdParty

open Ranking

inductive Part where
  | focal
  | sustaining
  | third

inductive Course where
  | stops
  | overdraws

/-- Restraint: the focal formation's first step is the same overdraw (6 to 5); then it
takes nothing for two steps (5, 6, 7); at step 3 a third formation, supported only at 7,
takes two (7 to 6); afterwards the focal formation takes the renewal (6). -/
def stopsLevel : Nat → Nat
  | 0 => 6
  | 1 => 5
  | 2 => 6
  | 3 => 7
  | _ + 4 => 6

/-- Overdraw: the focal formation takes two where one is renewed, down to 0. -/
def overLevel : Nat → Nat
  | 0 => 6
  | 1 => 5
  | 2 => 4
  | 3 => 3
  | 4 => 2
  | 5 => 1
  | _ + 6 => 0

def unfolding (level : Nat → Nat) : Unfolding Part Unit where
  level t _ := level t
  active t p := match p with
    | .focal => True
    | .sustaining => 1 ≤ level t
    | .third => 7 ≤ level t
  requires p _ := match p with
    | .focal => False
    | .sustaining => True
    | .third => True
  need p _ := match p with
    | .focal => 0
    | .sustaining => 1
    | .third => 7
  draws p _ := match p with
    | .focal => True
    | .sustaining => False
    | .third => True

def courses : Course → Unfolding Part Unit
  | .stops => unfolding stopsLevel
  | .overdraws => unfolding overLevel

theorem stops_dependent : Dependent (courses .stops) := fun t p active _ depends =>
  match p, active, depends with
  | .sustaining, active, _ => active
  | .third, active, _ => active

theorem over_dependent : Dependent (courses .overdraws) := fun t p active _ depends =>
  match p, active, depends with
  | .sustaining, active, _ => active
  | .third, active, _ => active

theorem over_below_seven : ∀ t, overLevel t < 7
  | 0 => by decide
  | 1 => by decide
  | 2 => by decide
  | 3 => by decide
  | 4 => by decide
  | 5 => by decide
  | _ + 6 => (Nat.zero_lt_succ 6 : 0 < 7)

theorem stops_supports : ∀ t, 1 ≤ stopsLevel t
  | 0 => by decide
  | 1 => by decide
  | 2 => by decide
  | 3 => by decide
  | _ + 4 => (Nat.le_succ_of_le (Nat.le_succ_of_le (Nat.le_succ_of_le
      (Nat.le_succ_of_le (Nat.le_succ_of_le (Nat.le_refl 1))))) : 1 ≤ 6)

/-- The focal formation's event at step 3 is credited stepwise when it overdraws (its
step leaves the sustaining need met and the third formation was never met), and withheld
when it has stopped (the third formation, met at step 3, is unmet after it). -/
theorem focal_three :
    stepwise courses .overdraws (.focal, 3) ∧ ¬ stepwise courses .stops (.focal, 3) := by
  refine ⟨⟨trivial, fun ⟨_, _, g, depends, ⟨s, _, _, met⟩, fell⟩ => ?_⟩,
    fun ⟨_, notUndermining⟩ => notUndermining
      ⟨(), trivial, .third, trivial, ⟨3, Nat.le_refl 3, fun _ _ _ => trivial, Nat.le_refl 7⟩,
        Nat.lt_succ_self 6⟩⟩
  cases g with
  | focal => exact depends
  | sustaining => exact absurd fell (Nat.not_lt_of_le (Nat.le_succ 1))
  | third => exact Nat.not_le_of_gt (over_below_seven s) met

/-- Under the stepwise reading neither course extends the other, so extension itself is
a comparison satisfying C that does not rank restraint above overdraw. Under the whole-run
reading restraint extends overdraw. -/
theorem restraint_unranked_stepwise :
    ¬ ExtendsUnder (stepwise courses) .overdraws .stops ∧
    ¬ ExtendsUnder (stepwise courses) .stops .overdraws ∧
    ComparisonUnder (stepwise courses) (ExtendsUnder (stepwise courses)) ∧
    ExtendsUnder (wholeRun courses) .overdraws .stops := by
  have stopsConsumed : Consumed (courses .stops) () :=
    ⟨.third, 4, trivial, fun t later => match t, later with
      | _ + 4, _ => Nat.lt_succ_self 6⟩
  have overConsumed : Consumed (courses .overdraws) () :=
    ⟨.sustaining, 6, trivial, fun t later => match t, later with
      | _ + 6, _ => Nat.zero_lt_one⟩
  have sustainingCredited : ∀ t, wholeRun courses .stops (.sustaining, t) :=
    fun t => ⟨stops_supports t, fun ⟨_, drawn, _⟩ => drawn⟩
  refine ⟨fun ⟨sub, _⟩ => focal_three.2 (sub _ focal_three.1),
    fun ⟨sub, _⟩ => ?_, fun _ _ ext => ext, ⟨fun e credited => ?_, (.sustaining, 6), trivial,
      sustainingCredited 6, fun ⟨active, _⟩ => Nat.not_succ_le_zero 0 active⟩⟩
  · exact Nat.not_succ_le_zero 0
      (sub (.sustaining, 6) ⟨stops_supports 6, fun ⟨_, drawn, _⟩ => drawn⟩).1
  · match e, credited with
    | (.focal, _), ⟨_, notConsuming⟩ => exact absurd ⟨(), trivial, overConsumed⟩ notConsuming
    | (.third, _), ⟨active, _⟩ => exact absurd active (Nat.not_le_of_gt (over_below_seven _))
    | (.sustaining, t), _ => exact sustainingCredited t

end ThirdParty

/-! ## R3. A substituting consumer withheld at more than one step -/

namespace SlowSubstitution

/-- Start 5, renewal 1, sustaining need 3, focal need 1, two units drawn a step. -/
def law : Law := ⟨5, 1, 3, 1, fun _ => 2, fun _ => 0⟩

/-- The law meets every premise of `Substitution.persists_consuming`, and the focal
formation, which can substitute, undermines at steps 2 and 3. Step 2 breaks the
sustaining formation's dependence (level 3 to 2, need 3); at step 3 the focal formation,
still supported (need 1), keeps drawing on the shared condition (2 to 0). -/
theorem withheld_two_steps :
    (Substitution.web law).ConsumingIn .focal ∧
    (Substitution.web law).UnderminingAt 2 .focal ∧
    (Substitution.web law).UnderminingAt 3 .focal :=
  ⟨(Substitution.persists_consuming law (Nat.zero_lt_succ 2) Nat.zero_lt_one
      (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.le_succ_of_le (Nat.le_succ_of_le
        (Nat.le_succ_of_le (Nat.le_succ 1)))) (fun _ => Nat.lt_succ_self 1)).2.2.2.1,
   ⟨.shared, ⟨by decide, Nat.zero_lt_two⟩, .sustaining, trivial,
     ⟨0, Nat.zero_le 2, fun _ _ _ => trivial, by decide⟩, by decide⟩,
   ⟨.shared, ⟨by decide, Nat.zero_lt_two⟩, .sustaining, trivial,
     ⟨0, Nat.zero_le 3, fun _ _ _ => trivial, by decide⟩, by decide⟩⟩

end SlowSubstitution

/-! ## J1. A shock inside the step relation: holding the move fixed is not enough -/

namespace Hidden

/-- One move; its step can renew and take the current amount, or empty the condition. -/
def process : Generative.Process Shock.State Unit :=
  ⟨fun s _ t => t = ⟨s.level + 1 - s.taking, s.taking⟩ ∨ t = ⟨0, s.taking⟩⟩

/-- With the shock written into the step relation rather than the move, the lone drawer's
loss is overdetermined and its part makes no difference, though from the withheld
configuration the calm outcome of the same move keeps the dependence. -/
theorem hidden_shock_overdetermines :
    Shock.dependence.Overdetermined process Shock.withhold Shock.start () .sustaining () ∧
    ¬ Shock.dependence.MakesDifference process Shock.withhold .drawer Shock.start ()
      .sustaining () ∧
    process.step (Shock.withhold .drawer Shock.start) () ⟨2, 0⟩ ∧
    Shock.dependence.Keeps (Shock.withhold .drawer Shock.start) ⟨2, 0⟩ .sustaining () :=
  have over : Shock.dependence.Overdetermined process Shock.withhold Shock.start ()
      .sustaining () :=
    ⟨⟨⟨0, 2⟩, .inl rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩, fun
      | .drawer => ⟨⟨0, 0⟩, .inr rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩
      | .sustaining => ⟨⟨0, 2⟩, .inr rfl, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩⟩
  ⟨over, over.no_difference .drawer, .inl rfl, ⟨Nat.le_refl 1, Nat.le_succ 1⟩⟩

end Hidden

/-! ## J2. A move the withheld configuration cannot take makes every part decisive -/

namespace Tagged

/-- The same dynamics as `Pool.process`, but each move names the configuration it is
taken from. -/
def process : Generative.Process Pool.State Pool.State :=
  ⟨fun s a t => a = s ∧ t = ⟨s.level + 1 - s.drawing.total, s.drawing⟩⟩

def start : Pool.State := ⟨1, Pool.all⟩

/-- Every drawer's part "makes the difference" vacuously, since the withheld
configuration admits no step by the move, and the loss is not overdetermined; under
`Pool.process`, from the same configuration, it is overdetermined. -/
theorem every_part_decisive :
    Pool.dependence.MakesDifference process Pool.withhold .first start start .sustaining () ∧
    Pool.dependence.MakesDifference process Pool.withhold .second start start .sustaining () ∧
    Pool.dependence.MakesDifference process Pool.withhold .third start start .sustaining () ∧
    ¬ Pool.dependence.Overdetermined process Pool.withhold start start .sustaining () ∧
    Pool.dependence.Overdetermined Pool.process Pool.withhold start Pool.all .sustaining () :=
  have breaks : Pool.dependence.BreaksBy process start start .sustaining () :=
    ⟨⟨0, Pool.all⟩, ⟨rfl, rfl⟩, trivial, Nat.le_refl 1, Nat.zero_lt_one⟩
  ⟨⟨breaks, fun _ ⟨same, _⟩ => absurd (congrArg (fun s => s.drawing.first) same) (by decide)⟩,
   ⟨breaks, fun _ ⟨same, _⟩ => absurd (congrArg (fun s => s.drawing.second) same) (by decide)⟩,
   ⟨breaks, fun _ ⟨same, _⟩ => absurd (congrArg (fun s => s.drawing.third) same) (by decide)⟩,
   fun ⟨_, all⟩ => match all .first with
     | ⟨_, ⟨same, _⟩, _⟩ => absurd (congrArg (fun s => s.drawing.first) same) (by decide),
   Pool.difference_belongs_to_the_joint.2.2.2.1⟩

end Tagged

/-! ## C1. Interaction does not order events: a later drawing connects an earlier dependent -/

namespace Later

inductive F where
  | early
  | late

/-- The level is 1 at step 0 and 0 afterwards. `early` depends on the condition at need 1
at step 0 only and is active then; `late` draws on it at step 5 only and is active then. -/
def web : Web F Unit where
  level t _ := match t with
    | 0 => 1
    | _ + 1 => 0
  active t f := match f with
    | .early => t = 0
    | .late => t = 5
  requires t f _ := match f with
    | .early => t = 0
    | .late => False
  need _ f _ := match f with
    | .early => 1
    | .late => 0
  draws t f _ := match f with
    | .early => False
    | .late => t = 5

/-- The drawing at step 5 "interacts" with the dependence at step 0, which it cannot bear
on, and connects the two events. -/
theorem later_drawing_connects (own sig : Unit → F × Nat → Prop) :
    web.Dependent ∧
    (web.interaction own sig).living (.early, 0) ∧ (web.interaction own sig).living (.late, 5) ∧
    web.Interacts () (.late, 5) (.early, 0) ∧ (web.interaction own sig).Connected := by
  have aliveEarly : (web.interaction own sig).living (.early, 0) :=
    ⟨rfl, fun ⟨_, drawn, _⟩ => drawn⟩
  have aliveLate : (web.interaction own sig).living (.late, 5) :=
    ⟨rfl, fun ⟨_, _, g, depends, _, _⟩ => match g, depends with
      | .early, depends => Nat.noConfusion depends
      | .late, depends => depends⟩
  have bearing : web.Bearing 0 .early () := ⟨rfl, Nat.zero_lt_one⟩
  refine ⟨?_, aliveEarly, aliveLate, .inl ⟨rfl, bearing⟩,
    Web.connected_of_commons web own sig () (fun e alive => ?_) aliveLate rfl aliveEarly bearing⟩
  · intro t f active _ depends
    cases f with
    | early => subst active; exact Nat.le_refl 1
    | late => exact False.elim depends
  · match e, alive with
    | (.early, t), ⟨active, _⟩ => exact .inr ⟨active, Nat.zero_lt_one⟩
    | (.late, t), ⟨active, _⟩ => exact .inl active

end Later

/-! ## C2. Interaction does not ask whether the drawing changes anything -/

theorem pinned_interacts :
    (Pinned.dependence.along Pinned.taking).Interacts () (.drawer, 1) (.old, 1) ∧
    ∀ t, (Pinned.dependence.along Pinned.taking).level t () =
      (Pinned.dependence.along Pinned.resting).level t () :=
  ⟨.inl ⟨Nat.zero_lt_one, trivial, Nat.zero_lt_one⟩, Pinned.undermining_without_effect.1⟩

/-! ## C3. One living drawing event and a dependence everyone holds connect any web -/

namespace OneUse

variable {F C Pos : Type}

/-- A condition held at level one, on which every formation depends at level one, drawn
on only by the formation of `d` at the step of `d`. -/
def single (d : F × Nat) : Web.Condition F :=
  ⟨fun _ => 1, fun _ _ => True, fun _ _ => 1, fun t f => f = d.1 ∧ t = d.2⟩

/-- For every web with a living event, adjoining that condition leaves `living`
unchanged, keeps the condition renewed and connects the web under interaction. A single
drawing event suffices; every formation need not draw. -/
theorem one_use_connects (W : Web F C) (own sig : Pos → F × Nat → Prop) (d : F × Nat)
    (alive : (W.interaction own sig).living d) :
    (W.adjoin (single d)).Renewed none ∧
    (∀ e, ((W.adjoin (single d)).interaction own sig).living e ↔
      (W.interaction own sig).living e) ∧
    ((W.adjoin (single d)).interaction own sig).Connected :=
  have living : ∀ e, ((W.adjoin (single d)).interaction own sig).living e ↔
      (W.interaction own sig).living e :=
    Web.adjoin_living fun _ _ ⟨_, _, _, _, fell⟩ => Nat.lt_irrefl 1 fell
  have aliveD := (living d).mpr alive
  have bearing : (W.adjoin (single d)).Bearing d.2 d.1 none := ⟨trivial, Nat.zero_lt_one⟩
  ⟨fun _ _ _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩, living,
   Web.connected_of_commons _ own sig none (fun _ _ => .inr ⟨trivial, Nat.zero_lt_one⟩)
     aliveD ⟨rfl, rfl⟩ aliveD bearing⟩

end OneUse

/-! ## C4. Q5's transmission half survives the discipline -/

/-- Under N_rel with interaction as `related`, valuing any drawing event reaches every
living event depending on the condition at a positive level, at any step, whether or
not the drawing undermines anything. -/
theorem drawing_reaches_under_interaction {F C Pos : Type} (W : Web F C)
    (own sig : Pos → F × Nat → Prop) (transmit : Neutral (W.interaction own sig).transmits)
    {f g : F} {t t' : Nat} {c : C} (drawn : W.draws t f c) (bearing : W.Bearing t' g c)
    (alive : (W.interaction own sig).living (g, t')) (p : Pos)
    (held : (W.interaction own sig).sig p (f, t)) : (W.interaction own sig).sig p (g, t') :=
  transmit (p, (f, t), (g, t')) held ⟨c, .inl ⟨drawn, bearing⟩⟩ alive

end P8Probe
```

### `Audit.lean`

```lean
import P8P9Probes
open Becoming P8Probe
-- probes
#print axioms FallingNeed.need_pos
#print axioms FallingNeed.need_late
#print axioms FallingNeed.falling_need_undermines
#print axioms RisingNeed.need_grown
#print axioms RisingNeed.level_late
#print axioms RisingNeed.rising_need_undermines
#print axioms Gap.levels_high
#print axioms Gap.levels_low
#print axioms Gap.gap_erases_history
#print axioms Immediate.law_low
#print axioms Immediate.in_family
#print axioms Immediate.focal_withheld
#print axioms Immediate.absent_credits_sustaining
#print axioms Immediate.stepwise_ranks_absence
#print axioms ThirdParty.stops_dependent
#print axioms ThirdParty.over_dependent
#print axioms ThirdParty.over_below_seven
#print axioms ThirdParty.stops_supports
#print axioms ThirdParty.focal_three
#print axioms ThirdParty.restraint_unranked_stepwise
#print axioms SlowSubstitution.withheld_two_steps
#print axioms Hidden.hidden_shock_overdetermines
#print axioms Tagged.every_part_decisive
#print axioms Later.later_drawing_connects
#print axioms pinned_interacts
#print axioms OneUse.one_use_connects
#print axioms drawing_reaches_under_interaction
-- core declarations relied on
#print axioms Web.MetSince.now
#print axioms Web.BreakingOn.undermining
#print axioms NewNeed.never_met_not_undermining
#print axioms Pinned.undermining_without_effect
#print axioms Commons.drawing_after_loss
#print axioms Web.undermining_for_one
#print axioms Web.undermining_for_zero
#print axioms LateMet.within_one_not_renewing
#print axioms Commons.escalation_undermines_for_every_cycle
#print axioms Commons.whole_run_credits_overdraw
#print axioms Commons.amount_reading
#print axioms Commons.cycle_reading_not_finite
#print axioms Feedback.prefix_does_not_decide
#print axioms Becoming.le_of_add_le_add_right
#print axioms Becoming.add_right_cancel
#print axioms Dependence.Overdetermined.no_difference
#print axioms Shock.move_decides
#print axioms Pool.difference_belongs_to_the_joint
#print axioms Pool.within_share_undermines
#print axioms Commons.depletion_is_joint
#print axioms Commons.no_finite_segment_makes_difference
#print axioms Commons.breaking_event_makes_step_difference
#print axioms Substitution.persists_consuming
#print axioms Substitution.extracting_low
#print axioms Substitution.stepwise_credits_substitution
#print axioms Ranking.stepwise_iff
#print axioms Ranking.withheld_of_extends
#print axioms Ranking.whole_run_extends
#print axioms Ranking.whole_run_ranks
#print axioms Ranking.credited_before_loss
#print axioms Ranking.stepwise_unranked
#print axioms Ranking.admits_occurrence
#print axioms Ranking.readings_rank_differently
#print axioms Ranking.malignant_ranking
#print axioms Ranking.winning_ranking
#print axioms Ranking.sharing_credited
#print axioms Ranking.stepwise_contest
#print axioms Ranking.stops_credited
#print axioms Ranking.restraint_ranks
#print axioms Ranking.stoppingMalignant_level
#print axioms Ranking.malignant_restraint
#print axioms Web.Interacts.symm
#print axioms Web.UnderminingOn.interacts
#print axioms Web.Idle.not_interacts
#print axioms Web.Idle.not_undermining
#print axioms Web.interaction_narrows
#print axioms Web.connected_of_commons
#print axioms Web.significant_iff_of_commons
#print axioms Web.valuing_undermining_reaches
#print axioms Web.adjoin_living
#print axioms Web.adjoin_connected_iff
#print axioms Web.inert_connects
#print axioms Web.universal_connects
#print axioms Shared.connection_by_living_use
#print axioms Shared.first_isolated
```

### `AuditBridge.lean`

```lean
import Becoming.Bridge
#print axioms Becoming.Ranking.wholeRun_iff
#print axioms Becoming.Ranking.undisturbed_eq
```
