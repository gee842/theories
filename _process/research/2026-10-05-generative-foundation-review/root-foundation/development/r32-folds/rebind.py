#!/usr/bin/env python3
"""R32 (20 October 2026), forwarders, copies and reading modules: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R32 was rebased on; RECEIPT_ID the passing core receipt of R32's checker run.
Adapted from R31's rebind (development/r31-support/rebind.py); the logic is R31's, the tables are R32's.

* The moves and removals are read off the two receipts (R31's, the base, and R32's): a declaration whose
  module changed moved with its full name (the folded modules' declarations, and the statements stated once
  in the prelude); one in the base and not in R32's was removed, and must be a key of REMAP (removals.json and
  b9-prelude.json: the law a pure forwarder applied, or the kept name of a copy) or one of DROPPED.
* In every declaration list (laws, references) a removed name is replaced by its name in REMAP; a removed
  alias is dropped. In references a declaration is filed under the file of its module in R32's receipt: a
  moved or replaced name goes to the record's reference to that file, added (with a proof binding where the
  record has bindings) where the record had none. A reference to a folded module's file (at its old path or,
  after the move, in the Lean history folder) is dropped once its declarations are filed, with its proof
  binding; a record whose canonical source was such a file takes the module it was folded into.
* TEXT replaces the sentences that named a removed declaration (each occurs once in the record).
* Proof bindings to the Lean files R32 changed are rebound to the receipt; references to the files R32
  changed are re-pointed where they matched BASE (the record was current), or where the render log reports
  drift in sections the record cites, after reading the change (WHAT says what changed).
* A history note says what moved, what was replaced and what was re-pointed.
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
sys.path.insert(0, HERE)
import fold  # noqa: E402

LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEANDIR + 'becoming/'
B = PKG + 'Becoming/'
BASE_RID = '20261019T213206.644158Z'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
assert not any(v for m in receipt['modules'] if m.get('layer') == 'core' for v in m['axiom_dependencies'].values()), 'core axiom report not empty'
base_receipt = json.load(open(PKG + 'becoming-checks/' + BASE_RID + '/verification.json'))


def homes(r):
    out = {}
    for m in r['modules']:
        if m.get('layer') != 'core':
            continue
        for x in m.get('declarations', []):
            out[x['name'] if isinstance(x, dict) else x] = m['module']
    return out


home, home_base = homes(receipt), homes(base_receipt)
path_of = {m: LEANDIR + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}
HIST = LEANDIR + 'history/becoming/Becoming/'
# Where the Lean history folder holds a former module's bytes (its MANIFEST).
_manifest = json.load(open(LEANDIR + 'history/MANIFEST.json'))
HISTORY_OF = {e['old_path']: e['new_path'] for e in _manifest['entries'] if e.get('old_path', '').endswith('.lean')}
# The folded files, at their old paths and where research.py move put their bytes; each goes to its fold target.
FOLDED_INTO = {d + x + '.lean': B + s + '.lean' for d in (B, HIST) for x, s in fold.FOLDS}
GONE_FILES = set(FOLDED_INTO)

_rows = json.load(open(os.path.join(HERE, 'removals.json')))['rows'] + json.load(open(os.path.join(HERE, 'b9-prelude.json')))['rows']
REMAP = {r['old']: r['new'] for r in _rows}
for _x in REMAP:
    while REMAP[_x] in REMAP:
        REMAP[_x] = REMAP[REMAP[_x]]
DROPPED = {'Becoming.MoveFormation.zero_add', 'Becoming.MoveFormation.succ_add'}
FORWARDERS = {r['old'] for r in _rows if r['why'] == 'pure forwarder (B10)'}
removed = set(home_base) - set(home)
assert removed == set(REMAP) | DROPPED, (sorted(removed - set(REMAP) - DROPPED), sorted(set(REMAP) | DROPPED - removed))
for x, y in REMAP.items():
    # a kept name the receipt does not list is a constant Lean generates (`Site.node.inj`) or the foundation's
    assert y in home or not y.startswith('Becoming.') or y.endswith('.inj'), y
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}
UNIVERSE = set()

TEXT = {}
PATHFIX = {}
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('§9 (receipt, counts, connectivity under the measure that no longer counts restatement) follows R32',
                                       '§9（回执、计数、不再计入重述的连通性度量）随 R32'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('§9 (receipt, counts, connectivity) follows R32', '§9（回执、计数、连通性）随 R32'),
    STUDY: ('section 223 added', '新增第 223 节'),
    PKG + 'Becoming.lean': ('the folded modules are no longer imported and their notes are gone',
                            '折入的模块不再导入，其说明删去'),
    PKG + 'README.md': ('the module table, generated, has no row for a folded module', '模块表（生成）不再有折入模块的行'),
    PKG + 'README.zh.md': ('the module table, generated, has no row for a folded module', '模块表（生成）不再有折入模块的行'),
    PKG + 'check_becoming.py': ("CORE follows R32's modules; the scope text names the section holding a folded module's laws; no logic changed",
                                'CORE 随 R32 的模块；范围说明指出持有折入模块之律的节；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R32's run", '当前回执为 R32 之运行'),
}
_folded_into = {}
for x, s in fold.FOLDS:
    _folded_into.setdefault(s, []).append(x)
LEAN_WHAT = {
    'Prelude.lean': ('twelve statements stated in two or more modules each, stated here once under the name kept',
                     '十二条原先在两个或更多模块中各自陈述的命题，在此以保留的名称陈述一次'),
}
for s, xs in _folded_into.items():
    LEAN_WHAT[s + '.lean'] = (
        'takes, as its final section' + ('s ' if len(xs) > 1 else ' ') + ', '.join(xs)
        + ', the module' + ('s' if len(xs) > 1 else '') + ' reading it, folded in with declarations, names and statements unchanged; '
        'pure forwarders and copies removed where it had them',
        '以末节收入 ' + '、'.join(xs) + '（读它的模块），声明、名称与陈述不变；其中的纯转发与副本删去')
DEFAULT_LEAN = ('pure forwarders and copies removed (B10, B9), uses pointed at the law they restate; imports follow the folds; kept statements unchanged',
                '纯转发与副本删去（B10、B9），用法改指所重述之律；导入随折入；保留的陈述不变')



def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


changed = subprocess.run(['git', 'diff', '--name-only', BASE, '--'], capture_output=True, text=True, check=True).stdout.split()
LEAN = {p for p in changed if p.startswith(B) and p.endswith('.lean') and p not in GONE_FILES}
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
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by = {r['path']: r for r in refs}
    moved, replaced, texts = [], [], 0
    for old, new in TEXT.get(rid, []):
        hits = [(c, k) for c, k in strings(d) if old in c[k]]
        if not hits and any(new in c[k] for c, k in strings(d)):
            continue  # applied by an earlier run
        assert len(hits) == 1 and hits[0][0][hits[0][1]].count(old) == 1, (rid, old[:60], len(hits))
        c, k = hits[0]
        c[k] = c[k].replace(old, new)
        texts += 1
    for law in d.get('laws', []) or []:
        if isinstance(law, dict) and law.get('declarations'):
            law['declarations'] = remap(law['declarations'], replaced)
    if isinstance(d.get('aliases'), list):
        replaced += [(x, REMAP[x]) for x in d['aliases'] if x in REMAP]
        d['aliases'] = [x for x in d['aliases'] if x not in REMAP]

    added, filed = [], set()
    from_gone = {}

    def ref_for(path, after):
        if path not in by:
            by[path] = {'path': path, 'role': 'proof', 'sha256': h(path), 'declarations': []}
            added.append(path)
            refs.insert(refs.index(after) + 1 if after in refs else len(refs), by[path])
        return by[path]

    for r in list(refs):
        if not r.get('declarations'):
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
                if r['path'] in GONE_FILES:
                    from_gone.setdefault(r['path'], {}).setdefault(target, 0)
                    from_gone[r['path']][target] += 1
                if y == x:
                    moved.append((x, r['path'], target))
            elif y not in keep:
                keep.append(y)
        r['declarations'] = keep
    # A record whose canonical source R32 folded takes the module it was folded into.
    canon = d.get('canonical_source')
    new_canon = None
    if canon in GONE_FILES:
        new_canon = FOLDED_INTO[canon]
        d['canonical_source'] = new_canon
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if d.get('proof_bindings'):
        for path in sorted(filed):
            if path not in bound and by[path].get('declarations'):
                d['proof_bindings'].append(binding(path))
                bound.add(path)
        d['proof_bindings'] = [b for b in d['proof_bindings'] if b['source'] not in GONE_FILES]
    rebound, touched, kept_alias = [], set(), []
    old_receipts = {b['receipt'] for b in d.get('proof_bindings', [])}
    for b in d.get('proof_bindings', []):
        if b['source'] in LEAN and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
            b['receipt'] = RECEIPT
            rebound.append(short(b['source']))
    # An alias that only the receipt left behind elaborated (a module since moved to the Lean history folder with
    # its bytes) stays elaborated: the history file is bound to that receipt, as the F3 sweep's records do.
    bound_now = {b['receipt'] for b in d.get('proof_bindings', [])}
    for old in sorted(old_receipts - bound_now):
        orec = json.load(open(old))
        for m in orec['modules']:
            names = {x['name'] if isinstance(x, dict) else x for x in m.get('declarations', [])}
            hit = [a for a in d.get('aliases', []) or [] if a in names and a not in home]
            path = HISTORY_OF.get(LEANDIR + orec['source_paths'][m['module']])
            # Only modules since moved to the history folder; a live periphery module keeps its own receipt.
            if not hit or not path:
                continue
            assert h(path) == orec['source_sha256'][m['module']], (rid, m['module'])
            d['proof_bindings'].append({'source': path, 'receipt': old, 'sha256_pointer': '/source_sha256/' + m['module'],
                                        'success_pointer': '/status', 'success_value': 'passed'})
            assert any(r['path'] == path for r in refs) and any(r['path'] == old for r in refs), rid
            kept_alias.append((short(path), old.split('/')[-2], hit))
    for r in refs:
        p = r['path']
        if p in GONE_FILES:
            continue
        if p in LEAN and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    # Empty references left by a move are dropped only where nothing else cites the file; a
    # reference to a removed file is dropped once its declarations are filed.
    for r in list(refs):
        if r['path'] in GONE_FILES:
            assert not r.get('declarations'), (rid, r['path'])
            refs.remove(r)
        elif r['role'] == 'proof' and not r.get('declarations') and any(m[1] == r['path'] for m in moved) \
                and r['path'] != d.get('canonical_source') \
                and not any(b['source'] == r['path'] for b in d.get('proof_bindings', [])):
            refs.remove(r)
    # Evidence and counterexample paths still naming a removed file (references, bindings and the canonical
    # source are settled above) name the split part holding what they cite.
    paths_fixed = []
    for c, k in list(strings(d)):
        if c[k] in GONE_FILES:
            new = FOLDED_INTO[c[k]]
            paths_fixed.append((short(c[k]), short(new)))
            c[k] = new
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R32 (forwarders, copies and reading modules: pure forwarders removed, statements stated once, reading modules folded into the module they read):'
    zh = '2026年10月20日，R32（转发、副本与读取模块：纯转发删去，命题只陈述一次，读取模块折入其所读模块）：'
    mv = sorted({(bare(x), short(a), short(c)) for x, a, c in moved})
    if mv:
        groups = {}
        for x, a, c in mv:
            groups.setdefault((a, c), []).append(x)
        en += ' Moved with their full names: ' + '; '.join(f'from {a} to {c}, ' + ', '.join(xs) for (a, c), xs in sorted(groups.items())) + '.'
        zh += '连同完整名称移动：' + '；'.join(f'从 {a} 到 {c}：' + '、'.join(xs) for (a, c), xs in sorted(groups.items())) + '。'
    rp = sorted({(bare(x), bare(y)) for x, y in replaced if x not in FORWARDERS})
    rf = sorted({(bare(x), bare(y)) for x, y in replaced if x in FORWARDERS})
    if rf:
        en += ' Removed as pure forwarders (each applied one law to its own binders), the law named instead: ' + '; '.join(
            f'{x} (now {y})' for x, y in rf) + '.'
        zh += '作为纯转发删去（各自只把一条律应用于自己的约束变量），改提该律：' + '；'.join(
            f'{x}（现为 {y}）' for x, y in rf) + '。'
    if rp:
        en += ' Removed, with the statement kept under one name: ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.'
        zh += '删去，陈述以一个名称保留：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。'
    if new_canon:
        en += f' The canonical source {short(canon)} was folded into {short(new_canon)} as its final section; it is now {short(new_canon)}.'
        zh += f'规范来源 {short(canon)} 已作为末节折入 {short(new_canon)}，现为 {short(new_canon)}。'
    if texts:
        en += ' The sentence that named a removed declaration names the kept one.'
        zh += '提到删去之声明的句子改提保留者。'
    for path, old, hit in kept_alias:
        en += (f' {path}, in the Lean history folder with its bytes, is bound to receipt {old}, which elaborates '
               + ', '.join(hit) + ', so the alias stays checked.')
        zh += f'{path}（连同字节在 Lean 历史目录中）绑定到回执 {old}，它精化了 ' + '、'.join(hit) + '，别名因此仍受检查。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    pf = sorted(set(paths_fixed))
    pf_en = (' The evidence and counterexample paths that named ' + '; '.join(f'{a} name {b}' for a, b in pf)
             + ' (the module it was folded into).') if pf else ''
    pf_zh = ('提到 ' + '；'.join(f'{a} 的证据与反例路径改提 {b}' for a, b in pf) + '（它所折入的模块）。') if pf else ''
    en += pf_en
    zh += pf_zh
    ps = sorted(touched)
    if ps:
        en += ' Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
        zh += '读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    en += ' The claim is unchanged.'
    zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R32'):
        if pf:
            last['en'] = last['en'].replace(' The claim is unchanged.', pf_en + ' The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', pf_zh + '论断不变。')
        if ps:
            last['en'] = last['en'].replace(' The claim is unchanged.', ' Also re-pointed after reading the change: '
                                            + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '. The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', '另读过改动后重新指向：'
                                            + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。论断不变。')
    else:
        d.setdefault('history', []).append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
