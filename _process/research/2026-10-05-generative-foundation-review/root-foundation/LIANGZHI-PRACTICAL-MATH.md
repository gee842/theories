# 实际依存的有限交接：形式构造与证明范围

2026年10月7日，Asia/Bangkok。AI 撰写，支持[同一关切怎样改变回应](LIANGZHI-PRACTICAL-ARGUMENT.md)及 Ren 的[生生正面伦理方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)。**新增20项声明已实际通过 Lean 4.29.1 检查。** [源码与检查目录](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/README.md)保留固定语义、所有尝试及正式回执。

本轮形式目标是一个有限发生问题：**实际建立替代支承之后，原支承是否可以结束，而同一项活动仍通过新通路实际完成？** 它供应四情形规范论证中的一个有内容的中间回应，不把手段误认、目的改变、知情拒绝、既有承担直接编码为四个决定动作的标志。它也没有证明这些变化的内在形成或权限。

## 1. 既有结果已解决什么

既有 [PatientConcern](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/PatientConcern.lean) 的 `means_stales_same_patient`、`episode_stales_same_patient` 已处理作用关系和 episode 改变使旧记录失效；`permission_preserves_factual_packet`、`permission_retires_authorization`、`permission_toggle_does_not_revive` 已区分事实仍在与技术授权退役。[履行后撤回](FULFILLMENT-WITHDRAWAL-INTEGRATION.md)也已实际实现，不需要再次把停止程序称为首次能力。

[ReasonProtection](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/protection/formal/ReasonProtection.lean) 已有 `enforced_release_protects_requested` 与 `withdrawal_consumes_opportunity` 等有限释放、撤回和保护结果。其 `release` 检查一次 episode 的保护 mask，`withdraw/refuse` 关闭该 episode；它没有在这一接口中重建仍在继续的活动与另一支承之间的实际通路。[ClaimLedger](../../../../experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/protection/claims/formal/ClaimLedger.lean) 的 admitted 在所证 episode 中保持不变，实际记录可以认证履行，但新的规范修订需要另外有根据的操作。

因此本轮不声称首次完成一般交接或撤回。新增的是下面这条同一有限历史及其比较：未形成材料 → 支承及其依存活动 → 替代支承实际形成、接通、运行 → 原支承结束 → 活动继续产出并完成。形式上仅导入原核心、共同发生描述与 `PurposeCorrection`，没有重新编译庞大的评价架构，也没有宣称这些全部机制已组合在一起。

## 2. 模型语义在检查前固定

[SEMANTICS.md](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/SEMANTICS.md)在首次 Lean 检查前写定，之后仅追加反审要求的竞争历史。`SupportHandoff.State` 包含：未组装材料 `loose`、操作支持 `fuel`、第一／第二支承、工作架、实际连接、形成的产物数、实际失败操作数。

第一和第二表示本次形成顺序与接口位置，不是两个原始独立主体。工作架、支承、原料和产物都在同一状态中；本地规则说明它们如何形成与相互作用。本模型没有另设不受追踪的材料来源。

| 事件 | 实際条件与变化 |
|---|---|
| `assembleFirst` | 由一个未组装材料形成第一支承。 |
| `beginWork` | 第一支承已形成；另一个材料形成工作架，同时建立其第一连接，产物初始为零。 |
| `assembleSecond` | 另一个材料形成第二支承；装配本身不建立工作连接。 |
| `connectSecond` | 已形成的工作架与第二支承实际连接。 |
| `attempt port` | 尚未达到给定配额的工作架进行一次实际操作。所用支承及连接存在、且有原料时，原料减少一、产物增加一；否则不形成产物，`failedAttempts` 增加一。失败尝试仍是物理允许的事件。 |
| `dismantleFirst/Second` | 拆除实际支承、解除该连接，返还一个材料；没有要求原工作必须先完成。 |
| `finishWork` | 只有产物确实达到给定有限配额后，才拆解工作架并返还一个材料，解除连接。 |

每个实际事件消耗一个 `fuel` 单位，失败操作、接通、拆除也计入。配方、这些数值、二个支承位置、产物意义及完成配额都是明列的局部输入，不是生成根核的普遍原语。`finishWork` **只表示按给定配额的完成**，不是所有有根据的取消、退出或终结的唯一规则。这里没有以未达产量为由，推导休息、自护或合理终止不正当。

