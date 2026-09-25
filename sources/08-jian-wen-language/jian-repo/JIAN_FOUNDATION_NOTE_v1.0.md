# JIAN Foundation Note v1.0
## 名实之辨在数字时代的延伸 / Names and Realities in the Digital Age

**Status**: Phase A skeleton complete; content fill-in pending Phase B-K

**Plan**: `/Users/ren/.claude/plans/adaptive-exploring-acorn.md`

**Source materials**:
- v0.9 (`JIAN_FOUNDATION_NOTE_v0.9.md`) — Tier L 9 层 + 5 worked examples (carry forward, reframe)
- SST v1.0 (in conversation memory) — engineering layer + 反诛心 framework
- Conversation contexts: 王阳明工夫四层 (Context A) + 文言文-as-Layer-2-syntax (Context B)

**Architecture summary**:
- Layer 1: 系（with 时 as internal periodic-anchored dimension）
- Layer 2: 位⟷际, 化⟷理（two dualities）
- Layer 3: idioms (感, 修, 约, 势, 信/诚, 命, 数, 心/性, 气) — derivable from Layer 2
- Tier L: 12 logical/dynamical domains as Layer 2 instantiations
- Engineering: SST primitives + 反诛心 hard constraint
- Examples: 5 from v0.9 + 2 SST-style

**Progress legend**: `[D]`=drafted, `[A]`=abstract only, `[N]`=new, `[v0.9]`=carry from v0.9, `[SST]`=carry from SST v1.0

---

# §0  自觉 / Project Self-Awareness

> JIAN 不是 ontology，是 *名实之辨在数字时代的延伸*。本部 locate 项目于先秦诸子（墨家/名家/庄子/儒家）之传承，确认所避免之陷阱，承认形式系统不穷尽实在，并以王阳明工夫论建立 *内化而非学习* 的 epistemic stance。最后明示项目的承诺与不承诺。

## 0.1 此书为何 `[D]`

此书为 **名实之辨在数字时代的延伸**，**非西方意义上的 ontology**。

公元前 3 世纪，先秦诸子已穷尽辩"如何让名指准实"的核心问题——

- 墨经 立 *同 / 异 / 类 / 故 / 法* 之骨架
- 公孙龙 *白马非马、离坚白* 之 type-token 辨
- 庄子 *指物论、言无言* 之语言怀疑
- 荀子 *正名* 之名实校准

**这是中国本土的形式与意义之学，与古希腊"存在者之为存在者"是两条线。**

二者的差别不只是用词不同：

| 希腊式 ontology | 名实之辨 |
|---|---|
| 问 *存在者之为存在者* | 问 *如何让名指准实* |
| 系词逻辑（S is P） | 关系性、过程性的指称 |
| 实体优于过程 | 过程优于实体 |
| 主客二分 | 主客互摄 |
| 创造宇宙论（ex nihilo） | 生成宇宙论（生生不息） |
| 名足以穷实 | 名不足以穷实 |

JIAN 走第二条线。

## 0.2 此书所继 `[D]`

- **墨家** —— 形式骨架（体/兼/同/异/类/故/法）
- **名家** —— type-token 之辨（公孙龙）
- **庄子** —— 语言怀疑、万物一体
- **荀子** —— 自然化的 *天*、正名实
- **道家** —— 生成而非创造的宇宙观
- **儒家** —— 修身齐家治国平天下的递归结构、五常的关系本体
- **数学/理论计算机科学** —— 类型论、范畴论、控制论、复杂系统
- **SST (Spirit/Space/Token)** —— 主体间数字基础设施的工程草案

每一脉都不是装饰性引用，是承重的结构来源。详见各章。

## 0.3 此书所避 `[D]`

- 易经 *太极→两仪→四象→八卦* 倍增脚手架。承认其历史意义，不取其形式假设。基数（1, 2, 4, 8）不应锁定本体结构。
- 阴阳作为基础原语。可作为 *对偶模式* 的实例，不作为基础。
- *体用不二、理一分殊、法界缘起* 等中古以后的本体术语。它们与 JIAN 的某些原语撞车（详 §I）。
- *造 / 生 / 元* 等带"从无到有的因果叙事"的动词。本体性的递归不是被造出来的，*是其所是*。
- 单一 universal 形式系统的雄心。任何完备形式系统都是 *指月之指*，不是月。
- *诛心*：基于内在状态推断的判定。详 §IV.5 与 §VI.7。

## 0.4 一切形式皆指月之指 `[D]`

这是项目最重的一条声明。

