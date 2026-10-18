#!/usr/bin/env python3
"""F3J, sub-chain 1 (18 October 2026): rebind the result records to the new core modules.

usage (from the checkout root): python3 -B rebind_f3j.py BASE RECEIPT_ID

BASE is the main commit the port is applied on; RECEIPT_ID the passing core receipt in this checkout.
A port restates; it adds no result. For every record:
* each periphery or bridge declaration a `proof` reference lists, which `map_s1.MAP` gives core
  counterparts for (port-j.md, sections 3 and 4), adds those counterparts to a proof reference to the
  core module the receipt says elaborates them (added, with its hash, where the record had none), with a
  proof binding to the receipt for that source; the periphery and bridge references stay, since those
  modules stay in the run until the sweep retires them;
* a canonical source that is a ported periphery module (`map_s1.CANONICAL`) moves to its core module;
* every proof binding to a package Lean file changed since BASE whose bytes no longer match the hash its
  receipt records is rebound to the receipt (a binding stale at BASE, in a file the port leaves alone,
  is left as it was);
* a history note names F3J and says what was added. Claims are unchanged.
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from map_s1 import MAP, CANONICAL  # noqa: E402

BASE, RID = sys.argv[1], sys.argv[2]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
path_of = {m: LEAN + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}
home = {}
for m in receipt.get('modules', []):
    for d in m.get('declarations', []):
        if isinstance(d, dict):
            home.setdefault(d['name'], m['module'])
NEW = {'Becoming.Lexical', 'Becoming.Frontier', 'Becoming.ScoreRepresentation', 'Becoming.Alternatives',
       'Becoming.Bundles', 'Becoming.Narrowing'}
missing = sorted({c for cs in MAP.values() for c in cs if c not in home})
if missing:
    sys.exit('not elaborated in the receipt: ' + ', '.join(missing))

changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True,
                             check=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


summary = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by_path = {r['path']: r for r in refs}
    added = {}
    for r in list(refs):
        if r.get('role') != 'proof' or not r.get('declarations'):
            continue
        for name in r['declarations']:
            for core in MAP.get(name, []):
                dest = path_of[home[core]]
                if dest not in by_path:
                    by_path[dest] = {'path': dest, 'role': 'proof', 'sha256': h(dest), 'declarations': []}
                    refs.append(by_path[dest])
                if core not in by_path[dest]['declarations']:
                    by_path[dest]['declarations'].append(core)
                    added.setdefault(home[core], []).append(core)
    moved_canonical = None
    src = d.get('canonical_source', '')
    if src.rsplit('/', 1)[-1] in CANONICAL and added:
        target = 'Becoming.' + CANONICAL[src.rsplit('/', 1)[-1]][:-5]
        d['canonical_source'] = path_of[target]
        moved_canonical = (src.rsplit('/', 1)[-1], CANONICAL[src.rsplit('/', 1)[-1]])
    bindings = d.setdefault('proof_bindings', [])
    bound = {b['source'] for b in bindings}
    for m in added:
        if path_of[m] not in bound:
            bindings.append(binding(path_of[m]))
            bound.add(path_of[m])
    rebound = []
    for b in bindings:
        if b['receipt'] == RECEIPT or b['source'] not in module_of or b['source'] not in changed:
            continue
        old = json.load(open(b['receipt'])).get('source_sha256', {}).get(b['sha256_pointer'].rsplit('/', 1)[-1])
        if old != h(b['source']):
            b['receipt'] = RECEIPT
            rebound.append(b['source'].rsplit('/', 1)[-1])
    for r in refs:
        p = r['path']
        if p in module_of and any(b['source'] == p and b['receipt'] == RECEIPT for b in bindings):
            r['sha256'] = h(p)
    if any(b['receipt'] == RECEIPT for b in bindings) and RECEIPT not in by_path:
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    note = ('18 October 2026, F3J, the port of the judgment and comparison family into the core (Ren: "work with '
            'other sessions, totally resolve these extra/ugly bridges, and move toward to the direction of '
            'unification"):')
    if added:
        note += (' the core counterparts of the cited periphery and bridge declarations are cited ('
                 + '; '.join(f'{len(v)} in {m}' for m, v in sorted(added.items()))
                 + '), graded in development/bridge-fold/port-j.md; the periphery stays cited until the sweep '
                   'retires it.')
    if moved_canonical:
        note += f' Canonical source moved from {moved_canonical[0]} to {moved_canonical[1]}.'
    if rebound:
        note += f' Rebound to core receipt {RID} after reading the change ({", ".join(sorted(set(rebound)))}).'
    note += ' A port restates; the claim is unchanged.'
    d['history'].append({'en': note, 'zh': '2026年10月18日，F3J 将判断与比较族移入核心：引用其核心对应声明'
                         + ('，规范来源随之移动' if moved_canonical else '') + '。移植只是重述，论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], {m: len(v) for m, v in added.items()}, moved_canonical, sorted(set(rebound))))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
