# 王阳明整合的形式支持：整体历程、应境分辨与实际实现

2026年10月7日，Asia/Bangkok。AI 撰写。回应 Ren「先完成王阳明」，支持[王阳明主文](../../../../theories/becoming/chapters/WANG-YANGMING.md)的整体重构。**新增 Lean 检查已通过；结果是已有生成过程上的表示充分性与实际实现的条件，不是阳明伦理的普遍证明。** 本文不把「真知」定义成必然善行，也没有新增善恶公理。

本轮真正检验的推论是：如果把知与行理解为同一实践的分化，那么一个只保留某些准确报告的表示，何时足以支持对整个后续历程负责的回应？其一般形式必须保留已发生的变化、实际可行性以及整段展开；若只分别证明局部响应可能，不能直接合成整体响应。该问题为普遍伦理研究提供**表达与实现的对应条件**；它不供应首个伦理根据，也不代替首个根据的辩护。

## 1. 复用的模型和本轮增量

新文件 [SituatedPractice.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/SituatedPractice.lean)只导入既有 `CoupledOccurrence`，后者只导入 `GenerativeCore`。没有添加新的物质控制器、转移规律、伦理评分或主体／客体原始类型，没有修改同时发展的 `universal-ethics` 包。

[既有共同发生研究](YITI-REN-COFORMATION-MATH.md)已经连接实际承受、记录形成、改变的评价影响和响应，保留中间事件及局部终点描述的不足。本轮不重复宣称发现该机制。新结果是一个针对**整个有限发生历程**的抽象充分性准则，并精确限定它和实际行动、旧判断的修正、整体共同可行性的关系。

`History P` 包含起点、终点、完整的有限 `(事件, 之前状态, 之后状态)` 序列及其 `Trace` 证明。同一个 `P` 的变化可以包含目的、理解、能力、评价及关系的形成；新接口没有把这些先行固定为独立价值单位。这里「完整」是对于 `P` 所表达的状态和转移而言，不是声称模型已收尽现实整体。该历史是数学表示，不是声称某个参与过程内部实际储存了全部历史。

`extend h suffix` 只能从 `h` 真正到达的末态延伸。原先的物质条件、产生的关系和此前事件通过原过程及事件序列保留，不能在接合处暗中重置。

## 2. 明列的对应条件

给定：

- `P`：正在分析的同一过程的转移关系，其充分性与现实对应需另外说明；
- `Fits : History P → Prop`：对整个有限延伸历程是否适切的判定关系；
- `readout : History P → Reading`：从这些历程取得的分析性描述；若解释为实际习得的辨别，必须另给形成与使用的机制对应。

`Fits` **不是**分别满足一组既定期待的加总，也没有固定目的、标量好坏或功利最大化的定义。它可以表达有差别的实现、负担、拒绝、撤回、关系变更及实际回应的整体比较。但某个具体 `Fits` 为什么是伦理上正确的，仍是独立的实质论证。本模型把这项对应留作参数，不把它想象为生成现实之外的一个价值领域。

对于有限事件词 `w`，定义：

\[
\operatorname{Ready}(F,h,w)\iff
\operatorname{Feasible}_P(\operatorname{last}(h),w)
\land
\forall k\;[k\text{ 是从 }h\text{ 末态执行 }w\text{ 的实际容许延伸}
\Rightarrow F(h\cdot k)].
\]

这是一项**有限、稳健、开放事件词**的表示要求：同一个词的每个容许实现都适切，同时至少有一个实现。它不是对所有伦理应境的定义。有些处境存在不可消除的风险、冲突或悲剧；有些回应必须根据后续探查分支而定。这些情况下，没有上述 `Ready` 并不等于不存在伦理理解，也不等于无回应比回应更好。本轮没有概率政策、长期保证或一般智慧的完备性结论。

## 3. 已检查的主结果

令 `readingAt h` 为 `h` 所达到的描述，描述的定义域只含确实由某条 `History P` 达到的值。`respond` 在描述上选出事件词。则：

\[
\begin{aligned}
&\exists\operatorname{respond}\;\forall h,
  \operatorname{Ready}(F,h,\operatorname{respond}(\operatorname{readingAt}h))\\
&\quad\Longleftrightarrow\quad
\forall r\text{（已达到的描述）},\ \exists w\;\forall h,
\operatorname{readout}(h)=r\Rightarrow\operatorname{Ready}(F,h,w).
\end{aligned}
\]

对应 `sound_response_iff_common_continuation`。这是标准共同选择／描述纤维准则在完整发生历程上的专门化；不声称数学上的首创。其内容是：**同一描述所没有区分开的所有相关历程，必须有一项共同的可行且适切的延伸，才能仅依靠该描述保证这一级别的响应。** 这些历程是同一过程模型中未被读数区分的可能情况，不是被预设为独立存在的主体或相互对立的价值领域。

正向只展开既有响应的充分性；反向使用 `Classical.choice` 选取每个已达到描述的共同延伸。因此它是存在性结果，不是可执行算法、内部选择机制的形成证明或智能必然服从伦理的论证。

另有以下检查：

