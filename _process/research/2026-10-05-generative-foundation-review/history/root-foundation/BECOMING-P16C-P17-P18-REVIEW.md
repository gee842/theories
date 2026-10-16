# P16c、P17 与 P18 的独立审查 / Independent review of P16c, P17 and P18

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写这三个阶段。对象：`main` 的 `badb652e`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of the three phases. Object: `main` at `badb652e`.

**摘要（中文）。** 三个阶段的全部 Lean 声明都在仓库之外从前导重新编译。核心闭包的 24 个模块退出码为 0，没有警告，1356 条源声明的公理报告全部为空。回执 `20261009T091503.719598Z`（799 项定理／1286 项声明审计，核心闭包 24 个模块，包 22 个模块）、37 个源哈希、保留运行的 221 个产物、20 份变更记录的 247 个引用哈希与 57 个证明绑定都对。398 个别名中 367 个在核心中解析，其余 31 个属于未重建的桥接（26）与 Mathlib 外围（5）。数学被接受，Lean 中没有发现数学错误。本审查写了 77 条探针声明（其中 54 项定理），都不依赖任何公理。问题共十项（L1–L10）：一项定义与其陈述的意义不符，两项散文中的错误，四项说得过强，一项缺少反例，两项记账与表述。

- **P16c（第七次审查的处理）。** K1–K8 都有处理，探针内容移入了核心。`Around`、`Inward`、`taking_draws_in`、`generation_draws_in`、`Covered`、`needs_new`、`Merge.idle`、`Confluence` 与 `EmbodiedSun` 都对。第七次审查没有构造的一步（`Enclosed.around`）也已证明。问题是残余。
  - **把体现读作生命（L1）。** K6 的更正没有带到所有地方。`Roles` 的三处标题与说明仍把 `active_of_bearing` 叫作“生作为生的条件”。P16c 自己写的 §23.4 反驳 4 说“生命以其他生命为条件”。章节、§18 与英文段落里仍有“承担自身的生命”“一个生命的生起”“need not be a life”。章节 §2 的中文保留了一句英文中没有的 AI 读法。
  - **省略前提的残余（L2）。** `Dissipation` 的模块标题仍是无条件的“汲入”。两份记录的 `related` 条目仍写“部分不长久”，其中一条还写“构成”。
  - **记账与用语（L3）。** 有六处：“给予者”残留在 §22 与计划中；“每条声明的公理报告为空”没有排除编译器生成的 `injEq` 引理；§24 的反驳次序是 1、2、3、4、6、5；英文用“draws”表示“耗用储备”；P16b 的英文段落仍把包写成核心；记录的审查时间早于它所引用的运行。
- **P17（储备与开始作为条件而在）。** `carries_zero` 恰好成立，`Dependent` 就是零储备。`lasts`、`lasts_within`、`active_finitely`、`arising_finitely`、`decays_by`、`ends_within`、`consumed_lasts` 与 `coextinct_lasts` 都对，`Seed`、`Viable` 与 `Famine` 达到这些界。`came_to_stand`、`Provisioned` 与 `Sleeper` 都对，`Sleeper` 耗散为空这一点已经披露。`Roles` 中九个体现定理改由 `ComesToStand` 推出，陈述不变。问题如下。
  - **“储备是所持的条件”（L4）。** 定理只给出一个方向：所持条件的水平可以是储备。本模块自己的见证 `Seed` 与 `Viable` 的储备不是任何条件的水平，它们的网中也没有所持条件能承载种子。所以储备在那里是另设的量，而不是“不是新的原语”。
  - **前提 `drawn` 的误述（L5）。** 散文与记录说持有者从所持的条件取用。前提只要求有形成从中取用。`Larder` 中，狐不参与、不取用，乌鸦吃掉脂肪，`carries_of_held` 的全部前提仍成立。
  - **转化的读法改变 living（L6）。** “同一展开”的两种读法对狐第 1 步的事件给出不同的 living：原读法下它侵蚀，转化的读法下不侵蚀。转化的读法可以一般地构造（`redirect_dependent`），所以它满足 `Dependent` 是由构造给出的，研究列为开放的一步在这里完成。
  - **要求跟着上升走（L7）。** 证明只用到水平上升带来的正的给予，不用从零开始。任何上升都如此（`rise_given`、`rise_lowers_on`、`Growing`）。
- **P18（以之为生与世系）。** 定理都对。`relabel_sustenance` 是真见证。`Brood.descended` 按陈述成立。整个关系项之间的世系已在模块说明、记录与反驳 2 中披露。问题如下。
  - **`LivesOn.active` 的省略前提（L8）。** 定理把“所依的关系项体现”作为假设。散文写成在 `Dependent` 之下只能以活跃的体现关系项为生。`Drowsy` 中，吃者在 `Dependent` 之下以一个既不体现、该步也不活跃的关系项为生。`Dependent` 实际给出的是：所依的关系项在该步作为条件而在（`LivesOn.stands`）。
  - **“体现第一次进入估值”（L9）。** `sustenance` 与 `descent` 的定义都不含 `Embodied`。进入估值的是一类读法的同一对应。
  - **世系接受不参与的给予者（L10，最严重）。** `Flow.Descends` 读的是 `give`，不要求给予的形成参与该步。不参与者的 `give` 不进入任何水平，平衡与 `Acting` 都不约束它。`Stranger` 中，两个流有同样的参与者、同样的 `given`，都平衡且 `Acting`，只差一个不参与者的 `give` 条目；世系连通一个而不连通另一个。在 `Brood` 中给予不看给予者，所以每一代都“从”每个自然数而来。所以“空的给予不造成世系，§10 排除的免费连通没有回来”在定义上不成立。要求给予者参与（`DescendsIn`）之后，已发表的正面结果全部保留，虚假的世系消失。
- **K1–K8。** K2、K5、K7 关闭。K1、K3、K4 关闭而有残余（L2）。K6 在指定处关闭，残余见 L1。K8 的八项中五项关闭，(c)、(g)、(h) 的模式再现（L3）。
- **非二元方法、Ren 的原话与读法选择。** 以之为生与世系是否算作 N_rel 所传递的形成关系，留给了 Ren。“生”的读法、接续、终结之步的汲取与“生生不息”读到哪个层次，都没有替 Ren 选择。Ren 的原话引用准确。L1 中的残余把体现读作生命，这是 K6 已经指出、P16c 已经承认属于 Ren 的读法。

**Summary (English).** Every Lean declaration of the three phases recompiles from the prelude outside the repository. The 24 modules of the core closure exit 0 with no warnings, and all 1356 of their source declarations have empty axiom reports. The receipt `20261009T091503.719598Z` (799 theorems and 1286 declaration audits; core closure 24 modules, package 22) is correct, as are its 37 source hashes, the 221 artifacts of its retained run and, for the 20 changed records, 247 reference hashes and 57 proof bindings. Of the 398 aliases, 367 resolve in the core; the other 31 belong to the unrebuilt bridge (26) and the Mathlib periphery (5). The mathematics is accepted; no mathematical error was found in the Lean. This review wrote 77 probe declarations (54 of them theorems), none of which depends on any axiom. The ten findings (L1–L10) are: one definition that does not match its stated meaning, two errors in prose, four overclaims, one missing counterexample, and two items of bookkeeping and presentation.

- **P16c (handling of the seventh review).** K1–K8 are all addressed, and the probe content moved into the core. `Around`, `Inward`, `taking_draws_in`, `generation_draws_in`, `Covered`, `needs_new`, `Merge.idle`, `Confluence` and `EmbodiedSun` are correct. The step the seventh review left unbuilt (`Enclosed.around`) is proved. The findings are residues.
  - **L1.** The K6 correction did not reach every place. Three headings and docstrings in `Roles` still call `active_of_bearing` "life as a condition of life". The §23.4 rebuttal 4, written in P16c, says "生命以其他生命为条件". The chapter, §18 and the English paragraphs still say "a life that bears on itself", "一个生命的生起" and "need not be a life". The Chinese of chapter §2 keeps an AI-reading sentence that the English omits.
  - **L2.** The `Dissipation` module title still says "draws in" without the enclosure. Two records' `related` entries still say "parts that do not last", and one also says "made of".
  - **L3.** Six bookkeeping items: "给予者" survives in §22 and the plan; "every declaration has an empty axiom report" does not exclude compiler-generated `injEq` lemmas; the §24 rebuttals run 1, 2, 3, 4, 6, 5; the English uses "draws" for "uses the reserve"; the English P16b paragraph still calls the package the core; and records carry review stamps earlier than the run they cite.
- **P17 (reserve, and coming to stand).** `carries_zero` holds exactly, so `Dependent` is the zero reserve. `lasts`, `lasts_within`, `active_finitely`, `arising_finitely`, `decays_by`, `ends_within`, `consumed_lasts` and `coextinct_lasts` hold, and `Seed`, `Viable` and `Famine` attain the bounds. `came_to_stand`, `Provisioned` and `Sleeper` are correct, and the vacuity of `Sleeper`'s dissipation is disclosed. The nine embodied theorems of `Roles` are re-derived through `ComesToStand` with their statements unchanged.
  - **L4.** "A reserve is a held condition" states an identity, but the theorem gives one direction: a held condition's level can be a reserve. The module's own `Seed` and `Viable` are carried by reserves that are no condition's level, and no held condition of their webs carries the seed. There the reserve is a supplied amount, not "no new primitive".
  - **L5.** The prose and the record say that the holder takes from what it holds. The premise only says that something takes from it. In `Larder` the fox takes no part and takes nothing, a crow eats the fat, and every premise of `carries_of_held` holds.
  - **L6.** The two readings of "the same unfolding" disagree on whether the fox's event at step one is living: it undermines under the published reading and does not under the transformed one. The transformed reading can be built in general (`redirect_dependent`), so its being `Dependent` holds by construction; this completes a step the study lists as open.
  - **L7.** The proofs use only the positive gift that any rise of level brings, not the start from zero (`rise_given`, `rise_lowers_on`, `Growing`).
- **P18 (living on and descent).** The theorems hold. `relabel_sustenance` is a genuine witness. `Brood.descended` holds as stated. Descent between whole relata is disclosed in the module doc, the record and rebuttal 2.
  - **L8.** `LivesOn.active` assumes that the lived-on relatum is embodied. The prose says that under `Dependent` an active formation lives only on an embodied relatum active at that step. In `Drowsy` an eater under `Dependent` lives on a relatum that is neither embodied nor active at that step. What `Dependent` gives is that the lived-on relatum stands at that step (`LivesOn.stands`).
  - **L9.** Neither `sustenance` nor `descent` mentions `Embodied`. What enters the valuation is the one-kind identification, not embodiment.
  - **L10 (the most serious).** `Flow.Descends` reads `give` and does not require the giver to take part in the step. A `give` entry of a formation not taking part enters no level, and neither balance nor `Acting` constrains it. In `Stranger`, two flows with the same formation taking part and the same `given`, both balanced and `Acting`, differ in one such entry, and descent connects one and not the other. In `Brood` the giver is ignored, so every generation "descends" from every number. So "no empty giving makes descent, and the free connection excluded in §10 does not return" is false of the definitions. With the giver required to take part (`DescendsIn`), every published positive result survives and the spurious descents vanish.
