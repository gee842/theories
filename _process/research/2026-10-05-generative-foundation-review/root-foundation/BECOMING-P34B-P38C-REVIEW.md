# P34b 至 P38c 的独立审查 / Independent review of P34b to P38c

2026-10-10。审查者：Claude Opus 5.5，独立 agent，未参与撰写 P34b、P35、P36、P36b、P38、P38b 与 P38c。对象：`main` 的 `c95f6576`，经六个提交 `9ad91910`、`4284d6ab`、`ba3b0e3b`、`82a9e3aa`、`0ed94604`、`c95f6576`；P37（`fc0f3c25`）与 P39（`8e857735`）不在对象之内，只核对第一部分总陈述是否如实转述 P37。这是第十四次独立审查。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of P34b, P35, P36, P36b, P38, P38b or P38c. Object: `main` at `c95f6576`, through six commits; P37 and P39 are outside the object, except that the Part I statement's account of P37 is checked. This is the fourteenth independent review.

**摘要（中文）。**

- **机械检查都对。**
  - 核心闭包的 34 个模块在仓库之外从前导（Lean 4.29.1）重新编译，退出码都为 0，核心模块没有输出。
  - 回执列出的闭包源声明 2462 条（核心 2342、基础 120），`#print axioms` 全部为空；其中 Population 138、Premises 161、Openness 253 条全部为空。
  - 闭包有 6697 个常量（Population 316、Premises 522、Openness 576）。依赖公理的只有 38 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同。
  - 六个提交的回执（`075031`、`083222`、`083222`、`101327`、`112632`、`132639`）及外围回执（`075308`、`084107`、`084107`、`102016`、`112836`、`132949`）：每个源哈希、检查器哈希与保留产物都与该提交一致，保留的回执与正式回执相同，没有多出的文件。定理／声明审计为 1356/2161 → 1356/2161 → 1430/2280 → 1488/2361 → 1512/2392，闭包 31 → 33 → 34，核心公理为空，`core_compiles_from_prelude` 为真。回执时间都早于其提交。
  - 章节 §9 的各模块计数都等于回执，合计 1512（核心 1478 加桥接 34）。
  - 在快照副本上运行登记检查（`registry.py --check`）与四份记录的聚焦检查（`research.py check --ids`）：134 份记录，没有错误，没有源漂移；P34b 新增的别名检查也通过。
  - P36 只改名：22 个改动的核心文件去掉注释后按词元比较，只有等长的标识符替换，没有插入或删除；替换是单射；保留运行的 29 个签名日志的 737 条签名在改名之下逐条相同；定理与声明审计数不变（1356/2161）；研究文档只追加了 §50 与英文段落，历史各节未改。
  - P36b：13 个英文标题、三处研究句与一个链接标签改动；记录只改了 sha256 行，所刷新的哈希恰是只改标题行的章节的新哈希。
- **数学被接受。** 对象中没有错误的 Lean 陈述。`counting_under`、`counting_binds_iff`、`taking_binds_counting`、`enclosed_counting_under`、`finite_counting_under`、`finite_counting_binds_iff`、`finite_change_bound_iff`、`enclosed_iff_finite_counting_under`、`binding_counting` 与 `binding_contingent` 都按所述成立且精确；`Pointwise` 只用于见证方向，是公平的假设。
- **本审查写了 32 条探针声明（定理 22 项），生成 82 个常量，都不依赖任何公理。**
- **问题共六项（V1–V6）。** 最重要的是 V1 与 V2。
  - **V1（过强，P38c 的说法）：** 起约束的队列中，“活动需要支持与有界传递起约束”只在 `World.Binds` 的实例意义上成立。它的网让每个关系项以其所立的水平依存于每个关系项，所以活动需要支持对任何活动都成立，有界传递对任何流都成立（探针 `bindingQueue_shape`）。`binding_counting` 本身对：它相对于 `World.Binds`。但“八个前提即使都在起作用”“依存与传递起约束”“约束世界而非空成立”读得比定义强。
  - **V2（过强）：** 计划 §10 把 Ren 的“let's aim for the strongest claim”写成“它是不用公理所能得到的最强陈述”；P38 的计划行写“每个前提加了什么在计数上补全”，随后 P38b 与 P38c 又补了两部分；总陈述末句“这是形式陈述的完整”没有指明是计划 §9 的四项标准。
  - **V3（表述，第一部分的总陈述）：** “每件都已在 Lean 中检查”覆盖了不是 Lean 陈述的话；被围住一句省去“从某步起”与随之的“此后没有关系项活跃的一步上没有生起”；终结之步一句省去“满足八个前提”；部分与区域一条不写 P37 定理的前提（平衡、扣留后的水平、只有活跃者给予、活动需要支持、要求不放松）；计数部分只说活动的计数、每个选择之下所选前提都起约束时的规律未陈述，这些边界不在总陈述之内。
  - **V4（缺少陈述）：** 三处“恰”或“没有”的说法没有核心定理：被围住时变化界恰在选中平衡、体现与耗散时是规律（探针 `enclosed_change_bound_iff`）；没有有限世界使每个前提都起约束（探针 `no_finite_binds`）；有限世界中除普查外七个条件都可以起约束（探针 `fhatch_binds_but_counted`），而这样的有限世界中计数的规律没有陈述，也未列为开放。
  - **V5（记账）：** counting-under-enclosure 的局限与下一步仍写“每个前提都起约束时计数的全部规律没有陈述”；章节 §8 进一步的证明中“整体与部分”一条只引到 P35；P36 对照表漏了 `Provisioned.gift → provision`；P38c 把算术引理 `add_sub_turn_add` 放进 Openness，与 P34b U6 集中算术的做法不一致。
  - **V6（命名）：** “idle”有两种意思（`hatch_idle` 不参与流；`drivenQueue` 的地关系项不活跃却驱动交换）；`bindingQueue` 以其在定理中的作用命名，不以其动力学命名；P36 之后核心仍有金融词 `credits`、`overdraw`（P36 只承诺改见证名）。
- **第十三次审查 U1–U9 的处理（P34b）：** 全部关闭，见 §1 的表。

**Summary (English).**

- **The mechanical checks pass.**
  - The 34 modules of the core closure recompile from the prelude (Lean 4.29.1) outside the repository. All exit 0; the core modules produce no output.
  - All 2462 closure source declarations listed by the receipt (2342 core, 120 foundation) have empty `#print axioms` reports, including all 138 of Population, 161 of Premises and 253 of Openness.
  - The closure has 6697 constants (Population 316, Premises 522, Openness 576). Exactly 38 depend on an axiom: generated `injEq` lemmas, each on `propext` only, equal to the receipt's list.
  - For each of the six commits, the core receipt (`075031`, `083222`, `083222`, `101327`, `112632`, `132639`) and periphery receipt (`075308`, `084107`, `084107`, `102016`, `112836`, `132949`) match the commit: every source hash, checker hash and retained artifact; the retained receipt equals the committed one; no extra files. Theorems and declaration audits go 1356/2161 → 1356/2161 → 1430/2280 → 1488/2361 → 1512/2392, the closure 31 → 33 → 34; core axioms empty; `core_compiles_from_prelude` true. Every receipt predates its commit.
  - All per-module counts in chapter §9 equal the receipt, summing to 1512 (1478 core plus 34 bridge).
  - On a copy of the snapshot, `registry.py --check` and `research.py check --ids` on the four records pass: 134 records, no errors, no source drift, P34b's new alias check included.
  - P36 renames only. In the 22 changed core files, with comments stripped, the token streams differ only by equal-length identifier substitutions, injective, with no insertion or deletion. The 737 signatures in the 29 retained signature logs agree entry by entry under the renaming. Counts are unchanged (1356/2161). The study only appended §50 and its English paragraph.
  - P36b changes 13 English titles, three research sentences and one link label. Its record edits are sha256 lines only, and the refreshed hashes are those of the chapters whose title line alone changed.
