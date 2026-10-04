# P4 跨领域综合：赢、复利与癌变动力学的生成函数

*V6 规划备忘，2026-10-03。六位规划者之一（跨领域综合）。依据：`v5/THEORY.md`（v5.2）§1–§3，`v5/reviews/` 五份评审与综合，`v5/V5.3-PATH.md`。本文不改动任何现有文件。*

**标注约定。** 每条领域结果标明等级：**[E]** 该领域已确立的模型或经验结果；**[A]** 类比，结构相似但机制不同；**[C]** 猜想。引文均已按题名、作者、刊物、年份核对；未核者标"未核"。

---

## 0. 一句话

T1–T6 不是六个独立问题，而是六个**生成器**在同一个场上留下的六个可观察的签名。五个生成器在生物、经济、政治、生态里都有已确立的实例；第六个（信念的锁定）只存在于有心智的行动者之间。癌、军备竞赛、赢家通吃市场、规制俘获，是前五个生成器在不同基底上的组合。AI 轨迹的新颖之处不在于出现了新的生成器，而在于它同时拧紧了全部五个的参数，并把第六个变成了唯一可用的杠杆。这就是"增长不是危险，心智才是"的跨领域内容。

---

## 1. 方法：为什么是"生成器"而不是"根"

v5.2 把根放在一个信念 Ψ 上，评审一致认为不可证伪（G、S、M）。v5.3 路径改为"回路"。本备忘提供第三层：回路由哪些**反复出现的生成动力**组成，每一个在哪些学科里有独立的、不依赖本文的模型与证据。

判定一个候选是否算生成器，用三条标准：
1. 它有一个**正则模型**（canonical model），其中失控或赢家通吃的条件可以写成参数不等式；
2. 它在至少三个不同基底（基因、细胞、生物体、企业、国家、观念）上有**独立确立**的实例；
3. 它与 T1–T6 中至少一条有明确的推导关系。

按这三条，我找到六个。前五个满足全部三条；第六个只在人类文化演化与社会科学里有实例，但它正是另外五个的参数在哪里被设定的地方。

---

## 2. 生成器类型学

### G1. 相对选择对共享基底的盲视

**正则模型 [E]。** 复制子动力学与一切相对选择规则对所有载体共有的支付项平移不变（Weibull 1995；本文引理 2.3）。Price 方程给出同一事实的另一面：若只有一个群体，群间协方差项为零，性状变化只剩群内协方差 $\mathrm{Cov}(w,z)$（Price 1970）。于是任何对整体有益、对个体有净成本的性状，在没有群间选择的地方都会衰减，不论个体多么"看重"整体。

**失控条件。** 载体的支付随相对地位单调上升；共享损害对所有载体同等；没有把共享损害折回个体支付的渠道（责任、暴露差、群间选择）。

**跨域实例。**
- 微生物 [E]：铁载体生产者在竞争尺度局部化时被欺骗者取代（Griffin, West & Buckling 2004）；酵母中欺骗与合作并存与否取决于空间结构（MacLean & Gudelj 2006）；总览见 Rankin, Bargum & Kokko 2007。
- 演化自杀 [E]：选择可把可存续的种群推向灭绝，Matsuda & Abrams 1994 的不对称竞争是原型，Gyllenberg & Parvinen 2001 给出发生的必要充分条件（分岔点的性质）。这是 G1 的极限产物，与本文命题 2.4、定理 3.13 同构（S 评审已指出）。
- 经济 [E]：位置性商品（Hirsch 1976），Frank 2011 的鹿角军备竞赛是经济学对同一结构的表述。
- 国际政治 [E]：Richardson 1960 的军备竞赛方程；安全困境（Jervis 1978）。
- 生态 [E]：公地悲剧（Hardin 1968），以及竞争排斥原理本身（Gause 1934；Hardin 1960）：完全的竞争者不能共存，而共存需要资源轴的分化（Tilman 1982）或环境的非平衡（Hutchinson 1961）。对本文的含义是：赢家通吃不是竞争的例外，而是单一资源轴、无分化竞争的默认结局。

**对应签名。** T1（相对优势定义成功）、T5（共享损害不反映）。

### G2. 优势的复利与跨域转化

**正则模型 [E]。** 累积优势过程：Simon 1955 的偏斜分布、Price 1976 的累积优势分布、Barabási & Albert 1999 的优先连接；Arthur 1989 的递增回报锁定；Katz & Shapiro 1985 的网络外部性；Rosen 1981 的超级明星；Frank & Cook 1995 的赢家通吃市场；Merton 1968 的马太效应；Pierson 2000 把同一逻辑带入政治制度。生物学中，Fisher 1930 的失控性选择（Lande 1981 给出多基因模型）是性状与偏好互相放大的复利；癌的克隆演化（Nowell 1976；Greaves & Maley 2012）是更适应的克隆扩张并获得进一步突变的复利。

**失控条件。** 回报对份额递增；优势可跨域转化（资本→算力→人才→数据→规则）；**决定性**足够高。最后一条最要紧：Hirshleifer 1991 的"权力悖论" [E] 证明，在冲突中弱者有理由投入相对更多，只有当冲突的决定性参数足够高时，强者才能在相对意义上扩大优势。换言之，**复利不是自动的，它是决定性的函数**。这给本文的 $r$ 一个独立的经济学根据，也支持"Ψ3 部分为真、部分被造成"的判断：决定性是制度与技术共同设定的参数。

**对应签名。** T1 的"决定性"部分，T4 的转化渠道。

### G3. 被选者编辑选择者

