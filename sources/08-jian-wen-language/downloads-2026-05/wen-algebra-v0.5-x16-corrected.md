# 文 代数 — 𝕏 为 16 元基型之校正版
**The Xiang Algebra — 𝕏 as the 16-State Core Type**

> **文 形式语言** · Foundation Note  
> Supersedes: `wen-algebra v0.4`  
> **Dual-track**: Lean 4 + Mathlib 机器证明 / 文 compiler IR + Clojure runtime  
> **v0.5 · 𝕏=16 校正版**

---

## Changelog

- **v0.5 — 核心校正**：
  - 𝕏 不再定义为 4 元 Klein 四元群。
  - 𝕏 定义为 **16 元基类型**，代数上为：
    \[
    \mathbb{X} \cong \mathbb{F}_2^4 \cong \mathrm{Mat}_{2\times2}(\mathbb{F}_2) \cong \mathrm{End}_{\mathbb{F}_2}(\mathbb{F}_2^2).
    \]
  - `道/错/综/错综` 不再等同于 𝕏 本身，只作为 𝕏 内部编码所用的 **四基字 / 四元操作字**。
  - **对象 = 𝕏² = 256 元**。
  - 旧版 `1,4,16,64,256` 不再是 𝕏⁰–𝕏⁴ 的容量表；新版容量表为：
    \[
    1,16,256,4096,65536.
    \]
  - Hom、tensor、dot product、LIC、type checker、Lean/Clojure skeleton 全部按 `𝕏 = 16 元` 重写。

---

# 0. 核心改正 · Core Correction

## 0.1 唯一的 𝕏

本文档中只有一个 𝕏 符号：

\[
\boxed{\mathbb{X} \text{ 是 16 元基类型}}
\]

不再有“4 元 𝕏”与“16 元 𝕏”两套记号。

旧版中把：

\[
\{道,错,综,错综\}
\]

直接称为 𝕏，是错误的。新版规定：

> `道/错/综/错综` 是 𝕏 内部的四基字，不是 𝕏 本身。

𝕏 本身是由这些四基字构成的 16 元结构，最自然地理解为一个 2×2 的 \(\mathbb{F}_2\) 矩阵，或等价地理解为四基字空间上的 endomorphism。

---

## 0.2 四基字不是第二个 𝕏

为避免再制造第二个 X，本文不用另一个 X-like 符号表示四基字集合。必要时称其为：

\[
\mathsf{基字}=\{道,错,综,错综\}
\]

其数学结构为：

\[
\mathsf{基字}\cong V_4\cong \mathbb{F}_2^2.
\]

但它只是 𝕏 的内部编码层，不是 𝕏 tower 的一层。

四基字坐标约定：

| 文 | English | \(\mathbb{F}_2^2\) 坐标 |
|---|---|---|
| 道 | Identity / Way | \((0,0)\) |
| 错 | Content-Flip | \((1,0)\) |
| 综 | Frame-Flip | \((0,1)\) |
| 错综 | Compound-Flip | \((1,1)\) |

这四个字仍然重要，但它们的地位是：

> 𝕏 的内部坐标字 / 基础操作字 / 2-bit 子结构。

而不是：

> 𝕏 本身。

---

# 1. 𝕏 的正确定义 · Definition of 𝕏

## 1.1 作为 16 元有限向量空间

\[
\boxed{\mathbb{X} \cong \mathbb{F}_2^4}
\]

因此：

\[
|\mathbb{X}|=2^4=16.
\]

𝕏 是一个 4-bit 的有限 \(\mathbb{F}_2\)-向量空间。

每个 \(x\in\mathbb{X}\) 可写成：

\[
 x=(x_{00},x_{01},x_{10},x_{11})\in\mathbb{F}_2^4.
\]

工程上也可编码为 4-bit word。

---

## 1.2 作为 2×2 矩阵

更结构化地：

\[
\boxed{\mathbb{X}\cong \mathrm{Mat}_{2\times2}(\mathbb{F}_2)}
\]

即每个 \(x\in\mathbb{X}\) 可写成：

\[
 x=\begin{pmatrix}
 a & b \\
 c & d
 \end{pmatrix},\quad a,b,c,d\in\mathbb{F}_2.
\]

因此 𝕏 有两种自然操作：

1. **加法 / XOR**：
   \[
   x+y
   \]
   逐位 XOR，是 Abelian group 结构。

