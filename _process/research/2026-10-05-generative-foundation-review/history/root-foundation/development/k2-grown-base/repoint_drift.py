#!/usr/bin/env python3
"""K2 (19 October 2026): re-point the chapter reference of records that `research.py render` reports as drifting only
in K2's edits (sections 2, 8 and 9), after reading the change: python3 -B repoint_drift.py ID ..."""
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
        'en': '19 October 2026, K2 (growth by attachment on the base): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              'record\'s reviewed hash, the cited text changed only in sections 2, 8 and 9: K2 added one sentence on worlds '
              'grown by attachment to the "Which links a closure needs" bullet of section 2, the connectivity rerun on its '
              'landing tree to the "Integration of the spine" row of section 8.2, and the K2 core receipt and its counts '
              '(263 core modules, 9,946 theorems) to section 9. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，K2（依附式生长在基上）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 2、8、9 节改动：'
              'K2 在第 2 节“闭包需要哪些联系”一条加上一句关于依附式生长的世界，在第 8.2 节“脊柱的整合”一行加上其落地树上的连通性重测，'
              '第 9 节改为 K2 的核心回执及其计数（263 个核心模块，9,946 条定理）。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
