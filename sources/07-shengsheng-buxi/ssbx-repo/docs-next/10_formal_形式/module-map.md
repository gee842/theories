# 模块地图

> 状态：v4 (2026-05-21) — 与当前工作树对齐。`Foundation/Bagua/` 已撤至 `Foundation/Atlas/Yi/`；`Foundation/Yi/` 同被并入 `Atlas/Yi/`；`Foundation/Squaring/` 不再作为目录存在（squaring 内容迁入 `R/Squaring.lean` 与 `R8/Squaring.lean`）。新增 `Doctrine/`、`Order/`、`Enriched/`、`Closure/`、`Wen/Embeddings/`、`Modern/QuantumRelativity*`、`R/` 多个子簇。
> **Last verified against code: 2026-05-21**
> 当前 proof 状态请参 [claim-status-ledger.md](claim-status-ledger.md) v0.8 (2026-05-21)。

模块地图把读者从主题带到 Lean 文件。完整列表由 `python3 scripts/docs_next.py build` 生成到 `docs-next/_generated/lean-index.md`；本页只描述模块簇的职责。

## 顶层入口

- [`formal/SSBX.lean`](../../formal/SSBX.lean) — 聚合入口
- [`formal/SSBX/Core.lean`](../../formal/SSBX/Core.lean) — 基础枚举、三值、开闭与若干共用结构
- [`formal/SSBX/Roster.lean`](../../formal/SSBX/Roster.lean) — 字根、生成项、primitive、recursive、pending 名册

被导入不等于 claim 已证明。

## 主要簇

