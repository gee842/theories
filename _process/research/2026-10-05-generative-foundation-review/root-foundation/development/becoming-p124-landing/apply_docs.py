#!/usr/bin/env python3
"""P124: the root module, the checker's core list, the Lean README, the theory chapter and the study.

usage: python3 -B apply_docs.py W [SECTION]

New entries go after Closing's (P122): the root's import and module bullet, the core list, the
checker's scope entry, the Lean README's L4 row and within-layer imports; in the chapter, a §2
paragraph after "How loops form within the unfolding", one "Part I stated whole" item after "How loops
form", the §8 further proof under feedback and reach that P124 answers (now given; how a formation
comes to observe a stock stays open), one §9 L4 row and two glossary rows after "closing"; the study
section before "English summary" and its English paragraph at the end. Each change asserts the text it
replaces, so a second run fails instead of applying twice.
"""
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 157
HERE = Path(__file__).resolve().parent
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
MOD = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Thresholds.lean'
REC = '../results/records/loops-within-what-a-law-reads.md'
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


BULLET = '''* `Becoming.Thresholds` (L4): loops within what a law reads, and the break, with no premise
  beyond what each statement names. A law reading a schedule is coupled to every unread level with
  strength zero, so every coupling, chain and loop runs through levels read, and a loop forms at a
  step only through a formation reading there a level downstream of where it gives. For every law,
  two courses apart only in a stock nothing reads are alike everywhere else. A law reading a stock
  only below a threshold, as one registering it without observing it does, carries a raise of the
  stock nowhere up to the break; before the break it is its standing law, with no loop through the
  stock, so the loop through the stock forms at the break, unforeseen.'''

SCOPE = ('    "Thresholds: a law reading a schedule is coupled to every unread level with strength zero, so "\n'
         '    "the strengths restricted to what is read are strengths of it, every coupling reads its level, "\n'
         '    "no loop passes through a level nothing reads, and a loop forms at a step only through a "\n'
         '    "formation reading there a level downstream of where it gives; laws reading through a "\n'
         '    "registration read every schedule covering it, and their courses are policies through it; for "\n'
         '    "every law, courses apart only in an unread stock are alike elsewhere, the gap held; a law "\n'
         '    "reading a stock only below a threshold, every law reading through a registration with the "\n'
         '    "stock unobserved among them, carries a raise of it nowhere up to the break, and before the "\n'
         '    "break gives as its standing law, which does not read the stock and has no loop through it; in "\n'
         '    "the draw witness every strength couples the stock into itself, and a raise shows only after "\n'
         '    "the break. "\n')

README_ROW = ('| L4 | [`Becoming.Thresholds`](Becoming/Thresholds.lean) | 回路在律所读之内，与断裂（除了各定理所写者不加前提）：'
              '读一个时程的律对每个未读的水平耦合强度为零（`ExchangeLaw.ReadsAt.respondsWithin_unread`），所以限于所读的强度是它的强度'
              '（`ExchangeLaw.ReadsAt.restrict`）；经识而读的律读每个覆盖其识的时程（`ExchangeLaw.Through.readsAt`），其进程是经识的策略'
              '（`ExchangeLaw.Through.policyThrough`）；每个耦合读其水平（`couples_reads`），没有回路经过无人读的水平'
              '（`not_onLoop_unread`），回路在一步形成只经过在那一步读其所给之处下游水平的形成（`onLoop_succ_reads`）；对每个律，只在'
              '无人读的储量上不同的两个进程在别处相同（`unread_carried_nowhere`）；只在储量低于阈值时才读它的律'
              '（`ExchangeLaw.ReadsBelow`，经识而不观察储量者是其实例：`ExchangeLaw.Through.readsBelow`）到断裂为止不把储量的抬高带到'
              '任何处（`break_carried_nowhere`），断裂之前就是其立律（`ExchangeLaw.standing`、`Flow.follows_standing_before`），'
              '不读储量、没有经过它的回路（`ExchangeLaw.ReadsBelow.standing_no_loop`）；汲取的见证（`Thresholds.Draw`）：每个强度都把'
              '储量耦合到自身（`Draw.onLoop`），抬高只在断裂之后显出（`Draw.diverges_at_break`）。/ Loops within what a law reads, and '
              'the break, with no premise beyond what each theorem names: a law reading a schedule is coupled to every unread level '
              'with strength zero, so the strengths restricted to what is read are strengths of it; a law reading through a '
              'registration reads every schedule covering it, and its courses are policies through registration; every coupling '
              'reads its level, no loop passes through a level nothing reads, and a loop forms at a step only through a '
              'formation reading there a level downstream of where it gives; for every law, two courses apart only in a stock '
              'nothing reads are alike elsewhere; a law reading a stock only below a threshold (one registering it without '
              'observing it is an instance) carries a raise of the stock nowhere up to the break, and before the break is its '
              'standing law, which does not read the stock and has no loop through it; in the draw witness every strength '
              'couples the stock into itself, and a raise shows only after the break. |')