- **The mathematics is accepted.** No Lean statement in the object is wrong. `counting_under`, `counting_binds_iff`, `taking_binds_counting`, `enclosed_counting_under`, `finite_counting_under`, `finite_counting_binds_iff`, `finite_change_bound_iff`, `enclosed_iff_finite_counting_under`, `binding_counting` and `binding_contingent` hold as stated and are exact. `Pointwise` is used only in the witness direction and is a fair hypothesis.
- **The probes are 32 source declarations (22 theorems); none of their 82 constants depends on any axiom.**
- **Six findings (V1–V6).** V1 and V2 matter most.
  - **V1 (overclaim, P38c prose).** In the binding queue, "activity needing support and bounded transmission bind" holds only in the instance sense of `World.Binds`. Its web makes every relatum depend on every relatum at what it stands at. So activity needing support holds under any activity, and bounded transmission under any flow (probe `bindingQueue_shape`). `binding_counting` is correct relative to `World.Binds`. But "even with all eight premises at work", "dependence and transmission bind" and "constrains the world rather than holding vacuously" read more into it than the definition gives.
  - **V2 (overclaim).** Plan §10 turns Ren's "let's aim for the strongest claim" into "Part I is the strongest claim with no axiom". The P38 plan row says counting "is now complete", and P38b and P38c then added two parts. The Part I statement's last sentence, "the completeness of a formal statement", does not say it means the plan's four criteria.
  - **V3 (presentation, Part I stated whole).**
    - "Each checked in Lean" covers sentences that are not Lean statements.
    - The enclosure sentence drops "from some step" and the law that comes with it, that from then on nothing arises across a step at which nothing is active.
    - The end-step sentence drops "meeting the eight premises".
    - The parts-and-regions bullet gives P37's theorems without their premises: balance, withheld levels, only active relata giving, activity needing support, unloosened requirements.
    - The statement does not say, in place, that its counting part is about activity only and that the laws where the premises of each selection bind are not stated.
  - **V4 (missing statement).** Three "exactly"/"no" claims have no core theorem:
    - under enclosure, the change bound is a law exactly where balance, embodiment and dissipation are selected (probe `enclosed_change_bound_iff`);
    - no finite world binds every premise (probe `no_finite_binds`);
    - in a finite world every clause of `Binds` but the census can hold (probe `fhatch_binds_but_counted`), and the laws of counting in such worlds are neither stated nor listed as open.
  - **V5 (bookkeeping).**
    - counting-under-enclosure's limitations and next step still say the laws where every premise binds are not stated.
    - Chapter §8's further-proofs item on the whole and its parts stops at P35.
    - The P36 rename table omits `Provisioned.gift → provision`.
    - P38c puts the arithmetic lemma `add_sub_turn_add` in Openness, against P34b's U6 consolidation.
  - **V6 (naming).**
    - "Idle" has two senses: `hatch_idle` takes no part in the flow, while `drivenQueue`'s ground relatum is inactive but drives the exchange.
    - `bindingQueue` names its role in a theorem, not its dynamics.
    - The financial verbs `credits` and `overdraw` remain after P36, whose pass promised witness names only.
- **The thirteenth review's U1–U9 (P34b).** All are closed; see the table in section 1.

## 0. Scope, materials and method

**Object.** `main` at `c95f6576`. Times are UTC, 2026-10-10.

| Commit | Time | Content | Core receipt | Periphery receipt |
|---|---|---|---|---|
| `9ad91910` | 08:06:59 | P34b (thirteenth review, §48) and P35 (§49) | `075031` | `075308` |
| `4284d6ab` | 08:57:32 | P36 renames and plan §10 (§50) | `083222` | `084107` |
| `ba3b0e3b` | 09:07:52 | P36b, "generative" to "becoming" at entry points and titles | `083222` | `084107` |
| `82a9e3aa` | 10:35:44 | P38: chapter restructure, Part I statement, counting under each selection (§52) | `101327` | `102016` |
| `0ed94604` | 11:33:19 | P38b: finite worlds under each selection (§54) | `112632` | `112836` |
| `c95f6576` | 13:34:06 | P38c: counting where every premise binds (§55) | `132639` | `132949` |

`fc0f3c25` (P37, 10:12:44) and `8e857735` (P39, 11:26:01) belong to another session. They were not reviewed, except for the Part I statement's account of P37 (V3).

**Isolation.**

- The object was exported with `git archive c95f6576 | tar -x` into `review14/snap/` and read from there.
- The core was rebuilt in `review14/build/` from copies of the snapshot's sources, with `import Std` removed from the three foundation files as `check_becoming.py` does for its prelude-only run.
- `git show`, `git diff`, `git log`, `git blame` and `git ls-tree` were run read-only against `/Users/ren/theories`. No file there was edited, and no state-changing git command, `make` target or repository checker was run against it.
- The registry checks ran on the snapshot copy only.
- The Mathlib periphery and `Becoming.Bridge` were not rebuilt. Their receipts and hashes were checked. `Bridge.lean` is unchanged in all six commits.

**Materials.** Each sha256 prefix equals that of `git show c95f6576:<path>`, except the three foundation files after `import Std` was removed.

| File | sha256 | Lines |
|---|---|---|
| `Becoming/Population.lean` | `fdd2aeece2b0b9b0` | 1412 |
| `Becoming/Premises.lean` | `282c1ed9d3dcb9ea` | 1695 |
| `Becoming/Openness.lean` | `736f42dabea4d9e3` | 2877 |
| `Becoming/Admission.lean` (P37, for V3) | `b38a7b1b0b6c4569` | — |
| `Becoming/Dependence.lean` | `984ce6e6b0cf1f32` | — |
| `Becoming/Flow.lean` | `4af6e1afa8f70407` | — |
| `Becoming/Identity.lean` | `de978e73fcc237b2` | — |
| `Becoming.lean` | `15360ca724977f1f` | — |
| other 25 closure modules | listed in `review14/logs/` | — |
| `InquirySufficiency.lean` (after removal) | `d4a95ca842f46ffa` | — |
| `RelationalRenewal.lean` (after removal) | `b97719c886e3dcd0` | — |
| `chapters/THE-THEORY-OF-BECOMING.md` | `6afe21caa659b57f` | 981 |
| `BECOMING-RENEWAL-READING.md` (study) | `b272925ddb8123e0` | 3811 |
| `BECOMING-UNIFICATION-PLAN.md` | `40c881a463bfb58c` | 390 |
| `BECOMING-P32-P34-REVIEW.md` (thirteenth review) | `91f1e808c848c867` | 1047 |
| `records/counting-under-enclosure.json` | `4a99731d4d7225a3` | 612 |
| `records/whole-law-of-counting.json` | `50bb9bc49e86f4e4` | 654 |
| `records/continued-change-needs-openness.json` | `9a010e546c523b22` | 731 |
| `records/map-of-premises.json` | `4a96af2e871edc64` | 562 |
| `sources/…/2026-10-10-zero-axiom-part-and-names.md` | `ae0f351949efa345` | 45 |
| `sources/…/2026-10-10-axiom-route-levels-and-possibilities.md` | `06edbaf87b47a1ff` | 67 |
| `becoming/becoming-verification.json` (receipt `132639`) | `7e012ae3e0a386fa` | 16718 |
| `becoming/check_becoming.py` | `3f5adf4fcd8f546c` | 1047 |
| `…/correction-inquiry-verification.json` (receipt `132949`) | `6d106b178f951699` | 1491 |
| `tools/research/registry.py` | `1309452c10bfc025` | 364 |
| `review14/Review14.lean` (probes) | `25aad897b5c8b3b4` | 300 |
| `review14/Review14Audit.lean` | `ea58ecdefcf7af2e` | 54 |

**Method.**

1. **Build.** The 34 closure modules were compiled one at a time in the receipt's order with `lean +leanprover/lean4:v4.29.1 -o`.
2. **Audit.** One file imports `Becoming` and `Lean`. It walks every constant of every closure module and collects axioms with `Lean.collectAxioms`. It then runs `#print axioms` on each of the 2462 closure declarations the receipt lists.
3. **Receipts.** A read-only script compared each receipt in the six commits with that commit's sources, checkers, retained artifacts and retained `verification.json`.
4. **Renames (P36).**
   - Token diff of the 22 changed core files between `9ad91910` and `4284d6ab`, comments removed, with the old-to-new identifier map checked for functionality and injectivity.
   - Entry-by-entry comparison of the 29 retained signature logs between runs `075031` and `083222`.
