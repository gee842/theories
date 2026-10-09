# P18b 至 P23 的独立审查 / Independent review of P18b through P23

2026-10-09。审查者：Claude Opus 5.5，独立 agent，未参与撰写这六个阶段。对象：`main` 的 `c6335c48`。/ Reviewer: Claude Opus 5.5, an independent agent that wrote none of the six phases. Object: `main` at `c6335c48`.

**摘要（中文）。** 六个阶段的全部 Lean 声明都在仓库之外从前导重新编译。核心闭包的 27 个模块（24 个核心模块与 3 个基础模块）退出码为 0，没有警告，1571 条源声明的公理报告全部为空。闭包的 4423 个常量中，依赖公理的只有 30 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列完全相同。回执 `20261009T114557.489291Z`（939 项定理／1501 项声明审计，核心闭包 27 个模块，包 25 个模块）、40 个源哈希、保留运行的 244 个产物、27 份变更记录的 314 个引用哈希与 73 个证明绑定都对。这些记录的 466 个别名中 425 个在核心中解析，其余 41 个属于未重建的桥接（26）、Mathlib 外围（5）与继承模块（10）。数学被接受，Lean 中没有发现数学错误。第八次审查的 L1–L10 全部关闭。本审查写了 63 条探针声明（其中 32 项定理），都不依赖任何公理。问题共十项（M1–M10）：一项替 Ren 选择了读法，四项省略前提，一项散文中的错误，两项缺少反例，两项表述与记账。

- **P18b（第八次审查的处理）。** L1–L10 都已关闭。新增的核心声明都对。检查器对生成常量的审计与本审查的独立枚举一致。问题是记账：审查时间的约定已写入工作流，但四份记录的审查时间晚于包含它的提交（M10）。
- **P19（变化的规律）。** 定理都对，`Dawn` 与 `Dusk` 是真见证。这些规律不加关于展开的前提，但依赖表示的承诺：离散的步、自然数的量、被计数的规定可判定。
  - **可判定性（M2）。** 不给可判定性，有限世界的规律就蕴含排中律（探针 N1）。P23 的表示清单漏掉了这一项，根基章节写成“不加前提”。
  - **规律的种类（M9）。** `change_readings` 由六个 `Iff.rfl` 证明，是定义上的同一。章节把它与有内容的规律标作同一种“规律”。
  - **读法（M1）。** P19 已把“有限家族中开始成立与不再成立同步”读作“生成与退化同步”，并标为作者的读法；P22 把这一读法写进整体的部分的定义。
- **P20（上升与下降在同一交换中）。** 定理都对，`Brood.rise_without_fall` 是真见证。问题在概括（M5）。
  - 章节与记录标题把“该步被耗散的家族”缩成“在耗散之下”。在 `Spray` 中流平衡且耗散，一个条件上升，没有任何条件下降。
  - “消耗前提由平衡与耗散推出”省略了“有形成从家族取用”。在 `Still` 中流平衡且耗散，事件每步发生，家族不被消耗。
- **P21（经世系的演化）。** 定理都对，`Drawdown` 与 `Unchecked` 是真见证，`TransmitsWithin` 作为前提公开。问题如下。
  - **`price`（M3）。** 等式成立，计数形式已经披露。但“从亲代到后代的变化分为选择项与传递项”说错了它：等式分解的是后代的总量，所谓选择项在没有任何选择时也不为零。
  - **传递（M6）。** 章节的“传下来的所需曾在给予之步被满足”只在界 δ 为零时成立。
- **P22（整体与其部分）。** 定理都对。`World` 经 `ofRoles` 与 roles 迁移引理嵌入两类读法。`Living` 的描述准确。Ren 的提议没有被改写成“不需要公理”的结论。问题如下。
  - **生成的与退化的（M1，最严重）。** 模块把 Ren 提议中的“generative, degenerative”读作“某个关系项在任意晚的步生起／止息”，并据此说有限世界中两者是同一部分、彼此交叠。Ren 在 2026-10-09 说：“generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧”。章节、模块说明、记录、词汇表与根基章节都没有提到这句原话，也没有把这一读法列入 Ren 的选择。
  - **活跨越生成（M7）。** “生成复现而有事件不活”的唯一见证 `spending`，依赖第 8 节列为 Ren 选择的一项：在承担自身的体现关系项终结之步的汲取是否计入不 living。探针 `Predator` 给出不依赖这一选择的见证。
  - **归于静止的前提（M4、M8）。** 章节第 4 条“在耗散之下继续生成，展开须越出每个有限部分”省略了平衡与生起者体现，模块自己的 `flicker` 与 `unbalanced` 就是有限的反例。`unbalanced` 的耗散为空；探针 `Leaking` 给出耗散不空的见证。
- **P23（完整的陈述）。** 原第 8 节的开放项没有丢失。“形式陈述的完整不是必然性的证明”在各处一致写明，完成没有被夸大。问题如下。
  - 表示承诺的清单漏掉了可判定性（M2）。
  - 完整陈述中有四处省略前提（M4、M5、M6），一处误述 `price`（M3）。
  - “规律”的标注不区分定义上的同一与有内容的规律；智慧一项被归入进一步的证明；计划四项完整标准中的第 3 项只对七个前提完成，现状却没有写出（M9）。
- **Ren 的原话与读法。** Ren 的原话引用准确。除 M1 外，没有发现替 Ren 选择读法。M7 中，一个见证依赖 Ren 尚未作出的选择。

**Summary (English).** Every Lean declaration of the six phases recompiles from the prelude outside the repository. The 27 modules of the core closure (24 core and 3 foundation modules) exit 0 with no warnings, and all 1571 of their source declarations have empty axiom reports. Of the closure's 4423 constants, the only ones depending on an axiom are 30 compiler-generated `injEq` lemmas, each depending only on `propext`; they are exactly the 30 the receipt lists. The receipt `20261009T114557.489291Z` (939 theorems and 1501 declaration audits; core closure 27 modules, package 25) is correct. So are its 40 source hashes, the 244 artifacts of its retained run and, for the 27 changed records, 314 reference hashes and 73 proof bindings. Of those records' 466 aliases, 425 resolve in the core; the other 41 belong to the unrebuilt bridge (26), the Mathlib periphery (5) and inherited modules (10). The mathematics is accepted; no mathematical error was found in the Lean. L1–L10 of the eighth review are all closed. This review wrote 63 probe declarations (32 of them theorems), none of which depends on any axiom. The ten findings (M1–M10) are: one reading chosen for Ren, four omitted premises, one error in prose, two missing counterexamples, and two items of presentation and bookkeeping.

- **P18b (handling of the eighth review).** L1–L10 are closed. The new core declarations are correct. The checker's audit of generated constants agrees with this review's own enumeration. The convention for review stamps is in the workflow, but four records carry stamps later than the commit that contains them (M10).
- **P19 (laws of change).** The theorems hold, and `Dawn` and `Dusk` are genuine witnesses. The laws need no premise about the unfolding, but they rest on the representation's commitments: discrete steps, natural-number amounts, and decidable determinations where they are counted.
  - **Decidability (M2).** Without decidability, the finite-world law yields excluded middle (probe N1). P23's lists of the representation's commitments omit it, and the foundation chapter says "with no premise".
  - **Kinds of law (M9).** `change_readings` is proved by six `Iff.rfl`, an identity by definition. The chapter tags it with the same "law" as laws with content.
  - **The reading (M1).** P19 already reads "coming to be and ceasing to be keep pace in a finite family" as "generation and degeneration recur together", labelled as the author's reading. P22 writes that reading into the definitions of the parts of the whole.
- **P20 (rising and falling in one exchange).** The theorems hold, and `Brood.rise_without_fall` is a genuine witness. The findings are in the summaries (M5).
  - The chapter and the record title shorten "a family dissipated on across the step" to "under dissipation". In `Spray` the flow balances and is dissipative, a condition rises, and no condition ever falls.
  - "The depletion premise follows from balance and dissipation" drops "and some formation takes from the family". In `Still` the flow balances and is dissipative, an event occurs at every step, and the family is not depleted.
- **P21 (evolution on descent).** The theorems hold, `Drawdown` and `Unchecked` are genuine witnesses, and `TransmitsWithin` is disclosed as a premise.
  - **`price` (M3).** The identity holds, and its counting form is disclosed. But "the change from parents to offspring divides into a selection term and a transmission term" misdescribes it. The identity divides the offspring's total, and its "selection term" is not zero when nothing is selected.
  - **Transmission (M6).** The chapter's "a transmitted need was met at the giving step" holds only when the bound δ is zero.
- **P22 (the whole and its parts).** The theorems hold. `World` embeds the two-kind reading through `ofRoles` and the roles transfer lemmas. `Living` is described accurately. Ren's proposal is not turned into a claim that no axiom is needed.
  - **Generative and degenerative (M1, the most serious).** The module reads the "generative, degenerative" of Ren's proposal as "some relatum arises / ceases at arbitrarily late steps". On that reading it states that in a finite world the two are one part and that they overlap. On 9 October Ren said: "generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧". The chapter, the module doc, the record, the glossary and the foundation chapter neither mention these words nor list the reading among Ren's choices.
  - **Living crosses generation (M7).** The only witness for "generation recurs and some event is not living" is `spending`. It rests on what §8 lists as Ren's choice: whether drawing on a self-bearing embodied relatum across the step at which it ends counts as not living. The probe `Predator` gives a witness that does not depend on that choice.
  - **Premises of rest (M4, M8).** The chapter's "under dissipation, continued generation needs the unfolding to go beyond every finite part" omits balance and embodied arising. The module's own `flicker` and `unbalanced` are finite counterexamples. The dissipation of `unbalanced` is vacuous; the probe `Leaking` is a witness with non-vacuous dissipation.
- **P23 (the full statement).** No open item of the old §8 is lost. "The completeness of a formal statement is not a proof of necessity" is written consistently, and completion is not overstated.
  - The lists of the representation's commitments omit decidability (M2).
  - The full statement omits premises in four places (M4, M5, M6) and misdescribes `price` (M3).
  - The "law" tag does not separate identities by definition from laws with content. Wisdom is filed under further proofs. Criterion 3 of the plan's four-part completeness is met for seven premises, and the status does not say so (M9).
- **Ren.** Ren's words are quoted exactly. Apart from M1, no reading is chosen for Ren. In M7 one witness depends on a choice Ren has not made.

## 0. Scope, materials and method

**Object.** `main` at `c6335c48fcbbb05ab9ce2b32028b5c9c14d859d8`, through six commits:

- **P19 (`4295dd2410ee1c33`).** [Becoming.Change](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Change.lean) in full; study §26 and the English P19 paragraph; the record [coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md); plan row 234.
- **P18b (`840320558de8462c`).** The handling of L1–L10 of [BECOMING-P16C-P17-P18-REVIEW](BECOMING-P16C-P17-P18-REVIEW.md) in `Flow`, `Dissipation`, `Roles`, `Reserve`, `Descent`, the checker and the records; study §27 and the in-place corrections it lists; plan row 233.
- **P20 (`a81c77c432973fcc`).** The `Flow`, `Dissipation` and `Roles` declarations it adds; study §28; the record [rising-and-falling-in-one-exchange](../../../../theories/becoming/results/records/rising-and-falling-in-one-exchange.md); plan row 235.
- **P21 (`85b6d341b93fa6f7`).** [Becoming.Evolution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Evolution.lean) in full and the move of descent out of `Descent`; study §29; the record [evolution-on-descent](../../../../theories/becoming/results/records/evolution-on-descent.md); plan row 236.
- **P22 (`5211c769df0c2140`).** [Becoming.Space](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Space.lean) in full; study §30; the record [space-and-its-parts](../../../../theories/becoming/results/records/space-and-its-parts.md); plan row 237.
- **P23 (`c6335c48fcbbb05a`).** The chapter's "The theory stated in full" and the rearranged §8 of [THE-THEORY-OF-BECOMING](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md); [BECOMING-FOUNDATION](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md) §5; the records [theory-of-becoming-foundation](../../../../theories/becoming/results/records/theory-of-becoming-foundation.md) and [generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md); study §31; plan row 238 and the four-part completeness of plan §9.

**Isolation.** The object was exported with `git archive c6335c48` into the reviewer's scratch directory, and every file was read from there. Nothing in the live repository or its `.git` was modified except the addition of this file. Another session was working in the repository during the review and committed P24 (`e5b61937`) and P25 (`a69455e3`); their work is outside the object and was not read. No `make` target or repository checker was run, and all compilation happened in scratch. Links in this file are relative to `_process/research/2026-10-05-generative-foundation-review/root-foundation/`, where reviews are filed.

**Materials** (sha256 prefixes at `c6335c48`; each equals the exported file):

