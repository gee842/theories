#!/usr/bin/env python3
"""Staged P83 landing driver. Runs no Lean checker and makes no commit.

prepare: copy/register Identification; docs: apply study/chapter/plan, README and reading entry;
records: bind the final bytes and re-point the existing records. Between prepare and docs, the
integrator runs the core/periphery checkers and inventory serially, reconciling classifications.
"""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
B = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('stage', choices=('prepare', 'docs', 'records'))
parser.add_argument('root', type=Path)
parser.add_argument('--section', type=int)
parser.add_argument('--base', default='HEAD')
parser.add_argument('--reviewed-at')
args = parser.parse_args()
root = args.root.resolve()


def run(script, *extra):
    subprocess.run([sys.executable, '-B', str(HERE / script), str(root), *map(str, extra)], check=True)


if args.stage == 'prepare':
    destination = root / B / 'Becoming/Identification.lean'
    assert not destination.exists(), 'Identification is already present'
    assert (root / B / 'Becoming/Description.lean').exists(), 'P70–P72 must land first'
    shutil.copyfile(HERE / 'lean/Becoming/Identification.lean', destination)
    run('root_edits.py', 'core')
elif args.stage == 'docs':
    assert args.section is not None, '--section is required'
    run('apply_docs.py', args.section, '| P72、P72q 语境中的识与量子实现', '- **P72 and P72q:**')
    run('root_edits.py', 'readmes')
    run('land_docs.py', args.base)
else:
    assert args.section is not None, '--section is required'
    reviewed = args.reviewed_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    run('make_records.py', reviewed, args.section)
    run('repoint.py', args.base)
