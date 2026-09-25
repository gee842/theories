# 間/Jian 本体框架 v7：完整核

> **状态**：handoff draft for Claude Code
> **目标**：完整、完备、自洽——可作为 Lean 形式化的 working spec
> **基础**：建立在既有 Lean 模块 `Foundation/JianOntology.lean` 之上

---

## 目录

0. [Meta & 设计原则](#0-meta--设计原则)
1. [哲学基础](#1-哲学基础)
2. [整体结构图](#2-整体结构图)
3. [Tier 0 — 底座](#3-tier-0--底座)
4. [Tier 1 — 四本](#4-tier-1--四本)
5. [Tier 1.5 — 本间 transformation 算子](#5-tier-15--本间-transformation-算子)
6. [Tier 1.6 — 本内 internal 算子](#6-tier-16--本内-internal-算子)
7. [Tier 2 — 六显](#7-tier-2--六显)
8. [Tier 2.5 — 显化派生算子](#8-tier-25--显化派生算子)
9. [Tier 3 — 六征 + 闸口 + 事件](#9-tier-3--六征--闸口--事件)
10. [Tier 4 — 合成形态](#10-tier-4--合成形态)
11. [Tier 5 — Reading 算子 + invariants](#11-tier-5--reading-算子--invariants)
12. [Tier 5.5 — Cognition](#12-tier-55--cognition)
13. [Tier 5.6 — Mode](#13-tier-56--mode)
14. [Tier 6 — Generative / Persistence](#14-tier-6--generative--persistence)
15. [Tier 6.5 — Modal](#15-tier-65--modal)
16. [Tier 6.6 — Causal Morphism](#16-tier-66--causal-morphism)
17. [Tier 6.7 — Identity / Meta](#17-tier-67--identity--meta)
18. [Tier 7 — Algebraic Structural](#18-tier-7--algebraic-structural)
19. [Tier 8 — Type Universe](#19-tier-8--type-universe)
20. [完整字汇表](#20-完整字汇表)
21. [Adjoint Pairs 完整清单](#21-adjoint-pairs-完整清单)
22. [Semiring 结构](#22-semiring-结构)
23. [Self-Reference 字](#23-self-reference-字)
24. [法则总览](#24-法则总览)
25. [Lock Algebra 路线图](#25-lock-algebra-路线图)
26. [测试用例](#26-测试用例)
27. [仍未决问题](#27-仍未决问题)
28. [字源 glossary](#28-字源-glossary)

---

## 0. Meta & 设计原则

### 0.1 设计原则

1. **每字承担不可派生的 fundamental work**——若一字可由其他字组合定义，则不入核。
2. **古文锚点优先**——每字必须有清晰古典文献来源；framework 不发明新字义。
3. **正交性 > 完备性 > 简洁性**（以此为优先级排序）——三本/四本不可还原比少字更重要。
4. **Self-reference 是 feature**——字在不同 tier 承担不同 level 工作是 lived language 的内在特性，不是 ambiguity。
5. **现象学厚度保留**——形式化必须能 derive 王阳明、易传、华严宗式陈述，不退化为 abstract algebra。
6. **生成 DAG 单向**——后层依赖前层，前层不 reference 后层。

### 0.2 与既有 Lean 模块的关系

- `Foundation/JianOntology.lean` 已 lock：三本（物/動/間）、三显（位/場/際）、三征（幾/勢/機）、闸口（開/閉）、合成（網/體/流）。这是 **保留的硬核心**。
- v7 的扩展是 **加层**，不是 **替换**：四本（加心）、六显（加象/思/境）、六征（加萌/绪/韵）、六合成（加我/念/神）、加 Tier 1.5/5/5.5/5.6/6/6.5/6.6/6.7/7/8 共 11 层。
- 既有 `OnticRoot`/`Manifestation`/`DynamicMark`/`Gate`/`CompositeForm` API 保持兼容，仅 inductive 扩展构造子。

### 0.3 文档约定

- **字 type signature**：`字 : Input → Output` 形式，承载 Lean 4 风格 type 直觉
- **法则编号**：法则 1-21（v7 共 21 条，比 v6 加 3 条）
- **待决标记**：`[待决: 描述]`——需要 Phase 测试中决定
- **self-ref 标记**：`[self-ref: 与 Tier X 字 Y 同字]`

---

## 1. 哲学基础

### 1.1 monism with structured aspects

**事**（Universe）是唯一的 ontological ground。一切均是 事 在某种 reading / projection 下的显化。事 不是抽象 universal 也不是物质 substrate——它是 **happening-as-such**，pre-aspect 的纯发生。

事 的 fundamental aspects 是**四本**：物（discrete）、動（continuous）、間（relational）、心（subjective-reflexive）。四本不可还原——任何一本不能由其他三本派生。

### 1.2 phenomenological 完备性的诉求

加入 **心** 作为第四本是 v7 关键 move。理由：

- 主体性（first-person perspective）不可被 物/動/間 任一面 lossless 捕获
- 任何 cognition / mode / measurement 都假设主体存在；若主体外置则框架不完备
- 古典锚点：阳明"心即理"、孟子"四端"、华严"三界唯心"、康德 transcendental subject

但 **心 不是 substance**——它是 reflexive aspect，self-referential 维度征。它内禀地不可外化（法则 17）。

### 1.3 与西方哲学的对照

- 物/動/間/心 ≈ 物质 / 过程 / 关系 / 主体（四元 ontology）
- 但中文 framework 不预设 mind-body 二元——心 与 物 是 *aspects of same 事*，不是两种 substances
- 与 Whitehead process philosophy 的 *actual occasions* 接近，但加上了显化层级
- 与 Nishida 西田几多郎"绝对无的场所"接近，但坚持 4-fold 而非单一基底

### 1.4 知行合一的 framework 表述

王阳明"知行合一"在 v7 framework 是 **法则 10**：
$$\text{cognition} \dashv \text{mode}$$
即 5 对 adjoint：觉⊣感、见⊣是、观⊣约、知⊣修、遍⊣诚。每对是 *主体-事 interaction surface* 的 inbound/outbound dual。

---

## 2. 整体结构图

```
┌──────────────────────────────────────────────────────────┐
│  Tier 0   底座 (1 字)                                    │
│   └─ 事                                                  │
│                                                          │
│  Tier 1   四本 (4 字)                                    │
│   └─ 物 動 間 心                                         │
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
│  Tier 5   Reading + Invariants (8 字)                    │
│   └─ 質律性觉 → 体道用明                                  │
│                                                          │
│  Tier 5.5 Cognition (5 字)                               │
│   └─ 觉 见 观 知 遍                                       │
│                                                          │
│  Tier 5.6 Mode (5 字)                                    │
│   └─ 感 是 约 修 诚                                       │
│                                                          │
│  Tier 6   Generative / Persistence (3 字)                │
│   └─ 生 存 涌                                             │
│                                                          │
│  Tier 6.5 Modal (6 字)                                   │
│   └─ 隐 现 限 许 实 虚                                    │
│                                                          │
│  Tier 6.6 Causal (7 字)                                  │
│   └─ 因 缘 果 致 应 报 承                                  │
│                                                          │
│  Tier 6.7 Identity / Meta (7 字)                         │
│   └─ 同 异 似 对 辨 类 化                                  │
│                                                          │
│  Tier 7   Algebraic Structural (5 字)                    │
│   └─ 合 和 寂 空 无                                       │
│                                                          │
│  Tier 8   Type Universe (5 字)                           │
│   └─ 态 形 量 度 序                                       │
│                                                          │
│  Cross-tier (Tier 1.5, 1.6, 2.5):                        │
│   ├─ Tier 1.5  本间 transformation: 作联子散约结演 触历悟意行施 │
│   ├─ Tier 1.6  本内 internal: 聚分指 续断节 连绝 省静     │
│   └─ Tier 2.5  显化派生: 界轨缘含                         │
└──────────────────────────────────────────────────────────┘
```

总字数 unique（去除 self-reference 双计）：约 **96 字**。

---

## 3. Tier 0 — 底座

### 事 :: Universe

唯一 ground。pre-aspect 的纯 happening。

```
事 : Universe
```

- **字源**：从又（手）持物之形，本义"做、所做"
- **语义重音**：被进行 / 被遇到的 *something*
- **角色**：所有其他字 derive from 事；不可被定义，只可被起点假设
- **古典锚点**：易传"形而上者谓之道，形而下者谓之器"中的 *形* 即 事
- **Lean**：`Universe` 类型层（不是 inductive，是 ground type）

```lean
constant 事 : Type 1  -- universe of all happenings
```

---

## 4. Tier 1 — 四本

四本是 事 的不可还原 aspects。

### 4.1 物 :: 0 维 / 离散个体性

```
物 : 事 → DiscreteAspect
```

- **字源**：牛勿（多色之牛 → 万物）
- **语义**：可指可数的 individuated entity
- **维度征**：0 维倾向
- **古典锚点**：庄子《齐物论》、墨子《经》"物，达也"
- **Lean**：`OnticRoot.wu`

### 4.2 動 :: n 维 / 连续过程性

```
動 : 事 → ContinuousAspect
```

- **字源**：重力（沉重之物被推动）
- **语义**：延展铺陈的过程
- **维度征**：n 维倾向
- **古典锚点**：易传"穷则变，变则通"
- **Lean**：`OnticRoot.dong`

### 4.3 間 :: 拓扑 / 关系结构性

```
間 : 事 → RelationalAspect
```

- **字源**：门月（门缝中之月 → 间隙）
- **语义**：拓扑关系结构
- **维度征**：拓扑倾向，无内在度量
- **古典锚点**：王弼"无所不通"、华严"重重无尽"
- **Lean**：`OnticRoot.jian`

### 4.4 心 :: 反身 / 主体内省性 [新]

```
心 : 事 → SubjectiveAspect
```

- **字源**：心脏之象形
- **语义**：第一人称视角，反身性，不可外化
- **维度征**：reflexive 维度（self-referential structure）
- **古典锚点**：王阳明"心即理"、孟子"四端之心"、华严"三界唯心"
- **Lean 扩展**：`OnticRoot.xin`（新构造子）

**关键约束**（法则 17）：心 不可被 物/動/間 任一本 lossless 捕获——任何 f: 心 → (物 ∪ 動 ∪ 間) 都是 lossy projection。

```lean
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
物              id         作         联
動              子         id         约
間              结         演         id
```

| 字 | 类型 | 工作 | 字源 |
|---|---|---|---|
| **作** | 物 → 動 | 让物进入运作 | 人乍（突然站起） |
| **联** | Multi → 間 | 把多个用关系联起 | 耳丝（连缀） |
| **子** | 動/場 → 物/位 | 凝出 discrete 单位 | 婴儿、种子 |
| **散** | 物 → 動 | 弥散为过程 | 攴肉（击打使分） |
| **约** | 動 → 間 | 过程约简为关系 | 丝勺（束系） |
| **结** | 間 → 位 | 关系凝出节点 | 丝吉（结绳） |
| **演** | 間 → 動 | 关系展开为过程 | 水寅（水流推演） |

### 5.2 心与三本之间（6 字）[新]

```
                物         動         間         心
物              -          作         联         触
動              子         -          约         历
間              结         演         -          悟
心              意         行         施         -
```

| 字 | 类型 | 工作 | 字源 |
|---|---|---|---|
| **触** | 物 → 心 | 物入心：被对象触动 | 角虫 |
| **历** | 動 → 心 | 動入心：经历过程 | 厤（曆） |
| **悟** | 間 → 心 | 間入心：领会关系 | 心吾 |
| **意** | 心 → 物 | 心出物：意向所指 | 心音 |
| **行** | 心 → 動 | 心出動：化心为行 | 彳亍 |
| **施** | 心 → 間 | 心出間：建立关系 | 㫃也 |

### 5.3 关键 adjoint pairs

```
意 ⊣ 触        intentionality ⊣ being-touched
行 ⊣ 历        enacting ⊣ experiencing
施 ⊣ 悟        instituting ⊣ comprehending
作 ⊣ 子        activating ⊣ localizing
联 ⊣ 结        linking ⊣ crystallizing
演 ⊣ 约        unfolding ⊣ summarizing
```

**6 对 adjoint** spell out 主体 ↔ 三本 + 三本两两 之间的对偶关系。**行 ⊣ 历** 是知行合一在 transformation 层的 instantiation。

```lean
def transform : OnticRoot → OnticRoot → Option Operator
  | .wu,   .dong => some .zuo    -- 作
  | .wu,   .jian => some .lian   -- 联
  | .wu,   .xin  => some .chu    -- 触
  | .dong, .wu   => some .zi     -- 子 (or .san for 散)
  | .dong, .jian => some .yue    -- 约
  | .dong, .xin  => some .li     -- 历
  | .jian, .wu   => some .jie    -- 结
  | .jian, .dong => some .yan    -- 演
  | .jian, .xin  => some .wu     -- 悟
  | .xin,  .wu   => some .yi     -- 意
  | .xin,  .dong => some .xing   -- 行
  | .xin,  .jian => some .shi    -- 施
  | _, _ => none
```

---

## 6. Tier 1.6 — 本内 internal 算子

每本内部的 manipulation algorithms。

### 6.1 物 内部（3 字）

```
聚 : Multi(物) → 物              aggregate
分 : 物 → Multi(物)              mereological split
指 : Context → 物                ostension
```

### 6.2 動 内部（3 字）

```
续 : 動 → 動                     continuation
断 : 動 → (動, 動)               temporal split
节 : 動 → Stream<事件>           rhythmize / discretize
```

### 6.3 間 内部（2 字）

```
连 : 間 × 位 × 位 → 間           add edge
绝 : 間 × 位 × 位 → 間           remove edge
```

### 6.4 心 内部（2 字）[新]

```
省 : 心 → 心                     reflexive turn (turn back on self)
静 : 心 → 心                     quiescent hold (sustained quiet)
```

- **省**：字源 *少目*（微视）。古典："吾日三省吾身"。承担心的 *self-examination*。
- **静**：字源 *青争*（澄澈）。古典："静而后能安"。承担心的 *quiescent state*。

**心-internal adjunctions**：
```
省 ⊣ 静        reflexive-turn ⊣ quiescent-hold
```

省是 active inward turn，静是 passive sustained quiet。互为 dual。

### 6.5 内部 split-merge adjoint

```
分 ⊣ 聚        物 内部 split-merge
断 ⊣ 续        動 内部 split-merge
绝 ⊣ 连        間 内部 split-merge
省 ⊣ 静        心 内部 split-merge analog
```

四本各有自己的 internal split-merge adjoint pair。结构对称。

---

## 7. Tier 2 — 六显

四本两两相交，二本括除，得 C(4,2) = 6 显化。

### 7.1 三本侧三显（既有 Lean）

```
位 = 物 ∩ 間, (動,心) 括除
場 = 動 ∩ 物, (間,心) 括除
際 = 間 ∩ 動, (物,心) 括除
```

| 显 | 形态 | Tier 1.5 等价生成 |
|---|---|---|
| **位** | 点状定位 | 子(場) |
| **場** | 延展介质 | 作(物) |
| **際** | 接触界面 | 演(間) |

### 7.2 心本侧三显（新）

```
象 = 心 ∩ 物, (動,間) 括除
思 = 心 ∩ 動, (物,間) 括除
境 = 心 ∩ 間, (物,動) 括除
```

| 显 | 形态 | Tier 1.5 等价生成 | 古典锚点 |
|---|---|---|---|
| **象** | 主体所对的对象 | 触(物) | 易传"在天成象"、佛教"诸法实相" |
| **思** | 主体随过程的流动 | 历(動) | 大学"虑而后能得"、子思 |
| **境** | 主体所栖的关系全场 | 悟(間) | 海德格尔 Umwelt、佛教"境界" |

**字源解释**：
- **象**：象之形——*作为图像呈现之物*。物-as-appears-to-mind，与 物（thing-in-itself）区分
- **思**：从田从心——*在心田中流动的内容*
- **境**：从土从竟——*所栖之地的边界与内域*

### 7.3 法则 18：六显的双重生成 equivalence

每显有两条 derivation path：

```
显 from "二本相交+二本括除"  ≡  显 from "Tier 1.5 transformation 算子作用"
```

```lean
theorem manifestation_dual_generation :
  ∀ m : Manifestation, 
    intersection_form m ≡ transformation_form m
```

这是 **核心 commutativity 定理**。

```lean
inductive Manifestation where
  | wei | chang | ji          -- 既有
  | xiang | si | jing         -- 新

def visibleRoots : Manifestation → List OnticRoot
  | .wei  => [.wu, .jian]
  | .chang => [.dong, .wu]
  | .ji   => [.jian, .dong]
  | .xiang => [.xin, .wu]
  | .si   => [.xin, .dong]
  | .jing => [.xin, .jian]

def bracketedRoots : Manifestation → List OnticRoot
  | .wei  => [.dong, .xin]
  | .chang => [.jian, .xin]
  | .ji   => [.wu, .xin]
  | .xiang => [.dong, .jian]
  | .si   => [.wu, .jian]
  | .jing => [.wu, .dong]

theorem every_manifestation_brackets_two_roots :
  ∀ m : Manifestation, m.bracketedRoots.length = 2
```

---

## 8. Tier 2.5 — 显化派生算子

派生于显化对象上的 second-order 算子。

```
界 : 場 → ∂場                    boundary of field
轨 : 動 → Path                   accumulated trajectory
缘 : 際 → ConditionMatrix        conditioning at interface
含 : 境 → ContextMatrix          enveloping context of lifeworld
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
```

界产出 triple：
- **内** : Region (bounded interior)
- **∂** : Boundary (the line itself)
- **外** : Region (exterior, often = 空 if 全外)

这把 *界内 / 界外* 显式化，并连接 Tier 7 的 **空**：

```
界(全宇宙之 場).外 = 空
```

天界外为空——没有更外的场，所以外部是 empty event。

### 8.2 缘 的双层 self-reference

**缘** 出现在两处：
- Tier 2.5：际的 conditioning（际之所依的条件）
- Tier 6.6：因缘果中的 conditioning（causal chain 中的 conditioning）

这两处不是不同字，是 **同一概念在不同 level 的应用**：缘 = conditioning that enables a manifestation/event。在 际 处它是 *接触条件*，在因果链处它是 *因果条件*。dispatch rule：context-determined。

---

## 9. Tier 3 — 六征 + 闸口 + 事件

### 9.1 三本侧三征（既有 Lean）

```
幾 : 位 的动征             0维处的"将而未"
勢 : 場 的动征             連续介质上幾的铺开
機 : 際 的动征             拓扑路由上幾的汇聚
```

定理（既有）：
```
勢 = 幾 沿连续介质铺开
機 = 幾 沿拓扑路由汇聚
```

### 9.2 心本侧三征（新）

```
萌 : 象 的动征             主体性的微兆
绪 : 思 的动征             思绪的张力
韵 : 境 的动征             境界的氛围
```

| 字 | 字源 | 工作 |
|---|---|---|
| **萌** | 草明（草初出） | 主体觉知的微生 |
| **绪** | 系者（丝头） | 思流的张力 |
| **韵** | 音员（声调） | 境之氛围质感 |

**对偶定理**（候选）：
```
绪 = 萌 沿主体过程铺开
韵 = 萌 沿主体关系汇聚
```

镜像于三本侧的 勢/機 = 幾 在两方向的展开。

### 9.3 闸口（既有，扩展）

```
開 / 閉 : 動征 → 事件
```

二值 only。

### 9.4 事件输出表

三本侧（既有）：
| 征 | 開 → | 閉 → |
|---|---|---|
| 幾 | 生 | 灭 |
| 勢 | 成 | 反 |
| 機 | 转 | 守 |

心本侧（新）：
| 征 | 開 → | 閉 → |
|---|---|---|
| 萌 | 醒 | 眠 |
| 绪 | 进 | 退 |
| 韵 | 畅 | 塞 |

注：**生** 在 Tier 3（闸口下游）和 Tier 6（generative algorithm）双层使用。dispatch：Tier 3 的 生 是 *事件类型 token*，Tier 6 的 生 是 *constructor*。两者通过 fixed-point 关系 consistent：constructor 的 instantiation 经过 闸口 生 这一步。

```lean
inductive DynamicMark where
  | ji | shi | jiMoment           -- 既有 幾勢機
  | meng | xu | yun               -- 新 萌绪韵

def DynamicMark.ofManifestation : Manifestation → DynamicMark
  | .wei => .ji      | .chang => .shi   | .ji => .jiMoment
  | .xiang => .meng  | .si => .xu       | .jing => .yun

inductive Event where
  | sheng | mie | cheng | fan | zhuan | shou
  | xing | mian | jin | tui | chang | sai

def Gate.result : DynamicMark → Bool → Event
  | .ji,    true  => .sheng    | .ji,    false => .mie
  | .shi,   true  => .cheng    | .shi,   false => .fan
  | .jiMoment, true => .zhuan  | .jiMoment, false => .shou
  | .meng,  true  => .xing     | .meng,  false => .mian
  | .xu,    true  => .jin      | .xu,    false => .tui
  | .yun,   true  => .chang    | .yun,   false => .sai
```

---

## 10. Tier 4 — 合成形态

### 10.1 三本侧合成（既有 Lean）

```
網 = 位 + 際                 关系图
體 = 位 + 場                 实体
流 = 場 + 際                 过程
```

回授（既有）：
```
網 → 位      體 → 場      流 → 際
```

### 10.2 心本侧合成（新）

```
我 = 象 + 境                 self-as-situated-object
念 = 象 + 思                 thought-as-content-in-stream
神 = 思 + 境                 spirit-as-stream-in-lifeworld
```

| 字 | 字源 | 工作 |
|---|---|---|
| **我** | 戈手（持戈者）→ self | 主体作为对象在境中 |
| **念** | 今心 | 单一思维单元 |
| **神** | 申示（伸展之示） | lived integration of stream and context |

回授（新）：
```
我 → 象      念 → 思      神 → 境
```

### 10.3 跨侧合成 [待决]

3×3 = 9 cross-side composites。最有意义候选：
- 位+象：thing-encountered
- 場+思：lived process
- 際+境：encountered-other

**[待决]**：是否将 9 cross-side composites 全部 commit。Phase 4 决定。

```lean
inductive CompositeForm where
  | wang | ti | liu          -- 既有
  | wo | nian | shen          -- 新
```

---

## 11. Tier 5 — Reading 算子 + invariants

每本一个 reading operator，提取该本的 invariant。

### 11.1 四本 reading 算子（4 字）

```
質 : 物 → 体                substantive identity
律 : 動 → 道                law / way-path
性 : 間 → 用                relational nature
觉 : 心 → 明                lucidity / awareness
```

[self-ref: 觉 同时是 Tier 5.5 cognition 算子]

### 11.2 四 invariants（4 字）

```
体 : 質(物) 的 fixed point          实质身份
道 : 律(動) 的 fixed point          所循之径
用 : 性(間) 的 fixed point          功能关系
明 : 觉(心) 的 fixed point          清明觉性
```

### 11.3 四字组合（古典 attestation）

四 invariant 字的两两组合在古典文献中均自然出现：

| 组合 | 古典文献 |
|---|---|
| 体用 | 朱熹"理一分殊" / 王阳明"体用一原" |
| 体道 | 庄子"得其环中"/ 韩愈"原道" |
| 体明 | "明体达用" |
| 道用 | "道用一如" |
| 道明 | "明道" |
| 用明 | 大学"明明德" |

四字相互勾连，形成 invariants 之间的 cross-references。

### 11.4 体用一如的 Yoneda 形式化（法则 9 扩展）

```
体(p) ≅ Hom(p, -) over 間-positions   通过 遍 算子
道(d) = invariant pattern of 律 over 動-trajectory
用(q) ≅ Hom(-, q) over 物-instances   通过 遍 算子
明(s) = lucidity of 觉 over 心-reflexion
```

四 invariants 通过 **遍** 算子互相 entangled：每个 invariant 由其 reading operator 在所有相对位置的 traversal 决定。

---

## 12. Tier 5.5 — Cognition 五字

主体 *向内 reading 事* 的 inbound 算子（5 字）。

```
觉 : 事 → Awareness                    bare awareness（最 raw）
见 : 事 → Phenomenology                direct seeing
观 : 事 × Context → Projection         contextual measurement
知 : 事 → Knowledge                    propositional knowing
遍 : 事 → (Context → Reading)          systematic traversal
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
```

按 conceptual mediation 程度排序。觉最 raw（pre-symbolic awareness），知最 conceptual（propositional），遍最 systematic（exhaustive traversal）。

### 12.2 古典锚点

- **觉**：佛教"本觉"、王阳明"良知"
- **见**：庄子"以神遇而不以目视"
- **观**：易传"观乎天文以察时变"
- **知**：荀子"凡以知，人之性也；可以知，物之理也"
- **遍**：华严"一即一切"

### 12.3 非对易性（法则 11）

```
[观₍i₎, 观₍j₎] ≠ 0    for i ≠ j ∈ {物, 動, 間, 心}
```

跨本 measurement 不对易。波粒二象性的精确化身。共 C(4,2) = 6 对 non-commuting。

---

## 13. Tier 5.6 — Mode 五字

主体 *向外 engage 事* 的 outbound 算子（5 字）。

```
感 : 主体 × 事 → ReceptiveState        pre-conceptual receptivity
是 : 主体 × 事 → Predication           propositional positing
约 : 主体 × 事 → Commitment            constraint-binding
修 : 主体 × 事 → CultivationProcess    iterative refinement
诚 : 主体 × 事 → AuthenticAlignment    authentic alignment
```

[self-ref: 约 同时是 Tier 1.5 動→間 transformation]

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

按 engagement 深度排序。感最 raw（receptivity），诚最 deep（authentic alignment with ground truth）。

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
```

5 对 adjoint。每对：reading inbound ⊣ engagement outbound。这是王阳明在 framework 内的 derivable theorem。

```lean
def cognitionModeAdjunction : List (Cognition × Mode) :=
  [(.jue, .gan), (.jian, .shi), (.guan, .yue), (.zhi, .xiu), (.bian, .cheng)]

theorem zhi_xing_he_yi : 
  ∀ (c, m) ∈ cognitionModeAdjunction, isAdjoint c m
```

---

## 14. Tier 6 — Generative / Persistence

```
生 : Context → 事                   event constructor
存 : 事 → 事                        persistence / identity-over-time
涌 : Pattern(Multi(事)) → 事ᴸ⁺¹    emergence / level-transition
```

[self-ref: 生 同时是 Tier 3 闸口下游事件 token]

### 14.1 涌的 level transition

```
涌 : Pattern(Multi(事ᴸ)) → 事ᴸ⁺¹
```

涌 把 lower-level 多重模式 lift 为 higher-level 实体。Examples:
- 蜂群 → 蜂巢
- 神经元 → 意识
- 粒子 → 物体
- 字 → 句

**法则 13**：涌(level n) ≠ trivial iter——涌 不是 simple aggregation，每次需新 aggregation pattern。

### 14.2 三时态结构

```
生 → 化 → 存 → 灭        (循环)
```

[化 在 Tier 6.7]

生发——演化——保持——消灭，构成时间性的最小四元结构。

---

## 15. Tier 6.5 — Modal 六字

```
隐 : 事 → LatentEvent              hide / latent shift
现 : LatentEvent → 事              manifest / reveal
限 : 事 × Constraint → 事          impose constraint
许 : 事 × Constraint → 事          relax constraint
实 : 事 → ActualEvent              actualize（new）
虚 : 事 → CounterfactualEvent      counterfactualize（new）
```

| 字 | 字源 | 工作 |
|---|---|---|
| **隐** | 阜㥯 | hidden but real |
| **现** | 王见 | manifest from latent |
| **限** | 阜艮 | impose constraint |
| **许** | 言午 | relax / permit |
| **实** | 宀贯 | actualize / make real（**新**） |
| **虚** | 虍业 | counterfactual / latent space（**新**） |

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

两 pair 不重合。隐的事 *已经* 发生，只是 hidden；虚的事 *未* 发生，是 modal alternative。

### 15.3 与闸口下游的关系

```
開 = 现 at 0-dim event-commit
閉 = 隐 at 0-dim event-commit
```

闸口的 開/閉 是 隐/现 在 0维事件 commit 处的 binary specialization。

---

## 16. Tier 6.6 — Causal Morphism 七字

```
因 : 事 → CausalGround
缘 : 事 → Conditions
果 : 事 → Effect
致 : 事 × 事 → CausalMorphism      strict causation
应 : 事 × 事 → ResponseMorphism    correspondence
报 : 事 → 事 (later)               karmic return（new）
承 : 事 × 事 → Continuation        continuation（new）
```

[self-ref: 缘 同时是 Tier 2.5 显化派生]

| 字 | 字源 | 工作 |
|---|---|---|
| **因** | 大囗 | causal ground |
| **缘** | 系彖 | conditioning |
| **果** | 木 | effect / fruit |
| **致** | 至攵 | bring-about |
| **应** | 心雁 | correspondence |
| **报** | 幸又 | karmic return（**新**） |
| **承** | 手丞 | bearing-forward（**新**） |

### 16.1 法则 15：因缘果链

```
致(因, 果) requires 缘
¬ ∃ causation without conditioning
```

因到果不是直接 morphism，必须经 缘 的 conditioning。

### 16.2 报/承 的扩展

- **报**：A 致 B，B 在某时回报 A（cyclic causation）。佛教"善有善报"。
- **承**：A 致 B，B 承受 A 的 effect 并 forward。enables long causation chains。

```
报 : 事 → (事 ∘ 致 ∘ ... ∘ 致 ∘ 自身)    reflexive causation
承 : 事 × 事 → 事                          forwarding morphism
```

---

## 17. Tier 6.7 — Identity / Meta 七字

```
同 : 事 × 事 → Bool             identity test
异 : 事 × 事 → Bool             difference test
似 : 事 × 事 → Degree           similarity degree
对 : 事 × 事 → Correspondence   pair / braiding
辨 : 事 → Kind                  kind discrimination
类 : 事 → ClassMembership       class membership
化 : 事 → 事                    temporal evolution
```

[self-ref: 类 同时是 Tier 8 type universe，化 是 動 的 algorithm 化身]

### 17.1 化 的特殊地位

```
化 : 事 → 事
化 = 動-as-operator
化* : 事 → Stream<事>          (iterated → trajectory)
```

化 是 動 这一本的 algorithmic 化身。其 iteration 生成 trajectory，等价于合成形态 **流**：

```
法则 14: 化* generates 流
```

### 17.2 对 作为 braiding

```
对 : 事 × 事 → 事 × 事 (swap with structure)
```

在 Tier 7 monoidal structure 中，**对** 充当 symmetric braiding。

---

## 18. Tier 7 — Algebraic Structural 五字

承担 algebra 的最底层结构 marker。**v7 关键改动：用 合 替换 抱，加入 和**。

```
合 : 事 × 事 → 事              monoidal product (multiplicative)
和 : 事 × 事 → 事              additive harmonic union
寂 : Unit                      monoidal identity (for 合)
空 : Empty                     additive identity (for 和) / empty event
无 : 事 → 事                   logical negation
```

| 字 | 字源 | 工作 |
|---|---|---|
| **合** | 亼口（聚口） | multiplicative combination |
| **和** | 禾口（禾粟和声） | additive harmonic union, 和而不同 |
| **寂** | 宀叔 | quiescent identity |
| **空** | 穴工 | empty / void |
| **无** | 無 | logical negation |

### 18.1 v7 关键改动说明

**抱 → 合**：之前 v6 用 抱 作 monoidal product。v7 改为 合，理由：

- 合 在古典中文里更基础（天人合一、合二为一）
- 合 已有 algebraic 味道（combine, fit-together）
- 抱 太具象身体性，不适合抽象代数 layer
- 合/和/生 progression 更准确反映古典中国哲学的组合 schema

**加 和**：和 不是 redundant with 合：

- **合**：multiplicative product（A 合 B = A ⊗ B）
- **和**：additive harmonic union（A 和 B = A ⊕ B with harmony）
- **生**：emergent generation（合(A, B) 产生新 C）

进展：A 和 B 先 **合** 在一起 → 然后 **和** 谐共存 → 最终 **生** 出新的 C。

### 18.2 古典锚点

- 易传："二气交感，化生万物"——合 → 和 → 生 progression
- 中庸："致中和，天地位焉，万物育焉"——和 是 harmony
- 论语："君子和而不同，小人同而不和"——和 ≠ 同

---

## 19. Tier 8 — Type Universe 五字

```
态 : 事 → State                    state space at type level
形 : 事 → Form                     form / shape
量 : 事 → Measure                  measure / quantity
度 : 事 → Degree                   graduated measure（new）
序 : 事 → Order                    ordered sequence at type level（new）
```

[self-ref: 类 also Tier 6.7]

| 字 | 字源 | 工作 |
|---|---|---|
| **态** | 心能 | state space |
| **形** | 开彡 | form / shape |
| **量** | 重旦 | measure / quantity |
| **度** | 庶又 | graduated measure（**新**） |
| **序** | 广予 | ordered sequence（**新**） |

### 19.1 Type universe 角色

这五字承担 *type-level objects*——不是 instance，是 type universe 的 first-class citizens。

```
态 :: TypeUniverse  -- a type of states
形 :: TypeUniverse  -- a type of forms
量 :: TypeUniverse  -- a type of quantities
度 :: TypeUniverse  -- a type of degrees
序 :: TypeUniverse  -- a type of ordered sequences
```

这些类型可以 parameterize 其他算子：例如 `量(物)` 给出 物的 measure type。

### 19.2 与 reading invariants 的关系

```
体 :: 态(物)        substance is a kind of state
道 :: 序(動)        way is a kind of order
用 :: 形(間)        function is a kind of form
明 :: 度(心)        lucidity is a kind of degree
```

四 invariants 各自栖居于 Tier 8 的 type universes 中。

---

## 20. 完整字汇表

### 20.1 按 Tier 排列

| Tier | 层级名 | 字 | 字数 |
|---|---|---|---|
| 0 | 底座 | 事 | 1 |
| 1 | 四本 | 物 動 間 心 | 4 |
| 1.5 | 本间 transformation | 作 联 子 散 约 结 演 触 历 悟 意 行 施 | 13 |
| 1.6 | 本内 internal | 聚 分 指 续 断 节 连 绝 省 静 | 10 |
| 2 | 六显 | 位 場 際 象 思 境 | 6 |
| 2.5 | 显化派生 | 界 轨 缘 含 | 4 |
| 3 | 六征+闸口+事件 | 幾 勢 機 萌 绪 韵 開 閉 生 灭 成 反 转 守 醒 眠 进 退 畅 塞 | 20 |
| 4 | 合成 | 網 體 流 我 念 神 | 6 |
| 5 | reading + invariants | 質 律 性 觉 体 道 用 明 | 8 |
| 5.5 | cognition | 觉 见 观 知 遍 | 5 |
| 5.6 | mode | 感 是 约 修 诚 | 5 |
| 6 | generative/persistence | 生 存 涌 | 3 |
| 6.5 | modal | 隐 现 限 许 实 虚 | 6 |
| 6.6 | causal | 因 缘 果 致 应 报 承 | 7 |
| 6.7 | identity/meta | 同 异 似 对 辨 类 化 | 7 |
| 7 | algebraic structural | 合 和 寂 空 无 | 5 |
| 8 | type universe | 态 形 量 度 序 | 5 |

### 20.2 Self-reference 字（multi-tier）

| 字 | 出现 Tiers | 关系说明 |
|---|---|---|
| 觉 | 5, 5.5 | reading 算子 = cognition 算子（awareness 双义） |
| 缘 | 2.5, 6.6 | 际之 conditioning = 因果链 conditioning |
| 生 | 3, 6 | 闸口下游事件 = constructor algorithm |
| 类 | 6.7, 8 | identity meta = type universe |
| 化 | 6.7, 動 | identity meta = 動 algorithm |
| 分 | 1.6 | 物内部 split (single tier; mentioned twice) |
| 约 | 1.5, 5.6 | transformation = mode commitment |

7 字承担 multi-tier 身份。

### 20.3 Unique 字数统计

```
总字数（含 self-ref 双计）：约 115
独立 unique 字数：约 108
```

精确数字在 Phase 1 Lean register 时 lock。

---

## 21. Adjoint Pairs 完整清单

### 21.1 Tier 1.5 transformation adjunctions（6 对）

```
作 ⊣ 子              activate (物→動) ⊣ localize (動→物)
联 ⊣ 结              link (Multi→間) ⊣ crystallize (間→位)
演 ⊣ 约              unfold (間→動) ⊣ summarize (動→間)
意 ⊣ 触              intend (心→物) ⊣ touched (物→心)
行 ⊣ 历              enact (心→動) ⊣ experience (動→心)
施 ⊣ 悟              institute (心→間) ⊣ comprehend (間→心)
```

### 21.2 Tier 1.6 internal split-merge（4 对）

```
分 ⊣ 聚              物 内部
断 ⊣ 续              動 内部
绝 ⊣ 连              間 内部
省 ⊣ 静              心 内部
```

### 21.3 Tier 5.5/5.6 知行合一（5 对）

```
觉 ⊣ 感              bare-awareness ⊣ receptivity
见 ⊣ 是              direct-seeing ⊣ positing
观 ⊣ 约              contextual-measure ⊣ commitment
知 ⊣ 修              cognition ⊣ cultivation
遍 ⊣ 诚              traversal ⊣ authentic-alignment
```

### 21.4 Tier 6.5 modal（3 对）

```
隐 ⊣ 现              hide ⊣ reveal
许 ⊣ 限              permit ⊣ constrain
实 ⊣ 虚              actualize ⊣ counterfactualize
```

### 21.5 子 ⊣ 散 special

```
子 ⊣ 散              localize ⊣ delocalize
```

这是跨 Tier 1.5 的额外 adjoint（作⊣子 + 子⊣散 共享 子 算子）。

### 21.6 总计

**19 对 adjoint pairs**。比 v6 的 15 对多 4 对（加 4 心-internal + 1 modal new + 1 子⊣散 - 2 减少 abstracted）。

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
theorem adjoint_unit_counit : ∀ p ∈ allAdjointPairs, isProperAdjoint p
```

---

## 22. Semiring 结构

### 22.1 (事, 和, 空, 合, 寂) 是 commutative semiring

```
(和)  : commutative monoid with identity 空
(合)  : commutative monoid with identity 寂  
(distributivity): A 合 (B 和 C) = (A 合 B) 和 (A 合 C)
                  (A 和 B) 合 C = (A 合 C) 和 (B 合 C)
(absorption): A 合 空 = 空
```

### 22.2 加上 生 的 progression

合 / 和 / 生 不是平行算子，是 progression：

```
合 : 事 × 事 → 事ᴬ⁺ᴮ        (raw combination)
和 : 事ᴬ⁺ᴮ → 事ᴬ⊕ᴮ_harmonized   (achieve harmony)
生 : 事ᴬ⊕ᴮ_harmonized → 事ᶜ_emergent  (generate new)
```

可写为：
```
生 ∘ 和 ∘ 合 : 事 × 事 → 事ᶜ
```

这正是易传"二气交感，化生万物"的形式化。

### 22.3 加 无 / 实 / 虚 的代数

```
无 : 事 → 事 (involution: 无 ∘ 无 = id)
实 : 事 → 事 (idempotent on actual events)
虚 : 事 → 事 (idempotent on counterfactual events)
实 ∘ 虚 = ⊥, 虚 ∘ 实 = ⊥                  (mutual exclusion)
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
  对 : symmetric braiding (for monoidal)
```

```lean
class Semiring (E : Type) where
  he : E → E → E       -- 和
  empty : E             -- 空
  he_comm : ∀ a b, he a b = he b a
  he_assoc : ∀ a b c, he (he a b) c = he a (he b c)
  he_empty : ∀ a, he a empty = a
  he_unit : ∀ a, he empty a = a
  
  he_combine : E → E → E   -- 合
  jiao : E              -- 寂
  he_combine_comm : ∀ a b, he_combine a b = he_combine b a
  -- ...
  distributivity : ∀ a b c, 
    he_combine a (he b c) = he (he_combine a b) (he_combine a c)
  absorption : ∀ a, he_combine a empty = empty
```

---

## 23. Self-Reference 字

7 字承担 multi-tier 身份。Dispatch rule 由 context 决定。

### 23.1 dispatch rule schema

每个 self-ref 字在 type system 中有 explicit level marker：

```lean
inductive Level where
  | tier1_5 | tier2_5 | tier3 | tier5 | tier5_5 | tier5_6 | tier6 | tier6_7 | tier8

structure SelfRefChar where
  glyph : String
  levels : List Level
  dispatch : Context → Level
```

### 23.2 七 self-ref 字详解

#### 觉

```
觉@5 : 心 → 明                  reading operator
觉@5.5 : 事 → Awareness         cognition operator
```

- **关系**：reading 心 yields awareness（明）；general 觉 applies to any 事 yielding general awareness。两者一致：`觉@5 = 觉@5.5 specialized to 心`
- **Dispatch**：input type is 心 → use @5; otherwise → use @5.5

#### 缘

```
缘@2.5 : 際 → ConditionMatrix     际之派生
缘@6.6 : 事 → Conditions           因果链中
```

- **关系**：两处都是 *conditioning that enables*。在际处是接触条件，在因果处是因果条件。是 *concept hierarchy* 不是 *ambiguity*。
- **Dispatch**：input type is 際 → use @2.5; otherwise → use @6.6

#### 生

```
生@3 : Event token              闸口下游事件
生@6 : Context → 事             constructor
```

- **关系**：constructor instantiation 经过 闸口 yielding 生 event token。两者通过 fixed-point relation consistent。
- **Dispatch**：input is Context → @6; output of 闸口 → @3

#### 类

```
类@6.7 : 事 → ClassMembership    instance classification
类@8 : Kind universe              type-level kind
```

- **关系**：classification at instance level vs type universe at type level。是 *level lifting*。
- **Dispatch**：input is 事 → @6.7; type-level reference → @8

#### 化

```
化@6.7 : 事 → 事                 identity meta evolution
化@動-algorithm                   動 的算子化身
```

- **关系**：化是 動 这一本的 algorithm。在 Tier 6.7 它作为 generic temporal evolution；implicitly 它是 動 的 algorithmic embodiment。
- **Dispatch**：always 化@6.7 syntactically; semantically 化 = 動 in algorithm form。

#### 约

```
约@1.5 : 動 → 間                 transformation
约@5.6 : 主体 × 事 → Commitment   mode
```

- **关系**：两者都是 *binding to constraint*。在 transformation 是 abstract-summary（过程被约简为关系）；在 mode 是 commitment（主体约定到承诺）。同一动作的两面。
- **Dispatch**：context provides 主体 → @5.6; context is purely 動→間 → @1.5

#### 分

```
分@1.6 : 物 → Multi(物)           物内部 split
分 (general) : ?                  ?
```

- **关系**：v7 中 分 仅在 Tier 1.6 出现一次。Self-ref 标记 reserved for future。
- **Dispatch**：always @1.6 in v7

### 23.3 Dispatch 完备性

7 self-ref 字均有 deterministic dispatch rule based on input/output types or context. Phase 1 Lean implementation must encode dispatch as type-level inference。

---

## 24. 法则总览

v7 共 21 条法则。

### 24.1 既有 Lean 法则（保留）

```
法则 1 (四本不可还原):
  ∀ i,j ∈ {物, 動, 間, 心}, i ≠ j: ¬∃ iso f: i → j

法则 2 (显化括除):
  ∀ 显 ∈ 六显, ∃! 二本被括除而不缺席

法则 4 (三征驱动):
  (位, 幾) (場, 勢) (際, 機) (象, 萌) (思, 绪) (境, 韵) drive 闸口

法则 5 (闸口二值):
  Open(動征) ∪ Close(動征) covers, disjoint, exhaustive

法则 6 (合成不可逆):
  ∃ 多 arrangements giving same parts

法则 7 (反馈律):
  網→位, 體→場, 流→際, 我→象, 念→思, 神→境

法则 12 (自指):
  ontology_is_instance_of_its_own_shape
```

### 24.2 v6/v7 新增法则

```
法则 3 (子化产生位 + 心扩展):
  位 = 子(場) = 物 ∩ 間 with (動,心) bracketed
  象 = 触(物) = 心 ∩ 物 with (動,間) bracketed
  思 = 历(動) = 心 ∩ 動 with (物,間) bracketed
  境 = 悟(間) = 心 ∩ 間 with (物,動) bracketed

法则 8 (Adjoint pairs hold):
  19 对 adjunctions in Section 21

法则 9 (体用一如, Yoneda 扩展四 invariants):
  体, 道, 用, 明 互相通过 遍 算子 entangled

法则 10 (知行合一):
  cognition ⊣ mode (5 对 adjoint)

法则 11 (非对易):
  [观₍i₎, 观₍j₎] ≠ 0 for i ≠ j ∈ {物,動,間,心}
  6 对 non-commuting

法则 13 (涌现非平凡):
  涌(level n) ≠ trivial iter

法则 14 (化生时间):
  化* generates 流

法则 15 (因缘果链):
  致(因, 果) requires 缘

法则 16 (空界关系):
  界(場) = (内, ∂, 外)
  外 ⊆ 空 if no surrounding 場

法则 17 (心不可外化):
  ∀ f: 心 → (物 ∪ 動 ∪ 間), f is lossy projection

法则 18 (六显双重生成):
  intersection_form ≡ transformation_form
```

### 24.3 v7 新增法则（4 条）

```
法则 19 (Semiring):
  (事, 和, 空, 合, 寂) is commutative semiring

法则 20 (合和生 progression):
  生 ∘ 和 ∘ 合 : 事 × 事 → 事ᶜ_emergent

法则 21 (实虚 modal decomposition):
  ∀ event e, e = 实(e) ⊕ 虚(e)
  实 ∘ 虚 = ⊥
```

```lean
-- 法则 21 形式化
theorem actual_counterfactual_decomposition :
  ∀ e : 事, e = combine (shi e) (xu e)
  ∧ shi (xu e) = bottom
  ∧ xu (shi e) = bottom
```

---

## 25. Lock Algebra 路线图

### Phase 1: 字汇 Lean module（约 2 周）

```lean
-- 扩展 Tier1Term inductive type
inductive Tier1Term where
  | shi  -- 事
  | wu | dong | jian | xin                    -- 四本
  | wei | chang | ji | xiang | si | jing      -- 六显
  | -- ... (全部 ~108 字)

def allTier1Terms : List Tier1Term := ...
theorem tier1_count : allTier1Terms.length = 108
theorem tier1_glyphs_registered : ...

-- 扩展 OnticRoot
inductive OnticRoot where
  | wu | dong | jian | xin

-- 扩展 Manifestation 
inductive Manifestation where
  | wei | chang | ji | xiang | si | jing
```

**目标**：所有字 register 为 Lean term，字源 / Tier / 类型 / 古典锚点 全部 metadata 化。

### Phase 2: 显化结构（约 1 周）

```lean
-- 六显完整定义
def visibleRoots / bracketedRoots
theorem every_manifestation_brackets_two_roots
theorem manifestation_dual_generation  -- 法则 18

-- 心-side 三显特殊性
theorem xin_manifestation_unique : 
  ∀ m ∈ {.xiang, .si, .jing}, OnticRoot.xin ∈ m.visibleRoots
```

### Phase 3: Tier 1.5 transformation 矩阵（约 2 周）

```lean
-- 12-cell transformation table
def transform : OnticRoot → OnticRoot → Option Operator

-- 6 心-related adjoints
theorem yi_chu_adjoint : isAdjoint .yi .chu
theorem xing_li_adjoint : isAdjoint .xing .li  
theorem shi_wu_adjoint : isAdjoint .shi .wu

-- 3 三本-internal adjoints  
theorem zuo_zi_adjoint : isAdjoint .zuo .zi
theorem lian_jie_adjoint : isAdjoint .lian .jie
theorem yan_yue_adjoint : isAdjoint .yan .yue
```

### Phase 4: 三征 + 闸口扩展（约 1 周）

```lean
-- 萌绪韵 加入 DynamicMark
inductive DynamicMark where | ji | shi | jiMoment | meng | xu | yun

-- 心-side gate outputs
inductive Event where
  | sheng | mie | cheng | fan | zhuan | shou
  | xing | mian | jin | tui | chang | sai

theorem gate_results_complete : ∀ d : DynamicMark, ∀ b : Bool, ...
```

### Phase 5: Reading + Cognition + Mode（约 2 周）

```lean
-- Tier 5 reading invariants
def reading : OnticRoot → ReadingOp
  | .wu => .zhi  | .dong => .lu  | .jian => .xing  | .xin => .jue

-- Tier 5.5/5.6 知行合一 adjunctions
def cognitionModeAdjunction : List (Cognition × Mode)

theorem zhi_xing_he_yi : 
  ∀ (c, m) ∈ cognitionModeAdjunction, isAdjoint c m

-- Yoneda for invariants
theorem ti_yong_ru_yi : 
  ∀ p : 物, 体 p ≅ Hom p (-) over 間 via 遍
```

### Phase 6: Modal + Causal + Algebraic（约 2 周）

```lean
-- Tier 6.5 modal
theorem yin_xian_adjoint : isAdjoint .yin .xian
theorem shi_xu_decomposition : ∀ e, e = combine (shi e) (xu e)

-- Tier 6.6 causal
theorem yin_yuan_guo : ∀ a c, zhi a c → ∃ y, yuan y

-- Tier 7 semiring
instance : Semiring 事 where ...
theorem semiring_complete : ...
```

### Phase 7: Self-validation（约 1 周）

```lean
-- 法则 12 扩展
theorem ontology_self_validates :
  let self := ontology
  consistent (zhi self) (lu self) (xing self) (jue self)

-- 字汇完备性
theorem framework_expresses_all_test_cases :
  ∀ test : 现象学测试用例, expressible_in_framework test

-- 自洽
theorem framework_consistent :
  ∀ T1 T2 : Tier_axiom, consistent T1 T2
```

### Phase 8: 测试用例验证（约 2 周）

详见 Section 26。

### 总时间估计

约 **13 周**（3 个月）从 v7 spec 到 fully-locked Lean formalization。

---

## 26. 测试用例

每个测试必须能在 framework 内 *完整* 表达，不需框架外字。

### 26.1 双缝实验

```
事 = 光子双缝 happening
观₍位₎(事) → 子(場) → 位 → 觉(粒子轨迹) → 体(粒子身份)
观₍勢₎(事) → 場 (uncollapsed) → 觉(波纹) → 道(干涉律)
[观₍位₎, 观₍勢₎] ≠ 0 (法则 11)
∴ 不能同时测量 → 波粒二象性
```

### 26.2 王阳明知行合一

```
事 = 道德处境
知(事) ⊣ 修(事) (法则 10 的 instantiation)
∴ 不能 知 而 不 行；不能 行 而 不 知
∴ 知行合一
```

### 26.3 蜂巢涌现

```
multi-蜂 = Multi(物 at level 0)
涌(蜂群 pattern) = 蜂巢 (at level 1, 法则 13)
觉(蜂巢) ≠ 觉(单蜂群)  → emergent properties
```

### 26.4 因缘果链

```
无明 → 缘(行) → 致(无明, 行)
行 → 缘(识) → 致(行, 识)
... (十二因缘 chain)
最终: 致(无明, 苦) via 缘 (法则 15)
```

### 26.5 易传"一阴一阳之谓道"

```
阴 / 阳 = 對 (Tier 6.7 braiding pair)
合(阴, 阳) → 和(阴, 阳) → 生(阴, 阳) (法则 20)
生(阴, 阳) → 万物
道 = 律(動)的 fixed point of 阴阳 evolution
```

### 26.6 大学"明明德"

```
明(心) = 觉的 invariant (Tier 5)
"明明德" = 修(心, 明) (Tier 5.6 mode)
∴ 通过 修 这一 mode achieve 明 invariant
```

### 26.7 中庸"诚者天之道"

```
诚 = 主体 mode 最高态 (Tier 5.6)
诚 ⊣ 遍 (法则 10)
诚的 fixed point = 主体与 道(動 invariant) 对齐
∴ "诚者天之道，诚之者人之道"
```

### 26.8 framework 自指

```
self_ontology = 一个 事 of 间 type
质(self) = 字汇 (108 字, 物-aspect)
律(self) = reduction rules + 法则 (動-aspect)
性(self) = type-signature graph (間-aspect)
觉(self) = 自指意识 (心-aspect)
∴ ontology 通过自身 reading 完整表达自身 (法则 12)
```

---

## 27. 仍未决问题

### 27.1 cross-side 合成（10 cell）

3 obj + 3 subj = 6 same-side composites（已 commit）。是否补全 9 cross-side composites？

[待决：Phase 4 测试时决定]

候选策略：
- (a) 补全所有 9 cross-side composite，总 15 composites
- (b) 仅补 3 essential：位+象, 場+思, 際+境
- (c) cross-side 用 ad-hoc tuple，不另外命名字

### 27.2 对偶 invariant fixed-point

体 / 道 / 用 / 明 是否互相之间有 *more strict equivalence* 通过 遍 算子？比如 体(p) 是否能完全 equal 用(q) 在某 q 上？

[待决：Phase 5 Yoneda 形式化时严格证]

### 27.3 报/承的代数定律

报 是 reflexive causation。它的 algebraic 定律是？  
承 是 forwarding morphism。它和 致 的关系是？

[待决：Phase 6 causal 形式化时确定]

### 27.4 心-side 三征 adjoint

幾/勢/機 之间有没有 adjoint？萌/绪/韵 之间呢？

[待决：Phase 4 三征结构时探索]

### 27.5 Type universe 字数

Tier 8 五字（态/形/量/度/序）足够吗？还需要：
- 维（dimension）？
- 阶（order/level）？
- 集（set）？
- 函（function）？

[待决：Phase 5 reading + Yoneda 形式化时如缺则补]

### 27.6 主体 first-class encoding 详细

心 作为四本 vs 主体作为 inhabit 心 instance：是 fundamental aspect 还是 specific instance？

[待决：Phase 1 Lean type design 时决定 dependent types vs algebraic types]

### 27.7 Modal possible worlds semantics

虚 capture counterfactual。但 *across counterfactuals* 的 reasoning 怎么 formalize？需要 Kripke frame？或仅 modal idempotents 够？

[待决：Phase 6 modal 形式化探索]

### 27.8 化 vs 動 的精确关系

化 是 動 algorithm。但 化 在 Tier 6.7 作为 generic 算子。是否需要明确 *化* 是 動 这一本上 algorithm 的 specialization？

[待决：Phase 5 reading 形式化时决]

### 27.9 自指 字 Lean encoding

如何在 Lean 4 中精确 encode 7 self-ref 字的 multi-tier 身份？候选：
- (a) 同字多个 inductive constructors
- (b) 字 as polymorphic with level marker
- (c) 字 as protocol/typeclass with multiple implementations

[待决：Phase 1 type design 决]

### 27.10 framework 完备性证明

如何证 framework 是 *complete*（任何现象学 phenomena 皆 expressible）？

[待决：可能不可证，但可通过测试用例 stress-test]

---

## 28. 字源 glossary

按 Unicode order，每字给出本义、framework 角色、古典锚点。

### 一画
- **一**：[未入核] 数一，统一

### 二画
- **二**：[未入核] 数二

### 三画
- **三**：[未入核] 数三
- **干**：[未入核]
- **下**：[未入核]
- **么**：[未入核]
- **大**：[未入核]
- **子**：婴儿之形，引申种子、个体单位 / Tier 1.5 動/間→物 localize / 易传"君子以经纶"

### 四画
- **不**：[未入核]
- **无**：[原 無] 没有，否定 / Tier 7 negation / 老子"无为而无不为"
- **化**：人匕（人翻转）/ Tier 6.7 + 動 algorithm / 易传"刚柔相推而生变化"
- **分**：八刀（切分）/ Tier 1.6 物 split / 庄子"判分"
- **公**：[未入核]
- **心**：心脏之象形 / Tier 1 第四本 / 阳明"心即理"
- **见**：目儿（目可见）/ Tier 5.5 cognition / 庄子"以神遇而不以目视"
- **气**：[未入核 in v7]
- **手**：[未入核]
- **及**：[未入核]
- **历**：[原 歷] 厤（曆）/ Tier 1.5 動→心 experience
- **认**：[未入核]
- **从**：[未入核]
- **介**：[未入核]
- **凶**：[未入核]
- **分**：（重复）

### 五画
- **本**：[作为算子名，未入核字汇]
- **正**：[未入核]
- **业**：[未入核]
- **生**：草土（草从土出）/ Tier 3 + Tier 6 / 易传"生生之谓易"
- **令**：[未入核 in v7 algebraic 部分]
- **以**：[未入核]
- **几**：[原 幾] / Tier 3 三征 / 易传"知几其神乎"
- **凡**：[未入核]
- **平**：[未入核]
- **打**：[未入核]
- **正**：（重复）
- **未**：[未入核]
- **末**：[未入核]
- **节**：[原 節] 竹即（竹之节）/ Tier 1.6 動 rhythmize / 庄子"节者不嗌"
- **去**：[未入核]
- **可**：[未入核]
- **古**：[未入核]
- **句**：[未入核]
- **史**：[未入核]
- **召**：[未入核]
- **司**：[未入核]
- **叶**：[未入核]
- **号**：[未入核]
- **四**：[未入核]
- **由**：[未入核]
- **甲**：[未入核]
- **申**：[未入核]
- **田**：[未入核]
- **目**：[未入核]
- **皮**：[未入核]
- **白**：[未入核]
- **皿**：[未入核]
- **目**：（重复）
- **矛**：[未入核]
- **矢**：[未入核]
- **石**：[未入核]
- **示**：[未入核]
- **禾**：[未入核 in v7 standalone, 但 和 字含禾]
- **穴**：[未入核]
- **立**：[未入核]
- **节**：（重复）

（以下省略 ASCII 顺序，重点字源已在各 Tier 节中给出）

### 关键字源详解

#### 事
从又（手）持物。本义"做、所做"。framework 中作为 Universe，为唯一 ground。古典：易传"形而上者谓之道，形而下者谓之器"。

#### 物
牛勿（多色之牛 → 万物）。本义为多色之牛，引申为"万物"。framework 中作 0 维离散个体性的本。古典：庄子《齐物论》。

#### 動
重力（沉重之物被推动）。本义"使力使物动"。framework 中作 n 维连续过程性的本。古典：易传"穷则变，变则通"。

#### 間
门月（门缝中之月 → 间隙）。本义"间隙、缝隙"。framework 中作拓扑关系结构性的本。古典：王弼"无所不通"。

#### 心
心脏之象形。framework 中作主体反身性的第四本。古典：王阳明"心即理"、孟子"四端"。

#### 象
象之形象（大象与象征双义）。framework 中作 心 ∩ 物 显化——object-as-perceived。古典：易传"在天成象，在地成形"。

#### 思
从田从心（田中之心）。framework 中作 心 ∩ 動 显化——stream-of-thought。古典：大学"虑而后能得"、子思《中庸》。

#### 境
从土从竟（疆土之边）。framework 中作 心 ∩ 間 显化——lifeworld。古典：境界、佛教 viṣaya。

#### 体（体）
[原 體] 骨豊（祭祀之骨）。framework 中作 質(物) 的 fixed point——substantive identity。古典：朱熹"体用"、王阳明"体用一原"。

#### 道
辶首（行走之首）。framework 中作 律(動) 的 fixed point——way-path。古典：老子《道德经》、庄子。

#### 用
卜中。framework 中作 性(間) 的 fixed point——functional relation。古典："体用"。

#### 明
日月（光明）。framework 中作 觉(心) 的 fixed point——lucidity。古典：大学"明明德"、佛教"明性"。

#### 合
亼口（聚口）。framework 中作 monoidal product——multiplicative combination。古典："合二为一"、"天人合一"。

#### 和
禾口（禾粟和声）。framework 中作 additive harmonic union。古典：中庸"致中和"、论语"和而不同"。

#### 寂
宀叔（屋下安静）。framework 中作 monoidal identity for 合。古典：佛教"涅槃寂静"、道家"虚静"。

#### 空
穴工（空洞）。framework 中作 additive identity for 和 / empty event。古典：佛教"空"、般若"色即是空"。

---

## 29. v7 状态总结 / commit log

### 29.1 v6 → v7 关键改动

1. **抱 → 合**：用 合 替换 抱 作 monoidal product（更古典、更准确）
2. **加 和 / 强化 生**：和 和 生 加入 Tier 7 / Tier 6，构成 合-和-生 progression
3. **觉_显 → 象**：用 象 替换 ugly 的 觉_显，作 心 ∩ 物 显化
4. **心-side 三征 commit**：萌/绪/韵 加入 Tier 3
5. **心-internal 算子 commit**：省/静 加入 Tier 1.6
6. **加 实**：modal 加入 实/虚 对偶
7. **加 报/承**：causal 加入 报/承
8. **加 度/序**：Type universe 加入 度/序
9. **Semiring 结构 lock**：(事, 和, 空, 合, 寂) 作为 commutative semiring
10. **法则增至 21 条**：新加 19/20/21（Semiring / 合和生 progression / 实虚 modal decomposition）

### 29.2 字数统计 v7

- v6 字数：约 86
- v7 字数：约 108-115
- 增量：22-29 字（加心-side 三征/三显/合成 + Tier 7/8 扩展）

### 29.3 待完成 phase 估计

- Phase 1-2: 字汇 + 显化（3 周）
- Phase 3-4: transformation + 三征（3 周）
- Phase 5: reading + 知行合一（2 周）
- Phase 6: modal + causal + semiring（2 周）
- Phase 7-8: self-validation + 测试（3 周）
- **总计**：约 13 周 / 3 个月

### 29.4 success criteria

framework v7 算 *完整完备自洽* 当且仅当：

1. ✓ 21 条法则全部 Lean prove
2. ✓ 19 对 adjoint 全部 unit-counit 验证
3. ✓ 6 对 non-commuting 显式 spell out
4. ✓ Semiring 结构 instance 验证
5. ✓ 七 self-ref 字 dispatch deterministic
6. ✓ 八个测试用例 全部 expressible
7. ✓ framework 自指（法则 12 扩展）通过
8. ✓ 与既有 Lean 模块 backward compatible

---

## 30. handoff notes for Claude Code

### 30.1 优先 Phase 启动顺序

1. **Phase 1**（字汇）：先扩展 `Tier1Term` inductive 加入 ~22 新字。run `tier1_count` 验证 ≈108。
2. **Phase 2**（显化）：扩展 `OnticRoot` 加 `.xin`，扩展 `Manifestation` 加 `.xiang/.si/.jing`，证 `every_manifestation_brackets_two_roots`。
3. **Phase 3**（transformation）：定义 12-cell `transform` table，证 6 心-related adjoints。
4. **Phase 4-8**：按路线图。

### 30.2 Risk areas

- **Risk 1**：心 first-class encoding 可能要 dependent types。如 Lean 4 standard inductive 不够，考虑 quotient types or HoTT-style。
- **Risk 2**：自指字 dispatch 可能引入 type system 复杂度。考虑 elaborator hint。
- **Risk 3**：Semiring 验证可能需 显式构造而非 instance auto-derive。
- **Risk 4**：法则 17（心不可外化）可能不 Lean-prove，需做 axiom 而非 theorem。
- **Risk 5**：法则 10（知行合一）prove 需 主体作为 first-class object，可能需要 Phase 5 才能 spell out。

### 30.3 backward compatibility check

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

### 30.4 questions to ask user during implementation

1. cross-side 合成（27.1）选 (a) (b) (c) 哪个？
2. self-ref 字的 Lean encoding（27.9）选 (a) (b) (c) 哪个？
3. 主体 first-class encoding（27.6）需 dependent types 吗？
4. 法则 17 作为 axiom 还是 theorem？
5. Type universe 字数（27.5）够吗，是否补 维/阶？

每个 decision point pause 等用户回复，不擅自决定。

---

**End of v7 spec.**

完整、完备、自洽是目标。本草稿是 *working draft*——Phase 测试中必有调整。但骨架（四本-六显-六征-六合成 + reading + cognition + mode + 21 法则 + Semiring）已 lock。

下一步：交付 Claude Code 启动 Phase 1。
