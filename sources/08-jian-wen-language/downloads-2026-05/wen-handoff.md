# 文 (Wen) · Lean 4 Interpreter — Implementation Handoff

> **作者**: 由前一个 Claude 整理，基于与 Ren 的设计对话  
> **接手实现**: 另一个 Claude Code 实例  
> **背景文件**: `wen-formal.md`（形式化 §1-§10 + 附录 A-B）  
> **本文档目的**: 把设计对话中确定的架构决策、术语约定、未决问题完整交接，避免重复绕弯

---

## 0. 项目语境（必读）

文 (Wen) 是 Ren 在做的形式化古典汉语 DSL，前身曾称"間"(Jian)，**已更名为"文"**——不要再用 Jian 这个旧名。

- **kernel**: 9 个虚词 atom `者 / 之 / 非 / 而 / 凡 / 即 / 也 / 是 / 令`，STLC-complete
- **理论基础**: BaguaAlgebra + I Ching 卦象结构 + 王阳明知行合一 + 大同思想
- **实现**: Lean 4，**纯 native 编译**，**不走 V8 / WASM / JS / 浏览器**
- **当前目标**: kernel formal proof + 完整 interpreter（涵盖整个 R_0..R_8 塔的算子）ground 成单一 native binary

### ⚠️ 关键的术语去歧义

Ren 口语中出现的 "V8" / "v8" **不是 Google 的 V8 引擎**，是 Wen 自己塔上的层级 **R_8** (= $\mathbb{F}_2^8$ = 256 元素的 cell 空间)。

类似地，"V4" / "v4" 是塔上的 R_4 (= $\mathbb{F}_2^4$ = 16 元素)。

前一轮设计对话中曾把 V8 误读为浏览器引擎，提出 WASM/emscripten/Proxy 一整套方案——**那套全部作废**。如果你在自己的推理中出现 "JS 兼容"、"浏览器"、"Proxy/Symbol"、"event loop hook" 这些词，**停下来检查**：你大概率走错了方向。

另有一处更精微的术语 collision，下文 §3.4 详述：paper 中的 $V_4$ (= 16 元) 与 diagram 注释中的 "V₄ (cuo/zong/hu)" (= Klein 四元群, 4 元) 是不同的对象，**不能混用**。

---

## 1. 形式化基础（来自 wen-formal.md）

### 1.1 爻空间

$$V_n := \mathbb{F}_2^n, \quad |V_n| = 2^n, \quad \dim_{\mathbb{F}_2} V_n = n$$

### 1.2 偶倍分解定理 (§2.1)

$$V_{2n} \cong V_n \oplus V_n$$

为 $\mathbb{F}_2$-向量空间同构。**这是跨层级 self-similarity 的核心**。

记 $v = (o\,;\,i)$ 其中 $o = \pi_\text{外}(v)$，$i = \pi_\text{内}(v)$。

### 1.3 道-集与道-依赖族 (§3)

$\mathcal{D}_n \subseteq V_n$ 表示该层级"为真"的子集。

道-依赖族 $\{\mathcal{D}_n^\text{内}(o)\}_{o \in \mathcal{D}_n^\text{外}}$ 给出递归构造：

$$\mathcal{D}_{2n} := \{(o\,;\,i) : o \in \mathcal{D}_n^\text{外} \land i \in \mathcal{D}_n^\text{内}(o)\}$$

这条规则跨层级自相似（每升一层规则不变，作用对象从 $V_{2^k}$ 替换为 $V_{2^{k+1}}$）。

### 1.4 位翻转 (§4)

$\sigma_j(v) := v + e_j$ (mod 2)，对合且两两对易，生成群 $(\mathbb{Z}/2)^n$。

在偶倍分解下分为：
- **外层翻转** $\sigma_j^\text{外}$：$(o\,;\,i) \mapsto (o + e_j\,;\,i)$
- **内层翻转** $\sigma_j^\text{内}$：$(o\,;\,i) \mapsto (o\,;\,i + e_j)$

