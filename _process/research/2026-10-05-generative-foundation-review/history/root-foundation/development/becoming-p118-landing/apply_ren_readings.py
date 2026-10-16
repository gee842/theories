#!/usr/bin/env python3
"""P118: Ren's decisions of 16 October 2026 on the three readings of Becoming.Loops.

usage: python3 -B apply_ren_readings.py W

Source: sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md. Ren
took the first reading in the AI's wording, called the second right with its qualifiers, and took the
third in a refined form for now, open to revision once a loop-formation theorem exists.

Changes: the readings in Loops.lean's module docstring (comments only); the readings in the chapter's
§2 paragraph "How a carried difference grows" (zh and en); a dated paragraph after the readings of
study §152 and a bullet in its English paragraph; in how-a-carried-difference-grows, the readings in
correspondence, next_delta, the source as a provenance reference, and one paired history note.
Statements and proofs are unchanged. Hashes of changed sources are reconciled at landing. Each change
asserts the text it replaces, so a second run fails.
"""
import hashlib
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
SOURCE = 'sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md'
LOOPS = W / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Loops.lean'
CHAPTER = W / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
STUDY = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
RECORD = W / 'theories/becoming/results/records/how-a-carried-difference-grows.json'
QUOTE = ('there are so many patterns and loops but we can still find a way to to integrate so we can still '
         'calculate this effects but how how accurate can we do that uh what is the limitation do we have losses')
out = {}


def once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)


def between(text, start, end):
    """The text from start up to (not including) end, both occurring once."""
    assert text.count(start) == 1, (start[:80], text.count(start))
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


# Loops.lean: the readings of the module docstring
t = LOOPS.read_text()
old = between(t, "**Readings (the AI's, pending Ren).**", 'What is not derived:')
new = (
    "**Readings (decided by Ren on 16 October 2026).** Ren took the first in the AI's wording, called the\n"
    "second right with its qualifiers, and took the third in a refined form, for now.\n"
    "- On 12 October Ren compared the theory with quantum dynamics and \"Fermi's diagrams\": \"there are so\n"
    "  many patterns and loops but we can still find a way to to integrate so we can still calculate\n"
    "  this effects but how how accurate can we do that uh what is the limitation do we have losses\".\n"
    "  Ren meant Feynman diagrams, and the match is structural, not physical. The integration Ren asked\n"
    "  about, for laws that are not determined, is the sum over histories with its four losses\n"
    "  (`Becoming.Weighted`). The orders here are the same structural kind, organized by the number of\n"
    "  responses as Feynman diagrams are by their vertices, `Loops.binom t i` counting the time\n"
    "  orderings of `i` responses. The two are not yet joined. A cut at order `j` misses at most the\n"
    "  rest of the sum, and this is attained: it is the limit of accuracy for what the strengths and the\n"
    "  starting gaps alone allow. Where no loop lies upstream there is no loss at a finite order. Where a\n"
    "  loop lies upstream, coupled at every step, every finite order loses something, and what reaches\n"
    "  the loop grows at least geometrically.\n"
    "- Only a loop makes a difference run away. Running away means growing faster than every\n"
    "  polynomial, and it is of the most difference that can arrive, not of what every law does.\n"
    "  Without a loop a held difference keeps arriving but grows at most polynomially\n"
    "  (`Propagation.Chain` is of degree one); with a loop that couples at every step it grows at least\n"
    "  geometrically (`Propagation.Loop` is the self-loop of strength one). So the most difference that\n"
    "  can arrive grows faster than every polynomial only through a loop, and through every loop that\n"
    "  couples at every step; couplings that hold only at some steps are open here.\n"
    "- Which loops a world has is part of its situation (Ren, 16 October: \"the situation makes it\n"
    "  true\"): loops form and dissolve within the unfolding, and the theorems take them as they stand\n"
    "  at each step. The strengths are supplied, as in `Becoming.Propagation`. This reading is taken for\n"
    "  now, open to revision once a theorem states how loops form within the unfolding, for example\n"
    "  where a formation's drawing comes to respond to the level its drawing lowers, where this meets\n"
    "  `Becoming.Runaway`.\n\n")
