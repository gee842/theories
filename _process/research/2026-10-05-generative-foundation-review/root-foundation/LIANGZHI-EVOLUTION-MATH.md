# 良知演化方向的形式接口：后果、复制机会与回应结构的传递

2026年10月7日，Asia/Bangkok。AI 撰写，支持 [Ren 授权的生成演化方向](../../../../sources/15-codex-theory-conversations/2026-10-07-liangzhi-generative-evolution.md)。本轮处理**实际回应改变后续条件 → 差异复制 → 后继的回应结构**之间的精确对应，不把选择成功定义成仁，也不把化学修复的 A 类型命名为良知。

**状态：新增19项声明已实际通过 Lean 4.29.1 检查。** 新文件为 [ConsequenceTransmission.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/ConsequenceTransmission.lean)，检查器与回执在[实验目录](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/README.md)。所有数学结论限于下面明列的模型与条件。

## 1. 继承了什么，本轮新增什么

[既有构造](../../../history/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-INTEGRATION.md)已经从两种响应都不存在开始，连接形成、占据位置、恢复捕获、实际捕获和同型复制。它也保留其他类型继承已修复位置的反例。因此本轮不能把「后果进入复制」再说成首次实现。

[旧选择分析](../../../history/2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-RETENTION-SELECTION.md)给过连续时间生成元的出生／损失公式及有限时域论证，但它明确不是 Lean 证明。本轮迁移的是其中**一次复制或计数不变事件的相对份额准则**。没有迁移死亡分母、连续时间过程、Dynkin 公式、严格有限时域概率下界或无限期演化结论。

新增的传递接口进一步分清：更多机会由某类模板获得，不等于后继中必有更多同类回应结构。原 native 规律的同型复制给出其中一个实际支路；允许传递改变结构的四格推广保持独立范围。native 中的两种类型、修复贡献、复制与同型传递在同一个既有事件过程内取得具体含义；四格统计接口则是明确的推广，尚未接成该过程的非忠实传递事件。两处都不预先设定独立主体、私人利益或外部适应度评判者。

## 2. 一步带权规律及其精确条件

设当前两类结构数量为 `a,h`，`n=a+h>0`；下一项被选择的事件属于下列三类：

| 事件类 | 权重 | 之后 A 的数量／总数量 |
|---|---:|---:|
| 同型复制 A | `x` | `(a+1)/(n+1)` |
| 同型复制 H | `y` | `a/(n+1)` |
| 两类计数都不变 | `z` | `a/n` |

权重为非负整数，`W=x+y+z>0`。事件概率是其权重除以 `W`；具有共同分母的有理权重可以缩放到这种表示。**权重规律是明列的局部输入，本轮没有从 core 唯一推出它。** 如果解释为 native 过程的下一事件，必须保证相应事件确实容许，并把所有被考虑的复制与计数不变事件分配到这些权重。其他可能事件若被排除，应说明这是条件化的事件域或已将其率设为零，不能默默忽略。

在共同正分母 `D=W*n*(n+1)` 上，下一步与当前份额的分子分别为：

\[
N_{\mathrm{next}}=n[x(a+1)+ya]+za(n+1),\qquad
N_{\mathrm{now}}=Wa(n+1).
\]

`denominator_positive` 检查 `D>0`；`numerator_balance` 检查不使用自然数截断减法的平衡式：

\[
N_{\mathrm{next}}+ya=N_{\mathrm{now}}+xh.
\]

`strict_increase_iff`、`neutral_iff`、`strict_decrease_iff` 因而给出增加、相等、下降的精确交叉乘积条件；增加恰好对应 `xh>ya`。分子恒等式对所有自然数成立，但份额及概率解释仍需上述正分母条件。

`shared_access_is_neutral` 检查 `x=k*a, y=k*h` 时的相等：每个模板同等获得共同复制支持，可以增加可用复制权重，却不因这一共同项本身提高 A 的下一步期望比例。**这不是所有共享改善、任意总体统计、存在新形成或损失时的中性定理。** 原 formed-variant 构造中新形成与数量相关性已经破坏过更宽泛的推断，本轮保持这些反例。

被归为 `z` 的事件可以改变支持、位置或后续反应机会；它只在本次计数比较中中性，不代表对后续历程无关。

