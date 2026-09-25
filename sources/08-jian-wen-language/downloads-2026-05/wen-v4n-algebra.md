# V₄ⁿ 代数：完备性、接口、信息守恒

> **文 形式语言** · Foundation Note
> Companion to: `v4-foundation.md`
> **Dual-track**: Lean 4 + Mathlib 机器证明 / 文 compiler IR + Clojure runtime
> v0.1

---

## 0. 文档目的

本文档是 `v4-foundation.md` 的**结构理论补**。
v4-foundation 给出 V₄ 这一**单层**的代数与跨域 atlas；
本文档证立 **V₄ⁿ 家族**作为 文 接口体系的不可替代性。

核心论点四条：

1. **V₄ⁿ 是代数完备的** — 在直和、子群、商、对偶、Hom、F₂-张量下，封闭于 V₄ⁿ 族内
2. **V₄ⁿ 是 文 的接口层** — 仅 V₄ⁿ (n=1,2,3,4,...) 是 文 的一等类型；R 塔的奇秩位是中间结构，不暴露
3. **每个 V₄ⁿ 层有精确的信息容量** — 2n 个 F₂-bit，组织为 n 个 V₄-坐标，唯一分解
4. **V₄ⁿ 上的 dot product 不丢信息** — 同时具备 (a) 非退化 → basis 恢复，(b) V₄-component 因式化 → 类型守恒

这四条直接决定 文 编译器的 type system 与 Lean 证明的 module 边界。

---

## 1. V₄ⁿ 的三视角定义

### 1.1 作为阿贝尔群

$$V_4^n := \underbrace{V_4 \times V_4 \times \cdots \times V_4}_{n \text{ 次}}$$

n 个 Klein 四元群的直积。

性质：
- 基数 $|V_4^n| = 4^n$
- 所有非恒等元自反 (self-inverse)
- 阿贝尔，exponent 2
- 等价于 elementary abelian 2-group of rank $2n$

### 1.2 作为 F₂ 向量空间

$V_4 \cong \mathbb{F}_2^2$ 作为 $\mathbb{F}_2$-向量空间。所以：

$$V_4^n \cong \mathbb{F}_2^{2n}$$

$\mathbb{F}_2$-维数 $2n$。元素一一对应于长度 $2n$ 的 0/1 串。

### 1.3 作为 V₄-坐标分解

$$V_4^n = V_4 \oplus V_4 \oplus \cdots \oplus V_4 \quad (n \text{ 次直和})$$

每个元素 $U \in V_4^n$ 唯一分解为 $U = (u^{(1)}, u^{(2)}, \ldots, u^{(n)})$，其中每个 $u^{(i)} \in V_4$。这个分解称为 $U$ 的 **V₄-坐标分解**。

### 1.4 三视角的关系

三个视角同构等价，但强调不同结构：

| 视角 | 强调 | 文中用途 |
|------|------|---------|
| (1.1) 阿贝尔群 | 群运算、self-inverse | Lean 中 CommGroup instance |
| (1.2) F₂-向量空间 | 线性、双线性、bit 表示 | IR encoding，bit-level 操作 |
| (1.3) V₄-坐标 | V₄ 作为不可约 typed primitive | type system 的根 |

**(1.3) 是 文 工程的首要视角**——V₄ⁿ 不是「2n 个 bit」，而是「n 个 V₄ 单位」。这个区别贯穿后续讨论。

---

## 2. 代数完备性

> **定义 (V₄ⁿ-族)**：所有 $V_4^n$ for $n \in \mathbb{N}_{\geq 0}$，含平凡 $V_4^0 = \{e\}$。

族在以下运算下封闭：

### 2.1 直积 / 直和

$$V_4^a \oplus V_4^b \;=\; V_4^{a+b}$$

阶 $4^a \cdot 4^b = 4^{a+b}$。结构仍是 Klein-tower。✓

### 2.2 V₄^k 形子群

每个 V₄^k 子群对应于固定某些 V₄-坐标位为 $e$。给定 $V_4^n$ 的任一 $V_4^k$ 子群 $H$，存在 $V_4^{n-k}$ 子群 $K$ 使：

$$V_4^n = H \oplus K$$

注意：不是所有子群都是 $V_4^k$ 形（例如对角嵌入），但 **所有 $V_4^k$ 形子群封闭**。

### 2.3 商封闭

$$V_4^n \,/\, V_4^k \;\cong\; V_4^{n-k}$$

