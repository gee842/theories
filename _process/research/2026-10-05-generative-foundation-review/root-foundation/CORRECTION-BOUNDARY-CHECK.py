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
    document = HERE / 'CORRECTION-FRONTIER-BOUNDARY.md'
    linked = 0
    for ref in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        if re.match(r'[a-z]+://', ref):
            continue
        name, _, anchor = ref.partition('#')
        target = (document.parent / name).resolve() if name else document
        assert target.is_file(), ref
        if anchor:
            assert anchor in chain.heading_ids(target), ref
        linked += 1
    receipt = json.loads((FORMAL / 'correction-boundary-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['new_theorems'] == 34 and receipt['new_audits'] == 58
    assert receipt['total_audits'] == 58
    frozen = ROOT / receipt['snapshot']
    assert json.loads((frozen / 'verification.json').read_text()) == receipt
    assert digest(FORMAL / 'check_correction_boundary.py') == receipt['checker_sha256']
    assert digest(frozen / 'check_correction_boundary.py') == receipt['checker_sha256']
    for module in receipt['modules']:
        name = module['module'] + '.lean'
        assert digest(ROOT / module['source']) == module['source_sha256']
        assert digest(frozen / 'sources' / name) == module['source_sha256']
    assert digest(frozen / 'lake-manifest.json') == receipt['manifest_sha256']
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(frozen / name) == fingerprint
    assert all(set(values) <= {'propext', 'Quot.sound', 'Classical.choice'}
               for values in receipt['nonempty_audits'].values())
    models = json.loads((FORMAL / 'correction-boundary-model-checks.json').read_text())
    assert models['status'] == 'passed'
    for source, fingerprint in models['sources'].items():
        assert digest(FORMAL / source) == fingerprint
    assert models['runner_sha256'] == digest(FORMAL / 'compare_correction_boundary.py')
    assert models['maximum_update_sequence_length'] == 5 and models['update_sequences'] == 63
    assert models['delayed_test_cases'] == 63504
    assert models['completed'] == 32256 and models['rejected'] == 31248
    assert models['rational_mixtures'] == len(models['mixtures']) == 561
    assert models['transcripts_through_length_8'] == 511
    assert models['binary_conflicts_checked'] == 2044
    assert models['threaded_trials'] == len(models['threaded_results']) == 60
    for mode in [(False,False),(True,False),(True,True)]:
        trials = [t for t in models['threaded_results'] if (t['protected'],t['bypass']) == mode]
        assert len(trials) == 20
        assert all(t['writer_completed'] and t['delivered'] is (mode[0] and not mode[1]) for t in trials)
    data = chain.read_data()
    rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    for ident in ('M23', 'F29'):
        assert next(s for s in generated if s.startswith('| '+ident+' |')) in table
        for link in rows[ident]['links']:
            path, fragment = chain.local_target(link['path'])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    edits = json.loads((HERE / 'CORRECTION-BOUNDARY-INDEX-EDITS.json').read_text())
    for path, fingerprint in edits['owned_fingerprints'].items():
        assert digest(ROOT / path) == fingerprint
        assert data['reviewed_sources'][path] == fingerprint
    # Check only our new navigation target, without certifying unrelated prose.
    nav = [ROOT / 'RESEARCH.md', ROOT / 'theories/becoming/README.md',
           ROOT / 'theories/becoming/chapters/ALIGNMENT-AND-GOVERNANCE.md',
           HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md']
    for path in nav:
        refs = [r for r in re.findall(r'\]\(([^)]+)\)', path.read_text()) if 'CORRECTION-FRONTIER-BOUNDARY.md' in r]
        assert refs, path
        assert all((path.parent / r.split('#')[0]).resolve() == document for r in refs)
    report = {'status':'passed', 'scope':'Local proof/model/document bindings; terminal realizability boundary and local reservation protocol, not an independent review',
              'new_theorems':34, 'new_declaration_audits':58, 'inherited_repository_audits':0, 'document_links':linked,
              'delayed_test_cases':63504, 'rational_mixtures':561, 'threaded_trials':60, 'scoped_rows':['M23','F29'],
              'document_sha256':digest(document), 'shared_index_pending':chain.changes(data)}
    (HERE / 'CORRECTION-BOUNDARY-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'shared_index_pending'},indent=2))


if __name__ == '__main__':
    main()