两类翻转**地位极不对称**（见 §5 与 §9）。

### 1.5 四值模态 (§7)

$$V_{2n} = \mathbf{N}_\text{真} \;\sqcup\; \mathbf{N}_\text{假} \;\sqcup\; \mathbf{C} \;\sqcup\; \boxtimes_{2n}$$

- $\boxtimes_{2n}$: $\pi_\text{外}(v) \notin \mathcal{D}_n^\text{外}$，gate 关闭，**结构性不可知**
- $\mathbf{N}_\text{真}$: $N_R(v) \subseteq \mathcal{D}_{2n}$，必真
- $\mathbf{N}_\text{假}$: $N_R(v) \cap \mathcal{D}_{2n} = \emptyset$，必假
- $\mathbf{C}$: 邻域两边都有，**可两 / 偶然**

### 1.6 救援必经外层 (§9.1, §9.2)

**塌缩不可逆**：$v \in \boxtimes_{2n}$ 经任何纯内层翻转序列后仍在 $\boxtimes_{2n}$。

**推论**：从 $\boxtimes$ 出来的翻转序列必含至少一次外层翻转。

修养论对应"**格物先于诚意**"——必须先开 gate (外层翻转, 格物)，才能在 gate 内做工夫 (内层翻转, 诚意)。这条不变量将推到 Lean 的 type system（见 §4.4）。

### 1.7 $\boxtimes$ 作为独立原子 (§10)

文-代数四值半格：

$$\top (\Box\text{真}) \;\succ\; \Diamond (\mathbf{C}) \;\succ\; \bot (\Box\text{假}), \quad \boxtimes \perp \{\top, \Diamond, \bot\}$$

$\boxtimes$ 与其它三值**不在同一序上**，是另一维度（语义存在性）。

**对比**：
- Kleene K3 第四值 = undefined（真假未定）
- Belnap FOUR 第四值 = both（信息冲突）
- **文** 第四值 = $\boxtimes$（gate 关闭，真假位无意义；结构性不可知）

$\boxtimes$ **不可还原为"非"**（"非"是布尔局部否定）。在 Lean 实现中必须做成 first-class，**不要**用 `Option.none` 或 exception 表达。

---

## 2. 塔架构 (R_0 .. R_8)

塔从 $R_0$ (太极) 拾级而上，每层 $R_n = \mathbb{F}_2^n$，基数 $2^n$。

| Layer | 基数 | 语义 anchor | 备注 |
|---|---|---|---|
| **R_0** | 1 | 太极 / 一元 / 元 / 极 / 一 | Unit |
| **R_1** | 2 | 爻 / 两仪 (实 / 虚) | 单 bit |
| **R_2** | 4 | 四象 (春 / 夏 / 秋 / 冬) | $(\mathbb{Z}/2)^2$ |
| **R_3** | 8 | 八卦 (健悦显起入险止顺) | 受 Klein 四元群 (cuo / zong / hu) 作用 |
| **R_4** | 16 | 面 / Mian = Ben × Zheng | 16-命 (本×征) |
| **R_5** | 32 | 五爻 = Mian × Bool | ⚠ **provisional, 无传统 anchor** |
| **R_6** | 64 | 重卦 / Hexagram (y₁..y₆: 改化变临主极) | 受 Klein 四元群作用 |
| **R_7** | 128 | 因卦 / Cell128 (+ 因 axis, 印 = toggle) | R_6 + 因 bit |
| **R_8** | 256 | 果卦 / Cell256 (+ 果 axis, 投 = toggle) | R_7 + 果 bit；**当前实现里程碑** |

**lift / proj 单步算子**：`liftR_n_to_R_{n+1}` 与 `projR_{n+1}_to_R_n`，所有相邻层之间都有。

**偶倍分解**：$R_{2k} \cong R_k \oplus R_k$ 对偶数 $2k$ 成立（R_2, R_4, R_6, R_8）。