2. **复合 / 矩阵乘法**：
   \[
   x\circ y
   \]
   是 endomorphism composition，一般不交换。

这一区分是新版的核心：

> 𝕏 的 additive state layer 是 Abelian；𝕏 的 operator composition layer 可以 non-Abelian。

---

## 1.3 作为四基字空间的 Endomorphism

因为四基字空间同构于 \(\mathbb{F}_2^2\)，所以：

\[
\boxed{\mathbb{X}:=\mathrm{End}_{\mathbb{F}_2}(\mathsf{基字})}
\]

即：

\[
\mathbb{X}\cong\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{F}_2^2,\mathbb{F}_2^2)
\cong\mathrm{Mat}_{2\times2}(\mathbb{F}_2).
\]

这给出 𝕏 的 16 元来源：

\[
|\mathrm{Mat}_{2\times2}(\mathbb{F}_2)|=2^4=16.
\]

因此，旧版中所谓“对象 = Hom(象,象) = 16 元”的那一层，实际上应提升为：

\[
\boxed{\mathbb{X}=\mathrm{Hom}(\mathsf{基字},\mathsf{基字})}
\]

而不是：

\[
\mathbb{X}=\mathsf{基字}.
\]

---

## 1.4 𝕏 的双重身份

𝕏 的每个元素既可读作 state，也可读作 op。

| 读法 | 数学形式 | 说明 |
|---|---|---|
| State | \(x\in\mathbb{F}_2^4\) | 4-bit / 16-state semantic atom |
| Matrix | \(x\in\mathrm{Mat}_{2\times2}(\mathbb{F}_2)\) | 2×2 binary matrix |
| Op | \(x:\mathsf{基字}\to\mathsf{基字}\) | four-base endomorphism |

此处 state/op 的共体性是 𝕏 的基础特征之一。但工程上必须区分 additive use 与 compositional use。

---

# 2. 𝕏ⁿ 塔 · The 𝕏ⁿ Tower

## 2.1 定义

\[
\mathbb{X}^n := \underbrace{\mathbb{X}\times\cdots\times\mathbb{X}}_{n\text{ 次}}
\]

由于：

\[
\mathbb{X}\cong\mathbb{F}_2^4,
\]

所以：

\[
\boxed{\mathbb{X}^n\cong\mathbb{F}_2^{4n}}
\]

并且：

\[
\boxed{|\mathbb{X}^n|=16^n=2^{4n}}.
\]

---

## 2.2 正确容量表

| 层 | 文名 | English | 容量 | F₂-bits | 𝕏-坐标数 |
|---|---|---|---:|---:|---:|
| \(\mathbb{X}^0\) | 太极 | Origin | 1 | 0 | 0 |
| \(\mathbb{X}^1\) | 象 / 𝕏 | Xiang / Core Image | 16 | 4 | 1 |
| \(\mathbb{X}^2\) | 对象 | Object / Paired Xiang | 256 | 8 | 2 |
| \(\mathbb{X}^3\) | 三象 / 复对象 | Triple Xiang | 4096 | 12 | 3 |
| \(\mathbb{X}^4\) | 四象场 | Quad Xiang Field | 65536 | 16 | 4 |
| \(\mathbb{X}^n\) | 𝕏ⁿ | n-fold Xiang | \(16^n\) | \(4n\) | \(n\) |

**规范句**：

\[
\boxed{对象 = \mathbb{X}^2 = 256\text{ 元}}
\]

---

## 2.3 旧容量表的降级

旧表：

\[
1,4,16,64,256
\]

不是 𝕏⁰–𝕏⁴ 的容量表。

它只是四基字集合 \(\mathsf{基字}\) 的幂容量：

\[
|\mathsf{基字}^0|,|\mathsf{基字}^1|,|\mathsf{基字}^2|,|\mathsf{基字}^3|,|\mathsf{基字}^4|
=1,4,16,64,256.
\]

这些结构可以作为 𝕏 内部编码、子结构、应用层 binding，但不得再称为 𝕏 tower。

特别地：

- 64 不是 \(\mathbb{X}^3\)，而是 \(\mathsf{基字}^3\) 或某种应用层 64-state 子结构。
- 256 可以同时等于 \(|\mathsf{基字}^4|\) 与 \(|\mathbb{X}^2|\)，但这只是 cardinality 相同，不代表二者结构等同。

