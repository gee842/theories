#!/usr/bin/env python3
"""F3Q (18 October 2026): rebind the records whose proofs cite the family to its core statements.

usage (from the checkout root): python3 -B rebind_q.py RECEIPT_ID [MODULE ...]

RECEIPT_ID is the passing core receipt in this checkout; MODULE limits the run to records citing
those periphery or join modules (default: every module of `port_q.FAMILY` and `port_q.JOINS`). A
port is not a new result: claims are unchanged. For every record with a proof reference to a family
or join file:
* each cited declaration with a core counterpart in `port_q.py` gains that counterpart in a proof
  reference to the core source that elaborates it (added, with the source's hash, where the record
  had none), and in every law listing the declaration, right after it; the periphery reference stays
  until the sweep retires the module;
* the canonical source moves to the core source holding most of the counterparts, where it was a
  family file;
* a proof binding to the receipt is added for each core source gained, with the receipt as a
  reference;
* a history note names F3Q and says what was added, including where a proof became constructive.
Declarations of a join or bridge file that `port_q.py` does not list (another family's) are left
alone. Idempotent.
"""
import glob
import hashlib
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import port_q  # noqa: E402

RID = sys.argv[1]
ONLY = set(sys.argv[2:])
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEAN + 'becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed', receipt['status']
path_of = {m: LEAN + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}
home = {}
for m in receipt.get('modules', []):
    for d in m.get('declarations', []):
        if isinstance(d, dict):
            home.setdefault(d['name'], m['module'])

TABLES = {**port_q.FAMILY, **port_q.JOINS}


def table(module):
    """Short name -> core counterparts, for one family or join module."""
    out = {}
    for old, _, after, counterpart, _ in TABLES[module]['rows']:
        if after.startswith('same') or after == 'step':
            out[old] = [c.strip() for c in counterpart.split(', ')]
    return out


FAMILY_PATHS = {LEAN + d['path']: name for name, d in TABLES.items()}
if ONLY:
    FAMILY_PATHS = {p: n for p, n in FAMILY_PATHS.items() if n in ONLY}

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
    added = {}            # core source -> new names
    new_of = {}           # old full name -> new full names
    from_canonical = []
    for r in list(refs):
        if r.get('role') != 'proof' or r['path'] not in FAMILY_PATHS or not r.get('declarations'):
            continue
        tab = table(FAMILY_PATHS[r['path']])
        for name in r['declarations']:
            news = tab.get(name.rsplit('.', 1)[-1])
            if not news:
                continue
            for new in news:
                mod = home.get(new)
                assert mod in path_of, (f, name, new)
                src = path_of[mod]
                if src not in by_path:
                    by_path[src] = {'path': src, 'role': 'proof', 'sha256': h(src), 'declarations': []}
                    refs.insert(refs.index(r) + 1, by_path[src])
                if new not in by_path[src]['declarations']:
                    by_path[src]['declarations'].append(new)
                added.setdefault(src, []).append(new)
                new_of.setdefault(name, []).append(new)
                if d.get('canonical_source') == r['path']:
                    from_canonical.append(src)
    if not added:
        continue
    for law in d.get('laws', []):
        decls = law.get('declarations', [])
        out = []
        for n in decls:
            out.append(n)
            out += [m for m in new_of.get(n, []) if m not in decls and m not in out]
        law['declarations'] = out
    if from_canonical:
        d['canonical_source'] = max(set(from_canonical), key=from_canonical.count)
    if d.get('proof_bindings') is not None:
        bound = {(b['source'], b['receipt']) for b in d['proof_bindings']}
        for src in added:
            if (src, RECEIPT) not in bound:
                d['proof_bindings'].append(binding(src))
        if RECEIPT not in by_path:
            refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    for src in added:
        by_path[src]['sha256'] = h(src)
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    mods = sorted({module_of[s].split('.', 1)[-1] for s in added})
    note = ('18 October 2026, F3Q, the port of the inquiry and composition family into the core (Ren: '
            '"work with other sessions, totally resolve these extra/ugly bridges, and move toward to the direction '
            'of unification"): the core statements of the cited declarations are added beside them ('
            + ', '.join(mods) + '; verdicts in port-q.md), bound to core receipt ' + RID
            + (', and the canonical source is the core module' if from_canonical else '')
            + '. Every core statement has an empty axiom report; where the periphery proof was classical, the core '
              'proof is constructive or names its hypothesis (port-q.md). The periphery references stay until the '
              'sweep retires their modules. No new result; the claim is unchanged.')
    if not any(n.get('en') == note for n in d.get('history', [])):
        d.setdefault('history', []).append({
            'en': note, 'zh': '2026年10月18日，F3Q 将探究与组合族移入核心：所引声明旁加上核心陈述（'
            + '、'.join(mods) + '），绑定到核心回执；核心陈述的公理报告皆为空，外围经典证明处核心证明为构造性或明示其假设；'
            '外围引用保留到清扫退役其模块。无新结果，论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], {module_of[s]: len(v) for s, v in added.items()}))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
