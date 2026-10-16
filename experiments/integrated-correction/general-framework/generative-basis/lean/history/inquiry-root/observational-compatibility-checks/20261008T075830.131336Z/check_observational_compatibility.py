#!/usr/bin/env python3
"""Actually compile and audit compatibility at a specified inquiry profile."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
HELPER = HERE.parent / 'universal-ethics/generative-capacity/check.py'
spec = importlib.util.spec_from_file_location('audit_support', HELPER)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
sha = lambda data: hashlib.sha256(data).hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    retained = HERE / 'observational-compatibility-checks' / stamp
    retained.mkdir(parents=True, exist_ok=False)
    source = HERE / 'ObservationalCompatibility.lean'
    files = {p.name: p.read_bytes() for p in [source, Path(__file__), HELPER]}
    for name, data in files.items():
        (retained / name).write_bytes(data)
    receipt = {'status': 'checking', 'utc': stamp, 'toolchain': audit.TOOLCHAIN,
               'retained_run': str(retained.relative_to(HERE)),
               'source_sha256': {'ObservationalCompatibility': sha(files[source.name])},
               'checker_sha256': {n: sha(b) for n, b in files.items() if n != source.name},
               'scope': 'Compatibility with all profile-expressible rivals is equivalent to coverage of every admissible profile. Invariance is an explicit additional premise for universal truth; finer profiles and one joint realization are distinguished. No definition of science, ethical countermodel, empirical experiment or proof of G0.'}
    try:
        declarations = audit.declarations(files[source.name].decode())
        lean = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
        receipt['lean_binary_sha256'] = sha(lean.read_bytes())
        with tempfile.TemporaryDirectory(prefix='observational-compatibility-lean-') as directory:
            work = Path(directory)
            (work / source.name).write_bytes(files[source.name])

            def run(args, filename):
                result = subprocess.run([str(lean)] + args, cwd=work, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (retained / filename).write_text(result.stdout)
                assert result.returncode == 0, result.stdout
                assert not re.search(r'\b(?:warning|error):', result.stdout), result.stdout
                return result.stdout

            receipt['lean_version'] = run(['--version'], 'version.log').strip()
            assert 'version 4.29.1' in receipt['lean_version']
            run(['-o', 'ObservationalCompatibility.olean', source.name], 'compile.log')
            # Explicit local search path for the just-compiled, byte-exact module.
            import os
            old_path = os.environ.get('LEAN_PATH')
            os.environ['LEAN_PATH'] = str(work)
            try:
                for suffix, command, items in [
                    ('AxiomAudit', '#print axioms ', declarations),
                    ('Signatures', '#check ', [d for d in declarations if d['kind'] == 'theorem'])]:
                    name = 'ObservationalCompatibility' + suffix + '.lean'
                    text = 'import ObservationalCompatibility\n' + '\n'.join(command + d['name'] for d in items) + '\n'
                    (work / name).write_text(text)
                    (retained / name).write_text(text)
                    run([name], suffix + '.log')
            finally:
                if old_path is None:
                    os.environ.pop('LEAN_PATH', None)
                else:
                    os.environ['LEAN_PATH'] = old_path
        output = (retained / 'AxiomAudit.log').read_text()
        dependencies = {}
        for d in declarations:
            name = d['name']
            if "'" + name + "' does not depend on any axioms" in output:
                dependencies[name] = []
            else:
                match = re.search(r"'" + re.escape(name) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                assert match, name
                dependencies[name] = [a.strip() for a in match[1].split(',') if a.strip()]
            assert set(dependencies[name]) <= {'propext', 'Quot.sound', 'Classical.choice'}, name
        assert source.read_bytes() == files[source.name], 'Source changed during check'
        assert Path(__file__).read_bytes() == files[Path(__file__).name], 'Checker changed during check'
        assert HELPER.read_bytes() == files[HELPER.name], 'Helper changed during check'
        receipt.update(status='passed', source_unchanged_during_check=True, kernel_checked=True,
                       theorems=sum(d['kind'] == 'theorem' for d in declarations),
                       declarations=declarations, axiom_dependencies=dependencies,
                       artifact_sha256={p.name: sha(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()})
    except Exception as error:
        receipt.update(status='failed', error=str(error))
        raise
    finally:
        serialized = json.dumps(receipt, indent=2) + '\n'
        (retained / 'verification.json').write_text(serialized)
        (HERE / 'observational-compatibility-verification.json').write_text(serialized)
    print(json.dumps({'status': receipt['status'], 'theorems': receipt['theorems'],
                      'declaration_audits': len(declarations),
                      'empty_dependency_audits': sum(not x for x in dependencies.values()),
                      'retained_run': receipt['retained_run']}))


if __name__ == '__main__':
    main()
