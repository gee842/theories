#!/usr/bin/env python3
"""F3, the periphery port's sweep: rebind the result records after a passing checker run.

usage (from the checkout root): python3 -B rebind_f3.py BASE RECEIPT_ID STEP [MACHINE_RECEIPT_ID]

BASE is the main commit the sweep step was applied on; RECEIPT_ID the passing core receipt in this
checkout; STEP the sweep step's label (for example "step 1"). Adapted from F1's rebind_f1.py: the sweep
removes declarations that read only superseded periphery modules and moves none. For every record:
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
* (final sweep) a reference whose path `research.py move` re-pointed from the package to
  `lean/history/becoming/` since BASE is named in the note: its bytes and the receipt binding it are
  unchanged; with MACHINE_RECEIPT_ID, a binding of `MachineInstances.lean` whose receipt no longer
  holds its bytes is rebound to that MachineInstances receipt;
* a history note says what moved and what was rebound. Claims are unchanged.
"""
import glob
import hashlib
import json
import subprocess
import sys

BASE, RID, STEP = sys.argv[1], sys.argv[2], sys.argv[3]
MRID = sys.argv[4] if len(sys.argv) > 4 else None
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


MACHINE = LEAN + 'universal-ethics/generative-capacity/MachineInstances.lean'
MRECEIPT = (LEAN + 'universal-ethics/generative-capacity/machine-instances-checks/' + MRID + '/verification.json'
            if MRID else None)
HISTORY = LEAN + 'history/becoming/'


def at_base_record(f):
    shown = subprocess.run(['git', 'show', f'{BASE}:{f}'], capture_output=True, text=True)
    return json.loads(shown.stdout) if shown.returncode == 0 else {}


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


WHAT = {
    'THE-THEORY-OF-BECOMING.md': "section 9's receipt, counts, rings and connectivity follow the final sweep's run (no "
                                 'bridge, no join, 75 superseded modules); sentences of sections 6 and 8 that named '
                                 'bridge declarations name their core statements',
    'THE-THEORY-OF-BECOMING.zh.md': 'the bridge rows and the sentences naming bridge declarations follow the sweep',
    'THE-THEORY-OF-BECOMING-REFERENCE.md': 'the bridge section says the bridge is in history since the sweep',
    'README.md': 'the rings, joins and verification text follow the sweep',
    'GranularityBridge.lean': 'the readings of the superseded ExplanatoryResiduals left the module; the declarations '
                              'the record cites are unchanged',
}
summary = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    before = json.dumps(d, ensure_ascii=False)
    base_paths = {r['path'] for r in at_base_record(f).get('references', [])}
    filed = sorted({r['path'].rsplit('/', 1)[-1] for r in d.get('references', []) if r['path'].startswith(HISTORY)
                    and r['path'] not in base_paths and PKG + r['path'][len(HISTORY):] in base_paths})
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
    machine = False
    for b in d.get('proof_bindings', []):
        if MRECEIPT and b['source'] == MACHINE and b['receipt'] != MRECEIPT:
            old = json.load(open(b['receipt'])).get('source_sha256', {}).get('MachineInstances')
            if old != h(MACHINE):
                b['receipt'] = MRECEIPT
                machine = True
            continue
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
        elif machine and p == MACHINE:
            r['sha256'] = h(p)
        elif p in changed and p in BASE_SHA and r.get('sha256') == BASE_SHA[p] != h(p):
            r['sha256'] = h(p)
            repointed.append(p.rsplit('/', 1)[-1])
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and RECEIPT not in by_path:
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if machine and MRECEIPT not in by_path:
        refs.append({'path': MRECEIPT, 'role': 'receipt', 'sha256': h(MRECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before and not filed:
        continue
    note = (f'19 October 2026, F3 sweep {STEP} (Ren: "work with other sessions, totally resolve these extra/ugly '
            'bridges, and move toward to the direction of unification"):')
    if moved:
        groups = {}
        for n, s, t in moved:
            groups.setdefault((s, t), []).append(n.rsplit('.', 1)[-1])
        note += (' declarations moved with their full Lean names, statements and proofs unchanged: '
                 + '; '.join(f'{", ".join(v)} from {s} to {t}' for (s, t), v in groups.items()) + '.')
    if rebound:
        note += f' Rebound to core receipt {RID} after reading the change ({", ".join(sorted(set(rebound)))}).'
    if filed:
        note += (' The bridge and join files it cites left the package with the periphery modules they read, '
                 'whose content the core now states (the bridge-fold port files): '
                 + ', '.join(filed) + (' are' if len(filed) > 1 else ' is') + ' in lean/history/becoming/ with '
                 + ('their' if len(filed) > 1 else 'its') + ' bytes, bound to the receipts that checked '
                 + ('them.' if len(filed) > 1 else 'it.'))
    if machine:
        note += (f' MachineInstances now states the two lemmas it took from the bridge module Instances; rebound to '
                 f'its receipt {MRID}.')
    if repointed:
        note += (' Re-pointed after reading the change ('
                 + '; '.join(f'{x}: {WHAT.get(x, "the fold")}' for x in sorted(set(repointed))) + ').')
    note += ' The claim is unchanged.'
    d['history'].append({'en': note, 'zh': f'2026年10月19日，F3 清扫 {STEP}：' + ('所引桥接与接合文件连同字节移入 lean/history/becoming/，仍绑定检查过它们的回执。' if filed else '') + ('读过改动后重新绑定或重新指向。' if rebound or repointed or machine else '') + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], len(moved), sorted(set(rebound)), len(filed), machine))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
