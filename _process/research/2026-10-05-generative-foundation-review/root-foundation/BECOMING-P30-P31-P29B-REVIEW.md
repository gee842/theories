# P30、P31 与 P29b 的独立审查 / Independent review of P30, P31 and P29b

2026-10-10。审查者：Claude Opus 5.5，独立 agent，未参与撰写 P30、P31 与 P29b。对象：`main` 的 `a9326202`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of P30, P31 or P29b. Object: `main` at `a9326202`.

**摘要（中文）。**

- **机械检查都对。**
  - 核心闭包的 29 个模块在仓库之外从前导重新编译，退出码为 0，没有警告。
  - 1896 条源声明的公理报告全部为空。其中定理 1171 项，计法同第十一次审查。
  - 闭包有 5333 个常量。依赖公理的只有 35 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同。其中 `World.Hatch.Relatum.ground.injEq` 取代了改名前的 `World.Brood…`。
  - 回执 `20261009T185557.684339Z` 的 42 个源哈希、检查器哈希与保留运行的 258 个产物都对。这次回执覆盖包 27 个模块，1131 项定理，1826 项声明审计。三个提交各自的回执与该提交的源和检查器一致。
  - 外围回执 `20261009T185801.898161Z` 的 33 个源哈希、3 个检查器哈希与 74 个产物都对。外围没有重建。
    - `170422` 与 `184936` 通过。
    - `173348` 失败：运行中源被改动，只检查了快照。P31 的提交说明已写出。
  - 自 `0cf14b8b` 起改动的 32 份记录中，402 个引用哈希与 112 个证明绑定都对。每份记录的时间戳都不晚于其提交：最晚的是 19:00:38Z，提交在 19:04:31Z。
  - 各阶段的计数与回执一致。
    - 定理数为 1086 → 1091 → 1109 → 1131，声明审计为 1760 → 1771 → 1793 → 1826。
    - 中间运行 `172715`（1106/1790）已被取代，提交说明已写出。
    - 章节 §9 的 26 个模块计数都等于回执，脊柱合计 1131。
  - 1155 个链接中没有坏锚点。
  - 名称有一处错（T1）。
    - 566 个别名中有 523 个在核心中解析。其余 43 个是第十一次审查已列的 41 个非核心别名，加上 P30 的 `Becoming.World.slow` 与 `Becoming.World.slow_world`。
    - 记录引用的 1567 个声明名中有 90 个不解析：84 个同前，属于非核心；6 个是 P30 的。
- **数学被接受。** 没有发现错误的 Lean 陈述。
  - P30 平衡读于复现是精确的。两个定律改由平衡证明，陈述不变。
    - `ceasing_of_returning`、`CountedBy.arising_iff_ceasing` 与 `slow_world` 分别等于第十一次审查的 `ceasing_of_coming_often`、`arising_iff_ceasing_often` 与 `paced_world`，回答了 R6。
    - `ceasing_of_outpacing` 是充分条件，正文也这样说。
  - P31 的 `chainEnd`、`chain_ends`、`chainEnd_zero` 与 `Cascade` 都对，界可以达到。`chain_ends_of_em` 以排中律为假设，不是公理。
  - P29b 的 `law_of_em`、`law_iff_em`、`Dependent.ceases_below`、`seedbank_world`、`hatch_*`、`holding_world`、`Finite.census_bounded`、`few_of_quiet` 与 `rest_few` 都对。
  - 本审查写了 55 条探针声明，其中 38 项定理。生成的 107 个常量都不依赖任何公理。
- **问题共八项（T1–T8）。** 其中三项错误（一项命名、一项散文、一项文档注释），三项过强，两项表述与记账。最严重的是 T2、T1 与 T3。
  - **T2（过强，未写出的前提）。** 问题在于链必须无限，而文本没有写出。
    - `Carries.chain_ends` 与 `chain_ends_of_em` 的前提 `bears` 对每个自然数 k 要求第 k+1 环依存于第 k 环。所以每一环之后都还有依存于它的一环。
    - 在有限、没有依存之环的网中（例如任何食物链），没有序列满足它，两个定理在那里是空的（探针 `no_chain`、`Short.short`）。
    - 研究 §41 反驳 3 与英文 P31 说“沿到达它的任一条链，界都成立”，说多了。
    - 章节 §2 与术语表把它与 `coextinct` 并列，而 `coextinct` 用的是有限的 `Reach`。
    - 同一归纳给出有限链的形式（探针 `chain_ends_upto`）；已提交的形式是它的实例。
  - **T1（错误，命名）。** `Openness.lean` 在已打开的 `namespace World` 里又打开了一次 `namespace World`（389、434 行）。
    - 所以 P30 的世界实际叫 `Becoming.World.World.slow` 与 `World.World.slow_world`。
    - 章节、研究、计划、两个 Lean 文档注释，以及记录 bounded-census-keeps-pace 的别名和引用，都写 `World.slow_world`。这些名称不存在。
    - P32（`df340093`）仍是如此。
  - **T3（错误，散文）。** 研究 §41 与英文 P31 说，把“只在有限多步活跃”化为终结之步“需要马尔可夫原则”。
    - 即使活动可判定且至多发生一次，这一步也蕴含 LPO（探针 `lpo_of_endStep`）。
    - 马尔可夫原则推不出 LPO。
- **其余各项。**
  - T4（错误，文档注释；R8 的残留）。`holding_world` 的注释说，在普查、“生起者体现”、平衡与耗散之下开放是必要的。
    - `arising_opens` 需要每个关系项都体现。
    - `kindling` 满足注释所列的前提，每步被围住，却生起不息（探针 `kindling_docstring`）。
  - T5（过强；R3 的残留）。`Openness` 与 `Premises` 的模块说明说，静止的世界中曾经活跃或立着的“只有有限多”。
    - `rest_few` 给出的是“不是无界多”。章节与记录写的是后者。
    - 若把“存在一个列表”作为 `few_of_quiet` 的结论，就蕴含 LPO（探针 `lpo_of_fewFinite`）。
  - T6（过强，轻微）。bounded-census-keeps-pace 的 next_delta 说“判据是比率”，但比率形式只是充分条件。
  - T7（出处；源自第十一次审查 R9(b)）。来源文件的更正说明说“生起”“止息”是 AI 在 P23c 中的译名。
    - 这两个译名自 P10、P19 起就在用。
    - P23c 只是用它们命名空间的部分。
  - T8（记账）。
    - 计划中 P30 一行没有回执（R11(b) 的残留）。
    - 提交的 `lean-index.json` 列入了另一会话未跟踪的草稿文件。
- **R1–R11 的处理。** R1、R2、R4、R5、R6、R7、R10 关闭。R3、R8、R9、R11 关闭，各留一处残留，分别是 T5、T4、T7、T8。

**Summary (English).**

- **The mechanical checks pass.**
  - The 29 modules of the core closure recompile from the prelude outside the repository. They exit 0 with no warnings.
  - All 1896 source declarations have empty axiom reports. Counted as the eleventh review counted, 1171 of them are theorems.
  - The closure has 5333 constants. Exactly 35 depend on an axiom, and they equal the receipt's list:
    - all are generated `injEq` lemmas, and all depend only on `propext`;
    - `World.Hatch.Relatum.ground.injEq` replaces the pre-rename `World.Brood…` lemma.
  - Receipt `20261009T185557.684339Z` covers 27 package modules, 1131 theorems and 1826 declaration audits. Its 42 source hashes, both checker hashes and the 258 retained artifacts match. Each of the three commits' receipts matches that commit's sources and checker.
  - Periphery receipt `20261009T185801.898161Z`: 33 source hashes, 3 checker hashes and 74 artifacts match. The periphery was not rebuilt.
    - `170422` and `184936` passed.
    - `173348` failed, as the P31 commit message says: the sources were edited during the run, so only a snapshot was checked.
  - The 32 records changed since `0cf14b8b` carry 402 reference hashes and 112 proof bindings, all of which match. Every record stamp is at or before its commit: the latest is 19:00:38Z, against a commit at 19:04:31Z.
  - The counts per phase match the receipts.
    - Theorems go 1086 → 1091 → 1109 → 1131, and declaration audits go 1760 → 1771 → 1793 → 1826.
    - The intermediate run `172715` (1106/1790) is superseded, and this is disclosed.
    - All 26 per-module counts in chapter §9 equal the receipt, and the spine sums to 1131.
  - None of the 1155 links has a bad anchor.
  - There is one naming fault (T1).
    - Of 566 aliases, 523 resolve in the core. The other 43 are the 41 non-core aliases the eleventh review listed, plus P30's `Becoming.World.slow` and `Becoming.World.slow_world`.
    - Of 1567 declaration names in the records' references, 90 do not resolve. 84 are the same non-core names as before, and 6 are P30's.