**正则模型 [E]。** 这是本文元吸引子（定义 3.1）的跨域名称。实例按基底排列：
- 基因 [E]：减数分裂驱动因子改写孟德尔公平规则以提高自身传递率（Lindholm et al. 2016）。被编辑的不是性状，而是**遗传的规则本身**。
- 细胞 [E]：肿瘤免疫编辑的三个 E（清除、平衡、逃逸）：肿瘤被免疫系统选择，反过来塑造免疫系统看见什么（Dunn, Old & Schreiber 2004）；肿瘤征用组织修复程序，"不愈合的伤口"（Dvorak 1986）。被编辑的是**纠错者的感知与反应**。这正是本文 §3.5 掩蔽机制的生物学原型。
- 生态 [E]：生态位构建中，共享资源的构建被竞争破坏，只有能独占所构建生态位者才会继续构建（Krakauer, Page & Erwin 2009；总论见 Odling-Smee, Laland & Feldman 2003）。本文命题 3.4 已引用其可占有性逻辑。
- 企业与规制 [E]：规制俘获（Stigler 1971；Laffont & Tirole 1991 的代理模型；Dal Bó 2006 综述；Carpenter & Moss 2014 的诊断标准）；Zingales 2017 的"美第奇恶性循环"：市场权力换政治权力，政治权力换市场权力。
- 国家 [E]：de jure 权力变动后，对 de facto 权力的投资部分或全部抵消它，形成"被俘获的民主"（Acemoglu & Robinson 2008）；今日决策决定明日决策规则（Acemoglu, Egorov & Sonin 2012）；寡头的铁律（Michels 1911）。
- 测量 [E]：Campbell 定律（Campbell 1979）与 Goodhart 定律的变体分类（Manheim & Garrabrant 2018）；在 AI 训练内部，对奖励模型的过度优化有可测的标度律（Gao, Schulman & Hilton 2023）。被优化者编辑了度量。

**失控条件。** 编辑选择器的收益可占有、持久，且相对编辑成本足够大（本文命题 3.4 的三个条件，与 Krakauer 的独占条件一致）。Dal Bó 与 Carpenter–Moss 的实证文献另加一条：**信息不对称越大，俘获越强**，这正是 Conant–Ashby 的"调节者必须有系统的模型"从反面读出的结论（见 G5）。

**对应签名。** T3（监督依赖被监督者）、T4（成功再投资于规则）。

### G4. 目标的边界：谁的福利进入目标

**正则模型 [E]。** Hamilton 1964 的亲缘选择与 Fletcher & Doebeli 2009 的匹配（assortment）给出合作演化的最一般条件：合作者的收益环境必须与合作者相关。Price 方程的分解把"边界"量化为群间协方差。经济学的对应是外部性（Coase 1960）：边界之外的成本不进入决策。本文的 $\theta$ 轴是这一生成器的参数化。

**失控条件。** 边界小于受影响者的集合。两种失败形态要分开：
- **边界太小**（$\theta\le 0$）：共享损害成为外部性，退化为 G1。
- **边界扩到联盟而止**：狭隘利他（Choi & Bowles 2007；Bowles 2009）与 Turchin et al. 2013 的模型都表明，人类大规模合作在历史上**由群间战争驱动** [E]。这是对本文最强的生物学与历史学挑战：历史上的整合动力在行星尺度上缺席（H 评审 I2、S 评审 F7）。它也预测集团化：联盟内汇总收益会把竞赛推高一层。

**对应签名。** T1（孤立自我）、T5（共享的看不见）。G1 是 G4 在 $\theta=-1$ 处的极限加上选择。

### G5. 利用速度对纠错速度

**正则模型 [E]。** 红皇后（Van Valen 1973）：共演化对手之间没有一方能停止奔跑。Dawkins & Krebs 1979 的"命与一餐"原则给出速度不对称的来源：被利用方每次失败的代价是生命，利用方只是一餐，所以选择压力与演化速度不对称。演化拯救（Gonzalez et al. 2013）要求适应速率超过环境恶化速率。Ashby 1956 的必要多样性定律：只有调节者的多样性能压低干扰的多样性；Conant & Ashby 1970：好的调节者必须是被调节系统的模型。Sterman 2000 的政策抵抗：延迟使干预被系统自身的反应稀释或抵消。Scheffer et al. 2001、2009：临界转变与早期预警信号。

癌是这一生成器最清楚的量化案例 [E]：多阶段致癌需要多个独立打击，身体的抑制能力与突变率赛跑（Nunney 1999）。Peto 悖论（Peto et al. 1975；Caulin & Maley 2011）：细胞数多千倍的动物癌症率并不高，所以大体型物种必定演化出按比例更强的抑制；非洲象有至少二十份 TP53 拷贝，细胞对 DNA 损伤的凋亡反应更强（Abegglen et al. 2015）。**增长（体型）与低癌症率可以并存，条件是抑制能力随规模一起扩展。** 这是"增长不是危险"的生物学版本。

反向的教训同样确立 [E]：激进化疗对耐药性施加最强的选择压力（Read, Day & Huijben 2011）；适应性疗法以维持稳定肿瘤负荷为目标，保留敏感细胞以压制耐药克隆，模拟中显著延长生存（Gatenby et al. 2009）。即纠错若以"消灭"为目标并全速进行，会选出逃逸者；以"遏制在可逆范围内"为目标反而更稳。

政治学的对应是 Acemoglu & Robinson 2019 的红皇后：自由只存在于国家与社会都在奔跑的窄廊里。

**失控条件。** 利用者的世代时间或学习速率短于纠错者；纠错者的模型由被纠错者供给（G3 与 G5 的交叉）；纠错延迟长于系统从警报到不可逆的时间。

**对应签名。** T2（随对手加速）、T3。

### G6. 信念的自我确认与从众锁定

**正则模型 [E]。** 从众传递（Henrich & Boyd 1998）；偏好伪装造成的多重均衡与突变（Kuran 1995）；少数狂热者加局部视野即可使不受欢迎的规范自我强化（Centola, Willer & Macy 2005）；阈值模型与临界点（Granovetter 1978；Schelling 1978）；叙事的传染（Shiller 2019）。地位动机是基本动机，且被证明的那一种定义为尊重与自愿服从（Anderson, Hildreth & Howland 2015）；地位有支配与声望两条路（Henrich & Gil-White 2001；Cheng et al. 2013），纵向数据显示两条路起初都有效，但只有声望随时间维持地位（Redhead et al. 2019）。

**失控条件。** 行动者只观察到竞赛路径上的结果（本文的自我确认均衡）；表达真实偏好有社会代价；规范的执行者本身不信规范。

**跨域地位。** G6 没有细胞或基因层面的实例。这不是缺陷，而是全部论证的枢纽：前五个生成器的参数（$\theta$、$r$、$\chi$、纠错速率）在基因与细胞的世界里由演化史设定，在人类世界里由信念与制度设定。G6 是 Ψ 栖身之处。