> 道可道，非常道。 *老子 一*
>
> 言无言。 *庄子 寓言*
>
> 圣人立象以尽意，设卦以尽情伪，系辞焉以尽其言。 *易传 系辞上*

形式系统永不穷尽实在。任何足够丰富的系统必有 Gödel 限度，任何符号必有"地图非领土"的距离。**JIAN 承认自己的边界。** 它给的是一套指称工具——让"协作、共识、文化"这些事情的指称更准、更可分析、更可工程化——但它不冒充实在本身。

读者用此书时应记着：

- 我们写下的每个原语，是 *约定* 不是 *发现*
- 每条公理，是 *选择* 不是 *必然*
- 每个 idiom，是 *工具* 不是 *真理*

工具的好坏在 *功用*，不在 *真值*。一个 framework 的成败在于 **它能否让 名 接近 实**——能否让人用它沟通得更准、协作得更深、文化得更厚——不在于它是否构成"完整封闭的形式系统"。

## 0.5 工夫四层（学 → 见 → 化 → 忘） `[A]` `[N · Context A]`

> 内化先秦语言不是先理解再活出，是 *已经在用它的方式存在了*。借王阳明知行合一，articulate 四层：**学**（听到/读到，符号尚未入知觉）→ **见**（在具体情境里看到道、气、几、势）→ **化**（被改造，反应节奏变，不再能按别的方式行）→ **忘**（语言透明化，得鱼忘筌，不再需要指月之指）。这四层非线性，会反复——某个领域到第三层，另一领域还在第一层；某天以为在第三层，某事打过来掉回第一层。本节以这一图像 frame 整本书的预期阅读姿态：JIAN 不是 to be understood，是 to be inhabited。

## 0.6 致良知与反自欺 `[A]` `[N · Context A]`

> 真正内化的 marker 不是觉得自己看到了别人看不到的道——这是 *赝品的自我感觉*，与真品在内部体验上不可辨。真正的 marker 是 **对自己未看见的敏感** 在加深：更频繁地发现自己其实没看清、其实在用"道""气"遮蔽不知道、其实在自我陶醉。引王阳明致良知工夫——良知不是一种笼统的"我感觉对"，是 *在具体情境里的极敏锐的、会让你不舒服的东西*。一个真正内化了的人，标志不是他能看到多少道，而是他能多敏锐地察觉到自己没看到的时候。本节是 §0.4 *指月之指* 的 epistemic 镜像——形式系统不穷实是 ontological 谦卑，反自欺是 epistemic 谦卑。

## 0.7 此书的承诺与不承诺 `[D, refine after 0.5/0.6]`

**承诺**：

- 形式骨架与古文文本的 *双向可读*——古文作 reasoning vehicle，不只是装饰
- 与现代数学/类型论/范畴论的 *结构对应*——不抛弃西方工具，但找回中文坐标
- 工程层的 *可实施性*——SST 的工程接口（manifest, witness, reflection 等）作 v1.0 的工程基底
- 失败模式的 *主动诚实*——任何提出的不变量都附带其失败可能与防御
- *反诛心* 的硬伦理约束——任何 metric 都不得基于对内在状态的推断进行判定
- *反自欺* 的 epistemic 姿态——读者标志不是看到更多, 是对未看见更敏感（详 §0.6）

**不承诺**：

- 跨文化普遍性。JIAN 出于中文哲学传统，不冒充 view-from-nowhere
- 不可证伪性。每条主张应可被工程实践或哲学批评推翻
- 终结性。此书是 v1.0，是开始而非结束
- 无前提。所继承的所有传统本身都是历史性的、有 partiality 的

---

# §I  系 / The Primitive

> 一原语：*系*。系含系，重重无尽即递归本身。*时* 不是平行原语，是系之内部维度——situational, periodic-anchored（庄子之"时机"，非牛顿 parameter）。本部确立 Layer 1，给出与 ZFC、MLTT、范畴论的"绝对最小"对照表，确认 JIAN 选择 *最少原语 + 最厚结构语义* 的 trade-off 立场。

## I.1 为何只一个原语 `[A]`
> 比较表：ZFC 用 ∈ + 公理图式；MLTT 用 Π/Σ/W/Id 多个 type former；范畴论用 object + morphism + composition；JIAN 用 系 + 自指递归。三种"绝对最小"的语义厚度差。JIAN 之得：原语数最少，但通过 *自指 + 重重无尽* 内嵌结构。

