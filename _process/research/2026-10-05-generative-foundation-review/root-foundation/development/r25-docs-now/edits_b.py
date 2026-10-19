#!/usr/bin/env python3
"""R25 (b): the exact relation of the two presentations, World and the run, in chapter §1 and §9 (en, zh)
and the Lean package README (twentieth review A1). Becoming.lean's and World.lean's module docs are Lean
sources; their wording is left for the next checker run (study note). Writes edits_b.json for sub.py."""
import json
C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
Z = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
README = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md'
RUNS = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Runs.lean'
E = []
def r(p, old, new):
    E.append([p, old, new])

r(C, "so `World` is the reading where the readings glue, not the start.\n",
  "so `World` is the reading where the readings glue, not the start.\n\n"
  "**The two presentations, exactly.** The core presents the one unfolding twice, and the two are not yet one definition. The process family (`Generative.Process`, `Trace`, `Run`, `Frame`) and the world family (`World`, `Web`, `Flow`) are defined independently: `Becoming.World` imports nothing, and `Becoming.Frame` imports only the foundation. They are joined exactly in one direction and with loss in the other ([Becoming.Runs](" + RUNS + ")).\n"
  "- *From a world to a run, by definition.* Every world is a run of the law it shows: its webs at each step are the configurations and its relata's exchanges the moves (`World.law`, `World.run`). A run whose configurations are webs and whose moves are exchanges is a world (`Run.world`). The two readings are one by `rfl`: the world of a world's run is that world, and the world of a run has the run's configurations and moves (`World.run_world`, `Run.world_webAt`, `Run.world_move`); a world's web is its run read through the dependences its webs carry (`World.web_along`). A `World` is the curried form of a history of webs and exchanges.\n"
  "- *From a run to a world, with loss.* A run of a process whose configurations are not webs is read as a world only through its claims: each claim is a relatum active exactly where it is realized, and nothing stands, depends, draws or is exchanged (`Frame.world`). With configurations as claims that world fixes the run's states (`Frame.world_fixes_run`), not its moves. That every process is the law of some world is not derived.\n\n"
  "So, read off the Lean as it stands, the root is the run: every reading of the unfolding is a run, and a world is one by definition [AI reading, D43]. `Becoming.World` is where the import tree starts, not the root. The two families meet in 163 statements on both and through correspondence theorems; in the theorem-connectivity measure neither family reaches the other (`families_reach_each_other` false in all four directions). Defining one family from the other, so that their laws are one statement, is open (section 8.1, item 1).\n")

r(C, "**Four layers on one base.** `import Becoming` brings in the whole core.\n- The base is `Becoming.World`: the records of the unfolding (web, flow, world, exchange) with no premise among them. It imports nothing, so it is a root of the import tree. It is not the only one: the three foundation modules (`GenerativeCore`, `InquirySufficiency`, `RelationalRenewal`) are roots",
  "**Four layers, and where the import tree starts.** `import Becoming` brings in the whole core. Where the import tree starts is not the root of the theory: the process and world families are two presentations of one unfolding, a world a run by `rfl` and a run of any process a world only through its claims (section 1, “The two presentations, exactly”).\n- The import tree starts at `Becoming.World`: the records of the unfolding (web, flow, world, exchange) with no premise among them. It imports nothing. It is not the only module that does: the three foundation modules (`GenerativeCore`, `InquirySufficiency`, `RelationalRenewal`) start the tree too")
r(C, "and so are nine core modules that state laws needing no record of the unfolding",
  "and so do nine core modules that state laws needing no record of the unfolding")

r(Z, "所以 `World` 是诸读法粘合的读法，不是起点）；",
  "所以 `World` 是诸读法粘合的读法，不是起点；两种呈现的确切关系见下段）；")
