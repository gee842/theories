# 間: Foundation Note

## On the Single Primitive Ontology

**Version**: 0.3 · *fully reorganized*
**作者**: Ren
**协作起草**: Claude

**v0.3 changelog**: 重新组织。从根改写,把零散积累的洞察聚焦为一份一致的文档。主要变化:
- 核心字集从 54 扩到 ~124 字,经过 worked examples 验证,covers full relational phenomena space
- 引入 **Layer 3: 动力学**(势、机、轨、理、节、度、常、变、动、静)用于描述 attractors 和 dynamics
- 引入**体用、心性、隐显**等中国哲学深层词汇作为本体精确性的工具(不是文化承诺)
- **古文作为 primary syntax**, S-expression 作为 ambiguous 时的 fallback
- Numbers, units, statistics, types 都是 relations, 不是 primitives
- Homoiconicity 显式化:代码即数据即日志即文档

**v0.2 changelog**: 一元论确立;"间是唯一原语"; numbers as relations。

**v0.1 changelog**: 第一次 sketch ground note。

**前置说明**: 这份 Note 是 *間 / Jian* 的本体地基,与 *間 Metaphysics v1.1* 配对使用。Metaphysics 文档用五个概念(感、位、际、誓、修)做教学性呈现;这份 Note 给出真正本体——它们都是同一個間在不同观察姿态下的呈现。读 Metaphysics 进入間 的世界,读这份 Note 看见底层。

---

## 目录

I. 立论 — 一切是间
II. 语言策略 — 古文 + ID + S-expression fallback
III. 核心字集 — 完整 ~124 字
IV. 没有 primitive types — 一切是 relation
V. Homoiconicity — 代码即数据即日志即文档
VI. 五种 Mode 作为观察姿态
VII. 三层架构 — 涉、际、动力学
VIII. SST 如何被含括
IX. Worked Examples — 古文与 S-expression 对照
X. 工程接口
XI. 与传统对话
XII. 限度
XIII. 接下来

附录 A: 一句话本体
附录 B: 核心字快查表
附录 C: 古文 syntax 速查
附录 D: 古文 ↔ S-expression 转换规则

---

## I. 立论 — 一切是间

> **一切是间。間 是唯一原语。間 即 happening,即 function evaluation。**

不是诗意修辞。是严格本体声明。

**为什么必须是一**

任何关系本体的"多原语"都会暴露循环依赖。考察五个概念(感、是、际、约、修):
- 是(identity)在哪里?——只能在 际(relation)中被识别
- 际是什么?——是感(resonance)的稳定化
- 感发生在哪?——在 是 之间
- 约(commitment)是什么?——是跨时间锁定的感模式
- 修(cultivation)是什么?——是 是 通过参与感而改变自身

每个概念的定义需要其他概念。**这种循环依赖意味着它们不是独立 primitives——是同一根本现象的不同切面**。

**为什么是 happening / function**

如果取消"实体先于关系"的预设,剩下的最基本结构是什么?

不是"东西"——东西预设实体性。
不是"状态"——状态预设承载它的什么。
不是"事件"——事件预设发生在哪。

剩下的是 **transformation 自身**:input → output,中间是 mapping。这就是 function。Lambda calculus 是这个本体最纯粹的数学化。

每次 happening 是一次 function evaluation:某些 是 涉入,transformation 发生,是 之际的 relation 改变。**这是间的唯一本体单元**。

**为什么这个 happening 叫 間**

候选词比较:
- *Process / Event*: 仍预设"在某处发生"
- *Resonance / 感*: 偏动,难表达稳定
- *Locus / 位*: 偏静,难表达流动
- *Field*: 仍预设"场中的什么"
- *間*: 既稳定也流动,既节点也关系,既空间也时间

**只有间不偏向任何一极**。日本"間"美学最深刻地把握了这一点——茶室中两人之间的"間"既是空间,也是时间,也是这两人当下关系本身。空间-时间-关系不是三件事,是同一個間的三种言说。

间不是某物。**间是"在间中之事"——既是间所在,也是间中所发生,也是这事本身**。

---

## II. 语言策略

### 总原则

间的表达使用三层混合语言:

1. **核心字 (~124 字)**: 古汉语单字承担本体精度
2. **ID (英文字符串)**: 引用具体 是、间-event、reference 等
3. **古文 syntax** (primary) + **S-expression** (fallback): 表达结构

这不是文化项目,是本体精确性选择。古文 happens to be 这个本体最好的语言形式——单字密度、词性流动、虚词系统、不强制主语,这些特征与一元 function 本体高度同构。

### 为什么是古文

古文有几个语言学特征,与间本体一致:

**单字密度**: 一字一义,每字承担最大本体含量。这与"一元 happening"对应——单元化的语言匹配单元化的本体。

**词性流动**: "修"既是动词("修身")也是名词("修者")也是形容词("修远"),根据上下文定。古文不预设"事物 vs 动作 vs 属性"的本体三分,与间不预设这种三分一致。

**虚词承担本体功能**: 之、其、以、于、然、因、果、若、则等虚词承担 happening 之间的 relations。这些虚词在工程上对应 access、let、if、cond、then、apply 等基础算子。**古文 syntax 已经是一种编程语言**——我们不需要发明,只需要 recover。

**不预设主语**: 古文里"道可道"没有明显主语。这与间"无主体在 act,只有 happening 在 happen"一致。

**这不是文化复兴**。如果有更准的语言形式,我们就用那个。古文 happens to be 现在能找到的最准。它承担的代价是文化误读风险,但本体精度收益更大。

### ID 系统

ID 是 stable reference encoding——它指向某个 是 (happening chain) 或某个 间-event,但**不描述其属性**。

