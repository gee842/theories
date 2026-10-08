# 局部回应怎样共同接续 / Joint continuation of local responses

2026-10-08。AI 撰写，回应 Ren 在理论重心下的“继续”。[原话](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md)。本轮接续[尺度描述的接续充分性](CONTINUATION-ADEQUACY-INTEGRATION.md)，推进**分别依记录回应的方案 → 同一实际历史中的共同方案**。

**中心结果：局部方案可以组成共同接续，但要分别证明两件事——共同活动造成的每个实际后果仍在各局部说明的范围内，以及所选活动在每个相容的后续记录分支都能共同实施。** 第一个条件防止把“单独活动的后果”当成“共同活动中的后果”；第二个条件防止多次承诺同一份支持。两者不由局部正确性自动产生。

**Central result:** local observation-dependent plans compose under faithful projection of joint effects and recursive joint executability. The theorem preserves each local requirement across every modeled joint successor. It does not infer compatibility from separate success, manufacture missing support, or confer normative priority on a selected requirement.

## 1. 复用已有成果，精确定位新增连接

前轮已证明接续充分性与有限观察分支方案的存在等价。本轮直接导入该模块，保留它的取得证据、对应和有限时域范围。

同一仓库的共同实现方向现已完成更多连接，必须信用：

- [共享身份与共同实现](EXPLANATORY-JOINTNESS-INTEGRATION.md)区分指定部分的真实相容与分别存在合适见证。
- [完整支持范围及全局实现](EXPLANATORY-GLOBAL-REALIZATION-INTEGRATION.md)已证明在固定接入、取得后持续占用的规律下，正确范围可以使局部证书接到整体取得历史；任意固定阶数的成功清单仍可能遗漏更大共同需求。
- [变化支持](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md)已把形成、撤去、取得和释放接到同一历史，区别准备可保持、修复后可完成与实际调度会完成。

本轮不把这些作为新发现，也不将其重开为待办。新增的是一个泛型、有限时域的**观察分支方案合成定理**。下面的消耗例是解释该接口的实例，不冒称首次证明容量冲突或高阶相容问题。

## 2. 共同历史先于局部分解

从一个共同状态类型 `X` 和实际联合转移 `joint x (u,v) y` 开始。映射 `pa`、`pb` 给出这段历史的两种局部描述；**没有假定 `X` 等于两个局部状态的笛卡尔积**，也没有要求任意两种局部状态能自由拼在一起。共享支持、占用、时钟和形成历史可以存在于共同状态中。

两个局部方案各自只根据其已形成的后续记录分支。`zipPlan` 把同一时域的活动配对，并把下一对记录分别交给原方案。它不向任何一方提供另一方的秘密读数，不会凭空形成通信或共同知识。本轮形式对象仍是一个同步的数学方案树；实际分布执行所需的时钟、通信、发令顺序和权限没有由树的存在证明。

局部相容范围可以比共同历史的投影更宽。初始覆盖只要求每个真实候选投影都在对应局部范围中；不要求这些范围彼此独立。后续记录也来自同一后继的两个投影，不是任取两个分别可能的记录冒充共同观察。

The global process is primary in the model; local views are projections of it. The combined observation is a pair of records from the same successor. The compositional theorem does not assume product-state independence, central omniscience, or arbitrary substitution of locally indistinguishable parts.

## 3. 两个不能混为一谈的合成条件

**作用覆盖 / Effect coverage.** 对每次实际联合转移，两种投影都必须是各自局部转移所承认的后果：

\[
joint(x,(u,v),y)\Rightarrow
left(pa(x),u,pa(y))\ \land\ right(pb(x),v,pb(y)).
\]

这里要求局部模型覆盖共同实施时的作用，不要求两边无相互影响。局部关系可以保守地容纳共享作用；代价是更多可能性可能使原方案不再可证。准确的隔离实验模型不一定满足这项覆盖，因为加入另一活动可能改变消耗、传递或损伤。

