# P15、P16 与 P16b 的独立审查 / Independent review of P15, P16 and P16b

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写这三个阶段。对象：`main` 的 `b24963f1`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of the three phases. Object: `main` at `b24963f1`.

**摘要（中文）。** 三个阶段的全部 Lean 声明都在仓库之外从前导重新编译。核心闭包的 22 个模块退出码为 0，没有警告，1185 条声明的公理报告全部为空。回执 `20261009T071936.578078Z`（676 项定理／1115 项声明审计，核心闭包 22 个模块，包 20 个模块）、35 个源哈希、18 份变更记录的 216 个引用哈希与 53 个证明绑定都对。335 个别名中 304 个在核心中解析，其余 31 个属于未重建的桥接（26）与 Mathlib 外围（5）。数学被接受，Lean 中没有发现数学错误。本审查写了 57 条探针声明（其中 46 项定理），都不依赖任何公理。问题出在前提的陈述、散文与对应上，共八项（K1–K8）：一项散文中的错误，五项说得过强，一项见证强度不足，一项记账与用语。

- **P15（生成即补充）。** `given_of_arises`、`replenishes`、`generation_needs_replenishment`、`takes_of_gives`、`arising_lowers`、`generation_opens` 与 `generation_ceases` 都对。`generation_ceases` 不需要 `Enclosed`：关系项总共有限时，每一步都封闭。`Handing`、`Kindling` 与 `Flicker` 是真见证。问题如下。
  - **J1 的模式移到了生成（K1）。** `generation_opens` 的结论是家族从任何一步起都不封闭，这可以由与家族无关的交换满足。`SprayHanding` 在 `Handing` 上加一个汇，它与每个辅助关系项交换，但从不触及两方。耗散因此空洞地成立。两方构成的家族存量每步为一，没有任何东西流入，生成在其中不息；定理的结论则由汇满足。所以下面三句话在定义上不成立：“耗散之下没有有限部分独自承担它”、“体现的生成在一个有限家族中复现，家族就须与其外交换”、“须由越出每个有限部分的展开承担”。P16b 为取用写明了这一点，却没有带到生成；P13 的记录标题也没有改。本审查形式化了更正：在包含家族的封闭之下（`Around`），取用或体现的生起复现时，在任意晚的步有给予家族者从家族之外取用（`taking_draws_in`、`generation_draws_in`）。`Kindling` 与 `Frontier` 非空地满足它。
  - **省去“被耗散”（K2）。** “耗散之下，给予家族者从家族取用”省去了家族须被耗散，即须封闭。`Frontier` 的太阳给予池，却不从池取用。
- **P16（整体与部分）。** `Whole`、`arises_part`、`parts_unceasing`、`arises_within` 与 `needs_arising` 都对；`Immortal`、`Countless`、`Generations`、`Shifts` 与 `Gaps` 是真见证。问题如下。
  - **“就是”（K3）。** “整体的持续就是部分的生成”是同一的说法，定理只给出必要条件：`Gaps` 表明逆命题不成立，英文标题用的也是 through。`Whole` 只是活动的同时：每个形成都是自身的整体，两个始终活跃的形成互为整体，两个主要定理也只用了它的一个方向。在 `Brief` 之下，“部分的生成”可以是两个部分反复生起（`Layered`）。所以“这一张力消失”、“整体的不息正由部分的生生构成”说得过强。只有在 `Ends` 与 `Listed` 之下，才有越出任何有限列表的新部分生起（`needs_new`，这是模块未陈述的推论）。
  - **省去 `Listed`（K4）。** 记录标题、章节英文、§9 与术语表中的“部分不长久时”省去了有限列出。`Countless` 的每个部分都终结，整体持续，却没有任何生起。
  - **反驳 3 有误（K5）。** §21 反驳 3 说 `Layered` 的成员不满足 `Brief`，两个定理都不适用。实际上成员满足 `Brief 1`，`arises_within` 适用，每一步都有成员生起。
- **P16b（第六次审查的处理）。** J1–J11 都有处理，探针内容移入了核心。`relabel` 只要求到上，比审查所用的对合更一般，并且正确；`roles_dissipative` 双向成立。`Lone`、`Rooted`、`witnesses_not_dissipative`、`Wilting`、`met_iff`、`apart_embodied`、`Fork`、`no_join`、`decideContinues` 与 `Dormant.no_split_without_arising` 都对。问题如下。
  - **生由生（K6）。** J7 的改题是对的。但“‘生由生’在只有体现者给予的前提下证明”把体现读成了生命。这一前提可以由一个太阳满足：它的水平定为一，不依存、不汲取、不取用，也不承担自身（`EmbodiedSun`）。体现的关系项是不是“生”，属于 Ren 对“生”的读法。第六次审查 §4 第 4 项的措辞“在只有生命给予的前提下证明生由生”引出了这一混同。
  - **合并的见证（K7）。** `Merge` 中没有形成延续为生长者，所以第一个生长者每一步都“生起”，`UnceasingFrom` 不需要“更多”就成立。第六次审查把它判为非空的见证，这是那次审查的错。`Confluence` 给出一个合并而没有虚假生起的见证。
  - **记账与用语（K8）。** 具体有八处：§20 引言残留“付出”；计划的 P15 一行仍写 `Brood.costless`；“给予者／giver”重新出现，而第五次审查 I4(d) 曾把它改名；“没有封闭的步”的措辞不准；`gives_less` 的注释省去“不重复”；§22.4 反驳 1 中“每步满足”的说法没有证明（探针已补证）；一份记录的审查时间早于它引用的回执；P15、P16 的段落把包写成核心。
- **J1–J11。** 八项关闭。J1 与 J7 已处理，但仍有说得过强之处（K1、K6）；J11 已处理，但有残余（K8）。
- **非二元方法、Ren 的原话与读法选择。** 没有替 Ren 选择接续的读法、终结之步的汲取、“生生不息”读到哪个层次，也没有替 Ren 定名称。Ren 的原话引用准确。K6 把“生”读作体现；K3 的“张力消失”给一个层次的读法赋予了多于定理的内容。两处都有 AI 标注，但标注不能让定理没有给出的内容成立。

**Summary (English).** Every Lean declaration of the three phases recompiles from the prelude outside the repository. The 22 modules of the core closure exit 0 with no warnings, and all 1185 of their declarations have empty axiom reports. The receipt `20261009T071936.578078Z` (676 theorems and 1115 declaration audits; core closure 22 modules, package 20) is correct, as are its 35 source hashes and, for the 18 changed records, 216 reference hashes and 53 proof bindings. Of the 335 aliases, 304 resolve in the core; the other 31 belong to the unrebuilt bridge (26) and the Mathlib periphery (5). The mathematics is accepted; no mathematical error was found in the Lean. This review wrote 57 probe declarations (46 of them theorems), none of which depends on any axiom. The eight findings (K1–K8) concern premises, prose and correspondence: one error in prose, five overclaims, one weak witness, and one item of bookkeeping and vocabulary.

- **P15.** `given_of_arises`, `replenishes`, `generation_needs_replenishment`, `takes_of_gives`, `arising_lowers`, `generation_opens` and `generation_ceases` hold. `generation_ceases` does not need `Enclosed`, since with finitely many relata every step is enclosed. `Handing`, `Kindling` and `Flicker` are genuine witnesses.
  - **K1.** This is the J1 pattern, carried into generation. The conclusion of `generation_opens`, that the family is not closed from any step on, can be met by exchange unrelated to the family.
    - `SprayHanding` is `Handing` plus a sink that exchanges with every auxiliary relatum and never touches the sides. Dissipation then holds vacuously.
    - The family of the two sides keeps a stock of one at every step and receives nothing from outside. Generation never ceases inside it, while the theorem's conclusion is met by the sink.
    - So "under dissipation no finite part bears it alone", "the family must exchange beyond itself" and "must be borne by an unfolding beyond every finite part" are false of the definitions.
    - P16b disclosed this pattern for taking but did not carry it to generation, and P13's record title is unchanged.
    - This review formalizes the correction. Under an enclosure containing the family (`Around`), recurring taking or embodied arising means that at arbitrarily late steps some formation gives to the family and takes from beyond it (`taking_draws_in`, `generation_draws_in`). `Kindling` and `Frontier` meet these premises non-vacuously.
  - **K2.** "Under dissipation a formation giving to a family takes from it" drops the requirement that the family be dissipated on, which requires it to be closed. `Frontier`'s sun gives to the pool and takes nothing from it.
- **P16.** `Whole`, `arises_part`, `parts_unceasing`, `arises_within` and `needs_arising` hold. `Immortal`, `Countless`, `Generations`, `Shifts` and `Gaps` are genuine witnesses.
  - **K3.** "整体的持续就是部分的生成" states an identity, but the theorems give only necessity. `Gaps` shows the converse fails, and the English title says "through".
    - `Whole` is coincidence of activity. Every formation is the whole of itself, two always-active formations are each other's whole, and the two main theorems use only one direction of it.
    - Under `Brief`, the generation of parts can be two parts arising again and again (`Layered`). So "the tension disappears" and "the whole's 不息 is made of its parts' 生生" overstate.
    - Only under `Ends` and `Listed` must parts beyond every finite list arise (`needs_new`, a corollary the module does not state).
  - **K4.** "Where parts do not last" omits `Listed` in the record title, the chapter's English, §9 and the glossary. In `Countless` every part ends and the whole persists, yet nothing arises.
  - **K5.** §21 rebuttal 3 says `Layered`'s members fail `Brief` and that neither theorem applies. In fact they are `Brief 1`, `arises_within` applies, and a member arises at every step.
- **P16b.** J1–J11 are all addressed, and the probe content moved into the core.
  - `relabel` needs only surjectivity, which is more general than the involution the sixth review used, and it is correct. `roles_dissipative` holds in both directions.
  - `Lone`, `Rooted`, `witnesses_not_dissipative`, `Wilting`, `met_iff`, `apart_embodied`, `Fork`, `no_join`, `decideContinues` and `Dormant.no_split_without_arising` are correct.
  - **K6.** The J7 retitle is right, but "'生由生' proved under the premise that only embodied relata give" reads embodiment as life. That premise is met by a sun given a level of one, which depends on nothing, draws on nothing, takes nothing and does not bear on itself (`EmbodiedSun`). Whether an embodied relatum is 生 belongs to Ren's reading of 生. The sixth review's §4 item 4 ("'life from life' proved under a stated premise that only lives give") invited this conflation.
  - **K7.** In `Merge` no formation continues as a grower, so the first grower "arises" at every step, and `UnceasingFrom` holds without "more". The sixth review judged `Merge` a non-vacuous witness; that judgement was its error. `Confluence` gives a merge with no spurious arising.
  - **K8.** Eight residues of bookkeeping and vocabulary:
    - "付出" survives in the §20 introduction.
    - The plan's P15 row still names `Brood.costless`.
    - "giver" is back, although the fifth review's I4(d) had renamed it.
    - The wording "no step is enclosed" is imprecise.
    - The gloss on `gives_less` drops "without repetition".
    - The "every step" claim in §22.4 rebuttal 1 was unproved; the probes now prove it.
    - One record's review stamp precedes the receipt it cites.
    - The P15 and P16 paragraphs call the package the core.
- **J1–J11.** Eight are closed. J1 and J7 are closed with an overclaim (K1, K6), and J11 is closed with residues (K8).
- **Ren.** No reading of succession, of drawing at an ending or of the level at which 生生不息 is read is chosen for Ren, and no name is fixed. Ren's words are quoted exactly. K6 reads 生 as embodiment, and K3's "the tension disappears" gives a reading at one level more content than the theorem has. Both are labelled as AI readings, but a label does not supply content the theorem does not give.

## 0. Scope, materials and method

**Object.** `main` at `b24963f19718445c054fb602d01d1eb13a934f57`:

- **P15 (`1101005682d37cb4`).**
  - The new sections of [Becoming.Roles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean): "Generation is replenishment" and the witnesses `Handing`, `Kindling` and `Flicker`.
  - `DissipatesOn.takes_of_gives` in `Dissipation`.
  - Study §20 and its English paragraph.
  - The record [generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md).
  - The chapter sentences on generation (§1 line 132, §2 lines 203 and 205, §8 line 429, §9 line 462).
- **P16 (`25a664245e26dcc4`).**
  - [Becoming.Wholes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Wholes.lean) in full.
  - Study §21 and its English paragraph.
  - The record [whole-persists-through-generation](../../../../theories/becoming/results/records/whole-persists-through-generation.md).
  - The chapter: §1 lines 131 and 142, §9 line 460 and glossary line 510.
- **P16b (`b24963f1`).**
  - The corrections answering J1–J11 of [BECOMING-P13-P14-P12B-REVIEW](BECOMING-P13-P14-P12B-REVIEW.md) in `Dissipation`, `Roles`, `Identity`, `Population`, `Correspondence`, `Flow` and the root module.
  - Study §22, the in-place corrections to §17–§20 and the English P16b paragraph.
  - The records no-finite-part-bears-taking, life-as-condition-of-life and identity-across-steps.
  - The chapter's §8 review row (line 431) and the plan rows 154–156.

**Isolation.** Every file was read from the object with `git show b24963f1:<path>` into the reviewer's scratch directory. Nothing in the live repository or its `.git` was modified. No `make` target or repository checker was run, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where reviews are filed.

**Materials** (sha256 prefixes at `b24963f1`):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` | `47e077148ea211a1` |
| chapter `THE-THEORY-OF-BECOMING.md` | `ea4892f2d269a648` |
| previous review `BECOMING-P13-P14-P12B-REVIEW.md` / plan `BECOMING-UNIFICATION-PLAN.md` | `d0f676a0375d5207` / `be28bfe28698ac5e` |
| `NONDUAL-METHOD.md` / `AGENTS.md` | `8c48b03a167a8909` / `da432369737e9a1f` |
| receipt `becoming-verification.json` / `check_becoming.py` | `54c294a996bace9e` / `18428f55cb88cab6` |
| `Becoming.lean` / package `README.md` | `c446f941c26b762d` / `2f0d986c1a3fcd33` |
| `Becoming/Roles` / `Dissipation` / `Wholes` | `4a4904e30fd94cf4` / `ba2eecfbcb551304` / `723a9ab162603e71` |
| `Becoming/Identity` / `Population` / `Correspondence` / `Flow` | `9b61a3e1f816a7df` / `602b84162f07c494` / `e34e6fa72be7ba9d` / `ef5a8bcfea44ff1a` |
| records generation-is-replenishment / whole-persists-through-generation | `e895cc1f063b777b` / `feef36d77092e7e1` |
| records life-as-condition-of-life / no-finite-part-bears-taking / identity-across-steps | `8dc7709c28f3d636` / `44908ea18c9fd685` / `80c8ae4abce552c5` |

**Read in full:**

- AGENTS.md, the nondual method and the sixth review.
- Study §20–§22 and the English P15, P16 and P16b paragraphs.
- `Wholes` in full; the `Roles` module doc, its P15 and P16b sections and their witnesses.
- The `Dissipation` doc and P16b additions.
- The `Identity` doc, `Fork`, `Merge` and `Dormant`.
- The five record JSONs named above.
- The chapter lines listed above, and the plan rows 150–156.

**Ren's words read**, for provenance:

- [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) (`740126fcca587edb`). The study and the two new records quote its line 12 exactly ("生生不息 - 一种整体的，不断创造更多生的方向").
- [recipient, money, pay](../../../../sources/15-codex-theory-conversations/2026-10-06-foundational-vocabulary-correction.md) (`222d407ab761a945`).

**No external literature was read.** Seeds, lineages, shifts and confluences are kinds of cases, not evidence.

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order.

- **Core.** The following 22 modules exit 0 from the prelude with no warnings:
  - `GenerativeCore`, with `import Std` removed as the checker does;
  - `InquirySufficiency` and `RelationalRenewal`;
  - `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Population, Identity, Wholes, Dissipation, Roles, Metaethics, Ranking, Correspondence}`;
  - the root module `Becoming`.
- **Bridge and periphery.** Not rebuilt (see "Not checked"). `Becoming.Bridge` is unchanged in `3828bcf8..b24963f1`, and its bytes match the receipt.

The checks:

- **Receipt.**
  - Status `passed`, Lean 4.29.1 `f72c35b3`, `core_compiles_from_prelude: true`, and `core_closure` of 22 modules.
  - All 35 `source_sha256` entries equal the object's files.
  - The 207 artifacts of the retained run `becoming-checks/20261009T071936.578078Z` match their recorded hashes.
  - The periphery receipt is `passed`.
- **Counts.**
  - Theorems per module: Frame 11, Inquiry 6, Renewal 6, Dependence 53, Return 29, Horizon 14, Joint 21, Substitution 7, Generation 30, Flow 60, Population 36, Identity 79, Wholes 26, Dissipation 55, Roles 110, Metaethics 35, Ranking 27, Correspondence 37 and Bridge 34, for 676 in all.
  - The 19 spine modules have 1065 declarations; Bridge's 50 make 1115.
  - Across the three commits the receipts show:
    - P15 adds 28 theorems to `Roles` and one to `Dissipation` (559 → 588, package 19 modules).
    - P16 adds `Wholes`, with 26 theorems (614, package 20).
    - P16b adds 62: Population +3, Identity +2 net (three list lemmas moved to `Population`), Dissipation +26, Roles +28 and Correspondence +3.
  - The study, the records and the chapter's §9 table agree.
- **Records.**
  - The 18 records changed in `3828bcf8..b24963f1` have 216 `references` hashes, and all equal the object's files.
  - All 53 proof bindings have `success_value` and `sha256_pointer`, resolved in their receipts, that equal the bound sources.
  - Four of the five records named above carry `reviewed_at_utc` 07:27:13Z. whole-persists-through-generation keeps 07:05:00Z, although its validation scope cites the run at 07:19:36Z (K8).
- **Names.**
  - `Aliases.lean` (`2f19e52285a0c856…`) runs `#check @` on all 335 aliases of the 18 records. 304 resolve in the core; the other 31 are 26 `Becoming.Bridge` names and the five `CorrectionInquiry` aliases of the Mathlib periphery reported by the sixth review.
  - `Names.lean` (`7ad18c36906fc9c6…`) does the same for the 959 qualified declaration names in the `references`. 892 resolve; the 67 that do not are 37 bridge, 19 inherited and 11 periphery declarations. None is a core declaration.
  - Every P15, P16 and P16b declaration resolves.
- **Axioms.**
  - `CoreAudit.lean` (`36943a92e907c9ed…`, 1185 lines generated from the receipt) prints the axioms of every declaration of the 22-module core closure.
  - `ProbeAudit.lean` (`8be909329fd0158f…`) does the same for all 57 probe declarations.
  - All 1242 report "does not depend on any axioms".

**Probes.** Three files import the unchanged `Becoming` and compile with exit 0 and no warnings:

| File | sha256 prefix | Theorems | Defs / inductives |
|---|---|---|---|
| `P15Probes.lean` | `262839035f9e6596` | 29 | 7 |
| `P16Probes.lean` | `fd7349f52e50d671` | 8 | 0 |
| `P16bProbes.lean` | `ebfd20f8babd19a3` | 9 | 4 |

The probes use term mode only: no tactic, no `simp`, `omega` or `decide`.

- In Lean 4.29.1, overlapping wildcard patterns in a `match` that defines a function, and `Nat.succ_ne_zero`, both report `propext`. The probes therefore list every case and use `Nat.noConfusion`.
- The probes are minimal models that satisfy the published definitions unchanged, or theorems over those definitions.
- Following the nondual method, they show what the definitions admit, not what actual systems do. A probe refutes a sentence only where the sentence claims more than the definitions give.

**Severity labels.**

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose is stronger than the Lean, including where a premise is left out.
- *missing counterexample*: a relevant witness is absent or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

The one *error* (K5) is a false claim in prose about a definition; no Lean statement is wrong.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P15: does generation carry a requirement of its own? | **Yes.** `given_of_arises` and `replenishes` need only balance and `Embodied`, and `generation_needs_replenishment` uses no uptake at all, which is what the fifth review's I3 asked for. Rebuttal 1 honestly calls it near-definitional. | — |
| 2. P15: does `generation_opens` say "no finite part bears it alone / the family must exchange beyond itself"? | **No.** It says that the family is not closed at arbitrarily late steps. `Dissipative` binds only enclosed steps, so a sink unrelated to the family both makes dissipation vacuous and meets the conclusion, while the family carries generation alone (`SprayHanding`). The inflow reading holds under an enclosure around the family (`generation_draws_in`, formalized here). | K1 |
| 3. P15: do `generation_ceases` and `arising_lowers` need `Enclosed`? | **No.** `arising_lowers` assumes the family closed. `generation_ceases` closes the finite world `all` directly, so every step is enclosed. Both hold and are correctly glossed. | — |
| 4. P15: is "under dissipation a giver to a family takes from it" right? | **Only for a family dissipated on, hence closed.** The record and the §20 table say so; the §20 bullet, the English paragraph and the chapter drop it (`Frontier.gives_without_taking`). | K2 |
| 5. P15: are `Handing`, `Kindling` and `Flicker` genuine? | **Yes.** `Kindling` is enclosed around the sides at every step (`Kindling.around`), so the corrected inflow theorem applies to it non-vacuously (`Kindling.draws_in`). That `Handing` shows dissipation needed is right, but the premise actually needed is dissipation on an enclosure around the family (`SprayHanding` keeps `Handing`'s behaviour under vacuous dissipation). | K1 |
| 6. P16: do `Whole` and its theorems say "整体的持续就是部分的生成"? | **They say "persists only through".** The zh "就是" claims identity, and `Gaps` refutes it. `Whole` is coincidence of activity (`whole_self`, `each_other`), and `arises_within` and `needs_arising` use only one direction (`arises_within_of_cover`, `needs_arising_of_cover`). Under `Brief`, two parts re-arising suffice (`Layered`); under `Ends` and `Listed`, ever-new parts must arise (`needs_new`). | K3 |
| 7. P16: are `Brief`, `Ends` and `Listed` disclosed correctly? | **In the theorems, the zh chapter §1, the root doc and the record's hypotheses, yes.** The record title, the chapter's English §1, the §9 row and the glossary say "parts do not last" and drop `Listed`, which `Countless` shows is needed. | K4 |
| 8. P16: are the rebuttals right? | **Rebuttal 3 is false about `Layered`**: its members are `Brief 1`, and `arises_within` applies (`layered_brief`, `layered_within`). Rebuttals 1, 2, 4 and 5 are right. | K5 |
| 9. P16b: are J1–J11 closed? | **Eight are closed. J1 and J7 are closed with an overclaim, and J11 with residues.** See the table below. | K1, K6, K8 |
| 10. P16b: new overclaims in relabel, `roles_dissipative`, `arises_from_embodied`, `Fork`, `Merge`? | **`relabel` with `onto` is correct and more general than the involution the review used** (injectivity is not needed). **`roles_dissipative` holds both ways, beyond what the review formalized.** **`Fork` is genuine.** **`arises_from_embodied` holds**; its premise is global where a local one would do, and "生由生 proved" reads embodiment as life. **`Merge`'s unceasing arising is spurious**: a persisting grower arises at every step. | K6, K7 |
| 11. P16b: `Enclosed`, `gives_less`, `giving_needs_uptake`, `Spray`, `Lone`, `Rooted` | **Correct.** The `gives_less` gloss drops "without repetition" (`repeated_family`). §22.4's claim that `Frontier`, `Rooted` and `Lone` are enclosed at every step is true (`Frontier.enclosed`, `Lone.enclosed`) but was unproved. | K8 |
| 12. Nondual method; Ren's choices; vocabulary | **No reading of succession, ending or the level of 生生不息 is chosen for Ren, and names are left as suggestions.** K6 reads 生 as embodiment. "giver" (a word the fifth review's I4(d) had removed) returns in P16b, and "付出" survives once. | K3, K6, K8 |
| 13. Records, receipt and counts | **Correct** (676 / 1115, run `20261009T071936.578078Z`, closure 22, package 20), with bookkeeping in K8. | K8 |

