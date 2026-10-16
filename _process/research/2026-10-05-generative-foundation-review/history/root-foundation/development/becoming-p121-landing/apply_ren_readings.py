#!/usr/bin/env python3
"""Ren's agreement of 16 October 2026 with the readings of P121 and P122, and with P118's third reading as revised.

usage: python3 -B apply_ren_readings.py W

Source: sources/15-codex-theory-conversations/2026-10-16-routes-closing-readings.md (“alright, agree”).
Writes: the readings headers of Routes.lean and Closing.lean and one sentence after the third reading of
Loops.lean (comments only); in the chapter, the readings clauses of the Routes and Closing paragraphs
and the dated clause after the third reading of the Loops paragraph (zh and en); a dated paragraph
after the readings of study §155 and §156 and a bullet in each English paragraph; in
orders-as-a-sum-over-histories, how-loops-form and how-a-carried-difference-grows the correspondence,
the source as a provenance reference and one paired history note. Ren's earlier readings stay as
recorded; statements and proofs unchanged. Each change asserts the text it replaces.
"""
import hashlib
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-routes-closing-readings.md'
L = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
REC = W / 'theories/becoming/results/records'
out = {}

# P118's third reading as revised (the AI's wording, taken by Ren)
THIRD_ZH = ('一个世界有哪些回路是其情境的一部分：回路在展开中由闭合而形成，在某个交换开始回应它所给条件下游的一个水平之步形成；'
            '在其耦合停止处消解（时程安定之后，有限阶精确恰在其后的耦合没有回路在上游处）；强度从进程读出时，哪些回路形成、何时形成'
            '从展开读出；定理按每步所立者取之，强度或读出强度的方式是给出的')
THIRD_EN = ('which loops a world has is part of its situation: loops form within the unfolding by closing, a loop forming at '
            'the step at which some exchange comes to respond to a level downstream of the condition it gives to, and '
            'dissolve where their couplings stop (once the schedule has settled, a finite order is exact exactly where no '
            'loop of the couplings that go on lies upstream); where the strengths are read off the course, which loops '
            'form and when is read off the unfolding; the theorems take the loops as they stand at each step, the '
            'strengths or the way they are read being supplied')


def once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


def after_block(text, heading, marker, insert):
    """Insert `insert` before the first `marker` after `heading`."""
    assert text.count(heading) == 1, heading
    i = text.index(heading)
    j = text.index(marker, i)
    return text[:j] + insert + text[j:]


# Lean module docstrings (comments only)
for name in ('Routes', 'Closing'):
    path = L / f'{name}.lean'
    out[path] = once(path.read_text(), '**Readings (the AI\'s, pending Ren).**',
                     '**Readings (the AI\'s, taken by Ren on 16 October 2026).**')
path = L / 'Loops.lean'
old = ("  where a formation's drawing comes to respond to the level its drawing lowers, where this meets\n"
       '  `Becoming.Runaway`.\n')
out[path] = once(path.read_text(), old, old +
                 '  On 16 October, with the loop-formation theorem of `Becoming.Closing`, Ren took the reading as\n'
                 '  revised: loops form within the unfolding by closing, at the step at which some exchange comes\n'
                 '  to respond to a level downstream of the condition it gives to, and dissolve where their\n'
                 '  couplings stop (`Becoming.Remainder`); where the strengths are read off the course, which loops\n'
                 '  form and when is read off the unfolding.\n')

# chapter
t = CHAPTER.read_text()
t = once(t, '（2026-10-16 之后，回路形成的定理是 `Becoming.Closing`：回路由闭合一条链的耦合而形成；这一读法待 Ren 再议）',
         '（2026-10-16 之后，回路形成的定理是 `Becoming.Closing`，Ren 同意读法修订为：' + THIRD_ZH + '；'
         '[来源](../../../' + SOURCE + ')）')
t = once(t, "(after 16 October the loop-formation theorem is `Becoming.Closing`: a loop forms through a coupling that "
            "closes a chain; this reading awaits Ren's revision)",
         '(after 16 October the loop-formation theorem is `Becoming.Closing`, and Ren agreed to the reading as revised: '
         + THIRD_EN + '; [source](../../../' + SOURCE + '))')
t = once(t, '读法（AI 的，待 Ren）：两个积分是一个', '读法（AI 的，Ren 2026-10-16 同意）：两个积分是一个')
t = once(t, "Readings (the AI's, pending Ren): the two integrations are one",
         "Readings (the AI's, agreed by Ren on 16 October): the two integrations are one")
t = once(t, '读法（AI 的，待 Ren）：回路在某个交换', '读法（AI 的，Ren 2026-10-16 同意）：回路在某个交换')
t = once(t, "Readings (the AI's, pending Ren): a loop forms by closing",
         "Readings (the AI's, agreed by Ren on 16 October): a loop forms by closing")
out[CHAPTER] = t

