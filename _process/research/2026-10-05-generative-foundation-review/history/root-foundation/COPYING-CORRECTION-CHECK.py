#!/usr/bin/env python3
"""Verify the owned formed correction-to-succession composition and disclose global status."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
sys.path.insert(0, str(ROOT))
from tools.research import registry, generative_chain as chain

PACKAGE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics'
VERIFIED = PACKAGE / 'copying-correction-verification'
STUDY = HERE / 'GROWN-FRAGMENTATION-INTEGRATION.md'
IDS = {'formed-copying-correction', 'formed-copying-registration', 'inherited-structural-copying', 'recurrent-chain-assembly',
       'growth-constrained-fragmentation', 'material-preparation-output'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    edits = json.loads((HERE / 'COPYING-CORRECTION-INDEX-EDITS.json').read_text())
    proof = json.loads((VERIFIED / 'verification.json').read_text())
    assert proof['status'] == 'passed' and proof['fresh_temporary_build']
    assert proof['source_unchanged_during_check']
    assert [proof[k] for k in ('new_theorem_count', 'new_audit_count', 'total_audit_count',
                              'new_empty_axiom_count')] == [27, 45, 529, 7]
    assert sha(VERIFIED / 'check.py') == proof['checker_sha256']
    for name, digest in proof['source_sha256'].items():
        assert sha(VERIFIED / 'sources' / name) == digest
        if name in proof['source_locations']:
            assert sha(PACKAGE.parent / proof['source_locations'][name]) == digest
        elif name == 'lean-toolchain':
            assert sha(PACKAGE / name) == digest
    for name, digest in proof['log_sha256'].items():
        assert sha(VERIFIED / name) == digest
    assert sum(map(len, proof['axiom_dependencies'].values())) == 529
    assert all(set(v) <= {'propext', 'Classical.choice', 'Quot.sound'}
               for module in proof['axiom_dependencies'].values() for v in module.values())

    records, load_errors = registry.load_records()
    owned = [r for r in records if r['id'] in IDS]
    assert len(owned) == len(IDS)
    errors, drift = registry.validate(owned)
    assert not errors and not drift, (errors, drift)
    global_errors, global_drift = registry.validate(records)
    global_errors = load_errors + global_errors

    links = []
    def check_links(path, body):
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, ref)
            # This run creates the receipt linked by the study; verify it after writing.
            assert target.is_file() or target == HERE / 'COPYING-CORRECTION-CHECKS.json', (path, ref)
            if anchor and target.suffix == '.md':
                assert unquote(anchor) in chain.heading_ids(target), (path, ref)
            links.append({'from': str(path.relative_to(ROOT)), 'reference': ref})
    source_dir = ROOT / 'sources/evolutionary-selection/structural-copying'
    for path in (STUDY, VERIFIED / 'README.md', source_dir / 'README.md'):
        check_links(path, path.read_text())
    chapter = ROOT / 'theories/becoming/chapters/EVOLUTIONARY-ORGANIZATION.md'
    owned_section = chapter.read_text().split('## Formed correction changes an existing successor\n', 1)[1].split('\n## ', 1)[0]
    check_links(chapter, owned_section)
    provenance = json.loads((source_dir / 'provenance.json').read_text())
    original = source_dir / provenance['file']
    assert original.stat().st_size == provenance['bytes'] == 107697
    assert sha(original) == provenance['sha256']

    new_source_dir = ROOT / 'sources/evolutionary-selection/copying-correction'
    check_links(new_source_dir / 'README.md', (new_source_dir / 'README.md').read_text())
    originals = json.loads((new_source_dir / 'provenance.json').read_text())['files']
    for item in originals:
        original_path = new_source_dir / item['file']
        assert original_path.stat().st_size == item['bytes']
        assert original_path.read_bytes().startswith(b'%PDF')
        assert sha(original_path) == item['sha256']
    assert len(originals) == 2
    prefix = STUDY.read_text().split('\n\n## Formed correction edits inherited material', 1)[0]
    assert hashlib.sha256(prefix.encode()).hexdigest() == edits['prior_study_prefix_sha256']

    full = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md'
    assert [l for l in full.read_text().splitlines() if l.startswith('| **')] == edits['six_requirement_rows']
    assert len(edits['six_requirement_rows']) == 6
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'C14')
    for k, suffix in edits['chain_update']['paired_suffixes'].items():
        assert suffix in entry[k]
    for path in edits['chain_update']['new_link_paths']:
        assert any(l['path'] == path for l in entry['links'])
    for path in edits['chain_update']['reviewed_owned_paths']:
        assert data['reviewed_sources'][path] == sha(ROOT / path)
    assert next(l for l in chain.render(data).splitlines() if l.startswith('| C14 |')) == \
           next(l for l in chain.OUTPUT.read_text().splitlines() if l.startswith('| C14 |'))

    cli = subprocess.run(['python3', '-B', 'tools/research/research.py', 'check', '--ids', *sorted(IDS)],
                         cwd=ROOT, text=True, capture_output=True)
    cli_report = json.loads(cli.stdout) if cli.stdout.strip() else {'stderr': cli.stderr}
    artifacts = [STUDY, PACKAGE / 'CopyingCorrection.lean', VERIFIED / 'verification.json',
                 VERIFIED / 'README.md', source_dir / 'README.md', source_dir / 'provenance.json',
                 HERE / 'COPYING-CORRECTION-INDEX-EDITS.json', new_source_dir / 'README.md',
                 new_source_dir / 'provenance.json'] + [registry.record_path(r) for r in owned]
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned material-correction result and its complete six-record dependency closure, '
                 'current Lean source/receipt, preserved primary bytes, links, C14 and six requirements. '
                 'Global metadata/navigation outcomes are reported separately; no empirical or independent-agent acceptance.',
        'new_theorem_count': 27, 'new_audit_count': 45, 'closure_audit_count': 529,
        'owned_record_errors': errors, 'owned_source_drift': drift,
        'global_metadata_errors': global_errors, 'global_source_drift': global_drift,
        'standard_focused_check_exit': cli.returncode, 'standard_focused_check': cli_report,
        'links_checked': len(links), 'links': links,
        'original_bytes_preserved': provenance['bytes'], 'new_originals_preserved': originals,
        'prior_study_prefix_preserved': True, 'six_requirements_preserved': True,
        'other_chain_entries_preserved_at_edit': edits['chain_update']['other_entries_preserved'],
        'C14_matches_paired_data': True, 'shared_chain_pending_reviews': chain.changes(data),
        'artifact_sha256': {str(p.relative_to(ROOT)): sha(p) for p in artifacts},
        'checker_sha256': sha(Path(__file__))}
    (HERE / 'COPYING-CORRECTION-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    assert (HERE / 'COPYING-CORRECTION-CHECKS.json').is_file()
    print(json.dumps({k: report[k] for k in ('status','new_theorem_count','new_audit_count',
        'closure_audit_count','links_checked','original_bytes_preserved','six_requirements_preserved',
        'standard_focused_check_exit','global_metadata_errors')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