| 簇 | 路径 | 职责 | 读法 |
|---|---|---|---|
| `Foundation/Core` | [`Foundation/Core/`](../../formal/SSBX/Foundation/Core/) | 单根、原子推导、价值、注意、人对齐、Renlei、生生不息、math axiom map | 看结构性 theorem 与 DAG 口径 |
| `Foundation/Atlas` | [`Foundation/Atlas/`](../../formal/SSBX/Foundation/Atlas/) | 顶层 atlas：`Yi/`、`R8/`、`Wen/`、`Role/`、`Judgment/`，加 Boolean / Fano / GF256 / Greimas / Hamming / Pauli 等代数表 | 看 ontology atlas 与字典 |
| **`Foundation/Atlas/Yi`** ⭐迁入 | [`Foundation/Atlas/Yi/`](../../formal/SSBX/Foundation/Atlas/Yi/) | 易核心 + 八卦代数：Bagua / BenZheng / Cell128 (R₇) / Cell256 (R₈) / Stratify / DaoSource / Shi / Hexagrams / Names / Operators / PhaseZero / Positions / Sheng / Tradition / WenSpec / YiCore / YiInstr / Diagonal；`Classical/{Algebra,Cells,Computation,Core,Diagonal}` 子目录承载 BaguaTuring / KleeneInternal / GodelLi / Newman / ChunkedDecide / CuoInvariance / FuelDiscipline | 看 8/64/128/256 cell 计算边界与 `kleene_recursion_axiom`；并入了旧 `Foundation/Bagua/` 与 `Foundation/Yi/` |
| `Foundation/Atlas/Wen` | [`Foundation/Atlas/Wen/`](../../formal/SSBX/Foundation/Atlas/Wen/) | atlas 层的文：NativeAliases / NativeLexicon / SurfaceDomainLaw / SurfaceLexicon / SurfaceSemantics | 看 atlas 给 Wen 提供的 lexicon 与 surface law |
| `Foundation/Atlas/R8` | [`Foundation/Atlas/R8/`](../../formal/SSBX/Foundation/Atlas/R8/) | Spacetime.lean — R₈ atlas 的时空切片 | 看 R₈ → spacetime 的连接 |
| `Foundation/Atlas/Role` / `Atlas/Judgment` | [`Atlas/Role/`](../../formal/SSBX/Foundation/Atlas/Role/) / [`Atlas/Judgment/`](../../formal/SSBX/Foundation/Atlas/Judgment/) | Role: Phantom / StateOp；Judgment: Attractor / Behavior / Information / R8 sub-cluster | 看角色记号与判定层 |
| `Foundation/Hierarchy` | [`Foundation/Hierarchy/`](../../formal/SSBX/Foundation/Hierarchy/) | R₀..R₈ index alias 文件 (R0_Taiji..R8_GuoHex) + RHierarchy umbrella + LiftProject + Operators/{Atomic, V4, V4Outer, Interlace, OXPrefix} + ZoneClassifier/{Axes, Classify, Examples, Interaction, Operators, Subsets, Types, WallCitations} + R432Conversion + RootLanguageTree | 一处 import 即得 R-index 命名 + 算子 inner/outer 拆分 + zone 分类 |
| `Foundation/Notation` | [`Foundation/Notation/`](../../formal/SSBX/Foundation/Notation/) | `OX["xxxxxxxx"]` 8-char Cell256 字面 macro | 给 256-cell 一个可读的字面 |
| **`Foundation/Doctrine`** ⭐新 | [`Foundation/Doctrine/`](../../formal/SSBX/Foundation/Doctrine/) | T_GUT / T_GUT_Enriched / FullGUT 主轴 + 多个 FullGUT*Frontier 切片 + EnrichedLawvereTheory / LawvereTheory + `Instance/` (Algebraic, Heyting, Topological, Witt, Quantum, EulerBridge, Hilbert, LSeries, Spectral, SemanticWitness, PrimaryComplete 等) | 看 GUT 主线与 model instance；categorical 公理与 native 桥分层 |
| **`Foundation/Order`** ⭐新 | [`Foundation/Order/`](../../formal/SSBX/Foundation/Order/) | FrameBimorphism / FrameCoproduct / FrmMonoidal / FrmBraided / FrmClosed / FrmClosedBraided / HeytingBimorphism / HeytingClassification / HeytingInternalHom / CubeFrameCoprod | 看 frame / Heyting 顺序结构与双线性桥 |
| **`Foundation/Enriched`** ⭐新 | [`Foundation/Enriched/`](../../formal/SSBX/Foundation/Enriched/) | Power / Cotensor / Weighted / Monad / Finitary / TypeOrdinary | 看 V-enriched (co)tensor、weighted limit、enriched monad 基础 |
| **`Foundation/Closure`** ⭐新 | [`Foundation/Closure/`](../../formal/SSBX/Foundation/Closure/) | PhiOperator.lean — closure / Φ 算子 | 看封闭算子层 |
| `Foundation/Squaring` ⚠️删除 | (已撤) | 旧 V4Tensor / L1 / RetractTower / StreamCarrier / ProfiniteLimit 已迁出；当前 squaring 见 [`Foundation/R/Squaring.lean`](../../formal/SSBX/Foundation/R/Squaring.lean) 与 [`Foundation/R8/Squaring.lean`](../../formal/SSBX/Foundation/R8/Squaring.lean)；profinite 极限改在 [`Foundation/RInfty/Profinite.lean`](../../formal/SSBX/Foundation/RInfty/Profinite.lean) | 旧引用请走当前 R / R8 / RInfty 路径 |
| **`Foundation/R`** ⭐新（顶层 R 簇） | [`Foundation/R/`](../../formal/SSBX/Foundation/R/) | R 家族 spine：OperationMonism / OperationMonismBridge / Hom / Judgment / JudgmentRequest / Tensor / DirectSum / DirectDecomp / Squaring / SubTower / Aut / Basic / BeyondR8 / RFamilyStructure / RPattern / RWord / Scope / StrategyA / Parametric / R4Minimality / D6_Tests / GUTAClosure / T5AClosure / UniquenessAlgebraic / UniquenessF2 / UniquenessGeneralField；子目录 `Algebra/`, `Awareness/`, `Bilinear/`, `ClaimZ/` (含 `Analytic/`), `Code/`, `Distinction/`, `PhaseZero/`, `UniquenessGeneral/` | 看 R 家族代数 spine、唯一性证明、Claim Z 证伪线、判断/算子单质 (operation monism) |
| `Foundation/R4` / `R8` / `RInfty` | [`R4/`](../../formal/SSBX/Foundation/R4/) / [`R8/`](../../formal/SSBX/Foundation/R8/) / [`RInfty/`](../../formal/SSBX/Foundation/RInfty/) | 单层结构：R4 (AutA8, Bilinear, EndR2, Enumeration, GL2Embedding, HomMat, RankStratification)；R8 (AutGL8, Bilinear, Ceiling, Dynamics, Enumeration, FiveIdentities, MatView, MathlibInstances, Squaring, Subgroups)；RInfty (Profinite) | 看 R₄/R₈/R∞ 的具体载体、自同构、squaring 与 profinite 极限 |
| `Foundation/Wen` | [`Foundation/Wen/`](../../formal/SSBX/Foundation/Wen/) | 文 / 文言微核 / 自释 / 自举 / quine 路线；含 Source / Kernel / WenEval / WenyanSyntax / WenyanParser / WenyanQuine* / REPL / Runner / RootRule* / ElabToRCode / R8ProjectionKernel / Binding / 等 | 看语法、求值、封装 witness 与路线层次 |
| `Foundation/Wen/Core` / `Analysis` / `Layered` / `MetaInterp` / `Native` / `Interpreter` / `Classical` / `RKernel` / `WenSurface` | (Wen 子目录) | Core (Instruction/Machine/State/Universal)、MetaInterp (Fetch/Dispatch/Execute Blocks)、Native (Backend/Eval/Surface/Quote)、Interpreter (Kernel + Adapters)、Layered (Runtime/Bridges)、WenSurface 等 | 各 substack 自带 README 风格的命名 |
| **`Foundation/Wen/Embeddings`** ⭐新 | [`Foundation/Wen/Embeddings/`](../../formal/SSBX/Foundation/Wen/Embeddings/) | HeisenbergWeylZModP / HeisenbergWeylOperators / StabilizerQM / HilbertPauliFunctor / PauliRingIso / PhasedPauli / FOL | 看 Wen 在 Heisenberg-Weyl / Pauli / stabilizer QM / FOL 上的嵌入 |
| `Foundation/Jian` | [`Foundation/Jian/`](../../formal/SSBX/Foundation/Jian/) | 间、本体、模式核、STLC、易桥、Minimality | 看「关系间隔」如何进入形式对象 |
| `Foundation/Lang` | [`Foundation/Lang/`](../../formal/SSBX/Foundation/Lang/) | Confucian / Core / DaoJudge / L1..L7 layer (Yao..Cell128) / Lexicon / Names / Pattern / Rule / Sexp / Wuchang / Partial/ 等 | 看 lang 层 layer 命名 + 句法 |
| `Foundation/Eight` | [`Foundation/Eight/`](../../formal/SSBX/Foundation/Eight/) | 八衍：DongLi / LeiYing / LuoJi / ShuSuan / TongJi / WuXiang / XinZhi / XingWei | 看专题中层接口，不读作经验充分性 |
| **`Foundation/Modern`** (扩展) | [`Foundation/Modern/`](../../formal/SSBX/Foundation/Modern/) | 现代数学 / 概率 / 逻辑 / 物理 / 神经科学：Kolmogorov / Lebesgue / BochnerPL / PicardLindelofGen / ODESmoothness / IIDWlln / Quantum / SUN / NaturalDeduction / Neuro / DaoLi / HistoryTapeStructure / WuJianShiTrinity / OperatorCellGridMarkovBridge；以及 12+ 边界 (Ce/Fou/Gan/Ke/Knowable/Liang/Ming/Tui/Unity/Xing/Yoneda/Zheng/Zhi…) | 看形式桥接与局部定理 |
| **`Foundation/Modern/QuantumRelativity*`** ⭐新 | (同上) | 25+ QuantumRelativity*Bridge 文件：ActionAmplitudeMeasurement / ActionPhase / AmplitudeChannel / Born* / CanonicalRep / ChannelCompose / Concrete / ContinuousActionFunctional / Discrete* / EndpointIndexed* / FiniteAction* / FiniteCausal* / FiniteKernel / FiniteKeyQuotient / FinitePathSum* / FinitePhaseEvolution / NormalizedMass / PathWeightMultiplication / FiniteProbabilityNormalization / BornWeightNormalization / SumOverMiddleChannel / BornMeasurement / etc. | 看 quantum-relativity 大套桥；多文件以同名 `.lean` + 同名目录形式存在 (主文件 + 辅助) |
| `Foundation/CategoryTheory` | [`Foundation/CategoryTheory/`](../../formal/SSBX/Foundation/CategoryTheory/) | ElementaryTopos | 看 topos / categorical 元结构 |
| `Foundation/Representation` | [`Foundation/Representation/`](../../formal/SSBX/Foundation/Representation/) | Articulate / Concept / Lexicon / OXPattern / Signature；子目录 `Lexicon/` | 看 representation / articulation 模型 |
| `Text` | [`Text/`](../../formal/SSBX/Text/) | glyph、义位、算子、覆盖性；含 OperatorAnchors / OperatorCellMap / LayerCharacterMap / OperatorReadings / OperatorSignatures / SenseSyntax / WenyanOperators | 看文字账本与算子表完备性 |
| `Truth` | [`Truth/`](../../formal/SSBX/Truth/) | claim ledger、语义、体系内真理、**SelfDescription**、Adequacy、Absolute | 看 claim status；`Cell256OperatorComplete` theorem |
| `Model` | [`Model/`](../../formal/SSBX/Model/) | Adequacy / ConcreteLedger | 看模型充分性如何被表述 |
| `Pending` | [`Pending/`](../../formal/SSBX/Pending/) | Examples / Interfaces — 经验接口与示例 | 看未闭合边界 |

