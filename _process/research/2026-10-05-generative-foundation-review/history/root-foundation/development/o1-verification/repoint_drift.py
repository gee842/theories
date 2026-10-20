#!/usr/bin/env python3
"""O1 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in section 8 (the open programme), after reading the change: python3 -B repoint_drift.py ID ..."""
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
        'en': '19 October 2026, O1 (what a finite stretch verifies): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              'record\'s reviewed hash, the cited text changed only in section 8 (the open programme): O1 revised the '
              'section 8.1 row of the scientific-inquiry target and the section 8.2 row "Origins and refutation", and '
              'added a rerun sentence in the integration row. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，O1（有限片段所证实者）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8 节'
              '（开放纲领）改动：O1 修订科学探究目标的第 8.1 节行与第 8.2 节“起源与否证”行，并在整合行加入一句重跑。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