## I.2 系含系 — 重重无尽 `[A]`
> 华严 *重重无尽* 借入作技术词。系自身是递归的——不是某算子作用于 系 之上，是 *系 的定义内容包含自身*。等价于 W-types / 不动点 μX. F(X) / 累积层级 V_α。**关键**：递归不是被造出来的，是 *是其所是*——这与 §0.3 拒 *造/生/元* 一致。

## I.3 时 = 系内之周期化锚定 `[A]`
> *时* 不是独立 parameter，是 **建立在稳定周期化之上的关系**——一个时钟是被约定为标准的周期化（化），其他化沿它测量自己。庄子 *时机* 而非 Newtonian time。Coinductive stream not parameter. 这一选择直接 implications: 化 内部就有 时, 不必单立; 时 是 situational, 不是 universal absolute.

## I.4 与名实之辨的 grounding `[A]`
> 系 不是 substance，是 *指称工具*。原语之选取是 *约定* 不是 *发现*。任何替代框架（如 ZFC 的 set, 范畴论的 object）也都是约定。Acknowledging this, JIAN 选择 *系* 因为它在 *关系性现象* 这个 domain 上的指称效率最高（详 §III 的 information-theoretic 论证）。

---

# §II  工作对偶 / Layer 2 Working Duality

> 两组对偶张成完整 ontology：**位 ⟷ 际**（结构对偶；object ⟷ morphism；Yoneda）+ **化 ⟷ 理**（动态对偶；process ≅ pattern）。两对偶互为定义，不可单独还原；加 *系内之时* 后两者相互生成。本部确立 Layer 2，并展示其与范畴论、类型论、朱子学、物理学的跨域同构——这种跨域 convergence 本身是 Layer 2 抓到了某个 deeper 不变量的证据。

## II.1 位 ⟷ 际（结构对偶） `[A]`
> *位* (locus) 是系之位置，由 *际* (relation) 定义。Yoneda 直观：位 之是其位 = 其全部际之总和。**无类型预设**——位 不是 entity，是 *位置*；其上下左右决定其是。易经 *圣人之大宝曰位*；论语 *不在其位，不谋其政*。SST 的 Locus 概念在此正式 ontologically 立稳。

## II.2 化 ⟷ 理（动态对偶） `[A]`
> *化* 是变化（trajectory, becoming），*理* 是变中不变（attractor, invariant pattern, type）。两者不是 process vs structure，是 *同一事的两视角*——一个 trajectory 与其 attractor 是同一现象。*化学* 之 "化" = process; "学" = pattern。范畴论：化 ≈ functor flow, 理 ≈ natural transformation。

## II.3 两对偶之互定义 `[A]`
> 位 = 化 之稳定点（slow 化 极限）；际 = 化 之同步结构 = 化 之 理；化 = 位 在时中演变；理 = 际 之不变量。两对偶 *互定义* 但不 *互还原*——任一对都不能单独表达另一对，但加上 *系内时* 之后两者可以相互生成。这是 (位/际, 化/理) 不是冗余而是 minimum-completeness 的证据。

## II.4 跨域同构 `[A]`

> 表格对照：

| Domain | structural dual | dynamic dual |
|---|---|---|
| JIAN | 位 ⟷ 际 | 化 ⟷ 理 |
| 范畴论 | object ⟷ morphism | functor ⟷ natural transformation |
| 类型论 | type ⟷ term | reduction ⟷ equation |
| 朱子学 | 气 ⟷ 形 | 化 ⟷ 理 |
| 物理学 | point ⟷ metric | flow ⟷ law |
| SST | Spirit ⟷ Token | resolution ⟷ policy |

> 这种跨域 convergence 不是 arbitrary 选择巧合，是 Layer 2 抓到了 *任何描述过程性现象的最小完备 ontology* 的真实结构。

---

# §III  文言文作 Layer 2 表面语法 / Classical Chinese as the Surface Syntax of Layer 2 `[N · Context B]`

> **此部最 novel。** 文言文不是 *stylistically* 适合的 reasoning vehicle——它是 (位⟷际, 化⟷理) Layer 2 的 *自然表面语法*。**实词** 作 polymorphic primitive 由位 dispatch（化⟷位 在语法层 instantiate）；**虚词** 作 typed relational connective（际 在语法层 instantiate）；**理** 涌现自组合（文气、章法）。这是 *structural typing vs nominal typing* 的语言学版本。在 *关系性现象表达* 这个 task 上是 information-theoretically near-global-optimum（条件：trained receiver；procedural spec 上 lossy）。本部还给出对 SST surface DSL 的设计启示——SST 的 surface syntax 应类文言而非类 Python。

