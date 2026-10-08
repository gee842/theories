# 尺度描述的接续充分性 / Continuation adequacy of scale descriptions

2026-10-08。AI 撰写，回应 Ren“请继续，专注在理论推进”。[原话记录](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md)。本轮复用已完成的尺度组合、查询选择、变化依存及经验比较，推进尚未回答的连接：**一个当前足够的描述，怎样支持活动之后仍能作出恰当回应？** 不再把新实验当成本轮理论推导的完成门槛；完整经验验证保留独立范围。

**中心推进：尺度描述的充分性具有接续结构。当前有共同可行回应，只解决当前一步；若活动改变了依存或可辨明范围，还须检查每个实际可能出现的后续记录是否允许继续回应。修复可以来自获得区别，也可以来自正当地改变实际依存。** 二者均有代价与对应条件，不能靠删除差别或扩大“允许损失”的定义获得。

**Central advance:** adequacy concerns a continuing relation among retained information, available activity and subsequent conditions. A common response now is not enough when the resulting histories later require incompatible responses. New evidence can separate them; an actual change in dependence can instead remove the need for that distinction. Neither operation is assumed free or ethically authorized merely because it restores feasibility.

## 1. 为什么已有结果还没有回答这一点

[查询选择](INQUIRY-CHOICE-INTEGRATION.md)已证明：同一观察类内所有相容情形具有共同可行回应，当且仅当存在只依赖该观察的适当单次策略。它的取得证据、耗时与支持失败已完成，直接复用。[变化依存](CHANGING-DEPENDENCY-INTEGRATION.md)又说明：准确的新读数之后仍可能发生改变，因此需要后续变化的可靠范围。[经验比较](PREDICTIVE-CALIBRATION-INTEGRATION.md)则显示：更准确的点预测和可靠的误差界是不同成就。

尚缺的是它们的接续关系。完成眼前一步以后，同一个记录可能对应几种已改变的依存；下一步是否还有一个共同可行回应，不能从第一步的成功推出。反过来，当前有些区别可能还不影响共同回应，直到后续阶段才变得必要。因此，尺度选择还取决于所要承担的时间范围与活动怎样改变后续条件。

这里的理论贡献不是重新发明“未来也重要”，而是明确三个量词的次序：先在当前相容范围内选择共同活动，再允许实际后果发生，最后只能依据届时取得的记录选择后续活动。不能在尚未取得区别时，为不同真实情形各自预选一条互不相容的完美路线，再把它们拼成可实施方案。

## 2. 同一过程里的状态、记录与活动

令 `X` 表示有关活动历史的当前截面，可以包含身体组织、已形成的记录、可用支持、时间及承担；`U` 是其中已经形成的可执行活动类型。它们是模型中的分析角色，不是独立的“主体”和“环境”。转移关系 `step x u y` 表示这样的活动怎样参与从当前截面到后续截面的展开。没有假定活动能独自控制全部转变：关系可有多个后继。

当前描述由相容范围 `B` 表示：哪些历史截面仍与已取得的证据相容。这个范围不是额外的世界实体，也不是谁可以任意宣布的真值集合。真实历史在其中、转移覆盖实际可能后果、读数确实由所述关系取得，都是独立对应前提。信念更新若排除了真实情形，就不能使用后面的保证。

`obs y` 描述下一阶段实际取得的记录。它可以来自更细的感知、历史的保留或已有组织的输出，不必意味着免费的外加测量。查询耗时、记录损坏、资源不足等若属于研究问题，就必须写入 `X`、转移及可用活动；本轮有限见证尚未建模这些代价，已有研究的代价结果仍有效。

`good x` 是本问题要求保留的条件；`allowed x u` 是该情形下容许的活动。名称不赋予伦理正当性。一般定理对任何此类条件成立，因此不证明某一条件值得维护。在生成性对齐的应用中，条件及权限应由已完成的 G0/J 一般实践判断和现实对应提供；不从“可以持续”倒推出“应当持续”。

## 3. 接续充分性的精确条件

活动 `u` 与后续读数 `o` 形成新的相容范围：

\[
B^{u,o}=\{y\mid \exists x\in B:\; step(x,u,y)\ \land\ obs(y)=o\}.
\]

这里同时保留活动造成的变化和后来证据的筛选。只筛选旧状态会忽略实际变化；只传播可能后果而不使用新记录，又可能保留已经排除的混淆。

定义 `V₀(B)` 为 `B` 中每一实际候选都满足要求。递推地，`Vₙ₊₁(B)` 要求：