**关键**：doubling 与 sequential lift 是**两组 first-class 算子族，互不替代**——doubling 给偶数层 self-similarity 递归，sequential 给塔的连续性。两者并存。

---

## 3. R_8 的双重结构（关键架构决策）

R_8 cell 是 8 bits，**bit layout 已确定**：

```
位:    7   6   5   4   3   2   1   0    (MSB → LSB)
内容: [ h_5 h_4 h_3 h_2 h_1 h_0 | 因 | 果 ]
       ↑──── hex 6 bits ────↑    ↑    ↑
                                bit 1  bit 0
```

R_8 上**同时存在两套结构**，**已确认是 orthogonal（不是 competing decompositions）**：

### 3.1 结构 A：偶倍分解（数据形状 / representation）

$$R_8 \cong R_4 \oplus R_4$$

按 **4+4** 切：

```
split:  [ b_7 b_6 b_5 b_4 | b_3 b_2 b_1 b_0 ]
            outer R_4         inner R_4
            (16 元)            (16 元)
```

256 = 16 × 16。这是 cell 的**数据如何由两半构成**——`split` / `merge` 双向 isomorphism。这是 paper §2.1 的偶倍分解定理在 R_8 上的实例。

### 3.2 结构 B：Klein × Shi 标签（语义 / quotient invariants）

按 **6+2** 切的两个**投影**：

```
hexClass : Cell 8 → KleinV4   -- hex 6 bits 经 cuo/zong/hu Klein 商
shiMode  : Cell 8 → ShiV4     -- (因, 果) 2 bits ↦ Shi modality
```

### 3.3 Shi ↔ (因, 果) 映射（已确认）

| (因, 果) | Shi | 含义 |
|---|---|---|
| (0, 0) | **未** | 未然，因果俱未起 |
| (1, 0) | **因 / 今** | 立因待果，当下进行中 |
| (0, 1) | **果** | 果显而因隐 / 反因之果 |
| (1, 1) | **已** | 因果俱足，事已闭 |

> **重要**：**"道" 不在 (因, 果) 的某个 bit 组合上**——它是横贯不变量 (horizontal invariant)，穿过所有四种 (因, 果) 配置的"永真"轴。
>
> 在 Lean 实现里："道" **不是 `ShiV4` 的第五个 constructor**，而是以 `∀ s : ShiV4, ...` 形式的 invariant claim 出现。或者表达为穿越所有 Shi 的不变性 theorem：`theorem dao_inv : ∀ s : ShiV4, P s`。

### 3.4 关键术语去歧义

**这里有个会反复绊倒人的 collision**：

- **paper §1 的 $V_4$** = $\mathbb{F}_2^4$ = **16 元素** = 塔上的 R_4 (面 / Mian)
- **diagram 注释的 "V₄ cuo/zong/hu" 和 "V₄ Shi"** = Klein 四元群 = **4 元素**

是两个不同的"V_4"！

**代码中的命名约定**：
- `Cell 4` 或 `BitVec 4` 表示 R_4 (16 元)
- `KleinV4` 表示 Klein 四元群 (4 元)，用于 hex 部分的 cuo/zong/hu 群作用
- `ShiV4` 表示 Shi 模态 {道, 已, 今, 未} (4 元)

**不要**使用未限定的 `V4` 作为标识符。

### 3.5 群作用 Klein V_4

cuo (错)、zong (综)、hu (互) 是 hex 6 bits 上的三个对合，加 identity 构成 Klein 四元群 $(\mathbb{Z}/2)^2$：

- **错 (cuo)**：阴阳全翻转 = 6-bit XOR with `0b111111`
- **综 (zong)**：爻序反转 = bit reversal of 6 bits
- **互 (hu)**：错 ∘ 综 = bit reversal 之后再 XOR

每个 hexagram 在 Klein V_4 作用下落入一个轨道。轨道数 ≤ 16（因 stabilizer 存在，例如乾 ☰☰ 被综固定，其轨道大小为 2 而非 4）。

### 3.6 两套结构的关系（图解）

