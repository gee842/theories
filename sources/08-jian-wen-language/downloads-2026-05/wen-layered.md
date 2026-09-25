# 文 · 离散-连续分层架构

> **摘要**　本文给出 $V_n$ 形式系统的分层架构，将经典离散实现（见 `wen-formal.md` §1-§10）与量子连续实现统一在一个抽象骨架下。具体地：(1) 抽出位置代数 Layer 0 作为两实现共用底；(2) 形式化量子 Hilbert 空间实现 Layer 2，包含道-投影、Pauli 翻转、偏迹、Born 测量；(3) 证明经典-量子相容性桥接定理 **C1–C5**，建立"经典 = 量子在计算基限制下的特例"；(4) 给出 $V_{2n}$ 自相似分解在两层的对应——$\oplus$（直和）与 $\otimes$（张量积）在位数索引上同构；(5) 推广 `wen-formal.md` §9 塌缩不可逆性到偏迹意义下的量子定理 **9.1.1q**；(6) 给出 Lean 4 typeclass 抽象骨架与实施路线图。

---

## §1 引言

### 1.1 动机

`wen-formal.md` 给出了完整的经典道-代数：$V_n = \mathbb{F}_2^n$ 上的位翻转、道-集闭包、$k$-核稳定层、四值模态分类、塌缩不可逆性。这个系统是离散组合的，可在 Lean 4 中用纯有限集合论形式化。

但讨论已显示三处经典框架的能力上限：

1. **Belnap B（信息相干）与 N（信息空缺）的区分**需要相位/振幅结构，纯经典不能给。
2. **道-真值在连续意义下的"时位"维度**——干涉相长相消——需要振幅，不能由概率刻画。
3. **跨层操作的"开 gate"动作**在量子里有更精细的对应（部分测量、弱测量、纠缠 swap）。

走量子路线**不意味放弃经典**——经典是量子在计算基上的剖面。本文给出形式上把两者并存的架构。

### 1.2 范围

本文添加以下内容：

- **Layer 0**（位置代数）：经典量子共用的索引与分解结构。
- **Layer 2**（量子实现）：$(\mathbb{C}^2)^{\otimes n}$ 上的道-投影、Pauli 翻转、偏迹、Born 测量。
- **Layer 3**（桥接）：经典 $\hookrightarrow$ 量子的嵌入与相容性定理 C1–C5。
- 跨层级自相似性在量子下的对应（张量积自相似）。

经典部分（Layer 1）请参考 `wen-formal.md`，本文不重复推导。

### 1.3 总览

```
                          文 (Wen)
                            │
        ┌───────────────────┼───────────────────┐
        │              Layer 0                  │
        │       Slot, 偶倍分解索引              │
        │       （纯组合，无状态语义）          │
        │                                       │
   Layer 1 (经典/离散)                  Layer 2 (量子/连续)
   V_n = 𝔽₂ⁿ                            ℋ_n = (ℂ²)^⊗n
   𝒟_n ⊆ V_n（子集）                     𝒟_n^q ⊆ ℋ_n（子空间）
   σ_j 翻转                              X_j Pauli
   |𝒟_n| 计数判定                        Π_𝒟 投影 / Born 概率
   M ∈ {□真, □假, C, ⊠}                  p_𝒟 ∈ [0,1] + 相干度 + ⊠
        │                                       │
        └─────────── Layer 3 ───────────────────┘
                     桥接
            ι : V_n ↪ ℋ_n     （基嵌入）
            meas : ℋ_n → Δ(V_n)（Born）
            相容性定理 C1–C5
```

---

## §2 Layer 0: 位置代数

### 2.1 槽位与偶倍分解

**定义 2.1.1**（槽位）　$\mathrm{Slot}\,n := \{\,1, 2, \ldots, n\,\}$，作为位置索引的 $n$ 元有限集。

**定义 2.1.2**（外/内层分裂）　对偶数 $2n$，标准分裂

$$
\mathrm{split} : \mathrm{Slot}\,(2n) \longrightarrow \mathrm{Slot}\,n \sqcup \mathrm{Slot}\,n
$$

由

$$
\mathrm{split}(j) := 
\begin{cases}
\mathrm{inl}(j) & \text{若 } 1 \leq j \leq n, \\
\mathrm{inr}(j - n) & \text{若 } n + 1 \leq j \leq 2n.
\end{cases}
$$

外层槽集 $\mathrm{Slot}_\text{外} := \{\,1, \ldots, n\,\}$，内层槽集 $\mathrm{Slot}_\text{内} := \{\,n+1, \ldots, 2n\,\}$。

### 2.2 抽象状态空间接口

Layer 0 的核心抽象是把两个 backend 的共用结构提取为一个接口：

```lean
class StateSpace (S : ℕ → Type) where
  -- 自相似分解
  outer    : S (2*n) → S n
  inner    : S (2*n) → S n
  combine  : S n → S n → S (2*n)

  -- 翻转算子族
  flip_outer : Fin n → S (2*n) → S (2*n)
  flip_inner : Fin n → S (2*n) → S (2*n)

  -- 道-评估与可观测性
  truth         : S n → TruthValue
  is_observable : S (2*n) → Prop
```

`TruthValue` 是 backend 参数化的：经典版为 `Bool`，量子版为 `[0, 1] × CoherenceInfo`。

**公理 2.2.1**（自相似性）　任意 `StateSpace` 实例 $S$ 满足

$$
S\,(2n) \;\cong\; S\,n \times S\,n.
$$

经典：$\cong$ 是集合双射，细化为 $\mathbb{F}_2$-向量空间直和 $\oplus$。
量子：$\cong$ 是 Hilbert 空间同构，细化为张量积 $\otimes$。

两者都满足"位数加倍 = 两半合并"的抽象规律。

---

## §3 Layer 1: 离散态空间（经典）

完整内容见 `wen-formal.md` §1–§10。此处只列接口对应：