PARA_ZH = (f'**回路在律所读之内，与断裂（第一部分）。** Ren 取了的读法留下“一个形成的汲取开始回应其汲取所降低的水平，那里与 '
           f'`Becoming.Runaway` 相遇”，2026-10-16 Ren 让把两者接起来（[Becoming.Thresholds]({MOD})）。一个律读一个时程'
           '（`ExchangeLaw.ReadsAt`），是说对部分之外的每个形成，在时程所标的条件上一致的历史下它给得相同。未读的水平耦合强度为零'
           '（`ExchangeLaw.ReadsAt.respondsWithin_unread`），所以限于所读的强度是律的强度（`ExchangeLaw.ReadsAt.restrict`）；经识而读的'
           '律读每个覆盖其识的时程（`ExchangeLaw.Through.readsAt`），其进程是 `Becoming.Runaway` 意义上经识的策略'
           '（`ExchangeLaw.Through.policyThrough`）。于是回路在所读之内：每个耦合读其水平（`couples_reads`），汲取回应它所降低的水平'
           '只在它读之处（`self_coupling_reads`），没有回路经过无人读的水平（`not_onLoop_unread`），回路在一步形成只经过在那一步读其所给'
           '之处下游水平的形成（`onLoop_succ_reads`）。对每个律，只在一个无人读的储量上不同的两个进程，在别处都相同，储量之差保持'
           '（`unread_carried_nowhere`）。一个律只在储量低于阈值时才读它（`ExchangeLaw.ReadsBelow`），是说储量立于阈值时律只读它立着；'
           '经识而读、部分之外无人观察储量、阈值不低于各自所需者的律都是这样（`ExchangeLaw.Through.readsBelow`），所以 '
           '`Becoming.Runaway` 的形成是其实例。对每个这样的律，储量抬高多少，到断裂为止别处都不变（`break_carried_nowhere`）：断裂还有'
           '多远不被带到任何处，对整个律而言，不只是其余固定的一个策略。断裂之前律就是其立律（`ExchangeLaw.standing`、'
           '`Flow.follows_standing_before`），它不读储量、对储量的耦合强度为零、没有经过储量的回路'
           '（`ExchangeLaw.ReadsBelow.standing_no_loop`）：经过储量的回路在断裂处形成。见证（`Thresholds.Draw`）：一个形成在储量立于 '
           'N + 1 时每步从储量汲取一个单位给产物；它的每个强度都把储量耦合到自身，一圈的回路（`Draw.onLoop`），断裂之前却给得如其立律'
           '（`Draw.forms_at_break`）；一步上一个进程的储量低于阈值、抬高者的立着，那一步抬高者多给产物一（`Draw.diverges_at_break`）。'
           f'读法（AI 的，待 Ren）：失控的断裂就是回路形成之处；`Becoming.Runaway` 的不识与 `Becoming.Closing` 的形成是同一件事的两面。见 '
           f'[loops-within-what-a-law-reads]({REC})。')