## v4 主要变更总结 (2026-05-21)

**目录撤销 / 合并**：
- ~~`Foundation/Bagua/`~~ → 全部并入 `Foundation/Atlas/Yi/`（Bagua.lean、BenZheng.lean、Cell128.lean、Cell256.lean 现皆在 `Atlas/Yi/` 根；Bagua 子模块如 BaguaTuring/KleeneInternal/GodelLi/Newman/Cuo/ChunkedDecide/FuelDiscipline 入 `Atlas/Yi/Classical/{Computation,Diagonal,Algebra}/`）
- ~~`Foundation/Yi/`~~ → 同样并入 `Foundation/Atlas/Yi/`
- ~~`Foundation/Squaring/`~~ → 撤为零文件目录；squaring 内容下沉到 `Foundation/R/Squaring.lean`、`Foundation/R8/Squaring.lean`、`Foundation/RInfty/Profinite.lean`

**新增顶层目录**（自 v3 以来）：
- `Foundation/Doctrine/` — GUT 主轴与 model instance
- `Foundation/Order/` — frame / Heyting 顺序结构
- `Foundation/Enriched/` — V-enriched 范畴层
- `Foundation/Closure/` — Φ closure 算子
- `Foundation/R/` — R 家族 spine（OperationMonism, ClaimZ, Distinction, UniquenessGeneral 等子目录）
- `Foundation/R4/`, `Foundation/R8/`, `Foundation/RInfty/` — 各 R 层独立载体目录
- `Foundation/Wen/Embeddings/` — Pauli / Heisenberg-Weyl / StabilizerQM / FOL 嵌入
- `Foundation/Modern/QuantumRelativity*` — 25+ 量子-相对论桥