英文字符串(`alice`, `project_001`, `2026-05-01T14:30`)作为方便的 encoding。本体上等价于 UUID、cryptographic hash、emoji——任何 stable reference 都可以。

ID 的几个 properties:
- Unique within scope
- Stable in lifetime  
- Cryptographically verifiable when needed
- Carries no semantic content (语义来自 happenings,不来自 ID 本身)

**在间的代码里,`alice` 不是英文单词,是 ID handle**。它的"陌生性"反而是优点,强制读者把它当 reference 处理。

### Hybrid Syntax: 古文 primary, S-expression fallback

**Primary**: 古文 syntax,自然语序、虚词、句末助词、标点(现代标点 OK)。

**Fallback**: 当出现以下情况时,切换到 S-expression:
- Nested expressions 容易歧义
- 需要 unambiguous machine parsing
- 复杂的 named arguments
- 需要 quote/unquote 的元编程

两种 syntax **isomorphic**——可以互相 transpile。同样的语义,不同的 surface form。

类比: LaTeX vs DVI、JSX vs React.createElement、markdown vs HTML。

详见附录 D 的转换规则。

---

## III. 核心字集

总数 ~124 字。每字承担本体含义,不可被英文还原。

### 1. 结构原语 (8)

```
間 jiān   — happening (唯一 primitive)
是 shì   — identity / presence
际 jì    — relation
约 yuē   — commitment / time-locked pattern
修 xiū   — cultivation / self-evolution
感 gǎn   — resonance / intensity / potential
化 huà   — transformation (qualitative change)
涉 shè   — involvement
```

### 2. 算子虚词 (14)

```
之 zhī   — possession / attribution
其 qí    — third-person reference
所 suǒ   — relativizer (that which)
者 zhě   — relativizer (the one who)
以 yǐ    — by means of, with
于 yú    — at, in, to
然 rán   — such, so (state confirmation)
而 ér    — and, yet (sequencing)
因 yīn   — because, due to
果 guǒ   — result, effect
故 gù    — therefore
若 ruò   — if (hypothetical)
则 zé    — then
否 fǒu   — else, no
```

### 3. 时序 (10)

```
前 qián  — before
后 hòu   — after
自 zì    — from
至 zhì   — to
跨 kuà   — span (interval)
循 xún   — recurring
始 shǐ   — beginning
终 zhōng — end
今 jīn   — now (current 间-event reference)
昔 xī    — past (general)
```

注:**没有 time units**(年、月、日、时、分、秒)。这些是 reference IDs,与 alice、bob 同样的本体地位。calendar string `2026-05-01` 是 ID,refer 到一个 wall-clock event。

### 4. 存在动态 (10)

```
生 shēng — emerge, give birth
灭 miè   — extinguish, vanish
立 lì    — establish
破 pò    — break, dissolve
成 chéng — become, accomplish
败 bài   — fail, fall apart
有 yǒu   — exists, possesses
无 wú    — absent, lack
在 zài   — present, being-there
存 cún   — preserved, continuing
```

注:**有/无** 是 relational existence。**在** 是 presence in a context (Heideggerian Dasein)。**存** 是 persistence over time。三者不同。

### 5. 方向变化 (12)

```
增 zēng  — increase
减 jiǎn  — decrease
益 yì    — benefit
损 sǔn   — lose / harm
得 dé    — obtain
失 shī   — miss / lose
予 yǔ    — give, bestow
受 shòu  — receive, accept
舍 shě   — release, give up
取 qǔ    — take, acquire
转 zhuǎn — turn, redirect
归 guī   — return, go back to
```

注:**予/受/舍/取** 是 give/receive/release/acquire 的 binary directional 操作,本体上 primitive。日常动词如"赠""借""卖"是这些 primitives 的组合。

### 6. 强度修饰 (8)

```
盛 shèng — flourishing, peak
衰 shuāi — declining, waning
强 qiáng — strong
弱 ruò   — weak
深 shēn  — deep
浅 qiǎn  — shallow
微 wēi   — subtle, minute
显 xiǎn  — manifest, evident
```

### 7. 距离结构 (8)

```
亲 qīn   — close, intimate
疏 shū   — distant, estranged
合 hé    — joined, united
分 fēn   — separated
内 nèi   — inner
外 wài   — outer
通 tōng  — penetrating, flowing through
塞 sè    — blocked, obstructed
```

注:**通/塞** 是 间能否流动的 binary。"塞"是 systemic dysfunction 的本体表达。

### 8. 反思认知 (8)

```
思 sī    — thinking
虑 lǜ    — deliberating, considering
知 zhī   — knowing
悟 wù    — realize, illuminate
省 xǐng  — reflect, examine self
明 míng  — clear, illuminated
迷 mí    — confused, lost
信 xìn   — trust, believe
```

### 9. 数量关系 (8)

```
计 jì    — count, cardinality
量 liàng — amount
序 xù    — order, ranking
比 bǐ    — ratio, comparison
平 píng  — average, balance
散 sàn   — variance, spread
多 duō   — many
少 shǎo  — few
```

注:数字本身(0、1、2、5、100)不是核心字,是特殊 IDs。数字必须与 relation 词同时出现——孤立的"5"无意义,"5 个 X"或"跨 5 X"才有本体地位。

### 10. 动力学 / Dynamics (10)

```
势 shì   — attractor / tendency / latent force
机 jī    — bifurcation point / critical moment
轨 guǐ   — trajectory
理 lǐ    — invariant pattern / dynamic structure
节 jié   — phase transition / joint
度 dù    — threshold / critical value
常 cháng — invariant, persistent
变 biàn  — change (often discontinuous)
动 dòng  — movement, activity
静 jìng  — stillness, rest
```