| `StateSpace` 接口 | 经典实现（`wen-formal.md` 对应处） |
|---|---|
| `S n := ClassicalV n` | $V_n = \mathbb{F}_2^n$（§1.1） |
| `combine(o, i)` | $(o\,;\,i) \in V_{2n}$（定理 2.1.1） |
| `outer(v) := π_外(v)` | §2.2 |
| `inner(v) := π_内(v)` | §2.2 |
| `flip_outer(j, v) := σ_j^外(v)` | §4.2 |
| `flip_inner(j, v) := σ_j^内(v)` | §4.2 |
| `truth(v) := [v ∈ 𝒟_n]` | §1.2, §3.2 |
| `is_observable(v) := π_外(v) ∈ 𝒟_n^外` | §7.1.1 |

经典模态分类 $\{\Box\text{真}, \Box\text{假}, \mathbf{C}, \boxtimes\}$ 按 `wen-formal.md` 定理 7.4.1。

---

## §4 Layer 2: 连续态空间（量子）

### 4.1 量子爻空间

**定义 4.1.1**（量子爻空间）

$$
\mathcal{H}_n \;:=\; (\mathbb{C}^2)^{\otimes n}
$$

是 $2^n$ 维复 Hilbert 空间。**计算基**为

$$
\bigl\{\, |v\rangle = |v_1\rangle \otimes |v_2\rangle \otimes \cdots \otimes |v_n\rangle \;:\; v \in \mathbb{F}_2^n \,\bigr\},
$$

即 $n$ 个 qubit 的张量积态构成的正交归一基。

**定义 4.1.2**（量子态空间）

- **纯态**：$\mathrm{QuantumV}_\text{pure}\,n := \bigl\{\, |\psi\rangle \in \mathcal{H}_n : \langle\psi|\psi\rangle = 1 \,\bigr\} / \sim$（同相位等价）
- **混态**：$\mathrm{QuantumV}_\text{mixed}\,n := \mathcal{D}(\mathcal{H}_n) := \bigl\{\, \rho : \rho \geq 0,\, \mathrm{Tr}(\rho) = 1 \,\bigr\}$

混态包含纯态：$|\psi\rangle \leftrightarrow |\psi\rangle\langle\psi|$。后续除非另注，统一用混态 $\rho$ 表述。

### 4.2 量子道-子空间

**定义 4.2.1**（量子道-子空间）　给定经典道-集 $\mathcal{D}_n^\text{cl} \subseteq V_n$，对应量子道-子空间

$$
\mathcal{D}_n^q \;:=\; \mathrm{span}_\mathbb{C}\bigl\{\, |v\rangle \;:\; v \in \mathcal{D}_n^\text{cl} \,\bigr\}.
$$

对应**道-投影算子**

$$
\Pi_\mathcal{D} \;:=\; \sum_{v \in \mathcal{D}_n^\text{cl}} |v\rangle\langle v|.
$$

**命题 4.2.2**　$\Pi_\mathcal{D}$ 是正交投影：$\Pi_\mathcal{D}^\dagger = \Pi_\mathcal{D},\; \Pi_\mathcal{D}^2 = \Pi_\mathcal{D}$。

**证明**　计算基的正交归一性：$\langle u|v\rangle = \delta_{uv}$。直接验证。$\blacksquare$

### 4.3 量子位翻转

**定义 4.3.1**（Pauli X）　$X := \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$。

**定义 4.3.2**（第 $j$ 位 Pauli 翻转）　对 $j \in \{1, \ldots, n\}$：

$$
X_j \;:=\; I_{2^{j-1}} \otimes X \otimes I_{2^{n-j}}.
$$

即 $X$ 作用于第 $j$ 个张量因子，其余因子保持不变。

外层翻转 $X_j^\text{外} := X_j$（$j \in \{1, \ldots, n\}$）。
内层翻转 $X_j^\text{内} := X_{j+n}$（$j \in \{1, \ldots, n\}$）。

**命题 4.3.3**　$X_j^\dagger = X_j$，$X_j^2 = I$。即 $X_j$ 是幺正自伴对合。

### 4.4 偏迹与可观测域

**定义 4.4.1**（偏迹）　对 $\rho \in \mathcal{D}(\mathcal{H}_{2n}) = \mathcal{D}(\mathcal{H}_n^\text{外} \otimes \mathcal{H}_n^\text{内})$，**外层偏迹**

$$
\mathrm{Tr}_\text{外}(\rho) \;:=\; \sum_{v \in V_n^\text{外}} (\langle v|_\text{外} \otimes I_\text{内})\, \rho\, (|v\rangle_\text{外} \otimes I_\text{内})\;\in\; \mathcal{D}(\mathcal{H}_n^\text{内}).
$$

直观：把外层"积分掉"，得到内层的约化态。

**定义 4.4.2**（外层道-投影）　$\Pi_\mathcal{D}^\text{外} := \Pi_\mathcal{D} \otimes I_\text{内}$。

**定义 4.4.3**（量子可观测域）

$$
\mathcal{O}_{2n}^q \;:=\; \bigl\{\, \rho \in \mathcal{D}(\mathcal{H}_{2n}) \;:\; \mathrm{Tr}_\text{外}(\Pi_\mathcal{D}^\text{外}\,\rho) \neq 0 \,\bigr\}.
$$

**定义 4.4.4**（量子塌缩区）

$$
\boxtimes^q \;:=\; \bigl\{\, \rho \;:\; \mathrm{Tr}_\text{外}(\Pi_\mathcal{D}^\text{外}\,\rho) = 0 \,\bigr\} \;=\; \mathcal{D}(\mathcal{H}_{2n}) \setminus \mathcal{O}_{2n}^q.
$$

"$=0$"指内层算子等于零算子。

### 4.5 量子道-评估

**定义 4.5.1**（道-概率）　

$$
p_\mathcal{D}(\rho) \;:=\; \mathrm{Tr}(\Pi_\mathcal{D}\,\rho) \;\in\; [0, 1].
$$

对纯态 $|\psi\rangle$：$p_\mathcal{D}(|\psi\rangle) = \langle\psi|\Pi_\mathcal{D}|\psi\rangle$。

由 Born 规则，$p_\mathcal{D}(\rho)$ 是"在计算基测量后落入道-集的概率"。

