#!/usr/bin/env python3
"""Check acquired-write provenance against unchanged predictor sources."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parents[2]
REPO = CORE.parents[4]
BASELINE = CORE / "verification-history/2026-10-06-before-acquired-record"
PREDICTOR = REPO / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal"
AUDITS = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parse(text):
    return [(name, sorted(x.strip() for x in deps.split(',') if x.strip()))
            for name, deps in AUDITS.findall(text)]


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    own_bytes = Path(__file__).read_bytes()
    manifest_bytes = (BASELINE / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    for item in manifest['files']:
        assert sha((REPO / item['snapshot']).read_bytes()) == item['sha256']
    previous = json.loads((BASELINE / 'predictor/verification.json').read_text())
    sources = {m['module']: REPO / m['source'] for m in previous['modules']}
    sources['OutcomeContinuation'] = CORE / 'OutcomeContinuation.lean'
    sources['AcquiredPredictionRecord'] = HERE / 'AcquiredPredictionRecord.lean'
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    allowed = {}
    for module in previous['modules']:
        assert sha(frozen[module['module']]) == module['source_sha256']
        saved = BASELINE / 'predictor' / module['output']
        assert sha(saved.read_bytes()) == module['output_sha256']
        allowed.update(dict(parse(saved.read_text())))

    seen = set()
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text), name
        assert not re.search(r'^\s*(axiom|constant|opaque)\s', text, re.M), name
        imports = re.findall(r'^import\s+(.+)$', text, re.M)
        assert all(item == 'Std' or item in seen for item in imports), (name, imports)
        seen.add(name)
        if name in {'OutcomeContinuation', 'AcquiredPredictionRecord'}:
            declarations = re.findall(r'^theorem\s+(\w+)', text, re.M)
            requested = re.findall(r'^#print axioms (\S+)', text, re.M)
            assert declarations and len(declarations) == len(set(declarations))
            assert declarations == [x.rsplit('.', 1)[-1] for x in requested], name
            if name == 'AcquiredPredictionRecord':
                assert {'trace_memory_is_replay', 'same_acquisition_same_next_command',
                        'acquired_record_and_executed_outcome',
                        'actual_acquisition_has_corrected_outcome'} <= set(declarations)

    toolchain_bytes = (CORE / 'lean-toolchain').read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == 'leanprover/lean4:v4.29.1'
    prefix = ['lean', '+' + toolchain]
    version = run(prefix + ['--version'], CORE)
    version.check_returncode()
    location = run(prefix + ['--print-prefix'], CORE)
    location.check_returncode()
    compiler = Path(location.stdout.strip()) / 'bin/lean'
    assert 'version 4.29.1,' in version.stdout
    logs = HERE / 'acquired-record-verification'
    logs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix='acquired-record-lean-') as temporary:
        build = Path(temporary)
        for name, source in frozen.items():
            (build / (name + '.lean')).write_bytes(source)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in sources:
            command = [str(compiler), '-o', name + '.olean', name + '.lean']
            result = run(command, build, env)
            output = logs / (name + '.txt')
            output.write_text(result.stdout)
            audits = parse(result.stdout)
            wanted = re.findall(r'^#print axioms (\S+)', frozen[name].decode(), re.M)
            matches = len(audits) == len(wanted) and bool(audits) and all(
                actual == expected or actual.endswith('.' + expected)
                for (actual, _), expected in zip(audits, wanted))
            added = {declaration: sorted(set(deps) - set(allowed.get(declaration, [])))
                     for declaration, deps in audits
                     if set(deps) - set(allowed.get(declaration, []))}
            clean = (result.returncode == 0 and 'warning:' not in result.stdout
                     and matches and not added)
            results.append({'module': name, 'source': str(sources[name].relative_to(REPO)),
                            'source_sha256': sha(frozen[name]), 'exit_code': result.returncode,
                            'audits': dict(audits), 'added_axiom_dependencies': added,
                            'clean': clean, 'output': str(output.relative_to(HERE)),
                            'output_sha256': sha(output.read_bytes())})
            if not clean:
                print(result.stdout)
                break
    sources_unchanged = all(path.read_bytes() == frozen[name] for name, path in sources.items())
    evidence_unchanged = all(sha((REPO / item['snapshot']).read_bytes()) == item['sha256']
                             for item in manifest['files'])
    checker_unchanged = Path(__file__).read_bytes() == own_bytes
    manifest_unchanged = (BASELINE / 'manifest.json').read_bytes() == manifest_bytes
    passed = (len(results) == len(sources) and all(x['clean'] for x in results)
              and sources_unchanged and evidence_unchanged and checker_unchanged and manifest_unchanged)
    record = {'status': 'passed' if passed else 'failed',
              'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'lean_version': version.stdout.strip(), 'compiler_sha256': sha(compiler.read_bytes()),
              'checker_sha256': sha(own_bytes), 'toolchain_sha256': sha(toolchain_bytes),
              'baseline_manifest_sha256': sha(manifest_bytes),
              'sources_unchanged': sources_unchanged, 'historical_evidence_unchanged': evidence_unchanged,
              'checker_unchanged': checker_unchanged, 'fresh_source_only_build': True,
              'inherited_sources_unchanged': True,
              'axiom_policy': 'Every new theorem has empty dependencies. Only exact historical '
                              'predictor declarations may retain their own archived dependencies.',
              'modules': results, 'audits': sum(len(x['audits']) for x in results),
              'new_bridge_audits': sum(len(x['audits']) for x in results if x['module'] == 'AcquiredPredictionRecord'),
              'scope': 'Actual paid predictor write provenance, native command dependence and '
                       'outcome-record interface. The old event law, decoder, update recipes and '
                       'scheduling remain supplied. No new physical law or assumption-free '
                       'self/ethical foundation is asserted. Typed material ancestry is an '
                       'inherited separate result, not newly re-proved here.'}
    destination = HERE / 'acquired-record-verification.json'
    destination.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'status': record['status'], 'modules': len(results),
                      'audits': record['audits'], 'new_bridge_audits': record['new_bridge_audits'],
                      'receipt': str(destination)}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
