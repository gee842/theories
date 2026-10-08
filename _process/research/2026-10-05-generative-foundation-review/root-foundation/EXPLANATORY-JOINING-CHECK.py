#!/usr/bin/env python3
"""Check this study's documents, owned index edits and frozen Lean receipt.
Does not rerun proofs or certify concurrently edited research branches.
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
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
OUTPUT = HERE / 'EXPLANATORY-JOINING-CHECKS.json'
RECEIPT = LEAN / 'explanatory-local-units-checks/20261007T225438.405152Z/receipt.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    docs = [ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EXPLANATORY-NECESSITY.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md',
            HERE / 'EXPLANATORY-JOINING-INTEGRATION.md', HERE / 'EXPLANATORY-COMPOSITION-INTEGRATION.md']
    edits = json.loads((HERE / 'EXPLANATORY-JOINING-INDEX-EDITS.json').read_text())
    contents = [(p, p.read_text()) for p in docs]
    for item in edits['shared_file_insertions']:
        p = ROOT / item['path']
        assert item['preserved_other_bytes'] and item['inserted_text'] in p.read_text(), item['path']
        contents.append((p, item['inserted_text']))
    links = []
    for p, content in contents:
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z]+:', ref):
                continue
            name, _, fragment = ref.partition('#')
            target = (p.parent / unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT), ref
            assert target.is_file() or target == OUTPUT, (p, ref)
            if fragment:
                assert unquote(fragment) in chain.heading_ids(target), (p, ref)
            links.append({'from': str(p.relative_to(ROOT)), 'reference': ref})
    receipt = json.loads(RECEIPT.read_text())
    assert receipt['passed'] and receipt['total_declaration_audits'] == 128 and receipt['total_empty_axiom_audits'] == 105 and receipt['total_standard_axiom_audits'] == 23
    assert receipt['checker_sha256'] == sha(LEAN / 'check_explanatory_local_units.py')
    bindings = []
    for m in receipt['modules']:
        source = ROOT / m['source']
        frozen = RECEIPT.parent / 'sources' / source.name
        log = RECEIPT.parent / (source.stem + '.log')
        assert sha(source) == sha(frozen) == m['sha256'], source
        assert m['passed'] and m['exit_code'] == 0 and m['source_unchanged_during_check']
        assert re.findall(r"'([^']+)' does not depend on any axioms", log.read_text()) == m['empty_axiom_audits']
        dependencies = {name: [a.strip() for a in deps.split(',')]
                        for name, deps in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]", log.read_text())}
        assert dependencies == m['standard_axiom_audits']
        assert all(set(deps) == {'propext'} for deps in dependencies.values())
        assert len(m['empty_axiom_audits']) + len(dependencies) == m['expected_audits']
        assert 'warning:' not in log.read_text()
        bindings.append({'source': m['source'], 'sha256': m['sha256'],
                         'log_sha256': sha(log), 'audits': m['expected_audits']})
    all_new_names = []
    for filename, count in [('ExplanatoryJoining.lean', 23), ('ExplanatoryLocalUnits.lean', 31)]:
        new_source = (LEAN / filename).read_text()
        names = re.findall(r'^theorem (\w+)', new_source, re.M)
        assert len(names) == len(set(names)) == count
        module = next(m for m in receipt['modules'] if m['source'].endswith('/' + filename))
        audited = [name.rsplit('.', 1)[-1] for name in module['empty_axiom_audits'] + list(module['standard_axiom_audits'])]
        assert set(names) == set(audited)
        all_new_names.extend(names)
    assert len(all_new_names) == 54
    last = receipt['modules'][-1]
    assert 'Generative.ExplanatoryLocalUnits.chain_complete_iff_unit_matching_suffices' in last['empty_axiom_audits']
    assert len(last['empty_axiom_audits']) == 23 and len(last['standard_axiom_audits']) == 8
    assert len(receipt['modules'][-2]['empty_axiom_audits']) == 20
    assert len(receipt['modules'][-2]['standard_axiom_audits']) == 3
    first_path = LEAN / 'explanatory-joining-checks/20261007T225110.058337Z/receipt.json'
    first = json.loads(first_path.read_text())
    assert first['passed'] and first['total_declaration_audits'] == 97
    assert first['total_empty_axiom_audits'] == 82 and first['total_standard_axiom_audits'] == 15
    assert first['checker_sha256'] == sha(LEAN / 'check_explanatory_joining.py')
    final_modules = {m['source']: m for m in receipt['modules']}
    for m in first['modules']:
        assert m == final_modules[m['source']]
        source = ROOT / m['source']
        assert sha(first_path.parent / 'sources' / source.name) == m['sha256']
        assert sha(first_path.parent / (source.stem + '.log')) == sha(RECEIPT.parent / (source.stem + '.log'))
    data = chain.read_data()
    rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    assert edits['preserved_other_entries']
    for key, value in edits['rows_after'].items():
        assert rows[key] == value, key
    expected = chain.render(data).splitlines()
    rendered = chain.OUTPUT.read_text().splitlines()
    assert edits['scoped_render']['preserved_other_lines']
    for key in edits['rows_after']:
        assert [line for line in expected if line.startswith('| ' + key + ' |')] == [line for line in rendered if line.startswith('| ' + key + ' |')]
    pending = chain.changes(data)
    result = {'passed': True, 'scope': 'This study only; global index freshness is a separate concurrent maintenance check.',
              'new_theorems': 54, 'stage_theorems': [23, 31], 'inherited_audits': 74, 'total_declaration_audits': 128,
              'total_empty_axiom_audits': 105, 'propext_only_audits': 23, 'new_empty_audits': 43, 'new_propext_only_audits': 11,
              'first_stage_receipt': str(first_path.relative_to(ROOT)), 'first_stage_receipt_sha256': sha(first_path),
              'receipt': str(RECEIPT.relative_to(ROOT)), 'receipt_sha256': sha(RECEIPT),
              'local_links_checked': len(links), 'links': links,
              'source_and_frozen_log_bindings': bindings,
              'owned_rows': ['C30', 'F22'], 'preserved_other_entries_at_edit': True,
              'owned_rendered_rows_match': True, 'concurrent_global_changes': pending,
              'sha256': {str(p.relative_to(ROOT)): sha(p) for p in docs + [Path(__file__), HERE / 'EXPLANATORY-JOINING-INDEX-EDITS.json']}}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['passed', 'new_theorems', 'total_declaration_audits', 'total_empty_axiom_audits', 'propext_only_audits', 'local_links_checked']}))

if __name__ == '__main__':
    main()
