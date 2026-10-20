#!/usr/bin/env python3
"""R33 (20 October 2026), joins: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R33 was rebased on; RECEIPT_ID the passing core receipt of R33's checker run.
Adapted from R32's rebind (development/r32-folds/rebind.py); the logic is R32's, the tables are R33's.

* The moves and renames are read off the two receipts (R32's, the base, and R33's): a declaration whose module
  changed moved with its full name (the declarations of LawThroughCoupling and LawThroughChangingCoupling, joined
  into LawAlongRun); one in the base and not in R33's was renamed, and must be a key of RENAME-TABLE.json's
  `declarations`.
* In every declaration list (laws, references, aliases) a renamed declaration takes its new name. In references a
  moved declaration is filed under the file of its module in R33's receipt (added, with a proof binding where the
  record has bindings, where the record had none); a reference to a joined module's file (at its old path or in
  the Lean history folder) is dropped once its declarations are filed.
* The two records R33 superseded (a law through coupling, through changing coupling) keep their declaration lists,
  canonical source and references to the joined modules' files in the Lean history folder (the evidence of what was
  checked when they were current; each history file holds its module's bytes); only their bindings to changed Lean
  files are rebound and their references to the changed docs re-pointed, so their pages render with their status.
* Proof bindings to the Lean files R33 changed are rebound to the receipt; references to the files R33 changed
  are re-pointed where they matched BASE (the record was current), where the render log reports drift in sections
  the record cites, after reading the change (WHAT says what changed), and always for the records R33 wrote or
  edited (records_r33.py), which were written against the R33 docs before these were committed.
* A history note says what moved, what was renamed and what was re-pointed; a record whose last note is R33's
  has that note extended instead.
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
BASE_RID = '20261019T231053.882924Z'
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
TABLE = json.load(open(os.path.join(HERE, 'RENAME-TABLE.json')))
REMAP = dict(TABLE['declarations'])
JOINS = {k.split('.', 1)[1]: v.split('.', 1)[1] for k, v in TABLE['modules'].items()}
FOLDED_INTO = {d + x + '.lean': B + s + '.lean' for d in (B, HIST) for x, s in JOINS.items()}
GONE_FILES = set(FOLDED_INTO)
removed = set(home_base) - set(home)
assert removed == set(REMAP), (sorted(removed - set(REMAP)), sorted(set(REMAP) - removed))
assert all(y in home for y in REMAP.values())
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}
print('moved', len(MOVED), sorted({(home_base[x], home[x]) for x in MOVED}))
SUPERSEDED = {'a-law-through-coupling-along-one-run', 'a-law-through-changing-coupling-along-one-run'}
R33_RECORDS = {'a-law-through-a-projection-along-one-run', 'learning-through-a-map-is-tracking-in-the-limit',
               'the-world-an-interleaving-builds', 'whether-a-loop-closes-a-difference', 'thresholds-of-waiting'}

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': (
        'the law along one run under a relation in one bullet, learning through a map as tracking, LoopReturn\'s factor '
        'and the join with Loops, the tolerance law on a web, the world an interleaving builds; §9 (receipt, counts, '
        'connectivity) follows R33',
        '沿一个运行、在一个关系之下的规律合为一条，经映射的学习即跟随，LoopReturn 的倍率及与 Loops 的并合，网上的容忍律，交错构造的世界；§9（回执、计数、连通性）随 R33'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the join with Loops, the web law; §9 (receipt, counts, connectivity) follows R33',
                                          '与 Loops 的并合，网的定律；§9（回执、计数、连通性）随 R33'),
    STUDY: ('section 224 added', '新增第 224 节'),
    RF + 'THEOREM-CONNECTIVITY.md': ('a paragraph on R33 added to section 11', '第 11 节新增关于 R33 的一段'),
    RF + 'THEOREM-CONNECTIVITY.json': ("measured on R33's tree", '在 R33 树上测量'),
    PKG + 'Becoming.lean': ('the joined modules are no longer imported and their notes are gone',
                            '并入的模块不再导入，其说明删去'),
    PKG + 'README.md': ('the module table, generated, has no row for a joined module', '模块表（生成）不再有并入模块的行'),
    PKG + 'README.zh.md': ('the module table, generated, has no row for a joined module', '模块表（生成）不再有并入模块的行'),
    PKG + 'check_becoming.py': ("CORE follows R33's modules; the scope text names where a joined module's laws are; no logic changed",
                                'CORE 随 R33 的模块；范围说明指出并入模块之律所在；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R33's run", '当前回执为 R33 之运行'),
}
LEAN_WHAT = {
    'LawAlongRun.lean': ('one law along a run under a relation (Run.law_under_iff), its readings through a projection, '
                         'through coupling and through changing coupling as corollaries, LawThroughCoupling and '
                         'LawThroughChangingCoupling joined in with their names and statements',
                         '运行上关系之下的一条规律（Run.law_under_iff），经投影、经耦合、经改变的耦合的读法为推论，LawThroughCoupling 与 LawThroughChangingCoupling 以原名与原陈述并入'),
    'LimitVerification.lean': ('Limit.Tracks added; kept statements unchanged', '新增 Limit.Tracks；保留的陈述不变'),
    'LearnableRuns.lean': ('predicts_iff_tracks, learnable_iff_tracks, learnable_iff_identifies and Merge.learnable_not_identifies added; kept statements unchanged',
                           '新增 predicts_iff_tracks、learnable_iff_tracks、learnable_iff_identifies 与 Merge.learnable_not_identifies；保留的陈述不变'),
    'LearningRuns.lean': ('pair_first_not_rests and pair_whole_rests renamed pair_first_not_predicts and pair_whole_predicts, statements unchanged',
                          'pair_first_not_rests、pair_whole_rests 改名 pair_first_not_predicts、pair_whole_predicts，陈述不变'),
    'LoopReturn.lean': ("a link's strength renamed its factor, whole_strengths whole_factors; the join with Loops (selfLoop_carried, selfLoop_gap, carried_around_course) added",
                        '环节的强度改称倍率，whole_strengths 改为 whole_factors；新增与 Loops 的并合（selfLoop_carried、selfLoop_gap、carried_around_course）'),
    'Tolerance.lean': ('the tolerance law as the run of a web (web_tolerating, web_answers, giftWeb_tolerating) added; kept statements unchanged',
                       '新增容忍律作为网的运行（web_tolerating、web_answers、giftWeb_tolerating）；保留的陈述不变'),
    'Interleavings.lean': ('the world an interleaving builds (LocalLaw.world, world_balances, world_final, world_swap, standings_of_courses) added; kept statements unchanged',
                           '新增交错构造的世界（LocalLaw.world、world_balances、world_final、world_swap、standings_of_courses）；保留的陈述不变'),
}
DEFAULT_LEAN = ('prose follows the joins (predicts where it said rests, factor where it said strength) or imports follow the joined modules; kept statements unchanged',
                '说明随并合（以“预测”代“停于”，以“倍率”代“强度”）或导入随并入的模块；保留的陈述不变')


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
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R33 (joins: one law along a run, learning through a map as tracking, one loop theory, the tolerance law on webs, the world an interleaving builds):'
    zh = '2026年10月20日，R33（并合：运行上的一条规律，经映射的学习即跟随，一个回路理论，网上的容忍律，交错构造的世界）：'
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
        parts_en.append('Renamed, statements unchanged (development/r33-joins/RENAME-TABLE.json): ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.')
        parts_zh.append('改名，陈述不变（development/r33-joins/RENAME-TABLE.json）：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。')
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
    if last.get('en', '').startswith('20 October 2026, R33'):
        last['en'] = last['en'].rstrip() + ' Also: ' + ' '.join(parts_en)
        last['zh'] = last['zh'].rstrip() + '另：' + ''.join(parts_zh)
    else:
        d.setdefault('history', []).append({'en': en + ' ' + ' '.join(parts_en) + ' The claim is unchanged.',
                                            'zh': zh + ''.join(parts_zh) + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