- **The mathematics is accepted.** No Lean statement is wrong.
  - P30: the balance read of recurrence is exact, and the two laws are re-proved through it with their statements unchanged.
    - `ceasing_of_returning`, `CountedBy.arising_iff_ceasing` and `slow_world` are the eleventh review's `ceasing_of_coming_often`, `arising_iff_ceasing_often` and `paced_world`. This answers R6.
    - `ceasing_of_outpacing` is sufficient only, as the body says.
  - P31: `chainEnd`, `chain_ends`, `chainEnd_zero` and `Cascade` are correct, and the bound is attained. `chain_ends_of_em` takes excluded middle as a hypothesis, not as an axiom.
  - P29b: `law_of_em`, `law_iff_em`, `Dependent.ceases_below`, `seedbank_world`, `hatch_*`, `holding_world`, `Finite.census_bounded`, `few_of_quiet` and `rest_few` are correct.
  - The probes are 55 source declarations, 38 of them theorems. None of their 107 constants depends on any axiom.
- **Eight findings (T1–T8).** There are three errors (one of naming, one in prose, one in a docstring), three overclaims, and two findings of presentation and bookkeeping. T2, T1 and T3 matter most.
  - **T2 (overclaim, unstated hypothesis).** The chain theorems need an infinite chain, and the texts do not say so.
    - The hypothesis `bears` of `Carries.chain_ends` and `chain_ends_of_em` asks, for every natural number k, that link k+1 depend on link k. So every link must have a further link depending on it.
    - In a finite web without a cycle of dependence, such as any food chain, no sequence meets this. Both theorems are vacuous there (probes `no_chain`, `Short.short`).
    - Study §41 rebuttal 3 and the English P31 paragraph say "the bound holds along any chain reaching a relatum".
    - Chapter §2 and the glossary set the result beside `coextinct`, whose chains are finite (`Reach`).
    - The same induction gives the finite form (probe `chain_ends_upto`), and the committed form is an instance of it.
  - **T1 (error, naming).** `Openness.lean` opens `namespace World` inside an already open `namespace World` (lines 389 and 434).
    - So P30's world is `Becoming.World.World.slow`, and its theorem is `World.World.slow_world`.
    - The chapter, the study, the plan, two Lean docstrings, and the aliases and references of record bounded-census-keeps-pace all cite `World.slow_world`. That name does not exist.
    - P32 (`df340093`) still has the doubled namespace.
  - **T3 (error, prose).** Study §41 and the English P31 paragraph say that turning "active only finitely often" into an end step "needs Markov's principle".
    - The step implies LPO, even when activity is decided and happens at most once (probe `lpo_of_endStep`).
    - Markov's principle does not prove LPO.
