#!/usr/bin/env python3
"""Re-point RO's passage map and chapter to RG's laws (board item RG; run from anywhere, after apply_text.py):
  python3 -B ro_points.py
For the four passages of RO's first gap (老子 77 天之道, 老子 42 冲气以为和, 左传 昭公二十年 宽猛, 中庸 中和): adds FIXES
entries to build_passages.py, each with its reason: the declarations of Becoming.Regulation and the record
two-sided-regulation-and-late-reading (`declarations_add`, `records_add`), the sentences of each reading that named the
gap replaced with what the laws now say (`reading_sub`, `reading_en_sub`; 中和 gains a sentence), and the gap marked
closed where the passage has one (`gap_closed`, its statement kept). passages.json changes only through FIXES: the
entries go before FIXES' closing brace, after whatever other items left, and build_passages.py is rerun. Then rewrites
the chapter's passage tables for the traditions touched (verify_ro.py --table), marks the gap's row in §8 closed (in its
"what is missing" cell, as Y5 and SC mark theirs), adds a paragraph after the table, and rewrites the §11 line of open
gaps from the gaps marked closed in it, whichever items closed them. Each edit must match exactly once. Run before
make_record.py; reland.sh runs verify_ro.py after the record exists."""
import json
import pprint
import re
import subprocess
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
RO = HERE.parent / 'ro-relational-sources'
ROOT = HERE.parents[5]
PASSAGES = RO / 'passages.json'
BUILD = RO / 'build_passages.py'
CHAPTER = ROOT / 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
RID = 'two-sided-regulation-and-late-reading'
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
sys.path.insert(0, str(RO))
import verify_ro as V  # noqa: E402

section = re.search(r'^## (\d+)\. A level held from both sides, and a level read late \(RG\)$', STUDY.read_text(), re.M)
assert section, 'study section missing'
N = int(section.group(1))


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


TWO_SIDED = ('RG (Becoming.Regulation, record two-sided-regulation-and-late-reading), as stated for one condition, with the bound '
             'read as no overshoot: the exchange is within the gap to m on both sides exactly where the next level lies '
             'between m and the level (Flow.withinGap_iff_between); with it and opposing on both sides the level is m '
             'from T plus its gap at T on (Flow.regulates, Flow.settles); (iii) is not needed, since at m the bound '
             'itself keeps the level at m (Flow.withinGap_iff_of_at). Both failures are exact: beyond the bound an '
             'opposing exchange crosses m and a witness alternates without end (Flow.crosses_of_above, '
             'Regulation.Overshooting.oscillates); with one side only the premise of Flow.restores holds and the level '
             'stays above m (Regulation.OneSided.above).')
LATE = ('RG (Becoming.Regulation, record two-sided-regulation-and-late-reading), in part. (iii) proved exactly: a start held at '
        'a - 1 for the first l + 1 steps leaves both ends without end where b + 2 <= a + (l + 1) M '
        '(Regulation.held_oscillates), every start held below a settles in the band where a + (l + 1) M <= b + 1 '
        '(Regulation.held_below_settles), and with the relay\'s runs (Regulation.relay_runs, where (l + 1) M <= b + 1) '
        'the threshold is exact (Regulation.relay_threshold). (i) proved for one start, the rule chosen with it: no '
        'rule reading l late keeps a band narrower than 2 (l + 1) d under every rest within d a step '
        '(Regulation.no_narrower_band), and the late return keeps that band (Regulation.lateReturn_band); one policy '
        'keeping [a, b] from every start in it is not proved. (ii) is not proved.')

