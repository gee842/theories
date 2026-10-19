#!/usr/bin/env python3
"""R21 (19 October 2026): re-point the references of records that `make research-render` reports as drifting only in
files R21 changed, after reading the change. Usage: python3 -B repoint_drift.py RENDER_LOG
RENDER_LOG is the output of `make research-render`; every drifting path must be one R21 changed, or the script stops."""
import hashlib, json, sys

L = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
DC = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
DOC = ('the module documentation or docstrings only (no statement, proof or name changed): ', '只改模块说明或文档字符串（陈述、证明与名称不变）：')
WHAT = {
    CH: ('the fixes of the nineteenth review (E1–E4, O1–O8, L2, L3, P4–P8, P11): wording brought to what the Lean states, '
         'readings labelled with their decisions, §8.8 updated', '第十九次审查的修正（E1–E4、O1–O8、L2、L3、P4–P8、P11）：措辞对齐 Lean 所陈述的，读法标上其决定，§8.8 更新'),
    DC: ('dated restatements in current terms (nineteenth review E5, O2); the original decisions kept', '以现行用语作出的注明日期的重述（第十九次审查 E5、O2）；原决定保留'),
}
for m, en, zh in [
    ('CourseWorlds', 'readings labelled D43; the attaining law named as the carrying law, which is not gainless', '读法标为 D43；达到者注明为携带律，它不是无增益的'),
    ('Frequency', 'readings labelled D43', '读法标为 D43'), ('Interleavings', 'reading labelled D43', '读法标为 D43'),
    ('Observation', 'readings labelled D43', '读法标为 D43'), ('Onward', 'readings labelled D43', '读法标为 D43'),
    ('Remainder', 'readings labelled D43', '读法标为 D43'), ('Runs', 'readings labelled D43', '读法标为 D43'),
    ('Tail', 'readings labelled D43', '读法标为 D43'), ('Propagation', 'readings labelled D39', '读法标为 D39'),
    ('ProfileReach', 'significance stated with no valence', '意义注明不带正负'),
    ('JointKeeping', 'the kernel conjunct stated at the starting configuration', '核心合取注明在起始构形'),
    ('Cuts', 'the bypass stated for a directed link (target within the source\'s closure)', '绕行按有向联系陈述（终点在起点的闭包之内）')]:
    WHAT[L + m + '.lean'] = (DOC[0] + en, DOC[1] + zh)

CLAIM = {
    'a-pattern-lasts-through-passing': ('The statement and law 1 were corrected (nineteenth review O1): `Web.begins_within` is in double-negation form, so they now say that no d consecutive steps pass without a carrier beginning.',
                                        '陈述与第一条律已更正（第十九次审查 O1）：`Web.begins_within` 是双重否定的形式，所以现在说不会连续 d 步都没有承载者开始。'),
    'conditions-kept-together': ('Law 4 was corrected (nineteenth review O4): the kernel conjunct is stated at the starting configuration.',
                                 '第四条律已更正（第十九次审查 O4）：核心合取陈述于起始构形。'),
}
log = open(sys.argv[1]).read()
dec = json.JSONDecoder()
for k in range(len(log)):
    if log[k] == '{':
        try:
            o, _ = dec.raw_decode(log[k:])
        except ValueError:
            continue
        if isinstance(o, dict) and 'source_drift' in o:
            break
drift = {}
for x in o['source_drift']:
    assert x['path'] in WHAT, ('drift outside R21', x['id'], x['path'])
    drift.setdefault(x['id'], set()).add(x['path'])
for i, paths in sorted(drift.items()):
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f))
    for p in paths:
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        n = 0
        for r in d['references']:
            if r['path'] == p and r['sha256'] != h:
                r['sha256'] = h
                n += 1
        assert n >= 1, (i, p)
    d['history'].append({
        'en': '19 October 2026, R21 (the nineteenth review\'s fix list): ' + ', '.join(p.split('/')[-1] for p in sorted(paths))
              + ' re-pointed. Since this record\'s reviewed hash, the cited files changed only where R21 changed them: '
              + '; '.join(p.split('/')[-1] + ', ' + WHAT[p][0] for p in sorted(paths)) + '. Read before re-pointing. ' + CLAIM.get(i, ('The claim is unchanged.',))[0],
        'zh': '2026年10月19日，R21（第十九次审查的修正清单）：' + '、'.join(p.split('/')[-1] for p in sorted(paths))
              + ' 重新指向。自本记录所审哈希以来，所引文件只在 R21 改动之处改动：'
              + '；'.join(p.split('/')[-1] + '，' + WHAT[p][1] for p in sorted(paths)) + '。重新指向前已读。' + CLAIM.get(i, (None, '论断不变。'))[1]})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i, len(paths))
