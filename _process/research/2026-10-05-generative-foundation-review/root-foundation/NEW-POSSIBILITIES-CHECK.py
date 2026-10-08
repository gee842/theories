#!/usr/bin/env python3
"""Check owned documentation, local links and exact successful Lean bindings.

This validates preservation and correspondence of the saved package, not the
philosophical argument or empirical interpretation. It does not rerun science.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
SOURCE = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-formation-of-new-possibilities.md'
DOCS = [THEORY / 'NEW-POSSIBILITIES.md', HERE / 'NEW-POSSIBILITIES-INTEGRATION.md',
        HERE / 'NEW-POSSIBILITIES-REVIEW.md', SOURCE]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    snapshot = {p: p.read_bytes() for p in DOCS}
    links = []
    for path, data in snapshot.items():
        for reference in re.findall(r'\]\(([^)]+)\)', data.decode()):
            if re.match(r'https?://', reference):
                continue
            target, _, fragment = reference.partition('#')
            resolved = (path.parent / unquote(target)).resolve() if target else path
            assert resolved.is_relative_to(ROOT), (path, reference)
            assert resolved.exists(), (path, reference)
            # Current owned local links contain no anchors; avoid pretending
            # existence validates a fragment if one is added later.
            assert not fragment, (path, 'add anchor validation before using fragments', reference)
            links.append({'from': str(path.relative_to(ROOT)), 'target': reference})
    receipt_path = LEAN / 'new-possibilities-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    assert (receipt['new_theorems'], receipt['new_audits'], receipt['total_audits']) == (45, 64, 92)
    run = ROOT / receipt['snapshot']
    assert json.loads((run / 'verification.json').read_text()) == receipt
    for module in receipt['modules']:
        current = ROOT / module['source']
        frozen = run / 'sources' / (module['module'] + '.lean')
        assert sha(current) == sha(frozen) == module['source_sha256']
    checker = LEAN / 'check_new_possibilities.py'
    assert sha(checker) == sha(run / checker.name) == receipt['checker_sha256']
    for name, digest in receipt['log_sha256'].items():
        assert sha(run / name) == digest
    assert all(set(axioms) <= {'propext', 'Quot.sound', 'Classical.choice'}
               for axioms in receipt['nonempty_audits'].values())
    spec = importlib.util.spec_from_file_location('chain_builder', HERE / 'build_generative_chain.py')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    chain = builder.read_data()
    errors = builder.validate(chain)
    assert not errors, errors
    rows = {e['id']: e for s in chain['sections'] for e in s['entries']}
    assert rows['C25']['links'][0]['path'].endswith('NEW-POSSIBILITIES.md')
    assert '45 new theorems and 64' in rows['F17']['claim_en']
    assert '45项新定理／64项' in rows['F17']['claim_zh']
    assert builder.OUTPUT.read_text() == builder.render(chain)
    for p, data in snapshot.items():
        assert p.read_bytes() == data, f'Concurrent edit: {p}'
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned document links, proof receipt/source bindings and paired chain entries. '
                 'Not independent scientific review or verification of concurrent studies.',
        'new_theorems': receipt['new_theorems'], 'new_audits': receipt['new_audits'],
        'full_closure_audits': receipt['total_audits'],
        'lean_receipt': str(receipt_path.relative_to(ROOT)),
        'lean_receipt_sha256': sha(receipt_path),
        'documents': {str(p.relative_to(ROOT)): sha(p) for p in DOCS},
        'checker_sha256': sha(Path(__file__)), 'local_links': links,
        'paired_rows': ['C25', 'F17'], 'chain_entries_at_check': len(rows),
        'concurrent_pages_left_for_their_maintainers': builder.changes(chain)['new_pages'],
    }
    (HERE / 'NEW-POSSIBILITIES-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'new_theorems', 'new_audits', 'full_closure_audits', 'paired_rows']}))


if __name__ == '__main__':
    main()
