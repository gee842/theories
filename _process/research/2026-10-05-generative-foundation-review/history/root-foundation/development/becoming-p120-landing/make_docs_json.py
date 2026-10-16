#!/usr/bin/env python3
"""P120: write docs.json, the texts apply_docs.py inserts (kept here so the JSON stays valid)."""
import json
from pathlib import Path

LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Remainder.lean'
RECORD = '../results/records/what-a-cut-loses.md'
SOURCE = '../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
QUOTE = 'how how accurate can we do that uh what is the limitation do we have losses'

bullet = """* `Becoming.Remainder` (L4): what a cut loses, for every schedule of couplings, with no premise
  beyond the strengths each statement names. The carried amount is order `j` plus what `j + 1`
  responses in turn carry from it, so a cut loses exactly that. Order `j` misses something exactly
  where a gap is conveyed through `j + 1` responses in time order, and it is exact from every start
  exactly where no chain of `j + 1` couplings in time order ends there; a finite order is exact
  exactly where those chains are bounded. Where the schedule has settled, they are bounded exactly
  where no loop of the couplings that go on lies upstream, with no listing of every condition, and
  the most difference that can arrive grows faster than every polynomial only through such a loop."""

scope = (
    '    "Remainder: for every schedule of couplings, the carried amount is order j plus what j + 1 "\n'
    '    "responses in turn carry from it; order j misses something at a condition exactly where a gap "\n'
    '    "is conveyed there through j + 1 responses, each reading a level the one before had reached, "\n'
    '    "and is exact from every start exactly where no chain of j + 1 couplings in time order ends "\n'
    '    "there; a finite order is exact from every start exactly where those chains are bounded; a fed "\n'
    '    "loop of recurring couplings upstream leaves every order inexact, and where no coupling reads a "\n'
    '    "level from step N on, order N is exact; where every coupling from step N on recurs, the chains "\n'
    '    "are bounded exactly where no loop of the couplings from step N on lies upstream, with no "\n'
    '    "listing of every condition, and without such a loop the carried amount is at most a "\n'
    '    "polynomial; the results of Loops on exactness follow as instances. "\n')

