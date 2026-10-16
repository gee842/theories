<a id="第十八次独立审查p107p127-与-i4b--eighteenth-independent-review-p107p127-and-i4b"></a>
# 第十八次独立审查：P107–P127 与 I4b

> **中文版（2026-10-17）。** 正典文本是[英文版](BECOMING-EIGHTEENTH-REVIEW.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-16，Asia/Bangkok。**AI 独立审查（第十八次；另一 agent，未参与撰写）。** 这是工作板项 R18（[工作板](../../../BECOMING-WORKBOARD.md)）。依据是 Ren 2026-10-16 的“do a full review … fix all”，以及[发布准备度审查](BECOMING-RELEASE-READINESS-REVIEW.md) §5。本文不是 Ren 的话。

审查对象
- 第十七次审查（2026-10-14，[BECOMING-GENERAL-LAWS-REVIEW](BECOMING-GENERAL-LAWS-REVIEW.md)）之后落地的全部内容，状态为 `ce808d6a`（主线，P127 落地 `1a78f978` 之后加两次工作板提交）。
- 研究
- 模块 / Modules，各在落地顺序中：
  - P107 `Novelty`、`Reading`、`Readings`；
  - P110 交托的读法 D1–D39（`DELEGATED-CHOICES.md`）；
  - P111 `Gain`；P112 `Gluing`；P113 `Sensitivity`；
  - P114 `Courses`、`CoursesBridge`；P115 `Propagation`；
  - P116 与 P119 `Parting`、`Typicality`；P117 `Situations`；
  - P118 `Loops`；P120 `Remainder`；P121 `Routes`；P122 `Closing`；
  - P123 `Frequency`；P124 `Thresholds`；P125 `Observation`；P126 `Tail`；P127 `Onward`；
  - I4b-1 `Gated`；I4b-2 `Selection`；I4b-3 `Horizon`；I4b-4 `Lasting`。
- 它们的记录，以及它们触及的 GENERATIVITY-CHAIN 条目。

本审查在自己的 git 工作树（分支 `r18-review`）中进行。按任务的限制：
- 没有运行 `check_becoming.py`，也没有 `lake` 构建；
- 没有改动记录、理论章、OPENING、README、GOALS 或任何生成文件；
- 没有编辑工作板。

只读 Lean，并用小的 Python 脚本抽取声明与文档。下文中“审查者的论证”一类的数学都没有经过 Lean 检查，标为待证。

严重度
- **error**：所写的话是假的；
- **overstatement**：所写的比所证的强；
- **understatement**：所写的比所证的弱，或者漏了一个已知的确切等价；
- **presentation**：真，但会误导，或把定义的展开当作规律；
- **credit**：标准结果没有指名来源；
- **confirmed**：核对过，所写与所证相符。

“薄”（thin）的意思是：真，而且如实陈述，但内容近于定义或已知的小事实。它不是错。

---

## 摘要

**形式状态。**
- 没有发现假的 Lean 定理。每个核对过的“恰当”（iff）都是真正的当且仅当。
- 构造性的标定都正确：
  - `Sensitivity` 与 `Tail` 中的 WLPO 与 LPO（规则形式与命题形式分开）；
  - `Frequency` 中的 `RecursOrStops`；
  - `Onward` 中的依赖选择；
  - `Gated` 中的双重否定消去；
  - `Horizon` 中的 Markov 原则。
- 有 ¬¬ 结论的定理在 Lean 中都写着 ¬¬。问题出在文字：有两处记录把 ¬¬ 丢了。

**主要问题在文字，不在定理。** 分四类：

1. **三处错误。**
   - `what-a-finite-history-refutes` 的陈述说“其外有附着运行的读法既不可否证也不可证实”。Lean 只给“不可否证”。终于发生是反例：它在所有序列的过程中可证实。
   - `Horizon` 的模块文档也说复现与终于发生“are neither”。
   - `every-origin-passes-the-gate` 的不显示项 1，中文把英文反过来了。
2. **构造性的过度陈述。** `Sensitivity` 说条件无穷多时“这一条件不能去掉”，D37 说这一读法“不适用”。但反例 `tailLaw` 要一个消失的判定，那给出 LPO；而任何反例都给出 WLPO。所以在核心里，这一条件既没有被驳倒，也没有被证明可以去掉。
3. **上界的见证不守恒。** `Propagation` 的上确界由 `ExchangeLaw.carrying` 达到。这个律什么都不取，却给出量，所以违反第一律（`Flow.Gainless`）。“所持的差别不断到达”与“每个回路至少使之加倍”都建立在这个律上，又依赖强度是不小于一的自然数。记录与 Ren 已取的读法没有说出这两点。
4. **把必要条件说成同一。** `Observation` 的标题“所识即在下游”，`Thresholds` 的陈述“断裂之前没有经过储量的回路”，以及 `Situations` 中“情境使之为真”的形式部分，都比所证的强，或者在构造上就为真。

**计数。**

| 严重度 | 数目 | 编号 |
|---|---|---|
| error | 3 | E1–E3 |
| overstatement | 11 | O1–O11 |
| understatement | 3 | U1–U3 |
| presentation | 9 | P1–P9 |
| credit | 12 | K1–K12 |
| confirmed | 14 | C1–C14 |

修正清单在文末，按 (L) Lean 文档或出处、(R) 记录字段、(S) 需要新的或改动的定理、(P) Ren 的决定 分类。

<a id="english-summary"></a>

<a id="0-范围与方法--scope-and-method"></a>
## 0. 范围与方法

<a id="1-发现表--findings-table"></a>
## 1. 发现表

<a id="errors"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| E1 | rec what-a-finite-history-refutes, statement en and zh | 陈述说“其外有附着运行的读法既不可否证也不可证实”。Lean 只给“不可否证”。不可证实需要读法之内有一个附着于补集的运行。终于发生是反例：全假的序列从外面附着于它，而它可证实（开集）。 | error | `not_refutable_of_adheres` concludes `¬ Refutable L` from an adhering run outside `L`; `not_verifiable_of_adheres` needs `Adheres (¬ L ·) r` with `L r`. Law 2 of the same record states both halves correctly. | en: "a reading with an adhering run outside it is not refutable, and one with a run inside adhering to its complement is not verifiable"; zh likewise: "其外有附着运行的读法不可否证，其内有附着于补集的运行的读法不可证实". |
| E2 | `Horizon` module doc, *core* `Horizon.lean` l. 48–51 | “复现与终于发生 are neither”接在“不可否证……对偶地不可证实”之后，读作两者都不可否证也不可证实。所引的两个定理都是 `_not_refutable`。终于发生可证实。 | error | `Sequences.recurs_not_refutable` and `Sequences.eventually_not_refutable`. The record's law 2 correctly adds that never-occurring is not verifiable (`never_not_verifiable`). | "recurrence and eventual occurrence are not refutable (…), and never occurring is not verifiable (`Sequences.never_not_verifiable`)". |
| E3 | rec every-origin-passes-the-gate, does_not_show 1, zh | 英文列的是不显示者：不判定 p 时，第一个使 p 成立的门控步。中文写成“不判定 p 时，起源之律给出第一个使 p 成立的门控步（之前 p 不成立）”，成了肯定的断言，与英文相反。 | error | Compare the en: "Without deciding p, the first gated step at which p comes to hold (failing before it): the law gives a gated step after which p holds." `origin` gives some gated step, not the first. | zh: "不判定 p 时，第一个使 p 成立的门控步（之前 p 不成立）：律只给出一个之后 p 成立的门控步。" |

<a id="overstatements"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| O1 | `Sensitivity` module doc (*core* `Sensitivity.lean` l. 45); rec sensitivity-is-the-least-registration, statement zh and counterexample 0; D37 (1) | 文档说“条件无穷多时这一条件不能去掉”；记录的反例 0 说没有连续性就没有最小的识；D37 说条件无穷多时这一读法“不适用”。但反例 `tailLaw` 以消失的判定 `decides` 为参数，而 `lpo_of_vanish_decided` 表明这个判定给出 LPO。反过来，`wlpo_of_not_through_sensitive` 表明任何反例都给出 WLPO。所以在核心里，条件既没有被驳倒，也没有被证明可以去掉：它独立于核心，在 WLPO 与 LPO 之间。 | overstatement | `tailLaw (decides : ∀ α, Decidable (VanishFrom α))`, l. 301; `tailLaw_no_least_registration` l. 357; `lpo_of_vanish_decided` l. 553; `wlpo_of_not_through_sensitive` l. 528. `Tail` (P126) states this calibration exactly; `Sensitivity` and D37 predate it and were not revised. | Doc: "With infinitely many conditions the condition cannot be dropped given a decision of vanishing (which gives LPO), and any law that drops it gives WLPO." Record: same in statement zh and counterexample 0. D37 (1): "with infinitely many conditions the reading is not shown to apply: given a decision of vanishing, the tail law has no least registration." |
| O2 | rec sensitivity-is-the-least-registration, statement en/zh and law 1 | `least_registration` 的结论是 `¬ ¬ W.Registers obs h c`。陈述与定律 1 说“最小的识”，没有双重否定。 | overstatement | `ExchangeLaw.ReadsFinitely.least_registration`, l. 181. | Add "up to double negation" (zh "于双重否定下"), or state it for stable `Registers`. |
| O3 | `Propagation`; rec how-much-difference-arrives (does_not_show 2, counterexample 1, readings); D39 (3) | `most_difference_arrives` 对一切律成立，上确界由 `ExchangeLaw.carrying` 达到。这个律取用为零（`fun _ _ _ _ => 0`），给出强度乘所有过去水平之和，所以只要给出任何量就违反 `Flow.Gainless`。“输入有界推不出到达有界……水平持有所给”与读法“所持的差别不断到达”（D39 (3) 已采用）都建立在一个创造量的律上。上界对无增益的律是否紧没有说明，记录也从未提到无增益。 | overstatement | *core* `Propagation.lean` l. 641–648: "nothing is taken". `Flow.Gainless`: `total cs (L.give t f) ≤ total cs (L.take t f)` for closed families. | Record: say that the attaining law is not gainless, and that the bound is shown attained over all laws, not over gainless ones. D39 (3): add the same scope. Optional (S): state the gainless case, either tightness or a sharper bound that uses the stock. |
| O4 | `Loops`, `Frequency`; rec how-a-carried-difference-grows, how-often-couplings-act (statements, readings); Ren's taken P118 reading | “每次返回至少使之加倍”“不论强度”成立，只因为强度是自然数，正的强度至少是一，而且携带律不耗散（又见 O3）。强度小于一时（实数的量），Neumann 级数在谱半径小于一时收敛，频繁的返回不一定失控。`Frequency` 的不显示项 3 承认这一点，但陈述与读法写的是一般情形。Ren 2026-10-16 取了“只有回路使差别失控……经过每个回路”。其中充分的一半（每个每步耦合的回路都失控）是 ℕ 的产物，Ren 应当知道这一点。 | overstatement | `carried_doubles_return`, `SelfLoop.carried_eq` (D·(1 + M)^a); *rec* how-often-couplings-act does_not_show 3 ("a positive strength may be below one"). | Statements: add "with natural-number strengths, each positive one at least one" (zh "强度为自然数，正的强度至少为一"). Readings: say that the sufficiency half is the natural-number case. (P): ask Ren whether the taken reading stands with this scope. |
| O5 | `Observation` headline (*core* `Observation.lean` l. 12, 30, 274, 353); rec observation-is-a-route (title, statement, readings) | 标题“所识即在下游”（“Registering is being downstream”“observing is being downstream”“Observation is a route”）说的是同一。`apart_only_downstream` 只证必要：不在下游者两边相同。反方向（下游者两边不同）不成立，记录的不显示项 0 也承认。读法“观察不是依存之外的第二种关系”超出定理：定理说观察不越过依存，没有说观察就是依存。 | overstatement | `apart_only_downstream` l. 285: `∀ t e, ¬ Upstream … c e → …alike`. | Headline: "Registering lies within the downstream" (zh "所识不出下游"). Statement: "a formation can register a difference only where it is downstream". (P): the reading. |
| O6 | rec loops-within-what-a-law-reads, statement en/zh | 陈述说“断裂之前没有经过储量的回路：经过储量的回路在断裂处形成”。但律自己的强度从一开始就把储量耦合到自身，反例 0 也这样说。没有回路的是立律（`standing`），断裂之前律的动作与立律相同（`follows_standing_before`）。所以形成的是动力学上起作用的回路，不是强度上的回路。 | overstatement | `ReadsBelow.standing_no_loop`, `Flow.follows_standing_before`, `Draw.onLoop` (every strengths of the draw put the stock on a loop). | "Before the break the law acts as its standing law, which has no loop through the stock; the loop that acts forms at the break." Same in zh. |
| O7 | `Horizon` docstring of `Refutable.adheres_least` (l. 316) | “最小的可否证读法”：定理只说包含 K 的每个可否证读法在附着于 K 的运行上于双重否定下成立。它没有证明 `Adheres K` 本身可否证，所以“最小”不成立。 | overstatement | Statement at l. 317–320. | Docstring: "Refutable supersets hold where the subset is adhered to." Optional (S): prove `Refutable (Adheres K)` (closure is closed), which would earn "least". |
| O8 | `Gated` module doc, *core* `Gated.lean` l. 24 | “律恰在每个门已判定处成立（`origin_of_decides`）”。`origin_of_decides` 只证充分。 | overstatement | `origin_of_decides (decides : ∀ a, gate a ∨ ¬ gate a)` l. 181. | "the law holds where each gate is decided". |
| O9 | rec every-origin-passes-the-gate, statement en/zh | “门是命题时这一律恰是双重否定消去”漏了“对每个过程都要求时”。对一个过程，这一律不是双重否定消去。 | overstatement | `origin_of_propositions_iff`; does_not_show 2 of the same record states it correctly. | Add "asked of every process" (zh "对每个过程都要求时"). |
| O10 | rec what-a-law-of-the-whole-and-no-part-takes (readings); `Tail` | 读法“同一整体……只取弱的规则”把 `neverIndicator` 与 `vanishIndicator` 当作同一个整体。两者只在经典意义下相同。在核心里，它们是两个不同的律。 | overstatement | `Tail` docstrings; the two indicators read different properties (never 1 vs vanishing from some point). | Reading: "a whole of the same kind" or "a related whole". (P) if Ren has taken it. |
| O11 | rec orders-as-a-sum-over-histories, statement en/zh; rec how-loops-form statement | “有限视界精确恰在上游没有回路处”漏了它的条件：条件全部列出，形成与强度每步相同（stationary）。`how-loops-form` 的“形成之前增长至多是多项式”也漏了“条件全部列出”。两处的条件在定律中都有，只是陈述里没有。 | overstatement (minor) | Laws 5 and hypotheses of both records. | Add "with every condition listed and the law stationary" (zh "条件全部列出、律每步相同时"). |

<a id="understatements"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| U1 | `Lasting.EitherThroughout` (*core* `Likeness.lean` l. 1251); rec lifting-where-branching-is-finite | `EitherThroughout` 是：对两个判定的、向下封闭的序列 α、β，若每处 α 或 β，则 α 处处或 β 处处。审查者的论证（未经 Lean 检查）：它等价于 LLPO。<br>正方向：给一个至多有一个 1 的序列 s，令 α k 为“k 以内偶位都为 0”，β k 为“k 以内奇位都为 0”。两者判定、向下封闭，每处其一成立。<br>反方向：令偶位 2k 标 α 第一次不成立之处，奇位 2k + 1 标 β 第一次不成立之处。向下封闭与“每处其一”保证至多一个 1，LLPO 即给出结论。<br>所以“课程每个长度与一个课程继续之间恰是 EitherThroughout”可以读作“恰是 LLPO”，与弱 König 引理的标定相合。<br>`EitherThroughout` says: for decided, downward-closed α and β with α or β at every step, α holds throughout or β does. Reviewer's argument, not Lean-checked: it is equivalent to LLPO.<br>Forward: given s with at most one 1, let α k be "no 1 at even positions ≤ k" and β k "no 1 at odd positions ≤ k". Both are decided and downward closed, and one holds at each k.<br>Converse: mark at position 2k the first failure of α and at 2k + 1 the first failure of β. Downward closure and "one at each step" give at most one 1, and LLPO gives the conclusion.<br>So "between courses of every length and one course going on lies exactly `EitherThroughout`" can read "exactly LLPO", in line with the weak König lemma calibration. | understatement | Definition l. 1251. Weak König ⇔ LLPO: Ishihara 1990; Bridges–Richman 1987. | (S): prove `EitherThroughout ↔ LLPO` in the core, with LLPO stated for Boolean sequences with at most one `true`. Then (R): name it in the record. |
| U2 | rec what-a-law-of-the-whole-and-no-part-takes, does_not_show 1 | “WLPO 是否推出 LPO”留为开放。作为命题，这一点已知不可证：WLPO 严格弱于 LPO（Akama–Berardi–Hayashi–Kohlenbach 2004）。核心不能证明它，这是已知的，不是开放问题。 | understatement | Record text. | Cite the result, scoped to Props over intuitionistic arithmetic; keep the rule form open if it is meant. |
| U3 | rec how-often-couplings-act (law 6, does_not_show 0) | `RecursOrStops` 是 Σ⁰₂ 层级的排中（Σ⁰₂-LEM），严格强于 LPO（= Σ⁰₁-LEM）。记录说它“给出”LPO，这是真的，却低估了它：每个时程都安定恰是 Σ⁰₂-LEM。记录的对应字段说“Σ⁰₂ 形式的排中”，陈述与不显示项没有说。 | understatement | `RecursOrStops : ∀ R : Nat → Nat → Bool, (∀ n, ∃ m, R n m = true) ∨ ∃ n, ∀ m, R n m = false`. | Statement and does_not_show 0: "exactly Σ⁰₂ excluded middle, which gives LPO" (zh "恰是 Σ⁰₂ 排中，给出有限全知原则"). |

<a id="presentation-true-but-misleading-or-thin-as-stated"></a>

| id | module / record | finding（中文 / English） | severity | evidence | proposed correction |
|---|---|---|---|---|---|
| P1 | `Reading`; rec premises-read-off-the-exchange | `readOff` 把要求定义为“低于所需即回应”，所以“活动需要支持”经 `supported_of_responds` 一行得出。`reading_glue`“不加前提”是定义的展开。记录承认平衡是构造的（不显示项 3），没有承认活动需要支持也是构造的。 | presentation | `readOff := ⟨level, L.Exchanging, requires, need, fun t f c => 0 < L.take t f c⟩`; `supported_of_responds := Nat.ge_of_not_lt fun below => responds l (fun _ _ _ => rfl) below exchanges`. | Add to does_not_show: "under `readWeb`, activity needs support by the definition of the requirement". |
| P2 | `Readings`; rec unity-of-readings | `Contextual.world_active` 是 `Iff.rfl`。`World.unity` 的第一合取项对每个 `World` 都成立：计入其余时，每个水平序列都是 `exchange` 的运行，所以它不排除任何东西。陈述“计入其余，每个世界都是一次交换的运行”没有说这一点。 | presentation (thin) | `w.withRest.exchangeRun World.withRest_balanced`. | Statement: add "which every sequence of levels is, the rest counted". |
| P3 | `Gain`; rec where-novelty-gain-comes-from, law 0 | “每次上升都是被给的”（`rise_netGiver`）是记账的恒等式：其余在 `withImbalance` 中被定义为剩余。定律 0 没有标明它是构造的。 | presentation | Definition of `withImbalance`. | Law 0: "by the definition of the rest as the residual". |
| P4 | `Situations`; rec weights-count-situations; the reading Ren took | `finerLaw := ⟨fun s x t => t = x.2.1 ∧ …⟩`：动作中的情境写着目标配置，所以 `finerLaw_determined`（`first.1.trans second.1.symm`）是构造的。读法“分支的律是忘了情境的确定的律”或“情境使之为真”，在形式上是一个小事实：把结果放进动作，结果就被确定。实质在 `sum_finer`，即计数。 | presentation (thin) | *core* `Situations.lean` l. 101–102. | Record: say that determination holds by construction and that the content is the count (`sum_finer`). (P): Ren should know this when the reading is cited. |
| P5 | `Parting`; rec identification-where-runs-part | `world_right_iff` 与 `some_right_iff` 把整个世界（P、moves、all、reg、s）给学习者。反方向是近于同语反复的不可区分论证，记录如实说它已知。 | presentation (thin) | Statements. | None needed beyond credit (K9). |
| P6 | `Closing`; rec how-loops-form | `onLoop_iff_formed` 近于定义：耦合被定义为“在某步作用”。`onLoop_succ_iff` 是图论的事实：加一条边，闭合一个环。 | presentation (thin) | Statements. | None. |
| P7 | rec typicality-by-counting | “0.88^n”与“pq/((p+q)²ε²n)”是文中的算术，不是 Lean 陈述。 | presentation (minor) | Record text against `Typicality` statements. | Mark them as arithmetic from the stated bounds, or bind them to theorems. |
| P8 | GENERATIVITY-CHAIN (`theories/becoming/results/data/generativity-chain.json`, `GENERATIVITY-CHAIN-INDEX-RECORD.md`) | 2026-10-14 全链复核（`e667f358`）之后，33 次落地刷新了 `reviewed_sources` 中 78 个指纹，提交说明写“chain review recorded”。索引记录在那之后没有条目。链的条目内容没有变（除新增一个评审来源），没有一个条目提到本审查范围内的模块。也许每个变动来源都读过、条目确实不受影响，但这没有记录。AGENTS.md 要求刷新哈希前先读并核对。链的学习与智慧部分是否应接入 `Parting`、`Observation`、`Selection`（“记忆不是智慧”），由 Ren 定。 | presentation (process) | `git diff e667f3587 HEAD -- theories/becoming/results/data/generativity-chain.json`: only hash lines and one review path change. `git log` of the index record: last commit `e667f358`. | (R): add one index-record entry listing the refreshed sources and what was checked; if they were not read, restore "pending" for them. (P): whether these modules enter the chain. |
| P9 | rec where-a-run-goes-on, law 0 zh | 中文“从运行的每个配置开始每个长度的路径”缺动词（“有”）。“运行的每个配置可从其起点得到”与英文“each is had from its start”所指不同：英文指每条路径，中文指每个配置。 | presentation (zh/en) | Record text. | zh: "从运行的每个配置开始，有每个长度的路径，每条都从其起点得到；……". |

<a id="credit"></a>

<a id="confirmed"></a>

<a id="readings-and-the-delegation-p110"></a>

<a id="2-各模块结论--verdict-per-module"></a>
## 2. 各模块结论

<a id="3-一元关系方法--the-nondual-method"></a>
## 3. 一元关系方法

<a id="4-未能检查--what-could-not-be-checked"></a>
## 4. 未能检查

---

<a id="fix-list--修正清单"></a>
## 修正清单

20. E3, *rec* every-origin-passes-the-gate, does_not_show 1 zh. Use: "不判定 p 时，第一个使 p 成立的门控步（之前 p 不成立）：律只给出一个之后 p 成立的门控步。"
38. P9, *rec* where-a-run-goes-on, law 0 zh. Use "从运行的每个配置开始，有每个长度的路径，每条都从其起点得到；……".