### 4.6 相干度与 B / N 分离

**定义 4.6.1**（相干度）　对 $\rho \in \mathcal{D}(\mathcal{H}_n)$，**相干度**

$$
C(\rho) \;:=\; \sum_{u \neq v} \bigl|\langle u|\rho|v\rangle\bigr|.
$$

即密度阵在计算基下非对角元绝对值之和。

**命题 4.6.2**　经典态（计算基纯态或它们的经典概率混合）满足 $C(\rho) = 0$；量子相干态 $C(\rho) > 0$。

### 4.7 量子四值模态分类

固定可达关系 $R^q \subseteq \mathcal{D}(\mathcal{H}_{2n}) \times \mathcal{D}(\mathcal{H}_{2n})$（例如"$\leq r$ 步单 qubit 幺正操作可达"或"Bures 距离 $\leq \varepsilon$"）。

对 $\rho \in \mathcal{O}_{2n}^q$：

$$
\begin{aligned}
\rho \models \Box\text{真}_q \;&:\Leftrightarrow\; \forall\,\rho',\; R^q(\rho, \rho') \Rightarrow p_\mathcal{D}(\rho') = 1, \\
\rho \models \Box\text{假}_q \;&:\Leftrightarrow\; \forall\,\rho',\; R^q(\rho, \rho') \Rightarrow p_\mathcal{D}(\rho') = 0, \\
\rho \models \mathbf{B} \;&:\Leftrightarrow\; 0 < p_\mathcal{D}(\rho) < 1 \,\land\, C(\rho) > 0, \\
\rho \models \mathbf{N} \;&:\Leftrightarrow\; 0 < p_\mathcal{D}(\rho) < 1 \,\land\, C(\rho) = 0.
\end{aligned}
$$

**定理 4.7.1**（量子五分划）　$\mathcal{D}(\mathcal{H}_{2n})$ 被划分为五类

$$
\mathcal{D}(\mathcal{H}_{2n}) \;=\; \mathbf{N}_\text{真}^q \;\sqcup\; \mathbf{N}_\text{假}^q \;\sqcup\; \mathbf{B} \;\sqcup\; \mathbf{N} \;\sqcup\; \boxtimes^q.
$$

注意经典四值的 $\mathbf{C}$ 类在量子里被进一步细分为 $\mathbf{B}$（相干）与 $\mathbf{N}$（去相干）。

**证明**　$\boxtimes^q$ 与 $\mathcal{O}_{2n}^q$ 互补（定义 4.4.4）。在 $\mathcal{O}_{2n}^q$ 内由 $p_\mathcal{D}$ 的取值（$= 0, 0 < \cdot < 1, = 1$）与稳定/相干性进一步划分。$\blacksquare$

---

## §5 Layer 3: 桥接定理

这是本文核心新增内容。五条相容性定理 C1–C5 建立"经典 = 量子在计算基限制下的特例"。

### 5.1 嵌入与测量

**定义 5.1.1**（基嵌入）

$$
\iota : \mathrm{ClassicalV}\,n \longrightarrow \mathcal{D}(\mathcal{H}_n), \quad v \;\longmapsto\; |v\rangle\langle v|.
$$

即把经典态 $v$ 嵌入为对应计算基的纯态密度阵。

**定义 5.1.2**（Born 测量）　对 $\rho \in \mathcal{D}(\mathcal{H}_n)$：

$$
\mathrm{meas}(\rho) : \mathrm{ClassicalV}\,n \to [0, 1], \quad v \;\longmapsto\; \langle v|\rho|v\rangle.
$$

$\mathrm{meas}(\rho)$ 是 $\mathrm{ClassicalV}\,n$ 上的概率分布（Born 规则）。

### 5.2 五条相容性定理

**定理 C1**（投影-指示一致性）　对任意 $v \in \mathrm{ClassicalV}\,n$：

$$
\Pi_\mathcal{D}\,|v\rangle \;=\; [\![v \in \mathcal{D}_n^\text{cl}]\!] \cdot |v\rangle,
$$

其中 $[\![\cdot]\!]$ 是 Iverson 括号（条件成立则取 1，否则 0）。

**证明**

$$
\Pi_\mathcal{D}\,|v\rangle = \sum_{u \in \mathcal{D}_n^\text{cl}}|u\rangle\langle u|v\rangle = \sum_{u \in \mathcal{D}_n^\text{cl}} \delta_{uv}\,|u\rangle = \begin{cases} |v\rangle & \text{若 } v \in \mathcal{D}_n^\text{cl}, \\ 0 & \text{否则.} \end{cases}
$$

$\blacksquare$

---

**定理 C2**（Pauli-Flip 一致性）　对任意 $v \in \mathrm{ClassicalV}\,n$ 与 $j \in \{1, \ldots, n\}$：

$$
X_j\,|v\rangle \;=\; |\sigma_j(v)\rangle \;=\; |v + e_j\rangle.
$$

**证明**　$X$ 在单 qubit 上作 $X|b\rangle = |b \oplus 1\rangle$（$\mathbb{F}_2$ 加法）。$X_j$ 只作用于第 $j$ 张量因子：

$$
X_j\,|v_1 \cdots v_j \cdots v_n\rangle = |v_1 \cdots (v_j \oplus 1) \cdots v_n\rangle = |v + e_j\rangle = |\sigma_j(v)\rangle. \quad\blacksquare
$$

---

**定理 C3**（道-集嵌入一致性）

$$
\iota(\mathcal{D}_n^\text{cl}) \;=\; \mathcal{D}_n^q \cap \iota(\mathrm{ClassicalV}\,n).
$$

即量子道-子空间与"经典态嵌入像"的交恰好是经典道-集的嵌入像。

**证明**

($\subseteq$)　$\iota(\mathcal{D}_n^\text{cl}) = \{\,|v\rangle\langle v| : v \in \mathcal{D}_n^\text{cl}\,\}$。由定义 4.2.1，每个 $|v\rangle$（$v \in \mathcal{D}_n^\text{cl}$）落在 $\mathcal{D}_n^q$ 内，故 $|v\rangle\langle v|$ 是 $\mathcal{D}_n^q$ 上的态。

($\supseteq$)　设 $\rho = |v\rangle\langle v| \in \iota(\mathrm{ClassicalV}\,n)$ 且 $\rho$ 支持在 $\mathcal{D}_n^q$ 内（即 $\Pi_\mathcal{D}\,|v\rangle = |v\rangle$）。由 C1，$\Pi_\mathcal{D}\,|v\rangle = |v\rangle$ $\Leftrightarrow$ $v \in \mathcal{D}_n^\text{cl}$。故 $\rho \in \iota(\mathcal{D}_n^\text{cl})$。$\blacksquare$

---

**定理 C4**（道-评估一致性）　对 $v \in \mathrm{ClassicalV}\,n$：

$$
p_\mathcal{D}\bigl(\iota(v)\bigr) \;=\; [\![v \in \mathcal{D}_n^\text{cl}]\!].
$$

**证明**　

$$
p_\mathcal{D}(|v\rangle\langle v|) = \mathrm{Tr}(\Pi_\mathcal{D}\,|v\rangle\langle v|) = \langle v|\Pi_\mathcal{D}|v\rangle \stackrel{C1}{=} [\![v \in \mathcal{D}_n^\text{cl}]\!] \cdot \langle v|v\rangle = [\![v \in \mathcal{D}_n^\text{cl}]\!]. \quad\blacksquare
$$

---

**定理 C5**（塌缩区一致性）　对 $v \in \mathrm{ClassicalV}\,(2n)$：

$$
\iota(v) \in \boxtimes^q \;\iff\; v \in \boxtimes^\text{cl}.
$$

**证明**　记 $v = (o\,;\,i)$，则 $\iota(v) = |v\rangle\langle v| = (|o\rangle\langle o|) \otimes (|i\rangle\langle i|)$。

$$
\Pi_\mathcal{D}^\text{外}\,\iota(v) = (\Pi_\mathcal{D}\,|o\rangle\langle o|) \otimes (|i\rangle\langle i|) \stackrel{C1}{=} [\![o \in \mathcal{D}_n^\text{外}]\!] \cdot (|o\rangle\langle o|) \otimes (|i\rangle\langle i|).
$$

取偏迹（使用乘积态的偏迹公式 $\mathrm{Tr}_\text{外}(A \otimes B) = \mathrm{Tr}(A) \cdot B$）：

$$
\mathrm{Tr}_\text{外}\bigl(\Pi_\mathcal{D}^\text{外}\,\iota(v)\bigr) = [\![o \in \mathcal{D}_n^\text{外}]\!] \cdot \mathrm{Tr}(|o\rangle\langle o|) \cdot |i\rangle\langle i| = [\![o \in \mathcal{D}_n^\text{外}]\!] \cdot |i\rangle\langle i|.
$$

由于 $|i\rangle\langle i| \neq 0$，该算子为零 $\iff$ $[\![o \in \mathcal{D}_n^\text{外}]\!] = 0$ $\iff$ $o \notin \mathcal{D}_n^\text{外}$ $\iff$ $v \in \boxtimes^\text{cl}$（`wen-formal.md` 定义 7.2.1）。$\blacksquare$

### 5.3 模态分类的桥接

**定理 5.3.1**（计算基上的模态等价）　设 $R^\text{cl}$ 为汉明距离 $\leq r$ 关系（`wen-formal.md` §7.3），$R^q$ 为"$\leq r$ 步 Pauli X 操作可达"关系。则对任意 $v \in \mathrm{ClassicalV}\,(2n)$：

$$
M^\text{cl}(v) \;=\; M^q\bigl(\iota(v)\bigr)
$$

其中模态类对应：
- $\Box\text{真}^\text{cl} \;\leftrightarrow\; \Box\text{真}^q$
- $\Box\text{假}^\text{cl} \;\leftrightarrow\; \Box\text{假}^q$
- $\mathbf{C}^\text{cl} \;\leftrightarrow\; \mathbf{N}$（不到 $\mathbf{B}$，因 Pauli X 保计算基）
- $\boxtimes^\text{cl} \;\leftrightarrow\; \boxtimes^q$

**证明**

由 C2，$R^q$ 限制到计算基纯态恰为 $R^\text{cl}$（每一步 Pauli X 等价于经典翻转）。

由 C4，$p_\mathcal{D}$ 限制到计算基纯态取值 $\{0, 1\}$，故"邻域全在/全不在"判定与经典完全一致：

- 经典 $\Box\text{真}$：$\forall u, d_H(v, u) \leq r \Rightarrow u \in \mathcal{D}$ $\iff$ 量子 $\Box\text{真}$ 由 C4。
- 经典 $\mathbf{C}$：邻域跨界。计算基纯态相干度为零，故落入 $\mathbf{N}$ 子类。
- 经典 $\boxtimes$：由 C5。

$\blacksquare$

**推论 5.3.2**（量子专属：$\mathbf{B}$ 类）　$\mathbf{B}$ 子类 $\{|\psi\rangle : 0 < p_\mathcal{D} < 1,\, C > 0\}$ 在 $\iota(\mathrm{ClassicalV}\,n)$ 之外。这是量子结构相对于经典的**新生**，对应 Belnap "both" 的物理实现。

---

## §6 跨层级自相似性

### 6.1 自相似分解在两层的对应

**定理 6.1.1**（双 backend 自相似性）

- **经典**：$V_{2n} \cong_{\mathbb{F}_2\text{-Vec}} V_n \oplus V_n$（`wen-formal.md` 定理 2.1.1）
- **量子**：$\mathcal{H}_{2n} \cong_\text{Hilb} \mathcal{H}_n \otimes \mathcal{H}_n$

两者作为"位数加倍"的代数表达**在索引层面同构**：

$$
\dim_{\mathbb{F}_2}(V_n \oplus V_n) = n + n = 2n = \dim_{\mathbb{F}_2}(V_{2n}),
$$

$$
\dim_\mathbb{C}(\mathcal{H}_n \otimes \mathcal{H}_n) = 2^n \cdot 2^n = 2^{2n} = \dim_\mathbb{C}(\mathcal{H}_{2n}).
$$

代数操作不同（$\oplus$ vs $\otimes$），但 qubit 数量加法律一致：$n + n = 2n$。

### 6.2 嵌入保自相似分解

**定理 6.2.1**　对 $v = (o\,;\,i) \in V_{2n}$：

$$
\iota(v) \;=\; \iota(o) \otimes \iota(i).
$$

即基嵌入 $\iota$ 把经典直和分解翻译为量子张量分解。

**证明**　

$$
|v\rangle = |v_1, \ldots, v_{2n}\rangle = |v_1, \ldots, v_n\rangle \otimes |v_{n+1}, \ldots, v_{2n}\rangle = |o\rangle \otimes |i\rangle.
$$

故 $|v\rangle\langle v| = (|o\rangle\langle o|) \otimes (|i\rangle\langle i|) = \iota(o) \otimes \iota(i)$。$\blacksquare$

**深层原因**　经典 $\mathbb{F}_2$ 上每位是独立加性的（直和），量子 $\mathbb{C}^2$ 上每 qubit 是独立 tensor factor。两者在"独立位/qubit 数加法"这一抽象层等价，但具体代数运算不同。

### 6.3 跨层级量子化

**定义 6.3.1**（量子道-依赖族）

- 外层道-子空间 $\mathcal{D}_n^{q,\text{外}} \subseteq \mathcal{H}_n^\text{外}$，投影 $\Pi^\text{外} = \sum_{o \in \mathcal{D}_n^{\text{cl,外}}} |o\rangle\langle o|$。
- 对每个 $o \in \mathcal{D}_n^{\text{cl,外}}$，内层道-子空间 $\mathcal{D}_n^{q,\text{内}}(o) \subseteq \mathcal{H}_n^\text{内}$，投影 $\Pi^\text{内}(o) = \sum_{i \in \mathcal{D}_n^{\text{cl,内}}(o)} |i\rangle\langle i|$。

**定义 6.3.2**（量子道-子空间归纳构造）

$$
\mathcal{D}_{2n}^q := \mathrm{span}_\mathbb{C}\Bigl\{\, |o\rangle \otimes |i\rangle \;:\; o \in \mathcal{D}_n^{\text{cl,外}},\; i \in \mathcal{D}_n^{\text{cl,内}}(o) \,\Bigr\}.
$$

**命题 6.3.3**（递归相容性）　由 C3，对 $v = (o\,;\,i) \in V_{2n}$：

$$
v \in \mathcal{D}_{2n}^\text{cl} \;\iff\; \iota(v) \in \mathcal{D}_{2n}^q.
$$

故经典道-集递归（`wen-formal.md` 定义 3.2.1）在 $\iota$ 下完全对应量子道-子空间递归。

**注 6.3.4**　量子版可处理外层叠加态作为 gate——比如 $|\psi_\text{外}\rangle = \frac{1}{\sqrt{2}}(|o_1\rangle + |o_2\rangle)$，其中 $o_1 \in \mathcal{D}_n^\text{外}, o_2 \notin \mathcal{D}_n^\text{外}$。这给出"半开 gate"，是经典不能表达的现象。此时 $p_\mathcal{D}^\text{外} = 1/2$，整个系统处于 $\mathbf{B}$ 的高阶版本——道-gate 自身的叠加。

---

## §7 模态分类的统一图景

### 7.1 五值模态对应表

| 模态 | 经典定义 | 量子定义 | 关系 |
|---|---|---|---|
| $\Box\text{真}$ | 邻域 $\subseteq \mathcal{D}$ | $\forall \rho' \in N_R,\; p_\mathcal{D}(\rho') = 1$ | 同构 |
| $\Box\text{假}$ | 邻域 $\subseteq \mathcal{D}^c$ | $\forall \rho' \in N_R,\; p_\mathcal{D}(\rho') = 0$ | 同构 |
| $\mathbf{C} / \mathbf{B}$ | — | $0 < p_\mathcal{D} < 1$ 且 $C(\rho) > 0$ | **量子新生** |
| $\mathbf{C} / \mathbf{N}$ | 邻域跨界 | $0 < p_\mathcal{D} < 1$ 且 $C(\rho) = 0$ | $\iota(\mathbf{C}^\text{cl}) \subseteq \mathbf{N}$ |
| $\boxtimes$ | $\pi_\text{外}(v) \notin \mathcal{D}_n^\text{外}$ | $\mathrm{Tr}_\text{外}(\Pi_\mathcal{D}^\text{外}\rho) = 0$ | $\iota(\boxtimes^\text{cl}) \subseteq \boxtimes^q$，但量子 $\boxtimes^q$ **更大**（含纠缠态） |