r(Z, "见[研究 §91](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#91-一个展开与它的读法过程与框架从世界一侧陈述p69)与 [process-and-frame-as-readings](../results/records/process-and-frame-as-readings.md)、[configurations-alike-by-relation](../results/records/configurations-alike-by-relation.md)。\n",
  "见[研究 §91](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#91-一个展开与它的读法过程与框架从世界一侧陈述p69)与 [process-and-frame-as-readings](../results/records/process-and-frame-as-readings.md)、[configurations-alike-by-relation](../results/records/configurations-alike-by-relation.md)。\n\n"
  "**两种呈现，确切地说。** 核心把同一展开呈现了两次，两者还不是一个定义。过程一族（`Generative.Process`、`Trace`、`Run`、`Frame`）与世界一族（`World`、`Web`、`Flow`）各自独立定义：`Becoming.World` 不导入任何模块，`Becoming.Frame` 只导入基础。两者在一个方向上确切相连，在另一个方向上有所失去（[Becoming.Runs](" + RUNS + ")）。\n"
  "- *从世界到运行，按定义。* 每个世界都是它所显示之律的运行：它每一步的网是配置，它的关系项的交换是动作（`World.law`、`World.run`）；配置为网、动作为交换的运行是一个世界（`Run.world`）。两种读法以 `rfl` 为一：一个世界的运行的世界就是它，一个运行的世界有该运行的配置与动作（`World.run_world`、`Run.world_webAt`、`Run.world_move`）；世界的网是它的运行经其网所带的依存读出（`World.web_along`）。`World` 是网与交换之历史的柯里化形式。\n"
  "- *从运行到世界，有所失去。* 配置不是网的过程，其运行只经它的主张读作世界：每个主张是一个关系项，恰在实现处活跃，没有什么立着、依存、汲取或交换（`Frame.world`）。以配置为主张时，这个世界固定运行的状态（`Frame.world_fixes_run`），不固定其动作。每个过程都是某个世界的律，这一点没有推出。\n\n"
  "所以照 Lean 现在的样子读，根是运行：展开的每种读法都是一个运行，世界按定义就是一个〔AI 读法，D43〕。`Becoming.World` 是导入树开始之处，不是根。两族经 163 条同时用到两族的陈述与对应定理相遇；在定理层面的连通度量中，哪一族都不到达另一族（`families_reach_each_other` 四个方向都为假）。由一族定义另一族，使它们的律成为一个陈述，仍开放（§8.1 第 1 项）。\n")
r(Z, "核心（基底 `Becoming.World`，L0 及其两个基础模块，加 L1–L4；导入树从基底开始，",
  "核心（`Becoming.World`，L0 及其两个基础模块，加 L1–L4；导入树从 `Becoming.World` 开始，那是导入树的起点，不是理论的根，见 §1“两种呈现，确切地说”；")

r(README, "`import Becoming` brings in all four and the base. The import tree starts from the base, `Becoming.World`, which imports nothing; the labelled process and the frame enter as readings of it (`Becoming.Labelled`), and no module free of the labelled process imports the frame:",
  "`import Becoming` brings in all four and the base. The import tree starts at `Becoming.World`, which imports nothing; that is where the tree starts, not the root of the theory. The process family (`Generative.Process`, `Run`, `Becoming.Frame`) and the world family (`World`, `Web`, `Flow`) are two presentations of one unfolding, defined independently and joined exactly in one direction: a world is a run of the law it shows by definition (`World.run_world`, `Run.world_webAt`, `Run.world_move`, all `rfl`, in [`Becoming.Runs`](Becoming/Runs.lean)), while a run of a process whose configurations are not webs is read as a world only through its claims, keeping neither its moves nor any standing (`Frame.world`, in `Becoming.Labelled`). Read off the Lean as it stands, the root is the run (the AI's reading, D43); making one family defined from the other is open (chapter §8.1, item 1). `Becoming.Labelled` states the readings, and no module free of the labelled process imports the frame:")

if __name__ == '__main__':
    json.dump(E, open(__file__.replace('.py', '.json'), 'w'), ensure_ascii=False, indent=0)
    print(len(E))