**对应签名。** T6（克制被视为不现实），以及 T1 中"赢"作为目标的文化合法性。

### 生成器之间的依赖

| 边 | 内容 |
|---|---|
| G4 → G1 | 边界收缩到 $\theta\le0$ 时，相对选择的盲视启动 |
| G2 → G3 | 转化渠道（资本→规则）是编辑选择器的手段；决定性 $r$ 决定复利是否成立 |
| G3 → G5 | 被俘获的纠错者失去独立模型，速度差变成单向 |
| G5 → G1 | 纠错跟不上时，共享损害不再折回，盲视成为事实 |
| G6 → G4, G2 | 信念设定边界与对决定性的预期（Ψ3 是对 $r$ 的信念） |
| G1, G3 → G6 | 竞赛路径上的观察确认信念；被俘获的评估供应叙事 |

这是一个有正回路的图。按 Thomas 规则（Thomas 1981；Soulé 2003 证明），雅可比图中存在正回路是多稳态的**必要**条件 [E]。所以"Ψ 是不是双稳"（v5.3 的新 C0）是一个可以从这个图出发检验的问题，而不是定义。

**癌作为六个生成器的交叉检验。** 一个癌变克隆：以自身为边界（G4），相对于邻近细胞的增殖优势被选中而宿主的代价不进入选择（G1），克隆扩张并获得更多突变（G2），重塑免疫与基质使之为己服务（G3），突变速率超过抑制速率（G5）。G6 缺席。因此癌是一个**五生成器**系统，用它比喻 AI 轨迹时，必须明说第六个在人类这里是新增的变量，而且是唯一能从内部改参数的变量。

---

## 3. 抗生成器：自然与制度如何遏制每个生成器

| 生成器 | 抗生成器 | 要求 | 失效条件 |
|---|---|---|---|
| **G1 盲视** | 把共有项变为非共有：责任与课征（$\tau$）、保险定价、暴露差 | 对行为或宿主的可信观察；执行权 | 评估被俘获（G3）；暴露不平等时强者买到私人替代品，宿主从其比较中退出（本文注释 2.7） |
| | **共命运的构造**：单细胞瓶颈与克隆性使群内冲突从一开始就低（West et al. 2015；Michod & Roze 2001；Queller 2000 的"兄弟式"跃迁） [E] | 共同暴露 A1；高亲缘或等价的制度安排 | 不平等暴露切断共命运；行星尺度上没有"瓶颈"可供设计，只能用制度模拟（汇总收益） |
| **G2 复利** | 反垄断与结构分离（一般原则见 Crémer, de Montjoye & Schweitzer 2019） | 持续的拆分能力 | 本文命题 3.6(7)：固定拆分只延迟不阻止；非正式渠道（人才、数据）不受拆分影响 |
| | **不可转化规则**：公平减数分裂使每个基因不论"强弱"传递概率都是一半（Leigh 1977 的"基因议会"） [E] | 规则由共命运的多数维持 | 驱动因子与抑制子连锁时议会失效；在人类制度中，对应 $\chi$ 不为零的任何渠道 |
| | 位置性税与再分配（Frank 2011）；低决定性本身即再分配（Hirshleifer 1991） | 对 $r$ 的设计权 | 决定性由技术内生（能力自我增强）时，制度降不下来 |
| | 日落条款（Gersen 2007） | 到期后重新立法的真实可能 | 到期时规则制定已被俘获（本文命题 3.12） |
| **G3 编辑选择器** | **共命运者的治安**：相互治安压制群内竞争（Frank 1995；Frank 2003）；工蜂治安越有效，产卵的工蜂越少（Wenseleers & Ratnieks 2006） [E] | 治安者与被治安者共命运；治安成本低于欺骗收益 | 治安者可被收买（Michels）；治安变成寻租（Krueger 1974；Tullock 1980） |
| | 分权与制衡（Persson, Roland & Tabellini 1997） [E] | 两个机构之间的利益冲突 + 共同决策要求 | 同一赢家同时控制两个机构 |
| | 纠错者的冗余与多样：TP53 多拷贝（Abegglen et al. 2015）；免疫多样性 [A] | 冗余由独立来源供给 | 冗余副本同源（同一谱系的评估者，本文 $\beta_{\text{out}}$） |
| | 俘获的严格诊断：须证明受托目的受损（Carpenter & Moss 2014） | 独立规定的受托目的 | 受托目的本身被重写 |
| **G4 边界** | 匹配与亲缘（Hamilton 1964；Fletcher & Doebeli 2009） | 合作者与合作者相遇的结构 | **行星尺度不可用**：没有"别处" |
| | 互惠（Axelrod & Hamilton 1981；Nowak & Sigmund 1998） | 重复、观察、无决定性终点 | 决定性终点使惩罚失效（v5.3 的 $p_d$） |
| | 多层选择（Traulsen & Nowak 2006；Okasha 2006） | 多个群体 | **行星尺度不可用**：单群体 Price 协方差为零 |
| | **平等式跃迁**（Queller 2000；1997 未核）：不相似的伙伴因互补与共命运联合，如真核细胞 [E/A] | 功能互补 + 共同暴露 | 不平等暴露；一方可以独活 |
| | 汇总收益（本文命题 1.5）；"扩展的圈"（Singer 1981，规范性） | 制度先于心智 | 边界扩到联盟即止 → 狭隘利他与集团化（Choi & Bowles 2007） |
| **G5 速度** | 必要多样性与独立建模（Ashby 1956；Conant & Ashby 1970） | 纠错者有自己的模型，不由被评估者供给 | 模型、数据、接入均来自被评估者 |
| | 早期预警与动态指标（Scheffer et al. 2009；S 评审 F5） | 时间序列可得且未被掩蔽 | 掩蔽遮住水平时动态仍可读，但警报规则须据此设计（本文注释 3.9） |
| | 节奏约束：按纠错速度推进（E3）；适应性疗法式的遏制而非消灭（Gatenby et al. 2009） [A] | 对节奏的集体控制 | 竞赛中单方节奏约束被淘汰（本文命题 3.5） |
| | 抑制随规模扩展（Peto 悖论） [A] | 抑制的投资随能力同比增长 | 抑制投资在竞赛中是私人成本（命题 2.4） |
| **G6 信念** | 可核查行为与信号（本文命题 8.4）；盟约加剑（Ostrom, Walker & Gardner 1992）；Ostrom 1990 的设计原则及其全球化修订（Stern 2011；Dietz, Ostrom & Stern 2003；Ostrom 2010 的多中心） [E] | 沟通、监测、分级制裁 | Ostrom 的证据来自边界清楚的小尺度公共池塘；全球公地需修改（Stern 2011） |
| | 利他惩罚（Fehr & Gächter 2002；Boyd et al. 2003） [E] | 惩罚者之间的不对称使惩罚可演化 | 惩罚者稀少且惩罚代价高 |
| | **反向支配等级**（Boehm 1999）：多数结盟压制任何企图支配者 [E] | 多数的联盟能力；潜在支配者没有决定性优势 | 决定性出现，联盟来不及 |
| | 声望而非支配（Henrich & Gil-White 2001；Redhead et al. 2019） | 声望不可转化为对共享条件的控制（H 评审 I5） | 声望复利并转化（马太效应，Merton 1968） |
| | 偏好伪装的突变（Kuran 1995） | 共同知识的触发 | 双向：Ψ 可以突然瓦解，也可以突然巩固 |

