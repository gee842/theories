# 定理层面的连通 / How the spine's theorems connect

2026-10-15，Asia/Bangkok。AI（Claude Opus 5.5）在一次 Claude Code 会话中应 Ren 的问题所作的测量。Ren 的原话：

> so for our theories, they are proved in a dag order and can be all connected right?

本文是测量，不是检查，也不登记成果；它不改动任何记录或生成页面。下面的分类与解读是 AI 的，待 Ren 审阅。

2026-10-15, Asia/Bangkok. A measurement made by the AI (Claude Opus 5.5) in a Claude Code session, in answer to Ren's question quoted above. It is a measurement, not a check, and registers no result; no record or generated page is changed. The classes and readings below are the AI's, pending Ren.

[Script](THEOREM-CONNECTIVITY.py) · [Lean dump](THEOREM-CONNECTIVITY-DUMP.lean) · [result, with every spine theorem's class](THEOREM-CONNECTIVITY.json) · module-level companion: [SPINE-INTEGRATION.py](SPINE-INTEGRATION.py)

## 1. 有向无环 / Directed and acyclic

**中文。** 证明按有向无环图的次序排列，这一点由 Lean 保证：导入不能成环，一个声明只能使用在它之前的声明。113 个脊柱模块的导入图无环，最长导入链 25 层。成果记录的 508 条依赖也无环，由 `research-check` 强制。

**English.** The proofs are in DAG order, and Lean guarantees it: imports cannot form a cycle and a declaration can use only what precedes it. The import graph of the 113 spine modules is acyclic, with a longest chain of 25 modules. The 508 dependency links between result records are acyclic too, as `research-check` enforces.

## 2. 方法 / Method

**中文。** 从检查器的共享缓存按 `check_becoming.py` 自己算出的键还原脊柱运行的全部编译模块（基础、核心、桥及桥所导入的继承模块，共 191 个），不重新编译。Lean 列出其中每个常量（26,505 个）的类型与值所用到的被跟踪常量。“基础”是两族定义：
- 过程族：`Generative.Process`、`Generative.Trace`（GenerativeCore），以及 `Becoming.Frame`、`Becoming.Run`；
- 世界族：`Becoming.World`，以及构成它的 `Becoming.Flow`、`Becoming.Web`。

每条脊柱定理归入第一个适用的类：陈述用到两族、只用到过程族或只用到世界族；陈述不用、证明经过某一族；被某个到达基础的常量（直接或间接）使用；都不是则为“独立”，即陈述只用本模块自己的定义，或不用任何被跟踪的常量。

**English.** The compiled modules of the spine run (foundation, core, bridge and the inherited modules the bridge imports; 191 in all) are restored from the checker's shared cache under the keys `check_becoming.py` itself computes, with no recompilation. Lean lists, for each of their 26,505 constants, the tracked constants its type and its value use. The base is two families of definitions:
- the Process family: `Generative.Process` and `Generative.Trace` (GenerativeCore), with `Becoming.Frame` and `Becoming.Run`;
- the World family: `Becoming.World`, with the `Becoming.Flow` and `Becoming.Web` it is built from.

Each spine theorem goes into the first class that fits. Its statement uses both families, only the Process family or only the World family. Otherwise, its proof goes through a family although its statement does not. Otherwise, some constant that reaches the base uses it, directly or indirectly. Failing all of these it stands apart: its statement uses only its module's own definitions, or no tracked constant at all.

## 3. 结果 / Results

Commit 108e278e, core receipt 20261015T163210.426211Z; the Lean sources match the commit.

| 类 / Class | 定理 / Theorems |
|---|---|
| 陈述用到两族 / Statement on both families | 124 |
| 陈述用到过程族 / Statement on Process/Frame/Run/Trace | 1,110 |
| 陈述用到世界族 / Statement on World/Flow/Web | 2,607 |
| 证明经过某一族 / Proof through a family | 19 |
| 被基础上的定理使用 / Used by a theorem on the base | 1,283 |
| 独立：自身词汇 / Apart: own vocabulary | 862 |
| 独立：只用前导库 / Apart: prelude-only statement | 84 |
| **共计 / Total** | **6,089** |

**中文。**
- **两个根，而非一个。** `Flow`、`Web`、`World` 都不到达过程族，`Process` 也不到达世界族。两族只在 124 条陈述中相遇，主要在 Correspondence（18）、Relevance（16）、Descent（15）、Ranking（13）、Dependence（10）、Joint 与 Regrouping（各 8）、Unfolding 与 Testing（各 6）。Unfolding 以对应定理表明过程与框架是同一展开的读法，但两族都不由对方定义。
- **独立的 946 条**中 406 条不被任何常量使用。整模块独立的有 Quantum 37/37、CrossSituational 37/37、Learnable、Segmentation、Retrodiction（各 17/17；Retrodiction 导入 Frame 却不用它）。过半独立的有 Identification 67/105、Learning 63/75、Lasting 63/69、Copying 58/71、ReferencePlan 46/58、Decidedness 38/65、Attraction 35/47、Weighted 30/44 等。
- **无向连通。** 6,089 条中 6,055 条在同一连通分量里；另外 34 条（Retrodiction 全部 17 条、Readout 9 条、Seeking 3 条、Learning 2 条及 3 条单独的定理）与其余不共享任何定义。
- **记录。** 179 条记录以别名指向脊柱定理。按其最好的一条，16 条陈述用到两族，62 条用到过程族，67 条用到世界族，5 条证明经过某一族，3 条被基础使用，26 条只落在独立定理上。这 26 条按模块：Copying 4、Bridge 4、Readout 3、Lasting 3（`market-*`）、CrossSituational 3，Weighted、Countdown、Segmentation 各 2，Retrodiction、Feedback、Description 各 1。完整清单见 [JSON](THEOREM-CONNECTIVITY.json) 的 `records_resting_only_on_apart_theorems`。
- **与早先一次的比较。** 在 69336fa3（6,019 条定理）上独立 890 条、只落在独立定理上的记录 21 条。I3d、I3e 之后新增的 5 条（binding-preserving-substitution、growth-constrained-fragmentation、material-preparation-output、organizational-formation-from-generative-comparison、risk-certificate-outcome-distinction）已陈述在脊柱上，其定理却陈述在各自的词汇上。可见“陈述在脊柱上”（SPINE-INTEGRATION.py 的计数）不等于“落在基础上”。

**English.**
- **Two roots, not one.** `Flow`, `Web` and `World` never reach the Process family, and `Process` never reaches the World family. The families meet only in the 124 statements on both, chiefly in:
  - Correspondence (18), Relevance (16), Descent (15), Ranking (13) and Dependence (10);
  - Joint and Regrouping (8 each), Unfolding and Testing (6 each).

  Unfolding shows by correspondence theorems that process and frame are readings of one unfolding, but neither family is defined from the other.
- **Of the 946 apart**, 406 are used by no constant at all.
  - Wholly apart modules: Quantum 37/37, CrossSituational 37/37, and Learnable, Segmentation and Retrodiction (17/17 each; Retrodiction imports Frame but does not use it).
  - More than half apart: Identification 67/105, Learning 63/75, Lasting 63/69, Copying 58/71, ReferencePlan 46/58, Decidedness 38/65, Attraction 35/47, Weighted 30/44 and others.
- **Undirected connectivity.** 6,055 of the 6,089 theorems lie in one connected component. The other 34 share no definition with the rest: all 17 of Retrodiction's, 9 in Readout, 3 in Seeking, 2 in Learning and 3 single theorems.
- **Records.** 179 records name spine theorems in their aliases. By the best class among those theorems:
  - 16 have statements on both families, 62 on the Process family and 67 on the World family;
  - 5 have a proof through a family, and 3 are only used by the base;
  - 26 rest only on apart theorems. By module: Copying 4, Bridge 4, Readout 3, Lasting 3 (`market-*`), CrossSituational 3, Weighted, Countdown and Segmentation 2 each, and Retrodiction, Feedback and Description 1 each.

  The full list of the 26 is in `records_resting_only_on_apart_theorems` in the [JSON](THEOREM-CONNECTIVITY.json).
- **Against an earlier run.** On 69336fa3 (6,019 theorems), 890 theorems stood apart and 21 records rested only on apart theorems. Five records joined by I3d and I3e have since been stated on the spine, but their theorems are stated in their own vocabulary:
  - binding-preserving-substitution;
  - growth-constrained-fragmentation;
  - material-preparation-output;
  - organizational-formation-from-generative-comparison;
  - risk-certificate-outcome-distinction.

  Being stated on the spine (what SPINE-INTEGRATION.py counts) is therefore not the same as resting on the base.

## 4. 界限 / What this does not show

**中文。**
- “独立”指在 Lean 中不依赖基础，不是说定理错误或空洞。对任意类型陈述的规律，一旦实例化就覆盖运行与世界；所缺的是作出这一实例化的定理。
- 数字取决于把哪些定义算作基础：只算 `World` 而不算 `Flow`、`Web` 时，约 2,600 条关于这两者的定理会显得不连通。
- 无向连通是很弱的联系：两条定理只要共用任一辅助引理，就算相连。
- 测量读的是编译环境中的依赖，不判断任何陈述的含义。

**English.**
- "Apart" means no Lean dependency on the base, not that a theorem is wrong or empty. A law stated for every type covers runs and worlds once it is instantiated. What is missing is the theorem that instantiates it.
- The numbers depend on which definitions count as the base. Counting `World` without `Flow` and `Web` makes about 2,600 theorems about those two look disconnected.
- Undirected connectivity is a weak link: two theorems count as connected if they share any helper lemma.
- The measure reads dependencies in the compiled environment and does not judge what any statement means.

## 5. 重跑 / Rerunning

```bash
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --write
```

**中文。** 需要检查器缓存中有当前源码的编译结果；缺少时脚本停下，先运行 `check_becoming.py`。约 15 秒。不加 `--write` 只打印摘要。

**English.** It needs the cache to hold the current sources' compiled modules; if any is missing the script stops, and `check_becoming.py` should be run first. It takes about 15 seconds. Without `--write` it only prints the summary.

## 6. P130 重跑，两种基 / The P130 rerun, under two base sets

2026-10-16。AI（Claude Opus 5.5）为工作板 P130 所作的重跑，在分支 `p130-frontier-on-base` 的 73d2f2bd 上（Lean 源与提交一致；提交时的核心回执 20261015T231055.702986Z；215 个被跟踪模块，29,151 个常量）。[JSON](THEOREM-CONNECTIVITY.json) 现为这次以原基所得的结果；§3 的数字仍是 108e278e 上那一次的。“之前”一列从同一编译环境中去掉六个新模块的常量算出：没有已有模块导入新模块，所以它恰是 ce808d6a 的状态，与在那里所测一致（7,089 条中 1,093 条独立）。扩展的基只在 `Becoming.Runs` 证明各读法之后才用：过程族加 `Becoming.Law.orbit`（轨道即运行，`Branching.law_run_state`），世界族加 `Becoming.ExchangeLaw` 与 `Becoming.carried`（`ExchangeLaw.courseWorld`、`carriedWorld`）。

2026-10-16. A rerun by the AI (Claude Opus 5.5) for board item P130, on 73d2f2bd of branch `p130-frontier-on-base` (Lean sources match the commit; core receipt at the commit 20261015T231055.702986Z; 215 tracked modules, 29,151 constants). The [JSON](THEOREM-CONNECTIVITY.json) now holds this run under the original base; the numbers of §3 remain those of 108e278e. The "before" columns remove the six new modules' constants from the same compiled environment: no existing module imports a new one, so this is exactly the state at ce808d6a, and it reproduces the measurement taken there (1,093 apart of 7,089). The extended base set is used only after `Becoming.Runs` proved the readings: `Becoming.Law.orbit` joins the Process family (an orbit is a run, `Branching.law_run_state`), and `Becoming.ExchangeLaw` and `Becoming.carried` join the World family (`ExchangeLaw.courseWorld`, `carriedWorld`).

| 类 / Class | 之前，原基 / Before, original | 之后，原基 / After, original | 之前，扩展 / Before, extended | 之后，扩展 / After, extended |
|---|---:|---:|---:|---:|
| 陈述用到两族 / Statement on both families | 124 | 145 | 132 | 154 |
| 陈述用到过程族 / Statement on Process/Frame/Run/Trace | 1,300 | 1,318 | 1,470 | 1,487 |
| 陈述用到世界族 / Statement on World/Flow/Web | 2,676 | 2,711 | 2,861 | 2,903 |
| 证明经过某一族 / Proof through a family | 125 | 127 | 36 | 36 |
| 被基础上的定理使用 / Used by a theorem on the base | 1,771 | 1,888 | 1,744 | 1,836 |
| 独立：自身词汇 / Apart: own vocabulary | 1,001 | 914 | 772 | 705 |
| 独立：只用前导库 / Apart: prelude-only statement | 92 | 84 | 74 | 66 |
| **独立共计 / Apart, total** | **1,093** | **998** | **846** | **771** |
| **定理共计 / Theorems** | **7,089** | **7,187** | **7,089** | **7,187** |

**中文。**
- 98 条新定理无一独立。原基之下 95 条已有定理离开独立类（1,093 → 998），扩展基之下 75 条（846 → 771）；单是扩展基就移动 247 条（1,093 → 846）。
- 两族相遇的陈述由 124 增到 145：`Runs` 16 条、`ParityReadings` 5 条。
- 按模块（原基，之前 → 之后）：Gluing 81 → 43（共 81），Quantum 37 → 9（共 37），Learnable 17 → 7（共 17），Situations 36 → 32，Context 23 → 18，Identification 48 → 44，Learning 42 → 40，Thresholds 24 → 22。Propagation、Loops、Remainder、Routes、Closing、Frequency、Observation 的独立数不变：其主要规律原已被基础上的定理使用，`CourseWorlds` 与 `FormedLoops` 给它们的是基础上的陈述（世界族陈述 2,676 → 2,711）。
- 两族在定义上仍不相及（`families_reach_each_other` 四项皆为假）：一个根是以恰好的对应得到的，不是重新定义。
- 连通分量 65 个，主分量之外 11 条定理，不变。只落在独立定理上的记录仍是 2 条：`selection-through-a-model-of-the-options` 与 `typicality-by-counting`。

**English.**
- None of the 98 new theorems is apart. Under the original base set 95 existing theorems leave the apart classes (1,093 → 998); under the extended base set 75 do (846 → 771). The base extension alone moves 247 (1,093 → 846).
- Statements on both families rise from 124 to 145: 16 in `Runs` and 5 in `ParityReadings`.
- By module (original base, before → after): Gluing 81 → 43 of 81, Quantum 37 → 9 of 37, Learnable 17 → 7 of 17, Situations 36 → 32, Context 23 → 18, Identification 48 → 44, Learning 42 → 40, Thresholds 24 → 22. Propagation, Loops, Remainder, Routes, Closing, Frequency and Observation keep their apart counts: their main laws were already used by theorems on the base, and `CourseWorlds` and `FormedLoops` give them statements on the base (World-family statements 2,676 → 2,711).
- The families still do not reach each other by definition (all four `families_reach_each_other` entries are false): the one root is reached by exact correspondence, not by redefinition.
- Components: 65, with 11 theorems outside the main one, unchanged. Two records still rest only on apart theorems: `selection-through-a-model-of-the-options` and `typicality-by-counting`.

The extended-base and "before" columns are not written to the JSON: the script's base lists are unchanged. They are reproduced by [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py), which imports the measure, changes only its base lists (and, for "before", drops the six new modules' constants) and writes into a folder of its own. 扩展基与“之前”两列不写入 JSON，脚本的基不变；它们由该脚本复现，它导入测量、只改基的列表（“之前”另去掉六个新模块的常量），并写入自己的文件夹。