| File | sha256 prefix |
|---|---|
| study `BECOMING-RENEWAL-READING.md` / plan `BECOMING-UNIFICATION-PLAN.md` | `72b96d79df5b52a5` / `9f55b84c4a31c3c4` |
| chapter `THE-THEORY-OF-BECOMING.md` / `BECOMING-FOUNDATION.md` | `26f97ca14520cf7f` / `78f2a82ddb304f5b` |
| eighth review `BECOMING-P16C-P17-P18-REVIEW.md` / `NONDUAL-METHOD.md` | `a9c11c3bbcfa9e9f` / `8c48b03a167a8909` |
| `_process/RESULT-WORKFLOW.md` | `ee0dd6a46e20f4ff` |
| receipt `becoming-verification.json` (= the retained run's `verification.json`) / `check_becoming.py` | `984afa36f9c803f3` / `667fa43395dd0098` |
| `Becoming.lean` / package `README.md` | `ef212c74d233ce56` / `755c57e97550f448` |
| `Becoming/Change` / `Evolution` / `Space` | `6ef06dafae509c60` / `2768313497b5256a` / `51c8cdea1f8e4f13` |
| `Becoming/Flow` / `Dissipation` / `Roles` | `22fd0168ed9a8027` / `941026b4548d30da` / `07086627aee4f9af` |
| `Becoming/Reserve` / `Descent` | `2379b8c4576c6359` / `11db87b79c808d10` |
| records coming-and-ceasing-keep-pace / rising-and-falling-in-one-exchange | `27be4809efe7a3a6` / `9bfacea59deeb842` |
| records evolution-on-descent / space-and-its-parts | `573801ba480f34b9` / `4b496984443c4197` |
| records theory-of-becoming-foundation / generation-is-replenishment / life-as-condition-of-life | `ff3cf79b38614601` / `9946523ae7918c26` / `7c5305e1e7aa320f` |

**Read in full:**

- AGENTS.md, the nondual method and the eighth review.
- Study §26–§31 and the English P19–P23 paragraphs; §27's in-place corrections where they were checked for L1–L10.
- `Change`, `Evolution` and `Space` in full; the diffs of `Flow`, `Dissipation`, `Roles`, `Reserve`, `Descent`, `Generation` and `Population` across `4295dd24^..c6335c48`; the definitions the new modules use (`Web`, `Flow`, `Balances`, `Acting`, `Taking`, `DissipatesOn`, `Dissipative`, `ClosedAt`, `Depletes`, `Supported`, `Dependent`, `MetAbove`, `UnderminingOn`, `Embodied`, `Carries`, `Handing`, `Flicker`, `Web.valuation`).
- The JSON of the four new records and the P23 diffs of theory-of-becoming-foundation and generation-is-replenishment; the fields changed in the other 21 records.
- The chapter's full statement (lines 60–124), §2 lines 196–215 and 267–287, §8 (lines 495–581), §9 (lines 583–623) and the glossary; foundation §5; the checker's scope text and the README rows for `Change`, `Evolution` and `Space`; plan §9 (lines 213–259).
- The old §8, read from `git show 5211c769:theories/becoming/chapters/THE-THEORY-OF-BECOMING.md`, to check P23's rearrangement item by item.

**Ren's words read**, for provenance:

| Source | sha256 prefix |
|---|---|
| [生生的伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md) | `740126fcca587edb` |
| [一元关系本体优先](../../../../sources/15-codex-theory-conversations/2026-10-08-monist-relational-ontology-first.md) | `54a19521ba6c1345` |
| [Theory of Becoming 的优先提议](../../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md) | `a08597b97e1763ff` |
| [纯净核心](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md) | `f7d31d6df74b8d8a` |
| [整体与 generative manifold](../../../../sources/15-codex-theory-conversations/2026-10-09-becoming-whole-generative-manifold.md) | `fed6e7ec428e5210` |
| [以关系结构分开更新与消耗](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md) | `a12a64304d9cb974` |

The chapter quotes the proposal (lines 36–38) and the clarification (lines 42–44) exactly. The last source was read because the study cites it (line 66) for Ren's statement that generation and degeneration do not overlap; M1 turns on it.

**No external literature was read.** Price's equation is discussed from general knowledge only, and only to say what the repository's identity does and does not state.

**Recompilation.** Lean 4.29.1 (commit `f72c35b3`) was run as `LEAN_PATH=<build> lean -o X.olean X.lean`, in the receipt's order.

- **Core.** The following 27 modules exit 0 from the prelude with no warnings:
  - `GenerativeCore`, with `import Std` removed as the checker does;
  - `InquirySufficiency` and `RelationalRenewal`;
  - `Becoming/{Frame, Inquiry, Renewal, Dependence, Return, Horizon, Joint, Substitution, Generation, Flow, Change, Population, Identity, Wholes, Dissipation, Roles, Reserve, Evolution, Space, Metaethics, Ranking, Correspondence, Descent}`;
  - the root module `Becoming`.
- **Bridge and periphery.** Not rebuilt. `Becoming/Bridge.lean`, `Metaethics.lean` and `Correspondence.lean` are unchanged in `badb652e..c6335c48`, and their bytes match the receipt.

The checks:

- **Receipt.**
  - Status `passed`, Lean 4.29.1 `f72c35b3`, `core_compiles_from_prelude: true`, `source_unchanged_during_check: true`, and a `core_closure` of 27 modules.
  - All 40 `source_sha256` entries equal the object's files, and the checker hash equals `check_becoming.py`.
  - The 244 artifacts of the retained run `becoming-checks/20261009T114557.489291Z` match their recorded hashes.
  - P23 changed no Lean, and `c6335c48` carries the P22 receipt unchanged.
- **Counts.**
  - Theorems per spine module: Frame 11, Inquiry 6, Renewal 6, Dependence 53, Return 29, Horizon 14, Joint 21, Substitution 7, Generation 30, Flow 76, Change 42, Population 36, Identity 83, Wholes 36, Dissipation 89, Roles 134, Reserve 42, Evolution 21, Space 29, Metaethics 35, Ranking 27, Correspondence 37, Descent 41 and Bridge 34, for 939 in all. The 24 core modules have 905 theorems and 1451 declaration audits; Bridge's 50 make 1501. The three foundation modules add 74 theorems and 120 audits to the closure.
  - The receipts at each commit:

    | Commit | Run | Closure / package | Theorems / audits | Generated with axioms |
    |---|---|---|---|---|
    | `badb652e` (eighth review) | `091503.719598Z` | 24 / 22 | 799 / 1286 | not audited |
    | P19 `4295dd24` | `095726.865589Z` | 25 / 23 | 841 / 1342 | not audited |
    | P18b `84032055` | `104417.218214Z` | 25 / 23 | 877 / 1387 | 29 |
    | P20 `a81c77c4` | `110204.479251Z` | 25 / 23 | 889 / 1399 | 29 |
    | P21 `85b6d341` | `112625.591552Z` | 26 / 24 | 910 / 1435 | 29 |
    | P22 `5211c769` and P23 `c6335c48` | `114557.489291Z` | 27 / 25 | 939 / 1501 | 30 |

  - The study, the plan rows and the chapter's §9 table agree with these.
- **Records.**
  - The 27 records changed in `4295dd24^..c6335c48` have 314 `references` hashes, and all equal the object's files.
  - All 73 proof bindings resolve their `sha256_pointer` and `success_pointer` in their receipts to the bound sources' hashes and `passed`.
  - Review stamps: see M10.
- **Names.**
  - `Aliases.lean` (`5f53ef63f4a18987…`) runs `#check @` on all 466 aliases of the 27 records. 425 resolve in the core. The other 41 are 26 `Becoming.Bridge` names, 5 Mathlib-periphery names, and 10 names of the inherited `OperativeCoherence` (6) and `BecomingCompatibility` (4) modules.
  - `Names.lean` (`42cf862e3dbc9b16…`) does the same for the 1317 qualified declaration names in those records' `references`. 1233 resolve. Of the 84 that do not, 38 are bridge, 36 inherited and 6 periphery declarations, and 4 (`GenerativeComparison.G0`, `PositionedPositiveReason.PositionedArticulation`, `PositionedPositiveReason.SecuresPositiveGround`, `UniversalEthics.CutCoverageAudit.Reach`) are inherited names that core files mention in prose. None is a core declaration.
  - Every P19–P22 declaration resolves.
- **Axioms.**
  - `CoreAudit.lean` (`89cfe09c3fa56087…`, `import Becoming` and 1571 `#print axioms` lines generated from the receipt) prints the axioms of every source declaration of the 27-module closure. All 1571 report "does not depend on any axioms".
  - `EnvAudit.lean` (`38b6efd1eb971b50…`) enumerates every constant of the closure, including compiler-generated ones, with `Lean.collectAxioms`. Its per-module counts equal the receipt's `core_closure_constants` (4423 in all; Change 96, Evolution 114, Space 129). Exactly 30 depend on an axiom, all `propext`, all generated `injEq` lemmas, and the 30 names equal the receipt's `generated_axiom_dependencies`; the one added since P18b is `Becoming.World.mk.injEq`.
  - The probe audits are in the appendix: all 63 probe source declarations are axiom-free, and of the probe module's 163 constants only the generated `Review9.Predator.Relatum.side.injEq` depends on `propext`.

**Probes.** One file, `Review9.lean` (`0e5031bc0ffc7d22…`, 492 lines), imports the unchanged `Becoming` and compiles with exit 0 and no warnings. It has 32 theorems, 29 definitions and 2 inductive types, in seven groups N1–N7.

- The probes use term mode only: no tactic, no `simp`, `omega` or `decide`.
- In Lean 4.29.1, a function-defining `match` with overlapping wildcards over a constructor with arguments reports `propext`. A first version of `Predator` did so; the published version lists every case, and its one remaining `propext` constant is the generated `injEq` lemma.
- The probes are minimal models that satisfy the published definitions unchanged, or theorems over those definitions. Following the nondual method, they show what the definitions admit, not what actual systems do. A probe refutes a sentence only where the sentence claims more than the definitions give.

| Probe | Shows | Finding |
|---|---|---|
| N1 `Undecided.law_gives_em` | if every finite world that generates also degenerates, with no decidability supplied, every proposition is decided | M2 |
| N2 `Spray.spray` | a balanced, dissipative flow, only active formations giving, in which a condition rises and none ever falls | M5 |
| N3 `Still.still` | a balanced, dissipative flow and an event at every step that does not deplete the family | M5 |
| N4 `Within.within` | balance, `Acting`, `Dependent` and transmission within one, with a descendant whose need exceeds its condition's level at the giving step and at every step | M6 |
| N5 `selected_uniform`, `one_each` | the selection term is `k` times the parents' total when every parent has `k` offspring, and five when nothing is selected | M3 |
| N6 `Predator.predator`, `not_self` | a finite, generative, `Dependent`, balanced, `Acting`, `Taking` world that is not `Living`, through a drawer that draws on a pool, not on itself | M7 |
| N7 `Leaking.leaking` | a finite, generative, embodied world, dissipative with a closed family taken from at every step, that is not balanced | M4, M8 |

**Severity labels** (as in the eighth review).

- *error*: a definition does not match its stated meaning, or a mathematical claim is false.
- *overclaim*: the prose is stronger than the Lean, including where a premise is left out or a reading is presented as settled.
- *missing counterexample*: a relevant witness is absent or does not exercise what it is cited for.
- *presentation*: wording, provenance or bookkeeping.

No Lean statement is wrong. The one *error* (M3) is a false description, in prose, of what a correct identity states.

## 1. Verdicts

| Question | Verdict | Findings |
|---|---|---|
| 1. P18b: are L1–L10 handled? | **Yes, all ten are closed.** See the table below. The stamp convention of L3(f) is written, and a new stamp pattern appears. | M10 |
| 2. P18b: are its new core declarations correct? | **Yes.** `Flow.Descends` and `DescendsAt` require the giver to take part; `Stranger.stranger`, `Brood.not_descends`, `LivesOn.stands`, `Drowsy.drowsy`, `Seed.no_held`, `Viable.no_held`, `Flow.carries_of_own`, `Web.redirect`, `redirect_dependent`, `Famine.living_differs`, `Balances.rise_given`, `rising_needs_replenishment`, the `rising_*` dissipation theorems and `Growing.growing` hold as glossed. The checker's environment audit reproduces independently. | — |
| 3. P19: do the laws hold with no premise about the unfolding? | **Yes, within the representation.** They are stated of every web and every amount. Counting needs decidable determinations (`mark`). `standing_recurs_iff` needs nothing further, since `0 < level` is decidable. The activity laws need decidable activity. Without it, the finite-world law gives excluded middle (N1). | M2 |
| 4. P19: is the content more than definitional? | **Partly.** `change_readings` is six `Iff.rfl`: arising *is* coming to be of activity, by definition. `over_stretch` telescopes. `keep_pace` and `coming_recurs_iff` follow from two-valuedness and finiteness. The module says so ("A determination counts as zero or one, so both hold of it"). The chapter's single "law" tag does not. | M9 |
| 5. P19: are `Dawn` and `Dusk` genuine? | **Yes.** Each recurs without the other, and each has infinitely many formations. | — |
| 6. P20: are the exchange theorems correct? | **Yes.** `falls_cover`, `falls_of_taking`, `depletes`, `rise_with_fall`, `standing_with_fall`, `rise_alone_opens` and `rise_exchange` hold. `depletes` needs a taker at each event step, and `rise_with_fall` needs the family dissipated on at the step. The record and the module say both. The chapter, the record title, the plan and the §9 table drop one or the other. | M5 |
| 7. P20: does the depletion premise follow? | **Only with taking.** It follows for an event at whose steps the family is dissipated on and taken from. Balance and dissipation alone do not give it (N3). | M5 |
| 8. P21: is `price` correct, and fairly called Price's equation? | **Correct; the counting form is disclosed; the gloss is wrong.** The identity is offspring + lowered = selected + raised. The parents' unweighted total appears nowhere, and `selected` is k × the parents' total under uniform reproduction (N5). | M3 |
| 9. P21: do only supported formations leave descendants? | **Yes, where only active formations give and activity needs support.** Both premises are stated (`unsupported_childless`, `never_supported_childless`, `selected_le`, `selection_within`). | — |
| 10. P21: is transmission disclosed as a premise? | **Yes** (`TransmitsWithin`, chapter item 8, §8 empirical correspondence). The gloss "was met at the giving step" drops the bound δ (N4). `Drawdown` and `Unchecked` are genuine. | M6 |
| 11. P22: does `World` embed the two-kind reading? | **Yes.** `ofRoles` with `generative_ofRoles`, `degenerative_ofRoles` and the `roles_*` transfer lemmas of `Roles` (balance, `Acting`, `Taking`, `Dissipative`, `Dependent`, undermining). | — |
| 12. P22: are "the laws hold of the whole space" earned? | **As a statement of quantifier form, yes; as new content, no.** The laws are stated of every web and amount, so they hold of every world. Space adds no law: the study concedes that `generative_iff` is `unceasing_iff` read of worlds. | M9 |
| 13. P22: are the witnesses of `contingent`, `living_crosses` and `rests_needs` non-vacuous? | **`contingent`: yes, all seven pairs.** **`living_crosses`: three corners are robust; the `spending` corner rests on a reading open to Ren** (N6 supplies one that does not). **`rests_needs`: `unbalanced` has vacuous dissipation** (N7 supplies one that does not); `flicker`'s vacuity is forced in the long run. | M7, M8 |
| 14. P22: is `Living` described accurately? | **Yes.** `World.Living` is "every event is living" of `Web.valuation`: no active relatum undermines. | — |
| 15. P22: is Ren's proposal turned into a no-axiom claim? | **No.** The module, the record, the study and the chapter all say that Space does not show that the theory needs no axiom. | — |
| 16. P19 and P22: is a reading chosen for Ren? | **Yes.** P19 reads coming to be and ceasing to be as generation and degeneration, labelled as the author's reading. P22 defines the generative and degenerative parts as arising and ceasing recurring, and on that reading they "are one part" in finite worlds. The canonical chapter states this without Ren's 9 October statement that they do not overlap, and without listing the reading among Ren's choices. | M1 |
| 17. P23: are the status tags right? | **Mostly.** Items 1, 3, 5–7 and 9–11 are tagged correctly. Item 2's price gloss is wrong; item 4 omits premises in three clauses; item 8 omits δ; the "law" tag covers three kinds. | M3–M6, M9 |
| 18. P23: is any open item lost or misclassified? | **None is lost.** Every "next inference" of the old §8 has a place in the four classes. Wisdom is filed under further proofs, and the reading of "generative, degenerative" is not listed among Ren's choices. | M1, M9 |
| 19. P23: is completion overstated? | **No.** "The completeness of a formal statement, not a proof of necessity" appears in item 11, §8, the foundation's spine status and the foundation record. The plan's criteria 2 and 3 are partly unmet, and the status does not say which. | M2, M9 |
| 20. P23: are the representation's commitments disclosed wherever laws are said to hold of every world? | **Discrete steps, natural-number amounts and the shared index: yes. Decidability: no.** | M2 |
| 21. Records, receipt and counts | **Correct**, with bookkeeping in M10. | M10 |

**Status of L1–L10.**

| Item | Status | Evidence |
|---|---|---|
| L1 | closed | `Roles.lean:38`, `:397` and `:435` read "An embodied relatum as a condition". The record's title reads "回答“生作为生的条件”：……". The zh sentence of chapter §2 is deleted. In the chapter, "生命" occurs only at lines 30, 469 and 477, all general uses. "need not be a life" and "a life that bears" survive only in marked originals. |
| L2 | closed | `Dissipation.lean:5` reads "recurring taking opens finite families and, enclosed around, draws in". The `related` entries of whole-persists-through-generation (to theory-of-becoming-foundation) and identity-across-steps (to whole-persists-through-generation) state the record title's condition and drop "made of". |
| L3 | closed, with one new pattern | (a) "给予者" survives only in marked originals and history, with one new residue in P21's own text (M10(c)). (b) The checker audits every constant of the closure; its 30 generated `injEq` lemmas equal this review's enumeration. (c) §24's rebuttals run 1–6. (d) "uses no reserve" is in place. (e) The English P16b paragraph reads "The package now has 676 theorems", marked as a P18b correction. (f) The convention is in `RESULT-WORKFLOW.md` line 50; four new stamps postdate their commits (M10(a)). |
| L4 | closed | "can be a held condition"; `Seed.no_held` and `Viable.no_held` are core theorems. |
| L5 | closed | The gloss of `carries_of_held` now reads "taken from, by whatever takes part" (`Reserve.lean:18`, `:201`); `Flow.carries_of_own` gives the holder's own form, and `Famine.carries` uses it. |
| L6 | closed | `Web.redirect`, `redirect_same`, `redirect_dependent`, `Famine.undermines_one`, `transformed_not_undermining` and `living_differs` are in the core; the choice of reading is listed among Ren's choices (chapter §8). |
| L7 | closed | `Balances.rise_given`, `Web.ComesToStand.rises`, `Web.rising_of_coming`, `rise_replenishes`, `rising_needs_replenishment`, the five `rising_*` dissipation theorems and `Growing` are in the core, and the `standing_*` theorems are derived from them with unchanged statements. |
| L8 | closed | `LivesOn.stands` and `Drowsy` are in `Descent`; each gloss of `LivesOn.active` states embodiment. |
| L9 | closed | "体现第一次进入估值" no longer occurs; the identification is named instead. |
| L10 | closed | `Flow.DescendsAt` (now in `Evolution`) is `g ∈ L.present t ∧ 0 < L.give t g x ∧ W.ComesToStand t x`. `Stranger.stranger` and `Brood.not_descends` are theorems. That descent counts gift entries rather than net flow is written as "a further choice of reading" in living-on-and-descent's limitations. |

## 2. Findings

### M1. overclaim (a reading chosen for Ren): Ren's "generative" and "degenerative" are read as arising and ceasing, and so "are one part"

**Location.**

- `Space.lean:6–11` (module doc): "Ren proposed that counting all the space, generative and degenerative, gives the theory of becoming. This module states the structure of that proposal. … The generative, degenerative and living parts are non-empty, and they overlap."
- `Space.lean:77–83`: `World.Generative := w.web.Unceasing` ("Generation recurs: some relatum arises at arbitrarily late steps") and `World.Degenerative` ("Degeneration recurs: some relatum ceases at arbitrarily late steps").
- Chapter, the theory stated in full: item 2 (lines 70, 102, tagged law), "活动可判定的有限世界中，生成复现恰当退化复现"; item 4 (lines 76, 108, tagged theorem), "有限世界中，生成的部分与退化的部分是同一部分 / In a finite world the generative and degenerative parts are one part; only with infinitely many relata do they separate".
- Chapter §2 (line 215), §8 status row "整体的规律" (line 510: "有限世界中生成与退化是同一部分") and glossary (line 687: "生成的／退化的 … 有限世界中两者是同一部分").
- Study §30 (line 1884): "“生成的”与“退化的”不是整体的两半，在有限的展开中它们是同一个部分".
- Record space-and-its-parts: the title, and the correspondence "this result gives that reading its formal structure … the generative, degenerative and living parts are all non-empty and overlap".
- Foundation §5, row 1 (line 72): "in a finite world generation recurs exactly when degeneration does, with no premise".
- The reading begins in P19. Study §26 (line 1643): "生成与退化不是两个可以分开的过程，在有限之中它们一同复现"; its rebuttal 1 (line 1650): "这正是 Ren 提议中“计入整个空间，包括生成与退化”的一个形式陈述……这一条把生成与退化绑在一起"; the English P19 paragraph (line 2109): "In any finite family, generation and degeneration recur together"; and the correspondence of coming-and-ceasing-keep-pace. These are labelled as the author's reading (an AI argument). P22 then turns the reading into the definitions of the parts of the space.

**Ren's words.** On 9 October, after an AI explanation of renewing and consuming formations, Ren asked ([source](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md), line 38):

> 为什么？我G0是什么？generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧

The study records this as supported by Ren's words (line 66). The AI correction in the same source (line 44) states that generation and degeneration, as relations, do not overlap (`renewing_not_consuming`), while one occurrence can take part in both.

**What the Lean says.** `generative_iff` is correct: in a finite world with decided activity, some relatum arises at arbitrarily late steps exactly when some relatum ceases at arbitrarily late steps. Neither definition mentions renewal, consumption, support or undermining. `Arises` includes arising that depends on depletion. The study's P11b correction (H7) and the chapter (line 267) already label "generation as arising" as the author's reading of the second 生. The plan's own acceptance for P22 (line 237) read the degenerative part as "消耗、终结" (consumption and ending); the module implements ceasing only.

**Why it matters.**

- The words "generative" and "degenerative" are Ren's, from the proposal that P22 sets out to structure. On the module's reading, the canonical chapter states as a theorem that they are one part in every finite world. Ren has said that they do not overlap.
- The chapter does not mention Ren's statement. Item 4 carries no label that this is the AI's reading of Ren's words.
- §8 lists among Ren's choices "the scope of the second 生, and whether arising that depends on depletion counts as generation", and the record leaves the names to Ren. Neither says which reading of the proposal's "generative, degenerative" the parts of the space take.
- "This module states the structure of that proposal" makes one reading of the proposal into its structure.
- This is the reading that the 9 October correction identified as an AI misreading: `generative` as any arising.
- The study's own boundary is right ("这些读法是 AI 的表述，名称由 Ren 定"); the canonical texts drop it.

**Correction.**

- State the law in the AI's own terms: "in a finite world whose activity is decided, arising recurs exactly when ceasing recurs". It is `Web.unceasing_iff` read of worlds. Name the parts accordingly (for example `World.ArisingRecurs` and `World.CeasingRecurs`, 生起复现／止息复现), or keep the present names only with the label "under the AI's reading of generation as arising".
- Remove "the generative and degenerative parts are one part" and "they overlap" from chapter items 2 and 4, §2, the §8 row, the glossary, the module doc, the record's title and correspondence, study §30 and foundation row 1. Alternatively, keep them labelled, next to Ren's 9 October words and to the relational reading under which generation and degeneration do not overlap as relations (`renewing_not_consuming`).
- Add to §8 Ren's choices: which reading of the proposal's "generative, degenerative" the parts of the space take. Candidates already on the spine include arising and ceasing recurring (on which they coincide in finite worlds) and renewing and consuming formations (on which they do not overlap as relations). This review does not choose between them.
- Write "states one structure for that proposal (an AI reading)" in the module doc and the record.
- Note in plan row 237 that the degenerative part was implemented as ceasing recurring, and that consumption is not part of `World.Degenerative`.

### M2. overclaim (omitted premise): decidability, which for the finite-world law is excluded middle, is left out of the representation's commitments

**Location.**

- Chapter, the definition of the status tags (lines 62, 94): the representation is "离散的步、自然数的量、把条件与关系项对应起来的共同索引 / discrete steps, natural-number amounts and a shared index".
- Chapter §8, philosophical warrant, "the scope of representation" (lines 543, 549): the same three.
- Foundation "Spine status" (line 78): the same three.
- Foundation §5, row 1 (line 72): "in a finite world generation recurs exactly when degeneration does, with no premise".
- Record theory-of-becoming-foundation, `related` entry for coming-and-ceasing-keep-pace: "in a finite family coming to be and ceasing to be recur together, with no premise / 有限族中生成与消失一同复现，无需前提".
- Chapter item 4 (lines 76, 108): the `World.rests` clause omits decidability, which `rests` assumes.

By contrast, `Change.lean:9–12` lists decidability among the representation's commitments ("counting needs the determination counted to be decidable at each step"), and so does criterion 2 of plan §9, in both languages. The space-and-its-parts record states it as a hypothesis, and chapter item 2 states it for `generative_iff`.

**What the Lean says.** `mark`, `held_over_stretch`, `keep_pace` and `coming_recurs_iff` take `[∀ a t, Decidable (p a t)]`. `Web.unceasing_iff`, `World.generative_iff` and `World.rests` take decidable activity. `standing_recurs_iff` needs no instance, because `0 < level` is decidable on `Nat`.

**Probe N1.** `Review9.Undecided.law_gives_em`:

```lean
theorem law_gives_em (law : ∀ w : World, w.Finite → w.Generative → w.Degenerative)
    (Q : Prop) : Q ∨ ¬ Q
```

The world has one relatum, no flow, and activity of period four: inactive, active, `Q`, inactive. It is finite, and it arises at the start of every period whatever `Q` is. Any ceasing it has decides `Q`: a ceasing out of the second phase gives `¬ Q`, and one out of the third gives `Q`. So a proof of the finite-world law for every world, without decidability, is a proof of excluded middle for every proposition.

**Why it matters.**

- Study §30 rebuttal 2 (line 1892) answers that decidability is "not a substantive premise about the unfolding but a requirement of constructive proof", since classically every world's activity is decidable. The first half is right. The second half means that the law over every world uses a logical axiom.
- Ren's priority directive asks that logical machinery be disclosed separately: "Disclose logical machinery, methodological commitments, model hypotheses, correspondence assumptions and normative premises separately" ([source](../../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md), item 4).
- P23 says the laws hold "of every world so represented". The lists of what "so represented" means are where this commitment belongs. Foundation row 1 is the row offered as evidence for the strong zero-axiom target, and it says "with no premise".

**Correction.**

- Add "decidability of each determination counted at each step (for every world, excluded middle)" to the three lists.
- In foundation row 1 and in the foundation record's `related` entry, write "in a finite world whose activity is decided".
- Add decidability to the `rests` clause of item 4.
- In §8, file "the law for finite worlds whose activity is not decided" under the disclosure of logical machinery as well as under further proofs: by N1 it holds there only with excluded middle, so it cannot enter the pure core.

### M3. error (in prose): what `price` divides

**Location.** Chapter item 2 (lines 71, 103): "从亲代到后代的变化分为选择项与传递项 / the change from parents to offspring divides into a selection term and a transmission term"; chapter §2 (line 287); `Evolution.lean:19–24` ("the change from parents to offspring divides into selection, the weighting of parents by their offspring, and transmission"); the record evolution-on-descent's claim; study §29.

**What the Lean says.** `price ps kids a b : offspring ps kids b + lowered ps kids a b = selected ps kids a + raised ps kids a b`, where `selected ps kids a = Σ_p |kids p| · a p`.

- The parents' own total `Σ_p a p` appears nowhere. The identity therefore does not decompose a change from parents to offspring. It divides the offspring's total into the parents' amounts weighted by their offspring, and the transmission change.
- **Probe N5.** `selected_uniform`: where every parent has `k` offspring, `selected ps kids a = k * total ps a`. No differential reproduction enters it. `one_each`: one parent with one offspring, both at five, gives `selected = 5` and `raised = lowered = 0`. Nothing is selected, and the "selection term" is five.
- In the usual statement of Price's equation, the selection term is the covariance of offspring number and amount, which is zero here. `selected` equals the total offspring number times the parents' mean, plus the number of parents times that covariance, so it contains a baseline beside selection.
- Plan row 236, chapter §2 and the record's correspondence and limitations call `price` an accounting identity (会计恒等式), and the record notes that two research notes derive its covariance form by hand. The chapter's full statement, the module doc and the record's claim still say that it divides "the change from parents to offspring".

**Correction.** Write: "Over any finite family of parents and offspring, the offspring's total divides into the parents' amounts weighted by their offspring and the change in transmission (`price`, an accounting identity in the counting form of Price's equation; the selection term proper, the covariance, is not stated)". In prose, call `selected` "the parents' amounts weighted by their offspring". `selected_le` and `selection_within` are correct as statements about that weighted total. The covariance form is already listed open.

### M4. overclaim (omitted premise): continued generation "under dissipation" goes beyond every finite part

**Location.** Chapter item 4, last clause (lines 76, 108): "在耗散之下继续生成，展开须越出每个有限部分，被围住时从其外汲入 / under dissipation, continued generation needs the unfolding to go beyond every finite part, and enclosed around, a part draws in (`generation_opens`, `generation_draws_in`)".

**What the Lean says.** `Web.generation_opens` and `Web.generation_draws_in` (`Roles.lean:623–640`) assume `L.Balances W`, and their arising members must be `Embodied`, in a finite family without repetition.

**Counterexamples in the core.**

- `World.flicker_world`: finite, balanced, dissipative and generative; its arising is not embodied.
- `World.unbalanced_world`: finite, dissipative, every relatum embodied, and generative; it is not balanced.

In both, generation continues under dissipation within one finite part. The sentence before this one, about `World.rests`, states balance and embodied arising; this one drops them. Probe N7 (`Leaking`) repeats the second counterexample with non-vacuous dissipation (M8).

**Correction.** "Under balance and dissipation, embodied members of a finite family that arise at arbitrarily late steps leave the family open at arbitrarily late steps, and enclosed around, it draws in."

### M5. overclaim (omitted premise): a rise "under dissipation", and depletion "from balance and dissipation"

**(a) The rise.**

- *Location.* Chapter item 4, first sentence (lines 76, 108): "在平衡与耗散之下，一个成员上升，同一步上另一个成员下降 / Under balance and dissipation, a member rising comes with another member falling across the same step". Title of the record rising-and-falling-in-one-exchange: "under dissipation, a member rising comes with another member falling across the same step".
- *What the Lean says.* `rise_with_fall` assumes `L.DissipatesOn ds t` for the family `ds` that contains the rising member. Under `Dissipative`, this holds only for finite families without repetition that are closed across the step.
- *Probe N2.* In `Spray`, one formation gives a unit to every condition in `Nat` and takes nothing, and every condition stands at the number of steps so far. The flow balances. It is dissipative, because no finite family is closed across any step. Only active formations give. Condition 0 rises across step 0, and no condition ever falls. So the sentence fails for every family once "dissipated on" is dropped.
- *Correction.* "Across a step at which a family is dissipated on (under `Dissipative`, a finite family without repetition closed across that step), a member rising comes with another member of the family falling." The record's claim already says this; its title and the chapter should too.

**(b) Depletion.**

- *Location.* Chapter §8 row "继续生成" (line 509): "消耗前提由平衡与耗散推出"; §9 row `Dissipation` (line 610): "消耗前提由此推出"; plan row 235: "`Balances.depletes`（`Generation` 的消耗前提由平衡与耗散推出）".
- *What the Lean says.* `Balances.depletes` also assumes `0 < L.takers ds t` at every step of the event.
- *Probe N3.* In `Still`, the still flow balances a constant web and is dissipative, and the event occurring at every step does not deplete the family.
- *Correction.* "for an event at whose steps the family is dissipated on and taken from", as the record, `Dissipation`'s module doc and `Generation`'s module doc already say.

### M6. overclaim (omitted premise): "a transmitted need was met at the giving step"

**Location.** Chapter item 8 (lines 86, 118): "传下来的所需曾在给予之步被满足 / a transmitted need was met at the giving step"; chapter §2 (line 287), §8 row "演化" (line 511: "传下来的所需曾被满足") and §9 row `Evolution` (line 613).

**What the Lean says.** `Flow.transmitted_supported` gives `W.need (t + 1) x c ≤ W.level t c + δ`. The descendant's need is at most the level at the giving step plus the bound of transmission. It is met there only when `δ = 0`. The record's title ("what is transmitted within a bound was selected") and the package README ("within a bound") are correct.

**Probe N4.** In `Within`, the flow balances, only active formations give, activity needs support, and the dependence on the pool is transmitted within one. The child descends from the parent across step 0. Its need (two) exceeds the pool's level (one) at the giving step and at every step: the transmitted need was never met.

**Correction.** "A transmitted need exceeds its condition's level at the giving step by at most the bound of transmission; with bound zero, it was met there."

### M7. missing counterexample: "living crosses generation" leans on a reading that is Ren's to choose

**Location.** `World.living_crosses` (`Space.lean:470`), with `spending_world` (`:240`) and `Spending.spends` (`:220`); chapter item 10 (lines 88, 120) and §2 (line 215); study §30 (line 1885): "`handing` 与 `spending` 的活动完全相同，只差各侧是否汲取自身的水平：活与否不由生成与止息的样式决定，而由汲取与依存的关系决定".

**What the Lean says.**

- The only witness of "generation recurs and some event is not living" is `spending`.
- Its event that is not living (`Spending.spends`) is the holder drawing on its own standing across the step at which it stops being active. That is an embodied relatum that bears on itself, drawn on by itself across the step at which it ends.
- Chapter §8 (lines 523, 532) lists exactly this as Ren's choice: "Whether drawing on a self-bearing embodied relatum across the step at which it ends counts as not living, and for which drawers."
- If Ren chooses that it does not count, every event of `spending` is living and the corner has no witness.

**Probe N6.** `Predator` adds a pool, a grazer and a browser to `Handing`.

- The sides draw only on their own standing, and nothing depends on it.
- The grazer and the browser depend on the pool at needs one and two. Both are active at step 0, when the grazer takes one unit of the pool.
- The world is finite and generative, and it is `Dependent`, balanced, `Acting` and `Taking`. It is not `Living`: the grazer's event undermines the browser's dependence.
- The event draws on the pool. The pool is not the drawer and is never active, and the grazer's own dependence is still met after the step (`not_self`).

So the corner holds under either choice.

**Correction.** Add such a witness to `Space` and cite it in `living_crosses`. Otherwise, state that the `spending` corner rests on the stepwise reading's verdict on self-drawing at an ending. In either case, qualify the study's inference from the `handing`/`spending` pair: as it stands, the pair shows it only under that verdict.

### M8. missing counterexample (vacuous witness): balance in `rests_needs`

**Location.** `World.unbalanced` (`Space.lean:323`) and `rests_needs` (`:482`); the module doc ("the same sides without any flow keep generating without balance") and the record.

**What the Lean says.** `unbalanced` has the still flow, so its dissipation holds because nothing takes part. It shows that balance is needed only among worlds with no exchange at all. The module discloses "without any flow". It does not say that the dissipation premise is then vacuous.

**Probe N7.** `Leaking` keeps `Handing.web`, with a flow in which the holder takes its own unit and gives nothing. The world is finite and generative, and every relatum is embodied. It is dissipative, with the family of both sides closed and taken from at every step. Only balance fails.

For embodiment (`flicker`) the vacuity is forced in the long run. In a finite, balanced, dissipative world, taking does not recur (`Flow.Dissipative.finite_ceases`). So any such witness is without exchange in its tail.

**Correction.** Replace `unbalanced` with, or add beside it, a witness like `Leaking`, and note that `flicker`'s vacuity is forced. This is minor.

### M9. presentation: status tags, the classes of open items, and the plan's completeness criteria

**(a) The "law" tag covers three kinds.**

- Identities by definition: `change_readings` is `⟨.rfl, .rfl, .rfl, .rfl, .rfl, .rfl⟩`.
- Arithmetic identities: `over_stretch` telescopes, and `price` is an accounting identity.
- Consequences of two-valuedness and finiteness: `keep_pace`, `coming_recurs_iff` and `generative_iff`.

None excludes any world's dynamics beyond what two-valued determinations, natural-number amounts and finiteness exclude. Study §26 rebuttal 1 (line 1650) answers the charge of triviality: "证明是计数，内容不是：它说在任何有限的展开中，生成与退化同步". That content depends on reading arising as generation and ceasing as degeneration (M1). Read neutrally, it is that a two-valued determination which changes infinitely often changes in both directions infinitely often. Ren's priority directive (item 5) asks that including every outcome type lead to "an explanation of actual possibilities and constraints, not an unconstrained catalogue". Item 11 and foundation row 4 say that the laws locate the whole claim rather than discharge it, which is right. The tag should also say which kind each law is, so that "laws of the whole" is not read as dynamical content.

**(b) Wisdom.** "Explaining how wisdom actually forms" (lines 569, 577) is filed under further proofs. It is an explanatory and empirical task. Its old "next inference" fits empirical correspondence or philosophical warrant better.

**(c) The plan's four-part completeness.** Plan §9 states four checkable criteria. The P23 row is ticked, but criteria 2 and 3 are partly unmet, and the status does not say so.

- Criterion 2's decidability is dropped downstream (M2).
- Criterion 3 asks that "each dynamical premise" pick out a proper part. It is shown for seven premises. `Census`, `TransmitsWithin`, `Around`, `Decays`, `NoSplit`, `Depletes` and `RenewedBy` are not mapped. Chapter §8 and foundation row 5 disclose this.
- The "mixed" part named in criterion 3 is not defined in `Space`.

**Correction.**

- Mark each law as identity, arithmetic, or consequence of finiteness and two-valuedness.
- Move the wisdom item.
- State in plan row 238 and study §31 which completeness criteria are met and which are not.

### M10. presentation (bookkeeping): stamps after their commits, the foundation record's Chinese vocabulary, and a "给予者" residue

**(a) Review stamps.** `RESULT-WORKFLOW.md` line 50 defines `reviewed_at_utc` as "the documentary review time". Four stamps are later than the commit that first contains them:

| Record | Stamp | Commit time (UTC) |
|---|---|---|
| evolution-on-descent | 11:40:00 | P21 `85b6d341`, 11:34:09 |
| space-and-its-parts | 12:00:00 | P22 `5211c769`, 11:52:54 |
| theory-of-becoming-foundation | 12:30:00 | P23 `c6335c48`, 12:09:37 |
| generation-is-replenishment | 12:10:00 | P23 `c6335c48`, 12:09:37 |

A time after the commit cannot be the time of a revision in it. The P19 and P20 stamps (10:05:00 and 11:05:00) precede their commits. **Correction:** use the actual time of the content revision, at or before the commit.

**(b) The foundation record's Chinese.** Its `related` entry for coming-and-ceasing-keep-pace reads "生起与终止、形成与消解、立起与不再立是同一变化的三种读法；有限族中生成与消失一同复现，无需前提". The chapter uses 止息, 开始与不再作为条件而在, and 开始成立与不再成立. "生成与消失" for coming to be and ceasing to be also carries M1. **Correction:** use the chapter's terms.

**(c) "给予者".** Study §29 rebuttal 3 (line 1840), written in P21, says "一类读法中的世系只说给予者给予". This is current text, which K8(c) and L3(a) moved to "给予它的关系项／形成". **Correction:** "只说给予它的形成给予".

## 3. What remains sound

- **The theorems.**
  - Every P18b, P19, P20, P21 and P22 theorem holds as stated, and P23 adds no Lean.
  - The 27-module core closure recompiles from the prelude. All 1571 source declarations have empty axiom reports. The 30 generated `injEq` lemmas are the only constants of the closure that depend on an axiom, as the receipt says.
  - The counts, receipt, source hashes, retained artifacts, reference hashes, aliases and bindings are correct.
- **P18b.**
  - Every L1–L10 item is closed at the located places, and the probes became core theorems.
  - The checker now audits every constant of the closure, and the audit reproduces independently.
- **P19.**
  - `over_stretch`, `family_over_stretch`, `fallen_within`, `risen_within`, `rising_recurs`, `falling_recurs`, `held_over_stretch`, `keep_pace`, `coming_recurs_iff`, `standing_recurs_iff`, `unceasing_iff`, `supported_of` and `falls_finitely_from_floor` are correct.
  - The module doc discloses its representational commitments, including decidability.
  - `Dawn` and `Dusk` show that finiteness does the work.
- **P20.** `falls_cover` gives a quantity: across a step dissipated on, falls cover rises plus one per taker. The module and the record state every premise. Calling the result "rising and falling", not "coming to be and ceasing", is an accurate self-correction.
- **P21.**
  - Descent requires the giver to take part.
  - Selection through support is correctly premised on `Acting` and `Dependent`.
  - `TransmitsWithin` is disclosed as a premise, not derived.
  - `Drawdown` shows transmission, variation, selection and the feedback of activity on selection in one unfolding. `Unchecked` shows what `Dependent` does.
  - Fitness is not defined, and the evolution programme keeps its scope.
- **P22.**
  - `World`, `ofRoles` and the transfer lemmas are sound.
  - `contingent` exhibits a world meeting and a world failing each of seven premises.
  - `separate` derives the infinitude of the separating worlds from the law.
  - `rests` and its four counterexamples are correct.
  - `Living` is the stepwise valuation's "every event living". No part is evaluated, and the module says that it does not show that no axiom is needed.
- **P23.**
  - The full statement gives every item a status, and no open item of the old §8 is lost.
  - G0 is tagged as an axiom adopted with Ren's authorization and not derived from the laws.
  - "The completeness of a formal statement, not a proof of necessity" and "whether every becoming can be so represented is part of the warrant still needed" are written consistently in the chapter, foundation and record.
  - The two targets, the whole's deductive necessity and the ethical orientation within it, stay separate.
- **Method and provenance.**
  - Ren's words are quoted exactly, and the study labels its readings as AI's.
  - No ethical predicate enters L1–L3. No cost or payment vocabulary returns in the new text; its one "代价 / cost" (study §26 rebuttal 4 and the English P19 paragraph) denies that ceasing is a cost of generation.

## 4. What would change these verdicts

1. **Generative and degenerative (M1).** State the finite-world law as arising and ceasing recurring, and remove "one part" and "overlap" from the canonical texts. Alternatively, label them as the AI's reading beside Ren's 9 October words. Then add the reading of the proposal's parts to Ren's choices.
2. **Decidability (M2).** Add it to every list of the representation's commitments, restore it in foundation row 1, the foundation record and item 4, and file the undecided law under logical machinery.
3. **`price` (M3).** Describe what it divides, and reserve "selection term" for the covariance.
4. **Premises in the full statement (M4–M6).** Restore balance and embodied arising in item 4's last clause, "the family dissipated on" in its first clause and in the record title, "and taken from" in the depletion clause of §8, §9 and the plan, and δ in item 8.
5. **Witnesses (M7, M8).** Add a living-crosses witness that does not draw on itself at its ending, or state the dependence on Ren's choice; add a non-vacuous balance witness.
6. **Presentation (M9, M10).** Sub-tags for the laws, the wisdom item, the plan's criteria, the stamps, the foundation record's terms and the "给予者" residue.
7. **Ren's choices.** These stay open and are not settled here:
   - the reading of "generative, degenerative" in the proposal (M1);
   - the reading of 生, 生生 and the second 生, including whether arising that depends on depletion is generation;
   - whether drawing on a self-bearing embodied relatum at its ending counts as not living, and for which drawers;
   - the reading of succession and the level at which 生生不息 is read;
   - whether living on and descent are adopted as direct valuations;
   - the names.
8. A finding would also fall if its probe misread a published definition. Every probe imports the unchanged `Becoming` and uses the definitions as they stand at `c6335c48`.

**Not checked.**

- `Becoming.Bridge` and the Mathlib periphery were not rebuilt. The bridge is unchanged since `badb652e`, and its bytes match the receipt. Its 26 aliases, the five periphery aliases and ten inherited aliases did not resolve here, nor did 84 reference names (38 bridge, 36 inherited, 6 periphery, and 4 inherited names mentioned in core prose).
- The generated overview pages and `make research-check` were not run, since they write into the live repository.
- No external literature was consulted. The remark on Price's covariance form is general knowledge, used only to say what the identity does not state.
- Parity between the Chinese and English texts was checked only for the passages quoted above.
- P24 (`e5b61937`) and P25 (`a69455e3`), committed during this review, were not read. Whether they already address any finding here is unchecked.
- The following were not built:
  - a non-vacuous witness for the necessity of embodiment in `rests` beyond the forced tail;
  - the covariance form of `price`;
  - the finite-world law in the periphery with classical logic.

## Appendix: probe sources and audit

Compiled with Lean 4.29.1 (`f72c35b3`) against the unchanged `c6335c48` core bytes, with `import Std` removed from `GenerativeCore` as the checker does. `Review9.lean` compiles with exit 0 and no warnings:

```text
LEAN_PATH=<build>:. lean -o Review9.olean Review9.lean        # exit 0, no output
LEAN_PATH=<build>:. lean Review9Audit.lean                    # exit 0
LEAN_PATH=<build>:. lean Review9Print.lean                    # exit 0
```

| File | sha256 |
|---|---|
| `Review9.lean` | `0e5031bc0ffc7d22ce58d45c4dd63412ec5c830c945ef077ead19f64bd0e156e` |
| `Review9Audit.lean` | `6489667489bc951714c5c7a970ed982eb620d8062f1a9d0c8570322346d804a9` |
| `Review9Print.lean` (generated: `#print axioms` for each of the 63 source declarations) | prefix `358f8e99bd927549` |

### `Review9.lean`

```lean
import Becoming

/-!
Probes of the ninth independent review (P18b through P23). Each is term-mode and
axiom-free; none is part of the repository.
-/

namespace Review9

open Becoming

/-! ## N1. The finite-world law without decidability gives excluded middle -/

namespace Undecided

/-- Period four: inactive, active, `Q`, inactive. -/
def act (Q : Prop) : Nat → Prop
  | 0 => False
  | 1 => True
  | 2 => Q
  | 3 => False
  | n + 4 => act Q n

/-- The starts of the periods. -/
def four : Nat → Nat
  | 0 => 0
  | n + 1 => four n + 4

theorem le_four : ∀ N, N ≤ four N
  | 0 => Nat.le_refl 0
  | N + 1 => Nat.add_le_add (le_four N) (Nat.le_add_left 1 3)

theorem arises_at (Q : Prop) : ∀ N, ¬ act Q (four N) ∧ act Q (four N + 1)
  | 0 => ⟨id, trivial⟩
  | N + 1 => arises_at Q N

def web (Q : Prop) : Web Unit Unit where
  level _ _ := 0
  active t _ := act Q t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- One relatum, no flow, activity of period four whose third phase is `Q`. -/
def world (Q : Prop) : World :=
  ⟨Unit, Flow.still, web Q⟩

theorem finite (Q : Prop) : (world Q).Finite :=
  ⟨[()], ⟨fun no => (nomatch no), trivial⟩, fun () => .head _⟩

/-- It generates whatever `Q` is: it arises at the start of every period. -/
theorem generative (Q : Prop) : (world Q).Generative :=
  fun N => ⟨four N, (), le_four N, arises_at Q N⟩

/-- Any ceasing decides `Q`. -/
theorem decides (Q : Prop) : ∀ t, act Q t → ¬ act Q (t + 1) → Q ∨ ¬ Q
  | 0, active, _ => False.elim active
  | 1, _, inactive => Or.inr inactive
  | 2, active, _ => Or.inl active
  | 3, active, _ => False.elim active
  | n + 4, active, inactive => decides Q n active inactive

/-- If every finite world that generates also degenerates, with no decidability supplied,
every proposition is decided. -/
theorem law_gives_em (law : ∀ w : World, w.Finite → w.Generative → w.Degenerative)
    (Q : Prop) : Q ∨ ¬ Q :=
  match law (world Q) (finite Q) (generative Q) 0 with
  | ⟨t, (), _, active, inactive⟩ => decides Q t active inactive

end Undecided

/-! ## N2. Under balance and dissipation a rise need not come with a fall -/

namespace Spray

/-- One formation gives a unit to every condition and takes nothing. -/
def flow : Flow Unit Nat :=
  ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 1⟩

/-- Every condition stands at the number of steps so far. -/
def web : Web Unit Nat where
  level t _ := t
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem balances : flow.Balances web :=
  fun _ _ => rfl

theorem outside (cs : List Nat) : ¬ (total cs (fun n => n) + 1) ∈ cs :=
  fun mem => Nat.not_succ_le_self _ (le_total_of_mem (q := fun n => n) mem)

/-- No finite family is closed across any step. -/
theorem never_closed (cs : List Nat) (t : Nat) : ¬ flow.ClosedAt cs t :=
  fun closed => Nat.not_succ_le_zero 0
    (Nat.le_of_eq (closed () (.head _) _ (outside cs)).2)

theorem dissipative : flow.Dissipative :=
  fun cs t _ closed => False.elim (never_closed cs t closed)

theorem acting : flow.Acting web :=
  fun _ _ _ _ _ => trivial

/-- The flow balances and is dissipative, only active formations give, a condition rises,
and no condition ever falls. -/
theorem spray :
    flow.Balances web ∧ flow.Dissipative ∧ flow.Acting web ∧ web.Rises 0 0 ∧
    ∀ t c, ¬ web.Falls t c :=
  ⟨balances, dissipative, acting, Nat.zero_lt_one,
   fun t _ falls => Nat.lt_irrefl t (Nat.lt_trans (Nat.lt_succ_self t) falls)⟩

end Spray

/-! ## N3. Balance and dissipation without taking do not deplete -/

namespace Still

def web : Web Unit Unit :=
  ⟨fun _ _ => 1, fun _ _ => False, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩

theorem still :
    (Flow.still : Flow Unit Unit).Balances web ∧ (Flow.still : Flow Unit Unit).Dissipative ∧
    ¬ web.Depletes [()] (fun _ => True) :=
  ⟨fun _ _ => rfl, Flow.still_dissipative,
   fun depletes => match depletes 0 trivial (fun _ _ rises => Nat.lt_irrefl 1 rises) with
    | ⟨_, _, falls⟩ => Nat.lt_irrefl 1 falls⟩

end Still

/-! ## N4. Transmission within one: the transmitted need was not met at the giving step -/

namespace Within

inductive Relatum
  | pool
  | parent
  | child

def web : Web Relatum Relatum where
  level t x := match x, t with
    | .pool, _ => 1
    | .parent, _ => 1
    | .child, 0 => 0
    | .child, _ + 1 => 1
  active t x := match x with
    | .pool => False
    | .parent => t = 0
    | .child => False
  requires _ x c := match x, c with
    | .pool, _ => False
    | .parent, .pool | .child, .pool => True
    | .parent, .parent | .parent, .child | .child, .parent | .child, .child => False
  need _ x _ := match x with
    | .pool => 0
    | .parent => 1
    | .child => 2
  draws _ _ _ := False

def flow : Flow Relatum Relatum where
  present t := match t with
    | 0 => [.parent]
    | _ + 1 => []
  take _ _ _ := 0
  give t f c := match t, f, c with
    | 0, .parent, .child => 1
    | 0, .parent, .pool | 0, .parent, .parent => 0
    | 0, .pool, _ | 0, .child, _ => 0
    | _ + 1, _, _ => 0

theorem dependent : web.Dependent
  | _, .pool, active => False.elim active
  | _, .child, active => False.elim active
  | _, .parent, rfl => fun c depends => match c with
    | .pool => Nat.le_refl 1
    | .parent => False.elim depends
    | .child => False.elim depends

/-- The flow balances, only active formations give, activity needs support, the
dependence on the pool is transmitted within one, the child descends from the parent, and
the child's need exceeds the pool's level at the giving step and at every step. -/
theorem within :
    flow.Balances web ∧ flow.Acting web ∧ web.Dependent ∧ flow.TransmitsWithin web .pool 1 ∧
    flow.DescendsAt web 0 .child .parent ∧ web.level 0 .pool < web.need 1 .child .pool ∧
    ∀ t, ¬ web.need t .child .pool ≤ web.level t .pool :=
  ⟨fun
    | 0, .pool => rfl
    | 0, .parent => rfl
    | 0, .child => rfl
    | _ + 1, .pool => rfl
    | _ + 1, .parent => rfl
    | _ + 1, .child => rfl,
   fun
    | 0, _, _, .head _, _ => rfl
    | 0, _, _, .tail _ rest, _ => nomatch rest
    | _ + 1, _, _, present, _ => (nomatch present),
   dependent,
   fun
    | 0, .child, _, ⟨.head _, _, _⟩, _ => ⟨trivial, Nat.le_refl 2⟩
    | 0, .pool, _, ⟨.head _, gives, _⟩, _ => absurd gives (Nat.lt_irrefl 0)
    | 0, .parent, _, ⟨.head _, gives, _⟩, _ => absurd gives (Nat.lt_irrefl 0)
    | 0, _, _, ⟨.tail _ rest, _, _⟩, _ => nomatch rest
    | _ + 1, _, _, ⟨present, _, _⟩, _ => (nomatch present),
   ⟨.head [], Nat.zero_lt_one, Nat.lt_irrefl 0, Nat.zero_lt_one⟩,
   Nat.lt_succ_self 1,
   fun _ le => Nat.not_succ_le_self 1 le⟩

end Within

/-! ## N5. The selection term of `price` without selection -/

/-- Where every parent has `k` offspring, the selection term is `k` times the parents'
total, whatever the amounts: nothing about differential reproduction enters it. -/
theorem selected_uniform {α : Type} (ps : List α) (kids : α → List α) (a : α → Nat) (k : Nat)
    (same : ∀ p, (kids p).length = k) : selected ps kids a = k * total ps a :=
  (total_congr (fun p => congrArg (· * a p) (same p)) ps).trans (total_mul k a ps)

/-- One parent, one offspring, both at five: no selection and no transmission change, and
the selection term is five. -/
theorem one_each :
    selected [()] (fun _ => [()]) (fun _ => 5) = 5 ∧
    raised [()] (fun _ => [()]) (fun _ => 5) (fun _ => 5) = 0 ∧
    lowered [()] (fun _ => [()]) (fun _ => 5) (fun _ => 5) = 0 ∧
    offspring [()] (fun _ => [()]) (fun _ => 5) = 5 :=
  ⟨rfl, rfl, rfl, rfl⟩

/-! ## N6. Generation recurring with an event not living, no self-drawing involved -/

namespace Predator

/-- The two sides of `Handing`, a pool, a grazer and a browser. -/
inductive Relatum
  | side (x : Bool)
  | pool
  | grazer
  | browser

def level : Nat → Relatum → Nat
  | t, .side y => Handing.stands y t
  | 0, .pool => 2
  | _ + 1, .pool => 1
  | _, .grazer => 1
  | _, .browser => 1

def active : Nat → Relatum → Prop
  | t, .side y => 0 < Handing.stands y t
  | _, .pool => False
  | t, .grazer => t = 0
  | t, .browser => t = 0

/-- Being the pool. -/
def isPool : Relatum → Prop
  | .side _ => False
  | .pool => True
  | .grazer => False
  | .browser => False

def requires : Nat → Relatum → Relatum → Prop
  | _, .side _, _ => False
  | _, .pool, _ => False
  | _, .grazer, c => isPool c
  | _, .browser, c => isPool c

def need : Nat → Relatum → Relatum → Nat
  | _, .side _, _ => 0
  | _, .pool, _ => 0
  | _, .grazer, _ => 1
  | _, .browser, _ => 2

/-- A side draws on its own standing while it stands. -/
def sideDraws (t : Nat) (y : Bool) : Relatum → Prop
  | .side z => z = y ∧ 0 < Handing.stands y t
  | .pool => False
  | .grazer => False
  | .browser => False

/-- The grazer draws on the pool at the first step. -/
def grazes (t : Nat) : Relatum → Prop
  | .side _ => False
  | .pool => t = 0
  | .grazer => False
  | .browser => False

def draws : Nat → Relatum → Relatum → Prop
  | t, .side y, c => sideDraws t y c
  | _, .pool, _ => False
  | t, .grazer, c => grazes t c
  | _, .browser, _ => False

/-- The sides hand a standing back and forth and draw on their own standing; the grazer
and the browser depend on the pool, at needs one and two, and are active at the first
step, when the grazer draws on the pool. -/
def web : Web Relatum Relatum :=
  ⟨level, active, requires, need, draws⟩

def present : Nat → List Relatum
  | 0 => [.side true, .grazer]
  | t + 1 => [.side (Handing.holder (t + 1))]

def sideTake (t : Nat) (x : Bool) : Relatum → Nat
  | .side y => Handing.flow.take t x y
  | .pool => 0
  | .grazer => 0
  | .browser => 0

def sideGive (t : Nat) (x : Bool) : Relatum → Nat
  | .side y => Handing.flow.give t x y
  | .pool => 0
  | .grazer => 0
  | .browser => 0

/-- A unit of the pool. -/
def poolUnit : Relatum → Nat
  | .side _ => 0
  | .pool => 1
  | .grazer => 0
  | .browser => 0

def take : Nat → Relatum → Relatum → Nat
  | t, .side x, c => sideTake t x c
  | _, .pool, _ => 0
  | _, .grazer, c => poolUnit c
  | _, .browser, _ => 0

def give : Nat → Relatum → Relatum → Nat
  | t, .side x, c => sideGive t x c
  | _, .pool, _ => 0
  | _, .grazer, _ => 0
  | _, .browser, _ => 0

/-- As in `Handing`, and across the first step the grazer takes a unit of the pool. -/
def flow : Flow Relatum Relatum :=
  ⟨present, take, give⟩

def world : World :=
  ⟨Relatum, flow, web⟩

/-- Reads a side's Boolean. -/
def sideOf : Relatum → Bool
  | .side x => x
  | .pool => false
  | .grazer => false
  | .browser => false

theorem mem_cons {a b : Relatum} {l : List Relatum} (mem : a ∈ b :: l) : a = b ∨ a ∈ l :=
  match mem with
  | .head _ => Or.inl rfl
  | .tail _ rest => Or.inr rest

theorem sides_distinct : ¬ Relatum.side true ∈ [Relatum.side false] :=
  fun mem => (mem_cons mem).elim
    (fun same => Bool.noConfusion (show true = false from congrArg sideOf same))
    (fun no => nomatch no)

theorem side_mem : ∀ x : Bool,
    Relatum.side x ∈ [.pool, .grazer, .browser, .side true, .side false]
  | true => .tail _ (.tail _ (.tail _ (.head _)))
  | false => .tail _ (.tail _ (.tail _ (.tail _ (.head _))))

theorem finite : world.Finite :=
  ⟨[.pool, .grazer, .browser, .side true, .side false],
   ⟨fun mem => match mem with | .tail _ (.tail _ (.tail _ (.tail _ no))) => (nomatch no),
    fun mem => match mem with | .tail _ (.tail _ (.tail _ no)) => (nomatch no),
    fun mem => match mem with | .tail _ (.tail _ no) => (nomatch no),
    sides_distinct,
    fun no => (nomatch no), trivial⟩,
   fun
    | .pool => .head _
    | .grazer => .tail _ (.head _)
    | .browser => .tail _ (.tail _ (.head _))
    | .side x => side_mem x⟩

theorem generative : world.Generative :=
  fun N => match Handing.recurs true N with
  | ⟨t, later, arises⟩ => ⟨t, .side true, later, arises⟩

theorem balanced : world.Balanced
  | 0, .side x => match x with
    | true => rfl
    | false => rfl
  | 0, .pool => rfl
  | 0, .grazer => rfl
  | 0, .browser => rfl
  | n + 1, .side y => Handing.balances (n + 1) y
  | _ + 1, .pool => rfl
  | _ + 1, .grazer => rfl
  | _ + 1, .browser => rfl

theorem acting : world.Acting
  | 0, _, _, .head _, _ => Nat.zero_lt_one
  | 0, _, _, .tail _ (.head _), gives => absurd gives (Nat.lt_irrefl 0)
  | 0, _, _, .tail _ (.tail _ rest), _ => nomatch rest
  | n + 1, _, _, .head _, _ => Handing.holder_stands (n + 1)
  | _ + 1, _, _, .tail _ rest, _ => nomatch rest

theorem side_taking (t : Nat) (x : Bool) (holds : 0 < Handing.stands x t) :
    ∀ c, 0 < take t (.side x) c → active t (.side x) ∧ draws t (.side x) c
  | .side _, takes => match World.Spending.self_taken takes with
    | rfl => ⟨holds, rfl, holds⟩
  | .pool, takes => absurd takes (Nat.lt_irrefl 0)
  | .grazer, takes => absurd takes (Nat.lt_irrefl 0)
  | .browser, takes => absurd takes (Nat.lt_irrefl 0)

theorem taking : world.Taking
  | 0, _, c, .head _, takes => side_taking 0 true Nat.zero_lt_one c takes
  | 0, _, c, .tail _ (.head _), takes => match c, takes with
    | .pool, _ => ⟨rfl, rfl⟩
    | .side _, takes => absurd takes (Nat.lt_irrefl 0)
    | .grazer, takes => absurd takes (Nat.lt_irrefl 0)
    | .browser, takes => absurd takes (Nat.lt_irrefl 0)
  | 0, _, _, .tail _ (.tail _ rest), _ => nomatch rest
  | n + 1, _, c, .head _, takes =>
    side_taking (n + 1) (Handing.holder (n + 1)) (Handing.holder_stands (n + 1)) c takes
  | _ + 1, _, _, .tail _ rest, _ => nomatch rest

theorem dependent : world.Dependent
  | _, .side _, _ => fun _ no => False.elim no
  | _, .pool, active => False.elim active
  | _, .grazer, rfl => fun c depends => match c, depends with
    | .pool, _ => Nat.le_succ 1
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no
  | _, .browser, rfl => fun c depends => match c, depends with
    | .pool, _ => Nat.le_refl 2
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no

/-- The grazer's event at the first step undermines the browser's dependence on the pool. -/
theorem not_living : ¬ world.Living :=
  fun living => living 0 .grazer rfl
    ⟨.pool, rfl, .browser, trivial,
     ⟨0, Nat.le_refl 0, fun _ _ _ => trivial, Nat.le_refl 2, Nat.lt_succ_self 1⟩,
     Nat.lt_succ_self 1⟩

/-- The grazer draws only on the pool, the pool is never active, and the grazer's own
dependence is still met after the step. -/
theorem not_self :
    (∀ t c, web.draws t .grazer c → c = .pool) ∧ (∀ t, ¬ web.active t .pool) ∧
    web.need 0 .grazer .pool ≤ web.level 1 .pool :=
  ⟨fun _ c drawn => match c, drawn with
    | .pool, _ => rfl
    | .side _, no => False.elim no
    | .grazer, no => False.elim no
    | .browser, no => False.elim no,
   fun _ active => active, Nat.le_refl 1⟩

/-- A finite world in which generation recurs and not every event is living, with every
premise that `spending` meets except embodiment; the event that is not living draws on a
pool that is not the drawer and never active. -/
theorem predator :
    world.Finite ∧ world.Generative ∧ ¬ world.Living ∧ world.Dependent ∧ world.Balanced ∧
    world.Acting ∧ world.Taking :=
  ⟨finite, generative, not_living, dependent, balanced, acting, taking⟩

end Predator

/-! ## N7. Balance needed with a non-vacuous dissipation -/

namespace Leaking

/-- Across each step the holder takes its own unit and gives nothing. -/
def flow : Flow Bool Bool :=
  ⟨fun t => [Handing.holder t], fun t x y => Handing.flow.take t x y, fun _ _ _ => 0⟩

def world : World :=
  ⟨Bool, flow, Handing.web⟩

theorem takes : ∀ t, 0 < total [true, false] (flow.take t (Handing.holder t))
  | 0 => Nat.zero_lt_one
  | 1 => Nat.zero_lt_one
  | t + 2 => takes t

/-- A finite world whose flow takes part at every step, with the family of both sides
closed and taken from at every step, and dissipative; whatever arises is embodied and
generation recurs; only balance fails. -/
theorem leaking :
    world.Finite ∧ world.Generative ∧ world.Dissipative ∧ world.Embodied ∧ ¬ world.Balanced ∧
    ∀ t, flow.ClosedAt [true, false] t ∧ 0 < total [true, false] (flow.take t (Handing.holder t)) :=
  ⟨⟨[true, false], Handing.distinct, Handing.every⟩,
   fun N => match Handing.recurs true N with
    | ⟨t, later, arises⟩ => ⟨t, true, later, arises⟩,
   fun cs _ _ _ _ _ => Nat.le_trans
     (Nat.le_of_eq ((congrArg (· + _) (total_zero cs)).trans (Nat.zero_add _))) (sign_le _),
   fun x => (Handing.embodied x).1,
   fun balanced => Nat.not_succ_le_zero 0 (Nat.le_of_eq (balanced 0 false)),
   fun t => ⟨fun _ _ c outside => absurd (Handing.every c) outside, takes t⟩⟩

end Leaking

end Review9
```

### `Review9Audit.lean`

```lean
import Lean
import Review9
open Lean Elab Command
#eval show CommandElabM Unit from do
  let env ← getEnv
  let some index := env.getModuleIdx? `Review9 | throwError "no module"
  let mut count := 0
  let mut withAx := 0
  let mut names : Array Name := #[]
  for (n, _) in env.constants.map₁.toList do
    if env.getModuleIdxFor? n == some index then
      count := count + 1
      names := names.push n
      let axioms ← liftCoreM <| Lean.collectAxioms n
      if axioms.size > 0 then
        withAx := withAx + 1
        logInfo m!"AXIOMS {n} {axioms.toList}"
  logInfo m!"CONSTANTS Review9 {count} WITHAXIOMS {withAx}"
#print axioms Review9.Undecided.law_gives_em
#print axioms Review9.Undecided.generative
#print axioms Review9.Spray.spray
#print axioms Review9.Still.still
#print axioms Review9.Within.within
#print axioms Review9.selected_uniform
#print axioms Review9.one_each
#print axioms Review9.Predator.predator
#print axioms Review9.Predator.not_self
#print axioms Review9.Leaking.leaking
```

Output:

```text
AXIOMS Review9.Predator.Relatum.side.injEq [propext]
CONSTANTS Review9 163 WITHAXIOMS 1
'Review9.Undecided.law_gives_em' does not depend on any axioms
'Review9.Undecided.generative' does not depend on any axioms
'Review9.Spray.spray' does not depend on any axioms
'Review9.Still.still' does not depend on any axioms
'Review9.Within.within' does not depend on any axioms
'Review9.selected_uniform' does not depend on any axioms
'Review9.one_each' does not depend on any axioms
'Review9.Predator.predator' does not depend on any axioms
'Review9.Predator.not_self' does not depend on any axioms
'Review9.Leaking.leaking' does not depend on any axioms
```

`Review9Print.lean` prints the axioms of all 63 source declarations of `Review9.lean` (32 theorems, 29 definitions, 2 inductive types); all 63 report "does not depend on any axioms". The one constant with an axiom, `Review9.Predator.Relatum.side.injEq`, is generated by Lean for the constructor with a field, like the 30 of the core.

### Core audits

`CoreAudit.lean` is `import Becoming` followed by one `#print axioms` line for each of the 1571 source declarations the receipt lists for the 27-module closure (1451 core, 120 foundation). All 1571 report "does not depend on any axioms".

`EnvAudit.lean` (`38b6efd1eb971b50…`) enumerates every constant of the closure, including compiler-generated ones:

```lean
import Lean
import Becoming
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  let mut total := 0
  let mut withAx := 0
  for m in [`GenerativeCore, `Becoming.Frame, `InquirySufficiency, `Becoming.Inquiry, `RelationalRenewal, `Becoming.Renewal, `Becoming.Dependence, `Becoming.Return, `Becoming.Horizon, `Becoming.Joint, `Becoming.Substitution, `Becoming.Generation, `Becoming.Flow, `Becoming.Change, `Becoming.Population, `Becoming.Identity, `Becoming.Wholes, `Becoming.Dissipation, `Becoming.Roles, `Becoming.Reserve, `Becoming.Evolution, `Becoming.Space, `Becoming.Metaethics, `Becoming.Ranking, `Becoming.Correspondence, `Becoming.Descent, `Becoming] do
    let some index := env.getModuleIdx? m | throwError m!"no module {m}"
    let mut count := 0
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then
          withAx := withAx + 1
          logInfo m!"AXIOMS {n} {axioms.toList}"
    total := total + count
    logInfo m!"CONSTANTS {m} {count}"
  logInfo m!"TOTAL {total} WITHAXIOMS {withAx}"