---

# 3. 代数结构 · Algebraic Structures

## 3.1 Additive Abelian structure

作为 additive group：

\[
(\mathbb{X},+)\cong(\mathbb{Z}/2)^4.
\]

所以：

\[
(\mathbb{X}^n,+)\cong(\mathbb{Z}/2)^{4n}.
\]

性质：

1. Abelian：\(x+y=y+x\)
2. exponent 2：\(x+x=0\)
3. every element self-inverse：\(-x=x\)
4. finite elementary abelian 2-group

这是 dot product、Pontryagin duality、LIC、normalization 的基础。

---

## 3.2 Compositional operator structure

作为 endomorphism：

\[
\mathbb{X}\cong\mathrm{End}_{\mathbb{F}_2}(\mathbb{F}_2^2).
\]

复合运算为矩阵乘法：

\[
A\circ B = AB.
\]

此结构一般不交换。

可逆元构成：

\[
\mathbb{X}^{\times}=\mathrm{GL}(2,\mathbb{F}_2)\cong S_3.
\]

数量：

| Rank | 数量 | 说明 |
|---:|---:|---|
| 0 | 1 | 零映射 |
| 1 | 9 | 退化映射 / projection-like maps |
| 2 | 6 | 可逆映射，组成 \(\mathrm{GL}(2,\mathbb{F}_2)\cong S_3\) |

因此：

> 𝕏 的 additive 层是 Abelian；𝕏 的 operator 层含有 non-Abelian symmetry。

这是新版中非常重要的双层结构。

---

# 4. 代数完备性 · Algebraic Completeness

## 4.1 直和 / 直积

\[
\mathbb{X}^a\oplus\mathbb{X}^b\cong\mathbb{X}^{a+b}.
\]

容量：

\[
16^a\cdot16^b=16^{a+b}.
\]

---

## 4.2 Typed 子群与商

若 \(H\subset\mathbb{X}^n\) 是由完整 𝕏-坐标生成的 typed coordinate subgroup，且 \(H\cong\mathbb{X}^k\)，则：

\[
\mathbb{X}^n/H\cong\mathbb{X}^{n-k}.
\]

注意：任意 \(\mathbb{F}_2\)-子空间未必保 𝕏-coordinate typing。新版必须区分：

| 类型 | 是否保 𝕏-typing |
|---|---|
| 完整 𝕏-坐标子群 | ✓ |
| 任意 \(\mathbb{F}_2\)-子空间 | 不一定 |
| 四基字子结构 | 只作为内部 / 应用层 |

---

## 4.3 Pontryagin 自对偶

由于 \(\mathbb{X}^n\) 是有限 Abelian group：

\[
\widehat{\mathbb{X}^n}=\mathrm{Hom}(\mathbb{X}^n,S^1).
\]

又因为每个元素都是 2-torsion，character 的值落在 \(\{\pm1\}\)，所以：

\[
\widehat{\mathbb{X}^n}\cong\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{X}^n,\mathbb{F}_2)
\cong\mathbb{F}_2^{4n}
\cong\mathbb{X}^n.
\]

因此：

\[
\boxed{\widehat{\mathbb{X}^n}\cong\mathbb{X}^n}
\]

𝕏ⁿ 仍然是 Pontryagin self-dual，但维度从旧版 \(2n\) bit 改为新版 \(4n\) bit。

---

## 4.4 Hom 封闭

\[
\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{X}^a,\mathbb{X}^b)
\cong
\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{F}_2^{4a},\mathbb{F}_2^{4b}).
\]

其 \(\mathbb{F}_2\)-维数为：

\[
(4b)(4a)=16ab.
\]

因为一个 𝕏 有 4 bit，所以：

\[
\mathbb{F}_2^{16ab}\cong\mathbb{X}^{4ab}.
\]

因此：

\[
\boxed{\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{X}^a,\mathbb{X}^b)\cong\mathbb{X}^{4ab}}
\]

特别地：

\[
\mathrm{End}_{\mathbb{F}_2}(\mathbb{X})\cong\mathbb{X}^4.
\]

这修正旧版错误：

> \(\mathrm{End}(\mathbb{X})\) 不是 \(\mathbb{X}^2\)，而是 \(\mathbb{X}^4\)。

---

## 4.5 Tensor 封闭