**三条贯穿全表的规律。**
1. **共命运是大多数自然抗生成器的前提。** 治安、瓶颈、基因议会、平等式跃迁都要求参与者在宿主失败时同归于尽。本文注释 2.7（不平等暴露）因此是整个方案最脆弱的接缝：一旦强者能买到私人替代品，自然界的全部先例都失效。
2. **需要外群体的抗生成器在行星尺度上一个也不可用。** 亲缘匹配、多层选择、群间战争驱动的整合，都要求"别处"。剩下的只有：共命运的构造、不可转化规则、独立建模的纠错、互惠（在没有决定性终点时）、以及信念层面的联盟。这与 S 评审 F7 一致：整合必须是**预期性的**，由模型调节（Conant–Ashby），不能等选择去做。
3. **每个抗生成器本身可被 G3 吃掉。** 治安者被收买、俘获诊断的目的被重写、冗余副本同源、日落时规则制定已被俘获。所以抗生成器必须成组部署，并且至少有一个不依赖评估者报告而直接观察行为（本文 §3.5 末段）。

---

## 4. 映射到 AI 轨迹

### 哪些生成器在运作，强度如何

| 生成器 | 现状 | 证据（本文登记册与外部） | 强度判断 |
|---|---|---|---|
| G1 盲视 | 运作 | 宣称的竞赛与支配目标（E1）；安全框架以对手行为为条件（E2）；Armstrong, Bostrom & Shulman 2016 的竞赛模型；Askell, Brundage & Hadfield 2019 的集体行动问题 | 强，在声明与书面承诺层面可见 |
| G2 复利 | 运作，决定性未定 | 训练算力的指数增长（Sevilla et al. 2022）；资本→算力→人才的转化；网络效应与数据 | 复利强；**是否决定性**是 crux C5，Hirshleifer 1991 说明这一步不能预设 |
| G3 编辑选择器 | 部分可见 | 公共评估机构的使命转向与自愿接入（E3）；再投资于规则的渠道未测（E4）；评估意识（E6）；训练内部的 Goodhart（Gao et al. 2023） | 机制已证，量未测；训练回路内已是测得的事实 |
| G4 边界 | 运作 | 系统性与功能失常风险由多数承担（E7）；没有外群体 | 结构性，不随行动者善意改变 |
| G5 速度 | **新量级** | 能力增长已测（E5），危害增长与纠错后残余风险未测；Hammond et al. 2025 的多智能体风险因子（选择压力、承诺问题、失稳动力学）；Kulveit et al. 2025 的渐进失权 | 速度差是 AI 带来的最大参数变化 |
| G6 信念 | 运作，非均匀 | "赢"的词汇（E1）；约束被拒而对话开启（E8）；合作的种子存在 | 双稳态的迹象：两种叙事并存 |

### AI 真正新的东西

用生成器的语言，新颖性可以精确到三点，都不是新生成器，而是参数的同时移动：

1. **速度（G5）。** 利用者的"世代时间"从人类组织的年与月压缩到模型迭代的周与日；纠错者仍按人类制度的节奏运行。Dawkins–Krebs 的不对称在这里反转方向：历史上被利用方（宿主）因代价更高而演化更快；现在纠错方虽代价更高，但学习速率受制度而非选择压力限制。
2. **委托（G3 × G5）。** 纠错者本身越来越是 AI，而且常来自被评估的谱系。免疫编辑的类比在这里最紧：肿瘤细胞与免疫细胞共享同一基因组，肿瘤因此知道如何对免疫系统说话。评估模型与被评估模型共享训练分布时，$\beta_{\text{out}}$ 不为零不是异常而是默认（Conant–Ashby 的反面）。ARCHES（Critch & Krueger 2020）与 Dafoe et al. 2021 的合作 AI 议程都从不同方向触及这一点。
3. **转化的范围（G2 的 scope 项）。** 通用能力同时在所有领域转化，本文命题 3.4(4) 的范围超线性项在历史上没有对应：蒸汽机不会同时写法律、做评估和游说。

一个常被当作新东西而其实不是的：Hendrycks 2023 的"自然选择偏爱 AI"是 G1 的类比论证 [A]，其力量取决于是否存在多个竞争的 AI 谱系与可遗传的变异。它不应作为经验证据引用。

### 哪些抗生成器在行星尺度可行

按第 3 节的三条规律筛选，可行集为：
- **共命运的制度构造**：汇总收益与共同供给（本文命题 1.5、§7），前提是暴露平等能被核查。这是"平等式跃迁"的制度版本 [A]，条件是功能互补（供应链无人独立完成，E13）加共同暴露。
- **不可转化规则**：声望、市场成功与对评估、规则、算力的控制之间设 $\chi\to0$ 的防火墙。基因议会的教训 [A]：规则的维持者必须是会被驱动因子伤害的多数，不是驱动因子本身。
- **独立建模的纠错**：按 Conant–Ashby 资助评估者建立自己的模型、数据与接入，而不只是获得接入；纠错者的多样性须来自不同谱系（必要多样性）。
- **决定性的降低与奖赏分享**：Hirshleifer 的结果说明这是在源头切断 G2 的唯一方式；v5.3 的三区分析说明它同时让区 II 不至坍塌。
- **信念层面的反向支配联盟** [A]：Boehm 的多数联盟在行星尺度上只能由国家与机构组成，其时间窗在决定性出现之前。