**Atlas/Yi/Classical/ 内部组织**：

```
Atlas/Yi/Classical/
├── Algebra/      (BaguaAlgebra, BenZheng, CuoInvariance, Newman)
├── Cells/        (R7, R8, R8Stratify)
├── Computation/  (BaguaTuring, BaguaWenSpec, ChunkedDecide, FuelDiscipline)
├── Core/         (Yi, YiCore)
└── Diagonal/     (GodelLi, KleeneInternal)
```

## 一处入口：RHierarchy umbrella

```lean
import SSBX.Foundation.Hierarchy.RHierarchy
-- 现在 R0..R8、liftR{n}toR{n+1}/projR{n+1}toR{n}、
-- 8 atomic XOR ops + V₄ outer 都在 namespace 内可用
```

## 索引优先

人工模块图会过期。核对时优先使用：

- `docs-next/_generated/lean-index.md`：模块、导入、声明、行数
- `docs-next/_generated/crossrefs.md`：文档与 Lean 路径/符号互证
- `docs-next/_generated/registry-index.md`：名册 kind 与 pending/recursive 项
- `docs-next/_generated/claim-index.md`：claim 状态
- [`claim-status-ledger.md`](claim-status-ledger.md) v0.8 (2026-05-21)：人工 claim status

## 阅读原则

先从模块簇判断「这页在证明什么」，再看 theorem 名称和依赖。不要只凭文件名推断强度：

- Truth / Doctrine 相关文件可记录 ledgerDependent claim
- Atlas/Yi 不完备路线（BaguaTuring / KleeneInternal） 仍依赖唯一 axiom（`kleene_recursion_axiom`，4 件具名原子）
- Pending 文件明确是接口边界
- Hierarchy / Notation 是 navigation / surface 层（无独立证明）
- Modern/QuantumRelativity*Bridge 多数是 categorical 桥，不直接传输 analytic 强度（参 [project_e1_rtower_rh_closed.md] doctrine 笔记）

