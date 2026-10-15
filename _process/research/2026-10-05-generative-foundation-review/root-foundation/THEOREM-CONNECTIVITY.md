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
