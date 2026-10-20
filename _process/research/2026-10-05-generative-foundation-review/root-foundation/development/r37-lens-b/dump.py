#!/usr/bin/env python3
"""R37: the run's constants as the connectivity dump reads them, for the removal tools of R32.

usage: python3 -B dump.py OUT.json      (writes {"c": constants, "reg": registry})
The compiled modules come from the checker's cache (run buildall.py first)."""
import importlib.util
import json
import os
import sys
from pathlib import Path

FOUNDATION = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('tc', FOUNDATION / 'THEOREM-CONNECTIVITY.py')
tc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tc)
out = Path(sys.argv[1]).resolve()
os.chdir(tc.ROOT)
constants, registry = tc.dump_constants()[:2]
json.dump({'c': constants, 'reg': registry}, open(out, 'w'))
print(len(constants), 'constants')