R = 'Becoming.Regulation.'
F = 'Becoming.Flow.'
EDITS = {
    'lao-77-tian-zhi-dao': dict(
        declarations=[F + 'withinGap_iff_between', F + 'regulates', F + 'settles', F + 'restores_exactly',
                      F + 'crosses_of_above', R + 'Overshooting.oscillates', R + 'OneSided.above'],
        zh=[('双向调节的确切定律（含两种失败：单侧、矫枉过正而振荡）是缺口。',
             '双向调节的确切定律已证（`Becoming.Regulation`）：平衡下，合取的交换在两侧都以与 m 的距离为界，'
             '恰是下一水平落在 m 与当前水平之间（`Flow.withinGap_iff_between`）；有界且两侧都与偏离相反时，'
             '距离为正则每步至少降一，距离用尽时水平定于 m（`Flow.regulates`、`Flow.settles`）。两种失败也是确切的：'
             '越界的相反交换越过 m（`Flow.crosses_of_above`），其证人在 m 两侧往复而永不到 m'
             '（`Overshooting.oscillates`）；只有一侧时，恢复律的前提成立而水平永在 m 之上（`OneSided.above`）。')],
        en=[('it is the property of a regulating coupling, and the two-sided law with its failure modes is a gap.',
             'it is the property of a regulating coupling. That law is proved (Becoming.Regulation): bounded by the gap '
             'on both sides and opposing, the level settles at m within its gap; beyond the bound it crosses m and can '
             'alternate without end; one side alone can leave it away for ever.')],
        gap=TWO_SIDED),
    'lao-42-chong-qi-yi-wei-he': dict(
        declarations=[F + 'withinGap_iff_between', F + 'settles', F + 'stays_between_at', R + 'Overshooting.never_at'],
        zh=[('脊柱目前只有单向的部分：', '脊柱有单向的部分：'),
            ('双向调节（高者抑、低者举）与其失败方式（单向、矫枉过正）没有被证明的定律，见缺口。',
             '双向调节（高者抑、低者举）与其失败方式已证（`Becoming.Regulation`，见第七十七章条）：两种相反作用'
             '各以与 m 的距离为界时，水平在界内永不越过 m（`Flow.stays_between_at`），与偏离相反时定于 m'
             '（`Flow.settles`）；越界则越过，可以永不到 m（`Overshooting.never_at`）。所以“和”在此读作受两侧有界的'
             '相反作用所保持的水平，是一种耦合的性质。')],
        en=[("'harmony' has only one-sided counterparts on the spine (restoration from below, excess lowering, difference "
             "closing on a loop); the two-sided regulating law is a gap, stated under lao-77-tian-zhi-dao.",
             "'harmony' is the level two-sided regulation keeps (Becoming.Regulation, under lao-77-tian-zhi-dao): "
             "bounded by the gap on both sides the level never crosses m, and opposing it settles there; beyond the "
             "bound it crosses and can miss m for ever. The one-sided counterparts (restoration from below, excess "
             "lowering, difference closing on a loop) are its parts.")],
        gap=TWO_SIDED),
    'zuo-zhao20-kuan-meng': dict(
        declarations=[R + 'late_spread', R + 'no_narrower_band', R + 'lateReturn_band', R + 'overshoot',
                      R + 'crossing_oscillates', R + 'held_oscillates', R + 'held_below_settles', R + 'relay_threshold'],
        zh=[('范围与分歧：这是两档玩具模型、即时响应；“政宽则民慢，慢则纠之以猛，猛则民残”描述的是迟到的读法造成两端越界的往复，'
             '模型没有覆盖（见缺口）。',
             '范围与分歧：这是两档玩具模型、即时响应。“政宽则民慢，慢则纠之以猛，猛则民残”所述的往复，是迟到读法的越界，'
             '已证（`Becoming.Regulation`）：迟 ℓ 步读的规则分不出其后 ℓ + 1 步内不同的扰动，所以扰动每步至多 d 时，'
             '任何这样的规则所保之带都不窄于 2(ℓ + 1)d（`late_spread`、`no_narrower_band`），而迟返恰保此带'
             '（`lateReturn_band`）。以步长 M 迟读的阈值调节越过入带处 ℓM（`overshoot`），一旦越过便两端越出而无尽'
             '（`crossing_oscillates`）；带下的起点恰在 a + (ℓ + 1)M ≤ b + 1 时都定于带内（`held_below_settles`、'
             '`relay_threshold`），过此阈值则贴近 a 的起点两端往复（`held_oscillates`）。')],
        en=[("the passage's overshoot from a late reading (宽→慢→猛→残) is beyond the model, and its frame governs the "
             "people as a regulated stock.",
             "the passage's overshoot from a late reading (宽→慢→猛→残) is proved beyond the model (Becoming.Regulation): "
             "no rule reading ℓ steps late keeps a band narrower than 2(ℓ + 1)d, and a relay reading late leaves both "
             "ends without end exactly past a threshold set by lateness times step. Its frame governs the people as a "
             "regulated stock.")],
        gap=LATE),
    'ru-zhongyong-zhi-zhong-he': dict(
        declarations=[F + 'withinGap_iff_between', F + 'settles', F + 'crosses_of_above'],
        zh_add=('“发而皆中节”的“节”也可读为（AI 读法）回应以距离为界：与偏离相反的回应在两侧都不超过它与 m 的距离，'
                '恰是下一水平落在 m 与当前水平之间（`Flow.withinGap_iff_between`），这时水平在距离用尽时定于 m'
                '（`Flow.settles`）；不中节的回应越过 m（`Flow.crosses_of_above`）。这是一种耦合的性质，不涉及天地之位。'),
        en_add=(' 发而皆中节 can also be read (AI) as a response within the gap: opposing, it stays within the level\'s '
                'distance to m on both sides exactly where the next level lies between m and the present one, and the '
                'level then settles at m (Flow.withinGap_iff_between, Flow.settles); a response beyond it crosses m.')),
}