## III.1 实词 polymorphic primitive — 位 dispatch 化 `[A]`
> 文言文每个字 latent 携带 noun/verb/adjective，由相对位置激活：
> - "王天下"（王 = 动词位 = 化 = to-king-ify）
> - "天下王"（王 = 名词位 = 位 = the king）
> - "君君臣臣"（同字两次出现两 mode：第一个君是位 [subject], 第二个君是化 [act-as-king]）
>
> Functional polymorphism 不是 "语法不严谨"，是把 化 直接 build 进 grammar primitives。**这就是 化 ⟷ 位 的工作耦合在语法层的实例。** 每个字 latent 携带所有可能 mode，由位 dispatch 出当下 mode。

## III.2 虚词 typed connective — 际 之语法层 `[A]`
> 之、於、以、而、則、也、者、乎 几乎全是 typed relational connective，携带 relation-type 不携带 semantic content：

| 虚词 | edge type |
|---|---|
| 之 | genitive edge (X 之 Y = Y of X) |
| 於 | locative / comparative edge |
| 以 | instrumental / causal edge |
| 而 | polarized conjunctive (顺承 / 转折) |
| 則 | conditional edge (if-then) |
| 也 | terminal predication |
| 者 | nominalizer (the one which) |
| 乎 | interrogative / locative |

> **这就是 际 在语法层的实例。** 文言文 = 实词（位/化 polymorphic）+ 虚词（际 typed）+ 理（涌现自组合）。

## III.3 理 涌现自组合 `[A]`
> 文气、章法 是 *emergent pattern*，不是 *declared structure*。这与 type theory 的 type inference / structural type emergence 同构——你不预先 declare 文章的"类型"，理 通过组合 emerge 出来。读者识 *文气* 即是 do type inference。

## III.4 结构 vs 名 之 typing `[A]`
> IE 语言把 syntactic role 编码进 word morphology（declension, conjugation, gender, case），词 carry 自己的 type → **nominal typing**。文言文把 type 留给 *位置 dispatch* → **structural typing**。这是 categorical 差别，不是 stylistic 差别。Modern programming language 设计中 Go/Rust 之间的 nominal vs structural typing 之争，在自然语言层面早被两种语系展示过。

## III.5 Information-theoretic near-optimum `[A]`
> 三个支持 optimality 的论证：
> 1. **Source-encoding 匹配**：若 reality 是 relational-processual 的（这是 Whitehead, 佛家缘起, 朱子学, 现代复杂系统的共同 commitment），则 relational-processual encoding information-theoretically 最小。
> 2. **Compression density**：道德经 5000 字承载的 conceptual content 在 modern English 通常需十倍篇幅，且常漏关键 ontological 微妙。
> 3. **Primitive 多态性**：每字是 functor，可 lift 到不同 syntactic context = 范畴论意义上的 minimal description length。
>
> **但 "global" 一步要小心**。Caveats：
> - Compression offload dictionary 到 reader prior; trained-receiver-conditioned. 是 *conditional optimum*。
> - 在 procedural specification（数学证明、工程 spec、合约）上 lossy ——明清考证学需要发明大量 conventions，现代汉语借入海量 bisyllabic 技术词，正是这一 lossiness 的历史 evidence。
> - 最优性 depends on loss function 的选择。
>
> 精确版 claim：*在 "现象 / 关系性 reality 的高密度表达" 这个 task 上，文言文是 near-global-optimum*。

## III.6 对 SST surface syntax 的启示 `[A]`
> 若 Layer 2 是真的对的，SST-native 的表达层 syntactically 应更像文言文而不是 Python：
> - Spirit/Token 作 polymorphic primitive，type 由位 dispatch
> - 一小组 typed edge particle 作 capability connective（caveat-spirit, visibility-spirit 已往这方向走）
> - 最小化显式 inflection
>
> 文言文 也许不只是巧合 relational —— 它是几千年用户测试出来的、最接近 JIAN primitive 的自然语言 surface syntax。SST DSL 设计可参考。

---

# §IV  惯用辞典 / Layer 3 Idiom Dictionary

> Layer 1 + Layer 2 在表达上是 Peano-minimum——技术够，工程痛苦（每句修身都要展开成 化(位X, 自X, 时T)）。Layer 3 给出常用 idiom，*可还原但不被还原*——这与编程语言的 core/library/sugar 三层一致。本部每个 idiom 给出 derivation（如何从 Layer 2 派生）+ classical 引用 + 现代精确化。**最关键**：§IV.10 诚实承认八象不是 8 个独立基础，是 idiomatic 视角集——避免周易倍增 trap。