- **K1–K8.** K2, K5 and K7 are closed. K1, K3 and K4 are closed with residues (L2). K6 is closed where it was located, with residues (L1). Five of K8's eight items are closed; the patterns of (c), (g) and (h) recur (L3).
- **Ren.** Whether living on and descent count as formed relations for N_rel is left to Ren. No reading of 生, succession, drawing at an ending or the level of 生生不息 is chosen for Ren. Ren's words are quoted exactly. The residues in L1 read embodiment as life, a reading that K6 identified and P16c acknowledges as Ren's.

## 0. Scope, materials and method

**Object.** `main` at `badb652e73fc614550cab8ffa41472fd3c0b209c`:

- **P16c (`eb700342e0bdfc03`).**
  - The handling of K1–K8 of [BECOMING-P15-P16-P16B-REVIEW](BECOMING-P15-P16-P16B-REVIEW.md) in `Dissipation`, `Roles`, `Wholes`, `Identity` and the root module.
  - Study §23, the in-place corrections to §17 and §20–§22, and the English P16c paragraph.
  - The five corrected records (generation-is-replenishment, no-finite-part-bears-taking, whole-persists-through-generation, life-as-condition-of-life, identity-across-steps) and the plan row 157.
- **P17 (`c8549538be8f91ef`).**
  - [Becoming.Reserve](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Reserve.lean) in full.
  - `Web.ComesToStand`, `eq_zero_of_not_pos` and the `standing_*` theorems in `Flow` and `Dissipation`; `Embodied.comesToStand`, `Embodied.coming` and the nine re-derived theorems in `Roles`.
  - Study §24 and its English paragraph; the record [reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md) and the extension of generation-is-replenishment; the chapter's new sentences (§1 lines 130 and 141, §2 lines 203 and 205, §8, §9 row 465, glossary lines 518–522).
- **P18 (`badb652e73fc6145`).**
  - [Becoming.Descent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Descent.lean) in full.
  - Study §25 and its English paragraph; the record [living-on-and-descent](../../../../theories/becoming/results/records/living-on-and-descent.md); the chapter's §2 bullet (line 339), §8 rows, §9 row 469 and glossary lines 528–529; the plan rows 158–159.

**Isolation.** The object was exported with `git archive badb652e` into the reviewer's scratch directory; every file was read from there. Nothing in the live repository or its `.git` was modified except the addition of this file. Another session was editing the working tree during the review; its uncommitted changes were not read. No `make` target or repository checker was run, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where reviews are filed.

**Materials** (sha256 prefixes at `badb652e`):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `6a0ff630e23bf468` |
| chapter `THE-THEORY-OF-BECOMING.md` | `d82ba3b4ea689ecb` |
| previous review `BECOMING-P15-P16-P16B-REVIEW.md` / plan `BECOMING-UNIFICATION-PLAN.md` | `10f7315ace2daa1f` / `75efedb7c1fab9c2` |
| `NONDUAL-METHOD.md` / `AGENTS.md` | `8c48b03a167a8909` / `da432369737e9a1f` |
| receipt `becoming-verification.json` / `check_becoming.py` | `eddb85693d93cfdb` / `fe6e99ef743106f6` |
| `Becoming.lean` / package `README.md` | `e069fed12890c057` / `9476c0f155d68118` |
| `Becoming/Reserve` / `Descent` | `6d2838c3758f5830` / `83ac38caf8e2199d` |
| `Becoming/Flow` / `Dissipation` / `Roles` | `edb5948be82fef13` / `2a25b6c4f65c2fdf` / `0083004bf5773638` |
| `Becoming/Correspondence` (unchanged) / `Metaethics` | `e34e6fa72be7ba9d` / `4ab1143c29ddcfe1` |
| records reserve-defers-ending / living-on-and-descent | `83f2c13614faaa16` / `f3c6ee103215994d` |
| records generation-is-replenishment / life-as-condition-of-life | `e103c0c259bc61b7` / `a80b00b295d6d057` |
| records no-finite-part-bears-taking / whole-persists-through-generation / identity-across-steps | `ac55687fbe2d96b0` / `a3ea3a6145ef2ce6` / `7ee7c624120a230a` |

**Read in full:**

- AGENTS.md, the nondual method and the seventh review.
- Study §23–§25 and the English P16c, P17 and P18 paragraphs; §17, §18 and §20–§22 where P16c corrected them.
- `Reserve` and `Descent` in full; the `Flow`, `Dissipation` and `Roles` module docs and the declarations P16c and P17 added; the `Correspondence` and `Metaethics` definitions that `Descent` uses (`Bearing`, `Interacts`, `interaction`, `Valuation`, `relations`, `Connected`, `transmits`, `significant_iff`).
- The JSON of the two new records and of the five records P16c corrected; the fields changed in the other 13 records.
- The chapter lines listed above, the root module doc, the checker's scope text for `Reserve` and `Descent`, and the plan rows 148–159.

**Ren's words read**, for provenance: [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) (`740126fcca587edb`). The study and the two new records quote its line 12 exactly ("生生不息 - 一种整体的，不断创造更多生的方向").

**No external literature was read.** Seeds, foxes, larders and lineages are kinds of cases, not evidence.

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order.

- **Core.** The following 24 modules exit 0 from the prelude with no warnings:
  - `GenerativeCore`, with `import Std` removed as the checker does;
  - `InquirySufficiency` and `RelationalRenewal`;
  - `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Population, Identity, Wholes, Dissipation, Roles, Reserve, Metaethics, Ranking, Correspondence, Descent}`;
  - the root module `Becoming`.
- **Bridge and periphery.** Not rebuilt (see "Not checked"). `Becoming.Bridge` is unchanged in `b24963f1..badb652e`, and its bytes match the receipt.

The checks:

- **Receipt.**
  - Status `passed`, Lean 4.29.1 `f72c35b3`, `core_compiles_from_prelude: true`, and `core_closure` of 24 modules.
  - All 37 `source_sha256` entries equal the object's files, and the checker hash equals `check_becoming.py`.
  - The 221 artifacts of the retained run `becoming-checks/20261009T091503.719598Z` match their recorded hashes.
- **Counts.**
  - Theorems per module: Frame 11, Inquiry 6, Renewal 6, Dependence 53, Return 29, Horizon 14, Joint 21, Substitution 7, Generation 30, Flow 64, Population 36, Identity 83, Wholes 36, Dissipation 77, Roles 133, Reserve 35, Metaethics 35, Ranking 27, Correspondence 37, Descent 25 and Bridge 34, for 799 in all.
  - The 22 spine modules have 1236 declarations; Bridge's 50 make 1286.
  - Across the three commits:
    - P16c adds 52 theorems: Dissipation +17, Roles +21, Wholes +10 and Identity +4 (728 / 1182, closure 22, package 20).
    - P17 adds 46: `Reserve` 35, Flow +4 (one moved from Dissipation), Dissipation +6 −1 and Roles +2 (774 / 1257, closure 23, package 21).
    - P18 adds `Descent`, with 25 theorems and 29 declarations (799 / 1286, closure 24, package 22).
  - The study, the records and the chapter's §9 table agree.
- **Records.**
  - The 20 records changed in `b24963f1..badb652e` have 247 `references` hashes, and all equal the object's files.
  - All 57 proof bindings carry `success_value` and `sha256_pointer`, resolved in their receipts, that equal the bound sources.
  - Review stamps: see L3(f).
- **Names.**
  - `Aliases.lean` (`aa41994a63ff75c7…`) runs `#check @` on all 398 aliases of the 20 records. 367 resolve in the core; the other 31 are 26 `Becoming.Bridge` names and the five `CorrectionInquiry` aliases of the Mathlib periphery.
  - `Names.lean` (`98dc397a7785e83f…`) does the same for the 1128 qualified declaration names in the `references`. 1061 resolve; the 67 that do not are 37 bridge, 19 inherited and 11 periphery declarations. None is a core declaration.
  - Every P16c, P17 and P18 declaration resolves.
- **Axioms.**
  - `CoreAudit.lean` (`a4f7e6ab9f7130d9…`, 1356 lines generated from the receipt) prints the axioms of every source declaration of the 24-module closure. All 1356 report "does not depend on any axioms".
  - `EnvAudit.lean` (`c51e1ba61ff5be9a…`) enumerates every constant of the closure, including compiler-generated ones, with `Lean.collectAxioms`. Of 3963 constants, 29 depend on `propext`; all 29 are generated `injEq` lemmas (L3(b)). `Reserve` (138 constants) and `Descent` (43) have none.
  - `ProbeAudit.lean` (`b0ccb4f2cf2c34e3…`) prints the axioms of all 77 probe declarations, and `ProbeEnvAudit.lean` (`be6280c196841fff…`) enumerates all 191 constants of the two probe modules. All are axiom-free.

**Probes.** Two files import the unchanged `Becoming` and compile with exit 0 and no warnings:

| File | sha256 prefix | Theorems | Defs / inductives |
|---|---|---|---|
| `P17Probes.lean` | `c261e2cb0bc5e104` | 18 | 10 / 2 |
| `P18Probes.lean` | `8ac45e45828b60b4` | 36 | 9 / 2 |

The probes use term mode only: no tactic, no `simp`, `omega` or `decide`.

- As noted in the seventh review, overlapping wildcard patterns in a function-defining `match` and `Nat.succ_ne_zero` report `propext` in Lean 4.29.1. The probes list every case and use `Nat.noConfusion` and constructor `noConfusion`.
- The probes are minimal models that satisfy the published definitions unchanged, or theorems over those definitions.
- Following the nondual method, they show what the definitions admit, not what actual systems do. A probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels** (as in the seventh review).

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose is stronger than the Lean, including where a premise is left out.
- *missing counterexample*: a relevant witness is absent or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