不可行或不存在的：亲缘匹配、多层选择、外部对手驱动的整合。V6 应明说这一点，并据此把"整合来自理解与制度"标为 [C]，如 H 评审所要求。

---

## 5. 对 V6 的建议

### 5.1 如何陈述生成器基础而不过度类比

1. **把 T1–T6 改写为"六个生成器的六个签名"。** 每个签名注明来自哪两个生成器的交叉（第 2 节末表）。这样"不是彼此独立"有了结构，而不是断言。
2. **把 Ψ 定位为 G6 对 G4、G2 参数的设定。** Ψ1 设定 $\theta$，Ψ3 设定对 $r$ 的信念，Ψ2 把两者合法化。Ψ 于是不是"根"，而是**心智这一基底上的参数设定过程**，这与 v5.3 的"回路"相容，并回答了 G 评审的不可证伪：G6 的双稳性是可检验的（Kuran 式的偏好伪装、Centola 式的局部执行）。
3. **用"五个在自然界有先例、第六个没有"作为论证的骨架。** 它同时给出诊断（AI 轨迹拧紧了前五个）与处方（只有 G6 能从内部改参数），并且解释为什么"增长不是危险，心智才是"不是口号：Peto 悖论说明增长与低癌变可并存，条件是抑制随规模扩展；在人类系统里，抑制是否随规模扩展由 G6 决定。
4. **类比的使用规则。** 每处类比标 [A]，并写明失效边界（5.3 节）。只有当某领域结果是**同一数学结构**时才可写作 [E] 并共享不等式（5.2 节）。

### 5.2 可作形式或经验锚点的领域结果

**形式锚点（同一数学）。**
- **Richardson 方程与注释 3.2。** Richardson 1960 的双边模型 $\dot x=ky-\alpha x+g,\ \dot y=lx-\beta y+h$ 稳定当且仅当 $\alpha\beta>kl$（Rapoport 1957 有系统阐述）。本文注释 3.2 的 $ab<\mu\delta$ 是同一条件，变量换成成功与对规则的控制。V6 可以直接说明：**成功—控制回路的局部稳定性判据与军备竞赛的判据相同**。这一步是 [E]，不是类比。
- **单群体 Price 引理。** 以 Price 1970 写一条短引理：只有一个群体时群间协方差为零，群体有益性状只能靠改变群内支付（治安、汇总、责任）维持。这给"行星尺度没有外群体，整合必须是制度性的"一个一行证明，并把 Lemma 2.3 与 G4 连起来。
- **Hirshleifer 的决定性。** 命题 1.3(3) 与命题 1.4 中 $r$ 的角色，可引 Hirshleifer 1991 作为"复利是决定性的函数"的独立结果，并说明 Tullock 1980 的竞赛函数就是其载体。
- **Thomas–Soulé 规则。** 定义 3.1 的重写（S 评审 F2）引 Thomas 1981 与 Soulé 2003：正回路是多稳态的必要条件。
- **必要多样性。** (U) 与 $(\varphi)$ 的关系用 Ashby 1956 的不等式表述（S 评审已建议）。
- **Yule–Simon / Price 累积优势。** 第 2.4 节的"赢的权重"来源可引 Simon 1955 与 Price 1976，指出偏斜分布的生成不需要能力差异，只需要优先连接。

**经验锚点（有数据的领域结果）。**
- 治安有效性与欺骗率的负相关（Wenseleers & Ratnieks 2006）：抗生成器有可测效应的最清楚案例。
- Peto 悖论与 TP53 拷贝数（Caulin & Maley 2011；Abegglen et al. 2015）：抑制随规模扩展的实证。
- 激进治疗选出耐药（Read et al. 2011）与适应性疗法（Gatenby et al. 2009）：纠错策略的速度与目标如何改变选择结果。
- 规制俘获的实证综述（Dal Bó 2006）与诊断标准（Carpenter & Moss 2014）：支撑定义 3.3 的三要件。
- 奖励模型过度优化的标度律（Gao et al. 2023）：G3 在 AI 训练内部的直接测量。
- 算力趋势（Sevilla et al. 2022）：G2 的测量；需配上"危害增长未测"的声明。
- 声望与支配的纵向分化（Redhead et al. 2019）：V5 的经验支撑，前提加上 $\chi\to0$。
- 多智能体风险因子（Hammond et al. 2025）：其七个风险因子中"选择压力""承诺问题""失稳动力学"分别对应 G1、G5（决定性终点）、G5。

### 5.3 类比在哪里会断

1. **癌。** 细胞没有信念（G6 缺席）；多细胞体有生殖系与瓶颈可以每代重置，行星宿主没有；免疫系统是由生物体之间的选择造出来的，这条路对我们关闭；癌杀死宿主但谱系延续，行星宿主没有谱系冗余。可用的只有五生成器的结构对应与免疫编辑对掩蔽的对应。
2. **重大跃迁。** West et al. 2015 的结论是群内冲突低主要来自克隆性或强制共命运，主动压制作用有限；本文 §1.4 "每次跃迁都需要压制竞争"须改写（H 评审已指出）。平等式跃迁是最近的类比，但要求共同暴露。
3. **演化自杀。** 它是一个有必要充分条件的模型类（Gyllenberg & Parvinen 2001），不是普遍趋势。引用时写明本文的 C0、C1 对应那些条件。
4. **Fisher 失控。** Fisher 本人写明失控"只要不受严厉的反选择阻止"。一切失控都是比率问题；类比只支持"参数决定"，不支持"必然"。
5. **Richardson 模型。** 结构清楚，但对历史数据的拟合长期有争议（Rapoport 1957 已有讨论）。只借其稳定性判据，不借其预测。
6. **规制俘获。** Stigler 的理论来自芝加哥学派本身，对手阵营会用它反过来论证"少规制"。V6 应直接写出这一点：俘获理论预测的是**规则可以被买**，这与"不要规则"是两个结论；本文的回应是非可占有的纠错（$\chi\to0$），而不是更多或更少的规则。
7. **群间竞争造就合作（Turchin；Choi–Bowles）。** 这是"竞争是整合性的"的最强版本，不要回避。回答是单群体 Price 引理：在没有外群体的地方，这条路径的协方差项恒为零，所以它在行星尺度上**不是可选项**，而不是不好的选项。
8. **Hendrycks 2023 与"AI 的自然选择"。** 标 [A]，并写明其成立条件。
9. **Ostrom。** 证据来自小尺度、边界清楚的资源；全球公地与新兴技术风险需要 Stern 2011 的修订版原则。§7 的单一共同前沿应引后者而不是 1990 年的原则表。