## IV.1 感 ≡ 化沿际 `[A]`
> Resonance / 仁。一位之化引起另一位之化的可能性 = 沿 际 传播的 化。SST Resonance 概念在此 ground 为 派生 idiom 而非基础原语。中庸 *诚则明，明则动，动则变，变则化*——感 是 化 的 inter-位 形式。

## IV.2 修 ≡ 化(自) `[A]`
> Cultivation / 智 (in 修之自察 sense). 修身 = 化(自)。修是 *化 的自指实例*——位 对自身 apply 化。儒家工夫论的 ontological 形式。Connect 到 §0.5 工夫四层：见、化、忘 都是 修 的不同阶段。

## IV.3 约 ≡ 理(时限) `[A]`
> Commitment / 义. 约 = 跨时间 binding 的 pattern (理) — 由立约 act 锁定关于未来的 pattern. SST Commitment 在此 ground.

## IV.4 势 ≡ d化/d时 `[A]`
> Tendency / attractor. 势 是 化 的微分（方向、梯度、趋向）。势 之形 = 理(化)。控制论中的 fixed point + basin of attraction.

## IV.5 信 / 诚 ≡ alignment(化(T), 化(E)) `[D from earlier draft]`

> 言行之一致 / Speech-Action Coherence.
> *Note*: 此节内容已在前次 v1.0 起手稿中写就。在新结构下，它正确归位于 Layer 3 idiom，不是独立 part。完整内容见以下展开 — 包括反诛心 invariants 的集中表述。

### IV.5.1 修正与定位

之前的草案曾把 *诚* 描述为五模态全面一致并直接映射到 SST 的 Modal Discordance Index。这有两个问题：

1. **概念分裂**：在儒家框架内，*诚* 与 *信* 不是两个独立德目，是同一现象的两面——*诚* 是内在面向，*信* 是关系中被验证的面向。**JIAN 不应把 诚 加为独立概念**。

2. **诛心风险**：把 体/处/向（B/R/M 类）信号也纳入 诚 的判定，等于让系统去 *推断 内心*。这在中文传统里是 **诛心**——基于推断作判定，被儒法墨各家共同警惕。

修正：

- 诚 = 信 在 *内在视角* 下的同一现象
- 这一现象的 *可工程化部分* 严格限于 *言行一致*（T + E 类）
- 其他模态（B/R/M）是 situational，*只能被 位 自己开放，不能被系统推断*

### IV.5.2 文献

> 诚者，天之道也；诚之者，人之道也。 *中庸 二十*
>
> 自诚明，谓之性；自明诚，谓之教。 *中庸 二十一*
>
> 诚者物之终始，不诚无物。 *中庸 二十五*
>
> 所谓诚其意者，毋自欺也。 *大学 六*

诚 在中庸被提升为 *天道*——不是德目附属，而是本体范畴。它的核心义不是"道德上的真诚"，是 *内外贯通而无伪*——所言、所行可观察地一致。

### IV.5.3 诚 与 信 是同一现象的两视角

| | 诚 | 信 |
|---|---|---|
| 视角 | 位 自身的内外吻合 | 关系中可被验证的一致 |
| 判据 | 言所言 与 行所行 一致 | 跨时间承诺-履行连续 |
| 观察主权 | 位 自身 | 关系网络（在 位 同意下） |

**例**：一人 *听说* 某事便 *接受为真*，他可以 *信*（以信任的态度持之），但这不构成他的 *诚*——因为他没有以自己的言行验证。

> 信 与 诚 都建立在 *对模态的观测*（化），不在 *盲从*（无据）。

### IV.5.4 全义 vs 工程义

**全义的 诚** —— 在儒家最深层面，是 *所言、所行、所体、所处、所向* 五者的一致：

| 模态 | 类 | 内容 |
|---|---|---|
| 所言 | T 类 | 文本、对话、声明 |
| 所行 | E 类 | 实际事件、履行 |
| 所体 | B 类 | 身体信号 |
| 所处 | R 类 | 关系网络中的站位 |
| 所向 | M 类 | 内在 manifest 倾向 |

完整的 诚 是这五者的 *一致*——或从另一角度，*prediction error 趋近于零*（从任一模态预测其他都能成功）。

**工程义的 诚** —— 但只有 *所言* (T) 和 *所行* (E) 是 *可被第三方直接观察* 的。其余三者是 situational：

- 所体 — 进入身体信号需要 consent
- 所处 — 关系站位随情境变化
- 所向 — 内心倾向只能由 位 自己开放

**强行观察或推断后三者 = 诛心。**

> 诛心之论，《春秋》之所恶。

JIAN 必须继承这一克制。