readme_row = (
    '| L4 | [`Becoming.Remainder`](Becoming/Remainder.lean) | 截断所失：任意耦合时程（除了各定理所写的强度不加前提）：一次回应从给定'
    '水平所携带的（`responded`），j 次回应依次所携带的（`responses`）；所携带的量是 j 阶之下各阶加上 j 次回应依次从所携带的量所携带的'
    '（`carried_eq_orderBelow_add`），所以在 j 阶截断恰好失去 j + 1 次回应所携带的（`carried_eq_carriedWithin_add`），所失随阶下降'
    '（`responses_antitone`），至多是 `Becoming.Loops` 的界（`responses_le_missBound`），自环恰好失去这个界'
    '（`Loops.SelfLoop.responses_eq`）；某步的耦合（`CouplesAt`），经 j 次或更多回应传到（`ConveyedThrough`）：j 阶之下各阶有所漏，'
    '恰在差经 j 次或更多回应传到处（`orderBelow_lt_iff`、`carriedWithin_eq_iff`）；按时间次序的耦合链（`CoupledIntoBy`）：j 阶从每个'
    '起始之差都精确，恰在没有 j + 1 个按时间次序的耦合的链终于那里处（`exact_every_start_iff`），有限阶从每个起始之差都精确，恰在这些'
    '链长度有界处（`finite_order_iff_bounded`、`finite_order_uniform_iff`）；复现的耦合（`CouplingRecurs`）：被送到的复现回路在上游'
    '使每一阶都不精确（`carriedWithin_lt_of_recurring_loop`、`unbounded_of_recurring_loop`），从第 N 步起没有耦合读水平处 N 阶精确'
    '（`exact_of_reading_before`），比条件数多一个耦合的链经过回路，不需列出全部条件（`loop_of_coupledInto_succ`、'
    '`no_chain_of_no_loop`），耦合每步成立时链有界恰在上游没有回路处（`bounded_iff_no_loop`）；第 N 步起的强度（`strengthsFrom`），'
    '时程自第 N 步安定（`SettledFrom`）：链有界与有限阶精确，恰在第 N 步起的耦合没有回路在上游处（`bounded_iff_no_loop_from`、'
    '`finite_order_iff_no_loop_from`），没有这样的回路时所携带的量至多是多项式（`carried_le_polynomial_from`），耦合每步成立时自'
    '第一步安定（`settledFrom_zero_of_always`）；`Loops.Once` 只读第一步（`Loops.Once.reads_first`、`Loops.Once.no_chain_of_two`、'
    '`Loops.Once.settled`）；`Becoming.Loops` 的精确性结果作为实例（`Remainder.carriedWithin_exact`、'
    '`Remainder.carriedWithin_exact_of_no_loop`、`Remainder.finite_order_iff_no_loop`、`Remainder.Once.exact`）；对一切具有这些'
    '强度的律：`gap_within_order_iff`；读法是 AI 的，待 Ren / '
    'what a cut loses, for every schedule of couplings (no premise beyond the strengths each theorem names): what one '
    'response carries from given levels (`responded`) and what j responses carry in turn (`responses`); the carried '
    'amount is the orders below j plus what j responses in turn carry from it (`carried_eq_orderBelow_add`), so a cut at '
    'order j loses exactly what j + 1 responses carry (`carried_eq_carriedWithin_add`), the loss falling as the order '
    'rises (`responses_antitone`), at most the bound of `Becoming.Loops` (`responses_le_missBound`) and exactly that for '
    'the self-loop (`Loops.SelfLoop.responses_eq`); couplings at a step (`CouplesAt`) and gaps conveyed through j '
    'responses or more (`ConveyedThrough`): the orders below j miss something exactly where a gap is conveyed there '
    'through j responses or more (`orderBelow_lt_iff`, `carriedWithin_eq_iff`); chains of couplings in time order '
    '(`CoupledIntoBy`): order j is exact from every start exactly where no chain of j + 1 couplings in time order ends '
    'there (`exact_every_start_iff`), and a finite order is exact from every start exactly where those chains are '
    'bounded (`finite_order_iff_bounded`, `finite_order_uniform_iff`); recurring couplings (`CouplingRecurs`): a fed '
    'loop of them upstream leaves every order inexact (`carriedWithin_lt_of_recurring_loop`, '
    '`unbounded_of_recurring_loop`), where no coupling reads a level from step N on order N is exact '
    '(`exact_of_reading_before`), a chain one longer than the list passes a loop, with no listing of every condition '
    '(`loop_of_coupledInto_succ`, `no_chain_of_no_loop`), and with couplings at every step the chains are bounded '
    'exactly where no loop lies upstream (`bounded_iff_no_loop`); the strengths from step N on (`strengthsFrom`) and a '
    'schedule settled by step N (`SettledFrom`): the chains are bounded and a finite order exact exactly where no loop '
    'of the couplings from step N on lies upstream (`bounded_iff_no_loop_from`, `finite_order_iff_no_loop_from`), and '
    'without such a loop the carried amount is at most a polynomial (`carried_le_polynomial_from`), couplings at every '
    'step having settled from the first (`settledFrom_zero_of_always`); `Loops.Once` reads the first step only '
    '(`Loops.Once.reads_first`, `Loops.Once.no_chain_of_two`, `Loops.Once.settled`); the results of `Becoming.Loops` '
    'on exactness as instances (`Remainder.carriedWithin_exact`, `Remainder.carriedWithin_exact_of_no_loop`, '
    '`Remainder.finite_order_iff_no_loop`, `Remainder.Once.exact`); for every law with the strengths: '
    '`gap_within_order_iff`; the readings are the AI\'s, pending Ren |')

