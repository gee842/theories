#!/usr/bin/env python3
"""R37 (20 October 2026), lens B of the twentieth review (B14, B4, B6): rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R37 was rebased on; RECEIPT_ID the passing core receipt of R37's checker run.
Adapted from the rebind of development/r35b-ring; the logic is that kit's, the tables R37's
(RENAME-TABLE.json: removed with the name kept, renamed, moved).

* A removed or renamed declaration takes the name it has now in every declaration list; one moved to
  another module (into Prelude, Change, Weighted, Roles or Likeness) is filed under that module's file.
  `CrossSituational.distinct_iff` was removed with no replacement (with one `Distinct` it states
  `Distinct l ↔ Distinct l`); a record citing it would fail the assertion below.
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
BASE_RID = '20261020T045544.667431Z'
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
# The receipt lists no constructors, so the renamed constructors (JointTest's, the relay members') are in the
# table and not among the receipt's removals.
CTORS = {x for x in REMAP if x.rsplit('.', 2)[-2] in ('JointTest', 'Member')}
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
    CH + 'THE-THEORY-OF-BECOMING.md': ('section 9: the receipt, the counts, the layers and the connectivity follow R37',
                                       '§9：回执、计数、层与连通性随 R37'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('section 9: the receipt and the counts follow R37', '§9：回执与计数随 R37'),
    STUDY: ('section 229 added', '新增第 229 节'),
    RF + 'THEOREM-CONNECTIVITY.md': ('a paragraph on R37 added to section 11', '第 11 节新增关于 R37 的一段'),
    RF + 'THEOREM-CONNECTIVITY.json': ("measured on R37's tree", '在 R37 树上测量'),
    RF + 'THEOREM-CONNECTIVITY-APART.json': ("the register follows R37's removals", '登记随 R37 的删除'),
    PKG + 'Becoming.lean': ('Becoming.Witnesses imported, with its note; a note for HexagramCommuting', '导入 Becoming.Witnesses 并加说明；HexagramCommuting 加说明'),
    PKG + 'README.md': ('the module table, generated, has a row for Witnesses; names follow R37', '模块表（生成）新增 Witnesses 一行；名称随 R37'),
    PKG + 'README.zh.md': ('names follow R37', '名称随 R37'),
    PKG + 'check_becoming.py': ('CORE adds Becoming.Witnesses; no logic changed', 'CORE 加 Becoming.Witnesses；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R37's run", '当前回执为 R37 之运行'),
}
LEAN_WHAT = {
    'Witnesses.lean': ('new: the library of the models the spine builds again and again (halted, single, profile, the empty flow, giving, unrequired webs, the relay and its members)',
                       '新增：脊柱反复构造的模型之库（halted、single、profile、空流、giving、不被需要的网、接力及其成员）'),
    'Prelude.lean': ('the definitions and statements stated once (Distinct, total, steps, nonzero, Copying.nth, Law.memberAt, Settling.consAct, DistinctUnder, downFrom and their laws) moved here; other statements unchanged',
                     '只陈述一次的定义与陈述（Distinct、total、steps、nonzero、Copying.nth、Law.memberAt、Settling.consAct、DistinctUnder、downFrom 及其规律）移入；其他陈述不变'),
    'Likeness.lean': ('likeness, bisimulations and tests stated once for a family of relations (BisimulationWith, AlikeWith, TestWith); MatchesParts moved here; Alike.holds_iff proved as the case of no relation; statements unchanged',
                      '为一族关系陈述一次的相似、互模拟与检验（BisimulationWith、AlikeWith、TestWith）；MatchesParts 移入；Alike.holds_iff 作为无关系的情形证明；陈述不变'),
    'Composition.lean': ('the joint frame is the case of one relation: JointTest, JointAlike, JointBisimulation, SameJointTests abbreviations of the general ones, the parallel laws removed; kept statements unchanged',
                         '联合框架是一个关系的情形：JointTest、JointAlike、JointBisimulation、SameJointTests 为一般者的缩写，平行的规律删去；保留的陈述不变'),
}
DEFAULT_LEAN = ('twin definitions, witness models or copies replaced by the definition stated once, the instance of Witnesses or the kept name; kept statements unchanged',
                '孪生定义、见证模型或副本由只陈述一次的定义、Witnesses 的实例或保留的名称取代；保留的陈述不变')


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
    en = '20 October 2026, R37 (lens B of the twentieth review: the witness models as instances of one library, one bisimulation theory for a family of relations, the definition twins and copies stated once):'
    zh = '2026年10月20日，R37（第二十次评审的 B 视角：见证模型为一个库的实例，为一族关系的一个互模拟理论，孪生定义与副本只陈述一次）：'
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
        parts_en.append('Replaced by the name stating it now, the same statement or its general form, or renamed (development/r37-lens-b/RENAME-TABLE.json): ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.')
        parts_zh.append('以现在陈述它的名称取代（陈述相同或为其一般形式）或改名（development/r37-lens-b/RENAME-TABLE.json）：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。')
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
    if last.get('en', '').startswith('20 October 2026, R37'):
        last['en'] = last['en'].rstrip() + ' Also: ' + ' '.join(parts_en)
        last['zh'] = last['zh'].rstrip() + '另：' + ''.join(parts_zh)
    else:
        d.setdefault('history', []).append({'en': en + ' ' + ' '.join(parts_en) + ' The claim is unchanged.',
                                            'zh': zh + ''.join(parts_zh) + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
