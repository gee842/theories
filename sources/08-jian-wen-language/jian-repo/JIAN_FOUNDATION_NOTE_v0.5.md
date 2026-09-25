# 間: Foundation Note

## On the Single Primitive Ontology

**Version**: 0.5 · *vocabulary completed, three-tier architecture*
**作者**: Ren
**协作起草**: Claude

**v0.5 changelog**: 完成核心字集 + 引入三层 vocabulary architecture。
- 核心字从 125 扩到 ~146,补全了关系现象空间中之前的 gaps
- 新增 Tier 2: **Standard Vocabulary** — 高频 emergent expressions 作为 std lib
- 明确三层 architecture:Tier 1 (core primitives) / Tier 2 (std emergent) / Tier 3 (domain-specific)
- 新增字按 dimension 系统补全:流、中、子、属、聚、渐、极、源、觉、忘、曰、言、默、念、欲、见、观、还、来、往、偏

**v0.4 修正 (二次)**: 数据结构命名彻底古文化——JianEvent → 間,ID → 是,Set/List/Optional → 集/列/或,Stream → 流,Attractor/Trajectory/Bifurcation/PhaseTransition → 势/轨/机/节。三层一致性:ontology + data structure + API。

**v0.4 changelog**: 核心字 composition rules、古文 grammar formalization、Layer 3 工程化、失/误处理、是之边界与终结、真实场景 worked examples。误 加入 core (124 → 125)。

**v0.3 changelog**: 核心字集 124,Layer 3 dynamics,古文 primary syntax,homoiconicity 显式化。

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
IX. **Three-Tier Vocabulary Architecture — Tier 1 / 2 / 3** *(restructured in v0.5)*
X. **古文 Grammar — 可 parse 的子集** *(new in v0.4)*
XI. **Layer 3 工程化 — Attractor 与 Trajectory** *(new in v0.4)*
XII. **失与误 — 失败模式与错误处理** *(new in v0.4)*
XIII. **是之边界与终结** *(new in v0.4)*
XIV. Worked Examples — 古文与 S-expression 对照 (扩充)
XV. 工程接口
XVI. 与传统对话
XVII. 限度
XVIII. 接下来

附录 A: 一句话本体
附录 B: 核心字快查表
附录 C: 古文 syntax 速查
附录 D: 古文 ↔ S-expression 转换规则
附录 E: **Common Idioms — 常见 happening patterns** *(new in v0.4)*

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

1. **核心字 (~125 字)**: 古汉语单字承担本体精度
2. **ID (英文字符串)**: 引用具体的 间(在某 view 下显现为 是、间-history、attractor 等)
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

ID 是 stable reference encoding——它指向某个间(在某 view 下显现为 是 / happening chain / attractor / trajectory),但**不描述其属性**。

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

## III. 核心字集 (Tier 1)

总数 ~146 字。每字承担本体含义,不可被英文还原。这是 **Tier 1 — language kernel**——本体 primitives。

(关于 Tier 2 standard vocabulary 与 Tier 3 domain expressions,见 Section IX。)

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

### 2. 算子虚词 (15)

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
曰 yuē   — say (quote-introducer; X 曰 "..." or X 曰 ...)
```

### 3. 时序 (12)

```
前 qián  — before
后 hòu   — after
自 zì    — from
至 zhì   — to
跨 kuà   — span (interval)
循 xún   — recurring
始 shǐ   — beginning
终 zhōng — end
今 jīn   — now (current 间 reference)
昔 xī    — past (general)
来 lái   — coming (future direction, dynamic)
往 wǎng  — going (past direction, dynamic)
```

注:**没有 time units**(年、月、日、时、分、秒)。这些是 reference IDs。

注:**前/后** vs **来/往** 的区分:前/后 是 static ordering(in temporal sequence);来/往 是 dynamic direction (coming-toward vs receding-from current 间)。

### 4. 存在动态 (11)

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
源 yuán  — source, origin (ontological grounding)
```

注:**有/无** 是 relational existence。**在** 是 presence in a context。**存** 是 persistence over time。**源** 不同于 **始**:始是 temporal beginning,源是 ontological source / root cause(水之源)。

### 5. 方向变化 (13)

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
还 huán  — return-what-was-owed (distinct from 归)
```

注:**归 vs 还**:归是 return-to-origin(归乡,return home);还是 return-what-was-borrowed/owed(还债,return debt)。涉及 commitment fulfillment 时用 还。

### 6. 强度修饰 (9)

```
盛 shèng — flourishing, peak
衰 shuāi — declining, waning
强 qiáng — strong
弱 ruò   — weak
深 shēn  — deep
浅 qiǎn  — shallow
微 wēi   — subtle, minute
显 xiǎn  — manifest, evident
极 jí    — extreme, utmost (boundary state)
```

注:**极** 是 boundary/limit state——当一个 dimension reach extreme,通常 triggers 反向 dynamic("物极必反")。重要的 dynamic threshold marker。

### 7. 距离结构 (11)

```
亲 qīn   — close, intimate
疏 shū   — distant, estranged
合 hé    — joined, united
分 fēn   — separated
内 nèi   — inner
外 wài   — outer
中 zhōng — center, within, middle
通 tōng  — penetrating, flowing through
塞 sè    — blocked, obstructed
子 zǐ    — sub, derived, part-of
属 shǔ   — belonging to, subordinate
```

注:**中** vs **内**:内是 inside (vs outside),中是 center / middle / balanced point。"中庸"、"中道"、"在...之中"。这是 dynamic equilibrium 的关键概念。

注:**子** vs **内**:内是 spatial inside,子是 hierarchical sub-relation。"子集" = sub-set,"子项" = sub-item。子表达 part-of / derived-from。

注:**属** 是 belonging-to-a-class——"alice 属 humans"、"task_001 属 project_X"。Hierarchical membership。

### 8. 反思认知 (13)

```
思 sī    — thinking (active reasoning)
虑 lǜ    — deliberating, considering
知 zhī   — knowing
觉 jué   — awakening, becoming aware
悟 wù    — realize, illuminate
省 xǐng  — reflect, examine self
见 jiàn  — see, perceive, encounter
观 guān  — observe, contemplate (sustained)
念 niàn  — thought-instance, mindful attention
明 míng  — clear, illuminated
迷 mí    — confused, lost
忘 wàng  — forget
信 xìn   — trust, believe
```

注:这里 cognitive layer 的细分在中文里非常 rich:
- **思** = active reasoning
- **虑** = anxious deliberation, planning
- **知** = knowing (state)
- **觉** = becoming aware, awakening (onset of awareness)
- **悟** = realizing deep insight (sudden illumination)
- **省** = reflecting on self
- **见** = seeing / encountering (perceptual basic)
- **观** = sustained observation / contemplation
- **念** = a single thought-instance / mindful attention to a particular thing
- **忘** = forget (cognitive primitive — independent of 知/不知)

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

### 10. 动力学 / Dynamics (13)

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
流 liú   — flow, stream (active happening flow)
聚 jù    — gather, converge (dual of 散)
渐 jiàn  — gradual, incremental (dual of 变 in 渐变 vs 突变)
```

**这是 v0.3 的关键 layer**。这一层描述的不是单个 happening,是 patterns of happenings over time——attractors 和 dynamics。

