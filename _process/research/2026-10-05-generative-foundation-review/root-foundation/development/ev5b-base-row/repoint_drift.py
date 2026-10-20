#!/usr/bin/env python3
"""EV5b (20 October 2026): re-point the chapter reference of records that `research.py check` reports as drifting only
in EV5b's edits (section 2.4's GroupEnding bullet and section 9's receipt and counts), after reading the change:
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
    if not d['history'][-1]['en'].startswith('20 October 2026, EV5b '):
        d['history'].append({
            'en': '20 October 2026, EV5b (the evolution row\'s central laws on the base): THE-THEORY-OF-BECOMING.md re-pointed. Since '
                  'this record\'s reviewed hash, the cited text changed only by EV5b\'s edits: the Becoming.GroupEnding bullet in 2.4 '
                  '(the law for groups not uniform) and section 9\'s receipt and counts. Read before re-pointing. The claim is unchanged.',
            'zh': '2026年10月20日，EV5b（演化一行的中心之律在流上）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只因 EV5b 的改动而变：'
                  '2.4 的 Becoming.GroupEnding 一条（各组不均匀时之律）与第 9 节的回执与计数。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