**Status of J1–J11.**

| Item | Status | Evidence |
|---|---|---|
| J1 | closed, with an overclaim | `Enclosed`, `enclosed_of_finite`, `gives_less`, `giving_needs_uptake` and `Spray` are in the core and the record. The Dissipation doc (lines 38–40) and the P13 claim ("越出的交换可以与家族无关") disclose the pattern for taking. The P13 title still reads "no finite part bears continued taking alone … must exchange beyond itself", which `SprayHanding.taking_opens_anyway` with `sides_within` refutes. P15's generation sentences repeat the pattern without the disclosure (K1). |
| J2 | closed | `Lone.lone` and `Lone.frontier` are in the core; §17, the chapter and the record are restated for any recurring uptake. |
| J3 | closed | `Rooted.rooted` (all premises jointly, `opens_of_arising` instantiated) and `witnesses_not_dissipative`. |
| J4 | closed | `relabel` (onto), `relabel_dependent`, `relabel_undermining`, `relabel_alive`, the two valuation connections, `apart_relabelled` and `Wilting.relabelled_not_embodied`. The prose now says that the identification is supplied by the shared index. |
| J5 | closed | `Mutualism.apart_embodied`; the omission is disclosed in §18 and the record. |
| J6 | closed | `Wilting.wilting` and `SelfBearing.met_iff`; the scope of Ren's choice (bystanders, natural endings, the life's own last event) is stated. |
| J7 | closed, with an overclaim | `arises_given` retitled, `SunSeed.sun_gives` and `arises_from_embodied`. §22.1, §22.3 item 4 and the record's correspondence present "生由生" as proved, reading embodied as living (K6). |
| J8 | closed | `roles_acting`, `roles_taking`, `roles_census`, `roles_distinct` and `roles_dissipative` (iff); "列出的读法"; the boundary clause dropped. |
| J9 | closed | `Fork.split_unceasing`; "sufficient, not necessary" in §19, the chapter and the record. |
| J10 | closed | `Dormant.no_split_without_arising`; census, distinctness and `Taking` restored in chapter §1 and §8 and the record title; balance and `Acting` restored for `arises_given`. `no_join` and `decideContinues` are in the core. `Merge` is weaker than the sixth review said (K7). |
| J11 | closed, with residues | (a) The §8 row is updated. (b) The count basis is disclosed, but the P15 and P16 paragraphs still say "core". (c) and (d) are done. (e) Done except §20's "付出" and the plan's `Brood.costless`. (f) The two stamps are refreshed, and whole-persists is now stale (K8). |

## 2. Findings

### K1. overclaim (undisclosed premise): `generation_opens` can be met by exchange unrelated to the family

**Location.**

- `Web.generation_opens` docstring (Roles.lean:588–590): "generation in it needs exchange beyond it".
- Root `Becoming.lean:82–84`: "so under dissipation generation that recurs in a finite family needs exchange beyond it".
- Study §20, in four places:
  - the introduction (line 1160): "在有限家族中复现的生成于是需要与家族之外交换";
  - the table row (line 1190): "在其中复现的生成需要在任意晚的步与家族之外交换";
  - the bullet heading (line 1201): "耗散之下，生成不由有限部分独自承担";
  - "对生生" (line 1204): "不息的生起不能由任何有限的部分独自承担，须由越出每个有限部分的展开承担".
- English P15 paragraph (line 1489).
- Chapter §2 zh (line 203): "体现的生成在一个有限家族中复现，家族就须在任意晚的步与其外交换"; en (line 205): "a finite family in which embodied generation recurs must exchange beyond itself".
- Chapter §8 row (line 429) and §9 Roles row (line 462).
- Record generation-is-replenishment:
  - title, zh "在耗散之下没有有限部分独自承担它" and en "under dissipation no finite part bears it alone";
  - correspondence: "under dissipation unceasing arising cannot be borne by any finite part";
  - hypothesis 3: "this result's conclusions under dissipation all concern closed finite families".
- Plan row P15 (line 154).
- For J1, the P13 record title: "Under dissipation no finite part bears continued taking alone: … must exchange beyond itself".

**What the Lean says.**

- `generation_opens` concludes `¬ ∀ t, T ≤ t → L.ClosedAt ds t`. At arbitrarily late steps, some formation taking part exchanges with something outside `ds`.
- Nothing ties that exchange to `ds` or its members. `Dissipative` binds only steps at which some finite family is closed (J1).
- `generation_ceases` is unaffected: there `all` is closed at every step.

**Evidence.** `SprayHanding.spray_handing`. The relata are the two sides of `Handing`, a sink, and auxiliary relata `aux n`.

- The sides hand one standing back and forth exactly as in `Handing`.
- The sink is always active and takes one unit from, and gives one unit back to, every auxiliary relatum. The auxiliary relata stand at one and are never active.
- The flow balances, only active relata give, and activity needs support. The sides are embodied and bear on themselves.
- No step is enclosed (`unenclosed`, from `fresh`), so `Dissipative` holds vacuously.
- Each side arises at arbitrarily late steps.
- Every relatum that gives to the family takes only from it. The sink never takes from or gives to a side, and the family's stock is one at every step.
- `opens_anyway` derives `generation_opens`'s conclusion for this flow.
- `sides_within`: the sides exchange only with each other.
- `takes` and `taking_opens_anyway`: taking from the sides recurs, and the conclusion of `Dissipative.opens` (P13) holds by the same sink.
- `not_around`: no enclosure contains the family.

**Why it matters.**

- `Handing` is the study's witness that, without dissipation, embodied generation can be unceasing in a closed finite world. `SprayHanding` is `Handing` with an unrelated sink added. In the sense of the definitions, that sink makes the flow dissipative, while the family still bears its generation alone.
- The theorem's conclusion is met by the sink. The glosses ("needs exchange beyond it", "no finite part bears it alone", "须由越出每个有限部分的展开承担") claim that the family receives from outside, which is false here.
- P16b disclosed exactly this for taking (Dissipation.lean:38–40: "The exchange beyond the family need not touch the family"; the P13 claim "越出的交换可以与家族无关"). It did not carry the disclosure into P15, and the P13 title keeps the old wording.
- The record's hypothesis 3 cites `Spray` for the vacuity of dissipation, but not for the conclusion, and then says that the conclusions under dissipation all concern closed families. `generation_opens` concerns a family that is not closed.

**Correction.** Formalized here in `P15Probes.lean`:

- `Around L ds t`: a finite family without repetition containing `ds` is closed across `t`.
- `Inward L ds t`: every formation taking part that gives to `ds` takes only from `ds`.
- `total_le_of_support` (a lemma) and `dissipatesOn_of_inward`: under dissipation, a family that is enclosed around and receives nothing from outside is dissipated on.
- `taking_draws_in`: under dissipation, if taking from `ds` recurs and `ds` is enclosed around from some step on, then at arbitrarily late steps some formation gives to `ds` and takes from beyond it.
- `generation_draws_in`: the same for embodied arising in `ds`.
- Both are non-vacuous:
  - `Kindling.around` and `Kindling.draws_in`: the holder burns fuel.
  - `Frontier.around` and `Frontier.draws_in`: the sun burns fuel.
- `around_of_finite` covers the finite world.
- `Enclosed` at a step gives `Around` for any finite family once equality is decidable (append the family and remove duplicates). This step is not formalized here.

With these in the core, the titles can read zh "在耗散之下，一步的交换落在有限个关系项之内时，体现的生成在有限家族中复现，就在任意晚的步从家族之外流入" / en "under dissipation, where each step's exchange lies within finitely many relata, a finite family in which embodied generation recurs draws in from beyond it at arbitrarily late steps".

Until then:

- Restrict the glosses to the literal conclusion: "从任何一步起都不封闭：在任意晚的步有参与者与其外交换；这一交换可以与家族无关（`SprayHanding`）".
- Add `SprayHanding` to the record's counterexamples.
- Correct hypothesis 3, since `generation_opens` is about non-closure.
- Retitle P13 likewise.

### K2. overclaim (omitted premise): "under dissipation a giver to a family takes from it"

**Location.**

- Study §20 bullet (line 1201): "耗散之下，生成不由有限部分独自承担。给予家族者从家族取用".
- English P15 paragraph (line 1489): "Under dissipation a formation giving to a family takes from it (`DissipatesOn.takes_of_gives`)".
- Chapter §2 zh (line 203): "在耗散之下，给予者从家族取用"; en (line 205): "Under dissipation the giver takes from the family".

**What the Lean says.** `DissipatesOn.takes_of_gives` assumes `L.DissipatesOn ds t`, and `Dissipative` yields that only for a family without repetition that is closed across `t`.

**Evidence.** `Frontier.gives_without_taking`. The frontier is dissipative (`Frontier.dissipative`). At every step after the first, the sun gives the pool `t + 1 > 0` and takes nothing from `[pool]`; the family `[pool]` is not closed, because the sun burns fuel.

**Why it matters.** This sentence is the hinge of the derivation in §20. The record ("a family dissipated on") and the §20 table ("被耗散时") state it correctly, but the three summaries drop it. Read literally, the summaries would yield the inflow reading of K1 without any enclosure, which `SprayHanding` refutes.

**Correction.** zh "给予被耗散的（跨该步封闭的不重复）家族者从家族取用"; en "a formation giving to a family dissipated on (closed across the step, without repetition) takes from it".

### K3. overclaim: "整体的持续就是部分的生成" and what `Whole` states

**Location.**

- Study §21 heading (line 1220) and the bullet "整体的持续就是部分的生成" (line 1260).
- §21 "对生生" (line 1263): "在部分不长久的前提下，这一张力消失：谱系的持续蕴含成员不断生起，整体的“不息”正由部分的“生生”构成".
- Record whole-persists-through-generation: zh title "整体的持续就是部分的生成" (en "persists through"); correspondence "the whole's 不息 is made of its parts' 生生".
- Chapter §1 zh (line 131): "部分就不断生起：整体的持续就是部分的生成" and "部分与整体的关系由整体陈述".
- Wholes.lean:7–8: "This module states that part–whole relation".

**What the Lean says.**

- `Whole parts w := ∀ t, active t w ↔ ∃ p, parts p ∧ active t p`.
- `arises_within` and `needs_arising` derive arising of parts from persistence of `w`, a necessary condition. Both use only the `→` direction of `Whole`.
- `Gaps` shows that the converse fails.

**Evidence.**