**这是 v0.3 的关键新增层**。这一层描述的不是单个 happening,是 patterns of happenings over time——attractors 和 dynamics。

- **势** = attractor: 系统中某种趋向的能量,使 trajectory 倾向某 region
- **机** = bifurcation point: 临界状态,微小扰动决定 trajectory
- **轨** = trajectory: 实际走过的路径
- **理** = invariant pattern: dynamics 遵循的内在规律
- **节** = phase transition: 系统组织方式的根本改变
- **度** = threshold: phase transition 的临界值
- **常/变** = stability vs change
- **动/静** = activity vs rest(《周易》"一动一静,互为其根")

### 11. 体用本末 (4)

```
体 tǐ    — body, structural ground
用 yòng  — function, manifestation
本 běn   — root, fundamental
末 mò    — surface, derivative
```

宋明理学最核心的对——**体是 invariant structure(对应 attractor),用是 dynamic manifestation(对应 trajectory)**。这一对让 protocol 与 instance、character 与 behavior、structure 与 process 有了精确的本体表达。

### 12. 心性情志 (5)

```
心 xīn   — heart-mind (cognition + emotion + will, indivisible)
性 xìng  — nature, essential character
情 qíng  — emotion, situation, circumstance
意 yì    — intention, mental tendency
志 zhì   — will, aspiration
```

中文心性论两千年沉淀的精确 vocabulary——描述 是 内部的 inner subject space。**这五字一起,有则全有,无则全无**——它们相互定义,共同覆盖 inner subject 的关键 dimensions。

英文需要 "essential character"、"active mind"、"situation/emotion"、"aspirational will"、"intention" 这一组词才能近似——而且仍然不准。

### 13. 隐显 (2)

```
隐 yǐn   — hidden, latent
潜 qián  — submerged, dormant
```

(微/显已列在强度修饰类。)

注:"莫见乎隐,莫显乎微"(《中庸》)——隐显是中文哲学独特的 dimension。一个 attractor 可以 latent (潜) 也可以 manifest (显)。**这一类与 Layer 3 dynamics 相关**——attractor 的 manifest 程度。

### 14. 协同响应 (6)

```
唱 chàng — initiate (in call-and-response)
应 yìng  — respond (structured answering)
和 hé    — harmony, dynamic alignment
违 wéi   — violate, go against
同 tóng  — same, agree
异 yì    — different, divergent
```

注:**唱/应** 是 leadership-following 的关系性结构。**和** vs **同** 区分(孔子"君子和而不同"):和是 dynamic harmony 中的差异共存,同是 simple agreement。

### 15. 力量结构 (4)

```
力 lì    — force, exerted power
能 néng  — capacity, potential
权 quán  — leverage, configurational authority
位 wèi   — structural position (in hierarchy or network)
```

注:**力**(actualized force)、**能**(potential capacity)、**权**(configurational leverage)三者不同。**位** 在 v0.3 中表 structural position(不是 v1.1 中的 Locus = 是)。

### 16. 进退 (2)

```
进 jìn   — advance, progress
退 tuì   — retreat, withdraw
```

### 17. 集合范围 (3)

```
全 quán  — all, complete
独 dú    — alone, independent
共 gòng  — common, shared
```

### 18. Epistemic Structural (2)

```
真 zhēn  — true, genuine
伪 wěi   — false, fabricated
```

注:这两个不是道德判断,是 epistemic structural——assertion 是否对应 actual happening。

---

### 总数

| 类 | 字数 | 累计 |
|----|------|------|
| 1. 结构原语 | 8 | 8 |
| 2. 算子虚词 | 14 | 22 |
| 3. 时序 | 10 | 32 |
| 4. 存在动态 | 10 | 42 |
| 5. 方向变化 | 12 | 54 |
| 6. 强度修饰 | 8 | 62 |
| 7. 距离结构 | 8 | 70 |
| 8. 反思认知 | 8 | 78 |
| 9. 数量关系 | 8 | 86 |
| 10. 动力学 | 10 | 96 |
| 11. 体用本末 | 4 | 100 |
| 12. 心性情志 | 5 | 105 |
| 13. 隐显 | 2 | 107 |
| 14. 协同响应 | 6 | 113 |
| 15. 力量结构 | 4 | 117 |
| 16. 进退 | 2 | 119 |
| 17. 集合范围 | 3 | 122 |
| 18. Epistemic | 2 | 124 |

**总数: 124 字**

### 明确排除

- **道德德目**(仁义礼智信、善恶):emergent virtues,不是 primitives
- **角色名**(君臣父子、师友徒朋):emergent role patterns,用 IDs
- **价值判断**(宜忌当善):预设外部价值,本体中立
- **具体动词**(送借买卖说教):emergent happening patterns
- **时间 units**(年月日时):reference IDs
- **量度 units**(米斤元):reference IDs
- **数字本身**:cardinality references
- **Cosmologically loaded**(道、气、天、神、命):虽深但工程 risky

---

## IV. 没有 primitive types — 一切是 relation

传统计算有 primitive types: int、float、string、bool、datetime、currency。

间没有 primitive types。**一切是 relation between happenings**。

### 数字是 cardinality relation

`5 个苹果` 不是 5 (number) 加 苹果 (object) 的属性。**5 是这一组苹果之间的某种 grouping relation 的 emergent reference**。

古文表达:
```
五苹果之合
或: 苹果 apple_1 apple_2 apple_3 apple_4 apple_5 计五
```

5 不被 declared,5 是这个 grouping 的 emergent property——可以被 query 时 derive。

### Unit 是 reference event

"5 米"不是 5 quantity + 米 unit。**米是一个 reference event**(国际计量大会 1983 年定义的光速距离),5 计 它的 instances。