out[LOOPS] = t.replace(old, new)

# the chapter's §2 paragraph, zh and en
SRC_CH = f'../../../{SOURCE}'
t = CHAPTER.read_text()
old = between(t, '读法（AI 的，待 Ren）：Ren 2026-10-12 把理论比作量子动力学', '强度本身、时有时无的耦合')
new = (
    f'读法（Ren 2026-10-16 决定，[来源]({SRC_CH})）：Ren 2026-10-12 把理论比作量子动力学与“Fermi\'s diagrams”，说“{QUOTE}”'
    '（[来源](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)）；Ren 指的是费曼图，相合是结构上的，'
    '不是物理上的。Ren 所问的积分，对不确定的律，是 `Becoming.Weighted` 的历史之和及其四种损失；这里的各阶是同一结构的另一种，按回应'
    '次数组织，如费曼图按顶点数组织，`Loops.binom` 数回应的时间次序；两者尚未连起来。截断的精度是剩下的和，并且恰好达到，是只由强度与'
    '起始之差所能有的极限；上游没有回路处有限阶没有损失，有回路且耦合每步成立处每个有限阶都有损失，到达回路者至少按几何级数增长。只有'
    '回路使差别失控：失控是快于每个多项式，说的是能到达的最大差别，不是每个律所做的；没有回路时所持的差别不断到达，至多按多项式增长'
    '（`Propagation.Chain` 是一次的），有每步耦合的回路时至少按几何级数增长（`Propagation.Loop` 是强度为一的自环）；所以能到达的最大'
    '差别快于每个多项式，只经由回路，且经由每个每步耦合的回路；只在某些步成立的耦合在这里开放。一个世界有哪些回路是其情境的一部分'
    '（Ren 2026-10-16：“the situation makes it true”）：回路在展开之中形成与消散，定理按每步的样子取用它们；强度是给出的。这一读法暂取'
    '此形式，待有定理陈述回路怎样在展开中形成时可修订，例如一个形成的汲取开始回应其汲取所降低的水平，那里与 `Becoming.Runaway` 相遇。')
t = t.replace(old, new)
old = between(t, "On the AI's reading, pending Ren: on 12 October Ren compared the theory",
              'The strengths themselves, couplings that come and go')
new = (
    f'Readings, as Ren decided them on 16 October ([source]({SRC_CH})): on 12 October Ren compared the theory with '
    f'quantum dynamics and "Fermi\'s diagrams": “{QUOTE}” '
    '([source](../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)); Ren meant Feynman diagrams, '
    'and the match is structural, not physical. The integration Ren asked about, for laws that are not determined, is '
    'the sum over histories of `Becoming.Weighted` with its four losses; the orders here are the same structural kind, '
    'organized by the number of responses as Feynman diagrams are by their vertices, `Loops.binom` counting their time '
    'orderings; the two are not yet joined. The accuracy of a cut is the rest of the sum, and it is attained, the limit '
    'for what the strengths and the starting gaps alone allow; where no loop lies upstream a finite order loses nothing, '
    'and where one does, coupled at every step, every finite order loses something and what reaches the loop grows at '
    'least geometrically. Only a loop makes a difference run away, where running away means growing faster than every '
    'polynomial, and of the most difference that can arrive, not of what every law does: without a loop a held '
    'difference keeps arriving but grows at most polynomially (`Propagation.Chain` is of degree one), and with a loop '
    'that couples at every step it grows at least geometrically (`Propagation.Loop` is the self-loop of strength one); '
    'so the most difference that can arrive grows faster than every polynomial only through a loop, and through every '
    'loop that couples at every step, couplings that hold only at some steps being open here. Which loops a world has '
    'is part of its situation (Ren, 16 October: “the situation makes it true”): loops form and dissolve within the '
    'unfolding, and the theorems take them as they stand at each step; the strengths are supplied. This reading is '
    'taken for now, open to revision once a theorem states how loops form within the unfolding, for example where a '
    'formation\'s drawing comes to respond to the level its drawing lowers, where this meets `Becoming.Runaway`. ')
