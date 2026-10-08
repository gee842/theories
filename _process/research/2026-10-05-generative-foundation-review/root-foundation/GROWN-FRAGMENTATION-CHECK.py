#!/usr/bin/env python3
"""Check owned integration, primary-source bytes and fresh Lean receipt bindings."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
PACKAGE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics'
VERIFIED = PACKAGE / 'grown-fragmentation-verification'
SOURCE = ROOT / 'sources/evolutionary-selection/grown-fragmentation'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / 'GROWN-FRAGMENTATION-INDEX-EDITS.json').read_text())
    docs = [HERE / 'GROWN-FRAGMENTATION-INTEGRATION.md', VERIFIED / 'README.md',
            SOURCE / 'README.md']
    links = []

    def check_links(path, text):
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT) and target.is_file(), (path, ref)
            if anchor and target.suffix == '.md':
                assert unquote(anchor) in chain.heading_ids(target), (path, ref)
            links.append({'from': str(path.relative_to(ROOT)), 'reference': ref})

    for path in docs:
        check_links(path, path.read_text())
    for edit in edits['edits']:
        path = ROOT / edit['path']
        assert edit['owned_passage'] in path.read_text(), path
        check_links(path, edit['owned_passage'])
    chapter = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EVOLUTIONARY-ORGANIZATION.md'
    section = chapter.read_text().split('## Growth forms fragmentation possibilities\n', 1)[1].split('\n## ', 1)[0]
    check_links(chapter, section)
    full = chapter.with_name('THE-THEORY-OF-EVOLUTION.md')
    assert [l for l in full.read_text().splitlines() if l.startswith('| **')] == edits['six_requirement_rows']
    assert len(edits['six_requirement_rows']) == 6
    assert 'The separate connectionist learning recovery remains open.' not in chapter.read_text()

    proof = json.loads((VERIFIED / 'verification.json').read_text())
    assert proof['status'] == 'passed' and proof['fresh_temporary_build']
    assert proof['new_theorem_count'] == 31 and proof['new_audit_count'] == 59 and proof['total_audit_count'] == 326
    assert proof['source_unchanged_during_check']
    assert sha(VERIFIED / 'check.py') == proof['checker_sha256']
    for name, digest in proof['source_sha256'].items():
        assert sha(VERIFIED / 'sources' / name) == digest, name
        if name in proof['source_locations']:
            assert sha(PACKAGE.parent / proof['source_locations'][name]) == digest, name
        elif name == 'lean-toolchain':
            assert sha(PACKAGE / name) == digest, name
    for name, digest in proof['log_sha256'].items():
        assert sha(VERIFIED / name) == digest, name
    deps = proof['axiom_dependencies']['GrownFragmentation']
    assert len(deps) == 59
    assert sum(len(v) for v in proof['axiom_dependencies'].values()) == 326
    assert all(set(x) <= {'propext', 'Classical.choice', 'Quot.sound'} for module in proof['axiom_dependencies'].values() for x in module.values())

    originals = []
    for item in json.loads((SOURCE / 'manifest.json').read_text()):
        if 'file' not in item:
            assert 'error' in item
            continue
        path = SOURCE / item['file']
        assert path.stat().st_size == item['bytes'] and sha(path) == item['sha256']
        assert path.suffix == '.html'
        expected_title = {'jacobeen2018.html': 'Cellular packing, mechanical stress and the evolution of multicellularity',
                          'bozdag2023.html': 'De novo evolution of macroscopic multicellularity'}[path.name]
        assert expected_title in path.read_text(), path
        originals.append(item)
    assert len(originals) == 2

    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'C14')
    for path in edits['chain_update']['new_link_paths']:
        assert any(link['path'] == path for link in entry['links'])
    for path in edits['chain_update']['reviewed_owned_paths']:
        assert data['reviewed_sources'][path] == sha(ROOT / path), path
    expected = next(l for l in chain.render(data).splitlines() if l.startswith('| C14 |'))
    observed = next(l for l in chain.OUTPUT.read_text().splitlines() if l.startswith('| C14 |'))
    assert expected == observed
    assert edits['chain_update']['maintenance_owned_passage'] in (HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md').read_text()
    binding_paths = docs + [PACKAGE / 'GrownFragmentation.lean', VERIFIED / 'verification.json',
                           HERE / 'GROWN-FRAGMENTATION-INDEX-EDITS.json', SOURCE / 'manifest.json']
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned links, original bytes, kernel-check receipt and source bindings, C14 and six preserved broader requirements. No empirical test or repository-wide review.',
        'links_checked': len(links), 'links': links, 'original_sources_checked': len(originals),
        'original_bytes': sum(x['bytes'] for x in originals),
        'new_Lean_theorems': 31, 'new_declaration_audits': 59, 'closure_declaration_audits': 326,
        'owned_index_insertions': len(edits['edits']), 'full_theory_requirements_preserved': 6,
        'other_chain_entries_preserved_at_edit': edits['chain_update']['other_entries_preserved'],
        'C14_matches_paired_data': True, 'shared_full_render_matches': chain.OUTPUT.read_text() == chain.render(data),
        'shared_structural_errors': chain.validate(data), 'shared_reviews_pending': chain.changes(data),
        'artifact_sha256': {str(p.relative_to(ROOT)): sha(p) for p in binding_paths},
        'checker_sha256': sha(Path(__file__)),
    }
    (HERE / 'GROWN-FRAGMENTATION-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'links_checked', 'original_sources_checked',
        'original_bytes', 'new_Lean_theorems', 'new_declaration_audits', 'closure_declaration_audits', 'full_theory_requirements_preserved',
        'C14_matches_paired_data', 'shared_full_render_matches']}, indent=2))


if __name__ == '__main__':
    main()