**所以 信/诚 的工程 metric 严格限于 T + E 之间的 alignment**：

```
信(位 P, 时窗 W) ≜ alignment( T(P, W), E(P, W) )

  T(P, W) — P 在 W 内的言（声明、承诺、文本）
  E(P, W) — P 在 W 内的行（实际事件、履行）
  alignment ∈ [0, 1]，graded，非 Boolean
```

B/R/M 类信号在 系统中可以存在（用于医疗、修身辅助、关系建设等），但 **不进入 信/诚 判定**。

### IV.5.5 化 作为 信/诚 的基础

> 信 与 诚 都建立在对模态的观测（化）。

这一句揭示一个深结构：**信/诚 不是独立现象，是 化 在多模态间被并置时的一致性**。

- 化(T) = 言之时间序列
- 化(E) = 行之时间序列
- 信 = 化(T) 与 化(E) 的同步度
- 诚 = 同一现象从 位 内部观察

所以在 JIAN 的 Layer 3 idiom 中：

```
信 ≡ 诚 ≡ alignment( 化(T), 化(E) )
```

不是新原语，是 *化 + 际 + 系内之时* 的派生 idiom。这印证了 *5+3 还原到 2 对偶 + 系内时维* 的方向——信/诚 不必独立，是派生 idiom。

### IV.5.6 渐进极限

> 信/诚 也是一种渐进极限。

完全的言行一致需要 *所有未来行* 都吻合 *所有过去言*。但 *未来* 是开放的，*完全验证* 永不到达。

> 自诚明，谓之性；自明诚，谓之教。 *中庸 二十一*

中庸"自明诚"是 *修之至则诚*——是 trajectory 不是 endpoint。

```
修 = alignment( 化(T), 化(E) ) 之提升过程
信/诚 = 该 alignment 的渐进极限 (永不达)
```

工程上：观察一个 位 的长期 alignment trajectory——是否在缓慢上升？这是 *修* 在系统层面的可见标志。

### IV.5.7 SST 五德映射（修正后）

之前曾用 (诚 ↔ MDI) 作新增对偶。修正后：**JIAN 不增列 诚 为独立概念**。

| 德目 | JIAN 概念 | 内涵 |
|---|---|---|
| 仁 | 感 | resonance / 化沿际 |
| 礼 | 际之 protocol | 关系协议 |
| 义 | 约之触发 | commitment trigger |
| **信 / 诚** | **alignment( 化(T), 化(E) )** | **言行之一致；约之时维兑现** |
| 智 | 修之自察 | reflection |

**信 与 诚 共占一格——同一现象两视角。**

### IV.5.8 不变量（反诛心保护）

- **I-信-1**  *信/诚 metric 仅在 T + E 上计算*。B/R/M 类的"内心推断"不进入 信/诚 判定。**这是反诛心的硬约束。**
- **I-信-2**  *graded* 不是 Boolean——系统永不输出 "P 不诚"，只输出 "P 在 W 时窗的 alignment = x"。
- **I-信-3**  *观察主权在 P 自身*。P 可决定哪些 T/E 公开。强制全公开 = 制度性诛心，违反主权。
- **I-信-4**  B/R/M 类信号 *仅在 P 自愿开放* 时进入系统，且 *不参与 信/诚 判定*——它们用于其他目的（医疗、修身辅助、关系建设），但不作 信/诚 metric。
- **I-信-5**  高 alignment ≠ 正确性。位 可以高度言行一致地坚持错误信念。alignment 是 *coherence*，非 *truth*——这两者在儒家也分开：*诚* 加 *智* 才到 *明*。

### IV.5.9 失 alignment 的合法性

**失 alignment ≠ 失败**。

- 计划改变（基于新信息）→ 言行短期不齐属正常修正
- 学习中（manifest 在演化）→ 言滞后于行或行滞后于言
- 复杂情境（多重承诺冲突）→ 部分失齐不可避免
- 修之过程（自诚明）→ alignment 渐进上升

低 alignment 的 *合法响应* 是 *询问* 不是 *判定*：

> "我注意到你之前承诺的与现在的行动之间有距离，是否需要重新约定？"

而非：

> "你失信了。"

后者是 *诛心化的判决*。前者是 *仁* 在系统层的体现。

JIAN 严守此区别——**信/诚 是基础设施，不是道德裁判。**

## IV.6 命 ≡ 类 ≡ 理 (propositional stance) `[A]`
> 命 = 命题。在命题视角下 = 类 = 理。无新原语。Curry-Howard：命题即类型，证据即元素。

