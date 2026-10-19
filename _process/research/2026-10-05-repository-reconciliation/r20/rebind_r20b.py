#!/usr/bin/env python3
"""R20(b) (19 October 2026): re-point records whose cited Markdown R20(b) changed, after reading the change.

usage: python3 -B rebind_r20b.py CHECK_JSON

CHECK_JSON is the output of `research.py check`. Only references to the two Markdown files R20(b)
changed are re-pointed (the canonical chapter and the nondual method); Lean sources whose docstrings
R20(b) changed are left drifting on purpose, because their records bind proof receipts and the new
bytes need a checker run first. Every record re-pointed here was read against the changed lines
(../r19/drift_lines.py prints them): R20(b) changed wording only, saying exactly what the Lean shows
(instantiation of the condition, witnesses for "can" claims, the whole-unit dependence of the rest
laws, definitional laws, the law_iff_em lemma, the pure core's axiom report) and adding section 8.9;
in the nondual method, "generative" no longer names any formation. No record's claim depends on
those lines. Each drifted reference gets the current hash and a dated note in English and Chinese.
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CHANGED = {'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md',
           'theories/becoming/chapters/NONDUAL-METHOD.md'}
text = open(sys.argv[1]).read()
start = text.index('{', text.index('research.py check') if 'research.py check' in text else 0)
chk, _ = json.JSONDecoder().raw_decode(text[start:])
drift = [d for d in chk['source_drift'] + chk['unrelated_source_drift'] if d['path'] in CHANGED]
by_id = {}
for d in drift:
    by_id.setdefault(d['id'], set()).add(d['path'])

EN = ("19 October 2026, R20(b) (chapter and method say exactly what the Lean shows): {files} re-pointed after reading "
      "the change. R20(b) changed wording only: consequences of the continuation condition are stated as instantiations, "
      "witnesses for \"can\" claims are marked as witnesses, the rest laws' dependence on whole-unit amounts is named, "
      "definitional laws are said to be definitional, law_iff_em is a lemma, the pure core's axiom report is stated "
      "exactly, section 8.9 lists objections not yet answered, and \"generative\" no longer names any formation. "
      "No line this record relies on changed its content. The claim is unchanged.")
ZH = ("2026年10月19日，R20(b)（理论章与方法恰说 Lean 所表明的）：{files} 读过改动后重新指向。R20(b) 只改措辞："
      "延续条件的推论陈述为实例化，“可以”的见证标为见证，指明停息定律依赖整单位的量，定义性的规律说明是定义性的，"
      "law_iff_em 是引理，纯核心的公理报告确切陈述，第 8.9 节列出尚未回答的反对，“generative”不再指任何形成。"
      "本记录所依的文字内容未变。论断不变。")

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
