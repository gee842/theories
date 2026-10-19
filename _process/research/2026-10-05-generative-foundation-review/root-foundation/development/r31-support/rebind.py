#!/usr/bin/env python3
"""R31 (20 October 2026), layers and one prelude: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R31 was rebased on; RECEIPT_ID the passing core receipt of R31's checker run.
Adapted from R29's rebind (development/r29-compression/rebind.py).

* The moves and removals are read off the two receipts (R30's, the base, and R31's): a declaration
  whose module changed moved with its full name; one in the base and not in R31's was removed, and
  must be a key of REMAP, read from dedup-table.json (the kept name stating the same).
* In every declaration list (laws, references) a removed name is replaced by its kept name; a removed
  alias is dropped. In references a declaration is filed under the file of its module in R31's
  receipt: a moved or replaced name goes to the record's reference to that file, added (with a proof
  binding where the record has bindings) where the record had none. A reference to a file R31
  removed (Order.lean, Naturals.lean, ListTests.lean) is dropped once its declarations are filed,
  with its proof binding; a record whose canonical source was such a file takes the file that holds
  most of its declarations from it.
* TEXT replaces the sentences that named a removed declaration (each occurs once in the record).
* Proof bindings to the Lean files R31 changed are rebound to the receipt; references to the files R31
  changed are re-pointed where they matched BASE (the record was current), or where the render log
  reports drift in sections the record cites, after reading the change (WHAT says what changed).
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
LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEANDIR + 'becoming/'
B = PKG + 'Becoming/'
BASE_RID = '20261019T194851.524223Z'
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
GONE_FILES = {B + 'Order.lean', B + 'Naturals.lean', B + 'ListTests.lean'}

TABLE = json.load(open(os.path.join(HERE, 'dedup-table.json')))
REMAP = {x: g['keep'] for g in TABLE['groups'] for x in g['delete']}
removed = set(home_base) - set(home)
assert removed == set(REMAP), (sorted(removed - set(REMAP)), sorted(set(REMAP) - removed))
for x, y in REMAP.items():
    assert y in home, y
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}

TEXT = {
    'how-often-couplings-act': [
        ('Reuses carriedGive_congr_strength, Closing.ble_false_of_lt and Closing.Onset',
         'Reuses carriedGive_congr_strength, Naturals.ble_false_of_lt and Closing.Onset'),
        ('复用 carriedGive_congr_strength、Closing.ble_false_of_lt 与 Closing.Onset',
         '复用 carriedGive_congr_strength、Naturals.ble_false_of_lt 与 Closing.Onset'),
    ],
}
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('§9 (layers by a checkable property, the module table, receipt, counts) follows R31',
                                       '§9（以可检查性质定义的层、模块表、回执、计数）随 R31'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('§9 (layers, module table, receipt, counts) follows R31', '§9（层、模块表、回执、计数）随 R31'),
    STUDY: ('section 222 added', '新增第 222 节'),
    PKG + 'Becoming.lean': ('imports the prelude and the modules R31 split or added; the notes carry the computed layers',
                            '导入前导与 R31 拆分或新增的模块；说明载有计算出的层'),
    PKG + 'README.md': ('the module table is generated from the import graph and the checker list, with computed layers',
                        '模块表由导入图与检查器列表生成，层由计算给出'),
    PKG + 'README.zh.md': ('the module table is generated, with computed layers', '模块表由生成，层由计算给出'),
    PKG + 'check_becoming.py': ("CORE follows R31's modules; the SCOPE text of the split modules; no logic changed",
                                'CORE 随 R31 的模块；拆分模块的 SCOPE 文本；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R31's run", '当前回执为 R31 之运行'),
}
LEAN_WHAT = {
    'Prelude.lean': ('new module: the lemmas on numbers, truth values, lists and options, each stated once, with Naturals, ListTests and the root arithmetic moved in; imports only Init',
                     '新模块：关于数、真值、列表与选项的引理，每条陈述一次，Naturals、ListTests 与根命名空间的算术移入；只导入 Init'),
    'Laws.lean': ('new module after the frame: Determined, the laws of change and partial laws of Assurance, GoAlikeUnder, and GoAlike as its case at equality, moved in with their names',
                  '框架之后的新模块：Determined、Assurance 的变化律与部分律、GoAlikeUnder，以及作为其相等情形的 GoAlike，连同名称移入'),
    'Retaining.lean': ('new module: retaining and adding with no condition, the margin theorems, the stepwise classes and Preemption, moved from Significance.lean',
                       '新模块：不加条件的保留与增加、余量定理、逐步类与 Preemption，自 Significance.lean 移入'),
    'Clearing.lean': ('new module: the witness Clearing and its facts on admission, regions and retaining, moved from Continuation.lean, Regions.lean and Significance.lean',
                      '新模块：见证 Clearing 及其关于接纳、区域与保留的事实，自 Continuation.lean、Regions.lean 与 Significance.lean 移入'),
    'Extension.lean': ('new module: C on frames and on level paths, with no valuation, moved from ValuationFrames.lean',
                       '新模块：框架与水平路径上的 C，不用赋值，自 ValuationFrames.lean 移入'),
    'BoundedSignificance.lean': ('new module: the theorems where bounded significance meets the continuation condition, moved from Interdependence.lean and Feedback.lean',
                                 '新模块：有界意义与延续条件相遇的定理，自 Interdependence.lean 与 Feedback.lean 移入'),
    'Stuttering.lean': ('new module: the stuttering part of Order.lean, moved unchanged', '新模块：Order.lean 的停顿部分，原样移入'),
    'Reordering.lean': ('new module: the reordering part of Order.lean, moved unchanged', '新模块：Order.lean 的重排部分，原样移入'),
    'IdleRemoval.lean': ('new module: the removal of idle steps from Order.lean, moved unchanged', '新模块：Order.lean 中去除空步的部分，原样移入'),
    'Significance.lean': ('what takes no condition moved to Retaining.lean and Clearing.lean; the conditional theorems kept, statements unchanged',
                          '不带条件者移到 Retaining.lean 与 Clearing.lean；条件定理保留，陈述不变'),
    'Interdependence.lean': ('the conditional theorems moved to BoundedSignificance.lean; imports Clearing, not Significance',
                             '条件定理移到 BoundedSignificance.lean；导入 Clearing 而非 Significance'),
    'Feedback.lean': ('the conditional theorems moved to BoundedSignificance.lean; comparison_within_reach proved with no condition, statement unchanged',
                      '条件定理移到 BoundedSignificance.lean；comparison_within_reach 不经条件证明，陈述不变'),
    'ValuationFrames.lean': ('C on frames moved to Extension.lean', '框架上的 C 移到 Extension.lean'),
    'Continuation.lean': ('the witness Clearing moved to Clearing.lean', '见证 Clearing 移到 Clearing.lean'),
    'Regions.lean': ("Clearing's losing beyond the dependence moved to Clearing.lean", 'Clearing 的依存之外的失去移到 Clearing.lean'),
    'Response.lean': ('responsive_comparison proves the two excesses itself, with no condition, statement unchanged',
                      'responsive_comparison 自证两个超出，不经条件，陈述不变'),
    'Joint.lean': ('Determined moved to Laws.lean', 'Determined 移到 Laws.lean'),
    'Assurance.lean': ('the laws of change and partial laws moved to Laws.lean; imports Laws in place of Joint', '变化律与部分律移到 Laws.lean；以导入 Laws 代替 Joint'),
    'Likeness.lean': ('GoAlikeUnder moved to Laws.lean', 'GoAlikeUnder 移到 Laws.lean'),
    'Mechanism.lean': ('GoAlike moved to Laws.lean, defined as GoAlikeUnder at equality', 'GoAlike 移到 Laws.lean，定义为相等处的 GoAlikeUnder'),
    'OrderNormal.lean': ('root list and Boolean lemmas moved to Prelude.lean; copies removed (one name per statement); imports IdleRemoval',
                         '根命名空间的列表与布尔引理移到 Prelude.lean；副本删去（每个陈述一个名称）；导入 IdleRemoval'),
}
DEFAULT_LEAN = ('prelude-only lemmas stated once in Prelude.lean: copies removed and uses re-pointed to the kept name, imports and docstrings follow R31; kept statements unchanged',
                '只用前导的引理在 Prelude.lean 中只陈述一次：副本删去，用法改指保留的名称，导入与说明随 R31；保留的陈述不变')


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
    # A record whose canonical source R31 removed takes the file holding most of its declarations from it.
    canon = d.get('canonical_source')
    new_canon = None
    if canon in GONE_FILES:
        counts = from_gone.get(canon, {})
        new_canon = max(sorted(counts), key=lambda p: counts[p])
        d['canonical_source'] = new_canon
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if d.get('proof_bindings'):
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
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R31 (layers and one prelude: the ethics out of the general import closure, one law module, one prelude, Order split):'
    zh = '2026年10月20日，R31（层与一个前导：伦理移出一般导入闭包、一个律模块、一个前导、Order 拆分）：'
    mv = sorted({(bare(x), short(a), short(c)) for x, a, c in moved})
    if mv:
        groups = {}
        for x, a, c in mv:
            groups.setdefault((a, c), []).append(x)
        en += ' Moved with their full names: ' + '; '.join(f'from {a} to {c}, ' + ', '.join(xs) for (a, c), xs in sorted(groups.items())) + '.'
        zh += '连同完整名称移动：' + '；'.join(f'从 {a} 到 {c}：' + '、'.join(xs) for (a, c), xs in sorted(groups.items())) + '。'
    rp = sorted({(bare(x), bare(y)) for x, y in replaced})
    if rp:
        en += ' Removed, with the statement kept under one name: ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.'
        zh += '删去，陈述以一个名称保留：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。'
    if new_canon:
        en += f' The canonical source {short(canon)} was split; it is now {short(new_canon)}.'
        zh += f'规范来源 {short(canon)} 已拆分，现为 {short(new_canon)}。'
    if texts:
        en += ' The sentence that named a removed declaration names the kept one.'
        zh += '提到删去之声明的句子改提保留者。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    ps = sorted(touched)
    if ps:
        en += ' Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
        zh += '读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    en += ' The claim is unchanged.'
    zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R31'):
        if ps:
            last['en'] = last['en'].replace(' The claim is unchanged.', ' Also re-pointed after reading the change: '
                                            + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '. The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', '另读过改动后重新指向：'
                                            + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。论断不变。')
    else:
        d.setdefault('history', []).append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), texts, sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
