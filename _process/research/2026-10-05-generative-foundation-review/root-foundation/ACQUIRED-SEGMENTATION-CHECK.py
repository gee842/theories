#!/usr/bin/env python3
"""Check this continuation's documents, frozen proofs and owned bilingual row.

This supersedes the predecessor's exact-row documentary check for current M26;
the predecessor's scientific receipt remains checked at its original scope.
No scientific rerun, independent review or full-goal certification is implied.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root'
THEORY = ROOT / 'theories/becoming/chapters/COGNITION-LEARNING-AND-EVOLUTION.md'
STUDY = HERE / 'ACQUIRED-SEGMENTATION-INTEGRATION.md'
spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
chain = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chain)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    links = []

    def check_links(p, text):
        for ref in re.findall(r'\]\(([^)]+)\)', text):
            if ref.startswith(('https://', 'http://')):
                continue
            name, _, fragment = ref.partition('#')
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and target.exists(), (str(p), ref)
            if fragment and target.suffix == '.md':
                assert unquote(fragment) in chain.heading_ids(target), (str(p), ref)
            links.append((str(p.relative_to(ROOT)), ref))

    # Own report is created before link validation, then replaced by the result.
    output = HERE / 'ACQUIRED-SEGMENTATION-CHECKS.json'
    output.write_text(json.dumps({'status': 'checking'}) + '\n')
    for p in [THEORY, STUDY, HERE / 'COMPOSITIONAL-TRANSMISSION-INTEGRATION.md']:
        check_links(p, p.read_text())

    receipts = {}
    for name, expected_modules in [
        ('compositional-acquisition-verification.json',
         [('KnowledgeCorrespondence', 20, 34), ('CompositionalAcquisition', 25, 52)]),
        ('compositional-formation-verification.json',
         [('KnowledgeCorrespondence', 20, 34), ('CompositionalAcquisition', 25, 52),
          ('CompositionalFormation', 37, 65)]),
        ('compositional-transmission-verification.json',
         [('KnowledgeCorrespondence', 20, 34), ('CompositionalAcquisition', 25, 52),
          ('CompositionalFormation', 37, 65), ('CompositionalTransmission', 27, 45)]),
        ('acquired-segmentation-verification.json',
         [('KnowledgeCorrespondence', 20, 34), ('CompositionalAcquisition', 25, 52),
          ('CompositionalFormation', 37, 65), ('CompositionalTransmission', 27, 45),
          ('AcquiredSegmentation', 23, 51)])
    ]:
        p = FORMAL / name
        receipt = json.loads(p.read_text())
        assert receipt['status'] == 'passed' and receipt['source_unchanged_during_check']
        frozen = FORMAL / receipt['retained_run']
        for module, sha in receipt['source_sha256'].items():
            assert digest(FORMAL / (module + '.lean')) == sha, module
            assert digest(frozen / (module + '.lean')) == sha, module
        for artifact, sha in receipt['artifact_sha256'].items():
            assert digest(frozen / artifact) == sha, artifact
        assert len(receipt['modules']) == len(expected_modules)
        for result, (module, theorems, declarations) in zip(receipt['modules'], expected_modules):
            assert result['module'] == module and result['kernel_checked']
            assert result['theorems'] == theorems and len(result['declarations']) == declarations
            assert len(result['axiom_dependencies']) == declarations
            assert all(set(deps) <= {'propext', 'Quot.sound', 'Classical.choice'}
                       for deps in result['axiom_dependencies'].values())
        receipts[name] = digest(p)

    edits = json.loads((HERE / 'ACQUIRED-SEGMENTATION-INDEX-EDITS.json').read_text())
    assert edits['all_other_entries_preserved'] and edits['all_other_rendered_lines_preserved']
    data = chain.read_data()
    found = [e for section in data['sections'] for e in section['entries'] if e['id'] == 'M26']
    assert found == [edits['updated_entry']]
    assert all(link in found[0]['links'] for link in edits['before_entry']['links'])
    canonical = next(line for line in chain.render(data).splitlines() if line.startswith('| M26 |'))
    assert canonical in chain.OUTPUT.read_text().splitlines()
    for name, sha in edits['reviewed_owned_sources'].items():
        assert digest(ROOT / name) == sha, name
        assert data['reviewed_sources'][name] == sha, name
    for name in edits['discovery_added']:
        assert name in data['known_discovery_paths']
    for name, change in edits['navigation_replacements'].items():
        p = ROOT / name
        assert change['inverse_preserves_other_bytes']
        assert change['new'] in p.read_text()
        check_links(p, change['new'])
    for name, change in edits['navigation_insertions'].items():
        p = ROOT / name
        assert change['inverse_preserves_other_bytes']
        assert change['text'] in p.read_text()
        check_links(p, change['text'])

    report = {
        'status': 'passed',
        'scope': 'Current owned theory/study/navigation, exact M26 and current/frozen proof bindings; other concurrent changes remain pending.',
        'local_links_checked': len(links),
        'new_theorems': 23, 'new_declaration_audits': 51,
        'inherited_declaration_audits': 196, 'owned_entry': 'M26',
        'proof_receipts_sha256': receipts,
        'files_sha256': {str(p.relative_to(ROOT)): digest(p) for p in [THEORY, STUDY]},
        'edit_record_sha256': digest(HERE / 'ACQUIRED-SEGMENTATION-INDEX-EDITS.json'),
        'other_source_reviews': chain.changes(data),
        'full_goal_complete': False, 'independent_review': False,
        'primary_evidence_reanalyzed': False,
    }
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ['other_source_reviews', 'files_sha256', 'proof_receipts_sha256']}))


if __name__ == '__main__':
    main()