\[
\mathbb{X}^a\otimes_{\mathbb{F}_2}\mathbb{X}^b
\cong
\mathbb{F}_2^{4a}\otimes\mathbb{F}_2^{4b}
\cong
\mathbb{F}_2^{16ab}
\cong
\mathbb{X}^{4ab}.
\]

所以：

\[
\boxed{\mathbb{X}^a\otimes\mathbb{X}^b\cong\mathbb{X}^{4ab}}
\]

---

## 4.6 新版闭合性主表

| 运算 | 新版指数律 | 说明 |
|---|---:|---|
| 直和 \(\oplus\) | \(a+b\) | interface joining |
| typed 子群 | \(k\le n\) | 仅完整 𝕏-coordinate |
| typed 商 | \(n-k\) | abstraction / projection |
| Pontryagin dual | \(n\) | self-duality |
| F₂-Hom | \(4ab\) | linear maps |
| F₂-tensor | \(4ab\) | state composition |
| End(𝕏) | 4 | \(\mathrm{End}(\mathbb{X})\cong\mathbb{X}^4\) |

---

# 5. Dot Product 与信息守恒 · Pairing and Information Preservation

## 5.1 𝕏 上的 Frobenius dot product

将：

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
B=\begin{pmatrix}e&f\\g&h\end{pmatrix}
\]

定义：

\[
\boxed{\langle A,B\rangle := ae+bf+cg+dh\in\mathbb{F}_2.}
\]

这就是 4-bit Frobenius pairing。

性质：

1. symmetric
2. \(\mathbb{F}_2\)-bilinear
3. non-degenerate
4. compatible with 𝕏-as-4-bit state

---

## 5.2 𝕏ⁿ 上的 dot product

对：

\[
U=(u^{(1)},\ldots,u^{(n)}),\quad V=(v^{(1)},\ldots,v^{(n)})\in\mathbb{X}^n,
\]

定义：

\[
\boxed{\langle U,V\rangle := \sum_{i=1}^n \langle u^{(i)},v^{(i)}\rangle_{\mathbb{X}}\in\mathbb{F}_2.}
\]

这给出：

\[
\mathbb{X}^n\xrightarrow{\sim}(\mathbb{X}^n)^*,\quad U\mapsto\langle U,-\rangle.
\]

---

## 5.3 信息守恒的新版含义

旧版中每个 𝕏-coordinate 有 2 bit；新版中每个 𝕏-coordinate 有 4 bit。

因此新版 LIC 为：

> **LIC**：给定 \(U\in\mathbb{X}^n\)，存在唯一 \(4n\)-bit 表示，并且该表示唯一分解为 \(n\) 个 𝕏-coordinate。

即：

\[
U=(u^{(1)},\ldots,u^{(n)}),\quad u^{(i)}\in\mathbb{X}.
\]

每个 \(u^{(i)}\) 可由该坐标内的 4 个 basis-pairing 独立恢复。

所以新版信息守恒仍分两层：

| Sense | 内容 |
|---|---|
| Sense 1: Linear losslessness | \(4n\) 个 basis pairing 可恢复 \(U\) |
| Sense 2: 𝕏-typed losslessness | 每个 𝕏-coordinate 独立恢复，不跨坐标混杂 |

---

# 6. 对象 · Object = 𝕏²

## 6.1 正确定义

\[
\boxed{对象 := \mathbb{X}^2}
\]

所以：

\[
|对象|=|\mathbb{X}|^2=16^2=256.
\]

对象不是旧版的 16 元层；对象是两个 𝕏-coordinate 组成的 256 元层。

---

## 6.2 对象的读法

若：

\[
O\in对象=\mathbb{X}^2,
\]

则：

\[
O=(x_1,x_2),\quad x_1,x_2\in\mathbb{X}.
\]

每个 \(x_i\) 自身是 16 元 𝕏。

因此对象含：

\[
4+4=8
\]

个 F₂ bits，总容量：

\[
2^8=256.
\]

---

## 6.3 对象不等于 End(𝕏)

新版必须明确：

\[
对象=\mathbb{X}^2
\]

但：

\[
\mathrm{End}_{\mathbb{F}_2}(\mathbb{X})\cong\mathbb{X}^4.
\]

所以：

\[
对象\ne\mathrm{End}(\mathbb{X}).
\]

更准确地：

