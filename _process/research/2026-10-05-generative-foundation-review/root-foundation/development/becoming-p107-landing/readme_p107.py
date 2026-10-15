#!/usr/bin/env python3
"""P107: the Lean package README rows for Novelty, Reading and Readings, the Imbalance row after Ren's
adoption, and the within-layer imports (run with the checkout root as argument; anchors asserted)."""
import sys
from pathlib import Path

p = Path(sys.argv[1]).resolve() / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md'
s = p.read_text()


def sub1(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)


sub1('不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；是否采用由 Ren 定）：',
     '不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；Ren 2026-10-14 采用，见 `Becoming.Reading`）：')
sub1('不采用，核心的规律仍以平衡为局部条件；读法是 AI 的，待 Ren / imbalance counted as a relatum, proved equivalent first '
     '(Ren, 11 October 2026: “please”; adoption is Ren\'s):',
     '采用之后，核心现有的规律仍以平衡为局部条件陈述；读法是 AI 的，待 Ren / imbalance counted as a relatum, proved equivalent '
     'first (Ren, 11 October 2026: “please”; adopted by Ren on 14 October 2026, see `Becoming.Reading`):')
sub1('nothing is adopted, the laws of the core keeping balance as a local condition; the readings are the AI\'s, pending Ren |',
     'adopted, the existing laws of the core keep balance as a local condition in their statements; the readings are the '
     'AI\'s, pending Ren |')
imb_end = ('the existing laws of the core keep balance as a local condition in their statements; the readings are the AI\'s, '
           'pending Ren |\n')
NOVELTY = ('| L3 | [`Becoming.Novelty`](Becoming/Novelty.lean) | 只用水平的回返、新与遗忘（Ren 2026-10-14：“trapped by our speculative '
           'conditions”，随后“please, finish all”）：任何依存网上，不用流、平衡、损失或世界的有限，每条规律写入部分的一个状态：存量从某步起'
           '在界内的家族回返（`Web.revisits_of_bounded`、`Web.returns_of_bounded`）；在有限多步上每步都新的家族在其中某步超出界'
           '（`Web.exceeds_of_new`），所以新而不止就是无界的增益（`Web.unbounded_of_new`，由 `Web.counting` 实现）；在界内、交换不止的'
           '家族与有限的整体不承载其历史（`Flow.uncarried_of_bounded`、`World.forgets_of_bounded`）；每次变化都下降时变化不无尽复现'
           '（`Web.rests_of_loses`）；Entropy 在第一律之下的形式是其情形（`first_law_cases`） / returning, novelty and forgetting on '
           'the levels alone: on any web, with no flow, balance, loss or finite world, each law with one state of the part written '
           'into it: a family whose stock stays within a bound returns; a family new at each of finitely many steps exceeds the '
           'bound at one of them, so novelty without end is gain without bound (realized by `Web.counting`); a bounded family '
           'exchanged with without end, and a finite whole, do not carry their history; with loss at each change, change does not '
           'recur without end; Entropy\'s forms under the first law are its cases (`first_law_cases`) |\n')
sub1(imb_end, imb_end + NOVELTY)
rel = [l for l in s.splitlines(keepends=True) if l.startswith('| L4 | [`Becoming.Relevance`]')]
assert len(rel) == 1
READING = ('| L4 | [`Becoming.Reading`](Becoming/Reading.lean) | 从交换读出的前提（Ren 2026-10-14 采用把整体的其余算作关系项）：把活跃读作'
           '交换、汲取读作所取，只有活跃者给与取，对每个流成立（`Flow.readOff_acting`、`Flow.readOff_taking`）；每个世界算入其余'
           '（`World.withRest`）都平衡，其平衡恰是其余从不活跃（`World.withRest_balanced`、`World.withRest_closed_iff`）；交换之律下把'
           '要求读作交换所回应的，活动对每个所需都需要支持，四个联结前提都不用前提成立（`ExchangeLaw.readWeb_dependent`、'
           '`ExchangeLaw.readWorld_glue`）；要求是律的反事实，没有历程固定它（`ExchangeLaw.requirement_beyond_course`） / premises read '
           'off the exchange (Ren adopted counting the rest of the whole as a relatum on 14 October 2026): with activity read as '
           'exchanging and drawing as taking, only active relata give and take, for every flow; every world with its rest counted '
           'balances, its balance being exactly the rest never active; under a law of exchange, with requirement read as what the '
           'exchange responds to, activity needs support for every need, so the four tying premises hold with no premise; '
           'requirement is a counterfactual of the law that no course fixes |\n')
READINGS = ('| L4 | [`Becoming.Readings`](Becoming/Readings.lean) | 一个展开在语境中的读法：一个运行在语境中的诸识总是一个世界的关系项，'
            '不用粘合，量子的识亦然（`Contextual.world`）；所立与交换恰在流平衡处同样读出变化，所以世界的平衡是两种读法的粘合'
            '（`Flow.changeReadings_glue_everywhere_iff`）；算入其余时两者处处粘合，每个世界都是交换之律的一次运行（`World.unity`）；'
            '在同样的不变标准下，意义在某个边界内成立只能因为对一切成立（`presupposition_iff_all_of_invariant`、'
            '`bounded_invariant_iff`，重述 `Becoming.Boundaries`） / one unfolding, read in context: the registrations in context of '
            'a run are always the relata of one world, with no gluing, quantum registrations included; the standing and the exchange '
            'read one change alike exactly where the flow balances, so a world\'s balance is the gluing of two readings; with the '
            'rest counted they glue at every step and every world is one run of the law of exchange; under the same standard of '
            'invariance, significance holds within some boundary only by holding for everything (restating `Becoming.Boundaries`) |\n')
sub1(rel[0], rel[0] + READING + READINGS)
sub1('`Regions` 导入 `Admission` 与 `Continuation`。L4 内：', '`Regions` 导入 `Admission` 与 `Continuation`；`Novelty` 导入 `Entropy` 与 `Imbalance`。L4 内：')
sub1('`Relevance` 导入 `Boundaries` 与 `Ranking`）。', '`Relevance` 导入 `Boundaries` 与 `Ranking`；`Reading` 导入 `Counterfactual`；`Readings` 导入 `Reading` 与 `Boundaries`）。')
sub1('`Regions` imports `Admission` and `Continuation`; within L4,', '`Regions` imports `Admission` and `Continuation`; `Novelty` imports `Entropy` and `Imbalance`; within L4,')
sub1('`Relevance` imports `Boundaries` and `Ranking`).', '`Relevance` imports `Boundaries` and `Ranking`; `Reading` imports `Counterfactual`; `Readings` imports `Reading` and `Boundaries`).')
p.write_text(s)
print('Lean README: three rows, Imbalance row, imports')
