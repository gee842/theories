#!/usr/bin/env python3
"""Fresh pinned build and dependency audit of the abstract renewal contract."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
REPO = next(parent for parent in HERE.parents if (parent / 'AGENTS.md').exists())
SOURCE = HERE / 'RenewalLiquidity.lean'
ALLOWED_AXIOMS = {'propext', 'Quot.sound', 'Classical.choice'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def command(argv, cwd, env=None):
    return subprocess.run(argv, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=180)


def main():
    toolchain_bytes = (HERE / 'lean-toolchain').read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == 'leanprover/lean4:v4.29.1'
    prefix = ['lean', '+' + toolchain]
    version = command(prefix + ['--version'], HERE)
    version.check_returncode()
    assert 'version 4.29.1,' in version.stdout
    installation = command(prefix + ['--print-prefix'], HERE)
    installation.check_returncode()
    compiler = Path(installation.stdout.strip()) / 'bin/lean'
    frozen = SOURCE.read_bytes()
    source = frozen.decode()
    assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', source)
    assert not re.search(r'^\s*(axiom|constant)\s', source, re.M)
    assert re.findall(r'^import\s+(.+)$', source, re.M) == ['Std']
    declarations = set(re.findall(r'^theorem\s+(\w+)', source, re.M))
    requested = re.findall(r'^#print axioms\s+([\w.]+)\s*$', source, re.M)
    assert len(requested) == len(declarations)
    assert {name.rsplit('.', 1)[-1] for name in requested} == declarations

    with tempfile.TemporaryDirectory(prefix='recipient-renewal-liquidity-') as temporary:
        build = Path(temporary)
        (build / SOURCE.name).write_bytes(frozen)
        env = dict(os.environ, LEAN_PATH=str(build))
        invocation = [str(compiler), '-o', 'RenewalLiquidity.olean', SOURCE.name]
        result = command(invocation, build, env)

    logs = HERE / 'verification'
    logs.mkdir(exist_ok=True)
    log_path = logs / 'RenewalLiquidity.txt'
    log_path.write_text(result.stdout)
    audits = re.findall(
        r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
        result.stdout)
    dependencies = sorted({item.strip() for _, group in audits
                           for item in group.split(',') if item.strip()})
    unchanged = SOURCE.read_bytes() == frozen
    passed = (result.returncode == 0 and 'warning:' not in result.stdout
              and 'sorryAx' not in result.stdout and unchanged
              and {name for name, _ in audits} == set(requested)
              and len(audits) == len(requested)
              and set(dependencies).issubset(ALLOWED_AXIOMS))
    record = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'passed' if passed else 'failed',
        'scope': ('Abstract signed-event liquidity and block-contract composition. '
                  'The displayed event lists assume the specified actual outcomes, '
                  'available source/parts, zero learner cash and accessible transfer '
                  'law. No stochastic-simulator refinement or material production '
                  'theorem is claimed.'),
        'toolchain': toolchain,
        'toolchain_sha256': sha(toolchain_bytes),
        'lean_version': version.stdout.strip(),
        'compiler_binary': str(compiler),
        'compiler_sha256': sha(compiler.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'source': str(SOURCE.relative_to(REPO)),
        'source_sha256': sha(frozen),
        'source_unchanged_during_check': unchanged,
        'fresh_temporary_build': True,
        'imports': ['Std'],
        'command': invocation,
        'exit_code': result.returncode,
        'new_audited_declarations': len(audits),
        'audited_declarations': [name for name, _ in audits],
        'axioms': dependencies,
        'output': str(log_path.relative_to(HERE)),
        'output_sha256': sha(log_path.read_bytes()),
    }
    (HERE / 'verification.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': record['status'], 'declarations': len(audits),
                      'axioms': dependencies, 'scope': record['scope']}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
