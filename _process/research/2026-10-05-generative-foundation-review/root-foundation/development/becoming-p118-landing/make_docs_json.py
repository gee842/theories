#!/usr/bin/env python3
"""P118: write docs.json, the texts apply_docs.py inserts (kept here so the JSON stays valid)."""
import json
from pathlib import Path

LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Loops.lean'
RECORD = '../results/records/how-a-carried-difference-grows.md'
SOURCE = '../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'

bullet = """* `Becoming.Loops` (L4): how a carried difference grows, with no premise beyond the strengths each
  statement names. The carried amount expands by order: order `j`, what routes of at most `j`
  responses carry, rises to the carried amount and is exact up to step `j`. Where no loop of
  couplings lies upstream of a condition, a finite order is exact there at every step and the
  carried amount is at most a polynomial in the steps; a cut at order `j` misses at most a bound
  that a self-loop attains. Around a loop what reaches it returns multiplied, every time around, by
  at least one plus the product of its strengths. With the same formations and strengths at every
  step, a finite order is exact, and the most difference that can arrive is bounded by a
  polynomial, exactly where no loop lies upstream."""

scope = (
    '    "Loops: the amount carried by routes of at most j responses rises with j to the carried "\n'
    '    "amount and is exact up to step j; where no chain of j + 1 couplings ends at a condition, "\n'
    '    "order j is exact there, and with every condition listed a chain as long as the list passes "\n'
    '    "a loop, so where no loop lies upstream the order one less than the number of conditions is "\n'
    '    "exact at every step; where the couplings hold at every step a fed loop upstream leaves every "\n'
    '    "order inexact, so a finite order is exact from every start exactly where no loop lies "\n'
    '    "upstream; around a loop what has reached it returns multiplied, every time around, by at "\n'
    '    "least one plus the product of its strengths; with starting gaps at most D and the strengths "\n'
    '    "into each condition at most M a step, order j carries at most D times the sum over i <= j "\n'
    '    "of C(t, i) * M^i, the carried amount at most D * (1 + M)^t, and a cut at order j misses at "\n'
    '    "most their difference, all three attained by a self-loop; a doubling outgrows every "\n'
    '    "polynomial, so with the same formations and strengths at every step the carried amount, "\n'
    '    "and the most difference that can arrive for every law with those strengths, is bounded by "\n'
    '    "a polynomial exactly where no loop lies upstream. "\n')

