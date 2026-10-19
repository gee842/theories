#!/usr/bin/env python3
"""X1b (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections 1 and 10, after reading the change (the 护闭 texts brought to the exact scope of the juncture laws):
python3 -B repoint_x1b.py ID ...
A record whose last history entry is X1b's own (every-loss-passes-a-juncture) gets the re-point in that entry."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
h = hashlib.sha256(open(C, 'rb').read()).hexdigest()
EN = ('THE-THEORY-OF-BECOMING.md re-pointed. Since this record\'s reviewed hash, the cited text changed only in section 1 '
      '(the D52 reading: keeping is the largest closure keeping s on its course from s) and in section 10 (the 护闭 row of '
      'the crosswalk: every loss passes a juncture where s returns; keeping is the largest on its course from s), which '
      'X1b brought to the exact scope of `loss_passes_juncture` and `keeping_greatest`. Read before re-pointing. '
      'The claim is unchanged.')
ZH = ('THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 1 节（D52 读法：保持是在自 s 起的路径上保住 s 的最大闭）'
      '与第 10 节（对照中护闭一行：s 返回时每次失去都经过关节；保持在自 s 起的路径上最大）改动，X1b 使其合于 '
      '`loss_passes_juncture` 与 `keeping_greatest` 的确切范围。重新指向前已读。论断不变。')
for i in sys.argv[1:]:
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f, encoding='utf-8'))
    n = 0
    for r in d['references']:
        if r['path'] == C and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (i, n)
    last = d['history'][-1]
    if last['en'].startswith('19 October 2026, X1b'):
        last['en'] += ' ' + EN
        last['zh'] += ZH
    else:
        d['history'].append({'en': '19 October 2026, X1b (the 护闭 texts at the exact scope of the juncture laws): ' + EN,
                             'zh': '2026年10月19日，X1b（护闭诸文合于关节律的确切范围）：' + ZH})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
