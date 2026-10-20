"""Register U's join modules in the Becoming core (17 October 2026).

usage (from the repository root): python3 -B .../u-unification/integrate.py SCOPE.json TREE ...

Copies every module under each TREE (`Becoming/Foo.lean`) into the package, refusing to overwrite an existing
module; adds each to `CORE` in check_becoming.py before the root `Becoming`, imports it from `Becoming.lean` after
the last import, adds a bullet `* \`Becoming.Foo\` (L4): <sentence>` before the closing paragraph of the root's
layer list, and adds the scope sentence `Foo: <sentence> ` before the Selection sentence of `SCOPE`. SCOPE.json maps
each module name to its sentence (written by the integrator from the module's docstring). Changes no existing
statement.
"""
import json
import re
import shutil
import textwrap
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
scope = json.loads(Path(sys.argv[1]).read_text())
modules = []
for tree in map(Path, sys.argv[2:]):
    for p in sorted((tree / 'Becoming').glob('*.lean')):
        name = 'Becoming.' + p.stem
        target = PKG / 'Becoming' / p.name
        assert not target.exists(), ('module exists', name)
        assert name in scope, ('no scope sentence', name)
        modules.append((name, p, target))
for name, p, target in modules:
    shutil.copyfile(p, target)

checker = PKG / 'check_becoming.py'
text = checker.read_text()
old = '"Becoming.FormedLoops", "Becoming"]'
assert old in text
text = text.replace(old, '"Becoming.FormedLoops", ' + ''.join(f'"{n}", ' for n, _, _ in modules) + '"Becoming"]', 1)
anchor = '    "Selection: two histories are selected alike'
assert anchor in text
lines = ''.join(f'    {json.dumps(n.split(".", 1)[1] + ": " + scope[n] + " ", ensure_ascii=False)}\n' for n, _, _ in modules)
text = text.replace(anchor, lines + anchor, 1)
checker.write_text(text)

root = PKG / 'Becoming.lean'
text = root.read_text()
last = list(re.finditer(r'^import .+\n', text, re.M))[-1]
text = text[:last.end()] + ''.join(f'import {n}\n' for n, _, _ in modules) + text[last.end():]
closing = '\n\nThe core imports nothing else, every source declaration has an empty axiom report, and'
assert closing in text
bullets = ''.join(textwrap.fill(f'* `{n}` (L4): {scope[n]}', width=99, subsequent_indent='  ') + '\n'
                  for n, _, _ in modules)
text = text.replace(closing, '\n' + bullets + closing[1:], 1)
root.write_text(text)
print(len(modules), 'modules registered:', ', '.join(n for n, _, _ in modules))
