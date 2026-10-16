# 良知校准研究：实验对照与既有形式结果的精确对应

2026年10月7日，Asia/Bangkok。AI 撰写，接续[规范根据接口](LIANGZHI-NORMATIVE-WARRANT-INTERFACE.md)与[已完成的发展机制](LIANGZHI-DEVELOPMENT-MATH.md)。本轮审查 **Hepach 等（2016）与 Martin、Olson（2013）的实验对照，对处境理解、回应纠正和关切解释究竟提供什么支持**。实验细节依照本轮原始来源审读者的[来源核读](LIANGZHI-CALIBRATION-SOURCES.md)，此形式审查不另称独立复读论文或重分析数据。

**结论：既有已检查接口足以表达本轮所需的区别，没有必要新增一个评分模型或不可识别性定理。** 两研究提供的对照有助于区分请求或动作表面与目的相关的物件、手段关系；它们尚未满足把实验直接代入任一伦理正确性定理的对应前提。本轮没有新增 Lean 声明，也不把下述对应审查称为新的伦理证明。

## 1. Hepach 等：表面伸手停止，与取得相关物件不是同一读出

视频对照中，成人接过相关或不相关物件后，都停止伸手并坐正；非社会动画也保持相同物体运动。这使「只对伸手是否继续作反应」与「区分物件对先前活动的相关性」成为可比较的解释。瞳孔结果的实际范围是初始唤醒与物件相关性的交互，不能改写为所有儿童对未被帮助者都显示同一种差异。瞳孔扩张也不是直接测出的伦理判断；惊讶等解释仍需比较。

现场捡物结果可支持先处理相关物的偏向，但儿童仍继续捡不相关物。**这不是实验已经实现的“要求满足后停止帮助”结果。** 视频中的成人停止伸手也没有显示最终堆放目标已完成，更没有直接测量福利改善。两阶段有重合参与者和固定先后次序，不能算作两项相互独立的复制。

对应时应避免把 `some true` 简单指定为「成人接过了任何物件」。在履行模型里，true 的服务意义已经是所计要求的一次真实实现。若实验所问的是相关物是否使活动能够继续，仅凭收到物件就把它计作履行，会把待判断的关系写进错误的记录解释；若所问只是一项“递过任意物件”的约定，它又是另一项要求。原始对照有助于查明儿童是否区分相关性，不自动决定哪一种要求有伦理效力。

## 2. Martin、Olson：同一坏物件在不同活动中的适用性

第一研究比较功能性与失效物件的请求，儿童对后者较多提供另一可用物件。丢弃任务的对照显示，坏物件本身不会普遍引发替换。第三研究进一步让同一个坏杯、玩具电话在另一个活动中成为可用手段：杯子可切面团，电话可压纸。回应随当前活动的适用性变化，削弱了「遇到坏东西就换掉」的简单解释。这里的任务和物件配对在儿童之间平衡，并非同一儿童对同一杯子经历现场目标改换；研究没有追踪新目的的形成或同一历史中终极目的的修订。

最切近的解释是：儿童的反应可以同时涉及先前表明的活动目的、所请求的具体物件，以及该物件是否能在这项活动中起作用。这是对“服从请求形式”与“理解所涉活动”作出的有内容比较。所用“坏”不是一个脱离活动而固定的负面本质。

这仍不等于判断成人的生活目的是否正当，或证明儿童有权替代一个知情成人的明确选择。作者将结果限定为提供另一手段，没有测试成人已经知道手段问题、仍坚持该选择时的强 paternalism。该实验也没有交叉操纵儿童的后续控制收益，不足以单独排除理解准确、行为相同的策略性控制解释。

## 3. 可复用的已检查接口及其未满足前提

下表列出的定理是既有结果。右栏不是附带免责声明，而是决定能否真的取得一个 theorem instance 的必要对应工作。