由 abelian 性，所有子群正规，商良定。✓

### 2.4 Pontryagin 对偶自封闭

V₄ⁿ 的 character 群：

$$\widehat{V_4^n} = \mathrm{Hom}(V_4^n, S^1) \cong \mathrm{Hom}(V_4^n, \mathbb{F}_2) \cong V_4^n$$

V₄ⁿ **Pontryagin 自对偶**。这是后续 dot product 自然存在的根。

### 2.5 Hom 封闭

$\mathbb{F}_2$-线性映射空间：

$$\mathrm{Hom}_{\mathbb{F}_2}(V_4^a, V_4^b) \cong \mathbb{F}_2^{2a \times 2b} = \mathbb{F}_2^{4ab} \cong V_4^{2ab}$$

✓ 但注意指数律变化：$(a, b) \mapsto 2ab$（不是 $a + b$）。

### 2.6 F₂-张量封闭

向量空间张量积：

$$V_4^a \otimes_{\mathbb{F}_2} V_4^b \cong \mathbb{F}_2^{2a} \otimes_{\mathbb{F}_2} \mathbb{F}_2^{2b} = \mathbb{F}_2^{4ab} \cong V_4^{2ab}$$

封闭。指数律 $(a, b) \mapsto 2ab$。

### 2.7 封闭性主定理

**定理 (V₄ⁿ-族闭合)**：以下函子均将 V₄ⁿ-族映回自身：

| 函子 | 指数律 | 用处 |
|------|--------|------|
| 直和 $\oplus$ | $n + m$ | 拼接元素层 |
| V₄^k-子群 | $k \leq n$ | 投影 |
| 商 / V₄^k | $n - k$ | 抽象化 |
| Pontryagin 对偶 | $n$ | dot product 来源 |
| F₂-Hom | $2nm$ | 线性映射空间 |
| F₂-张量 | $2nm$ | 状态空间复合 |

——这是 V₄ⁿ 族 **代数完备性** 的精确含义。

### 2.8 与族外对象的对比

考虑奇秩 $\mathbb{F}_2^{2k+1}$：

- 是 abelian 群、是 F₂-向量空间
- **不属于 V₄ⁿ 族**（无 V₄-张量分解）
- 与 V₄ⁿ 的直和会产生奇秩输出：$V_4^n \oplus \mathbb{F}_2^{2k+1} = \mathbb{F}_2^{2n+2k+1}$ ← 仍奇秩，逃出族

$$\mathbb{F}_2^{2k+1} = V_4^k \oplus \mathbb{F}_2 \;\;\text{（不典则）}$$

其中 $\mathbb{F}_2$ 是「孤立的半个 V₄」——无法获得完整 V₄-typing。

**结论**：V₄ⁿ 族是 F₂-向量空间这个更大世界中 **保 V₄-typing 的闭合子世界**。

---

## 3. 接口层级

### 3.1 V₄ⁿ 序列

文 工程的接口层级：

```
n = 0:  V₄⁰ = 1 元      平凡    (恒等)
n = 1:  V₄¹ = 4 元      原子算子层    {道, 错, 综, 错综}
n = 2:  V₄² = 16 元     pair 算子层   (命名缺口)
n = 3:  V₄³ = 64 元     卦空间        (易经 64 卦)
n = 4:  V₄⁴ = 256 元    V₈ cell 层    (卦 × 时态)
n = 5:  V₄⁵ = 1024 元   ...
```

V₄ 与 V₈ 之前并列为「双接口」。修正后：

> V₄ = V₄¹（底层算子接口）
> V₈ = V₄⁴（含时态状态接口）
> V₄²、V₄³ **同样是接口层**，不是 V₄ 与 V₈ 之间的过渡

### 3.2 接口 vs 中间结构的判别

**接口层（$\in$ V₄ⁿ-族）**：
- 是 文 surface syntax 中可命名的语义类型
- 编译器 IR 的 first-class type
- Lean 中作为 `inductive` / `def` 单独定义
- 保 V₄ typing propagation
- 与同族其他层的运算结果仍在族内（§2 闭合性）

**中间结构（$\notin$ V₄ⁿ-族）**：
- 出现在分解 / 分析过程中（子空间、coset、fiber）
- 编译器中作为 internal computation step，不暴露给 surface syntax
- Lean 中作为引理或辅助定义
- 不保 V₄ typing，需在边界 coerce

