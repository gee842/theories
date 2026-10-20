#!/usr/bin/env python3
"""EV2 (20 October 2026): re-point the chapter reference of records that `research.py check` reports as drifting only
in EV2's edits (section 2.4's bullet, fitness sentence and record list, the record table's row, section 8.1 item 9, and
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
    if not d['history'][-1]['en'].startswith('20 October 2026, EV2 '):
        d['history'].append({
            'en': '20 October 2026, EV2 (what bounds offspring numbers): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
                  'record\'s reviewed hash, the cited text changed only by EV2\'s additions: in 2.4 a bullet for '
                  'Becoming.Reproduction, the fitness sentence and the record list; a row of the record table; 8.1 item 9; '
                  'and section 9\'s receipt and counts. Read before re-pointing. The claim is unchanged.',
            'zh': '2026年10月20日，EV2（什么约束后代数）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只因 EV2 的增补而改动：'
                  '2.4 的 Becoming.Reproduction 一条、适应度一句与记录列表；记录表的一行；8.1 第 9 项；以及第 9 节的回执与计数。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
