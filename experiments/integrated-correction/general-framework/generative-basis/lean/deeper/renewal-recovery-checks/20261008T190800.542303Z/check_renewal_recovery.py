#!/usr/bin/env python3
"""Compile a fresh two-module closure and retain source-bound audit evidence."""
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
    (HERE / 'RelationalRenewal.lean', 'RelationalRenewal', []),
    (HERE / 'RenewalRecovery.lean', 'RenewalRecovery', ['Std', 'RelationalRenewal']),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    run = HERE / 'renewal-recovery-checks' / stamp
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
        assert re.findall(r'^namespace (.+)$', code, re.M)[0] == namespace
        assert not re.search(r'\b(sorry|admit|axiom|opaque|unsafe|native_decide|implemented_by|skipKernelTC)\b', code)
        scopes, found = [], []
        for line in code.splitlines():
            scope = re.match(r'^(namespace|section)\b\s*(\S*)', line)
            if scope:
                scopes.append((scope[1], scope[2]))
                continue
            if re.match(r'^end(?:\s|$)', line):
                assert scopes
                scopes.pop()
                continue
            declaration = re.match(r'^(def|theorem|structure|inductive|abbrev) (\w+)', line)
            if declaration:
                prefix = '.'.join(n for kind, n in scopes if kind == 'namespace')
                found.append((declaration[1], prefix + '.' + declaration[2]))
        assert not scopes and found
        declarations[p] = found
    (run / Path(__file__).name).write_bytes(checker)
    names = [name for ds in declarations.values() for _, name in ds]
    assert len(names) == len(set(names))
    audits = 'import RenewalRecovery\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    signatures = 'import RenewalRecovery\n' + ''.join('#check ' + n + '\n' for n in names)
    (run / 'Audit.lean').write_text(audits)
    (run / 'Signatures.lean').write_text(signatures)
    (run / 'lean-toolchain').write_text('leanprover/lean4:v4.29.1\n')
    logs, jobs_run, dependencies = {}, [], {}
    failure = None
    try:
        with tempfile.TemporaryDirectory(prefix='renewal-recovery-') as tmp:
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
        'scope': 'Recovery inside the inherited support-gated renewal law. An active route with '
                 'positive net contribution throughout a finite window restores sustaining support '
                 'by the deficit bound. If both activities are unsupported, the level is invariant '
                 'despite later nominal contribution inputs. Two actual input histories have the '
                 'same initial condition and future inputs but differ in recovery; a recovered '
                 'history is neither all-time renewing nor permanently consuming. The law, '
                 'thresholds, contribution schedule and physical correspondence remain supplied. '
                 'No general irreversibility, unique ontology, ethical or axiom-free foundation claim.'

    }
    encoded = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    (run / 'verification.json').write_text(encoded)
    if failure is None:
        (HERE / 'renewal-recovery-verification.json').write_text(encoded)
    print(json.dumps({k: record[k] for k in ['status', 'new_theorems', 'new_declaration_audits',
                                          'total_declaration_audits', 'snapshot', 'failure']}))
    if failure is not None:
        raise SystemExit(1)
    print(json.dumps({'new_empty_dependencies': sum(not dependencies[n] for _, n in new),
                      'all_empty_dependencies': sum(not ds for ds in dependencies.values())}))


if __name__ == '__main__':
    main()
