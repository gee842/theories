#!/usr/bin/env python3
"""PE1 (20 October 2026): re-point the chapter reference of records that `research.py render` reports as drifting only
in PE1's edits to section 0 (the proof-language row) and section 9 (the paragraph on propext, the receipt and counts),
after reading the change: python3 -B repoint_drift.py ID ...   (from the checkout root)"""
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
    d['history'].append({
        'en': '20 October 2026, PE1 (what identifying interderivable propositions keeps and loses): '
              'THE-THEORY-OF-BECOMING.md re-pointed. Since this record\'s reviewed hash, the chapter changed only by '
              'PE1\'s edits: a sentence in section 0\'s proof-language row, and in section 9 a paragraph on why the core '
              'excludes propext, the receipt, counts and layers. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月20日，PE1（等同可互推的命题保留什么、失去什么）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，'
              '本章只因 PE1 的改动而变：第 0 节证明语言一行的一句，以及第 9 节关于核心为何不用 propext 的一段、回执、计数与层。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
