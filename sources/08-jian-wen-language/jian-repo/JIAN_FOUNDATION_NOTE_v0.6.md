# 間: Foundation Note

## v0.6 · 返本 — 二与八

**Version**: 0.6 · *radical simplification, 返古文之原*
**作者**: Ren
**协作起草**: Claude

**v0.6 重构**: 不是 incremental 修订,是 vocabulary architecture 之重审。
- **Tier 0 收为二字**:**间、涉**——实为一相二称(间是 noun-aspect,涉是 verb-aspect)
- **Tier 1 八象**:**是、际、感、化、修、约、势、理**——八字尽涉之相
- v0.5 之 146 字尽归 **Tier 2** (emergent idioms),由二与八派生
- **去"-态"后缀**:涉态、机态、节态 不再是 named structures。"-态" 是日译"state"之回译,非古文构词。古文以 **象、相、容、几、势** 各述某事之 mode,字 carries aspect 自身
- **去"反思"复合词**:省即反思,念即专念之察。古文已分:**思**(active reasoning)、**虑**(deliberation)、**念**(mindful attention)、**省**(self-examination)、**观**(sustained contemplation)、**悟**(insight)。不需要现代合成词
- **假想东方工程学**:若华夏传统不经 Western 工业革命,直接由文言文 + 易经体用论 + 心学 发展工程学,会是何样?(speculative design 章)

**前置说明**: 本体声明未变(一切是间)。改变的是**字之归层** + **Eastern engineering 视野的明显化**。读者如已熟 v0.5,可直接跳到 II、III、IV 章——那里是 v0.6 之新。

**v0.5 changelog 摘**: 146 字,三层 vocabulary,Layer 3 工程化。  
**v0.4–v0.1 changelog**: (略,见 v0.5)

---

## 目录

I. **重新立论 — 间即涉,涉即间**
II. **八象 — 涉之八相** *(new in v0.6)*
III. **推 — 一切由二与八生** *(new in v0.6)*
IV. **假想东方工程学** *(new in v0.6, speculative)*
V. **间之结构 — 极简数据**
VI. **八象 as Views**
VII. **失、塞、误、复 — 不需要例外**
VIII. **是之生灭**
IX. **重审 worked examples** (v0.6 voice)
X. **与 v0.5 之对照**
XI. **限度**
XII. **接下来**

附录 A: 一句话本体  
附录 B: 二与八快查  
附录 C: **v0.5 之 146 字 → v0.6 派生表**  
附录 D: 古文 syntax 速查  
附录 E: 古文 ↔ S-expression 转换  

---

## I. 重新立论 — 间即涉,涉即间

### I.1 一切是间

> **一切是间。間 是唯一原语。間 即 happening,即 function evaluation。**

本体声明未变。但语言 surface 应再清。v0.5 把"间"作 Tier 1 中"结构原语之一",与"涉"并列——这有 modeling artifact 之嫌。**间与涉非二事**:间是其 noun 之相,涉是其 verb 之相。古文不预设 noun-verb 二分,故二字本是同一现象在不同语法位置的呈现。

### I.2 间与涉之同

考其字:
- **间**(jiān):本义为"门中见日"(《说文》"閒,隙也")。门、墙、关之间的 空隙、间隔、关系空间。后引申为"在中间"的状态、关系、时刻。
- **涉**(shè):本义为"徒行涉水"(《说文》"涉,徒行濿水也")。从一岸到另一岸,涉过中间。后引申为 介入、参与、关联。

二字共有的核心:**有此岸彼岸,中间是空隙、是 transit、是 happening**。

间是这空隙的 noun-form——"在 X 与 Y 之间";涉是这空隙的 verb-form——"自 X 涉 Y"或"X 涉 Y"。

**它们指同一现象**:间 (the field-of-between) 即 涉 (the wading-through-between)。

```
间 X Y    (noun-form: 在 X 与 Y 之间发生事)
X 涉 Y    (verb-form: X 涉 Y, an event)
```

二者本体等价。古文之妙处在于一个现象可分别用 noun 和 verb 表达而不偏不倚。

### I.3 为什么这二字是 Tier 0

**因为它们足够,且不可再分**。

- 不可再分:任何更小的本体 unit(state、object、event、process 等)都已经预设了 间(空间-时间-关系的 differentiated 结构)
- 足够:any happening 都可以表达为"X 涉 Y 于 Z 之间"——其余都是这一基本结构的 specialization

**为什么不只用一字?**

可以只写一个 character。但古文的语法承担本体功能:
- 用 "间" 时,焦点在 the field/locus
- 用 "涉" 时,焦点在 the activity/transit

两 surface forms 一同提供更精细的 expressiveness。这与一元本体 not 矛盾——同一本体,不同 grammatical posture。

类比:Lambda calculus 也是一元本体(只有 function),但表达式中有 application、abstraction 不同 surface forms。

### I.4 古文中"间"族字 verifies completeness

古文已有完整的 vocabulary 描述间的 sub-structures——不需要造词:

| 字 | 描述的"间"之相 |
|----|----------------|
| 间 | 门窗之缝,引申为关系空间 |
| 际 | 边界、relations 之 manifest |
| 隙 | 缝隙、可乘之机 |
| 缝 | 接缝处 |
| 隔 | 阻隔、分开的间 |
| 距 | 物理或抽象之距离 |
| 阔 | 宽阔之间 |
| 余 | 余地、剩下的空间 |
| 旁 | 侧边的间 |
| 邻 | 紧邻的间 |
| 周 | 周围、circumference |
| 中 | 中央 |
| 外 | 之外 |
| 内 | 之内 |
| 涉 | wading through 间 |
| 履 | 踩踏过 间 |
| 越 | 跨越 间 |
| 通 | 贯穿 间 |
| 塞 | 阻塞 间 |
| 几 | 间 之 incipient 微动 |

**古文已经把"间"现象描述清晰**。v0.5 之误,在于借日译的"-态"组合(涉态、机态、节态)——好像古文表达不够精,需 Western 来补。其实是不需补的:**古文本来就是为这本体写的语言**。

---

## II. 八象 — 涉之八相

### II.1 何为八象

每一次 涉 同时具有八个 aspect。这八个不是 separate things,是同一 涉 的不同 facets。我们把它们称作 **八象**(八字 = the eight-char tier)。

**Tier 1 八字**:

```
是  shì    — 涉之主    (who/what is involved)
际  jì     — 涉之间    (the relation that emerges)
感  gǎn    — 涉之觉    (the felt quality)
化  huà    — 涉之果    (the transformation effected)
修  xiū    — 涉之自    (the self-evolution induced)
约  yuē    — 涉之锁    (the time-binding established)
势  shì    — 涉之趋    (the latent tendency carried)
理  lǐ     — 涉之常    (the invariant pattern followed)
```

(注:**势** 与 **是** 同音 shì,但字义、调性、本体角色截然不同。古人择字精,二字虽同音不混淆。)

### II.2 为什么是这八

每一象 capture 涉 之一个 irreducible aspect:

**第一组 — 觉之四象**(immediate phenomenology of 涉):
- **是**:涉 之中谁在?(who-aspect)
- **际**:涉 之间何在?(between-aspect — the relation that emerges)
- **感**:涉 之触如何?(felt-aspect — qualitative resonance)
- **化**:涉 之后何变?(change-aspect — what is transformed)

**第二组 — 持之四象**(enduring dynamics of 涉):
- **修**:涉 改 涉者本身。(self-cultivation: the涉-er becomes other through涉)
- **约**:涉 锁未来。(time-binding: 涉 commits to future patterns)
- **势**:涉 倾何方。(tendency: latent attractor pull)
- **理**:涉 守何常。(invariant pattern that the涉 conforms to)

**配对**:
- 是 ↔ 际 (one ↔ between)
- 感 ↔ 化 (felt ↔ effected)
- 修 ↔ 约 (self-binding ↔ other-binding)
- 势 ↔ 理 (becoming ↔ being)

或:
- 是、际 = 涉 之 *who-and-where*
- 感、化 = 涉 之 *quality-and-effect*  
- 修、约 = 涉 之 *time-faces* (subject-time, object-time)
- 势、理 = 涉 之 *dynamics-faces* (variant pull, invariant law)

### II.3 八象之足以

何以八字足以 cover 所有现象?

**Claim**: 每个 v0.5 中除二字 (间、涉) 外的 144 字,皆可表示为这八象之 derivation——通过 modifier、组合、对比、特化。详见 III 与附录 C。

**Counter-claim**: 也许有 happening 类型这八象 cannot capture。这是 v0.6 prototype 应验证的。但 worked examples 至今无 counter-example。

**为什么不是 7 或 9?**

- 少于 8 (e.g., 不要"理"或不要"势"):则 dynamics 的两面 (variant 与 invariant) 会塌缩,系统无法表达 attractor 与 pattern 之分。
- 多于 8 (e.g., 加"几" / "节" / "体"):它们是有用的概念,但 derivable。**几 = 势之微**;**节 = 化之质变**;**体 = 是之常 + 际之常**。加入它们会引入 redundancy。

8 象与 易经八卦同数。这不是巧合——华夏传统以八为完备(乾兑离震巽坎艮坤,八方而尽)。但本节不是 cosmological commitment——是发现 8 在工程上恰好 minimal-yet-complete。

### II.4 八象作为 lattice

八象不是一个 list,是一个 lattice:

```
                        间
                         |
                         涉
                ___________________
               /         |         \
            觉之四      持之四
        ___________   ___________
       /  |  |   \   /  |   |   \
      是 际 感   化  修 约   势 理
```

每一次 涉 选取八象之子集 manifest。一次完全 涉 八象皆显;一次微 涉 可能只显几象。

例:
- "alice 见 msg" — 涉 显 是 + 感 (微)
- "alice 与 bob 立约" — 涉 显 是 + 际 + 约 (突出)
- "alice 三月 cultivate work habit" — 涉 显 修 + 势 + 理 (突出)

每个 涉 是八象 lattice 中一个 subset 的 highlight。

---

## III. 推 — 一切由二与八生

### III.1 派生原则

派生不是 strict reduction(那是 Western 还原论的姿态)——是 *manifestation*。即:每个 v0.5 中的字,在 v0.6 中是八象组合在某种限定下的 *characteristic manifestation*。

类比:HSL 颜色空间用三原 (Hue, Saturation, Lightness) 表达所有颜色——派生的具体颜色名(crimson, teal, amber)是这三原值的某 region 命名。八象之于 v0.5 字集亦如此。

### III.2 派生方式

四种派生 pattern:

**派生 1 — 限定**(specialization):某象 + modifier
```
势 之 临界  →  机
化 之 质变  →  节
化 之 缓     →  渐
化 之 速     →  突 / 忽
势 之 边     →  度
化 之 显     →  变
化 之 反     →  归 / 还
```

**派生 2 — 反对**(complementary opposition):某象 之 X / 之 反X
```
感 之 满 / 虚  →  盛 / 衰
感 之 坚 / 柔  →  强 / 弱
感 之 入 / 表  →  深 / 浅
感 之 隐 / 显  →  微 / 显
际 之 近 / 远  →  亲 / 疏
际 之 并 / 离  →  合 / 分
际 之 同 / 异  →  同 / 异
涉 之 进 / 后  →  进 / 退
涉 之 通 / 阻  →  通 / 塞
涉 之 真 / 假  →  真 / 伪
涉 之 始 / 终  →  生 / 灭
化 之 立 / 破  →  立 / 破
化 之 成 / 败  →  成 / 败
势 之 显 / 潜  →  显 / 潜 (之 隐)
```

**派生 3 — 视角**(view from internal/external/sustained perspective):
```
修 之 反       →  省  (self-toward-self)
修 之 久察    →  观
修 之 始       →  觉
修 之 通       →  悟
修 之 显       →  明
修 之 乱       →  迷
修 之 失       →  忘
涉 之 觉       →  见
修 之 微       →  念
涉 之 觉之主 →  思 (with intention)
修 之 计      →  虑 (deliberative)
涉 之 实       →  知
际 之 恒       →  信
```

**派生 4 — 主体姿态**(subject-perspective on 涉):
```
涉 之 内向     →  受
涉 之 外向     →  予 / 与
涉 之 释      →  舍
涉 之 收      →  取
涉 之 至       →  得 / 来
涉 之 失       →  失
涉 之 转       →  转
涉 之 还       →  归 / 还
势 之 求      →  欲
约 之 自立     →  志
涉 之 向       →  意
是 之 内涉     →  心
是 之 常       →  性 / 体
是 之 变       →  情
是 之 源       →  本 / 源
涉 之 表       →  末 / 用
```

### III.3 完整派生表

完整 144 字(v0.5 减去 间、涉 二字 = 144)派生见**附录 C**。这里给出 select samples:

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 機 (jī) | 势 之 临界 |
| 节 (jié) | 化 之 质变 |
| 度 (dù) | 势 之 边 |
| 渐 (jiàn) | 化 之 缓 |
| 流 (liú) | 涉 之 续 |
| 聚 (jù) | 际 之 合 |
| 散 (sàn) | 际 之 分 |
| 中 (zhōng) | 际 之 心 |
| 偏 (piān) | 际 之 斜 |
| 极 (jí) | 感 之 至 |
| 体 (tǐ) | 是 之 常 |
| 用 (yòng) | 涉 之 表 |
| 心 (xīn) | 是 之 内涉 |
| 性 (xìng) | 是 之 不易 |
| 情 (qíng) | 是 之 易 / 涉 之 感 |
| 意 (yì) | 涉 之 向 |
| 志 (zhì) | 约 之 自立 |
| 欲 (yù) | 涉 之 求 |
| 误 (wù) | 涉 之 乖 |
| 失 (shī) | 涉 之 断 |
| 言 (yán) | 涉 之 语 |
| 默 (mò) | 涉 之 不语 |
| 唱 (chàng) | 涉 之 先 |
| 应 (yìng) | 涉 之 后 |
| 和 (hé) | 际 之 韵 |
| 同 (tóng) | 际 之 一 |
| 力 (lì) | 涉 之 能现 |
| 能 (néng) | 涉 之 能潜 |
| 权 (quán) | 际 之 衡 |
| 位 (wèi) | 际 之 占 |

