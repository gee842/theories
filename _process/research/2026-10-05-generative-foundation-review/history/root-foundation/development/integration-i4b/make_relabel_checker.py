#!/usr/bin/env python3
"""Integration I4b item 2: write the instance checker of selection by the record alone (run from the repository
root): python3 -B make_relabel_checker.py

It runs `../integration-i3e/make_checker.py relabel.json` and then makes the changes a module outside the Lean
root with unreceipted originals needs, each asserted to apply once:
* the Lean root is `generative-basis/lean`, four folders up from the remaining-dependency package and down into
  `lean`;
* the core's module index covers that root only, so `PluralRecords`, `TieBreaking` and the target are added from
  the package folder, and source paths are written relative to the Lean root with `os.path.relpath`;
* the originals have no machine receipt, only the build record `inquiry-warrant/BUILD.md`, so they are checked
  here: they need no passed receipt, their declarations are audited with the target's, and every report must be
  empty;
* the core's declaration scanner reads names of word characters, and the originals also name declarations with `?`
  and `'` (`find?_some_true`, `mem_finRange'`), so they are scanned with those characters admitted, by the core
  scanner's rules otherwise, and the audit lines are read anchored at their start, so a primed name is read whole;
* `TieBreaking` prints one warning, the unused hypothesis `noWithhold` of `full_tie_open_uniform`, kept as stated;
  its compile step allows exactly that warning and the receipt records it.
"""
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
OUT = Path('experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/'
           'feedback/remaining-dependency/formal/check_selection_relabel_correspondence.py')

subprocess.run([sys.executable, '-B', str(KIT.parent / 'integration-i3e' / 'make_checker.py'),
                str(KIT / 'relabel.json')], check=True)
s = OUT.read_text()


def change(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)


change('LEAN_ROOT = HERE.parents[4]\n', 'LEAN_ROOT = HERE.parents[4] / "lean"\n')
change('# Seconds allowed for each Lean run', '''# The originals instantiated here: they import only the prelude and have no machine receipt, so this checker
# compiles and audits them, and every report must be empty.
ORIGINALS = ("PluralRecords", "TieBreaking")
# The one warning the originals print, kept as stated.
ALLOWED_WARNINGS = {"TieBreaking": "TieBreaking.lean:63:46: warning: unused variable `noWithhold`"}
# Seconds allowed for each Lean run''')
change('''    index = core.module_index()
''', '''    index = core.module_index()
    # The core indexes its Lean root only; the originals and this module sit in the remaining-dependency package.
    for name in ORIGINALS + (TARGET,):
        assert name not in index, name
        index[name] = [HERE / (name + ".lean")]
''')
change('"source_paths": {name: str(paths[name].relative_to(LEAN_ROOT)) for name in order},',
       '"source_paths": {name: os.path.relpath(paths[name], LEAN_ROOT) for name in order},\n'
       '        "checked_here": list(ORIGINALS) + [TARGET], "allowed_warnings": ALLOWED_WARNINGS,')
change('''        for name in order[:-1]:
            found =''', '''        for name in order[:-1]:
            if name in ORIGINALS:
                continue
            found =''')
change('''AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \\[([^\\]]*)\\])")''',
       '''# Read anchored at the line's start, so a name ending in a prime is read whole.
AUDIT = re.compile(r"^'(.+?)' (?:does not depend on any axioms|depends on axioms: \\[([^\\]]*)\\])", re.M)''')
change('''def passed_receipts():''', '''def original_declarations(data):
    """The core scanner's rules, with `?`, `!` and `'` admitted in names, as the originals use them."""
    code = core.audit_support.code_only(data.decode())
    assert not re.search(r"\\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\\b|debug\\.skipKernelTC", code), \\
        "Proof escape in source"
    scopes, result = [], []
    for line in code.splitlines():
        scope = re.match(r"^(namespace|section)\\b\\s*(\\S*)", line)
        if scope:
            scopes.append((scope[1], scope[2]))
            continue
        if re.match(r"^end(?:\\s|$)", line):
            assert scopes, line
            scopes.pop()
            continue
        declaration = re.match(r"^(theorem|def|abbrev|structure|inductive|instance)\\s+([\\w.'?!]+)", line)
        if declaration:
            prefix = ".".join(n for kind, n in scopes if kind == "namespace")
            result.append({"kind": declaration[1],
                           "name": prefix + "." + declaration[2] if prefix else declaration[2]})
    assert not scopes and result
    assert len({item["name"] for item in result}) == len(result)
    return result


def passed_receipts():''')
change('''        registry = core.declarations(sources[TARGET])
''', '''        registry = core.declarations(sources[TARGET])
        originals = {name: original_declarations(sources[name]) for name in ORIGINALS}
        audited_registry = registry + [d for name in ORIGINALS for d in originals[name]]
        empty = EMPTY | {d["name"] for name in ORIGINALS for d in originals[name]}
''')
change('''            def run(args, log, key=None, outputs=(), driver=None):''',
       '''            def run(args, log, key=None, outputs=(), driver=None, allowed=""):''')
change('''                assert not re.search(r"\\b(?:error|warning):", p.stdout), p.stdout''',
       '''                assert not re.search(r"\\b(?:error|warning):", p.stdout.replace(allowed, "") if allowed else p.stdout), \\
                    p.stdout''')
change('''                run(["-o", olean, core.source_file(name)], name + ".log", key=keys[name], outputs=[olean])''',
       '''                run(["-o", olean, core.source_file(name)], name + ".log", key=keys[name], outputs=[olean],
                    allowed=ALLOWED_WARNINGS.get(name, ""))''')
change('''            audit = f"import {TARGET}\\n" + "".join(f"#print axioms {d['name']}\\n" for d in registry)''',
       '''            audit = f"import {TARGET}\\n" + "".join(f"#print axioms {d['name']}\\n" for d in audited_registry)''')
change('''        for item in registry:
            assert item["name"] in audited''', '''        for item in audited_registry:
            assert item["name"] in audited''')
change('''            assert not (item["name"] in EMPTY and found), ("must not depend on axioms", item["name"], found)''',
       '''            assert not (item["name"] in empty and found), ("must not depend on axioms", item["name"], found)''')
change('''        assert EMPTY <= set(dependencies), sorted(EMPTY - set(dependencies))''',
       '''        assert empty <= set(dependencies), sorted(empty - set(dependencies))''')
change('''            "declarations": registry, "axiom_dependencies": dependencies, "kernel_checked": True,
        }]''', '''            "declarations": registry,
            "axiom_dependencies": {d["name"]: dependencies[d["name"]] for d in registry}, "kernel_checked": True,
        }] + [{
            "module": name, "layer": "periphery original, checked here",
            "theorems": sum(d["kind"] == "theorem" for d in originals[name]),
            "declarations": originals[name],
            "axiom_dependencies": {d["name"]: dependencies[d["name"]] for d in originals[name]},
            "kernel_checked": True,
        } for name in ORIGINALS]''')
change('''                      "declaration_audits": len(registry),''', '''                      "declaration_audits": len(audited_registry),''')
OUT.write_text(s)
print(OUT)
