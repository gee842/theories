#!/usr/bin/env python3
"""Owned proof, execution and index bindings; not independent acceptance."""
from collections import Counter
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
    document = HERE / 'VERSIONED-CORRECTION-INTEGRATION.md'
    chapter = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PLURAL-SYSTEMS-AND-CORRECTION.md'
    source = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-plural-systems-and-parent-correction.md'
    linked = 0

    def links(current, content):
        nonlocal linked
        for ref in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'[a-z]+://', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (current.parent / name).resolve() if name else current
            if target == HERE / 'VERSIONED-CORRECTION-CHECKS.json' and not target.exists():
                continue
            assert target.is_file(), (current.name, ref)
            if anchor:
                assert anchor in chain.heading_ids(target), (current.name, ref)
            linked += 1

    for current in (document, chapter, source):
        links(current, current.read_text())
    assert '> continue\n' in source.read_text()
    assert '33 new Lean theorems / 62 audits' in chapter.read_text()
    assert '33 new Lean theorems / 62 new declaration audits' in document.read_text()
    assert '62 inherited theorems / 100 audits' in document.read_text()
    receipt = json.loads((FORMAL / 'correction-versioned-verification.json').read_text())
    assert receipt['status'] == 'passed' and receipt['targets'] == ['CorrectionVersioned']
    assert receipt['new_theorems'] == 33 and receipt['new_audits'] == 62
    assert receipt['total_audits'] == 162 and not receipt['source_changed_during_run']
    modules = {m['module']: m for m in receipt['modules']}
    assert {name: (m['theorems'], m['audits']) for name, m in modules.items()} == {
        'CorrectionRelations': (39, 55), 'CorrectionHandoff': (23, 45),
        'CorrectionVersioned': (33, 62)}
    frozen = ROOT / receipt['snapshot']
    assert json.loads((frozen / 'verification.json').read_text()) == receipt
    for path in (FORMAL / 'check_correction_versioned.py', frozen / 'check_correction_versioned.py'):
        assert digest(path) == receipt['checker_sha256']
    assert digest(Path(receipt['commands'][0][0]).resolve()) == receipt['compiler_sha256']
    for module in receipt['modules']:
        assert digest(ROOT / module['source']) == module['source_sha256']
        assert digest(frozen / 'sources' / (module['module'] + '.lean')) == module['source_sha256']
    assert digest(frozen / 'lake-manifest.json') == receipt['manifest_sha256']
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(frozen / name) == fingerprint
    new = modules['CorrectionVersioned']
    counts = Counter(tuple(v) for v in new['nonempty_audits'].values())
    assert counts == {('propext',): 5, ('propext', 'Quot.sound'): 7,
                      ('propext', 'Classical.choice', 'Quot.sound'): 12}
    assert new['audits'] - len(new['nonempty_audits']) == 38
    assert Counter(d['kind'] for d in new['declarations']) == {
        'theorem': 33, 'def': 23, 'structure': 3, 'instance': 2, 'inductive': 1}
    code = (FORMAL / 'CorrectionVersioned.lean').read_text()
    assert 'set_option autoImplicit false' in code
    for name in ('every_prefix_correct', 'equal_whole_relations_do_not_protect_mixed_requests',
                 'late_registration_after_capture_can_fail', 'valid_head_completes',
                 'two_banks_can_both_be_unavailable', 'completion_allows_old_retirement'):
        assert 'theorem ' + name in code

    models = json.loads((FORMAL / 'correction-versioned-model-checks.json').read_text())
    assert models['status'] == 'passed'
    for name, fingerprint in models['sources'].items():
        assert digest(FORMAL / name) == fingerprint
    assert models['runner_sha256'] == digest(FORMAL / 'compare_correction_versioned.py')
    assert models['total_states'] == sum(g['states'] for g in models['graphs']) == 4512
    assert models['total_transitions'] == sum(g['transitions'] for g in models['graphs']) == 63168
    assert {(g['span'], g['capacity']) for g in models['graphs']} == {
        (span, capacity) for span in range(3) for capacity in (1, 2)}
    assert all(g['closed_reachable_graph'] and g['transitions'] == 14 * g['states']
               for g in models['graphs'])
    assert len(models['repeated_handoffs']) == 100
    for i, handoff in enumerate(models['repeated_handoffs']):
        assert handoff['iteration'] == i
        assert handoff['output'] == [[i % 2 == 1, i % 2 == 1]]
    assert len(models['thread_trials']) == 80
    modes = Counter(t['mode'] for t in models['thread_trials'])
    assert modes == {'versioned': 20, 'read_active_again': 20, 'premature_reuse': 20, 'split_capture': 20}
    for trial in models['thread_trials']:
        assert trial['output'] == [[True, trial['mode'] == 'versioned']]
        assert trial['history']

    data = chain.read_data()
    rows = {e['id']: e for section in data['sections'] for e in section['entries']}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    edits = json.loads((HERE / 'VERSIONED-CORRECTION-INDEX-EDITS.json').read_text())
    for ident in ('C33', 'M23', 'F29'):
        assert next(s for s in generated if s.startswith('| ' + ident + ' |')) in table
        for field in ('claim_zh', 'claim_en', 'scope_zh', 'scope_en'):
            assert edits['after_rows'][ident][field] in rows[ident][field]
        for link in rows[ident]['links']:
            path, fragment = chain.local_target(link['path'])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    assert edits['unrelated_entries_preserved'] == 90
    assert edits['unrelated_rendered_lines_preserved']
    assert len(edits['owned_fingerprints']) == 8
    for path, fingerprint in edits['owned_fingerprints'].items():
        assert digest(ROOT / path) == fingerprint, path
        assert data['reviewed_sources'][path] == fingerprint, path
    for insertion in edits['shared_insertions']:
        path = ROOT / insertion['path']
        assert insertion['added_text'] in path.read_text(), path
        links(path, insertion['added_text'])
    assert next(line for line in generated if line.startswith('内容更新 / Content updated:')) in table
    report = {
        'status': 'passed',
        'scope': 'Owned versioned correction documents, proof, controls and rows; not independent review or whole-table freshness',
        'new_theorems': 33, 'new_declaration_audits': 62, 'new_empty_audits': 38,
        'new_propext_only': 5, 'new_propext_quot': 7, 'new_propext_choice_quot': 12,
        'inherited_theorems': 62, 'inherited_audits': 100, 'total_audits': 162,
        'document_links': linked, 'model_states': 4512, 'model_transitions': 63168,
        'repeated_handoffs': 100, 'thread_trials': dict(modes),
        'scoped_rows': ['C33', 'M23', 'F29'], 'document_sha256': digest(document),
        'checker_sha256': digest(Path(__file__)), 'shared_index_pending': chain.changes(data)}
    (HERE / 'VERSIONED-CORRECTION-CHECKS.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'shared_index_pending'}, indent=2))


if __name__ == '__main__':
    main()