- **Identity versus necessity.** `Gaps` (the paper's own) refutes "就是", and the study says so one bullet later. The English title uses "through". Since Chinese and English are equally primary, the Chinese overstates.
- **Coincidence, not constitution.** `whole_self`: every formation is the whole of itself. `each_other`: in `Immortal.web`, `false` is the whole of `true` and `true` is the whole of `false`.
- **The `←` direction is idle.** `arises_within_of_cover` and `needs_arising_of_cover` prove both theorems from "some part is active at every step from `T` on", with no whole at all.
- **Under `Brief`, generation can be re-arising.** In `layered_two`, every arising in `Layered` is the arising of `first` or `second`, and neither part's activity ends, while the lineage is active at every step.
- **Under `Ends` and `Listed`, new parts must arise.** `needs_new`: for every finite list of parts, parts outside it arise at arbitrarily late steps. This corollary of `needs_arising` is stronger than anything the module states.

**Why it matters.**

- "张力消失" claims that the persistence reading entails what §19 found missing: "不断创造" in Ren's words.
- Under `Brief`, persistence entails only that the same finitely many parts keep re-arising (`Layered`), and nothing new is created.
- Under `Ends` and `Listed`, it entails ever-new parts (`needs_new`), but not more of them: `Generations` has two alive at every step.
- "构成 / is made of" reads constitution into a relation of co-activity. "This module states that part–whole relation" presents the supplied relation as the relation itself. This is the I7/J4 pattern again, though record hypothesis 1 discloses "only through activity".

**Correction.**

- zh "整体的持续需要部分的生成" or "整体经由部分的生成而持续".
- §21 "对生生": "在 Ends 与 Listed 之下，谱系的持续蕴含越出任何有限成员列表的新成员不断生起（`needs_new`）；在 Brief 之下只蕴含成员反复生起（`Layered`）；两者都不蕴含数目增长".
- Wholes.lean: "This module states one part–whole relation, coincidence of activity".
- Move `needs_new` and the cover forms into `Wholes`.

### K4. overclaim (omitted premise): "parts that do not last" drops `Listed`

**Location.**

- Record whole-persists-through-generation title: en "where parts do not last, a persisting whole needs its parts to keep arising"; zh "部分不长久时，持续的整体需要部分不断生起".
- Chapter summary bullet (line 142): "a whole that persists through parts that do not last persists only through their generation".
- §9 Wholes row (line 460): "持续的整体，若部分不长久，需要部分不断生起".
- Glossary (line 510): "部分不长久时，整体的持续需要部分不断生起".
- Record hypothesis 2 and study §21 "Supplied premises": "Brief，或 Ends 与 Listed，是对部分不长久的陈述".

**What the Lean says.** `needs_arising` needs both `Ends` and `Listed`.

**Evidence.** In `Countless.countless` (the paper's own), every part ends, the whole persists at every step, and nothing ever arises.

**Why it matters.** `Listed` is a finiteness premise, not a statement about lasting; §21's own bullet "为什么需要不长久与有限" keeps the two apart. Folding `Listed` into "do not last" makes the titles false of `Countless`, whose parts each end. The zh chapter §1 (line 131) and the root doc (`Becoming.lean:68–70`) state the premise correctly.

**Correction.** Use zh "部分不长久且同时活跃的部分有限时" and en "where parts do not last and finitely many are active at once". Alternatively, name the two premises: "部分短暂（Brief），或部分终结且可有限列出".

### K5. error (in prose): §21 rebuttal 3 on `Layered`

**Location.** Study §21, rebuttal 3 (line 1271): "`Layered` 的成员隔一步就再活跃，`Ends` 与 `Brief` 都不成立，两个定理都不适用".

**What the Lean says.** `Layered.web`: `first` is active iff `odd t = false` and `second` iff `odd t = true`, with `odd (t + 1) = !odd t`.

**Evidence.**

- `layered_brief`: both members are `Brief 1`.
- `layered_within`: `Whole.arises_within` with `d = 1` applies to `Layered.composed`, so a member arises at every step.

**Why it matters.**

- The rebuttal asserts something false about a definition, using the paper's own witness. The members fail `Ends` but satisfy `Brief`, and one of the two theorems applies.
- The conclusion "premises sufficient, not necessary" may still be true, but this witness does not show it.
- It also hides the point of K3: `Brief` does not say that parts end, and it admits the same parts arising again.

**Correction.**

- "`Layered` 的成员满足 `Brief 1`，`arises_within` 适用：每一步都有成员生起；它们的活动不终结，`needs_arising` 不适用。所以 `Brief` 不说部分终结，它允许同样的部分反复生起。"
- A witness that the premises are not necessary needs parts whose activity spells grow without bound, so that they are `Brief` for no `d`, never end, and keep the whole active. That witness is not built here.

### K6. overclaim (a reading chosen for Ren): "生由生" stated as proved

**Location.**

- Study §22.3 item 4 (line 1355): "“生由生”在只有体现者给予的前提下证明（`arises_from_embodied`）".
- §22.1 J7 row (line 1316): "“生由生”只在所述前提下成立，写为对应".
- Record life-as-condition-of-life correspondence (en): "which is a life only where only lives give (arises_from_embodied)".
- Roles.lean:966–968, the `SunSeed` docstring: "the giver `arises_given` names need not be a life", which treats "embodied" and "a life" as one.

**What the Lean says.**

- `Embodied.arises_from_embodied` assumes `givers : ∀ t f c, f ∈ L.present t → 0 < L.give t f c → W.Embodied f`. Its conclusion is that the giver to an arising embodied `x` is embodied and stands at a positive level.
- `Embodied f := ∀ t, active t f ↔ 0 < level t f`.

**Evidence.** `EmbodiedSun.embodied_sun`. Take `SunSeed` with the sun's level set to one.

- Every premise holds, and the theorem names the sun: it is embodied, and it stands at one while it gives.
- The sun requires nothing, draws on nothing, takes nothing and does not bear on itself.

**Why it matters.**

- The theorem proves "embodied from embodied, where only embodied relata give". Beyond `arises_given`, its content is the premise applied to the giver.
- Reading "embodied relatum" as 生 is a reading of 生 and of living. That reading is Ren's: generation-is-replenishment's `next_delta` lists "生成在多大程度上必须读作体现（Ren）", and the chapter's §8 row (line 429) lists "生成在多大程度上读作体现（Ren）".
- The chapter labels its sentence as an AI reading. §22.1, §22.3 and the record correspondence instead state it as what was proved.
- The sixth review's §4 item 4 ("'life from life' proved under a stated premise that only lives give") wrote "lives" for "embodied relata" first. This review corrects that wording.

**Correction.**

- "在只有体现的关系项给予这一表示前提下，体现关系项的给予者也体现（`arises_from_embodied`）；把体现的关系项读作“生”，是 AI 读法，属于 Ren 对“生”的读法".
- In the record: "which is embodied only where only embodied relata give".
- Optionally, weaken the premise to the givers of `x` across `t`.

### K7. missing counterexample (witness strength): `Merge` arises without "more"

**Location.**

- Identity.lean:924–926 (`Merge.merging` docstring): "with no split and the garden's census, more without end makes formations arise under it at arbitrarily late steps".
- Identity doc (line 83): "and so is one with merges (`Merge`)".
- Study §22.1 J10 row and §22.2 (line 1336): "形成在任意晚的步生起".
- Record identity-across-steps counterexample: "含合并的延续下定理非空地适用（Merge.merging）".
- Sixth review, verdict 11: "non-vacuous … including under merges".

**What the Lean says.** `Merge.merges _ g f := f = (.renewer, g.2)`. No formation continues as a grower, so every grower active after a step continues nothing.

**Evidence.**

- `merge_idle`:
  - `(grower, 0)` arises under `merges` across every step `N`;
  - `UnceasingFrom merges` therefore holds with no use of `More`;
  - under the identity continuation, the same grower arises only across step zero.
- On `Garden.web` every formation stays active once it starts. A merge without a split therefore forces some formation that is still active to count as arising: n sources can cover at most n − 1 old targets once two of them merge. This counting argument is not formalized here.
- `Confluence.confluence` is a proper witness:
  - `a` and `b`, both active at step zero, continue as `b`, and `a` is not active afterwards;
  - there is no split;
  - every arising under the continuation is the new formation of its step, and one arises at every step.

**Why it matters.** `Merge` is cited to show that `More.unceasingFrom` tolerates merges. Its conclusion holds for a reason unrelated to "more": a persisting formation is re-read as new at every step. The sixth review made this claim with the same relation, and P16b moved it into the core; the error is that review's.

**Correction.**

- Gloss `Merge` as "the premises hold under a continuation with merges; on the garden, whose formations never end, merges come with formations re-read as arising".
- Add a witness in which the merged formation ends, as `Confluence` does.
- A census witness in which `More.unceasingFrom` does the work under a merge would be a new result.

### K8. presentation: bookkeeping and vocabulary

- **(a) "付出".** Study §20 introduction (line 1160): "在耗散之下，补充须付出所取". The paragraph carries a P16b wording marker but keeps this phrase. Use "给予须以取用为条件".
- **(b) Plan.** The P15 row (line 154) still cites `Brood.costless`, which no longer exists, and "体现的生成复现的有限家族须与其外交换" (K1).
- **(c) "giver".**
  - P16b raises the lines containing "giver" in Roles.lean from 0 to 6 and adds a hypothesis named `givers`. Lines containing "giver / 给予者" go from 2 to 4 in the chapter and from 7 to 17 in the study (some of the latter quote the sixth review).
  - The fifth review's I4(d) had renamed "giver". Ren questioned "recipient, money, pay" as foundational vocabulary on 2026-10-06, and "giver" is the counterpart of "recipient".
  - This is a consistency point only; Ren decides. "给予的关系项 / the relatum that gives" and `gives_embodied` would avoid the role noun.
- **(d) "No step is enclosed."** Dissipation.lean:24–25: "Where a formation exchanges with infinitely many conditions, no step is enclosed". The accurate form is: "a step is not enclosed when some formation taking part in it exchanges with infinitely many conditions".
- **(e) `gives_less` without "without repetition".** This affects the study Delta (line 1289, "在封闭家族上取得多于所给") and §22.2 (line 1327). `repeated_family`: in `Lone`, the family `[pool, pool, fuel t]` is closed across `t`, and the sun gives it two units while taking two.
- **(f) An unproved "every step".** §22.4 rebuttal 1 (line 1363) says "`Frontier`、`Rooted` 与 `Lone` 每步都满足它". It is true but was not stated in the core. `Frontier.enclosed` covers `Rooted`, which shares `Frontier.flow`, and `Lone.enclosed` covers `Lone`.
- **(g) Stamp.** whole-persists-through-generation keeps `reviewed_at_utc` 07:05:00Z, set at P16, although P16b changed its validation scope to the run at 07:19:36Z. The other four changed Becoming records are at 07:27:13Z.
- **(h) "Core".** The English P15 and P16 paragraphs (lines 1489, 1491) say "The core now has 588 … over 19 modules" and "614 … over 20 modules"; these count the package. The P16b bullet discloses this, but the word "core" stands in place.

## 3. What remains sound

- **The theorems.**
  - Every P15, P16 and P16b theorem holds as stated.
  - The 22-module core recompiles from the prelude, and all 1185 declarations have empty axiom reports.
  - The counts, receipt, hashes, aliases, bindings and retained artifacts are correct.
- **P15.**
  - Generation now carries a requirement of its own without any uptake. `given_of_arises`, `replenishes` and `generation_needs_replenishment` answer I3, and rebuttal 1 calls this near-definitional.
  - `takes_of_gives` and `arising_lowers` correctly derive the physical premise of `dissipation_ceases` for embodied arising in closed families.
  - `generation_ceases` is correct and needs no further premise.
  - `Handing`, `Kindling` and `Flicker` are genuine. `Kindling` is enclosed around its family, so the corrected inflow theorem applies to it.
  - `Embodied` is disclosed as a representational premise, together with its limits for remains, seed banks and dormancy (rebuttal 5).
- **P16.**
  - The definitions are clean, and `arises_part` and `parts_unceasing` use both directions of `Whole`.
  - The boundary witnesses form a complete set: the bound is attained (`Shifts`), each premise is needed (`Immortal`, `Countless`), the premises are consistent (`Generations`), and the converse fails (`Gaps`).
  - The boundary "整体只由活动关联部分" and the level of 生生不息 are left honestly open.
  - `needs_arising` is stronger than stated (`needs_new`), which supports a better form of the study's reading.
- **P16b.**
  - `Enclosed`, `gives_less` and `giving_needs_uptake` are what J1 asked for, and the Dissipation doc discloses `Spray`.
  - `Lone`, `Rooted` and `witnesses_not_dissipative` are in the core.
  - `relabel` with `onto` is more general than the review's involution.
  - The `roles_*` theorems hold, including both directions of `roles_dissipative`.
  - `Wilting` and `met_iff` show Ren the scope of the choice about endings.
  - `SunSeed`, `Fork`, `Dormant.no_split_without_arising`, `no_join`, `decideContinues` and `apart_embodied` are correct.
  - Corrections are made in place, marked, and keep their original wording.
- **Method and provenance.**
  - Ren's words are quoted exactly, and AI readings are labelled.
  - The readings of succession and ending, the level of 生生不息 and the names are left to Ren.
  - No ethical predicate, ranking or axiom enters.

## 4. What would change these verdicts

1. **Inflow (K1, K2).** Any one of these:
   - state `Around` (or `Enclosed` with decidable equality) and the inflow theorems in the core, with `Kindling` and `Frontier` as witnesses;
   - restrict every generation and P13 title to the literal conclusion, add `SprayHanding` to the record and correct hypothesis 3.

   In either case, restore "dissipated on" in the three summaries.
2. **Wholes (K3–K5).**
   - Write "需要／经由" for "就是".
   - State `needs_new` and the cover forms.
   - Restate the "张力" sentence premise by premise.
   - Add `Listed` (or name `Brief`) in the titles, §9 and the glossary.
   - Correct rebuttal 3 with `layered_brief`.
   - Describe `Whole` as coincidence of activity.
3. **Giving (K6).** Drop "生由生 proved", state "embodied from embodied under the premise that only embodied relata give", and leave to Ren whether embodied relata are 生.
4. **Merges (K7).** Re-gloss `Merge`, and add a witness in which the merged formation ends.
5. **Bookkeeping (K8).** The eight items.
6. **Ren's choices.** These stay open and are not settled here:
   - the reading of 生 and of living, including whether embodied relata are 生;
   - the reading of succession;
   - at which level 生生不息 is read;
   - whether drawing at an ending counts, and for which drawers;
   - the names: `Depletes`, the cost wording, `Brood.not_dissipative` and "giver".
7. A finding would also fall if its probe misread a published definition. Every probe imports the unchanged `Becoming`, and each uses the definitions as they stand at `b24963f1`.

**Not checked.**

- `Becoming.Bridge` and the Mathlib periphery were not rebuilt. The bridge's 50 declarations were not re-audited here; its bytes are unchanged and match the receipt. Its 26 aliases and the five periphery aliases did not resolve, nor did 67 declaration names (37 bridge, 19 inherited, 11 periphery).
- The generated overview pages and `make research-check` were not run, since they write into the live repository.
- No external literature was consulted.
- Parity between the Chinese and English texts was checked only for the passages quoted above.
- The following were not built:
  - the step from `Enclosed` to `Around`, which needs decidable equality;
  - a census witness in which `More.unceasingFrom` works under a merge with an ending formation;
  - a witness that the P16 premises are not necessary;
  - the counting argument that merges on `Garden` force re-arising.

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 against the unchanged `b24963f1` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. The three probe files compile with exit 0 and no warnings. `ProbeAudit.lean` prints the axioms of all 57 probe declarations, and every one reports "does not depend on any axioms". `CoreAudit.lean` (1185 `#print axioms` lines generated from the receipt), `Aliases.lean` (335 `#check @` lines) and `Names.lean` (959) are mechanical and are not reproduced; their hashes and results are in §0.

### `P15Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P15, P16 and P16b: the P15 part

Each probe is a minimal model satisfying the published definitions at `b24963f1`
unchanged, or a theorem over them. It shows what the definitions admit, not what actual
systems usually do.
-/

namespace P15Probe

open Becoming

/-! ## K1. Where no step is enclosed, recurring embodied generation in a finite family
needs no exchange with anything beyond it -/

namespace SprayHanding

/-- The two sides of `Handing`, a sink, and auxiliary relata. -/
inductive Relatum where
  | side (x : Bool)
  | sink
  | aux (n : Nat)

/-- The holder hands its standing to the other side, as in `Handing`; the sink takes one
unit from every auxiliary relatum and gives it back. -/
def flow : Flow Relatum Relatum where
  present t := [.side (Handing.holder t), .sink]
  take t f c := match f, c with
    | .side x, .side y => Handing.flow.take t x y
    | .side _, .sink => 0
    | .side _, .aux _ => 0
    | .sink, .side _ => 0
    | .sink, .sink => 0
    | .sink, .aux _ => 1
    | .aux _, _ => 0
  give t f c := match f, c with
    | .side x, .side y => Handing.flow.give t x y
    | .side _, .sink => 0
    | .side _, .aux _ => 0
    | .sink, .side _ => 0
    | .sink, .sink => 0
    | .sink, .aux _ => 1
    | .aux _, _ => 0

/-- The sides stand and are active as in `Handing` and depend on themselves at need one;
the sink is always active and stands at one; auxiliary relata stand at one and are never
active. -/
def web : Web Relatum Relatum where
  level t c := match c with
    | .side x => Handing.stands x t
    | .sink => 1
    | .aux _ => 1
  active t c := match c with
    | .side x => 0 < Handing.stands x t
    | .sink => True
    | .aux _ => False
  requires _ c d := match c with
    | .side _ => d = c
    | .sink => False
    | .aux _ => False
  need _ _ _ := 1
  draws _ f c := match f, c with
    | .side _, _ => False
    | .sink, .side _ => False
    | .sink, .sink => False
    | .sink, .aux _ => True
    | .aux _, _ => False

/-- The family of the two sides. -/
def sides : List Relatum := [.side true, .side false]

theorem sides_distinct : Distinct sides :=
  ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩

/-- One more than the largest auxiliary index in a list. -/
def bound : List Relatum → Nat
  | [] => 0
  | .aux n :: l => n + 1 + bound l
  | .side _ :: l => bound l
  | .sink :: l => bound l

theorem le_bound {m : Nat} : ∀ {l : List Relatum}, Relatum.aux m ∈ l → m + 1 ≤ bound l
  | _ :: l, .head _ => Nat.le_add_right (m + 1) (bound l)
  | .aux n :: l, .tail _ mem => Nat.le_trans (le_bound mem) (Nat.le_add_left (bound l) (n + 1))
  | .side _ :: l, .tail _ mem => le_bound (l := l) mem
  | .sink :: l, .tail _ mem => le_bound (l := l) mem

/-- Every finite list of relata misses an auxiliary relatum. -/
theorem fresh (l : List Relatum) : ¬ Relatum.aux (bound l) ∈ l :=
  fun mem => Nat.not_succ_le_self _ (le_bound mem)

theorem balances : flow.Balances web
  | t, .side y => Handing.balances t y
  | _, .sink => rfl
  | _, .aux _ => rfl

theorem acting : flow.Acting web := fun t f _ present _ => match f, present with
  | _, .head _ => Handing.holder_stands t
  | _, .tail _ (.head _) => trivial
  | _, .tail _ (.tail _ no) => (nomatch no)

theorem dependent : web.Dependent := fun _ c active d depends => match c, d, depends with
  | .side _, _, rfl => active

/-- No step is enclosed: the sink exchanges with an auxiliary relatum outside every
finite list. -/
theorem unenclosed (_t : Nat) : ¬ flow.Enclosed _t :=
  fun ⟨E, _, closed⟩ =>
    Nat.noConfusion ((closed .sink (.tail _ (.head _)) (.aux (bound E)) (fresh E)).1 : (1 : Nat) = 0)

theorem dissipative : flow.Dissipative :=
  fun E t distinct closed => absurd ⟨E, distinct, closed⟩ (unenclosed t)

theorem even_sum : ∀ t, Handing.even t + Handing.even (t + 1) = 1
  | 0 => rfl
  | 1 => rfl
  | t + 2 => even_sum t

/-- The flow balances, only active relata give, activity needs support, the sides are
embodied and bear on themselves, and the flow is dissipative, vacuously, since no step is
enclosed. Each side arises at arbitrarily late steps in the finite family of the two
sides. Yet every relatum that gives to the family takes only from the family, the sink,
the only relatum exchanging beyond it, never takes from or gives to it, and the family's
stock is one at every step: generation recurs in a finite family that exchanges with
nothing beyond it. -/
theorem spray_handing :
    flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧
    (∀ x, web.Embodied (.side x) ∧ web.SelfBearing (.side x)) ∧ flow.Dissipative ∧
    (∀ t, ¬ flow.Enclosed t) ∧ (∀ x N, ∃ t, N ≤ t ∧ web.Arises t (.side x)) ∧
    (∀ t f, f ∈ flow.present t → 0 < total sides (flow.give t f) →
      ∀ c, 0 < flow.take t f c → c ∈ sides) ∧
    (∀ t x, flow.take t .sink (.side x) = 0 ∧ flow.give t .sink (.side x) = 0) ∧
    ∀ t, web.stock sides t = 1 :=
  ⟨balances, acting, dependent, fun _ => ⟨fun _ => Iff.rfl, fun _ _ => ⟨rfl, Nat.zero_lt_one⟩⟩,
   dissipative, unenclosed, fun x N => Handing.recurs x N,
   fun _ f present gives c takes => match f, present with
    | _, .head _ => match c, takes with
      | .side true, _ => .head _
      | .side false, _ => .tail _ (.head _)
      | .sink, takes => absurd takes (Nat.lt_irrefl 0)
      | .aux _, takes => absurd takes (Nat.lt_irrefl 0)
    | _, .tail _ (.head _) => absurd gives (Nat.lt_irrefl 0)
    | _, .tail _ (.tail _ no) => (nomatch no),
   fun _ _ => ⟨rfl, rfl⟩, even_sum⟩

/-- The conclusion of `Web.generation_opens` holds here, by the theorem itself: the family
of the sides is not closed from any step on. Its openness is the sink's exchange, which
never touches the family. -/
theorem opens_anyway (T : Nat) : ¬ ∀ t, T ≤ t → flow.ClosedAt sides t :=
  Web.generation_opens balances dissipative sides_distinct
    (fun N => match Handing.recurs true N with
      | ⟨t, later, arises⟩ => ⟨t, .side true, later, .head _, fun _ => Iff.rfl, arises⟩) T

/-- The sides exchange only with the sides. -/
theorem sides_within : ∀ t x c,
    (0 < flow.take t (.side x) c ∨ 0 < flow.give t (.side x) c) → c ∈ sides
  | _, _, .side true, _ => .head _
  | _, _, .side false, _ => .tail _ (.head _)
  | _, _, .sink, .inl pos => absurd pos (Nat.lt_irrefl 0)
  | _, _, .sink, .inr pos => absurd pos (Nat.lt_irrefl 0)
  | _, _, .aux _, .inl pos => absurd pos (Nat.lt_irrefl 0)
  | _, _, .aux _, .inr pos => absurd pos (Nat.lt_irrefl 0)

/-- Taking from the sides recurs at every step: the holder takes its own unit. -/
theorem takes (t : Nat) : 0 < flow.takers sides t :=
  show 0 < sign (total sides (flow.take t (.side (Handing.holder t)))) +
      (sign (total sides (flow.take t .sink)) + 0) from
  match Handing.holder t with
  | true => Nat.zero_lt_one
  | false => Nat.zero_lt_one

/-- So the conclusion of `Flow.Dissipative.opens` (P13) holds here too, by the same
exchange of the sink, while the sides take, give and recur among themselves alone. -/
theorem taking_opens_anyway (T : Nat) : ¬ ∀ t, T ≤ t → flow.ClosedAt sides t :=
  Flow.Dissipative.opens balances dissipative sides_distinct (fun _ mem => mem)
    (fun N => ⟨N, Nat.le_refl N, takes N⟩) T

end SprayHanding

/-! ## K1. Under enclosure around the family, the exchange beyond is inflow -/

/-- A total over a list without repetition is at most the total over any list holding
each member at which the quantity is positive. -/
theorem total_le_of_support {α : Type} {q : α → Nat} :
    ∀ {l m : List α}, Distinct l → (∀ a, a ∈ l → 0 < q a → a ∈ m) → total l q ≤ total m q
  | [], _, _, _ => Nat.zero_le _
  | a :: l, m, ⟨fresh, distinct⟩, sub => match h : q a with
    | 0 =>
      have rest : total l q ≤ total m q :=
        total_le_of_support distinct fun b mem => sub b (.tail a mem)
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + total l q) h).trans (Nat.zero_add _))) rest
    | n + 1 =>
      match List.append_of_mem (sub a (.head l)
          (Eq.subst (motive := fun k => 0 < k) h.symm (Nat.succ_pos n))) with
      | ⟨p, r, split⟩ =>
        have inner : total l q ≤ total (p ++ r) q :=
          total_le_of_support distinct fun b mem positive =>
            mem_remove (fun same => fresh (Eq.subst (motive := fun x => x ∈ l) same mem))
              (Eq.subst (motive := fun x => b ∈ x) split (sub b (.tail a mem) positive))
        have whole : total m q = q a + total (p ++ r) q :=
          (congrArg (total · q) split).trans ((total_append q (a :: r) p).trans
            ((Nat.add_left_comm (total p q) (q a) (total r q)).trans
              (congrArg (q a + ·) (total_append q r p).symm)))
        Nat.le_trans (Nat.add_le_add_left inner (q a)) (Nat.le_of_eq whole.symm)