### 3.3 旧塔 R₀–R₈ 的修正

旧 R₀–R₈ 塔将 9 个层级线性平铺。修正：

| R-层 | 维数 | $\in$ V₄ⁿ-族 | 角色 |
|------|------|------|------|
| R₀ | 0 | V₄⁰ | 平凡接口 |
| R₁ | 1 | ✗ | **中间** (半 V₄) |
| R₂ | 2 | V₄¹ | **接口** — 原子算子 |
| R₃ | 3 | ✗ | **中间** |
| R₄ | 4 | V₄² | **接口** — pair |
| R₅ | 5 | ✗ | **中间** |
| R₆ | 6 | V₄³ | **接口** — 卦空间 |
| R₇ | 7 | ✗ | **中间** |
| R₈ | 8 | V₄⁴ | **接口** — V₈ cell |

**只有偶秩 R-层是接口**。奇秩 R-层（R₁, R₃, R₅, R₇）是分解过程中出现的中间结构，**不应作为接口暴露**。

旧塔把 9 层线性陈列，掩盖了真正的结构事实——**接口分布在偶秩 R-层上，并对应于 V₄ⁿ 的 n 轴**。

### 3.4 为什么奇秩不是接口

**结构原因**：$\mathbb{F}_2^{2n+1}$ 不可能写成 V₄ 的整数次直和：

$$\mathbb{F}_2^{2n+1} = V_4^n \oplus \mathbb{F}_2$$

孤立的 $\mathbb{F}_2$ 因子是「半个 V₄」——它有一个 bit，但没有完整 V₄ 的双轴结构，无 typed 身份。

**实践影响**：

1. 文 surface 不应有「半 V₄」字
2. 任何编译过程若产出奇秩中间，必须 round-trip 回偶秩才能 emit
3. type checker 拒绝奇秩 $\mathbb{F}_2^?$ 类型出现于 surface
4. Lean 证明的 module 边界沿偶秩切——奇秩仅作为引理的内部步骤

---

## 4. 每层信息守恒

### 4.1 Layer Information Completeness (LIC)

> **LIC 定义**：给定 V₄ⁿ 层的任意元素 $U$，存在**唯一** 2n-bit 表示
> $$\big[u_1^{(\alpha)}, u_1^{(\beta)}, u_2^{(\alpha)}, u_2^{(\beta)}, \ldots, u_n^{(\alpha)}, u_n^{(\beta)}\big]$$
> 且此表示与 V₄-坐标分解 $U = (u^{(1)}, \ldots, u^{(n)})$ 一一对应。

LIC 等价于：**$U$ 的 V₄-坐标分解唯一**。

### 4.2 V₄-坐标分解的典则性

V₄ⁿ 的 V₄-张量分解依赖**典则基**：

$$\mathcal{B} = \{E_i^{(\alpha)}, E_i^{(\beta)}\}_{i=1,\ldots,n}$$

其中 $E_i^{(\alpha)}$ 是「第 $i$ 个 V₄ 的 $\alpha$-坐标为 1，其他全 0」的元素，类似 $E_i^{(\beta)}$。

这个基典则，因为：

1. 由 $V_4^n = V_4 \times \cdots \times V_4$ 的直积结构**直接给出**
2. 与 V₄ 的群运算**兼容**（每分量独立做 V₄ 运算）
3. 任何保 V₄-typing 的 V₄ⁿ 自同构 $\sigma$ 将 $\mathcal{B}$ 映到等价基（差一个 V₄ⁿ-内 permutation + V₄-内自同构）

**定理 (V₄-坐标唯一性)**：在 V₄ⁿ 上保 V₄-typing 的自同构群作用下，V₄-坐标分解唯一。

### 4.3 每层信息容量表

| 层 | 元素数 | F₂-bits | V₄-坐标数 | 文中地位 |
|----|-------|---------|-----------|---------|
| V₄¹ | 4 | 2 | 1 | 原子算子 |
| V₄² | 16 | 4 | 2 | pair 算子（命名空缺）|
| V₄³ | 64 | 6 | 3 | 64 卦 |
| V₄⁴ | 256 | 8 | 4 | 256 V₈ cells |
| V₄ⁿ | $4^n$ | $2n$ | $n$ | — |

每层从下一层翻倍 V₄-坐标数 → 平方元素数。这是层级信息的精确刻度。

### 4.4 64 / 256 的代数解释

