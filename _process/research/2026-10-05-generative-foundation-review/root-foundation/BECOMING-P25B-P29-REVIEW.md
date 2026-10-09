# P25b 至 P29 的独立审查 / Independent review of P25b to P29

2026-10-10。审查者：Claude Opus 5.5，独立 agent，未参与撰写 P26、P27、P28、P25b 与 P29。对象：`main` 的 `0cf14b8b`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of P26, P27, P28, P25b or P29. Object: `main` at `0cf14b8b`.

**摘要（中文）。**

- **机械检查都对。**
  - 核心闭包的 29 个模块在仓库之外从前导重新编译，退出码为 0，没有警告。
  - 1830 条源声明（1126 项定理）的公理报告全部为空。
  - 闭包有 5153 个常量。依赖公理的只有 35 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同。比第十次审查多出的一条是 `World.Brood.Relatum.ground.injEq`。
  - 回执 `20261009T163512.365801Z`（包 27 个模块，1086 项定理，1760 项声明审计）的 42 个源哈希、检查器哈希和保留运行的 258 个产物都对。
  - 外围回执 `20261009T163805.366023Z` 的 33 个源哈希与 74 个产物都对。外围没有重建。
  - 自 `63437779` 起改动的 32 份记录中，394 个引用哈希与 111 个证明绑定都对。
  - 548 个别名中 507 个在核心中解析；其余 41 个与第十次审查相同。
  - 各阶段的定理数为 1016 → 1029 → 1045 → 1061 → 1077 → 1086，与研究、计划和章节一致。
  - 每份记录的时间戳都不晚于其提交。
- **数学被接受。**
  - 下列结果在 Lean 中都对：P26 的普查定律与静止定理，P27 的有界普查定律，P28 的普查平衡，P25b 的新声明，P29 的 `World.Binds` 与 `brood`。没有发现错误的 Lean 陈述。
  - 本审查写了 47 条探针声明（32 项定理）。生成的 159 个常量都不依赖任何公理。
- **问题共十一项（R1–R11）**：两项散文中的错误，六项过强（其中一项缺少反例），三项表述与出处。最严重的是 R1、R2 与 R3。
  - **R1（错误；措辞来自第十次审查的 O10 与 Q8）。** “活动需要支持时，对持续不变的依存的每次侵蚀都与依存者的终结同时”不成立。
    - `Web.Dependent.inactive_below` 只给出依存者在该步之后不活跃。依存者此前就不活跃时，没有终结。
    - 探针 sleeper 是一个有限、平衡、每个关系项都体现、活动需要支持的世界。其中一次侵蚀使事件不活，而整个世界没有任何止息。
    - 这句话出现在 Roles、Space、README、检查器、章节第 10 条、§8 新增的 Ren 选择项、§9、一份记录与研究中，并决定了那个选择项的范围。
  - **R2（错误）。** 研究 §38 与英文 P25b 说，`law_decides` 的逆命题需要选择公理，在纯净核心中不能陈述。逆命题可以陈述；以排中律为假设，不用可判定性与选择也能证明（探针 `law_iff_em`，无公理）。
  - **R3（过强）。** P29 中普查起约束的条件是“世界不有限”（`Binds.counted`）。
    - 在 `brood` 中，这一条件由无限多个闲置的地关系项满足：它们从不立着、从不活跃、从不参与交换，也没有谁依存或汲取它们。
    - `brood` 的普查来自只有三个关系项曾经活跃（`brood_counted_ever`）。
    - 更一般地，在静止定理适用的每个世界中，曾经活跃的和曾经立着的都不是无界多（`rest_few`）。
    - 所以“普查不来自有限”只对整个世界是否有限成立。静止定理比 `rests` 多涵盖的世界，只多出从不立着、从不活跃的关系项。
- **其余各项。**
  - R4：记录 continued-change-needs-openness 的标题漏掉活动的普查，`dusk` 反驳它。
  - R5：P27 重新引入了“生成不息恰当止息复现”（O7 的残留）。
  - R6（缺少反例）：有界定律只需要界在无限多步上成立（`ceasing_of_coming_often`）。任何不减且趋于无穷的计数都允许只生不灭（`paced_world`），所以记录中“对数增长”的开放项已有答案。
  - R7：`Finite.countedWithin` 的说明“每个普查”比它的陈述强。
  - R8：开放加上八个前提并不给出生起不息（`holding`）。
  - R9：Ren 的“不overlap吧”有三种写法；Ren 确认的是英文的 arising/ceasing；Ren 回复时的语境没有写出。
  - R10：核心中有两个不同的 brood。
  - R11：依存的平衡、计数行等记账问题。
- **O1–O11 的处理。**
  - O2–O6 与 O9 关闭。
  - O1 关闭，但记录标题有残留（R4）。
  - O7 与 O8 部分关闭（R5、R9）。
  - O10 的处理沿用了第十次审查过强的那句话（R1）。
  - O11 关闭，只是 (a) 的新说明本身有误（R2）。

**Summary (English).**

- **The mechanical checks are clean.**
  - The 29 modules of the core closure recompile from the prelude outside the repository, with exit 0 and no warnings.
  - All 1830 of their source declarations (1126 theorems) have empty axiom reports.
  - The closure has 5153 constants. The only ones depending on an axiom are 35 compiler-generated `injEq` lemmas, each depending only on `propext`, exactly as the receipt lists. The one added since the tenth review is `World.Brood.Relatum.ground.injEq`.
  - The receipt `20261009T163512.365801Z` (package of 27 modules, 1086 theorems, 1760 declaration audits) is correct: its 42 source hashes, checker hashes and the 258 artifacts of its retained run all match.
  - The periphery receipt `20261009T163805.366023Z` has 33 source hashes and 74 artifacts, all matching. The periphery was not rebuilt.
  - The 32 records changed since `63437779` have 394 reference hashes and 111 proof bindings, all correct.
  - Of their 548 aliases, 507 resolve in the core; the other 41 are the same 41 as at the tenth review.
  - Theorem counts run 1016 → 1029 → 1045 → 1061 → 1077 → 1086 across the phases, as the study, plan and chapter say.
  - Every record stamp is at or before its commit.
- **The mathematics is accepted.**
  - These results are correct in Lean: the census law and the rest theorem (P26), the bounded census law (P27), the census balance (P28), the new declarations of P25b, and `World.Binds` and `brood` (P29). No Lean statement was found to be wrong.
  - This review wrote 47 probe declarations (32 theorems). None of the 159 constants they generate depends on any axiom.