5. **Reading.**
   - Population's P34b additions, the Premises selection section, Openness from `EnclosedQueue` to the end, and `World.Binds`, `Hatch` and `Admission`'s boundary theorems.
   - Study §§48–50 and 52–55 with their English paragraphs, plan §10, chapter Part I header, items 3–4, the Part I statement and §8–§9.
   - The four records, both source files.
   - The P36b diff of chapters, entry points, records and data.
6. **Probes.** `Review14.lean` (term mode, imports `Becoming`) was compiled against the rebuilt core and audited by `Review14Audit.lean`, which walks every constant of the probe module and prints the axioms of each source declaration (appendices A and B).

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Build, axioms, receipts, hashes, artifacts, counts | **Correct.** <ul><li>34 modules compile from the prelude; 2462 empty reports; 38 generated `injEq` on `propext`, as listed.</li><li>Six core and six periphery receipts match their commits; retained equals committed.</li><li>§9 counts equal the receipt.</li></ul> | — |
| 2. Records, aliases, registry | **Correct.** Registry and focused checks pass on the snapshot; the new alias check exists (`registry.py` l. 157–163). Two records carry stale fields. | V5 |
| 3. P34b: U1–U9 handled? | **Yes.** See the table below. One later regression of U6. | V5 |
| 4. P35: `ChangeBound`, `occurrences`, `changeBound_iff_zero`, `ChangeBound.lpo_of_ends`; `enclosure_bounds_change`, `EnclosedQueue`, `enclosed_counting`, `FiniteQueue`, `finite_counting`, `enclosed_iff_finite_counting`, `finite_dissipation_binds`, `replaced_attains`, `lpo_of_finite_ends` | **Correct and exact.** The law is stated once, from step 0; the end step needs LPO (witness `Swap`), as the thirteenth review proposed. | — |
| 5. P36: renames only; history keeps old names | **Yes.** Code differs only by an injective identifier map; signatures agree under it; counts equal; historical study sections untouched. One table row missing. | V5 |
| 6. P36b: entry points and titles only | **Yes.** Title lines, three research sentences, one link label; record edits are hash refreshes for title-only changes. | — |
| 7. P38: `Premise`, `Meets`, `BindsCounting`, `counting_under`, `counting_binds_iff`, `taking_binds_counting`, `drivenQueue`; `closingQueue`, `BoundsChange`, `enclosed_counting_under` | **Correct and exact.** Two kinds of law under the 256 selections. The enclosure law carries its own step. The "exactly" for the change bound under enclosure is unproved in the core but true (probe). | V4 |
| 8. P38b: `Ring`, `ring`, `embodiedRing`, `balancedRing` and their `_meets`; `finite_counting_under`, `finite_counting_binds_iff`, `finite_change_bound_iff`, `enclosed_iff_finite_counting_under`, `Queue.lone_settles` | **Correct and exact.** Three kinds of law in finite worlds, pairwise distinct (fixed by the two `_iff` theorems). | — |
| 9. P38c: `BindingQueue`, `bindingQueue` and its `_premised`, `_binds`, `_exceeds`, `_dissipative`; `binding_counting`, `binding_contingent` | **Correct relative to `World.Binds`.** Dissipation binds substantively at `T`; support and transmission are met only by the web's shape. | V1 |
| 10. Exactness claims ("iff", "exactly", "three kinds", "only this one") | **All Lean "iff"s hold.** Three prose "exactly"/"no" claims lack a theorem; probes supply two and show the third's open neighbour. | V4 |
| 11. `Pointwise` | **Fair.** Ten theorems take it, and use it only to carry a witness's counts to the given counts (`enclosed_iff_finite_counting` composes two such theorems). Each concrete `Q` used in the core and probes proves it directly. | — |
| 12. Non-vacuity of witnesses | **Yes**, except the binding queue's web. Each `_meets` world fails exactly the stated premise. `drivenQueue`'s dissipation is vacuous and disclosed. | V1 |
| 13. Part I statement: three parts accurate, no overclaim | **Accurate in substance; imprecise in five places; "complete" and "strongest" overreach.** | V2, V3 |
| 14. Ren's words vs AI; 生生 and generative/degenerative; nondual method | **Kept apart.** <ul><li>The region reading of generative/degenerative/neutral is marked "AI reading pending Ren" in chapter and study.</li><li>P36b follows Ren's "model of becoming/evolution".</li><li>The one slip is "strongest" stated as fact.</li></ul> | V2 |
| 15. zh/en parity | **Parallel** in the Part I statement, items 3–4, §§52–55 and the records read. One pre-existing en-only passage lies outside the object (section 3). | — |
| 16. Naming against Ren's criteria | **Mostly met.** Three precision points. | V6 |

**The thirteenth review's findings, as handled in P34b.**

| Item | Status | Evidence |
|---|---|---|
| U1 | closed | `Balance`, `Tally.balance`, `Tally.ceasing_le`, `tally_iff`, `balance_not_tally` are in Population. "The tally is the whole law of counting" replaces the headline wherever current. No current "平衡是计数的全部规律" remains outside history. |
| U2 | closed | whole-law-of-counting, census-balance-under-continuation, census-balance and counting-under-enclosure use the standard sentence, which quotes Ren's tag question and marks the inference as the AI's. |
| U3 | closed | `tended_not_binds` (now `openQueue_not_binds`), `binds_arising` and `binds_adds` are in the core; the docstring is corrected; P38c then answers the open question (V1 qualifies how). |
| U4 | closed | The law is stated once with a change bound from step 0; `EnclosedQueue` has `Nat` relata and no `T`. |
| U5 | closed | `Swap`, `ChangeBound.lpo_of_ends`, `World.lpo_of_finite_ends`. P35 prose says "does not recur". The pre-existing `World.arising_stops` keeps its name, defined as non-recurrence. |
| U6 | closed, one later regression | `le_dest`, `le_of_add_le_add_right`, `add_right_cancel`, `add_sub_turn`, `add_sub_of_le` head Dependence; `le_total_of_mem` is in Flow. P38c adds `add_sub_turn_add` in Openness (V5). |
| U7 | closed | `Tally.congr`, `tally_iff_counted` in core; §46 reads "有函数外延性时", with an in-place note. |
| U8 | closed | Identity (l. 97, 688) and the checker's scope say "more formations are listed after the step than before". |
| U9 | closed | Open items updated with P35; `registry.py` checks Lean-shaped aliases against the bound receipts. The check passes on the snapshot. |

## 2. Findings

### V1. Overclaim (P38c prose): in the binding queue, activity needing support and bounded transmission "bind" only by the web's shape

**Evidence.**

- `BindingQueue.web` (Openness l. 2614–2619) sets `requires _ _ _ := True` and `need t _ k := level n c T E t k`. Every relatum requires every relatum, at exactly that relatum's level.
- Probe `bindingQueue_reflexive` shows the web is definitionally the reflexive web of R1. Probe `bindingQueue_shape` then gives two facts.
  - With this level path and *any* activity predicate whatever, the web is `Dependent` (`reflexive_dependent`). The support inequality is `level ≤ level`.
  - For *every* flow on `Nat`, the web transmits every dependence within `1 + E` (`reflexive_transmits`). `TransmitsWithin` reduces to "a level after the step is at most a level before it plus δ", true because all levels are at most `1 + E`.
