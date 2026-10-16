# 相互依赖怎样有根据地启动与维持 / Seeded mutual continuation

2026-10-08。AI 撰写，接续 Ren 的[“继续”](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md)与理论推进重心。上一轮[共同接续](JOINT-CONTINUATION-INTEGRATION.md)把递推共同可实施作为合成前提；本轮推进到**已有共同支持 + 一步互相维持的规律 → 依记录分支方案的递推共同可实施**。

**结果：相互依赖可以在时间上有根据地接续，而不需要把另一方尚未实现的未来当作当前保证。** 已有条件支持本步活动，本步的共同后果再支持下一步；在每个实际可能分支都成立的局部规律下，这个连接可以归纳到任意给定有限时域。它不证明互相许诺会自动形成启动条件。

**Result:** seeded one-step mutual preservation and joint availability derive the previous recursive compatibility condition for locally valid observation-dependent plans. With faithful projections, the existing composition theorem then gives a valid paired plan. Initial support, actual successor availability and scope of the admitted transitions remain explicit hypotheses.

## 1. 接续的是哪个缺口

已有[完整支持](EXPLANATORY-GLOBAL-REALIZATION-INTEGRATION.md)和[变化支持](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md)已证明条件性的共同取得、准备保持、修复与完成，并保留准备始终存在而调度从不推进的历史。本轮不重做这些结果，也不把相容、启动、保持与实际履行的区别说成首次发现。

上一轮 `joint_plan_composition` 已将两个依各自记录分支的方案合成，但调用者须给出整棵方案树上的 `compatible` 证明。新的 `compatible_from_seed` 允许以初始共同条件和统一的一步规律履行这个义务。`seeded_joint_plan` 直接调用上一轮合成定理，接回同一套 `Plan`、`post`、`works` 与局部证据类，避免另造一个孤立的“循环可行”模型代替原问题。

“承诺”在本轮具有有限含义：给定方案对其后续实施条件的要求。数学对象没有自行包含人际承诺的正当性、信任、权限或参与动机。这些关系并未被否认；它们须在应用的对应说明中获得内容。

## 2. 从同一历史分化条件，避免同期循环

仍从同一共同状态 `X`、联合转移 `joint` 和两种局部投影出发。`R(x)`、`S(x)` 描述本次接续所需的两项关系性条件，例如已形成的传递通道和仍可承担的共同支持；它们不必属于两个独立实体，也不要求相互排斥或统计独立。把两项条件写开，是为了审计每个后果的依存。

本轮的互相维持义务是：

\[
R(x)\land S(x)\land joint(x,(u,v),y)\Rightarrow R(y),
\]
\[
R(x)\land S(x)\land joint(x,(u,v),y)\Rightarrow S(y).
\]

右边的下一步条件由左边**已经成立的本步条件**和实际转移推出。没有用尚未证明的 `S(y)` 推出 `R(y)`，再反向用 `R(y)` 证明 `S(y)`。`mutual_history` 检查：初始两条件成立且每步遵循这种规律的任意给定历史，在每个自然数位置都保留两条件。它是已有历史上的保持结论；不从无后继的转移关系中制造历史。

这也不要求所有实际循环都可切成这种离散顺序。同步耦合或连续关系可能需要别的表示；本轮给出一种充分的时间归纳接口，而非对所有循环的唯一解释。选定研究起点已有根据，不等于宇宙起源或生成基础无需进一步解释。

## 3. 从一步义务接到观察分支方案

新定理保留五组公开前提：

| 前提 | 在证明中的作用 | 本轮没有替它证明什么 |
|---|---|---|
| 初始覆盖和共同支持 | 所有与已取得记录相容的共同候选都投影到局部候选，并满足 `R ∧ S` | 人们实际取得了可靠的启动证据 |
| 两份局部方案有效 | 各自选择局部容许的活动，保持自己的状态要求，并随自己的记录分支 | 两份方案的目标已经穷尽整体的善 |
| 共同作用覆盖 | 每个共同后继投影都在局部模型承认的转移内 | 隔离实验的规律自动适用于共同活动 |
| 一步共同可实施 | 当 `R ∧ S` 成立时，每一对局部容许活动都共同容许，且至少有一个实际后继 | 任意分别合法的活动天然相容，或存在公平调度 |
| 一步互相维持 | 每个被模型容纳的共同后继都保持 `R ∧ S` | 现实全部扰动都服从这个规律 |

归纳步骤是：局部方案给出当前选择及其局部容许性；已有共同支持使这对选择具有实际后继；每个后继由作用覆盖进入对应局部证据类，同时由维持规律继续满足共同支持。因此，每个实际记录分支都能再次应用相同论证。

由此推得上一轮的递推 `compatible`，再由原有合成定理推得配对方案 `works`。**新增的是把整棵树上的递推操作条件归约为初始与一步义务的已检查接口。** 一步义务仍可能难以履行；对所有局部容许活动对的量化很强，超出固定方案实际到达的节点，因此这是充分条件，不是必要条件。失败时应检查更窄的已授权活动关系、实际方案或其他路线，不应断言所有共同接续都不可能。

## 4. 启动、空保证与共同相位

保留两种直接反审：

1. 两个“如果对方最终发生，我方也最终发生”的命题，可以同时成立而双方永远都不发生。`reciprocal_eventual_promises_can_be_empty` 给出自然数历史上的见证。它否定无条件的启动推论，不否定有实际支承的相互依赖。
2. 无任何后继的转移关系自动满足“每个后继都保留条件”。`preservation_without_availability` 检查这种空真。因此，保持条件不能代替存在可执行的下一步；新合成接口把这两项分开。