具体比较取初始材料6、操作支持14、配额3。装配3个组织各占1材料，3个实际产物各占1材料。材料总量为：

`loose + bit first + bit second + bit work + products`。

这是一项独立的有限发生规律，不是原 `FormedSelection` 化学模型的精化，不声称生物实现或复杂度指标。它不直接测量理解、福利、多样性或整体伦理质量。

## 3. 一般账与操作含义

`runnable_trace` 把逐项真实容许的事件词接到原 `Generative.Trace`。

`step_material` 与 `trace_material` 证明，每次容许事件及任意有限实际历史都保持上述材料总量。材料不是在交接时重置；拆除组件后可再利用，但已经形成的产物仍在账中。

`step_support` 与 `trace_support` 分别证明事件消耗一个操作支持单位，以及终点支持加实际事件词长度等于起点支持。`insufficient_support_for_word` 据此拒绝支持不足的**所指定词**；它没有宣称某词是全局最短路线。

`disconnected_second_cannot_produce` 检查只有第二组件并不够；连接仍是实际条件。`successful_attempt_constructs_product` 检查一次真正可运行的操作把原料变为新增产物；`unavailable_attempt_is_actual` 则检查失败操作真实发生、消耗支持且没有产物。本轮不把此失败数解释成体验痛苦或伦理伤害。

## 4. 同一历史中的形成、测试、交接与完成

共同前缀从无组织开始：装配第一支承 → 形成工作架和连接 → 经第一支承实际形成一个产物。到达 `prepared` 时第一依存实际存在，第二支承尚无。

随后装配、接通第二支承，并**先经第二连接形成第二个产物**。到达 `tested` 时两条连接都实际存在。此时拆除第一支承，工作架仍在、产物只有2；最后经第二连接形成第三个产物，再完成工作并拆除第二支承。

`formation_and_dependency_are_actual`、`replacement_is_assembled_connected_and_tested`、`original_support_ends_before_real_completion` 分别检查这些真实片段。第三项将原支承结束与活动实际完成放在不同时间；没有先让活动完成，再称作正在继续的活动获得交接。

`whole_handoff_preserves_material_and_support` 检查从无组织初态到最终结束的完整 `Generative.Trace`。十个事件之后，三个产物保留，三个材料重新处于未组装状态，全部支承和工作架均结束；操作支持从14变为4，失败操作为零。

这证明一个具体共同可实现性：**原参与结束、后续操作仍实际完成**可以在同一历史成立。它不是二者无代价，也不证明这条路线比每条替代路线整体更丰富或在伦理上总是优越。

## 5. 实际失败、恢复与先拆后建的真实竞争史

`early_exit_reaches_an_actual_failed_attempt` 从同一个 `prepared` 出发，先拆第一支承，再真的在该已拆连接上进行一次 `attempt.first`。无产物增加，失败计数成为1，支持仍消耗。它只说明**这一条真实操作词**的结果；没有把一瞬间连接缺失本身记为伤害。

`recovery_can_complete_the_same_activity` 保留修复路线：从这个真实终点装配、接通第二支承，实际完成剩余两个产物，再结束。最终仍有三产物、全部组织结束、材料总量6、支持3，失败计数保持1。没有把中断说成永久不可恢复。

更重要的竞争史由反审补出，并已实际检查。`replacement_after_removal_can_complete_without_failure` 先拆第一支承，然后装配并接通第二支承，**再开始**两个剩余操作，同样完成，失败计数为0、支持为4。这说明本地规律没有要求替代支承必须先于旧支承的拆除。规律没有墙钟、连续需求或期限事件；装配空档不会自动产生失败尝试。若要研究持续生命支持等有时间压力的情形，须另给真实发生规律，而不能把它们暗中加入当前见证。

`later_recovery_does_not_erase_failed_occurrence` 对原 `PurposeCorrection.actual_violation_not_erased` 作具体实例化：早退后实际失败的发生描述和恢复史相接，仍是同一完整历史；它不能同时被认证为每次发生前后都满足 `NoFailedAttempt`。此处 `NoFailedAttempt` 只是 `failedAttempts=0` 的操作描述，不是 `Good` 或规范义务。

