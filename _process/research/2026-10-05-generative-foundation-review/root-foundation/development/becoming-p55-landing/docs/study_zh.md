## {S}. 失控：经自身反映的回路所不能反映的（P55）

2026-10-11。Ren 最初问的是“wisdoms to avoid run away feedbacks”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-wisdom-from-registration.md)）。P49 把失控读作在一种不见之中运行的回路，并说这是启发，不是陈述（§{P49}）。P53 之后，AI 提议在策略的层面陈述失控问题，Ren 答：“no extra review needed, merge, then continue”。本节是统一计划 P55。它不加公理，只在被反映的条件上逐步假设平衡，属于第一部分。核心新增模块 `Becoming.Runaway`，{N_MODULE} 项定理，导入 `Becoming.Testing`，不改任何已有模块。

成果记录新增一项：[runaway-distance-unregistered](../../../../theories/becoming/results/records/runaway-distance-unregistered.md)。

```text
Result(s): 复用 subthreshold-registration（Flow.ExchangeFollows、Flow.subthreshold_alike_always、
           Flow.difference_changes_after_divergence）、testing-within-registration（Web.RegistersAlike、Web.Registers、
           Web.observed_level_registers）、laws-of-one-step（Flow.BalancesOn、Flow.Balances.on）；新增上列一项
Delta: 策略：Flow.PolicyThrough、Flow.OthersFixed、Flow.exchangeFollows_of_policy、Flow.policy_keeps_difference、
       Flow.policy_uses_after_failure。断裂的距离：Web.raise、Web.le_raise、Web.Supported.raise、Web.raise_other、
       Web.registersAlike_raise、Web.observed_raise_registers、Web.needUpTo、Web.need_le_needUpTo、Web.Dependent.raise、
       Web.break_not_bounded、Flow.BalancesOn.raise。实例：SupportDrawn.break_unregistered
Supplied premises / correspondence: 不加公理；平衡只在被反映的条件上逐步假设；策略经反映与其余固定是给出的假设
       （PolicyThrough、OthersFixed），由它们推出 ExchangeFollows；离散的步、自然数的量；读法是 AI 的，待 Ren
Evidence: 合并检查器回执 {RECEIPT}（Becoming.Runaway {N_MODULE} 项定理，全部源声明公理报告为空），外围回执 {PERIPHERY}
Boundary: 形成汲取多于更新、想要保持支持、形成策略都不推出；他者回应什么是给出的；回路与增益没有定义，失控的读法仍是读法，
          这里给的是它所依的两条定理；不含伦理谓词
Integration: 计划 P55；把 P49 失控读法所依的两点陈述为定理：对每个经反映的策略（T5 的策略形式），以及断裂的距离不被反映
```

| 声明 | 内容 |
|---|---|
| `Flow.PolicyThrough`、`Flow.OthersFixed`、`Flow.exchangeFollows_of_policy` | 形成的策略经其反映：凡它直到某步反映相同，它在所反映条件上的取用与给予在两个流中相同；其余形成在这些条件上的交换固定；两者合起来就是交换随反映（`Flow.ExchangeFollows`） |
| `Flow.policy_keeps_difference` | 对每个经反映的策略，其余固定：起始只在形成依存而不观察的储量上不同、第二个网中高 d，第一个网每步都支持它时，储量每步都高 d，形成每步都反映相同：保持支持的策略永不动用较多的储量 |
| `Flow.policy_uses_after_failure` | 对每个经反映的策略，其余固定：所反映条件上的差别在某步之前已改变，第一个网就并非此前每步都支持形成 |
| `Web.raise`、`Web.le_raise`、`Web.Supported.raise`、`Web.raise_other`、`Flow.BalancesOn.raise`、`Web.Dependent.raise` | 把储量每步抬高 d、其余不变的网；它不低于原网，支持原网所支持的，在别的条件上相同；流在一个家族上平衡，在抬高的网上也平衡；原网依存之处，抬高的网也依存 |
| `Web.registersAlike_raise` | 在网支持形成的每一步，对形成不观察的储量的抬高，形成反映相同 |
| `Web.needUpTo`、`Web.need_le_needUpTo`、`Web.break_not_bounded` | 断裂没有被反映的界：形成不观察储量，且到某一视界为止只有这个储量的所需可能不满足时，有一个抬高，在原网支持形成的每一步都反映相同，并在视界之前每步都支持它。所以断裂之前，形成所反映的什么都不界定断裂还有多远 |
| `Web.observed_raise_registers` | 观察储量时，任何正的抬高每步都被反映 |
| `SupportDrawn.break_unregistered` | 实例：较低的网在第三步不支持形成；一个抬高在原网支持形成的每一步反映相同，在第三步支持它，流在其上平衡 |

