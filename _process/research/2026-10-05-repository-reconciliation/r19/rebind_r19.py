#!/usr/bin/env python3
"""R19 (19 October 2026): re-point records whose cited text R19 changed, after reading the change.

usage: python3 -B rebind_r19.py CHECK_JSON

CHECK_JSON is the output of `research.py check`. Every record in its source_drift and
unrelated_source_drift lists was read against the changed lines (drift_lines.py in this
folder prints them). R19 changed wording only: living significance stated as the Lean shows,
reasons in place of Ren's past words as warrant, review bookkeeping dropped, a moved chapter's
link. No record's claim depends on those lines. Each drifted reference gets the current hash and
a dated history note in English and Chinese.
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
text = open(sys.argv[1]).read()
chk = json.loads(text[text.index('{'):])
drift = chk['source_drift'] + chk['unrelated_source_drift']
by_id = {}
for d in drift:
    by_id.setdefault(d['id'], set()).add(d['path'])

EN = ("19 October 2026, R19 (the review of 19 October, fixed): {files} re-pointed after reading the change. "
      "R19 changed wording only: living significance is stated as the Lean shows (significance from every standpoint, "
      "no valence; the `living` readings do not include further generation); reasons replace Ren's past words where "
      "they served as warrant or standing; review bookkeeping was dropped; a link follows a chapter moved to history. "
      "No line this record relies on changed its content. The claim is unchanged.")
ZH = ("2026年10月19日，R19（10月19日审查的修正）：{files} 读过改动后重新指向。R19 只改措辞：生命意义按 Lean 所证陈述"
      "（从每个立足点都有意义，不带正负；`living` 的读法不含继续生成）；以理由取代把 Ren 过去的话当作依据或地位之处；"
      "删去审查记账；一处链接随移入历史的章节更新。本记录所依的文字内容未变。论断不变。")

for rid, paths in sorted(by_id.items()):
    p = ROOT / 'theories/becoming/results/records' / f'{rid}.json'
    d = json.loads(p.read_text())
    files = []
    for r in d['references']:
        if r.get('path') in paths:
            r['sha256'] = hashlib.sha256((ROOT / r['path']).read_bytes()).hexdigest()
            files.append(r['path'].rsplit('/', 1)[-1])
    names = ', '.join(sorted(set(files)))
    d['history'].append({'en': EN.format(files=names), 'zh': ZH.format(files=names)})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(rid, names)