t = t.replace(old, new)
out[CHAPTER] = t

# study §152: a dated paragraph after the readings, and a bullet in the English paragraph
SRC_ST = f'../../../../{SOURCE}'
t = STUDY.read_text()
section = between(t, '\n## 152. 所携带的差别怎样增长', '\n## 153.' if '\n## 153.' in t else '\n## English summary')
assert section.count('\n**作者反审。**') == 1
decided_zh = (
    f'**Ren 的决定（2026-10-16）。** Ren 决定了上面三条读法（[来源]({SRC_ST})）。一、取 AI 的措辞：Ren 指的是费曼图，相合是结构上'
    '的，不是物理上的；Ren 所问的积分，对不确定的律，是 P82 的历史之和及其四种损失（`Becoming.Weighted`）；P118 的各阶是同一结构的'
    '另一种，按回应次数组织，如费曼图按顶点数组织；两者尚未连起来，连起来是进一步的证明。二、“只有回路使差别失控”是对的，附限定：失控是'
    '快于每个多项式；说的是能到达的最大差别，不是每个律所做的；只在某些步成立的耦合开放。一句话：能到达的最大差别快于每个多项式，只经由'
    '回路，且经由每个每步耦合的回路。三、取精炼的形式：一个世界有哪些回路是其情境的一部分；回路在展开之中形成与消散，定理按每步的样子取'
    '用它们。Ren 说“leave it pending until a loop-formation theorem exists”：这一读法暂取此形式，待有回路形成之定理时可修订（候选：'
    '一个形成的汲取开始回应其汲取所降低的水平，那里与 `Becoming.Runaway` 相遇）。记录、第 2 节的段落与模块说明已相应修改。\n')
new_section = section.replace('\n**作者反审。**', '\n' + decided_zh + '\n**作者反审。**')
t = t.replace(section, new_section)
bullet = between(t, "- **Readings (the AI's, pending Ren).** The orders are the integration Ren asked about",
                 '\n- **Boundaries.**')
t = t.replace(bullet, bullet + (
    f"\n- **Ren's decisions (16 October).** Ren decided the three readings ([source]({SRC_ST})). The first is taken in "
    "the AI's wording: Ren meant Feynman diagrams, the match structural, not physical; the integration Ren asked "
    "about, for laws that are not determined, is P82's sum over histories with its four losses, and P118's orders are "
    "the same structural kind, organized by number of responses as Feynman diagrams are by vertices; the two are not "
    "yet joined, which is a further proof. The second is right with its qualifiers: running away means faster than "
    "every polynomial, of the most difference that can arrive, not of every law, and couplings that hold only at some "
    "steps are open; in one sentence, the most difference that can arrive grows faster than every polynomial only "
    "through a loop, and through every loop that couples at every step. The third is taken in a refined form for now: "
    "which loops a world has is part of its situation, loops forming and dissolving within the unfolding and the "
    "theorems taking them as they stand at each step, open to revision once a loop-formation theorem exists (Ren: "
    "“leave it pending until a loop-formation theorem exists”)."))
out[STUDY] = t

# the record
r = json.loads(RECORD.read_text())
c = r['correspondence']
old_zh = between(c['zh'], '读法（AI 的，待 Ren）：', '数学是标准的')
c['zh'] = c['zh'].replace(old_zh, (
    '读法（Ren 2026-10-16 决定）：Ren 指的是费曼图，相合是结构上的，不是物理上的；Ren 所问的积分，对不确定的律，是历史之和及其四种损失'
    '（P82，losses-of-the-sum-over-histories），这里的各阶是同一结构的另一种，按回应次数组织，如费曼图按顶点数，两者尚未连起来；只有'
    '回路使差别失控，失控是快于每个多项式，说的是能到达的最大差别：只经由回路，且经由每个每步耦合的回路，只在某些步成立的耦合开放；一个'
    '世界有哪些回路是其情境的一部分（Ren 2026-10-16：“the situation makes it true”），回路在展开之中形成与消散，定理按每步的样子取用'
    '它们，暂取此形式，待有回路形成之定理时可修订。'))
