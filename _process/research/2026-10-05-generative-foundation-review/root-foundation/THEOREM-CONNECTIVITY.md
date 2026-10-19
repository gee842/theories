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

## 9. U2: the periphery measured and joined

17 October 2026. This is the integrator's run on the landing tree of board item U2 (core receipt 20261017T113233.209872Z). The [JSON](THEOREM-CONNECTIVITY.json) holds this run.

The script changed in three ways:
- It now measures the periphery of the run as well as the spine: the foundation, the 75 inherited modules and, since U2, the periphery-join modules. The results are reported under `periphery`, with the same classes.
- Periphery roots are held to the same register and `--check`.
- Records are matched against periphery theorems as well.

The dump imports the bridge's new join modules, and the periphery-join modules are added to the dump at run time.

| Class | Spine before U2 (3ed09e437) | Spine after U2 | Periphery after U2 |
|---|---:|---:|---:|
| Statement on both families | 152 | 156 | 0 |
| Statement on Process/Frame/Run/Trace | 1,658 | 1,919 | 586 |
| Statement on World/Flow/Web | 2,807 | 2,823 | 3 |
| Proof through a family | 127 | 127 | 0 |
| Used by a theorem on the base | 2,759 | 2,802 | 701 |
| Apart: own vocabulary | 187 | 173 | 227 |
| Apart: prelude-only statement | 8 | 7 | 2 |
| **Apart, total** | **195** | **180** | **229** |
| **Theorems** | **7,698** | **8,007** | **1,519** |

