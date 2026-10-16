#!/usr/bin/env python3
"""Compile a fresh four-module closure and retain source-bound audit evidence."""
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
MODULES = [
    (HERE.parent / 'GenerativeCore.lean', 'Generative', ['Std']),
    (HERE.parent / 'systems-complexity/SystemsOrganization.lean', 'SystemsOrganization', ['GenerativeCore']),
    (HERE / 'OperativeCoherence.lean', 'Generative.OperativeCoherence', ['Std']),
    (HERE / 'RelationalReduction.lean', 'Generative.RelationalReduction',
     ['OperativeCoherence', 'SystemsOrganization']),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    run = HERE / 'relational-reduction-checks' / stamp
    run.mkdir(parents=True)
    sources = {p: p.read_bytes() for p, _, _ in MODULES}
    checker = Path(__file__).read_bytes()
    compiler = LEAN.read_bytes()
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    declarations = {}
    for p, namespace, imports in MODULES:
        data = sources[p]
        (run / p.name).write_bytes(data)
        code = re.sub(r'/\-.*?\-/', '', data.decode(), flags=re.S)
        code = re.sub(r'--[^\n]*', '', code)
        assert re.findall(r'^import (.+)$', code, re.M) == imports
        assert re.findall(r'^namespace (.+)$', code, re.M) == [namespace]
        assert not re.search(r'\b(sorry|admit|axiom|opaque|unsafe|native_decide|implemented_by|skipKernelTC)\b', code)
        declarations[p] = [(kind, namespace + '.' + name) for kind, name in
                           re.findall(r'^(def|theorem|structure|inductive) (\w+)', code, re.M)]
    (run / Path(__file__).name).write_bytes(checker)
    names = [name for ds in declarations.values() for _, name in ds]
    assert len(names) == len(set(names))
    audits = 'import RelationalReduction\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    signatures = 'import RelationalReduction\n' + ''.join('#check ' + n + '\n' for n in names)
    (run / 'Audit.lean').write_text(audits)
    (run / 'Signatures.lean').write_text(signatures)
    (run / 'lean-toolchain').write_text('leanprover/lean4:v4.29.1\n')
    logs, jobs_run, dependencies = {}, [], {}
    failure = None
    try:
        with tempfile.TemporaryDirectory(prefix='relational-reduction-') as tmp:
            stage = Path(tmp)
            for p, data in sources.items():
                (stage / p.name).write_bytes(data)
            (stage / 'Audit.lean').write_text(audits)
            (stage / 'Signatures.lean').write_text(signatures)
            env = dict(os.environ, LEAN_PATH=str(stage))
            jobs = [(p.stem + '-compile.txt', ['-o', p.stem + '.olean', p.name]) for p in sources]
            jobs += [('axioms.txt', ['Audit.lean']), ('signatures.txt', ['Signatures.lean'])]
            for label, args in jobs:
                result = subprocess.run([str(LEAN)] + args, cwd=stage, env=env,
                                        capture_output=True, text=True, timeout=60)
                logs[label] = result.stdout + result.stderr
                jobs_run.append({'log': label, 'exit_code': result.returncode, 'arguments': args})
                assert result.returncode == 0 and 'warning:' not in logs[label] and 'error:' not in logs[label], logs[label]
        reports = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", logs['axioms.txt'])
        assert [n for n, _ in reports] == names
        dependencies = {n: [x.strip() for x in dep.split(',') if x.strip()] for n, dep in reports}
        assert all(set(ds) <= {'propext', 'Quot.sound'} for ds in dependencies.values())
        for p, data in sources.items():
            assert p.read_bytes() == data, 'source changed during compilation: ' + str(p)
        assert Path(__file__).read_bytes() == checker and LEAN.read_bytes() == compiler
    except Exception as exc:
        failure = str(exc)
    for label, output in logs.items():
        (run / label).write_text(output)
    new = declarations[MODULES[-1][0]]
    record = {
        'status': 'passed' if failure is None else 'failed',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'lean_version': version, 'compiler_sha256': sha(compiler), 'checker_sha256': sha(checker),
        'modules': [{'path': str(p.relative_to(ROOT)), 'source_sha256': sha(data),
                     'theorems': sum(k == 'theorem' for k, _ in declarations[p]),
                     'declarations': [n for _, n in declarations[p]]} for p, data in sources.items()],
        'new_theorems': sum(k == 'theorem' for k, _ in new),
        'new_declaration_audits': len(new), 'total_declaration_audits': len(names),
        'dependencies': dependencies, 'jobs': jobs_run, 'failure': failure,
        'snapshot': str(run.relative_to(ROOT)),
        'artifact_sha256': {p.name: sha(p.read_bytes()) for p in sorted(run.iterdir())},
        'scope': 'Integer real-amplitude algebra with specified controlled-X and local Z. '
                 'Equal pairs of reduced states and computational-basis masses do not determine '
                 'the next control density. A four-integer summary retaining the relevant joint '
                 'cross contribution gives exact control responses for all finite words of the '
                 'two supplied operations, using SystemsOrganization.evolve_semiconjugacy. '
                 'Normalized physical interpretation is supplied. No quantum-foundation, '
                 'causal-nonseparability, universal nonlocality, empirical, ethical or zero-axiom claim.'
    }
    encoded = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    (run / 'verification.json').write_text(encoded)
    if failure is None:
        (HERE / 'relational-reduction-verification.json').write_text(encoded)
    print(json.dumps({k: record[k] for k in ['status', 'new_theorems', 'new_declaration_audits',
                                          'total_declaration_audits', 'snapshot', 'failure']}))
    if failure is not None:
        raise SystemExit(1)
    print(json.dumps({'new_empty_dependencies': sum(not dependencies[n] for _, n in new),
                      'all_empty_dependencies': sum(not ds for ds in dependencies.values())}))


if __name__ == '__main__':
    main()