| 既有源文件与精确声明 | 本轮可以复用的区别 | 实验尚未建立的对应 |
|---|---|---|
| [FulfillmentStatus.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/succession/fulfillment/formal/FulfillmentStatus.lean)：`fulfilled_iff`、`pending_iff`、`unknown_iff` | 真实履行史与可访问记录不同；只在所有相容历史均满足／未满足同一固定要求时，记录才能分别认证这两种状态。 | 尚未给出儿童内部记录到 `List (Option Bool)` 的对应、记录忠实性、机会分段以及固定 `k` 的服务意义。Hepach 的视频没有给出已完成最终目标的履行史；Martin 的选择也不是规定数量服务的完成证明。 |
| 同模块：`forged_record_misleads` | 某个正记录本身不保证实际履行；需要真实相应关系。 | 论文没有伪造该形式模型的 episode-bound receipt，也没有证明实验中的姿势或请求是这种记录。不能称该定理已被论文直接验证。 |
| [SemanticCalibration.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/transport/calibration/formal/SemanticCalibration.lean)：`replay_corroboration_is_compatible`、`grounded_corroboration_is_compatible` | 提供由已取得且适用的关系支持后续认可的条件保证；`Sound`、稳定对应与实际接受是充分条件，replay 给出一种取得路线，不证明它是唯一必要渠道。 | 论文没有证明儿童按该 binary updater 取得 registers，也没有确定全部相关情境保持同一个二值作用律；此处不应把坏杯的跨活动变化归为同一未变化 law。 |
| 同模块：`self_import_guarantees_agreement_without_calibration`、`stale_qualification_can_accept_old_error_and_decline_new_truth` | 把待检验内容直接写进作为凭据的记录会制造循环认可；失效的旧资格也可拒绝新事实。 | 请求的作用不能未经论证就等同于形式操作 `importClaim`。这些是校准协议的已检查边界，不是儿童实际内部机制的诊断，更不是一般同意不可靠的定理。 |
| [AcquiredPurposeCriterion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/AcquiredPurposeCriterion.lean)：`actual_repair_identifies_common`、`learned_criterion_fits_repair` | 从实际活动后果取得对继续条件的认识，可以形成可操作的要求；这种结论有声明的候选规律族。 | 原定理使用原生 repair 的真实状态转移与单通道消耗族。儿童实验没有这些类型、消耗律或相同训练史，不能把物件功能理解当作已构造的 chemical repair 实例。 |
| 同模块：`successful_repair_does_not_exclude_fallback`、`fallback_has_a_genuinely_different_continuation` | 成功样本只在所检验的规律范围内有区分力；原模型保留一个在已有样本上相符而在另一支持条件下不同的实质替代。 | 本轮实验没有提供该 source-funded fallback。它提示明确写出竞争机制与区分条件，不支持随意添加一个永远模仿结果的隐藏动机来取消一切经验支持。 |
| [SituatedPractice.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/SituatedPractice.lean)：`enacted_ready_fits`、`sound_response_iff_common_continuation`、`incompatible_histories_obstruct_response` | 所用描述是否足以支持可实现的适切回应，须在完整的实际历史及其继续中考察；共同描述不能略去决定回应的关系。 | `Fits`、有限可行响应词、所有相容历史与 readout 均须另行确定。上述实验是有限统计证据，不是穷尽全部 realization 的稳健选择证明，更没有证明一个伦理 `Fits`。 |

这些接口与实验的联系是**带有明确未完对应的解释关系**，不是新的定理实例。尤其不能以给定 `Fits` 或 fixed claim 完成了数学检查，反过来证明它们表达的伦理判断正确。这里把作用、记录和评价分别分析，是为了说明同一活动中的关系与推论，不把它们放进互不相关的事实／价值领域。

## 4. 不重开已完成机制，也不把新证据压成没有贡献