PARA_EN = (f'**Loops within what a law reads, and the break (Part I).** The reading Ren took left open “where a formation\'s '
           f'drawing comes to respond to the level its drawing lowers, where this meets `Becoming.Runaway`”, and on 16 '
           f'October Ren gave the go to join them ([Becoming.Thresholds]({MOD})). A law reads a schedule '
           '(`ExchangeLaw.ReadsAt`) when, for each formation outside the part, it gives alike under histories agreeing on the '
           'conditions the schedule marks. An unread level is coupled with strength zero '
           '(`ExchangeLaw.ReadsAt.respondsWithin_unread`), so the strengths restricted to what is read are strengths of the law '
           '(`ExchangeLaw.ReadsAt.restrict`); a law reading through a registration reads every schedule covering it '
           '(`ExchangeLaw.Through.readsAt`), and its courses are policies through registration in the sense of '
           '`Becoming.Runaway` (`ExchangeLaw.Through.policyThrough`). So loops lie within what is read: every coupling reads its '
           'level (`couples_reads`), a draw responds to the level it lowers only where it reads it (`self_coupling_reads`), no '
           'loop passes through a level nothing reads (`not_onLoop_unread`), and a loop forms at a step only through a '
           'formation reading there a level downstream of where it gives (`onLoop_succ_reads`). For every law, two courses '
           'apart only in a stock nothing reads are alike everywhere else, the stock\'s gap held (`unread_carried_nowhere`). A '
           'law reads a stock only below a threshold (`ExchangeLaw.ReadsBelow`) when, while the stock stands at the threshold, '
           'it reads only that it stands; every law reading through a registration in which no formation outside the part '
           'observes the stock, with the threshold at least each need of it, is such a law (`ExchangeLaw.Through.readsBelow`), '
           'so `Becoming.Runaway`\'s formation is an instance. For every such law, raising the stock by any amount changes '
           'nothing else up to the break (`break_carried_nowhere`): the distance to the break is carried nowhere, for the '
           'whole law and not only for one policy with the rest fixed. Before the break the law is its standing law '
           '(`ExchangeLaw.standing`, `Flow.follows_standing_before`), which does not read the stock, is coupled to it with '
           'strength zero and has no loop through it (`ExchangeLaw.ReadsBelow.standing_no_loop`): the loop through the stock '
           'forms at the break. Witness (`Thresholds.Draw`): a formation draws one unit from a stock and gives it to a product '
           'at each step while the stock stands at N + 1; every strengths of it couple the stock into itself, a loop of one '
           '(`Draw.onLoop`), yet before the break it gives as its standing law (`Draw.forms_at_break`); at a step where one '
           'course\'s stock stands below the threshold and a raised one\'s at it, the raised course gives one more to the '
           'product (`Draw.diverges_at_break`). Readings (the AI\'s, pending Ren): a runaway\'s break is where a loop forms; '
           'the blindness of `Becoming.Runaway` and the formation of `Becoming.Closing` are one event seen from two sides. See '
           f'[loops-within-what-a-law-reads]({REC}).')

WHOLE_ZH = ('- **回路在律所读之内，与断裂。** 未读的水平耦合强度为零，没有回路经过无人读的水平，回路在一步形成只经过在那一步读的形成'
            '（`not_onLoop_unread`、`onLoop_succ_reads`）；只在储量低于阈值时才读它的律，到断裂为止不把储量的抬高带到任何处'
            '（`break_carried_nowhere`），断裂之前没有经过储量的回路（`ExchangeLaw.ReadsBelow.standing_no_loop`）：回路在断裂处形成。')
WHOLE_EN = ('- **Loops within what a law reads, and the break.** An unread level is coupled with strength zero, no loop passes '
            'through a level nothing reads, and a loop forms at a step only through a formation reading there '
            '(`not_onLoop_unread`, `onLoop_succ_reads`); a law reading a stock only below a threshold carries a raise of it '
            'nowhere up to the break (`break_carried_nowhere`), with no loop through the stock before it '
            '(`ExchangeLaw.ReadsBelow.standing_no_loop`): the loop forms at the break.')

FURTHER_ZH = ('回路在律所读之内、经过储量的回路在断裂处形成已给出（`Becoming.Thresholds`：未读的水平耦合强度为零，回路在一步形成只经过'
              '在那一步读的形成；只在储量低于阈值时才读它的律，到断裂为止不把储量的抬高带到任何处，断裂之前没有经过储量的回路）；一个形成'
              '怎样开始观察它所依赖的储量；')
FURTHER_EN = ('loops within what a law reads, and the loop through a stock forming at its break, are given '
              '(`Becoming.Thresholds`: an unread level is coupled with strength zero, and a loop forms at a step only through '
              'a formation reading there; a law reading a stock only below a threshold carries a raise of it nowhere up to '
              'the break, with no loop through the stock before it); how a formation comes to observe a stock it depends '
              'on; ')