- So in the witness these two premises exclude no activity and no exchange. Their clauses in `World.Binds` are met because something is active (probe `reflexive_binds_dependent`) and something descends: an instance exists. The premises do no work there. Only dissipation binds substantively, at `T`, where the front loses its excess within a closed span.
- The theorem is right. `binding_counting` quantifies over worlds meeting `World.Binds`, and the witness meets it. The prose reads more into "binds":
  - Openness module doc l. 164–166: "every relatum depends on every relatum, needing what it stands at, so activity needing support and bounded transmission bind wherever something joins". The English P38c study paragraph and the whole-law-of-counting record repeat it. The plan's P38c rows (zh l. 333, en l. 388) describe the web without the disclosure.
  - Chapter item 3 (en l. 104, zh l. 72) sets the open queue, where "nothing depends on anything", against the binding queue, which "meets all eight with each binding". This suggests the binding queue removes the open queue's idleness of dependence. For dependence and transmission it does so only nominally.
  - Study §55 解读 (l. 3401): "所以八个前提即使都在起作用，对计数的约束也不多于计数表与……".
  - The 一元的读法 bullet (l. 3405), "起约束说的是前提在这个展开中确有实例：有依存……", is accurate as an instance reading. But the dependence in the witness is not a formed relation that differentiates one relatum's condition from another's. Under the nondual method it is a representational identity, not a relation that forms and changes.
  - Counterreply 1 (l. 3409) argues: "更强的依存只会使更少的世界满足前提，不会使已在所有起约束的世界中失败的性质成为规律". This is true of the witness and does not meet the objection. The objection concerns the *notion* of binding. A notion of binding that requires a premise to exclude something would admit fewer worlds, and might admit more laws.
  - `World.Binds` docstring (Premises l. 825): "so the premise constrains the world rather than holding vacuously". Non-vacuous is not the same as constraining. The binding queue meets the dependent and transmitting clauses while both premises constrain nothing. The docstring predates the object (P29), but P38c's argument rests on it.
- Partial disclosure exists:
  - whole-law-of-counting limitations: "the binding queue's web is the weakest … and serves only as a witness";
  - map-of-premises limitations: "binding says only that some condition is met".
  - Neither says that the support and transmission premises are identically true in the witness.

**Fix.**

1. Where the binding queue is described (module doc, chapter item 3, §55, plan P38c rows, whole-law-of-counting), say that in it activity needing support and bounded transmission hold for any activity and any flow, because each need is defined as the level. Their clauses of `World.Binds` are met only as instances; dissipation alone binds substantively.
2. State `binding_counting` as the law "where every clause of `World.Binds` has an instance". Replace "八个前提即使都在起作用" by "即使 `World.Binds` 的八个条件都有实例".
3. Correct the `Binds` docstring: "something meets its condition, so the premise does not hold vacuously; an instance need not exclude anything (`Review14.bindingQueue_shape`)".
4. Add to whole-law-of-counting's next step the open question this leaves. Under a sense of binding in which each premise excludes some alternative the representation allows, is "something arises" still the only added law? Moving R1 into the core would make the disclosure checkable.

### V2. Overclaim: "the strongest claim with no axiom" and "complete"

**Evidence.**

- Ren's words are an aim: "let's aim for the strongest claim without axiom, as the first part" (zero-axiom-part-and-names). Plan §10, under "结构（AI 的读法）", states it as a fact.
  - l. 308: "第一部分：不用公理。它是不用公理所能得到的最强陈述".
  - l. 376: "Part I is the strongest claim with no axiom".
  - The source's AI-authored operational reading says the same.
- Nothing establishes it. Three things show the opposite:
  - The P38 plan row (en l. 386) says "What each premise adds to counting is now complete". P38b then added the finite-world laws, and P38c the binding laws.
  - §55's boundary leaves the laws where the premises of each selection bind, and the counts of standing and dependence under the premises, unstated.
  - V4 finds the finite-world binding laws neither stated nor listed.
- The Part I statement ends: "这是形式陈述的完整，不是必然性的证明 / This is the completeness of a formal statement". In P23 this phrase meant the plan's four checkable criteria (§9 l. 222–227). In the Part I statement it reads as a claim that Part I is complete.

**Fix.**

- Plan §10: "第一部分以不用公理所能得到的最强陈述为目标 / Part I aims at the strongest claim with no axiom".
- P38 row: "complete under the 256 selections, for activity counts in general worlds", in place of "now complete".
- Part I statement: "这是计划 §9 四项标准意义上形式陈述的完整，不是必然性的证明", with a link. Also list in place what remains open (V3).

### V3. Presentation (Part I stated whole): five imprecisions against the Lean

**Evidence and fix, item by item** (chapter l. 445–497).

1. "每件都已在 Lean 中检查 / each checked in Lean" (l. 447, 473). Several sentences are not Lean statements:
   - "These laws exclude no unfolding beyond what the representation excludes".
   - "Whether actual unfoldings meet the premises is empirical".
   - "The laws and theorems give no part significance" (in part backed by `Web.significance_undetermined`, P39).

   *Fix:* "每条定理都已在 Lean 中检查", and mark the meta-statements as such.
2. "从某步起被围住时，选中平衡、体现与耗散，还多一个变化界 / With enclosure from some step on, selecting balance, embodiment and dissipation adds a change bound" (l. 458, 484). `World.enclosed_counting_under` adds `∃ T B, ChangeBound T B n c a ∧ ∀ t ≥ T, 0 < a t → 0 < n t`: a bound *from some step*, and from then on nothing arising across a step at which nothing is active.
   - For selections that do not bind counting, the second conjunct is a law not otherwise present. Probes `bed_quiet_eventually` and `bed_not_quiet`: under balance, embodiment and dissipation alone, it holds from some step on but not at every step.
   - Classically the conjunct follows from the bound. Constructively it does not, which is why Lean states it ("the second condition carries its step").
   - Item 4 says this correctly ("再加从某步起的变化界与此后这一条").

   *Fix:* use item 4's wording.
3. "若对每个这样的有限世界都有此后不再生起的一步 / for every such finite world" (l. 466, 492). `World.lpo_of_finite_ends` quantifies over finite worlds that meet the eight premises and have decided activity. "Under enclosure change does not recur" likewise needs a census, embodiment, balance and dissipation.

   *Fix:* name them.
4. "部分与区域 / Parts and regions" (l. 461, 487) states P37's theorems with no premises:
   - `Balances.supported_iff_within_margin`, `supported_of_net_give` and `admits_of_net_draw` assume a balanced flow and withheld levels (`L.WithheldLevels part W l`). The comparison "without the part" holds the rest of the exchange fixed (`Flow.withhold`), and that is a representational choice.
   - `gains_from_supported` ("支持只从被支持者获得 / support is gained only from the supported") assumes balance, only active relata giving, activity needing support, and `Unloosened` requirements.
   - Every other bullet of part II names its premises.

   *Fix:* "在平衡的流中，以扣留部分而其余交换不变的水平为比较……；在平衡、只有活跃者给予、活动需要支持且要求不放松时，支持只从被支持者获得".
5. Part II's counting bullet is accurate as far as it goes, but its boundary is not stated in place:
   - it concerns the counts of activity only;
   - the counts of standing and dependence under the premises are not stated;
   - the laws where the premises of each selection bind are not stated;
   - "binds" is `World.Binds` (V1).

   The boundary is in §55 and the records, not in the statement that "closes Part I".

   *Fix:* one sentence of boundary after the counting bullet.

### V4. Missing statement: three "exactly"/"no" claims without a core theorem, and one unlisted gap

**Evidence.**

1. **Exactness of the change bound under enclosure.** The following say the change bound is added "exactly where balance, embodiment and dissipation are selected" (zh "恰在"):
   - Openness module doc l. 134;
   - the English P38 study paragraph;
   - plan P38 rows (zh l. 331, en l. 386).

   The core proves the characterization `enclosed_counting_under` and the finite-world exactness `finite_change_bound_iff`, but no enclosed-world exactness theorem. It is true: probe `enclosed_change_bound_iff` proves that "from some step, a change bound and nothing arising across a step at which nothing is active" is a law of counting in worlds enclosed from some step on, under a selection, iff `BoundsChange`. Its counterexample for the other selections is the growing count `n t = t + 1`, `c = 0`, `a = 1`.

   Item 4's "不选耗散时被围住不加任何规律 / without dissipation enclosure adds no law" is true but weaker than this: enclosure also adds no law where balance or embodiment is unselected.