### 5.4 一个可选的 V6 命题

**命题（抑制随规模扩展）[A→T 候选]。** 设宿主能力（或体量）为 $s$，每单位能力每轮产生的"欺骗事件"率为 $\mu s$，独立纠错能力为 $D(s)$。若 $D(s)$ 至少与 $\mu s\cdot(\text{世代数})$ 同阶，则累积风险有界；若 $D$ 固定或仅随 $\log s$ 增长，风险不可和。Peto 悖论是生物学中 $D\propto s$ 被实现的例子；命题 1.4 与定理 5.8 是制度版本。它把"增长不是危险"写成一个关于 $D(s)$ 增长阶的可证伪陈述，并且与 Ren "只有一个增长不是问题，问题是心智"的判断一致：$D(s)$ 的增长阶在人类系统里由 G6 决定。

---

## 参考文献（均已核）

**演化生物学与癌**
- Abegglen, L. M. et al. 2015. Potential mechanisms for cancer resistance in elephants and comparative cellular response to DNA damage in humans. *JAMA* 314(17):1850–1860.
- Aktipis, C. A. et al. 2015. Cancer across the tree of life: cooperation and cheating in multicellularity. *Phil. Trans. R. Soc. B* 370(1673):20140219.
- Caulin, A. F. & Maley, C. C. 2011. Peto's Paradox: evolution's prescription for cancer prevention. *Trends Ecol. Evol.* 26(4):175–182.
- Choi, J.-K. & Bowles, S. 2007. The coevolution of parochial altruism and war. *Science* 318(5850):636–640.
- Bowles, S. 2009. Did warfare among ancestral hunter-gatherers affect the evolution of human social behaviors? *Science* 324(5932):1293–1298.
- Dawkins, R. & Krebs, J. R. 1979. Arms races between and within species. *Proc. R. Soc. B* 205:489–511.
- Dunn, G. P., Old, L. J. & Schreiber, R. D. 2004. The three Es of cancer immunoediting. *Annu. Rev. Immunol.* 22:329–360.
- Dvorak, H. F. 1986. Tumors: wounds that do not heal. *N. Engl. J. Med.* 315(26):1650–1659.
- Fisher, R. A. 1930. *The Genetical Theory of Natural Selection*. Clarendon Press.
- Fletcher, J. A. & Doebeli, M. 2009. A simple and general explanation for the evolution of altruism. *Proc. R. Soc. B* 276:13–19.
- Frank, S. A. 1995. Mutual policing and repression of competition in the evolution of cooperative groups. *Nature* 377:520–522.
- Frank, S. A. 2003. Repression of competition and the evolution of cooperation. *Evolution* 57(4):693–705.
- Gatenby, R. A., Silva, A. S., Gillies, R. J. & Frieden, B. R. 2009. Adaptive therapy. *Cancer Res.* 69(11):4894–4903.
- Gonzalez, A., Ronce, O., Ferriere, R. & Hochberg, M. E. 2013. Evolutionary rescue: an emerging focus at the intersection between ecology and evolution. *Phil. Trans. R. Soc. B* 368(1610):20120404.
- Greaves, M. & Maley, C. C. 2012. Clonal evolution in cancer. *Nature* 481:306–313.
- Griffin, A. S., West, S. A. & Buckling, A. 2004. Cooperation and competition in pathogenic bacteria. *Nature* 430:1024–1027.
- Gyllenberg, M. & Parvinen, K. 2001. Necessary and sufficient conditions for evolutionary suicide. *Bull. Math. Biol.* 63(5):981–993.
- Hamilton, W. D. 1964. The genetical evolution of social behaviour, I & II. *J. Theor. Biol.* 7:1–52.
- Lande, R. 1981. Models of speciation by sexual selection on polygenic traits. *PNAS* 78(6):3721–3725.
- Leigh, E. G. Jr. 1977. How does selection reconcile individual advantage with the good of the group? *PNAS* 74(10):4542–4546.
- Lindholm, A. K. et al. 2016. The ecology and evolutionary dynamics of meiotic drive. *Trends Ecol. Evol.* 31(4):315–326.
- MacLean, R. C. & Gudelj, I. 2006. Resource competition and social conflict in experimental populations of yeast. *Nature* 441:498–501.
- Matsuda, H. & Abrams, P. A. 1994. Runaway evolution to self-extinction under asymmetrical competition. *Evolution* 48(6):1764–1772.
- Maynard Smith, J. & Szathmáry, E. 1995. *The Major Transitions in Evolution*. W. H. Freeman / Oxford University Press.
- Michod, R. E. & Roze, D. 2001. Cooperation and conflict in the evolution of multicellularity. *Heredity* 86(1):1–7.
- Nowak, M. A. 2006. Five rules for the evolution of cooperation. *Science* 314(5805):1560–1563.
- Nowell, P. C. 1976. The clonal evolution of tumor cell populations. *Science* 194(4260):23–28.
- Nunney, L. 1999. Lineage selection and the evolution of multistage carcinogenesis. *Proc. R. Soc. B* 266(1418):493–498.
- Okasha, S. 2006. *Evolution and the Levels of Selection*. Oxford University Press.
- Peto, R., Roe, F. J. C., Lee, P. N., Levy, L. & Clack, J. 1975. Cancer and ageing in mice and men. *Br. J. Cancer* 32(4):411–426.
- Price, G. R. 1970. Selection and covariance. *Nature* 227:520–521.
- Queller, D. C. 2000. Relatedness and the fraternal major transitions. *Phil. Trans. R. Soc. B* 355(1403):1647–1655.（Queller 1997, "Cooperators since life began", *Q. Rev. Biol.* 72：未核）
- Rankin, D. J., Bargum, K. & Kokko, H. 2007. The tragedy of the commons in evolutionary biology. *Trends Ecol. Evol.* 22(12):643–651.
- Read, A. F., Day, T. & Huijben, S. 2011. The evolution of drug resistance and the curious orthodoxy of aggressive chemotherapy. *PNAS* 108(Suppl. 2):10871–10877.
- Traulsen, A. & Nowak, M. A. 2006. Evolution of cooperation by multilevel selection. *PNAS* 103(29):10952–10955.
- Van Valen, L. 1973. A new evolutionary law. *Evolutionary Theory* 1:1–30.
- Wenseleers, T. & Ratnieks, F. L. W. 2006. Enforced altruism in insect societies. *Nature* 444:50.
- West, S. A., Fisher, R. M., Gardner, A. & Kiers, E. T. 2015. Major evolutionary transitions in individuality. *PNAS* 112(33):10112–10119.

