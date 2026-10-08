# 非二元生成核心的形式接口：历史、派生角色与实际响应范围

2026 年 10 月 6 日。AI 撰写。连接是**共同生成过程 → 实际历史中的局部作用关系 → 可重叠、可改变、可解组的响应角色**。接续[非二元生成重构](NONDUAL-GENERATIVE-RECONSTRUCTION.md)、[主客分化之前的起点问题](NONDUAL-GROUNDING-QUESTION.md)与[生成之我](../../../../theories/becoming/chapters/GENERATED-SELF-AND-ETHICS.md)。先前 Actor/Patient 下标并未断言独立实体；现有 `Generative.Process` 本来也没有这些原始类型。本轮将这个依赖方向明确落实为代码架构和可检查的角色派生接口。

**建立的正结果：同一实际生成过程可以先被表示，再从它的历史、连接与实际作用条件读出局部角色；这种描述扩展可以完整保留原过程的路径和终点。同时，具体共同基底内可以形成重叠的联合响应范围、产生实际效果、再解组；一个先前受作用的位置可以成为后续响应的必要来源。** 这建立的是角色可作派生描述的形式实现，不是已经推导出自我、体验或伦理。

## 1. 依赖方向与原始承诺

代码拆成三个不同层次：

| 文件 | 依赖与责任 |
|---|---|
| [lean/NondualCore.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/NondualCore.lean) | 仅导入既有 `GenerativeCore`；实际历史、描述呈现、净作用与信息保真标准。不导入 Patient、Actor、伦理契约、资源律或有利方向。 |
| [NondualFormation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/NondualFormation.lean) | 导入新通用核心，在供给的信号法则中实现形成、重叠、实际作用、解组及角色转换；不导入患者模型。 |
| [NondualConcernAdapter.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/NondualConcernAdapter.lean) | 导入核心与旧 `GroundingContract`；把伦理和旧患者下标定位为额外解释层，明确保留其契约。 |

因此不存在从旧患者类型或 C2 回流到新通用核心的导入路径。新的[公共入口](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeNondualModel.lean)同时导入既有 `GenerativeOutcomeModel` 和新核心，直接连接原模型及其带终点结果的延续接口。旧公共入口和旧来源字节不被替换。

通用接口仍以给定的状态类型、事件类型和 `P.step` 为基础。它未声称推导现实事件律，也未声称可以不用逻辑或类型背景。事件类型只为发生的转换提供标签，不暗含一个先在行动者。任意状态类型可能已经包含应用者自己的分化；本轮不把所有现有局部模型的类型设计追溯性地改造成从零生成。

## 2. 实际历史与描述扩展保持同一个过程

`ActualHistory P` 记录起点、事件词、终点以及其 `Generative.Trace` 见证。它不假设额外的观察者或所有者。该见证位于 Prop；遇到非确定过程时，这份记录未必区分具有同一起点、事件词和终点的所有中间分支，也不是可直接读取的完整中间状态日志。

`historyProcess P` 的一步必须由原过程的真实一步扩展原有历史。以下精确关系通过既有核心的 `trace_map`、`trace_lift` 和投影定理得到：

\[
\operatorname{Trace}_P(h.finish,w,t)
\quad\Longleftrightarrow\quad
\exists k\,[\operatorname{Trace}_{H(P)}(h,w,k)\land k.finish=t].
\]

它保持实际终点，不只保持“某个事件词可发生”。完整历史结构是分析者的数学构造；没有据此宣布原系统已物理存储自己的全部历史。

给任何描述函数 \(d:S\to D\)，其一致呈现为：

\[
\widehat S_d=\{(s,r)\mid r=d(s)\}.
\]

新呈现的转换仅由原转换决定：\((s,d(s))\xrightarrow e(t,d(t))\) 当且仅当 \(s\xrightarrow e t\)。遗忘描述与恢复描述互逆，因此所有对应起终点和事件词的路径严格等价。将 S 取为实际历史载体，即得到历史依赖的派生角色描述。