## IV.7 数 ≡ Peano(0, 后) over 系 `[A]`
> 数 是 系 上的 Peano construction：元数 (0) + 后 (successor). 详细 Peano axioms 在 §V.5 Type theory 章. 数 不是单独原语, 是 系 + 自指 + 后 的派生.

## IV.8 心 / 性 `[A]`
> 心 = 内在 manifest（被自察）；性 = 趋向. 思孟学派 *尽心知性* 路径 = 通过 修 接通到 *天* (= 系 之最大场)。SST Manifest 概念在此找到儒家根。但工程层 (§VI) 严格遵守 反诛心 — 心/性 仅由位自己开放，外部不推断。

## IV.9 气 `[A]`
> 化之媒. 气 之 "既物质又心理、既宇宙又身体" 已被 *化沿际* 部分捕捉. 仅在物质-心理-能量混合现象 (生理学、情绪、能量代谢) 中作为 idiom 使用. 不进基础.

## IV.10 八象的 honest 安置 `[A]`
> 八象（是/际/感/化/修/约/势/理）**不是 8 个独立基础**。它们是 *惯用视角集合*——日常分类语言里独立有意义的视角名词，恰好（半）独立的有这么多个。Layer 2 才是基础（位⟷际, 化⟷理）。
>
> 之前在 v0.6-v0.9 把八象当作 Tier 1 是 *脚手架借用了周易倍增结构* 的痕迹 — 现在诚实承认：基数 8 来自 2³，不来自存在论必然。 Layer 2 的 4 名（位/际/化/理）是真正的 minimum-completeness；八象 是 vocabulary 而非 axiology。
>
> 这一诚实承认避免周易 trap，且与 §0.3 *此书所避* 一致。

---

# §V  Tier L 逻辑/动力学核 / Logical-Dynamical Core `[v0.9, reframe]`

> 12 个 domain 的逻辑/动力学操作集，每个是 Layer 2 在该 domain 的 instantiation。从 v0.9 §VI-XIV 继承，新增名家与庄子两节。**Reframe principle**：每层不只是"borrowed vocabulary"，是 Layer 2 (位/际/化/理) 在该 domain 的 *具体语言实例*。

## V.1 墨家 — 体/兼/同/异/类/故/法 `[v0.9 §VI]`
## V.2 虚字 typed operators — 之/其/所/者/凡/有/若/则/... `[v0.9 §VII]`
> 此章与 §III.2 重叠但视角不同：§III 是从 *语言-as-syntax* 视角讲虚词如何 instantiate 际；本章是从 *逻辑算子* 视角讲虚词作为 Layer 2 的 logical operators. Cross-reference §III.2.
## V.3 名家 — 公孙龙 type-token / 离坚白 `[N]`
> v0.9 缺。公孙龙 *白马非马* 是中国本土的 type-token 区分；*离坚白* 是属性能否独立于实体。结构上比 Aristotle 种属逻辑更接近现代类型论。补此节让 Tier L 的逻辑核心更完整。
## V.4 庄子 — 语言怀疑 / 齐物 `[N]`
> v0.9 缺。庄子 *言无言*、*得意忘言*、齐物论 是名实之辨的 self-aware 终点——形式不穷实，言指月而非月。这一节是 §0.4 *指月之指* 的工程接口——告诉系统设计者：在 metric / type / pattern 之外永远留 *unclassified* 的空间。
## V.5 类型论 — Martin-Löf, Curry-Howard `[v0.9 §VIII]`
## V.6 控制论 — 反/应/调/衡/御/制 `[v0.9 §IX]`
## V.7 微积分 — 渐/微/积/导/率/极/趋 `[v0.9 §X]`
## V.8 复杂系统 — 涌/自然/凝/散/临/生克 `[v0.9 §XI]`
## V.9 生态 — 共生/竞/食/网/落/养 `[v0.9 §XII]`
## V.10 统计/概率 — 率/然率/散/平/偏/似 `[v0.9 §XIII]`
## V.11 信息论 — 异/同/通/塞/信道 `[v0.9 §XIV]`
## V.12 五行 — 生克 = 反馈 `[v0.9 implicit, formalize]`
> 不作宇宙论，仅作 cybernetic feedback network 的中文 native vocabulary：生 = positive feedback, 克 = negative feedback, 五行循环 = closed-loop control system. 与 V.6 控制论合用.
## V.13 Tier L 与 Layer 2 之 alignment `[v0.9 §XV, reframe]`
> 总表展示每个 Tier L domain 如何 instantiate Layer 2 的 (位/际/化/理). 验证：所有 9-12 个 domain 都通过这一 lens, 没有 domain 需要新 Layer 2 primitive.