**同一组 8 bits，两条切线**：

```
     bit:  7   6   5   4   3   2   1   0
           ─────────────────  ───  ─  ─
A split:  [ outer  ][  inner  ]              ← 4+4 切（数据形状）
B 投影:   [    hex bits   ][因][果]          ← 6+2 切（语义标签）

A 与 B 切线不同 → orthogonal。
A 决定 cell 怎么 represent；B 决定 cell 落在哪个语义等价类。
```

Lean 实现中分别定义、**互不污染**：

```lean
-- A：数据 representation
def split  : Cell 8 → Cell 4 × Cell 4
def merge  : Cell 4 × Cell 4 → Cell 8

-- B：tag（由 cell 算出，无独立 storage）
def hexClass : Cell 8 → KleinV4
def shiMode  : Cell 8 → ShiV4
```

`hexClass` 和 `shiMode` 是 **derived projection**，不占独立 storage——它们与 `split` 是同一组 bits 的两种独立 view。

---

## 4. Lean 4 实现架构

### 4.1 核心类型（参数化）

**关键原则：不要 hard-code R_8。优化不是目标，扩展性是。**

```lean
namespace Wen

-- 参数化 n。R_8 是当前里程碑，不是上限。R_9, R_10 ... 都应零成本复用代码。
def Cell (n : Nat) : Type := BitVec n

-- 道-集做成 predicate，不做位图（保持运行时无 size 假设；位图是优化，不是设计）
def DaoSet (n : Nat) : Type := Cell n → Prop

-- 道-依赖族
structure DaoFamily (n : Nat) where
  outer : DaoSet n
  inner : (o : Cell n) → o ∈ outer → DaoSet n

-- 四值模态（first-class，⊠ 作为独立 constructor，per §10.1）
inductive Mode where
  | boxTrue    -- □真
  | boxFalse   -- □假  
  | both       -- C / 可两
  | collapsed  -- ⊠（不是 Option.none，不是 exception！）
  deriving DecidableEq, Repr

end Wen
```

### 4.2 spec / impl 分离

paper 附录 B 用 `Fin n → Bool` 做 spec。实现用 `BitVec n` 做 runtime。二者通过桥接 theorem 关联：

```lean
-- spec layer
def CellSpec (n : Nat) : Type := Fin n → Bool

def BitVec.toFun {n : Nat} (v : BitVec n) : Fin n → Bool :=
  fun i => v.getLsb i.val

theorem dao_iff_spec (𝒟 : DaoSet n) (𝒟_spec : Set (Fin n → Bool)) (v : BitVec n) :
    𝒟 v ↔ BitVec.toFun v ∈ 𝒟_spec := ...
```

所有 §1-§9 的 proof 在 spec 层做（用 `Fin n → Bool`，proof-friendly），runtime 在 impl 层跑（用 `BitVec n`，native int fold），桥接 theorem 保证一致性。

### 4.3 偶倍分解的 polymorphic 同构

```lean
def split : {n : Nat} → Cell (2*n) → Cell n × Cell n := 
  fun v => 
    (BitVec.extract v 0 (n-1), BitVec.extract v n (2*n-1))  -- 伪码，需校对索引

def merge : {n : Nat} → Cell n × Cell n → Cell (2*n) := 
  fun (o, i) => BitVec.append o i  -- 伪码

theorem split_merge : ∀ (p : Cell n × Cell n), split (merge p) = p := ...
theorem merge_split : ∀ (v : Cell (2*n)), merge (split v) = v := ...
```

**所有递归算子免费**：

```lean
def daoCheck {n : Nat} (𝒟 : DaoFamily n) (v : Cell (2*n)) : Prop :=
  let (o, i) := split v
  ∃ h : 𝒟.outer o, 𝒟.inner o h i

def Boxtimes {n : Nat} (𝒟 : DaoFamily n) (v : Cell (2*n)) : Prop :=
  ¬ 𝒟.outer (split v).1

def hammingWeight : {n : Nat} → Cell n → Nat := ...
-- 等等，全部 {n : Nat} 起头
```

