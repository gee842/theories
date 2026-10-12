**P79：一步的规律就是一步的全部规律。** 按 Ren 的“move towards 100%”，此前只对计数成立的强意义上的完备（`tally_iff_counted`），这里对 Locality 的一步之律证明。新的核心模块 `Becoming.OneStep`（导入 `Counting` 与 `Sampling`），不用公理，不加前提，不改动已有模块。
- **每个条件下精确。** 一个模式（家族成员的通过、取用者之数、是否有交换）恰在服从每步之律时由某个世界显示（`OneStep.every_iff`）；在被平衡、耗减、封闭或两者兼有的家族上，恰在还服从该条件之律时（`OneStep.balance_iff`、`OneStep.runsDown_iff`、`OneStep.closed_iff`、`OneStep.runsDownClosed_iff`）；所以一个性质在每个这样的步成立，恰在它对服从该律的每个模式成立时（`OneStep.laws`）。跨一个家族的运行，唯一多出的律是每步之后所立就是下一步之前所立（`OneStep.Chained`、`OneStep.run_every_iff`）。
- **脊柱此前未陈述的两条律。** 有所取就有取用者（`Flow.sign_uptake_le_takers`）；所取不超过所立加所给（`Flow.BalancesOn.taken_le`）。没有前者，所陈述的律允许没有世界显示的模式（`OneStep.stated_not_realized`）；有了它，对耗减且封闭的家族它们就是全部规律（`OneStep.runsDownClosed_iff_stated`）。

读法是 AI 的，待 Ren。未涵盖：给家族的关系项之数；逐步选择家族的运行。由本会话的一个 Opus 子代理构建（379 个常量，公理报告为空）。尚无独立审查。
