#!/usr/bin/env python3
"""Bind the owned recurrent-assembly continuation, records and Lean receipt."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
PACKAGE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics'
VERIFIED = PACKAGE / 'recurrent-assembly-verification'
STUDY = HERE / 'GROWN-FRAGMENTATION-INTEGRATION.md'
RECORDS = ROOT / 'theories/shengsheng-buxi-generative-existence/results/records'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / 'RECURRENT-ASSEMBLY-INDEX-EDITS.json').read_text())
    links = []

    def check_links(path, body):
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT) and target.is_file(), (path, ref)
            if anchor and target.suffix == '.md':
                assert unquote(anchor) in chain.heading_ids(target), (path, ref)
            links.append({'from': str(path.relative_to(ROOT)), 'reference': ref})

    check_links(STUDY, STUDY.read_text())
    check_links(VERIFIED / 'README.md', (VERIFIED / 'README.md').read_text())
    for edit in edits['edits']:
        path = ROOT / edit['path']
        assert edit['owned_passage'] in path.read_text(), path
        check_links(path, edit['owned_passage'])
    chapter = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md'
    assert [line for line in chapter.read_text().splitlines() if line.startswith('| **')] == edits['six_requirement_rows']
    assert len(edits['six_requirement_rows']) == 6
    proof = json.loads((VERIFIED / 'verification.json').read_text())
    assert proof['status'] == 'passed' and proof['fresh_temporary_build'] and proof['source_unchanged_during_check']
    assert (proof['new_theorem_count'], proof['new_audit_count'], proof['total_audit_count'], proof['new_empty_axiom_count']) == (31, 47, 373, 11)
    assert sha(VERIFIED / 'check.py') == proof['checker_sha256']
    for name, digest in proof['source_sha256'].items():
        assert sha(VERIFIED / 'sources' / name) == digest
        if name in proof['source_locations']:
            assert sha(PACKAGE.parent / proof['source_locations'][name]) == digest
        elif name == 'lean-toolchain':
            assert sha(PACKAGE / name) == digest
    for name, digest in proof['log_sha256'].items():
        assert sha(VERIFIED / name) == digest
    assert sum(map(len, proof['axiom_dependencies'].values())) == 373
    assert all(set(x) <= {'propext', 'Classical.choice', 'Quot.sound'}
               for module in proof['axiom_dependencies'].values() for x in module.values())
    ids = edits['canonical_records']
    run = subprocess.run(['python3', '-B', 'tools/research/research.py', 'check', '--ids', *ids],
                         cwd=ROOT, text=True, capture_output=True, check=True)
    registry = json.loads(run.stdout)
    assert not registry['errors'] and not registry['source_drift']
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'C14')
    for path in edits['chain_update']['new_link_paths']:
        assert any(link['path'] == path for link in entry['links'])
    for path in edits['chain_update']['reviewed_owned_paths']:
        assert data['reviewed_sources'][path] == sha(ROOT / path)
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| C14 |'))
    observed = next(line for line in chain.OUTPUT.read_text().splitlines() if line.startswith('| C14 |'))
    assert expected == observed
    artifacts = [STUDY, PACKAGE / 'RecurrentAssembly.lean', VERIFIED / 'README.md', VERIFIED / 'verification.json',
                 HERE / 'RECURRENT-ASSEMBLY-INDEX-EDITS.json'] + [RECORDS / (ident + '.json') for ident in ids]
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Owned continuation, source-bound Lean result, two migrated interfaces, new composition record, local links, paired C14 and preserved broad requirements. No empirical or independent-agent validation.',
                  new_theorem_count=31, new_audit_count=47, closure_audit_count=373,
                  links_checked=len(links), links=links, new_canonical_results=1, migrated_interfaces=2,
                  registry_check=registry, six_requirements_preserved=True,
                  other_chain_entries_preserved_at_edit=edits['chain_update']['other_entries_preserved'],
                  C14_matches_paired_data=True, full_chain_render_matches=chain.OUTPUT.read_text() == chain.render(data),
                  shared_structural_errors=chain.validate(data), shared_reviews_pending=chain.changes(data),
                  artifact_sha256={str(p.relative_to(ROOT)): sha(p) for p in artifacts}, checker_sha256=sha(Path(__file__)))
    (HERE / 'RECURRENT-ASSEMBLY-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'new_theorem_count', 'new_audit_count', 'closure_audit_count',
          'links_checked', 'new_canonical_results', 'migrated_interfaces', 'six_requirements_preserved', 'C14_matches_paired_data']}))


if __name__ == '__main__':
    main()
