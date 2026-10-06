# 从形成的活动关系取得适用范围：形式账

6 October 2026。AI 撰写的形式账。实现为 [AcquiredActivityScope.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/AcquiredActivityScope.lean)，遵循[共享非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)。[新鲜形式验证](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/scope-verification.json) 已通过：以下分别报告通用声明、九例原生保存历史以及两条另外构造的 Lean 历史。

承接 [上一轮判据形成](YITI-REN-CRITERION-MATH.md)。上一轮真实修复的支持差分进入记录，改变了完成判据及实际后续行为；但 `laterRepair` 仍是输入的适用范围。新连接所要解释的是：**实际形成且尚可继续的活动关系怎样进入记录，改变取得的适用范围，以及单项活动结束以后为什么不能把其余活动或既有结果一并消去。** 这与重新证明计数不足以完成、重新安装另一个范围位不同。

## 同一历史中的材料结构

起点仍是上一轮真实材料祖先及训练路径，使用 `trained(laterRepair=false)`：修复通道已经取得，旧判据的范围激活没有预先打开。新 reader 与两项活动都由原有自由 A/H 部件形成，占材从原生可用容量扣除。选择、接触与结构形成所需的支持也留在同一账中。

活动 A 的初步反应消耗局部支持并改变原生界面，使其留下未完成的物理阶段。该阶段的产品反应再次需要局部支持；在已损界面且局部支持为空时，原生修复和捕获成为实际的中间条件。这个损伤来自前一步反应，不是因为一个分析者安装了“以后要修复”的目标位。活动 B 的继续反应走共同支持通道，保留独立可检验的反应条件。

相位不是独立宣告的好坏：形成、中间物、产品和解离分别改变哪些反应仍可发生、材料在哪、哪些支持已经消耗。产品继续占材；解离返还未成产品的材料，不能退还已经消耗的支持或抹去界面损伤。

## 范围投影保存什么

取得的记录由有成本的接触形成，随后读取记录而不是读取旧 `laterRepair` 配置来选择可继续的反应。范围是这个取得记录的投影；完整状态保留实际相位、产品和材料、既有训练结果及支持账。

两个区别必须同时保存：

- 产品形成与解离都可以解除该项活动的未完成范围，但只有产品形成给出产品。范围为空不能推出全部完成。
- A 的范围解除不意味着 B 的实际反应也已结束。局部终止不得从状态或记录中删除 B，也不得回写过去已经发生的反应。

错误、缺失、过期接触与相同记录下的 reader 阻断是实际机制对照。它们检验取得范围的行为作用，不是通过任意设置一个伦理谓词来反驳更完整的非二元整体。

## 已证明的层次与限制

新过程直接接入 `Generative.Process/Trace`。`inherited_training_is_actual` 保留 `laterRepair=false` 的真实训练；`admitted_is_actual_trace` 把守卫通过的实际事件字连接到核心 trace。`admitted_native_is_original` 对显式 `.plant e` 证明扣除旧 recorder、新 reader、在持有相位的活动部件之后的原生守卫和状态变换。所选计划的 `.act` 每次只执行一个守卫通过的原始步骤；其原生投影在这批有限历史中核对，不把前一个定理扩大成任意 Python 或任意 `.act` 的精化定理。

`priming_changes_actual_continuation` 从实际获准的 A 初步反应推出中间相位、界面已损与局部支持为空，因而原生捕获和直接形成产品都被阻断。`ending_A_preserves_B` 是两个结束变换保留 B 相位和记录的字段性质，实际结束的发生另由 trace 证明。`legacy_activation_does_not_choose` 证明新选择不读取旧 `criterionActive`；新配置根本不接受 `laterRepair`，但仍接受明示的接触与 reader 对照配置。

`trace_preserves_history_and_products` 对任意获准历史证明已有 A/B 产品及旧 count-completion 历史不被后续活动抹去。`depleted_common_blocks_every_B_completion` 给出更强的失败保留：一旦共同支持为零、B 仍是中间物，本轮任意获准后继历史都仍然共同支持为零、B 未完成；既不能形成 B 产品，也不能免费解离它。这是针对本轮反应律的结果，不排除另外形成补给能力的新规律。这里没有宣称新的全历史支持守恒定理；各保存历史的完整账由对应证书及独立重放核对。

这里解释**物理活动范围的形成与取得**。这还不同于对一项活动的承担，更不同于承担的规范正当性。取得的可继续性不自动要求继续每一项活动；解离不能仅凭相位编号就一律判为善或恶。合理拒绝和适当结束的普遍条件仍须更完整的关系来判断。