chapter_row = (
    f'| L4 | [Becoming.Remainder]({LEAN}) | 截断所失：任意耦合时程（除了各定理所写的强度不加前提）：所携带的量是 j 阶加上 j + 1 次'
    '回应从它所携带的，截断恰好失去这些；j 阶有所漏恰在差经 j + 1 次按时间次序的回应传到处；有限阶从每个起始之差都精确，恰在按时间次序的'
    '耦合链有界处；时程安定时，恰在其后的耦合没有回路在上游处，不需列出全部条件，能到达的最大差别快于每个多项式只经由这样的回路。/ What '
    'a cut loses, for every schedule of couplings, with no premise beyond the strengths each theorem names: the carried '
    'amount is order j plus what j + 1 responses carry from it, which is exactly what a cut loses; order j misses '
    'something exactly where a gap is conveyed through j + 1 responses in time order; a finite order is exact from '
    'every start exactly where the chains of couplings in time order are bounded; where the schedule has settled, '
    'exactly where no loop of the couplings that go on lies upstream, with no listing of every condition, and the most '
    'difference that can arrive grows faster than every polynomial only through such a loop. | 58 |')

paragraph_zh = (
    '**截断所失：任意耦合时程（第一部分）。** `Becoming.Loops` 的当且仅当要求每个耦合每步成立、全部条件列出，只在第一步耦合的回路'
    f'表明前者不能照原样去掉（[Becoming.Remainder]({LEAN})）。这里对任意耦合时程、任意条件之列，陈述截断恰好失去什么、在哪里失去。'
    '一次回应从给定水平所携带的（`responded`）是携带之律去掉起始之差与部分之差；j 次回应依次所携带的（`responses`）每次对上一次所携带的'
    '再作一次回应。所携带的量是 j 阶之下各阶加上 j 次回应依次从所携带的量自身所携带的（`carried_eq_orderBelow_add`），所以在 j 阶截断'
    '恰好失去 j + 1 次回应从所携带的量所携带的（`carried_eq_carriedWithin_add`）；证明只用加法，因为给出对所读的水平可加'
    '（`carriedGive_add`、`carriedFrom_add`）。所失随阶下降（`responses_antitone`），在任意时程下至多是 `Becoming.Loops` 的界'
    '（`responses_le_missBound`），自环恰好失去这个界（`Loops.SelfLoop.responses_eq`）。一次回应到第 t 步有所携带到 c，恰在 t 之前某步'
    '一个条件的水平耦合到 c（`CouplesAt`）且为正（`responded_pos_iff`）；差经 j 次或更多回应传到 c（`ConveyedThrough`），是说 '
    '`Becoming.Propagation` 的时间路线（`Conveyed`）到达一个条件，再经 j 个耦合传到 c，每个耦合所读的水平在前一个到达之后。j 阶之下'
    '各阶在第 t 步 c 处有所漏，恰在差经 j 次或更多回应传到那里（`orderBelow_lt_iff`）；j 阶精确，恰在没有差经 j + 1 次传到那里'
    '（`carriedWithin_eq_iff`）。j 个耦合的按时间次序的链终于 c（`CoupledIntoBy`），是说每个耦合所读的水平在前一个到达之后：j 阶从每个'
    '起始之差都精确，恰在没有 j + 1 个耦合的这种链终于那里（`exact_every_start_iff`）；有限阶在 c 处每步从每个起始之差都精确，恰在终于 '
    'c 的按时间次序的链长度有界（`finite_order_iff_bounded`），这时一个阶对一切起始之差都精确（`finite_order_uniform_iff`）。这些不加'
    '前提。耦合复现（`CouplingRecurs`），是说它所读水平所在的步要多晚有多晚：差到达复现耦合的回路、又有复现耦合从它通到 c 时，每一阶'
    '都在 c 处漏掉一些（`carriedWithin_lt_of_recurring_loop`）；没有耦合从第 N 步起读水平时，N 阶处处精确（`exact_of_reading_before`）。'
    '每个耦合读一个列出的条件，所以比条件数多一个耦合的链经过回路，不需列出全部条件（`loop_of_coupledInto_succ`）。第 N 步起的强度'
    '（`strengthsFrom`）去掉第 N 步之前水平上的读取；耦合复现，恰是它从每步起都是耦合（`couplingRecurs_iff`）；N + j 个耦合的按时间'
    '次序的链，后 j 个是第 N 步起的耦合的链（`CoupledIntoBy.tail`）。时程自第 N 步安定（`SettledFrom`），是说第 N 步起的每个耦合都'
    '复现：这时有限阶在 c 处从每个起始之差都精确，恰在第 N 步起的耦合没有回路在 c 的上游（`finite_order_iff_no_loop_from`），不需列出'
    '全部条件；不论时程，第 N 步起的耦合没有回路在上游时，所携带的量至多是步数的多项式（`carried_le_polynomial_from`）。耦合每步成立时'
    '自第一步安定（`settledFrom_zero_of_always`），所以 `finite_order_iff_no_loop` 不需列出全部条件也成立'
    '（`Remainder.finite_order_iff_no_loop`）；`Loops.Once` 只读第一步，没有两个耦合的按时间次序的链，其时程自第二步安定且其后没有'
    '耦合（`Loops.Once.no_chain_of_two`、`Loops.Once.settled`）。由 `most_difference_arrives`，对一切具有这些强度的律：每个差从每个'
    '起始之差都至多是 j 阶所携带的，恰在没有 j + 1 个耦合的按时间次序的链终于那里（`gap_within_order_iff`）。读法（AI 的，待 Ren）：'
    f'Ren 2026-10-12 问“{QUOTE}”（[来源]({SOURCE})），2026-10-16 把 `Becoming.Loops` 的各阶取为与历史之和同一结构的一种；精确余项'
    '说截断这一展开失去什么，形如 Neumann 级数的余项：j 阶之下各阶是少于 j 次回应的项，截断所失是 j 次回应从整体所携带的；如按时间次序'
    '的微扰展开（Dyson 级数），一条路线上的回应按时间次序；截断恰在有更多回应的时间路线到达处失去；损失属于截断，不属于理论，所携带的量'
    '本身是精确的。决定截断之损失的是耦合的时间次序，不是不计时间画出的回路：有意义的回路是持续的耦合的回路，耦合停止的回路只是经过。'
    '能到达的最大差别快于每个多项式只经由持续耦合的回路；是否经由每个这样的回路这里不推出。每个时程是否终将安定不推出（不复现的耦合会'
    '停止，但耦合是否复现这里不判定，核心不假设排中律）；比强度之积更细的失控速度、在一步读无穷多条件之律、连续时间与实数的量也不推出。'
    f'见 [what-a-cut-loses]({RECORD})。')