| 结构 | 容量 | 𝕏 指数 |
|---|---:|---:|
| 𝕏 | 16 | 1 |
| 对象 = 𝕏² | 256 | 2 |
| End(𝕏) | 65536 | 4 |

对象可以作为 paired state / paired semantic atom；若要表达 𝕏 上的任意线性操作，需要 \(\mathbb{X}^4\)。

---

# 7. Hom Representation 新版

## 7.1 通用 Hom

\[
\mathrm{Hom}_{\mathbb{F}_2}(\mathbb{X}^n,\mathbb{X}^m)
\cong\mathbb{X}^{4mn}.
\]

作为矩阵，它是一个 \((4m)\times(4n)\) 的 \(\mathbb{F}_2\)-矩阵。

若按 𝕏-block 组织，每个 block 是一个 \(4\times4\) binary matrix，即 \(16\) bit，即 \(\mathbb{X}^4\)。

因此 surface 表示应为：

\[
\boxed{\mathrm{Hom}(\mathbb{X}^n,\mathbb{X}^m)
\cong
\mathrm{Mat}_{m\times n}(\mathbb{X}^4).}
\]

旧版写成 \(\mathrm{Mat}_{m\times n}(对象)\) 不再正确，因为对象只有 \(\mathbb{X}^2\)，不足以表示一个 \(4\times4\) block。

---

## 7.2 三类 operation type

新版应区分：

| 类型 | 数学 | 容量 | 用途 |
|---|---|---:|---|
| 基础 𝕏-op | \(\mathbb{X}=\mathrm{End}(\mathsf{基字})\) | 16 | 操作四基字 |
| 对象 | \(\mathbb{X}^2\) | 256 | paired 𝕏 state |
| 𝕏-endomorphism | \(\mathrm{End}(\mathbb{X})\cong\mathbb{X}^4\) | 65536 | 操作 𝕏 本身 |

这防止旧版中的 state/op 混淆。

---

# 8. 四基字子结构与外部传统 · Internal Four-Base Layer and External Bindings

## 8.1 旧 4/64/256 结构的正确地位

`道/错/综/错综` 仍可形成四基字结构：

\[
\mathsf{基字}\cong\mathbb{F}_2^2.
\]

其幂有容量：

\[
1,4,16,64,256,\ldots
\]

但这不是 𝕏 tower。

它可以作为：

1. 𝕏 的内部编码层；
2. 某些子结构；
3. 易经 / Pauli / Boolean 等 external binding 的应用层；
4. Lean/Clojure 中的辅助 primitive。

---

## 8.2 易经 64 与 𝕏 的关系

若保留 64-state 八卦/六十四卦解释，则它应属于：

\[
\mathsf{基字}^3
\]

或某个应用层 binding，而不是：

\[
\mathbb{X}^3.
\]

因为新版：

\[
|\mathbb{X}^3|=4096.
\]

所以对外表述必须改为：

> 易学 64 结构是 𝕏 内部四基字层的三重结构，或应用层 binding，不是 𝕏³。

---

## 8.3 256 的双重出现

256 可以来自两个不同结构：

\[
|\mathsf{基字}^4|=4^4=256
\]

也可以来自：

\[
|\mathbb{X}^2|=16^2=256.
\]

二者 cardinality 相同，但结构不同。

新版应把 **对象** 专门留给：

\[
\boxed{对象=\mathbb{X}^2.}
\]

若讨论 \(\mathsf{基字}^4\)，应称为“四基字四重结构”或应用层时态结构，不应称为 𝕏² 对象，除非给出明确 equivalence / encoding。

---

# 9. Type Checker 新规则

```text
Rule 1: 𝕏 是 16 元基类型；不得把 {道,错,综,错综} 称为 𝕏。
Rule 2: 𝕏ⁿ 的容量为 16ⁿ，F₂-bit 数为 4n。
Rule 3: 对象 = 𝕏² = 256 元。
Rule 4: dot : 𝕏ⁿ × 𝕏ⁿ → 𝔽₂，n 必须相同。
Rule 5: surface type 若写 𝕏ⁿ，必须保持完整 𝕏-coordinate，不得暴露半个 𝕏。
Rule 6: 四基字 {道,错,综,错综} 只可作为内部编码层 / 应用层 binding，不作为 𝕏 tower。
Rule 7: Hom(𝕏ⁿ,𝕏ᵐ) 的标准 block 表示为 Mat_{m×n}(𝕏⁴)。
Rule 8: End(𝕏)=𝕏⁴；不得再写 End(𝕏)=𝕏²。
Rule 9: 𝕏 的加法层 Abelian；𝕏 的复合层可 non-Abelian。两种运算必须在语法上区分。
Rule 10: 64-state 传统对应属于四基字层或 application binding，不是 𝕏³。
```