Of the three *errors*, one (L10) is a definition that admits what its prose excludes, and two (L5, L9) are false claims in prose about a definition. No Lean statement is wrong.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P16c: are K1–K8 handled? | **Yes, with residues.** `Around`, `Inward`, `dissipatesOn_of_inward`, `taking_draws_in`, `generation_draws_in` and `Enclosed.around` are in the core, and every record title now states the literal conclusion plus inflow where the family is enclosed around. The module title of `Dissipation`, two `related` entries and several "life" phrasings were missed. | L1, L2, L3 |
| 2. P16c: are the new core declarations correct? | **Yes.** `Enclosed.around` (decidable equality, via `adjoin`) is the step the seventh review left unbuilt. `Covered.*`, `Whole.covered`, `needs_new`, `whole_self`, `each_other`, `Layered.brief/within/arise_again`, `Merge.idle`, `Confluence`, `EmbodiedSun`, `SprayHanding`, `Kindling.around/draws_in`, `Frontier.enclosed/around/draws_in/gives_without_taking` and `Lone.enclosed/draws_in/repeated_family` hold as glossed. | — |
| 3. P17: is `Carries` a relaxation of `Dependent`? | **Yes, exactly.** `carries_zero` is an equivalence, and `Carries.pos` is what the relaxation adds. | — |
| 4. P17: do the bounds hold and are they attained? | **Yes.** `lasts` needs decidable activity, disclosed. `ends_within` needs `Decays`, disclosed, and `Seed.not_decays` shows `Carries` does not give it. `Seed` (2 wakings for a reserve of 2), `Viable` (inactive from step 3) and `Famine` (2 extra steps for 2 units of fat) attain the bounds. | — |
| 5. P17: is "a reserve is a held condition" right? | **Only as "can be".** `carries_of_held` gives one direction. `Seed` and `Viable` are carried by supplied reserves that no held condition can carry (`seed_no_held`, `viable_no_held`). The gloss of its premise also misstates who takes (`Larder`). | L4, L5 |
| 6. P17: is `Famine.transformed_dependent` "the same unfolding"? | **The same levels, activity, drawing and flow, but not the same `living`.** The fox's event at step one undermines under the published reading and not under the transformed one. The general construction holds with decidable support (`redirect_dependent`). | L6 |
| 7. P17: are the `ComesToStand` theorems correct, and do the Roles statements survive? | **Yes.** The nine embodied theorems keep their statements (their source statements are identical at `eb700342` and `badb652e`). What the proofs use is a rise, which P11's `renewedBy` already gives; the start from zero only adds the bound `given ≥ new standing`. | L7 |
| 8. P17: `came_to_stand`, `Provisioned`, `Sleeper` | **Correct.** `came_to_stand` uses only "stands while active". `Provisioned` is genuine. `Sleeper`'s vacuous dissipation is disclosed in rebuttal 6. | L3(c) |
| 9. P18: does living on reintroduce P9's free connection? | **No.** It needs an actual drawing and a dependence at a positive need, the discipline of interaction. But the stated form of that discipline ("only on an embodied relatum active at that step") drops `LivesOn.active`'s premise (`Drowsy`). | L8, L9 |
| 10. P18: does descent reintroduce P9's free connection? | **Yes, through givers that do not take part.** `Descends` reads `give` for formations outside `present`, which nothing constrains (`Stranger`, `brood_descends_from_any`). Requiring the giver to take part removes this and keeps every published result (`DescendsIn`). | L10 |
| 11. P18: is "descent relates every event" disclosed? | **Yes**, in the module doc, the table, the record's boundary and rebuttal 2. Rebuttal 2's example of a local reading ("第 0 代在第 5 步的事件就孤立了") depends on L10: with the present `Descends`, generation 0 "gives" to generation 6 at step 5. | L10 |
| 12. P18: are `Brood.descended` and `relabel_sustenance` genuine? | **Yes.** `relabel_sustenance` shows that the identification enters living on. `Brood.descended` holds, and its connection survives the correction of L10 (`brood_descentIn_connected`); as published, every generation descends from every number. | L10 |
| 13. Nondual method; Ren's choices; vocabulary | **No reading is chosen for Ren in P17 or P18, and adoption of the two relations is left to Ren.** The K6 residues read embodiment as life. "给予者" survives in four places. | L1, L3 |
| 14. Records, receipt and counts | **Correct** (799 / 1286, run `20261009T091503.719598Z`, closure 24, package 22), with bookkeeping in L3. | L3 |

**Status of K1–K8.**

| Item | Status | Evidence |
|---|---|---|
| K1 | closed, with a residue | `Around`, `Inward`, `dissipatesOn_of_inward`, `taking_draws_in`, `generation_draws_in` and `Enclosed.around` are in the core; `SprayHanding` is in `Roles` and the records; the titles of generation-is-replenishment and no-finite-part-bears-taking, hypothesis 3, §17, §20, the chapter, the root doc and the checker scope state the literal conclusion. The `Dissipation` module title (line 5) still reads "recurring taking draws in from beyond the family" (L2). |
| K2 | closed | "被耗散的家族 / dissipated on" is restored in §20, the English P15 paragraph and chapter §2; `Frontier.gives_without_taking` is in the core. |
| K3 | closed, with a residue | `Covered`, `Whole.covered`, `needs_new`, `whole_self` and `each_other` are in the core; "就是" became "经由". whole-persists-through-generation's `related` entry for theory-of-becoming-foundation still says "由……构成 / is made of" (L2). |
| K4 | closed, with residues | Record title, chapter §1, §9, glossary, Wholes title and root doc name `Listed`. Two `related` entries still say "部分不长久 / parts that do not last" (L2). |
| K5 | closed | §21 rebuttal 3 is rewritten; `Layered.brief`, `within` and `arise_again` are in `Wholes`. |
| K6 | closed where located, with residues | §22.1 J7, §22.3 item 4, the record and the `SunSeed` docstring are corrected, and `EmbodiedSun` is in `Roles`. "Life" for embodied relata survives in `Roles` headings, chapter, §18, §23.4 and the English summary (L1). |
| K7 | closed | `Merge.idle` and `Confluence` are in `Identity`; the `merging` docstring, the Identity doc, §22 and the record are corrected. |
| K8 | five closed; (c), (g) and (h) recur | (a) §20's introduction is corrected; "付出" remains only in quoted originals and in §15's P11b handling text, outside K8's scope. (b) The plan's P15 row is corrected. (c) "给予者" survives in §22 (lines 1285, 1320) and the plan (lines 148, 152) (L3(a)). (d) is corrected in the `Dissipation` doc, and (e) there, in §22's Delta (line 1293) and in §22.2 (line 1331). (f) `Frontier.enclosed` and `Lone.enclosed` are in the core. (g) The stamps were refreshed at P16c, but the pattern recurs in P17 and P18 (L3(f)). (h) The P15 and P16 paragraphs are corrected; the P16b paragraph is not (L3(e)). |

## 2. Findings

### L1. overclaim (a reading chosen for Ren): embodied relata are still called lives

**Location.**

- `Roles.lean:38` (module doc bullet), `:407` (section heading) and `:445` (the `Embodied.active_of_bearing` docstring): "Life as a condition of life. Under `Dependent`, a formation depending on an embodied relatum at a positive need is active only while that relatum is".
- Study §23.4 rebuttal 4 (line 1457), written in P16c: "它说的是关系项作为条件而在的结构：生命以其他生命为条件（`active_of_bearing`、`coextinct`）". The next sentence says that which embodied relata are lives is Ren's reading.
- Study §18 (line 1049), in the P16b correction that P16c kept: "所以它说的是一个生命的生起由另一个活跃者的给予给出".
- Study §18 (line 1051) and chapter §2 zh (line 203): "在承担自身的生命终结之步汲取它"; chapter en (line 205): "Drawing on a life that bears on itself, across the step at which it ends". The chapter's §8 row (line 431) lists Ren's choice as "在承担自身的生命终结之步的汲取是否计入不 living".
- Chapter §2 zh (line 203): "作者把这读作原话中两个“生”之间关系的一种形式内容，一个生命的生起由另一个生命的活动给出（AI 论证）". The English (line 205) has no counterpart, so the two texts differ.
- English P14 paragraph (line 1706) and P16c paragraph (line 1720): "that formation need not be a life", "which need not be a life (`SunSeed`)".
- Record life-as-condition-of-life, title: "生作为生的条件 / life as a condition of life".

**What the Lean says.** `active_of_bearing`, `coextinct`, `ending_breaks` and `arises_given` are stated for `Embodied` relata: `∀ t, active t x ↔ 0 < level t x`. `EmbodiedSun` shows that a sun given a level of one, depending on and drawing on nothing, is embodied.

**Why it matters.**

- K6 found that "being embodied" had been read as "being a life", and P16c's §23.1 accepts the correction: "体现是作为条件而在的表示，不是是生命的表示；把体现的关系项读作“生”是 AI 读法，属于 Ren".
- The places above still name embodied relata "life / 生命" in theorem docstrings, in the chapter's statement of a theorem and in the list of Ren's open choices. There the reading is presented as already made.
- "Life as a condition of life" is the fourth review's name (H14) for what the two-kind representation omitted. As a name for the target it is fine. Attached to `active_of_bearing`, it says that the theorem is about lives.

**Correction.**

- In `Roles`: "An embodied relatum as a condition" for the headings and the docstring.
- In the chapter, §8, §18 and the English: "承担自身的体现关系项 / an embodied relatum that bears on itself"; "need not be embodied" for "need not be a life".
- In §23.4 rebuttal 4: "依存于体现关系项的形成只在它活跃时活跃".
- Delete the zh sentence in chapter §2, or give it in both languages with the same label.
- The record title can keep H14's phrase as the name of what it answers: "回答‘生作为生的条件’：形成与条件是一个关系项的两种角色……".

### L2. overclaim (omitted premise): residues of K1, K3 and K4

**Location and evidence.**

- `Dissipation.lean:5`, the module title: "Dissipation: recurring taking draws in from beyond the family". The body (lines 45–53), both record titles, the chapter and the root doc say "enclosed around". `SprayHanding.taking_opens_anyway` refutes the title as written: taking recurs in the sides' family, and nothing flows in.
- whole-persists-through-generation, `related` entry for theory-of-becoming-foundation (JSON lines 122–123): zh "持续的整体由不长久的部分的不息生成构成", en "a persisting whole is made of the unceasing generation of parts that do not last". This repeats K3 ("构成 / made of"; `Gaps` refutes the identity) and K4 (no `Listed`; `Countless` refutes it).
- identity-across-steps, `related` entry for whole-persists-through-generation (JSON lines 162–163): zh "部分不长久时，整体的持续需要部分不断生起", en "where parts do not last a whole's persistence needs its parts to keep arising". `Countless` refutes it.

**Correction.**

- Title: "Dissipation: recurring taking opens finite families and, enclosed around, draws in".
- The two `related` entries in the form of the record title: "部分短暂，或部分终结且同时活跃的部分有限时，整体经由部分的生成而持续 / where parts are brief, or end with finitely many active at once, a whole persists through the generation of its parts".

### L3. presentation: bookkeeping and vocabulary

- **(a) "给予者" in current text.** K8(c) changed the current text of §17–§22, the records and the plan. Four places were missed:
  - study §22 introduction (line 1285): "有限支撑下给予者取得多于所给（J1）";
  - §22.1, J7 handling column (line 1320): "给予者也体现";
  - plan P11 row (line 148): "每次上升由给予者造成", "需要给予者没有最终的界";
  - plan P14 row (line 152): "给予者不必体现".

  Quoted originals in correction markers are fine. The vocabulary is Ren's to decide; this is consistency only.
- **(b) "Every declaration has an empty axiom report".**
  - The claim appears in root `Becoming.lean:125`, `check_becoming.py:11`, the chapter's §9 (line 472) and the validation scopes of the 20 records ("every declaration in it has an empty axiom report").
  - The checker audits the 1356 source declarations of the closure, and all are empty.
  - The closure's environment has 3963 constants. 29 of them, compiler-generated `injEq` lemmas in 14 modules, depend on `propext`. Examples: `Becoming.Web.mk.injEq`, `Becoming.Flow.mk.injEq` and `Becoming.Valuation.mk.injEq`, and P16c's `Becoming.Confluence.Formation.new.injEq` and `Becoming.SprayHanding.Relatum.side.injEq`.
  - No source declaration uses them, and `Reserve` and `Descent` have none.
  - Correction: "every source declaration", or audit the generated lemmas and name the exception.