角色描述的输出类型 D 没有限定为互斥分区；它可以包含若干重叠关系、条件角色或查询剖面。定理没有自行选出一个唯一正确的身体边界或角色解释。选择 d 与说明其解释意义仍是工作。它也不否定实际自我模型的因果作用：本节处理数学附注；若获得的模型改变行动，模型寄存、读取、更新与作用必须在原 `P.step` 中有物理实现。既有[获得的自我表征桥](SELF-ACQUISITION-BRIDGE.md)是不同的实现层。

`Affected readout h` 定义为某个实际状态读数在 h 起点和终点不相等，附加一致描述保持它。这是净作用指标。它不检测被后续事件抵消的中途变化；净变化为零绝不推出没有发生中途伤害。读数本身也不自动识别体验、所有权或价值。

## 3. 角色描述何时可以被压缩

设 H 为所关心的历史/状态域，\(\Phi(h,l)\) 是对局部角色或后果问题 l 的回答，\(q:H\to R\) 为报告。存在精确读出 \(\rho\)，使

\[
\rho(q(h),l)\leftrightarrow\Phi(h,l)
\]

当且仅当 q 不合并对某个问题答案不同的历史：

\[
q(h)=q(k)\Rightarrow\forall l\,[\Phi(h,l)\leftrightarrow\Phi(k,l)].
\]

必要性由同一报告的读出必须相同得到；充分性可取“存在一个产生该报告的历史对该问题回答为真”的汇合解释。这个构造不需要挑选一个隐藏的真正主人，也不要求报告保存一切差别。但它同样不实现传感、学习或记忆硬件。

这是[既有 GeneratedSelf 精确摘要准则](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean)在指定角色/后果问题上的一般化应用，不算重新发现一个独立的信息定理。其用途是防止非二元叙述把仍然决定真实后果的差异删除。表述不分原始主客，不等于可以将各种能力、遭遇和历史视为可互换。

## 4. 一个共同基底中的实际形成与角色改变

具体实例只有一种节点载体 Nat。状态是有向连接列表与活动节点列表。供给的事件法则允许连接、断开与脉冲；脉冲在满足下述条件时反转目标的活动状态：有两位不同的、目前活动的非自身来源，通过当前连接指向它。没有 Actor/Patient 类型、痛苦变量、帮助目标、私人奖励或伦理排序。

`Support(s,n,a)` 从实际状态读出：a 活动、a 不同于 n、并有 a→n 的连接。形式定理证明它与这些条件等价，也证明脉冲的使能条件恰好是存在两个不同的 Support 来源。同一来源的重复边不能伪造联合能力。

初态的节点 0、1、2 已活动，尚无连接。它们及脉冲法则是输入，本轮派生的是响应范围，并未生成基本节点。四次连接事件依次形成：

\[
\{0,1\}\longrightarrow3,
\qquad
\{1,2\}\longrightarrow4.
\]

两个来源范围不同而重叠于 1。它们不是连通分量式的互斥分区；没有由重叠推出共同体验者。当前各有恰好两位来源，形式检查证明断开其中任一输入连接会使相应目标失能。一般有三位以上来源时，`sources` 是全部候选来源的合集，每个成员未必必要；最小二元支持由两位不同来源给出。

随后真实脉冲 3、4 将两个目标由不活动变为活动。再断开四条连接，当前活动状态保持，而两个目标的脉冲能力都消失。脉冲采用反转法则，先前成功后仍能再次脉冲，所以这里的失能确由断边产生，不能归咎于“任务已完成而自然不再使能”。已有活动也没有因响应范围解组而被抹除。形成、响应、解组的合成是原 `Generative.Trace`，不是分析表格中的角色赋值。

另一个分支从真实响应之后开始：形成 3→4、断开 2→4。此时 4 的来源变为 \(\{1,3\}\)。3 原先是被作用的目标，现在成为使能后续脉冲的必要来源：断开 3→4 或在同样连接中移去 3 的活动都使 4 失能。下一次真实脉冲将 4 从活动变为不活动。

这个后缀的重要性是角色转换，而非把开或关定义为善。它明确打破固定的来源 0–2 / 目标 3–4 二分。同一共同载体上的作用关系产生所讨论的局部角色，角色可以随实际历史改变。

