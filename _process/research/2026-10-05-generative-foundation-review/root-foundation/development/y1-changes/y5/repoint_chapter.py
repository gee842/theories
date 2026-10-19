#!/usr/bin/env python3
"""Y5: re-point the reference to the chapter on the 易传 of the three records whose statement it is beside Y1's
(place-relations-in-context, hexagram-world-laws, fixed-places-and-sole-lines), after reading the change. Their
reference was already stale at the landing base (the U5 follow-up regenerated the chapter's passage table for 非覆即變
and left it), so rehash_refs.py leaves it; Y5's opening paragraph, which these records cite, names the new module and
the new counts. The claims are unchanged.
usage (from the landing checkout's root, after make_record.py): python3 -B repoint_chapter.py"""
import hashlib, json

p = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
cur = hashlib.sha256(open(p, 'rb').read()).hexdigest()
for rid in ('place-relations-in-context', 'hexagram-world-laws', 'fixed-places-and-sole-lines'):
    f = f'theories/becoming/results/records/{rid}.json'
    d = json.load(open(f, encoding='utf-8'))
    refs = [r for r in d['references'] if r['path'] == p and r['sha256'] != cur]
    if not refs:
        print(rid, 'nothing to re-point')
        continue
    for r in refs:
        r['sha256'] = cur
    d['history'].append({
        'en': '19 October 2026, Y5 (Becoming.HexagramSequences): YI-ZHUAN-AND-BECOMING.md re-pointed after reading the '
              'change (the opening names the fifth module, Becoming.HexagramSequences, and counts 90 passages; section 2 '
              'gains a subsection on the arrangements of the 傳, section 5 points, section 7 a reading line, and section 8 '
              'corrects the claim that the order is the orbit of no law; the passage table holds two more passages and '
              'the U5 follow-up\'s 非覆即變). The claim is unchanged.',
        'zh': '2026年10月19日，Y5（Becoming.HexagramSequences）：读过改动后，YI-ZHUAN-AND-BECOMING.md 重新指向（开篇列第五个模块 '
              'Becoming.HexagramSequences，计 90 段；第 2 节增传中诸排列一小节，第 5 节增要点，第 7 节增一条读法，第 8 节更正“卦序不是任何律的'
              '轨道”之说；对应表增两段，并含 U5 后续对非覆即變的改动）。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(rid, 're-pointed', len(refs))
