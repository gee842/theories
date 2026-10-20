#!/usr/bin/env python3
"""F3R sub-chain 2 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as
drifting only in sections 8 and 9 through F3R's landing edits, after reading the change: python3 -B repoint_drift_r.py ID ..."""
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
        'en': '19 October 2026, F3R sub-chain 2 (Becoming.ActivationCapacity): THE-THEORY-OF-BECOMING.md re-pointed. Since '
              "this record's reviewed hash, the cited text changed only in section 8 (the connectivity rerun sentence of the "
              '"Integration of the spine" row) and section 9 (the core module counts and the current receipt). Read before '
              're-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，F3R 第二子链（Becoming.ActivationCapacity）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，'
              '所引文字只在第 8 节（“脊柱的整合”行的连通性重测句）和第 9 节（核心模块计数与当前回执）改动。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
