#!/usr/bin/env python3
"""R33 (from R32): compile the whole run in scratch and keep going past failures, to see every error at once.

usage: python3 -B buildall.py BUILD_DIR [ROOT_MODULE]

Like scratch_build.py (same Lean, keys and shared cache; passed steps reused, passing steps stored), but
every module whose imports compiled is compiled even where another failed, and the errors of every
failed module are printed. A working build, not a receipt; no audit is run."""
import concurrent.futures
import os
import re
import subprocess
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path

PKG = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
sys.path.insert(0, str(PKG))
import check_becoming as cb  # noqa: E402

build = Path(sys.argv[1]).resolve()
root = sys.argv[2] if len(sys.argv) > 2 else 'Becoming'
index = cb.module_index()
order = cb.closure(index, [root])
sources = {name: index[name][0].read_bytes() for name in order}
command, binary, _ = cb.resolve_lean()
context = [cb.audit_support.TOOLCHAIN, cb.audit_support.digest(binary.read_bytes())]
keys = cb.module_keys(context, sources, order)
origin = {'utc': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ'), 'retained': 'R33 buildall, not retained'}
for name, data in sources.items():
    target = build / cb.source_file(name)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.is_file() or target.read_bytes() != data:
        target.write_bytes(data)
state, lock, ran = {}, threading.Lock(), []


def compile_one(name):
    olean = cb.source_file(name)[:-5] + '.olean'
    if cb.reuse(keys[name], [build / olean]):
        return True, ''
    p = subprocess.run(command + ['-o', olean, cb.source_file(name)], cwd=build, env={**os.environ, 'LEAN_PATH': str(build)},
                       text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
    with lock:
        ran.append(name)
    if p.returncode != 0:
        return False, p.stdout
    if re.search(r'\b(?:error|warning):', p.stdout):
        return False, p.stdout
    cb.store(keys[name], [build / olean], p.stdout, origin)
    return True, ''


imports = {n: [m for m in cb.imports_of(sources[n]) if m in keys] for n in order}
pending = set(order)
futures = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=cb.JOBS) as pool:
    while pending or futures:
        for n in sorted(pending):
            if all(state.get(m) is True for m in imports[n]):
                futures[pool.submit(compile_one, n)] = n
                pending.discard(n)
            elif any(state.get(m) in (False, 'skipped') for m in imports[n]):
                state[n] = 'skipped'
                pending.discard(n)
        if not futures:
            break
        done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
        for f in done:
            n = futures.pop(f)
            ok, out = f.result()
            state[n] = ok
            if not ok:
                print(f'== FAILED {n}')
                print(out[:12000])
failed = [n for n, s in state.items() if s is False]
skipped = [n for n, s in state.items() if s == 'skipped']
print(f'modules {len(order)}, ran {len(ran)}, failed {len(failed)}, skipped {len(skipped)}')
print('failed:', ' '.join(failed))
