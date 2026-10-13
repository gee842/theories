"""P88 preserved draft landing, after P78, using becoming-landing-kit.
The integrator supplies S and runs the actual checkers. No proof is added here.
"""
LABEL = 'P88'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md'
PKG = 'becoming-p88-landing'
KEY = 'ORDERNORMAL'
PROVENANCE = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/' + PKG
ZH = ('给定对称相连关系、有限段与交换的自然数名字，安排可达恰在相连交换的先后相同；给出段中不同交换不相连的判定，'
      '可构造字典序最小、幂等的正规形，可达恰在正规形一致时，有限段上自然数值的完整不变量也恰需要该判定。'
      '两侧分开的任意重排双向保持活动与所立者的普查；任意交换给正向保存。每步每个关系项的闲置可判定时，'
      '有最小包含足迹，其相连与次序被所有包含足迹包含；关系项相等可判定时，最小布尔包含足迹的存在恰等价于闲置可判定。')
EN = ('For a symmetric joining relation and a finite stretch of naturally named exchanges, arrangements are reachable '
      'exactly where they orient joined pairs alike. Decided apartness for distinct exchanges gives a lexicographically '
      'least, idempotent normal form; reachability is agreement of forms, and a natural-number-valued complete invariant '
      'compared on the finite stretch needs exactly that decision. Every reordering with split sides preserves activity '
      'and standing census existence both ways; arbitrary commutation preserves it forward. Decided idleness at every '
      'step and relatum gives the least containing footprint, whose joining and order are contained in every containing '
      'footprint’s. With decidable equality of relata, existence of a least Boolean containing footprint is equivalent '
      'to decided idleness.')
BOUND_ZH = ('正规形依赖名字与有限段；没有无名、Foata 同时层或无界正规形。没有从实际世界导出所需判定，也未给不可判定闲置的具体世界。'
            '重排的两侧仍给定；连续时间对应开放。读法由 AI 提出，待 Ren。')
BOUND_EN = ('The normal form depends on names and a finite stretch; no unnamed, Foata-layer or unbounded form is supplied. '
            'No decision is derived for actual worlds and no concrete undecidable-idleness world is given. The sides of '
            'reordering remain supplied; continuous-time correspondence remains open. The readings are the AI’s, pending Ren.')
PACKAGES = [dict(
    module='OrderNormal', package=PKG, key=KEY, prefix='p88', after='Order', layer='L3',
    scope_before='Attraction: for every determined law,',
    bullet='* `Becoming.OrderNormal` (L3): the order of exchanges completed (P88). ' + EN + ' ' + BOUND_EN,
    scope='OrderNormal: ' + EN + ' ' + BOUND_EN,
    readme_zh=ZH, readme_en=EN,
    imports_zh=('`Order` 导入 `Sampling`；', '`Order` 导入 `Sampling`；`OrderNormal` 导入 `Order`；'),
    imports_en=('`Order` imports `Sampling`;', '`Order` imports `Sampling`; `OrderNormal` imports `Order`;'),
)]
IDS = ['normal-forms-need-decided-apartness', 'least-footprint-where-idleness-decided']
LINKS = '、'.join('['+r+'](../results/records/'+r+'.md)' for r in IDS)
PLAN_ZH = ('| P88 交换次序的正规形、普查与最小足迹 ✓ | 接续现存 Claude 草稿；`Becoming.OrderNormal`（{N_ORDERNORMAL} 项定理，只导入 Order）。'
           + ZH + ' ' + BOUND_ZH + ' 新记录 ' + '、'.join(IDS) + '；普查推进 exchanges-commute-unless-joined；研究 §{S_ORDERNORMAL}。 |')
PLAN_EN = ('- **P88:** normal form, census and least footprint. Integrates the existing Claude draft `Becoming.OrderNormal` '
           '({N_ORDERNORMAL} theorems, importing Order only). ' + EN + ' ' + BOUND_EN + ' New records ' + ', '.join(IDS)
           + '; the census advances exchanges-commute-unless-joined; study §{S_ORDERNORMAL}.')