- **势** = attractor: 系统中某种趋向的能量,使 trajectory 倾向某 region
- **机** = bifurcation point: 临界状态,微小扰动决定 trajectory
- **轨** = trajectory: 实际走过的路径
- **理** = invariant pattern: dynamics 遵循的内在规律
- **节** = phase transition: 系统组织方式的根本改变
- **度** = threshold: phase transition 的临界值
- **常/变** = stability vs change
- **动/静** = activity vs rest(《周易》"一动一静,互为其根")
- **流** = active flow (resources、信息、energy 之 flow,与 通/塞 不同:通/塞 是 state,流是 active happening)
- **聚/散** = converging vs dispersing (聚 在此 layer 加入,与 distance-structure 中的 散 配对)
- **渐/变** = gradual vs sudden change(渐变与突变是 dynamic 的根本对立)

### 11. 体用本末 (4)

```
体 tǐ    — body, structural ground
用 yòng  — function, manifestation
本 běn   — root, fundamental
末 mò    — surface, derivative
```

宋明理学最核心的对——**体是 invariant structure(对应 attractor),用是 dynamic manifestation(对应 trajectory)**。这一对让 protocol 与 instance、character 与 behavior、structure 与 process 有了精确的本体表达。

### 12. 心性情志 (6)

```
心 xīn   — heart-mind (cognition + emotion + will, indivisible)
性 xìng  — nature, essential character
情 qíng  — emotion, situation, circumstance
意 yì    — intention, mental tendency
志 zhì   — will, aspiration
欲 yù    — desire, want, motivation
```

中文心性论两千年沉淀的精确 vocabulary——描述 是 内部的 inner subject space。**这六字一起,有则全有,无则全无**——它们相互定义,共同覆盖 inner subject 的关键 dimensions。

注:**欲** 是 desire/want——这是动机系统的基础。"欲" 不同于 "意"(意是 directional intention,欲是 underlying motivational pull)。"欲" 不同于 "志"(志是 long-term aspiration,欲是 immediate want)。修身的核心问题之一是处理 desires("从心所欲不逾矩")。

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

### 17. 集合范围 (4)

```
全 quán  — all, complete
独 dú    — alone, independent
共 gòng  — common, shared
偏 piān  — biased, partial (dual of 全 / 中)
```

注:**偏** 是 systemic bias / partiality——系统是否 biased toward some attractor,或 sampling 是否 偏 某 dimension。健康的 system 通常 寻求 中(balanced)而非 偏。

### 18. Epistemic Structural (3)

```
真 zhēn  — true, genuine
伪 wěi   — false, fabricated
误 wù    — error, mistake (added v0.4)
```

注:这三个不是道德判断,是 epistemic structural——assertion 是否对应 actual happening。**误** 是 actually-happened 与 should-have-happened 的 mismatch。

### 19. 言说 (2 — new in v0.5)

```
言 yán   — words, speech (the linguistic/articulated)
默 mò    — silence, the unspoken
```

注:言/默 是关系性 fundamental dimension。所有 communication 现象——message、speech act、commitment expression——都涉及 言。但同等重要的是 默——意义 sometimes lies in what's not said。"默契"是 deep agreement without explicit words。

(算子 **曰** 在 Section 2 — 它是 speech 的 syntactic 引入器,而 言/默 是 semantic content distinction。)

---

### 总数

| 类 | 字数 | 累计 |
|----|------|------|
| 1. 结构原语 | 8 | 8 |
| 2. 算子虚词 | 15 | 23 |
| 3. 时序 | 12 | 35 |
| 4. 存在动态 | 11 | 46 |
| 5. 方向变化 | 13 | 59 |
| 6. 强度修饰 | 9 | 68 |
| 7. 距离结构 | 11 | 79 |
| 8. 反思认知 | 13 | 92 |
| 9. 数量关系 | 8 | 100 |
| 10. 动力学 | 13 | 113 |
| 11. 体用本末 | 4 | 117 |
| 12. 心性情志 | 6 | 123 |
| 13. 隐显 | 2 | 125 |
| 14. 协同响应 | 6 | 131 |
| 15. 力量结构 | 4 | 135 |
| 16. 进退 | 2 | 137 |
| 17. 集合范围 | 4 | 141 |
| 18. Epistemic | 3 | 144 |
| 19. 言说 | 2 | 146 |

**总数: 146 字** (v0.5: +21 字: 流、中、子、属、聚、渐、极、源、觉、忘、曰、言、默、念、欲、见、观、还、来、往、偏)

### 明确排除 from Tier 1 (但 some 可作为 Tier 2 emergent)

**完全排除**(本体不适合):
- **道德德目**(仁义礼智信、善恶):emergent virtues,不是 primitives
- **角色名**(君臣父子、师友徒朋):emergent role patterns,用 IDs
- **价值判断**(宜忌当善):预设外部价值,本体中立
- **时间 units**(年月日时):reference IDs (与 IDs 同等地位)
- **量度 units**(米斤元):reference IDs
- **数字本身**:cardinality references
- **Cosmologically heavy**(天、神、命、鬼):工程 risky

**作为 Tier 2 emergent OK** (高频但可 reduce 到 core):
- **具体动词**(送借买卖说教):每个是 emergent happening pattern
- **气** (qì):distributed energy/tendency — 可作为 Tier 2 idiom 用 (e.g., "气盛"、"气衰"),但不进 Tier 1 因为承载太多 traditional 含义
- **密 / 稀**:可由 计 + 强度词 derive (密 = 计多 + 近, 稀 = 计少 + 远)
- **复**:可 derive 自 归 + 立 (return-and-establish)
- **病**:可 derive 自 失 之 常 (loss of normal pattern)
- **学** / **教**:可 derive 自 修 之 应 / 修 之 唱
- **谢**:可 derive 自 心 应 益 (heart responding to benefit received)
- **含**:可 derive 自 内 + 有 (inner + has)
- 其他常用动词均可作为 Tier 2 idiom

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

返回是 happening——一次 query 间,结果是新的 是 (the answer)。

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

- **没有 schema vs implementation 二元**: 你直接写 间,系统从中归纳 schema
- **没有 source code vs runtime data 二元**: 你写的代码和系统记录的数据是同一格式。系统可以读自己运行过的历史,把它当代码 re-evaluate——这是 cultivation 的工程基础
- **没有 code vs documentation 二元**: 写代码 = 写文档。读代码 = 读文档。文档过时问题被消除
- **没有 log vs replay 二元**: 记录的 happening 流可以直接被 replay
- **没有 API vs implementation 二元**: 两个间系统通信时交换的是 间——同样的核心字 + ID。API 不需要被单独设计,它就是间语言本身

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

工程实现:**view functions over the same 间 log**。

```
// View functions: 输入是间集, 输出是间集 (一切是间)
是_view : 流<間> × 是 → 列<間>           // identity history
际_view : 流<間> × 集<是> → 列<間>       // relation history  
感_view : 流<間> × 集<是> × 是 → 列<間>  // resonance pattern (last 是 is dimension)
约_view : 流<間> → 列<間>                // active commitments
修_view : 流<間> × 是 → 列<間>           // cultivation trajectory
```

注: comments 是英文 gloss for readability — `流<間>` reads as "stream of 间", `集<是>` reads as "set of 是", etc.

同一个 间 log 上五种独立 view function 运作,互不冲突,互不缺一。每个 view 输入是间, 输出是间——保持一切是间的本体一致性。

---

## VII. 三层架构 — 涉、际、动力学

间 的描述 actually 工作在三个层次:

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
- "Token 流过 Space" → 间 在某际拓扑中的连续展开
- "Spirit 互相协作" → 多个是在多次 间 中的际持续

**间不只能含括 SST,且更精确**——因为它不预设三个分立的本体类别,允许更细微的 happening 描述。

---

