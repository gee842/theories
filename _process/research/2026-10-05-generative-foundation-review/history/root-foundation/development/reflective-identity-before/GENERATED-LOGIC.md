# 生成条件与逻辑规则 / Generative conditions and logical rules

**第四轮完成：取得记录、核对当前适用性与实际执行接通。** [第12节](#acquired-support-use)在明确读取、版本维护及原子使用条件下，将记录支持的执行投影到同一原生占用过程；新增28项 Lean 定理通过。无关位置可以变化，反复失效也可以耗尽有限预算。/ **Fourth round complete:** acquired tickets support native use under explicit correspondence and atomicity conditions, with selective interference and exact retry accounting. Physical sensing and synchronization remain realization obligations; established concurrency results remain credited.

**第三轮完成：允许未来改接的范围决定摘要必须保留的占用区别。** 第11节给出必要与充分条件、由实际历史产生的反例及旧摘要无法自行更新的限制；新增24项 Lean 定理通过。既有交错占用研究直接复用；“动态”本身仍不构成前沿新颖性。/ **Third round complete:** future access scope determines the occupancy distinctions required by an exact summary. Section 11 adds checked bounds and a native counterexample; existing interleaving results are credited.

2026-10-08，Asia/Bangkok。研究方向与继续指示：Ren；本候选、形式化及作者反审：AI。[本次原话](../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md)。

**第二轮完成：共享历史推出固定上下文的精确适用条件，相关支承位摘要保留指定工作负载及步数预算判断。** 新37项 Lean 定理／220项闭包审计通过；总量摘要会丢失就绪判断，所选单支承摘要也会丢失完整初始相容性。下文第7–10节完成第一轮提出的这个有范围连接，保留动态交错、真实时间及前沿新颖性的独立问题。/ **Second completed round:** exact frozen-context conditions and scoped abstraction, with 37 new checked theorems and explicit counterexamples. Sections 7–10 supersede the corresponding first-round next-step wording at this bounded scope.

**第一轮完成：在明确的过程与上下文条件下，收缩规则的可容许性有实际复制的充要判据；有限补给只支持带成本的替代，顺序复用不保证重叠占用。** 38项新 Lean 定理通过，继承27项审计；没有由此证明全部经典逻辑、普遍生成规律或逻辑学新颖性。

**First completed pilot:** under an explicit process and context contract, contraction is admissible exactly when duplication is reachable. Finite provision supports paid replacement; serial reuse does not ensure overlapping use. Thirty-eight new Lean theorems pass, alongside 27 inherited audits. This establishes neither all classical logic nor a universal process law or a novelty claim.

## 1. 从同一展开中刻画推理 / Reasoning within one unfolding

承载条件、可实现的活动与对活动的判断，是同一展开的分析性表达。本轮采用既有[数学核心](MATHEMATICAL-CORE.md)的配置、事件、步骤与有限历史，不引入独立的主体和环境。配置边界必须保留问题所需的共享支持、消耗和干扰；给定形式过程不等于已经说明现实对应。

The resource configurations, their transformations and judgments about them describe selected relations within the same unfolding. The model uses the existing process root. A context is a composition of configurations relevant to a question, not an independently constituted external world. The mathematical decomposition preserves declared availability and endpoint reachability; it omits physical realization, duration and any unrepresented common support.

Lean 的类型、命题、等式、归纳与推理规则仍是公开的元逻辑。本轮另定义一个小型资源推导演算，原始规则只有身份、原生步骤、推理接续及上下文提升，**不含收缩构造子**。随后证明它与所声明的有限可达性相符。对象演算的收缩得到证明，不等于元逻辑从无前提产生。

Lean remains the explicit metatheory. The object calculus `Derives` contains identity, primitive process steps, cut and framing, but no contraction constructor. Its expressions are configurations; it is not a full language of arbitrary propositions, implication, negation and quantifiers. Soundness and completeness here mean correspondence with finite endpoint reachability only.

## 2. 收缩规则的精确判据 / Exact criterion for contraction

记 \(x\leadsto y\) 为原有 `Reach`：存在一个有限历史把配置 \(x\) 变为 \(y\)。给定组合 \(g\otimes x\)，公开两项条件：

1. 存在左单位 \(I\)，\(I\otimes x=x\)。
2. **原生步骤的上下文相容性**：若 \(x\xrightarrow e y\)，则 \(g\otimes x\xrightarrow e g\otimes y\)。

Let reachability mean an existential finite trace in the original process. Supply a context operation with a left unit and preservation of primitive steps under each declared left context. No associativity, commutativity or unlimited copying is hidden in this theorem's premises. Primitive compatibility implies finite-path compatibility by the already checked path construction.

在所定义资源演算中，所问规则为：

\[
\frac{g\otimes(a\otimes a)\vdash c}{g\otimes a\vdash c}.
\]

**已实查：**这条规则对所有所声明的 \(g,c\) 可容许，当且仅当

\[
a\leadsto a\otimes a.
\]

The checked theorem is `admissible_contraction_iff_duplicate`. A duplicate-producing trace lifts through the context, then composes with the proposed continuation. Conversely, instantiate the rule at the empty context and the target containing both copies; soundness yields the duplication trace. The semantic counterpart is `contraction_iff_duplicate`.

该判据需要目标范围允许询问“两个支持本身是否共同可达”。任意有限准备均被允许；结论没有保留固定事件字、耗时、概率、所有调度下的成功或被模型遗漏的副作用。二元复制再推出任意有限正份数的可达性及相应替代；没有证明无限执行或线性逻辑完整的指数提升规则。

The converse relies on a goal language containing the duplicated configuration itself. Reachability permits preparation and forgets the event word. The result does not promise bounded latency, probability, inevitable execution, or preservation of effects absent from the state. Binary duplication gives every finite positive multiplicity, not an infinite run or the full exponential modality.

## 3. 实际供给：付费替代与普通收缩 / Paid replacement and ordinary contraction

用 \((a,b)\) 表示同一配置中 \(a\) 份已就绪支持与 \(b\) 份可转化供给。公开局部规律：

\[
(a,b+1)\xrightarrow{\mathrm{form}}(a+1,b),\qquad
(a+1,b)\xrightarrow{\mathrm{spend}}(a,b).
\]

组合是两坐标相加。原生步骤的上下文相容性由这些规律实查于 Lean，不再作为本实例的独立输入。`spend` 表示退出当前可用量账户，不主张物质消失；没有生物或物理实验认证。转换规律、离散计数和组合解释仍是所声明的模型内容。

The two coordinates count readiness and convertible provision in one configuration. Framing is proved from the displayed laws and coordinate addition. Spending removes availability from this account, without asserting physical annihilation. These are stipulated local dynamics, not an empirical discovery or a universal conservation principle.

从 \((1,b)\) 可以达到至少 \(n+1\) 份就绪支持，**当且仅当** \(n\le b\)。充分方向构造 \((n+1,b-n)\)；必要方向保留每一步的 \(a+b\) 不增量。`budget_exact` 因而是精确供给界限，不是若干有限数值测试。

From \((1,b)\), a state with at least \(n+1\) ready supports is reachable exactly when \(n\le b\). The witness retains leftover provision explicitly; the bound follows from the proved nonincrease of the availability sum.

令 \(A=(1,0)\)、\(Z=(1,1)\)。有 \(Z\leadsto A\otimes A\)，故可以用 \(Z\) 替代对两个 \(A\) 的需要。没有 \(A\leadsto A\otimes A\)。更强地，**任何有限完整包 \((1,b)\) 都不能收缩为它自身的两份**：复制其供给也要计入目标。对应 `paid_contraction`、`no_free_contraction`、`no_budget_contraction`。

A package containing one ready support and one provision unit can replace two ready supports. A bare support cannot. No finite package \((1,b)\) duplicates the entire package including its provision. Paid replacement therefore does not establish ordinary contraction of the funded package.

## 4. 形成、消耗与两项反例 / Formation, exhaustion and counterexamples

同一历史中，\((0,2)\to(1,1)\to(2,0)\to(1,0)\)。初态不能立即 `spend`；第一步形成了这种即时能力。中段包能支持付费替代，末态不能。已证明的命题没有被“撤销”：不同配置具有不同能力。

There is an actual path through the four displayed configurations. Immediate spending is disabled initially and enabled after formation. Paid substitution is available in the middle and exhausted at the end. This changes the configuration to which a judgment applies; it does not invalidate a theorem.

**反审修正：**若任意有限准备都算入可达性，那么初态也已能达到两个就绪支持。`replacement_backwards` 证明：在固定规律与相容上下文下，若 \(x\leadsto y\)，且 \(y\) 能替代固定目标 \(z\)，则 \(x\) 也能。不能把形成“现在可用”的支持，改说成该无限制可达关系中新出现的能力。

**Review correction:** allowing arbitrary finite preparation means the initial configuration already has the later reachable capability. `replacement_backwards` proves this for a fixed replacement target. A formation claim must specify immediate availability, deadlines or another independently motivated access condition; the unrestricted reachability account alone cannot represent that kind of novelty.

另有两个实查反例：

- 单端口可对任意自然数 \\(n\) 完成 \\(n\) 次“取得—释放”，但“取得—取得”不可行。顺序复用不证明两个支持同时可用。
- 一个具左单位的五状态例允许孤立复制，加入指定上下文后却阻断相应步骤，收缩失败。这个例子否定省略上下文相容条件的推广；它没有满足并反驳完整判据，也没有独自解释物理干扰。

Two checked controls separate arbitrary finite serial reuse from overlapping acquisition, and standalone duplication from duplication in every declared context. The latter deliberately lacks primitive frame compatibility while retaining a left unit. Both preserve the stated scope of the positive theorem.

## 5. 第一轮前沿评估与后续目标 / First-round frontier assessment and subsequent target

本轮完成了过程根基到一个资源规则的具体对应。**不声称新数学或新的逻辑基础。** 收缩与复制、Petri 网与线性逻辑、带数量的使用约束都有深厚先例；动态分享和撤回也已有研究。仅增加“生成”命名或动态标签不足以推进前沿。完整[来源、反审与依赖表](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATED-LOGIC-INTEGRATION.md)说明相邻工作。

This pilot is an explicit, checked reconstruction inside our existing process account. It is not a claim of novel mathematics. Dynamic sharing and loss of permissions already have substantial logical treatments, in addition to linear, graded and Petri-net approaches.

第一轮提出的后续目标是：**以既有共同支持和历史模型为内容，独立规定及时就绪与共享相容的问题，推导哪些上下文允许规则，并检查压缩表示是否保留这些判断；与 Iris/Leaf 的框架和分级逻辑作同目标比较。** 如果这些结果只是已有机制的直接实例，就按应用／整合成果归档；只有额外的定理、适用范围或不可由既有比较保留的解释内容，才构成前沿候选。第7–10节完成其固定上下文与所选工作负载范围；更广泛的动态交错与实际时间仍须另作判断，不重开已完成结果。

The first-round next bridge was from independently specified readiness and shared-support histories to admissible contexts and faithful abstraction. Sections 7–10 now close the frozen-context and selected-workload interface. Comparison with Iris/Leaf and graded systems remains necessary for any novelty claim. A direct instance belongs among applications and integrations. This does not alter the completed G0/J ethical route: accurate support accounting informs joint-realization judgments, but copying or renewability does not itself establish goodness.

## 6. 检查与复现 / Verification and reproduction

运行：

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_generated_contraction.py
```

[通用判据与演算](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/GeneratedContraction.lean)：14项新定理，全部空命名公理报告。[机制与反例](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ContractionMechanisms.lean)：24项新定理，其中10项空报告、14项仅依赖 `propext` 或 `propext` 与 `Quot.sound`。没有 `Classical.choice`、自定义公理或证明洞。继承的过程核心18项及路径9项均为空；合计65项审计，51项为空。空报告仍使用 Lean 的类型理论和明示前提。

The isolated Lean 4.29.1 build checks 38 new theorems and 27 inherited declarations: 65 audits, 51 empty. Fourteen new reports use only the standard dependencies stated above. The [immutable successful receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/generated-contraction-checks/20261008T101759.536385Z/receipt.json) binds copied sources, compiler output and dependencies; the [latest pointer](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/generated-contraction-verification.json) supports reproduction. No independent-agent acceptance, empirical validation or repository-wide audit is claimed.

## 7. 从共享历史推出规则适用的上下文 / Deriving admissible contexts from shared histories

按 Ren 再次“请继续”，本轮直接扩展已有[占用／释放模型](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryLeaseDynamics.lean)，保留两种活动角色、两个支承位置及其共享或分开接入的局部规律。角色由同一接入关系区分，未增加独立主体或外在环境。局部占用 \(b\) 与在本段执行中固定的另一部分占用 \(g\) 合为 \(g\cup b\)。初始时二者不能重复占有同一位置。

This continuation reuses the existing two-slot acquisition/release process. The activity roles differentiate through its access relation. A local occupancy and a held context are portions of one common configuration. The frame is frozen during the local word; its own acquisition and release can occur before or after that segment in the same process.

给定一段原本可行的有限历史 \(b\xrightarrow{w}t\)，令 \(F(w)\) 是按实际接入关系确定、被这段历史取得或释放的位置。由原生步骤推出：

\[
\operatorname{Feasible}(g\cup b,w)
\quad\Longleftrightarrow\quad
\forall i\in F(w),\ g(i)=\mathrm{free},
\]

前提是原历史可行、初始占用不重合、\(g\) 在执行期间固定。若成立，实际终点正是 \(g\cup t\)。这不是预设所有上下文都相容，而是从步骤规律推出**这一段历史允许哪些上下文**。`framed_feasible_iff`、`trace_frame_lift` 和 `trace_frame_reflect` 检查两个方向及终点。

The footprint test is necessary and sufficient for replay of a locally valid finite word in a compatible frozen context. The lifted endpoint is the frame merged with the original endpoint. This establishes both preservation and reflection for the stated local law. A certified preparation then composes with a continuation beginning at its actual reached state (`guarded_substitution`). It does not grant unrestricted contraction or certify arbitrary external interleavings.

相容性随实际占用改变：另一活动取得同一支承后，本活动的“取得—释放”段不可行；接入不同位置则仍可行；释放该占用后恢复。`context_acquired`、`occupied_context_iff`、`release_restores_episode` 将这些上下文接回同一原生历史。固定的是所分析的执行段中的上下文，不是整个世界永远不变。

The context occupancy is itself produced by the same acquisition law. Acquiring the relevant support disables the episode; occupying a distinct accessible support does not; release restores it. These are changes in operational availability, not changes in the validity of a proved theorem.

## 8. 压缩什么才不丢失判断 / What an adequate summary must retain

**总量不足。** 在分开接入的同一模型中，“位置0被占用”和“位置1被占用”总占用数都为1，但任务0的即时取得判断不同。两种配置都由原生取得产生。`count_cannot_decide_readiness` 证明不存在一个只看总量的判定谓词，可以对所有配置准确回答该问题。错误来自遗漏接入关系需要的区别。

**A total count is insufficient.** Two natively obtainable configurations have equal occupancy totals and different readiness for the same task. No predicate of the count alone answers that readiness question exactly throughout the model. This is an omitted relation in the proposed summary, not failure of all abstraction.

**限定工作负载后可以真正压缩。** 在两个任务共用位置0的模型中，限定工作负载为取得这些任务及释放位置0，保留 \(q(b)=b(0)\) 一位即可。该投影确实合并了不同原状态；每一步都从每个对应原状态保留并可提升，故保留所有所选有限事件字，而不只是几个例子。另有 \(q(g\cup b)=q(g)\lor q(b)\)，所以指定上下文中的执行判断也保留。

**A genuine selective compression works.** With both task roles accessing slot 0, retain its occupancy and restrict the workload to those acquisitions and release of slot 0. A one-bit projection merges distinct states yet preserves and lifts every selected primitive step from every representative. Consequently it preserves every finite word and the corresponding merged-context feasibility. The event labels themselves are retained.

但该一位摘要**不能**判定位置1上的初始重复占用，也不保留释放位置1的可行性。`projection_loses_global_disjointness` 与 `hidden_release_lost` 明确保留这两项失败。因此，对第7节规则的使用，完整初始相容性仍须有根据；本摘要只保留给定范围的历史判断与支承测试，不认证完整共享关系。

The one-bit view loses whole-configuration disjointness and release of the omitted support. These are checked counterexamples. In particular, a representation exact for selected behavior does not automatically certify every premise needed to apply a contextual rule. For the selected words, the footprint guard itself is retained (`safe_projection`, `visible_guard_exact`); the initial full compatibility obligation remains explicit.

这里遗漏位置的反例使用模型允许的初始占用，未声称它们在共享接入模式下由全空配置生成。前面的总量反例则明确使用分开接入模式中的原生取得结果。/ The hidden-slot witnesses use allowed initial occupancies; they are not claimed to be generated from the vacant state in the shared-access mode. The count counterexample separately uses native acquisition outcomes in the distinct-access mode.

## 9. 就绪预算与一般表示条件 / Readiness budgets and general representation conditions

定义 \(\operatorname{MayBy}_P(s,n,G)\)：存在不超过 \\(n\) 个原生事件的历史，使目标 \(G\) 成立。零预算精确对应 \(G\) 现在成立。它刻画有限准备问题，未把事件个数等同真实时间，也不是必然执行或概率保证。

`MayBy` asks for an existential path of at most a specified number of original events to a declared goal. At zero budget it is exactly the current goal. Event count is not physical elapsed time; inevitability, scheduling and probabilistic success are different contracts.

一般定理 `mayBy_exact` 与 `contextual_mayBy_exact` 说明：若同标签的步骤保留、逐原状态提升、目标对应成立，且组合与投影相容，则所有这类预算判断在对应上下文中等价。它们复用原数学核心已完成的历史投影／提升。第8节的单支承摘要满足具体条件，因此准确保留“位置0在 \\(n\) 步内可就绪”的判断。

The general proof transports the same event word and hence the same length. It requires preservation, lifting from each concrete representative, goal correspondence, and compatibility of composition with projection. The one-bit instance discharges those conditions for its selected workload. Collapsing an entire episode into one abstract event would not satisfy this budget contract merely by preserving eventual reachability.

**预算结论的上下文范围：**这里 `MayBy` 从合并后的整体配置出发，未要求路径中的每一步都保留原来的占用部分 \(g\)。它与第7节的“固定占用仍在场时重放一段局部历史”是不同问题。第7节的使用仍须保留局部历史、初始相容和支承避让条件；不能仅凭整体预算判断，声称在不动用已占支承的条件下也能及时就绪。

**Budget-context scope:** `MayBy` runs from the merged whole configuration and does not require preservation of the initial held portion at every step. It is distinct from replay under a frozen frame. The latter retains the local-trace, initial-disjointness and footprint obligations of section 7. Exact abstraction of the merged process does not remove those obligations.

## 10. 本轮完成范围、先例与剩余问题 / Completion, precedent and remaining questions

本轮完成上一轮提出的**固定共享上下文判据—实际形成与释放—有限步就绪—有范围摘要**连接。Iris 已有资源相容与保持上下文的更新，Leaf 已有临时分享及收回；这些不是本理论首次提出。本轮将相关问题接到我们的原生历史模型并实查，仍属整合与应用结果，未建立对已有逻辑的表达力优势或数学新颖性。[原典比较及作者反审](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTEXTUAL-LOGIC-INTEGRATION.md)区分它们的形式目标。

The frozen-context/readiness/abstraction interface is complete at the declared scope. Iris and Leaf already address compatibility, framing and changing sharing arrangements. This study provides a checked integration with our existing history model; it does not establish an expressive advantage or a new logical foundation. The proposed next comparison concerned changing support during interleaved activity. Section 11 credits the repository's already completed interleaving study and isolates a further access-reconfiguration target; the generic dynamic-support task is not reopened.

新增[上下文推导](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ContextualLeaseRules.lean)16项定理、[摘要与预算](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ContextualLogicAbstraction.lean)21项，共37项；其中12项空命名公理依赖，25项只含 `propext` 或 `propext`／`Quot.sound`，无新增 `Classical.choice`。12个继承模块的183项审计及源码与原共同支持检查保持一致；14模块合计220项，124空、96标准依赖。继承闭包中既有经典选择依赖保留，不混为新增证明依赖。

Run [check_contextual_logic.py](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_contextual_logic.py). The [frozen successful receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/contextual-logic-checks/20261008T103742.401003Z/receipt.json) records Lean 4.29.1, source bytes, logs and all 220 audits. The earlier 38-theorem contraction study retains its original scope and receipt. No independent-agent acceptance or empirical validation is claimed.

## 11. 接入关系改变时，旧摘要为何需要修订 / Why changing access can require a revised summary

首先信用既有[变化中的共同支持研究](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md)：形成、撤回、交错占用／释放、证书恢复和实际进度已有42项实查定理。本轮不重做这些结果，而检验**接入关系改变后，原先准确的表示还能否继续支持推理**。

The completed changing-support study already covers interleaved occupancy and readiness preservation. The new target is exact representation when the activity's access relation changes. We continue to describe one configuration: a current route and shared support occupancy. Neither is an independently constituted subject or environment.

公开局部模型：支承域为 \(R\)，占用为 \(b:R\to\{0,1\}\)，当前接入位置为 \(a\)，允许的支承范围为 \(K\subseteq R\)。三个原子事件为：改接到 \(r\in K\)；取得当前未占用且属于 \(K\) 的支承；释放 \(K\) 内的已占支承。改接改变关系，保留占用。所有身份和 \(K\) 仍明确给定；没有由此解释物理布线、权限的取得或新支承身份的创造。

The supplied operations redirect to any permitted slot, acquire the current free permitted slot, and release a permitted held slot. Their atomicity, support identities and access permission are assumptions. `K` is fixed within each process; comparing narrower and broader `K` compares contracts, not an already implemented mechanism for changing permissions. Actual routing changes occur as native events within the broader process.

**精确结果。** 对当前接入位置相同的两个配置，以下两项等价：

\[
\begin{aligned}
&\text{所有允许的有限事件字具有相同可行性}\\
\Longleftrightarrow\quad
&\forall r\in K,\ b_1(r)=b_2(r).
\end{aligned}
\]

充分方向逐步保持关系并匹配同一事件字。必要方向只需“改接到 \(r\)—取得”这两个事件：其可行性准确揭示 \(r\) 是否空闲。因此，准确处理全部未来改接的摘要，不能混同 \(K\) 内不同的占用；范围外的占用区别可以省略。`fixed_route_behavior_iff`、`observation_sufficient`、`exact_reader_separates` 检查这些范围。若每个位置都允许改接，则对固定当前接入，任何准确编码必须在占用函数上单射；这不禁止更紧凑的无损编码。

With the current route fixed, agreement on occupancy throughout `K` is necessary and sufficient for equality of all permitted finite-word feasibility judgments. Two-event probes suffice for the necessary direction. Keeping the route and the restriction of occupancy to `K` is sufficient. The unrestricted case forbids losing occupancy distinctions; it does not forbid lossless compression, restrict all conceivable logics, or prove minimality of the route representation itself.

**实际反例。** 从两个位置都空闲、接入位置0开始，执行“改接1—取得—改接0”。到达的配置与原配置对仅接入位置0的全部工作负载完全等价，旧摘要也相同。允许再改接1后，原配置可取得而后者不可取得。两者由同一原生过程相连，避免把任意初始隐藏状态当作已生成事实。

The two states have the same old observation and every old-workload feasibility judgment, yet a newly admitted probe distinguishes them. `hidden_formed` records the native three-event history. The change in access can alter current readiness while occupancy itself remains identical (`redirect_changes_readiness_only`). No proved theorem becomes false: its process, state and scope parameters must remain attached to its application.

**更新也需要信息。** `no_blind_redirect_update` 证明：仅拿旧的“当前位置及该位置占用”摘要和改接目的地，不能对所有配置准确算出改接后的同类摘要。新位置的当前占用信息足以完成这个局部更新，但取得可信读数、保持读取与使用一致，需要另有机制。本轮没有把观察正确性藏进修复算法。

An updater given only the old active-slot view and the destination cannot reconstruct every updated view. A current reading of the newly relevant slot supplies the missing bit; the checked `refreshed_view` identity is a correspondence, not a verified sensing or synchronization protocol. Retained history or other stored information also changes the premise of the impossibility result.

本轮新增[24项定理](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ReconfigurableSupportLogic.lean)，其中12项空命名公理报告、12项仅用 `propext` 和／或 `Quot.sound`；继承过程核心18项均为空，合计42项审计、30项为空。[冻结回执](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/reconfigurable-logic-checks/20261008T105809.742208Z/receipt.json)保留实际 Lean 4.29.1 检查；[整合、来源和反审](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECONFIGURABLE-LOGIC-INTEGRATION.md)说明完成范围。

**前沿结论：**得到了一条有范围的解释——未来可形成的接入关系，约束当前抽象允许遗忘什么。既有局部 rely-guarantee 逻辑已处理变化中的共享，抽象解释也已有完整性与修复理论。本结果仍是本仓库中的严谨整合，未证明超出这些工作的数学新颖性。本轮结束时提出的下一问题，是有成本、可能失准的信息取得怎样支持改接时的正确更新，并与现有方法比较；第12节已完成其中的有条件执行连接。此处的精确静态范围界限不再列为待证。

The derived bound is an integration result, not an established frontier advance. Existing local rely-guarantee and abstraction-repair methods prevent a novelty claim based merely on dynamic access or refinement. At this round's completion, the remaining connection was warranted acquisition and use under explicit cost and interference. Section 12 now supplies a checked operational bridge under a declared observation and synchronization contract. The exact scope bound proved here remains complete and reusable.

<a id="acquired-support-use"></a>

## 12. 读得正确，何时能实际使用 / When a correct reading supports actual use

本轮接续第11节，直接复用已有[交接与版本](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CORRECTION-HANDOFF-INTEGRATION.md)、[读取与保护区间](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CORRECTION-FRONTIER-BOUNDARY.md)及[付费证据](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/EVIDENCE-QUALIFIED-CORRECTION-INTEGRATION.md)研究。新问题是：取得的信息能否在同一原生占用过程里支持后续操作，并保留其取得代价。

The extension keeps the prior route and occupancy configuration, adding per-slot revisions, an optional reading record and an allocated budget. These are related coordinates of one process. A projection theorem specifies exactly which physical effects are retained when reading and rejection bookkeeping are omitted; their charges remain in the extended account.

公开机制：每次取得或释放支承，都增加该位置的自然数版本；改接只改变当前接入关系。一次原子读取记录当前位置、其版本及占用。使用前须同时满足：当前位置仍与记录相符、版本相同、记录为空闲、接入仍被允许、预算足够。核对与取得合为一个原子事件。读取和使用各计一个预算单位，其他原生变化及丢弃记录不计入此项专用预算；这不表示它们没有真实代价。

Every admitted occupancy writer maintains its slot's revision. Reads are supplied coherent samples; revisions do not wrap; support identities and permission scope remain fixed. Atomic validation together with use is an explicit law, not a proved hardware property. No ownership authentication or sensor implementation is derived.

**已证的执行连接。** 读取建立记录的条件性准确关系，后续合法事件保持该关系。过期记录可以仍符合这个保持关系，却无法通过当前使用检查。使用规则本身不再查询实际占用；从记录保持关系与核对结果，证明原生取得要求的“当前位置确实空闲”。任意有限执行据此投影为第11节过程中的合法历史（`use_is_native`、`trace_projects`）。

The use guard checks the stored free value and present route/revision, without adding the native occupancy test as a second guard. The preserved invariant supplies that test's truth. Every finite extended trace from a sound initial session projects to a legal native trace; empty-ticket initial sessions are sound. This is a one-way refinement, not a claim that every native trace is affordable in the extended process.

**可以不冻结全部位置。** 读取当前位置后，释放另一个位置，再使用原记录，是实查通过的合法历史。另一方面，当前位置被占用后，记录失效；即使随后释放、实际值又恢复为空闲，旧版本仍被拒绝。绕过版本维护的写入会破坏记录对应，错误放行的见证也明确保留。

An unrelated release can preserve admission. A relevant update invalidates the ticket, and restoration of the old Boolean value need not restore its revision. This protocol is therefore conservative. An untracked writer can make the check pass while native acquisition is impossible; the checked bypass control violates the invariant and demonstrates why full mediation matters.

**代价与完成分别成立。** 整段历史满足“终余预算＋读取／使用次数＝初始预算”。紧接的“读取—使用”可行，当且仅当当前位置被允许、实际空闲且至少还有两单位预算。对于每次“读取—被占—释放—拒绝旧记录”的指定干扰循环，循环 \(n\) 次再成功读取／使用的精确条件是：

\[
B\geq n+2.
\]

The bound concerns that specified history with a final quiet read/use pair. For every finite budget \(B\), a legal history of \(B\) failed-reading cycles restores the slot to free but exhausts the budget, disabling further reads and uses. It establishes possible exhaustion, not inevitable starvation under every scheduler or an optimal cost theorem.

该耗尽结论只阻止这条记录支持路径中的后续读取和使用。模型仍允许按原生条件发生 `change take`；没有证明整个过程无法取得支承，也没有把指定历史的预算下界推广为全部可达路径的下界。

Native `change take` remains possible under its own guard. Exhaustion of the allocated reading/use budget is not failure of every route to an occupancy goal.

因此，**可靠使用、取得信息的成本与最终完成，是需要分别接通的条件**。本轮已经完成这项有条件的执行连接。进一步的现实应用须给出具体读取实现、全部写入维护及核对／使用原子性的证据；若目标包含最终完成，还须兑现干扰限制、保护或预算接续条件。再增加相似的小模型，不能代替这些对应证据。

This completes the local acquisition-to-use bridge. It does not derive trustworthy sensing, universal progress or metalogic from no premises. Established optimistic validation already addresses validation/write intervals and retry limits; the [primary-source comparison and author counterreview](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ACQUIRED-SUPPORT-USE-INTEGRATION.md) records why no frontier novelty is claimed.

新增[记录与执行](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/AcquiredSupportUse.lean)15项定理、[干扰与代价见证](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/AcquiredSupportUseCases.lean)13项，共28项，其中8项空命名公理报告、20项仅标准 `propext` 和／或 `Quot.sound`，无经典选择。继承42项审计保持范围；四模块合计70项、38空。[实际 Lean 4.29.1 冻结回执](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/acquired-support-use-checks/20261008T112000.799032Z/receipt.json)保留源码及日志。空报告不取消显式过程规律、参数或元逻辑。
