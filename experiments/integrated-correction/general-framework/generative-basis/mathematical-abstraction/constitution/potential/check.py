#!/usr/bin/env python3
"""Check potentialist first-order truth and future-coverage boundaries."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE
while not (ROOT / 'AGENTS.md').exists():
    ROOT = ROOT.parent
FORMAL = PACKAGE / 'formal'
REPORTS = PACKAGE / 'verification'
TOOLCHAIN = (PACKAGE / 'lean-toolchain').read_text().strip()
DEPENDENCIES = []
MODULES = [('PotentialTruth', 'PotentialTruth'), ('CoverageBoundary', 'CoverageBoundary')]
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def named_declarations(source: str, namespace: str) -> list[tuple[str, str]]:
    return [(kind, f'{namespace}.{name}') for kind, name in re.findall(
        r'(?m)^(?:noncomputable\s+)?(theorem|def|abbrev|structure|inductive|instance)\s+([\w.]+)',
        source)]


def command(args: list[str], cwd: Path, env: dict[str, str], log: Path) -> str:
    result = subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True)
    output = result.stdout + result.stderr
    log.write_text(output)
    if result.returncode or re.search(r'\b(?:error|warning):', output):
        raise RuntimeError(f'Lean failed: {log}\n{output}')
    return output


def parse_audits(output: str) -> dict[str, list[str]]:
    result = {}
    pattern = r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
    for name, dependencies in re.findall(pattern, output, re.S):
        if name in result:
            raise RuntimeError(f'Duplicate audit: {name}')
        values = sorted(x.strip() for x in dependencies.split(',') if x.strip())
        if not set(values) <= ALLOWED:
            raise RuntimeError(f'Unapproved dependency: {name}: {values}')
        result[name] = values
    return result


def main() -> None:
    if TOOLCHAIN != 'leanprover/lean4:v4.29.1':
        raise RuntimeError(f'Unexpected toolchain: {TOOLCHAIN}')
    version = subprocess.check_output(['lean', f'+{TOOLCHAIN}', '--version'], text=True).strip()
    if 'version 4.29.1,' not in version:
        raise RuntimeError(version)
    REPORTS.mkdir(exist_ok=True)
    receipt = PACKAGE / 'verification.json'
    # A failed rerun must not leave a current-looking successful receipt.
    receipt.unlink(missing_ok=True)
    all_declarations, sources, inherited, frozen = [], {}, {}, {}
    for module, namespace in MODULES:
        path = FORMAL / f'{module}.lean'
        data = path.read_bytes()
        source = data.decode()
        prohibited = re.findall(r'\b(?:sorry|admit|axiom|native_decide|unsafe)\b', source)
        if prohibited:
            raise RuntimeError(f'Prohibited tokens in {path}: {prohibited}')
        declarations = named_declarations(source, namespace)
        if not declarations:
            raise RuntimeError(f'No audited declarations: {path}')
        all_declarations.extend(declarations)
        frozen[path] = data
        sources[str(path.relative_to(ROOT))] = {
            'sha256': digest(data), 'named_declarations': len(declarations),
            'theorems': sum(kind == 'theorem' for kind, _ in declarations),
        }
    driver = REPORTS / 'KernelAudit.lean'
    driver.write_text('\n'.join(f'import {module}' for module, _ in MODULES) + '\n\n' +
                      '\n'.join(f'#print axioms {name}' for _, name in all_declarations) + '\n')
    env = os.environ.copy()
    with tempfile.TemporaryDirectory(prefix='potential-truth-lean-') as temp:
        work = Path(temp)
        env['LEAN_PATH'] = str(work)
        for path, data in frozen.items():
            (work / path.name).write_bytes(data)
        (work / driver.name).write_bytes(driver.read_bytes())
        for module in DEPENDENCIES + [name for name, _ in MODULES]:
            command(['lean', f'+{TOOLCHAIN}', '-o', str(work / f'{module}.olean'),
                     str(work / f'{module}.lean')], work, env, REPORTS / f'{module}.log')
        output = command(['lean', f'+{TOOLCHAIN}', '-o', str(work / 'KernelAudit.olean'),
                          str(work / driver.name)], work, env, REPORTS / 'KernelAudit.log')
    for path, data in frozen.items():
        if path.read_bytes() != data:
            raise RuntimeError(f'Source changed during build: {path}')
    audits = parse_audits(output)
    expected = {name for _, name in all_declarations}
    if len(expected) != len(all_declarations) or set(audits) != expected:
        raise RuntimeError(f'Audit coverage mismatch: missing={expected-set(audits)}, extra={set(audits)-expected}')
    supporting = [Path(__file__), PACKAGE / 'lean-toolchain', driver,
                  *[REPORTS / f'{name}.log' for name in
                    DEPENDENCIES + [module for module, _ in MODULES] + ['KernelAudit']]]
    result = {
        'status': 'passed', 'toolchain': TOOLCHAIN, 'lean_version': version,
        'fresh_isolated_olean_build': True, 'frozen_source_build': True,
        'sources': sources, 'inherited_sources_sha256': inherited,
        'inherited_receipts_sha256': {},
        'theorems_checked': sum(kind == 'theorem' for kind, _ in all_declarations),
        'named_declarations_audited': len(audits),
        'standard_axioms_used': sorted({a for deps in audits.values() for a in deps}),
        'custom_axioms_or_holes': False, 'audits': audits,
        'supporting_files_sha256': {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in supporting},
        'scope': 'New declarations only in counts. Two sources built in order in a fresh '
                 'isolated directory; only bundled Std imported. Relational first-order '
                 'truth mirrored through future quantifiers under a supplied stable '
                 'interpretation, increasing frame and coverage from every stage. '
                 'Finite Nat prefixes and a branching failure are explicit. The coverage '
                 'converse tests all ambient unary predicates, not a fixed signature. '
                 'No independent admission, truth algorithm, higher-order extension or '
                 'unique metaphysical grounding is inferred.',
    }
    receipt.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'theorems_checked',
                                          'named_declarations_audited', 'standard_axioms_used']}))


if __name__ == '__main__':
    main()
