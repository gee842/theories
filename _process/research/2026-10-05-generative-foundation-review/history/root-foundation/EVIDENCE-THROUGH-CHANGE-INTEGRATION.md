# 从取得证据到共同实施 / Evidence through change to joint action

2026-10-08。AI 撰写，回应 Ren 的[继续指示](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md)。本轮接续[有根据的相互接续](SEEDED-CONTINUATION-INTEGRATION.md)，研究**取得时的相容范围 → 行动前可能发生的变化 → 执行时的共同支持及局部方案适用范围**。

**中心结果：支持行动的证据必须覆盖执行时仍可能到达的情形。** 记录可以仍然正确地描述过去，却不再足以支持现在的行动。新的证明把变化后的候选范围接回既有有限方案合成，并区分两条正面路线：容纳变化后仍能回应，以及通过实际保护改变可能的变化范围。

**Central result:** propagate acquisition-time candidates through the admitted changes before use; certify the shared seed conditions and the domains of both local plans over that propagated set. The existing seeded composition theorem then supplies a valid joint plan. This is a conditional evidence-to-execution interface, not an automatic warrant for the change envelope, sensing process or ethical permission.

## 1. 已有结果直接复用

- [变化依存](CHANGING-DEPENDENCY-INTEGRATION.md)已检查读数误差、时间变化界限、刷新后仍失败及保留未来界限的修复。新鲜不等于未来准确，这不是本轮新发现。
- [变化支持](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md)已把当前占用、保护、恢复及实际推进放入同一历史，保留静态清单相同而准备不同的例子。
- [纠正交接](CORRECTION-HANDOFF-INTEGRATION.md)已实现实际探测、版本检查和有限／无界前缀保持，保留漏记变化、重复版本和提前关闭的失败；原子性、真实探测及全体相关变化受管理仍是前提。
- [可失实见证](FALLIBLE-INSPECTION-INTEGRATION.md)已说明怎样保留真实候选而不指定一个绝对可靠的见证者。它提供候选覆盖的条件性来源，不替本轮自动覆盖检查后新发生的变化。

新工作直接导入 `SeededContinuation`，不重写上述机制或声称已经解决它们的全部部署问题。新增的 `delayed_seeded_plan` 明确把**变化后的**范围用作旧定理的初始条件；不能只验证共同支持，却继续让局部方案依赖过时的适用范围。

## 2. 同一历史中的取得与使用

令 `C(x)` 表示取得记录后仍相容的共同状态，`D(x,y)` 表示从取得到实际使用之间被容纳的变化。二者描述同一历史的不同关系，没有预设独立的观察者和被观察世界。取得记录本身的影响应进入取得后的状态；若读数与完成取得之间已有时延，也须计入候选构造或 `D`。

执行时保留的范围是：

\[
T_D(C)(y)\iff\exists x\,[C(x)\land D(x,y)].
\]

若实际取得后的状态在 `C` 中，实际后续变化被 `D` 覆盖，则实际执行前状态在 `T_D(C)` 中。这里没有概率先验、权重或“最可能状态”选择。缩减候选必须有新的证据或机制根据，不能为获得许可而删除不利情形。

针对条件 `I`，证据的充分性写为：

\[
\forall x,y\,[C(x)\land D(x,y)\Rightarrow I(y)].
\]

Lean 检查它等价于 `T_D(C)` 中每个候选都满足 `I`。这是所给集合／关系下的精确等价。如果 `C` 或 `D` 是保守扩大后的范围，未能通过证书只说明当前证据不足以保证，不证明真实行动一定失败。如果它们漏掉实际状态或变化，证书通过也不能据此推出实际结果。

两段变化的传播可合成为一次关系复合。较小变化范围保留较大范围上已经成立的证书；反向一般不成立。对任意有限长度的变化历史，若初始候选满足 `I` 且每一步变化保持 `I`，则全部可达候选都满足它。这里的“有限任意长”没有提供物理时间无限或无限方案抽取。

## 3. 接回共同方案时必须一并保留什么

上一轮的共同启动需要 `R ∧ S`，两份局部方案分别只对其候选范围 `Ca,Cb` 有效。因此本轮必须认证的是：

\[
I(y)=Ca(pa(y))\land Cb(pb(y))\land R(y)\land S(y).
\]

源码采用等价的分组括号。它保留了两个不同义务：共享条件仍足够，局部方案仍适用。共同支持尚在，却因状态改变而离开局部计划的保证范围，仍不能直接调用旧计划证明。

`delayed_seeded_plan` 以这份证书、旧的局部有效性、共同作用投影、一步共同可实施和互相保持为前提，调用已检查的 `seeded_joint_plan`，推出配对方案在整个 `T_D(C)` 上有效。行动仍依各自记录分支；没有把实际未知的状态直接交给局部选择者。

**范围。** 此接口把启动前变化接入已有计划。执行中的变化必须包含在旧定理的共同转移里；若每次读数后到下一动作之间还发生额外变化，就必须合入每步转移或在每次接口处重新履行对应条件。一次启动证书不能自动覆盖以后所有未建模的插入事件。

## 4. 真实读数如何失效，实际保护如何修复

