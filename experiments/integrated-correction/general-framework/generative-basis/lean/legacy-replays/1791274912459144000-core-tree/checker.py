#!/usr/bin/env python3
"""Fresh-build nondual episode/rearticulation with unchanged ancestor contracts."""

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CORE = HERE.parent
ROOT = CORE.parents[4]
PREDICTION = CORE / 'learning/construction/prediction'
ARCHIVE = HERE / 'verification-history/2026-10-06-before-core-tree-continuation'
MANIFEST_SHA256 = '3f1cb5f088cfc9cdb7b92668e986a016d2bc321e9af33874fc5573fe655450ca'
NEW = {
    'CoreTreeRearticulation': HERE / 'CoreTreeRearticulation.lean',
    'GenerativeEpisode': PREDICTION / 'GenerativeEpisode.lean',
    'GenerativeCoreTreeModel': CORE / 'GenerativeCoreTreeModel.lean',
}
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    manifest_bytes = (ARCHIVE / 'manifest.json').read_bytes()
    assert sha(manifest_bytes) == MANIFEST_SHA256
    manifest = json.loads(manifest_bytes)
    for item in manifest['files']:
        assert sha((ROOT / item['snapshot']).read_bytes()) == item['sha256'], item['snapshot']
        assert sha((ROOT / item['source']).read_bytes()) == item['sha256'], item['source']
    old = {m['module']: m for m in manifest['modules']}
    sources = {name: ROOT / m['source'] for name, m in old.items()}
    sources.update(NEW)
    frozen = {name: path.read_bytes() for name, path in sources.items()}
    checker = Path(__file__).read_bytes()
    imports = {}
    requests = {}
    for name, data in frozen.items():
        text = data.decode()
        if name in old:
            assert sha(data) == old[name]['source_sha256'], name
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text), name
        assert not re.search(r'^\s*(axiom|constant|opaque)\s', text, re.M), name
        imports[name] = re.findall(r'^import\s+(.+)$', text, re.M)
        assert set(imports[name]) <= {'Std', *sources}, name
        requests[name] = re.findall(r'^#print axioms (\S+)', text, re.M)
        assert requests[name] and len(requests[name]) == len(set(requests[name])), name
        if name in NEW:
            declarations = re.findall(r'^theorem\s+(\w+)', text, re.M)
            assert declarations == [x.rsplit('.', 1)[-1] for x in requests[name]], name
    assert imports['GenerativeCoreTreeModel'] == [
        'GenerativeNondualModel', 'GenerativeReceiptModel',
        'CoreTreeRearticulation', 'GenerativeEpisode']
    assert 'InquiryRoot.CoreTree.whole_tree_rearticulation' in requests['CoreTreeRearticulation']
    assert 'InquiryRoot.CoreTree.added_branch_conservative_iff' in requests['CoreTreeRearticulation']
    # Dependency order is checked rather than inherited from receipt ordering.
    order, done = [], {'Std'}
    while len(order) < len(sources):
        ready = [name for name in sources if name not in done and set(imports[name]) <= done]
        assert ready, 'Cyclic or incomplete source closure'
        order.extend(ready)
        done.update(ready)
    toolchain_bytes = (CORE / 'lean-toolchain').read_bytes()
    toolchain = toolchain_bytes.decode().strip()
    assert toolchain == 'leanprover/lean4:v4.29.1'
    prefix = ['lean', '+' + toolchain]
    version = run(prefix + ['--version'], CORE)
    version.check_returncode()
    assert 'version 4.29.1,' in version.stdout
    located = run(prefix + ['--print-prefix'], CORE)
    located.check_returncode()
    compiler = Path(located.stdout.strip()) / 'bin/lean'
    compiler_sha = sha(compiler.read_bytes())
    logs = HERE / 'core-tree-verification'
    logs.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix='generative-core-tree-') as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + '.lean')).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in order:
            result = run([str(compiler), '-o', name + '.olean', name + '.lean'], build, env)
            log = logs / (name + '.txt')
            log.write_text(result.stdout)
            entries = [(n, sorted(x.strip() for x in deps.split(',') if x.strip()))
                       for n, deps in AUDIT.findall(result.stdout)]
            actual = dict(entries)
            complete = len(entries) == len(actual) == len(requests[name]) and all(
                n == wanted or n.endswith('.' + wanted)
                for (n, _), wanted in zip(entries, requests[name]))
            contract = (actual == old[name]['audits'] if name in old
                        else all(not deps for deps in actual.values()))
            passed = result.returncode == 0 and 'warning:' not in result.stdout and complete and contract
            results.append(dict(module=name, source=str(sources[name].relative_to(ROOT)),
                                source_sha256=sha(frozen[name]), new_module=name in NEW,
                                exit_code=result.returncode, audits=actual,
                                audit_complete=complete, exact_dependency_contract=contract,
                                passed=passed, output=str(log.relative_to(HERE)),
                                output_sha256=sha(log.read_bytes())))
            if not passed:
                print(result.stdout)
                break
    preserved = sha((ARCHIVE / 'manifest.json').read_bytes()) == MANIFEST_SHA256 and all(
        sha((ROOT / item[k]).read_bytes()) == item['sha256']
        for item in manifest['files'] for k in ('source', 'snapshot'))
    unchanged = all(path.read_bytes() == frozen[name] for name, path in sources.items())
    infrastructure = (Path(__file__).read_bytes() == checker
                      and (CORE / 'lean-toolchain').read_bytes() == toolchain_bytes
                      and sha(compiler.read_bytes()) == compiler_sha)
    passed = (preserved and unchanged and infrastructure and len(results) == len(sources)
              and all(r['passed'] for r in results))
    record = dict(status='passed' if passed else 'failed',
                  checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  lean_version=version.stdout.strip(), compiler_sha256=compiler_sha,
                  checker_sha256=sha(checker), toolchain_sha256=sha(toolchain_bytes),
                  baseline_manifest_sha256=MANIFEST_SHA256,
                  preserved_ancestor_files=len(manifest['files']), ancestors_unchanged=preserved,
                  fresh_source_only_build=True, sources_unchanged=unchanged,
                  infrastructure_unchanged=infrastructure, modules=results,
                  inherited_modules=len(old), audits=sum(len(m['audits']) for m in results),
                  new_audits=sum(len(m['audits']) for m in results if m['new_module']),
                  new_axiom_dependencies=sorted({a for m in results if m['new_module']
                                                for deps in m['audits'].values() for a in deps}),
                  scope='One actual episode jointly changes receipt, memory and continuation support; '
                        'proof-level rearticulation preserves all contextual derivations in the existing calculus. '
                        'No new physical dynamics, no derivation of ontology or experience, and no identification '
                        'of the whole generative tree with deduction. Existing model and logical dependencies remain local inputs.')
    (HERE / 'core-tree-verification.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: record[k] for k in ('status', 'audits', 'new_audits',
                                           'new_axiom_dependencies', 'ancestors_unchanged')}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