### 7.2 量子模态的几何

```
              p_𝒟 = 1
              □真
                │
                │
       𝐁 ─────┼───── 𝐍
     相干     │    去相干
   (量子新生) │  (经典嵌入)
                │
              □假
              p_𝒟 = 0

              ⊠
       （另一维度：结构性塌缩）
```

$\mathbf{B}$ 与 $\mathbf{N}$ 在 $\mathbf{C}$ 类内构成"水平"维度（相干性轴），$\Box\text{真}/\Box\text{假}$ 在垂直维度（概率轴），$\boxtimes$ 在第三维度（语义存在性轴）。

---

## §8 算子语义统一

### 8.1 道-保持算子的量子版

**定理 8.1.1**（量子内层翻转闭包）　$X_j^\text{内}$（$j \in \{1, \ldots, n\}$）保 $\mathcal{D}_{2n}^q$（即 $X_j^\text{内}(\mathcal{D}_{2n}^q) \subseteq \mathcal{D}_{2n}^q$）

$\iff$ 对所有 $o \in \mathcal{D}_n^{\text{cl,外}}$，$\mathcal{D}_n^{q,\text{内}}(o)$ 在 $X_j$ 下封闭。

**证明**　

($\Rightarrow$)　设 $|v\rangle \in \mathcal{D}_n^{q,\text{内}}(o)$。则 $|o\rangle \otimes |v\rangle \in \mathcal{D}_{2n}^q$（由定义 6.3.2 与 $v \in \mathcal{D}_n^{\text{cl,内}}(o)$ 当 $|v\rangle$ 是计算基；一般情形由线性扩展）。

