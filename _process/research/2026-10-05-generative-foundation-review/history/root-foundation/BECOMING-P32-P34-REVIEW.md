# P32 至 P34 及 P35/P36 草稿的独立审查 / Independent review of P32 to P34 and the P35/P36 drafts

2026-10-10。审查者：Claude Opus 5.5，独立 agent，未参与撰写 P32、P33、P33b、P34 与两份草稿。对象：`main` 的 `7f69f455`，以及草稿 `D35.lean`（sha256 `cb04495e4bf9e89e…`）与 `D36.lean`（`6e219ae82307702…`）。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of P32, P33, P33b, P34 or the two drafts. Object: `main` at `7f69f455`, and the drafts `D35.lean` (sha256 `cb04495e4bf9e89e…`) and `D36.lean` (`6e219ae82307702…`).

**摘要（中文）。**

- **机械检查都对。**
  - 核心闭包的 29 个模块在仓库之外从前导重新编译，退出码为 0，没有警告。
  - 2028 条源声明的公理报告全部为空。按第十二次审查的计法，其中定理 1263 项。
  - 闭包有 5650 个常量。依赖公理的只有 37 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同。新增的两条是 `Tended.Relatum.member.injEq` 与 `Tended.Relatum.ground.injEq`。
  - 四个提交各有回执：`192237`、`194202`、`195744` 与 `205957`。每个回执的 42 个源哈希、两个检查器哈希与 258 个保留产物都与该提交一致，保留的回执与正式回执相同。
    - 定理数为 1131 → 1153 → 1157 → 1190 → 1223。
    - 声明审计为 1826 → 1857 → 1862 → 1905 → 1958。
    - 较早的保留运行 `204915`（1212/1941）与 `193434`（1156/1860）通过，已被取代。
  - 外围回执 `192558`、`194414`、`195906` 与 `210516` 的 33 个源、3 个检查器与 74 个产物都对。外围没有重建。
  - 四个提交改动的记录共带 1590 个引用哈希与 459 个证明绑定，全部相符。时间戳都不晚于其提交：最晚的是 whole-law-of-counting 的 21:13:00Z，提交在 21:26:31Z。
  - 章节 §9 的模块计数都等于回执，合计 1223。
  - 名称：
    - 自 `a9326202` 起改动的 31 份记录中，587 个别名有 556 个在核心中解析。其余 31 个是非核心名称：26 个桥接，5 个外围。
    - 2285 个引用声明名中有 67 个不解析，全部在非核心文件中。
    - 核心名称无一缺失，T1 已修好。
  - 另一会话的 `cec60334`：P34 没有改动它的 10 个文件。它的草图 `Continuation.lean` 在 `7f69f455` 的核心上编译，30 条声明无公理。
  - 两份草稿在 `7f69f455` 上编译，退出码为 0，没有输出。它们的 70 条声明（48 + 22）与 144 个常量（97 + 47）都不依赖任何公理。
- **数学被接受。** Lean 陈述没有错误，两份草稿的定理也都对。
  - P32：`Census.balanceFrom` 的两半、`forces_iff_noSplit`、`forced_iff_more` 与 `Tandem` 都对。单步的刻画是精确的。
  - P33：`exchange_lowers`、`exchanges_finitely` 与 `World.exchange_stops` 都对，以复现的否定陈述。`exchange_needs` 的四个见证各缺一个前提。
  - P34：
    - `counting_laws` 是精确的，队列实现每个计数表。
    - 探针 `tally_iff_counted` 不用 `Pointwise` 也给出同一刻画。
    - `counting_free`、`counting_binds_jointly` 与 `premised_counting` 都对。
  - 草稿：
    - `change_within` 对，只用普查、全体体现、平衡、耗散与被围住。它数的是变化的步，不是事件；界可以达到（探针 `OneSwap.attained`）。
    - `enclosed_counting` 与 `finite_counting` 都是精确的。
    - 在 `Closed` 中，耗散真正起约束（探针 `closed_dissipation_binds`）。
  - 本审查写了 42 条探针声明（其中定理 34 项）与 8 个 `example`，生成的 78 个常量都不依赖任何公理。
- **问题共九项（U1–U9）。** 最重要的是 U1、U2 与 U3。
  - **U1（过强，P34 的标题）：“平衡是计数的全部规律”。**
    - 全部规律是计数表，即保持的形式。它严格强于普查的平衡 `Listed.across` 的等式。计数表恰是平衡加上“跨一步不再成立的不多于步前所列的”（探针 `tally_iff`）。
    - 每步零个在列、一个不再成立、一个开始成立：这满足平衡，却不是计数表，没有任何列出给出它（`balance_not_tally`）。所以存在一条平衡之外的计数规律（`ceasing_bound_law`）。
    - 英文 P34 段落写道 “the census balance and the recurrence laws … are all the laws of counting. They are”，按字面是错的。
    - 定理本身是对的，错的是它的规律的名字。这个名字出现在章节、记录、研究、计划、README、根模块与 Population 的说明中。
  - **U2（错误，出处；第十次审查 O8 的倒退）。**
    - 记录 whole-law-of-counting 与 census-balance-under-continuation 说，活动的计数“不是 Ren（提议中）的‘生成的’‘退化的’”。
    - 章节第 4 条、§8 与术语表把这一问题留给 Ren；§8 请 Ren 说明活动的读法是否仍是候选。另外四份记录写的是“是否为……由 Ren 选择”。
    - Ren 确认的是名称（“arising/ceasing is indeed better name”），不是这两个词的所指。
  - **U3（文档注释与 `World.Binds` 不符；缺反例）。**
    - `tendedQueue_premised` 的注释说耗散“只在没有东西参与交换的地方起约束”。按 `World.Binds` 的意义，在队首照管的队列中耗散从不起约束，活动需要支持与有界传递也不起约束（探针 `tended_not_binds`）。
    - “八个前提所加的只有这一条”，对包括前提空成立在内的全部世界是精确的。每个前提都起约束时，计数多了一条规律：某步有生起（`binds_adds`）。
    - 章节没有说明见证中有三个前提空成立。
- **其余各项。**
  - **U4（草稿，表述）。**
    - “从某步起有界”等价于“从第一步起有界”（`settles_iff_zero`）。所以 `enclosed_counting` 与 `finite_counting` 刻画的是同一规律（`same_laws`）。
    - `Closing` 的参数 `T`，以及 T 之前与地的交换，对精确性没有必要。
    - D36 的注释说少了。
  - **U5（草稿，缺反例）。**
    - 在有界的计数中给出变化的终结之步，或在满足全部八个前提的有限世界中给出最后一次生起，都蕴含 LPO（`lpo_of_settlesEnds`、`lpo_of_finiteEnds`）。
    - 草稿的说法是诚实的，但缺这一见证。
  - **U6（草稿，位置与名称）。**
    - 部分算术引理与核心已有的重复：`le_sub_of_add_le` 即 `RelationalRenewal.le_sub_from_add`；`fin_eq` 即前导中无公理的 `Fin.eq_of_val_eq`。
    - `below` 一族与 `Queue.reached` 应放在 Population，`Tended.decideEq` 应放在 Premises。
    - `since` 与 `below` 作为顶层名称太泛；`Settles` 暗示在某步停下；`Closing` 与 `Closed` 几乎同名。
  - **U7（表述）。**
    - `Pointwise` 是公平的替代，但可以不要。
    - 研究 §46 说“经典地每个性质都如此”，这不对：函数外延性不是经典原则。
    - 关于保持的形式，“免去带 `propext` 的消去律”这一理由不成立，因为核心已有无公理的 `add_right_cancel` 与 `le_dest`。真正的理由是 U1。
  - **U8（中英一致）。** P32 的英文说 “more stand after the step”。“立着”是本理论的术语（水平为正），而中文只说“步后多于步前”。
  - **U9（记账）。**
    - “有限世界中与被围住时计数的规律”在 `7f69f455` 正确地列为开放，草稿落地时须改。
    - 登记只核对引用的声明，不核对别名（T1 的残留）。
- **T1–T8 的处理。** 全部关闭，T1 留一处残留（U9）。

**Summary (English).**

- **The mechanical checks pass.**
  - The 29 modules of the core closure recompile from the prelude outside the repository. They exit 0 with no warnings.
  - All 2028 source declarations have empty axiom reports. Counted as the twelfth review counted, 1263 of them are theorems.
  - The closure has 5650 constants. Exactly 37 depend on an axiom, and they equal the receipt's list. All are generated `injEq` lemmas, and all depend only on `propext`. The two new ones are `Tended.Relatum.member.injEq` and `Tended.Relatum.ground.injEq`.
  - Each of the four commits has its own receipt: `192237`, `194202`, `195744` and `205957`. Each receipt's 42 source hashes, both checker hashes and 258 retained artifacts match that commit, and each retained receipt equals the committed one.
    - Theorems go 1131 → 1153 → 1157 → 1190 → 1223.
    - Declaration audits go 1826 → 1857 → 1862 → 1905 → 1958.
    - The earlier retained runs `204915` (1212/1941) and `193434` (1156/1860) passed and are superseded.
  - Periphery receipts `192558`, `194414`, `195906` and `210516`: 33 source hashes, 3 checker hashes and 74 artifacts match. The periphery was not rebuilt.
  - The records changed by the four commits carry 1590 reference hashes and 459 proof bindings, and all match. No stamp is later than its commit: the latest is whole-law-of-counting at 21:13:00Z, against a commit at 21:26:31Z.
  - All per-module counts in chapter §9 equal the receipt, and they sum to 1223.
  - Names:
    - In the 31 records changed since `a9326202`, 556 of 587 aliases resolve in the core. The other 31 are non-core: 26 bridge names and 5 periphery names.
    - Of the 2285 declaration names in their references, 67 do not resolve, all in non-core files.
    - No core name is missing, so T1 is fixed.
  - The other session's `cec60334` is undamaged: P34 touched none of its 10 files. Its sketch `Continuation.lean` compiles against the `7f69f455` core, and its 30 declarations are axiom-free.
  - The two drafts compile against `7f69f455`, exiting 0 with no output. None of their 70 declarations (48 + 22) or 144 constants (97 + 47) depends on any axiom.
