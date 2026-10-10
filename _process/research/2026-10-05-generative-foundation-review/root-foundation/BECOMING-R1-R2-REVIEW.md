# R1、R1b 与 R2 的独立审查 / Independent review of R1, R1b and R2 (`Becoming.Resolution`)

2026-10-11。审查者：Claude Opus 5.5，独立 agent，未参与撰写 R1、R1b 与 R2。

对象是 `Becoming.Resolution` 及其文档，经三个提交：`658db670`（R1）、`e79e00e5`（R1b）、`de17f533`（R2）。

- 任务说明把 R2 描述为未提交。审查期间它以 `de17f533` 提交。提交的 `Resolution.lean` 与审查所读的工作树文件及暂存副本逐字节相同（sha256 `374611f2…`）。所以对 R2 的结论就是对 `de17f533` 的结论。
- 其后的 `8237d0a8` 与 `12403fea`（P45）不在对象之内。它们没有改动 `Resolution.lean`，只移动了根模块与检查器中的行号，并重指记录的验证范围。

这是第十五次独立审查。

/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of R1, R1b or R2.

Object: `Becoming.Resolution` and its documentation, through three commits: `658db670` (R1), `e79e00e5` (R1b) and `de17f533` (R2).

- The brief described R2 as uncommitted. It was committed as `de17f533` during the review. The committed `Resolution.lean` is byte-identical to the working-tree file and the scratch copy reviewed (sha256 `374611f2…`), so the verdicts on R2 are verdicts on `de17f533`.
- The later commits `8237d0a8` and `12403fea` (P45) are outside the object. They leave `Resolution.lean` unchanged; they only shift line numbers in the root module and the checker and re-point the record's validation scope.

This is the fifteenth independent review.

**摘要（中文）。**

- **机械检查都对。**
  - R2 的核心闭包 37 个模块在仓库之外从前导（Lean 4.29.1）重新编译，退出码都为 0。
  - R1 到 R2 之间只有 `Resolution.lean` 与根模块 `Becoming.lean` 改动，所以 R1、R1b 两版的 `Resolution.lean` 也对同一闭包各自编译，退出码 0。
  - `Becoming.Resolution` 生成的常量（R1／R1b／R2）：
    - 常量数 204／229／313，没有一个依赖公理；
    - 非内部声明 128／149／204，`#print axioms` 全空；
    - 这些声明包含回执所列的 126／145／200 条，多出的 2／4／4 条是生成的 `Decidable` 实例。
  - R2 闭包有 7142 个常量。依赖公理的只有 38 条生成的 `injEq`，只依赖 `propext`，与回执相同。
  - 三个提交的回执：
    - 核心回执 `155424`、`163746`、`165248`，外围回执 `161037`、`164738`、`165548`；
    - 源哈希（核心 50，外围 41）、检查器哈希与保留产物（314 与 90）都与各自提交一致；
    - 保留的回执等于正式回执，`core_compiles_from_prelude` 为真，回执时间都早于提交。
  - 计数：
    - Resolution 的定理／声明为 97/126 → 110/145 → 153/200；
    - 脊柱合计 1649/2571 → 1662/2590 → 1705/2645；
    - 都与提交说明、计划行及章节 §9 一致。
- **数学被接受。**
  - 对象中没有错误的 Lean 陈述。
  - R2 把 `Flow.DissipatesBy` 改为对家族陈述，确实使交换、增长、下降与静止的每条规律变强：证明只用对家族的总和。
  - `Trickle` 恰好说明了它所说的：每一尺度的转移都有最小损失时，增长仍可不止。
- **本审查写了 72 条探针声明（定理 56 项），生成 108 个常量，都不依赖任何公理**（附录 A、B）。
- **问题共十一项（W1–W11）。W1、W3、W4 最重要。**
  - **W1（过强，中）：** “计数关系项需要对家族的比例”与“只有损失随所转移的量成比例，分割才不能把损失分没”不成立。
    - 探针 `growth_bound_of_replenished_loss` 在一个严格更弱的前提下给出增长的规律，以及生起不复现。这个前提是：家族得到至少 `1/p` 单位时至少失去 `1/m` 单位（`ReplenishedLoses`）。
    - 它由三者各自给出：对家族的比例（m = p q）；脊柱单位固定时的耗散（m = 1）；每一尺度的最小损失加上每步至多 K 次转移（`growth_bound_of_least_loss_few`）。
    - `Tick` 满足它而不满足任何比例。
    - `Trickle` 恰好只缺“每步转移的次数有界”（`growth_needs_bounded_transfers`）。
    - 所以 `Trickle` 缺的不是比例，而是有界的同时转移。任何对家族总量的前提都不能被分割分没，不只是比例。
    - 模块说明的“either … or”也漏了这第三条路。
  - **W2（过强，低）：** 计划 R2 行与 §59.2 开头说“把前提推到最弱”，提交说明说“to its weakest form”；W1、W5 给出三处更弱的前提。
  - **W3（错误，中）：** 章节 l. 477 中文把 Trickle 写成“一整个单位可以由越来越多、越来越小的转移带过而不复现地停止”。英文 l. 504 与 Lean 都是“without end”。中英意思相反。
  - **W4（缺少前提，中）：** 量子的规律在以下五处省去了耗散（或家族不被增益）：模块说明 l. 19–21 与 l. 86–88、根模块 l. 249–250、包 README l. 46、检查器范围 l. 615–618。Lean 的 `Flow.quantum_bound` 有这一前提，记录也写了。探针 `Pump` 说明缺了它句子为假：平衡、单位固定、封闭的池在任意晚的步失去一个整单位。
  - **W5（前提强于所用，低）：** `Flow.quantum_bound` 只用家族不被增益；`Flow.exchange_bound_of_least_loss` 只用逐个形成不增益（`DissipatesOn.give_le`）。两者都要 `Flow.Dissipative`（每次取用至少失去一单位）。记录与研究对这一前提的注释“每个形成给回封闭家族的不多于所取”描述的正是较弱的前提，与 Lean 不符。探针给出两个较弱的版本，并证明较弱是严格的。
  - **W6（边界陈述变弱，低）：**
    - R2 之后，`rest_needs_quantum` 与 `arising_needs_quantum` 中 `DissipativeBy` 的合取项只断言对家族的比例。R1b 时它们断言的是逐个形成的比例，是更强的边界。
    - 反驳 11 只说规律变强，没有说这两条见证定理变弱。
    - 探针 `EachShare`、`Asymptote.eachShare`、`Emission.eachShare` 与 `arising_needs_quantum_each` 恢复了更强的形式。
  - **W7（缺少陈述，低）：**
    - “反之不然”没有核心见证（探针 `family_share_strictly_weaker`）。
    - 去掉固定单位的见证没有证明它们不满足固定单位（探针 `Emission.not_balanced`、`Alternation.not_balanced`、`Asymptote.not_balanced`）。
    - 文字说 Trickle 中“得到、失去、开始或终结”的计数都需要更多，但只陈述了生起。
    - 交换界可达（探针 `Tight.attained`）；手算显示增长界在 p = q = S = 1 时不可达。
  - **W8（量词与范围，低）：**
    - “缺少任一，各自无尽地继续”应为“可以”；
    - 交换的规律被写成“围住之内……以所立者的总水平为界”，它实际只对从 T 起固定的封闭家族、以其存量为界；
    - “每一分辨率下的静止”只是每一尺度的静止；
    - “each boundary is attained”与记录的“界是否可达未证”用同一个词说两件事。
  - **W9（记账，低）：**
    - 记录说“其余见证只有一两个关系项”，Emission 不是；
    - “说明前提彼此独立”过宽；
    - Trickle 的 `flow` 文档说每份是“the step after next”的四分之一，方向反了。
  - **W10（命名与出处，低）：**
    - “最小花费 / least cost”是金融词；
    - “share”有歧义且带金融色彩；
    - Trickle 的 `carriers` 与储备的 `Web.CarriesAt` 同词异义；
    - “the loss law”指两样东西；
    - 记录的“The readings are Ren's / 读法属于 Ren”与同一字段的“作者的读法（AI 论证）”相冲突，只此一份记录用这句话。
  - **W11（方法，低，已披露）：** Trickle 的转移者从不立、从不活跃。定理不要求它们活跃，所以见证公平。按一元方法，这是表示的装置而非形成的关系。建议构造转移者活跃的变体（只有草图，未检查）。

**Summary (English).**

- **The mechanical checks pass.**
  - The 37 modules of R2's core closure recompile from the prelude (Lean 4.29.1) outside the repository. All exit 0.
  - Between R1 and R2 only `Resolution.lean` and the root `Becoming.lean` change. So the R1 and R1b versions of `Resolution.lean` were also compiled against the same closure; both exit 0.
  - Constants generated by `Becoming.Resolution` (R1 / R1b / R2):
    - 204 / 229 / 313 constants, none depending on any axiom;
    - 128 / 149 / 204 non-internal declarations, every `#print axioms` empty;
    - these include the 126 / 145 / 200 the receipts list; the extra 2 / 4 / 4 are generated `Decidable` instances.
  - R2's closure has 7142 constants. Exactly 38 depend on an axiom: generated `injEq` lemmas, on `propext` only, equal to the receipt.
  - Receipts for the three commits:
    - core receipts `155424`, `163746`, `165248`; periphery receipts `161037`, `164738`, `165548`;
    - each matches its commit in source hashes (50 core, 41 periphery), checker hashes and retained artifacts (314 and 90);
    - the retained receipt equals the committed one, `core_compiles_from_prelude` is true, and every receipt predates its commit.
  - Counts:
    - Resolution theorems/declarations go 97/126 → 110/145 → 153/200;
    - the spine totals go 1649/2571 → 1662/2590 → 1705/2645;
    - all agree with the commit messages, plan rows and chapter §9.
- **The mathematics is accepted.**
  - No Lean statement in the object is wrong.
  - Restating `Flow.DissipatesBy` per family genuinely strengthens every law of exchange, growth, falling and rest: the proofs use only the family's total.
  - `Trickle` shows exactly what it is said to show: a least loss at each size of transfer does not stop growth.
- **The probes are 72 source declarations (56 theorems). None of their 108 constants depends on any axiom** (appendices A and B).
- **Eleven findings (W1–W11). W1, W3 and W4 matter most.**
  - **W1 (overclaim, moderate):** "Counting relata needs the share" and "only a loss in proportion to what is transferred cannot be split away" are false.
    - Probe `growth_bound_of_replenished_loss` gives the growth law, and non-recurrence of arising, under a strictly weaker premise: a family given at least `1/p` of the unit loses at least `1/m` of it (`ReplenishedLoses`).
    - Each of three things gives that premise: the family's share (m = p q); the spine's dissipation at a fixed unit (m = 1); and a least loss at each size of transfer with at most K transfers per step (`growth_bound_of_least_loss_few`).
    - `Tick` meets it and no share.
    - `Trickle` lacks exactly the bound on transfers per step (`growth_needs_bounded_transfers`).
    - So what `Trickle` exploits is unboundedly many simultaneous transfers, not the absence of proportion. No premise on the family's totals can be split away, not only the share.
    - The module doc's "either … or" also misses this third route.
  - **W2 (overclaim, low):** Plan R2 and §59.2 open with "把前提推到最弱", and the commit message says "to its weakest form"; W1 and W5 give three weaker premises.
  - **W3 (error, moderate):** Chapter l. 477 (zh) says the whole unit passes in ever smaller transfers "而不复现地停止" (and stops, not recurring). The English l. 504 and the Lean say "without end". The two primary languages say opposite things.
  - **W4 (missing hypothesis, moderate):** The quantum law is stated without dissipation (or non-gain) in five places: the module doc l. 19–21 and l. 86–88, the root doc l. 249–250, the package README l. 46 and the checker scope l. 615–618. The Lean `Flow.quantum_bound` has the premise and so does the record. Probe `Pump` shows the sentence is false without it: a balanced, fixed-unit, closed pool loses a whole unit at arbitrarily late steps.
  - **W5 (premise stronger than used, low):** `Flow.quantum_bound` uses only that the family is not gained on, and `Flow.exchange_bound_of_least_loss` only that no formation gains on it (`DissipatesOn.give_le`). Both assume `Flow.Dissipative` (a unit lost at every take). The record and study gloss that premise as "each formation gives a closed family no more than it takes", which is the weaker premise, not the Lean one. Probes give both weaker versions and prove the weakening strict.
  - **W6 (boundary statements weakened, low):**
    - After R2, the `DissipativeBy` conjuncts of `rest_needs_quantum` and `arising_needs_quantum` assert only the per-family share. At R1b they asserted the per-formation share, a stronger boundary.
    - Counterreply 11 says the laws got stronger but not that these two witness theorems got weaker.
    - Probes `EachShare`, `Asymptote.eachShare`, `Emission.eachShare` and `arising_needs_quantum_each` restore the stronger form.
  - **W7 (missing statements, low):**
    - "Not conversely" has no core witness (probe `family_share_strictly_weaker`).
    - The witnesses that drop the fixed unit are not shown to fail it (probes `Emission.not_balanced`, `Alternation.not_balanced`, `Asymptote.not_balanced`).
    - The prose says counting what relata "gain, lose, begin or end" needs more, but Trickle states only arising.
    - The exchange bound is attained (probe `Tight.attained`); by hand, the growth bound is not attained at p = q = S = 1.
  - **W8 (quantifiers and scope, low):**
    - "each continues without end" should be "can continue";
    - the exchange law is described as bounded by "the total standing … inside an enclosure", but it is stated for a fixed family closed from T, bounded by its stock;
    - "rest at every resolution" is rest at each size;
    - "each boundary is attained" uses the record's word for tightness to mean "witnessed".
  - **W9 (bookkeeping, low):**
    - The record says "the other witnesses have one or two relata"; Emission does not;
    - "show the premises independent" overreaches;
    - the Trickle `flow` docstring says each part is a quarter of the parts of "the step after next"; that is inverted.
  - **W10 (naming and provenance, low):**
    - "least cost / 最小花费" is financial;
    - "share" is ambiguous and financial in tone;
    - Trickle's `carriers` collide with the reserve's `Web.CarriesAt`;
    - "the loss law" names two things;
    - the record's "The readings are Ren's / 读法属于 Ren" contradicts "The author's reading (an AI argument)" in the same field. No other record uses the phrase.
  - **W11 (method, low, disclosed):** Trickle's carriers never stand and are never active. The theorems do not require activity, so the witness is fair. Under the nondual method it is a representational device rather than a formed relation. An active-carrier variant is recommended (sketch only, unchecked).

