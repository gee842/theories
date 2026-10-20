#!/usr/bin/env python3
"""EV4 and EV5 (20 October 2026): re-point the chapter reference of records that `research.py check` reports as drifting only
in EV4's and EV5's edits (section 2.4's bullets and record list, the record table's row, section 8.1 item 9, and
section 9's receipt and counts), after reading the change:
python3 -B repoint_drift.py ID ...   (from the checkout root)"""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
h = hashlib.sha256(open(C, 'rb').read()).hexdigest()
for i in sys.argv[1:]:
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f))
    n = 0
    for r in d['references']:
        if r['path'] == C and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (i, n)
    if not d['history'][-1]['en'].startswith('20 October 2026, EV4 and EV5 '):
        d['history'].append({
            'en': '20 October 2026, EV4 and EV5 (selection within and among groups; among groups by ending): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
                  'record\'s reviewed hash, the cited text changed only by EV4\'s and EV5\'s additions: in 2.4 a bullet for each of '
                  'Becoming.SelectionLevels and Becoming.GroupEnding and the record list; two rows of the record table; 8.1 item 9; '
                  'and section 9\'s receipt and counts. Read before re-pointing. The claim is unchanged.',
            'zh': '2026年10月20日，EV4 与 EV5（组内与组间选择；经由终止的组间选择）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只因 EV4 与 EV5 的增补而改动：'
                  '2.4 的 Becoming.SelectionLevels 与 Becoming.GroupEnding 各一条与记录列表；记录表的两行；8.1 第 9 项；以及第 9 节的回执与计数。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