| 声明 | 精确意义与限制 |
|---|---|
| `extension_erases_to_actual_trace` | 去除发生描述后仍是原 `P` 的真实容许历程；没有新增物理步骤。 |
| `enacted_ready_fits` | 在 `Ready` **以及另外给出的实际执行历程**下，整个接合的历程满足 `Fits`。可行性与正确表示不会自行产生行动。 |
| `ready_has_fitting_extension` | `Ready` 至少有一个完整的适切延伸，不会用「全部不可能分支均适切」的空真来冒充实现。 |
| `ready_empty_iff` | 零事件后缀的 `Ready` 等价于原有限历史满足 `Fits`。零事件后缀不是现实关停、撤回干预、积极拒绝或停止后的无限未来。 |
| `no_fitting_history_no_ready` | 如果所给判定关系没有任何适切历史，表示接口不会凭空造出一个适切响应。这是接口的逻辑界限，不是切换 `Good=false` 来反驳伦理实质。 |
| `refinement_preserves_response_existence` | 在同一个过程、同一个历史域和同一个 `Fits` 下，细化描述而保留粗描述，不会失去原有共同响应的存在性。没有声称实际获取细化无需条件或代价。 |
| `incompatible_histories_obstruct_response` | 同描述下若存在没有共同 `Ready` 的两段历史，该描述不足以支持上述统一响应。反驳的是这一级别的表示充分性，不是非二元论或伦理可能性。 |
| `changed_appraisal_requires_response_revision` | 若旧响应符合旧判定，而新判定在具体历史明确排除它，旧响应就不再满足新判定。为什么新判定正确、为何原根据支持这种改判，不能由该条件推论代替。 |

对于有根据的拒绝、自我保护、差等或合理结束，必须把相应的真实活动及其后果纳入 `P`，并独立辩护整个延伸的 `Fits`。本文件没有将这些行为一律赋予正或负值；`ready_empty_iff` 不证明它们的伦理正当性。

## 4. 两两相容不等于整体相容

三个纯数学条件分别排除 `0`、`1`、`2`；可选项也是 `0`、`1`、`2`。任意两个条件都有共同选项，三个条件却没有共同选项。若已区分条件，则每个条件又有自己的可用选项。

三个声明 `every_pair_has_common_response`、`whole_family_has_no_common_response`、`differentiated_response_fits` 均经 Lean 检查。这个简单例子说明上一节必须量化到**整个描述纤维**，不能用两两检查代替。它没有将三个条件解释成三个先行固有的利益，也没有证明现实中的三方必然伦理冲突。其与「整体」的关联是表达充分性：独立的局部存在见证不能未经接合检验就被说成一个共同实现。

## 5. 对王阳明解释的作用

这些结果支持一项克制而积极的对应：在本轮所检验的有限稳健响应范围内，知与行若要被解释为同一事的分化，表示必须足以支持情境中的共同实现，并能在真实活动改变条件之后被重新检验。准确命题、适切判断、可实现的响应与实际躬行，可以在一个发生过程内分辨而不设为独立本体。相互关联不等于相互自动推出。

形式化没有定义「真知」「良知」或「仁」，没有从行为成功倒推其善，也没有从不能行动倒推毫无道德认识。它不要求把王阳明解释成先知后行的串联模块。原典所说心、意、知、物和格、致、诚、正、修为同一事的不同展开，仍需文本解释和哲学辩护；不能由同用一个 Lean 类型直接证明。

改变既有判断和丢弃其根据不同。新定理只明确「旧判定保证」不自动迁移到新判定；对于伦理上正确的修正，仍须解释新的整体关系、原判断的误认或真正的反向理由。成功控制、更能让人服从、删除投诉或维持固定输出都不等于去蔽。反过来，把每个旧判定都永久保持，也可能阻断真实纠正。后者的实质辩护与限制见[整体继续与判断修正](WHOLE-CONTINUATION-WARRANT-INTEGRATION.md)。

## 6. 检查、依赖和保存

运行：[check_wang_practice.py](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/check_wang_practice.py)。采用已核验的 Lean **4.29.1** 编译器，在新临时目录从保存的源代码编译三个模块，使用 `-s65536`，无旧构建产物复用。

- 总共检查 37 项声明的依赖，其中既有核心与发生描述 25 项，本轮新增 12 项。
- 新增 12 项中 **8 项无命名公理依赖**。`ready_empty_iff` 使用 `propext`；主存在性等价使用 `Classical.choice`；两个有限正例还使用 `propext` 或 `Quot.sound`。标准依赖并集为这三项。
- 没有自定义公理、`sorry`、`admit`、`native_decide`、`unsafe` 或未核实的证明占位。通过报告的这一点不消除 `P`、`Fits`、`readout` 的语义对应义务，也不等于满足无假设目标。
- [通过回执](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/wang-practice-verification.json)绑定编译器、源文件、检查器与日志的 SHA-256。固定通过尝试保存在 [1791371990097356000](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/wang-practice-checks/1791371990097356000/receipt.json)。
- [首次失败](../../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/wang-practice-checks/1791371969976789000/receipt.json)连同源代码与日志保留：两个有限例未展开 `Accepts`，导致不能自动合成 `Decidable`。显式展开后通过；没有更改定理命题或伦理范围。

代码检查属于实际形式验证。其他代理另行阅读源代码、回执及对应范围属于本次 AI 辅助内部审查，不是外部同行评审，也没有新增经验实验。原有 coformation 与 universal-ethics 的科学结果按其既定范围保留。