- **The rest.**
  - T4 (error in a docstring; residue of R8). `holding_world`'s docstring says that openness is necessary under a census, "with whatever arises embodied", balance and dissipation.
    - `arising_opens` needs every relatum embodied.
    - `kindling` meets the docstring's premises, is enclosed at every step, and arises without end (probe `kindling_docstring`).
  - T5 (overclaim; residue of R3). The module docs of `Openness` and `Premises` say that in a world at rest "only finitely many" relata are ever active or stand.
    - `rest_few` gives "not unboundedly many", which is what the chapter and the records say.
    - The "finitely many" form of `few_of_quiet`, in which some list holds them all, implies LPO (probe `lpo_of_fewFinite`).
  - T6 (overclaim, minor). The next_delta of bounded-census-keeps-pace says "what decides is the rate". The rate form is sufficient only.
  - T7 (provenance; from the eleventh review's R9(b)). The correction note in the source file dates 生起/止息 to P23c.
    - The AI used these renderings from P10 and P19.
    - P23c used them to name the parts of the space.
  - T8 (bookkeeping).
    - The plan row for P30 cites no receipt (residue of R11(b)).
    - The committed `lean-index.json` lists another session's untracked draft files.
- **R1–R11.** R1, R2, R4, R5, R6, R7 and R10 are closed. R3, R8, R9 and R11 are closed with one residue each: T5, T4, T7 and T8.

## 0. Scope, materials and method

**Object.** The object is `main` at `a93262028e30d9014d0820524ace14a3c5204e43`, through three commits (times UTC, 2026-10-09):

- `e448c56b` (P30), 17:14:43Z. Recurrence laws from the census balance, and growing bounds.
- `62beb5c0` (P31), 18:54:24Z. Lagged coextinction along chains of dependence.
- `a9326202` (P29b), 19:04:31Z. Integration of the eleventh review (R1–R11).

`df340093` (P32) landed on `main` during this review. It is not part of the object and was not reviewed. I checked with `git show` that:
- its `Openness.lean` still has the inner `namespace World` (T1);
- its `Reserve.lean` still has no finite chain form (T2).

**Isolation.**
- The object was exported with `git archive a9326202 | tar -x` into `review12/tree/` and read from there.
- No file under `/Users/ren/theories` was edited, and no state-changing git command was run.
- The live tree's uncommitted files belong to another session and were neither reviewed nor touched. They are `CONTINUATION-GROUNDING-PLAN.md`, `development/continuation-grounding-sketch/`, the 2026-10-10 source file, and a paragraph in `RESEARCH-DIRECTIVES.md`.
- One Lean process ran at a time.

**Materials.** Each sha256 prefix equals that of `git show a9326202:<path>`.

| File | sha256 | Lines |
|---|---|---:|
| `Becoming/Change.lean` | `02cdbffe26cc1aa8` | 554 |
| `Becoming/Population.lean` | `2afe5706600f97b2` | 860 |
| `Becoming/Roles.lean` | `42c42c015abaf468` | 1540 |
| `Becoming/Reserve.lean` | `173d7bf397117fe0` | 843 |
| `Becoming/Space.lean` | `05b633bd26c2910a` | 1033 |
| `Becoming/Premises.lean` | `fb05cc2e431b85ae` | 1025 |
| `Becoming/Openness.lean` | `456bfd6a84f68141` | 977 |
| `lean/becoming/README.md` | `0046dbd240e88f80` | 99 |
| `theories/becoming/chapters/THE-THEORY-OF-BECOMING.md` | `b98b27db0f184236` | 727 |
| `theories/becoming/chapters/BECOMING-FOUNDATION.md` | `cc39142fcdad952f` | 140 |
| `BECOMING-RENEWAL-READING.md` (study) | `aae8691838fb0261` | 2870 |
| `BECOMING-UNIFICATION-PLAN.md` | `349d5ad721c67bc1` | 285 |
| record `bounded-census-keeps-pace.json` | `d2dad22df9669045` | 491 |
| record `reserve-defers-ending.json` | `caa32b5c099107ab` | 493 |
| record `continued-change-needs-openness.json` | `1c28f2ae0d2d0983` | 610 |
| `sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md` | `a2c4030202ca041e` | 25 |
| receipt `becoming-checks/20261009T185557.684339Z/verification.json` | `5e52e607c018edf0` | 13709 |

**Read in full.**
- The diffs of the three commits in the seven Lean modules above, and the declarations they add or change.
- In the chapter: items 3, 4 and 10 (zh and en), §2, §8 (Ren's choices and the logical commitment), §9 and the glossary.
- In the study: §40–§42, and the English P30, P31 and P29b paragraphs.
- Plan rows P30, P31 and P29b, zh and en.
- The claim, limitations, next_delta, aliases and references of four records: bounded-census-keeps-pace, census-balance, reserve-defers-ending and continued-change-needs-openness.
- The source file.
- The eleventh review's findings R1–R11, and its §1.

**Read in part.**
- The other changed records: titles, claims, history and validation fields.
- The module README and BECOMING-FOUNDATION.
- `check_becoming.py`, for the counts and the closure.
- `tools/research/lean_catalogue.py`, for how it discovers files.

**Ren's words read**, for provenance:
- the source file above;
- Ren's sentence as quoted in the module doc of `Space.lean`;
- chapter §8;
- the study's citations of Ren's instruction ("aim a complete theory of becoming, and finish related work").

No external literature was read.

**Recompilation.**
- Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's `compile_order`, one process at a time.
- `GenerativeCore` was compiled with its `import Std` line removed, as the checker does. Every other file is byte-identical to the object.
- The bridge and the periphery were not rebuilt. Their bytes and receipts were checked.

**Checks.**

- **Receipt.**
  - The receipt is `passed`, with `core_compiles_from_prelude: true` and `source_unchanged_during_check: true`. It has 29 closure modules and 27 spine modules.
  - All 42 `source_sha256` entries and both checker hashes equal the object.
  - The retained run's 258 artifacts match their hashes, and its `verification.json` is byte-identical to the receipt.
  - The receipts `170233` (P30, 1091/1771) and `184816` (P31, 1109/1793) match their own commits' sources and checker.
- **Counts.**
  - All 26 numeric rows of the chapter §9 table were compared with the receipt by script, and each equals the receipt's `theorems` for that module. Examples: Change 46, Population 62, Roles 136, Reserve 59, Space 54, Premises 49, Openness 64.
  - The spine sums to 1131.
  - Study §40–§42, the English paragraphs and the plan give 1091/1771, 1109/1793 and 1131/1826.
- **Records.**
  - `check_records.py` re-hashed the 402 `references` of the 32 records changed in `0cf14b8b..a9326202` against the exported files.
  - It resolved the JSON pointers of the 112 proof bindings to the bound receipts, each `passed` with matching source hashes.
  - In each of the three commits, every changed record's `reviewed_at_utc` is at or before the commit time.
  - Many records keep an older `reviewed_at_utc` while their validation is re-pointed to the new receipts. That is the house convention.
- **Names.** `Names12.lean` (`f6fd75a82aff56cd…`) imports `Becoming` and checks `env.contains` for the 566 aliases and the 1567 reference declaration names of the changed records (T1).
- **Axioms.**
  - `CoreAudit.lean` (`095cc75cfd9ed8f7…`) has 1896 `#print axioms` lines generated from the receipt. All report "does not depend on any axioms".
  - `EnvAudit.lean` (`420f85b14528ce05…`) is byte-identical to the eleventh review's. Its per-module constant counts equal the receipt's `core_closure_constants`, 5333 in all, and exactly the 35 listed `injEq` lemmas depend on `propext`.
- **Links.** `anchors.py` resolved the 1155 Markdown links in the chapter, foundation, study, plan, README and changed records. None points to a bad file or anchor.

**Probes.**

- There is one file, `Review12.lean` (`ee79342984f15691…`, 390 lines). It imports the unchanged `Becoming` and compiles with exit 0 and no output.
- It has 55 source declarations in six groups, P1–P6:
  - 38 theorems;
  - 13 definitions, one of them an `abbrev`;
  - 4 `example`s.
- It is term mode only, with no tactic block and no `sorry`. Impossible cases use `nomatch`, and Boolean case splits use exhaustive patterns.
- The probes are theorems over the published definitions, or small webs and worlds that satisfy those definitions unchanged.
- Following the nondual method, they show what the definitions admit, not what actual systems do. A probe refutes a sentence only where the sentence claims more than the definitions give.

| Probe | Shows | Finding |
|---|---|---|
| P1 `chain_ends_upto`, `chain_ends_of_upto` | The per-link bound for a chain of `n` links, with `embodied` and `bears` asked only below `n`, by the same induction as `chain_ends`. The committed form is an instance of it. | T2 |
| P2 `climbs`, `no_chain`, `Short.*` | Where every dependence climbs a rank bounded by `K`, no sequence meets `bears`, for any `T`. In `Cascade` cut to three relata, the finite form gives relatum 2 inactive from `chainEnd 2 = 3`, and the bound is attained (relatum 2 is active at step 2). No sequence meets the committed hypothesis. | T2 |
| P3 `clear`, `Once.*`, `EndStep`, `lpo_of_endStep` | One formation that is never supported, with a carried reserve, active exactly at the first `true` of a Boolean sequence. Its activity is decided and happens at most once, and `active_finitely` applies. If every such web had an end step, LPO would hold. | T3 |
| P4 `Few.*`, `FewFinite`, `lpo_of_fewFinite` | A determination listed at each step by a list of at most one member, coming to hold at most once. If `few_of_quiet` gave a list holding every member that ever holds, LPO would hold. | T5 |
| P5 `kindling_docstring` | `kindling` is counted, whatever arises in it is embodied, it balances and dissipates, every step is enclosed, and arising recurs; yet not every relatum is embodied. | T4 |
| P6 four `example`s | The names Lean records are `Becoming.World.World.slow_world`, `World.World.slow`, `World.Slow.census` and `World.Slow.grows_between`. | T1 |

**Severity labels** are those of the ninth to eleventh reviews:

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose says more than the Lean, including where a premise is left out or a reading is presented as settled.
- *missing counterexample*: a relevant witness is absent, or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

No Lean statement is wrong. The three errors are:
- a namespace slip that leaves every citation of P30's world unresolvable (T1);
- a false sentence in prose (T3);
- a false docstring (T4).

The Lean these three concern is correct.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. Build, axioms, receipts, hashes, artifacts, bindings, counts, stamps | **Correct.** 29 modules compile from the prelude, with 1896 empty axiom reports. 35 generated `injEq` lemmas depend on `propext`, as listed. 42 + 33 source hashes, 258 + 74 artifacts, 402 reference hashes and 112 bindings match. Counts go 1086 → 1091 → 1109 → 1131 and 1760 → 1771 → 1793 → 1826. §9 equals the receipt. No stamp is later than its commit. | — |
| 2. Names and aliases | **One fault.** P30's world and its lemmas live under `Becoming.World.World` and `Becoming.World.Slow`, so every citation and two aliases miss. The other unresolved names are the non-core ones known since the tenth review. | T1 |
| 3. P30: balance exactness (`ceasing_iff_shortfall`, `coming_iff_excess`, `recurring_accumulates`; `coming_of_ceasing` and `ceasing_of_coming` re-proved) | **Correct.** Both equivalences are the census balance read of recurrence. The six removed lemmas are proof steps. Their statements and checks are kept in receipt `163512`, retained in `becoming-checks/`, and in the history, as §40 says. The two laws keep their statements. | — |
| 4. P30: growing bounds (`ceasing_of_returning`, `CountedBy`, `CountedBy.arising_iff_ceasing`, `slow_world`, `ceasing_of_outpacing`) | **Correct, and R6 is answered.** `slow_world` needs a non-decreasing, unbounded bound, as stated. §40 rebuttal 4 rightly leaves the non-monotone case unconstructed without a modulus. The next_delta overstates the rate. | T1, T6 |
| 5. P30: `Web.DependenceCensus.over_stretch` | **Correct**, with `requires` decided in the signature. This answers R11(a). | — |
| 6. P31: `chainEnd`, `chainEnd_ge`, `chainEnd_zero`, `Carries.chain_ends`, `Cascade` | **Correct as stated, and the bound is attained.** The hypothesis needs an infinite chain, which the texts do not say. The graph sentence says more than any stated form. | T2 |
| 7. P31: `chain_ends_of_em`, `exists_not_of_em` | **Correct.** Excluded middle is a hypothesis, and the core stays axiom-free. The stated reason for needing it is wrong. | T2, T3 |
| 8. P29b: new declarations (`stays_failing`, `persists_of_em`, `Dependent.ceases_below`, `quiet_of_once`, `Seedbank`, `law_of_em`, `law_iff_em`, `listed_of_ever`, `counted_of_ever`, `World.Hatch`, `hatch_ever`, `hatch_idle`, `hatch_rests`, `holding_world`, `Finite.census_bounded`, `Listed.few_of_quiet`, `few_active`, `rest_few`) | **Correct as stated.** `law_of_em` gives both directions with no decidability, and `law_iff_em` is an equivalence over all finite worlds. One new docstring is false, and two module docs say "finitely many" for `rest_few`. | T4, T5 |
| 9. P29b: are R1–R11 fixed everywhere, zh and en? | **Yes, with four residues.** See the table below. | T4, T5, T7, T8 |
| 10. Ren's words and AI elaboration | **Kept apart.** Ren's sentence is quoted verbatim or glossed as a tag question. Ren's confirmation is of the English pair, and the Chinese pair is marked as the AI's. §8 asks Ren about the context of the reply. The dating of the Chinese rendering is wrong. | T7 |
| 11. Overclaims, stale references, anchors | **Anchors resolve.** Four phrasings say more than the Lean: the chain hypothesis, the logical strength of the end step, "finitely many", and "what decides is the rate". | T2, T3, T5, T6 |

**Status of R1–R11.**

| Item | Status | Evidence |
|---|---|---|
| R1 | closed | `Dependent.ceases_below` (Roles) states the ending with activity at the step. `inactive_below` is glossed as "inactive after the step" in Roles, Space, chapter item 10, §8 and the scope text. |
| R2 | closed | `World.law_iff_em` and `law_of_em` are in `Space`, axiom-free. Study §38 and the English P25b paragraph are corrected in place. |
| R3 | closed, one residue | The chapter, glossary 699, the records and `rest_few`'s docstring say "not unboundedly many". `listed_of_ever`, `counted_of_ever`, `hatch_ever` and `hatch_idle` are in the core, and the `Binds` docstring says what the census field asks. The module docs of `Openness` (11–13, 75–79) and `Premises` (47–50) still say "only finitely many" (T5). |
| R4 | closed | The title of continued-change-needs-openness now reads "finitely many standing and finitely many active at each step (censuses of both)". |
| R5 | closed | Population and the records say "arising recurs exactly when ceasing recurs". |
| R6 | closed by P30 | `ceasing_of_returning`, `CountedBy.arising_iff_ceasing` and `slow_world` answer the record's open item. Their names are wrong (T1). |
| R7 | closed | `Finite.census_bounded` is added, and the gloss of `Finite.countedWithin` is narrowed. |
| R8 | closed, one residue | `holding_world` is added, with "one such world". The docstring of `holding_world` itself states `arising_opens` with too weak a premise (T4). |
| R9 | closed, one residue | (a) Ren's sentence is quoted verbatim or glossed as a tag question in `Space`, the records and the plan. (b) The Chinese pair is marked as the AI's rendering in the chapter (541), the study (2868) and the source note, but the note dates it to P23c (T7). (c) The context of the reply is in the source note, and §8 asks Ren. |
| R10 | closed | `World.Brood` is renamed `World.Hatch`. Roles' `Brood` is unchanged and still cited correctly: chapter 271 and 275, generation-is-replenishment, life-as-condition-of-life and living-on-and-descent. Historical receipt descriptions ("Premises adds brood") are left as history. |
| R11 | closed, one residue | (a) `DependenceCensus.over_stretch` is stated. (b) Count lines are added, and plan rows P25b and P29 cite receipts, but the P30 row cites none (T8). (c) §2 now says "tends to infinity". (d) No action was needed. |

## 2. Findings

### T1. error (naming): P30's world is `World.World.slow`

**Location.**

- `Becoming/Openness.lean` nests a second `namespace World` inside the first:
  - line 389 opens `namespace World`, for `procession`;
  - line 409 opens `namespace Slow`, which closes at 432;
  - line 434 opens `namespace World` again, which closes at 458;
  - the outer `World` closes at 580.
  The P30 commit introduced this, at its lines 367, 387 and 412.
- Lean therefore records these names:
  - `Becoming.World.Slow.{web, length, census, grows_between}`;
  - `Becoming.World.World.{slow, slow_decided, slow_world}`.
  The receipt's declaration list, the generated `lean-index.json` and `lean-declarations/core.md` all show them, and probe P6 elaborates them.
- These places cite names that do not exist:
  - chapter item 4 (zh 76, en 108) and glossary 672 cite `World.slow_world`;
  - study §40 (2398–2399 and 2419), §42 (2526) and the English P30 paragraph (2854);
  - plan rows 249 and 280;
  - the docstrings at `Population.lean:451` and `Openness.lean:44`;
  - record bounded-census-keeps-pace:
    - aliases `Becoming.World.slow` and `Becoming.World.slow_world`;
    - references `Becoming.World.slow`, `Becoming.World.slow_world`, `Becoming.Slow.web`, `Becoming.Slow.length`, `Becoming.Slow.census` and `Becoming.Slow.grows_between`;
    - its claim and next_delta.

**Why it matters.**
- Aliases are how readers, and `make research-find`, move from a claim to its Lean. `#check Becoming.World.slow_world` fails.
- Nothing in the receipts or the record validation catches this. Reference hashes and proof bindings are checked per file, and alias resolution was checked here only by `Names12.lean`.
- The P30 code itself compiles, because inside the doubled namespace `Slow.census` and `slow` resolve locally.
- At `df340093` the inner `namespace World` is still there.

**Correction.**
- Delete the inner `namespace World` (line 434) and its `end World` (line 458).
- Move the `namespace Slow … end Slow` block (lines 409–432) above line 389, beside `Dawn` and `Procession`.
- The names then become `Becoming.Slow.*` and `Becoming.World.{slow, slow_decided, slow_world}`, which is what every text and the record already say. Recheck and re-point the receipts.
- Add a resolution step for core names to the record checks: an `env.contains` audit like `Names12.lean`, reporting non-core names separately.

### T2. overclaim (unstated hypothesis): the chain theorems need an infinite chain

**Location.**

- `Becoming/Reserve.lean` 315–355. `Carries.chain_ends` and `Carries.chain_ends_of_em` take `chain : Nat → X` with two hypotheses:
  - `bears : ∀ k t, T ≤ t → W.requires t (chain (k + 1)) (chain k) ∧ 0 < W.need t (chain (k + 1)) (chain k)`;
  - `embodied : ∀ k, W.Embodied (chain k)`.
  The docstrings say "where each relatum of a chain depends at a positive need on the one before it".
- Study §41 rebuttal 3 (2486): "一个关系项依存于几个条件时，任一个所需不被满足都使它不被支持；所以沿到达它的任一条链，界都成立：图上的每个关系项在到达它的某条链的 `chainEnd` 之后终结".
- English P31 paragraph (2858): "Along a graph rather than a chain, the bound holds along any chain reaching a relatum".
- Other texts that state the result without the hypothesis:
  - chapter §2: zh 197 "储备衰减时共灭沿依存之链逐环有界"; en 209 "coextinction runs down a chain of dependence within a bound at each link";
  - chapter §8, zh 507;
  - glossary 685, which puts `chain_ends` beside `coextinct` ("终结每个依存链……到达它的形成");
  - README 40;
  - plan row 250, and the English list at 281.
- Record reserve-defers-ending:
  - claim: "where the relata of a chain are embodied, each depends … on the one before it";
  - limitations: "the chain is a sequence, and the form taking the least bound over the chains of a graph is not stated";
  - next_delta: "the least bound over the chains of a graph".

**What the Lean says, with probes P1 and P2.**

- `bears` is asked for every `k : Nat`, so a chain meeting it never stops. Link `k + 1` depends on link `k` for every `k`, so every link has a further link depending on it. `Cascade`, the witness, has infinitely many relata, as it must.
- In a finite web, a sequence meeting `bears` must revisit a relatum. So it needs a cycle of dependence reachable upward from `chain 0`. (This is a pigeonhole hand argument; it is not formalized.)
- Probe `no_chain`: wherever every dependence climbs a rank bounded by `K`, no sequence meets `bears`, for any `T`. Every finite web without a cycle of dependence has such a rank. Both theorems are then vacuous. A plant, a herbivore and a predator form such a web.
- Probe `Short.short` uses `Cascade` cut to three relata, in which relatum `x + 1` depends on `x` only for `x + 1 ≤ 2`.
  - It carries and decays the same reserve, and every relatum is embodied.
  - The finite form gives relatum 2 inactive from step `chainEnd 2 = 3`. The bound is attained, since relatum 2 is active at step 2.
  - No sequence meets the committed `bears`.
- Probe `chain_ends_upto` asks `embodied` and `bears` only for `k < n` and concludes for `k ≤ n`, by the same induction line for line. `chain_ends_of_upto` derives the committed theorem from it, so nothing is lost.
- `coextinct` (Roles 455) is stated over `Reach (W.bearing t) g y`, that is, over finite paths. The finite form, not the committed one, is its lagged analogue.

**Why it matters.**
- The cases the texts give as motivation are all finite chains: a fox on a hare, food chains, seed banks, savings.
- As stated, P31's main theorem applies to none of them.
- The graph sentence asserts a result for finite chains that no theorem states.
- Rebuttal 3's argument is itself sound for finite chains: it is exactly the induction of the finite form.

**Correction.**
- In Lean, state the finite form: P1's `chain_ends_upto`, and the same change for `chain_ends_of_em`. Derive the infinite form as an instance.
- Or state it along `Reach (W.bearing t)` paths, as `coextinct` is, with the bound the sum along the path.
- Until one of these is stated, change the texts:
  - In the docstrings, chapter, glossary, README, plan, study and record, say "along an infinite chain of dependence (each link depended on by the next)".
  - Add to the limitations: "finite chains, such as a food chain, are not covered; in a finite web the hypothesis needs a cycle of dependence".
  - Mark rebuttal 3 and the English sentence in place: "the bound along each finite chain reaching it follows by the same induction (not stated)". Or cite the finite form once it is stated.

### T3. error (in prose): "needs Markov's principle"

**Location.**
- Study §41 (2478): "在构造的逻辑中“不复现”不能化为终结之步（这需要马尔可夫原则）".
- English P31 paragraph (2858): "turning “only finitely often” into an end step needs Markov's principle".
- No record or chapter text repeats it.

**What the Lean says, with probe P3.**

- The step in question goes:
  - from `¬ ∀ N, ∃ t, N ≤ t ∧ W.active t f`, which `Carries.active_finitely` gives;
  - to `∃ E, ∀ t, E ≤ t → ¬ W.active t f`, an end step.
- `Once.web s` is a web with one formation, built to meet the step's hypotheses:
  - It is never supported: it needs one unit of a condition whose level is zero.
  - It is active exactly at the first `t` with `s t = true`.
  - Its reserve is 1 until then and 0 after, and it carries (`Once.carries`).
  - Its activity is decided (`Once.decided`) and happens at most once (`Once.once`).
  - `active_finitely` applies to it (`Once.finitely`).
  - It does not decay: the reserve stays 1 while the formation is dormant.
- `lpo_of_endStep` says: if every such web has an end step, then LPO holds. That is, for every `s : Nat → Bool`, `(∃ n, s n = true) ∨ ∀ n, s n = false`. The proof is axiom-free. Here "such a web" means one formation, decided activity, a carried reserve, and never supported.
- Markov's principle does not prove LPO. This is a standard fact, not formalized here: in Kleene's number realizability, Markov's principle is realized and LPO is not (see e.g. Troelstra and van Dalen, *Constructivism in Mathematics* I, ch. 4).
- So the end step needs at least LPO, and Markov's principle does not suffice. Excluded middle suffices, as `chain_ends_of_em` uses it. The exact strength of the step was not determined.

**Correction.** Mark both places in place.
- zh: "（这一步不是构造性的：即使活动可判定且至多发生一次，它也蕴含 LPO，马尔可夫原则不够）".
- en: "turning 'only finitely often' into an end step is not constructive: even for decided activity happening at most once it implies LPO, which Markov's principle does not give".

Rebuttal 5 says that the one non-constructive step is this conversion. That sentence stands.

### T4. error (in a docstring; residue of R8): `holding_world`'s gloss of `arising_opens`

**Location.** `Becoming/Openness.lean` 849–852, the docstring of `World.holding_world`: "Under a census, with whatever arises embodied, balance and dissipation, openness is necessary for arising without end (`arising_opens`), not sufficient."

**What the Lean says, with probe P5.**

- `World.arising_opens` (line 575) takes `embodied : w.Embodied`, every relatum embodied. It does not take `ArisingEmbodied`.
- Probe `kindling_docstring` shows that `kindling`:
  - is counted, `ArisingEmbodied`, balanced and dissipative;
  - has every step enclosed;
  - has arising recurring;
  - does not have every relatum embodied, because unburnt fuel stands without acting.
- Every ingredient of the probe is already in `World.rest_needs_standing`. The probe only reads `Around` as `Enclosed` and adds the last conjunct.
- So the docstring's sentence is false.
- Every other statement of the sentence that I checked says "every relatum embodied" or "the eight", and is correct: chapter en 108 and zh 510, foundation 76, README 44, plan 273, and the counterexample in continued-change-needs-openness.

**Correction.** Replace the docstring with: "Under a census, with every relatum embodied, balance and dissipation, openness is necessary for arising without end (`arising_opens`), not sufficient. With only whatever arises embodied it is not necessary: `kindling` is enclosed at every step and arises without end (`rest_needs_standing`)."

### T5. overclaim (residue of R3): "only finitely many" for "not unboundedly many"

**Location.**

- `Becoming/Openness.lean` 11–13, module doc: "In a world that comes to rest so, only finitely many relata ever stand or are active (`World.rest_few`)".
- `Becoming/Openness.lean` 75–79: "So in every world that comes to rest under the rest theorem, only finitely many relata are ever active and only finitely many ever stand (`World.rest_few`); conversely, where finitely many are ever active and activity is decided, a census exists (`World.counted_of_ever`)".
- `Becoming/Premises.lean` 47–50: "In every world that comes to rest under the rest theorem, only finitely many relata are ever active or stand (`World.rest_few` in `Becoming.Openness`), so there a census binds only so."
- The eleventh review's own §1, row 3, used the loose phrase.
- The chapter (§2, glossary 699), the records and `rest_few`'s docstring say "not unboundedly many", and are correct.

**What the Lean says, with probe P4.**

- `rest_few` and `few_of_quiet` conclude `¬ ∀ L, ∃ t x, … ∧ ¬ x ∈ L`. That is: not every list misses some member that ever holds.
- `counted_of_ever`, the "converse", assumes `∃ L, ∀ t x, active t x → x ∈ L`: some list holds every member ever active. That is "finitely many" in the strong sense.
- Probe `lpo_of_fewFinite` shows that the strong form of `few_of_quiet` would give LPO.
  - The strong form says: for every determination that is decided, listed at each step, and whose coming to hold does not recur, there is a list `L` with `∀ t a, p a t → a ∈ L`.
  - The determination used is "being the first `true` of `s`, before step `t`". It is listed by a list of at most one member, and it comes to hold at most once.
  - I did not build a world-level witness. `rest_few` is proved from `few_of_quiet`, so the gap there is the same in kind.
- So the module docs pair a weak conclusion with a converse that needs the strong one.
- The two forms coincide with excluded middle. The core's logical commitment (chapter §8, lines 550 and 557) keeps them apart.

**Correction.**
- Write "not unboundedly many" in the three places.
- In `Openness.lean` 78–79: "conversely, where some list holds every relatum ever active and activity is decided, a census exists (`World.counted_of_ever`)".
- In `Premises.lean`: "…not unboundedly many relata are ever active or stand…".
- Optionally, state the strong form with excluded middle as a hypothesis, as `law_of_em` does.

### T6. overclaim (minor): "what decides is the rate"

**Location.** Record bounded-census-keeps-pace, next_delta:
- zh: "判据是比率（Listed.ceasing_of_outpacing），精确地是缺额（Listed.ceasing_iff_shortfall）";
- en: "what decides is the rate (Listed.ceasing_of_outpacing), exactly the shortfall (Listed.ceasing_iff_shortfall)".

**What the Lean says.**
- `ceasing_iff_shortfall` is the exact criterion.
- `ceasing_of_outpacing` is sufficient only. `slow` never meets it, and the lists can stay far below `B`.
- The record's claim, study §40 ("这是充分条件，不是必要条件") and the English paragraph all say so. Only next_delta says the rate decides.

**Correction.**
- zh: "精确的判据是缺额（Listed.ceasing_iff_shortfall）；比率形式（Listed.ceasing_of_outpacing）是充分条件，slow 中从不满足".
- en: "the exact criterion is the shortfall (Listed.ceasing_iff_shortfall); the rate form (Listed.ceasing_of_outpacing) is sufficient, and slow never meets it".

The limitation "no corresponding world is given (its construction needs data from existence)" is accurate, and no change is needed. A hand argument, not formalized, would make it sharper:
- If a modulus of divergence is supplied as data, one can build a non-decreasing, unbounded lower bound, and so a `slow` world under it.
- Without such a modulus, this cannot be done in general.
- So the modulus is the missing data.

### T7. presentation (provenance; from the eleventh review's R9(b)): when 生起/止息 entered

**Location.**
- `sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md`, correction note (line 5): "中文的“生起”“止息”是 AI 在 P23c 中的译名".
- The eleventh review, BECOMING-P25B-P29-REVIEW.md line 476: "The Chinese terms 生起/止息 are the AI's, from P23c."

**Evidence.**
- The AI used 生起 from P10 (`5669f67d`, section "继续生成：生起、不息与更新", 48 diff lines).
- It used 止息 from P19 (`4295dd24`, "生起复现恰当止息复现", 34 diff lines).
- P23c used them to name the parts of the space: `World.ArisingRecurs` and `World.CeasingRecurs`.
- The substance of the note is right: the Chinese pair is the AI's, not words Ren confirmed. Ren's quotation and the AI note are unchanged, as the note says.

**Correction.** Change the note to: "中文的“生起”“止息”是 AI 的译名（P10、P19 起用于本理论，P23c 起用于命名空间的部分），不是 Ren 确认的用语". The eleventh review is an evidence artifact and should not be edited; this report records the erratum to its R9(b).

### T8. presentation (bookkeeping)

- **(a) The plan row for P30 cites no receipt.**
  - Plan row 249 ends "核心与外围检查通过；见研究 §40".
  - Rows P25b, P29, P31 and P29b now cite their receipts, as R11(b) asked.
  - Add "回执 20261009T170233.740799Z；外围 20261009T170422.519028Z".
- **(b) The committed index lists untracked files.** Low severity.
  - At `a9326202`, `theories/becoming/results/data/lean-index.json` lists three paths under `development/continuation-grounding-sketch/`: `Audit.lean`, `Continuation.lean` and its `README.md`. None of them is in the commit.
  - This is by design: `lean_catalogue.py` discovers files with `rg --files --hidden --no-ignore` and includes untracked files (its line 292).
  - As a result, a clean checkout of `a9326202` regenerates a different index.
  - Those files belong to another session's work and must not be touched to fix this.
  - Either exclude untracked paths from committed generated data, or regenerate the index after that work is committed.

## 3. What remains sound

- **The core.**
  - It compiles from the prelude, and every source declaration is axiom-free.
  - The only axiom-dependent constants are the 35 generated `injEq` lemmas that the receipt lists.
  - Excluded middle enters only as a hypothesis: in `law_of_em`, `law_iff_em`, `chain_ends_of_em`, `persists_of_em`, `quiet_of_once` and `exists_not_of_em`.
- **P30's single route.**
  - The census law and the bounded law follow from the balance by accumulation (`recurring_accumulates`), as the finite-family laws of §26 did.
  - The shortfall and excess equivalences are exact.
  - Removing the six list-length lemmas loses no stated result. The laws keep their statements, and the old statements stay checked in a retained receipt.
- **Growing bounds.**
  - The bound need only return within some number at arbitrarily late steps.
  - Any non-decreasing, unbounded bound, however slow, admits arising without ceasing (`slow_world`, under its real name).
  - The dichotomy for non-decreasing bounds is disclosed as classical.
- **Lagged coextinction.** Under a decaying reserve the per-link bound is correct:
  - it reads each reserve where the previous link ended, so replenishment while supported is counted;
  - it reduces to simultaneous coextinction at the zero reserve;
  - it is attained (`Cascade`);
  - its finite form follows by the same proof (P1).
- **P29b.**
  - `law_iff_em` closes R2 inside the pure core.
  - `Dependent.ceases_below` states exactly when an undermining is an ending.
  - `holding_world` shows that openness is not sufficient.
  - `hatch_idle` and `hatch_ever` disclose what the census binding amounts to.
  - The rename separates the two broods.
- **Provenance.** Ren's words and the AI's elaboration are kept apart.
  - Ren's sentence is quoted verbatim or glossed as a tag question presuming no overlap.
  - What Ren confirmed is the English pair.
  - §8 asks Ren, rather than reading the reply as settling the candidate.
  - Names remain marked as AI proposals for Ren to choose.
- **Bookkeeping.**
  - Receipts, artifacts, reference hashes, bindings, counts, stamps and anchors are consistent across the three commits.
  - Superseded and failed runs are retained and disclosed.

## 4. What would change the verdicts

- **The mathematics.** The verdict would change if a probe failed at the object, a hash did not match, or a declaration's statement differed from the receipt. None of these was found. "No Lean statement is wrong" holds for the statements as written. T2 is about their scope as presented, not about their truth.
- **T1** would be withdrawn if the texts and records were meant to cite `World.World.*`. They clearly are not: the record references `Becoming.Slow.*`, and every text writes `World.slow_world`.
- **T2.**
  - It would reduce to a wording fix once a finite-chain or `Reach` form is stated, or once every text says "infinite chain".
  - It would be withdrawn only if a finite chain could meet `bears`. P2 shows that none can, in any web whose dependence climbs a bounded rank.
- **T3.**
  - It would be withdrawn only if Markov's principle proved LPO, which fails in standard models.
  - If "Markov's principle" was meant loosely, as "a non-constructive principle", the fix is a matter of wording.
- **T4** stands as long as `arising_opens` needs `Embodied`. It cannot be weakened to `ArisingEmbodied`: `kindling` refutes that version.
- **T5** would become a note if Ren chose to read the theory classically, with excluded middle as an axiom. The current logical commitment (§8) does the opposite.
- **T6–T8** are wording and bookkeeping. None of them changes a result.
- **Ren's choices.** Two questions are Ren's to settle: whether the activity reading remains a candidate for Ren's "生成的／退化的", and the names. Nothing in this review depends on either.

## Appendix A. Probe source

`build/Review12.lean`, sha256 `ee79342984f156917263ae6e8bb76c0e68ebcb2bbf37f559e92cade3edea8731`.

- It was compiled as `LEAN_PATH=<build> lean +leanprover/lean4:v4.29.1 -o Review12.olean Review12.lean`.
- It exited 0, and the output file is empty (sha256 `e3b0c442…`).

```lean
import Becoming

/-!
# Probes of the twelfth independent review (P30, P31, P29b)

Term mode throughout; no tactic blocks. The axiom audit is in `Review12Audit.lean`.

* P1 `chain_ends_upto`: `Carries.chain_ends` for a finite chain of `n` links; the committed
  infinite form is its instance (`chain_ends_of_upto`).
* P2 `no_chain`, `Short.short`: in a web whose dependences climb a bounded rank (every
  finite acyclic web), no sequence satisfies the hypothesis `bears` of `chain_ends` and
  `chain_ends_of_em`; a three-link cascade where the finite form gives the attained bound
  and the committed form is vacuous.
* P3 `lpo_of_endStep`: turning "active only finitely often" (`active_finitely`) into an
  end step, for a single never-supported formation with a carried reserve, decided
  activity holding at most once, implies LPO.
* P4 `lpo_of_fewFinite`: the "finitely many" form (`∃ L`) of `Listed.few_of_quiet`
  implies LPO.
* P5 `kindling_docstring`: a counted world, whatever arises embodied, balanced and
  dissipative, every step enclosed, arising recurring; `holding_world`'s docstring says
  openness is necessary under exactly these premises.
* P6: the P30 names as Lean records them.
-/

namespace Review12

open Becoming

/-! ## Booleans -/

theorem bool_absurd {b : Bool} (f : b = false) (t : b = true) : False :=
  nomatch f.symm.trans t

theorem bool_false : ∀ b : Bool, (b = true → False) → b = false
  | false, _ => rfl
  | true, h => (h rfl).elim

theorem and_left : ∀ {b c : Bool}, (b && c) = true → b = true
  | true, _, _ => rfl
  | false, _, h => h

theorem and_right : ∀ {b c : Bool}, (b && c) = true → c = true
  | true, _, h => h
  | false, _, h => nomatch h

theorem and_both : ∀ (b c : Bool), b = true → c = true → (b && c) = true
  | true, true, _, _ => rfl
  | false, _, h, _ => nomatch h
  | true, false, _, h => nomatch h

theorem bool_cases : ∀ b : Bool, b = false ∨ b = true
  | false => .inl rfl
  | true => .inr rfl

theorem not_true : ∀ {b : Bool}, (!b) = true → b = false
  | false, _ => rfl
  | true, h => nomatch h

/-! ## P1. A finite chain -/

section Chains

variable {X : Type} {W : Web X X}

/-- `Carries.chain_ends` for a chain of `n` links: the hypotheses are asked only of the
links below `n`, and the conclusion is given for the relata up to `n`. -/
theorem chain_ends_upto {r : Nat → X → Nat} (carries : W.Carries r) (decays : W.Decays r)
    {chain : Nat → X} {n : Nat} (embodied : ∀ k, k < n → W.Embodied (chain k)) {T : Nat}
    (bears : ∀ k t, k < n → T ≤ t →
      W.requires t (chain (k + 1)) (chain k) ∧ 0 < W.need t (chain (k + 1)) (chain k))
    (ended : ∀ t, T ≤ t → ¬ W.active t (chain 0)) :
    ∀ k, k ≤ n → ∀ t, Web.chainEnd r chain T k ≤ t → ¬ W.active t (chain k)
  | 0, _ => ended
  | k + 1, le => fun _ later active =>
    have unsupported := Web.unsupported_after_end (embodied k le)
      (fun s from_ => bears k s le (Nat.le_trans (Web.chainEnd_ge r chain T k) from_))
      (chain_ends_upto carries decays embodied bears ended k (Nat.le_of_succ_le le))
    match le_dest later with
    | ⟨m, same⟩ => carries.ends_within decays unsupported (Nat.le_add_right _ m)
        (Eq.subst (motive := fun s => W.active s (chain (k + 1)))
          (same.trans (Nat.add_assoc _ _ m)) active)

/-- The committed infinite form is an instance of the finite one. -/
theorem chain_ends_of_upto {r : Nat → X → Nat} (carries : W.Carries r)
    (decays : W.Decays r) {chain : Nat → X} (embodied : ∀ k, W.Embodied (chain k)) {T : Nat}
    (bears : ∀ k t, T ≤ t →
      W.requires t (chain (k + 1)) (chain k) ∧ 0 < W.need t (chain (k + 1)) (chain k))
    (ended : ∀ t, T ≤ t → ¬ W.active t (chain 0)) :
    ∀ k t, Web.chainEnd r chain T k ≤ t → ¬ W.active t (chain k) :=
  fun k => chain_ends_upto carries decays (n := k) (fun j _ => embodied j)
    (fun j t _ later => bears j t later) ended k (Nat.le_refl k)

/-! ## P2. The committed hypothesis needs an infinite chain -/

theorem climbs {ρ : X → Nat} {chain : Nat → X}
    (up : ∀ k, ρ (chain k) < ρ (chain (k + 1))) : ∀ k, k ≤ ρ (chain k)
  | 0 => Nat.zero_le _
  | k + 1 => Nat.lt_of_le_of_lt (climbs up k) (up k)

/-- Where every dependence climbs a rank bounded by `K` (as in every finite web without a
cycle of dependence), no sequence satisfies `bears` of `Carries.chain_ends` and
`Carries.chain_ends_of_em`, for any `T`: both are vacuous there. -/
theorem no_chain {ρ : X → Nat} {K : Nat}
    (ranked : ∀ t g c, W.requires t g c → ρ c < ρ g ∧ ρ g ≤ K) {chain : Nat → X} {T : Nat}
    (bears : ∀ k t, T ≤ t →
      W.requires t (chain (k + 1)) (chain k) ∧ 0 < W.need t (chain (k + 1)) (chain k)) :
    False :=
  Nat.not_succ_le_self K (Nat.le_trans
    (climbs (fun k => (ranked T _ _ (bears k T (Nat.le_refl T)).1).1) (K + 1))
    (ranked T _ _ (bears K T (Nat.le_refl T)).1).2)

end Chains

/-! `Cascade` cut to three relata: relatum `x + 1` depends on relatum `x` only for
`x + 1 ≤ 2`. -/
namespace Short

def web : Web Nat Nat where
  level t x := Cascade.upto t x
  active t x := t ≤ x
  requires _ x c := x = c + 1 ∧ x ≤ 2
  need _ _ _ := 1
  draws _ _ _ := False

theorem unsupported {t x : Nat} (no : ¬ web.Supported t x) : ¬ Cascade.web.Supported t x :=
  fun supported => no fun c requires => supported c requires.1

theorem carries : web.Carries Cascade.reserve :=
  fun t x no => Cascade.carries t x (unsupported no)

theorem decays : web.Decays Cascade.reserve :=
  fun t x no => Cascade.decays t x (unsupported no)

theorem embodied (x : Nat) : web.Embodied x :=
  Cascade.embodied x

theorem ranked : ∀ t g c, web.requires t g c → c < g ∧ g ≤ 2 :=
  fun _ _ c requires =>
    ⟨Eq.subst (motive := fun g => c < g) requires.1.symm (Nat.lt_succ_self c), requires.2⟩

/-- In the three-link cascade the finite form gives that relatum `2` is not active from
step `chainEnd 2 = 3` on, attained since it is active at step `2`; no sequence satisfies
the committed `bears`. -/
theorem short :
    web.Carries Cascade.reserve ∧ web.Decays Cascade.reserve ∧ (∀ x, web.Embodied x) ∧
    (∀ t, 1 ≤ t → ¬ web.active t 0) ∧
    (∀ t, Web.chainEnd Cascade.reserve (fun k => k) 1 2 ≤ t → ¬ web.active t 2) ∧
    Web.chainEnd Cascade.reserve (fun k => k) 1 2 = 2 + 1 ∧ web.active 2 2 ∧
    ∀ (chain : Nat → Nat) (T : Nat), ¬ ∀ k t, T ≤ t →
      web.requires t (chain (k + 1)) (chain k) ∧ 0 < web.need t (chain (k + 1)) (chain k) :=
  ⟨carries, decays, embodied,
   fun _ later active => Nat.not_succ_le_zero 0 (Nat.le_trans later active),
   chain_ends_upto carries decays (chain := fun k => k) (n := 2) (fun k _ => embodied k)
     (fun _ _ lt _ => ⟨⟨rfl, lt⟩, Nat.zero_lt_one⟩)
     (fun _ later active => Nat.not_succ_le_zero 0 (Nat.le_trans later active))
     2 (Nat.le_refl 2),
   Cascade.ends 2, Nat.le_refl 2,
   fun _ _ bears => no_chain (ρ := fun x => x) (K := 2) ranked bears⟩

end Short

/-! ## The first `true` of a Boolean sequence -/

/-- No `true` before `t`. -/
def clear (s : Nat → Bool) : Nat → Bool
  | 0 => true
  | t + 1 => clear s t && !s t

theorem clear_le (s : Nat → Bool) {i : Nat} :
    ∀ {t}, i ≤ t → clear s t = true → clear s i = true
  | _, .refl, h => h
  | _ + 1, .step le, h => clear_le s le (and_left h)

theorem false_before (s : Nat → Bool) {t : Nat} (c : clear s t = true) {i : Nat}
    (lt : i < t) : s i = false :=
  not_true (and_right (clear_le s lt c))

theorem clear_or_first (s : Nat → Bool) :
    ∀ n, clear s n = true ∨ ∃ m, m < n ∧ clear s m = true ∧ s m = true
  | 0 => .inl rfl
  | n + 1 => match clear_or_first s n with
    | .inr ⟨m, lt, c, h⟩ => .inr ⟨m, Nat.lt_succ_of_lt lt, c, h⟩
    | .inl c => match bool_cases (s n) with
      | .inl f => .inl (and_both _ _ c (Eq.subst (motive := fun b => (!b) = true) f.symm rfl))
      | .inr h => .inr ⟨n, Nat.lt_succ_self n, c, h⟩

theorem first_of_true (s : Nat → Bool) {n : Nat} (h : s n = true) :
    ∃ m, clear s m = true ∧ s m = true :=
  match clear_or_first s n with
  | .inl c => ⟨n, c, h⟩
  | .inr ⟨m, _, c, hm⟩ => ⟨m, c, hm⟩

theorem first_unique (s : Nat → Bool) {a b : Nat} (ca : clear s a = true) (ha : s a = true)
    (cb : clear s b = true) (hb : s b = true) : a = b :=
  match Nat.lt_or_ge a b with
  | .inl lt => (bool_absurd (false_before s cb lt) ha).elim
  | .inr ge => match Nat.lt_or_ge b a with
    | .inl lt => (bool_absurd (false_before s ca lt) hb).elim
    | .inr ge' => Nat.le_antisymm ge' ge

/-- The limited principle of omniscience for Boolean sequences. -/
def LPO : Prop :=
  ∀ s : Nat → Bool, (∃ n, s n = true) ∨ ∀ n, s n = false

/-! ## P3. The end step is LPO, not Markov -/

/-- The step `chain_ends_of_em` takes excluded middle for: a single formation never
supported, with a carried reserve and decided activity, has an end step. Without it
`Carries.active_finitely` gives only that it is not active at arbitrarily late steps. -/
def EndStep : Prop :=
  ∀ (W : Web Unit Unit) (r : Nat → Unit → Nat), (∀ t, Decidable (W.active t ())) →
    W.Carries r → (∀ t, ¬ W.Supported t ()) → ∃ E, ∀ t, E ≤ t → ¬ W.active t ()

namespace Once

def ind : Bool → Nat
  | true => 1
  | false => 0

theorem ind_and_le : ∀ b c : Bool, ind (b && c) ≤ ind b
  | true, true => Nat.le_refl 1
  | true, false => Nat.zero_le 1
  | false, _ => Nat.le_refl 0

theorem ind_fall : ∀ b c : Bool, b = true → c = true → ind (b && !c) < ind b
  | true, true, _, _ => Nat.zero_lt_one
  | false, _, h, _ => nomatch h
  | true, false, _, h => nomatch h

variable (s : Nat → Bool)

/-- One formation, never supported, active exactly at the first `true` of `s`. -/
def web : Web Unit Unit where
  level _ _ := 0
  active t _ := clear s t = true ∧ s t = true
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := False

/-- One until the first `true` has passed. -/
def reserve (t : Nat) (_ : Unit) : Nat :=
  ind (clear s t)

theorem unsupported (t : Nat) : ¬ (web s).Supported t () :=
  fun supported => Nat.not_succ_le_zero 0 (supported () trivial)

theorem carries : (web s).Carries (reserve s) :=
  fun t _ _ => ⟨ind_and_le (clear s t) (!s t),
    fun active => ind_fall (clear s t) (s t) active.1 active.2⟩

def decided (t : Nat) : Decidable ((web s).active t ()) :=
  (instDecidableAnd : Decidable (clear s t = true ∧ s t = true))

/-- Active at most once. -/
theorem once {t u : Nat} (at_t : (web s).active t ()) (at_u : (web s).active u ()) : t = u :=
  first_unique s at_t.1 at_t.2 at_u.1 at_u.2

/-- `Carries.active_finitely` applies. -/
theorem finitely : ¬ ∀ N, ∃ t, N ≤ t ∧ (web s).active t () :=
  (carries s).active_finitely (T := 0) fun t _ => unsupported s t

end Once

theorem lpo_of_endStep (step : EndStep) : LPO := fun s =>
  match step (Once.web s) (Once.reserve s) (Once.decided s) (Once.carries s)
      (Once.unsupported s) with
  | ⟨E, quiet⟩ => match clear_or_first s E with
    | .inr ⟨m, _, _, h⟩ => .inl ⟨m, h⟩
    | .inl c => .inr fun n => bool_false (s n) fun h =>
      match first_of_true s h with
      | ⟨m, cm, hm⟩ => match Nat.lt_or_ge m E with
        | .inl lt => bool_absurd (false_before s c lt) hm
        | .inr ge => quiet m ge ⟨cm, hm⟩

/-! ## P4. "Finitely many" is LPO -/

/-- The `∃ L` form of `Listed.few_of_quiet`. -/
def FewFinite : Prop :=
  ∀ (p : Nat → Nat → Prop) (l : Nat → List Nat), (∀ a t, Decidable (p a t)) →
    Listed p l → (¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) →
    ∃ L : List Nat, ∀ t a, p a t → a ∈ L

namespace Few

def pick : Bool → Nat → List Nat → List Nat
  | true, t, _ => [t]
  | false, _, l => l

variable (s : Nat → Bool)

/-- The first `true` once it has passed. -/
def found : Nat → List Nat
  | 0 => []
  | t + 1 => pick (clear s t && s t) t (found t)

/-- Holding at `t`: being the first `true`, before `t`. -/
abbrev p (a t : Nat) : Prop :=
  a < t ∧ clear s a = true ∧ s a = true

theorem distinct_pick : ∀ (b : Bool) (t : Nat) {l : List Nat}, Distinct l →
    Distinct (pick b t l)
  | true, _, _, _ => ⟨fun no => (nomatch no), trivial⟩
  | false, _, _, d => d

theorem distinct_found : ∀ t, Distinct (found s t)
  | 0 => trivial
  | t + 1 => distinct_pick (clear s t && s t) t (distinct_found t)

theorem mem_pick (t a : Nat) : ∀ b : Bool, (clear s t && s t) = b →
    (p s a t ↔ a ∈ found s t) → (p s a (t + 1) ↔ a ∈ pick b t (found s t))
  | true, h, _ =>
    ⟨fun ⟨_, c, h'⟩ => Eq.subst (motive := fun x => x ∈ [t])
        (first_unique s (and_left h) (and_right h) c h') (List.Mem.head []),
     fun m => match mem_cons_cases m with
      | .inl same => Eq.subst (motive := fun x => p s x (t + 1)) same.symm
          ⟨Nat.lt_succ_self t, and_left h, and_right h⟩
      | .inr no => nomatch no⟩
  | false, h, ih =>
    ⟨fun ⟨lt, c, h'⟩ => ih.mp ⟨match Nat.lt_or_ge a t with
        | .inl lt' => lt'
        | .inr ge => (bool_absurd h (Eq.subst (motive := fun x => (clear s x && s x) = true)
            (Nat.le_antisymm (Nat.le_of_lt_succ lt) ge) (and_both _ _ c h'))).elim, c, h'⟩,
     fun m => match ih.mpr m with
      | ⟨lt, c, h'⟩ => ⟨Nat.lt_succ_of_lt lt, c, h'⟩⟩

theorem mem_found : ∀ t a, p s a t ↔ a ∈ found s t
  | 0, a => ⟨fun h => absurd h.1 (Nat.not_lt_zero a), fun h => nomatch h⟩
  | t + 1, a => mem_pick s t a (clear s t && s t) rfl (mem_found t a)

theorem listed : Listed (p s) (found s) :=
  fun t => ⟨distinct_found s t, fun a => mem_found s t a⟩

def decided (a t : Nat) : Decidable (p s a t) :=
  (inferInstance : Decidable (a < t ∧ clear s a = true ∧ s a = true))

/-- What comes to hold comes to hold at its own index. -/
theorem comes_at {a t : Nat} (comes : ComesToBe (p s a) t) : a = t :=
  match comes with
  | ⟨fails, holds⟩ => match holds with
    | ⟨lt, c, h⟩ => match Nat.lt_or_ge a t with
      | .inl lt' => (fails ⟨lt', c, h⟩).elim
      | .inr ge => Nat.le_antisymm (Nat.le_of_lt_succ lt) ge

/-- Coming to hold happens at most once. -/
theorem quiet : ¬ ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p s a) t :=
  fun all => match all 0 with
  | ⟨t₀, _, _, c₀⟩ => match all (t₀ + 1) with
    | ⟨_, _, later, c₁⟩ =>
      Nat.not_succ_le_self t₀ (Nat.le_trans later (Nat.le_of_eq
        (((comes_at s c₁).symm.trans (first_unique s c₁.2.2.1 c₁.2.2.2 c₀.2.2.1 c₀.2.2.2)).trans
          (comes_at s c₀))))

end Few

theorem lpo_of_fewFinite (few : FewFinite) : LPO := fun s =>
  match few (Few.p s) (Few.found s) (Few.decided s) (Few.listed s) (Few.quiet s) with
  | ⟨L, covers⟩ => match clear_or_first s (beyond L) with
    | .inr ⟨m, _, _, h⟩ => .inl ⟨m, h⟩
    | .inl c => .inr fun n => bool_false (s n) fun h =>
      match first_of_true s h with
      | ⟨m, cm, hm⟩ => bool_absurd
          (false_before s c (lt_beyond (covers (m + 1) m ⟨Nat.lt_succ_self m, cm, hm⟩))) hm

/-! ## P5. `holding_world`'s docstring -/

/-- `kindling` is counted, whatever arises in it is embodied, it balances and dissipates,
every step is enclosed and arising recurs. `holding_world` says that under a census, with
whatever arises embodied, balance and dissipation, openness is necessary for arising
without end; `arising_opens` needs every relatum embodied, which fails here. -/
theorem kindling_docstring :
    World.kindling.Counted ∧ World.kindling.ArisingEmbodied ∧ World.kindling.Balanced ∧
    World.kindling.Dissipative ∧ (∀ t, World.kindling.flow.Enclosed t) ∧
    World.kindling.ArisingRecurs ∧ ¬ World.kindling.Embodied :=
  match World.rest_needs_standing.1 with
  | ⟨counted, arising, balanced, dissipative, around, recurs, _⟩ =>
    ⟨counted, arising, balanced, dissipative,
     fun t => match around t with
      | ⟨es, distinct, _, closed⟩ => ⟨es, distinct, closed⟩,
     recurs,
     fun embodied => ((embodied (Kindling.Relatum.fuel 0) 0).mpr (Kindling.fuel_stands 0) :
       False)⟩

/-! ## P6. The names of P30's world -/

example := @Becoming.World.World.slow_world
example := @Becoming.World.World.slow
example := @Becoming.World.Slow.census
example := @Becoming.World.Slow.grows_between

end Review12
```

## Appendix B. Probe axiom audit

`build/Review12Audit.lean`, sha256 `e05660468e6e91a892ad942eb426abca534376428b33adaaccf7dd06079ba1ad`. Run with the same toolchain, it exits 0.

```lean
import Lean
import Review12
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review12 | throwError "no module Review12"
  let mut count := 0
  let mut withAxioms := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      let axs ← liftCoreM (Lean.collectAxioms n)
      if axs.size > 0 then withAxioms := withAxioms.push (n, axs)
  logInfo m!"Review12 constants: {count}; with axioms: {withAxioms.size}: {withAxioms.toList}"

#print axioms Review12.chain_ends_upto
#print axioms Review12.chain_ends_of_upto
#print axioms Review12.no_chain
#print axioms Review12.Short.short
#print axioms Review12.Once.once
#print axioms Review12.Once.finitely
#print axioms Review12.lpo_of_endStep
#print axioms Review12.Few.quiet
#print axioms Review12.Few.listed
#print axioms Review12.lpo_of_fewFinite
#print axioms Review12.kindling_docstring
```

Output, `Review12Audit.out`, sha256 `237c004a97abea6395eb302cf60579ebb1f538ab2cf8de35b9b85f6f81099190`:

```text
Review12 constants: 107; with axioms: 0: []
'Review12.chain_ends_upto' does not depend on any axioms
'Review12.chain_ends_of_upto' does not depend on any axioms
'Review12.no_chain' does not depend on any axioms
'Review12.Short.short' does not depend on any axioms
'Review12.Once.once' does not depend on any axioms
'Review12.Once.finitely' does not depend on any axioms
'Review12.lpo_of_endStep' does not depend on any axioms
'Review12.Few.quiet' does not depend on any axioms
'Review12.Few.listed' does not depend on any axioms
'Review12.lpo_of_fewFinite' does not depend on any axioms
'Review12.kindling_docstring' does not depend on any axioms
```

The toolchain is Lean 4.29.1, arm64-apple-darwin24.6.0, commit `f72c35b3f637c8c6571d353742168ab66cc22c00`, Release.