```
跨五米    ; 跨越 5 个"米"reference events
量百元    ; 量 100 个"元"reference instances
跨三十日  ; 跨越 30 个"日"reference events
```

**米、元、日 都是 IDs**——和 alice、bob 同样的本体地位。它们 happen to refer 到某种 standardized reference happening,本体上不特殊。

### Time 是 events 之间的 relation

`alice 30 岁` 不是 alice 的属性。是 alice 出生 happening 与今之间的 跨 relation。

古文:
```
alice 自其生至今,跨三十年。
```

返回某个 quantity-relation——calendar 表达为 30 年,本体是两个 events 的 relation。

### Boolean 是 relation query

`X is true` 不是值,是 query result——一次 query happening。

```
问 X 之 履否?     ; X 是否完成?
问 alice bob 之感强否?
```

返回是 happening——一次 query 间-event,结果是新的 是 (the answer)。

### Statistics 是 emergent relations

`average score is 85` 不是 operation result,是 relation。

```
event_1 至 event_n,各之 score,其平 X
```

X 是 emergent of all events——不被 stored,被 derived on query。

### "类型"是 emergent

如果一组 是 在 happenings 中表现出 similar pattern,它们 emerge 出一个类。

```
alice bob carol 之 manifest 同 pattern_001
```

但**类不是 declared schema**——它是 detected pattern。明天可能新成员加入或退出。**类型是 fluid emergent group,不是 fixed structural definition**。

### 工程含义

- **没有 ORM**: 不需要把"对象"映射到"表"。直接 query happenings
- **没有 Schema migration**: 类型 emergent,不预设 schema
- **没有 Type errors**: relation 不匹配会触发 happening,不会"crash"
- **没有 Static analysis** (in traditional sense): 但有 pattern detection——系统从 history 学习什么 patterns 是常见 / 异常

这看似 chaotic,实际更稳定——系统不假装它知道未来 schema 长什么样。

---

## V. Homoiconicity — 代码即数据即日志即文档

间的语言形式有一个深刻 property: **代码、数据、日志、文档 是同一种东西**。

这不是 Lisp-style 的 syntactic 选择,是间本体的必然——

如果一切是 happening,那:
- 代码 = 描述 will-happen 的 happenings 序列
- 数据 = 已经 happen 或正在 happen 的 happenings 记录
- 日志 = 系统自己 happen 过的 happenings 流
- 文档 = 用间语言对系统的描述

**它们本体上是同一种东西的不同时间段或抽象层次**。一段间表达式可以同时被读为这四者中任何一种。

### 一段间表达,四种用法

```
今 alice 与 bob 之间生感, msg_001 之内 "..."。
```

**作为代码**: 系统执行这个会引发对应 happening——alice 与 bob 之间感之生,msg_001 创建。

**作为数据**: 这是一条 happening record——可以被 query、被 fold、被 aggregate。

**作为日志**: 这就是该 happening 的 log entry——不需要单独的 logging format。

**作为文档**: 它读起来 self-documenting——"今天 alice 与 bob 之间发生了一次感的生起,关于 msg_001..."。

### 工程含义

- **没有 schema vs implementation 二元**: 你直接写 间-events,系统从中归纳 schema
- **没有 source code vs runtime data 二元**: 你写的代码和系统记录的数据是同一格式。系统可以读自己运行过的历史,把它当代码 re-evaluate——这是 cultivation 的工程基础
- **没有 code vs documentation 二元**: 写代码 = 写文档。读代码 = 读文档。文档过时问题被消除
- **没有 log vs replay 二元**: 记录的 happening 流可以直接被 replay
- **没有 API vs implementation 二元**: 两个间系统通信时交换的是 间-events——同样的核心字 + ID。API 不需要被单独设计,它就是间语言本身

---

## VI. 五种 Mode 作为观察姿态

如果只有间是原语,五个概念(感、是、际、约、修)是什么?

**它们不是 primitives,是观察间的姿态**。

每次间-happening 同时具有这五种 mode 的可能元素:

- 当间表现得稳定 → 我们看见 **是**(在某时间窗口内不变的 happening 流)
- 当间表现得多向 → 我们看见 **际**(涉及多个是的结构)
- 当间表现得有节律 → 我们看见 **感**(强度、势、节律 pattern)
- 当间跨时间锁定 → 我们看见 **约**(承诺、约束、未来锁定)
- 当间自身改变 → 我们看见 **修**(cultivation,自身演化)

**这五个 mode 同时呈现**——一次 happening 不是只属于一个 mode,在不同 dimensions 上以不同 mode 显现。

工程实现:**view functions over the same event log**。

```
是 之 view  : Stream<JianEvent> × ID → IdentityHistory
际 之 view  : Stream<JianEvent> × Set<ID> → RelationHistory  
感 之 view  : Stream<JianEvent> × Set<ID> × Dim → ResonancePattern
约 之 view  : Stream<JianEvent> → ActiveCommitments
修 之 view  : Stream<JianEvent> × ID → CultivationTrajectory
```

同一个 event log 上五种独立 view function 运作,互不冲突,互不缺一。

---

## VII. 三层架构 — 涉、际、动力学

间-events 的描述 actually 工作在三个层次:

### Layer 0: 间 (单一 primitive)

唯一本体单位。所有其他都是它的 view 或 fold。

### Layer 1: 涉 (within a happening)

一次 happening 涉及哪些是,在哪些维度上,以何种 mode。这是单个 happening 的内部结构。

涉的 arity 任意——可以 1-ary(自身)、2-ary(双方)、3-ary(三方共在)、N-ary。

```
间涉 alice                    ; 1-ary, 自反
间涉 alice bob                ; 2-ary
间涉 alice bob gift_001       ; 3-ary
间涉 community_members 计百   ; N-ary
```

