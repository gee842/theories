#!/usr/bin/env python3
"""R28 (20 October 2026), one base by definition: rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R28 was rebased on; RECEIPT_ID the passing core receipt of R28's checker run.

* Declarations that moved with their full names (`Dependence` from Dependence.lean and `WebAt` from
  Runs.lean to World.lean; `Law.process` from Labelled.lean, and the five notions of every process with
  the four lemmas reading a course as an orbit from Branching.lean, to Recurrence.lean) move to the
  record's reference to their new file, which is added with a proof binding where the record had none.
  Every move is checked against the receipt's list of elaborated declarations.
* `worlds-are-runs` gains the declarations that make a world a run by its type (World.lean:
  `everyStep`, `World.web`, `World.flow`, `World.of`, `World.of_web`, `World.of_flow`;
  Runs.lean: `World.run_history`) and its boundary "worlds are still defined without processes" is
  removed, since that is now shown; `recurrence-without-premise` gains the five unfolding lemmas
  (`Law.lossless_iff`, `Law.merges_iff`, `Law.returns_iff`, `Law.reachable_iff`, `Law.keeps_iff`). Both
  records' text is edited by hand (see the study section); this script only binds.
* Proof bindings to the Lean files R28 changed are rebound to the receipt; references to the files R28
  changed are re-pointed where they matched BASE (the record was current), or where the render log
  reports drift in sections the record cites, after reading the change (WHAT says what changed).
* A history note says what moved and what was re-pointed; claims are unchanged except where stated.
"""
import glob
import hashlib
import json
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
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
B = PKG + 'Becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
assert not any(v for m in receipt['modules'] if m.get('layer') == 'core' for v in m['axiom_dependencies'].values()), 'core axiom report not empty'

MOVES = {
    'Becoming.Dependence': (B + 'Dependence.lean', B + 'World.lean'),
    'Becoming.WebAt': (B + 'Runs.lean', B + 'World.lean'),
    'Becoming.Law.process': (B + 'Labelled.lean', B + 'Recurrence.lean'),
}
for n in ('Reachable', 'KeepsPossibilities', 'Returns', 'Lossless', 'Merges', 'units_length', 'law_trace_of',
          'law_trace_iff', 'law_reach_iff'):
    MOVES['Becoming.Branching.' + n] = (B + 'Branching.lean', B + 'Recurrence.lean')
ADD = {
    'worlds-are-runs': {B + 'World.lean': ['Becoming.Dependence', 'Becoming.WebAt', 'Becoming.everyStep',
                                           'Becoming.World.web', 'Becoming.World.flow',
                                           'Becoming.World.of', 'Becoming.World.of_web', 'Becoming.World.of_flow'],
                        B + 'Runs.lean': ['Becoming.World.run_history']},
    'recurrence-without-premise': {B + 'Recurrence.lean': ['Becoming.Law.lossless_iff', 'Becoming.Law.merges_iff',
                                                           'Becoming.Law.returns_iff', 'Becoming.Law.reachable_iff',
                                                           'Becoming.Law.keeps_iff']},
}
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('§1 "One base, the run" replaces "The two presentations, exactly"; the theory stated in full item 1, §8.1 item 1, "What this completeness is" and §9 (layers, import tree, receipt, counts) follow R28',
                                       '§1“一个基底：运行”取代“两种呈现，确切地说”；完整陈述第 1 条、§8.1 第 1 项、“这种完整是什么”与 §9（层、导入树、回执、计数）随 R28'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('the matching sentences of §1, item 1, §8.1 item 1 and §9 follow R28', '§1、第 1 条、§8.1 第 1 项与 §9 的对应句子随 R28'),
    CH + 'THE-THEORY-OF-BECOMING-REFERENCE.md': ('the module rows of World, Recurrence, Branching and Runs follow R28', 'World、Recurrence、Branching 与 Runs 的模块行随 R28'),
    STUDY: ('section 219 added', '新增第 219 节'),
    PKG + 'Becoming.lean': ('the header and the World and Runs notes state one base, the run', '开头与 World、Runs 的说明陈述一个基底：运行'),
    PKG + 'README.md': ('the layer paragraph and the base row state one base, the run', '层的段落与基底一行陈述一个基底：运行'),
    PKG + 'README.zh.md': ('the layer paragraph and the base row state one base, the run', '层的段落与基底一行陈述一个基底：运行'),
    PKG + 'check_becoming.py': ('the SCOPE text and a comment state one base, the run; no logic changed', 'SCOPE 文本与一条注释陈述一个基底：运行；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R28's run", '当前回执为 R28 之运行'),
}
LEAN_WHAT = {
    'World.lean': ('Dependence and WebAt moved in; Web is Dependence Nat; World is a relatum type with its history, a run of every step, read by World.web, World.flow and World.move, built by World.of; imports the frame',
                   'Dependence 与 WebAt 移入；Web 即 Dependence Nat；World 是关系项类型及其历史（每一步之运行），由 World.web、World.flow、World.move 读出，由 World.of 构造；导入框架'),
    'Runs.lean': ('WebAt moved to World.lean; World.webAt and Run.world read the history; World.run_history added; root paragraph',
                  'WebAt 移到 World.lean；World.webAt 与 Run.world 读历史；新增 World.run_history；根的段落'),
    'Recurrence.lean': ('imports the frame; Law.process, the five notions of every process and four orbit lemmas moved in; Law.Lossless, Merges, Returns, Reachable and KeepsPossibilities are abbreviations at Law.process with five unfolding lemmas; proofs take .mp/.mpr of them, statements unchanged',
                        '导入框架；Law.process、每个过程的五个概念与四条轨道引理移入；Law.Lossless、Merges、Returns、Reachable、KeepsPossibilities 是 Law.process 上的缩写，附五条展开引理；证明取其 .mp/.mpr，陈述不变'),
    'Branching.lean': ('the five notions and four orbit lemmas moved to Recurrence.lean; the five law_*_iff bridges are Iff.rfl',
                       '五个概念与四条轨道引理移到 Recurrence.lean；五座 law_*_iff 桥为 Iff.rfl'),
    'Labelled.lean': ('Law.process moved to Recurrence.lean; Frame.world built by World.of; header', 'Law.process 移到 Recurrence.lean；Frame.world 由 World.of 构造；开头说明'),
    'Dependence.lean': ('the structure Dependence moved to World.lean; docstrings', '结构 Dependence 移到 World.lean；说明'),
}
DEFAULT_LEAN = ('worlds built by World.of instead of the anonymous constructor, or the orbit forms of Law.* read through the unfolding lemmas, or a docstring no longer saying the module does not import the frame; statements unchanged',
                '世界改由 World.of 构造而非匿名构造子，或 Law.* 的轨道形式经展开引理读出，或说明不再说本模块不导入框架；陈述不变')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


changed = subprocess.run(['git', 'diff', '--name-only', BASE, '--'], capture_output=True, text=True, check=True).stdout.split()
changed += subprocess.run(['git', 'ls-files', '--others', '--exclude-standard', PKG + 'becoming-checks/' + RID],
                          capture_output=True, text=True, check=True).stdout.split()
LEAN = {p for p in changed if p.startswith(B) and p.endswith('.lean')}
WHAT = dict(DOCS)
for p in LEAN:
    WHAT[p] = LEAN_WHAT.get(p.rsplit('/', 1)[-1], DEFAULT_LEAN)
base = {}
for p in WHAT:
    out = subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True)
    base[p] = hashlib.sha256(out.stdout).hexdigest() if out.returncode == 0 else None