## 7. 落地头上的重跑 / The rerun on the landing head

2026-10-16。整合者在 `land-p130` 的 29a8556d 上重跑（P129 与 P130 都已合入；Lean 源与提交一致；核心回执 20261016T124157.989030Z；215 个被跟踪模块，29,213 个常量，7,214 条脊柱定理）。[JSON](THEOREM-CONNECTIVITY.json) 现为这次以原基所得的结果；扩展基一列由 [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py) 算出，不写入 JSON。

2026-10-16. The integrator's rerun on 29a8556d of `land-p130`, with both P129 and P130 merged. The Lean sources match the commit; core receipt 20261016T124157.989030Z; 215 tracked modules, 29,213 constants, 7,214 spine theorems. The [JSON](THEOREM-CONNECTIVITY.json) now holds this run under the original base set. The extended-base column comes from [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py) and is not written to the JSON.

| 类 / Class | 原基 / Original | 扩展 / Extended |
|---|---:|---:|
| 陈述用到两族 / Statement on both families | 145 | 154 |
| 陈述用到过程族 / Statement on Process/Frame/Run/Trace | 1,324 | 1,493 |
| 陈述用到世界族 / Statement on World/Flow/Web | 2,711 | 2,903 |
| 证明经过某一族 / Proof through a family | 127 | 36 |
| 被基础上的定理使用 / Used by a theorem on the base | 1,888 | 1,836 |
| 独立：自身词汇 / Apart: own vocabulary | 929 | 720 |
| 独立：只用前导库 / Apart: prelude-only statement | 90 | 72 |
| **独立共计 / Apart, total** | **1,019** | **792** |
| **定理共计 / Theorems** | **7,214** | **7,214** |