具体法则仍被供给，实际历史也被选择；没有证明所有生成系统都有这类联合结构，或它们必然形成、持续、有利。两路共享来源并不计入燃料或竞争成本；这不是前轮患者服务的资源模型，也不声称已自动共享其完整物质历史。

## 5. 有意义的失败证据

只知道活动节点，不能精确恢复响应能力。响应后与解组后活动列表完全相同，但连接不同，目标的脉冲能力相反。`no_activity_only_capacity_report` 因此证明：没有仅依赖活动列表的读出能在所有状态正确回答该能力问题。这是上节报告充分性标准的具体失败见证。

同样，任意重新命名或补充角色附注不会生成缺失的连接。没有连接的初态不具备两个指定目标的能力；重复来源也不构成二者合力。相反，实际连接、来源活动或触发法则的变化可以改变能力。呈现变化与真实作用条件变化被区分开了。

这防止两种误读：统一描述不允许抹去现实差异；派生角色也不等于它们毫无因果根据。实际起作用的是共同状态中的连接与活动，而不是角色名的宣告。

## 6. 伦理下标作为扩展及其保留条件

独立的 `NondualConcernAdapter` 使用整个情境 X 上的谓词 A、O、F，表述：\(A(x)\land O(x)\Rightarrow F(x)\)。它不位于通用核心，也不由通用核心推导。角色呈现 \(v:R\to X\) 总能把该契约拉回到角色化描述；若角色呈现覆盖所有 A∧O 情境，角色层上的契约也能反射回情境层。覆盖不可省略，否则未被命名的实际发生会被静默丢掉。

旧 C2 的 `(State,Patient)` 是这类情境描述的一个应用，原患者条件、机会和 Merit 正好给出 A、O、F。Lean 证明两种陈述对应，而非声称从描述等价获得规范正向性。旧局部患者类型还在兼容层内，它未被宣布为全局本体原语，也没有在本轮从实际体验中推导出来。

因此本轮真正解除的是**通用形式核心必须先装入固定主客/患者类型**这一架构要求；它不能解除 C1/C2 的伦理根据、体验实现、合宜性与现实身份识别的论证义务。原核心本已容许这种单向依赖，本轮补的是明确的扩展定理、非固定角色实例和公共接口。它既不证明原始独立我必需，也不证明经验世界的所有我都已由该示例生成。

## 7. 构建与检查

独立新检查命令：

```sh
python3 -B experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/check_nondual.py
```

该检查在新临时目录重建七个模块，新增 **31 个声明的依赖审计**：通用核心 11、具体形成实例 16、兼容层 4。[新收据](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/nondual-verification.json)记录冻结源码、日志及旧收据保留结果。通用核心与兼容层的新审计为空；实例中部分证明使用 `propext`、`Quot.sound`、`Classical.choice`。空审计只报告形式证明依赖，不意味着没有给定过程、描述函数、解释条件、逻辑或类型背景。

公共入口的两个包装定理与继承模块另有[通过的构建回执](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/nondual-model-verification.json)：重建 18 个模块，两个新包装的依赖报告为空；重复构建的核心不重复计数。因此本轮共 **33 个不同的新增声明审计**，不是 33 个独立经验发现。

[独立回执](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/nondual-independent-review.json)又在全新临时目录重建包含公共入口、具体实例与兼容层的全部 23 个模块，确认同一冻结字节、33 项新增审计、旧来源/收据保留，以及公共入口不依赖 Patient 模块。独立作者还编译实际 Lean 查询，将所声明的七条候选边与五个活动节点的全部布尔配置交叉，得到 4,096 个状态、对目标 3 与 4 的 8,192 次能力查询，与独立集合解释全部一致；六个关键状态逐字段重放以及重复边/自边检查通过。该有限切片不等于穷尽无限 Nat 节点网络；通用命题的范围由 Lean 定理给出。

这些检查确认描述/路径关系和给定信号法则的结果，没有新增生物学、意识或伦理经验数据。既有角色获取机制、患者好坏与价值方向仍须在各自范围内得到解释与识别。