### Layer 2: 际 (relations between 是 across happenings)

是与是之间持续的关系性结构。这是 happenings 之间的 patterns。

```
alice 与 bob 之际渐亲
team_X 之内际紧密
```

### Layer 3: 动力学 (patterns of relations over time)

attractors、trajectories、phase transitions、bifurcations——关系网络的动力学结构。

```
alice 之轨,自拖延之势,趋勤之势,跨三月,渐成。
team 之理:冲突-和解-冲突,循环,周二周。
今见机:若 facilitator 当下应,则势趋深和;否则势趋表面化。
```

**Layer 3 是 v0.3 的关键新增**。它让间能描述:
- Cultivation 的方向(朝某 attractor)
- Social pattern 的识别
- Strategic intervention(在 critical point 行动)
- Health monitoring(系统是否朝某 attractor 漂移)

没有 Layer 3,系统只能记录 events,不能识别 patterns。

---

## VIII. SST 如何被含括

之前的 SST(Spirit-Space-Token)三原语在间中如何呈现?

- **Spirit** = 一种是,具有 active manifest 的是。但是比 Spirit 更基本——人、文档、社群都是是,不一定是 active spirit
- **Space** = 一组是通过际形成的可识别区域。它是际拓扑模式的命名,不是独立 primitive
- **Token** = 间之离散记录。当一次 间-happening 被 fold 为可流转的 reference 时,它是 token。Token 是间的 trace,不是它的本质

**SST 的所有表达都可以在间中被表达**:
- "Spirit A 把 Token T 发给 Spirit B" → 一次 间-happening,涉 A T B,其感改变(T-A 衰、T-B 盛),其修 A 舍 T,B 受 T
- "Token 流过 Space" → 间-events 在某际拓扑中的连续展开
- "Spirit 互相协作" → 多个是在多次 间-events 中的际持续

**间不只能含括 SST,且更精确**——因为它不预设三个分立的本体类别,允许更细微的 happening 描述。

---

## IX. Worked Examples

每个 example 用古文 primary,S-expression 在 ambiguous 处或长 nested expression 处使用 fallback 显示 isomorphism。

### 9.1 简单消息

**古文**:
```
今 alice 与 bob 间生感微, msg_001 之内 "..."。
时 2026-05-01T14:30。
```

**S-expression** (等价):
```
(間 涉 [alice bob msg_001]
    感 微 生 于 (alice bob)
    内 msg_001 "..."
    时 2026-05-01T14:30)
```

### 9.2 赠予

**古文**:
```
今 alice 以 gift_001 予 bob。
其感: alice 与 gift_001 渐疏, bob 与 gift_001 渐亲, alice 与 bob 益亲。
其修: alice 舍 gift_001 之系, bob 受之, gift_001 转所属, 自 alice 至 bob。
省 alice 曰: 祝吾友新婚。
```

**注**: 没有"赠"字——"赠"是 emergent pattern,系统从感衰盛 + 修舍受 识别这是 gift event。

### 9.3 立约 — 博士导师与学生

**古文**:
```
立约。
其涉: advisor 与 student。
其期: 跨五年。
其体: 师徒之际也。
其用: dissertation_research 之修也。

若 dissertation_complete 成,
则: 际节转, student 化 doctor, 得 doctor_status。
否: 际衰, student 失 doctor_status, 归于 candidate。

证以 committee_1 committee_2。
advisor 意曰: 吾期此生五年矣。
省曰: 知 student 之能, 信其必成。
```

**注**: 体/用 一对让 protocol(师徒之际)与 instance(dissertation 研究)清晰分离。这是 v0.3 的关键深度。

### 9.4 反思与修

**古文**:
```
今间涉 alice。
因前三日间涉 alice 与 bob 之冲。

省曰:
  明: 吾未能感 bob 之心, 吾过于己见。
  虑: 当时若微听则不至此。今当何以应之?

悟曰: 感在心, 不在言也。

修:
  其性之急当缓。
  其心之应当顺 bob 之情。

志曰: 明日当致歉。
```

**注**: 心、性、情、志四字共同覆盖 inner subject space。明、虑、悟、省四字覆盖 cognitive modes。这是王阳明日记的 voice,但描述的是数字系统中的 cultivation。

### 9.5 多方共识

**古文**:
```
今间涉 alice bob carol。

其际:
  初: alice 与 bob 合, alice 与 carol 合, bob 与 carol 异。
  经思虑与应答。
  终: alice bob carol 同。

其序: alice 唱, bob 应, carol 异, 共思, 终和。

生是 decision_001。
其出 alice bob carol 之共。
其立在和。
```

**注**: 唱/应、和/同 这些字让 group dynamics 的内部结构精确。和≠同——和是 dynamic harmony 中的差异共存。

### 9.6 数量与时间

**古文**:
```
alice 自其生至今, 跨三十年。
```

或纯关系性(完全不用 calendar):
```
alice 自 event_1996_05_01 至 event_2026_05_01, 跨 ...
```

返回某个 quantity-relation,可以被显示为"30 年"(用 calendar reference)或更原始的 relation。

### 9.7 系统识别 attractor 漂移 (用上 Layer 3)

**古文**:
```
今间涉 system_self。

省自身:
  理见: 自身之 manifest_homogenization 之势日增,
       其微节跨三月, 恐至度则节至矣。
  虑曰: 不立 counter-attractor, 必化于单。
       其机迫在三周。

悟曰: 病不在数, 在维之偏也。

故修自身:
  立 counter-attractor diversification_dynamic。
  体不易, 用增维。

证以 auditor_1 auditor_2 auditor_3。
意守多元。
时今。
```