module_of = {receipt['source_paths'][m] if isinstance(receipt.get('source_paths'), dict) else None: m
             for m in receipt['source_sha256']}
module_of = {p: m for p, m in module_of.items() if p}
if not module_of:
    module_of = {B + m.split('.', 1)[1].replace('.', '/') + '.lean': m for m in receipt['source_sha256'] if m.startswith('Becoming.')}
elaborated = {}
for m in receipt['modules']:
    elaborated[m['module']] = {x['name'] if isinstance(x, dict) else x for x in m.get('declarations', [])}
for name, (_, new) in MOVES.items():
    assert name in elaborated[module_of[new]], (name, new)


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


def short(p):
    return p.rsplit('/', 1)[-1]


n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = d['id']
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by = {r['path']: r for r in refs}
    moved, added = [], []

    def ref_for(path, after):
        if path not in by:
            by[path] = {'path': path, 'role': 'proof', 'sha256': h(path), 'declarations': []}
            refs.insert(refs.index(after) + 1 if after in refs else len(refs), by[path])
        return by[path]

    for r in list(refs):
        if not r.get('declarations'):
            continue
        keep = []
        for x in r['declarations']:
            if x in MOVES and MOVES[x][0] == r['path']:
                target = ref_for(MOVES[x][1], r)
                if x not in target['declarations']:
                    target['declarations'].append(x)
                moved.append((x, r['path'], MOVES[x][1]))
            else:
                keep.append(x)
        r['declarations'] = keep
    for path, names in ADD.get(rid, {}).items():
        target = ref_for(path, refs[0])
        for x in names:
            assert x in elaborated[module_of[path]], x
            if x not in target['declarations']:
                target['declarations'].append(x)
                added.append(x)
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    if d.get('proof_bindings'):
        for _, _, path in moved:
            if path not in bound:
                d['proof_bindings'].append(binding(path))
                bound.add(path)
        for path in ADD.get(rid, {}):
            if path not in bound:
                d['proof_bindings'].append(binding(path))
                bound.add(path)
    rebound, touched = [], set()
    for b in d.get('proof_bindings', []):
        if b['source'] in LEAN and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source'])
            b['receipt'] = RECEIPT
            rebound.append(short(b['source']))
    for r in refs:
        p = r['path']
        if p in LEAN and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    # Empty references left by a move are dropped only where nothing else cites the file.
    for r in list(refs):
        if r['role'] == 'proof' and not r.get('declarations') and any(m[1] == r['path'] for m in moved) \
                and r['path'] != d.get('canonical_source') \
                and not any(b['source'] == r['path'] for b in d.get('proof_bindings', [])):
            refs.remove(r)
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R28 (one base by definition: a world is a run by its type; Web is Dependence Nat; Law.* are the notions of Law.process):'
    zh = '2026年10月20日，R28（按定义的一个基底：世界按其类型就是运行；Web 即 Dependence Nat；Law.* 即 Law.process 的概念）：'
    if moved:
        en += ' ' + '; '.join(f'{x.split("Becoming.", 1)[1]} moved from {short(a)} to {short(c)}' for x, a, c in moved) + ', with its full name.'
        zh += '；'.join(f'{x.split("Becoming.", 1)[1]} 从 {short(a)} 移到 {short(c)}' for x, a, c in moved) + '，名称不变。'
    if added:
        en += ' Added: ' + ', '.join(x.split('Becoming.', 1)[1] for x in added) + '.'
        zh += '新增：' + '、'.join(x.split('Becoming.', 1)[1] for x in added) + '。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    ps = sorted(touched)
    if ps:
        en += ' Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
        zh += '读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    if rid not in ADD:
        en += ' The claim is unchanged.'
        zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R28'):
        if ps:
            last['en'] = last['en'].rstrip() + ' Also re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
            last['zh'] = last['zh'].rstrip() + '另读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    else:
        d.setdefault('history', []).append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(moved), len(added), sorted(set(rebound)), len(ps))
print(n, 'records changed')
