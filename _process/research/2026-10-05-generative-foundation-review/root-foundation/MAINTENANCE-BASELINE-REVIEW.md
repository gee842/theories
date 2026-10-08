# 维护参照不能被自身撤除改写：独立反审

2026-10-08。AI 独立反审，沿已有 G0/J 公理路线。按[本轮协议](MAINTENANCE-BASELINE-PROTOCOL.md)，这里只检查 `ChanceAdequacy` 的一类具体对应错误；不把它称为新的 J3、普遍反操纵原则或旧定理的反例。**独立验收：接受**，范围是下述任务对应纠错与实际检查的条件性应用。

## 1. 先关闭重复的研究入口

已完整核读[时间变化中的检查](TEMPORAL-INSPECTION-INTEGRATION.md)、[共同接续](JOINT-CONTINUATION-INTEGRATION.md)、[纠正交接](CORRECTION-HANDOFF-INTEGRATION.md)、[版本化请求](VERSIONED-CORRECTION-INTEGRATION.md)与[变化支持](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md)。逐次失实记录与动态候选覆盖、失败前缀与费用保留、共同作用和共享资源、旧版本请求的历史、准备与实际完成的区别均已有成果。`EffectiveCommand.revoked_before_execution` 及取得纠正路线中的当前撤权与费用保留，也已检查。不能仅再添前缀、漂移、权限或损失字段就声称接通新的一般机制。

这些成果没有独立认证一个指定现实安装的变化律、记录及权限组织。当前实现线的实质证据边界在这里：还需要实际关系的根据，而不是一个新的谓词名。继续以供给机制重写相同定理不能越过这个边界。

