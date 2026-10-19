#!/usr/bin/env python3
"""R30 working build: compile every module the checker checks, in dependency order, continuing past a failure
(a module importing a failed one is skipped), so that one run lists every module's errors. Passed compiles are
stored in the checker's cache, so the landing run reuses them. Not a receipt.

usage: python3 -B wave.py BUILD_DIR [ERRORS_FILE]"""
import json
import os
import re
import subprocess
import sys
import threading
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKGDIR = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
sys.path.insert(0, str(PKGDIR))
sys.dont_write_bytecode = True
import check_becoming as cb  # noqa: E402

build = Path(sys.argv[1]).resolve()
errfile = Path(sys.argv[2]) if len(sys.argv) > 2 else build / 'errors.txt'
index = cb.module_index()
order = cb.closure(index)
sources = {n: index[n][0].read_bytes() for n in order}
command, binary, _ = cb.resolve_lean()
context = [cb.audit_support.TOOLCHAIN, cb.audit_support.digest(binary.read_bytes())]
keys = cb.module_keys(context, sources, order)
origin = {'utc': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ'), 'retained': 'R30 working build, not retained'}
for name, data in sources.items():
    t = build / cb.source_file(name)
    t.parent.mkdir(parents=True, exist_ok=True)
    if not t.is_file() or t.read_bytes() != data:
        t.write_bytes(data)
deps = {n: [m for m in cb.imports_of(sources[n]) if m in keys] for n in order}
status, errors, lock = {}, {}, threading.Lock()
stats = {'ran': 0, 'reused': 0}


def compile_one(name):
    olean = build / (cb.source_file(name)[:-5] + '.olean')
    found = cb.reuse(keys[name], [olean])
    if found:
        stats['reused'] += 1
        return True, ''
    p = subprocess.run(command + ['-o', str(olean.relative_to(build)), cb.source_file(name)], cwd=build,
                       env={**os.environ, 'LEAN_PATH': str(build)}, text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, timeout=int(os.environ.get('LEAN_TIMEOUT', '1800')))
    stats['ran'] += 1
    ok = p.returncode == 0 and not re.search(r'\b(?:error|warning):', p.stdout)
    if ok:
        cb.store(keys[name], [olean], p.stdout, origin)
    return ok, p.stdout


pending = set(order)
with ThreadPoolExecutor(max_workers=cb.JOBS) as pool:
    running = {}
    while pending or running:
        for n in sorted(pending, key=order.index):
            if len(running) >= cb.JOBS:
                break
            if any(status.get(d) in ('failed', 'skipped') for d in deps[n]):
                status[n] = 'skipped'; pending.discard(n); continue
            if all(status.get(d) == 'passed' for d in deps[n]):
                running[pool.submit(compile_one, n)] = n; pending.discard(n)
        if not running:
            continue
        done, _ = wait(running, return_when=FIRST_COMPLETED)
        for f in done:
            n = running.pop(f)
            try:
                ok, out = f.result()
            except Exception as e:  # timeout
                ok, out = False, repr(e)
            status[n] = 'passed' if ok else 'failed'
            if not ok:
                errors[n] = out
                print('FAILED', n, flush=True)
with open(errfile, 'w') as fh:
    for n, out in errors.items():
        fh.write(f'===== {n}\n{out}\n')
c = {}
for v in status.values():
    c[v] = c.get(v, 0) + 1
print(json.dumps({'status': c, **stats, 'failed': sorted(errors)}, indent=1))