```

Output, summarized: constants per module GenerativeCore 54, Frame 61, InquirySufficiency 107, Inquiry 15, RelationalRenewal 134, Renewal 58, Dependence 475, Return 84, Horizon 43, Joint 203, Substitution 40, Generation 216, Flow 225, Change 96, Population 138, Identity 487, Wholes 147, Dissipation 318, Roles 463, Reserve 144, Evolution 114, Space 129, Metaethics 226, Ranking 170, Correspondence 159, Descent 117 and `Becoming` 0; `TOTAL 4423 WITHAXIOMS 30`. Each of the 30 is a generated `injEq` lemma depending only on `[propext]`, and the 30 names equal the receipt's `generated_axiom_dependencies`:

- GenerativeCore: `Generative.Process.mk.injEq`
- Becoming.Frame: `Becoming.Run.mk.injEq`, `Becoming.Frame.mk.injEq`
- InquirySufficiency: `Generative.InquirySufficiency.Policy.respond.injEq`, `Generative.InquirySufficiency.Policy.inquire.injEq`
- RelationalRenewal: `RelationalRenewal.Unfolding.mk.injEq`, `RelationalRenewal.Law.mk.injEq`
- Becoming.Renewal: `Becoming.Conditions.mk.injEq`
- Becoming.Dependence: `Becoming.Crossing.State.mk.injEq`, `Becoming.Crossing.Move.fall.injEq`, `Becoming.Dependence.mk.injEq`, `Becoming.Pinned.State.mk.injEq`, `Becoming.Web.mk.injEq`
- Becoming.Joint: `Becoming.Pool.Draw.mk.injEq`, `Becoming.Pool.State.mk.injEq`, `Becoming.Shock.State.mk.injEq`, `Becoming.Shock.Move.calm.injEq`
- Becoming.Flow: `Becoming.Flow.mk.injEq`
- Becoming.Identity: `Becoming.Reidentify.mk.injEq`, `Becoming.Confluence.Formation.new.injEq`
- Becoming.Wholes: `Becoming.Generations.Formation.member.injEq`
- Becoming.Dissipation: `Becoming.Frontier.Formation.grower.injEq`, `Becoming.Frontier.Condition.fuel.injEq`
- Becoming.Roles: `Becoming.Kindling.Relatum.side.injEq`, `Becoming.Kindling.Relatum.fuel.injEq`, `Becoming.SprayHanding.Relatum.aux.injEq`, `Becoming.SprayHanding.Relatum.side.injEq`
- Becoming.Space: `Becoming.World.mk.injEq`
- Becoming.Metaethics: `Becoming.Valuation.mk.injEq`
- Becoming.Correspondence: `Becoming.Web.Condition.mk.injEq`

`Change` and `Evolution` have none; `Space` has only `Becoming.World.mk.injEq`, the one added since P18b.
