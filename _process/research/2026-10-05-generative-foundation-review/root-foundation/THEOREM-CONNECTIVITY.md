<a id="定理层面的连通--how-the-spines-theorems-connect"></a>
# How the spine's theorems connect

> Some passages exist only in the [Chinese edition](THEOREM-CONNECTIVITY.zh.md): sections “Results”.

> so for our theories, they are proved in a dag order and can be all connected right?

2026-10-15, Asia/Bangkok. A measurement made by the AI (Claude Opus 5.5) in a Claude Code session, in answer to Ren's question quoted above. It is a measurement, not a check, and registers no result; no record or generated page is changed. The classes and readings below are the AI's, pending Ren.

[Script](THEOREM-CONNECTIVITY.py) · [Lean dump](THEOREM-CONNECTIVITY-DUMP.lean) · [result, with every spine theorem's class](THEOREM-CONNECTIVITY.json) · module-level companion: [SPINE-INTEGRATION.py](SPINE-INTEGRATION.py)

<a id="1-有向无环--directed-and-acyclic"></a>
## 1. Directed and acyclic

**English.** The proofs are in DAG order, and Lean guarantees it: imports cannot form a cycle and a declaration can use only what precedes it. The import graph of the 113 spine modules is acyclic, with a longest chain of 25 modules. The 508 dependency links between result records are acyclic too, as `research-check` enforces.

<a id="2-方法--method"></a>
## 2. Method

**English.** The compiled modules of the spine run (foundation, core, bridge and the inherited modules the bridge imports; 191 in all) are restored from the checker's shared cache under the keys `check_becoming.py` itself computes, with no recompilation. Lean lists, for each of their 26,505 constants, the tracked constants its type and its value use. The base is two families of definitions:
- the Process family: `Generative.Process` and `Generative.Trace` (GenerativeCore), with `Becoming.Frame` and `Becoming.Run`;
- the World family: `Becoming.World`, with the `Becoming.Flow` and `Becoming.Web` it is built from.

Each spine theorem goes into the first class that fits. Its statement uses both families, only the Process family or only the World family. Otherwise, its proof goes through a family although its statement does not. Otherwise, some constant that reaches the base uses it, directly or indirectly. Failing all of these it stands apart: its statement uses only its module's own definitions, or no tracked constant at all.

<a id="3-结果--results"></a>
## 3. Results

Commit 108e278e, core receipt 20261015T163210.426211Z; the Lean sources match the commit.

| Class | Theorems |
|---|---|
| Statement on both families | 124 |
| Statement on Process/Frame/Run/Trace | 1,110 |
| Statement on World/Flow/Web | 2,607 |
| Proof through a family | 19 |
| Used by a theorem on the base | 1,283 |
| Apart: own vocabulary | 862 |
| Apart: prelude-only statement | 84 |
| Total** | **6,089** |

- **独立的 946 条**中 406 条不被任何常量使用。整模块独立的有 Quantum 37/37、CrossSituational 37/37、Learnable、Segmentation、Retrodiction（各 17/17；Retrodiction 导入 Frame 却不用它）。过半独立的有 Identification 67/105、Learning 63/75、Lasting 63/69、Copying 58/71、ReferencePlan 46/58、Decidedness 38/65、Attraction 35/47、Weighted 30/44 等。

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

<a id="4-界限--what-this-does-not-show"></a>
## 4. What this does not show

**English.**
- "Apart" means no Lean dependency on the base, not that a theorem is wrong or empty. A law stated for every type covers runs and worlds once it is instantiated. What is missing is the theorem that instantiates it.
- The numbers depend on which definitions count as the base. Counting `World` without `Flow` and `Web` makes about 2,600 theorems about those two look disconnected.
- Undirected connectivity is a weak link: two theorems count as connected if they share any helper lemma.
- The measure reads dependencies in the compiled environment and does not judge what any statement means.

<a id="5-重跑--rerunning"></a>
## 5. Rerunning

```bash
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.py --write
```

**English.** It needs the cache to hold the current sources' compiled modules; if any is missing the script stops, and `check_becoming.py` should be run first. It takes about 15 seconds. Without `--write` it only prints the summary.

<a id="6-p130-重跑两种基--the-p130-rerun-under-two-base-sets"></a>
## 6. The P130 rerun, under two base sets

2026-10-16. A rerun by the AI (Claude Opus 5.5) for board item P130, on 73d2f2bd of branch `p130-frontier-on-base` (Lean sources match the commit; core receipt at the commit 20261015T231055.702986Z; 215 tracked modules, 29,151 constants). The [JSON](THEOREM-CONNECTIVITY.json) now holds this run under the original base; the numbers of §3 remain those of 108e278e. The "before" columns remove the six new modules' constants from the same compiled environment: no existing module imports a new one, so this is exactly the state at ce808d6a, and it reproduces the measurement taken there (1,093 apart of 7,089). The extended base set is used only after `Becoming.Runs` proved the readings: `Becoming.Law.orbit` joins the Process family (an orbit is a run, `Branching.law_run_state`), and `Becoming.ExchangeLaw` and `Becoming.carried` join the World family (`ExchangeLaw.courseWorld`, `carriedWorld`).

| Class | Before, original | After, original | Before, extended | After, extended |
|---|---:|---:|---:|---:|
| Statement on both families | 124 | 145 | 132 | 154 |
| Statement on Process/Frame/Run/Trace | 1,300 | 1,318 | 1,470 | 1,487 |
| Statement on World/Flow/Web | 2,676 | 2,711 | 2,861 | 2,903 |
| Proof through a family | 125 | 127 | 36 | 36 |
| Used by a theorem on the base | 1,771 | 1,888 | 1,744 | 1,836 |
| Apart: own vocabulary | 1,001 | 914 | 772 | 705 |
| Apart: prelude-only statement | 92 | 84 | 74 | 66 |
| Apart, total** | **1,093** | **998** | **846** | **771** |
| Theorems** | **7,089** | **7,187** | **7,089** | **7,187** |

**English.**
- None of the 98 new theorems is apart. Under the original base set 95 existing theorems leave the apart classes (1,093 → 998); under the extended base set 75 do (846 → 771). The base extension alone moves 247 (1,093 → 846).
- Statements on both families rise from 124 to 145: 16 in `Runs` and 5 in `ParityReadings`.
- By module (original base, before → after): Gluing 81 → 43 of 81, Quantum 37 → 9 of 37, Learnable 17 → 7 of 17, Situations 36 → 32, Context 23 → 18, Identification 48 → 44, Learning 42 → 40, Thresholds 24 → 22. Propagation, Loops, Remainder, Routes, Closing, Frequency and Observation keep their apart counts: their main laws were already used by theorems on the base, and `CourseWorlds` and `FormedLoops` give them statements on the base (World-family statements 2,676 → 2,711).
- The families still do not reach each other by definition (all four `families_reach_each_other` entries are false): the one root is reached by exact correspondence, not by redefinition.
- Components: 65, with 11 theorems outside the main one, unchanged. Two records still rest only on apart theorems: `selection-through-a-model-of-the-options` and `typicality-by-counting`.

The extended-base and "before" columns are not written to the JSON: the script's base lists are unchanged. They are reproduced by [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py), which imports the measure, changes only its base lists (and, for "before", drops the six new modules' constants) and writes into a folder of its own. 扩展基与“之前”两列不写入 JSON，脚本的基不变；它们由该脚本复现，它导入测量、只改基的列表（“之前”另去掉六个新模块的常量），并写入自己的文件夹。

