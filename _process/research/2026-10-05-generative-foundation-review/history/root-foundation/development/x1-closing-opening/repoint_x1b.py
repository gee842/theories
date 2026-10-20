#!/usr/bin/env python3
"""X1b (19 October 2026): re-point the references of records that `make research-render` reports as drifting only
where X1b changed the cited text, after reading the change (the 护闭 texts brought to the exact scope of the juncture
laws): the chapter in sections 1 and 10, the renewal study in section 199.
python3 -B repoint_x1b.py ID:FILE ...  (FILE is the drifting path's file name, as the render reports it; only that
reference is re-pointed, so a record whose other cited text changed elsewhere keeps its reviewed hash there)
A record whose last history entry is X1b's own (every-loss-passes-a-juncture) gets the re-points in that entry."""
import hashlib, json, sys

NOTES = {
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md': (
        'THE-THEORY-OF-BECOMING.md re-pointed. Since this record\'s reviewed hash, the cited text changed only in '
        'section 1 (the D52 reading: keeping is the largest closure keeping s on its course from s) and in section 10 '
        '(the 护闭 row of the crosswalk: every loss passes a juncture where s returns; keeping is the largest on its '
        'course from s), which X1b brought to the exact scope of `loss_passes_juncture` and `keeping_greatest`. Read '
        'before re-pointing. The claim is unchanged.',
        'THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 1 节（D52 读法：保持是在自 s 起的路径上保住 s 的'
        '最大闭）与第 10 节（对照中护闭一行：s 返回时每次失去都经过关节；保持在自 s 起的路径上最大）改动，X1b 使其合于 '
        '`loss_passes_juncture` 与 `keeping_greatest` 的确切范围。重新指向前已读。论断不变。'),
    '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md': (
        'BECOMING-RENEWAL-READING.md re-pointed. Since this record\'s reviewed hash, the cited text changed only in '
        'section 199, whose reading of 护闭 now says that keeping is the largest closure keeping s on its course from s '
        '(`keeping_greatest`), as X1b brought it. Read before re-pointing. The claim is unchanged.',
        'BECOMING-RENEWAL-READING.md 重新指向。自本记录所审哈希以来，所引文字只在第 199 节改动：其护闭读法现说保持是在自 s 起的'
        '路径上保住 s 的最大闭（`keeping_greatest`），由 X1b 改。重新指向前已读。论断不变。'),
}
HASH = {p: hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in NOTES}
BY_ID = {}
for arg in sys.argv[1:]:
    i, name = arg.split(':', 1)
    paths = [p for p in NOTES if p.rsplit('/', 1)[-1] == name]
    assert len(paths) == 1, arg
    BY_ID.setdefault(i, set()).add(paths[0])
for i, drifting in sorted(BY_ID.items()):
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f, encoding='utf-8'))
    moved = []
    for r in d['references']:
        if r['path'] in drifting and r['sha256'] != HASH[r['path']]:
            r['sha256'] = HASH[r['path']]
            moved.append(r['path'])
    assert sorted(moved) == sorted(drifting), (i, moved, drifting)
    en = ' '.join(NOTES[p][0] for p in moved)
    zh = ''.join(NOTES[p][1] for p in moved)
    last = d['history'][-1]
    if last['en'].startswith('19 October 2026, X1b'):
        last['en'] += ' ' + en
        last['zh'] += zh
    else:
        d['history'].append({'en': '19 October 2026, X1b (the 护闭 texts at the exact scope of the juncture laws): ' + en,
                             'zh': '2026年10月19日，X1b（护闭诸文合于关节律的确切范围）：' + zh})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i, ' '.join(p.rsplit('/', 1)[-1] for p in moved))