2. **"No finite world binds every premise"** (§55, chapter item 3, Openness doc l. 172). This holds by definition, since `Binds.counted` is `¬ w.Finite`, but no theorem states it. Probe `no_finite_binds` is one line.
3. **Finite worlds in which the other seven clauses bind.** Probe `fhatch_binds_but_counted` shows the census clause is the only obstacle:
   - `fhatch`, which is `hatch` without its idle ground relata, is finite and meets all eight premises;
   - it meets the seven clauses of `World.Binds` other than `counted`;
   - and `¬ fhatch.Binds`.

   So `hatch` binds every premise only by adding infinitely many relata that take no part (`hatch_idle`). Nothing in the object states the laws of counting in finite worlds where the seven non-census clauses bind. The expected law is the finite-world law plus "something arises", but a finite witness for each such tally is not given. Nor is this listed among the open items, which name only "the laws where the premises of each selection bind".

**Fix.**

- Move `enclosed_change_bound_iff` (with `occurrences_congr` and `eventualBound_pointwise`) and `no_finite_binds` into Openness and cite them where "exactly" and "no finite world" are said.
- Replace item 4's "不选耗散时" by "恰在不同时选中平衡、体现与耗散时".
- Add the finite-world binding laws to the open items of whole-law-of-counting and counting-under-enclosure, and to chapter §8.

### V5. Bookkeeping

**Evidence and fix.**

1. **counting-under-enclosure** (record, at `c95f6576`):
   - Limitations: "每个前提都起约束时计数的全部规律没有陈述，它至少多出一个生起 / the whole law of counting where every premise binds is not stated, adding at least an arising".
   - next_delta: "每个前提都起约束时计数的规律 / The laws where every premise binds".
   - Both are stale since P38c (`binding_counting`), although the record's P38c history entry re-points it to receipt `132639` with "断言不变".

   *Fix:* replace them with "已给出（whole-law-of-counting，相对于 `World.Binds`）", and list the open item of V4.3.
2. **Chapter §8, further proofs, "整体与部分 / The whole and its parts"** (l. 804, 812) cites only P34 and P35 for counting. It does not record:
   - the selection laws (P38, P38b);
   - the binding law (P38c);
   - the remaining open items: the laws where the premises of each selection bind, and in finite worlds where the seven non-census clauses bind.

   *Fix:* update the parenthesis.
3. **P36 rename table** (plan §10, l. 346–366) has no row for `Provisioned.gift → Provisioned.provision` (Reserve l. 943). The token diff finds it twice, and the commit message mentions it ("the provisioned gift -> provision"). Otherwise the table covers every renamed identifier the diff finds, including the local renames `keeper → drawer` (Lossless), `bloom → consumer` (Recycle), `other → dweller`, `supply → resource` and `spends → undermines`.

   *Fix:* add the row.
4. **Arithmetic placement.** P34b (U6) collected natural-number arithmetic at the head of Dependence. P38c adds `add_sub_turn_add` (Openness l. 2567), a pure `Nat` identity used only by `bindingQueue_balanced`.

   *Fix:* move it next to `add_sub_turn` in Dependence.

### V6. Presentation (naming against Ren's criteria)

**Evidence.**

1. **"Idle" has two senses.**
   - `World.hatch_idle` defines idle ground relata as standing at nothing, not active, and taking no part in the flow.
   - `drivenQueue` (Premises l. 1420, 1436; chapter item 3; study §52 table, "闲置的地关系项") calls its driver "an idle ground relatum", although the driver takes part at every step and exchanges a unit with every ground relatum. It is inactive, not idle in `hatch_idle`'s sense.

   *Fix:* "an inactive ground relatum / 不活跃的地关系项".
2. **`BindingQueue` names its role** in `binding_counting`, not its dynamics. Ren's criterion asks for formal words that describe the abstract dynamics. The dynamics is a queue open at every step but one, at which it closes and loses an excess. A name such as `OnceClosedQueue` or `SingleClosureQueue` would say this. This matters little, but it is the one P38c name chosen by role.
3. **P36's pass covered witnesses**, as its commit says. The core still has the accounting verbs `credits` (seven names, e.g. `Renewable.stepwise_credits_before_escalation`, `Ranking.credited_before_loss`) and `overdraw` (`Renewable.whole_run_credits_overdraw`). This is not a defect of P36, which did what it claimed. It is a candidate for the planned body sweep under "social and financial words not first".

## 3. What remains sound

- **Every Lean statement in the object.** In particular:
  - **Population.**
    - `ChangeBound`, `occurrences`, `ChangeBound.from_zero` (bound `B + T + total (steps 0 T) n`), `changeBound_iff_zero`, `ChangeBound.not_recurring` and `ChangeBound.reach` (`gone + n ≤ B + B * B`).
    - `ChangeBound.lpo_of_ends`, with witness `Swap` (change bound 2).
  - **Premises.**
    - `counting_under`: two kinds of law, by case split on the selection, with `queue`, `embodiedQueue`, `openQueue` and `drivenQueue` as witnesses for the selections that do not bind counting. Its exactness comes through `counting_binds_iff` and `Queue.lone_tally`.
    - `taking_binds_counting` is a genuine second route: a closed family of the relata active after the step cannot be given to without taking.
  - **Openness, enclosure.**
    - `enclosure_bounds_change`, `EnclosedQueue` (store `B − occurrences`), `closingQueue`, `enclosed_counting_under`.
    - The finite queue of size `B + B * B + 1`, `finite_counting`, `finite_dissipation_binds`, `replaced_attains`.
  - **Openness, finite worlds.** The ring family seats a queue round `2M + 1` places by its own recursion, avoiding the prelude's `%` lemmas with `propext`. The three rings each fail exactly embodiment, balance or dissipation. Three kinds of law in finite worlds. `enclosed_iff_finite_counting_under` ↔ `BoundsChange ∧ BindsCounting`, with counterexamples `n t = t + 1` and `lone` (`lone_settles`).
  - **Openness, binding.**
    - `bindingQueue_exceeds` and `_dissipative` are a real dissipation at `T`.
    - `binding_contingent`: `hatch` rests; the one-member replacing queue `bindingQueue 1 1 0 2` binds every clause and arising and ceasing recur.