## IX. Three-Tier Vocabulary Architecture

间 的 vocabulary 分三层。这是 v0.5 的明确架构(类似编程语言 kernel + std lib + user code)。

### 9.1 三层架构

**Tier 1 — Core Characters (~146)**: language kernel
- 本体不可还原的 primitives
- 每个字含义无法由其他字 derive 而不失精度
- 工程上是 system 的 keyword 集合
- Section III 列出全部

**Tier 2 — Standard Vocabulary (Std)**: standard library
- 高频使用的 emergent expressions
- 可由 Tier 1 字 derive,但 derive 太 awkward / verbose
- 作为"标准库"提供——一旦学会,日常使用极频繁
- 类比: C 标准库的 printf——它不是 keyword,但每个 C 程序员都知道

**Tier 3 — Domain Expressions**: user / domain code
- 特定领域的复合表达
- Each domain / community 自由 develop
- 不需要 standardize across communities

这三层的关系 mirror 编程语言:
- Tier 1 = keywords (`if`, `while`, `lambda`)
- Tier 2 = stdlib (`println`, `map`, `filter`)
- Tier 3 = domain libraries (Django、React、numpy)

### 9.2 Tier 1 → Tier 2 的 Composition

Tier 1 字组合产生 Tier 2 expressions。三种组合方式:

**Direct Composition** (两字直接连用):

```
反思 = 反 + 思     (return-and-think → reflect)
理见 = 理 + 见     (pattern-see → pattern recognition)
势增 = 势 + 增     (attractor-strengthen)
心知 = 心 + 知     (heart-knows → intuitive knowing)
```

规则:**前字修饰或限定后字**。前字常作 adverb / modifier,后字作 head verb / noun。

**Particle Composition** (通过虚词组合):

```
alice 之 心          ; alice's heart-mind
心 之 应 顺          ; the heart's responding-with-accord
以 微 见             ; by means of subtle perception
于 今 立 约          ; at-now establishing pact
因 衝 故 修          ; because-of-conflict therefore cultivate
若 失 则 复 立       ; if lost, then re-establish
```

虚词承担 grouping 与 relation 功能。

**Pattern + ID** (idiom + reference):

```
舍受 + ID            ; transfer-of-X (赠/借/卖都是这个 + 不同 context)
立约 + parties       ; make-commitment between parties
节转 + 状           ; phase-transition + state
```

### 9.3 Tier 2 标准库 — 常用 emergent expressions

下面是建议的 Tier 2 std lib。这是 v0.5 的初步建议,实际 std lib 会基于 prototype 经验演化。

**A. 通信 (Communication)**

```
言   = primitive (Tier 1, 言说类)
默   = primitive (Tier 1)
告   = 言 + 与 + ID    →  "tell X" (主动告知)
问   = primitive       →  query happening (already covered)
答   = 应 + 言         →  respond-with-words
听   = 受 + 言         →  receive-words (listening)
默契 = 默 + 合         →  silent-agreement (deep alignment without words)
```

**B. 关系动作 (Relational Actions)**

```
助   = 益 + ID (recipient)         →  help (benefit toward target)
教   = 修 + 唱                     →  teach (initiate cultivation pattern)
学   = 修 + 应                     →  learn (respond to teaching with cultivation)
习   = 修 + 循                     →  practice (recurring cultivation)
信   = primitive (信 in Tier 1)    →  trust (relational)
疑   = 信 + 衰                     →  doubt (waning trust)
```

**C. 状态变化 (State Change Idioms)**

```
复   = 归 + 立                  →  recover/restore (return-and-establish)
谢   = 心 + 应 + 益             →  thank/apologize (heart responding to benefit/harm)
含   = 内 + 有                  →  contain (inner-having)
病   = 失 + 常                  →  pathology (loss of normal pattern)
癒   = 复 + 常                  →  heal (recovery to normal pattern)
```

**D. 动力学习语 (Dynamics Idioms)**

```
趋   = 动 + 向 (from "至")     →  tend toward
渐变 = 渐 + 变                  →  gradual change
突变 = 节 + 变                  →  sudden / phase change
极反 = 极 + 反                  →  reach extreme then reverse (from 物极必反)
气盛 = 气 (Tier 2 idiom) + 盛   →  high collective energy
气衰 = 气 + 衰                  →  low collective energy
```

注:**气** 在 Tier 2 作为 idiom 使用是 OK 的——它表达 distributed/collective tendency,可由 "聚之 势 之 量" 长形 derive。Tier 2 给 idiomatic shortcut。

**E. Quantity / Distribution Idioms**

```
密   = 计 + 多 + 近   →  dense
稀   = 计 + 少 + 远   →  sparse  
均   = 散 + 平        →  evenly distributed
差   = 比 + 分        →  difference (in comparison)
```

**F. 时序习语**

```
即   = 至 + 今        →  immediately / namely
俄   = 微 + 跨        →  briefly / a moment
久   = 跨 + 长 (from "深")  →  long-lasting
渐   = primitive (Tier 1)
忽   = 节 + 来        →  suddenly arriving
```

### 9.4 Tier 3 — Domain Expressions

每个 domain (OpenClaw、Nomad OS、706 community) 可以发展自己的 expressions。例如:

OpenClaw 可能有:
```
唤起 agent X    ; awaken / activate agent
agent 之 任    ; agent's responsibility / task
```

Nomad OS:
```
通汇            ; cross-border transfer (通 + 汇货)
轻钱            ; micro-transaction (轻 + 钱)
```

706 community:
```
共修            ; collective cultivation (共 + 修)
慎论            ; careful deliberation (慎 + 言)
```

这些 Tier 3 expressions 在 community 内 standardize,不需要全局 stdlib。

### 9.5 Composition Soundness Rules

(原 v0.4 内容,保留)

不是所有组合都有效。三条 soundness rules:

**Rule 1: Type Compatibility**

某些字只能与特定 ontological type 的后续字组合。

- 时序字(前、后、自、至)必须接 time-like 表达
- 反思字(思、虑、知、悟)必须接 cognitive content
- 强度字(盛、衰、强、弱)必须修饰 happening 或 quantity

**Rule 2: Valence Preservation**

某些字有 directional valence,组合不能 violate:
- 益/损 是 valence opposite,组合 "益损" = "gain-and-loss" 作为 pair concept
- 进/退、聚/散、动/静 同样

**Rule 3: Layer Consistency**

跨层组合需要明确:
- Layer 1 字(感、是、际)+ Layer 3 字(势、机)需要明确表达哪一层
- "感之势" = 一次感的 attractor tendency = OK, layer 1+3 explicit
- "感势" = ambiguous, prefer "感之势"

### 9.6 实践指南

写间表达时 priority:

1. **Tier 1 first** — 尽量用核心字直接表达
2. **Tier 2 standard idioms** — 当 Tier 1 awkward,用标准 idiom
3. **Tier 3 domain expressions** — 在 domain 内可使用,explicitly mark domain
4. **Domain ID 用英文/拼音** — 具体 entity、concept、property 用 ID
5. **Ambiguous nesting 用 S-expression** — 当古文 grouping 不清楚时

System 内部 representation 总是 reduce 到 Tier 1 forms。Tier 2 / 3 是 surface convenience。

---

## X. 古文 Grammar — 可 parse 的子集

为了 prototype, 古文 syntax 必须有**well-defined, parsable subset**。这不是约束所有古文,只是定义系统能可靠 parse 的一部分。

### 10.1 Lexical Tokens

四种 token type:

1. **核心字** (Core Char): 146 字白名单,each is a single Chinese character
2. **ID** (Identifier): 拉丁字母、数字、_、@、-,with optional namespace `name@network`
3. **String Literal**: `"..."` (double-quoted)
4. **Punctuation**: `。 , 、 : ; "..." ( ) [ ]`

注:中文标点(。、)和现代标点(. , :)都接受;parser 内部统一。

### 10.2 BNF Grammar (subset)

```
program     ::= statement+
statement   ::= [time-clause] expression terminator

terminator  ::= "。" | "也" "。" | "矣" "。" | newline

time-clause ::= "时" time-ref | "于" time-ref "时"
time-ref    ::= ID | "今" | relative-time
relative-time ::= ("前" | "后") ID time-quantity
                | "自" ID "至" ID
                | "跨" quantity ID

expression  ::= involvement | conditional | reflection | invocation | composition

involvement ::= "間" "涉" id-list [property-list]
              | id "予" id "于" id   ; alice gives gift to bob
              | id "受" id "自" id   ; bob receives gift from alice
              | id-list verb-phrase

id-list     ::= id ("、" id)* | id (id)*  ; both comma-separated and space-separated allowed
                                          ; for ambiguous cases, use S-expression

conditional ::= "若" expression "则" expression ["否" expression]
              | expression "因" expression "故" expression

reflection  ::= "省" id "曰" string-or-expr+
              | "悟" "曰" string-or-expr
              | "意" id "曰" string-or-expr

invocation  ::= "问" id "之" property [time-clause]
              | "立" "约" property-list

composition ::= core-char ("之" | "其")? expression
              | quantity quantity-relation id  ; 跨五年, 量百元

property    ::= core-char id?
              | "之" core-char value
              
property-list ::= property+ | indented-block
indented-block ::= newline (indent property newline)+

quantity    ::= ID  ; numbers are IDs; e.g., 5, 100, 30
quantity-relation ::= "跨" | "量" | "计" | "序" | "比"

verb-phrase ::= core-char [adverb] [object]
              ; e.g., "渐疏", "舍 gift_001", "立 约"
```

### 10.3 Disambiguation Rules

When 古文 grammar 是 ambiguous, parser uses these rules in order:

1. **Greedy matching for time-clause**: time-clause 必须在 statement 开头
2. **Right-associative** for chained 之: `A 之 B 之 C` = `A 之 (B 之 C)`
3. **Punctuation breaks**: `。` always ends a statement, `,` is soft break
4. **Indent-based grouping**: 缩进表示 sub-expression 属于上一层
5. **Fall back to S-expression**: 如果以上都不能 disambiguate,系统报错并提示用户用 S-expression

### 10.4 Concrete Parsing Example

输入:
```
今 alice 与 bob 间生感微, msg_001 之内 "..."。
```

Parse tree:
```
Statement
├── TimeClause: 今 (ref to current happening)
└── Expression: Composition
    ├── Subject: [alice, bob]
    ├── Predicate: 间 + 生 + 感
    ├── Modifier: 微 (intensity qualifier)
    ├── Object-ref: msg_001
    └── Property: 之 内 "..."
```

S-expression equivalent:
```
(間 :time 今
    :涉 [alice bob]
    :感 (生 :intensity 微)
    :内 (msg_001 "..."))
```

### 10.5 What's NOT in the Parsable Subset

The following are valid 古文 but **outside the parsable subset**, requiring S-expression:

1. **Heavy ellipsis** — 古文常省略主语和虚词,过度省略难 parse
2. **Poetic inversions** — 文学性的语序变换
3. **Archaic registers** — 上古汉语 vs 中古汉语 vs 近古汉语,都各有特点
4. **Quotations of historical text** — 这些是 string content,parser treats as string literals

间 用的是**可被 standardized 的简体古文 + 现代标点**——简洁、规范、可 parse,但保留古文 syntax 的核心特征。

---

## XI. Layer 3 工程化 — Attractor 与 Trajectory

v0.3 引入 Layer 3,但没说**怎么 detect**。这一节给 sketch 算法。

### 11.1 势 (Attractor) Detection

**问题**: 给定一个是的 history (its 间 stream),如何识别它倾向哪些 势?

**算法 sketch (Density-based)**:

```
势_detect(间集: 流<間>, 主: 是) -> 列<間>:
  // input: a stream of 间, plus the 是 whose attractors we're finding
  // output: list of 势-间 (each is itself a 間 representing an attractor)
  
  1. Project 间 into multi-dimensional state space
     - Each 维 (dimension): 感 strength, 修 manifest property, etc.
     - Each 间 becomes a point in state space
  
  2. Find density basins (kernel density estimation)
     - Where do points cluster?
     - Each cluster center → candidate 势
  
  3. Verify 势 properties:
     - 常 (persistence): 主 returns to this region over time
     - 强 (strength): how strongly is 主 pulled to this region
     - 久 (duration): across what time scales is it stable
  
  4. Return 势-间 meeting threshold of 强 + 常
```

**间 表达** (生成的势-间 looks like):
```
势_001 之 体: density_basin                  // (structural ground)
其 用: 见于 间_1 间_3 间_7 间_15 ...           // (manifests in these 间)
其 强 之 量: 0.78                             // (strength quantity)
其 久: 跨 三月                                // (duration: spanning three months)
其 涉: alice                                 // (whose 势 this is)
```

### 11.2 机 (Bifurcation) Detection

**问题**: 何时系统处于 机——微小扰动决定 trajectory?

**算法 sketch (Stability-based)**:

```
机_detect(间集: 流<間>, 当下: 间) -> 或<間>:
  // returns a 机-间 if current state is at a bifurcation point
  
  1. Compute local Lyapunov exponent at current state
     - High Lyapunov = sensitive to perturbation = near 机
  
  2. Check 距 (distance) to multiple 势 (attractors)
     - If close to multiple competing 势, 机 likely
  
  3. Look for historical 机-pattern:
     - Past 间 where small intervention changed 轨 significantly
     - Match current state to those patterns
  
  4. Return 机-间 if all three signals present
```

**间 表达** (生成的机-间 looks like):
```
今 见 机。
其 度 微 而 至。                              // (threshold subtle but reached)
若 alice 应, 则 势 趋 势_growth。            // (if alice responds, attractor tends to growth)
否, 则 势 趋 势_stagnation。
其 机 之 量: 0.85                            // (high — Lyapunov is high)
```

### 11.3 轨 (Trajectory) Tracking

**问题**: 给定一个是,如何构建它的 cultivation 轨?

**算法 sketch (Path through state space)**:

```
轨_construct(间集: 流<間>, 主: 是) -> 列<間>:
  // returns ordered 间 forming 主's trajectory
  
  1. Order 间 chronologically
  2. For each 间, compute state position
  3. Connect consecutive states as 轨 segments
  4. Identify current 势 (closest attractor)
  5. Estimate 速 (velocity — rate of state change)
  6. Predict short-term future based on 势 pull
```

**间 表达**:
```
alice 之 轨:
  自 状_initial 经 状_1 状_2 ... 状_n 至 今。
  现 趋 势_X。
  其 速 之 量: 0.3                              // (velocity quantity)
  其 期: 至 势_X 跨 二十 间。                    // (estimated 20 间 to reach 势_X)
```

### 11.4 节 (Phase Transition) Detection

**问题**: 系统什么时候发生 qualitative jump 而非 gradual change?

**算法 sketch**:

```
节_detect(间集: 流<間>) -> 列<間>:
  // returns 节-间 — moments where structure reorganized qualitatively
  
  1. Compute 常 (system-level invariants) over time
  2. Identify moments where 常 changes discontinuously
  3. Verify with structural metrics:
     - Network topology changes drastically?
     - 势 landscape reshapes?
     - 是-types reorganize?
  4. Mark these as 节-间
```

**间 表达** (生成的节-间 looks like):
```
team 之 节:
  自 体_growth 至 体_consolidation。            // (from-state to-state, both as 是)
  其 度 在 100 之 active_members。              // (threshold at 100 active members)
  时 2024-Q3。
  其 体 之 重组: 轨 自 loose 至 tight。         // (structural reorganization)
```

### 11.5 Counter-势 Intervention

最难也最关键:**如果 势 is unhealthy (e.g., 同质化 of manifest),如何引入 counter-势?**

这不是纯 algorithmic——it requires **designed intervention**。系统的 role 是:
1. **检测** unhealthy 势 (前面的算法)
2. **预测** 轨 toward 势
3. **建议** intervention candidates (based on historical similar cases)
4. **观察** intervention 之效

干预本身是 **人类决策 + 系统执行** 的混合过程。系统不替人决定 what is unhealthy——是 systematized 省 (reflection) 流程产生这个判断。

间 表达:
```
省 自身 曰:
  势_homogenization 之 势 增。                  // (the homogenization-attractor's strength is increasing)
  当 立 counter-势。                            // (a counter-attractor should be established)
  
建议:
  势_diversification 可 立。                    
  其 体: 结构 不易。                            // (structural ground unchanged)
  其 用: 增 维 之 数。                          // (functioning: increase dimension count)
  
等 auditor_1 auditor_2 auditor_3 之 应。

若 应 同, 则 立 counter-势。
否, 则 续 省。
```

### 11.6 工程实现 Stack

实现 Layer 3 需要的技术:

- **State space embedding**: PyTorch / similar tensor library
- **Density estimation**: KDE algorithms (scikit-learn 等)
- **Lyapunov computation**: numerical methods
- **Topology analysis**: network analysis libs (NetworkX 等)
- **Time series anomaly detection**: 多种现成方法

间 不是从零造这些——是**用 间 语言协调它们**。每个 detector 是一个 是,它的 manifest 是某个算法,它的 happenings 是 detection events。

---

## XII. 失与误 — 失败模式与错误处理

任何系统都会失败。间 中的失败不是"crash",是 happening 的某种特殊形式。

### 12.1 三种失败类型

**失 (shī) — 失去 / 丢失**

某个 是 应该 maintained 的状态被丢失。

```
alice 失 X 之系       ; alice loses connection to X
约 失 履              ; commitment fails to be fulfilled
是 失 manifest        ; an identity loses its manifest pattern
```

**误 (wù) — 错误 / 错位**

发生的 happening 与 intended happening 不一致。或者表达与 referent 不匹配。

但 **"误" 不在核心字** — 这是个 emergent expression。怎么 reduce?

```
误 = 应 + 违 = response that violates intended pattern
  = 失 + 当 = loss of appropriate fit
  = 表 + 异 + 实 = expression diverges from actuality
```

这显示一件事:**v0.3 的核心字不够覆盖错误**。"误" 必须被频繁使用,但它要 reduce 到 应+违 这种 awkward 组合。**v0.4 应该考虑加"误"或类似字进核心**。

候选加入:
- **误 wù** — error, mistake (reduces to 应违 but used so often)
- **过 guò** — excess, transgression (reduces to 度+越 but...)

**决定**: v0.4 把**误**加入核心字集 (新核心总数 125)。

**塞 (sè) — 阻塞** (already in core)

间不能流动。System dysfunction 的本体表达。

```
alice bob 之间塞     ; communication blocked between alice and bob
信道塞               ; channel blocked
约塞                 ; commitment can't progress
```

### 12.2 错误的 间 表达

错误本身是一次 happening。它有完整的 间 structure。

```
今 间涉 alice bob msg_001。
其 用: alice 欲 予 msg_001 与 bob。
其 实: msg_001 灭于 网络。
故: 其 间 误。

省 alice 曰: msg_001 失。
其 应: 复 予 msg_001。
其 修: alice 之 心 待 confirmation。
```

注意"误"作为新核心字的使用。整个错误处理是一个完整的 happening chain。

### 12.3 Validation 与 Type Errors

间 没有 static types。但可以 detect 不一致:

```
误_detect(待验: 间) -> 或<間>:
  // returns a 误-间 if inconsistency found
  
  1. Check 涉 constraints:
     - 涉 中的 是 都存在 (are referenced 是 valid)?
     - 数 (arity) 与 维 (dimension) compatible?
  
  2. Check pattern soundness:
     - Conflicts with historical patterns?
     - 例: "alice 予 X 与 bob" 但 alice 不持有 X
  
  3. Check temporal consistency:
     - 时序合理? (cause precedes effect?)
  
  4. If any check fails, generate 误-间 with explanation
```

错误是 **emergent from inconsistency**,不是 declared schema violation。

### 12.4 Recovery / 复

复 (restoration) 是错误后的自然回应。但**复不在核心字** — 它是 emergent。

```
复 = 归 + 立 = return-and-establish
  = 修 + 失 之 反 = cultivation reversing the loss
```

**Recovery 表达**:
```
alice 失 X 之系。
其 应: 寻 X。
其 修: 立 X 之 系 复。
```

### 12.5 Byzantine Failures

最难的: 是 故意 misrepresent 自己的 manifest 或 history。

间 的 architecture 要 detect 这种:

1. **Cryptographic signing** — 关键 happenings 必须由 是 的 ID 签名
2. **Multi-witness verification** — 重要 happenings 由多个独立 witness 见证
3. **Temporal consistency check** — 是 的 history 内部不能矛盾
4. **Cross-是 cross-check** — 不同是的 history 在交集处必须一致

如果这些 check 失败,触发 Byzantine 误-event:

```
今 验证 alice 之 history。
理见: alice 之 record 与 [bob carol] 之 record 异。
其 度: significant (>0.3)。

故: alice 之 history 误。
其 应: 标记 alice 为 suspected_byzantine。
等 community_audit 之 应。
```

**信 (trust)** 在这种情况变得显式:
```
alice 之 信 衰。
其 量: 自 0.8 至 0.4 跨 此事件。
```

---

## XIII. 是之边界与终结

v0.3 列了"灭"在存在动态,但没展开。一个 是 的 lifetime 怎么处理?

### 13.1 是 的边界 (Boundary)

**问题**: 一个 是 何时算 一个 是? 它的 boundary 是什么?

**答**: 一个 是 = a coherent happening chain 满足:
- 有持续的 ID(stable reference)
- 有持续的 manifest pattern(consistent across time)
- 有 reflection capacity (可以省自身 — 哪怕是简单的 system-level reflection)

**最小是 (minimal 是)**: 
- 一条消息: ID + content + sender — 这是 minimal 是 with very short lifetime
- 一次会议: ID + participants + happenings — 也是 minimal 是

**复杂是**:
- 一个人 (Ren): ID + 多年 manifest 演化 + 持续 reflection
- 一个社群 (706): collective ID + members + history + ongoing cultivation

**Boundary 模糊性**: 有些 是 的 boundary 不清楚——比如"团队"什么时候算一个独立的 是?这个**boundary 自身是一个 是**——一次 happening 中,boundary 被 negotiate。

```
今 间涉 [alice bob carol]。
其 间: 立 是 team_001。
其 涉: [alice bob carol] 共 立 team_001 之 是。
其 度: team_001 之 boundary 始 显。
```