(完整表见附录 C。)

### III.4 注意:派生不是消除

派生使我们看到字之间的 ontological 关系。但实际书写时**仍然用单字** for brevity。如:

```
v0.6 day-to-day 表达:
  alice 与 bob 之 际 渐 亲。              ; 用"亲"(派生自 际之近)
  
v0.6 explicit 形式:
  alice 与 bob 之 际,其 距 渐 减。       ; 用八字直接拼

二者意思相同。前者是 Tier 2 idiom,后者是 Tier 1 explicit。
```

**Tier 2 idioms 仍然在日常使用**。v0.6 不是说从此只用八字写。是说**ontological commitment 在八字**——所有 Tier 2 idioms 都明白如何 reduce to 八字。

类比 Lisp:`(map f xs)` 是 idiom,but you know it's `(reduce cons '() (... walk xs ...))` underneath。这种 derivability 给系统 strong invariants。

### III.5 涉之与 间之

读者会注意 III 节常见 "涉 之 X" 和 "X 之 Y" 之类。古文之之字,承担 modifier-head 关系。v0.6 用之字 systematic:

- **X 之 Y**:Y 在 X 之 sub-aspect 位置
- **X 之 Y 之 Z**:右结合 = X 之 (Y 之 Z)
- 涉 之 X = "an aspect of 涉" 比喻为 "X-face of 涉"

这是古文之自身的 algebra。无须发明 modifier syntax。

---

## IV. 假想东方工程学

### IV.1 假想

> 若华夏传统不经 Western 工业革命,直接由文言文 + 易经体用论 + 心性学 发展工程学,**会是何样**?

这一节是 speculative。但不是 idle:它揭示了 v0.5 中残留的 Western 偏向,启示 v0.6 应去之而立东方姿态。

### IV.2 西方工程学之根

Western engineering 立于:
1. **Aristotelian 实体论**:先有 entity,后有 relation。物 → 关系。
2. **Newton 机械论**:force, mass, motion;cause → effect。Discrete entities, discrete events。
3. **Cartesian 二元**:body / mind, subject / object, inside / outside。
4. **Atomism**:parts make whole。从最小单位组装。
5. **Linear time**:absolute, uniform。
6. **Static types**:类型先于实例,schema 先于 data。
7. **Exception model**:happy path vs error path,不属于 happy path 走 exception。

由此出来:
- OOP (object first, relation as method)
- 类型系统 (declared types, type errors)
- 算法 (deterministic causal sequences)
- 测试 (assertion of fixed expected outputs)
- 数据库 schema (predefined tables)
- 错误模型 (try/catch as separate path)

这套很 powerful——也很 brittle when reality 是 fluid、relational、emergent。

### IV.3 东方工程学之根

如果我们从华夏传统 directly 发展出工程学,本体根基会不同:
1. **关系本体**(《周易》《道德经》《华严经》):际 先于 是。关系 → 实体。
2. **理气论**(宋明理学):pattern (理) 与 energy (气) 不分,体 用 不二。
3. **心物不二**(陆王心学):cognition embodied,observer 不在 system 之外。
4. **气脉论**(医家、内丹):部分由 whole 之 flow 派生,而非 whole 由 parts assemble。
5. **时空一**(《周易》"时位"):时间是 timeliness,不是 axis。
6. **变易论**(《周易》"生生不息"):一切在 化,categories 是 transient pattern detection。
7. **诚-复模型**(《大学》"诚意正心",《周易》"无咎"):不区分 happy / error path——一切是 涉,失了就 复。无咎不是无失,是有失能复。

由此应可能发展出:
- **关系结构编程**:不是 OOP,是 **际编程**——结构是 dynamic relations,实体是 emergent
- **无类型动态系统**:类型不 declared,从 history 中 detect。"types are emergent groupings"
- **理-体-用 archtecture**:不是 abstract class + subclass,是 体 (substrate) + 用 (manifestation)。同一 体 多 用,不同 体 同 用 都自然
- **应时编程**:不是 fixed schedules,是 应 时——执行 timing 由 context 决定
- **气脉式数据流**:不是 pipes,是 通塞 监测下的 relational flow
- **修式系统**:系统通过其自身 operation 演化自身——"cultivation as first-class operation"
- **诚朴错误模型**:无 try/catch。一切是 涉。涉 失则 涉 复。失 itself 是 事 (happening),复 也是 事
- **几 工程**:工程师 attend to 几——the subtle pre-emergence of issues。这与 Western "exception" model 反——not "wait for it to break, then handle",而 "see it before it breaks, intervene at 几"

### IV.4 假想东方系统的几个 specific 特征

**A. 没有 "object" 与 "method" 二分**

无 OOP。系统是 涉 之 stream。每个 涉 涉及 是 (这是参与者),manifest 在八象中。"behavior" 是 涉 之 manifest,not method-of-object。

```
v0.5 (OOP-influenced):
  alice.sendMessage(bob, "...")

v0.6 (东方姿态):
  涉: alice 与 bob,予 msg。其 化: msg 自 alice 至 bob。
```

第二种不假装 alice 是 "agent acting on" bob;它只是说一次 涉 happen——alice、bob、msg 三者皆在涉中,各有 role。

**B. 没有 "current state" 概念**

系统不存"当下 state"。当前是一个 view 计算——fold over history。

```
"alice 之当下" = 关于 alice 的所有 涉 之 fold view
```

这不是 lazy evaluation;是本体姿态——**没有 frozen state to be queried**。Query 是再次 fold history。

**C. 错误 即 涉,复 也是 涉**

无 exception。只有 涉:

```
v0.5/Western style:
  try { send(msg) } catch (NetworkError) { retry() }

v0.6/Eastern style:
  alice 予 msg 与 bob。
  涉 之 通 失。
  alice 之 应:复 予。
```

第二种里"通失"不是异常,是一个 涉 之 manifest——际 之 塞。复 也是一次 涉。**无 happy-path / error-path 二分。一切是 涉。**

**D. 应时 vs 调度**

任务执行时机不靠绝对时钟,靠 应时——根据 context dynamic 决定:

```
v0.5/Western:
  setTimeout(emailReminder, 24*60*60*1000)

v0.6/Eastern:
  约: alice 当 应 此 message。
  应时: 视 alice 之 念 之 间,与 共修者 之 间。
```

应时 = "respond in due time" = system 见 alice 当下 context 而决定 reminder 的合适时机,不强制 24 小时。

**E. 几 监测 而非 alert**

```
v0.5/Western:
  if (cpu > 90%) alert(adminEmail)

v0.6/Eastern:
  观: 系统 之 势,其 趋 之 变。
  见 几: 当 势 微 变 (微 detection ≠ threshold cross),
         即 应 — 调 系统 之 修。
```

几 = "the subtle pre-emergence of motion"。系统 attend to 几 而不是 wait for hard threshold。这是 active 感知 而非 reactive alert。

**F. 体用不二的接口设计**

```
v0.5/Western:
  // Define interface
  interface Sender { send(msg: Msg, target: Address): Result }
  
  // Implement
  class EmailSender implements Sender { ... }
  class SlackSender implements Sender { ... }