old_en = between(c['en'], "Readings (the AI's, pending Ren):", 'The mathematics is standard')
c['en'] = c['en'].replace(old_en, (
    'Readings, decided by Ren on 16 October: Ren meant Feynman diagrams, the match structural, not physical; the '
    'integration Ren asked about, for laws that are not determined, is the sum over histories with its four losses (P82, '
    'losses-of-the-sum-over-histories), and the orders here are the same structural kind, organized by number of '
    'responses as Feynman diagrams are by vertices, the two not yet joined; only a loop makes a difference run away, '
    'running away meaning faster than every polynomial, of the most difference that can arrive: only through a loop, and '
    'through every loop that couples at every step, couplings at only some steps being open; which loops a world has is '
    'part of its situation (Ren, 16 October: “the situation makes it true”), loops forming and dissolving within the '
    'unfolding and the theorems taking them as they stand at each step, taken for now and open to revision once a '
    'loop-formation theorem exists. '))
d = r['next_delta']
d['zh'] = once(d['zh'], '与 Becoming.Runaway 的策略相连；独立审查；Ren 对读法的判断。',
               '回路怎样在展开中形成（汲取与 Becoming.Runaway 的策略相遇处）；把各阶与历史之和连起来；独立审查。')
d['en'] = once(d['en'], "the link to Becoming.Runaway's policies; an independent review; Ren's judgment on the readings.",
               "how loops form, where a draw meets Becoming.Runaway's policies; joining the orders to the sum over "
               'histories; an independent review.')
assert all(x['path'] != SOURCE for x in r['references'])
r['references'].append({'path': SOURCE, 'role': 'provenance',
                        'sha256': hashlib.sha256((W / SOURCE).read_bytes()).hexdigest()})
r['history'].append({
    'zh': ('2026-10-16：Ren 决定三条读法（来源 ' + SOURCE + '）。一、取 AI 的措辞：Ren 指的是费曼图，相合是结构上的；Ren 所问的积分对不'
           '确定的律是历史之和及其四种损失，这里的各阶是同一结构的另一种，两者尚未连起来。二、“只有回路使差别失控”是对的，附限定：失控是快于'
           '每个多项式，说的是能到达的最大差别，只在某些步成立的耦合开放。三、取精炼的形式：一个世界有哪些回路是其情境的一部分，回路在展开中'
           '形成与消散，待有回路形成之定理时可修订。correspondence 改为所决定的读法；next_delta 去掉“Ren 对读法的判断”，“与 '
           'Becoming.Runaway 的策略相连”并入回路怎样在展开中形成，加把各阶与历史之和连起来；references 加来源；Loops.lean 的模块说明、'
           '理论第 2 节的段落与研究 §152 相应修改（只改说明与读法）。陈述与证明不变。'),
    'en': ('16 October 2026: Ren decided the three readings (source ' + SOURCE + '). (1) Taken in the AI\'s wording: Ren '
           'meant Feynman diagrams, the match structural; the integration Ren asked about, for laws that are not '
           'determined, is the sum over histories with its four losses, and the orders are the same structural kind, the '
           'two not yet joined. (2) “Only a loop makes a difference run away” is right, with the qualifiers that running '
           'away means faster than every polynomial, that it is of the most difference that can arrive, and that couplings '
           'at only some steps are open. (3) Taken in a refined form: which loops a world has is part of its situation, '
           'loops forming and dissolving within the unfolding, open to revision once a loop-formation theorem exists. '
           'correspondence states the decided readings; next_delta drops Ren\'s judgment on the readings, folds the link '
           'to Becoming.Runaway\'s policies into how loops form, and adds joining the orders to the '
           'sum over histories; references add the source; Loops.lean\'s module docstring, the chapter\'s §2 paragraph '
           'and study section 152 change accordingly (comments and readings only). Statement and proofs unchanged.')})
out[RECORD] = json.dumps(r, ensure_ascii=False, indent=2) + '\n'

for path, text in out.items():
    path.write_text(text)
print('applied Ren\'s readings to', len(out), 'files')
