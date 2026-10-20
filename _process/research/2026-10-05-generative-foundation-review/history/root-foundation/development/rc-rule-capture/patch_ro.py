#!/usr/bin/env python3
"""Re-point RO's passage map, chapter and record to RC's laws (board item RC; from the checkout root, after
apply_text.py and before make_record.py, whose record binds the chapter and the map as patched):
  python3 -B patch_ro.py SECTION DECISION BASE
For the three passages of RO's third gap (二柄, 据有余而制不足, 壹赏壹刑壹教): the passage map changes only through
build_passages.py's FIXES, which a rebuild would otherwise overwrite. So this adds one FIXES entry per passage
(declarations of Becoming.RuleCapture and the record capture-through-the-rule added, a sentence of each reading replaced
or extended in both languages, 二柄's gap marked closed with its statement kept), rebuilds passages.json and checks that
only these three passages changed. Then it rewrites the chapter's table of 兵家、法家与轻重纵横 (verify_ro.py's table),
marks the gap's row in §8 closed (in its "what is missing" cell, as SC and Y5 mark theirs), adds a paragraph after the
§8 table, corrects §5.7 (which said the spine lacks the loop) and §11 (the open gaps), and brings RO's record to the map
(counts, the next step without this gap, the record related, references that matched at BASE re-pointed, history).
Each edit must match exactly once; a line in an unknown form stops the script."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RO = HERE.parent / 'ro-relational-sources'
ROOT = HERE.parents[5]
PASSAGES = RO / 'passages.json'
BUILD = RO / 'build_passages.py'
CHAPTER = ROOT / 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
RO_RECORD = ROOT / 'theories/becoming/results/records/chinese-sources-on-the-spine.json'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/RuleCapture.lean'
RID = 'capture-through-the-rule'
TRADITION = '兵家、法家与轻重纵横'
N, D, BASE = sys.argv[1], sys.argv[2], sys.argv[3]
STUDY_LINK = f'../../../{RF}/BECOMING-RENEWAL-READING.md#{N}-capture-through-the-rule-rc'
sys.path.insert(0, str(RO))
import verify_ro as V  # noqa: E402

assert re.search(rf'^## {N}\. Capture through the rule \(RC\)$', (ROOT / RF / 'BECOMING-RENEWAL-READING.md').read_text(),
                 re.M), 'study section missing'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


def rc(*names):
    return ['Becoming.RuleCapture.' + n for n in names]


EDITS = {
    'hanfei-er-bing': dict(
        declarations=rc('locked_stays', 'favouring_locks', 'perturbation_absorbed', 'uniform_locks'),
        zh=('脊柱分别有这两部分，没有证明它们闭合成回路（见 gap）。',
            '回路的闭合由 RuleCapture 证明：规则从所选出者的份额单调地读出时，锁定之后回路不回转（locked_stays），没有规则反对读法时在第一个'
            '读取步锁定（favouring_locks），保持方向的规则扰动在下一读取步被吸收（perturbation_absorbed），只有改变规则怎样读才离开'
            '（uniform_locks）。'),
        en=('whose parts the spine has (Pace.rule_at_reading, Capture) but whose closure it does not prove.',
            'whose closure RuleCapture proves: with the rule read monotonically from the share it selects, the loop locks '
            '(locked_stays; at the first reading step where no rule turns against the reading, favouring_locks), a '
            'perturbation of the rule that keeps its direction is absorbed at the next reading step '
            '(perturbation_absorbed), and only a change of how the rule reads leaves (uniform_locks).')),
    'guanzi-guoxu-ju-you-yu': dict(
        declarations=rc('Counts.proportional_locks'),
        zh=('两个可互替的供给者任一即足（either_suffices）。',
            '两个可互替的供给者任一即足（either_suffices）。据有余而制不足若读作规则按各类所持之比例给出（比例读法），持多者被偏向而持得更多，'
            '回路不回转（Counts.proportional_locks）。'),
        en=('where two feeders would each suffice (either_suffices).',
            'where two feeders would each suffice (either_suffices). Read as a rule given in proportion to what each kind '
            'holds, the kind holding more is favoured and holds more, and the loop does not turn back '
            '(Counts.proportional_locks).')),
    'shangjunshu-yi-shang-yi-xing-yi-jiao': dict(
        declarations=rc('uniform_locks', 'Second.second_exact'),
        zh=('商君书把壹作为为国之道；',
            '壹读作一个在每个份额都偏向同一方向的读法时，每条进程自第二个读取步之后锁定，且确切（uniform_locks、Second.second_exact），'
            '只有改变规则怎样读才离开。商君书把壹作为为国之道；'),
        en=('(share_rises_through); the text takes',
            '(share_rises_through); read as one reading favouring one way at every share, every course is locked from its '
            'second reading step, exactly, and only a change of how the rule reads leaves (uniform_locks, '
            'Second.second_exact); the text takes')),
}
GAP = (f'RC (Becoming.RuleCapture, record {RID}, study section {N}); the statement above is kept as proposed. With the '
       'margin a natural number, as stated, (i) and (ii) hold at every step, not only at reading steps '
       '(Counts.margin_course, Counts.rises_strictly_along), and (iii) holds for every change of the margin '
       '(perturbation_absorbed). Where rules can favour the others, (i) and (ii) need the start locked (locked_stays; '
       'Alternating refutes them without it), (iii) holds exactly for perturbations keeping the direction '
       '(Reversed.not_absorbed), and leaving needs a change of h where the reading favours at every share '
       f'(uniform_locks, exact by Second.second_exact). Readings D{D}.')
WHY = ('RC: Becoming.RuleCapture proved the loop the reading named as a gap (capture through the rule); its laws and '
       'record added and a sentence of each reading replaced or extended (both languages)')

# 1. The passage map, through FIXES.
src = BUILD.read_text()
for key in ("fix.get('declarations_add', [])", "fix.get('records_add', [])", "fix.get('gap_closed')",
            "fix.get('reading_sub', [])", "fix.get('reading_en_sub', [])"):
    assert key in src, ('the build lacks', key)
assert 'RuleCapture' not in src, 'RC entries already in FIXES'


def lit(s, indent):
    """A Python string literal, split into adjacent literals of at most 100 characters, after a space or a mark."""
    parts, i = [], 0
    while len(s) - i > 100:
        cut = max(s.rfind(c, i + 40, i + 100) for c in ' ，；、。）')
        cut = cut + 1 if cut > 0 else i + 100
        parts.append(s[i:cut])
        i = cut
    parts.append(s[i:])
    if len(parts) == 1:
        return repr(parts[0])
    return '(' + ('\n' + ' ' * (indent + 1)).join(repr(x) for x in parts) + ')'


def entry_text(pid, fix):
    lines = [f'    {pid!r}: {{']
    for k, v in fix.items():
        head = f'        {k!r}: '
        if isinstance(v, str):
            lines.append(head + lit(v, len(head)) + ',')
        elif k in ('reading_sub', 'reading_en_sub'):
            pairs = []
            for old, new in v:
                pad = len(head) + 2
                pairs.append('(' + lit(old, pad) + ',\n' + ' ' * pad + lit(new, pad) + ')')
            lines.append(head + '[' + (',\n' + ' ' * (len(head) + 1)).join(pairs) + '],')
        else:
            lines.append(head + '[' + (',\n' + ' ' * (len(head) + 1)).join(repr(x) for x in v) + '],')
    lines[-1] = lines[-1][:-1] + '},'
    return '\n'.join(lines) + '\n'


before = {p['id']: p for p in json.loads(PASSAGES.read_text())['passages']}
assert all(i in before for i in EDITS)
ns = {'__file__': str(BUILD), '__name__': 'build_passages'}
exec(compile(src[:src.index('\n\ndef tradition(')], str(BUILD), 'exec'), ns)
FIXES = ns['FIXES']
for pid, e in EDITS.items():
    fix = {'declarations_add': e['declarations'], 'records_add': [RID],
           'reading_sub': [e['zh']], 'reading_en_sub': [e['en']]}
    if 'gap' in before[pid]:
        fix['gap_closed'] = GAP
    if pid in FIXES:
        # Merge into the entry already there (one key per passage; a second key would drop the first).
        old = FIXES[pid]
        assert 'gap_closed' not in old or 'gap_closed' not in fix, pid
        merged = {k: v for k, v in old.items() if k != 'why'}
        for k, v in fix.items():
            merged[k] = merged.get(k, []) + v if isinstance(v, list) else v
        merged['why'] = old['why'] + '; ' + WHY
        i = src.index(f'    {pid!r}: {{')
        j = src.index('},\n', i) + 3
        src = src[:i] + entry_text(pid, merged) + src[j:]
    else:
        CLOSE = '\n}\n\n\ndef tradition('
        src = once(src, CLOSE, '\n' + entry_text(pid, dict(fix, why=WHY)).rstrip('\n') + CLOSE)
ns = {'__file__': str(BUILD), '__name__': 'build_passages'}
exec(compile(src[:src.index('\n\ndef tradition(')], str(BUILD), 'exec'), ns)
assert set(ns['FIXES']) == set(FIXES) | set(EDITS)
assert all(ns['FIXES'][k] == FIXES[k] for k in FIXES if k not in EDITS)
for pid in EDITS:
    assert ns['FIXES'][pid]['records_add'][-1] == RID, pid
BUILD.write_text(src)
r = subprocess.run([sys.executable, '-B', str(BUILD)], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
data = json.loads(PASSAGES.read_text())
after = {p['id']: p for p in data['passages']}
assert set(after) == set(before)
changed = sorted(i for i in after if after[i] != before[i])
assert changed == sorted(EDITS), ('the rebuild changed other passages', changed)
for pid, e in EDITS.items():
    p = after[pid]
    assert p['declarations'][-len(e['declarations']):] == e['declarations'] and p['records'][-1] == RID, pid
    assert e['zh'][1] in p['reading'] and e['en'][1] in p['reading_en'], pid
    assert ('gap' not in p) or p['gap'].get('closed') == GAP, pid
assert {after[pid]['tradition'] for pid in EDITS} == {TRADITION}

# 2. The chapter.
chapter = CHAPTER.read_text()
b, e = V.begin(TRADITION), V.end(TRADITION)
i, j = chapter.index(b) + len(b), chapter.index(e)
chapter = chapter[:i] + '\n' + V.table(data['passages'], TRADITION) + '\n' + chapter[j:]
# §8: the row's "what is missing" cell says the gap is closed, as SC and Y5 mark theirs.
chapter = once(chapter, '| `Capture` 说“胜者塑造规则”未推出；`Pace` 的规则读快层，但没有份额与选择 |',
               f'| 已由 RC 补上（[`Becoming.RuleCapture`]({LEAN})，记录 [{RID}](../results/records/{RID}.md)）；'
               '此前 `Capture` 说“胜者塑造规则”未推出，`Pace` 的规则读快层，但没有份额与选择 |')
# §5.7 said the spine lacks the loop.
chapter = once(chapter, '并且说出了脊柱所缺的一个环：被选择者开始写选择的规则（君反制于臣，§8）。',
               '并且说出了一个环：被选择者开始写选择的规则（君反制于臣）。这一回路由 `RuleCapture` 给出（§8）：规则从所选出者的份额'
               '单调地读出时，回路锁定，只有改变规则怎样读才离开（`locked_stays`、`uniform_locks`）。')
# §11: the open gaps. The line lists the open gaps by number and then the gaps written; this one moves from the first
# list to the second, in order.
NUM = '一二三四五六七'
lines = [l for l in chapter.split('\n') if l.startswith('- §8 的')]
assert len(lines) == 1, lines
m = re.fullmatch(r'- §8 的第([一二三四五六七、]+)项缺口，各待写成 Lean（已认领者见工作板）；(.+)。', lines[0])
if not m or '三' not in m.group(1).split('、'):
    sys.exit(f'§11 line in an unknown form, edit by hand: {lines[0]}')
open_ = [x for x in m.group(1).split('、') if x != '三']
done = re.split(r'，(?=第[一二三四五六七]项)', m.group(2))
assert all(re.match(r'第[一二三四五六七]项（', x) for x in done), done
done.append('第三项（经由规则的捕获）已由 RC 写成')
done.sort(key=lambda x: NUM.index(x[1]))
new = (f'- §8 的第{"、".join(open_)}项缺口，各待写成 Lean（已认领者见工作板）；' if open_ else '- §8 的七项缺口都已写成：') \
    + '，'.join(done) + '。'
chapter = once(chapter, lines[0], new)
para = (HERE / 'ro_paragraph.zh.txt').read_text(encoding='utf-8').replace('{N}', N).replace('{D}', D) \
    .replace('{LEAN}', LEAN).replace('{STUDY}', STUDY_LINK).rstrip('\n')
TABLE_END = '\n\n另有两项已在映射期间由别处完成，或交给别处：'
chapter = once(chapter, TABLE_END, '\n\n' + para + TABLE_END)
CHAPTER.write_text(chapter)

# 3. RO's record.
decls = len({x for p in data['passages'] for x in p['declarations']})
recs = len({r for p in data['passages'] for r in p['records']})
d = json.loads(RO_RECORD.read_text())
vs = d['validation_scope']
vs['en'], k1 = re.subn(r'\d+ declarations in the current receipt, \d+ records',
                       f'{decls} declarations in the current receipt, {recs} records', vs['en'])
vs['zh'], k2 = re.subn(r'\d+ 个声明在现行回执中，\d+ 份记录', f'{decls} 个声明在现行回执中，{recs} 份记录', vs['zh'])
assert k1 == k2 == 1, (k1, k2)
nd = d['next_delta']
EN = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
ZH = '零一二三四五六七'
m_en = re.fullmatch(r'(One|Two|Three|Four|Five|Six|Seven) gaps?, each to be claimed before it is written: (.*?)\.(?: (Then .*))?',
                    nd['en'], re.S)
m_zh = re.fullmatch(r'([一二三四五六七])项缺口，各先认领再写：(.*?)。(然后.*)?', nd['zh'], re.S)
if not (m_en and m_zh):
    sys.exit(f'next_delta in an unknown form, edit by hand: {nd}')
gaps_en = m_en.group(2).split('; ')
gaps_zh = m_zh.group(2).split('；')
assert 'capture through the rule' in gaps_en and '经由规则的捕获' in gaps_zh, (gaps_en, gaps_zh)
gaps_en.remove('capture through the rule')
gaps_zh.remove('经由规则的捕获')
assert len(gaps_en) == len(gaps_zh) == EN.index(m_en.group(1)) - 1, (gaps_en, gaps_zh)
if gaps_en:
    nd['en'] = (f'{EN[len(gaps_en)]} gap{"s" if len(gaps_en) > 1 else ""}, each to be claimed before it is written: '
                f'{"; ".join(gaps_en)}.' + (f' {m_en.group(3)}' if m_en.group(3) else ''))
    nd['zh'] = f'{ZH[len(gaps_zh)]}项缺口，各先认领再写：{"；".join(gaps_zh)}。' + (m_zh.group(3) or '')
else:
    nd['en'] = 'Every gap the map found is written.' + (f' {m_en.group(3)}' if m_en.group(3) else '')
    nd['zh'] = '映射所见的缺口都已写成。' + (m_zh.group(3) or '')
assert len(nd['en']) <= 400 and len(nd['zh']) <= 180, (len(nd['en']), len(nd['zh']))
assert not any(x['id'] == RID for x in d.get('related', []))
d.setdefault('related', []).append({
    'id': RID,
    'detail': {'en': 'Closes the third gap (capture through the rule); the passages 二柄, 据有余而制不足 and 壹 are re-pointed '
                     'to its laws.',
               'zh': '补上第三项缺口（经由规则的捕获）；二柄、据有余而制不足与壹三段改指向其律。'}})
h = lambda p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True,
                                                  cwd=ROOT).stdout).hexdigest()
files = []
for ref in d['references']:
    p = ref['path']
    if ref.get('sha256') == at_base(p) != h(p):
        ref['sha256'] = h(p)
        files.append(p.rsplit('/', 1)[-1])
assert 'passages.json' in files and 'CHINESE-SOURCES-AND-BECOMING.md' in files, files
n_open = len(gaps_en)
d['history'].append({
    'en': f'19 October 2026, RC (capture through the rule): the third gap closed by Becoming.RuleCapture ({RID}); three '
          f'passages re-pointed to its laws (declarations, the record, a sentence of each reading) through the build\'s '
          f'FIXES and 二柄\'s gap marked closed, and the gap marked closed in chapter sections 5.7, 8 and 11; the next '
          f'step lists the {EN[n_open].lower() if n_open else "no"} gap{"s" if n_open != 1 else ""} still open; the '
          f'counts verify_ro.py reports brought to {decls} declarations and {recs} records; '
          f'{", ".join(sorted(set(files)))} re-pointed after reading the change. The assessment is otherwise unchanged.',
    'zh': f'2026年10月19日，RC（经由规则的捕获）：第三项缺口由 Becoming.RuleCapture（{RID}）补上；三段经构建的 FIXES 改指向其律（声明、'
          f'记录、各读法中的一句），二柄的缺口标为已补上，章节第 5.7、8、11 节亦然；下一步只列尚未补上的{ZH[n_open]}项缺口；'
          f'verify_ro.py 所报计数更新为 {decls} 个声明、{recs} 份记录；读过改动后，{"、".join(sorted(set(files)))} 重新指向。评估其余不变。'})
RO_RECORD.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('patched', len(EDITS), 'passages;', TRADITION, '; RO record', ', '.join(sorted(set(files))))
