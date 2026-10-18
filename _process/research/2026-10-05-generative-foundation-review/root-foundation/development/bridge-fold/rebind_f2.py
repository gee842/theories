#!/usr/bin/env python3
"""F2, joins into the core (18 October 2026): rebind the result records after a passing checker run.

usage (from the checkout root): python3 -B rebind_f2.py BASE RECEIPT_ID

BASE is the commit F2 was applied on; RECEIPT_ID the passing core receipt in this checkout. The
mechanics are F1's (`rebind_f1.py`): declarations that moved keep their full Lean names. For
every record:
* each declaration a `proof` reference lists under a package Lean file is looked up among the
  declarations the receipt says Lean elaborated for each module; where it is now elaborated in
  another module, it moves to a reference to that module's source (added, with the source's hash,
  where the record had none), and a proof binding to the receipt is added for that source;
* a reference left with no declarations, where it had some, is removed with its binding, unless it is
  the canonical source, which then follows the declarations;
* every proof binding to a package Lean file whose bytes no longer match the hash its receipt
  records is rebound to the receipt, and the reference's hash follows the source;
* other files changed since BASE are re-pointed only where the reference matched the file at BASE
  (a reference already stale at BASE is left as it was);
* a history note says what moved and what was rebound. Claims are unchanged.
Then, for the three records whose canonical source F2 ported (PORT-PROGRAM rule 6, `port-f2.md`):
the canonical source becomes the core module stating the record's law, a proof reference to the
F2 core module that states the rest is added with its declarations and bound to the receipt, and
the history note says so.
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


def resolve(doc, pointer):
    """The value at a JSON pointer, or None where it does not resolve (F2: F1's version read every receipt's
    `source_sha256`, which periphery receipts do not have, and so rebound valid bindings)."""
    for part in pointer.lstrip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        if isinstance(doc, dict) and part in doc:
            doc = doc[part]
        elif isinstance(doc, list) and part.isdigit() and int(part) < len(doc):
            doc = doc[int(part)]
        else:
            return None
    return doc if isinstance(doc, str) else None


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


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
    for b in d.get('proof_bindings', []):
        if b['receipt'] == RECEIPT or b['source'] not in module_of:
            continue
        old = resolve(json.load(open(b['receipt'])), b['sha256_pointer'])
        if old is not None and old != h(b['source']):
            b['receipt'] = RECEIPT
            b['sha256_pointer'] = '/source_sha256/' + module_of[b['source']]
            rebound.append(b['source'].rsplit('/', 1)[-1])
    for r in refs:
        p = r['path']
        if p in module_of and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            r['sha256'] = h(p)
        elif p in changed and p in BASE_SHA and r.get('sha256') == BASE_SHA[p] != h(p):
            r['sha256'] = h(p)
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and RECEIPT not in by_path:
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    note = ('18 October 2026, F2, joins into the core (Ren: "please, do them, reduce bridges and add more theory '
            'to the spine"): declarations moved with their full Lean names.')
    if moved:
        groups = {}
        for n, s, t in moved:
            groups.setdefault((s, t), []).append(n.rsplit('.', 1)[-1])
        note += ' Moved: ' + '; '.join(f'{", ".join(v)} from {s} to {t}' for (s, t), v in groups.items()) + '.'
    if rebound:
        note += f' Rebound to core receipt {RID} after reading the change ({", ".join(sorted(set(rebound)))}).'
    note += ' The claim is unchanged.'
    last = d['history'][-1] if d['history'] else {}
    if last.get('en', '').startswith('18 October 2026, F2'):
        last['en'] += note[note.index(':', note.index('to the spine"')) + 1:]
    else:
        d['history'].append({'en': note})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], len(moved), sorted(set(rebound))))
PORTED = {
    'becoming-context-coherence': ('Context', 'ContextArrivalTraces', 'BecomingCompatibility',
        ['Becoming.ContextArrivalTraces.step_arrives', 'Becoming.ContextArrivalTraces.empty_support_no_arrival',
         'Becoming.ContextArrivalTraces.changed_context_arrives']),
    'derived-history-law-exactness': ('Readout', 'SummaryFutures', 'DerivedHistoryLaw',
        ['Becoming.SummaryFutures.every_word', 'Becoming.SummaryFutures.futures_through',
         'Becoming.SummaryFutures.endpoint_moved']),
    'endpoint-loss-and-return': ('Recurrence', 'Irreversibility', 'BecomingReversibility',
        ['Becoming.Irreversibility.deadEnd_no_return', 'Becoming.Irreversibility.same_change_different_return',
         'Becoming.Irreversibility.constant_reading_hides_loss']),
}
for rid, (law, extra, old, names) in PORTED.items():
    f = f'theories/becoming/results/records/{rid}.json'
    d = json.load(open(f))
    canon, src = path_of['Becoming.' + law], path_of['Becoming.' + extra]
    refs = d['references']
    if not any(r['path'] == src for r in refs):
        at = next(i for i, r in enumerate(refs) if r['path'] == canon) + 1 if any(r['path'] == canon for r in refs) else len(refs)
        refs.insert(at, {'path': src, 'role': 'proof', 'sha256': h(src), 'declarations': names})
    if not any(b['source'] == src for b in d['proof_bindings']):
        d['proof_bindings'].append(binding(src))
    if not any(b['source'] == canon for b in d['proof_bindings']):
        d['proof_bindings'].append(binding(canon))
    if RECEIPT not in {r['path'] for r in refs}:
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    d['canonical_source'] = canon
    note = (f'18 October 2026, F2 (Ren: "please, do them, reduce bridges and add more theory to the spine"): every '
            f'theorem of {old}.lean is stated in the core (port-f2.md, all graded same or step). The canonical source '
            f'is now {law}.lean; {extra}.lean states the rest ({", ".join(n.rsplit(".", 1)[-1] for n in names)}). '
            f'{old}.lean keeps its path and bytes and its old receipt; its retirement from the run is the sweep\'s (F3). '
            f'The claim is unchanged.')
    d['history'].append({'en': note})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((rid, 'ported', old))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
