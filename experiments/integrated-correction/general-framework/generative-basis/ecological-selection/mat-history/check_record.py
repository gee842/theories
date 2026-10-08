#!/usr/bin/env python3
"""Check saved mat-history evidence bindings and scoped integration, not biology."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/evolutionary-selection/ferguson-2013'
STUDIES = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
THEORY = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    manifest = json.loads((SOURCE / 'manifest.json').read_text())
    verification = json.loads((HERE / 'verification.json').read_text())
    edits = json.loads((STUDIES / 'MAT-HISTORY-INDEX-EDITS.json').read_text())
    assert verification['checks_passed']
    assert verification['source_manifest_sha256'] == sha(SOURCE / 'manifest.json')
    assert verification['script_sha256'] == sha(HERE / 'inspect_movies.py')
    metadata = json.loads((SOURCE / 'biostudies.json').read_text())
    sizes = {f['path']: f['size'] for f in metadata['section']['files']}
    for f in manifest['files']:
        p = SOURCE / f['file']
        assert p.stat().st_size == f['bytes'] and sha(p) == f['sha256']
        if f['file'] in sizes:
            assert f['bytes'] == sizes[f['file']]
    counts = {'S1': 1198, 'S4': 1419, 'S5': 641, 'S6': 1537}
    for label, expected in counts.items():
        m = verification['movies'][label]
        assert m['encoded_frames'] == expected and not m['acquisition_time_mapping_verified']
        assert m['source_sha256'] == sha(SOURCE / m['source_file'])
        assert len({f['encoded_frame'] for f in m['selected']}) == len(m['selected'])
        assert all(f['full_decode_md5_match'] for f in m['selected'])
    assert sum(len(m['selected']) for m in verification['movies'].values()) == 44
    assert sum(m['encoded_frames'] for m in verification['movies'].values()) == 4795
    for view in verification['views'].values():
        assert sha(HERE / view['file']) == view['sha256']
    spec = importlib.util.spec_from_file_location('chain', STUDIES / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    data = chain.read_data()
    c14 = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'C14')
    assert c14 == edits['chain']['entry_after']
    scoped = copy.deepcopy(data)
    scoped['sections'] = [{'entries': [c14]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    row = next(s for s in chain.render(data).splitlines() if s.startswith('| C14 |'))
    assert row == next(s for s in chain.OUTPUT.read_text().splitlines() if s.startswith('| C14 |'))
    rows = [s for s in THEORY.read_text().splitlines() if s.startswith('| **')]
    assert len(rows) == 6
    assert rows == edits['completion_requirement_rows_before'] == edits['completion_requirement_rows_after']
    docs = [SOURCE / 'README.md', HERE / 'README.md', STUDIES / 'MAT-HISTORY-INTEGRATION.md', THEORY]
    checked_links = []
    for doc in docs:
        for ref in re.findall(r'\]\(([^\s)]+)\)', doc.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
                continue
            name, _, fragment = ref.partition('#')
            target = (doc.parent / unquote(name)).resolve() if name else doc
            assert target.is_relative_to(ROOT) and target.is_file(), (doc, ref)
            if fragment and target.suffix == '.md':
                assert unquote(fragment) in chain.heading_ids(target), (doc, ref)
            checked_links.append({'document': str(doc.relative_to(ROOT)), 'reference': ref})
    bound = docs + [SOURCE / 'manifest.json', HERE / 'verification.json',
                    HERE / 'inspect_movies.py', Path(__file__), STUDIES / 'MAT-HISTORY-INDEX-EDITS.json']
    pending = chain.changes(data)
    result = {
        'scope': 'Saved evidence bindings, original byte lengths, selected-frame receipts, local links and C14 rendering. Not biological replication, a fresh media decode, a proof or full-table certification.',
        'checks_passed': True,
        'original_files': len(manifest['files']),
        'original_bytes': sum(f['bytes'] for f in manifest['files']),
        'movies': counts, 'selected_frames': 44, 'decoded_frames': 4795,
        'derived_sheets': len(verification['views']),
        'links': checked_links, 'local_links_checked': len(checked_links),
        'completion_requirement_rows_unchanged': 6,
        'scoped_C14_valid': True,
        'unrelated_review_obligations': {k: len(v) for k, v in pending.items()},
        'bound_files': {str(p.relative_to(ROOT)): sha(p) for p in bound},
        'new_theorem_claimed': False, 'independent_agent_review_claimed': False,
        'biological_replication_claimed': False, 'full_theory_complete': False,
    }
    (STUDIES / 'MAT-HISTORY-CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['checks_passed', 'original_files', 'local_links_checked', 'completion_requirement_rows_unchanged', 'unrelated_review_obligations']}))


if __name__ == '__main__':
    main()