readme_row = (
    '| L4 | [`Becoming.Loops`](Becoming/Loops.lean) | 所携带的差别怎样增长（除了各定理所写的强度不加前提）：所携带的量按阶展开'
    '（`carriedWithin`，至多 j 次回应的路线所携带的；每一阶是强度对下一阶所作的，`carriedFrom`），各阶随 j 上升到所携带的量'
    '（`carriedWithin_mono`、`carriedWithin_le_carried`），j 阶到第 j 步为止精确（`carriedWithin_exact`）；耦合（`Couples`）、'
    '耦合的链（`Coupled`）、回路（`OnLoop`）与上游（`Upstream`）；没有 j + 1 个耦合的链终于一个条件处，j 阶在那里精确'
    '（`carriedWithin_exact_of_not_coupledInto`），条件全部列出时与列表一样长的链经过回路（`loop_of_coupledInto`），所以上游没有回路处'
    '比条件数少一的阶每步精确（`carriedWithin_exact_of_no_loop`）；耦合每步成立时，上游被送到的回路使每一阶都不精确'
    '（`carriedWithin_lt_of_loop`），有限阶精确恰在上游没有回路处（`finite_order_iff_no_loop`），只在第一步耦合的回路让 1 阶精确'
    '（`Loops.Once.not_always`）；沿链乘以强度之积'
    '（`carried_along`），绕回路每圈至少乘以一加其强度之积（`carried_around`、`carried_runaway`）；起始之差至多 D、进入每个条件的强度'
    '（`inflow`）每步至多 M 时，j 阶至多是 D 乘对 i ≤ j 的 C(t, i)·M^i 之和（`carriedWithin_le_withinBound`、`Loops.withinBound_eq`），'
    '所携带的量至多 D(1 + M)^t（`carried_le_geomBound`），在 j 阶截断所漏至多两者之差（`carried_le_carriedWithin_add`），自环三者都'
    '恰好达到（`Loops.SelfLoop.attained`）；上游没有回路处所携带的量至多是多项式（`carried_le_polynomial`）；形成与强度每步相同'
    '（`stationary`）时，回路每圈至少使到达者加倍（`carried_doubles_around`、`carried_doubles_into`），加倍超过每个多项式'
    '（`Loops.not_poly_of_doubling`），所以有多项式界恰在上游没有回路处（`polynomial_iff_no_loop`）；对一切具有这些强度的律：'
    '`most_difference_within`、`gap_le_polynomial`、`gap_polynomial_iff_no_loop`；读法是 AI 的，待 Ren / '
    'how a carried difference grows (no premise beyond the strengths each theorem names): the carried amount expands by '
    'order (`carriedWithin`, what routes of at most j responses carry; each order is what the strengths make of the order '
    'below, `carriedFrom`), the orders rising with j to the carried amount (`carriedWithin_mono`, '
    '`carriedWithin_le_carried`) and order j exact up to step j (`carriedWithin_exact`); couplings (`Couples`), chains '
    '(`Coupled`), loops (`OnLoop`) and upstream (`Upstream`); where no chain of j + 1 couplings ends at a condition, order '
    'j is exact there (`carriedWithin_exact_of_not_coupledInto`), and with every condition listed a chain as long as the '
    'list passes a loop (`loop_of_coupledInto`), so where no loop lies upstream the order one less than the number of '
    'conditions is exact at every step (`carriedWithin_exact_of_no_loop`); where the couplings hold at every step, a fed '
    'loop upstream leaves every order inexact (`carriedWithin_lt_of_loop`), and a finite order is exact exactly where no '
    'loop lies upstream (`finite_order_iff_no_loop`), while a loop coupled at the first step only leaves order one exact '
    '(`Loops.Once.not_always`); along a chain the product of the strengths (`carried_along`), and '
    'around a loop, every time around, at least one plus the product of its strengths (`carried_around`, '
    '`carried_runaway`); with starting gaps at most D and the strengths into each condition (`inflow`) at most M a step, '
    'order j carries at most D times the sum over i ≤ j of C(t, i)·M^i (`carriedWithin_le_withinBound`, '
    '`Loops.withinBound_eq`), the carried amount at most D(1 + M)^t (`carried_le_geomBound`), a cut at order j misses at '
    'most their difference (`carried_le_carriedWithin_add`), and a self-loop attains all three '
    '(`Loops.SelfLoop.attained`); where no loop lies upstream the carried amount is at most a polynomial '
    '(`carried_le_polynomial`); with the same formations and strengths at every step (`stationary`), every loop at least '
    'doubles what reaches it every time around (`carried_doubles_around`, `carried_doubles_into`), a doubling outgrows '
    'every polynomial (`Loops.not_poly_of_doubling`), so a polynomial bound holds exactly where no loop lies upstream '
    '(`polynomial_iff_no_loop`); for every law with the strengths: `most_difference_within`, `gap_le_polynomial`, '
    '`gap_polynomial_iff_no_loop`; the readings are the AI\'s, pending Ren |')