[实际履行后撤回](FULFILLMENT-WITHDRAWAL-INTEGRATION.md)已经有明确支持的记录、改变的推荐、待履行／已履行对照及伪造失败。[自模型认证](PLURAL-CLAIMS-INTEGRATION.md#2-certifying-fulfillment-with-a-self-model)中的 `self_model_certifies_more` 与 `needs_stationarity` 也已说明，实际更新规律能够增加推断内容，但需要稳定作用律与两次机会实际发生。它们不是本轮还需要从零构造的能力。

另一方面，两个实验也不是对这些工程构造的直接生物实现验证。新证据的贡献在于真实的对照：同样停止伸手时仍区分物件相关性；同样坏物件在不同目的关系中引出不同回应；请求形式与可用手段可以不同。这些区别支持比纯动作匹配或固定物件分类更丰富的理解解释，也给后续关切假说提供需要一起解释的观察。

这种支持可以是可撤销的，不需要先排尽任意想象的动机才成立。其进一步伦理意义仍需说明：被理解的活动及承受为什么构成有根据的回应，哪些目的或权限应当修订，什么情况下应尊重知情选择、履行已有承诺或保护自己。准确追踪真实处境也可服务于控制，故技术校准不自动就是伦理校准；反过来，存在控制解释并不自动取消经过具体对照支持的理解或关切解释。

与[上一轮发展模型](LIANGZHI-DEVELOPMENT-MATH.md)的剩余生物对应也须保留：尚未从儿童这些干预数据识别与复制 carrier、held rig、gate、sample/capture/bind 相同的结构；没有证明该组织沿同一实际发展史被再形成，也没有给出遗传、发育与群体选择的完整连接。上一轮检查保证局部模型的真实运行，本轮实验使功能性解释更有内容，两者尚不能自动合并为本然良知已被普遍推导。

## 5. 本轮不采用的评分提案

调查中曾提出把「未履行、熟悉线索、后续控制收益」放进一个非负线性二行动评分族，再求全因子干预下的辨别条件。经过反审，本轮不采用：这两项原始研究没有该三因素交叉设计，也未支持该线性族，新增它会先给出所需结构，而不是解释当前证据如何校准伦理辨识。

该提案没有实现、没有经过 Lean 检查，也没有用于任何结论。它仅是被放弃的研究建议，不是数学反例、失败定理或失败实验。没有新增数学义务时，复用已检查接口比另造一个正确但不对应此处证据的界更合适。

## 6. 原证明绑定的只读核验

本轮未修改 Lean 源、未重复编译、未重跑实验。对最相关三个已通过回执作了只读核验：

| 回执 | 本轮核验内容 | 结果 |
|---|---|---|
| [wang-practice-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/wang-practice-verification.json) | 3个模块的当前源与旧编译日志 SHA-256、所记编译器 SHA-256 | 全部匹配；包含 `SituatedPractice`。 |
| [criterion-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/criterion-verification.json) | 4个模块的当前源与旧编译日志 SHA-256、所记编译器 SHA-256 | 全部匹配；包含 `AcquiredPurposeCriterion` 与 fixtures。 |
| [SemanticCalibration 的 verification.json](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/transport/calibration/formal/verification.json) | 4个模块的当前源与旧编译日志 SHA-256、所记编译器 SHA-256 | 全部匹配；包含实际 recipient feedback 依赖。 |

对应回执本身的 SHA-256 分别为 `aae5d070d36a8152e307b831b49fc3ace84e611cd20a9389df99852aac97e454`、`86533fadfffa399b7f051622cd30fb7b1a5c14fc75586470c02aa60fa1ec6905`、`2bc0000d45d027eb33484aaae52ea867b1898b7da023b3975f4195e9f869d14f`。模块数按每个回执计，包含重复核心，不能相加当作11个不同的新模块。

`FulfillmentStatus` 与 `SelfModelCertification` 本轮精读当前源码和既有[7日重建记录](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal/inquiry-warrant/BUILD.md#addendum-7-october-2026-empty-axiom-reports)，保留该处已检查状态；本轮不把旧历史源码哈希当成最新重写源的绑定证据，也不额外宣称完成了这两个模块的新编译审计。上述核验确认已有形式接口的来源，不提高实验或伦理推论的证据等级。