发生记录来自 `CoupledOccurrence` 对实际前后状态的数学描述。它不是新装配的内部记忆，也没有新增被影响者的经历假设。其作用是保留那次**已经真正发生的失败操作**，不把成功终点替换成另一条从未失败的过去。

## 6. 真实有限终结与支持不足

`real_completion_needs_no_replacement` 给出另一整段历史：从没有组织、支持仅7开始，形成第一支承和工作架，经第一连接实际形成全部三个产物，完成工作并拆除原支承。第二支承从未形成，活动仍真实完成；终点留下3个产物、3个未组装材料、支持0，全部组织结束。

`low_support_blocks_handoff_but_not_finite_ending` 同时保留：这7个支持单位足够上述有限结束路线，却不足以运行所声明的十事件交接词。这不是所有替代交接均不可能的下界证明，更不是要求无论成本如何都建立后继。它让本轮正面生成解释保留一个真实限制：在选定条件中，直接完成可以比所示交接节省支持。

## 7. 对四情形与生生方向的实际贡献

本结果将根论证中的交接候选变成可检查的发生，而非把 `permission`、`admitted` 或 `fulfilled` 翻转后宣布问题解决。依存活动从材料中形成；替代通路需要新的装配、接通与真实运行；退出前后的可行操作因这些关系而不同。它也保留修复、等待后再接通、有限完成以及不足支持。

对 Ren 的正面方向，这说明改变关系可以形成原固定参与之外的一种实际继续；它不给当前产物计数冒充“更多生”的完整含义。模型没有多样性或复杂组织持续增长指标，也没有比较有害活动、生活方式、生态负担和不同生的范围。**从因果依存到有根据的接续责任、从这种共同可实现性到整体更丰富的生，都需要[根论证](LIANGZHI-PRACTICAL-ARGUMENT.md)所明列的进一步评价。** 原义务是否成立、谁来交接、拒绝是否取消某个权限、何时合理结束，没有被这里的事件 guard 定义为真。

因此本轮是生生实践方向的一项有限机制支撑，不是四情形的自动道德查表器、本然良知的生物实现或无假设普遍证明。它也不占用其他研究中生成树、无限接续与无上界复杂化的证明任务。

## 8. 实際验证、依赖与失败记录

[check.py](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/check.py)从既有 `purpose-verification.json` 核对所导入源及固定编译器，冻结四个模块、检查器与语义契约，在新临时目录编译。检查编译器为 Lean 4.29.1。正式回执记录源、日志、检查器、语义契约及编译器 SHA-256，并要求新 theorem 全部有命名公理审计，拒绝证明占位、自定义公理及跳过内核的原生求值。

最终成功尝试为 [1791378712930201000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/checks/1791378712930201000/receipt.json)，[正式回执](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/verification.json)共65项审计：核心18、共同发生描述7、既有目的历史接口20、本轮20。新增20项中10项的命名公理依赖为空；另10项仅使用标准 `propext`，其中算术结果另外使用 `Quot.sound`。没有自定义伦理公理或证明占位；发生规律、配额、材料语义和规范解释仍是前述实质输入。

保存的失败依次是：

1. [1791378482224854000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/checks/1791378482224854000/receipt.json)：检查器前置扫描误把既有注释中的 `unsafe` 当作代码，尚未调用 Lean。改用既有 purpose 检查器的注释剥离函数后继续。
2. [1791378482401590000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/checks/1791378482401590000/receipt.json)：首次实际编译含记录语法、保留字 `prefix`、布尔引理调用及合取排列错误，产生后续 elaboration 诊断。修复的是表达与证明实现。
3. [1791378575636007000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/checks/1791378575636007000/receipt.json)：其余声明通过，一项通用支持证明将 dependent case 的命题 binder 误认作接口位置。改为先证明实际更新的 fuel 投影，再应用自然数算术。

最后一轮同时加入反审要求的先拆后建竞争史；原事件律和已有结论未变。前置失败、每次实际编译的源快照、日志和回执均保留，失败日志内 Lean 继续诊断产生的 `sorryAx` 不进入成功结果。通过后的源 SHA-256 为 `c80dd58859388aacb730afb429f94931fe3172eecc2784d46dc7012882301159`；正式回执 SHA-256 为 `670fda19556251e6594d117483f9d7ca90da0f1ab77968c4964ca288e0ae6364`。