/-- Across the step from `t`, a finite family without repetition containing `ds` is
closed: the exchange of the step, together with the family, lies within finitely many
conditions. -/
def Around {F C : Type} (L : Flow F C) (ds : List C) (t : Nat) : Prop :=
  ∃ E, Distinct E ∧ (∀ c, c ∈ ds → c ∈ E) ∧ L.ClosedAt E t

/-- Across the step from `t`, every formation taking part that gives to the family takes
only from the family: nothing beyond the family flows into it. -/
def Inward {F C : Type} (L : Flow F C) (ds : List C) (t : Nat) : Prop :=
  ∀ f, f ∈ L.present t → 0 < total ds (L.give t f) → ∀ c, 0 < L.take t f c → c ∈ ds

/-- If finitely many conditions are all there is, every step is enclosed around every
family. -/
theorem around_of_finite {F C : Type} {L : Flow F C} {all : List C} (distinct : Distinct all)
    (every : ∀ c, c ∈ all) (ds : List C) (t : Nat) : Around L ds t :=
  ⟨all, distinct, fun c _ => every c, fun _ _ c outside => absurd (every c) outside⟩

/-- Under dissipation, a family without repetition enclosed across a step, into which
nothing beyond it flows, is dissipated on across that step. -/
theorem dissipatesOn_of_inward {F C : Type} {L : Flow F C} (dissipative : L.Dissipative)
    {ds : List C} (distinct : Distinct ds) {t : Nat} (around : Around L ds t)
    (inward : Inward L ds t) : L.DissipatesOn ds t :=
  match around with
  | ⟨E, distinctE, sub, closed⟩ => fun f present =>
    match Nat.decLt 0 (total ds (L.give t f)) with
    | isFalse nothing =>
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (eq_zero_of_not_pos nothing)).trans
        (Nat.zero_add _))) (sign_le _)
    | isTrue gives =>
      have giveE : total ds (L.give t f) ≤ total E (L.give t f) :=
        total_le_of_support distinct fun c mem _ => sub c mem
      have takeE : total E (L.take t f) ≤ total ds (L.take t f) :=
        total_le_of_support distinctE fun c _ positive => inward f present gives c positive
      have dissE := dissipative E t distinctE closed
      have one : sign (total E (L.take t f)) = 1 := Nat.le_antisymm (sign_le_one _)
        (sign_pos (dissE.takes_of_gives present (Nat.lt_of_lt_of_le gives giveE)))
      Nat.le_trans (Nat.add_le_add_left (sign_le_one _) _)
        (Nat.le_trans (Nat.add_le_add_right giveE 1)
          (Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) one.symm))
            (Nat.le_trans (dissE f present) takeE)))

