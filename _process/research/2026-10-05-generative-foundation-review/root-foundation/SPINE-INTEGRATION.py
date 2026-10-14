#!/usr/bin/env python3
"""How much of the repository's Lean the Becoming spine run compiles: python3 -B SPINE-INTEGRATION.py [RECEIPT]

Reads the consolidated checker's receipt (by default `becoming-verification.json`, the latest passed run) and prints,
as JSON:

* records: each result record by where its claim is proved. `stated on the spine` has its canonical source in the core,
  the foundation or the bridge, or an alias naming a declaration of the `Becoming` package; otherwise the main proof
  (the canonical source where it is Lean, else the first Lean proof cited) is `in an inherited module` the spine run
  compiles because the bridge imports it, or `outside the spine run`; `no Lean proof` cites none. Counted apart, more
  widely: the records citing some proof in the core, the foundation or the bridge.
* lean: theorem declarations in tracked Lean files outside the run, counted once per (file stem, name). A stem the run compiles is an older
  version of a run module and is left out; a declaration found only under a copy or evidence path (run folders,
  verification history, sources, snapshots) is counted apart from those in live paths, which are grouped by family.

A measurement, not a check: it reads text with regular expressions and does not run Lean."""
import collections
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
COPY = re.compile(r'(-checks/|verification-history|verification-runs|/runs?/|/history/|frozen|snapshot|^sources/|evidence)')
DECL = re.compile(r'^\s*(?:private\s+|protected\s+)*(?:theorem|lemma)\s+(\S+)', re.M)


def main():
    os.chdir(ROOT)
    receipt_path = sys.argv[1] if len(sys.argv) > 1 else L + 'becoming/becoming-verification.json'
    receipt = json.loads(Path(receipt_path).read_text())
    layer = {m['module']: m.get('layer') for m in receipt['modules']}
    in_run = {os.path.normpath(L + p): layer.get(mod) for mod, p in receipt['source_paths'].items()}
    run_stems = {Path(p).stem for p in in_run}

    records, citing = collections.defaultdict(list), 0
    config = json.loads(Path('_process/research-config.json').read_text())
    for directory in config['record_directories']:
        for path in sorted(Path(directory).glob('*.json')):
            record = json.loads(path.read_text())
            lean = [os.path.normpath(r['path']) for r in record.get('references', [])
                    if r.get('role') == 'proof' and r['path'].endswith('.lean')]
            source = os.path.normpath(record.get('canonical_source', ''))
            main = source if source.endswith('.lean') else (lean[0] if lean else None)
            if in_run.get(source) in ('core', 'foundation', 'bridge') or '/becoming/Becoming/' in source or any(
                    str(a).startswith('Becoming.') for a in record.get('aliases', [])):
                kind = 'stated on the spine'
            elif main is None:
                kind = 'no Lean proof'
            elif in_run.get(main) == 'inherited':
                kind = 'in an inherited module'
            elif in_run.get(main) in ('core', 'foundation', 'bridge'):
                kind = 'stated on the spine'
            else:
                kind = 'outside the spine run'
            records[kind].append(record['id'])
            citing += any(in_run.get(p) in ('core', 'foundation', 'bridge') or '/becoming/Becoming/' in p for p in lean)

    names = collections.defaultdict(set)
    tracked = subprocess.run(['git', 'ls-files', '-z', '--', '*.lean'], capture_output=True, check=True).stdout
    for p in sorted(os.path.normpath(t) for t in tracked.decode().split('\0') if t):
        path = Path(p)
        if p in in_run or path.stem in run_stems:
            continue
        for name in DECL.findall(path.read_text(encoding='utf-8', errors='replace')):
            names[(path.stem, name)].add(p)
    live, stems, copies = collections.Counter(), collections.defaultdict(set), 0
    for (stem, _), paths in names.items():
        live_paths = sorted(p for p in paths if not COPY.search(p))
        if not live_paths:
            copies += 1
            continue
        parts = live_paths[0].split('/')
        family = '/'.join(parts[:6] if live_paths[0].startswith(L) else parts[:3])
        live[family] += 1
        stems[family].add(stem)

    print(json.dumps({
        'receipt': receipt.get('utc'),
        'run_modules': collections.Counter(layer.values()),
        'records': {k: len(v) for k, v in sorted(records.items())},
        'records_citing_a_spine_proof': citing,
        'records_in_an_inherited_module': records['in an inherited module'],
        'records_outside_the_spine_run': records['outside the spine run'],
        'lean_outside_the_run': {'theorems_in_live_paths': sum(live.values()),
                                 'modules_in_live_paths': sum(len(s) for s in stems.values()),
                                 'theorems_only_in_copies': copies},
        'lean_families': [{'family': f, 'theorems': n, 'modules': len(stems[f])} for f, n in live.most_common()],
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
