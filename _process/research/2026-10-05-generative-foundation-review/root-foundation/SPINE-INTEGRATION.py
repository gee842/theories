#!/usr/bin/env python3
"""How much of the repository's Lean the Becoming spine run compiles: python3 -B SPINE-INTEGRATION.py [RECEIPT]

Reads the consolidated checker's receipt (by default `becoming-verification.json`, the latest passed run) and prints,
as JSON:

* records: each result record by where its claim is proved. `stated on the spine` has its canonical source in the core,
  the foundation or the bridge, or an alias naming a declaration of the `Becoming` package; otherwise the main proof
  (the canonical source where it is Lean, else the first Lean proof cited) is `in an inherited module` the spine run
  compiles because the bridge imports it, or `outside the spine run`; `no Lean proof` cites none. Counted apart, more
  widely: the records citing some proof in the core, the foundation or the bridge.
* lean: theorem declarations in tracked Lean files outside the run, by the rules of the I4 classification table
  (study §139; Ren's decision (c), 16 October 2026, sources/15-codex-theory-conversations/2026-10-16-measure-fix-decision.md):
  - a file is left out as an older version of a run module only where its full module name is that run module's
    (`Becoming/Admission.lean` is `Becoming.Admission`; a local `Admission.lean` elsewhere is another module and counts);
  - a path is a copy under a copy or evidence path (the measure's earlier rule) or under a run, check, source-copy,
    verification or history folder, or a folder named by a timestamp or a numeric run id (the table's snapshot rule);
  - each module (file stem) with a live path is counted from its canonical file, its own folder before a review,
    landing or development copy: every theorem declaration in it, grouped by family; a theorem name found only under
    copy paths is counted apart, once per (stem, name).
  Until 16 October 2026 the measure left out every file sharing a run module's stem and pooled theorem names over all
  live files of a stem, once per name; it also counted as copies the checker's saved sources of run modules, which are
  named by full module name (`Becoming.Imbalance.lean`). Numbers in earlier study sections were taken that way at
  their own receipts.

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
# The classification table's snapshot rule (development/integration-i4a/connect.py), applied to each folder of a path.
SNAP = re.compile(r'^(\d{9,}|\d{8}T\d{6}.*|.*-runs?|runs?|.*-checks|checks|sources|.*-verification|verification|.*-history|history)$')
DECL = re.compile(r'^\s*(?:private\s+|protected\s+)*(?:theorem|lemma)\s+(\S+)', re.M)


def is_copy(p):
    return bool(COPY.search(p)) or any(SNAP.match(segment) for segment in p.split('/')[:-1])


def module_name(path):
    # As the table's inventory (development/integration-i4a/inventory.py): a file in a `Becoming` folder is
    # `Becoming.<stem>`; elsewhere the run's inherited modules are named by their stem.
    return ('Becoming.' + path.stem) if path.parent.name == 'Becoming' else path.stem


def canonical(paths):
    # The table's canonical path: a module's own folder before a review, landing or development copy of it.
    return sorted(paths, key=lambda p: (p.startswith(('_process/', 'drafts/')) or '/development/' in p, p))[0]


def main():
    os.chdir(ROOT)
    receipt_path = sys.argv[1] if len(sys.argv) > 1 else L + 'becoming/becoming-verification.json'
    receipt = json.loads(Path(receipt_path).read_text())
    layer = {m['module']: m.get('layer') for m in receipt['modules']}
    in_run = {os.path.normpath(L + p): layer.get(mod) for mod, p in receipt['source_paths'].items()}
    run_names = set(receipt['source_paths'])

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

    files, names = collections.defaultdict(list), collections.defaultdict(set)
    tracked = subprocess.run(['git', 'ls-files', '-z', '--', '*.lean'], capture_output=True, check=True).stdout
    for p in sorted(os.path.normpath(t) for t in tracked.decode().split('\0') if t):
        path = Path(p)
        if p in in_run or module_name(path) in run_names:
            continue
        declared = DECL.findall(path.read_text(encoding='utf-8', errors='replace'))
        files[path.stem].append((p, declared))
        for name in set(declared):
            names[(path.stem, name)].add(p)
    live, stems = collections.Counter(), collections.defaultdict(set)
    for stem, entries in files.items():
        live_paths = [p for p, _ in entries if not is_copy(p)]
        if not live_paths:
            continue
        main_path = canonical(live_paths)
        declared = dict(entries)[main_path]
        if not declared:
            continue
        parts = main_path.split('/')
        family = '/'.join(parts[:6] if main_path.startswith(L) else parts[:3])
        live[family] += len(declared)
        stems[family].add(stem)
    copies = sum(1 for paths in names.values() if all(is_copy(p) for p in paths))

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
