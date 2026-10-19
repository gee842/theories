#!/usr/bin/env python3
"""RG (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections RG changed, after reading the change: python3 -B repoint_drift.py SECTIONS_JSON ID ...
SECTIONS_JSON maps each drifting record id to its changed sections, from the render log."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
WHAT = {
    '## 4. Collective dynamics': 'RG added a paragraph on a level held from both sides and read late (Becoming.Regulation) '
                                 'after the paragraph on Pace, and amended constraint 7 of the table',
    '## 8. Open programme': 'RG amended the collective-continuation row and added a rerun sentence in the integration row',
    '## 9. The formal spine': 'RG revised the receipt sentence and counts',
}
WHAT_ZH = {
    '## 4. Collective dynamics': '第 4 节（RG 在 Pace 段后加入两侧保持与迟读之段，并修订表中第 7 条）',
    '## 8. Open programme': '第 8 节（RG 修订集体延续行，并在整合行加入一句重跑）',
    '## 9. The formal spine': '第 9 节（RG 更新回执句与计数）',
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
        'en': '19 October 2026, RG (two-sided regulation and late reading): THE-THEORY-OF-BECOMING.md re-pointed. Since '
              'this record\'s reviewed hash, the cited text changed only where RG added text: '
              + '; '.join(WHAT[s] for s in secs) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，RG（双向调节与迟读）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在 RG 加文之处改动：'
              + '；'.join(WHAT_ZH[s] for s in secs) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
