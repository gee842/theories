#!/usr/bin/env python3
"""K3 (19 October 2026): re-point the chapter reference of records that `research.py check` reports as drifting only in
sections 8 and 9, after reading the change: python3 -B repoint_drift.py ID ..."""
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
        'en': '19 October 2026, K3 (Becoming.Cuts): THE-THEORY-OF-BECOMING.md re-pointed. Since this record\'s reviewed '
              'hash, the cited text changed only in sections 8 and 9: K3 added the connectivity rerun on its landing tree '
              'to the "Integration of the spine" row of section 8.2, and section 9 now names the K3 core receipt (counts '
              'unchanged). Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，K3（Becoming.Cuts）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8、9 节改动：'
              'K3 在第 8.2 节“脊柱的整合”一行加上其落地树上的连通性重测，第 9 节改为 K3 的核心回执（计数不变）。'
              '重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