chapter_row = (
    f'| L4 | [Becoming.Loops]({LEAN}) | 所携带的差别怎样增长（除了各定理所写的强度不加前提）：所携带的量按阶展开，j 阶是至多 j 次回应的'
    '路线所携带的，随 j 上升到所携带的量，到第 j 步为止精确；上游没有回路处有限阶每步精确，所携带的量至多是步数的多项式；在 j 阶截断所漏'
    '有界，自环恰好达到这个界；回路每绕一圈至少乘以一加其强度之积；形成与强度每步相同时，有限阶精确与能到达的最大差别有多项式界，都恰在'
    '上游没有回路处。/ How a carried difference grows, with no premise beyond the strengths each theorem names: the carried '
    'amount expands by order, order j being what routes of at most j responses carry, rising with j to the carried amount '
    'and exact up to step j; where no loop lies upstream a finite order is exact at every step and the carried amount is '
    'at most a polynomial in the steps; a cut at order j misses at most a bound a self-loop attains; a loop multiplies what '
    'reaches it, every time around, by at least one plus the product of its strengths; with the same formations and '
    'strengths at every step, a finite order is exact and the most difference that can arrive is bounded by a polynomial, '
    'both exactly where no loop lies upstream. | 113 |')

paragraph_zh = (
    '**所携带的差别怎样增长（第一部分）。** `Becoming.Propagation` 给出能到达的最大差别，回路却只有见证'
    f'（[Becoming.Loops]({LEAN})）。所携带的量按阶展开：j 阶（`carriedWithin`）是至多 j 次回应的路线所携带的，每一阶是强度对下一阶'
    '所作的（`carriedFrom`）；各阶随 j 上升到所携带的量（`carriedWithin_mono`、`carriedWithin_le_carried`），j 阶到第 j 步为止精确'
    '（`carriedWithin_exact`），因为每一步至多多一次回应。一个条件的水平耦合到另一个（`Couples`），是说某步一个在场、在部分之外的形成'
    '以正强度在该水平上与后者交换；耦合的链（`Coupled`）从一个条件通到另一个，回路（`OnLoop`）回到出发的条件，e 在 c 的上游'
    '（`Upstream`）是说有链从 e 通到 c。没有 j + 1 个耦合的链终于 c 处，j 阶在 c 处每步精确（`carriedWithin_exact_of_not_coupledInto`）；'
    '条件全部列出时，与列表一样长的链两次经过同一个条件（`loop_of_coupledInto`，鸽笼），所以 c 的上游没有回路处，比条件数少一的阶在 c '
    '处每步精确（`carriedWithin_exact_of_no_loop`）。耦合每步都成立时（`CouplesAlways`），到达上游回路的沿更长的路线不断到达 c，每一阶'
    '都漏掉一些（`carriedWithin_lt_of_loop`）：有限阶从每个起始之差都精确，恰在上游没有回路处（`finite_order_iff_no_loop`）；耦合须每步'
    '成立，只在第一步耦合的回路让 1 阶精确（`Loops.Once.not_always`）。沿强度'
    '至少为 w 的链，到达起点者乘以强度之积到达终点（`carried_along`）；绕回路一圈，到达回路者至少乘以一加回路上强度之积回到它'
    '（`carried_around`），绕 R 圈是这个因子的 R 次方（`carried_runaway`）。部分在起始之后不给差、起始之差至多 D、每步进入每个条件的'
    '强度（`inflow`）合计至多 M 时：j 阶至多是 D 乘对 i ≤ j 之和，每项是在 t 步中安放 i 次回应的方式数（`Loops.binom`）乘 M^i，t 的'
    ' j 次多项式（`carriedWithin_le_withinBound`、`Loops.withinBound_eq`）；所携带的量至多 D(1 + M)^t（`carried_le_geomBound`）；在 j 阶'
    '截断所漏至多是两者之差（`carried_le_carriedWithin_add`）。一个以强度 M 把自身水平送回自身的条件（自环）三者都恰好达到'
    '（`Loops.SelfLoop.attained`），所以由 D 与 M 推不出更小的界。上游没有回路处，所携带的量至多是步数的多项式，次数比条件数少一'
    '（`carried_le_polynomial`）。形成与强度每步相同（`stationary`）时，每个耦合每步成立，回路每绕一圈至少使到达者加倍'
    '（`carried_doubles_around`），到达上游回路者如此加倍地到达 c（`carried_doubles_into`）；加倍超过每个多项式'
    '（`Loops.not_poly_of_doubling`），所以所携带的量有多项式界，恰在 c 的上游没有回路处（`polynomial_iff_no_loop`）。由 '
    '`most_difference_arrives`，这些是关于一切具有这些强度之律的陈述：上游没有回路处，能到达的最大差别就是有限阶所携带的'
    '（`most_difference_within`），每个差至多是那个多项式（`gap_le_polynomial`）；形成与强度每步相同时，能到达的最大差别有多项式界，恰在'
    '上游没有回路处（`gap_polynomial_iff_no_loop`）。读法（AI 的，待 Ren）：Ren 2026-10-12 把理论比作量子动力学与“Fermi\'s diagrams”'
    '（AI 读作费曼图），说“there are so many patterns and loops but we can still find a way to to integrate so we can still '
    f'calculate this effects but how how accurate can we do that uh what is the limitation do we have losses”（[来源]({SOURCE})）；'
    '`Becoming.Weighted` 对历史之和以四种损失回答，这里对所携带的差别回答：各阶就是那种积分，如同按顶点数求图之和，每一阶加上多一次回应'
    '的路线，`Loops.binom` 数回应的时间次序；截断的精度是剩下的和，并且恰好达到，是只由强度与起始之差所能有的极限；上游没有回路处有限阶'
    '没有损失，有回路处每个有限阶都有损失，到达回路者至少按几何级数增长。只有回路使差别失控：没有回路时所持的差别不断到达，至多按多项式'
    '增长（`Propagation.Chain` 是一次的），有回路时至少按几何级数增长（`Propagation.Loop` 是强度为一的自环）。强度是给出的：一个世界有哪些'
    '回路是其情境（Ren 2026-10-16：“the situation makes it true”）。强度本身、时有时无的耦合、比强度之积更细的失控速度、无穷多条件、'
    f'连续时间与实数的量都不推出。见 [how-a-carried-difference-grows]({RECORD})。')