/-- Taking draws in: under dissipation, a finite family without repetition from which
formations take at arbitrarily late steps, enclosed around from some step on, receives at
arbitrarily late steps from some formation that gives to it and takes from a condition
beyond it. -/
theorem taking_draws_in {F C : Type} {L : Flow F C} {W : Web F C} (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List C} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → Around L ds t) (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t)
    (N : Nat) : ¬ ∀ t, N ≤ t → Inward L ds t :=
  fun inward => balances.taking_ceases (T := N + T₀)
    (fun t later => dissipatesOn_of_inward dissipative distinct
      (around t (Nat.le_trans (Nat.le_add_left T₀ N) later))
      (inward t (Nat.le_trans (Nat.le_add_right N T₀) later))) recurs

/-- Generation draws in: under dissipation, a finite family without repetition in which
embodied members arise at arbitrarily late steps, enclosed around from some step on,
receives at arbitrarily late steps from some relatum that gives to it and takes from a
relatum beyond it. -/
theorem generation_draws_in {X : Type} {L : Flow X X} {W : Web X X} (balances : L.Balances W)
    (dissipative : L.Dissipative) {ds : List X} (distinct : Distinct ds) {T₀ : Nat}
    (around : ∀ t, T₀ ≤ t → Around L ds t)
    (arising : ∀ N, ∃ t x, N ≤ t ∧ x ∈ ds ∧ W.Embodied x ∧ W.Arises t x) (N : Nat) :
    ¬ ∀ t, N ≤ t → Inward L ds t :=
  fun inward =>
    have dissipates : ∀ t, N + T₀ ≤ t → L.DissipatesOn ds t := fun t later =>
      dissipatesOn_of_inward dissipative distinct
        (around t (Nat.le_trans (Nat.le_add_left T₀ N) later))
        (inward t (Nat.le_trans (Nat.le_add_right N T₀) later))
    falls_finitely (W.stock ds) (N + T₀)
      (fun t later => Nat.le_trans (Nat.le_add_right _ _) (balances.runs_down (dissipates t later)))
      fun M => match arising (M + (N + T₀)) with
      | ⟨t, _, later, mem, embodied, arises⟩ =>
        have late : N + T₀ ≤ t := Nat.le_trans (Nat.le_add_left _ M) later
        ⟨t, Nat.le_trans (Nat.le_add_right M _) later,
          match total_pos (L.present t) (Nat.lt_of_lt_of_le ((embodied (t + 1)).mp arises.2)
              (embodied.given_of_arises balances arises)) with
          | ⟨_, present, gives⟩ => Nat.lt_of_lt_of_le
              (Nat.lt_add_of_pos_right (total_pos_of_mem
                (q := fun f => sign (total ds (L.take t f))) present
                (sign_pos ((dissipates t late).takes_of_gives present
                  (total_pos_of_mem mem gives)))))
              (balances.runs_down (dissipates t late))⟩

/-- In the spray, nothing flows into the sides from beyond, at every step: the premise
`Around` is what `generation_draws_in` needs, since its conclusion fails here. -/
theorem SprayHanding.not_around (t : Nat) : ¬ Around SprayHanding.flow SprayHanding.sides t :=
  fun ⟨E, distinct, _, closed⟩ => SprayHanding.unenclosed t ⟨E, distinct, closed⟩

/-- `Kindling` is enclosed around the two sides at every step, by the sides and the fuel
burnt. -/
theorem Kindling.around (t : Nat) :
    Around Kindling.flow [.side true, .side false] t :=
  ⟨[.side true, .side false, .fuel t],
   ⟨fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
    ⟨fun mem => match mem with | .tail _ no => (nomatch no),
     ⟨fun no => (nomatch no), trivial⟩⟩⟩,
   fun c mem => match c, mem with
    | _, .head _ => .head _
    | _, .tail _ (.head _) => .tail _ (.head _),
   fun f present c outside => match f, present, c with
    | _, .head _, .side true => absurd (.head _) outside
    | _, .head _, .side false => absurd (.tail _ (.head _)) outside
    | _, .head _, .fuel n => ⟨show 2 * Frontier.burning n t = 0 from
        match h : Frontier.burning n t with
        | 0 => rfl
        | k + 1 => absurd (Eq.subst (motive := fun m =>
              Kindling.Relatum.fuel m ∈ [.side true, .side false, .fuel t])
            (Frontier.burning_at n t (Eq.subst (motive := fun b => 0 < b) h.symm
              (Nat.succ_pos k))).symm (.tail _ (.tail _ (.head _)))) outside, rfl⟩⟩

/-- So in `Kindling`, at arbitrarily late steps the side that gives to the family takes
from beyond it: the fuel. -/
theorem Kindling.draws_in (N : Nat) :
    ¬ ∀ t, N ≤ t → Inward Kindling.flow [.side true, .side false] t :=
  generation_draws_in (ds := [.side true, .side false]) Kindling.balances Kindling.dissipative
    ⟨fun mem => match mem with | .tail _ no => (nomatch no), fun no => (nomatch no), trivial⟩
    (T₀ := 0) (fun t _ => Kindling.around t)
    (fun M => match Handing.recurs true M with
      | ⟨t, later, arises⟩ => ⟨t, .side true, later, .head _, fun _ => Iff.rfl, arises⟩) N

/-! ## K2. Under dissipation, a giver to a family that is not closed need not take from it -/

/-- The frontier is dissipative, and at every step after the first the sun gives the pool
something while taking nothing from it: `DissipatesOn.takes_of_gives` needs the family to
be dissipated on, hence closed. -/
theorem Frontier.gives_without_taking :
    Frontier.flow.Dissipative ∧ ∀ t,
      0 < total [Frontier.Condition.pool] (Frontier.flow.give (t + 1) .sun) ∧
      total [Frontier.Condition.pool] (Frontier.flow.take (t + 1) .sun) = 0 :=
  ⟨Frontier.dissipative, fun t => ⟨Nat.succ_pos t, rfl⟩⟩

/-! ## The witnesses of `Becoming.Dissipation` are enclosed at every step -/

theorem Lone.enclosed (t : Nat) : Lone.flow.Enclosed t :=
  ⟨[.pool, .fuel t], ⟨fun mem => match mem with | .tail _ no => (nomatch no),
    ⟨fun no => (nomatch no), trivial⟩⟩,
   fun f _ c outside => match f, c with
    | .sun, .pool => absurd (.head _) outside
    | .eater, .pool => absurd (.head _) outside
    | .sun, .fuel n => ⟨show 2 * Frontier.burning n t = 0 from
        match h : Frontier.burning n t with
        | 0 => rfl
        | k + 1 => absurd (Eq.subst (motive := fun m =>
              Frontier.Condition.fuel m ∈ [Frontier.Condition.pool, .fuel t])
            (Frontier.burning_at n t (Eq.subst (motive := fun b => 0 < b) h.symm
              (Nat.succ_pos k))).symm (.tail _ (.head _))) outside, rfl⟩
    | .eater, .fuel _ => ⟨rfl, rfl⟩⟩

