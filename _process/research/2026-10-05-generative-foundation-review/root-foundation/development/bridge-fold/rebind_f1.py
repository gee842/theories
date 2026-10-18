#!/usr/bin/env python3
"""F1, the bridge fold (18 October 2026): rebind the result records after a passing checker run.

usage (from the checkout root): python3 -B rebind_f1.py BASE RECEIPT_ID

BASE is the commit the fold was applied on; RECEIPT_ID the passing core receipt in this checkout.
Declarations moved between files with their full Lean names, statements and proofs unchanged. For
every record:
* each declaration a `proof` reference lists under a package Lean file is looked up among the
  declarations the receipt says Lean elaborated for each module; where it is now elaborated in
  another module, it moves to a reference to that module's source (added, with the source's hash,
  where the record had none), and a proof binding to the receipt is added for that source;
* a reference left with no declarations, where it had some, is removed with its binding, unless it is
  the canonical source, which then follows the declarations;
* every proof binding to a package Lean file changed since BASE whose bytes no longer match the hash
  its receipt records is rebound to the receipt, and the reference's hash follows the source (a binding
  already stale at BASE, in a file the fold leaves alone, is left as it was);
* other files changed since BASE are re-pointed only where the reference matched the file at BASE
  (a reference already stale at BASE is left as it was);
* a history note says what moved and what was rebound. Claims are unchanged.
"""
import glob
import hashlib
import json
import subprocess
import sys

BASE, RID = sys.argv[1], sys.argv[2]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
paths = receipt['source_paths']
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
path_of = {m: LEAN + p for m, p in paths.items()}
module_of = {p: m for m, p in path_of.items()}
home = {}
for m in receipt.get('modules', []):
    for d in m.get('declarations', []):
        if isinstance(d, dict):
            home.setdefault(d['name'], m['module'])

changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True,
                             check=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True)
                                   .stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed if not p.endswith('.json') or 'records' not in p}


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


WHAT = {
    'THE-THEORY-OF-BECOMING.md': "section 2's closure sentence names Becoming.EdgeClosure; section 9's bridge bullet "
                                 'says what the fold moved, and its counts, receipt and connectivity follow the F1 run',
    'THE-THEORY-OF-BECOMING.zh.md': 'the closure sentence and the module rows follow the fold',
    'THE-THEORY-OF-BECOMING-REFERENCE.md': 'rows for the four new core modules; the Bridge and RenewalBridge rows and '
                                           'the bridge total follow the fold',
    'README.md': 'module rows follow the fold',
}
summary = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by_path = {r['path']: r for r in refs}
    moved = []
    for r in list(refs):
        if r.get('role') != 'proof' or r['path'] not in module_of or not r.get('declarations'):
            continue
        here = module_of[r['path']]
        keep = []
        for name in r['declarations']:
            to = home.get(name)
            if to is None or to == here or to not in path_of:
                keep.append(name)
                continue
            dest = path_of[to]
            if dest not in by_path:
                by_path[dest] = {'path': dest, 'role': 'proof', 'sha256': h(dest), 'declarations': []}
                refs.insert(refs.index(r) + 1, by_path[dest])
            if name not in by_path[dest]['declarations']:
                by_path[dest]['declarations'].append(name)
            moved.append((name, r['path'].rsplit('/', 1)[-1], dest.rsplit('/', 1)[-1]))
        r['declarations'] = keep
        if not keep:
            dests = [path_of[home[n]] for n, s, _ in moved if s == r['path'].rsplit('/', 1)[-1]]
            if d.get('canonical_source') == r['path'] and dests:
                d['canonical_source'] = max(set(dests), key=dests.count)
            refs.remove(r)
            del by_path[r['path']]
            d['proof_bindings'] = [b for b in d.get('proof_bindings', []) if b['source'] != r['path']]
    bound = {b['source'] for b in d.get('proof_bindings', [])}
    for _, _, dest in moved:
        src = next(p for p in by_path if p.rsplit('/', 1)[-1] == dest and p in module_of)
        if src not in bound and d.get('proof_bindings') is not None and bound:
            d['proof_bindings'].append(binding(src))
            bound.add(src)
    rebound = []
    repointed = []
    for b in d.get('proof_bindings', []):
        if b['receipt'] == RECEIPT or b['source'] not in module_of or b['source'] not in changed:
            continue
        old = json.load(open(b['receipt'])).get('source_sha256', {}).get(b['sha256_pointer'].rsplit('/', 1)[-1])
        if old != h(b['source']):
            b['receipt'] = RECEIPT
            rebound.append(b['source'].rsplit('/', 1)[-1])
    for r in refs:
        p = r['path']
        if p in module_of and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            r['sha256'] = h(p)
        elif p in changed and p in BASE_SHA and r.get('sha256') == BASE_SHA[p] != h(p):
            r['sha256'] = h(p)
            repointed.append(p.rsplit('/', 1)[-1])
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and RECEIPT not in by_path:
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    note = ('18 October 2026, F1, the bridge fold (Ren: "so there seems to be a lot bridges in our code, how do '
            'they work? do we really need a bridge?", then "please do all"):')
    if moved:
        groups = {}
        for n, s, t in moved:
            groups.setdefault((s, t), []).append(n.rsplit('.', 1)[-1])
        note += (' declarations moved with their full Lean names, statements and proofs unchanged: '
                 + '; '.join(f'{", ".join(v)} from {s} to {t}' for (s, t), v in groups.items()) + '.')
    if rebound:
        note += f' Rebound to core receipt {RID} after reading the change ({", ".join(sorted(set(rebound)))}).'
    if repointed:
        note += (' Re-pointed after reading the change ('
                 + '; '.join(f'{x}: {WHAT.get(x, "the fold")}' for x in sorted(set(repointed))) + ').')
    note += ' The claim is unchanged.'
    last = d['history'][-1] if d['history'] else {}
    if last.get('en', '').startswith('18 October 2026, F1'):
        last['en'] += note[note.index(':', note.index('"please do all"')) + 1:]
        if 'zh' in last:
            last['zh'] += ('声明连同完整 Lean 名称、陈述与证明原样移入核心模块；' if moved else '') + '读过改动后重新绑定或重新指向。论断不变。'
    else:
        d['history'].append({'en': note, 'zh': '2026年10月18日，F1 桥接折叠：' + ('声明连同完整 Lean 名称、陈述与证明原样移入核心模块；' if moved else '')
                             + ('读过改动后重新绑定或重新指向。' if rebound or repointed else '') + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], len(moved), sorted(set(rebound))))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