- **Witness fairness.** Each counterexample world fails exactly the premise claimed and meets the others. The vacuity of dissipation in `drivenQueue` is disclosed. V1 concerns the reading of one witness, not its validity.
- **Disclosure of commitments.** Decidability, `Pointwise` and natural-number steps are disclosed in every record. `Pointwise` is avoidable (`tally_iff_counted`), and is used only in witness directions.
- **Provenance.**
  - Ren's instructions are quoted verbatim with sources.
  - The generative/degenerative/neutral reading of regions is marked as AI's pending Ren in the chapter and study.
  - The U2 sentence is uniform across the four counting records.
  - P36b follows Ren's "it should be the model of becoming/evolution" and keeps "generative" for the property Ren named ("its existence creates more possibilities of becoming"). Ren's two confirmed readings (possibilities as what can form next; the whole as never a center's model) are used as confirmed.
- **Nondual method.**
  - The Part I statement opens with the single change read of activity, dependence and standing.
  - Rest and openness are stated as relations of exchange, not as properties of separate holders.
  - No ethical predicate enters Part I's object.
- **Counts and stamps** agree everywhere checked.
- **Outside the object, observed only.** Chapter §8's English "Continuation" further-proofs bullet (l. 815) lists three items absent from the Chinese (l. 807). These are a witness with two removable sources, the deontic reading of the weak form, and the clearer's witness. They were introduced by W8 (`4d4e06b3`); P36 only renamed `keeper` to `clearer` on that line. This is a zh/en parity gap for the session that owns W8.

## 4. What would change the verdicts

- **V1 would become an error** if a text claimed that in the binding queue the support or transmission premise *excludes* some activity or flow. None does. It would disappear if the core showed a binding-queue variant whose web makes activity needing support fail for some activity on the same level path, while still counting every tally with something arising. Equally, a theorem would settle the question if it showed the law unchanged under a stronger notion of binding.
- **V2 would be withdrawn** by a theorem or argument that no axiom-free statement in the representation is stronger than Part I, which is not available. It would also be withdrawn by Ren saying "strongest" was meant as a fact rather than an aim.
- **V3–V6 are presentation and bookkeeping.** No mathematical verdict depends on them.
- **The mathematical verdicts would change** if:
  - a rebuild of `Becoming.Bridge` or the periphery against this core failed (only their receipts were checked);
  - an `#print axioms` report differed on another machine with the same toolchain;
  - a retained artifact differed from the committed file under a hash collision. None is expected.

## Appendix A. Probe source

`review14/Review14.lean` (sha256 `25aad897b5c8b3b41a06409097c5b6505d48fe13330f48fa9d096bdf56974d6b`, 300 lines). Compiled with `LEAN_PATH=review14/build lean +leanprover/lean4:v4.29.1 -o Review14.olean Review14.lean` against the rebuilt core: exit 0, no output.

Groups:

- **R1** (V1): the reflexive web; support and transmission hold by shape (`reflexive`, `reflexive_dependent`, `reflexive_transmits`, `bindingQueue_reflexive`, `bindingQueue_shape`, `reflexive_binds_dependent`).
- **R2** (V4.2): `no_finite_binds`.
- **R3** (V4.3): `fhatch`, a finite world meeting the eight premises and every clause of `Binds` but the census (`FHatch.*`, `fhatch_*`, `fhatch_binds_but_counted`).
- **R4** (V4.1): `enclosed_change_bound_iff`, with `EventualBound`, `occurrences_congr`, `eventualBound_pointwise`.
- **R5** (V3.2): under balance, embodiment and dissipation alone, quiet holds from some step under enclosure but not at every step (`bed`, `bed_bounds`, `bed_not_binding`, `bed_quiet_eventually`, `bed_not_quiet`).

```lean
/-
Fourteenth independent review, probes (P34b-P38c). Not part of the repository.
Compiled against the core at c95f6576 rebuilt from the prelude (Lean 4.29.1).
Every declaration here must have an empty axiom report (see Review14Audit.lean).
-/
import Becoming

namespace Review14

open Becoming

/-! ## R1. The binding queue's support and transmission hold by the web's shape alone

`BindingQueue.web` requires every relatum of every relatum and needs exactly the level.
Such a web is `Dependent` whatever is active, and transmits every dependence within any
bound on the levels, for every flow whatsoever. So in the witness of `binding_counting`
the clauses `Binds.dependent` and `Binds.transmitting` are met in the instance sense, and
the premises they make non-vacuous exclude no activity and no exchange. -/

/-- A reflexive web: every relatum requires every relatum, needing what it stands at. -/
def reflexive {R : Type} (level : Nat → R → Nat) (active : Nat → R → Prop)
    (draws : Nat → R → R → Prop) : Web R R :=
  ⟨level, active, fun _ _ _ => True, fun t _ k => level t k, draws⟩

/-- Activity needing support holds in a reflexive web whatever is active. -/
theorem reflexive_dependent {R : Type} (level : Nat → R → Nat) (active : Nat → R → Prop)
    (draws : Nat → R → R → Prop) : (reflexive level active draws).Dependent :=
  fun _ _ _ _ _ => Nat.le_refl _

/-- Bounded transmission holds in a reflexive web for every flow, within any bound on the
levels. -/
theorem reflexive_transmits {R : Type} (L : Flow R R) (level : Nat → R → Nat)
    (active : Nat → R → Prop) (draws : Nat → R → R → Prop) {B : Nat}
    (bounded : ∀ t k, level t k ≤ B) (c : R) :
    L.TransmitsWithin (reflexive level active draws) c B :=
  fun t _ _ _ _ => ⟨trivial, Nat.le_trans (bounded (t + 1) c) (Nat.le_add_left _ _)⟩

/-- The binding queue's web is reflexive (definitionally). -/
theorem bindingQueue_reflexive (n c : Nat → Nat) (T E : Nat) :
    (World.bindingQueue n c T E).web =
      reflexive (BindingQueue.level n c T E) (fun t k => Queue.holds n c k t)
        (fun _ _ _ => True) :=
  rfl

/-- In the binding queue's web, activity needing support would hold under any activity
whatever, and bounded transmission (δ = 1 + E) holds of every flow on `Nat` whatever. -/
theorem bindingQueue_shape (n c : Nat → Nat) (T E : Nat) :
    (∀ active : Nat → Nat → Prop,
      (reflexive (BindingQueue.level n c T E) active (fun _ _ _ => True)).Dependent) ∧
    ∀ (L : Flow Nat Nat) (k : Nat),
      L.TransmitsWithin (World.bindingQueue n c T E).web k (1 + E) :=
  ⟨fun active => reflexive_dependent _ active _,
   fun L k => reflexive_transmits L _ _ _ (fun t k => BindingQueue.level_le t k) k⟩

/-- So in a reflexive embodied web, `Binds.dependent` is met as soon as anything is active. -/
theorem reflexive_binds_dependent {R : Type} {level : Nat → R → Nat}
    {active : Nat → R → Prop} {draws : Nat → R → R → Prop}
    (embodied : ∀ t x, active t x ↔ 0 < level t x) {t : Nat} {f : R} (now : active t f) :
    ∃ t f c, (reflexive level active draws).active t f ∧
      (reflexive level active draws).requires t f c ∧ 0 < (reflexive level active draws).need t f c :=
  ⟨t, f, f, now, trivial, (embodied t f).mp now⟩

/-! ## R2. No finite world binds every premise

This holds by the definition of `World.Binds` (its census clause is `¬ w.Finite`). -/

theorem no_finite_binds (w : World) (finite : w.Finite) : ¬ w.Binds :=
  fun binds => binds.counted finite

/-! ## R3. A finite world meeting the eight in which every clause of `Binds` but the census
holds

`fhatch` is `hatch` without its idle ground relata: the food, the parent and the child.
It is finite, meets all eight premises, and meets the seven clauses of `World.Binds`
other than `counted`. So among finite worlds, "every premise binds" fails only through the
census clause; `hatch` binds every premise by adding infinitely many idle relata
(`World.hatch_idle`). -/

namespace FHatch

inductive R where
  | food
  | parent
  | child

def emb : R → World.Hatch.Relatum
  | .food => .food
  | .parent => .parent
  | .child => .child

def flow : Flow R R where
  present
    | 0 => [.parent]
    | _ + 1 => []
  take t x y := World.Hatch.flow.take t (emb x) (emb y)
  give t x y := World.Hatch.flow.give t (emb x) (emb y)

def web : Web R R where
  level t x := World.Hatch.level t (emb x)
  active t x := 0 < World.Hatch.level t (emb x)
  requires _ x y := World.Hatch.eats (emb x) ∧ y = .food
  need _ _ _ := 1
  draws _ x y := x = .parent ∧ (y = .food ∨ y = .parent)

theorem taking_part : ∀ {t : Nat} {g : R}, g ∈ flow.present t → t = 0 ∧ g = .parent
  | 0, _, .head _ => ⟨rfl, rfl⟩
  | 0, _, .tail _ no => nomatch no
  | _ + 1, _, no => nomatch no

abbrev all : List R :=
  [.food, .parent, .child]

theorem all_distinct : Distinct all :=
  ⟨fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
   fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩

theorem closed (t : Nat) : flow.ClosedAt all t :=
  fun f present c out => match f, taking_part present, c, out with
  | _, ⟨_, rfl⟩, .food, out => absurd (.head _) out
  | _, ⟨_, rfl⟩, .parent, out => absurd (.tail _ (.head _)) out
  | _, ⟨_, rfl⟩, .child, out => absurd (.tail _ (.tail _ (.head _))) out

end FHatch

def fhatch : World :=
  ⟨FHatch.R, FHatch.flow, FHatch.web⟩

instance fhatch_decided : ∀ t x, Decidable (fhatch.web.active t x) :=
  fun t x => Nat.decLt 0 (World.Hatch.level t (FHatch.emb x))

theorem fhatch_finite : fhatch.Finite :=
  ⟨FHatch.all, FHatch.all_distinct, fun
    | .food => .head _
    | .parent => .tail _ (.head _)
    | .child => .tail _ (.tail _ (.head _))⟩

theorem fhatch_balanced : fhatch.Balanced
  | 0, .food => rfl
  | 0, .parent => rfl
  | 0, .child => rfl
  | _ + 1, .food => rfl
  | _ + 1, .parent => rfl
  | _ + 1, .child => rfl

theorem fhatch_dissipative : fhatch.Dissipative :=
  fun cs t distinct closed f present => match t, f, FHatch.taking_part present with
  | _, _, ⟨rfl, rfl⟩ =>
    have given : total cs (fhatch.flow.give 0 .parent) ≤ 1 :=
      total_le_at (a := .child) (fun b positive => match b, positive with
        | .child, _ => rfl
        | .food, positive => absurd positive (Nat.lt_irrefl 0)
        | .parent, positive => absurd positive (Nat.lt_irrefl 0)) distinct
    Decidable.of_not_not fun wrong => absurd (Nat.le_of_eq (closed .parent present .food
      fun mem => wrong (Nat.le_trans (Nat.add_le_add given (sign_le_one _))
        (le_total_of_mem (q := fhatch.flow.take 0 .parent) mem))).1) (Nat.not_succ_le_zero 1)

theorem fhatch_premised : fhatch.Premised :=
  .of (fun _ _ _ c requires => match c, requires with | _, ⟨_, rfl⟩ => Nat.le_add_left 1 _)
    fhatch_balanced
    (fun t f _ present _ => match t, f, FHatch.taking_part present with
      | _, _, ⟨rfl, rfl⟩ => Nat.zero_lt_one)
    (fun t f c present takes => match t, f, FHatch.taking_part present, c, takes with
      | _, _, ⟨rfl, rfl⟩, .food, _ => ⟨Nat.zero_lt_one, rfl, .inl rfl⟩
      | _, _, ⟨rfl, rfl⟩, .parent, _ => ⟨Nat.zero_lt_one, rfl, .inr rfl⟩
      | _, _, ⟨rfl, rfl⟩, .child, takes => absurd takes (Nat.lt_irrefl 0))
    fhatch_dissipative (fun _ _ => Iff.rfl) (World.Finite.counted fhatch_finite)
    ⟨0, fun _ _ _ g descends requires => match g, FHatch.taking_part descends.1 with
      | _, ⟨_, rfl⟩ => ⟨⟨trivial, requires.2⟩, Nat.le_refl 1⟩⟩

/-- Every clause of `World.Binds` but the census holds in the finite `fhatch`. -/
theorem fhatch_binds_but_counted :
    fhatch.Finite ∧ fhatch.Premised ∧ ¬ fhatch.Binds ∧
    (∃ t f c, fhatch.web.active t f ∧ fhatch.web.requires t f c ∧ 0 < fhatch.web.need t f c) ∧
    (∃ t c, fhatch.web.level (t + 1) c ≠ fhatch.web.level t c) ∧
    (∃ t f c, f ∈ fhatch.flow.present t ∧ 0 < fhatch.flow.give t f c) ∧
    (∃ t f c, f ∈ fhatch.flow.present t ∧ 0 < fhatch.flow.take t f c) ∧
    (∃ cs t f, Distinct cs ∧ fhatch.flow.ClosedAt cs t ∧ f ∈ fhatch.flow.present t ∧
      0 < total cs (fhatch.flow.take t f)) ∧
    (∃ t x, fhatch.web.Arises t x) ∧
    (∃ t x g c, fhatch.flow.DescendsAt fhatch.web t x g ∧ fhatch.web.requires (t + 1) x c) :=
  ⟨fhatch_finite, fhatch_premised, no_finite_binds _ fhatch_finite,
   ⟨0, .parent, .food, Nat.zero_lt_one, ⟨trivial, rfl⟩, Nat.zero_lt_one⟩,
   ⟨0, .food, Nat.ne_of_lt (Nat.succ_lt_succ (Nat.zero_lt_succ 1))⟩,
   ⟨0, .parent, .child, .head _, Nat.zero_lt_one⟩,
   ⟨0, .parent, .food, .head _, Nat.zero_lt_two⟩,
   ⟨FHatch.all, 0, .parent, FHatch.all_distinct, FHatch.closed 0, .head _,
     Nat.lt_of_lt_of_le Nat.zero_lt_two (le_total_of_mem (a := FHatch.R.food)
       (q := fhatch.flow.take 0 FHatch.R.parent) (.head _))⟩,
   ⟨0, .child, Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
   ⟨0, .child, .parent, .food, ⟨.head _, Nat.zero_lt_one, Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
     ⟨trivial, rfl⟩⟩⟩

/-! ## R4. Under enclosure, the change bound is a law exactly where balance, embodiment and
dissipation are selected

The module documentation of `Becoming.Openness` says enclosure adds a law "exactly" for
these selections; the core proves the characterization (`World.enclosed_counting_under`)
and the finite-world exactness (`World.finite_change_bound_iff`), but not this exactness
as a named theorem. -/

/-- From some step `T` on, change stays within a bound and nothing arises across a step at
which nothing is active: the extra law of `World.enclosed_counting_under`. -/
def EventualBound (n c a : Nat → Nat) : Prop :=
  ∃ T B, ChangeBound T B n c a ∧ ∀ t, T ≤ t → 0 < a t → 0 < n t

theorem occurrences_congr {T : Nat} {q q' : Nat → Nat} (same : ∀ s, q s = q' s) :
    ∀ t, occurrences T q t = occurrences T q' t
  | 0 => rfl
  | t + 1 => (congrArg (· + mark (T ≤ t ∧ 0 < q t)) (occurrences_congr same t)).trans
      (congrArg (occurrences T q' t + ·) (mark_iff
        ⟨fun h => ⟨h.1, Nat.lt_of_lt_of_le h.2 (Nat.le_of_eq (same t))⟩,
         fun h => ⟨h.1, Nat.lt_of_lt_of_le h.2 (Nat.le_of_eq (same t).symm)⟩⟩))

theorem eventualBound_pointwise : Pointwise EventualBound :=
  fun {n c a _ c' a'} same ⟨T, B, bound, quiet⟩ =>
    have sums : ∀ s, c' s + a' s = c s + a s := fun s =>
      (congrArg (· + a' s) (same s).2.1.symm).trans (congrArg (c s + ·) (same s).2.2.symm)
    ⟨T, B, fun t later => Nat.le_trans (Nat.le_of_eq
        ((congrArg (· + occurrences T (fun s => c' s + a' s) t) (same t).1.symm).trans
          (congrArg (n t + ·) (occurrences_congr sums t)))) (bound t later),
     fun t later pos => Nat.lt_of_lt_of_le
       (quiet t later (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2.symm)))
       (Nat.le_of_eq (same t).1)⟩

theorem enclosed_change_bound_iff (S : World.Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey EventualBound) ↔
      World.BoundsChange S :=
  ⟨fun law =>
    if bounds : S .balanced = true ∧ S .embodied = true ∧ S .dissipative = true then bounds
    else
      have tally : Tally (fun t => t + 1) (fun _ => 0) (fun _ => 1) := fun t => ⟨t + 1, rfl, rfl⟩
      match (World.enclosed_counting_under S eventualBound_pointwise).mpr law
          (fun t => t + 1) (fun _ => 0) (fun _ => 1) tally
          (fun _ t _ => Nat.zero_lt_succ t) (fun b => absurd b bounds) with
      | ⟨T, B, bound, _⟩ => (Nat.not_succ_le_self B (Nat.le_trans
          (Nat.succ_le_succ (Nat.le_add_right B T)) (Nat.le_trans (Nat.le_add_right _ _)
            (bound (B + T) (Nat.le_add_left T B))))).elim,
   fun bounds => (World.enclosed_counting_under S eventualBound_pointwise).mp
      fun _ _ _ _ _ eventual => eventual bounds⟩

/-! ## R5. The extra law under enclosure carries its own step

For the selection of balance, embodiment and dissipation alone, in worlds enclosed from some
step on, nothing arising across a step at which nothing is active holds from some step on
but is not a law at every step. The Part I statement says only that this selection "adds a
change bound". -/

def bed : World.Premise → Bool
  | .dependent => false
  | .balanced => true
  | .acting => false
  | .taking => false
  | .dissipative => true
  | .embodied => true
  | .counted => false
  | .transmitting => false

theorem bed_bounds : World.BoundsChange bed :=
  ⟨rfl, rfl, rfl⟩

theorem bed_not_binding : ¬ World.BindsCounting bed :=
  fun ⟨_, _, giving⟩ => match giving with
    | .inl acting => Bool.noConfusion acting
    | .inr ⟨taking, _⟩ => Bool.noConfusion taking

theorem bed_quiet_eventually :
    ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets bed →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
      w.CountsObey fun n _ a => ∃ T, ∀ t, T ≤ t → 0 < a t → 0 < n t :=
  (World.enclosed_counting_under bed (Q := fun n _ a => ∃ T, ∀ t, T ≤ t → 0 < a t → 0 < n t)
    (fun same ⟨T, quiet⟩ => ⟨T, fun t later pos => Nat.lt_of_lt_of_le
      (quiet t later (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2.symm)))
      (Nat.le_of_eq (same t).1)⟩)).mp
    fun _ _ _ _ _ eventual => match eventual bed_bounds with
      | ⟨T, _, _, quiet⟩ => ⟨T, quiet⟩

theorem bed_not_quiet :
    ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets bed →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
      w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t :=
  fun law =>
    have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
      fun same quiet t pos => Nat.lt_of_lt_of_le
        (quiet t (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2.symm)))
        (Nat.le_of_eq (same t).1)
    Nat.lt_irrefl 0 ((World.enclosed_counting_under bed pointwise).mpr law
      Queue.lone (fun _ => 0) Queue.joins Queue.lone_tally
      (fun binds => absurd binds bed_not_binding)
      (fun _ => ⟨1, 1, fun t later => match t, later with
          | _ + 1, _ => Nat.le_of_eq (congrArg (1 + ·) (occurrences_quiet _)),
        fun t later _ => match t, later with | _ + 1, _ => Nat.zero_lt_one⟩)
      0 Nat.zero_lt_one)
where
  /-- After the first step nothing changes in `lone`, so nothing occurs from step one. -/
  occurrences_quiet : ∀ t, occurrences 1 (fun s => (fun _ => 0 : Nat → Nat) s + Queue.joins s) (t + 1) = 0
    | 0 => rfl
    | t + 1 => (congrArg (· + _) (occurrences_quiet t)).trans rfl

end Review14
```

## Appendix B. Probe axiom audit

`review14/Review14Audit.lean` (sha256 `ea58ecdefcf7af2e40d8fa689b0d52f3f76a9a8b16b011dc39fa1c9a5893b167`), run with `LEAN_PATH=review14/build lean +leanprover/lean4:v4.29.1 Review14Audit.lean`: exit 0.

Result: the module `Review14` has 82 constants (source declarations, auxiliary definitions, equation lemmas, match compilers and the like), and none depends on any axiom. All 32 source declarations print "does not depend on any axioms".

The core audit (`review14/build/CoreAudit.lean`, generated: an environment walk over the 34 closure modules followed by `#print axioms` on the 2462 receipt-listed closure declarations) gave `TOTAL 6697 WITH_AXIOMS 38`; the 38 are generated `injEq` lemmas, each depending on `propext` only, and equal the receipt's `generated_axiom_dependencies`; all 2462 reports are empty. Its output is `review14/logs/CoreAudit.out`.

```lean
import Review14
import Lean
open Lean Elab Command

/-! Axiom audit of the fourteenth review's probes: every constant the module `Review14`
generates (source declarations, auxiliary definitions, equation lemmas, structure eta and
match compilers alike), followed by `#print axioms` for each source declaration. -/

#eval show CommandElabM Unit from do
  let env ← getEnv
  let some idx := env.getModuleIdx? `Review14 | throwError "no module Review14"
  let mut count := 0
  let mut withAx := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some idx then
      count := count + 1
      let axs ← liftCoreM <| Lean.collectAxioms n
      if axs.size > 0 then withAx := withAx.push (n, axs)
  logInfo m!"PROBE_CONSTANTS {count} WITH_AXIOMS {withAx.size}"
  for (n, axs) in withAx do
    logInfo m!"AXIOMS {n} {axs.toList}"

#print axioms Review14.reflexive
#print axioms Review14.reflexive_dependent
#print axioms Review14.reflexive_transmits
#print axioms Review14.bindingQueue_reflexive
#print axioms Review14.bindingQueue_shape
#print axioms Review14.reflexive_binds_dependent
#print axioms Review14.no_finite_binds
#print axioms Review14.FHatch.R
#print axioms Review14.FHatch.emb
#print axioms Review14.FHatch.flow
#print axioms Review14.FHatch.web
#print axioms Review14.FHatch.taking_part
#print axioms Review14.FHatch.all
#print axioms Review14.FHatch.all_distinct
#print axioms Review14.FHatch.closed
#print axioms Review14.fhatch
#print axioms Review14.fhatch_decided
#print axioms Review14.fhatch_finite
#print axioms Review14.fhatch_balanced
#print axioms Review14.fhatch_dissipative
#print axioms Review14.fhatch_premised
#print axioms Review14.fhatch_binds_but_counted
#print axioms Review14.EventualBound
#print axioms Review14.occurrences_congr
#print axioms Review14.eventualBound_pointwise
#print axioms Review14.enclosed_change_bound_iff
#print axioms Review14.bed
#print axioms Review14.bed_bounds
#print axioms Review14.bed_not_binding
#print axioms Review14.bed_quiet_eventually
#print axioms Review14.bed_not_quiet
#print axioms Review14.bed_not_quiet.occurrences_quiet
```

Output (`review14/logs/Review14Audit.out`):

```text
PROBE_CONSTANTS 82 WITH_AXIOMS 0
'Review14.reflexive' does not depend on any axioms
'Review14.reflexive_dependent' does not depend on any axioms
'Review14.reflexive_transmits' does not depend on any axioms
'Review14.bindingQueue_reflexive' does not depend on any axioms
'Review14.bindingQueue_shape' does not depend on any axioms
'Review14.reflexive_binds_dependent' does not depend on any axioms
'Review14.no_finite_binds' does not depend on any axioms
'Review14.FHatch.R' does not depend on any axioms
'Review14.FHatch.emb' does not depend on any axioms
'Review14.FHatch.flow' does not depend on any axioms
'Review14.FHatch.web' does not depend on any axioms
'Review14.FHatch.taking_part' does not depend on any axioms
'Review14.FHatch.all' does not depend on any axioms
'Review14.FHatch.all_distinct' does not depend on any axioms
'Review14.FHatch.closed' does not depend on any axioms
'Review14.fhatch' does not depend on any axioms
'Review14.fhatch_decided' does not depend on any axioms
'Review14.fhatch_finite' does not depend on any axioms
'Review14.fhatch_balanced' does not depend on any axioms
'Review14.fhatch_dissipative' does not depend on any axioms
'Review14.fhatch_premised' does not depend on any axioms
'Review14.fhatch_binds_but_counted' does not depend on any axioms
'Review14.EventualBound' does not depend on any axioms
'Review14.occurrences_congr' does not depend on any axioms
'Review14.eventualBound_pointwise' does not depend on any axioms
'Review14.enclosed_change_bound_iff' does not depend on any axioms
'Review14.bed' does not depend on any axioms
'Review14.bed_bounds' does not depend on any axioms
'Review14.bed_not_binding' does not depend on any axioms
'Review14.bed_quiet_eventually' does not depend on any axioms
'Review14.bed_not_quiet' does not depend on any axioms
'Review14.bed_not_quiet.occurrences_quiet' does not depend on any axioms
```
