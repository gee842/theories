#!/usr/bin/env python3
"""R22 (19 October 2026), the nineteenth review's names, adapted from R21's kit: rebind and re-point the result records after reading
the change. Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R22 was made on; RECEIPT_ID the passing core receipt of R22's checker run. A reference to a
file R22 changed (renamed, or whose names it rewrote) whose hash matched the file at BASE follows the file; a proof
binding to one of the three Lean files R22 changed is rebound to the receipt; the receipt is added as a reference.
With a render log, records drifting in a file R22 changed are re-pointed too. A history note says what changed."""
import glob, hashlib, json, subprocess, sys

BASE, RID = sys.argv[1], sys.argv[2]
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
NOTE = ('names only (nineteenth review N1, N2; table in development/r22-names/RENAME-TABLE.json)', '只改名称（第十九次审查 N1、N2；对照表见 development/r22-names/RENAME-TABLE.json）')
WHAT = {p: NOTE for p in [
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md',
    'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md', 'theories/becoming/OPENING.md',
    DC + '.md', DC + '.zh.md', PKG + 'becoming-verification.json', PKG + 'README.md', PKG + 'README.zh.md', PKG + 'Becoming.lean',
    L + 'LoopReturn.lean', L + 'PatternPassing.lean', L + 'Relevance.lean',
    '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-UNIFICATION-PLAN.md',
    '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-UNIFICATION-PLAN.zh.md']}
OLD_PATH = {L + 'LoopReturn.lean': L + 'Widening.lean', L + 'PatternPassing.lean': L + 'Passing.lean'}
LEANS = {p for p in WHAT if p.endswith('.lean')}
CLAIM = {}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{OLD_PATH.get(p, p)}'], capture_output=True).stdout).hexdigest() for p in WHAT}
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
        'en': '19 October 2026, R22 (the names of the nineteenth review): ' + ', '.join(p.rsplit('/', 1)[-1] for p in ps)
              + (f' re-pointed{", proof bindings rebound to core receipt " + RID if rebound else ""}. Since the reviewed hash, the cited files changed only where R22 renamed: ')
              + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '. Read before re-pointing. '
              + CLAIM.get(rid, ('The claim is unchanged.',))[0],
        'zh': '2026年10月19日，R22（第十九次审查的名称）：' + '、'.join(p.rsplit('/', 1)[-1] for p in ps)
              + ' 重新指向' + ('，证明绑定改到核心回执 ' + RID if rebound else '') + '。自所审哈希以来，所引文件只在 R22 改名之处改动：'
              + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。重新指向前已读。'
              + CLAIM.get(rid, (None, '论断不变。'))[1]})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(ps), 'rebound' if rebound else '')
print(n, 'records changed')
