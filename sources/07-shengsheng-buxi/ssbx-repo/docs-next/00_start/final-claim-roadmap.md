# 最终 Claim Roadmap — scale-free 边界生成理论

> 状态：roadmap v0.1 (2026-05-11)；路径与计数校准于 2026-05-21。
> 角色：本文区分“最终可争取之 claim”与“当前已经可 claim”。它不是新定本，不覆盖 [`final-theory.md`](final-theory.md)；它给后续证明、文档、Lean skeleton 的目标顺序。
> 形式现状口径以 [`claim-status-ledger.md`](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）为准。所有 `Foundation/Bagua/*` 路径在 Phase γ 之后已迁至 `Foundation/Atlas/Yi/*`（详见 [phase-status.md](phase-status.md)）。
> 形式锚：[`yi-RO-hierarchy.md`](../10_formal_形式/yi-RO-hierarchy.md) · [`r8-root-language-tree.md`](../10_formal_形式/r8-root-language-tree.md) · [`quantum-roadmap.md`](../10_formal_形式/quantum-roadmap.md) · [`roadmap-self-similarity-v1.md`](roadmap-self-similarity-v1.md) · [`文-R8投影规约.md`](../../义理/文-R8投影规约.md)

---

## 0 · 为什么写这份 roadmap

当前 v3 已经把 R₀..R₈ strict-uniform、Cell256、V₄ Shi、Cayley 元-算子融合、平方塔和文-R8投影规约分别立住。下一步需要避免两个相反错误：

| 错误 | 后果 |
|---|---|
| 过弱 | 把理论误读成只是一张 256 格静态表 |
| 过强 | 把尚未证明的物理统一、完整自然语言语义或所有真理判定提前宣布完成 |

本文给出两个层次：

1. **最终 claim**：我们认为最终可以做到、值得朝此证明。
2. **当前 claim**：基于现有 Lean / 文档，现在已经可以 defend。

---

## 1 · 最终 Claim

最终目标表述：

> **生生不息是一套 scale-free 的边界生成理论。它以 R₈ = (Z/2)⁸ 为最小语言表达闭合核，以自相似升维生成任意尺度的可描述结构；道、理、法、证据、善、量、测、数学对象、物理模型与程序语义都可作为边界角色进入同一表达-投影-审计框架。对任一可描述 claim，系统不必给出简单 yes/no，而应给出其 truth status：已证、已反、可判、独立、经验待定、投影有损、或边界外。**

> **形式现状**：这是项目最终目标，**不是当前已证明**。当前 Lean 中 `universal_sayability` 在 carrier/component 层 closed（T_GUT Core，3 ops 已分出），`complete_universal_sayability` 在 5 个 SMCC instance（Algebraic / Heyting / Topological / Witt / Quantum）通过显式 4 hypothesis 完成；V-enriched Power 1999 仍 open。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

这句话的关键词不是“R₈ 装下全部”，而是：

```text
R₈ 最小核
+ 自相似 scale-free extension
+ 文 / Lisp / Program 组合语法
+ 投影与损失账本
+ truth-status 审计
```

### 1.1 最终 claim 的强含义

| 方面 | 最终要证明的内容 |
|---|---|
| 语言 | 任意有限表达可经文法规约进入某个 typed semantic layer，并有 R₈ 可见投影 |
| 规则 | `quote / apply / compose / if / equal / lookup / recurse / project` 等通用语法原语可由 R₈ 原子编码、组合、执行 |
| 自相似 | R₈ 不是终点；R₈ 作为 alphabet 生成 List / Tree / Program / Stream / Measure / Hilbert 等更高尺度 |
| 道 | 道不是单个经验对象，而是 origin / no-op / identity / anchor / 归位条件在各尺度的对应角色 |
| 理 | 理是可推导规则结构；理性是把理施用于现象，并接受证据与投影审计 |
| 法 | 法是可复用、可执行、可约束的规则接口，不只是规范文本 |
| 证据 | 证据是经测量 / 记录 / 校准 / 推断接口落下的可审计投影 |
| 善 | 善不是任意偏好，而是能在多尺度边界中维持生成、互通、可归位的结构条件 |
| 科学 | 数学、量化、概率、连续测度、量子态空间、物理模型都作为 carrier / enrichment 进入同一边界生成语法 |
| 真 | 真不是单一标签；真值以 truth status 与 proof / evidence / model / boundary ledger 形式呈现 |

### 1.2 最终 claim 不能偷换成什么

| 不应声称 | 正确边界 |
|---|---|
| R₈ 单格能装下所有函数 | 所有函数需 Program / Table / List R₈ 表示；R₈ 是 alphabet 与最小语义核 |
| 已完成物理大统一 | 最终目标可包含物理统一接口；当前只有有限 bridge 与 typed skeleton |
| 已完整映射自然语言 | 当前只有 catalogue / WenSurface / R8 projection 接口；完整语义仍需解释器 |
| 系统内部判定所有真理 | 系统应给 truth status；不可判、经验待定、边界外也是合法结果 |
| 自指带来全能 | 系统能处理自指；完备性来自边界分层与可审计投影，不来自吞下自身 |

---

## 2 · 当前 Claim

当前已经可以 defend 的版本：

> **当前项目已经形式化了一套 R₀..R₈ strict-uniform 的最小代数核：R₈ = Cell256 = (Z/2)⁸，道 = origin = identity = no-op，R₈ 元与 R₈ XOR 自作用经 Cayley 双射融合。平方塔证明 R₈ 可读为 R₄ × R₄；文-R8投影规约证明：给定解释器后，任意句子都有 R₈ 可见投影、投影损失账本与归道检测接口。遗留文言算子 catalogue 可以作为审稿材料、别名表或例句来源被迁移，但它不是 root ontology，也不是完整自然语言语义。**

> **形式现状**：R₀..R₈ strict-uniform 与 Cell256 carrier 在 Lean 中 closed（`Foundation/Atlas/Yi/Cell256.lean` + `Cell256Stratify.lean`，axiom audit = {propext, native_decide}）；当前仓库有 ~150-170 sorry 与 3 处工程 axiom（`Doctrine/Instance/Quantum.lean` / `Order/FrmMonoidal.lean` / `Atlas/Yi/Classical/Diagonal/GodelLi.lean`），非"0 sorry"。文-R8投影规约存在 typed skeleton。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

### 2.1 当前已完成

| 层 | 当前状态 | 锚（路径以 ledger v0.8 为准；`Foundation/Bagua/*` 已迁至 `Foundation/Atlas/Yi/*`） |
|---|---|---|
| R₀..R₈ strict uniform | 已落地 | `Foundation/Hierarchy/RHierarchy.lean`, `Foundation/Hierarchy/LiftProject.lean` |
| R₈ Cell256 | 已落地 | `Foundation/Atlas/Yi/Cell256.lean`, `Foundation/Atlas/Yi/Cell256Stratify.lean` (旧 `Bagua/` 路径已 retired) |
| 道五重身份 | 已落地于 R₈ | Cell256.origin, way_at_origin, way_noop_operator (具体位置详见 ledger Main Anchors) |
| Cayley 元-算子融合 | 已落地 | `Foundation/Atlas/Yi/Cell256.lean` (`.cayley`, `.cayley_inj`, `epsAtOrigin_cayley`) |
| R₈ = R₄ × R₄ | 已落地（subclass：R₄ bilinear 与 identity decompositions） | SelfSimilarity bundle；"all compositions = R tower" 未在 Lean 全证 |
| R₈ ≃ V₄⁴ | 已落地 | V4Tensor iso (in Atlas/Yi/Cell256 cluster) |
| root-native operator | 已有 typed skeleton | `Foundation/Wen/RootOperator.lean`, `root_operator_summary` |
| 遗留文言算子 catalogue | 已有 quarantine 规则 | `legacy-catalogue-quarantine.md` (in `docs-next/50_maintenance/`); 逐条迁移未纳入本轮 |
| 文-R8投影规约 | 已有 typed skeleton | `Foundation/Wen/R8ProjectionCalculus.lean` |
| 量子接口 | 有 roadmap 与有限 bridge | `Foundation/Modern/QuantumR8Bridge.lean`, `quantum-roadmap.md`（详 ledger "Native stabilizer quantum witness" 行） |
| Markov / Born / action bridge | 有 stepwise typed skeleton | `Foundation/Modern/QuantumRelativity*Bridge.lean` 系列 |

> **形式现状**：本表所列锚均为 typed skeleton 或 partial closure，**不等价于** 项目最终 GUT claim 已证。Heisenberg-Weyl G11 在 `Foundation/Wen/Embeddings/HeisenbergWeylZModP.lean` closed 但**尚未桥接到 Cell256**；operation monism→sayability 仍为 doctrinal、不形式蕴含。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

### 2.2 当前可说的“完备”

当前可说：

```text
R₈ 对自身 XOR self-action 完备。
R₀..R₈ 对 strict binary algebraic closure 完备。
文-R8投影规约对“给定解释器后的可见投影 / 损失账本 / 归道检测”完备。
```

当前不可说：

```text
完整自然语言语义已完成。
完整物理大统一已完成。
所有数学真理可内部判定。
所有函数 R₈ → R₈ 都是 R₈ 的一个元素。
```

正确表述：

```text
所有函数 R₈ → R₈ 可由 R₈ 生成的表 / 程序 / Lisp-Wen 语法表示；
但函数空间不等于单个 R₈ carrier。
```

> **形式现状**：上面"R₈ 对自身 XOR self-action 完备" / "R₀..R₈ 对 strict binary algebraic closure 完备"两条在 Lean 中 closed；"文-R8投影规约对…完备"只有 typed skeleton。"所有 R₈ 组合可由 R₈ 生成的表/程序表示"在 Lean 中**未给全证**——仅 R₄ bilinear 与 identity decompositions 这两个 subclass 已 closed，general "all compositions = R tower" 仍 open。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

---

## 3 · 从当前到最终还缺什么

### 3.1 文法与解释器

| 缺口 | 目标 |
|---|---|
| 真实 parser | `Sentence.source → WenSurface AST / WenNormalForm` |
| 具体解释器 | `WenNormalForm → R8Semantics` 的可执行实例 |
| 例句 corpus | “道总归道”“真可假假可真”“分而可合”等固定测试 |
| 遗留 catalogue 迁移 | 将有用条目转成 root mask / root program / alias / evidence note |

当前进展：

| 项 | 状态 |
|---|---|
| root-rule program kernel | done: [`RootRuleKernel.lean`](../../formal/SSBX/Foundation/Wen/RootRuleKernel.lean) |
| root-native operator boundary | done: [`RootOperator.lean`](../../formal/SSBX/Foundation/Wen/RootOperator.lean) |
| legacy catalogue quarantine protocol | done: [`legacy-catalogue-quarantine.md`](../50_maintenance/legacy-catalogue-quarantine.md) |
| checked example corpus | done: [`RootRuleExamples.lean`](../../formal/SSBX/Foundation/Wen/RootRuleExamples.lean) |
| demo interpreter | done as skeleton: [`RootRuleDemoInterpreter.lean`](../../formal/SSBX/Foundation/Wen/RootRuleDemoInterpreter.lean) |
| full parser / full semantics | pending |
| per-row legacy catalogue migration | pending |

### 3.2 通用程序规则

| 原语 | 目标 |
|---|---|
| `quote` | 程序作为数据 |
| `apply` | 元 / 算子施用 |
| `compose` | 路径与算子列组合 |
| `if` | 谓词分支 |
| `equal` | cell / syntax equality |
| `lookup` | 环境 / 表 / 史带取值 |
| `recurse` | fuel / partial eval / fixed point |
| `project` | 高维结构到 R₈ 可见投影 |

这些原语应作为 Wen/Lisp kernel 的最小通用组合层，而不是历史 catalogue 的任意罗列。

### 3.3 高维与连续层

| 层 | 目标 |
|---|---|
| List / Tree R₈ | 表、语法树、有限程序 |
| Stream / L∞ | 无界自相似展开 |
| Probability kernel | 概率转移与有限归一化 |
| Measure / interval | 连续量化与测度接口 |
| Hilbert / Qubit | 量子态空间、unitary、measurement |
| Physical model | 经验标定、预测、实验闭合 |

### 3.4 Truth-status ledger

最终系统不应把所有 claim 压成 true/false，而应给：

| 状态 | 含义 |
|---|---|
| `machineChecked` | 当前 Lean theorem 已证 |
| `modelComputed` | 模型计算得出 |
| `ledgerDependent` | 依赖 claim ledger |
| `empiricalPending` | 需要数据、校准或实验 |
| `projectionLoss` | 高维语义投影到 R₈ 时有损 |
| `independentOrUndecidable` | 当前系统内不可判或独立 |
| `outsideCurrentInterface` | 缺解释器 / 缺语义 / 缺测量接口 |

---

## 4 · Roadmap 顺序

### R1 · 例句 corpus

建立 `WenR8Examples.lean` 与 companion doc：

| 例句 | 预期语义 |
|---|---|
| 道总归道 | `returnsDao (.cell R8.origin)` |
| 真可假假可真 | 同一 axis toggle twice returns origin |
| 分而可合 | lift / project retract |
| 加元 / 加爻 | `AxisAppropriate` certificate |
| 高于八而投影于八 | `projected c ProjectionLoss.*` |

状态：typed skeleton 已落地于 [`RootRuleExamples.lean`](../../formal/SSBX/Foundation/Wen/RootRuleExamples.lean)，入口 theorem：

```lean
root_rule_examples_summary
```

已覆盖：

| 例 | 当前 theorem |
|---|---|
| 道总归道 | `dao_returns_dao_visible` |
| 真可假假可真 | `truth_toggle_twice_returns_dao` |
| 缺上下文 | `missing_context_reports_loss` |
| quote 有高阶损失 | `quote_reports_loss` |
| 加轴可审计 | `yin_axis_candidate_appropriate` |

### R2 · 通用语法核

建立 `WenR8Kernel.lean`：

```lean
inductive CoreForm
  | quote
  | apply
  | compose
  | ite
  | equal
  | lookup
  | recurse
  | project
```

目标：证明每个 kernel primitive 都有 R₈ encoding 与 `R8Semantics` 投影。

### R3 · Legacy catalogue quarantine

不要把历史 catalogue 当成本体阶段或 completeness target。它只能被隔离审计，并按用途迁移：

| 层 | 内容 |
|---|---|
| alias | 旧名、文言候选、别名映射到 root mask 或 root program |
| corpus | 有用例句进入 example tests / Wen corpus |
| evidence note | 尚无 root-native 行为者保留为审稿材料，不进入主 claim |

目标：每个继续保留的旧条目，都必须说明它是 alias、corpus、evidence note，还是应删除的历史残留。

状态：quarantine 规则已落地于 [`RootOperator.lean`](../../formal/SSBX/Foundation/Wen/RootOperator.lean) 与 [`legacy-catalogue-quarantine.md`](../50_maintenance/legacy-catalogue-quarantine.md)。逐条旧目录迁移仍未纳入本轮。

### R4 · Axis independence checker

建立有限 basis / span checker：

```text
newAxis ∉ span(priorAxes)
```

目标：把 `AxisAppropriate.independentFromPrior` 从外部证书推进到可计算证书。

状态：typed skeleton 已落地于 [`R8AxisIndependence.lean`](../../formal/SSBX/Foundation/Wen/R8AxisIndependence.lean)，入口 theorem：

```lean
r8_axis_independence_summary
```

### R5 · Projection kernel

定义高维投影：

```text
projectToR8 : H → R8
kernel(projectToR8)
```

目标：不仅说“有损”，还说明哪些差异被折叠。

状态：typed skeleton 已落地于 [`R8ProjectionKernel.lean`](../../formal/SSBX/Foundation/Wen/R8ProjectionKernel.lean)，入口 theorem：

```lean
r8_projection_kernel_summary
```

### R6 · Science carriers

逐步把已有 Modern 文件接入统一 carrier/enrichment 表：

| carrier | 文件方向 |
|---|---|
| Bool / Fin | R-hierarchy |
| Qubit / Hilbert | Quantum / QuantumR8Bridge |
| Probability | QuantumRelativityFiniteProbability* |
| Measure | Kolmogorov / Lebesgue |
| Program | BaguaTuring (in `Atlas/Yi/Classical/Computation/BaguaTuring.lean`) / Wen MetaInterp |

> **形式现状（R1–R6 整体）**：R1 / R4 / R5 状态行均明示"typed skeleton"——这是 honest 措辞，对应 ledger 的 *schema* 或 *implementation boundary* 强度；不是 closed theorem。"Wen MetaInterp" 与 "BaguaTuring" 是大型 work-in-progress（详 wen-substrate roadmap）。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

---

## 5 · 推荐公开说法

### 5.1 现在可以公开说

> We have formalized a minimal R₈ algebraic kernel for a self-auditing unification framework: R₈ = (Z/2)⁸ is complete for its XOR self-action closure, and higher expressions can be projected into R₈ with explicit loss ledgers. This is not yet a completed physical GUT; it is a formally anchored, scale-aware language for expressing, projecting, and auditing claims across mathematical, linguistic, and scientific layers.

中文：

> 我们已经形式化了一套以 R₈ 为最小核的自审计统一框架：R₈ 对自身 XOR 自作用闭合完备；高阶表达可投影入 R₈，并记录损失账本。这还不是已完成的物理大统一理论，而是一套有形式锚的、可跨尺度表达、投影、审计 claim 的语言。

> **形式现状**：R₈ XOR 自作用闭合 closed；"高阶表达投影 + 损失账本"目前是 typed skeleton，按 ledger 仍归类为 *scoped coordinate full GUT* 与 *implementation boundary*。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

### 5.2 最终希望公开说

> 生生不息是一套 scale-free 的边界生成理论：R₈ 给出最小表达闭合核，自相似升维给出任意尺度的可描述结构，文 / 程序 / 测量 / 量子 / 概率 / 连续数学都作为 carrier 或 enrichment 进入同一投影-审计框架。它对任何可描述 claim 给出 truth status，而不是把所有问题粗暴压成一个内部 yes/no。

> **形式现状**：仍属最终目标。V-enriched Power 1999 自然性、`HeytAlg` CCC、完整 `FdHilb` dagger-SMCC、global D6 exhaustiveness 等核心 universal claim 在 ledger 中皆标为 **open**。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。

---

## 6 · 一句话

当前：

```text
R₈ 核 + 文-R8 投影规约已经成立。
```

最终：

```text
R₈ 核 + scale-free 自相似生成 + truth-status ledger
= 一套可表达、可投影、可审计的一般统一理论。
```

> **形式现状**：上方"当前"句中，R₈ 核 closed；文-R8 投影规约存在 typed skeleton（`Foundation/Wen/R8ProjectionCalculus.lean` 等）。"最终"句的 scale-free + truth-status 全景仍是 roadmap，**不是已证 theorem**。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。