## 有实际来源的对照和范围终止

[保存的原生结果](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/continuing-dependency/scope-results.json) 有九例：完成后的真实/过期/缺失接触和 reader 阻断；解离后的真实/过期接触；未完活动的真实/错误缺席接触；入射支持真实耗尽。每例都从同一个已有训练端点开始，再实际形成 reader 和 A/B 结构。真实与 clamped completion 分支在选择前完整 36 坐标相同，读取策略不同，故分别继续 B 和浪费支持于已经结束的 A；后一条失败保留到产品反应的实际守卫。

这里必须保留记录滞后的边界：保存的两条完整结束原生历史在 B 产品形成以后没有资源再接触 B。因此它们的实际 pending 已空，取得的记录仍保留 B；不能把实际结束写成免费自动更新的记录。`actual_empty_scope_has_different_products` 另给两条 **Lean-only 富支持历史**，均从同一个真实训练端点出发，没有从耗尽端点重置资源。它们不安排那批大量泄漏，实际完成 B 后仍有支持执行 `contactB`，由此实际范围和取得范围都为空。一条保留 A 产品，另一条保留 A 解离、返还的 A/H 材料而无 A 产品；两者都保留 B 产品、此前 count-completion 和真实界面损伤。两条分别含 17 和 15 个新增事件，不能计入九例 Python 保存历史。

范围取得与选择的表示也有清楚边界：phase 1 和 2 都在 pending 投影中，但本轮选择配方处理已 primed 的 phase 2；未证明对任意刚形成活动都能自行发明下一步。所选计划不是全局强制执行器；过程仍允许明确列出的其他原生或结构事件。不存在由范围变大自动推出改善或更高规范价值的单调性定理。

## 新鲜验证与来源绑定

[check_scope.py](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/check_scope.py) 不导入或运行原生 producer。它从冻结结果生成祖先、旧训练和九条新历史的 Lean 命题，核对每个事件守卫、完整状态序列和最终状态、各实际到达点的拒绝及 actual/acquired pending。另有同状态 reader 对照声明。原生实现及依赖源码由结果中的哈希绑定；编译在隔离临时目录运行，旧与新 Lean 源码、生成命题和日志均保存。

首轮 fresh build 的四个源模块通过，生成 fixture 模块在输出声明审计前发生线程栈溢出。[失败收据](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/scope-checks/1791287398620303000/receipt.json) 保留。[成功构建](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/scope-checks/1791287626704976000/receipt.json) 使用同一固定 Lean 4.29.1 编译器明示支持的 `-s 65536`（64 MiB 线程栈），实际参数已写进收据。两轮全部 Lean 源码与生成 fixture 的哈希相同，没有删除事件、坐标、守卫或失败对照。首次失败是验证资源不足，不是过程的科学反例。

成功构建核对九例中的 **2,920 个新增事件、2,929 个完整 36 坐标状态、4 个拒绝**，加上共享的 94 个祖先事件和 22 个继承训练事件。五个模块合计 106 条声明审计；其中新源文件 14 条（含辅助声明），生成对应证书 12 条。它们是审计计数，不是 106 项独立发现。全部输入在构建期间保持不变。新声明只依赖标准 `propext`、`Quot.sound` 和 `Classical.choice` 的子集，没有自定义公理、证明缺口或 `native_decide`；这不表示局部物理律、接触构造和逻辑前提消失。

## 依赖来源

| 项目 | 本轮的来源或状态 |
| --- | --- |
| 修复的共同支持依赖 | 继承真实修复差分、有限家族取得及其既有对照 |
| 活动结构、未完阶段、产品与解离 | 新局部材料反应律及实际形成历史；反应律仍给定 |
| 活动范围信息 | 有资源约束的实际接触；接触校准与有限表示方案仍给定 |
| 哪种取得记录引导哪项反应 | 明示的局部 reader/选择构造；并非从零取得全部构造律 |
| 起始资源与实际事件安排 | 既有祖先加新增形成/接触路径；初始条件和安排仍给定 |
| 旧 `laterRepair` 范围输入 | 新选择路径不再读取；继承字段保留但不参与选择，实际关系接触进入新记录 |
| 规范正当性、普遍有利方向 | 本轮不据此宣称证明 |
| 形式逻辑与数学工具 | 仍使用 Lean 的逻辑基础；无自定义公理不等于无前提 |

给定局部反应律并不意味着该律在生成实在之外；它意味着这份形式表示尚未解释它自身的形成。新证明应准确关闭它实际解释的连接，同时把这项剩余解释义务留下。