**它回答了什么。**
- **T5 的策略形式。** 计划的 T5 问：只经支持的策略能否在较低的世界保持支持、又在较高的世界用上较多的储量。对每个经反映的策略，在其余固定之下，答案是否定的：保持支持就永不动用较多的储量（`Flow.policy_keeps_difference`），动用了就已在较低的世界失去支持（`Flow.policy_uses_after_failure`）。观察储量的策略可以两者兼得（`Gauged`，§{P49}）。
- **断裂的距离不被反映。** 断裂之前，对每一个视界，都有一个储量多到撑过那个视界的世界，与实际在形成所反映的一切上相同（`Web.break_not_bounded`）。所以经支持的反馈不仅在断裂之前不变，而且不给断裂还有多远的任何界。
- **量度给出它。** 观察储量，任何差别立刻被反映（`Web.observed_raise_registers`）。

**读法（AI 的，待 Ren）。**
- 失控是这样的回路：断裂之前，它自身的反映与储量多出任意多的世界相同。它的策略再精巧，也不能用上它所不反映的。
- 要避免失控而又不放弃所有的，形成需要反映储量的东西（量度），或储量的模型（理，对反映负责的模型），或反映它的另一个形成（§{P49}）；要知道自己的动作造成什么，需要返回与关于何者无关的模型（P53）。
- 合于 Ren 4 日的话：理 须调节 心，使其正反馈循环不失控（「不能让正反馈循环失控」）。这里 心 的回路经支持反映，理 是反映储量或其模型的那一部分。

**作者反审。**
1. **增量小而确切。** `policy_keeps_difference` 与 `policy_uses_after_failure` 是 P49 阈下定理的推论，增量是策略的层面：经反映的策略加其余固定推出交换随反映。实质的新陈述是 `break_not_bounded`：对每个视界的量化。
2. **其余固定是强的假设。** 他者若回应储量本身，较高的储量可以先终结形成（`Attracting`，§{P49}）；那时 T5 的策略形式不成立。
3. **抬高的世界用同一个流。** 断裂之后，实际与抬高的世界反映不同，同一个流在抬高的世界里仍是一个平衡的展开，但不必是形成所会做的；定理只说断裂之前的反映。
4. **回路没有定义。** 失控仍是读法；这里陈述的是它所依的两点。定义回路（水平影响取用、取用又影响水平的闭合）并陈述失控本身，是下一步。
5. **“只有这个储量可能不满足”是局部条件。** 写在定理中；别的所需若也失败，抬高这个储量不足以撑过视界。

**检查。**
- 模块在暂存区对 main 的核心编译，没有错误或警告；逐条审计全部常量，公理报告全部为空。
- 合并检查器在落地队列中检查一次，通过：回执 {RECEIPT}。`Becoming.Runaway` 的 {N_MODULE} 项定理全部空依赖；包共 {N_THM} 项定理、{N_DECL} 项声明审计，核心闭包 {N_CORE} 个模块。外围桥接对这个核心重查，通过：回执 {PERIPHERY}。
- 按 Ren 的“no extra review needed”，不作独立审查。