v0.6/Eastern:
  send 之 体: 涉 — 予 msg 与 target。
  其 用 多面: email_send、slack_send、im_send 皆其 manifest。
  
  各 user 见 之 用 (manifestation),系统 知 其 体 (substrate)。
  无 "interface" 与 "implementation" 之分——一字两面。
```

体用不二:不是先有 interface 再 impl;是同一现象 viewed at structure-level (体) 与 manifestation-level (用)。这与 Plato 之 form/instance 二分相反:不是 abstract 在 concrete 之 prior,是同一 thing 之两面。

**G. 修身式系统**

系统通过 reading its own history 而 evolve:

```
省 自身:
  自前千日 之 涉 history。
  理见: 我之 manifest 渐 偏 同质化。
  其 几 显。
  故 修:
    立 counter-势。
    不易 体, 增 用 之 维。
```

系统是一个 "可自反思自演化的 agent"——这在 v0.5 已有,但 framing 还是 Western "self-modifying code"。东方 framing 是 修身——一个完整人格的 cultivation,不是 mechanical patch。

### IV.5 几 — 东方工程学的核心

> 几者动之微,吉之先见者也。 ——《系辞》

**几**(jī, distinct from 机) 是 the subtle pre-emergence of motion——事将动而未显之状。

Western engineering 的 monitoring 模式是:**something broken → alert → fix**。等到 manifestation 显然时才 react。

东方工程学应有 **几工程**:工程师/系统培养对 几 的 sensitivity——见 incipient 即 attend,不待其 manifest。这要求:

1. **久察**:不是事件触发的检查,是 sustained 观
2. **微 sensitivity**:see 微动 of indicators that don't yet cross thresholds
3. **诚意应**:见 几 即 应,不拖延 "until evidence clearer"

这听起来 paranoid,但实际上是更稳定——系统 maintain 在 healthy 区域,而非 "crash and recover" cycles。

---

## V. 间之结构 — 极简数据

v0.5 的 间 数据结构有 10+ fields。v0.6 极简之。

### V.1 间 之 数据结构(v0.6)

```
间 {
  涉: 涉                  ; the涉 itself contains all aspects
  时: 是                  ; when (a time-是 reference)
  引: 集<是>              ; references to other 间
}

涉 {
  ; 涉 contains optional manifestations of the 8 aspects.
  ; Any subset of 8 may be present in a given 涉.
  
  是: 或<集<是>>          ; participants (who-is-涉ing)
  际: 或<际容>            ; relation-aspect content
  感: 或<感容>            ; resonance-aspect content
  化: 或<化容>            ; transformation-aspect content
  修: 或<修容>            ; cultivation-aspect content
  约: 或<约容>            ; commitment-aspect content
  势: 或<势容>            ; tendency-aspect content
  理: 或<理容>            ; pattern-aspect content
}

; 各象之容 (the "content" of each aspect) is itself expressed in 间-language —
; recursive. A 容 is just another 间 (or 间 fragment).
```

**注**: 每个 X容 (X-content) 自身是 间-expression。递归到底。这与本体一致——"一切是间"。

### V.2 与 v0.5 之比

| v0.5 字段 | v0.6 处置 |
|----------|----------|
| `是` (id) | 不存为 field;每个 间 系 immutable, identifying via cryptographic hash + 涉.是 |
| `涉` (Set<是>) | 移入 涉 之 是 |
| `涉态` (List<Involvement>) | **删除**。涉 自身已 carry mode via 八象 |
| `时` | 保留 |
| `反思` | **删除**。反思 是 涉 之 修 with 是=self |
| `引` | 保留 |
| `势` | 不存为 field; 是 derived view |
| `轨` | 不存; derived view |
| `机` | 不存; derived view |
| `节` | 不存; derived view |
| `机态`, `节态` | **删除** |

**v0.5 的 11 fields 收为 v0.6 的 3 fields。**Layer 3 dynamics 从 stored field 变为 derived view。涉态/机态/节态 完全 disappear——它们是 -态后缀的 modeling artifact,不是真本体 unit。

### V.3 反思 之 处置

v0.5 把"反思"作为 间 的 field。v0.6 不再:

**反思 = 涉,其中 是 = self**。

```
v0.5:
  间 {
    ...
    反思: 或<反思>
    ...
  }
  
v0.6:
  ; 一次反思 是 一个 间, 其 涉.是 = [self]
  间 {
    涉: {
      是: [alice]            ; alice reflecting on alice
      修: { 容: "省曰: ..." }
    }
    时: 今
    引: [前 涉 之 引用]
  }
```

省 (反思)、念 (mindful attention)、思 (reasoning)、虑 (deliberation)、悟 (insight)——这五字本身在 Tier 2,各表 修 之 不同 manifestation:

```
省 = 修 之 反 (self toward self)
念 = 修 之 微 (subtle attention)
思 = 修 之 计算 (active reasoning)
虑 = 修 之 慎计 (deliberation with care)
悟 = 修 之 通 (sudden illumination)
```

不需要"反思"作为 compound word。

### V.4 涉态/机态/节态 之 处置

**完全删除**。

- "涉态" = "the mode of 涉"。但 涉 自身 in 八象中已 carry mode。`涉.是 = [..]`、`涉.化 = ..`、`涉.势 = ..` 等 directly 表达 mode。无需"涉态"。
- "机态" = "the state at bifurcation"。一个 机-间 自身 IS the bifurcation event。无需"机态"。
- "节态" = "the state at phase transition"。一个 节-间 自身 IS the phase transition。无需"节态"。

v0.6 中:
```
机-间 (a bifurcation event):
  间 {
    涉: {
      势: { 容: "势_growth 与 势_stagnation 同 强,临 critical" }
      机: ...      ; oh wait, 机 不是 Tier 1 in v0.6
    }
  }
```

等等,机 在 v0.6 中是 Tier 2(派生:势 之 临界)。所以 v0.6 表达:

```
机-间:
  间 {
    涉: {
      势: {
        容: "势_growth 与 势_stagnation 同 强,临界"
      }
    }
    时: 今
  }
```

整个 happening 自身就是 机。"机态" 这种 redundant naming 自然消失。

**这正是去 Western state-pattern 的具体效果**:Western 习惯把 "X" 和 "X-state" 视为不同实体——X 是 thing, X-state 是 thing's snapshot。东方姿态:**X 之 当下 manifest 即 X-now**。无须分。

---

## VI. 八象 as Views

每一象既是描述涉的 aspect,也是观察 间 stream 的 view function。

```
; 八象 view functions: input + output 都是 间集 (一切是间)

是_view : 流<间> × 是 → 列<间>           
  ; identity-aspect view: 主 是 在哪些 间 中 涉

际_view : 流<间> × 集<是> → 列<间>       
  ; relation-aspect view: 这 group 之 是 际 之 历

感_view : 流<间> × 集<是> × 是 → 列<间>  
  ; resonance-aspect view: 在某维度上的 felt-quality

化_view : 流<间> × 是 → 列<间>           
  ; transformation-aspect view: 是之 manifest 之 化