paragraph_en = (
    '**What a cut loses, for every schedule of couplings (Part I).** The equivalence of `Becoming.Loops` needs every '
    'coupling to hold at every step and every condition listed, and a loop coupled at the first step only shows that '
    f'the first cannot be dropped as it stands ([Becoming.Remainder]({LEAN})). Here what a cut loses, and where, is '
    'stated for every schedule of couplings and any list of conditions. What one response carries from given levels '
    '(`responded`) is the carrying law with no starting gap and no gap of the part; j responses in turn (`responses`) '
    'respond each to what the one before carried. The carried amount is the orders below j plus what j responses in '
    'turn carry from the carried amount itself (`carried_eq_orderBelow_add`), so a cut at order j loses exactly what '
    'j + 1 responses carry from it (`carried_eq_carriedWithin_add`); the proof only adds, as giving is additive in the '
    'levels read (`carriedGive_add`, `carriedFrom_add`). The loss falls as the order rises (`responses_antitone`), is '
    'at most the bound of `Becoming.Loops` for every schedule (`responses_le_missBound`), and is exactly that bound for '
    'the self-loop (`Loops.SelfLoop.responses_eq`). One response carries something to c by step t exactly where, at a '
    'step before t, the level of a condition is coupled into c (`CouplesAt`) and positive (`responded_pos_iff`); a gap '
    'is conveyed to c through j responses or more (`ConveyedThrough`) where the route in time of `Becoming.Propagation` '
    '(`Conveyed`) reaches a condition and j couplings carry it on to c, each reading a level the one before had reached. '
    'The orders below j miss something at c at step t exactly where a gap is conveyed there through j responses or more '
    '(`orderBelow_lt_iff`), and order j is exact there exactly where none is conveyed through j + 1 '
    '(`carriedWithin_eq_iff`). A chain of j couplings in time order ends at c (`CoupledIntoBy`) where each coupling '
    'reads a level the one before had reached: order j is exact from every start exactly where no such chain of j + 1 '
    'couplings ends there (`exact_every_start_iff`), and a finite order is exact at c at every step from every start '
    'exactly where the chains in time order into c are bounded in length (`finite_order_iff_bounded`), one order then '
    'serving every start (`finite_order_uniform_iff`). These need no premise. A coupling recurs (`CouplingRecurs`) '
    'where it reads levels at steps as late as one likes: where a gap reaches a loop of recurring couplings and '
    'recurring couplings lead from it to c, every order misses something at c (`carriedWithin_lt_of_recurring_loop`); '
    'where no coupling reads a level from step N on, order N is exact everywhere (`exact_of_reading_before`). Each '
    'coupling reads a listed condition, so a chain one longer than the list passes a loop, with no listing of every '
    'condition (`loop_of_coupledInto_succ`). The strengths from step N on (`strengthsFrom`) drop every reading of a '
    'level before N; a coupling recurs exactly where it is a coupling from every step on (`couplingRecurs_iff`); of a '
    'chain in time order of N + j couplings, the last j are a chain of the couplings from step N on '
    '(`CoupledIntoBy.tail`). A schedule has settled by step N (`SettledFrom`) where every coupling from N on recurs: '
    'then a finite order is exact at c from every start exactly where no loop of the couplings from step N on lies '
    'upstream of c (`finite_order_iff_no_loop_from`), with no listing of every condition; whatever the schedule, where '
    'no such loop lies upstream the carried amount is at most a polynomial in the steps '
    '(`carried_le_polynomial_from`). Couplings at every step have settled from the first step '
    '(`settledFrom_zero_of_always`), so `finite_order_iff_no_loop` holds with no listing of every condition '
    '(`Remainder.finite_order_iff_no_loop`); `Loops.Once` reads the first step only, has no chain of two couplings in '
    'time order, and its schedule has settled from the second step with nothing coupling (`Loops.Once.no_chain_of_two`, '
    '`Loops.Once.settled`). By `most_difference_arrives`, for every law with the strengths, every gap from every start '
    'is at most what order j carries exactly where no chain of j + 1 couplings in time order ends there '
    f'(`gap_within_order_iff`). On the AI\'s reading, pending Ren: Ren asked on 12 October “{QUOTE}” ([source]({SOURCE})), '
    'and on 16 October took the orders of `Becoming.Loops` as the same structural kind as the sum over histories; the '
    'exact remainder says what a cut of that expansion loses, in the form of a Neumann series\'s remainder: the orders '
    'below j are the terms of fewer than j responses, and a cut loses what j responses carry from the whole; as in '
    'time-ordered perturbation theory (the Dyson series), the responses of a route come in time order, and a cut loses '
    'exactly where a route in time with more responses arrives; the loss is the cut\'s, not the theory\'s, the carried '
    'amount itself being exact. What decides a cut\'s loss is the time order of the couplings, not loops drawn without '
    'time: the loops that matter are those of the couplings that go on, and a loop whose couplings stop is passing. The '
    'most difference that can arrive grows faster than every polynomial only through a loop of the couplings that go '
    'on; whether through every such loop is not derived here. That every schedule settles at some step is not derived '
    '(a coupling that does not recur stops, but whether one recurs is not decided here, and the core assumes no '
    'excluded middle); nor are how fast a runaway is beyond the product of the strengths, laws reading infinitely many '
    f'conditions at a step, continuous time and real amounts. See [what-a-cut-loses]({RECORD}).')

