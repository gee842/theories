#!/usr/bin/env python3
"""RG (19 October 2026): bring RO's record, chinese-sources-on-the-spine, to the passage map RG re-pointed:
  python3 -B update_ro_record.py BASE        (from the checkout root, after ro_points.py and make_record.py)
As SC's script does: the counts verify_ro.py reports (declarations, records) are recomputed from passages.json; the next
step lists only the gaps still open (whichever landing closed the others); RG's record is added to the related list;
the closed connection is a progress line anchored at RG's study section; each reference that matched its file at BASE
and changed is re-pointed; a history note says what changed."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = sys.argv[1]
ROOT = Path.cwd()
RID = 'two-sided-regulation-and-late-reading'
PATH = ROOT / 'theories/becoming/results/records/chinese-sources-on-the-spine.json'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
PASSAGES = ROOT / f'{RF}/development/ro-relational-sources/passages.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
GAP_EN, GAP_ZH = 'two-sided regulation of a level and its late-reading form', '水平的双向调节及迟到读法之形'

study = (ROOT / STUDY).read_text()
title = re.search(r'^## ((\d+)\. A level held from both sides, and a level read late \(RG\))$', study, re.M)
assert title, 'study section missing'
SLUG = re.sub(r'[^\w\- ]', '', title.group(1).lower()).replace(' ', '-')

passages = json.loads(PASSAGES.read_text())['passages']
decls = len({x for p in passages for x in p['declarations']})
recs = len({r for p in passages for r in p['records']})
d = json.loads(PATH.read_text())
vs = d['validation_scope']
vs['en'], k1 = re.subn(r'\d+ declarations in the current receipt, \d+ records',
                       f'{decls} declarations in the current receipt, {recs} records', vs['en'])
vs['zh'], k2 = re.subn(r'\d+ 个声明在现行回执中，\d+ 份记录', f'{decls} 个声明在现行回执中，{recs} 份记录', vs['zh'])
assert k1 == k2 == 1, (k1, k2)
# The next step lists the gaps still open: this one leaves the list, and so does any gap another landing marked closed
# in place; the count is the number left. A closing sentence ("Then …") is kept where there is one.
nd = d['next_delta']
EN = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
ZH = '零一二三四五六七'
m_en = re.fullmatch(r'(One|Two|Three|Four|Five|Six|Seven) gaps?, each to be claimed before it is written: (.*?)\.(?: (Then .*))?',
                    nd['en'], re.S)
m_zh = re.fullmatch(r'([一二三四五六七])项缺口，各先认领再写：(.*?)。(然后.*)?', nd['zh'], re.S)
assert m_en and m_zh, nd
assert GAP_EN in m_en.group(2).split('; ') and GAP_ZH in m_zh.group(2).split('；'), nd
gaps_en = [g for g in m_en.group(2).split('; ') if g != GAP_EN and '(closed by' not in g]
gaps_zh = [g for g in m_zh.group(2).split('；') if g != GAP_ZH and '补上' not in g]
assert gaps_en and len(gaps_en) == len(gaps_zh) < EN.index(m_en.group(1)), (gaps_en, gaps_zh)
dropped = EN.index(m_en.group(1)) - len(gaps_en)
nd['en'] = f'{EN[len(gaps_en)]} gap{"s" if len(gaps_en) > 1 else ""}, each to be claimed before it is written: ' \
           f'{"; ".join(gaps_en)}.' + (f' {m_en.group(3)}' if m_en.group(3) else '')
nd['zh'] = f'{ZH[len(gaps_zh)]}项缺口，各先认领再写：{"；".join(gaps_zh)}。' + (m_zh.group(3) or '')
assert len(nd['en']) <= 400 and len(nd['zh']) <= 180, (len(nd['en']), len(nd['zh']))
assert not any(r['id'] == RID for r in d.get('related', []))
d.setdefault('related', []).append({
    'id': RID,
    'detail': {'en': 'Closes the first gap (two-sided regulation of a level and its late-reading form); the passages '
                     '天之道 (老子 77), 冲气以为和, 宽猛相济 and 中和 are re-pointed to its laws.',
               'zh': '补上第一项缺口（水平的双向调节及迟到读法之形）；天之道（老子七十七章）、冲气以为和、宽猛相济与中和四段改指向其律。'}})
d.setdefault('progress', []).append({
    'en': 'The first gap closed: a level held from both sides settles exactly where it does not overshoot, and read '
          'late it needs a band growing with the lateness (two-sided-regulation-and-late-reading).',
    'zh': '第一项缺口补上：两侧保持的水平恰在不越过处定下，迟读时所需之带随迟而增（two-sided-regulation-and-late-reading）。',
    'source': f'{STUDY}#{SLUG}'})
h = lambda p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout).hexdigest()
files = []
for r in d['references']:
    p = r['path']
    if r.get('sha256') == at_base(p) != h(p):
        r['sha256'] = h(p)
        files.append(p.rsplit('/', 1)[-1])
assert 'passages.json' in files and 'CHINESE-SOURCES-AND-BECOMING.md' in files, files
d['history'].append({
    'en': f'19 October 2026, RG (two-sided regulation and late reading): the first gap closed by Becoming.Regulation '
          f'({RID}); four passages re-pointed to its laws (declarations, the record, the sentences of each reading that '
          f'named the gap; 中和 gains a reading of 中节) and the gap marked closed in the map and in chapter sections 8 '
          f'and 11, two points of the 宽猛 gap left open; the next step lists the {len(gaps_en)} gaps still open'
          f'{" (the gaps closed earlier leave the list too)" if dropped > 1 else ""}; the counts verify_ro.py reports '
          f'brought to {decls} declarations and {recs} records; {", ".join(sorted(set(files)))} re-pointed after '
          'reading the change. The assessment is otherwise unchanged.',
    'zh': f'2026年10月19日，RG（双向调节与迟读）：第一项缺口由 Becoming.Regulation（{RID}）补上；四段改指向其律（声明、记录、'
          f'各读法中指称缺口的句子；中和增一条中节之读），缺口在对应表与章节第 8、11 节标为已补上，宽猛条缺口中的两点仍开放；'
          f'下一步只列尚未补上的 {len(gaps_zh)} 项缺口{"（此前已补上的也移出）" if dropped > 1 else ""}；verify_ro.py 所报计数'
          f'更新为 {decls} 个声明、{recs} 份记录；读过改动后，{"、".join(sorted(set(files)))} 重新指向。评估其余不变。'})
PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated chinese-sources-on-the-spine:', decls, 'declarations,', recs, 'records; open', len(gaps_en),
      '; re-pointed', sorted(set(files)))