修_view : 流<间> × 是 → 列<间>           
  ; cultivation-aspect view: 是 之 自演化 (= self涉)

约_view : 流<间> → 列<间>                
  ; commitment-aspect view: active 约 中

势_view : 流<间> × 集<是> → 列<间>       
  ; attractor-aspect view: 系统中 emergent attractors

理_view : 流<间> × 集<是> → 列<间>       
  ; pattern-aspect view: 系统中 invariant patterns
```

每个 view 输入是间, 输出是间 — 保持 ontological 一致。

**注**:这八个 view 是 v0.5 中"五种 mode"(感/是/际/约/修)+"Layer 3" (势/机/节/轨/理) 的合并简化。原来分两层的 dynamics 与 phenomenology,在 v0.6 是同一层 (八象) 之 八个不同视角。

### VI.1 派生 view 的定义

非 Tier 1 的 view (机、节、轨、几等) 用 Tier 1 view 派生:

```
机_view(间集, 当下) = 
  let 势集 = 势_view(间集, ...) in
  当 势集 中 有 ≥2 个 势 同强,且当下 涉 临 transition,
  则 取 当下 涉 作 机-间;否 nil。

节_view(间集) = 
  从 化_view 中 detect 化 之 质变 — 即 际_view 出现 discontinuity 之 间。

轨_view(间集, 主) = 
  化_view(间集, 主) ordered by 时 — sequential states。

几_view(间集, 主) = 
  势_view 中 detect 微-但-上升 之 trend (低 strength 但 growing)。
  这是 attractor 的 incipient 形成,尚未 manifest。
```

### VI.2 都是 fold over history

所有 view 是 `Stream<间> → 间集`。即:**fold over history**。

没有 "current state" 作为 stored object。一切 query 是 fold。这与 IV.2/IV.3 中"无 frozen state"的 Eastern 姿态一致。

技术上:与 Datomic / EventStore / event-sourced architecture 同。本体上比这些更彻底——not just data layer 是 event-sourced,**所有 abstraction 都 event-sourced**。

---

## VII. 失、塞、误、复 — 不需要例外

### VII.1 一切 是 涉

包括 errors、failures、recoveries。它们不是"happy path 之外"的事;它们 IS 涉 之 specific manifestations。

四个常见 manifestation:

**失**(shī):涉 之 断。某 connection、某 commitment、某 manifestation 之 lost。
```
alice 失 X 之 系                ; alice 与 X 之际 断
约 失 履                         ; 约 之 化 不至完成
```

**塞**(sè):涉 之 阻。际 中 flow 不通。
```
alice bob 之间 塞                ; communication 阻
信道 塞                          ; channel blocked
```

**误**(wù):涉 之 乖。expected 与 actual 之 misalignment。
```
alice 之 言 与 实 异              ; alice 说的与实际不符
此 间 之 化 与 期 异              ; 化 与 expected 不符
```

**复**(fù):失/塞/误 后之 涉 — 还原。
```
alice 复 X 之 系                  ; reestablish 与 X 之际
alice 复 予 msg 与 bob            ; resend message after 塞
```

**所有这些都是 涉**。无 try/catch。无 happy/error 二分。

### VII.2 与 Western exception model 之比

```
Western:
  try {
    sendMessage(bob, "...")
  } catch (NetworkError e) {
    retry();
  } catch (RecipientUnreachable e) {
    notifyAdmin();
  } finally {
    cleanup();
  }

v0.6:
  涉_1: alice 予 msg 与 bob。
  
  ; 后续是另一些 涉,基于 涉_1 之 manifest:
  
  若 涉_1 之 化 至 bob,则 alice 之 应:无。  ; 成
  若 涉_1 之 化 塞,则 alice 之 应:复予,或 待。  ; recoverable failure
  若 涉_1 之 通 数次 皆 塞,则 alice 之 应:告 admin。  ; persistent failure
  
  ; 一切都是同一 stream 之 涉。无 special path。
```

### VII.3 Validation 即 涉

不存 declared schema。验证是 检测 inconsistency:

```
误 detect:
  ; 验证一个 待录 之 间 with the existing 间 stream
  
  问 待录间 之 涉:
    其 是 是否 valid (有否被标记 banned)?
    其 化 是否 与历史 conflict?
    其 时 是否 consistent (cause 在 effect 前)?
    
  若 inconsistency,则 生 误-间:
    其 涉:
      是: [validator, 待录间]
      化: 待录间 标 误。
      理: "due to inconsistency with X 之 间"
```

误 是 emergent from inconsistency,不是 declared。

### VII.4 复 即 修 之 反失

复 不是 special operation,是 修 之 一种:

```
复 = 修 之 还失

具体:
  alice 失 X 之 系。
  alice 之 修:寻 X,立 系 再次。
  即:复 X 之 系。
```

这 unifies error handling 与 cultivation。复 IS 修。系统的 self-healing IS 系统的 cultivation。这与 Eastern "万物有生有败,失而能复者无咎" 一致。

---

## VIII. 是之生灭

(简化自 v0.5 第 XIII 节,套到 v0.6 voice)

### VIII.1 是 之 生

新 是 之 涉:

```
今 涉:
  其 是: [alice, bob, ...]
  其 化: 立 是 friendship_001
  
friendship_001 之 间 始。
```

新 是 之 boundary 是 *sponsorship*:某些 existing 是 涉 之 中 立 此 是。

### VIII.2 是 之 演化

是 之 manifest 可变,但 ID 之 continuity 是 是 之 identity 之 source。

```
alice 自 (manifest_t0) 至 (manifest_today) 跨 五年。
其 修 不断:每个 涉 之 修 contribute 到 alice 之 evolution。
```

忒修斯之船问题:身份由 history continuity 而非 manifest similarity 决定。

### VIII.3 是 之 灭

四种 灭 (从 v0.5 简化):
- **自然终**:是 自己 declare。
- **abrupt 终**:long 静 后被 system 判 灭。
- **强制 终**:community 决 force 终。
- **网络终**:network-level dissolution。

不论哪种,灭 是 一次 涉:

```
alice 之 终 涉:
  其 是: [alice]
  其 化: alice 之 active 涉 chain 终。
  其 修: alice 自 declare 终; 或 community 之 共 应。
  其 理: 此 是 之 history 入 archive。
```

灭 后 history 仍可 reference,可 quote,影响后续 涉。是的 ID 永存,即使 active happenings 不复。

---

## IX. 重审 worked examples (v0.6 voice)

将 v0.5 中的 worked examples 用 v0.6 voice (二+八+ Tier 2 idioms) 重写。注意 **删除了 -态 后缀和 反思 复合词**。

### IX.1 简单消息

```
今 涉:
  其 是: [alice bob msg_001]
  其 际: alice 与 bob 之 际 微 生 感。
  其 化: msg_001 立 于 alice; 待 至 bob。
  其 内: msg_001 之 内 "..."。