<a id="7-落地头上的重跑--the-rerun-on-the-landing-head"></a>
## 7. The rerun on the landing head

2026-10-16. The integrator's rerun on 29a8556d of `land-p130`, with both P129 and P130 merged. The Lean sources match the commit; core receipt 20261016T124157.989030Z; 215 tracked modules, 29,213 constants, 7,214 spine theorems. The [JSON](THEOREM-CONNECTIVITY.json) now holds this run under the original base set. The extended-base column comes from [connectivity_bases.py](development/p130-frontier-on-base/connectivity_bases.py) and is not written to the JSON.

| Class | Original | Extended |
|---|---:|---:|
| Statement on both families | 145 | 154 |
| Statement on Process/Frame/Run/Trace | 1,324 | 1,493 |
| Statement on World/Flow/Web | 2,711 | 2,903 |
| Proof through a family | 127 | 36 |
| Used by a theorem on the base | 1,888 | 1,836 |
| Apart: own vocabulary | 929 | 720 |
| Apart: prelude-only statement | 90 | 72 |
| Apart, total** | **1,019** | **792** |
| Theorems** | **7,214** | **7,214** |

**English.**
- Against §6's "after" column, there are 21 more apart theorems: 998 → 1,019 under the original base set, and 771 → 792 under the extended one. All 21 are new P129 theorems: 19 helpers and equivalences of LLPO, and two linking theorems (`ReferencePlan.alike_iff_agreeOn`, `CrossSituational.distinct_iff`). No existing theorem became apart. Their statements use their own vocabulary or only the prelude, and do not reach the base.
- The families still do not reach each other by definition.
- There are 65 components, with 11 theorems outside the main one.
- Two records still rest only on apart theorems: `selection-through-a-model-of-the-options` and `typicality-by-counting`.

<a id="8-u-every-spine-theorem-on-the-base"></a>
## 8. U: every spine theorem on the base

17 October 2026. The integrator's run on the landing tree of board item U (44 join modules; core receipt 20261017T071851.986246Z, 181 spine modules). The [JSON](THEOREM-CONNECTIVITY.json) holds this run. Two changes to the script: record matching now reads the declarations and witnesses of a record's laws, limits and counterexamples as well as its aliases (209 records name spine theorems, against 186 by aliases alone); and the script now reports the roots among the apart theorems with their categories from [THEOREM-CONNECTIVITY-APART.json](THEOREM-CONNECTIVITY-APART.json), and `--check` fails where an apart root has no entry or an entry is no longer an apart root.

| Class | Before U (7b1e7450b) | After U |
|---|---:|---:|
| Statement on both families | 145 | 152 |
| Statement on Process/Frame/Run/Trace | 1,324 | 1,658 |
| Statement on World/Flow/Web | 2,711 | 2,807 |
| Proof through a family | 127 | 127 |
| Used by a theorem on the base | 1,888 | 2,759 |
| Apart: own vocabulary | 929 | 187 |
| Apart: prelude-only statement | 90 | 8 |
| Apart, total** | **1,019** | **195** |
| Theorems** | **7,214** | **7,698** |

- **Roots.** 486 apart roots before, 134 after, every one classified: model witness 40, support 36, bridge interface 22, restates 17, logical strength 13, general structure 6.
- **Records.** None rests only on apart theorems (two before).
- **Components.** 60, with 2 theorems outside the main one (65 and 11 before).
- **The families** still do not reach each other by definition; they meet by exact correspondence.
- Study: [section 166](BECOMING-RENEWAL-READING.md#166-every-spine-theorem-on-the-base-u); how the joins were made: [development/u-unification](development/u-unification/README.md).