## 形式锚

- [`formal/SSBX.lean`](../../formal/SSBX.lean)
- [`formal/SSBX/Foundation/Hierarchy/RHierarchy.lean`](../../formal/SSBX/Foundation/Hierarchy/RHierarchy.lean)
- [`formal/SSBX/Foundation/Hierarchy/LiftProject.lean`](../../formal/SSBX/Foundation/Hierarchy/LiftProject.lean)
- [`formal/SSBX/Foundation/Hierarchy/Operators/Atomic.lean`](../../formal/SSBX/Foundation/Hierarchy/Operators/Atomic.lean)
- [`formal/SSBX/Foundation/Hierarchy/Operators/V4Outer.lean`](../../formal/SSBX/Foundation/Hierarchy/Operators/V4Outer.lean)
- [`formal/SSBX/Foundation/Notation/OXNotation.lean`](../../formal/SSBX/Foundation/Notation/OXNotation.lean)
- [`formal/SSBX/Foundation/Atlas/Yi/Cell128.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Cell128.lean)
- [`formal/SSBX/Foundation/Atlas/Yi/Cell256.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Cell256.lean)
- [`formal/SSBX/Foundation/Atlas/Yi/Stratify.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Stratify.lean)
- [`formal/SSBX/Foundation/Atlas/Yi/Bagua.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Bagua.lean)
- [`formal/SSBX/Foundation/Atlas/Yi/BenZheng.lean`](../../formal/SSBX/Foundation/Atlas/Yi/BenZheng.lean)
- [`formal/SSBX/Foundation/Doctrine/T_GUT.lean`](../../formal/SSBX/Foundation/Doctrine/T_GUT.lean)
- [`formal/SSBX/Foundation/Doctrine/T_GUT_Enriched.lean`](../../formal/SSBX/Foundation/Doctrine/T_GUT_Enriched.lean)
- [`formal/SSBX/Foundation/Doctrine/FullGUT.lean`](../../formal/SSBX/Foundation/Doctrine/FullGUT.lean)
- [`formal/SSBX/Foundation/Doctrine/EnrichedLawvereTheory.lean`](../../formal/SSBX/Foundation/Doctrine/EnrichedLawvereTheory.lean)
- [`formal/SSBX/Foundation/Enriched/Power.lean`](../../formal/SSBX/Foundation/Enriched/Power.lean)
- [`formal/SSBX/Foundation/Enriched/Cotensor.lean`](../../formal/SSBX/Foundation/Enriched/Cotensor.lean)
- [`formal/SSBX/Foundation/Order/FrameBimorphism.lean`](../../formal/SSBX/Foundation/Order/FrameBimorphism.lean)
- [`formal/SSBX/Foundation/Order/FrmMonoidal.lean`](../../formal/SSBX/Foundation/Order/FrmMonoidal.lean)
- [`formal/SSBX/Foundation/Closure/PhiOperator.lean`](../../formal/SSBX/Foundation/Closure/PhiOperator.lean)
- [`formal/SSBX/Foundation/R/OperationMonism.lean`](../../formal/SSBX/Foundation/R/OperationMonism.lean)
- [`formal/SSBX/Foundation/R/OperationMonismBridge.lean`](../../formal/SSBX/Foundation/R/OperationMonismBridge.lean)
- [`formal/SSBX/Foundation/R/Squaring.lean`](../../formal/SSBX/Foundation/R/Squaring.lean)
- [`formal/SSBX/Foundation/R8/Squaring.lean`](../../formal/SSBX/Foundation/R8/Squaring.lean)
- [`formal/SSBX/Foundation/RInfty/Profinite.lean`](../../formal/SSBX/Foundation/RInfty/Profinite.lean)
- [`formal/SSBX/Foundation/Wen/Embeddings/HilbertPauliFunctor.lean`](../../formal/SSBX/Foundation/Wen/Embeddings/HilbertPauliFunctor.lean)
- [`formal/SSBX/Foundation/Wen/Embeddings/StabilizerQM.lean`](../../formal/SSBX/Foundation/Wen/Embeddings/StabilizerQM.lean)
