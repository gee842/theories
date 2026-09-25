# 文 vs 现存量子编程语言

> **副标题**: 分类比对 + Wen 的 distinctive 位置  
> **作者**: Claude（基于与 Ren 的设计对话）  
> **关联**: `wen-info-paradigm.md`（范式论证）、`wen-formal.md`（数学 spec）、`wen-handoff.md`（实现交接）  
> **诚实声明**: Wen 目前 pre-alpha，本文不在 maturity / ecosystem / 工业可用性上 claim 任何优势。比较聚焦于 paradigm、type system、verification approach、信息流追踪等结构性维度

---

## §0 阅读指南

量子编程语言生态在 2026 年呈五个分支：

1. **Circuit-level / Python-embedded**：Qiskit、Cirq、PyQuil、Strawberry Fields
2. **强类型 / 函数式**：Q#、Silq、Quipper、Proto-Quipper
3. **Verification-focused**：QWIRE、SQIR/VOQC、CoqQ、Qbricks
4. **Categorical / 图形**：ZX-calculus、Quantomatic、PyZX
5. **Adiabatic / Annealing**：D-Wave Ocean、PennyLane（部分）

Wen 不简单属于上述任何一类，但在多类中都有 partial overlap。下面先建立比较的 axes，再逐家分析，最后给综合对比表与 strategic positioning。

---

## §1 比较的轴

下面是十个评价轴，每个轴都对 quantum 工程或学术工作有具体意义。