**递推共同可实施 / Recursive joint executability.** 在当前相容范围中，方案所选的活动对必须对每个候选都容许，并有至少一个实际后继；对每个联合记录，原方案的后续分支仍须满足同一条件。`compatible` 只表达这些操作义务，不偷偷包含局部 `good` 条件。它既不自动分配支持，也不从“方案希望这样做”推出机制存在。

在两份局部方案已经满足各自要求、初始投影覆盖成立的前提下，Lean 证明：上述作用覆盖与递推共同可实施足以使配对方案满足两项要求的合取。证明随时域归纳；每一步先把共同后继类投影到相应局部后继类，再使用局部已检查的后续分支。

还检查了必要方向：成功的配对方案必然满足其递推共同可实施条件。因此，若实际某个相容分支无法共同实施，这一配对方案不能靠原有两份局部证明获得成功认证。这个必要性只针对固定配对方案；换时序、目标、活动或取得新证据，可能形成另一方案。

**完成的精确范围：** 泛型定理覆盖任意给定状态类型和转移关系、任意有限共同步数，以及所选同步分支方案。它不是所有异步并发系统的无条件完备合成法，也不保证可行方案被实际采用。

## 4. 真实消耗说明为什么局部证书会失效

用一项明确局部规律 `spend c x y` 表示有 `c ≤ x` 且 `y = x-c`。Lean 检查实际余量加消耗等于原量，并检查两次先后消耗等价于一次总消耗。该规律适合可加、不可在本段自动更新的量；不把所有生活条件、支持、时间或规范价值归为一种通用货币。

每个局部方案计划执行两次，每次消耗一单位。分别从两单位起算，两份方案均通过检查。把它们放到**同一份两单位**支持上同步实施：第一轮共同消耗两单位，已经归零；第二轮没有后继。Lean 保留这条真实耗尽轨迹。

| 检验对象 | 实查结果 | 没有因此证明什么 |
|---|---|---|
| 两份局部两步方案分别从两单位开始 | 分别可实施 | 同一份支持可以给两边各算一次 |
| 两方案在共同两单位上配对 | 第一轮成功，第二轮阻塞 | 当前共同可实施可自动保持 |
| 同样两方案在共同四单位上配对 | 两轮成功 | 四单位支持怎样形成、是否可得或应优先给它们 |
| 两单位下改为四次逐个消耗 | 仍不可能全部完成 | 排队本身能恢复已消耗的量 |

更直接地，共同首轮的转移是 `2 → 0`，而隔离局部模型预期一次 `2 → 1`。因此作用覆盖条件已经失败。这个例子没有反驳充分条件；它指出原先正确的局部规律被错误移用了。若局部模型明确写入另一活动的可能消耗，覆盖可以修正，但原有“两单位足够两步”的局部证明随之需要重新检查。

另两个算术定理给出具体支持接口：若分配给两项的范围分别是 `l,r`，选定需求是 `a ≤ l,b ≤ r`，且 `l+r` 不超过同一实际总量，则这次总需求可实施；消耗后，两项剩余额度加实际总消耗仍等于原分配。它们可用来履行具体步骤的共同可实施义务，却未单独完成任意分支方案的额度形成、长期更新或正当分配。

容量二能容纳三项单位请求中的每一对，却不能同时容纳三项，也在此模块检查为简明实例。较强的任意阶数结果已由上面的全局实现研究完成，这里不重新认领。

## 5. 对尺度理论与生成性对齐的推进

“尺度之间的关系”现在多了一项明确内容：**局部说明不仅要各自正确，还要说明它们在共同实施中怎样继续正确。** 各处的描述可能共享同一个支持来源、同一个已经作出的承诺或同一段时间。共同历史中的身份和作用不能在投影后被当成可以独立复制的量。

这也限定“整体”的含义。整体不是各局部成功分数相加；需要追踪同一活动形成的相互影响和后续可实施范围。但整体视角也不意味着必须取消局部差异、设立唯一中心，或让任何人替全部参与者作决定。局部记录和回应仍可保留；合成要求它们的关系有根据。

