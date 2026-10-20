#!/usr/bin/env python3
"""R33: list the pure forwarders the connectivity dump finds in the modules R33 changed (inspection;
restores the compiled run from the checker's cache as THEOREM-CONNECTIVITY.py does, writes nothing)."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('tc', HERE.parents[1] / 'THEOREM-CONNECTIVITY.py')
tc = importlib.util.module_from_spec(spec)
sys.argv = ['THEOREM-CONNECTIVITY.py']
spec.loader.exec_module(tc)
constants = tc.dump_constants()
if isinstance(constants, tuple):
    constants = constants[0]
MODS = ('LawAlongRun', 'LearnableRuns', 'Limit.', 'LoopReturn', 'Tolerance', 'Interleavings', 'Run.', 'Conditions.',
        'Dependence.', 'Web.')
for n, x in sorted(constants.items()):
    if 'f' in x and x['f'] in constants and any(m in n for m in MODS):
        print(n, '->', x['f'])