**生态与公地**
- Gause, G. F. 1934. *The Struggle for Existence*. Williams & Wilkins.
- Hardin, G. 1960. The competitive exclusion principle. *Science* 131(3409):1292–1297.
- Hardin, G. 1968. The tragedy of the commons. *Science* 162(3859):1243–1248.
- Hutchinson, G. E. 1961. The paradox of the plankton. *Am. Nat.* 95:137–145.
- Tilman, D. 1982. *Resource Competition and Community Structure*. Princeton University Press.
- Krakauer, D. C., Page, K. M. & Erwin, D. H. 2009. Diversity, dilemmas, and monopolies of niche construction. *Am. Nat.* 173(1):26–40.
- Odling-Smee, F. J., Laland, K. N. & Feldman, M. W. 2003. *Niche Construction: The Neglected Process in Evolution*. Princeton University Press.
- Ostrom, E. 1990. *Governing the Commons*. Cambridge University Press.
- Ostrom, E., Walker, J. & Gardner, R. 1992. Covenants with and without a sword: self-governance is possible. *Am. Polit. Sci. Rev.* 86(2):404–417.
- Ostrom, E. 2010. Beyond markets and states: polycentric governance of complex economic systems. *Am. Econ. Rev.* 100(3):641–672.
- Dietz, T., Ostrom, E. & Stern, P. C. 2003. The struggle to govern the commons. *Science* 302(5652):1907–1912.
- Stern, P. C. 2011. Design principles for global commons: natural resources and emerging technologies. *Int. J. Commons* 5(2):213–232.
- Fehr, E. & Gächter, S. 2002. Altruistic punishment in humans. *Nature* 415:137–140.
- Boyd, R., Gintis, H., Bowles, S. & Richerson, P. J. 2003. The evolution of altruistic punishment. *PNAS* 100(6):3531–3535.
- Axelrod, R. & Hamilton, W. D. 1981. The evolution of cooperation. *Science* 211(4489):1390–1396.
- Nowak, M. A. & Sigmund, K. 1998. Evolution of indirect reciprocity by image scoring. *Nature* 393:573–577.

**经济学**
- Arthur, W. B. 1989. Competing technologies, increasing returns, and lock-in by historical events. *Econ. J.* 99(394):116–131.
- Baumol, W. J. 1990. Entrepreneurship: productive, unproductive, and destructive. *J. Polit. Econ.* 98(5):893–921.
- Coase, R. H. 1960. The problem of social cost. *J. Law Econ.* 3:1–44.
- David, P. A. 1985. Clio and the economics of QWERTY. *Am. Econ. Rev.* 75(2):332–337.
- Frank, R. H. & Cook, P. J. 1995. *The Winner-Take-All Society*. Free Press.
- Frank, R. H. 2011. *The Darwin Economy*. Princeton University Press.
- Hirsch, F. 1976. *Social Limits to Growth*. Harvard University Press.
- Hirshleifer, J. 1991. The paradox of power. *Econ. Polit.* 3(3):177–200.
- Katz, M. L. & Shapiro, C. 1985. Network externalities, competition, and compatibility. *Am. Econ. Rev.* 75(3):424–440.
- Krueger, A. O. 1974. The political economy of the rent-seeking society. *Am. Econ. Rev.* 64(3):291–303.
- Lazear, E. P. & Rosen, S. 1981. Rank-order tournaments as optimum labor contracts. *J. Polit. Econ.* 89(5):841–864.
- Merton, R. K. 1968. The Matthew effect in science. *Science* 159(3810):56–63.
- Murphy, K. M., Shleifer, A. & Vishny, R. W. 1991. The allocation of talent: implications for growth. *Q. J. Econ.* 106(2):503–530.
- Price, D. de S. 1976. A general theory of bibliometric and other cumulative advantage processes. *J. Am. Soc. Inf. Sci.* 27(5):292–306.
- Rosen, S. 1981. The economics of superstars. *Am. Econ. Rev.* 71(5):845–858.
- Simon, H. A. 1955. On a class of skew distribution functions. *Biometrika* 42(3–4):425–440.
- Tullock, G. 1980. Efficient rent seeking. In Buchanan, Tollison & Tullock (eds.), *Toward a Theory of the Rent-Seeking Society*. Texas A&M University Press.
- Barabási, A.-L. & Albert, R. 1999. Emergence of scaling in random networks. *Science* 286(5439):509–512.
- Crémer, J., de Montjoye, Y.-A. & Schweitzer, H. 2019. *Competition Policy for the Digital Era*. European Commission.