---

# 10. Lean 4 骨架修订

```lean
import Mathlib.Data.Matrix.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.LinearAlgebra.Basic

namespace 文

/-- 四基字：不是 𝕏，只是 𝕏 内部编码层 -/
inductive 基字 where
  | 道
  | 错
  | 综
  | 错综
  deriving DecidableEq, Repr, Fintype

namespace 基字

/-- 基字 ≃ F₂² 的语义性占位。实际证明中可用 Fin 2 → Bool。 -/
def toBits : 基字 → Bool × Bool
  | 道 => (false, false)
  | 错 => (true, false)
  | 综 => (false, true)
  | 错综 => (true, true)

end 基字

/-- 𝕏 = 16 元基类型 = 2×2 Bool matrix = F₂⁴ -/
structure 𝕏 where
  m00 : Bool
  m01 : Bool
  m10 : Bool
  m11 : Bool
  deriving DecidableEq, Repr

namespace 𝕏

/-- additive XOR structure placeholder -/
def add (A B : 𝕏) : 𝕏 :=
  ⟨Bool.xor A.m00 B.m00,
   Bool.xor A.m01 B.m01,
   Bool.xor A.m10 B.m10,
   Bool.xor A.m11 B.m11⟩

/-- Frobenius dot product on 𝕏 = F₂⁴ -/
def dot (A B : 𝕏) : Bool :=
  Bool.xor
    (Bool.xor (A.m00 && B.m00) (A.m01 && B.m01))
    (Bool.xor (A.m10 && B.m10) (A.m11 && B.m11))

/-- Matrix composition layer; distinct from additive structure. -/
def comp (A B : 𝕏) : 𝕏 :=
  let c00 := Bool.xor (A.m00 && B.m00) (A.m01 && B.m10)
  let c01 := Bool.xor (A.m00 && B.m01) (A.m01 && B.m11)
  let c10 := Bool.xor (A.m10 && B.m00) (A.m11 && B.m10)
  let c11 := Bool.xor (A.m10 && B.m01) (A.m11 && B.m11)
  ⟨c00,c01,c10,c11⟩

end 𝕏

/-- 𝕏ⁿ = n-fold product of 16-state 𝕏 -/
def 𝕏n (n : ℕ) : Type := Fin n → 𝕏

namespace 𝕏n

/-- dot on 𝕏ⁿ = sum of coordinate dot products -/
def dot {n : ℕ} (U V : 𝕏n n) : Bool :=
  (Finset.univ : Finset (Fin n)).foldr
    (fun i acc => Bool.xor (𝕏.dot (U i) (V i)) acc) false

end 𝕏n

/-- Interface aliases -/
abbrev 太极 : Type := 𝕏n 0      -- 1 元
abbrev 象   : Type := 𝕏n 1      -- 16 元
abbrev 对象 : Type := 𝕏n 2      -- 256 元

/-- End(𝕏) = 𝕏⁴ as F₂-linear map space, not 𝕏². -/
abbrev End𝕏 : Type := 𝕏n 4

end 文
```

---

# 11. Clojure / compiler IR 修订

