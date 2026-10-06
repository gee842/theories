#!/usr/bin/env python3
"""Fresh-check the receipt extension with exact predecessor dependency pins."""

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
BASELINE = CORE / 'verification-history/2026-10-06-before-receipt-identification'
MANIFEST_SHA256 = '9dc9b7122716dec42c90c0e2692382a22656dd702d63a28d385f0cdafae5a0d7'
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")
NEW = {
    'ReceiptIdentification': HERE / 'ReceiptIdentification.lean',
    'ReceiptRevisionBoundary': HERE / 'ReceiptRevisionBoundary.lean',
    'GenerativeReceiptModel': CORE / 'GenerativeReceiptModel.lean',
}
REQUIRED = {
    'ReceiptIdentification': {'complete_decoder_correct_iff', 'partial_decode_exact',
                              'all_failure_records_do_not_identify', 'sound_complete_decoder_unique'},
    'ReceiptRevisionBoundary': {'enabled_after_work_must_be_write', 'available_work_write_update',
                                'acquired_success_does_not_identify_current_regime',
                                'actual_dynamic_successes_refute_fixed_pooling'},
    'GenerativeReceiptModel': {'partial_answer_matches_actual_receipt',
                               'actual_next_step_uses_fresh_receipt'},
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def audits(text):
    return [(name, sorted(a.strip() for a in deps.split(',') if a.strip()))
            for name, deps in AUDIT.findall(text)]


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    checker = Path(__file__).read_bytes()
    manifest_bytes = (BASELINE / 'manifest.json').read_bytes()
    assert sha(manifest_bytes) == MANIFEST_SHA256
    manifest = json.loads(manifest_bytes)
    for item in manifest['files']:
        assert sha((REPO / item['snapshot']).read_bytes()) == item['sha256']
    sources, hashes, old_audits = {}, {}, {}
    for tag, source_base in [('core', CORE), ('acquired', REPO)]:
        prior = json.loads((BASELINE / tag / 'verification.json').read_text())
        assert prior['status'] == 'passed'
        for module in prior['modules']:
            name = module['module']
            source = source_base / module['source']
            assert sha(source.read_bytes()) == module['source_sha256'], name
            log = BASELINE / tag / 'logs' / (name + '.txt')
            assert sha(log.read_bytes()) == module['output_sha256'], name
            entries = audits(log.read_text())
            assert entries, name
            if name in sources:
                assert sources[name] == source and old_audits[name] == entries, name
            else:
                sources[name], hashes[name], old_audits[name] = source, module['source_sha256'], entries
    sources.update(NEW)
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    seen = {'Std'}
    for name, data in frozen.items():
        text = data.decode()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text), name
        assert not re.search(r'^\s*(axiom|constant|opaque)\s', text, re.M), name
        imports = re.findall(r'^import\s+(.+)$', text, re.M)
        assert set(imports) <= seen, (name, imports)
        seen.add(name)
        if name in NEW:
            declarations = re.findall(r'^theorem\s+(\w+)', text, re.M)
            requests = re.findall(r'^#print axioms (\S+)', text, re.M)
            assert declarations and len(declarations) == len(set(declarations))
            assert declarations == [n.rsplit('.', 1)[-1] for n in requests], name
            assert REQUIRED[name] <= set(declarations), name
        if name == 'GenerativeReceiptModel':
            assert imports == ['GenerativeOutcomeModel', 'ReceiptRevisionBoundary']
    toolchain_bytes = (CORE / 'lean-toolchain').read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == 'leanprover/lean4:v4.29.1'
    prefix = ['lean', '+' + toolchain]
    version = run(prefix + ['--version'], CORE); version.check_returncode()
    location = run(prefix + ['--print-prefix'], CORE); location.check_returncode()
    compiler = Path(location.stdout.strip()) / 'bin/lean'
    assert 'version 4.29.1,' in version.stdout
    logs = HERE / 'receipt-identification-verification'; logs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix='receipt-identification-lean-') as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + '.lean')).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in sources:
            command = [str(compiler), '-o', name + '.olean', name + '.lean']
            result = run(command, build, env)
            log = logs / (name + '.txt'); log.write_text(result.stdout)
            actual = audits(result.stdout)
            requests = re.findall(r'^#print axioms (\S+)', frozen[name].decode(), re.M)
            matched = bool(actual) and len(actual) == len(requests) and all(
                a == p or a.endswith('.' + p) for (a, _), p in zip(actual, requests))
            dependency_ok = (actual == old_audits[name] if name in old_audits
                             else all(not deps for _, deps in actual))
            clean = result.returncode == 0 and 'warning:' not in result.stdout and matched and dependency_ok
            results.append({'module': name, 'source': str(sources[name].relative_to(REPO)),
                            'source_sha256': sha(frozen[name]), 'exit_code': result.returncode,
                            'audits': dict(actual), 'dependency_contract_met': dependency_ok,
                            'new_module': name in NEW, 'clean': clean,
                            'output': str(log.relative_to(HERE)), 'output_sha256': sha(log.read_bytes())})
            if not clean:
                print(result.stdout)
                break
    unchanged = all(path.read_bytes() == frozen[name] for name, path in sources.items())
    history_unchanged = (sha((BASELINE / 'manifest.json').read_bytes()) == MANIFEST_SHA256 and all(
        sha((REPO / item['snapshot']).read_bytes()) == item['sha256'] for item in manifest['files']))
    checker_unchanged = Path(__file__).read_bytes() == checker
    passed = (len(results) == len(sources) and unchanged and history_unchanged and checker_unchanged
              and all(r['clean'] for r in results))
    record = {'status': 'passed' if passed else 'failed',
              'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'lean_version': version.stdout.strip(), 'compiler_sha256': sha(compiler.read_bytes()),
              'checker_sha256': sha(checker), 'toolchain_sha256': sha(toolchain_bytes),
              'baseline_manifest_sha256': MANIFEST_SHA256, 'historical_files_checked': len(manifest['files']),
              'fresh_source_only_build': True, 'sources_unchanged': unchanged,
              'checker_unchanged': checker_unchanged, 'historical_evidence_unchanged': history_unchanged,
              'unchanged_inherited_modules': len(old_audits),
              'modules': results, 'audits': sum(len(r['audits']) for r in results),
              'new_audits': sum(len(r['audits']) for r in results if r['new_module']),
              'new_axiom_dependencies': sorted({a for r in results if r['new_module']
                                                for deps in r['audits'].values() for a in deps}),
              'scope': 'Receipt identification relative to the unchanged response relation; '
                       'fixed-regime compatibility, partial certainty, derived work/write timing '
                       'and actual stale/fresh receipt histories. No new physical dynamics, '
                       'installed partial controller, universal stability or ethical premise. '
                       'Stochastic outages remain a separate executable implementation.'}
    destination = HERE / 'receipt-identification-verification.json'
    destination.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: record[k] for k in ['status', 'audits', 'new_audits',
                                           'new_axiom_dependencies', 'unchanged_inherited_modules']}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