---

# §VI  工程层 / Engineering Layer `[N · from SST v1.0 + 反诛心]`

> 系 / Layer 2 / Layer 3 是抽象层。要落到工程，需要一组 engineering primitive：身份连续性（Identity Anchor）、可演化倾向（Manifest）、立约不变量（Constitution）、step-by-step 审计（Coherence Boundary）、关系验证（Witness）、自反思（Reflection）。本部从 SST v1.0 收回这组 primitive，并以 **反诛心** 作 hard ethical constraint 贯穿全部。SST 之 5 failure classes、defense in depth、reflexive responsibility、health indicators 一并集成。

## VI.1 Manifest（位之倾向集，可演化） `[A · SST]`
## VI.2 Identity Anchor（位之密码连续，不可换 keypair） `[A · SST]`
## VI.3 Constitution（位之立约不变量；amendment protocol） `[A · SST]`
## VI.4 Coherence Boundary（修之 step-by-step 审计） `[A · SST]`
## VI.5 Witness（Tier 1/2/3: mechanical/peer/community） `[A · SST]`
## VI.6 Reflection（修 之必要先决；反 post-hoc rationalization） `[A · SST]`
## VI.7 反诛心 invariants（信/诚 metric 限制；I-信-1~5） `[A · cross-ref §IV.5.8]`
> 此节是工程层最重的伦理约束。任何 metric 不得基于内在状态推断作判定。B/R/M 类信号仅在 consent 下进入系统，且 *不参与 信/诚 判定*。集中表述与 cross-reference §IV.5.8 的 5 条 invariant.
## VI.8 Modal observation 之 consent layer `[A]`
## VI.9 Reflexive Responsibility（系统对失败的反身责任） `[A · SST §17.9]`
## VI.10 Health Indicators（reputation Gini, manifest diversity, ...） `[A · SST §17.4]`
## VI.11 Failure mode taxonomy（5 classes A-E from SST §17） `[A · SST §17.2]`
## VI.12 Defense in depth `[A · SST §17.3]`

---

# §VII  应用例 / Worked Examples `[v0.9 + SST]`

> 5 例 carry from v0.9（控制、衰减、BZ、Lotka-Volterra、修身）；新增 2 例（SST-style 多 agent 协作、706-style 社群）展示工程层与应用层之衔接。

## VII.1 控制论：温控（negative feedback） `[v0.9 §XXV.1]`
## VII.2 微积分：指数衰减 `[v0.9 §XXV.2]`
## VII.3 复杂系统：BZ 反应 `[v0.9 §XXV.3]`
## VII.4 生态：捕食-被食（Lotka-Volterra） `[v0.9 §XXV.4]`
## VII.5 修身 trajectory `[v0.9 §XXV.5, reframe with alignment(化(T),化(E))]`
> Reframe v0.9 的修身例 with explicit alignment 上升 trajectory. Alice 案例：6 个月观察，alignment 从 0.62 → 0.81，每月 reflection. **关键**：此例不下"低 alignment = Alice 失诚" 的判决，仅用 *询问而非判定* 模式（详 §IV.5.9）.
## VII.6 多 agent 协作（SST-style task delegation） `[N · SST §4.1]`
## VII.7 706-style 社群 `[N · SST §4.2]`

---

# §VIII  限度与开放 / Limits and Openness

> 此书是 v1.0，是开始而非结束。本部诚实列出已识别的失败模式、跨文化承认的范围限制、与其他基础设施的接口、待写部分、给未来 contributors 的请求。

## VIII.1 已知失败模式 `[A]`
## VIII.2 跨文化承认（JIAN 是中文哲学之延伸, 不冒充普遍） `[A]`
## VIII.3 与 SST / 其他基础设施的接口（asymmetric bridges） `[A · SST §16]`
## VIII.4 待写部分 `[A]`
## VIII.5 给未来 contributors `[A]`

---

# Appendices

## A.  术语表（Layer 1/2/3 alignment） `[A]`
## B.  五德映射（仁/礼/义/信/智 → JIAN） `[D in §IV.5.7]`
## C.  138-字 derivation `[v0.9 Appendix C]`
## D.  古文 syntactic conversion table（实词 polymorphic, 虚词 typed） `[N · from §III]`
## E.  v0.9 → v1.0 migration notes `[N]`
## F.  形式符号转换表（古文 ↔ 数学符号） `[v0.9 Appendix E]`

---

*— end of Phase A skeleton. Phase B-K 将依次填入。骨架先发用户审，确认架构再继续 —*