paragraph_en = (
    '**How a carried difference grows (Part I).** `Becoming.Propagation` gives the most difference that can arrive, with '
    f'witnesses only for loops ([Becoming.Loops]({LEAN})). The carried amount expands by order: order j (`carriedWithin`) '
    'is what routes of at most j responses carry, each order being what the strengths make of the order below '
    '(`carriedFrom`); the orders rise with j to the carried amount (`carriedWithin_mono`, `carriedWithin_le_carried`), and '
    'order j is exact up to step j (`carriedWithin_exact`), as each step adds at most one response. The level of one '
    'condition is coupled into another (`Couples`) where at some step a formation present, outside the part, exchanges '
    'with the second with positive strength on that level; a chain of couplings (`Coupled`) leads from one condition to '
    'another, a loop (`OnLoop`) back to where it started, and e lies upstream of c (`Upstream`) where a chain leads from e '
    'to c. Where no chain of j + 1 couplings ends at c, order j is exact at c at every step '
    '(`carriedWithin_exact_of_not_coupledInto`); with every condition listed, a chain as long as the list passes some '
    'condition twice (`loop_of_coupledInto`, by pigeonhole), so where no loop lies upstream of c, the order one less than '
    'the number of conditions is exact at c at every step (`carriedWithin_exact_of_no_loop`). Where the couplings hold at '
    'every step (`CouplesAlways`), what reaches a loop upstream keeps arriving at c by longer routes, so every order '
    'leaves something out (`carriedWithin_lt_of_loop`): a finite order is exact from every starting gap exactly where no '
    'loop lies upstream (`finite_order_iff_no_loop`); the couplings must hold at every step, as a loop coupled at the '
    'first step only leaves order one exact (`Loops.Once.not_always`). Along a chain with strengths at least w, what '
    'reaches its start '
    'arrives at its end times the product of the strengths (`carried_along`); around a loop, what has reached it returns '
    'multiplied by at least one plus the product of the strengths around it (`carried_around`), and after R times around '
    'by that factor to the power R (`carried_runaway`). With the part giving no gap after the start, starting gaps at most '
    'D and the strengths into each condition (`inflow`) summing to at most M at each step: order j carries at most D times '
    'the sum over i ≤ j of the ways to place i responses among t steps (`Loops.binom`) times M^i, a polynomial in t of '
    'degree j (`carriedWithin_le_withinBound`, `Loops.withinBound_eq`); the carried amount is at most D(1 + M)^t '
    '(`carried_le_geomBound`); and a cut at order j misses at most their difference (`carried_le_carriedWithin_add`). One '
    'condition returning its level to itself with strength M, a self-loop, attains all three exactly '
    '(`Loops.SelfLoop.attained`), so no smaller bound follows from D and M alone. Where no loop lies upstream, the carried '
    'amount is at most a polynomial in the steps, of degree one less than the number of conditions '
    '(`carried_le_polynomial`). With the same formations and strengths at every step (`stationary`), every coupling holds '
    'at every step, every loop at least doubles what reaches it every time around (`carried_doubles_around`), and what '
    'reaches a loop upstream of c arrives at c so doubled (`carried_doubles_into`); a doubling outgrows every polynomial '
    '(`Loops.not_poly_of_doubling`), so the carried amount is bounded by a polynomial exactly where no loop lies upstream '
    'of c (`polynomial_iff_no_loop`). By `most_difference_arrives` these are statements about every law with the '
    'strengths: where no loop lies upstream, the most difference that can arrive is what the finite order carries '
    '(`most_difference_within`), and every gap is at most the polynomial (`gap_le_polynomial`); with the same formations '
    'and strengths at every step, the most difference that can arrive is bounded by a polynomial exactly where no loop lies '
    'upstream (`gap_polynomial_iff_no_loop`). On the AI\'s reading, pending Ren: on 12 October Ren compared the theory '
    'with quantum dynamics and "Fermi\'s diagrams" (read by the AI as Feynman diagrams): “there are so many patterns and '
    'loops but we can still find a way to to integrate so we can still calculate this effects but how how accurate can we '
    f'do that uh what is the limitation do we have losses” ([source]({SOURCE})); `Becoming.Weighted` answered for sums over histories with '
    'four losses, and here the question is answered for the carried difference. The orders are that integration: like a '
    'sum over diagrams by their number of vertices, each order adds the routes with one more response, and `Loops.binom` '
    'counts their time orderings; the accuracy of a cut is the rest of the sum, and it is attained, the limit for what the '
    'strengths and the starting gaps alone allow; where no loop lies upstream a finite order loses nothing, and where one '
    'does every finite order loses something and what reaches the loop grows at least geometrically. Only a loop makes a '
    'difference run away: without one a held difference keeps arriving but grows at most polynomially '
    '(`Propagation.Chain` is of degree one), and with one it grows at least geometrically (`Propagation.Loop` is the '
    'self-loop of strength one). The strengths are supplied: which loops a world has is its situation (Ren, 16 October: '
    '“the situation makes it true”). The strengths themselves, couplings that come and go, how fast a runaway is beyond '
    'the product of the strengths, infinitely many conditions, continuous time and real amounts are not derived. See '
    f'[how-a-carried-difference-grows]({RECORD}).')