**注**: 这段使用 Layer 3 全套——理(invariant pattern)、势(attractor force)、微节、度、机(critical window)、变(qualitative change)、体/用(structural unchanged but manifestation expanded)。**这种 attractor-aware 的系统反思,只有用 v0.3 全集才能写**。

### 9.8 复杂 nested condition (S-expression fallback)

某些 nested logic 在古文里容易歧义,用 S-expression:

```
(若 (与 (履 X) (履 Y))
    (或 (是 Z 成) (是 W 成))
   则 (生 是 result_1)
   否 (若 (失 X)
         则 (修 alice 反思)
         否 (修 alice 待)))
```

如果用古文写:
```
若 X 履与 Y 履, 而 Z 成或 W 成, 则生是 result_1。
否, 若 X 失, 则修 alice 反思; 否则修 alice 待。
```

第二句仍然能读,但 nested condition 的 grouping 不如 S-expression 明确。**对人类阅读古文版本足够,对 machine parsing 用 S-expression 版本**。

### 9.9 Federation — 间-event 跨网络

**古文**:
```
今间涉 alice@network_A 与 bob@network_B。
其感际立。
跨网络: network_A network_B。
```

`@network_X` 作为 ID 的 namespace 标记。跨网络的 happening 用同样语言表达。

### 9.10 Query 自身是 happening

**古文**:
```
问 alice 之 间, 自前七日至今。
其际之平与散, 其修之轨与进退,
其约之履与失, 其感之盛衰,
其心之静或动。
取之。
```

"问"也是一次 happening——它涉及 alice 这个被 query 的是,涉及一个 query agent,输出是 间-events list。Query 不是"对系统的外部操作",是系统内部的一次 happening。

---

## X. 工程接口

### 10.1 数据底层

唯一的本体单位:**间-event**。所有数据是 间-events 的 stream。

```
JianEvent {
  id: HappeningID
  涉: Set<是ID>           // 涉及哪些是
  涉态: List<Involvement>  // 在不同 dimensions 上的 involvement
  时: TimeReference        // calendar string 或 event reference
  反思: Optional<ReflectionTrace>
  reference: Set<JianEventID>  // 与其他 happening 的关系
  
  // Layer 3 attachments (optional)
  attractor_ref: Optional<AttractorID>
  trajectory_ref: Optional<TrajectoryID>
  bifurcation: Optional<BifurcationContext>
  phase_transition: Optional<PhaseTransitionRecord>
}

Involvement {
  dim: DimensionID  // 维度
  arity: Int        // 1, 2, 3, N
  participants: Subset<是ID>
  pattern: 增 | 减 | 衰 | 盛 | 生 | 立 | 破 | 转 | ...
  intensity: Optional<emergent quantity>
}

Attractor {
  id: AttractorID
  description: 间-language description
  basin: dynamic
  strength: emergent metric (势之量)
  observed_in: Set<JianEventID>
}

Trajectory {
  id: TrajectoryID
  是: 是ID
  path: List<JianEventID>
  current_attractor: Optional<AttractorID>
  velocity: emergent metric
}
```

注:Attractor 和 Trajectory 自身也是是。它们有 ID、有 history、可被 reference。这与本体一致——所有可被 reference 的存在都是是。

### 10.2 Storage

存储 = append-only log of 间-events。

技术参考:Datomic、EventStore、Kafka log compaction。但间比这些更彻底——所有 query 都是 fold over log,**没有"current state"作为 stored object**。

### 10.3 Query

Query 自身是 happening。系统接收一个 query event,返回 events list。

技术参考:Datomic 的 datalog query、GraphQL subscription。但间的 query 用 same language 作为系统其他部分。

### 10.4 Time

不存储绝对时间。每个 event 有 TimeReference,可以是:
- Calendar string(`2026-05-01T14:30`)作为 ID,refer 到 wall-clock event
- Event reference(`event_001`)直接 refer 到另一个 event
- Relative expression(`(前 event_X 五日)` or "前 event_X 五日")作为派生

时间运算 = relation arithmetic between events,not unit-based。

### 10.5 Identity

ID 系统:
- 默认 cryptographic public key(Ed25519、DID-style)
- Composite IDs for groups: `[alice bob]`
- Domain IDs: `project_001`、`msg_5`
- Calendar IDs: `2026-05-01`

ID 的 spoofing 防御:核心 happenings 必须由 ID 持有者签名。

### 10.6 Evolution

类型 emergent,运行时可观察、可统计、可演化。

修(cultivation)作为 first-class operation——一个是自己改变自己的 manifest 是合法 happening,不是 schema migration。

### 10.7 Prototype Path

**Phase 1**: Clojure-based DSL。用 Clojure macros 实现核心字 keywords。基于 Datomic 或类似 store。Parser 支持古文 primary syntax + S-expression fallback。几周到 1-2 月工作量。

**Phase 2**: 独立 parser + interpreter。古文 syntax 的 well-defined subset + S-expression。1-2 月。

**Phase 3**: 完整 runtime——distributed event log + identity system + reactive evaluation + Layer 3 attractor detection。3-6 月。

**Phase 4**: 形式 specification——把间的 semantics 写成 categorical structure。无固定时间表。

### 10.8 与现有 stack 的接口

- **Persistence**: 任何 append-only store。Datomic / EventStore / Kafka / IPFS
- **Network**: libp2p / 类似 P2P
- **Crypto**: standard Ed25519、Blake3、Merkle DAG
- **Compute**: any runtime。Clojure / Elixir / Rust 都合适

间的 architecture 是 thin layer——大部分技术 building blocks 已存在。新的工作是**把这些 blocks 用间-language 组合,且坚持本体一致性**。

---

## XI. 与传统对话

间不是凭空。它在多个传统的交汇:

- **Lambda calculus / Lisp**: 一切是 function evaluation 的极致。Lisp 的 homoiconicity 是间的工程兄弟
- **Category theory**: 一切是 morphism, objects 是 identity morphism 的退化。Higher category theory / topos theory 可能是间的 mathematical foundation
- **Event sourcing / CQRS**: 应用层的 happening-centric architecture。间把这个推到本体层
- **Erlang / Actor model**: 关系性的运行时。间比 Erlang 更彻底——actor 仍有内部 state,间的是完全是 happening chain
- **Datalog / relational calculus**: 关系即查询
- **易传**: "感而遂通"、"几者动之微"。间的形而上根基
- **王阳明心学**: "心即理"、"知行合一"。间中,反思与行动同源
- **华严宗**: "理事无碍,事事无碍"。间的极致——无独立事物,只有相互含摄的 happenings
- **宋明理学体用论**: 体/用 一对直接进入间的核心字

间是这些 traditions 的 emergent convergence——不同方向的深思考碰到同一本体。

---

## XII. 限度

**1. 一元论无法被证明,只能被选择**

任何一元本体都无法被外部证明。它们是本体姿态。间也一样。它的合理性来自它的 productivity——能让多少深问题被 cleanly 处理——不来自它的 certainty。

**2. 表达能力的待验证**

我们论证了 ~124 字 + ID + 组合 能表达任何 happening,经过 worked examples 验证。但全面 claim 需要 prototype 进一步验证。可能发现某些 happening 类型需要新的 idiom。

**3. 学习成本**

~124 字的学习 + 对这种本体姿态的内化,加上学习古文 syntax 的基本规则——这是 间的"门槛"。比传统 framework 高,但比学一门完整新语言低。学会后,表达力强于现有任何 framework。

**4. 工程成熟度**

间没有现成 stack。所有 building blocks 存在(append log、p2p、crypto)但需要 integration。第一个完整 prototype 可能需要 6 个月,production-grade 实现可能 2-3 年。

**5. 文化误读风险**

间用古文核心字、用宋明理学的 vocabulary——会被误读为"中国项目"或"传统主义项目"。这是误读。**间是本体精确性选择,不是文化身份**。但这个误读会发生,需要持续澄清。

**6. 评判标准的不对称**

间用一套术语,主流工程用另一套。这意味着间的评判很难被现有 benchmarking 系统衡量。"多快"、"多 scalable"、"多容易"——这些 metrics 假设了间不预设的 ontology。这是长期挑战。

**7. 古文 syntax 的 ambiguity**

某些复杂 nested expression 在古文里容易歧义,需要 fallback 到 S-expression。这是 hybrid syntax 不可避免的代价——但比纯 S-expression 失去古文 voice 或纯古文失去精度好。

---

## XIII. 接下来

这份 Note 把间的本体推到一个稳定位置,可以开始 prototype。

**Step 1**: 基于这份 Note 修订 v1.1 → v1.2,把术语统一(commitment → 约,locus/identity → 是,等),把 Layer 3 dynamics 整合,把 homoiconicity 显式化。

**Step 2**: Clojure prototype——选 OpenClaw 内一个限定场景,用间语言实现。让形而上承诺在工程压力下显形。

**Step 3**: 邀请几位信任的 contributors 读 Note,批评 / 增删核心字集 / 暴露未察盲点。

**Step 4**: 第一个 worked production case——可能是 Nomad OS 的某个 sub-feature,可能是 706 内部的某个协作场景。

**Step 5**: 基于 prototype 经验,Foundation Note v0.4。可能有意外发现需要 onto 修订。

---

## 附录 A: 一句话本体

**间是 happening。Happening 是 function evaluation。一次 evaluation 涉及一些是,在某些维度上有相互涉入。一切语言、数字、时间、关系、计算,都是 happenings 之间 relations 的不同呈现。没有 primitive types,没有 entities,没有 absolute time——只有 happenings 和它们的相互涉入。**

中文:**間 即"涉之进行"——既是涉所在,也是涉中所发生,也是这进行自身。一切是间。**

---

## 附录 B: 核心字快查表 (124)