Team_001 的 emergence 自身是一次 happening——三人共同认可它作为独立 是。

### 13.2 是 的演化 (Evolution)

一个 是 的 manifest 可以变,但 ID 不变。这是 cultivation 的 essence。

```
alice 自 (manifest_t0) 至 (manifest_today) 跨 五年。
其 ID 常。
其 manifest 经 [m1 m2 m3 ... m_today]。
其 修: 不断。
```

**boundary case**: alice 的 manifest 变得非常剧烈,与 t0 几乎完全不同。**还是同一个 alice 吗?**

这是**忒修斯之船** problem,在 间 中的处理:**身份由 history continuity 决定,不由 manifest similarity 决定**。只要 happening chain 不断,alice 是 alice。

但 **如果 chain 真的断了**(长期 inactive 后重新 active),系统可能需要**确认是同一是**:

```
今 alice@network_A active 后, 跨二十年。
其 history 与 alice@network_A_old 之 history 是否 续?

省 [community auditors] 曰:
  比对 cryptographic 签名: 同。
  比对 manifest: 异 (度 0.7).
  比对 self-claim: alice 自称续。

故: 暂判 续, 但 标 manifest_drift。
```

这是 是 的"觉醒"—— 长期休眠后的重新 active。

### 13.3 是 的灭 (Mortality)

灭不是简单的"删除"。它有结构。

**类型 1: 自然灭 (Natural End)**

是 主动声明终结。人类老死(由 representative 代为声明)、AI agent 主动退役、社群正式解散。

```
alice 之 终 间。
其涉: alice。
其 灭: alice 之 active happening chain。
其 反思 alice 曰: 吾终矣。

继 alice 之 history 入 archive。
其 ID 永存。
其 active happenings 不复。
```

**类型 2: 意外灭 (Abrupt End)**

是 没有最后声明就停止。需要**待**+**判**:

```
alice 之 happenings 自 三月前 终。
等 跨 六月 无 active happening。
故 系统 判: alice 灭。
但 标 abrupt, 不 finalized。
```

**类型 3: 强制灭 (Forced Removal)**

由于 Byzantine 行为或严重违规,community 决定 force terminate。

```
经 [auditor_1 auditor_2 auditor_3] 之 共 应:
  alice 之 history 误 reaches threshold。
  其 信 衰 至 critical。
  
故: alice 之 active capacity 灭。
其 history 留作 警。
其 ID 标 banned, 不复 issue。
```

**类型 4: 网络灭 (Network Death)**

整个网络终止。成员迁移或归 archive。

### 13.4 灭后的 happenings

死亡的 是 不完全静默。它的 history 仍可 reference。

**引用 (Quote)**:
```
今 bob 反思曰:
  alice 曰 (在 event_2024_05 中): "感在心,不在言"。
  此言 alice 之 灵 仍 启发 我。
```

**追思 (Memorial)**:
```
今 跨 alice 之 灭 之 周年。
间涉 [member_1 member_2 ... member_n]。
其感: 共 思 alice。
其修: 各 反 alice 之 教。
```

**遗志的延续**:
```
alice 之 志 曰: "完成 project_X"。
今 alice 灭, 其志 未 履。
应: [继承者] 立 约 续 之。
```

### 13.5 是 的 Birth

灭的对偶是生。一个新 是 怎么诞生?

```
今 间涉 [alice bob]。
其感 益。
故 立 是 friendship_001。
其 出 自 (alice bob) 之 共。
其 ID 立 cryptographic_id_xyz。
其 manifest 始 emerge。
```

或:
```
今 [alice bob carol] 共 商。
其 终: 立 是 project_001。
其涉: [alice bob carol]。
其 体: 协作之 际。
其 用: build something_X。
```

**新是 的诞生需要**:
- Active sponsor(s) — 一个或多个现有是 commit to 它的存在
- 初始 manifest — 它做什么
- Initial ID — cryptographic / domain / structural

诞生本身是一次 happening,完整记录。

---

## XIV. Worked Examples

每个 example 用古文 primary,S-expression 在 ambiguous 处或长 nested expression 处使用 fallback 显示 isomorphism。

### 14.1 简单消息

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

### 14.2 赠予

**古文**:
```
今 alice 以 gift_001 予 bob。
其感: alice 与 gift_001 渐疏, bob 与 gift_001 渐亲, alice 与 bob 益亲。
其修: alice 舍 gift_001 之系, bob 受之, gift_001 转所属, 自 alice 至 bob。
省 alice 曰: 祝吾友新婚。
```

**注**: 没有"赠"字——"赠"是 emergent pattern,系统从感衰盛 + 修舍受 识别这是 gift event。

### 14.3 立约 — 博士导师与学生

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

### 14.4 反思与修

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

### 14.5 多方共识

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

### 14.6 数量与时间

**古文**:
```
alice 自其生至今, 跨三十年。
```

或纯关系性(完全不用 calendar):
```
alice 自 event_1996_05_01 至 event_2026_05_01, 跨 ...
```

返回某个 quantity-relation,可以被显示为"30 年"(用 calendar reference)或更原始的 relation。

### 14.7 系统识别 attractor 漂移 (用上 Layer 3)

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

### 14.8 复杂 nested condition (S-expression fallback)

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

### 14.9 Federation — 间 跨网络

**古文**:
```
今间涉 alice@network_A 与 bob@network_B。
其感际立。
跨网络: network_A network_B。
```

`@network_X` 作为 ID 的 namespace 标记。跨网络的 happening 用同样语言表达。

### 14.10 Query 自身是 happening

**古文**:
```
问 alice 之 间, 自前七日至今。
其际之平与散, 其修之轨与进退,
其约之履与失, 其感之盛衰,
其心之静或动。
取之。
```

"问"也是一次 happening——它涉及 alice 这个被 query 的是,涉及一个 query agent,输出是 间 list。Query 不是"对系统的外部操作",是系统内部的一次 happening。

### 14.11 错误与恢复 — 消息丢失

真实工程场景:消息发送失败,系统检测,重试,最终成功或放弃。

**古文**:
```
事件1:
  今 alice 间 予 msg_001 与 bob。
  其 应: 期 bob 之 受。

事件2 (跨 五秒):
  待 久, bob 未 受。
  理见: 其 通 塞。
  故: 此 间 误。

事件3:
  alice 之 应: 复 予 msg_001 与 bob。
  此 间涉 [alice msg_001 bob]。
  其 序: 第二 试。

事件4 (跨 一秒):
  bob 受 msg_001。
  alice 之 心 安。
  失 之 复, 成。

省 alice 曰: 网络 偶 塞, 当 习 retry 之 度。
```

注意完整的 happening chain:发送 → 失败检测 → 重试 → 成功 → 反思。每一步都是一次 间。

### 14.12 Concurrent Updates — 并发修改冲突

两个是同时修改 shared resource。

**古文**:
```
事件A (时 t1):
  alice 修 doc_001 之 内: 易 第一节。

事件B (时 t1, 几乎同时):
  bob 修 doc_001 之 内: 易 第二节。

事件C (时 t1+ε, 系统 detect):
  理见: alice bob 之 修 同时 涉 doc_001。
  其 度: 各修 异节, 不 直接 衝。
  故: 自动 合 二修。
  生 doc_001@v2: 含 alice 之 易 与 bob 之 易。

事件D (alice bob 同时):
  alice bob 各 受 doc_001@v2 之 通知。
  其 信 在 系统 之 fairness。
```

但如果两人改了同一节:

```
事件C' (alternative):
  理见: alice bob 之 修 同 涉 第一节。
  其 衝。
  自动 合 不能。

  系统 之 应:
    保留 alice 之 修 (时序 略前)。
    bob 之 修 标 conflict, 待 bob 之 应。
    通知 [alice bob] 之 衝。

事件 D':
  bob 受 通知。
  其 应: 见 alice 之 修, 调整 自身 之 修。
  生 doc_001@v3: 二人 之 共同 修。
```

### 14.13 Byzantine — 不可信参与者

最难的:某个是 misrepresent 自己。

**古文**:
```
背景:
  alice bob carol 共 立约 project_001。
  alice 当 履 task_X。

事件1:
  alice 言 [bob carol] "task_X 履 矣"。

事件2 (验证):
  bob 验: alice 之 history。
  理见: alice 未 实 履 task_X。
  其 history 与 其 言 异。
  故: alice 之 言 误 (或 伪)。

事件3:
  bob 言 carol: alice 之 言 不 真。
  carol 验: 同。

事件4 (community 之 应):
  共 [bob carol] 之 反:
    alice 之 信 衰 自 0.7 至 0.3。
    标 alice 为 suspected_dishonest。
    其 后续 言 待 验 方 受。

事件5:
  alice 之 应: 二 可能。
  若 alice 之 误 因 系统 bug, 则:
    alice 申 解释。
    系统 audit alice 之 history。
    若 解释 真, 则 alice 之 信 复。
  若 alice 之 误 因 deceit, 则:
    alice 之 信 续 衰。
    项目 之 约 重立, 不含 alice。
    alice 标 为 byzantine。
```

注:**信** 在这里是 first-class quantity——可被 measure、tracked、affected by happenings。Byzantine handling 不是某种 special case,是 normal 间-language 流程。

### 14.14 灭 — 是的 graceful 终结

一个项目正式结束。

**古文**:
```
事件1:
  project_001 之 约 至 期。
  其 用 履 (full delivery)。
  其 体 仍 立。

事件2:
  共 [alice bob carol] 之 反:
    成 矣。
    续 之 需 否?
    答: 否。各 之 修 已 成。

事件3:
  立 project_001 之 终 间。
  其 涉: project_001。
  其 灭: project_001 之 active happening chain。
  其 反思 共 曰: "始 于 (event_X), 终 于 今。共 学 颇 多。"

事件4:
  project_001 之 history 入 archive。
  其 ID 永存, 但 active 不复。
  [alice bob carol] 之 际 不 因 此 灭。
  反 益 — 共 经 事, 际 益 深。

事件5 (跨 一年):
  alice 反思曰:
    project_001 已 灭, 但 其 教 仍 活 于 我之 修。
    引 (project_001 之 反思 第三): "..."
```

注:即使项目灭了,它的 history 仍可被 quote、reference、影响后续 happenings。这是 v0.4 第 XIII 节"灭后的 happenings"的具体应用。

---

## XV. 工程接口

### 15.1 数据底层

唯一的本体单位:**间**。所有数据是间的 stream。

```
間 {
  是: 是                   // identifier — this 间's handle for reference
  涉: 集<是>               // (involvement) — which 是 are involved
  涉态: 列<涉态>           // (involvement-modes) — modes across dimensions
  时: 时                   // (time-ref) — calendar string or 间 reference
  反思: 或<反思>           // (optional reflection trace)
  引: 集<是>               // (reference) — relations to other 间
  
  // Layer 3 — 动力学 attachments (all optional)
  // 这些都是 reference to 间, which themselves are 势/轨/机/节 patterns
  势: 或<是>               // (attractor reference)
  轨: 或<是>               // (trajectory reference)
  机: 或<机态>             // (bifurcation context, if at critical point)
  节: 或<节态>             // (phase transition record, if at jump)
}

涉态 {
  维: 是                   // (dimension) — 维 is itself an 是
  数: 数                   // (arity) — 1, 2, 3, N
  参: 子集<是>             // (participants) — subset of involved 是
  式: 增 | 减 | 衰 | 盛 | 生 | 立 | 破 | 转 | ...   // (pattern)
  量: 或<量>               // (intensity, if applicable — emergent quantity)
}

反思 {
  者: 是                   // (reflector) — which 是 is reflecting
  内: 列<文 | 间>          // (content) — text or other 间 references
}

机态 {
  度: 量                   // (threshold value)
  距: 量                   // (proximity to bifurcation)
  趋: 列<势>              // (potential attractors, in 势-references)
}

节态 {
  自: 是                   // (from-state — references previous structure-间)
  至: 是                   // (to-state — references new structure-间)
  度: 量                   // (threshold crossed)
}
```

**注解** (comments 用英文是工程妥协,不是本体姿态):

- 是 (shì) as a *type* means "an 是-reference" — i.e., an identifier handle. 是 (shì) as a *value* means a specific 是 instance referenced by that handle.
- 维 (wéi) is itself an 是: a dimension like "trust", "spatial-proximity", "time" is referenced by ID.
- 量 (liàng) is emergent quantity — a relational measure derived from the 间, not a stored primitive.
- 集 = Set, 列 = List, 子集 = Subset, 或 = Optional, 数 = Number(数 here as quantity-relation, see Section IV)

### 15.1.1 没有单独的 type for 势 / 轨 / 机 / 节

一个 attractor (势) 是一个间 — 它的 manifest 是 "I attract" pattern。一个 trajectory (轨) 是一组 ordered 间 — referenced via 是。同理 机 (bifurcation) 与 节 (phase transition)。

```
// 势之 view (attractor view) over 间-stream
势_view(间集: 流<間>, 范围: 集<是>) -> 列<間>:
  // returns the 间 that happen as attractors within this scope
  // each returned 间's manifest 是 "this attracts these 是"

// 轨之 view (trajectory view) for a specific 是
轨_view(间集: 流<間>, 主: 是) -> 列<間>:
  // returns ordered 间 forming 主's trajectory through state space

// 机之 view (bifurcation detection)
机_view(间集: 流<間>, 当下: 间) -> 或<間>:
  // returns 机-间 if current state is at a bifurcation point

// 节之 view (phase transition detection)  
节_view(间集: 流<間>) -> 列<間>:
  // returns 节-间 — points where structure reorganized qualitatively
```

**所有 view functions 输入 + 输出都是 间**。一切是间。没有 "special data type",只有 special views——它们都返回间的 subset 或 ordered list。

这与本体一致到底:不只 ontologically ("一切是间"),也 in data structure ("所有 type 是 間"),也 in API ("所有 function 输入输出是 間")。**Three-level coherence**。

### 15.2 Storage

存储 = append-only log of 间。

技术参考:Datomic、EventStore、Kafka log compaction。但间比这些更彻底——所有 query 都是 fold over log,**没有"current state"作为 stored object**。

### 15.3 问 (Query)

问 (query) 自身是间。系统接收一个 问-间,返回间集。

技术参考:Datomic 的 datalog query、GraphQL subscription。但 间 的 问 用 same language as 系统 other parts——一切是间,包括 queries。

### 15.4 时 (Time)

不存储 absolute time。每个间有 时-reference,可以是:
- Calendar string (`2026-05-01T14:30`) 作为 是,refer 到 wall-clock 间
- 间 reference (`间_001`) 直接 refer 到另一个间
- Relative expression (`前 间_X 五日` or in S-expr `(前 间_X 五日)`) 作为派生

时间运算 = relation arithmetic between 间,not unit-based。

### 15.5 是 (Identity)

