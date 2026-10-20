#!/usr/bin/env python3
"""R34 (20 October 2026), one evaluative chain: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R34 was rebased on; RECEIPT_ID the passing core receipt of R34's checker run.
Adapted from R33's rebind (development/r33-joins/rebind.py); the logic is R33's, the tables are R34's.

* The moves and removals are read off the two receipts (R33's, the base, and R34's): a declaration whose module
  changed moved with its full name (LivingSignificance to Extension, Ranking.stepwise_iff to Relevance); one in the
  base and not in R34's was removed as the same statement as a kept one, or renamed, and must be in
  RENAME-TABLE.json (`removed`, `renamed`).
* In every declaration list (laws, references, aliases) a removed or renamed declaration takes its kept name. In
  references a moved declaration is filed under the file of its module in R34's receipt (added, with a proof
  binding where the record has bindings).
* Proof bindings to the Lean files R34 changed are rebound to the receipt; references to the files R34 changed
  are re-pointed where they matched BASE (the record was current), where the render log reports drift in sections
  the record cites, after reading the change (WHAT says what changed), and always for the records R34 wrote or
  edited (records_r34.py).
* A history note says what moved, what was replaced and what was re-pointed; a record whose last note is R34's
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
BASE_RID = '20261019T235844.485705Z'
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
REMAP = {x['old']: x['kept'] for x in TABLE['removed']}
REMAP.update({x['old']: x['new'] for x in TABLE['renamed']})
JOINS = {}
FOLDED_INTO = {d + x + '.lean': B + s + '.lean' for d in (B, HIST) for x, s in JOINS.items()}
GONE_FILES = set(FOLDED_INTO)
removed = set(home_base) - set(home)
assert removed == set(REMAP), (sorted(removed - set(REMAP)), sorted(set(REMAP) - removed))
assert all(y in home for y in REMAP.values())
MOVED = {x for x in home_base if x in home and home[x] != home_base[x]}
print('moved', len(MOVED), sorted({(home_base[x], home[x]) for x in MOVED}))
SUPERSEDED = set()
R33_RECORDS = {'the-run-classes-and-widening', 'comparison-by-widening', 'held-lives-g0-is-centering',
               'alignment-direction-g0-j', 'ranking-under-readings', 'relational-reading-comparison'}

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': (
        'the run classes and widening (§6.8), standpoints as formations (§5, §6, §6.7), one object of admission '
        '(§6.12), the GrownBy blocker (§6.13), the direction on the spine (§7.5), §8.1 items 2-5, D2 in §8.3, obs in '
        '§8.4 and the glossary row of generative; §9 (receipt, counts, layers, connectivity) follows R34',
        '整段的类与扩大（§6.8）、以形成为立场（§5、§6、§6.7）、接纳这一个对象（§6.12）、GrownBy 的障碍（§6.13）、脊柱上的方向（§7.5）、§8.1 第 2–5 项、'
        '§8.3 的 D2、§8.4 的 obs 与术语表“生成的”一行；§9（回执、计数、层、连通性）随 R34'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the same local edits; §9 and its module table follow R34',
                                          '同样的局部修改；§9 及其模块表随 R34'),
    STUDY: ('section 225 added', '新增第 225 节'),
    RF + 'DELEGATED-CHOICES.md': ('D2 revised (the formation-level reading dropped from "generative"), D1 states the GrownBy blocker',
                                  'D2 修订（“生成的”不再取形成层次的读法），D1 写明 GrownBy 的障碍'),
    RF + 'THEOREM-CONNECTIVITY.md': ('a paragraph on R34 added to section 11', '第 11 节新增关于 R34 的一段'),
    RF + 'THEOREM-CONNECTIVITY.json': ("measured on R34's tree", '在 R34 树上测量'),
    RF + 'THEOREM-CONNECTIVITY-APART.json': ('two roots retired (Ranking.active_of_renewed, ActiveReading.absent_included)',
                                             '两个根退出（Ranking.active_of_renewed、ActiveReading.absent_included）'),
    'theories/becoming/OPENING.md': ('the footnote on alignment names the condition for scope and C for order and cites the core schema; the body is unchanged',
                                     '关于对齐的脚注写明条件定范围、C 定次序并引核心模式；正文不变'),
    PKG + 'Becoming.lean': ('Becoming.Direction imported, with its note; layer tags of Ranking, ActiveReading and ScoreRepresentation now L1',
                            '导入 Becoming.Direction 并加说明；Ranking、ActiveReading、ScoreRepresentation 的层标为 L1'),
    PKG + 'README.md': ('the module table, generated, has a row for Direction and the new layers', '模块表（生成）新增 Direction 一行并随新的层'),
    PKG + 'README.zh.md': ('the module table, generated, follows the new layers', '模块表（生成）随新的层'),
    PKG + 'check_becoming.py': ("CORE adds Becoming.Direction; the scope text names R34's laws; no logic changed",
                                'CORE 加 Becoming.Direction；范围说明写 R34 的规律；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R34's run", '当前回执为 R34 之运行'),
}
LEAN_WHAT = {
    'Retaining.lean': ('the run classes and widening added (Flow.Balances.includes_of_renewed, not_narrows_of_renewed, includes_of_renewingIn, narrows_of_consumed, Preemption.renewingAt_consuming_narrows, Untaken); kept statements unchanged',
                       '新增整段的类与扩大（Flow.Balances.includes_of_renewed、not_narrows_of_renewed、includes_of_renewingIn、narrows_of_consumed、Preemption.renewingAt_consuming_narrows、Untaken）；保留的陈述不变'),
    'Relevance.lean': ('Web.paths_one_object added; the readings of possibility read worlds as webs (restated, study section 225); Ranking.stepwise_iff moved here',
                       '新增 Web.paths_one_object；可能性读法把世界读作网（重述，见研究第 225 节）；Ranking.stepwise_iff 移入'),
    'Boundaries.lean': ('standpoints as formations added (Web.selfValuation and its laws); imports Standpoints; kept statements unchanged',
                        '新增以形成为立场（Web.selfValuation 及其规律）；导入 Standpoints；保留的陈述不变'),
    'Ranking.lean': ('worlds read as webs (restated, study section 225); imports Frame and Extension only; stepwise_iff moved to Relevance',
                     '世界读作网（重述，见研究第 225 节）；只导入 Frame 与 Extension；stepwise_iff 移到 Relevance'),
    'ActiveReading.lean': ('worlds read as webs (restated); livingSignificance_wholeRun_web_iff and absent_web_dependent removed as the same statements as the kept ones',
                           '世界读作网（重述）；livingSignificance_wholeRun_web_iff 与 absent_web_dependent 因与保留者陈述相同而删去'),
    'Extension.lean': ('LivingSignificance stated here, moved unchanged from ValuationFrames', 'LivingSignificance 在此陈述，自 ValuationFrames 原样移入'),
    'ValuationFrames.lean': ('LivingSignificance moved to Extension, unchanged; kept statements unchanged', 'LivingSignificance 原样移到 Extension；保留的陈述不变'),
    'Direction.lean': ("new: the direction on a web's moves", '新增：网之动作上的方向'),
}
DEFAULT_LEAN = ('docstrings only (standpoints of any type, obs the second supplied relation, the fixed-type limit, the run classes) or an import; kept statements unchanged',
                '只改说明（任何类型的立场、obs 是第二个给出的关系、固定类型的界、整段的类）或导入；保留的陈述不变')


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
    en = '20 October 2026, R34 (one evaluative chain: the run classes and widening, one object of admission, standpoints as formations, the direction on a web\'s moves, worlds read as webs):'
    zh = '2026年10月20日，R34（一条评价之链：整段的类与扩大，接纳这一个对象，以形成为立场，网之动作上的方向，世界读作网）：'
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
        parts_en.append('Replaced by the kept name, the same statement once the world is a web, or renamed (development/r34-evaluative-chain/RENAME-TABLE.json): ' + '; '.join(f'{x} (now {y})' for x, y in rp) + '.')
        parts_zh.append('以保留的名称取代（世界是网之后陈述相同）或改名（development/r34-evaluative-chain/RENAME-TABLE.json）：' + '；'.join(f'{x}（现为 {y}）' for x, y in rp) + '。')
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
    if last.get('en', '').startswith('20 October 2026, R34'):
        last['en'] = last['en'].rstrip() + ' Also: ' + ' '.join(parts_en)
        last['zh'] = last['zh'].rstrip() + '另：' + ''.join(parts_zh)
    else:
        d.setdefault('history', []).append({'en': en + ' ' + ' '.join(parts_en) + ' The claim is unchanged.',
                                            'zh': zh + ''.join(parts_zh) + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(mv), len(rp), sorted(set(rebound)), len(ps), short(new_canon) if new_canon else '')
print(n, 'records changed')
