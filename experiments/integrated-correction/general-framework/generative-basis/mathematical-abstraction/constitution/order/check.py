#!/usr/bin/env python3
"""Fresh kernel builds and complete named-declaration audits for this package."""
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
MODULES = [('DenseOrder', 'OrderGenerativity')]
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args: list[str], env: dict[str, str], log: Path) -> str:
    completed = subprocess.run(args, cwd=PACKAGE, env=env, text=True, capture_output=True)
    output = completed.stdout + completed.stderr
    log.write_text(output)
    if completed.returncode != 0 or re.search(r'\b(?:error|warning):', output):
        raise RuntimeError(f'Lean check failed: {log}\n{output}')
    return output


def declarations(source: str, namespace: str) -> list[tuple[str, str]]:
    # These standalone modules have one declared namespace each.
    return [(kind, f'{namespace}.{name}') for kind, name in re.findall(
        r'(?m)^(?:noncomputable\s+)?(theorem|def|structure|inductive|instance)\s+([\w.]+)', source)]


def parse_audits(output: str) -> dict[str, list[str]]:
    audits: dict[str, list[str]] = {}
    pattern = r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
    for name, dependencies in re.findall(pattern, output, re.S):
        if name in audits:
            raise RuntimeError(f'Duplicate audit: {name}')
        values = sorted(x.strip() for x in dependencies.split(',') if x.strip())
        if not set(values) <= ALLOWED:
            raise RuntimeError(f'Unapproved kernel dependency: {name}: {values}')
        audits[name] = values
    return audits


def main() -> None:
    if TOOLCHAIN != 'leanprover/lean4:v4.29.1':
        raise RuntimeError(f'Unexpected toolchain: {TOOLCHAIN}')
    REPORTS.mkdir(exist_ok=True)
    env = os.environ.copy()
    version = subprocess.check_output(['lean', f'+{TOOLCHAIN}', '--version'], text=True).strip()
    if 'version 4.29.1,' not in version:
        raise RuntimeError(version)
    all_declarations: list[tuple[str, str]] = []
    sources: dict[str, dict[str, object]] = {}
    for module, namespace in MODULES:
        path = FORMAL / f'{module}.lean'
        source = path.read_text()
        # Deliberately scan the complete source, including comments.
        prohibited = re.findall(r'\b(?:sorry|admit|axiom|native_decide|unsafe)\b', source)
        if prohibited:
            raise RuntimeError(f'Prohibited source tokens in {path}: {prohibited}')
        ds = declarations(source, namespace)
        all_declarations.extend(ds)
        sources[str(path.relative_to(ROOT))] = {
            'sha256': digest(path), 'named_declarations': len(ds),
            'theorems': sum(kind == 'theorem' for kind, _ in ds),
        }
    driver = REPORTS / 'KernelAudit.lean'
    driver.write_text('\n'.join(f'import {module}' for module, _ in MODULES) + '\n\n' +
        '\n'.join(f'#print axioms {name}' for _, name in all_declarations) + '\n')
    with tempfile.TemporaryDirectory(prefix='dense-order-constitution-lean-') as temp:
        env['LEAN_PATH'] = temp
        for module, _ in MODULES:
            command(['lean', f'+{TOOLCHAIN}', '-o', str(Path(temp) / f'{module}.olean'),
                     str(FORMAL / f'{module}.lean')], env, REPORTS / f'{module}.log')
        output = command(['lean', f'+{TOOLCHAIN}', '-o', str(Path(temp) / 'KernelAudit.olean'),
                          str(driver)], env, REPORTS / 'KernelAudit.log')
    audits = parse_audits(output)
    expected = {name for _, name in all_declarations}
    if set(audits) != expected:
        raise RuntimeError(f'Audit mismatch missing={expected-set(audits)} extra={set(audits)-expected}')
    result = {
        'status': 'passed', 'toolchain': TOOLCHAIN, 'lean_version': version,
        'fresh_isolated_olean_build': True,
        'sources': sources,
        'named_declarations_audited': len(audits),
        'theorems_checked': sum(kind == 'theorem' for kind, _ in all_declarations),
        'standard_axioms_used': sorted({a for ds in audits.values() for a in ds}),
        'custom_axioms_or_holes': False,
        'audits': audits,
        'supporting_files_sha256': {
            str(p.relative_to(ROOT)): digest(p) for p in
            [Path(__file__), PACKAGE / 'lean-toolchain', driver, REPORTS / 'KernelAudit.log',
             *[REPORTS / f'{module}.log' for module, _ in MODULES]]},
        'scope': 'Full pure order/equality formula preservation and executable decision under explicit '
                 'dense linear order and no-endpoint hypotheses; finite before/between/after generation. '
                 'Not universal mathematical coverage or exclusive metaphysical grounding.',
    }
    (PACKAGE / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ['status', 'theorems_checked',
        'named_declarations_audited', 'standard_axioms_used']}, indent=2))


if __name__ == '__main__':
    main()
