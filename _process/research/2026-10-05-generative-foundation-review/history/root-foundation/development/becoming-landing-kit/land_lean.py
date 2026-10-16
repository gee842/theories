#!/usr/bin/env python3
"""Step 1 of a landing: copy each package's module into a checkout W and register it in the root module
(import and docstring bullet), the checker's CORE and scope, and the Lean README (row and import sentences).
Usage: python3 -B land_lean.py RUN_DIR W

Each entry of the config's PACKAGES gives: module, package, after (the registered module it follows in the
root's imports, its bullets, CORE and the README rows), scope_before (the start of the scope paragraph it
goes before), bullet, scope, readme_zh, readme_en, imports_zh, imports_en (pairs: an existing phrase of
the import sentences and the phrase that replaces it)."""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit  # noqa: E402

RUN = Path(sys.argv[1]).resolve()
W = Path(sys.argv[2]).resolve()
config = kit.load_config(RUN)
B = W / kit.D

for p in config.PACKAGES:
    module, after = p['module'], p['after']
    src = W / kit.DEV / p['package'] / 'lean/Becoming' / f'{module}.lean'
    dst = B / 'Becoming' / f'{module}.lean'
    assert not dst.exists(), dst
    shutil.copyfile(src, dst)
    print('copied', module)

    root = B / 'Becoming.lean'
    s = root.read_text()
    a = f'import Becoming.{after}\n'
    assert s.count(a) == 1 and f'import Becoming.{module}\n' not in s
    s = s.replace(a, a + f'import Becoming.{module}\n')
    start = kit.line_start(s, f'* `Becoming.{after}` (')
    nxt = s.index('\n* `', start) + 1
    bullet = p['bullet'].rstrip('\n') + '\n'
    assert bullet.startswith(f'* `Becoming.{module}` (')
    s = s[:nxt] + bullet + s[nxt:]
    root.write_text(s)
    print('edited Becoming.lean')

    kit.edit(W, f'{kit.D}/check_becoming.py', [
        (f'"Becoming.{after}",', f'"Becoming.{after}", "Becoming.{module}",'),
        (f'    "{p["scope_before"]}', kit.scope_lines(p['scope']) + f'    "{p["scope_before"]}'),
    ])

    readme = B / 'README.md'
    s = readme.read_text()
    i = s.index(f'| [`Becoming.{after}`](Becoming/{after}.lean) |')
    i = s.rindex('\n', 0, i) + 1
    j = s.index('\n', i) + 1
    layer = p.get('layer', 'L3')
    assert bullet.startswith(f'* `Becoming.{module}` ({layer})'), (module, layer)
    row = f'| {layer} | [`Becoming.{module}`](Becoming/{module}.lean) | {p["readme_zh"]} / {p["readme_en"]} |\n'
    s = s[:j] + row + s[j:]
    readme.write_text(s)
    kit.edit(W, f'{kit.D}/README.md', [p['imports_zh'], p['imports_en']])
