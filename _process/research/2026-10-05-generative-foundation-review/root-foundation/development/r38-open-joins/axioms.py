#!/usr/bin/env python3
"""R38: print the axiom report of every declaration a module states, in a scratch build.

usage: python3 -B axioms.py BUILD_DIR MODULE [PREFIX ...]

Reads the module's source for its `theorem`/`def`/`abbrev` names (in their namespaces), writes a driver
importing the module with `#print axioms` for each (only names starting with a PREFIX, where given), and
runs the checker's Lean on it with the scratch build on LEAN_PATH. A working check, not the receipt: the
checker's own audit is the evidence."""
import os
import re
import subprocess
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
sys.path.insert(0, str(PKG))
import check_becoming as cb  # noqa: E402

build, module = Path(sys.argv[1]).resolve(), sys.argv[2]
prefixes = sys.argv[3:]
src = (PKG / (module.replace('.', '/') + '.lean')).read_text()
names, stack = [], []
for line in src.splitlines():
    m = re.match(r'^namespace (\S+)', line)
    if m:
        stack.append(m.group(1))
        continue
    m = re.match(r'^end (\S+)', line)
    if m and stack and stack[-1] == m.group(1):
        stack.pop()
        continue
    m = re.match(r'^(?:private )?(?:theorem|def|abbrev) (\S+)', line)
    if m:
        name = '.'.join(stack + [m.group(1)])
        if not prefixes or any(name.startswith(p) for p in prefixes):
            names.append(name)
driver = build / 'R38Axioms.lean'
driver.write_text(f'import {module}\n' + ''.join(f'#print axioms {n}\n' for n in names))
command, _, _ = cb.resolve_lean()
p = subprocess.run(command + [str(driver)], cwd=build, env={**os.environ, 'LEAN_PATH': str(build)},
                   text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out = p.stdout
bad = [l for l in out.splitlines() if 'depends on axioms' in l or 'error' in l]
print(f'{len(names)} declarations, {len(bad)} with axioms or errors')
for line in bad:
    print(line)