whole_zh = (
    '- **所携带的差别怎样增长。** 所携带的量按阶展开，j 阶到第 j 步为止精确（`carriedWithin_exact`）；上游没有回路处有限阶每步精确'
    '（`carriedWithin_exact_of_no_loop`），所携带的量至多是步数的多项式（`carried_le_polynomial`），在 j 阶截断所漏有界且由自环达到'
    '（`carried_le_carriedWithin_add`、`Loops.SelfLoop.attained`）；回路每绕一圈至少乘以一加其强度之积（`carried_runaway`）；形成与强度'
    '每步相同时，有限阶精确与能到达的最大差别有多项式界，都恰在上游没有回路处（`finite_order_iff_no_loop_stationary`、'
    '`gap_polynomial_iff_no_loop`）。')
whole_en = (
    '- **How a carried difference grows.** The carried amount expands by order, order j being exact up to step j '
    '(`carriedWithin_exact`); where no loop lies upstream a finite order is exact at every step '
    '(`carriedWithin_exact_of_no_loop`) and the carried amount is at most a polynomial in the steps '
    '(`carried_le_polynomial`), and a cut at order j misses at most a bound a self-loop attains '
    '(`carried_le_carriedWithin_add`, `Loops.SelfLoop.attained`); a loop multiplies what reaches it, every time around, by '
    'at least one plus the product of its strengths (`carried_runaway`); with the same formations and strengths at every '
    'step, a finite order is exact and the most difference that can arrive is bounded by a polynomial, both exactly where '
    'no loop lies upstream (`finite_order_iff_no_loop_stationary`, `gap_polynomial_iff_no_loop`).')

