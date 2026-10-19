#!/usr/bin/env python3
"""M4 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
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
        'en': "19 October 2026, M4 (Becoming.Rejoining): THE-THEORY-OF-BECOMING.md re-pointed. Since this record's "
              'reviewed hash, the cited text changed only in section 8 (the open programme): M4 revised the "Selection, '
              'causes and experiment" row of section 8.2 (where two courses rejoin stated, its record linked, the open item '
              'restated as which law closes rather than widens a difference) and extended the section 7 line of the '
              'open readings in section 8.4. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，M4（Becoming.Rejoining）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8 节'
              '（开放纲领）改动：M4 修订第 8.2 节“选择、原因与实验”行（陈述了两个进程在何处重合，链接其记录，开放项改述为哪个律闭合而非扩大差别），'
              '并扩展第 8.4 节开放读法中第 7 节一行。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