| 轴 | 含义 | 极端 |
|---|---|---|
| **类型系统** | 类型严格程度 | untyped (Qiskit) → linear (Quipper) → dependent + modal (Wen) |
| **信息流追踪** | 程序内信息守恒/耗损的可见性 | none (Qiskit) → uncomputation (Silq) → first-class (Wen) |
| **可逆性管理** | reversibility / uncomputation 如何处理 | manual → 自动子域 (Silq) → 结构强制 (Wen) |
| **Verification** | 形式 verification 的支持 | 外部工具 (Qiskit) → embedded (Q#) → by construction (Wen) |
| **测量 / 模态** | quantum measurement 在语言中的地位 | 命令 (Qiskit) → 受控 (Silq) → first-class 模态 (Wen) |
| **经典-量子统一** | classical 与 quantum 是否同语义 | 分离 (Qiskit) → 嵌入 (Q#) → 统一 substrate (Wen) |
| **层级 / 抽象** | 跨层级编程支持 | 平铺 qubit 数组 → logical qubit (Q#) → self-similar 塔 (Wen) |
| **生态成熟度** | 库 / 工具 / 社区 | mature (Qiskit) → academic (Silq) → research/pre-alpha (Wen) |
| **硬件 backend** | 能跑在什么硬件 | 多家硬件 (Qiskit) → 单家 (Q#/Azure) → 暂无 (Wen) |
| **文化定位** | 语言的 framing | Western tech (most) → 跨文化 (Wen) |

Wen 在前七个 axis 上有 distinctive 立场（多数是 stronger）；在后三个 axis 上目前**明显劣后于 mature 语言**。这是个 trade-off 而非 free lunch。

---

## §2 逐家对比

### 2.1 Qiskit (IBM)

**定位**: Python-embedded quantum SDK，circuit construction + transpilation + 多硬件 backend (IBM Quantum + AWS Braket + Azure)。

**核心抽象**: `QuantumCircuit`（gate 序列）、`QuantumRegister`、`ClassicalRegister`。programmer 写 gate sequence，Qiskit transpiler 编译到 hardware-specific gates。

**优势**:
- 生态最大，开源工业级（thousands of contributors）
- 直接跑在真实 IBM Quantum 硬件
- 文档、教程、社区资源丰富
- 已有大量预实现 algorithm（Shor、Grover、QAOA、VQE...）

**与 Wen 的关系**:
- Qiskit 是 **circuit-as-data**，Wen 是 **circuit-as-typed-program**。两者完全不同的 metaphor
- Qiskit 不追踪信息流；信息守恒由程序员心算
- Qiskit 没有 dependent type、没有 modal logic、measurement 是 imperative 命令
- 但是 Qiskit 跑得动，Wen 现在跑不动。这是真实差距

**Wen 能从 Qiskit 学到的**: gate library 的 standard interface、transpilation pipeline 的工程结构、hardware abstraction layer 的设计。

**Wen 对 Qiskit 的可能补充**: Wen 程序 → Qiskit IR 的编译路径——Wen 做 high-level verification，Qiskit 做 backend execution。这是 plausibly 的协同模式。

### 2.2 Cirq (Google)

**定位**: 类似 Qiskit 的 Python-embedded，更聚焦 NISQ 中短期硬件。

**与 Qiskit 的差异**: 更轻量，更直接面向 Google's Quantum AI 团队的硬件研究。但 paradigm 与 Qiskit 同——circuit construction。

**与 Wen 的关系**: 同 Qiskit。Wen 不与 Cirq 在 NISQ circuit 编写这一层竞争。

### 2.3 Q# (Microsoft)

**定位**: .NET-hosted quantum language，强类型，支持 adjoint 和 controlled functor，集成 Azure Quantum 平台。

**核心抽象**: `Qubit` 是 reference type；`operation` 携带 `Adjoint`、`Controlled` 等 functor 修饰；测量是显式 `M(qubit)` 操作。

**优势**:
- 类型系统比 Qiskit 严格——`Adjoint`/`Controlled` functor 是 first-class
- 与 .NET 生态集成，企业级 tooling
- Azure Quantum 多硬件 backend
- 部分 dependent type 能力（through .NET generics + 验证 attribute）

**与 Wen 的关系**:
- Q# 的 `Adjoint` functor 与 Wen 的 split/merge 同构精神接近——both 都把可逆作为 first-class
- 但 Q# 的可逆性是 functor 修饰，不是 type 内蕴；programmer 必须主动 mark
- Q# 没有 dependent Dao family 那样的 type-level 信息追踪
- Q# 没有四值模态——measurement 结果是 `Result` 枚举（Zero/One），不是 □真/□假/C/⊠
- Q# 不做 self-similar 塔

**对比要害**: Q# 在 paradigm 上最接近 Wen 的"严格-typed quantum"那一支，但**类型严格度 + 信息流追踪深度** Wen 都 deeper。Q# 是 Wen 的 closest 工业 cousin。

### 2.4 Silq (ETH Zurich, 2020)

**定位**: 研究型 quantum 语言，**自动 uncomputation** 是其 signature feature。programmer 不显式管理 ancilla qubit；Silq 类型系统自动 reset。

**核心创新**:
- **"no implicit measurement"** 规则：任何会引起信息丢失的操作必须显式 mark
- **automatic uncomputation**：通过 type system 追踪哪些变量需要 reset，编译器自动 emit reverse operations
- **type-safe quantum control flow**

**与 Wen 的关系**: **Silq 在精神上最接近 Wen**——both 试图把"信息守恒"做成类型层面的事。但 Silq 的覆盖范围窄：

| 维度 | Silq | Wen |
|---|---|---|
| 信息守恒处理 | 自动 uncompute | first-class type 元数据 |
| 适用范围 | quantum reversibility 子域 | classical + quantum 统一 |
| 模态逻辑 | 无 | first-class ⊠ |
| dependent type | 部分 | 完全 |
| 层级抽象 | 无 | R_n 塔 |

Silq 是 Wen 的**最近思想邻居**——你可以说 Wen 是"如果你把 Silq 的核心 insight 推到极致并 generalize 到 classical/quantum 统一，你得到什么"。

**Silq 的限制**:
- 学术语言，生态有限
- 仅 simulator backend
- type system 仅覆盖 uncomputation 一面

**Wen 可向 Silq 学习的**: 具体的 uncomputation 算法、type inference 策略、user-facing syntax 简洁性。

### 2.5 Quipper / Proto-Quipper

**定位**: Haskell-embedded 函数式量子语言；GADTs 表达 circuit types。Proto-Quipper 是其 type-theoretic refinement，引入 linear types 严格管理 qubit。

**与 Wen 的关系**:
- Proto-Quipper 的 **linear types for qubits** 实质做的事是"qubit 不可复制"——这与 Wen 的"split/merge 是同构但 cloning 不是"同 spirit
- Quipper 的 GADT 编码 circuit types，类似 Wen 的 dependent typing 但 less expressive
- Quipper 主要在 academic circle，工业采用极少

**Wen 与 Quipper 的关键差异**:
- Quipper 是 quantum-specific；Wen 是 classical/quantum 统一
- Quipper 没有 modal 维度；Wen 有 first-class ⊠
- Quipper 用 linear types 表达 quantum constraint；Wen 用 dependent + modal 表达更广的信息流约束

### 2.6 QWIRE / SQIR / VOQC (Princeton 系列)

**定位**: Coq-embedded 量子程序 verification framework。QWIRE 是 typed quantum circuit language；SQIR 是 verified quantum IR；VOQC 是 verified quantum optimizing compiler。

**核心贡献**: 量子编译器 / 算法的 machine-checked 形式 verification——任何 compiler pass 都带 Coq proof 说明它保持 semantics。

**与 Wen 的关系**: **这是 Wen 的 closest verification cousin**。两者都用 dependent type theory（Coq vs Lean）做 quantum 验证。差别在：

| 维度 | QWIRE/SQIR | Wen |
|---|---|---|
| 宿主语言 | Coq | Lean 4 |
| 信息流 | 命题手写 prove | first-class type 内蕴 |
| 模态 | 无 first-class | 四值 modal |
| 经典/量子统一 | 主要 quantum | 完全统一 |
| 表达 surface | Coq 数学 syntax | 古文 surface |

QWIRE 系列是 Wen 在 verification 这一支的**最近学术工作**——任何对 Wen 严肃的 academic 比较都应引用 QWIRE。

**互补关系**: Wen 与 QWIRE/SQIR 都用 dependent type system。如果 Wen 成熟，技术上可以与 QWIRE 互译——把 Wen 程序编译到 SQIR，反向把 SQIR theorem import 回 Wen 作为 lemma。这是 plausibly 协同。

### 2.7 ZX-calculus / PyZX

**定位**: 量子计算的**图形 calculus**——不是 programming language，是数学语言。用 spiders、edges、rewriting rules 表达 quantum 程序，有 completeness theorem (any equation in Clifford+T can be derived via ZX rules)。

**核心特征**:
- 图形 vs 文本
- 重写规则 + 简化 normal form
- 优化 circuit (PyZX 在 T-count 上比 Qiskit transpiler 强很多)
- 与 stabilizer formalism 紧密对应

**与 Wen 的关系**: **ZX 是 Wen 的 mathematical sister**——both 在 stabilizer 子代数 + Clifford+T 这一层做事。差别：

- ZX 是 calculus（数学操作 system），Wen 是 programming language（可写可跑的程序）
- ZX 没有类型系统（图就是程序），Wen 有 dependent type
- ZX 优化能力 mature 且 industry-adopted（IBM 用 PyZX 优化 transpiler），Wen 无
- ZX 不携带模态信息（只是 quantum 拓扑），Wen 有 ⊠ + 四值模态

**互补关系**: Wen 的"信息流"维度与 ZX 的"图形拓扑"维度是 orthogonal——可以 imagine 一个工具链把 Wen 程序 transpile 到 ZX 做图形优化，再回 Wen 做 verification。这是合理协作路径。

### 2.8 D-Wave Ocean / Adiabatic 范式

**定位**: 完全不同的 quantum paradigm——adiabatic / annealing。把 problem 编码成 QUBO 或 Ising Hamiltonian，让物理 system 慢演化到 ground state。

**与 Wen 的关系**: **Wen 不与 D-Wave Ocean 竞争或可比**——两者属于不同 quantum paradigm。Wen 是 gate-model；D-Wave 是 adiabatic。

**唯一可能的连接**: Wen 的 modal 结构理论上能 model adiabatic process（缓慢演化 + 守恒约束），但这需要 Wen 引入连续时间动力学，目前不在 scope。

### 2.9 PennyLane (Xanadu)

**定位**: 可微分 quantum programming，主要服务 quantum ML / variational algorithm。Python embedded，gradient 自动微分。

**与 Wen 的关系**:
- PennyLane 是 quantum + 自动微分；Wen 是 quantum + 信息流追踪。**完全不同的 specialty**
- 但都把 quantum 看作 "structured computation"，不是单纯 circuit
- 工业上 PennyLane 在 variational quantum algorithm 领域 dominant

**互补**: Wen 程序可能作为 PennyLane variational ansatz 的 verified template——Wen 提供 ansatz 的 structure proof，PennyLane 做 parameter 优化。

---

## §3 综合对比表

| 语言 | 类型 | 信息流 | 可逆性 | Modal | C/Q 统一 | 层级 | Verification | Hardware | 成熟度 |
|---|---|---|---|---|---|---|---|---|---|
| **Qiskit** | weak | none | manual | none | 分离 | 平铺 | external | many | ⭐⭐⭐⭐⭐ |
| **Cirq** | weak | none | manual | none | 分离 | 平铺 | external | Google + | ⭐⭐⭐⭐ |
| **Q#** | strong | partial | functor | basic | 嵌入 | logical qubit | embedded | Azure | ⭐⭐⭐⭐ |
| **Silq** | strong | implicit | **automatic** | none | quantum only | 平铺 | type-driven | simulator | ⭐⭐ |
| **Quipper** | strong (linear) | partial | linear | none | quantum only | 平铺 | external | simulator | ⭐⭐ |
| **QWIRE/SQIR** | dependent (Coq) | manual prove | manual prove | none | quantum only | 平铺 | **by construction** | research | ⭐⭐ |
| **ZX-calculus** | N/A (graphical) | graphical | graphical | none | quantum only | flat graph | proof system | optimization | ⭐⭐⭐ |
| **PennyLane** | weak | none | manual | none | hybrid ML | 平铺 | external | many | ⭐⭐⭐⭐ |
| **D-Wave Ocean** | weak | N/A | N/A | N/A | annealing | flat | external | D-Wave only | ⭐⭐⭐ |
| **文 (Wen)** | **dependent + modal** | **first-class** | **structural** | **first-class** | **统一 substrate** | **self-similar 塔** | **by construction** | **none yet** | ⭐ (pre-alpha) |

**关键观察**:

1. Wen 在前 7 个 paradigm/structural 轴上**单家占据最深位置**——没有其他语言在这些 axis 上同时达到 Wen 的深度
2. Wen 在后 3 个 maturity/practical 轴上**明显劣后于工业 mature 语言**——这是真实劣势，不是修辞
3. 没有任何一种语言在所有维度都领先；Wen 选择了 paradigm depth 而牺牲 maturity

---

## §4 Wen 的 distinctive 位置

### 4.1 独占的设计空间

Wen 在一个**没人占据**的 design space：

- **Silq** 追求 uncomputation 自动化，但仅 quantum
- **Q#** 追求工业可用，但 paradigm depth 不够
- **QWIRE/SQIR** 追求 verification，但用 Coq 数学 syntax（程序员 hostile）、且 quantum-only
- **ZX** 追求图形优化，但不是 programming language

**Wen** 把这几条线**同时做到**：dependent + modal + 信息流 first-class + classical/quantum 统一 + 由 surface syntax 可写可跑 + by construction verification。**这个组合在 2026 年没有别人在做**。

### 4.2 paradigm gap 的具体内容

举一个具体的对比：写 "verified Grover's algorithm"。

**Qiskit**: 构造 circuit，写 unit test，希望它对。verification 不在语言里。

**Q#**: 构造 operation with `Adjoint`、`Controlled`，run unit test，可以用 Q# Quantum Development Kit 的 estimator。verification 有限。

**Silq**: 类型 check 保证 uncomputation 正确，但算法 correctness 仍需手 verify。

**QWIRE/SQIR**: 在 Coq 里写 Grover，写 spec，写 proof。**严格 verified 但工程成本巨大**（每个 lemma 手写）。

**Wen**: 用 Wen 的 9 atom + R_n 塔结构写 Grover。**信息守恒 by construction**；amplification 步骤的 fixed-point 性质由 ⊠ + 救援不变量自动表达；最终 measurement 的 success 概率由 modal classification 给出 type-level 保证。verification 是构造过程的副产品。

**这是 paradigm gap**：Wen 不是更易用、不是更快，是**让一类原本困难的 verification 变成自动副产品**。

### 4.3 ⊠ 是关键 differentiator

所有其他 QPL 都**没有 first-class ⊠**。

- Qiskit / Cirq: measurement 失败 = exception
- Q# / Silq: measurement 是 `Result` 类型 (Zero/One)
- QWIRE: measurement 是 distribution
- ZX: 不直接 model measurement uncertainty

**Wen 的 ⊠**：把 "gate 关闭，信息不可获取，结构上塌缩" 做成与 □真/□假 同级的一阶状态。这能 model 的物理现象：
- **leakage** (qubit 离开 computational subspace)
- **erasure** (qubit 物理消失)
- **gauge mismatch** (encoded state 不在 codespace)

这些现象在量子硬件中是真实 failure mode，目前 QPL 都把它当 error 处理，**Wen 把它做成 first-class state**。这是真正的 paradigm 创新。

---

## §5 各语言的协同 vs 竞争

### 5.1 不竞争（不同 niche）

- **D-Wave Ocean**: 不同 paradigm（adiabatic vs gate）
- **PennyLane**: 不同 specialty（auto-diff vs info-flow）
- **ZX-calculus**: 不同 modality（图形 vs 文本）

### 5.2 部分竞争 / 互补

- **Q#**: 同 strong-typed niche，但 Wen 更深；Q# 工业可用 Wen 未来可用；**长期 Wen 替代部分 Q# verification 任务**
- **Silq**: 思想最近，但 Silq 仅 quantum；**Wen 实质 generalize Silq**
- **QWIRE/SQIR**: 同 verification niche；**长期 Wen 与 QWIRE 互译协作**，不是替代

### 5.3 直接竞争（同设计空间）

**没有**——这是上文 §4.1 的结论。Wen 占据的 design space 目前无 competitor。

### 5.4 可能的协同 pipeline

```
Wen high-level (verification, info flow)
    ↓ transpile
Q# / Silq (mid-level typed quantum)
    ↓ transpile  
Qiskit / Cirq IR (circuit-level)
    ↓ optimize
ZX-calculus (graphical optimization)
    ↓ output
OpenQASM (hardware IR)
    ↓ execute
IBM/Google/AWS hardware
```

Wen 在 stack 最上层做 paradigm/verification 工作，每一层向下 transpile 时承诺 preserve specific properties。这是 plausibly 的工业整合路径。

---

## §6 实用建议：何时用什么

### 6.1 现在 (2026) 用什么

| 任务 | 推荐 | 理由 |
|---|---|---|
| 在 IBM Quantum 上跑算法 | **Qiskit** | 生态 + 硬件 |
| Google Quantum AI 上做 NISQ 研究 | **Cirq** | 团队工具链 |
| 企业 .NET 集成 quantum | **Q#** | 平台集成 |
| 量子 ML / VQE / QAOA | **PennyLane** | auto-diff |
| 形式 verified quantum compiler | **QWIRE / SQIR** | 已有成果 |
| Clifford+T circuit 优化 | **ZX-calculus** | optimization power |
| QUBO / 组合优化 | **D-Wave Ocean** | adiabatic 范式 |
| **Wen** | research / formal foundation | 不是 production-ready |

**诚实说**：2026 年没有 production 工作应该用 Wen。Wen 现阶段是 research foundation。

### 6.2 2-5 年后用什么

Wen 成熟后的 niche：
- **量子算法 verification**（替代 QWIRE 的部分工作，更易用）
- **可逆经典计算工具链**（目前空白）
- **跨 classical/quantum boundary 的形式 verified pipeline**（目前不存在）
- **量子编程教学 / 跨文化 outreach**（Wen 的中文 surface 是独特资源）

### 6.3 长期 (10+ 年) 的 vision

Wen 成熟生态下：
- **standard verification language** for fault-tolerant quantum compilers
- **可逆计算 paradigm** 的 mainstream 入口
- **Wen-shaped hardware**（见 wen-info-paradigm.md §8 的 hardware vision）的 high-level 语言
- 经典-量子 hybrid 系统的统一开发 framework

这是 vision，不是承诺。落地依赖 ecosystem + community + 实际 hardware 配合。

---

## §7 一个 honest 自评

不能写完一篇比较然后只说 Wen 的好。诚实交代 Wen 当前的劣势：

### 7.1 生态空白

- 无 standard library
- 无 IDE 支持
- 无 package manager
- 无 tutorial / cookbook
- 无 community

每一项都是 Qiskit / Q# 多年积累。Wen 至少需要 2-3 年才能在这些维度达到"可用"水平。

### 7.2 无硬件 backend

不能在真硬件跑。simulator 也未实现。任何"我想跑这段 Wen 试试"的需求**现在都做不到**。

### 7.3 学习曲线陡

需要先理解：
- Lean 4 dependent type
- $\mathbb{F}_2$ 上的代数（偶倍分解、闭包、汉明几何）
- 道-依赖族的模态语义
- 古文 surface syntax
- 修养论/易学的概念框架

这是 PhD-level prerequisites。Qiskit 大一学生可学，Wen 现阶段对 PhD 都有挑战。

### 7.4 还未经实战检验

paper §1-§10 的形式系统是**纸上**正确，但还没在大型程序上磨过。可能会发现某些设计在工程实践中不 scale，需要修正。这是 research-stage 项目的常态，但要诚实交代。

### 7.5 cultural framing 的 mixed reception

中文 surface + 古典哲学 framing 在英语主导的 quantum community 可能 alienating 或 mis-perceived as "exotic"。这一选择有真实成本——academic conference 接受度、industry adoption 摩擦、reviewer bias 都可能受影响。

但这一 framing 也有**真实价值**——把 quantum 从纯西方话语挪开一条路，让中文母语者通过熟悉的语法范畴接触量子，是有 educational 意义的。trade-off 不是 free。

---

## §8 一句 strategic positioning

**Wen 与现存 quantum 编程语言的关系**：

- 不和 Qiskit / Cirq 竞争 NISQ circuit 编写（不同抽象层）
- 不和 Q# / Quipper 竞争工业 production（成熟度差距）
- 不和 D-Wave 竞争 adiabatic 范式（不同物理基础）
- 不和 PennyLane 竞争 quantum ML（不同 specialty）

**Wen 与现存 quantum 编程语言的关系**：

- **generalize 并 deepen Silq 的核心 insight**——信息守恒做成结构而非自动化
- **更 programmer-friendly 地实现 QWIRE/SQIR 的 verification 愿景**——用古文 surface 替代 Coq math syntax
- **互补 ZX-calculus 的图形优化**——Wen 做 verification，ZX 做拓扑简化
- **占据无 competitor 的 paradigm depth + classical/quantum 统一 + cultural distinctiveness 的设计空间**

短期（2026-2028）：**research foundation**，与 academic verification community 对话。

中期（2028-2032）：**verification 工具**，覆盖 fault-tolerant 量子编译的特定 niche。

长期（2032+）：**substrate**，给围绕 Wen 设计的 quantum 硬件（见 wen-info-paradigm.md §8）做 native high-level 语言。

---

## 附录 A：每家语言的代表论文 / 文档

供 academic 引用：

- **Qiskit**: Cross et al., "Open Quantum Assembly Language", arXiv:1707.03429
- **Cirq**: Google AI Quantum, "Cirq: A Python framework for ...", 2018
- **Q#**: Svore et al., "Q#: Enabling Scalable Quantum Computing ...", 2018
- **Silq**: Bichsel et al., "Silq: A High-Level Quantum Language ...", PLDI 2020
- **Quipper**: Green et al., "Quipper: A Scalable Quantum Programming Language", PLDI 2013
- **Proto-Quipper**: Ross, "Algebraic and Logical Methods in Quantum Computation", PhD thesis 2015
- **QWIRE**: Paykin, Rand, Zdancewic, "QWIRE: A Core Language for Quantum Circuits", POPL 2017
- **SQIR**: Hietala et al., "A verified optimizer for Quantum circuits", POPL 2021
- **ZX-calculus**: Coecke, Duncan, "Interacting Quantum Observables", 2008 (original); van de Wetering, "ZX-calculus for the working quantum computer scientist", arXiv:2012.13966 (modern review)
- **PennyLane**: Bergholm et al., arXiv:1811.04968
- **D-Wave Ocean SDK**: D-Wave documentation

## 附录 B：与 `wen-info-paradigm.md` 的呼应

本文是 paradigm 论证的**经验对照**。`wen-info-paradigm.md` §3 给出抽象的语言光谱表；本文 §3 的综合表是其 quantum 具体化。

`wen-info-paradigm.md` §7 列了 Wen 的"杀手 use case"；本文 §6 给出现实可执行的"何时用什么"——把 vision 落到具体决策。

两文同读，可获得 Wen 在 quantum 编程语言生态中的完整定位。