**R_8 跑通的代码 R_{16} 直接复用。**

### 4.4 翻转算子 + 救援不变量推到 type level

```lean
-- 通用单 bit 翻转
def flip {n : Nat} (v : Cell n) (j : Fin n) : Cell n :=
  v ^^^ (BitVec.ofNat n 1).shiftLeft j.val

-- 外层翻转（基于偶倍分解）
def flipOuter {n : Nat} (v : Cell (2*n)) (j : Fin n) : Cell (2*n) :=
  let (o, i) := split v
  merge (flip o j, i)

-- 内层翻转：约束在非 collapsed 状态（§9.2 救援必经外层）
def flipInner {n : Nat} (𝒟 : DaoFamily n) 
    (v : Cell (2*n)) (h : ¬ Boxtimes 𝒟 v) (j : Fin n) : Cell (2*n) :=
  let (o, i) := split v
  merge (o, flip i j)
```

**注意 `flipInner` 的签名带 refinement type** `h : ¬ Boxtimes 𝒟 v`。

这把 §9.2 的"救援必经外层"不变量推到**编译期**——任何对 collapsed cell 的内层翻转尝试，编译时就拒绝。caller 必须先 prove or refute 落点。

这是把"诚意必先格物"形式化进了 type system——你**不能**在还没格物 (gate 没开) 的状态下做诚意 (内层工夫)，编译器替你把住这关。

### 4.5 模态分类 (§7.5)

```lean
def modalClassify {n : Nat} (𝒟 : DaoFamily n) (R : Cell (2*n) → Cell (2*n) → Prop)
    [DecidablePred (𝒟.outer)] [/* 必要的 Decidable 实例 */]
    (v : Cell (2*n)) : Mode :=
  if ¬ 𝒟.outer (split v).1 then .collapsed
  else
    -- 邻域分析
    let N := { u | R v u }
    if N ⊆ daoCheck 𝒟 then .boxTrue
    else if N ∩ daoCheck 𝒟 = ∅ then .boxFalse
    else .both
```

（伪码：需要补 Decidable 实例与有限性证明。实际写时用具体的可枚举邻域如汉明球 $R_r$。）

### 4.6 R_8 特定算子

```lean
namespace Wen.R8

-- 6+2 投影（bit 0 = 果, bit 1 = 因, bit 2..7 = hex）
def hexBits : Cell 8 → Cell 6 := fun v => BitVec.extract v 2 7
def yinBit  : Cell 8 → Bool   := fun v => v.getLsb 1
def guoBit  : Cell 8 → Bool   := fun v => v.getLsb 0

-- Klein 四元群（4 元素，不是 R_4）
inductive KleinV4 where
  | id | cuo | zong | hu
  deriving DecidableEq, Repr

-- cuo/zong/hu 在 hex bits 上的作用
def kleinAction (k : KleinV4) (h : Cell 6) : Cell 6 := 
  match k with
  | .id   => h
  | .cuo  => ~~~h                          -- 错：阴阳全翻转
  | .zong => h.reverse                     -- 综：爻序反转
  | .hu   => (~~~h).reverse                -- 互 = cuo ∘ zong

-- hexClass: hex 部分模 Klein 商的代表元
def hexClass : Cell 8 → KleinV4 := 
  fun v => /* 选每个 Klein 轨道的 canonical 代表，需具体定 */

-- Shi 模态（4 元素，已确认映射）
inductive ShiV4 where
  | wei  -- 未  (因=0, 果=0)
  | yin  -- 因/今 (因=1, 果=0)
  | guo  -- 果  (因=0, 果=1)
  | yi   -- 已  (因=1, 果=1)
  deriving DecidableEq, Repr

def shiMode : Cell 8 → ShiV4 := fun v =>
  match yinBit v, guoBit v with
  | false, false => .wei
  | true,  false => .yin
  | false, true  => .guo
  | true,  true  => .yi

-- 印 = 因位 toggle（在 R_7 → R_8 进入时的算子）
def yinToggle : Cell 8 → Cell 8 := fun v => flip v ⟨1, by decide⟩

-- 投 = 果位 toggle（R_8 内部算子）
def guoToggle : Cell 8 → Cell 8 := fun v => flip v ⟨0, by decide⟩

-- "道" 是横贯不变量，不在 ShiV4 上
-- 体现为：某性质对所有 ShiV4 取值都成立
def daoInvariant (P : Cell 8 → Prop) : Prop :=
  ∀ v : Cell 8, (∀ s : ShiV4, /* P 在 shiMode 替换下不变 */) → P v

end Wen.R8
```

