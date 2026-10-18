#!/usr/bin/env python3
"""After apply_renames.py and a passing checker run: rename in live text and rebind the records (18 October 2026).

usage: python3 -B rebind_records.py TREE BASE RECEIPT_ID [TEXT_FILE ...]

TREE is the checkout the renames were applied to, BASE the commit they were applied on (the changed Lean files are
`git diff --name-only BASE` in TREE), RECEIPT_ID the passing core receipt in TREE. From RENAME-TABLE.json:
* in every result record, the live fields (not `history` or `text_versions`) name declarations by the new names:
  qualified names anywhere, and inside backticks also the unique components; prose words are not touched;
* each reference to a changed file gets its new hash and its renamed declarations; each proof binding to a changed
  Lean file is rebound to the receipt, which is added as a reference; a history note says what changed;
* each TEXT_FILE (the chapter, the package README, ...) gets the same identifier rewrite.
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TREE, BASE, RID = Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3]
TEXT = sys.argv[4:]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
data = json.loads((HERE / 'RENAME-TABLE.json').read_text())
full, GLOBAL = data['renamed'], data['global_components']

windows = {}
for old, new in full.items():
    o, n = old.split('.')[1:], new.split('.')[1:]
    for k in range(2, len(o) + 1):
        windows[tuple(o[-k:])] = n[-k:]
    windows[('Becoming',) + tuple(o)] = ['Becoming'] + n
DOT = dict(GLOBAL)
for o, n in (('Registers', 'CoupledInto'), ('RegistersAlike', 'AlikeThrough'), ('RegistersAlikeUpTo', 'AlikeThroughUpTo'),
             ('RegistersAlikeAll', 'AlikeThroughAll'), ('Belief', 'ClassThrough'), ('Refutes', 'Excludes'),
             ('RefutesWithin', 'ExcludesWithin'), ('RefutesBy', 'ExcludesBy')):
    DOT[o] = n
IDENT = re.compile(r"(?<![A-Za-z0-9_'!?])\.?[A-Za-z_][A-Za-z0-9_'!?]*(?:\.[A-Za-z_][A-Za-z0-9_'!?]*)*")


def rename_ident(tok, bare):
    lead = tok.startswith('.')
    c = tok[1:].split('.') if lead else tok.split('.')
    out = list(c)
    for i in range(len(c)):
        hit = False
        for k in range(min(i + 1, 6), 0, -1):
            w = tuple(c[i - k + 1:i + 1])
            if w in windows and (k >= 2 or w[0] == 'Becoming'):
                out[i - k + 1:i + 1] = windows[w]
                hit = True
                break
        if hit or not bare:
            continue
        if i == 0 and not lead:
            out[i] = GLOBAL.get(c[i], c[i])
        else:
            out[i] = DOT.get(c[i], c[i])
    s = '.'.join(out)
    return '.' + s if lead else s


def rewrite(s):
    """Qualified names anywhere; inside backticks, unique components too."""
    parts = re.split(r'(`[^`\n]+`)', s)
    out = []
    for p in parts:
        if p.startswith('`') and p.endswith('`') and len(p) > 1:
            out.append('`' + IDENT.sub(lambda m: rename_ident(m.group(0), True), p[1:-1]) + '`')
        else:
            out.append(IDENT.sub(lambda m: rename_ident(m.group(0), False), p))
    return ''.join(out)


def walk(x, key=None):
    if isinstance(x, str):
        return full.get(x, rewrite(x)) if key != 'path' else x
    if isinstance(x, list):
        return [walk(v, key) for v in x]
    if isinstance(x, dict):
        return {k: (v if k in ('history', 'text_versions', 'sha256', 'path') else walk(v, k)) for k, v in x.items()}
    return x


changed = set(subprocess.run(['git', '-C', str(TREE), 'diff', '--name-only', BASE], capture_output=True, text=True,
                             check=True).stdout.split())
for f in TEXT:
    p = TREE / f
    t = p.read_text()
    n = rewrite(t)
    if n != t:
        p.write_text(n)
        changed.add(f)
h = lambda p: hashlib.sha256((TREE / p).read_bytes()).hexdigest()
lean_changed = sorted(f for f in changed if f.endswith('.lean'))
summary = {'records_text': [], 'records_rebound': []}
for p in sorted((TREE / 'theories/becoming/results/records').glob('*.json')):
    d = json.loads(p.read_text())
    before = json.dumps(d, ensure_ascii=False)
    d2 = walk(d)
    text_changed = json.dumps({k: v for k, v in d2.items() if k != 'references'}, ensure_ascii=False) != \
        json.dumps({k: v for k, v in d.items() if k != 'references'}, ensure_ascii=False)
    d = d2
    files, rebound = [], []
    for r in d.get('references', []):
        if r.get('path') in changed:
            r['sha256'] = h(r['path'])
            files.append(r['path'].rsplit('/', 1)[-1])
    for b in d.get('proof_bindings', []):
        if b.get('source') in lean_changed and b.get('receipt') != RECEIPT:
            b['receipt'] = RECEIPT
            rebound.append(b['source'].rsplit('/', 1)[-1])
    if rebound and not any(r.get('path') == RECEIPT for r in d['references']):
        d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    note = ("18 October 2026, the N1 renaming (Ren: \"Renames, full scope\"; adopted vocabulary of the naming study, "
            "section 7): declarations renamed as in development/n1-migration/RENAME-TABLE.json, the statements and "
            "proofs otherwise unchanged.")
    if text_changed:
        note += " This record's live fields name the declarations by their new names; prose words are unchanged."
    if files:
        note += " Changed by the renaming: " + ", ".join(sorted(set(files))) + "."
    if rebound:
        note += f" Rebound to core receipt {RID} after reading the change."
    note += " The claim is unchanged."
    d['history'].append({'en': note})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    (summary['records_rebound'] if rebound else summary['records_text']).append(p.stem)
print(json.dumps({k: len(v) for k, v in summary.items()} | {'lean_changed': len(lean_changed)}, indent=1))
