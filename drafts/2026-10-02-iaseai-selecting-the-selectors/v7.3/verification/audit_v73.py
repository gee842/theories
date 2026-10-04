"""Preservation, source reproducibility and delivery checks for V7.3."""
from pathlib import Path
import ast
import difflib
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT.parent / 'v7.2'
VERIFY = ROOT / 'verification'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def history(text):
    tail = text.split('## 8. Renderings', 1)[1]
    return re.split(r'\n## 12\.', tail, maxsplit=1)[0].rstrip()


def audit():
    baseline = json.loads((VERIFY / 'v72-baseline-manifest.json').read_text())
    changed = [name for name, value in baseline.items()
               if not (BASE / name).is_file() or digest(BASE / name) != value]
    docs = sorted(ROOT.glob('*.md'))
    before = {p.name: digest(p) for p in docs}
    run = subprocess.run([sys.executable, str(ROOT / 'src/assemble_v73.py')],
                         cwd=ROOT, capture_output=True, text=True)
    (VERIFY / 'assembly.log').write_text(run.stdout + run.stderr)
    after = {p.name: digest(p) for p in docs}
    previous = json.loads((BASE / 'src/keymap.json').read_text())
    current = json.loads((ROOT / 'src/keymap.json').read_text())
    identity = lambda row: tuple(row[k] for k in ('kind', 'number', 'file'))
    altered = [key for key in previous
               if key not in current or identity(current[key]) != identity(previous[key])]
    additions = sorted(set(current) - set(previous))
    historical_sources = history((BASE / 'src/reg/CLAIMS.md').read_text()) == history((ROOT / 'src/reg/CLAIMS.md').read_text())
    historical_outputs = history((BASE / 'CLAIMS.md').read_text()) == history((ROOT / 'CLAIMS.md').read_text())

    patch = []
    source_changes = {}
    for path in sorted((ROOT / 'src').rglob('*')):
        if not path.is_file() or path.suffix not in ('.md', '.py'):
            continue
        relative = path.relative_to(ROOT)
        old_relative = Path(str(relative).replace('v73', 'v72'))
        old_path = BASE / old_relative
        old = old_path.read_text() if old_path.exists() else ''
        new = path.read_text()
        if old != new:
            source_changes[str(relative)] = {'baseline': str(old_relative) if old_path.exists() else None,
                                             'sha256': digest(path)}
            patch.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                         fromfile='v7.2/' + str(old_relative), tofile='v7.3/' + str(relative)))
    (VERIFY / 'source-diff.patch').write_text(''.join(patch))
    (VERIFY / 'source-changes.json').write_text(json.dumps(source_changes, indent=2) + '\n')
    # These outputs are populated below; create their paths before auditing links.
    for name in ('summary.json', 'preservation.json', 'v73-input-manifest.json'):
        if not (VERIFY / name).exists():
            (VERIFY / name).write_text('{}\n')
    missing = []
    for path in docs:
        for link in re.findall(r'\]\(([^)\n]+)\)', path.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            name = re.sub(r':\d+$', '', link.split('#', 1)[0].strip('<>'))
            if name and not (path.parent / name).resolve().exists():
                missing.append({'document': path.name, 'target': link})

    log = (ROOT / 'checks_v73.log').read_text()
    matches = re.findall(r'^=== assertions: (\d+) passed, (\d+) failed', log, re.M)
    numerical = {'passed': int(matches[-1][0]), 'failed': int(matches[-1][1])} if matches else None
    tree = ast.parse((ROOT / 'checks_v73.py').read_text())
    order = next(ast.literal_eval(node.value) for node in tree.body
                 if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'ORDER' for target in node.targets))
    seen_blocks = re.findall(r'^=== ([A-Z0-9]{2}) \[', log, re.M)
    numerical_complete = bool(numerical and numerical['failed'] == 0 and seen_blocks == order and re.search(r'^=== done in ', log, re.M))
    xref_ok = (VERIFY / 'xref.log').read_text().rstrip().endswith('ALL CHECKS PASS')
    inputs = sorted({p for p in (ROOT / 'src').rglob('*') if p.is_file() and p.suffix in ('.md', '.py')} |
                    {ROOT / 'checks_v73.py', ROOT / 'xref_v73.py', Path(__file__).resolve()} |
                    set(VERIFY.glob('*_checks.py')) | set((ROOT / 'reviews').glob('*.md')) |
                    set((ROOT / 'reviews').glob('*.py')) |
                    set((ROOT / 'planning').glob('*.md')) | {ROOT / 'planning/USER-PROPOSAL.txt'})
    manifest = {str(p.relative_to(ROOT)): digest(p) for p in inputs}
    (VERIFY / 'v73-input-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    result = {
        'edition': 'V7.3', 'v72_files_checked': len(baseline), 'changed_v72_files': changed,
        'inherited_declarations': len(previous), 'inherited_identity_changes': altered,
        'new_declarations': additions, 'total_declarations': len(current),
        'historical_claims_8_to_11_source_preserved': historical_sources,
        'historical_claims_8_to_11_output_preserved': historical_outputs,
        'assembly_exit_code': run.returncode, 'assembly_reproducible': before == after,
        'missing_local_document_links': missing, 'cross_reference_checks_pass': xref_ok,
        'numerical': numerical, 'default_blocks': len(order), 'numerical_run_complete': numerical_complete,
        'institutional_test_N_run': False, 'general_institutional_preservation_proved': False,
        'reduced_finite_transition_review': 'accepted within maintained model premises',
        'real_institutional_pilot_run': False,
        'fresh_review_reports': ['V73-MATH-REVIEW.md', 'V73-INSTITUTION-REVIEW.md', 'V73-CLAIM-REVIEW.md'],
        'review_is_independent_human_certification': False,
        'verified_input_files': len(manifest), 'changed_source_files': len(source_changes),
        'document_sha256': after,
    }
    success = (not changed and not altered and additions == ['reformpath'] and historical_sources and
               historical_outputs and run.returncode == 0 and before == after and not missing and
               xref_ok and numerical_complete)
    result['audit_pass'] = success
    for name in ('preservation.json', 'summary.json'):
        (VERIFY / name).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return success


if __name__ == '__main__':
    sys.exit(0 if audit() else 1)