CHAPTER_EDITS = [
    ('before', '**整体与 manifold。**', '**交换的次序：正规形、普查与最小足迹（第一部分，P88）。** ' + ZH + ' ' + BOUND_ZH
     + ' 见 [Becoming.OrderNormal]({LEAN}/OrderNormal.lean)、[研究 §{S_ORDERNORMAL}]({STUDY_ORDERNORMAL})与 ' + LINKS
     + '；普查接入既有 [exchanges-commute-unless-joined](../results/records/exchanges-commute-unless-joined.md)。\n\n'
     + '**The order of exchanges: normal form, census and least footprint (Part I, P88).** ' + EN + ' ' + BOUND_EN),
    ('after_line', '- 过程与框架是同一展开的读法', '- ' + ZH + '（P88）。'),
    ('after_line', '- The process and the frame are readings of one unfolding', '- ' + EN + ' (P88).'),
    ('after_line', '| 一个关系的起点（P69） |', '| 交换的正规形与最小足迹（P88） | 已陈述并检查：' + ZH + ' ' + BOUND_ZH + ' ' + LINKS + ' |'),
    ('after_line', '| L3 | [Becoming.Order]', '| L3 | [Becoming.OrderNormal]({LEAN}/OrderNormal.lean) | ' + ZH + '（P88） | {N_ORDERNORMAL} |'),
    ('replace', 'P78 给出足迹所定的有交集交换偏序，恰刻画可通过交换无交集相邻步达到的次序；最小足迹、正规形与重排中的普查仍开放；',
     'P78 给出足迹所定的相连交换偏序；P88 在有限、有名交换段内以不相连判定构造正规形，双向传递两侧分开的重排之普查，并在闲置可判定时给最小足迹（存在的逆刻画还需关系项相等可判定）；无名、Foata 同时层、无界正规形与连续时间对应仍开放；'),
    ('replace', 'P78 characterizes reachable reorderings by the partial order of joined exchanges for a given footprint; the least footprint, a normal form and censuses along reorderings remain open;',
     'P78 characterizes reachable reorderings by joined-exchange order; P88 gives a named finite normal form with decided apartness, census equivalence along split-sided reorderings, and the least footprint with decided idleness (the existence converse additionally needs decidable equality of relata); unnamed, Foata-layer and unbounded forms and continuous-time correspondence remain open;'),
    ('after_line', '- 一个关系的起点（P69）：', '- P88：有限交换段的正规形以原世界的步作名字；最小足迹由给定闲置判定读出；这些读法与实际对应仍由 Ren 审定。'),
    ('after_line', '- One relational starting point (P69):', '- P88: a finite normal form names exchanges by their original steps; a supplied idleness decision reads off the least footprint. These readings and their actual correspondence remain for Ren’s assessment.'),
]
READING = dict(
    after_en="(P69; Ren agreed that law and history are one unfolding read two ways, “there are no two realities”; the other readings are the AI's, pending Ren). ",
    after_zh='（P69；Ren 同意律与历史是同一展开的两种读法，“there are no two realities”；其余读法是 AI 的，待 Ren）。',
    en=EN + ' ' + BOUND_EN + ' (P88). ', zh=ZH + BOUND_ZH + '（P88）。', lean_after='Order.lean',
)
HISTORY = {KEY: (
    '2026-10-13：接管时保存并整合 Claude P88 既有草稿；原字节与出处保留，不新增证明；见整合文档 §{S}。',
    '2026-10-13: preserved and integrated the existing Claude P88 draft during takeover; original bytes and provenance retained, no proof added; see integration §{S}.'
)}
RECORDS = {
    IDS[0]: dict(package=KEY,
        sections=['Commuting exchanges a relation does not join', 'Arrangements of a stretch', 'The lexicographic normal form',
                  'What the normal form needs: the boundary', "A world's exchanges in normal form", 'Three exchanges, the first and the last joined'],
        named=['rearranges_iff', 'normalForm_iff', 'normalForm_normal', 'normalForm_least', 'complete_iff',
               'decides_of_complete', 'Footprinted.normalize_premises', 'Footprinted.normalize_reorder', 'Triple.not_rearranged'],
        builds_on=['Reindexes', 'Footprinted', 'Footprinted.Contains', 'Footprinted.Joined', 'Footprinted.Precedes',
                   'Footprinted.sorts_iff', 'Footprinted.converse', 'Footprinted.reorder_premises', 'Footprinted.reorder_precedes'],
        provenance=[SOURCE, PROVENANCE + '/provenance.json', PROVENANCE + '/evidence/TASK.md']),
    IDS[1]: dict(package=KEY, sections=['The least footprint'],
        named=['Footprinted.least_contains', 'Footprinted.least_touch_iff', 'Footprinted.least_le', 'Footprinted.least_joined',
               'Footprinted.least_precedes', 'Footprinted.least_keeps', 'Footprinted.least_exists_iff', 'Footprinted.decidesIdle_iff'],
        builds_on=['Footprinted', 'Footprinted.Contains', 'Web.Unmoved', 'Footprinted.Joined.mono',
                   'Footprinted.Precedes.mono', 'Footprinted.Keeps', 'Footprinted.sorts_iff'],
        provenance=[SOURCE, PROVENANCE + '/provenance.json', PROVENANCE + '/evidence/TASK.md']),
}
DELTAS = ['record_delta.py']
