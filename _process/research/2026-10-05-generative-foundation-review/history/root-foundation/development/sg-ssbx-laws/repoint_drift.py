#!/usr/bin/env python3
"""SG (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections SG changed, after reading the change: python3 -B repoint_drift.py SECTIONS_JSON ID ...
SECTIONS_JSON maps each drifting record id to its changed sections, from the render log."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
WHAT = {
    '## 1. Becoming: one unfolding': 'SG added the paragraphs on where a configuration is lost (Becoming.Junctures) and '
                                     'what a commuting law keeps apart (Becoming.Commuting)',
    '## 3. Knowing and inquiry': 'SG added the item on the liar with a third value (Becoming.Undecided)',
    '## 8. Open programme': 'SG added its records and open items to the "When the course branches" and "What a '
                            'description keeps and loses" rows, a section 8.3 item and a rerun sentence in the '
                            'integration row',
    '## 9. The formal spine': 'SG revised the receipt sentence and counts',
    '## 10. Glossary': 'SG added rows for juncture, keeping and losing, commuting law and undecided',
}
WHAT_ZH = {
    '## 1. Becoming: one unfolding': '第 1 节（SG 加入配置在何处失去、交换的律保持什么分开两段）',
    '## 3. Knowing and inquiry': '第 3 节（SG 加入第三值下的说谎者一条）',
    '## 8. Open programme': '第 8 节（SG 在两行加入记录与开放项，加入第 8.3 节一条与整合行一句重跑）',
    '## 9. The formal spine': '第 9 节（SG 更新回执句与计数）',
    '## 10. Glossary': '第 10 节（SG 加入关节、保持与失去、交换之律、未定各行）',
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
        'en': '19 October 2026, SG (junctures, commuting laws and the third value): THE-THEORY-OF-BECOMING.md re-pointed. '
              'Since this record\'s reviewed hash, the cited text changed only where SG added text: '
              + '; '.join(WHAT[s] for s in secs) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，SG（关节、交换之律与第三值）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在 SG 加文之处改动：'
              + '；'.join(WHAT_ZH[s] for s in secs) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