- **Periphery before U2.** The 78 inherited modules had 1,282 theorems, 814 of them apart and 524 of those roots ([periphery-before.json](development/u-unification/u2/periphery-before.json); the docstring and proof folds of U2 had already been applied).
- **Periphery after U2.** 104 modules (78 inherited, 26 periphery joins) with 1,519 theorems. None of the 237 periphery-join theorems is apart. 171 roots remain, each classified: model witness 112, periphery scope 26, support 15, restates 10, general structure 7, bridge interface 1.
- **Spine roots.** 122, each classified: model witness 40, support 36, bridge interface 19, logical strength 13, restates 8, general structure 6.
- **Records.** `positioned-positive-reason` rests only on periphery theorems that are apart and classified. No spine record does.
- **Components.** 56, with 2 spine theorems outside the main one.
- **Not measured.** The Mathlib leaves (`CorrectionInquiry`, `LearningCorrespondence`) are outside the run.
- **Study.** [Section 167](BECOMING-RENEWAL-READING.md#167-the-unification-follow-through-u2).

<a id="10-reruns-on-each-landing-17-19-october-2026"></a>
## 10. Reruns on each landing, 17–19 October 2026

Moved here on 20 October 2026 (board item R25, twentieth review C4 and G14) from the row “Integration of the spine” of the canonical chapter's §8.2, where each landing from U2 to RG appended its rerun. The text is unchanged, split into one paragraph per rerun, with its links rebased to this file. The chapter keeps one current sentence (§9) and the open item it names (§8.1, item 1). The [JSON](THEOREM-CONNECTIVITY.json) holds the last run, on R27's landing tree (`81f013ca0`, core receipt `20261019T174929.247241Z`): 495 of 11,676 spine theorems apart, 349 roots, each classified.

The [theorem-connectivity measure](#9-u2-the-periphery-measured-and-joined), rerun on the landing tree of board item U2 (receipt 20261017T113233.209872Z), counts 180 of 8,007 spine theorems apart from both base families: 1,019 of 7,214 before U and 195 of 7,698 after it.

Rerun on R1's landing tree (receipt 20261018T000841.184655Z), it counts 180 of 8,078, none of them in `Becoming.LevelCoupling` or `Becoming.Interleavings`.

Rerun with R2 in the tree (receipt 20261018T012738.651832Z), it counts 178 of 8,134, none in `Becoming.CensusCounts`; two theorems of `Becoming.Decidedness` that stood apart are now used on the base.

Rerun with R2b (receipt 20261018T060442.434639Z), it counts 177 of 8,163, none in `Becoming.CensusBinding`; `Counts.pos_of_mem`, an apart root, is now used on the base and left the apart register.

Rerun with L1 (receipt 20261018T070401.460540Z), it counts 177 of 8,178, none in `Becoming.Unrolling`.

Rerun with S1 (receipt 20261018T073050.517313Z), it counts 177 of 8,187, none in `Becoming.Enough`.

Rerun with S2 (receipt 20261018T075849.482455Z), it counts 177 of 8,214, none in `Becoming.Settling`.

Rerun with G1 (receipt 20261018T081005.105592Z), it counts 177 of 8,221, none in `Becoming.SelectionGap`.

Rerun with G2 (receipt 20261018T091757.535800Z), it counts 177 of 8,234, none in `Becoming.SelectionReach`.

Rerun with S3 (receipt 20261018T093527.497358Z), it counts 177 of 8,254, none in `Becoming.LastChange`.

Rerun with M2 (receipt 20261018T122313.319851Z), it counts 177 of 8,287, none in `Becoming.SelectionPool`.

Rerun with G3 (receipt 20261018T150254.342862Z), it counts 175 of 8,304, none in `Becoming.LawAlongRun`.

Rerun with L2 (receipt 20261018T154830.591298Z), it counts 175 of 8,355, none in `Becoming.Labels`.

Rerun with C1 (receipt 20261018T154830.591298Z), it counts 175 of 8,355, none in `Becoming.Exclusion`.

Rerun with F1, the bridge fold (receipt 20261018T134446.673561Z), it counts 175 of 8,287: the transfer of `diamond_correct_iff_em` through the encodings uses `Recipe.ofProgram_toProgram`, which no longer stands apart.

Rerun with M3 (receipt 20261018T165934.927469Z), it counts 175 of 8,373, none in `Becoming.PoolResponse`.

Rerun with G4 (receipt 20261018T200007.370225Z), it counts 201 of 8,676, none in `Becoming.LawThroughCoupling`.

Rerun with F3R sub-chain 2 (receipt 20261018T203356.753598Z), none of the seven theorems of `Becoming.ActivationCapacity` stands apart, and the apart count is unchanged.

Rerun with F3Q, the port of the inquiry and composition family (receipt 20261018T204907.920360Z), it counts 303 of 9,225: 37 of the 278 theorems of its six core modules stand apart (`PartialReadout` 12, `Derivation` 7, `CodeAcquisition` 13, `RouteFormation` 2, `LearnedGrouping` 3), the facts of its constructed examples (the channel, the codes, the Bool countermodel, the supplied logs), the evaluation lemmas of its own grammar, and the two whole-domain equivalences of `PartialReadout` with `Readout` and `Learning`; their 32 roots are in the apart register under the categories of their periphery counterparts.

Rerun with F3 sweep step 1 (receipt 20261018T181445.797056Z), it counts 175 of 8,365: the eight readings that left with `ExplanatoryResiduals` stood connected.

Rerun with F2, joins into the core (receipt 20261018T191422.542444Z), it counts 201 of 8,658: of its six core modules only the witness `ScopedReach.domain_covers` stands apart, and the 22 periphery theorems the joins no longer cite stand apart as laws the core restates, each in the apart register. The other 25 theorems apart since that rerun are in the modules of F3R sub-chain 1, which landed without a connectivity rerun (`StrictTransport` 11, `MatchedCourses` 4, `ProjectedLaws` 4, `ActiveReading` 2, `Dephasing` 2, `SupportRecovery` 1, `Integers` 1); F3R then registered their 21 roots (`39c66e31b`), so every apart root has an entry.

Rerun with the F3 sweep (receipt 20261019T001020.322558Z), it counts 441 of 9,648: no bridge or join module is in the run, and the periphery measured is the three foundation modules.

Rerun with C2 (receipt 20261019T002234.676341Z), it counts 441 of 9,671, none in `Becoming.Exhaustion`.

Rerun with G5 (receipt 20261019T003752.845229Z), it counts 441 of 9,696, none in `Becoming.LawThroughChangingCoupling`.

Rerun with M4 (receipt 20261019T004321.279483Z), it counts 441 of 9,716, none in `Becoming.Rejoining`.

Rerun with A4-L (receipt 20261019T020248.454200Z), it counts 466 of 9,895: 16 of the 99 theorems of `Becoming.Ideals` and 9 of the 80 of `Becoming.HistoryIdeals` stand apart: support lemmas of the order (equivalences, the empty class, unpacked definitions, two laws of directed suprema), the hull's idempotence, whose case of runs is `Becoming.Horizon`'s `Adheres.adheres`, and the classification of the ideals of words with its lemmas, which `Stretches.classification` states for every process; their 18 roots are in the apart register. The first build of the two modules had 115 of 139 apart; reading each law of ideals on the histories of a process (`Stretches`) joined the rest. The apart roots of the superseded modules and of the bridge left the register with them (kept in the fold workspace, [`apart-retired.json`](development/bridge-fold/apart-retired.json)); `ChangingContext.ends` (a model witness) and `Joining.tree_lifts` (a law of every joining), which only the bridge used, now stand apart, so the record `finite-joining-tree-lifting` rests on apart theorems alone. U's 44 join modules state the laws of 78 core modules of runs, processes, traces, frames, worlds, flows and webs: a determined law as a process whose runs are its orbits, a sequence as a run's configurations, a structure's step as a process with the theorem making the reading exact ([study section 166](BECOMING-RENEWAL-READING.md#166-every-spine-theorem-on-the-base-u)). U2 measures the periphery of the run, the 78 inherited modules, by the same classes and joins it with 57 join modules ([study section 167](BECOMING-RENEWAL-READING.md#167-the-unification-follow-through-u2)): 814 of its 1,282 theorems stood apart, and 229 do now. 31 of the join modules are pure and sit on the bridge; 26 go through periphery proofs that carry `propext`, `Quot.sound` or `Classical.choice`, and form a periphery-join ring that the core and the bridge do not import, with every inherited axiom reported. Every one of the 313 apart roots has a category and reason in the [apart register](THEOREM-CONNECTIVITY-APART.json), and the measure's check fails on a new unexplained one. At the sweep's rerun the records resting only on apart theorems are `finite-joining-tree-lifting`.

Rerun with K1 (receipt 20261019T052230.247441Z), it counts 478 of 9,919: 12 of the 24 theorems of `Becoming.Cuts` stand apart, the laws of growth by a list of attachments, whose three roots are registered as general structure; its laws of cutting and joining one link are read on the base through systems (`Flow.system_unchanged_without_iff`, `Flow.withinSystem_two_takers_iff`).

Rerun with K2 (receipt 20261019T054535.337999Z), it counts 467 of 9,946: those laws are now read on a world grown by attachment (`Flow.GrownBy`), and of `Becoming.Cuts`' 51 theorems one stands apart, `Cuts.Attaches.listed_once`, registered as restating `Flow.GrownBy.cond_ne`.

Rerun with K3 (receipt 20261019T055924.801141Z), it counts 466 of 9,946, none in `Becoming.Cuts`: `Flow.GrownBy.cond_ne` now uses `listed_once` for the case of a second listing.

Rerun with Y1 (receipt 20261019T060745.666273Z), it counts 471 of 10,017: 5 of the 71 theorems of `Becoming.Hexagrams` stand apart, the received order's length and pairing and the two lemmas the pairing is told by, facts of the text's one list, whose two roots are registered as support and model witness; its laws are read on the base through `Law.process`, `Branching` and the frame of the lines.

Rerun with V (receipt 20261019T064004.300228Z), it counts 469 of 10,174, none in the five modules `Becoming.Withholding`, `Becoming.LoopReturn`, `Becoming.Pace`, `Becoming.PatternPassing` and `Becoming.JointKeeping`: every main law is stated on a run of the spine (`Law.run`), a `Run`, a viability kernel or a web, and `Law.lost_stays`, registered apart as restating, is now used on the base by `Becoming.Pace` and leaves the register.

Rerun with Y2 (receipt 20261019T080527.161049Z), it counts 490 of 10,282: 21 of the 108 theorems of `Becoming.HexagramPlaces` stand apart, what the 彖 and the 象 say of named configurations and the four censuses, registered as model witnesses, and the six-step law on the orbit, registered as restating; the module's laws are read on the base along the runs of waxing and waning, of the change of one line, of the law backward and of any process, and on the frames of any process.

Rerun with V2 (receipt 20261019T083316.966154Z), it counts 488 of 10,334, none in `Becoming.Tolerance`, whose main laws are stated on runs of the spine (`Law.run`); `FaultEnvelopes.availability_iff_separated` and `FaultEnvelopes.correlated_three_blocks`, registered apart, are now used on the base by `Becoming.Tolerance` and leave the register.

Rerun with U3 (receipt 20261019T092027.048735Z), it counts 426 of 10,388, none in the four modules `Becoming.FrontierFrames`, `Becoming.FrontierWorlds`, `Becoming.AcceptanceFrames` and `Becoming.PresentationFrames`: the largest groups apart, taken by module, are read on the base, the practical commitments with the options of a step as what one move reaches, presentations with the questions as a frame's branching tests, listing with the list as what takes part in a step, and the received pairing of the hexagrams through the law of waxing and waning; 34 apart roots are now used on the base and left the register. The rest stand apart as model witnesses, support lemmas, or general structure whose base reading is the next step, each group's disposition in [study section 196](BECOMING-RENEWAL-READING.md#196-theorems-apart-from-the-base-largest-groups-first-the-practical-commitments-in-the-core-u3-u4).

Rerun with Y3 (receipt 20261019T101219.302788Z), it counts 439 of 10,571: 13 of the 132 theorems of `Becoming.HexagramLaws` stand apart, the censuses over the received order and the facts of which pairs it makes by which symmetry, registered as model witnesses, and the composition table of the symmetries and the order's listing, registered as support; the module's laws are read on the base along the runs of each law and on its process.

Rerun with SG (receipt 20261019T102354.824114Z), it counts 441 of 10,706: none of the theorems of `Becoming.Junctures` and `Becoming.Commuting` stands apart, their laws stated on processes, traces and runs (`Law.run`), and of the 64 of `Becoming.Undecided` two do, `Undecided.incomplete`, a law of every family of three-valued readings registered as general structure, and the lemma it uses; revision is stated on its run.

Rerun with the Y3 follow-up after SG (receipt 20261019T103817.145646Z), where `Becoming.HexagramLaws` states two of its laws as instances of `Law.Commutes.iterate` and `Law.Commutes.apart`, it counts 441 of 10,704, 13 of the 130 theorems of `Becoming.HexagramLaws` apart with the same roots.

Rerun with Z1 (receipt 20261019T110924.527968Z), it counts 441 of 10,744: none of the 40 theorems of `Becoming.RelativePosition` stands apart.

Rerun with Y4 (receipt 20261019T113250.301688Z), it counts 464 of 10,847: 23 of the 103 theorems of `Becoming.HexagramSites` stand apart, what the 彖, the 小象, the 文言, the line texts and 王弼's 略例下 say of named configurations, the censuses, 王弼's dilemma and the witnesses and census of the twelve configurations with a sole line, registered as model witnesses, and 2 lemmas only they use; the module's laws are read on the base along the runs of waxing and waning, of the change of one line, of the law backward and of any process.

Rerun with PT1 (receipt 20261019T122417.550535Z), it counts 464 of 10,920, none in `Becoming.PlaceTransitionNets`, whose laws are stated on a net's flow, web and world.

Rerun with LL1 (receipt 20261019T124334.350424Z), it counts 511 of 10,994: 47 of the 74 theorems of `Becoming.LeastLoss` stand apart, the dyadic and layered models and their arithmetic, while its laws are used on the base by its six whole-number restatements (`World.rests_unrefuted_enclosed_whole` among them).

Rerun with O1 and O2 (receipt 20261019T130853.816105Z), it counts 519 of 11,150, 8 of them in `Becoming.Verification`: its laws are stated at points read as ideals and read on runs, and the seven roots left apart are registered (five interior lemmas whose run forms are stated, one restatement and one calibration), and none of `Becoming.LimitVerification`'s stands apart.

Rerun with SC (receipt 20261019T141645.763808Z), it counts 488 of 11,412, none in `Becoming.SharedCodes`, whose laws are stated on runs of hearing and on the runs of its laws.

Rerun with HS (receipt 20261019T143634.829557Z), it counts 492 of 11,453, 4 of 41 in `Becoming.HistorySums`: two witnesses that grouping by order needs commuting, the self-loop's exact orders, and the weight along a joined course, registered; each other law of the module is read on the traces of a process.

Rerun with MD1 (receipt 20261019T144846.235357Z), it counts 495 of 11,486: 3 of the 33 theorems of `Becoming.MutualDependence` stand apart, the pace of a selection stated for any listing of offspring (`share_ratio_pow`, registered). There are 66 dependency components, with 18 spine theorems outside the main one; 163 statements use both families.

Rerun with E1 (receipt 20261019T100412.397267Z), it counts 426 of 10,439, none in `Becoming.ExchangePremises`, whose laws are stated on flows, webs and worlds read off laws of exchange; 58 dependency components, 20 spine theorems outside the main one, 161 statements on both families.

Rerun with U5 (receipt 20261019T133615.720595Z), it counts 480 of 11,195 (519 of 11,150 before), none in `Becoming.WitnessRefinementRuns`, `Becoming.NarrowingRuns`, `Becoming.HistoryIdealsTraces` or `Becoming.FrontierWorlds`: the groups study section 196 left apart as general structure without a base object are stated on the base, joint plans and undertakings on a world's moves, the roster laws on the process of inspection for every roster, the safe and greatest answer on the belief narrowed on the pure observation and its runs, and the word half on the courses a process can take; 22 apart roots are now used on the base and left the register, and what stays apart in these modules is model witnesses and support ([study section 208](BECOMING-RENEWAL-READING.md#208-general-laws-read-on-the-base-joint-plans-inspection-narrowing-and-the-histories-of-words-u5)); 64 dependency components, 18 spine theorems outside the main one, 161 statements on both families.

Rerun with Y5 (receipt 20261019T140534.048868Z), it counts 488 of 11,293 (480 of 11,195 before): 9 of the 98 theorems of `Becoming.HexagramSequences` stand apart, the 雜卦's list and the order's pairing as facts about the texts' lists, the census of the twenty with three unbroken lines, the opposite stations of 說卦 ch. 5 and two restatements, registered, and 1 lemma only they use; the module's laws are read on the base along the runs of the laws running the order, of waxing and waning, of the change of one line and of the exchanges; 65 dependency components, 18 spine theorems outside the main one, 163 statements on both families.

Rerun with RC (receipt 20261019T151254.157652Z), it counts 496 of 11,539, one of them in `Becoming.RuleCapture`: `Counts.share_not_lower_counts` restates `share_not_lower` in the share order of counts and is registered as a restatement, while every other law of the module is stated on the two-level course of `Becoming.Pace` ([study section 213](BECOMING-RENEWAL-READING.md#213-capture-through-the-rule-rc)); 66 dependency components, 18 spine theorems outside the main one, 163 statements on both families.

Rerun with RG (receipt 20261019T152617.511553Z), it counts 495 of 11,647 (496 of 11,539 before), none in `Becoming.Regulation`, whose laws are stated on a flow and a web; `gap_le_iff` is now used on the base and left the register ([study section 214](BECOMING-RENEWAL-READING.md#214-a-level-held-from-both-sides-and-a-level-read-late-rg)); 66 dependency components, 18 spine theorems outside the main one, 163 statements on both families. The two course worlds are two readings of one flow and one web, defined once. Duplicated proofs of one law now cite one proof, except the Law forms of `Recurrence`, which the general process forms import. The Process family and the World family still do not reach each other by definition; they meet through exact correspondence theorems. The Mathlib leaves are outside the run and not measured. Open: a definitional join of the two families.

Rerun with R28, one base by definition (receipt 20261019T181519.226999Z, 20 October 2026), it counts 485 of 11,684 (495 of 11,676 before). A world is now a run by its type, so the World family reaches the Process family: `families_reach_each_other` is true from World to Process, the acceptance test of the twentieth review's step 4, and stays false from Process, Flow and Web, since a process need not be a world and flows and webs (`Web` is `Dependence Nat`) are records over the step index. Statements on both families rise from 163 to 870, every statement on `World` now among them. With `Law.*` abbreviations at `Law.process`, four orbit forms that restated their `Branching` forms reach the process and are no longer apart roots (`Law.Lossless.unlisted`, `Law.drawn_of_lost`, `Law.loss_needs_merge`, `Law.rise_not_lossless`); their entries moved to [the R28 kit](development/r28-one-base/apart-retired.json) ([study section 219](BECOMING-RENEWAL-READING.md#219-one-base-by-definition-the-run-r28)). 345 apart roots, 12 of them restatements; 66 dependency components, 18 spine theorems outside the main one. The measure's definition of the two families is unchanged; its docstring now says what they are under one base. Open: the companion modules that carried laws across the old gap fold back (R32).

Rerun with R29, compression under board rule 9 (receipt 20261019T185632.962707Z, 20 October 2026), it counts 489 of 11,658 (485 of 11,684 before). The families are unchanged: World reaches Process, and Process, Flow and Web reach neither; 866 statements are on both families (870 before, the removed second names among them). The two whole-number restatements in the register were removed, and their entries moved to [the R29 kit](development/r29-compression/apart-retired.json). Four theorems whose only user was a removed second name are now apart roots, each registered with its reason: `Dependence.level_registers`, `unrefuted_falls_exceed` (support), `ExchangeLaw.Nonanticipating.readsFinitely_of_every` and `no_chain_of_no_loop_listed` (general structure) ([study section 220](BECOMING-RENEWAL-READING.md#220-compression-below-not-beside-r29)). There are 347 apart roots, 10 of them restatements; 66 dependency components, 18 spine theorems outside the main one.

Rerun with R30, one notion, one name (receipt 20261019T194851.524223Z, 20 October 2026), it counts 489 of 11,658, as before: renaming changes no statement, so no theorem changes class. The families are unchanged (World reaches Process; Process, Flow and Web reach neither), and 866 statements are on both families. The register's nine entries whose theorems were renamed are keyed by the new names, and four reasons name renamed declarations by the table ([the R30 kit's apart.py](development/r30-names/apart.py), [study section 221](BECOMING-RENEWAL-READING.md#221-one-notion-one-name-r30)). There are 347 apart roots, 10 of them restatements; 66 dependency components, 18 spine theorems outside the main one.

Records: [worlds-are-runs](../../../../theories/becoming/results/records/worlds-are-runs.md), [becoming-spine-instances](../../../../theories/becoming/results/records/becoming-spine-instances.md).
