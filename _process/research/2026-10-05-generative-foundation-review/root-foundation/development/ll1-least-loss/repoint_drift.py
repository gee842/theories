#!/usr/bin/env python3
"""LL1 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections LL1 changed, after reading the change: python3 -B repoint_drift.py SECTIONS_JSON ID ...
SECTIONS_JSON maps each drifting record id to its changed sections, from the check log."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
WHAT = {
    '## The theory stated in full': 'LL1 extended the sentence of item 4 on the rest theorem\'s whole unit with the '
                                    'least-loss law, the approach to rest and the join with recurrence',
    '## 0. Premise card': 'LL1 added to the dissipation row and the natural-number amounts row where the least loss is '
                          'a premise (Becoming.LeastLoss)',
    '## 1. Becoming: one unfolding': 'LL1 restated the last sentence of "Limits of the rest theorem" as the least-loss '
                                     'law, the approach to rest and the join with recurrence',
    '## 8. Open programme': 'LL1 added to the entropy and recurrence row (its open item and the record least-loss-rest), '
                            'a rerun sentence in the integration row, and sentences in sections 8.6 and 8.7',
    '## 9. The formal spine': 'LL1 revised the receipt sentence and counts',
}
WHAT_ZH = {
    '## The theory stated in full': '完整陈述（LL1 在第 4 条关于整数单位的一句后加入最小损失律、趋近停息与复现的连接）',
    '## 0. Premise card': '第 0 节（LL1 在耗散行与自然数量行加入最小损失作为前提之处）',
    '## 1. Becoming: one unfolding': '第 1 节（LL1 把“停息定理的界限”末句重述为最小损失律、趋近停息与复现的连接）',
    '## 8. Open programme': '第 8 节（LL1 在熵与复现行加入开放项与记录 least-loss-rest，在整合行加入一句重跑，在第 8.6、8.7 节加句）',
    '## 9. The formal spine': '第 9 节（LL1 更新回执句与计数）',
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
        'en': '19 October 2026, LL1 (the least loss as a premise of rest): THE-THEORY-OF-BECOMING.md re-pointed. '
              'Since this record\'s reviewed hash, the cited text changed only where LL1 added text: '
              + '; '.join(WHAT[s] for s in secs) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，LL1（最小损失作为停息的前提）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在 LL1 加文之处改动：'
              + '；'.join(WHAT_ZH[s] for s in secs) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