- **(c) Order.** §24's author's counterreview runs 1, 2, 3, 4, 6, 5 (lines 1525–1535).
- **(d) "Draws".**
  - The English P17 paragraph (line 1742) says "Dormancy itself draws nothing under `Carries`". The record's English limitation says "under Carries dormancy does not draw the reserve".
  - "Draw" is a defined term (`Web.draws`). The Chinese says "休眠不耗用储备". Use "uses no reserve".
- **(e) "Core".** The English P16b paragraph (line 1724) says "The core now has 676 theorems and 1115 declaration audits over a closure of 22 modules (a package of 20)". This is K8(h)'s pattern one paragraph later; 676 counts the package.
- **(f) Stamps.**
  - The seventh review's K8(g) treated a review stamp earlier than the run a record's validation scope cites as stale.
  - By that standard, 19 of the 20 records changed in these phases are stale. All cite `20261009T091503.719598Z` (09:15:03Z); only living-on-and-descent (09:19:57Z) is later.
  - Two of them also changed content without a new stamp. becoming-dependence-dynamics (00:55:55Z) changed `limitations` and `next_delta` in P17. life-as-condition-of-life (08:40:51Z) changed `limitations` and `next_delta` in P17, and `next_delta` and `related` in P18.
  - The convention in use appears to be that only changes to a claim refresh the stamp. Either state that convention in the result workflow or refresh the stamps of records whose limitations or next steps changed.

### L4. overclaim: "a reserve is a held condition"

**Location.**

- `Reserve.lean:17` (bullet "A reserve is a held condition") and `:193` (section heading).
- Root `Becoming.lean:97`: "`Dependent` is exactly the zero reserve, and a reserve is a held condition".
- Package `README.md:39`: "储备是所持的条件".
- Study §24:
  - introduction (line 1463): "按非二元方法，储备不作为新的原语：它是形成所持的一个条件的水平";
  - Delta (line 1471): "储备是所持条件的水平（Flow.carries_of_held）";
  - bullet (line 1517): "储备是所持的条件 … 滞后就是依存转化到所持的条件上 … 缓冲不在依存之外";
  - English (line 1740): "A reserve is a held condition".
- Record reserve-defers-ending:
  - title: "Dependent 是零储备，储备是所持的条件 / … and a reserve is a held condition";
  - claim: "储备是所持的条件 / A reserve is a held condition";
  - correspondence: "储备不是新的原语：它是形成所持的一个条件的水平 / a reserve is not a new primitive: it is the standing of a condition the formation holds".
- Chapter §9 Reserve row (line 465): "储备是所持的条件".
- The chapter's §1 bullets (lines 130, 141) and glossary (line 522) say "可以就是／可以是 / can be", which is accurate.

**What the Lean says.**

- `Web.Carries r` holds of any `r : Nat → F → Nat` satisfying two inequalities at unsupported steps.
- `Flow.carries_of_held` gives one direction: under its premises, the level of a held condition is a reserve.
- No theorem gives the converse.

**Evidence.** `seed_no_held` and `viable_no_held`.

- `Seed` and `Viable` are the module's own witnesses for `lasts` and `ends_within`. Their reserves are supplied functions (2, 2, 1, 1, 0 and 3, 2, 1, 0).
- Every level of their webs is zero.
- No held condition carries the seed: at the active unsupported step (step one, resp. two), `Carries.pos` would make the held condition's level positive.

**Why it matters.**

- The nondual reading is that a reserve "is not a new primitive". That holds where a flow and a held condition are represented, as in `Famine`.
- Where they are not, `Carries` is a supplied amount. The record's hypothesis 1 says exactly this ("Carries 与 Dependent 一样是表示前提：哪个量承载一个形成……由应用给出").
- The dormancy bounds the study draws from `Seed` and `Viable` are bounds on such a supplied amount.
- "滞后就是依存转化到所持的条件上" fails for `Seed`: its web has no condition onto which a dependence at need one could be moved.

**Correction.** "A reserve can be a held condition (`carries_of_held`); where no held condition is represented, the reserve is supplied (`Seed`, `Viable`)." Apply it to the title, the module bullet and heading, the root doc, the README, the study's introduction, Delta and bullet, the record's claim and correspondence, and the §9 row. "Lag is dependence transformed onto what is held" then reads "where a held condition carries it".

### L5. error (in prose): who takes from the held condition

**Location.**

- `Reserve.lean:17–19` and the `carries_of_held` docstring (lines 199–201): "that its holder takes from while active there".
- Study §24 table (line 1497): "活跃时被它取用"; English (line 1740): "that the holder takes from while active there".
- Record reserve-defers-ending: hypothesis 3, zh "持有者在不被支持而活跃的步上从中取用", en "the holder takes from it at each unsupported active step"; claim (en) "which its holder takes from when active there".
- The study's bullet (line 1517, "在持有者活跃时被取用") and `check_becoming.py:255` ("taken from while the holder is active there") are accurate.

**What the Lean says.** `drawn : ∀ t f, ¬ W.Supported t f → W.active t f → 0 < L.taken t (hold f)`. Here `L.taken t c` is the total taken from `c` by all formations taking part.

**Evidence.** `Larder.larder`.

- A fox depends at need one on a hare that is gone, and draws on nothing. A crow, which depends on nothing, eats one unit of fat across steps zero and one. Only the crow takes part.
- The flow balances, nothing gives, and the fox is active and unsupported at steps zero and one.
- Every premise of `carries_of_held` holds with `hold fox = fat`. The fat "carries" the fox, though the fox takes no part (`fox_absent`) and takes nothing.

**Why it matters.**

- The study and the record read the theorem as a fox burning its own fat.
- The theorem also covers a stock that others deplete while the holder is active. There the "reserve" is not the holder's use of what it holds, and "滞后就是依存转化到所持的条件上" has no holder's use to rest on.
- The bound remains true; only the reading changes.

**Correction.** Either gloss the premise as "taken from (by whatever takes part) while the holder is active and unsupported", or strengthen `drawn` to `f ∈ L.present t ∧ 0 < L.take t f (hold f)`. `carries_of_own` derives the stronger form from `carries_of_held` in two lines, and `Famine` meets it.

### L6. missing counterexample: the transformed reading changes which events are living

**Location.**

- `Reserve.lean:20–23` and the `Famine.transformed_dependent` docstring (line 469): "Read so, activity needs support: the fox's lag is its dependence transformed onto the condition it holds".
- Study §24 bullet (line 1517): "所以同一展开有两种表示……滞后就是依存转化到所持的条件上".
- Rebuttal 2 (line 1527): "两种表示描述同一展开：水平、活动、汲取与流都相同，只是依存于什么不同……哪一种更合适，取决于应用把脂肪读作狐的一部分还是狐所依存的另一个条件。一般地构造转化的读法需要“是否被支持”可判定，这里只给出见证".
- Record reserve-defers-ending: claim, correspondence, limitations ("一般地构造……没有给出，只有见证") and next_delta.
- Chapter §8 row (line 429): "一般地构造依存转化到所持条件上的读法" as an open item.

**What the Lean says.** `Famine.transformed` changes `requires` only. In the stepwise reading, `living` is `active ∧ ¬ UnderminingAt`, and `UnderminingOn` reads `requires`.

**Evidence.**

- `famine_living_differs`: the fox is active at step one under both readings.
  - Under `Famine.web` its event there is undermining (`famine_undermines_one`). It draws on the hare, whose dependence it met at need one at step zero, and the hare is below need after the step.
  - Under `Famine.transformed` it is not undermining (`famine_transformed_not_undermining_one`). It depends on the fat, which stands at one after the step and meets the need.
  - So the fox's event at step one is living under the transformed reading and not under the published one.
- `redirect_dependent`, the general construction:
  - with decidable support, move each unsupported formation's dependence onto its held condition at need one;
  - if the held condition carries the formation, the redirected web is `Dependent`;
  - levels, activity and drawing are unchanged (`redirect_same`).

**Why it matters.**

- The study presents the choice between the two readings as which condition the application takes the fat to be. The choice also changes `living`, the object of G0 in the stepwise reading, so it is not neutral for the valuation.
- The redirect is available wherever a held condition carries the formation. So its being `Dependent` adds nothing to `Carries.pos`. "Lag is dependence transformed" re-describes the reserve; it is not a further fact about the unfolding. This is the pattern of the seventh review's K7, a re-reading presented as content.

**Correction.**

