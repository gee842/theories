#!/usr/bin/env python3
"""Integration I4b items 3 and 4: write the instance checker of a completion-package module (run from the
repository root): python3 -B make_prefix_checker.py [SPEC MODULE]

With no arguments it writes the PrefixSafety checker from `prefix.json` (item 3); item 4 runs it with
`branching.json FiniteBranching`. It runs `../integration-i3e/make_checker.py SPEC` and then makes the three changes
a module outside the Lean root needs, each asserted to apply once:
* the Lean root is `generative-basis/lean`, two folders up from the completion package and down into `lean`;
* the core's module index covers that root only, so the package module and the target are added from the package
  folder, and source paths are written relative to the Lean root with `os.path.relpath`;
* the package module matches the package receipt `verification.json`. The package checker `check.py` writes no status
  field: it writes the receipt only after every module compiled fresh and every audit passed, so the receipt counts
  as passed when it says so (`fresh_build`, no custom axiom, no proof hole).
"""
import json
import os
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
SPEC, MODULE = (KIT / sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else (KIT / 'prefix.json', 'PrefixSafety')
spec = json.loads(SPEC.read_text())
OUT = Path(os.path.normpath(Path('experiments/integrated-correction/general-framework/generative-basis/lean')
                            / spec['dir'] / spec['checker']))

subprocess.run([sys.executable, '-B', str(KIT.parent / 'integration-i3e' / 'make_checker.py'), str(SPEC)], check=True)
s = OUT.read_text()


def change(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)


change('LEAN_ROOT = HERE.parents[2]\n', 'LEAN_ROOT = HERE.parents[2] / "lean"\n')
change('# Seconds allowed for each Lean run', '''# The completion package's receipt; see passed_receipts.
PACKAGE_RECEIPT = HERE / "verification.json"
# Seconds allowed for each Lean run''')
change('''            receipts.append((str(path.relative_to(LEAN_ROOT)), text))
    return receipts
''', '''            receipts.append((str(path.relative_to(LEAN_ROOT)), text))
    # check.py in this folder writes its receipt only after every module compiled fresh and every audit passed;
    # it has no status field, so the receipt counts as passed when it says so.
    text = PACKAGE_RECEIPT.read_text()
    package = json.loads(text)
    if package["fresh_build"] is True and package["custom_axioms"] == [] and package["proof_holes"] is False:
        receipts.append((os.path.relpath(PACKAGE_RECEIPT, LEAN_ROOT), text))
    return receipts
''')
change('''    index = core.module_index()
''', f'''    index = core.module_index()
    # The core indexes its Lean root only; {MODULE} and this module sit in the completion package.
    for name in ("{MODULE}", TARGET):
        assert name not in index, name
        index[name] = [HERE / (name + ".lean")]
''')
change('"source_paths": {name: str(paths[name].relative_to(LEAN_ROOT)) for name in order},',
       '"source_paths": {name: os.path.relpath(paths[name], LEAN_ROOT) for name in order},')
OUT.write_text(s)
print(OUT)
