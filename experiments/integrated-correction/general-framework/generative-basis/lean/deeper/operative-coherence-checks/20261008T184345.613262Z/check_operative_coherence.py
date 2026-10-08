#!/usr/bin/env python3
"""Fresh Lean build and source-bound audits for the controlled-coherence calculation."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEAN = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
SOURCES = [HERE / 'OperativeCoherence.lean']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    sources = {p: p.read_bytes() for p in SOURCES}
    checker = Path(__file__).read_bytes()
    compiler = LEAN.read_bytes()
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    declarations = {}
    for p, data in sources.items():
        code = re.sub(r'/\-.*?\-/', '', data.decode(), flags=re.S)
        code = re.sub(r'--[^\n]*', '', code)
        assert not re.search(r'\b(sorry|admit|axiom|opaque|unsafe|native_decide|implemented_by|skipKernelTC)\b', code)
        expected = ['Std']
        assert re.findall(r'^import (.+)$', code, re.M) == expected
        namespace = 'Generative.OperativeCoherence.'
        declarations[p] = [(kind, namespace + name) for kind, name in
                           re.findall(r'^(def|theorem|structure|inductive) (\w+)', code, re.M)]
    names = [name for ds in declarations.values() for _, name in ds]
    assert len(names) == len(set(names))
    audit = 'import OperativeCoherence\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    logs = {}
    with tempfile.TemporaryDirectory(prefix='operative-coherence-') as tmp:
        stage = Path(tmp)
        for p, data in sources.items():
            (stage / p.name).write_bytes(data)
        (stage / 'Audit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=str(stage))
        jobs = [(p.stem + '-compile.txt', ['-o', p.stem + '.olean', p.name]) for p in SOURCES]
        jobs.append(('axioms.txt', ['Audit.lean']))
        for label, args in jobs:
            r = subprocess.run([str(LEAN)] + args, cwd=stage, env=env,
                               capture_output=True, text=True, timeout=60)
            logs[label] = r.stdout + r.stderr
            assert r.returncode == 0 and 'warning:' not in logs[label] and 'error:' not in logs[label], logs[label]
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", logs['axioms.txt'])
    assert [n for n, _ in audits] == names
    dependencies = {n: [x.strip() for x in dep.split(',') if x.strip()] for n, dep in audits}
    assert all(set(ds) <= {'propext', 'Quot.sound', 'Classical.choice'} for ds in dependencies.values())
    for p, data in sources.items():
        assert p.read_bytes() == data, 'concurrent source change: ' + str(p)
    assert Path(__file__).read_bytes() == checker and LEAN.read_bytes() == compiler
    run = HERE / 'operative-coherence-checks' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    run.mkdir(parents=True)
    for p, data in sources.items():
        (run / p.name).write_bytes(data)
    (run / Path(__file__).name).write_bytes(checker)
    (run / 'Audit.lean').write_text(audit)
    (run / 'lean-toolchain').write_text('leanprover/lean4:v4.29.1\n')
    for label, output in logs.items():
        (run / label).write_text(output)
    new = declarations[SOURCES[-1]]
    record = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'lean_version': version, 'compiler_sha256': sha(compiler), 'checker_sha256': sha(checker),
        'modules': [{'path': str(p.relative_to(ROOT)), 'source_sha256': sha(data),
                     'theorems': sum(k == 'theorem' for k, _ in declarations[p]),
                     'declarations': [n for _, n in declarations[p]]} for p, data in sources.items()],
        'new_theorems': sum(k == 'theorem' for k, _ in new),
        'new_declaration_audits': len(new), 'total_declaration_audits': len(names),
        'dependencies': dependencies, 'snapshot': str(run.relative_to(ROOT)),
        'log_sha256': {label: sha(output.encode()) for label, output in logs.items()},
        'scope': 'Integer amplitude and density-numerator algebra for specified X/Z controlled '
                 'orders, dephasing, a fixed control measurement, failure of uniform recovery '
                 'from the reduced matrix alone, and exact dephasing from a reversible joint '
                 'interaction with an initially blank register. Physical interpretation is supplied. No proof of '
                 'causal nonseparability, general quantum theory, a laboratory implementation, '
                 'universal irreversibility, axiom-free ontology or ethical warrant.'}
    encoded = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    (run / 'verification.json').write_text(encoded)
    (HERE / 'operative-coherence-verification.json').write_text(encoded)
    print(json.dumps({k: record[k] for k in ['status', 'new_theorems', 'new_declaration_audits',
                                          'total_declaration_audits', 'snapshot']}))
    print(json.dumps({'new_empty_dependencies': sum(not dependencies[n] for _, n in new),
                      'all_empty_dependencies': sum(not ds for ds in dependencies.values())}))


if __name__ == '__main__':
    main()