CHAPTER_ROW = (f'| L4 | [Becoming.Thresholds]({MOD}) | 回路在律所读之内，与断裂（除了各定理所写者不加前提）：未读的水平耦合强度为零，'
               '每个耦合读其水平，没有回路经过无人读的水平，回路在一步形成只经过在那一步读的形成；对每个律，只在无人读的储量上不同的进程在'
               '别处相同；只在储量低于阈值时才读它的律，经识而不观察储量者是其实例，到断裂为止不把储量的抬高带到任何处，断裂之前没有经过'
               '储量的回路，回路在断裂处形成。/ Loops within what a law reads, and the break, with no premise beyond what each '
               'theorem names: an unread level is coupled with strength zero, every coupling reads its level, no loop passes '
               'through a level nothing reads, and a loop forms at a step only through a formation reading there; for every '
               'law, courses apart only in an unread stock are alike elsewhere; a law reading a stock only below a threshold, '
               'one registering it without observing it being an instance, carries a raise of it nowhere up to the break, '
               'with no loop through the stock before it: the loop forms at the break. |')

GLOSSARY = [
    '| 律所读（的时程） | what a law reads (schedule) | 对部分之外的每个形成，在所标条件上一致的历史下律给得相同；未读的水平耦合强度为零，'
    '回路在所读之内 | `ExchangeLaw.ReadsAt`、`restrictReads`、`ExchangeLaw.ReadsAt.respondsWithin_unread`、`couples_reads`、'
    '`onLoop_succ_reads` |',
    '| 断裂（只在低于阈值时才读的储量的） | break (of a stock read only below a threshold) | 储量立于阈值时律只读它立着；断裂之前律是其'
    '立律，不读储量、没有经过它的回路，储量的抬高不被带到任何处；经过储量的回路在断裂处形成 | `ExchangeLaw.ReadsBelow`、'
    '`ExchangeLaw.standing`、`break_carried_nowhere`、`ExchangeLaw.ReadsBelow.standing_no_loop`、`Thresholds.Draw` |',
]

path = L / 'Becoming.lean'
t = path.read_text()
t = once(t, '\nimport Becoming.Closing\n', '\nimport Becoming.Closing\nimport Becoming.Thresholds\n')
last = ('  amount of the strengths it reads; in the threshold witness a loop forms at the step a level\n'
        '  reaches the threshold and doubles from then on.\n')
t = once(t, last, last + BULLET + '\n')
out[path] = t

path = L / 'check_becoming.py'
t = path.read_text()
t = once(t, '"Becoming.Closing", ', '"Becoming.Closing", "Becoming.Thresholds", ')
end = '    "the step the level reaches the threshold and the level plus one doubles from then on. "\n'
t = once(t, end, end + SCOPE)
out[path] = t

path = L / 'README.md'
t = path.read_text()
t = after_line(t, '| L4 | [`Becoming.Closing`]', README_ROW)
t = once(t, '；`Closing` 导入 `Remainder`）', '；`Closing` 导入 `Remainder`；`Thresholds` 导入 `Closing` 与 `Runaway`）')
t = once(t, '; `Closing` imports `Remainder`)', '; `Closing` imports `Remainder`; `Thresholds` imports `Closing` and `Runaway`)')
out[path] = t

t = CHAPTER.read_text()
t = after_line(t, '**How loops form within the unfolding (Part I).**', '', PARA_ZH, '', PARA_EN)
t = after_line(t, '- **回路怎样形成。**', WHOLE_ZH)
t = after_line(t, '- **How loops form.**', WHOLE_EN)
t = once(t, '在一个律中把回路的形成与 `Becoming.Runaway` 的策略连起来；', FURTHER_ZH)
t = once(t, "joining the formation of loops and `Becoming.Runaway`'s policies within one law; ", FURTHER_EN)
t = after_line(t, '| L4 | [Becoming.Closing]', CHAPTER_ROW)
t = after_line(t, '| 闭合（回路的形成） |', *GLOSSARY)
out[CHAPTER] = t

section = (HERE / 'study.md').read_text().replace('{SECTION}', str(SECTION))
paragraph = (HERE / 'study-en.md').read_text().replace('{SECTION}', str(SECTION))
t = STUDY.read_text()
assert section.splitlines()[0] not in t and paragraph.splitlines()[0][:60] not in t
anchor = '\n## English summary\n'
t = once(t, anchor, '\n' + section.rstrip('\n') + '\n' + anchor)
t = t.rstrip('\n') + '\n\n' + paragraph.rstrip('\n') + '\n'
out[STUDY] = t

for p, text in out.items():
    p.write_text(text)
print('root, checker, Lean README, chapter and study updated; section', SECTION)