V₄³ = 64：每卦由 3 个 V₄-坐标决定。
- 与 6 爻一一对应（每 V₄-坐标 = 2 爻）
- 错卦 = 在所有 3 个 V₄-坐标上施 $a$；综卦 = 施 $b$
- **3 个 V₄-坐标是文层级建模的基本计量**，不是「6 爻」也不是「2³ 三爻」

V₈ = V₄⁴ = 256：每 cell 由 4 个 V₄-坐标决定。
- 前 3 V₄-坐标 = 卦空间 (V₄³)
- 第 4 V₄-坐标 = 时间 V₄ = {道, 未, 已, 今}
- $256 = 64 \times 4$

这两个数字在 文 中不是「神秘巧合」——它们是 $V_4^n$ 在 $n=3, 4$ 的自然 cardinality。

---

## 5. Dot Product 与信息不失

### 5.1 V₄ 上的 dot product

V₄ 作为 $\mathbb{F}_2^2$，坐标 $(\alpha, \beta)$：

$$\langle u, v \rangle := u_\alpha \cdot v_\alpha + u_\beta \cdot v_\beta \in \mathbb{F}_2$$

其中 $\cdot = \mathrm{AND}$，$+ = \mathrm{XOR}$。

V₄ pairing 表：

| | $e$ | $a$ | $b$ | $ab$ |
|---|---|---|---|---|
| $e$  | 0 | 0 | 0 | 0 |
| $a$  | 0 | 1 | 0 | 1 |
| $b$  | 0 | 0 | 1 | 1 |
| $ab$ | 0 | 1 | 1 | 0 |

性质：对称、双线性、非退化（每非零元配对全空间时取值非恒零）。

### 5.2 V₄ⁿ 上的 dot product

对 $U = (u^{(1)}, \ldots, u^{(n)})$, $V = (v^{(1)}, \ldots, v^{(n)}) \in V_4^n$：

$$\boxed{\;\langle U, V \rangle := \sum_{i=1}^{n} \langle u^{(i)}, v^{(i)} \rangle_{V_4} \in \mathbb{F}_2 \;}$$

——**V₄ⁿ 的 dot product 是 n 个 V₄ dot product 的正交直和**。

这是 V₄ⁿ 上 dot product 的**典则定义**。它继承 V₄ pairing 的全部结构，并且：

> dot product 计算 **component-wise 分解**，与 V₄-坐标分解兼容

这是「typed 兼容性」陈述。是 V₄ⁿ 与一般 $\mathbb{F}_2^k$ 的关键差异。

### 5.3 基本性质

V₄ⁿ 上 $\langle \cdot, \cdot \rangle$ 满足：

1. **对称**：$\langle U, V \rangle = \langle V, U \rangle$
2. **F₂-双线性**：$\langle U + W, V \rangle = \langle U, V \rangle + \langle W, V \rangle$
3. **非退化**：$\forall V.\ \langle U, V \rangle = 0 \Rightarrow U = 0$
4. **V₄-component 因式化**：$\langle U, V \rangle = \sum_{i} \langle u^{(i)}, v^{(i)} \rangle$

性质 (4) 是 V₄ⁿ 的 **不可替代特征**。

### 5.4 信息不失的两层含义

**Sense 1（线性）：非退化 ⇒ basis 全恢复**

给定 V₄ⁿ 的典则基 $\mathcal{B} = \{E_1, \ldots, E_{2n}\}$（§4.2），任意 $U$ 可由其与基的配对完全恢复：

$$U = \sum_{i=1}^{2n} \langle U, E_i \rangle \cdot E_i$$

dot product 与基的全部 $2n$ 次配对，**足以零损失重构 $U$**。

这等价于 V₄ⁿ 的 Pontryagin 自对偶（§2.4）的具体实现：

$$V_4^n \xrightarrow{\;\sim\;} (V_4^n)^*, \quad U \mapsto \langle U, \cdot \rangle$$

——dot product 实现这个典则同构。

**Sense 2（V₄-typed）：因式化 ⇒ V₄-坐标独立恢复**

对 $U$ 的 V₄-坐标分解 $U = (u^{(1)}, \ldots, u^{(n)})$，每个 $u^{(i)}$ 由它在**第 $i$ 个 V₄-子空间内的两次配对**独立恢复：

