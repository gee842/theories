# 评价目的所不能省略的关系 / Indispensable relations in evaluating ends

2026-10-08，Asia/Bangkok。AI 撰写，执行 [Ren 再次要求继续](../../../../sources/15-codex-theory-conversations/2026-10-08-wisdom-paper-direction.md#continuing-goal-grounding)，接续[回应必要性](WISDOM-RESPONSE-NECESSITY.md)，推进 [the root of wisdom 完整目标](CORE-CONSTRAINT-AND-WISDOM.md#root-of-wisdom-target)。本轮复用已经完成的目标形成、实际修订和 G0/J/E 根据，不重开这些任务。

**结果：在同一既有过程律内，旧、新目标的全部给定成就指标相同，基本生活条件不同，可以使目标评价相反。任何始终符合这项公开比较的确定性选择器，都必须保留足以区分这两种处境的信息；一个固定但回应这些关系的规则也能满足要求。** 新增7项 Lean 定理、11项显式声明审计。这个条件性必要关系已证；整个 core 对所有智慧的不可替代性仍未证。

**Result.** Identical attainment profiles for both supplied goals coexist with opposed practical frontiers under the inherited outcome law. Any uniformly adequate deterministic selector must distinguish the two configurations. A fixed relation-sensitive rule is sufficient throughout the supplied family. This is a content requirement under explicit comparative commitments, not a refutation of fixed higher-level explanations or a universal definition of wisdom.

<a id="reuse-and-contribution"></a>
## 1. 此前已完成什么，本轮增加什么

[生成性对齐论证](GENERATIVE-ALIGNMENT-REVISION.md)已经说明：目的、评价者和塑造它们的安排均可按同一 G0/J/E 根据评价。其历史性的“尚待相连实现”后来由[目标形成与修订](GOAL-FORMATION-REVISION-INTEGRATION.md)以及[相连接续](GOAL-REVISION-CONTINUATION.md)完成。原目标仍获奖励、仍能成功，新目的却有根据并实际影响后续行动，这些均为既有成果。

本轮不重新声称发现“目标可以变化”，也不把固定上层规则当作已经排除的对手。既有模型明确保留该解释。现在推进的是根基必要性：**保留相同判断内容的实现，最低限度不能省略什么？** 上轮对行动充分描述的结论不能直接回答目标评价；本轮在已有目标模型内部检验。

“最低限度”不预设唯一最粗表示。结论只要求区分两个评价确实相反的配置；至于通过记忆、惯习、共同制度、显式模型还是其他表示实现，并未限定。

<a id="fixed-law-comparison"></a>
## 2. 保持同一过程律，改变真实损失关系

直接使用 `GoalFormationRevision.perform`，不改写继承源码：旧实践产生2单位计数产出和0单位掌握，新实践产生1单位计数产出和1单位掌握。旧目的以计数产出为成就，新目的以掌握为成就。两个指标在整个局部条件族内不变；两种实践仍各自实现对应目的的最优给定手段。

同一法则还保留两个基本条件：实际参与能力与必要维护。旧实践可能破坏参与；新实践可能破坏维护。它们的有无由原模型已有的两个条件控制，不靠新加一个任意“善”标签改变评价。

| 配置 | 旧实践的保护与成就 | 新实践的保护与成就 | 公开 J2 范围内的比较 |
|---|---|---|---|
| 旧安排损伤参与，新安排保住维护 | 丢失参与，保住维护；产出2、掌握0 | 保住参与和维护；产出1、掌握1 | 新实践严格胜出 |
| 旧安排保住参与，新安排损伤维护 | 保住参与和维护；产出2、掌握0 | 保住参与，丢失维护；产出1、掌握1 | 旧实践严格胜出 |

两行具有相同的旧、新目标成就表，原模型的同一 attendance 选择规则也给相同反馈。评价反转来自不同的实际保护关系，在公开 J2 比较下生效。**不是新目标天然较好，也不是改变天然较好。** 两项基本条件都未受损时，既有定理保留两种可放弃增益的不可比；两项分别受损时，既有定理保留基本损失冲突。本轮不删除这两类情况。

形式模型把实际参与和维护取为局部已说明的保护项，不是把一切损害压成通用真假位。应用中须独立说明这些关系确属基本条件、其程度和历史范围，且不存在被遗漏的其他基本代价。无可靠对应时，不能直接使用这一强比较。这里完成的是同一给定条件族中的推理，不是教育实践的实测结论。

两行比较的是同一法则下的不同配置，本轮未把它们的转换另行实现为连续时段。目的、辨别和响应的形成沿用原来的相连历史，未被设为过程之外的独立实体；当前局部接口省略形成细节，只保留所检验的后果与比较关系。

<a id="checked-necessity"></a>
## 3. 被检查的必要性及其边界

`achievementProfile c` 返回每个已给定目的在每种实践中的成就，即 `Goal → Practice → Nat`，包含旧、新目的，不能把失败归咎于只看旧目标。`Acceptable c p` 使用继承的 `Frontier`：在两个均被列入菜单的实践中，p未被 `Better` 击败。这不是完整的伦理许可；权限、实际可执行性、历史承担和正当选择程序仍需另行成立。

| 新定理 | 结论与所需内容 |
|---|---|
| `achievement_profiles_equal` | 任意两个局部配置的完整给定成就表相同 |
| `retaining_goal_preferred` | 保住参与而新安排破坏维护时，旧实践按继承比较严格胜出；复用已有保护优先定理 |
| `revision_frontier_iff` | 第一行配置中，未被击败恰好要求选新实践 |
| `retention_frontier_iff` | 第二行配置中，未被击败恰好要求选旧实践 |
| `adequate_goal_selector_distinguishes` | 对任意表示类型及确定性选择器，若每个配置的选择均未被击败，表示不能合并这两个配置 |
| `attainment_only_selector_insufficient` | 因成就表合并二者，仅通过该表作选择无法满足上述全配置要求 |
| `fixed_ground_rule_adequate` | 复用既有 `callsForRevision` 的一个固定规则，在全部局部配置中选出未被击败的实践 |

证明没有把智慧谓词自由开关来产生差别。两项相反比较从原有保护法则和原有 `Better` 推出，通用表示必要性再由这两个结论得到。它延续上一轮“先固定要兑现的内容，再反查不可省略关系”的方法，并直接落在已有规范候选上。

**必要性的准确量词。** 对所有能始终满足这个局部比较要求的确定性选择器，区分必要；并非对所有被认为有智慧的人、所有单次决定或全部智慧内容。合理的风险承担、有限证据下有根据但失利的判断，以及不要求始终选择未被实际比较击败者的实践，不能由这项全配置定理直接裁判。

另一种更丰富的“目标”可以把参与、维护和其他生活关系一并编码。本轮没有证明任何目标函数都无效；它证明的是**这些已给定的成就指标**不足。一旦对手加入所缺关系，就已经离开被否定的输入限制，必须给予完整比较信用。

<a id="fixed-rule-rival"></a>
## 4. 固定上层规则是一个成立的对手

`fixedRule` 复用原有判别：旧安排损伤参与且新安排保住维护时选择新实践，否则保留旧实践。在最后两类不可比配置中，保留旧实践只是一个未被击败的选项，定理不赋予其唯一优先或自动实施权。这个规则在整个给定族内满足形式要求，却没有在每次比较时改写自身。

因此应保留一个正面结论：**相同的规范根据可以支持目的改变，也可以支持目的保留；稳定的比较结构与可修订的操作目的能够共存。** 若一种固定目标或普通控制说明忠实表达全部有关关系，它不会因为术语不同而失格。它也没有因固定这一点获得伦理根据；此处的根据仍是明确采用的 G0/J/E。

“固定规则能实现”与“这些具体关系不必要”不是同一命题。前者已有成功见证；后者受到上述条件性必要结果限制。适当的根基论证需要说明双方共同保留了什么，而不是试图用目标变化本身排除所有固定上层说明。

本轮使用的是直接给定实际条件的选择规则。识别条件、形成目的、响应理由及改变支持已有[同史实现](GOAL-FORMATION-REVISION-INTEGRATION.md)；本轮信用归还该研究，未重建一个更简单模型来替代它。其识别准确性、资源、权限与动机前提不因被复用而消失。

<a id="constraint-and-reason"></a>
## 5. 这怎样推进“core 是 constraint”

可以把候选解释接为更具体的三个环节，而不将它们视作独立现实领域：

1. **形成关系有实际内容。** 哪种实践使参与丧失、哪种改变使维护中断、哪些替代保住这些条件，关系在共同展开中成立。给定目标的计数成功不能改写它们。
2. **公开根据使这些差别进入理由。** G0肯定生活及其继续生成，J2在其适用范围内给保护基本条件以优先。比较的伦理力量来自这些公开承诺与真实对应，不是来自任意关系都可写入一个类型。
3. **理由反过来约束目的及其形成。** 被评价的目的本身形成于这些活动，并继续影响它们。当其成功伴随被充分击败的损失配置时，成功不使它免于修订；反向配置又能支持保留。

这里不用为每一层“评价目标的目标”另造一套规范根据。目的取得、目标执行及规则改革均改变相同的生活关系，已有[跨层规范论证](GENERATIVE-ALIGNMENT-REVISION.md)使公开根据适用于这些作用。**这不是推出 G0/J2 的无公理证明，也不把无限反思设为智慧的前提。** 若修订 G0或J2自身，就在修改规范候选，必须公开变更和相应结论的依赖；本轮没有这样做。

所增加的解释力是：从“怎样达到目标”的条件，推进到“哪些真实差别不能被目标评价省略”的条件。它使 core 作为构成理由之关系根基的候选更具体，同时保留通用过程接口与实质生成理论的区别。**整个 core 的全部承诺不可缺少**，还不能由一对必要区别获得。

<a id="counterreview-and-sources"></a>
## 6. 作者反审与原典比较

本节是作者反审，不是独立 agent 验收。

**对手一：你把智慧偷偷定义成遵守J2。** 本轮没有定义智慧。所证的是满足该公开比较的必要信息关系。一个承认所有实际后果而拒绝J2词典序优先的理论，并未被数学证明为不一致。若要把此必要关系推广至全部智慧，必须另有独立的智慧刻画与实质桥梁；不能把接受J2写进“所有智慧”的定义。

**对手二：固定规则已经解释全部结果，你的根就没有贡献。** 这个对手在算法实现层成立，故本轮给出其正面见证。它仍使用实际保护、损失及比较关系；解释这些关系的形成与根据，是不同于实现某个映射的工作。是否必须采用整个生成理论尚待论证，不能因共享两项关系就把对手全部改名为本 core。

**对手三：选择器只是把答案读入。** 本轮的条件确实给定，规范比较也已存在；新贡献是跨表示的省略障碍与固定规则对照，不是发现伦理内容。实际取得、校准和响应来自已有研究，保持其条件范围。模型可指出一种输入不足，不能替应用者完成尚未成立的对应E。

**对手四：智慧常常在不确定中行动，为什么要求完美选择？** 同意这一界限。当前证明检验一种明确保证，不能把该保证强加给全部智慧。已有风险、有限认识及情境判断成果继续复用；本轮完成后不能凭增加更多全信息例子宣布覆盖了有限、默会、共同或观照的智慧。

本轮于2026-10-08核读两项原作者材料。均为链接式阅读，未导入原始字节、复现算法或实施历史盲测：

- Everitt等，[Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142)，2016，v1摘要：在其模型中研究自我修改及以当前效用评价未来的条件。该问题已有形式前例；摘要没有证明当前效用具有伦理正当性。本轮固定规则对照不宣称算法原创或推翻该研究。
- 亚里士多德，[《尼各马可伦理学》第VI卷](https://classics.mit.edu/Aristotle/nicomachaen.6.vi.html)，W.D. Ross译，重点核读§§9、12–13：文本区分达到既定目标的聪敏与实践智慧，并要求正确欲求、选择及德性。它还将使目标正确的作用归于德性、使手段正确的作用归于实践智慧，须保留这一分工。这里只支持成就不足以判定智慧的结构比较，不把其善、人性或灵魂学说等同于G0，也不宣称它已经提出我们的目的修订理论。

后一材料本来就是熟悉的哲学主题，本轮又是定点选读；因此只有解释比较价值，没有独立预测或跨文化收敛证据。它也保留了真实差异，不能只取“聪明不等于智慧”一句当作共同根已获历史证明。

<a id="verification"></a>
## 7. 实查与依赖账目

[源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/WisdomGoalGrounds.lean)、[隔离检查器](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_wisdom_goal_grounds.py)、[冻结回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/wisdom-goal-grounds-checks/20261008T120426.039061Z/verification.json)及[当前回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/wisdom-goal-grounds-verification.json)记录 Lean 4.29.1 的实际检查。新源码直接导入 `GoalFormationRevision`，递归导入 `PracticalJudgment` 与 `KnowledgeCorrespondence`；四模块均按冻结原字节编译并核对声明、定理签名与依赖。

| 范围 | 定理 | 显式声明审计 | 空报告 | 标准依赖报告 |
|---|---:|---:|---:|---:|
| 本轮 `WisdomGoalGrounds` | 7 | 11 | 4 | 7 |
| 继承三模块 | 93 | 165 | 104 | 61 |
| 本轮完整导入检查 | 100 | 176 | 108 | 68 |

新增7项定理中，5项仅报告`propext`，1项仅`Quot.sound`，1项同时报告二者；4项新定义为空报告。完整导入还包含继承的`Classical.choice`。无未完成证明、原生决策逃逸或编译警告。不是零公理证明，不是100项新定理，不是全仓库审计。规范承诺仍在解释层明示，不能从没有额外Lean公理推成伦理已无前提。

局部输入保留：给定的两种实践和两种成就判准、固定后果法则、保护项解释、J2/J1比较、确定性选择、全配置要求，以及菜单含两种实践。真正取得信息、获权实施、执行及生物／社会对应不在新定理中。继承模型的形成历史不被删除，本轮也不把静态选择器视作它的完整替代。

<a id="integration"></a>
## 8. 根基论证的整合位置

本轮完成了此前明确的一个检验：评价目的也有可定位的表示必要性，且最强的固定上层规则对手得到正面信用。结合上轮，可陈述两项已证局部事实：足够行动不必完整表示一切；但目标成就表也可能遗漏足以反转目标评价的关系。二者共同要求按声称兑现的内容辨明哪些关系必要，避免全知要求与任意简化两种过强结论。

**完整目标保持：证明 core 是智慧之根。** 现在尚未闭合的是从这些有内容的局部必要关系，到整个实质 core 在独立刻画的智慧范围中的构成地位，以及与已完成形成解释的充分接合。后续应直接核对智慧范围和构成承诺，复用风险与有限认识成果，不再以增加“会改目标”的控制例代替该连接，也不重开G0无公理证明作为门槛。

**Integration.** The target-evaluation test is complete under explicit premises. The remaining universal burden is coverage and constitutive necessity for independently characterized wisdom, including fallible and limited judgment, with existing formation and risk results credited. Neither the fixed-rule witness nor the omission theorem settles the whole root claim.
