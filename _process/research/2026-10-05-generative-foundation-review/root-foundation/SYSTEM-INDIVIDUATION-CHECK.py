#!/usr/bin/env python3
"""Check owned systems integration and preserved proof receipts, not new science."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import unquote
import hashlib, importlib.util, json, re, sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').is_file())
EDITS = HERE / 'SYSTEM-INDIVIDUATION-INDEX-EDITS.json'
OUTPUT = HERE / 'SYSTEM-INDIVIDUATION-CHECKS.json'
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
AUTHOR = LEAN / 'deeper/system-individuation-checks/20261007T233431.104249Z/receipt.json'
INDEPENDENT = HERE / 'development/system-individuation-review/20261007T233530.588639Z/receipt.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads(EDITS.read_text())
    author = json.loads(AUTHOR.read_text())
    independent = json.loads(INDEPENDENT.read_text())
    assert author['status'] == independent['status'] == 'passed'
    assert author['source_unchanged_during_check'] and independent['source_unchanged_during_check']
    assert author['counts']['new']['theorems'] == independent['new_theorems'] == 27
    assert author['counts']['new']['declarations'] == independent['new_declarations'] == 41
    assert author['counts']['inherited']['declarations'] == 18
    new = next(m for m in author['modules'] if m['new'])
    assert new['axiom_dependencies'] == independent['axiom_dependencies']
    assert not any(new['axiom_dependencies'].values())
    assert sha(AUTHOR) == independent['author_receipt_sha256']
    assert author['source_sha256'] == independent['source_sha256']
    for name, path in author['source_paths'].items():
        assert sha(ROOT / path) == author['source_sha256'][name]
    artifacts = 0
    for path, receipt in [(AUTHOR, author), (INDEPENDENT, independent)]:
        for name, digest in receipt['artifact_sha256'].items():
            assert sha(path.parent / name) == digest, (path, name)
            artifacts += 1
    for name, digest in author['checker_sha256'].items():
        current = (LEAN / 'deeper' / name) if name != 'audit_support.py' else (LEAN / 'universal-ethics/generative-capacity/check.py')
        assert sha(current) == digest
    assert sha(INDEPENDENT.parent.parent / 'check.py') == independent['artifact_sha256']['check.py']
    texts = []
    for path, digest in edits['owned_reviewed_sources'].items():
        p = ROOT / path
        assert sha(p) == digest, path
        if p.suffix == '.md':
            texts.append((p, p.read_text()))
    for fragment in edits['shared_fragments']:
        path = ROOT / fragment['path']
        assert path.read_text().count(fragment['text']) == 1, path
        texts.append((path, fragment['text']))
    links = []
    for path, content in texts:
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z]+:', ref):
                continue
            name, _, fragment = ref.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, ref)
            assert target.is_file() or target == OUTPUT, (path, ref)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (path, ref)
            links.append({'from': str(path.relative_to(ROOT)), 'reference': ref})
    data = chain.read_data()
    entries = {e['id']: e for section in data['sections'] for e in section['entries']}
    assert entries['C01'] == edits['rows_after']['C01']
    canonical = [line for line in chain.render(data).splitlines() if line.startswith('| C01 |')]
    actual = [line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| C01 |')]
    assert len(canonical) == 1 and actual == canonical
    for path, digest in edits['owned_reviewed_sources'].items():
        assert data['reviewed_sources'][path] == digest
    assert edits['other_rows_unchanged'] and edits['generated_other_rows_unchanged']
    review = (HERE / 'SYSTEM-INDIVIDUATION-REVIEW.md').read_text()
    assert 'Accepted' in review and 'Pending receipt' not in review
    for path, digest in edits['owned_reviewed_sources'].items():
        if path.endswith(('SYSTEM-INDIVIDUATION.md', 'SYSTEM-INDIVIDUATION-ARGUMENT.md',
                          'SYSTEM-INDIVIDUATION-FORMAL.md', 'SYSTEM-INDIVIDUATION-INTEGRATION.md')):
            assert digest in review, ('independent reviewed version mismatch', path)
    assert author['source_sha256']['SystemIndividuation'] in review
    result = {
        'passed': True, 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned document/source bindings, author and independent proof receipts, eight shared fragments, local links and C01. No empirical rerun or universal-foundation completion.',
        'new_theorems': 27, 'new_empty_audits': 41, 'inherited_audits': 18,
        'retained_proof_artifacts_checked': artifacts, 'local_links_checked': len(links),
        'links': links, 'shared_fragments': len(edits['shared_fragments']), 'owned_rows': ['C01'],
        'stronger_foundation_completed': False,
        'receipt_sha256': {str(p.relative_to(ROOT)): sha(p) for p in [AUTHOR, INDEPENDENT]},
        'owned_document_sha256': edits['owned_reviewed_sources'],
        'checker_sha256': sha(Path(__file__)), 'edit_record_sha256': sha(EDITS),
        'concurrent_global_changes_not_certified': chain.changes(data),
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['passed', 'new_theorems', 'new_empty_audits', 'retained_proof_artifacts_checked', 'local_links_checked', 'shared_fragments']}))


if __name__ == '__main__':
    main()