# study
SRC_ST = '../../../../' + SOURCE
t = STUDY.read_text()
t = after_block(t, '## 155. 携带差别的阶作为历史之和', '\n**作者反审。**',
                f'\n**Ren 的决定（2026-10-16）。** Ren 答 P121 与 P122 落地的报告：“alright, agree”（[来源]({SRC_ST})）。'
                'AI 读为 Ren 取这两条读法，用 AI 的措辞；两个积分是一个，对应是结构的。\n')
t = after_block(t, '## 156. 回路怎样在展开中形成', '\n**作者反审。**',
                f'\n**Ren 的决定（2026-10-16）。** 同一句“alright, agree”（[来源]({SRC_ST})）。AI 读为 Ren 取这两条读法，'
                f'并取 P118 第三项读法的修订形式：{THIRD_ZH}。在一个律中把回路的形成与 `Becoming.Runaway` 的策略连起来，'
                'AI 不读为已开始；P120 的读法不在其中。\n')
t = once(t, '- **Readings (the AI\'s, pending Ren).** The structural match is now exact:',
         '- **Ren\'s decision (16 October 2026).** Answering the report that P121 and P122 had landed, Ren wrote '
         f'“alright, agree” ([source]({SRC_ST})), read by the AI as taking these readings in its wording.\n'
         '- **Readings (the AI\'s, agreed by Ren).** The structural match is now exact:')
t = once(t, '- **Readings (the AI\'s, pending Ren).** Loops form within the unfolding by closing,',
         '- **Ren\'s decision (16 October 2026).** The same “alright, agree” takes these readings and P118\'s third '
         f'reading as revised: {THIRD_EN}. Joining loop formation with `Becoming.Runaway`\'s policies is not taken as '
         'begun; P120\'s readings are not covered.\n'
         '- **Readings (the AI\'s, agreed by Ren).** Loops form within the unfolding by closing,')
out[STUDY] = t

# records
sha = hashlib.sha256((W / SOURCE).read_bytes()).hexdigest()


def record(ident):
    return json.loads((REC / f'{ident}.json').read_text())


def provenance(r):
    assert all(x['path'] != SOURCE for x in r['references'])
    r['references'].append({'path': SOURCE, 'role': 'provenance', 'sha256': sha})


def replace(field, zh, en):
    for lang, (old, new) in (('zh', zh), ('en', en)):
        assert field[lang].count(old) == 1, (lang, old)
        field[lang] = field[lang].replace(old, new)


NOTE_ZH = f'2026-10-16：Ren 答 P121 与 P122 落地的报告：“alright, agree”（来源 {SOURCE}）。'
NOTE_EN = f'16 October 2026: answering the report that P121 and P122 had landed, Ren wrote “alright, agree” (source {SOURCE}). '
KEEP_ZH, KEEP_EN = '陈述与证明不变。', 'Statement and proofs unchanged.'

recs = []
for ident in ('orders-as-a-sum-over-histories', 'how-loops-form'):
    r = record(ident)
    replace(r['correspondence'], ('读法（AI 的，待 Ren）：', '读法（AI 的，Ren 2026-10-16 同意）：'),
            ("Readings (the AI's, pending Ren):", "Readings (the AI's, agreed by Ren on 16 October 2026):"))
    provenance(r)
    r['history'].append({'zh': NOTE_ZH + 'AI 读为 Ren 取本记录的读法，用 AI 的措辞；correspondence 注明，references 加来源。' + KEEP_ZH,
                         'en': NOTE_EN + "The AI reads it as Ren taking this record's readings in the AI's wording; "
                         'correspondence says so and references add the source. ' + KEEP_EN})
    recs.append(r)

r = record('how-a-carried-difference-grows')
replace(r['correspondence'], ('第三项读法待 Ren 再议。）', f'Ren 2026-10-16 同意第三项读法修订为：{THIRD_ZH}。）'),
        ("the third reading awaits Ren's revision.)", f'Ren agreed on 16 October to the third reading as revised: {THIRD_EN}.)'))
provenance(r)
r['history'].append({'zh': NOTE_ZH + 'AI 读为 Ren 取第三项读法的修订形式（回路由闭合而形成，在耦合停止处消解，强度从进程读出时形成从展开读出）；'
                     'correspondence 中“待 Ren 再议”改为所取的形式，Ren 此前的读法照原样保留；references 加来源。' + KEEP_ZH,
                     'en': NOTE_EN + "The AI reads it as Ren taking the third reading as revised (loops form by closing, "
                     'dissolve where their couplings stop, and with strengths read off the course their formation is '
                     "read off the unfolding); in correspondence “awaits Ren's revision” becomes the form taken, Ren's "
                     'earlier readings kept as recorded; references add the source. ' + KEEP_EN})
recs.append(r)
for r in recs:
    out[REC / f'{r["id"]}.json'] = json.dumps(r, ensure_ascii=False, indent=2) + '\n'

for path, text in out.items():
    path.write_text(text)
print('updated', len(out), 'files')