**中文。**
- 与 §6 的“之后”一列相比，独立定理多出 21 条（原基 998 → 1,019；扩展基 771 → 792）。它们都是 P129 新增的定理：LLPO 的 19 条辅助与等价定理，以及两条连接定理（`ReferencePlan.alike_iff_agreeOn`、`CrossSituational.distinct_iff`）。没有已有定理变为独立。这些陈述用的是自身词汇或只用前导库，不经过基。
- 两族在定义上仍不相及。
- 连通分量 65 个，主分量之外 11 条定理。
- 只落在独立定理上的记录仍是 2 条：`selection-through-a-model-of-the-options` 与 `typicality-by-counting`。

**English.**
- Against §6's "after" column, there are 21 more apart theorems: 998 → 1,019 under the original base set, and 771 → 792 under the extended one. All 21 are new P129 theorems: 19 helpers and equivalences of LLPO, and two linking theorems (`ReferencePlan.alike_iff_agreeOn`, `CrossSituational.distinct_iff`). No existing theorem became apart. Their statements use their own vocabulary or only the prelude, and do not reach the base.
- The families still do not reach each other by definition.
- There are 65 components, with 11 theorems outside the main one.
- Two records still rest only on apart theorems: `selection-through-a-model-of-the-options` and `typicality-by-counting`.
