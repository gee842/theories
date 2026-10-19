#!/usr/bin/env python3
"""U5 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections U5 changed, after reading the change: python3 -B repoint_drift.py SECTIONS_JSON ID ...
SECTIONS_JSON maps each drifting record id to its changed sections, from the render log."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
WHAT = {
    '## 0. Premise card': 'U5 added the world reading of J3 to row F',
    '## 2. Organization, renewal and evolution': 'U5 added the word half of histories to the paragraph on what a '
                                                 'finite stretch refutes (Becoming.HistoryIdealsTraces)',
    '## 3. Knowing and inquiry': 'U5 added narrowing on the pure observation (Becoming.NarrowingRuns) and evidence '
                                 'under fallible witnesses for every roster (Becoming.WitnessRefinementRuns)',
    '## 6. Significance, comparison and practical judgment': 'U5 added J3 on a world\'s moves (FrontierWorlds)',
    '## 8. Open programme': 'U5 added a rerun sentence in the integration row',
    '## 9. The formal spine': 'U5 revised the receipt sentence and counts',
}
WHAT_ZH = {
    '## 0. Premise card': '第 0 节（U5 在 F 行加入 J3 的世界读法）',
    '## 2. Organization, renewal and evolution': '第 2 节（U5 加入只按移动读的历史）',
    '## 3. Knowing and inquiry': '第 3 节（U5 加入沿纯观察收窄与对每个名册的检视）',
    '## 6. Significance, comparison and practical judgment': '第 6 节（U5 加入世界移动上的 J3）',
    '## 8. Open programme': '第 8 节（U5 在整合行加入一句重跑）',
    '## 9. The formal spine': '第 9 节（U5 更新回执句与计数）',
}
sections = json.load(open(sys.argv[1]))
h = hashlib.sha256(open(C, 'rb').read()).hexdigest()
for i in sys.argv[2:]:
    secs = sections[i]
    assert secs and all(s in WHAT for s in secs), (i, secs)
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f))
    n = 0
    for r in d['references']:
        if r['path'] == C and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (i, n)
    d['history'].append({
        'en': '19 October 2026, U5 (general laws read on the base): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              'record\'s reviewed hash, the cited text changed only where U5 added text: '
              + '; '.join(WHAT[s] for s in secs) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，U5（在基上读出的一般规律）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在 U5 加文之处改动：'
              + '；'.join(WHAT_ZH[s] for s in secs) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