$$u^{(i)} = \langle u^{(i)}, e_\alpha^{(i)} \rangle \cdot a + \langle u^{(i)}, e_\beta^{(i)} \rangle \cdot b$$

——**V₄-坐标层级的信息恢复是平行的，不需要跨 V₄ 因子的通信**。

**两个 sense 合起来说**：

> V₄ⁿ 上的 dot product 实现 **类型守恒的自对偶**——既守信息（线性 sense），又守 V₄ 类型（component sense）。

### 5.5 为什么仅在 V₄ⁿ 上成立

考虑奇秩 $\mathbb{F}_2^{2n+1}$：

- 任意 $\mathbb{F}_2^k$ 上都有非退化 dot product（**Sense 1 仍成立**）
- 但**无典则 V₄-坐标分解**（§3.4），所以**Sense 2 失败**
- dot product **无法 component-wise 因式**——必须在整个 $2n+1$ 维空间做内积，不能拆为 V₄ 因子之间的局部内积之和

操作上：

$$\mathbb{F}_2^3 = V_4 \oplus \mathbb{F}_2 \;\;\text{（分解不典则）}$$

$\mathbb{F}_2^3$ 上 dot 算出的 F₂ 标量，**不能被解释为 V₄ pairing 的结果**——它混合了一个无 V₄-typing 的孤立 bit。

**总结**：

| F₂-空间类型 | Sense 1 信息恢复 | Sense 2 V₄-typed |
|------|----|----|
| V₄ⁿ (偶秩) | ✓ | ✓ |
| 奇秩 $\mathbb{F}_2^{2k+1}$ | ✓ | ✗ |
| 非 V₄ⁿ-典则的偶秩子空间 | ✓ | ✗ |

——「lossless dot product」在 文 工程中的精确含义是 **Sense 1 + Sense 2 同时成立**，这等价于「输入空间是 V₄ⁿ 且使用典则 V₄-坐标基」。

---

## 6. 形式化骨架

### 6.1 Lean 4 + Mathlib

```lean
import Mathlib.Algebra.Group.Basic
import Mathlib.LinearAlgebra.Basic
import Mathlib.LinearAlgebra.BilinearForm.Basic
import Wen.V4

namespace Wen.V4n

open Wen.V4

/-- V₄ⁿ as n-fold direct product of V₄ -/
def V4n (n : ℕ) : Type := Fin n → V4.Elem

instance (n : ℕ) : CommGroup (V4n n) := Pi.commGroup

/-- V₄ pairing (atomic, on a single V₄) -/
def V4.dot : V4.Elem → V4.Elem → Bool
  | .dao,     _        => false
  | _,        .dao     => false
  | .cuo,     .cuo     => true
  | .cuo,     .zong    => false
  | .cuo,     .cuozong => true
  | .zong,    .cuo     => false
  | .zong,    .zong    => true
  | .zong,    .cuozong => true
  | .cuozong, .cuo     => true
  | .cuozong, .zong    => true
  | .cuozong, .cuozong => false

/-- V₄ⁿ dot product: orthogonal sum of V₄ dots -/
def dot {n : ℕ} (U V : V4n n) : Bool :=
  (Finset.univ : Finset (Fin n)).foldr
    (fun i acc => Bool.xor (V4.dot (U i) (V i)) acc) false

/-- §5.2: Component-wise factorization (by def) -/
theorem dot_componentwise {n : ℕ} (U V : V4n n) :
    dot U V = (Finset.univ : Finset (Fin n)).foldr
      (fun i acc => Bool.xor (V4.dot (U i) (V i)) acc) false := rfl

/-- §5.3.1: Symmetry -/
theorem dot_symm {n : ℕ} (U V : V4n n) :
    dot U V = dot V U := by
  -- by V₄.dot symmetry + commutativity of XOR
  ...

/-- §5.3.3: Non-degeneracy -/
theorem dot_nondegenerate {n : ℕ} (U : V4n n) :
    (∀ V, dot U V = false) ↔ U = (fun _ => V4.dao) := by
  ...

/-- §5.4 Sense 1: basis recovery -/
def basis_alpha {n : ℕ} (i : Fin n) : V4n n :=
  fun j => if h : i = j then V4.cuo else V4.dao

def basis_beta {n : ℕ} (i : Fin n) : V4n n :=
  fun j => if h : i = j then V4.zong else V4.dao

theorem info_recovery {n : ℕ} (U : V4n n) :
    U = (fun i =>
      let α := dot U (basis_alpha i)
      let β := dot U (basis_beta i)
      match α, β with
      | false, false => V4.dao
      | true,  false => V4.cuo
      | false, true  => V4.zong
      | true,  true  => V4.cuozong) := by
  ...

/-- §5.4 Sense 2: V₄-coordinate independent recovery -/
theorem coord_independent_recovery {n : ℕ} (U : V4n n) (i : Fin n) :
    U i = recover_v4_coord (dot U (basis_alpha i)) (dot U (basis_beta i)) := by
  ...

end Wen.V4n
```