/-- Across the step from `t`, the frontier's exchange lies within the pool and the `t`th
fuel. -/
theorem Frontier.closed (t : Nat) : Frontier.flow.ClosedAt [.pool, .fuel t] t :=
  fun f _ c outside => match f, c with
    | .sun, .pool => absurd (.head _) outside
    | .grower _, .pool => absurd (.head _) outside
    | .sun, .fuel n => ⟨show (n + 1) * Frontier.burning n t = 0 from
        match h : Frontier.burning n t with
        | 0 => Nat.mul_zero (n + 1)
        | k + 1 => absurd (Eq.subst (motive := fun m =>
              Frontier.Condition.fuel m ∈ [Frontier.Condition.pool, .fuel t])
            (Frontier.burning_at n t (Eq.subst (motive := fun b => 0 < b) h.symm
              (Nat.succ_pos k))).symm (.tail _ (.head _))) outside, rfl⟩
    | .grower _, .fuel _ => ⟨rfl, rfl⟩

theorem Frontier.pool_fuel_distinct (t : Nat) :
    Distinct [Frontier.Condition.pool, .fuel t] :=
  ⟨fun mem => match mem with | .tail _ no => (nomatch no), ⟨fun no => (nomatch no), trivial⟩⟩

theorem Frontier.enclosed (t : Nat) : Frontier.flow.Enclosed t :=
  ⟨[.pool, .fuel t], Frontier.pool_fuel_distinct t, Frontier.closed t⟩

/-- The frontier is enclosed around the pool at every step. -/
theorem Frontier.around (t : Nat) : Around Frontier.flow [.pool] t :=
  ⟨[.pool, .fuel t], Frontier.pool_fuel_distinct t,
   fun c mem => match c, mem with | _, .head _ => .head _, Frontier.closed t⟩

/-- So `taking_draws_in` applies to the frontier, whose growers take from the pool more and
more: at arbitrarily late steps a formation gives to the pool and takes from beyond it,
the sun burning fuel. -/
theorem Frontier.draws_in (N : Nat) : ¬ ∀ t, N ≤ t → Inward Frontier.flow [.pool] t :=
  taking_draws_in (ds := [Frontier.Condition.pool]) Frontier.balances Frontier.dissipative
    ⟨fun no => (nomatch no), trivial⟩ (T₀ := 0)
    (fun t _ => Frontier.around t)
    (Flow.More.takers_recur Frontier.more) N

end P15Probe
```

### `P16Probes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P15, P16 and P16b: the P16 part

Each probe is a minimal model satisfying the published definitions at `b24963f1`
unchanged, or a theorem over them.
-/

namespace P16Probe

open Becoming

/-! ## K4. `Layered`'s members are brief, and `Whole.arises_within` applies to them -/

/-- Each member of `Layered` is never active at two consecutive steps. -/
theorem layered_brief : ∀ p, p ≠ Layered.Level.lineage → Layered.web.Brief 1 p
  | .first, _ => fun t now later =>
      Bool.noConfusion ((congrArg (!·) now).symm.trans (later : (!odd t) = false))
  | .second, _ => fun t now later =>
      Bool.noConfusion ((congrArg (!·) now).symm.trans (later : (!odd t) = true))
  | .lineage, other => absurd rfl other

/-- So `Whole.arises_within` applies with `d = 1`: a member arises at every step. -/
theorem layered_within (S : Nat) :
    ¬ ∀ j, j < 1 → ∀ p, p ≠ Layered.Level.lineage → ¬ Layered.web.Arises (S + j) p :=
  Web.Whole.arises_within Layered.composed layered_brief (T := 0) (fun _ _ => trivial)
    (Nat.zero_le S)

/-! ## K3. Under `Brief`, the generation of parts may be two parts arising again and again -/

/-- In `Layered`, every arising is the arising of one of two parts, and neither part's
activity ends: the persistence that `Whole.arises_within` reads as the generation of
parts is carried by two parts re-arising, nothing new. -/
theorem layered_two :
    (∀ t p, Layered.web.Arises t p → p ∈ [Layered.Level.first, .second]) ∧
    ¬ Layered.web.Ends .first ∧ ¬ Layered.web.Ends .second :=
  ⟨fun _ p arises => match p, arises with
    | .first, _ => .head _
    | .second, _ => .tail _ (.head _)
    | .lineage, arises => absurd trivial arises.1,
   fun ⟨T, gone⟩ => match h : odd T with
    | false => gone T (Nat.le_refl T) h
    | true => gone (T + 1) (Nat.le_succ T) (congrArg (!·) h),
   fun ⟨T, gone⟩ => match h : odd T with
    | true => gone T (Nat.le_refl T) h
    | false => gone (T + 1) (Nat.le_succ T) (congrArg (!·) h)⟩

/-- Under `Ends` and `Listed`, by contrast, no finite list of parts carries the
persistence: parts outside any finite list of parts arise at arbitrarily late steps. -/
theorem needs_new {F C : Type} {W : Web F C} {parts : F → Prop} {w : F} {alive : Nat → List F}
    (whole : W.Whole parts w) (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p)
    {T : Nat} (persists : ∀ t, T ≤ t → W.active t w) {l : List F} (inl : ∀ p, p ∈ l → parts p)
    (N : Nat) : ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ p ∈ l → ¬ W.Arises t p :=
  fun quiet => match Web.Ends.all (W := W) (l := l) (fun p mem => ends p (inl p mem)) with
  | ⟨M, gone⟩ => Web.Whole.needs_arising whole listed ends persists (N + M)
      fun t later p part arises => quiet t (Nat.le_trans (Nat.le_add_right N M) later) p part
        (fun mem => gone p mem (t + 1)
          (Nat.le_trans (Nat.le_add_left M N) (Nat.le_trans later (Nat.le_succ t))) arises.2)
        arises

/-! ## K3. `Whole` is coincidence of activity, and its converse direction is idle -/

/-- Every formation is the whole of itself. -/
theorem whole_self {F C : Type} (W : Web F C) (f : F) : W.Whole (· = f) f :=
  fun _ => ⟨fun active => ⟨f, rfl, active⟩,
    fun ⟨_, same, active⟩ => Eq.subst (motive := fun g => W.active _ g) same active⟩

/-- Two formations active at every step are each the whole of the other. -/
theorem each_other : Immortal.web.Whole (· = true) false ∧ Immortal.web.Whole (· = false) true :=
  ⟨fun _ => ⟨fun _ => ⟨true, rfl, trivial⟩, fun _ => trivial⟩,
   fun _ => ⟨fun _ => ⟨false, rfl, trivial⟩, fun _ => trivial⟩⟩

/-- `Whole.arises_within` without a whole: it is enough that some part is active at every
step from `T` on. -/
theorem arises_within_of_cover {F C : Type} {W : Web F C} {parts : F → Prop} {d : Nat}
    (brief : ∀ p, parts p → W.Brief d p) {T : Nat}
    (covered : ∀ t, T ≤ t → ∃ p, parts p ∧ W.active t p) {S : Nat} (after : T ≤ S) :
    ¬ ∀ j, j < d → ∀ p, parts p → ¬ W.Arises (S + j) p :=
  fun none => match covered (S + d) (Nat.le_trans after (Nat.le_add_right S d)) with
  | ⟨_, part, active⟩ =>
    Web.active_back none part active fun before => brief _ part S before active

/-- `Whole.needs_arising` without a whole: it is enough that some part is active at every
step from `T` on. -/
theorem needs_arising_of_cover {F C : Type} {W : Web F C} {parts : F → Prop}
    {alive : Nat → List F} (listed : W.Listed parts alive) (ends : ∀ p, parts p → W.Ends p)
    {T : Nat} (covered : ∀ t, T ≤ t → ∃ p, parts p ∧ W.active t p) (N : Nat) :
    ¬ ∀ t, N ≤ t → ∀ p, parts p → ¬ W.Arises t p :=
  fun none => match Web.Ends.all (W := W) (l := alive (N + T))
      (fun p mem => ends p ((listed _ p).mp mem).1) with
  | ⟨M, gone⟩ =>
    match covered (N + T + M) (Nat.le_trans (Nat.le_add_left T N)
        (Nat.le_add_right (N + T) M)) with
    | ⟨p, part, active⟩ =>
      Web.active_back (fun j _ p part => none (N + T + j)
          (Nat.le_trans (Nat.le_add_right N T) (Nat.le_add_right (N + T) j)) p part) part
        active fun before => gone p ((listed _ p).mpr ⟨part, before⟩) (N + T + M)
          (Nat.le_add_left M (N + T)) active

end P16Probe
```

### `P16bProbes.lean`

```lean
import Becoming

/-!
# Probes for the independent review of P15, P16 and P16b: the P16b part

Each probe is a minimal model satisfying the published definitions at `b24963f1`
unchanged, or a theorem over them.
-/

namespace P16bProbe

open Becoming

/-! ## K5. Under `arises_from_embodied`'s premise, the embodied giver may be a sun that
stands at one and depends on nothing -/

namespace EmbodiedSun

/-- `SunSeed.web`, with the sun standing at one instead of zero. -/
def web : Web SunSeed.Relatum SunSeed.Relatum where
  level t x := match x with
    | .sun => 1
    | .seed => SunSeed.sprout t
  active t x := match x with
    | .sun => True
    | .seed => 0 < SunSeed.sprout t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem balances : SunSeed.flow.Balances web
  | _, .sun => rfl
  | 0, .seed => rfl
  | _ + 1, .seed => rfl

theorem acting : SunSeed.flow.Acting web := fun _ f _ mem _ => match f, mem with
  | .sun, _ => trivial
  | .seed, .tail _ no => (nomatch no)

theorem givers : ∀ t f c, f ∈ SunSeed.flow.present t → 0 < SunSeed.flow.give t f c →
    web.Embodied f := fun _ f _ mem _ => match f, mem with
  | .sun, _ => fun _ => ⟨fun _ => Nat.zero_lt_one, fun _ => trivial⟩
  | .seed, .tail _ no => (nomatch no)

/-- Every premise of `Embodied.arises_from_embodied` holds, and it names the sun: embodied,
standing as a condition while it gives. The sun requires nothing, draws on nothing, takes
nothing and does not bear on itself; it is embodied because the representation lets it
stand at one exactly while it is active. -/
theorem embodied_sun :
    SunSeed.flow.Balances web ∧ SunSeed.flow.Acting web ∧
    (∀ t f c, f ∈ SunSeed.flow.present t → 0 < SunSeed.flow.give t f c → web.Embodied f) ∧
    web.Embodied .seed ∧ web.Arises 0 .seed ∧
    (∃ f, web.Embodied f ∧ 0 < web.level 0 f ∧ f ∈ SunSeed.flow.present 0 ∧
      0 < SunSeed.flow.give 0 f .seed ∧ f ≠ .seed) ∧
    (∀ t c, ¬ web.requires t .sun c ∧ ¬ web.draws t .sun c ∧ SunSeed.flow.take t .sun c = 0) ∧
    ¬ web.SelfBearing .sun :=
  have seed : web.Embodied .seed := fun _ => Iff.rfl
  have arises : web.Arises 0 .seed := ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩
  ⟨balances, acting, givers, seed, arises,
   Web.Embodied.arises_from_embodied balances acting givers seed arises,
   fun _ _ => ⟨fun no => no, fun no => no, rfl⟩,
   fun self => (self 0 trivial).1⟩

end EmbodiedSun

/-! ## K6. In `Merge`, a grower that persists arises at every step -/

/-- Under `Merge.merges`, the first grower, active from step one on, arises across every
step: no formation continues as a grower. So formations arise under `merges` at
arbitrarily late steps without more without end. Under each formation continuing only
itself, the same grower arises only across step zero. -/
theorem merge_idle :
    (∀ N, Garden.web.ArisesFrom Merge.merges N (.grower, 0)) ∧
    Garden.web.UnceasingFrom Merge.merges ∧
    ∀ N, ¬ Garden.web.Arises (N + 1) (.grower, 0) :=
  have idle : ∀ N, Garden.web.ArisesFrom Merge.merges N (.grower, 0) := fun N =>
    ⟨Nat.succ_pos N, fun ⟨_, _, same⟩ => Garden.Kind.noConfusion (congrArg Prod.fst same)⟩
  ⟨idle, fun N => ⟨N, (.grower, 0), Nat.le_refl N, idle N⟩,
   fun N arises => arises.1 (Nat.succ_pos N)⟩

