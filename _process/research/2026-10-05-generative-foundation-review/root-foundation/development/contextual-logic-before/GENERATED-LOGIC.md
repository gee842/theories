# 生成条件与逻辑规则 / Generative conditions and logical rules

2026-10-08，Asia/Bangkok。研究方向与继续指示：Ren；本候选、形式化及作者反审：AI。[本次原话](../../../sources/15-codex-theory-conversations/2026-10-08-generative-logic-investigation.md)。

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

- 单端口可对任意自然数 \(n\) 完成 \(n\) 次“取得—释放”，但“取得—取得”不可行。顺序复用不证明两个支持同时可用。
- 一个具左单位的五状态例允许孤立复制，加入指定上下文后却阻断相应步骤，收缩失败。这个例子否定省略上下文相容条件的推广；它没有满足并反驳完整判据，也没有独自解释物理干扰。

Two checked controls separate arbitrary finite serial reuse from overlapping acquisition, and standalone duplication from duplication in every declared context. The latter deliberately lacks primitive frame compatibility while retaining a left unit. Both preserve the stated scope of the positive theorem.

## 5. 前沿评估与下一连接 / Frontier assessment and next connection

本轮完成了过程根基到一个资源规则的具体对应。**不声称新数学或新的逻辑基础。** 收缩与复制、Petri 网与线性逻辑、带数量的使用约束都有深厚先例；动态分享和撤回也已有研究。仅增加“生成”命名或动态标签不足以推进前沿。完整[来源、反审与依赖表](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATED-LOGIC-INTEGRATION.md)说明相邻工作。

This pilot is an explicit, checked reconstruction inside our existing process account. It is not a claim of novel mathematics. Dynamic sharing and loss of permissions already have substantial logical treatments, in addition to linear, graded and Petri-net approaches.

下一连接具体限定为：**以既有共同支持和历史模型为内容，独立规定及时就绪与共享相容的问题，推导哪些上下文允许规则，并检查压缩表示是否保留这些判断；与 Iris/Leaf 的框架和分级逻辑作同目标比较。** 如果这些结果只是已有机制的直接实例，就按应用／整合成果归档；只有额外的定理、适用范围或不可由既有比较保留的解释内容，才构成前沿候选。此后续尚未完成，不重复本轮已完成判据。

The next bridge is from independently specified readiness and shared-support histories to admissible contexts and faithful abstraction of those judgments. It must be compared with Iris/Leaf and graded systems on the same target. A direct instance belongs among applications and integrations; a frontier claim requires an additional result. This does not alter the completed G0/J ethical route: accurate support accounting informs joint-realization judgments, but copying or renewability does not itself establish goodness.

## 6. 检查与复现 / Verification and reproduction

运行：

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_generated_contraction.py
```

[通用判据与演算](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/GeneratedContraction.lean)：14项新定理，全部空命名公理报告。[机制与反例](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ContractionMechanisms.lean)：24项新定理，其中10项空报告、14项仅依赖 `propext` 或 `propext` 与 `Quot.sound`。没有 `Classical.choice`、自定义公理或证明洞。继承的过程核心18项及路径9项均为空；合计65项审计，51项为空。空报告仍使用 Lean 的类型理论和明示前提。

The isolated Lean 4.29.1 build checks 38 new theorems and 27 inherited declarations: 65 audits, 51 empty. Fourteen new reports use only the standard dependencies stated above. The [immutable successful receipt](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/generated-contraction-checks/20261008T101759.536385Z/receipt.json) binds copied sources, compiler output and dependencies; the [latest pointer](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/generated-contraction-verification.json) supports reproduction. No independent-agent acceptance, empirical validation or repository-wide audit is claimed.