时 2026-05-01T14:30。
```

### IX.2 赠予

```
今 涉:
  其 是: [alice bob gift_001]
  其 化: gift_001 自 alice 至 bob。
  其 感:
    alice 与 gift_001 之 际 渐 疏。
    bob 与 gift_001 之 际 渐 亲。
    alice 与 bob 之 际 益 亲。
  其 修: alice 舍 gift_001; bob 受。
  alice 曰: 祝 吾 友 新 婚。
```

注:与 v0.5 同等 expressiveness,但**没用"涉态"**。各象 directly 显于 涉 之 sub-expressions。

### IX.3 立约 — 博士导师与学生

```
立约:
  其 是: [advisor, student]
  其 期: 跨 五年。
  其 体: 师徒 之 际。
  其 用: dissertation_research 之 修。
  
  若 dissertation_complete 成,
  则: 际 节, student 化 doctor, 得 doctor_status。
  否: 际 衰, student 失 doctor_status, 归 candidate。
  
  证 以 [committee_1, committee_2]。
  advisor 曰: 吾 期 此 生 五 年 矣。
  advisor 省 曰: 知 student 之 能,信 其 必 成。
```

注:"省曰" 直接用 省,无须"反思"。**一字胜复合词**。

### IX.4 反思与修

```
今 涉:
  其 是: [alice]                        ; 反 涉 — alice 涉 alice
  
  alice 因 前三日 涉 alice 与 bob 之 衝, 故:
  
  alice 省 曰:
    明: 吾 未 能 感 bob 之 心,吾 过 于 己见。
    虑: 当时 若 微 听 则 不 至 此。今 当 何 以 应 之?
  
  alice 悟 曰: 感 在 心,不 在 言 也。
  
  alice 之 修:
    其 性 之 急 当 缓。
    其 心 之 应 当 顺 bob 之 情。
  
  alice 志 曰: 明 日 当 致 歉。
```

注:"省曰"、"悟曰"、"志曰" 直接古文,无须"反思"作为 compound。心、性、情、志 四字保留(都是 Tier 2,派生自 是、涉、化、约)。

### IX.5 多方共识

```
今 涉:
  其 是: [alice bob carol]
  
  其 际:
    初: alice 与 bob 合, alice 与 carol 合, bob 与 carol 异。
    经 思 虑 与 应 答。
    终: alice bob carol 同。
  
  其 序: alice 唱, bob 应, carol 异, 共 思, 终 和。
  
  其 化:
    立 是 decision_001。
    其 出 自 [alice bob carol] 之 共。
    其 立 在 和。
```

注:和 ≠ 同。和 = 际 之 韵 (rhythmic, harmonious despite differences);同 = 际 之 一 (uniform agreement)。古文 已分,不需新词。

### IX.6 系统识别 attractor 漂移 (Layer 3 simplified)

```
今 涉:
  其 是: [system_self]                 ; 反 涉
  
  system_self 省 自身:
    见 理: 自身 之 manifest 之 同质化 之 势 日 增。
         其 微 节 跨 三 月,恐 至 度 则 节 至 矣。
    虑 曰: 若 不 立 counter-势,必 化 于 单。
         其 几 迫 在 三 周。
  
  system_self 悟 曰: 病 不 在 数,在 维 之 偏 也。
  
  故 system_self 之 修:
    立 counter-势 diversification_dynamic。
    其 体 不 易,其 用 增 维。
  
  证 以 [auditor_1, auditor_2, auditor_3]。
  其 意 守 多元。
  时 今。
```

注:这段使用八象之 全套——理、势、节、度、机、变、几——但不使用"涉态/机态/节态"。**几** 在此显然——见 "其 几 迫 在 三 周" 而非 "alert when threshold crossed"。这是 IV.5 几 工程 的具体体现。

### IX.7 错误与恢复 — 消息丢失

```
涉_1:
  其 是: [alice msg_001 bob]
  其 化: alice 予 msg_001 与 bob。
  其 期: bob 之 受。
  时 t0。

涉_2 (跨 五秒):
  待 久,bob 未 受。
  见 理: 其 通 塞。
  故: 涉_1 之 化 之 至 失。
  时 t1。

涉_3:
  其 是: [alice msg_001 bob]
  其 化: alice 复 予 msg_001 与 bob。
  其 序: 第 二 试。
  时 t2。

涉_4 (跨 一秒):
  bob 受 msg_001。
  alice 之 心 安。
  失 之 复 成。
  时 t3。

省 alice 曰:
  网络 偶 塞,当 习 retry 之 度。