namespace Confluence

/-- Two formations that merge, and one new formation for each step. -/
inductive Formation where
  | a
  | b
  | new (n : Nat)

/-- `a` is active at step zero only, `b` at every step, the `n`th new formation from step
`n + 1` on. -/
def web : Web Formation Unit where
  level _ _ := 0
  active t f := match f with
    | .a => t = 0
    | .b => True
    | .new n => n < t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Each formation continues itself, and across step zero `a` also continues as `b`. -/
def continues (t : Nat) (g f : Formation) : Prop :=
  g = f ∨ (t = 0 ∧ g = .a ∧ f = .b)

theorem succ_ne_zero (n : Nat) : n + 1 ≠ 0 := fun same => Nat.noConfusion same

theorem noSplit : web.NoSplit continues :=
  fun t _ _ _ _ r r' after after' => match r, r' with
  | .inl same, .inl same' => same.symm.trans same'
  | .inr ⟨_, _, isB⟩, .inr ⟨_, _, isB'⟩ => isB.trans isB'.symm
  | .inl same, .inr ⟨_, isA, _⟩ => absurd (Eq.subst (motive := fun h => web.active (t + 1) h)
      (same.symm.trans isA) after) (succ_ne_zero t)
  | .inr ⟨_, isA, _⟩, .inl same' => absurd (Eq.subst (motive := fun h => web.active (t + 1) h)
      (same'.symm.trans isA) after') (succ_ne_zero t)

/-- Two formations active at step zero continue as one, without a split; the merged
formation `a` is not active after it; every formation arising under the continuation is
the new formation of its step, and one arises at every step. -/
theorem confluence :
    web.active 0 .a ∧ web.active 0 .b ∧ Formation.a ≠ .b ∧ continues 0 .a .b ∧
    continues 0 .b .b ∧ web.active 1 .b ∧ ¬ web.active 1 .a ∧ web.NoSplit continues ∧
    (∀ t f, web.ArisesFrom continues t f → f = .new t) ∧ web.UnceasingFrom continues :=
  ⟨rfl, trivial, fun same => Formation.noConfusion same, .inr ⟨rfl, rfl, rfl⟩, .inl rfl,
   trivial, succ_ne_zero 0, noSplit,
   fun t f ⟨after, alone⟩ => match f, after with
    | .a, after => absurd after (succ_ne_zero t)
    | .b, _ => absurd ⟨.b, trivial, .inl rfl⟩ alone
    | .new n, after => congrArg Formation.new (Nat.le_antisymm (Nat.le_of_lt_succ after)
        (Nat.ge_of_not_lt fun before => alone ⟨.new n, before, .inl rfl⟩)),
   fun N => ⟨N, .new N, Nat.le_refl N, Nat.lt_succ_self N, fun ⟨_, active, r⟩ => match r with
    | .inl same => Nat.lt_irrefl N
        (Eq.subst (motive := fun h => web.active N h) same active)
    | .inr ⟨_, _, isB⟩ => Formation.noConfusion isB⟩⟩

end Confluence

/-! ## K7. `gives_less` needs the family without repetition -/

/-- In `Lone`, the family listing the pool twice and the fuel of the step is closed across
the step, and the sun gives it two units while taking two: on a family with repetition a
giver need not take more than it gives. -/
theorem repeated_family (t : Nat) :
    Lone.flow.Dissipative ∧ Lone.flow.ClosedAt [.pool, .pool, .fuel t] t ∧
    Lone.Formation.sun ∈ Lone.flow.present t ∧
    total [Frontier.Condition.pool, .pool, .fuel t] (Lone.flow.give t .sun) = 2 ∧
    total [Frontier.Condition.pool, .pool, .fuel t] (Lone.flow.take t .sun) = 2 :=
  ⟨Lone.dissipative,
   fun f _ c outside => match f, c with
    | .sun, .pool => absurd (.head _) outside
    | .eater, .pool => absurd (.head _) outside
    | .sun, .fuel n => ⟨show 2 * Frontier.burning n t = 0 from
        match h : Frontier.burning n t with
        | 0 => rfl
        | k + 1 => absurd (Eq.subst (motive := fun m =>
              Frontier.Condition.fuel m ∈ [Frontier.Condition.pool, .pool, .fuel t])
            (Frontier.burning_at n t (Eq.subst (motive := fun b => 0 < b) h.symm
              (Nat.succ_pos k))).symm (.tail _ (.tail _ (.head _)))) outside, rfl⟩
    | .eater, .fuel _ => ⟨rfl, rfl⟩,
   .head _, rfl,
   show 0 + (0 + (2 * Frontier.burning t t + 0)) = 2 from
     Eq.subst (motive := fun b => 0 + (0 + (2 * b + 0)) = 2) (Frontier.burning_self t).symm rfl⟩

end P16bProbe
```

### `ProbeAudit.lean`

```lean
import P15Probes
import P16Probes
import P16bProbes

#print axioms P15Probe.SprayHanding.Relatum
#print axioms P15Probe.SprayHanding.flow
#print axioms P15Probe.SprayHanding.web
#print axioms P15Probe.SprayHanding.sides
#print axioms P15Probe.SprayHanding.sides_distinct
#print axioms P15Probe.SprayHanding.bound
#print axioms P15Probe.SprayHanding.le_bound
#print axioms P15Probe.SprayHanding.fresh
#print axioms P15Probe.SprayHanding.balances
#print axioms P15Probe.SprayHanding.acting
#print axioms P15Probe.SprayHanding.dependent
#print axioms P15Probe.SprayHanding.unenclosed
#print axioms P15Probe.SprayHanding.dissipative
#print axioms P15Probe.SprayHanding.even_sum
#print axioms P15Probe.SprayHanding.spray_handing
#print axioms P15Probe.SprayHanding.opens_anyway
#print axioms P15Probe.SprayHanding.sides_within
#print axioms P15Probe.SprayHanding.takes
#print axioms P15Probe.SprayHanding.taking_opens_anyway
#print axioms P15Probe.total_le_of_support
#print axioms P15Probe.Around
#print axioms P15Probe.Inward
#print axioms P15Probe.around_of_finite
#print axioms P15Probe.dissipatesOn_of_inward
#print axioms P15Probe.taking_draws_in
#print axioms P15Probe.generation_draws_in
#print axioms P15Probe.SprayHanding.not_around
#print axioms P15Probe.Kindling.around
#print axioms P15Probe.Kindling.draws_in
#print axioms P15Probe.Frontier.gives_without_taking
#print axioms P15Probe.Lone.enclosed
#print axioms P15Probe.Frontier.closed
#print axioms P15Probe.Frontier.pool_fuel_distinct
#print axioms P15Probe.Frontier.enclosed
#print axioms P15Probe.Frontier.around
#print axioms P15Probe.Frontier.draws_in
#print axioms P16Probe.layered_brief
#print axioms P16Probe.layered_within
#print axioms P16Probe.layered_two
#print axioms P16Probe.needs_new
#print axioms P16Probe.whole_self
#print axioms P16Probe.each_other
#print axioms P16Probe.arises_within_of_cover
#print axioms P16Probe.needs_arising_of_cover
#print axioms P16bProbe.EmbodiedSun.web
#print axioms P16bProbe.EmbodiedSun.balances
#print axioms P16bProbe.EmbodiedSun.acting
#print axioms P16bProbe.EmbodiedSun.givers
#print axioms P16bProbe.EmbodiedSun.embodied_sun
#print axioms P16bProbe.merge_idle
#print axioms P16bProbe.Confluence.Formation
#print axioms P16bProbe.Confluence.web
#print axioms P16bProbe.Confluence.continues
#print axioms P16bProbe.Confluence.succ_ne_zero
#print axioms P16bProbe.Confluence.noSplit
#print axioms P16bProbe.Confluence.confluence
#print axioms P16bProbe.repeated_family
```

### `ProbeAudit` output

```text
'P15Probe.SprayHanding.Relatum' does not depend on any axioms
'P15Probe.SprayHanding.flow' does not depend on any axioms
'P15Probe.SprayHanding.web' does not depend on any axioms
'P15Probe.SprayHanding.sides' does not depend on any axioms
'P15Probe.SprayHanding.sides_distinct' does not depend on any axioms
'P15Probe.SprayHanding.bound' does not depend on any axioms
'P15Probe.SprayHanding.le_bound' does not depend on any axioms
'P15Probe.SprayHanding.fresh' does not depend on any axioms
'P15Probe.SprayHanding.balances' does not depend on any axioms
'P15Probe.SprayHanding.acting' does not depend on any axioms
'P15Probe.SprayHanding.dependent' does not depend on any axioms
'P15Probe.SprayHanding.unenclosed' does not depend on any axioms
'P15Probe.SprayHanding.dissipative' does not depend on any axioms
'P15Probe.SprayHanding.even_sum' does not depend on any axioms
'P15Probe.SprayHanding.spray_handing' does not depend on any axioms
'P15Probe.SprayHanding.opens_anyway' does not depend on any axioms
'P15Probe.SprayHanding.sides_within' does not depend on any axioms
'P15Probe.SprayHanding.takes' does not depend on any axioms
'P15Probe.SprayHanding.taking_opens_anyway' does not depend on any axioms
'P15Probe.total_le_of_support' does not depend on any axioms
'P15Probe.Around' does not depend on any axioms
'P15Probe.Inward' does not depend on any axioms
'P15Probe.around_of_finite' does not depend on any axioms
'P15Probe.dissipatesOn_of_inward' does not depend on any axioms
'P15Probe.taking_draws_in' does not depend on any axioms
'P15Probe.generation_draws_in' does not depend on any axioms
'P15Probe.SprayHanding.not_around' does not depend on any axioms
'P15Probe.Kindling.around' does not depend on any axioms
'P15Probe.Kindling.draws_in' does not depend on any axioms
'P15Probe.Frontier.gives_without_taking' does not depend on any axioms
'P15Probe.Lone.enclosed' does not depend on any axioms
'P15Probe.Frontier.closed' does not depend on any axioms
'P15Probe.Frontier.pool_fuel_distinct' does not depend on any axioms
'P15Probe.Frontier.enclosed' does not depend on any axioms
'P15Probe.Frontier.around' does not depend on any axioms
'P15Probe.Frontier.draws_in' does not depend on any axioms
'P16Probe.layered_brief' does not depend on any axioms
'P16Probe.layered_within' does not depend on any axioms
'P16Probe.layered_two' does not depend on any axioms
'P16Probe.needs_new' does not depend on any axioms
'P16Probe.whole_self' does not depend on any axioms
'P16Probe.each_other' does not depend on any axioms
'P16Probe.arises_within_of_cover' does not depend on any axioms
'P16Probe.needs_arising_of_cover' does not depend on any axioms
'P16bProbe.EmbodiedSun.web' does not depend on any axioms
'P16bProbe.EmbodiedSun.balances' does not depend on any axioms
'P16bProbe.EmbodiedSun.acting' does not depend on any axioms
'P16bProbe.EmbodiedSun.givers' does not depend on any axioms
'P16bProbe.EmbodiedSun.embodied_sun' does not depend on any axioms
'P16bProbe.merge_idle' does not depend on any axioms
'P16bProbe.Confluence.Formation' does not depend on any axioms
'P16bProbe.Confluence.web' does not depend on any axioms
'P16bProbe.Confluence.continues' does not depend on any axioms
'P16bProbe.Confluence.succ_ne_zero' does not depend on any axioms
'P16bProbe.Confluence.noSplit' does not depend on any axioms
'P16bProbe.Confluence.confluence' does not depend on any axioms
'P16bProbe.repeated_family' does not depend on any axioms
```