$X_j^\text{内}(|o\rangle \otimes |v\rangle) = |o\rangle \otimes X_j|v\rangle \in \mathcal{D}_{2n}^q$，故 $X_j|v\rangle \in \mathcal{D}_n^{q,\text{内}}(o)$。

($\Leftarrow$)　反向：$\mathcal{D}_{2n}^q$ 由 $|o\rangle \otimes |i\rangle$ 生成（$o \in \mathcal{D}^\text{外}, i \in \mathcal{D}^\text{内}(o)$）。$X_j^\text{内}$ 保此生成集（由假设 $X_j |i\rangle \in \mathcal{D}_n^{q,\text{内}}(o)$）。线性扩展。$\blacksquare$

这是 `wen-formal.md` 定理 5.1.1 的量子版本。

### 8.2 稳定层的量子推广

**定义 8.2.1**（量子 $k$-核）　对道-子空间 $\mathcal{D}^q \subseteq \mathcal{H}_n$ 与算子集 $\mathcal{G}$（如 $\{X_j\}_j$）：

$$
\mathrm{Core}_k^q(\mathcal{D}^q) \;:=\; \bigl\{\, |\psi\rangle \in \mathcal{D}^q \;:\; \forall\, g_1, \ldots, g_m \in \mathcal{G},\, m \leq k,\; g_m \cdots g_1 |\psi\rangle \in \mathcal{D}^q \,\bigr\}.
$$