- **Eleven findings (R1–R11)**: two errors in prose, six overclaims (one of them a missing counterexample), and three items of presentation and provenance. R1, R2 and R3 are the most serious.
  - **R1 (error; the wording comes from the tenth review's O10 and Q8).** "Where activity needs support, every undermining of a dependence persisting unchanged co-occurs with the ending of the relatum depending" is false.
    - `Web.Dependent.inactive_below` gives only that the relatum depending is not active after the step. If it was not active before, nothing ends.
    - In the probe `sleeper`, a finite, balanced world with every relatum embodied and activity needing support, an undermining makes an event not living while nothing in the world ever ceases.
    - The sentence appears in `Roles`, `Space`, the README, the checker, chapter item 10, the new Ren's choice in §8, §9, a record and the study. It sets the scope of that choice.
  - **R2 (error).** Study §38 and the English P25b paragraph say that the converse of `law_decides` needs choice and cannot be stated in the pure core. It can be stated, and with excluded middle as a hypothesis it is proved with neither decidability nor choice (probe `law_iff_em`, axiom-free).
  - **R3 (overclaim).** P29 takes "the world is not finite" as what it is for a census to bind (`Binds.counted`).
    - In `brood` this condition is met by infinitely many idle ground relata: they never stand, are never active, never take part in exchange, and nothing depends on them or draws on them.
    - `brood`'s census comes from only three relata ever being active (`brood_counted_ever`).
    - More generally, in every world to which the rest theorem applies, not unboundedly many relata are ever active or ever stand (`rest_few`).
    - So "the census does not come from finiteness" is true only of whether the whole world is finite. The worlds the rest theorem covers beyond `rests` differ from finite ones only by relata that never stand or act.
- **The remaining findings.**
  - R4: the record title of continued-change-needs-openness omits the census of activity, and `dusk` refutes it.
  - R5: P27 reintroduced "generation is unceasing exactly when ceasing recurs", a residue of O7.
  - R6 (missing counterexample): the bounded law needs its bound only at infinitely many steps (`ceasing_of_coming_often`). Any nondecreasing count tending to infinity allows arising without ceasing (`paced_world`), so the record's open question about logarithmic growth is answered.
  - R7: the gloss "every census" of `Finite.countedWithin` claims more than its statement.
  - R8: openness together with the eight premises does not give arising without end (`holding`).
  - R9: Ren's "不overlap吧" is rendered three ways; what Ren confirmed is the English pair arising/ceasing; and the context of Ren's reply is not recorded.
  - R10: two different worlds named brood are in the core.
  - R11: bookkeeping, including the dependence reading of the balance and missing count lines.
- **Handling of O1–O11.**
  - O2–O6 and O9 are closed.
  - O1 is closed, with a residue in a record title (R4).
  - O7 and O8 are partly closed (R5, R9).
  - The handling of O10 carries over an overstatement from the tenth review itself (R1).
  - O11 is closed, except that its new gloss for (a) is itself wrong (R2).

## 0. Scope, materials and method

**Object.** The object is `main` at `0cf14b8be6a05f886157e0e0e6dd5e8a5c04017a`, through five commits (all times UTC):

- **P26 (`f1ef72d2`, 14:06:22Z).** Ceasing needs arising, and the rest theorem: `Listed`-based census law in `Population`, `World.arising_of_ceasing`, `census_one_way`, `comes_to_rest`, `Finite.standing`, `Finite.comes_to_rest`, `rest_needs_census`, `rests_around`. Study §35; record ceasing-needs-arising.
- **P27 (`439d18bc`, 14:24:18Z).** The census law for any listed determination, and the bounded law: `Listed.*`, `Web.ceasing_of_arising`, `Web.unceasing_iff_bounded`, `World.CountedWithin`, `Finite.countedWithin`, `procession_world`, `dawn_unbounded`, `StandingCensus.coming_iff_ceasing`, `DependenceCensus.*`. Study §36; record bounded-census-keeps-pace.
- **P28 (`24ab3973`, 14:38:16Z).** The census balance: `Listed.across`, `over_stretch`, `ceasings_within`, `comings_within`, `Web.Census.over_stretch`, `StandingCensus.over_stretch`. Study §37; record census-balance.
- **P25b (`ae839e3b`, 16:34:56Z).** Integration of the tenth review: the changes to `Dissipation`, `Roles`, `Space`, `Premises`, `Openness`, `Change`, `Evolution` and the root module; study §38; the in-place corrections to §26, §30 and §32–§37; the English P25b paragraph; the chapter; foundation row 5; the plan; the checker's `SCOPE`; the periphery checker's `LEAN_TIMEOUT`.
- **P29 (`0cf14b8b`, 16:46:36Z).** `World.Binds`, `World.Brood`, `brood`, `brood_balanced`, `brood_dissipative`, `brood_counted`, `brood_binds`, `brood_rests`. Also the source file [2026-10-09-arising-ceasing-names](../../../../sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md), study §39 and the English P29 paragraph, and the records that carry the name confirmation.

**Isolation.**

- The object was exported with `git archive 0cf14b8b` into the reviewer's scratch directory, and every file was read from there.
- Commit stamps, diffs and per-commit receipts were read from the live repository with read-only `git show`, `git diff` and `git log`. Nothing in the live repository or its `.git` was modified.
- No `make` target or repository checker was run, and all compilation happened in scratch.
- During the review, an unrelated Lean process belonging to another session (compiling `Becoming/Reserve.lean` in the live tree) was observed. It was not touched.
- Links here are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where the tenth review is filed.

**Materials** (sha256 prefixes at `0cf14b8b`; each equals the exported file):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` / plan `BECOMING-UNIFICATION-PLAN.md` | `16ff875adfba8d43` / `7ba8ea95d0f19f56` |
| chapter `THE-THEORY-OF-BECOMING.md` / `BECOMING-FOUNDATION.md` / `CLAIMS.md` | `2a39d018ef054a74` / `bf6c17b0e21f77d5` / `4913cfea848b1b3b` |
| tenth review `BECOMING-P23C-P24-P25-REVIEW.md` | `71f1ff8e0ec97b4e` |
| receipt `becoming-verification.json` / `check_becoming.py` | `25b8905cbfb9981b` / `b3bff61f4ed1b03e` |
| periphery receipt `correction-inquiry-verification.json` | `b261f387aa4c1d7c` |
| `Becoming.lean` / package `README.md` | `11aac35e80f9b05f` / `8ad4632ba573379e` |
| `Becoming/Population` / `Openness` / `Premises` | `581fd437896566b6` / `8b5190eec61870d5` / `27ed9136b28e604a` |
| `Becoming/Space` / `Roles` / `Dissipation` / `Change` | `6f2da9247609c54f` / `d55d6e19e755b923` / `f079e8b4e85babc6` / `f37088ca49d10ceb` |
| records ceasing-needs-arising / bounded-census-keeps-pace / census-balance | `67630fe0f871404c` / `210a6c841b1be466` / `42da6ec1426c1d04` |
| records continued-change-needs-openness / map-of-premises | `9e755c1ddc8f703b` / `0018c2b37cd9077e` |
| records space-and-its-parts / coming-and-ceasing-keep-pace | `2b49f053cdceab99` / `cae8cedb7624e07b` |

**Read in full.**

- AGENTS.md and the tenth review.
- `Population` §§ on `Listed`, censuses and dependence (lines 1–40 and 280–560), `Openness` in full, `Premises` lines 1–75 and 700–973, and the P25b diffs of `Roles`, `Space`, `Dissipation` and `Change`.
- Study §35–§39 and the English P25–P29 paragraphs.
- The JSON of the five P26–P29 records and continued-change-needs-openness.
- The chapter items 3, 4 and 10 (zh and en), §2 (lines 215 and 219), §8 (lines 495–545), §9 and the glossary (lines 693–700).
- Foundation row 5, plan rows 244–248 and 268–276, and the P29 rows of CLAIMS.

**Read in part.**

- These definitions: `Web`, `Supported`, `Dependent`, `MetAbove`, `UnderminingOn`, `Living`, `Flow`, `Balances`, `Acting`, `Taking`, `ClosedAt`, `DissipatesOn`, `Dissipative`, `Enclosed`, `AroundStanding`, `StandingCensus`, `Census`, `Listed`, `Distinct`, `Arises`, `Ceases`, `ComesToBe`, `CeasesToBe`, `ComesToStand`, `DescendsAt`, `TransmitsWithin`, `Premised`, `Exposed`, `Dawn`, `Dusk`, `Procession`.
- The older `Brood` world in `Roles` (lines 900–1002).

**Ren's words read**, for provenance:

| Source | sha256 prefix |
|---|---|
| [arising/ceasing names](../../../../sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md) | `9643bf25025de149` |
| [renewing and consuming without axioms](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md) | `a12a64304d9cb974` |

**No external literature was read.**

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order, one process at a time.

- **Core.** All 29 modules of the receipt's `core_closure` exit 0 from the prelude with no warnings. The only output is the modules' own `#print axioms` lines in `GenerativeCore` (18) and `InquirySufficiency` (17), each reporting no axioms.
  - `GenerativeCore` is compiled with its `import Std` line removed, as the checker does; otherwise it is byte-identical.
  - `InquirySufficiency`, `RelationalRenewal`, `Becoming/*` and the root module `Becoming` are byte-identical to the object.
- **Bridge and periphery.** Not rebuilt; their bytes match the receipts.

**Checks.**

- **Receipt.**
  - Status `passed`, `core_compiles_from_prelude: true` and `source_unchanged_during_check: true`; `core_closure` has 29 modules and `spine` has 27.
  - All 42 `source_sha256` entries equal the object's files, and both checker hashes match (`check_becoming.py`, `check.py`).
  - The 258 artifacts of `becoming-checks/20261009T163512.365801Z` match their hashes, and its `verification.json` is byte-identical to the receipt.
- **Periphery receipt.**
  - `20261009T163805.366023Z` (`passed`, Lean `v4.30.0-rc2`): its 33 source hashes, its three checker hashes and its 74 artifacts match.
  - The two timed-out runs that P25b retains (`20261009T145404.970266Z`, `20261009T151818.075474Z`) are `failed` with a timeout, as disclosed.
  - `LEAN_TIMEOUT` (default 900) is read at `check_correction_inquiry.py:34`, as the commit message says.
- **Counts.**
  - Per receipt, the package goes 1016 (P23c) → 1029 (P26) → 1045 (P27) → 1061 (P28) → 1077 (P25b) → 1086 (P29) theorems, and 1662 → 1676 → 1697 → 1716 → 1739 → 1760 declaration audits.
  - Study §35–§39 and the English P26–P29 paragraphs state these numbers.
  - Every per-module count in chapter §9 equals the receipt (Population 63, Openness 49, Premises 45, Space 49, Roles 135, Dissipation 90, Change 42).
  - The closure has 1830 source declarations (1126 theorems).
- **Records.**
  - The 32 records changed in `63437779..0cf14b8b` carry 394 `references` hashes, all equal to the object's files.
  - All 111 proof bindings resolve their JSON pointers to the bound sources' hashes and to `passed`.
- **Names.**
  - `Names11.lean` (`e7b999eb48e74357…`) checks `env.contains` on the 548 aliases of those records. 507 resolve in the core. The other 41 are the same 41 as at the tenth review: 26 in `Becoming.Bridge`, 5 in the `CorrectionInquiry` periphery, and 10 in the inherited `deeper/` modules (`BecomingCompatibility` 4, `OperativeCoherence` 6), located here by their definitions in the exported sources.
  - The same file checks the 1503 declaration names listed in the records' `references`. 1419 resolve, and none of the 84 that do not is a core declaration.
  - Every P26–P29 and P25b declaration resolves.
- **Axioms.**
  - `CoreAudit.lean` (`e11246d4f9690c97…`) is `import Becoming` with 1830 `#print axioms` lines generated from the receipt. All 1830 report "does not depend on any axioms".
  - `EnvAudit.lean` (`420f85b14528ce05…`, the checker's environment audit instantiated for the closure; byte-identical to the tenth review's) enumerates every constant with `Lean.collectAxioms`.
    - The per-module counts equal the receipt's `core_closure_constants` (5153 in all; Population 206, Dissipation 324, Roles 464, Space 243, Premises 339, Openness 164).
    - Exactly 35 constants depend on an axiom. All are generated `injEq` lemmas, all depend only on `propext`, and their names equal the receipt's `generated_axiom_dependencies` (Appendix C).
- **Stamps.** In each of the five commits, every changed record's `reviewed_at_utc` is at or before the commit time. The latest are 16:38:21Z at P29, committed at 16:46:36Z. The P25b receipt (14:50:10Z) precedes its records (15:23:01Z) and its commit.

**Probes.**

- One file, `Review11.lean` (`16142d92675bbd83…`, 507 lines), imports the unchanged `Becoming` and compiles with exit 0 and no warnings.
- It has 47 source declarations: 32 theorems, 13 definitions, 1 instance and 1 inductive type, in six groups S1–S6.
- It is term mode only: no tactic and no `sorry`. The `if h : … then … else …` and `▸` it uses are term-level.
- The probes are small worlds that satisfy the published definitions unchanged, or theorems over those definitions.
- Following the nondual method, they show what the definitions admit, not what actual systems do. A probe refutes a sentence only where the sentence claims more than the definitions give.

| Probe | Shows | Finding |
|---|---|---|
| S1 `s1_sleeper`, `s1_inactive_below` | a finite, balanced world, every relatum embodied, activity needing support; the drawer's event undermines the seed's unchanged dependence and is not living; `inactive_below` applies; the seed is never active and nothing in the world ever ceases | R1 |
| S2 `few_of_quiet`, `rest_few`, `listed_of_ever`, `counted_of_ever`, `brood_ever`, `brood_counted_ever`, `brood_idle`, `brood_few` | where arising (or coming to stand) does not recur under a listing, not unboundedly many relata are ever active (or ever stand); so in every world to which the rest theorem applies, both are finite in this sense; conversely, finitely many ever active gives a census; `brood`'s census is that; its ground relata are idle | R3 |
| S3 `ceasing_of_coming_often`, `arising_iff_ceasing_often`, `paced_world` | a bound at infinitely many steps suffices for the bounded law; for every nondecreasing, unbounded count `g` a world with a census counting `g t` arises without end and never ceases | R6 |
| S4 `law_of_em`, `law_iff_em` | with excluded middle as a hypothesis, every finite world in which arising recurs has ceasing recurring, with no decidability; so the law `law_decides` assumes is equivalent to excluded middle, axiom-free | R2 |
| S5 `finite_census_bounded` | every census of a finite world is bounded by the number of its relata, with no decidability | R7 |
| S6 `s6_holding` | a world meeting all eight premises with no step enclosed in which nothing ever arises or ceases | R8 |

**Severity labels** are those of the ninth and tenth reviews:

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose says more than the Lean, including where a premise is left out or a reading is presented as settled.
- *missing counterexample*: a relevant witness is absent, or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

No Lean statement is wrong. Both errors (R1, R2) are false sentences in prose. The Lean they cite, or would cite, is correct.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Build, axioms, receipt, hashes, bindings, names | **Correct.** 29 modules, 1830 empty axiom reports, 35 generated `injEq` on `propext` as listed, 42 + 33 source hashes, 258 + 74 artifacts, 394 reference hashes, 111 bindings, 507 of 548 aliases in the core (the rest non-core, as before). | — |
| 2. P26: the census law (`Listed.coming_of_ceasing`, `comes_or_held`, `comes_or_fewer`, `comes_within`) and its readings | **Correct**, with hypotheses in the signatures (listing; decided determination). `census_one_way` is the right witness pair. | — |
| 3. P26: the rest theorem (`arising_stops`, `comes_to_rest`, `Finite.standing`, `Finite.comes_to_rest`, `rests_around`, `rests_enclosed`, `rest_needs_census`, `rest_needs_standing`) | **Correct.** Both censuses are needed, as shown. Every world it applies to has only finitely many relata ever active and ever standing (`rest_few`), so the generalization beyond `rests` adds only relata that never stand or act. The record title still omits the census of activity. | R3, R4 |
| 4. P27: the bounded law (`ceases_or_kept`, `ceases_or_more`, `ceases_within`, `ceasing_of_coming`, `coming_iff_ceasing`, `CountedWithin.arising_iff_ceasing`, `procession_world`, `dawn_unbounded`) | **Correct.** The bound is needed only at infinitely many steps, and the record's open question has a complete answer. The web-level docstrings and the record reintroduce O7's wording. `Finite.countedWithin` is glossed as "every census" but states that some census is bounded. | R5, R6, R7 |
| 5. P28: the census balance (`Listed.across`, `over_stretch`, `ceasings_within`, `comings_within`, `marks_le_of_sub`, `balance_over_stretch`) | **Correct.** The balance is an exact count of kept, ceased and new members. "Of dependence alike" is said in the chapter and plan, while the record lists it as a next step and no instance is stated. | R11 |
| 6. P25b: are O1–O11 fixed everywhere, zh and en? | **Mostly.** See the table below. | R1, R2, R4, R5, R9 |
| 7. P25b: new declarations (`Enclosed.around_not_not`, `aroundStanding_not_not`, `stills` with `¬¬`, `acting_across`, `draining_but`, `Dependent.inactive_below`, `grazing_decided`, `grazing_browser_ends`, `living_crosses_ceasing`, `exposed_standing`, `openness_contingent`, `rest_needs_standing`) | **Correct as stated.** The prose drawn from `inactive_below` says more than it gives. | R1 |
| 8. P29: is `Binds` fair or gerrymandered? | **Fair as non-vacuity for seven premises; the census field is of another kind.** It asks that the world not be finite, which idle relata satisfy. In a world that comes to rest, no census can bind in a stronger sense (`rest_few`). | R3 |
| 9. P29: hidden vacuities in `brood` | **Three.** The ground relata are idle (`brood_idle`). Activity needing support is never tight: the food never falls below the need. The flow takes part at step 0 only; that it takes part at only finitely many steps the rest theorem's premises appear to force (hand argument in R3). The name `Brood` is already taken in the core by a world of the opposite kind. | R3, R10 |
| 10. Ren's words and AI elaboration | **Quoted exactly in the chapter, plan §6 and the source file; rendered two other ways elsewhere.** The zh texts say Ren confirmed 生起与止息, while Ren wrote "arising/ceasing is indeed better name". The context of the reply is not carried into the canonical texts. | R9 |
| 11. Overclaims about what the theorems need | Rest needs both censuses (title), the bound needs only infinitely many steps, openness is necessary rather than sufficient, and the converse of `law_decides` is provable. | R2, R4, R6, R8 |

**Status of O1–O11.**

| Item | Status | Evidence |
|---|---|---|
| O1 | closed, one residue | Chapter item 4, §2, §8 row 510, glossary 699, foundation row 5, the module doc and study §33/§38 state finitely many standing and both censuses; `rest_needs_standing` is in the core. The record title of continued-change-needs-openness (and so CLAIMS row 38) omits the census of activity, and its correspondence equates "the two censuses" with "finitely many standing" (R4). |
| O2 | closed | `arising_stops`; `comes_to_rest` covers the hand argument; next_delta fields updated. |
| O3 | closed | `rests_enclosed` and `arising_opens` take no `DecidableEq`; `stills` takes `¬¬` enclosure. |
| O4 | closed | `openness_contingent`. The replacement sentence "a world meeting all eight with no step enclosed arises without end" (my predecessor's wording) reads generically and is false generically (R8). |
| O5 | closed | `exposed_standing`. |
| O6 | closed | Vacuities listed in the module doc, record and §33. |
| O7 | partly closed | `Change`, the root module, README, chapter §2/§9 and the §26 paragraph fixed. P27, written before P25b, reintroduced "generation is unceasing exactly when ceasing recurs" in `Population.lean:31` and `:535–537`, in the claim of bounded-census-keeps-pace (zh and en) and in study §36; the §26 table row (1632) and the English P19 paragraph (2557) keep it (R5). |
| O8 | partly closed | One status (a candidate for Ren) in the canonical texts; Ren quoted in the chapter and plan §6. `Space.lean:12–13` still renders the sentence as an assertion; four records and plan line 257 render it as an open question (R9). |
| O9 | closed | Decidability added, `acting_across`, `draining_but`, vacuity disclosed, "three of the eight", relativity to the eight. |
| O10 | handled, with a new error | `inactive_below`, `grazing_browser_ends`, `living_crosses_ceasing` and the new Ren's choice are in. The general sentence comes from the tenth review and is false (R1). |
| O11 | closed except (a) | (b)–(h) done; (i) disclosed as uncheckable. The gloss for (a) now carries a false claim about the converse (R2). |

## 2. Findings

R1 and R2 are errors, and R1–R3 are the most serious. R1 corrects the tenth review itself, whose O10 and Q8 introduced the sentence.

### R1. error (in prose; from the tenth review): not every undermining co-occurs with an ending

**Location.**

- `Roles.lean:50–54`, module doc: "so every undermining of a dependence that persists unchanged co-occurs with the ending of the formation depending". `Roles.lean:476–479`, the `Dependent.inactive_below` docstring, says the same.
- `Space.lean:688–690`, the `grazing_browser_ends` docstring: "as every undermining of a dependence persisting unchanged must where activity needs support".
- README rows `Roles` (line 39) and `Space` (line 42), in zh and en.
- `check_becoming.py:414–417` (`SCOPE`).
- Chapter item 10 (zh 88, en 120). §8, the new Ren's choice (zh 525, en 537): "活动需要支持时，对持续不变的依存的每次侵蚀都是这样的侵蚀". §9 Roles row (619).
- Record space-and-its-parts, claim (zh and en).
- Study §34 rebuttal 3, P25b mark (2104); §38.1 O10 row (2304); §38.2 Roles row (2312).
- **Origin.** Tenth review O10: "So in any world where activity needs support, every undermining of an unchanged dependence co-occurs with the ending of the relatum depending."

**What the Lean says.**

- `Web.Dependent.inactive_below` concludes `¬ W.active (t + 1) g`, from `Dependent`, `level (t+1) c < need t g c`, `requires (t+1) g c` and `need t g c ≤ need (t+1) g c`.
- `UnderminingOn t f c` asks that `f` draws on `c` and that some `g` with `requires t g c` met an earlier need (`MetAbove`) and is now below it. It does not ask that `g` be active at `t`. Neither does `MetAbove`.
- So the theorem gives an ending (`Ceases t g`) only when `g` was active at `t`. Where it was not, the undermining co-occurs with `g` staying inactive.

**Probe S1 (`s1_sleeper`).**

- The world has three relata: a drawer standing at one throughout, a seed standing at nothing, and soil standing at three and then one. Every relatum is active exactly while it stands.
- The seed depends on the soil at need two throughout. Across the first step the drawer takes two units of soil.
- The world is finite, balanced, every relatum is embodied, and activity needs support.
- `UnderminingOn 0 drawer soil` holds, so `¬ sleeper.Living`. The seed's dependence persists at the same need, and `inactive_below` applies (`s1_inactive_below`).
- Yet the seed is never active, and `∀ t x, ¬ Ceases t x`: nothing in the world ever ends.
- The seed reads naturally as a dormant dependence, such as a seed bank whose soil is depleted.

**Why it matters.**

- The sentence was used to scope a choice for Ren: "whether undermining that co-occurs with the ending of the relatum depending counts as not living". The text claims that under `Dependent` this choice covers every undermining of an unchanged dependence.
- It does not. Undermining of a dormant relatum's dependence co-occurs with no ending. Where Ren's choice concerns endings, it leaves such cases as `Living` already decides them: not living.
- `grazing_browser_ends` itself is correct, because the browser was active at step 0.

**Correction.**

- State the sentence with its premise: "the relatum depending is not active after the step; where it was active, this is its ending". Optionally, add to `Roles` the variant with `(active : W.active t g)` concluding `W.Ceases t g`.
- Widen the §8 item: "whether undermining that co-occurs with the relatum depending not being active after the step (its ending if it was active; a dormant dependence otherwise, `sleeper`) counts as not living, and for which drawers".
- Correct the README, `SCOPE`, the record and §38. Disclose that the overstatement came from the tenth review.

### R2. error (in prose): the converse of `law_decides` needs no choice and can be stated in the pure core

**Location.**

- Study §38.1, row O11 (2305): "逆命题需要从排中律得到可判定的数据，在纯净核心中不能陈述".
- §38.4 rebuttal 4 (2338): "需要把 `Q ∨ ¬Q` 变为可判定的数据，即 `Decidable`；从命题的析取消去到数据，在纯净核心中需要选择公理".
- English P25b (2671): "its converse needs choice to turn a disjunction into decidable data, so it cannot be stated in the pure core".

**What the Lean says, with probe S4.**

- The converse is a proposition: `(∀ Q, Q ∨ ¬ Q) → ∀ w, w.Finite → w.ArisingRecurs → w.CeasingRecurs`. It can be stated.
- It does not need `Decidable` data, because the proof can stay in `Prop`:
  - `push` turns `¬ CeasingRecurs` into a step `N` after which nothing ceases.
  - `stays` shows that what is active from `N` on stays active.
  - `arises_finitely` shows, by induction on the finite list of relata, that each relatum can arise at most once after `N`. It splits on excluded middle in `Prop`, with no `DecidableEq`.
  - `law_of_em` concludes.
- `law_iff_em : (∀ w, w.Finite → w.ArisingRecurs → w.CeasingRecurs) ↔ ∀ Q, Q ∨ ¬ Q` pairs this with the core's `law_decides`. All of these are axiom-free (Appendix B).

**Why it matters.**

- A false meta-claim about what the pure core can express is offered as the reason the gloss stays one-directional.
- With `law_iff_em`, the original gloss, "the law asked of every finite world without decidability is excluded middle", holds as an equivalence for the direction `law_decides` uses. The tenth review's O11(a) asked either to weaken the gloss or to state the converse. The converse is available.

**Correction.**

- Move `law_iff_em` into `Space`. It is about 70 lines, pure and term-mode.
- Then gloss: "asked of every finite world without decidability, the law is equivalent to excluded middle". Delete the "needs choice / cannot be stated" sentences in §38.1, §38.4 and the English P25b paragraph.
- The opposite direction (ceasing to arising) follows by the symmetric argument. This review did not formalize it.

### R3. overclaim: what the census binding and the rest theorem's generalization amount to

**Location.**

- `Premises.lean:40–43` (module doc), "Infinitely many ground relata stand at nothing, so the census does not come from finiteness". `:772–777` (`Binds` docstring): "a census where the world is not finite, so that the census does not come from finiteness".
- Chapter item 3 (zh 72, en 104), "所以普查不来自有限 / so the census does not come from finiteness".
- Record map-of-premises (claim) and plan row 248.
- Study §39, the 解读 bullet "普查起作用": "所以普查与所立者的普查都不来自有限；静止定理在其中起作用，而 `premised_rests` 不适用。这正是 §38 O1 的要点". Rebuttal 2 there. The English P29 paragraph: "so neither census comes from finiteness".
- Chapter item 4 (zh 76, en 108), §2 (215, 219) and foundation row 5. Each heads the rest theorem with "the world itself need not be finite". Foundation row 5 adds: "in one world, not finite, all eight hold, each binds, and it comes to rest".

**What the Lean says.**

- `Binds.counted` is `¬ w.Finite`. It is a property of the world, not an instance of the census condition, unlike the other seven fields, each of which exhibits the premise's condition being met.
- In `brood`, `¬ Finite` holds only through the ground relata. `brood_idle` shows that each ground relatum, at every step:
  - stands at nothing and is never active;
  - is never present in the flow;
  - is never taken from or given to;
  - is never required and never drawn on.
- `brood_ever` shows that only the food, the parent and the child are ever active. `counted_of_ever` (from `listed_of_ever`) builds a census from any such list. `brood_counted_ever` is `brood`'s census obtained this way. The census comes from finiteness: of what is ever active.
- This is not peculiar to `brood`. `few_of_quiet`: where what holds is listed at each step and coming to be does not recur, not every finite list misses a member holding at some step.
  - `few_active`: under a census, a world in which arising does not recur has not unboundedly many relata ever active.
  - `rest_few`: in every world to which `comes_to_rest` applies, not unboundedly many relata are ever active, and not unboundedly many ever stand. The second half uses `stills`.
- Hence, under the rest theorem's premises, a census binds at most as in `brood`, by the presence of relata that never stand or act. Rebuttal 2 of §39 says the census's content "is given by nothing else only when the world is not finite". Within these premises, it is given by finitely many relata ever being active.

**Why it matters.**

- The P25/P26 thesis, "the world need not be finite; what does the work is finitely many standing at each step", is formally true. The hypotheses are per step and easier to check than finiteness.
- But the worlds it covers beyond `rests` differ from finite worlds only by relata that never stand and are never active.
- The tenth review's §3 called the step from `rests` "a real generalization" without this qualification. That qualification now belongs with it.
- `brood` does not show that the census does work beyond finiteness. It shows that idle relata can be added to a finite resting world without disturbing the premises.

**Also, on `brood` and `Binds`.**

- **Activity needing support** binds by `Binds`' definition: the active parent depends on the food at need one. It is never tight, however. The food stands at three and then one, never below the need, so the premise excludes nothing in `brood`.
- **The four flow premises** bind at step 0 only. From step 1 on, `present = []`.
- That the flow takes part at only finitely many steps is not peculiar to `brood`; under the rest theorem's premises it appears forced. Under balance and dissipation, each step enclosed around what stands with someone taking from the enclosing family lowers the total standing by at least one (`standing_runs_down`). Giving there needs uptake (`acting_across`). With finitely many standing, this can happen at only finitely many steps from the step of enclosure on. That is a hand argument; this review did not formalize it.

**Correction.**

- Replace "so the census does not come from finiteness" with "the world is not finite, though only the food, the parent and the child are ever active; the ground relata are idle".
- Rename the field or gloss it as "the world is not finite (not: the census does work beyond finiteness)".
- Add `rest_few` (or `few_of_quiet`) to `Openness`, and qualify the headlines: "the world need not be finite; in a world that comes to rest under these premises, only finitely many relata ever stand or act, the others being inert".
- Correct study §39 ("普查起作用", rebuttal 2) and the English P29 paragraph.

### R4. overclaim (omitted premise; residue of O1): the record title of the rest theorem

**Location.**

- Record continued-change-needs-openness, title (zh, en): "a balanced, dissipative world with finitely many standing at each step, whose arising is embodied, comes to rest once enclosed, the world itself need not be finite". CLAIMS row 38 copies it.
- The record's correspondence: "what does the work is finitely many standing at each step (the two censuses)", and "so in an unfolding enclosed and with finitely many standing at each step, change happens only finitely often".
- The chapter item 4 and §2 headlines ("起作用的是每步立着的有限多，连同围住它们") omit the census of activity in the clause itself, though the same sentences go on to state it.

**What the Lean says.**

- `World.rest_needs_census` is a core theorem. `dusk` has a census of what stands (nothing stands), embodied arising, balance and dissipation, and every step enclosed around what stands. Ceasing recurs in it.
- So `dusk` meets every premise in the title and does not come to rest.
- The census of activity counts what is active, not what stands. Calling both "finitely many standing" conflates them.
- "Change happens only finitely often" holds of changes of standing (`stills`), not of activity (`dusk`).

**Correction.**

- Title: "… with finitely many standing and finitely many active at each step (censuses of both), whose arising is embodied, comes to rest once enclosed around what stands …".
- Correspondence: "finitely many standing and finitely many active at each step (the two censuses)", and "changes of standing happen only finitely often".
- In chapter item 4 and §2, write "每步立着的与活跃的有限多".

### R5. overclaim (residue of O7, reintroduced by P27): "generation is unceasing exactly when ceasing recurs"

**Location.**

- `Population.lean:29–31` (module doc): "under a census bounded from some step on generation is unceasing exactly when ceasing recurs (`Web.unceasing_iff_bounded`)".
- `Population.lean:535–537`, the `unceasing_iff_bounded` docstring: "generation is unceasing exactly when some formation ceases at arbitrarily late steps".
- Record bounded-census-keeps-pace, claim: zh "生成不息恰当止息复现", en "generation is unceasing exactly when ceasing recurs".
- Study §36 table (2193): "有界普查之下，生成不息恰当止息复现".
- Unchanged from before: the study §26 table row for `Web.unceasing_iff` (1632), "形成有限多时，生成不息恰当某个形成在任意晚的步止息", and the English P19 paragraph (2557), "With finitely many formations, generation is unceasing exactly when ceasing is".

**What the Lean says.**

- `Web.Unceasing` is "some formation arises at arbitrarily late steps".
- P25b corrected this wording in `Change`, the root module, the README, chapter §2 and §9 and the §26 paragraph, as O7 asked.
- P27 was written before P25b and repeated the old wording in new places. §38 says "§35–§37 … 中受影响的句子一并更正", but these four were missed.

**Correction.** Write "arising recurs exactly when ceasing recurs" (生起复现恰当止息复现) in all six places. Mark the §26 table and P19 edits in place.

### R6. missing counterexample and overclaim: the bound is needed only at infinitely many steps, and the open question about growth is answered

**Location.**

- Record bounded-census-keeps-pace:
  - correspondence: the "three tiers by counting", "finite at each step but unbounded, ceasing needs arising and not conversely";
  - limitations: "The bound must hold uniformly at every step from some step on; it fails where the bound grows with the steps";
  - next_delta: "What remains where the bound grows slowly with the steps (for instance, whether arising without ceasing is still possible under logarithmic growth)".
- Chapter item 4 (76, 108): "所需的是计数的界 / What this needs is a bound on the count".
- Chapter §2 (215, 219): "须同时活跃者无界 / only where the count of the active is unbounded".

**What the Lean says, with probe S3.**

- **The bound is needed only at infinitely many steps.**
  - `grows`: if coming to be recurs, then for each `k`, from some step on, either something has ceased since `N` or the list is longer than at `N` by `k`.
  - `ceasing_of_coming_often`: where at arbitrarily late steps at most `B` are listed, coming to be recurring needs ceasing to be recurring.
  - `arising_iff_ceasing_often`: under a census with at most `B` active at arbitrarily late steps, arising recurs exactly when ceasing does.
  - This strictly extends `Listed.ceasing_of_coming`. For example, a world in which nothing is active at even steps and relata `0, …, n` at step `2n + 1` meets the new premise but no bound from some step on. This example is a hand example, not formalized.
- **Any unbounded pace allows arising without ceasing.**
  - `paced_world g`: for every count `g` that never falls and later exceeds each of its values (`g t ≤ g (t+1)` and `∀ N, ∃ d, g N < g (N + d)`), relatum `k` active from the step at which `g` first exceeds `k` gives a census counting `g t` at step `t`. In this world arising recurs and nothing ever ceases.
  - Logarithmic growth is a case. `dawn` is the case `g t = t`.
- **Together, the boundary is sharp.** Where nothing ceases from some step on, the count is nondecreasing from there. Arising recurring then forces the count to infinity, which the bound at infinitely many steps forbids. Conversely, every nondecreasing count tending to infinity is realized by `paced_world`.
  - So under a census, arising without ceasing is possible exactly for counts that are nondecreasing from some step on and tend to infinity.
  - Ceasing without arising is impossible under any census (P26).

**Why it matters.** The record's three tiers are cut by whether the count is bounded. The relevant quantity is whether the count tends to infinity, that is, whether it stays bounded at infinitely many steps. The open question in next_delta is answered by the two probes.

**Correction.**

- Add `ceasing_of_coming_often` (Listed, activity, standing) and `paced_world` to the core.
- Restate the tiers:
  - count bounded at infinitely many steps: the two recur together;
  - count tending to infinity: ceasing needs arising, and not conversely, at any nondecreasing pace (`paced_world`);
  - no census: ceasing can recur alone (`dusk`).
- Replace next_delta with this answer. In chapter item 4 write "a bound on the count at infinitely many steps". In §2 write "only where the count of the active tends to infinity".

### R7. overclaim (docstring stronger than statement): "every census of a finite world is bounded"

**Location.**

- The `Openness.lean:260` docstring, "Every census of a finite world counts within the number of its relata". `Openness.lean:31–32` (module doc).
- Record bounded-census-keeps-pace, claim: "every census of a finite world is bounded (World.Finite.countedWithin)". Hypotheses: "Finite.countedWithin needs decided activity".

**What the Lean says.**

- `World.Finite.countedWithin` proves `∃ B, w.CountedWithin B`, that is, some census is bounded. It needs `[∀ t x, Decidable (w.web.active t x)]` to build that census.
- The universal form holds with no decidability (S5, `finite_census_bounded`): `w.Finite → ∃ B, ∀ alive, w.web.Census alive → ∀ t, (alive t).length ≤ B`.

**Correction.** State the universal form in the core, or gloss `Finite.countedWithin` as "a finite world whose activity is decided has a bounded census". Drop "needs decided activity" from the universal reading.

### R8. overclaim (generic reading): openness with the eight premises does not give arising without end

**Location.**

- Chapter item 4: zh 76 "满足它们而没有一步被围住的世界以零净量交换、生起不息"; en 108 "a world meeting them with no step enclosed exchanges at zero net and keeps arising".
- §8 row 510: "满足全部八个前提而没有一步被围住的世界生起不息".
- Foundation row 5: "a world meeting all eight with no step enclosed arises without end".
- Plan line 270 (English P25): "a world meeting all eight premises with no step enclosed keeps arising".
- The wording follows the tenth review's O4 correction, which had the same ambiguity.

**Probe S6 (`s6_holding`).**

- One holder stands at one throughout and, at every step, takes a unit from each of infinitely many ground relata and gives it back.
- The world meets all eight premises, and no step is enclosed. Nothing ever arises or ceases, and the world is not finite.
- So openness is, under a census with every relatum embodied, balance and dissipation, necessary for arising without end (`arising_opens`), and not sufficient.

**Correction.** Write "one such world (`exposed`) …" (一个这样的世界……), and add `s6_holding` beside `openness_contingent`: "nor does openness, with the eight premises, give arising without end".

### R9. presentation (provenance): Ren's words on overlap and on the names

**(a) One sentence of Ren's, three renderings.** The sentence is "generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧".

- **Verbatim:** chapter item 4 and §2, glossary line 697, plan §6 (line 168).
- **As an assertion:** `Space.lean:12–13`, "Ren said that, though both are in one becoming model, they do not overlap". This is unmarked and unchanged since P23c. The tenth review's §3 called the quotation in `Space` exact; it is a paraphrase without the 吧.
- **As an open question:** records ceasing-needs-arising, bounded-census-keeps-pace, census-balance and coming-and-ceasing-keep-pace ("Ren asked whether the two do not overlap") and plan line 257 ("Ren asked whether they do not overlap").
- The sentence ends in 吧, a tag that presumes the answer. "Asked whether" drops the presumption, and "said that" drops the tag.

**(b) What Ren confirmed.**

- Ren's words are English: "arising/ceasing is indeed better name".
- The Chinese terms 生起/止息 are the AI's, from P23c. Several zh texts say Ren confirmed the Chinese names:
  - the source file's title, "Ren：生起与止息是更好的名称";
  - plan lines 226 (the P29 note) and 248 ("Ren 确认生起与止息是更好的名称"), and the English line 276 ("Ren confirmed arising and ceasing as the better names"), which is accurate;
  - chapter §8 names (529: "生起与止息已由 Ren 确认");
  - study §39 ("不再列为 AI 拟定的用语").
- Chinese and English are equally primary, and the Chinese pair remains an AI rendering of the names Ren confirmed.

**(c) The context of the reply.**

- Ren replied to an AI note saying that the spine's names "reuse Ren's 'generative/degenerative' terms despite Ren saying they shouldn't overlap".
- The source file records this note in full. The canonical texts quote only Ren's reply, keep the activity reading as "a candidate for Ren's choice" for the proposal's terms, and render Ren's sentence as a question.
- Ren did not contest the note's "Ren saying they shouldn't overlap". Whether that settles the candidate is Ren's to say. This review does not choose.

**Correction.**

- Quote the sentence verbatim in `Space.lean` and the four records, or gloss it consistently as "a tag question presuming they do not overlap".
- In zh, write "Ren 确认英文名称 arising/ceasing（中文 生起／止息 为 AI 的译名）", and retitle the source file accordingly, or note the translation.
- In §8's first item, quote the AI note's sentence with Ren's reply, and ask Ren whether the activity reading remains a candidate.

### R10. presentation: two different worlds named brood

- `Roles` already has `Becoming.Brood` (lines 905–1002): generation after generation arising without end, nothing taken, not dissipative (`Brood.not_dissipative`, `Brood.rise_without_fall`). It is cited by the chapter as `Brood` (§2, lines 271 and 275), by rising-and-falling-in-one-exchange and life-as-condition-of-life, and by `Descent` (`Brood.descended`).
- P29 adds `Becoming.World.Brood` and `World.brood`. This world is dissipative and comes to rest after one arising.
- The chapter now cites both as `Brood`/`brood`, a few paragraphs apart, for opposite purposes.
- **Correction.** Rename one of them (names are Ren's to choose in any case), or always qualify (`World.brood`).

### R11. presentation and bookkeeping

- **(a) The balance read of dependence.**
  - Chapter item 4 (zh 76, en 108) says the balance holds "of activity, standing and dependence alike", and plan line 274 (P28) says "read of activity, standing and dependence".
  - No dependence instance of `over_stretch` is stated. The census-balance record lists "the balance read of dependence" under next_delta.
  - It does follow from `Listed.over_stretch`, but only with `requires` decided, as `DependenceCensus.forming_of_dissolving` assumes.
  - State the instance with its decidability, or remove "dependence" from the two sentences.
- **(b) Count lines.**
  - The English P25b paragraph (2665–2671) gives no "package now has" line, unlike P23c, P26–P28 and P29. The zh §38 gives 1077/1739.
  - Plan rows 247–248 (P25b, P29) cite no receipt, unlike rows 244–246.
- **(c) §2 of the chapter** (215, 219) says "only with infinitely many relata do they separate … and then only where the count of the active is unbounded". See R6 for the sharp form.
- **(d)** The census-balance record's next_delta lists "deriving the recurrence laws from the balance so that the two routes are one". That is reasonable and not needed for correctness. No action.

## 3. What remains sound

**Build and receipt.**

- The 29 modules of the core closure compile from the prelude, exit 0, with no warnings.
- All 1830 source declarations have empty axiom reports. Of the 5153 constants, only the 35 generated `injEq` lemmas have an axiom, `propext`, exactly as the receipt lists them.
- The receipts' counts, source hashes and retained artifacts are correct, as are the 394 reference hashes and 111 proof bindings of the 32 changed records.
- The periphery checker's `LEAN_TIMEOUT` and the retained timed-out runs are disclosed.

**P26.**

- The census law is correct, and its proof is a clean counting argument: a ceasing not preceded by a coming to be shortens the list.
- `census_one_way` shows both directions of its strictness with existing worlds.
- The rest theorem is correct with its premises in the signature.
- `rest_needs_census` (`dusk`) and `rest_needs_standing` (`kindling`, `ember`) show each census is needed.
- `Finite.comes_to_rest` and `rests_around` exhibit `rests` and the embodied case as instances, as claimed.

**P27.**

- `Listed` is a good abstraction. The same law reads of activity, standing and dependence by instantiation, matching §26's one change read three ways.
- The bounded law is correct, and `procession_world` correctly shows it reaches beyond finite worlds.

**P28.**

- `Listed.across` is an exact per-step identity with a careful proof (`marks_le_of_sub` both ways).
- `over_stretch`, `ceasings_within` and `comings_within` are correct, and the record's rate reading matches them.

**P25b.**

- The new declarations are correct.
- `stills` now takes `¬¬` enclosure. That is a real strengthening, and it frees `rests_enclosed` and `arising_opens` from `DecidableEq`, as the tenth review's Q4 suggested.
- The handling table of §38 is honest about what was moved into the core and what was not.
- The in-place corrections that were made are marked and quote the originals.

**P29.**

- `brood_binds` and `brood_rests` are correct.
- `Binds` is a reasonable non-vacuity notion for seven of the eight premises.
- §39 is careful to say that binding is not independence, with `acting_across` as its example.
- The source file separates Ren's words from the AI's note and the AI's interpretation, and records the note in full.

**Ren and method.**

- Names are listed as Ren's to choose.
- No payment, ledger or "giver" vocabulary enters the account of 生生.
- The worlds are read with one kind of relatum. No module evaluates arising, ceasing, rest or openness.
- The probes here show what the definitions admit, not what actual systems do.

## 4. What would change the verdicts

1. **R1.** State the undermining sentence with "where the relatum depending was active", or add the `Ceases` variant, and widen the §8 choice to dormant dependences. Verdict 7 then has nothing left to qualify.
2. **R2.** Move `law_iff_em` into `Space`, or delete the "needs choice / cannot be stated" sentences.
3. **R3.** Gloss `Binds.counted` as the world not being finite, state that `brood`'s census comes from three relata ever active, and add `rest_few` with the qualified headline. Verdicts 3, 8 and 9 then become "yes, as qualified".
4. **R4–R8.** Make the listed edits. Move `ceasing_of_coming_often`, `paced_world`, `finite_census_bounded` and `s6_holding` into the core, or cite them.
5. **R9–R11.** Make the provenance and bookkeeping edits.
6. **Withdrawals.**
   - If Ren states that undermining a dormant dependence counts as not living, the §8 choice item (R1) becomes a record of that statement. The core fix to the sentence remains.
   - If Ren states whether the activity reading is withdrawn as a candidate, R9(c) reduces to quoting that statement.
   - No change of wording removes the probes of R1, R2, R3, R6, R7 and R8. They are theorems about the published definitions.

**Ren's choices.** These are as listed in chapter §8. This review adds one and refines another:

- whether undermining a dependence whose relatum is dormant (not active) counts against living (R1);
- whether the activity reading remains a candidate for the proposal's "generative, degenerative", given the context of Ren's reply (R9).

**Not checked.**

- **Rebuilt and run.**
  - The bridge and periphery were not rebuilt; their bytes match the receipts.
  - No `make` target, `research-check` or `research-render` was run.
- **Not read.** No external literature.
- **Checked only in part.** Chinese–English parity was checked only at the cited lines.
- **Not formalized.**
  - The flow taking part only finitely often under the rest theorem's premises (R3).
  - The ceasing-to-arising direction of `law_of_em` (R2).
  - The even/odd example showing that the bound at infinitely many steps is strictly weaker than the bound from some step on (R6).

## Appendix A. Probe source

`Review11.lean` (sha256 `16142d92675bbd8357322aa3ea26325b03738b3b6acfb124ac3c730b1b74e8a5`, 507 lines). Compiled with `LEAN_PATH=<core build> lean -o Review11.olean Review11.lean`: exit 0, no warnings, no `sorry`, no tactic.

```lean
import Becoming

/-!
Probes of the eleventh independent review (P26, P27, P28, P25b, P29). Each is
term-mode and axiom-free; none is part of the repository.
-/

namespace Review11

open Becoming

/-! ## S1. Undermining with no ending: a sleeper -/

namespace Sleeper

inductive Relatum where
  | drawer
  | seed
  | soil

def soilLevel : Nat → Nat
  | 0 => 3
  | _ + 1 => 1

/-- The drawer stands at one throughout, the seed at nothing, the soil at three and then
one. -/
def level (t : Nat) : Relatum → Nat
  | .drawer => 1
  | .seed => 0
  | .soil => soilLevel t

/-- Across the first step the drawer takes two units of soil; nothing is given. -/
def flow : Flow Relatum Relatum where
  present
    | 0 => [.drawer]
    | _ + 1 => []
  take _ x y := match x, y with
    | .drawer, .soil => 2
    | .drawer, .drawer => 0
    | .drawer, .seed => 0
    | .seed, _ => 0
    | .soil, _ => 0
  give _ _ _ := 0

/-- Every relatum is active while it stands. The seed depends on the soil at need two
throughout; the drawer draws on the soil. -/
def web : Web Relatum Relatum where
  level := level
  active t x := 0 < level t x
  requires _ x y := x = .seed ∧ y = .soil
  need _ _ _ := 2
  draws _ x y := x = .drawer ∧ y = .soil

theorem distinct : Distinct [Relatum.drawer, .seed, .soil] :=
  ⟨fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
   fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩

end Sleeper

def sleeper : World :=
  ⟨Sleeper.Relatum, Sleeper.flow, Sleeper.web⟩

/-- A finite, balanced world in which activity needs support and every relatum is
embodied. The drawer's event at the first step undermines the seed's dependence on the
soil, which persists unchanged, so the event is not living; `Web.Dependent.inactive_below`
applies. Yet the seed is never active and nothing ever ceases: the undermining co-occurs
with no ending. -/
theorem s1_sleeper :
    sleeper.Dependent ∧ sleeper.Embodied ∧ sleeper.Balanced ∧ sleeper.Finite ∧
    sleeper.web.UnderminingOn 0 .drawer .soil ∧ ¬ sleeper.Living ∧
    (sleeper.web.level 1 .soil < sleeper.web.need 0 .seed .soil ∧
      sleeper.web.requires 1 .seed .soil ∧
      sleeper.web.need 0 .seed .soil ≤ sleeper.web.need 1 .seed .soil) ∧
    (∀ t, ¬ sleeper.web.active t .seed) ∧ (∀ t x, ¬ sleeper.web.Ceases t x) :=
  have undermining : sleeper.web.UnderminingOn 0 .drawer .soil :=
    ⟨⟨rfl, rfl⟩, .seed, ⟨rfl, rfl⟩,
     ⟨0, Nat.le_refl 0, fun _ _ _ => ⟨rfl, rfl⟩, Nat.le_succ 2, Nat.lt_succ_self 1⟩,
     Nat.lt_succ_self 1⟩
  ⟨fun _ f active c requires => match f, c, requires, active with
     | _, _, ⟨rfl, rfl⟩, active => absurd active (Nat.lt_irrefl 0),
   fun _ _ => Iff.rfl,
   fun t c => match t, c with
     | 0, .drawer => rfl
     | 0, .seed => rfl
     | 0, .soil => rfl
     | _ + 1, .drawer => rfl
     | _ + 1, .seed => rfl
     | _ + 1, .soil => rfl,
   ⟨[.drawer, .seed, .soil], Sleeper.distinct, fun x => match x with
     | .drawer => .head _
     | .seed => .tail _ (.head _)
     | .soil => .tail _ (.tail _ (.head _))⟩,
   undermining,
   fun living => living 0 .drawer Nat.zero_lt_one ⟨.soil, undermining⟩,
   ⟨Nat.lt_succ_self 1, ⟨rfl, rfl⟩, Nat.le_refl 2⟩,
   fun _ => Nat.lt_irrefl 0,
   fun _ x ceases => match x, ceases with
     | .drawer, ⟨_, no⟩ => no Nat.zero_lt_one
     | .seed, ⟨active, _⟩ => absurd active (Nat.lt_irrefl 0)
     | .soil, ⟨_, no⟩ => no Nat.zero_lt_one⟩

/-- The core lemma applies to the sleeper, and its conclusion is that the seed is not
active after the step, which it never was. -/
theorem s1_inactive_below : ¬ sleeper.web.active 1 .seed :=
  Web.Dependent.inactive_below s1_sleeper.1 (t := 0) (c := .soil) (Nat.lt_succ_self 1)
    ⟨rfl, rfl⟩ (Nat.le_refl 2)

/-! ## S2. A census in a world that comes to rest is a census of finitely many -/

section Few

variable {α : Type} {p : α → Nat → Prop} [∀ a t, Decidable (p a t)] {l : Nat → List α}

/-- The lists of the steps up to `n`, joined. -/
def gather (l : Nat → List α) : Nat → List α
  | 0 => l 0
  | n + 1 => l (n + 1) ++ gather l n

theorem gather_self {a : α} : ∀ {s : Nat}, a ∈ l s → a ∈ gather l s
  | 0, mem => mem
  | _ + 1, mem => mem_append_left _ mem

theorem mem_gather {a : α} {s : Nat} (mem : a ∈ l s) : ∀ {n}, s ≤ n → a ∈ gather l n
  | _, .refl => gather_self mem
  | m + 1, .step within => mem_append_right (l (m + 1)) (mem_gather mem within)

/-- A member holding after `N` but not at `N` comes to be from `N` on. -/
theorem comes_after {a : α} {N : Nat} (fails : ¬ p a N) :
    ∀ {T}, N ≤ T → p a T → ∃ t, N ≤ t ∧ ComesToBe (p a) t
  | _, .refl, holds => absurd holds fails
  | m + 1, .step within, holds =>
    if h : p a m then comes_after fails within h else ⟨m, within, h, holds⟩

/-- Where what holds is listed at each step and coming to be does not recur, not
unboundedly many members ever hold: not every finite list misses a member holding at some
step. -/
theorem few_of_quiet (listed : Listed p l)
    (quiet : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ¬ ∀ L : List α, ∃ t a, p a t ∧ ¬ a ∈ L :=
  fun many => quiet fun N => match many (gather l N) with
    | ⟨t, a, holds, out⟩ =>
      have fails : ¬ p a N := fun h => out (mem_gather (((listed N).2 a).mp h) (Nat.le_refl N))
      match Nat.decLe N t with
      | isTrue later => match comes_after fails later holds with
        | ⟨s, after, comes⟩ => ⟨s, a, after, comes⟩
      | isFalse early => absurd (mem_gather (((listed t).2 a).mp holds)
          (Nat.le_of_lt (Nat.gt_of_not_le early))) out

/-- Conversely, where every member ever holding is on one list without repetition, what
holds is listed at each step. -/
theorem listed_of_ever {L : List α} (distinct : Distinct L) (ever : ∀ t a, p a t → a ∈ L) :
    Listed p (fun t => keep (fun a => p a t) L) :=
  fun t => ⟨keep_distinct distinct, fun a =>
    ⟨fun holds => mem_keep.mpr ⟨ever t a holds, holds⟩, fun mem => (mem_keep.mp mem).2⟩⟩

end Few

section Worlds

variable {w : World}

/-- Read of activity: under a census, where arising does not recur, not unboundedly many
relata are ever active. -/
theorem few_active [∀ t x, Decidable (w.web.active t x)] {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) (quiet : ¬ w.ArisingRecurs) :
    ¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L :=
  few_of_quiet (p := fun x t => w.web.active t x) census quiet

/-- In every world to which the rest theorem applies, not unboundedly many relata are ever
active, and not unboundedly many ever stand. -/
theorem rest_few [∀ t x, Decidable (w.web.active t x)] (counted : w.Counted)
    {stand : Nat → List w.Relatum} (standing : w.web.StandingCensus stand)
    (embodied : w.ArisingEmbodied) (balanced : w.Balanced) (dissipative : w.Dissipative)
    {T : Nat} (around : ∀ t, T ≤ t → w.flow.AroundStanding stand t) :
    (¬ ∀ L : List w.Relatum, ∃ t x, w.web.active t x ∧ ¬ x ∈ L) ∧
    (¬ ∀ L : List w.Relatum, ∃ t x, 0 < w.web.level t x ∧ ¬ x ∈ L) :=
  match counted with
  | ⟨_, census⟩ =>
    ⟨few_active census (World.arising_stops standing embodied balanced dissipative around),
     few_of_quiet (p := fun x t => 0 < w.web.level t x) standing fun coming =>
       Flow.stills balanced dissipative standing (fun t later => not_not_intro (around t later))
         fun N => match coming N with
         | ⟨t, x, later, comes⟩ =>
           ⟨t, x, later, .inl (Web.ComesToStand.rises (W := w.web) comes)⟩⟩

/-- A world whose activity is decided and whose relata ever active lie on one list has a
census. -/
theorem counted_of_ever [∀ t x, Decidable (w.web.active t x)] {L : List w.Relatum}
    (distinct : Distinct L) (ever : ∀ t x, w.web.active t x → x ∈ L) : w.Counted :=
  ⟨_, listed_of_ever (p := fun x t => w.web.active t x) distinct ever⟩

end Worlds

instance brood_decided : ∀ t x, Decidable (World.brood.web.active t x) :=
  fun t x => Nat.decLt 0 (World.Brood.level t x)

/-- In `brood` only the food, the parent and the child are ever active. -/
theorem brood_ever : ∀ t x, World.brood.web.active t x → x ∈ World.Brood.kin
  | _, .food, _ => .head _
  | _, .parent, _ => .tail _ (.head _)
  | _, .child, _ => .tail _ (.tail _ (.head _))
  | _, .ground _, active => absurd active (Nat.lt_irrefl 0)

/-- So `brood`'s census comes from finitely many relata ever active. -/
theorem brood_counted_ever : World.brood.Counted :=
  counted_of_ever World.Brood.kin_distinct brood_ever

/-- The ground relata of `brood` are idle: never standing or active, never taking part,
never taken from or given to, never depended on or drawn on. -/
theorem brood_idle (t n : Nat) :
    World.brood.web.level t (.ground n) = 0 ∧ ¬ World.brood.web.active t (.ground n) ∧
    ¬ World.Brood.Relatum.ground n ∈ World.brood.flow.present t ∧
    (∀ f, World.brood.flow.take t f (.ground n) = 0 ∧
      World.brood.flow.give t f (.ground n) = 0) ∧
    (∀ f, ¬ World.brood.web.requires t f (.ground n)) ∧
    (∀ f, ¬ World.brood.web.draws t f (.ground n)) :=
  ⟨rfl, Nat.lt_irrefl 0,
   fun mem => match t, mem with
     | 0, .tail _ no => (nomatch no)
     | _ + 1, no => (nomatch no),
   fun f => match f with
     | .food => ⟨rfl, rfl⟩
     | .parent => ⟨rfl, rfl⟩
     | .child => ⟨rfl, rfl⟩
     | .ground _ => ⟨rfl, rfl⟩,
   fun _ requires => (nomatch requires.2),
   fun _ draws => match draws.2 with
     | .inl no => (nomatch no)
     | .inr no => (nomatch no)⟩

/-- As in every world where arising stops under a census, not unboundedly many relata of
`brood` are ever active. -/
theorem brood_few :
    ¬ ∀ L : List World.brood.Relatum, ∃ t x, World.brood.web.active t x ∧ ¬ x ∈ L :=
  match World.brood_counted with
  | ⟨_, census⟩ => few_active census World.brood_rests.2.2.1

/-! ## S3. A bound at infinitely many steps suffices, and any unbounded pace allows arising
without ceasing -/

section Often

variable {α : Type} {p : α → Nat → Prop} [∀ a t, Decidable (p a t)] {l : Nat → List α}

/-- Where coming to be recurs, for each `k`, from some step on either something has ceased
since `N` or the list is longer than at `N` by `k`. -/
theorem grows (listed : Listed p l) (coming : ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ∀ k N, ∃ M, N ≤ M ∧ ∀ T, M ≤ T →
      (∃ t a, N ≤ t ∧ CeasesToBe (p a) t) ∨ (l N).length + k ≤ (l T).length
  | 0, N => ⟨N, Nat.le_refl N, fun _ later => match listed.ceases_or_kept later with
      | .inl found => .inl found
      | .inr kept => .inr (length_le_of_sub (listed N).1 fun a mem =>
          ((listed _).2 a).mp (kept a (((listed N).2 a).mpr mem)))⟩
  | k + 1, N => match coming N with
    | ⟨M0, _, later, comes⟩ => match listed.ceases_or_more later comes with
      | .inl found => ⟨N, Nat.le_refl N, fun _ _ => .inl found⟩
      | .inr more => match grows listed coming k (M0 + 1) with
        | ⟨M, after, all⟩ => ⟨M, Nat.le_trans (Nat.le_succ_of_le later) after, fun T late =>
            match all T late with
            | .inl ⟨t, b, tl, ceases⟩ =>
              .inl ⟨t, b, Nat.le_trans (Nat.le_succ_of_le later) tl, ceases⟩
            | .inr bound => .inr (Nat.le_trans (Nat.le_of_eq (Nat.succ_add (l N).length k).symm)
                (Nat.le_trans (Nat.add_le_add_right more k) bound))⟩

/-- The bounded law needs the bound only at infinitely many steps: where at arbitrarily
late steps at most `B` are listed, coming to be recurring needs ceasing to be recurring. -/
theorem ceasing_of_coming_often (listed : Listed p l) {B : Nat}
    (often : ∀ N, ∃ t, N ≤ t ∧ (l t).length ≤ B)
    (coming : ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t :=
  fun N => match grows listed coming (B + 1) N with
    | ⟨M, _, all⟩ => match often M with
      | ⟨T, late, small⟩ => match all T late with
        | .inl found => found
        | .inr big => absurd (Nat.le_trans (Nat.le_add_left (B + 1) (l N).length)
            (Nat.le_trans big small)) (Nat.not_succ_le_self B)

end Often

/-- Read of worlds: under a census with at most `B` active at arbitrarily late steps,
arising recurs exactly when ceasing does. -/
theorem arising_iff_ceasing_often {w : World} [∀ t x, Decidable (w.web.active t x)]
    {alive : Nat → List w.Relatum} (census : w.web.Census alive) {B : Nat}
    (often : ∀ N, ∃ t, N ≤ t ∧ (alive t).length ≤ B) :
    w.ArisingRecurs ↔ w.CeasingRecurs :=
  ⟨ceasing_of_coming_often (p := fun x t => w.web.active t x) census often,
   World.arising_of_ceasing ⟨alive, census⟩⟩

/-- The numbers below `n`. -/
def upto : Nat → List Nat
  | 0 => []
  | n + 1 => n :: upto n

theorem mem_upto : ∀ {n k : Nat}, k ∈ upto n ↔ k < n
  | 0, k => ⟨fun mem => (nomatch mem), fun lt => absurd lt (Nat.not_lt_zero k)⟩
  | n + 1, _ => ⟨fun mem => match mem with
      | .head _ => Nat.lt_succ_self _
      | .tail _ mem => Nat.lt_succ_of_lt (mem_upto.mp mem),
    fun lt => match Nat.eq_or_lt_of_le (Nat.le_of_lt_succ lt) with
      | .inl same => same ▸ .head _
      | .inr lower => .tail _ (mem_upto.mpr lower)⟩

theorem distinct_upto : ∀ n, Distinct (upto n)
  | 0 => trivial
  | n + 1 => ⟨fun mem => Nat.lt_irrefl n (mem_upto.mp mem), distinct_upto n⟩

theorem length_upto : ∀ n, (upto n).length = n
  | 0 => rfl
  | n + 1 => congrArg (· + 1) (length_upto n)

/-- Relatum `k` is active from the step at which the count `g` first exceeds `k`. -/
def Paced.web (g : Nat → Nat) : Web Nat Nat where
  level _ _ := 0
  active t k := k < g t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- `dawn` at any pace. -/
def paced (g : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Paced.web g⟩

theorem find_rise (g : Nat → Nat) (N : Nat) :
    ∀ d, g N < g (N + d) → ∃ s, N ≤ s ∧ g s < g (s + 1)
  | 0, h => absurd h (Nat.lt_irrefl _)
  | d + 1, h => match Nat.decLt (g (N + d)) (g (N + d + 1)) with
    | isTrue r => ⟨N + d, Nat.le_add_right N d, r⟩
    | isFalse r => find_rise g N d (Nat.lt_of_lt_of_le h (Nat.ge_of_not_lt r))

/-- For every count `g` that never falls and later exceeds each of its values (a count
growing logarithmically, say), some world has a census counting `g t` at step `t`, in which
arising recurs and nothing ever ceases. -/
theorem paced_world (g : Nat → Nat) (mono : ∀ t, g t ≤ g (t + 1))
    (grows : ∀ N, ∃ d, g N < g (N + d)) :
    (paced g).web.Census (fun t => upto (g t)) ∧ (∀ t, (upto (g t)).length = g t) ∧
    (paced g).ArisingRecurs ∧ ¬ (paced g).CeasingRecurs :=
  ⟨fun t => ⟨distinct_upto (g t), fun _ => mem_upto.symm⟩,
   fun t => length_upto (g t),
   fun N => match grows N with
     | ⟨d, h⟩ => match find_rise g N d h with
       | ⟨s, later, rise⟩ => ⟨s, g s, later, Nat.lt_irrefl (g s), rise⟩,
   fun ceasing => match ceasing 0 with
     | ⟨t, _, _, active, inactive⟩ => inactive (Nat.lt_of_lt_of_le active (mono t))⟩

/-! ## S4. The converse of `law_decides` needs no choice -/

/-- With excluded middle, a negated universal has a counterexample. -/
theorem push (em : ∀ P : Prop, P ∨ ¬ P) {Q : Nat → Prop} (notAll : ¬ ∀ N, Q N) :
    ∃ N, ¬ Q N :=
  match em (∃ N, ¬ Q N) with
  | .inl found => found
  | .inr nothing => absurd (fun N => match em (Q N) with
      | .inl q => q
      | .inr nq => absurd ⟨N, nq⟩ nothing) notAll

/-- Where nothing ceases from `N` on, what is active from `N` on stays active. -/
theorem stays (em : ∀ P : Prop, P ∨ ¬ P) {w : World} {N : Nat}
    (still : ¬ ∃ t x, N ≤ t ∧ w.web.Ceases t x) {x : w.Relatum} {s : Nat} (from_ : N ≤ s)
    (active : w.web.active s x) : ∀ {T}, s ≤ T → w.web.active T x
  | _, .refl => active
  | m + 1, .step within => match em (w.web.active (m + 1) x) with
    | .inl a => a
    | .inr na => absurd ⟨m, x, Nat.le_trans from_ within,
        stays em still from_ active within, na⟩ still

/-- Where nothing ceases from `N` on, the relata of a list can arise only finitely often. -/
theorem arises_finitely (em : ∀ P : Prop, P ∨ ¬ P) {w : World} {N : Nat}
    (still : ¬ ∃ t x, N ≤ t ∧ w.web.Ceases t x) :
    ∀ (L : List w.Relatum) (N' : Nat), N ≤ N' →
      (∀ x, ¬ w.web.active N' x → x ∈ L ∨ ∀ T, N' ≤ T → ¬ w.web.Arises T x) →
      ∃ M, N' ≤ M ∧ ∀ T x, M ≤ T → ¬ w.web.Arises T x
  | [], N', from_, covered => ⟨N', Nat.le_refl N', fun T x later arises =>
      match covered x (fun active => arises.1 (stays em still from_ active later)) with
      | .inl no => (nomatch no)
      | .inr never => never T later arises⟩
  | a :: L, N', from_, covered => match em (∃ T, N' ≤ T ∧ w.web.Arises T a) with
    | .inl ⟨T, later, arisesA⟩ =>
      match arises_finitely em still L (T + 1) (Nat.le_trans from_ (Nat.le_succ_of_le later))
        (fun x inactive => match covered x
            (fun active => inactive (stays em still from_ active (Nat.le_succ_of_le later))) with
          | .inl mem => match mem_cons_cases mem with
            | .inl same => absurd (Eq.mpr (congrArg (fun y => w.web.active (T + 1) y) same)
                arisesA.2) inactive
            | .inr rest => .inl rest
          | .inr never => .inr fun T' later' =>
              never T' (Nat.le_trans (Nat.le_succ_of_le later) later')) with
      | ⟨M, after, quiet⟩ => ⟨M, Nat.le_trans (Nat.le_succ_of_le later) after, quiet⟩
    | .inr nothing =>
      match arises_finitely em still L N' from_ (fun x inactive => match covered x inactive with
          | .inl mem => match mem_cons_cases mem with
            | .inl same => .inr fun T later arises => nothing ⟨T, later,
                Eq.mpr (congrArg (fun y => w.web.Arises T y) same.symm) arises⟩
            | .inr rest => .inl rest
          | .inr never => .inr never) with
      | ⟨M, after, quiet⟩ => ⟨M, after, quiet⟩

/-- With excluded middle as a hypothesis, and no decidability, in every finite world in
which arising recurs ceasing recurs. -/
theorem law_of_em (em : ∀ P : Prop, P ∨ ¬ P) (w : World) (finite : w.Finite)
    (arising : w.ArisingRecurs) : w.CeasingRecurs :=
  match em w.CeasingRecurs with
  | .inl ceasing => ceasing
  | .inr notCeasing =>
    match push em (Q := fun N => ∃ t x, N ≤ t ∧ w.web.Ceases t x) notCeasing with
    | ⟨N, still⟩ => match finite with
      | ⟨all, _, every⟩ =>
        match arises_finitely em still all N (Nat.le_refl N) (fun x _ => .inl (every x)) with
        | ⟨M, _, quiet⟩ => match arising M with
          | ⟨t, x, later, arises⟩ => absurd arises (quiet t x later)

/-- So the law asked of every finite world without decidability is equivalent to excluded
middle, in the pure core and without choice. -/
theorem law_iff_em :
    (∀ w : World, w.Finite → w.ArisingRecurs → w.CeasingRecurs) ↔ ∀ Q : Prop, Q ∨ ¬ Q :=
  ⟨World.law_decides, fun em w finite arising => law_of_em em w finite arising⟩

/-! ## S5. Every census of a finite world is bounded, with no decidability -/

theorem finite_census_bounded {w : World} (finite : w.Finite) :
    ∃ B, ∀ alive, w.web.Census alive → ∀ t, (alive t).length ≤ B :=
  match finite with
  | ⟨all, _, every⟩ => ⟨all.length, fun _ census t =>
      length_le_of_sub (census t).1 fun x _ => every x⟩

/-! ## S6. Openness without arising: a holder exchanging at zero net -/

namespace Holding

/-- One side stands at one throughout; the other side and the ground stand at nothing. -/
def level (_ : Nat) : Exposed.Relatum → Nat
  | .side true => 1
  | .side false => 0
  | .ground _ => 0

/-- At every step the standing side takes a unit from each ground relatum and gives it
back. -/
def flow : Flow Exposed.Relatum Exposed.Relatum where
  present _ := [.side true]
  take _ x y := match x, y with
    | .side true, .ground _ => 1
    | .side true, .side _ => 0
    | .side false, _ => 0
    | .ground _, _ => 0
  give _ x y := match x, y with
    | .side true, .ground _ => 1
    | .side true, .side _ => 0
    | .side false, _ => 0
    | .ground _, _ => 0

def web : Web Exposed.Relatum Exposed.Relatum where
  level := level
  active t x := 0 < level t x
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

theorem open_at (t : Nat) : ¬ flow.Enclosed t :=
  fun ⟨cs, _, closed⟩ => Nat.zero_ne_one
    (closed (.side true) (.head _) _ (Exposed.outside cs)).1.symm

theorem census : web.Census fun _ => [.side true] :=
  fun _ => ⟨⟨fun no => (nomatch no), trivial⟩, fun x => match x with
    | .side true => ⟨fun _ => .head _, fun _ => Nat.zero_lt_one⟩
    | .side false => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Exposed.Relatum.side false ∈ [Exposed.Relatum.side true]) => match mem with
          | .tail _ no => (nomatch no)⟩
    | .ground n => ⟨fun no => absurd no (Nat.lt_irrefl 0),
        fun (mem : Exposed.Relatum.ground n ∈ [Exposed.Relatum.side true]) => match mem with
          | .tail _ no => (nomatch no)⟩⟩

end Holding

def holding : World :=
  ⟨Exposed.Relatum, Holding.flow, Holding.web⟩

/-- A world meeting all eight premises with no step enclosed in which nothing ever arises or
ceases: openness, with the eight premises, does not give arising without end. -/
theorem s6_holding :
    holding.Premised ∧ (∀ t, ¬ holding.flow.Enclosed t) ∧ ¬ holding.ArisingRecurs ∧
    ¬ holding.CeasingRecurs ∧ ¬ holding.Finite :=
  ⟨.of (fun _ _ _ _ no => no.elim)
     (fun _ c => match c with
      | .side true => rfl
      | .side false => rfl
      | .ground _ => rfl)
     (fun _ f _ present _ => match f, present with
      | _, .head _ => Nat.zero_lt_one
      | _, .tail _ no => (nomatch no))
     (fun _ f _ present _ => match f, present with
      | _, .head _ => ⟨Nat.zero_lt_one, trivial⟩
      | _, .tail _ no => (nomatch no))
     (fun cs t distinct closed => absurd ⟨cs, distinct, closed⟩ (Holding.open_at t))
     (fun _ _ => Iff.rfl) ⟨_, Holding.census⟩ ⟨0, fun _ _ _ _ _ no => no.elim⟩,
   Holding.open_at,
   fun arising => match arising 0 with
    | ⟨_, x, _, arises⟩ => match x, arises with
      | .side true, arises => arises.1 Nat.zero_lt_one
      | .side false, arises => absurd arises.2 (Nat.lt_irrefl 0)
      | .ground _, arises => absurd arises.2 (Nat.lt_irrefl 0),
   fun ceasing => match ceasing 0 with
    | ⟨_, x, _, ceases⟩ => match x, ceases with
      | .side true, ceases => ceases.2 Nat.zero_lt_one
      | .side false, ceases => absurd ceases.1 (Nat.lt_irrefl 0)
      | .ground _, ceases => absurd ceases.1 (Nat.lt_irrefl 0),
   fun ⟨all, _, every⟩ => Exposed.outside all (every _)⟩

end Review11
```

## Appendix B. Probe axiom audit

`Review11Audit.lean` (sha256 `bd0b43499c7d289371675358dc2322226651431426078e57afab8d3148eadbcd`) enumerates every constant the probe module adds, including auxiliary and generated ones, with `Lean.collectAxioms`, and prints the axioms of the fifteen main probes:

```lean
import Lean
import Review11
open Lean Elab Command
#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review11 | throwError "no module"
  let mut count := 0
  let mut withAx := 0
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then
        withAx := withAx + 1
        logInfo m!"AXIOMS {n} {axioms.toList}"
  logInfo m!"CONSTANTS Review11 {count} WITHAXIOMS {withAx}"
#print axioms Review11.s1_sleeper
#print axioms Review11.s1_inactive_below
#print axioms Review11.few_of_quiet
#print axioms Review11.rest_few
#print axioms Review11.counted_of_ever
#print axioms Review11.brood_counted_ever
#print axioms Review11.brood_idle
#print axioms Review11.brood_few
#print axioms Review11.ceasing_of_coming_often
#print axioms Review11.arising_iff_ceasing_often
#print axioms Review11.paced_world
#print axioms Review11.law_of_em
#print axioms Review11.law_iff_em
#print axioms Review11.finite_census_bounded
#print axioms Review11.s6_holding
```

Output:

```text
CONSTANTS Review11 159 WITHAXIOMS 0
'Review11.s1_sleeper' does not depend on any axioms
'Review11.s1_inactive_below' does not depend on any axioms
'Review11.few_of_quiet' does not depend on any axioms
'Review11.rest_few' does not depend on any axioms
'Review11.counted_of_ever' does not depend on any axioms
'Review11.brood_counted_ever' does not depend on any axioms
'Review11.brood_idle' does not depend on any axioms
'Review11.brood_few' does not depend on any axioms
'Review11.ceasing_of_coming_often' does not depend on any axioms
'Review11.arising_iff_ceasing_often' does not depend on any axioms
'Review11.paced_world' does not depend on any axioms
'Review11.law_of_em' does not depend on any axioms
'Review11.law_iff_em' does not depend on any axioms
'Review11.finite_census_bounded' does not depend on any axioms
'Review11.s6_holding' does not depend on any axioms
```

`Review11Print.lean` (sha256 `e04f1f6922ae02eb340d44685319cd03225d7cc5897f92ea606cd83cdf184860`) runs `#print axioms` on each of the 47 source declarations (32 theorems, 13 definitions, 1 instance, 1 inductive type). All 47 report "does not depend on any axioms":

`Review11.Sleeper.Relatum`, `Review11.Sleeper.soilLevel`, `Review11.Sleeper.level`, `Review11.Sleeper.flow`, `Review11.Sleeper.web`, `Review11.Sleeper.distinct`, `Review11.sleeper`, `Review11.s1_sleeper`, `Review11.s1_inactive_below`, `Review11.gather`, `Review11.gather_self`, `Review11.mem_gather`, `Review11.comes_after`, `Review11.few_of_quiet`, `Review11.listed_of_ever`, `Review11.few_active`, `Review11.rest_few`, `Review11.counted_of_ever`, `Review11.brood_decided`, `Review11.brood_ever`, `Review11.brood_counted_ever`, `Review11.brood_idle`, `Review11.brood_few`, `Review11.grows`, `Review11.ceasing_of_coming_often`, `Review11.arising_iff_ceasing_often`, `Review11.upto`, `Review11.mem_upto`, `Review11.distinct_upto`, `Review11.length_upto`, `Review11.Paced.web`, `Review11.paced`, `Review11.find_rise`, `Review11.paced_world`, `Review11.push`, `Review11.stays`, `Review11.arises_finitely`, `Review11.law_of_em`, `Review11.law_iff_em`, `Review11.finite_census_bounded`, `Review11.Holding.level`, `Review11.Holding.flow`, `Review11.Holding.web`, `Review11.Holding.open_at`, `Review11.Holding.census`, `Review11.holding`, `Review11.s6_holding`.

## Appendix C. Core audit

`CoreAudit.lean` (sha256 `e11246d4f9690c97b9ae2c2e7d825045f94abdb6ea4d71eddab511a3bcf42a4b`) is `import Becoming` with one `#print axioms` line for each of the 1830 source declarations the receipt lists for the 29 closure modules. All 1830 report "does not depend on any axioms".

`EnvAudit.lean` (sha256 `420f85b14528ce054087131a212c1c881294b396992b9f6a221a294a26bc77f0`) counts constants per module. Each count equals the receipt's `core_closure_constants`. Modules whose count changed since the tenth review are marked \*, with the count in the receipt at `63437779` in parentheses (`Change` and `Evolution` changed only in docstrings):

| Module | Constants | Module | Constants |
|---|---|---|---|
| `GenerativeCore` | 54 | `Becoming.Identity` | 487 |
| `Becoming.Frame` | 61 | `Becoming.Wholes` | 147 |
| `InquirySufficiency` | 107 | `Becoming.Dissipation` \* | 324 (318) |
| `Becoming.Inquiry` | 15 | `Becoming.Roles` \* | 464 (463) |
| `RelationalRenewal` | 134 | `Becoming.Reserve` | 144 |
| `Becoming.Renewal` | 58 | `Becoming.Evolution` | 152 |
| `Becoming.Dependence` | 475 | `Becoming.Space` \* | 243 (238) |
| `Becoming.Return` | 84 | `Becoming.Premises` \* | 339 (245) |
| `Becoming.Horizon` | 43 | `Becoming.Openness` \* | 164 (79) |
| `Becoming.Joint` | 203 | `Becoming.Metaethics` | 226 |
| `Becoming.Substitution` | 40 | `Becoming.Ranking` | 170 |
| `Becoming.Generation` | 216 | `Becoming.Correspondence` | 159 |
| `Becoming.Flow` | 225 | `Becoming.Descent` | 117 |
| `Becoming.Change` | 96 | `Becoming` | 0 |
| `Becoming.Population` \* | 206 (138) |  |  |
| total | 5153 (4894) | | |

There are 35 constants with an axiom. All are generated `injEq` lemmas depending only on `propext`, and they equal the receipt's `generated_axiom_dependencies`; the one added since the tenth review is marked \*:

`Generative.Process.mk.injEq`, `Becoming.Run.mk.injEq`, `Becoming.Frame.mk.injEq`, `Generative.InquirySufficiency.Policy.respond.injEq`, `Generative.InquirySufficiency.Policy.inquire.injEq`, `RelationalRenewal.Unfolding.mk.injEq`, `RelationalRenewal.Law.mk.injEq`, `Becoming.Conditions.mk.injEq`, `Becoming.Crossing.State.mk.injEq`, `Becoming.Crossing.Move.fall.injEq`, `Becoming.Dependence.mk.injEq`, `Becoming.Pinned.State.mk.injEq`, `Becoming.Web.mk.injEq`, `Becoming.Pool.Draw.mk.injEq`, `Becoming.Pool.State.mk.injEq`, `Becoming.Shock.State.mk.injEq`, `Becoming.Shock.Move.calm.injEq`, `Becoming.Flow.mk.injEq`, `Becoming.Reidentify.mk.injEq`, `Becoming.Confluence.Formation.new.injEq`, `Becoming.Generations.Formation.member.injEq`, `Becoming.Frontier.Formation.grower.injEq`, `Becoming.Frontier.Condition.fuel.injEq`, `Becoming.Kindling.Relatum.side.injEq`, `Becoming.Kindling.Relatum.fuel.injEq`, `Becoming.SprayHanding.Relatum.aux.injEq`, `Becoming.SprayHanding.Relatum.side.injEq`, `Becoming.World.Grazing.Relatum.side.injEq`, `Becoming.World.mk.injEq`, `Becoming.World.Brood.Relatum.ground.injEq` \*, `Becoming.World.Scatter.Relatum.ground.injEq`, `Becoming.Exposed.Relatum.side.injEq`, `Becoming.Exposed.Relatum.ground.injEq`, `Becoming.Valuation.mk.injEq`, `Becoming.Web.Condition.mk.injEq`.