一个明确的共同配置例进一步区分形成和维持。配置记录左右两项已形成的活动条件及一项仍可用的启动能力。每个 `tick` 把旧右条件传到新左、旧左传到新右，启动能力暂时不变。这是给定的离散传递规律，不是已验证的生物更新或通用守恒律。

- 两边最初都没有条件，反复传递始终为空；再多轮循环也不会产生起点。
- 只有一边已有条件时，条件随步数换位，但任意时刻都不具备两边同时成立的共同准备。这对本轮选定的共同目标构成失败，**并非所有交替活动都失败**。
- 若配置中确有启动能力，明确的 `ignite` 转移使用它，形成两边共同条件，并将启动能力置为不可再用。之后给定的 `tick` 历史在每个自然数位置保持共同准备。
- 没有这项启动能力的空配置不允许该启动转移。起点不是由“对方会支持我”的文字产生，也没有从模型外无记名地赠送；不过它的形成历史、实际成本和启动规律仍是明确输入。

这使肯定结论和失败共享同一套条件含义：`active_run_iff` 给出这一传递律下共同准备的精确保持关系；实际储备允许的启动则改变当前配置。正例不是偷偷把失败中的空状态改名为成功状态。

## 5. 对尺度关系与生成性对齐的意义

静态关系图上的一个环，可能表示已经运转的相互维持，也可能表示无人能开始的互相等待。仅保留连接方向会丢掉**启动是否已形成、后果在何时可用、活动对能否共同实行**。对于声称足以指导接续的尺度描述，这些区别必须由描述本身或有根据的对应关系保留。这里是一个具体的表示义务，不是已经证明所有尺度都需要同一套变量。

实际责任和支持也不能仅靠相互条件句闭合。例如，机构以另一机构将来提供支持作为自己的履行前提，后者又采用对称前提；这两份声明没有独自给出当前启动能力。合理的共同安排可以明确已有支持、启动活动及其后果怎样接到后续承担。谁应承担启动成本、怎样保护可能受损者以及何时结束，仍由已完成的 G0/J 实践判断承担规范论证。

相互维持因而可以是一种有条件的生成关系：先前活动已经形成的关系参与下一步，并在下一步得到保留或改变。循环的形状本身既不证成其善，也不使它成为无效解释。破坏性组织同样可能满足保持定理；本轮没有把可持续性偷换成伦理正当性。

## 6. 来源、对手解释与验证

Abadi and Lamport, [*Composing Specifications*](https://lamport.azurewebsites.net/pubs/abadi-composing.pdf), introduction, PDF pp. 3–4 (printed pp. 75–76), explicitly contrasts conditional safety guarantees with mutually conditional eventual outputs. The latter allow a composite that never starts. This is an established limitation of unqualified composition. Our seeded finite observation-tree result uses ordinary induction and does not reproduce their general temporal proof rules, realizability account or completeness results. This round read the specified opening example and discussion; the source remains link-only.

常规对手解释已经足够给出本轮形式推论：带初始条件的不变式归纳、条件保证与模拟关系。理论贡献是把它们接到本项目中从尺度描述、取得记录、局部方案到共同接续的推导链。没有通过改名主张新数学、生成本体的唯一必要性或优于现有组合验证理论。

**实质反审：** `R`、`S` 是不是只把所需结论换名为前提？它们由应用者给出，必须有独立的实际含义；定理不为其内容背书。证明的新推论是：一步可实施和保持义务如何在真实投影与局部方案下覆盖全部有限记录分支。若应用者把“这个完整方案成功”直接定义成 `R`，形式定理虽可用，解释推进却为空；本轮具体传递例没有这样定义。

**实质反审：** 肯定例是否解决支持形成与现实部署？没有。启动能力初始已有，`ignite` 的规律被供给；`tick` 被选作实际后续。扰动、稀缺供给、非原子检查、通信时延、合规动机与无限物理实现均未推出。已有变化支持中的无进展反例仍有效。

[源码](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/SeededContinuation.lean) · [重现脚本](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_seeded_continuation.py) · [实查回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/seeded-continuation-verification.json)。**13项新定理／13项新审计通过，6项空依赖、7项标准逻辑依赖；另重放30项继承审计。** 新结果不依赖经典选择，无自定义公理或证明缺口。Lean 4.30.0-rc2，固定 Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`。首次检查因两个未使用变量警告而未通过严格门槛；改为明确的忽略绑定后，完整构建通过。冻结源码与输出均保存。这里是作者反审，不是独立 agent 验收；无新经验实验。

## 7. 本轮完成与剩余连接

本轮已完成**有根据起点和一步相互维持 → 有限观察方案的递推共同可实施 → 已有局部要求的共同保持**。不能再把这个有条件的合成连接列为未做；上一轮的共享耗尽反例和本轮的空保证、缺少启动能力及相位错开都作为结果保留。

下一理论接口是**启动与维持条件的证据何时足以授权实际共同行动**：当前证明要求初始相容范围内所有候选都已有共同支持；只有真实状态满足而参与者无从确认，或确认后支持发生改变，可能不足以兑现这项前提。后续须先信用既有取得证据、时效校准、变化支持及监测／交接结果，再检验它们怎样共同履行这里的前提。它不是重新证明一般保持定理，也不是把新的实验变成本轮理论完成门槛。