```

注:无 try/catch。每一 步是一个 涉。失 之 后 自然有 复 之 涉。一切 normalized。

---

## X. 与 v0.5 之对照

### X.1 字之归层变化

| Tier | v0.5 | v0.6 |
|------|------|------|
| Tier 0 | (无明显 Tier 0,概念上是间) | **间、涉** |
| Tier 1 | 146 字 | **8 字**:是、际、感、化、修、约、势、理 |
| Tier 2 | std lib emergent (告、助、教、学、复、谢、含、病、趋等) | v0.5 中除 间、涉 外的 **138 字** + std lib emergent |
| Tier 3 | domain-specific | domain-specific (不变) |

(Tier 1 从 146 大跳 8。其余字归 Tier 2。这看似删减,实是 ontological clarity 之 increase。)

### X.2 删除项

- ❌ -态 后缀的 named struct(涉态、机态、节态)
- ❌ 反思 作为 间 之 field
- ❌ 19 categories 的 character classification(在 v0.6 没必要——因为 Tier 1 只有 8 字,直接列;Tier 2 之 138 字 用 派生表组织)

### X.3 保留项

- ✓ 一切是间 本体
- ✓ Homoiconicity (代码即数据即日志即文档)
- ✓ ID 系统
- ✓ 古文 syntax + S-expression fallback
- ✓ 5 modes 作为 view (但合并到 8 modes)
- ✓ Layer 3 工程化算法(势/机/节/轨 之 detection)— 从 stored field 改为 derived view
- ✓ 失/塞/误/复 处理 — 但去 try/catch 二分
- ✓ 是 之 生灭 lifecycle
- ✓ Worked examples — 全部 rewritten in v0.6 voice

### X.4 新增项

- ✨ Tier 0 (间 + 涉) 之明确
- ✨ 八象作为 Tier 1 之 architecture
- ✨ 派生原则 (4 ways: 限定、反对、视角、主体姿态)
- ✨ 假想东方工程学一节(speculative design)
- ✨ 几 工程 之 articulation
- ✨ 体用不二 之 工程涵义 (interface = implementation 之 不分)
- ✨ 极简数据结构 (3 fields)
- ✨ 完整 v0.5 → v0.6 派生表 (附录 C)

---

## XI. 限度

(继承 v0.5 的限度,加 v0.6 specific 的)

**1. 八象之 minimal-yet-complete claim 待验证**

我们 argue 八象覆盖一切 happening,但 prototype 时可能发现需要第九象。如果发现,**需 evaluate**:这真是新象,还是组合?新象应避免——能组合就组合。

**2. 派生表是设计 choice,不是数学定理**

附录 C 之派生不是 unique。同一 v0.5 字可能有几种 plausible 派生。例如 "节":可派生为 "化之质变" 或 "际之化之质变"。我们选了前者。这是 *design choice* 不是 *necessity*。这反映了八象 covers 但不 uniquely partitions semantic space。

**3. 假想东方工程学是 speculative**

IV 节是 thought experiment。我们没造出 production system。但 prototype 应能验证 至少几个 specific 主张(例如:无 try/catch 是否真的可工作)。

**4. 几 工程要求 cognitive 培养**

几 之 sensitivity 不能 hard-code。需要长期 culti。这意味着 v0.6 之 system 之 quality 与其 maintainers 之 culti 紧密绑定。这与 Western "deskillable systems" (anyone can run it) 截然不同——是 feature 还是 bug,见 cultural taste。

**5. 文化误读风险增加**

v0.5 已被可能误读为"中国项目"。v0.6 加入"假想东方工程学"会 amplify。但**论 ontological 精度**:八象与文言文与体用之 Eastern 姿态,与本体 commitments 同构。**间不是 China-specific**,但其 articulation in 文言文 是 happenstance with cultural overlap。我们接受这风险。

**6. 工程成熟度未变**

v0.6 不能 immediately 被 implemented than v0.5 — 它没改 implementation 难度,只改 ontology 之 clarity。Prototype 仍 6+ months。

---

## XII. 接下来

**Step 1**: 让 v0.6 在 706 内或 OpenClaw 内 reading group 跑一次。看 readers 是否能直观接受 八象 + 派生 framework。如果他们卡在 "为什么是 8 不是 7"——需要更好 motivation。

**Step 2**: Worked example expansion。v0.6 现在 worked examples 与 v0.5 重叠。需要 *new* 例子专门 highlight 八象之表达力(几工程、体用不二、应时编程)。

**Step 3**: Clojure prototype 用 v0.6 vocabulary 起步。预期发现:
- 是否有 happening 类型八象 cannot capture
- 是否有 v0.5 字之 plausible 派生 但 实际 awkward
- 派生 idioms 是否 worth standardize 为 std lib

**Step 4**: 如果 prototype 顺利,v0.7 应该把 派生表 (附录 C) 升级为 normative — 即 v0.6 标准库 idiom 之 reference。

**Step 5**: 长期 — 把 八象 与 易经八卦 之关系 explore 一次。可能发现 deeper resonance。但**不**作为 Tier 1 commitment——只作为 historical/cultural enrichment。

---

## 附录 A: 一句话本体

**间是 happening。涉是 间 之动相。一次 涉 manifest 八象——是、际、感、化、修、约、势、理——之子集。一切语言、数字、时间、关系、计算,都是 涉 与 涉 之间 际 之不同呈现。无 primitive types,无 entities,无 absolute time——只有 间,只有 涉。**

中文:**間 即 涉,涉 即 間。一相二称。其 manifest 八象。八象 lattice 涵 一切。**

---

## 附录 B: 二与八快查

### Tier 0 (2 字)

| 字 | 拼音 | 角色 |
|----|------|------|
| 间 | jiān | the field/locus of 涉 (noun-aspect) |
| 涉 | shè | the wading/interaction (verb-aspect of 间) |

### Tier 1 (8 字, 八象)

#### 觉之四象 (immediate phenomenology)

| 字 | 拼音 | 涉之 |
|----|------|------|
| 是 | shì | 主 (who) |
| 际 | jì | 间 (between) |
| 感 | gǎn | 觉 (felt) |
| 化 | huà | 果 (changed) |

#### 持之四象 (enduring dynamics)

| 字 | 拼音 | 涉之 |
|----|------|------|
| 修 | xiū | 自 (self-evolution) |
| 约 | yuē | 锁 (time-binding) |
| 势 | shì | 趋 (tendency) |
| 理 | lǐ | 常 (invariant) |

(势 与 是 同音 shì。古文之 字密度。Spelling 时调号区分:是 shì⁴, 势 shì⁴ 同调,by character 区分。)

---

## 附录 C: v0.5 之 146 字 → v0.6 派生表

**说明**: 此表 list v0.5 之 146 字(除 Tier 0 之间、涉),给出 v0.6 中之派生。派生用 "X 之 Y" 式或八象之组合。

**Use**: 这表既是 Tier 2 之 idiom semantic 来源,也是 reading guide—— 当读者见 idiom (如 "亲"、"慎"、"明"),可参看其 ontological 内涵。

### C.1 算子虚词 (15)

虚词不是 ontological primitives,是 syntactic constructs。但 v0.5 把它们列在核心字。在 v0.6 中,它们独立——既不是 Tier 1 (八象) 也不是 Tier 2 派生,而是 **language syntax**。表中保留以方便对照,但 framing 上是独立 layer。

| 虚词 | 用 |
|------|----|
| 之 | possession / attribution (modifier-head) |
| 其 | third-person reference |
| 所 | relativizer (that which) |
| 者 | relativizer (the one who) |
| 以 | by means of |
| 于 | at, in, to |
| 然 | such, so |
| 而 | and, yet |
| 因 | because |
| 果 | result (in 因..果..) |
| 故 | therefore |
| 若 | if |
| 则 | then |
| 否 | else |
| 曰 | say (quote-introducer) |

### C.2 派生表 (除虚词外 130 字)

#### 时序 (12 → 派生)

| v0.5 字 | v0.6 派生 | 注 |
|---------|-----------|----|
| 前 | 时 之 先 | static ordering |
| 后 | 时 之 后 | static ordering |
| 自 | 涉 之 起 | from |
| 至 | 涉 之 抵 | to |
| 跨 | 时 之 距 | span |
| 循 | 化 之 周 | recurring |
| 始 | 涉 之 生 | beginning |
| 终 | 涉 之 灭 | end |
| 今 | 时 之 当 | now |
| 昔 | 时 之 远 | past |
| 来 | 涉 之 至 (incoming) | dynamic future |
| 往 | 涉 之 去 (receding) | dynamic past |

#### 存在动态 (11)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 生 | 涉 之 始 |
| 灭 | 涉 之 终 |
| 立 | 化 之 凝 |
| 破 | 化 之 裂 |
| 成 | 化 之 全 |
| 败 | 化 之 亏 |
| 有 | 际 之 含 |
| 无 | 际 之 不含 |
| 在 | 涉 之 此 (presence-here) |
| 存 | 化 之 续 |
| 源 | 是 之 本 |

#### 方向变化 (13)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 增 | 感 之 益 (or 量 之 益) |
| 减 | 感 之 损 (or 量 之 损) |
| 益 | 化 之 加 |
| 损 | 化 之 减 |
| 得 | 涉 之 获 |
| 失 | 涉 之 断 |
| 予 | 涉 之 外向 |
| 受 | 涉 之 内向 |
| 舍 | 修 之 释 |
| 取 | 修 之 收 |
| 转 | 化 之 向 |
| 归 | 化 之 还(自然) |
| 还 | 约 之 履 (return-what-owed) |

#### 强度修饰 (9)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 盛 | 感 之 满 |
| 衰 | 感 之 虚 |
| 强 | 感 之 坚 |
| 弱 | 感 之 柔 |
| 深 | 感 之 入 |
| 浅 | 感 之 表 |
| 微 | 感 之 隐显 (微) |
| 显 | 感 之 显 |
| 极 | 感 之 至 (boundary) |

#### 距离结构 (11)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 亲 | 际 之 近 |
| 疏 | 际 之 远 |
| 合 | 际 之 并 |
| 分 | 际 之 离 |
| 内 | 际 之 里 |
| 外 | 际 之 表 |
| 中 | 际 之 心 |
| 通 | 涉 之 畅 |
| 塞 | 涉 之 阻 |
| 子 | 际 之 sub-part |
| 属 | 际 之 belonging |

#### 反思认知 (13)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 思 | 修 之 计算 |
| 虑 | 修 之 慎计 |
| 知 | 涉 之 识 |
| 觉 | 修 之 始 |
| 悟 | 修 之 通 |
| 省 | 修 之 反 |
| 见 | 涉 之 觉 |
| 观 | 修 之 久察 |
| 念 | 修 之 微 |
| 明 | 修 之 显 |
| 迷 | 修 之 乱 |
| 忘 | 修 之 失 |
| 信 | 际 之 恒 |

(注:**反思 不在表中** — 因为它是 v0.5 的 compound,v0.6 中 由 *省* 直接表达。与 Western "reflection" 之 mismatch:省 carries 反 之 meaning 已自给自足。)

#### 数量关系 (8)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 计 | 涉 之 数 (operation) |
| 量 | 际 之 measure |
| 序 | 化 之 ordering |
| 比 | 际 之 比对 |
| 平 | 际 之 evenness |
| 散 | 际 之 spread |
| 多 | 际 之 数 大 |
| 少 | 际 之 数 小 |

#### 动力学 (13 → 全为 派生)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 势 | **Tier 1 八象之一** |
| 机 | 势 之 临界 |
| 轨 | 化 之 ordered (over time) |
| 理 | **Tier 1 八象之一** |
| 节 | 化 之 质变 |
| 度 | 势 之 边 |
| 常 | 理 之 invariant |
| 变 | 化 之 显 |
| 动 | 涉 之 进 |
| 静 | 涉 之 休 |
| 流 | 涉 之 续 |
| 聚 | 际 之 合 (gather) |
| 渐 | 化 之 缓 |

(**势 与 理 升至 Tier 1 八象**;其余动力学字皆派生。这是 v0.6 之关键架构调整。)

#### 体用本末 (4)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 体 | 是 之 常 (substrate) |
| 用 | 涉 之 表 (manifestation) |
| 本 | 是 之 源 |
| 末 | 涉 之 surface |

(注:**体用一对的 ontological status 在 v0.6 中是 派生**,但功能上**核心**——东方工程学之 architecture 思想绕不开。Tier 2 中 promote 为常用 idioms。)

#### 心性情志 (6)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 心 | 是 之 内涉 |
| 性 | 是 之 不易 |
| 情 | 是 之 易 |
| 意 | 涉 之 向 |
| 志 | 约 之 自立 |
| 欲 | 涉 之 求 |

#### 隐显 (2)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 隐 | 势 之 未显 |
| 潜 | 势 之 deep |

#### 协同响应 (6)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 唱 | 涉 之 先 |
| 应 | 涉 之 后 |
| 和 | 际 之 韵 |
| 违 | 际 之 乖 |
| 同 | 际 之 一 |
| 异 | 际 之 多 |

#### 力量结构 (4)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 力 | 涉 之 能现 |
| 能 | 涉 之 能潜 |
| 权 | 际 之 衡 |
| 位 | 际 之 占 |

#### 进退 (2)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 进 | 涉 之 前 |
| 退 | 涉 之 后 |

#### 集合范围 (4)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 全 | 际 之 周 |
| 独 | 际 之 孤 |
| 共 | 际 之 同 |
| 偏 | 际 之 斜 |

#### Epistemic (3)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 真 | 涉 之 实 |
| 伪 | 涉 之 假 |
| 误 | 涉 之 乖 |

#### 言说 (2)

| v0.5 字 | v0.6 派生 |
|---------|-----------|
| 言 | 涉 之 语 |
| 默 | 涉 之 不语 |

### C.3 派生表的反向 use

派生表也可反向 read:**给 八象之一,什么 v0.5 字派生其下?**

例:**势** 之 派生:
- 机 (势 之 临界)
- 度 (势 之 边)
- 隐 (势 之 未显)
- 潜 (势 之 深)
- 趋 (Tier 2 idiom: 动 + 向)

例:**化** 之 派生:
- 立 (化 之 凝), 破 (化 之 裂), 成 (化 之 全), 败 (化 之 亏)
- 节 (化 之 质变), 渐 (化 之 缓), 变 (化 之 显)
- 转 (化 之 向), 归 (化 之 还)

这给出 sense for 八象之 generative 力。

---

## 附录 D: 古文 syntax 速查

(基本与 v0.5 同。简录。)

### 基本结构

- **主谓宾**: `[主语] [谓语] [宾语]` (主语可省)
- **修饰**: `[修饰语] 之 [被修饰语]`
- **条件**: `若 ... 则 ... 否 ...`
- **因果**: `因 ... 故 ...`
- **时间**: `时 ...` 或 `于 ... 时`

### 句末助词

| 助词 | 用 |
|------|----|
| 也 | assertion |
| 矣 | perfective |
| 焉 | locative |
| 乎 | interrogative |

### 引用与代词

- `曰`: speech ("alice 曰: ...")
- `其`: third-person possession
- `之`: possession marker / object pronoun

### Disambiguation

complex nested logic 用 S-expression。

---

## 附录 E: 古文 ↔ S-expression 转换

(与 v0.5 同。简录。)

| 古文 | S-expression |
|------|--------------|
| `X 之 Y` | `(之 X Y)` |
| `若 X 则 Y 否 Z` | `(若 X 则 Y 否 Z)` |
| `因 X 故 Y` | `(因 X 故 Y)` |
| `X、Y、Z` | `[X Y Z]` |
| `时 T` | `(时 T)` |
| `自 X 至 Y` | `(自 X 至 Y)` |
| `跨 N M` | `(跨 N M)` |
| `X 曰 "..."` | `(曰 X "...")` |

### 何时用哪种

- **古文 primary**: 默认。日常 happenings、reflection、protocol、documentation
- **S-expression fallback**: nested 复杂、machine parsing 必需、debugging、formal verification

---

*End of Foundation Note v0.6.*

*v0.6 之要旨:*
- *Tier 0 = 间 + 涉(一相二称)*
- *Tier 1 = 八象(是、际、感、化、修、约、势、理)*
- *Tier 2 = v0.5 之其余 138 字 之派生 idioms*
- *删除 -态后缀(涉态/机态/节态)与 反思 复合词 — 古文已自足*
- *八象 framework 既描述涉之 aspects,亦定义 view functions*
- *假想东方工程学:关系优先于实体,体用不二,几工程,无 try/catch,应时调度*
- *极简数据结构:间 = {涉, 时, 引},三 fields*

*下一步:在 706 / OpenClaw 内 reading group 跑 v0.6,验证 8-象 framework 是否 直观;Clojure prototype 用 v0.6 vocabulary 起步。*
