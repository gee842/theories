<a id="定理层面的连通--how-the-spines-theorems-connect"></a>
# 定理层面的连通

> **中文版（2026-10-17）。** 正典文本是[英文版](THEOREM-CONNECTIVITY.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-15，Asia/Bangkok。AI（Claude Opus 5.5）在一次 Claude Code 会话中应 Ren 的问题所作的测量。Ren 的原话：

本文是测量，不是检查，也不登记成果；它不改动任何记录或生成页面。下面的分类与解读是 AI 的，待 Ren 审阅。

<a id="1-有向无环--directed-and-acyclic"></a>
## 1. 有向无环

**中文。** 证明按有向无环图的次序排列，这一点由 Lean 保证：导入不能成环，一个声明只能使用在它之前的声明。113 个脊柱模块的导入图无环，最长导入链 25 层。成果记录的 508 条依赖也无环，由 `research-check` 强制。

<a id="2-方法--method"></a>
## 2. 方法

**中文。** 从检查器的共享缓存按 `check_becoming.py` 自己算出的键还原脊柱运行的全部编译模块（基础、核心、桥及桥所导入的继承模块，共 191 个），不重新编译。Lean 列出其中每个常量（26,505 个）的类型与值所用到的被跟踪常量。“基础”是两族定义：
- 过程族：`Generative.Process`、`Generative.Trace`（GenerativeCore），以及 `Becoming.Frame`、`Becoming.Run`；
- 世界族：`Becoming.World`，以及构成它的 `Becoming.Flow`、`Becoming.Web`。

每条脊柱定理归入第一个适用的类：陈述用到两族、只用到过程族或只用到世界族；陈述不用、证明经过某一族；被某个到达基础的常量（直接或间接）使用；都不是则为“独立”，即陈述只用本模块自己的定义，或不用任何被跟踪的常量。

<a id="3-结果--results"></a>
## 3. 结果

| 类 | 定理 |
|---|---|
| 陈述用到两族 | 124 |
| 陈述用到过程族 | 1,110 |
| 陈述用到世界族 | 2,607 |
| 证明经过某一族 | 19 |
| 被基础上的定理使用 | 1,283 |
| 独立：自身词汇 | 862 |
| 独立：只用前导库 | 84 |
| **共计 | **6,089** |

**中文。**
- **两个根，而非一个。** `Flow`、`Web`、`World` 都不到达过程族，`Process` 也不到达世界族。两族只在 124 条陈述中相遇，主要在 Correspondence（18）、Relevance（16）、Descent（15）、Ranking（13）、Dependence（10）、Joint 与 Regrouping（各 8）、Unfolding 与 Testing（各 6）。Unfolding 以对应定理表明过程与框架是同一展开的读法，但两族都不由对方定义。
- **无向连通。** 6,089 条中 6,055 条在同一连通分量里；另外 34 条（Retrodiction 全部 17 条、Readout 9 条、Seeking 3 条、Learning 2 条及 3 条单独的定理）与其余不共享任何定义。
- **记录。** 179 条记录以别名指向脊柱定理。按其最好的一条，16 条陈述用到两族，62 条用到过程族，67 条用到世界族，5 条证明经过某一族，3 条被基础使用，26 条只落在独立定理上。这 26 条按模块：Copying 4、Bridge 4、Readout 3、Lasting 3（`market-*`）、CrossSituational 3，Weighted、Countdown、Segmentation 各 2，Retrodiction、Feedback、Description 各 1。完整清单见 [JSON](THEOREM-CONNECTIVITY.json) 的 `records_resting_only_on_apart_theorems`。
- **与早先一次的比较。** 在 69336fa3（6,019 条定理）上独立 890 条、只落在独立定理上的记录 21 条。I3d、I3e 之后新增的 5 条（binding-preserving-substitution、growth-constrained-fragmentation、material-preparation-output、organizational-formation-from-generative-comparison、risk-certificate-outcome-distinction）已陈述在脊柱上，其定理却陈述在各自的词汇上。可见“陈述在脊柱上”（SPINE-INTEGRATION.py 的计数）不等于“落在基础上”。

<a id="4-界限--what-this-does-not-show"></a>
## 4. 界限

**中文。**
- “独立”指在 Lean 中不依赖基础，不是说定理错误或空洞。对任意类型陈述的规律，一旦实例化就覆盖运行与世界；所缺的是作出这一实例化的定理。
- 数字取决于把哪些定义算作基础：只算 `World` 而不算 `Flow`、`Web` 时，约 2,600 条关于这两者的定理会显得不连通。
- 无向连通是很弱的联系：两条定理只要共用任一辅助引理，就算相连。
- 测量读的是编译环境中的依赖，不判断任何陈述的含义。

<a id="5-重跑--rerunning"></a>
## 5. 重跑

```bash
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --write
```

**中文。** 需要检查器缓存中有当前源码的编译结果；缺少时脚本停下，先运行 `check_becoming.py`。约 15 秒。不加 `--write` 只打印摘要。

<a id="6-p130-重跑两种基--the-p130-rerun-under-two-base-sets"></a>
## 6. P130 重跑，两种基

2026-10-16。AI（Claude Opus 5.5）为工作板 P130 所作的重跑，在分支 `p130-frontier-on-base` 的 73d2f2bd 上（Lean 源与提交一致；提交时的核心回执 20261015T231055.702986Z；215 个被跟踪模块，29,151 个常量）。[JSON](THEOREM-CONNECTIVITY.json) 现为这次以原基所得的结果；§3 的数字仍是 108e278e 上那一次的。“之前”一列从同一编译环境中去掉六个新模块的常量算出：没有已有模块导入新模块，所以它恰是 ce808d6a 的状态，与在那里所测一致（7,089 条中 1,093 条独立）。扩展的基只在 `Becoming.Runs` 证明各读法之后才用：过程族加 `Becoming.Law.orbit`（轨道即运行，`Branching.law_run_state`），世界族加 `Becoming.ExchangeLaw` 与 `Becoming.carried`（`ExchangeLaw.courseWorld`、`carriedWorld`）。

| 类 | 之前，原基 | 之后，原基 | 之前，扩展 | 之后，扩展 |
|---|---:|---:|---:|---:|
| 陈述用到两族 | 124 | 145 | 132 | 154 |
| 陈述用到过程族 | 1,300 | 1,318 | 1,470 | 1,487 |
| 陈述用到世界族 | 2,676 | 2,711 | 2,861 | 2,903 |
| 证明经过某一族 | 125 | 127 | 36 | 36 |
| 被基础上的定理使用 | 1,771 | 1,888 | 1,744 | 1,836 |
| 独立：自身词汇 | 1,001 | 914 | 772 | 705 |
| 独立：只用前导库 | 92 | 84 | 74 | 66 |
| **独立共计 | **1,093** | **998** | **846** | **771** |
| **定理共计 | **7,089** | **7,187** | **7,089** | **7,187** |

**中文。**
- 98 条新定理无一独立。原基之下 95 条已有定理离开独立类（1,093 → 998），扩展基之下 75 条（846 → 771）；单是扩展基就移动 247 条（1,093 → 846）。
- 两族相遇的陈述由 124 增到 145：`Runs` 16 条、`ParityReadings` 5 条。
- 按模块（原基，之前 → 之后）：Gluing 81 → 43（共 81），Quantum 37 → 9（共 37），Learnable 17 → 7（共 17），Situations 36 → 32，Context 23 → 18，Identification 48 → 44，Learning 42 → 40，Thresholds 24 → 22。Propagation、Loops、Remainder、Routes、Closing、Frequency、Observation 的独立数不变：其主要规律原已被基础上的定理使用，`CourseWorlds` 与 `FormedLoops` 给它们的是基础上的陈述（世界族陈述 2,676 → 2,711）。
- 两族在定义上仍不相及（`families_reach_each_other` 四项皆为假）：一个根是以恰好的对应得到的，不是重新定义。
- 连通分量 65 个，主分量之外 11 条定理，不变。只落在独立定理上的记录仍是 2 条：`selection-through-a-model-of-the-options` 与 `typicality-by-counting`。

<a id="7-落地头上的重跑--the-rerun-on-the-landing-head"></a>
## 7. 落地头上的重跑

2026-10-16。整合者在 `land-p130` 的 29a8556d 上重跑（P129 与 P130 都已合入；Lean 源与提交一致；核心回执 20261016T124157.989030Z；215 个被跟踪模块，29,213 个常量，7,214 条脊柱定理）。[JSON](THEOREM-CONNECTIVITY.json) 现为这次以原基所得的结果；扩展基一列由 [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py) 算出，不写入 JSON。

| 类 | 原基 | 扩展 |
|---|---:|---:|
| 陈述用到两族 | 145 | 154 |
| 陈述用到过程族 | 1,324 | 1,493 |
| 陈述用到世界族 | 2,711 | 2,903 |
| 证明经过某一族 | 127 | 36 |
| 被基础上的定理使用 | 1,888 | 1,836 |
| 独立：自身词汇 | 929 | 720 |
| 独立：只用前导库 | 90 | 72 |
| **独立共计 | **1,019** | **792** |
| **定理共计 | **7,214** | **7,214** |

**中文。**
- 与 §6 的“之后”一列相比，独立定理多出 21 条（原基 998 → 1,019；扩展基 771 → 792）。它们都是 P129 新增的定理：LLPO 的 19 条辅助与等价定理，以及两条连接定理（`ReferencePlan.alike_iff_agreeOn`、`CrossSituational.distinct_iff`）。没有已有定理变为独立。这些陈述用的是自身词汇或只用前导库，不经过基。
- 两族在定义上仍不相及。
- 连通分量 65 个，主分量之外 11 条定理。
- 只落在独立定理上的记录仍是 2 条：`selection-through-a-model-of-the-options` 与 `typicality-by-counting`。