WHY = {
    'lao-77-tian-zhi-dao': 'RG proved the two-sided law the reading named as a gap, with both of its failures',
    'lao-42-chong-qi-yi-wei-he': 'RG proved the two-sided law the reading named as a gap (stated under lao-77-tian-zhi-dao)',
    'zuo-zhao20-kuan-meng': "RG proved the late reading's overshoot the reading placed beyond the model, with the least "
                            "band a late rule needs and the relay's exact threshold",
    'ru-zhongyong-zhi-zhong-he': 'RG: 中节 read as a response within the gap, the bound two-sided regulation proves exact',
}
# 中和 gains a sentence: its reading's last clause is replaced by itself and the sentence.
TAIL_ZH, TAIL_EN = '（见程颢“一体”条）。', 'not as such.'

old_map = {p['id']: p for p in json.loads(PASSAGES.read_text())['passages']}
build = BUILD.read_text()
assert 'reading_en_sub' in build, 'build_passages.py has no reading_en_sub key yet (SC adds it; land after SC)'
start = build.index('\nFIXES = {\n')
close = build.index('\n}\n', start)
for pid in EDITS:
    assert f"\n    '{pid}': {{" not in build[start:close], f'{pid} has a FIXES entry: merge the keys into it'
    assert not any(d.startswith(R) for d in old_map[pid]['declarations']), pid
entries = {}
for pid, e in EDITS.items():
    zh, en = list(e.get('zh', [])), list(e.get('en', []))
    if e.get('zh_add'):
        assert old_map[pid]['reading'].count(TAIL_ZH) == 1 and old_map[pid]['reading_en'].count(TAIL_EN) == 1, pid
        zh.append((TAIL_ZH, TAIL_ZH + e['zh_add']))
        en.append((TAIL_EN, TAIL_EN + e['en_add']))
    for old, _ in zh:
        assert old_map[pid]['reading'].count(old) == 1, (pid, old)
    for old, _ in en:
        assert old_map[pid]['reading_en'].count(old) == 1, (pid, old)
    fix = {'declarations_add': [d for d in e['declarations'] if d not in old_map[pid]['declarations']],
           'records_add': [RID], 'reading_sub': zh, 'reading_en_sub': en}
    if e.get('gap'):
        assert old_map[pid].get('gap') and 'closed' not in old_map[pid]['gap'], pid
        fix['gap_closed'] = e['gap']
    fix['why'] = WHY[pid]
    entries[pid] = fix


def entry_source(pid, fix):
    """One FIXES entry in the file's layout: the id on its own line, each key on its own line."""
    out = [f'    {pid!r}: {{']
    for n, (key, value) in enumerate(fix.items()):
        lead = 8 + len(repr(key)) + 2
        body = textwrap.indent(pprint.pformat(value, width=118 - lead, sort_dicts=False), ' ' * lead)[lead:]
        out.append(f'        {key!r}: {body}' + ('},' if n == len(fix) - 1 else ','))
    return '\n'.join(out) + '\n'


block = ''.join(entry_source(pid, fix) for pid, fix in entries.items())
build = build[:close] + '\n' + block.rstrip('\n') + build[close:]
compile(build, str(BUILD), 'exec')
BUILD.write_text(build)
run = subprocess.run([sys.executable, '-B', str(BUILD)], cwd=RO, capture_output=True, text=True)
assert run.returncode == 0, run.stdout[-3000:] + run.stderr[-3000:]
data = json.loads(PASSAGES.read_text())
touched = set()
for p in data['passages']:
    e = EDITS.get(p['id'])
    if not e:
        continue
    assert RID in p['records'] and all(d in p['declarations'] for d in e['declarations']), p['id']
    assert ('closed' in p.get('gap', {})) == bool(e.get('gap')), p['id']
    touched.add(p['tradition'])
