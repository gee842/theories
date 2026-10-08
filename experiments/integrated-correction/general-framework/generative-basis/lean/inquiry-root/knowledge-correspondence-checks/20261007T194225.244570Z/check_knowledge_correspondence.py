#!/usr/bin/env python3
"""Fresh Lean check of exact correspondence, not a certification of knowledge."""
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
SOURCE = HERE / 'KnowledgeCorrespondence.lean'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    source, checker, compiler = SOURCE.read_bytes(), Path(__file__).read_bytes(), LEAN.read_bytes()
    # This module contains no nested block comments or strings with comment syntax.
    code = re.sub(r'/\-.*?\-/', '', source.decode(), flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    assert re.findall(r'^import (.+)$', code, re.M) == ['Std']
    assert not re.search(r'\b(sorry|admit|axiom|opaque|unsafe|native_decide|implemented_by|skipKernelTC)\b', code)
    declarations = re.findall(r'^(?:noncomputable )?(def|theorem|structure) (\w+)', code, re.M)
    names = ['Generative.KnowledgeCorrespondence.' + name for _, name in declarations]
    assert names and len(names) == len(set(names))
    audit = 'import KnowledgeCorrespondence\n' + ''.join('#print axioms ' + n + '\n' for n in names)
    run = HERE / 'knowledge-correspondence-checks' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    run.mkdir(parents=True)
    (run / SOURCE.name).write_bytes(source)
    (run / Path(__file__).name).write_bytes(checker)
    (run / 'KnowledgeCorrespondenceAudit.lean').write_text(audit)
    (run / 'lean-toolchain').write_text('leanprover/lean4:v4.29.1\n')
    version = subprocess.check_output([str(LEAN), '--version'], text=True).strip()
    assert 'version 4.29.1,' in version
    commands, logs = [], {}
    with tempfile.TemporaryDirectory(prefix='knowledge-correspondence-') as temporary:
        stage = Path(temporary)
        (stage / SOURCE.name).write_bytes(source)
        (stage / 'KnowledgeCorrespondenceAudit.lean').write_text(audit)
        env = dict(os.environ, LEAN_PATH=str(stage))
        for args, label in [(['-o', 'KnowledgeCorrespondence.olean', SOURCE.name], 'compile.txt'),
                            (['KnowledgeCorrespondenceAudit.lean'], 'axioms.txt')]:
            command = [str(LEAN)] + args
            result = subprocess.run(command, cwd=stage, env=env, text=True,
                                    capture_output=True, timeout=60)
            output = result.stdout + result.stderr
            commands.append(command)
            logs[label] = output
            (run / label).write_text(output)
            assert result.returncode == 0 and 'warning:' not in output and 'error:' not in output, output
    audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", logs['axioms.txt'])
    assert [name for name, _ in audits] == names
    dependencies = {name: [a.strip() for a in deps.split(',') if a.strip()] for name, deps in audits}
    assert all(set(deps) <= {'propext', 'Quot.sound', 'Classical.choice'} for deps in dependencies.values())
    assert SOURCE.read_bytes() == source and Path(__file__).read_bytes() == checker and LEAN.read_bytes() == compiler
    record = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'lean_version': version, 'source': str(SOURCE.relative_to(ROOT)),
        'source_sha256': sha(source), 'checker_sha256': sha(checker), 'compiler_sha256': sha(compiler),
        'snapshot': str(run.relative_to(ROOT)), 'theorems': sum(k == 'theorem' for k, _ in declarations),
        'explicit_declaration_audits': len(audits), 'dependencies': dependencies,
        'commands': commands, 'log_sha256': {k: sha(v.encode()) for k, v in logs.items()},
        'scope': 'Exact answers relative to supplied domains, evidence and target meanings; '
                 'abstract decoder existence uses classical choice. No general definition of knowledge, '
                 'empirical calibration, cognitive uptake or G0 necessity is proved.'}
    output = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    (run / 'verification.json').write_text(output)
    (HERE / 'knowledge-correspondence-verification.json').write_text(output)
    print(json.dumps({key: record[key] for key in ['status', 'theorems', 'explicit_declaration_audits', 'snapshot']}))


if __name__ == '__main__':
    main()
