#!/usr/bin/env python3
"""Z1 (19 October 2026): re-point the chapter reference of records that `research.py render` reports as drifting only
in Z1's edits (sections 8 and 9), after reading the change: python3 -B repoint_drift.py ID ..."""
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
    if not d['history'][-1]['en'].startswith('19 October 2026, Z1 '):
      d['history'].append({
        'en': '19 October 2026, Z1 (the game of relative position): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              'record\'s reviewed hash, the cited text changed only in sections 8 and 9: Z1 added the connectivity rerun '
              'on its tree to the "Integration of the spine" row of section 8.2, and the Z1 core receipt and its counts '
              'to section 9. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，Z1（相对位置的博弈）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8、9 节改动：'
              'Z1 在第 8.2 节“脊柱的整合”一行加上其树上的连通性重测，第 9 节改为 Z1 的核心回执及其计数。'
              '重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
