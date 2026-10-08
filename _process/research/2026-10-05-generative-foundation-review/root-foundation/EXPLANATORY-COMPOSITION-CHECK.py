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
OUTPUT = HERE / 'EXPLANATORY-COMPOSITION-CHECKS.json'
RECEIPT = LEAN / 'explanatory-composition-checks/20261007T223124.386181Z/receipt.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    docs = [ROOT / 'theories/becoming/chapters/EXPLANATORY-NECESSITY.md',
            ROOT / 'sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md',
            HERE / 'EXPLANATORY-COMPOSITION-INTEGRATION.md', HERE / 'EXPLANATORY-STRUCTURE-INTEGRATION.md']
    edits = json.loads((HERE / 'EXPLANATORY-COMPOSITION-INDEX-EDITS.json').read_text())
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
    assert receipt['passed'] and receipt['total_declaration_audits'] == 110 and receipt['total_empty_axiom_audits'] == 77 and receipt['total_standard_axiom_audits'] == 33
    assert receipt['checker_sha256'] == sha(LEAN / 'check_explanatory_composition.py')
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
        assert all(set(deps) <= {'propext', 'Quot.sound'} for deps in dependencies.values())
        assert len(m['empty_axiom_audits']) + len(dependencies) == m['expected_audits']
        assert 'warning:' not in log.read_text()
        bindings.append({'source': m['source'], 'sha256': m['sha256'],
                         'log_sha256': sha(log), 'audits': m['expected_audits']})
    all_new_names = []
    for filename, count in [('ExplanatoryComposition.lean', 36)]:
        new_source = (LEAN / filename).read_text()
        names = re.findall(r'^theorem (\w+)', new_source, re.M)
        assert len(names) == len(set(names)) == count
        module = next(m for m in receipt['modules'] if m['source'].endswith('/' + filename))
        audited = [name.rsplit('.', 1)[-1] for name in module['empty_axiom_audits'] + list(module['standard_axiom_audits'])]
        assert set(names) == set(audited)
        all_new_names.extend(names)
    assert len(all_new_names) == 36
    last = receipt['modules'][-1]
    assert 'Generative.ExplanatoryComposition.structural_unique_correspondence' in last['empty_axiom_audits']
    assert len(last['empty_axiom_audits']) == 15
    assert sum(set(a) == {'propext'} for a in last['standard_axiom_audits'].values()) == 18
    both = {n.rsplit('.', 1)[-1] for n, a in last['standard_axiom_audits'].items()
            if set(a) == {'propext', 'Quot.sound'}}
    assert both == {'canonical_reduced', 'reduced_presentation_exists', 'canonical_factorization'}
    assert sum(set(a) == {'propext'} for m in receipt['modules'] for a in m['standard_axiom_audits'].values()) == 30
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
              'new_theorems': 36, 'inherited_audits': 74, 'total_declaration_audits': 110,
              'total_empty_axiom_audits': 77, 'propext_only_audits': 30, 'propext_and_quot_sound_audits': 3,
              'receipt': str(RECEIPT.relative_to(ROOT)), 'receipt_sha256': sha(RECEIPT),
              'local_links_checked': len(links), 'links': links,
              'source_and_frozen_log_bindings': bindings,
              'owned_rows': ['C30', 'F22'], 'preserved_other_entries_at_edit': True,
              'owned_rendered_rows_match': True, 'concurrent_global_changes': pending,
              'sha256': {str(p.relative_to(ROOT)): sha(p) for p in docs + [Path(__file__), HERE / 'EXPLANATORY-COMPOSITION-INDEX-EDITS.json']}}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['passed', 'new_theorems', 'total_declaration_audits', 'total_empty_axiom_audits', 'propext_only_audits', 'propext_and_quot_sound_audits', 'local_links_checked']}))

if __name__ == '__main__':
    main()
