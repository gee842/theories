#!/usr/bin/env python3
"""How much of the repository's Lean the Becoming spine run compiles: python3 -B SPINE-INTEGRATION.py [RECEIPT]

Reads the consolidated checker's receipt (by default `becoming-verification.json`, the latest passed run) and prints,
as JSON:

* records: each result record by where its Lean proof is checked. `spine` cites a module of the core, the foundation or
  the bridge (or any file under `Becoming/`); `inherited only` cites only periphery modules the spine run compiles
  because the bridge imports them; `outside the spine run` cites only Lean the run does not compile; `no Lean proof`
  cites none.
* lean: theorem declarations outside the run, counted once per (file stem, name). A stem the run compiles is an older
  version of a run module and is left out; a declaration found only under a copy or evidence path (run folders,
  verification history, sources, snapshots) is counted apart from those in live paths, which are grouped by family.

A measurement, not a check: it reads text with regular expressions and does not run Lean."""
import collections
import json
import os
import re
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

    records = collections.defaultdict(list)
    config = json.loads(Path('_process/research-config.json').read_text())
    for directory in config['record_directories']:
        for path in sorted(Path(directory).glob('*.json')):
            record = json.loads(path.read_text())
            lean = [os.path.normpath(r['path']) for r in record.get('references', [])
                    if r.get('role') == 'proof' and r['path'].endswith('.lean')]
            layers = {in_run.get(p) for p in lean}
            if not lean:
                kind = 'no Lean proof'
            elif layers & {'core', 'foundation', 'bridge'} or any('/becoming/Becoming/' in p for p in lean):
                kind = 'spine'
            elif 'inherited' in layers:
                kind = 'inherited only'
            else:
                kind = 'outside the spine run'
            records[kind].append(record['id'])

    names = collections.defaultdict(set)
    for path in sorted(Path('.').rglob('*.lean')):
        p = os.path.normpath(str(path))
        if '.lake' in p or '/.build/' in p or p in in_run or path.stem in run_stems:
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
        'records_inherited_only': records['inherited only'],
        'records_outside_the_spine_run': records['outside the spine run'],
        'lean_outside_the_run': {'theorems_in_live_paths': sum(live.values()),
                                 'modules_in_live_paths': sum(len(s) for s in stems.values()),
                                 'theorems_only_in_copies': copies},
        'lean_families': [{'family': f, 'theorems': n, 'modules': len(stems[f])} for f, n in live.most_common()],
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
