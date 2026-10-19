#!/usr/bin/env python3
"""R32: sort the pure forwarders into removable and kept, with the reason for each kept one.

usage: python3 -B fwclass.py DUMP.json OUT.json

A forwarder T (dump field `f`, target G) is kept where:
- its statement names a witness: a closed value of the run, or a definition, inductive or constructor
  with no type parameter (dump field `g` = 0), that G's statement does not name (an instance at a model);
- it is cited by a text that is not re-pointed: the chapter (en, zh), OPENING (body and footnotes), the
  generativity chain, the other live documents under theories/ and sources/ and the RO and Y1 passage maps.
  A record, the reference catalogue or a Lean README citing a removed forwarder is re-pointed to the
  general law. Studies, reviews, receipts and kits under _process keep old names as history and are not
  read; the generated declaration pages are regenerated.
"""
import collections
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
DEV = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/'
# Texts re-pointed where they cite a removed forwarder; every other group blocks the removal.
REPOINTED = ('records', 'reference', 'lean readme')
TOKEN = re.compile(r"[A-Za-z_][\w'.!?]*")


def group(f):
    if f.startswith('theories/becoming/results/records/') and f.endswith('.json'):
        return 'records'
    if f.startswith('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE'):
        return 'reference'
    if f.startswith('theories/becoming/chapters/THE-THEORY-OF-BECOMING'):
        return 'chapter'
    if f == 'theories/becoming/OPENING.md':
        return 'opening'
    if f.endswith('GENERATIVITY-CHAIN.md'):
        return 'chain'
    if f.startswith('theories/becoming/results/lean-declarations/') or f.startswith('theories/becoming/results/LEAN-'):
        return None
    if f.startswith(('theories/', 'sources/')) and f.endswith('.md') and '/records/' not in f \
            and '/history/' not in f:
        return 'live text'
    if f in (LEAN + 'README.md', LEAN + 'README.zh.md'):
        return 'lean readme'
    if f.startswith((DEV + 'ro-relational-sources/', DEV + 'y1-changes/')) and f.endswith('.json'):
        return 'passage map'
    return None


def citation_index():
    files = subprocess.run(['git', 'ls-files'], cwd=ROOT, text=True, stdout=subprocess.PIPE).stdout.split('\n')
    index = {}
    for f in files:
        name = group(f) if f else None
        if not name:
            continue
        try:
            text = (ROOT / f).read_text(errors='ignore')
        except (IsADirectoryError, FileNotFoundError):
            continue
        for tok in set(TOKEN.findall(text)):
            parts = tok.rstrip('.').split('.')
            for i in range(len(parts)):
                index.setdefault('.'.join(parts[i:]), set()).add((name, f))
    return index


LAST = collections.Counter()


def unique_last(names):
    """Count the last components of the run's names, so a bare citation counts only for a unique one."""
    LAST.update(n.rsplit('.', 1)[-1] for n in names)


def cited(index, full):
    """Texts naming `full` by at least its last two components, or by its last one where that has an
    underscore (a word no prose uses) and no other name of the run ends with it."""
    short = full[len('Becoming.'):] if full.startswith('Becoming.') else full
    parts = short.split('.')
    keys = {'.'.join(parts[i:]) for i in range(len(parts) - 1)} if len(parts) > 1 else {short}
    if '_' in parts[-1] and LAST[parts[-1]] <= 1:
        keys.add(parts[-1])
    out = set()
    for k in keys:
        out |= index.get(k, set())
    return sorted(out)


def main():
    d = json.load(open(sys.argv[1]))
    c = d['c']

    def model(n):
        """A witness: a closed value of the run, or a type with no type parameter (with its constructors)
        declared outside the base modules, such as a model's states or moves."""
        x = c.get(n)
        if not x or x['k'] not in ('def', 'ind', 'ctor', 'opaque'):
            return False
        if x.get('cv'):
            return True
        if x['k'] == 'ctor':
            ind = next((y for y in x['v'] if c.get(y, {}).get('k') == 'ind'), None)
            return bool(ind) and model(ind)
        return x['k'] == 'ind' and x.get('g') == 0 and x['m'] not in BASE_MODULES

    # Modules defining the base and its vocabulary: a type of theirs without parameters (World, its relata)
    # is the base, not a model.
    BASE_MODULES = {'Becoming.World', 'Becoming.Frame', 'Becoming.Flow', 'Becoming.Dependence', 'GenerativeCore',
                    'Becoming.Prelude'}
    # who uses each forwarder (other than itself), for the report
    users = collections.defaultdict(set)
    for n, x in c.items():
        for y in set(x['t']) | set(x['v']):
            if y != n:
                users[y].add(n)

    index = citation_index()
    unique_last(c)
    res = {}
    for n, x in sorted(c.items()):
        if 'f' not in x or not x['m'].startswith('Becoming.'):
            continue
        g = x['f']
        names = {y for y in x['t'] if model(y)} - set(c[g]['t'])
        why = []
        if names:
            why.append('names a witness: ' + ', '.join(sorted(names)[:4]))
        where = cited(index, n)
        blocking = sorted({f for name, f in where if name not in REPOINTED})
        if blocking:
            why.append('cited: ' + ', '.join(blocking[:6]) + (' …' if len(blocking) > 6 else ''))
        res[n] = {'module': x['m'], 'target': g, 'target_module': c[g]['m'], 'kind': x['fk'],
                  'kept': why, 'removable': not why, 'users': sorted(users[n]),
                  'repoint': sorted({f for name, f in where if name in REPOINTED})}
    json.dump(res, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    print('forwarders', len(res), 'removable', sum(v['removable'] for v in res.values()),
          'witness', sum(any(w.startswith('names') for w in v['kept']) for v in res.values()),
          'cited', sum(any(w.startswith('cited') for w in v['kept']) for v in res.values()),
          'removable and re-pointed', sum(1 for v in res.values() if v['removable'] and v['repoint']))
    print('removable with Lean users', sum(1 for v in res.values() if v['removable'] and v['users']))
    print(collections.Counter(v['module'] for v in res.values() if v['removable']).most_common(50))


if __name__ == '__main__':
    main()