### 6.2 Clojure / 文 compiler IR

```clojure
(ns wen.v4n
  "V₄ⁿ algebra · Wen compiler IR runtime"
  (:require [clojure.spec.alpha :as s]))

;; V₄ⁿ 元素表示
(s/def ::v4-elem #{:dao :cuo :zong :cuozong})
(s/def ::v4n-elem (s/coll-of ::v4-elem :kind vector?))

(defn v4n-arity [U] (count U))

;; ─── V₄ atomic dot product (§5.1) ───────────────────
(def v4-dot-table
  {[:dao :dao] 0,     [:dao :cuo] 0,      [:dao :zong] 0,     [:dao :cuozong] 0
   [:cuo :dao] 0,     [:cuo :cuo] 1,      [:cuo :zong] 0,     [:cuo :cuozong] 1
   [:zong :dao] 0,    [:zong :cuo] 0,     [:zong :zong] 1,    [:zong :cuozong] 1
   [:cuozong :dao] 0, [:cuozong :cuo] 1,  [:cuozong :zong] 1, [:cuozong :cuozong] 0})

(defn v4-dot [u v] (v4-dot-table [u v]))

;; ─── V₄ⁿ dot product as orthogonal sum (§5.2) ───────
(defn v4n-dot
  "V₄ⁿ dot product = XOR of V₄ dots over all coordinates."
  [U V]
  (assert (= (count U) (count V)) "V₄ⁿ arity mismatch")
  (->> (map v4-dot U V)
       (reduce bit-xor 0)))

;; ─── V₄-coordinate independent recovery (§5.4 Sense 2) ───
(defn recover-v4-coord
  "Recover the i-th V₄ coordinate of U from its two basis pairings.
   No information from other V₄ coordinates is used."
  [U i]
  (let [u_i (nth U i)
        bit-a (v4-dot u_i :cuo)
        bit-b (v4-dot u_i :zong)]
    (case [bit-a bit-b]
      [0 0] :dao
      [1 0] :cuo
      [0 1] :zong
      [1 1] :cuozong)))

;; ─── Basis-recovery convenience (§5.4 Sense 1) ──────
(defn basis-alpha [n i]
  (assoc (vec (repeat n :dao)) i :cuo))

(defn basis-beta [n i]
  (assoc (vec (repeat n :dao)) i :zong))

(defn recover-from-basis-pairings
  "Reconstruct U ∈ V₄ⁿ from its dot products with all 2n basis elements."
  [n basis-pairings]
  (vec
    (for [i (range n)]
      (let [bit-a (basis-pairings [:alpha i])
            bit-b (basis-pairings [:beta  i])]
        (case [bit-a bit-b]
          [0 0] :dao [1 0] :cuo [0 1] :zong [1 1] :cuozong)))))
```

### 6.3 双轨 round-trip 一致性

Lean 侧的每一条定理对应 Clojure 侧的一个 invariant：

| Lean 定理 | Clojure 对应 |
|-----------|----------------|
| `dot_componentwise` | `v4n-dot` 实现即定义 |
| `dot_symm` | `(v4n-dot U V) = (v4n-dot V U)` 性质测试 |
| `dot_nondegenerate` | type checker 拒绝零退化输入 |
| `info_recovery` | `recover-from-basis-pairings` |
| `coord_independent_recovery` | `recover-v4-coord` 仅依赖第 i 坐标 |

CI 检查：Clojure 的 `v4n-dot` 在所有 V₄ⁿ ($n \leq 4$ 穷举) 与 Lean kernel 计算一致。

---

## 7. 对 文 的工程影响

### 7.1 接口字层级

| 层 | 接口字范围 | 命名状态 |
|----|-----------|---------|
| V₄¹ | {道, 错, 综, 错综} | 完整（4 字）|
| V₄² | 16 个 | **空缺，待定** |
| V₄³ | 64 卦字 | 古已有之 |
| V₄⁴ | 64 × {道, 未, 已, 今} | 复合字（笛卡尔积命名）|

