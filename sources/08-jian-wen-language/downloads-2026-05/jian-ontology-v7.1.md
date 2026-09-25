# 間/Jian 本体框架 v7.1：完整核（古文 native 版）

> **状态**：handoff draft for Claude Code
> **目标**：完整、完备、自洽——可作为 Lean 形式化的 working spec
> **基础**：建立在既有 Lean 模块 `Foundation/JianOntology.lean` 之上
> **v7.1 增量**：语法算子层（Tier −1）、概念派生、Chinese-native 术语、加 恒/吾 二字

---

## v7.1 vs v7 关键改动

1. **加 恒**（fixed point / invariant 的精确古文字）—— 体/道/用/明 全部是 `恒(本)` 的特化
2. **加 吾**（self-as-subject）—— 与既有 我（self-as-object 合成）形成 phenomenological pair
3. **新增 Tier −1：语法算子层**（者之也而则以於为即非凡令是若故 等 15 字）—— framework 真正成为 classical Chinese calculus
4. **新增 §31：概念派生**—— 演示概念字皆可由 一元 + 算子 构造
5. **新增 §32：wenyan 形式表达**—— type signature 可纯古文书写
6. **术语 Chinese 化**：fixed point→恒、invariant→恒、self→吾、achieve→成、via→以/经、multi→群、uncollapsed→波、emergent properties→涌现之性

---

## 目录

