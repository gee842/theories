#!/usr/bin/env python3
"""MA1 (20 October 2026): re-point the chapter reference of records that `research.py render` reports as drifting only
in MA1's edits to section 4 (4.1, 4.3's table row 6, 4.5) and section 9, after reading the change:
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
    if not d['history'][-1]['en'].startswith('20 October 2026, MA1 '):
        d['history'].append({
            'en': '20 October 2026, MA1 (the meta-attractor\'s loop closed on the spine): THE-THEORY-OF-BECOMING.md '
                  're-pointed. Since this record\'s reviewed hash, the cited text changed in section 4 only by MA1\'s '
                  'additions: a sentence in 4.1, the law cell of row 6 of 4.3\'s table, and in 4.5 a sentence of "In '
                  'words", a bullet for Becoming.ClosedCapture, a reading of the meta-attractor and the record list; and '
                  'section 9\'s receipt and counts. Read before re-pointing. The claim is unchanged.',
            'zh': '2026年10月20日，MA1（元吸引子的回路在主干上闭合）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，第 4 节所引文字只因 '
                  'MA1 的增补而改动：4.1 的一句，4.3 表第 6 行的定律格，4.5 的“要点”一句、Becoming.ClosedCapture 的一条、元吸引子的读法与记录列表；'
                  '以及第 9 节的回执与计数。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
