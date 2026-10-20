#!/usr/bin/env python3
"""R35b (20 October 2026), the instance and applications ring: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R35b was rebased on; RECEIPT_ID the passing core receipt of R35b's checker run.
Adapted from the rebind of development/r34-evaluative-chain; the logic is that kit's, with the receipt's
declarations read from every pure layer (core, instance, application) and the tables R35b's.

* The seven declarations of Commuting's `namespace Hexagram` section moved, with their full names, to
  Becoming.HexagramCommuting; nothing was removed or renamed.
* Proof bindings to the Lean files R35b changed are rebound to the receipt; references to the files R35b changed
  are re-pointed where they matched BASE, or where the render log reports drift in sections the record cites,
  after reading the change (WHAT says what changed).
* Only records whose declaration lists changed are written here, with a history note saying what moved; the
  hash-only re-points and rebinds of the other records go through tools/research/repoint.py, one log line (E3).
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

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
HERE = os.path.dirname(os.path.abspath(__file__))

LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEANDIR + 'becoming/'
B = PKG + 'Becoming/'
HIST = LEANDIR + 'history/becoming/Becoming/'
BASE_RID = '20261020T005554.047169Z'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
PURE_LAYERS = ('core', 'instance', 'application')
assert not any(v for m in receipt['modules'] if m.get('layer') in PURE_LAYERS for v in m['axiom_dependencies'].values()), 'axiom report not empty'
base_receipt = json.load(open(PKG + 'becoming-checks/' + BASE_RID + '/verification.json'))


def homes(r):
    out = {}
    for m in r['modules']:
        if m.get('layer') not in PURE_LAYERS:
            continue
        for x in m.get('declarations', []):
            out[x['name'] if isinstance(x, dict) else x] = m['module']
    return out


home, home_base = homes(receipt), homes(base_receipt)
path_of = {m: LEANDIR + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}
REMAP = {}
JOINS = {}
FOLDED_INTO = {d + x + '.lean': B + s + '.lean' for d in (B, HIST) for x, s in JOINS.items()}
GONE_FILES = set(FOLDED_INTO)
removed = set(home_base) - set(home)
assert removed == set(REMAP), (sorted(removed - set(REMAP)), sorted(set(REMAP) - removed))
assert all(y in home for y in REMAP.values())
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}
print('moved', len(MOVED), sorted({(home_base[x], home[x]) for x in MOVED}))
SUPERSEDED = set()
R33_RECORDS = set()

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('section 9: the rings (instances and applications), the receipt and the counts follow R35b',
                                       '§9：环（实例与应用）、回执与计数随 R35b'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('section 9: the rings, the receipt and the counts follow R35b', '§9：环、回执与计数随 R35b'),
    STUDY: ('section 228 added', '新增第 228 节'),
    RF + 'THEOREM-CONNECTIVITY.py': ('reports the classes by ring', '按环报告各类'),
    'tools/research/lean_catalogue.py': ("the receipt's instance and application layers form the group becoming-ring", '回执的实例层与应用层组成 becoming-ring 组'),
    PKG + 'Becoming.lean': ('Becoming.HexagramCommuting imported, with its note; the Commuting note no longer states the instance',
                            '导入 Becoming.HexagramCommuting 并加说明；Commuting 的说明不再陈述该实例'),
    PKG + 'README.md': ('three rings: the instances and applications ring added; a row for HexagramCommuting', '三环：新增实例与应用环；HexagramCommuting 一行'),
    PKG + 'README.zh.md': ('three rings: the instances and applications ring added', '三环：新增实例与应用环'),
    PKG + 'check_becoming.py': ("INSTANCES and APPLICATIONS out of CORE, held to the same conditions, with an import-direction check; the receipt names each module's ring as its layer",
                                'INSTANCES 与 APPLICATIONS 移出 CORE，受同样条件约束，并检查导入方向；回执以各模块的环为其层'),
    PKG + 'becoming-verification.json': ("the current receipt is R35b's run", '当前回执为 R35b 之运行'),
}
LEAN_WHAT = {
    'Commuting.lean': ('the namespace Hexagram section (complement_moves, waxWane_apart, waxWane_halfway, wane_breaks, flip_complement, changes_symmetric, changes_mirror_apart) moved unchanged to HexagramCommuting; no longer imports Hexagrams; the general laws unchanged',
                       'namespace Hexagram 一节（complement_moves、waxWane_apart、waxWane_halfway、wane_breaks、flip_complement、changes_symmetric、changes_mirror_apart）原样移到 HexagramCommuting；不再导入 Hexagrams；一般规律不变'),
    'HexagramCommuting.lean': ("new: Commuting's instance in the Changes, moved unchanged", '新增：Commuting 在《周易》中的实例，原样移入'),
    'HexagramLaws.lean': ('imports HexagramCommuting instead of Commuting; statements unchanged', '改导入 HexagramCommuting 而非 Commuting；陈述不变'),
}
DEFAULT_LEAN = ('an import only; statements unchanged', '只改导入；陈述不变')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


changed = subprocess.run(['git', 'diff', '--name-only', BASE, '--'], capture_output=True, text=True, check=True).stdout.split()
LEAN = {p for p in changed if p.startswith(B) and p.endswith('.lean') and p not in GONE_FILES}
print('changed Lean', sorted(p.rsplit('/', 1)[-1] for p in LEAN))
WHAT = dict(DOCS)
for p in LEAN:
    WHAT[p] = LEAN_WHAT.get(p.rsplit('/', 1)[-1], DEFAULT_LEAN)
base = {}
for p in WHAT:
    out = subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True)
    base[p] = hashlib.sha256(out.stdout).hexdigest() if out.returncode == 0 else None


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


def short(p):
    return p.rsplit('/', 1)[-1]


P = 'Becoming.'


def bare(x):
    return x.split(P, 1)[1] if x.startswith(P) else x


def remap(names, replaced):
    out = []
    for x in names:
        y = REMAP.get(x, x)
        if y != x:
            replaced.append((x, y))
        if y not in out:
            out.append(y)
    return out


def strings(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k == 'history':
                continue
            if isinstance(v, str):
                yield x, k
            else:
                yield from strings(v)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            if isinstance(v, str):
                yield x, i
            else:
                yield from strings(v)


n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = d['id']
    light = rid in SUPERSEDED
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by = {r['path']: r for r in refs}
    moved, replaced = [], []
    for law in ([] if light else d.get('laws', []) or []):
        if isinstance(law, dict) and law.get('declarations'):
            law['declarations'] = remap(law['declarations'], replaced)
    if isinstance(d.get('aliases'), list):
        d['aliases'] = remap(d['aliases'], replaced)

    added, filed = [], set()

    def ref_for(path, after):
        if path not in by:
            by[path] = {'path': path, 'role': 'proof', 'sha256': h(path), 'declarations': []}
            added.append(path)
            refs.insert(refs.index(after) + 1 if after in refs else len(refs), by[path])
        return by[path]

    for r in list(refs):
        if not r.get('declarations') or light:
            continue
        keep = []
        for x in r['declarations']:
            y = REMAP.get(x, x)
            if y != x:
                replaced.append((x, y))
            target = path_of[home[y]] if y in home else r['path']
            if target != r['path'] and (y != x or x in MOVED or r['path'] in GONE_FILES):
                t = ref_for(target, r)
                t.setdefault('declarations', [])
                if y not in t['declarations']:
                    t['declarations'].append(y)
                filed.add(target)
                if y == x:
                    moved.append((x, r['path'], target))
            elif y not in keep:
                keep.append(y)
        r['declarations'] = keep
    canon = d.get('canonical_source')
    new_canon = None
    if canon in GONE_FILES and not light:
        new_canon = FOLDED_INTO[canon]
        d['canonical_source'] = new_canon
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if d.get('proof_bindings') and not light:
        for path in sorted(filed):
            if path not in bound and by[path].get('declarations'):
                d['proof_bindings'].append(binding(path))
                bound.add(path)
        d['proof_bindings'] = [b for b in d['proof_bindings'] if b['source'] not in GONE_FILES]
    rebound, touched = [], set()
    for b in d.get('proof_bindings', []):
        if b['source'] in LEAN and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
            b['receipt'] = RECEIPT
            rebound.append(short(b['source']))
    for r in refs:
        p = r['path']
        if p in GONE_FILES:
            continue
        if p in LEAN and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ()) or rid in R33_RECORDS) \
                and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    for r in list(refs):
        if light:
            break
        if r['path'] in GONE_FILES:
            assert not r.get('declarations'), (rid, r['path'])
            refs.remove(r)
        elif r['role'] == 'proof' and not r.get('declarations') and any(m[1] == r['path'] for m in moved) \
                and r['path'] != d.get('canonical_source') \
                and not any(b['source'] == r['path'] for b in d.get('proof_bindings', [])):
            refs.remove(r)
    paths_fixed = []
    for c, k in ([] if light else list(strings(d))):
        if c[k] in GONE_FILES:
            new = FOLDED_INTO[c[k]]
            paths_fixed.append((short(c[k]), short(new)))
            c[k] = new
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before or not moved:
        # Hash-only re-points and rebinds are bookkeeping, logged once by tools/research/repoint.py (E3).
        continue
    en = "20 October 2026, R35b (the instance and applications ring: the Changes and place/transition nets as instances, six leaves as applications, both held to the core's conditions and outside it by direction):"
    zh = '2026年10月20日，R35b（实例与应用环：《周易》与位置/迁移网为实例，六个叶子模块为应用，二者受核心同样的条件约束，按方向在核心之外）：'
    parts_en, parts_zh = [], []
    mv = sorted({(bare(x), short(a), short(c)) for x, a, c in moved})
    if mv:
        groups = {}
        for x, a, c in mv:
            groups.setdefault((a, c), []).append(x)
        parts_en.append('Moved with their full names: ' + '; '.join(f'from {a} to {c}, ' + ', '.join(xs) for (a, c), xs in sorted(groups.items())) + '.')
        parts_zh.append('连同完整名称移动：' + '；'.join(f'从 {a} 到 {c}：' + '、'.join(xs) for (a, c), xs in sorted(groups.items())) + '。')
    rp = sorted({(bare(x), bare(y)) for x, y in replaced})
    if rp:
        raise AssertionError(('R35b renames nothing', rp))
    if new_canon:
        parts_en.append(f'The canonical source {short(canon)} was joined into {short(new_canon)}; it is now {short(new_canon)}.')
        parts_zh.append(f'规范来源 {short(canon)} 已并入 {short(new_canon)}，现为 {short(new_canon)}。')
    if rebound:
        parts_en.append(f'Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.')
        parts_zh.append(f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。')
    pf = sorted(set(paths_fixed))
    if pf:
        parts_en.append('The evidence and counterexample paths that named ' + '; '.join(f'{a} name {b}' for a, b in pf) + ' (the module it was joined into).')
        parts_zh.append('提到 ' + '；'.join(f'{a} 的证据与反例路径改提 {b}' for a, b in pf) + '（它所并入的模块）。')
    ps = sorted(touched)
    if ps:
        parts_en.append('Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.')
        parts_zh.append('读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。')
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R35b'):
        last['en'] = last['en'].rstrip() + ' Also: ' + ' '.join(parts_en)
        last['zh'] = last['zh'].rstrip() + '另：' + ''.join(parts_zh)
    else:
        d.setdefault('history', []).append({'en': en + ' ' + ' '.join(parts_en) + ' The claim is unchanged.',
                                            'zh': zh + ''.join(parts_zh) + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