## 0. Scope, materials and method

**Object.** Times are UTC, 2026-10-10.

| Commit | Time | Content | Core receipt | Periphery receipt |
|---|---|---|---|---|
| `658db670` | 16:23:42 | R1: `Becoming.Resolution`, the loss law, exchange and growth at every resolution, four witnesses (§59) | `20261010T155424.663562Z` | `20261010T161037.642977Z` |
| `e79e00e5` | 16:52:28 | R1b: falling, ceasing, the reserve, `Dwindle` (§59.1) | `20261010T163746.432774Z` | `20261010T164738.513555Z` |
| `de17f533` | 17:05:55 | R2: `DissipatesBy` per family, `LosesAtSize`, `Trickle` (§59.2) | `20261010T165248.121581Z` | `20261010T165548.911356Z` |

`8237d0a8` (17:14:47) and `12403fea` (P45, 17:26:33) came later. They are not reviewed. Line numbers below are at `12403fea` (HEAD) unless stated.

- `Resolution.lean`, the chapter and the package README rows are at the same lines as at `de17f533`.
- `Becoming.lean` is 6 lines later than at `de17f533`; `check_becoming.py` is 12 lines later; the study's English paragraphs are 61 lines later.
- The cited text is unchanged in every case.

**Isolation.**

- Nothing in `/Users/ren/theories` was edited, added or committed.
- `git show`, `git diff`, `git log`, `git ls-tree` and `git grep` ran read-only.
- All builds, audits and probes ran under this scratch directory.
- The Mathlib periphery and `Becoming.Bridge` were not rebuilt. Their receipts and hashes were checked.

**Materials** (sha256 prefix at `de17f533` / at HEAD; lines).

| File | `de17f533` | HEAD | Lines |
|---|---|---|---|
| `Becoming/Resolution.lean` | `374611f290cc9ecc` | same | 1783 |
| `Becoming/Openness.lean` | `98bd13dd51347a86` | same | 1206 |
| `Becoming/Dissipation.lean` | `8b1c821ce8e4d9da` | same | 1192 |
| `Becoming/Flow.lean` | `4af6e1afa8f70407` | same | 921 |
| `Becoming.lean` | `cc1e8e6952575319` | `d662912d3a130ede` | 368 / 374 |
| `becoming/README.md` | `0fa9f6ef96915703` | `2107b82c6f98b979` | 107 |
| `becoming/check_becoming.py` | `c112aa7eb61a43e4` | `53be11a5d9d88166` | 1104 / 1116 |
| `chapters/THE-THEORY-OF-BECOMING.md` | `6323837dadefb496` | `e846a226e8ab5af8` | 1034 |
| `BECOMING-RENEWAL-READING.md` (study) | `4ce9e8ba4bbd88c3` | `8018ff5e8ead0760` | 4141 / 4211 |
| `BECOMING-UNIFICATION-PLAN.md` | `04f53f5d20daf67a` | `c4df7e79e34c75ef` | 402 / 404 |
| `records/rest-at-every-resolution.json` | `b505069c79d33820` | `6cf0ab071180a843` | 651 / 655 |
| `sources/…/2026-10-10-pareto-frontier.md` | `80bacdae44c98994` | same | 38 |
| `Resolution.lean` at `658db670` / `e79e00e5` | `972098b0a8aee90e` / `bab1b691aa597449` | — | — |
| `review/probes/Review15.lean` | `1a026465303f31ec` | — | 749 |
| `review/probes/Review15Audit.lean` | `0e0e63c40c848f0f` | — | 26 |

Between `de17f533` and HEAD the record changed only in its validation scope, reference hashes and one history entry. Its title, claim, hypotheses, correspondence, limitations and next step are as at R2.

**Method.**

1. **Build.**
   - `review/build_prelude.py` copied the 37 closure sources of `de17f533` out of git, removed `import Std` as `check_becoming.py` does for its prelude-only run, and compiled each with `lean +leanprover/lean4:v4.29.1 -o` in dependency order into `review/build_r2/`. All exit 0.
   - The R1 and R1b versions of `Resolution.lean` were compiled the same way against that closure, after checking with `git diff --name-only 658db670^ de17f533` that no other core source changed. Both exit 0.
2. **Audit.** `review/ResolutionAudit.lean` walks every constant of `Becoming.Resolution` with `Lean.collectAxioms`, then every closure constant, then prints each non-internal Resolution declaration with its axioms. It imports `Becoming` at R2 and `Becoming.Resolution` at R1 and R1b, so the closure figure covers the whole package only at R2.
3. **Receipts.**
   - `review/check_receipts.py` and `review/check_periphery.py` compared each commit's receipts with that commit's sources, checkers, retained artifacts and retained `verification.json`.
   - The core receipt's `check.py` entry is `universal-ethics/generative-capacity/check.py`. The script resolved it to a wrong path, so it was checked by hand: `b9f56e1700c03f00` at all three commits, equal to the receipt.
4. **Reading.**
   - `Resolution.lean` whole, against `Flow`, `Dissipation` and `Openness`.
   - The module doc; the root doc; the package README row; the checker scope.
   - Chapter Part I (l. 477, 504) and §9 (l. 905).
   - Study §§59–59.2 and their English paragraphs (l. 4191–4200).
   - Plan rows R1, R1b, R2 (zh l. 338–341, en l. 403–404).
   - The record.
   - The sources `2026-10-10-pareto-frontier.md`, `structural-names.md` and `zero-axiom-part-and-names.md`, and `NONDUAL-METHOD.md`.
5. **Probes.**
   - `review/probes/Review15.lean` (term mode, imports `Becoming`, namespace `Review15`) was compiled against `build_r2`.
   - `Review15Audit.lean` walks every constant of the probe module and prints the axioms of each non-internal declaration.
   - The probe file contains no tactic proofs. The prelude's `Nat.le_of_add_le_add_left` depends on `propext`, so it is replaced by `Review15.left_cancel`, which goes through the core's axiom-free `le_of_add_le_add_right`.

## 1. Verdicts

**Mechanical checks.**