对生成性对齐，本轮提供的是实施侧的约束：智能、人类与机构各自有理由支持的活动，可能依赖同一组有限条件。提出共同方案时，必须把这些共同作用、已经承诺的支持及后续变化计入，而不能对每一方分别许诺完整余量。这项约束不决定谁优先，也不允许把某一方真实损失从要求中删掉来制造“相容”。取舍、权限、补救和有限结束直接复用已完成的 G0/J 一般实践判断。

此外，形式结论只保证共同状态满足**所列局部要求的合取**。它不证明这些要求穷尽整体伦理质量；被遗漏的其他生命、生成机会和新形成的承担仍可能改变评价。有根据地改变目标需要规范论证，不能用这份合成定理暗中替代。

## 6. 来源比较、反审与验证

Abadi and Lamport, [*Composing Specifications*](https://lamport.azurewebsites.net/pubs/abadi-composing.pdf), opening composition-principle discussion (PDF pp. 1–2), explicitly asks how component guarantees jointly establish a system guarantee and how the other components satisfy each component's assumptions. This is established compositional reasoning, not an invention of the present account. Our finite observation-tree result does not reproduce their general temporal composition or realizability theorems. The source was inspected at this stated scope and remains link-only.

Reynolds, [*Separation Logic*](https://www.cs.cmu.edu/~jcr/seplogic.pdf), introduction and separating-conjunction semantics (PDF pp. 1–5), supplies a clear precedent for controlling sharing in local reasoning. Its disjoint heap semantics is more specific than our arbitrary joint state and projections. We do not import a universal disjointness law or claim to formalize the frame rule. Source comparison is not empirical evidence.

**反审。** 合成定理是否把共同成功直接作为前提？没有预设共同满足两项状态要求；这部分由局部有效性和真实作用投影推出。但是共同可实施性确实是独立且可能很难的操作前提，定理不隐藏这一点。对于只关心“不阻塞”的实例，状态要求取真，失败展示的是支持耗尽而非已证的生物损害。对更实质的要求，应用者必须给出其现实及规范含义。

**反审。** 同步步是否暗中解决现实并发？没有。检查—执行之间的变化、通信成本及异步交错必须在所选共同转移中覆盖，或另给细化关系。把实际不能同时取得的两个读数拼成一个观察对，会破坏对应。已有变化支持研究的原子性范围保持明确。

**反审。** 兼容性失败是否意味着所有共同未来都失败？没有。它拒绝的是固定方案、固定时域和给定机制下的实现；实际支持形成、目标的正当修订或其他路线可能修复。四单位成功只证明在增加支持的前提下可行，没有生成支持或合法分配的证明。

[Lean 源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/JointContinuation.lean) · [重现脚本](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_joint_continuation.py) · [实查回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/joint-continuation-verification.json)。**16项新定理／16项新审计；14项接续充分性审计另列继承重放。** Lean 4.30.0-rc2、固定 Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`；无自定义公理、证明缺口或本机绕过。首次编译的两个有限判定因定义未展开失败，改用展开后的逻辑证明；最终完整编译通过。所有新／继承源文件和输出已冻结并绑定。由实现者自我反审，无独立 agent 验收或新实验。

## 7. 完成与下一个理论接口

本轮完成的是：**两份依各自记录分支的有效局部方案，在明确的共同作用覆盖和递推可实施条件下合成有效共同方案**，以及必要操作条件、共享消耗反例和有限修复。它补充已有共同支持与观察接续成果，不取代它们。

下一连接更具体地落在**相互依赖的承诺怎样取得非循环的维持根据**：一方的可行性以另一方按约行动为前提，而另一方也反向依赖时，哪些已形成的共同条件能启动并保持这条接续？不能把彼此的希望当成已经成立的保证。该接口应复用已有共同实现、支持形成和实际推进结果，区分可相容、可启动、可保持与实际履行；一般规范优先与经验全验证仍各有自己的范围。
