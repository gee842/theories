#!/usr/bin/env python3
"""E1 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting only
in section 0 (the premise card) or section 8 (the open programme), after reading the change:
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
        'en': '19 October 2026, E1 (premises read off one exchange): THE-THEORY-OF-BECOMING.md re-pointed. Since this '
              "record's reviewed hash, the cited text changed only in section 0 (premise card C) or section 8 (the open "
              'programme): E1 rewrote card C\'s bullet on what the independence measures, the necessity row of section '
              '8.1, and added a sentence and three records to the section 8.2 row on one relational start. Read before '
              're-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，E1（从一次交换读出的前提）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 0 节'
              '（前提卡 C）或第 8 节（开放纲领）改动：E1 重写了卡 C 关于独立性度量什么的条目、第 8.1 节的必然性一行，并在第 8.2 节关于从关系'
              '开始的一行加入一句与三个记录。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
