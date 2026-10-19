#!/usr/bin/env python3
"""R21 (19 October 2026), the nineteenth review's fix list: rebind and re-point the result records after reading
the change. Usage (from the checkout root): python3 -B repoint_drift.py BASE RECEIPT_ID

BASE is the main commit R21 was rebased on; RECEIPT_ID the passing core receipt of R21's checker run.
For every record, a reference to a file R21 changed whose hash matched the file at BASE follows the file; a proof
binding to one of the twelve Lean files whose documentation R21 changed is rebound to the receipt (the receipt's
hash of the source must be the current one), and the receipt is added as a reference. A reference that was
already stale at BASE is left as it was. A history note says what changed; two records whose claim text R21
corrected (nineteenth review O1, O4) say so."""
import glob, hashlib, json, subprocess, sys

BASE, RID = sys.argv[1], sys.argv[2]
# Optional third argument: a `make research-render` log. Records it reports as drifting in a file R21 changed,
# whose reference was already behind BASE in sections they do not cite, are re-pointed too.
DRIFT = {}
if len(sys.argv) > 3:
    _log = open(sys.argv[3]).read()
    _dec = json.JSONDecoder()
    for _k in range(len(_log)):
        if _log[_k] == '{':
            try:
                _o, _ = _dec.raw_decode(_log[_k:])
            except ValueError:
                continue
            if isinstance(_o, dict) and 'source_drift' in _o:
                for _x in _o['source_drift']:
                    DRIFT.setdefault(_x['path'], set()).add(_x['id'])
                break
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
L = PKG + 'Becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
DC = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES'
DOC = ('documentation only (no name, statement or proof changed): ', '只改说明（名称、陈述与证明不变）：')
WHAT = {
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md': (
        'the fixes of the nineteenth review (E1–E4, O1–O8, L2, L3, P1, P4–P8, P11): wording brought to what the Lean '
        'states, readings labelled with their decisions, §8.8 and the §9 roots, counts and receipt updated',
        '第十九次审查的修正：措辞对齐 Lean 所陈述的，读法标上其决定，§8.8 与 §9 的根、计数与回执更新'),
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md': (
        'the same fixes in the Chinese edition, and its §9 receipt paragraph regenerated (P2)', '中文版的同样修正，§9 回执段重写（P2）'),
    'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md': (
        'the conditions of the laws read for 生生之謂易 named (O2)', '生生之謂易所读诸律的条件写明（O2）'),
    DC + '.md': ('dated restatements in current terms (E5, O2); the original decisions kept', '以现行用语作出的注明日期的重述（E5、O2）；原决定保留'),
    DC + '.zh.md': ('the same restatements in Chinese', '同样的重述（中文）'),
    PKG + 'becoming-verification.json': ('the current receipt is R21\'s run', '当前回执为 R21 之运行'),
}
for m, en, zh in [
    ('CourseWorlds', 'readings labelled D43; the attaining law named as the carrying law, which is not gainless', '读法标为 D43；达到者注明为携带律，它不是无增益的'),
    ('Frequency', 'readings labelled D43', '读法标为 D43'), ('Interleavings', 'reading labelled D43', '读法标为 D43'),
    ('Observation', 'readings labelled D43', '读法标为 D43'), ('Onward', 'readings labelled D43', '读法标为 D43'),
    ('Remainder', 'readings labelled D43', '读法标为 D43'), ('Runs', 'readings labelled D43', '读法标为 D43'),
    ('Tail', 'readings labelled D43', '读法标为 D43'), ('Propagation', 'readings labelled D39', '读法标为 D39'),
    ('ProfileReach', 'significance stated with no valence', '意义注明不带正负'),
    ('JointKeeping', 'the kernel conjunct stated at the starting configuration', '核心合取注明在起始构形'),
    ('Cuts', "the bypass stated for a directed link (target within the source's closure)", '绕行按有向联系陈述（终点在起点的闭包之内）')]:
    WHAT[L + m + '.lean'] = (DOC[0] + en, DOC[1] + zh)
LEANS = {p for p in WHAT if p.endswith('.lean')}
CLAIM = {
    'a-pattern-lasts-through-passing': ('The statement and law 1 were corrected (nineteenth review O1): `Web.begins_within` is in double-negation form, so they now say that no d consecutive steps pass without a carrier beginning.',
                                        '陈述与第一条律已更正（第十九次审查 O1）：`Web.begins_within` 是双重否定的形式，所以现在说不会连续 d 步都没有承载者开始。'),
    'conditions-kept-together': ('Law 4 was corrected (nineteenth review O4): the kernel conjunct is stated at the starting configuration.',
                                 '第四条律已更正（第十九次审查 O4）：核心合取陈述于起始构形。'),
}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout).hexdigest() for p in WHAT}
module_of = {'experiments/integrated-correction/general-framework/generative-basis/lean/' + p: m for m, p in receipt['source_paths'].items()}
n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    touched = set()
    rebound = False
    for b in d.get('proof_bindings', []):
        if b['source'] in LEANS and b['receipt'] != RECEIPT and base[b['source']] != h(b['source']):
            old = json.load(open(b['receipt'])).get('source_sha256', {}).get(module_of[b['source']])
            if old != h(b['source']):
                assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
                b['receipt'] = RECEIPT
                touched.add(b['source'])
                rebound = True
    refs = d.get('references', [])
    for r in refs:
        p = r['path']
        if p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if rebound and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if not touched:
        continue
    ps = sorted(touched)
    d['history'].append({
        'en': '19 October 2026, R21 (the nineteenth review\'s fix list): ' + ', '.join(p.rsplit('/', 1)[-1] for p in ps)
              + (f' re-pointed{", proof bindings rebound to core receipt " + RID if rebound else ""}. Since the reviewed hash, the cited files changed only where R21 changed them: ')
              + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '. Read before re-pointing. '
              + CLAIM.get(rid, ('The claim is unchanged.',))[0],
        'zh': '2026年10月19日，R21（第十九次审查的修正清单）：' + '、'.join(p.rsplit('/', 1)[-1] for p in ps)
              + ' 重新指向' + ('，证明绑定改到核心回执 ' + RID if rebound else '') + '。自所审哈希以来，所引文件只在 R21 改动之处改动：'
              + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。重新指向前已读。'
              + CLAIM.get(rid, (None, '论断不变。'))[1]})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(ps), 'rebound' if rebound else '')
print(n, 'records changed')
