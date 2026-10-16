#!/usr/bin/env python3
"""P125: the root module, the checker's core list, the Lean README, the theory chapter and the study,
with the follow-up for Ren's agreement with P124's readings.

usage: python3 -B apply_docs.py W [SECTION]

New entries go after Thresholds' (P124): the root's import and module bullet, the core list, the
checker's scope entry, the Lean README's L4 row and within-layer imports; in the chapter, a §2
paragraph after "Loops within what a law reads, and the break", one "Part I stated whole" item after
it, the §8 further proof under feedback and reach that P125 answers (how a formation comes to observe
a stock, now given), one §9 L4 row and two glossary rows after "break"; the study section before
"English summary" and its English paragraph at the end.

Follow-up (Ren, 16 October, "agree in general", source 2026-10-16-thresholds-readings-and-measure-
question): the chapter's P124 paragraph marks its readings as agreed by Ren and names the second one;
study §157 gains Ren's decision after its readings, and its English paragraph marks them agreed. The
Thresholds.lean header and the rename of Thresholds.le_of_not_lt are edited in the module itself.
Each change asserts the text it replaces, so a second run fails instead of applying twice.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 159
HERE = Path(__file__).resolve().parent
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
MOD = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Observation.lean'
REC = '../results/records/observation-is-a-route.md'
AGREED = '../../../../sources/15-codex-theory-conversations/2026-10-16-thresholds-readings-and-measure-question.md'
out = {}


def once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


def after_line(text, prefix, *new):
    lines = text.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines[hits[0] + 1:hits[0] + 1] = list(new)
    return '\n'.join(lines)


BULLET = '''* `Becoming.Observation` (L4): observation as a route from what is observed, with no premise
  beyond what each statement names. A gap of one stock alone is conveyed only downstream of it, so
  the carried amount is zero elsewhere. For every law reading into each condition a schedule, two
  courses apart at the start only in a stock are alike at every condition not downstream of it by
  the readings formed so far: a formation's exchange registers the stock only through a level it
  reads that lies downstream, observing the stock itself being the route of length zero. A route
  forms by closing, as a loop does; in the measurement witness the route stock → record and the loop
  through the draw form at the step the measurement starts, and the raise registers after it.'''

SCOPE = ('    "Observation: a gap of one stock alone is conveyed only downstream of it, so the carried amount "\n'
         '    "is zero elsewhere; a law reading a schedule reads it into every condition, a level unread into "\n'
         '    "a condition is coupled into it with strength zero, and routes of the restricted strengths are "\n'
         '    "routes of reading; for every law reading into each condition a schedule of listed levels, two "\n'
         '    "courses apart at the start only in a stock are alike at every condition and step not downstream "\n'
         '    "of it by the readings formed by then, so a formation exchanges alike where its readings lie off "\n'
         '    "the downstream; a route forms by closing; in the measurement witness the route and the loop "\n'
         '    "through the stock form at the step the measurement starts, and the raise registers in the "\n'
         '    "record after it. "\n')

README_ROW = ('| L4 | [`Becoming.Observation`](Becoming/Observation.lean) | 观察是从所观察者出发的路线（除了各定理所写者不加前提）：'
              '起始之差只在一个储量上时，差只被传到它的下游（`conveyed_upstream`），所携带的量在别处为零'
              '（`carried_zero_off_downstream`）；读入每个条件的律（`ExchangeLaw.ReadsInto`；读一个时程者是其特例，'
              '`ExchangeLaw.ReadsAt.readsInto`、`ExchangeLaw.Through.readsInto`）对未读入的水平耦合强度为零'
              '（`ExchangeLaw.ReadsInto.respondsWithin_unread`），强度的路线是所读的路线（`upstream_readCouplings`）；对每个这样的律，'
              '起始只在储量上不同的两个进程，在不在其下游之处都相同（`apart_only_downstream`），形成的交换只经它所读的下游水平回应储量'
              '（`exchange_alike_off_downstream`、`ExchangeLaw.Through.alike_off_downstream`）；路线由闭合而形成（`upstream_succ_iff`）；'
              '量度的见证（`Observation.Measure`）：从储量到记录的路线与经过汲取的回路在量度开始之步形成（`Measure.loop_at`），抬高在其后'
              '经记录被识（`Measure.registers_after`）。/ Observation as a route from what is observed, with no premise beyond '
              'what each theorem names: a gap of one stock alone is conveyed only downstream of it, the carried amount zero '
              'elsewhere; a law reading into each condition a schedule (a law reading a schedule is the case alike for every '
              'condition) is coupled with strength zero to levels unread into a condition, and routes of strength are routes '
              'of reading; for every such law, two courses apart at the start only in a stock are alike wherever not downstream '
              'of it, so a formation registers the stock only through a level it reads downstream; a route forms by closing; '
              'in the measurement witness the route stock → record and the loop through the draw form at the step the '
              'measurement starts, and the raise registers through the record after it. |')

PARA_ZH = (f'**观察是从所观察者出发的路线（第一部分）。** P124 留下一个形成怎样开始观察它所依赖的储量，`Becoming.Runaway` 中观察是给出的；'
           f'2026-10-16 Ren 认可 P124 的做法并让继续（[Becoming.Observation]({MOD})）。起始之差只在储量 c 上、部分不给差时，在第 t 步被传到'
           '的条件都在 c 的下游，按到 t 为止形成的耦合（`conveyed_upstream`），所以所携带的量，能到达的最多的差，在别处为零'
           '（`carried_zero_off_downstream`）。一个律读入每个条件一个时程（`ExchangeLaw.ReadsInto`），是说形成与一个条件的交换只由为那个'
           '条件所标的水平决定；读一个时程的律是对所有条件读得一样的特例（`ExchangeLaw.ReadsAt.readsInto`、`ExchangeLaw.Through.readsInto`），'
           '未读入的水平耦合强度为零（`ExchangeLaw.ReadsInto.respondsWithin_unread`），强度的路线是所读的路线（`upstream_readCouplings`）。'
           '对每个这样的律，起始只在 c 上不同的两个平衡进程，在每一步，凡不在 c 下游（按到那一步形成的所读路线）的条件都相同'
           '（`apart_only_downstream`），不判定条件、不需条件有限：一个形成的交换回应储量之差，只经它所读的、在储量下游的水平'
           '（`exchange_alike_off_downstream`、`ExchangeLaw.Through.alike_off_downstream`）。所观察的储量是长度为零的路线。路线由闭合而形成，'
           '如回路（`upstream_succ_iff`、`route_forms_by_closing`）。见证（`Observation.Measure`）：一个形成从第 T 步起把储量的水平加到记录上，'
           '在记录显示至少 N 时从储量汲取；T 之前储量下游只有它自己、没有经过它的回路，在第 T 步从储量到记录的路线与储量 → 记录 → 汲取的'
           '回路形成（`Measure.loop_at`）；只在储量上不同的进程，记录到 T 为止相同，其后差出抬高（`Measure.registers_after`），汲取回应记录'
           f'（`Measure.draw_responds`）。读法（AI 的，待 Ren）：观察不是依赖之外的第二种关系，而是站在从所观察者出发的所读路线的末端；一个'
           f'形成开始观察，是一次读闭合一条路线。见 [observation-is-a-route]({REC})。')

PARA_EN = (f'**Observation as a route from what is observed (Part I).** P124 left open how a formation comes to observe a stock '
           f'it depends on, observation being given in `Becoming.Runaway`; on 16 October Ren approved P124\'s approach and said '
           f'to continue ([Becoming.Observation]({MOD})). With the starting gap at a stock c alone and none from the part, a gap '
           'conveyed to a condition at step t lies downstream of c by the couplings formed by t (`conveyed_upstream`), so the '
           'carried amount, the most difference that can arrive, is zero elsewhere (`carried_zero_off_downstream`). A law reads '
           'into each condition a schedule (`ExchangeLaw.ReadsInto`) when what a formation exchanges with a condition is fixed '
           'by the levels marked for that condition; a law reading a schedule is the case reading alike for every condition '
           '(`ExchangeLaw.ReadsAt.readsInto`, `ExchangeLaw.Through.readsInto`), a level unread into a condition is coupled into '
           'it with strength zero (`ExchangeLaw.ReadsInto.respondsWithin_unread`), and routes of strength are routes of reading '
           '(`upstream_readCouplings`). For every such law, two balanced courses apart at the start only in c are alike, at '
           'each step, at every condition not downstream of c by the readings formed by then (`apart_only_downstream`), with no '
           'decision on conditions and no finiteness: a formation\'s exchange responds to the stock\'s difference only through '
           'a level it reads that lies downstream of the stock (`exchange_alike_off_downstream`, '
           '`ExchangeLaw.Through.alike_off_downstream`). The stock it observes is the route of length zero. A route forms by '
           'closing, as a loop does (`upstream_succ_iff`, `route_forms_by_closing`). Witness (`Observation.Measure`): from '
           'step T a formation adds the stock\'s level to a record and draws from the stock while the record shows at least N; '
           'before T only the stock lies downstream of it and no loop passes through it; at T the route stock → record and '
           'the loop stock → record → draw form (`Measure.loop_at`); in courses apart only on the stock the record is alike up '
           'to T and differs by the raise after it (`Measure.registers_after`), and the draw responds to the record '
           '(`Measure.draw_responds`). Readings (the AI\'s, pending Ren): observation is not a second relation beside '
           'dependence but standing at the end of a route of readings from what is observed; a formation comes to observe by a '
           f'reading that closes a route. See [observation-is-a-route]({REC}).')

WHOLE_ZH = ('- **观察是从所观察者出发的路线。** 起始之差只在一个储量上时，差只往它的下游去（`conveyed_upstream`）；对每个读入每个条件的律，'
            '只在储量上不同的进程在不在其下游之处都相同（`apart_only_downstream`）：形成只经它所读的下游水平识储量，所观察者是长度为零的'
            '路线；路线由闭合而形成（`upstream_succ_iff`）。')
WHOLE_EN = ('- **Observation as a route from what is observed.** A gap of one stock alone goes only downstream of it '
            '(`conveyed_upstream`); for every law reading into each condition, courses apart only in the stock are alike '
            'wherever not downstream of it (`apart_only_downstream`): a formation registers the stock only through a level it '
            'reads downstream, what it observes being the route of length zero; a route forms by closing '
            '(`upstream_succ_iff`).')

FURTHER_ZH_OLD = '一个形成怎样开始观察它所依赖的储量；'
FURTHER_ZH = ('一个形成怎样开始观察它所依赖的储量已给出（`Becoming.Observation`：差只往下游去，形成只经它所读的、在储量下游的水平识储量，'
              '观察是从所观察者出发的路线，由闭合而形成）；')
FURTHER_EN_OLD = 'how a formation comes to observe a stock it depends on; '
FURTHER_EN = ('how a formation comes to observe a stock it depends on is given (`Becoming.Observation`: a difference goes only '
              'downstream, and a formation registers the stock only through a level it reads downstream of it; observation is a '
              'route from what is observed, forming by closing); ')

CHAPTER_ROW = (f'| L4 | [Becoming.Observation]({MOD}) | 观察是从所观察者出发的路线（除了各定理所写者不加前提）：起始之差只在一个储量上时，'
               '差只往它的下游去，所携带的量在别处为零；对每个读入每个条件的律，只在储量上不同的进程在不在其下游之处都相同，形成只经它所读的'
               '下游水平识储量；路线由闭合而形成；量度的见证中路线与回路在量度开始之步形成。/ Observation as a route from what is '
               'observed, with no premise beyond what each theorem names: a gap of one stock alone goes only downstream of it, '
               'the carried amount zero elsewhere; for every law reading into each condition, courses apart only in the stock '
               'are alike wherever not downstream of it, so a formation registers the stock only through a level it reads '
               'downstream; a route forms by closing; in the measurement witness the route and the loop form at the step the '
               'measurement starts. |')

GLOSSARY = [
    '| 读入（每个条件的时程） | reading into (each condition, a schedule) | 形成与一个条件的交换只由为那个条件所标的水平决定；读一个时程'
    '者是对所有条件读得一样的特例；未读入的水平耦合强度为零 | `ExchangeLaw.ReadsInto`、`readCouplings`、`restrictInto`、'
    '`ExchangeLaw.ReadsAt.readsInto` |',
    '| 下游（储量之差的） | downstream (of a stock\'s difference) | 从储量出发、按到某步形成的所读路线可达的条件；只在储量上不同的进程在'
    '不在下游之处相同；所观察者是长度为零的路线 | `Upstream`、`conveyed_upstream`、`apart_only_downstream`、`upstream_succ_iff`、'
    '`Observation.Measure` |',
]

# Ren's agreement with P124's readings (16 October).
P124_ZH_OLD = ('读法（AI 的，待 Ren）：失控的断裂就是回路形成之处；`Becoming.Runaway` 的不识与 `Becoming.Closing` 的形成是同一件事的'
               '两面。')
P124_ZH_NEW = ('读法（AI 的，Ren 2026-10-16 同意）：失控的断裂就是回路形成之处；`Becoming.Runaway` 的不识与 `Becoming.Closing` 的形成是'
               '同一件事的两面；能识断裂还有多远者，是断裂之前对储量水平的读。')
P124_EN_OLD = ("Readings (the AI's, pending Ren): a runaway's break is where a loop forms; the blindness of `Becoming.Runaway` "
               "and the formation of `Becoming.Closing` are one event seen from two sides.")
P124_EN_NEW = ("Readings (the AI's, agreed by Ren on 16 October): a runaway's break is where a loop forms; the blindness of "
               "`Becoming.Runaway` and the formation of `Becoming.Closing` are one event seen from two sides; what can register "
               "how near the break is, is a reading of the stock's level before it.")

DECISION_ZH = (f'**Ren 的决定（2026-10-16）。** P124 落地之后，对两项读法与改名的问题，Ren 答：“agree in general, need more '
               f'explanation for c”（[来源]({AGREED})；c 是脊柱整合量度的修正，另行解释，不在本节）。AI 读为 Ren 取这两项读法，并同意把 '
               '`Thresholds.le_of_not_lt` 改名为 `Thresholds.le_of_not_not`（它的前提是 `¬¬ a ≤ b`，新名字恰说它所证者），陈述与证明不变；'
               '改名随 P125（§{0}）落地。“in general”没有指出保留，AI 不读为对落地文字每一字的判断。').format(SECTION)
DECISION_EN = ("- **Ren's decision (16 October 2026).** Asked after P124 landed about the two readings and the renaming, Ren "
               f"wrote “agree in general, need more explanation for c” ([source]({AGREED}); c is the fix to the spine-integration "
               "measure, explained separately), read by the AI as taking both readings and agreeing to rename "
               "`Thresholds.le_of_not_lt` to `Thresholds.le_of_not_not`, which states exactly what it proves; the rename lands "
               f"with P125 (section {SECTION}).")
P124_STUDY_EN_OLD = "- **Readings (the AI's, pending Ren).** A runaway's break is where a loop forms"
P124_STUDY_EN_NEW = "- **Readings (the AI's, agreed by Ren).** A runaway's break is where a loop forms"

path = L / 'Becoming.lean'
t = path.read_text()
t = once(t, '\nimport Becoming.Thresholds\n', '\nimport Becoming.Thresholds\nimport Becoming.Observation\n')
last = '  stock, so the loop through the stock forms at the break, unforeseen.\n'
t = once(t, last, last + BULLET + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Thresholds", ', '"Becoming.Thresholds", "Becoming.Observation", ')
end = '    "the break. "\n'
t = once(t, end, end + SCOPE)
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Thresholds`]', README_ROW)
t = once(t, '；`Thresholds` 导入 `Closing` 与 `Runaway`', '；`Thresholds` 导入 `Closing` 与 `Runaway`；`Observation` 导入 `Thresholds`')
t = once(t, '; `Thresholds` imports `Closing` and `Runaway`',
         '; `Thresholds` imports `Closing` and `Runaway`; `Observation` imports `Thresholds`')
out[path] = t

t = CHAPTER.read_text()
t = once(t, P124_ZH_OLD, P124_ZH_NEW)
t = once(t, P124_EN_OLD, P124_EN_NEW)
t = after_line(t, '**Loops within what a law reads, and the break (Part I).**', '', PARA_ZH, '', PARA_EN)
t = after_line(t, '- **回路在律所读之内，与断裂。**', WHOLE_ZH)
t = after_line(t, '- **Loops within what a law reads, and the break.**', WHOLE_EN)
t = once(t, FURTHER_ZH_OLD, FURTHER_ZH)
t = once(t, FURTHER_EN_OLD, FURTHER_EN)
t = after_line(t, '| L4 | [Becoming.Thresholds]', CHAPTER_ROW)
t = after_line(t, '| 断裂（只在低于阈值时才读的储量的） |', *GLOSSARY)
out[CHAPTER] = t

section = (HERE / 'study.md').read_text().replace('{SECTION}', str(SECTION))
paragraph = (HERE / 'study-en.md').read_text().replace('{SECTION}', str(SECTION))
t = STUDY.read_text()
assert section.splitlines()[0] not in t and paragraph.splitlines()[0][:60] not in t
t = after_line(t, '2. **能识距离者是断裂之前对储量水平的读。**', '', DECISION_ZH)
t = once(t, P124_STUDY_EN_OLD, P124_STUDY_EN_NEW)
t = after_line(t, "- **Readings (the AI's, agreed by Ren).** A runaway's break is where a loop forms", DECISION_EN)
anchor = '\n## English summary\n'
t = once(t, anchor, '\n' + section.rstrip('\n') + '\n' + anchor)
t = t.rstrip('\n') + '\n\n' + paragraph.rstrip('\n') + '\n'
out[STUDY] = t

for p, text in out.items():
    p.write_text(text)
print('root, checker, Lean README, chapter and study updated; section', SECTION)
