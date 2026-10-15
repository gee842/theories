#!/usr/bin/env python3
"""P121 and P122: write docs.json, the texts apply_docs.py inserts.

usage: python3 -B make_docs_json.py

Root module bullets, checker scope entries, Lean README rows, the chapter's §2 paragraphs, its
"Part I stated whole" items, its §9 rows and glossary rows, for Becoming.Routes (P121) and
Becoming.Closing (P122). Theorem counts are read from the modules in this checkout.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
W = HERE.parents[5]
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'


def theorems(module):
    return sum(1 for l in (L / f'Becoming/{module}.lean').read_text().splitlines() if l.startswith('theorem '))


ROUTES, CLOSING = theorems('Routes'), theorems('Closing')

docs = {
    'bullet_routes': (
        '* `Becoming.Routes` (L4): the orders of a carried difference as a sum over histories, with no\n'
        '  premise beyond what each statement names. For every weighting whose steps split into a ground\n'
        '  and a response part, order `j` of the sum over histories is exact at every horizon up to `j`.\n'
        '  Traced back in time, a route steps by one response to an earlier level, the level holding\n'
        '  between, or ends at a source; with counting weights the transfer of horizon `j + 1` over the\n'
        '  route points is order `j` of the carried amount, so each order, and the carried amount, is a\n'
        '  sum over courses, a cut is a truncation, and a finite horizon is exact exactly where no loop\n'
        '  lies upstream (stationary strengths).'),
    'bullet_closing': (
        '* `Becoming.Closing` (L4): how loops form within the unfolding, with no premise beyond the\n'
        '  strengths each statement names. The loops formed by a step are the loops of the couplings\n'
        '  acting before it, and a world\'s loops are those formed by some step. The loops formed by\n'
        '  `T + 1` are those formed by `T` and those through a coupling acting at `T` that closes a\n'
        '  chain; an exchange coming to respond to the level it gives to forms a loop of one. Before a\n'
        '  loop forms upstream the carried amount is at most a polynomial, and the amounts before it do\n'
        '  not show whether it will. Strengths read off the course give a course that is the carried\n'
        '  amount of the strengths it reads; in the threshold witness a loop forms at the step a level\n'
        '  reaches the threshold and doubles from then on.'),
    'scope_routes': (
        '    "Routes: for every weighting with each step split into a ground and a response part, order "\n'
        '    "j of the sum over histories is exact at every horizon up to j, readings keeping the laws "\n'
        '    "can be taken order by order, and for counting the orders rise to the sum; with one "\n'
        '    "configuration, ground one and response M, order j at horizon n is the order sum of Loops "\n'
        '    "and the sum (1 + M)^n; with counting weights on routes back in time, each step one "\n'
        '    "response or an end at a source, the transfer of horizon j + 1 is order j of the carried "\n'
        '    "amount at every condition and step, so each order and the carried amount are sums over "\n'
        '    "courses, horizons rise to the carried amount and miss at most the bound on a cut, and with "\n'
        '    "stationary strengths a finite horizon is exact exactly where no loop lies upstream. "\n'),
    'scope_closing': (
        '    "Closing: the couplings formed by step T are those acting before T, every chain is formed "\n'
        '    "by some step, so the loops are those formed by some step; the loops formed by T + 1 are "\n'
        '    "those formed by T and those through a coupling acting at T that closes a chain, and an "\n'
        '    "exchange responding to the level it gives to forms a loop of one; the carried amount up to "\n'
        '    "T reads only the couplings before T, so with no loop formed by T upstream it is at most a "\n'
        '    "polynomial up to T; a self-loop forming at T and one forming later agree up to T, one "\n'
        '    "doubling after; strengths read from the levels so far generate a course that is the "\n'
        '    "carried amount of the strengths it reads, and in the threshold witness the loop forms at "\n'
        '    "the step the level reaches the threshold and the level plus one doubles from then on. "\n'),
    'readme_routes': (
        '| L4 | [`Becoming.Routes`](Becoming/Routes.lean) | 携带差别的阶作为历史之和（除了各定理所写者不加前提）：对每一种权重，'
        '每步的权重分成基础部分与回应部分，j 阶（`Weights.within`）在每个不超过 j 的视界上就是历史之和（`Weights.within_exact`），'
        '保持律的读法可逐阶取（`Weights.Hom.within`），计数时各阶上升到历史之和（`counting_within_le_succ`、`counting_within_le_transfer`）；'
        '一个构形、基础一、回应 M 时 j 阶是 `Loops.orderSum`（`Routes.SelfLoop.within_eq`）、和是 (1 + M)^n（`Routes.SelfLoop.transfer_eq`）；'
        '沿时间往回的路线（`RoutePoint`、`responseWeight`、`routeWeight`、`routeSum`）的视界 j + 1 就是所携带的量的 j 阶'
        '（`routeSum_eq_carriedWithin`），每一阶与所携带的量都是历程之和（`carriedWithin_eq_courses`、`carried_eq_courses`），'
        '截断就是视界（`routeSum_exact`、`routeSum_mono`、`carried_le_routeSum_add`），有限视界精确恰在上游没有回路处'
        '（`finite_horizon_iff_no_loop`）；读法是 AI 的，待 Ren / the orders of a carried difference as a sum over histories '
        '(no premise beyond what each theorem names): for every weighting, each step\'s weight split into a ground and a response '
        'part, order j (`Weights.within`) is the sum over histories at every horizon up to j (`Weights.within_exact`), readings '
        'keeping the laws can be taken order by order (`Weights.Hom.within`), and for counting the orders rise to the sum '
        '(`counting_within_le_succ`, `counting_within_le_transfer`); with one configuration, ground one and response M, order j '
        'is `Loops.orderSum` (`Routes.SelfLoop.within_eq`) and the sum (1 + M)^n (`Routes.SelfLoop.transfer_eq`); the horizon '
        'j + 1 of routes back in time (`RoutePoint`, `responseWeight`, `routeWeight`, `routeSum`) is order j of the carried amount '
        '(`routeSum_eq_carriedWithin`), each order and the carried amount are sums over courses (`carriedWithin_eq_courses`, '
        '`carried_eq_courses`), a cut is a truncation (`routeSum_exact`, `routeSum_mono`, `carried_le_routeSum_add`), and a '
        'finite horizon is exact exactly where no loop lies upstream (`finite_horizon_iff_no_loop`); the readings are the AI\'s, '
        'pending Ren |'),
    'readme_closing': (
        '| L4 | [`Becoming.Closing`](Becoming/Closing.lean) | 回路怎样在展开中形成（除了各定理所写的强度不加前提）：第 T 步之前的强度'
        '（`strengthsBefore`）保留在 T 之前作用的耦合（`couples_before_iff`），每条链都在某步形成（`coupled_formed`），回路恰是到某步'
        '形成的回路（`onLoop_iff_formed`、`upstream_iff_formed`）；到 T + 1 形成的回路是到 T 形成的与经过在第 T 步作用、闭合一条链的'
        '耦合的（`onLoop_succ_iff`、`forms_by_closing`），开始回应自身所给条件的水平形成一圈的回路（`responds_to_own_level`）；到 T '
        '所携带的量只读 T 之前的耦合（`carried_before`），到 T 形成的回路不在上游时至多是多项式（`carried_le_polynomial_before`）；'
        '在 T 形成与更晚形成的自环到 T 为止相同（`Closing.Onset`）；从水平读出的强度（`ReadsBefore`、`ExchangeLaw.carryingRead`）生成的'
        '进程是其所读强度的所携带的量（`formedCourse_eq_carried`），阈值的见证中回路在水平达到阈值之步形成（`Closing.Threshold`）；'
        '读法是 AI 的，待 Ren / how loops form within the unfolding (no premise beyond the strengths each theorem names): the '
        'strengths before step T (`strengthsBefore`) keep the couplings acting before T (`couples_before_iff`), every chain is '
        'formed by some step (`coupled_formed`), and the loops are those formed by some step (`onLoop_iff_formed`, '
        '`upstream_iff_formed`); the loops formed by T + 1 are those formed by T and those through a coupling acting at T that '
        'closes a chain (`onLoop_succ_iff`, `forms_by_closing`), and coming to respond to the level it gives to forms a loop of '
        'one (`responds_to_own_level`); the carried amount up to T reads only the couplings before T (`carried_before`), and with '
        'no loop formed by T upstream it is at most a polynomial (`carried_le_polynomial_before`); self-loops forming at T and '
        'later agree up to T (`Closing.Onset`); strengths read from the levels (`ReadsBefore`, `ExchangeLaw.carryingRead`) '
        'generate a course that is the carried amount of the strengths it reads (`formedCourse_eq_carried`), and in the '
        'threshold witness the loop forms at the step the level reaches the threshold (`Closing.Threshold`); the readings are '
        'the AI\'s, pending Ren |'),
    'paragraph_routes_zh': (
        f'**携带差别的阶作为历史之和（第一部分）。** Ren 取了读法：2026-10-12 所问的积分是 `Becoming.Weighted` 的历史之和及其损失，'
        f'`Becoming.Loops` 的阶是同一结构类的，两者尚未接合（[Becoming.Routes]({LINK}Routes.lean)）。对每一种权重，把每步的权重分成基础部分与回应部分，j 阶（`Weights.within`）'
        '跨每步由基础部分读 j 阶、由回应部分读 j − 1 阶，在每个不超过 j 的视界上就是整个历史之和（`Weights.within_exact`）；一个构形、'
        '基础一、回应 M 时，j 阶是 `Loops.orderSum M j n`，和是 (1 + M)^n（`Routes.SelfLoop.within_eq`、`Routes.SelfLoop.transfer_eq`）。'
        '把一个差别沿时间往回追，一步是一次回应，到较早的一个水平，权重是强度在回应能发生的各步上之和，其间水平保持（`responseWeight`）；'
        '或者终于源（`routeWeight`）。这些计数权重的转移在视界 j + 1 上就是所携带的量的 j 阶（`routeSum_eq_carriedWithin`），于是每一阶'
        '与所携带的量都是历程之和（`carriedWithin_eq_courses`、`carried_eq_courses`），截断就是视界（`routeSum_exact`、'
        '`carried_le_routeSum_add`），形成与强度每步相同时有限视界精确恰在上游没有回路处（`finite_horizon_iff_no_loop`）。'
        '读法（AI 的，待 Ren）：两个积分是一个，回应是图的顶点，顶点之间水平保持，如同传播子对中间时刻求和；`Becoming.Weighted` 的回路损失就是 `Becoming.Loops` 的失控；'
        '对应是结构的，计数的权重不相消。'),
    'paragraph_routes_en': (
        f'**The orders of a carried difference as a sum over histories (Part I).** Ren took the reading that the integration '
        f'asked about on 12 October is the sum over histories of `Becoming.Weighted` with its losses, that the orders of '
        f'`Becoming.Loops` are of the same structural kind, and that the two were not yet joined ([Becoming.Routes]({LINK}Routes.lean)). For every weighting, each step\'s '
        'weight split into a ground and a response part, order j (`Weights.within`) reads order j through the ground part and '
        'order j − 1 through the response part, and is the whole sum over histories at every horizon up to j '
        '(`Weights.within_exact`); with one configuration, ground one and response M, order j is `Loops.orderSum M j n` and the '
        'sum (1 + M)^n (`Routes.SelfLoop.within_eq`, `Routes.SelfLoop.transfer_eq`). Traced back in time, a difference steps by '
        'one response to an earlier level, weighted by the strengths summed over the steps at which it can occur with the level '
        'holding between (`responseWeight`), or ends at a source (`routeWeight`). The transfer of these counting weights at '
        'horizon j + 1 is order j of the carried amount (`routeSum_eq_carriedWithin`), so each order and the carried amount are '
        'sums over courses (`carriedWithin_eq_courses`, `carried_eq_courses`), a cut is a truncation (`routeSum_exact`, '
        '`carried_le_routeSum_add`), and with the same formations and strengths at every step a finite horizon is exact exactly '
        'where no loop lies upstream (`finite_horizon_iff_no_loop`). Readings (the AI\'s, pending Ren): the two integrations '
        'are one, the responses being the vertices of a diagram and the level holding between them as a propagator sums over '
        'intermediate times; the loss by loops of `Becoming.Weighted` is the runaway of `Becoming.Loops`; the match is structural, and counting weights do not '
        'cancel.'),
    'paragraph_closing_zh': (
        f'**回路怎样在展开中形成（第一部分）。** Ren 取了“回路在展开中形成与消解”的读法，待回路形成的定理（[Becoming.Closing]({LINK}Closing.lean)）。'
        '第 T 步之前的强度（`strengthsBefore`）保留在 T 之前作用的耦合（`couples_before_iff`），所以到 T 形成的回路用 `Becoming.Loops` 的'
        '定义陈述；每条链都在某步形成，一个世界的回路恰是到某步形成的回路（`onLoop_iff_formed`）。回路由闭合而形成：到 T + 1 形成的回路，'
        '是到 T 形成的回路与经过一个在第 T 步作用、闭合一条链的耦合的回路（`onLoop_succ_iff`、`forms_by_closing`）；一个交换开始回应它'
        '所给的条件的水平，形成一圈的回路（`responds_to_own_level`）。到 T 所携带的量只读 T 之前的耦合（`carried_before`），所以到 T 形成'
        '的回路都不在上游时，到 T 为止至多是多项式（`carried_le_polynomial_before`）；形成之前的量不显示它是否将形成（`Closing.Onset`）。'
        '强度从至每步的水平读出时（`ReadsBefore`），生成的进程是其所读强度的所携带的量（`formedCourse_eq_carried`）：回路的形成从展开'
        '读出；阈值的见证中回路在水平达到阈值之步形成，此后加倍（`Closing.Threshold`）。消解见 `Becoming.Remainder`（停止的耦合）。'
        '读法（AI 的，待 Ren）：回路在某个交换开始回应它所给条件下游的水平之步闭合而形成；形成不从之前的量预见，这与 `Becoming.Runaway` '
        '相遇。'),
    'paragraph_closing_en': (
        f'**How loops form within the unfolding (Part I).** Ren took the reading that loops form and dissolve within the '
        f'unfolding, pending a loop-formation theorem ([Becoming.Closing]({LINK}Closing.lean)). The strengths before step T '
        '(`strengthsBefore`) keep the couplings acting before T (`couples_before_iff`), so the loops formed by T are stated '
        'with the definitions of `Becoming.Loops`; every chain is formed by some step, and a world\'s loops are exactly those '
        'formed by some step (`onLoop_iff_formed`). A loop forms by closing: the loops formed by T + 1 are those formed by T '
        'and those through a coupling acting at step T that closes a chain (`onLoop_succ_iff`, `forms_by_closing`); an '
        'exchange coming to respond to the level of the condition it gives to forms a loop of one (`responds_to_own_level`). '
        'The carried amount up to T reads only the couplings before T (`carried_before`), so with no loop formed by T upstream '
        'it is at most a polynomial up to T (`carried_le_polynomial_before`); the amounts before a loop forms do not show '
        'whether it will (`Closing.Onset`). Where strengths are read from the levels up to each step (`ReadsBefore`), the '
        'course generated is the carried amount of the strengths it reads (`formedCourse_eq_carried`): formation is read off '
        'the unfolding; in the threshold witness the loop forms at the step a level reaches the threshold and doubles from then '
        'on (`Closing.Threshold`). How loops dissolve is in `Becoming.Remainder` (couplings that stop). Readings (the AI\'s, '
        'pending Ren): a loop forms by closing, at the step an exchange comes to respond to a level downstream of what it '
        'gives to; its formation is not foreseen from the amounts before it, which meets `Becoming.Runaway`.'),
    'whole_routes_zh': (
        '- **携带差别的阶作为历史之和。** 每个历史之和按阶展开，j 阶到视界 j 精确（`Weights.within_exact`）；沿时间往回的路线之和在视界 '
        'j + 1 上就是所携带的量的 j 阶（`routeSum_eq_carriedWithin`），所携带的量是历程之和（`carried_eq_courses`）；有限视界精确恰在'
        '上游没有回路处（`finite_horizon_iff_no_loop`）。'),
    'whole_routes_en': (
        '- **The orders of a carried difference as a sum over histories.** Every sum over histories expands by order, order j '
        'exact up to horizon j (`Weights.within_exact`); the sum over routes back in time at horizon j + 1 is order j of the '
        'carried amount (`routeSum_eq_carriedWithin`), which is a sum over courses (`carried_eq_courses`); a finite horizon is '
        'exact exactly where no loop lies upstream (`finite_horizon_iff_no_loop`).'),
    'whole_closing_zh': (
        '- **回路怎样形成。** 到 T + 1 形成的回路是到 T 形成的与经过在第 T 步作用、闭合一条链的耦合的（`onLoop_succ_iff`）；形成之前增长'
        '至多是多项式（`carried_le_polynomial_before`），且不显示它是否将形成（`Closing.Onset.unforeseen`）；强度从进程读出时进程是其所读'
        '强度的所携带的量（`formedCourse_eq_carried`）。'),
    'whole_closing_en': (
        '- **How loops form.** The loops formed by T + 1 are those formed by T and those through a coupling acting at T that '
        'closes a chain (`onLoop_succ_iff`); before a loop forms growth is at most polynomial (`carried_le_polynomial_before`) '
        'and does not show whether it will (`Closing.Onset.unforeseen`); with strengths read off the course, the course is the '
        'carried amount of the strengths it reads (`formedCourse_eq_carried`).'),
    'chapter_row_routes': (
        f'| L4 | [Becoming.Routes]({LINK}Routes.lean) | 携带差别的阶作为历史之和（除了各定理所写者不加前提）：每个历史之和按阶展开，j 阶到视界 '
        'j 精确；一个构形时 j 阶是所携带的量的阶之和；沿时间往回的路线之和在视界 j + 1 上就是所携带的量的 j 阶，每一阶与所携带的量都是历程'
        '之和，截断就是视界；形成与强度每步相同时有限视界精确恰在上游没有回路处。/ The orders of a carried difference as a sum over '
        'histories, with no premise beyond what each theorem names: every sum over histories expands by order, order j exact '
        'up to horizon j; with one configuration order j is the order sum of the carried amount; the sum over routes back in '
        'time at horizon j + 1 is order j of the carried amount, each order and the carried amount being sums over courses and '
        f'a cut a truncation; with the same formations and strengths at every step a finite horizon is exact exactly where no '
        f'loop lies upstream. | {ROUTES} |'),
    'chapter_row_closing': (
        f'| L4 | [Becoming.Closing]({LINK}Closing.lean) | 回路怎样在展开中形成（除了各定理所写的强度不加前提）：一个世界的回路恰是到某步形成'
        '的回路；到 T + 1 形成的回路是到 T 形成的与经过在第 T 步作用、闭合一条链的耦合的；开始回应自身所给条件的水平形成一圈的回路；形成之前'
        '增长至多是多项式，且不显示它是否将形成；强度从进程读出时进程是其所读强度的所携带的量，回路的形成从展开读出。/ How loops form '
        'within the unfolding, with no premise beyond the strengths each theorem names: a world\'s loops are exactly those '
        'formed by some step; the loops formed by T + 1 are those formed by T and those through a coupling acting at T that '
        'closes a chain; coming to respond to the level of the condition it gives to forms a loop of one; before a loop forms '
        'growth is at most polynomial and does not show whether it will; with strengths read off the course, the course is '
        f'the carried amount of the strengths it reads, and formation is read off the unfolding. | {CLOSING} |'),
    'glossary_route': (
        '| 沿时间往回的路线 | route back in time | 从某步某条件的水平往回，每步一次回应到较早的水平，其间水平保持，或终于源；其计数权重的转移在视界 '
        'j + 1 上就是所携带的量的 j 阶，所携带的量是这些路线之和 | `RoutePoint`、`routeWeight`、`routeSum`、`routeSum_eq_carriedWithin`、'
        '`carried_eq_courses` |'),
    'glossary_closing': (
        '| 闭合（回路的形成） | closing (the formation of a loop) | 到某步形成的回路是该步之前作用的耦合的回路；回路在一步形成，恰经过在那一步作用、'
        '闭合一条链的耦合：它给一个条件，而该条件已有链通到它所读的水平 | `strengthsBefore`、`onLoop_iff_formed`、`onLoop_succ_iff`、'
        '`forms_by_closing`、`responds_to_own_level` |'),
}

(HERE / 'docs.json').write_text(json.dumps(docs, ensure_ascii=False, indent=2) + '\n')
print('docs.json written:', ROUTES, CLOSING, 'theorems')
