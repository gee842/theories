#!/usr/bin/env python3
"""SC (19 October 2026): bring RO's record, chinese-sources-on-the-spine, to the passage map SC re-pointed:
  python3 -B update_ro_record.py BASE        (from the checkout root, after patch_ro.py)
The counts verify_ro.py reports (declarations in the current receipt, records) are recomputed from passages.json; the
next step lists only the gaps still open; SC's record is added to its related list; each reference that matched
its file at BASE and changed is re-pointed; a history note says what changed."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

BASE = sys.argv[1]
ROOT = Path.cwd()
RID = 'a-code-formed-between-formations'
PATH = ROOT / 'theories/becoming/results/records/chinese-sources-on-the-spine.json'
PASSAGES = ROOT / ('_process/research/2026-10-05-generative-foundation-review/root-foundation/development/'
                   'ro-relational-sources/passages.json')


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


passages = json.loads(PASSAGES.read_text())['passages']
decls = len({x for p in passages for x in p['declarations']})
recs = len({r for p in passages for r in p['records']})
d = json.loads(PATH.read_text())
vs = d['validation_scope']
vs['en'], k1 = re.subn(r'\d+ declarations in the current receipt, \d+ records',
                       f'{decls} declarations in the current receipt, {recs} records', vs['en'])
vs['zh'], k2 = re.subn(r'\d+ 个声明在现行回执中，\d+ 份记录', f'{decls} 个声明在现行回执中，{recs} 份记录', vs['zh'])
assert k1 == k2 == 1, (k1, k2)
# The next step lists the gaps still open: this one leaves the list, and so does any gap another landing marked closed in
# place (Y5 marks its gap "(closed by …)"); the count is the number left. The closing sentence ("Then …") is kept
# where there is one (RH removes it).
nd = d['next_delta']
EN = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
ZH = '零一二三四五六七'
m_en = re.fullmatch(r'(One|Two|Three|Four|Five|Six|Seven) gaps?, each to be claimed before it is written: (.*?)\.(?: (Then .*))?',
                    nd['en'], re.S)
m_zh = re.fullmatch(r'([一二三四五六七])项缺口，各先认领再写：(.*?)。(然后.*)?', nd['zh'], re.S)
assert m_en and m_zh, nd
gaps_en = [g for g in m_en.group(2).split('; ') if g != 'a code formed between formations' and '(closed by' not in g]
gaps_zh = [g for g in m_zh.group(2).split('；') if g != '在形成之间形成的编码' and '补上' not in g]
assert len(gaps_en) == len(gaps_zh) < EN.index(m_en.group(1)), (gaps_en, gaps_zh)
dropped = EN.index(m_en.group(1)) - len(gaps_en)
nd['en'] = f'{EN[len(gaps_en)]} gap{"s" if len(gaps_en) > 1 else ""}, each to be claimed before it is written: ' \
           f'{"; ".join(gaps_en)}.' + (f' {m_en.group(3)}' if m_en.group(3) else '')
nd['zh'] = f'{ZH[len(gaps_zh)]}项缺口，各先认领再写：{"；".join(gaps_zh)}。' + (m_zh.group(3) or '')
assert len(nd['en']) <= 400, len(nd['en'])
assert not any(r['id'] == RID for r in d.get('related', []))
d.setdefault('related', []).append({
    'id': RID,
    'detail': {'en': 'Closes the second gap (a code formed between formations); the passages 同则同之, 名无固宜, the '
                     '說文\'s 止戈 gloss and 书同文 are re-pointed to its laws.',
               'zh': '补上第二项缺口（在形成之间形成的编码）；同则同之、名无固宜、说文止戈之释与书同文四段改指向其律。'}})
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
    'en': f'19 October 2026, SC (a code formed between formations): the second gap closed by '
          f'Becoming.SharedCodes ({RID}); four passages re-pointed to its laws (declarations, the record, the sentence of '
          f'each reading that named the gap) and the gap marked closed in the map and in chapter sections 5.4, 8 and 11; '
          f'the next step lists the {len(gaps_en)} gaps still open'
          f'{" (the gaps closed earlier leave the list too)" if dropped > 1 else ""}; the counts '
          f'verify_ro.py reports brought to {decls} declarations and {recs} records; {", ".join(sorted(set(files)))} '
          're-pointed after reading the change. The assessment is otherwise unchanged.',
    'zh': f'2026年10月19日，SC（在形成之间形成的编码）：第二项缺口由 Becoming.SharedCodes（{RID}）补上；四段改指向其律（声明、记录、各读法'
          f'中指称缺口的那一句），缺口在对应表与章节第 5.4、8、11 节标为已补上；下一步只列尚未补上的 {len(gaps_zh)} 项缺口'
          f'{"（此前已补上的也移出）" if dropped > 1 else ""}；verify_ro.py 所报计数更新为 {decls} 个声明、{recs} 份记录；读过改动后，'
          f'{"、".join(sorted(set(files)))} 重新指向。评估其余不变。'})
PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated chinese-sources-on-the-spine:', decls, 'declarations,', recs, 'records; re-pointed', sorted(set(files)))