是 系统:
- 默认 cryptographic public key(Ed25519、DID-style)
- Composite 是 for groups: `[alice bob]`
- Domain 是: `project_001`, `msg_5`
- Calendar 是: `2026-05-01`

是 的 spoofing 防御:核心间必须由 是 持有者签名。

### 15.6 Evolution

类型 emergent,运行时可观察、可统计、可演化。

修(cultivation)作为 first-class operation——一个是自己改变自己的 manifest 是合法 happening,不是 schema migration。

### 15.7 Prototype Path

**Phase 1**: Clojure-based DSL。用 Clojure macros 实现核心字 keywords。基于 Datomic 或类似 store。Parser 支持古文 primary syntax + S-expression fallback。几周到 1-2 月工作量。

**Phase 2**: 独立 parser + interpreter。古文 syntax 的 well-defined subset + S-expression。1-2 月。

**Phase 3**: 完整 runtime——distributed event log + identity system + reactive evaluation + Layer 3 attractor detection。3-6 月。

**Phase 4**: 形式 specification——把间的 semantics 写成 categorical structure。无固定时间表。

### 15.8 与现有 stack 的接口

- **Persistence**: 任何 append-only store。Datomic / EventStore / Kafka / IPFS
- **Network**: libp2p / 类似 P2P
- **Crypto**: standard Ed25519、Blake3、Merkle DAG
- **Compute**: any runtime。Clojure / Elixir / Rust 都合适

间的 architecture 是 thin layer——大部分技术 building blocks 已存在。新的工作是**把这些 blocks 用间-language 组合,且坚持本体一致性**。

---

## XVI. 与传统对话

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

## XVII. 限度

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

## XVIII. 接下来

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

## 附录 B: 核心字快查表 (146)

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
| | 曰 | yuē | say (quote-introducer) |
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
| | 来 | lái | coming |
| | 往 | wǎng | going |
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
| | 源 | yuán | source |
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
| | 还 | huán | return-owed |
| 强度 | 盛 | shèng | flourish |
| | 衰 | shuāi | wane |
| | 强 | qiáng | strong |
| | 弱 | ruò | weak |
| | 深 | shēn | deep |
| | 浅 | qiǎn | shallow |
| | 微 | wēi | subtle |
| | 显 | xiǎn | manifest |
| | 极 | jí | extreme |
| 距离 | 亲 | qīn | close |
| | 疏 | shū | distant |
| | 合 | hé | joined |
| | 分 | fēn | separated |
| | 内 | nèi | inner |
| | 外 | wài | outer |
| | 中 | zhōng | center |
| | 通 | tōng | flowing |
| | 塞 | sè | blocked |
| | 子 | zǐ | sub / part-of |
| | 属 | shǔ | belonging-to |
| 反思 | 思 | sī | think |
| | 虑 | lǜ | deliberate |
| | 知 | zhī | know |
| | 觉 | jué | awaken |
| | 悟 | wù | realize |
| | 省 | xǐng | reflect |
| | 见 | jiàn | see / encounter |
| | 观 | guān | observe |
| | 念 | niàn | thought-instance |
| | 明 | míng | clear |
| | 迷 | mí | confused |
| | 忘 | wàng | forget |
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
| | 流 | liú | flow |
| | 聚 | jù | gather |
| | 渐 | jiàn | gradual |
| 体用 | 体 | tǐ | structure |
| | 用 | yòng | manifestation |
| | 本 | běn | root |
| | 末 | mò | surface |
| 心性 | 心 | xīn | heart-mind |
| | 性 | xìng | nature |
| | 情 | qíng | situation/emotion |
| | 意 | yì | intention |
| | 志 | zhì | will |
| | 欲 | yù | desire |
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
| | 偏 | piān | biased |
| epistemic | 真 | zhēn | true |
| | 伪 | wěi | false |
| | 误 | wù | error |
| 言说 | 言 | yán | words |
| | 默 | mò | silence |

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

## 附录 E: Common Idioms — 常见 happening patterns

实践中频繁出现的 happening patterns。这些是 emergent—可由核心字组合表达,但作为 idiom 学起来更快。

### E.1 通信类

```
A 言 B "..."           ; A says to B "..."  (实是: 间涉 [A B msg], A 予 msg 与 B)
A 问 B "..."           ; A asks B
A 答 B "..."           ; A answers B
A B 共商                ; A and B deliberate together
```

### E.2 协作类

```
A 助 B X               ; A helps B with X (实是: 间涉 [A B X], A 之力 益 B 之 X)
A 委 B X               ; A delegates X to B (实是: A 立约, B 履)
A B 协 X               ; A and B coordinate on X
```

### E.3 关系演化

```
A B 渐亲              ; A and B grow closer (际 之 亲 增)
A B 渐疏              ; A and B grow distant
A 信 B               ; A trusts B (实是: A 之 信 之 量 高 于 B)
A 疑 B               ; A doubts B
A B 和                ; A and B are in harmony
A B 衝               ; A and B in conflict
```

### E.4 状态变化

```
X 成                  ; X completes/succeeds
X 败                  ; X fails
X 立                  ; X is established
X 破                  ; X breaks
X 续                  ; X continues
X 终                  ; X ends
```

### E.5 修身类

```
A 修 X               ; A cultivates X
A 学 X               ; A learns X (实是: A 之 manifest 修 by X)
A 习 X               ; A practices X (实是: 修 with 循)
A 悟 X               ; A realizes X
A 改 X               ; A changes X
```

注:学/习/改 都是 emergent。系统内部 reduce 到核心字。

### E.6 决策类

```
A 决 X               ; A decides X (实是: A 之 志 立 于 X)
A 让 B               ; A yields to B (实是: A 退, B 进)
A 拒 X               ; A refuses X (实是: A 之 应 否 X)
A 受 X               ; A accepts X
```

### E.7 错误与恢复

```
A 失 X               ; A loses X
A 误 X               ; A errs at X
A 复 X               ; A restores X (实是: 修 之 反 失)
A 谢 B               ; A apologizes/thanks B (实是: A 之 心 应 B 之 益)
```

注:谢 在中文同时有"道歉"和"感谢"——根据 context disambiguate。系统内部用 happenings chain 区分。

### E.8 知识与发现

```
A 知 X               ; A knows X
A 不知 X             ; A doesn't know X (实是: A 之 知 无 X)
A 见 X               ; A sees/perceives X
A 信 X 是 真          ; A believes X is true
```

### E.9 时间表达

```
今 X                  ; X happens now
昔 X                 ; X happened in the past
来 X                 ; X will happen / X is coming
跨 N 时 X            ; X spans N (with 时 as some reference)
循 周 X              ; X recurs weekly (with 周 as a reference)
```

### E.10 量度表达

```
量 N 元              ; N RMB
跨 N 米              ; N meters
跨 N 日              ; N days
量 多                ; many / much
量 少                ; few / little
其量 N               ; its quantity is N
```

---

*End of Foundation Note v0.5.*

*v0.5 完成 vocabulary architecture:*
- *146 个 Tier 1 core characters covers full relational phenomena space*
- *Tier 2 standard vocabulary as emergent shortcuts (告、助、教、学、复、谢、含、病、趋 等)*
- *Tier 3 domain-specific expressions as community/project freedom*
- *Three-tier 类比 programming language: kernel / stdlib / user code*

*这份 Note 现在 prototype-ready 且 vocabulary-complete。下一步:Clojure prototype。在 OpenClaw 内选一个限定场景,实施第一个间-runtime,看哪些 design decisions 在工程压力下成立、哪些需要修正。Foundation Note v0.6 will be informed by prototype experience.*