- State in §24 and the record that the two readings differ in `living` (the fox's event at step one).
- Record the general construction as available with decidable support, and its `Dependent` as holding by construction.
- List the choice of reading, where it changes `living`, among the correspondence premises that bear on the valuation.

### L7. presentation (scope): what the requirement uses is a rise, not the start from zero

**Location.**

- Study §24 bullet (line 1519): "§20 与 §23 用到的体现只有一点：生起时水平从零上升".
- Rebuttal 4 (line 1531): "§20 与 §23 的结论用到的不是体现，而是水平从零上升".
- `Flow.lean:378`, the `standing_needs_replenishment` docstring: "Coming to stand carries the requirement itself".

**What the Lean says.**

- `standing_replenishes`, `standing_lowers_on` and the theorems built on them use `comes` only through `0 < L.given t c`.
- In a balanced flow any rise gives that. P11's `Balances.renewedBy` already states that every rise is given to by an active formation.
- What the start from zero adds is the bound `level (t + 1) c ≤ given t c` in `standing_given`, which no conclusion uses beyond its positivity.

**Evidence.**

- `rise_given`: in a balanced flow every rise is given to, without `Acting`.
- `comes_rises`: coming to stand is a rise.
- `rise_lowers_on`: `standing_lowers_on` for any rise.
- `Growing`: a balanced flow in which a condition rises at every step and never comes to stand, and is given to at every step.

**Why it matters.**

- "从零上升" locates the requirement more narrowly than the proofs do. The root doc's "where standing rises, not where activity does" is the accurate form.
- The conclusions about `Sleeper` and `Provisioned` are unaffected: waking without any rise of level needs nothing given.

**Correction.** "用到的是水平跨生起之步上升（体现时从零上升）". Optionally state the dissipation theorems for `Rises`, with `ComesToStand` as the case from zero.

### L8. overclaim (omitted premise): `LivesOn.active` assumes embodiment

**Location.**

- `Descent.lean:18–20` (module doc) and `:79–80` (docstring): "Like interaction, this is not free: under `Dependent` an active formation lives only on an embodied relatum active at that step".
- Study §25 table (line 1567) and bullet (line 1579): "在 `Dependent` 之下，只能以在该步活跃的体现关系项为生（`LivesOn.active`）".
- Record living-on-and-descent claim: zh "在 Dependent 之下，活跃的形成只以在该步活跃的体现关系项为生", en "under Dependent an active formation lives only on an embodied relatum active at that step".
- Chapter §2 bullet (line 339): "以之为生与交互一样不免费：在 `Dependent` 之下只能以在该步活跃的体现关系项为生".
- English P18 paragraph (line 1753) and `check_becoming.py:326–327`.

**What the Lean says.** `LivesOn.active (dependent) (lives) (embodied : W.Embodied e'.1) (active) : W.active e.2 e'.1`. That the lived-on relatum is embodied is a hypothesis.

**Evidence.** `Drowsy.drowsy`.

- A sleeper stands at one at every step and is awake at odd steps. An eater is always active, draws on the sleeper and depends on it at need one. `Dependent` holds.
- At step zero the eater lives on the sleeper. The sleeper is not embodied (it stands while dormant) and is not active at step zero.
- `sustenance` connects the web, and `interaction` does not: interaction relates only the eater's events.

What `Dependent` does give without embodiment is `LivesOn.stands`: the lived-on relatum stands at that step at a positive level.

**Why it matters.**

- The sentence is the stated reason that living on is "not free".
- The discipline that holds is that of interaction: an actual drawing and a dependence that can fail. That suffices for the point of P9, and it is what `Drowsy` meets.
- "Only on an embodied relatum active at that step" is not part of it, and the theorem cited for it needs a premise the sentence omits.

**Correction.** "在 `Dependent` 之下，所依的关系项在该步以正的水平作为条件而在（`LivesOn.stands`）；它体现时，它在该步活跃（`LivesOn.active`）."

### L9. error (in prose): "embodiment enters the valuation"

**Location.**

- Study §25 (line 1578): "§22 J4 写明同一对应是表示的前提，J5 写明体现不进入两种估值；这里体现第一次进入估值，正是经由这一对应".
- Record living-on-and-descent:
  - correspondence (JSON line 32) and the dependency on life-as-condition-of-life (line 80): "回答其下一步“直接读出体现的估值” / answers its next step ‘a valuation reading embodiment directly’";
  - history (lines 343–344).
- Record life-as-condition-of-life, `next_delta`: "直接读出体现的估值已有两种候选读法".

**What the Lean says.**

- Neither `Web.sustenance` nor `Flow.descent` mentions `Embodied`.
- `Embodied` enters only as a hypothesis of `Embodied.descends`, `arisen_reached` and `LivesOn.active`.

**Evidence.** In `Drowsy`, `sustenance` relates and connects a relatum that is not embodied.

**Why it matters.**

- What enters the valuation is the one-kind identification, that a condition is a relatum, as `relabel_sustenance` shows.
- Embodiment stays outside, as §22 J5 and the chapter's glossary (line 518, "体现本身不进入两种估值") say of the earlier valuations.
- P14's next step asked for a valuation relating a drawer to "the embodied relatum it draws on". `sustenance` relates a drawer to any relatum it draws on at a positive need, embodied or not.

**Correction.** "这里一类读法的同一对应第一次进入估值；`sustenance` 与 `descent` 的定义不含体现". In the records, say that the next step is answered in a broader form.

### L10. error (definition): `Flow.Descends` admits a giver that does not take part

**Location.**

- The definition, `Descent.lean:109–110`: `Descends x g := ∃ t, 0 < L.give t g x ∧ W.ComesToStand t x`.
- Study §25 bullet (line 1579): "世系要求正的给予与开始作为条件而在，空的给予不造成它。所以 §10（P9）排除的免费连通没有回来".
- Rebuttal 1 (line 1586): "世系要求实际的给予与开始作为条件而在".
- Rebuttal 2 (line 1588): "只把给予的那一步与生起者相关，会使父代的其他事件与后代无关（`Brood` 中第 0 代在第 5 步的事件就孤立了）".
- Record living-on-and-descent:
  - correspondence: "世系要求正的给予与开始作为条件而在，所以不由空的给予造成 / descent requires a positive gift and coming to stand, so no empty giving makes it";
  - dependency interface: "a positive gift and coming to stand".

**What the Lean says.**

- `L.given t c` sums `L.give t f c` over `f ∈ L.present t` only.
- `Balances` constrains `given` and `taken`. `Acting` and `Taking` constrain only formations in `present`.
- So `L.give t g x` for `g ∉ L.present t` is unconstrained and enters no level. `Descends` reads it.

**Evidence.**

- `Stranger.stranger`. One web, with a parent, a seed and a stranger; nothing depends on or draws on anything.
  - Two flows, `honest` and `nominal`, have the same formation taking part (the parent) and the same `given` for every condition at every step (`same_given`). Both balance and both are `Acting`.
  - They differ only in `nominal`'s positive `give` entry from the stranger to the seed across step zero. The stranger never takes part (`absent`).
  - `nominal.Descends web .seed .stranger` holds. Descent connects `nominal` (`nominal_connected`) and does not connect `honest` (`honest_not_connected`): in `honest` the stranger's events are related to nothing.
- `brood_descends_from_any`. `Brood.flow.give t _ x := birth x t` ignores the giver, so generation `t + 1` descends from every number `g`. `brood_examples`:
  - generation 1 descends from generation 7, which neither takes part at step zero nor stands there;
  - generation 6 descends from generation 0 across step five.
- So rebuttal 2's example fails for a local reading built on the present definition: generation 0's event at step five "gives" to generation 6.

**Why it matters.**

- This is the free connection that P9's discipline excluded. It re-enters through a component of the representation that nothing constrains.
- Under N_rel for `descent`, valuing any event of the stranger reaches every living event of the seed, and conversely (`descent_reaches`, `ancestry_reaches`), though nothing the stranger does enters any level.
- None of the published positive results needs it.

**Correction.** Require the giver to take part:

```lean
def DescendsIn (L : Flow X X) (W : Web X X) (x g : X) : Prop :=
  ∃ t, g ∈ L.present t ∧ 0 < L.give t g x ∧ W.ComesToStand t x
```

Formalized here:

- `Embodied.descendsIn` restates `Embodied.descends` for `DescendsIn`. `arises_given` already supplies the membership.
- `brood_descendsIn` and `provisioned_descendsIn` restate `Brood.descends` and `Provisioned.descends`.
- `brood_descentIn_connected`: `Brood.descended`'s connection survives.
- The spurious descents vanish: `brood_not_descendsIn` (generation 1 from 7) and `stranger_not_descendsIn`.

Even with presence required, `Descends` counts gross giving. Whether a gift taken back across the same step should count is a further correspondence choice, not probed here.

## 3. What remains sound

- **The theorems.**
  - Every P16c, P17 and P18 theorem holds as stated.
  - The 24-module core recompiles from the prelude, and all 1356 source declarations have empty axiom reports.
  - The counts, receipt, source hashes, retained artifacts, reference hashes, aliases and bindings are correct.
- **P16c.**
  - Every K1–K8 item is addressed at the located places, and the probes became core theorems.
  - `Enclosed.around` closes the step the seventh review left unbuilt, so drawing in needs nothing beyond finitely many conditions per step once equality is decidable.
  - The corrections are made in place and marked, with the original wording kept.
- **P17.**
  - `carries_zero` makes "`Dependent` is the zero reserve" an exact equivalence; relaxing `Dependent` is shown to mean a positive reserve.
  - `lasts`, `lasts_within`, `active_finitely`, `arising_finitely`, `decays_by`, `ends_within`, `consumed_lasts` and `coextinct_lasts` are correct. Their premises (decidable activity, `Decays`) are disclosed, and `Seed.not_decays` shows that `Carries` does not give `Decays`.
  - `Seed`, `Viable` and `Famine` attain the bounds. `Famine`'s fat is a genuine held condition in a balanced flow, and the fox takes from it.
  - `came_to_stand`, `Provisioned` and `Sleeper` are correct. `Provisioned` separates coming to stand from arising, and rebuttal 6 discloses that `Sleeper`'s dissipation is vacuous.
  - The nine embodied theorems of `Roles` are re-derived through `ComesToStand` with their statements unchanged.
  - The boundary is honest: the conclusions bind a formation unsupported from some step on, not whether support returns.
- **P18.**
  - `living_on_reaches`, `lived_on_reaches`, `descent_reaches`, `ancestry_reaches`, `Embodied.descends` and `arisen_reached` are correct instances of N_rel.
  - `Mutualism.apart_sustenance_connected` and `relabel_sustenance` are genuine: the identification enters living on, and co-participation and interaction do not see it.
  - `Brood.descended` holds, and its connection survives requiring the giver to take part.
  - `Provisioned.descends` and `Sleeper.no_descent` correctly place descent at coming to stand.
  - Living on keeps the discipline of interaction: idle relata cannot be lived on, and connection needs an actual drawing and a dependence that can fail.
  - That descent relates whole relata is disclosed, and the choice to adopt either relation is left to Ren.
- **Method and provenance.**
  - Ren's words are quoted exactly, and AI readings are labelled.
  - `living` and C are unchanged, and nothing is said to make bringing about new arising better.
  - No ethical predicate, ranking or axiom enters.

## 4. What would change these verdicts

1. **Descent (L10).** Require the giver to take part in `Descends` (as `DescendsIn`), restate `Embodied.descends`, `Brood.descends` and `Provisioned.descends`, and restate "no empty giving makes it" and rebuttal 2. Alternatively, keep the definition and state that a non-participating `give` entry makes descent, with `Stranger` as the witness.
2. **Living on (L8, L9).** State `LivesOn.stands` as what `Dependent` gives, keep `LivesOn.active` with its premise in every gloss, and replace "体现第一次进入估值" with the identification.
3. **Reserve (L4–L6).**
   - Write "can be a held condition", with `Seed` and `Viable` as supplied reserves.
   - Correct the gloss of `drawn`, or strengthen it to the holder's own take.
   - State that the transformed reading changes `living` at the fox's step one, and record the general construction.
4. **Rise (L7).** Say "the level rises (from zero, for coming to stand)".
5. **Residues (L1–L3).** The "life" phrasings, the `Dissipation` title, the two `related` entries and the six bookkeeping items.
6. **Ren's choices.** These stay open and are not settled here:
   - whether living on and descent count as formed relations for N_rel;
   - the reading of 生 and of living, including whether embodied relata are 生;
   - the reading of succession and the level at which 生生不息 is read;
   - whether drawing at an ending counts, and for which drawers;
   - the names, including the giving vocabulary.
7. A finding would also fall if its probe misread a published definition. Every probe imports the unchanged `Becoming`, and each uses the definitions as they stand at `badb652e`.

**Not checked.**

- `Becoming.Bridge` and the Mathlib periphery were not rebuilt. The bridge is unchanged since `b24963f1`, and its bytes match the receipt. Its 26 aliases and the five periphery aliases did not resolve here, nor did 67 declaration names (37 bridge, 19 inherited, 11 periphery).
- The generated overview pages and `make research-check` were not run, since they write into the live repository.
- No external literature was consulted.
- Parity between the Chinese and English texts was checked only for the passages quoted above.
- The following were not built:
  - lagged coextinction along chains of dependence with reserves (open in the repository);
  - a net-giving form of descent;
  - the dissipation theorems of P17 restated for every `Rises` (only `rise_lowers_on` is built).

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 against the unchanged `badb652e` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. The two probe files compile with exit 0 and no warnings.

- `ProbeAudit.lean` prints the axioms of all 77 probe declarations (`#print axioms`, one line each, generated from the two files). Every one reports "does not depend on any axioms".
- `ProbeEnvAudit.lean` enumerates every constant of the two probe modules, including compiler-generated ones, with `Lean.collectAxioms`. The output: `P17Probes: 76 constants, 0 with axioms`; `P18Probes: 115 constants, 0 with axioms`.
- `CoreAudit.lean` (1356 `#print axioms` lines generated from the receipt), `Aliases.lean` (398 `#check @` lines) and `Names.lean` (1128) are mechanical and are not reproduced; their hashes and results are in §0.
- `EnvAudit.lean` and its output are reproduced after the probes.

### `P17Probes.lean`

sha256 `c261e2cb0bc5e10467802a6eda56fa82ca592a8fdda767ebaf23d27b5c04502e`.

```lean
import Becoming

/-!
# Probes for P17 (eighth independent review)

Term mode only. Every declaration imports the unchanged `Becoming` at `badb652e`.
-/

namespace Becoming.Probe

variable {F C : Type}

/-! ## L4: a reserve need not be any condition's level -/

/-- No held condition of `Seed.web` carries the seed: the seed is active and unsupported
at step one, so `Carries.pos` would make the held condition's level positive, and every
level of `Seed.web` is zero. The reserve `Seed.reserve` carries it all the same. -/
theorem seed_no_held : ∀ hold : Unit → Unit,
    ¬ Seed.web.Carries fun t f => Seed.web.level t (hold f) :=
  fun _ carries => Nat.lt_irrefl 0 (carries.pos (t := 1) (f := ()) Nat.zero_lt_one (Seed.dark 1))

/-- The same for `Viable`, active and unsupported at step two. -/
theorem viable_no_held : ∀ hold : Unit → Unit,
    ¬ Viable.web.Carries fun t f => Viable.web.level t (hold f) :=
  fun _ carries => Nat.lt_irrefl 0 (carries.pos (t := 2) (f := ()) rfl (Viable.dark 2))

/-! ## L5: `drawn` counts anyone's uptake -/

namespace Larder

inductive Formation where
  | fox
  | crow

inductive Condition where
  | hare
  | fat

/-- The fat: two units, then one, then none. -/
def stock : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

/-- The crow eats a unit of fat across steps zero and one. -/
def eat : Nat → Nat
  | 0 => 1
  | 1 => 1
  | _ + 2 => 0

/-- The fox depends on the hare, which is gone, at need one; the fox draws on nothing.
The crow draws on the fat. Both are active at steps zero and one. -/
def web : Web Formation Condition where
  level t c := match c with
    | .hare => 0
    | .fat => stock t
  active t f := match f with
    | .fox => t < 2
    | .crow => t < 2
  requires _ f c := f = .fox ∧ c = .hare
  need _ _ _ := 1
  draws _ f c := f = .crow ∧ c = .fat

def crowEats (t : Nat) : Condition → Nat
  | .hare => 0
  | .fat => eat t

/-- Only the crow takes part; it eats the fat. Nothing gives. -/
def flow : Flow Formation Condition where
  present _ := [.crow]
  take t f c := match f with
    | .fox => 0
    | .crow => crowEats t c
  give _ _ _ := 0

/-- The fox "holds" the fat. -/
def hold : Formation → Condition
  | .fox => .fat
  | .crow => .fat

theorem balances : flow.Balances web
  | 0, .hare | 0, .fat => rfl
  | 1, .hare | 1, .fat => rfl
  | _ + 2, .hare | _ + 2, .fat => rfl

/-- `Flow.carries_of_held` applies with every premise met, though the fox takes nothing
and does not take part: the fat that "carries" the fox is eaten by the crow. -/
theorem carries : web.Carries fun t f => web.level t (hold f) :=
  Flow.carries_of_held balances hold (fun _ _ _ => total_zero _) fun t f unsupported active =>
    match f, t, unsupported, active with
    | .crow, _, unsupported, _ => False.elim (unsupported fun _ depends => nomatch depends.1)
    | .fox, 0, _, _ => Nat.zero_lt_one
    | .fox, 1, _, _ => Nat.zero_lt_one
    | .fox, _ + 2, _, active => absurd active (Nat.not_lt_of_le (Nat.le_add_left 2 _))

theorem fox_absent (t : Nat) : ¬ Formation.fox ∈ flow.present t :=
  fun mem => match mem with
    | .tail _ no => nomatch no

theorem larder : flow.Balances web ∧ web.Carries (fun t f => web.level t (hold f)) ∧
    (∀ t, ¬ Formation.fox ∈ flow.present t) ∧ (∀ t c, flow.take t .fox c = 0) ∧
    ¬ web.Dependent ∧ web.active 1 .fox :=
  ⟨balances, carries, fox_absent, fun _ _ => rfl,
   fun dependent => Nat.not_succ_le_zero 0 (dependent 1 .fox (Nat.lt_succ_self 1) .hare ⟨rfl, rfl⟩),
   Nat.lt_succ_self 1⟩

end Larder

/-- Corrected form: the holder itself takes part and takes from what it holds. -/
theorem carries_of_own {L : Flow F C} {W : Web F C} (balances : L.Balances W) (hold : F → C)
    (unreplenished : ∀ t f, ¬ W.Supported t f → L.given t (hold f) = 0)
    (takes : ∀ t f, ¬ W.Supported t f → W.active t f →
      f ∈ L.present t ∧ 0 < L.take t f (hold f)) :
    W.Carries fun t f => W.level t (hold f) :=
  Flow.carries_of_held balances hold unreplenished fun t f unsupported active =>
    total_pos_of_mem (takes t f unsupported active).1 (takes t f unsupported active).2

/-! ## L6: the transformed reading in general, and what it changes -/

/-- Choice on a decidable proposition. -/
def pick {α : Sort u} {p : Prop} [d : Decidable p] (a b : α) : α :=
  match d with
  | .isTrue _ => a
  | .isFalse _ => b

theorem pick_cases {α : Sort u} {β : Sort v} {p : Prop} [d : Decidable p] {a a' : α}
    {b b' : β} {q : α → β → Prop} (yes : p → q a b) (no : ¬ p → q a' b') :
    q (pick (p := p) a a') (pick (p := p) b b') :=
  match d with
  | .isTrue holds => yes holds
  | .isFalse fails => no fails

/-- The same unfolding with each unsupported formation's dependence moved onto the
condition it holds, at need one: levels, activity and drawing unchanged. -/
def redirect (W : Web F C) (hold : F → C) [∀ t f, Decidable (W.Supported t f)] : Web F C where
  level := W.level
  active := W.active
  requires t f c := pick (p := W.Supported t f) (W.requires t f c) (c = hold f)
  need t f c := pick (p := W.Supported t f) (W.need t f c) 1
  draws := W.draws

/-- The general construction the study lists as open: wherever a held condition carries a
formation, the redirected reading is `Dependent`. -/
theorem redirect_dependent (W : Web F C) (hold : F → C) [∀ t f, Decidable (W.Supported t f)]
    (carries : W.Carries fun t f => W.level t (hold f)) : (redirect W hold).Dependent :=
  fun t f active c => pick_cases (p := W.Supported t f)
    (q := fun (r : Prop) (n : Nat) => r → n ≤ W.level t c)
    (fun supported depends => supported c depends)
    (fun unsupported same => Eq.subst (motive := fun y => 1 ≤ W.level t y) same.symm
      (carries.pos active unsupported))

theorem redirect_same (W : Web F C) (hold : F → C) [∀ t f, Decidable (W.Supported t f)] :
    (redirect W hold).level = W.level ∧ (redirect W hold).active = W.active ∧
      (redirect W hold).draws = W.draws :=
  ⟨rfl, rfl, rfl⟩

/-- In `Famine` the fox's event at step one is undermining as published: it draws on the
hare, whose dependence it met at step zero, and the hare is below need after the step. -/
theorem famine_undermines_one : Famine.web.UnderminingAt 1 .fox :=
  ⟨.hare, ⟨rfl, .inl rfl⟩, .fox, ⟨rfl, rfl⟩,
   ⟨0, Nat.zero_le 1, fun _ _ _ => ⟨rfl, rfl⟩, Nat.le_refl 1, Nat.zero_lt_one⟩,
   Nat.zero_lt_one⟩

/-- Read with the dependence transformed onto the fat, the same event is not undermining:
the fat stands at one after the step, which meets the need. -/
theorem famine_transformed_not_undermining_one : ¬ Famine.transformed.UnderminingAt 1 .fox :=
  fun ⟨_, _, _, ⟨_, same⟩, _, below⟩ =>
    Nat.lt_irrefl 1 (Eq.subst (motive := fun y => Famine.transformed.level 2 y < 1) same below)

/-- So the two readings of "the same unfolding" disagree on whether the fox's event at
step one is living in the stepwise reading (active and not undermining). -/
theorem famine_living_differs :
    (Famine.web.active 1 .fox ∧ Famine.web.UnderminingAt 1 .fox) ∧
    (Famine.transformed.active 1 .fox ∧ ¬ Famine.transformed.UnderminingAt 1 .fox) :=
  ⟨⟨Nat.lt_succ_of_lt (Nat.lt_succ_self 1), famine_undermines_one⟩,
   ⟨Nat.lt_succ_of_lt (Nat.lt_succ_self 1), famine_transformed_not_undermining_one⟩⟩

/-! ## L7: what the requirement uses is a rise -/

/-- In a balanced flow every rise of a condition is given to (the qualitative part of P11's
`Balances.renewedBy`, without `Acting`). -/
theorem rise_given {L : Flow F C} {W : Web F C} (balances : L.Balances W) {t : Nat} {c : C}
    (rises : W.Rises t c) : 0 < L.given t c :=
  Nat.pos_of_ne_zero fun none =>
    Nat.not_le_of_gt rises (Nat.le_trans (Nat.le_add_right _ (L.taken t c))
      (Nat.le_of_eq ((balances t c).trans (congrArg (W.level t c + ·) none))))

/-- Coming to stand is the rise from zero. -/
theorem comes_rises {W : Web F C} {t : Nat} {c : C} (comes : W.ComesToStand t c) :
    W.Rises t c :=
  Nat.lt_of_le_of_lt (Nat.le_of_eq (eq_zero_of_not_pos comes.1)) comes.2

/-- `standing_lowers_on` for any rise. -/
theorem rise_lowers_on {L : Flow F C} {W : Web F C} (balances : L.Balances W) {ds : List C}
    {t : Nat} (dissipates : L.DissipatesOn ds t) {c : C} (mem : c ∈ ds) (rises : W.Rises t c) :
    W.stock ds (t + 1) < W.stock ds t :=
  match total_pos (L.present t) (rise_given balances rises) with
  | ⟨_, present, gives⟩ => Nat.lt_of_lt_of_le
      (Nat.lt_add_of_pos_right (total_pos_of_mem (q := fun f => sign (total ds (L.take t f)))
        present (sign_pos (dissipates.takes_of_gives present (total_pos_of_mem mem gives)))))
      (balances.runs_down dissipates)

namespace Growing

/-- A condition rising by one at every step; it never comes to stand. -/
def web : Web Unit Unit where
  level t _ := t + 1
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

def flow : Flow Unit Unit := ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 1⟩

theorem balances : flow.Balances web := fun _ _ => rfl

theorem growing : flow.Balances web ∧ (∀ t, ¬ web.ComesToStand t ()) ∧
    (∀ t, web.Rises t ()) ∧ ∀ t, 0 < flow.given t () :=
  ⟨balances, fun t comes => comes.1 (Nat.succ_pos t), fun t => Nat.lt_succ_self (t + 1),
   fun t => rise_given balances (Nat.lt_succ_self (t + 1))⟩

end Growing

end Becoming.Probe
```

### `P18Probes.lean`

sha256 `8ac45e45828b60b4c202f9554c1279f51b6bf1a1cc78cc349b96de9f1fbfc8e6`.

```lean
import Becoming

/-!
# Probes for P18 (eighth independent review)

Term mode only. Every declaration imports the unchanged `Becoming` at `badb652e`.
-/

namespace Becoming.Probe

variable {X Pos : Type}

/-! ## L8 and L9: living on a relatum that is neither embodied nor active -/

/-- What `Dependent` does give: a lived-on relatum stands at that step. -/
theorem LivesOn.stands {W : Web X X} (dependent : W.Dependent) {e e' : X × Nat}
    (lives : W.LivesOn e e') (active : W.active e.2 e.1) : 0 < W.level e.2 e'.1 :=
  Nat.lt_of_lt_of_le lives.2.2 (dependent e.2 e.1 active e'.1 lives.2.1)

namespace Drowsy

inductive Relatum where
  | eater
  | sleeper

/-- One at odd steps, zero at even ones. -/
def odd : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n + 2 => odd n

/-- The sleeper stands at one throughout and is awake at odd steps; the eater is always
active, draws on the sleeper and depends on it at need one. -/
def web : Web Relatum Relatum where
  level _ x := match x with
    | .eater => 0
    | .sleeper => 1
  active t x := match x with
    | .eater => True
    | .sleeper => 0 < odd t
  requires _ g y := g = .eater ∧ y = .sleeper
  need _ _ _ := 1
  draws _ g y := g = .eater ∧ y = .sleeper

theorem dependent : web.Dependent :=
  fun t _ _ _ depends =>
    Eq.subst (motive := fun y => 1 ≤ web.level t y) depends.2.symm (Nat.le_refl 1)

theorem not_undermining (t : Nat) (f : Relatum) : ¬ web.UnderminingAt t f :=
  fun ⟨_, drawn, _, _, _, below⟩ =>
    Nat.lt_irrefl 1 (Eq.subst (motive := fun y => web.level (t + 1) y < 1) drawn.2 below)

theorem lives (t s : Nat) : web.LivesOn (.eater, t) (.sleeper, s) :=
  ⟨⟨rfl, rfl⟩, ⟨rfl, rfl⟩, Nat.zero_lt_one⟩

variable (own sig : Pos → Relatum × Nat → Prop)

theorem eater_alive (t : Nat) : (web.sustenance own sig).living (.eater, t) :=
  ⟨trivial, not_undermining t .eater⟩

theorem sleeper_alive : (web.sustenance own sig).living (.sleeper, 1) :=
  ⟨Nat.zero_lt_one, not_undermining 1 .sleeper⟩

theorem down : ∀ e, (web.sustenance own sig).living e →
    Reach (web.sustenance own sig).relations e (.eater, 0)
  | (.eater, t), _ => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inl (lives t 1)), sleeper_alive own sig⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inr (lives 0 1)), eater_alive own sig 0⟩)
  | (.sleeper, s), _ => Reach.of_step (a := ()) ⟨.inr (.inr (lives 0 s)), eater_alive own sig 0⟩

theorem up : ∀ e, (web.sustenance own sig).living e →
    Reach (web.sustenance own sig).relations (.eater, 0) e
  | (.eater, t), alive => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inl (lives 0 1)), sleeper_alive own sig⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inr (lives t 1)), alive⟩)
  | (.sleeper, s), alive => Reach.of_step (a := ()) ⟨.inr (.inl (lives 0 s)), alive⟩

theorem sustenance_connected : (web.sustenance own sig).Connected :=
  fun c d alive alive' => Reach.trans (down own sig c alive) (up own sig d alive')

/-- Interaction relates only the eater's events: every interacting target is the eater. -/
theorem not_interacting : ¬ (web.interaction own sig).Connected := fun connected =>
  Relatum.noConfusion (Invariant.reach (P := (web.interaction own sig).relations)
    (I := fun e => e.1 = Relatum.eater)
    (fun _ _ _ ⟨⟨_, interacts⟩, _⟩ _ => match interacts with
      | .inl ⟨_, bearing⟩ => bearing.1.1
      | .inr ⟨_, drawn⟩ => drawn.1)
    (connected (.eater, 0) (.sleeper, 1) ⟨trivial, not_undermining 0 .eater⟩
      ⟨Nat.zero_lt_one, not_undermining 1 .sleeper⟩) rfl)

/-- Under `Dependent`, an active formation lives on a relatum that is not embodied and not
active at that step; living on connects the web, and interaction does not. -/
theorem drowsy : web.Dependent ∧ ¬ web.Embodied .sleeper ∧ web.active 0 .eater ∧
    web.LivesOn (.eater, 0) (.sleeper, 0) ∧ ¬ web.active 0 .sleeper ∧
    (web.sustenance own sig).Connected ∧ ¬ (web.interaction own sig).Connected :=
  ⟨dependent, fun embodied => Nat.lt_irrefl 0 ((embodied 0).mpr Nat.zero_lt_one), trivial,
   lives 0 0, Nat.lt_irrefl 0, sustenance_connected own sig, not_interacting own sig⟩

end Drowsy

/-! ## L10: descent from a formation that does not take part -/

namespace Stranger

inductive Relatum where
  | parent
  | seed
  | stranger

def gift : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- The seed stands and is active from step one; the parent and the stranger are always
active and stand at zero. Nothing depends on or draws on anything. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .parent => 0
    | .seed => SunSeed.sprout t
    | .stranger => 0
  active t x := match x with
    | .parent => True
    | .seed => 0 < SunSeed.sprout t
    | .stranger => True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

def toSeed (t : Nat) : Relatum → Nat
  | .parent => 0
  | .seed => gift t
  | .stranger => 0

/-- Only the parent takes part, and it gives the seed one unit across step zero. -/
def honest : Flow Relatum Relatum where
  present _ := [.parent]
  take _ _ _ := 0
  give t g y := match g with
    | .parent => toSeed t y
    | .seed => 0
    | .stranger => 0

/-- The same, with a `give` entry for the stranger, which does not take part. -/
def nominal : Flow Relatum Relatum where
  present _ := [.parent]
  take _ _ _ := 0
  give t g y := match g with
    | .parent => toSeed t y
    | .seed => 0
    | .stranger => toSeed t y

theorem honest_balances : honest.Balances web
  | 0, .parent | 0, .seed | 0, .stranger => rfl
  | _ + 1, .parent | _ + 1, .seed | _ + 1, .stranger => rfl

theorem nominal_balances : nominal.Balances web
  | 0, .parent | 0, .seed | 0, .stranger => rfl
  | _ + 1, .parent | _ + 1, .seed | _ + 1, .stranger => rfl

theorem honest_acting : honest.Acting web
  | _, .parent, _, _, _ => trivial
  | _, .seed, _, _, gives => absurd gives (Nat.lt_irrefl 0)
  | _, .stranger, _, _, _ => trivial

theorem nominal_acting : nominal.Acting web
  | _, .parent, _, _, _ => trivial
  | _, .seed, _, _, gives => absurd gives (Nat.lt_irrefl 0)
  | _, .stranger, _, _, _ => trivial

theorem same_given (t : Nat) (y : Relatum) : honest.given t y = nominal.given t y := rfl

theorem absent (t : Nat) : ¬ Relatum.stranger ∈ nominal.present t :=
  fun mem => match mem with
    | .tail _ no => nomatch no

theorem from_parent : nominal.Descends web .seed .parent :=
  ⟨0, Nat.zero_lt_one, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩⟩

theorem from_stranger : nominal.Descends web .seed .stranger :=
  ⟨0, Nat.zero_lt_one, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩⟩

theorem honest_from_parent : honest.Descends web .seed .parent :=
  ⟨0, Nat.zero_lt_one, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩⟩

theorem not_undermining (t : Nat) (f : Relatum) : ¬ web.UnderminingAt t f :=
  fun ⟨_, drawn, _⟩ => drawn

variable (own sig : Pos → Relatum × Nat → Prop)

theorem seed_alive : (nominal.descent web own sig).living (.seed, 1) :=
  ⟨Nat.zero_lt_one, not_undermining 1 .seed⟩

theorem parent_alive (t : Nat) : (nominal.descent web own sig).living (.parent, t) :=
  ⟨trivial, not_undermining t .parent⟩

theorem down : ∀ e, (nominal.descent web own sig).living e →
    Reach (nominal.descent web own sig).relations e (.seed, 1)
  | (.parent, _), _ => Reach.of_step (a := ()) ⟨.inr (.inl from_parent), seed_alive own sig⟩
  | (.seed, _), _ => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inr from_parent), parent_alive own sig 0⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inl from_parent), seed_alive own sig⟩)
  | (.stranger, _), _ => Reach.of_step (a := ()) ⟨.inr (.inl from_stranger), seed_alive own sig⟩

theorem up : ∀ e, (nominal.descent web own sig).living e →
    Reach (nominal.descent web own sig).relations (.seed, 1) e
  | (.parent, _), alive => Reach.of_step (a := ()) ⟨.inr (.inr from_parent), alive⟩
  | (.seed, _), alive => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inr from_parent), parent_alive own sig 0⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inl from_parent), alive⟩)
  | (.stranger, _), alive => Reach.of_step (a := ()) ⟨.inr (.inr from_stranger), alive⟩

theorem nominal_connected : (nominal.descent web own sig).Connected :=
  fun c d alive alive' => Reach.trans (down own sig c alive) (up own sig d alive')

/-- In the honest flow nothing related to the stranger's events: no step reaches it. -/
theorem honest_not_connected : ¬ (honest.descent web own sig).Connected := fun connected =>
  Invariant.reach (P := (honest.descent web own sig).relations)
    (I := fun e => ¬ e.1 = Relatum.stranger)
    (fun _ _ _ ⟨related, _⟩ _ same => match related with
      | .inl ⟨_, interacts⟩ => match interacts with
        | .inl ⟨drawn, _⟩ => drawn
        | .inr ⟨_, drawn⟩ => drawn
      | .inr (.inl ⟨u, _, comes⟩) => Nat.lt_irrefl 0
          (Eq.subst (motive := fun y => 0 < web.level (u + 1) y) same comes.2)
      | .inr (.inr ⟨u, gives, _⟩) => Nat.lt_irrefl 0
          (Eq.subst (motive := fun y => 0 < honest.give u y _) same gives))
    (connected (.parent, 0) (.stranger, 0) ⟨trivial, not_undermining 0 .parent⟩
      ⟨trivial, not_undermining 0 .stranger⟩)
    (fun same => Relatum.noConfusion same) rfl

/-- Two flows over the same web, both balanced and `Acting`, with the same formations
taking part and the same amount given to every condition at every step, differ only in a
`give` entry of a formation that does not take part. Descent connects one and not the
other. -/
theorem stranger : honest.Balances web ∧ nominal.Balances web ∧ honest.Acting web ∧
    nominal.Acting web ∧ (∀ t y, honest.given t y = nominal.given t y) ∧
    (∀ t, ¬ Relatum.stranger ∈ nominal.present t) ∧
    nominal.Descends web .seed .stranger ∧ honest.Descends web .seed .parent ∧
    (nominal.descent web own sig).Connected ∧ ¬ (honest.descent web own sig).Connected :=
  ⟨honest_balances, nominal_balances, honest_acting, nominal_acting, same_given, absent,
   from_stranger, honest_from_parent, nominal_connected own sig, honest_not_connected own sig⟩

end Stranger

/-- In `Brood` the giver of `give` is ignored, so every generation descends from every
number: generation `t + 1` descends from generation `g`, whatever `g` is. -/
theorem brood_descends_from_any (t g : Nat) : Brood.flow.Descends Brood.web (t + 1) g :=
  ⟨t, Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (Brood.birth_next t).symm), Brood.arises t⟩

/-- In particular generation one descends from generation seven, which neither takes part
at step zero nor stands there; and generation six descends from generation zero across
step five. -/
theorem brood_examples : Brood.flow.Descends Brood.web 1 7 ∧ ¬ 7 ∈ Brood.flow.present 0 ∧
    Brood.web.level 0 7 = 0 ∧ Brood.flow.Descends Brood.web 6 0 :=
  ⟨brood_descends_from_any 0 7, (fun mem => match mem with | .tail _ no => nomatch no), rfl,
   brood_descends_from_any 5 0⟩

/-! ## Corrected descent: the giver takes part -/

/-- `x` descends from `g` when `g` takes part at a step at which it gives to `x` and `x`
comes to stand. -/
def DescendsIn (L : Flow X X) (W : Web X X) (x g : X) : Prop :=
  ∃ t, g ∈ L.present t ∧ 0 < L.give t g x ∧ W.ComesToStand t x

/-- `Embodied.descends` holds unchanged for the corrected form. -/
theorem Embodied.descendsIn {W : Web X X} {L : Flow X X} (balances : L.Balances W)
    (acting : L.Acting W) {x : X} (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ g, W.active t g ∧ g ≠ x ∧ DescendsIn L W x g :=
  match embodied.arises_given balances acting arises with
  | ⟨g, active, present, gives, other⟩ =>
    ⟨g, active, other, t, present, gives, embodied.comesToStand arises⟩

theorem brood_descendsIn (t : Nat) : DescendsIn Brood.flow Brood.web (t + 1) t :=
  ⟨t, .head _, Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (Brood.birth_next t).symm),
   Brood.arises t⟩

theorem brood_not_descendsIn : ¬ DescendsIn Brood.flow Brood.web 1 7 :=
  fun ⟨t, mem, gives, _⟩ => match t, mem, gives with
    | 0, mem, _ => match mem with
      | .tail _ no => nomatch no
    | _ + 1, _, gives => Nat.lt_irrefl 0 gives

theorem provisioned_descendsIn : DescendsIn Provisioned.flow Provisioned.web .seed .parent :=
  ⟨0, .head _, Nat.zero_lt_one, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩⟩

theorem stranger_not_descendsIn :
    ¬ DescendsIn Stranger.nominal Stranger.web .seed .stranger :=
  fun ⟨t, mem, _⟩ => Stranger.absent t mem

/-- Descent with the giver taking part, read stepwise beside interaction. -/
def descentIn (L : Flow X X) (W : Web X X) (own sig : Pos → X × Nat → Prop) :
    Valuation Pos (X × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := (∃ c, W.Interacts c e e') ∨ DescendsIn L W e'.1 e.1 ∨ DescendsIn L W e.1 e'.1
  own := own
  sig := sig

/-- `Brood.descended`'s connection survives the correction. -/
theorem brood_descentIn_connected (own sig : Pos → Nat × Nat → Prop) :
    (descentIn Brood.flow Brood.web own sig).Connected :=
  have self_alive (t : Nat) : (descentIn Brood.flow Brood.web own sig).living (t, t) :=
    Brood.alive_of_stands own sig
      (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (Brood.standing_self t).symm))
  have down : ∀ x s, (descentIn Brood.flow Brood.web own sig).living (x, s) →
      Reach (descentIn Brood.flow Brood.web own sig).relations (x, s) (0, 0) :=
    fun x => Nat.rec (motive := fun x => ∀ s, (descentIn Brood.flow Brood.web own sig).living (x, s) →
        Reach (descentIn Brood.flow Brood.web own sig).relations (x, s) (0, 0))
      (fun _ _ => Reach.trans
        (Reach.of_step (a := ()) ⟨.inr (.inl (brood_descendsIn 0)), self_alive 1⟩)
        (Reach.of_step (a := ()) ⟨.inr (.inr (brood_descendsIn 0)), self_alive 0⟩))
      (fun x below _ _ => Reach.trans
        (Reach.of_step (a := ()) ⟨.inr (.inr (brood_descendsIn x)), self_alive x⟩)
        (below x (self_alive x))) x
  have up : ∀ y s, (descentIn Brood.flow Brood.web own sig).living (y, s) →
      Reach (descentIn Brood.flow Brood.web own sig).relations (0, 0) (y, s) :=
    fun y => Nat.rec (motive := fun y => ∀ s, (descentIn Brood.flow Brood.web own sig).living (y, s) →
        Reach (descentIn Brood.flow Brood.web own sig).relations (0, 0) (y, s))
      (fun _ alive => Reach.trans
        (Reach.of_step (a := ()) ⟨.inr (.inl (brood_descendsIn 0)), self_alive 1⟩)
        (Reach.of_step (a := ()) ⟨.inr (.inr (brood_descendsIn 0)), alive⟩))
      (fun y below _ alive => Reach.trans (below y (self_alive y))
        (Reach.of_step (a := ()) ⟨.inr (.inl (brood_descendsIn y)), alive⟩)) y
  fun c d alive alive' => Reach.trans (down c.1 c.2 alive) (up d.1 d.2 alive')

end Becoming.Probe
```

### `ProbeEnvAudit.lean`

sha256 `be6280c196841fffee4a6daa4042b053f985cd24132c04d971b07958a79f24cd`.

```lean
import P17Probes
import P18Probes
import Lean
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [`P17Probes, `P18Probes] do
    let some idx := env.getModuleIdx? m | logInfo m!"no module {m}"
    let mut total := 0
    let mut bad : Array Name := #[]
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some idx then
        total := total + 1
        let axs ← liftCoreM <| Lean.collectAxioms n
        if axs.size > 0 then bad := bad.push n
    logInfo m!"{m}: {total} constants, {bad.size} with axioms: {bad.toList}"
```

### `EnvAudit.lean`

sha256 `c51e1ba61ff5be9ad4f6cc59a5d8753fe7c0e900834c3bb8cddb7a815b3183b0`.

```lean
import Becoming
import Lean
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  let mods : List Name := [`GenerativeCore, `InquirySufficiency, `RelationalRenewal,
    `Becoming.Frame, `Becoming.Inquiry, `Becoming.Renewal, `Becoming.Dependence, `Becoming.Return,
    `Becoming.Horizon, `Becoming.Joint, `Becoming.Substitution, `Becoming.Generation,
    `Becoming.Flow, `Becoming.Population, `Becoming.Identity, `Becoming.Wholes,
    `Becoming.Dissipation, `Becoming.Roles, `Becoming.Reserve, `Becoming.Metaethics,
    `Becoming.Ranking, `Becoming.Correspondence, `Becoming.Descent, `Becoming]
  let mut all := 0
  let mut withAx := 0
  for m in mods do
    let some idx := env.getModuleIdx? m | logInfo m!"no module {m}"
    let mut total := 0
    let mut bad : Array (Name × Array Name) := #[]
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some idx then
        total := total + 1
        let axs ← liftCoreM <| Lean.collectAxioms n
        if axs.size > 0 then bad := bad.push (n, axs)
    all := all + total
    withAx := withAx + bad.size
    let nonInj := bad.filter (fun (n, _) => !(n.toString.endsWith "injEq"))
    logInfo m!"{m}: {total} constants, {bad.size} with axioms, {nonInj.size} of them not injEq: {nonInj.toList}"
  logInfo m!"ALL: {all} constants, {withAx} with axioms"
```

Output of `EnvAudit.lean` (each line: constants of the module, how many depend on an axiom, and how many of those are not `injEq` lemmas):

```text
GenerativeCore: 54 constants, 1 with axioms, 0 of them not injEq: []
InquirySufficiency: 107 constants, 2 with axioms, 0 of them not injEq: []
RelationalRenewal: 134 constants, 2 with axioms, 0 of them not injEq: []
Becoming.Frame: 61 constants, 2 with axioms, 0 of them not injEq: []
Becoming.Inquiry: 15 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Renewal: 58 constants, 1 with axioms, 0 of them not injEq: []
Becoming.Dependence: 475 constants, 5 with axioms, 0 of them not injEq: []
Becoming.Return: 84 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Horizon: 43 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Joint: 203 constants, 4 with axioms, 0 of them not injEq: []
Becoming.Substitution: 40 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Generation: 216 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Flow: 206 constants, 1 with axioms, 0 of them not injEq: []
Becoming.Population: 138 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Identity: 487 constants, 2 with axioms, 0 of them not injEq: []
Becoming.Wholes: 147 constants, 1 with axioms, 0 of them not injEq: []
Becoming.Dissipation: 298 constants, 2 with axioms, 0 of them not injEq: []
Becoming.Roles: 461 constants, 4 with axioms, 0 of them not injEq: []
Becoming.Reserve: 138 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Metaethics: 226 constants, 1 with axioms, 0 of them not injEq: []
Becoming.Ranking: 170 constants, 0 with axioms, 0 of them not injEq: []
Becoming.Correspondence: 159 constants, 1 with axioms, 0 of them not injEq: []
Becoming.Descent: 43 constants, 0 with axioms, 0 of them not injEq: []
Becoming: 0 constants, 0 with axioms, 0 of them not injEq: []
ALL: 3963 constants, 29 with axioms
```

The 29 are, by module: GenerativeCore `Generative.Process.mk.injEq`; InquirySufficiency `Policy.respond.injEq`, `Policy.inquire.injEq`; RelationalRenewal `Unfolding.mk.injEq`, `Law.mk.injEq`; Frame `Run.mk.injEq`, `Frame.mk.injEq`; Renewal `Conditions.mk.injEq`; Dependence `Crossing.State.mk.injEq`, `Crossing.Move.fall.injEq`, `Dependence.mk.injEq`, `Pinned.State.mk.injEq`, `Web.mk.injEq`; Joint `Pool.Draw.mk.injEq`, `Pool.State.mk.injEq`, `Shock.State.mk.injEq`, `Shock.Move.calm.injEq`; Flow `Flow.mk.injEq`; Identity `Reidentify.mk.injEq`, `Confluence.Formation.new.injEq`; Wholes `Generations.Formation.member.injEq`; Dissipation `Frontier.Formation.grower.injEq`, `Frontier.Condition.fuel.injEq`; Roles `Kindling.Relatum.side.injEq`, `Kindling.Relatum.fuel.injEq`, `SprayHanding.Relatum.aux.injEq`, `SprayHanding.Relatum.side.injEq`; Metaethics `Valuation.mk.injEq`; Correspondence `Web.Condition.mk.injEq`. Each depends on `propext` only.