```clojure
(ns wen.algebra.v05
  "文 代数 v0.5 · 𝕏 = 16 元基类型")

;; 四基字：内部编码层，不是 𝕏
(def base-words #{:dao :cuo :zong :cuozong})

(def base-word->bits
  {:dao     [0 0]
   :cuo     [1 0]
   :zong    [0 1]
   :cuozong [1 1]})

;; 𝕏 = 16 元 = 2×2 F₂ matrix = 4 bits
;; Represented as [m00 m01 m10 m11]
(defn x? [x]
  (and (vector? x)
       (= 4 (count x))
       (every? #{0 1} x)))

(defn x-add [a b]
  {:pre [(x? a) (x? b)]}
  (vec (map bit-xor a b)))

(defn x-dot [[a b c d] [e f g h]]
  (bit-xor (bit-xor (bit-and a e) (bit-and b f))
           (bit-xor (bit-and c g) (bit-and d h))))

(defn x-comp [[a b c d] [e f g h]]
  ;; matrix multiplication over F₂
  [(bit-xor (bit-and a e) (bit-and b g))
   (bit-xor (bit-and a f) (bit-and b h))
   (bit-xor (bit-and c e) (bit-and d g))
   (bit-xor (bit-and c f) (bit-and d h))])

;; 𝕏ⁿ = vector of n x-elements
(defn xn? [U]
  (and (vector? U) (every? x? U)))

(defn xn-arity [U] (count U))

(defn xn-dot [U V]
  {:pre [(xn? U) (xn? V) (= (count U) (count V))]}
  (reduce bit-xor 0 (map x-dot U V)))

;; Object = 𝕏² = 256 states
(defn object? [O]
  (and (xn? O) (= 2 (count O))))

;; End(𝕏) = 𝕏⁴, not 𝕏²
(defn end-x? [E]
  (and (xn? E) (= 4 (count E))))

(defn capacity-xn [n]
  ;; |𝕏ⁿ| = 16^n
  (bigint (Math/pow 16 n)))
```

---

# 12. v0.4 → v0.5 Migration Checklist

| v0.4 旧说法 | v0.5 新说法 |
|---|---|
| \(\mathbb{X}=\{道,错,综,错综\}\) | \(\mathbb{X}\) 是 16 元；四字只是内部基字 |
| \(\mathbb{X}\cong V_4\) | \(\mathbb{X}\cong\mathbb{F}_2^4\cong\mathrm{Mat}_2(\mathbb{F}_2)\) |
| \(\mathbb{X}^n\cong\mathbb{F}_2^{2n}\) | \(\mathbb{X}^n\cong\mathbb{F}_2^{4n}\) |
| 容量 \(1,4,16,64,256\) | 容量 \(1,16,256,4096,65536\) |
| 对象 = \(\mathbb{X}^2=16\) | 对象 = \(\mathbb{X}^2=256\) |
| End(𝕏)=对象 | End(𝕏)=\(\mathbb{X}^4\) |
| Hom(𝕏ⁿ,𝕏ᵐ)=Mat(对象) | Hom(𝕏ⁿ,𝕏ᵐ)=Mat(\(\mathbb{X}^4\)) |
| LIC = \(2n\) bits | LIC = \(4n\) bits |
| 64 = 𝕏³ | 64 = 四基字³ / application binding |
| 256 = 𝕏⁴ | 256 = 𝕏²；也可等于四基字⁴但结构不同 |

---

# 13. 完成度自检

| 项目 | v0.5 状态 |
|---|---|
| 唯一 𝕏 符号 | ✓ |
| 𝕏=16 元 | ✓ |
| 四基字降级为内部编码层 | ✓ |
| 对象=𝕏²=256 | ✓ |
| 容量表修正 | ✓ |
| Abelian additive layer | ✓ |
| non-Abelian composition layer | ✓ |
| Pontryagin self-duality 保留 | ✓ |
| dot product 改为 4-bit Frobenius pairing | ✓ |
| LIC 改为 4n bits | ✓ |
| Hom 指数律改为 4ab | ✓ |
| End(𝕏)=𝕏⁴ | ✓ |
| 64/256 外部传统位置重排 | ✓ |
| Type checker 新规则 | ✓ |
| Lean skeleton 更新 | ✓ |
| Clojure skeleton 更新 | ✓ |

---

# 14. 仍需决定的问题

1. 𝕏 的 16 个元素是否需要逐一命名？
2. 对象 \(\mathbb{X}^2\) 的 256 元是否需要 surface 命名，还是只用复合表示？
3. 四基字层是否允许 surface 暴露？若允许，应如何避免用户误认为它是 𝕏？
4. 64-state 易学结构在新版中应放入哪一个 application note？
5. 𝕏 的 composition layer 是否升为 surface syntax，还是只在 op mode 中使用？
6. Hom(𝕏ⁿ,𝕏ᵐ)=Mat(𝕏⁴) 是否太重？是否需要特殊压缩表示？
7. 是否将 \(\mathbb{X}=\mathrm{End}(\mathsf{基字})\) 作为唯一正式定义，而把 \(\mathbb{F}_2^4\) 作为实现视角？

---

*End of v0.5 · 𝕏=16 校正版*  
*The Xiang Algebra · 16-State Core Type Revision*