whole_zh = (
    '- **截断所失。** 对任意耦合时程，所携带的量是 j 阶加上 j + 1 次回应从它所携带的（`carried_eq_carriedWithin_add`）；j 阶从每个'
    '起始之差都精确，恰在没有 j + 1 个耦合的按时间次序的链终于那里（`exact_every_start_iff`），有限阶精确恰在这些链长度有界处'
    '（`finite_order_iff_bounded`）；时程安定时，恰在其后的耦合没有回路在上游处（`finite_order_iff_no_loop_from`），不需列出全部条件；'
    '没有这样的回路时增长至多是多项式（`carried_le_polynomial_from`）。')
whole_en = (
    '- **What a cut loses.** For every schedule of couplings, the carried amount is order j plus what j + 1 responses '
    'carry from it (`carried_eq_carriedWithin_add`); order j is exact from every start exactly where no chain of j + 1 '
    'couplings in time order ends there (`exact_every_start_iff`), and a finite order is exact exactly where those '
    'chains are bounded (`finite_order_iff_bounded`); where the schedule has settled, exactly where no loop of the '
    'couplings from then on lies upstream (`finite_order_iff_no_loop_from`), with no listing of every condition; '
    'without such a loop the growth is at most polynomial (`carried_le_polynomial_from`).')

