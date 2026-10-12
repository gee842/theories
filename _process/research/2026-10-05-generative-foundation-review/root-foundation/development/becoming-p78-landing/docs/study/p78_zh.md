**P78：步序号的重新奠基。** 按 Ren 的“move towards 100%”，像 P69 对出发点那样，检查零前提计划中共享的离散步序号这一承诺。新的核心模块 `Becoming.Order`（只导入 `Becoming.Sampling`），不用公理，不加前提，不改动已有模块。它给出与 Sampling 的较粗读法相反的两个动作：插入空步，以及以相反次序取两个交换。
- **停顿。** 经停顿读的世界恰在原世界满足前提时满足它们（`World.stutter_premises_iff`），任何段上的总量就是所读之段的总量（`stutter_total`），生起、止息与变化恰在原来复现时复现（`World.stutter_arisingRecurs_iff`）。改变的是每步所计的：空步出现得任意晚时没有什么无终地更多（`Flow.sample_not_more`），每步读两次时储备须加倍（`Lapse.reserve_step_relative`）。
- **交换次序。** 两侧分开的相继两个交换可以以相反次序取：平衡、耗散与体现恰在原来成立处成立，段上的计数与总量保持（`World.commute_laws`、`World.commute_counts`），在任意次这样的交换下也如此（`Reorders.laws`、`Reorders.totals`），即 Mazurkiewicz 迹等价。
- **次序携带什么。** 次序经依存与共享的关系项被登记：在 `Crossing` 中次序相反时一个关系项在没有支持时活跃，在 `Arising` 中一个关系项在活跃之前给予（`Crossing.order_registers`、`Arising.order_registers`）。

读法是 AI 的，待 Ren：对规律、总量与复现，步序号不携带变化次序以外的东西；速率相对于读法的单位；规律所需的次序会是交换的偏序，逆方向（Foata 范式）没有证明。由本会话的一个 Opus 子代理构建（338 个常量，公理报告为空）。尚无独立审查。
