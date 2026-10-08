#!/usr/bin/env python3
"""Scoped bindings and links; not an independent scientific review."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    document = HERE / 'PLURAL-CORRECTION-INTEGRATION.md'
    chapter = ROOT / 'theories/becoming/chapters/PLURAL-SYSTEMS-AND-CORRECTION.md'
    source = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-plural-systems-and-parent-correction.md'
    linked = 0
    for current in [document, chapter, source]:
        for ref in re.findall(r'\]\(([^)]+)\)', current.read_text()):
            if re.match(r'[a-z]+://', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (current.parent / name).resolve() if name else current
            assert target.is_file(), ref
            if anchor:
                assert anchor in chain.heading_ids(target), ref
            linked += 1
    assert "we have many samples of systems - we can try" in source.read_text()
    assert "when a group of systems can be counted as one" in source.read_text()
    receipt = json.loads((FORMAL / 'correction-population-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['new_theorems'] == 37 and receipt['new_audits'] == 58
    assert receipt['total_audits'] == 89
    frozen = ROOT / receipt['snapshot']
    assert json.loads((frozen / 'verification.json').read_text()) == receipt
    assert digest(FORMAL / 'check_correction_population.py') == receipt['checker_sha256']
    assert digest(frozen / 'check_correction_population.py') == receipt['checker_sha256']
    for module in receipt['modules']:
        name = module['module'] + '.lean'
        assert digest(ROOT / module['source']) == module['source_sha256']
        assert digest(frozen / 'sources' / name) == module['source_sha256']
    assert digest(frozen / 'lake-manifest.json') == receipt['manifest_sha256']
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(frozen / name) == fingerprint
    assert all(set(values) <= {'propext', 'Quot.sound', 'Classical.choice'}
               for values in receipt['nonempty_audits'].values())
    models = json.loads((FORMAL / 'correction-population-model-checks.json').read_text())
    assert models['status'] == 'passed'
    for source, fingerprint in models['sources'].items():
        assert digest(FORMAL / source) == fingerprint
    assert models['runner_sha256'] == digest(FORMAL / 'compare_correction_population.py')
    assert models['probability_grid_points'] == len(models['probability_records']) == 101
    assert models['common_mixture_grid_points'] == 10201
    assert models['tenth_error'] == {'independent':'7/250','shared':'1/10','common_mixture':'313/2500'}
    assert models['parent_only_local_stop_laws'] == 0
    assert models['contained_site_states'] == 8 and len(models['pilot_transfer_cases']) == 8
    assert models['capacity_models'][0]['joint'] is False and models['capacity_models'][1]['joint'] is True
    for item in models['observation_models']:
        assert item['left_successful_policies'] == item['right_successful_policies'] == 0
        assert item['joint_successful_policies'] == 1
    data = chain.read_data()
    rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    for ident in ('C33', 'M23', 'F29'):
        assert next(s for s in generated if s.startswith('| '+ident+' |')) in table
        for link in rows[ident]['links']:
            path, fragment = chain.local_target(link['path'])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    edits = json.loads((HERE / 'PLURAL-CORRECTION-INDEX-EDITS.json').read_text())
    for path, fingerprint in edits['owned_fingerprints'].items():
        assert digest(ROOT / path) == fingerprint
        assert data['reviewed_sources'][path] == fingerprint
    # New navigation only: shared files' unrelated changes are not certified.
    nav = [ROOT / 'RESEARCH.md', ROOT / 'theories/becoming/README.md',
           ROOT / 'theories/becoming/chapters/ALIGNMENT-AND-GOVERNANCE.md',
           HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md', ROOT / 'sources/SOURCES.md']
    for path in nav:
        refs = [r for r in re.findall(r'\]\(([^)]+)\)', path.read_text())
                if any(name in r for name in ['PLURAL-CORRECTION-INTEGRATION.md','PLURAL-SYSTEMS-AND-CORRECTION.md'])]
        assert refs, path
        assert all((path.parent / r.split('#')[0]).resolve() in [document,chapter] for r in refs)
    assert next(line for line in generated if line.startswith('内容更新 / Content updated:')) in table
    report = {'status':'passed', 'scope':'Local proof/model/document bindings; plural-system correction and parent/subsystem relationships, not an independent review',
              'new_theorems':37, 'new_declaration_audits':58, 'inherited_theorems':19, 'inherited_repository_audits':31, 'document_links':linked,
              'probability_grid_points':101, 'mixture_grid_points':10201, 'scoped_rows':['C33','M23','F29'],
              'document_sha256':digest(document), 'shared_index_pending':chain.changes(data)}
    (HERE / 'PLURAL-CORRECTION-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'shared_index_pending'},indent=2))


if __name__ == '__main__':
    main()