status_zh = (
    '；截断所失：对任意耦合时程，截断恰好失去更多次回应所携带的，有限阶精确恰在按时间次序的耦合链有界处，时程安定时恰在其后的耦合没有'
    f'回路在上游处（[what-a-cut-loses]({RECORD})）')
open_zh = '开放：律本身；反例之存在的确切强度；每个耦合时程是否终将安定；复现耦合的回路是否都使能到达的最大差别失控'

further_zh = (
    '；时有时无的耦合已给出（`Becoming.Remainder`：截断恰好失去更多次回应所携带的；有限阶精确恰在按时间次序的耦合链有界处；时程安定'
    '时恰在其后的耦合没有回路在上游处，不需列出全部条件；快于每个多项式只经由持续耦合的回路）；每个时程是否终将安定，复现耦合的回路是否'
    '都使之失控，比强度之积更细的失控速度。')
further_en = (
    '; couplings that come and go are given (`Becoming.Remainder`: a cut loses exactly what more responses carry; a '
    'finite order is exact exactly where the chains of couplings in time order are bounded; where the schedule has '
    'settled, exactly where no loop of the couplings that go on lies upstream, with no listing of every condition; '
    'growth faster than every polynomial only through such a loop); whether every schedule settles, whether every loop '
    'of recurring couplings makes a difference run away, and how fast a runaway is beyond the product of the strengths.')

glossary = [
    '| 截断所失 | what a cut loses | 在 j 阶截断时所携带的量中未被携带的：恰是 j + 1 次回应依次从所携带的量所携带的；随阶下降；为正恰在差经 '
    'j + 1 次按时间次序的回应传到处 | `responses`、`carried_eq_carriedWithin_add`、`responses_antitone`、`carriedWithin_lt_iff` |',
    '| 按时间次序的耦合链 | chain of couplings in time order | 每个耦合所读的水平在前一个耦合到达之后的链；有限阶从每个起始之差都精确，'
    '恰在终于所论条件的这种链长度有界处 | `CoupledIntoBy`、`exact_every_start_iff`、`finite_order_iff_bounded` |',
    '| 安定（耦合时程的） | settled (schedule of couplings) | 自某步起的每个耦合都复现；安定之后，有限阶精确恰在其后的耦合没有回路在上游'
    '处 | `SettledFrom`、`strengthsFrom`、`CouplingRecurs`、`finite_order_iff_no_loop_from` |',
]

docs = {'bullet': bullet, 'scope': scope, 'readme_row': readme_row, 'chapter_row': chapter_row,
        'paragraph_zh': paragraph_zh, 'paragraph_en': paragraph_en, 'whole_zh': whole_zh, 'whole_en': whole_en,
        'status_zh': status_zh, 'open_zh': open_zh, 'further_zh': further_zh, 'further_en': further_en,
        'glossary': glossary}
(Path(__file__).resolve().parent / 'docs.json').write_text(json.dumps(docs, ensure_ascii=False, indent=2) + '\n')
print('wrote docs.json', len(docs))