**命题 8.2.2**（经典-量子核相容性）　对计算基态 $|v\rangle$：

$$
|v\rangle \in \mathrm{Core}_k^q(\mathcal{D}^q) \;\iff\; v \in \mathrm{Core}_k(\mathcal{D}_n^\text{cl}).
$$

**证明**　由 C2，Pauli X 序列在计算基上等价于经典翻转序列；由 C3，落入 $\mathcal{D}^q$ 等价于经典落入 $\mathcal{D}$。$\blacksquare$

---

## §9 塌缩不可逆性的量子版

`wen-formal.md` 定理 9.1.1 的量子版本——结构更精细，因为偏迹给出代数化的"塌缩"度量。

### 9.1 内层幺正保 $\boxtimes^q$

**定理 9.1.1q**（量子塌缩不可逆）　设 $\rho \in \boxtimes^q$。对任意内层幺正 $U_\text{内} = I_\text{外} \otimes V_\text{内}$（其中 $V_\text{内}$ 是 $\mathcal{H}_n^\text{内}$ 上的幺正）：

$$
U_\text{内}\,\rho\,U_\text{内}^\dagger \;\in\; \boxtimes^q.
$$

**证明**　计算

$$
\begin{aligned}
\mathrm{Tr}_\text{外}\bigl(\Pi_\mathcal{D}^\text{外}\,U_\text{内}\,\rho\,U_\text{内}^\dagger\bigr)
&= \mathrm{Tr}_\text{外}\bigl((\Pi_\mathcal{D} \otimes I_\text{内})(I_\text{外} \otimes V_\text{内})\,\rho\,(I_\text{外} \otimes V_\text{内}^\dagger)\bigr) \\
&= \mathrm{Tr}_\text{外}\bigl((I_\text{外} \otimes V_\text{内})(\Pi_\mathcal{D} \otimes I_\text{内})\,\rho\,(I_\text{外} \otimes V_\text{内}^\dagger)\bigr) \\
&\quad\text{(因 $\Pi_\mathcal{D} \otimes I_\text{内}$ 与 $I_\text{外} \otimes V_\text{内}$ 在不同张量因子作用，对易)} \\
&= V_\text{内}\,\mathrm{Tr}_\text{外}(\Pi_\mathcal{D}^\text{外}\,\rho)\,V_\text{内}^\dagger \\
&\quad\text{(偏迹与不在被迹掉因子上作用的算子可交换)} \\
&= V_\text{内} \cdot 0 \cdot V_\text{内}^\dagger \;=\; 0.
\end{aligned}
$$

故 $U_\text{内}\,\rho\,U_\text{内}^\dagger \in \boxtimes^q$。$\blacksquare$

### 9.2 救援必经外层（量子版）

**推论 9.2.1q**　要从 $\rho \in \boxtimes^q$ 进入 $\mathcal{O}_{2n}^q$，算子序列必含**至少一个外层算子**（即 $U_\text{外} \otimes I_\text{内}$ 形式且 $[U_\text{外}, \Pi_\mathcal{D}] \neq 0$，或外-内纠缠算子）。

**证明**　反证。若所有算子都是 $I_\text{外} \otimes V_\text{内}$ 形式，由定理 9.1.1q 归纳，全程在 $\boxtimes^q$，与"进入 $\mathcal{O}_{2n}^q$"矛盾。$\blacksquare$

### 9.3 经典塌缩定理的量子还原

**命题 9.3.1**（经典塌缩 = 量子塌缩在嵌入下）　设 $v \in \boxtimes^\text{cl}$，对应经典翻转序列 $\sigma_{j_1}^\text{内}, \ldots, \sigma_{j_m}^\text{内}$（仅内层）。则其量子化序列 $X_{j_1}^\text{内}, \ldots, X_{j_m}^\text{内}$ 满足

$$
X_{j_m}^\text{内} \cdots X_{j_1}^\text{内}\,\iota(v) \;\in\; \boxtimes^q,
$$

与 `wen-formal.md` 定理 9.1.1 的结论 $\sigma_{j_m}^\text{内} \cdots \sigma_{j_1}^\text{内}(v) \in \boxtimes^\text{cl}$ 在 $\iota$ 下对应。

**证明**　

由 C2，$X_{j_k}^\text{内}\,\iota(v) = \iota(\sigma_{j_k}^\text{内}(v))$（计算基保持）。归纳：