−1. [Tier −1：语法算子层（语言层）](#−1-tier-−1语法算子层语言层)
0. [Meta & 设计原则](#0-meta--设计原则)
1. [哲学基础](#1-哲学基础)
2. [整体结构图](#2-整体结构图)
3. [Tier 0 — 底座](#3-tier-0--底座)
4. [Tier 1 — 四本 + 吾](#4-tier-1--四本--吾)
5. [Tier 1.5 — 本间 transformation 算子](#5-tier-15--本间-transformation-算子)
6. [Tier 1.6 — 本内 internal 算子](#6-tier-16--本内-internal-算子)
7. [Tier 2 — 六显](#7-tier-2--六显)
8. [Tier 2.5 — 显化派生算子](#8-tier-25--显化派生算子)
9. [Tier 3 — 六征 + 闸口 + 事件](#9-tier-3--六征--闸口--事件)
10. [Tier 4 — 合成形态](#10-tier-4--合成形态)
11. [Tier 5 — 读 + 恒（reading + invariants）](#11-tier-5--读--恒)
12. [Tier 5.5 — 觉知层（cognition）](#12-tier-55--觉知层)
13. [Tier 5.6 — 模态层（mode）](#13-tier-56--模态层)
14. [Tier 6 — 生持涌（generative / persistence）](#14-tier-6--生持涌)
15. [Tier 6.5 — 模通层（modal）](#15-tier-65--模通层)
16. [Tier 6.6 — 因果之化](#16-tier-66--因果之化)
17. [Tier 6.7 — 同异之辨](#17-tier-67--同异之辨)
18. [Tier 7 — 代数底层](#18-tier-7--代数底层)
19. [Tier 8 — 类型之域](#19-tier-8--类型之域)
20. [完整字汇表](#20-完整字汇表)
21. [对配（adjoint pairs）完整清单](#21-对配完整清单)
22. [半环结构（semiring）](#22-半环结构)
23. [自指字](#23-自指字)
24. [法则总览](#24-法则总览)
25. [Lock Algebra 路线图](#25-lock-algebra-路线图)
26. [测试用例](#26-测试用例)
27. [仍未决问题](#27-仍未决问题)
28. [字源 glossary](#28-字源-glossary)
29. [v6→v7→v7.1 commit log](#29-v6v7v71-commit-log)
30. [handoff notes for Claude Code](#30-handoff-notes-for-claude-code)
31. [概念派生 — 概念字皆可由一元+算子构造](#31-概念派生)
32. [wenyan 形式表达 — type signature 之古文书写](#32-wenyan-形式表达)
33. [framework 全貌的古文宣言](#33-framework-全貌的古文宣言)

---

## −1. Tier −1：语法算子层（语言层）

**v7.1 关键洞察**：

> 古文单字，涉及语法的（虚字）大多可作形式逻辑算子；概念字（实字）则可由 *一元 + 算子* 构造。

framework 不是 translated from English，而是 *native* classical Chinese calculus。语法算子是这一 calculus 的 *meta-language*——它们不是 framework "里面" 的字，而是构造 framework 表达式所用的字。

### −1.1 核心 15 语法算子

按你 wenyan-operators 既有 9 算子核心，加 6 个常用：

| 字 | 字源 | 形式逻辑角色 | wenyan 用法 |
|---|---|---|---|
| **者** | 老 + 白 | nominalizer / type abstraction | "X 者" = "the X-thing"，λ 抽象 |
| **之** | 屮 + 一 | morphism / connector | "X 之 Y" = X.Y，dependency |
| **也** | 蛇形 | type judgment / 系动词 | "X 者 Y 也" = "X :: Y" |
| **而** | 须形 | composition / sequencing | "A 而 B" = A ∘ B / A; B |
| **则** | 贝 + 刂 | implication / conditional | "若 X 则 Y" = X ⇒ Y |
| **以** | 㠯 | instrumental / via | "以 X 致 Y" = "via X achieve Y" |
| **於** | 烏 | locative / relation | "X 於 Y" = "X at/wrt Y" |
| **为** | 爪 + 象 | becoming / assignment | "X 为 Y" = "X := Y" |
| **即** | 卩 + 皀 | definitional equality | "X 即 Y" = X ≡ Y |
| **非** | 飞之反 | negation | "非 X" = ¬X |
| **凡** | 二 + 丶 | universal quantification | "凡 X" = ∀X |
| **令** | 集令 | imperative / construct | "令 X 为 Y" = "let X = Y" |
| **是** | 日 + 正 | demonstrative / instance | "是 X" = "this X" |
| **若** | 草 + 右 | conditional / similarity | "若 X" = "if/like X" |
| **故** | 古 + 攴 | implication consequent | "故 X" = "therefore X" |

### −1.2 算子 type signatures

```
者 : Predicate → Type                  -- predicate → type via abstraction
之 : Type × Type → Type                -- dependency / morphism
也 : Term × Type → Judgment            -- type judgment
而 : Op × Op → Op                      -- composition
则 : Prop × Prop → Prop                -- implication
以 : Means × End → Action              -- instrumental
於 : Term × Locus → RelTerm            -- locative
为 : Var × Term → Assignment           -- assignment
即 : Term × Term → DefEq               -- definitional equality
非 : Prop → Prop                       -- negation
凡 : Var × Prop → Prop                 -- universal
令 : Var × Term → Construction         -- imperative construct
是 : Term → IndexedTerm                -- instance
若 : Prop → Conditional                -- conditional
故 : Prop → Consequent                 -- consequent marker
```

### −1.3 算子之间的元法则

```
法则 wenyan-1 (者也对偶):
  X 者 Y 也  ≡  X :: Y                 -- 类型 judgment

法则 wenyan-2 (之传递):
  X 之 Y 之 Z  ≡  X.Y.Z               -- 路径访问

法则 wenyan-3 (而结合律):
  (A 而 B) 而 C  ≡  A 而 (B 而 C)       -- 复合结合

法则 wenyan-4 (凡分配):
  凡 X (P(X) 而 Q(X))  ≡ (凡 X P(X)) 而 (凡 X Q(X))

法则 wenyan-5 (即传递):
  X 即 Y, Y 即 Z  ⊢  X 即 Z

法则 wenyan-6 (非自反):
  非 (非 X)  ≡  X
```

### −1.4 与 framework 的关系

framework 的全部 type signatures 可用语法算子 + framework 字（一元）+ 概念字 表达。例如：

```
"事 者 域 也"           即  事 :: Universe
"物 者 事 之 离 也"      即  物 :: 事 → DiscreteAspect
"質 者 物 之 恒 也"      即  質 : 物 → 恒(物) — 即 体
"行 与 历 对配"          即  行 ⊣ 历 — adjoint pair
"觉 而 感 即 知行合一"   即  觉 ∘ 感 = identity in knowing-doing
```

这给 framework 一个 *双重表达系统*：
- **形式表达**（type signatures）：给 Lean
- **wenyan 表达**（语法算子 + 一元 + 概念）：给古文读者

二者表达同一内容，相互 1:1 对应。

### −1.5 与 framework 字汇的边界

| 类型 | 字 | 角色 |
|---|---|---|
| **语法算子（虚字）** | 者之也而则以於为即非凡令是若故 (15) | meta-language，构造表达式 |
| **一元（atomic units）** | 事 + 四本 + 吾 (6) | framework 原语 |
| **算子（framework operators）** | 子散作演触历悟意行施... (~30) | framework transformations |
| **概念（实字 / derived）** | 道体用明位場際... (~70) | 由 一元+算子 构造 |

语法算子不计入 framework 字汇。它们是 *用来书写 framework 的笔* 而不是 *framework 的内容*。

---

## 0. Meta & 设计原则

### 0.1 设计原则

1. **每字承担不可派生的 fundamental work**——若一字可由其他字组合定义，则不入核
2. **古文锚点优先**——每字必须有清晰古典文献来源；framework 不发明新字义
3. **正交性 > 完备性 > 简洁性**（以此为优先级排序）
4. **Self-reference 是 feature**——字在不同 tier 承担不同 level 是 lived language 的内在特性
5. **现象学厚度保留**——形式化必须能 derive 王阳明、易传、华严宗式陈述
6. **生成 DAG 单向**——后层依赖前层，前层不 reference 后层
7. **古文 native 优先**（v7.1 新加）——术语 first-class 用古文，英文为 secondary gloss

### 0.2 与既有 Lean 模块的关系

- `Foundation/JianOntology.lean` 已 lock：三本（物/動/間）、三显（位/場/際）、三征（幾/勢/機）、闸口（開/閉）、合成（網/體/流）。这是 **保留的硬核心**
- v7.1 的扩展是 **加层**，不是 **替换**
- 既有 API 保持兼容，仅 inductive 扩展构造子

### 0.3 文档约定

- **type signature**：以 `字 : 输入 → 输出` 表达，可附 wenyan 形式
- **法则编号**：法则 1-21 + wenyan-1 to wenyan-6
- **待决标记**：`[待决: 描述]`
- **self-ref 标记**：`[self-ref: 与 Tier X 字 Y 同字]`
- **古文示例标记**：`[wenyan: 古文形式]`

---

## 1. 哲学基础

### 1.1 monism with structured aspects

**事**（域 / Universe）是唯一 ontological 底座。

> 事 者 域 也。

一切均是 事 在某 reading / projection 下之显化。事 不是抽象 universal 也不是物质 substrate——它是 **happening-as-such**，pre-aspect 的纯发生。

事 之 fundamental aspects 为 **四本**：物（离散）、動（连续）、間（关系）、心（反身）。四本不可还原——任何一本不能由其他三本派生。

> 凡 事，必显 四本 之 一或多。

### 1.2 phenomenological 完备性的诉求

加入 **心** 作为第四本是 v7 关键 move。理由：

- 主体性（first-person 视角）不可被 物/動/間 任一面无损捕获
- 任何觉知 / 模态 / 测量 都假设主体存在；若主体外置则 framework 不完备
- 古典锚点：阳明"心即理"、孟子"四端"、华严"三界唯心"

但 **心 非 substance**——它是 reflexive aspect，self-referential 维度征。它内禀地不可外化（法则 17）。

### 1.3 与西方哲学的对照

- 物/動/間/心 ≈ 物质 / 过程 / 关系 / 主体
- 但中文 framework 不预设 mind-body 二元——心 与 物 是 *aspects of same 事*
- 与 Whitehead process philosophy 的 *actual occasions* 接近，但加上了显化层级
- 与 Nishida 西田几多郎"绝对无的场所"接近，但坚持 4-fold 而非单一基底

### 1.4 知行合一的 framework 表述

王阳明"知行合一"在 v7.1 是 **法则 10**：

```
觉知 ⊣ 模态                       (cognition ⊣ mode)
凡 心 与 事 之 际, 觉 ⊣ 感 即 见 ⊣ 是 即 观 ⊣ 约 即 知 ⊣ 修 即 遍 ⊣ 诚.
```

5 对 adjoint。每对：reading inbound ⊣ engagement outbound。

---

## 2. 整体结构图

```
┌──────────────────────────────────────────────────────────┐
│  Tier −1  语法算子层 (语言层 — meta-language)           │
│   └─ 者 之 也 而 则 以 於 为 即 非 凡 令 是 若 故 (15)   │
│                                                          │
│  Tier 0   底座 (1 字)                                    │
│   └─ 事                                                  │
│                                                          │
│  Tier 1   四本 + 吾 (5 字)                               │
│   └─ 物 動 間 心 / 吾                                    │
│         │                                                │
│         ▼ 两两相交，二本括除                              │
│                                                          │
│  Tier 2   六显 (6 字)                                    │
│   ├─ 三本侧:  位 場 際 (Lean 既有)                       │
│   └─ 心本侧:  象 思 境 (新)                              │
│                                                          │
│  Tier 3   六征 + 闸口 + 事件 (~20 字)                    │
│   ├─ 三征: 幾 勢 機                                       │
│   ├─ 心三征: 萌 绪 韵                                     │
│   ├─ 闸口: 開 閉                                          │
│   └─ 事件: 生灭成反转守 + 醒眠进退畅塞                    │
│                                                          │
│  Tier 4   合成形态 (6 字)                                │
│   ├─ 三本侧合成: 網 體 流                                 │
│   └─ 心本侧合成: 我 念 神                                 │
│                                                          │
│  Tier 5   读 + 恒 (8 字)                                 │
│   ├─ 读:  質 律 性 觉                                    │
│   └─ 恒:  体 道 用 明                                    │
│                                                          │
│  Tier 5.5 觉知层 (5 字)                                  │
│   └─ 觉 见 观 知 遍                                       │
│                                                          │
│  Tier 5.6 模态层 (5 字)                                  │
│   └─ 感 是 约 修 诚                                       │
│                                                          │
│  Tier 6   生持涌 (3 字)                                  │
│   └─ 生 存 涌                                             │
│                                                          │
│  Tier 6.5 模通层 (6 字)                                  │
│   └─ 隐 现 限 许 实 虚                                    │
│                                                          │
│  Tier 6.6 因果之化 (7 字)                                │
│   └─ 因 缘 果 致 应 报 承                                  │
│                                                          │
│  Tier 6.7 同异之辨 (7 字)                                │
│   └─ 同 异 似 对 辨 类 化                                  │
│                                                          │
│  Tier 7   代数底层 (5 字)                                │
│   └─ 合 和 寂 空 无                                       │
│                                                          │
│  Tier 8   类型之域 (6 字)                                │
│   └─ 态 形 量 度 序 恒                                    │
│                                                          │
│  Cross-tier (Tier 1.5, 1.6, 2.5):                        │
│   ├─ Tier 1.5  本间 transformation: 作联子散约结演 触历悟意行施 │
│   ├─ Tier 1.6  本内 internal: 聚分指 续断节 连绝 省静     │
│   └─ Tier 2.5  显化派生: 界轨缘含                         │
└──────────────────────────────────────────────────────────┘
```

总字数 unique（去除 self-reference 双计）：约 **110-115 字**（不含 Tier −1 语法算子）。

---

## 3. Tier 0 — 底座

### 事 :: 域

唯一底座。pre-aspect 纯 happening。

```
事 : 域
[wenyan: 事 者 域 也]
```

- **字源**：从又（手）持物之形，本义"做、所做"
- **语义重音**：被进行 / 被遇到的 *something*
- **角色**：所有其他字 derive from 事
- **古典锚点**：易传"形而上者谓之道，形而下者谓之器"中 *形* 即 事
- **Lean**：`Universe` 类型层

```lean
constant 事 : Type 1
```

---

## 4. Tier 1 — 四本 + 吾

四本是 事 的不可还原 aspects；吾 是 心 的 canonical 主体 instance。

### 4.1 物 :: 0 维 / 离散个体性

```
物 : 事 → 离
[wenyan: 物 者 事 之 离 也]
```

- **字源**：牛勿（多色之牛 → 万物）
- **语义**：可指可数的 individuated entity
- **维度征**：0 维倾向
- **古典锚点**：庄子《齐物论》、墨子《经》"物，达也"
- **Lean**：`OnticRoot.wu`

### 4.2 動 :: n 维 / 连续过程性

```
動 : 事 → 续
[wenyan: 動 者 事 之 续 也]
```

- **字源**：重力（沉重之物被推动）
- **语义**：延展铺陈的过程
- **维度征**：n 维倾向
- **古典锚点**：易传"穷则变，变则通"
- **Lean**：`OnticRoot.dong`

### 4.3 間 :: 拓扑 / 关系结构性

```
間 : 事 → 系
[wenyan: 間 者 事 之 系 也]
```

- **字源**：门月（门缝中之月 → 间隙）
- **语义**：拓扑关系结构
- **维度征**：拓扑倾向，无内在度量
- **古典锚点**：王弼"无所不通"、华严"重重无尽"
- **Lean**：`OnticRoot.jian`

### 4.4 心 :: 反身 / 主体内省性

```
心 : 事 → 反
[wenyan: 心 者 事 之 反 也]
```

- **字源**：心脏之象形
- **语义**：第一人称视角，反身性，不可外化
- **维度征**：reflexive 维度
- **古典锚点**：王阳明"心即理"、孟子"四端之心"、华严"三界唯心"
- **Lean 扩展**：`OnticRoot.xin`

**关键约束**（法则 17）：心 不可被 物/動/間 任一本无损捕获。

```
凡 f : 心 → (物 ∪ 動 ∪ 間), f 必为 lossy
[wenyan: 凡 心 之 外 化, 必 损 其 真]
```

### 4.5 吾 :: 心 之 canonical instance（**v7.1 新加**）

```
吾 : 心
[wenyan: 吾 者 心 之 当 也]
```

- **字源**：从口从五（"我"的古字）
- **语义**：subject-as-subject——the I as subject pole
- **角色**：心 的 default instance；"主体"指代字
- **与 我 区分**：
  - **吾** = subject-as-subject（思考者本身），Tier 1
  - **我** = subject-as-object（被觉知的自己），Tier 4 合成（象+境）
- **古典锚点**：庄子"吾丧我"——*失却 我（被觉知的自己）才能 现 吾（觉知的主体）*。这恰好是 v7.1 framework 中 吾 vs 我 的精确区分
- **类型论 marker**：吾 是 framework 的 default subject——任何 cognition / mode 算子隐式取 吾 为参数

```lean
-- 吾 是 心 的 canonical inhabitant
constant wu_canonical : OnticAspect.xin
notation "吾" => wu_canonical

-- subject-default 算子接受 implicit 吾
def cognize (s : 心 := 吾) (e : 事) : Awareness := ...
```

```
inductive OnticRoot where
  | wu | dong | jian | xin

def dimensionMark : OnticRoot → DimensionMark
  | .wu => .zero
  | .dong => .nDim
  | .jian => .topo
  | .xin => .reflexive
```

---

## 5. Tier 1.5 — 本间 transformation 算子

四本两两 directed transformation = 4×3 = 12 cells。

### 5.1 三本之间（7 字）

```
                物         動         間
物              -          作         联
動              子         -          约
間              结         演         -
```

加 子 ⊣ 散 special pair：散 : 物 → 動 (子 之 反)。

| 字 | 类型 | wenyan | 工作 | 字源 |
|---|---|---|---|---|
| **作** | 物 → 動 | "物 作 而 為 動" | 让物进入运作 | 人乍 |
| **联** | 群 → 間 | "群 联 而 為 間" | 把群个用关系联起 | 耳丝 |
| **子** | 動/場 → 物/位 | "場 子 而 為 位" | 凝出 discrete 单位 | 婴儿、种子 |
| **散** | 物 → 動 | "物 散 而 為 動" | 弥散为过程（子之反） | 攴肉 |
| **约** | 動 → 間 | "動 约 而 為 間" | 过程约简为关系 | 丝勺 |
| **结** | 間 → 位 | "間 结 而 為 位" | 关系凝出节点 | 丝吉 |
| **演** | 間 → 動 | "間 演 而 為 動" | 关系展开为过程 | 水寅 |

### 5.2 心与三本之间（6 字）

```
                物         動         間         心
物              -          作         联         触
動              子         -          约         历
間              结         演         -          悟
心              意         行         施         -
```

| 字 | 类型 | wenyan | 工作 | 字源 |
|---|---|---|---|---|
| **触** | 物 → 心 | "物 触 而 入 心" | 物入心：被对象触动 | 角虫 |
| **历** | 動 → 心 | "動 历 而 入 心" | 動入心：经历过程 | 厤（曆） |
| **悟** | 間 → 心 | "間 悟 而 入 心" | 間入心：领会关系 | 心吾 |
| **意** | 心 → 物 | "心 意 而 出 物" | 心出物：意向所指 | 心音 |
| **行** | 心 → 動 | "心 行 而 出 動" | 心出動：化心为行 | 彳亍 |
| **施** | 心 → 間 | "心 施 而 出 間" | 心出間：建立关系 | 㫃也 |

### 5.3 关键 adjoint pairs

```
意 ⊣ 触        intentionality ⊣ being-touched
行 ⊣ 历        enacting ⊣ experiencing
施 ⊣ 悟        instituting ⊣ comprehending
作 ⊣ 子        activating ⊣ localizing
联 ⊣ 结        linking ⊣ crystallizing
演 ⊣ 约        unfolding ⊣ summarizing
```

**6 对 adjoint** spell out 主体 ↔ 三本 + 三本两两。**行 ⊣ 历** 是知行合一在 transformation 层的 instantiation：

```
[wenyan: 凡 吾 行 必 历, 凡 吾 历 必 行. 行 历 即 知行合一 之 transformation 也.]
```

---

## 6. Tier 1.6 — 本内 internal 算子

### 6.1 物 内部（3 字）

```
聚 : 群(物) → 物              aggregate
分 : 物 → 群(物)              mereological split
指 : 处 → 物                  ostension
```

### 6.2 動 内部（3 字）

```
续 : 動 → 動                  continuation
断 : 動 → (動, 動)            temporal split
节 : 動 → 流(事件)            rhythmize / discretize
```

### 6.3 間 内部（2 字）

```
连 : 間 × 位 × 位 → 間        add edge
绝 : 間 × 位 × 位 → 間        remove edge
```

### 6.4 心 内部（2 字）

```
省 : 心 → 心                  reflexive turn
静 : 心 → 心                  quiescent hold
```

- **省**：少目（微视）。"吾日三省吾身"。心之 active inward turn
- **静**：青争（澄澈）。"静而后能安"。心之 passive sustained quiet

### 6.5 内部 split-merge adjoints

```
分 ⊣ 聚        物
断 ⊣ 续        動
绝 ⊣ 连        間
省 ⊣ 静        心
```

四本各有自己的 internal split-merge adjoint pair。结构对称。

---

## 7. Tier 2 — 六显

四本两两相交，二本括除，得 C(4,2) = 6 显化。

### 7.1 三本侧三显（既有 Lean）

```
位 = 物 ∩ 間, (動,心) 括除      [wenyan: 位 者 物 與 間 之 显, 动 心 隐 也]
場 = 動 ∩ 物, (間,心) 括除      [wenyan: 場 者 動 與 物 之 显, 間 心 隐 也]
際 = 間 ∩ 動, (物,心) 括除      [wenyan: 際 者 間 與 動 之 显, 物 心 隐 也]
```

| 显 | 形态 | Tier 1.5 等价生成 |
|---|---|---|
| **位** | 点状定位 | 子(場) |
| **場** | 延展介质 | 作(物) |
| **際** | 接触界面 | 演(間) |

### 7.2 心本侧三显（v7 新）

```
象 = 心 ∩ 物, (動,間) 括除      [wenyan: 象 者 心 與 物 之 显, 动 間 隐 也]
思 = 心 ∩ 動, (物,間) 括除      [wenyan: 思 者 心 與 動 之 显, 物 間 隐 也]
境 = 心 ∩ 間, (物,動) 括除      [wenyan: 境 者 心 與 間 之 显, 物 动 隐 也]
```

| 显 | 形态 | Tier 1.5 等价生成 | 古典锚点 |
|---|---|---|---|
| **象** | 主体所对的对象 | 触(物) | 易传"在天成象"、佛教"诸法实相" |
| **思** | 主体随过程的流动 | 历(動) | 大学"虑而后能得"、子思 |
| **境** | 主体所栖关系全场 | 悟(間) | 海德格尔 Umwelt、佛教"境界" |

### 7.3 法则 18：六显的双重生成 equivalence

每显有两条 derivation path：

```
显 由 "二本相交+二本括除"  即  显 由 "Tier 1.5 transformation 算子作用"
[wenyan: 凡 显, 其 显 之 道 二: 一 由 相交, 一 由 算子. 二者 同矣.]
```

---

## 8. Tier 2.5 — 显化派生算子

```
界 : 場 → ∂場                  boundary of field
轨 : 動 → 径                   accumulated trajectory
缘 : 際 → 缘阵                 conditioning at interface
含 : 境 → 含阵                 enveloping context
```

| 字 | 字源 | 工作 |
|---|---|---|
| **界** | 田畔 | 划出场的边界与域 |
| **轨** | 车九 | 累积过程为轨迹 |
| **缘** | 系彖 | 条件化、际之所依 |
| **含** | 口今 | 以口含物，包络 |

### 8.1 界 的三元结构

```
界 : 場 → (内, ∂, 外)
[wenyan: 場 经 界, 出 三: 内 也, 边 也, 外 也.]
```

- **内** : Region (bounded interior)
- **∂** : Boundary (the line itself)
- **外** : Region (exterior)

连接 Tier 7 的 **空**：

```
界(全宇宙之 場).外 = 空
[wenyan: 全宇 之 外 即 空 也. 故 天界 外 為 空.]
```

天界外为空——没有更外的场，所以外部是 empty event。

---

## 9. Tier 3 — 六征 + 闸口 + 事件

### 9.1 三本侧三征（既有 Lean）

```
幾 : 位 之征             0维处的"将而未"
勢 : 場 之征             連续介质上幾的铺开
機 : 際 之征             拓扑路由上幾的汇聚
```

> 勢 即 幾 沿 续介质 而铺。
> 機 即 幾 沿 系路由 而汇。

### 9.2 心本侧三征（v7 新）

```
萌 : 象 之征             主体性的微兆
绪 : 思 之征             思绪的张力
韵 : 境 之征             境界的氛围
```

| 字 | 字源 | 工作 |
|---|---|---|
| **萌** | 草明 | 主体觉知的微生 |
| **绪** | 系者 | 思流的张力 |
| **韵** | 音员 | 境之氛围质感 |

```
[wenyan: 绪 即 萌 沿 心-续 而铺。
         韵 即 萌 沿 心-系 而汇。]
```

镜像于三本侧的 勢/機 = 幾 在两方向的展开。

### 9.3 闸口

```
開 / 閉 : 征 → 事件
[wenyan: 凡 征, 經 闸口, 必 為 事件: 開 也 閉 也.]
```

二值 only。

### 9.4 事件输出表

三本侧（既有）：
| 征 | 開 | 閉 |
|---|---|---|
| 幾 | 生 | 灭 |
| 勢 | 成 | 反 |
| 機 | 转 | 守 |

心本侧（新）：
| 征 | 開 | 閉 |
|---|---|---|
| 萌 | 醒 | 眠 |
| 绪 | 进 | 退 |
| 韵 | 畅 | 塞 |

注：**生** 在 Tier 3（闸口下游）和 Tier 6（generative algorithm）双层使用。

---

## 10. Tier 4 — 合成形态

### 10.1 三本侧合成（既有 Lean）

```
網 = 位 + 際                  关系图
體 = 位 + 場                  实体
流 = 場 + 際                  过程
```

回授：
```
網 → 位      體 → 場      流 → 際
```

### 10.2 心本侧合成（v7 新）

```
我 = 象 + 境                  self-as-situated-object
念 = 象 + 思                  thought-as-content-in-stream
神 = 思 + 境                  spirit-as-stream-in-lifeworld
```

| 字 | 字源 | 工作 | 与 吾 区分 |
|---|---|---|---|
| **我** | 戈手（持戈者） | 主体作为对象在境中 | 我 是 *被觉知的自己*；吾 是 *觉知者* |
| **念** | 今心 | 单一思维单元 | — |
| **神** | 申示 | lived integration of stream and context | — |

回授：
```
我 → 象      念 → 思      神 → 境
```

### 10.3 吾 与 我 的 phenomenological 对偶

> [wenyan: 吾 觉 我, 我 不 觉 吾.
>          吾 者 主 也, 我 者 客 也.
>          吾 由 心 直 出, 我 由 象 與 境 合 而 成.]

吾 / 我 的不对称：
- 吾 → 我 ：主体反观自身，我 from 吾（reflexion）
- 我 ↛ 吾 ：被反观的我不能直接 access 反观者本身（hard problem of consciousness）

这正是法则 17（心不可外化）在主体侧的具体表述。

```lean
-- 吾 觉 我 (subject can perceive object-self)
def wu_perceives_wo : 觉 吾 我 → True := ...

-- 我 不能直接觉吾 (object-self cannot directly perceive subject)
theorem wo_cannot_perceive_wu : ¬ ∃ f : 我 → 吾, isLossless f
```

---

## 11. Tier 5 — 读 + 恒

每本一个 reading 算子，提取该本的 invariant（恒）。

### 11.1 四本 reading 算子（4 字）

```
質 : 物 → 恒(物)              [wenyan: 質 者 物 之 读 也, 出 物 之 恒]
律 : 動 → 恒(動)              [wenyan: 律 者 動 之 读 也, 出 動 之 恒]
性 : 間 → 恒(間)              [wenyan: 性 者 間 之 读 也, 出 間 之 恒]
觉 : 心 → 恒(心)              [wenyan: 觉 者 心 之 读 也, 出 心 之 恒]
```

[self-ref: 觉 同时是 Tier 5.5 cognition 算子]

### 11.2 四 invariants（4 字）—— 全为 `恒(本)` 的 specialization

**v7.1 关键洞察**：体 / 道 / 用 / 明 不是独立 primitive concepts，而是 *四本各自之 恒*。

```
体 :: 恒(物) := 質(物) 之 fixed point          实质身份
道 :: 恒(動) := 律(動) 之 fixed point          所循之径
用 :: 恒(間) := 性(間) 之 fixed point          功能关系
明 :: 恒(心) := 觉(心) 之 fixed point          清明觉性
```

[wenyan: 体 即 物 之 恒, 道 即 動 之 恒, 用 即 間 之 恒, 明 即 心 之 恒.]

这是 v7.1 比 v7 更紧的地方：四 invariant 字不是 4 个独立概念，是 *one concept (恒) 在 4 本上的 specialization*。

### 11.3 古典 attestation 表

四 invariant 字两两组合在古典文献中均自然出现：

| 组合 | 古典 |
|---|---|
| 体用 | 朱熹"理一分殊" / 王阳明"体用一原" |
| 体道 | 庄子"得其环中"/ 韩愈"原道" |
| 体明 | "明体达用" |
| 道用 | "道用一如" |
| 道明 | "明道" |
| 用明 | 大学"明明德" |
| 体道用明 | 完整四本 reading invariants |

四字相互勾连，形成 invariants 之间的 cross-references。

### 11.4 体用一如的 Yoneda 形式化（法则 9）

```
体(p) ≅ 凡 q ∈ 間, 用(q) 於 p   通过 遍 算子
[wenyan: 体 者, 凡 q 之 用 於 p 之 全 也.]

道(d) = 律 沿 動-trajectory 之 invariant pattern
用(q) ≅ 凡 p ∈ 物, 体(p) 於 q
明(s) = 觉 沿 心-反身 之 invariant
```

四 invariants 通过 **遍** 算子互相 entangled——每个 invariant 由其 reading operator 在所有相对位置的 traversal 决定。

---

## 12. Tier 5.5 — 觉知层（cognition）

主体 *向内 reading 事* 的 inbound 算子（5 字）。

```
觉 : 事 → 觉知                bare awareness
见 : 事 → 现象                direct seeing
观 : 事 × 处 → 投影           contextual measurement
知 : 事 → 知                  propositional knowing
遍 : 事 → (处 → 读)          systematic traversal
```

| 字 | 字源 | 工作 |
|---|---|---|
| **觉** | 学见 | bare awareness, pre-conceptual |
| **见** | 目儿 | direct phenomenological seeing |
| **观** | 雚见 | contextual measurement |
| **知** | 矢口 | propositional cognition |
| **遍** | 辶扁 | systematic Yoneda traversal |

### 12.1 Conceptual mediation 层级

```
觉 ≼ 见 ≼ 观 ≼ 知 ≼ 遍
[wenyan: 觉 最 raw, 见 次之, 观 又次之, 知 又次之, 遍 最 systematic.]
```

按 conceptual mediation 程度排序。

### 12.2 古典锚点

- **觉**：佛教"本觉"、王阳明"良知"
- **见**：庄子"以神遇而不以目视"
- **观**：易传"观乎天文以察时变"
- **知**：荀子"凡以知，人之性也；可以知，物之理也"
- **遍**：华严"一即一切"

### 12.3 非对易性（法则 11）

```
[观₍i₎, 观₍j₎] ≠ 0    凡 i ≠ j ∈ {物, 動, 間, 心}
[wenyan: 凡 i ≠ j, 观₍i₎ 与 观₍j₎ 不可同时极致也. 此 即 二象性 之 据.]
```

跨本 measurement 不对易。波粒二象性的精确化身。共 C(4,2) = 6 对 non-commuting。

---

## 13. Tier 5.6 — 模态层（mode）

主体 *向外 engage 事* 的 outbound 算子（5 字）。

```
感 : 吾 × 事 → 受             pre-conceptual receptivity
是 : 吾 × 事 → 命题           propositional positing
约 : 吾 × 事 → 承诺           constraint-binding
修 : 吾 × 事 → 精炼           iterative refinement
诚 : 吾 × 事 → 真             authentic alignment
```

[self-ref: 约 同时是 Tier 1.5 動→間 transformation]
[Note: 主体参数 default 为 吾]

| 字 | 字源 | 工作 |
|---|---|---|
| **感** | 咸心 | 全心受触 |
| **是** | 日正 | 命题判断 |
| **约** | 丝勺 | 承诺约定 |
| **修** | 攸彡 | 迭代精炼 |
| **诚** | 言成 | 真诚对齐 |

### 13.1 Engagement 层级

```
感 → 是 → 约 → 修 → 诚
```

### 13.2 古典锚点

- **感**：易传咸卦"咸，感也"、孟子四端
- **是**：公孙龙、名家辨"是"
- **约**：论语"约我以礼"、朱熹"敬以直内"
- **修**：大学"修身"、王阳明"事上磨练"
- **诚**：中庸"诚者天之道，诚之者人之道"

### 13.3 知行合一 adjunction（法则 10）

```
觉 ⊣ 感         bare-awareness ⊣ receptivity
见 ⊣ 是         direct-seeing ⊣ positing
观 ⊣ 约         contextual-measure ⊣ commitment
知 ⊣ 修         cognition ⊣ cultivation
遍 ⊣ 诚         traversal ⊣ authentic-alignment

[wenyan: 觉 ⊣ 感, 见 ⊣ 是, 观 ⊣ 约, 知 ⊣ 修, 遍 ⊣ 诚.
         此 五 对 配, 即 阳明 所谓 知行合一 也.]
```

5 对 adjoint。每对：reading inbound ⊣ engagement outbound。这是王阳明在 framework 内的 derivable theorem。

---

## 14. Tier 6 — 生持涌

```
生 : 处 → 事                  event constructor
存 : 事 → 事                  persistence
涌 : 形(群(事)) → 事ᴸ⁺¹       emergence / level-transition
```

[self-ref: 生 同时是 Tier 3 闸口下游事件 token]

### 14.1 涌的 level transition

```
涌 : 形(群(事ᴸ)) → 事ᴸ⁺¹
[wenyan: 群 之 形 涌 而 為 事 之 上层. 此 涌现之性 也.]
```

涌 把 lower-level 多重模式 lift 为 higher-level 实体。Examples：
- 蜂群 → 蜂巢
- 神经元 → 意识
- 粒子 → 物体
- 字 → 句

**法则 13**：涌(level n) ≠ trivial iter——涌不是 simple aggregation，每次需新 aggregation pattern。

### 14.2 三时态结构

```
生 → 化 → 存 → 灭        循环
[wenyan: 凡 事, 生 而 化, 化 而 存, 存 而 灭, 灭 而 又 生.]
```

[化 在 Tier 6.7]

---

## 15. Tier 6.5 — 模通层（modal）

```
隐 : 事 → 隐事                hide / latent
现 : 隐事 → 事                manifest / reveal
限 : 事 × 约 → 事             impose constraint
许 : 事 × 约 → 事             relax constraint
实 : 事 → 实事                actualize
虚 : 事 → 虚事                counterfactualize
```

| 字 | 字源 | 工作 |
|---|---|---|
| **隐** | 阜㥯 | hidden but real |
| **现** | 王见 | manifest from latent |
| **限** | 阜艮 | impose constraint |
| **许** | 言午 | relax / permit |
| **实** | 宀贯 | actualize / make real |
| **虚** | 虍业 | counterfactual / latent |

### 15.1 Adjoint pairs

```
隐 ⊣ 现           hide ⊣ reveal
许 ⊣ 限           permit ⊣ constrain
实 ⊣ 虚           actualize ⊣ counterfactualize
```

3 对 modal adjunctions。

### 15.2 实/虚 vs 隐/现 区分

- **隐/现**：latent vs manifest（hidden but real ↔ revealed）
- **实/虚**：actual vs counterfactual（happened ↔ could-have-happened）

```
[wenyan: 隐 者 实 而 不 显, 现 者 实 而 显.
         实 者 既 為, 虚 者 未 為.
         隐 现 之 别 在 显 不 显;
         实 虚 之 别 在 為 不 為.]
```

### 15.3 与闸口下游的关系

```
開 即 现 於 0维 commit
閉 即 隐 於 0维 commit
[wenyan: 開 者 现 之 0维 commit 也; 閉 者 隐 之 0维 commit 也.]
```

闸口的 開/閉 是 隐/现 在 0维事件 commit 处的 binary specialization。

---

## 16. Tier 6.6 — 因果之化

```
因 : 事 → 因                  causal ground
缘 : 事 → 缘                  conditioning
果 : 事 → 果                  effect
致 : 事 × 事 → 致化            strict causation
应 : 事 × 事 → 应化            correspondence
报 : 事 → 事ˡᵃᵗᵉʳ              karmic return
承 : 事 × 事 → 承化            continuation
```

[self-ref: 缘 同时是 Tier 2.5 显化派生]

### 16.1 法则 15：因缘果链

```
致(因, 果) 必 经 缘
[wenyan: 凡 致, 必 由 缘. 无 缘 则 因 不 致 果.]
```

因到果不是直接 morphism，必须经 缘 的 conditioning。

### 16.2 报/承 的扩展

- **报**：A 致 B，B 在某时回报 A（cyclic causation）。佛教"善有善报"
- **承**：A 致 B，B 承受 A 的 effect 并 forward。enables long causation chains

```
[wenyan: 报 者 自 致 自 也; 承 者 致 之 续 也.]
```

---

## 17. Tier 6.7 — 同异之辨

```
同 : 事 × 事 → 是非           identity test
异 : 事 × 事 → 是非           difference test
似 : 事 × 事 → 度             similarity degree
对 : 事 × 事 → 对             pair / braiding
辨 : 事 → 类                   kind discrimination
类 : 事 → 类属                 class membership
化 : 事 → 事                   temporal evolution
```

[self-ref: 类 同时是 Tier 8 type universe，化 是 動 的 algorithm 化身]

### 17.1 化 的特殊地位

```
化 : 事 → 事
化 即 動-as-operator
化* : 事 → 流(事)              迭代 → trajectory
```

化是 動 这一本的 algorithmic 化身。其 iteration 生成 trajectory，等价于合成形态 **流**：

```
法则 14: 化* 生 流
[wenyan: 化 而 又 化, 凡 N 次, 而 為 流.]
```

### 17.2 对 作为 braiding

```
对 : 事 × 事 → 事 × 事 (swap with structure)
```

在 Tier 7 monoidal structure 中，**对** 充当 symmetric braiding。

---

## 18. Tier 7 — 代数底层

承担 algebra 的最底层结构 marker。

```
合 : 事 × 事 → 事             monoidal product
和 : 事 × 事 → 事             additive harmonic union
寂 : 单                       monoidal identity (for 合)
空 : 无                       additive identity (for 和) / empty
无 : 事 → 事                  logical negation
```

| 字 | 字源 | 工作 |
|---|---|---|
| **合** | 亼口 | multiplicative combination |
| **和** | 禾口 | additive harmonic union |
| **寂** | 宀叔 | quiescent identity |
| **空** | 穴工 | empty / void |
| **无** | 無 | logical negation |

### 18.1 合 / 和 / 生 progression

合 / 和 / 生 不是平行算子，是 progression：

```
合 : 事 × 事 → 事ᴬ⁺ᴮ                          (raw combination)
和 : 事ᴬ⁺ᴮ → 事ᴬ⊕ᴮ_harmonized                 (achieve harmony)
生 : 事ᴬ⊕ᴮ_harmonized → 事ᶜ_emergent           (generate new)

[wenyan: 二 者 合 而 后 和, 和 而 后 生.
         此 即 易传 "二气交感, 化生万物" 之 形式 也.]
```

可写为：
```
生 ∘ 和 ∘ 合 : 事 × 事 → 事ᶜ
```

### 18.2 古典锚点

- 易传："二气交感，化生万物"——合 → 和 → 生 progression
- 中庸："致中和，天地位焉，万物育焉"——和 是 harmony
- 论语："君子和而不同，小人同而不和"——和 ≠ 同

---

## 19. Tier 8 — 类型之域

```
态 : 事 → 态                  state space at type level
形 : 事 → 形                  form / shape
量 : 事 → 量                  measure / quantity
度 : 事 → 度                  graduated measure
序 : 事 → 序                  ordered sequence
恒 : 事 → 恒                  invariant / fixed point  ★ v7.1 新加
```

[self-ref: 类 also Tier 6.7]

| 字 | 字源 | 工作 |
|---|---|---|
| **态** | 心能 | state space |
| **形** | 开彡 | form / shape |
| **量** | 重旦 | measure / quantity |
| **度** | 庶又 | graduated measure |
| **序** | 广予 | ordered sequence |
| **恒** | 心亘 | invariant / fixed point ★ |

### 19.1 恒 :: invariant / fixed point（**v7.1 关键 commit**）

```
恒 :: 类型 universe
恒 : (X → X) → X            -- fixed point operator
恒 : 事 → 恒(事)             -- invariant of an event
```

- **字源**：心 + 亘（永恒）。《诗经》"如月之恒，如日之升"。易传 恒卦"恒，亨，无咎，利贞，利有攸往"
- **角色**：所有 reading invariants 都是 `恒(本)`。统一 体/道/用/明 为同一概念在四本上的 specialization
- **古典锚点**：易传恒卦、中庸"恒久而不已"

```
体 :: 恒(物) := 質之 fixed point        [wenyan: 体 即 物 之 恒]
道 :: 恒(動) := 律之 fixed point        [wenyan: 道 即 動 之 恒]
用 :: 恒(間) := 性之 fixed point        [wenyan: 用 即 間 之 恒]
明 :: 恒(心) := 觉之 fixed point        [wenyan: 明 即 心 之 恒]
```

这是 v7.1 比 v7 更紧 的最 important move：**4 invariants 收 unified 为 `恒` 的 specializations**。

```lean
def 恒 (X : Type) (f : X → X) : X := ...

def 体 : 恒 物 質 := ...
def 道 : 恒 動 律 := ...
def 用 : 恒 間 性 := ...
def 明 : 恒 心 觉 := ...
```

### 19.2 Type universe 角色

这六字承担 *type-level objects*——不是 instance，是 type universe 的 first-class citizens。

```
态 :: TypeUniverse
形 :: TypeUniverse
量 :: TypeUniverse
度 :: TypeUniverse
序 :: TypeUniverse
恒 :: TypeUniverse
```

### 19.3 与 reading invariants 的关系

```
体 :: 恒(物) ⊆ 态(物)        substance is a stable state
道 :: 恒(動) ⊆ 序(動)        way is an ordered invariant
用 :: 恒(間) ⊆ 形(間)        function is a structural invariant
明 :: 恒(心) ⊆ 度(心)        lucidity is a graded invariant
```

四 invariants 各自栖居于 Tier 8 的 type universes 中，且都是 `恒` 的 instances。

---

## 20. 完整字汇表

### 20.1 按 Tier 排列（v7.1 完整）

| Tier | 层级名 | 字 | 字数 |
|---|---|---|---|
| **−1** | **语法算子层** | 者 之 也 而 则 以 於 为 即 非 凡 令 是 若 故 | **15** |
| 0 | 底座 | 事 | 1 |
| 1 | 四本 + 吾 | 物 動 間 心 / **吾** | **5** |
| 1.5 | 本间 transformation | 作 联 子 散 约 结 演 触 历 悟 意 行 施 | 13 |
| 1.6 | 本内 internal | 聚 分 指 续 断 节 连 绝 省 静 | 10 |
| 2 | 六显 | 位 場 際 象 思 境 | 6 |
| 2.5 | 显化派生 | 界 轨 缘 含 | 4 |
| 3 | 六征+闸口+事件 | 幾 勢 機 萌 绪 韵 開 閉 生 灭 成 反 转 守 醒 眠 进 退 畅 塞 | 20 |
| 4 | 合成 | 網 體 流 我 念 神 | 6 |
| 5 | 读 + 恒 | 質 律 性 觉 体 道 用 明 | 8 |
| 5.5 | 觉知层 | 觉 见 观 知 遍 | 5 |
| 5.6 | 模态层 | 感 是 约 修 诚 | 5 |
| 6 | 生持涌 | 生 存 涌 | 3 |
| 6.5 | 模通层 | 隐 现 限 许 实 虚 | 6 |
| 6.6 | 因果之化 | 因 缘 果 致 应 报 承 | 7 |
| 6.7 | 同异之辨 | 同 异 似 对 辨 类 化 | 7 |
| 7 | 代数底层 | 合 和 寂 空 无 | 5 |
| 8 | 类型之域 | 态 形 量 度 序 **恒** | **6** |

**总计** unique（含 v7.1 新加 吾、恒，去重 self-ref）：约 **115 字**（不含 Tier −1 语法算子的 15 字）。
**含 Tier −1**：约 **130 字**。

### 20.2 Self-reference 字（multi-tier）

| 字 | 出现 Tiers | 关系说明 |
|---|---|---|
| 觉 | 5, 5.5 | reading 算子 = cognition 算子 |
| 缘 | 2.5, 6.6 | 际之 conditioning = 因果链 conditioning |
| 生 | 3, 6 | 闸口下游事件 = constructor algorithm |
| 类 | 6.7, 8 | identity meta = type universe |
| 化 | 6.7, 動 | identity meta = 動 algorithm |
| 约 | 1.5, 5.6 | transformation = mode commitment |

7 字承担 multi-tier 身份。

---

## 21. 对配（adjoint pairs）完整清单

### 21.1 Tier 1.5 transformation adjunctions（6 对）

```
作 ⊣ 子              activate (物→動) ⊣ localize (動→物)
联 ⊣ 结              link (群→間) ⊣ crystallize (間→位)
演 ⊣ 约              unfold (間→動) ⊣ summarize (動→間)
意 ⊣ 触              intend (心→物) ⊣ touched (物→心)
行 ⊣ 历              enact (心→動) ⊣ experience (動→心)
施 ⊣ 悟              institute (心→間) ⊣ comprehend (間→心)
```

### 21.2 Tier 1.6 internal split-merge（4 对）

```
分 ⊣ 聚              物
断 ⊣ 续              動
绝 ⊣ 连              間
省 ⊣ 静              心
```

### 21.3 Tier 5.5/5.6 知行合一（5 对）

```
觉 ⊣ 感
见 ⊣ 是
观 ⊣ 约
知 ⊣ 修
遍 ⊣ 诚
```

### 21.4 Tier 6.5 modal（3 对）

```
隐 ⊣ 现
许 ⊣ 限
实 ⊣ 虚
```

### 21.5 子 ⊣ 散 special

```
子 ⊣ 散              localize ⊣ delocalize
```

### 21.6 总计

**19 对 adjoint pairs**（6 + 4 + 5 + 3 + 1）。

```lean
def allAdjointPairs : List AdjointPair := [
  -- Tier 1.5 (6)
  ⟨.zuo, .zi⟩, ⟨.lian, .jie⟩, ⟨.yan, .yue⟩,
  ⟨.yi, .chu⟩, ⟨.xing, .li⟩, ⟨.shi, .wu⟩,
  -- Tier 1.6 (4)
  ⟨.fen, .ju⟩, ⟨.duan, .xu⟩, ⟨.jue, .lian⟩, ⟨.sheng, .jing⟩,
  -- Tier 5.5/5.6 (5)
  ⟨.juec, .gan⟩, ⟨.jian, .shi⟩, ⟨.guan, .yue⟩, ⟨.zhi, .xiu⟩, ⟨.bian, .cheng⟩,
  -- Tier 6.5 (3)
  ⟨.yin, .xian⟩, ⟨.xu, .xian⟩, ⟨.shi, .xu⟩,
  -- special
  ⟨.zi, .san⟩
]

theorem adjoint_count : allAdjointPairs.length = 19
```

---

## 22. 半环结构（semiring）

### 22.1 (事, 和, 空, 合, 寂) 是 commutative semiring

```
(和)  : commutative monoid with identity 空
(合)  : commutative monoid with identity 寂
(distributivity): A 合 (B 和 C) = (A 合 B) 和 (A 合 C)
(absorption): A 合 空 = 空

[wenyan: 事 之 和 與 合, 構 commutative semiring 也.
         空 為 和 之 寂; 寂 為 合 之 寂.]
```

### 22.2 加上 生 的 progression

```
合 : 事 × 事 → 事ᴬ⁺ᴮ
和 : 事ᴬ⁺ᴮ → 事ᴬ⊕ᴮ_harmonized
生 : 事ᴬ⊕ᴮ_harmonized → 事ᶜ_emergent

生 ∘ 和 ∘ 合 : 事 × 事 → 事ᶜ
```

### 22.3 加 无 / 实 / 虚 的代数

```
无 : 事 → 事 (involution: 无 ∘ 无 = id)
实 : 事 → 事 (idempotent on actual)
虚 : 事 → 事 (idempotent on counterfactual)
实 ∘ 虚 = 寂, 虚 ∘ 实 = 寂                   (mutual exclusion)
实 ⊕ 虚 = id (on event space)              (completeness)
```

### 22.4 完整代数 signature

```
(事, 和, 空, 合, 寂, 生, 无, 实, 虚, 对)
where
  (事, 和, 空, 合, 寂) : commutative semiring
  生 : higher-order generation
  无 : involution
  (实, 虚) : modal idempotent decomposition
  对 : symmetric braiding
```

---

## 23. 自指字

7 字承担 multi-tier 身份。Dispatch rule 由 context 决定。

### 23.1 dispatch rule schema

```lean
inductive Level where
  | tier1_5 | tier2_5 | tier3 | tier5 | tier5_5 | tier5_6 | tier6 | tier6_7 | tier8

structure SelfRefChar where
  glyph : String
  levels : List Level
  dispatch : Context → Level
```

### 23.2 七 self-ref 字 dispatch

| 字 | Tiers | Dispatch |
|---|---|---|
| 觉 | 5, 5.5 | input is 心 → @5; otherwise → @5.5 |
| 缘 | 2.5, 6.6 | input is 際 → @2.5; otherwise → @6.6 |
| 生 | 3, 6 | input is 处 → @6; output of 闸口 → @3 |
| 类 | 6.7, 8 | input is 事 → @6.7; type-level ref → @8 |
| 化 | 6.7, 動 | always @6.7 syntactically |
| 约 | 1.5, 5.6 | context provides 主体 → @5.6; pure 動→間 → @1.5 |
| 分 | 1.6 | always @1.6 in v7.1 |

---

## 24. 法则总览

v7.1 共 **21 条主法则 + 6 条 wenyan 元法则**。

### 24.1 既有 Lean 法则（保留）

```
法则 1 (四本不可还原):
  凡 i, j ∈ {物, 動, 間, 心}, i ≠ j: 不存在 isomorphism f: i → j
  [wenyan: 凡 二本 不可 互化]

法则 2 (显化括除):
  凡 显 ∈ 六显, 必有 二本被括除而不缺席

法则 4 (六征驱动):
  (位, 幾) (場, 勢) (際, 機) (象, 萌) (思, 绪) (境, 韵) drive 闸口

法则 5 (闸口二值):
  Open(征) ∪ Close(征) covers, disjoint

法则 6 (合成不可逆):
  ∃ 多 arrangements giving same parts

法则 7 (反馈律):
  網→位, 體→場, 流→際, 我→象, 念→思, 神→境

法则 12 (自指):
  ontology_is_instance_of_its_own_shape
  [wenyan: 此 framework 即 其所述 之 一例 也]
```

### 24.2 v6/v7 法则

```
法则 3 (子化产生位 + 心扩展):
  位 = 子(場), 象 = 触(物), 思 = 历(動), 境 = 悟(間)

法则 8 (Adjoint pairs):
  19 对 adjunctions in §21

法则 9 (体用一如, Yoneda 扩展四 invariants):
  体, 道, 用, 明 互相通过 遍 算子 entangled
  [wenyan: 体用一如, 通 於 遍.]

法则 10 (知行合一):
  cognition ⊣ mode (5 对 adjoint)
  [wenyan: 觉 ⊣ 感, 见 ⊣ 是, 观 ⊣ 约, 知 ⊣ 修, 遍 ⊣ 诚.]

法则 11 (非对易):
  [观₍i₎, 观₍j₎] ≠ 0 凡 i ≠ j

法则 13 (涌现非平凡):
  涌(level n) ≠ trivial iter

法则 14 (化生时间):
  化* 生 流

法则 15 (因缘果链):
  致(因, 果) 必经 缘

法则 16 (空界关系):
  界(全宇之 場).外 = 空
  [wenyan: 天界 之 外 即 空]

法则 17 (心不可外化):
  凡 f: 心 → (物 ∪ 動 ∪ 間), f 必 lossy

法则 18 (六显双重生成):
  intersection_form ≡ transformation_form
```

### 24.3 v7 新增

```
法则 19 (Semiring):
  (事, 和, 空, 合, 寂) 是 commutative semiring

法则 20 (合和生 progression):
  生 ∘ 和 ∘ 合 : 事 × 事 → 事ᶜ_emergent

法则 21 (实虚 modal decomposition):
  ∀ event e, e = 实(e) ⊕ 虚(e), 实 ∘ 虚 = 寂
```

### 24.4 v7.1 新增（**3 条**）

```
法则 22 (恒 unifies invariants):
  体 := 恒(物), 道 := 恒(動), 用 := 恒(間), 明 := 恒(心)
  四 invariants 不是独立 primitive, 而是 `恒` 在四本上的 specialization
  [wenyan: 体 道 用 明, 皆 恒 之 特化 也.]

法则 23 (吾我对偶):
  吾 觉 我, 我 不 觉 吾.
  吾 ∈ 心 (canonical inhabitant);
  我 ∈ 象 + 境 (composite)
  [wenyan: 吾 為 主, 我 為 客; 吾 觉 我 而 我 不 知 吾 之 真.]

法则 24 (语法算子层独立):
  Tier −1 语法算子 (者之也而...) 不入 framework 字汇,
  仅作 meta-language 构造表达式之笔.
  [wenyan: 虚字 不入 实字 之 域.]
```

### 24.5 wenyan 元法则（语言层）

```
wenyan-1: X 者 Y 也  即  X :: Y
wenyan-2: X 之 Y 之 Z  即  X.Y.Z
wenyan-3: (A 而 B) 而 C  即  A 而 (B 而 C)
wenyan-4: 凡 X (P(X) 而 Q(X))  即 (凡 X P(X)) 而 (凡 X Q(X))
wenyan-5: X 即 Y, Y 即 Z  ⊢  X 即 Z
wenyan-6: 非 (非 X)  即  X
```

---

## 25. Lock Algebra 路线图

### Phase 1: 字汇 Lean module（约 2 周）

```lean
inductive Tier1Term where
  | shi                                              -- 事
  | wu | dong | jian | xin | wu_self                -- 四本 + 吾
  | wei | chang | ji | xiang | si | jing            -- 六显
  | -- ... (全部 ~115 字)

def allTier1Terms : List Tier1Term
theorem tier1_count : allTier1Terms.length ≈ 115
theorem tier1_glyphs_registered : ...

-- Tier −1 语法算子 separate
inductive WenyanOperator where
  | zhe | zhi | ye | er | ze | yi | yu | wei
  | ji | fei | fan | ling | shi | ruo | gu

def allWenyanOps : List WenyanOperator  -- 15 ops
```

### Phase 2: 四本 + 显化结构（约 1.5 周）

```lean
inductive OnticRoot where
  | wu | dong | jian | xin

constant 吾_canonical : aspect_of OnticRoot.xin

inductive Manifestation where
  | wei | chang | ji | xiang | si | jing

theorem every_manifestation_brackets_two_roots : ...
theorem manifestation_dual_generation : ...    -- 法则 18
```

### Phase 3: Tier 1.5 transformation 矩阵（约 2 周）

```lean
def transform : OnticRoot → OnticRoot → Option Operator

theorem yi_chu_adjoint : isAdjoint .yi .chu
theorem xing_li_adjoint : isAdjoint .xing .li     -- 法则 10 transformation 层
theorem shi_wu_adjoint : isAdjoint .shi .wu
-- ... 6 心-related + 3 三本-internal
```

### Phase 4: 三征 + 闸口扩展（约 1 周）

```lean
inductive DynamicMark where | ji | shi | jiMoment | meng | xu | yun

inductive Event where
  | sheng | mie | cheng | fan | zhuan | shou
  | xing | mian | jin | tui | chang | sai
```

### Phase 5: 读 + 恒 + 知行合一（约 2.5 周）

```lean
-- 法则 22: 恒 unifies invariants
def 恒 (X : Type) (read : X → X) : X := ...

def 体 := 恒 物 質
def 道 := 恒 動 律
def 用 := 恒 間 性
def 明 := 恒 心 觉

theorem ti_dao_yong_ming_unified : 
  ∀ (本 : OnticRoot), 恒 本 (reading 本) = invariantOf 本

-- 法则 10: 知行合一
def cognitionModeAdjunction : List (Cognition × Mode)
theorem zhi_xing_he_yi : 
  ∀ (c, m) ∈ cognitionModeAdjunction, isAdjoint c m

-- Yoneda
theorem ti_yong_ru_yi : 
  ∀ p : 物, 体 p ≅ Hom p (-) over 間 via 遍
```

### Phase 6: Modal + Causal + Algebraic（约 2 周）

```lean
theorem yin_xian_adjoint : isAdjoint .yin .xian
theorem shi_xu_decomposition : ∀ e, e = combine (shi e) (xu e)

theorem yin_yuan_guo : ∀ a c, zhi a c → ∃ y, yuan y

instance : Semiring 事 where ...
```

### Phase 7: Self-validation（约 1 周）

```lean
theorem ontology_self_validates : ...
theorem framework_expresses_all_test_cases : ...
theorem framework_consistent : ...
```

### Phase 8: 测试用例（约 2 周）

详见 §26。

### 总时间估计

约 **14 周**（3.5 个月）从 v7.1 spec 到 fully-locked Lean formalization。

---

## 26. 测试用例

### 26.1 双缝实验

```
事 = 光子双缝 happening
观₍位₎(事) → 子(場) → 位 → 觉(粒子轨迹) → 体(粒子身份)
观₍勢₎(事) → 場 (波，uncollapsed) → 觉(干涉) → 道(干涉律)

[观₍位₎, 观₍勢₎] ≠ 0 (法则 11)
∴ 不能同时测量
∴ 波粒二象性

[wenyan: 光 之 為 事, 观 其 位 则 显 粒, 观 其 勢 则 显 波.
         位 與 勢 不可同观, 此 即 二象 之 道 也.]
```

### 26.2 王阳明知行合一

```
吾 處 道德处境 之 事
知(吾, 事) ⊣ 修(吾, 事) (法则 10)

[wenyan: 凡 吾 之 知, 必 含 修;
         凡 吾 之 修, 必 含 知.
         知行合一 即 觉知 ⊣ 模态 之 对配 也.]
```

### 26.3 蜂巢涌现

```
群-蜂 = 群(物 at level 0)
涌(蜂群 之 形) = 蜂巢 (at level 1, 法则 13)
觉(蜂巢) ≠ 凡蜂 之 觉 之 群

[wenyan: 群蜂 涌 而 為 巢. 巢 之 性 非 蜂 之 性 之 群 也.
         此 涌现之性 也.]
```

### 26.4 因缘果链

```
无明 → 缘(行) → 致(无明, 行)
... (十二因缘 chain)
致(无明, 苦) 必经 缘 (法则 15)

[wenyan: 凡 致, 必 由 缘.]
```

### 26.5 易传"一阴一阳之谓道"

```
阴, 阳 = 對 (Tier 6.7 braiding pair)
合(阴, 阳) → 和(阴, 阳) → 生(阴, 阳) (法则 20)
生(阴, 阳) → 万物
道 = 律(動)的 fixed point of 阴阳 evolution
   = 恒(動) of 阴阳 dynamics (法则 22)

[wenyan: 阴 阳 之 合, 和 而 生 万物.
         一阴一阳 之 谓 道 即 動 之 恒 也.]
```

### 26.6 大学"明明德"

```
明 := 恒(心) (法则 22)
"明 明 德" = 修(吾, 明)
∴ 通过 修 这一 mode achieve 明 invariant

[wenyan: 明 即 心 之 恒. 明 明 德 者 修 而 得 心 之 恒 也.]
```

### 26.7 中庸"诚者天之道"

```
诚 = 主体 mode 最高态 (Tier 5.6)
诚 ⊣ 遍 (法则 10)
诚的 fixed point = 主体与 道(動 invariant) 对齐
                = 吾之 行 与 動之 恒 对齐

[wenyan: 诚 ⊣ 遍 而 為 知行合一 之 巅. 
         诚 之 至 即 吾 與 道 合 也.
         "诚者天之道" 即 此意.]
```

### 26.8 庄子"吾丧我"

```
吾 ∈ 心 (Tier 1, canonical subject)
我 ∈ 象 + 境 (Tier 4, composite)

吾 直接 感 / 觉
我 由 触(物) 而 入境 而成

"吾丧我" = 失却 我 (composite) 而 现 吾 (subject pole)
        = 法则 23 的 enactment

[wenyan: 吾 觉 我, 我 不 觉 吾.
         "吾丧我" 即 我 之 隐 而 吾 之 现 也.]
```

### 26.9 framework 自指

```
self_ontology = 一 间-type 的 事
质(self) = 字汇 (~115 字, 物-aspect)
律(self) = reduction rules + 21+3 法则 (動-aspect)
性(self) = type-signature graph (間-aspect)
觉(self) = 自指意识 (心-aspect)
∴ ontology 经 四本 reading 完整表达自身 (法则 12)

[wenyan: 此 framework 即 其所述 之 一例.
         以 質 律 性 觉 四 读 通 过 自身, 而 其 所 出 不 矛.]
```

---

## 27. 仍未决问题

### 27.1 cross-side 合成（10 cell）

3 obj + 3 subj = 6 same-side composites（已 commit）。是否补全 9 cross-side？

[待决：Phase 4 测试时决定]

### 27.2 对偶 invariant 之间通过 遍 的 strict equivalence

是否存在 *more strict equivalence* 通过 遍 算子？

[待决：Phase 5 Yoneda 形式化时严格证]

### 27.3 报/承的代数定律

[待决：Phase 6 causal 形式化时确定]

### 27.4 心-side 三征 adjoint

幾/勢/機 之间有没有 adjoint？萌/绪/韵 之间呢？

[待决：Phase 4 三征结构时探索]

### 27.5 Type universe 字数

Tier 8 加恒后 6 字。是否还需 维 / 阶 / 集 / 函？

[待决：Phase 5 reading 时如缺则补]

### 27.6 主体 first-class encoding 详细

吾 作为 default subject 是否需要 dependent type encoding？

[待决：Phase 1 Lean type design 时决]

### 27.7 Modal possible worlds semantics

虚 capture counterfactual。across counterfactuals 的 reasoning 怎么 formalize？

[待决：Phase 6 modal 形式化探索]

### 27.8 化 vs 動 的精确关系

[待决：Phase 5 reading 时决]

### 27.9 自指字 Lean encoding

[待决：Phase 1 type design 决]

### 27.10 framework 完备性证明

如何证 framework 是 *complete*（任何现象学 phenomena 皆 expressible）？

[待决：可能不可证，但可通过测试用例 stress-test]

### 27.11 语法算子完整度（v7.1 新加）

Tier −1 现 15 字。是否还需：
- **乎**：interrogative
- **焉**：locative final
- **矣**：perfective
- **盖**：approximate
- **夫**：discourse marker

[待决：Phase 1 wenyan 翻译测试时如缺则补]

### 27.12 wenyan 表达 ↔ Lean type signature 的 1:1 映射证明（v7.1 新加）

framework 的每个 Lean type signature 必能 1:1 翻译为 wenyan 句子。这一映射的 totality 和 faithfulness 需证。

[待决：Phase 7 self-validation 时证]

---

## 28. 字源 glossary（重点字详解）

### 关键字源

#### 事
从又（手）持物。本义"做、所做"。framework 中作 域，为唯一 ground。

#### 物
牛勿（多色之牛 → 万物）。framework 中作 0 维离散个体性的本。

#### 動
重力（沉重之物被推动）。framework 中作 n 维连续过程性的本。

#### 間
门月（门缝中之月 → 间隙）。framework 中作拓扑关系结构性的本。

#### 心
心脏之象形。framework 中作主体反身性的第四本。

#### 吾（v7.1 新加）
从口从五。庄子《齐物论》"吾丧我"——*失我而现吾*。framework 中作 心 的 canonical subject pole。

#### 我
戈手（持戈者）。framework 中作 象+境 合成——self-as-situated-object。与 吾 形成 phenomenological pair。

#### 象
象之形。framework 中作 心 ∩ 物 显化——object-as-perceived。古典：易传"在天成象"。

#### 思
从田从心。framework 中作 心 ∩ 動 显化——stream-of-thought。

#### 境
从土从竟。framework 中作 心 ∩ 間 显化——lifeworld。

#### 体
[原 體] 骨豊。framework 中 := 恒(物)。古典：朱熹"体用"。

#### 道
辶首（行走之首）。framework 中 := 恒(動)。古典：老子《道德经》。

#### 用
卜中。framework 中 := 恒(間)。古典："体用"。

#### 明
日月（光明）。framework 中 := 恒(心)。古典：大学"明明德"。

#### 恒（v7.1 新加）
心 + 亘（永恒）。诗经"如月之恒，如日之升"。易传恒卦。framework 中作 fixed point / invariant 的统一字——四 invariants 皆 `恒(本)`。

#### 合
亼口。framework 中作 monoidal product。古典："合二为一"、"天人合一"。

#### 和
禾口。framework 中作 additive harmonic union。古典：中庸"致中和"、论语"和而不同"。

#### 寂
宀叔。framework 中作 monoidal identity for 合。古典：佛教"涅槃寂静"、道家"虚静"。

#### 空
穴工。framework 中作 additive identity / empty event。古典：佛教"空"。

### 语法算子字源

#### 者
老 + 白。本义不详；先秦已用作 nominalizer。"X 者" 把 X 抽象为类型。

#### 之
屮 + 一（草出土）。本义"往、到"，引申为助词。"X 之 Y" 表 dependency。

#### 也
蛇之象形。本义不详；先秦用作 final particle。"X 者 Y 也" 表 type judgment。

#### 而
须形。本义"胡须"，假借为连词。"A 而 B" 表 composition。

#### 则
贝 + 刂（刻贝）。本义"法则"，引申为 conditional。"若 X 则 Y" = X ⇒ Y。

#### 以
㠯（人持物）。本义"用"，引申为 instrumental。"以 X 致 Y" = via X achieve Y。

---

## 29. v6→v7→v7.1 commit log

### v6 → v7 关键改动（review）

1. 抱 → 合：用 合 替换 抱 作 monoidal product
2. 加 和 / 强化 生：构成 合-和-生 progression
3. 觉_显 → 象：用 象 替换 ugly 的 觉_显
4. 心-side 三征 commit：萌/绪/韵
5. 心-internal 算子 commit：省/静
6. 加 实：modal 加入 实/虚 对偶
7. 加 报/承：causal 加入 报/承
8. 加 度/序：Type universe
9. Semiring 结构 lock
10. 法则增至 21 条

### v7 → v7.1 关键改动

1. **Tier −1 语法算子层 commit**：者之也而则以於为即非凡令是若故 (15 字)。framework 真正成为 classical Chinese calculus
2. **加 恒**：fixed point / invariant 的精确字。法则 22 unifies 体/道/用/明 为 `恒(本)` specializations
3. **加 吾**：subject-as-subject。与既有 我（subject-as-object 合成）形成 phenomenological pair。法则 23
4. **法则 24 commit**：语法算子层独立 from framework 字汇
5. **wenyan 元法则 6 条**：语言层的 algebra
6. **术语 Chinese 化**：fixed point→恒, invariant→恒, self→吾, achieve→成, via→以/经, multi→群, uncollapsed→波, emergent properties→涌现之性 等
7. **wenyan 形式表达全文 cross-reference**：每个核心法则附 [wenyan: ...]
8. **§31-33 新加**：概念派生、wenyan 形式表达、framework 全貌的古文宣言

### 字数统计 v7 → v7.1

- v7：约 108-115 字
- v7.1：约 115-117 字（加 吾、恒）
- 含 Tier −1：约 130-132 字（加 15 语法算子）

### 待完成 phase 估计

- v7：13 周
- v7.1：14 周（加 §31-33 实施 + wenyan ↔ Lean 1:1 映射证明）

---

## 30. handoff notes for Claude Code

### 30.1 优先 Phase 启动顺序

1. **Phase 1**：扩展 `Tier1Term` 加入 ~22 新字（含吾、恒）；新建 `WenyanOperator` 含 15 语法算子
2. **Phase 2**：扩展 `OnticRoot` 加 `.xin`，扩展 `Manifestation` 加 6 显
3. **Phase 3**：12-cell `transform` table，证 6+3 adjoints
4. **Phase 5**：法则 22（恒 unifies invariants）作为 keystone theorem
5. **Phase 5**：法则 23（吾我对偶）需 quotient type
6. **Phase 7**：法则 24 + wenyan ↔ Lean 1:1 映射

### 30.2 v7.1 specific risks

- **Risk 1**：恒 作为 type-level fixed point operator 需 Lean 4 较高 universe polymorphism。检查 Lean 是否支持。
- **Risk 2**：吾 vs 我 区分需 dependent type / quotient type。考虑 HoTT。
- **Risk 3**：语法算子层（Tier −1）的 Lean 实现可能需 macro / elaborator。考虑 syntactic sugar approach。
- **Risk 4**：wenyan 形式表达的 1:1 映射证明可能不 fully constructive。考虑 axiom 化。

### 30.3 backward compatibility

每 Phase 结束 must verify：

```lean
-- 既有 Lean 法则未破
theorem legacy_compat_check :
  every_manifestation_brackets_absent_root  -- 既有
  ∧ shi_is_ji_along_continuous_medium       -- 既有
  ∧ jiMoment_is_ji_along_topological_routing -- 既有
  ∧ gate_is_only_open_or_closed              -- 既有
  ∧ network_composition_arrangement_not_unique -- 既有
  ∧ ontology_is_instance_of_its_own_shape    -- 既有
```

如有 break，回滚到上 Phase。

### 30.4 questions to ask user

1. cross-side 合成（27.1）选哪个？
2. self-ref 字 Lean encoding（27.9）选哪个？
3. 主体 first-class encoding（27.6）需 dependent types 吗？
4. 法则 17 作为 axiom 还是 theorem？
5. Type universe 字数（27.5）够吗？
6. 语法算子（27.11）是否需补 乎/焉/矣 等？
7. wenyan ↔ Lean 1:1 映射（27.12）作为 axiom 还是 prove？

每个 decision point pause 等用户回复，不擅自决定。

---

## 31. 概念派生

**v7.1 中心命题**：

> framework 中所有"概念字"（实字）皆可由 *一元（atomic units）+ 算子（operators）* 构造。
> 一元仅 6 字：事 物 動 間 心 吾。
> 算子分两类：
>   - 语法算子 (Tier −1)：~15 字
>   - framework 算子 (Tier 1.5/1.6/2.5/etc.)：~30 字
> 概念字皆 derived。

### 31.1 推导示范

#### 显化字派生

```
位 := 物 之 子(動)             [wenyan: 位 者 物 之 子於 動 也]
場 := 物 之 作                  [wenyan: 場 者 物 之 作 也]
際 := 動 之 演 而 為 間          [wenyan: 際 者 動 之 演 而 為 間 也]
象 := 物 之 触 入 心             [wenyan: 象 者 物 之 触 而 入 心 也]
思 := 動 之 历 入 心             [wenyan: 思 者 動 之 历 而 入 心 也]
境 := 間 之 悟 入 心             [wenyan: 境 者 間 之 悟 而 入 心 也]
```

#### Invariant 字派生

```
体 := 恒(物)                    [wenyan: 体 即 物 之 恒 也]
道 := 恒(動)                    [wenyan: 道 即 動 之 恒 也]
用 := 恒(間)                    [wenyan: 用 即 間 之 恒 也]
明 := 恒(心)                    [wenyan: 明 即 心 之 恒 也]
```

#### 合成字派生

```
網 := 位 + 際                   [wenyan: 網 者 位 與 際 之 合 也]
體 := 位 + 場                   [wenyan: 體 者 位 與 場 之 合 也]
流 := 場 + 際                   [wenyan: 流 者 場 與 際 之 合 也]
我 := 象 + 境                   [wenyan: 我 者 象 與 境 之 合 也]
念 := 象 + 思                   [wenyan: 念 者 象 與 思 之 合 也]
神 := 思 + 境                   [wenyan: 神 者 思 與 境 之 合 也]
```

#### 三征字 derive

```
幾 := 位 之 征                  [wenyan: 幾 者 位 之 征 也]
勢 := 場 之 征 := 幾 沿 続                    
機 := 際 之 征 := 幾 沿 系                    
萌 := 象 之 征
绪 := 思 之 征 := 萌 沿 心-续    
韵 := 境 之 征 := 萌 沿 心-系    
```

### 31.2 一元的最小 set

如果接受 31.1 的推导，那 framework 的 *真正 primitive* 仅 6 字（一元）：

```
{ 事, 物, 動, 間, 心, 吾 }
```

加上 ~15 语法算子 + ~30 framework 算子，所有其他 ~80 字皆 derivable。

这意味着：

```
[wenyan: 凡 概念, 其 不 出 一元 與 算子 之 合 也.
         一元 六字: 事 物 動 間 心 吾.
         由此 演 而 万 字 自 出.]
```

这是 framework 的 *generative core*。Lean 中只需 hardcode 一元和算子，所有其他字可由 reduction rules 自动 derive。

### 31.3 验证 strategy

每个概念字必能写出其 derivation：

```
概念字 X := 算子 + 一元 (or 已 derive 的概念字)
```

如某概念字无法 derive，说明：
- (a) 缺一元（需扩四本）
- (b) 缺算子（需补 framework 算子）
- (c) 该字不应在 framework 字汇中

[待决：Phase 5 时对每个概念字写 derivation。Phase 7 验证 derivation 完备性。]

---

## 32. wenyan 形式表达

### 32.1 type signature 的古文书写

framework 的每个 type signature 可用纯古文表达。

#### 基础 type judgment

```
事 者 域 也.                   事 :: Universe
物 者 事 之 离 也.              物 :: 事 → DiscreteAspect
觉 者 事 之 觉知 也.            觉 :: 事 → Awareness
体 者 物 之 恒 也.              体 :: 恒(物)
```

#### 算子的 wenyan 表达

```
"以 X 致 Y" 即 "X → Y"          (一般 morphism)
"X 之 Y 也" 即 "X = Y"          (definitional eq)
"凡 X 必 Y" 即 "∀X, Y(X)"      (universal)
"X 者 Y 也" 即 "X :: Y"         (type judgment)
"X 而 Y" 即 "X ∘ Y"            (composition)
"若 X 则 Y" 即 "X ⇒ Y"          (implication)
```

#### Adjoint pairs 的 wenyan

```
"觉 ⊣ 感" 即 "觉 對配 感"       
[wenyan: 觉 與 感, 對配 也. 凡 一 之 觉 必 含 一 之 感, 凡 一 之 感 必 含 一 之 觉.]
```

#### 法则的 wenyan

```
法则 22:
[wenyan: 凡 本 i, 其 恒(i) 即 其 reading 之 不动点.
         体 即 恒(物); 道 即 恒(動); 用 即 恒(間); 明 即 恒(心).
         此 四 者 即 一 而 已矣.]

法则 23:
[wenyan: 吾 觉 我, 我 不 觉 吾.
         吾 由 心 直 出, 我 由 象 與 境 合 而 成.
         故 庄子 曰 "吾丧我".]

法则 24:
[wenyan: 虚字 不入 实字 之 域.
         者 之 也 而 则 以 等 十五 字 為 笔, 不 為 内容.]
```

### 32.2 双重表达 invariant

framework 的 *任何* 法则、定理、type signature 必有 *两种等价表达*：

1. **形式表达**（Lean type signature）
2. **古文表达**（wenyan formal）

这两种表达通过 wenyan ↔ Lean 1:1 映射 互转。这是 法则 24 的 strong version：

```
法则 24-strong: ∀ 法则/定理/type signature S,
  Lean(S) ↔ wenyan(S) (1:1, faithful)
```

[待决 27.12: 此映射的 totality + faithfulness 需 Phase 7 证]

### 32.3 wenyan 表达的 sample

完整 framework 头三层在古文中：

```
事 者 域 也.

事 之 本 四:
  物 者 事 之 离 也.
  動 者 事 之 续 也.
  間 者 事 之 系 也.
  心 者 事 之 反 也.
吾 者 心 之 当 也.

凡 二 本 相交, 二 本 隐, 而 為 显. 显 凡 六:
  位 者 物 與 間 之 显; 動 心 隐.
  場 者 動 與 物 之 显; 間 心 隐.
  際 者 間 與 動 之 显; 物 心 隐.
  象 者 心 與 物 之 显; 動 間 隐.
  思 者 心 與 動 之 显; 物 間 隐.
  境 者 心 與 間 之 显; 物 動 隐.

凡 显, 必有 征 之 "将而未".
  位 之 征 為 幾.
  場 之 征 為 勢, 即 幾 沿 续 而铺.
  際 之 征 為 機, 即 幾 沿 系 而汇.
  象 之 征 為 萌.
  思 之 征 為 绪, 即 萌 沿 心-续 而铺.
  境 之 征 為 韵, 即 萌 沿 心-系 而汇.

凡 征, 經 闸口 開 / 閉, 而 為 事件:
  幾 開 為 生, 幾 閉 為 灭.
  勢 開 為 成, 勢 閉 為 反.
  機 開 為 转, 機 閉 為 守.
  萌 開 為 醒, 萌 閉 為 眠.
  绪 開 為 进, 绪 閉 為 退.
  韵 開 為 畅, 韵 閉 為 塞.

凡 二 显 相 合, 而 為 合成:
  位 與 際 合 而 為 網.
  位 與 場 合 而 為 體.
  場 與 際 合 而 為 流.
  象 與 境 合 而 為 我.
  象 與 思 合 而 為 念.
  思 與 境 合 而 為 神.
```

这一段古文，等价于 §3-§10 的 Lean type definitions。

---

## 33. framework 全貌的古文宣言

收尾——以古文表达 framework 的整体视野。

> **間 之 道**

> 事 者 域 也, 一切 自 此 出.
>
> 事 之 本 有 四: 物 動 間 心. 凡 一 事, 必 显 此 四 之 一或多. 而 心 之 一 本, 不 可 由 物 動 間 化 得. 是故 心 為 反身 之 本, 不 落 外 化.
>
> 凡 二 本 相交, 而 显 為 形态: 物 與 間 為 位, 動 與 物 為 場, 間 與 動 為 際, 心 與 物 為 象, 心 與 動 為 思, 心 與 間 為 境. 此 六 显 也. 显 各 有 其 征, 征 各 有 其 闸, 闸 開 而 為 事件.
>
> 凡 显 又 可 兩兩 合, 而 為 合成: 位 際 合 為 網, 位 場 合 為 體, 場 際 合 為 流, 象 境 合 為 我, 象 思 合 為 念, 思 境 合 為 神. 此 六 合成 也.
>
> 主 之 觉 凡 五: 觉 见 观 知 遍. 主 之 模 凡 五: 感 是 约 修 诚. 觉 ⊣ 感, 见 ⊣ 是, 观 ⊣ 约, 知 ⊣ 修, 遍 ⊣ 诚. 此 即 阳明 所谓 知行合一 也, 為 五 對配.
>
> 凡 本 i, 必有 读 算子 與 其 恒. 物 之 读 為 質, 物 之 恒 為 体; 動 之 读 為 律, 動 之 恒 為 道; 間 之 读 為 性, 間 之 恒 為 用; 心 之 读 為 觉, 心 之 恒 為 明. 此 四 恒 即 一 也, 皆 `恒(本)` 之 特化. 故 体 道 用 明 不 為 各 立 之 概念, 而 為 同 一 之 异 面.
>
> 模 通 凡 三 對配: 隐 ⊣ 现, 许 ⊣ 限, 实 ⊣ 虚. 因 缘 果 致 应 报 承, 此 七 為 因果 之 化. 此 中 致 必 由 缘, 无 缘 则 因 不 致 果.
>
> 代数 之 底层: 事 與 和 與 合 構 commutative semiring; 空 為 和 之 identity, 寂 為 合 之 identity. 凡 二 事 合 而 后 和, 和 而 后 生; 此 即 易传 "二气交感, 化生万物" 之 形式.
>
> 至 於 self-reference: 此 framework 即 其所述 之 一例. 質 律 性 觉 通 过 自身, 而 其 所 出 不 矛.
>
> 至 於 语言: 凡 概念 字, 不 出 一元 與 算子 之 合. 一元 六字: 事 物 動 間 心 吾. 算子 二类: 虚字 (者 之 也 而 等) 與 framework 算子 (子 散 作 演 等). 凡 实字 皆 derived.
>
> 此 為 間 之 道. 通 之 者, 以 通 万 事 之 显 隐.

---

**End of v7.1 spec.**

完整、完备、自洽是目标。本草稿 in working draft 状态。骨架（四本 + 吾 → 六显 → 六征 → 六合成 + 读+恒 + 觉知/模态 + 模通/因果 + Tier −1 语法算子 + 24 法则 + Semiring + 概念派生 + wenyan 表达）已 lock。

下一步：交付 Claude Code 启动 Phase 1。