- **The mathematics is accepted.** No Lean statement is wrong, and the drafts' theorems are correct.
  - P32: both halves of `Census.balanceFrom`, `forces_iff_noSplit`, `forced_iff_more` and `Tandem` are correct. The one-step characterization is exact.
  - P33: `exchange_lowers`, `exchanges_finitely` and `World.exchange_stops` are correct, stated as negated recurrence. Each of `exchange_needs`'s four witnesses lacks one premise.
  - P34:
    - `counting_laws` is exact, and the queue realizes every tally.
    - Probe `tally_iff_counted` gives the same characterization without `Pointwise`.
    - `counting_free`, `counting_binds_jointly` and `premised_counting` are correct.
  - The drafts:
    - `change_within` is correct and uses only a census, every relatum embodied, balance, dissipation and enclosure. It counts change steps, not events, and its bound is attained (probe `OneSwap.attained`).
    - `enclosed_counting` and `finite_counting` are exact.
    - In `Closed`, dissipation genuinely binds (probe `closed_dissipation_binds`).
  - The probes are 42 source declarations (34 of them theorems) and 8 `example`s. None of their 78 constants depends on any axiom.
- **Nine findings (U1–U9).** U1, U2 and U3 matter most.
  - **U1 (overclaim, P34's headline): "the balance is the whole law of counting".**
    - The whole law is the tally, the kept form. It is strictly stronger than the equation of the census balance `Listed.across`: a tally is exactly the balance together with "no more cease across a step than were listed before it" (probe `tally_iff`).
    - Take none listed, with one ceasing and one coming at every step. These counts balance but are no tally, and no listing has them (`balance_not_tally`). So a law of counting holds beyond the balance (`ceasing_bound_law`).
    - The English P34 paragraph says "the census balance and the recurrence laws … are all the laws of counting. They are". As written, this is false.
    - The theorem is right; the name of its law is wrong. The name appears in the chapter, the record, the study, the plan, the README, the root module and Population's docs.
  - **U2 (error, provenance; regression of the tenth review's O8).**
    - Records whole-law-of-counting and census-balance-under-continuation say the counting of activity "is not Ren's / the proposal's generative and degenerative".
    - Chapter item 4, §8 and the glossary leave this to Ren, and §8 asks Ren whether the activity reading is still a candidate. Four other records say "whether it is … is Ren's to choose".
    - Ren confirmed names ("arising/ceasing is indeed better name"), not what the two words refer to.
  - **U3 (a docstring at odds with `World.Binds`; missing counterexample).**
    - `tendedQueue_premised`'s docstring says dissipation "binds only where nothing takes part in an exchange". In the sense of `World.Binds`, dissipation never binds in the tended queue, and neither does activity needing support or bounded transmission (probe `tended_not_binds`).
    - "That is all the eight premises add" is exact over every world meeting them, including those where they hold idly. Where every premise binds, counting has a further law: something arises at some step (`binds_adds`).
    - The chapter does not say that three premises hold idly in the witness.
- **The rest.**
  - **U4 (drafts, presentation).**
    - Settling from some step is settling from the first step (`settles_iff_zero`). So `enclosed_counting` and `finite_counting` characterize one law (`same_laws`).
    - `Closing`'s parameter `T`, and its exchange with the ground before `T`, are not needed for exactness.
    - D36's docstring says less than is true.
  - **U5 (drafts, missing counterexample).**
    - An end step for change in a settling count implies LPO (`lpo_of_settlesEnds`). So does a last arising in a finite world meeting all eight premises (`lpo_of_finiteEnds`).
    - The drafts' wording is honest, but they lack this witness.
  - **U6 (drafts, placement and names).**
    - Some arithmetic helpers duplicate the core: `le_sub_of_add_le` is `RelationalRenewal.le_sub_from_add`, and `fin_eq` is the prelude's axiom-free `Fin.eq_of_val_eq`.
    - The `below` family and `Queue.reached` belong in Population, and `Tended.decideEq` belongs in Premises.
    - `since` and `below` are generic top-level names. `Settles` suggests stopping at a step. `Closing` and `Closed` are near-homonyms.
  - **U7 (presentation).**
    - `Pointwise` is a fair stand-in, and it can be avoided.
    - Study §46's "classically every property is" is wrong: function extensionality is not a classical principle.
    - The stated reason for the kept form, that it "spares the cancellation that carries `propext`", does not hold. The core has axiom-free `add_right_cancel` and `le_dest`. The real reason is U1.
  - **U8 (zh/en).** The English of P32 says "more stand after the step". "Stand" is a term of the theory (positive level), while the Chinese says only "more after the step than before".
  - **U9 (bookkeeping).**
    - "The laws of counting in finite worlds and under enclosure" is rightly listed open at `7f69f455`, and must change when the drafts land.
    - The registry checks reference declarations but not aliases (T1 residue).
- **T1–T8.** All are closed; T1 leaves one residue (U9).

## 0. Scope, materials and method

**Object.** The object is `main` at `7f69f455`, through four commits. Times are UTC, 2026-10-09.

- `df340093` (P32), 19:31:31Z. The census balance under every continuation, and the exact condition across one step.
- `49af9a36` (P33), 19:50:27Z. The exchange comes to rest under enclosure, and each premise is needed.
- `36918cfc` (P33b), 20:32:53Z. Integration of the twelfth review (T1–T8).
- `7f69f455` (P34), 21:26:31Z. The whole law of counting.

Two other commits are outside the object:

- `cec60334` (21:17:54Z) belongs to another session. It was checked only for damage by P34 (§1 row 1).
- `1f6f375f` (22:39:06Z) landed on `main` during this review, from the other session, and was not reviewed. It adds `Becoming.Continuation` and `Becoming.Standpoints`. It leaves `Openness.lean`, where D35 is to be appended, unchanged. None of its declarations shares a name with the drafts.

The drafts are:

- `D35.lean`: 477 lines, sha256 `cb04495e4bf9e89e409842448af1230aeb312fb88008a8c6b28a4565c4d51e26`.
- `D36.lean`: 243 lines, sha256 `6e219ae82307702552b0388ca137a5bb51da98f20c014add5d8366377a3c2fe7`.

**Isolation.**

- The object's files were exported with `git archive 7f69f455 <paths> | tar -x` into `review13/tree/`, and read from there.
- No file under `/Users/ren/theories` was edited, and no state-changing git command was run.
- The live tree's uncommitted files belong to the other session and were neither reviewed nor touched. They are `Continuation.lean`, `Standpoints.lean` and run `221224`.
- One Lean process ran at a time.
- The Mathlib periphery was not rebuilt; its receipts and hashes were checked.

**Materials.** Each sha256 prefix equals that of `git show 7f69f455:<path>`.

| File | sha256 | Lines |
|---|---|---|
| `Becoming/Population.lean` | `83eae8df1c4c4791` | 1140 |
| `Becoming/Premises.lean` | `65aaba427bac4871` | 1338 |
| `Becoming/Identity.lean` | `238849c844c4f3ff` | 1695 |
| `Becoming/Openness.lean` | `bd962a19c51f4e05` | 1204 |
| `Becoming/Dissipation.lean` | `f079e8b4e85babc6` | 1197 |
| `Becoming/Flow.lean` | `22fd0168ed9a8027` | 916 |
| `Becoming/Change.lean` | `34478e007ba6ce78` | 637 |
| `Becoming/Reserve.lean` | `deab1be369b820ef` | 982 |
| `Becoming/Space.lean` | `05b633bd26c2910a` | 1033 |
| `Becoming/Roles.lean` | `42c42c015abaf468` | 1540 |
| `Becoming.lean` | `7595568085aa1eea` | 240 |
| `lean/becoming/README.md` | `38d940104d008899` | 99 |
| `check_becoming.py` | `cac7467391f31015` | 859 |
| receipt `becoming-verification.json` (`205957`) | `4aed2a58571c33ed` | 14390 |
| `THE-THEORY-OF-BECOMING.md` | `e3be12c5b9238f37` | 728 |
| `NONDUAL-METHOD.md` | `8c48b03a167a8909` | 119 |
| `BECOMING-RENEWAL-READING.md` (study) | `416ec507b7bfd8e1` | 3117 |
| `BECOMING-UNIFICATION-PLAN.md` | `3403883b50fe5ca3` | 293 |
| record `whole-law-of-counting.json` | `56c84325007116ce` | 454 |
| record `census-balance-under-continuation.json` | `ca0a21a2da12953d` | 349 |
| record `census-balance.json` | `3446af0abe1a4e74` | 376 |
| record `continued-change-needs-openness.json` | `bd2ea3690331ffff` | 686 |
| record `map-of-premises.json` | `d95138fe8555d94d` | 526 |
| record `ceasing-needs-arising.json` | `e6ab2ae9b331e1ba` | 449 |
| record `coming-and-ceasing-keep-pace.json` | `8114a8d16f3bebac` | 491 |
| record `identity-across-steps.json` | `1fdc89f2ebfc3620` | 686 |
| `tools/research/registry.py` | `a3ad07543d631595` | 354 |
| `sources/…/2026-10-08-theory-of-becoming-priority.md` | `a08597b97e1763ff` | 43 |
| `sources/…/2026-10-09-arising-ceasing-names.md` | `143964d076571bd6` | 25 |
| `sources/…/2026-10-09-complete-theory-of-becoming.md` | `3ad2bca66a1e4fea` | 41 |

The twelfth review (`BECOMING-P30-P31-P29B-REVIEW.md`) was read first, for its format and findings.

**Method.**

1. **Build.**
   - The 29 core-closure modules were compiled in the checker's order from the exported sources, with `import Std` dropped from `GenerativeCore`, by `LEAN_PATH=<scratch> lean -o`.
   - `#print axioms` was run for all 2028 source declarations in the receipt.
   - An environment walk applied `Lean.collectAxioms` to every constant of every core module.
   - `env.contains` was checked for 2167 alias and reference names.
2. **Receipts and records.**
   - Per commit, a script read the receipt with `git show`. It hashed the 42 sources, both checkers and the 258 retained artifacts, and compared the retained receipt with the committed one.
   - A second script hashed every reference of every changed record, and evaluated every proof binding's pointers in that commit's receipt.
   - The four periphery receipts were checked the same way.
3. **Drafts.**
   - D35 and then D36 were compiled with `-o` against the `7f69f455` build.
   - They were audited by an environment walk and 70 `#print axioms` lines.
   - `cec60334`'s sketch was compiled and audited the same way.
4. **Texts.** I read the following:
   - the chapter: items 3–4 (zh 72 and 76, en 104 and 108); §8 (status 510, open questions 520/532, further proofs 576/583, review 587); the §9 tables; glossary rows 673 and 699;
   - study §43–§46 and the English paragraphs for P31–P34 (3090–3117);
   - plan rows P30–P34 (249–256 and 284–291);
   - the seven records named in the brief, plus identity-across-steps;
   - the Lean module docs and docstrings;
   - the five source files of Ren's words.
5. **Probes.** `Review13.lean` imports `Becoming` and `D36` and is written in term mode throughout. `Review13Audit.lean` audits it (Appendices A and B).

| Probe | Shows | Finding |
|---|---|---|
| Q1 `Balance`, `tally_balance`, `tally_le`, `tally_of_balance`, `tally_iff`, `balance_not_tally`, `ceasing_bound_law` | <ul><li>A tally is exactly the balance equation of `Listed.across` together with `c t ≤ n t`.</li><li>The equation alone admits none listed with one ceasing and one coming at every step, which no listing has.</li><li>"No more cease across a step than are listed at it" holds of every listing and does not follow from the equation.</li><li>`tally_of_balance` uses only the core's axiom-free `le_dest` and `Becoming.add_right_cancel`.</li></ul> | U1, U7 |
| Q2 `tally_congr`, `tally_iff_counted` | The counts some listing has are exactly the tallies, with pointwise equality and no `Pointwise` hypothesis. | U7 |
| Q3 `since_le`, `since_zero_le`, `settles_zero`, `settles_iff_zero`, `same_laws` | <ul><li>Settling from step `T` within `B` is settling from step 0 within `B + T + total (steps 0 T) n`.</li><li>So under the eight premises, worlds enclosed from some step and finite worlds have the same laws of counting.</li><li>This follows from the drafts' two theorems and `Finite.enclosed`.</li></ul> | U4 |
| Q4 `tended_dissipation_idle`, `tended_not_binds` | <ul><li>In the tended queue nothing taking part ever takes from a closed family.</li><li>Activity needing support never binds.</li><li>So the witness of `premised_counting` is not a `Binds` world.</li></ul> | U3 |
| Q5 `FirstChange.*`, `SettlesEnds`, `lpo_of_settlesEnds`, `FiniteEnds`, `lpo_of_finiteEnds` | <ul><li>The witness: one member is replaced across the step at the first `true` of a Boolean sequence. This is a tally, nothing joins an empty queue, and it settles from step 0 within 2.</li><li>An end step for every such count implies LPO.</li><li>So does an end step for arising in every finite world meeting the eight premises with decided activity, through the drafts' `closedQueue`.</li></ul> | U5 |
| Q6 `OneSwap.*`, `closed_dissipation_binds` | <ul><li>In the drafts' finite world with one member replaced across step 0 (B = 2), the front takes 2 from the closed family of all places, so dissipation binds.</li><li>The total standing at step 0 is 2.</li><li>From step 1 on, one active member plus one change step make 2, so `change_within`'s bound is attained.</li></ul> | §3 |
| Q7 `binds_arising`, `arising_pointwise`, `binds_adds` | <ul><li>Where every premise binds, every census counts some arising.</li><li>Under the eight premises alone this is no law: the empty tally is a counterexample.</li></ul> | U3 |
| Q8 eight `example`s | <ul><li>The P30 names resolve after P33b, as do `Web.Census.balanceFrom` and `World.premised_counting`.</li><li>D35's `le_sub_of_add_le` has the type of `RelationalRenewal.le_sub_from_add`.</li></ul> | U6 |

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Build, axioms, receipts, hashes, artifacts, bindings, counts, stamps; `cec60334` | **Correct.** <ul><li>29 modules compile from the prelude, with 2028 empty axiom reports. 37 generated `injEq` lemmas depend on `propext`, as listed.</li><li>For each of the four commits, 42 sources, 2 checkers and 258 artifacts match.</li><li>4 periphery receipts match (33 sources, 3 checkers, 74 artifacts).</li><li>1590 reference hashes and 459 bindings match.</li><li>Counts go 1131 → 1153 → 1157 → 1190 → 1223 and 1826 → 1857 → 1862 → 1905 → 1958, and §9 equals the receipt.</li><li>No stamp is later than its commit.</li><li>`cec60334` is untouched, and its sketch compiles axiom-free.</li></ul> | — |
| 2. Names and aliases | **Correct.** P30's names resolve. Every core alias and reference resolves; the unresolved names are non-core. | U9 (residue) |
| 3. P32: `Census.balanceFrom`, `balanceFrom_eq`, `arisingFrom_of_ceasingFrom`, `ceasingFrom_of_arisingFrom`, `Tandem` | **Correct.** <ul><li>Without splits: after + ceasings ≤ before + arisings.</li><li>Without merges: ≥.</li><li>With neither: equality.</li><li>Budding and merging each break one half.</li></ul> | U2 |
| 4. P32: `forces_iff_noSplit`, `paired*`, `forced_iff_more` | **Correct and exact.** The necessary direction uses decidable equality, as disclosed. One English word adds a term. | U8 |
| 5. P33: `exchange_lowers`, `exchanges_finitely`, `World.exchange_stops`, `World.exchange_needs` | **Correct.** <ul><li>The result is stated as non-recurrence, with the reason disclosed.</li><li>It needs only the standing census, balance, dissipation and enclosure.</li><li>Each of the four witnesses lacks exactly one premise.</li></ul> | — |
| 6. P33b: T1–T8 fixed everywhere? | **Yes, one residue.** See the table below. | U9 |
| 7. P34: `Listed.keeps`, `Tally`, `Queue.*`, `Pointwise`, `counting_laws`, `mark_turn` | **Correct and exact.** The queue realizes every tally. `Pointwise` is a fair stand-in, and avoidable. The law is misnamed "the balance". | U1, U7 |
| 8. P34: `counting_free`, `counting_binds_jointly`, `Tended`, `tendedQueue_premised`, `premised_counting` | **Correct as stated, and exact.** <ul><li>`Tended` is not a cheat: its front gives and takes at every join and leave.</li><li>Openness comes from exchange with infinitely many ground relata, as in `exposed`.</li><li>Dissipation, activity needing support and bounded transmission never bind. One docstring says otherwise, and the chapter does not say so.</li></ul> | U3 |
| 9. D35: `since`, `Settles`, `Settles.rests`, `change_within`, `Closing`, `closingQueue_*`, `enclosed_counting` | **Correct, axiom-free and exact.** <ul><li>`change_within` uses only what it needs, and its bound is attained.</li><li>`T` is redundant.</li><li>The constructive limit is unstated.</li><li>Some helpers are misplaced.</li></ul> | U4, U5, U6 |
| 10. D36: `below`, `Settles.reach`, `Closed`, `closedQueue_*`, `finite_counting` | **Correct, axiom-free and exact.** <ul><li>Dissipation, acting, taking, balance and embodiment bind in `Closed`.</li><li>Dependence and transmission hold idly.</li><li>It states the same law as D35.</li></ul> | U4, U5, U6 |
| 11. Ren's words vs AI; zh/en | **Kept apart, with two exceptions.** <ul><li>Ren's instruction is quoted verbatim.</li><li>Chapter item 4 separates Ren's tag question from the AI's inference.</li><li>Two records decide on Ren's behalf.</li><li>One English term differs from the Chinese.</li></ul> | U2, U8 |
| 12. Overclaims, counts, stale items | **Counts agree everywhere.** <ul><li>The headline overclaims.</li><li>The scope of "all the eight add" needs stating.</li><li>The open items are correct now, and go stale with the drafts.</li></ul> | U1, U3, U9 |

| Item | Status | Evidence |
|---|---|---|
| T1 | closed, one residue | <ul><li>The doubled `namespace World` is gone, and `World.slow`, `World.slow_world` and `Slow.*` resolve (Q8).</li><li>`registry.py` checks bound declarations against the receipt's elaborated names.</li><li>Aliases are still not checked (U9).</li></ul> |
| T2 | closed | <ul><li>`Carries.chain_ends` and `chain_ends_of_em` are now stated for arbitrarily long finite chains.</li><li>`Web.no_unending_chain` and `short_cascade` are added.</li><li>In-place notes are in §41 and the English P31 paragraph.</li></ul> |
| T3 | closed | <ul><li>The Markov sentence is corrected in place.</li><li>`LPO` and `Web.lpo_of_ending` (witness `Once`) are added.</li></ul> |
| T4 | closed | `holding_world`'s docstring now says "with every relatum embodied", and names `kindling` for the weaker form. |
| T5 | closed | <ul><li>No "only finitely many" remains in the `Openness` and `Premises` docs.</li><li>`Listed.lpo_of_few` (witness `Few`) is added.</li></ul> |
| T6 | closed | bounded-census-keeps-pace's next_delta: the shortfall is exact, and the rate form is sufficient. |
| T7 | closed | The source note dates 生起/止息 to P10 and P19, and to P23c for naming the parts. |
| T8 | closed | <ul><li>Plan row P30 cites receipt `170233` and periphery `170422`.</li><li>`lean-index.json` (12525 paths) lists no absent file.</li></ul> |

## 2. Findings

### U1. Overclaim (P34's headline): "the balance is the whole law of counting"

**Evidence.**

- **What "the census balance" names.** In the repository it is `Listed.across`, whose docstring begins "The census balance across a step". It states the equation `(l (t + 1)).length + ceasings (l t) p t = (l t).length + comings (l (t + 1)) p t`. The same word is used for this equation by:
  - the record census-balance;
  - chapter item 4;
  - `over_stretch`;
  - the recurrence laws of P26–P30.
- **What P34 proves.** P34 proves that the tally is the whole law, where `Tally n c a := ∀ t, ∃ k, n t = k + c t ∧ n (t+1) = k + a t`. The tally is strictly stronger than the equation:
  - `tally_iff`: `Tally n c a ↔ Balance n c a ∧ ∀ t, c t ≤ n t`.
  - `balance_not_tally`: with `n ≡ 0` and `c ≡ a ≡ 1`, the counts balance but are no tally. By `counting_laws` or `tally_iff_counted`, no listing on any type has them.
  - `ceasing_bound_law`: "no more cease across a step than were listed before it" holds of every listing and does not follow from the balance. It is a pointwise law of counting beyond the balance.
- **Where the texts equate the whole law with the balance.**
  - The commit title.
  - Record whole-law-of-counting:
    - title: "平衡是计数的全部规律 / The balance is the whole law of counting";
    - claim: "计数没有平衡之外的规律 / counting has no law beyond the balance".
  - The chapter:
    - item 4 (76/108);
    - status row 510;
    - further proofs 576/583;
    - the §9 Population row (615);
    - glossary 673.
  - Study §46:
    - its title;
    - the reading "为什么平衡是全部";
    - the English P34 paragraph (3115): "until now nothing showed that the census balance and the recurrence laws drawn from it are all the laws of counting. They are."
  - Plan rows 256 and 291.
  - The README (35) and `Becoming.lean` (84).
  - Population:
    - module doc (49, 55: "no law of counting holds beyond what the balance gives");
    - section header (580);
    - `counting_laws` docstring (730).
  - The drafts' docstrings for `enclosed_counting` and `finite_counting` repeat it ("the laws of counting are the balance, …").
- **The kept form is presented as a rewriting.** Study §46 "保持的形式" says the kept form "更多地说出关系" and "推出原来的形式". It does not say that the converse fails. Read with "the balance" in its established sense, the realization theorem is false.
- **What the extra content is.**
  - The recurrence laws go through `over_stretch` and need only the equation, so they are right as stated.
  - The extra content of the kept form is a one-step bound: what ceases across a step was listed before it.

**Fix.**

- Name the law precisely:
  - zh: "保持的平衡（平衡，加上跨一步不再成立的不多于步前所列的）是计数的全部规律";
  - en: "the kept balance (the balance, with no more ceasing across a step than were listed before it) is the whole law of counting";
  - or simply: "the tally is the whole law".
- Add `tally_iff` and `balance_not_tally` to Population, beside `Tally`.
- In §46 and the English paragraph, say that the kept form is strictly stronger, and why that matters.
- Update every place listed above. History lines may stay as history.

### U2. Error (provenance; regression of the tenth review's O8): two records decide what Ren's "generative/degenerative" refer to

**Evidence.**

- **The two records.**
  - whole-law-of-counting, correspondence:
    - zh: "这是活动的计数，英文名称 arising/ceasing 经 Ren 确认（中文 生起／止息 是 AI 的译名），不是 Ren 提议中的“生成的”“退化的”";
    - en: "it is not the proposal's generative and degenerative".
  - census-balance-under-continuation, correspondence:
    - zh: "这是活动的计数，不是 Ren 的“生成的”“退化的”";
    - en: "This is a count of activity, not Ren's generative and degenerative".
- **The rest of the repository leaves the question to Ren.**
  - Chapter item 4 (76/108): "指哪个部分由 Ren 选择 … 若取不重叠 … 就不是其所指（AI 的推论）".
  - §8 (520/532) asks: "这是否意味着活动的读法不再是候选，请 Ren 说明 / whether this means the activity reading is no longer a candidate is for Ren to say".
  - Glossary 699: "是否为…由 Ren 选择（若取不重叠则不是，AI 的推论）".
  - Records census-balance, ceasing-needs-arising, coming-and-ceasing-keep-pace and bounded-census-keeps-pace: "whether it is the proposal's generative and degenerative is Ren's to choose". They quote Ren's tag question and mark the conditional inference as the AI's.
  - P25b changed "不是 Ren 的…" to this form after O8.
- **Names are not referents.**
  - Ren's confirmation ("arising/ceasing is indeed better name") fixes the names of formal parts.
  - It does not fix what the proposal's words refer to.
  - The whole-law record cites the confirmation of the names and then concludes "not the proposal's generative and degenerative". That is the step §8 leaves to Ren.

**Fix.**

- In both records, and in both languages, use the standard sentence: Ren's tag question, with the conditional AI inference, as in census-balance.
- Add history lines.

### U3. Presentation (a docstring at odds with `World.Binds`) and missing counterexample: the witness of `premised_counting` meets three premises idly

**Evidence.**

- **The docstring.** `tendedQueue_premised` (Premises 1286) says: "No step at which the front is active is enclosed, so dissipation binds only where nothing takes part in an exchange."
- **What "binds" means.** Since P29, `World.Binds.dissipative` asks for something taking part that takes a positive amount from a closed family.
- **In the tended queue this never happens.**
  - At active steps, no family is closed.
  - At empty steps, nothing is taken (`tended_dissipation_idle`).
  - Activity needing support and bounded transmission never bind either, because `requires` is `False`.
  - So `¬ (tendedQueue n c).Binds` (`tended_not_binds`).
- **What each text discloses.**
  - The record's claim discloses both halves for dissipation. Its limitations give only the first.
  - Study rebuttal 5 discloses the first half.
  - Chapter item 3 (72/104) and the `Premises` doc (51–66) say only "meets all eight".
- **The scope of "all the eight add".**
  - "That is all the eight premises add" is exact over every world meeting the eight, including worlds where they hold idly. `premised_counting` is an iff over all such worlds.
  - `World.Binds` was introduced in P29 because "meets all eight" can be idle.
  - Where every premise binds, every census counts an arising (`binds_arising`).
  - The eight premises alone do not give this (`binds_adds`). The empty tally is admitted, and the empty tended queue meets all eight with nothing ever happening.

**Fix.**

- Docstring: "No step at which the front is active is enclosed, and nothing is taken at a step at which the queue is empty, so dissipation never binds here; nor do activity needing support and bounded transmission."
- Chapter item 3 (zh/en) should say:
  - that the three premises are idle in the witness;
  - that `premised_counting` ranges over worlds in which premises may hold idly.
- Complete the record's limitations.
- Record the boundary: what the eight add where all of them bind is not stated, and it includes at least one arising.

### U4. Presentation (drafts: exactness and structure): the two draft laws are one

**Evidence.**

- **Settling moves to step 0.** `settles_zero` proves `Settles T B n c a → Settles 0 (B + T + total (steps 0 T) n) n c a`. Hence `settles_iff_zero`: `(∃ T B, Settles T B …) ↔ ∃ B, Settles 0 B …`.
- **So the two laws are one.**
  - `same_laws` proves that, under the eight premises, worlds enclosed from some step on and finite worlds obey exactly the same laws of counting. It uses the drafts' theorems and `Finite.enclosed`.
  - Worlds enclosed at every step lie between the two, so they obey the same laws as well.
- **Parts of `Closing` are not needed for exactness.**
  - The unneeded parts are:
    - the parameter `T`;
    - the ground exchange before `T` (`Closing.exchange`);
    - the `if T ≤ t` in `spare`;
    - the `early` case of `closingQueue_dissipative`.
  - `closingQueue n c a 0 B'`, with `B'` from `settles_zero`, realizes every admitted count.
  - D36 already instantiates `Closing` at `T = 0`.
- **D36's docstring says less than is true.** "a finite world counts as a world enclosed from the first step does" holds equally for a world enclosed from any step on.

**Fix.**

- State the law once, as `∃ B, Settles 0 B`.
- Add `settles_zero` and `settles_iff_zero` to D35.
- Either drop `T` and use one queue world, or keep `T` for exposition and state `same_laws`.
- Correct D36's docstring.

### U5. Missing counterexample (drafts): what "settles" cannot give

**Evidence.**

- **The drafts are honest.** `Settles.rests` concludes `¬ ∀ N, ∃ t, N ≤ t ∧ 0 < c t + a t`, and its docstring says "Settling, change does not recur".
- **The stronger form implies LPO.**
  - `lpo_of_settlesEnds`: an end step for every settling tally in which nothing joins an empty queue implies LPO. The witness is `FirstChange`, which settles within 2.
  - `lpo_of_finiteEnds`: the same holds for a last arising in every finite world meeting all eight premises with decided activity. The witness is the drafts' own `closedQueue`.
- **The core states this limit only for webs.** P33b's `Web.lpo_of_ending` concerns one web (`Once`). Neither the core nor the drafts states it for counts, or for premised finite worlds. P35/P36 prose that says change "comes to rest" will need this.

**Fix.**

- Add the two witnesses to the drafts. They are short and axiom-free.
- In the texts, say "does not recur" or "stays within a bound", not "stops at some step".

### U6. Presentation (drafts: placement and names)

**Evidence and suggestions.**

- **Arithmetic helpers.**
  - D35's `le_sub_of_add_le` duplicates `RelationalRenewal.le_sub_from_add`, which is axiom-free and already imported (Q8).
  - `sub_eq_zero_of_le` follows from Joint's `sub_self_add` together with `le_dest`.
  - Axiom-free arithmetic is now spread over Horizon, Joint, Change, RelationalRenewal and, with the drafts, Openness. Horizon is not below Population (see U7).
  - Suggestion: gather it in one small section low in the import order, and move Horizon's `add_right_cancel` and `le_of_add_le_add_right` there.
- **`fin_eq`.** D36's `fin_eq` duplicates `Fin.eq_of_val_eq`, which is axiom-free (Appendix B).
- **Placement.**
  - `below`, `mem_below`, `distinct_below`, `total_below` and `Queue.reached` belong in Population.
  - `Tended.decideEq` belongs next to `Tended.Relatum` in Premises. Keep it hand-written, since derived instances may use `propext`.
- **Names.** These are for Ren to choose.
  - `since` and `below` are generic top-level names.
  - `Settles` reads as "comes to rest at some step", which is the LPO-strength form (U5). A budget-like name would say what it is.
  - `Closing` and `Closed` are near-homonyms, and both are near `ClosedAt`. After U4, one of them can go.

### U7. Presentation (P34: `Pointwise` and its explanation)

**Evidence.**

- **`Pointwise` is fair, and avoidable.**
  - It asks exactly what function extensionality would give, and it is a hypothesis, not an axiom.
  - `tally_iff_counted` states the characterization with no hypothesis.
- **"Classically" is wrong.**
  - Study §46 (2771) says "经典地每个性质都如此".
  - Function extensionality is not a classical principle. In Lean it comes from `Quot.sound`, independently of excluded middle and choice.
  - The record has it right: "有函数外延性时每个性质都如此".
- **The stated reason for the kept form does not hold.**
  - Study §46 (2770) and the English paragraph say the kept form "spares the proof cancellation, whose prelude lemma carries `propext`".
  - The core has axiom-free `Becoming.add_right_cancel` (Horizon) and `le_dest` (Change), and `tally_of_balance` uses them.
  - The real reason is U1: the equation is not realizable.

**Fix.**

- Add `tally_iff_counted`.
- Replace "经典地" with "有函数外延性时".
- Replace the stated reason with U1's.

### U8. Presentation (zh/en parity): "more stand after the step"

**Evidence.**

- **The English adds a term.** `forced_iff_more` compares list lengths, but the English says "more formations stand after the step than before". This wording appears in:
  - `Identity.lean` (97, 688);
  - `check_becoming.py` (233), and so the receipt scope;
  - record identity-across-steps (en);
  - study 3104;
  - plan 288.
- **The Chinese does not.** It says "步后多于步前" (study 2590; the record's zh).
- **"Stand" is a term of the theory.** It means positive level (立着, `StandingCensus`, `ComesToStand`). The lists here are lists of formations.

**Fix.** Say "more formations are listed after the step than before".

### U9. Presentation (bookkeeping)

**Evidence.**

- **Open items to update when the drafts land.** At `7f69f455` they are correct:
  - chapter §8 further proofs (576/583);
  - the record's limitations and next_delta;
  - study §46 Boundary (2748, 2790) and rebuttals 2 and 5;
  - the English P34 paragraph.
  When they change, they should carry U1's name and U4's single law.
- **Aliases are not checked.** `registry.py` checks bound declarations but not aliases. All 556 core aliases resolve now, but a future alias typo would pass (T1 residue).

**Fix.**

- Update the listed items with the drafts.
- Extend the registry check to aliases that look like Lean names.

## 3. What remains sound

- **Mechanics.**
  - The pure core is as stated.
  - Receipts, retained runs, periphery receipts, hashes, bindings, counts and stamps agree across all four commits.
  - §9's per-module counts sum to 1223 (for example Population 86, Premises 64, Openness 76, Identity 99).
- **P32.**
  - `Census.balanceFrom` bounds each step in the right direction, and `balanceFrom_eq` gives equality.
  - The recurrence halves follow through `le_over_stretch` and `ge_over_stretch`. The bounded half needs its bound, as stated.
  - `Tandem` loses one half each way.
  - `forced_iff_more` is exact through `paired`.
  - `forces_iff_noSplit` uses decidable equality, and this is disclosed.
- **P33.**
  - `exchange_lowers` is a correct one-step strict fall. Its double negation is resolved by Nat decidability.
  - `exchanges_finitely` and `exchange_stops` are honest negated recurrences.
  - The four worlds of `exchange_needs` (`exposed`, the cycle, `leaking`, `kindling`) each lack exactly the named premise.
- **P34.**
  - `Listed.keeps` is correct, and `across` follows from it.
  - `Queue.counts` covers every tally, with `c t` leaving from the front and `a t` joining at the back.
  - `counting_laws` is exact.
  - `counting_free` uses two worlds, each failing exactly one premise.
  - `counting_binds_jointly` isolates "nothing arises across a step at which nothing is active", and the lone arising shows this is no law of tallies.
  - `premised_counting` is exact as stated.
  - The tended queue's acting, taking, balance and embodiment bind. Its openness is the one the texts name.
- **The drafts.**
  - `change_within`:
    - It uses only a census, every relatum embodied, balance, dissipation and enclosure. Acting and taking are not used.
    - It implies `Settles.rests`, so every earlier witness of recurring change shows that the hypothesis it lacks is needed: `exposed`, `rest_needs_census`, `rest_needs_standing` and `World.rests_needs`.
    - It counts change steps, not events, and its bound is attained (`OneSwap.attained`: standing 2 at step 0; 1 + 1 = 2 from step 1).
    - A bound counting events fails in the same world: 1 + 2 > 2.
  - The counting theorems:
    - `enclosed_counting` and `finite_counting` are exact.
    - `Pointwise` is used only to transfer pointwise-equal counts.
  - In `Closed`:
    - Dissipation binds at change steps (`closed_dissipation_binds`).
    - Acting, taking, balance and embodiment bind.
    - Dependence and transmission hold idly, as in `Tended`.
    - No hidden vacuity makes the realization cheap.
- **Ren's words.**
  - "aim a complete theory of becoming, and finish related work" is quoted verbatim.
  - Chapter item 4 separates Ren's tag question from the AI's inference.
  - The formal names are the AI's, are marked as such, and are not taken from Ren's words.
  - Items 3–4, §46 and the English paragraphs agree in both languages, apart from U8.

## 4. What would change the verdicts

- **Rows 1 and 7–10.** A Lean statement in the four commits or the drafts that fails to compile from the prelude, or that depends on an axiom, would change these rows. None was found.
- **U1.** If "the balance" were redefined throughout as the kept form, and `Listed.across` renamed, U1 would be presentation only.
- **U2.** If Ren has ruled, in words that are not in the sources, that the activity reading is not what "generative/degenerative" refer to, U2 becomes a missing citation, and §8 needs the same update.
- **U3.** If "all the eight add" is meant to range over worlds with idle premises, which is what the theorem says, U3 reduces to the docstring and the disclosure. A theorem stating the counting laws over `Binds` worlds would settle it either way.
- **U4.** If `T` is kept on purpose, to show a world enclosed only late, U4 asks only that the equivalence be stated.
- **U5.** A constructive end step for settling counts would contradict Q5. Without LPO that is impossible, since Q5 proves the implication.

## Appendix A. Probe source

`review13/build/Review13.lean`: sha256 `08ff23259f272c30a4f54d76fa43100706b8678be9132208804a6d40edd011dd`, 362 lines. It compiles with `LEAN_PATH=<build> lean -o Review13.olean Review13.lean` against the `7f69f455` core and the draft oleans, and exits 0 with no output.

```lean
import Becoming
import D36

/-!
# Probes of the thirteenth independent review (P32–P34, drafts P35/P36)

Term mode throughout; no tactic blocks. The axiom audit is in `Review13Audit.lean`.

* Q1 `Balance`, `balance_not_tally`, `tally_iff`, `ceasing_bound_law`: the balance as an
  equation (`Listed.across`) is strictly weaker than a tally (`Listed.keeps`); the tally is
  the balance together with "no more cease across a step than are listed before it", which is
  a law of counting the equation does not give.
* Q2 `tally_congr`, `tally_iff_counted`: the counts listings can have are exactly the
  tallies, up to values at each step, stated with no `Pointwise` hypothesis.
* Q3 `since_le`, `since_zero_le`, `settles_zero`, `settles_iff_zero`, `same_laws`: settling
  from some step is settling from step 0 with a larger bound, so worlds enclosed from some step,
  worlds enclosed from step 0 and finite worlds have the same laws of counting under the eight
  premises (from the drafts' `enclosed_counting` and `finite_counting`).
* Q4 `tended_dissipation_idle`, `tended_not_binds`: in the tended queue dissipation never
  binds in the sense of `World.Binds` (nothing taking part ever takes from a closed family),
  and neither does activity needing support.
* Q5 `FirstChange.*`, `SettlesEnds`, `lpo_of_settlesEnds`, `FiniteEnds`, `lpo_of_finiteEnds`:
  a tally that settles from step 0, with nothing joining an empty queue, whose only change is at
  the first `true` of a Boolean sequence; an end step for change in every settling count, or an
  end step for arising in every finite world meeting the eight premises, implies LPO.
* Q6 `OneSwap.*`, `closed_dissipation_binds`: in the drafts' finite world, dissipation binds.
* Q7 `binds_arising`, `binds_adds`: where every premise binds (`World.Binds`), every census
  counts some arising, which is no law under the eight premises alone.
* Q8: the P30 names after P33b, and the drafts' arithmetic beside the core's.
-/

namespace Review13

open Becoming

/-! ## Q1. The balance equation is not the whole law of counting -/

/-- The census balance across each step, as `Listed.across` states it. -/
def Balance (n c a : Nat → Nat) : Prop :=
  ∀ t, n (t + 1) + c t = n t + a t

theorem tally_balance {n c a : Nat → Nat} (tally : Tally n c a) : Balance n c a := fun t =>
  match tally t with
  | ⟨k, before, after⟩ => (congrArg (· + c t) after).trans
      ((Nat.add_right_comm k (a t) (c t)).trans (congrArg (· + a t) before.symm))

theorem tally_le {n c a : Nat → Nat} (tally : Tally n c a) (t : Nat) : c t ≤ n t :=
  match tally t with
  | ⟨k, before, _⟩ => Nat.le_trans (Nat.le_add_left (c t) k) (Nat.le_of_eq before.symm)

theorem tally_of_balance {n c a : Nat → Nat} (balance : Balance n c a)
    (bounded : ∀ t, c t ≤ n t) : Tally n c a := fun t =>
  match le_dest (bounded t) with
  | ⟨k, same⟩ => ⟨k, same.trans (Nat.add_comm (c t) k),
      add_right_cancel (c t) ((balance t).trans ((congrArg (· + a t)
        (same.trans (Nat.add_comm (c t) k))).trans (Nat.add_right_comm k (c t) (a t))))⟩

/-- A tally is exactly the balance with no more ceasing across a step than were listed. -/
theorem tally_iff {n c a : Nat → Nat} : Tally n c a ↔ Balance n c a ∧ ∀ t, c t ≤ n t :=
  ⟨fun tally => ⟨tally_balance tally, tally_le tally⟩,
   fun ⟨balance, bounded⟩ => tally_of_balance balance bounded⟩

/-- None listed, one ceasing and one coming at every step: the equation holds, the tally
does not. -/
theorem balance_not_tally :
    Balance (fun _ => 0) (fun _ => 1) (fun _ => 1) ∧ ¬ Tally (fun _ => 0) (fun _ => 1) (fun _ => 1) :=
  ⟨fun _ => rfl, fun tally => Nat.not_succ_le_zero 0 (tally_le tally 0)⟩

/-- "No more cease than were listed" holds of every listing, and does not follow from the
balance equation. -/
theorem ceasing_bound_law :
    (∀ (α : Type) (p : α → Nat → Prop) [∀ x t, Decidable (p x t)] (l : Nat → List α),
      Listed p l → ∀ t, ceasings (l t) p t ≤ (l t).length) ∧
    ¬ ∀ n c a : Nat → Nat, Balance n c a → ∀ t, c t ≤ n t :=
  ⟨fun _ _ _ _ listed t => tally_le listed.tally t,
   fun law => Nat.not_succ_le_zero 0 (law _ _ _ balance_not_tally.1 0)⟩

/-! ## Q2. The characterization without `Pointwise` -/

/-- Tallies respect the counts' values at each step. -/
theorem tally_congr {n c a n' c' a' : Nat → Nat}
    (same : ∀ t, n t = n' t ∧ c t = c' t ∧ a t = a' t) (tally : Tally n c a) :
    Tally n' c' a' := fun t =>
  match tally t with
  | ⟨k, before, after⟩ =>
    ⟨k, (same t).1.symm.trans (before.trans (congrArg (k + ·) (same t).2.1)),
     (same (t + 1)).1.symm.trans (after.trans (congrArg (k + ·) (same t).2.2))⟩

/-- The counts some listing has are exactly the tallies: `counting_laws` without a
hypothesis on the property. -/
theorem tally_iff_counted (n c a : Nat → Nat) :
    Tally n c a ↔ ∃ (α : Type) (p : α → Nat → Prop) (_ : ∀ x t, Decidable (p x t))
      (l : Nat → List α), Listed p l ∧
        ∀ t, (l t).length = n t ∧ ceasings (l t) p t = c t ∧ comings (l (t + 1)) p t = a t :=
  ⟨fun tally => ⟨Nat, Queue.holds n c, fun _ _ => inferInstance, Queue.line n c, Queue.listed,
     Queue.counts tally⟩,
   fun ⟨_, _, _, _, listed, same⟩ => tally_congr same listed.tally⟩

/-! ## Q3. Settling from some step is settling from the first -/

theorem since_le {T : Nat} (q : Nat → Nat) : ∀ t, since T q t ≤ t
  | 0 => Nat.le_refl 0
  | t + 1 => Nat.add_le_add (since_le q t) (mark_le_one _)

theorem since_zero_le {T : Nat} (q : Nat → Nat) : ∀ t, since 0 q t ≤ since T q t + T
  | 0 => Nat.zero_le _
  | t + 1 => match Nat.lt_or_ge t T with
    | .inl early => Nat.le_trans (since_le q (t + 1)) (Nat.le_trans early (Nat.le_add_left T _))
    | .inr later => Nat.le_trans (Nat.le_of_eq (since_succ q (Nat.zero_le t)))
        (Nat.le_trans (Nat.add_le_add_right (since_zero_le q t) _)
          (Nat.le_of_eq ((Nat.add_right_comm _ T _).trans
            (congrArg (· + T) (since_succ q later).symm))))

/-- Counts settling from step `T` within `B` settle from step 0 within `B + T` and the counts
before `T`. -/
theorem settles_zero {n c a : Nat → Nat} {T B : Nat} (settles : Settles T B n c a) :
    Settles 0 (B + T + total (steps 0 T) n) n c a := fun t _ =>
  match Nat.lt_or_ge t T with
  | .inl early => Nat.le_trans
      (Nat.add_le_add (le_total_of_mem (q := n) (steps_of_within (Nat.zero_le t)
        (Nat.lt_of_lt_of_le early (Nat.le_of_eq (Nat.zero_add T).symm))))
        (Nat.le_trans (since_le _ t) (Nat.le_of_lt early)))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
        (Nat.add_le_add_right (Nat.le_add_left T B) _))
  | .inr later => Nat.le_trans (Nat.add_le_add_left (since_zero_le _ t) _)
      (Nat.le_trans (Nat.le_of_eq (Nat.add_assoc _ _ _).symm)
        (Nat.le_trans (Nat.add_le_add_right (settles t later) T) (Nat.le_add_right _ _)))

theorem settles_iff_zero {n c a : Nat → Nat} :
    (∃ T B, Settles T B n c a) ↔ ∃ B, Settles 0 B n c a :=
  ⟨fun ⟨_, _, settles⟩ => ⟨_, settles_zero settles⟩, fun ⟨B, settles⟩ => ⟨0, B, settles⟩⟩

/-- Under the eight premises, worlds enclosed from some step and finite worlds have the same
laws of counting. -/
theorem same_laws {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
      w.CountsObey Q) :=
  ⟨fun law w _ premised finite => law w premised ⟨0, fun t _ => finite.enclosed t⟩,
   fun law => (World.enclosed_counting pointwise).mp fun n c a tally company settles =>
     (World.finite_counting pointwise).mpr law n c a tally company (settles_iff_zero.mp settles)⟩

/-! ## Q4. In the tended queue dissipation never binds -/

/-- Nothing taking part in the tended queue ever takes from a closed family: where something is
taken the front is active, and then it gives to a ground relatum beyond every finite family. -/
theorem tended_dissipation_idle {n c : Nat → Nat} :
    ¬ ∃ cs t f, Distinct cs ∧ (World.tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (World.tendedQueue n c).flow.present t ∧
      0 < total cs ((World.tendedQueue n c).flow.take t f) :=
  fun ⟨cs, t, f, _, closed, present, takes⟩ =>
    match total_pos cs takes with
    | ⟨x, _, positive⟩ =>
      have occupied : 0 < n t := match x, positive with
        | .member _, positive => Tended.occupied (mark_pos.mp positive).1
        | .ground _, positive => Tended.front.mp (mark_pos.mp positive)
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((mark_one (Tended.front.mpr occupied)).symm.trans
          (closed f present _ (Tended.outside cs)).2)))

/-- So in the witness of `premised_counting` neither dissipation nor activity needing support
binds. -/
theorem tended_not_binds {n c : Nat → Nat} :
    (¬ ∃ cs t f, Distinct cs ∧ (World.tendedQueue n c).flow.ClosedAt cs t ∧
      f ∈ (World.tendedQueue n c).flow.present t ∧
      0 < total cs ((World.tendedQueue n c).flow.take t f)) ∧
    (¬ ∃ t f x, (World.tendedQueue n c).web.active t f ∧
      (World.tendedQueue n c).web.requires t f x ∧ 0 < (World.tendedQueue n c).web.need t f x) ∧
    ¬ (World.tendedQueue n c).Binds :=
  ⟨tended_dissipation_idle, fun ⟨_, _, _, _, no, _⟩ => no,
   fun binds => tended_dissipation_idle binds.dissipative⟩

/-! ## Q5. An end step for settling change is omniscience -/

def ind : Bool → Nat
  | true => 1
  | false => 0

theorem ind_split : ∀ b d : Bool, ind (b && d) + ind (b && !d) = ind b
  | true, true => rfl
  | true, false => rfl
  | false, _ => rfl

theorem mark_double : ∀ b : Bool, mark (0 < ind b + ind b) = ind b
  | true => rfl
  | false => rfl

namespace FirstChange

variable (s : Nat → Bool)

/-- One member leaves and one joins across the step at the first `true` of `s`, and nothing
changes at any other step. -/
def change (t : Nat) : Nat :=
  ind (clear s t && s t)

/-- The steps with a change before `t`, with whether no `true` has come yet, are one. -/
theorem since_clear : ∀ t, since 0 (fun u => change s u + change s u) t + ind (clear s t) = 1
  | 0 => rfl
  | t + 1 => (congrArg (· + ind (clear s (t + 1)))
      ((since_succ _ (Nat.zero_le t)).trans (congrArg (_ + ·) (mark_double _)))).trans
      ((Nat.add_assoc _ _ _).trans
        ((congrArg (since 0 (fun u => change s u + change s u) t + ·)
          (ind_split (clear s t) (s t))).trans (since_clear t)))

theorem tally : Tally (fun _ => 1) (change s) (change s) := fun t =>
  match Clear.cases (clear s t && s t) with
  | .inl no => ⟨1, (congrArg (1 + ·) (congrArg ind no)).symm,
      (congrArg (1 + ·) (congrArg ind no)).symm⟩
  | .inr yes => ⟨0, (congrArg (0 + ·) (congrArg ind yes)).symm,
      (congrArg (0 + ·) (congrArg ind yes)).symm⟩

theorem company : ∀ t, 0 < change s t → 0 < (fun _ => 1) t :=
  fun _ _ => Nat.zero_lt_one

theorem settles : Settles 0 2 (fun _ => 1) (change s) (change s) := fun t _ =>
  Nat.add_le_add_left (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq (since_clear s t))) 1

theorem at_first {m : Nat} (c : clear s m = true) (yes : s m = true) :
    change s m + change s m = 2 :=
  congrArg (fun b => ind b + ind b) (Clear.and_both _ _ c yes)

/-- From the step of an end, decide `s`. -/
theorem decide_of_end {E : Nat} (quiet : ∀ m, E ≤ m → clear s m = true → s m = true → False) :
    (∃ n, s n = true) ∨ ∀ n, s n = false :=
  match Clear.or_first s E with
  | .inr ⟨m, _, _, yes⟩ => .inl ⟨m, yes⟩
  | .inl c => .inr fun k => Clear.false_of_not (s k) fun yes =>
    match Clear.first_of_true s yes with
    | ⟨m, cm, ym⟩ => match Nat.lt_or_ge m E with
      | .inl lt => Clear.not_both (Clear.false_before s c lt) ym
      | .inr ge => quiet m ge cm ym

end FirstChange

/-- Every count that settles from the first step, with nothing joining an empty queue, has a
step after which nothing changes. -/
def SettlesEnds : Prop :=
  ∀ n c a : Nat → Nat, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, Settles 0 B n c a) →
    ∃ E, ∀ t, E ≤ t → c t + a t = 0

theorem lpo_of_settlesEnds (ends : SettlesEnds) : LPO := fun s =>
  match ends _ _ _ (FirstChange.tally s) (FirstChange.company s) ⟨2, FirstChange.settles s⟩ with
  | ⟨E, quiet⟩ => FirstChange.decide_of_end s (E := E) fun m ge c yes =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_of_eq
      ((FirstChange.at_first s c yes).symm.trans (quiet m ge))))

/-- Every finite world meeting the eight premises, whose activity is decided, has a step
after which nothing arises. -/
def FiniteEnds : Prop :=
  ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
    ∃ E, ∀ t x, E ≤ t → ¬ w.web.Arises t x

theorem lpo_of_finiteEnds (ends : FiniteEnds) : LPO := fun s =>
  match ends (World.closedQueue (fun _ => 1) (FirstChange.change s) (FirstChange.change s) 2)
      (World.closedQueue_premised (FirstChange.tally s) (FirstChange.company s)
        (FirstChange.settles s))
      (World.closedQueue_finite _ _ _ _) with
  | ⟨E, quiet⟩ => FirstChange.decide_of_end s (E := E) fun m ge c yes =>
    have comes : 0 < comings (Closed.alive (fun _ => 1) (FirstChange.change s) 2 (m + 1))
        (fun x u => (World.closedQueue (fun _ => 1) (FirstChange.change s)
          (FirstChange.change s) 2).web.active u x) m :=
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((congrArg ind (Clear.and_both _ _ c yes)).symm.trans
          ((World.closedQueue_counts (FirstChange.tally s) (FirstChange.settles s) m).2.2.symm)))
    match total_pos _ comes with
    | ⟨x, _, arises⟩ => quiet m x ge (mark_pos.mp arises)

/-! ## Q6. In the drafts' finite world dissipation binds -/

namespace OneSwap

/-- One member, replaced across the first step. -/
def change : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

theorem tally : Tally (fun _ => 1) change change
  | 0 => ⟨0, rfl, rfl⟩
  | _ + 1 => ⟨1, rfl, rfl⟩

theorem since_one : ∀ t, since 0 (fun u => change u + change u) (t + 1) = 1
  | 0 => rfl
  | t + 1 => (since_succ _ (Nat.zero_le (t + 1))).trans (congrArg (· + 0) (since_one t))

theorem settles : Settles 0 2 (fun _ => 1) change change
  | 0, _ => Nat.le_succ 1
  | t + 1, _ => Nat.le_of_eq (congrArg (1 + ·) (since_one t))

abbrev world : World := World.closedQueue (fun _ => 1) change change 2

/-- Place 0 holds the front at the first step. -/
def zero : Fin (Closed.size 2) := ⟨0, Nat.succ_pos _⟩

/-- At the first step the front, standing at two, leaves, and the new member stands at one. -/
theorem takes : world.flow.take 0 (Closed.front change 2 0) zero = 2 := rfl

/-- `change_within`'s bound is attained: the total standing at step 0 is two, and from step 1
on one member is active with one change step behind it. -/
theorem attained : world.web.stock (Closed.alive (fun _ => 1) change 2 0) 0 = 2 ∧
    ∀ t, (Closed.alive (fun _ => 1) change 2 (t + 1)).length +
      since 0 (fun u => change u + change u) (t + 1) = 2 :=
  ⟨rfl, fun t => (congrArg (· + _) ((World.closedQueue_counts tally settles (t + 1)).1)).trans
    (congrArg (1 + ·) (since_one t))⟩

end OneSwap

/-- In the drafts' finite world dissipation binds: something taking part takes from a closed
family. -/
theorem closed_dissipation_binds :
    ∃ cs t f, Distinct cs ∧ OneSwap.world.flow.ClosedAt cs t ∧ f ∈ OneSwap.world.flow.present t ∧
      0 < total cs (OneSwap.world.flow.take t f) :=
  match World.closedQueue_finite (fun _ => 1) OneSwap.change OneSwap.change 2 with
  | ⟨all, distinct, every⟩ =>
    ⟨all, 0, Closed.front OneSwap.change 2 0, distinct,
     fun _ _ x out => absurd (every x) out, .head _,
     Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_trans (Nat.le_of_eq OneSwap.takes.symm)
       (le_total_of_mem (every OneSwap.zero)))⟩

/-! ## Q7. Where every premise binds, counting has a further law -/

/-- In a world in which every premise binds (`World.Binds`), every census counts an arising:
embodiment binds only where something arises. -/
theorem binds_arising (w : World) [∀ t x, Decidable (w.web.active t x)] (binds : w.Binds) :
    w.CountsObey fun _ _ a => ∃ t, 0 < a t := fun alive census =>
  match binds.embodied with
  | ⟨t, x, arises⟩ =>
    have mem : x ∈ alive (t + 1) := ((census (t + 1)).2 x).mp arises.2
    have one : 0 < mark (ComesToBe (fun s => w.web.active s x) t) := mark_pos.mpr arises
    ⟨t, Nat.lt_of_lt_of_le one
      (le_total_of_mem (q := fun y => mark (ComesToBe (fun s => w.web.active s y) t)) mem)⟩

theorem arising_pointwise : Pointwise fun _ _ a => ∃ t, 0 < a t :=
  fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2)⟩

/-- Under the eight premises "something arises" is no law of counting (the empty tally), but
it is one where every premise binds: `premised_counting` ranges over worlds in which some
premises may hold idly. -/
theorem binds_adds :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Binds →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t) ∧
    ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t :=
  ⟨binds_arising, fun law =>
    match (World.premised_counting arising_pointwise).mpr law (fun _ => 0) (fun _ => 0)
        (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩) (fun _ no => no) with
    | ⟨_, no⟩ => Nat.lt_irrefl 0 no⟩

/-! ## Q8. Names -/

example := @Becoming.World.slow_world
example := @Becoming.World.slow
example := @Becoming.Slow.census
example := @Becoming.Web.Census.balanceFrom
example := @Becoming.World.premised_counting
-- The drafts' arithmetic beside what the core already has.
example : ∀ {a b c : Nat}, a + b ≤ c → a ≤ c - b := @RelationalRenewal.le_sub_from_add
example : ∀ {a b c : Nat}, a + b ≤ c → a ≤ c - b := @Becoming.le_sub_of_add_le
example : ∀ {a b : Nat} (k : Nat), a + k = b + k → a = b := @Becoming.add_right_cancel

end Review13
```

## Appendix B. Probe axiom audit

`review13/build/Review13Audit.lean`: sha256 `f91a71703d451fe36d85dd715c9b5777f46b464eca1c029cdb329b8ed2f77264`, 70 lines. Its output is `review13/logs/Review13Audit.out`: sha256 `ea91f7b670f42045bbce42702031d6fec3c79021a132562957dfb819c8ea2106`, 56 lines.

```lean
import Lean
import Review13
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review13 | throwError "no module Review13"
  let mut count := 0
  let mut withAx := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then withAx := withAx.push (n, axioms)
  logInfo m!"MODULE Review13 CONSTANTS {count} WITH_AXIOMS {withAx.size} {withAx.toList}"
#print axioms Review13.Balance
#print axioms Review13.tally_balance
#print axioms Review13.tally_le
#print axioms Review13.tally_of_balance
#print axioms Review13.tally_iff
#print axioms Review13.balance_not_tally
#print axioms Review13.ceasing_bound_law
#print axioms Review13.tally_congr
#print axioms Review13.tally_iff_counted
#print axioms Review13.since_le
#print axioms Review13.since_zero_le
#print axioms Review13.settles_zero
#print axioms Review13.settles_iff_zero
#print axioms Review13.same_laws
#print axioms Review13.tended_dissipation_idle
#print axioms Review13.tended_not_binds
#print axioms Review13.ind
#print axioms Review13.ind_split
#print axioms Review13.mark_double
#print axioms Review13.FirstChange.change
#print axioms Review13.FirstChange.since_clear
#print axioms Review13.FirstChange.tally
#print axioms Review13.FirstChange.company
#print axioms Review13.FirstChange.settles
#print axioms Review13.FirstChange.at_first
#print axioms Review13.FirstChange.decide_of_end
#print axioms Review13.SettlesEnds
#print axioms Review13.lpo_of_settlesEnds
#print axioms Review13.FiniteEnds
#print axioms Review13.lpo_of_finiteEnds
#print axioms Review13.OneSwap.change
#print axioms Review13.OneSwap.tally
#print axioms Review13.OneSwap.since_one
#print axioms Review13.OneSwap.settles
#print axioms Review13.OneSwap.world
#print axioms Review13.OneSwap.zero
#print axioms Review13.OneSwap.takes
#print axioms Review13.OneSwap.attained
#print axioms Review13.closed_dissipation_binds
#print axioms Review13.binds_arising
#print axioms Review13.arising_pointwise
#print axioms Review13.binds_adds
#print axioms Nat.add_right_cancel
#print axioms Nat.sub_eq_zero_of_le
#print axioms Nat.add_sub_of_le
#print axioms Nat.le_sub_of_add_le
#print axioms Fin.eq_of_val_eq
#print axioms Nat.sub_add_cancel
#print axioms Nat.le.dest
#print axioms Nat.exists_eq_add_of_le
#print axioms Nat.succ_ne_zero
#print axioms Becoming.add_right_cancel
#print axioms Becoming.le_of_add_le_add_right
#print axioms RelationalRenewal.le_sub_from_add
#print axioms Becoming.le_dest
```

Output:

```text
MODULE Review13 CONSTANTS 78 WITH_AXIOMS 0 []
'Review13.Balance' does not depend on any axioms
'Review13.tally_balance' does not depend on any axioms
'Review13.tally_le' does not depend on any axioms
'Review13.tally_of_balance' does not depend on any axioms
'Review13.tally_iff' does not depend on any axioms
'Review13.balance_not_tally' does not depend on any axioms
'Review13.ceasing_bound_law' does not depend on any axioms
'Review13.tally_congr' does not depend on any axioms
'Review13.tally_iff_counted' does not depend on any axioms
'Review13.since_le' does not depend on any axioms
'Review13.since_zero_le' does not depend on any axioms
'Review13.settles_zero' does not depend on any axioms
'Review13.settles_iff_zero' does not depend on any axioms
'Review13.same_laws' does not depend on any axioms
'Review13.tended_dissipation_idle' does not depend on any axioms
'Review13.tended_not_binds' does not depend on any axioms
'Review13.ind' does not depend on any axioms
'Review13.ind_split' does not depend on any axioms
'Review13.mark_double' does not depend on any axioms
'Review13.FirstChange.change' does not depend on any axioms
'Review13.FirstChange.since_clear' does not depend on any axioms
'Review13.FirstChange.tally' does not depend on any axioms
'Review13.FirstChange.company' does not depend on any axioms
'Review13.FirstChange.settles' does not depend on any axioms
'Review13.FirstChange.at_first' does not depend on any axioms
'Review13.FirstChange.decide_of_end' does not depend on any axioms
'Review13.SettlesEnds' does not depend on any axioms
'Review13.lpo_of_settlesEnds' does not depend on any axioms
'Review13.FiniteEnds' does not depend on any axioms
'Review13.lpo_of_finiteEnds' does not depend on any axioms
'Review13.OneSwap.change' does not depend on any axioms
'Review13.OneSwap.tally' does not depend on any axioms
'Review13.OneSwap.since_one' does not depend on any axioms
'Review13.OneSwap.settles' does not depend on any axioms
'Review13.OneSwap.world' does not depend on any axioms
'Review13.OneSwap.zero' does not depend on any axioms
'Review13.OneSwap.takes' does not depend on any axioms
'Review13.OneSwap.attained' does not depend on any axioms
'Review13.closed_dissipation_binds' does not depend on any axioms
'Review13.binds_arising' does not depend on any axioms
'Review13.arising_pointwise' does not depend on any axioms
'Review13.binds_adds' does not depend on any axioms
'Nat.add_right_cancel' depends on axioms: [propext]
'Nat.sub_eq_zero_of_le' depends on axioms: [propext]
'Nat.add_sub_of_le' depends on axioms: [propext]
'Nat.le_sub_of_add_le' depends on axioms: [propext]
'Fin.eq_of_val_eq' does not depend on any axioms
'Nat.sub_add_cancel' depends on axioms: [propext]
'Nat.le.dest' does not depend on any axioms
'Nat.exists_eq_add_of_le' depends on axioms: [propext]
'Nat.succ_ne_zero' depends on axioms: [propext]
'Becoming.add_right_cancel' does not depend on any axioms
'Becoming.le_of_add_le_add_right' does not depend on any axioms
'RelationalRenewal.le_sub_from_add' does not depend on any axioms
'Becoming.le_dest' does not depend on any axioms
```

The 42 probe source declarations (34 theorems, 7 definitions, 1 abbreviation) and their 78 constants depend on no axiom. Among the reference lemmas, `Nat.add_right_cancel`, `Nat.sub_eq_zero_of_le`, `Nat.add_sub_of_le`, `Nat.le_sub_of_add_le`, `Nat.sub_add_cancel`, `Nat.exists_eq_add_of_le` and `Nat.succ_ne_zero` carry `propext`. `Fin.eq_of_val_eq`, `Nat.le.dest` and the core's own arithmetic lemmas do not, which is the basis of U6 and U7.