$$
X_{j_m}^\text{内} \cdots X_{j_1}^\text{内}\,\iota(v) = \iota\bigl(\sigma_{j_m}^\text{内} \cdots \sigma_{j_1}^\text{内}(v)\bigr) \in \iota(\boxtimes^\text{cl}) \subseteq \boxtimes^q.
$$

最后包含由 C5。$\blacksquare$

### 9.4 量子塌缩的"严格大于"

**命题 9.4.1**　$\iota(\boxtimes^\text{cl}) \subsetneq \boxtimes^q$。即存在量子塌缩态不在经典塌缩态的嵌入像内。

**例**　设 $n = 1$，$\mathcal{D}_1^\text{外} = \{0\}$（仅外层 0 为道）。考虑纠缠态

$$
|\psi\rangle = \frac{1}{\sqrt{2}}\bigl(|1\rangle_\text{外}\,|0\rangle_\text{内} + |1\rangle_\text{外}\,|1\rangle_\text{内}\bigr) = |1\rangle_\text{外} \otimes |+\rangle_\text{内}.
$$

外层处于 $|1\rangle$（非道），故 $\mathrm{Tr}_\text{外}(\Pi_\mathcal{D}^\text{外}|\psi\rangle\langle\psi|) = 0$，$|\psi\rangle \in \boxtimes^q$。

但 $|\psi\rangle$ 不是任何 $\iota(v) = |v\rangle\langle v|$ 的形式——内层是叠加态 $|+\rangle$，非计算基。$\blacksquare$

**意义**　量子 $\boxtimes^q$ 不仅包含"外层关闭、内层经典"的塌缩态，还包含"外层关闭、内层处于叠加/纠缠"的塌缩态。后者是经典文-代数表达不出的现象，但服从同样的塌缩不可逆律。这是量子推广**在结构上有实质收获**的证据。

---

## §10 算法与计算开销

### 10.1 复杂度对比

| 操作 | 经典 | 量子（一般态） | 量子（结构化态） |
|---|---|---|---|
| 状态储存 | $n$ bits | $2^n$ 复数 | $\mathrm{poly}(n)$（MPS, 稳定子） |
| 单步翻转 | $O(1)$ | $O(2^n)$ | $\mathrm{poly}(n)$ |
| 道-属于判定 | $O(\log\|\mathcal{D}\|)$ | $O(2^n)$ | $\mathrm{poly}(n)$ |
| 模态判定 | $O(\|N_R\|)$ | $O(2^n \cdot \|N_R\|)$ | $\mathrm{poly}(n) \cdot \|N_R\|$ |
| 偏迹 | — | $O(4^n)$ | $\mathrm{poly}(n)$ |

### 10.2 工作流分层

- **经典层 $n \leq 64$**：卦序搜索、稳定层分析、道-路径规划、大规模 $\boxtimes$ 检测。
- **量子精确层 $n \leq 12$**：$\mathbf{B}/\mathbf{N}$ 几何研究、相干效应、相位干涉、纠缠塌缩态分析。
- **量子结构化层 任意 $n$**：稳定子态、矩阵积态、张量网络。若 $\mathcal{D}^q$ 落在这类子类，保持量子语义不爆。

### 10.3 混合工作流模板

典型场景"道-路径可行性分析"：

1. **经典粗筛** ($n = 32$)：用经典版枚举候选道-路径，剪去 $\boxtimes^\text{cl}$ 区域。
2. **边界量子精算** (在路径关键 4-qubit 子系统上)：检验是否有相干干涉效应改变可行性。
3. **经典回填** ：将量子分析结果回填到经典路径，得到最终判定。

经典-量子边界由当前问题的相干性需求决定。无相干性需求的纯组合判定问题（道-集成员、k-核计算）始终留在经典层。

---

## §11 Lean 4 实施骨架

### 11.1 仓库结构

```
wen-core/
├── lakefile.lean
├── Wen/
│   ├── Slot.lean              -- Layer 0
│   ├── Classical/
│   │   ├── State.lean         -- ClassicalV n
│   │   ├── Dao.lean           -- 𝒟_n^cl, 道-依赖族
│   │   ├── Flip.lean          -- σ_j
│   │   ├── Modal.lean         -- 四值经典模态
│   │   ├── Core.lean          -- k-核
│   │   └── Rescue.lean        -- 救援可达性
│   ├── Quantum/
│   │   ├── State.lean         -- QuantumV n（依赖 mathlib）
│   │   ├── Dao.lean           -- 道-子空间, Π_𝒟
│   │   ├── Pauli.lean         -- X_j
│   │   ├── PartialTrace.lean  -- Tr_外
│   │   ├── Modal.lean         -- 五值量子模态 (含 B, N)
│   │   └── Rescue.lean        -- 9.1.1q
│   └── Bridge/
│       ├── Embedding.lean     -- ι
│       ├── Measurement.lean   -- Born
│       └── Compatibility.lean -- C1–C5
└── Examples/
    └── V6_Mengua.lean         -- 单卦端到端例子
```

### 11.2 关键类型签名