## 3. 权重怎样接回实际生成史

Native 接口使用原 `FormedSelection.Enabled`，定义：

- A 的 bulk 权重在原 bulk A 反应容许时为 `b*aCount`；H 为 `b*hCount`；
- local 权重 `l` 只赋予当前确实容许的 local copy，取决于实际 resident、localFuel 和剩余材料条件；
- `b,l` 是共同的非负事件系数；没有读取「值得增强」「仁」或某个分析者的成功分数。

`positive_a_weight_has_native_event` 与 H 对应命题证明：正复制权重至少有一项容许的原生复制事件；构成 `Step` 还需要原来的状态有效性。它们没有证明任意 `z` 都能对应某个原生中性事件，也没有证明完整随机过程之间的 refinement。

两个实际支路采用同一个原始 native 规律：

**已有正支路。** 原 `initial → … → repaired → captured → copied` 历程完整保留。repair 之后尚无 localFuel；capture 将真实 source 转为 localFuel。`actual_capture_changes_copy_access` 证明在 `b=l=z=1` 的所选事件域，权重由 `(0,0,1)` 变为 `(1,0,1)`，A、H 各一个时产生正的复制份额比较。原有形成与复制历程不是新证明的原创内容，新检查的是其边界到本轮权重接口的对应。

**本轮补出的双类保留移交支路。** 从 `A=H=0, common=6, source=1, material=3` 出发：

> 形成 A → 再形成 A → 形成 H → A 关联 → 修复 → resident 磨损 → H 关联 → 捕获。

到达时仍有一个 A 和一个 H，localFuel 为一，resident 是 H。下一项真实 H local copy 生成第二个 H。`actual_transfer_with_both_structures_present` 逐步检查这一八事件前缀及复制事件，并证明当前权重为 `(0,1,1)`、比较方向为负。它没有在中间重置材料、恢复已失去的 A 或补充支持。修复的实际作用被保留，但后续访问关系已经变化。

`same_composition_opposite_access` 表明两支路在当前类型数量同为 `1,1` 时具有相反的复制访问差异。它们有不同的起始条件和实际历史，不是配对随机实验，也不是同一祖史的因果控制反事实。`reached_neutral_event_is_native` 另外证明这些已达到状态中的 damage 确实是计数不变的原生事件，可供该处 `z=1` 对应。

这两支路仍受原有限 stock 的限制。其先前已证明的有限历程界限保持有效；本轮没有将其改成无限更新或种系稳态。

## 4. 模板获得复制机会，与回应结构被传下去

引入一个独立的有限传递接口，四个权重分别是：

\[
AA,\quad AH,\quad HA,\quad HH.
\]

第一个字母表示模板的结构，第二个表示新增后继的结构。它们读取复制关系中的两个位置，不是原始的两个自足价值主体。若应用于实际过程，模板必须存在，事件必须能够生成相应后继；数学表格本身不实现这些转化。

模板机会按行计数：

\[
x_T=AA+AH,\qquad y_T=HA+HH.
\]

新增后继结构按列计数：

\[
x_D=AA+HA,\qquad y_D=AH+HH.
\]

`transmission_preserves_total_event_weight` 检查二者总权重相同；没有以归一化变化制造差异。`transmitted_structure_increase_iff` 将上节结果应用于真实被传递的列计数，其精确增加条件是

\[
h(AA+HA)>a(AH+HH).
\]

模板机会偏向 A 所要求的却是

\[
h(AA+AH)>a(HA+HH).
\]

**忠实传递 `AH=HA=0` 是两判准重合的充分条件，并不是回应结构增加的必要条件。** `faithful_transmission_matches_template` 和 `faithful_increase_iff_template_increase` 检查此桥梁；`balanced_transfer_matches_template` 给出更弱充分条件 `AH=HA`，允许两个方向都有非忠实传递。其他不平衡传递也可能使回应结构增加，是否增加由上面的精确不等式决定。

`native_copy_transmits_its_response_structure` 连接回原 native copying 定律：A copy 的模板确实存在，增加一个 A 而保持 H；H 对称。因此 native 程序实现了这个**已指定响应类型**的忠实传递。它不保证后继所有属性都忠实，也不等于证明遗传或发育架构的起源。