assert len([p for p in data['passages'] if p['id'] in EDITS]) == len(EDITS)
before = {k: v for k, v in old_map.items() if k not in EDITS}
after = {p['id']: p for p in data['passages'] if p['id'] not in EDITS}
assert before == after, 'the rebuild changed passages RG does not touch: ' + ', '.join(
    sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k)))[:500]

chapter = CHAPTER.read_text()
for t in sorted(touched):
    b, e = V.begin(t), V.end(t)
    i, j = chapter.index(b) + len(b), chapter.index(e)
    chapter = chapter[:i] + '\n' + V.table(data['passages'], t) + '\n' + chapter[j:]
MODULE = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Regulation.lean'
# §8: the row's passages cell links 中和, and its "what is missing" cell says the gap is closed, as Y5 and SC mark theirs.
chapter = once(chapter, '[宽猛相济](#p-zuo-zhao20-kuan-meng)；儒家中和 | `Flow.restores` 只是单向的，`AssurancePlans.Regulation` '
                        '只是两档、即时响应 |',
               '[宽猛相济](#p-zuo-zhao20-kuan-meng)；儒家[中和](#p-ru-zhongyong-zhi-zhong-he) | 已由 RG 补上'
               f'（[`Becoming.Regulation`]({MODULE})，记录 [{RID}](../results/records/{RID}.md)）；此前 `Flow.restores` '
               '只是单向的，`AssurancePlans.Regulation` 只是两档、即时响应 |')
# §11: the line of open gaps, rebuilt from the gaps it marks closed (RO's form, or as Y5, SC or another item left it).
NUMS = '一二三四五六七'
lines = [l for l in chapter.split('\n') if l.startswith('- §8 的')]
assert len(lines) == 1, lines
line = lines[0]
marks = re.findall(r'第([一二三四五六七])项（([^）]+)）已由 (\S+?) 写成', line)
assert line.count('已由') == len(marks), ('§11 line has a closed gap in an unknown form', line)
done = {n: (name, by) for n, name, by in marks}
assert '一' not in done
done['一'] = ('一个水平的双向调节', 'RG')
still = [n for n in NUMS if n not in done]
assert still, 'every gap closed'
new = (f'- §8 的第{"、".join(still)}项缺口，各待写成 Lean（已认领者见工作板）；'
       + '，'.join(f'第{n}项（{done[n][0]}）已由 {done[n][1]} 写成' for n in NUMS if n in done) + '。')
chapter = once(chapter, line, new)
# The paragraph after the table: first among the paragraphs closed gaps add there (before SC's, where it is).
PARA = (f'第一项已由看板项 RG 补上（`Becoming.Regulation`，记录 [{RID}](../results/records/{RID}.md)，研究第 {N} 节）。'
        '所拟陈述都成立，其中几点更确切：界恰是不越过（`Flow.withinGap_iff_between`），不是另加的条件；在 m 时保持一条不需要另设，'
        '界本身使水平留在 m（`Flow.withinGap_iff_of_at`）；无界则越过 m，其证人往复而永不到 m（`Overshooting.oscillates`），'
        '只有一侧时水平可永在 m 之上（`OneSided.above`）。迟读之下，最小带宽恰是 2(ℓ + 1)d：任何迟 ℓ 步读的规则都不能更窄'
        '（`no_narrower_band`），迟返恰保此带（`lateReturn_band`）；阈值调节越过入带处 ℓM（`overshoot`），带下保持的每个起点'
        '恰在 a + (ℓ + 1)M ≤ b + 1 时定于带内，否则贴近 a 的起点两端越出而无尽（`relay_threshold`、`held_oscillates`）。'
        '未证的是[宽猛](#p-zuo-zhao20-kuan-meng)条目缺口中的两点：对带中每个起点都保带的单一策略，以及把几个受调节的水平'
        '读作一个的归并。四段的读法已改指向这些律。')
TABLE_END = '\n\n另有两项已在映射期间由别处完成，或交给别处：'
SC_PARA = '\n\n第二项已由看板项 SC 补上'
anchor = SC_PARA if chapter.count(SC_PARA) == 1 else TABLE_END
chapter = once(chapter, anchor, '\n\n' + PARA + anchor)
CHAPTER.write_text(chapter)

print('patched', len(EDITS), 'passages;', ', '.join(sorted(touched)), '| §11:', new)