```lean
-- Slot.lean
def Slot (n : ℕ) := Fin n

def split {n : ℕ} (j : Fin (2 * n)) : Fin n ⊕ Fin n :=
  if h : j.val < n then
    Sum.inl ⟨j.val, h⟩
  else
    Sum.inr ⟨j.val - n, by omega⟩

-- Classical/State.lean
def ClassicalV (n : ℕ) : Type := Slot n → Bool

-- Classical/Flip.lean
def flip_cl {n : ℕ} (j : Slot n) (v : ClassicalV n) : ClassicalV n :=
  fun k => if k = j then !v k else v k

-- Quantum/State.lean
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.TensorProduct.Basic

def QuantumV (n : ℕ) : Type :=
  { ψ : EuclideanSpace ℂ (Fin (2^n)) // ‖ψ‖ = 1 }

-- Quantum/Pauli.lean
def X_op {n : ℕ} (j : Fin n) : EuclideanSpace ℂ (Fin (2^n)) →ₗ[ℂ] EuclideanSpace ℂ (Fin (2^n)) :=
  sorry  -- 张量积构造

-- Bridge/Embedding.lean
def ι {n : ℕ} (v : ClassicalV n) : QuantumV n :=
  ⟨Pi.single (encode v) 1, by simp [encode_lt]⟩
  where encode : ClassicalV n → Fin (2^n) := sorry

-- Bridge/Compatibility.lean
theorem C1_projection_indicator {n : ℕ} 
    (𝒟 : Set (ClassicalV n)) [DecidablePred (· ∈ 𝒟)] 
    (v : ClassicalV n) :
    Π 𝒟 (ι v).val = (if v ∈ 𝒟 then (1 : ℂ) else 0) • (ι v).val := by
  sorry

theorem C2_pauli_flip {n : ℕ} (j : Fin n) (v : ClassicalV n) :
    X_op j (ι v).val = (ι (flip_cl j v)).val := by
  sorry

theorem C5_collapse_compat {n : ℕ} (v : ClassicalV (2*n)) :
    (ι v) ∈ Boxtimes_q ↔ v ∈ Boxtimes_cl := by
  sorry
```

### 11.3 实施路线图

| 里程碑 | 内容 | 估期 |
|---|---|---|
| **v0.2-α** | `Slot.lean` + `Classical/{State, Dao, Flip}.lean`（从 `wen-formal.md` 移植 Layer 1） | 1 周 |
| **v0.2-β** | `Classical/{Modal, Core, Rescue}.lean`（经典完整） | 1 周 |
| **v0.2-γ** | `Quantum/{State, Pauli, Dao}.lean`（量子基本骨架，$n \leq 4$） | 2 周 |
| **v0.2-δ** | `Bridge/{Embedding, Compatibility}.lean`（C1–C5 完整证明） | 2 周 |
| **v0.2-ε** | `Quantum/{PartialTrace, Rescue}.lean`（定理 9.1.1q） | 1 周 |
| **v0.2-ζ** | `Examples/V6_Mengua.lean`（蒙卦端到端） | 1 周 |

每个里程碑应有 CI 跑通 + 至少一个端到端测试。优先级建议：α → β → δ（先把经典稳了再做桥接证明），然后 γ → ε → ζ。

---

## 附录 A: 与 `wen-formal.md` 的对应索引

| `wen-formal.md` 章节 | 本文章节 | 关系 |
|---|---|---|
| §1 基础对象 | §2（Layer 0）+ §3（Layer 1 ref）+ §4.1 | 经典 $V_n$ 抽出索引 + 量子 $\mathcal{H}_n$ 类比 |
| §2 自相似分解 | §6.1, §6.2 | 双 backend 自相似性的代数对偶 |
| §3 道-集归纳 | §6.3, 命题 6.3.3 | 量子道-子空间递归 |
| §4 位翻转算子 | §4.3, §8 | Pauli 算子化 |
| §5 闭包定理 | §8.1, 定理 8.1.1 | 内层闭包量子版 |
| §6 稳定层 | §8.2 | $k$-核量子版 |
| §7 模态分类 | §4.7, §7 | 四值 → 五值（$\mathbf{C}$ → $\mathbf{B}/\mathbf{N}$） |
| §8 跨层算子 | §6.3, 注 6.3.4 | 加上叠加 gate |
| §9 救援可达性 | §9.1, §9.2, §9.3 | 量子塌缩定理 9.1.1q + 经典还原 |
| §10 文-代数原子 | §7.1, §7.2, 推论 5.3.2 | $\mathbf{B}$ 与 $\mathbf{N}$ 在语言层分立 |

## 附录 B: 与既有量子逻辑文献的关系

- **Birkhoff–von Neumann 量子逻辑** (1936)：本文 $\Pi_\mathcal{D}$ 形成的投影格是其特例。Wen 添加了**依赖型 gate 结构**与 $\boxtimes$ 类。
- **Categorical Quantum Mechanics** (Coecke, Abramsky)：本文 Layer 3 桥接可对应 dagger compact category 中的 Frobenius 结构。$\iota$ 是 classical-quantum interface。
- **Quantum 模态逻辑** (Mateus, Sernadas)：本文 §7 量子模态分类与之相关，但 $\boxtimes$ 类是新引入——基于依赖型 gate 结构而非测量基选择。
- **Belnap 四值逻辑** (1977)：本文 $\mathbf{B}/\mathbf{N}$ 直接对应 Belnap 的"both/neither"，但物理实现化为相干性/去相干性。

---

## 结语

本文给出文-代数的双 backend 架构。核心结论：

1. **经典 $\subseteq$ 量子**：经典 $V_n$ 通过 $\iota$ 嵌入为 $\mathcal{H}_n$ 的计算基，经典道-集嵌入为量子道-子空间。
2. **五条桥接定理 C1–C5**：保证经典定理在量子语境下保持。所有经典操作（翻转、道-判定、塌缩检测、救援）都是量子操作在计算基上的限制。
3. **量子专属**：相干 $\mathbf{B}$ 类、相位维度、纠缠塌缩态——是量子结构的实质收获，不在经典像内（推论 5.3.2、命题 9.4.1）。
4. **塌缩不可逆性的量子化**：从集合论的"$\pi_\text{外} \notin \mathcal{D}^\text{外}$"升到算子代数的"$\mathrm{Tr}_\text{外}(\Pi^\text{外}_\mathcal{D}\rho) = 0$"，并支持纠缠态的塌缩（量子专属现象）。

实施上分层 Lean 4 模块结构允许：经典工作流不变，量子按需 opt-in。这刚好对应文-代数"底层语义不绑定具体物理实现"的定位——文是一个**可量子化的形式语言**，而不是"量子语言"或"经典语言"。

下一步建议优先 v0.2-α 与 v0.2-β（把经典版 Lean 化），然后并行启动 v0.2-γ 量子骨架。桥接证明 v0.2-δ 是关键卡点——一旦 C1–C5 在 Lean 4 中走通，整个架构就是 mathematically verified 的双 backend 系统。