文 surface syntax 暴露的「foundation 字」即上述各层的元素字。V₄²（16 个）是当前命名缺口——见 §8 Open Question 1。

### 7.2 Type checker 规则

```
Rule 1: 任何 surface 字 c 必有 V₄ⁿ-签名: ∃ n. Type(c) = V₄ⁿ
Rule 2: dot product: dot : V₄ⁿ × V₄ⁿ → F₂  (n 相同强制)
Rule 3: arity 不同 / 类型非 V₄ⁿ ⇒ 编译失败
Rule 4: 奇秩 𝔽₂^? 禁出于 surface（只能 IR-internal）
Rule 5: 跨层 V₄ⁿ ↔ V₄ᵐ 必经显式 lift/project 算子
```

### 7.3 Normalize pass 的闭合性保证

由 §2.7 闭合性定理，编译器 normalize pass 中所有 V₄ⁿ 之间的操作（直和、Hom、张量、子群、商、dot product）均**保 V₄ⁿ-typing**。

> **normalize pass 在 V₄ⁿ 范围内 closed under composition**

不需要在中间步骤做 type coerce。这是相当强的工程保证——编译器可以做无类型擦除地连续 normalize，直到 surface emit 阶段。

### 7.4 与 v4-foundation.md 的边界

| `v4-foundation.md` | `wen-v4n-algebra.md` (本文档) |
|------|------|
| V₄ 单层的代数 atlas | V₄ⁿ 家族的塔结构 |
| {道, 错, 综, 错综} 的跨域映射 | V₄ⁿ 的代数完备性 |
| 4 级 preservation hierarchy | 信息容量分层 |
| {e, 错综} 子群特权 | 接口 vs 中间结构判别 |
| V₄-action on hexagrams | V₄ⁿ dot product 的两种 sense |

两文档配套：v4-foundation 给出 V₄ 的 **semantics**，本文档给出 V₄ⁿ 的 **scaffolding**。

---

## 8. Open Questions

1. **V₄² 的 16 个元素如何命名？** 从 Tier 1 借字？造新字？还是按 V₄ × V₄ 笛卡尔积 (道道, 道错, 道综, ..., 错综错综) 复合命名？
2. **V₄⁵ 及以上是否在 文 surface 暴露？** 还是仅作为 IR 内部使用？V₄⁵ = 1024 元，超出人脑可命名规模，可能要 IR-only。
3. **F₂ pairing 是否需要 quadratic refinement（Arf 不变量）才能区分某些 V₄ⁿ 子结构？** 这关系到 V₄ⁿ 上是否有更精细的 Boolean / symplectic 结构需刻画。
4. **Hom(V₄ⁿ, V₄ᵐ) 在 文 surface 如何 represent？** 是 $V_4^{2nm}$ 元素直接 emit，还是函数原语 + closure？
5. **V₄ⁿ 子群分类（subgroup lattice）** 在 文 中如何利用——尤其 §6.1 (v4-foundation) 的 {e, 错综} 在 V₄³ 中如何 lift？
6. **dot product 之外，V₄ⁿ 还有 quadratic form / symplectic form 等更精细 pairing。** 这些在 文 surface 是否暴露？

---

## 9. 完成度自检

| 内容 | 已覆盖 |
|------|------|
| V₄ⁿ 三视角定义 | ✓ §1 |
| 代数完备性（6 类闭合 + 主定理）| ✓ §2 |
| 接口 vs 中间结构判别 | ✓ §3 |
| 旧塔 R₀–R₈ 修正 | ✓ §3.3 |
| 信息容量分层（LIC）| ✓ §4 |
| 64 / 256 的代数解释 | ✓ §4.4 |
| Dot product 定义与性质 | ✓ §5.1–5.3 |
| 信息不失 Sense 1 + Sense 2 | ✓ §5.4 |
| 为何仅在 V₄ⁿ 上成立 | ✓ §5.5 |
| Lean + Clojure 双轨骨架 | ✓ §6 |
| 工程影响（type checker, normalize）| ✓ §7 |
| 与 v4-foundation.md 边界 | ✓ §7.4 |
| Open Questions | ✓ §8 |

---

*End of v0.1 · 文 V₄ⁿ Foundation Note · Algebra-Tower track*
