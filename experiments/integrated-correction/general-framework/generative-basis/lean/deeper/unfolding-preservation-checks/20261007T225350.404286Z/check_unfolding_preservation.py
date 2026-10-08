#!/usr/bin/env python3
"""Check the declared unfolding-preservation closure in a fresh Lean build.

Inherited audits are pinned to immutable receipts, not silently strengthened or
recounted as new results. All new explicit named declarations must have empty
axiom dependencies. Generated constructors/projections are checked through Lean
but are not separately counted. No empirical or universal adequacy claim.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LEAN = HERE.parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').is_file())
CAPACITY = LEAN / 'universal-ethics/generative-capacity'
SUPPORT = CAPACITY / 'check.py'
BASES = [
    (HERE / 'explanatory-composition-checks/20261007T223124.386181Z/receipt.json',
     'ee6c7cbe004afe3e0f6489948400488212a8f04b5267af98b8625ea786456ebd'),
    (CAPACITY / 'formed-grounds-checks/20261007T221235.147749Z/verification.json',
     '109f3cb54fbeba8e1b5e3ddd1eaf97fe5ae8045c3c2c17c12cb97dfd1c123a59'),
]
SOURCES = {
    'GenerativeCore': LEAN / 'GenerativeCore.lean',
    **{n: HERE / (n + '.lean') for n in ['HistoryRealization', 'ExplanatoryNecessity',
       'ExplanatoryStructure', 'ExplanatoryUniqueness']},
    'KnowledgeCorrespondence': LEAN / 'inquiry-root/KnowledgeCorrespondence.lean',
    **{n: CAPACITY / (n + '.lean') for n in ['NormativeActivity', 'StandardsBridge', 'FormedGrounds']},
    **{n: HERE / (n + '.lean') for n in ['UnfoldingPreservation', 'FormedUnfoldingPreservation']},
}
IMPORTS = {
    'GenerativeCore': ['Std'], 'HistoryRealization': ['GenerativeCore'],
    'ExplanatoryNecessity': ['HistoryRealization'],
    'ExplanatoryStructure': ['ExplanatoryNecessity'],
    'ExplanatoryUniqueness': ['ExplanatoryStructure'],
    'KnowledgeCorrespondence': ['Std'], 'NormativeActivity': ['KnowledgeCorrespondence'],
    'StandardsBridge': ['Std'], 'FormedGrounds': ['NormativeActivity', 'StandardsBridge'],
    'UnfoldingPreservation': ['GenerativeCore', 'ExplanatoryUniqueness'],
    'FormedUnfoldingPreservation': ['FormedGrounds', 'UnfoldingPreservation'],
}
NEW = {'UnfoldingPreservation', 'FormedUnfoldingPreservation'}
TOOLCHAIN = 'leanprover/lean4:v4.29.1'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def audit_map(output):
    answer = {n: [] for n in re.findall(r"'([^']+)' does not depend on any axioms", output)}
    answer.update({n: [a.strip() for a in deps.split(',') if a.strip()]
                   for n, deps in re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", output)})
    return answer


def main():
    spec = importlib.util.spec_from_file_location('audit_support', SUPPORT)
    support = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(support)
    baselines = []
    for path, expected in BASES:
        raw = path.read_bytes()
        assert digest(raw) == expected, ('baseline changed', path)
        baselines.append(json.loads(raw))
    expected_hashes, inherited = {}, {}
    for m in baselines[0]['modules'][:5]:
        name = Path(m['source']).stem
        expected_hashes[name] = m['sha256']
        inherited[name] = {n: [] for n in m['empty_axiom_audits']}
        inherited[name].update(m['standard_axiom_audits'])
    for m in baselines[1]['modules']:
        name = m['module']
        expected_hashes[name] = baselines[1]['source_sha256'][name]
        inherited[name] = m['axiom_dependencies']
    assert sum(map(len, inherited.values())) == 248
    sources = {n: p.read_bytes() for n, p in SOURCES.items()}
    inventories = {}
    for name, raw in sources.items():
        code = support.code_only(raw.decode())
        assert re.findall(r'^import\s+(.+)$', code, re.M) == IMPORTS[name], name
        normalized = re.sub(r'^import\s+[^\n]+', 'import Std', code, flags=re.M)
        normalized = re.sub(r'^noncomputable def\b', 'def', normalized, flags=re.M)
        inventories[name] = support.declarations(normalized)
        if name not in NEW:
            assert digest(raw) == expected_hashes[name], ('inherited source changed', name)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    retained = HERE / 'unfolding-preservation-checks' / stamp
    retained.mkdir(parents=True, exist_ok=False)
    helpers = {Path(__file__).name: Path(__file__).read_bytes(), 'audit_support.py': SUPPORT.read_bytes()}
    for name, raw in helpers.items():
        (retained / name).write_bytes(raw)
    for name, raw in sources.items():
        (retained / (name + '.lean')).write_bytes(raw)
    receipt = {
        'status': 'checking', 'utc': stamp, 'toolchain': TOOLCHAIN,
        'scope': 'Native finite-trace fidelity and same-law acquired-ground witnesses; conditional correspondence, no universal explanatory or empirical completion claim.',
        'source_paths': {n: str(p.relative_to(ROOT)) for n, p in SOURCES.items()},
        'source_sha256': {n: digest(raw) for n, raw in sources.items()},
        'baselines': [{'path': str(p.relative_to(ROOT)), 'sha256': h} for p, h in BASES],
        'checker_sha256': {n: digest(raw) for n, raw in helpers.items()},
        'new_modules': sorted(NEW), 'modules': [],
    }
    try:
        binary = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
        receipt['lean_binary_sha256'] = digest(binary.read_bytes())
        command = [str(Path.home() / '.elan/bin/lean'), '+' + TOOLCHAIN]
        with tempfile.TemporaryDirectory(prefix='unfolding-preservation-') as scratch:
            work = Path(scratch)
            env = {**os.environ, 'LEAN_PATH': str(work)}
            def run(args, log):
                p = subprocess.run(command + args, cwd=work, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, (log, p.stdout)
                assert not re.search(r'\b(?:error|warning):', p.stdout), (log, p.stdout)
                return p.stdout
            receipt['lean_version'] = run(['--version'], 'version.log').strip()
            assert 'version 4.29.1' in receipt['lean_version']
            for name, raw in sources.items():
                (work / (name + '.lean')).write_bytes(raw)
            for name in sources:
                run(['-o', name + '.olean', name + '.lean'], name + '.log')
                by_name = {d['name']: d for d in inventories[name]}
                names = list(by_name) if name in NEW else list(inherited[name])
                assert set(names) <= set(by_name), (name, set(names) - set(by_name))
                for suffix, commands in [
                    ('AxiomAudit', ['#print axioms ' + n for n in names]),
                    ('Signatures', ['#check ' + n for n in names if by_name[n]['kind'] == 'theorem']),
                ]:
                    filename = name + suffix + '.lean'
                    content = 'import ' + name + '\n' + '\n'.join(commands) + '\n'
                    (work / filename).write_text(content)
                    (retained / filename).write_text(content)
                    output = run([filename], name + suffix + '.log')
                    if suffix == 'AxiomAudit':
                        dependencies = audit_map(output)
                assert set(dependencies) == set(names), name
                if name in NEW:
                    assert not any(dependencies.values()), (name, dependencies)
                else:
                    assert dependencies == inherited[name], ('inherited dependency map changed', name)
                receipt['modules'].append({
                    'module': name, 'new': name in NEW,
                    'declarations': [by_name[n] for n in names],
                    'theorems': sum(by_name[n]['kind'] == 'theorem' for n in names),
                    'axiom_dependencies': dependencies, 'kernel_checked': True,
                    'audit_scope': 'all explicit named declarations' if name in NEW else 'exact inherited baseline inventory',
                })
        assert all(SOURCES[n].read_bytes() == raw for n, raw in sources.items()), 'source changed during check'
        assert Path(__file__).read_bytes() == helpers[Path(__file__).name]
        assert SUPPORT.read_bytes() == helpers['audit_support.py']
        receipt['source_unchanged_during_check'] = True
        receipt['counts'] = {kind: {
            'modules': sum(m['new'] == is_new for m in receipt['modules']),
            'declarations': sum(len(m['declarations']) for m in receipt['modules'] if m['new'] == is_new),
            'theorems': sum(m['theorems'] for m in receipt['modules'] if m['new'] == is_new),
            'empty_audit_dependencies': sum(not aa for m in receipt['modules'] if m['new'] == is_new for aa in m['axiom_dependencies'].values()),
            'standard_dependency_audits': sum(bool(aa) for m in receipt['modules'] if m['new'] == is_new for aa in m['axiom_dependencies'].values()),
        } for kind, is_new in [('new', True), ('inherited', False)]}
        receipt['artifact_sha256'] = {p.name: digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()}
        receipt['status'] = 'passed'
    except Exception as error:
        receipt['status'] = 'failed'
        receipt['error'] = str(error)
        raise
    finally:
        (retained / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        (HERE / 'unfolding-preservation-verification.json').write_text(json.dumps({
            'status': receipt['status'], 'receipt': str((retained / 'receipt.json').relative_to(ROOT)),
            'counts': receipt.get('counts'),
        }, indent=2) + '\n')
    print(json.dumps({'status': receipt['status'], 'counts': receipt['counts'], 'receipt': str(retained / 'receipt.json')}))


if __name__ == '__main__':
    main()
