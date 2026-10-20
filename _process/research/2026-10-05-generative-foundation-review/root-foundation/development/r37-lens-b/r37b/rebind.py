#!/usr/bin/env python3
"""R37b (20 October 2026), B11 of the twentieth review: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R37b was built on; RECEIPT_ID the passing core receipt of R37b's checker run.
The logic is that of development/r37-lens-b/rebind.py (itself r35b's), the tables R37b's
(RENAME-TABLE.json beside this file: the helpers the census tables leave unused, each with the name
that states its use now). Declarations moved under their full names (into CensusTable, into Counting)
are filed under their new module's file.

* Only records whose declaration lists changed are written here, with a history note; the hash-only
  re-points and rebinds of the other records go through tools/research/repoint.py, one log line (E3).
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
BASE_RID = '20261020T051144.879480Z'
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
TABLE = json.load(open(os.path.join(HERE, 'RENAME-TABLE.json')))
REMAP = {x['old']: x['kept'] for x in TABLE['removed'] if x['kept']}
REMAP.update({x['old']: x['new'] for x in TABLE['renamed']})
NONE = {x['old'] for x in TABLE['removed'] if not x['kept']}
JOINS = {}
FOLDED_INTO = {d + x + '.lean': B + s + '.lean' for d in (B, HIST) for x, s in JOINS.items()}
GONE_FILES = set(FOLDED_INTO)
removed = set(home_base) - set(home)
CTORS = set()
assert removed == (set(REMAP) | NONE) - CTORS, (sorted(removed - set(REMAP) - NONE), sorted((set(REMAP) | NONE) - CTORS - removed))
assert all(y in home for x, y in REMAP.items() if x not in CTORS), [y for x, y in REMAP.items() if x not in CTORS and y not in home]
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}
print('moved', len(MOVED), sorted({(home_base[x], home[x]) for x in MOVED}))
SUPERSEDED = set()
R33_RECORDS = set()

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('section 9: the receipt, the counts, the layers and the connectivity follow R37b',
                                       '§9：回执、计数、层与连通性随 R37b'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('section 9: the receipt and the counts follow R37b', '§9：回执与计数随 R37b'),
    STUDY: ('section 230 added', '新增第 230 节'),
    RF + 'THEOREM-CONNECTIVITY.md': ('a paragraph on R37b added to section 11', '第 11 节新增关于 R37b 的一段'),
    RF + 'THEOREM-CONNECTIVITY.json': ("measured on R37b's tree", '在 R37b 树上测量'),
    RF + 'THEOREM-CONNECTIVITY-APART.json': ("the register follows R37b's removals", '登记随 R37b 的删除'),
    PKG + 'Becoming.lean': ('Becoming.CensusTable imported, with its note; the notes of CensusCounts and CensusBinding say they read the table',
                            '导入 Becoming.CensusTable 并加说明；CensusCounts 与 CensusBinding 的说明写明它们读该表'),
    PKG + 'README.md': ('the module table, generated, has a row for CensusTable', '模块表（生成）新增 CensusTable 一行'),
    PKG + 'README.zh.md': ('names follow R37b', '名称随 R37b'),
    PKG + 'check_becoming.py': ('CORE adds Becoming.CensusTable; no logic changed', 'CORE 加 Becoming.CensusTable；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R37b's run", '当前回执为 R37b 之运行'),
}
LEAN_WHAT = {
    'CensusTable.lean': ('new: one census table for any listing (counted soundness and a witness lemma give the law with counts as relations and with the marks of a procedure), agreeing listings, and the census of activity moved here from CensusCounts and Counting with its counts',
                         '新增：任一列举的一个普查表（计数式的可靠性与见证引理给出以关系计数和以程序标记两种形式的规律）、一致的列举，以及从 CensusCounts 与 Counting 移入的活动普查及其计数'),
    'Counting.lean': ('each law of counting a census table, from a counted soundness and a witness lemma; the counted binding steps moved here from CensusCounts and CensusBinding; statements unchanged',
                      '每条计数规律为一个普查表，由计数式的可靠性与见证引理给出；计数式的约束步骤从 CensusCounts 与 CensusBinding 移入；陈述不变'),
    'CensusCounts.lean': ('each counted law the census table of its decided form in Counting; the census of activity moved to CensusTable, the binding steps to Counting; helpers left unused removed; kept statements unchanged',
                          '每条计数式规律为 Counting 中其判定形式的普查表；活动普查移至 CensusTable，约束步骤移至 Counting；不再使用的辅助引理删去；保留的陈述不变'),
    'CensusBinding.lean': ('each counted binding law the census table of its decided form in Counting; the binding steps moved to Counting; kept statements unchanged',
                           '每条计数式约束规律为 Counting 中其判定形式的普查表；约束步骤移至 Counting；保留的陈述不变'),
    'Standing.lean': ('what stands and what depends as census tables of their listings, with counted soundness and witness lemmas; ceasings_congr and comings_congr moved to CensusTable; helpers left unused removed; kept statements unchanged',
                      '所立与所依作为其列举的普查表，附计数式的可靠性与见证引理；ceasings_congr 与 comings_congr 移至 CensusTable；不再使用的辅助引理删去；保留的陈述不变'),
}
DEFAULT_LEAN = ('statements unchanged', '陈述不变')


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
            assert x not in NONE, (rid, x)
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
    if json.dumps(d, ensure_ascii=False) == before or not (moved or replaced):
        # Hash-only re-points and rebinds are bookkeeping, logged once by tools/research/repoint.py (E3).
        continue
    en = '20 October 2026, R37b (B11 of the twentieth review: one census table for any listing, the laws of counting what is active, what stands and what depends its instances, the counted and decided forms from one soundness and one witness):'
    zh = '2026年10月20日，R37b（第二十次评审的 B11：任一列举的一个普查表，计数所活动、所立与所依的规律为其实例，计数式与判定式由一个可靠性与一个见证给出）：'
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
        parts_en.append('Replaced by the name stating it now, the same statement or its general form, or renamed (development/r37-lens-b/r37b/RENAME-TABLE.json): ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.')
        parts_zh.append('以现在陈述它的名称取代（陈述相同或为其一般形式）或改名（development/r37-lens-b/r37b/RENAME-TABLE.json）：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。')
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
        by_what = {}
        for p in ps:
            by_what.setdefault(WHAT[p], []).append(short(p))
        parts_en.append('Re-pointed after reading the change: ' + '; '.join(', '.join(fs) + ': ' + w[0] for w, fs in by_what.items()) + '.')
        parts_zh.append('读过改动后重新指向：' + '；'.join('、'.join(fs) + '：' + w[1] for w, fs in by_what.items()) + '。')
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R37b'):
        last['en'] = last['en'].rstrip() + ' Also: ' + ' '.join(parts_en)
        last['zh'] = last['zh'].rstrip() + '另：' + ''.join(parts_zh)
    else:
        d.setdefault('history', []).append({'en': en + ' ' + ' '.join(parts_en) + ' The claim is unchanged.',
                                            'zh': zh + ''.join(parts_zh) + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
