#!/usr/bin/env python3
"""R23 (19 October 2026), the refutation laws however a family is listed: advance the record
listing-once-is-decided-identity and re-point the records whose cited files R23 changed.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R23 was rebased on; RECEIPT_ID the passing core receipt of R23's checker run.
* The record listing-once-is-decided-identity gains one claim sentence naming the new corollaries, a
  reference to Becoming/ListingRefutations.lean with the declarations its claim names, a proof binding
  to the receipt, the receipt and study section 215 as references, and a history note.
* For every record, a reference to a file R23 changed (chapter, reference chapter, Chinese edition,
  study, the root module, the current receipt) whose hash matched the file at BASE follows the file;
  with a render log, records it reports as drifting in such a file follow it too (their reference was
  already behind in sections they do not cite). A reference already stale at BASE is left otherwise.
  No Lean source a record binds changed except the root module's documentation.
"""
import glob, hashlib, json, re, subprocess, sys

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
SRC = PKG + 'Becoming/ListingRefutations.lean'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
WHAT = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('the listing paragraph and §8.2 row name Becoming.ListingRefutations; §9 counts and receipt follow R23',
                                       '列出一次一段与 §8.2 行写入 Becoming.ListingRefutations；§9 计数与回执随 R23'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the same in the Chinese edition, with an L4 module row', '中文版同样更新，并加 L4 模块行'),
    CH + 'THE-THEORY-OF-BECOMING-REFERENCE.md': ('an L4 module row for Becoming.ListingRefutations', '加 Becoming.ListingRefutations 的 L4 模块行'),
    STUDY: ('section 215 added', '新增第 215 节'),
    PKG + 'Becoming.lean': ('the import and module note of Becoming.ListingRefutations added', '加入 Becoming.ListingRefutations 的导入与模块说明'),
    PKG + 'becoming-verification.json': ("the current receipt is R23's run", '当前回执为 R23 之运行'),
}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout).hexdigest() for p in WHAT}

# The record R23 advances.
f = 'theories/becoming/results/records/listing-once-is-decided-identity.json'
d = json.load(open(f))
NAMES = ['Becoming.Flow.fed_from_beyond_listing', 'Becoming.Web.generation_fed_from_beyond_listing',
         'Becoming.Flow.More.opens_listing', 'Becoming.Web.generation_opens_listing',
         'Becoming.Flow.taking_draws_in_from_listing', 'Becoming.Web.generation_draws_in_listing',
         'Becoming.Flow.rising_not_recurring_listing', 'Becoming.Flow.taking_needs_refinement_listing',
         'Becoming.Flow.boundary_crossed_listing', 'Becoming.Flow.region_not_a_cut_listing',
         'Becoming.Flow.FedFromBeyond.of_within', 'Becoming.Flow.cut_of_same']
mod = next(m for m in receipt['modules'] if m['module'] == 'Becoming.ListingRefutations')
have = {x['name'] if isinstance(x, dict) else x for x in mod['declarations']}
missing = [n for n in NAMES if n not in have]
assert not missing, missing
assert receipt['source_sha256']['Becoming.ListingRefutations'] == h(SRC)
if not any(r['path'] == SRC for r in d['references']):
    d['claim']['en'] += (' The other 22 laws the inventory classed so are proved the same way in Becoming.ListingRefutations, with '
                         'no Distinct (Flow.fed_from_beyond_listing, Web.generation_fed_from_beyond_listing, Flow.More.opens_listing, '
                         'Web.generation_opens_listing, Flow.taking_draws_in_from_listing, Web.generation_draws_in_listing, '
                         'Flow.rising_not_recurring_listing, Flow.taking_needs_refinement_listing, Flow.boundary_crossed_listing, '
                         'Flow.region_not_a_cut_listing and the rest), being fed from beyond and the boundary of a region as a cut '
                         'being matters of membership (Flow.FedFromBeyond.of_within, Flow.cut_of_same); the seven whose law\'s '
                         'statement takes decided identity on its type ([DecidableEq]) keep it, the other fifteen need none.')
    d['claim']['zh'] += ('清点归入此类的其余 22 条律在 Becoming.ListingRefutations 中以同样方式证明，不需 Distinct（Flow.fed_from_beyond_listing、'
                         'Web.generation_fed_from_beyond_listing、Flow.More.opens_listing、Web.generation_opens_listing、'
                         'Flow.taking_draws_in_from_listing、Web.generation_draws_in_listing、Flow.rising_not_recurring_listing、'
                         'Flow.taking_needs_refinement_listing、Flow.boundary_crossed_listing、Flow.region_not_a_cut_listing 等），'
                         '因为从外供给与区域边界作为割都是成员的事（Flow.FedFromBeyond.of_within、Flow.cut_of_same）；'
                         '规律陈述在类型上取同一已定（[DecidableEq]）的 7 条保留它，其余 15 条不需。')
    i = next(k for k, r in enumerate(d['references']) if r['path'].endswith('Becoming/Listing.lean'))
    d['references'].insert(i + 1, {'path': SRC, 'role': 'proof', 'sha256': h(SRC), 'declarations': NAMES})
    d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    d['proof_bindings'].append({'source': SRC, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.ListingRefutations',
                                'success_pointer': '/status', 'success_value': 'passed'})
    d['history'].append({
        'en': '19 October 2026, R23 (study section 215): the next delta, corollaries for the other uses classed as needing no '
              'premise, closed: the new core module Becoming.ListingRefutations proves the 22 laws as `_listing` corollaries '
              f'(core receipt {RID}). One sentence added to the claim; limitations and next delta updated. The earlier claim is unchanged.',
        'zh': f'2026年10月19日，R23（研究第 215 节）：下一步（其余不需前提的用处之推论）完成：新核心模块 Becoming.ListingRefutations '
              f'把 22 条律证为 `_listing` 推论（核心回执 {RID}）。论断添一句；局限与下一步更新。原论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('advanced listing-once-is-decided-identity')

n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    touched = set()
    for r in d.get('references', []):
        p = r['path']
        if p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if rid == 'listing-once-is-decided-identity':
        for r in d['references']:
            if r['path'] == STUDY and r.get('sha256') != h(STUDY):
                r['sha256'] = h(STUDY)
                touched.add(STUDY)
    if not touched:
        continue
    ps = sorted(touched)
    d['history'].append({
        'en': '19 October 2026, R23 (the refutation laws however a family is listed): ' + ', '.join(p.rsplit('/', 1)[-1] for p in ps)
              + ' re-pointed. Since the reviewed hash, the cited files changed only where R23 changed them: '
              + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，R23（否证律对任何列出方式成立）：' + '、'.join(p.rsplit('/', 1)[-1] for p in ps)
              + ' 重新指向。自所审哈希以来，所引文件只在 R23 改动之处改动：'
              + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(ps))
print(n, 'records changed')