status_zh = (
    f'；回路：上游没有回路处有限阶精确、所携带的量至多是多项式，截断所漏有界且由自环达到，回路每圈至少乘以一加其强度之积，形成与强度'
    f'每步相同时能到达的最大差别有多项式界恰在上游没有回路处（[how-a-carried-difference-grows]({RECORD})）')

further_zh = (
    '；回路的一般理论已给出（`Becoming.Loops`：所携带的量按阶展开；上游没有回路处有限阶精确、增长至多是多项式；截断所漏有界且由自环'
    '达到；回路每圈至少乘以一加其强度之积；形成与强度每步相同时，有多项式界恰在上游没有回路处）；时有时无的耦合上的回路，比强度之积更细的'
    '失控速度。')
further_en = (
    '; a general theory of loops is given (`Becoming.Loops`: the carried amount expands by order; where no loop lies '
    'upstream a finite order is exact and the growth at most polynomial; a cut misses at most a bound a self-loop attains; '
    'a loop multiplies what reaches it every time around by at least one plus the product of its strengths; with the same '
    'formations and strengths at every step, a polynomial bound holds exactly where no loop lies upstream); loops whose '
    'couplings come and go, and how fast a runaway is beyond the product of the strengths.')

glossary_order = (
    '| 阶（所携带的量的） | order (of the carried amount) | 至多 j 次回应的路线所携带的：强度对下一阶所作的；随 j 上升到所携带的量，'
    '到第 j 步为止精确；上游没有回路处有限阶每步精确；截断所漏有界，自环恰好达到这个界 | `carriedWithin`、`carriedFrom`、'
    '`carriedWithin_exact`、`carriedWithin_exact_of_no_loop`、`carried_le_carriedWithin_add` |')
glossary_loop = (
    '| 回路（耦合的） | loop (of couplings) | 从一个条件经正强度的耦合回到它自身的链；上游的回路有链通向所论条件；到达回路者每绕一圈至少乘以一'
    '加其强度之积；形成与强度每步相同时，只有上游的回路使所携带的差别超过每个多项式 | `Couples`、`Coupled`、`OnLoop`、`Upstream`、'
    '`carried_runaway`、`polynomial_iff_no_loop` |')

docs = {'bullet': bullet, 'scope': scope, 'readme_row': readme_row, 'chapter_row': chapter_row,
        'paragraph_zh': paragraph_zh, 'paragraph_en': paragraph_en, 'whole_zh': whole_zh, 'whole_en': whole_en,
        'status_zh': status_zh, 'further_zh': further_zh, 'further_en': further_en,
        'glossary_order': glossary_order, 'glossary_loop': glossary_loop}
(Path(__file__).resolve().parent / 'docs.json').write_text(json.dumps(docs, ensure_ascii=False, indent=2) + '\n')
print('wrote docs.json', len(docs))