1. 当前候选均满足要求；
2. 存在一个对所有候选都容许、并且在每个候选处都有实际后继的共同活动 `u`；
3. 对每个可能取得的读数 `o`，更新后的范围 `Bᵘ˒ᵒ` 满足 `Vₙ`。

显式要求后继存在，避免把“没有后续状态”误当成所有后续状态都成功。没有实际对应的观察分支是空集；若活动类型非空，它们不给方案添加实际负担。有限结束并未被否决：本轮验证有限时域，零步处不再要求后继。若要把有根据的完成、交接或结束纳入更长任务，可以将它作为已满足后续要求的终结状态；不能把停止计算当成真实世界冻结。

**Lean 证明该递推条件等价于一个只依赖后续记录的有限分支方案存在。** 方案先选共同活动，再依 `obs` 选择下一分支。这个等价不是已执行的合成算法：它使用经典选择把存在见证组织成分支函数，没有界定计算量或给出所有现实问题的求解器。

另有一般结果：

- 在其他关系不变时，缩小相容范围保留已有有限方案；应用时仍须保证真实情形没有被排除。
- 若一个后续读数可映射回旧读数，且活动、后果和要求不变，细化读数保留原有可行性。**改变采样代价或时间后，这个“不变”前提不再成立**。
- 较长时域的充分性蕴涵较短时域的充分性，反向一般不成立。
- 若一族相容范围中的每一项都满足当前要求，而且存在共同活动使每个后续观察类仍落在该族，就支持每个有限时域。证明没有抽取一个无限方案，也没有将任意给定范围宣告为真实可维护范围。
- 从当前递推充分性选出的活动，其每个实际相容后继都进入仍充分的后续观察类。结论覆盖模型关系中的全部后继，不只一个幸运后果。

## 4. 同一反例中的失败与两种修复

有限见证的状态是阶段与一个持续依存区别的组合。阶段为起始、需要回应、完成或损失。起始有两种相容历史；第一步无论选择哪一活动，都把它们送到需要回应的阶段，区别仍然存在。第二步只有匹配该区别的回应才到达完成，否则出现损失。损失状态持续保留，不能用后来的好结果抵消。

| 描述／活动关系 | 一步 | 两步 | 原因 |
|---|---|---|---|
| 所有记录相同，保留原有依存转移 | 可行 | 不可行 | 第一步共同成功；第二步需要相反回应，记录无法区分 |
| 后续记录实际揭示该持续区别，同一转移 | 可行 | 可行 | 先执行共同一步，再依取得的记录选择匹配回应 |
| 保持原粗记录，改为实际消除待回应依存的转移 | 可行 | 可行 | 两种情形均真实进入完成阶段；不需要认出区别 |

第三行在形式上使用另一明确给定的转移 `settle`，不是声称原有操作已能神奇修复一切。它保留区别但改变区别对以后是否完成的作用。其可获得性、代价、其他后果和正当性均未推导。这个对照建立一个有限反例：**未来辨别不是唯一可能的修复途径**。它不建立一般的“忽略差别无害”原则，也不容许把受损者移出评价范围来伪造完成。

The finite construction checks genuine transitions into retained failure or completion states. It distinguishes epistemic refinement from changing the dependency itself. The alternative transition is supplied, not discovered, funded or justified by these theorems. General observation refinement is proved under unchanged dynamics; the costful acquisition question remains governed by the earlier completed comparison.

## 5. 对身体、认知与生成性对齐的意义

细胞、器官、身体、生态关系并不是预先排成一列的信息压缩器。某一尺度的活动会改变另一些关系的后续条件：组织维持某些共同可行活动，损伤或支持中断使原有描述失去足够范围，新的感知或组织转化又可能恢复。当前模型把这类接续结构说清楚；它没有证明全部生物机制都服从同一个具体转移式。

因此，“必须保留什么”要相对于具体接续来回答。一个局部历史可能已经保留相互作用留下的后果，因此能支持当前任务；另一个任务若涉及被省略的具体承担、局部损失或未来分歧，就可能要求新的区别。这里不能从温度预测中的局部模型成功，推广为应当只关心局部；也不能从一元关系性直接推出每步必须显式表示整个世界。

在生成性对齐中，新的理论要求是：**评价一个能改变后续判断条件的方案时，要将这些条件的变化纳入其理由与可行性评价。** 可预见地破坏后续辨别、纠正、交接或履行承担的条件，是需进入比较的真实后果。某一方案仍可能因已完成任务、正当有限结束、替代关系形成或更强理由而适当；本轮没有再增设“无限保持一切可能性”的最高义务。