### 4.7 9-atom kernel（design space — 与 Ren 推进）

每个 atom 在 R_8 cell 上 dispatch，**返回 `Mode` 而非 `Bool`**：

```lean
inductive Atom where
  | zhe   -- 者: 主题化 / topicalization
  | zhi   -- 之: 关系查询 / relational query
  | fei   -- 非: 否定（布尔局部，不要与 ⊠ 混同！）
  | er    -- 而: 序连 / sequence
  | fan   -- 凡: 全称量化
  | ji    -- 即: definitional equality / unification
  | ye    -- 也: 句之终结 + 判断
  | shi   -- 是: 指代 / context reference
  | ling  -- 令: 引入绑定

-- evalAtom 接受 cell + arg cell + dao family，返回 Mode 与新 cell
def evalAtom (a : Atom) (v : Cell 8) (arg : Cell 8) (𝒟 : DaoFamily 4) 
    : Mode × Cell 8 := /* dispatch by a */
```

具体每个 atom 的 evaluator **是 design space**，需要和 Ren case-by-case 推。前期可以给 stub，让 type 跑通。

**关键提示**：
- "非" 是布尔局部否定（XOR a bit），**不是** ⊠。两者在 §10.1 明确区分
- "之" 是关系查询，可能返回 `.collapsed`（"未明"）
- "凡" 在可枚举 R_n (n 小) 上展开成 generator；不可枚举时留为命题
- "者...也" 是配对结构（判断 + 绑定）
- "令 A 为 B" 是 explicit 引入

---

## 5. 推荐模块结构

```
Wen/
├── Cell.lean         -- Cell, BitVec wrappers, flip, split/merge
├── Dao.lean          -- DaoSet, DaoFamily, daoCheck, Boxtimes
├── Flip.lean         -- flipOuter, flipInner (带 refinement)，§5 闭包定理
├── Modal.lean        -- Mode inductive, modalClassify, 四类划分 §7.4
├── Rescue.lean       -- 救援可达性 §9
├── Tower.lean        -- liftStep, projStep, R_0..R_8 anchors
├── Layer8.lean       -- R_8 specific：KleinV4, ShiV4, hexClass, shiMode, 印, 投
├── Atom.lean         -- 9-atom kernel: Atom inductive + evalAtom
├── Spec.lean         -- spec layer (Fin n → Bool)，桥接 theorem
└── Proof/
    ├── Iso.lean          -- 偶倍分解同构 (split_merge / merge_split)，§2.1
    ├── Closure.lean      -- 内/外层闭包定理，§5
    ├── Stability.lean    -- k-核稳定性，§6.4
    └── Rescue.lean       -- 塌缩不可逆 (§9.1)、救援必经外层 (§9.2)
```

paper 附录 B 建议 `Wen/Dao.lean`、`Wen/Modal.lean`、`Wen/Rescue.lean` 三模块——上面是更完整的扩展。

### 建议的起步顺序