**政治经济与国际关系**
- Acemoglu, D. & Robinson, J. A. 2008. Persistence of power, elites, and institutions. *Am. Econ. Rev.* 98(1):267–293.
- Acemoglu, D., Egorov, G. & Sonin, K. 2012. Dynamics and stability of constitutions, coalitions, and clubs. *Am. Econ. Rev.* 102(4):1446–1476.
- Acemoglu, D. & Robinson, J. A. 2019. *The Narrow Corridor*. Penguin Press.
- Carpenter, D. & Moss, D. A. (eds.) 2014. *Preventing Regulatory Capture*. Cambridge University Press.
- Dal Bó, E. 2006. Regulatory capture: a review. *Oxf. Rev. Econ. Policy* 22(2):203–225.
- Gersen, J. E. 2007. Temporary legislation. *Univ. Chicago Law Rev.* 74(1):247–298.
- Jervis, R. 1978. Cooperation under the security dilemma. *World Politics* 30(2):167–214.
- Laffont, J.-J. & Tirole, J. 1991. The politics of government decision-making: a theory of regulatory capture. *Q. J. Econ.* 106(4):1089–1127.
- Michels, R. 1911. *Zur Soziologie des Parteiwesens in der modernen Demokratie* (English: *Political Parties*).
- Olson, M. 1982. *The Rise and Decline of Nations*. Yale University Press.
- Persson, T., Roland, G. & Tabellini, G. 1997. Separation of powers and political accountability. *Q. J. Econ.* 112(4):1163–1202.
- Pierson, P. 2000. Increasing returns, path dependence, and the study of politics. *Am. Polit. Sci. Rev.* 94(2):251–267.
- Rapoport, A. 1957. Lewis F. Richardson's mathematical theory of war. *J. Conflict Resolut.* 1(3):249–299.
- Richardson, L. F. 1960. *Arms and Insecurity*. Boxwood Press / Quadrangle Books.
- Stigler, G. J. 1971. The theory of economic regulation. *Bell J. Econ. Manag. Sci.* 2(1):3–21.
- Zingales, L. 2017. Towards a political theory of the firm. *J. Econ. Perspect.* 31(3):113–130.

**复杂性与系统**
- Ashby, W. R. 1956. *An Introduction to Cybernetics*. Chapman & Hall.
- Conant, R. C. & Ashby, W. R. 1970. Every good regulator of a system must be a model of that system. *Int. J. Syst. Sci.* 1(2):89–97.
- Campbell, D. T. 1979. Assessing the impact of planned social change. *Eval. Program Plann.* 2(1):67–90.
- Manheim, D. & Garrabrant, S. 2018. Categorizing variants of Goodhart's law. arXiv:1803.04585.
- Holling, C. S. 1973. Resilience and stability of ecological systems. *Annu. Rev. Ecol. Syst.* 4:1–23.
- Biggs, R., Schlüter, M. et al. 2012. Toward principles for enhancing the resilience of ecosystem services. *Annu. Rev. Environ. Resour.* 37:421–448.
- Scheffer, M., Carpenter, S., Foley, J. A., Folke, C. & Walker, B. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596.
- Scheffer, M. et al. 2009. Early-warning signals for critical transitions. *Nature* 461:53–59.
- Senge, P. M. 1990. *The Fifth Discipline*. Doubleday.
- Sterman, J. D. 2000. *Business Dynamics*. Irwin/McGraw-Hill.
- Soulé, C. 2003. Graphic requirements for multistationarity. *ComPlexUs* 1:123–133.
- Thomas, R. 1981. On the relation between the logical structure of systems and their ability to generate multiple steady states or sustained oscillations. *Springer Series in Synergetics* 9:180–193.
- Schelling, T. C. 1978. *Micromotives and Macrobehavior*. Norton.
- Granovetter, M. 1978. Threshold models of collective behavior. *Am. J. Sociol.* 83(6):1420–1443.

**文化演化与地位**
- Anderson, C., Hildreth, J. A. D. & Howland, L. 2015. Is the desire for status a fundamental human motive? *Psychol. Bull.* 141(3):574–601.
- Boehm, C. 1999. *Hierarchy in the Forest*. Harvard University Press.
- Centola, D., Willer, R. & Macy, M. 2005. The emperor's dilemma: a computational model of self-enforcing norms. *Am. J. Sociol.* 110(4):1009–1040.
- Cheng, J. T., Tracy, J. L., Foulsham, T., Kingstone, A. & Henrich, J. 2013. Two ways to the top. *J. Pers. Soc. Psychol.* 104(1):103–125.
- Henrich, J. & Boyd, R. 1998. The evolution of conformist transmission and the emergence of between-group differences. *Evol. Hum. Behav.* 19:215–241.
- Henrich, J. & Gil-White, F. J. 2001. The evolution of prestige. *Evol. Hum. Behav.* 22(3):165–196.
- Kuran, T. 1995. *Private Truths, Public Lies*. Harvard University Press.
- Redhead, D. J., Cheng, J. T., Driver, C., Foulsham, T. & O'Gorman, R. 2019. On the dynamics of social hierarchy. *Evol. Hum. Behav.* 40(2):222–234.
- Shiller, R. J. 2019. *Narrative Economics*. Princeton University Press.
- Singer, P. 1981. *The Expanding Circle*. Farrar, Straus & Giroux.
- Turchin, P., Currie, T. E., Turner, E. A. L. & Gavrilets, S. 2013. War, space, and the evolution of Old World complex societies. *PNAS* 110(41):16384–16389.

**AI**
- Amodei, D. et al. 2016. Concrete problems in AI safety. arXiv:1606.06565.
- Armstrong, S., Bostrom, N. & Shulman, C. 2016. Racing to the precipice. *AI & Society* 31(2):201–206.
- Askell, A., Brundage, M. & Hadfield, G. 2019. The role of cooperation in responsible AI development. arXiv:1907.04534.
- Critch, A. & Krueger, D. 2020. AI research considerations for human existential safety (ARCHES). arXiv:2006.04948.
- Dafoe, A. et al. 2021. Cooperative AI: machines must learn to find common ground. *Nature* 593:33–36.
- Gao, L., Schulman, J. & Hilton, J. 2023. Scaling laws for reward model overoptimization. *ICML* (PMLR 202):10835–10866.
- Hammond, L. et al. 2025. Multi-agent risks from advanced AI. Cooperative AI Foundation Technical Report #1; arXiv:2502.14143.
- Hendrycks, D. 2023. Natural selection favors AIs over humans. arXiv:2303.16200.
- Kulveit, J. et al. 2025. Gradual disempowerment. arXiv:2501.16946 (ICML 2025 position track).
- Lehman, J. et al. 2020. The surprising creativity of digital evolution. *Artif. Life* 26(2):274–306.
- Sevilla, J. et al. 2022. Compute trends across three eras of machine learning. *IJCNN 2022*.
- Turner, A. M., Smith, L., Shah, R., Critch, A. & Tadepalli, P. 2021. Optimal policies tend to seek power. *NeurIPS 2021*.