[关切内容扩展](../../../../theories/becoming/chapters/CONCERN-AND-NEW-REASONS.md)已经说明新理由如何保留、改变或反转比较，直接复用。本轮补充的是实施侧的时间条件：新理由获得根据后，还必须有能落实相应回应的后续机会。如果规范条件本身变化，不能用保持固定 `good/allowed` 的定理冒充旧方案仍适当；应先更新有根据的要求，再检查接续。

这也说明实践智慧为何不能只等同于更精细预测：它还包括辨别什么值得保持、何时需要进一步认识、何时改变实际关系，以及何时有根据地完成或结束。本轮只完成其中的条件化实施接口，不重新声称已解决关切的自发形成或普遍遵从。

## 6. 数学实查、前提与来源比较

[Lean 源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/ContinuationAdequacy.lean) · [重现脚本](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_continuation_adequacy.py) · [实查回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/continuation-adequacy-verification.json)。本轮 **14项新定理／14项声明审计**，独立模块直接导入固定 Mathlib；此前各轮证明没有重复编译或合并计数。Lean 4.30.0-rc2，Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`。9项无公理依赖；存在方案等价及有限见证只用标准经典／逻辑依赖，无 `sorry`、自定义公理或未经检查的本机判定。源文件、编译器、直接导入和审计输出有版本绑定。

一般定理量化任意给定状态、活动与读数类型；不要求有限状态。有限的只是所证时域，另外四个构造见证使用有限状态。模型没有要求观测到整个状态，也未证明观测机制、资源和规范条件的来源。若状态省略会改变未来的依存，`step` 的对应就需重建；定理不会自动补齐缺失关系。

**Primary comparison.** Reissig, Weber and Rungger, [*Feedback Refinement Relations for the Synthesis of Symbolic Controllers*](https://arxiv.org/html/1503.03715), introduction and Definition V.2, explicitly address the availability of state information, enabled inputs and containment of successor behavior. This gives conventional control theory full credit for distinguishing a formal abstraction from one that supports implementable feedback. Our information-set recursion is narrower, not a new proof of their necessity or canonical-abstraction results. We inspected these sections, not all algorithms or examples; source retained as a link only.

Russ Tedrake's [*Underactuated Robotics*, recursive feasibility subsection](https://underactuated.csail.mit.edu/trajopt.html) explains why a feasible current plan can become infeasible after the horizon shifts, and gives terminal conditions that preserve further feasibility. This is direct precedent for the temporal issue. Our finite partial-information condition addresses a related interface within the theory; it claims no priority over invariant-set or predictive-control methods. The source comparison is not new experimental evidence.

## 7. 实质反审与完成范围

**是不是把结论写进定义？** 递推定义表达待实现的要求；`viable_iff_plan` 的贡献是证明它恰好对应所列信息限制下的方案存在，不能独自证明实际关系满足它。反例和修复进一步检查同一明确依存的后果。理论增量在于把已有一步条件接到可实施的后续分支，并列清应用的对应义务。

**是否用完美信息偷渡成功？** 初始两种情形保持不可区分；精细读数只在第一步以后形成。原粗读数的第二步不可能性保留。一般定理不允许依据未取得的真实状态选择分支。不过读数真实取得及代价仍是给定的对应，不是已经解释的感知起源。

**是否忽略有限结束？** `V₀` 只要求终点适当，后继要求仅用于承诺继续的步骤。每个有限时域可行不被冒称一个无限生命史，更不被转为永不结束的道德命令。

**改变关系是否只是改名？** 修复转移真实到达完成阶段；原有待回应转移仍保留失败。这里确实更换了假设中的可用机制，所以只证明“这种实际修复若可获得，辨别未必必要”，没有证明它普遍存在或无损。

**一般条件是否保证最优尺度？** 没有。它不给出最小记录容量、最便宜的信息取得方法或最优组织设计；也不比较未经表示的新活动。对计算时间、错误证据和实际成本，需使用或扩展已有机制结果，不能由存在量词忽略。

本轮完成接续充分性的理论接口、一般证明、反例、两种修复及既有理论定位。自我反审由实现者完成，不冒称独立 agent 验收。下一理论连接是**多处形成的局部接续承诺怎样在共享条件下相容**：每一处各有方案，并不说明它们能同时实施；须把共享占用、时序与承担接回同一历史。已核读[共同实现研究](EXPLANATORY-JOINTNESS-INTEGRATION.md)：共享占用／释放、指定部分身份与逐节点方案恢复已有结果；未完成的是跨分支共享条件下的一般全局接合。本轮下一接口是把这些已说明的相容关系带入观察后的递推，而非重新证明共享支持会冲突。完整经验验证保留其独立目标，不成为本轮已经完成的理论接口的新门槛。