本轮选出的更窄问题有明确位置：**评价接管是否兑现仍有效承担时，不能把接管已造成的能力丧失，直接代入原任务的参照，借目标变空来报告完成。** 这项规范根据已经在 [J3 与目的修订](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PRACTICAL-JUDGMENT.md#6-目的变化学习与结束责任--changed-purposes-learning-and-discharge)、[机会充分性论证](CHANCE-ADEQUACY-ARGUMENT.md)和[先前反审](CHANCE-ADEQUACY-REVIEW.md)中明示。风险修订的 `resetting_allowance_exceeds_original_scope` 也已给基准反复重设的独立诊断；本轮只补特定维护判定的操作控制，不能重复认领一般原则。

## 2. 必须区分的三种判断

当前路线能否工作，是能力问题；原任务是否实际履行，是历史与效果问题；原任务是否仍正当且有效，是规范问题。三者相关，但不能直接互换。

如果路线真的被撤掉，报告当前不能工作可以完全准确。错误发生在把这个准确能力报告用于另一项主张：既然现在不能工作，先前仍有效的保护便被算作没有要求，因此任务已经完成。剩余责任不创造资源，也不推出当下必须完成不可能的操作；它可能要求有范围的修复、交接或如实承认未满足。

相反，原要求若确实只保护特定窗口、有合法退出条件，或后续事实使原目标失去根据，就不能无限冻结初始任务。原有合法安排也不自动享有永久机会份额。自然失效可以改变可行回应，但不独自证明已经履行，更不自动清除修复或其他救助理由。

## 3. 最强反对与正面控制

**行动造成目标减弱，不一定有错。** 治愈可以真正解除需要，交付可以完成任务，有根据的结束可以取消未来要求。若原则禁止所有由行动造成的目标变化，它会错误禁止这些正面结果。本轮保留实际执行完成交付、随后允许旧路线退役的正例，不能把旧路线永存写成善。更长的持续替代仍须使用相应既有机制及其独立对应，不由一次交付推出。

**表面需求消失也不一定是治愈。** 删除报告、破坏表达条件、使受损生活无法再进入评价，也可能让某个需求字段变假。仅凭 `demand = false` 不足以区分真实缓解与遮蔽。正当释放须有其地位、范围及程序根据，不能由自设 `released = true` 消掉他人的残余要求。这里复用已完成 J3，不新增一个带任意标签的规范守卫。

**新增能力不等于实际完成。** 一条替代路线可用，说明存在某种支持方式；任务已完成则须有实际履行。肯定见证应让完成记录由有效支持下的执行产生，再展示旧路线退役并不抹掉该记录，而不是由“愿意接管”直接设置完成。

**参照保持也不等于规范正确。** 在固定、仍有效任务下，证书传递要求保留该任务的内容；其一般包含逻辑只是条件推论。若一项真实改变正当地修订了任务，须说明新的规范范围，再判断履行，而不是对任何旧目标无条件要求字面保持。

## 4. 实查与完成范围

已独立完整核读冻结的[源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/MaintenanceBaseline.lean)、[专用检查器](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_maintenance_baseline.py)、[肯定论证](MAINTENANCE-BASELINE-ARGUMENT.md)、[证明说明](MAINTENANCE-BASELINE-PROOF.md)与[整合](MAINTENANCE-BASELINE-INTEGRATION.md)。本轮不新增原典读取或经验测量，[此前来源](CHANCE-ADEQUACY-SOURCES.md)保持原范围。

实际 Lean 4.29.1 [回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/maintenance-baseline-verification.json)记录运行 `20261008T121326.478309Z`：**4 项新定理／13 项新声明审计**；`AlignmentInquiry`、`ChanceAdequacy` 和 `ObservableContinuation` 的 **21 项继承定理／55 项继承审计**单列，未重新算作新增。逐一检查全部声明扫描、精确导入、签名及依赖日志，核对四个现行模块、两个检查器、全部 **29 项保留产物**、顶层与保留回执的相同字节，以及记录的 Lean 二进制哈希。三个附加例确已内核检查，未加入新定理数。新声明中 11 项空依赖，1 项仅 `propext`，1 项含 `propext` 与 `Quot.sound`，没有自设公理。**未另运行 Lean 编译器**；本次独立验收依据实际编译产物与对应源码，不冒称第二次执行。

实质核对结果如下：

- 退役确实禁用左路及包含左路的并行操作，需求和未交付没有被偷偷改成完成。缩小后的目标通过与原目标失败同时成立，故检验的是对应误用，而非旧定理无效。
- 正例从指定初态调用实际响应并扣除预算，先形成交付记录，再退役。原左路成功模式已交付；另一模式在单左路例中仍未服务，不能因此取消其其他理由。并行例扩大的是此次交付事件，不是退役后持续能力。
- 通用传递条件容许“同任务真正完成”或“当前仍待覆盖”两条路径。完成记录与实际交付的对应、原任务有效性均显式保留，不能由记录名取得；不要求所有旧目标永久原样存在。
- 自然数质量界只使用共同正总量下的有限事件表示。原目标质量一、裸退役交付质量零，以及先并行交付质量二均吻合源码；没有另外证明任意实数概率、不停供保证或新的伦理权重。

现行 [ChanceAdequacy 对应说明](CHANCE-ADEQUACY-CORRESPONDENCE.md)的一段定向修正已经反审：原通道失效必须按原任务和有根据的比较条件判断，不能自动采用本次撤除后的能力。该段同时保留当前不可能、真正完成、修复和有根据结束的区别。已核[变更记录](MAINTENANCE-BASELINE-INDEX-EDITS.json)首项所存原文、改文及前后哈希，并以单段反替换恢复原哈希；其他内容保持。旧 8 项定理／14 项审计及其历史验证不变，本轮不追认新版本为旧时已经读过的版本。

验收绑定的新源码 SHA-256 为 `48d26515db6aa2a4e2692e22e1eea1586c95090b139d2a728a21031a8bd3ca77`，专用检查器为 `360814559168e7adc0defbab761d3910238c64656f68f8f8e5d3abb018c1a635`；论证为 `4e302947d6e98b9bb367bc14ec0699e5dc9891ebaa979bb2126b9c15e654919a`，证明说明为 `2697cb4538d77d85e2b00a3da00d38e0b7b380555b60bed7e34e2c264602d232`。范围检查接受的是这一窄应用，不是对实际装置、全部正当变更或普遍伦理的完整认证。

这项具体对应审计完成后，应关闭该实施诊断。下一中心规范问题回到**没有此前受保护承担时，初始机会怎样才充分，以及哪些合法裁量允许直接选择**。不能以再找一项旧基线或增添另一个控制器不断推迟这个未解比较。