| Check | R1 `658db670` | R1b `e79e00e5` | R2 `de17f533` |
|---|---|---|---|
| Core receipt status / predates commit | passed / yes (15:54) | passed / yes (16:37) | passed / yes (16:52) |
| Periphery receipt / predates commit | passed / yes (16:10) | passed / yes (16:47) | passed / yes (16:55) |
| Core sources in receipt matching commit | 50 / 50 | 50 / 50 | 50 / 50 |
| Periphery sources matching commit | 41 / 41 | 41 / 41 | 41 / 41 |
| Checker hashes (`check_becoming.py`, `check.py`) | `18f49333`, `b9f56e17` | `62d0d48a`, `b9f56e17` | `c112aa7e`, `b9f56e17` |
| Retained artifacts, core / periphery | 314 / 90, no problems | 314 / 90 | 314 / 90 |
| Retained `verification.json` equals receipt | yes | yes | yes |
| `core_compiles_from_prelude`, `source_unchanged_during_check` | true, true | true, true | true, true |
| `Resolution.lean` sha256 (receipt = commit) | `972098b0` | `bab1b691` | `374611f2` |
| Rebuilt here from the prelude | Resolution against the R2 closure, exit 0 | same, exit 0 | 37 modules, exit 0 |
| Resolution constants / with axioms | 204 / 0 | 229 / 0 | 313 / 0 |
| Non-internal declarations / with empty report | 128 / 128 | 149 / 149 | 204 / 204 |
| Receipt's declarations ⊆ audited (extras) | 126 ⊆ 128 (2 instances) | 145 ⊆ 149 (4) | 200 ⊆ 204 (4) |
| Resolution theorems / declarations (receipt) | 97 / 126 | 110 / 145 | 153 / 200 |
| Spine theorems / declarations (receipt = commit message) | 1649 / 2571 | 1662 / 2590 | 1705 / 2645 |
| Closure constants / with axioms | 4199 / 24 (Resolution's closure) | 4224 / 24 | 7142 / 38 (= receipt) |
| Axioms in the closure | only `injEq` on `propext` | same | same, as the receipt lists |
| Plan / chapter §9 counts | plan R1 97 | plan R1b 110 | plan R2 153, §9 153 |

**Questions.**

| Question | Verdict | Findings |
|---|---|---|
| 1. Build, axioms, receipts, counts | **Correct.** See the table above. | — |
| 2. Lean statements | **Correct.** Every theorem read holds as stated. `Flow.DissipatesBy.of_each`, `exchange_bound`, `growth_bound`, `fall_bound`, `rests_at_resolution`, `exchange_bound_of_least_loss`, `losesAtSize_of_each` and `Web.CarriesAt.lasts` are each what their docstrings say. Two take a stronger premise than their proofs use. | W5 |
| 3. Is the per-family share strictly weaker? | **Yes, but unproved in the core.** Probe `family_share_strictly_weaker`: a spine-dissipative flow with share 1 per family and no share for any `q` per formation. | W7 |
| 4. Boundaries: each witness meets all premises but one | **Yes, with gaps.** <ul><li>Circulation, Alternation, Dwindle and Trickle prove the failure of the premise they lack.</li><li>Asymptote and Emission do not prove that they fail the fixed unit; probes do.</li><li>R2 weakened what Asymptote and Emission are stated to meet.</li></ul> | W6, W7 |
| 5. Prose says what the Lean says | **Mostly.** <ul><li>One zh/en inversion.</li><li>One missing hypothesis in five places.</li><li>One false necessity claim in module doc, record and study reading.</li><li>Several quantifier slips.</li></ul> | W1, W3, W4, W8 |
| 6. Pareto frontier within reach | **Yes.** <ul><li>Weaker premises for the quantum law and the least-loss exchange law.</li><li>A premise strictly weaker than the share that still gives the growth law, answering R2's open item.</li><li>The exact place of Trickle.</li><li>The exchange bound attained.</li></ul> All are probed axiom-free. | W1, W5, W7 |
| 7. "Weakest" and "needs" | **Overclaimed.** | W1, W2 |
| 8. Records and bookkeeping | **Accurate counts. Three factual slips and one provenance conflict in the record.** | W9, W10 |
| 9. Naming against Ren's criteria | **Mostly structural. Two financial words and two collisions.** | W10 |
| 10. Ren's words vs AI readings; nondual method | **Mostly kept apart.** <ul><li>The study labels its readings "AI, pending Ren".</li><li>The record's "readings are Ren's" does not.</li><li>Trickle's zero-level carriers are a representational device, disclosed.</li></ul> | W10, W11 |

## 2. Findings

### W1. Overclaim: "counting relata needs the share". A strictly weaker premise gives the growth law

**Evidence.**

- Places asserting necessity or exclusivity:
  - Module doc l. 46–47: "Counting relata needs the share: a whole unit can pass in ever more, ever smaller transfers."
  - l. 83–84: "Counting transfers needs only a least loss at each size; counting what relata gain, lose, begin or end needs the share."
  - l. 80–82: "So the rest of enclosed change is carried either by a least loss per exchange in a fixed unit, as in the spine, or, at every resolution, by loss in proportion together with a least size of what is exchanged, arises or ceases".
  - Record correspondence (en; zh the same): "counting what relata gain, lose, begin or end needs the family's share, since a whole unit can pass in ever more, ever smaller transfers (Trickle): only a loss in proportion to what is transferred cannot be split away."
  - Study §59.2 读法 (l. 3722): "只有损失随所转移的量成比例，分割才不能把损失分没，每一尺度的最小损失做不到这一点".
- The author's own careful statements say less, and correctly:
  - counterreply 13 (l. 3720): "只说明每一尺度的最小损失不够……比对家族的比例更弱而仍给出增长的规律的前提没有陈述";
  - the record's limitations and next step;
  - plan R2's open item;
  - the English study paragraph (l. 4200): "needs more".
  - The sentences above contradict them.
- What `growth_needs_proportion` proves:
  - a least loss at each size of *transfer*, with the spine's dissipation, does not stop growth;
  - Trickle meets no share.
  - It does not prove that growth needs the share.
- Probe Q4 shows it does not:
  - **The premise.** `ReplenishedLoses L R p m cs t := R (t+1) ≤ p * replenishment cs t → R (t+1) + m * replenishment cs t ≤ m * uptake cs t`. Where the family is given at least `1/p` of the unit, it loses at least `1/m` of it.
  - **The law.** `growth_bound_of_replenished_loss` takes:
    - census, embodied, `BalancesAt r`;
    - every closed family from `T` on not gained on and meeting `ReplenishedLoses`;
    - every step from `T` on enclosed; base, unit, refining.

    Its conclusion: the relata gaining at least `1/p` of the unit, counted relatum by relatum and step by step, number at most `p S · m S`, where `S` is the total standing at `T`. `growth_not_recurring_of_replenished_loss` and `arising_not_recurring_of_replenished_loss` follow.
  - **Three sources of the premise.**
    - The share gives it with `m = p q` (`share_replenishedLoses`).
    - The spine's dissipation at a fixed unit gives it with `m = 1` (`fixed_replenishedLoses`).
    - A least loss at each size of transfer with at most `K` transfers per step gives it, the size taken as `1/(p K)` (`few_replenishedLoses`, through the pigeonhole lemma `exists_large`). Hence `growth_bound_of_least_loss_few`: the growth law under `Dissipative`, `LosesAtSize R (p*K) m` and at most `K` transfers per step from `T`.
  - **Strictly weaker than the share.** `replenishedLoses_strictly_weaker`: `Tick` (take `t+1`, give `t`) is dissipative, meets `ReplenishedLoses (fun _ => 1) p 1` for every `p`, and meets no share. This witness is at a fixed unit. A witness at a refining unit is plausible but not probed. Sketch: at a quartering unit, take `2^t + 1` and give back `2^t` units of the step after from a pool of one unit of step 0.
  - **The exact place of Trickle.** `growth_needs_bounded_transfers`:
    - Trickle meets every premise of `growth_bound_of_least_loss_few` except the bound on transfers per step: it has more than `K` transfers at step `K` (`Trickle.transfers_unbounded`);
    - a whole unit arises at arbitrarily late steps;
    - for no `m` does it meet `ReplenishedLoses` at `p = 1` (`Trickle.not_replenishedLoses`).
- So what Trickle exploits is *unboundedly many transfers within one step*, not the absence of proportion.
- The conceptual point of the 读法 also needs correcting. Splitting a gain across transfers changes per-transfer quantities, not the family's totals. So *any* premise on the family's totals is immune to splitting: the share, and equally `ReplenishedLoses`. What splitting defeats is a premise per transfer.
- The "either … or" (l. 80–82) misses the third route above. It holds at every resolution and is neither the spine's fixed-unit loss nor loss in proportion.
- **Caveat on constants.** Under the share, the core's bound `p q S` is sharper than Q4's `p S · p q S`. Q4 weakens the premise, not the constant. The fall law, and so ceasing, under `ReplenishedLoses` was not probed.

**Fix.**

1. Module doc l. 46–47: "Counting relata needs more than a least loss at each size of transfer: a whole unit can pass in ever more, ever smaller transfers." l. 83–84: "…counting what relata gain needs a least loss on the family's totals, which the share gives; a least loss per transfer is not enough."
2. Replace the "either … or" by the routes known, without exclusivity.
3. Record correspondence: drop "needs the family's share" and "only a loss in proportion … cannot be split away".
4. Study §59.2 读法: keep the text and add an in-place correction note. The study's practice for historical passages is to preserve them.
5. Consider moving Q4 into the core: `Flow.ReplenishedLoses`, `World.growth_bound_of_replenished_loss`, the three sources, and `growth_needs_bounded_transfers` as the exact place of Trickle. This closes the record's next step, "premises between a least loss at each size and it", and plan R2's open item. Whether the family's share or a least loss on the family's totals is the premise to read physically remains Ren's question.

### W2. Overclaim: "push the premise to the weakest"

**Evidence.**

- Plan zh R2 row (l. 341): "同一方向：把前提推到最弱".
- Study §59.2 (l. 3692): "同一方向：把前提推到最弱".
- Commit `de17f533`: "Pushing the premise of R1 and R1b to its weakest form."
- The same texts list as open "a premise weaker than the family's share that still gives the growth law". W1 gives one.
- W5 gives weaker premises for the quantum law and the least-loss exchange law, which R2 restated without weakening.
- The English plan line (l. 404) is neutral.

**Fix.** "把前提推向更弱 / weakening the premise". The commit message is history and stays.

### W3. Error: the Chinese chapter inverts Trickle

**Evidence.**

- Chapter l. 477 (zh): "每一尺度的最小损失只给出交换的规律：一整个单位可以由越来越多、越来越小的转移带过而不复现地停止（`growth_needs_proportion`）".
- l. 504 (en): "a whole unit can pass in ever more, ever smaller transfers without end (`growth_needs_proportion`)".
- `growth_needs_proportion` (Resolution l. 1770–1781) states `∀ N, ∃ t x, N ≤ t ∧ Trickle.web.Arises t x ∧ quarter (t + 1) ≤ 1 * Trickle.web.level (t + 1) x`: a whole unit arises at arbitrarily late steps.
- The zh says the passing stops without recurring. What does not recur is each *fixed size of transfer* (`Trickle.exchange_stops`), not the passing of the unit.
- The sentence was introduced in R2 and is unchanged at HEAD. Chinese and English are equally primary (AGENTS).

**Fix.** "一整个单位可以由越来越多、越来越小的转移无尽地带过（每个固定尺度的转移不复现）".

### W4. Missing hypothesis: the quantum law stated without dissipation

**Evidence.**

- The Lean has the premise:
  - `Flow.quantum_bound` (l. 279–287) and `Flow.quantum_not_recurring` (l. 289–297) take `dissipative : L.Dissipative`, `distinct` and `closed`;
  - the docstring (l. 275) begins "Balanced at resolution `r` and dissipative";
  - the record's claim has it: "balanced at a refining resolution and dissipative".
- Prose that drops it:
  - Module doc l. 19–21: "So the steps at which a family closed from `T` on loses at least `1/q` of the unit of step `T` number at most `q` times its stock at `T` (`Flow.quantum_bound`)".
  - Module doc l. 86–88: "What holds at every resolution without either is the quantum law: an enclosed family cannot keep losing at a non-vanishing rate."
  - Root doc l. 249–250: "Whatever the refinement, the times a closed family loses at least `1/q` of the unit number at most `q` times its stock (the loss law)."
  - Package README l. 46: "所以封闭家族损失至少 1/q 单位的步不多于 q 乘其存量" / "so steps at which a closed family loses at least 1/q of the unit number at most q times its stock and do not recur".
  - Checker scope l. 615–618: "a flow balanced at that resolution has, over any family closed from some step, the quanta … so steps losing at least 1/q of the unit number at most q times the stock and do not recur".
  - Checker scope l. 633–634 states the least-loss exchange law without the spine's dissipation: "where each formation taking at least 1/p of the unit loses at least 1/m of it, such takings number at most m times the stock".
- Without the premise the sentences are false. Probe `quantum_needs_not_gained`:
  - `Pump` is balanced at the fixed unit, its one-member pool is closed at every step and without repetition;
  - it loses a whole unit (`LosesQuantum … 1`) at arbitrarily late steps;
  - a formation gives the pool one unit from nothing at even steps and takes it at odd steps.
- §9 of the chapter (l. 905) has it right: "被耗散的封闭家族".

**Fix.** Add "dissipated on" (or, with W5, "not gained on") in each place. Changing the checker's scope text changes its hash, which the next run records anyway.

### W5. Premise stronger than used: the quantum law and the least-loss exchange law

**Evidence.**

- **The quantum law.**
  - `Flow.quantum_bound` derives non-rising from `Dissipative` through `balances.lowers (dissipative cs u distinct (closed u after))` (l. 286–287). Only `replenishment ≤ uptake` of the family is used.
  - Probe `quantum_bound_of_not_gained` takes just `∀ t, T ≤ t → L.replenishment cs t ≤ L.uptake cs t`, with no closure, no distinctness, no unit loss and no share.
  - `not_gained_of_dissipative` recovers the core's version.
- **The least-loss exchange law.**
  - `Flow.exchange_bound_of_least_loss` (l. 598–609) passes `dissipative …` to `BalancesAt.takers_lose_least`, which uses it only through `Flow.DissipatesOn.give_le`: each formation gives no more than it takes.
  - Probe `exchange_bound_of_least_loss_not_gaining` takes `NotGaining` (that per-formation inequality on closed families without repetition) instead.
  - `lossless_not_gaining_not_dissipative` shows `NotGaining` strictly weaker: a lossless transfer.
- **The gloss disagrees with the Lean.**
  - Record hypothesis 3: "the spine's dissipation (each formation gives a closed family no more than it takes)".
  - Study §59.2 (l. 3701): "最小损失的交换律另要脊柱的耗散（每个形成给回封闭家族的不多于所取）".
  - Both describe `NotGaining`. `Flow.Dissipative` (Dissipation l. 230, through `DissipatesOn`, l. 224–226) asks `total cs give + sign (total cs take) ≤ total cs take`: a formation that takes gives back at least one unit less.
  - The gloss truncates the spine's own docstring (l. 222–223), "gives the family no more than it takes from it, and less when it takes"; it drops "and less when it takes".
- At a refining unit that one-unit loss is a loss of one unit of the step after, a vanishing amount. The premise the proof needs is the gloss's, not the Lean's.

**Fix.** Weaken the two theorems (preferred, in R2's own direction), or make the gloss say "gives back at least one unit of the step after less than it takes".

### W6. R2 weakened what two boundary theorems assert

**Evidence.**

- At R1b, `DissipatesBy q cs t` was per formation (`e79e00e5`, l. 318–319): `∀ f, f ∈ L.present t → (q + 1) * total cs (L.give t f) ≤ q * total cs (L.take t f)`. R2 makes it per family (l. 332–333).
- The names `Asymptote.dissipativeBy`, `Emission.dissipativeBy` and the conjuncts `∀ q, (Asymptote.flow split).DissipativeBy q` of `rest_needs_quantum` and `Emission.flow.DissipativeBy 1` of `arising_needs_quantum` are unchanged. They now assert the weaker property.
- A boundary is stronger the more a witness meets. At R1b these theorems said that even loss in proportion *at every transfer* does not bring rest without a quantum. At R2 they say it only for the family's share.
- Counterreply 11 (l. 3716), "名称与定理的陈述不变，前提变弱，所以每条定理变强", is true of the laws, not of these two witness theorems.
- The study's "按比例耗散的见证（Asymptote、Emission）经 `of_each` 满足它" (l. 3710) is true, but the per-formation fact is no longer stated in the core.
- The negative witnesses (`Circulation`, `Alternation`, `Trickle` `not_dissipativeBy`) became stronger, as the study says.
- Probe Q5 restores the stronger boundary:
  - `EachShare` (R1b's predicate) and `EachShare.dissipativeBy`;
  - `Asymptote.eachShare` for every `q`;
  - `Emission.eachShare` at `1`;
  - `arising_needs_quantum_each`.

**Fix.** Keep a named per-formation predicate in the core (e.g. `Flow.DissipativeEach q`) and state both witness theorems with it.

### W7. Missing statements

**Evidence.**

1. **"Not conversely" has no witness.** Study l. 3710 "反之不然", record hypothesis 2 "not conversely" and study en l. 4200 "not conversely" assert it.
   - Probe `family_share_strictly_weaker`: `FamilyShare.flow` has two formations on one condition, one taking `t+1` and giving `t`, the other taking `t+1` and giving nothing.
   - It is `Dissipative`, meets `DissipativeBy 1`, and fails `EachShare q` for every `q`.
   - The study's example, "一个形成可以无损" (a formation may be lossless), would break the spine's dissipation. The probe keeps it.
2. **The fixed unit is not shown to fail.** The R1 English paragraph (l. 4194) says "Each witness is balanced at a unit splitting without end and dissipative, and lacks one premise". For `Asymptote` and `Emission` the premise lacked is the fixed unit, but their theorems state `BalancesAt` at a refining unit, never `¬ Balances`.
   - Probes `Emission.not_balanced` and `Alternation.not_balanced` derive it from `World.arising_opens`.
   - Probe `Asymptote.not_balanced` derives it, under `rest_needs_quantum`'s own `splits`, from `Flow.Balances.taking_ceases`.
   - For `Circulation` the analogue presumably follows from `World.exchange_stops`; not probed.
3. **Trickle's falling and ceasing.** The study en (l. 4200) and record say counting what relata "gain, lose, begin or end" needs more. `growth_needs_proportion` states only arising.
   - By the definitions (`Trickle.side`, `Trickle.level`, l. 1430–1437), the holder stands at `quarter t + halving t` units of step `t` and at nothing at step `t+1`. So it falls by more than a whole unit and ceases at every step.
   - A core lemma is missing. Not probed here.
4. **Attainment.** The record's limitations say "whether the bounds are attained is not proved"; next step "Whether the bounds are attained".
   - **Exchange bound.** Probe Q7 shows it is attained.
     - `Tight` is a pool of one unit of step 0 at a halving unit, taking one unit of step 0 and giving back half of it at steps 0 and 1. It is `DissipativeBy 1`.
     - `Tight.bound` instantiates `Flow.exchange_bound`.
     - `Tight.attained` (by `rfl`): the count over steps 0–1 equals `p (q + 1) S = 2` at `p = q = S = 1`.
   - **Growth bound (hand argument, not Lean-checked).** It is not attained at `p = q = S = 1`.
     - A gain of one unit needs a replenishment of at least one unit (`BalancesAt.gain_given`).
     - The share then makes the enclosing family lose at least one unit.
     - The standing never exceeds `S`, so nothing remains to stand on, while the gainer stands at a unit.
     - So the tight growth constant may lie below `p q S`; offered as a lead.

**Fix.** State 1–3 in the core. Update the record's attainment limitation with Q7, or move Q7 into the core.

### W8. Quantifier and scope slips

**Evidence and fix.**

1. **"Each continues without end".**
   - Places:
     - record title "and without either each continues without end" / "缺少任一，各自无尽地继续";
     - chapter l. 477 "缺少比例、最小尺度或最小花费，各自无尽地继续";
     - chapter l. 504 "without the share, a least size or a least cost, each continues without end".
   - The witnesses show that change *can* continue: "可以无尽地继续 / can continue without end".
   - "either" also has three antecedents in the chapter.
2. **The exchange law is not a law of enclosures.**
   - Places:
     - chapter l. 504: "the times something takes, gains or arises at least `1/p` of the unit inside an enclosure are bounded by `p` and the share times the total standing (`Flow.exchange_bound`, …)";
     - zh l. 477: "围住之内取用、增长或生起……以 p 与比例乘所立者的总水平为界";
     - root doc l. 250–255: "the times a formation takes, and the times a relatum gains, falls, arises or ceases, at least `1/p` of the unit, inside an enclosure, are bounded by the standing".
   - `Flow.exchange_bound` is stated for a fixed family closed from `T` and is bounded by *its* stock. The record's own limitation says "not read of worlds with changing enclosures".
   - Fix: separate the two: "takings from a family closed from T are bounded by its stock; gains, falls, arisings and ceasings inside an enclosure by the total standing".
3. **"Rest at every resolution".**
   - The record title, `World.rests_at_resolution` docstring and module doc "the rest theorem at every resolution" name rest at each fixed size `1/p`.
   - `Emission` shows that arising itself continues at every resolution, below every size.
   - Fix: "rest at each size, at every resolution / 每一分辨率下每一固定尺度的静止", at least in titles.
4. **"Each boundary is attained".**
   - Root doc l. 256–257 and package README l. 46: "At a unit splitting without end each boundary is attained".
   - The record uses "attained" for tightness of the bounds ("whether the bounds are attained is not proved").
   - Fix: "each boundary is witnessed".

### W9. Bookkeeping

**Evidence and fix.**

1. **Emission's relata.**
   - Record limitations: "the other witnesses have one or two relata" / "其余见证只有一两个关系项".
   - `Emission.flow : Flow (Option Nat) (Option Nat)` (l. 1103), and a new relatum arises at every step.
   - Fix: "Asymptote, Circulation and Dwindle have one relatum, Alternation two; Emission adds one at every step".
2. **"Show the premises independent".**
   - Each witness shows that the one premise it lacks is not implied by those it meets. That is not mutual independence of all premises; the census, embodiment and enclosure have no witness here.
   - Fix: "each shows the premise it lacks is needed given the others".
3. **Trickle docstring.**
   - `Trickle.flow` docstring (l. 1439–1442): "the whole of what the holder holds passes in `halving t` parts, each a quarter as large, in units of step 0, as the parts of the step after next".
   - A part at step `t` is `4 (2^t + 1)` units of step `t+1`, that is `(2^t + 1)/4^t` of step 0. The ratio of a part at `t` to a part at `t + 2` is `16 (2^t + 1)/(2^(t+2) + 1)`: 6.4 at `t = 0`, tending to 4.
   - So parts at `t` are about *four times* those of the step after next.
   - Fix: "each about four times as large, in units of step 0, as the parts of the step after next", or "about half those of the step before".

### W10. Naming and provenance

**Evidence and fix.**

1. **"Least cost / 最小花费".**
   - Where: module doc l. 82–83 "only with a least cost per active step"; record title "a least cost bounds the end a reserve defers"; chapter l. 477, 504 and §9; plan R1b; `reserve_needs_quantum` docstring.
   - The word is financial. Ren's 10-10 criteria ask for formal, scientific or systems names; the fourteenth review flagged `credits` and `overdraw` on the same ground.
   - `Web.CarriesAt` says the reserve falls by at least `1/p` at each active step beyond support.
   - Suggest "a least fall of the reserve per active step / 每个活跃步储备的最小下降". The module already says "a reserve that only falls".
2. **"Share".**
   - Uses:
     - "dissipated on by the share `q`" (l. 335–336) uses `q` as an index whose returned fraction is `q/(q+1)`;
     - chapter "loses a fixed share of what is taken" uses the lost fraction;
     - "the family's share" uses the premise.
   - The Chinese already uses 比例.
   - Suggest "proportion lost (at least `1/(q+1)`)" or "return ratio `q/(q+1)`", and fix one referent.
3. **Carriers.** `Trickle.carriers` and "carriers" in prose collide with the reserve's `Web.Carries`, `Web.CarriesAt` and `Web.CarriesIn` in the same module. Suggest "conduits" for Trickle.
4. **"The loss law".**
   - The module doc l. 16 and the `losses_bound` docstring (l. 210) use it for the abstract count `losses_bound`.
   - The root doc l. 250 uses it for the quantum bound.
   - Use one referent.
5. **Provenance.**
   - The record correspondence begins "The author's reading (an AI argument)" and ends "The readings are Ren's." The limitations end "names and readings are Ren's" / "名称与读法属于 Ren".
   - `git grep` finds the phrase in no other record.
   - Read literally, it attributes the AI's readings, including the overclaim of W1, to Ren. AGENTS asks to "Distinguish Ren's words from AI elaboration".
   - Suggest the study's own formula, "AI reading, pending Ren / 读法（AI，待 Ren）", and, if meant, "the choice of reading and names is Ren's".

### W11. Method: Trickle's carriers never stand

**Evidence.**

- `Trickle.web` makes a relatum active exactly while it stands (l. 1448–1449). The carriers `.inr i` have `side t (.inr _) = 0`, so they never stand and are never active.
- The flow therefore fails "only active relata taking/giving" (`Flow.Taking`, `Flow.Acting`). These are premises the spine's world laws can carry; the growth law does not assume them.
- The witness is fair for the theorem stated. The author discloses it in counterreply 12, the limitations, the next step and the commit's "Open".
- Under the nondual method a transfer is a relation that forms between the sides. Conveyance through relata that stand at nothing separates "who carries" from what is carried, a representational device rather than a formed relation. The boundary would be stronger with active carriers.
- Q4 says what any variant must keep: unboundedly many transfers in one step.

**Suggestion (sketch, not checked).** Let the holder seed the next step's carriers with one unit of the step after each, so they stand and are active. They take from the holder and give to the other side, the seeds counted in the standing and arising at vanishing sizes. Then check that `Flow.Acting`, `Flow.Taking` and the census still hold.

## 3. The Pareto frontier: what the probes add

| Probe group | Main declaration | What it shows | Where it would go |
|---|---|---|---|
| Q1 | `family_share_strictly_weaker` | The per-family share is strictly weaker than the per-formation share, even for a spine-dissipative flow | Resolution, next to `DissipatesBy.of_each` |
| Q2 | `quantum_bound_of_not_gained`, `quantum_needs_not_gained` | The quantum law needs only that the family is not gained on (no closure, distinctness or unit loss); without that, it fails (`Pump`) | Replace the premise of `Flow.quantum_bound` |
| Q3 | `exchange_bound_of_least_loss_not_gaining`, `lossless_not_gaining_not_dissipative` | The least-loss exchange law needs only per-formation non-gain, strictly weaker than `Dissipative` | Replace the premise of `exchange_bound_of_least_loss` |
| Q4 | `growth_bound_of_replenished_loss`, `share_replenishedLoses`, `fixed_replenishedLoses`, `few_replenishedLoses`, `growth_bound_of_least_loss_few`, `replenishedLoses_strictly_weaker`, `growth_needs_bounded_transfers` | A premise strictly weaker than the share gives the growth law and non-recurrence of arising; it unifies the spine (m = 1), the share (m = p q) and least loss with bounded transfers; Trickle lacks exactly bounded transfers | Resolution; answers R2's open item |
| Q5 | `EachShare`, `Asymptote.eachShare`, `Emission.eachShare`, `arising_needs_quantum_each` | The two witnesses meet loss in proportion at every transfer | Restore R1b's stronger boundary |
| Q6 | `Emission.not_balanced`, `Alternation.not_balanced`, `Asymptote.not_balanced` | Witnesses that drop the fixed unit fail it | Complete the boundary theorems |
| Q7 | `Tight.attained` | The exchange bound `p (q + 1) S` is attained at `p = q = S = 1` | Resolution; update the record's limitation |

Still open after the probes:

- the fall and ceasing laws under `ReplenishedLoses`;
- whether `ReplenishedLoses` is itself the weakest such premise;
- a refining-unit witness separating it from the share;
- the tight growth constant;
- active carriers.

## 4. What remains sound

- **The design.**
  - `losses_invariant`/`losses_bound` separate the counting argument from the dynamics.
  - `bounded_not_recurring` separates the bound from non-recurrence.
  - Every law reduces to one invariant. Q4 reuses `losses_bound` unchanged, with one quantum per step at which something gains.
- **Connection to the spine** by instance theorems, as AGENTS asks:
  - `Flow.balancesAt_one`;
  - `Flow.taking_stops`, reducing to `Flow.Balances.taking_ceases`;
  - `Web.Carries.carriesAt` and `Web.carriesIn_one`.
- **R2's per-family restatement.** Every proof used only `DissipatesBy.replenishment_le`, `BalancesAt.nonrisingBy` and `lowersBy` on the family's total, so every law strengthened. The witnesses dissipative by no share (Circulation, Alternation, Trickle) now fail the weaker premise, a stronger negation.
- **Fair witnesses.** Each meets the stated premises of the theorems it bounds. `Trickle` meets `Counted`, `Embodied`, `BalancesAt 4`, `Dissipative`, `Enclosed` and `LosesAtEverySize quarter`, and its transfers of each fixed size stop (`Trickle.exchange_stops`).
- **Honest counterreview.** Counterreplies 12 and 13 state exactly what Trickle shows and does not show. The record's limitations and next step list the open premise question and the inactive carriers.
- **Preserved history.** Historical §59 and plan R1 text are kept, as counterreply 11 says. The failed first R1 run is retained and named (`20261010T154024.599588Z`).
- **Labelled readings.** The study's readings are labelled "AI, pending Ren" (§59.2 读法; R1 "On the AI's reading, pending Ren"), and the premises awaiting Ren are named.
- **Bookkeeping.** Counts, receipts, hashes and retained artifacts are accurate throughout.

## 5. What would change the verdicts

- **W1.** A core theorem showing that, among premises on the family's totals invariant under the representation, the share is the weakest giving the growth law with constant `p q S`, would turn W1 into a matter of wording. The necessity claim as written would still be false.
- **W4 and W5.** A definition elsewhere under which "closed family" includes being dissipated on would withdraw W4. None was found in `Dissipation.lean` (l. 219–235) or `Flow.lean`.
- **W6.** If the boundary theorems are meant to show only that the per-family premise is not enough, W6 is a choice, not a regression. The study's sentence would then need to say so.
- **W7.4.** A Lean proof that the growth bound is attained at some `p, q, S` would refute the hand argument's lead (it covers only `p = q = S = 1`).
- **W11.** Ren judging zero-level conveyance an acceptable relation would withdraw W11.
- **Overall.** Contradictory evidence in a later commit outranks these labels; this review covers `658db670`, `e79e00e5` and `de17f533` only.

## Appendix A. Probe source

`review/probes/Review15.lean` (sha256 `1a026465303f31ec3b6978807caf8e09d7b8fe9b211dd31dadb78c3568783ea1`, 749 lines). It was compiled in `review/probes/` with `env LEAN_PATH=../build_r2 lean +leanprover/lean4:v4.29.1 -o Review15.olean Review15.lean` against the core rebuilt from the prelude at `de17f533`. Exit 0, no output.

Groups:

- **Helper.** `left_cancel`, axiom-free left cancellation.
- **Q1 (W7.1).** `EachShare`, `EachShare.dissipativeBy`, `FamilyShare.*`, `family_share_strictly_weaker`.
- **Q2 (W4, W5).** `quantum_bound_of_not_gained`, `not_gained_of_dissipative`, `Pump.*`, `quantum_needs_not_gained`.
- **Q3 (W5).** `NotGaining`, `Dissipative.notGaining`, `losesAtSize_over`, `exchange_bound_of_least_loss_not_gaining`, `lossless`, `lossless_not_gaining_not_dissipative`.
- **Q5 (W6).** `Asymptote.eachShare`, `Emission.eachShare`, `arising_needs_quantum_each`.
- **Q6 (W7.2).** `Emission.not_balanced`, `Alternation.not_balanced`, `Asymptote.not_balanced`.
- **Q4 (W1).**
  - The premise and its steps: `ReplenishedLoses`, `lose_step`, `keep_step`, `over_standing`, `replenished_step`, `standing_nonrising`, `standing_within`, `gainers_size`.
  - The laws: `growth_bound_of_replenished_loss`, `growth_not_recurring_of_replenished_loss`, `arising_not_recurring_of_replenished_loss`.
  - The three sources: `share_replenishedLoses`, `exists_large`, `few_replenishedLoses`, `fixed_replenishedLoses`, `growth_bound_of_least_loss_few`.
  - Trickle and strictness: `lt_halving`, `Trickle.transfers_unbounded`, `Trickle.not_replenishedLoses`, `growth_needs_bounded_transfers`, `Tick.*`, `replenishedLoses_strictly_weaker`.
- **Q7 (W7.4).** `Tight.*`, with `Tight.attained`.

```lean
/-
Fifteenth independent review, probes (R1, R1b, R2: `Becoming.Resolution`). Not part of the
repository. Compiled against the core at `de17f533` (Resolution sha256 374611f2…), rebuilt
from the prelude with Lean 4.29.1. Every constant here must depend on no axiom
(`Review15Audit.lean`).
-/
import Becoming

namespace Review15

open Becoming

variable {F C : Type}

/-- Left cancellation, through the core's axiom-free right cancellation (the prelude's own
left cancellation lemma for `Nat` depends on `propext`). -/
theorem left_cancel {a b c : Nat} (le : a + b ≤ a + c) : b ≤ c :=
  le_of_add_le_add_right a (Nat.le_trans (Nat.le_of_eq (Nat.add_comm b a))
    (Nat.le_trans le (Nat.le_of_eq (Nat.add_comm a c))))

/-! ## Q1. The share per family is strictly weaker than the share per formation

`Flow.DissipatesBy` (R2) asks the closed family to get back at most `q` parts in `q + 1`.
The per-formation form (`EachShare`) gives it (`Flow.DissipatesBy.of_each`). Study §59.2 says
the converse fails; here is a witness: a dissipative flow, sharing by `1` per family, with no
per-formation share for any `q`. One formation loses one unit of a growing take, the other
loses all it takes. -/

/-- Loss in proportion at each transfer: every formation taking part gives every closed
family without repetition at most `q` parts in `q + 1` of what it takes from it. -/
def EachShare (L : Flow F C) (q : Nat) : Prop :=
  ∀ cs t, Distinct cs → L.ClosedAt cs t → ∀ f, f ∈ L.present t →
    (q + 1) * total cs (L.give t f) ≤ q * total cs (L.take t f)

theorem EachShare.dissipativeBy {L : Flow F C} {q : Nat} (each : EachShare L q) :
    L.DissipativeBy q :=
  fun cs t distinct closed => Flow.DissipatesBy.of_each (each cs t distinct closed)

namespace FamilyShare

/-- Two formations on one condition: `true` takes `t + 1` and gives back `t`; `false` takes
`t + 1` and gives nothing. -/
def flow : Flow Bool Unit :=
  ⟨fun _ => [true, false], fun t _ _ => t + 1, fun t f _ => match f with
    | true => t
    | false => 0⟩

theorem closed (t : Nat) : flow.ClosedAt [()] t :=
  fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside

theorem distinct : Distinct [()] :=
  ⟨(fun mem => nomatch mem), trivial⟩

theorem dissipative : flow.Dissipative :=
  fun cs t distinct _ f _ => match cs, distinct, f with
  | [], _, _ => Nat.le_refl 0
  | [()], _, true => Nat.le_refl (t + 1)
  | [()], _, false => Nat.le_trans (Nat.le_of_eq (Nat.zero_add 1))
      (Nat.succ_le_succ (Nat.zero_le t))
  | () :: () :: _, ⟨fresh, _⟩, _ => absurd (List.Mem.head _) fresh

theorem given (t : Nat) : flow.given t () = t := rfl

theorem taken (t : Nat) : flow.taken t () = (t + 1) + (t + 1) := rfl

theorem two_mul (t : Nat) : (1 + 1) * t = t + t :=
  (add_mul_split 1 1 t).trans
    ((congrArg (· + 1 * t) (Nat.one_mul t)).trans (congrArg (t + ·) (Nat.one_mul t)))

/-- Per family, the flow gives back at most half of what is taken. -/
theorem dissipativeBy : flow.DissipativeBy 1 :=
  fun cs t distinct _ => match cs, distinct with
  | [], _ => Nat.zero_le _
  | [()], _ => show (1 + 1) * (flow.given t () + 0) ≤ 1 * (flow.taken t () + 0) from
      Nat.le_trans (Nat.le_of_eq (two_mul t))
        (Nat.le_trans (Nat.add_le_add (Nat.le_succ t) (Nat.le_succ t))
          (Nat.le_of_eq (Nat.one_mul _).symm))
  | () :: () :: _, ⟨fresh, _⟩ => absurd (List.Mem.head _) fresh

/-- No share holds formation by formation: at step `q + 1`, `true` gives back `q + 1` of
`q + 2`. -/
theorem not_each (q : Nat) : ¬ EachShare flow q :=
  fun each =>
    have le : (q + 1) * (q + 1 + 0) ≤ q * (q + 1 + 1 + 0) :=
      each [()] (q + 1) distinct (closed (q + 1)) true (List.Mem.head _)
    Nat.not_succ_le_self q (left_cancel (a := q * (q + 1)) (calc
      q * (q + 1) + (q + 1) = (q + 1) * (q + 1 + 0) :=
          ((congrArg (q * (q + 1) + ·) (Nat.one_mul (q + 1)).symm).trans
            (add_mul_split q 1 (q + 1)).symm)
      _ ≤ q * (q + 1 + 1 + 0) := le
      _ = q * (q + 1) + q := (Nat.left_distrib q (q + 1) 1).trans
          (congrArg (q * (q + 1) + ·) (Nat.mul_one q))))

end FamilyShare

/-- The per-family share is strictly weaker than the per-formation share, even for a flow
that dissipates in the spine's sense. -/
theorem family_share_strictly_weaker :
    FamilyShare.flow.Dissipative ∧ FamilyShare.flow.DissipativeBy 1 ∧
      ∀ q, ¬ EachShare FamilyShare.flow q :=
  ⟨FamilyShare.dissipative, FamilyShare.dissipativeBy, FamilyShare.not_each⟩

/-! ## Q2. The quantum law needs only that the family is not gained on

`Flow.quantum_bound` assumes the flow dissipative and the family without repetition and
closed from `T` on. Its proof uses only that the family's stock never rises in the finer unit,
which follows from the family's replenishment being within its uptake. Neither closure,
distinctness, the spine's unit loss nor any share is needed. -/

theorem quantum_bound_of_not_gained {L : Flow F C} {W : Web F C} {r R : Nat → Nat}
    (balances : L.BalancesAt r W) {cs : List C} {T : Nat}
    (notGained : ∀ t, T ≤ t → L.replenishment cs t ≤ L.uptake cs t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t)
    (q n : Nat) :
    total (steps T n) (fun u => mark (LosesQuantum r R (W.stock cs) q u)) ≤ q * W.stock cs T :=
  Becoming.quantum_bound base unit refining (fun u later =>
    le_of_add_le_add_right (L.replenishment cs u)
      (Nat.le_trans (Nat.add_le_add_left (notGained u later) _)
        (Nat.le_of_eq (balances.over cs u)))) n

/-- The core's premise gives it. -/
theorem not_gained_of_dissipative {L : Flow F C} (dissipative : L.Dissipative) {cs : List C}
    (distinct : Distinct cs) {T : Nat} (closed : ∀ t, T ≤ t → L.ClosedAt cs t) :
    ∀ t, T ≤ t → L.replenishment cs t ≤ L.uptake cs t :=
  fun t later => Nat.le_trans (Nat.le_add_right _ _)
    (dissipative cs t distinct (closed t later)).replenishment_takers

/-! The premise cannot be dropped, even at a fixed unit and for a closed family: in `Pump` a
formation gives one unit to a pool from nothing at even steps and takes it at odd steps. The
flow balances, the pool is closed, and the pool loses a whole unit at arbitrarily late steps. -/

namespace Pump

def level : Nat → Nat
  | 0 => 0
  | 1 => 1
  | t + 2 => level t

def give : Nat → Nat
  | 0 => 1
  | 1 => 0
  | t + 2 => give t

def take : Nat → Nat
  | 0 => 0
  | 1 => 1
  | t + 2 => take t

def flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun t _ _ => take t, fun t _ _ => give t⟩

def web : Web Unit Unit :=
  ⟨fun t _ => level t, fun _ _ => True, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => True⟩

theorem balances_at : ∀ t, level (t + 1) + (take t + 0) = 1 * level t + (give t + 0)
  | 0 => rfl
  | 1 => rfl
  | t + 2 => balances_at t

theorem balances : flow.BalancesAt (fun _ => 1) web :=
  fun t c => match c with
  | () => balances_at t

theorem closed (t : Nat) : flow.ClosedAt [()] t :=
  fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside

theorem odd_level : ∀ k, level (2 * k + 1) = 1 ∧ level (2 * k + 1 + 1) = 0
  | 0 => ⟨rfl, rfl⟩
  | k + 1 => odd_level k

theorem loses_recurs :
    ∀ N, ∃ t, N ≤ t ∧ LosesQuantum (fun _ => 1) (fun _ => 1) (web.stock [()]) 1 t :=
  fun N => ⟨2 * N + 1,
    Nat.le_trans (Nat.le_trans (Nat.le_of_eq (Nat.one_mul N).symm)
      (Nat.mul_le_mul_right N (Nat.le_succ 1))) (Nat.le_succ _),
    show 1 + 1 * (level (2 * N + 1 + 1) + 0) ≤ 1 * (1 * (level (2 * N + 1) + 0)) from
      Nat.le_of_eq ((congrArg (fun k => 1 + 1 * (k + 0)) (odd_level N).2).trans
        (congrArg (fun k => 1 * (1 * (k + 0))) (odd_level N).1).symm)⟩

end Pump

/-- So the quantum law on flows needs its non-gain premise: `Pump` is balanced at the fixed
unit, its pool is closed at every step, and losing a quantum recurs. -/
theorem quantum_needs_not_gained :
    Pump.flow.BalancesAt (fun _ => 1) Pump.web ∧ (∀ t, Pump.flow.ClosedAt [()] t) ∧
      Distinct [()] ∧
      ∀ N, ∃ t, N ≤ t ∧ LosesQuantum (fun _ => 1) (fun _ => 1) (Pump.web.stock [()]) 1 t :=
  ⟨Pump.balances, Pump.closed, FamilyShare.distinct, Pump.loses_recurs⟩

/-! ## Q3. The least-loss exchange law needs only that no formation gains on the family

`Flow.exchange_bound_of_least_loss` assumes `Flow.Dissipative`, whose unit loss per take
(`sign`) is not used: the proof uses only `Flow.DissipatesOn.give_le`. -/

/-- No formation taking part gives a closed family without repetition more than it takes. -/
def NotGaining (L : Flow F C) : Prop :=
  ∀ cs t, Distinct cs → L.ClosedAt cs t → ∀ f, f ∈ L.present t →
    total cs (L.give t f) ≤ total cs (L.take t f)

theorem Dissipative.notGaining {L : Flow F C} (dissipative : L.Dissipative) : NotGaining L :=
  fun cs t distinct closed _ present => (dissipative cs t distinct closed).give_le present

theorem losesAtSize_over {L : Flow F C} {R : Nat → Nat} {p m : Nat} {cs : List C} {t : Nat}
    (giveLe : ∀ f, f ∈ L.present t → total cs (L.give t f) ≤ total cs (L.take t f))
    (loses : L.LosesAtSize R p m cs t) :
    m * L.replenishment cs t + L.takersAbove R p cs t * R (t + 1) ≤ m * L.uptake cs t :=
  calc m * L.replenishment cs t + L.takersAbove R p cs t * R (t + 1)
      = total (L.present t) (fun f => m * total cs (L.give t f)) +
          total (L.present t) (fun f => mark (R (t + 1) ≤ p * total cs (L.take t f)) *
            R (t + 1)) :=
        (congrArg (· + L.takersAbove R p cs t * R (t + 1))
          ((congrArg (m * ·) (total_swap (fun f c => L.give t f c) cs (L.present t)).symm).trans
            (total_mul m (fun f => total cs (L.give t f)) (L.present t)).symm)).trans
          (congrArg (total (L.present t) (fun f => m * total cs (L.give t f)) + ·)
            (Flow.total_mul_right _ _ _))
    _ = total (L.present t) (fun f => m * total cs (L.give t f) +
          mark (R (t + 1) ≤ p * total cs (L.take t f)) * R (t + 1)) :=
        (total_add _ _ _).symm
    _ ≤ total (L.present t) (fun f => m * total cs (L.take t f)) :=
        total_le (L.present t) fun f present => mark_cases
          (q := fun k => m * total cs (L.give t f) + k * R (t + 1) ≤ m * total cs (L.take t f))
          (fun takes => Nat.le_trans (Nat.le_of_eq ((congrArg (m * total cs (L.give t f) + ·)
              (Nat.one_mul _)).trans (Nat.add_comm _ _))) (loses f present takes))
          (fun _ => Nat.le_trans (Nat.le_of_eq ((congrArg (m * total cs (L.give t f) + ·)
              (Nat.zero_mul _)).trans (Nat.add_zero _)))
            (Nat.mul_le_mul_left m (giveLe f present)))
    _ = m * L.uptake cs t :=
        (total_mul m (fun f => total cs (L.take t f)) (L.present t)).trans
          (congrArg (m * ·) (total_swap (fun f c => L.take t f c) cs (L.present t)))

theorem exchange_bound_of_least_loss_not_gaining {L : Flow F C} {W : Web F C}
    {r : Nat → Nat} (balances : L.BalancesAt r W) (notGaining : NotGaining L) {R : Nat → Nat}
    {p m : Nat} (loses : ∀ cs t, Distinct cs → L.ClosedAt cs t → L.LosesAtSize R p m cs t)
    {cs : List C} (distinct : Distinct cs) {T : Nat} (closed : ∀ t, T ≤ t → L.ClosedAt cs t)
    (base : R T = 1) (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t)
    (refining : ∀ t, T ≤ t → 0 < r t) (n : Nat) :
    total (steps T n) (L.takersAbove R p cs) ≤ m * W.stock cs T :=
  losses_bound base unit refining (fun t later =>
    le_of_add_le_add_right (m * L.replenishment cs t) (calc
      m * W.stock cs (t + 1) + L.takersAbove R p cs t * R (t + 1) + m * L.replenishment cs t
          = m * W.stock cs (t + 1) +
              (m * L.replenishment cs t + L.takersAbove R p cs t * R (t + 1)) :=
            (Nat.add_assoc _ _ _).trans (congrArg (m * W.stock cs (t + 1) + ·) (Nat.add_comm _ _))
      _ ≤ m * W.stock cs (t + 1) + m * L.uptake cs t :=
            Nat.add_le_add_left (losesAtSize_over
              (notGaining cs t distinct (closed t later)) (loses cs t distinct (closed t later))) _
      _ = m * (r t * W.stock cs t) + m * L.replenishment cs t :=
            (Nat.left_distrib _ _ _).symm.trans ((congrArg (m * ·) (balances.over cs t)).trans
              (Nat.left_distrib _ _ _)))) n

/-- Not gaining is strictly weaker than the spine's dissipation: a lossless transfer. -/
def lossless : Flow Unit Unit :=
  ⟨fun _ => [()], fun _ _ _ => 1, fun _ _ _ => 1⟩

theorem lossless_not_gaining_not_dissipative :
    NotGaining lossless ∧ ¬ lossless.Dissipative :=
  ⟨fun cs _ _ _ _ _ => Nat.le_refl (total cs fun _ => 1),
   fun dissipative => Nat.not_succ_le_self 1
     (dissipative [()] 0 ⟨(fun mem => nomatch mem), trivial⟩
       (fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside)
       () (List.Mem.head _))⟩

/-! ## Q5. The witnesses that share keep the stronger, per-formation share

After R2, `rest_needs_quantum` and `arising_needs_quantum` state only the per-family share for
`Asymptote` and `Emission`. Both meet the per-formation share, which is the stronger boundary:
even loss in proportion at every single transfer does not bring them to rest. -/

theorem Asymptote.eachShare (split : Nat → Nat) (q : Nat) :
    EachShare (Asymptote.flow split) q :=
  fun cs _ _ _ _ _ => Nat.le_trans (Nat.le_of_eq ((congrArg ((q + 1) * ·) (total_zero cs)).trans
    (Nat.mul_zero _))) (Nat.zero_le _)

theorem Emission.eachShare : EachShare Emission.flow 1 :=
  fun _ _ distinct closed _ _ =>
    Nat.le_trans (Nat.mul_le_mul_left 2 (Emission.emitted_le_one distinct))
      (Nat.le_trans (le_total_of_mem (q := Emission.drawn) (Emission.pool_mem closed))
        (Nat.le_of_eq (Nat.one_mul _).symm))

theorem arising_needs_quantum_each :
    Emission.world.Counted ∧ Emission.world.Embodied ∧
      Emission.flow.BalancesAt (fun _ => 2) Emission.web ∧ Emission.world.Dissipative ∧
      EachShare Emission.flow 1 ∧
      (∀ t, Emission.world.flow.Enclosed t) ∧ Emission.world.ArisingRecurs :=
  ⟨Emission.counted, Emission.embodied, Emission.balances, Emission.dissipative,
    Emission.eachShare, Emission.enclosed, Emission.arising_recurs⟩

/-! ## Q6. Each witness that drops the fixed unit fails it

The boundary theorems for `Asymptote` and `Emission` drop the fixed unit; the core does not
state that they fail it. They do, by the spine's laws. -/

theorem Emission.not_balanced : ¬ Emission.world.Balanced :=
  fun balanced => World.arising_opens Emission.counted Emission.embodied balanced
    Emission.dissipative Emission.arising_recurs 0 fun t _ => Emission.enclosed t

theorem Alternation.not_balanced : ¬ Alternation.world.Balanced :=
  fun balanced => World.arising_opens Alternation.counted Alternation.embodied balanced
    Alternation.dissipative Alternation.arising_recurs 0 fun t _ => Alternation.enclosed t

theorem Asymptote.not_balanced (split : Nat → Nat) (splits : ∀ N, ∃ t, N ≤ t ∧ 0 < split t) :
    ¬ (Asymptote.flow split).Balances (Asymptote.web split) :=
  fun balances => Flow.Balances.taking_ceases balances (T := 0)
    (fun t _ => Asymptote.dissipative split [()] t Asymptote.distinct (Asymptote.closed split t))
    (Asymptote.taking_recurs split splits)

/-! ## Q4. A premise strictly weaker than the family's share that gives the growth law

Study §59.2 and plan R2 leave open "a premise weaker than the family's share that still gives
the growth law". One is a least loss at each size of what the family is given: where a closed
family is given at least `1/p` of the unit, it loses at least `1/m` of it. With the family not
gained on, it bounds the times a relatum gains at least `1/p` of the unit by `p S · m S`, `S`
the total standing at `T`. The share gives it (`m = p q`); so does a least loss at each size
of transfer with at most `K` transfers per step (`m` of size `p K`); and so does the spine's
dissipation at a fixed unit (`m = 1`). `Trickle` has unboundedly many transfers per step and
meets it for no `m`. -/

/-- Where the family is given at least `1/p` of the unit counted by `R` across the step from
`t`, it loses at least `1/m` of it. -/
def ReplenishedLoses (L : Flow F C) (R : Nat → Nat) (p m : Nat) (cs : List C) (t : Nat) :
    Prop :=
  R (t + 1) ≤ p * L.replenishment cs t → R (t + 1) + m * L.replenishment cs t ≤ m * L.uptake cs t

theorem lose_step {m s1 R up rep rr : Nat} (over : s1 + up = rr + rep)
    (family : R + m * rep ≤ m * up) : m * s1 + 1 * R ≤ m * rr :=
  le_of_add_le_add_right (m * rep) (calc
    m * s1 + 1 * R + m * rep = m * s1 + (R + m * rep) :=
        (congrArg (· + m * rep) (congrArg (m * s1 + ·) (Nat.one_mul R))).trans
          (Nat.add_assoc _ _ _)
    _ ≤ m * s1 + m * up := Nat.add_le_add_left family _
    _ = m * (rr + rep) := (Nat.left_distrib _ _ _).symm.trans (congrArg (m * ·) over)
    _ = m * rr + m * rep := Nat.left_distrib _ _ _)

theorem keep_step {m s1 R up rep rr : Nat} (over : s1 + up = rr + rep) (notGained : rep ≤ up) :
    m * s1 + 0 * R ≤ m * rr :=
  Nat.le_trans (Nat.le_of_eq ((congrArg (m * s1 + ·) (Nat.zero_mul R)).trans (Nat.add_zero _)))
    (Nat.mul_le_mul_left m (le_of_add_le_add_right rep
      (Nat.le_trans (Nat.add_le_add_left notGained s1) (Nat.le_of_eq over))))

section Growth

variable {w : World} {alive : Nat → List w.Relatum} {r R : Nat → Nat} {p m : Nat}

/-- Balance across a step, read on what stands, through a family enclosing it. -/
theorem over_standing (census : w.web.Census alive) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {es : List w.Relatum} {t : Nat}
    (distinct : Distinct es) (before : ∀ c, c ∈ alive t → c ∈ es)
    (after : ∀ c, c ∈ alive (t + 1) → c ∈ es) :
    w.web.stock (alive (t + 1)) (t + 1) + w.flow.uptake es t =
      r t * w.web.stock (alive t) t + w.flow.replenishment es t :=
  have standing := World.standingCensus census embodied
  (congrArg (· + w.flow.uptake es t) (standing.stock_eq distinct after)).trans
    ((balances.over es t).trans (congrArg (fun k => r t * k + w.flow.replenishment es t)
      (standing.stock_eq distinct before).symm))

/-- Across a step enclosed around what stands, where some relatum gains at least `1/p` of the
unit, the standing falls by at least `1/m` of it; otherwise it does not rise. -/
theorem replenished_step (census : w.web.Census alive) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {t : Nat}
    (notGained : ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (loses : ∀ cs, Distinct cs → w.flow.ClosedAt cs t → ReplenishedLoses w.flow R p m cs t)
    (enclosed : w.flow.Enclosed t) :
    m * w.web.stock (alive (t + 1)) (t + 1) +
        mark (0 < w.web.gainers r R p t (alive (t + 1))) * R (t + 1) ≤
      m * (r t * w.web.stock (alive t) t) :=
  Decidable.of_not_not fun no => enclosed.aroundStanding_not_not alive
    fun ⟨es, distinct, before, after, closed⟩ =>
      have over := over_standing census embodied balances distinct before after
      no (mark_cases (q := fun k => m * w.web.stock (alive (t + 1)) (t + 1) + k * R (t + 1) ≤
            m * (r t * w.web.stock (alive t) t))
        (fun pos => match total_pos (alive (t + 1)) pos with
          | ⟨c, mem, positive⟩ =>
            lose_step over (loses es distinct closed (Nat.le_trans
              (balances.gain_given (mark_pos.mp positive))
              (Nat.mul_le_mul_left p (le_total_of_mem (q := w.flow.given t) (after c mem))))))
        (fun _ => keep_step over (notGained es distinct closed)))

/-- Not gained on, the standing does not rise across a step enclosed around it. -/
theorem standing_nonrising (census : w.web.Census alive) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {t : Nat}
    (notGained : ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (enclosed : w.flow.Enclosed t) :
    w.web.stock (alive (t + 1)) (t + 1) ≤ r t * w.web.stock (alive t) t :=
  Decidable.of_not_not fun no => enclosed.aroundStanding_not_not alive
    fun ⟨es, distinct, before, after, closed⟩ =>
      no (le_of_add_le_add_right (w.flow.replenishment es t)
        (Nat.le_trans (Nat.add_le_add_left (notGained es distinct closed) _)
          (Nat.le_of_eq (over_standing census embodied balances distinct before after))))

/-- From `T` on, the standing never exceeds its value at `T`, counted in the unit of `T`. -/
theorem standing_within (census : w.web.Census alive) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {T : Nat}
    (notGained : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (n : Nat) :
    w.web.stock (alive (T + n)) (T + n) ≤ w.web.stock (alive T) T * R (T + n) :=
  Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm)
    (Nat.le_trans (Nat.le_add_right _ _)
      (Nat.le_trans (losses_invariant (s := fun t => w.web.stock (alive t) t)
          (k := fun _ => 0) (q := 1) base unit (fun t later => Nat.le_trans (Nat.le_of_eq
            ((congrArg (· + 0 * R (t + 1)) (Nat.one_mul _)).trans
              ((congrArg (w.web.stock (alive (t + 1)) (t + 1) + ·) (Nat.zero_mul _)).trans
                (Nat.add_zero _))))
            (Nat.le_trans (standing_nonrising census embodied balances (notGained t later)
              (enclosed t later)) (Nat.le_of_eq (Nat.one_mul _).symm))) n)
        (Nat.le_of_eq (congrArg (· * R (T + n)) (Nat.one_mul _)))))

/-- The members gaining at least `1/p` of the unit across a step are at most `p` times the
standing after it, in units of the step after. -/
theorem gainers_size (t : Nat) :
    w.web.gainers r R p t (alive (t + 1)) * R (t + 1) ≤ p * w.web.stock (alive (t + 1)) (t + 1) :=
  Nat.le_trans (Nat.le_of_eq (Flow.total_mul_right _ _ _))
    (Nat.le_trans (total_le (alive (t + 1)) fun c _ => mark_cases
        (q := fun k => k * R (t + 1) ≤ p * w.web.level (t + 1) c)
        (fun gains => Nat.le_trans (Nat.le_of_eq (Nat.one_mul _))
          (Nat.le_trans (Nat.le_add_right _ _) gains))
        (fun _ => Nat.le_trans (Nat.le_of_eq (Nat.zero_mul _)) (Nat.zero_le _)))
      (Nat.le_of_eq (total_mul p (w.web.level (t + 1)) (alive (t + 1)))))

/-- The growth law under a least loss at each size of what is given. In a world with a census
whose relata are embodied, balanced at a resolution that only refines, with every step from
`T` on enclosed and every closed family from `T` on not gained on and losing at least `1/m` of
the unit where it is given at least `1/p` of it, the times since `T` that a relatum gains at
least `1/p` of the unit, counted relatum by relatum, number at most `p S · m S`, `S` the total
standing at `T`. -/
theorem growth_bound_of_replenished_loss (census : w.web.Census alive) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {T : Nat}
    (notGained : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (loses : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      ReplenishedLoses w.flow R p m cs t)
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t) (n : Nat) :
    total (steps T n) (fun t => w.web.gainers r R p t (alive (t + 1))) ≤
      p * w.web.stock (alive T) T * (m * w.web.stock (alive T) T) :=
  have count : total (steps T n) (fun t => mark (0 < w.web.gainers r R p t (alive (t + 1)))) ≤
      m * w.web.stock (alive T) T :=
    losses_bound (s := fun t => w.web.stock (alive t) t) base unit refining
      (fun t later => replenished_step census embodied balances (notGained t later)
        (loses t later) (enclosed t later)) n
  have each : ∀ t, t ∈ steps T n → w.web.gainers r R p t (alive (t + 1)) ≤
      mark (0 < w.web.gainers r R p t (alive (t + 1))) * (p * w.web.stock (alive T) T) :=
    fun t mem => mark_cases (q := fun k => w.web.gainers r R p t (alive (t + 1)) ≤
        k * (p * w.web.stock (alive T) T))
      (fun _ =>
        have later : T ≤ t := steps_mem mem
        match Nat.le.dest later with
        | ⟨j, same⟩ =>
          have within : w.web.stock (alive (t + 1)) (t + 1) ≤
              w.web.stock (alive T) T * R (t + 1) :=
            Eq.subst (motive := fun u => w.web.stock (alive (u + 1)) (u + 1) ≤
                w.web.stock (alive T) T * R (u + 1)) same
              (standing_within census embodied balances notGained enclosed base unit (j + 1) :
                w.web.stock (alive (T + j + 1)) (T + j + 1) ≤ w.web.stock (alive T) T * R (T + j + 1))
          Nat.le_trans (Nat.le_of_mul_le_mul_right
              (Nat.le_trans (gainers_size t) (Nat.le_trans (Nat.mul_le_mul_left p within)
                (Nat.le_of_eq (mul_regroup p _ _).symm)))
              (units_pos base unit refining (Nat.le_succ_of_le later)))
            (Nat.le_of_eq (Nat.one_mul _).symm))
      (fun zero => Nat.le_of_eq ((eq_zero_of_not_pos zero).trans (Nat.zero_mul _).symm))
  Nat.le_trans (total_le (steps T n) each)
    (Nat.le_trans (Nat.le_of_eq (Flow.total_mul_right _ _ _).symm)
      (Nat.le_trans (Nat.mul_le_mul_right _ count) (Nat.le_of_eq (Nat.mul_comm _ _))))

/-- So no relatum gains at least `1/p` of the unit at arbitrarily late steps. -/
theorem growth_not_recurring_of_replenished_loss (counted : w.Counted) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {T : Nat}
    (notGained : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (loses : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      ReplenishedLoses w.flow R p m cs t)
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t) :
    ¬ ∀ N, ∃ t x, N ≤ t ∧ w.web.Gains r R p t x :=
  match counted with
  | ⟨_, census⟩ => fun recurs => bounded_not_recurring
    (growth_bound_of_replenished_loss census embodied balances notGained loses enclosed base
      unit refining)
    fun N => match recurs (N + T) with
    | ⟨t, x, after, gains⟩ =>
      have later := Nat.le_trans (Nat.le_add_left T N) after
      have stands : 0 < w.web.level (t + 1) x := Nat.pos_of_ne_zero fun zero =>
        Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
          (units_pos base unit refining (Nat.le_succ_of_le later))
          (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_trans gains
            (Nat.le_of_eq ((congrArg (p * ·) zero).trans (Nat.mul_zero p))))))
      ⟨t, Nat.le_trans (Nat.le_add_right N T) after,
        total_pos_of_mem (q := fun c => mark (w.web.Gains r R p t c))
          (((World.standingCensus census embodied (t + 1)).2 x).mp stands) (mark_pos.mpr gains)⟩

/-- So arising at least `1/p` of the unit does not recur. -/
theorem arising_not_recurring_of_replenished_loss (counted : w.Counted) (embodied : w.Embodied)
    (balances : w.flow.BalancesAt r w.web) {T : Nat}
    (notGained : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      w.flow.replenishment cs t ≤ w.flow.uptake cs t)
    (loses : ∀ t, T ≤ t → ∀ cs, Distinct cs → w.flow.ClosedAt cs t →
      ReplenishedLoses w.flow R p m cs t)
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t) :
    ¬ ∀ N, ∃ t x, N ≤ t ∧ w.web.Arises t x ∧ R (t + 1) ≤ p * w.web.level (t + 1) x :=
  fun recurs => growth_not_recurring_of_replenished_loss counted embodied balances notGained
    loses enclosed base unit refining fun N => match recurs N with
    | ⟨t, x, after, arises, size⟩ => ⟨t, x, after, Nat.le_trans (Nat.le_of_eq
        ((congrArg (fun k => R (t + 1) + p * (r t * k))
          (eq_zero_of_not_pos fun pos => arises.1 ((embodied x t).mpr pos))).trans
          ((congrArg (fun k => R (t + 1) + p * k) (Nat.mul_zero (r t))).trans
            ((congrArg (R (t + 1) + ·) (Nat.mul_zero p)).trans (Nat.add_zero _))))) size⟩

end Growth

/-! ### Three sources of a least loss at each size of what is given -/

/-- The family's share gives it, with `m = p q`. -/
theorem share_replenishedLoses {L : Flow F C} {q : Nat} {cs : List C} {t : Nat}
    (dissipates : L.DissipatesBy q cs t) (R : Nat → Nat) (p : Nat) :
    ReplenishedLoses L R p (p * q) cs t :=
  fun given => calc R (t + 1) + p * q * L.replenishment cs t
      ≤ p * L.replenishment cs t + p * (q * L.replenishment cs t) :=
        Nat.add_le_add given (Nat.le_of_eq (mul_regroup p q _))
    _ = p * ((q + 1) * L.replenishment cs t) :=
        (Nat.left_distrib _ _ _).symm.trans (congrArg (p * ·) ((Nat.add_comm _ _).trans
          ((congrArg (q * L.replenishment cs t + ·) (Nat.one_mul _).symm).trans
            (add_mul_split q 1 _).symm)))
    _ ≤ p * (q * L.uptake cs t) := Nat.mul_le_mul_left p dissipates
    _ = p * q * L.uptake cs t := (mul_regroup p q _).symm

/-- Among at most `K` summands, one is at least a `K`th of the total. -/
theorem exists_large {α : Type} {g : α → Nat} {R p K : Nat} (pos : 0 < R) :
    ∀ (l : List α), l.length ≤ K → R ≤ p * total l g → ∃ a, a ∈ l ∧ R ≤ p * K * g a
  | [], _, big => absurd (Nat.le_trans big (Nat.le_of_eq (Nat.mul_zero p)))
      (Nat.not_le_of_gt pos)
  | a :: l, short, big =>
    match decideSome (p := fun b => R ≤ p * K * g b) (a :: l) with
    | isTrue found => found
    | isFalse absent =>
      have small : ∀ b, b ∈ a :: l → p * K * g b + 1 ≤ R :=
        fun b mem => Nat.lt_of_not_le fun large => absent ⟨b, mem, large⟩
      have total_eq : total (a :: l) (fun b => p * K * g b + 1) =
          p * K * total (a :: l) g + (l.length + 1) :=
        (total_add _ _ _).trans ((congrArg (· + total (a :: l) fun _ => 1)
          (total_mul (p * K) g (a :: l))).trans (congrArg (p * K * total (a :: l) g + ·)
            (total_ones (a :: l))))
      have sum : p * K * total (a :: l) g + (l.length + 1) ≤ p * K * total (a :: l) g + 0 :=
        Nat.le_trans (Nat.le_of_eq total_eq.symm)
          (Nat.le_trans (total_le (a :: l) small)
            (Nat.le_trans (Nat.le_of_eq (total_const R (a :: l)))
              (Nat.le_trans (Nat.mul_le_mul_right R short)
                (Nat.le_trans (Nat.mul_le_mul_left K big)
                  (Nat.le_of_eq (((mul_turn K p _).trans (mul_regroup p K _).symm).trans
                    (Nat.add_zero _).symm))))))
      absurd (left_cancel sum) (Nat.not_succ_le_zero _)

/-- A least loss at each size of transfer, with at most `K` transfers in the step, gives a
least loss at each size of what is given: a family given `1/p` of the unit has a transfer
taking at least `1/(p K)` of it. -/
theorem few_replenishedLoses {L : Flow F C} {R : Nat → Nat} {p K m : Nat} {cs : List C}
    {t : Nat} (dissipates : L.DissipatesOn cs t) (loses : L.LosesAtSize R (p * K) m cs t)
    (few : (L.present t).length ≤ K) (pos : 0 < R (t + 1)) : ReplenishedLoses L R p m cs t :=
  fun given =>
    match exists_large (g := fun f => total cs (L.give t f)) pos (L.present t) few
        (Nat.le_trans given (Nat.le_of_eq (congrArg (p * ·)
          (total_swap (fun f c => L.give t f c) cs (L.present t)).symm))) with
    | ⟨_, present, large⟩ =>
      have counted : 1 ≤ L.takersAbove R (p * K) cs t :=
        total_pos_of_mem (q := fun f => mark (R (t + 1) ≤ p * K * total cs (L.take t f)))
          present (mark_pos.mpr (Nat.le_trans large
            (Nat.mul_le_mul_left _ (dissipates.give_le present))))
      Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
        (Nat.le_trans (Nat.add_le_add_left (Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm)
            (Nat.mul_le_mul_right _ counted)) _)
          (loses.over dissipates))

/-- The spine's dissipation at a fixed unit gives it, with `m = 1`: a family given anything
has a formation that takes, and so loses a whole unit. -/
theorem fixed_replenishedLoses {L : Flow F C} {cs : List C} {t : Nat}
    (dissipates : L.DissipatesOn cs t) (p : Nat) : ReplenishedLoses L (fun _ => 1) p 1 cs t :=
  fun given =>
    have pos : 0 < total (L.present t) fun f => total cs (L.give t f) :=
      Nat.lt_of_lt_of_le (Nat.pos_of_ne_zero fun zero => Nat.not_succ_le_zero 0
          (Nat.le_trans given (Nat.le_of_eq ((congrArg (p * ·) zero).trans (Nat.mul_zero p)))))
        (Nat.le_of_eq (total_swap (fun f c => L.give t f c) cs (L.present t)).symm)
    match total_pos (L.present t) pos with
    | ⟨_, present, gives⟩ =>
      have loses : L.LosesAtSize (fun _ => 1) 1 1 cs t := fun g present' large =>
        Nat.le_trans (Nat.le_of_eq ((congrArg (1 + ·) (Nat.one_mul _)).trans (Nat.add_comm _ _)))
          (Nat.le_trans (Nat.add_le_add_left (sign_pos (Nat.lt_of_lt_of_le Nat.zero_lt_one
              (Nat.le_trans large (Nat.le_of_eq (Nat.one_mul _))))) _)
            (Nat.le_trans (dissipates g present') (Nat.le_of_eq (Nat.one_mul _).symm)))
      have counted : 1 ≤ L.takersAbove (fun _ => 1) 1 cs t :=
        total_pos_of_mem (q := fun f => mark (1 ≤ 1 * total cs (L.take t f))) present
          (mark_pos.mpr (Nat.le_trans (Nat.lt_of_lt_of_le gives (dissipates.give_le present))
            (Nat.le_of_eq (Nat.one_mul _).symm)))
      Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
        (Nat.le_trans (Nat.add_le_add_left (Nat.le_trans (Nat.le_of_eq (Nat.one_mul _).symm)
            (Nat.mul_le_mul_right _ counted)) _)
          (loses.over dissipates))

/-- The growth law with a least loss at each size of transfer and boundedly many transfers. -/
theorem growth_bound_of_least_loss_few {w : World} {alive : Nat → List w.Relatum}
    (census : w.web.Census alive) (embodied : w.Embodied) {r : Nat → Nat}
    (balances : w.flow.BalancesAt r w.web) (dissipative : w.flow.Dissipative)
    {R : Nat → Nat} {p K m : Nat}
    (loses : ∀ cs t, Distinct cs → w.flow.ClosedAt cs t → w.flow.LosesAtSize R (p * K) m cs t)
    {T : Nat} (few : ∀ t, T ≤ t → (w.flow.present t).length ≤ K)
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) (base : R T = 1)
    (unit : ∀ t, T ≤ t → R (t + 1) = r t * R t) (refining : ∀ t, T ≤ t → 0 < r t) (n : Nat) :
    total (steps T n) (fun t => w.web.gainers r R p t (alive (t + 1))) ≤
      p * w.web.stock (alive T) T * (m * w.web.stock (alive T) T) :=
  growth_bound_of_replenished_loss census embodied balances
    (fun t _ cs distinct closed => Nat.le_trans (Nat.le_add_right _ _)
      (dissipative cs t distinct closed).replenishment_takers)
    (fun t later cs distinct closed => few_replenishedLoses (dissipative cs t distinct closed)
      (loses cs t distinct closed) (few t later)
      (units_pos base unit refining (Nat.le_succ_of_le later)))
    enclosed base unit refining n

/-! ### `Trickle`: every premise but a bound on the transfers per step -/

theorem lt_halving : ∀ t, t < halving t
  | 0 => Nat.one_pos
  | t + 1 => Nat.lt_of_lt_of_le (Nat.succ_lt_succ (lt_halving t))
      (Nat.le_trans (Nat.add_le_add_left (halving_pos t) _)
        (Nat.le_of_eq (FamilyShare.two_mul (halving t)).symm))

/-- `Trickle` has more transfers at step `K` than `K`. -/
theorem Trickle.transfers_unbounded (K : Nat) : K < (Trickle.flow.present K).length :=
  Nat.lt_of_lt_of_le (lt_halving K) (Nat.le_of_eq (Trickle.carriers_length (halving K)).symm)

theorem Trickle.not_replenishedLoses (m : Nat) :
    ¬ ∀ t, 0 ≤ t → ∀ cs, Distinct cs → Trickle.flow.ClosedAt cs t →
      ReplenishedLoses Trickle.flow quarter 1 m cs t :=
  fun loses => arising_not_recurring_of_replenished_loss (w := Trickle.world) (r := fun _ => 4)
    Trickle.counted Trickle.embodied Trickle.balances
    (fun t _ cs distinct closed => Nat.le_trans (Nat.le_add_right _ _)
      (Trickle.dissipative cs t distinct closed).replenishment_takers)
    loses (fun t _ => Trickle.enclosed t) rfl (fun _ _ => rfl) (fun _ _ => Nat.succ_pos 3)
    Trickle.arising_whole

/-- The exact place of `Trickle`: it meets every premise of `growth_bound_of_least_loss_few`
but the bound on transfers per step, and a whole unit arises without end; it meets a least
loss at each size of what is given for no `m`. -/
theorem growth_needs_bounded_transfers :
    Trickle.world.Counted ∧ Trickle.world.Embodied ∧
      Trickle.flow.BalancesAt (fun _ => 4) Trickle.web ∧ Trickle.world.Dissipative ∧
      (∀ t, Trickle.world.flow.Enclosed t) ∧ Trickle.flow.LosesAtEverySize quarter ∧
      (∀ K, ∃ t, K < (Trickle.flow.present t).length) ∧
      (∀ N, ∃ t x, N ≤ t ∧ Trickle.web.Arises t x ∧
        quarter (t + 1) ≤ 1 * Trickle.web.level (t + 1) x) ∧
      ∀ m, ¬ ∀ t, 0 ≤ t → ∀ cs, Distinct cs → Trickle.flow.ClosedAt cs t →
        ReplenishedLoses Trickle.flow quarter 1 m cs t :=
  ⟨Trickle.counted, Trickle.embodied, Trickle.balances, Trickle.dissipative, Trickle.enclosed,
    Trickle.losesAtEverySize, fun K => ⟨K, Trickle.transfers_unbounded K⟩, Trickle.arising_whole,
    Trickle.not_replenishedLoses⟩

/-- A least loss at each size of what is given is strictly weaker than the family's share. At
the spine's fixed unit, `Tick` takes `t + 1` and gives back `t` at step `t`: it dissipates, so
it meets the least loss with `m = 1` at every `p` (`fixed_replenishedLoses`), and it meets no
share. -/
def Tick.flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun t _ _ => t + 1, fun t _ _ => t⟩

theorem Tick.dissipative : Tick.flow.Dissipative :=
  fun cs t distinct _ f _ => match cs, distinct, f with
  | [], _, _ => Nat.le_refl 0
  | [()], _, () => Nat.le_refl (t + 1)
  | () :: () :: _, ⟨fresh, _⟩, _ => absurd (List.Mem.head _) fresh

theorem Tick.not_share (q : Nat) : ¬ Tick.flow.DissipativeBy q :=
  fun share =>
    have le : (q + 1) * (q + 1 + 0 + 0) ≤ q * (q + 1 + 1 + 0 + 0) :=
      share [()] (q + 1) FamilyShare.distinct
        (fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside)
    Nat.not_succ_le_self q (left_cancel (a := q * (q + 1)) (calc
      q * (q + 1) + (q + 1) = (q + 1) * (q + 1 + 0 + 0) :=
          ((congrArg (q * (q + 1) + ·) (Nat.one_mul (q + 1)).symm).trans
            (add_mul_split q 1 (q + 1)).symm)
      _ ≤ q * (q + 1 + 1 + 0 + 0) := le
      _ = q * (q + 1) + q := (Nat.left_distrib q (q + 1) 1).trans
          (congrArg (q * (q + 1) + ·) (Nat.mul_one q))))

theorem replenishedLoses_strictly_weaker :
    Tick.flow.Dissipative ∧
      (∀ p cs t, Distinct cs → Tick.flow.ClosedAt cs t →
        ReplenishedLoses Tick.flow (fun _ => 1) p 1 cs t) ∧
      ∀ q, ¬ Tick.flow.DissipativeBy q :=
  ⟨Tick.dissipative, fun p cs t distinct closed =>
    fixed_replenishedLoses (Tick.dissipative cs t distinct closed) p, Tick.not_share⟩

/-! ## Q7. The exchange bound is attained

At a unit halving at each step, a pool of one unit of step 0 is drawn on twice: at each step
one unit of step 0 is taken and half of it given back. The flow is dissipative by the share
`1` per family, and the exchange law's bound `p (q + 1)` times the stock, here `2`, is
reached. -/

namespace Tight

def take : Nat → Nat
  | 0 => 2
  | 1 => 4
  | _ => 0

def give : Nat → Nat
  | 0 => 1
  | 1 => 2
  | _ => 0

def level : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ => 0

def flow : Flow Unit Unit :=
  ⟨fun _ => [()], fun t _ _ => take t, fun t _ _ => give t⟩

def web : Web Unit Unit :=
  ⟨fun t _ => level t, fun _ _ => True, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => True⟩

theorem balances : flow.BalancesAt (fun _ => 2) web
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem dissipativeBy : flow.DissipativeBy 1 :=
  fun cs t distinct _ => match cs, distinct, t with
  | [], _, _ => Nat.zero_le _
  | [()], _, 0 => Nat.le_refl 2
  | [()], _, 1 => Nat.le_refl 4
  | [()], _, _ + 2 => Nat.le_refl 0
  | () :: () :: _, ⟨fresh, _⟩, _ => absurd (List.Mem.head _) fresh

theorem closed (t : Nat) : flow.ClosedAt [()] t :=
  fun _ _ c outside => absurd (match c with | () => List.Mem.head []) outside

theorem bound (n : Nat) :
    total (steps 0 n) (flow.takersAbove halving 1 [()]) ≤ 1 * (1 + 1) * web.stock [()] 0 :=
  Flow.exchange_bound balances dissipativeBy FamilyShare.distinct (T := 0) (fun t _ => closed t)
    (R := halving) rfl (fun _ _ => rfl) (fun _ _ => Nat.succ_pos 1) 1 n

theorem attained : total (steps 0 2) (flow.takersAbove halving 1 [()]) =
    1 * (1 + 1) * web.stock [()] 0 :=
  rfl

end Tight

end Review15
```

## Appendix B. Axiom audit

**Probes.**

- `review/probes/Review15Audit.lean` (sha256 `0e0e63c40c848f0fe3cd8c69ac142f6f346fd9dff1632d087e13d3776822117d`) was run with `env LEAN_PATH=$PWD:../build_r2 lean +leanprover/lean4:v4.29.1 Review15Audit.lean`. Exit 0.
- The module `Review15` generates 108 constants: source declarations, auxiliary definitions, equation lemmas, match compilers and the like. None depends on any axiom.
- Each of the 72 non-internal declarations (16 definitions, 56 theorems) reports `[]`.

```lean
import Review15
import Lean
open Lean Elab Command

/-! Axiom audit of the fifteenth review's probes: every constant the module `Review15`
generates, then `#print`-style reports for each non-internal constant. -/

#eval show CommandElabM Unit from do
  let env ← getEnv
  let some idx := env.getModuleIdx? `Review15 | throwError "no module Review15"
  let mut count := 0
  let mut withAx := #[]
  let mut srcs : Array Name := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some idx then
      count := count + 1
      let axs ← liftCoreM <| Lean.collectAxioms n
      if axs.size > 0 then withAx := withAx.push (n, axs)
      if !n.isInternalDetail then srcs := srcs.push n
  logInfo m!"PROBE_CONSTANTS {count} WITH_AXIOMS {withAx.size} NONINTERNAL {srcs.size}"
  for (n, axs) in withAx do
    logInfo m!"AXIOMS {n} {axs.toList}"
  let sorted := srcs.qsort (fun a b => a.toString < b.toString)
  for n in sorted do
    let axs ← liftCoreM <| Lean.collectAxioms n
    logInfo m!"DECL {n} {axs.toList}"
```

Output (`review/logs/Review15Audit.out`):

```text
PROBE_CONSTANTS 108 WITH_AXIOMS 0 NONINTERNAL 72
DECL Review15.Alternation.not_balanced []
DECL Review15.Asymptote.eachShare []
DECL Review15.Asymptote.not_balanced []
DECL Review15.Dissipative.notGaining []
DECL Review15.EachShare []
DECL Review15.EachShare.dissipativeBy []
DECL Review15.Emission.eachShare []
DECL Review15.Emission.not_balanced []
DECL Review15.FamilyShare.closed []
DECL Review15.FamilyShare.dissipative []
DECL Review15.FamilyShare.dissipativeBy []
DECL Review15.FamilyShare.distinct []
DECL Review15.FamilyShare.flow []
DECL Review15.FamilyShare.given []
DECL Review15.FamilyShare.not_each []
DECL Review15.FamilyShare.taken []
DECL Review15.FamilyShare.two_mul []
DECL Review15.NotGaining []
DECL Review15.Pump.balances []
DECL Review15.Pump.balances_at []
DECL Review15.Pump.closed []
DECL Review15.Pump.flow []
DECL Review15.Pump.give []
DECL Review15.Pump.level []
DECL Review15.Pump.loses_recurs []
DECL Review15.Pump.odd_level []
DECL Review15.Pump.take []
DECL Review15.Pump.web []
DECL Review15.ReplenishedLoses []
DECL Review15.Tick.dissipative []
DECL Review15.Tick.flow []
DECL Review15.Tick.not_share []
DECL Review15.Tight.attained []
DECL Review15.Tight.balances []
DECL Review15.Tight.bound []
DECL Review15.Tight.closed []
DECL Review15.Tight.dissipativeBy []
DECL Review15.Tight.flow []
DECL Review15.Tight.give []
DECL Review15.Tight.level []
DECL Review15.Tight.take []
DECL Review15.Tight.web []
DECL Review15.Trickle.not_replenishedLoses []
DECL Review15.Trickle.transfers_unbounded []
DECL Review15.arising_needs_quantum_each []
DECL Review15.arising_not_recurring_of_replenished_loss []
DECL Review15.exchange_bound_of_least_loss_not_gaining []
DECL Review15.exists_large []
DECL Review15.family_share_strictly_weaker []
DECL Review15.few_replenishedLoses []
DECL Review15.fixed_replenishedLoses []
DECL Review15.gainers_size []
DECL Review15.growth_bound_of_least_loss_few []
DECL Review15.growth_bound_of_replenished_loss []
DECL Review15.growth_needs_bounded_transfers []
DECL Review15.growth_not_recurring_of_replenished_loss []
DECL Review15.keep_step []
DECL Review15.left_cancel []
DECL Review15.lose_step []
DECL Review15.losesAtSize_over []
DECL Review15.lossless []
DECL Review15.lossless_not_gaining_not_dissipative []
DECL Review15.lt_halving []
DECL Review15.not_gained_of_dissipative []
DECL Review15.over_standing []
DECL Review15.quantum_bound_of_not_gained []
DECL Review15.quantum_needs_not_gained []
DECL Review15.replenishedLoses_strictly_weaker []
DECL Review15.replenished_step []
DECL Review15.share_replenishedLoses []
DECL Review15.standing_nonrising []
DECL Review15.standing_within []
```

**Core (`Becoming.Resolution`).**

- `review/ResolutionAudit.lean` walks every constant of `Becoming.Resolution` with `Lean.collectAxioms`, then every constant of the loaded closure. It then prints each non-internal Resolution declaration with its axioms.
- At R2 it imports `Becoming`. At R1 and R1b it imports `Becoming.Resolution` (`review/build_<commit>/Audit.lean`), with that commit's `Resolution.olean` and the R2 closure's other modules, unchanged across the three commits.

```text
R1  658db670  RESOLUTION_CONSTANTS 204 WITH_AXIOMS 0   RESOLUTION_NONINTERNAL 128 (all [])   CLOSURE_CONSTANTS 4199 WITH_AXIOMS 24
R1b e79e00e5  RESOLUTION_CONSTANTS 229 WITH_AXIOMS 0   RESOLUTION_NONINTERNAL 149 (all [])   CLOSURE_CONSTANTS 4224 WITH_AXIOMS 24
R2  de17f533  RESOLUTION_CONSTANTS 313 WITH_AXIOMS 0   RESOLUTION_NONINTERNAL 204 (all [])   CLOSURE_CONSTANTS 7142 WITH_AXIOMS 38
```

Notes on these figures:

- The non-internal declarations include every declaration the receipts list (126, 145, 200). The extras are generated instances:
  - R1: `instDecidableGains`, `instDecidableLosesQuantum`;
  - R1b and R2 add `instDecidableLoses` and `Dwindle.instDecidableActiveUnitWebUnit`.
- At R2 the 38 axiom-dependent closure constants are generated `injEq` lemmas, each on `propext` only. Their set equals the receipt's `generated_axiom_dependencies`.
- At R1 and R1b the 24 are the subset in Resolution's own import closure.
- Full outputs: `review/logs/ResolutionAudit.R2.out`, `ResolutionAudit.658db670.out`, `ResolutionAudit.e79e00e5.out`.