| 类 | 字 | 拼音 | 含义 |
|----|----|----|------|
| 结构 | 間 | jiān | happening |
| | 是 | shì | identity |
| | 际 | jì | relation |
| | 约 | yuē | commitment |
| | 修 | xiū | cultivation |
| | 感 | gǎn | resonance |
| | 化 | huà | transformation |
| | 涉 | shè | involvement |
| 算子 | 之 | zhī | of |
| | 其 | qí | its |
| | 所 | suǒ | that which |
| | 者 | zhě | the one who |
| | 以 | yǐ | by |
| | 于 | yú | at |
| | 然 | rán | such |
| | 而 | ér | and |
| | 因 | yīn | because |
| | 果 | guǒ | result |
| | 故 | gù | therefore |
| | 若 | ruò | if |
| | 则 | zé | then |
| | 否 | fǒu | else |
| 时序 | 前 | qián | before |
| | 后 | hòu | after |
| | 自 | zì | from |
| | 至 | zhì | to |
| | 跨 | kuà | span |
| | 循 | xún | recurring |
| | 始 | shǐ | begin |
| | 终 | zhōng | end |
| | 今 | jīn | now |
| | 昔 | xī | past |
| 存在 | 生 | shēng | emerge |
| | 灭 | miè | vanish |
| | 立 | lì | establish |
| | 破 | pò | dissolve |
| | 成 | chéng | become |
| | 败 | bài | fail |
| | 有 | yǒu | exist |
| | 无 | wú | absent |
| | 在 | zài | present |
| | 存 | cún | persist |
| 变化 | 增 | zēng | increase |
| | 减 | jiǎn | decrease |
| | 益 | yì | benefit |
| | 损 | sǔn | lose |
| | 得 | dé | obtain |
| | 失 | shī | miss |
| | 予 | yǔ | give |
| | 受 | shòu | receive |
| | 舍 | shě | release |
| | 取 | qǔ | take |
| | 转 | zhuǎn | turn |
| | 归 | guī | return |
| 强度 | 盛 | shèng | flourish |
| | 衰 | shuāi | wane |
| | 强 | qiáng | strong |
| | 弱 | ruò | weak |
| | 深 | shēn | deep |
| | 浅 | qiǎn | shallow |
| | 微 | wēi | subtle |
| | 显 | xiǎn | manifest |
| 距离 | 亲 | qīn | close |
| | 疏 | shū | distant |
| | 合 | hé | joined |
| | 分 | fēn | separated |
| | 内 | nèi | inner |
| | 外 | wài | outer |
| | 通 | tōng | flowing |
| | 塞 | sè | blocked |
| 反思 | 思 | sī | think |
| | 虑 | lǜ | deliberate |
| | 知 | zhī | know |
| | 悟 | wù | realize |
| | 省 | xǐng | reflect |
| | 明 | míng | clear |
| | 迷 | mí | confused |
| | 信 | xìn | trust |
| 数量 | 计 | jì | count |
| | 量 | liàng | amount |
| | 序 | xù | order |
| | 比 | bǐ | ratio |
| | 平 | píng | average |
| | 散 | sàn | spread |
| | 多 | duō | many |
| | 少 | shǎo | few |
| 动力 | 势 | shì | attractor |
| | 机 | jī | bifurcation |
| | 轨 | guǐ | trajectory |
| | 理 | lǐ | invariant pattern |
| | 节 | jié | phase transition |
| | 度 | dù | threshold |
| | 常 | cháng | persistent |
| | 变 | biàn | change |
| | 动 | dòng | activity |
| | 静 | jìng | rest |
| 体用 | 体 | tǐ | structure |
| | 用 | yòng | manifestation |
| | 本 | běn | root |
| | 末 | mò | surface |
| 心性 | 心 | xīn | heart-mind |
| | 性 | xìng | nature |
| | 情 | qíng | situation/emotion |
| | 意 | yì | intention |
| | 志 | zhì | will |
| 隐显 | 隐 | yǐn | hidden |
| | 潜 | qián | dormant |
| 协同 | 唱 | chàng | initiate |
| | 应 | yìng | respond |
| | 和 | hé | harmony |
| | 违 | wéi | violate |
| | 同 | tóng | same |
| | 异 | yì | different |
| 力量 | 力 | lì | force |
| | 能 | néng | capacity |
| | 权 | quán | leverage |
| | 位 | wèi | position |
| 进退 | 进 | jìn | advance |
| | 退 | tuì | retreat |
| 集合 | 全 | quán | all |
| | 独 | dú | alone |
| | 共 | gòng | shared |
| epistemic | 真 | zhēn | true |
| | 伪 | wěi | false |

---

## 附录 C: 古文 syntax 速查

### 基本结构

**主谓宾**: `[主语] [谓语] [宾语]`
- "alice 予 gift_001" — alice gives gift_001
- 主语可省略

**修饰**: `[修饰语] 之 [被修饰语]`
- "alice 之 manifest" — alice's manifest
- "团队 之 内际" — the team's inner relations

**条件**: `若 ... 则 ... 否 ...`
- "若 X 履,则 Y 成,否 Z 立"

**因果**: `因 ... 故 ...` 或 `... 因 ... 故 ...`
- "因前三日之冲,故今修"

**时间**: `时 ...` 或 `于 ... 时`
- "时今"
- "于 2026-05-01"

**多 items**: 顿号 inline 或换行 + 缩进
- "alice、bob、carol 共思"
- 长 list 用换行

### 句末助词

- `也` : 断定 ("XX 也" = it is XX)
- `矣` : 完成时态/感叹 ("成矣" = has been accomplished)
- `焉` : there/in it (locative)
- `乎` : 疑问 ("何乎" = what?)

### 引用

- `曰`: speech ("alice 曰: ...")

### 代词

- `其`: third-person possession/reference
- `之`: third-person object pronoun, possession marker

### Disambiguation

当 nested logic 复杂时,使用 S-expression。规则见附录 D。

---

## 附录 D: 古文 ↔ S-expression 转换规则

两种 syntax isomorphic。机械转换规则:

### 古文 → S-expression

| 古文 | S-expression |
|------|--------------|
| `X 之 Y` | `(之 X Y)` 或 `X.Y` |
| `若 X 则 Y 否 Z` | `(若 X 则 Y 否 Z)` |
| `因 X 故 Y` | `(因 X 故 Y)` |
| `X、Y、Z` | `[X Y Z]` |
| `时 T` | `(时 T)` |
| `自 X 至 Y` | `(自 X 至 Y)` |
| `跨 N M` | `(跨 N M)` |
| `X 曰 "..."` | `(曰 X "...")` |
| `[句末] 也` | (assertion marker) |
| `[句末] 矣` | (perfective marker) |

### S-expression → 古文

逆向。Reader function 可以自动 transpile。

### 何时用哪种

- **古文 primary**: 默认。日常 happenings、reflection、protocol、documentation
- **S-expression fallback**: Nested logic 容易歧义、machine parsing 必需、debugging、formal verification

---

*End of Foundation Note v0.3.*

*这份 Note 现在 stable enough 可以开始 prototype。下一步是把 v1.1 Metaphysics 文档同步到 v1.2,然后开始 Clojure prototype。Foundation Note v0.4 会基于 prototype 经验修订。*