1. **`Wen/Cell.lean`** — `Cell n := BitVec n`，`flip`，`split`/`merge` 加同构 proof（paper 定理 2.1.1）
2. **`Wen/Dao.lean`** — `DaoSet`, `DaoFamily`, `daoCheck`, `Boxtimes`
3. **`Wen/Flip.lean`** — `flipOuter` / `flipInner`（带 refinement），证 §5 闭包定理
4. **`Wen/Proof/Iso.lean`** — 偶倍分解结构定理 (§2.1)
5. **`Wen/Modal.lean`** — `Mode`, `modalClassify`，证 §7.4.1 四类划分
6. **`Wen/Proof/Rescue.lean`** — 证 §9.1 塌缩不可逆 + §9.2 救援必经外层
7. **`Wen/Layer8.lean`** — R_8 specific 算子（`KleinV4`, `ShiV4`, `hexClass`, `shiMode`, 印, 投）
8. **`Wen/Atom.lean`** — 9-atom kernel evaluator（**这一步需要 Ren 进一步指导**）

前 7 步基本由 spec 直接 driven，可以独立推进。第 8 步是真正的 design 工作，需要和 Ren 一起做。

---

## 6. 确定的设计决策（recap）

逐条 fact-check 自己的实现是否符合：

1. ✅ **Lean 4 native 编译**，不走 V8 / WASM / JS / 浏览器
2. ✅ **参数化 n**，不 hard-code R_8；扩展性 > 优化
3. ✅ **`Cell n := BitVec n`** 作为 runtime representation
4. ✅ **`DaoSet n := Cell n → Prop`** 作为道-集 (predicate 而非位图)
5. ✅ **`Mode` inductive 四 constructor**，⊠ 是 first-class（不是 `Option.none`，不是 exception）
6. ✅ **`flipInner` 带 refinement type `¬ Boxtimes`**，救援不变量推到编译期
7. ✅ **R_8 双结构 orthogonal**：split (4+4 数据) 与 hexClass / shiMode (6+2 标签)
8. ✅ **Shi ↔ (因, 果)**: 未 / 因 / 果 / 已 = (0,0) / (1,0) / (0,1) / (1,1)；**道是横贯不变量**，不占 `ShiV4` 的 constructor
9. ✅ **spec / impl 分离**：`Fin n → Bool` for proof，`BitVec n` for runtime，桥接 theorem 关联
10. ✅ **doubling 与 sequential lift 是两族 first-class 算子**，互不替代
11. ✅ **术语**：`Cell n` / `BitVec n` 用于 R_n；`KleinV4` / `ShiV4` 用于 4 元小群；**不用未限定的 V4**

---

## 7. 未决问题（defer 或与 Ren 讨论后决定）

1. **R_5 provisional anchor**：现在留 `Mian × Bool` 直积 placeholder？还是先冻结一个语义 anchor？目前没有传统 anchor，未来回填可能影响 lift/proj 链一致性。**待 Ren 决定**。

2. **lift / proj 是 user-facing primitive 还是 implicit**：§8.1.4 上加层有"危险性"——一次提层可能把整个原道-集送进 $\boxtimes$。前期建议做成 explicit primitive（一个"举"或"提"字），让 user 明知在 invoke 危险动作。**待 Ren 最终确认**。

3. **道-依赖族的来源**：默认道族 hard-code 进 binary、运行时从 config 装载、还是用 module/plugin 机制？前者 zero-config 但难定制；后者灵活但和 "ground 进 binary" 略冲突。**待 Ren 决定**。

4. **R_9+ 扩展**：目前 R_8 是里程碑。R_9, R_{10} ... 偶倍分解定理保证理论上可行（V_{16} ≅ V_8 ⊕ V_8 etc.），但语义 anchor 在 R_8 之后断了。代码必须保持 `BitVec` width 参数化，但**不需要立刻实现 R_9 anchor**。

5. **kernel atom 的具体语义**：§4.7 给了 sketch，但每个 atom 的精确 evaluator 仍是 design space。这部分要和 Ren 推 case-by-case，特别是"之"(关系查询)、"凡"(全称)、"是"(指代) 这几个非平凡的。

