#!/usr/bin/env python3
"""PT1 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections 8 and 9 (the open programme and the formal spine), after reading the change:
python3 -B repoint_drift.py ID ..."""
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
        'en': '19 October 2026, PT1 (place/transition nets on the spine): THE-THEORY-OF-BECOMING.md re-pointed. Since '
              'this record\'s reviewed hash, the cited text changed only in sections 8 and 9: PT1 added a section 8.7 '
              'bullet on place/transition nets and a rerun sentence in the integration row, and brought the section 9 '
              'receipt and counts to its run. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，PT1（脊柱上的库所/变迁网）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在'
              '第 8、9 节改动：PT1 在 8.7 节加入关于库所/变迁网的一条，在整合行加入一句重跑，并把第 9 节的回执与计数更新到其运行。'
              '重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