具体配置记录一项支持是否仍可用、是否已为本次活动保留，以及最近读数。它们是共同过程中的三种关系；记录不是被默认为永远正确的额外实体。

`readNow` 取得当时的真实可用性。`takeElsewhere` 允许在未被保留时消耗同一支持，并留下读数不变。于是：先读取可用，再发生该消耗，最后准备行动；读数仍说可用，实际支持却已不在。两段历史的记录相同，当前可用性不同。

`no_exact_record_only_decision` 检查：仅以这一条保留的布尔读数作判断，无法同时对这两个具体可达情形准确判定当前可用性。恒拒绝可以避免误准，但不是准确识别；额外证据或新的行动安排可能改变问题。此结论不泛化为所有知识都不可靠。

正面修复 `reserve` 在一个明确原子步骤中检查当前可用且未被保留，并实际建立保留关系，同时产生记录。允许的后续变化只有停留或未保留支持的上述消耗。在这个规律下：

- 一次实际保留从已读的可用状态确实可执行；
- 保留建立真实保护与肯定记录；
- 任意有限的允许变化历史都保留支持可用性；
- 同一份支持不能再次通过同样的保留操作；
- 不服从该保护关系的破坏可以使支持失效，保留记录本身阻止不了它。

因此，保留的效果来自改变后续活动的实际关系，不是把旧读数升级成更有权威的标签。该例是具体规律下的条件实现：它仍假定保留操作原子、所有相关消耗尊重保留、支持不自行损坏；没有解决保留机制自身的硬件实现、到期、释放、公平性或真实授权。

## 5. 两条正面路线与理论推进

一条路线是**容纳变化**：传播可能后果，若原方案仍适用于所有候选，就不必冻结过程。早前变化依存研究的有界回应属于这一方向。另一条是**改变后续变化条件**：例如取得实际保留，使原本可能的冲突不再属于受保护历史。这两条路线可以组合，但不能仅在模型中删去不利变化而没有现实根据。

由此，尺度描述的充分性不仅取决于记录保留多少细节，还取决于记录所依赖的关系怎样维持到作用发生。更细的读数未必弥补无界时延或未受管理的占用；较粗的读数在确有稳定保护时也可能够用。这是关于所选行动及变化范围的充分性，不是无限制赞成粗略描述或控制全部变化。

对生成性对齐，实施侧的问题是：提出承诺时确认过的支持、权限和关系，是否继续支撑实际履行。技术上可保留的条件不因此值得强制冻结，也不使持有记录者自动获得支配权。哪些影响可以约束、谁承担等待与占用成本、何时释放或结束，继续复用 G0/J 实践判断。可行性、认识根据和规范理由在同一活动中相关，但本轮没有把其中一项的成立当成其他两项的证明。

## 6. 来源与实质反审

Read Dean and Hu, [*Fixing Races for Fun and Profit: How to use access(2)*](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/dean/dean_html/accessopen.html), §§2.1–3. Their specific filesystem result makes the allowed interfaces and adversarial scheduling assumptions explicit; separate checks can be overtaken before use. Our finite shared-support example credits this established problem and does not reproduce their filesystem impossibility theorem or endorse their probabilistic remedy. Source inspection is link-only; no publication bytes were imported.

**反审：传播候选只是把“不知道”写大了吗？** 传播由给定变化关系限定，不是任意怀疑。若关系太宽，会失去可执行的共同方案；若太窄，会失去真实覆盖。如何获得恰当关系是实际对应问题，本轮不把历史最大误差或成功次数当成其证明。

**反审：证书是否把结论放进定义？** 等价定理确实展开一个充分性判准，本身不提供新的经验根据。新增推导在于将该判准准确接到既有共同方案的全部初始义务，并证明组合和有限变化保持；具体反例与保护规律展示何时不能、何时能够履行这些义务。一般关系像、程序前置条件和不变式足以解释这些形式结果，不主张新数学或唯一生成本体。

**反审：以原子保留修复非原子问题是否偷换？** 它明确改变可用操作并承担更强实现前提，所以只是一个修复方案的充分条件。没有从旧的纯读数接口证明实际已有这种原语，也没有宣称本轮完成并行研究中的非原子物理部署。若保护不被实际执行，失败见证仍成立。

## 7. 检查、完成范围与下一连接

[源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/EvidenceThroughChange.lean) · [重现脚本](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_evidence_through_change.py) · [形式回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/evidence-through-change-verification.json)。**15项新定理／15项审计通过，10项空依赖、5项仅 `propext`；另重放43项继承审计。** Lean 4.30.0-rc2，固定 Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`；无自定义公理、证明缺口或经典选择依赖进入新结果。初次编译暴露保留字命名与未展开定义的判定问题，修正后完整构建通过；冻结源码、日志及工具绑定已保留。作者反审不是独立 agent 验收，无新经验实验。

本轮完成取得候选经变化传播后接入共同计划的条件接口，并保留读数失效和受保护修复。下一连接是**执行后的证据如何同时检验实际后果与先前采用的变化范围**：未预见变化已经发生时，不能仅在旧范围中重新筛选；需要辨认是范围遗漏、读数失实、执行偏差，还是计划本身失效。已有候选修订和可失实见证成果须直接复用，后续研究只处理这些解释怎样在同一反馈历史中被区分和修正。
