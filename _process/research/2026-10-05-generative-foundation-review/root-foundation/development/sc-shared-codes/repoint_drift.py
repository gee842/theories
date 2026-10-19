#!/usr/bin/env python3
"""SC (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections 4, 8 and 9 (where SC added its paragraph, its rows and its receipt), after reading the change:
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
        'en': '19 October 2026, SC (a code formed between formations): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              'record\'s reviewed hash, the cited text changed only in sections 4, 8 and 9: SC added a section 4 paragraph '
              'on a code formed between formations, a clause to the collective continuation row, a section 8.3 item and '
              'a rerun sentence in the integration row, and brought the section 9 receipt and counts to its run. Read '
              'before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，SC（在形成之间形成的编码）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 '
              '4、8、9 节改动：SC 在第 4 节加入关于在形成之间形成的编码的一段，在集体延续一行加入一句，在 8.3 节加入一项，在整合行加入一句'
              '重跑，并把第 9 节的回执与计数更新到其运行。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