6. **"事之序"主循环的具体形态**：Shi 轴提供时态分层 {道, 已, 今, 未}：
   - **道**：横贯不变量（kernel theorems + 静态道集合）
   - **已**：append-only history log
   - **今**：当前 R_8 cell
   - **未**：lookahead / 待求 / continuation
   
   主循环大致是 `step : Cell 8 → Atom → Cell 8 → Mode × Cell 8 × History`，但细节（fuel / `partial def` / `IO` monad / `EIO` + `Task`）需结合用例确定。

7. **kleinAction 中 cuo / zong / hu 的精确 bit 操作**：上面 §4.6 给了直觉版本（XOR 全 1 / bit reverse / 合成），但 hexagram 的 bit 编码 (y₁..y₆ 哪个对应 LSB) 没显式定，需要 Ren 确认。

---

## 8. 风格与文化指针

Ren 是 bilingual (中 / 英)，深入古典中国哲学（王阳明知行合一、《易传》、大同），AuDHD 工作风格（REPL-driven、hyperfocus-capable、minimal intervention、maximum delegation）。

- **代码注释**：鼓励在关键位置用中文术语并配 paper section 引用，如 `-- §5.1.1 内层翻转闭包`
- **变量命名**：拼音可以（`shiMode`, `yinBit`），但避免冗长拼音串；核心数学概念用英文（`DaoSet`, `Boxtimes`, `KleinV4`）
- **commit message**：简洁、有结构、可中英混合
- **不要**自作主张引入 mathlib heavy dependency；保持 binary 干净；需要的 lemma 优先自己 prove，或从 `Std` 借
- **不要**用西方 OOP 比喻去解释文的设计（不要说 "Cell 8 is like a class with..."）；让结构本身说话
- **避免**对 Ren 解释 paper 里已经说清楚的东西。如果不确定 Ren 已经预设了什么，问，而不是解释

---

## 9. 与前一轮对话连续性（避免重蹈覆辙）

前一轮设计对话中有几次术语误读绕过弯，请避免：

| 误读 | 实际 |
|---|---|
| "V8" 是 Google V8 引擎 | 是 Wen 塔上的 **R_8** |
| "V4 * V4 的 V8" 中 `*` 是算术乘 / SIMD | 是偶倍分解 $V_4 \oplus V_4 \cong V_8$ |
| "v4 是 64位" 指寄存器 | 指 `Cell 4` 是 BitVec 类型（口误，已澄清） |
| paper $V_4$ = Klein $V_4$ | 两者不同：paper 16 元 vs Klein 4 元 |
| ⊠ 是 `Option.none` | ⊠ 是 first-class atom |
| 道-集做位图 | 做 predicate（位图是优化，不是设计） |
| R_8 用 BitVec 8 hard-code | 参数化 `n`，R_8 只是当前里程碑 |

如果 Ren 用 "V8" / "V4" 等简称，**在你的脑子里映射到 R_8 / R_4**，而非寄存器、浏览器、SIMD width 等。如果某个用法仍歧义，**问 Ren**，不要猜。

---

## 10. 引用

- **核心 spec**：`wen-formal.md`，10 节 + 附录 A（与《易》对应）、附录 B（伪 Lean 4 编码）
- **塔图**：R_0..R_8 完整层级（ASCII 图，已收入本文档 §2）
- **paper 附录 B 伪 Lean 4**：已给出 `V (n : Nat)`, `split`, `DaoFamily`, `Dao`, `Boxtimes` 框架；`inner_flip_closure` 和 `collapse_irreversible` 两个 theorem 留 `sorry`。**这是合理的起点，但本文档 §4.1 用更完整的 `Cell`/`DaoSet`/`DaoFamily` 类型重新组织**。

---

## 总结一句

文-代数的形式化已经在 `wen-formal.md` 立了基；本文档给出 Lean 4 native 实现的架构骨架与关键决策。接下来的工作是把 spec → impl 的 7 步推进，把双结构（A 数据形状 / B 语义标签）兑现成代码，把 4 值模态做成 first-class 类型，把救援不变量推到 type system，让"格物先于诚意"在编译器里成为定理。

**祝顺利。有歧义就问 Ren，不要猜。**