四格非忠实支路是本轮**明确新设的传递统计推广**；原 native 事件中仍没有 mutation。不能把下面的代数反例写成原化学事件已经生成了不忠实后继。

## 5. 全部通道为正的反例

取 `a=h=1`、`z=0`、四格权重

\[
(AA,AH,HA,HH)=(1,5,2,2).
\]

所有传递通道都有正权重，模板机会是 A 六次、H 四次；被传下去的结构却是 A 三次、H 七次。在共同分母 60 上，当前份额分子为 30，模板机会若被忠实实现会给出正比较，实际列计数的下一步分子为 26，即 `13/30 < 1/2`。

`positive_template_advantage_can_reverse_in_transmission` 检查全部正权重、总量十以及这两个相反方向和 `26/60` 的精确数值。反例保留两个初始类型，不靠全灭、空总体或改变分母制造结论。它否定的是「不对传递作任何要求，只凭模板机会占优就推出回应结构增加」；它不证明忠实性必要，更不反驳真实社会关切的演化可能。

## 6. 对良知演化研究的含义与下一对应

这组结果支持一项具体研究程序：先独立识别实际感应、照料、理解或自我纠正的结构；说明其活动怎样改变共同生活与后继形成的条件；再追踪那些条件怎样通过实际访问、再形成和发育传递，改变这些结构的继续。不能只观察载体数量或共同改善，就宣告当前响应倾向被保留。

种系中形成、个体中先于显性推理而出现的能力，是可以继续研究的候选；当前数学没有把它作为先验个体偏好塞入根核。不过，本轮 A 只由原反应规律中的修复能力独立识别；社会感应、非工具性关切、意识经验和伦理正确性均未被这个类型实现。[评价继承研究](../../../../theories/becoming/history/EVALUATIVE-SUCCESSION.md)已把习得评价影响接到实际不同的后继、鲜明标记的新证据及其改变的选择，不能再说这类传递全都缺失。下一接口是不同可传递响应架构在共同发展中如何发生差异再形成，并独立识别它们何时构成社会关切；不能仅把 A 政名为良知。

[评价与谱系](../../../../experiments/valuation-development/README.md)已有共同过程中的评价形成、路线修订、继承与支持更新；[renewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/renewal/README.md)已有其所定规律族上的继续条件。这里不给它们补一个未经证明的唯一有利方向，也不重新宣称它们缺失。新一步准则可以供应其**传递对应的一个边界**；无限历史、相对选择与更新规律的完整组合仍需实际给出兼容关系。

## 7. 验证与依赖

以 [check.py](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/check.py) 在新临时目录编译冻结源文件。编译器固定为既有 Lean 4.29.1，哈希与原形成结果回执核对。既有 `GenerativeCore`、`FormedSelection`、`FormationRoot` 均保持原源字节，再编译后检查全部已请求依赖审计；新增文件的每项 `theorem` 都要求对应审计。

通过状态、源／检查器／编译器／日志的哈希以及精确新声明数见[正式回执](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/verification.json)。每次失败也连同源快照保留在 `evolution/checks/`，不会以通过的文件覆盖失败记录。标准逻辑公理与 supplied local inputs 分别报告；无自定义公理不等于已经完成无假设目标。


最终通过尝试为 [1791373894116817000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/checks/1791373894116817000/receipt.json)：四个模块共90项审计（核心18、原形成43、原核心适配10、本轮19）。新增19项中6项不依赖命名公理，其余13项只依赖标准 `propext`；没有新增伦理公理、证明占位或原生求值绕过。继承模块仍按其原有标准逻辑依赖报告。

首次尝试 [1791373695246850000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/checks/1791373695246850000/receipt.json) 中命题编译成立，但两个无用简化参数触发警告，严格检查判为失败。清理警告并减少算术证明依赖后的第二次尝试 [1791373791396295000](../../../../experiments/shared-renewal-capability/regulation/retention/formation/evolution/checks/1791373791396295000/receipt.json) 中，一个重排证明未先消去结构投影而失败；改用直接加法结合、交换证明后通过。数学命题、事件规律和检验范围未随修复扩大。
