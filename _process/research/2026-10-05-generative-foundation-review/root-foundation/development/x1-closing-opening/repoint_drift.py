#!/usr/bin/env python3
"""X1 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections 8 and 10 (the open programme and the glossary), after reading the change:
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
        'en': '19 October 2026, X1 (the crosswalk of closing and opening, D49): THE-THEORY-OF-BECOMING.md re-pointed. Since '
              "this record's reviewed hash, the cited text changed only in section 8 (the open programme), where X1 added "
              'the reading D49 and the range D1–D49, and in section 10 (the glossary), where X1 added the subsection '
              '"Closing and opening: a crosswalk" and a clause to the corpus rows 开 and 闭 / 成闭. Read before re-pointing. '
              'The claim is unchanged.',
        'zh': '2026年10月19日，X1（闭与开的对照，D49）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8 节'
              '（开放纲领）与第 10 节（术语表）改动：X1 在第 8 节加入读法 D49 与编号范围 D1–D49，在第 10 节加入“Closing and opening: '
              'a crosswalk”一小节，并在语料对照的“开”与“闭／成闭”两行各加一句。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
